# Progress Log

Session-to-session continuity. **Read the snapshot and the top entry at the start of every session; update both before ending one.** Newest entry first. Keep entries short: what changed, evidence, what is next. Long-form history goes to [PROJECT_HISTORY.md](PROJECT_HISTORY.md) at milestones.

## Snapshot (overwrite each session)

- **Active feature:** `perf-001` in progress: first-view speed is in (D-083 to D-087); PageSpeed's late first paint is open and needs an API key to chase (TD-039). Off-repo: `int-002` lpsync (private marketing repo).
- **Theme state:** `staging` branch (from `us`): API-uploaded theme 193151959352 is **published on the staging store** (D-079), the only store where the redesign is live; `master` = UK draft 189821452674; `us`, `eu`, `uk` branches equal to master in design; US draft 193373995317, EU draft 168919728345; News redesign on `news` (unpublished 190930518311). Nothing published.
- **Waiting on Letisha / owner:** owner fixes from the storefront QA (TD-023 to TD-031: the 0.00 jade roller, CELLNERGY WELLNESS 110V first on the UK and Europe, the UK footer Join Us link, which claims apply to skin care and devices, Stamped settings), apps Keep/Remove decisions (`apps-001`), News review (`news-001`), science hero artwork + video (`sci-002`), checkout extension deploy approval (`ref-002`), publish approval (`launch-001`), Impact 7.2.0 in a library (`ms-003`), which products Truemed accepts for the US HSA/FSA note (TD-016), Stamped review requests for the products with no reviews (TD-019), struck reference prices and the compare-at field (TD-022).
- **Known risks:** see [tech-debt.md](tech-debt.md) (top: customer data in public CSVs).
- **Next suggested step:** pick one `not_started` or newly requested item; run `./init.sh` first.

## Entry template

```
## YYYY-MM-DD · <feature id> · <one-line summary>
- Done: ...
- Evidence: commits, ./init.sh --full result, draft checks (390/1440), screenshots
- Decisions: D-NNN added? (docs/DECISIONS.md)
- Lessons: L-NNN added? (docs/LESSONS.md)
- Next: ...
- Blockers: ...
```

---

## 2026-11-28 · chk-001 · Checkout trust block built (not deployed)

- Done (D-110): "Order with confidence" checkout UI extension in `~/Documents/lifepharm-checkout-referral/extensions/trust-block`, next to the referral block. Design record and rollout plan in that project's `docs/trust-block.md`.
- Evidence: strict TypeScript against `@shopify/ui-extensions` 2026.10.0, Shopify extension validator passed for `purchase.checkout.block.render` (API 2026-04 and 2026-07), production bundle builds (about 9 KB gzipped). Not seen in a real checkout yet.
- Next: a person links the app and deploys; preview on staging with a one-time and a subscription cart; set the support email per store; EU store first.
- Added the same day: linked and deployed with an app automation token the owner created (service account, app development on this app only). App version `developer-lifepharm-2` is released with both blocks ("Referred by", "Order with confidence"). Nothing shows in any checkout until a block is placed in the checkout editor.
- Added the same day (D-111): a short strip, "Rating and guarantee" (live Stamped rating, three real LAMININE reviewers, guarantee), app version `developer-lifepharm-3`. Reviewer photos uploaded to Files on all four stores. Open check: the rating needs checkout to read the `stamped` product metafields, which have no definition; confirm on staging.
- Added the same day (D-112): the developer saw no rating or photos in the US checkout editor. Cause: the editor's sample cart is Gut Defense System, which has 0 Stamped reviews on the US store (LAMININE: 4.85 from 980), so the line was rightly left out. Editor-only sample data added for the rating and the subscription line; released as `developer-lifepharm-4`. Still open: a real LAMININE checkout must confirm that checkout passes the `stamped` metafields (still no definition on the US store).
- Added the same day (D-113): orange stars, ringed photo stack and "Loved by 980 customers"; images uploaded to Files on the four stores (`files_upload.py` now sends PNGs as PNG); released as `developer-lifepharm-5`.
- Added the same day (D-114): the rating is now each store's total over all products (shop metafield written by `tools/store-audit/reviews_summary.py`), and the strip can sit below the header; released as `developer-lifepharm-7`. Re-run the summary daily (TD-043).
- Added the same day (D-115): reviewer photos removed (Letisha), "Trusted by {count} customers" from each store's buyers, editable; released as `developer-lifepharm-8`.
- Blockers: owner approval to place the block; staging first.

## 2026-11-26 · co-002 · Company page: new purpose and five core values

- Done (D-109): the hero title is the new purpose; one "How We Work" section with five numbered values replaces the credo and BIIG sections; `lp-about-credo.liquid` deleted. Letisha's request.
- Evidence: master 45831dc and 0b8cb91; us 40ffd2c, eu 1f081c9, uk 1b001a1, staging cc05817 plus theme upload. `./init.sh --full` READY. Checked on the UK, US and Europe drafts and on staging at 1440 and 390: five values, no credo or BIIG text, no sideways scroll. The only page error seen was Stamped's `e is not a function` on the US draft (L-033).
- Next: ask Letisha whether the homepage mission line ("make optimal well-being inclusive for all") should follow the new purpose.

## 2026-11-26 · qa-letisha · Staging clicked through as a shopper (390 and 1440)

- Journey: home, Shop Best Sellers, country switch to US, quick add, PDP sizes and plans, cart drawer (qty, Share), checkout referral dialog, enroller search, checkout page (not submitted), menu, Join Us, search, sign-in sheet.
- Fixed (D-106, L-088): page jump on size change; Share and referral dialogs swallowed the first tap and closed the drawer on touch; search count included hidden results. Re-verified by tapping on staging, and with a mouse at 1440. Pushed to master, us, eu, uk and staging.
- Seen, not changed: Stamped `getappkey` 404 on the staging store only; pre-ticked "Email me with news and offers" in Shopify's sign-in sheet (admin setting, matters for UK/EU); long country list without search; review count wraps under the stars on mobile cards; low-contrast orange text ("Added to your cart!", inactive search tab).

## 2026-11-26 · qa-letisha · Pre-launch list, UK products, Modern Web Guidance
- Done: D-091 (subscription strikes the reference price, quick add without buttons), D-092 (Letisha's list), D-093 (UK products), D-094 (modern web audit).
- Evidence: `pdp_price_consistency_check.py` PASS on US (LAMIDERM APEX, LAMININE) and UK (LAMIDERM APEX, Diffuser) drafts at 1440 and 390; quick add drawer checked on US and UK drafts at both widths; staging checked at both widths (home counts 980 everywhere, no negative counter, zero-price and packs out of listings, policies 200, unpublished pages 404, contact links clean, no JS errors, no sideways scroll); UK live Shop All lists 14 products; `./init.sh --full` 0 fail, theme check 13 = baseline; live themes unchanged (18 and 19 Nov).
- Not checked: Europe draft quick add at 1440 (429); Safari fallback for light dismiss (no WebKit here).
- Added the same day: D-095, checked as a guest on staging and the US draft at 1440 and 390 (five packs not found; LAMININE, starter kit and the two enrolment pages fine). A signed-in IBO was not tested (needs a real IBO login).
- Added the same day: D-096 (apps as on live; every app host seen on live home, LAMININE and cart pages is seen on the draft: US 16, Europe 14, UK 8; no JS errors, no sideways scroll at 1440 and 390), D-097, filter button script error fixed, Europe price check PASS, Europe quick add checked at 390 only (429 at 1440).
- Added the same day: D-098, live data clean-up, checked on the three storefronts (zero-price products and 18 or so pages 404, Join Us 200, enrol page 200, Contact and FAQs 200).
- Added the same day: D-102 Selleasy off on the drafts (checked US and Europe at 1440 and 390: no widget, no Selleasy request, product pages and cart fine). Publish is on hold at the developer's request.
- Next: publish when the developer says so; Letisha on IBO packs, Gut Defense UK price and SKU, TD-042.

## 2026-11-25 · perf-001 · Widgets after the first view; the late paint is not ours alone
- Done: D-090; TD-039 controls (Horizon 16 of 16, app embeds off 6 of 21, settings restored and compared equal); four experiment files deleted from the staging theme after the developer's yes.
- Evidence: in feature_list perf-001; `./init.sh --full` passes; live UK, US and EU themes unchanged.
- Decisions: D-090. Lessons: L-080. Debt: TD-039 rewritten.
- Next: app decisions (TD-036, TD-041) are what is left for the product page score.

## 2026-11-25 · perf-001 · PageSpeed API key: how often the late first paint happens, and where
- Done: `psi_run.py --api --brief` (reads `GOOGLE_CONSOLE_API` or `PSI_API_KEY` from `.env`; unique address per run, because the API returns cached results). Controls and four elimination tests on staging: results in TD-039.
- Correction: the product page is also slow without the stall. Its four prompt API runs scored 76 to 86 (median 83.5, LCP 4.1 to 4.8 s); the earlier note that the 60 was only the stall, and the local 87 and 89, were too kind. "Mobile only" rests on five desktop runs.
- Note: the `content-visibility` experiment was briefly in the published staging stylesheet; it was taken out and read back identical to master.
- Next: product page weight; app embeds and a stock Impact copy as the next TD-039 tests; delete the experiment files on staging after a yes.

## 2026-11-25 · perf-001 · Product page 60 on PageSpeed mobile: the same lab stall, plus real image fixes
- Done: read both reports the developer saved (product page 60, homepage 91). The 60 is TD-039 again: first paint 2.12 s after the last render-blocking file, constant to 2 ms across three slow runs, mobile only (desktop 0 of 5). Product page: first gallery image preloaded from `<head>`, packshot and timeline `sizes` corrected (D-089). `hero_requests.py` takes a selector and a drawn share.
- Evidence: `./init.sh --full` passes; `hero_requests.py` on the staging product page passes on eight set-ups; local Lighthouse mobile on the product page 87 and 89 with a reused profile.
- Decisions: D-088 (Letisha: past referral orders are not re-credited), D-089. Debt: TD-039 rewritten with the new facts.
- Next: PageSpeed API key, then compare staging with the live US store and with theme copies (TD-039).
- Blockers: as before.

## 2026-11-25 · perf-001 · The developer's third PageSpeed run fell back to 69: same late first paint as the first report
- Done: read the report (FCP 2.5 s, LCP 6.8 s, TBT 0; observed first paint 2.4 s). It is the pattern of the first report, so not caused by D-085/D-086. Tried to reproduce it on software rendering, a slowed and saturated machine, and a GitHub runner (`.github/workflows/lighthouse-lab.yml`, new): never seen. `psi_run.py --api` added for a PageSpeed API key.
- Evidence: three PageSpeed reports saved in `tools/perf/reports/`; runner medians on staging: new headless 89.5 (eight runs), old headless shell 80.5 (ten runs). The laptop median of 98 is not what a datacentre machine gives; the honest range for the page as it is now is high 80s to about 90 when the lab paints on time.
- Also: Teqnavi's connector fix is live (their message via Letisha); `docs/knowledge/integrations.md` updated. D-055 can be relaxed after a test order confirms it.
- Next: a PageSpeed API key in `.env` (TD-039), then the elimination runs. Test order for the Teqnavi fix.
- Blockers: no way to run PageSpeed from here without the key.

## 2026-11-25 · perf-001 · Why PageSpeed mobile said 68, and the first-view fixes
- Done: (1) read the developer's PageSpeed report from its raw data: mobile 68 is LCP 7.4 s (1 of 25 points), FCP 2.5 s, SI 5.6 s; TBT and CLS are full marks. (2) Layout: viewport first in `<head>`, no preload for the unused settings fonts, `custom.css` inline, Design Packs styles only where used. (3) Homepage hero: phone photo announced in the Link header with device-based sizes, three-step `<picture>`. (4) Country options wait in a template. (5) `tools/perf/`: `lh_run.py`, `psi_run.py`, `hero_requests.py`. Plan picker label "One-Time Purchase" in title case on all stores (0e7ae18).
- Evidence: `./init.sh --full` passes (theme check 13 = baseline); staging homepage Lighthouse 13.6 mobile, medians of five: LCP 3415 to 3032 ms, score 91 and 90 (no real change); `hero_requests.py` passes on staging and on the US draft (one file per device on eight set-ups); the UK, US and EU drafts hold the four new files (read back through the API); the Design Packs condition is not exercised, since no published page or active product uses those sections; DOM 2323 to 1600; country switch works at 390 and 1440, no JS errors, no horizontal scroll.
- Second pass, after the developer's new PageSpeed run (mobile 90): hero preload moved from the Link header to two `<link>` tags in `<head>` with `fetchpriority` and `media` (D-085); the referral app's section moved to the footer group because its stylesheet held the hero paint (D-086); homepage meta description fallback for SEO 100 (D-087).
- Evidence, second pass: staging homepage Lighthouse medians of five: score 90 to 98, LCP 3032 to 1963 ms, hero in the first paint; Lighthouse SEO 100; `hero_requests.py` passes; referral dialog opens from the phone menu and at 1440; drafts read back through the API.
- Decisions: D-083 to D-087. Lessons: L-077 to L-079. Debt: TD-039 to TD-041, TD-037 updated.
- Next: the developer runs PageSpeed once more on staging to confirm the second pass there (it refuses this network); read it with `psi_run.py --report`. Then product pages and the three drafts on screen (TD-037).
- Blockers: PageSpeed quota on this network; the late first paint in the first report is unexplained (TD-039).

## 2026-11-24 · seo-001, perf-001 · SEO check and fixes, lighter images, first Lighthouse batch
- Done: (1) `tools/seo/seo_check.py`, an end-to-end SEO check for a draft or live theme (categories and weights from the claude-seo skill); theme fixes for titles, descriptions, canonical of Our Studies, product rating in JSON-LD and missing alt attributes. (2) Images: 3x screens ask for 2x pixels, finer width lists, one hero picture, no hover photos on touch screens, right-sized icons, Shopify's own country flags; `tools/qa/image_weight_check.py`. (3) First Lighthouse batch: price sync throttled, pinch zoom allowed, crawlable share links, country button label. Project skills added under `.claude/skills/`: `baoyu-compress-image`, `pagespeed-enhancer`.
- Evidence: SEO score on the drafts US 91 to 97, UK 91 to 95, Europe 91 to 97; images on the US draft phone 9.5 MB to 6.1 MB and desktop 9.4 MB to 7.7 MB over eight pages; Lighthouse mobile before the last batch: performance 39 / 49, accessibility 89, best practices 75, SEO 85 / 92; ./init.sh --full READY (13 = baseline) after each batch.
- Decisions: D-080 to D-082. Lessons: L-073 to L-075. Debt: TD-035 to TD-038.
- Not verified: the last batch (master 1d1aaac; us d2ba73e, eu 13f7fcd, uk 01dc14d) was pushed after `./init.sh --full` but not checked on the drafts, because the storefronts stopped answering the test machine. Staging carries the same build (origin/staging 07033b3, theme 193151959352 updated).
- Next: run the five checks and Lighthouse again (TD-037), then the app decisions that hold most of the speed (TD-036).

---

## 2026-11-24 · nav-003, ms-004 · Promo ticket in the mobile menu, team photo controls, staging store set up
- Done: (1) Mobile menu promo redrawn as a guarantee ticket with the brand's 60-day badge (third version; the developer rejected the dark panel and a plain sand row). (2) Team section: per-person Photo zoom and Mirror the photo; Daniel West mirrored and at 120%. (3) Wellness Stand "Compatible with" links to CELLNERGY WELLNESS. (4) Store data, live at once: US refund policy typo fixed; Gut Defense System added to the `all` collection on the US and Europe. (5) Staging: branch `staging` from `us`, unpublished theme uploaded by API, header menu created, 66 Files copied from the US.
- Evidence: master 3d5ba02 (promo), 5e79705 (team data), d16306c (stand link), 21fdc05 (store tools); us 895d453, eu a397c7f, uk 315910e; origin/staging d45edb6; ./init.sh --full READY (13 = baseline); draft checks at 390x844 and 1440x900 for the promo, the team grid, the stand link (200 on each store) and Shop All (Gut Defense System listed on the US and Europe, 15 products); staging audit: images, videos, menus, collections and pages all resolve.
- Decisions: D-075 to D-078. Lessons: L-071, L-072. Debt: TD-032 to TD-034.
- Next: developer connects GitHub branch `staging` on the staging store (TD-032); owner items TD-023 to TD-031.
- Blockers: the staging storefront is password-protected, so nothing there was checked on screen.
- Later the same day: the developer asked for the theme to be published on staging; done through the Admin API (D-079). The UK, US and Europe stores are unchanged and unpublished.

---

## 2026-11-24 · qa-001 · Storefront QA fixes on the US, UK and Europe drafts
- Done: three QA reports (one per store) were traced to their sources and the theme-side defects fixed on every store. (1) The buy-box delivery tile is built from the store's currency and free delivery threshold; the US and Europe had shown "Free UK Delivery Over £150". (2) Fully NSF Tested, Made in the USA and Clinically Studied show only on products tagged Nutritionals. (3) A product priced at zero reads Not Sold Separately, with no Add to Cart, dynamic checkout, sticky bar or quick add, and is noindex. (4) Homepage review numbers come from the live LAMININE count through `[reviews]` (980+ US, 970+ UK, 910+ Europe; the typed 978+ is gone). (5) Size cards show the price per unit for the selected plan, the same number as the sticky bar. (6) Stamped's hidden review thumbnails point at the store's own product image. (7) One h1 on the homepage; Join Us, Contact and FAQs now have one. (8) Removed the typed OMNIA "PREORDER SHIPS APRIL 2026" notice. (9) "1 review" on product tab cards; long mobile menu label wraps; share dialog links and the box dialog picture have valid addresses. No product data, menu or app setting was changed.
- Evidence: master cd51c38, 7ce8b4a; us 54d04d9, 7afcfe0; eu 69bfe99, ae401d7; uk c094b7e, 6ce37c9; ./init.sh --full READY (13 = baseline); `tools/qa/store_claims_check.py us uk eu` passes at 1440x900 and 390x844; `tools/qa/broken_images_check.py us uk eu` 54 of 54 pages (23 failed before).
- Decisions: D-069 to D-074 (D-071 supersedes the typed 978+ in CLAUDE.md section 3). Lessons: L-068, L-069, L-070.
- Not defects (by design or third party): "1,100+ reviews across LifePharm products" and a pack's "Includes IMMUNE+++ (20 reviews)" (D-065); Our Studies equal to Science (sci-003, redirect at publish); filter counts above the total; Pandectes and Stamped console errors.
- Next: the owner and LifePharm items in TD-023 to TD-031, most urgent first: unpublish the 0.00 jade roller, put 220V first on the UK and Europe, fix the UK footer Join Us link.
- Blockers: the Chrome extension would not connect to Claude Code this session, so the checks ran with the Playwright scripts above.

---

## 2026-11-24 · pdp-001 · LAMININE Why It Works shows the same photo on every store
- Done: the section showed the bottle photo on Europe and the telomere illustration on the US and UK, because it fell back to each store's own benefits image. The LAMININE template now names the bottle photo (developer's pick). Checked every product on the three stores: only LAMININE differed; DIGESTIVE+++ and REFIVE use the same photo under different file names. The gallery still differs on Europe on purpose (different label and nutrition table). No product data was changed.
- Evidence: master 4aa28a9; us c8d5953, eu c3fde77, uk f96c1b2; ./init.sh --full READY (13 = baseline); `tools/qa/pdp_highlights_image_check.py` 6/6 on the US, UK and EU drafts at 1440x900 and 390x844.
- Decisions: D-068. Lessons: L-067.

## 2026-11-23 · pdp-010 · Offer and price agree on every product page
- Done: the Save badge on a size card, the struck price in Add to Cart and the struck price in the plan picker's One-time row now come from one reference price; the sticky bar reads sizes like the size card (Family Pack shows $1.52 / capsule, ml products show a price per ml, Cellnergy sizes show In stock); every price row reads struck original first, price to pay second; the plan picker's Save badge sits higher and its rows have more padding. No product data was changed.
- Evidence: master 9ed8db3, 72c5c4d, 127f229; us 4c64e2a, eu c8699da, uk 4192dc1; ./init.sh --full READY (13 = baseline); `tools/qa/pdp_price_consistency_check.py` US 28/28, UK 14/14, EU 10/10 at 1440x900 and 390x844.
- Decisions: D-067. Lessons: L-066. Debt: TD-022 (compare-at in the admin is the developer's and LifePharm's decision).

## 2026-11-23 · pdp-001 · Reviews widget: Questions tab no longer shows the reviews as well
- Done: pressing Questions in the Stamped widget left the review cards on screen with the questions below them, on every product page. Our forced two-column grid on the reviews list overrode Stamped's own hide. The hidden state is now forced too. Found by the developer.
- Evidence: master b27394e; us 04f7bf4, eu 420874c, uk 28413de; `tools/qa/pdp_reviews_tabs_check.py` at 1440x900 and 390x844: US CELLNERGY WELLNESS, LAMININE, OMEGA+++, FootCharge; UK and EU LAMININE and CELLNERGY WELLNESS; Reviews, Questions, back, Write a Review and Ask a Question each show only their own list.
- Lessons: L-065.

## 2026-11-23 · pdp-009 · Space above What to Expect on device pages
- Done: removing the large How to section (D-066) left the timeline directly under the sand cards band with no space above its heading, on every device page. The timeline now brings its own top gap after a tinted band, and a tinted cards band closes at 60% of the section gap. Pages where a plain section comes first (LAMININE and the other supplements) are unchanged.
- Evidence: master 67bc1a3; us c8bf15f, eu 5607662, uk 087d2d2; ./init.sh --full READY (13 = baseline); measured on the drafts at 1440x900 and 390x844: space above the heading 115px / 64px, band bottom 69px / 38px (US Diffuser, Hydration System, FootCharge, Wellness; UK FootCharge; EU Wellness); LAMININE still 0 on US and UK.

## 2026-11-23 · pdp-002 · Pairs Well With no longer disappears after quick add is closed
- Done: the rule that hides the customer-stories heading until the stories load also hid the whole "Pairs Well With" block once its quick-add drawer had been opened (the drawer nests another product's buy box inside the block). The rule now names its own block types. Found by the developer on a phone.
- Evidence: master cad4852; us e1a2fba, eu 369fd43, uk f60e073; `tools/qa/pdp_quick_add_check.py` at 1440x900 and 390x844: US LAMININE, OMEGA+++, Wellness Stand; UK and EU LAMININE: every product opened and closed, block still shown, cart unchanged.
- Lessons: L-064.

## 2026-11-23 · pdp-008, pdp-009 · No empty stars; one set of buy-box dropdowns
- Done: (1) Rating row: a product with no reviews shows "Includes LAMININE (980 reviews)" with stars on packs, or "1,100+ reviews across LifePharm products" elsewhere, never empty stars. (2) Every product template has the same dropdowns after the buy buttons; the "LifePharm Guarantee" card, the large How to Use / How to Replace sections and the What's in the Box section are gone. What's in the Box is a new `lp_box` block with a photo per item and a viewer. Dropdown lists are indented; "return policy" links to the refund policy. Tool `tools/store-audit/pdp_dropdowns.py`; checks `tools/qa/pdp_rating_row_check.py` and `tools/qa/pdp_dropdowns_check.py`.
- Evidence: master 7aaa372 to e2b32fc; us 832268a, eu f3ca7cd, uk 920bcad; ./init.sh --full READY (13 = baseline); rating row US 24/24, UK 8/8, EU 8/8; dropdowns US 18/18, UK 10/10, EU 10/10 at 1440x900 and 390x844. Live themes not touched.
- Decisions: D-065, D-066. Lessons: L-060 to L-063. Debt: TD-019 to TD-021.
- Next: Letisha: Stamped review requests for the zero-review products (TD-019); Truemed product list (TD-016).

## 2026-11-23 · pdp-007 · HSA/FSA payment note: one line from one setting
- Done: the US product pages showed "Pay with HSA/FSA" from hand-written blocks in 6 of 20 product templates (twice on the Diffuser and Hydration System, missing on LAMININE, OMEGA+++, IMMUNE+++, DIGESTIVE+++). Now `snippets/lp-hsa-fsa.liquid` renders one line under the trust tiles, and Theme settings > Payment notes decides which products show it. 11 template blocks removed on `us`. US draft: same ten products as before. UK and EU: hidden. `sync_branch.py` keeps `lp_hsa_*` per store and takes `--root`. New check `tools/qa/pdp_payment_note_check.py`.
- Evidence: master f2e73a5; us 57fc9c8, eu 9d3d5b3, uk 98e1f71; ./init.sh --full READY (13 = baseline); theme check us 88, unchanged; US draft 18/18, UK 4/4, EU 2/2 at 1440x900 and 390x844. Live US theme not touched.
- Decisions: D-064. Lessons: L-058, L-059. Debt: TD-016 to TD-018.
- Next: Letisha to say which products Truemed accepts (TD-016), then set the list. US trust tile still says "Free UK Delivery Over £150" (TD-017).
- Blockers: none for the build. The session ran from a clone outside iCloud; the copy in `~/Documents` is behind origin until iCloud delivers its files (TD-018).

## 2026-11-22 · coll-002, nav-002 · Collection filters redesigned; shopping links open what their label says
- Done: (1) Link audit of the UK draft, then fixes on all three stores: both "Shop best sellers" buttons open all products sorted by best selling (they opened Nutritionals); Shop menu category links ignore a tag filter saved on the menu item (UK "Nutritionals" listed one product); the product FAQ button stays on the shopper's store (it opened the US store from UK); collections page card renamed Frequency Regeneration and its "View all products" link is no longer an absolute UK address. (2) Collection filters: the drawer is replaced by chips that apply at once. Desktop shows labelled rows; phones show a Filter button, a rail of quick chips and a sheet with every choice ("Show N products"). Sort list added (Featured, Best Sellers, price). A first version (white card with two rails) was rejected by the developer the same day and replaced. Files: `snippets/lp-collection-filters.liquid` (new), `sections/main-collection.liquid`, `assets/lp-premium.js`, `locales/en.default.json`, `snippets/mega-menu-horizontal.liquid`, `snippets/lp-mobile-menu.liquid`, `sections/lp-pdp-faq.liquid`, collection, index and list-collections templates per store.
- Evidence: master 0d7410b, 08305e5, 2ba0a3a, 2b84462, a749c9e; store branches pushed (uk, us, eu); ./init.sh --full READY (13 = baseline); theme check on us 88 and eu 23 errors, unchanged; `tools/qa/collection_filters_check.py` on the UK, US and EU drafts at 1440x900 and 390x844.
- Decisions: D-048, D-049. Lessons: L-056, L-057. Debt: TD-011 to TD-015.
- Next: owner or Letisha to fix in admin: the UK "Nutritionals" menu item (TD-011, visible on the live site today), CELLNERGY FOOTCHARGE missing from UK Shop All (TD-012), US collection naming (TD-013).

## 2026-11-22 · pdp-003 · Sticky Add to Cart: one-row layout with a short Add button
- Done: bar reads thumbnail (now on mobile too), size name with one quiet line under it (price per capsule, or "In stock"), price on the right, button "Add" (accessible name still "Add to Cart"). Guarantee chip removed from the bar. A long size name wraps to two lines instead of being cut off. Files: `sections/main-product.liquid`, `assets/lp-premium.css`, `assets/lp-premium.js`.
- Evidence: ce869f3, 78d3434; ./init.sh --full READY; UK draft at 390x844 and 1440x900 on LAMININE, Cellnergy Wellness, OMNIA, Lamiderm Apex: one row on one axis, no cut-off text, no h-scroll, price and size follow the picker, no new JS errors.
- Decisions: D-047.
- Lessons: L-055 (repo folder in iCloud: evicted files make git and the checks hang).
- Next: none for this feature.

## 2026-11-21 · pdp-006 · One compact buy box on every PDP: price in Add to Cart, Ideal For everywhere, floating sticky bar
- Done: price moved into the Add to Cart button (per variant, Skio plan aware; `snippets/buy-buttons.liquid`, `syncPrice` in lp-premium.js); price row, quantity stepper, separator and Stamped badge disabled on every product template (`tools/normalize_buybox.py`). Ideal For shows on every product: theme defaults per handle when custom.value_1 is empty or holds other content, five new brand icons (circulation, foot, handsfree, travel, face). Variant cards: saving as a top-edge badge, no Free Bottle badge. Skio: legend hidden, one-line subscription note, rounded saving badge. Sticky Add to Cart rebuilt as `lp-sticky-atc`: visible whenever the main button is off screen, hidden at the footer and under drawers, inert when hidden; floating card, no product name, large price. Pack and IBO templates take the standard lower sections (`tools/sync_pdp_layout.py`); empty sections hide themselves.
- Evidence: ./init.sh --full READY; drafts at 1440x900 and 390x844: Add to Cart bottom 893 (LAMININE), 907 (Omega, Digestive), 658 (Wellness), 781 (REFIVE EU); price changes with variant on Wellness, Hydration, Power Cream; no h-scroll, no new JS errors.
- Next: Power Cream template suffix on UK/US and UK footer Join Us link still await owner approval (admin data, live-facing).

## 2026-11-21 · pdp-005 · Cellnergy buy box follows LAMININE; white product area; visible gallery borders
- Done: every Cellnergy template (FootCharge, Wellness, Stand, Power Cream, Hydration, Diffuser) now runs title, rating, summary + Ideal For, big price with hairline, IBO price, variant cards (lp_card), then the rest (`tools/normalize_cellnergy_buybox.py`). Theme price, separator and Stamped badge blocks disabled; Clinicians' Choice moved under the buy buttons. Cellnergy cards show the pack price, not "per capsule". Main product section background is #ffffff on every product template, all branches. Gallery image and thumbnails get a 1px stone outline (drawn above full-bleed photos), rounded corners, white thumbnail fill.
- Evidence: ./init.sh --full READY; draft checks 1440/390 on US Wellness, Hydration, Diffuser, LAMININE, EU Power Cream, UK LAMININE: white bg, cards and Save chips correct, no h-scroll, no new JS errors.
- Next: Power Cream template suffix on UK/US and UK footer Join Us link still await owner approval.

## 2026-11-21 · qa-001 · Full-coverage QA on UK, US, EU drafts + Cellnergy PDP family

- Done: `tools/qa/site_qa.py` (every published product, collection, page, blog, article; 390 and 1440; rate-limit aware), `tools/qa/e2e_flows.py` (menu, language, search, quick add, PDP add/qty/remove, cart, referral question, Shopify checkout; never places an order), `tools/qa/data_qa.py` (Admin API data completeness), `tools/qa/fix_mojibake.py`. Fixed: sideways scroll from long rich-text URLs (main clips overflow), duplicate `dpProductBadge` declaration, US Get Started featured a deleted product, EU Diffuser PDP had no price, dead Contact/Science links (EU, UK), U+FFFD "?" symbols in copied US/EU content, orange `.h2` override on 6 product templates, empty-cart copy, Winston/Wickson titles. All Cellnergy PDPs (Wellness, Power Cream, Hydration, Diffuser, FootCharge, Stand) share the FootCharge layout via `tools/build_cellnergy_pdp.py`; LP sections take images from metafields (comma fallbacks) or product media.
- Evidence: crawl US 463 checks / EU 346 / UK 180, 0 bad links after fixes; E2E 10/10 at 1440 and 390 on UK, US, EU (EU cart API needs pacing).
- Open (owner): Power Cream UK/US still on the default template (needs templateSuffix switch); UK footer menu Join Us points at a deleted page; merchant data gaps in `tools/qa/reports/data-latest.json` (alt text, SEO descriptions, FootCharge short summary).
- Lessons: L-054 shared theme code must not reference store-only Files; L-055 storefront QA must be paced (one tab, delays) or Cloudflare blocks the IP for ~30 min, and the cart API rate-limits separately.

---

## 2026-11-21 · review · Letisha fixes: Ideal For icons, PDP gallery, home steps, FootCharge photos

- Done: Ideal For icons moved from UK-only Files into theme assets (US/EU were blank and uneven); PDP gallery panel white, PNG packshots smaller (sand + multiply read as a grey/beige cast); How It Works centred with larger, darker type, step 1 shows the full range (`lp-home-step-choose-range.jpg`) and drops "Start with LAMININE"; FootCharge How to Use and 1-month phase use seated photos (`lp-pdp-footcharge-seated*.jpg`, cut from product image 05 with the baked text removed). All stores.
- Evidence: init.sh --full READY; Playwright US/EU 390 and 1440: 4/4 icons on one row, panel rgb(255,255,255), no horizontal scroll, no page errors; seated images load on US/EU.
- Lessons: store-specific Files referenced from shared theme code break other stores; shared icons belong in assets.

---

## 2026-11-21 · pdp-004 · Cellnergy device PDPs rebuilt on all stores

- Done: replaced the legacy Impact sections under the buy box (spec table, text walls, guarantee marquee, slider timeline) on `product.cellnergy-footcharge` and `product.cellnergy-wellness-stand` with new reusable sections `lp-pdp-overview` (image, stats, chips), `lp-pdp-cards` (image / numbered / icon cards, mobile side-scroll) and `lp-pdp-split` (image with steps, notes, detail rows); `lp-pdp-timeline` now accepts Phase blocks (Laminine still uses metafields). Copy cleaned of em dashes and softened ("helps maintain muscle tone", not "prevent atrophy"). Same templates on master, uk, us, eu.
- Evidence: `./init.sh --full` READY; Playwright on UK/US/EU drafts, both products, 390 and 1440: no broken images, no horizontal scroll, no page errors.
- Next: Letisha review of the two pages.

---

## 2026-11-20 · harness-001 · Harness adopted

- Done: added `init.sh`, `tools/harness/check_theme.py` (JSON validity, 25-section limit, range/select/checkbox vs schema, em dash and amber-deep warnings, secret scan) and `theme_check_ratchet.py` (13 accepted vendor errors). Wrote PROJECT_HISTORY, LESSONS, DECISIONS, feature_list, QUALITY_SCORE, tech-debt and `docs/knowledge/`. Moved `claudedocs/` plans into `docs/exec-plans/`. Rescued `sync_branch.py`, `port_templates.py`, `files_upload.py`, `replace_file.py` from old scratchpads into `tools/store-audit/`.
- Evidence: `./init.sh --full` READY; guard FAILs on an injected `input_border_radius: 99` in a scratch copy (the 2026-11-10 incident).
- Decisions: D-006.
- Lessons: L-045 (scripts in scratchpads), L-046 (public repo).
- Next: owner decision on the public CSVs (tech debt TD-001).

## 2026-11-20 · ms-001 · Teqnavi embeds on US/EU branches

- Done: copied Sync Engine and Enrollment Handler app embeds into `config/settings_data.json` on `us` and `eu` with live settings; draft cart attributes now match live plus `Referrer Name`.
- Lessons: L-008.

## 2026-11-19 · ref-001 · Referral prompt skipped for existing Exigo customers

- Done: dialog and mobile-menu entry not rendered when `customer.metafields.Exigo.CustomerId` is set (842b6b2). Company page team edits; PDP gallery cursor restored.
- Evidence: Exigo credit check CSV (228 orders).
