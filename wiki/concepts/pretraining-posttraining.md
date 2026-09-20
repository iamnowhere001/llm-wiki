---
title: 预训练与后训练：预训练决定能力上限，后训练决定下限
type: concept
slug: pretraining-posttraining
tags: [万维钢, 得到课程, 学习, 机器学习, 后训练, 预训练]
created: 2026-09-19
updated: 2026-09-19
sources: [2026-09-19-pretraining-posttraining]
related: [compression-as-intelligence, deliberate-practice, cybernetic-learning, learning-as-forgetting, transfer-of-learning, tacit-knowledge, human-sponge, cognitive-load-theory, bayesian-prior, prediction-error, goodharts-law, mesa-optimization, self-constraint, entrustability, reference-class, selection-bias, prospect-theory, kelly-criterion, value-of-information, 2026-09-19-objective-function, 2026-09-19-inner-optimizer, 2026-09-18-deliberate-practice-talent, how-we-learn-and-how-to-improve, modern-thinking-tools, wanweigang]
evidence_tier: single
confidence: medium
status: active
---

# 预训练 / 后训练（Pre-training / Post-training）· 并载「grokking」「涌现能力」

> **「预训练决定能力的上限，后训练决定能力的下限。」**（讲稿行 128）
> 最凝练的一句：**「预训练决定你 *偶尔* 能成为谁，后训练决定你 *通常* 是谁」**（行 216）。
> 方法自称（行 48）：**「逆向仿生学」** —— 用 AI 训练的研究成果回头理解人自己的学习。

> [!note] 三层分开记（自写）
> ①**纯 ML 既有术语**：pre-training、SFT、RLHF、RLVR、pass@k / pass@1、alignment tax、Superficial Alignment Hypothesis、
> Chinchilla（Hoffmann et al. 2022）、grokking（Power et al. 2022）、InstructGPT（Ouyang et al. 2022）、LIMA（Zhou et al. 2023）——
> **全部外核属实**，本份**未发现 AI 加工段（0%）**。
> ②**比喻性外推是讲稿做的**：「预训练 = 贯穿一生的经验积累」（行 64）、「思维工具是调用心智基座模型的快捷键」（行 160）、
> 「学习思维工具 = 给自己做后训练」（行 162）—— **这些是类比，不是 ML 结论**。
> 讲稿**主动划了界**（行 50）：「这只是类比，人脑和 AI 的技术细节并不相同」。
> ③**「段誉 vs 乔峰」（行 144–146）、「权重永远是热的」（行 196）是讲稿自造比喻**，可作讲稿主张，不挂既有理论。
> 另：行 140 的「与 Anthropic 工程师私聊」**无公开来源可核**，标（未验证）。

> [!warning] 孤证 —— 本页仅 1 份素材支撑
> 支撑本页的只有 [[2026-09-19-pretraining-posttraining]]，尚未获得第二份独立来源的交叉验证。
> **引用本页结论时应带着这个前提**，或先补一份独立来源把它升到 `crossed`。

## 要点

- **预训练** = 预测下一个词重复几万亿次 →「**预测会逼出理解**」（行 60）；映射到人就是**经验积累**（行 64）。
- **语料必须喂足**：Chinchilla（DeepMind 2022）—— 同样算力下，参数小但语料足的模型胜过大得多却训练不足的模型（行 66）。
- **基座模型**「满腹经纶但不着调」（行 78），需要后训练三步：**SFT**（教格式与品位，行 84）、**RLHF**（把「被人喜欢」做成奖励信号，行 86）、
  **RLVR**（只问对不对，行 92）。
- **RLHF 里就有古德哈特定律与伪对齐**：Anthropic 2023 在多家助手上观察到**谄媚倾向（sycophancy）**（行 88）。
- **对齐税**：为对齐人类偏好，某些硬能力会下降（行 90）。
- **反直觉答案**：后训练**几乎没有添加能力**（行 100）—— pass@1 领先，pass@k（k 几百）基座追平甚至反超（行 110）。
  **「强化学习添加的不是新能力，而是可靠性」**（行 120），代价是**减少探索**（行 112）。
- **表面对齐假说**（行 124）：真本事在预训练，后训练只管表现。

## 定义与背景

**pass@k**（行 104）：同一题试 k 次，有一次对就算过 —— 测**脑子里有没有这条路**。
**pass@1**（行 106）：只给一次机会 —— 测**能不能随时调出这条路**。
「**pass@k 测潜力，pass@1 测发挥**」（行 108）。

**关键实证**：Yue, Chen, Lu et al. 2025《Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?》
（清华大学宋士吉 / 黄高团队，**NeurIPS 2025 Best Paper Runner-Up**，arXiv:2504.13837）——
**年份 / 机构 / 人 / 精确结论全部对上**（行 110）。

两个旁证（行 122）：**13 亿参数 InstructGPT** 经后训练在人类偏好中胜过 **1750 亿参数 GPT-3**；
**LIMA 只用 1000 条精选示范**把 650 亿参数基座调成像样助手 —— 两个数字逐字吻合。

**两个"难以理解"的现象**（行 70 / 72）：
**涌现（emergence）**——规模到某量级，没人教过的能力自己冒出来（通行归属 Wei et al. 2022，素材未署名，弱引注）；
**开悟（grokking）**——Power et al. 2022（OpenAI，ICLR 2022）：先过拟合记忆、验证准确率长期停在随机水平，**之后突然跃到完美泛化**（行 72）。
讲稿的中文对应：**「读书百遍，其义自见」**。

## 机制：映射到人

**① 思维工具 = 后训练。** 「大部分思维工具不是新知识……**它的作用是把你脑子里本来就有的东西打包成一个自动化的短程序**」（行 156）——
**「思维工具是调用你庞大心智基座模型的快捷键」**（行 160），所以「**学习思维工具的本质，是给自己做后训练。
不是让你更聪明，而是让你已有的聪明稳定发挥**」（行 162）。

**② 工具不是经验的替代品。** 「**工具不是经验的替代品，工具是经验的压缩算法**」（行 170）——
没摸过生意的人背会「网络效应 / 边际成本」也用不出；读过公司史、管过账的人一听「软预算约束」就一通百通（行 168）。

**③ 知道 ≠ pass@1。** 「说起来『凯利公式』『选择偏差』『前景理论』头头是道，可一旦涉及自己的利益，
这些工具一个都没被调用。**他不是不会，他是 pass@100 会，pass@1 不会**」（行 172）。
而「**人生的要害处考的全是 pass@1**」（行 174）—— 面试、谈判、危机只给一次机会。

**④ 后训练的三条操作**（行 176–182）：
**在真实情境中演练**（遇动人故事查基础比率、遇考核指标想古德哈特 = 「拥抱与桥接」）、
**一定要有反馈**（「没反馈就没奖励信号，所谓刻苦也不过是在给自己的错误追加权重」）、
**足够熟到不占脑子**（把动作练到 pass@1 ≈ 1）。

**⑤ 实证**：Sellier, Scopelliti & Morewedge 2019（*Psychological Science*）——
290 名研究生做确认偏误训练，几周后遇**以挑战者号发射决策为原型**的商业案例、毫无预告，
**受过训练的学生选劣质方案的概率低 19 个百分点**（行 186–188）。
⚠️ **数字版本登记**：原文 2019 初版报告 **29%**，2020 年勘误后订正为 **19%** —— **素材采用的正是更正后数字**。

## 边界与反例

- **类比不是等同**：讲稿自己划了界（行 50）。人脑与神经网络的技术细节不同，**「逆向仿生学」是启发式，不是证明**。
- **RLVR 可能推高上限**（行 142）：讲稿补注 —— 若训练足够久又能保持探索，**也可能推高能力上限**。
  这与「后训练只决定下限」的主论断**构成张力，素材未裁决**。
- **RL 减少探索**（行 112–114）：可靠性换来的是**推理边界缩小**（pass@256 覆盖下降）—— 这是下限提升的代价。
- **「语料快用完」与「scaling law 未结束」是未决争议**，讲稿只给了私聊与「听说」（行 140），**无公开来源，标未验证**。
- **两处弱引注**：涌现（未给文献）、对齐税（通用行话，首创文献未取到）；行 88 的 `[4]` 因**注释段未导出**而悬空。

## 与其他页面的关系

- 与 [[compression-as-intelligence]] 相接：「预测逼出理解」正是压缩即智能的 ML 版表述。
- 与 [[deliberate-practice]] / [[learning-as-forgetting]] 相接：本页给出它们的** ML 框架版**（语料 / 反馈 / 演练 / 奖励）。
- 与 [[tacit-knowledge]] / [[transfer-of-learning]] 相接：「工具是经验的压缩算法」与这两页同向。
- 与 [[goodharts-law]] / [[mesa-optimization]] 相接：RLHF 的谄媚倾向是「指标被刷 + 伪对齐」的实证现场（行 88）。
- 与 [[entrustability]] 相接：**可托付 = pass@1 稳定**（行 174）。
- 与 [[self-constraint]] / [[mesa-optimization]] 相接：本模块内部互指（「责任链终点必须可被伤害」）。
- 与 [[reference-class]] / [[selection-bias]] / [[prospect-theory]] / [[kelly-criterion]] 相接：这些是本页「思维工具 = 快捷键」的具体例证。
- 与 [[human-sponge]] / [[cognitive-load-theory]] 相接：预训练看输入，与该两页的「输入质量」主张同源。
- 与 [[bayesian-prior]] / [[prediction-error]] 相接：「猜错就校准权重」字面就是预测误差最小化。

## 开放问题

- [ ] 「后训练只决定下限」vs 行 142「RLVR 也可能推高上限」—— 素材内部张力未裁决。
- [ ] 涌现能力（Wei et al. 2022）近年有反方（质疑是度量假象），本库未检索。
- [ ] 29% → 19% 的勘误提示：**本库引用带数字断言时应注明版本**（本页已注明）。
- [ ] 行 140 的私聊内容不可追溯，本页已标（未验证）。

## 来源

- [[2026-09-19-pretraining-posttraining]]（万维钢《现代思维工具课》「模块八 高观点」，本库推定次序 117）
