# Workflow: merge Science + Our Studies into one page

Strategy: systematic · Executor: Claude Code (theme repo → draft theme 189821452674)
Date: 2026-11-12 · Request: Letisha ("combine the new science page with our studies page… listed together on one page")

## Inputs (audited)
- `templates/page.science.json`: hero "Crack Open Youthful Living", intro, 4 media-with-text chapters (repair, how it works, additional support, science-backed benefits), "We don't cut corners" + button to Our Studies. Advisory board sections are **disabled by the merchant**, so they stay out.
- `templates/page.our-studies.json`: hero, marquee facts (18+ clinical studies, regeneration patent Sept 2020, Monde Selection Gold, Dermatest 5 stars), 8 product rich-text blocks with **22 study links** (3 duplicates across products → 19 unique).
- Dropbox "new science page" design file: not opened (download needs owner OK). Built from the live page content plus the site design system.

## Story arc (storytelling-web, scroll mode)
1. **Hook**: "Regeneration, studied". One promise, four real proof chips, jump links.
2. **Problem → mechanism**: four numbered chapters (repair slows with age → growth factors signal → building blocks → what studies suggest).
3. **Proof (key moment)**: the published studies library, filterable by product, each study tagged and linked to its source.
4. **Close**: "We don't cut corners" quality standard, real trust facts, CTA to shop. Disclaimer.

## UI/UX rules applied (ui-ux-pro-max + project CLAUDE.md)
- Style guide only: Playfair uppercase display headings, Metropolis UI, ink #414042, accent #FF8F00, amber-deep #A65A00 for orange text, ivory/sand surfaces. (The tool's generic navy/gold/Exo suggestion is rejected.)
- Filter chips: real `<button>`s with `aria-pressed`, 44px targets, live result count, works without JS (all studies visible).
- Links to studies open in a new tab with `rel="noopener"` and an "opens in new tab" hint.
- Contrast ≥ 4.5:1 for text, visible focus, no layout-shift hovers, no infinite motion, no reveal on text.
- Copy: British English, no em dashes, no exclamation marks, soft claims. Fixes: "reverse signs of aging" → "support healthy ageing"; "all 22 essential amino acids" (inaccurate) → "amino acids, the building blocks of protein"; study title typo "Redudes" → "Reduces"; all-caps titles → title case.

## Build
| Section | File | Notes |
|---|---|---|
| Hero | `sections/lp-sci-hero.liquid` | eyebrow, H1, lead, 4 fact chips, jump links, image |
| Chapters | `sections/lp-sci-chapters.liquid` | blocks: chapter (image, title, text) |
| Studies | `sections/lp-sci-studies.liquid` | blocks: study (title, url, source, products); JS filter |
| Standard | `sections/lp-sci-standard.liquid` | closing, trust facts, CTA, disclaimer |
| Templates | `page.science.json`, `page.our-studies.json` | identical section stack, so both URLs show the merged page |

## Launch notes (owner, not done by Claude)
- After publishing: add URL redirect `/pages/our-studies` → `/pages/science#studies` and point the "Our Studies" footer link to `/pages/science#studies` (admin navigation, live data).

## Validation
Theme check (no new errors), JSON valid, ≤25 sections per template, draft preview at 390 / 1440: no horizontal scroll, no JS errors, filter works, contrast checks.
