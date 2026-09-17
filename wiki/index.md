---
title: 索引
type: meta
slug: index
created: 2026-09-18
updated: 2026-09-18
status: active
---

# 索引

> 本文件由 `python3 tools/wiki.py index` 从各页 frontmatter 自动生成。
> 每次 ingest 后重新生成。查询时先读本页定位候选页面，再深入阅读。

页面总数 **23** ｜ 素材 **4** 份 ｜ 最后更新 2026-09-18

## 素材摘要 (3)

- [[2026-09-18-dankoe-remember-what-you-read|How to remember everything you read (stop trying) — Dan Koe]] — 一篇创作者视角的长文，论证「记不住读过的东西不是问题，不理解才是」。提出学习是**输出过程**而非输入过程，并把「第二大脑」重新定义为**创作燃料库**（共同笔记簿）。  `学习方法` `知识管理` `创作`
- [[2026-09-18-karpathy-llm-wiki|LLM Wiki — 用 LLM 构建个人知识库的模式]] — Karpathy 提出的一个模式：让 LLM 把原始素材**增量编译**成一份持久、互相链接的 Markdown wiki，而不是每次查询都从零检索。  `知识管理` `LLM` `RAG` `模式`
- [[2026-09-18-second-brain-skill-readme|Second Brain Skill — 把 LLM Wiki 封装成 Claude Code Skill]] — 一个把 [[llm-wiki-pattern]] 落成可执行 Skill 的开源项目。它的核心表述是：**传统 RAG 是解释器，Second Brain Skill 是编译器。…  `实现` `Skill` `工具`

## 实体 (7)

- [[andrej-karpathy|Andrej Karpathy]] — [[llm-wiki-pattern]] 的提出者。本知识库的起点素材作者。  `人物` `LLM`
- [[dan-koe|Dan Koe]] — 独立创作者与写作者，关注「一人公司」、个人发展与创作方法论。在本知识库中，他是**独立收敛到 LLM Wiki 架构的第二条证据链**的来源。  `人物` `创作` `知识管理`
- [[eden|Eden（知识库与内容研究工具）]] — 一个面向创作者的知识库与选题研究工具。在本知识库中，它的价值是作为一个**「嵌入检索」路线的代表**出现 —— 但所有能力描述均来自其运营者的推广文案，未经独立验证。  `工具` `产品` `检索`
- [[notebooklm|NotebookLM（作为 RAG 范式的代表）]] — 在本知识库中，它不作为产品被研究，而是作为 [[rag-vs-wiki]] 里 **RAG 范式的代表案例**被引用 —— 作者用它说明「每次查询都从零重新发现知识」的典型形态。  `工具` `RAG` `反例`
- [[obsidian|Obsidian（作为 wiki 的 IDE）]] — 本地 Markdown 编辑器。在 [[llm-wiki-pattern]] 中承担「IDE」的角色：LLM 是写代码的人，wiki 是代码库，人类用 Obsidian 实时浏览…  `工具` `编辑器`
- [[qmd|qmd（本地 Markdown 检索引擎）]] — 面向 Markdown 文件的本地搜索引擎，混合 BM25 与向量检索，并做 LLM 重排。同时提供 CLI 和 MCP server —— 前者让 LLM 通过 shell 调…  `工具` `检索`
- [[vannevar-bush|Vannevar Bush 与 Memex]] — 1945 年提出 Memex 构想：一台私人、主动策展的知识装置，其中**文档之间的关联路径（associative trails）与文档本身同样有价值**。[[llm-wiki…  `人物` `历史` `知识管理`

## 概念 (10)

- [[commonplace-book|共同笔记簿：作为创作燃料而非收藏品]] — 一个比「第二大脑」古老得多的实践：把读到的、想到的摘录与想法集中记录，供日后取用。[[dan-koe]] 的判断是 —— 历史上有共同笔记簿的人与今天「第二大脑爱好者」的**唯一…  `知识管理` `历史` `创作`
- [[compounding-knowledge|复利式知识积累]] — [[llm-wiki-pattern]] 的价值来源：知识库的产出不是随素材线性增长，而是因为**页面之间互相引用、新素材修改旧页面**而产生组合式增长。  `知识管理` `认识论`
- [[cybernetic-learning|控制论式学习：为什么目标是记忆的前提]] — [[dan-koe]] 的核心论证：学习是**输出过程**而非输入过程。链条是 **目标 → 误差信号 → 过滤器 → 相关性 → 留存**。没有目标，大脑不会标记什么重要 ——…  `学习方法` `控制论` `机制`
- [[index-and-log|索引与日志：index.md 与 log.md]] — wiki 里两个承担导航职责的特殊文件：`index.md` 面向内容（有什么页），`log.md` 面向时间（发生过什么）。它们让 wiki 在增长后仍然可被 LLM 和人类快…  `导航` `约定`
- [[ingest-query-lint|三个操作：Ingest / Query / Lint]] — [[llm-wiki-pattern]] 的全部日常操作收敛为三件事：把素材编译进 wiki、基于 wiki 回答问题、给 wiki 做体检。三者共同保证知识库「保鲜」。  `工作流` `操作`
- [[llm-wiki-pattern|LLM Wiki 模式]] — 让 LLM 增量构建并持续维护一份持久、互相链接的 Markdown 知识库，作为人与原始素材之间的中间层 —— 知识**编译一次，然后保鲜**，而不是每次查询重新推导。  `知识管理` `LLM` `模式`
- [[plain-text-and-git|纯文本与 Git：知识库的基础设施]] — 整个 wiki 就是「一个装 Markdown 文件的 git 仓库」。这不是实现细节，而是 [[llm-wiki-pattern]] 能成立的前提 —— 没有版本历史，「人类与…  `基础设施` `版本控制` `约定`
- [[three-layer-architecture|三层架构：raw / wiki / schema]] — [[llm-wiki-pattern]] 的物理结构：不可变的原始素材、LLM 全权拥有的知识库、描述维护规则的规范文件。三层各有明确的写入权限归属。  `架构` `模式`
- [[use-cases|适用场景：五类积累型知识领域]] — [[llm-wiki-pattern]] 只在一种条件下划算：**知识在时间上累积，且需要跨素材综合**。作者给出五个具体领域，它们共享同一个结构特征。  `场景` `选型`
- [[wiki-lint|Wiki 体检（Lint）]] — 定期让 LLM 检查知识库的健康状况。它既修问题，也**生产下一步的选题** —— 这是 [[llm-wiki-pattern]] 对抗熵增的机制。  `工作流` `维护` `质量`

## 分析 (3)

- [[commonplace-book-vs-llm-wiki|共同笔记簿 vs LLM Wiki：两条独立路径走到同一个架构]] — 结论：[[andrej-karpathy]] 从 AI 工程角度、[[dan-koe]] 从写作创作角度，**独立收敛到了同一个架构** —— 让 LLM 维护一个「原始素材 /…  `对比` `综合` `模式`
- [[rag-vs-wiki|RAG 与 LLM Wiki 的对比]] — 结论：两者不是「好检索」与「差检索」的关系，而是**知识在哪里被编译**的关系。RAG 在查询时编译（每次都重算），LLM Wiki 在收录时编译（编译一次、持续保鲜）。选择取决…  `对比` `RAG` `架构`
- [[second-brain-skill|second-brain-skill 评估：把 LLM Wiki 封装成 Skill]] — 结论：这个项目把 [[llm-wiki-pattern]] 从「一份理念文档」落成了「一组可执行命令」，用**自然语言意图识别**替代命令记忆，还补上了原构想缺失的运维命令。但它…  `工具` `实现` `Skill`

## 系统页

- [[overview|总览]] — 这个知识库在讲什么
- [[log|日志]] — 按时间记录的所有操作
- [[conventions|使用约定]] — 人类的偏好设置
