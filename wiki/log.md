---
title: 日志
type: meta
slug: log
created: 2026-09-18
updated: 2026-09-18
status: active
---

# 日志

> 只追加，不改写。条目格式固定，便于 `grep "^## \[" wiki/log.md | tail -5`。
> 类型：`init` / `ingest` / `query` / `lint` / `edit`

## [2026-09-18] init | 知识库初始化

建立三层目录结构（`raw/` + `wiki/` + `AGENTS.md`），确定页面类型、frontmatter 规范与三个工作流。

## [2026-09-18] ingest | LLM Wiki — 用 LLM 构建个人知识库的模式（Karpathy Gist）

收录首份素材，生成 14 个页面：1 个素材摘要页、6 个概念页、5 个实体页、2 个分析页。
其中 [[vannevar-bush]]、[[qmd]]、[[notebooklm]]、[[second-brain-skill]] 四页为单来源推断，已显式标注 `confidence` 与待核验警告。

## [2026-09-18] edit | 构建工具链与浏览站点

新增零依赖 CLI 工具链 `tools/wiki.py`（init / lint / stats / search / index / build / log / new / graph），以及单文件浏览站点 `site/index.html`。
## [2026-09-18] lint | 构建完成后的首次体检：0 项机器可查问题

## [2026-09-18] ingest | 重抓 Karpathy Gist（r2）—— 发现 r1 丢失行内链接，新增 raw/2026-09-18-karpathy-llm-wiki-r2.md

## [2026-09-18] ingest | Second Brain Skill 仓库 README —— 解决 second-brain-skill 页的悬空引用

## [2026-09-18] edit | 补建 use-cases、plain-text-and-git 两页；重写 second-brain-skill 评估；AGENTS.md 增加抓取质量与重抓命名规则

## [2026-09-18] edit | git init：知识库纳入版本控制，首次提交 a980e7b

## [2026-09-18] ingest | Dan Koe《How to remember everything you read》X 长文 —— 创作者视角，独立收敛到同一架构

## [2026-09-18] edit | 补建 cybernetic-learning、commonplace-book、dan-koe、eden、commonplace-book-vs-llm-wiki；回填 index-and-log、second-brain-skill、use-cases、overview

## [2026-09-18] ingest | Vannevar Bush《As We May Think》(1945) 全文 —— 取自 MIT STS.035 镜像 PDF（Atlantic 原刊有付费墙），撤销 vannevar-bush 页的待核验警告

## [2026-09-18] ingest | Maggie Appleton《A Short History of Bi-Directional Links》+ Tim Berners-Lee《HyperText Design Issues: Topology》—— 双向链接线的两份主干材料，后者是万维网设计者关于链接拓扑的一手笔记

## [2026-09-18] ingest | Frand & Hixon《Personal Knowledge Management: Who? What? Why? When? Where? How?》(Educom 98, 1998-10-15) —— PKM 术语首发文献；原文标注 1998，纠正二手来源的 1999 引用误差

## [2026-09-18] ingest | Niklas Luhmann 原始 Zettelkasten 方法（Ernest Chiang 二手整理，2025）—— 明确区分卢曼原法与 Ahrens 2017 的再诠释；卢曼 1981 原文仍缺

## [2026-09-18] query | 个人知识管理系统的历史与演进（1945-2026）→ 归档为 analyses/pkm-history，并新建 bidirectional-links、zettelkasten 两个概念页

## [2026-09-18] edit | 补建 ted-nelson / niklas-luhmann / tim-berners-lee / roam-research 四个实体页；回填 vannevar-bush（medium→high）、commonplace-book、obsidian、overview

## [2026-09-18] lint | 收录历史素材后的体检：39 页 / 360 链接 / 0 项机器可查问题；无孤岛页。语义层面标记 1 处年份矛盾（Nelson 1963 vs 1965）与 4 项待核验

