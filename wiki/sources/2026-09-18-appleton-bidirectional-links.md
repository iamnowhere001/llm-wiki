---
title: A Short History of Bi-Directional Links — Maggie Appleton
type: source
slug: 2026-09-18-appleton-bidirectional-links
tags: [历史, 双向链接, 万维网]
created: 2026-09-18
updated: 2026-09-18
sources: [2026-09-18-appleton-bidirectional-links]
related: [bidirectional-links, pkm-history, ted-nelson, tim-berners-lee]
confidence: medium
status: active
---

# A Short History of Bi-Directional Links — Maggie Appleton

> 一篇梳理「双向链接为什么没有成为万维网的基础」的权威通俗文献。核心结论：**双向链接在技术上一直可行，被放弃的原因是治理 —— 如果任何人都能让链接出现在你的页面上，垃圾与恶意引用无法控制。** 单向链接是让万维网得以普及的妥协。

- **作者**：Maggie Appleton（设计人类学背景，Digital Garden 概念的主要推广者之一）
- **链接**：https://maggieappleton.com/bidirectionals
- **发表**：约 2020 年（页面自述 "Planted over 6 years ago"）
- **素材路径**：`raw/2026-09-18-appleton-bidirectional-links.md`

## 关键要点

1. **双向链接不新。** 思想源头是 1945 年 [[vannevar-bush]] 的 Memex ——「关联索引」的构想。
2. **[[ted-nelson]] 在 1965 年创造 hypertext 一词**，直接受 Bush 启发，并计划在 Project Xanadu 中实现「每个句子、区块、页面都属于一张巨大的双向链接网络」。
3. **Xanadu 没做成，我们得到了万维网。** 万维网在基础设施层面不支持双向链接。
4. **原因不是技术，是治理。** 若每个指向你的站点都可见、而你无法控制谁可以链接你，就会出现「恶意引用的后果」。过滤、审核、权限设计「变得相当复杂」。
5. **决策是对的。** 考虑到创造者要的是「普遍采用」，用更简单的单向链接实现万维网是正确的选择。
6. **个人站点绕开了这个问题。** 单一作者站点的垃圾与恶意风险为零，因此双向链接在「数字花园」运动中复兴。

## 摘要

文章从当下的现象切入：[[roam-research]] 的兴起让双向链接「又火了一阵」。而我们已经太习惯万维网的单向链接 ——「它们是我们沿线性顺序跟随的单向指针」。

作者给出了一个很准确的描述：**双向链接具有「社会意识」** —— 它知道有哪些页面指向它，并能把这些页面展示给人看。于是站点之间形成双向对话，而单向链接「试图建立关系，却被另一端完全无视」。

**历史部分**是本文最有价值的内容：

- **1945 / Bush**：Memex 想要一个能「按意愿立即、自动地选中另一个条目……从而把众多条目连接成一条路径」的系统。Appleton 判断这篇文章是「直接导向互联网与万维网这两套彼此独立的技术」的基础文献。她特别指出：Bush 的描述之所以惊人，是因为**数字计算机当时才出现 5 年**，大多还是军用的大型计算器，实现一个高度交互的个人知识库「几乎不是一个选项」。于是这个想法**冬眠**到六七十年代个人计算兴起。
- **1965 / Nelson**：一个「不太像电影导演和社会学家的人」误入一系列计算机讲座，开始想象图形界面如何重塑我们书写与连接想法的方式。他直接受 Bush 启发，创造 hypertext 一词描述「一张蔓延的、互相链接的信息网络」。他计划用 **Project Xanadu** 实现：不只是回溯来源，还能看到**谁引用、重组、扩展了**那个原始内容。Appleton 特别提到 Xanadu 应被理解为一种 **pattern language（模式语言）** 而非失败的软件项目 —— 它还包括 transclusion（内容嵌入）与 transcopyright（一套关于权限与版权的设想）。
- **1989→ / 万维网**：Xanadu 没实现，我们得到的是「没那么花哨，但真实得多、可用得多」的万维网。作者引用 [[tim-berners-lee]] 1999 年的一份笔记，说明他**确实权衡过双向链接的利弊**，但显然的设计问题是：双向连接自由流动会带来恶意引用的后果。过滤、审核、权限的设计细节变得复杂，最终「用更简单的单向链接实现万维网是正确的事，因为创造者要的是普遍采用」。
- **当下 / 数字花园**：在**单一作者站点**范围内加双向链接绕开了治理问题。作者点名 **Andy Matuschak 的笔记**是这股风潮的起点，其关键是每篇笔记底部的 "Links to this Note" 区块。此外还有 TiddlyWiki（非开发者方案）与 **WebMentions**（IndieWeb 社区推动，W3C 于 2017 年给出规范推荐状态）—— 一种「可选加入」的双向链接系统。

## 与现有知识库的关系

**这是本库 [[pkm-history]] 这条线的主干文献之一。** 它把 1945（Bush）→ 1965（Nelson）→ 1989/1999（万维网妥协）→ 2020（数字花园复兴）串成一条有因果关系的链条，而不是一串孤立的年份。

**对 [[llm-wiki-pattern]] 的意义**：本文给出了「为什么中心化的双向链接在公开网络上不可行」的**治理层面**解释。这反过来解释了为什么 [[llm-wiki-pattern]] 强调知识库应当是**私有的**（"private, actively curated"）—— 在单一所有者的封闭域内，治理问题不存在，双向链接可以自由使用。[[vannevar-bush]] 的判断「比万维网更接近」由此获得了机制上的解释。

**它引入了两个新实体**：[[ted-nelson]] 与 [[roam-research]]；以及一份一手材料 [[2026-09-18-berners-lee-link-topology]]。

## 待办

- [ ] 原文的多张插图（Xanadu 设计稿、Andy Matuschak 笔记截图）未下载
- [ ] Appleton 称 Xanadu 为 pattern language 并提到 transclusion / transcopyright，本库尚无独立页
- [ ] 「Bush 是互联网奠基推动者」的说法引用了 Walter Isaacson《The Innovators》，属二次转引
- [ ] 本文是通俗文献而非学术史，年份需与其他来源交叉验证（见 [[pkm-history]] 的年份矛盾一节）

## 相关页面

- [[bidirectional-links]]
- [[pkm-history]]
- [[ted-nelson]]
- [[tim-berners-lee]]
- [[roam-research]]

## 来源

- [[2026-09-18-appleton-bidirectional-links]]
