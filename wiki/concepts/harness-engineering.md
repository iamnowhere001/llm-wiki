---
title: Harness Engineering（挽具工程）
type: concept
slug: harness-engineering
tags: [AI, Agent, harness, 工程实践]
created: 2026-09-19
updated: 2026-09-19
sources: [2026-09-19-hashimoto-my-ai-adoption-journey, 2026-09-19-openai-harness-engineering-codex, 2026-09-19-bockeler-harness-engineering-coding-agent-users, 2026-09-19-trivedy-anatomy-of-agent-harness]
related: [harness, agents-md, guides-and-sensors, cybernetic-learning, wiki-lint]
evidence_tier: crossed
confidence: medium
status: active
---

# Harness Engineering（挽具工程）

> 不改模型权重、只改造模型外部环境的一类工程实践 —— 目标是让 agent 少犯错，且犯错后能自己发现。

> [!note] 本页有**作者一手文本**支撑，但 `evidence_tier` 显示不出来
> 本页 4 份支撑素材**全部是作者本人的一手文本**（`kind: essay`），不是转述：
> Hashimoto 的命名原文、OpenAI 的实践报告、Böckeler 的系统分析、Trivedy 的定义原文。
> **但本库 `evidence_tier` 的判据是 `PRIMARY_KINDS = ("paper",)`，只看期刊论文** ——
> 因此本页只能算 `crossed`，**这不代表它是二手转述**。
> 本库已登记的同类实例：Bush 1945、Berners-Lee 1999、Luhmann 1981、Kotler 2021
> （见 [[llm-wiki-research]] 开放问题里的「待北洛裁定」）。**本页是这条判据缺陷的第 5–8 个实例。**
> 按 [[schema]] §1.2 的要求，此处**用文字显式声明**：**本页有一手文本支撑。**

## 关键要点

- **命名者自认不确定**：Mitchell Hashimoto 2026-02-05 首次使用该词，**原文自陈不知道业界有没有公认术语**。
- **定义来自一次「补定义」**：`Agent = Model + Harness` 出自 LangChain（2026-03-10），
  且它出现的那一节标题就是「Can Someone Please Define a "Harness"?」。
- **定义立刻被收窄**：Böckeler 引用它并指出「太宽」，收窄到「**外部 harness**」（用户自己建的那层）。
- **核心动作一句话**：发现 agent 犯错 → 工程化一个方案 → **让它永远不再犯**。
- **两种形式**：① 改规则文件（`AGENTS.md`）；② 写程序化的验证工具。
- **两个方向**：guides（前馈，动手前引导）/ sensors（反馈，动手后检测）。
- **⚠️ 术语状态**：**没有任何标准组织定义或维护它**。连最高可见度的采用者（OpenAI）
  在正文里都**不再使用这个词**（仅标题用了一次）。

## 正文

### 来历：一次自认不确定的命名

[[2026-09-19-hashimoto-my-ai-adoption-journey]] 的第 5 步是命名现场。原文：

> "I don't know if there is a broad industry-accepted term for this yet, but I've grown to calling this
> 'harness engineering.' It is the idea that anytime you find an agent makes a mistake, you take the time
> to engineer a solution such that the agent never makes that mistake again."

**这句话里最值得注意的是前半句。** 命名者本人当时并不知道它会不会成为通用术语 ——
因此本库记录这个词时，**不能说「业界公认」**，只能说「**被这几篇文本采用并互相引用**」。

### 定义：一次「补定义」，以及它立刻被收窄

[[2026-09-19-trivedy-anatomy-of-agent-harness]] 给出了最常被引用的切法：

> "**If you're not the model, you're the harness.**"
> "A harness is every piece of code, configuration, and execution logic that isn't the model itself."

**关键在于它出现的位置**：那一节的标题是「Can Someone Please Define a "Harness"?」。
**这说明当时这个词在被广泛使用却没有定义** —— 该文是去补这个洞的。

一个月后，[[2026-09-19-bockeler-harness-engineering-coding-agent-users]] 引用这个定义，
随即指出它**太宽**（"a very wide definition"），并收窄到她讨论的对象：
**外部 harness** —— coding agent 的**用户**能自己建的那一层。

**本库要显式记录这条链**：提出 → 立即收窄。
中文转述常把 `Agent = Model + Harness` 当作「业界共识定义」，**实际情况是这两个动作**。

### 边界：什么不算 harness

按 Böckeler 的收窄，**agent 自带的**（系统提示词、检索机制、编排系统）不算「外部 harness」。
她给的判据是**能不能被用户为自己的场景改造**。

> [!note] 这个边界有一处未解
> 「内置」与「外部」的界线**随产品而变** —— 今天算内置的，明天可能开放成配置项。
> 本库**没有找到任何一份材料讨论这个边界会漂移**。这属于本项目的真实缺口。

### 与 Prompt Engineering / Context Engineering 的关系

**⚠️ 本库在这个问题上没有一手支撑。**

中文技术社区普遍给出一个三段演进（Prompt → Context → Harness），并称三者是**嵌套**关系
（`Harness ⊇ Context ⊇ Prompt`）或**互补**关系。**这些说法本库只见到中文二手转述，
未能核到任何提出者的原文** —— 因此不写入本页作为事实。

已核到的只有一条**间接**证据：Böckeler 的文章摘要说她的心智模型是
「brings together emerging concepts from **context and harness engineering**」（把 context 与 harness
engineering 这两个新兴概念合到一起）—— 这**支持「两者是并列的两个领域」**，
但**不支持「三段演进」这个说法**。

**结论：三段论目前是「未获一手支撑」，不是「已被证伪」。** 已挂进 [[harness]] 的缺口表。

### 高可见度采用者的实际情况

[[2026-09-19-openai-harness-engineering-codex]] 的标题用了 "Harness engineering"，
但**正文里 harness 几乎不再出现** —— 除标题外仅 1 处技术性用法（「Evaluation harnesses」）
**且全文从未定义它**。

**本库的判法**：把 OpenAI 记作「**高可见度的采用者与示范者**」，而不是「提出者」。
中文圈「OpenAI 提出了 Harness Engineering」的说法与原文有实质差距。

## 与其他页面的关系

- **是 [[harness]] 项目的核心概念页** —— 该项目的「定义」维度主要靠本页承载。
  **该项目的交付物是 [[harness-explained]]** —— 本页是它的概念主干，它承载四个维度的展开。
- **与 [[guides-and-sensors]]**：后者是 Böckeler 给出的控制机制二分，是本页「两个方向」的展开。
- **与 [[agents-md]]**：`AGENTS.md` 是本页「第一种形式」的最常见载体。
  两者共享同一个张力（写多 vs 写少），见 [[agents-md]] 的「常驻成本」一节。
- **与 [[cybernetic-learning]]**：「发现错误 → 工程化方案 → 不再犯」**看起来是**
  「目标 → 误差信号 → 过滤器」的一个实例。**本库要检验这个对应是否成立，而不是顺手类比。**
  目前可说的是：cybernetic-learning 讲的是**系统层面**的误差信号，
  harness 讲的是**把人的判断固化成机器可执行的规则** —— 后者多了一步「固化」，这一步是否等价于「过滤器」，未验证。

## 待办 / 开放问题

- [ ] **三段演进（Prompt → Context → Harness）缺一手** —— 需找到「Context Engineering」一词的原始出处
- [ ] 「内置 / 外部 harness」边界是否会漂移 —— 无任何材料
- [ ] 本页 4 份素材全部 `kind: essay`，**再次暴露 `PRIMARY_KINDS` 判据过窄** —— 是否要推动裁定
- [ ] 「harness」这个隐喻本身是否合适 —— Böckeler 已自认「撑不住」（见其 sources 页）

## 来源

- [[2026-09-19-hashimoto-my-ai-adoption-journey]]
- [[2026-09-19-trivedy-anatomy-of-agent-harness]]
- [[2026-09-19-bockeler-harness-engineering-coding-agent-users]]
- [[2026-09-19-openai-harness-engineering-codex]]
