# free-test-llm-api

> Catalog of **copy-paste** free testing LLM APIs: `LLM_BASE_URL` + `LLM_MODEL_NAME`
>
> Inspired by [Page Agent · Free Testing API](https://alibaba.github.io/page-agent/docs/features/models/#free-testing-api)

[中文](./README.md) · Source: [`data/endpoints.yaml`](./data/endpoints.yaml) · Updated: `2026-07-15`

## What this is / is not

| ✅ We include | ❌ We exclude |
| --- | --- |
| Official **project demo testing APIs** | Unofficial reverse proxies / shared keys |
| **No-signup** public free endpoints | Chat UIs without an HTTP API |
| Zero-cost keys with **OpenAI-compatible** bases | Marketing fluff without a clear test entry |
| Every entry has **copy-paste env** | Production SLA guarantees |

**Focus**: Copy-paste free testing LLM endpoints (BASE_URL + MODEL), not permanent free-tier signup catalogs.

**Disclaimer**: Most endpoints are for technical evaluation only; may be rate-limited or removed anytime. Not for production or sensitive data. Follow each project's terms.

## Overview (11)

| Name | Category | Region | Needs key | OpenAI-compatible | Status | Docs |
| --- | --- | --- | --- | --- | --- | --- |
| [Page Agent Free Testing API (Qwen)](https://alibaba.github.io/page-agent/docs/features/models/#free-testing-api) | `project_demo` | CN | No | Yes | ✅ active | [docs](https://alibaba.github.io/page-agent/docs/features/models/#free-testing-api) |
| [OVHcloud AI Endpoints (Anonymous Free)](https://www.ovhcloud.com/en/public-cloud/ai-endpoints/catalog/) | `anonymous` | EU | No | Yes | ✅ active | [docs](https://www.ovhcloud.com/en/public-cloud/ai-endpoints/catalog/) |
| [Cerebras Inference Free](https://inference-docs.cerebras.ai/) | `free_token` | US | Yes | Yes | ✅ active | [docs](https://inference-docs.cerebras.ai/) |
| [GitHub Models](https://docs.github.com/en/github-models) | `free_token` | US | Yes | Yes | ✅ active | [docs](https://docs.github.com/en/github-models) |
| [Google AI Studio (Gemini Free)](https://ai.google.dev/gemini-api/docs) | `free_token` | US | Yes | Yes | ✅ active | [docs](https://ai.google.dev/gemini-api/docs) |
| [Groq Free Tier](https://console.groq.com/docs) | `free_token` | US | Yes | Yes | ✅ active | [docs](https://console.groq.com/docs) |
| [LLM7.io](https://llm7.io) | `free_token` | GB | Yes | Yes | ✅ active | [docs](https://llm7.io) |
| [NVIDIA NIM (Developer Free)](https://docs.api.nvidia.com/) | `free_token` | US | Yes | Yes | ✅ active | [docs](https://docs.api.nvidia.com/) |
| [OpenRouter Free Models](https://openrouter.ai/docs) | `free_token` | US | Yes | Yes | ✅ active | [docs](https://openrouter.ai/docs) |
| [SiliconFlow Free Models](https://docs.siliconflow.cn/) | `free_token` | CN | Yes | Yes | ✅ active | [docs](https://docs.siliconflow.cn/) |
| [Z.AI / Zhipu Free Flash Models](https://docs.bigmodel.cn/) | `free_token` | CN | Yes | Yes | ✅ active | [docs](https://docs.bigmodel.cn/) |

## Call example (OpenAI-compatible)

Example using the **OVH anonymous** endpoint (no key):

```bash
export LLM_BASE_URL="https://oai.endpoints.kepler.ai.cloud.ovh.net/v1"
export LLM_MODEL_NAME="Meta-Llama-3_3-70B-Instruct"

curl "$LLM_BASE_URL/chat/completions" \
  -H "Content-Type: application/json" \
  -d "{
    \"model\": \"$LLM_MODEL_NAME\",
    \"messages\": [{\"role\": \"user\", \"content\": \"hello\"}],
    \"max_tokens\": 64
  }"
```

## Project official testing APIs (demo / evaluation)

### Page Agent Free Testing API (Qwen)

- **Category**: `project_demo` · **Provider**: Alibaba page-agent maintainers (via Alibaba Cloud FC + BaiLian) · **Region**: CN
- **Status**: ✅ active · **Last verified**: `2026-07-15`
- **Base URL**: `https://page-ag-testing-ohftxirgbn.cn-shanghai.fcapp.run`
- **API key required**: No
- **Sample models**: `qwen3.5-plus`, `qwen3.5-flash`
- **Docs**: https://alibaba.github.io/page-agent/docs/features/models/#free-testing-api
- **Repo**: https://github.com/alibaba/page-agent
- **Terms**: https://github.com/alibaba/page-agent/blob/main/docs/terms-and-privacy.md#2-testing-api-and-demo-disclaimer--terms-of-use

**Copy-paste config**

```bash
LLM_BASE_URL="https://page-ag-testing-ohftxirgbn.cn-shanghai.fcapp.run"
LLM_MODEL_NAME="qwen3.5-plus"
```

**Restrictions**

> Strictly for PageAgent.js / Extension technical evaluation and R&D.
> No production use; no PII/sensitive data; processed via Mainland China servers.
> Proxy validates requests: first message must be system/developer and system prompt must match official page-agent prompt (generic chat may be rejected).
> May be rate-limited or discontinued without notice.

## Anonymous public endpoints (no key)

### OVHcloud AI Endpoints (Anonymous Free)

- **Category**: `anonymous_public` · **Provider**: OVHcloud · **Region**: EU
- **Status**: ✅ active · **Last verified**: `2026-07-15`
- **Base URL**: `https://oai.endpoints.kepler.ai.cloud.ovh.net/v1`
- **API key required**: No
- **Sample models**: `Meta-Llama-3_3-70B-Instruct`, `Llama-3.1-8B-Instruct`, `gpt-oss-120b`, `gpt-oss-20b`, `Qwen3-32B`, `Qwen3-Coder-30B-A3B-Instruct`, `Mistral-Small-3.2-24B-Instruct`, `Mistral-Nemo-Instruct-2407`, `Mistral-7B-Instruct-v0.3`
- **Docs**: https://www.ovhcloud.com/en/public-cloud/ai-endpoints/catalog/
- **Terms**: https://www.ovhcloud.com/en/terms-and-conditions/

**Copy-paste config**

```bash
LLM_BASE_URL="https://oai.endpoints.kepler.ai.cloud.ovh.net/v1"
LLM_MODEL_NAME="Meta-Llama-3_3-70B-Instruct"
```

**Restrictions**

> Anonymous tier: no signup, no API key; about 2 RPM per IP per model (verify docs).
> Good for wiring OpenAI SDK / agents; higher limits need OVH account + billing project.
> EU-hosted. Catalog may change — check GET /v1/models.

## Free token / free tier (key required)

### Cerebras Inference Free

- **Category**: `free_token` · **Provider**: Cerebras · **Region**: US
- **Status**: ✅ active · **Last verified**: `2026-07-15`
- **Base URL**: `https://api.cerebras.ai/v1`
- **API key required**: Yes · [Get key](https://cloud.cerebras.ai/)
- **Sample models**: `llama3.1-8b`, `gpt-oss-120b`
- **Docs**: https://inference-docs.cerebras.ai/
- **Terms**: https://www.cerebras.ai/terms-of-service

**Copy-paste config**

```bash
LLM_BASE_URL="https://api.cerebras.ai/v1"
LLM_MODEL_NAME="llama3.1-8b"
LLM_API_KEY="<https://cloud.cerebras.ai/>"
```

**Restrictions**

> Free-tier key; very high throughput for client/streaming tests.
> Free model list and context caps can change abruptly.

### GitHub Models

- **Category**: `free_token` · **Provider**: GitHub · **Region**: US
- **Status**: ✅ active · **Last verified**: `2026-07-15`
- **Base URL**: `https://models.github.ai/inference`
- **API key required**: Yes · [Get key](https://github.com/settings/tokens)
- **Sample models**: `openai/gpt-4.1-mini`, `openai/gpt-4o-mini`, `meta/Llama-3.3-70B-Instruct`, `deepseek/DeepSeek-R1`
- **Docs**: https://docs.github.com/en/github-models
- **Terms**: https://docs.github.com/en/site-policy

**Copy-paste config**

```bash
LLM_BASE_URL="https://models.github.ai/inference"
LLM_MODEL_NAME="openai/gpt-4.1-mini"
LLM_API_KEY="<GitHub PAT with models access>"
```

**Restrictions**

> Use a GitHub token with models permissions for prototyping.
> Limits depend on Copilot tier; strict per-request caps — good for feature tests.

### Google AI Studio (Gemini Free)

- **Category**: `free_token` · **Provider**: Google · **Region**: US
- **Status**: ✅ active · **Last verified**: `2026-07-15`
- **Base URL**: `https://generativelanguage.googleapis.com/v1beta/openai`
- **API key required**: Yes · [Get key](https://aistudio.google.com/app/apikey)
- **Sample models**: `gemini-2.5-flash`, `gemini-2.5-flash-lite`, `gemini-2.0-flash`
- **Docs**: https://ai.google.dev/gemini-api/docs
- **Terms**: https://ai.google.dev/gemini-api/terms

**Copy-paste config**

```bash
LLM_BASE_URL="https://generativelanguage.googleapis.com/v1beta/openai"
LLM_MODEL_NAME="gemini-2.5-flash"
LLM_API_KEY="<https://aistudio.google.com/app/apikey>"
```

**Restrictions**

> Free API key via AI Studio; free tier unavailable in some regions.
> Read ToS for data use / regional limits; quotas vary by model.

### Groq Free Tier

- **Category**: `free_token` · **Provider**: Groq · **Region**: US
- **Status**: ✅ active · **Last verified**: `2026-07-15`
- **Base URL**: `https://api.groq.com/openai/v1`
- **API key required**: Yes · [Get key](https://console.groq.com/keys)
- **Sample models**: `llama-3.1-8b-instant`, `llama-3.3-70b-versatile`, `openai/gpt-oss-20b`, `qwen/qwen3-32b`
- **Docs**: https://console.groq.com/docs
- **Terms**: https://groq.com/terms-of-use/

**Copy-paste config**

```bash
LLM_BASE_URL="https://api.groq.com/openai/v1"
LLM_MODEL_NAME="llama-3.1-8b-instant"
LLM_API_KEY="<https://console.groq.com/keys>"
```

**Restrictions**

> Free console key, typically no card for testing; RPM/TPM/RPD limits apply.
> Great for latency-sensitive wiring; verify official rate-limits page.

### LLM7.io

- **Category**: `free_token` · **Provider**: LLM7.io · **Region**: GB
- **Status**: ✅ active · **Last verified**: `2026-07-15`
- **Base URL**: `https://api.llm7.io/v1`
- **API key required**: Yes · [Get key](https://token.llm7.io)
- **Sample models**: `deepseek-v4-flash`, `gemma3:27b`, `gpt-5.4-mini`, `kimi-k2.6`, `minimax-m2.7`
- **Docs**: https://llm7.io
- **Terms**: https://llm7.io

**Copy-paste config**

```bash
LLM_BASE_URL="https://api.llm7.io/v1"
LLM_MODEL_NAME="deepseek-v4-flash"
LLM_API_KEY="<get free token at https://token.llm7.io>"
```

**Restrictions**

> Free token available; limits per official site (token usually raises RPM).
> Third-party gateway — evaluate stability, compliance, and data path yourself.
> Model availability changes; good for quick OpenAI-compatible client tests.

### NVIDIA NIM (Developer Free)

- **Category**: `free_token` · **Provider**: NVIDIA · **Region**: US
- **Status**: ✅ active · **Last verified**: `2026-07-15`
- **Base URL**: `https://integrate.api.nvidia.com/v1`
- **API key required**: Yes · [Get key](https://build.nvidia.com/)
- **Sample models**: `meta/llama-3.1-8b-instruct`, `microsoft/phi-3-mini-4k-instruct`, `google/gemma-2-9b-it`
- **Docs**: https://docs.api.nvidia.com/
- **Terms**: https://www.nvidia.com/en-us/about-nvidia/privacy-policy/

**Copy-paste config**

```bash
LLM_BASE_URL="https://integrate.api.nvidia.com/v1"
LLM_MODEL_NAME="meta/llama-3.1-8b-instruct"
LLM_API_KEY="<https://build.nvidia.com/>"
```

**Restrictions**

> Free access for NVIDIA Developer Program members; signup/verification usual.
> Rate-limited and often context-capped — fine for model smoke tests.

### OpenRouter Free Models

- **Category**: `free_token` · **Provider**: OpenRouter · **Region**: US
- **Status**: ✅ active · **Last verified**: `2026-07-15`
- **Base URL**: `https://openrouter.ai/api/v1`
- **API key required**: Yes · [Get key](https://openrouter.ai/keys)
- **Sample models**: `openrouter/free`, `meta-llama/llama-3.3-70b-instruct:free`, `qwen/qwen3-coder:free`, `openai/gpt-oss-20b:free`, `google/gemma-4-31b-it:free`
- **Docs**: https://openrouter.ai/docs
- **Terms**: https://openrouter.ai/terms

**Copy-paste config**

```bash
LLM_BASE_URL="https://openrouter.ai/api/v1"
LLM_MODEL_NAME="openrouter/free"
LLM_API_KEY="<https://openrouter.ai/keys>"
```

**Restrictions**

> Free API key after signup; use models with `:free` suffix (or free router).
> Low default daily limits; free providers may log prompts. For dev/testing.

### SiliconFlow Free Models

- **Category**: `free_token` · **Provider**: SiliconFlow · **Region**: CN
- **Status**: ✅ active · **Last verified**: `2026-07-15`
- **Base URL**: `https://api.siliconflow.cn/v1`
- **API key required**: Yes · [Get key](https://cloud.siliconflow.cn/account/ak)
- **Sample models**: `Qwen/Qwen3-8B`, `deepseek-ai/DeepSeek-R1-Distill-Qwen-7B`
- **Docs**: https://docs.siliconflow.cn/
- **Terms**: https://docs.siliconflow.cn/

**Copy-paste config**

```bash
LLM_BASE_URL="https://api.siliconflow.cn/v1"
LLM_MODEL_NAME="Qwen/Qwen3-8B"
LLM_API_KEY="<https://cloud.siliconflow.cn/account/ak>"
```

**Restrictions**

> Create a key after signup; some models permanently free, others paid.
> Trust console free-model labels; convenient for CN network testing.

### Z.AI / Zhipu Free Flash Models

- **Category**: `free_token` · **Provider**: Zhipu / Z.AI · **Region**: CN
- **Status**: ✅ active · **Last verified**: `2026-07-15`
- **Base URL**: `https://open.bigmodel.cn/api/paas/v4`
- **API key required**: Yes · [Get key](https://open.bigmodel.cn/usercenter/apikeys)
- **Sample models**: `glm-4.7-flash`, `glm-4.6v-flash`
- **Docs**: https://docs.bigmodel.cn/
- **Terms**: https://open.bigmodel.cn/

**Copy-paste config**

```bash
LLM_BASE_URL="https://open.bigmodel.cn/api/paas/v4"
LLM_MODEL_NAME="glm-4.7-flash"
LLM_API_KEY="<https://open.bigmodel.cn/usercenter/apikeys>"
```

**Restrictions**

> Official permanent free Flash-class models; concurrency/quotas per console.
> Useful for Chinese-language feature validation.

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md).

1. Add an entry to `data/endpoints.yaml` (`env.LLM_BASE_URL` + `env.LLM_MODEL_NAME` required)
2. `python scripts/validate.py && python scripts/generate_readme.py`
3. Open a PR with docs links and evaluation-only notes

## Reference style

```bash
# qwen3.5-plus / qwen3.5-flash
LLM_BASE_URL="https://page-ag-testing-ohftxirgbn.cn-shanghai.fcapp.run"
LLM_MODEL_NAME="qwen3.5-plus"
```

From: <https://alibaba.github.io/page-agent/docs/features/models/#free-testing-api>

## License

[MIT](./LICENSE)
