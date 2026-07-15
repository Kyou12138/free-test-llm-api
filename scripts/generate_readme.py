#!/usr/bin/env python3
"""Generate README.md (zh) and README.en.md from data/endpoints.yaml."""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Missing dependency: PyYAML. pip install -r requirements.txt", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "endpoints.yaml"

CAT_ORDER = ["project_demo", "anonymous_public", "free_token"]
CAT_ZH = {
    "project_demo": "开源项目官方测试接口（Demo / 技术评估）",
    "anonymous_public": "匿名公开端点（无需 Key）",
    "free_token": "免费 Token / 免费档（拿 Key 即可测）",
}
CAT_EN = {
    "project_demo": "Project official testing APIs (demo / evaluation)",
    "anonymous_public": "Anonymous public endpoints (no key)",
    "free_token": "Free token / free tier (key required)",
}


def load():
    with DATA.open(encoding="utf-8") as f:
        doc = yaml.safe_load(f)
    return doc.get("meta", {}), doc["endpoints"]


def status_badge(s: str) -> str:
    return {
        "active": "✅ active",
        "limited": "⚠️ limited",
        "unknown": "❓ unknown",
        "down": "❌ down",
    }.get(s, s)


def yes_no(v: bool, lang: str) -> str:
    if lang == "zh":
        return "是" if v else "否"
    return "Yes" if v else "No"


def env_block(env: dict) -> str:
    lines = []
    for k in ("LLM_BASE_URL", "LLM_MODEL_NAME", "LLM_API_KEY"):
        if k in env:
            lines.append(f'{k}="{env[k]}"')
        elif k == "LLM_API_KEY":
            # show comment-style when not required
            pass
    # include any other keys
    for k, v in env.items():
        if k not in ("LLM_BASE_URL", "LLM_MODEL_NAME", "LLM_API_KEY"):
            lines.append(f'{k}="{v}"')
    return "```bash\n" + "\n".join(lines) + "\n```"


def overview_table(endpoints: list, lang: str) -> str:
    if lang == "zh":
        rows = [
            "| 名称 | 类别 | 地区 | 需 Key | OpenAI 兼容 | 状态 | 文档 |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
    else:
        rows = [
            "| Name | Category | Region | Needs key | OpenAI-compatible | Status | Docs |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
    cat_label = CAT_ZH if lang == "zh" else CAT_EN
    for ep in endpoints:
        name = ep["name_zh"] if lang == "zh" else ep["name"]
        cat = cat_label.get(ep["category"], ep["category"])
        # shorten category for table
        short = {
            "project_demo": "project_demo" if lang == "en" else "项目 Demo",
            "anonymous_public": "anonymous" if lang == "en" else "匿名公开",
            "free_token": "free_token" if lang == "en" else "免费 Token",
        }.get(ep["category"], ep["category"])
        rows.append(
            f"| [{name}]({ep['source_docs']}) | `{short}` | {ep['region']} | "
            f"{yes_no(ep['api_key_required'], lang)} | {yes_no(ep['openai_compatible'], lang)} | "
            f"{status_badge(ep['status'])} | [docs]({ep['source_docs']}) |"
        )
    return "\n".join(rows)


def detail(ep: dict, lang: str) -> str:
    title = ep["name_zh"] if lang == "zh" else ep["name"]
    models = ", ".join(f"`{m}`" for m in ep["models"])
    restrict = ep["restrictions_zh"] if lang == "zh" else ep["restrictions_en"]
    restrict = "\n".join(f"> {line}" if line.strip() else ">" for line in restrict.strip().splitlines())
    terms = ep.get("terms") or ep["source_docs"]
    repo = ep.get("source_repo")

    if lang == "zh":
        lines = [
            f"### {title}",
            "",
            f"- **类别**: `{ep['category']}` · **提供方**: {ep['provider']} · **地区**: {ep['region']}",
            f"- **状态**: {status_badge(ep['status'])} · **上次核对**: `{ep['last_verified']}`",
            f"- **Base URL**: `{ep['base_url']}`",
            f"- **需 API Key**: {yes_no(ep['api_key_required'], lang)}"
            + (f" · [获取 Key]({ep['api_key_url']})" if ep.get("api_key_url") else ""),
            f"- **示例模型**: {models}",
            f"- **文档**: {ep['source_docs']}",
        ]
        if repo:
            lines.append(f"- **仓库**: {repo}")
        lines.append(f"- **条款**: {terms}")
        lines.extend(["", "**可复制配置**", "", env_block(ep["env"]), "", "**限制与说明**", "", restrict, ""])
    else:
        lines = [
            f"### {title}",
            "",
            f"- **Category**: `{ep['category']}` · **Provider**: {ep['provider']} · **Region**: {ep['region']}",
            f"- **Status**: {status_badge(ep['status'])} · **Last verified**: `{ep['last_verified']}`",
            f"- **Base URL**: `{ep['base_url']}`",
            f"- **API key required**: {yes_no(ep['api_key_required'], lang)}"
            + (f" · [Get key]({ep['api_key_url']})" if ep.get("api_key_url") else ""),
            f"- **Sample models**: {models}",
            f"- **Docs**: {ep['source_docs']}",
        ]
        if repo:
            lines.append(f"- **Repo**: {repo}")
        lines.append(f"- **Terms**: {terms}")
        lines.extend(["", "**Copy-paste config**", "", env_block(ep["env"]), "", "**Restrictions**", "", restrict, ""])
    return "\n".join(lines)


def curl_example(lang: str) -> str:
    if lang == "zh":
        title = "## 调用示例（OpenAI 兼容）"
        note = "以 **OVH 匿名端点**为例（无需 Key）："
    else:
        title = "## Call example (OpenAI-compatible)"
        note = "Example using the **OVH anonymous** endpoint (no key):"
    code = """```bash
export LLM_BASE_URL="https://oai.endpoints.kepler.ai.cloud.ovh.net/v1"
export LLM_MODEL_NAME="Meta-Llama-3_3-70B-Instruct"

curl "$LLM_BASE_URL/chat/completions" \\
  -H "Content-Type: application/json" \\
  -d "{
    \\"model\\": \\"$LLM_MODEL_NAME\\",
    \\"messages\\": [{\\"role\\": \\"user\\", \\"content\\": \\"hello\\"}],
    \\"max_tokens\\": 64
  }"
```"""
    return "\n".join([title, "", note, "", code, ""])


def generate_zh(meta: dict, endpoints: list) -> str:
    updated = meta.get("updated", "")
    parts = [
        "# 免费测试 LLM API",
        "",
        "> 收集 **可直接粘贴使用** 的免费测试接口：`LLM_BASE_URL` + `LLM_MODEL_NAME`",
        ">",
        "> 形态对齐 [Page Agent · Free Testing API](https://alibaba.github.io/page-agent/docs/features/models/#free-testing-api)",
        "",
        f"[English](./README.en.md) · 数据源 [`data/endpoints.yaml`](./data/endpoints.yaml) · 更新：`{updated}`",
        "",
        "## 这是什么 / 不是什么",
        "",
        "| ✅ 我们收录 | ❌ 我们不收录 |",
        "| --- | --- |",
        "| 开源项目为 Demo 提供的 **官方测试接口** | 非官方反代 / 盗 Key / 爬聊天网页 |",
        "| **无需注册** 的公开免费端点 | 仅有网页 Chat、没有 HTTP API |",
        "| 零成本拿 Key 就能测的 **OpenAI 兼容** 端点 | 纯营销「送额度」却无稳定测试入口说明 |",
        "| 每条都给出 **可复制 env** | 生产级 SLA 承诺（我们不承诺） |",
        "",
        f"**定位**：{meta.get('focus_zh', '')}",
        "",
        f"**免责声明**：{meta.get('disclaimer_zh', '')}",
        "",
        f"## 总览（{len(endpoints)}）",
        "",
        overview_table(endpoints, "zh"),
        "",
        curl_example("zh"),
    ]

    for cat in CAT_ORDER:
        group = [e for e in endpoints if e["category"] == cat]
        if not group:
            continue
        parts.append(f"## {CAT_ZH[cat]}")
        parts.append("")
        for ep in group:
            parts.append(detail(ep, "zh"))

    parts.extend(
        [
            "## 如何贡献",
            "",
            "见 [CONTRIBUTING.md](./CONTRIBUTING.md)。",
            "",
            "1. 在 `data/endpoints.yaml` 增加条目（必须有 `env.LLM_BASE_URL` + `env.LLM_MODEL_NAME`）",
            "2. `python scripts/validate.py && python scripts/generate_readme.py`",
            "3. 提交 PR，附上官网/文档链接与是否仅限技术评估的说明",
            "",
            "## 参考形态",
            "",
            "Page Agent 官方文档中的免费测试接口写法：",
            "",
            "```bash",
            '# qwen3.5-plus / qwen3.5-flash',
            'LLM_BASE_URL="https://page-ag-testing-ohftxirgbn.cn-shanghai.fcapp.run"',
            'LLM_MODEL_NAME="qwen3.5-plus"',
            "```",
            "",
            "来源：<https://alibaba.github.io/page-agent/docs/features/models/#free-testing-api>",
            "",
            "## License",
            "",
            "[MIT](./LICENSE)",
            "",
        ]
    )
    return "\n".join(parts)


def generate_en(meta: dict, endpoints: list) -> str:
    updated = meta.get("updated", "")
    parts = [
        "# Free Testing LLM APIs",
        "",
        "> Catalog of **copy-paste** free testing endpoints: `LLM_BASE_URL` + `LLM_MODEL_NAME`",
        ">",
        "> Inspired by [Page Agent · Free Testing API](https://alibaba.github.io/page-agent/docs/features/models/#free-testing-api)",
        "",
        f"[中文](./README.md) · Source: [`data/endpoints.yaml`](./data/endpoints.yaml) · Updated: `{updated}`",
        "",
        "## What this is / is not",
        "",
        "| ✅ We include | ❌ We exclude |",
        "| --- | --- |",
        "| Official **project demo testing APIs** | Unofficial reverse proxies / shared keys |",
        "| **No-signup** public free endpoints | Chat UIs without an HTTP API |",
        "| Zero-cost keys with **OpenAI-compatible** bases | Marketing fluff without a clear test entry |",
        "| Every entry has **copy-paste env** | Production SLA guarantees |",
        "",
        f"**Focus**: {meta.get('focus_en', '')}",
        "",
        f"**Disclaimer**: {meta.get('disclaimer_en', '')}",
        "",
        f"## Overview ({len(endpoints)})",
        "",
        overview_table(endpoints, "en"),
        "",
        curl_example("en"),
    ]

    for cat in CAT_ORDER:
        group = [e for e in endpoints if e["category"] == cat]
        if not group:
            continue
        parts.append(f"## {CAT_EN[cat]}")
        parts.append("")
        for ep in group:
            parts.append(detail(ep, "en"))

    parts.extend(
        [
            "## Contributing",
            "",
            "See [CONTRIBUTING.md](./CONTRIBUTING.md).",
            "",
            "1. Add an entry to `data/endpoints.yaml` (`env.LLM_BASE_URL` + `env.LLM_MODEL_NAME` required)",
            "2. `python scripts/validate.py && python scripts/generate_readme.py`",
            "3. Open a PR with docs links and evaluation-only notes",
            "",
            "## Reference style",
            "",
            "```bash",
            '# qwen3.5-plus / qwen3.5-flash',
            'LLM_BASE_URL="https://page-ag-testing-ohftxirgbn.cn-shanghai.fcapp.run"',
            'LLM_MODEL_NAME="qwen3.5-plus"',
            "```",
            "",
            "From: <https://alibaba.github.io/page-agent/docs/features/models/#free-testing-api>",
            "",
            "## License",
            "",
            "[MIT](./LICENSE)",
            "",
        ]
    )
    return "\n".join(parts)


def main() -> int:
    meta, endpoints = load()
    endpoints = sorted(
        endpoints,
        key=lambda e: (CAT_ORDER.index(e["category"]) if e["category"] in CAT_ORDER else 99, e["name"].lower()),
    )
    (ROOT / "README.md").write_text(generate_zh(meta, endpoints), encoding="utf-8", newline="\n")
    (ROOT / "README.en.md").write_text(generate_en(meta, endpoints), encoding="utf-8", newline="\n")
    print(f"Wrote README.md and README.en.md ({len(endpoints)} endpoints)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
