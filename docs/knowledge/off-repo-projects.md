# Related Work Outside This Repo

Pointers only, so a session in this repo knows these exist. Their own docs are the source of truth.

| Project | Where | Status | Notes |
|---|---|---|---|
| Exigo → Klaviyo service (lpsync) | Private repo `LifePharm/lifepharm-marketing`, folder `exigo-klaviyo-integration/` | In progress (`int-002`); Klaviyo flows are drafts only | Replaces the HubSpot IBO workflows (V5 doc is the reference spec, HubSpot is not running). Has its own harness there: `exigo-klaviyo-integration/CLAUDE.md`, `init.sh`, `docs/` (progress, decisions, lessons, history, original plan). Start there for any lpsync work. Never set flows live without LifePharm sign-off. |
| Checkout extensions (referral block, trust block) | `~/Documents/lifepharm-checkout-referral` | Built, not deployed (`ref-002`, `chk-001`) | Two checkout UI extensions for the "Developer Lifepharm" app: "Referred by" and "Order with confidence" (design record in its `docs/trust-block.md`) |
| HyperFrames films | `~/Documents/Lifepharm-*-film`, `~/Documents/Lifepharm-freedelivery-icon` | Done | Source for the play-once MP4s in `assets/` |
| Exigo API docs crawler | `docs/exigo-api/tools/` (in this repo) | Done | Refresh: see CLAUDE.md section 6 |

Private operational facts (credentials, hosts, IPs, account ids) live in the developer's private notes, never here (L-046).
