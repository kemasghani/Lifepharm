"""Draft check for the things one market or one product must not borrow from another, at 1440 and 390:
the delivery line in the buy box (L-068), the product claims (NSF, USA, clinically studied) on products
they are not made for (D-069), a product with no price (D-070), the homepage review number (D-071) and
the single h1. Read-only.

Usage: uv run --no-project --with playwright python tools/qa/store_claims_check.py [us uk eu]
       Optional LP_SHOTS=<dir> saves a screenshot of each buy box. Set LP_CHROME if system Chrome is not installed."""
import asyncio, json, os, sys
from playwright.async_api import async_playwright

STORES = {
    'uk': ('https://uk.lifepharm.com', '189821452674', 'Free UK Delivery Over £150'),
    'us': ('https://shop.lifepharm.com', '193373995317', 'Free Shipping Over $150'),
    'eu': ('https://europe.lifepharm.com', '168919728345', 'Free Delivery Over €150'),
}
CLAIMS = ['Fully NSF Tested', 'Made in the USA', 'Clinically Studied']
NUTRITIONAL, DEVICE, NO_PRICE = 'laminine', 'cellnergy-wellness', 'jade-roller-and-gua-sha-set'
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36'
LAUNCH = {'executable_path': os.environ['LP_CHROME']} if os.environ.get('LP_CHROME') else {'channel': 'chrome'}
SHOTS = os.environ.get('LP_SHOTS')

HOME = r"""() => ({ theme: String(Shopify.theme.id), h1: [...document.querySelectorAll('h1')].map(h => h.innerText.trim().slice(0, 40)),
  typed: document.body.innerText.includes('978'), placeholder: document.body.innerHTML.includes('[reviews]'),
  rating: [...document.querySelectorAll('.lp-hh__rating, .lp-guarantee__rating, .lp-hero__rating')].map(e => e.innerText.replace(/\s+/g, ' ').trim()),
  hscroll: document.documentElement.scrollWidth > innerWidth + 1 })"""
PAGE = r"""() => ({ h1: [...document.querySelectorAll('h1')].map(h => h.innerText.trim().slice(0, 40)), hscroll: document.documentElement.scrollWidth > innerWidth + 1 })"""
UNITS = r"""() => { const num = t => (t.match(/\d[\d.,]*/) || [''])[0];
  const card = document.querySelector('.product-info .lp-vcard.is-selected [data-lp-vcard-unit], .product-info input:checked + label [data-lp-vcard-unit], .product-info input:checked ~ .lp-vcard [data-lp-vcard-unit]');
  const sticky = document.querySelector('[data-lp-sticky-unit]');
  return { card: card ? num(card.textContent) : null, sticky: sticky ? num(sticky.textContent) : null, cards: [...document.querySelectorAll('.product-info [data-lp-vcard-unit]')].map(e => num(e.textContent)),
    notice: !!document.querySelector('.preorder-notice') } }"""
PDP = r"""() => { const button = document.querySelector('.product-info__buy-buttons buy-buttons button[type=submit]');
  return { theme: String(Shopify.theme.id), row: [...document.querySelectorAll('.product-info .lp-trust-row__item > span:last-child')].map(e => e.textContent.replace(/\s+/g, ' ').trim()),
    button: button ? button.textContent.replace(/\s+/g, ' ').trim().slice(0, 40) : null, disabled: button ? button.disabled : null,
    payment: !!document.querySelector('.product-info__buy-buttons .shopify-payment-button'), sticky: !!document.querySelector('lp-sticky-atc'),
    hscroll: document.documentElement.scrollWidth > innerWidth + 1 } }"""


async def run(stores):
    failed = 0
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, **LAUNCH)
        for store in stores:
            base, tid, delivery = STORES[store]
            other = [line for key, (_, _, line) in STORES.items() if key != store]
            for name, vp in (('1440', {'width': 1440, 'height': 900}), ('390', {'width': 390, 'height': 844})):
                ctx = await browser.new_context(viewport=vp, user_agent=UA, device_scale_factor=2); page = await ctx.new_page()
                errors = []; page.on('pageerror', lambda e: errors.append(str(e)[:120]))
                checks = []
                await page.goto(f'{base}/?preview_theme_id={tid}', wait_until='domcontentloaded'); await page.wait_for_timeout(2500)
                h = await page.evaluate(HOME)
                numbers = [r.split('+')[0].replace(',', '') for r in h['rating']]
                checks += [('home: draft theme', h['theme'] == tid, h['theme']), ('home: one h1', len(h['h1']) == 1, h['h1']),
                           ('home: no typed review number', not h['typed'] and not h['placeholder'], ''),
                           ('home: live review number', bool(numbers) and all(n.isdigit() and int(n) % 10 == 0 for n in numbers), h['rating']),
                           ('home: no sideways scroll', not h['hscroll'], '')]
                for handle in (NUTRITIONAL, DEVICE, NO_PRICE):
                    response = await page.goto(f'{base}/products/{handle}', wait_until='domcontentloaded'); await page.wait_for_timeout(2500)
                    if response.status == 404:
                        checks.append((f'{handle}: not on the storefront', True, '404')); continue
                    s = await page.evaluate(PDP)
                    claims = [c for c in CLAIMS if c in s['row']]
                    checks += [(f'{handle}: draft theme', s['theme'] == tid, s['theme']),
                               (f'{handle}: this store\'s delivery line', delivery in s['row'] and not [o for o in other if o in s['row']], s['row']),
                               (f'{handle}: no sideways scroll', not s['hscroll'], '')]
                    if handle == NUTRITIONAL:
                        checks += [(f'{handle}: all three claims', claims == CLAIMS, claims), (f'{handle}: can be bought', s['disabled'] is False, s['button'])]
                    else:
                        checks.append((f'{handle}: no product claims', not claims, claims))
                    if handle == DEVICE:
                        checks.append((f'{handle}: can be bought', s['disabled'] is False, s['button']))
                    if handle == NO_PRICE:
                        checks.append((f'{handle}: cannot be bought from its page', s['disabled'] is True and s['button'] == 'Not Sold Separately' and not s['payment'] and not s['sticky'], [s['button'], s['disabled'], s['payment'], s['sticky']]))
                    if SHOTS:
                        await page.locator('.product-info').first.screenshot(path=f'{SHOTS}/{store}-{handle}-{name}.png')
                await page.wait_for_timeout(1500)
                await page.goto(f'{base}/products/{NUTRITIONAL}', wait_until='domcontentloaded'); await page.wait_for_timeout(4000)
                u = await page.evaluate(UNITS)
                checks.append((f'{NUTRITIONAL}: size card and sticky bar show one price per unit', bool(u['card']) and u['card'] == u['sticky'], u))
                response = await page.goto(f'{base}/products/omnia', wait_until='domcontentloaded'); await page.wait_for_timeout(1500)
                if response.status < 400:
                    checks.append(('omnia: no dated pre-order notice', not (await page.evaluate(UNITS))['notice'], ''))
                for path in ('/pages/join-us', '/pages/contact', '/pages/faq', '/pages/faqs'):
                    response = await page.goto(base + path, wait_until='domcontentloaded'); await page.wait_for_timeout(1200)
                    if response.status >= 400: continue
                    g = await page.evaluate(PAGE)
                    checks += [(f'{path}: one h1', len(g['h1']) == 1, g['h1']), (f'{path}: no sideways scroll', not g['hscroll'], '')]
                checks.append(('no JS errors', not errors, errors))
                for label, ok, detail in checks:
                    failed += not ok
                    print(('PASS ' if ok else 'FAIL ') + f'{store} {name} · {label}' + (f'  {json.dumps(detail, ensure_ascii=False)}' if detail not in ('', []) and (not ok or 'review number' in label or 'delivery' in label or 'per unit' in label) else ''))
                await ctx.close()
        await browser.close()
    print('RESULT', 'PASS' if not failed else f'FAIL ({failed})'); sys.exit(1 if failed else 0)

asyncio.run(run([a for a in sys.argv[1:] if a in STORES] or list(STORES)))
