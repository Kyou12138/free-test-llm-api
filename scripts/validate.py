#!/usr/bin/env python3
"""Validate data/providers.yaml against schema and project rules."""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Missing dependency: PyYAML. Install with: pip install pyyaml jsonschema", file=sys.stderr)
    sys.exit(1)

try:
    from jsonschema import Draft202012Validator
except ImportError:
    print("Missing dependency: jsonschema. Install with: pip install pyyaml jsonschema", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "providers.yaml"
SCHEMA = ROOT / "schema" / "provider.schema.json"

URL_RE = re.compile(r"^https?://", re.I)
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def load_yaml(path: Path):
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_schema(path: Path):
    import json

    with path.open(encoding="utf-8") as f:
        return json.load(f)


def main() -> int:
    if not DATA.exists():
        print(f"ERROR: missing {DATA}", file=sys.stderr)
        return 1
    if not SCHEMA.exists():
        print(f"ERROR: missing {SCHEMA}", file=sys.stderr)
        return 1

    doc = load_yaml(DATA)
    schema = load_schema(SCHEMA)
    errors: list[str] = []

    if not isinstance(doc, dict) or "providers" not in doc:
        print("ERROR: providers.yaml must contain a top-level 'providers' list", file=sys.stderr)
        return 1

    providers = doc["providers"]
    if not isinstance(providers, list) or not providers:
        print("ERROR: providers list is empty", file=sys.stderr)
        return 1

    validator = Draft202012Validator(schema)
    seen_ids: set[str] = set()

    for i, p in enumerate(providers):
        prefix = f"providers[{i}]"
        if not isinstance(p, dict):
            errors.append(f"{prefix}: must be an object")
            continue

        for err in sorted(validator.iter_errors(p), key=lambda e: list(e.path)):
            loc = ".".join(str(x) for x in err.path) or "(root)"
            errors.append(f"{prefix}.{loc}: {err.message}")

        pid = p.get("id")
        if pid in seen_ids:
            errors.append(f"{prefix}.id: duplicate id '{pid}'")
        seen_ids.add(pid)

        ft = p.get("free_tier") or {}
        if ft.get("permanent") is not True:
            errors.append(f"{prefix}.free_tier.permanent: must be true (trial-only credits are out of scope)")

        for key in ("website", "docs", "api_key_url"):
            url = p.get(key, "")
            if url and not URL_RE.match(str(url)):
                errors.append(f"{prefix}.{key}: must be http(s) URL")

        base = p.get("base_url")
        if base is not None and base != "" and not URL_RE.match(str(base)):
            errors.append(f"{prefix}.base_url: must be http(s) URL or null")

        lv = p.get("last_verified", "")
        if lv and not DATE_RE.match(str(lv)):
            errors.append(f"{prefix}.last_verified: expected YYYY-MM-DD")

    if errors:
        print(f"Validation FAILED ({len(errors)} error(s)):\n", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    vendors = sum(1 for p in providers if p.get("type") == "model_vendor")
    platforms = sum(1 for p in providers if p.get("type") == "inference_platform")
    print(f"OK: {len(providers)} providers ({vendors} model_vendor, {platforms} inference_platform)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
