# Integrations: Exigo, Apps, Analytics

Business rules and system boundaries verified on the stores. Access details (hosts, credentials, IPs) are deliberately not in this public repo.

## Exigo (MLM back office)

- API docs crawl: [../exigo-api/README.md](../exigo-api/README.md). Read it before writing any Exigo code; do not guess fields.
- Calls only work from a whitelisted static IP; the developer's home IP rotates (L-041).

### How orders reach Exigo

- A Shopify app titled **"Exigo"** (built by Teqnavi, their "Sync Engine") receives order webhooks about 10 s after creation.
  - Writes tag `SyncedExigo: <ExigoOrderID>` (or `Syncfailed`) and customer metafields `Exigo.CustomerId`, `Exigo.Webalias`, `Exigo.Referral` (US only), `Exigo.CustomerTypeId`, `Exigo.PointAccountId`.
  - Refunds become Exigo returns; cancellations without refund are not synced; fulfilment flows Exigo → Shopify hourly.
- Coverage since 2026-09-20: UK 100%; US and EU about 90%, with all misses in one October outage window. Teqnavi has not said what caused it; they describe a job every 2 hours that queues orders missing in Exigo, plus a health check and alert on failed syncs. Those orders were keyed into Exigo by hand as "Customer Service" orders.
- Idea, not built: alert on paid orders still missing `SyncedExigo` after about 15 minutes.

### Referral and commission (verified in Exigo, 228 orders)

- Enroller precedence in the connector: cart attribute `Referral`, then landing `?ref=`, then the store default.
- `referrer_webalias`, `referrer_name`, `ReferralSessionId` are display only.
- **Commission credit follows the customer's enroller.** The order's referral counts only when the Exigo customer is created; existing customers stay with their enroller even when the referral changed in checkout. Hence D-055 (L-042).
- Teqnavi's rule "move existing customers off the default enroller" did not fire on four real orders. Teqnavi explained why on 2026-11-25: the connector's configured default enroller is the CorporateShopifyRetail account, while those customers sit under the RetailDirect account, which it treats as a real enroller. Only the web alias `retaildirect` counts as "no referral" today; `CorpOrphan` (the Europe embed default) is not a web alias in Exigo, so it is read as a real referral, the `?ref=` fallback is skipped and the customer lands under CorporateShopifyRetail.
  - **Teqnavi's fix, live since 2026-11-25 (their message, relayed by Letisha; not yet checked with a test order):** new orders with a real referral link place the customer under that referrer instead of RetailDirect or CorporateShopifyRetail; customers with no referral still go to the default account; 65 past customers on Teqnavi's list were not touched and wait for LifePharm's decision. What was proposed: customers under RetailDirect or CorporateShopifyRetail count as unplaced; `retaildirect`, `CorpOrphan` and `CorporateShopifyRetail` count as "no referral" (case-insensitive), so `?ref=` still applies; a customer is never moved under themselves.
  - **Checked 2026-11-25 on the US draft, guest, after the banner block moved to the footer group (D-086):** Checkout on the cart page opens our dialog, Add My Referrer opens the app's search, a pick changes the cart attribute `Referral` from the default to the picked web alias and adds our `Referrer Name`, and both are still on the cart at checkout. No order was placed, so the Exigo side of the fix is still Teqnavi's word. The staging store cannot test this: its only buyable product is the enrolment kit, and with the kit in the cart pressing Checkout raised no submit event in the test (the app's enrolment handler is the likely reason; not confirmed).
  - **What it means for the referral dialog:** once the fix is live, an existing customer who is still unplaced is moved when their order carries a real referral. D-055 hides the dialog from every logged-in Exigo customer, which will then be too strict for unplaced ones. `Exigo.Referral` holds the customer's enroller web alias (Teqnavi), so the theme can tell an unplaced customer from a placed one. Do not change the theme until Teqnavi confirms the fix is deployed; then check with a test order that the move happens before the order is credited.
  - `Exigo.Referral` is written on all three stores; Europe and the UK only lack the metafield definition, so it shows under unstructured metafields.
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

### Who is an IBO (checked 2026-11-26, counts only)

- Customer metafield `Exigo.CustomerTypeId`, written by the Exigo connector: 3 is an IBO. Of the IBOs (type 3) with orders that were checked, it appears about 12 seconds after the first order for most (US 8 of 11, Europe 7 of 10); a few had it before the order.
- Customer tag `IBO`: on the US it matches type 3 (17 of 17 recent type 3 customers have it). On Europe and the UK it also sits on many type 2 customers. Shopify does not record who adds a customer tag, and no event shows it, so its source is not known.
- The theme uses the type (D-097), not the tag.
