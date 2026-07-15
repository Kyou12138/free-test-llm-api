#!/usr/bin/env python3
"""Validate data/endpoints.yaml against schema and project rules."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Missing dependency: PyYAML. pip install -r requirements.txt", file=sys.stderr)
    sys.exit(1)

try:
    from jsonschema import Draft202012Validator
except ImportError:
    print("Missing dependency: jsonschema. pip install -r requirements.txt", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "endpoints.yaml"
SCHEMA = ROOT / "schema" / "endpoint.schema.json"
URL_RE = re.compile(r"^https?://", re.I)
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
CATEGORIES = {"project_demo", "anonymous_public", "free_token"}


def main() -> int:
    if not DATA.exists():
        print(f"ERROR: missing {DATA}", file=sys.stderr)
        return 1

    with DATA.open(encoding="utf-8") as f:
        doc = yaml.safe_load(f)
    with SCHEMA.open(encoding="utf-8") as f:
        schema = json.load(f)

    if not isinstance(doc, dict) or "endpoints" not in doc:
        print("ERROR: endpoints.yaml must contain top-level 'endpoints' list", file=sys.stderr)
        return 1

    endpoints = doc["endpoints"]
    if not isinstance(endpoints, list) or not endpoints:
        print("ERROR: endpoints list is empty", file=sys.stderr)
        return 1

    validator = Draft202012Validator(schema)
    errors: list[str] = []
    seen: set[str] = set()

    for i, ep in enumerate(endpoints):
        prefix = f"endpoints[{i}]"
        if not isinstance(ep, dict):
            errors.append(f"{prefix}: must be object")
            continue

        for err in sorted(validator.iter_errors(ep), key=lambda e: list(e.path)):
            loc = ".".join(str(x) for x in err.path) or "(root)"
            errors.append(f"{prefix}.{loc}: {err.message}")

        eid = ep.get("id")
        if eid in seen:
            errors.append(f"{prefix}.id: duplicate '{eid}'")
        seen.add(eid)

        if ep.get("category") not in CATEGORIES:
            errors.append(f"{prefix}.category: must be one of {sorted(CATEGORIES)}")

        for key in ("base_url", "source_docs"):
            val = ep.get(key, "")
            if val and not URL_RE.match(str(val)):
                errors.append(f"{prefix}.{key}: must be http(s) URL")

        env = ep.get("env") or {}
        if "LLM_BASE_URL" not in env or "LLM_MODEL_NAME" not in env:
            errors.append(f"{prefix}.env: requires LLM_BASE_URL and LLM_MODEL_NAME")

        if ep.get("api_key_required") and not ep.get("api_key_url") and "LLM_API_KEY" not in env:
            errors.append(f"{prefix}: api_key_required true needs api_key_url or env.LLM_API_KEY hint")

        lv = ep.get("last_verified", "")
        if lv and not DATE_RE.match(str(lv)):
            errors.append(f"{prefix}.last_verified: expected YYYY-MM-DD")

    if errors:
        print(f"Validation FAILED ({len(errors)} error(s)):\n", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    by_cat: dict[str, int] = {}
    for ep in endpoints:
        by_cat[ep["category"]] = by_cat.get(ep["category"], 0) + 1
    summary = ", ".join(f"{k}={v}" for k, v in sorted(by_cat.items()))
    print(f"OK: {len(endpoints)} endpoints ({summary})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
