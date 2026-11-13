"""Minimal Admin API client for the LifePharm stores. Reads secrets from the repo's .env and never prints them."""
import json, pathlib, time, urllib.error, urllib.parse, urllib.request

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
API_VERSION = "2026-04"
CONFIG = json.loads((HERE / "stores.json").read_text())
STORE_KEYS = list(CONFIG["stores"])


def _env():
    env = {}
    for line in (REPO / ".env").read_text().splitlines():
        if "=" in line and not line.strip().startswith("#"):
            key, value = line.split("=", 1)
            env[key.strip()] = value.strip().strip("\"'")
    return env


ENV = _env()
_tokens = {}


def domain(store):
    value = ENV[CONFIG["stores"][store]["domain_env"]].replace("https://", "").replace("http://", "").strip("/")
    return value if "." in value else value + ".myshopify.com"


def token(store):
    """Client-credentials token for the LifePharm custom app installed on each store."""
    if store not in _tokens:
        body = urllib.parse.urlencode({
            "grant_type": "client_credentials",
            "client_id": ENV["SHOPIFY-APP-CLIENT-ID"],
            "client_secret": ENV["SHOPIFY-APP-CLIENT-SECRET"],
        }).encode()
        request = urllib.request.Request(f"https://{domain(store)}/admin/oauth/access_token", body)
        _tokens[store] = json.load(urllib.request.urlopen(request, timeout=30))["access_token"]
    return _tokens[store]


def gql(store, query, variables=None):
    request = urllib.request.Request(
        f"https://{domain(store)}/admin/api/{API_VERSION}/graphql.json",
        json.dumps({"query": query, "variables": variables or {}}).encode(),
        {"Content-Type": "application/json", "X-Shopify-Access-Token": token(store)},
    )
    for attempt in range(4):
        try:
            return json.load(urllib.request.urlopen(request, timeout=90))
        except urllib.error.HTTPError as error:
            if error.code not in (429, 502, 503, 504) or attempt == 3:
                return {"errors": f"HTTP {error.code}"}
        except (urllib.error.URLError, TimeoutError) as error:
            if attempt == 3:
                return {"errors": f"network: {error}"}
        time.sleep(2 * (attempt + 1))


def paged(store, query, path, variables=None):
    """Follow a connection to the end. `path` is the key path to the connection inside `data`."""
    nodes, after = [], None
    while True:
        response = gql(store, query, {**(variables or {}), "after": after})
        if response.get("errors"):
            return nodes, str(response["errors"])[:200]
        connection = response["data"]
        for key in path:
            connection = connection[key]
        nodes += connection["nodes"]
        if not connection["pageInfo"]["hasNextPage"]:
            return nodes, None
        after = connection["pageInfo"]["endCursor"]
