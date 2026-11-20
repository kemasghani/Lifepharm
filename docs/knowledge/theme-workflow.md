# Theme Workflow: Deploy, Preview, Verify

## Deploy path

- Push to `master` → Shopify GitHub integration → draft theme **"Lifepharm/master" (189821452674)** on the UK store. Sync takes 1 to 10 minutes.
- Store branches `uk`, `us`, `eu`, `news` connect to their own unpublished themes (IDs in [multi-store-ops.md](multi-store-ops.md)).
- The live themes are never touched without the owner's approval in chat.

## Preview

- UK: `https://uk.lifepharm.com/?preview_theme_id=189821452674`
- curl needs a cookie jar and `-L` (L-006): `curl -sL -c /tmp/j -b /tmp/j "<url>" | grep -c "<marker>"`.
- To prove one section renders: `?section_id=<section-file-name>`.

## When a change does not show up

1. Did the push land? Two pushes within a minute can skip the second (L-005).
2. Read the draft's real file: Admin API `theme(id: "gid://shopify/OnlineStoreTheme/<id>") { files(filenames: ["templates/x.json"]) { nodes { body { ... on OnlineStoreThemeFileBodyText { content } } } } }`.
3. If assets synced but a JSON template did not, Shopify rejected it silently. Run `./init.sh`: the guard reports over-25 sections and out-of-range values (L-001, L-002). Otherwise bisect the change across templates in one sync.

## Admin API access

- `tools/store-audit/shopify.py` exchanges the app client id/secret in `.env` for a client-credentials token on any of the four stores (`gql(store, query, vars)`). It never prints secrets. Read-only unless the task needs a write.
- Never `source .env` (L-040).
- Orders are visible for 60 days only (`read_all_orders` missing, L-043).

## Shopify Files (images, videos)

- Edited images are uploaded to the store's **Files** and referenced as `shopify://shop_images/<filename>`.
- New files: `STORE=uk python3 tools/store-audit/files_upload.py a.jpg b.jpg` (skips existing names).
- Replace in place, same filename: `python3 tools/store-audit/replace_file.py uk path/to/file.jpg` (L-053).
- Copy missing Files to another store: `python3 tools/store-audit/sync_files.py --to us [--apply]`.
- Naming: `lp-<area>-<subject>.jpg` (`lp-cat-*`, `lp-hover-<product-handle>.jpg`, `lp-home-step-*`, `lp-benefit-*.png`, `lp-history-*.png`).
- Files are store admin data shared by every theme, including the live one: upload finished images only.

## QA tools

- Playwright (`uv run --no-project --with playwright`), `channel="chrome"`, `wait_until="load"` (L-031). Viewports 390x844 and 1440x900.
- Keep storefront automation light: Cloudflare challenges after heavy runs (L-032).
- Browser automation preference: `jev-browse` first, claude-in-chrome as fallback (it only has permission for uk.lifepharm.com and cannot act on admin.shopify.com).
- Known third-party console noise: Stamped `e is not a function`; `/collections/all` `addEventListener` null (also on live) (L-033).

## HyperFrames (motion assets)

Source projects live outside this repo: `~/Documents/Lifepharm-pdp-film`, `~/Documents/Lifepharm-referral-film`, `~/Documents/Lifepharm-freedelivery-icon`, `~/Documents/Lifepharm-brand-film`. Render to small MP4 plus a poster JPG (final frame), play once.
