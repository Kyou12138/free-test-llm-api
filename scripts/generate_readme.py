#!/usr/bin/env python3
"""Generate README.md (zh) and README.en.md from data/providers.yaml."""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Missing dependency: PyYAML. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "providers.yaml"


def load_providers():
    with DATA.open(encoding="utf-8") as f:
        doc = yaml.safe_load(f)
    return doc.get("meta", {}), doc["providers"]


def yes_no(v: bool, lang: str) -> str:
    if lang == "zh":
        return "是" if v else "否"
    return "Yes" if v else "No"


def type_label(t: str, lang: str) -> str:
    if lang == "zh":
        return "模型厂商" if t == "model_vendor" else "推理平台"
    return "Model vendor" if t == "model_vendor" else "Inference platform"


def status_badge(status: str) -> str:
    return {"active": "✅ active", "limited": "⚠️ limited", "unknown": "❓ unknown"}.get(
        status, status
    )


def md_link(text: str, url: str) -> str:
    return f"[{text}]({url})"


def overview_table(providers: list, lang: str) -> str:
    if lang == "zh":
        headers = "| 名称 | 类型 | 地区 | OpenAI 兼容 | 需绑卡 | 状态 | 文档 |"
        sep = "| --- | --- | --- | --- | --- | --- | --- |"
    else:
        headers = "| Name | Type | Region | OpenAI-compatible | Card required | Status | Docs |"
        sep = "| --- | --- | --- | --- | --- | --- | --- |"

    rows = [headers, sep]
    for p in providers:
        name = p["name_zh"] if lang == "zh" else p["name"]
        rows.append(
            "| "
            + " | ".join(
                [
                    md_link(name, p["website"]),
                    type_label(p["type"], lang),
                    p["region"],
                    yes_no(p["openai_compatible"], lang),
                    yes_no(p["credit_card_required"], lang),
                    status_badge(p["status"]),
                    md_link("docs", p["docs"]),
                ]
            )
            + " |"
        )
    return "\n".join(rows)


def detail_section(p: dict, lang: str) -> str:
    title = p["name_zh"] if lang == "zh" else p["name"]
    ft = p["free_tier"]
    notes = ft["notes_zh"] if lang == "zh" else ft["notes_en"]
    models = ", ".join(f"`{m}`" for m in p["models_sample"])
    base = p.get("base_url") or ("—" if lang == "en" else "—")
    phone = p.get("phone_required", False)
    commercial = ft.get("commercial_use", "unknown")
    training = ft.get("data_used_for_training")

    if lang == "zh":
        train_s = {True: "可能用于训练/改进", False: "通常不用于训练", None: "未知"}.get(
            training, "未知"
        )
        lines = [
            f"### {title}",
            "",
            f"- **类型**: {type_label(p['type'], lang)} · **地区**: {p['region']} · **状态**: {status_badge(p['status'])}",
            f"- **官网**: {p['website']}",
            f"- **文档**: {p['docs']}",
            f"- **获取 Key**: {p['api_key_url']}",
            f"- **Base URL**: `{base}`",
            f"- **OpenAI 兼容**: {yes_no(p['openai_compatible'], lang)} · **需绑卡**: {yes_no(p['credit_card_required'], lang)} · **手机验证**: {yes_no(phone, lang)}",
            f"- **速率/额度（摘要）**: {ft['rate_limits_summary']}",
            f"- **商业使用**: `{commercial}` · **数据用途**: {train_s}",
            f"- **示例模型**: {models}",
            f"- **说明**: {notes}",
            f"- **上次核对**: `{p['last_verified']}`",
            "",
        ]
    else:
        train_s = {True: "may be used for training/improvement", False: "typically not for training", None: "unknown"}.get(
            training, "unknown"
        )
        lines = [
            f"### {title}",
            "",
            f"- **Type**: {type_label(p['type'], lang)} · **Region**: {p['region']} · **Status**: {status_badge(p['status'])}",
            f"- **Website**: {p['website']}",
            f"- **Docs**: {p['docs']}",
            f"- **API key**: {p['api_key_url']}",
            f"- **Base URL**: `{base}`",
            f"- **OpenAI-compatible**: {yes_no(p['openai_compatible'], lang)} · **Card required**: {yes_no(p['credit_card_required'], lang)} · **Phone**: {yes_no(phone, lang)}",
            f"- **Rate / quota (summary)**: {ft['rate_limits_summary']}",
            f"- **Commercial use**: `{commercial}` · **Data use**: {train_s}",
            f"- **Sample models**: {models}",
            f"- **Notes**: {notes}",
            f"- **Last verified**: `{p['last_verified']}`",
            "",
        ]
    return "\n".join(lines)


def generate_zh(meta: dict, providers: list) -> str:
    vendors = [p for p in providers if p["type"] == "model_vendor"]
    platforms = [p for p in providers if p["type"] == "inference_platform"]
    updated = meta.get("updated", "")
    criteria = meta.get("criteria_zh", "")

    parts = [
        "# 免费 LLM API 目录",
        "",
        "> 官方 + 主流推理平台 · **仅永久免费档** · 结构化数据驱动",
        "",
        f"[English](./README.en.md) · 数据源 [`data/providers.yaml`](./data/providers.yaml) · 上次数据更新：`{updated}`",
        "",
        "## 这是什么",
        "",
        "收集并维护**可公开申请**的 LLM HTTP API，条件是：",
        "",
        f"- {criteria}",
        "- 有官方文档与申请入口",
        "- **不包含**一次性试用额度、非官方反代、聊天网页扒接口",
        "",
        "## 免责声明",
        "",
        "- 配额、模型列表、服务条款**随时可能变更**，请以各服务商官网为准。",
        "- 本仓库只做信息整理，不提供代理、Key 共享或绕过限制的方法。",
        "- 使用前请阅读各厂商 ToS（商业用途、数据训练、地区限制等）。",
        "- 请合理使用免费档，避免滥用导致社区失去这些资源。",
        "",
        f"## 总览（{len(providers)}）",
        "",
        overview_table(providers, "zh"),
        "",
        "## 模型厂商官方 API",
        "",
    ]
    for p in vendors:
        parts.append(detail_section(p, "zh"))

    parts.append("## 主流推理平台")
    parts.append("")
    for p in platforms:
        parts.append(detail_section(p, "zh"))

    parts.extend(
        [
            "## 快速开始示例",
            "",
            "多数 OpenAI 兼容接口可如下调用（以 Groq 为例）：",
            "",
            "```bash",
            "export OPENAI_API_KEY=gsk_xxx",
            "export OPENAI_BASE_URL=https://api.groq.com/openai/v1",
            "",
            "curl \"$OPENAI_BASE_URL/chat/completions\" \\",
            "  -H \"Authorization: Bearer $OPENAI_API_KEY\" \\",
            "  -H \"Content-Type: application/json\" \\",
            "  -d '{\"model\":\"llama-3.1-8b-instant\",\"messages\":[{\"role\":\"user\",\"content\":\"hello\"}]}'",
            "```",
            "",
            "## 如何贡献",
            "",
            "见 [CONTRIBUTING.md](./CONTRIBUTING.md)。",
            "",
            "1. 编辑 `data/providers.yaml`",
            "2. 运行 `python scripts/validate.py`",
            "3. 运行 `python scripts/generate_readme.py`",
            "4. 提交 PR（勿手改生成的 README）",
            "",
            "## 与同类项目的差异",
            "",
            "| 项目 | 差异 |",
            "| --- | --- |",
            "| [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | 更全，含试用额度；本仓库**只收永久免费**并提供 YAML SSOT + 中英双语 |",
            "| [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | Awesome 列表风格；本仓库强调 schema 校验与可生成 README |",
            "",
            "致谢上述社区整理工作。",
            "",
            "## 维护",
            "",
            "```bash",
            "pip install -r requirements.txt",
            "python scripts/validate.py",
            "python scripts/generate_readme.py",
            "```",
            "",
            "## License",
            "",
            "[MIT](./LICENSE)",
            "",
        ]
    )
    return "\n".join(parts)


def generate_en(meta: dict, providers: list) -> str:
    vendors = [p for p in providers if p["type"] == "model_vendor"]
    platforms = [p for p in providers if p["type"] == "inference_platform"]
    updated = meta.get("updated", "")
    criteria = meta.get("criteria_en", "")

    parts = [
        "# Free LLM API Catalog",
        "",
        "> Official vendors + mainstream inference platforms · **Permanent free tiers only** · Data-driven",
        "",
        f"[中文](./README.md) · Source of truth: [`data/providers.yaml`](./data/providers.yaml) · Data updated: `{updated}`",
        "",
        "## What is this",
        "",
        "A curated catalog of publicly obtainable LLM HTTP APIs where:",
        "",
        f"- {criteria}",
        "- Official docs and signup / key pages exist",
        "- **Excluded**: one-shot trial credits only, unofficial reverse proxies, scraped chatbot UIs",
        "",
        "## Disclaimer",
        "",
        "- Quotas, models, and ToS **change without notice** — always verify official docs.",
        "- This repo is informational only; no proxies, shared keys, or bypass guides.",
        "- Read each provider's ToS (commercial use, training, regional limits).",
        "- Use free tiers responsibly so the community keeps access.",
        "",
        f"## Overview ({len(providers)})",
        "",
        overview_table(providers, "en"),
        "",
        "## Model vendor APIs",
        "",
    ]
    for p in vendors:
        parts.append(detail_section(p, "en"))

    parts.append("## Inference platforms")
    parts.append("")
    for p in platforms:
        parts.append(detail_section(p, "en"))

    parts.extend(
        [
            "## Quick start",
            "",
            "Most OpenAI-compatible endpoints work like this (Groq example):",
            "",
            "```bash",
            "export OPENAI_API_KEY=gsk_xxx",
            "export OPENAI_BASE_URL=https://api.groq.com/openai/v1",
            "",
            "curl \"$OPENAI_BASE_URL/chat/completions\" \\",
            "  -H \"Authorization: Bearer $OPENAI_API_KEY\" \\",
            "  -H \"Content-Type: application/json\" \\",
            "  -d '{\"model\":\"llama-3.1-8b-instant\",\"messages\":[{\"role\":\"user\",\"content\":\"hello\"}]}'",
            "```",
            "",
            "## Contributing",
            "",
            "See [CONTRIBUTING.md](./CONTRIBUTING.md).",
            "",
            "1. Edit `data/providers.yaml`",
            "2. Run `python scripts/validate.py`",
            "3. Run `python scripts/generate_readme.py`",
            "4. Open a PR (do not hand-edit generated READMEs)",
            "",
            "## Related projects",
            "",
            "| Project | How we differ |",
            "| --- | --- |",
            "| [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | Broader (includes trial credits); we keep **permanent free only** + YAML SSOT + bilingual docs |",
            "| [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | Awesome-list style; we focus on schema validation and generated READMEs |",
            "",
            "Thanks to those community efforts.",
            "",
            "## Maintenance",
            "",
            "```bash",
            "pip install -r requirements.txt",
            "python scripts/validate.py",
            "python scripts/generate_readme.py",
            "```",
            "",
            "## License",
            "",
            "[MIT](./LICENSE)",
            "",
        ]
    )
    return "\n".join(parts)


def main() -> int:
    meta, providers = load_providers()
    # stable sort: vendors first, then platforms, then name
    providers = sorted(
        providers,
        key=lambda p: (0 if p["type"] == "model_vendor" else 1, p["name"].lower()),
    )
    zh = generate_zh(meta, providers)
    en = generate_en(meta, providers)
    (ROOT / "README.md").write_text(zh, encoding="utf-8", newline="\n")
    (ROOT / "README.en.md").write_text(en, encoding="utf-8", newline="\n")
    print(f"Wrote README.md and README.en.md ({len(providers)} providers)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
