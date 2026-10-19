---
title: 46 页高置信单源页逐页裁定
type: output
slug: 2026-10-19-confidence-audit
created: 2026-10-19
updated: 2026-10-19
status: 已执行
open_executed: 0
open_decided: 0
for: llm-wiki-research
---

# 46 页高置信单源页逐页裁定（2026-10-19）

> **范围**：`confidence: high` 且 `evidence_tier` 为 `single` / `crossed-same-family` 的知识页。
> **结果**：**15 页保留 `high`，31 页降为 `medium`，0 页降为 `low`**。
> 保留的 15 页全部写入 `confidence_note`；`lint` 对已有该字段的页面不再重复提示。

## 裁定口径

只看两件事，不看页面长短：

1. **证据是否逐条核过。** 「引注真实存在」不等于「引注支持这句话」。只有正文明确记录**承重断言**已回原文 / 官方数据核对，才可能保留 `high`。
2. **已知缺陷是否承重。** 有一处未修复的数字、引注错配、译文偏差或零引注史例，就降 `medium`；缺陷只影响边角例子也一样 —— `high` 不保留「已知洞」。

另外两条硬规则：

- **实体页**：按 [[schema]] §6，单来源 / 单来源族的实体页一律 `medium`，即使素材是本人一手文章。一手性写在页内，不改变这一档。
- **分析页**：单源分析页 `medium`；RAG 一侧没有独立来源，不能拿 Karpathy 的转述当 RAG 的证据。

## 逐页表

| # | 页面 | 类型 | 证据层级 | 裁定 | 理由 |
|---:|---|---|---|---|---|
| 1 | `rag-vs-wiki` | analysis | single | **medium** | 分析页只有 Karpathy Gist 一份来源；RAG 一侧没有独立材料，对比的对方是转述 |
| 2 | `alpha-vs-beta` | concept | single | **medium** | CAPM / Jensen 只是背景，核心「Alpha → 经济租」是讲稿自拟综合，不是文献结论 |
| 3 | `baumols-cost-disease` | concept | single | **high** | Baumol 年代线与两组宏观数字已外核；AI 加工段明确不采 |
| 4 | `common-knowledge` | concept | single | **medium** | 定义文献（Lewis / Aumann）可核，但页面自报一处价格与引注不匹配，未修复 |
| 5 | `credential-inflation` | concept | single | **medium** | 31% 工资溢价未核；Collins 论文页码缺失 |
| 6 | `economic-rent` | concept | single | **medium** | 具名引证属实，但「八类租」是讲稿自拟整理，不是学界分类 |
| 7 | `effectuation` | concept | crossed-same-family | **high** | Sarasvathy 2001 原文与 U-Haul 案例逐项核对；同族讲次只作增厚 |
| 8 | `enshittification` | concept | single | **high** | Doctorow 的术语、年份、机构、成书均核；三段 / 四段差异已登记 |
| 9 | `externality` | concept | single | **medium** | 7 条引注只核「文献存在」，未逐条比对内容；公共品 / 科斯 / 奥斯特罗姆三概念合并 |
| 10 | `goodharts-law` | concept | single | **high** | Goodhart 1975 与 Strathern 普及版归属已核；讲稿弱引注但内容一致 |
| 11 | `granularity-causal-mediation` | concept | single | **medium** | 11 条中 1 条弱引注、1 条不可追溯；AI 段占 54% |
| 12 | `incentive-compatibility` | concept | single | **medium** | 10 条引注真实，但 +44% / +14% 两个数字未回原文 |
| 13 | `index-and-log` | concept | single | **high** | Karpathy Gist 一手原文；页面只描述该文提出的结构 |
| 14 | `ingest-query-lint` | concept | single | **high** | 同上 |
| 15 | `jevons-paradox` | concept | single | **medium** | 新疆滴灌 115% 与黄仁勋引语不可追溯；放射科医生预言未点名 |
| 16 | `kelly-criterion` | concept | single | **high** | 14 条核查：12 已核、1 简化、1 素材缺口；无伪引注、无使用失真 |
| 17 | `legibility` | concept | single | **medium** | 10 条只核「真实文献」，未逐条比对；metis / 默会知识边界未裁 |
| 18 | `llm-wiki-pattern` | concept | single | **high** | Karpathy Gist 一手原文；卢曼类推已显式标为本库推断 |
| 19 | `market-for-lemons` | concept | single | **medium** | 5 条引注真实，但 Tyler 的 1,575 / 804 两个数字未核；程序正义子概念并入 |
| 20 | `moloch` | concept | single | **medium** | 讲稿综合，无质量核查记录；核心是讲者框架 |
| 21 | `no-free-lunch-theorem` | concept | single | **high** | 3 条具名引注全部可核；AI 段未引入新具名引注或精确数字 |
| 22 | `optionality` | concept | single | **medium** | 9 条中 1 条两层结论、1 条不可追溯；核心标准但仍是单源 |
| 23 | `plain-text-and-git` | concept | single | **high** | Karpathy Gist 一手原文；页面只描述该文提出的结构 |
| 24 | `planning-fallacy` | concept | single | **medium** | 11 条中 2 条弱引注、2 个数字不可追溯 |
| 25 | `platform-business-model` | concept | single | **medium** | AI 段「消费者越过平台」未验证；「数据—算法飞轮」是讲稿自拟 |
| 26 | `regression-to-the-mean` | concept | single | **high** | 核心引注逐项对上；AI 段四个自查点复核大体正确 |
| 27 | `ritual-as-protocol` | concept | single | **medium** | 5 条引注未逐条比对原文；礼 / 共同知识 / 第三物边界未裁 |
| 28 | `scapegoat-mechanism` | concept | single | **medium** | 11 条引注真实，但瑞森引文有译文偏差，58% 未核 |
| 29 | `single-track-tournament` | concept | single | **medium** | 核心公式「价值单一 + 机会平等 = 全民锦标赛」是讲者判断，无引注 |
| 30 | `slow-variables` | concept | single | **medium** | 8 条学术引注真实，但 4 个史例 + 4 段正史引文零引注 |
| 31 | `social-status` | concept | single | **high** | 13 条引注全部核对；承重证据三条线均核到具名文献 |
| 32 | `soft-budget-constraint` | concept | single | **medium** | 13 条引注真实，但「60 美分」未回原文 |
| 33 | `state-formation` | concept | single | **medium** | 12 条只核「真实文献」，未逐条比对；黄宗羲定律并入 |
| 34 | `third-object` | concept | single | **high** | 讲稿段 100%；7 条引注全部核对，卷期页码无错 |
| 35 | `three-layer-architecture` | concept | single | **high** | Karpathy Gist 一手原文；页面只描述该文提出的结构 |
| 36 | `unintended-consequences` | concept | single | **medium** | 12 条真实、三条数字核过，但 40% / 70% 未核 |
| 37 | `value-pluralism` | concept | single | **medium** | 讲稿综合，无质量核查记录；核心是讲者框架 |
| 38 | `wiki-lint` | concept | single | **high** | Karpathy Gist 一手原文；页面只描述该文提出的结构 |
| 39 | `andrej-karpathy` | entity | single | **medium** | 单来源实体页（schema §6）；素材是本人 Gist，但只覆盖本库出现部分 |
| 40 | `birgitta-bockeler` | entity | single | **medium** | 单来源实体页（schema §6）；素材是本人署名文章，一手性已写在页内 |
| 41 | `cory-doctorow` | entity | single | **medium** | 单来源实体页（schema §6）；核心事实已外核，但不改变档位 |
| 42 | `james-gross` | entity | single | **medium** | 单来源实体页（schema §6）；过程模型映射有一部分是本库推断 |
| 43 | `lisa-feldman-barrett` | entity | single | **medium** | 单来源实体页（schema §6）；原书未核，仍是单篇课程转引 |
| 44 | `mitchell-hashimoto` | entity | single | **medium** | 单来源实体页（schema §6）；素材是本人自述，一手性已写在页内 |
| 45 | `obsidian` | entity | single | **medium** | 单来源实体页（schema §6）；通用事实（创建者 / 日期）未验证 |
| 46 | `saras-sarasvathy` | entity | crossed-same-family | **medium** | 同来源族实体页（schema §6）；Sarasvathy 原文已核，但两讲同族 |

## 保留 `high` 的 15 页

| 组 | 页面 | 为什么单源仍 `high` |
|---|---|---|
| 一手原文（6） | `llm-wiki-pattern` / `three-layer-architecture` / `ingest-query-lint` / `index-and-log` / `plain-text-and-git` / `wiki-lint` | 页面只描述 Karpathy Gist 提出的模式；`single` 反映 raw 份数，不表示结论已被独立验证 |
| 承重引注逐条核过（9） | `kelly-criterion` / `no-free-lunch-theorem` / `regression-to-the-mean` / `third-object` / `social-status` / `effectuation` / `enshittification` / `baumols-cost-disease` / `goodharts-law` | 页面记录了承重断言的外核结果；已知边角缺口留在「边界与反例」，不冒充已验证 |

## 验证

- `python3 tools/wiki.py lint`：`high + single/same-family` 提示 **0 条**（15 页有 `confidence_note`）。
- `python3 tools/wiki.py doctor`：0 项不一致。
- `python3 tools/wiki.py rawcheck`：无违规。
- 全库 `confidence`：`high` 24 / `medium` 233 / `low` 54；本次净降 31 页。
- 本轮只改 `confidence`、`confidence_note`、实体页单源说明与 `updated`；**没有改动任何事实断言**。

## 未解决

- `confidence` 仍是主观字段；本轮做的是「把没有理由的 high 降下来」，不是给所有页面重定级。
- 9 个保留 `high` 的页面仍有边角未核项（见各自「边界与反例」）；它们不阻止 `high`，但引用时须带限定。
- 实体页单源 `high` 是否应开例外，仍是 [[decisions]] 的未决问题；本轮按现行 [[schema]] §6 执行。
