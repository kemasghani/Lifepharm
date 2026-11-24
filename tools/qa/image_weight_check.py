"""Draft check of every picture a shopper actually downloads: its bytes, its format, and whether it is larger
or smaller than the place it is shown needs. Phone (390 wide, 3x screen) and desktop (1440 wide, 2x). Read-only.

For each image on the page after a full scroll:
  heavy      more than HEAVY KB over the wire
  oversized  more pixels than 1.35 x what the slot can show on this screen (wasted bytes)
  soft       fewer pixels than 0.9 x what the slot needs at 2x (looks blurry on retina)
  old format served as PNG or JPEG although the picture is a photo that WebP or AVIF would carry in fewer bytes

Usage: uv run --no-project --with playwright python tools/qa/image_weight_check.py [us uk eu] [--live] [--json FILE]
       Set LP_CHROME if system Chrome is not installed. Exit code 1 when a page breaks its budget."""
import asyncio, json, os, sys
from playwright.async_api import async_playwright

STORES = {
    'uk': ('https://uk.lifepharm.com', '189821452674'),
    'us': ('https://shop.lifepharm.com', '193373995317'),
    'eu': ('https://europe.lifepharm.com', '168919728345'),
}
PATHS = ['/', '/collections/all', '/products/laminine', '/products/omega', '/products/cellnergy-wellness', '/products/lamiderm-apex-smart-serum', '/pages/science', '/pages/company']
VIEWS = (('phone', {'width': 390, 'height': 844}, 3, True), ('desktop', {'width': 1440, 'height': 900}, 2, False))
HEAVY = 150          # KB for one image
BUDGET = {'phone': 900, 'desktop': 1600}   # KB of images for one page after a full scroll
UA_PHONE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'
UA_DESK = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36'
LAUNCH = {'executable_path': os.environ['LP_CHROME']} if os.environ.get('LP_CHROME') else {'channel': 'chrome'}
LIVE = '--live' in sys.argv

SCROLL = r"""async () => { const step = innerHeight * .7; for (let y = 0; y < document.documentElement.scrollHeight; y += step) { scrollTo(0, y); await new Promise(r => setTimeout(r, 220)); } scrollTo(0, 0); }"""
IMAGES = r"""() => [...document.querySelectorAll('img')].filter(i => (i.currentSrc || i.src) && !i.closest('#preview-bar-iframe')).map(i => { const b = i.getBoundingClientRect();
  const where = i.closest('[class*="lp-"], [class*="product-"], [class*="stamped"], header, footer, [id^="shopify-section"]');
  return { src: i.currentSrc || i.src, natural: i.naturalWidth, shown: Math.round(b.width), shownH: Math.round(b.height), loading: i.getAttribute('loading'), sizes: i.getAttribute('sizes'),
    fit: getComputedStyle(i).objectFit, where: where ? String(where.className || where.tagName).split(' ')[0].slice(0, 40) : '' }; })"""


async def run(stores):
    over = 0
    report = {}
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, **LAUNCH)
        for store in stores:
            base, tid = STORES[store]
            for view, viewport, dpr, mobile in VIEWS:
                ctx = await browser.new_context(viewport=viewport, device_scale_factor=dpr, is_mobile=mobile, user_agent=UA_PHONE if mobile else UA_DESK)
                page = await ctx.new_page()
                seen = {}
                async def on_response(response):
                    try:
                        kind = (response.headers.get('content-type') or '').split(';')[0]
                        if kind.startswith('image/'):
                            size = int(response.headers.get('content-length') or 0) or len(await response.body())
                            seen[response.url] = (kind, size)
                    except Exception:
                        pass
                page.on('response', on_response)
                if not LIVE:
                    await page.goto(f'{base}/?preview_theme_id={tid}', wait_until='domcontentloaded'); await page.wait_for_timeout(1200)
                for path in PATHS:
                    seen.clear()
                    response = await page.goto(base + path, wait_until='load', timeout=90000)
                    if response.status >= 400: continue
                    await page.wait_for_timeout(1500); await page.evaluate(SCROLL); await page.wait_for_timeout(2500)
                    rows = []
                    for img in await page.evaluate(IMAGES):
                        kind, size = seen.get(img['src'], ('', 0))
                        if not size or img['src'].startswith('data:'): continue
                        need = img['shown'] * dpr
                        flags = []
                        if size > HEAVY * 1024: flags.append('heavy')
                        if img['shown'] > 0 and img['natural'] > need * 1.35 and img['natural'] - need > 120: flags.append('oversized')
                        if img['shown'] > 40 and img['natural'] < img['shown'] * min(dpr, 2) * 0.9: flags.append('soft')
                        if kind in ('image/png', 'image/jpeg') and size > 40 * 1024: flags.append('old format')
                        rows.append({'file': img['src'].split('/')[-1].split('?')[0][:52], 'host': img['src'].split('/')[2], 'kb': round(size / 1024), 'type': kind.replace('image/', ''), 'natural': img['natural'], 'shown': img['shown'], 'need': need, 'where': img['where'], 'loading': img['loading'], 'sizes': img['sizes'], 'flags': flags})
                    total = round(sum(size for _, size in seen.values()) / 1024)
                    flagged = [r for r in rows if r['flags']]
                    bad = total > BUDGET[view]
                    over += bad
                    report.setdefault(store, {}).setdefault(view, {})[path] = {'total_kb': total, 'images': len(seen), 'rows': rows}
                    print(f"{'FAIL' if bad else 'PASS'} {store} {view:7} {path:38} images {len(seen):3} · {total:5} KB (budget {BUDGET[view]}) · flagged {len(flagged)}")
                    for r in sorted(flagged, key=lambda r: -r['kb'])[:8]:
                        print(f"       {r['kb']:4} KB {r['type']:5} {r['natural']:5}px for {r['shown']:4}px slot (needs {r['need']:4})  {','.join(r['flags']):28} {r['where'][:26]:26} {r['file']}")
                await ctx.close()
        await browser.close()
    if '--json' in sys.argv:
        json.dump(report, open(sys.argv[sys.argv.index('--json') + 1], 'w'), indent=1)
    print('RESULT', 'PASS' if not over else f'FAIL ({over} pages over budget)'); sys.exit(1 if over else 0)

asyncio.run(run([a for a in sys.argv[1:] if a in STORES] or list(STORES)))
