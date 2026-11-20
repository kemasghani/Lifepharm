# Tech Debt and Risks

Debt we know about and chose to defer. Add a row when you defer something; remove it (with a progress.md note) when fixed.

| ID | Date | Area | Debt / risk | Why deferred | Risk | Next trigger |
|---|---|---|---|---|---|---|
| TD-001 | 2026-11-20 | privacy | `docs/multi-store/*.csv` hold order numbers and IBO webaliases, and the GitHub repo is **public** | Needs the owner's decision (make the repo private, or remove the files and rewrite history) | Customer and affiliate data exposed | Now: ask the developer |
| TD-002 | 2026-11-20 | copy | Em dashes inside older `lp-pdp-*` code (15 lines, guard WARN) | Mostly fallback text and comments; fix when touching the file | Low | Next edit of those files |
| TD-003 | 2026-11-17 | QA | Title-case sweep (L-030) is a manual Playwright routine, not a script in `tools/` | Time | Client-visible misses | Next page handover: script it into `tools/harness/` |
| TD-004 | 2026-11-14 | brand | #FF8F00 small text on ivory is about 2.2:1 (below AA) | Client's explicit choice (D-014) | Accessibility | If the client asks for an AA review |
| TD-005 | 2026-11-18 | cart | Share Your Cart waits on the external lpshopify API (about 0.9 s) | Not our service | Slow share | If Exigo/lpshopify changes |
| TD-006 | 2026-11-10 | perf | Exigo integration loads render-blocking jQuery 1.9.1 in a header custom-liquid block; inline `$` use prevents deferring it everywhere | Needs the Exigo developer | LCP | Launch performance pass |
| TD-007 | 2026-11-14 | templates | Product templates use 20 to 23 of 25 sections (many disabled legacy ones) | Merchant may still use them | A new section can push a template over the limit (L-001) | Before adding a PDP section |
| TD-008 | 2026-11-18 | multi-store | Every code change must be synced to uk/us/eu by hand (`sync_branch.py` per store) | Works; low frequency | Branch drift | If drift is found by audit |
| TD-009 | 2026-11-17 | apps | Idle or broken apps still installed (Intelligems, Koala, Instafeed, Tolstoy, Magefan) | Awaiting Letisha (`apps-001`) | Page weight, errors | Her decision |
| TD-010 | 2026-11-20 | integrations | EU Teqnavi Sync Engine default enroller is `CorpOrphan` while Teqnavi names `retaildirect` as the default | Their configuration | Wrong default credit on EU | Raise with Teqnavi |
