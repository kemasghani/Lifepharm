#!/usr/bin/env python3
"""Repair U+FFFD replacement characters in theme templates (punctuation lost when live content was copied).
Rules are applied in order, from specific to generic, using the surrounding characters to recover the intent.
    python3 tools/qa/fix_mojibake.py <theme checkout> [--store us|eu|uk]   (writes in place, prints what is left)"""
import glob, re, sys
R = '�'
root = sys.argv[1]
store = sys.argv[sys.argv.index('--store') + 1] if '--store' in sys.argv else 'uk'
cur = {'us': '$', 'eu': '€', 'uk': '£'}[store]
rules = [
    (re.compile(f'Tritan{R} {R} '), 'Tritan™, '),
    (re.compile(f'd{R}colletage'), 'décolletage'),
    (re.compile(f'over {R}(\\d)'), f'over {cur}\\1'),
    (re.compile(f'(🙏+){R}'), '\\1 '),
    (re.compile(f'(\\d){R}([CF])\\b'), '\\1°\\2'),
    (re.compile(f'(\\d){R}(\\d)'), '\\1–\\2'),
    (re.compile(f'([A-Za-z]){R}([tsldvrm]\\b|re\\b|ve\\b|ll\\b)'), '\\1’\\2'),
    (re.compile(f' {R} '), ', '),
    (re.compile(f'(\\S){R}(<br)'), '\\1,\\2'),
    (re.compile(f'(\\S){R}(\\S)'), '\\1, \\2'),
]
for f in sorted(glob.glob(f'{root}/templates/*.json')):
    s = open(f, encoding='utf-8').read()
    if R not in s:
        continue
    n0 = s.count(R)
    for rx, rep in rules:
        s = rx.sub(rep, s)
    open(f, 'w', encoding='utf-8').write(s)
    left = [m.group(0) for m in re.finditer(f'.{{0,25}}{R}.{{0,25}}', s)]
    print(f'{f.split("/")[-1]}: fixed {n0 - len(left)}/{n0}', left[:3])
