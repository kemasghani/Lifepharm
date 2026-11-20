#!/usr/bin/env python3
"""Full-coverage storefront QA of a draft theme: every published product, collection, page, blog and article,
plus the system pages, at 390px and 1440px. Read-only (never submits a form or places an order).

    uv run --with playwright python tools/qa/site_qa.py --store us            # one store
    uv run --with playwright python tools/qa/site_qa.py --store all --widths 1440,390

Per URL it records: HTTP status, served theme id, page errors (known third-party noise tagged), broken images,
horizontal scroll, 'Liquid error' / 'translation missing' text, placeholder images, empty LP sections and, on product
pages, title / price / add-to-cart / gallery / Ideal For icons. Then it checks every internal link it saw for 404s.
Report: tools/qa/reports/<store>-<date>.json and a printed summary.
"""
import argparse, asyncio, datetime, json, os, re, sys, time, urllib.request, urllib.error
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'store-audit'))
from shopify import gql  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
STORES = {
    'uk': ('https://uk.lifepharm.com', '189821452674'),
    'us': ('https://shop.lifepharm.com', '193373995317'),
    'eu': ('https://europe.lifepharm.com', '168919728345'),
}
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36'
DELAY = 2.5
NOISE = [r'e is not a function', r'shouldShowBanner', r'stamped', r'tolstoy', r'klaviyo', r'ResizeObserver loop',
         r'Script error', r'weglot', r'clarity', r'intelligems', r'triplewhale', r'pandectes', r'skio']

PAGE_JS = r"""
() => {
  const txt = document.body ? document.body.innerText : '';
  const imgs = [...document.querySelectorAll('main img, header img, footer img')].filter(i => i.offsetParent !== null || i.closest('[data-lp-reveal]'));
  const broken = imgs.filter(i => i.currentSrc && i.complete && i.naturalWidth === 0).map(i => (i.currentSrc || i.src).split('/').pop().split('?')[0]);
  const unloaded = imgs.filter(i => !i.complete && i.loading !== 'lazy').length;
  const lpEmpty = [...document.querySelectorAll('main .shopify-section')].filter(s => s.querySelector('[class^="lp-"], [class*=" lp-"]') && s.offsetHeight > 0 && s.innerText.trim().length < 3 && !s.querySelector('img, video, iframe')).map(s => s.id.split('__').pop());
  const out = {
    theme: (window.Shopify && Shopify.theme && Shopify.theme.id) || null,
    title: document.title,
    hscroll: document.documentElement.scrollWidth > window.innerWidth + 1,
    liquidError: (txt.match(/Liquid (syntax )?error[^\n]{0,80}/i) || [null])[0],
    translationMissing: (txt.match(/translation missing[^\n]{0,60}/i) || [null])[0],
    placeholders: document.querySelectorAll('main svg.placeholder-svg, main .placeholder-svg').length,
    brokenImages: broken, unloadedEager: unloaded, emptyLpSections: lpEmpty,
    mainText: (document.querySelector('main') || document.body).innerText.trim().length,
  };
  if (document.querySelector('.shopify-section--main-product')) {
    const ideal = [...document.querySelectorAll('.lp-ideal__item')];
    out.product = {
      title: !!(document.querySelector('.product-info__title, .product-title, h1') || {}).innerText,
      price: !!document.querySelector('.product-info__price sale-price, .price-list sale-price, sale-price'),
      atc: !!document.querySelector('form[action*="/cart/add"] button[type="submit"], buy-buttons button[type="submit"]'),
      gallery: document.querySelectorAll('.product-gallery__media img').length,
      idealItems: ideal.length,
      idealIconsOk: ideal.filter(i => { const m = i.querySelector('img'); return m && m.naturalWidth > 0; }).length,
      idealRows: [...new Set(ideal.map(i => Math.round(i.getBoundingClientRect().top)))].length,
      summary: !!document.querySelector('.lp-pdp-summary'),
    };
  }
  out.links = [...new Set([...document.querySelectorAll('a[href]')].map(a => a.getAttribute('href')).filter(h => h && h.startsWith('/') && !h.startsWith('//')).map(h => h.split('#')[0].split('?')[0]).filter(Boolean))];
  return out;
}
"""


def discover(store):
    q = '''{products(first:250,query:"status:active"){nodes{handle onlineStoreUrl}}
      collections(first:250){nodes{handle}}
      pages(first:250){nodes{handle isPublished}}
      blogs(first:20){nodes{handle articles(first:250){nodes{handle isPublished}}}}}'''
    d = gql(store, q)['data']
    urls = ['/', '/collections', '/collections/all', '/search?q=laminine', '/cart', '/account/login', '/account/register',
            '/pages/does-not-exist-qa', '/policies/privacy-policy', '/policies/refund-policy', '/policies/terms-of-service']
    urls += [f"/products/{p['handle']}" for p in d['products']['nodes'] if p['onlineStoreUrl']]
    urls += [f"/collections/{c['handle']}" for c in d['collections']['nodes']]
    urls += [f"/pages/{p['handle']}" for p in d['pages']['nodes'] if p['isPublished']]
    for b in d['blogs']['nodes']:
        urls.append(f"/blogs/{b['handle']}")
        urls += [f"/blogs/{b['handle']}/{a['handle']}" for a in b['articles']['nodes'] if a['isPublished']]
    return list(dict.fromkeys(urls))


async def check(browser, base, tid, path, width, sem):
    async with sem:
        ctx = await browser.new_context(viewport={'width': width, 'height': 900 if width > 500 else 844}, user_agent=UA)
        page = await ctx.new_page()
        errors = []
        page.on('pageerror', lambda e: errors.append(str(e)[:160]))
        sep = '&' if '?' in path else '?'
        rec = {'path': path, 'width': width}
        for attempt in range(4):
            try:
                resp = await page.goto(f'{base}{path}{sep}preview_theme_id={tid}', wait_until='load', timeout=90000)
                rec['status'] = resp.status if resp else None
                title = await page.title()
                if rec['status'] == 429 or 'just a moment' in title.lower():
                    rec['status'] = 'CHALLENGE'
                    print(f'  rate limited on {path}, cooling down', flush=True)
                    await asyncio.sleep(120 * (attempt + 1)); continue
                break
            except Exception as e:  # noqa: BLE001
                rec['status'] = f'ERR {str(e)[:80]}'
                await asyncio.sleep(5)
        try:
            await page.wait_for_timeout(1500)
            h = await page.evaluate('document.body.scrollHeight')
            for y in range(0, min(h, 30000), 700):
                await page.evaluate(f'window.scrollTo(0,{y})'); await page.wait_for_timeout(60)
            await page.wait_for_timeout(1200)
            rec.update(await page.evaluate(PAGE_JS))
        except Exception as e:  # noqa: BLE001
            rec['evalError'] = str(e)[:120]
        rec['errors'] = [e for e in errors if not any(re.search(n, e, re.I) for n in NOISE)]
        rec['noise'] = len(errors) - len(rec['errors'])
        await ctx.close()
        await asyncio.sleep(DELAY)
        return rec


async def html_checks(browser, base, tid, paths):
    """One plain request per URL with the preview cookie: status, served theme, Liquid errors, missing translations."""
    ctx = await browser.new_context(user_agent=UA)
    page = await ctx.new_page()
    await page.goto(f'{base}/?preview_theme_id={tid}', wait_until='load', timeout=90000)
    out = []
    for p in paths:
        rec = {'path': p, 'width': 'html'}
        for attempt in range(4):
            r = await ctx.request.get(base + p, timeout=60000)
            body = await r.text()
            if r.status == 429 or 'Just a moment' in body[:3000]:
                print(f'  rate limited on {p}, cooling down', flush=True)
                await asyncio.sleep(120 * (attempt + 1)); continue
            break
        rec['status'] = r.status
        m = re.search(r'Shopify\.theme\s*=\s*(\{.*?\});', body)
        rec['theme'] = (json.loads(m.group(1)).get('id') if m else None)
        rec['liquidError'] = (re.search(r'Liquid (syntax )?error[^<]{0,80}', body) or [None])[0]
        rec['translationMissing'] = (re.search(r'translation missing[^<]{0,60}', body) or [None])[0]
        rec['mainText'] = len(re.sub(r'<[^>]+>', ' ', body.split('<main', 1)[-1].split('</main>', 1)[0]).split())
        out.append(rec)
        await asyncio.sleep(1.2)
    await ctx.close()
    return out


def link_status(base, paths):
    out = {}
    for p in paths:
        req = urllib.request.Request(base + p, headers={'User-Agent': UA}, method='GET')
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                out[p] = r.status
        except urllib.error.HTTPError as e:
            out[p] = e.code
        except Exception as e:  # noqa: BLE001
            out[p] = f'ERR {str(e)[:40]}'
        time.sleep(1.0)
    return out


def problems(rec, tid):
    p = []
    st = rec.get('status')
    expect_404 = rec['path'] == '/pages/does-not-exist-qa'
    if st != 200 and not (expect_404 and st == 404):
        p.append(f'status {st}')
    if rec.get('theme') and str(rec['theme']) != tid:
        p.append(f"served theme {rec['theme']}")
    for k in ('hscroll', 'liquidError', 'translationMissing'):
        if rec.get(k):
            p.append(f'{k}: {rec[k]}')
    if rec.get('brokenImages'):
        p.append(f"broken images {rec['brokenImages'][:4]}")
    if rec.get('placeholders'):
        p.append(f"{rec['placeholders']} placeholder image(s)")
    if rec.get('emptyLpSections'):
        p.append(f"empty LP sections {rec['emptyLpSections']}")
    if rec.get('errors'):
        p.append(f"JS errors {rec['errors'][:2]}")
    if rec.get('evalError'):
        p.append(f"eval {rec['evalError']}")
    pr = rec.get('product')
    if pr:
        for k in ('title', 'price', 'atc'):
            if not pr[k]:
                p.append(f'product missing {k}')
        if pr['gallery'] == 0:
            p.append('product has no gallery image')
        if pr['idealItems'] and pr['idealIconsOk'] < pr['idealItems']:
            p.append(f"Ideal For icons {pr['idealIconsOk']}/{pr['idealItems']}")
        if pr['idealItems'] and pr['idealRows'] > 1 and rec['width'] > 500:
            p.append(f"Ideal For wraps into {pr['idealRows']} rows")
    if rec.get('mainText', 1) < (10 if rec['width'] == 'html' else 40) and not rec.get('product'):
        p.append(f"almost no content ({rec.get('mainText')} chars)")
    return p


async def run_store(store, widths, conc):
    base, tid = STORES[store]
    urls = discover(store)
    print(f'[{store}] {len(urls)} urls x {len(widths)} widths', flush=True)
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(channel='chrome')
        sem = asyncio.Semaphore(conc)
        articles = [u for u in urls if u.count('/') == 3 and u.startswith('/blogs/')]
        full = [u for u in urls if u not in articles]
        # every article gets the light HTML check; the first three also get the full browser check (same template)
        full += articles[:3]
        print(f'[{store}] browser: {len(full)} urls x {len(widths)}, html-only: {len(articles)} articles', flush=True)
        html_results = await html_checks(browser, base, tid, articles) if articles else []
        tasks = [check(browser, base, tid, u, w, sem) for u in full for w in widths]
        results = []
        for i, fut in enumerate(asyncio.as_completed(tasks), 1):
            results.append(await fut)
            if i % 25 == 0:
                print(f'[{store}] {i}/{len(tasks)}', flush=True)
        await browser.close()
    results += html_results
    links = sorted({l for r in results for l in r.get('links', []) if not l.startswith(('/cart/', '/account', '/checkout', '/apps/', '/cdn/', '/search', '/policies'))})
    linkres = link_status(base, links)
    for r in results:
        r['problems'] = problems(r, tid)
        r.pop('links', None)
    bad_links = {k: v for k, v in linkres.items() if v != 200}
    report = {'store': store, 'theme': tid, 'date': datetime.date.today().isoformat(), 'urls': len(urls),
              'checks': len(results), 'results': sorted(results, key=lambda r: (r['path'], str(r['width']))),
              'links_checked': len(links), 'bad_links': bad_links}
    os.makedirs(os.path.join(HERE, 'reports'), exist_ok=True)
    path = os.path.join(HERE, 'reports', f"{store}-{report['date']}.json")
    json.dump(report, open(path, 'w'), indent=1)
    flagged = [r for r in results if r['problems']]
    print(f'\n[{store}] {len(results)} checks, {len(flagged)} with problems, {len(links)} links, {len(bad_links)} bad links -> {path}')
    for r in sorted(flagged, key=lambda r: r['path']):
        print(f"  {str(r['width']):>4} {r['path']}: " + ' | '.join(r['problems']))
    for k, v in bad_links.items():
        print(f'  LINK {v} {k}')
    return report


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--store', default='all')
    ap.add_argument('--widths', default='1440,390')
    ap.add_argument('--concurrency', type=int, default=1)
    a = ap.parse_args()
    widths = [int(x) for x in a.widths.split(',')]
    for s in (STORES if a.store == 'all' else [a.store]):
        asyncio.run(run_store(s, widths, a.concurrency))


if __name__ == '__main__':
    main()
