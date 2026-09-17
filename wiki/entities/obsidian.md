---
title: Obsidian（作为 wiki 的 IDE）
type: entity
slug: obsidian
tags: [工具, 编辑器]
created: 2026-09-18
updated: 2026-09-18
sources: [2026-09-18-karpathy-llm-wiki]
related: [index-and-log, llm-wiki-pattern]
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

## 相关概念

- [[index-and-log]]
- [[wiki-lint]]
- [[qmd]]

## 来源

- [[2026-09-18-karpathy-llm-wiki]]
