# 免费测试 LLM API

> 收集 **可直接粘贴使用** 的免费测试接口：`LLM_BASE_URL` + `LLM_MODEL_NAME`
>
> 形态对齐 [Page Agent · Free Testing API](https://alibaba.github.io/page-agent/docs/features/models/#free-testing-api)

[English](./README.en.md) · 数据源 [`data/endpoints.yaml`](./data/endpoints.yaml) · 更新：`2026-07-15`

## 这是什么 / 不是什么

| ✅ 我们收录 | ❌ 我们不收录 |
| --- | --- |
| 开源项目为 Demo 提供的 **官方测试接口** | 非官方反代 / 盗 Key / 爬聊天网页 |
| **无需注册** 的公开免费端点 | 仅有网页 Chat、没有 HTTP API |
| 零成本拿 Key 就能测的 **OpenAI 兼容** 端点 | 纯营销「送额度」却无稳定测试入口说明 |
| 每条都给出 **可复制 env** | 生产级 SLA 承诺（我们不承诺） |

**定位**：免费测试用 LLM API 端点（BASE_URL + MODEL 可复制），非「注册领永久 free tier」平台清单。

**免责声明**：多数端点仅供技术评估；可能随时限流、变更或下线。禁止生产、禁止输入敏感数据。请遵守各项目使用条款。

## 总览（11）

| 名称 | 类别 | 地区 | 需 Key | OpenAI 兼容 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- | --- |
| [Page Agent 免费测试接口（通义千问）](https://alibaba.github.io/page-agent/docs/features/models/#free-testing-api) | `项目 Demo` | CN | 否 | 是 | ✅ active | [docs](https://alibaba.github.io/page-agent/docs/features/models/#free-testing-api) |
| [OVHcloud AI Endpoints（匿名免费）](https://www.ovhcloud.com/en/public-cloud/ai-endpoints/catalog/) | `匿名公开` | EU | 否 | 是 | ✅ active | [docs](https://www.ovhcloud.com/en/public-cloud/ai-endpoints/catalog/) |
| [Cerebras 免费推理](https://inference-docs.cerebras.ai/) | `免费 Token` | US | 是 | 是 | ✅ active | [docs](https://inference-docs.cerebras.ai/) |
| [GitHub Models](https://docs.github.com/en/github-models) | `免费 Token` | US | 是 | 是 | ✅ active | [docs](https://docs.github.com/en/github-models) |
| [Google AI Studio（Gemini 免费）](https://ai.google.dev/gemini-api/docs) | `免费 Token` | US | 是 | 是 | ✅ active | [docs](https://ai.google.dev/gemini-api/docs) |
| [Groq 免费档](https://console.groq.com/docs) | `免费 Token` | US | 是 | 是 | ✅ active | [docs](https://console.groq.com/docs) |
| [LLM7.io](https://llm7.io) | `免费 Token` | GB | 是 | 是 | ✅ active | [docs](https://llm7.io) |
| [NVIDIA NIM（开发者免费）](https://docs.api.nvidia.com/) | `免费 Token` | US | 是 | 是 | ✅ active | [docs](https://docs.api.nvidia.com/) |
| [OpenRouter 免费模型（:free）](https://openrouter.ai/docs) | `免费 Token` | US | 是 | 是 | ✅ active | [docs](https://openrouter.ai/docs) |
| [硅基流动免费模型](https://docs.siliconflow.cn/) | `免费 Token` | CN | 是 | 是 | ✅ active | [docs](https://docs.siliconflow.cn/) |
| [智谱 Z.AI 免费 Flash 模型](https://docs.bigmodel.cn/) | `免费 Token` | CN | 是 | 是 | ✅ active | [docs](https://docs.bigmodel.cn/) |

## 调用示例（OpenAI 兼容）

以 **OVH 匿名端点**为例（无需 Key）：

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

## 开源项目官方测试接口（Demo / 技术评估）

### Page Agent 免费测试接口（通义千问）

- **类别**: `project_demo` · **提供方**: Alibaba page-agent maintainers (via Alibaba Cloud FC + BaiLian) · **地区**: CN
- **状态**: ✅ active · **上次核对**: `2026-07-15`
- **Base URL**: `https://page-ag-testing-ohftxirgbn.cn-shanghai.fcapp.run`
- **需 API Key**: 否
- **示例模型**: `qwen3.5-plus`, `qwen3.5-flash`
- **文档**: https://alibaba.github.io/page-agent/docs/features/models/#free-testing-api
- **仓库**: https://github.com/alibaba/page-agent
- **条款**: https://github.com/alibaba/page-agent/blob/main/docs/terms-and-privacy.md#2-testing-api-and-demo-disclaimer--terms-of-use

**可复制配置**

```bash
LLM_BASE_URL="https://page-ag-testing-ohftxirgbn.cn-shanghai.fcapp.run"
LLM_MODEL_NAME="qwen3.5-plus"
```

**限制与说明**

> 仅供 PageAgent.js / Extension 技术评估与 R&D。
> 禁止生产环境；禁止输入 PII/敏感数据；数据经中国大陆服务器处理。
> 代理会校验请求：首条需为 system/developer，且 system prompt 需匹配官方 page-agent 提示词（通用聊天可能被拒绝）。
> 可能随时限流或下线。

## 匿名公开端点（无需 Key）

### OVHcloud AI Endpoints（匿名免费）

- **类别**: `anonymous_public` · **提供方**: OVHcloud · **地区**: EU
- **状态**: ✅ active · **上次核对**: `2026-07-15`
- **Base URL**: `https://oai.endpoints.kepler.ai.cloud.ovh.net/v1`
- **需 API Key**: 否
- **示例模型**: `Meta-Llama-3_3-70B-Instruct`, `Llama-3.1-8B-Instruct`, `gpt-oss-120b`, `gpt-oss-20b`, `Qwen3-32B`, `Qwen3-Coder-30B-A3B-Instruct`, `Mistral-Small-3.2-24B-Instruct`, `Mistral-Nemo-Instruct-2407`, `Mistral-7B-Instruct-v0.3`
- **文档**: https://www.ovhcloud.com/en/public-cloud/ai-endpoints/catalog/
- **条款**: https://www.ovhcloud.com/en/terms-and-conditions/

**可复制配置**

```bash
LLM_BASE_URL="https://oai.endpoints.kepler.ai.cloud.ovh.net/v1"
LLM_MODEL_NAME="Meta-Llama-3_3-70B-Instruct"
```

**限制与说明**

> 匿名档：无需注册、无需 API Key；约 2 RPM / IP / 模型（以官网为准）。
> 适合联调 OpenAI SDK / Agent 工具；更高配额需 OVH 账号与计费项目。
> 模型托管在欧盟。模型列表可能变更，请用 GET /v1/models 确认。

## 免费 Token / 免费档（拿 Key 即可测）

### Cerebras 免费推理

- **类别**: `free_token` · **提供方**: Cerebras · **地区**: US
- **状态**: ✅ active · **上次核对**: `2026-07-15`
- **Base URL**: `https://api.cerebras.ai/v1`
- **需 API Key**: 是 · [获取 Key](https://cloud.cerebras.ai/)
- **示例模型**: `llama3.1-8b`, `gpt-oss-120b`
- **文档**: https://inference-docs.cerebras.ai/
- **条款**: https://www.cerebras.ai/terms-of-service

**可复制配置**

```bash
LLM_BASE_URL="https://api.cerebras.ai/v1"
LLM_MODEL_NAME="llama3.1-8b"
LLM_API_KEY="<https://cloud.cerebras.ai/>"
```

**限制与说明**

> 免费档 Key；超高吞吐，适合压测客户端与流式输出。
> 免费模型列表与上下文上限可能突然变更。

### GitHub Models

- **类别**: `free_token` · **提供方**: GitHub · **地区**: US
- **状态**: ✅ active · **上次核对**: `2026-07-15`
- **Base URL**: `https://models.github.ai/inference`
- **需 API Key**: 是 · [获取 Key](https://github.com/settings/tokens)
- **示例模型**: `openai/gpt-4.1-mini`, `openai/gpt-4o-mini`, `meta/Llama-3.3-70B-Instruct`, `deepseek/DeepSeek-R1`
- **文档**: https://docs.github.com/en/github-models
- **条款**: https://docs.github.com/en/site-policy

**可复制配置**

```bash
LLM_BASE_URL="https://models.github.ai/inference"
LLM_MODEL_NAME="openai/gpt-4.1-mini"
LLM_API_KEY="<GitHub PAT with models access>"
```

**限制与说明**

> 使用 GitHub Token（需 models 相关权限）即可原型测试。
> 限额与 Copilot 档位相关，单次输入输出上限较紧，适合功能验证。

### Google AI Studio（Gemini 免费）

- **类别**: `free_token` · **提供方**: Google · **地区**: US
- **状态**: ✅ active · **上次核对**: `2026-07-15`
- **Base URL**: `https://generativelanguage.googleapis.com/v1beta/openai`
- **需 API Key**: 是 · [获取 Key](https://aistudio.google.com/app/apikey)
- **示例模型**: `gemini-2.5-flash`, `gemini-2.5-flash-lite`, `gemini-2.0-flash`
- **文档**: https://ai.google.dev/gemini-api/docs
- **条款**: https://ai.google.dev/gemini-api/terms

**可复制配置**

```bash
LLM_BASE_URL="https://generativelanguage.googleapis.com/v1beta/openai"
LLM_MODEL_NAME="gemini-2.5-flash"
LLM_API_KEY="<https://aistudio.google.com/app/apikey>"
```

**限制与说明**

> AI Studio 可免费创建 API Key；部分地区无免费档。
> 免费层数据使用/地区限制请读官方条款；配额按模型变化。

### Groq 免费档

- **类别**: `free_token` · **提供方**: Groq · **地区**: US
- **状态**: ✅ active · **上次核对**: `2026-07-15`
- **Base URL**: `https://api.groq.com/openai/v1`
- **需 API Key**: 是 · [获取 Key](https://console.groq.com/keys)
- **示例模型**: `llama-3.1-8b-instant`, `llama-3.3-70b-versatile`, `openai/gpt-oss-20b`, `qwen/qwen3-32b`
- **文档**: https://console.groq.com/docs
- **条款**: https://groq.com/terms-of-use/

**可复制配置**

```bash
LLM_BASE_URL="https://api.groq.com/openai/v1"
LLM_MODEL_NAME="llama-3.1-8b-instant"
LLM_API_KEY="<https://console.groq.com/keys>"
```

**限制与说明**

> 控制台免费创建 Key，无需绑卡即可测；有 RPM/TPM/RPD 限制。
> 适合速度敏感的联调；模型与配额以官方 rate limits 页为准。

### LLM7.io

- **类别**: `free_token` · **提供方**: LLM7.io · **地区**: GB
- **状态**: ✅ active · **上次核对**: `2026-07-15`
- **Base URL**: `https://api.llm7.io/v1`
- **需 API Key**: 是 · [获取 Key](https://token.llm7.io)
- **示例模型**: `deepseek-v4-flash`, `gemma3:27b`, `gpt-5.4-mini`, `kimi-k2.6`, `minimax-m2.7`
- **文档**: https://llm7.io
- **条款**: https://llm7.io

**可复制配置**

```bash
LLM_BASE_URL="https://api.llm7.io/v1"
LLM_MODEL_NAME="deepseek-v4-flash"
LLM_API_KEY="<get free token at https://token.llm7.io>"
```

**限制与说明**

> 可免费领取 token；基础访问与限额以官网为准（有 token 通常更高 RPM）。
> 第三方聚合网关，稳定性/合规/数据路径请自行评估；模型可用性会变。
> 适合快速打通 OpenAI 兼容客户端做联调测试。

### NVIDIA NIM（开发者免费）

- **类别**: `free_token` · **提供方**: NVIDIA · **地区**: US
- **状态**: ✅ active · **上次核对**: `2026-07-15`
- **Base URL**: `https://integrate.api.nvidia.com/v1`
- **需 API Key**: 是 · [获取 Key](https://build.nvidia.com/)
- **示例模型**: `meta/llama-3.1-8b-instruct`, `microsoft/phi-3-mini-4k-instruct`, `google/gemma-2-9b-it`
- **文档**: https://docs.api.nvidia.com/
- **条款**: https://www.nvidia.com/en-us/about-nvidia/privacy-policy/

**可复制配置**

```bash
LLM_BASE_URL="https://integrate.api.nvidia.com/v1"
LLM_MODEL_NAME="meta/llama-3.1-8b-instruct"
LLM_API_KEY="<https://build.nvidia.com/>"
```

**限制与说明**

> NVIDIA Developer 计划可免费调用部分模型；通常需注册/验证。
> 有速率限制，上下文可能较短，适合模型摸底测试。

### OpenRouter 免费模型（:free）

- **类别**: `free_token` · **提供方**: OpenRouter · **地区**: US
- **状态**: ✅ active · **上次核对**: `2026-07-15`
- **Base URL**: `https://openrouter.ai/api/v1`
- **需 API Key**: 是 · [获取 Key](https://openrouter.ai/keys)
- **示例模型**: `openrouter/free`, `meta-llama/llama-3.3-70b-instruct:free`, `qwen/qwen3-coder:free`, `openai/gpt-oss-20b:free`, `google/gemma-4-31b-it:free`
- **文档**: https://openrouter.ai/docs
- **条款**: https://openrouter.ai/terms

**可复制配置**

```bash
LLM_BASE_URL="https://openrouter.ai/api/v1"
LLM_MODEL_NAME="openrouter/free"
LLM_API_KEY="<https://openrouter.ai/keys>"
```

**限制与说明**

> 注册即可拿 Key；调用模型名带 `:free` 后缀的免费模型（或 free router）。
> 默认日请求限额较低；免费路由可能记录提示词。仅建议开发测试。

### 硅基流动免费模型

- **类别**: `free_token` · **提供方**: SiliconFlow · **地区**: CN
- **状态**: ✅ active · **上次核对**: `2026-07-15`
- **Base URL**: `https://api.siliconflow.cn/v1`
- **需 API Key**: 是 · [获取 Key](https://cloud.siliconflow.cn/account/ak)
- **示例模型**: `Qwen/Qwen3-8B`, `deepseek-ai/DeepSeek-R1-Distill-Qwen-7B`
- **文档**: https://docs.siliconflow.cn/
- **条款**: https://docs.siliconflow.cn/

**可复制配置**

```bash
LLM_BASE_URL="https://api.siliconflow.cn/v1"
LLM_MODEL_NAME="Qwen/Qwen3-8B"
LLM_API_KEY="<https://cloud.siliconflow.cn/account/ak>"
```

**限制与说明**

> 注册后创建 Key；部分模型永久免费，其余计费。
> 以控制台标注的免费模型为准，适合国内网络环境联调。

### 智谱 Z.AI 免费 Flash 模型

- **类别**: `free_token` · **提供方**: Zhipu / Z.AI · **地区**: CN
- **状态**: ✅ active · **上次核对**: `2026-07-15`
- **Base URL**: `https://open.bigmodel.cn/api/paas/v4`
- **需 API Key**: 是 · [获取 Key](https://open.bigmodel.cn/usercenter/apikeys)
- **示例模型**: `glm-4.7-flash`, `glm-4.6v-flash`
- **文档**: https://docs.bigmodel.cn/
- **条款**: https://open.bigmodel.cn/

**可复制配置**

```bash
LLM_BASE_URL="https://open.bigmodel.cn/api/paas/v4"
LLM_MODEL_NAME="glm-4.7-flash"
LLM_API_KEY="<https://open.bigmodel.cn/usercenter/apikeys>"
```

**限制与说明**

> 官方提供永久免费 Flash 类模型；并发/配额以控制台为准。
> 适合中文场景功能验证。

## 如何贡献

见 [CONTRIBUTING.md](./CONTRIBUTING.md)。

1. 在 `data/endpoints.yaml` 增加条目（必须有 `env.LLM_BASE_URL` + `env.LLM_MODEL_NAME`）
2. `python scripts/validate.py && python scripts/generate_readme.py`
3. 提交 PR，附上官网/文档链接与是否仅限技术评估的说明

## 参考形态

Page Agent 官方文档中的免费测试接口写法：

```bash
# qwen3.5-plus / qwen3.5-flash
LLM_BASE_URL="https://page-ag-testing-ohftxirgbn.cn-shanghai.fcapp.run"
LLM_MODEL_NAME="qwen3.5-plus"
```

来源：<https://alibaba.github.io/page-agent/docs/features/models/#free-testing-api>

## License

[MIT](./LICENSE)
