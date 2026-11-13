# Apps per store

Checked 2026-11-14 with `tools/store-audit`. "Present" means the store's **live theme** renders the app (an app embed or an app block). The API scopes we hold cannot list installed apps, so an app with no theme footprint (back-office or pixel-only apps) does not show here, and "not present" can also mean "installed but unused by the live theme". Confirm in each admin under Settings > Apps before installing anything.

Store branches: `uk`, `us`, `eu`, `news`. Live themes: UK Impact 7.0.1, US Impact 6.4.1, EU Impact 6.4.1, News Dawn 16.1.1.

## 1. Apps the redesign needs

These 13 apps are referenced by the theme JSON on the store branches. A store needs each one installed, or the reference removed from that store's branch.

| App | How the redesign uses it | UK | US | EU | News |
|---|---|:-:|:-:|:-:|:-:|
| Design Packs (`design-packs`) | embed on | yes | yes | yes | **no** |
| Gorgias (live chat) (`gorgias-live-chat-helpdesk`) | embed on | yes | yes | yes | **no** |
| Instafeed (`instafeed`) | embed on | yes | yes | yes | **no** |
| Koala Free Gift (`koala-free-gift`) | embed on | yes | **no** | yes | **no** |
| Pandectes GDPR (cookie banner) (`pandectes-gdpr-compliance`) | embed on | yes | **no** | yes | **no** |
| Recharge Subscriptions (`recharge-subscriptions`) | embed on, 0 of 1 blocks on | yes | yes | yes | **no** |
| Stamped Reviews (`stamped-reviews`) | 8 of 18 blocks on | yes | yes | yes | **no** |
| Teqnavi LifePharm (referral) (`teqnavi-lifepharm`) | 1 of 1 blocks on | yes | yes | yes | **no** |
| Tolstoy (video) (`tolstoy`) | 5 of 9 blocks on | **no** | yes | yes | **no** |
| Tolstoy Ads: Image & Video (`tolstoy-ads-image-video`) | 2 of 6 blocks on | yes | **no** | yes | **no** |
| Tolstoy Shoppable Video & Quiz (`tolstoy-shoppable-video-quiz`) | 2 of 3 blocks on | yes | yes | yes | **no** |
| Tolstoy Shoppable Video & UGC (`tolstoy-shoppable-video-ugc`) | embed on | yes | yes | yes | **no** |
| Weglot (translation) (`weglot-translate-your-store`) | embed on | yes | yes | yes | yes |
| **Present** | | **12 / 13** | **10 / 13** | **13 / 13** | **1 / 13** |

### To do per store

- [ ] **UK**: missing Tolstoy (video) (`tolstoy`).
- [ ] **US**: missing Koala Free Gift (`koala-free-gift`), Pandectes GDPR (cookie banner) (`pandectes-gdpr-compliance`), Tolstoy Ads: Image & Video (`tolstoy-ads-image-video`).
- [x] **EU**: nothing missing.
- [ ] **NEWS**: missing Design Packs (`design-packs`), Gorgias (live chat) (`gorgias-live-chat-helpdesk`), Instafeed (`instafeed`), Koala Free Gift (`koala-free-gift`), Pandectes GDPR (cookie banner) (`pandectes-gdpr-compliance`), Recharge Subscriptions (`recharge-subscriptions`), Stamped Reviews (`stamped-reviews`), Teqnavi LifePharm (referral) (`teqnavi-lifepharm`), Tolstoy (video) (`tolstoy`), Tolstoy Ads: Image & Video (`tolstoy-ads-image-video`), Tolstoy Shoppable Video & Quiz (`tolstoy-shoppable-video-quiz`), Tolstoy Shoppable Video & UGC (`tolstoy-shoppable-video-ugc`).

Notes:
- UK: the home page reviews carousel uses the `tolstoy` app block, which the UK live theme does not use. That is why the carousel renders empty on the UK draft. Use the `tolstoy-shoppable-video-ugc` block UK already has, or install the app.
- US: the cookie banner there is `gdpr-cookie-consent`, not Pandectes. Swap the embed on the `us` branch rather than installing a second banner.
- News: a blog store. Only Weglot is in use; see the open decision in `ARCHITECTURE.md`.

## 2. Apps only some stores use

Not referenced by the redesign. If a store still wants one, its embed or block has to be added on that store's branch, or it disappears when the store moves to the new theme.

| App | UK | US | EU | News |
|---|:-:|:-:|:-:|:-:|
| Affirm (pay over time messaging) (`affirm-pay-over-time-messaging`) | - | 0 of 1 blocks on | - | - |
| Afterpay (on-site messaging) (`afterpay-on-site-messaging`) | - | 12 of 14 blocks on | - | - |
| Back in Stock: Restock Alerts (`back-in-stock-restock-alerts`) | - | - | embed on | - |
| C-Hub Customer Accounts (`c-hub-customer-accounts`) | - | embed on | embed on | - |
| Easify Product Options (`easify-options`) | - | embed on, 1 of 3 blocks on | - | - |
| Easyflow Product Options (`easyflow`) | - | embed off, 5 of 8 blocks on | - | - |
| GDPR Cookie Consent (`gdpr-cookie-consent`) | - | embed on | - | - |
| Intelligems (A/B testing) (`intelligems-a-b-testing`) | - | embed on | - | - |
| Klaviyo (`klaviyo-email-marketing-sms`) | - | embed on | embed on | - |
| Microsoft Clarity (`microsoft-clarity`) | - | embed on | - | - |
| NoFraud (`nofraud-fraud-protection`) | - | embed on | embed on | - |
| Powerful Form Builder (`powerful-form-builder`) | - | embed on, 1 of 1 blocks on | - | - |
| Selleasy (upsell) (`selleasy`) | - | embed on, 7 of 12 blocks on | embed on, 6 of 11 blocks on | - |
| Stamped Loyalty & Referrals (`stamped-loyalty-referrals`) | - | embed off, 4 of 5 blocks on | embed on, 4 of 5 blocks on | - |
| Toki Loyalty (`toki-loyalty`) | - | embed off, 1 of 1 blocks on | - | - |
| Triple Whale (`triplewhale`) | - | embed on | - | - |
| UpPromote Affiliate (`uppromote-affiliate`) | - | embed on | - | - |

### Carry-over checklist

- [ ] **US**: decide whether Affirm (pay over time messaging) stays (0 of 1 blocks on).
- [ ] **US**: decide whether Afterpay (on-site messaging) stays (12 of 14 blocks on).
- [ ] **US**: decide whether C-Hub Customer Accounts stays (embed on).
- [ ] **US**: decide whether Easify Product Options stays (embed on, 1 of 3 blocks on).
- [ ] **US**: decide whether Easyflow Product Options stays (embed off, 5 of 8 blocks on).
- [ ] **US**: decide whether GDPR Cookie Consent stays (embed on).
- [ ] **US**: decide whether Intelligems (A/B testing) stays (embed on).
- [ ] **US**: decide whether Klaviyo stays (embed on).
- [ ] **US**: decide whether Microsoft Clarity stays (embed on).
- [ ] **US**: decide whether NoFraud stays (embed on).
- [ ] **US**: decide whether Powerful Form Builder stays (embed on, 1 of 1 blocks on).
- [ ] **US**: decide whether Selleasy (upsell) stays (embed on, 7 of 12 blocks on).
- [ ] **US**: decide whether Stamped Loyalty & Referrals stays (embed off, 4 of 5 blocks on).
- [ ] **US**: decide whether Toki Loyalty stays (embed off, 1 of 1 blocks on).
- [ ] **US**: decide whether Triple Whale stays (embed on).
- [ ] **US**: decide whether UpPromote Affiliate stays (embed on).
- [ ] **EU**: decide whether Back in Stock: Restock Alerts stays (embed on).
- [ ] **EU**: decide whether C-Hub Customer Accounts stays (embed on).
- [ ] **EU**: decide whether Klaviyo stays (embed on).
- [ ] **EU**: decide whether NoFraud stays (embed on).
- [ ] **EU**: decide whether Selleasy (upsell) stays (embed on, 6 of 11 blocks on).
- [ ] **EU**: decide whether Stamped Loyalty & Referrals stays (embed on, 4 of 5 blocks on).
