# 免费 LLM API 目录

> 官方 + 主流推理平台 · **仅永久免费档** · 结构化数据驱动

[English](./README.en.md) · 数据源 [`data/providers.yaml`](./data/providers.yaml) · 上次数据更新：`2026-07-15`

## 这是什么

收集并维护**可公开申请**的 LLM HTTP API，条件是：

- 仅收录提供持续可用免费档的模型厂商官方 API 与主流推理平台；排除一次性试用额度与非官方反代。
- 有官方文档与申请入口
- **不包含**一次性试用额度、非官方反代、聊天网页扒接口

## 免责声明

- 配额、模型列表、服务条款**随时可能变更**，请以各服务商官网为准。
- 本仓库只做信息整理，不提供代理、Key 共享或绕过限制的方法。
- 使用前请阅读各厂商 ToS（商业用途、数据训练、地区限制等）。
- 请合理使用免费档，避免滥用导致社区失去这些资源。

## 总览（19）

| 名称 | 类型 | 地区 | OpenAI 兼容 | 需绑卡 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- | --- |
| [Aion Labs](https://www.aionlabs.ai) | 模型厂商 | IL | 是 | 否 | ✅ active | [docs](https://www.aionlabs.ai) |
| [Cohere](https://cohere.com) | 模型厂商 | CA | 否 | 否 | ✅ active | [docs](https://docs.cohere.com/) |
| [Google AI Studio（Gemini）](https://aistudio.google.com) | 模型厂商 | US | 是 | 否 | ✅ active | [docs](https://ai.google.dev/gemini-api/docs) |
| [Mistral AI（La Plateforme）](https://console.mistral.ai/) | 模型厂商 | FR | 是 | 否 | ✅ active | [docs](https://docs.mistral.ai/) |
| [智谱 Z.AI（BigModel）](https://open.bigmodel.cn/) | 模型厂商 | CN | 是 | 否 | ✅ active | [docs](https://docs.bigmodel.cn/) |
| [Cerebras Inference](https://cloud.cerebras.ai/) | 推理平台 | US | 是 | 否 | ✅ active | [docs](https://inference-docs.cerebras.ai/) |
| [Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/) | 推理平台 | US | 否 | 否 | ✅ active | [docs](https://developers.cloudflare.com/workers-ai/) |
| [GitHub Models](https://github.com/marketplace/models) | 推理平台 | US | 是 | 否 | ✅ active | [docs](https://docs.github.com/en/github-models) |
| [Groq](https://console.groq.com) | 推理平台 | US | 是 | 否 | ✅ active | [docs](https://console.groq.com/docs) |
| [Hugging Face Inference Providers](https://huggingface.co) | 推理平台 | US | 是 | 否 | ✅ active | [docs](https://huggingface.co/docs/inference-providers) |
| [LLM7.io](https://llm7.io) | 推理平台 | GB | 是 | 否 | ⚠️ limited | [docs](https://llm7.io) |
| [魔搭 ModelScope API-Inference](https://modelscope.cn) | 推理平台 | CN | 是 | 否 | ✅ active | [docs](https://modelscope.cn/docs/model-service/API-Inference/intro) |
| [NVIDIA NIM](https://build.nvidia.com/explore/discover) | 推理平台 | US | 是 | 否 | ✅ active | [docs](https://docs.api.nvidia.com/) |
| [Ollama Cloud](https://ollama.com) | 推理平台 | US | 否 | 否 | ✅ active | [docs](https://docs.ollama.com/cloud) |
| [OpenRouter（免费模型）](https://openrouter.ai) | 推理平台 | US | 是 | 否 | ✅ active | [docs](https://openrouter.ai/docs) |
| [OVHcloud AI Endpoints](https://www.ovhcloud.com/en/public-cloud/ai-endpoints/) | 推理平台 | EU | 是 | 否 | ✅ active | [docs](https://help.ovhcloud.com/csm/en-public-cloud-ai-endpoints) |
| [SambaNova Cloud](https://cloud.sambanova.ai/) | 推理平台 | US | 是 | 否 | ✅ active | [docs](https://docs.sambanova.ai/) |
| [硅基流动 SiliconFlow](https://siliconflow.cn) | 推理平台 | CN | 是 | 否 | ✅ active | [docs](https://docs.siliconflow.cn/) |
| [Vercel AI Gateway](https://vercel.com/docs/ai-gateway) | 推理平台 | US | 是 | 否 | ✅ active | [docs](https://vercel.com/docs/ai-gateway) |

## 模型厂商官方 API

### Aion Labs

- **类型**: 模型厂商 · **地区**: IL · **状态**: ✅ active
- **官网**: https://www.aionlabs.ai
- **文档**: https://www.aionlabs.ai
- **获取 Key**: https://www.aionlabs.ai
- **Base URL**: `https://api.aionlabs.ai/v1`
- **OpenAI 兼容**: 是 · **需绑卡**: 否 · **手机验证**: 否
- **速率/额度（摘要）**: 15 RPM, ~20K tokens/day
- **商业使用**: `unknown` · **数据用途**: 未知
- **示例模型**: `aion-2.5`, `aion-2.0`, `aion-rp-1.0`
- **说明**: 永久免费档，偏角色扮演/叙事场景；无需绑卡。
- **上次核对**: `2026-07-15`

### Cohere

- **类型**: 模型厂商 · **地区**: CA · **状态**: ✅ active
- **官网**: https://cohere.com
- **文档**: https://docs.cohere.com/
- **获取 Key**: https://dashboard.cohere.com/api-keys
- **Base URL**: `https://api.cohere.com/v2`
- **OpenAI 兼容**: 否 · **需绑卡**: 否 · **手机验证**: 否
- **速率/额度（摘要）**: 20 RPM, ~1,000 requests/month (shared)
- **商业使用**: `no` · **数据用途**: 未知
- **示例模型**: `command-a-03-2025`, `command-r-plus-08-2024`, `command-r7b-12-2024`, `command-a-vision-07-2025`
- **说明**: Trial/免费 API Key，通常无需绑卡；约 1000 次/月、20 RPM；非商业用途限制请读服务条款。
- **上次核对**: `2026-07-15`

### Google AI Studio（Gemini）

- **类型**: 模型厂商 · **地区**: US · **状态**: ✅ active
- **官网**: https://aistudio.google.com
- **文档**: https://ai.google.dev/gemini-api/docs
- **获取 Key**: https://aistudio.google.com/app/apikey
- **Base URL**: `https://generativelanguage.googleapis.com/v1beta`
- **OpenAI 兼容**: 是 · **需绑卡**: 否 · **手机验证**: 否
- **速率/额度（摘要）**: Per-model; e.g. Flash-class often ~5–30 RPM / tens–thousands RPD; Gemma often higher RPD
- **商业使用**: `restricted` · **数据用途**: 可能用于训练/改进
- **示例模型**: `gemini-2.5-flash`, `gemini-2.5-flash-lite`, `gemini-3.1-flash-lite`, `gemma-3-27b-it`
- **说明**: 免费档在部分地区（如 EU/UK/CH）可能不可用；免费层提示词可能被用于产品改进（部分地区除外）。配额会调整，以官网为准。
- **上次核对**: `2026-07-15`

### Mistral AI（La Plateforme）

- **类型**: 模型厂商 · **地区**: FR · **状态**: ✅ active
- **官网**: https://console.mistral.ai/
- **文档**: https://docs.mistral.ai/
- **获取 Key**: https://console.mistral.ai/api-keys
- **Base URL**: `https://api.mistral.ai/v1`
- **OpenAI 兼容**: 是 · **需绑卡**: 否 · **手机验证**: 是
- **速率/额度（摘要）**: ~1 RPS, ~500K TPM, ~1B tokens/month per model (Experiment)
- **商业使用**: `restricted` · **数据用途**: 可能用于训练/改进
- **示例模型**: `mistral-small-latest`, `mistral-medium-latest`, `codestral-latest`, `mistral-nemo`
- **说明**: Experiment 计划免费档；通常需手机验证；可能需同意数据用于改进模型。~1B tokens/月量级（以官方为准）。
- **上次核对**: `2026-07-15`

### 智谱 Z.AI（BigModel）

- **类型**: 模型厂商 · **地区**: CN · **状态**: ✅ active
- **官网**: https://open.bigmodel.cn/
- **文档**: https://docs.bigmodel.cn/
- **获取 Key**: https://open.bigmodel.cn/usercenter/apikeys
- **Base URL**: `https://open.bigmodel.cn/api/paas/v4`
- **OpenAI 兼容**: 是 · **需绑卡**: 否 · **手机验证**: 否
- **速率/额度（摘要）**: Often ~1 concurrent on free Flash models (verify)
- **商业使用**: `restricted` · **数据用途**: 未知
- **示例模型**: `glm-4.7-flash`, `glm-4.6v-flash`
- **说明**: 提供永久免费模型（如 GLM Flash 系列），并发/配额以控制台为准；国际站可能有不同入口。
- **上次核对**: `2026-07-15`

## 主流推理平台

### Cerebras Inference

- **类型**: 推理平台 · **地区**: US · **状态**: ✅ active
- **官网**: https://cloud.cerebras.ai/
- **文档**: https://inference-docs.cerebras.ai/
- **获取 Key**: https://cloud.cerebras.ai/
- **Base URL**: `https://api.cerebras.ai/v1`
- **OpenAI 兼容**: 是 · **需绑卡**: 否 · **手机验证**: 否
- **速率/额度（摘要）**: e.g. gpt-oss-120b: ~30 RPM, ~14.4K RPD, ~1M TPD (verify)
- **商业使用**: `yes` · **数据用途**: 通常不用于训练
- **示例模型**: `gpt-oss-120b`, `llama3.1-8b`
- **说明**: 晶圆级芯片推理，速度极高；免费档模型列表与上下文上限可能变动（曾出现免费上下文封顶）。
- **上次核对**: `2026-07-15`

### Cloudflare Workers AI

- **类型**: 推理平台 · **地区**: US · **状态**: ✅ active
- **官网**: https://developers.cloudflare.com/workers-ai/
- **文档**: https://developers.cloudflare.com/workers-ai/
- **获取 Key**: https://dash.cloudflare.com/profile/api-tokens
- **Base URL**: `https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run`
- **OpenAI 兼容**: 否 · **需绑卡**: 否 · **手机验证**: 否
- **速率/额度（摘要）**: ~10,000 neurons/day shared across models
- **商业使用**: `yes` · **数据用途**: 未知
- **示例模型**: `@cf/meta/llama-3.3-70b-instruct-fp8-fast`, `@cf/meta/llama-4-scout-17b-16e-instruct`, `@cf/openai/gpt-oss-120b`, `@cf/qwen/qwen3-30b-a3b-fp8`
- **说明**: 每日 Neurons 免费额度（如 10,000 neurons/day）；模型目录丰富。
- **上次核对**: `2026-07-15`

### GitHub Models

- **类型**: 推理平台 · **地区**: US · **状态**: ✅ active
- **官网**: https://github.com/marketplace/models
- **文档**: https://docs.github.com/en/github-models
- **获取 Key**: https://github.com/settings/tokens
- **Base URL**: `https://models.github.ai/inference`
- **OpenAI 兼容**: 是 · **需绑卡**: 否 · **手机验证**: 否
- **速率/额度（摘要）**: Tier-based RPM/RPD (e.g. free often ~10–15 RPM / ~50–150 RPD class)
- **商业使用**: `restricted` · **数据用途**: 未知
- **示例模型**: `openai/gpt-4.1-mini`, `meta/Llama-3.3-70B-Instruct`, `deepseek/DeepSeek-R1`, `mistral-ai/Mistral-Small-3.1`
- **说明**: 面向原型开发；限额与 Copilot 订阅档位相关；单次输入/输出 token 上限较紧。
- **上次核对**: `2026-07-15`

### Groq

- **类型**: 推理平台 · **地区**: US · **状态**: ✅ active
- **官网**: https://console.groq.com
- **文档**: https://console.groq.com/docs
- **获取 Key**: https://console.groq.com/keys
- **Base URL**: `https://api.groq.com/openai/v1`
- **OpenAI 兼容**: 是 · **需绑卡**: 否 · **手机验证**: 否
- **速率/额度（摘要）**: Model-dependent; e.g. ~30 RPM, ~1K–14K RPD, TPM in thousands–tens of thousands
- **商业使用**: `yes` · **数据用途**: 通常不用于训练
- **示例模型**: `llama-3.3-70b-versatile`, `llama-3.1-8b-instant`, `openai/gpt-oss-120b`, `qwen/qwen3-32b`
- **说明**: LPU 超快推理；免费档有 RPM/TPM/RPD 限制，大模型 RPD 通常更紧。
- **上次核对**: `2026-07-15`

### Hugging Face Inference Providers

- **类型**: 推理平台 · **地区**: US · **状态**: ✅ active
- **官网**: https://huggingface.co
- **文档**: https://huggingface.co/docs/inference-providers
- **获取 Key**: https://huggingface.co/settings/tokens
- **Base URL**: `https://router.huggingface.co/v1`
- **OpenAI 兼容**: 是 · **需绑卡**: 否 · **手机验证**: 否
- **速率/额度（摘要）**: Credit-metered monthly free allocation
- **商业使用**: `restricted` · **数据用途**: 未知
- **示例模型**: `meta-llama/Meta-Llama-3.1-8B-Instruct`, `mistralai/Mistral-7B-Instruct-v0.3`, `Qwen/Qwen2.5-7B-Instruct`
- **说明**: 免费用户每月有小额 Inference Provider 额度（如约 $0.10 量级）；路由到多家后端。
- **上次核对**: `2026-07-15`

### LLM7.io

- **类型**: 推理平台 · **地区**: GB · **状态**: ⚠️ limited
- **官网**: https://llm7.io
- **文档**: https://llm7.io
- **获取 Key**: https://token.llm7.io
- **Base URL**: `https://api.llm7.io/v1`
- **OpenAI 兼容**: 是 · **需绑卡**: 否 · **手机验证**: 否
- **速率/额度（摘要）**: ~30 RPM default; ~120 RPM with token
- **商业使用**: `unknown` · **数据用途**: 未知
- **示例模型**: `gemini-2.5-flash-lite`, `mistral-small-3.1-24b`, `qwen2.5-coder-32b`
- **说明**: 低门槛网关；基础访问可无注册；有 token 时限额更高。第三方聚合，稳定性/合规请自行评估。
- **上次核对**: `2026-07-15`

### 魔搭 ModelScope API-Inference

- **类型**: 推理平台 · **地区**: CN · **状态**: ✅ active
- **官网**: https://modelscope.cn
- **文档**: https://modelscope.cn/docs/model-service/API-Inference/intro
- **获取 Key**: https://modelscope.cn/my/myaccesstoken
- **Base URL**: `https://api-inference.modelscope.cn/v1`
- **OpenAI 兼容**: 是 · **需绑卡**: 否 · **手机验证**: 是
- **速率/额度（摘要）**: e.g. ~2,000 RPD total, per-model cap ~500 RPD (dynamic)
- **商业使用**: `restricted` · **数据用途**: 未知
- **示例模型**: `Qwen/Qwen3.5-35B-A3B`, `Qwen/Qwen3.5-27B`
- **说明**: 注册用户 API-Inference 免费；通常需绑定阿里云账号与实名；日配额动态调整。
- **上次核对**: `2026-07-15`

### NVIDIA NIM

- **类型**: 推理平台 · **地区**: US · **状态**: ✅ active
- **官网**: https://build.nvidia.com/explore/discover
- **文档**: https://docs.api.nvidia.com/
- **获取 Key**: https://build.nvidia.com/
- **Base URL**: `https://integrate.api.nvidia.com/v1`
- **OpenAI 兼容**: 是 · **需绑卡**: 否 · **手机验证**: 是
- **速率/额度（摘要）**: ~40 RPM (typical free); no simple public daily token cap
- **商业使用**: `restricted` · **数据用途**: 未知
- **示例模型**: `meta/llama-3.1-405b-instruct`, `deepseek-ai/deepseek-r1`, `nvidia/nemotron-3-super-120b-a12b`, `qwen/qwen2.5-72b-instruct`
- **说明**: NVIDIA Developer 计划免费调用；通常需手机验证；上下文窗口可能受限。
- **上次核对**: `2026-07-15`

### Ollama Cloud

- **类型**: 推理平台 · **地区**: US · **状态**: ✅ active
- **官网**: https://ollama.com
- **文档**: https://docs.ollama.com/cloud
- **获取 Key**: https://ollama.com/settings/keys
- **Base URL**: `https://api.ollama.com`
- **OpenAI 兼容**: 否 · **需绑卡**: 否 · **手机验证**: 否
- **速率/额度（摘要）**: Session/weekly qualitative limits (unpublished exact numbers)
- **商业使用**: `restricted` · **数据用途**: 未知
- **示例模型**: `gpt-oss:120b-cloud`, `deepseek-r1:cloud`, `qwen3-coder:480b-cloud`
- **说明**: 有免费轻量使用档；限额偏会话/周级且文档不一定公开具体数字；API 为 Ollama 协议，非标准 OpenAI SDK。
- **上次核对**: `2026-07-15`

### OpenRouter（免费模型）

- **类型**: 推理平台 · **地区**: US · **状态**: ✅ active
- **官网**: https://openrouter.ai
- **文档**: https://openrouter.ai/docs
- **获取 Key**: https://openrouter.ai/keys
- **Base URL**: `https://openrouter.ai/api/v1`
- **OpenAI 兼容**: 是 · **需绑卡**: 否 · **手机验证**: 否
- **速率/额度（摘要）**: e.g. ~20 RPM, ~50–200 RPD default; up to ~1000 RPD after $10 lifetime top-up
- **商业使用**: `restricted` · **数据用途**: 可能用于训练/改进
- **示例模型**: `qwen/qwen3-coder:free`, `meta-llama/llama-3.3-70b-instruct:free`, `openai/gpt-oss-20b:free`, `google/gemma-4-31b-it:free`
- **说明**: 仅统计 `:free` 模型；无余额也可调用免费模型。免费路由可能记录提示词。充值一定金额可提高免费模型日限额。
- **上次核对**: `2026-07-15`

### OVHcloud AI Endpoints

- **类型**: 推理平台 · **地区**: EU · **状态**: ✅ active
- **官网**: https://www.ovhcloud.com/en/public-cloud/ai-endpoints/
- **文档**: https://help.ovhcloud.com/csm/en-public-cloud-ai-endpoints
- **获取 Key**: https://www.ovhcloud.com/en/public-cloud/ai-endpoints/catalog/
- **Base URL**: `https://oai.endpoints.kepler.ai.cloud.ovh.net/v1`
- **OpenAI 兼容**: 是 · **需绑卡**: 否 · **手机验证**: 否
- **速率/额度（摘要）**: Anonymous ~2 RPM/IP/model; authenticated higher (paid)
- **商业使用**: `yes` · **数据用途**: 未知
- **示例模型**: `Meta-Llama-3_3-70B-Instruct`, `gpt-oss-120b`, `Mistral-Small-3.2-24B-Instruct`, `Qwen3-Coder-30B-A3B-Instruct`
- **说明**: 匿名免费档：无需注册/Key，按 IP 限流（约 2 RPM/模型）；更高额度需账号计费。数据在欧盟机房。
- **上次核对**: `2026-07-15`

### SambaNova Cloud

- **类型**: 推理平台 · **地区**: US · **状态**: ✅ active
- **官网**: https://cloud.sambanova.ai/
- **文档**: https://docs.sambanova.ai/
- **获取 Key**: https://cloud.sambanova.ai/apis
- **Base URL**: `https://api.sambanova.ai/v1`
- **OpenAI 兼容**: 是 · **需绑卡**: 否 · **手机验证**: 否
- **速率/额度（摘要）**: ~20 RPM, ~20 RPD, ~200K TPD per model (verify)
- **商业使用**: `yes` · **数据用途**: 未知
- **示例模型**: `Meta-Llama-3.3-70B-Instruct`, `DeepSeek-V3.1`, `gpt-oss-120b`
- **说明**: 有持续免费档（RPM/RPD/TPD）；新用户可能另有试用额度（试用不算收录标准，但免费档本身持续）。
- **上次核对**: `2026-07-15`

### 硅基流动 SiliconFlow

- **类型**: 推理平台 · **地区**: CN · **状态**: ✅ active
- **官网**: https://siliconflow.cn
- **文档**: https://docs.siliconflow.cn/
- **获取 Key**: https://cloud.siliconflow.cn/account/ak
- **Base URL**: `https://api.siliconflow.cn/v1`
- **OpenAI 兼容**: 是 · **需绑卡**: 否 · **手机验证**: 否
- **速率/额度（摘要）**: e.g. free models ~30 RPM / ~60K TPM class (verify)
- **商业使用**: `restricted` · **数据用途**: 未知
- **示例模型**: `Qwen/Qwen3-8B`, `deepseek-ai/DeepSeek-R1-Distill-Qwen-7B`
- **说明**: 部分模型永久免费；大量模型为付费。OpenAI 兼容接口。
- **上次核对**: `2026-07-15`

### Vercel AI Gateway

- **类型**: 推理平台 · **地区**: US · **状态**: ✅ active
- **官网**: https://vercel.com/docs/ai-gateway
- **文档**: https://vercel.com/docs/ai-gateway
- **获取 Key**: https://vercel.com/account/tokens
- **Base URL**: `—`
- **OpenAI 兼容**: 是 · **需绑卡**: 否 · **手机验证**: 否
- **速率/额度（摘要）**: Monthly free credit allowance
- **商业使用**: `yes` · **数据用途**: 未知
- **示例模型**: `various-via-gateway`
- **说明**: 网关路由到多家提供商；每月有免费额度（如约 $5/月量级，以官网定价页为准）。
- **上次核对**: `2026-07-15`

## 快速开始示例

多数 OpenAI 兼容接口可如下调用（以 Groq 为例）：

```bash
export OPENAI_API_KEY=gsk_xxx
export OPENAI_BASE_URL=https://api.groq.com/openai/v1

curl "$OPENAI_BASE_URL/chat/completions" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"llama-3.1-8b-instant","messages":[{"role":"user","content":"hello"}]}'
```

## 如何贡献

见 [CONTRIBUTING.md](./CONTRIBUTING.md)。

1. 编辑 `data/providers.yaml`
2. 运行 `python scripts/validate.py`
3. 运行 `python scripts/generate_readme.py`
4. 提交 PR（勿手改生成的 README）

## 与同类项目的差异

| 项目 | 差异 |
| --- | --- |
| [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | 更全，含试用额度；本仓库**只收永久免费**并提供 YAML SSOT + 中英双语 |
| [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | Awesome 列表风格；本仓库强调 schema 校验与可生成 README |

致谢上述社区整理工作。

## 维护

```bash
pip install -r requirements.txt
python scripts/validate.py
python scripts/generate_readme.py
```

## License

[MIT](./LICENSE)
