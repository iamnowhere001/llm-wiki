---
title: NotebookLM（作为 RAG 范式的代表）
type: entity
slug: notebooklm
tags: [工具, RAG, 反例]
created: 2026-09-18
updated: 2026-09-18
sources: [2026-09-18-karpathy-llm-wiki]
related: [rag-vs-wiki, llm-wiki-pattern]
evidence_tier: single
confidence: medium
status: active
---

# NotebookLM（作为 RAG 范式的代表）

> 在本知识库中，它不作为产品被研究，而是作为 [[rag-vs-wiki]] 里 **RAG 范式的代表案例**被引用 —— 作者用它说明「每次查询都从零重新发现知识」的典型形态。

- **类型**：产品
- **外部链接**：https://notebooklm.google.com/

> [!warning] 孤证 —— 本页仅 1 份素材支撑
> 支撑本页的只有 [[2026-09-18-karpathy-llm-wiki]]，尚未获得第二份独立来源的交叉验证。
> **引用本页结论时应带着这个前提**，或先补一份独立来源把它升到 `crossed`。

## 是什么

一个上传文档集合、基于检索生成回答的产品。它本身工作良好，问题不在实现质量，而在**范式选择**。

## 关键事实

| 属性 | 在本库中的意义 | 来源 |
|---|---|---|
| 上传文件 → 检索 → 生成 | 知识不累积，每次提问重新推导 | [[2026-09-18-karpathy-llm-wiki]] |
| 与 ChatGPT 文件上传同类 | 被作者并列为「大多数 RAG 系统」 | [[2026-09-18-karpathy-llm-wiki]] |

## 在本知识库中的角色

它扮演**对照物**。本库引用它不是为了评价产品，而是为了给 [[rag-vs-wiki]] 一个具体锚点：当讨论「知识不累积」时，读者需要一个能立刻想起的例子。

这带来一个写作上的好处：抽象论断（「RAG 不累积」）有了具体载体，后续素材如果讨论 NotebookLM 的实际改进，可以直接接到这一页上。

## 相关概念

- [[rag-vs-wiki]]
- [[compounding-knowledge]]

## 来源

- [[2026-09-18-karpathy-llm-wiki]]

> [!warning] 待核验
> 本页未收录 NotebookLM 的产品文档或实测结果。作者只是把它作为范式举例，未展开评价。
