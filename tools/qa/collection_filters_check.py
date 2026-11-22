"""Draft check of the collection filter bar and the shopping links, at 1440 and 390. Read-only: it never submits a cart form.
It clicks chips, uses the keyboard, clears, sorts, lands on the Best Sellers link, then reads the home, menu, FAQ and
collections-page links. Output: <outdir>/<store>-filters.json plus screenshots.

Usage: uv run --no-project --with playwright python tools/qa/collection_filters_check.py <outdir> [base_url theme_id]
       (default: the UK draft). Set LP_CHROME to a browser binary if system Chrome is not installed."""
import asyncio, json, os, sys
from playwright.async_api import async_playwright

OUT = sys.argv[1]
BASE, TID = (sys.argv[2], sys.argv[3]) if len(sys.argv) > 3 else ('https://uk.lifepharm.com', '189821452674')
TAG = BASE.split('//')[1].split('.')[0]
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36'
LAUNCH = {'executable_path': os.environ['LP_CHROME']} if os.environ.get('LP_CHROME') else {'channel': 'chrome'}
NOISE = ['e is not a function', 'shouldShowBanner', 'stamped', 'tolstoy', 'klaviyo', 'ResizeObserver loop', 'Script error', 'weglot', 'clarity',
         'intelligems', 'triplewhale', 'pandectes', 'skio', 'gorgias', 'Failed to load resource', 'unload is not allowed']

STATE = r"""
() => {
  const bar = document.querySelector('[data-lp-filters]');
  const t = (el) => el ? el.textContent.replace(/\s+/g, ' ').trim() : null;
  if (!bar) return { bar: false, theme: window.Shopify && Shopify.theme && Shopify.theme.id };
  const box = (el) => { const b = el.getBoundingClientRect(); return { x: Math.round(b.left), y: Math.round(b.top), w: Math.round(b.width), h: Math.round(b.height) }; };
  const chips = [...bar.querySelectorAll('.lp-chip')];
  const sel = bar.querySelector('[data-lp-sort]');
  return {
    bar: true, theme: Shopify.theme.id, url: location.pathname + location.search.replace(/&?preview_theme_id=\d+/, ''),
    vw: innerWidth, hscroll: document.documentElement.scrollWidth > innerWidth + 1,
    groups: [...bar.querySelectorAll('.lp-filters__group')].map(g => { const rail = g.querySelector('.lp-filters__rail'); return {
      label: t(g.querySelector('.lp-filters__label')), chips: g.querySelectorAll('.lp-chip').length,
      railScrolls: rail.scrollWidth > rail.clientWidth + 1, scrollLeft: Math.round(rail.scrollLeft), rows: new Set([...g.querySelectorAll('.lp-chip')].map(c => Math.round(c.getBoundingClientRect().top))).size }; }),
    chipMinH: Math.min(...chips.map(c => Math.round(c.getBoundingClientRect().height))), chipMinW: Math.min(...chips.map(c => Math.round(c.getBoundingClientRect().width))),
    active: chips.filter(c => c.classList.contains('is-active')).map(c => t(c.querySelector('.lp-chip__text'))),
    disabled: chips.filter(c => c.classList.contains('is-disabled')).map(c => t(c.querySelector('.lp-chip__text'))),
    sample: chips.slice(0, 4).map(c => ({ text: c.querySelector('.lp-chip__text').innerText, count: t(c.querySelector('.lp-chip__count')), transform: getComputedStyle(c.querySelector('.lp-chip__text')).textTransform })),
    activeStyle: (() => { const a = chips.find(c => c.classList.contains('is-active')); if (!a) return null; const cs = getComputedStyle(a); return { bg: cs.backgroundColor, color: cs.color }; })(),
    count: t(bar.querySelector('.lp-filters__count')), clear: !!bar.querySelector('.lp-filters__clear'),
    sort: sel ? { value: sel.value, options: [...sel.options].map(o => o.value + '=' + o.text), box: box(sel), font: getComputedStyle(sel).fontSize } : null,
    panel: bar.querySelector('.lp-filters__panel') ? box(bar.querySelector('.lp-filters__panel')) : null, foot: box(bar.querySelector('.lp-filters__foot')),
    cards: [...document.querySelectorAll('product-list product-card')].map(c => c.getAttribute('handle')),
    oldUi: { drawer: !!document.querySelector('#facets-drawer'), topbar: !!document.querySelector('.collection__top-bar'), floating: !!document.querySelector('.facets__floating-filter') },
    focus: document.activeElement ? (document.activeElement.dataset.lpChip || document.activeElement.id || document.activeElement.tagName) : null,
  };
}
"""

async def main():
    res = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(**LAUNCH)
        for w, h in ((1440, 900), (390, 844)):
            ctx = await browser.new_context(viewport={'width': w, 'height': h}, device_scale_factor=2, user_agent=UA, is_mobile=(w < 700), has_touch=(w < 700))
            page = await ctx.new_page()
            errs = []
            page.on('pageerror', lambda e: errs.append('pageerror: ' + str(e)[:160]))
            page.on('console', lambda m: errs.append(m.text[:160]) if m.type == 'error' else None)
            out = {'w': w, 'steps': {}}

            async def go(path):
                await asyncio.sleep(6)
                sep = '&' if '?' in path else '?'
                r = await page.goto(f'{BASE}{path}{sep}preview_theme_id={TID}', wait_until='load', timeout=90000)
                await page.wait_for_timeout(2500)
                await page.add_style_tag(content='#preview-bar-iframe, #PBarNextFrameWrapper { display: none !important; }')
                return r.status if r else None

            async def settle():
                await page.wait_for_function("!document.querySelector('.shopify-section--main-collection').classList.contains('is-loading')", timeout=30000)
                await page.wait_for_timeout(900)

            async def shot(name, focus_bar=True):
                if focus_bar:
                    await page.evaluate("document.querySelector('[data-lp-filters]').scrollIntoView({block: 'start'}); window.scrollBy(0, -140)")
                    await page.wait_for_timeout(400)
                await page.screenshot(path=f'{OUT}/{TAG}-{name}-{w}.png')

            for attempt in range(8):
                out['status'] = await go('/collections/all')
                st = await page.evaluate(STATE)
                if st.get('bar'):
                    break
                await asyncio.sleep(25)
            out['steps']['load'] = st
            if not st.get('bar'):
                res.append(out); await ctx.close(); continue
            await shot('filters-default')

            # 1. choose a health chip
            # the group with the most choices (the health concern list on every store)
            sizes = await page.evaluate("[...document.querySelectorAll('.lp-filters__group')].map(g => g.querySelectorAll('a.lp-chip').length)")
            big = sizes.index(max(sizes))
            out['group_sizes'] = sizes
            first = page.locator('.lp-filters__group').nth(big).locator('a.lp-chip').nth(2)
            out['picked1'] = (await first.locator('.lp-chip__text').inner_text())
            await first.click(); await settle()
            out['steps']['one_chip'] = await page.evaluate(STATE)
            await shot('filters-one')
            # 2. add a chip from the last group, with the keyboard
            other = (big + 1) % len(sizes) if len(sizes) > 1 else big
            target = page.locator('.lp-filters__group').nth(other).locator('a.lp-chip:not(.is-active)').first
            if await target.count():
                await target.focus(); await page.keyboard.press('Enter'); await settle()
                out['steps']['two_groups_keyboard'] = await page.evaluate(STATE)
            # 3. clear all
            if await page.locator('.lp-filters__clear').count():
                await page.locator('.lp-filters__clear').click(); await settle()
            out['steps']['cleared'] = await page.evaluate(STATE)
            # 4. far end of a rail keeps its place (mobile)
            if w < 1000:
                rail = page.locator('.lp-filters__rail').nth(big)
                await rail.evaluate('r => r.scrollTo({ left: r.scrollWidth, behavior: "instant" })')
                await page.wait_for_timeout(500)
                tail = rail.locator('a.lp-chip').last
                out['picked_tail'] = await tail.locator('.lp-chip__text').inner_text()
                await tail.click(); await settle()
                out['steps']['tail_chip'] = await page.evaluate(STATE)
                await shot('filters-tail')
                await page.locator('.lp-filters__clear').click(); await settle()
            # 5. sort
            await page.select_option('[data-lp-sort]', 'best-selling'); await settle()
            out['steps']['sorted_best'] = await page.evaluate(STATE)
            await shot('filters-sorted')
            await page.select_option('[data-lp-sort]', 'price-ascending'); await settle()
            s = await page.evaluate(STATE)
            s['prices'] = await page.evaluate("[...document.querySelectorAll('product-list product-card .price-list')].map(p => p.textContent.replace(/\\s+/g, ' ').trim().slice(0, 40))")
            out['steps']['sorted_price'] = s
            # 6. chip plus sort keeps both
            await page.locator('.lp-filters__group').nth(big).locator('a.lp-chip').nth(1).click(); await settle()
            out['steps']['chip_after_sort'] = await page.evaluate(STATE)

            # direct landing from the Best Sellers buttons
            out['best_status'] = await go('/collections/all?sort_by=best-selling')
            out['steps']['landing_best'] = await page.evaluate(STATE)
            await page.screenshot(path=f'{OUT}/{TAG}-landing-best-{w}.png')
            # category page
            await go('/collections/nutritionals')
            out['steps']['nutritionals'] = await page.evaluate(STATE)
            await shot('filters-nutritionals')

            # shopping links
            await go('/')
            out['links'] = await page.evaluate(r"""
            () => { const t = (el) => (el.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 50);
              const pick = (sel) => [...document.querySelectorAll(sel)].map(a => t(a) + ' -> ' + a.getAttribute('href'));
              return { hero: pick('[id$="lp_home_hero"] a.button'), guarantee: pick('[id$="lp_guarantee"] a.button'),
                menuNutritionals: [...document.querySelectorAll('a[href*="/collections/nutritionals"]')].map(a => t(a) + ' -> ' + a.getAttribute('href')).filter((v, i, a) => a.indexOf(v) === i),
                shopAll: [...document.querySelectorAll('a.lp-menu__cta')].map(a => t(a) + ' -> ' + a.getAttribute('href')),
                megaHeads: [...document.querySelectorAll('.mega-menu__nav > li > a')].map(a => t(a) + ' -> ' + a.getAttribute('href')),
                taggedLinks: [...document.querySelectorAll('a[href*="/collections/"]')].filter(a => new URL(a.href).pathname.split('/').filter(Boolean).length > 2).map(a => t(a) + ' -> ' + a.getAttribute('href')).filter((v, i, a) => a.indexOf(v) === i) }; }""")
            await go('/products/laminine')
            out['faq_button'] = await page.evaluate("[...document.querySelectorAll('.lp-faq__actions a')].map(a => (a.textContent || '').trim() + ' -> ' + a.getAttribute('href'))")
            await go('/collections')
            out['collections_page'] = await page.evaluate(r"""() => [...document.querySelectorAll('main a[href*="/collections/"]')].map(a => (a.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 40) + ' -> ' + a.getAttribute('href'))""")
            out['errors'] = sorted(set(e for e in errs if not any(n.lower() in e.lower() for n in NOISE)))
            out['noise'] = len(errs)
            res.append(out)
            json.dump(res, open(f'{OUT}/{TAG}-filters.json', 'w'), indent=1)
            await ctx.close()
        await browser.close()
    json.dump(res, open(f'{OUT}/{TAG}-filters.json', 'w'), indent=1)
    print('done')

asyncio.run(main())
