"""Read-only inventory of what a store's admin holds."""
import re
from shopify import gql, paged

QUERIES = {
    "product": ("query($after:String){ products(first:250, after:$after){ pageInfo{hasNextPage endCursor} nodes{ handle } } }", ["products"]),
    "collection": ("query($after:String){ collections(first:250, after:$after){ pageInfo{hasNextPage endCursor} nodes{ handle } } }", ["collections"]),
    "page": ("query($after:String){ pages(first:250, after:$after){ pageInfo{hasNextPage endCursor} nodes{ handle } } }", ["pages"]),
    "blog": ("query($after:String){ blogs(first:100, after:$after){ pageInfo{hasNextPage endCursor} nodes{ handle } } }", ["blogs"]),
    "menu": ("query($after:String){ menus(first:100, after:$after){ pageInfo{hasNextPage endCursor} nodes{ handle } } }", ["menus"]),
}
FILES = "query($after:String){ files(first:250, after:$after){ pageInfo{hasNextPage endCursor} nodes{ __typename ... on MediaImage{ image{ url } } ... on Video{ filename } ... on GenericFile{ url } } } }"
METAFIELDS = "query($after:String){ metafieldDefinitions(first:250, after:$after, ownerType: PRODUCT){ pageInfo{hasNextPage endCursor} nodes{ namespace key } } }"
THEMES = "{ themes(first: 50) { nodes { id role } } }"
THEME_JSON = 'query($id:ID!,$after:String){ theme(id:$id){ files(first:250, after:$after, filenames:["templates/*.json","sections/*.json","config/settings_data.json"]){ pageInfo{hasNextPage endCursor} nodes{ body{ ... on OnlineStoreThemeFileBodyText{ content } } } } } }'


def basename(url):
    return url.split("?")[0].rsplit("/", 1)[-1] if url else None


def installed_apps(store):
    """The app list is not readable with this app's scopes, so use the apps the live theme already renders as evidence."""
    themes = gql(store, THEMES)
    if themes.get("errors"):
        return [], str(themes["errors"])[:200]
    live = [t["id"] for t in themes["data"]["themes"]["nodes"] if t["role"] == "MAIN"]
    if not live:
        return [], "no live theme"
    nodes, error = paged(store, THEME_JSON, ["theme", "files"], {"id": live[0]})
    apps = set()
    for node in nodes:
        apps.update(re.findall(r"shopify:\\?/\\?/apps\\?/([a-z0-9\-_]+)\\?/blocks", (node.get("body") or {}).get("content") or ""))
    return sorted(apps), error


def inventory(store):
    result, errors = {}, {}
    files, error = paged(store, FILES, ["files"])
    if error:
        errors["files"] = error
    result["image"] = sorted({basename(f["image"]["url"]) for f in files if f["__typename"] == "MediaImage" and f.get("image")})
    result["video"] = sorted({f["filename"] for f in files if f["__typename"] == "Video" and f.get("filename")})
    result["file"] = sorted({basename(f["url"]) for f in files if f["__typename"] == "GenericFile" and f.get("url")})
    for kind, (query, path) in QUERIES.items():
        nodes, error = paged(store, query, path)
        if error:
            errors[kind] = error
        result[kind] = sorted({n["handle"] for n in nodes})
    result["collection"] = sorted(set(result["collection"]) | {"all"})
    definitions, error = paged(store, METAFIELDS, ["metafieldDefinitions"])
    if error:
        errors["metafield"] = error
    result["metafield"] = sorted({f"product.{d['namespace']}.{d['key']}" for d in definitions})
    result["app"], error = installed_apps(store)
    if error:
        errors["app"] = error
    result["errors"] = errors
    return result
