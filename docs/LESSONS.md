# Lessons Learned

Every time something cost us time, it goes here once, as a rule. This is the project's learning record: read the section for the area you are about to touch.

**Format:** `L-NNN · date · Symptom → Cause → Rule · Enforced by`.
"Enforced by" says whether a machine checks it (`init.sh`), a doc reminds us, or nothing yet. **If a lesson is hit twice, promote it to a check** in `tools/harness/check_theme.py`.

Add new lessons at the end of their section with the next free number.

---

## A. Shopify sync and deploy

- **L-001** · 2026-11-10 · Template edit never appeared on the draft → a JSON template held more than 25 sections; Shopify rejects the whole file **silently** → keep templates at 25 sections or fewer; product templates sit at 20 to 23, so remove disabled legacy sections before adding. · `init.sh` (FAIL above 25, WARN at 24).
- **L-002** · 2026-11-10 · Same silent rejection → one setting outside its schema range (`input_border_radius` max 10) → validate every range, select and checkbox value against its schema. `shopify theme check` does not catch this. · `init.sh` (range/select/checkbox checks on templates, section groups, settings_data).
- **L-003** · 2026-11-10 · Template rejected → empty image or url values written as `""` → omit the key instead of writing an empty string. · doc.
- **L-004** · 2026-11-11 · A "disabled" app section in a section group kept rendering → Shopify drops `disabled` on app sections inside groups → remove the app section from the group instead. · doc.
- **L-005** · 2026-11-14 · Second of two quick pushes never reached the draft → Shopify's GitHub sync applied the first and skipped the second → leave a minute between pushes; confirm with the Admin API `theme(id:).files(filenames:)` before assuming a rejection. · doc.
- **L-006** · 2026-11-10 · curl on the preview showed the live theme → `preview_theme_id` needs a cookie jar, and the first answer is a 302 → `curl -L -c jar -b jar "...?preview_theme_id=..."`; poll for a marker string, sync takes 1 to 10 minutes. · doc.
- **L-007** · 2026-11-18 · US/EU pages showed only a title → branches started as a UK copy and lacked live-only templates → after creating a store branch, run `tools/store-audit/port_templates.py` (read-only on live, never overwrites). · doc.
- **L-008** · 2026-11-20 · Referral attributes differed between draft and live → US/EU drafts lacked the Teqnavi app embeds → any branch sync must keep each store's own app embeds (`sync_branch.py` does). · doc.
- **L-058** · 2026-11-23 · `sync_branch.py us` would have rewritten 27 data files (index, FAQ pages, product templates) for a five-file code change, because the US branch has moved on from master's data since the last full sync → for a code-only change, first confirm the touched files are identical on the store branch and on master before the change (`git diff <store> master~1 -- <file>`), then `git checkout master -- <those files>` on the store branch; keep `sync_branch.py` for a deliberate full resync. A theme setting that is one store's own choice must be listed in `STORE_SETTINGS` there, or a full sync resets it. · this file.

## B. Liquid, CSS and JS

- **L-010** · 2026-11-18 · `class` silently missing on images → a filter inside `image_tag` arguments (`alt: x | default: y`) drops the other args → assign first, then pass the variable. · doc.
- **L-011** · 2026-11-12 · Variant image script compared the wrong id → the product form has an input named `id`, so `form.id` and `detail.formId` return an element → use `form.getAttribute('id')`. · doc.
- **L-012** · 2026-11-18 · Page froze after a referrer was set → a MutationObserver wrote text into the subtree it watched → never write DOM unconditionally inside an observer on the same subtree; compare first. · doc.
- **L-013** · 2026-11-18 · Share Your Cart stopped working after a quantity change → its jQuery handler was bound to the element, which the drawer re-render replaces → delegate events from a stable ancestor. · doc.
- **L-014** · 2026-11-11 · Quick add did not update the drawer → the request must bundle the theme's cart sections like the theme does → reuse the theme's section-rendering list. · doc.
- **L-015** · 2026-11-18 · Button styles ignored → Impact's button reset beats plain class selectors → style as `button.x:not(#lp-none)`. · doc.
- **L-016** · 2026-11-17 · News styles missing on some pages → Dawn loads a section's `{% stylesheet %}` only where that section renders; Dawn's root is 62.5% → shared styles go in `assets/lp-news.css`; scale rem by 1.6. · doc.
- **L-017** · 2026-11-18 · Odd character in About copy → merchant text contained a hidden `\x03` → strip control characters when pasting client copy. · doc.
- **L-057** · 2026-11-22 · Filter sheet closed and chips jumped after every choice → the theme's `facet:update` replaces every child of the section (DOMParser, then replaceChildren), so an open dialog, scroll positions and focus are gone, and `<noscript>` content comes back as real elements → keep that state in JS and restore it in a MutationObserver on the section (`initFilterBar` in `assets/lp-premium.js`). · doc.
- **L-060** · 2026-11-23 · A link written as `/products/x#anchor` reached the page as `/products/x#anchor?ref=retaildirect` → the Teqnavi referral app appends `?ref=` to the end of every internal link, after any hash, which breaks both the anchor and the parameter → do not put a `#anchor` on an internal link in theme code. · this file.
- **L-061** · 2026-11-23 · New list styling in the buy-box dropdowns lost to square bullets and a 1.4em row gap → most product templates carry merchant `custom_css` on the main-product section, and Shopify scopes it with the section id, so it beats any class selector → check `custom_css` in the template JSON when a rule "does not apply"; `!important` is the honest fix for shared code that must look the same on every template. · this file.
- **L-062** · 2026-11-23 · A new block type between two dropdowns produced a gap and a doubled rule → Impact groups consecutive `collapsible_text` blocks into one `.accordion-group` in `snippets/product-info.liquid`, by block type → a block that renders an accordion must be added to that grouping condition (`lp_dropdown_types`). Also: `height: 100%` on an image inside a `display: grid` box with an auto row is ignored (the photo was cropped); use a block box. · this file.
- **L-063** · 2026-11-23 · An icon beside 14px Metropolis looked low although the flex row was centred → the font's caps sit above the line box centre and a hand-drawn SVG was not centred in its viewBox → measure the ink (screenshot at 4x, compare the icon's rows with the first glyph's rows) and nudge by the measured amount; `tools/qa` checks cannot see this, a person or a pixel measure can. · this file.
- **L-064** · 2026-11-23 · "Pairs Well With" vanished after its quick-add drawer was opened and closed → the drawer loads another product's whole buy box inside the block, and a `.product-info__block-item:has(...)` rule meant for one small block then matched the outer block too → a `:has()` rule on `.product-info__block-item` must name the block (`[data-block-type=...]` or `[data-block-id=...]`), because quick-add nests a second buy box inside the first. Check: `tools/qa/pdp_quick_add_check.py`. · this file.

## C. Design process and client

- **L-020** · 2026-11-13 · 13 commits in one day flipping trust-tile icons (PNG, SVG, line icons and back) → iterating in code on an open visual question → for icon or style direction, show two or three options side by side (one screenshot) and get a pick before committing. · doc.
- **L-021** · 2026-11-11 · Homepage rebuilt as a Laminine landing page was rejected ("it became like a PDP") → the homepage has its own job → keep the homepage a brand homepage; push the hero product inside it. · doc.
- **L-022** · 2026-11-11 to 11-18 · Referral UI changed form four times (bar, slide-in, removed, slide-in, checkout dialog) → requirements flipped as the business learned → follow the latest instruction, record each change in [DECISIONS.md](DECISIONS.md), keep CLAUDE.md section 5 current. · doc.
- **L-023** · 2026-11-12 · Dark panels rejected twice (#414042, then #888B8D) → client wants light and bright → no dark or mid-grey surfaces; cream first. · CLAUDE.md section 7.
- **L-024** · 2026-11-14 · Client asked for #FF8F00 on eyebrows although it is about 2.2:1 on ivory → client choice beats the AA default here → apply it, state the trade-off once, do not silently revert. · CLAUDE.md, DECISIONS D-010.
- **L-025** · 2026-11-12 · Mockup-only designs led to cropped artwork → ask for source files (XD, original artwork, video) whenever only a mockup exists. · CLAUDE.md section 7.

## D. QA and verification

- **L-030** · 2026-11-17 · Client had to point out "Still unsure?" in sentence case → only h1/h2 get CSS capitalize; h3, summaries, tabs and labels slip through → write title case at the source; before handing over, sweep the rendered page (h1 to h6, `[role=tab]`, summary, button, label under 12 words) and flag lowercase non-minor words. Leave quoted study titles, form labels, sentences and metafield text alone. · doc (candidate for a scripted sweep, see tech debt).
- **L-031** · 2026-11-11 · 390px screenshots were wrong → headless Chrome `--window-size` renders too wide → use Playwright with `channel="chrome"`, `wait_until="load"`, never `networkidle`. · doc.
- **L-032** · 2026-11-18 · Storefront started answering 429 and a Cloudflare challenge → heavy Playwright runs against uk/shop domains → use the Admin API for ids and data; keep browser runs short. · doc.
- **L-033** · 2026-11-11 · Console errors blamed on the theme → `e is not a function` comes from Stamped.io; `addEventListener` null on /collections/all also happens on live → compare with the live theme before fixing "our" error. · doc.
- **L-035** · 2026-11-21 · Full QA crawl got the IP a Cloudflare challenge (429) for ~30 min on uk.lifepharm.com, and EU's cart API returned 429 mid-run → crawl one tab at a time with delays (`tools/qa/site_qa.py` does), light HTML checks for same-template pages, and pace cart-heavy E2E runs. · `tools/qa/`.
- **L-034** · 2026-11-12 · Done claimed before the draft had synced → always verify on the draft preview at 390px and 1440px: no horizontal scroll, no new JS errors. · CLAUDE.md section 1, `init.sh` reminder.
- **L-056** · 2026-11-22 · Menu "Nutritionals" showed one product, "Shop best sellers" opened a category, UK "View all FAQs" opened the US store → nobody had read each label against its destination (a menu item saved with a tag filter, store addresses hard-coded in templates and metafields) → after link or menu work run `tools/qa/collection_filters_check.py` on each store and read the links block. · tool.

## E. Data, integrations and tooling

- **L-040** · 2026-11-17 · Secrets printed to the terminal → `source .env` in zsh echoes lines with hyphenated keys as "command not found" → never source `.env`; parse only the keys you need (as `tools/store-audit/shopify.py` does). Never name a zsh loop variable `path`. · doc.
- **L-041** · 2026-11-18 · Exigo calls began failing with "IP not allowed" → the developer's ISP address rotates (mobile CGNAT) → run Exigo calls only from the whitelisted static egress host (details in private notes). · doc.
- **L-042** · 2026-11-18 · Assumed an order's referral moves commission → verified in Exigo: credit follows the customer's enroller; the referral counts only for new customers → do not show referral prompts to existing Exigo customers. · CLAUDE.md section 5.
- **L-043** · 2026-11-11 · Order history stopped at 60 days → the app lacks `read_all_orders` → state the window in any sales analysis. · doc.
- **L-044** · 2026-11-18 · Exigo `DequeueCustomerEvents` pops events for good → never call it while exploring. · doc.
- **L-045** · 2026-11-20 · Useful scripts (`sync_branch.py`, `port_templates.py`, Files upload) lived only in session scratchpads and nearly vanished → any script used twice goes into `tools/` in the same session. · this file.
- **L-046** · 2026-11-20 · Repo is **public** on GitHub → anything committed is published → no secrets, IPs, account ids, personal emails or customer data in commits; private facts stay in the developer's private notes. · `init.sh` secret scan.
- **L-055** · 2026-11-22 · The working copy lives in `~/Documents`, which iCloud can offload: 21 theme files and about 800 git objects became placeholders that never downloaded, so `./init.sh`, `grep -r` and most git commands hung with no output → if a command that only reads the repo stalls, check `ls -lO` / `find . -flags +dataless` before anything else; work from a fresh `git clone` outside iCloud (same credential helper as `.git/config`), then mark the folder "Keep Downloaded" or move the repo out of iCloud. · this file.
- **L-059** · 2026-11-23 · L-055 hit a second time: `./init.sh`, `grep -r` and `git grep` hung again, and `brctl download` did not bring the files back; the storefront also answers plain `curl` with 429 → work from a clone outside iCloud straight away (copy the `credential` helper from the old `.git/config`, symlink `.env`, pass `--root` to the store-audit tools); read live pages with Playwright, never curl. The folder still needs moving out of iCloud (TD-018). · this file.

## F. Assets and imagery

- **L-050** · 2026-11-11 · Grey rectangle under a composite product → the box PNG had a baked-in shadow → strip low-alpha pixels in the bottom area before compositing. · doc.
- **L-051** · 2026-11-13 · AI "collection" shots had garbled small print → check every AI image's labels at full resolution; single-product shots are usually clean. · doc.
- **L-052** · 2026-11-15 · Dropbox zips broke mid-download → the archive is too large → fetch one month folder at a time (`dl=1` on the subfolder); a truncated zip still extracts with `bsdtar -xf`. · doc.
- **L-054** · 2026-11-21 · "Ideal For" icons blank on US/EU → the icons were Files on the UK store only, referenced from shared theme code → shared images belong in `assets/`; store Files only for store content. · doc.
- **L-053** · 2026-11-18 · Replacing an image changed its URL → use `fileUpdate(originalSource)` to keep the filename (`tools/store-audit/replace_file.py`). · doc.
