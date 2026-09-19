---
title: My AI Adoption Journey（Mitchell Hashimoto，2026-02-05）
type: source
slug: 2026-09-19-hashimoto-my-ai-adoption-journey
tags: [AI, Agent, harness, 一手, 英文]
created: 2026-09-19
updated: 2026-09-19
sources: [2026-09-19-hashimoto-my-ai-adoption-journey]
related: [harness, harness-engineering, agents-md, 2026-09-19-trivedy-anatomy-of-agent-harness]
confidence: high
status: active
---

# My AI Adoption Journey（Mitchell Hashimoto，2026-02-05）

> HashiCorp 联合创始人记录自己从 AI 怀疑论者走到深度依赖的六步历程 —— **第 5 步是「Harness Engineering」这个词的命名现场**。

- **作者**：Mitchell Hashimoto（HashiCorp 联合创始人；Vagrant / Terraform / Ghostty 作者）
- **链接**：https://mitchellh.com/writing/my-ai-adoption-journey
- **发布时间**：2026-02-05
- **素材路径**：`raw/2026-09-19-hashimoto-my-ai-adoption-journey.md`（291 行）
- **性质**：**一手**（作者自述）。文末脚注明确声明 **"I don't work for, invest in, or advise any AI companies"** —— 本库登记的**无利益关联**。

> [!note] 行号坐标系
> 本节所有行号均为**文件绝对行号**（`wc -l` = 291 的坐标系），已回原文逐条核对。

## 关键要点

1. **六步历程**（括号内为该文件绝对行号）：
   Step 1 Drop the Chatbot（57）→ Step 2 Reproduce Your Own Work（92）→ Step 3 End-of-Day Agents → Step 4 Outsource the Slam Dunks（169）→ **Step 5 Engineer the Harness（206）** → Step 6 Always Have an Agent Running。
2. **命名现场，原文（行 214–215）**：
   > "I don't know if there is a broad industry-accepted term for this yet, but I've grown to calling this 'harness engineering.' It is the idea that anytime you find an agent makes a mistake, you take the time to engineer a solution such that the agent never makes that mistake again."
3. **作者自陈不确定这是不是业界通用术语** —— 这是本项目「定义」维度最硬的一条证据（见下节）。
4. **两种形式**（行 223–224）：① **Better implicit prompting（AGENTS.md）**；② **Actual, programmed tools**（截图脚本、过滤测试等）。
5. **Ghostty 的 `AGENTS.md`**（行 223）：作者称**每一行都基于一次 agent 的坏行为**，且「almost completely resolved them all」。
6. **第 2 步的方法论**（作者自称从第一性原理自己发现，非引用他人）：把会话拆成独立可执行任务；模糊请求拆成「规划」与「执行」两次会话；**给 agent 一个能自我验证的途径，它多半会自己改对并防止回归**。
7. **第 4 步一条反直觉的建议**（行 186）：**关掉 agent 的桌面通知** —— 「上下文切换很贵；打断的时机应由人控制，而不是由 agent 控制」。
8. **第 6 步仍只是目标**：作者自述「也许有效保持后台 agent 运行的时间占正常工作日的 10–20%」，且**明确不打算同时跑多个 agent**。

## 摘要

文章按作者自己的六步演进组织，每一步都记录了「先失败、再找到价值」的过程。

**前两步是破与立。** 第一步放弃聊天机器人 —— 理由是它「效率明显低于自己动手」；第二步**强迫自己把每一件手工工作用 agent 重做一遍**，只为形成专长。作者称这一步「excruciating」（极其痛苦），但强调**没耗尽努力之前不能下结论**，而且**自己发现比读到别人的结论更有价值**。

**第三步起是效率。** 把 agent 放在「自己本来无法工作的时间」里跑（下班前 30 分钟启动），换来第二天早上的 warm start。

**第四步是分工。** 把「几乎肯定会做对」的任务全交给 agent，**同时自己去干别的事** —— 并特意声明不是去刷社交媒体，而是进入自己的深度思考模式。作者在这里坦率地处理了一个张力：外包任务会让人**不形成该任务的技能**（他引用了 Anthropic 的 skill formation 论文），但他的取舍是「在委托掉的任务上不形成技能，换在保留的任务上继续形成技能」。

**第五步即命名现场。** 核心主张一句话：**每当 agent 犯错，就花时间设计一个让它永远不再犯的方案**。

**第六步是目标而非现状。** 作者明确拒绝「为了跑而跑」。

## 与现有知识库的关系

- **本项目（[[harness]]）的第一份一手素材**，也是「命名现场」的唯一直接证据。
- **校准了中文二手材料的普遍说法**：中文材料普遍把 Harness Engineering 描述成一个 2026 年 2 月「突然火起来」的业界术语。
  原文显示：**命名者本人当时并不知道它会不会成为通用术语**（行 214）。这**不构成对中文材料的证伪** ——
  它说明的是：**这个术语的权威性来自后续引用者的采纳，不来自任何标准组织或原始定义**。
- **与 [[agents-md]] 存在一处真实张力**：本页关于「常驻成本」的判断是「`AGENTS.md` 写长了，每次任务都多付一次」；
  Hashimoto 的用法方向一致（都把 `AGENTS.md` 当**错误清单**而非规范文档），**但成本模型相反** ——
  他追求「每加一行就永久消灭一类错误」，本库更关心「每加一行就永久多付一次成本」。
  **两种说法都成立，但结论可能冲突：前者支持「尽可能多写」，后者支持「尽可能少写」。本库显式标注这是一处未决。**
- 与 [[cybernetic-learning]] 的关系：第 5 步的动作（发现错误 → 工程化解决方案 → 永不再犯）**看起来是**「目标 → 误差信号 → 过滤器」的一个实例，
  但本库要检验这个对应是否真的成立，而不是顺手类比（见 [[harness]] 的「知识」一节）。

## 新出现的实体 / 概念

- 实体：**Mitchell Hashimoto**、**Ghostty**（他开发的终端模拟器；其 `AGENTS.md` 是 harness 第一种形式的实例）
- 概念：**harness engineering**（见 [[harness-engineering]]）

## 已知缺失

- 正文的视觉硬换行未完全重组（原文按约 70 字符换行），**跨行检索可能漏**（与 [[2026-09-19-art-of-impossible-book-en]] 同类问题）。
- 页面导航与「Table of Contents」列表在提取时被保留，未与正文区分。
- **作者引用的 Ghostty `AGENTS.md` 原文未收录** —— 它是「每一行对应一次错误」这一说法的凭据。

## 待办

- [ ] 抓取 Ghostty 的 `AGENTS.md`（GitHub 上，链接在原文行 223）—— **这是「第一种形式」唯一的实物证据**
- [ ] 核对第 2 步的三条方法论与 [[traecode-pkm-article]] 缺口表里「从零跑通」的需求是否有可复用之处

## 相关页面

- [[harness]]
- [[harness-engineering]]
- [[agents-md]]
- [[2026-09-19-trivedy-anatomy-of-agent-harness]]
- [[2026-09-19-bockeler-harness-engineering-coding-agent-users]]
- [[2026-09-19-openai-harness-engineering-codex]]

## 来源

- [[2026-09-19-hashimoto-my-ai-adoption-journey]]
