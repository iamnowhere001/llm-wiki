---
title: Guides 与 Sensors（前馈控制与反馈控制）
type: concept
slug: guides-and-sensors
tags: [AI, Agent, harness, 控制论]
created: 2026-09-19
updated: 2026-09-19
sources: [2026-09-19-bockeler-harness-engineering-coding-agent-users]
related: [harness-engineering, harness, cybernetic-learning, wiki-lint, agents-md]
evidence_tier: single
confidence: medium
status: active
---

# Guides 与 Sensors（前馈控制与反馈控制）

> Böckeler 给出的 harness 内部二分：**guides 在 agent 动手前引导，sensors 在动手后检测** —— 合起来构成一个自纠错回路。

> [!note] 本页是孤证
> 全部内容来自 [[2026-09-19-bockeler-harness-engineering-coding-agent-users]] 一份素材。
> 该素材是**作者一手文本**（`kind: essay`，非转述），但本库 `evidence_tier` 只认 `paper`，故记 `single`。

> [!warning] 孤证 —— 本页仅 1 份素材支撑
> 支撑本页的只有 [[2026-09-19-bockeler-harness-engineering-coding-agent-users]]，尚未获得第二份独立来源的交叉验证。
> **引用本页结论时应带着这个前提**，或先补一份独立来源把它升到 `crossed`。

## 要点

- **guides = 前馈**：在 agent 行动**之前**塑造它的行为（规则文件、示例、约束）。
- **sensors = 反馈**：在 agent 行动**之后**检测结果（linter、测试、可观测性）。
- 两者**不是二选一** —— Böckeler 把它们并列为 harness 的两种控制手段。
- 另有一个正交维度：**computational vs inferential**（机械可判定 vs 需要判断）。
- **回路的关键**：sensor 发现的问题，应当被**固化回 guide** —— 这正是 harness engineering 的核心动作。

## 正文

### 二分本身

Böckeler 把 harness 的控制手段分成两类（原文行 67–93）：

| | Guides | Sensors |
|---|---|---|
| 方向 | **前馈**（feedforward） | **反馈**（feedback） |
| 时机 | agent 动手**前** | agent 动手**后** |
| 作用 | 提高一次做对的概率 | 让问题在到达人眼之前暴露 |
| 本库实例 | `AGENTS.md`、[[schema]] | [[wiki-lint]]、`seed_evidence_tier.py` |

**两者服务于同一目标的两个半边** —— 这也是 Böckeler 对「外部 harness」的定义：
「提高 agent 一次做对的概率」+「提供反馈回路让问题自我修正」。

### 正交维度：computational vs inferential

Böckeler 另给一组切法（原文行 67–85）：**computational** 是机械可判定的
（linter、结构测试、类型检查），**inferential** 是需要判断的（代码审查、设计评审）。

**这条维度的实际价值**：它解释了为什么 harness 无法完全自动化 ——
**inferential 的那一半必须由人（或另一个模型）承担**，而且它的质量无法机械保证。

### 回路：sensor 的结果要固化回 guide

单有 sensors 只是「检测」；harness engineering 的核心动作是**把检测到的问题固化进 guides**，
使同一类错误不再发生。Hashimoto 的原话是「engineer a solution such that the agent never makes
that mistake again」（见 [[harness-engineering]]）。

**因此 guides 与 sensors 不是两个独立清单，是一个循环的两端。**

## 与其他页面的关系

- **是 [[harness-engineering]] 的机制层展开**。
  **被 [[harness-explained]] 的「最小 harness 清单」直接使用** —— 那张表按 guides / sensors 二分裁剪，
  并且它记下了本页指出的那个空白：**Böckeler 的三类 regulation category 描述的是监管的对象，
  没有描述「把一次错误固化成一条永久规则」这个动作** —— 而后者才是 harness engineering 的核心动作。
- **与 [[cybernetic-learning]] 的关系需要检验**：后者讲「目标 → 误差信号 → 过滤器」。
  guides / sensors 看起来是它的具体化，但**「固化」这一步在 cybernetic-learning 里没有对应物** ——
  控制论讲的是系统持续接收误差信号并调整；harness 讲的是**把一次误差变成一条永久规则**。
  **后者引入了「规则会累积、也会腐坏」这个控制论框架里没有的问题。**
- **与 [[wiki-lint]]**：本库的 `lint` 是一个标准的 sensor。它符合 Böckeler 的 computational 类。
- **与 [[agents-md]]**：本库的 `AGENTS.md` 是一个标准的 guide（前馈）。**本库此前只用「常驻成本」这一个视角看它，
  本页提供了第二个视角。**

## 待办 / 开放问题

- [ ] Böckeler 提到的 "harness templates" 未收录，可能与 guides 的落地形式有关
- [ ] 「computational / inferential」这一对术语是否为 Böckeler 原创，未核

## 来源

- [[2026-09-19-bockeler-harness-engineering-coding-agent-users]]
