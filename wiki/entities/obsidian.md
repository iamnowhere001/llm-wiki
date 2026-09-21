---
title: Obsidian（作为 wiki 的 IDE）
type: entity
slug: obsidian
tags: [工具, 编辑器]
created: 2026-09-18
updated: 2026-09-18
sources: [2026-09-18-karpathy-llm-wiki]
related: [index-and-log, llm-wiki-pattern, pkm-history, bidirectional-links, roam-research]
evidence_tier: single
confidence: high
status: active
---

# Obsidian（作为 wiki 的 IDE）

> 本地 Markdown 编辑器。在 [[llm-wiki-pattern]] 中承担「IDE」的角色：LLM 是写代码的人，wiki 是代码库，人类用 Obsidian 实时浏览结果。

- **类型**：工具
- **别名**：—
- **外部链接**：https://obsidian.md/

## 是什么

一个直接打开本地 Markdown 目录的编辑器。它的价值不在于编辑，而在于**把一堆 Markdown 文件呈现成一张知识网络**：双链跳转、反向链接面板、图谱视图。

作者的工作流是「LLM agent 开在一侧，Obsidian 开在另一侧」—— LLM 根据对话改文件，人类实时浏览改动、点链接、看图谱。

## 关键事实

| 功能 | 在 LLM Wiki 中的作用 |
|---|---|
| 图谱视图（Graph View） | 看 wiki 的形状：哪些是枢纽、哪些是孤岛 —— 与 [[wiki-lint]] 的孤岛检查互补 |
| 反向链接（Backlinks） | 从任一页面看到谁引用了它 |
| 附件目录设置 | 把 `raw/assets/` 设为附件目录，素材图片集中存放 |
| 下载附件快捷键 | 绑定后一键把网页文章里的图片下载到本地，避免外链失效 |
| Dataview 插件 | 基于 frontmatter 做动态查询，把 `type` / `tags` / `updated` 变成表格 |
| Marp 插件 | 从 wiki 内容直接生成幻灯片 |
| Web Clipper 扩展 | 浏览器一键把网页文章转成 Markdown 放进 `raw/` |

## 在本知识库中的角色

它是**读取层**。本仓库刻意保持了 Obsidian 兼容：`.obsidian/app.json` 已把附件目录设为 `raw/assets`，页面使用 `[[slug]]` 双链语法，frontmatter 字段也按 Dataview 可查询的方式设计（见 [[index-and-log]]）。

除了 Obsidian，本仓库还提供了一个零依赖的浏览站点（`python3 tools/wiki.py build`），不需要安装任何软件即可查看图谱与全文检索。

## 与其他页面的关系

- [[index-and-log]]
- [[wiki-lint]]
- [[qmd]]
- [[notes-apps-vs-llm-wiki]] —— 在「笔记软件 vs LLM Wiki」的选型讨论中，本页的定位是**不是竞争者，是推荐搭档**（阅读层）。该页同时指出本页作为搭档的硬优势：**打开的是本地纯文本目录，AI 可以在人类浏览的同时改文件** —— 托管方案即使提供导出也做不到这一点

## 在历史谱系中的位置

Obsidian 是 [[pkm-history]] 上「双向链接在私有域内复兴」这一阶段的产品之一。与它同期的是 [[roam-research]]。

| | [[roam-research]] | Obsidian |
|---|---|---|
| 数据 | 托管 | **本地 Markdown 文件** |
| 价格 | 订阅 | 免费（个人使用） |
| 链接单位 | 块（block） | 页面 + 块引用 |
| 对 LLM 的友好度 | 需通过 API | **文件可直接读写** |

**本库选择 Obsidian 而非 Roam，原因与 [[plain-text-and-git]] 一致**：本地纯文本才能被 LLM 与 git 直接操作。这不只是偏好 —— 它是 [[llm-wiki-pattern]] 能成立的前提。托管方案即使提供导出，也无法让 LLM 在「人类正在浏览时」实时改文件（见本页「在本知识库中的角色」）。

> [!note] 未验证的事实
> 据检索结果，Obsidian 由 Erica Xu 与 Shida Li 创建，首个公开版本发布于 **2020-03-30**。
> 这些信息**未收录素材**，因此标注为未验证。需收录官方文档或独立报道后方可提升置信度。

## 来源

- [[2026-09-18-karpathy-llm-wiki]]
