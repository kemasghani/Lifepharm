"""Make a store branch's theme identical to master (code + data), keep that store's own app embeds,
and localise market copy. Then run remap.py --store <store> --apply and audit.py.
Usage: python3 tools/store-audit/sync_branch.py <us|eu|uk> [--root <worktree>]  (default worktree ~/Documents/Lifepharm-worktrees/<store>, must be clean;
pass --root when working from a clone outside iCloud, see L-055)"""
import json, os, re, subprocess, sys
store = sys.argv[1]
wt = os.path.abspath(sys.argv[sys.argv.index('--root') + 1]) if '--root' in sys.argv else os.path.expanduser(f'~/Documents/Lifepharm-worktrees/{store}')
run = lambda *a: subprocess.run(a, cwd=wt, check=True, capture_output=True, text=True).stdout
assert run('git', 'status', '--porcelain').strip() == '', 'worktree not clean'
_b = run('git', 'show', 'HEAD:config/settings_data.json'); before = json.loads(_b[_b.index('{'):])
run('git', 'checkout', 'master', '--', '.')

# 1. app embeds: keep this store's embeds (its own app config), add master's embeds for app blocks the store lacks
p = os.path.join(wt, 'config/settings_data.json'); _raw = open(p).read(); prefix = _raw[:_raw.index('{')]; data = json.loads(_raw[len(prefix):])
mine = before.get('current', {}).get('blocks', {}) or {}
theirs = data['current'].get('blocks', {}) or {}
mine_types = {b.get('type') for b in mine.values()}
merged = dict(mine)
for k, b in theirs.items():
    if b.get('type') not in mine_types and k not in merged:
        merged[k] = b
data['current']['blocks'] = merged
# 1b. theme settings that are a store's own choice, not shared design: keep the store's value (or absence)
STORE_SETTINGS = ('lp_hsa_',)  # HSA/FSA payment note: US only
for k in [k for k in data['current'] if k.startswith(STORE_SETTINGS)]: del data['current'][k]
kept = {k: v for k, v in before.get('current', {}).items() if k.startswith(STORE_SETTINGS)}
data['current'].update(kept)
print(f'store settings kept: {sorted(kept) or "none"}')
open(p, 'w').write(prefix + json.dumps(data, indent=2, ensure_ascii=False) + '\n')
print(f'embeds: kept {len(mine)} {store} embeds, added {len(merged) - len(mine)} from master')

# 2. market copy on the data files
COPY = {
    'us': [('Free UK delivery on orders over £150', 'Free shipping on orders over $150'), ('free shipping on orders over £150', 'free shipping on orders over $150'), ('£150', '$150')],
    'eu': [('Free UK delivery on orders over £150', 'Free delivery on orders over €150'), ('free shipping on orders over £150', 'free delivery on orders over €150'), ('£150', '€150')],
}.get(store, [])
changed = 0
for root, _, files in os.walk(wt):
    rel = os.path.relpath(root, wt)
    if not (rel.startswith('templates') or rel == 'sections' or rel == 'config'): continue
    for f in files:
        if not f.endswith('.json') or (rel == 'sections' and not f.endswith('-group.json')): continue
        fp = os.path.join(root, f); s = open(fp).read(); o = s
        for a, b in COPY: s = s.replace(a, b)
        if s != o: open(fp, 'w').write(s); changed += 1
print('market copy files changed:', changed)
left = run('git', 'grep', '-n', '-I', '-e', '£', '-e', 'UK delivery', '--', 'templates', 'sections/*-group.json', 'config/settings_data.json') if store != 'uk' else ''
print('remaining £/UK mentions:\n' + '\n'.join(l[:160] for l in left.splitlines()[:20]) if left else 'none')
