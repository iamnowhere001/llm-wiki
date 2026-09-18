---
title: LLM Wiki 模式研究
type: project
slug: llm-wiki-research
tags: [知识管理, LLM, 研究]
created: 2026-09-18
updated: 2026-09-18
goal: 把 LLM Wiki 模式的思想谱系、机制与适用边界研究到能写出一篇对外文章的深度
stage: active
started: 2026-09-18
sources: []
related: [pkm-history, why-pkm-in-ai-era, llm-wiki-pattern]
confidence: high
status: active
---

# LLM Wiki 模式研究

> 把「让 LLM 维护知识库」这件事研究清楚 —— 它从哪来、为什么成立、什么时候不成立。

- **目标（可验收）**：把 LLM Wiki 模式的思想谱系、机制与适用边界研究到能写出一篇对外文章的深度
- **阶段**：active
- **起始**：2026-09-18
- **目标完成**：—

> [!note] 关于这个 goal
> 本页的 `goal` 由 LLM 从本库自己已经声明的缺口（见 [[overview]] 的「本库自己的缺口」一节）起草，
> **待确认或改写**。按 `AGENTS.md` 第 8 节，项目应由人类提出 —— 本页是项目层的第一个实例，
> 用本库真实存在的研究线做演示，可随时替换或删除。

## 当前缺口

> 这一节是控制论里的**误差信号**，也是全页最重要的部分 —— **它决定下一步该找什么素材**。
> 每次 ingest 之前先读这里：这份素材填的是哪个缺口？填不上就不收。

| 缺口 | 卡在哪 | 需要什么素材 / 信息 |
|---|---|---|
| 卢曼的一手文献缺失 | [[niklas-luhmann]] 与 [[zettelkasten]] 全靠一份二手整理，数字无法核验 | 1981 年《Kommunikation mit Zettelkästen》英译本 |
| 只有支持方证据 | [[why-pkm-in-ai-era]] 全是「该建库」的论证，是明显的偏斜 | 一份严谨论证「AI 时代个人知识库已过时」的反方文献 |
| 1960–1980 年代空白 | [[pkm-history]] 在 Nelson 1965 与万维网 1989 之间没有锚点 | Engelbart 的 Augment、Xerox PARC 的一手材料 |
| 1998–2017 年空白 | 「PKM」命名到 Roam 兴起之间有近 20 年没有覆盖 | 那一时期的笔记工具演化史料 |
| [[roam-research]] 证据薄弱 | 两份素材都只是顺带提到它，`confidence: low` | 一份关于 Roam 历史的独立报道 |
| [[eden]] 能力未验证 | 全部信息来自其运营者的推广文案 | 独立评测，或干脆降级为「仅记录宣称」 |

## 知识（本项目消耗的页面）

> 项目与知识库之间的正向连接。这里链到的页面，就是「服务于本项目」的页面。

- **机制层**：[[llm-wiki-pattern]]、[[compounding-knowledge]]、[[cybernetic-learning]]、[[rag-vs-wiki]]、[[wiki-lint]]
- **历史层**：[[pkm-history]]、[[bidirectional-links]]、[[zettelkasten]]、[[commonplace-book-vs-llm-wiki]]、[[commonplace-book]]
- **人物线**（历史层的骨架）：[[vannevar-bush]]、[[ted-nelson]]、[[tim-berners-lee]]、[[andrej-karpathy]]
- **动机层**：[[why-pkm-in-ai-era]]、[[dan-koe]]
- **边界层**：[[use-cases]]
- **参照实现层**：[[second-brain-skill]]、[[qmd]]、[[notebooklm]]、[[eden]]

## 产出（外向回路）

> 知识库的价值在这里流出。**没有产出的项目是死项目**（见「共同笔记簿」页的「燃料而非收藏」）。

| 产出 | 形态 | 位置 |
|---|---|---|
| PKM 的历史与演进（1945–2026） | 分析页 | `wiki/analyses/pkm-history.md` |
| 为什么在 AI 时代仍然需要 PKMS | 分析页 | `wiki/analyses/why-pkm-in-ai-era.md` |
| 一篇对外文章 | 文章 | **待定 —— 这是本项目唯一真正的对外产出** |

> [!warning] 本项目的产出缺口
> 目前三个产出里有两个是**库内页面**，只有一个是真正的对外产出，而且还没开始。
> 按 [[why-pkm-in-ai-era]] 自己的论证，**只产出库内页面等于没有产出** —— 这个项目目前正踩在这条线上。

## 决策记录

> 项目里做过的判断 —— 这是 AI 拿不到的部分，也是本库存在的核心理由（见「为什么在 AI 时代仍然需要 PKMS」页）。

| 日期 | 决定 | 理由 |
|---|---|---|
| 2026-09-18 | 采用「收录时编译」而非纯 RAG 用法 | 同一批素材会被反复提问且需跨素材综合，编译成本可摊薄 |
| 2026-09-18 | 历史线写成 `analyses/` 而非 `concepts/` | 它是本库的综合判断而非素材给出的结论，需逐节点标注证据性质 |
| 2026-09-18 | 保留 4 处「待核验」而非删掉不确定内容 | 显式标注不确定比装作确定更有价值，也便于后续定点补料 |
| 2026-09-18 | 引入项目层作为 ingest 的入口 | 原库缺目标与过滤器，收到后来自己也不知道为什么收 |

## 不做什么（反范围）

> 明确排除什么，避免范围蔓延。

- 不做通用 RAG 工程实践（向量库选型、嵌入模型评测）
- 不做具体产品的功能评测
- 不涉及 LLM 训练与微调
- 不追求收录数量 —— 缺口表才是收录的判据

## 开放问题

- [ ] 对外文章的目标读者是谁？决定哪些内容需要展开、哪些可以略过
- [ ] 「LLM Wiki」这个模式有别的独立实现可以对照吗？
- [ ] 本库自身要不要做成可复用的模板/工具？

## 相关页面

- [[overview]]
- [[pkm-history]]
- [[why-pkm-in-ai-era]]
