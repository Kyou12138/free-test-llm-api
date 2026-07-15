# Contributing / 贡献指南

[English](#english) · [中文](#中文)

---

## 中文

感谢贡献！本仓库只收录 **永久免费档** 的官方/主流 LLM API。

### 收录标准

**可以加：**
- 模型厂商官方 API 的持续免费档
- 主流推理平台的持续免费档（有公开文档）
- 字段尽量完整：文档链接、base URL、速率摘要、示例模型

**不要加：**
- 仅有注册试用额度、无持续 free tier
- 非官方反代 / 共享 Key / 爬聊天网页
- 无法核实的“听说免费”

### 流程

1. Fork 本仓库
2. 编辑 **`data/providers.yaml`**（唯一数据源）
3. 本地校验与生成：

```bash
pip install -r requirements.txt
python scripts/validate.py
python scripts/generate_readme.py
```

4. 提交时包含：`providers.yaml` + 生成后的 `README.md` / `README.en.md`
5. 打开 PR，说明：官网依据、是否永久免费、`last_verified` 日期

### 字段提示

- `type`: `model_vendor` | `inference_platform`
- `free_tier.permanent` 必须为 `true`
- `last_verified` 用 `YYYY-MM-DD`
- `status`: `active` | `limited` | `unknown`
- 配额写 **摘要 + 提醒以官网为准**，避免把过时数字写成保证

---

## English

Thanks for contributing! This repo lists **permanent free tiers** only.

### Criteria

**Accept:**
- Model-vendor official APIs with ongoing free tiers
- Mainstream inference platforms with ongoing free tiers and public docs
- Complete fields: docs, base URL, rate summary, sample models

**Reject:**
- Trial credits only (no ongoing free tier)
- Unofficial reverse proxies / shared keys / scraped chat UIs
- Unverifiable “someone said it’s free”

### Workflow

1. Fork
2. Edit **`data/providers.yaml`** (SSOT)
3. Validate & regenerate:

```bash
pip install -r requirements.txt
python scripts/validate.py
python scripts/generate_readme.py
```

4. Commit `providers.yaml` + generated READMEs
5. Open a PR with evidence links, permanence rationale, and `last_verified`

### Field tips

- `type`: `model_vendor` | `inference_platform`
- `free_tier.permanent` must be `true`
- `last_verified`: `YYYY-MM-DD`
- `status`: `active` | `limited` | `unknown`
- Rate limits are **summaries**, not guarantees — always point readers to official docs
