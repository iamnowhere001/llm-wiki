---
title: 三个操作：Ingest / Query / Lint
type: concept
slug: ingest-query-lint
tags: [工作流, 操作]
created: 2026-09-18
updated: 2026-09-18
sources: [2026-09-18-karpathy-llm-wiki]
related: [llm-wiki-pattern, wiki-lint, index-and-log]
evidence_tier: single
confidence: high
status: active
---

# 三个操作：Ingest / Query / Lint

> [[llm-wiki-pattern]] 的全部日常操作收敛为三件事：把素材编译进 wiki、基于 wiki 回答问题、给 wiki 做体检。三者共同保证知识库「保鲜」。

> [!warning] 孤证 —— 本页仅 1 份素材支撑
> 支撑本页的只有 [[2026-09-18-karpathy-llm-wiki]]，尚未获得第二份独立来源的交叉验证。
> **引用本页结论时应带着这个前提**，或先补一份独立来源把它升到 `crossed`。

## 要点

- **Ingest** 是唯一的知识入口，也是工作量最大的一步（一份素材触及 10-15 页）。
- **Query** 的产物不应该只留在聊天里 —— 好答案要归档成 `analyses/` 页面。
- **Lint** 是让 wiki 不腐烂的机制，且它同时是**选题引擎**：体检会产出「下一步该读什么」。
- 三者共享同一份 schema，所以换会话、换模型后行为仍一致。

## 定义与背景

| 操作 | 输入 | 输出 | 触发方式 |
|---|---|---|---|
| Ingest | `raw/` 中的一份素材 | 摘要页 + 若干实体/概念页 + 既有页面的回填 + index/log 更新 | 「收录这篇」 |
| Query | 一个问题 | 带引用的回答（可选归档为 `analyses/` 页面） | 「XX 是什么」 |
| Lint | 现有 wiki | 问题清单 + 新素材建议 + 新问题建议 | 「检查一下知识库」 |

## 机制 / 原理

**Ingest 的关键是「连锁更新」。** 只写摘要页等于没做 ingest。正确的流程是：读 → 与人类对齐要点（尤其要指出与已有页面的**矛盾**）→ 写摘要页 → 按阈值拆实体/概念页 → 回填所有被影响的旧页面 → 更新索引 → 写日志 → 跑 lint。矛盾必须显式标注，不允许静默覆盖。

**Query 的关键是「归档」。** 作者的原话是：好的回答可以作为一个新页面被归档回 wiki。一次对比、一份分析、一个你发现的连接 —— 这些都有价值，不该消失在聊天记录里。这让**探索也复利**，与收录素材是同一机制。

**Lint 的关键是「语义问题机器查不出」。** 断链、孤岛、缺 frontmatter 可以脚本化；但矛盾、过期、该建未建需要 LLM 阅读理解。详见 [[wiki-lint]]。

## 边界与反例

- **批量 ingest 会降低质量。** 作者偏好一次一份、全程参与；批量收录省事但会丢失「与人类对齐要点」这一步，矛盾更容易被漏掉。
- **Query 不一定都要归档。** 一次性的、无复用价值的查询不必建页，否则 wiki 会被噪音淹没。
- **Lint 不是越频繁越好。** 它的价值随 wiki 增长而上升；十页的时候跑 lint 是浪费。

## 与其他页面的关系

- 定义在 [[three-layer-architecture]] 的规范层中。
- Ingest 与 Query 的产物都由 [[index-and-log]] 记录。
- Lint 展开为 [[wiki-lint]]。
- 归档的 Query 产物存放在 `analyses/`，例如 [[rag-vs-wiki]]。

## 开放问题

- [ ] 是否需要一个「Ingest 检查清单」脚本，确保第 5 步（回填）没被跳过？

## 来源

- [[2026-09-18-karpathy-llm-wiki]]
