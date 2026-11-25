#!/usr/bin/env python3
"""Settings the live theme holds that the draft lost: for every template and section group both themes have, compare each
section and block (same id) and list setting keys that live has with a value and the draft does not. Typical cause: the live
theme had a customised section schema (an extra setting), so the copy in the redesign dropped the value. Read-only.

  python3 tools/store-audit/lost_settings.py [us eu uk]"""
import json, os, re, sys, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shopify import gql
TH = {'uk': (188195209602, 189821452674), 'us': (190368612661, 193373995317), 'eu': (152722014425, 168919728345)}
Q = 'query($i:ID!,$c:String){theme(id:$i){files(first:50,after:$c,filenames:["templates/*.json","sections/*-group.json"]){pageInfo{hasNextPage endCursor} nodes{filename body{... on OnlineStoreThemeFileBodyText{content} ... on OnlineStoreThemeFileBodyUrl{url}}}}}}'


def files(store, theme):
    out, cursor = {}, None
    while True:
        page = gql(store, Q, {'i': f'gid://shopify/OnlineStoreTheme/{theme}', 'c': cursor})['data']['theme']['files']
        for n in page['nodes']:
            b = n['body'] or {}
            out[n['filename']] = b.get('content') or (urllib.request.urlopen(b['url']).read().decode() if b.get('url') else '')
        if not page['pageInfo']['hasNextPage']: return out
        cursor = page['pageInfo']['endCursor']


def load(text):
    try: return json.loads(re.sub(r'^\s*/\*.*?\*/', '', text, flags=re.S))
    except ValueError: return None


def empty(v): return v in (None, '', [], {}, '<p></p>')


found = 0
for store in [a for a in sys.argv[1:] if a in TH] or list(TH):
    live, draft = (files(store, t) for t in TH[store])
    for name in sorted(set(live) & set(draft)):
        L, D = load(live[name]), load(draft[name])
        if not L or not D: continue
        for sid, ls in (L.get('sections') or {}).items():
            ds = (D.get('sections') or {}).get(sid)
            if not ds or ls.get('type') != ds.get('type') or ls.get('disabled'): continue
            pairs = [('', ls.get('settings') or {}, ds.get('settings') or {})]
            pairs += [(bid, b.get('settings') or {}, ((ds.get('blocks') or {}).get(bid) or {}).get('settings') or {})
                      for bid, b in (ls.get('blocks') or {}).items() if not b.get('disabled') and bid in (ds.get('blocks') or {})]
            for bid, lset, dset in pairs:
                for key, value in lset.items():
                    if not empty(value) and key not in dset:
                        found += 1
                        print(f'{store} {name} {ls["type"]} {sid}{"/" + bid if bid else ""} {key}: {str(value)[:90]!r}')
print(f'{found} lost settings'); sys.exit(1 if found else 0)
