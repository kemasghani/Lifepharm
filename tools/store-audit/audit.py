#!/usr/bin/env python3
"""Check that a theme checkout only references things that exist in a store's admin.

  python3 tools/store-audit/audit.py --store us            # audit the current checkout against the US store
  python3 tools/store-audit/audit.py --store all           # the same checkout against every store
  python3 tools/store-audit/audit.py --store eu --refresh  # ignore the cached inventory

Read-only. Exits 1 when an enabled section references something the store does not have.
"""
import argparse, json, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shopify import HERE, REPO, STORE_KEYS
from refs import collect
from inventory import inventory

KINDS = ["image", "video", "file", "product", "collection", "page", "blog", "menu", "app", "metafield"]
CACHE = HERE / ".cache"
REPORTS = HERE / "reports"


def store_inventory(store, refresh, max_age=1800):
    CACHE.mkdir(exist_ok=True)
    path = CACHE / f"{store}.json"
    if not refresh and path.exists() and time.time() - path.stat().st_mtime < max_age:
        return json.loads(path.read_text())
    data = inventory(store)
    path.write_text(json.dumps(data))
    return data


def compare(refs, inv):
    report = {}
    for kind in KINDS:
        have = set(inv.get(kind, []))
        have_lower = {h.lower() for h in have}
        missing = {v: w for v, w in refs.get(kind, {}).items() if v not in have and v.lower() not in have_lower}
        active = {v: w for v, w in missing.items() if any("(disabled)" not in x for x in w)}
        report[kind] = {"referenced": len(refs.get(kind, {})), "missing": missing, "missing_active": sorted(active)}
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--store", default="all", choices=STORE_KEYS + ["all"])
    parser.add_argument("--root", default=str(REPO), help="theme checkout to audit (default: this repo)")
    parser.add_argument("--refresh", action="store_true", help="re-read the store instead of using the 30 minute cache")
    parser.add_argument("--quiet", action="store_true", help="summary table only")
    args = parser.parse_args()
    stores = STORE_KEYS if args.store == "all" else [args.store]
    refs = collect(args.root)
    REPORTS.mkdir(exist_ok=True)
    reports = {}
    for store in stores:
        inv = store_inventory(store, args.refresh)
        reports[store] = compare(refs, inv)
        (REPORTS / f"{store}.json").write_text(json.dumps({"root": args.root, "report": reports[store], "errors": inv.get("errors", {})}, indent=1))
    print(f"{'kind':<11}{'refs':>5}  " + "  ".join(f"{s:^16}" for s in stores))
    for kind in KINDS:
        cells = []
        for store in stores:
            r = reports[store][kind]
            cells.append(f"{'ok':^16}" if not r["missing"] else f"{len(r['missing_active']):>3} live {len(r['missing']) - len(r['missing_active']):>3} off  ")
        print(f"{kind:<11}{reports[stores[0]][kind]['referenced']:>5}  " + "  ".join(cells))
    failed = False
    for store in stores:
        active = {k: reports[store][k]["missing_active"] for k in KINDS if reports[store][k]["missing_active"]}
        failed = failed or bool(active)
        if args.quiet or not any(reports[store][k]["missing"] for k in KINDS):
            continue
        print(f"\n{store}: missing in the store admin")
        for kind in KINDS:
            for value, where in sorted(reports[store][kind]["missing"].items()):
                off = "" if value in reports[store][kind]["missing_active"] else "  (only in disabled sections)"
                print(f"  {kind:<10} {value}{off}\n             {where[0]}" + (f"  (+{len(where) - 1} more)" if len(where) > 1 else ""))
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
