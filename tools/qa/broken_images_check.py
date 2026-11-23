"""Draft check for pictures that do not show: every published product page and the homepage of a store's draft,
scrolled top to bottom at 390 wide. Lists each image that is on screen but failed to load, has no address,
or is served from another LifePharm store (each store serves its own files, L-070). Read-only.

Usage: uv run --no-project --with playwright python tools/qa/broken_images_check.py [us uk eu] [--only handle,handle]
       Set LP_CHROME if system Chrome is not installed."""
import asyncio, json, os, sys
from playwright.async_api import async_playwright

STORES = {
    'uk': ('https://uk.lifepharm.com', '189821452674'),
    'us': ('https://shop.lifepharm.com', '193373995317'),
    'eu': ('https://europe.lifepharm.com', '168919728345'),
}
UA = 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'
LAUNCH = {'executable_path': os.environ['LP_CHROME']} if os.environ.get('LP_CHROME') else {'channel': 'chrome'}
ONLY = sys.argv[sys.argv.index('--only') + 1].split(',') if '--only' in sys.argv else None

SCROLL = r"""async () => { const step = innerHeight * .8; for (let y = 0; y < document.documentElement.scrollHeight; y += step) { scrollTo(0, y); await new Promise(r => setTimeout(r, 180)); } scrollTo(0, 0); }"""
FIND = r"""() => { const own = location.hostname, stores = ['shop.lifepharm.com', 'uk.lifepharm.com', 'europe.lifepharm.com', 'news.lifepharm.com'];
  const where = el => { const s = el.closest('[class*="lp-"], [class*="stamped"], [id^="shopify-section"], [class*="product-"]'); return s ? (s.className && String(s.className).split(' ')[0]) || s.id : el.parentElement.tagName.toLowerCase(); };
  const out = [];
  for (const img of document.querySelectorAll('img')) {
    const box = img.getBoundingClientRect(); const shown = box.width > 1 && box.height > 1 && getComputedStyle(img).visibility !== 'hidden';
    const attr = img.getAttribute('src') || '', src = img.currentSrc || img.src || '';
    let host = ''; try { host = src ? new URL(src, location.href).hostname : ''; } catch (e) {}
    let problem = '';
    if (!attr.trim() && !img.getAttribute('srcset')) problem = 'no address';
    else if (shown && img.complete && img.naturalWidth === 0) problem = 'failed to load';
    else if (stores.includes(host) && host !== own) problem = 'served by another store';
    if (problem) out.push({ problem, file: src.split('/').pop().split('?')[0].slice(0, 70) || '(empty)', host, where: where(img), alt: (img.alt || '').slice(0, 40) });
  }
  return { theme: String(Shopify.theme.id), images: document.querySelectorAll('img').length, problems: out }; }"""


async def run(stores):
    failed = 0
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, **LAUNCH)
        for store in stores:
            base, tid = STORES[store]
            ctx = await browser.new_context(viewport={'width': 390, 'height': 844}, user_agent=UA, device_scale_factor=2, is_mobile=True); page = await ctx.new_page()
            await page.goto(f'{base}/?preview_theme_id={tid}', wait_until='domcontentloaded'); await page.wait_for_timeout(2000)
            handles = ONLY or await page.evaluate("fetch('/products.json?limit=250').then(r => r.json()).then(d => d.products.map(p => p.handle))")
            for path in ['/'] + [f'/products/{h}' for h in handles]:
                response = await page.goto(base + path, wait_until='domcontentloaded')
                if response.status >= 400:
                    print(f'SKIP {store} {path}  ({response.status})'); continue
                await page.wait_for_timeout(1500); await page.evaluate(SCROLL); await page.wait_for_timeout(2500)
                s = await page.evaluate(FIND)
                ok = s['theme'] == tid and not s['problems']
                failed += not ok
                print(('PASS ' if ok else 'FAIL ') + f"{store} {path}  images={s['images']}" + ('' if s['theme'] == tid else f"  wrong theme {s['theme']}"))
                for item in s['problems']:
                    print('     ' + json.dumps(item, ensure_ascii=False))
            await ctx.close()
        await browser.close()
    print('RESULT', 'PASS' if not failed else f'FAIL ({failed} pages)'); sys.exit(1 if failed else 0)

asyncio.run(run([a for a in sys.argv[1:] if a in STORES] or list(STORES)))
