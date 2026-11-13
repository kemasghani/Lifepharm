# store-audit

Checks that a theme checkout only points at things that exist in a store's Shopify admin. Background and branch rules: `docs/multi-store/ARCHITECTURE.md`.

Needs Python 3.9+ and the repo's `.env` (app client id and secret, plus the four store domains). No packages to install.

```
python3 tools/store-audit/audit.py --store all            # current checkout against every store
python3 tools/store-audit/audit.py --store us --refresh   # one store, fresh inventory
python3 tools/store-audit/sync_files.py --to us           # dry run: Files to copy from UK
python3 tools/store-audit/sync_files.py --to us --apply
python3 tools/store-audit/remap.py --store us             # dry run: handles to rewrite
python3 tools/store-audit/remap.py --store us --apply
```

Every command takes `--root <path>` to audit another checkout, such as a git worktree of a store branch.

| File | Purpose |
|---|---|
| `stores.json` | Store registry: branch, env key for the domain, and the per-store `remap` table. No secrets. |
| `shopify.py` | Admin API client (client-credentials token, retries, pagination). |
| `refs.py` | Finds every reference in the theme JSON, using each section's schema to read handle settings. |
| `inventory.py` | Read-only inventory of a store. |
| `audit.py` | Compares the two and reports. Exit code 1 when an enabled section is affected. |
| `sync_files.py` | Copies missing Files between stores. Additive only. |
| `remap.py` | Applies the `remap` table to the data files. |
| `setup-git.sh` | Enables the `merge=ours` driver used by `.gitattributes`. Run once per clone. |

`.cache/` (30 minute inventory cache) and `reports/` are git-ignored.
