"""Run Lighthouse (mobile, the same settings PageSpeed Insights uses) on this machine several times and print each
run and the median. One run means little: the score moves by several points between runs, so compare medians.

Usage: python3 tools/perf/lh_run.py URL [--runs 5] [--desktop] [--out DIR] [--label before]
       Needs node (npx) and Chrome. A draft theme is measured with URL?preview_theme_id=<id>.
       This machine is faster and closer to the store than Google's lab, so scores here run higher than PageSpeed's;
       use them to compare before and after, not as the number a client will see."""
import json, os, statistics, subprocess, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lhr import numbers, summary

ARGS = sys.argv[1:]
def opt(name, default=None):
    return ARGS[ARGS.index(name) + 1] if name in ARGS else default
URL = next((a for a in ARGS if a.startswith('http')), None)
RUNS = int(opt('--runs', 5)); LABEL = opt('--label', 'run')
OUT = opt('--out', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reports'))
CHROME = os.environ.get('LP_CHROME', '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
if not URL:
    sys.exit(__doc__)
os.makedirs(OUT, exist_ok=True)
rows = []
for i in range(RUNS):
    path = os.path.join(OUT, f"lh-{LABEL}-{time.strftime('%Y%m%d-%H%M%S')}.json")
    cmd = ['npx', '-y', 'lighthouse@13', URL, '--quiet', '--output=json', f'--output-path={path}', '--only-categories=performance',
           '--chrome-flags=--headless=new --no-first-run', '--max-wait-for-load=60000'] + (['--preset=desktop'] if '--desktop' in ARGS else [])
    done = subprocess.run(cmd, capture_output=True, text=True, env={**os.environ, 'CHROME_PATH': CHROME})
    if done.returncode or not os.path.exists(path):
        print(f'run {i + 1}: failed  {done.stderr.strip()[-200:]}'); continue
    lh = json.load(open(path)); n = numbers(lh); rows.append(n)
    print(f'run {i + 1}: ' + ' · '.join(f'{k} {v}' for k, v in n.items()))
    if i == RUNS - 1: print(summary(lh))
    time.sleep(8)
if rows:
    print(f'MEDIAN of {len(rows)} ({LABEL}): ' + ' · '.join(f'{k} {statistics.median(r[k] for r in rows):g}' for k in rows[0]))
