#!/usr/bin/env python3
"""Are the draft's apps the live theme's apps? Compares app embeds (config/settings_data.json) and enabled app blocks
(templates, section groups) of a store's live theme (read from the Admin API) with its branch, and can write the live ones into a checkout.

  python3 tools/store-audit/app_parity.py                                    # report for us, eu, uk
  python3 tools/store-audit/app_parity.py --store us --write <checkout dir>  # put live's embeds and app blocks into that checkout

Never touches a theme: it only reads live and writes files. Left out on purpose (REPLACED): what the redesign shows with its own sections,
and apps that are uninstalled (UNINSTALLED). Run it after every branch port (L-008, L-085)."""
import argparse, json, os, re, subprocess, sys, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shopify import REPO, gql

LIVE = {'uk': 188195209602, 'us': 190368612661, 'eu': 152722014425}
REPLACED = {'stamped-reviews/blocks/star-rating-badge': 'snippets/lp-rating-row', 'stamped-reviews/blocks/carousel': 'home review section',
            'instafeed/blocks/app-block': 'removed from the homepage design', 'teqnavi-lifepharm/blocks/referral-banner': 'moved to the footer group (D-086)'}
UNINSTALLED = {'triplewhale/blocks/triple_pixel_snippet'}
UPSELL = 'selleasy/blocks/lb-upsell'
Q = 'query($i:ID!,$c:String,$f:[String!]){theme(id:$i){files(first:50,after:$c,filenames:$f){pageInfo{hasNextPage endCursor} nodes{filename body{... on OnlineStoreThemeFileBodyText{content} ... on OnlineStoreThemeFileBodyUrl{url}}}}}}'


def live_files(store, patterns):
    out, cursor = {}, None
    while True:
        page = gql(store, Q, {'i': f'gid://shopify/OnlineStoreTheme/{LIVE[store]}', 'c': cursor, 'f': patterns})['data']['theme']['files']
        for node in page['nodes']:
            body = node['body'] or {}
            out[node['filename']] = body.get('content') or (urllib.request.urlopen(body['url']).read().decode() if body.get('url') else '')
        if not page['pageInfo']['hasNextPage']: return out
        cursor = page['pageInfo']['endCursor']


def split(text):
    head = re.match(r'^\s*/\*.*?\*/\s*', text, flags=re.S)
    return (head.group(0) if head else ''), json.loads(text[head.end():] if head else text)


def name(kind): return re.sub(r'/[0-9a-f-]{30,}$', '', kind.replace('shopify://apps/', ''))
def uuid(kind): return kind.rsplit('/', 1)[-1]
def is_app(kind): return kind.startswith('shopify://apps/')


def embeds(data):
    current = data['current']
    current = data['presets'][current] if isinstance(current, str) else current
    return current.setdefault('blocks', {})


def app_blocks(data):
    """(section id, block id, block) of every enabled app block in an enabled section."""
    for sid, section in (data.get('sections') or {}).items():
        if section.get('disabled') or sid not in data.get('order', [sid]): continue
        for bid in section.get('block_order', []):
            block = section['blocks'][bid]
            if is_app(block['type']) and not block.get('disabled'): yield sid, bid, block


def place(section, kind, live_order, live_types):
    """Index in the draft's block_order for a live app block."""
    order = section['block_order']; types = [section['blocks'][b]['type'] for b in order]; on = [not section['blocks'][b].get('disabled') for b in order]
    first = lambda *wanted: next((i for i, t in enumerate(types) if on[i] and t in wanted), None)
    n = name(kind)
    if n == 'teqnavi-lifepharm/blocks/ibo-price': i = first('variant_picker'); return i if i is not None else 1
    if n.startswith('afterpay'): i = first('payment_terms'); i = i if i is not None else first('buy_buttons'); return (i + 1) if i is not None else len(order)
    if n.startswith(('easyflow', 'easify')): i = first('buy_buttons'); return i if i is not None else len(order)
    if n.startswith(UPSELL) and section['type'] == 'main-cart': return 0 if live_types and live_types[0] == kind else len(order)
    return len(order)


def run(store, write):
    live = live_files(store, ['config/settings_data.json', 'templates/*.json', 'sections/*-group.json'])
    read = lambda f: subprocess.run(['git', '-C', str(REPO), 'show', f"origin/{'master' if store == 'uk' else store}:{f}"], capture_output=True, text=True).stdout
    gaps = 0
    head, draft = split(read('config/settings_data.json')); _, lv = split(live['config/settings_data.json'])
    want = {k: b for k, b in embeds(lv).items() if is_app(b['type']) and name(b['type']) not in UNINSTALLED}
    live_name = {uuid(b['type']) + name(b['type']).split('/')[-1]: name(b['type']) for b in want.values()}   # an app can change its handle (Pandectes was gdpr-cookie-consent)
    have = {live_name.get(uuid(b['type']) + name(b['type']).split('/')[-1], name(b['type'])): b for b in embeds(draft).values() if is_app(b['type'])}
    state = lambda b: 'none' if b is None else 'off' if b.get('disabled') else 'on'
    for n in sorted({name(b['type']) for b in want.values()} | set(have)):
        l = next((b for b in want.values() if name(b['type']) == n), None); d = have.get(n)
        if {state(l), state(d)} - {'off', 'none'} and (state(l) != state(d) or (l or {}).get('settings') != (d or {}).get('settings')):
            gaps += 1; print(f'  {store} embed {n}: live {state(l)}, draft {state(d)}' + (' (settings differ)' if state(l) == state(d) else ''))
    if write:
        blocks = embeds(draft); keep = {k: b for k, b in blocks.items() if not is_app(b['type'])}
        blocks.clear(); blocks.update(keep); blocks.update(want)
        open(os.path.join(write, 'config/settings_data.json'), 'w', encoding='utf-8').write(head + json.dumps(draft, indent=2, ensure_ascii=False).replace('/', '\\/' if '\\/' in read('config/settings_data.json') else '/') + '\n')
    for f, text in sorted(live.items()):
        if not f.startswith('templates/'): continue
        src = read(f)
        if not src: continue
        try: head, d = split(src); _, l = split(text)
        except ValueError: continue
        changed = False
        for sid, bid, block in list(app_blocks(l)):
            n = name(block['type'])
            if n in REPLACED or n in UNINSTALLED: continue
            same = [b for _, _, b in app_blocks(d) if uuid(b['type']) == uuid(block['type']) and name(b['type']).split('/')[-1] == n.split('/')[-1]]
            if any(b['type'] == block['type'] for b in same): continue
            if same:
                print(f"  {store} {f}: {name(same[0]['type'])} is {n} on live"); gaps += 1
                for b in same: b['type'] = block['type']
                changed = True; continue
            kind = l['sections'][sid]['type']
            target = next((s for k, s in d['sections'].items() if s['type'] == kind and not s.get('disabled') and k in d['order']), None)
            print(f'  {store} {f}: {n} missing ({kind})' + ('' if target and kind != 'apps' else ', no section for it: skipped')); gaps += 1
            if not target or kind == 'apps': continue
            ltypes = [l['sections'][sid]['blocks'][b]['type'] for b in l['sections'][sid]['block_order'] if not l['sections'][sid]['blocks'][b].get('disabled')]
            off = next((k for k, b in target['blocks'].items() if b['type'] == block['type'] and b.get('disabled')), None)
            if off: target['blocks'][off].pop('disabled'); target['blocks'][off]['settings'] = block.get('settings', {}); changed = True; continue
            target['block_order'].insert(place(target, block['type'], None, ltypes), bid); target['blocks'][bid] = block; changed = True
        if changed and write:
            compact = '\n' not in src[len(head):].strip()[:400]
            out = json.dumps(d, ensure_ascii=False, separators=(',', ':')) if compact else json.dumps(d, indent=2, ensure_ascii=False)
            if '\\/' in src: out = out.replace('/', '\\/')
            open(os.path.join(write, f), 'w', encoding='utf-8').write(head + out + ('' if compact else '\n'))
    print(f'{store}: {gaps} differences'); return gaps


a = argparse.ArgumentParser(); a.add_argument('--store', choices=list(LIVE)); a.add_argument('--write'); o = a.parse_args()
sys.exit(1 if sum(run(s, o.write) for s in ([o.store] if o.store else LIVE)) else 0)
