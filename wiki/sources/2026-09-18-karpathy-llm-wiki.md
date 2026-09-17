---
title: LLM Wiki — 用 LLM 构建个人知识库的模式
type: source
slug: 2026-09-18-karpathy-llm-wiki
tags: [知识管理, LLM, RAG, 模式]
created: 2026-09-18
updated: 2026-09-18
sources: [2026-09-18-karpathy-llm-wiki, 2026-09-18-karpathy-llm-wiki-r2]
related: [llm-wiki-pattern, three-layer-architecture, ingest-query-lint]
confidence: high
status: active
---

# LLM Wiki — 用 LLM 构建个人知识库的模式

> Karpathy 提出的一个模式：让 LLM 把原始素材**增量编译**成一份持久、互相链接的 Markdown wiki，而不是每次查询都从零检索。

- **作者**：[[andrej-karpathy]]
- **链接**：https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- **发布时间**：2026-04-04
- **素材路径**：`raw/2026-09-18-karpathy-llm-wiki.md`（r1）、`raw/2026-09-18-karpathy-llm-wiki-r2.md`（r2，推荐引用）

## 版本与捕获

同一份 Gist 存在两个抓取版本，**内容有实质差异**：

| | r1 | r2 |
|---|---|---|
| 文件 | `raw/2026-09-18-karpathy-llm-wiki.md` | `raw/2026-09-18-karpathy-llm-wiki-r2.md` |
| 正文行内超链接 | **丢失** | 保留 |
| `->` 字符 | 转成了纯文本 | 保留为 `→` |

具体差异（r2 相对 r1）：

1. `Tolkien Gateway` 在 r1 中是纯文本，r2 中带链接 → `https://tolkiengateway.net/wiki/Main_Page`
2. `qmd` 在 r1 中是纯文本，r2 中带链接 → `https://github.com/tobi/qmd`
3. 两处 `Settings -> Files and links` / `Settings -> Hotkeys` 的箭头字符

**这不是作者改稿，是 r1 的抓取缺陷** —— 2026-09-18 07:05 首次抓取该页面时行内链接还在（见 `wiki/log.md`），07:06 落盘的 r1 已丢失。因此 r2 才是忠实副本，**引用时应指向 r2**。

按 `AGENTS.md` 的 `raw/` 不可变约定，r1 未被修改，两版并存。r2 的 frontmatter 中 `supersedes` 字段指向 r1。

## 来源边界（重要）

**本素材（Gist 文件正文）是纯英文的，不包含任何中文内容。**

Gist 页面正文之后附有一段中文项目说明（关于 `ChavesLiu/second-brain-skill`），它**不在本素材中**，位置无法确定（description / 评论 / 附加文档皆有可能）。

**已解决（2026-09-18）**：那段中文说明经核实是第三方仓库的 README。已直接采集该仓库的 README 原文作为独立素材 → [[2026-09-18-second-brain-skill-readme]]。

> [!warning] 教训
> 初版 `analyses/second-brain-skill.md` 曾把 `sources` 指向本素材，而本素材并不包含该页总结的内容 —— 一个**悬空引用**。已修正为指向新素材。
> 触发这次核查的是「重新抓取同一素材做比对」这个动作。这说明：**对已有素材做周期性重抓，除了能发现上游改动，还能暴露自己当初的捕获缺陷。**


## 关键要点

1. **wiki 是持久、会复利的产物**，不是查询时的临时检索结果。交叉引用已经建好，矛盾已经标注，综述已经反映了读过的一切。
2. **三层架构**：`raw/` 不可变素材 → `wiki/` LLM 维护的 Markdown → schema 文件（CLAUDE.md / AGENTS.md）描述维护规则。
3. **三个操作**：Ingest（收录）、Query（查询）、Lint（体检）。
4. **人类不写 wiki，LLM 不做选题。** 人类负责挑素材、提问、判断重要性；LLM 负责摘要、交叉引用、归档、记账。
5. **好答案要归档回 wiki**，让探索也能像素材一样复利，而不是消失在聊天记录里。
6. **索引 + 日志**两个特殊文件承担导航职责：`index.md` 面向内容，`log.md` 面向时间。
7. 中等规模（~100 份素材、数百页）下，索引文件足够，**不需要向量检索基础设施**。

## 摘要

文章的核心论证是一条对比：主流做法（NotebookLM、ChatGPT 文件上传、多数 RAG）在**每次提问时重新发现知识**。要回答一个需要综合五份文档的问题，LLM 每次都得重新找出并拼装那些碎片。什么都不会累积。

作者主张的替代方案是：LLM **增量构建并维护一份持久 wiki**。新素材进来时，它不只是建索引，而是阅读、提取、整合 —— 更新实体页、修订主题摘要、标注新数据与旧论断的矛盾、强化或挑战正在成形的综述。

由此推出三层架构与三个操作。作者特别强调「schema 层」是关键配置文件：它让 LLM 成为一个**有纪律的 wiki 维护者**，而不是通用聊天机器人。并且这套 schema 应该由人类和 LLM 一起演进。

在操作层面，作者给出几个具体做法：收录一份素材通常触及 **10-15 个页面**；只写摘要页是失败的做法。查询时先读 `index.md` 定位候选页，再深入。日志条目用固定前缀（`## [2026-04-02] ingest | 标题`）以便用 `grep` 解析。

最后，作者解释了为什么这件事现在可行：维护知识库真正累人的不是阅读和思考，而是**记账** —— 更新交叉引用、保持摘要新鲜、记录矛盾、维持几十个页面的一致性。人类放弃 wiki 是因为维护成本增长快于价值增长。LLM 不会厌烦、不会忘记更新引用、能一次改动 15 个文件。

## 与现有知识库的关系

- 这是本知识库的**第一份素材**，也是本知识库自身的构建依据。本仓库的 `AGENTS.md` 即该文所述 schema 层的一个具体实例。
- 作者把思想源头指向 [[vannevar-bush]] 1945 年的 Memex 构想：私人、主动策展、文档之间的连接与文档本身同样有价值。Bush 没能解决的是「谁来做维护」—— 这正是 LLM 补上的那一环。

## 新出现的实体 / 概念

- 实体：[[andrej-karpathy]]、[[vannevar-bush]]、[[obsidian]]、[[qmd]]、[[notebooklm]]
- 概念：[[llm-wiki-pattern]]、[[three-layer-architecture]]、[[ingest-query-lint]]、[[index-and-log]]、[[compounding-knowledge]]、[[wiki-lint]]、[[use-cases]]、[[plain-text-and-git]]
- 分析：[[rag-vs-wiki]]
- 已提及但未独立成页（仅出现一次，未达 `AGENTS.md` 的建页阈值）：Tolkien Gateway、Marp、Dataview、Obsidian Web Clipper、ChatGPT 文件上传

## 待办

- [ ] **补录 Gist 页面附加的中文项目说明**，解决 [[second-brain-skill]] 的悬空引用（优先级最高）
- [ ] 补充其他 Agent 平台（Codex / OpenCode）对 schema 文件的约定差异
- [ ] 找到 qmd 的实际基准数据，评估在多少页之后索引文件开始失效
- [ ] Tolkien Gateway 是「社区共建 wiki」的最佳实例，值得收录一份独立素材

## 相关页面

- [[llm-wiki-pattern]]
- [[rag-vs-wiki]]
- [[second-brain-skill]]
