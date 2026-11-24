"""Run PageSpeed Insights on a public address through pagespeed.web.dev and print what the score is made of.

The PageSpeed API refuses anonymous calls once its shared daily quota is used up, so this opens the public page in
Chrome, waits for the run and reads the Lighthouse result the page holds. Besides the simulated metrics the score
uses, it prints the observed ones (what the lab browser really measured): a late observed first paint points at
something on the page, a late simulated one at weight on the network.

Usage: uv run --no-project --with playwright python tools/perf/psi_run.py URL [URL ...] [--desktop] [--runs N] [--out DIR]
       An existing report can be read with --report https://pagespeed.web.dev/analysis/...
       With a Google API key (PSI_API_KEY in the environment or in .env; the PageSpeed Insights API is free) add --api:
       it calls the API instead of the page, needs no browser (plain python3) and is not held back by the anonymous quota.
       --api prints how many runs had a late first paint (TD-039).
       Set LP_CHROME if system Chrome is not installed. The address is sent to Google, so only use public pages.
       When PageSpeed answers "Unable to resolve" for an address that does open, its anonymous quota for this network
       is used up: run it by hand in a browser and read that report with --report, or use lh_run.py."""
import asyncio, json, os, re, sys, time, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ARGS = sys.argv[1:]
def opt(name, default=None):
    return ARGS[ARGS.index(name) + 1] if name in ARGS else default
FORM = 'desktop' if '--desktop' in ARGS else 'mobile'
RUNS = int(opt('--runs', 1))
OUT = opt('--out', os.path.join(os.path.dirname(__file__), 'reports'))
REPORT = opt('--report')
URLS = [a for i, a in enumerate(ARGS) if a.startswith('http') and (i == 0 or ARGS[i - 1] not in ('--report',))]
LAUNCH = {'executable_path': os.environ['LP_CHROME']} if os.environ.get('LP_CHROME') else {'channel': 'chrome'}
from lhr import summary


async def read(page, address, wait):
    await page.goto(address, wait_until='domcontentloaded', timeout=90000)
    key = '__LIGHTHOUSE_MOBILE_JSON__' if FORM == 'mobile' else '__LIGHTHOUSE_DESKTOP_JSON__'
    end = time.time() + wait
    while time.time() < end:
        await page.wait_for_timeout(2500)
        if await page.evaluate(f"!!(window.{key} && (window.{key}.lighthouseResult || window.{key}).audits)"):
            return json.loads(await page.evaluate(f"JSON.stringify(window.{key})"))
        text = await page.evaluate("document.body.innerText")
        if re.search(r'(Oops|Lighthouse returned error|Unable to resolve|Try again)', text) and 'Running analysis' not in text:
            raise RuntimeError(re.sub(r'\s+', ' ', text)[-300:])
    raise TimeoutError('PageSpeed did not finish in time')


def api_key():
    key = os.environ.get('PSI_API_KEY')
    env = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '.env')
    if not key and os.path.exists(env):
        for line in open(env, encoding='utf-8'):
            if line.strip().startswith('PSI_API_KEY='): key = line.split('=', 1)[1].strip().strip('"\'')
    return key


def run_api():
    import urllib.request
    key = api_key()
    if not key: sys.exit('PSI_API_KEY is not set (environment or .env)')
    os.makedirs(OUT, exist_ok=True); late = total = 0
    for target in URLS:
        for i in range(RUNS):
            q = urllib.parse.urlencode([('url', target), ('strategy', FORM), ('category', 'performance'), ('key', key)])
            try:
                lh = json.load(urllib.request.urlopen('https://www.googleapis.com/pagespeedonline/v5/runPagespeed?' + q, timeout=180))
            except Exception as error:
                print(f"== {target}\n   FAILED    {str(error)[:200]}"); continue
            m = lh['lighthouseResult']['audits']['metrics']['details']['items'][0]; total += 1; late += m.get('observedFirstPaint', 0) > 1500
            name = re.sub(r'[^a-z0-9]+', '-', target.lower()).strip('-')[-70:]
            path = os.path.join(OUT, f"psi-{name}-{FORM}-{time.strftime('%Y%m%d-%H%M%S')}.json"); json.dump(lh, open(path, 'w'))
            print(f"== {target} (run {i + 1})\n{summary(lh)}\n   saved     {path}"); time.sleep(3)
    print(f'LATE FIRST PAINT (observed after 1.5 s): {late} of {total} runs')


async def main():
    from playwright.async_api import async_playwright
    os.makedirs(OUT, exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, **LAUNCH)
        jobs = [(REPORT, REPORT)] if REPORT else [(u, 'https://pagespeed.web.dev/analysis?url=' + urllib.parse.quote(u, safe='') + '&form_factor=' + FORM) for u in URLS for _ in range(RUNS)]
        for target, address in jobs:
            page = await browser.new_page(viewport={'width': 1300, 'height': 900})
            try:
                lh = await read(page, address, 60 if REPORT else 240)
                name = re.sub(r'[^a-z0-9]+', '-', (lh.get('lighthouseResult', lh).get('requestedUrl') or target).lower()).strip('-')[-70:]
                path = os.path.join(OUT, f"psi-{name}-{FORM}-{time.strftime('%Y%m%d-%H%M%S')}.json")
                json.dump(lh, open(path, 'w'))
                print(f"== {target}\n{summary(lh)}\n   saved     {path}\n   report    {page.url}")
            except Exception as error:
                print(f"== {target}\n   FAILED    {str(error)[:300]}")
            await page.close()
        await browser.close()

if not (URLS or REPORT):
    sys.exit(__doc__)
if '--api' in ARGS:
    run_api()
else:
    asyncio.run(main())
