"""Copy templates that exist on a store's LIVE theme but not in a branch checkout, plus the sections/snippets/blocks/assets
they need that the checkout lacks. Never overwrites an existing file. Read-only on the live theme.
Usage: port_templates.py <store> <live_theme_id> <worktree> [--apply]"""
import sys, os, re, json, base64, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shopify import gql
store, tid, root = sys.argv[1], sys.argv[2], sys.argv[3]
apply = '--apply' in sys.argv
GID = f'gid://shopify/OnlineStoreTheme/{tid}'

def list_files(pattern):
    out, after = [], None
    while True:
        d = gql(store, 'query($id:ID!,$a:String,$f:[String!]){theme(id:$id){files(first:250,after:$a,filenames:$f){nodes{filename} pageInfo{hasNextPage endCursor}}}}', {'id': GID, 'a': after, 'f': [pattern]})['data']['theme']['files']
        out += [n['filename'] for n in d['nodes']]
        if not d['pageInfo']['hasNextPage']: return out
        after = d['pageInfo']['endCursor']

def fetch(names):
    res = {}
    for i in range(0, len(names), 20):
        d = gql(store, '''query($id:ID!,$f:[String!]){theme(id:$id){files(first:50,filenames:$f){nodes{filename body{
            ... on OnlineStoreThemeFileBodyText{content} ... on OnlineStoreThemeFileBodyBase64{contentBase64} ... on OnlineStoreThemeFileBodyUrl{url}}}}}}''', {'id': GID, 'f': names[i:i+20]})['data']['theme']['files']['nodes']
        for n in d:
            b = n['body']
            if 'content' in b: res[n['filename']] = b['content'].encode()
            elif 'contentBase64' in b: res[n['filename']] = base64.b64decode(b['contentBase64'])
            elif 'url' in b: res[n['filename']] = urllib.request.urlopen(b['url'], timeout=60).read()
    return res

exists = lambda f: os.path.exists(os.path.join(root, f))
live_templates = list_files('templates/*')
todo = [f for f in live_templates if not exists(f) and not f.startswith('templates/customers/')]
live_all = set(list_files('sections/*') + list_files('snippets/*') + list_files('blocks/*') + list_files('assets/*'))
print(f'{store}: {len(todo)} templates missing in {root}')

got, queue, seen = {}, list(todo), set()
while queue:
    batch = [f for f in queue if f not in seen]; queue = []
    seen.update(batch)
    files = fetch(batch); got.update(files)
    for name, data in files.items():
        text = data.decode('utf-8', 'ignore')
        deps = set()
        if name.endswith('.json'):
            body = text[text.find('{'):]
            try: j = json.loads(body)
            except Exception: j = {}
            def walk(o):
                if isinstance(o, dict):
                    t = o.get('type')
                    if isinstance(t, str) and not t.startswith(('shopify://', '@')):
                        deps.add(f'sections/{t}.liquid'); deps.add(f'blocks/{t}.liquid')
                    for v in o.values(): walk(v)
                elif isinstance(o, list):
                    for v in o: walk(v)
            walk(j.get('sections', {}))
            if 'wrapper' in j: pass
        else:
            for m in re.findall(r"{%-?\s*(?:render|include)\s+['\"]([^'\"]+)['\"]", text): deps.add(f'snippets/{m}.liquid')
            for m in re.findall(r"{%-?\s*section\s+['\"]([^'\"]+)['\"]", text): deps.add(f'sections/{m}.liquid')
            for m in re.findall(r"['\"]([\w.\-]+\.(?:css|js|png|jpg|jpeg|svg|gif|webp|woff2?|json))['\"]\s*\|\s*asset_(?:url|img_url)", text): deps.add(f'assets/{m}')
            for m in re.findall(r"{%-?\s*content_for\s+['\"]block['\"],\s*type:\s*['\"]([^'\"]+)['\"]", text): deps.add(f'blocks/{m}.liquid')
        for dep in deps:
            if dep in live_all and not exists(dep) and dep not in seen: queue.append(dep)

kinds = {}
for f in got: kinds.setdefault(f.split('/')[0], []).append(f)
for k, v in sorted(kinds.items()): print(f'  {k}: {len(v)}  ', ', '.join(sorted(os.path.basename(x) for x in v))[:600])
if apply:
    for f, data in got.items():
        p = os.path.join(root, f); os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, 'wb').write(data)
    print('written', len(got))
