"""Draft check that the "Why It Works" image on a product page is the same file on every store, at 1440 and 390.
Read-only. The section falls back to each store's own benefits image, so a template that names no image can
show a different picture per store (L-067).

Usage: uv run --no-project --with playwright python tools/qa/pdp_highlights_image_check.py <handle> <expected_file_stem> <base_url>=<theme_id> ...
       Optional LP_SHOTS=<dir> saves a screenshot of the section per store and viewport.
       Set LP_CHROME if system Chrome is not installed."""
import asyncio, json, os, sys
from playwright.async_api import async_playwright

HANDLE, STEM, TARGETS = sys.argv[1], sys.argv[2], [t.split('=') for t in sys.argv[3:]]
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36'
LAUNCH = {'executable_path': os.environ['LP_CHROME']} if os.environ.get('LP_CHROME') else {'channel': 'chrome'}
SHOTS = os.environ.get('LP_SHOTS')
STATE = r"""() => { const img = document.querySelector('.lp-hl__img'); if (!img) return null;
  const box = img.getBoundingClientRect();
  return { theme: Shopify.theme.id, file: (img.currentSrc || img.src).split('/').pop().split('?')[0], loaded: img.complete && img.naturalWidth > 0,
    width: Math.round(box.width), height: Math.round(box.height), hscroll: document.documentElement.scrollWidth > innerWidth + 1 } }"""

async def main():
    ok = True
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, **LAUNCH)
        for base, tid in TARGETS:
            for name, vp in (('1440', {'width': 1440, 'height': 900}), ('390', {'width': 390, 'height': 844})):
                ctx = await browser.new_context(viewport=vp, user_agent=UA, device_scale_factor=2); page = await ctx.new_page()
                errors = []; page.on('pageerror', lambda e: errors.append(str(e)[:120]))
                await page.goto(f'{base}/?preview_theme_id={tid}', wait_until='domcontentloaded')
                await page.goto(f'{base}/products/{HANDLE}', wait_until='domcontentloaded'); await page.wait_for_timeout(2500)
                await page.evaluate("document.querySelector('.lp-hl__img')?.scrollIntoView({block: 'center'})")
                try: await page.wait_for_function("(() => { const i = document.querySelector('.lp-hl__img'); return i && i.complete && i.naturalWidth > 0 })()", timeout=15000)
                except Exception: pass
                await page.wait_for_timeout(800)
                s = await page.evaluate(STATE)
                good = bool(s) and str(s['theme']) == tid and STEM in s['file'] and s['loaded'] and not s['hscroll'] and not errors
                ok = ok and good
                print(('PASS ' if good else 'FAIL ') + json.dumps({'store': base.split('//')[1], 'viewport': name, **(s or {'note': 'no image'}), 'jsErrors': errors}))
                if SHOTS and s:
                    await page.locator('.lp-hl__grid').first.screenshot(path=f"{SHOTS}/{base.split('//')[1].split('.')[0]}-{name}.png")
                await ctx.close()
        await browser.close()
    print('RESULT', 'PASS' if ok else 'FAIL'); sys.exit(0 if ok else 1)

asyncio.run(main())
