"""Give every product template the same buy-box dropdowns and remove what they replace (D-066).

For each templates/product*.json in the checkout:
1. delete the "LifePharm Guarantee" offer card (the guarantee is already a trust tile and a dropdown);
2. switch on the standard dropdowns after the buy buttons: Benefits, Ingredients, How to Use and
   60-Day Money-Back Guarantee (a dropdown with no content for the product does not render);
3. where the page has a large "How to ..." lp-pdp-split section (device pages), move its steps and
   notes into the How to Use dropdown, its spec rows into a Specifications dropdown, and delete the section;
4. where the page has an lp-pdp-split section with an "In the box" row (What's in the Box), turn that row into
   the lp_box dropdown (one item per comma-separated entry; photos are set by hand afterwards, see BOX_PHOTOS),
   move the other rows into Specifications, and delete the section.
A template that shows no guarantee card and has neither section is left alone. Idempotent.

Usage: python3 tools/store-audit/pdp_dropdowns.py [--root <checkout>] [--apply]"""
import argparse, glob, json, os, pathlib, re

REPO = pathlib.Path(__file__).resolve().parent.parent.parent
BENEFITS, INGREDIENTS, HOWTO, GUARANTEE, SPECS = "collapsible_text_DKpjzh", "collapsible_text_KbRjKK", "collapsible_text_PDdyLw", "collapsible_text_XwdWte", "lp_specs"
BOX = "lp_box"
BASE = {"icon": "none", "icon_width": 20, "page": ""}
# Gallery position of the photo for each box item, per product template. Checked against the product media
# on the US, UK and EU stores (same eight photos in the same order) on 2026-11-23.
BOX_PHOTOS = {"product.cellnergy-wellness-stand": {"Cellnergy Wellness Stand": 7, "Portable carry bag": 5, "Assembly hardware": 1}}
STANDARD = {
    BENEFITS: {"title": "Benefits", "content": "{{ product.metafields.custom.text_benefits | metafield_tag }}"},
    INGREDIENTS: {"title": "Ingredients", "content": "{{ product.metafields.custom.ingredients | metafield_tag }}"},
    HOWTO: {"title": "How to Use", "content": "<p>{{ product.metafields.custom.value_2 | metafield_tag }}</p>", "lp_how_steps": True},
    GUARANTEE: {"title": "60-Day Money-Back Guarantee", "content": "<p>All of our products come with a 60-Day Money-Back Guarantee. </p><p>Try it, and if it doesn’t work, it's on us! Our hassle-free return policy offers a 100% money-back guarantee within 60 days of delivery.</p>"},
}
plain = lambda html: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html or "")).strip()


def after_buy_buttons(main):
    order, blocks = main["block_order"], main["blocks"]
    i = order.index("buy_buttons") if "buy_buttons" in order else next(k for k, b in enumerate(order) if blocks[b]["type"] == "buy_buttons")
    while i + 1 < len(order):
        nxt = blocks[order[i + 1]]; kind = nxt["type"]
        follows = kind == "payment_terms" or "afterpay" in kind or "affirm" in kind or (kind == "liquid" and "clinicianschoice" in nxt.get("settings", {}).get("liquid", ""))
        if not follows: break
        i += 1
    return i + 1


def convert(data, name=""):
    notes = []
    main = next((s for s in data["sections"].values() if s.get("type") == "main-product"), None)
    if not main or not any(b["type"] == "buy_buttons" for b in main.get("blocks", {}).values()):
        return notes
    blocks, order = main["blocks"], main["block_order"]
    is_card = lambda b: blocks[b]["type"] == "offer" and blocks[b].get("settings", {}).get("title") == "LifePharm Guarantee"
    split_with = lambda test: any(s.get("type") == "lp-pdp-split" and test(s) for s in data["sections"].values())
    shows_card = any(is_card(b) and not blocks[b].get("disabled") for b in order)
    has_how = split_with(lambda s: (s.get("settings", {}).get("eyebrow") or "").lower().startswith("how to") and any(b["type"] == "step" for b in s.get("blocks", {}).values()))
    has_box = split_with(lambda s: any(b["type"] == "row" and plain(b["settings"].get("label")).lower() == "in the box" for b in s.get("blocks", {}).values()))
    already = HOWTO in blocks and not blocks[HOWTO].get("disabled") and blocks[HOWTO].get("settings", {}).get("lp_how_steps") is False
    if not (shows_card or has_how or has_box or already or BOX in blocks):
        return notes  # a page that showed none of these (standard, funnel or legacy template) is left as it is
    for bid in [b for b in order if is_card(b)]:
        del blocks[bid]; order.remove(bid); notes.append("guarantee card removed")

    how = next((sid for sid in data["order"] if data["sections"][sid].get("type") == "lp-pdp-split"
                and (data["sections"][sid].get("settings", {}).get("eyebrow") or "").lower().startswith("how to")
                and any(b["type"] == "step" for b in data["sections"][sid].get("blocks", {}).values())), None)
    wanted = {k: dict(BASE, **v) for k, v in STANDARD.items()}
    specs = None
    if how:
        sec = data["sections"][how]; parts = [sec["blocks"][b] for b in sec.get("block_order", [])]
        steps = [plain(b["settings"].get("text")) for b in parts if b["type"] == "step"]
        tips = [plain(b["settings"].get("text")) for b in parts if b["type"] == "note"]
        rows = [(plain(b["settings"].get("label")), plain(b["settings"].get("value"))) for b in parts if b["type"] == "row"]
        wanted[HOWTO] = dict(BASE, title=sec["settings"]["eyebrow"], lp_how_steps=False,
                             content="<ol>" + "".join(f"<li>{s}</li>" for s in steps if s) + "</ol>" + "".join(f"<p>{t}</p>" for t in tips if t))
        if rows:
            specs = dict(BASE, title="Specifications", content="<ul>" + "".join(f"<li><strong>{k}:</strong> {v}</li>" for k, v in rows if k and v) + "</ul>")
        del data["sections"][how]; data["order"].remove(how); notes.append(f"'{sec['settings']['eyebrow']}' section moved into dropdowns ({len(steps)} steps, {len(tips)} notes, {len(rows)} spec rows)")
    elif HOWTO in blocks and blocks[HOWTO].get("settings", {}).get("lp_how_steps") is False and not blocks[HOWTO].get("disabled"):
        wanted[HOWTO] = blocks[HOWTO]["settings"]  # already converted on an earlier run

    box = None
    boxed = next((sid for sid in data["order"] if data["sections"][sid].get("type") == "lp-pdp-split"
                  and any(b["type"] == "row" and plain(b["settings"].get("label")).lower() == "in the box" for b in data["sections"][sid].get("blocks", {}).values())), None)
    if boxed:
        sec = data["sections"][boxed]; parts = [sec["blocks"][b] for b in sec.get("block_order", [])]
        rows = [(plain(b["settings"].get("label")), plain(b["settings"].get("value"))) for b in parts if b["type"] == "row"]
        items = [i.strip() for k, v in rows if k.lower() == "in the box" for i in v.split(",") if i.strip()]
        items = [i[0].upper() + i[1:] for i in items][:6]
        photos = BOX_PHOTOS.get(name, {})
        box = {"title": "What's in the Box"}
        for n, item in enumerate(items, 1):
            box[f"item_{n}"] = item; box[f"media_{n}"] = photos.get(item, 0)
        rest = [(k, v) for k, v in rows if k.lower() != "in the box" and k and v]
        if rest:
            specs = dict(BASE, title="Specifications", content="<ul>" + "".join(f"<li><strong>{k}:</strong> {v}</li>" for k, v in rest) + "</ul>")
        del data["sections"][boxed]; data["order"].remove(boxed)
        notes.append(f"What's in the Box section moved into dropdowns ({len(items)} items, {sum(1 for i in items if photos.get(i))} with a photo, {len(rest)} spec rows)")

    has_box = bool(box) or BOX in blocks
    ids = [BENEFITS, INGREDIENTS, HOWTO] + ([BOX] if has_box else []) + ([SPECS] if specs or SPECS in blocks else []) + [GUARANTEE]
    if specs: wanted[SPECS] = specs
    elif SPECS in blocks: wanted[SPECS] = blocks[SPECS]["settings"]
    before = json.dumps([(b, blocks.get(b)) for b in ids]) + json.dumps(order)
    for bid in ids:
        if bid == BOX: blocks[bid] = {"type": "lp_box", "settings": box or blocks[bid]["settings"]}
        else: blocks[bid] = {"type": "collapsible_text", "settings": wanted[bid]}
        if bid in order: order.remove(bid)
    at = after_buy_buttons(main)
    order[at:at] = ids
    if json.dumps([(b, blocks.get(b)) for b in ids]) + json.dumps(order) != before: notes.append("dropdowns on: " + ", ".join(blocks[b]["settings"]["title"] for b in ids))
    assert set(order) == set(blocks) and len(order) == len(set(order))
    return notes


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--root", default=str(REPO)); parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(); changed = 0
    for path in sorted(glob.glob(os.path.join(args.root, "templates", "product*.json"))):
        raw = open(path, encoding="utf-8").read(); start = raw.index("{"); data = json.loads(raw[start:])
        notes = convert(data, os.path.basename(path)[:-5]); out = raw[:start] + json.dumps(data, indent=2, ensure_ascii=False) + "\n"
        if out == raw: continue
        changed += 1; print(os.path.basename(path) + ": " + "; ".join(notes))
        if args.apply: open(path, "w", encoding="utf-8").write(out)
    print(f"{changed} template(s) {'changed' if args.apply else 'would change (dry run, add --apply)'}")


if __name__ == "__main__":
    main()
