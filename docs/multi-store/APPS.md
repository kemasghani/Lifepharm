# Apps per store

The full comparison and the removal proposal are in `LifePharm-Shopify-Apps-Audit-2026-11-16.pdf` (same folder). This page keeps the facts a developer needs when working on a store branch.

## Removed (2026-11-18)

- **Replo** (US) and **Triple Whale** were uninstalled by the developer on 2026-11-18, after Letisha approved both removals. The pre-checks showed nothing on any storefront depended on either.

## Share Your Cart (2026-11-18)

The Exigo shared-cart feature now lives in `snippets/lp-share-cart.liquid` (rendered from `layout/theme.liquid`). The old custom-liquid block in `sections/footer-group.json`, with its Font Awesome stylesheet, was removed on every branch. The API is `lpshopify.azurewebsites.net` (Azure South Central US). The snippet relies on the Exigo app embed's globals: `apiUrl`, `shopUrl`, `customerId`, `isCustomer`, `referralCookieName`, `getCookie` and `logCart`.

## Correction (2026-11-16)

The first version of this page counted app block handles, and two apps appear in the themes under more than one handle because their vendors renamed them:

- **Tolstoy** is one app. `tolstoy`, `tolstoy-ads-image-video`, `tolstoy-shoppable-video-quiz` and `tolstoy-shoppable-video-ugc` share one extension id.
- **Pandectes GDPR** is one app. `gdpr-cookie-consent` is its old handle.

So the UK store is not missing Tolstoy, and the US store does not run a different cookie banner. `tools/store-audit/audit.py` now matches apps on the extension id as well as the handle. The empty reviews carousel on the UK home page is therefore not explained by a missing app; its cause is still open.

## How status is established

1. App embeds and app blocks in each store's live theme (on, or switched off).
2. Scripts and theme app extensions the live storefront actually loads (home page, a product page, the cart).
3. Data that apps leave in the store admin (shop metafield namespaces).

The API scopes we hold cannot list installed apps, so apps that only work in the admin or the checkout may be missing, and a data trace can outlive an uninstalled app. Confirm in Settings > Apps before removing anything.

## What the redesign branches need

The theme JSON on the store branches references these apps. With renamed handles counted once:

| App | UK | US | EU | News |
|---|:-:|:-:|:-:|:-:|
| Design Packs | yes | yes | yes | no |
| Gorgias | yes | yes | yes | no |
| Instafeed | yes | yes | yes | no |
| Koala Free Gift | yes | **no** | yes | no |
| Pandectes GDPR | yes | yes | yes | no |
| Recharge Subscriptions | off | off | off | no |
| Stamped Reviews | yes | yes | yes | no |
| Teqnavi LifePharm | yes | yes | yes | no |
| Tolstoy | yes | yes | yes | no |
| Weglot | yes | yes | yes | yes |

To do on the branches:

- [ ] **US**: Koala Free Gift is not on the US store. Remove its embed from the `us` branch, or install it.
- [ ] **All**: Recharge is still referenced (an app embed and one disabled block) but loads nothing on any storefront; Skio runs subscriptions. Remove the reference once the owner confirms Recharge is retired.
- [ ] **News**: blog store, only Weglot in use. See the open decision in `ARCHITECTURE.md`.

## Apps active on the storefront but absent from the theme JSON

These load through script tags or pixels, so they never show up in a theme audit: Skio, FrontrowMD, NoFraud (UK), Magefan Customer Assistance, Cartbot (UK), Microsoft Clarity and Intelligems (US), plus the custom Exigo script on all three commerce stores. The `9gtb.com` loader on UK, US and EU is **Gorgias Convert** (identified 2026-11-17): the Gorgias app block loads `content.9gtb.com/loader.js` with `data-gorgias-loader-convert`, and the file defines `ConvertRootLoader` and `GorgiasBridge`. UK also has an older Convert script tag (`media.9gtb.com/loader.js?g_cvt_id=26fad685-...`), the same file loaded twice. Whether any Convert campaign is live can only be seen in Gorgias > Convert.
