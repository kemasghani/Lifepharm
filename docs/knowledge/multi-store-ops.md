# Multi-Store Operations

The design spec is [../multi-store/ARCHITECTURE.md](../multi-store/ARCHITECTURE.md). This page is the operational state and the routine.

## Current state (2026-11-20)

| Branch | Store | Connected theme | Notes |
|---|---|---|---|
| `master` | UK | "Lifepharm/master" 189821452674 (draft) | Shared code; still the UK draft until cutover (`ms-002`) |
| `uk` | UK | none yet | Identical to master |
| `us` | US | "Lifepharm/us" 193373995317 (draft) | Header menu `main-menu-redesign`; own `koala-free-gift` embed; Teqnavi embeds |
| `eu` | EU | "Lifepharm/eu" 168919728345 (draft) | Teqnavi embeds |
| `news` | News | "Lifepharm/news" 190930518311 (draft) | Dawn redesign, see [news-store.md](news-store.md) |
| `news-dawn` | News | none | History only |
| `staging` | Staging (staging.lifepharm.com) | "Lifepharm/staging (redesign draft)" 193151959352 (unpublished, API upload) | Starts from `us`; Files copied from the US; not connected to GitHub yet (TD-032) |

Worktrees: `~/Documents/Lifepharm-worktrees/<branch>`. Run `tools/store-audit/setup-git.sh` once per clone (enables the `merge=ours` driver).

## Routine after any code change on master

1. `./init.sh --full`, push `master`, verify the UK draft.
2. For each of `uk`, `us`, `eu` (worktree clean):
   `python3 tools/store-audit/sync_branch.py <store>` (keeps the store's app embeds, localises market copy),
   then `python3 tools/store-audit/remap.py --store <store> --apply`,
   then `python3 tools/store-audit/audit.py --store <store> --root ~/Documents/Lifepharm-worktrees/<store>`.
3. If Files are missing on the target store: `sync_files.py --to <store> --include-disabled --apply`.
4. Commit and push the store branch; check its draft.

Code-only change: skip the full sync and check out just the changed files from master on each store branch (L-058). Working from a clone outside iCloud: `sync_branch.py <store> --root <worktree>` (L-059).

## Store differences to remember

- US collections `cell-regeneration` / `skin-regeneration` (UK/EU `nutritionals` / `skin-health`); US footer menus `company`, `shop-footer`, `support`. The remap table in `tools/store-audit/stores.json` handles these.
- Store-only theme settings (kept by `sync_branch.py`, list `STORE_SETTINGS`): `lp_hsa_*`, the HSA/FSA payment note. US: only the listed products; UK and EU: hidden.
- Market copy: US "Free shipping on orders over $150", EU "Free delivery on orders over €150", UK "Free UK delivery over £150". The buy-box delivery tile is not typed: it is built from the store currency and the free delivery threshold (L-068).
- Live-only templates were ported with `port_templates.py` (US 47, EU 40). Re-run it if the merchant adds templates on live (L-007).
- All three stores lack the `product.custom.badges` metafield definition.
- US `/pages/privacy-policy` is empty on live too; policies live at `/policies/`.
- Live themes: UK Impact 7.0.1, US and EU Impact 6.4.1, News Dawn 16.1.1.
