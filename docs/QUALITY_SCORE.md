# Quality Score

Where the codebase is strong and where it is weak, so the next session knows where risk sits. Update after a significant session or before a new phase.

**Grades.** A: verified, clean, easy for an agent to follow, mechanically checked. B: verified on the draft, mostly clean, gaps in docs or checks. C: works with known gaps or hard-to-follow code. D: broken or structurally unsound.

No automated browser tests exist yet, so nothing is above B on behaviour. Verification today = `./init.sh --full` + manual draft checks.

## Pages and components

| Area | Grade | Verified how | Key gaps | Updated |
|---|---|---|---|---|
| Homepage | B | Draft at 390/1440, trust chips in first viewport | Tolstoy carousel empty (cause unknown); client still iterating | 2026-11-20 |
| PDP (sections + buy box) | B | Draft on Laminine, Omega, Lamiderm, one-time products | Older `lp-pdp-*` files hold em dashes in code (guard WARN); product templates at 20 to 23 of 25 sections | 2026-11-20 |
| Science page | C | Draft | Half of the mockup not built (`sci-002`); studies duplicated in two templates by design | 2026-11-20 |
| Company page | B | Draft | Timeline icons cut from a mockup | 2026-11-20 |
| Cart drawer | B | Draft, US checkout reached | Share Your Cart depends on an external API (about 0.9 s) | 2026-11-20 |
| Referral dialog | B | US draft end to end | Depends on Teqnavi app markup and reload behaviour; breaks silently if the app changes | 2026-11-20 |
| Navigation and footer | B | Draft | None known | 2026-11-20 |
| News redesign | B | Unpublished theme | Bloggle content CSS quirks; awaiting review | 2026-11-20 |

## Layers

| Layer | Grade | Enforcement | Key gaps | Updated |
|---|---|---|---|---|
| Template / section-group JSON | A | Guard: JSON, 25-section limit, schema ranges | Block-count limits not checked | 2026-11-20 |
| `config/settings_data.json` | A | Guard: ranges vs settings_schema | App embed blocks not validated | 2026-11-20 |
| Liquid sections/snippets | B | Theme-check ratchet (no new errors) | No render tests | 2026-11-20 |
| `assets/lp-premium.css` / `.js` | B | Guard: amber-deep colour warning | One large file each; no lint | 2026-11-20 |
| Store branches | B | `tools/store-audit/audit.py` | Sync is manual per branch (`sync_branch.py`) | 2026-11-20 |
| Harness and docs | B | `init.sh` | New; title-case sweep not scripted | 2026-11-20 |

## Change history

### 2026-11-20
- First scoring, at harness adoption. JSON and settings layers promoted to A by the new guard.
