"""Collect every store-owned resource a theme checkout points at: files, products, collections, pages, blogs, menus, app blocks, product metafields."""
import collections, glob, json, os, re

DATA_GLOBS = ("templates/**/*.json", "sections/*.json")
URI = re.compile(r"shopify://([a-z_]+)/([^\"'<>)\\]+)")
PATH = re.compile(r"(?:href=\\?[\"']|^)/(pages|collections|products|blogs)/([a-z0-9][a-z0-9\-_]*)")
URI_KIND = {"products": "product", "collections": "collection", "pages": "page", "blogs": "blog", "articles": "article", "policies": "policy"}
PATH_KIND = {"pages": "page", "collections": "collection", "products": "product", "blogs": "blog"}
HANDLE_TYPES = {"product": "product", "collection": "collection", "page": "page", "blog": "blog", "link_list": "menu"}


def load_json(path):
    """Shopify writes a comment header on generated JSON; drop it before parsing."""
    return json.loads(re.sub(r"^\s*/\*.*?\*/", "", open(path).read(), flags=re.S))


def section_schema(root, section_type):
    path = os.path.join(root, "sections", section_type + ".liquid")
    if not os.path.exists(path):
        return {}
    match = re.search(r"{%-?\s*schema\s*-?%}(.*?){%-?\s*endschema\s*-?%}", open(path).read(), flags=re.S)
    try:
        return json.loads(match.group(1)) if match else {}
    except ValueError:
        return {}


def data_files(root):
    files = []
    for pattern in DATA_GLOBS:
        files += glob.glob(os.path.join(root, pattern), recursive=True)
    return sorted(files) + [os.path.join(root, "config", "settings_data.json")]


def collect(root):
    """Return {kind: {value: [where, ...]}}. `where` ends in "(disabled)" when the section is switched off."""
    refs = collections.defaultdict(lambda: collections.defaultdict(set))

    def add(kind, value, where):
        if value:
            refs[kind][value].add(where)

    def scan_value(value, setting_type, where):
        if isinstance(value, list):
            for item in value:
                scan_value(item, setting_type, where)
            return
        if not isinstance(value, str):
            return
        if setting_type in HANDLE_TYPES:
            add(HANDLE_TYPES[setting_type], value.rsplit("/", 1)[-1], where)
            return
        if setting_type in ("product_list", "collection_list"):
            add(setting_type.split("_")[0], value.rsplit("/", 1)[-1], where)
            return
        for match in URI.finditer(value):
            kind, rest = match.group(1), match.group(2).strip()
            if kind == "shop_images":
                add("image", rest, where)
            elif kind == "files":
                add("video" if rest.startswith("videos/") else "file", rest.split("/", 1)[-1], where)
            elif kind == "apps":
                add("app", rest.split("/")[0], where)
            elif kind in URI_KIND:
                add(URI_KIND[kind], rest.split("/")[0] if kind != "articles" else rest, where)
        for match in PATH.finditer(value):
            add(PATH_KIND[match.group(1)], match.group(2), where)

    def scan_settings(settings, definitions, where):
        types = {d["id"]: d["type"] for d in (definitions or []) if "id" in d}
        for key, value in (settings or {}).items():
            scan_value(value, types.get(key), f"{where}.{key}")

    for path in data_files(root):
        name = os.path.relpath(path, root)
        try:
            doc = load_json(path)
        except ValueError as error:
            add("invalid_json", name, str(error)[:80])
            continue
        if name.endswith("settings_data.json"):
            current = doc.get("current")
            if not isinstance(current, dict):
                continue
            schema = load_json(os.path.join(root, "config", "settings_schema.json"))
            definitions = [s for group in schema for s in group.get("settings", [])]
            scan_settings({k: v for k, v in current.items() if k not in ("sections", "blocks", "content_for_index")}, definitions, name)
            for block in (current.get("blocks") or {}).values():
                block_type = block.get("type", "")
                if block_type.startswith("shopify://apps/") and not block.get("disabled"):
                    add("app", block_type.split("/")[3], name + "#app-embed")
            continue
        for section_id, section in (doc.get("sections") or {}).items():
            schema = section_schema(root, section.get("type", ""))
            where = f"{name}#{section_id}" + ("(disabled)" if section.get("disabled") else "")
            scan_settings(section.get("settings"), schema.get("settings"), where)
            block_settings = {b["type"]: b.get("settings") for b in schema.get("blocks", []) if "type" in b}
            for block_id, block in (section.get("blocks") or {}).items():
                block_type = block.get("type", "")
                if block_type.startswith("shopify://apps/"):
                    add("app", block_type.split("/")[3], where)
                scan_settings(block.get("settings"), block_settings.get(block_type), f"{where}/{block_id}")

    result = {kind: {value: sorted(where) for value, where in values.items()} for kind, values in refs.items()}
    result["metafield"] = product_metafields(root)
    return result


def product_metafields(root):
    """Product metafields the Liquid reads, so a store missing a definition shows up before launch."""
    keys = collections.defaultdict(set)
    for path in glob.glob(os.path.join(root, "sections", "*.liquid")) + glob.glob(os.path.join(root, "snippets", "*.liquid")):
        text, name = open(path).read(), os.path.basename(path)
        for match in re.finditer(r"product\.metafields\.([a-z_]+)\.([a-z0-9_]+)", text):
            keys[f"product.{match.group(1)}.{match.group(2)}"].add(name)
        if re.search(r"assign mf = product\.metafields\.custom", text):
            for match in re.finditer(r"\bmf\.([a-z0-9_]+)", text):
                keys[f"product.custom.{match.group(1)}"].add(name)
    return {key: sorted(where) for key, where in keys.items()}
