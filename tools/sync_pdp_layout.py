#!/usr/bin/env python3
"""Keep the lower half of every non-Cellnergy product template identical to the standard one.

Each target keeps its own `main` section (buy box blocks, app blocks) and takes every other section, with
their order, from its source template. Sections whose metafields are empty render nothing, so packs show the
buy box, reviews and FAQ. Fee and flow templates (minimal, signup-fee, instalment journey) are left alone.

Run from a checkout root:  python3 tools/sync_pdp_layout.py
"""
import json, os, re

TARGETS = {  # target suffix -> source suffix ('' is templates/product.json)
    'ibo-pack': '', 'ibo-one-time-purchase': '', 'one-time-purchase-pack': '', 'refive': '', 'immune-ibo': '',
    'lamiderm-apex-ibo': 'lamiderm-apex',
}


def path(suffix):
    return f'templates/product.{suffix}.json' if suffix else 'templates/product.json'


def load(p):
    text = open(p).read()
    m = re.match(r'\s*/\*.*?\*/\s*', text, flags=re.S)
    header = m.group(0) if m else ''
    return header, json.loads(text[len(header):])


def main():
    # Omega carried one extra section (FrontrowMD clinician reviews); the Clinicians' Choice banner is already on the gallery.
    if os.path.exists(path('omega')):
        header, data = load(path('omega'))
        for sec in data['sections'].values():
            if sec['type'] == 'custom-liquid' and 'FrontrowMD' in sec.get('settings', {}).get('liquid', ''):
                sec['disabled'] = True
        open(path('omega'), 'w').write(header + json.dumps(data, indent=2, ensure_ascii=False) + '\n')

    for target, source in TARGETS.items():
        if not (os.path.exists(path(target)) and os.path.exists(path(source))):
            continue
        header, data = load(path(target))
        _, src = load(path(source))
        main_sec = data['sections']['main']
        sections = {'main': main_sec}
        order = ['main']
        for key in src['order']:
            if key == 'main':
                continue
            sections[key] = json.loads(json.dumps(src['sections'][key]))
            order.append(key)
        data['sections'], data['order'] = sections, order
        assert len(sections) <= 25, target
        open(path(target), 'w').write(header + json.dumps(data, indent=2, ensure_ascii=False) + '\n')
        print(path(target), '<-', path(source), len(order), 'sections')


if __name__ == '__main__':
    main()
