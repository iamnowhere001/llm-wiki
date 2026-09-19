---
title: qmd（本地 Markdown 检索引擎）
type: entity
slug: qmd
tags: [工具, 检索]
created: 2026-09-18
updated: 2026-09-18
sources: [2026-09-18-karpathy-llm-wiki]
related: [index-and-log, obsidian, wiki-lint]
evidence_tier: single
confidence: medium
status: active
---

# qmd（本地 Markdown 检索引擎）

> 面向 Markdown 文件的本地搜索引擎，混合 BM25 与向量检索，并做 LLM 重排。同时提供 CLI 和 MCP server —— 前者让 LLM 通过 shell 调用，后者让 LLM 把它当原生工具用。

- **类型**：工具
- **外部链接**：https://github.com/tobi/qmd ｜ 仓库 `tobi/qmd`

> [!warning] 孤证 —— 本页仅 1 份素材支撑
> 支撑本页的只有 [[2026-09-18-karpathy-llm-wiki]]，尚未获得第二份独立来源的交叉验证。
> **引用本页结论时应带着这个前提**，或先补一份独立来源把它升到 `crossed`。

## 是什么

当 wiki 增长到 [[index-and-log]] 中描述的失效点之后，单靠 `index.md` 定位页面会消耗过多上下文。qmd 是作者推荐的替代方案：全在本地运行（on-device），不需要把知识库发到云端。

## 关键事实

| 属性 | 值 | 来源 |
|---|---|---|
| 检索方式 | 混合 BM25 + 向量 | [[2026-09-18-karpathy-llm-wiki]] |
| 重排 | LLM re-ranking | [[2026-09-18-karpathy-llm-wiki]] |
| 运行位置 | 全本地（on-device） | [[2026-09-18-karpathy-llm-wiki]] |
| 接口 | CLI + MCP server | [[2026-09-18-karpathy-llm-wiki]] |

**双接口的意义**：CLI 让 LLM 可以「shell 出去」调用它，这对任何能执行命令的 Agent 都成立；MCP server 让它变成一个结构化工具，参数和返回更规范。作者把这两条路并列，是因为不同 Agent 平台的工具调用能力差异很大。

## 在本知识库中的角色

它是**可选的规模化组件**。作者的态度是明确的「可选」：小规模下索引文件就够，需要时再上。本仓库当前的替代方案是 `tools/wiki.py search`（纯 Python 实现的 BM25，支持中文二字组切分），零依赖但精度低于 qmd。

这意味着本库存在一条明确的**升级路径**：页面数增长 → `index.md` 开始吃力 → 切换到 `wiki.py search` → 仍不够 → 引入 qmd。

## 相关概念

- [[index-and-log]] —— qmd 解决的是它的失效问题
- [[obsidian]] —— 同为本地优先的工具选择
- [[llm-wiki-pattern]]

## 来源

- [[2026-09-18-karpathy-llm-wiki]]

> [!warning] 待核验
> qmd 的具体性能数据、支持的嵌入模型、MCP 工具接口细节，本库尚未收录一手资料。上表全部来自 Karpathy 的转述。
>
> 补充：qmd 的仓库地址曾因 r1 抓取丢失行内链接而无法确认，现已从 r2 抓取中核实为 `https://github.com/tobi/qmd`。详见 [[2026-09-18-karpathy-llm-wiki]] 的「版本与捕获」一节。
