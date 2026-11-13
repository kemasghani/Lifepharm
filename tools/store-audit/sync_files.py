#!/usr/bin/env python3
"""Copy the Files (images and videos) a checkout references from the source store to a store that lacks them.

  python3 tools/store-audit/sync_files.py --to us            # dry run: list what would be copied
  python3 tools/store-audit/sync_files.py --to us --apply    # copy them

Additive only: it never deletes or replaces a file, and keeps the filename so `shopify://shop_images/<name>` resolves.
"""
import argparse, json, os, sys, time, urllib.request, uuid
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shopify import CONFIG, REPO, STORE_KEYS, gql
from refs import collect
from audit import compare, store_inventory

FIND = "query($q:String){ files(first:10, query:$q){ nodes{ __typename alt ... on MediaImage{ image{ url } mimeType } ... on Video{ filename originalSource{ url mimeType } } } } }"
STAGE = "mutation($input:[StagedUploadInput!]!){ stagedUploadsCreate(input:$input){ stagedTargets{ url resourceUrl parameters{ name value } } userErrors{ field message } } }"
CREATE = "mutation($files:[FileCreateInput!]!){ fileCreate(files:$files){ files{ id fileStatus } userErrors{ field message } } }"
STATUS = "query($id:ID!){ node(id:$id){ ... on File{ fileStatus } } }"
MIME = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".webp": "image/webp", ".gif": "image/gif", ".svg": "image/svg+xml", ".mp4": "video/mp4", ".mov": "video/quicktime"}


def source_file(store, kind, name):
    nodes = gql(store, FIND, {"q": f'filename:"{name}"'})["data"]["files"]["nodes"]
    for node in nodes:
        if kind == "image" and node["__typename"] == "MediaImage" and node.get("image"):
            if node["image"]["url"].split("?")[0].rsplit("/", 1)[-1].lower() == name.lower():
                return node["image"]["url"], node.get("alt") or ""
        if kind == "video" and node["__typename"] == "Video" and node.get("filename") == name:
            return node["originalSource"]["url"], node.get("alt") or ""
    return None, None


def upload(store, kind, name, data, alt):
    mime = MIME.get(os.path.splitext(name)[1].lower(), "application/octet-stream")
    staged = gql(store, STAGE, {"input": [{"filename": name, "mimeType": mime, "httpMethod": "POST", "resource": "VIDEO" if kind == "video" else "FILE", "fileSize": str(len(data))}]})["data"]["stagedUploadsCreate"]
    if staged["userErrors"]:
        return f"stage failed: {staged['userErrors']}"
    target = staged["stagedTargets"][0]
    boundary = uuid.uuid4().hex
    body = b"".join(f'--{boundary}\r\nContent-Disposition: form-data; name="{p["name"]}"\r\n\r\n{p["value"]}\r\n'.encode() for p in target["parameters"])
    body += f'--{boundary}\r\nContent-Disposition: form-data; name="file"; filename="{name}"\r\nContent-Type: {mime}\r\n\r\n'.encode() + data + f"\r\n--{boundary}--\r\n".encode()
    urllib.request.urlopen(urllib.request.Request(target["url"], body, {"Content-Type": f"multipart/form-data; boundary={boundary}"}), timeout=300)
    created = gql(store, CREATE, {"files": [{"originalSource": target["resourceUrl"], "contentType": "VIDEO" if kind == "video" else "IMAGE", "alt": alt, "filename": name}]})["data"]["fileCreate"]
    if created["userErrors"]:
        return f"create failed: {created['userErrors']}"
    file_id = created["files"][0]["id"]
    for _ in range(60):
        status = gql(store, STATUS, {"id": file_id})["data"]["node"]["fileStatus"]
        if status in ("READY", "FAILED"):
            return status
        time.sleep(3)
    return "PROCESSING"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--to", required=True, choices=STORE_KEYS)
    parser.add_argument("--from", dest="source", default=CONFIG["source_of_truth"], choices=STORE_KEYS)
    parser.add_argument("--root", default=str(REPO))
    parser.add_argument("--include-disabled", action="store_true", help="also copy files only used by disabled sections")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    report = compare(collect(args.root), store_inventory(args.to, refresh=True))
    todo = []
    for kind in ("image", "video"):
        names = report[kind]["missing"] if args.include_disabled else report[kind]["missing_active"]
        todo += [(kind, name) for name in sorted(names)]
    print(f"{len(todo)} file(s) referenced by this checkout are missing in {args.to}")
    failures = 0
    for kind, name in todo:
        url, alt = source_file(args.source, kind, name)
        if not url:
            print(f"  SKIP   {name}  (not found in {args.source} either)")
            failures += 1
            continue
        if not args.apply:
            print(f"  would copy {kind:<5} {name}")
            continue
        data = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "store-audit"}), timeout=300).read()
        result = upload(args.to, kind, name, data, alt)
        print(f"  {result:<10} {name}  ({len(data) // 1024} KB)")
        failures += result != "READY"
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
