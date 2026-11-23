"""Draft check of the buy-box dropdowns (D-066), at 1440 and 390. Read-only: it never submits a form.
Per product: the dropdown titles in order, no "LifePharm Guarantee" card, no large How to / What's in the Box
section left on the page, lists indented inside the text column, and, where the page has a What's in the Box
dropdown, that a row opens its photo, Next moves on and Escape closes. Also horizontal scroll and new JS errors.
Output: <outdir>/<store>-dropdowns.json plus a screenshot of the open dropdowns (and of the photo viewer).

Usage: uv run --no-project --with playwright python tools/qa/pdp_dropdowns_check.py <outdir> <base_url> <theme_id> <expect> ...
       <expect> is handle=Title|Title|... (the dropdown titles expected, in order), or handle=* to accept any set
       that includes the guarantee. The guarantee dropdown must link "return policy" to /policies/refund-policy,
       and that page must load. Set LP_CHROME if needed."""
import asyncio, json, os, sys
from playwright.async_api import async_playwright

OUT, BASE, TID = sys.argv[1], sys.argv[2], sys.argv[3]
EXPECT = {a.split('=', 1)[0]: a.split('=', 1)[1].split('|') for a in sys.argv[4:]}
TAG = BASE.split('//')[1].split('.')[0]
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36'
LAUNCH = {'executable_path': os.environ['LP_CHROME']} if os.environ.get('LP_CHROME') else {'channel': 'chrome'}
NOISE = ['e is not a function', 'shouldShowBanner', 'stamped', 'tolstoy', 'klaviyo', 'ResizeObserver loop', 'Script error', 'weglot', 'clarity',
         'intelligems', 'triplewhale', 'pandectes', 'skio', 'gorgias', 'Failed to load resource', 'unload is not allowed', 'shop.app', 'Failed to fetch']

STATE = r"""
() => {
  const info = document.querySelector('.shopify-section--main-product .product-info');
  if (!info) return { info: false, theme: window.Shopify && Shopify.theme && Shopify.theme.id, path: location.pathname };
  const t = (el) => el ? el.textContent.replace(/\s+/g, ' ').trim() : null;
  const acc = [...info.querySelectorAll('details.product-info__accordion')];
  acc.forEach(d => { d.open = true; d.setAttribute('aria-expanded', 'true'); });
  const lists = acc.flatMap(d => [...d.querySelectorAll('.prose ul, .prose ol')]).map(l => {
    const li = l.querySelector('li'), content = l.closest('.accordion__content').getBoundingClientRect(), b = li ? getComputedStyle(li, '::before') : null, lr = li ? li.getBoundingClientRect() : null;
    return { tag: l.tagName, in: t(l.closest('details').querySelector('summary')), style: getComputedStyle(l).listStyleType, items: l.children.length,
      liLeftVsContent: lr ? Math.round(lr.left - content.left) : null, textIndent: li ? Math.round(parseFloat(getComputedStyle(li).paddingInlineStart)) : null,
      marker: b ? { left: Math.round(parseFloat(b.left)), w: Math.round(parseFloat(b.width)), text: b.content } : null };
  });
  const splits = [...document.querySelectorAll('.shopify-section')].filter(s => /lp-pdp-split/.test(s.className)).map(s => t(s.querySelector('.lp-eyebrow, [class*="eyebrow"]')) || t(s.querySelector('h2')));
  const rows = [...info.querySelectorAll('[data-lp-box-open]')];
  return {
    info: true, theme: Shopify.theme.id, path: location.pathname,
    dropdowns: acc.map(d => t(d.querySelector('summary'))), empty: acc.filter(d => !t(d.querySelector('.accordion__content')) && !d.querySelector('.accordion__content img')).map(d => t(d.querySelector('summary'))),
    card: [...info.querySelectorAll('.offer')].filter(o => o.getClientRects().length && /LifePharm Guarantee/i.test(o.textContent)).length,
    splits, lists, groups: info.querySelectorAll('.accordion-group').length,
    gaps: acc.slice(1).map((d, k) => Math.round(d.getBoundingClientRect().top - acc[k].getBoundingClientRect().bottom)),
    policy: (() => { const g = acc.find(d => /Money-Back Guarantee/.test(t(d.querySelector('summary')))), a = g && g.querySelector('.accordion__content a'); return a ? { text: t(a), href: a.getAttribute('href') } : null })(),
    box: rows.length ? { rows: rows.length, labels: rows.map(r => r.dataset.label), thumbs: rows.map(r => { const i = r.querySelector('img'); return i.complete && i.naturalWidth > 0; }),
      rowH: rows.map(r => Math.round(r.getBoundingClientRect().height)), plain: info.querySelectorAll('.lp-box__row--plain').length } : null,
    vw: innerWidth, hscroll: document.documentElement.scrollWidth > innerWidth + 1,
  };
}
"""
VIEWER = r"""
() => { const d = document.querySelector('[data-lp-box-dialog]'), i = d && d.querySelector('[data-lp-box-img]'), r = d && d.open ? d.getBoundingClientRect() : null;
  return d ? { open: d.open, caption: d.querySelector('[data-lp-box-caption]').textContent, count: (d.querySelector('[data-lp-box-count]') || {}).textContent || null,
    img: i.complete && i.naturalWidth > 0, alt: i.alt, fits: r ? r.left >= 0 && r.right <= innerWidth && r.top >= 0 && r.bottom <= innerHeight : null,
    close: (() => { const c = d.querySelector('[data-lp-box-close]').getBoundingClientRect(); return Math.round(c.width) + 'x' + Math.round(c.height); })() } : null; }
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
                await page.evaluate("document.querySelectorAll('details.product-info__accordion').forEach(d => { d.open = true })")
                if await page.locator('.lp-box').count():
                    await page.evaluate("document.querySelector('.lp-box').scrollIntoView({block: 'center'})")
                    try: await page.wait_for_function("[...document.querySelectorAll('.lp-box__thumb img')].every(i => i.complete && i.naturalWidth > 0)", timeout=15000)
                    except Exception: pass
                st = await page.evaluate(STATE)
                st.update(handle=handle, viewport=name, want=want)
                titles_ok = st.get('dropdowns') == want or (want == ['*'] and '60-Day Money-Back Guarantee' in (st.get('dropdowns') or []))
                good = bool(st.get('info')) and str(st.get('theme')) == TID and titles_ok and not st['empty'] and st['card'] == 0 and not st['hscroll']
                good = good and st['groups'] <= 1 and all(g == 0 for g in st['gaps']) and bool(st['policy']) and st['policy']['text'] == 'return policy' and st['policy']['href'].split('?')[0] == '/policies/refund-policy'
                good = good and not [s for s in st['splits'] if s and (s.lower().startswith('how to') or s.lower() == 'specifications')]
                good = good and all(l['style'] == 'none' and l['liLeftVsContent'] == 0 and l['textIndent'] >= 20 and l['marker'] and 0 <= l['marker']['left'] for l in st['lists'])
                if good and st['box']:
                    good = all(st['box']['thumbs']) and min(st['box']['rowH']) >= 44
                    await page.evaluate("document.querySelector('.lp-box').scrollIntoView({block: 'center'})"); await page.wait_for_timeout(300)
                    await page.locator('[data-lp-box-open]').nth(1 if st['box']['rows'] > 1 else 0).click()
                    await page.wait_for_function("(() => { const i = document.querySelector('[data-lp-box-img]'); return i && i.complete && i.naturalWidth > 0 })()", timeout=15000)
                    await page.wait_for_timeout(400); v1 = await page.evaluate(VIEWER)
                    await page.screenshot(path=os.path.join(OUT, f'{TAG}-viewer-{handle}-{name}.png'))
                    await page.keyboard.press('ArrowRight'); await page.wait_for_timeout(500); v2 = await page.evaluate(VIEWER)
                    await page.keyboard.press('Escape'); await page.wait_for_timeout(300); v3 = await page.evaluate(VIEWER)
                    focus_back = await page.evaluate("document.activeElement && document.activeElement.matches('[data-lp-box-open]')")
                    st['viewer'] = {'opened': v1, 'next': v2, 'closed': not v3['open'], 'focusBack': focus_back}
                    good = good and v1['open'] and v1['img'] and v1['fits'] and v1['close'] == '44x44' and v1['caption'] == v1['alt'] and (st['box']['rows'] < 2 or v2['caption'] != v1['caption']) and not v3['open'] and focus_back
                st['errors'] = [e[:140] for e in errors if not any(n.lower() in e.lower() for n in NOISE)]
                st['pass'] = bool(good and not st['errors']); ok = ok and st['pass']; results.append(st)
                try:
                    first = page.locator('details.product-info__accordion').first
                    await first.scroll_into_view_if_needed(timeout=3000); await page.evaluate("window.scrollBy(0, -90)"); await page.wait_for_timeout(300)
                    await page.screenshot(path=os.path.join(OUT, f'{TAG}-dropdowns-{handle}-{name}.png'), full_page=False)
                except Exception: pass
                print(('PASS ' if st['pass'] else 'FAIL ') + json.dumps({k: st.get(k) for k in ('viewport', 'handle', 'dropdowns', 'want', 'empty', 'card', 'splits', 'lists', 'groups', 'gaps', 'policy', 'box', 'viewer', 'hscroll', 'errors', 'theme', 'info')}))
            if name == '1440':
                resp = await page.goto(f'{BASE}/policies/refund-policy', wait_until='domcontentloaded')
                h1 = (await page.locator('h1').first.text_content() or '').strip() if await page.locator('h1').count() else ''
                policy_ok = bool(resp and resp.status == 200 and h1)
                print(('PASS ' if policy_ok else 'FAIL ') + json.dumps({'policy_page': resp.status if resp else None, 'h1': h1[:60]})); ok = ok and policy_ok
            await ctx.close()
        await browser.close()
    json.dump(results, open(os.path.join(OUT, f'{TAG}-dropdowns.json'), 'w'), indent=1)
    print('RESULT', 'PASS' if ok else 'FAIL', f'({sum(r["pass"] for r in results)}/{len(results)})')
    sys.exit(0 if ok else 1)

asyncio.run(main())
