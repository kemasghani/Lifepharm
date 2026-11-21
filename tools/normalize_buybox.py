#!/usr/bin/env python3
"""Give every product template the same compact buy box.

Order at the top of the `main` section:
    title, badges, rating row, summary + Ideal For, IBO price (app, if present), variant picker, then the rest.
The price lives inside the Add to Cart button (snippets/buy-buttons.liquid), so the theme price block, the
lp_price row, the separator, the quantity stepper and the Stamped star badge are disabled. Cellnergy templates use variant cards
(lp_card). The Clinicians' Choice badge moves under the buy buttons.

Run from a checkout root (master or a worktree):  python3 tools/normalize_buybox.py
"""
import json, os, re, sys

import glob
CARDS = ['cellnergy-footcharge', 'one-time-purchase', 'cellnergy-power-cream', 'cellnergy-water-bottle',
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
    lp_defs = {k: ref_blocks[k] for k in ('lp_rating', 'lp_summary')}

    for path in sorted(glob.glob('templates/product*.json')):
        t = path[len('templates/product.'):-len('.json')] if path != 'templates/product.json' else ''
        header, data = load(path)
        main_sec = data['sections'].get('main')
        if not main_sec or main_sec.get('type') != 'main-product':
            continue
        blocks, order = main_sec['blocks'], main_sec['block_order']

        def find(pred):
            return [k for k in order if pred(k, blocks[k])]

        # Make sure the three LP blocks exist under their canonical ids; reuse an existing copy if it has another id.
        for key, snippet in (('lp_rating', 'lp-rating-row'), ('lp_summary', 'lp-pdp-summary')):
            if key in blocks:
                blocks[key].pop('disabled', None)
                continue
            twins = find(lambda k, b: b['type'] == 'liquid' and snippet in b.get('settings', {}).get('liquid', ''))
            for tw in twins:
                blocks[tw]['disabled'] = True
            blocks[key] = json.loads(json.dumps(lp_defs[key]))
            order.append(key)

        for k in find(lambda k, b: b['type'] in ('price', 'separator') or 'star-rating-badge' in b['type']
                      or (b['type'] == 'liquid' and 'lp-pdp-price' in b.get('settings', {}).get('liquid', ''))):
            blocks[k]['disabled'] = True

        vp = find(lambda k, b: b['type'] == 'variant_picker' and not b.get('disabled'))
        if t in CARDS:
            for k in vp:
                blocks[k].setdefault('settings', {})['selector_style'] = 'lp_card'

        title = find(lambda k, b: b['type'] == 'title')[:1]
        prefix = order[:order.index(title[0])] if title else []
        head = prefix + title + find(lambda k, b: b['type'] == 'badges')[:1]
        head += ['lp_rating', 'lp_summary']
        head += find(lambda k, b: 'ibo-price' in b['type'])
        head += vp[:1]
        clin = find(lambda k, b: b['type'] == 'liquid' and 'clinicianschoice' in b.get('settings', {}).get('liquid', ''))
        rest = [k for k in order if k not in head and k not in clin]
        bb = [i for i, k in enumerate(rest) if blocks[k]['type'] == 'buy_buttons']
        at = bb[0] + 1 if bb else len(rest)
        rest = rest[:at] + clin + rest[at:]
        # Installment messaging follows the button that now carries the price.
        pay = [k for k in rest if blocks[k]['type'] == 'payment_terms' or 'payments-messaging' in blocks[k]['type']]
        rest = [k for k in rest if k not in pay]
        bb = [i for i, k in enumerate(rest) if blocks[k]['type'] == 'buy_buttons']
        at = bb[0] + 1 if bb else len(rest)
        rest = rest[:at] + pay + rest[at:]
        # Skio: plans stacked (side by side breaks around the frequency list), legend for screen readers only.
        for k in rest:
            if 'skio' in blocks[k]['type']:
                st = blocks[k].setdefault('settings', {})
                st.update({'show_legend': False, 'layout': 'vertical'})
                if '<ul>' in st.get('additional_subscription_content', ''):
                    st['additional_subscription_content'] = '<p>Save [discount], skip or cancel any time</p>'
        # No quantity stepper on product pages: quantity is changed in the cart.
        for k in rest:
            if blocks[k]['type'] == 'quantity_selector':
                blocks[k]['disabled'] = True
        main_sec.setdefault('settings', {})['show_fixed_add_to_cart'] = True  # sticky Add to Cart on every PDP
        main_sec['block_order'] = head + rest

        open(path, 'w').write(header + json.dumps(data, indent=2, ensure_ascii=False) + '\n')
        print(path, [blocks[k]['type'].split('/')[-2] if '/' in blocks[k]['type'] else k for k in head if not blocks[k].get('disabled')])


if __name__ == '__main__':
    sys.exit(main())
