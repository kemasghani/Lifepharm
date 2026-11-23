"""Draft check of the HSA/FSA payment note on product pages, at 1440 and 390. Read-only: it never submits a form.
For each product handle it reports whether the note shows, how many times HSA/FSA is mentioned in the buy box
(must be 0 or 1), where the note sits (under the trust tiles, above the Shop Pay line), the icon, horizontal
scroll and new JS errors. Output: <outdir>/<store>-payment-note.json plus one buy-box screenshot per page.

Usage: uv run --no-project --with playwright python tools/qa/pdp_payment_note_check.py <outdir> <base_url> <theme_id> <expect> ...
       <expect> is handle:yes or handle:no (note expected or not). Set LP_CHROME if system Chrome is not installed."""
import asyncio, json, os, sys
from playwright.async_api import async_playwright

OUT, BASE, TID = sys.argv[1], sys.argv[2], sys.argv[3]
EXPECT = dict(a.rsplit(':', 1) for a in sys.argv[4:])
TAG = BASE.split('//')[1].split('.')[0]
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36'
LAUNCH = {'executable_path': os.environ['LP_CHROME']} if os.environ.get('LP_CHROME') else {'channel': 'chrome'}
NOISE = ['e is not a function', 'shouldShowBanner', 'stamped', 'tolstoy', 'klaviyo', 'ResizeObserver loop', 'Script error', 'weglot', 'clarity',
         'intelligems', 'triplewhale', 'pandectes', 'skio', 'gorgias', 'Failed to load resource', 'unload is not allowed', 'shop.app', 'Failed to fetch']

STATE = r"""
() => {
  const info = document.querySelector('.shopify-section--main-product .product-info');
  if (!info) return { info: false, theme: window.Shopify && Shopify.theme && Shopify.theme.id, title: document.title, path: location.pathname };
  const top = (el) => el ? Math.round(el.getBoundingClientRect().top + scrollY) : null;
  const note = info.querySelector('.lp-pay-note'), img = note && note.querySelector('img');
  const mentions = [...info.querySelectorAll('*')].filter(el => el.children.length === 0 || el.matches('p, .product-info__liquid'))
    .filter(el => /HSA\s*\/\s*FSA/i.test(el.textContent) && ![...el.children].some(c => /HSA\s*\/\s*FSA/i.test(c.textContent)) && el.offsetParent !== null);
  const terms = info.querySelector('.product-info__payment-terms'), trust = info.querySelector('.lp-trust-row'), buy = info.querySelector('.product-info__buy-buttons');
  const r = note && note.getBoundingClientRect();
  return {
    info: true, theme: Shopify.theme.id, path: location.pathname, template: (document.body.className.match(/template-[\w-]+/g) || []).join(' '),
    note: !!note, text: note ? note.textContent.replace(/\s+/g, ' ').trim() : null, mentions: mentions.length,
    font: note ? getComputedStyle(note).fontSize + ' ' + getComputedStyle(note).color : null,
    box: r ? { x: Math.round(r.left), w: Math.round(r.width), h: Math.round(r.height) } : null,
    icon: img ? { loaded: img.complete && img.naturalWidth > 0, natural: img.naturalWidth, shown: Math.round(img.getBoundingClientRect().width) + 'x' + Math.round(img.getBoundingClientRect().height), src: img.currentSrc.split('?')[0].split('/').pop() } : null,
    order: { buy: top(buy), trust: top(trust), note: top(note), shopPay: terms && terms.offsetHeight ? top(terms) : null },
    vw: innerWidth, hscroll: document.documentElement.scrollWidth > innerWidth + 1,
  };
}
"""

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
                await page.wait_for_timeout(3500)
                st = await page.evaluate(STATE)
                st.update(handle=handle, viewport=name, want=want, errors=[e[:140] for e in errors if not any(n.lower() in e.lower() for n in NOISE)])
                good = st.get('info') and str(st.get('theme')) == TID and st['note'] == (want == 'yes') and st['mentions'] == (1 if want == 'yes' else 0) and not st['hscroll'] and not st['errors']
                if good and want == 'yes':
                    o = st['order']; good = bool(st['icon'] and st['icon']['loaded']) and o['trust'] < o['note'] and (o['shopPay'] is None or o['note'] < o['shopPay'])
                st['pass'] = bool(good); ok = ok and st['pass']; results.append(st)
                target = page.locator('.lp-pay-note').first if st.get('note') else page.locator('.product-info__buy-buttons').first
                try:
                    await target.scroll_into_view_if_needed(timeout=3000); await page.wait_for_timeout(300)
                    await page.screenshot(path=os.path.join(OUT, f'{TAG}-note-{handle}-{name}.png'))
                except Exception:
                    pass
                print(('PASS ' if st['pass'] else 'FAIL ') + json.dumps({k: st.get(k) for k in ('viewport', 'handle', 'want', 'note', 'mentions', 'text', 'icon', 'order', 'font', 'hscroll', 'errors', 'theme', 'template', 'info', 'title')}))
            await ctx.close()
        await browser.close()
    json.dump(results, open(os.path.join(OUT, f'{TAG}-payment-note.json'), 'w'), indent=1)
    print('RESULT', 'PASS' if ok else 'FAIL', f'({sum(r["pass"] for r in results)}/{len(results)})')
    sys.exit(0 if ok else 1)

asyncio.run(main())
