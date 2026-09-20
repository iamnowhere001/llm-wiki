---
title: The Anatomy of an Agent Harness（Vivek Trivedy，2026-03-10）
type: source
slug: 2026-09-19-trivedy-anatomy-of-agent-harness
tags: [AI, Agent, harness, LangChain]
created: 2026-09-19
updated: 2026-09-20
sources: [2026-09-19-trivedy-anatomy-of-agent-harness]
related: [harness, harness-engineering, 2026-09-19-bockeler-harness-engineering-coding-agent-users]
confidence: medium
status: active
---

# The Anatomy of an Agent Harness（Vivek Trivedy，2026-03-10）

> **`Agent = Model + Harness` 这个定义的原始出处** —— 而且它出现在一节标题为「Can Someone Please Define a "Harness"?」之下。

- **作者**：Vivek Trivedy（LangChain）
- **链接**：https://blog.langchain.com/the-anatomy-of-an-agent-harness/
- **发表**：2026-03-10
- **素材路径**：`raw/2026-09-19-trivedy-anatomy-of-agent-harness.md`（211 行）

> [!warning] 利益披露（按 [[schema]] §3.4 处理）
> 作者为 LangChain 员工，文末含 LangSmith（LangChain 自家 Agent 工程平台）的推广段
> 「See what your agent is really doing / Try LangSmith」。
> **降级的是行为，不是作者身份** —— 本文的定义与分类是可用的，但引用时须带 `confidence: medium` 这个前提。

> [!note] 行号核对
> 本节行号已回原文逐条核对（`wc -l` = 211）。

## 关键要点

1. **定义原句（行 39–41）**：
   > "**If you're not the model, you're the harness.**"
   > "A harness is every piece of code, configuration, and execution logic that isn't the model itself."
2. **提出方式本身就是信息**（行 35）：这一节的小标题是
   「**Can Someone Please Define a "Harness"?**」（谁能给 harness 下个定义？）——
   **说明这份定义是一次「补定义」动作，提出时业界并无共识。**
   这是本项目「定义」维度最值得记的一条：**该定义的权威性来自后续引用者的采纳，不来自任何标准组织。**
3. **TLDR（行 33）**："Agent = Model + Harness. Harness engineering is how we build systems around models to turn them into work engines.
   The model contains the intelligence and the harness makes that intelligence useful."
4. **harness 的具体构成清单**（行 41 之后）：文章给出一份具体列举 —— 本库若要回答「**个人最小 harness 是什么**」，这是最直接的材料。
5. **两条 Key Takeaways（行 28 之后）**：规划工具让 agent 分解任务、跟踪进度并随学习调整；
   **派生 subagent 并行处理独立子任务，各自持有隔离的上下文**。
6. **上下文是贯穿全文的核心约束**：文中多次围绕 context window 展开（行 78、132、136、138、146、148）。

## 摘要

文章要解决的问题写在标题里：**harness 这个词人人都在用，但没人给过定义。**

作者先给出一个极简切法 —— `Agent = Model + Harness`，并用一句话把它讲透：
**「如果你不是模型，你就是 harness。」** 他随即把 harness 界定为「一切不是模型本身的代码、配置与执行逻辑」，
并强调**原始模型不是 agent**：模型提供智能，harness 让这份智能变得有用。

文章随后从这一定义出发，推导出「今天的 agent 与明天的 agent 分别需要哪些核心组件」，
其中两个被放在 Key Takeaways 里：**规划工具**（分解任务、跟踪进度、随学习调整）与**subagent 并行**
（为独立子任务派生各自持有隔离上下文的子 agent）。

**上下文管理是全文的组织轴** —— 多处讨论都围绕 context window 展开。

## 与本库既有页面的关系

- **本项目的第三份一手素材**，也是 [[harness-engineering]] 这个概念页的**定义来源**。
- **与 [[2026-09-19-bockeler-harness-engineering-coding-agent-users]] 构成一条链**：
  本页**提出**定义 → Böckeler **引用并指出它太宽**，收窄到「外部 harness」。
  **本库必须显式记录这条链**：中文转述常把 `Agent = Model + Harness` 当作「业界共识定义」，
  而实际情况是**一次补定义 + 一次立即的收窄**。
- **对本库「个人如何高效实践」维度的正面材料**：本页的「harness 具体构成清单」是四篇里最接近
  「个人最小 harness 该包含什么」的一份 —— 尽管它写的是通用 agent，不是个人场景。
- **与本库的自我对照**：本库的 `AGENTS.md` / `lint` / `decisions.md` 在本文的分类下分别是
  「指令类 harness」「验证类 harness」「记忆类 harness」。**这条对照要写进 [[harness-engineering]]。**

## 新出现的实体 / 概念

- 实体：**Vivek Trivedy**、**LangChain**、**LangSmith**
- 概念：**`Agent = Model + Harness`**（见 [[harness-engineering]]）、**subagent 隔离上下文**

## 已知缺失

- 作者头像与社交链接在提取时被删除。
- 文末推广段保留（已在上方利益披露中标注）。
- 文中提到的「明天的 agent 需要的组件」部分**本库尚未逐条核对**，摘要只覆盖了 Key Takeaways 层面的内容。

## 待办 / 开放问题

- [ ] 逐条整理本页的「harness 构成清单」—— 它是「个人最小 harness」的直接材料来源
- [ ] 核对本页对 context window 的论述与 [[llm-wiki-pattern]] 的「编译」主张是否有可对照之处

## 相关页面

- [[harness]]
- [[harness-engineering]]
- [[2026-09-19-bockeler-harness-engineering-coding-agent-users]]
- [[2026-09-19-hashimoto-my-ai-adoption-journey]]
- [[2026-09-19-openai-harness-engineering-codex]]

## 归属判断

- **性质**：**一手**（作者署名），但**含利益披露**

## 来源

- [[2026-09-19-trivedy-anatomy-of-agent-harness]]
