"""Run Lighthouse (mobile, the same settings PageSpeed Insights uses) on this machine several times and print each
run and the median. One run means little: the score moves by several points between runs, so compare medians.

Usage: python3 tools/perf/lh_run.py URL [--runs 5] [--desktop] [--out DIR] [--label before] [--trace-over MS]
       Needs node (npx) and Chrome. A draft theme is measured with URL?preview_theme_id=<id>.
       --trace-over 1500 keeps the full trace of every run whose observed first paint is later than 1500 ms
       (used by .github/workflows/lighthouse-lab.yml to catch the late first paint of TD-039 on a datacentre machine).
       LP_CHROME sets the Chrome binary, LP_CHROME_FLAGS replaces the default flags.
       This machine is faster and closer to the store than Google's lab, so scores here run higher than PageSpeed's;
       use them to compare before and after, not as the number a client will see."""
import glob, json, os, shutil, statistics, subprocess, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lhr import numbers, summary

ARGS = sys.argv[1:]
def opt(name, default=None):
    return ARGS[ARGS.index(name) + 1] if name in ARGS else default
URL = next((a for a in ARGS if a.startswith('http')), None)
RUNS = int(opt('--runs', 5)); LABEL = opt('--label', 'run')
OUT = opt('--out', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reports'))
CHROME = os.environ.get('LP_CHROME') or next((c for c in ('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', shutil.which('google-chrome') or '', shutil.which('chromium') or '') if c and os.path.exists(c)), '')
FLAGS = os.environ.get('LP_CHROME_FLAGS', '--headless=new --no-first-run')
TRACE_OVER = int(opt('--trace-over', 0))
if not URL:
    sys.exit(__doc__)
os.makedirs(OUT, exist_ok=True)
rows = []
for i in range(RUNS):
    path = os.path.join(OUT, f"lh-{LABEL}-{time.strftime('%Y%m%d-%H%M%S')}.json")
    cmd = ['npx', '-y', 'lighthouse@13', URL, '--quiet', '--output=json', f'--output-path={path}', '--only-categories=performance',
           f'--chrome-flags={FLAGS}', '--max-wait-for-load=60000'] + (['--preset=desktop'] if '--desktop' in ARGS else []) + (['--save-assets'] if TRACE_OVER else [])
    done = subprocess.run(cmd, capture_output=True, text=True, env={**os.environ, 'CHROME_PATH': CHROME})
    if done.returncode or not os.path.exists(path):
        print(f'run {i + 1}: failed  {done.stderr.strip()[-200:]}'); continue
    lh = json.load(open(path)); n = numbers(lh); rows.append(n)
    print(f'run {i + 1}: ' + ' · '.join(f'{k} {v}' for k, v in n.items()))
    if TRACE_OVER:
        assets = [a for a in glob.glob(path[:-5] + '*') if a != path]
        if n['seen FCP'] > TRACE_OVER: print(f'   late first paint: kept {[os.path.basename(a) for a in assets]}')
        else: [os.remove(a) for a in assets]
    if i == RUNS - 1: print(summary(lh))
    time.sleep(8)
if rows:
    print(f'MEDIAN of {len(rows)} ({LABEL}): ' + ' · '.join(f'{k} {statistics.median(r[k] for r in rows):g}' for k in rows[0]))
