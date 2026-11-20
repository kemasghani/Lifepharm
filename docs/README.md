# LifePharm Docs: Map

The repository is the system of record. If a fact is not in here (or in CLAUDE.md), treat it as unknown and write it down once you learn it. This repo is **public**: no secrets, IPs, account ids, personal emails or customer data.

## Start of a session (5 minutes)

1. `./init.sh` and read its output (branch, sync state, active feature, guard result). Fix any FAIL first.
2. [progress.md](progress.md): the snapshot and the newest entry.
3. [feature_list.json](feature_list.json): pick **one** feature, set it to `in_progress`.
4. The knowledge page for the area you will touch (below), plus its section of [LESSONS.md](LESSONS.md).

## During the work

- A decision made or reversed → [DECISIONS.md](DECISIONS.md) (never delete the old one; add "supersedes").
- Something cost time → [LESSONS.md](LESSONS.md). Hit twice → turn it into a check in `tools/harness/check_theme.py`.
- Debt deferred → [tech-debt.md](tech-debt.md).
- Work spanning sessions or several areas → a plan in `exec-plans/active/` (objective, scope, verification, risks, progress log, open decisions); move it to `exec-plans/completed/` when done.
- A script used twice → `tools/` (never only in a scratchpad, L-045).

## End of a session (definition of done)

1. `./init.sh --full` passes; pushed; verified on the draft at 390px and 1440px (no horizontal scroll, no new JS errors); title-case sweep on changed pages.
2. [feature_list.json](feature_list.json): status plus evidence (commits, checks).
3. [progress.md](progress.md): new entry on top, snapshot updated.
4. Milestone? Add a line to [PROJECT_HISTORY.md](PROJECT_HISTORY.md). Area got better or worse? [QUALITY_SCORE.md](QUALITY_SCORE.md).
5. Commit with a descriptive message. The next session must be able to start with `./init.sh` alone.

## Map

| Need | Go to |
|---|---|
| Standing rules (brand, copy, motion, client taste, safety) | [../CLAUDE.md](../CLAUDE.md) |
| What happened so far, by phase | [PROJECT_HISTORY.md](PROJECT_HISTORY.md) |
| Why things are the way they are | [DECISIONS.md](DECISIONS.md) |
| Mistakes we will not repeat | [LESSONS.md](LESSONS.md) |
| Current state and next step | [progress.md](progress.md), [feature_list.json](feature_list.json) |
| Where quality is weak | [QUALITY_SCORE.md](QUALITY_SCORE.md), [tech-debt.md](tech-debt.md) |
| Deploy, preview, Files upload, QA tooling | [knowledge/theme-workflow.md](knowledge/theme-workflow.md) |
| Homepage, PDP, content pages, cart, referral | [knowledge/storefront.md](knowledge/storefront.md) |
| Image sources and rules | [knowledge/imagery-and-files.md](knowledge/imagery-and-files.md) |
| Exigo, apps, GA4, Clarity | [knowledge/integrations.md](knowledge/integrations.md) |
| Store branches and the sync routine | [knowledge/multi-store-ops.md](knowledge/multi-store-ops.md), [multi-store/ARCHITECTURE.md](multi-store/ARCHITECTURE.md) |
| News store | [knowledge/news-store.md](knowledge/news-store.md) |
| Projects outside this repo | [knowledge/off-repo-projects.md](knowledge/off-repo-projects.md) |
| Exigo API reference | [exigo-api/README.md](exigo-api/README.md) |
| Plans | [exec-plans/active/](exec-plans/active/), [exec-plans/completed/](exec-plans/completed/) |

## Tools

| Command | What |
|---|---|
| `./init.sh` | Context, harness state, theme guard (~3 s) |
| `./init.sh --full` | Plus the `shopify theme check` ratchet (~45 s). Run before every push |
| `python3 tools/harness/theme_check_ratchet.py --update` | Accept the current theme-check state after reviewing it |
| `tools/store-audit/*` | Store audit, Files sync, handle remap, branch sync, template port, Files upload/replace (see [knowledge/multi-store-ops.md](knowledge/multi-store-ops.md)) |

Harness model: [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) (instructions, state, verification, scope, lifecycle).
