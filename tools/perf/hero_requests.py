"""Which homepage hero files does Chrome fetch, when, and how sharp is the result, on phones, a fold-out, a tablet and
desktop (fresh profile each). The hero is preloaded from <head> (D-085); a preload whose srcset, sizes or media differs
from the picture's fetches a second file without anything looking broken (L-077). Read-only.

PASS for a set-up means: one hero file and at least 1.9x the slot on a phone.

Usage: uv run --no-project --with playwright python tools/perf/hero_requests.py URL
       A draft is checked with URL?preview_theme_id=<id>. Set LP_CHROME if system Chrome is not installed."""
import asyncio, json, os, sys
from playwright.async_api import async_playwright
URL = sys.argv[1] if len(sys.argv) > 1 else sys.exit(__doc__)
LAUNCH = {'executable_path': os.environ['LP_CHROME']} if os.environ.get('LP_CHROME') else {'channel': 'chrome'}
FAILED = []
AND = 'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36'
MAC = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
VIEWS = (('phone 412 @1.75 (Moto G, PageSpeed)', {'width': 412, 'height': 823}, 1.75, True, AND, None),
         ('phone 390 @3 (iPhone size)', {'width': 390, 'height': 844}, 3, True, AND, None),
         ('phone 412 @2.625 (Pixel)', {'width': 412, 'height': 915}, 2.625, True, AND, None),
         ('phone 360 @2', {'width': 360, 'height': 740}, 2, True, AND, None),
         ('fold-out 673 @2.6', {'width': 673, 'height': 841}, 2.6, True, AND, None),
         ('tablet 820 @2', {'width': 820, 'height': 1180}, 2, True, AND, None),
         ('desktop 1440 @2', {'width': 1440, 'height': 900}, 2, False, MAC, None),
         ('desktop window 600 wide on a 1440 screen', {'width': 600, 'height': 800}, 2, False, MAC, {'width': 1440, 'height': 900}))
async def main():
    async with async_playwright() as p:
        for name, vp, dpr, mobile, ua, screen in VIEWS:
            b = await p.chromium.launch(headless=True, **LAUNCH)
            ctx = await b.new_context(viewport=vp, device_scale_factor=dpr, is_mobile=mobile, has_touch=mobile, user_agent=ua, **({'screen': screen} if screen else {}))
            page = await ctx.new_page(); cdp = await ctx.new_cdp_session(page); await cdp.send('Network.enable')
            seen = {}; hints = []
            cdp.on('Network.requestWillBeSent', lambda e: seen.setdefault(e['requestId'], {'url': e['request']['url'], 'start': e['timestamp'], 'init': e.get('initiator', {}).get('type'), 'prio': e['request'].get('initialPriority')}))
            cdp.on('Network.responseReceived', lambda e: seen.get(e['requestId'], {}).update({'cache': e['response'].get('fromDiskCache') or e['response'].get('fromPrefetchCache'), 'status': e['response']['status'], 'mime': e['response'].get('mimeType')}))
            cdp.on('Network.loadingFinished', lambda e: seen.get(e['requestId'], {}).update({'end': e['timestamp'], 'bytes': e.get('encodedDataLength')}))
            cdp.on('Network.responseReceivedEarlyHints', lambda e: hints.append(len(json.dumps(e.get('headers', {})))))
            await page.goto(URL, wait_until='load', timeout=90000); await page.wait_for_timeout(2500)
            t0 = min(r['start'] for r in seen.values())
            info = await page.evaluate("""() => { const i = document.querySelector('.lp-hh__img'); const e = performance.getEntriesByType('resource').filter(r => /lp-home-hero/.test(r.name)).map(r => [r.name.split('/').pop().replace(/\\?v=\\d+/, ''), Math.round(r.startTime), Math.round(r.responseEnd), r.transferSize, r.initiatorType]);
              const lcp = performance.getEntriesByType('largest-contentful-paint').pop(); const nav = performance.getEntriesByType('navigation')[0];
              return { current: i.currentSrc.split('/').pop().replace(/\\?v=\\d+/, ''), natural: i.naturalWidth, shown: Math.round(i.getBoundingClientRect().width), entries: e, ttfb: Math.round(nav.responseStart), fcp: Math.round(performance.getEntriesByName('first-contentful-paint')[0]?.startTime || 0) } }""")
            real = int(info['current'].split('width=')[-1]) if 'width=' in info['current'] else 0
            files = [r for r in seen.values() if 'lp-home-hero' in r['url'] or info['current'].split('&')[0] in r['url']]
            big = [r for r in files if not r['url'].endswith('width=50')]
            ok = len(big) == 1 and (not mobile or vp['width'] >= 520 or real / max(1, info['shown']) >= 1.9)
            if not ok: FAILED.append(name)
            print(f"{'PASS' if ok else 'FAIL'} {name} | TTFB {info['ttfb']} ms | FCP {info['fcp']} ms | img uses {info['current'].replace('lp-home-hero-', '')} for a {info['shown']}px slot = {round(real / max(1, info['shown']), 2)}x")
            for r in sorted(files, key=lambda r: r['start']):
                if True:
                    print(f"     {round((r['start'] - t0) * 1000):5} -> {round((r.get('end', r['start']) - t0) * 1000):5} ms  {round((r.get('bytes') or 0) / 1024, 1):5} KB  {r.get('prio'):6} {r['url'].split('/')[-1].split('?')[0].replace('lp-home-hero-', '')[:22]} {r['url'].split('width=')[-1]}w")
            
            await b.close()
asyncio.run(main())
print('RESULT', 'PASS' if not FAILED else f'FAIL ({len(FAILED)}: ' + ', '.join(FAILED) + ')'); sys.exit(1 if FAILED else 0)
