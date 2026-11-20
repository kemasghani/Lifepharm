# Project History

How the LifePharm redesign got to where it is, day by day. Reconstructed on 2026-11-20 from 220 commits on `master` plus the session notes kept so far. Add a dated block when a milestone lands; day-to-day detail belongs in [progress.md](progress.md).

**People.** Developer: Kemas (Treelogy). Client reviewer: Letisha (LifePharm marketing). Owner approval is needed to publish anything.

**Scope today.** One Impact 7.0.1 theme codebase for the UK, US and EU stores, a separate Dawn redesign for the News store, analytics on all four stores, and integration work around Exigo (the MLM back office). The Exigo to Klaviyo service is a separate private repo (see [knowledge/off-repo-projects.md](knowledge/off-repo-projects.md)).

---

## Phase 1: Foundation and first redesign (2026-11-10)

- Repo created, UK theme imported, connected through the Shopify GitHub integration to draft theme "Lifepharm/master" (189821452674).
- First "premium CRO" pass: design tokens in `assets/lp-premium.css`, a motion layer, new `lp-*` homepage sections, a HyperFrames brand film in the hero, cart CRO (checkout as the one primary action).
- Editorial PDP: metafield-driven `lp-pdp-*` sections, so one layout serves every product.
- **First silent-rejection incident:** a template change never reached the draft. Two bisect commits proved the cause: product templates went over Shopify's 25-section limit. Also found: an out-of-range setting makes Shopify drop the whole file. Both are now checked by `./init.sh`.
- Typography started as a "Seed-style" single sans (Inter); replaced the next day.

## Phase 2: Brand guide and Figma build (2026-11-11)

- Motion rules settled: one scroll reveal per section, on a visual only; no infinite decoration.
- Copy pass: no em dashes, calmer voice; metafield em dashes normalised at render time.
- **Brand guide adopted** (Quick Style Guide 2024): Metropolis self-hosted, Black 90% ink, Pantone orange CTAs with dark text.
- Figma build P1 to P4: Playfair display headings, announcement bar, new mobile header and menu, homepage with press strip, categories and tabbed product grid.
- Referral slide-in built, then removed the same day (owner: referrals are detected server side).
- One sticky add-to-cart component for every breakpoint.
- Exigo Web Services API documentation crawled into `docs/exigo-api/` (294 operations).
- Homepage rebuilt as a Laminine landing page, **rejected** ("it became like a PDP"), rebuilt as a brand homepage that pushes Laminine inside it.
- GA4: four stores into one property through the Google & YouTube app.

## Phase 3: First client review (2026-11-12)

- Orange moved to the live-site #FF8F00 (Letisha).
- Footer and comparison panel tried on Pantone 423 grey, found too dark, moved to light grey #E2E3E4.
- Science and Our Studies merged into one story page; top rebuilt from Letisha's Dropbox mockup.
- Letisha's feedback round 2: title case everywhere, brand orange circle icons for "Ideal for", variant choice changes the main image, comparison full width.
- About Us: company history timeline above leadership.
- Referral slide-in restored.
- Client preferences written into CLAUDE.md section 7 as the standing brief.

## Phase 4: Trust, imagery and buy box (2026-11-13 to 11-14)

- Trust tiles went through 13 commits in one day (PNG badges, SVG, line icons, back again) before settling on frameless line icons drawn from the brand badges. See lesson L-020.
- Kive AI photography on the homepage and menus; labels checked at full resolution.
- How to Use moved into one buy-box accordion; Ideal-for icons for every product.
- PDP gallery: large square image with a thumbnail row; savings chips on multi-packs; sticky columns.
- Homepage rebuilt on the "high-converting anatomy": hero with three benefits and one button, How It Works steps with play-once clips.
- Comparison chart from Letisha's nine-row table; reviews restyled.
- **Multi-store architecture**: `master` = code, `uk`/`us`/`eu`/`news` = store data, `tools/store-audit/`.

## Phase 5: Audits and analytics (2026-11-15 to 11-16)

- Homepage daily-life gallery from Letisha's social media Dropbox.
- Azure access working (resource group for integration work).
- Apps audit across four stores: 36 apps found, PDF proposal for Letisha.
- Microsoft Clarity: one project per store, linked to GA4.
- Minimalist cream category tiles from Kive and Higgsfield.

## Phase 6: Second client review and polish (2026-11-17)

- Letisha's rules made permanent: only #FF8F00 for orange text and icons, product names in brand capitals, title-case tabs and labels.
- **Title-case sweep:** 207 strings across 30 templates fixed after a miss ("Still unsure?"). Became lesson L-030 and a QA step.
- Header language selector driving Weglot.
- Footer moved from grey to warm sand with an all-dark-grey logo.
- News store redesign started on Dawn, on its own branch.
- Runtime apps check: idle and broken apps identified (Intelligems, Koala, Instafeed, Tolstoy, Magefan).

## Phase 7: Cart, referral at checkout, store rollout (2026-11-18)

- Product-card hover photos (Soona shoot, Kive, Higgsfield), new collection banner and Shop All tile.
- Cart drawer revamp: one Checkout action, discount chips, a free-delivery component with a play-once truck clip.
- Share Your Cart moved into a snippet; opens at once.
- **Referral became a checkout confirmation dialog** (fourth form of the referral UI), confirmed state after the Teqnavi reload, `Referrer Name` cart attribute.
- Company page revamp (`lp-about-*` sections).
- **All store branches set equal to `master`** (design must be the same everywhere); US and EU drafts connected; 47 (US) and 40 (EU) live-only templates ported; US header menu `main-menu-redesign`.
- Exigo order sync traced end to end (Shopify "Exigo" app webhook, Teqnavi Sync Engine, lpshopify middleware).
- Static egress IP for Exigo calls (the home ISP address rotates).
- News redesign moved onto the `news` branch, connected to an unpublished theme.

## Phase 8: Exigo rules and team page (2026-11-19 to 11-20)

- Verified in Exigo: commission credit follows the customer's enroller; an order's referral only counts when the customer is new. So the referral prompt is **skipped for existing Exigo customers**.
- Company page team edits (removals, new member, three per row).
- PDP gallery cursor restored.
- Exigo to Klaviyo service (lpsync) built and reviewed in the private marketing repo; Klaviyo flows kept as drafts.
- Teqnavi Sync Engine and Enrollment Handler embeds copied into the US and EU branches to match live.
- **Harness adopted** (this document set, `init.sh`, `tools/harness/`), following walkinglabs/learn-harness-engineering.
