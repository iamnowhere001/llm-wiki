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
- **个人知识管理的历史谱系** —— 从 1945 年的 Memex 到当下的 LLM Wiki
- **知识如何转化为产出** —— 学习机制、笔记传统、创作回路

**不在范围内（目前）：**
- 通用 RAG 工程实践（向量库选型、嵌入模型评测）
- LLM 训练与微调
- 具体产品的功能评测（[[eden]] 页仅记录其宣称能力，不做评测）

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
11. **为什么要有目标**：没有目标就没有误差信号，也就没有留存。→ [[cybernetic-learning]]
12. **输出回路**：只收藏不产出，笔记就是死物。→ [[commonplace-book-vs-llm-wiki]]

历史纵深：→ [[pkm-history]]（1945–2026 的完整谱系）、[[vannevar-bush]]、[[commonplace-book]]、[[zettelkasten]]、[[bidirectional-links]]
参照实现：→ [[second-brain-skill]]、[[eden]]

### 一条贯穿的主线

第 1-10 条来自 [[andrej-karpathy]] 的工程视角，第 11-12 条来自 [[dan-koe]] 的创作者视角。**两者独立收敛到同一架构**，但目的相反 —— 一个为了理解与检索，一个为了创作与输出。

这个交汇点本身是本库目前最有价值的内容：见 [[commonplace-book-vs-llm-wiki]]。

**横向的交汇之外还有一条纵向的线**：本库讨论的所有主张，在 [[pkm-history]] 里都能找到 80 年前的对应物。Bush 1945 年定义的「连接如何建立 + 谁来维护」这两个问题，是这整条线的骨架。

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

- 素材：**9 份** —— 除原有的 [[2026-09-18-karpathy-llm-wiki]]（含 r1/r2 两版抓取）、[[2026-09-18-second-brain-skill-readme]]、[[2026-09-18-dankoe-remember-what-you-read]] 外，本次为梳理历史收录了 5 份：[[2026-09-18-bush-as-we-may-think]]、[[2026-09-18-appleton-bidirectional-links]]、[[2026-09-18-berners-lee-link-topology]]、[[2026-09-18-frand-hixon-pkm]]、[[2026-09-18-luhmann-zettelkasten]]
- 页面：**39 个**（内容页 35 + 系统页 4）
- 结构：**两条线索的交汇 + 一条历史纵深** —— Karpathy 的工程视角（主干）+ Dan Koe 的创作者视角（补上目标机制与输出回路），中间是 second-brain-skill 作为参照实现；纵向上由 [[pkm-history]] 把 1945 年至今串成一条线

## 本库自己的缺口（按 [[cybernetic-learning]] 的判据）

[[dan-koe]] 的论证给本库提出一个自查问题：**这个知识库服务于什么目标？**

目前 `wiki/conventions.md` 记录了「怎么用」，但没有记录「为什么建」。按 [[cybernetic-learning]] 的推论，**没有持续目标的知识库会因「不知道收了干什么」而停滞**。

同时，本库只有「查询→归档」这条**内向回路**，缺少指向库外产出的**外向回路**（见 [[commonplace-book-vs-llm-wiki]]）。

这两条是当前最需要补的结构性缺口，已列入下方建议。

**本次收录后新增的一个缺口**：[[pkm-history]] 把 1945–2026 串了起来，但中间有两大段空白 —— 1960–1980 年代的个人计算实验（Engelbart、Xerox PARC），以及 1998 年命名到 2017 年 Roam 之间近 20 年的演化。见 [[pkm-history]] 的开放问题。

## 下一步建议

- [ ] **给本库定一个明确的目标**，写进 `wiki/conventions.md` 或本页 —— 否则按 [[cybernetic-learning]] 的推论难以持续
- [ ] **设计一条输出回路**：知识库的产出应该流向哪里？（文章 / 报告 / 决策？）
- [x] ~~收录 Vannevar Bush《As We May Think》原文，核验 [[vannevar-bush]] 中待验证的描述~~ —— **已完成**，[[vannevar-bush]] 已提升为 `confidence: high`
- [ ] **收录卢曼 1981 年《Kommunikation mit Zettelkästen》** —— 这是 [[pkm-history]] 上最大的证据缺口（[[niklas-luhmann]] 与 [[zettelkasten]] 目前全靠二手文献）
- [ ] 收录 1960–1980 年代个人计算实验的资料（Engelbart 的 Augment、Xerox PARC）—— 补 [[pkm-history]] 的空白段
- [ ] 收录一份关于 [[roam-research]] 历史的独立报道，把它从 `low` 提升到 `high`
- [ ] 收录 qmd 的仓库文档，把 [[qmd]] 从 `medium` 置信度提升到 `high`
- [ ] 找一份独立的 RAG 评测资料，为 [[rag-vs-wiki]] 补充非作者来源的证据
- [ ] 独立验证 [[eden]] 的能力描述（目前全为厂商自述，`confidence: low`）
- [ ] 核校 [[2026-09-18-dankoe-remember-what-you-read]] 的正文（经 AI 抓取工具提取，有转写偏差风险）
- [ ] 比对 second-brain-skill 的 `skills/wiki/README.md` 与本仓库 `AGENTS.md` 的规范差异

## 使用约定

回答风格、收录偏好等个人设置见 [[conventions]]。维护规则见仓库根目录的 `AGENTS.md`。
