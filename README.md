# free-test-llm-api

**Demo / 测试类** 免费 LLM 接口：不用去官网申请个人 Key（Key 为空，或文档写死的固定 Key）。

> 仅供试用/评估。随时可能挂、限流。勿上生产。

---

## 一、项目官方 Demo（和 Page Agent 一类）

开源项目为**自己产品演示**挂的测试代理。

### 1. Page Agent（国内）

- 项目：https://github.com/alibaba/page-agent  
- 文档：https://alibaba.github.io/page-agent/docs/features/models/#free-testing-api  
- Key：**无**  
- 用途：评估 Page Agent；有 system prompt 限制  

```env
OPENAI_BASE_URL=https://page-ag-testing-ohftxirgbn.cn-shanghai.fcapp.run
OPENAI_API_KEY=
OPENAI_MODEL=qwen3.5-plus
```

模型：`qwen3.5-plus` · `qwen3.5-flash`

---

### 2. LangChain4j Demo（固定 Key = `demo`）

- 项目：https://github.com/langchain4j/langchain4j  
- 文档：https://docs.langchain4j.dev/get-started  
- 官方写明：`apiKey = "demo"` 时走他们的体验代理  
- 实测可用（偶发 502）  
- 模型基本只有 **`gpt-4o-mini`**  
- 注意文档用的是 **http**（不是 https）

```env
OPENAI_BASE_URL=http://langchain4j.dev/demo/openai/v1
OPENAI_API_KEY=demo
OPENAI_MODEL=gpt-4o-mini
```

```bash
curl "http://langchain4j.dev/demo/openai/v1/chat/completions" \
  -H "Authorization: Bearer demo" \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-4o-mini","messages":[{"role":"user","content":"你好"}],"max_tokens":64}'
```

---

## 二、匿名公共测试口（不是某项目 Demo，但免申请 Key）

| 名称 | Base URL | Key | 示例 Model |
| --- | --- | --- | --- |
| OVH 匿名 | `https://oai.endpoints.kepler.ai.cloud.ovh.net/v1` | 无 | `gpt-oss-20b` |
| Pollinations | `https://text.pollinations.ai/openai/v1` | 无 | `openai-fast` |
| Kilo Gateway | `https://api.kilo.ai/api/gateway/v1` | 无 | `kilo-auto/free` |
| LLM7（部分模型） | `https://api.llm7.io/v1` | 无 | `gemma3:27b` |
| AI Horde | `https://oai.aihorde.net/v1` | 固定 `0000000000` | `koboldcpp/Llama-3.2-3B` |

### OVH

```env
OPENAI_BASE_URL=https://oai.endpoints.kepler.ai.cloud.ovh.net/v1
OPENAI_API_KEY=
OPENAI_MODEL=gpt-oss-20b
```

### Pollinations

```env
OPENAI_BASE_URL=https://text.pollinations.ai/openai/v1
OPENAI_API_KEY=
OPENAI_MODEL=openai-fast
```

### Kilo

```env
OPENAI_BASE_URL=https://api.kilo.ai/api/gateway/v1
OPENAI_API_KEY=
OPENAI_MODEL=kilo-auto/free
```

### LLM7（仅部分模型可匿名）

```env
OPENAI_BASE_URL=https://api.llm7.io/v1
OPENAI_API_KEY=
OPENAI_MODEL=gemma3:27b
```

另可试：`codestral-latest`

### AI Horde

```env
OPENAI_BASE_URL=https://oai.aihorde.net/v1
OPENAI_API_KEY=0000000000
OPENAI_MODEL=koboldcpp/Llama-3.2-3B
```

（`max_tokens` 建议 ≥ 16）

---

## 速查

| 类型 | 名称 | Key | 国内 | 备注 |
| --- | --- | --- | --- | --- |
| 项目 Demo | **Page Agent** | 无 | ✅ | 限评估 |
| 项目 Demo | **LangChain4j** | 固定 `demo` | ⚠️ | 仅 gpt-4o-mini，偶发 502 |
| 匿名公共 | OVH | 无 | ⚠️ 代理 | 通用聊天 |
| 匿名公共 | Pollinations | 无 | ⚠️ 代理 | |
| 匿名公共 | Kilo | 无 | ⚠️ 代理 | |
| 匿名公共 | LLM7 | 无* | ⚠️ 代理 | 仅部分模型 |
| 匿名公共 | AI Horde | `0000000000` | ⚠️ 代理 | 慢、模型会变 |

---

## GitHub 上找 demo/测试类的结论

| 找到什么 | 说明 |
| --- | --- |
| **Page Agent** | 最标准的「项目官方免费测试代理」 |
| **LangChain4j Demo** | 同类：官方文档写死的体验 URL + Key=`demo` |
| 大量 fork / Hermes skill | 都在**复用** Page Agent 那条 URL，不是新接口 |
| freellmapi / awesome 列表 | 多数是「注册领 free tier」，不是项目 Demo |
| keyless-gpt-wrapper 等 | 要自建，反代网页聊天，不算官方测试口 |

**真正「项目官方 Demo 测试口」目前就明确 2 个：Page Agent + LangChain4j。**  
其它是匿名公共接口，形态不同。

---

## 数据

[`apis.json`](./apis.json)

## License

[MIT](./LICENSE)
