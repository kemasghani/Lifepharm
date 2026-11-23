"""Draft check of the product rating row, at 1440 and 390. Read-only: it never submits a form.
A product with reviews shows its Stamped stars. A product with none must show no empty stars and, from real
Stamped data, either "Includes <product>, rated ..." (packs) or the store-wide review count. Reports what
is visible, the link target, the tap area, horizontal scroll and new JS errors.
Output: <outdir>/<store>-rating-row.json plus one screenshot per page.

Usage: uv run --no-project --with playwright python tools/qa/pdp_rating_row_check.py <outdir> <base_url> <theme_id> <expect> ...
       <expect> is handle:stars, handle:brand, handle:none or handle:included=<lead product handle>.
       Set LP_CHROME if system Chrome is not installed."""
import asyncio, json, os, sys
from playwright.async_api import async_playwright

OUT, BASE, TID = sys.argv[1], sys.argv[2], sys.argv[3]
EXPECT = dict(a.split(':', 1) for a in sys.argv[4:])
TAG = BASE.split('//')[1].split('.')[0]
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36'
LAUNCH = {'executable_path': os.environ['LP_CHROME']} if os.environ.get('LP_CHROME') else {'channel': 'chrome'}
NOISE = ['e is not a function', 'shouldShowBanner', 'stamped', 'tolstoy', 'klaviyo', 'ResizeObserver loop', 'Script error', 'weglot', 'clarity',
         'intelligems', 'triplewhale', 'pandectes', 'skio', 'gorgias', 'Failed to load resource', 'unload is not allowed', 'shop.app', 'Failed to fetch']

STATE = r"""
() => {
  const row = document.querySelector('.shopify-section--main-product .lp-rating-row');
  if (!row) return { row: false, theme: window.Shopify && Shopify.theme && Shopify.theme.id, path: location.pathname };
  const vis = (el) => !!el && el.getClientRects().length > 0 && getComputedStyle(el).visibility !== 'hidden';
  const t = (el) => el ? el.textContent.replace(/\s+/g, ' ').trim() : null;
  const badge = row.querySelector('.stamped-badge'), stars = row.querySelector('.stamped-starrating'), proof = row.querySelector('.lp-proof');
  const title = document.querySelector('.shopify-section--main-product .product-info__title, .shopify-section--main-product h1');
  const r = vis(proof) ? proof.getBoundingClientRect() : null, tr = title ? title.getBoundingClientRect() : null;
  const after = proof && proof.tagName === 'A' ? getComputedStyle(proof, '::after') : null;
  const starsEl = proof && proof.querySelector('.lp-proof__stars'), mark = proof && proof.querySelector('.lp-proof__mark');
  const text = proof && proof.querySelector('.lp-proof__text');
  return {
    row: true, theme: Shopify.theme.id, path: location.pathname,
    stamped: badge ? { rating: badge.getAttribute('data-rating'), visible: vis(stars), caption: t(row.querySelector('.stamped-badge-caption')) } : null,
    proof: vis(proof) ? {
      kind: proof.classList.contains('lp-proof--included') ? 'included' : 'brand', text: t(text), href: proof.getAttribute('href'),
      box: { x: Math.round(r.left), y: Math.round(r.top + scrollY), w: Math.round(r.width), h: Math.round(r.height) }, lines: text ? text.getClientRects().length : 0,
      font: getComputedStyle(proof).fontSize + ' ' + getComputedStyle(proof).fontWeight + ' ' + getComputedStyle(proof).color,
      tapHeight: after ? Math.round(parseFloat(after.height)) : null,
      stars: starsEl ? { w: Math.round(starsEl.getBoundingClientRect().width), fill: getComputedStyle(starsEl).getPropertyValue('--lp-stars').trim(), masked: getComputedStyle(starsEl).webkitMaskImage !== 'none' } : null,
      mark: mark ? { w: Math.round(mark.getBoundingClientRect().width), masked: getComputedStyle(mark).webkitMaskImage !== 'none' } : null,
      underTitle: tr ? Math.round(r.top - tr.bottom) : null, right: Math.round(r.right),
    } : null,
    rowBox: { h: Math.round(row.getBoundingClientRect().height), right: Math.round(row.getBoundingClientRect().right) },
    vw: innerWidth, hscroll: document.documentElement.scrollWidth > innerWidth + 1,
  };
}
"""

def judge(st, want):
    if not st.get('row') or str(st.get('theme')) != TID or st['hscroll'] or st['errors']: return False
    stamped, proof = st['stamped'], st['proof']
    empty_stars = bool(stamped and stamped['visible'] and stamped['rating'] in ('0.0', '0', None))
    if empty_stars: return False
    if want == 'stars': return bool(stamped and stamped['visible']) and proof is None
    if want == 'none': return proof is None and not (stamped and stamped['visible'])
    if proof is None or (stamped and stamped['visible']): return False
    if proof['right'] > st['vw'] or not (0 <= (proof['underTitle'] or 0) <= 40): return False
    if want == 'brand': return proof['kind'] == 'brand' and bool(proof['mark'] and proof['mark']['masked']) and 'reviews across LifePharm' in proof['text']
    lead = want.split('=', 1)[1]
    return (proof['kind'] == 'included' and proof['href'].split('?')[0].endswith(f'/products/{lead}') and '#' not in proof['href'] and proof['text'].startswith('Includes ')
            and bool(proof['stars'] and proof['stars']['masked']) and (proof['tapHeight'] or 0) >= 44)

async def main():
    os.makedirs(OUT, exist_ok=True); results = []; ok = True
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, **LAUNCH)
        for name, vp in (('1440', {'width': 1440, 'height': 900}), ('390', {'width': 390, 'height': 844})):
            ctx = await browser.new_context(viewport=vp, user_agent=UA, device_scale_factor=2)
            page = await ctx.new_page(); errors = []
            page.on('pageerror', lambda e: errors.append(str(e)))
            await page.goto(f'{BASE}/?preview_theme_id={TID}', wait_until='domcontentloaded')
            for handle, want in EXPECT.items():
                errors.clear()
                await page.goto(f'{BASE}/products/{handle}', wait_until='domcontentloaded')
                try: await page.wait_for_selector('.lp-rating-row .stamped-badge', state='attached', timeout=9000)
                except Exception: pass
                await page.wait_for_timeout(1500)
                st = await page.evaluate(STATE)
                st.update(handle=handle, viewport=name, want=want, errors=[e[:140] for e in errors if not any(n.lower() in e.lower() for n in NOISE)])
                st['pass'] = bool(judge(st, want)); ok = ok and st['pass']; results.append(st)
                try:
                    await page.evaluate("document.querySelector('.shopify-section--main-product .lp-rating-row')?.scrollIntoView({block: 'center'})")
                    await page.wait_for_timeout(300); await page.screenshot(path=os.path.join(OUT, f'{TAG}-rating-{handle}-{name}.png'))
                except Exception: pass
                print(('PASS ' if st['pass'] else 'FAIL ') + json.dumps({k: st.get(k) for k in ('viewport', 'handle', 'want', 'stamped', 'proof', 'rowBox', 'hscroll', 'errors', 'theme', 'row')}))
            await ctx.close()
        await browser.close()
    json.dump(results, open(os.path.join(OUT, f'{TAG}-rating-row.json'), 'w'), indent=1)
    print('RESULT', 'PASS' if ok else 'FAIL', f'({sum(r["pass"] for r in results)}/{len(results)})')
    sys.exit(0 if ok else 1)

asyncio.run(main())
