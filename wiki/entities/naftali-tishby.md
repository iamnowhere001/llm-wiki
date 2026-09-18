---
title: 纳夫塔利·蒂什比（Naftali Tishby）
type: entity
slug: naftali-tishby
tags: [信息论, 机器学习, 深度学习, 以色列, 一手研究者]
created: 2026-09-18
updated: 2026-09-18
sources: [2026-09-18-learning-is-forgetting]
related: [information-bottleneck, compression-as-intelligence, andrew-saxe, thomas-griffiths]
confidence: medium
status: active
---

# 纳夫塔利·蒂什比（Naftali Tishby，1952–2021）

> 信息瓶颈方法的提出者。他把「学习 = 压缩」从一句哲学话变成了一个**可以算的量**，
> 并且**本人在 2015–2017 年就把它用到了深度学习上** —— 这一点本素材没讲，但它决定了该怎么读那篇 2026 年的论文。

## 要点

- 1952 年生，**2021 年 8 月 9 日逝世**（希伯来大学讣告）。耶路撒冷希伯来大学计算机科学教授，
  Edmond and Lily Safra 脑科学中心 Ruth and Stan Flinkman 脑科学研究主席。**（以上已外部核实，来源为中文百科与报道，非一手讣告原文）**
- **1999 年**与 Fernando Pereira、William Bialek 共同提出**信息瓶颈方法**（Allerton 会议论文）。
- **2015 年**与学生 Noga Zaslavsky 发表《Deep Learning and the Information Bottleneck Principle》（arXiv:1503.02406）—— **主张深度学习本身就是一个信息瓶颈过程**。
- **2017 年**与学生 Ravid Shwartz-Ziv 发表《Opening the Black Box of Deep Neural Networks via Information》，用实验展示了训练中的压缩过程。
- Hinton 听过他的报告后曾写邮件说：「信息瓶颈极其有趣，我要再听一万遍才能真正理解它……或许它就是解开谜题的那把钥匙。」（转述，标（未验证））

## 为什么本库给他单独建页

**理由不是「他提出了一个重要概念」，而是本库需要他来纠正一处可能的误读。**

[[2026-09-18-learning-is-forgetting]] 的叙事给人的印象是：

> 信息瓶颈是 Tishby 二十多年前的老理论 → 一直算不动大模型 → **2026 年这篇论文第一次把它扩展到大模型**，
> 并发现了「训练分两阶段（先装箱、再扔东西）」。

**按外部核查到的时间线，这个叙事至少有一半是错的**：

| 环节 | 素材的暗示 | 核查到的实际情况 |
|---|---|---|
| 谁把 IB 用于深度学习 | 2026 年那篇论文 | **Tishby 本人 2015 年就提出了**（Zaslavsky & Tishby；2017 年 Shwartz-Ziv & Tishby 做了实验） |
| 「两阶段」是谁的发现 | 2026 年那篇论文 | **很可能来自 Shwartz-Ziv & Tishby 2017** —— 该论文正是用 IB 分析 DNN 训练并展示「先拟合、后压缩」（**本库标（未验证）—— 未读该文原文**） |
| 2026 年论文的贡献 | 「发现了两阶段」 | 更可能是**把 IB 分析扩展到 LLM 规模**（解决「算不动」的方法问题），并**把表征结构连到下游表现** —— 后者是摘要里明确写的 |

**这个纠正不改变素材的结论，但改变了它的价值定位**：那份素材让人以为自己在读一个新发现，
实际上读到的是**一个 2015 年提出、2017 年实验、2018 年被质疑、2026 年在 LLM 规模上重检的**研究脉络的通俗版。

## 与其他页面的关系

- 是 [[information-bottleneck]] 的**提出者** —— 该页目前的可追溯性几乎全部落在他身上。
- 与 [[andrew-saxe]] 构成**正方 / 反方**一对：Saxe 等 2018（ICLR）《On the Information Bottleneck Theory of Deep Learning》
  正是对 Tishby 2015/2017 这一支的批评。**这是本库目前唯一一对「同一主张的正反双方」，
  且是本库第一次在收录素材的同一天就拿到了反方。**
- 与 [[thomas-griffiths]] 的关系：2026 年那篇论文（Griffiths 为作者之一）在这个脉络里的位置，
  本库判断是「**在新规模上重检一个已被质疑的旧主张**」，而非「提出新主张」。**该判断为本库所加，标（未验证）。**

## 开放问题

- [ ] Tishby, Pereira & Bialek 1999 原文（Allerton）未收录 —— 可一键取回
- [ ] Shwartz-Ziv & Tishby 2017 原文未收录 —— 需读它才能确认「两阶段」的真正出处
- [ ] 本页生平段来自中文百科与报道，**非一手讣告或机构页面**，全部标（未验证）

## 来源

- [[2026-09-18-learning-is-forgetting]]（素材只说「二十多年前 Tishby 提出来的」，未给文献、未提 2015/2017 两篇）
- 外部核查：中文百科与科技媒体报道（生平）、arXiv:1503.02406 与 2017 年论文的公开引用（时间线）
