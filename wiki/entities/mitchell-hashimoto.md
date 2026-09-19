---
title: Mitchell Hashimoto
type: entity
slug: mitchell-hashimoto
tags: [人物, AI, 工程]
created: 2026-09-19
updated: 2026-09-19
sources: [2026-09-19-hashimoto-my-ai-adoption-journey]
related: [harness-engineering, harness, agents-md]
evidence_tier: single
confidence: high
status: active
---

# Mitchell Hashimoto

> HashiCorp 联合创始人、Vagrant / Terraform / Ghostty 作者 —— **「Harness Engineering」这个词的命名者**。

> [!note] 本页是孤证，但素材是**本人一手自述**
> 全部信息来自他本人的博客 [[2026-09-19-hashimoto-my-ai-adoption-journey]]（`kind: essay`）。
> **这是一手文本，不是转述** —— 本库 `evidence_tier` 只认 `paper`，故记 `single`。

> [!warning] 孤证 —— 本页仅 1 份素材支撑
> 支撑本页的只有 [[2026-09-19-hashimoto-my-ai-adoption-journey]]，尚未获得第二份独立来源的交叉验证。
> **引用本页结论时应带着这个前提**，或先补一份独立来源把它升到 `crossed`。

## 要点

- **身份**：HashiCorp 联合创始人；Vagrant、Terraform、Ghostty 的作者。
- **与本库的关系**：2026-02-05 在博客《My AI Adoption Journey》第 5 步中**首次使用「harness engineering」**。
- **他的核心主张**：每当 agent 犯错，就花时间工程化一个让它**永远不再犯**的方案。
- **他给出的两种形式**：改 `AGENTS.md`（如他给 Ghostty 写的那份）；写程序化的验证工具。
- **他的利益声明**（文末脚注原文）："I don't work for, invest in, or advise any AI companies."
  **本库登记的「无利益关联」** —— 这在 harness 相关的四份素材里是唯一一份。

## 他的六步 AI 采用历程

| 步 | 标题 | 一句话 |
|---|---|---|
| 1 | Drop the Chatbot | 放弃用聊天机器人做正经工作，改用 agent |
| 2 | Reproduce Your Own Work | **强迫自己把手工工作用 agent 重做一遍**，只为形成专长 |
| 3 | End-of-Day Agents | 下班前 30 分钟启动 agent，换取第二天的 warm start |
| 4 | Outsource the Slam Dunks | 把「几乎肯定做对」的任务交给 agent，自己去干别的 |
| 5 | **Engineer the Harness** | **命名现场** —— 犯错就工程化，永不再犯 |
| 6 | Always Have an Agent Running | 目标而非现状；他自述做到 10–20%，且**不打算跑多个** |

## 与本库的关系

- **[[harness-engineering]] 的命名者**，[[harness]] 项目的起点人物。
- **他的 `AGENTS.md` 用法与 [[agents-md]] 构成一处张力**：他把 `AGENTS.md` 当**错误清单**用
  （每加一行消灭一类错误），而本库更关心它的**常驻成本**（每加一行永久多付一次）。
  两种说法都成立，结论可能冲突。见 [[agents-md]]。

## 待办

- [ ] 抓取他给 Ghostty 写的 `AGENTS.md` —— 「第一种形式」唯一的实物证据

## 相关页面

- [[harness-engineering]]
- [[harness]]
- [[agents-md]]
- [[2026-09-19-hashimoto-my-ai-adoption-journey]]

## 来源

- [[2026-09-19-hashimoto-my-ai-adoption-journey]]
