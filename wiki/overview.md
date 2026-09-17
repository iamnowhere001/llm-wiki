---
title: 总览
type: meta
slug: overview
tags: []
created: 2026-09-18
updated: 2026-09-18
sources: []
related: [llm-wiki-pattern]
confidence: high
status: active
---

# 总览

> 这个知识库在讲什么：**LLM Wiki 模式** —— 让 LLM 把原始素材增量编译成一份持久、互相链接的 Markdown 知识库。本仓库同时是这个模式的实例。

## 范围

**在范围内：**
- LLM 与个人知识管理的结合方式
- 「收录时编译」与「查询时检索」（RAG）两条路线的对比
- 维护知识库的工具链与约定
- 该模式的思想源头与相关实现

**不在范围内（目前）：**
- 通用 RAG 工程实践（向量库选型、嵌入模型评测）
- LLM 训练与微调
- 具体产品的功能评测

## 核心线索

这个知识库围绕一条主线展开，可以按顺序读：

1. **问题**：主流 RAG 用法在每次提问时从零重新发现知识，什么都不会累积。
2. **主张**：让 LLM 增量构建并维护一份持久 wiki，知识编译一次、持续保鲜。→ [[llm-wiki-pattern]]
3. **结构**：不可变素材 / LLM 拥有的知识库 / 共同演进的规范。→ [[three-layer-architecture]]
4. **操作**：收录、查询、体检。→ [[ingest-query-lint]]
5. **导航**：内容索引与时间日志。→ [[index-and-log]]
6. **价值来源**：素材与探索两条通道的复利。→ [[compounding-knowledge]]
7. **防腐机制**：定期体检，同时生产选题。→ [[wiki-lint]]
8. **路线对比**：什么时候该用哪条路。→ [[rag-vs-wiki]]
9. **落地场景**：五类积累型知识领域，以及不该用的三类。→ [[use-cases]]
10. **基础设施**：纯 Markdown + git 是「共同演进」可审计的前提。→ [[plain-text-and-git]]

历史纵深：→ [[vannevar-bush]]
参照实现：→ [[second-brain-skill]]

## 页面地图

| 分类 | 内容 | 入口 |
|---|---|---|
| 素材摘要 | 每份 `raw/` 素材一页 | `wiki/sources/` |
| 实体 | 人物、组织、工具 | `wiki/entities/` |
| 概念 | 理论、方法、模式 | `wiki/concepts/` |
| 分析 | 对比、综述、回答归档 | `wiki/analyses/` |
| 系统 | 索引、日志、本页、使用约定 | `wiki/` 根 |

完整的页面清单见 [[index]]。

## 当前状态

- 素材：2 份 —— [[2026-09-18-karpathy-llm-wiki]]（含 r1/r2 两版抓取）、[[2026-09-18-second-brain-skill-readme]]
- 页面：20 个（内容页 16 + 系统页 4）
- 结构：Karpathy Gist 是主干，second-brain-skill 是第一个参照实现

## 下一步建议

- [ ] 收录 Vannevar Bush《As We May Think》原文，核验 [[vannevar-bush]] 中待验证的描述
- [ ] 收录 qmd 的仓库文档，把 [[qmd]] 从 `medium` 置信度提升到 `high`
- [ ] 找一份独立的 RAG 评测资料，为 [[rag-vs-wiki]] 补充非作者来源的证据
- [ ] 比对 second-brain-skill 的 `skills/wiki/README.md` 与本仓库 `AGENTS.md` 的规范差异
- [ ] 核实 second-brain-skill 的 LICENSE 是否真的缺失（README 声明 MIT，API 字段为空）

## 使用约定

回答风格、收录偏好等个人设置见 [[conventions]]。维护规则见仓库根目录的 `AGENTS.md`。
