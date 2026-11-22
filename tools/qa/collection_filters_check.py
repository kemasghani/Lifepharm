"""Draft check of the collection filters and the shopping links, at 1440 and 390. Read-only: it never submits a cart form.
Desktop: chip rows (mouse and keyboard), Clear all, sort. Phone: quick rail, Filter sheet (choice keeps it open,
Show N products, Escape), round clear button, sort. Then the Best Sellers landing, a category page, and the home,
menu, FAQ and collections-page links. Output: <outdir>/<store>-filters.json plus screenshots.

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
         'intelligems', 'triplewhale', 'pandectes', 'skio', 'gorgias', 'Failed to load resource', 'unload is not allowed', 'shop.app', 'Failed to fetch']

STATE = r"""
() => {
  const bar = document.querySelector('[data-lp-filters]');
  const t = (el) => el ? el.textContent.replace(/\s+/g, ' ').trim() : null;
  if (!bar || !bar.querySelector('.lp-filters__bar, .lp-filters__foot')) return { bar: false, theme: window.Shopify && Shopify.theme && Shopify.theme.id };
  const shown = (el) => !!el && el.offsetParent !== null;
  const box = (el) => { const b = el.getBoundingClientRect(); return { x: Math.round(b.left), y: Math.round(b.top), w: Math.round(b.width), h: Math.round(b.height) }; };
  const rows = bar.querySelector('.lp-filters__rows'), rail = bar.querySelector('[data-lp-rail]'), dialog = bar.querySelector('[data-lp-fsheet]');
  const scope = dialog && dialog.open ? dialog : shown(rows) ? rows : bar.querySelector('.lp-filters__bar');
  const chips = scope ? [...scope.querySelectorAll('.lp-chip:not(.lp-filters__open)')] : [];
  const sel = bar.querySelector('[data-lp-sort]'), opener = bar.querySelector('.lp-filters__open'), badge = bar.querySelector('.lp-filters__badge');
  return {
    bar: true, v2: !!bar.querySelector('.lp-filters__bar'), theme: Shopify.theme.id, url: location.pathname + location.search.replace(/&?preview_theme_id=\d+/, ''),
    vw: innerWidth, hscroll: document.documentElement.scrollWidth > innerWidth + 1, htmlOverflow: document.documentElement.style.overflow,
    layout: shown(rows) ? 'rows' : 'bar',
    groups: shown(rows) ? [...rows.querySelectorAll('.lp-fgroup')].map(g => ({ label: t(g.querySelector('.lp-fgroup__label')), chips: g.querySelectorAll('.lp-chip').length,
      rows: new Set([...g.querySelectorAll('.lp-chip')].map(c => Math.round(c.getBoundingClientRect().top))).size })) : null,
    rail: shown(rail) ? { label: rail.getAttribute('aria-label'), chips: rail.querySelectorAll('.lp-chip').length, scrolls: rail.scrollWidth > rail.clientWidth + 1, scrollLeft: Math.round(rail.scrollLeft), right: Math.round(rail.getBoundingClientRect().right) } : null,
    opener: shown(opener) ? { h: box(opener).h, badge: badge ? parseInt(badge.textContent, 10) : 0, expanded: opener.getAttribute('aria-expanded') } : null,
    reset: shown(bar.querySelector('.lp-filters__reset')),
    sheet: dialog ? { open: dialog.open, groups: [...dialog.querySelectorAll('.lp-fgroup')].map(g => t(g.querySelector('.lp-fgroup__label')) + ':' + g.querySelectorAll('.lp-chip').length), button: t(dialog.querySelector('.lp-fsheet__show')), clear: !!dialog.querySelector('.lp-filters__clear'), scrollTop: Math.round(dialog.querySelector('.lp-fsheet__body').scrollTop), box: dialog.open ? box(dialog) : null } : null,
    chipMinH: chips.length ? Math.min(...chips.map(c => Math.round(c.getBoundingClientRect().height))) : null,
    active: chips.filter(c => c.classList.contains('is-active')).map(c => t(c.querySelector('.lp-chip__text'))),
    disabled: chips.filter(c => c.classList.contains('is-disabled')).length,
    sample: chips.slice(0, 3).map(c => c.querySelector('.lp-chip__text').innerText + ' ' + (t(c.querySelector('.lp-chip__count')) || '')),
    count: t(bar.querySelector('.lp-filters__count')), clearInline: shown(bar.querySelector('.lp-filters__clear--inline')),
    foot: box(bar.querySelector('.lp-filters__foot')),
    sort: sel ? { value: sel.value, options: [...sel.options].map(o => o.value + '=' + o.text), box: box(sel), font: getComputedStyle(sel).fontSize } : null,
    cards: [...document.querySelectorAll('product-list product-card')].map(c => c.getAttribute('handle')),
    oldUi: { drawer: !!document.querySelector('#facets-drawer'), topbar: !!document.querySelector('.collection__top-bar'), floating: !!document.querySelector('.facets__floating-filter') },
    focus: document.activeElement ? (document.activeElement.dataset.lpChip || document.activeElement.id || document.activeElement.className.toString().slice(0, 40) || document.activeElement.tagName) : null,
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

            async def step(name):
                out['steps'][name] = await page.evaluate(STATE)
                return out['steps'][name]

            async def shot(name, to_bar=True):
                if to_bar:
                    await page.evaluate("document.querySelector('[data-lp-filters]').scrollIntoView({block: 'start'}); window.scrollBy(0, -90)")
                    await page.wait_for_timeout(400)
                await page.screenshot(path=f'{OUT}/{TAG}-{name}-{w}.png')

            for attempt in range(8):
                out['status'] = await go('/collections/all')
                st = await page.evaluate(STATE)
                if st.get('bar') and st.get('v2'):
                    break
                await asyncio.sleep(25)
            out['steps']['load'] = st
            if not (st.get('bar') and st.get('v2')):
                res.append(out); await ctx.close(); continue
            await shot('filters-default')

            if w >= 1000:
                sizes = await page.evaluate("[...document.querySelectorAll('.lp-filters__rows .lp-fgroup')].map(g => g.querySelectorAll('a.lp-chip').length)")
                big = sizes.index(max(sizes)); other = (big + 1) % len(sizes)
                group = lambda i: page.locator('.lp-filters__rows .lp-fgroup').nth(i)
                await group(big).locator('a.lp-chip').nth(2).click(); await settle()
                await step('one_chip'); await shot('filters-one')
                if len(sizes) > 1:
                    await group(other).locator('a.lp-chip:not(.is-active)').first.focus(); await page.keyboard.press('Enter'); await settle()
                    await step('second_group_by_keyboard')
                await page.locator('.lp-filters__clear--inline').click(); await settle()
                await step('cleared')
            else:
                rail = page.locator('[data-lp-rail]')
                chip = rail.locator('a.lp-chip').nth(1)
                before = (await chip.bounding_box())['x']
                await chip.tap(); await settle()
                s = await step('rail_chip')
                s['chip_moved_px'] = round((await rail.locator('a.lp-chip.is-active').first.bounding_box())['x'] - before)
                await shot('filters-one')
                # the sheet: opens, a choice keeps it open with new counts, Show closes it
                await page.locator('[data-lp-fsheet-open]').tap(); await page.wait_for_timeout(700)
                await step('sheet_open'); await page.screenshot(path=f'{OUT}/{TAG}-sheet-{w}.png')
                await page.evaluate("document.querySelector('.lp-fsheet__body').scrollTop = 60")
                await page.locator('.lp-fsheet .lp-fgroup').last.locator('a.lp-chip:not(.is-active)').first.tap(); await settle()
                await step('sheet_choice'); await page.screenshot(path=f'{OUT}/{TAG}-sheet-chosen-{w}.png')
                await page.locator('.lp-fsheet__show').tap(); await page.wait_for_timeout(1300)
                await step('sheet_shown')
                await page.locator('[data-lp-fsheet-open]').tap(); await page.wait_for_timeout(700)
                await page.keyboard.press('Escape'); await page.wait_for_timeout(900)
                await step('sheet_escape')
                await page.locator('.lp-filters__reset').tap(); await settle()
                await step('cleared')
                # far end of the rail keeps its place
                await rail.evaluate('r => r.scrollTo({ left: r.scrollWidth, behavior: "instant" })'); await page.wait_for_timeout(500)
                tail = rail.locator('a.lp-chip').last
                before = (await tail.bounding_box())['x']
                await tail.tap(); await settle()
                s = await step('rail_tail_chip')
                s['chip_moved_px'] = round((await rail.locator('a.lp-chip.is-active').first.bounding_box())['x'] - before)
                await page.locator('.lp-filters__reset').tap(); await settle()

            await page.select_option('[data-lp-sort]', 'best-selling'); await settle()
            await step('sorted_best'); await shot('filters-sorted')
            await page.select_option('[data-lp-sort]', 'price-ascending'); await settle()
            s = await step('sorted_price')
            s['prices'] = await page.evaluate("[...document.querySelectorAll('product-list product-card .price-list')].map(p => (p.textContent.match(/[\\d.,]+/) || [''])[0])")
            first_chip = page.locator('.lp-filters__rows a.lp-chip, [data-lp-rail] a.lp-chip').locator('visible=true').first
            await first_chip.click(); await settle()
            await step('chip_after_sort')

            out['best_status'] = await go('/collections/all?sort_by=best-selling')
            await step('landing_best')
            await go('/collections/nutritionals')
            await step('category'); await shot('filters-category')

            await go('/')
            out['links'] = await page.evaluate(r"""
            () => { const t = (el) => (el.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 50);
              const pick = (sel) => [...document.querySelectorAll(sel)].map(a => t(a) + ' -> ' + a.getAttribute('href'));
              return { hero: pick('[id$="lp_home_hero"] a.button'), guarantee: pick('[id$="lp_guarantee"] a.button'),
                shopAll: pick('a.lp-menu__cta'), megaHeads: pick('.mega-menu__nav > li > a'),
                taggedLinks: [...document.querySelectorAll('a[href*="/collections/"]')].filter(a => new URL(a.href).pathname.split('/').filter(Boolean).length > 2).map(a => t(a) + ' -> ' + a.getAttribute('href')).filter((v, i, a) => a.indexOf(v) === i) }; }""")
            await go('/products/laminine')
            out['faq_button'] = await page.evaluate("[...document.querySelectorAll('.lp-faq__actions a')].map(a => (a.textContent || '').trim() + ' -> ' + a.getAttribute('href'))")
            await go('/collections')
            out['collections_page'] = await page.evaluate(r"""() => [...document.querySelectorAll('main a[href*="/collections/"]')].map(a => (a.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 40) + ' -> ' + a.getAttribute('href')).filter((v, i, a) => a.indexOf(v) === i)""")
            out['errors'] = sorted(set(e for e in errs if not any(n.lower() in e.lower() for n in NOISE)))
            out['noise'] = len(errs)
            res.append(out)
            json.dump(res, open(f'{OUT}/{TAG}-filters.json', 'w'), indent=1)
            await ctx.close()
        await browser.close()
    json.dump(res, open(f'{OUT}/{TAG}-filters.json', 'w'), indent=1)
    print('done')

asyncio.run(main())
