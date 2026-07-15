# free-test-llm-api

国内能用的 **免费测试 LLM API**。复制下面配置就能用。

> 仅供测试，不要上生产。模型/额度以官网为准。

---

## 硅基流动

Key：https://cloud.siliconflow.cn/account/ak

```env
OPENAI_BASE_URL=https://api.siliconflow.cn/v1
OPENAI_API_KEY=你的Key
OPENAI_MODEL=Qwen/Qwen3-8B
```

其他免费模型：`deepseek-ai/DeepSeek-R1-Distill-Qwen-7B`（以控制台「免费」为准）

---

## 智谱

Key：https://open.bigmodel.cn/usercenter/apikeys

```env
OPENAI_BASE_URL=https://open.bigmodel.cn/api/paas/v4
OPENAI_API_KEY=你的Key
OPENAI_MODEL=glm-4.7-flash
```

其他免费模型：`glm-4-flash` · `glm-4.6v-flash`

---

## 魔搭 ModelScope

Key：https://modelscope.cn/my/myaccesstoken  
（一般要绑阿里云 + 实名）

```env
OPENAI_BASE_URL=https://api-inference.modelscope.cn/v1
OPENAI_API_KEY=你的Token
OPENAI_MODEL=Qwen/Qwen2.5-7B-Instruct
```

---

## 阿里云百炼

Key：https://bailian.console.aliyun.com/

```env
OPENAI_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
OPENAI_API_KEY=你的Key
OPENAI_MODEL=qwen-turbo
```

其他：`qwen-plus` · `qwen-flash`

---

## DeepSeek

Key：https://platform.deepseek.com/api_keys

```env
OPENAI_BASE_URL=https://api.deepseek.com
OPENAI_API_KEY=你的Key
OPENAI_MODEL=deepseek-chat
```

其他：`deepseek-reasoner`

---

## Page Agent 测试接口（无需 Key）

文档：https://alibaba.github.io/page-agent/docs/features/models/#free-testing-api  
仅限技术评估，有 system prompt 限制，不是通用聊天。

```env
OPENAI_BASE_URL=https://page-ag-testing-ohftxirgbn.cn-shanghai.fcapp.run
OPENAI_API_KEY=
OPENAI_MODEL=qwen3.5-plus
```

其他：`qwen3.5-flash`

---

## 调用示例

拿到上面三段变量后：

```bash
curl "$OPENAI_BASE_URL/chat/completions" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"model\":\"$OPENAI_MODEL\",\"messages\":[{\"role\":\"user\",\"content\":\"你好\"}]}"
```

Python：

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.siliconflow.cn/v1",  # 换成你复制的 URL
    api_key="你的Key",
)
r = client.chat.completions.create(
    model="Qwen/Qwen3-8B",
    messages=[{"role": "user", "content": "你好"}],
)
print(r.choices[0].message.content)
```

---

## 机器可读

见 [`apis.json`](./apis.json)（`base_url` / `api_key_url` / `models`）。

## License

[MIT](./LICENSE)
