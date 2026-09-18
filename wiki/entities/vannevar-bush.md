---
title: Vannevar Bush 与 Memex
type: entity
slug: vannevar-bush
tags: [人物, 历史, 知识管理]
created: 2026-09-18
updated: 2026-09-18
sources: [2026-09-18-bush-as-we-may-think, 2026-09-18-karpathy-llm-wiki]
related: [pkm-history, bidirectional-links, llm-wiki-pattern, compounding-knowledge]
confidence: high
status: active
---

# Vannevar Bush 与 Memex

> 1945 年提出 Memex 构想：一台私人、机械化的文件与图书馆装置，其中**文档之间的关联路径（associative trails）与文档本身同样有价值**。这是整条个人知识管理谱系的起点文献，也是 [[bidirectional-links]] 最早的思想源头。

- **类型**：人物 + 其提出的概念
- **别名**：Memex
- **外部链接**：https://en.wikipedia.org/wiki/Vannevar_Bush
- **一手材料**：[[2026-09-18-bush-as-we-may-think]]（《As We May Think》全文）

## 是什么

Memex 是 Bush 在 1945 年《As We May Think》中描述的一种假想设备。**原文定义**（本库直引）：

> Consider a future device for individual use, which is a sort of mechanized private file and library. It needs a name, and to coin one at random, "memex" will do. A memex is a device in which an individual stores all his books, records, and communications, and which is mechanized so that it may be consulted with exceeding speed and flexibility. **It is an enlarged intimate supplement to his memory.**

关键在于它允许建立**关联路径** —— 在两个条目之间拉一条永久可回溯的线，且这些路径可以被命名、复制、转交。**原文强调的重点是「连接动作」本身**：

> ...associative indexing, the basic idea of which is a provision whereby any item may be caused at will to select immediately and automatically another. **This is the essential feature of the memex. The process of tying two items together is the important thing.**

## 关键事实

| 时间 | 事实 | 来源 |
|---|---|---|
| 1945-07 | 在《大西洋月刊》发表《As We May Think》，提出 Memex | [[2026-09-18-bush-as-we-may-think]] |
| 1945 | 定义 Memex 为「记忆的放大而私密的补充物」 | [[2026-09-18-bush-as-we-may-think]] |
| 1945 | 提出 associative indexing：任何条目可按意愿立即自动选中另一个 | [[2026-09-18-bush-as-we-may-think]] |
| 1945 | 设想路径可被拍摄并转交给朋友，插入其 memex | [[2026-09-18-bush-as-we-may-think]] |
| 1945 | 预言「带有现成关联路径网的新型百科全书」 | [[2026-09-18-bush-as-we-may-think]] |
| — | Bush 未能解决的核心问题是「谁来做维护」 | [[2026-09-18-karpathy-llm-wiki]] |

## 三个容易被忽略的细节

**1｜连接是对称的。** Bush 描述的是「两个条目被永久连接」，任一方都能抵达另一方。**这是双向链接最早的思想源头** —— 比 [[ted-nelson]] 的 hypertext 早 20 年。见 [[bidirectional-links]]。

**2｜路径本身是可分享的知识产物。** 原文描述用户把一整条路径「拍摄下来，交给朋友插入他自己的 memex，在那里被链接进更一般的路径」。**路径不是私人索引，而是可转交、可拼接的对象。** 这一点比「检索快」重要得多。

**3｜他承认机器胜不过心智的地方，也指出了机器能胜的地方。** 原文说人类无法在速度与灵活性上比拟「心智沿着联想路径行进」的方式，但机器可以在**持久性与清晰度**上决定性地胜出。这是对「为什么需要外部系统」的早期论证。

## 在本知识库中的角色

它提供了一条**历史纵深的参照**。[[compounding-knowledge]] 描述的复利机制，本质上是把 Memex 的「关联路径」自动化了：Bush 设想人类手工拉线，而 LLM 可以自动建立并持续更新这些线。

[[andrej-karpathy]] 对它的判断值得单独记下：Bush 的构想「比万维网后来变成的样子更接近」这个模式 —— 私有的、主动策展的，连接的价值不低于内容本身。**他唯一没解决的是维护者是谁。** LLM 补上了这一环。

**完整的历史位置见 [[pkm-history]]。** 简言之：Bush 定义了问题（连接如何建立、谁来维护），此后八十年是不断尝试回答它的过程。

## 相关概念

- [[pkm-history]]
- [[bidirectional-links]]
- [[llm-wiki-pattern]]
- [[compounding-knowledge]]
- [[commonplace-book]]

## 来源

- [[2026-09-18-bush-as-we-may-think]]
- [[2026-09-18-karpathy-llm-wiki]]

> [!note] 置信度说明
> 本页此前只有单一来源（[[andrej-karpathy]] 的转述），置信度为 `medium` 并挂了待核验警告。
> **现已收录 Bush 原文《As We May Think》全文**，本页所有关于 Memex 的描述均可在原文中核对，
> 因此提升为 `confidence: high`，待核验警告撤销。
> 唯一仍属转引的是「Bush 是互联网奠基推动者之一」的说法（来自 [[2026-09-18-appleton-bidirectional-links]]）。
