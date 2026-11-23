"""Draft check of "Pairs Well With" (complementary products) on a product page, at 1440 and 390.
Presses "+ Add" on each product, which opens the quick-add drawer, closes the drawer without adding, and
checks that the block and its products are still on the page afterwards (L-064). It never adds to the cart.
Output: one line per product plus a screenshot after closing.

Usage: uv run --no-project --with playwright python tools/qa/pdp_quick_add_check.py <outdir> <base_url> <theme_id> <handle> ...
       Set LP_CHROME if system Chrome is not installed."""
import asyncio, json, os, sys
from playwright.async_api import async_playwright

OUT, BASE, TID = sys.argv[1], sys.argv[2], sys.argv[3]
TAG = BASE.split('//')[1].split('.')[0]
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36'
LAUNCH = {'executable_path': os.environ['LP_CHROME']} if os.environ.get('LP_CHROME') else {'channel': 'chrome'}
NOISE = ['e is not a function', 'shouldShowBanner', 'stamped', 'tolstoy', 'klaviyo', 'ResizeObserver loop', 'Script error', 'weglot', 'clarity',
         'intelligems', 'triplewhale', 'pandectes', 'skio', 'gorgias', 'Failed to load resource', 'unload is not allowed', 'shop.app', 'Failed to fetch']
STATE = r"""() => { const r = document.querySelector('.shopify-section--main-product product-recommendations'), item = r && r.closest('.product-info__block-item');
  return { theme: Shopify.theme.id, block: !!r, shown: !!r && getComputedStyle(item).display !== 'none' && r.getBoundingClientRect().height > 40,
    buttons: r ? [...r.querySelectorAll('button[aria-controls^="quick-buy"]')].filter(b => b.getClientRects().length).length : 0,
    drawerOpen: !!document.querySelector('quick-buy-drawer[open], quick-buy-modal[open]'), cart: document.querySelector('cart-count') ? document.querySelector('cart-count').textContent.trim() : null } }"""

async def main():
    os.makedirs(OUT, exist_ok=True); ok = True
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, **LAUNCH)
        for name, vp in (('1440', {'width': 1440, 'height': 900}), ('390', {'width': 390, 'height': 844})):
            ctx = await browser.new_context(viewport=vp, user_agent=UA, device_scale_factor=2)
            page = await ctx.new_page(); errors = []
            page.on('pageerror', lambda e: errors.append(str(e)))
            await page.goto(f'{BASE}/?preview_theme_id={TID}', wait_until='domcontentloaded')
            for handle in sys.argv[4:]:
                errors.clear()
                await page.goto(f'{BASE}/products/{handle}', wait_until='domcontentloaded'); await page.wait_for_timeout(4500)
                rec = page.locator('.shopify-section--main-product product-recommendations')
                if not await rec.count(): print('SKIP ' + json.dumps({'viewport': name, 'handle': handle, 'note': 'no complementary products block'})); continue
                await rec.scroll_into_view_if_needed(); await page.wait_for_timeout(1200)
                before = await page.evaluate(STATE); steps = []
                for i in range(before['buttons']):
                    await rec.locator('button[aria-controls^="quick-buy"]').nth(i).click(); await page.wait_for_timeout(3000)
                    opened = (await page.evaluate(STATE))['drawerOpen']
                    await page.keyboard.press('Escape'); await page.wait_for_timeout(2200)
                    after = await page.evaluate(STATE); steps.append({'opened': opened, 'closed': not after['drawerOpen'], 'shown': after['shown'], 'buttons': after['buttons']})
                after = await page.evaluate(STATE)
                errs = [e[:140] for e in errors if not any(n.lower() in e.lower() for n in NOISE)]
                good = str(before['theme']) == TID and before['shown'] and before['buttons'] > 0 and all(s['opened'] and s['closed'] and s['shown'] and s['buttons'] == before['buttons'] for s in steps) and after['cart'] == before['cart'] and not errs
                ok = ok and good
                await rec.scroll_into_view_if_needed(); await page.wait_for_timeout(300); await page.screenshot(path=os.path.join(OUT, f'{TAG}-quickadd-{handle}-{name}.png'))
                print(('PASS ' if good else 'FAIL ') + json.dumps({'viewport': name, 'handle': handle, 'before': before, 'steps': steps, 'errors': errs}))
            await ctx.close()
        await browser.close()
    print('RESULT', 'PASS' if ok else 'FAIL'); sys.exit(0 if ok else 1)

asyncio.run(main())
