#!/usr/bin/env python3
"""End-to-end shopper flows on each draft theme, at 1440px and 390px. Never places an order: the run stops when the
Shopify checkout page has loaded, then empties the cart.

    uv run --with playwright python tools/qa/e2e_flows.py --store all

Flows: header menu (desktop SHOP / mobile menu), language selector, predictive search, collection quick add,
PDP variant card + add to cart, drawer quantity +/- and remove, cart page, checkout button -> referral question ->
"continue" -> Shopify checkout, account login form, newsletter form present.
"""
import argparse, asyncio, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
STORES = {
    'uk': ('https://uk.lifepharm.com', '189821452674'),
    'us': ('https://shop.lifepharm.com', '193373995317'),
    'eu': ('https://europe.lifepharm.com', '168919728345'),
}
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36'
NOISE = re.compile(r'e is not a function|shouldShowBanner|stamped|tolstoy|klaviyo|ResizeObserver|Script error|weglot|clarity|intelligems', re.I)


async def flows(browser, store, width):
    base, tid = STORES[store]
    ctx = await browser.new_context(viewport={'width': width, 'height': 900 if width > 500 else 844}, user_agent=UA)
    page = await ctx.new_page()
    errors, steps = [], []
    page.on('pageerror', lambda e: None if NOISE.search(str(e)) else errors.append(str(e)[:140]))
    page.on('dialog', lambda d: asyncio.ensure_future(d.dismiss()))

    async def step(name, coro):
        try:
            res = await coro
            ok = bool(res) if not isinstance(res, tuple) else res[0]
            detail = None if not isinstance(res, tuple) else res[1]
        except Exception as e:  # noqa: BLE001
            ok, detail = False, f'{type(e).__name__}: {str(e)[:120]}'
        steps.append({'step': name, 'ok': ok, 'detail': detail})
        return ok

    async def goto(path):
        sep = '&' if '?' in path else '?'
        r = await page.goto(f'{base}{path}{sep}preview_theme_id={tid}', wait_until='load', timeout=90000)
        await page.wait_for_timeout(2500)
        return r.status

    async def cart_count():
        return await page.evaluate("fetch('/cart.js').then(r=>r.json()).then(c=>c.item_count)")

    async def clear_cart():
        await page.evaluate("fetch('/cart/clear.js',{method:'POST'})")
        await page.wait_for_timeout(600)

    # 1. Home + menu
    async def home_menu():
        st = await goto('/')
        theme = await page.evaluate('Shopify.theme && Shopify.theme.id')
        if str(theme) != tid:
            return False, f'served theme {theme}'
        if width > 999:
            trig = page.locator('header summary').filter(has_text=re.compile('shop', re.I)).first
            await trig.hover(); await page.wait_for_timeout(600)
            if not await page.evaluate("[...document.querySelectorAll('header details')].some(d=>d.open)"):
                await trig.click(); await page.wait_for_timeout(900)
            vis = await page.evaluate("[...document.querySelectorAll('header details[open]')].some(d=>d.querySelectorAll('a').length>3)")
            return vis, f'status {st}, mega menu visible={vis}'
        await page.locator('[data-lp-menu-toggle]').first.click(); await page.wait_for_timeout(900)
        info = await page.evaluate("(()=>{const m=document.getElementById('lp-menu');return m?{open:m.open||m.hasAttribute('open')||getComputedStyle(m).visibility!=='hidden',links:m.querySelectorAll('a').length}:null})()")
        await page.keyboard.press('Escape'); await page.wait_for_timeout(500)
        return bool(info and info['links'] > 3), info
    await step('home + menu', home_menu())

    # 2. Language selector
    async def lang():
        btn = page.locator('.lp-lang__btn:visible').first
        if await btn.count() == 0:
            return False, 'no language button'
        await btn.click(); await page.wait_for_timeout(700)
        info = await page.evaluate("(()=>{const d=[...document.querySelectorAll('.lp-lang__dialog')].find(d=>d.open);return d?d.querySelectorAll('.lp-lang__opt, li').length:0})()")
        await page.keyboard.press('Escape'); await page.wait_for_timeout(400)
        return info > 3, f'{info} options'
    await step('language selector', lang())

    # 3. Predictive search
    async def search():
        trig = page.locator('[aria-controls="search-drawer"]:visible').first
        where = 'header'
        if not await trig.count():
            await page.locator('[data-lp-menu-toggle]').first.click(); await page.wait_for_timeout(900)
            trig = page.locator('#lp-menu [aria-controls="search-drawer"]:visible, #lp-menu a[href*="/search"]:visible, #lp-menu input[type=search]:visible').first
            where = 'mobile menu'
            if not await trig.count():
                await page.keyboard.press('Escape')
                return False, 'no search entry in the mobile header or menu'
        await trig.click(); await page.wait_for_timeout(900)
        inp = page.locator('#search-drawer input[type="search"]:visible, #search-drawer input[name="q"]:visible, input[type=search]:visible').first
        await inp.fill('laminine'); await page.wait_for_timeout(3000)
        n = await page.evaluate("document.querySelectorAll('#search-drawer a[href*=\"/products/\"]').length")
        await page.keyboard.press('Escape'); await page.wait_for_timeout(400)
        return n > 0, f'{n} product results (via {where})'
    await step('predictive search', search())

    # 4. Collection quick add
    async def quick_add():
        await clear_cart()
        await goto('/collections/all')
        cards = await page.evaluate("document.querySelectorAll('product-card, .product-card').length")
        first = page.locator('.product-card').first
        await first.scroll_into_view_if_needed(); await first.hover(); await page.wait_for_timeout(700)
        btn = first.locator('button:visible').first
        if await btn.count() == 0:
            return False, f'{cards} cards, no visible quick add button'
        await btn.click(); await page.wait_for_timeout(3500)
        c = await cart_count()
        if c == 0:
            add = page.locator('quick-buy-drawer form[action*="/cart/add"] button[type=submit]:visible, [id^="quick-buy"] form[action*="/cart/add"] button[type=submit]:visible').first
            if await add.count():
                await add.click(); await page.wait_for_timeout(3500); c = await cart_count()
        drawer = await page.evaluate("(()=>{const d=document.getElementById('cart-drawer');return !!d && (d.open||d.hasAttribute('open'))})()")
        return c > 0, f'{cards} cards, cart {c}, cart drawer open={drawer}'
    await step('collection quick add', quick_add())

    # 5. PDP: variant card, add to cart, drawer qty and remove
    async def pdp():
        await clear_cart()
        await goto('/products/laminine')
        img0 = await page.evaluate("(document.querySelector('.product-gallery__media:not([hidden]) img')||{}).currentSrc||''")
        cards = page.locator('.lp-card, [data-lp-card], .variant-picker label').filter(has_text=re.compile('count|pack', re.I))
        changed = None
        if await cards.count() > 1:
            await cards.nth(1).click(); await page.wait_for_timeout(1500)
            url = page.url
            changed = 'variant=' in url
        await page.locator('form[action*="/cart/add"] button[type="submit"]:visible, buy-buttons button[type="submit"]:visible').first.click()
        await page.wait_for_timeout(3500)
        c1 = await cart_count()
        plus = page.locator('#cart-drawer .lp-qty__btn--plus').first
        c2 = None
        if await plus.count():
            await plus.click(); await page.wait_for_timeout(3000); c2 = await cart_count()
        return c1 > 0 and (c2 is None or c2 == c1 + 1), f'variant url changed={changed}, cart after add {c1}, after + {c2}'
    await step('pdp add to cart + qty', pdp())

    async def remove():
        rm = page.locator('#cart-drawer .lp-cline__remove').first
        if not await rm.count():
            return False, 'no remove link'
        await rm.click(); await page.wait_for_timeout(3500)
        c = await cart_count()
        return c == 0, f'cart after remove {c}'
    await step('drawer remove', remove())

    # 6. Cart page
    async def cart_page():
        await goto('/products/laminine')
        vid = await page.evaluate("(document.querySelector('form[action*=\"/cart/add\"] [name=id]')||{}).value")
        await page.evaluate(f"fetch('/cart/add.js',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{items:[{{id:{vid},quantity:1}}]}})}})")
        await page.wait_for_timeout(1200)
        await goto('/cart')
        rows = await page.evaluate("document.querySelectorAll('main line-item, main .line-item, main [data-line-key], main .cart-item').length")
        return rows > 0, f'{rows} line(s) on /cart'
    await step('cart page', cart_page())

    # 7. Checkout from drawer -> referral question -> continue -> Shopify checkout
    async def checkout():
        await goto('/collections/all')
        await page.locator('[aria-controls="cart-drawer"]:visible').first.click()
        await page.wait_for_timeout(2500)
        await page.locator('#cart-drawer button[name="checkout"]:visible').first.click()
        await page.wait_for_timeout(1500)
        asked = await page.evaluate("(()=>{const d=document.querySelector('[data-lp-refq]');return !!(d&&d.open)})()")
        if asked:
            async with page.expect_navigation(timeout=45000):
                await page.locator('[data-lp-refq] [data-lp-refq-skip]:visible, [data-lp-refq] [data-lp-refq-continue]:visible').first.click()
        else:
            await page.wait_for_load_state('load')
        await page.wait_for_timeout(4000)
        on_checkout = '/checkouts/' in page.url or '/checkout' in page.url
        return on_checkout, f'referral question shown={asked}, landed {page.url.split("?")[0][:70]}'
    await step('checkout (stops at Shopify checkout)', checkout())

    # 8. Account login + newsletter
    async def account():
        await clear_cart()
        await goto('/account/login')
        form = await page.evaluate("!!document.querySelector('form[action*=\"/account/login\"], form#customer_login, a[href*=\"shopify.com/authentication\"], form[action*=\"login\"]')")
        url = page.url
        return form or 'shopify.com' in url, f'login form={form}, url {url.split("?")[0][:60]}'
    await step('account login', account())

    async def newsletter():
        await goto('/')
        n = await page.evaluate("document.querySelectorAll('footer form input[type=email], form[action*=\"contact\"] input[type=email]').length")
        return n > 0, f'{n} email field(s)'
    await step('newsletter form present', newsletter())

    try:
        await clear_cart()
    except Exception:  # noqa: BLE001
        pass
    await ctx.close()
    return {'store': store, 'width': width, 'steps': steps, 'errors': errors}


async def main_async(stores, widths):
    from playwright.async_api import async_playwright
    out = []
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(channel='chrome')
        for s in stores:
            for w in widths:
                r = await flows(browser, s, w)
                out.append(r)
                print(f"\n[{s} {w}]")
                for st in r['steps']:
                    print(f"  {'PASS' if st['ok'] else 'FAIL'}  {st['step']}: {st['detail']}")
                if r['errors']:
                    print('  JS errors:', r['errors'][:3])
        await browser.close()
    os.makedirs(os.path.join(HERE, 'reports'), exist_ok=True)
    json.dump(out, open(os.path.join(HERE, 'reports', 'e2e-latest.json'), 'w'), indent=1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--store', default='all')
    ap.add_argument('--widths', default='1440,390')
    a = ap.parse_args()
    stores = list(STORES) if a.store == 'all' else [a.store]
    asyncio.run(main_async(stores, [int(x) for x in a.widths.split(',')]))


if __name__ == '__main__':
    main()
