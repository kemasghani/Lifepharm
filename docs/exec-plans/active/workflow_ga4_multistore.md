# Workflow: 4 Shopify stores → 1 GA4 property (clean data)

Strategy: systematic · Depth: deep · Executor: Claude in Chrome (owner's logged-in session)
Created: 2026-11-11 · Last updated: 2026-11-11 (News store added, Store split exploration built)

**Status: all 4 production stores live and verified. `purchase` not yet observed (no orders since setup).**

## 0. Facts (audited)

### GA4
| Item | Value |
|---|---|
| Account / property | 167823404 / 395660189 "LifePharm - GA4" |
| Web stream | 5794376250, `G-C4WLTGDWTT` (one stream for every store) |
| Reporting currency / time zone | USD / America/Los_Angeles |
| Do NOT use | `G-3K4TGS1VQV` (261662153 "Landing Pages"). The Google & YouTube app selects it by default: always switch to G-C4WLTGDWTT |

### Stores (Shopify org "LifePharm Inc.", 5 stores)
| Store | Shopify handle | Domain | Currency | In GA4 | Other pixels |
|---|---|---|---|---|---|
| US ("LifePharm Inc") | lifepharm-usa | `shop.lifepharm.com` | USD | ✅ Active | Elevar custom pixel 109838645 disconnected (was dead, config 404) |
| UK | lifepharm-uk | `uk.lifepharm.com` | GBP | ✅ Active | none (GA-wise) |
| EU | lifepharm-eu | `europe.lifepharm.com` | EUR | ✅ Active | none (GA-wise) |
| News | lifepharm-news | `news.lifepharm.com` | USD | ✅ Active | Elevar app installed but **not connected** (no events) |
| Staging | lifepharm-staging | n/a | n/a | ❌ **Excluded on purpose** | Test traffic must never reach production GA4 |

News is a content/blog storefront (Beauty, Business, Health, Nutrition, Recipes, Science), 0 products. Expect page_view/engagement only, no ecommerce events.

## 1. Architecture decision

**One property, one web stream, one tag source per store.**
- All stores are subdomains of `lifepharm.com`, so the `_ga` cookie is shared: one visitor = one user across US/UK/EU/News (verified: same `cid` on all 4).
- Split by store with the built-in **Hostname** dimension (Exploration "Store split", see D6).
- Separate streams/properties per store were rejected: double-counted users, fragmented reporting.
- Tagging only via the **Shopify Google & YouTube app** (sandboxed Web Pixel, consent-aware). Never add theme `gtag`, GTM or a second GA4 custom pixel.

## 2. Configuration (done)

### A. GA4 property hygiene
| # | Setting | Value |
|---|---|---|
| A1 | Currency / time zone | USD / America/Los_Angeles (unchanged, do not change) |
| A3 | Data retention | Event data **14 months** |
| A5 | Enhanced measurement | Page views only (sandboxed pixel cannot read DOM; other auto-events would be noise) |
| A6 | Configure your domains | contains `lifepharm.com` (covers all 4 subdomains, incl. News) |
| A7 | Unwanted referrals | laminine.com, klaviyo.com, paypal.com, lifepharm.com, myshopify.com, shopify.com, shop.app, klarna.com, clearpay.co.uk, stripe.com, afterpay.com, cardinalcommerce.com, 3dsecure, adyen.com, arcot.com |
| A12 | Reporting identity | **Device-based** (changed from Blended on 2026-11-12 via Admin API, to avoid Google Signals thresholding on low-traffic stores; reversible) |
| A8 | Internal traffic filter | **Not set** (needs office/agency IPs from owner) |
| A9 | Developer traffic filter | Active (default) |
| A11 | Key events | `purchase` only |
| — | Redact data | Email redaction ON |

### B. Store connection (per store)
Procedure used for every store:
1. Settings > Customer events: confirm no other GA4/GTM/gtag pixel.
2. Install **Google & YouTube** → Connect Google account (owner completes Google sign-in/passkey).
3. Carousel card 2/2 "Looking only to set up Google Analytics 4" → Get started (no Merchant Center).
4. Property dropdown: switch from G-3K4TGS1VQV to **G-C4WLTGDWTT (395660189)** → Connect.
5. Marketing emails: leave unchecked → Confirm → Complete setup. Status must read **Active**.
6. Verify one `g/collect?...tid=G-C4WLTGDWTT` per page on the storefront.

| Store | Date | Result |
|---|---|---|
| US | 2026-11-11 | Active, hits verified |
| UK | 2026-11-11 | Active, hits + ecommerce verified |
| EU | 2026-11-11 | Active, hits verified |
| News | 2026-11-11 | Active, hit verified on `/collections/all` (tid G-C4WLTGDWTT, gcs=G111, same cid as other stores) |

### C. Consent
- UK + EU: Pandectes GDPR → Shopify `setTrackingConsent` → Consent Mode signals (`gcs`/`gcd`) reach the pixel.
- EU Pandectes shows a pending permission re-authorisation (owner to approve).
- US / News: no blocking banner required.

## 3. Validation

| # | Check | Status |
|---|---|---|
| D1 | Realtime hits from all hostnames | ✅ shop./uk./europe. in Realtime; news. verified by network hit |
| D2 | Exactly one `g/collect` per page_view | ✅ all 4 stores |
| D3 | Ecom events carry currency + value | ✅ view_item_list, view_item, add_to_cart (cu=GBP, value), view_cart, remove_from_cart, begin_checkout |
| D4 | Exactly one `purchase` per order, `transaction_id` present | ⏳ awaiting first real order per store |
| D5 | No `lifepharm.com` / payment domains in Session source (after 48h) | ⏳ check 2026-11-13 |
| D7 | GA4 vs Shopify sessions (2026-11-10 15:00–21:59 PT, via GA4 Data API + ShopifyQL) | US 67 vs 63 (106%) ✅ · EU 21 vs 38 (55%, gap = burst of US-desktop "direct" sessions on the EU store, bot-like, GA4 filters these) · UK 7 vs 16 (44%, UK opt-in consent) · News 1 vs 1. Purchases: 2 US web orders (#3966US, #3967US at 21:27/21:33 PT) fell in a GA4 hour that was only partly processed, recheck 2026-11-12. Skio renewals (`subscription_contract_checkout_one`) are server-side and never reach GA4 by design |
| D6 | Reporting by store | ✅ Exploration **"Store split - US, UK, EU, News (by Hostname)"**, tab "Funnel by store": Hostname × Total users, Sessions, Views, Add to carts, Checkouts, Ecommerce purchases, Purchase revenue (last 28 days) |

## 4. Open items (owner)
1. Approve Pandectes permission re-authorisation on EU.
2. First real order per store: confirm one `purchase` in Realtime, and Shop Pay (`shop.app`) checkout events.
3. Optional: send office/agency IPs → internal traffic rule (Testing 7 days → Active).
4. Never connect **LifePharm Staging** to G-C4WLTGDWTT. If staging needs analytics, use a separate test property.

## 5. Monitoring
- 2026-11-13: D5 attribution check (Session source / medium in the Store split exploration).
- 2026-11-25 (week 2): referral audit, extend A7 if payment/3DS hosts appear.
- Monthly: Shopify orders vs GA4 purchases per store (expect 80 to 95% match given consent).

## 6. Change log
| Date | Change |
|---|---|
| 2026-11-11 | Retention 2 → 14 months; unwanted referrals; email redaction; key event purchase only |
| 2026-11-11 | US, UK, EU connected via Google & YouTube (GA4-only) |
| 2026-11-11 | US Elevar custom pixel 109838645 disconnected on owner request (dead, config 404; reconnectable) |
| 2026-11-11 | News store connected (owner request); Staging deliberately excluded |
| 2026-11-11 | Exploration "Store split - US, UK, EU, News (by Hostname)" created |
