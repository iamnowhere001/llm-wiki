---
title: 纯文本与 Git：知识库的基础设施
type: concept
slug: plain-text-and-git
tags: [基础设施, 版本控制, 约定]
created: 2026-09-18
updated: 2026-09-18
sources: [2026-09-18-karpathy-llm-wiki]
related: [llm-wiki-pattern, three-layer-architecture, index-and-log]
evidence_tier: single
confidence: high
status: active
---

# 纯文本与 Git：知识库的基础设施

> 整个 wiki 就是「一个装 Markdown 文件的 git 仓库」。这不是实现细节，而是 [[llm-wiki-pattern]] 能成立的前提 —— 没有版本历史，「人类与 LLM 共同演进 schema」就是不可审计的。

> [!warning] 孤证 —— 本页仅 1 份素材支撑
> 支撑本页的只有 [[2026-09-18-karpathy-llm-wiki]]，尚未获得第二份独立来源的交叉验证。
> **引用本页结论时应带着这个前提**，或先补一份独立来源把它升到 `crossed`。

## 要点

- 作者的原话：*The wiki is just a git repo of markdown files. You get version history, branching, and collaboration for free.*
- **纯文本**带来的是可移植性与可 diff 性：任何编辑器能开、`grep` 能搜、LLM 天然能读写。
- **Git** 带来的是可回溯性：LLM 改错了能回退，矛盾如何被解决有据可查。
- 与 [[three-layer-architecture]] 的关系：schema 层要「共同演进」，而演进的记录必须存在同一个仓库里。
- 二进制素材（PDF、图片）是纯文本假设的例外，需要单独处理。

## 机制 / 原理

**为什么必须是纯文本。** 知识库要活十年，就不能绑定在任何单一工具上。Markdown 的好处是它同时满足四个约束：

1. **任何编辑器都能打开。** 见 [[obsidian]] —— 换工具不用迁移数据。
2. **可以 diff。** 这是最关键的一点：LLM 一次改 15 个页面，如果格式不可 diff，人类根本无法审核。可 diff 才使「人类只读」这个分工成立 —— 因为审核成本足够低。
3. **LLM 原生可读写。** 不需要解析专有格式，也不需要导出步骤。
4. **可被 unix 工具处理。** 作者举的例子：日志条目用固定前缀，就能 `grep "^## \[" wiki/log.md | tail -5`。

**为什么必须进版本控制。** 三个具体收益：

- **回退。** LLM 误删或误改页面时能恢复。这是最实际的收益。
- **审计「共同演进」。** schema 层（`AGENTS.md`）改动频繁。只有它在仓库里，才能回答「三周前这条规则是什么样」。
- **冲突解决留痕。** 新素材推翻旧结论时，`git log` 能显示这次修订发生在什么时候、依据哪份素材。

**为什么这对 LLM 协作尤其重要。** 人类维护知识库时，改动少而慢，出错可以靠记忆弥补。LLM 一次改动 15 个文件，且每次会话都是冷启动 —— 没有版本历史，就无法判断「这个页面为什么长这样」。

## 边界与反例

- **二进制素材会撑爆仓库。** PDF、扫描件、大图放进 git 会让仓库体积不可控。可选方案：Git LFS，或干脆把 `raw/assets/` 排除出版本控制（代价是素材失去历史）。**本仓库目前的取舍：素材纳入版本控制，因为规模还小；规模变大后再考虑 LFS。**
- **版本控制不能替代 lint。** Git 记录「改了什么」，但不判断「改得对不对」。矛盾、过期、该建未建仍然要靠 [[wiki-lint]]。
- **分支协作对单人场景价值有限。** 作者提到 branching，但个人知识库很少真正用到分支 —— 主要收益还是回退与历史。
- **纯文本假设不成立于图片密集型领域。** 如果素材主要是图表、扫描件，这个模式的收益会明显下降。

## 与其他页面的关系

- 是 [[three-layer-architecture]] 中「共同演进」的可行性前提。
- 让 [[index-and-log]] 的日志格式约定（固定前缀 + grep）成为可能。
- 与 [[obsidian]] 互补：Obsidian 是阅读层，git 是历史层。
- 本仓库已初始化为 git 仓库，`site/` 与 `.workbuddy-ai/` 通过 `.gitignore` 排除。

## 开放问题

- [ ] `raw/assets/` 在什么规模下必须切换到 Git LFS？
- [ ] 是否应该给每次 ingest 打一个 tag（如 `ingest-2026-09-18-karpathy`），让「某份素材带来的全部改动」可以一次性 diff？

## 来源

- [[2026-09-18-karpathy-llm-wiki]]
