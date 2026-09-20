---
title: Second Brain Skill — 把 LLM Wiki 封装成 Claude Code Skill
type: source
slug: 2026-09-18-second-brain-skill-readme
tags: [工具, Skill, 实现]
created: 2026-09-18
updated: 2026-09-20
sources: [2026-09-18-second-brain-skill-readme]
related: [second-brain-skill, llm-wiki-pattern, three-layer-architecture]
confidence: high
status: active
---

# Second Brain Skill — 把 LLM Wiki 封装成 Claude Code Skill

> 一个把 [[llm-wiki-pattern]] 落成可执行 Skill 的开源项目。它的核心表述是：**传统 RAG 是解释器，Second Brain Skill 是编译器。**

- **作者**：ChavesLiu
- **链接**：https://github.com/ChavesLiu/second-brain-skill
- **素材路径**：`raw/2026-09-18-second-brain-skill-readme.md`（README 逐字副本，取自 GitHub API）

## 关键要点

1. **定位**：不是 Karpathy Gist 的一部分，而是**受其启发的第三方实现**。README 开头即致谢 Karpathy。
2. **核心表述**：把 RAG 与 wiki 的差异概括为「解释器 vs 编译器」—— 解释器每次提问都从原始文档重新检索推理；编译器预先编译成结构化 wiki，知识持续复利增长。
3. **三层架构照搬**，但第三层落在 `Skill` 而非仓库内文件：`raw/`（你写）→ `wiki/`（LLM 写）→ `Skill`（共同演进）。
4. **命令集比原构想多三个**：`init`（创建并注册知识库）、`wipe`（删除/重置，有回收站）、`test`（自动化测试）。
5. **自然语言意图识别是显式设计目标** —— README 用一张表列出「你说的话 → 执行的操作」，明确「你不需要记住任何命令」。
6. **目录结构与本仓库高度一致**：`wiki/{index,log,overview,conventions,sources,entities,concepts,analyses}`。
7. **依赖安装**：`pip install -r skills/wiki/scripts/requirements.txt` —— 与原构想「零依赖、按需自建工具」的取向不同。

## 摘要

README 的论证结构是：先给出「解释器 vs 编译器」的对比，再展示三层架构表，然后是四步快速开始（安装 → 初始化 → 收录 → 查询）。

安装方式是把它当作 Claude Code 的全局 Skill：`cp -r second-brain-skill/skills/wiki ~/.claude/skills/wiki`。初始化 `/wiki init` 会让用户选择路径、名称和语言（zh/en）。

它支持 Markdown / PDF / 图片三种素材格式，并明确「一次收录可能触发 10-15 个页面的创建或更新」—— 与原构想一致。

文档体系包含三份：`docs/user-guide.md`（使用手册，含 Obsidian 集成与 OpenClaw 接入）、`skills/wiki/IDEA.md`（设计理念）、`skills/wiki/README.md`（技术文档）。

## 与本库既有页面的关系

- **印证**了 [[three-layer-architecture]] 与 [[ingest-query-lint]] —— 目录结构与工作流几乎逐项对应。
- **补充**了原构想中没有的 `conventions.md` 落点机制：README 明确列出「回答要标注来源 → 记录偏好到 conventions.md」。
- **补充**了 `init` / `wipe` / `test` 三个运维命令，原构想完全没提这些。
- **与 [[llm-wiki-pattern]] 存在一处张力**：把 schema 放进 Skill 而非仓库内文件，削弱了「共同演进」的可审计性。详见 [[second-brain-skill]]。

> [!warning] 两处待核
> 1. **License 不一致**：README 结尾写 MIT，但 GitHub API 的 `license` 字段为空（仓库根目录未见 LICENSE 文件）。
> 2. **描述与 README 不一致**：仓库 description 写「接入 Claude/ChatGPT」，README 标题写「接入 Claude Code」，正文只提 Claude Code。ChatGPT 是否真的支持未说明。

## 新出现的实体 / 概念

- 实体：ChavesLiu（未独立成页，仅出现一次）、OpenClaw（未独立成页）
- 概念：[[second-brain-skill]]（评估）

## 待办 / 开放问题

- [ ] 核实 LICENSE 文件是否真的缺失
- [ ] 查看 `skills/wiki/README.md` 与 `IDEA.md`，确认页面规范是否与本仓库的 `AGENTS.md` 有差异
- [ ] 确认 OpenClaw 是什么（Web 端运行环境？）

## 素材基本信息

- **仓库创建**：2026-04-14 ｜ **最后推送**：2026-04-15
- **采集时数据**：54 stars / 9 forks / Python / 默认分支 `main`

## 相关页面

- [[second-brain-skill]]
- [[llm-wiki-pattern]]
- [[2026-09-18-karpathy-llm-wiki]]

## 来源

- [[2026-09-18-second-brain-skill-readme]]
