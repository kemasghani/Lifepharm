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
  - Headings: Metropolis **Light (300)**, letter-spacing `-0.02em`, line-height `1.1`.
  - Body: Metropolis Regular (400). Buttons and labels: SemiBold (600).
  - Eyebrows and small labels: Metropolis **ExtraBold (800)**, UPPERCASE, `letter-spacing .1em`.
- The guide also lists Playfair Display Bold. It is **not used**: the site keeps one family, by the owner's choice.
- **No italics** in headings and no decorative or "weird" type styles. Accents use colour only.
- Do not add Google Fonts or any other font family.

### Colour
| Token | Value | Use |
|---|---|---|
| `--lp-ink` | **#414042** (Black 90%) | text, dark surfaces |
| `--lp-amber` | **#F18A00** (Pantone 144) | brand accent, **all primary CTA buttons**, badges, icons |
| `--lp-amber-deep` | #A65A00 | orange **text** only (AA contrast on light backgrounds) |
| Logo grey | #888B8D (Pantone 423) | logo and illustration only, not body text |
| `--lp-muted` | #6B6A6C | secondary text |
| `--lp-ivory` / `--lp-sand` | #FBF9F5 / #F3EFE7 | backgrounds |

- **Primary buttons are #F18A00 with #1F1E20 text** (7.5:1). Never use white text on #F18A00 (2.5:1). Do not bring back dark or "pale black" buttons.
- Product colours, for product-specific accents only:
  - Laminine #F18A00
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

- Referral UI: **none in the theme**. The Teqnavi referral app section in `sections/header-group.json` is disabled. The owner will auto-detect referrals from the referral link on the server. Do not add referral prompts or bars.
- PDP sections: `sections/lp-pdp-*.liquid`. They are metafield-driven (`product.metafields.custom.*`).
- Size cards: `snippets/option-value.liquid` (`lp_card`). The grid is fixed at 3 columns.
- Design tokens and global overrides: `assets/lp-premium.css`.

## 6. Exigo integration knowledge

- `docs/exigo-api/` is the full crawl of the Exigo Web Services API docs (https://api.exigo.com/3.0/, version v2025.11.7.6). It covers all 294 operations, including 42 that are in the WSDL but not in the docs menu, plus 792 types, 43 enums and the company-specific lookup fields.
- **Always read it before writing Exigo integration code.** Start with `docs/exigo-api/README.md` for transports, auth and the index, then the category file in `operations/`, then `types.md` and `enums.md`. Do not guess field names, REST routes or enum values from memory.
- Company-specific values (warehouses, ship methods, price types, etc.) need LifePharm's Exigo API credentials (see `company-lists.md`).
- Refresh with `python3 docs/exigo-api/tools/crawl.py && python3 docs/exigo-api/tools/parse.py && python3 docs/exigo-api/tools/gen.py`.
