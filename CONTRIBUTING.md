# Contributing / 贡献指南

## 中文

本仓库收录 **免费测试用 LLM API 端点**（可复制 `LLM_BASE_URL` + `LLM_MODEL_NAME`），形态参考：

https://alibaba.github.io/page-agent/docs/features/models/#free-testing-api

### 收录标准

| 类别 | 说明 |
| --- | --- |
| `project_demo` | 开源项目为 Demo/技术评估提供的官方测试接口 |
| `anonymous_public` | 无需注册、无需 Key 的公开免费端点 |
| `free_token` | 可免费拿 Key/Token 后立刻测试的 OpenAI 兼容端点 |

**拒绝：** 非官方反代、共享 Key、爬网页聊天、无法核实来源。

### 流程

```bash
# 1. 编辑数据
# data/endpoints.yaml

# 2. 校验 + 生成 README
pip install -r requirements.txt
python scripts/validate.py
python scripts/generate_readme.py

# 3. PR 必须包含 endpoints.yaml 与生成后的 README
```

每条必须有：

- `base_url` / `models` / `source_docs`
- `env.LLM_BASE_URL` + `env.LLM_MODEL_NAME`
- `restrictions_zh` + `restrictions_en`（写清是否仅技术评估、地区、限流）
- `last_verified: YYYY-MM-DD`

---

## English

We catalog **free testing LLM endpoints** (copy-paste `LLM_BASE_URL` + `LLM_MODEL_NAME`), in the spirit of Page Agent's Free Testing API.

### Categories

- `project_demo` — official demo/eval endpoints from open-source projects  
- `anonymous_public` — no signup / no key public free endpoints  
- `free_token` — free key/token, OpenAI-compatible testing  

**Reject:** unofficial reverse proxies, shared keys, scraped chat UIs, unverifiable sources.

### Workflow

Edit `data/endpoints.yaml` → `validate.py` → `generate_readme.py` → PR.
