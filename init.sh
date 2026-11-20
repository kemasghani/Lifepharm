#!/usr/bin/env bash
# LifePharm harness: standard startup + verification path.
#
#   ./init.sh          context + harness state + theme guard (~3 s)
#   ./init.sh --full   also runs the shopify theme-check ratchet (~45 s); use before every push
#
# Exit code is non-zero if any check FAILs. Fix the baseline before adding scope.
set -uo pipefail
cd "$(dirname "$0")"
FULL=0; [ "${1:-}" = "--full" ] && FULL=1
STATUS=0

echo "== Context"
echo "  repo:    $(pwd)"
echo "  branch:  $(git branch --show-current)  (master -> draft 189821452674; never the live theme)"
git fetch -q origin 2>/dev/null && echo "  vs origin: $(git rev-list --left-right --count origin/$(git branch --show-current)...HEAD 2>/dev/null | awk '{print "behind "$1", ahead "$2}')"
echo "  dirty:   $(git status --porcelain | grep -vc '^??') tracked, $(git status --porcelain | grep -c '^??') untracked"
echo "  last commits:"; git log --oneline -5 | sed 's/^/    /'

echo; echo "== Harness state"
if [ -f docs/feature_list.json ]; then
  python3 - <<'EOF'
import json
d = json.load(open("docs/feature_list.json"))
feats = d["features"]
by = {}
for f in feats: by.setdefault(f["status"], []).append(f)
print("  features: " + ", ".join(f"{k} {len(v)}" for k, v in sorted(by.items())))
for f in by.get("in_progress", []):
    print(f"  ACTIVE  {f['id']}  {f['title']}")
for f in by.get("blocked", [])[:5]:
    print(f"  blocked {f['id']}  {f['title']}  ({f.get('blocker','')})")
EOF
else
  echo "  WARN  docs/feature_list.json missing"
fi
[ -f docs/progress.md ] && echo "  progress.md last entry: $(grep -m1 -E '^## [0-9]{4}-' docs/progress.md | sed 's/^## //')"

echo
python3 tools/harness/check_theme.py || STATUS=1

if [ $FULL -eq 1 ]; then
  echo
  if command -v shopify >/dev/null; then
    python3 tools/harness/theme_check_ratchet.py || STATUS=1
  else
    echo "  WARN  shopify CLI not found, theme check skipped"
  fi
fi

echo
if [ $STATUS -eq 0 ]; then echo "== READY (fix WARNs when you touch those files)"; else echo "== NOT READY: fix FAILs first"; fi
[ $FULL -eq 0 ] && echo "   before pushing: ./init.sh --full, then verify the draft at 390px and 1440px"
exit $STATUS
