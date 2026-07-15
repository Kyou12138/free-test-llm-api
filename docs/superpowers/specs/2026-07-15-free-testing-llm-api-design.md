# Free Testing LLM API Catalog — Design (v2)

**Date:** 2026-07-15  
**Status:** Active (replaces permanent free-tier catalog design)  
**Repo:** free-test-llm-api

## Problem

Previous catalog listed “permanent free tiers” (Groq, Gemini free tier, etc.).  
User intent is different: **Page Agent-style Free Testing APIs** — endpoints published for technical evaluation / demo, documented as copy-paste:

```bash
LLM_BASE_URL="https://..."
LLM_MODEL_NAME="..."
```

Reference: https://alibaba.github.io/page-agent/docs/features/models/#free-testing-api

## Goal

Maintain a bilingual, machine-readable catalog of free **testing** LLM HTTP endpoints.

## Categories

1. `project_demo` — OSS project official testing proxies (e.g. page-agent Qwen FC proxy)
2. `anonymous_public` — no key public free APIs (e.g. OVH anonymous)
3. `free_token` — free key/token OpenAI-compatible bases for rapid testing

## Out of scope

- Unofficial reverse proxies / key sharing
- Production SLA
- Live quota scraping (v1)

## Data model

SSOT: `data/endpoints.yaml`  
Schema: `schema/endpoint.schema.json`  
Each entry **must** include `env.LLM_BASE_URL` + `env.LLM_MODEL_NAME`.

## Tooling

- `scripts/validate.py`
- `scripts/generate_readme.py` → `README.md` + `README.en.md`
