---
title: Harness engineering for coding agent users（Birgitta Böckeler，2026-04-02）
type: source
slug: 2026-09-19-bockeler-harness-engineering-coding-agent-users
tags: [AI, Agent, harness, Thoughtworks]
created: 2026-09-19
updated: 2026-09-20
sources: [2026-09-19-bockeler-harness-engineering-coding-agent-users]
related: [harness, harness-engineering, agents-md, 2026-09-19-trivedy-anatomy-of-agent-harness]
confidence: high
status: active
---

# Harness engineering for coding agent users（Birgitta Böckeler，2026-04-02）

> 目前对 harness **最系统的一份分析** —— 给出 guides / sensors 二分、computational vs inferential 维度，以及三类 regulation category。

- **作者**：Birgitta Böckeler（Thoughtworks 的 Distinguished Engineer）
- **链接**：https://martinfowler.com/articles/harness-engineering.html
- **发表**：2026-04-02（文末记 2026-02-17 另有一份初版 memo）
- **素材路径**：`raw/2026-09-19-bockeler-harness-engineering-coding-agent-users.md`（241 行）

> [!warning] 署名纠错 —— 本库第一处此类
> 本页**挂在 `martinfowler.com` 域名下，但作者不是 Martin Fowler**，是 **Birgitta Böckeler**。
> 本库此前的调研笔记与多份中文转述都把此文记作「Fowler 的文章」—— **这是错的**。
> 正确说法：**Fowler 站点上、由 Böckeler 署名的文章**。
> **同类错误值得系统排查**：中文圈有把 `martinfowler.com` 上的文章一律归给 Fowler 的倾向。
> 这条已记入本页「待办 / 开放问题」。

> [!note] 行号核对
> 本节行号已回原文逐条核对（`wc -l` = 241）。

## 关键要点

1. **外部 harness 的两个目标**（正文）：提高 agent **一次做对**的概率；提供**反馈回路**，让问题在到达人眼之前自我修正。
2. **guides / sensors 二分**（行 67–93）：guides 是**前馈**（动手前引导），sensors 是**反馈**（动手后检测）。
3. **computational vs inferential 维度**（行 67–85）：区分「机械可判定」的控制与「需要判断」的控制。
4. **三类 regulation category**：
   - **Maintainability harness**（行 135–139）—— 管内部代码质量与可维护性，作者称「目前最容易做的一类」
   - **Architecture fitness harness**（行 147）—— 架构适应度函数（Fitness Functions）
   - **Behaviour harness**（行 156–167）—— 功能行为，作者称它是「房间里的大象」，并明确说**这一类远未成熟**：
     原文 "we still have a lot to do to figure out good harnesses for functional behaviour that increase our confidence enough to reduce supervision and manual testing."
5. **`Agent = Model + Harness` 是引用而非原创**（行 54）：Böckeler 引用的是 LangChain 的 [[2026-09-19-trivedy-anatomy-of-agent-harness]]，
   随即指出该定义**太宽**（"a very wide definition"），于是把它收窄到「**外部 harness**」——即用户为自己的场景和系统所建的那部分。
6. **作者自己承认隐喻撑不住**（行 56）："Metaphors only go so far" ——
   有人向她指出「往 harness 外面再套 harness 说不通：**你试过往狗的身体内侧套挽具吗？**」她接受这个拉伸，理由是「如果它有助于厘清这个词的用法」。

## 摘要

文章的起点是一个工程判断：**要让 coding agent 在更少监督下工作，就得有办法提高我们对它结果的信心。**
作者提出的心智模型把 context engineering 与 harness engineering 的概念合到一起。

她的关键动作是**收窄定义**：`Agent = Model + Harness` 这个说法太宽（按它算，系统提示词、检索机制、编排系统都算 harness），
所以她把讨论限定在「**coding agent 的用户**能自己建的那一层」—— 即外部 harness。她承认 harness 套 harness 的隐喻拉伸，但认为可用。

然后她给出两套正交的切法：**guides / sensors**（前馈 vs 反馈）与 **computational / inferential**（机械 vs 判断）。
再落到三类 regulation category，其中 **behaviour harness 被她明确标为未解** —— 这一条对本库「个人如何高效实践」维度是负面证据：
**连团队尺度都还没解决「怎么验证功能行为」，个人尺度更不可能直接照搬。**

## 与本库既有页面的关系

- **本项目的第二份一手素材**，且是**唯一系统化的分析**。
- **与 [[2026-09-19-trivedy-anatomy-of-agent-harness]] 是上下游关系**：Trivedy 给出定义，Böckeler 引用它并收窄它。
  **本库要显式记录这个链条** —— 因为中文转述常把 `Agent = Model + Harness` 直接算作「共识定义」，
  而实际上**提出者是一次「补定义」，第一位引用者立刻说它太宽**。
- **对本库 [[harness]] 项目「个人如何高效实践」维度的一条负面证据**：Behaviour harness 未成熟
  → 团队尺度都做不到「减少人工监督」，个人尺度更不能照搬。**这条要写进项目页的缺口表依据里。**
- 与 [[agents-md]] 的关系：Böckeler 的 guides 概念把 `AGENTS.md` 归为**前馈控制**，本库此前只把它当作「常驻成本」，
  **这是本库没有的视角**。

## 新出现的实体 / 概念

- 实体：**Birgitta Böckeler**、**Thoughtworks**
- 概念：**guides / sensors**（前馈 / 反馈控制）、**regulation category 三类**、**computational vs inferential**

## 已知缺失

- 页面顶部的作者照片与简介块在提取时被删除（作者信息已入 frontmatter）。
- 文末修订历史保留（含 2026-02-17 的初版 memo 链接，**该 memo 未收录**）。
- 作者提到的 **"harness templates"** 未在本文展开，指向了别处 —— 若本项目要落地「个人最小 harness 清单」，**这是需要追的一条线**。

## 待办 / 开放问题

- [ ] 追 "harness templates" 的指向（正文提及但未展开）
- [ ] 核对文中 "Fitness Functions" 的出处（作者当作既有概念使用）
- [ ] **系统排查本库是否还有其他「martinfowler.com → 误记为 Fowler」的署名错误**

## 相关页面

- [[harness]]
- [[harness-engineering]]
- [[agents-md]]
- [[2026-09-19-trivedy-anatomy-of-agent-harness]]
- [[2026-09-19-hashimoto-my-ai-adoption-journey]]
- [[2026-09-19-openai-harness-engineering-codex]]

## 归属判断

- **性质**：**一手**（作者本人署名文章）

## 来源

- [[2026-09-19-bockeler-harness-engineering-coding-agent-users]]
