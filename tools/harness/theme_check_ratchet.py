#!/usr/bin/env python3
"""Ratchet over `shopify theme check`: existing errors are accepted, new ones fail.

The vendor theme ships ~1,050 MatchingTranslations errors (locale noise) plus a
handful of real ones. Instead of a wall of red, we store the accepted errors in
theme-check-baseline.json and fail only when a (check, file) pair gets worse.

Usage:
  python3 tools/harness/theme_check_ratchet.py            # compare
  python3 tools/harness/theme_check_ratchet.py --update   # accept current state (after a review)
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
BASELINE = os.path.join(HERE, "theme-check-baseline.json")
IGNORED_CHECKS = {"MatchingTranslations"}


def current() -> Counter:
    out = subprocess.run(
        ["shopify", "theme", "check", "--output", "json", "--path", ROOT],
        capture_output=True, text=True,
    ).stdout
    start = out.find("[")
    data = json.loads(out[start:]) if start >= 0 else []
    counts: Counter = Counter()
    for f in data:
        rel = os.path.relpath(f["path"], ROOT) if os.path.isabs(f["path"]) else f["path"]
        for o in f["offenses"]:
            if o["severity"] == "error" and o["check"] not in IGNORED_CHECKS:
                counts[f"{o['check']}|{rel}"] += 1
    return counts


def main() -> int:
    now = current()
    if "--update" in sys.argv:
        with open(BASELINE, "w") as fh:
            json.dump(dict(sorted(now.items())), fh, indent=2)
            fh.write("\n")
        print(f"theme check baseline updated: {sum(now.values())} accepted errors")
        return 0
    try:
        with open(BASELINE) as fh:
            base = Counter(json.load(fh))
    except FileNotFoundError:
        print("  WARN  no baseline yet, run with --update")
        return 0
    worse = {k: (base.get(k, 0), v) for k, v in now.items() if v > base.get(k, 0)}
    fixed = [k for k in base if now.get(k, 0) < base[k]]
    print(f"theme check: {sum(now.values())} errors (baseline {sum(base.values())}, MatchingTranslations ignored)")
    for k, (b, v) in sorted(worse.items()):
        print(f"  FAIL  new theme-check error {k}: {b} -> {v}")
    if fixed:
        print(f"  note  {len(fixed)} baseline entries improved; run --update to lock the gain")
    return 1 if worse else 0


if __name__ == "__main__":
    sys.exit(main())
