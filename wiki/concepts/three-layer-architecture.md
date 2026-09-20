---
title: 三层架构：raw / wiki / schema
type: concept
slug: three-layer-architecture
tags: [模式, 架构]
created: 2026-09-18
updated: 2026-09-18
sources: [2026-09-18-karpathy-llm-wiki]
related: [llm-wiki-pattern, ingest-query-lint, andrej-karpathy]
evidence_tier: single
confidence: high
status: active
---

# 三层架构：raw / wiki / schema

> [[llm-wiki-pattern]] 的物理结构：不可变的原始素材、LLM 全权拥有的知识库、描述维护规则的规范文件。三层各有明确的写入权限归属。

> [!warning] 孤证 —— 本页仅 1 份素材支撑
> 支撑本页的只有 [[2026-09-18-karpathy-llm-wiki]]，尚未获得第二份独立来源的交叉验证。
> **引用本页结论时应带着这个前提**，或先补一份独立来源把它升到 `crossed`。

## 要点

- 分层的核心不是目录美观，而是**写入权限的隔离**。
- `raw/` 不可变 —— 它是事实来源（source of truth）。
- `wiki/` 由 LLM 独占写入，人类只读。
- schema 层是**人类与 LLM 共同演进**的，这是唯一需要双方都动笔的一层。

## 定义与背景

| 层 | 位置 | 谁写 | 谁读 | 内容 |
|---|---|---|---|---|
| 原始素材 | `raw/` | 人类 | LLM（只读） | 文章、论文、笔记、PDF、图片 |
| 知识库 | `wiki/` | LLM | 人类 | 摘要、实体、概念、分析、交叉引用 |
| 规范 | `AGENTS.md` / `CLAUDE.md` | 共同演进 | LLM | 结构、约定、工作流 |

## 机制 / 原理

**为什么 `raw/` 必须不可变。** 如果 LLM 可以修改素材，就再也无法区分「素材原本这么说」和「LLM 以为素材这么说」。所有引用都会失去可追溯性。当 wiki 里出现矛盾时，唯一能裁决的就是回到 `raw/` 原文。因此需要修正时，正确做法是在 `wiki/` 里写清楚「素材原文如此，但应理解为 X」，而不是去改素材。

**为什么 wiki 由 LLM 独占。** 人类一旦动手写 wiki，就会破坏两件事：一是风格与结构的统一性（LLM 后续维护时面对的是一堆不一致的既有页面）；二是「人类只负责判断什么重要」这个清晰分工。人类改的是**规范层**——把偏好写进 `conventions.md`，让 LLM 去执行。

**为什么规范层要共同演进。** 作者强调 schema 是「关键配置文件」，它才是让 LLM 成为有纪律维护者的东西。但没有任何一份初始 schema 能一次写对 —— 领域不同、人类偏好不同、LLM 能力也在变。所以它必须可改，且改动应该发生在实践中发现问题的当下。

## 边界与反例

- **小规模下可以合并层。** 只有十几页时，`raw/` 和 `wiki/` 放同一个目录也能跑，但会很快失控。
- **schema 过长会失效。** 超过某个长度后，LLM 不会完整遵守。规范应当精炼、可执行，而不是百科。**本库的 `AGENTS.md` 目前约 18 KB，这条边界正在被实际触碰** —— 如果规范还是每次任务常驻加载的（见 [[agents-md]] 的「常驻成本」），那么篇幅不只是可读性问题，而是每次都付的开销。这已记入 [[traecode-pkm-article]] 的缺口表。
- **不等于「数据仓库分层」。** 这里的分层依据是写入权限，不是数据加工深度。

## 与其他页面的关系

- 是 [[llm-wiki-pattern]] 的结构化表达。
- 规范层里定义的工作流即 [[ingest-query-lint]]。
- `wiki/` 内部的导航文件见 [[index-and-log]]。
- 本仓库的三层实例：`raw/`、`wiki/`、`AGENTS.md`。
- 规范层的物理形态、跨工具性质与加载时机见 [[agents-md]]；它在真实产品中的实现方见 [[traecode]]。

## 待办 / 开放问题

- [ ] 规范层是否需要区分「稳定规则」与「临时偏好」？后者是否更适合放在 `conventions.md`？

## 来源

- [[2026-09-18-karpathy-llm-wiki]]
