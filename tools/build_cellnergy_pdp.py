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


def rebuild(name, new_sections, seed=None):
    path = ROOT / 'templates' / f'{name}.json'
    if not path.exists():
        if not seed or not (ROOT / 'templates' / f'{seed}.json').exists():
            print(name, '-> skipped (template not in this checkout)')
            return
        header, d = load(ROOT / 'templates' / f'{seed}.json')
        print(name, f'-> created from {seed}.json')
    else:
        header, d = load(path)
    sections, order = {'main': d['sections']['main']}, ['main']
    for key, sec in new_sections:
        sections[key] = sec
        order.append(key)
    reviews = [k for k, v in d['sections'].items() if v['type'] == 'apps' and 'stamped-reviews/blocks/main-widget' in json.dumps(v)]
    for k in reviews[:1]:
        d['sections'][k].pop('disabled', None)
        sections[k] = d['sections'][k]
        order.append(k)
    d['sections'], d['order'] = sections, order
    assert len(order) <= 25
    write(path, header, d)
    print(name, '->', order)


TIMELINE_HEAD = {'eyebrow': 'What to Expect', 'heading': 'Benefits That Build Over Time',
                 'subheading': 'Use it daily and the benefits build. Here’s what to look for, and when.', 'next_label': 'What comes next'}
FAQ_HEAD = {'heading': 'Still Deciding? Start Here.', 'button_label': 'View All FAQs', 'contact_label': 'Contact Us',
            'q_who': '', 'q_how': '', 'q_when': ''}
FDA = '*These statements have not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure, or prevent any disease.'
WARRANTY_Q = ('item', {'question': 'What Is the Warranty?', 'answer': '<p>Your device comes with a one-year warranty from the date of purchase. If it develops a fault in that time, contact our Customer Service team. The warranty does not cover damage from not following the instruction manual, mishandling, or repair by an unauthorised party.</p>'})


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
        ('phase', {'image': IMG('lp-pdp-footcharge-rested.jpg'), 'label': '1 to 3 days', 'title': 'Steadier and More Rested',
                   'text': '<p>Continued use helps reawaken dormant nerve pathways and support microcirculation. You may notice less numbness, more stable movement, quicker reactions and more restorative sleep.*</p>'}),
        ('phase', {'image': IMG('lp-pdp-footcharge-seated-wide.jpg'), 'label': '1 month and beyond', 'title': 'A Daily Ritual That Lasts',
                   'text': '<p>Over time, FootCharge helps support cellular energy, nerve pathways and coordination from the ground up. You may feel less discomfort, less stress and steadier energy through the day, without the crash.*</p>'}),
    ])),

    ('lp_faq', section('lp-pdp-faq', {
        'heading': 'Still Deciding? Start Here.', 'button_label': 'View All FAQs', 'contact_label': 'Contact Us',
        'q_who': '', 'q_how': '', 'q_when': '',
    }, [
        ('item', {'question': 'Why Do I Feel Tingling?', 'answer': '<p>The tingling comes from CellWave™ Bioactivation. If it feels too strong, lower the intensity with the “-” button.</p>'}),
        ('item', {'question': 'Why Does It Switch Off After 15 Minutes?', 'answer': '<p>The 15-minute timer is part of how FootCharge works. After a session your body needs time to absorb the benefits, and continuous use can reduce how well your feet respond. The timer keeps every session effective and avoids overstimulation.</p>'}),
        ('item', {'question': 'I Turned the Intensity Up but Feel No Difference', 'answer': '<p>Make sure both feet are damp and in full contact with both pads.</p>'}),
        ('item', {'question': 'How Long Does the Battery Last?', 'answer': '<p>A full charge takes up to 3 hours and covers several 15-minute sessions. Battery life varies with how often and how intensely you use it.</p>'}),
        WARRANTY_Q,
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


WELLNESS = [
    ('lp_overview', section('lp-pdp-overview', {
        'mf_image': 'image_benefits', 'image_fit': 'cover', 'caption': 'Cellnergy Wellness', 'media_position': 'start',
        'eyebrow': 'Why Cellnergy Wellness', 'heading': 'A New Wave to Feel Your Best',
        'text': '<p>Cellnergy Wellness brings three technologies together in one hand-held device. Terahertz waves may help activate healthy cells, 630 nm red light helps boost cellular energy, and gentle heat helps ease muscle tension and support relaxation.*</p><p>Ten minutes on each area, once a day, fits easily into your morning or evening routine.</p>',
        'chips_label': 'Supports', 'chips': 'Joint comfort, Skin health, Restful sleep, Stress relief, Feeling young',
        'note_label': '', 'note': '',
    }, [('stat', {'value': '3', 'label': 'Technologies in one device'}), ('stat', {'value': '630 nm', 'label': 'Red light'}),
        ('stat', {'value': '10 min', 'label': 'Per area, daily'}), ('stat', {'value': '3', 'label': 'Speed and heat settings'})])),
    ('lp_tech', section('lp-pdp-cards', {
        'style': 'icon', 'columns': 3, 'background': 'none', 'eyebrow': 'The Technology', 'heading': 'Three Technologies, One Device',
        'text': '<p>Each works at a different depth, so together they support your body from the skin down to the cells.</p>', 'disclaimer': '',
    }, [
        ('card', {'icon': 'cell', 'label': 'Terahertz waves', 'title': 'Terahertz Waves (THz)', 'text': '<p>May help activate healthy cells, supporting cellular regeneration, tissue repair and overall vitality.*</p>'}),
        ('card', {'icon': 'sparkle', 'label': '630 nm', 'title': 'Red Light Therapy', 'text': '<p>Reaches deeper than other light colours to help boost cellular energy (ATP), supporting collagen production, circulation and recovery.*</p>'}),
        ('card', {'icon': 'heart', 'label': 'Controlled warmth', 'title': 'Heat Therapy', 'text': '<p>Delivers gentle, controlled heat to targeted areas to help improve blood flow, ease muscle tension and discomfort, and promote relaxation.*</p>'}),
    ])),
    ('lp_benefits', section('lp-pdp-cards', {
        'style': 'number', 'columns': 3, 'background': 'sand', 'eyebrow': 'Benefits', 'heading': 'Support That Builds Session by Session',
        'text': '', 'disclaimer': '*This product is used for self-education and research purposes to support general wellbeing. It is not intended to treat disease or to prevent impairment of human health. When used according to directions, it does not present any potential risk of illness or injury.',
    }, [
        ('card', {'title': 'Renewed-Looking Skin', 'text': '<p>Supports collagen and fibroblast production for skin that looks rejuvenated.*</p>'}),
        ('card', {'title': 'Better Circulation', 'text': '<p>Helps increase blood circulation, aiding nutrient delivery and waste removal.*</p>'}),
        ('card', {'title': 'Everyday Comfort', 'text': '<p>Helps reduce inflammation and supports overall comfort.*</p>'}),
        ('card', {'title': 'A More Youthful Look', 'text': '<p>Helps soften the look of wrinkles, fine lines and age spots.*</p>'}),
        ('card', {'title': 'Faster Recovery', 'text': '<p>Helps support recovery after physical activity.*</p>'}),
        ('card', {'title': 'A Brighter Mood', 'text': '<p>Supports a positive mood and a general sense of wellbeing.*</p>'}),
    ])),
    ('lp_how', section('lp-pdp-split', {
        'mf_image': 'image_ingredients', 'caption': 'Hold it 20 to 30 cm from your skin', 'image_fit': 'cover',
        'media_position': 'start', 'background': 'none', 'eyebrow': 'How to Use', 'heading': '10 Minutes on Each Area', 'text': '',
    }, [
        ('step', {'text': '<p>Choose a setting: 1 for high speed and low heat, 2 for low speed and high heat, or 3 for medium speed and high heat.</p>'}),
        ('step', {'text': '<p>Hold the device 20 to 30 cm (8 to 12 inches) away from your body.</p>'}),
        ('step', {'text': '<p>Move it in slow sweeping or circular motions, over bare skin or clothing.</p>'}),
        ('step', {'text': '<p>Spend 10 minutes on each area, in the morning or evening.</p>'}),
        ('note', {'icon': 'clock', 'text': 'Use in 10-minute intervals, then switch the device off for at least 5 minutes to cool down.'}),
        ('note', {'icon': 'shield', 'text': 'Not for use on open wounds, near metal implants, or during pregnancy or menstruation.'}),
        ('row', {'label': 'Certifications', 'value': '<p>Patent-pending, CE, UL, ISO 9001, ISO 14001, 9S Methodology</p>'}),
        ('row', {'label': 'Power', 'value': '<p>110–127V or 220–240V, 50/60Hz, 900W input</p>'}),
        ('row', {'label': 'Warranty', 'value': '<p>One year from the date of purchase</p>'}),
    ])),
    ('lp_timeline', section('lp-pdp-timeline', dict(TIMELINE_HEAD, image_1=IMG('lp-tl-wellness-1.jpg'), image_2=IMG('lp-tl-wellness-2.jpg'), image_3=IMG('lp-tl-wellness-3.jpg')))),
    ('lp_faq', section('lp-pdp-faq', FAQ_HEAD, [
        ('item', {'question': 'What Settings Does the Device Have?', 'answer': '<p>There are four settings: 0 is off, 1 is high speed with low heat, 2 is low speed with high heat, and 3 is medium speed with high heat.</p>'}),
        ('item', {'question': 'Can I Use It on My Scalp?', 'answer': '<p>Yes. Hold it 20 to 30 cm from your scalp, as long as there are no open wounds.</p>'}),
        ('item', {'question': 'Does It Emit Electromagnetic Radiation?', 'answer': '<p>No. The device has been tested with an electromagnetic radiation detector and does not emit radiation.</p>'}),
        ('item', {'question': 'Can I Use It If I Have a Health Condition?', 'answer': '<p>If you have a pre-existing health concern or condition, please speak to your healthcare provider before using the device.</p>'}),
        WARRANTY_Q,
        ('item', GUARANTEE_Q),
    ])),
]

POWER_CREAM = [
    ('lp_overview', section('lp-pdp-overview', {
        'mf_image': 'image_ingredients', 'image_fit': 'cover', 'caption': 'Cellnergy Power Cream', 'media_position': 'start',
        'eyebrow': 'Why Power Cream', 'heading': 'Relief That Doesn’t Wait',
        'text': '<p>Cellnergy Power Cream is a self-warming cream for achy joints and tired muscles. Its ThermalWave Technology pairs Bio-Active Growth Factors with a natural warming agent and infrared minerals, for a comforting warmth that helps ease joint discomfort and supports relaxation.*</p><p>Apply twice a day, or on the back of the neck and upper back before bed to help you unwind.</p>',
        'chips_label': 'Supports', 'chips': 'Joint comfort, Circulation, Deep sleep, Relaxation',
        'note_label': '', 'note': '',
    }, [('stat', {'value': '3', 'label': 'Active technologies'}), ('stat', {'value': '2×', 'label': 'A day'}),
        ('stat', {'value': '1–60 min', 'label': 'Gentle warming'})])),
    ('lp_tech', section('lp-pdp-cards', {
        'style': 'icon', 'columns': 3, 'background': 'sand', 'eyebrow': 'The Formula', 'heading': 'Three Technologies in One Cream',
        'text': '', 'disclaimer': FDA,
    }, [
        ('card', {'icon': 'cell', 'label': 'Growth factors', 'title': 'Egg Bioactive Growth Factors', 'text': '<p>A proprietary blend including FGF-2, designed to help reactivate dormant stem cells and support the body’s natural repair.*</p>'}),
        ('card', {'icon': 'sparkle', 'label': 'Self-warming', 'title': 'ThermalWave Technology', 'text': '<p>A natural warming agent and infrared minerals help soothe achy joints, stimulate blood flow and promote cellular activity.*</p>'}),
        ('card', {'icon': 'leaf', 'label': 'Joint support', 'title': 'Joint Support Formula', 'text': '<p>Hyaluronic acid, vitamins A and C, ceramides, arnica and hemp to support joint comfort.*</p>'}),
    ])),
    ('lp_how', section('lp-pdp-split', {
        'mf_image': 'image_benefits', 'caption': 'Massage in until absorbed', 'image_fit': 'contain',
        'media_position': 'start', 'background': 'none', 'eyebrow': 'How to Use', 'heading': 'Twice a Day, Where You Need It', 'text': '',
    }, [
        ('step', {'text': '<p>Apply a generous amount to the areas that need it, such as knees, shoulders or lower back.</p>'}),
        ('step', {'text': '<p>Massage gently until the cream is fully absorbed.</p>'}),
        ('step', {'text': '<p>Repeat morning and evening.</p>'}),
        ('note', {'icon': 'sparkle', 'text': 'Pro tip: for better sleep, apply to the back of your neck and upper back before bed.'}),
        ('row', {'label': 'Free from', 'value': '<p>Parabens, phthalates and sulfates. Hypoallergenic.</p>'}),
        ('row', {'label': 'Certifications', 'value': '<p>ISO 9001</p>'}),
    ])),
    ('lp_timeline', section('lp-pdp-timeline', dict(TIMELINE_HEAD, image_1=IMG('lp-tl-cream-1.jpg'), image_2=IMG('lp-tl-cream-2.jpg'), image_3=IMG('lp-tl-cream-3.jpg')))),
    ('lp_faq', section('lp-pdp-faq', FAQ_HEAD, [
        ('item', {'question': 'What Is ThermalWave Technology?', 'answer': '<p>A blend of a natural sensory agent and infrared minerals that makes the cream self-warming. It creates a soothing warmth on your skin and joints and helps stimulate blood flow.*</p>'}),
        ('item', {'question': 'Where Do the Growth Factors Come From?', 'answer': '<p>From fertilised avian eggs sourced from a USDA-inspected farm in the USA. The hens are raised cage-free on high-quality whole grains, and no chemicals or extreme heat are used in processing.</p>'}),
        ('item', {'question': 'Can I Use It With Other Creams or Supplements?', 'answer': '<p>Yes. It does not interfere with other creams, medication or supplements. It also pairs well with the Cellnergy Wellness device and LAMININE.</p>'}),
        ('item', {'question': 'Who Should Not Use It?', 'answer': '<p>It is suitable for anyone over 12. If you are pregnant, nursing or have a medical condition, please speak to your physician first.</p>'}),
        ('item', {'question': 'Full List of Ingredients', 'answer': '{{ product.metafields.custom.ingredients | metafield_tag }}'}),
        ('item', GUARANTEE_Q),
    ])),
]

HYDRATION = [
    ('lp_overview', section('lp-pdp-overview', {
        'media_index': 2, 'image_fit': 'contain', 'caption': 'Cellnergy Hydration System', 'media_position': 'start',
        'eyebrow': 'Why Cellnergy Hydration', 'heading': 'Regeneration Begins With Water',
        'text': '<p>Your body depends on water every day. The Cellnergy Hydration System makes that daily habit work harder, combining four water-conditioning technologies in one reusable bottle.</p><p>Fill it with filtered water, wait about 15 minutes, and drink through the day. No powders, mixing, batteries or charging.</p>',
        'chips_label': 'In every refill', 'chips': 'Hydrogen-rich water, Alkaline conditioning, Trace minerals, A smoother taste, No electricity',
        'note_label': '', 'note': '',
    }, [('stat', {'value': '4', 'label': 'Technologies'}), ('stat', {'value': 'pH 8–9.5', 'label': 'Alkaline water'}),
        ('stat', {'value': '1.1 mg/L', 'label': 'Dissolved hydrogen'}), ('stat', {'value': '15 min', 'label': 'To condition'})])),
    ('lp_tech', section('lp-pdp-cards', {
        'style': 'number', 'columns': 4, 'background': 'sand', 'eyebrow': 'The Technology', 'heading': 'Four Technologies, One Bottle',
        'text': '<p>One 15-minute conditioning process. No electricity required.</p>', 'disclaimer': FDA,
    }, [
        ('card', {'title': 'Mineral Activation', 'text': '<p>A replaceable Mineral Activation Diffuser holds essential trace minerals that condition your water as it rests in the bottle.</p>'}),
        ('card', {'title': 'Alkaline Conditioning', 'text': '<p>Helps raise your water to a pH of about 8 to 9.5, depending on the water you start with, for a smooth taste.</p>'}),
        ('card', {'title': 'Molecular Hydrogen', 'text': '<p>1.1 mg/L (1,100 ppb) of dissolved hydrogen after 15 minutes, independently measured by H2 Analytics (2026). More than twice the 0.5 mg/L industry threshold.*</p>'}),
        ('card', {'title': 'Far-Infrared and Terahertz', 'text': '<p>Far-infrared mineral media and terahertz-frequency technology add a further layer to the non-powered conditioning system.</p>'}),
    ])),
    ('lp_how', section('lp-pdp-split', {
        'mf_image': 'image_ingredients', 'caption': 'Fill, condition, drink', 'image_fit': 'cover',
        'media_position': 'start', 'background': 'none', 'eyebrow': 'How to Use', 'heading': 'Fill, Wait 15 Minutes, Drink', 'text': '',
    }, [
        ('step', {'text': '<p>Fill the bottle with filtered or purified drinking water.</p>'}),
        ('step', {'text': '<p>Leave it for about 15 minutes while the minerals condition the water.</p>'}),
        ('step', {'text': '<p>Drink throughout the day as part of your hydration routine.</p>'}),
        ('note', {'icon': 'drop', 'text': 'Before first use: wash the bottle 2–3 times with mild dish soap, rinse the diffuser, then fill, shake and empty until the water runs clear.'}),
        ('note', {'icon': 'clock', 'text': 'Replace the Mineral Activation Diffuser about every 2 months for the best performance.'}),
        ('row', {'label': 'Care', 'value': '<p>Hand wash only and air-dry with the lid open. Do not microwave, freeze or fill with boiling liquids.</p>'}),
        ('row', {'label': 'Temperature', 'value': '<p>Cold and warm water up to 60°C / 140°F</p>'}),
        ('row', {'label': 'Material', 'value': '<p>BPA-free, medical-grade Tritan™</p>'}),
    ])),
    ('lp_timeline', section('lp-pdp-timeline', dict(TIMELINE_HEAD, subheading='Drink from it daily and the difference builds. Here’s what to look for, and when.'), [
        ('phase', {'mf_image': 'phase_4_image,image_benefits', 'label': 'Day 1', 'title': 'A Noticeably Different Sip', 'text': '<p>Most people notice a smoother, cleaner, lighter taste from the very first glass.*</p>'}),
        ('phase', {'mf_image': 'phase_1_image,image_benefits', 'label': 'Week 1', 'title': 'Feeling Genuinely Hydrated', 'text': '<p>Many people feel more refreshed and satisfied after drinking, with a lighter sensation that stays through the day.*</p>'}),
        ('phase', {'mf_image': 'phase_2_image,image_benefits', 'label': 'Month 1', 'title': 'Steadier Energy, Clearer Days', 'text': '<p>With daily use, steadier energy through the day becomes noticeable and the afternoon dip eases.*</p>'}),
        ('phase', {'mf_image': 'phase_3_image,image_benefits', 'label': 'Month 2 and beyond', 'title': 'A Foundation for Everything Else', 'text': '<p>Many people report quicker recovery after exercise, clearer focus and healthier-looking skin, as hydration supports the rest of their routine.*</p>'}),
    ])),
    ('lp_faq', section('lp-pdp-faq', FAQ_HEAD, [
        ('item', {'question': 'How Does It Work?', 'answer': '<p>A built-in mineral diffuser conditions your water with mineral alkalisation (pH 8 to 9.5), molecular hydrogen and terahertz-frequency restructuring. Fill it with filtered water, wait 15 minutes, and it is ready to drink.*</p>'}),
        ('item', {'question': 'What Water Should I Use?', 'answer': '<p>Filtered or purified water. It lets the technologies work best and gives the cleanest taste.</p>'}),
        ('item', {'question': 'Does Alkaline Water Change My Body’s pH?', 'answer': '<p>No. Your body tightly regulates its blood pH. Alkaline water is not intended to change it; it is designed to support everyday hydration.</p>'}),
        ('item', {'question': 'Is the Bottle Safe?', 'answer': '<p>Yes. It is made from BPA-free, medical-grade Tritan™ and suits cold and warm water up to 60°C / 140°F. It is not suitable for boiling or hot liquids.</p>'}),
        ('item', {'question': 'Do I Need to Replace the Diffuser?', 'answer': '<p>Yes, about every 2 months of daily use. After that the mineral output declines and the water gradually returns to ordinary. Replacement diffusers are sold separately.</p>'}),
        ('item', GUARANTEE_Q),
    ])),
]

DIFFUSER = [
    ('lp_overview', section('lp-pdp-overview', {
        'image': IMG('lp-pdp-diffuser-hero.jpg'), 'image_fit': 'cover', 'caption': 'Cellnergy Mineral Activation Diffuser', 'media_position': 'start',
        'eyebrow': 'Why Replace It', 'heading': 'Keep Every Sip at Its Best',
        'text': '<p>Your Cellnergy Hydration System depends on one thing: fresh minerals. Over time the diffuser’s output declines and your water slowly returns to ordinary.</p><p>A fresh Mineral Activation Diffuser restores hydrogen output, alkaline balance and water structuring within 15 minutes of your first fill.</p>',
        'chips_label': '', 'chips': '', 'note_label': 'Fits:', 'note': 'Cellnergy Hydration System',
    }, [('stat', {'value': '15 min', 'label': 'Back to full performance'}), ('stat', {'value': '3', 'label': 'Mineral technologies'}),
        ('stat', {'value': '2 months', 'label': 'Of daily use'})])),
    ('lp_tech', section('lp-pdp-cards', {
        'style': 'icon', 'columns': 3, 'background': 'none', 'eyebrow': 'The Minerals', 'heading': 'Three Technologies, Restored in 15 Minutes',
        'text': '<p>The same mineral blend as your original diffuser, active from the first fill. No break-in period.</p>', 'disclaimer': '',
    }, [
        ('card', {'icon': 'bolt', 'label': 'Hydrogen', 'title': 'Active Hydrogen Minerals', 'text': '<p>Restore molecular hydrogen output, with antioxidant support from your very first sip.*</p>'}),
        ('card', {'icon': 'drop', 'label': 'Alkaline', 'title': 'Alkaline Mineral Blend', 'text': '<p>Re-establishes a higher alkaline pH on the first fill, for smoother-tasting water.</p>'}),
        ('card', {'icon': 'cell', 'label': 'Structuring', 'title': 'Terahertz-Compatible Minerals', 'text': '<p>Restore the mineral and frequency synergy your bottle was designed for.</p>'}),
    ])),
    ('lp_compare', section('lp-pdp-cards', {
        'style': 'icon', 'columns': 2, 'background': 'sand', 'eyebrow': 'The Difference', 'heading': 'Fresh Diffuser vs. Depleted Diffuser',
        'text': '', 'disclaimer': FDA,
    }, [
        ('card', {'icon': 'check', 'title': 'With a Fresh Diffuser', 'text': '<p>Full hydrogen output from the first fill. Alkaline balance restored straight away. Water structuring back at its best, so your supplements and daily habits get the hydration support they were designed for.*</p>'}),
        ('card', {'icon': 'refresh', 'title': 'With a Depleted Diffuser', 'text': '<p>Hydrogen output drops close to zero and the pH drifts back to neutral. Structuring fades, and you are left with ordinary water from a premium bottle.</p>'}),
    ])),
    ('lp_how', section('lp-pdp-split', {
        'mf_image': 'image_ingredients', 'caption': 'Swap, rinse, fill', 'image_fit': 'cover',
        'media_position': 'start', 'background': 'none', 'eyebrow': 'How to Replace', 'heading': 'Swap It in a Minute', 'text': '',
    }, [
        ('step', {'text': '<p>Remove the old diffuser from the base of your bottle.</p>'}),
        ('step', {'text': '<p>Rinse the new diffuser under running water for 30 seconds.</p>'}),
        ('step', {'text': '<p>Insert it securely into the base and tighten.</p>'}),
        ('step', {'text': '<p>Fill with filtered or purified water, wait 15 minutes, and enjoy.</p>'}),
        ('note', {'icon': 'drop', 'text': 'Rinse the diffuser under running water after each refill. Hand wash the bottle only, never in the dishwasher.'}),
    ])),
    ('lp_timeline', section('lp-pdp-timeline', {'eyebrow': 'What to Expect', 'heading': 'The Life of a Diffuser',
                                                'subheading': 'Here’s what happens to your water over time, and when to swap.', 'next_label': 'What comes next'}, [
        ('phase', {'image': IMG('lp-tl-diffuser-1.jpg'), 'label': 'Day 1', 'title': 'Full Performance Restored', 'text': '<p>Fresh minerals are active within 15 minutes. Hydrogen output, alkaline balance and water structuring are all back.</p>'}),
        ('phase', {'image': IMG('lp-tl-diffuser-2.jpg'), 'label': 'Months 1 to 2', 'title': 'Peak Hydration', 'text': '<p>Every sip delivers hydrogen-rich, alkaline, structured water to support your daily routine.*</p>'}),
        ('phase', {'image': IMG('lp-tl-diffuser-3.jpg'), 'label': 'Month 3', 'title': 'Output Begins to Decline', 'text': '<p>Performance drops gradually and quietly: hydrogen falls and the pH drifts. Most people do not notice for weeks.</p>'}),
        ('phase', {'image': IMG('lp-tl-diffuser-4.jpg'), 'label': 'Replace now', 'title': 'Back to Full Performance', 'text': '<p>Swap the diffuser and fill the bottle. Fifteen minutes later, your water is working as designed again.</p>'}),
    ])),
    ('lp_faq', section('lp-pdp-faq', dict(FAQ_HEAD, button_label=''), [
        ('item', {'question': 'How Often Should I Replace It?', 'answer': '<p>About every 2 months of daily use, when mineral output starts to decline.</p>'}),
        ('item', {'question': 'What Happens If I Don’t Replace It?', 'answer': '<p>The minerals do not expire dangerously; they simply stop conditioning. Your water gradually returns to that of a regular bottle until you fit a fresh diffuser.</p>'}),
        ('item', {'question': 'Which Bottle Does It Fit?', 'answer': '<p>The Cellnergy Hydration System.</p>'}),
        ('item', GUARANTEE_Q),
    ])),
]

if __name__ == '__main__':
    rebuild('product.cellnergy-footcharge', FOOTCHARGE)
    rebuild('product.cellnergy-wellness-stand', STAND)
    rebuild('product.one-time-purchase', WELLNESS)
    rebuild('product.cellnergy-power-cream', POWER_CREAM, seed='product')
    rebuild('product.cellnergy-water-bottle', HYDRATION)
    rebuild('product.cellnergy-diffuser-new', DIFFUSER)
