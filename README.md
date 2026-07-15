# free-test-llm-api

**不用去申请个人 Key** 的免费测试 LLM 接口（Key 为空，或文档公布的**固定匿名 Key**）。

> 这类接口本身就很少。下面都是能直接复制用的，仅供测试。

---

## 1. Page Agent（国内服务器）

文档：https://alibaba.github.io/page-agent/docs/features/models/#free-testing-api  

- 无需 Key  
- 国内可访问  
- 有 system prompt 限制，给 Page Agent 评估用，不是通用聊天

```env
OPENAI_BASE_URL=https://page-ag-testing-ohftxirgbn.cn-shanghai.fcapp.run
OPENAI_API_KEY=
OPENAI_MODEL=qwen3.5-plus
```

模型：`qwen3.5-plus` · `qwen3.5-flash`

---

## 2. OVHcloud 匿名（无需 Key）

目录：https://www.ovhcloud.com/en/public-cloud/ai-endpoints/catalog/  

- 无需注册、无需 Key  
- 约 2 次/分钟/IP/模型  
- 欧盟节点，**国内可能要代理**  
- 不要乱填假 Key（会 403），Key 留空即可

```env
OPENAI_BASE_URL=https://oai.endpoints.kepler.ai.cloud.ovh.net/v1
OPENAI_API_KEY=
OPENAI_MODEL=gpt-oss-20b
```

模型示例：

```text
gpt-oss-20b
gpt-oss-120b
Meta-Llama-3_3-70B-Instruct
Qwen3-32B
Qwen3-Coder-30B-A3B-Instruct
Qwen3.5-9B
Qwen3.6-27B
Mistral-Small-3.2-24B-Instruct-2506
```

```bash
curl https://oai.endpoints.kepler.ai.cloud.ovh.net/v1/models
```

---

## 3. Pollinations（无需 Key）

站点：https://pollinations.ai/  

- 无需 Key  
- 国际节点，**国内可能要代理**

```env
OPENAI_BASE_URL=https://text.pollinations.ai/v1
OPENAI_API_KEY=
OPENAI_MODEL=openai
```

也可：

```env
OPENAI_BASE_URL=https://text.pollinations.ai/openai
OPENAI_API_KEY=
OPENAI_MODEL=openai
```

---

## 4. AI Horde（固定匿名 Key）

文档：https://oai.aihorde.net/  

- 官方允许匿名 Key：`0000000000`（优先级最低、更慢）  
- 社区算力，模型随时上下线  
- **国内可能要代理**  
- `max_tokens` 建议 ≥ 16

```env
OPENAI_BASE_URL=https://oai.aihorde.net/v1
OPENAI_API_KEY=0000000000
OPENAI_MODEL=koboldcpp/Llama-3.2-3B
```

查当前模型：

```bash
curl https://oai.aihorde.net/v1/models -H "Authorization: Bearer 0000000000"
```

---

## 一键测试

```bash
# OVH 示例（无 Key）
curl "https://oai.endpoints.kepler.ai.cloud.ovh.net/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-oss-20b","messages":[{"role":"user","content":"你好"}],"max_tokens":64}'
```

```bash
# AI Horde 示例（固定 Key）
curl "https://oai.aihorde.net/v1/chat/completions" \
  -H "Authorization: Bearer 0000000000" \
  -H "Content-Type: application/json" \
  -d '{"model":"koboldcpp/Llama-3.2-3B","messages":[{"role":"user","content":"你好"}],"max_tokens":32}'
```

---

## 速查

| 名称 | Base URL | Key | 示例 Model | 国内 |
| --- | --- | --- | --- | --- |
| Page Agent | `…fcapp.run` | 无 | `qwen3.5-plus` | ✅（限评估） |
| OVH 匿名 | `…ovh.net/v1` | 无 | `gpt-oss-20b` | ⚠️ 可能代理 |
| Pollinations | `text.pollinations.ai/v1` | 无 | `openai` | ⚠️ 可能代理 |
| AI Horde | `oai.aihorde.net/v1` | **固定** `0000000000` | `koboldcpp/Llama-3.2-3B` | ⚠️ 可能代理 |

---

## 为什么这么少？

「免 Key / 固定 Key + OpenAI 兼容 + 还能长期公开」的官方测试口本来就极少：

- 厂商怕滥用，一般让你注册领个人 Key  
- 国内能直连的公开测试口，目前明确可用的主要是 **Page Agent**（且有用途限制）  
- 通用聊天免 Key：多在海外（OVH / Pollinations / Horde）

**不收录：** 注册领个人 Key、盗 Key、非官方反代。

有新的「免申请 / 固定 Key」接口欢迎 PR：改 `README.md` + `apis.json` 即可。

## License

[MIT](./LICENSE)
