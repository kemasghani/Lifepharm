#!/usr/bin/env python3
"""LifePharm theme guard: the checks Shopify does not run for you.

Each check here exists because the failure already happened on this project
(see docs/LESSONS.md). Shopify's GitHub sync rejects a bad JSON file silently
and `shopify theme check` does not catch these, so we check before pushing.

Usage: python3 tools/harness/check_theme.py [--root PATH]
Exit code 1 if any FAIL, 0 otherwise (WARN does not fail).
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import subprocess
import sys

FAILS: list[str] = []
WARNS: list[str] = []


def fail(msg: str) -> None:
    FAILS.append(msg)


def warn(msg: str) -> None:
    WARNS.append(msg)


def load_json(path: str):
    """Shopify JSON may start with an auto-generated /* ... */ header."""
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    text = re.sub(r"^\s*/\*.*?\*/", "", text, count=1, flags=re.S)
    return json.loads(text)


SCHEMA_RE = re.compile(r"{%-?\s*schema\s*-?%}(.*?){%-?\s*endschema\s*-?%}", re.S)


def load_schema(path: str):
    try:
        with open(path, encoding="utf-8") as fh:
            m = SCHEMA_RE.search(fh.read())
        return json.loads(m.group(1)) if m else None
    except (OSError, json.JSONDecodeError):
        return None


def settings_index(settings_list):
    return {s["id"]: s for s in settings_list or [] if isinstance(s, dict) and "id" in s}


def check_value(where: str, sid: str, value, spec: dict) -> None:
    t = spec.get("type")
    if isinstance(value, str) and value.strip().startswith("{{"):
        return  # dynamic source, resolved at render time
    if t == "range":
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            fail(f"{where}: '{sid}' = {value!r} is not a number (range)")
            return
        lo, hi = spec.get("min"), spec.get("max")
        if lo is not None and value < lo or hi is not None and value > hi:
            fail(f"{where}: '{sid}' = {value} outside range {lo}..{hi} (Shopify rejects the whole file)")
            return
        step = spec.get("step")
        if step and lo is not None:
            q = (value - lo) / step
            if abs(q - round(q)) > 1e-6:
                warn(f"{where}: '{sid}' = {value} not on step {step} from {lo}")
    elif t in ("select", "radio"):
        allowed = [o.get("value") for o in spec.get("options", [])]
        if allowed and value not in allowed:
            fail(f"{where}: '{sid}' = {value!r} not one of {allowed}")
    elif t == "checkbox":
        if not isinstance(value, bool):
            fail(f"{where}: '{sid}' = {value!r} is not true/false (checkbox)")


def check_settings(where: str, values: dict, specs: dict) -> None:
    for sid, value in (values or {}).items():
        spec = specs.get(sid)
        if spec:
            check_value(where, sid, value, spec)


def check_template_like(path: str, data: dict, section_schemas: dict, block_schemas: dict) -> None:
    sections = data.get("sections", {}) or {}
    n = len(sections)
    if n > 25:
        fail(f"{path}: {n} sections (max 25, Shopify rejects the file silently)")
    elif n >= 24:
        warn(f"{path}: {n} of 25 sections used")
    for key, sec in sections.items():
        stype = sec.get("type", "")
        if stype.startswith("shopify://") or stype.startswith("_"):
            continue
        schema = section_schemas.get(stype)
        if schema is None:
            if not os.path.exists(os.path.join(ROOT, "sections", f"{stype}.liquid")):
                fail(f"{path}: section '{key}' uses missing section type '{stype}'")
            continue
        check_settings(f"{path} [{key}]", sec.get("settings"), settings_index(schema.get("settings")))
        local_blocks = {b.get("type"): b for b in schema.get("blocks", []) if isinstance(b, dict)}
        check_blocks(f"{path} [{key}]", sec.get("blocks"), local_blocks, block_schemas)


def check_blocks(where: str, blocks: dict, local_blocks: dict, block_schemas: dict) -> None:
    for bkey, blk in (blocks or {}).items():
        btype = blk.get("type", "")
        if btype.startswith("shopify://") or btype.startswith("@"):
            continue
        spec = local_blocks.get(btype) or block_schemas.get(btype)
        if spec is not None:
            check_settings(f"{where} block '{bkey}'", blk.get("settings"), settings_index(spec.get("settings")))
            nested_local = {b.get("type"): b for b in spec.get("blocks", []) if isinstance(b, dict)}
            check_blocks(f"{where} block '{bkey}'", blk.get("blocks"), nested_local, block_schemas)


def check_json_and_schemas() -> None:
    section_schemas = {}
    for p in glob.glob(os.path.join(ROOT, "sections", "*.liquid")):
        s = load_schema(p)
        if s is not None:
            section_schemas[os.path.splitext(os.path.basename(p))[0]] = s
    block_schemas = {}
    for p in glob.glob(os.path.join(ROOT, "blocks", "*.liquid")):
        s = load_schema(p)
        if s is not None:
            block_schemas[os.path.splitext(os.path.basename(p))[0]] = s

    json_files = (
        glob.glob(os.path.join(ROOT, "templates", "**", "*.json"), recursive=True)
        + glob.glob(os.path.join(ROOT, "sections", "*.json"))
        + glob.glob(os.path.join(ROOT, "config", "*.json"))
        + glob.glob(os.path.join(ROOT, "locales", "*.json"))
    )
    parsed = 0
    for p in sorted(json_files):
        rel = os.path.relpath(p, ROOT)
        try:
            data = load_json(p)
        except json.JSONDecodeError as e:
            fail(f"{rel}: invalid JSON ({e})")
            continue
        parsed += 1
        if rel.startswith("templates/") or (rel.startswith("sections/") and rel.endswith("-group.json")):
            check_template_like(rel, data, section_schemas, block_schemas)
    print(f"  parsed {parsed} JSON files, {len(section_schemas)} section schemas")

    # settings_data "current" against settings_schema
    try:
        schema = load_json(os.path.join(ROOT, "config", "settings_schema.json"))
        sdata = load_json(os.path.join(ROOT, "config", "settings_data.json"))
        specs = {}
        for group in schema:
            specs.update(settings_index(group.get("settings")))
        current = sdata.get("current")
        if isinstance(current, dict):
            check_settings("config/settings_data.json current", current, specs)
    except (OSError, json.JSONDecodeError) as e:
        fail(f"settings_data/settings_schema unreadable: {e}")


def check_copy_and_brand() -> None:
    # Em dashes: CLAUDE.md section 3. Only our own lp-* code and template text.
    own = glob.glob(os.path.join(ROOT, "sections", "lp-*.liquid")) + glob.glob(
        os.path.join(ROOT, "snippets", "lp-*.liquid")
    )
    hits = []
    for p in own:
        with open(p, encoding="utf-8") as fh:
            for i, line in enumerate(fh, 1):
                if "—" in line and "{%" not in line[: line.find("—")][-3:]:
                    hits.append(f"{os.path.relpath(p, ROOT)}:{i}")
    if hits:
        warn(f"em dash in lp-* code ({len(hits)}): {', '.join(hits[:5])}{' ...' if len(hits) > 5 else ''}")

    # --lp-amber-deep must not colour text or icons (Letisha 2026-11-17)
    deep = []
    pat = re.compile(r"(?<![-\w])(color|fill|stroke)\s*:\s*var\(--lp-amber-deep")
    for p in glob.glob(os.path.join(ROOT, "assets", "lp-*.css")) + own:
        with open(p, encoding="utf-8") as fh:
            for i, line in enumerate(fh, 1):
                if pat.search(line):
                    deep.append(f"{os.path.relpath(p, ROOT)}:{i}")
    if deep:
        warn(f"--lp-amber-deep used as text/icon colour ({len(deep)}): {', '.join(deep[:5])}")


SECRET_PATTERNS = [
    (re.compile(r"shp(at|ss|ca|pa)_[0-9a-fA-F]{32}"), "Shopify token"),
    (re.compile(r"\bpk_[0-9a-f]{34}\b"), "Klaviyo private key"),
    (re.compile(r"-----BEGIN (RSA |OPENSSH |EC )?PRIVATE KEY-----"), "private key"),
    (re.compile(r"(?i)(EXIGO_PASSWORD|EXIGO_REPORTING_PWD|CLIENT_SECRET|BOT_TOKEN)\s*=\s*\S{6,}"), "credential assignment"),
    (re.compile(r"\b\d{8,10}:AA[0-9A-Za-z_-]{30,}\b"), "Telegram bot token"),
]


def check_secrets() -> None:
    """The GitHub repo is PUBLIC. Nothing secret may be tracked or staged."""
    try:
        tracked = subprocess.run(
            ["git", "-C", ROOT, "ls-files", "--cached", "--others", "--exclude-standard"],
            capture_output=True, text=True, check=True,
        ).stdout.split("\n")
    except (OSError, subprocess.CalledProcessError):
        warn("git not available, secret scan skipped")
        return
    if ".env" in tracked:
        fail(".env is tracked or unignored (repo is public)")
    scanned = 0
    for rel in tracked:
        if not rel or rel.startswith("docs/exigo-api/") or rel.endswith(
            (".png", ".jpg", ".jpeg", ".webp", ".gif", ".mp4", ".mov", ".woff2", ".woff", ".pdf", ".svg", ".ico")
        ):
            continue
        p = os.path.join(ROOT, rel)
        try:
            if os.path.getsize(p) > 2_000_000:
                continue
            with open(p, encoding="utf-8", errors="ignore") as fh:
                text = fh.read()
        except OSError:
            continue
        scanned += 1
        for pat, label in SECRET_PATTERNS:
            if pat.search(text):
                fail(f"{rel}: looks like a {label} (public repo)")
    print(f"  secret scan: {scanned} files")


def main() -> int:
    global ROOT
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
    ROOT = ap.parse_args().root
    print("theme guard")
    check_json_and_schemas()
    check_copy_and_brand()
    check_secrets()
    for w in WARNS:
        print(f"  WARN  {w}")
    for f in FAILS:
        print(f"  FAIL  {f}")
    print(f"  result: {len(FAILS)} fail, {len(WARNS)} warn")
    return 1 if FAILS else 0


ROOT = "."
if __name__ == "__main__":
    sys.exit(main())
