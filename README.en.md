# Free LLM API Catalog

> Official vendors + mainstream inference platforms · **Permanent free tiers only** · Data-driven

[中文](./README.md) · Source of truth: [`data/providers.yaml`](./data/providers.yaml) · Data updated: `2026-07-15`

## What is this

A curated catalog of publicly obtainable LLM HTTP APIs where:

- Permanent free tiers only from model vendors and mainstream inference platforms. No one-shot trial credits or unofficial reverse proxies.
- Official docs and signup / key pages exist
- **Excluded**: one-shot trial credits only, unofficial reverse proxies, scraped chatbot UIs

## Disclaimer

- Quotas, models, and ToS **change without notice** — always verify official docs.
- This repo is informational only; no proxies, shared keys, or bypass guides.
- Read each provider's ToS (commercial use, training, regional limits).
- Use free tiers responsibly so the community keeps access.

## Overview (19)

| Name | Type | Region | OpenAI-compatible | Card required | Status | Docs |
| --- | --- | --- | --- | --- | --- | --- |
| [Aion Labs](https://www.aionlabs.ai) | Model vendor | IL | Yes | No | ✅ active | [docs](https://www.aionlabs.ai) |
| [Cohere](https://cohere.com) | Model vendor | CA | No | No | ✅ active | [docs](https://docs.cohere.com/) |
| [Google AI Studio (Gemini)](https://aistudio.google.com) | Model vendor | US | Yes | No | ✅ active | [docs](https://ai.google.dev/gemini-api/docs) |
| [Mistral AI (La Plateforme)](https://console.mistral.ai/) | Model vendor | FR | Yes | No | ✅ active | [docs](https://docs.mistral.ai/) |
| [Z.AI (Zhipu / BigModel)](https://open.bigmodel.cn/) | Model vendor | CN | Yes | No | ✅ active | [docs](https://docs.bigmodel.cn/) |
| [Cerebras Inference](https://cloud.cerebras.ai/) | Inference platform | US | Yes | No | ✅ active | [docs](https://inference-docs.cerebras.ai/) |
| [Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/) | Inference platform | US | No | No | ✅ active | [docs](https://developers.cloudflare.com/workers-ai/) |
| [GitHub Models](https://github.com/marketplace/models) | Inference platform | US | Yes | No | ✅ active | [docs](https://docs.github.com/en/github-models) |
| [Groq](https://console.groq.com) | Inference platform | US | Yes | No | ✅ active | [docs](https://console.groq.com/docs) |
| [Hugging Face Inference Providers](https://huggingface.co) | Inference platform | US | Yes | No | ✅ active | [docs](https://huggingface.co/docs/inference-providers) |
| [LLM7.io](https://llm7.io) | Inference platform | GB | Yes | No | ⚠️ limited | [docs](https://llm7.io) |
| [ModelScope API-Inference](https://modelscope.cn) | Inference platform | CN | Yes | No | ✅ active | [docs](https://modelscope.cn/docs/model-service/API-Inference/intro) |
| [NVIDIA NIM](https://build.nvidia.com/explore/discover) | Inference platform | US | Yes | No | ✅ active | [docs](https://docs.api.nvidia.com/) |
| [Ollama Cloud](https://ollama.com) | Inference platform | US | No | No | ✅ active | [docs](https://docs.ollama.com/cloud) |
| [OpenRouter (free models)](https://openrouter.ai) | Inference platform | US | Yes | No | ✅ active | [docs](https://openrouter.ai/docs) |
| [OVHcloud AI Endpoints](https://www.ovhcloud.com/en/public-cloud/ai-endpoints/) | Inference platform | EU | Yes | No | ✅ active | [docs](https://help.ovhcloud.com/csm/en-public-cloud-ai-endpoints) |
| [SambaNova Cloud](https://cloud.sambanova.ai/) | Inference platform | US | Yes | No | ✅ active | [docs](https://docs.sambanova.ai/) |
| [SiliconFlow](https://siliconflow.cn) | Inference platform | CN | Yes | No | ✅ active | [docs](https://docs.siliconflow.cn/) |
| [Vercel AI Gateway](https://vercel.com/docs/ai-gateway) | Inference platform | US | Yes | No | ✅ active | [docs](https://vercel.com/docs/ai-gateway) |

## Model vendor APIs

### Aion Labs

- **Type**: Model vendor · **Region**: IL · **Status**: ✅ active
- **Website**: https://www.aionlabs.ai
- **Docs**: https://www.aionlabs.ai
- **API key**: https://www.aionlabs.ai
- **Base URL**: `https://api.aionlabs.ai/v1`
- **OpenAI-compatible**: Yes · **Card required**: No · **Phone**: No
- **Rate / quota (summary)**: 15 RPM, ~20K tokens/day
- **Commercial use**: `unknown` · **Data use**: unknown
- **Sample models**: `aion-2.5`, `aion-2.0`, `aion-rp-1.0`
- **Notes**: Permanent free tier focused on roleplay/storytelling; no card required.
- **Last verified**: `2026-07-15`

### Cohere

- **Type**: Model vendor · **Region**: CA · **Status**: ✅ active
- **Website**: https://cohere.com
- **Docs**: https://docs.cohere.com/
- **API key**: https://dashboard.cohere.com/api-keys
- **Base URL**: `https://api.cohere.com/v2`
- **OpenAI-compatible**: No · **Card required**: No · **Phone**: No
- **Rate / quota (summary)**: 20 RPM, ~1,000 requests/month (shared)
- **Commercial use**: `no` · **Data use**: unknown
- **Sample models**: `command-a-03-2025`, `command-r-plus-08-2024`, `command-r7b-12-2024`, `command-a-vision-07-2025`
- **Notes**: Trial/free API key, typically no card; ~1,000 calls/month, 20 RPM; non-commercial limits — read ToS.
- **Last verified**: `2026-07-15`

### Google AI Studio (Gemini)

- **Type**: Model vendor · **Region**: US · **Status**: ✅ active
- **Website**: https://aistudio.google.com
- **Docs**: https://ai.google.dev/gemini-api/docs
- **API key**: https://aistudio.google.com/app/apikey
- **Base URL**: `https://generativelanguage.googleapis.com/v1beta`
- **OpenAI-compatible**: Yes · **Card required**: No · **Phone**: No
- **Rate / quota (summary)**: Per-model; e.g. Flash-class often ~5–30 RPM / tens–thousands RPD; Gemma often higher RPD
- **Commercial use**: `restricted` · **Data use**: may be used for training/improvement
- **Sample models**: `gemini-2.5-flash`, `gemini-2.5-flash-lite`, `gemini-3.1-flash-lite`, `gemma-3-27b-it`
- **Notes**: Free tier may be unavailable in EU/UK/CH. Free-tier prompts may be used to improve products outside certain regions. Quotas change; verify official docs.
- **Last verified**: `2026-07-15`

### Mistral AI (La Plateforme)

- **Type**: Model vendor · **Region**: FR · **Status**: ✅ active
- **Website**: https://console.mistral.ai/
- **Docs**: https://docs.mistral.ai/
- **API key**: https://console.mistral.ai/api-keys
- **Base URL**: `https://api.mistral.ai/v1`
- **OpenAI-compatible**: Yes · **Card required**: No · **Phone**: Yes
- **Rate / quota (summary)**: ~1 RPS, ~500K TPM, ~1B tokens/month per model (Experiment)
- **Commercial use**: `restricted` · **Data use**: may be used for training/improvement
- **Sample models**: `mistral-small-latest`, `mistral-medium-latest`, `codestral-latest`, `mistral-nemo`
- **Notes**: Experiment plan free tier; phone verification usually required; may require opt-in for training. ~1B tokens/month class limits (verify docs).
- **Last verified**: `2026-07-15`

### Z.AI (Zhipu / BigModel)

- **Type**: Model vendor · **Region**: CN · **Status**: ✅ active
- **Website**: https://open.bigmodel.cn/
- **Docs**: https://docs.bigmodel.cn/
- **API key**: https://open.bigmodel.cn/usercenter/apikeys
- **Base URL**: `https://open.bigmodel.cn/api/paas/v4`
- **OpenAI-compatible**: Yes · **Card required**: No · **Phone**: No
- **Rate / quota (summary)**: Often ~1 concurrent on free Flash models (verify)
- **Commercial use**: `restricted` · **Data use**: unknown
- **Sample models**: `glm-4.7-flash`, `glm-4.6v-flash`
- **Notes**: Permanent free models (e.g. GLM Flash family); concurrency/quotas per console. International portals may differ.
- **Last verified**: `2026-07-15`

## Inference platforms

### Cerebras Inference

- **Type**: Inference platform · **Region**: US · **Status**: ✅ active
- **Website**: https://cloud.cerebras.ai/
- **Docs**: https://inference-docs.cerebras.ai/
- **API key**: https://cloud.cerebras.ai/
- **Base URL**: `https://api.cerebras.ai/v1`
- **OpenAI-compatible**: Yes · **Card required**: No · **Phone**: No
- **Rate / quota (summary)**: e.g. gpt-oss-120b: ~30 RPM, ~14.4K RPD, ~1M TPD (verify)
- **Commercial use**: `yes` · **Data use**: typically not for training
- **Sample models**: `gpt-oss-120b`, `llama3.1-8b`
- **Notes**: Wafer-scale ultra-fast inference; free model catalog and context caps can change.
- **Last verified**: `2026-07-15`

### Cloudflare Workers AI

- **Type**: Inference platform · **Region**: US · **Status**: ✅ active
- **Website**: https://developers.cloudflare.com/workers-ai/
- **Docs**: https://developers.cloudflare.com/workers-ai/
- **API key**: https://dash.cloudflare.com/profile/api-tokens
- **Base URL**: `https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run`
- **OpenAI-compatible**: No · **Card required**: No · **Phone**: No
- **Rate / quota (summary)**: ~10,000 neurons/day shared across models
- **Commercial use**: `yes` · **Data use**: unknown
- **Sample models**: `@cf/meta/llama-3.3-70b-instruct-fp8-fast`, `@cf/meta/llama-4-scout-17b-16e-instruct`, `@cf/openai/gpt-oss-120b`, `@cf/qwen/qwen3-30b-a3b-fp8`
- **Notes**: Daily free Neurons allocation (e.g. 10,000/day); large model catalog.
- **Last verified**: `2026-07-15`

### GitHub Models

- **Type**: Inference platform · **Region**: US · **Status**: ✅ active
- **Website**: https://github.com/marketplace/models
- **Docs**: https://docs.github.com/en/github-models
- **API key**: https://github.com/settings/tokens
- **Base URL**: `https://models.github.ai/inference`
- **OpenAI-compatible**: Yes · **Card required**: No · **Phone**: No
- **Rate / quota (summary)**: Tier-based RPM/RPD (e.g. free often ~10–15 RPM / ~50–150 RPD class)
- **Commercial use**: `restricted` · **Data use**: unknown
- **Sample models**: `openai/gpt-4.1-mini`, `meta/Llama-3.3-70B-Instruct`, `deepseek/DeepSeek-R1`, `mistral-ai/Mistral-Small-3.1`
- **Notes**: For prototyping; limits depend on Copilot tier; per-request input/output caps are strict.
- **Last verified**: `2026-07-15`

### Groq

- **Type**: Inference platform · **Region**: US · **Status**: ✅ active
- **Website**: https://console.groq.com
- **Docs**: https://console.groq.com/docs
- **API key**: https://console.groq.com/keys
- **Base URL**: `https://api.groq.com/openai/v1`
- **OpenAI-compatible**: Yes · **Card required**: No · **Phone**: No
- **Rate / quota (summary)**: Model-dependent; e.g. ~30 RPM, ~1K–14K RPD, TPM in thousands–tens of thousands
- **Commercial use**: `yes` · **Data use**: typically not for training
- **Sample models**: `llama-3.3-70b-versatile`, `llama-3.1-8b-instant`, `openai/gpt-oss-120b`, `qwen/qwen3-32b`
- **Notes**: Ultra-fast LPU inference; free tier has RPM/TPM/RPD caps (tighter RPD on larger models).
- **Last verified**: `2026-07-15`

### Hugging Face Inference Providers

- **Type**: Inference platform · **Region**: US · **Status**: ✅ active
- **Website**: https://huggingface.co
- **Docs**: https://huggingface.co/docs/inference-providers
- **API key**: https://huggingface.co/settings/tokens
- **Base URL**: `https://router.huggingface.co/v1`
- **OpenAI-compatible**: Yes · **Card required**: No · **Phone**: No
- **Rate / quota (summary)**: Credit-metered monthly free allocation
- **Commercial use**: `restricted` · **Data use**: unknown
- **Sample models**: `meta-llama/Meta-Llama-3.1-8B-Instruct`, `mistralai/Mistral-7B-Instruct-v0.3`, `Qwen/Qwen2.5-7B-Instruct`
- **Notes**: Free users get monthly Inference Provider credits (e.g. ~$0.10 class); routes to multiple backends.
- **Last verified**: `2026-07-15`

### LLM7.io

- **Type**: Inference platform · **Region**: GB · **Status**: ⚠️ limited
- **Website**: https://llm7.io
- **Docs**: https://llm7.io
- **API key**: https://token.llm7.io
- **Base URL**: `https://api.llm7.io/v1`
- **OpenAI-compatible**: Yes · **Card required**: No · **Phone**: No
- **Rate / quota (summary)**: ~30 RPM default; ~120 RPM with token
- **Commercial use**: `unknown` · **Data use**: unknown
- **Sample models**: `gemini-2.5-flash-lite`, `mistral-small-3.1-24b`, `qwen2.5-coder-32b`
- **Notes**: Low-friction gateway; basic access without signup; higher limits with token. Third-party aggregation — evaluate stability/compliance yourself.
- **Last verified**: `2026-07-15`

### ModelScope API-Inference

- **Type**: Inference platform · **Region**: CN · **Status**: ✅ active
- **Website**: https://modelscope.cn
- **Docs**: https://modelscope.cn/docs/model-service/API-Inference/intro
- **API key**: https://modelscope.cn/my/myaccesstoken
- **Base URL**: `https://api-inference.modelscope.cn/v1`
- **OpenAI-compatible**: Yes · **Card required**: No · **Phone**: Yes
- **Rate / quota (summary)**: e.g. ~2,000 RPD total, per-model cap ~500 RPD (dynamic)
- **Commercial use**: `restricted` · **Data use**: unknown
- **Sample models**: `Qwen/Qwen3.5-35B-A3B`, `Qwen/Qwen3.5-27B`
- **Notes**: Free API-Inference for registered users; often needs Alibaba Cloud binding + real-name verification; dynamic daily quotas.
- **Last verified**: `2026-07-15`

### NVIDIA NIM

- **Type**: Inference platform · **Region**: US · **Status**: ✅ active
- **Website**: https://build.nvidia.com/explore/discover
- **Docs**: https://docs.api.nvidia.com/
- **API key**: https://build.nvidia.com/
- **Base URL**: `https://integrate.api.nvidia.com/v1`
- **OpenAI-compatible**: Yes · **Card required**: No · **Phone**: Yes
- **Rate / quota (summary)**: ~40 RPM (typical free); no simple public daily token cap
- **Commercial use**: `restricted` · **Data use**: unknown
- **Sample models**: `meta/llama-3.1-405b-instruct`, `deepseek-ai/deepseek-r1`, `nvidia/nemotron-3-super-120b-a12b`, `qwen/qwen2.5-72b-instruct`
- **Notes**: Free with NVIDIA Developer Program; phone verification common; context often limited.
- **Last verified**: `2026-07-15`

### Ollama Cloud

- **Type**: Inference platform · **Region**: US · **Status**: ✅ active
- **Website**: https://ollama.com
- **Docs**: https://docs.ollama.com/cloud
- **API key**: https://ollama.com/settings/keys
- **Base URL**: `https://api.ollama.com`
- **OpenAI-compatible**: No · **Card required**: No · **Phone**: No
- **Rate / quota (summary)**: Session/weekly qualitative limits (unpublished exact numbers)
- **Commercial use**: `restricted` · **Data use**: unknown
- **Sample models**: `gpt-oss:120b-cloud`, `deepseek-r1:cloud`, `qwen3-coder:480b-cloud`
- **Notes**: Free light-usage tier; limits are session/weekly and not always fully published; Ollama API, not stock OpenAI SDK.
- **Last verified**: `2026-07-15`

### OpenRouter (free models)

- **Type**: Inference platform · **Region**: US · **Status**: ✅ active
- **Website**: https://openrouter.ai
- **Docs**: https://openrouter.ai/docs
- **API key**: https://openrouter.ai/keys
- **Base URL**: `https://openrouter.ai/api/v1`
- **OpenAI-compatible**: Yes · **Card required**: No · **Phone**: No
- **Rate / quota (summary)**: e.g. ~20 RPM, ~50–200 RPD default; up to ~1000 RPD after $10 lifetime top-up
- **Commercial use**: `restricted` · **Data use**: may be used for training/improvement
- **Sample models**: `qwen/qwen3-coder:free`, `meta-llama/llama-3.3-70b-instruct:free`, `openai/gpt-oss-20b:free`, `google/gemma-4-31b-it:free`
- **Notes**: Only `:free` models count. Free models work without balance. Providers may log prompts. Lifetime top-up can raise free-model RPD.
- **Last verified**: `2026-07-15`

### OVHcloud AI Endpoints

- **Type**: Inference platform · **Region**: EU · **Status**: ✅ active
- **Website**: https://www.ovhcloud.com/en/public-cloud/ai-endpoints/
- **Docs**: https://help.ovhcloud.com/csm/en-public-cloud-ai-endpoints
- **API key**: https://www.ovhcloud.com/en/public-cloud/ai-endpoints/catalog/
- **Base URL**: `https://oai.endpoints.kepler.ai.cloud.ovh.net/v1`
- **OpenAI-compatible**: Yes · **Card required**: No · **Phone**: No
- **Rate / quota (summary)**: Anonymous ~2 RPM/IP/model; authenticated higher (paid)
- **Commercial use**: `yes` · **Data use**: unknown
- **Sample models**: `Meta-Llama-3_3-70B-Instruct`, `gpt-oss-120b`, `Mistral-Small-3.2-24B-Instruct`, `Qwen3-Coder-30B-A3B-Instruct`
- **Notes**: Anonymous free tier: no signup/key, ~2 RPM per IP per model; higher limits need paid project. EU-hosted.
- **Last verified**: `2026-07-15`

### SambaNova Cloud

- **Type**: Inference platform · **Region**: US · **Status**: ✅ active
- **Website**: https://cloud.sambanova.ai/
- **Docs**: https://docs.sambanova.ai/
- **API key**: https://cloud.sambanova.ai/apis
- **Base URL**: `https://api.sambanova.ai/v1`
- **OpenAI-compatible**: Yes · **Card required**: No · **Phone**: No
- **Rate / quota (summary)**: ~20 RPM, ~20 RPD, ~200K TPD per model (verify)
- **Commercial use**: `yes` · **Data use**: unknown
- **Sample models**: `Meta-Llama-3.3-70B-Instruct`, `DeepSeek-V3.1`, `gpt-oss-120b`
- **Notes**: Ongoing free tier (RPM/RPD/TPD). Signup trial credits may exist separately; permanent free tier is what qualifies.
- **Last verified**: `2026-07-15`

### SiliconFlow

- **Type**: Inference platform · **Region**: CN · **Status**: ✅ active
- **Website**: https://siliconflow.cn
- **Docs**: https://docs.siliconflow.cn/
- **API key**: https://cloud.siliconflow.cn/account/ak
- **Base URL**: `https://api.siliconflow.cn/v1`
- **OpenAI-compatible**: Yes · **Card required**: No · **Phone**: No
- **Rate / quota (summary)**: e.g. free models ~30 RPM / ~60K TPM class (verify)
- **Commercial use**: `restricted` · **Data use**: unknown
- **Sample models**: `Qwen/Qwen3-8B`, `deepseek-ai/DeepSeek-R1-Distill-Qwen-7B`
- **Notes**: Selected models permanently free; many others paid. OpenAI-compatible API.
- **Last verified**: `2026-07-15`

### Vercel AI Gateway

- **Type**: Inference platform · **Region**: US · **Status**: ✅ active
- **Website**: https://vercel.com/docs/ai-gateway
- **Docs**: https://vercel.com/docs/ai-gateway
- **API key**: https://vercel.com/account/tokens
- **Base URL**: `—`
- **OpenAI-compatible**: Yes · **Card required**: No · **Phone**: No
- **Rate / quota (summary)**: Monthly free credit allowance
- **Commercial use**: `yes` · **Data use**: unknown
- **Sample models**: `various-via-gateway`
- **Notes**: Gateway to multiple providers; monthly free allowance (e.g. ~$5/month class — verify pricing page).
- **Last verified**: `2026-07-15`

## Quick start

Most OpenAI-compatible endpoints work like this (Groq example):

```bash
export OPENAI_API_KEY=gsk_xxx
export OPENAI_BASE_URL=https://api.groq.com/openai/v1

curl "$OPENAI_BASE_URL/chat/completions" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"llama-3.1-8b-instant","messages":[{"role":"user","content":"hello"}]}'
```

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md).

1. Edit `data/providers.yaml`
2. Run `python scripts/validate.py`
3. Run `python scripts/generate_readme.py`
4. Open a PR (do not hand-edit generated READMEs)

## Related projects

| Project | How we differ |
| --- | --- |
| [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | Broader (includes trial credits); we keep **permanent free only** + YAML SSOT + bilingual docs |
| [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | Awesome-list style; we focus on schema validation and generated READMEs |

Thanks to those community efforts.

## Maintenance

```bash
pip install -r requirements.txt
python scripts/validate.py
python scripts/generate_readme.py
```

## License

[MIT](./LICENSE)
