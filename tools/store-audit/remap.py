#!/usr/bin/env python3
"""Rewrite references that are valid on the source store but carry a different handle on this store (see `remap` in stores.json).

  python3 tools/store-audit/remap.py --store us            # dry run
  python3 tools/store-audit/remap.py --store us --apply    # edit the JSON on the current checkout

Run it on the store's own branch. It only touches the data files (templates, section groups, settings_data).
"""
import argparse, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shopify import CONFIG, REPO, STORE_KEYS
from refs import data_files

URI_SEGMENT = {"collection": "collections", "page": "pages", "product": "products", "blog": "blogs"}


def patterns(kind, old, new):
    """Every spelling a handle takes in theme JSON: a shopify:// URI, a storefront path, or a bare handle setting."""
    found = []
    if kind in URI_SEGMENT:
        segment = URI_SEGMENT[kind]
        found.append((re.compile(rf"(shopify:\\?/\\?/{segment}\\?/){re.escape(old)}(?=[\"\\/?#])"), rf"\g<1>{new}"))
        found.append((re.compile(rf"((?:\"|\\\"|')\\?/{segment}\\?/){re.escape(old)}(?=[\"'\\/?#])"), rf"\g<1>{new}"))
        found.append((re.compile(rf"(\"(?:{kind}|[a-z_]*_{kind})\":\s*\"){re.escape(old)}(\")"), rf"\g<1>{new}\g<2>"))
    if kind == "menu":
        found.append((re.compile(rf"(\"[a-z_]*menu\":\s*\"){re.escape(old)}(\")"), rf"\g<1>{new}\g<2>"))
    return found


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--store", required=True, choices=STORE_KEYS)
    parser.add_argument("--root", default=str(REPO))
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    rules = [(kind, old, new, patterns(kind, old, new)) for kind, table in CONFIG["stores"][args.store].get("remap", {}).items() for old, new in table.items()]
    total = 0
    for path in data_files(args.root):
        text = original = open(path).read()
        for kind, old, new, compiled in rules:
            for pattern, replacement in compiled:
                text, count = pattern.subn(replacement, text)
                if count:
                    total += count
                    print(f"  {os.path.relpath(path, args.root)}: {kind} {old} -> {new} (x{count})")
        if args.apply and text != original:
            open(path, "w").write(text)
    print(f"{total} reference(s) {'rewritten' if args.apply else 'would be rewritten'} for {args.store}")


if __name__ == "__main__":
    main()
