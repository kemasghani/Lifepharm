"""Draft check that the offer and the price agree on a product page, at 1440 and 390. Read-only: nothing is added to the cart.
For every size card: select it, then compare the card's "Save" badge with the Add to Cart button
(struck price minus price must equal the badge; no badge means no struck price), with the plan picker's
One-time row (same struck price) and with the sticky bar (same price per unit as the size card, or "In stock"
when the size is not sold by the unit). Then, where the page has a Subscribe & Save option, select it and
check the button and the subscription row strike the same price as the One-time row (D-091), or the one-time
price when the size has no reference price.
Output: one line per size and a screenshot of the buy box for the last size.

Usage: uv run --no-project --with playwright python tools/qa/pdp_price_consistency_check.py <outdir> <base_url> <theme_id> <handle> ...
       Set LP_CHROME if system Chrome is not installed."""
import asyncio, json, os, re, sys
from playwright.async_api import async_playwright

OUT, BASE, TID = sys.argv[1], sys.argv[2], sys.argv[3]
TAG = BASE.split('//')[1].split('.')[0]
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36'
LAUNCH = {'executable_path': os.environ['LP_CHROME']} if os.environ.get('LP_CHROME') else {'channel': 'chrome'}
STATE = r"""() => { const info = document.querySelector('.shopify-section--main-product .product-info'); if (!info) return null;
  const t = (e) => e ? e.textContent.replace(/\s+/g, ' ').trim() : null, num = (s) => parseFloat((s || '').replace(/[^0-9.,]/g, '').replace(/,(?=\d{3}\b)/g, '').replace(',', '.')) || 0;
  const cards = [...info.querySelectorAll('.lp-vcard')], sel = cards.find(c => c.classList.contains('is-selected') || (c.control && c.control.checked) || (c.previousElementSibling && c.previousElementSibling.checked));
  const badge = sel ? sel.querySelector('.lp-vcard__badge--amber') : null, now = info.querySelector('.lp-atc .lp-pdp-price__now'), was = info.querySelector('.lp-atc .lp-pdp-price__was');
  return { theme: Shopify.theme.id, cards: cards.length, selected: sel ? t(sel.querySelector('.lp-vcard__name')) : null, badge: badge && /save/i.test(badge.textContent) ? t(badge) : null, badgeAmount: badge && /save/i.test(badge.textContent) ? num(badge.textContent) : 0,
    cardUnit: sel && /per /.test(t(sel.querySelector('.lp-vcard__meta')) || '') ? num(t(sel.querySelector('.lp-vcard__meta'))) : null,
    sticky: t(document.querySelector('.lp-sticky__sub')), stickyUnit: (() => { const u = document.querySelector('[data-lp-sticky-unit]'); return u ? num(u.textContent) : null })(),
    rows: (() => { const pk = info.querySelector('skio-plan-picker'), root = pk && pk.shadowRoot; if (!root) return null;
      return [...root.querySelectorAll('.group-container')].map(g => ({ title: t(g.querySelector('.group-title')), selected: g.classList.contains('group-container--selected'), struck: g.querySelector('.skio-price s') ? num(g.querySelector('.skio-price s').textContent) : null,
        price: (() => { const p = g.querySelector('.skio-price'); if (!p) return null; const c = p.cloneNode(true); c.querySelectorAll('s').forEach(x => x.remove()); return num(c.textContent) })() })) })(),
    now: now ? num(now.textContent) : null, was: was && !was.hidden && was.getClientRects().length ? num(was.textContent) : null, oneTime: was ? num(was.dataset.price) : null, hscroll: document.documentElement.scrollWidth > innerWidth + 1 } }"""

async def main():
    os.makedirs(OUT, exist_ok=True); ok = True
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, **LAUNCH)
        for name, vp in (('1440', {'width': 1440, 'height': 900}), ('390', {'width': 390, 'height': 844})):
            ctx = await browser.new_context(viewport=vp, user_agent=UA, device_scale_factor=2); page = await ctx.new_page()
            # Marketing pop-ups (Klaviyo) cover the buy box once the live apps run on the draft; hide them for the test only.
            await ctx.add_init_script("document.addEventListener('DOMContentLoaded',()=>{const s=document.createElement('style');s.textContent='div.needsclick[role=dialog],div[class*=kl-private-reset-css][role=dialog],.klaviyo-form[role=dialog]{display:none!important}';document.head.append(s)})")
            await page.goto(f'{BASE}/?preview_theme_id={TID}', wait_until='domcontentloaded')
            for handle in sys.argv[4:]:
                await page.goto(f'{BASE}/products/{handle}', wait_until='domcontentloaded'); await page.wait_for_timeout(4500)
                info = page.locator('.shopify-section--main-product .product-info'); n = await info.locator('.lp-vcard').count()
                for i in range(max(n, 1)):
                    if n:
                        await info.locator('.lp-vcard').nth(i).scroll_into_view_if_needed(); await info.locator('.lp-vcard').nth(i).click(); await page.wait_for_timeout(2600)
                    picker = info.locator('skio-plan-picker')
                    if await picker.count():
                        try: await picker.get_by_text(re.compile('One-time', re.I), exact=False).first.click(timeout=4000); await page.wait_for_timeout(1500)
                        except Exception: pass
                    st = await page.evaluate(STATE)
                    diff = round((st['was'] or st['now']) - st['now'], 2)
                    # the badge is rounded down to a whole currency unit, a merchant compare-at price can carry cents
                    good = str(st['theme']) == TID and st['now'] and not st['hscroll'] and ((st['badgeAmount'] == 0 and st['was'] is None) or (st['was'] is not None and st['badgeAmount'] == int(diff + 1e-6))) if n else (str(st['theme']) == TID and (st['was'] is None or st['was'] > st['now']))
                    one = next((r for r in (st['rows'] or []) if r['title'] and 'one' in r['title'].lower()), None)
                    if n and one: good = good and one['struck'] == st['was'] and one['price'] == st['now']
                    if n: good = good and ((st['cardUnit'] is None and st['stickyUnit'] is None and st['sticky'] == 'In stock') or (st['cardUnit'] is not None and st['stickyUnit'] == st['cardUnit']))
                    plan = None
                    if await picker.count():
                        try:
                            await picker.get_by_text(re.compile('Subscribe'), exact=False).first.click(timeout=4000); await page.wait_for_timeout(1800)
                            sp = await page.evaluate(STATE); sub = next((r for r in (sp['rows'] or []) if r['selected']), None)
                            plan = {'now': sp['now'], 'was': sp['was'], 'oneTime': sp['oneTime'], 'row': [sub['struck'], sub['price']] if sub else None}
                            if sp['now'] and sp['oneTime'] and sp['now'] < sp['oneTime'] - 0.001: strike = st['was'] or sp['oneTime']; good = good and sp['was'] == strike and bool(sub) and sub['struck'] == strike and sub['price'] == sp['now']
                            await picker.get_by_text(re.compile('One-time', re.I), exact=False).first.click(timeout=4000); await page.wait_for_timeout(1500)
                            back = await page.evaluate(STATE); good = good and back['was'] == st['was'] and back['now'] == st['now']
                        except Exception as e: plan = {'note': 'no plan option: ' + str(e)[:50]}
                    ok = ok and bool(good)
                    print(('PASS ' if good else 'FAIL ') + json.dumps({'viewport': name, 'handle': handle, 'size': st['selected'], 'badge': st['badge'], 'price': st['now'], 'struck': st['was'], 'struckMinusPrice': diff if st['was'] else 0, 'oneTimeRow': [one['struck'], one['price']] if one else None, 'cardPerUnit': st['cardUnit'], 'sticky': st['sticky'], 'onPlan': plan}))
                await page.evaluate("document.querySelector('.shopify-section--main-product .lp-atc')?.scrollIntoView({block: 'center'})"); await page.wait_for_timeout(300)
                await page.screenshot(path=os.path.join(OUT, f'{TAG}-price-{handle}-{name}.png'))
            await ctx.close()
        await browser.close()
    print('RESULT', 'PASS' if ok else 'FAIL'); sys.exit(0 if ok else 1)

asyncio.run(main())
