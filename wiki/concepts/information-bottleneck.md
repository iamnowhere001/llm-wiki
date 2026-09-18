---
title: 信息瓶颈（Information Bottleneck）
type: concept
slug: information-bottleneck
tags: [信息论, 压缩, 表征, 大模型, 学习]
created: 2026-09-18
updated: 2026-09-18
sources: [2026-09-18-learning-is-forgetting]
related: [compression-as-intelligence, learning-as-forgetting, naftali-tishby, thomas-griffiths, schema-psychology, llm-wiki-pattern, retrieval-practice]
confidence: medium
status: active
---

# 信息瓶颈（Information Bottleneck）

> **好的表征 = 对输出高度预测，同时对输入高度压缩。** 学习不是把输入存下来，而是把「与预测目标无关的部分」扔掉。

## 要点

- 提出者 [[naftali-tishby]] 与合作者（1999），最初是信息论框架，二十多年后被用于解释大模型的训练动态。
- 两个量：**复杂度 I(X;Z)**（表征里还剩多少原始输入的信息，越低越好）与**表达力 I(Z;Y)**（表征里有多少关于输出的有用信息，越高越好）。
- 把这两个量画成坐标系（横轴复杂度、纵轴表达力），理想终点是一条**斜率为 1 的对角线** —— 留下的每一份信息都有用，没有一件多余。这条线就是**信息瓶颈边界**。
- 2026 年 Conklin 等八人的论文（arXiv:2604.07569，ICLR 2026）把这个框架**扩展到了大模型规模**，结论是预训练后的模型**逼近**这条边界。

## 定义与背景

信息瓶颈方法要解决的问题是：给定输入 X 与目标 Y，如何学到一个**压缩的表征 Z**，使得 Z 尽可能少地保留 X 的信息、同时尽可能多地保留关于 Y 的信息。

形式上是最大化：

```
I(Z;Y) − β · I(X;Z)
```

即「表达力减去 β 倍的复杂度」，β 控制压缩的激进程度。这个权衡的帕累托前沿就是**信息瓶颈边界**。

**为什么它此前没被用在大模型上**：传统方法要估计高维空间里的互信息，需要把空间离散化分箱，维度一高就组合爆炸。**这是本素材给出的解释，标（未验证）** —— 论文摘要只说该方法「可在大规模部署」，未说明被绕开的具体障碍。

## 脉络（本段为本库外部核查所得，素材未给出）

**本素材的叙事会让人以为「IB → 深度学习 → 大模型」是 2026 年那篇论文一次走完的。核查到的时间线不是这样：**

| 年份 | 事件 | 状态 |
|---|---|---|
| 1999 | Tishby, Pereira & Bialek 提出信息瓶颈方法 | 原文未收录 |
| 2015 | Tishby & Zaslavsky《Deep Learning and the Information Bottleneck Principle》—— **主张深度学习本身就是 IB 过程** | 原文未收录 |
| 2017 | Shwartz-Ziv & Tishby 用实验展示训练中的压缩过程 | 原文未收录 |
| **2018** | **Saxe et al.（ICLR）《On the Information Bottleneck Theory of Deep Learning》—— 直接批评** | 原文未收录，**已确认存在** |
| 2026 | Conklin et al.（arXiv:2604.07569, ICLR 2026）在 LLM 规模上重检 | 原文未收录，仅读摘要 |

**这条时间线改变了对 2026 年论文的定位**：它更可能是「**在新规模上重检一个已被质疑的旧主张**」，
而不是「发现了一个新现象」。见 [[andrew-saxe]] 与 [[naftali-tishby]]。

## 机制 / 原理

按本素材（A 段，署名）转述的论文叙事，训练分两个阶段：

| 阶段 | 素材用名 | 发生什么 |
|---|---|---|
| 1 | **装箱期**（fitting phase） | 训练早期，模型增加表征中关于输出的信息量 —— 先看到，才能筛选 |
| 2 | **扔东西期**（compression phase） | 损失趋平后，模型不再增加新信息，转而**减少表征中关于输入的信息**，同时保持预测能力不掉 |

**论文摘要支持这个两阶段的「结论」，但不支持素材讲的细节**：

- 摘要原文：「pre-training results in models that are **optimally compressed for next-sequence prediction, approaching the Information Bottleneck bound**」—— 支持「逼近边界」。
- 摘要原文：「Across an array of open weights models, **each compresses differently**, likely due to differences in the data and training recipes used」—— 说的是**模型之间压缩方式不同**。
- 素材讲的「7B 紧贴边界、1B 在该压缩时开始震荡」（归因为参数容量不足）—— **摘要中完全未出现，标（未验证）**。
  而且**这两句话的因果方向不一样**：摘要说差异来自数据与训练配方，素材说差异来自参数规模。

## 边界与反例

- **它不是一个「越大越压缩」的定律。** 摘要明确说不同模型家族压缩方式**各自不同**，
  所以不存在一条所有模型都走的统一轨迹。**素材的「小模型没有容量完成压缩」是把观察改写成了机制断言。**
- **「逼近边界」不等于「到达边界」。** 摘要用的是 approaching，不是 reaching。
- **它衡量的是表征结构，不是能力。** 摘要里真正可操作的发现是
  「**压缩的最优性与表征中的信息量可以预测下游 benchmark 表现**」——
  这是把结构连到性能的那一环，**而本素材的通俗版完全没讲这一条**。
- **容易与 [[schema-psychology]] 混淆**：图式是「把多个元素打包成一个整体」，信息瓶颈是「把与目标无关的信息扔掉」。
  两者方向一致（都在减少占用），但**图式讲的是打包，信息瓶颈讲的是丢弃** —— 打包后东西还在，丢弃后不在了。

## 与其他页面的关系

- 是 [[compression-as-intelligence]] 的**技术版本**：后者是哲学命题（智能＝压缩），本页给出了可计算的量。
- 是 [[learning-as-forgetting]] 的**机制解释**：为什么遗忘是学习的组成部分 —— 因为压缩要求丢弃。
- 与 [[llm-wiki-pattern]] 的关系（本库自己的联想，`confidence: low`）：本库把「编译」当作核心动作，
  而编译的本质按本页就是**有损压缩**。**本库此前从未给「编译」下过定义**，本页提供了一条候选定义。
- 与 [[retrieval-practice]] 的关系（本库自己的联想，`confidence: low`）：提取练习之所以有效，
  按本页的框架可以理解为「强制表征对输出保持高预测性」—— 但这只是本库的推断，素材与一手文献均未这么说。

## 开放问题

- [ ] **最高优先级**：把 arXiv:2604.07569 的 PDF 取回 —— 需要确认「两阶段」的表述、「软熵估计」这一方法名、以及 7B/1B 对比是否真的在论文正文里。
- [ ] Tishby, Pereira & Bialek 1999 原文未收录 —— 本页目前全部来自通俗转述 + 论文摘要。
- [ ] 「表征压缩度可预测下游表现」这条摘要里的发现，本素材没讲 —— 它的效应量有多大？是否有反例（压缩得更狠但表现更差的模型）？

## 来源

- [[2026-09-18-learning-is-forgetting]]（李继刚的通俗转述；**核心引注 arXiv:2604.07569 已外部核实为真**）
- 外部核查：arXiv:2604.07569 摘要页（八位作者、ICLR 2026、2026-04-08 提交）
