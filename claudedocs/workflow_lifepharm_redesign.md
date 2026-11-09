# LifePharm UK — Premium CRO Redesign Workflow

Target: draft theme `Lifepharm/master` (ID 189821452674), synced from GitHub `kemasghani/Lifepharm@master`.
Live theme is never touched. Base: Impact 7.0.1.

## Design direction: "Clinical Luxury"
- Warm ivory canvas `#FBF9F5`, ink `#15171B`, brand amber `#E8890C` as accent only (stars, highlights, progress).
- Primary CTA ink pill (AAA contrast), amber glow on hover. Checkout colours untouched.
- Type: Playfair Display (editorial headings, tight tracking) + Inter (body, 0 tracking).
- Generous whitespace, 20px card radius, soft layered shadows, hairline borders.
- Real trust facts only (60-day guarantee, Made in USA, NSF tested, clinically studied, free UK delivery £150+, 978+ Laminine reviews). No invented stats.
- UK/ASA-safe copy: keep the site's own wording + disclaimer, no medical cure claims.

## Phases
1. **Design tokens** – `config/settings_data.json` (colours, fonts, radius, motion, quick-buy on).
2. **Global design layer** – `assets/lp-premium.css` loaded after theme.css: typography rhythm, buttons, header (glass sticky), announcement, product cards, PDP, cart drawer, footer, forms, focus states.
3. **Motion & loading system** – `assets/lp-premium.js` + CSS:
   cross-document View Transitions, top navigation progress bar, skeleton shimmer for images,
   add-to-cart loading/success states, scroll reveal, count-up, reduced-motion support.
4. **New CRO sections** – `lp-hero`, `lp-trust-bar`, `lp-shop-by-goal`, `lp-science`, `lp-guarantee`.
5. **Homepage recomposition** – `templates/index.json` uses new sections + existing merchant content (bestsellers, press logos, reviews app, Instafeed).
6. **PDP CRO** – trust row under buy buttons, sticky ATC polish, guarantee snippet.
7. **HyperFrames brand film** – rendered MP4/WebM hero loop (offline render, lazy-loaded, poster fallback).
8. **QA** – `shopify theme check`, skill validator, preview at 375/768/1440, push → auto-sync to draft.

## Checkpoints
- After each phase: theme check passes, preview renders, no console errors.
- Never push to a branch connected to the live theme.
