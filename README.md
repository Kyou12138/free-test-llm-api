# free-test-llm-api

国内能用的 **免费测试 LLM API**（OpenAI 兼容）。

每条只记三样：**Base URL · Models · API Key 入口**。

> 仅供技术测试，不要上生产。配额会变，以官网为准。

---

## 国内直连（优先）

### 1. 硅基流动 SiliconFlow

| 字段 | 值 |
| --- | --- |
| **Base URL** | `https://api.siliconflow.cn/v1` |
| **API Key** | https://cloud.siliconflow.cn/account/ak |
| **Models** | `Qwen/Qwen3-8B` · `deepseek-ai/DeepSeek-R1-Distill-Qwen-7B`（控制台里标免费的模型） |

```bash
export OPENAI_BASE_URL=https://api.siliconflow.cn/v1
export OPENAI_API_KEY=sk-xxx
export OPENAI_MODEL=Qwen/Qwen3-8B
```

---

### 2. 智谱 Z.AI / BigModel

| 字段 | 值 |
| --- | --- |
| **Base URL** | `https://open.bigmodel.cn/api/paas/v4` |
| **API Key** | https://open.bigmodel.cn/usercenter/apikeys |
| **Models** | `glm-4.7-flash` · `glm-4-flash` · `glm-4.6v-flash`（免费 Flash 系列，以控制台为准） |

```bash
export OPENAI_BASE_URL=https://open.bigmodel.cn/api/paas/v4
export OPENAI_API_KEY=xxx
export OPENAI_MODEL=glm-4.7-flash
```

---

### 3. 魔搭 ModelScope

| 字段 | 值 |
| --- | --- |
| **Base URL** | `https://api-inference.modelscope.cn/v1` |
| **API Key** | https://modelscope.cn/my/myaccesstoken |
| **Models** | 开通了 API-Inference 的模型，如 `Qwen/Qwen2.5-7B-Instruct`（以魔搭页面为准） |

> 通常要绑阿里云 + 实名。有日请求限额。

```bash
export OPENAI_BASE_URL=https://api-inference.modelscope.cn/v1
export OPENAI_API_KEY=xxx
export OPENAI_MODEL=Qwen/Qwen2.5-7B-Instruct
```

---

### 4. 阿里云百炼 DashScope

| 字段 | 值 |
| --- | --- |
| **Base URL** | `https://dashscope.aliyuncs.com/compatible-mode/v1` |
| **API Key** | https://bailian.console.aliyun.com/ |
| **Models** | `qwen-plus` · `qwen-turbo` · `qwen-flash`（新用户常有免费额度） |

```bash
export OPENAI_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
export OPENAI_API_KEY=sk-xxx
export OPENAI_MODEL=qwen-turbo
```

---

### 5. Page Agent 免费测试接口（无需 Key）

| 字段 | 值 |
| --- | --- |
| **Base URL** | `https://page-ag-testing-ohftxirgbn.cn-shanghai.fcapp.run` |
| **API Key** | 不需要 |
| **Models** | `qwen3.5-plus` · `qwen3.5-flash` |

> 官方说明：仅供 [Page Agent](https://alibaba.github.io/page-agent/docs/features/models/#free-testing-api) 技术评估，有 system prompt 校验，**不是通用聊天接口**。

```bash
export OPENAI_BASE_URL=https://page-ag-testing-ohftxirgbn.cn-shanghai.fcapp.run
export OPENAI_MODEL=qwen3.5-plus
# 无需 OPENAI_API_KEY
```

---

### 6. DeepSeek

| 字段 | 值 |
| --- | --- |
| **Base URL** | `https://api.deepseek.com` |
| **API Key** | https://platform.deepseek.com/api_keys |
| **Models** | `deepseek-chat` · `deepseek-reasoner` |

> 新用户常有免费额度，用完需充值。国内可直连。

```bash
export OPENAI_BASE_URL=https://api.deepseek.com
export OPENAI_API_KEY=sk-xxx
export OPENAI_MODEL=deepseek-chat
```

---

## 速查表

| 名称 | Base URL | API Key | 示例 Model | 备注 |
| --- | --- | --- | --- | --- |
| 硅基流动 | `https://api.siliconflow.cn/v1` | [领取](https://cloud.siliconflow.cn/account/ak) | `Qwen/Qwen3-8B` | 有永久免费模型 |
| 智谱 | `https://open.bigmodel.cn/api/paas/v4` | [领取](https://open.bigmodel.cn/usercenter/apikeys) | `glm-4.7-flash` | Flash 免费 |
| 魔搭 | `https://api-inference.modelscope.cn/v1` | [领取](https://modelscope.cn/my/myaccesstoken) | `Qwen/Qwen2.5-7B-Instruct` | 需实名 |
| 百炼 | `https://dashscope.aliyuncs.com/compatible-mode/v1` | [领取](https://bailian.console.aliyun.com/) | `qwen-turbo` | 免费额度 |
| Page Agent | `https://page-ag-testing-ohftxirgbn.cn-shanghai.fcapp.run` | 无需 | `qwen3.5-plus` | 仅评估用 |
| DeepSeek | `https://api.deepseek.com` | [领取](https://platform.deepseek.com/api_keys) | `deepseek-chat` | 注册送额度 |

---

## 最小调用示例

```bash
curl "$OPENAI_BASE_URL/chat/completions" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"model\":\"$OPENAI_MODEL\",\"messages\":[{\"role\":\"user\",\"content\":\"你好\"}]}"
```

---

## 贡献

直接改本 README，补三行：`Base URL` / `API Key 链接` / `Models`，并注明是否国内可直连。

## License

[MIT](./LICENSE)
