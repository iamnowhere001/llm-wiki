---
title: 个人知识管理系统的历史与演进（1945–2026）
type: analysis
slug: pkm-history
tags: [历史, 知识管理, 综述]
created: 2026-09-18
updated: 2026-09-18
sources: [2026-09-18-bush-as-we-may-think, 2026-09-18-appleton-bidirectional-links, 2026-09-18-berners-lee-link-topology, 2026-09-18-frand-hixon-pkm, 2026-09-18-luhmann-zettelkasten]
related: [llm-wiki-pattern, bidirectional-links, zettelkasten, commonplace-book, vannevar-bush, three-layer-architecture]
confidence: medium
status: active
---

# 个人知识管理系统的历史与演进（1945–2026）

> 个人知识管理不是互联网时代的产物。它有一条 80 年的清晰谱系：**1945 年 Bush 提出「关联路径」→ 1965 年 Nelson 命名 hypertext → 1989/1999 年万维网为普及而放弃双向链接 → 1998 年「PKM」一词被命名 → 1950s–1990s 卢曼用纸笔证明了个人系统可以支撑一生的工作 → 2017–2020 双向链接在私有域内复兴 → 2026 年 LLM 接手维护。**
>
> 贯穿始终的只有两个问题：**知识之间的连接如何建立**，以及**谁来维护这些连接**。

## 要点

1. **这条线的起点是 1945 年**，而不是 2000 年代的「第二大脑」热潮。[[vannevar-bush]] 的 Memex 已经包含了此后所有方案的核心要素。
2. **每一次进步都发生在「记录成本下降」之后**：印刷 → 复印 → 个人电脑 → 万维网 → 双向链接工具 → LLM。瓶颈从「记录」转移到「检索」，再转移到**「连接与维护」**。
3. **万维网放弃双向链接是一次治理决策，不是技术失误。** [[tim-berners-lee]] 明确权衡过，并在笔记里给出了折中方案。
4. **「PKM」这个术语到 1998 年才被命名**（[[2026-09-18-frand-hixon-pkm]]），比 Memex 晚了 53 年 —— **实践远早于命名**。
5. **[[niklas-luhmann]] 是手工时代的极限案例**：40 余年、90,000 张卡片、70 本书，证明了个人系统可以规模化 —— 代价是全部维护由一个人承担。
6. **双向链接在 2017–2020 年复兴，但只在私有域内。** 公开网络的治理问题至今无解（见 [[bidirectional-links]]）。
7. **LLM 补上了这条线上一直缺失的一环**：连接的建立与维护。这是 [[llm-wiki-pattern]] 的历史位置。

## 一张时间表

| 时间 | 事件 | 类型 | 来源 |
|---|---|---|---|
| 古典–19C | 共同笔记簿（commonplace book）传统 | 实践 | [[commonplace-book]] |
| 1945 | [[vannevar-bush]] 提出 Memex 与「关联路径」 | 构想 | [[2026-09-18-bush-as-we-may-think]] |
| 1950s–1998 | [[niklas-luhmann]] 的卡片盒（90,000+ 张卡片） | 实践 | [[2026-09-18-luhmann-zettelkasten]] |
| 1965 | [[ted-nelson]] 创造 **hypertext** 一词；发起 Xanadu | 术语 + 构想 | [[2026-09-18-appleton-bidirectional-links]] |
| 1989 | 万维网提案 | 实现 | — |
| 1998-10-15 | Frand & Hixon 命名 **Personal Knowledge Management** | 术语 | [[2026-09-18-frand-hixon-pkm]] |
| c.1999 | [[tim-berners-lee]] 权衡链接拓扑，提出折中方案 | 设计决策 | [[2026-09-18-berners-lee-link-topology]] |
| 2017 | Sönke Ahrens《How to Take Smart Notes》系统化卡片盒方法 | 普及 | [[2026-09-18-luhmann-zettelkasten]] |
| 2017–2019 | [[roam-research]] 让双向链接重回主流 | 工具 | [[2026-09-18-appleton-bidirectional-links]] |
| 2020-03 | [[obsidian]] 首个公开版本 | 工具 | （未验证，检索结果） |
| 2026 | [[llm-wiki-pattern]]：LLM 增量维护知识库 | 模式 | [[2026-09-18-karpathy-llm-wiki]] |

## 阶段一｜1945：问题被正确地提出

**这是整条线的起点，也是问题定义得最清楚的一次。**

[[vannevar-bush]] 在《As We May Think》中的判断是：**瓶颈不是记录，而是「在记录中穿行」。** 原文说出版量已远超人类使用记录的能力，检索手段却「还停留在方帆船时代」。

他给出的方案是 Memex，其定义（本库直引原文）：

> A memex is a device in which an individual stores all his books, records, and communications, and which is mechanized so that it may be consulted with exceeding speed and flexibility. It is an enlarged intimate supplement to his memory.

但**核心机制不是速度，是 associative indexing**：

> ...associative indexing, the basic idea of which is a provision whereby any item may be caused at will to select immediately and automatically another. **This is the essential feature of the memex. The process of tying two items together is the important thing.**

三点值得记住：

1. **它是对称的** —— 两个条目被「永久连接」，任一方都能抵达另一方。这是 [[bidirectional-links]] 最早的思想源头。
2. **路径可以被转交** —— Bush 描述了把一整条路径「拍摄下来，交给朋友插入他自己的 memex」。**路径本身是一种可分享的知识产物**，不只是私人索引。
3. **他预言了知识形态的改变** —— 「带有现成关联路径网、可直接放进 memex 再扩增的新型百科全书」。

**Bush 没有回答的问题**：谁来做维护？他设想用户手工拉线，并假设「路径不会消退」。**这个假设是本条线上最大的一个未解难题，直到 2026 年才有人接手。**

**一个被忽略的时代背景**：Bush 写作时数字计算机才出现 5 年，且多是军用大型计算器。[[2026-09-18-appleton-bidirectional-links]] 因此判断，实现「一个高度交互的个人知识库」在当时「几乎不是一个选项」—— 于是这个想法**冬眠**到六七十年代个人计算兴起。

## 阶段二｜1950s–1998：卢曼用纸笔跑通了

**如果 Bush 是提出者，[[niklas-luhmann]] 是证明者。** 在 Memex 之后的三十年里，他是最接近「用一套系统持续几十年积累知识」的人 —— 只是用的是纸和笔。

| 维度 | 数据 |
|---|---|
| 时间跨度 | 1950 年代 – 1998 年去世 |
| 卡片总量 | 超过 90,000 张 |
| 产出 | 70 本书 + 400 余篇论文 |
| 系统结构 | 两套卡片盒（书目盒 + 主盒） |

**他与 Bush 的关系值得单独记下**：Bush 设想的是**机器**，Luhmann 做的是**手工版**。两人面对的是同一个问题 —— 如何让知识之间的连接不消退。Bush 没回答「谁维护」，**Luhmann 的答案是「自己每天维护，持续四十年」**。

这既是答案，也是这个方案无法被普通人复制的原因。方法论细节见 [[zettelkasten]]。

**一个关键的表述**：Luhmann 说「我从不从零开始写作。我只是取出卡片盒中已经准备好的思考」。这句话与 [[llm-wiki-pattern]] 的「编译一次、持续保鲜」是同一个主张的两种说法 —— 只是他手工编译了四十年。

## 阶段三｜1965：hypertext 被命名

[[ted-nelson]] 直接受 Bush 启发，在 1965 年创造 **hypertext** 一词，描述「一张蔓延的、互相链接的信息网络」。

他的野心比万维网大得多。他发起 **Project Xanadu**，目标不只是「回溯来源」（现代网页链接也能做），而是**「看到谁引用、重组、扩展了那个原始内容」**。[[2026-09-18-appleton-bidirectional-links]] 给了一个重要的判断框架：

> Xanadu 应当被理解为一种 **pattern language（模式语言）**，而不是一个失败的软件项目。

它包含的设想远超双向链接：**transclusion**（引用即嵌入，原件更新则引用处同步）与 **transcopyright**（让嵌入在尊重版权前提下成立的权限设想）。**今天笔记工具里的「块引用」就是 transclusion 的简化版** —— 一个 1965 年的设计，在 2020 年以另一种形式复活。

**Xanadu 没有做成。** 本库记录这个失败时的态度是：它不是「一个人异想天开」，而是**一组被反复重新发现的设计模式**，其难度在于治理而非技术。

## 阶段四｜1989–1999：万维网为普及放弃双向

**这是整条线上最重要的一次分叉，也是最容易被误读的一次。**

结果：万维网采用了**单向链接**。今天我们在网上建立的每一条链接，目标页都不知道。

**容易被误读的地方**：这看起来像是疏漏或权宜之计。但 [[2026-09-18-berners-lee-link-topology]] 证明它是**被论证过的工程取舍**。[[tim-berners-lee]] 在笔记里并列了正反两面：

- **双向更优的地方**：反向关系是「**免费增加的信息**」；建链成本更低；文档被销毁或移动时可预知**悬空链接**。
- **双向的代价**：「强制双向的一个缺点是**它会约束超文本的作者**」；以及一个当时无解的问题 —— 如何对受保护的数据库建立双向链接。
- **他提出的折中**：「数据模型里链接是单向的，但当任何链接被建立时，创建一个反向链接，只要这不会侵犯保护机制。」

**为什么折中没被采用** —— 这是这份笔记没有明说、而 [[2026-09-18-appleton-bidirectional-links]] 补上的部分：若每个指向你的站点都自动出现在你的页面上，而你又无法控制谁能链接你，**恶意引用无法避免**；过滤、审核、权限的设计随之「变得相当复杂」。考虑到创造者的目标是**普遍采用**，用更简单的单向链接是正确的选择。

**这一段的真正结论**：双向链接不是「没被想到」，而是**被治理成本否决了**。完整分析见 [[bidirectional-links]]。

## 阶段五｜1998：「PKM」被命名

**注意这个时间点**：万维网普及（1993 起）之后仅五年。**实践远早于命名** —— Bush 的构想在 1945 年就有了，但「个人知识管理」这个名字要到 1998 年才出现。

[[2026-09-18-frand-hixon-pkm]] 是这个词的首发文献：1998 年 10 月 15 日 EDUCOM'98 会议上的演讲幻灯片，作者来自 UCLA（商学院 + 图书馆）。

它的定义很克制：

> A conceptual framework to organize and integrate information that we, as individuals, **feel is important** so that it becomes part of our personal knowledge base.

「个人认为重要」是判断标准 —— 这成为 PKM 与企业知识管理分野的关键。

**它给出的最有价值的东西是一张对照表**，论证「为什么个人必须自己做策展」：

| | 传统信息资源 | 万维网 |
|---|---|---|
| 生产成本 | 高 | 低 |
| 编辑审核 | 出版前 | 基本没有 |
| 内容评价 | 由专业人士 | **由用户** |
| 生产者数量 | 受控 | 无限 |

**当生产与分发的门槛消失，评价与筛选的责任就必然转移到个人身上。** 这个论证结构在 28 年后被 [[dan-koe]] 以另一种说法重现：「当 AI 什么都能生成时，策展比任何时候都重要。」

**一次由一手文献纠正的引用误差**：本库在检索阶段把这份文献记为 1999 年（多个二手来源如此引用）。**原文封面与存档的推荐引用均标注 1998**（Educom 98）。本库以原文为准。

## 阶段六｜2017–2020：双向链接在私有域内复兴

**这个复兴有两个同时发生的推力：**

- **2017 年，Sönke Ahrens 出版《How to Take Smart Notes》**，把 [[niklas-luhmann]] 的方法系统化（并加上了卢曼本人从未使用的「闪念/文献/永久笔记」三分法）。
- **2017–2019 年，[[roam-research]] 让双向链接重回主流。** [[2026-09-18-appleton-bidirectional-links]] 的观察很直接：双向链接「不新」，是 Roam 的兴起让它「又火了一阵」。

**为什么这次能成，而 1999 年不能？** 因为**作用域变了**：

- 1999 年的问题是**全网**的双向链接 —— 涉及任意人之间的链接可见性，治理无解。
- 2017 年的场景是**单作者私有域** —— 一个所有者，垃圾与恶意风险为零，治理问题消失。

[[2026-09-18-appleton-bidirectional-links]] 的判断很准确：「在**单一作者网站**的范围内加双向链接绕开了这个问题。」

**2020 年 3 月，[[obsidian]] 发布首个公开版本**（未验证，检索结果）。它用「本地 Markdown 文件 + 免费」接住了同一批需求，并因为纯文本而成为 [[llm-wiki-pattern]] 推荐的「wiki 的 IDE」（见 [[plain-text-and-git]]）。

**同一时期还有一条支线**：IndieWeb 社区推动的 **WebMentions**（W3C 于 2017 年给出规范推荐状态）—— 一种「可选加入」的双向链接，试图在公开网络上部分实现它，代价是需要站点主动接入。

## 阶段七｜2026：LLM 补上缺失的一环

**回到 Bush 那个未被回答的问题：谁来做维护？**

| 时代 | 维护者 | 后果 |
|---|---|---|
| Bush 1945 | 用户手工拉线 | 从未实现 |
| Luhmann 1950s–1998 | 一个人，每天，四十年 | 成功，但不可复制 |
| 万维网 1989– | 每个作者各自维护 | 链接腐烂、无反向关系 |
| 双向链接工具 2017– | 用户手工建链接 | 门槛降低，但仍是手工 |
| **LLM Wiki 2026** | **LLM** | **首次把维护外包给非人** |

[[llm-wiki-pattern]] 的历史位置由此清晰：**它不是「又一个新的笔记方法」，而是这条线上第一次让「连接的建立与维护」不再依赖人的持续投入。**

三个与前史直接接榫的点：

1. **「编译一次、持续保鲜」= Luhmann 的「取出已准备好的思考」** —— 同一个主张，只是编译者换成了 LLM。
2. **自动维护反向链接 = Berners-Lee 1999 年的折中方案** —— 他提出的「数据模型单向 + 后台进程收集反向链接」，在 LLM 时代变得可行。
3. **私有知识库绕开治理问题 = 数字花园的策略** —— [[vannevar-bush]] 判断 Memex「比万维网更接近」本模式的真正原因在此。

**一个诚实的保留**：把 LLM 放进这条谱系，是**本库自己的综合判断**，不是 [[andrej-karpathy]] 的原文主张。原 Gist 只把 Bush 作为历史参照提出。见下方「本页的方法论说明」。

## 两条可分离的谱系

这条历史其实是**两条线纠缠**，分开看更清楚：

**线索 A｜链接的谱系**（技术侧）
Bush 1945 对称关联 → Nelson 1965 双向 + 溯源 → 万维网 1999 单向妥协 → Roam/Obsidian 2020 私有域双向 → LLM 自动维护
→ 见 [[bidirectional-links]]

**线索 B｜方法的谱系**（实践侧）
共同笔记簿（摘录传统）→ Luhmann 卡片盒（结构化连接传统）→ Ahrens 2017 系统化 → 数字花园 / 第二大脑 → LLM Wiki
→ 见 [[commonplace-book]]、[[zettelkasten]]

**两条线的交点**是同一个洞察：**关系的价值不低于节点本身。** 线索 A 从技术上说这件事，线索 B 从实践上说这件事。

## 矛盾与待核验

> [!warning] 矛盾：Nelson 创造 hypertext 的年份
> **说法一（1965）**：[[2026-09-18-appleton-bidirectional-links]] 明确写「in 1965 when he coined the term hypertext」；检索到的多个来源（Computing History、Wikiwand）也指向 1965 年他在 ACM 会议上发表论文。
> **说法二（1960 或更早）**：另有来源称他在 1960 年已构思这一方法并称之为 hypertext。
> **本库处理**：采用 **1965**（术语的公开创造与发表年份），但把「他更早就已构思」作为并存信息记录。两种说法可能都成立 —— 区别在于**构思**与**命名/发表**。见 [[ted-nelson]]。

> [!warning] 待核验
> - **[[2026-09-18-berners-lee-link-topology]] 的日期**：页面未标注，1999 年来自二手引用
> - **[[obsidian]] 的发布日**（2020-03-30）与 **[[roam-research]] 的创立日**（2017-04）：来自检索结果，**未收录素材**
> - **[[niklas-luhmann]] 的全部数字**：来自二手整理，该整理未标注一级来源
> - **「治理成本导致放弃双向」的因果链**：[[2026-09-18-berners-lee-link-topology]] 只列权衡，未下结论；因果来自通俗转述

## 本页的方法论说明

**这条历史是「拼」出来的，不是任何单一来源给出的。** 五份素材各自只覆盖一段：

| 素材 | 覆盖区间 | 性质 |
|---|---|---|
| [[2026-09-18-bush-as-we-may-think]] | 1945 | 一手（原文） |
| [[2026-09-18-luhmann-zettelkasten]] | 1950s–1998 | **二手** |
| [[2026-09-18-appleton-bidirectional-links]] | 1945→2020（链接线） | 通俗文献 |
| [[2026-09-18-berners-lee-link-topology]] | c.1999 | 一手（设计笔记） |
| [[2026-09-18-frand-hixon-pkm]] | 1998 | 一手（首发文献） |

**因此本页的 `confidence: medium`** —— 每个节点有据可查，但**节点之间的因果连接是本库的综合**，其中「治理成本否决双向链接」与「LLM 补上维护环」这两条最关键的解释，证据强度低于事实本身。这正是 [[wiki-lint]] 要求显式标注的东西。

**一个反身观察**：本页自身就是 [[llm-wiki-pattern]] 的一次演示 —— 五份分散素材被编译成一页连贯叙述，且明确标出了哪里是事实、哪里是推断。如果每次都从零检索，这个综合过程不会累积。

## 与其他页面的关系

- 是本库历史纵深的**主干**：[[vannevar-bush]]、[[commonplace-book]]、[[ted-nelson]]、[[niklas-luhmann]]、[[zettelkasten]]、[[tim-berners-lee]]、[[bidirectional-links]]、[[roam-research]]、[[obsidian]] 都挂在这条线上。
- [[2026-09-18-frand-hixon-pkm]] 提供了「PKM」这个名字本身的出处。
- 与 [[commonplace-book-vs-llm-wiki]] 互补：那页讲**两条独立线索的交汇**（Karpathy 与 Dan Koe），本页讲**80 年的纵向谱系**。
- 与 [[compounding-knowledge]] 呼应：整条线都在试图让知识「不消退」。

## 开放问题

- [ ] **卢曼的一手文献《Kommunikation mit Zettelkästen》（1981）未收录**，是这条线上最大的证据缺口
- [ ] 1989 年万维网提案到 1999 年单向链接定案之间的决策过程，本库只有概述
- [ ] 1960–1980 年代还有哪些个人知识系统实验？（如 Engelbart 的 Augment、Xerox PARC 的工作）本库完全空白
- [ ] 「PKM」1998 年命名之后到 2017 年 Roam 之间近 20 年的演化，本库同样空白
- [ ] 需要一份关于 Roam Research 历史的独立报道，把 [[roam-research]] 从 `low` 提升到 `high`
- [ ] 需要核实 [[obsidian]] 的发布日与创始人信息

## 来源

- [[2026-09-18-bush-as-we-may-think]]
- [[2026-09-18-appleton-bidirectional-links]]
- [[2026-09-18-berners-lee-link-topology]]
- [[2026-09-18-frand-hixon-pkm]]
- [[2026-09-18-luhmann-zettelkasten]]
