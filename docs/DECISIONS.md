# Decision Log

Durable decisions and **why** they were made, newest at the bottom of each area. When a decision is reversed, do not delete it: add the new one with `supersedes D-NNN`, so the next session can see the whole path and does not re-propose a rejected option.

Standing rules that follow from these decisions live in [CLAUDE.md](../CLAUDE.md). This file holds the reasoning.

`D-NNN · date · decision · by · why`

---

## Workflow and platform

- **D-001** · 2026-11-10 · Work on a GitHub-synced draft theme only; never publish without the owner. · owner · The live theme carries Skio and live orders.
- **D-002** · 2026-11-14 · One codebase, branch per store: `master` = code, `uk`/`us`/`eu`/`news` = store data (`merge=ours`). · developer · One redesign everywhere without broken handles. Spec: [multi-store/ARCHITECTURE.md](multi-store/ARCHITECTURE.md).
- **D-003** · 2026-11-18 · All store branches carry the same design as `master` ("pokoknya harus sama"); only app embeds, handles and market copy differ. · developer · Supersedes the slower per-store adoption idea in D-002.
- **D-004** · 2026-11-18 · New header (Shop / Science / Company / Join Us / News) for every store. · Letisha · One brand structure.
- **D-005** · 2026-11-17 · News store redesigned on Dawn in its own branch (`news`), not the Impact codebase. · developer · It is a blog store with no products.
- **D-006** · 2026-11-20 · Adopt the harness: repo is the system of record; `init.sh` plus `tools/harness/` are the verification path. · developer · Knowledge was spread over chat, memory and scratchpads.

## Brand and visual

- **D-010** · 2026-11-11 · Follow the LifePharm Quick Style Guide 2024 (Metropolis, Black 90% ink). · developer · Client brand source of truth.
- **D-011** · 2026-11-11 · Display headings in Playfair Display 400; Metropolis for everything else. · Figma build · Supersedes the 2026-11-10 Inter "Seed-style" headings.
- **D-012** · 2026-11-12 · Headings in title case, never all caps. · Letisha · Supersedes the Figma uppercase display headings.
- **D-013** · 2026-11-12 · Accent orange #FF8F00 (live-site orange). · Letisha · Pantone 144 #F18A00 looked dull.
- **D-014** · 2026-11-14 / 11-17 · All visible orange text, icons and ticks use #FF8F00; `--lp-amber-deep` only for focus, shadow and gradient depth. · Letisha · The deep tone reads brown. Trade-off: about 2.2:1 on ivory for small orange text, accepted by the client.
- **D-015** · 2026-11-12 · No dark panels. Ink #414042 rejected as too heavy, #888B8D "still too dark", so the light tint #E2E3E4 is used. · Letisha
- **D-016** · 2026-11-17 · Footer on warm sand #F3EFE7 with an all-dark-grey logo; grey #E2E3E4 kept only for the PDP comparison. · Letisha · Grey footer "doesn't really go with the rest of the site". Supersedes the footer part of D-015.
- **D-017** · 2026-11-11 · CTA buttons orange with near-black text (7.3:1); never white on orange. · developer · Accessibility.
- **D-018** · 2026-11-14 · Ingredient written "Fertilized Avian Egg Extract" (American spelling, capitalised) wherever named. · Letisha · Explicit exception to British English.
- **D-019** · 2026-11-14 / 11-17 · Product names in brand capitals everywhere: LAMININE, OMEGA+++, IMMUNE+++, DIGESTIVE+++. · Letisha
- **D-020** · 2026-11-13 · Trust tiles: frameless line icons drawn from the brand badges, same size, stroke and colour. · Letisha and owner · Final after 13 commits of alternatives (see L-020).
- **D-021** · 2026-11-16 / 11-17 · Imagery minimalist and premium: cream backgrounds, soft daylight, one subject, no baked-in text. · developer and Letisha

## Motion

- **D-030** · 2026-11-11 · One scroll reveal per section, visuals only; no infinite decorative motion; no hero film. · developer · Supersedes the 2026-11-10 hero brand film and rotating rings.
- **D-031** · 2026-11-11 · Animations made with HyperFrames, rendered to small MP4s that play once. · developer

## Pages and components

- **D-040** · 2026-11-11 · Homepage is a brand homepage that pushes LAMININE inside it, not a Laminine landing page. · developer · First version "became like a PDP". Reason for the LAMININE focus: it is by far the largest seller on every store (figures in private notes).
- **D-041** · 2026-11-14 · Homepage follows the "high-converting anatomy" (hero with three benefits and one button, How It Works, best sellers, science, reviews, categories, promos, FAQ, guarantee). · developer
- **D-042** · 2026-11-17 · Homepage tabs: Best Sellers (hand-picked four), then Skin Health and Frequency. · Letisha
- **D-043** · 2026-11-12 · Science and Our Studies merged into one page; no "All" tab; first product open. · Letisha
- **D-044** · 2026-11-12 · Company history timeline on About Us above leadership, icons all visible, text on click. · Letisha
- **D-045** · 2026-11-13 · How to Use lives in one buy-box accordion; timeline strip removed. · Letisha · Say it once.
- **D-046** · 2026-11-18 · Cart drawer has one action (Checkout); View Cart off. · developer

## Referral (history of a requirement that changed four times)

- **D-050** · 2026-11-10 · Referral bar restyled (ink). · developer
- **D-051** · 2026-11-11 · Slide-in prompt from the left with a HyperFrames illustration. · developer · Supersedes D-050.
- **D-052** · 2026-11-11 · All referral UI removed; referrals detected server side. · owner · Supersedes D-051.
- **D-053** · 2026-11-12 · Slide-in restored. · owner · Supersedes D-052.
- **D-054** · 2026-11-18 · Referral becomes a confirmation dialog when Checkout is pressed, with "Don't show this again". · developer · Supersedes D-053.
- **D-055** · 2026-11-19 · No referral dialog or menu entry for logged-in existing Exigo customers. · developer · Verified in Exigo that their orders always credit the existing enroller (L-042).

## Analytics and integrations

- **D-060** · 2026-11-11 · All four stores report to one GA4 property through the Google & YouTube app; no theme gtag or GTM; staging excluded. · owner · Subdomains share the `_ga` cookie; one stream avoids double counting.
- **D-061** · 2026-11-16 · One Microsoft Clarity project per store, all linked to GA4. · developer · Same URL paths across stores; per-store consent.
- **D-062** · 2026-11-18 · Klaviyo routing by store, not language: US store to Klaviyo US; UK and EU stores to Klaviyo Europe. · developer
- **D-063** · 2026-11-20 · WhatsApp moves to Klaviyo; HubSpot V5 workflows are only the reference spec (not running). · Letisha
