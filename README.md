# free-test-llm-api

**免注册、免申请 Key**（或 Key 可留空）的免费测试 LLM 接口。  
复制就能调。仅供技术测试，勿上生产。

---

## 1. Page Agent 测试接口（国内）

- 文档：https://alibaba.github.io/page-agent/docs/features/models/#free-testing-api  
- **无需 Key**  
- 注意：校验官方 system prompt，主要给 Page Agent 评估用，**不是通用聊天**

```env
OPENAI_BASE_URL=https://page-ag-testing-ohftxirgbn.cn-shanghai.fcapp.run
OPENAI_API_KEY=
OPENAI_MODEL=qwen3.5-plus
```

可用模型：`qwen3.5-plus` · `qwen3.5-flash`

---

## 2. OVHcloud 匿名端点（无需 Key）

- 目录：https://www.ovhcloud.com/en/public-cloud/ai-endpoints/catalog/  
- **无需注册、无需 Key**  
- 约 2 RPM / IP / 模型  
- 服务器在欧盟，**国内可能需代理**

```env
OPENAI_BASE_URL=https://oai.endpoints.kepler.ai.cloud.ovh.net/v1
OPENAI_API_KEY=
OPENAI_MODEL=gpt-oss-20b
```

可用模型（节选）：

```text
gpt-oss-20b
gpt-oss-120b
Meta-Llama-3_3-70B-Instruct
Mistral-Small-3.2-24B-Instruct-2506
Qwen3-32B
Qwen3-Coder-30B-A3B-Instruct
Qwen3.5-9B
Qwen3.5-397B-A17B
Qwen3.6-27B
```

查全量：

```bash
curl https://oai.endpoints.kepler.ai.cloud.ovh.net/v1/models
```

---

## 3. Pollinations（无需 Key）

- 站点：https://pollinations.ai/  
- **无需 Key** 可调 OpenAI 兼容接口  
- 国际节点，**国内可能需代理**；稳定性不保证

```env
OPENAI_BASE_URL=https://text.pollinations.ai/v1
OPENAI_API_KEY=
OPENAI_MODEL=openai
```

或：

```env
OPENAI_BASE_URL=https://text.pollinations.ai/openai
OPENAI_API_KEY=
OPENAI_MODEL=openai
```

模型名以他们当前开放列表为准，常见可试 `openai`。

---

## 调用示例（复制即测）

```bash
export OPENAI_BASE_URL=https://oai.endpoints.kepler.ai.cloud.ovh.net/v1
export OPENAI_MODEL=gpt-oss-20b

curl "$OPENAI_BASE_URL/chat/completions" \
  -H "Content-Type: application/json" \
  -d "{\"model\":\"$OPENAI_MODEL\",\"messages\":[{\"role\":\"user\",\"content\":\"你好\"}],\"max_tokens\":64}"
```

Python：

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://oai.endpoints.kepler.ai.cloud.ovh.net/v1",
    api_key="not-needed",  # 无 Key 时随便填非空占位；部分端点可留空
)
print(client.chat.completions.create(
    model="gpt-oss-20b",
    messages=[{"role": "user", "content": "你好"}],
).choices[0].message.content)
```

> 说明：有的 SDK 强制 `api_key` 非空，可写 `not-needed` / `sk-no-key`；  
> OVH 实测：**不带 Authorization** 或 `Bearer ` 空串可以，**假 Key 反而 403**。

---

## 速查（全是测试口，不用去领 Key）

| 名称 | Base URL | Key | Model 示例 | 国内 |
| --- | --- | --- | --- | --- |
| Page Agent | `https://page-ag-testing-ohftxirgbn.cn-shanghai.fcapp.run` | 无 | `qwen3.5-plus` | ✅ 直连（限 Page Agent） |
| OVH 匿名 | `https://oai.endpoints.kepler.ai.cloud.ovh.net/v1` | 无 | `gpt-oss-20b` | ⚠️ 可能需代理 |
| Pollinations | `https://text.pollinations.ai/v1` | 无 | `openai` | ⚠️ 可能需代理 |

---

## 不收录

- 要去官网注册才能领个人 Key 的（硅基流动、智谱、百炼、DeepSeek…）
- 非官方盗 Key / 反代共享站
- 不能 OpenAI 兼容、无法直接复制调用的纯网页

---

## 数据文件

[`apis.json`](./apis.json)

## License

[MIT](./LICENSE)
