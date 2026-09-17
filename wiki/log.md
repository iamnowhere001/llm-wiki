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

