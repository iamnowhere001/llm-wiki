---
title: Birgitta Böckeler
type: entity
slug: birgitta-bockeler
tags: [人物, AI, 工程, Thoughtworks]
created: 2026-09-19
updated: 2026-09-19
sources: [2026-09-19-bockeler-harness-engineering-coding-agent-users]
related: [harness-engineering, guides-and-sensors, harness]
evidence_tier: single
confidence: high
status: active
---

# Birgitta Böckeler

> Thoughtworks 的 Distinguished Engineer —— **harness 这个话题上目前最系统的一份分析的作者**。

> [!note] 本页是孤证，但素材是**本人一手署名文章**
> 全部信息来自她署名的 [[2026-09-19-bockeler-harness-engineering-coding-agent-users]]（`kind: essay`）。
> **这是一手文本，不是转述** —— 本库 `evidence_tier` 只认 `paper`，故记 `single`。

> [!note] 一处必须记住的署名事实
> 她的文章**挂在 `martinfowler.com` 域名下**，因此被大量中文转述记作「Fowler 的文章」。
> **这是错的。** 作者是 Böckeler 本人。正确说法：**Fowler 站点上、由 Böckeler 署名的文章**。
> 本库已把这条记入该 sources 页，并要求**系统排查同类错误**。

> [!warning] 孤证 —— 本页仅 1 份素材支撑
> 支撑本页的只有 [[2026-09-19-bockeler-harness-engineering-coding-agent-users]]，尚未获得第二份独立来源的交叉验证。
> **引用本页结论时应带着这个前提**，或先补一份独立来源把它升到 `crossed`。

## 要点

- **身份**：Thoughtworks 的 Distinguished Engineer，AI-assisted delivery 方向；
  自述有 20 多年开发者 / 架构师 / 技术负责人经验（据其文章页的作者简介）。
- **她对本议题的贡献**：
  ① 把 `Agent = Model + Harness` 这个「太宽」的定义**收窄到「外部 harness」**；
  ② 提出 **guides / sensors** 二分（见 [[guides-and-sensors]]）；
  ③ 提出 **computational vs inferential** 维度；
  ④ 给出 harness 的**三类 regulation category**（maintainability / architecture fitness / behaviour）。
- **她的诚实之处**：明确指出 **behaviour harness 远未成熟**；
  并承认 harness 隐喻本身撑不住（"Metaphors only go so far"）。

## 她划出的三类 regulation category

| 类 | 管什么 | 她的评价 |
|---|---|---|
| Maintainability harness | 内部代码质量与可维护性 | 「目前最容易做的一类」 |
| Architecture fitness harness | 架构适应度（Fitness Functions） | —— |
| **Behaviour harness** | **功能行为是否正确** | 「房间里的大象」；**远未成熟** |

> [!note] 第三类对本库的意义
> **Behaviour harness 未成熟**，意味着连团队尺度都还没解决「怎么验证 agent 做出来的东西功能上对不对」。
> 这是 [[harness]] 项目「个人如何高效实践」维度的一条**负面证据** ——
> 个人尺度不可能跳过团队尺度尚未解决的问题。

## 待办

- [ ] 她 2026-02-17 的初版 memo 未收录
- [ ] 她提到的 "harness templates" 未收录
- [ ] 排查本库是否还有其他「martinfowler.com → 误记为 Fowler」的错误

## 相关页面

- [[harness-engineering]]
- [[guides-and-sensors]]
- [[harness]]
- [[2026-09-19-bockeler-harness-engineering-coding-agent-users]]

## 来源

- [[2026-09-19-bockeler-harness-engineering-coding-agent-users]]
