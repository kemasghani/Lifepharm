# Progress Log

Session-to-session continuity. **Read the snapshot and the top entry at the start of every session; update both before ending one.** Newest entry first. Keep entries short: what changed, evidence, what is next. Long-form history goes to [PROJECT_HISTORY.md](PROJECT_HISTORY.md) at milestones.

## Snapshot (overwrite each session)

- **Active feature:** none in this repo. Off-repo: `int-002` lpsync (private marketing repo).
- **Theme state:** `master` = UK draft 189821452674; `us`, `eu`, `uk` branches equal to master in design; US draft 193373995317, EU draft 168919728345; News redesign on `news` (unpublished 190930518311). Nothing published.
- **Waiting on Letisha / owner:** apps Keep/Remove decisions (`apps-001`), News review (`news-001`), science hero artwork + video (`sci-002`), checkout extension deploy approval (`ref-002`), publish approval (`launch-001`), Impact 7.2.0 in a library (`ms-003`).
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
