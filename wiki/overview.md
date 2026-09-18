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
- 具体产品的功能评测（[[eden]] 页仅记录其宣称能力，不做评测；[[traecode]] 页只记录其规则体系，同样不做产品评测）

## 核心线索

> **入口是项目，不是素材。** 先读 [[llm-wiki-research]] 的「当前缺口」表 —— 它决定下一份素材该是什么。
> 下面这条线索是「理解本库在讲什么」的路径，不是收录顺序。

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
动机层：→ [[why-pkm-in-ai-era]]（为什么在 AI 时代仍然值得建）
参照实现：→ [[second-brain-skill]]、[[eden]]

### 一条贯穿的主线

第 1-10 条来自 [[andrej-karpathy]] 的工程视角，第 11-12 条来自 [[dan-koe]] 的创作者视角。**两者独立收敛到同一架构**，但目的相反 —— 一个为了理解与检索，一个为了创作与输出。

这个交汇点本身是本库目前最有价值的内容：见 [[commonplace-book-vs-llm-wiki]]。

**横向的交汇之外还有一条纵向的线**：本库讨论的所有主张，在 [[pkm-history]] 里都能找到 80 年前的对应物。Bush 1945 年定义的「连接如何建立 + 谁来维护」这两个问题，是这整条线的骨架。

## 页面地图

| 分类 | 内容 | 入口 |
|---|---|---|
| **项目（入口层）** | 我在做什么、因此什么重要 | `wiki/projects/` |
| 素材摘要 | 每份 `raw/` 素材一页 | `wiki/sources/` |
| 实体 | 人物、组织、工具 | `wiki/entities/` |
| 概念 | 理论、方法、模式 | `wiki/concepts/` |
| 分析 | 对比、综述、回答归档 | `wiki/analyses/` |
| 系统 | 索引、日志、本页、使用约定 | `wiki/` 根 |

完整的页面清单见 [[index]]。

## 当前状态

- 素材：**11 份** —— 除原有的 [[2026-09-18-karpathy-llm-wiki]]（含 r1/r2 两版抓取）、[[2026-09-18-second-brain-skill-readme]]、[[2026-09-18-dankoe-remember-what-you-read]] 外，为梳理历史收录了 5 份（[[2026-09-18-bush-as-we-may-think]]、[[2026-09-18-appleton-bidirectional-links]]、[[2026-09-18-berners-lee-link-topology]]、[[2026-09-18-frand-hixon-pkm]]、[[2026-09-18-luhmann-zettelkasten]]），为 TraeCode 文章收录了 2 份（[[2026-09-18-trae-rules-docs]]、[[2026-09-18-trae-agents-md-vs-rules-forum]]）
- 页面：**46 个**（内容页 42 + 系统页 4）
- **项目：2 个** —— [[llm-wiki-research]]（研究模式本身，讲「为什么」）与 [[traecode-pkm-article]]（面向知识工作者的公众号文章，讲「怎么做」）。分工已确认为**两篇分开、暂不合并**。
- 结构：**两条线索的交汇 + 一条历史纵深 + 一个入口层** —— Karpathy 的工程视角（主干）+ Dan Koe 的创作者视角（补上目标机制与输出回路），中间是 second-brain-skill 作为参照实现；纵向上由 [[pkm-history]] 把 1945 年至今串成一条线；入口层由两个项目的缺口表共同决定下一步收什么

## 本库自己的缺口（按 [[cybernetic-learning]] 的判据）

[[dan-koe]] 的论证给本库提出一个自查问题：**这个知识库服务于什么目标？**

> [!success] 已部分解决 —— 引入项目层
> 本库原先有两个结构性缺口，**第一个已有解**：
>
> 1. ~~没有明确目标~~ → 新增 `wiki/projects/` 作为**入口层**。项目页把「目标」与「误差信号（当前缺口）」显式写下来，并规定 **ingest 前先读缺口表**。见 [[llm-wiki-research]] 与 `AGENTS.md` 第 3.5 节。
> 2. **外向回路仍然缺失。** 「查询→归档」让探索复利，但产出**只存回库里**。[[llm-wiki-research]] 的「产出」一节里，三个产出有两个是库内页面 —— **这正踩在它自己批评的那条线上**（见 [[commonplace-book-vs-llm-wiki]]）。[[traecode-pkm-article]] 把「公众号文章」定为核心产出、渠道与读者都已确认，是迄今最接近闭合的一次，但**尚未动笔** —— 所以这一条仍未闭合。

**仍未解决的那个更值得警惕**：项目层提供的是**机制**，不是**目标本身**。不过这里出现了一个正面信号：[[traecode-pkm-article]] 的 `goal` 走完了完整流程 —— **LLM 起草 → 人类回答关键前提 → 锁定**。而 [[llm-wiki-research]] 的 `goal` 仍是 LLM 起草、**待人类确认或改写**的状态。**机制可以代劳，目标不能。**

**历史线上的空白**：[[pkm-history]] 把 1945–2026 串了起来，但中间有两大段空白 —— 1960–1980 年代的个人计算实验（Engelbart、Xerox PARC），以及 1998 年命名到 2017 年 Roam 之间近 20 年的演化。**这些缺口已逐条记入 [[llm-wiki-research]] 的缺口表**，不再散落在本页。

## 下一步建议

> 收录素材的判据现在由 [[llm-wiki-research]] 的「当前缺口」表给出。
> 下面只保留**不属于任何项目**的维护性事项。

- [x] ~~确认或改写两个项目的 `goal`~~ —— **完成一半**：[[traecode-pkm-article]] 的三个前提已由北洛确认、goal 已锁定；[[llm-wiki-research]] 的 goal 仍是 LLM 起草、待确认
- [x] ~~建第二个项目 —— 一个项目不是项目层，是特例~~ —— **已完成**：[[traecode-pkm-article]]。两个项目立刻暴露了第一个真问题：**项目会重叠**（共享知识页、都以文章为产出）。北洛已裁定分两篇写，界线是「为什么」与「怎么做」
- [ ] **补上真正的对外产出** —— 唯一有希望的是 [[traecode-pkm-article]] 的公众号文章。它目前卡在四个**【阻塞】**缺口上，第一个是「最小可用 `AGENTS.md`」——见该页缺口表
- [ ] **本库 `AGENTS.md` 瘦身（18 KB）** —— 它既是文章的必要产出，也是本库自己的改进项：按「常驻成本」的说法，它每次任务都在付费。见 [[agents-md]] 的「常驻成本」一节
- [x] ~~收录 Vannevar Bush《As We May Think》原文，核验 [[vannevar-bush]] 中待验证的描述~~ —— **已完成**，[[vannevar-bush]] 已提升为 `confidence: high`
- [ ] 收录 qmd 的仓库文档，把 [[qmd]] 从 `medium` 置信度提升到 `high`
- [ ] 找一份独立的 RAG 评测资料，为 [[rag-vs-wiki]] 补充非作者来源的证据
- [ ] 核校 [[2026-09-18-dankoe-remember-what-you-read]] 的正文（经 AI 抓取工具提取，有转写偏差风险）
- [ ] 比对 second-brain-skill 的 `skills/wiki/README.md` 与本仓库 `AGENTS.md` 的规范差异

## 使用约定

回答风格、收录偏好等个人设置见 [[conventions]]。维护规则见仓库根目录的 `AGENTS.md`。
