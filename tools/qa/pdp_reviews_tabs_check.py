"""Draft check of the Stamped reviews widget tabs on a product page, at 1440 and 390. Read-only: no form is sent.
Walks Reviews -> Questions -> Reviews, then opens Write a Review and Ask a Question, and checks that only the
active tab's list and filter are on screen each time (L-065). Products without questions are reported as SKIP.

Usage: uv run --no-project --with playwright python tools/qa/pdp_reviews_tabs_check.py <base_url> <theme_id> <handle> ...
       Set LP_CHROME if system Chrome is not installed."""
import asyncio, json, os, sys
from playwright.async_api import async_playwright

BASE, TID = sys.argv[1], sys.argv[2]
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36'
LAUNCH = {'executable_path': os.environ['LP_CHROME']} if os.environ.get('LP_CHROME') else {'channel': 'chrome'}
STATE = r"""() => { const w = document.querySelector('#stamped-main-widget'); if (!w) return null;
  const vis = (s) => { const e = w.querySelector(s); return !!e && e.getClientRects().length > 0 && e.getBoundingClientRect().height > 0 };
  return { theme: Shopify.theme.id, reviews: vis('.stamped-reviews'), questions: vis('.stamped-questions'), reviewsFilter: vis('.stamped-reviews-filter'), questionsFilter: vis('.stamped-questions-filter'),
    reviewForm: vis('form.new-review-form'), questionForm: vis('form.new-question-form'), hscroll: document.documentElement.scrollWidth > innerWidth + 1 } }"""

async def main():
    ok = True
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, **LAUNCH)
        for name, vp in (('1440', {'width': 1440, 'height': 900}), ('390', {'width': 390, 'height': 844})):
            ctx = await browser.new_context(viewport=vp, user_agent=UA, device_scale_factor=2); page = await ctx.new_page()
            await page.goto(f'{BASE}/?preview_theme_id={TID}', wait_until='domcontentloaded')
            for handle in sys.argv[3:]:
                await page.goto(f'{BASE}/products/{handle}', wait_until='domcontentloaded'); await page.wait_for_timeout(2500)
                await page.evaluate("document.querySelector('#stamped-main-widget')?.scrollIntoView()")
                try: await page.wait_for_selector('#stamped-main-widget .stamped-tabs li[data-type="reviews"]', timeout=15000)
                except Exception: print('SKIP ' + json.dumps({'viewport': name, 'handle': handle, 'note': 'no reviews widget tabs'})); continue
                w = page.locator('#stamped-main-widget'); await page.wait_for_timeout(1500)
                if not await w.locator('.stamped-tabs li[data-type="questions"]').count(): print('SKIP ' + json.dumps({'viewport': name, 'handle': handle, 'note': 'no Questions tab'})); continue
                steps = {'start': await page.evaluate(STATE)}
                await w.locator('.stamped-tabs li[data-type="questions"]').click(); await page.wait_for_timeout(1500); steps['questions'] = await page.evaluate(STATE)
                await w.locator('.stamped-tabs li[data-type="reviews"]').click(); await page.wait_for_timeout(1500); steps['reviews'] = await page.evaluate(STATE)
                for key, sel in (('write', '.stamped-summary-actions-newreview'), ('ask', '.stamped-summary-actions-newquestion')):
                    if await w.locator(sel).count(): await w.locator(sel).first.click(); await page.wait_for_timeout(1200); steps[key] = await page.evaluate(STATE)
                on_reviews = lambda s: s['reviews'] and not s['questions'] and not s['questionsFilter']
                on_questions = lambda s: s['questions'] and not s['reviews'] and not s['reviewsFilter']
                good = str(steps['start']['theme']) == TID and on_reviews(steps['start']) and on_questions(steps['questions']) and on_reviews(steps['reviews'])
                good = good and ('write' not in steps or (steps['write']['reviewForm'] and on_reviews(steps['write']))) and ('ask' not in steps or (steps['ask']['questionForm'] and on_questions(steps['ask'])))
                good = good and not any(s['hscroll'] for s in steps.values()); ok = ok and good
                print(('PASS ' if good else 'FAIL ') + json.dumps({'viewport': name, 'handle': handle, **{k: [v['reviews'], v['questions']] for k, v in steps.items()}}))
            await ctx.close()
        await browser.close()
    print('RESULT', 'PASS' if ok else 'FAIL'); sys.exit(0 if ok else 1)

asyncio.run(main())
