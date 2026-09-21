---
title: AGENTS.md（跨工具的智能体约定文件）
type: concept
slug: agents-md
tags: [工具, 模式, 约定, 规范]
created: 2026-09-18
updated: 2026-09-19
sources: [2026-09-18-trae-rules-docs, 2026-09-18-trae-agents-md-vs-rules-forum, 2026-09-19-openai-harness-engineering-codex]
related: [three-layer-architecture, llm-wiki-pattern, traecode, plain-text-and-git, conventions]
evidence_tier: crossed
confidence: medium
status: active
---

# AGENTS.md（跨工具的智能体约定文件）

> 放在项目根目录、用 Markdown 写的一份**给 AI 智能体的行为约定**。它的关键性质不是「能被 AI 读到」，而是**换一个 IDE 还能用** —— 这让它成为一个接口，而不是某家的配置格式。

## 关键要点

- 位置固定：项目根目录，纯 Markdown，随代码一起进 git。
- 作用域：项目级 —— 只在该项目中生效。
- 跨工具：[[traecode]] 官方文档明确「在 TraeCode 中创建的 AGENTS.md 可以在其他支持 AGENTS.md 的 IDE 中复用，反之亦然」。
- **它是常驻成本**：整份内容会在每次会话/任务开始时进入上下文。写在里面的每一行，都在每一次任务里被付费。
- 因此它的正确用法是**总纲，不是细则** —— 细则应下沉到按需加载的位置（子目录规则、独立文件、或知识库页面）。
- 在本库中，它**就是三层架构的第三层（schema 层）的物理形态**。

## 正文

### 它解决的是「约定放在哪」

AI 编程工具普遍需要一个「告诉 AI 这个项目的规矩」的地方。早期做法是每家的私有配置：`.cursorrules`、自定义指令框、项目内散落的说明文件。问题在于**这些位置互不相通** —— 换一个工具，同一套约定要重写一遍。

`AGENTS.md` 把这件事收敛到一个**与工具无关的路径**：项目根目录的一个 Markdown 文件。任何支持它的工具都读同一个文件。

判断它是不是「标准」，不看有没有人发起，而看**实现方是否承认互操作性**。[[2026-09-18-trae-rules-docs]] 里那句话的分量就在于此：它不是「我们也支持这个文件名」，而是「**互相可以复用**」。后者才是接口，前者只是兼容。

### 与私有规则系统的分工

以 [[traecode]] 为例，它同时提供两套机制（见 [[2026-09-18-trae-rules-docs]]）：

| | `AGENTS.md` | `.trae/rules/` |
|---|---|---|
| 位置 | 项目根目录（或子目录） | `.trae/rules/`（可嵌套，至多 3 层） |
| 粒度 | 宏观总纲 | 细分条款 |
| 加载 | 随会话/任务进入上下文 | 四档生效方式：始终 / 指定文件 / 智能 / 手动 `#Rule` |
| 跨工具 | **可复用** | 产品私有 |
| 适合写 | 项目是什么、AI 的角色、不可违反的大原则 | 代码规范、架构约束、安全细则 |

**这个分工有一个直接推论**：`AGENTS.md` 承担的是**每次都要付的固定成本**，`.trae/rules/` 承担的是**按需唤起**。所以判断一段内容该放哪，可以问一句：「AI 在写一个完全不相关的模块时，需不需要知道这条？」需要 → `AGENTS.md`；不需要 → 规则文件或子目录。

社区对这个分工的概括与官方一致（见 [[2026-09-18-trae-agents-md-vs-rules-forum]]）：前者「偏宏观总纲」，后者是「拆分落地的细分强制约束」。

### 常驻成本：一个容易被忽略的约束

因为 `AGENTS.md` 常驻，它有一个**与篇幅直接相关的代价**。写长了，每次任务都多付一次；写短了，约定不全。这不是美学问题，是工程问题。

推论是：**`AGENTS.md` 应该薄，厚的内容应该外置。** 可用的外置位置有三类：

1. **产品私有规则系统** —— 如 `.trae/rules/`，可按文件匹配或智能判断触发。
2. **子目录约定文件** —— 只在该目录的文件被提及/读取时加载。
3. **知识库本体** —— 内容留在 wiki 页面里，`AGENTS.md` 只写「去哪里找」和「必须怎么做」。

> [!note] 本库自身正踩在这条线上
> 本仓库的 `AGENTS.md` 目前约 18 KB，是全库最长的单文件之一。如果「常驻」这一性质成立，
> 那么它每次任务都在付出可观的开销 —— 而其中相当一部分（页面规范细则、工作流细节）
> **只在特定动作时才需要**。这是一个真实的设计缺口，已记入 [[traecode-pkm-article]] 的缺口表。
> 可能的解法：根 `AGENTS.md` 压到「一句话 + 铁律 + 指路」，把页面规范与工作流细则拆成
> 按需读取的文件，由 `AGENTS.md` 指向它们。
>
> **2026-09-19 已执行。** `AGENTS.md` 从 629 行压到约 150 行：规则移入 [[schema]]，
> 人类裁定史与墓碑独立为 [[decisions]]，内联的素材案例数据回到对应 `sources/` 页。
> **内容零删除，只是搬家** —— 完整做法与理由见 [[decisions]]。

### 两条本库此前未评估的失败模式（2026-09-19 新增）

[[2026-09-19-openai-harness-engineering-codex]] 记录了他们尝试「一个大 `AGENTS.md`」的四种失败方式。
其中**两条本库此前从未评估过** —— 本库对 `AGENTS.md` 的关切此前只有「常驻成本」这一个维度：

| 失败模式 | 原文 | 本库此前是否评估 |
|---|---|---|
| **指导过载** | "Too much guidance becomes *non-guidance*. When everything is 'important,' nothing is." | **否** |
| **规则腐坏** | "It rots instantly. A monolithic manual turns into a graveyard of stale rules. Agents can't tell what's still true, humans stop maintaining it, and the file quietly becomes an attractive nuisance." | **否** |

**这两条对本库的直接含义：**

- **「指导过载」**：[[schema]] 有 561 行，但它**按需读**；`AGENTS.md` 本身约 150 行。
  **「按需读」是否足以规避指导过载，本库从未验证过。**
- **「规则腐坏」更尖锐**：本库的 `AGENTS.md` / [[schema]] / [[decisions]] 里有大量规则是**特定时点的产物**
  （例：HFQ 的废止、`PRIMARY_KINDS` 的争议）。**没有任何机制会告诉维护者哪一条已经过时。**
  本库的 [[wiki-lint]] 检查的是**结构与链接**，**不检查规则是否仍然成立**。

> [!note] 与 [[harness-engineering]] 的关系
> 这两条是 harness 领域的**通用失败模式**，不只是 OpenAI 一家的经验。
> 「规则腐坏」尤其重要 —— 它可能是 harness 最真实的失败模式（已记入 [[harness]] 的开放问题）。

### 加载时机：一个尚未澄清的问题

官方文档说明了**如何开启**（设置 > 规则 > 导入设置 > 「将 AGENTS.md 包含在上下文中」），但**没有说明何时加载**。这一空白只能靠社区实测填补，而社区说法并不统一（见 [[2026-09-18-trae-agents-md-vs-rules-forum]]）：

- 一种说法：会话/任务启动时加载一次，**中途修改不会在当前会话生效，需开新任务**。
- 另一种说法：取决于提示词缓存命中，换模型时缓存失效。

官方文档「最佳实践」中的一条间接支持前一种：「新建或修改规则后，建议开启全新的对话再使用，以避免历史上下文与新规则产生冲突。」

**这条不确定性对使用者的实际含义**：修改 `AGENTS.md` 之后，应当**重开会话再验证效果**，否则可能误判为「约定没起作用」。这条已写进本库的运维约定（见 [[ingest-query-lint]]）。

### 在本库中的位置

本库的 [[three-layer-architecture]] 把架构分为素材层 / 知识库层 / 规范层，规范层的落点就是 `AGENTS.md` + `wiki/conventions.md`。

`AGENTS.md` 在这里回答的是**「这个知识库如何被维护」**，而不是「这个知识库讲了什么」。它是一个**元层**文件：不描述知识，描述生产知识的规则。

这也解释了为什么它与 [[plain-text-and-git]] 是同一套取向：约定必须是纯文本、进版本控制、能被任何工具读写。如果约定存在某个产品的数据库里，它就既不可审计、也不可移植 —— 而「不可移植」直接摧毁了 [[llm-wiki-pattern]] 的长期可行性，因为那意味着知识库的维护方式被锁在一个会过期的工具上。

## 与其他页面的关系

- 是 [[three-layer-architecture]] 第三层的具体形态。
- 是 [[traecode]] 的规则体系中最具「可移植性」的部分。
- 与 [[plain-text-and-git]] 同源：约定也必须是纯文本、可 diff、可迁移。
- 区别于 [[second-brain-skill]]：后者把维护手册封装成 Skill，**放进了工具**；`AGENTS.md` 把它**放进了仓库**。前者省事，后者可审计、可移植。这个对比值得展开。
- 是 [[llm-wiki-pattern]] 中「schema 层由人类与 LLM 共同演进」的载体。
- 是 [[harness-engineering]] 中「第一种形式」的最常见载体，也是 [[harness]] 项目的枢纽页。
  即**把 agent 犯过的错固化成一条常驻规则** —— 这条用法在 [[2026-09-19-hashimoto-my-ai-adoption-journey]] 里有明确实例（Ghostty 的 `AGENTS.md`）。
  **2026-09-19 该对应关系已获一手核实**：素材已落盘，Hashimoto 原文 称 Ghostty 的 `AGENTS.md`
  **每一行都基于一次 agent 的坏行为**，且「almost completely resolved them all」。
  **本条此前写的「一手素材未落盘，只建立链接不立断言」已过期，现更正。**
  **展开见 [[harness-explained]] 的「最小 harness 清单」** —— 那张表把本页定位为构件 1（薄的常驻规则文件），
  并指出它超过一定体量就会触发 **指导过载**（见下节）。

## 待办 / 开放问题

- [ ] `AGENTS.md` 的加载时机与缓存行为需要一手验证（官方未说明）
- [ ] 与 `.trae/rules/` 冲突时的优先级未知
- [ ] 是否存在跨工具的事实标准组织在维护这个文件名？（未验证）
- [x] **本库 `AGENTS.md` 的瘦身方案** —— 2026-09-19 执行（见下）

## 来源

- [[2026-09-18-trae-rules-docs]]
- [[2026-09-18-trae-agents-md-vs-rules-forum]]
