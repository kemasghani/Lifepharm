# Progress Log

Session-to-session continuity. **Read the snapshot and the top entry at the start of every session; update both before ending one.** Newest entry first. Keep entries short: what changed, evidence, what is next. Long-form history goes to [PROJECT_HISTORY.md](PROJECT_HISTORY.md) at milestones.

## Snapshot (overwrite each session)

- **Active feature:** none in this repo; `perf-001` is blocked on verification (TD-037). Off-repo: `int-002` lpsync (private marketing repo). Off-repo: `int-002` lpsync (private marketing repo).
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

## 2026-11-24 · seo-001, perf-001 · SEO check and fixes, lighter images, first Lighthouse batch
- Done: (1) `tools/seo/seo_check.py`, an end-to-end SEO check for a draft or live theme (categories and weights from the claude-seo skill); theme fixes for titles, descriptions, canonical of Our Studies, product rating in JSON-LD and missing alt attributes. (2) Images: 3x screens ask for 2x pixels, finer width lists, one hero picture, no hover photos on touch screens, right-sized icons, Shopify's own country flags; `tools/qa/image_weight_check.py`. (3) First Lighthouse batch: price sync throttled, pinch zoom allowed, crawlable share links, country button label. Project skills added under `.claude/skills/`: `baoyu-compress-image`, `pagespeed-enhancer`.
- Evidence: SEO score on the drafts US 91 to 97, UK 91 to 95, Europe 91 to 97; images on the US draft phone 9.5 MB to 6.1 MB and desktop 9.4 MB to 7.7 MB over eight pages; Lighthouse mobile before the last batch: performance 39 / 49, accessibility 89, best practices 75, SEO 85 / 92; ./init.sh --full READY (13 = baseline) after each batch.
- Decisions: D-080 to D-082. Lessons: L-073 to L-075. Debt: TD-035 to TD-038.
- Not verified: the last batch (master 1d1aaac; us d2ba73e, eu 13f7fcd, uk 01dc14d) was pushed after `./init.sh --full` but not checked on the drafts, because the storefronts stopped answering the test machine. Staging is one merge behind `us`.
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
