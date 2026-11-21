#!/usr/bin/env python3
"""Give every Cellnergy product template the LAMININE buy box.

Order at the top of the `main` section:
    title, badges, rating row, summary + Ideal For, big price (with its hairline),
    IBO price (app, if present), variant cards (lp_card), then the rest as it was.
The theme price block, the separator and the Stamped star badge are disabled (the rating row and
lp_price replace them). The Clinicians' Choice badge moves under the buy buttons.

Run from a checkout root (master or a worktree):  python3 tools/normalize_cellnergy_buybox.py
"""
import json, os, re, sys

TEMPLATES = ['cellnergy-footcharge', 'one-time-purchase', 'cellnergy-power-cream', 'cellnergy-water-bottle',
             'cellnergy-diffuser-new', 'cellnergy-wellness-stand']
REF = 'templates/product.laminine.json'


def load(path):
    text = open(path).read()
    m = re.match(r'\s*/\*.*?\*/\s*', text, flags=re.S)
    header = m.group(0) if m else ''
    return header, json.loads(text[len(header):])


def main():
    _, ref = load(REF)
    ref_blocks = ref['sections']['main']['blocks']
    lp_defs = {k: ref_blocks[k] for k in ('lp_rating', 'lp_summary', 'lp_price')}

    for t in TEMPLATES:
        path = f'templates/product.{t}.json'
        if not os.path.exists(path):
            continue
        header, data = load(path)
        main_sec = data['sections']['main']
        blocks, order = main_sec['blocks'], main_sec['block_order']

        def find(pred):
            return [k for k in order if pred(k, blocks[k])]

        # Make sure the three LP blocks exist under their canonical ids; reuse an existing copy if it has another id.
        for key, snippet in (('lp_rating', 'lp-rating-row'), ('lp_summary', 'lp-pdp-summary'), ('lp_price', 'lp-pdp-price')):
            if key in blocks:
                blocks[key].pop('disabled', None)
                continue
            twins = find(lambda k, b: b['type'] == 'liquid' and snippet in b.get('settings', {}).get('liquid', ''))
            for tw in twins:
                blocks[tw]['disabled'] = True
            blocks[key] = json.loads(json.dumps(lp_defs[key]))
            order.append(key)

        for k in find(lambda k, b: b['type'] in ('price', 'separator') or 'star-rating-badge' in b['type']):
            blocks[k]['disabled'] = True

        vp = find(lambda k, b: b['type'] == 'variant_picker' and not b.get('disabled'))
        for k in vp:
            blocks[k].setdefault('settings', {})['selector_style'] = 'lp_card'

        head = find(lambda k, b: b['type'] == 'title')[:1] + find(lambda k, b: b['type'] == 'badges')[:1]
        head += ['lp_rating', 'lp_summary', 'lp_price']
        head += find(lambda k, b: 'ibo-price' in b['type'])
        head += vp[:1]
        clin = find(lambda k, b: b['type'] == 'liquid' and 'clinicianschoice' in b.get('settings', {}).get('liquid', ''))
        rest = [k for k in order if k not in head and k not in clin]
        bb = [i for i, k in enumerate(rest) if blocks[k]['type'] == 'buy_buttons']
        at = bb[0] + 1 if bb else len(rest)
        rest = rest[:at] + clin + rest[at:]
        main_sec['block_order'] = head + rest

        open(path, 'w').write(header + json.dumps(data, indent=2, ensure_ascii=False) + '\n')
        print(path, [blocks[k]['type'].split('/')[-2] if '/' in blocks[k]['type'] else k for k in head])


if __name__ == '__main__':
    sys.exit(main())
