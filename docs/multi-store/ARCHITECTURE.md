# LifePharm multi-store theme architecture

One repository, one codebase, four stores. This document says what is shared, what belongs to each store, how changes move, and how we prove a branch matches its store before it goes near a customer.

## 1. Stores and branches

| Branch | Store | Storefront | Currency | Live theme today | Role of the branch |
|---|---|---|---|---|---|
| `master` | none (UK draft "Lifepharm/master" until cutover) | n/a | n/a | n/a | Shared code. The only place Liquid, CSS, JS, locales and schema change. |
| `uk` | lifepharm-uk | uk.lifepharm.com | GBP | Impact 7.0.1 | UK store data on top of `master`. |
| `us` | lifepharm-usa | shop.lifepharm.com | USD | Impact 6.4.1 | US store data on top of `master`. |
| `eu` | lifepharm-EU | europe.lifepharm.com | EUR | Impact 6.4.1 | EU store data on top of `master`. |
| `news` | lifepharm-news | news.lifepharm.com | USD | Dawn 16.1.1 | Blog store. See section 7 before using it. |

Theme version: the repository is Impact 7.0.1, the newest version present in any of the four theme libraries (checked 2026-11-14). The Theme Store lists Impact 7.2.0 (2026-07-06). Moving to it starts with the owner adding 7.2.0 to one store's theme library; see section 6.

## 2. Principle: code is shared, data is per store

A Shopify theme mixes two different things in one folder tree.

| Kind | Paths | Owner | Changes on |
|---|---|---|---|
| Code | `layout/`, `sections/*.liquid`, `snippets/`, `blocks/`, `assets/`, `locales/`, `config/settings_schema.json` | The team | `master` only |
| Store data | `templates/**/*.json`, `sections/*-group.json`, `config/settings_data.json` | Each store | That store's branch only |
| Store admin | Files, products, collections, pages, blogs, menus, metafield definitions, installed apps | The merchant | Shopify admin, never in git |

Store data is a set of pointers into the store admin (`shopify://shop_images/hero.jpg`, a collection handle, a menu handle, an app block). A pointer that is valid in the UK admin is often wrong elsewhere: the US store calls the nutritionals collection `cell-regeneration`, and its footer menus are `company`, `shop-footer` and `support`. That is why data cannot be shared and why it has to be checked against the admin it points into.

## 3. Branch model

```
                 code only
   feature/* ───────────────▶ master ──┬── merge ──▶ uk   ⇄ UK theme (GitHub integration)
                                       ├── merge ──▶ us   ⇄ US theme
                                       ├── merge ──▶ eu   ⇄ EU theme
                                       └── merge ──▶ news ⇄ (decision pending)
```

- Code flows one way: `master` into the store branches. A store branch is never merged back into `master`.
- Store data stays put. `.gitattributes` marks the data paths `merge=ours`, so merging `master` into a store branch keeps that store's JSON whenever both sides changed it. Run `tools/store-audit/setup-git.sh` once per clone to enable the driver.
- The theme editor writes to the store branch. With the Shopify GitHub integration, edits a merchant makes in the editor are committed to the connected branch, which is exactly where store data belongs.
- A change that needs both code and data (a new section plus its content) lands as code on `master`, is merged into each store branch, then the content is added per store, by hand in the editor or by copying the JSON block and running the audit.

## 4. The audit: proof that a branch matches its store

`tools/store-audit/` reads the checkout, collects every pointer, and compares it with a read-only inventory of the store.

| Command | What it does |
|---|---|
| `python3 tools/store-audit/audit.py --store us` | Lists every reference in the checkout that the US admin does not have. Exit code 1 if an enabled section is affected. |
| `python3 tools/store-audit/sync_files.py --to us [--apply]` | Copies missing images and videos from the source store (UK) into the target store's Files, keeping filenames. Additive only. |
| `python3 tools/store-audit/remap.py --store us [--apply]` | Rewrites handles that differ per store, using the `remap` table in `stores.json`. |

What is checked: images, videos and other Files; products, collections, pages, blogs and menus by handle; app blocks and app embeds; product metafield definitions the Liquid reads.

What is not checked, and needs a person: copy that names a market ("Free UK delivery over £150"), prices typed into text, legal wording, and whether a product that exists is the right one to feature.

The app list cannot be read with the current API scopes, so "installed" means "already rendered by that store's live theme". Treat an app finding as a prompt to look, not as proof.

## 5. Workflows

### Ship a code change to every store
1. Branch from `master`, change code, open a pull request, merge.
2. For each store branch: `git merge master`, then `audit.py --store <store>`.
3. Push. The connected draft theme updates. Check it at 390px and 1440px.
4. Publishing stays a manual, per-store decision by the owner.

### Change one store's content
Edit in that store's theme editor, or edit the JSON on that store's branch. Run the audit. Nothing else moves.

### Bring a store onto the redesign for the first time
1. `sync_files.py --to <store> --apply` so the Files exist.
2. Fill the `remap` table for handles that differ, then `remap.py --store <store> --apply` on the store branch.
3. `audit.py --store <store>` until only known, accepted items remain.
4. Rewrite market copy (currency, delivery threshold, spelling) on the store branch.
5. Connect a new draft theme to the branch in that store's admin. Review. The owner publishes.

## 6. Guardrails

- Never publish from a script. Publishing is the owner's click, per store.
- `.env` holds the app credentials and store domains. It is git-ignored; the tools read it and never print it.
- The tools never delete or overwrite store data. `sync_files.py` only adds Files.
- JSON templates stay at 25 sections or fewer, or Shopify rejects the file without an error.
- Two pushes less than a minute apart can leave the first unsynced. Confirm with a theme file read before assuming a template was rejected.
- Recommended next step: run `audit.py` in CI on every pull request into a store branch, with the credentials as repository secrets.
- Theme upgrades (for example Impact 7.2.0): keep the untouched vendor release on a `vendor/impact` branch, merge it into `master`, resolve conflicts against our overrides in `assets/lp-premium.css` and the edited theme files, then merge `master` into the store branches as usual.

## 7. Open decisions

1. **News store.** It is a blog on Dawn with no products, one page and three menus. The `news` branch currently holds the commerce theme, and almost none of its references resolve there. Either keep News on Dawn in its own lineage, or decide the blog moves to the LifePharm theme and give it blog-only templates.
2. **UK cutover.** The UK draft still syncs from `master`. Connect a UK theme to `uk`, then stop syncing a store from `master`.
3. **Impact 7.2.0.** Needs the owner to add the release to a theme library first.
4. **Apps that differ per store.** See the audit output for app blocks a store's live theme does not use.
