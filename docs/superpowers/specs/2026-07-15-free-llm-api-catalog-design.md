# Free LLM API Catalog — Design Spec (superseded)

**Date:** 2026-07-15  
**Status:** Superseded by free-testing-llm-api design  
**Repo:** free-test-llm-api

## Goal

Publish a maintainable GitHub catalog of **official + mainstream inference-platform** LLM APIs that offer a **permanent free tier**. Structured YAML is the single source of truth; bilingual READMEs are generated.

## Inclusion criteria

**In:**
- Model vendor official APIs with permanent free tiers
- Mainstream inference platforms with permanent free tiers and public docs
- Clear website / docs / API key entry points

**Out:**
- One-shot trial credits only (e.g. “$5 for 30 days” with no ongoing free tier)
- Unofficial reverse-engineered chatbot proxies / key sharing
- Chat UIs without an API

## Non-goals (v1)

- Live quota scraping
- Proxy / gateway service
- Full static website (may come later)

## Repository layout

```
data/providers.yaml          # SSOT
schema/provider.schema.json  # validation
scripts/generate_readme.py   # YAML → README.md + README.en.md
scripts/validate.py          # schema + required fields
README.md / README.en.md     # generated
CONTRIBUTING.md
LICENSE
.github/workflows/ci.yml
```

## Provider fields

See `schema/provider.schema.json`. Core fields: `id`, `name`, `name_zh`, `type`, `region`, URLs, `openai_compatible`, `base_url`, `credit_card_required`, `free_tier`, `models_sample`, `last_verified`, `status`.

## Differentiation

1. Permanent free only (no mixed trial lists)
2. Machine-readable YAML + JSON Schema
3. Chinese + English READMEs
4. `last_verified` + CI validation

## License

MIT
