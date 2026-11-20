"""Rebuild the lower half of the two Cellnergy device PDP templates (FootCharge, Wellness Stand) with the LP premium
sections (lp-pdp-overview, lp-pdp-cards, lp-pdp-split, lp-pdp-timeline, lp-pdp-faq). Keeps the `main` section and the
Stamped reviews app section untouched. Run from a theme checkout root; images are Files that exist in UK, US and EU.

    python3 tools/build_cellnergy_pdp.py            # writes templates/product.cellnergy-*.json
"""
import json, sys, pathlib

ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
IMG = lambda name: f'shopify://shop_images/{name}'
GUARANTEE_Q = {'question': 'What If It Isn’t Right for Me?',
               'answer': '<p>Then you don’t pay for it. Every LifePharm product comes with a 60-day money-back guarantee. Let us know within 60 days of delivery and we’ll refund you in full.</p>'}


def blocks(items):
    out, order = {}, []
    for i, (btype, settings) in enumerate(items, 1):
        key = f'{btype}_{i}'
        out[key] = {'type': btype, 'settings': settings}
        order.append(key)
    return out, order


def section(stype, settings, items=()):
    b, o = blocks(items)
    s = {'type': stype, 'settings': settings}
    if o:
        s['blocks'], s['block_order'] = b, o
    return s


def load(path):
    raw = path.read_text()
    i = raw.index('{')
    return raw[:i], json.loads(raw[i:])


def write(path, header, data):
    path.write_text(header + json.dumps(data, indent=2, ensure_ascii=False) + '\n')


def rebuild(name, new_sections):
    path = ROOT / 'templates' / f'{name}.json'
    header, d = load(path)
    keep = {'main': d['sections']['main']}
    reviews_key = '17128952497cac699c'
    sections, order = dict(keep), ['main']
    for key, sec in new_sections:
        sections[key] = sec
        order.append(key)
    if reviews_key in d['sections']:
        sections[reviews_key] = d['sections'][reviews_key]
        sections[reviews_key].pop('disabled', None)
        order.append(reviews_key)
    d['sections'], d['order'] = sections, order
    assert len(order) <= 25
    write(path, header, d)
    print(name, '->', order)


FOOTCHARGE = [
    ('lp_overview', section('lp-pdp-overview', {
        'image': IMG('CellnergyFOOTCHARGE-withbox.png'), 'image_fit': 'contain', 'caption': 'Cellnergy FootCharge and its box', 'media_position': 'start',
        'eyebrow': 'Why FootCharge', 'heading': 'Regeneration From the Ground Up',
        'text': '<p>Cellnergy FootCharge brings full-body regeneration from the ground up by stimulating the nerve-rich zones in your feet. It combines CellWave™ Bioactivation, Terahertz Resonance and Infrared Thermotherapy to help restore neuromuscular communication, support circulation and support cellular energy production.</p><p>Whether you’re dealing with fatigue, numbness or stress, it helps your body rebalance through a daily, drug-free ritual.</p>',
        'chips_label': 'Regenerative Support For',
        'chips': 'Nervous system support, Circulation, Nerve-related discomfort, Balance and coordination, Cellular energy, Nerve fatigue, Restorative sleep',
        'note_label': '', 'note': '',
    }, [('stat', {'value': '6', 'label': 'Smart modes'}), ('stat', {'value': '10', 'label': 'Intensity levels'}),
        ('stat', {'value': '2', 'label': 'Heat levels'}), ('stat', {'value': '15 min', 'label': 'Auto-off session'})])),

    ('lp_tech', section('lp-pdp-cards', {
        'style': 'image', 'columns': 3, 'background': 'none', 'eyebrow': 'The Technology',
        'heading': 'Three Technologies, One Daily Ritual',
        'text': '<p>Together they create a complete regenerative experience, designed to help restore your feet, your nervous system and your overall wellbeing.</p>',
        'disclaimer': '',
    }, [
        ('card', {'image': IMG('AdobeStock_912094788.jpg'), 'label': 'Low-frequency waves', 'title': 'CellWave™ Bioactivation',
                  'text': '<p>Gentle low-frequency waves stimulate your nerves and neuromuscular pathways. This may awaken dormant signalling between brain and body, supporting balance, coordination and nervous system vitality.</p>'}),
        ('card', {'image': IMG('AdobeStock_1439178340.jpg'), 'label': 'About 1 THz', 'title': 'Terahertz Resonance',
                  'text': '<p>Terahertz resonance helps reactivate cellular activity by harmonising your body’s natural electromagnetic rhythms, supporting renewed energy and functional vitality at the cellular level.</p>'}),
        ('card', {'image': IMG('AdobeStock_1338758573.jpg'), 'label': '38 to 45°C', 'title': 'Infrared Thermotherapy',
                  'text': '<p>Soothing, controlled heat reaches deep into your tissues to help boost circulation and oxygenation. Better blood flow supports cellular repair and recovery while easing tension and discomfort.</p>'}),
    ])),

    ('lp_modes', section('lp-pdp-cards', {
        'style': 'number', 'columns': 3, 'background': 'sand', 'eyebrow': '6 Smart Modes',
        'heading': 'A Mode for How You Feel Today',
        'text': '<p>Pair any mode with one of 2 heat levels and 10 intensity levels.</p>',
        'disclaimer': '*If you have any medical concerns or conditions, please consult a physician before use. This product is intended for educational and research purposes to support general wellness. It is not designed to diagnose, treat, cure or prevent any disease. When used as directed, it poses no risk of illness or injury.',
    }, [
        ('card', {'title': 'Relax', 'text': '<p>Supports deeper, more restorative sleep and helps reduce nerve-related fatigue for renewed energy.*</p>'}),
        ('card', {'title': 'Knead', 'text': '<p>Helps boost circulation and ease muscle tension and discomfort.*</p>'}),
        ('card', {'title': 'Tap', 'text': '<p>Helps sharpen reaction time, supporting balance, coordination, agility and confident mobility.*</p>'}),
        ('card', {'title': 'Squeeze', 'text': '<p>Helps support nerve sensitivity and brain-body communication, for responsiveness, mental clarity and focus.*</p>'}),
        ('card', {'title': 'Pulse', 'text': '<p>Helps support metabolism and ease numbness, tingling and neuropathy-related discomfort.*</p>'}),
        ('card', {'title': 'Strength', 'text': '<p>Helps support stability and power, and helps maintain muscle tone.*</p>'}),
    ])),

    ('lp_how', section('lp-pdp-split', {
        'image': IMG('lp-pdp-footcharge-seated.jpg'), 'caption': 'Sit down, bare feet flat on the pads', 'image_fit': 'cover',
        'media_position': 'start', 'background': 'none', 'eyebrow': 'How to Use',
        'heading': '15 Minutes, Up to Twice a Day', 'text': '',
    }, [
        ('step', {'text': '<p>Sit comfortably and place your bare feet on the FootCharge pads.</p>'}),
        ('step', {'text': '<p>Hold the power button for 3 seconds to turn the device on.</p>'}),
        ('step', {'text': '<p>Choose one of the 6 smart modes.</p>'}),
        ('step', {'text': '<p>Pick one of the 2 heat levels.</p>'}),
        ('step', {'text': '<p>Adjust the 10 intensity levels to your comfort.</p>'}),
        ('note', {'icon': 'drop', 'text': 'Tip: moisten your feet with a damp towel first. Damp feet in full contact with the pads improve conductivity.'}),
        ('note', {'icon': 'clock', 'text': 'Each session switches off after 15 minutes. Use 15 to 30 minutes per session, up to twice daily, and no more than 60 minutes a day.'}),
        ('row', {'label': 'Certifications', 'value': '<p>Patent-pending, CE, UL, ISO 9001, ISO 14001, PSE, RoHS, FCC</p>'}),
        ('row', {'label': 'Warranty', 'value': '<p>One year from the date of purchase</p>'}),
    ])),

    ('lp_timeline', section('lp-pdp-timeline', {
        'eyebrow': 'What to Expect', 'heading': 'Benefits That Build Over Time',
        'subheading': 'Use it daily and the benefits build. Here’s what to look for, and when.', 'next_label': 'What comes next',
    }, [
        ('phase', {'image': IMG('AdobeStock_1273796619.jpg'), 'label': '1 to 30 minutes', 'title': 'Warmth and Relief',
                   'text': '<p>As soon as your feet are on the pads, gentle warmth and bioactivation begin. Low-frequency stimulation and infrared heat help awaken tired nerves and soothe tension, so you may feel immediate relief and deep relaxation.*</p>'}),
        ('phase', {'image': IMG('lp-hover-cellnergy-footcharge.jpg'), 'label': '1 to 3 days', 'title': 'Steadier and More Rested',
                   'text': '<p>Continued use helps reawaken dormant nerve pathways and support microcirculation. You may notice less numbness, more stable movement, quicker reactions and more restorative sleep.*</p>'}),
        ('phase', {'image': IMG('lp-pdp-footcharge-seated-wide.jpg'), 'label': '1 month and beyond', 'title': 'A Daily Ritual That Lasts',
                   'text': '<p>Over time, FootCharge helps support cellular energy, nerve pathways and coordination from the ground up. You may feel less discomfort, less stress and steadier energy through the day, without the crash.*</p>'}),
    ])),

    ('lp_faq', section('lp-pdp-faq', {
        'heading': 'Still Deciding? Start Here.', 'button_label': 'View All FAQs', 'contact_label': 'Contact Us',
        'q_who': 'Who is [product] for?', 'q_how': 'How do I use [product]?', 'q_when': 'When will I notice a difference?',
    }, [
        ('item', {'question': 'Why Do I Feel Tingling?', 'answer': '<p>The tingling comes from CellWave™ Bioactivation. If it feels too strong, lower the intensity with the “-” button.</p>'}),
        ('item', {'question': 'Why Does It Switch Off After 15 Minutes?', 'answer': '<p>The 15-minute timer is part of how FootCharge works. After a session your body needs time to absorb the benefits, and continuous use can reduce how well your feet respond. The timer keeps every session effective and avoids overstimulation.</p>'}),
        ('item', {'question': 'I Turned the Intensity Up but Feel No Difference', 'answer': '<p>Make sure both feet are damp and in full contact with both pads.</p>'}),
        ('item', {'question': 'How Long Does the Battery Last?', 'answer': '<p>A full charge takes up to 3 hours and covers several 15-minute sessions. Battery life varies with how often and how intensely you use it.</p>'}),
        ('item', {'question': 'What Is the Warranty?', 'answer': '<p>FootCharge comes with a one-year warranty from the date of purchase. If your device develops a fault in that time, contact our Customer Service team. The warranty does not cover damage from not following the instruction manual, mishandling, or repair by an unauthorised party.</p>'}),
        ('item', GUARANTEE_Q),
    ])),
]

STAND = [
    ('lp_overview', section('lp-pdp-overview', {
        'image': IMG('lp-hover-cellnergy-wellness-stand.jpg'), 'image_fit': 'cover', 'caption': 'Cellnergy Wellness Stand', 'media_position': 'start',
        'eyebrow': 'Hands-Free Therapy', 'heading': 'Your Therapy. Hands-Free. Exactly Where You Need It.',
        'text': '<p>The Cellnergy Wellness Stand holds your device at the precise height and angle you need, completely hands-free. It folds away for storage or travel and is built from coated steel that won’t rust.</p><p>Already own the Cellnergy Wellness Device? The stand changes how, and where, you use it every day.</p>',
        'chips_label': '', 'chips': '', 'note_label': '', 'note': '',
    }, [('stat', {'value': '60–160cm', 'label': 'Height range'}), ('stat', {'value': 'Foldable', 'label': 'Tripod design'}),
        ('stat', {'value': 'Included', 'label': 'Carry bag'})])),

    ('lp_features', section('lp-pdp-cards', {
        'style': 'icon', 'columns': 3, 'background': 'sand', 'eyebrow': 'Built for Daily Use',
        'heading': 'Built for Daily Use. Ready to Travel.', 'text': '', 'disclaimer': '',
    }, [
        ('card', {'icon': 'refresh', 'title': 'Adjustable Height', 'text': '<p>The telescoping pole adjusts from 60cm to 160cm, so knees, lower back, shoulders and neck are all within reach.</p>'}),
        ('card', {'icon': 'sparkle', 'title': 'Multi-Angle Positioning', 'text': '<p>Set the exact angle for the area you’re targeting. The device stays locked in place for the whole session, so coverage is consistent.</p>'}),
        ('card', {'icon': 'heart', 'title': 'Hands-Free Sessions', 'text': '<p>Sit, stand or lie back while your Cellnergy Wellness Device does the work. Read, rest and recover without holding a thing.</p>'}),
        ('card', {'icon': 'check', 'title': 'Foldable Tripod', 'text': '<p>The tripod base folds down in seconds into a compact form, for storage between sessions or packing for travel.</p>'}),
        ('card', {'icon': 'shield', 'title': 'Anti-Rust Coating', 'text': '<p>An electrophoretic coating forms a protective anti-rust layer on the steel, built to hold up in any room for the long term.</p>'}),
        ('card', {'icon': 'truck', 'title': 'Carry Bag Included', 'text': '<p>Take your full Cellnergy set-up anywhere: a second home, a hotel room or a friend’s place.</p>'}),
    ])),

    ('lp_why', section('lp-pdp-split', {
        'image': IMG('CellnergyStand-Full-Shorter.png'), 'caption': 'Stand with the Wellness Device', 'image_fit': 'contain',
        'media_position': 'end', 'background': 'none', 'eyebrow': 'Why It Matters',
        'heading': 'Consistency Is What Creates Results',
        'text': '<p>The research behind Cellnergy is built on consistent, daily use. The stand removes the biggest barrier to that consistency: holding the device in position for a full session, every day.</p><p>People who complete full, uninterrupted sessions are the ones who feel the difference. The stand makes that the default, not the exception.</p>',
    })),

    ('lp_specs', section('lp-pdp-split', {
        'image': IMG('CellnergyStand-Overview.png'), 'caption': 'Stand, mount and fittings', 'image_fit': 'contain',
        'media_position': 'start', 'background': 'none', 'eyebrow': 'Specifications',
        'heading': 'What’s in the Box', 'text': '',
    }, [
        ('row', {'label': 'In the box', 'value': '<p>Cellnergy Wellness Stand, portable carry bag, assembly hardware</p>'}),
        ('row', {'label': 'Material', 'value': '<p>High-quality steel</p>'}),
        ('row', {'label': 'Surface treatment', 'value': '<p>Electrophoretic anti-rust coating</p>'}),
        ('row', {'label': 'Height range', 'value': '<p>60cm to 160cm</p>'}),
        ('row', {'label': 'Design', 'value': '<p>Foldable tripod</p>'}),
        ('row', {'label': 'Compatible with', 'value': '<p>Cellnergy Wellness Device (sold separately)</p>'}),
    ])),
]

if __name__ == '__main__':
    rebuild('product.cellnergy-footcharge', FOOTCHARGE)
    rebuild('product.cellnergy-wellness-stand', STAND)
