# Workflow: Figma menu, header and homepage (systematic, deep)

**Source:** Figma `qu2GgBdooNVuxcrO5lmFaH`. The MCP had no access, so the frames were read in the browser.
- Menu 33-3764
- Open 33-3942
- Hp 33-3413

**Target:** the draft theme only. Rules are in `CLAUDE.md`.

## Analysis

### Menu frame (390 wide)
- Orange announcement bar.
- Header: X (close) on the left, logo in the centre, account and cart on the right.
- Heading "SHOP BY CATEGORY", in Playfair uppercase.
- Category rows: grey #F2F2F2 tile, 72px image, bold label, chevron.
- "Shop All" button: orange, square corners.
- Text links: About, Blog, Contact.

### Open frame
- The same header.
- Promo card: navy, "TRY IT RISK FREE FOR 60 DAYS", Lamiderm bottle.
- Heading "SHOP NUTRITIONAL".
- Product rows: image, name, price, compare-at price, chevron, and a "Best Seller" badge.
- "Shop All Nutritional" button.

### Hp frame
1. Hero
2. Press logos
3. Shop by category
4. "Better health starts here": tabbed product grid (Shop All / Nutritional / Skin Health / Frequency)
5. "A full system, not just a supplement": bullets, image, CTA
6. "Try it risk free for 60 days"

### Data
- `main-menu` > Shop has three children: Nutritionals, Skin Health and Frequency Regeneration. Each links to a collection.
- Top-level menu items: Science, Company, Join Us, News.
- Collections: `nutritionals` (7), `skin-health` (2), `frequency-regeneration` (9), `all` (12).

### Conflicts and resolutions
| Item | Figma | Resolution |
|---|---|---|
| Headings | Playfair uppercase | Adopt. Playfair Display is a guideline font. Uppercase only for short display headings. |
| Button text | white on orange (2.5:1) | Keep #1F1E20 text (AA). Adopt square corners (4px). |
| Hero badge | "Over 10,000 five star reviews" | Not a verified fact, so omit it. |
| "Best Seller" badge | shown on a product | Show only when the product is tagged `best-seller`. Never invent it. |
| Announcement copy | "Spend $50+ … USA" | UK fact: "Free UK delivery on orders over £150". |
| Hero art | navy Lamiderm | Asset not supplied. Keep the current hero (trust chips above the fold) with Figma typography. |

## Phases

### P1: Foundations (global, replaces rather than adds)
1. Self-host Playfair Display Regular (woff2) next to Metropolis. Display headings h1 and h2 use Playfair 400 uppercase.
2. Button radius 60 → 4. Primary button is orange with dark text (unchanged).
3. Update `CLAUDE.md` typography rules.

### P2: Announcement and header
1. Enable the Impact announcement bar: #F18A00 background, #1F1E20 text, UK delivery message.
2. Mobile header layout:
   - Left: hamburger, which morphs into an X.
   - Centre: logo.
   - Right: account and cart. Search moves into the menu.

### P3: Mobile menu (replaces Impact `navigation-drawer#header-sidebar-menu` and `navigation-panel` on mobile)
1. New `snippets/lp-mobile-menu.liquid`:
   - Level 1: "Shop by category" rows built from the Shop children, with images from header settings.
   - Shop All button and secondary links.
   - Level 2 panels per category:
     - back control
     - promo card
     - category heading
     - first 4 products (image, title, price, compare-at, honest badge)
     - "Shop all {category}" button
2. JS (`lp-premium.js`):
   - Toggle with the header kept visible (sits under the header).
   - Panel slide.
   - Focus trap, Esc, scroll lock, history back.
   - Close on resize to lg.
   - `prefers-reduced-motion`.
3. Remove the old drawer markup from the header. Desktop keeps the mega menu.

### P4: Homepage merge
1. Order: hero → press logos → shop by category → product tabs (new) → science → full system (new) → reviews → Cellnergy feature → mission → guarantee (Figma style) → chat CTA.
2. New `sections/lp-product-tabs.liquid`:
   - Tabs are real collections. Panels are server-rendered (no fetch).
   - Cards: rating, title, summary, price, quick add through `/cart/add.js` with the theme cart refresh.
   - Replaces `featured-collection`.
3. New `sections/lp-system.liquid` (Figma "A full system"): bullets with orange markers, image, CTA.
4. Restyle the press logos (monochrome strip, mobile scroll), the shop-by-category heading and the guarantee card to the Figma style.
5. Motion: no new infinite motion. Reveal only on visuals (rule 4).

### P5: Verification
- Theme check (errors only in touched files).
- JSON validation: 25 sections or fewer.
- Puppeteer at 390 and 1440:
  - menu open and close, panel navigation, focus and Esc
  - quick add to cart
  - no horizontal scroll, no JS errors
  - first-viewport chips still visible

## Checkpoints
- Commit and push after each phase.
- Verify on the draft preview before moving on.
- Never publish.
