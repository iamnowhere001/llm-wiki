---
title: Harness engineering: leveraging Codex in an agent-first world（Ryan Lopopolo / OpenAI，2026-02-11）
type: source
slug: 2026-09-19-openai-harness-engineering-codex
tags: [AI, Agent, harness, Codex, OpenAI]
created: 2026-09-19
updated: 2026-09-20
sources: [2026-09-19-openai-harness-engineering-codex]
related: [harness, harness-engineering, agents-md]
confidence: medium
status: active
---

# Harness engineering: leveraging Codex in an agent-first world（Ryan Lopopolo / OpenAI，2026-02-11）

> OpenAI 内部用 5 个月、0 行手写代码、约 100 万行、约 1500 个 PR 构建一个产品的实践报告 ——
> **标题用了 "Harness engineering"，正文却没有定义它。**

- **作者**：Ryan Lopopolo（OpenAI, Member of the Technical Staff）—— **个人署名，不是「Harness 团队」**
- **链接**：https://openai.com/index/harness-engineering/
- **发表**：2026-02-11
- **素材路径**：`raw/2026-09-19-openai-harness-engineering-codex.md`（200 行）

> [!warning] 两条降级理由，不要混
> ① **利益披露**：OpenAI 自述自家产品实践，数字（0 行手写代码 / 约 100 万行 / 约 1500 PR / 3.5 PR 每人每天）
> **无从独立验证** —— 这是「**说的可能不准**」。
> ② **抓取质量**：官方站对 curl 返回 403，存档站与公开代理在本环境被沙箱阻断，
> **本文件经 AI 中介提取**（`capture_quality: medium`，**未做逐字比对**）—— 这是「**记的可能不准**」。
> **两者是不同的问题，降级理由不同，不要合并成一条。**

> [!note] 行号核对
> 本节行号已回原文逐条核对（`wc -l` = 200）。

## 关键要点

1. **⚠️ 术语状态（本页最重要的发现）**：文章标题用了 "Harness engineering"，
   但**正文中 "harness" 几乎不再出现** —— 除标题外**仅有一处**：
   「Evaluation harnesses」（行 153，列在「Agents produce」清单里）。
   **正文从未给出 harness 的显式定义**（没有 "By harness we mean…" 或 "A harness is…" 这类句子）。
   **这与中文圈「OpenAI 提出了 Harness Engineering」的普遍说法有实质差距：文章命名了它，但没有定义它。**
2. **规模数字**（行 43）：5 个月、约 100 万行、约 1500 PR、3 名工程师起（后增至 7）、
   平均 3.5 PR/工程师/天，且**吞吐量随团队扩大而上升**。开发时间约为手写的 1/10。
3. **瓶颈转移**（行 61）："our bottleneck became human QA capacity."
4. **`AGENTS.md` 当目录用**（行 71、80）："give Codex a map, not a 1,000-page instruction manual"。
   他们试过「一个大 `AGENTS.md`」，**失败方式有四条**（行 80 附近）：
   挤占上下文 / 太多指导等于没有指导 / **瞬间腐坏（"It rots instantly"）** / 难以验证。
5. **可验证性是机制化的**：专用 linter 与 CI 任务校验知识库的新鲜度与交叉链接；
   有一个**定期扫描过时文档并自动开修复 PR 的 doc-gardening agent**。
6. **架构约束机械化**：每个业务域分层，依赖方向严格校验（Types → Config → Repo → Service → Runtime → UI），
   由**自定义 linter** 强制；**且 linter 的错误信息里直接注入修复指令**。
7. **垃圾回收**（行 183、185）：此前每周五花 **20% 时间**清理 "AI slop"；后改为把 "golden principles" 编码进仓库，
   由后台 Codex 任务定期扫描偏差、更新质量评分、开定向重构 PR，「多数可在 1 分钟内审完并自动合并」。
8. **卡住时的姿势**（行 55 附近）：几乎从不「try harder」，而是问
   「**缺了什么能力，怎么让它对 agent 既可见又可强制**」。
9. **作者自己划的边界**（文末）：这套行为「depends heavily on the specific structure and tooling of this repository
   and should not be assumed to generalize without similar investment—at least, not yet.」

## 摘要

文章是一份内部实践报告：从空 git 仓库起步，5 个月里由一个 3 人（后 7 人）团队驱动 Codex
建出约 100 万行代码的产品，**人类没有直接贡献任何一行代码**。作者把这称为团队的核心哲学：no manually-written code。

文章的主体不是「怎么做出来的」，而是**「人类的工程工作变成了什么」**。作者的答案：
**设计环境、指定意图、构建反馈回路**。具体包括——
让应用本身对 agent 可读（把 Chrome DevTools Protocol 接进 agent 运行时，让它自己复现 bug）；
把仓库知识变成唯一事实来源（"if it isn't discoverable to the agent, it's illegible"）；
用自定义 linter 与结构测试把架构约束**机械化**；以及用「垃圾回收」式的后台任务对抗熵增。

文章也记录了失败：**「一个大 `AGENTS.md`」这条路走不通**，原因是上下文稀缺、指导过载、瞬间腐坏、难以验证。
他们的解法是把它当目录而不是百科全书。

## 与本库既有页面的关系

- **本项目的第四份一手素材**，也是「业界实践」维度的**最大样本**（也是唯一的团队尺度样本）。
- **校准了一条中文圈广泛流传的说法**：普遍表述是「OpenAI 提出了 Harness Engineering」。
  原文证据显示：**文章标题命名了它，但正文既没有定义它，也几乎没有再使用它**（全文正文仅 1 处技术性用法）。
  **本库的判法是**：把 OpenAI 记作「**一个高可见度的采用者与示范者**」，而不是「提出者」。
  提出者按现有证据是 [[2026-09-19-hashimoto-my-ai-adoption-journey]]（且他本人当时也不确定这是不是通用术语）。
- **与 [[agents-md]] 直接相关，且提供了本库此前没有的一条证据**：
  「大 `AGENTS.md`」的四种失败方式里，**"It rots instantly"（瞬间腐坏）** 与
  「too much guidance becomes *non-guidance*」这两条，**本库的 `AGENTS.md` 从未评估过**。
  本库此前的关切只有「常驻成本」这一个维度。**这条要回填进 [[agents-md]]。**
- **对本项目「个人如何高效实践」维度的关键反证**：这套做法的成本结构是**团队专属**的 ——
  7 名工程师、每周 20% 时间做清理（后来才自动化）、专职维护知识库的 CI 与 linter。
  **个人的瓶颈恰恰是没有那个人力**。这直接支撑 [[harness]] 缺口表第 2 条。
- **与本库的自我对照（潜在矛盾）**：本文说 `AGENTS.md` 约 100 行、当目录用；
  本库 `AGENTS.md` 已压到约 150 行、也在做同样的事 —— **方向一致**。
  但本文同时说「too much guidance becomes non-guidance」，而本库的 [[schema]] 有 561 行。
  **本库的结构与本文建议不冲突（细则在按需读的文件里），但这个对照值得显式写下来。**

## 新出现的实体 / 概念

- 实体：**Ryan Lopopolo**、**OpenAI**、**Codex**、**Aardvark**（文中提到的另一个在库上工作的 agent）
- 概念：**agent legibility（对 agent 可见性）**、**progressive disclosure**、**golden principles**、
  **垃圾回收式技术债偿还**、**"It rots instantly"（规则腐坏）**

## 已知缺失

- 仓库知识库目录结构的代码块被 AI 中介省略（正文中已标注位置）。
- 小节锚点列表未保留。
- **未做逐字比对** —— 若本项目要引用具体数字，**需先补一次真正的一手核对**。

## 待办 / 开放问题

- [ ] **补一次真正的一手核对**：换一条路径拿原始 HTML（或找可访问的官方镜像），把本页的 `capture_quality` 从 medium 升到 high
- [ ] 回填 [[agents-md]]：补上「规则腐坏」与「指导过载」两个本库未评估的失败模式
- [ ] 核对文中「Ralph Wiggum Loop」的所指

## 相关页面

- [[harness]]
- [[harness-engineering]]
- [[agents-md]]
- [[2026-09-19-hashimoto-my-ai-adoption-journey]]
- [[2026-09-19-bockeler-harness-engineering-coding-agent-users]]
- [[2026-09-19-trivedy-anatomy-of-agent-harness]]

## 归属判断

- **性质**：**厂商自述**（利益披露）+ **经 AI 中介提取**（官方站 403）

## 来源

- [[2026-09-19-openai-harness-engineering-codex]]
