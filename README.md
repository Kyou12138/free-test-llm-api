# free-test-llm-api

**不用申请个人 Key** 的免费测试 LLM 接口（Key 为空，或官方固定匿名 Key）。

来源：GitHub 项目文档 / 社区聚合器（如 [freellmapi](https://github.com/tashfeenahmed/freellmapi)、[ob-1](https://github.com/Overbrilliant/ob-1)）+ 实测。

> 仅供测试。接口随时可能挂/限流。国内多数要代理。

---

## 1. Page Agent（国内）

- 源：https://github.com/alibaba/page-agent  
- 文档：https://alibaba.github.io/page-agent/docs/features/models/#free-testing-api  
- Key：**无**  
- 限制：校验 system prompt，给 Page Agent 评估用

```env
OPENAI_BASE_URL=https://page-ag-testing-ohftxirgbn.cn-shanghai.fcapp.run
OPENAI_API_KEY=
OPENAI_MODEL=qwen3.5-plus
```

模型：`qwen3.5-plus` · `qwen3.5-flash`

---

## 2. OVHcloud 匿名

- 社区引用：[freellmapi](https://github.com/tashfeenahmed/freellmapi) / [ob-1](https://github.com/Overbrilliant/ob-1)  
- Key：**无**（别填假 Key，会 403）  
- 约 2 RPM / IP / 模型 · 欧盟

```env
OPENAI_BASE_URL=https://oai.endpoints.kepler.ai.cloud.ovh.net/v1
OPENAI_API_KEY=
OPENAI_MODEL=gpt-oss-20b
```

模型示例：`gpt-oss-20b` · `gpt-oss-120b` · `Meta-Llama-3_3-70B-Instruct` · `Qwen3-32B` · `Qwen3.6-27B`

```bash
curl https://oai.endpoints.kepler.ai.cloud.ovh.net/v1/models
```

---

## 3. Pollinations

- 社区引用：freellmapi / ob-1  
- Key：**无**  
- 匿名模型：`openai-fast`（别名 `openai`）

```env
OPENAI_BASE_URL=https://text.pollinations.ai/openai/v1
OPENAI_API_KEY=
OPENAI_MODEL=openai-fast
```

---

## 4. Kilo Gateway（GitHub 标注 keyless）

- 源：freellmapi / ob-1 注册为 `keyless: true`  
- Key：**无**  
- 实测 `openrouter/free`、`kilo-auto/free` 可用；带 `:free` 的模型会下线

```env
OPENAI_BASE_URL=https://api.kilo.ai/api/gateway/v1
OPENAI_API_KEY=
OPENAI_MODEL=kilo-auto/free
```

也可用：

```env
OPENAI_MODEL=openrouter/free
```

查模型：

```bash
curl https://api.kilo.ai/api/gateway/models
```

---

## 5. LLM7（部分模型匿名）

- 源：freellmapi 写 “anonymous works for basic models”  
- 实测：**无 Key 时** `gemma3:27b`、`codestral-latest` 可通；多数模型要 Key  
- 国内可能要代理

```env
OPENAI_BASE_URL=https://api.llm7.io/v1
OPENAI_API_KEY=
OPENAI_MODEL=gemma3:27b
```

或：

```env
OPENAI_MODEL=codestral-latest
```

---

## 6. AI Horde（固定匿名 Key）

- 源：https://github.com/Haidra-Org/AI-Horde · 代理 https://oai.aihorde.net/  
- Key：**固定** `0000000000`（最低优先级）  
- `max_tokens` ≥ 16 · 模型列表常变 · 较慢

```env
OPENAI_BASE_URL=https://oai.aihorde.net/v1
OPENAI_API_KEY=0000000000
OPENAI_MODEL=koboldcpp/Llama-3.2-3B
```

```bash
curl https://oai.aihorde.net/v1/models -H "Authorization: Bearer 0000000000"
```

---

## 速查

| 名称 | Base URL | Key | 示例 Model | 国内 |
| --- | --- | --- | --- | --- |
| Page Agent | `…fcapp.run` | 无 | `qwen3.5-plus` | ✅ 限评估 |
| OVH | `…ovh.net/v1` | 无 | `gpt-oss-20b` | ⚠️ 代理 |
| Pollinations | `text.pollinations.ai/openai/v1` | 无 | `openai-fast` | ⚠️ 代理 |
| Kilo | `api.kilo.ai/api/gateway/v1` | 无 | `kilo-auto/free` | ⚠️ 代理 |
| LLM7 | `api.llm7.io/v1` | 无* | `gemma3:27b` | ⚠️ 代理 |
| AI Horde | `oai.aihorde.net/v1` | `0000000000` | `koboldcpp/Llama-3.2-3B` | ⚠️ 代理 |

\*LLM7 仅部分模型可匿名。

---

## 一键测试

```bash
# Kilo 免 Key
curl "https://api.kilo.ai/api/gateway/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -d '{"model":"kilo-auto/free","messages":[{"role":"user","content":"你好"}],"max_tokens":64}'
```

```bash
# OVH 免 Key
curl "https://oai.endpoints.kepler.ai.cloud.ovh.net/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-oss-20b","messages":[{"role":"user","content":"你好"}],"max_tokens":64}'
```

---

## GitHub 上还看到但未收录的

| 类型 | 例子 | 为何不收 |
| --- | --- | --- |
| 要注册领个人 Key | Groq / Gemini / OpenRouter / 硅基流动 | 不符合「免申请」 |
| 自建反代聊天网页 | [keyless-gpt-wrapper-api](https://github.com/callbacked/keyless-gpt-wrapper-api) 等 | 本地自建 + 非官方接口，不是公开测试口 |
| 聚合器（自己填各家 Key） | [freellmapi](https://github.com/tashfeenahmed/freellmapi) | 它是路由工具，不是端点本身 |
| Telegram 领 Key | 各类 Free GPT API 仓库 | 仍要领个人 Key |

参考列表（多数是「免费 Key」不是「免 Key」）：

- https://github.com/cheahjs/free-llm-api-resources  
- https://github.com/mnfst/awesome-free-llm-apis  
- https://github.com/tashfeenahmed/freellmapi  

---

## 数据

[`apis.json`](./apis.json)

## License

[MIT](./LICENSE)
