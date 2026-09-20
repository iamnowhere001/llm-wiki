---
title: TraeCode
type: entity
slug: traecode
tags: [工具, AI, IDE]
created: 2026-09-18
updated: 2026-09-18
sources: [2026-09-18-trae-rules-docs, 2026-09-18-trae-agents-md-vs-rules-forum]
related: [agents-md, 2026-09-18-trae-rules-docs, 2026-09-18-trae-agents-md-vs-rules-forum, llm-wiki-pattern, obsidian]
evidence_tier: crossed
confidence: medium
status: active
---

# TraeCode

> 一个 AI 原生 IDE。对本库而言它重要的不是「能写代码」，而是它**支持把项目规则写成 `AGENTS.md`** —— 这意味着本库的 schema 层可以不被绑死在任何一个工具上。

- **类型**：工具 / 开发环境
- **别名**：TRAE
- **外部链接**：https://www.trae.cn/ ｜ 文档 https://docs.trae.cn/ ｜ 社区 https://forum.trae.cn/

## 是什么

一个把 AI 智能体嵌进编辑器工作流的 IDE。文档中出现了**两种界面模式**：「IDE 模式」与「SOLO 模式」，两者的设置入口都在各自界面右上角的设置图标里。

对本知识库有意义的，是它的**规则体系** —— 也就是「如何让 AI 稳定遵守项目约定」这个问题的产品化答案。

## 规则体系（一手事实）

来源：官方文档 [[2026-09-18-trae-rules-docs]]。

| 维度 | 事实 |
|---|---|
| 规则分类 | **全局规则**（所有项目生效）/ **项目规则**（仅本项目生效） |
| 全局规则位置 | `~/.trae-cn/user_rules`（macOS/Linux）；`%userprofile%/.trae-cn/user_rules`（Windows） |
| 项目规则位置 | 项目下 `.trae/rules/` |
| 生效方式 | 四档：始终生效 / 指定文件生效（`globs`）/ 智能生效（`description`）/ 手动触发生效（`#Rule`） |
| 嵌套上限 | `.trae/rules/` 下可建子文件夹归类，递归读取，**至多 3 层** |
| 子目录规则 | 支持任意子目录下的 `.trae/rules/` 与子目录 `AGENTS.md`，**在该目录文件被提及或读取时才生效** |
| 支持的约定文件 | `AGENTS.md`、`CLAUDE.md`、`CLAUDE.local.md` |
| 默认状态 | **不生效** —— 需在「设置 > 规则 > 导入设置」手动打开「将 AGENTS.md 包含在上下文中」 |
| 提交信息规则 | 规则文件中写 `scene: git_message` 字段，独立于 `alwaysApply`/`description`/`globs` |
| 引用优先级 | 文档明确：**`#Rule` 的优先级最高** |

## 对本库的意义

**它是 [[agents-md]] 这个约定在真实产品里的一个实现方。**

本库把规范层放在 `AGENTS.md`（见 [[three-layer-architecture]]）。这个选择原本有一个隐患：如果每个 AI IDE 都有自己的私有规则格式，那么 schema 层就被绑死在一个工具上，换工具等于重写。TraeCode 的官方文档明确说了相反的话：

> 在 TraeCode 中创建的 AGENTS.md 文件可以在其他支持 AGENTS.md 的 IDE 中复用，反之亦然。

**这句话把 `AGENTS.md` 从「某个产品的配置」变成了「一个跨工具的接口」。** 对本库而言，这是「schema 层可移植」的直接证据 —— 也是新建项目 [[traecode-pkm-article]] 要写进文章的核心论点之一。

另一处值得注意的设计是**子目录规则的按需加载**：根目录放总纲，模块目录放细则，只有涉及该模块时才加载。这与本库「入口层决定什么重要、其余按需」的思路同源（见 [[cybernetic-learning]] 的过滤器）。

## 与相邻工具的位置

| | [[traecode]] | [[obsidian]] |
|---|---|---|
| 定位 | AI 原生 IDE（写代码为主） | 本地 Markdown 编辑器（读知识为主） |
| 规则载体 | `AGENTS.md` + `.trae/rules/` | 无（靠插件） |
| 对本库的角色 | **schema 层的宿主** —— 让 AI 按 `AGENTS.md` 干活 | **读取层** —— 让人浏览 wiki |
| 数据形态 | 打开的项目目录 | 打开的 vault 目录 |

两者不是替代关系：本库的工作流是「LLM agent 在一侧改文件，Obsidian 在另一侧实时看结果」。TraeCode 可以占据前者的位置。

> [!warning] 未验证的事实
> 以下信息**未收录素材**，仅来自检索，标注为未验证：
> - TraeCode 隶属字节跳动（TRAE 产品线），宣传语为「The Real AI Engineer」。
> - 产品线中另有 TraeWork（AI 办公平台）与 TraeCode 并列。
> - 发布年份与版本历史均未核实。
>
> 另有一处**观察而非事实**：全局规则路径为 `~/.trae-cn/`，带 `-cn` 后缀，推测存在面向不同区域的变体（如 `.trae`）。文档只写了 `-cn` 一种，未说明是否存在国际版。

## 待办 / 开放问题

- [ ] `AGENTS.md` 与 `.trae/rules/` 同时存在且冲突时，谁优先？官方文档未说明
- [ ] 子目录 `AGENTS.md` 是否也受「3 层」限制？
- [ ] 本库的 `AGENTS.md` 直接放进 TraeCode 打开，实际表现如何？（需要实测）

## 相关页面

- [[agents-md]]
- [[2026-09-18-trae-rules-docs]]
- [[2026-09-18-trae-agents-md-vs-rules-forum]]
- [[llm-wiki-pattern]]
- [[obsidian]]

## 来源

- [[2026-09-18-trae-rules-docs]]
- [[2026-09-18-trae-agents-md-vs-rules-forum]]
