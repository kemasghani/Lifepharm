# LifePharm UK theme: project rules (always follow)

Shopify **Impact 7.0.1** theme for uk.lifepharm.com. Every change in this file is a standing rule. If a request conflicts with a rule, point it out before acting.

## 1. Workflow and safety

- This repo syncs through GitHub to the **draft theme "Lifepharm/master" (ID 189821452674)**. Pushing to `master` updates the draft only.
- **Never publish the theme, and never touch the live theme** ("Updated copy of Skio Go live", ID 188195209602), without the owner's explicit approval in chat.
- Preview: `https://uk.lifepharm.com/?preview_theme_id=189821452674`. For curl, use a cookie jar (`-c/-b`), otherwise the live theme is served.
- JSON templates: **25 sections at most**, otherwise Shopify silently rejects the file. Validate JSON before pushing.
- In `config/settings_data.json`, edit only the `"current"` block, never the presets.
- `.env` holds an admin token for the **US** store. It is read-only for reference and never committed.
- Shopify work: use the `shopify-plugin:*` skills and validate against the live schema (see the global CLAUDE.md).
- After changes: run theme check, push, then verify on the draft preview at 390px and 1440px. Check for no horizontal scroll and no JS errors.

## 2. Brand guideline (LifePharm Quick Style Guide 2024)

Source: Dropbox "Branding Resources" > `LifePharm-QuickStyleGuide-2024.pdf`. Fonts are in the `Fonts` folder.

### Typography
- **Metropolis** is the only web font. It is self-hosted in `assets/metropolis-*.woff2` and loaded in `layout/theme.liquid`.
  - Display headings (h1, h2): **Playfair Display, weight 400, title case** (first letter of each word). Never all caps. Product names stay as the brand writes them (LAMININE).
  - Small headings (h3) and UI: Metropolis SemiBold (600).
  - Body: Metropolis Regular (400). Buttons and labels: SemiBold (600).
  - Eyebrows and small labels: Metropolis **ExtraBold (800)**, UPPERCASE, `letter-spacing .1em`.
- Two families only: Playfair Display for display headings, Metropolis for everything else.
- **No italics** in headings and no decorative or "weird" type styles. Accents use colour only.
- Do not add Google Fonts or any other font family.

### Colour
| Token | Value | Use |
|---|---|---|
| `--lp-ink` | **#414042** (Black 90%) | text. **Not for large panels**: the client finds dark panels too heavy |
| Panel grey | **#E2E3E4** (light tint of Pantone 423) | footer, comparison section. Ink text on it |
| `--lp-amber` | **#FF8F00** (live-site orange, chosen by Letisha 2026-11-12; was Pantone 144 #F18A00) | brand accent, **all primary CTA buttons**, badges, icons |
| `--lp-amber-deep` | #A65A00 | orange **text** only (AA contrast on light backgrounds) |
| Logo grey | #888B8D (Pantone 423) | logo and illustration only. Too dark as a panel background (tried and rejected) |
| `--lp-muted` | #6B6A6C | secondary text |
| `--lp-ivory` / `--lp-sand` | #FBF9F5 / #F3EFE7 | backgrounds |

- **Primary buttons are #FF8F00 with #1F1E20 text** (7.3:1). Never use white text on #FF8F00 (2.3:1). Do not bring back dark or "pale black" buttons.
- Product colours, for product-specific accents only:
  - Laminine #FF8F00
  - Omega+++ #E1251B
  - Digestive+++ #3DAE2B
  - Immune+++ #F2CD00
  - Lamiderm Apex / Omnia #0033A1 + gold #A48A3D
  - Cellnergy #D2232A + #898B8E
- Keep text at WCAG AA (4.5:1) or better.

## 3. Copywriting

- Natural, warm, premium **British English** ("recognised", "fertilised", "ageing").
- **Never use em dashes (—)**. Use commas, colons or full stops. Metafield em dashes are normalised to commas at render time.
- No exclamation marks, no hype, no filler buzzwords. Clear beats clever. One idea per section.
- Health claims stay soft and compliant ("supports", "helps"). Never "cures", "treats", "lengthens".
- Use only real trust facts:
  - 60-day money-back guarantee
  - Made in the USA
  - Fully NSF tested
  - Clinically studied
  - Free UK delivery over £150
  - 978+ Laminine reviews
- Never invent ratings, numbers or testimonials.
- Do not edit merchant product data (metafields). Adapt presentation in the theme instead.

## 4. Motion and UX

- **Scroll reveal: at most one per section, on a visual only** (image, card group). Never on headings, body text, prices, tables, FAQ or the buy box.
- Reveal timing: 600ms, 16px travel, ease-out `cubic-bezier(.16,1,.3,1)`, plays once.
- **No infinite decorative animation**: no spinning rings, floating or bobbing elements, drifting glows or hero films.
- Never hide above-the-fold or LCP content behind JS (opacity 0).
- Always respect `prefers-reduced-motion`.
- Animations are built with **HyperFrames**, rendered to small MP4 assets and played once. Runtime UI motion (slide-ins, accordions) is CSS.
  - HyperFrames source projects: `~/Documents/Lifepharm-pdp-film` and `~/Documents/Lifepharm-referral-film`.
- Touch targets are at least 44px. Focus states are visible. Layout has no horizontal scroll at 390px.
- The homepage hero must show the trust chips in the first viewport (1280×720 and up, and mobile).

## 5. Key components

- Referral UI: **restored 2026-11-12 at the developer's request** (it had been removed on 2026-11-11). `snippets/lp-referral-nudge.liquid` slides in from the left, closes with X and minimises to a "Referred?" tab; it drives the Teqnavi referral app block in `sections/header-group.json`, whose own bar is collapsed by CSS. The HyperFrames animation is `assets/lp-referral-anim.mp4`. Keep attribution logic in the app.
- PDP sections: `sections/lp-pdp-*.liquid`. They are metafield-driven (`product.metafields.custom.*`).
- Size cards: `snippets/option-value.liquid` (`lp_card`). The grid is fixed at 3 columns.
- Design tokens and global overrides: `assets/lp-premium.css`.

## 6. Exigo integration knowledge

- `docs/exigo-api/` is the full crawl of the Exigo Web Services API docs (https://api.exigo.com/3.0/, version v2025.11.7.6). It covers all 294 operations, including 42 that are in the WSDL but not in the docs menu, plus 792 types, 43 enums and the company-specific lookup fields.
- **Always read it before writing Exigo integration code.** Start with `docs/exigo-api/README.md` for transports, auth and the index, then the category file in `operations/`, then `types.md` and `enums.md`. Do not guess field names, REST routes or enum values from memory.
- Company-specific values (warehouses, ship methods, price types, etc.) need LifePharm's Exigo API credentials (see `company-lists.md`).
- Refresh with `python3 docs/exigo-api/tools/crawl.py && python3 docs/exigo-api/tools/parse.py && python3 docs/exigo-api/tools/gen.py`.

## 7. Client design preferences (Letisha Suyanto, LifePharm)

Collected from her reviews on 2026-11-12. Treat these as the brief for every new design. If a new request conflicts, ask.

### Look
- **Light and bright.** No dark panels. Grey surfaces are the light tint #E2E3E4; orange is the bright live-site orange #FF8F00.
- **Titles in title case**, never full caps. That includes accordion titles ("How to Use", "60-Day Money-Back Guarantee"), ingredient names and menu headlines.
- **Menu headlines**: larger than the links, title case, orange (use `--lp-amber-deep` so they stay readable).
- **Use the brand's own orange circle icons** (Dropbox "ICONS 2024"; cut versions in Files as `lp-benefit-*.png`) wherever a list of benefits would otherwise be plain text that "gets lost".
- **Follow her Dropbox designs** when one exists for a page. Ask for the source image or video if only the mockup is available.

### Layout
- **Image above its text.** Timelines and step content become columns of cards (image on top), not tabs beside a collage.
- **Charts and tables take the full width**, with the title above them, not beside.
- **Space repeated elements evenly** (for example icons around a product).
- **Every image needs a title or caption** so customers know what they are looking at.
- **Say it once.** Trust icons live in one place per page (the buy box on product pages); no second strip lower down. Remove sections that repeat another one.
- **Keep long content short on screen.** No "All" tab that lists everything; open on the first category. For long timelines show all the icons and reveal the text on click.
- **Related pages are merged** (Science + Our Studies are one page).
- **Disclaimers**: centred, one line on desktop.
- **Options update the visual.** Choosing a variant must change the main image.

### Developer's own standards (same project)
- Product pages are compact: tight gaps between buy-box elements.
- Mobile: a row that does not fit scrolls sideways, and the next item is cut in half so it is clear there is more.
- Things on one row are aligned on one axis; images are sharp on retina (serve 2x to 3x).
- The sticky add-to-cart never sits on top of an open menu or under page content.
- Real customer photos (from their own reviews) beside the rating; never invented.
