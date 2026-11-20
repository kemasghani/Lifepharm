# Integrations: Exigo, Apps, Analytics

Business rules and system boundaries verified on the stores. Access details (hosts, credentials, IPs) are deliberately not in this public repo.

## Exigo (MLM back office)

- API docs crawl: [../exigo-api/README.md](../exigo-api/README.md). Read it before writing any Exigo code; do not guess fields.
- Calls only work from a whitelisted static IP; the developer's home IP rotates (L-041).

### How orders reach Exigo

- A Shopify app titled **"Exigo"** (built by Teqnavi, their "Sync Engine") receives order webhooks about 10 s after creation.
  - Writes tag `SyncedExigo: <ExigoOrderID>` (or `Syncfailed`) and customer metafields `Exigo.CustomerId`, `Exigo.Webalias`, `Exigo.Referral` (US only), `Exigo.CustomerTypeId`, `Exigo.PointAccountId`.
  - Refunds become Exigo returns; cancellations without refund are not synced; fulfilment flows Exigo → Shopify hourly.
- Coverage since 2026-09-20: UK 100%; US and EU about 90%, with all misses in one October outage window. Those orders were keyed into Exigo by hand as "Customer Service" orders.
- Idea, not built: alert on paid orders still missing `SyncedExigo` after about 15 minutes.

### Referral and commission (verified in Exigo, 228 orders)

- Enroller precedence in the connector: cart attribute `Referral`, then landing `?ref=`, then the store default.
- `referrer_webalias`, `referrer_name`, `ReferralSessionId` are display only.
- **Commission credit follows the customer's enroller.** The order's referral counts only when the Exigo customer is created; existing customers stay with their enroller even when the referral changed in checkout. Hence D-055 (L-042).
- Teqnavi's stated rule "move existing customers off the default enroller" is contradicted by four real orders.
- US and EU live themes run the Teqnavi Sync Engine and Enrollment Handler embeds; the UK live theme has neither and writes only `Referral`. Keep these embeds on every branch sync (L-008).

### Storefront middleware

- `lpshopify` (external ASP.NET host, not ours) serves `exigoscript.js`, loaded from a custom-liquid block in `sections/header-group.json` (`Exigo.Settings`: cookie `refId`, param `ref`, default webalias). It does not intercept checkout. Endpoints include enroller search, customer sync, shared cart.
- Do not call lpshopify from new code; read order attributes, tags and metafields instead.
- Never call `DequeueCustomerEvents` while exploring (L-044).

## Apps (runtime-checked 2026-11-17)

- Full audit: [../multi-store/APPS.md](../multi-store/APPS.md) and the PDFs in `docs/multi-store/`.
- Subscriptions: **Skio** on UK/US/EU (Recharge referenced but loads nothing). Skio renewals never fire a GA4 purchase (no browser).
- Reviews: Stamped. Translations: Weglot (JS integration). Chat: Gorgias (`9gtb.com` = Gorgias Convert loader, idle). Consent: Pandectes (keep its Clarity integration off).
- Black Friday automatic discounts: Regios Discounts.
- Idle or broken: Intelligems, Koala, Cartbot, Instafeed, Tolstoy (empty on home/PDP/cart), Magefan (500). Replo and Triple Whale uninstalled 2026-11-18.
- Detect apps from three sources together: live theme JSON, storefront network requests, order/line custom attributes (`_lb-product` Selleasy, `_chub` C-Hub, `igId` Intelligems).

## Analytics

- **GA4:** one property for US, UK, EU and News via the Google & YouTube app (D-060). Split stores with the Hostname dimension. Never add gtag/GTM to the theme. Compare GA4 purchases only with `web` orders. Plan and open items: [../exec-plans/active/workflow_ga4_multistore.md](../exec-plans/active/workflow_ga4_multistore.md).
- **Clarity:** one project per store, all linked to GA4, installed through the Clarity Shopify app (D-061). The app sends Shopify Customer Privacy consent.
- Search Console domain property verified; sitemaps for all four storefronts submitted.
