# Storefront: Pages and Components

Where each part of the redesign lives and what it depends on. Rules for look and copy are in CLAUDE.md; reasons are in [../DECISIONS.md](../DECISIONS.md).

## Homepage (`templates/index.json`)

- Order: `lp-home-hero` (three benefits, one button, trust chips in the first viewport) · `lp-press` · `lp-home-steps` (How It Works, play-once clips `lp-home-step-*.mp4`) · `lp-product-tabs` (Best Sellers hand-picked via the `products` setting: LAMININE, CELLNERGY WELLNESS, IMMUNE+++, CELLNERGY FOOTCHARGE; then Skin Health, Frequency) · `lp-science` · `lp-home-life` (six brand photos) · reviews · `lp-home-cats` (`lp-cat-*.jpg`) · `lp-home-promos` · `lp-home-faq` · `lp-guarantee`.
- Disabled but kept: `lp-home-offer`, `lp-home-pairs`, `lp-home-cta`.
- The developer reviews on a phone: promo cards stack, buttons and tags never wrap, no offer repeated in two blocks, tight section gaps.

## Navigation

- Mega menu and mobile menu (Figma build). Headlines larger than links, title case, `--lp-amber`.
- Language selector `snippets/lp-lang-switch.liquid` drives Weglot's JS API (same URL, translated in place). Weglot's own switcher is hidden by CSS.
- Footer: sand `#F3EFE7` (`footer_background` in settings_data), logo `LifePharm_logo_mono_ink.png`, orange headings. Footer icon strip hidden on product pages.

## Product page (`templates/product*.json`)

- Story sections `sections/lp-pdp-*.liquid` read `product.metafields.custom.*` (text_benefits, phase_1..3, text_ingredients, value_1..5, header_*). Merchant metafield em dashes are rendered as commas. Never edit the metafields.
- Buy box: `snippets/lp-pdp-summary.liquid` (Ideal-for icons `lp-benefit-*.png`), size cards in `snippets/option-value.liquid` (`lp_card`, fixed 3 columns, savings chip vs single-bottle unit price), Skio plan picker, trust tiles, then the payment note `snippets/lp-hsa-fsa.liquid` (HSA/FSA line; shown per store from Theme settings > Payment notes, never from a template block; D-064), How to Use accordion.
- Variant changes the main image: script in `snippets/product-gallery.liquid` (L-011).
- Rating row: real reviewer faces on LAMININE only (from their Stamped photos); other PDPs show stars and count.
- Product templates use 20 to 23 of 25 sections (TD-007).

## Content pages

- **Science** (`page.science.json` and `page.our-studies.json`, same stack): `lp-sci-hero`, `lp-sci-intro`, `lp-sci-chapters` (#how-it-works), `lp-sci-studies` (#studies, product filter chips, first product open), `lp-sci-standard`. Add a study as a `study` block in **both** templates; its products field must match a filter name.
- **Company / About Us** (`/pages/company`, `page.company.json`; `/pages/about` is unused): `lp-about-*` sections (hero facts, founder story, credo, values, team with bio dialog, logos) plus `lp-history` (milestone `event` blocks: image, date, text).
- **Join Us** (`page.join-us.json`): identical on all branches. US and EU render it on page handle `join-us-1724800657`; UK on `join-us`.
- **Collection**: banner `lp-collection-all-products.jpg` (+ `-mobile-v3.jpg`, 390x480 box). Product-card hover photo from Files `lp-hover-<handle>.jpg` (`snippets/product-card.liquid`), else the second media. Filters: `snippets/lp-collection-filters.liquid` (layout "Filter bar" in `main-collection`; D-048): chip links built from `collection.filters`, a Filter sheet (`<dialog>`) under 1000px, a short sort list; state is kept across the section refresh by `initFilterBar` in `assets/lp-premium.js`. Filter names and values come from Search & Discovery; a filter that cannot narrow the list is not shown. Check with `tools/qa/collection_filters_check.py`.

## Cart drawer

- `sections/cart-drawer.liquid` + `snippets/lp-cart-line.liquid`; JS in `assets/lp-premium.js`; CSS in the "Cart drawer (premium revamp)" block of `assets/lp-premium.css`.
- One action: Checkout (overlay-group `show_view_cart_button: false`). Discounts as chips plus a Savings row.
- Free delivery: one `.lp-ship` card for both states; Liquid computes `lp_fd_reached` with the same rule as the free-shipping bar; JS rechecks with `Shopify.currency.rate`, fills to 100%, then plays `assets/lp-free-delivery.mp4` once per session (sessionStorage `lp-fd-played`). Row `[data-lp-ship-row]` shows "Delivery: Free". UK rule: free standard delivery at £150 or more, otherwise £7.95.
- Share Your Cart: `snippets/lp-share-cart.liquid`, calls the external lpshopify shared-cart API; delegated events (L-013).

## Referral dialog (checkout confirmation)

- Markup and CSS `snippets/lp-referral-nudge.liquid` (`<dialog data-lp-refq>`); JS `initReferralCheckout` in `assets/lp-premium.js`; animation `assets/lp-referral-anim.mp4`.
- Trigger: capture-phase `submit` on forms whose submitter is `name="checkout"` (drawer and /cart).
- Shows only if: Teqnavi button `.referral-banner__name--clickable` exists, no referrer yet, localStorage `lp-ref-optout` is not `1`, and the customer has no `Exigo.CustomerId` metafield (not rendered at all for them).
- "Add My Referrer" closes the drawer and clicks the app button. The app sets cart attribute `Referral` and cookie `refId`, then reloads to `?ref=<webalias>`; the intent survives in sessionStorage `lp-refq-resume`, so the drawer and a confirmed dialog reopen. The theme writes cart attribute `Referrer Name`.
- "No, Continue to Checkout" re-submits with `requestSubmit` (after a reload: `/checkout`).
- Depends on the Teqnavi app block in `sections/header-group.json`; the app's own bar is collapsed by CSS.
- Mobile menu keeps "Were you referred by someone?" (`.lp-menu__ref`), also hidden for Exigo customers.
