---
title: 安德鲁·萨克斯（Andrew M. Saxe）与 IB 理论的争议
type: entity
slug: andrew-saxe
tags: [深度学习, 信息论, 反方, 可重复性, 争议]
created: 2026-09-18
updated: 2026-09-18
sources: [2026-09-18-learning-is-forgetting]
related: [information-bottleneck, naftali-tishby, compression-as-intelligence, thomas-griffiths]
evidence_tier: single
confidence: medium
status: active
---

# 安德鲁·萨克斯（Andrew M. Saxe）与 IB 理论的争议

> 本库**第一次在收录素材的同一天就拿到了反方**。这条记录的存在本身比它的内容更重要 ——
> 它证明「顺手查一下这个主张有没有人反对」是一条高收益的动作，而本库此前多次没收就先信了。

> [!warning] 孤证 —— 本页仅 1 份素材支撑
> 支撑本页的只有 [[2026-09-18-learning-is-forgetting]]，尚未获得第二份独立来源的交叉验证。
> **引用本页结论时应带着这个前提**，或先补一份独立来源把它升到 `crossed`。

## 要点

- Saxe 等（2018, ICLR）《On the Information Bottleneck Theory of Deep Learning》是对
  [[naftali-tishby]] 一支（2015 提出、2017 实验）的**直接批评**。
- 论文中一句被反复引用的表述：**「the compression phase, when it exists, does not arise from stochasticity in training」**
  —— 注意 **「when it exists」（当它存在时）** 这个限定语。它意味着：**压缩阶段不是普遍现象，是有条件的。**
- 该文后被扩展为期刊版本（*Journal of Statistical Mechanics*, 2019）。
- **对本库的直接后果**：[[2026-09-18-learning-is-forgetting]] 讲的「训练必经装箱期与压缩期」，
  是**一个有争议的主张**，不是教科书事实。**素材把它当作既定事实在讲，没有任何限定。**

## 为什么这条记录重要

本库在 2026-09-18 一天之内，为一个新收录的概念（[[information-bottleneck]]）同时拿到了：

| | 来源 | 状态 |
|---|---|---|
| 提出者 | Tishby, Pereira & Bialek 1999 | 未收录原文 |
| 用于深度学习 | Tishby & Zaslavsky 2015 / Shwartz-Ziv & Tishby 2017 | 未收录原文 |
| **反方** | **Saxe et al. 2018, ICLR** | **未收录原文，但已确认存在** |
| 在 LLM 规模上重检 | Conklin et al. 2026（arXiv:2604.07569, ICLR 2026） | 未收录原文，仅读摘要 |

**这是一个罕见的机会**：本库在概念入库的第一天就知道了它有争议，
而不是等到基于它写了三页结论之后才发现。**本库在 [[information-bottleneck]] 与
[[2026-09-18-learning-is-forgetting]] 两页里都已显式写入这条争议。**

## 与其他页面的关系

- 是 [[information-bottleneck]] 的**反方** —— 该页的「边界与反例」一节直接引用本页。
- 与 [[naftali-tishby]] 构成一对：前者质疑，后者主张。**两者的原文本库均未收录，故本库不裁定谁对。**
- 与 [[thomas-griffiths]] 的潜在关系（本库自造的判断，`confidence: low`）：
  2026 年那篇论文若用新方法（素材称「软熵估计」）重检 IB，**很可能正是在回应 Saxe 等人的质疑** ——
  因为 Saxe 的一条批评路径就是**互信息估计方法本身不可靠**（在确定性网络里分箱估计会失真）。
  **若这个判断成立，2026 年论文的性质就不是「验证」而是「救回」** —— 差别很大，需读原文才能定。
- 与 [[compression-as-intelligence]] 的关系：本页的争议**不冲击**那条更一般的命题。
  被质疑的是「深度网络训练必经压缩阶段」这个具体观察，**不是**「智能 ≈ 压缩」这个框架。

## 开放问题

- [ ] **取回 Saxe et al. 2018 原文**（ICLR 版本 PDF 已定位到公开链接）—— 需确认「when it exists」的具体条件（激活函数类型？）
- [ ] 取回 Conklin et al. 2026 原文，确认它是否正面回应了 Saxe 的批评
- [ ] Saxe 的生平与机构未核实（本页只记其作为该文第一作者的身份）

## 来源

- 本页**不由素材派生** —— 素材里完全没有提到这个争议。
  它来自本库在收录核查时主动做的「反方检索」，是本库自己的产物。
- 外部核查：Saxe et al. 2018 ICLR 论文 PDF（saxelab.org / IBM Research 页面）、2019 年期刊扩展版
