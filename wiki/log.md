---
title: 日志
type: meta
slug: log
created: 2026-09-18
updated: 2026-09-18
status: active
---

# 日志

> 只追加，不改写。条目格式固定，便于 `grep "^## \[" wiki/log.md | tail -5`。
> 类型：`init` / `ingest` / `query` / `lint` / `edit`

## [2026-09-18] init | 知识库初始化

建立三层目录结构（`raw/` + `wiki/` + `AGENTS.md`），确定页面类型、frontmatter 规范与三个工作流。

## [2026-09-18] ingest | LLM Wiki — 用 LLM 构建个人知识库的模式（Karpathy Gist）

收录首份素材，生成 14 个页面：1 个素材摘要页、6 个概念页、5 个实体页、2 个分析页。
其中 [[vannevar-bush]]、[[qmd]]、[[notebooklm]]、[[second-brain-skill]] 四页为单来源推断，已显式标注 `confidence` 与待核验警告。

## [2026-09-18] edit | 构建工具链与浏览站点

新增零依赖 CLI 工具链 `tools/wiki.py`（init / lint / stats / search / index / build / log / new / graph），以及单文件浏览站点 `site/index.html`。
## [2026-09-18] lint | 构建完成后的首次体检：0 项机器可查问题

## [2026-09-18] ingest | 重抓 Karpathy Gist（r2）—— 发现 r1 丢失行内链接，新增 raw/2026-09-18-karpathy-llm-wiki-r2.md

## [2026-09-18] ingest | Second Brain Skill 仓库 README —— 解决 second-brain-skill 页的悬空引用

## [2026-09-18] edit | 补建 use-cases、plain-text-and-git 两页；重写 second-brain-skill 评估；AGENTS.md 增加抓取质量与重抓命名规则

## [2026-09-18] edit | git init：知识库纳入版本控制，首次提交 a980e7b

## [2026-09-18] ingest | Dan Koe《How to remember everything you read》X 长文 —— 创作者视角，独立收敛到同一架构

## [2026-09-18] edit | 补建 cybernetic-learning、commonplace-book、dan-koe、eden、commonplace-book-vs-llm-wiki；回填 index-and-log、second-brain-skill、use-cases、overview

## [2026-09-18] ingest | Vannevar Bush《As We May Think》(1945) 全文 —— 取自 MIT STS.035 镜像 PDF（Atlantic 原刊有付费墙），撤销 vannevar-bush 页的待核验警告

## [2026-09-18] ingest | Maggie Appleton《A Short History of Bi-Directional Links》+ Tim Berners-Lee《HyperText Design Issues: Topology》—— 双向链接线的两份主干材料，后者是万维网设计者关于链接拓扑的一手笔记

## [2026-09-18] ingest | Frand & Hixon《Personal Knowledge Management: Who? What? Why? When? Where? How?》(Educom 98, 1998-10-15) —— PKM 术语首发文献；原文标注 1998，纠正二手来源的 1999 引用误差

## [2026-09-18] ingest | Niklas Luhmann 原始 Zettelkasten 方法（Ernest Chiang 二手整理，2025）—— 明确区分卢曼原法与 Ahrens 2017 的再诠释；卢曼 1981 原文仍缺

## [2026-09-18] query | 个人知识管理系统的历史与演进（1945-2026）→ 归档为 analyses/pkm-history，并新建 bidirectional-links、zettelkasten 两个概念页

## [2026-09-18] edit | 补建 ted-nelson / niklas-luhmann / tim-berners-lee / roam-research 四个实体页；回填 vannevar-bush（medium→high）、commonplace-book、obsidian、overview

## [2026-09-18] lint | 收录历史素材后的体检：39 页 / 360 链接 / 0 项机器可查问题；无孤岛页。语义层面标记 1 处年份矛盾（Nelson 1963 vs 1965）与 4 项待核验

## [2026-09-18] query | 为什么在 AI 时代仍然需要 PKMS → 归档为 analyses/why-pkm-in-ai-era：核心是「AI 吃掉存取、留下策展」，五条理由 + 反面判据 + 本库自身对照

## [2026-09-18] edit | 回填 overview（新增动机层入口）、pkm-history、use-cases、llm-wiki-pattern 指向 why-pkm-in-ai-era

## [2026-09-18] lint | 第 6 次体检：40 页 / 382 链接 / 0 项机器可查问题。本页新增一项开放问题：本库缺少「AI 时代个人知识库过时」的反方素材

## [2026-09-18] edit | 引入项目层（project 页类型）：新增 wiki/projects/ 目录与模板；工具链支持 project 类型（PAGE_DIRS/TYPE_LABEL/stats/index/graph/站点配色与导航）

## [2026-09-18] edit | 新增项目层检查：项目页缺 goal、stage 取值非法、空壳项目（未链接任何知识页）；新增语义提示「未被任何项目引用的知识页」与「本库无项目页」

## [2026-09-18] edit | AGENTS.md 新增第 3.5 节「项目页（入口层）」：stage 与 status 的维度区分、goal 必须可验收、项目是 ingest 的入口；第 1 节补「三层之外的第 0 问：为什么」；分工表补「LLM 不发明项目」

## [2026-09-18] edit | 新建 wiki/projects/llm-wiki-research —— 项目层第一个实例，goal 由 LLM 从本库既有缺口起草待确认；回填 overview / pkm-history / why-pkm-in-ai-era

## [2026-09-18] lint | 引入项目层后的体检：41 页 / 398 链接 / 0 项机器可查问题；语义提示 15 个知识页未被任何项目引用

## [2026-09-18] ingest | 收录 TraeCode 官方规则文档（docs.trae.cn/ide_rules）—— 一手规格，确认 AGENTS.md 支持跨 IDE 复用、规则四档生效方式、.trae/rules 三层嵌套上限

## [2026-09-18] ingest | 收录 TRAE 官方社区帖（forum.trae.cn/t/topic/171687）—— 社区对 AGENTS.md vs rules 的分工解释，以及官方文档未回答的加载时机问题（无官方回复，置信度 low）

## [2026-09-18] edit | 新建项目 traecode-pkm-article（stage: planning）—— 写一篇「如何用 TraeCode 构建 PKMS」的文章；新增实体页 traecode、概念页 agents-md；回填 three-layer-architecture 与 overview；项目层首次有 2 个项目

## [2026-09-18] edit | 锁定 traecode-pkm-article 的 goal（北洛确认：微信公众号 / 知识工作者读者 / 不配示例仓库 / 与 llm-wiki-research 分两篇）；stage planning → active；缺口表重写为 8 条并新增【阻塞】优先级标注（4 条阻塞）；AGENTS.md 3.5 节补【阻塞】标注约定

## [2026-09-18] ingest | 收录「个人情绪觉知」主题三份素材：① 飞书《情绪觉知》个人笔记集（53.9k 字，内部混层：逐字引文 + 王路《情绪觉知100讲》课程文稿 + AI 辅助阐释 + AI 分析报告，含两处未导出的内嵌表格，含私人关系段落）② YJango《摆脱内耗：如何在焦虑与懊悔中找回自我》（一手观点长文，署名完整）③ 一份与 Claude 的对话记录《心力》（**本库第一份纯 AI 生成素材**，无任何来源，整页降级 low）

## [2026-09-18] edit | 新建项目 emotion-awareness（stage: planning）—— goal 为 LLM 起草的待确认版本，三个前提（项目性质/验收标准/期限）待北洛回答后锁定；缺口表暂为草稿。新建 13 个概念页（情绪颗粒度、刺激-回应间隙、内耗、抱怨、受害者心态、宽恕、思考vs感觉、叙事自我vs身体自我、情绪即耦合、控制二分法、情绪调节工具箱、人生是混沌系统、心力）+ 6 个实体页（王路、马可·奥勒留、弗兰克尔、索维尔、梅洛-庞蒂、YJango）；回填 overview（本库首次出现第二条独立主线）

## [2026-09-18] ingest | 认知解耦：三步调节负面情绪（得到《精英日课》）

## [2026-09-18] edit | 情绪觉知项目页回填：缺口表重写、知识层补 11 人、决策记录 +3、开放问题补 ④⑤⑥

## [2026-09-18] edit | 锁定 emotion-awareness 的 goal（北洛四答）；goal 验收对象由「人」转向「知识库」；AI 生成内容约定写入 AGENTS.md；反方素材缺口升级为【阻塞】

## [2026-09-18] edit | 项目生命周期规则：缺口表清空即 shipped，清空后新缺口另开项目；后继项目必须显式继承前任（写入 AGENTS.md 3.5）

## [2026-09-18] lint | 新增项目生命周期检查：shipped 但缺口表未清空报错 / 缺口表已清空但项目未收尾给提示。0 项机器可查问题

## [2026-09-18] query | 认知路径与身体路径如何串联 → 归档 analyses/cognitive-vs-somatic-paths（本库立论，confidence: low）

## [2026-09-18] edit | 回填 6 页：internal-friction / narrative-self-vs-bodily-self / cognitive-decoupling / emotion-regulation-toolkit / emotion-as-coupling / 项目页

## [2026-09-18] ingest | 《不可能的技艺》读书笔记（含《盗火》与心流综述）—— 混层素材（AI摘要/成书正文/课程讲稿），含本库首例伪引注；另开项目 peak-performance，并从 emotion-awareness 继承两条缺口

## [2026-09-18] query | 普通人如何掌握巅峰表现这项不可能的技艺 —— 归档 analyses/ordinary-people-peak-performance（本库第一次归档「答不好」的答案）。顺带逐行核对发现「4% 原则」只在 AI 生成段、成书正文没有；并更正了 raw/ 分层区间的判断

## [2026-09-18] ingest | 收录《超高效》(Storoni) 读书笔记 —— peak-performance 第二份素材，含弱引注；四类证据问题成型

## [2026-09-18] edit | 建 concepts/flow-terminology（心流的术语边界）；「弱引注」写入 AGENTS.md 4.1；更正本库三处自身错误（心流无定义说 / 伪引注位置与数量 / C 段未点名契克森米哈赖）；修复 lint 与 build 链接计数口径不一致

## [2026-09-18] edit | 按北洛裁定执行 raw/ 抓取元数据例外（AGENTS.md 1.1）：移除两份素材 capture_note 里的错误分层表，改为指向 sources 页的指针。查清真正病因是坐标系不同（内容相对 vs 文件绝对，偏 +39/+46）。更正本身使行数变化（+3/-5），全部下游行号已重新测量同步

## [2026-09-18] ingest | 收录《隐藏的潜能》读书笔记（亚当·格兰特）— raw/2026-09-18-hidden-potential-notes.md（895 行；含英文原书 PDF + 30 张图片已下载）

## [2026-09-18] edit | 建 sources 摘要页（四段混层：两份互相矛盾的 AI 摘要 + 成书正文 + 参考资料）、实体页 adam-grant、概念页 character-skills；更新 flow-terminology（第三侧：Grant 零次使用「心流」）与 peak-performance 缺口表

## [2026-09-18] ingest | 收录《清晰思考》(Shane Parrish) 读书笔记 —— 混层素材（未署名整理 + 中译本节选 + 得到讲书稿），自带英文原版 PDF。首次用一手原文反向核对二手整理：A 段有 5 处加法（自造『位置定律 The Law of Position』『反脆弱』『四个神经网络』、把『3+』窄化为『3-5』），并把引文误当论点。发现原书有 37,859 字符完整尾注 —— 节选丢弃了尾注，因此『素材无出处』不等于『作者无出处』。新建 sources 页 + shane-parrish 实体页；回填 stimulus-response-gap（补机制层 + 自由意志张力）与 viktor-frankl（第三个归属节点）。归属未定：填不上任何现有项目缺口，待北洛裁定

## [2026-09-18] edit | 读英文原书 PDF（395 页）核实 6 条可疑数字：4 条原书真有（2 条被改精度/单位）、1 条张冠李戴、1 条未发现；正文弱引注全部在原书尾注补齐；发现 PISA 563/507 原书不存在

## [2026-09-18] edit | 拆出 8 个概念页：imperfectionism / human-sponge / deliberate-play / scaffolding / opportunity-systems / looping / brainwriting / trajectory-evaluation（7 页已核实到原书页码，confidence 由 low 升 medium）

## [2026-09-18] ingest | 收录《思考如何超越思考》读书笔记（安妮·墨菲·保罗，The Extended Mind）—— raw/2026-09-18-extended-mind-notes.md（495 行 / 11,709 字符，本库首份零内嵌资源的混层素材）。四段混层（AI 书籍解读 / AI 文献综述 / AI 读书笔记 / 书籍目录），可确认为原书正文的不足 10%。外部核查发现本库首例「过期引注」：权力姿势激素效应（N=42 原始研究，2015 年 N=200 复现失败，2016 年第一作者公开撤回）与面部反馈重复性争议（Wagenmakers 2016 十七实验室重复失败 / Coles 2022 n=3,878 效应极小）被当作既定事实陈述，且与行 284 的争议说明互不引用。另核实武汉大学人民医院 2025 研究（痴呆-36%/抑郁-34%/帕金森-61%）与 Nature 2023 SCAN 网络为真，属弱引注。派生 6 概念页 + 1 实体页；回填 why-pkm-in-ai-era（新增理由 6：外部表征是思考本身的一部分）、cognitive-vs-somatic-paths、peak-performance 与 emotion-awareness 缺口表

## [2026-09-18] ingest | 收录《我们如何学习：大脑为何比机器学得快》（迪昂《精准学习》）读书笔记 —— raw/2026-09-18-how-we-learn-notes.md（844 行，无内嵌资源）。**本库第一份「分层边界不可判」的素材**：它不是书籍笔记，而是一份多轮 AI 对话的产物（含 Claude 对话链接；E 段自陈『作为认知神经科学领域的审稿人，我对你的稿件进行了深度重构』），A–D 段的『原稿』是否由 AI 生成文内无证据可判。含 5 条自陈式 AI 加工硬证据、三套『七』清单（与 flow-terminology 的九/六/五同构）、『四大支柱』重复 13 次。**核查**：概念图实验定位到 Karpicke & Blunt 2011 Science 331:772，摘要证实『提取练习 > 概念图』，但素材『概念图甚至不如多读几遍』在摘要中无支持 —— 命名为「外推式失真」（与同日 extended-mind 提出的「过期引注」并列为两个『第五类』候选，待裁定）。建 7 页：实体 stanislas-dehaene + 概念 four-pillars-of-learning / retrieval-practice / spaced-repetition / consolidation-and-sleep / prediction-error / innate-knowledge（全部 low，因原书未收录、核查停在摘要层）；回填 flow-terminology（第四侧）、cybernetic-learning（第四例，第一次落到神经层）、human-sponge（首例『看似矛盾实则同一主张』）；peak-performance 缺口表新增『五套框架互不引用』并更新单来源缺口为五次收录

## [2026-09-18] query | 我们如何学习、如何提高学习效果 → 归档 analyses/how-we-learn-and-how-to-improve（第一次综合「学习力」；外部核查 Dunlosky et al. 2013 PSPI 14(1):4-58 十种学习技术效用分级，但该文献本库未收录，故不入 sources —— 本库第一例『外部证据强于库内证据』的页面）。识别出新缺口：迁移（transfer）在库内为空白；交错练习无对应页。peak-performance 缺口表新增一条

## [2026-09-18] ingest | 收录 Dunlosky et al. 2013《Improving Students' Learning With Effective Learning Techniques》—— raw/2026-09-18-dunlosky-learning-techniques.md（5,910 行 / 324,348 字符，PDF 原件 55 页入 assets）。本库第一份一手学术文献，材料类型的第一次更换。校准结果：提取练习与间隔练习『高效用』获一手背书；『概念图不如重读』仍未获支撑（该综述也未收录此比较）；Cepeda 元分析已定位（转引）。建 sources 页 + 实体页 john-dunlosky；回填 retrieval-practice（low→medium）与 spaced-repetition（low→medium）；how-we-learn-and-how-to-improve 撤销『未收录』标注；peak-performance 缺口表该条标记已解

## [2026-09-18] ingest | 收录万维钢《现代思维工具》「学习与教育」板块九讲（2026-05）—— raw/2026-09-18-{cognitive-load-theory,icap-framework,deliberate-practice-talent,mental-representations,synthesis-research,tacit-knowledge,desirable-difficulty,autonomy-support,transfer-bridging}.md。本库第一次整系列收录；首次以 bot 身份抓取

## [2026-09-18] edit | 万维钢九讲派生：10 概念页 + 7 实体页 + 9 sources 页（含孤儿素材 cognitive-load-diagrams 补建 sources 页）；回填 peak-performance（缺口表 +4 条、知识层新增学习力簇）与 llm-wiki-research（边界层/方法层 + 缺口表 +2 条）；lint 0 项问题

## [2026-09-18] edit | 完善 concepts/icap-framework：新增「如何实操」（三思维转换 / 三档换挡 / 三场景动作升级 / 三个陷阱）与「AI 时代：助力与陷阱」（四步 SOP + 4 条 Prompt 模板 + 认知负荷守恒定律 + 三明治路线图）。两节内容全部出自 AI 生成段（raw 行 506–1010），已在页面顶部与节首显式标注。另补两条素材没有的陷阱（AI 无立场 / AI 总结制造更深的流利度幻觉），标为本库立论 low 无来源；新增本库流程与 ICAP 的对照表

## [2026-09-18] ingest | 写作即思考：不要把认知外包（飞书文档，多来源缝合 / 分 18 段 / 三处引注失真）

## [2026-09-18] edit | 北洛裁定本库层面三条约定，全部写入 AGENTS.md 4.1 与第 8 节：(1)「错位引用」与「外推式失真」合并为一类「引注的使用失真」（5 例，处置=逐条公示素材说X↔原文说Y，不整页降级）；(2) ingest 必须含一个 LLM 不可代劳的动作，定为 HFQ 人类先问（第 −1 步，人类须在 LLM 读素材前亲笔写收录理由+1–3 个问题，LLM 不得代写）；(3) AI 生成占比过半不触发整页降级，改按内容质量判（判据=这段话若错了读者能不能自己发现）。同步改动：sources/2026-09-18-writing-is-thinking 由 low 上调 medium（新增『定级变更说明』与『人类先问』占位节）；tools/wiki.py lint 新增 HFQ 检查（语义提示，不计问题数）；overview 六类表重写并记三条裁定；llm-wiki-research 缺口表移出『哪一步只有人能做的』一条并记入决策记录；cognitive-outsourcing 回填已裁定。lint 0 问题

## [2026-09-18] edit | 写作即思考素材派生：5 概念页（writing-as-thinking / cognitive-debt / cognitive-outsourcing / brain-rot / productive-resistance）+ 4 实体页（nataliya-kosmyna / advait-sarkar / alain-de-botton / wang-shuaiguo）。回填 traecode-pkm-article（知识节「动机层的反面补丁」簇 +5 页）与 peak-performance（缺口表 +1 条：注意力侧首次触及）。此前只记了 ingest，派生页无记录 —— 本次补记

## [2026-09-18] lint | 全库巡检 + 收尾：154 页 / 1810 链接 / 机器可查 0 项。重建 index 与 site（此前 site 停在 13:37，10 个文件更新在其后）。**修正一处口径误判**：index 的「页面总数」不含 4 个 meta 页，lint 的数含它们，两者恒差 4 —— 巡检时曾据此误判「index 滞后 10 页」，实际 index 一直是准的。已在 cmd_index 生成的统计行里显式标注口径。另核查：行区间坐标系已修复（抽查 5 处全中）；断链 / 悬空 sources / 出链过少均为 0

## [2026-09-18] query | 「写不出来」有几种病因？→ 立论归档 analyses/why-writing-fails。「写作即思考」说写不出来＝没想清楚，但库内已有两个反例（德波顿：害羞；波兰尼：不在文本里）。本页把四种病因摆在一起，关键结论：波兰尼那条不是第四条并列项，而是**否定前三条的前提** —— 前三条说写是治疗，第四条说写是损害。故与 writing-as-thinking 的关系从「界线未划」升级为「有限范围内的真实冲突」（仅默会知识那一类）。已回填三处：writing-as-thinking（限定断言适用范围 + 冲突升级）、tacit-knowledge（关系节）、traecode-pkm-article（知识节，作为文章论点的边界护栏）。四条待验证假设已写成可证伪形式

## [2026-09-18] ingest | 收录李继刚《学习即遗忘，理解即压缩，压缩即智能》（raw/2026-09-18-learning-is-forgetting.md，543行/13,964字符，三张PNG全部下载）；建 source 页 + 3 概念页（information-bottleneck / compression-as-intelligence / learning-as-forgetting）+ 5 实体页（naftali-tishby / marcus-hutter / thomas-griffiths / andrew-saxe / li-jigang）；外部核查 6 项：arXiv:2604.07569 真实存在（ICLR 2026，八位作者，李继刚不在其中）、Hutter Prize 1GB 属实（本库原怀疑其错，核查后是素材对）、怀特海引语归属存疑、两阶段叙事有反方（Saxe et al. 2018）、素材未提 Tishby 2015/2017 与 2018 争议三个环节

## [2026-09-18] query | 问：『遗忘作为学习机制』在认知科学里有没有一手文献？答：有，且标题就是该命题 —— Robert A. Bjork《Forgetting as a Friend of Learning》(2014, Psychology Press, Jacoby Festschrift)。已从 UCLA Bjork Lab 官网取回 PDF 原件（23页/39,272字符，文本层完好）+ 建 source 页。核心：storage strength 与 retrieval strength 非对称（存储增益是提取强度的递减函数）；Vlach et al. 2008「间隔诱发遗忘，遗忘促进抽象」。learning-as-forgetting 由 low 上调 medium。卡点：Bjork & Bjork 1992 原文 PDF 是扫描件无文本层 —— 本库第一条因技术形态被卡的文献

## [2026-09-18] ingest | 收录《叙事：这个宇宙的第一性原理》（万维钢《现代思维工具课》「基本世界观」第一讲，2026-03-18）— raw/2026-09-18-narrative-first-principle.md（681 行 / 15,559 字符；4 张内嵌图片因 bot 无媒体权限未下载，图注保留在 alt 文本）。**六段混层**（A 万维钢主文 / B 三名读者留言 / C·D·E·F 四份 AI 生成块，AI 生成约占 60% 篇幅），为本库分层最多的素材（首次六层）。**本库两个「第一次」**：①**第一份引注全部核实为真的素材** —— 七条具名引注一条不假，注释 [9] 的 Albert《Physics and Narrative》(Reading Putnam 2012, ch.18) 与 Judes《Narratability and Cluster Decomposition》arXiv:1002.1726 精确到章节与编号，**且 Judes 实为反驳 Albert，素材措辞「后续讨论」是准确的**；Shiller 叙事经济学 2017 亦精确到 AER 107(4):967-1004。②**第一份「批判块批判了一篇它没读过的文章」的素材** —— F 段点名主文「缝合了卡尼曼／惠勒／塔勒布／贝佐斯」，四人在 A 段**零次出现**（逐字统计：卡尼曼 1、惠勒 1、贝佐斯 1 全在 F 段自身行 621；塔勒布 2 次亦全在 F 段），A 段实际所引为 Wolfram／Dennett／Friston／Harari／Shiller，与 F 段名单无一重合；F 段「AI 时代即叙事工业化」为第四支柱之说同样无对应。**提出新失真类别候选「批判对象失真」**（伪引注伪造来源、使用失真错用来源，本例**伪造的是被批判对象本身**），与已裁定的「引注的使用失真」并列为当日第二个候选，待北洛裁定是否入 AGENTS.md 4.1 分类表。与 [[narrative-self-vs-bodily-self]] 构成**本库第二处明确内部矛盾**（该页：叙事是覆盖身体的异化；本素材：自我由叙事构成）——但层级不同，可能可调和，素材未做辨析。另给 [[cybernetic-learning]] 的「目标 vs 焦虑」张力提供了第三种答案：**目标是叙事的产物，不是给定量**。归属建议 [[emotion-awareness]]（填三条非阻塞缺口，不填任何【阻塞】），**本轮未回填任何项目页**，等裁定；HFQ 节已建，等北洛亲笔

## [2026-09-18] edit | 《叙事》素材派生 8 个概念页：narrative-as-first-principle（判为「有启发性的隐喻，不是物理主张」，反方就在素材注释 [9] 里）/ narrative-power（三级递进，操作层全出自 AI 生成段；反方是叙事暴政）/ narrative-identity（与 narrative-self-vs-bodily-self 构成本库第二处明确内部矛盾）/ narrative-as-objective-function（「叙事决定目标函数」接上 cybernetic-learning 的链条，给 emotion-awareness 那条悬置张力提供第三种答案：目标不是给定量）/ ruliad（只在库里起踏板作用，一手未取回）/ free-energy-principle（把 prediction-error 的「三层链条」问题推成四层 —— 加剧缺口而非解决）/ narrative-economics（Shiller 2017 AER 107(4):967-1004，本素材核查最干净的一条引注）/ critique-target-distortion（新失真类别候选，n=1，待裁定）。**实体页一个都不建** —— 按 AGENTS.md 3.2 阈值（≥2 份素材或核心论点），Wolfram/Dennett/Friston/Harari/Shiller 均只在 1 份素材出现且非核心，作用已分别写进对应概念页。回填四处既有页：narrative-self-vs-bodily-self（新增矛盾关系 + 开放问题部分缓解）、cybernetic-learning（新增上游）、prediction-error（三层变四层）、sources 页（候选清单改为链接并写明不建实体页的理由）。lint 0 项，174 页；但 lint 提示「9 个知识页未被任何项目引用」（8 新页 + shane-parrish）—— **这是归属未定的正确信号，等北洛裁定**

## [2026-09-18] edit | 北洛裁定：为「基本世界观」六讲另开项目页 modern-thinking-tools；第一讲归属改判，8 个派生概念页归位，万维钢实体页更新

## [2026-09-18] edit | 北洛亲定 modern-thinking-tools 的 goal：把六讲编译成逐条标注证据性质的综述（采纳 LLM 版本 A 的前半句，未纳入「裁决与九讲的张力」）— 项目转 stage: active；缺口表【阻塞】重判：只剩 HFQ 与具名引注核查，其余降为非阻塞

## [2026-09-18] edit | 北洛裁定：全面移除 HFQ（人类先问），后续 ingest 不再有这个前置条件 — 已同步移除 AGENTS.md 4.1 第 −1 步与第 8 节、tools/wiki.py 的 lint 检查、2 份已建节的 sources 页（narrative-first-principle / writing-is-thinking）；AGENTS.md 4.1 保留墓碑块记录原条款与代价。连带后果：cognitive-outsourcing 那条「本库算不算『先思考』一侧」的开放问题由 [x] 改回 [ ]（判据就是 HFQ，判据没了问题重开）；overview / wiki-lint / llm-wiki-research / modern-thinking-tools 均已同步

## [2026-09-18] ingest | 收录《重尾：世界服从极端值》（万维钢《现代思维工具》「基本世界观」第 2 讲，2026-03-18）— raw/2026-09-18-heavy-tail-notes.md（2,619 行）。**本库两项纪录**：分层最多（15 层，前纪录 6 层）＋ AI 生成占比最高（约 92%，A 段讲稿仅 148 行占 5.7%，AI 输出量是原稿的 15 倍）。AI 段不是摘要扩展，而是**在讲稿上寄生出一整套个人商业产品**（Multiplicative OS v1／飞书模板／半自动 v2／Prompt Library／三层变现飞轮／公众号投放建议），末段附一份以第一人称索取「乘法」领模板的**推广文案草稿**（非万维钢所写，是飞书文档整理者的内容）—— 按利益披露条款整页降为 low，A 段单独 medium。核心论证链：小世界人为平均 → 真实世界重尾（1%>99%、8 人>后一半人口）→ 成因是正反馈（马太效应；资本／吉布拉特定律／名气／学术四类例证）→ 机制公式「增量 = 动作 × 存量」→ 加法世界 vs 乘法世界 → 行动层放弃补短板做长板（Sam Altman 2019-04-20 推文）→ 风险层黑天鹅与第二曲线。引注核查 11 条：**具名 5 条已核**（索维尔《社会正义谬误》2023 乌干达例 = 二手印证、Sam Altman 引语 = 内容印证、帕累托／吉布拉特定律／塔勒布概念真实但一手未取回）；**无出处精确数字 4 条标弱引注**（最富 1%／8 人／风投 10%→85%）；引注编号 [2] [4] 无对应注释段（注释段未随飞书导出）。**Oracle/AMD 2025 股价一夜涨 30–40% 未核，计入项目【阻塞】**。与 [[deliberate-practice]] 线方向相反（本讲把「努力」定性为线性思维，那边默认努力有效）—— 同一作者同一门课两个板块，未裁决，是 [[modern-thinking-tools]] 最值钱的非阻塞缺口。新建 2 个概念页 [[heavy-tailed-distribution]]、[[multiplicative-world]]；**实体页一个都不新建**（帕累托／吉布拉特／塔勒布／Sam Altman 均只出现 1 次且非核心论点），**回填 [[thomas-sowell]]**（补上《社会正义谬误》，是其第一条标了书名与年份的引用）。归 [[modern-thinking-tools]]。本次 ingest 无 HFQ 前置（该条款已于同日由北洛裁定移除）

## [2026-09-18] ingest | 收录《能动：稳态生存的观念陷阱》（万维钢《现代思维工具》「基本世界观」第 3 讲，2026-03-18）— raw/2026-09-18-steady-state-trap-notes.md（575 行，正文 537 行）。A 段讲稿 39–189 行占 28%，AI 段 72%。

【本份与第 2 讲《重尾》是两种不同型的 AI 段缺陷 —— 这是本轮最重要的判定】重尾那份是「寄生」（在原稿上盖商业产品，讲稿内容基本没被动）；本份是「改写」—— 讲稿行 61 明确声明「我不想用弱者/底层/前现代之类的词……这些是策略问题，不是阶层问题」，而 4 份 AI 生成的《人生说明书》通篇是「底层/平民子弟/向上攀爬」，连那份看起来最忠实的「核心洞见」摘要都独独删掉了这一句。改写比寄生更隐蔽，因为它冒充忠实摘要。

【另一处差异：本份的 AI 段是半被邀请的】讲稿行 189（作者正文）写着「GPT读罢此文后制作的一页版《人生说明书》」，第一份 AI 输出属被邀请；但只邀请了「一页版」，文档里却有 4 个版本 + 1 个合并版 + 1 份核心洞见。H 段自陈「我之前提供的那份（版本A）」「GPT提供的这份（版本B）」—— 直接证明至少两拨 AI 输出在文档内部互相点评。另：同一份 10 条在行 195–208 与 222–235 逐字重复两次（复制粘贴未清理）。

【定级】本份无推广内容，不触发利益披露降级（与重尾那份不同，后者整页 low 的唯一理由是末尾引流话术）。按北洛 2026-09-18 裁定，AI 占比 72% 本身不是降级理由，故整页 medium；不给 high 的理由是 A 段内有 2 条不可追溯引注 + 若干未验证断言。

【引注核查 12 条】具名 2 条已核：① Hoffman & Yoeli《隐藏的博弈》「次级奖励」（书真实，MIT 两位研究科学家，术语经二手印证「we can learn to like them」，一手书页未取回）；②「苏超」= 江苏省城市足球联赛（2025-05-10 开幕，13 设区市，官方定位省级业余赛事）—— 讲稿定性为「业余联赛」与事实相符，本条原本可疑（该词也可指苏格兰超级联赛，但那不是业余的），核查后成立。概念可核 1 条：文化滞后 = Ogburn 1922《社会变迁》，讲稿未具名。与主流叙述张力 1 条：侘寂「起源于物资匮乏」—— 可及来源把侘寂追溯到茶道（珠光、利休）与禅宗，与「物哀」「幽玄」并列，未找到支持匮乏起源说的来源，可查而未查。注释 [3] [4] 不可追溯（注释段未随飞书导出）。收束小诗（行 181–185）作者存疑未标：同讲行 189 证明作者此时已用 GPT，且第 4 讲注释 [9] 自述其收束小诗前两句为 GPT 所作。

【新建 2 个概念页】[[steady-state-survival-logic]]（稳态生存逻辑，作者自造词，三大基因：资源匮乏/强从众/简单模型 → 四类推论：风险厌恶/低能动性/面子文化/指标崇拜）、[[agent-vs-tool]]（能动者 vs 工具）。后者是本讲最值钱的交叉点：讲稿行 175「你是调用工具的人，你不能是别人的工具」为 [[cognitive-outsourcing]] 那条因 HFQ 移除而重开的开放问题提供了候选判据 —— 看你是调用工具的那个还是被调用的那个。且「能动性」在第 4 讲《约束》讲稿段也出现（raw 行 94/151/226/232），满足 ≥2 份素材阈值。

【回填 3 个旧页】[[victim-mentality]]（第二份素材：结论同向但论证强度差一档 —— 那份拆过七层，这份没拆且不在讲稿 AI 段里；已回填且未上调其 confidence，同向重复不构成独立佐证）、[[heavy-tailed-distribution]] 与 [[multiplicative-world]]（第 3 讲行 53 显式回指「我要让他理解重尾分布……加入乘法世界」，坐实六讲互指）。

【实体页一个都不新建】Hoffman & Yoeli 只出现 1 次且非核心论点，与上一讲不建帕累托/吉布拉特/Sam Altman 同一判例；Ogburn 讲稿根本没提，是本库查出来的，不建页。

【修正上一讲的一处估计值】[[2026-09-18-heavy-tail-notes]] 原写「第 3 讲行 ~107」，本轮核实精确行号为 145，已回填。

归 [[modern-thinking-tools]]（第 3 讲）。项目页知识一节已回填，两条开放问题关闭（四版本《人生说明书》的性质判定、重尾推广草稿的定级），转入决策记录；具名引注核查进度 2/6。lint：无断链，未被项目引用的知识页只剩 shane-parrish（与本项目无关）。

## [2026-09-18] ingest | 收录《现代思维工具·发刊词》（万维钢，得到课程，2026-03-18）— raw/2026-09-18-modern-thinking-tools-prospectus.md（1,701 行；frontmatter 1–68 行，正文自第 70 行起，坐标系：正文行号 = 文件行号 − 69）。抓取路径：lark-cli wiki +node-get 解析 obj_token（bot 缺 wiki:node:retrieve，node-list 报 99991672，目录未取得）→ docs +fetch --doc-format markdown（document_id UmOudHoP5oEaEmxuXvvcuWIznwd，revision_id 1650，45,319 字符）。**混层最深的一份**：22 段（A–V），讲稿仅 B 段 94–228 行占 8.3%，AI 生成段 D–V 合计 84.0%（前纪录 heavy-tail 15 段 / 92%，本次为分段数最多的）；2 张图片未下载、3 条外链含 claude.ai 分享链接。**判为课程发刊词（讲次 00），不是「基本世界观」六讲之一** —— WebSearch 取回得到官方大纲，确认基本世界观实为 7 讲（缺《问答：叙事和讲故事、造梦的区别是什么？》）。**本份最值钱的一段**：B 段讲稿行 1295–1304 就德鲁克「可测量即可管理」自我指出这是误引 —— 但同段又把爱因斯坦那句错配成德鲁克句的下半句，即「自指误引」与「引注使用失真」在同一段并存。外部核查 8 条具名引注：富勒 ✅、德鲁克误引 ✅ 且素材自指、威尔逊 ✅ 一处改写、芒格 ✅ 一处混淆、苏格拉底-米尔曼 ✅ 且素材主动标疑、眼镜蛇效应 ⚠️ 存疑、古德哈特等 7 个只列名无内容。新建 sources 页 + 4 概念页（intelligent-life-system / three-solutions / ai-convergence / lesser-and-greater-vehicle）+ 1 实体页（charlie-munger —— 建页依据是 ≥2 份素材且本份给了第一条可核到书与章节的引注 Poor Charlie Almanack Talk Eleven）。**四元素不拆成四页**（拆开会丢掉「闭环」）；**七个名单概念不建页**（讲稿零内容，按 AGENTS.md 3.2 阈值等再次出现）。回填既有页 6 处：wanweigang（收录计数 15→16，新增身份证据第 5 条与写作特征第 5 条——行 148 作者自述 AI 分工）、modern-thinking-tools（知识节新增发刊词整段、缺口表新增 3 行、关闭「板块几讲」开放问题）、cybernetic-learning（新增第五例：同一条控制论骨架被两个作者拆成两套四要素；并据「控制论外壳装预测编码判据」收窄开放问题问法）、cognitive-outsourcing（新增两个样本：N 段 AI 被质疑迎合后逐字否认迎合的一手原文——本页第一份非二手材料——与行 148 的人机分工自述）、compression-as-intelligence（新增第二份素材并定为「命题 vs 用例」关系，不上调 confidence）、productive-resistance（新增「阻力缺位」样本，与待办里「阻力过载」明确分列不合并）、free-energy-principle（第四处出现——进了「AI 最爱用」名单，只作为流行度观测，知识增量为零）。**新增待裁定项**：①发刊词归属（甲暂归 modern-thinking-tools / 乙另开课程级项目 / 丙不归）；②是否收录课程官方大纲进 raw；③是否收录《问答》素材；④「AI 否认迎合」与「收敛≠解释力（以流行度冒充有效性）」这两类是否提为 AGENTS.md 4.1 新类别（本库均建议不并、单列）；⑤德鲁克误引是否提为样本。**顺带修了一处错**：charlie-munger 初稿把尚未 ingest 的 raw/2026-09-18-hard-constraints-notes.md 写进了 sources 与 wikilink（该素材是 modern-thinking-tools 待收录的第 4 讲），造成 2 条断链并**掩盖了 lint 的「raw 尚未收录」信号**（该检查把「任何页 sources 里提过」都算作已收录）；已改为纯路径引用，lint 的未收录清单由 2 项恢复为正确的 3 项。索引已重建（183 页，不含 4 个系统页）。

## [2026-09-18] edit | 北洛指令：单独开一轮把 overview 补到当前状态（含主线四「现代思维工具」）。**本页此前落后 29 页**（停在 154 页 / 32 摘要页 / 4 项目，实际 187 / 38 / 5），且这不是某次 ingest 的疏忽 —— **AGENTS.md 4.1 第 6 步只要求更新 index，没有要求更新 overview**，所以连续 4 次 ingest 都合法地跳过了它。**已把「更新 overview」列为待裁定项，并附条件（只在新增主线/新增项目/页面数变化超 10/出现新证据类别时才必须改）**，避免常驻成本失控。本次改了 9 处：(1) 顶部 TL;DR 由「三条线」改「四条线」＋新增主线四定义（唯一按「一门课」而不是「一个主题」为单位收录的线）；(2) 范围节新增主线四在范围块（收录单位、两个板块、关心的是证据性质与 AI 段占比、明确不包含什么）＋「四个项目」改「五个」；(3) 核心线索节补一张「另外三条线的入口」表 —— 原 12 条线索只覆盖主线一，容易让人误以为本库只讲 PKM；(4) 当前状态节全量重算：38 摘要页 / raw 42 个 .md / 页面 187（内容页 183 + 系统页 4）/ 五项目（附各自缺口表行数 10·8·10·19·12）＋新增素材按主线分布（一 13 / 二 4 / 三 7 / 四 14）＋六个「第一份」历史记录（补上 narrative-first-principle 是第一份七条具名引注全真的素材，且它属主线四）＋**3 份已落盘未收录的清单**（硬约束第 4 讲 / 可能第 5 讲 / 内核第 6 讲，三份 frontmatter 已自带 series）；(5) 新增「### 第四条线的位置」整节，含**两个结构性问题**：问题一「同一门课的素材被两个项目分掉」（教育与学习九讲 → peak-performance，基本世界观 → modern-thinking-tools，代价是这门课在入口层没有单一归属）＋问题二「发刊词归属未定」（甲暂归 modern-thinking-tools / 乙另开课程级项目 / 丙不归）；并记下主线四**最值钱的自相矛盾**——同一门课两个板块对「努力」方向相反（刻意练习那讲默认努力能改变能力，重尾第 2 讲把努力定性为线性思维），素材未辨析、本库也不替它辨析；(6) 新增「仍在排队的四个类别候选」表（素材无出处↔作者无出处 / 批判对象失真 / AI 否认迎合 / 以流行度冒充有效性，四类均未过「≥2 份素材」阈值，建议先记账不动 AGENTS.md，唯第一条是核查动作规则建议直接写入）；(7) 六类表下方补第 4 条「伪引注」由「待定」改为「已写入 AGENTS.md 4.1」（该条记录已过期）；(8) 「本库自己的缺口」第 3 条（素材混层）由「四例」更新为「十一例」并补两项纪录（重尾 15 段/92%、发刊词 22 段/84%），得出**分层表已从临时补丁变成标准件，但不建议改模板**（逐份不同，容纳任意段数等于不要模板），改为建议「分层表定为 sources 页必需节」；并记下 AI 占比与分层数不是一回事（段数最多的那份占比反而更低）；(9) 下一步建议节新增 7 条（最重要：把更新 overview 写进 AGENTS.md 4.1 收尾步骤、收录基本世界观剩余三讲、发刊词归属裁定、同门课归两项目是否要加可检索记号、是否收录课程官方大纲与《问答》一讲、四个类别候选裁定）。**顺带修一处新引入的断链**：overview 误引 `deliberate-practice-talent` 双括号链接（该 slug 不存在，它是讲次名；实际是 source slug `2026-09-18-deliberate-practice-talent`，概念页是 `deliberate-practice`）已在 lint 查出后改为双链接。**本条日志首次写出时把该 slug 写成了双括号链接，自己也引入一次同样的断链，已就地改为行内代码。**lint 复跑 0 断链；3 项待收录保持不变（那是待收事实，不是问题）。

## [2026-09-18] ingest | 收录万维钢《现代思维工具》「基本世界观」板块剩余三讲（北洛指令：把 raw/ 里 3 份已落盘未收录的素材全部收录）—— 第 4 讲《约束：先尊重，再行动》（raw/2026-09-18-hard-constraints-notes.md，564 行，正文自 40 行起，2026-03-19 22:46）、第 5 讲《可能：不确定性是意义的燃料》（uncertainty-fuel-notes，373 行，正文自 41 行起，2026-03-22 23:02）、第 6 讲《内核：你的三个「自我」》（three-selves-notes，1,342 行，正文自 41 行起，2026-03-23 22:46）。**收纳后「基本世界观」六讲 + 发刊词全部到齐，raw/ 与 sources/ 首次完全对齐（0 份待收录）。** 三讲的证据质量落差极大，逐份判定：第 4 讲讲稿占 25.2%、全篇仅 2 个编号引注但 DOGE 一组数字「不靠引注靠公开预算结构」可验算、AI 段 68.5%（新定型「人设化改写」，把讲稿「约束才值得学习」改写成「严禁为了成长而学习」）；第 5 讲讲稿占 36.9%（已收四讲最高）、**引注 8/8 全部为真**、AI 段 53.5%；**第 6 讲讲稿仅占 12.1%（最低），后段 22.9% 是无署名异源拼接，整页定 low**。外部核查 14 条，其中 5 条硬结果：①**柯维《高效能人士的七个习惯》第一条可核引注**（1990 Fireside 版 p.90 英文原文「While we are free to choose our actions...」，素材两处用词简化但非伪造）；②**「运气 > 能力」的核心实验找到原文** —— Pluchino, Biondo & Rapisarda (2018) *Talent vs Luck*, arXiv:1802.07068 / Advances in Complex Systems 21(03n04):1850014，参数逐条对上（1,000 agent / 正态天赋 / 40 年 / 每半年随机事件 → power law），项目页该缺口「圆满关闭」；③**科研经费抽签制度属实且素材偏保守**（新西兰 HRC Explorer Grants 2013 全球首次 / 德国大众基金会 Experiment! / 瑞士 SNSF，另有奥地利 FWF 与英国科学院素材未提）；④**第 6 讲「决定前几百毫秒」查明为「过期共识（无引注版）」** —— 所指是 Libet et al. (1983) Brain 106:623-642，但已被 Schurger, Sitt & Dehaene (2012) PNAS 109:E2904-E2913 实质修正，而素材无引注却写「科学家用多个实验证明」；**这是「过期引注」的第 2 例**（此前只有 1 例，该类别单列与否仍在等裁定），本库建议扩宽定义以容纳「暗示的引注」；⑤**查出一处新的使用失真**：第 4 讲把 CBS/PSP 原文明确排除的诉讼费与税收损失并进了 1,350 亿（本库「引注的使用失真」第 6 例）。核查同时发现两处本库应当公道的记录：第 5 讲格林《权力的 48 条法则》四条方法逐条对应 Law 17/27/32/5（**转述准确，不是编的**）；第 6 讲那段「西方谚语」（当心你的思想…）**素材不给任何归属** —— 而该格言学界公认源流不明（常见误挂老子/佛陀/爱默生/撒切尔之父，目前最早可考的定型版本是 1977 年 Frank Outlaw），**不给归属是对的**。新建 3 份 sources 页 + 7 个概念页（hard-constraints / wishful-thinking-layers / types-of-uncertainty / uncertainty-as-fuel / luck-over-talent / compensatory-control / three-selves）+ **2 个实体页**（daniel-dennett —— 库内第二次出现，叙事重心；nassim-taleb —— **补一笔欠账**，他在库内已出现 4 次早过阈值却一直未建）。**回填 15 处既有页**：modern-thinking-tools（**整体重写**：缺口表移除 6 条已关闭项并新增 4 条、决策记录 +6、知识节按讲次重排、验收判据第 4 与第 5 条标记达成）、agent-vs-tool（第 4 讲关闭其挂账「他人也是能动者」+ 第 6 讲提出新问题「能动者被指定给内核自我，但能动这个动作发生在别处」）、free-energy-principle（**第一次拿到可操作内容**：打脸时三条路）、prediction-error（三层链条问题 → 加第四层「认知 / 自我层」，也是本库第一次拿到「误差之后怎么办」）、cybernetic-learning（补上链条的后半段）、narrative-identity（**第 6 讲把叙事自我下调一层**，第 1 讲 vs 第 6 讲的关系待判）、narrative-as-first-principle（**叙事获得一个新功能**：把不确定变成确定的奖励瞬间）、steady-state-survival-logic（**板块内第二处方向性张力**：第 3 讲求稳是基因 vs 第 5 讲「静，并不好」）、deliberate-practice 与 character-skills（对撞「能力本身也是运气」）、heavy-tailed-distribution（第 5 讲补齐机制）、intelligent-life-system（后三讲把四元素逐格填上内容）、stephen-covey、charlie-munger（由纯路径引用改为链接）、wanweigang（**更正一处提前记账**：此前写「已收十六份」但当时三讲只有 raw 文件、无 sources 页；现已对齐）、overview（数字 + 主线四收官）。**新增待裁定项 5 条**：①「过期共识（无引注版）」并入「过期引注」还是单列；②「不靠引注、靠公开预算结构就能验算」是否立为新的证据类别（DOGE 样本）；③「中年」人设 AI 段的判别词表是否写进 AGENTS.md 4.1 作分层辅助信号；④23 张内嵌图片是否放弃重抓、改为逐张标注「图中数字未核」；⑤第 5 讲 cite 块指向的三份飞书文档是否收录。**另提出一个需要北洛拍板的选择**：综述页（goal 本体）是按六讲的论证线写，还是按「讲稿 / AI 段 / 证据性质」三栏写 —— 本库倾向混合。lint 复跑 **0 项机器可查问题**，页面 199（内容页 195 + 系统页 4），新增 12 页全部有入链、无孤岛。

## [2026-09-18] edit | 重建浏览站点 site/index.html（北洛指令）。此前一版停在 2026-09-18 18:11，落后 12 个页面 —— 该时间点之后发生了三次改动：发刊词 ingest（18:17–18:19）、overview 补到当前状态（18:36）、「基本世界观」第 4/5/6 讲 ingest（18:5x–19:1x）。重建后 199 个页面 / 2511 条链接，文件 1.61 MB → 1.91 MB。已校验：12 个新增 slug（7 概念 + 2 实体 + 3 sources）全部在 JSON 数据里，三个模板占位符无残留，副标题为「199 个页面 · 2026-09-18 生成」。注意 site/ 是**构建产物**，每次改完 wiki/ 都应重跑 build —— 否则浏览站点与实际内容不一致，而这件事没有任何自动检查会发现。

## [2026-09-18] edit | 北洛裁定：站点构建「只在里程碑时」—— 写入 AGENTS.md 新增 4.1.1 节，并在 4.1 的收尾步骤里加第 9 步（条件性构建）。内容：①明确 site/index.html 是**构建产物**（视图）而非文档，**不与 index.md / log.md 同级、不需要每次更新**；②五条里程碑判据（新增主线 / 新增或关闭项目 / 页面总数变化超 10 / 一次大 ingest 收尾（整系列、多批、或单份派生 ≥5 新页）/ 人类明确要求），**满足任意一条即构建，都不命中则一律不构建**；③写明代价：**没有任何机制会发现站点落后** —— lint 只管 wiki/ 下的 Markdown、index 只管 wiki/index.md，site/ 不在任何检查覆盖内（2026-09-18 曾落后 12 个页面，靠人发现才补），因此落地方式定为「照表逐条判断」而不是「记得构建」，因为**「明确地不构建」与「忘了构建」结果相同、过程不同 —— 前者可审计**；④构建后须在 log.md 记明**上一次构建时间**与**跨越的改动次数**（例：此前停在 18:11，之后发生三次 ingest），这是日后判断站点可信度的唯一依据；⑤补一条与第 6 步「更新索引」的区别说明：index.md 是知识库的组成部分（查询第一站）必须每次更新，site/index.html 是导出的快照、允许滞后 —— 把两者混为一谈会让「必须做的」和「可以攒着做的」共用一条规则，那才是常驻成本失控的来路。另在 overview 的待裁定项上补记：这条裁定是本库同类问题的**先例**（「该更新的东西不在清单里 → 靠人发现 → 补规则」），overview 自身那条「是否进 4.1 收尾清单」可照 4.1.1 的写法办，两者触发条件高度重叠。**这是本库第三次走「素材或事故逼出规则 → 人类裁定 → 写入 schema」这条路。**

## [2026-09-18] ingest | 收录《叙事自我》（飞书 wiki 文档，2,279 行 / 47,673 字符）—— **本库第一次推翻自己的一个证据类别判定**

**素材身份（本轮最重要的发现）**：北洛给的链接 `GNALwzikvijEwCkDYZ9cHkyQnRg` **不是一份新素材** —— 它是本库已收录第一讲 [[2026-09-18-narrative-first-principle]] **正文行 83 的 `<cite>` 所指文档**，也是它的**飞书 wiki 子节点**（`parent_node_token` = 第一讲 node_token `O6UPwafnNiqlqakqyKYcJGKHnOf`），且**创建于 2025-03-05，早于第一讲一年有余**。第一讲 sources 页那条挂账待办「追一份素材……本库未收录」**本轮关闭**。落盘 `raw/2026-09-18-narrative-self.md`（frontmatter 1–58，正文自第 60 行起，**加号坐标系 = 原文行号 +59**）。

**抓取路径更正（重要）**：首次用渲染页提取，**只取回开头约 20 行格言块**（2,279 行中不到 1%），**且无任何截断提示**；改用 `lark-cli wiki +node-get` → `docs +fetch --doc XoRddxNRvod8MOxCQlZc8tGxnMf --doc-format markdown`（revision_id 923）后取回全文。**无图片、无附件**，正文外链仅 1 条（《科学思考者》-万维钢 dedao 电子书页）。**这是本库又一次验证 4.1 第 0 步「抓取质量优先于抓取速度」。**

**分层**：24 段。**可确认为署名作者原文的只有 91 行 / 2,279 行（约 4%）** —— C 段（叙事自我引文块）、E 段（something bigger / 战俘 / 张载）、G 段（曾国藩天津教案全文，自带来源标注）；**其余约 93% 为无署名 AI 加工**。文档内多处保留 AI 对话轮次语言特征，其中行 676「以下为您提供三种不同风格的排版方案，您可以根据发布的平台……选择最合适的一款」是**决定性的** —— 它是对用户请求的直接回复。整页 `low`（理由三条：AI 框架以规律口吻给出却零引注／含一处来源等级冒认／署名段与 AI 段无缝混排无标记）。

**一、本库层面的重大修正：第一讲 F 段的「批判对象失真」判定被推翻，该类别撤回。** 本库原判（记于 [[critique-target-distortion]] 与第一讲 sources 页核查表第 8 条）：F 段**幻觉**出一个被批判对象 —— 依据是逐字统计「卡尼曼／惠勒／贝佐斯／塔勒布在 A 段零次出现」。**新证据推翻它**：F 段所称「四大支柱」在本文档**逐条可查** —— ④「AI 时代即叙事工业化时代」= 本文档 **行 2100–2187**；②「文明即叙事机器」= **行 2188–2243**；③「元叙事与时间叙事」= **行 1648 / 1992**；①「时间之箭与因果律等同于叙事语法」= **行 1382 / 1395**。F 段「价值肯定」点名的「反脆弱叙事＋塔勒布」= **行 2065–2098**。名单四位亦各有落点（赫拉利 ≥8 处、卡尼曼 232、惠勒 1382、塔勒布 2067），**只剩贝佐斯全文 0 次**。**性质从「伪造被批判对象」修正为「张冠李戴」**（读到了同一 wiki 空间的关联文档，把它的属性安给了主文）。**后果**：候选类别「批判对象失真」**应撤回**，**不得写入 AGENTS.md**（幸而它当时只被记为「n=1 待裁定」，未进 schema —— 推翻它不需要改 schema）；[[critique-target-distortion]] 按 4.3 标 `status: stale`，**保留不删**，改为一次类别误判的记录。**本库同时记下一个教学点：那个「计数法」给出的原始事实全对，错的是从计数直接推到「幻觉」的那一步 —— 跳过了「被批判者引了谁」。这正是 4.2 第 6 条「说『库里没有 X』之前必须先检索」的现场验证，而那份文档的 doc-id 就写在第一讲 raw 的行 57 与行 83 里。**

**二、新类别候选：「来源等级冒认」。** 行 1333「**量子叙事学派**提出的『动态叙事本体论』」—— 本轮外部核查发现文本**真实存在**：MA, N. (2025). *The Essence of the Universe: Mathematical Laws as Narrative—An Ontological Hypothesis of the Quantum Narrative School*. **Zenodo**. doi:10.5281/zenodo.17520562；素材转述的术语（「以数学规律为内在叙事语法的高维动力系统」「迭代生成、拓扑约束、有序化」）与该摘要**逐条对得上**。**但它是 Zenodo 上的一篇单人预印本**（开放上传平台、无同行评议），素材称之为「**学派**」是**等级夸大**。与已有五类的区别：伪引注伪造**存在性**、弱引注放弃**精确性**，**本条冒认的是权威等级** —— 且它比伪引注更隐蔽，因为**一查就有**，核查者看到术语吻合会以为通过了。**待北洛裁定**：①单列一类，还是并入「引注的使用失真」（两者都属「核对对应关系而非存在性」）；②该预印本的二次传播文本自称由「人工及 AI（豆包、元宝、DeepSeek）分析整合」—— 可能是**「AI 生成 → 上传预印本 → 被 AI 引用」的闭环**，本库仅记录、不判断。

**三、引注核查 16 条：15 条可核为真，1 条冒认。** 最硬的一条是 **Alia Crum**：素材行 764「斯坦福大学心理学家阿利亚·克鲁姆的研究」**精确可核** —— Crum, Salovey & Achor (2013) *JPSP* **104(4):716-733**，SPARQ 复现研究（n=388）证实 stress-is-enhancing / debilitating 心态的生理差异，**素材描述方向一致**。其余可核为真：卡尼曼体验自我/记忆自我（232）、弗兰克尔（549）、张载横渠四句（287）、维特根斯坦《逻辑哲学论》5.6（1312）、海德格尔（1312）、马尔克斯《活着为了讲述》（1327）、鲁凯泽（1351）、惠勒 It from bit（1382）、赫拉利（≥8 处）、塔勒布 Antifragile（2067）；阿德勒那句出自《被讨厌的勇气》，是**日方作者的转述而非阿德勒原文**。**刘旸段（648–1000）判为弱引注**：新东方九年 ✅、浙大理工科 ✅、2018 上海国际喜剧大赛冠军 ✅、大年初三往返学表演 ✅ 均有多篇独立访谈可证，但**「月薪 150 元」「207 套高考题」「年均 170 本书」未找到独立来源** → 逐条标「（未核）」，**不整段降级**。曾国藩史实**本轮未核**。

**四、同源证据（本库第一次能做结构比对，而非措辞相似推断）。** 本文档 **D 段**（行 194–265）与第一讲 **E 段**（叙事身份理论那节）**同源**：五特征 vs 四特征，**多出的那一条恰是唯一带真实引用的**（卡尼曼）；核心句几乎逐字相同（行 63 vs E 段行 378）。**方向指向 D 段 → E 段**（压缩时先删了唯一有引用的那条）。**连带修正**：本文档**自己同时装着矛盾两方** —— 行 63 格言块是**构成论**（「我们是在『创作』人生」），行 230–237 同一文档的 AI 段是**批判论**（「『叙事自我』对『体验自我』的**暴政**……我们变成了自己人生的『观众』」）。**因此本库此前记为「第二处明确内部矛盾（跨素材）」不准确** —— 打架的不是两份素材，而是**同一套 AI 生成源内部本就没有调和**。已回填 [[narrative-identity]] 与 [[narrative-self-vs-bodily-self]]，**待北洛裁定**是否统一措辞为「同源内部矛盾」。

**新建 5 页**：sources 1（[[2026-09-18-narrative-self]]）＋ 概念 3（[[meta-narrative]] —— 元叙事四因，行 1648–1709，是本页「叙事决定目标函数」的机制化展开；[[narrative-reframing]] —— 叙事重构五步法，与 [[cognitive-reappraisal]] **同族不同层**；[[narrative-industrialization]] —— **F 段批判的真实落点**）＋ 实体 1（[[yuval-harari]] —— 建页依据：库内 ≥2 份素材，且在本档 T 段是论证主体，**补的是与塔勒布同型的一笔欠账**）。**不建页 6 位，按 3.2 阈值判定**：**丹·麦克亚当斯**（仅行 194 一次，**但他是 [[narrative-identity]] 长期开放问题点名要的人，本库第一次拿到这个可追人名** —— 已记入该页开放问题，**第二次出现即建页**）、阿利亚·克鲁姆（引注质量最高但仅一次）、卡尼曼（行 232 一句）、惠勒（1382）、刘旸、阿德勒。

**回填 12 处**：第一讲 sources 页（**关闭待办 + 核查表第 8／9 条加修正 + 「待北洛裁定」块标为已无需裁定 + 派生页节加 4 页说明**）、[[critique-target-distortion]]（**整页重写为修正版，标 stale**）、[[narrative-identity]]（同源证据块 + 矛盾措辞修正块 + 开放问题补 McAdams 线索）、[[narrative-self-vs-bodily-self]]（新增与 [[narrative-reframing]] 的关系 —— **本库第三处「同一主题两个方向」，且它比前两处更锋利：问的不是「叙事是什么」而是「什么时候可以用它」**）、[[modern-thinking-tools]]（知识节 + 决策记录 2 条 + 缺口表新增「贝佐斯为何在名单里」一行 + 相关页面）、[[narrative-as-first-principle]]、[[narrative-power]]、[[narrative-as-objective-function]]、[[cybernetic-learning]]（**第六例，但补的是链条上游：目标从哪来**）、[[cognitive-reappraisal]]、[[viktor-frankl]]（第四次出现，引注已核）、[[wanweigang]]（说明本档是关联档案、非课程文章、不计入讲次）。

**lint 0 项机器可查问题**，页面 204（内容页 200 + 系统页 4），链接 2,624。语义提示仅 1 条（`shane-parrish` 未被任何项目引用，**本轮之前即存在**）。

**站点构建判断（按 4.1.1 逐条）**：①新增主线？否（叙事线已有）。②新增/关闭项目？否。③页面总数变化超 10？否（199 → 204，**+5**）。④一次大 ingest 收尾？**否** —— 非整系列、非多份同批、**派生新页 4 个（不含 sources 页），未达 ≥5 门槛**。⑤人类明确要求？否。**五条均不命中 → 明确地不构建。** 站点仍停在 **199 页版本**，当前落后 **5 个页面**；此判断记录在此，供日后核对（按 4.1.1，「明确地不构建」与「忘了构建」结果相同、过程不同 —— 前者可审计）。
## [2026-09-18] edit | 北洛裁定：主线四的项目由板块级升格为课程级 —— basic-worldview → modern-thinking-tools

【裁定内容】原 title「基本世界观（万维钢《现代思维工具》六讲）」与 slug basic-worldview 一并废弃，改为 title「现代思维工具（万维钢 · 得到课程）」、slug modern-thinking-tools，文件名同改。goal 的验收对象从「六讲」扩为「已收板块 + 一张覆盖全课的地图」，新增验收判据第 6 条（全课地图覆盖官方大纲列出的全部区块）。评审判据第 1–5 条内容不变。

【顺带关闭两个长期挂着的结构性问题】① 发刊词（讲次 00）归属的「甲 / 乙 / 丙」三方案 —— 落地为原【乙】方案：课程级总纲归课程级项目；②「同一门课的素材被两个项目分掉」—— 不合并、改为显式登记，记号落在新增的「全课地图」一节。

【关键取舍：不迁移「教育与学习」九讲】九讲仍归 peak-performance，本项目只做登记。理由：迁移会掏空 peak-performance 的 goal（学习机制是它的核心，不是附属），而登记已把「这门课收齐了吗」的信息成本消解掉。已在 peak-performance 的「学习力簇」节补一句反向指针，使两个方向都可答。

【边界声明：课程级 ≠ 收录承诺】官方大纲的八个模块一律不进缺口表，只在线图里记状态。理由：shipped 的判据正是缺口表清空，把未收模块记成缺口等于让项目不可完成。该区分写进项目页首警示块与「不做什么」一节。

【执行范围】全库 116 处 slug 引用 / 45 个文件同步替换。其中 log.md 的历史条目也一并替换 —— 因为 lint 会检查 log.md 内的 wikilink，不改会立刻产生 13 条断链；该改动本身记在此条，作为可审计留痕（依 AGENTS.md 1.1 例外条款「不得覆盖、只能追加、改动必须留痕」的精神）。index.md 已重建（200 页）。新增「全课地图」节含 11 行区块登记，结构基准来自发刊词 sources 页记录的外部官方大纲。

【未做的两件事】① 官方大纲仍未收录进 raw/ —— 升格后其价值上升（现在是全课地图的结构基准），待裁定；② 「教育与学习」九讲与「基本世界观」六讲之间的方向性张力仍未裁决，且升格后它同时成为「同一门课两个板块」的证据。

lint 复跑 0 项机器可查问题，页面 204（内容页 200 + 系统页 4），链接 2,648。

## [2026-09-18] edit | 站点构建（按 AGENTS.md 4.1.1 逐条判断）。五条判据命中第 2 条「新增或关闭一个项目」——严格说项目数未变（5 → 5），但项目本身发生了 slug 与管辖层级的变更，属「入口层变了」；且另有一个更硬的理由：site/index.html 是构建产物，不重建则站内全部指向该项目的链接都指向一个已不存在的 slug（这是内容已错误，不只是滞后）。其余四条均不命中（无新增主线 / 页面数 204 → 204 未超 10 / 非大 ingest 收尾 / 人类未明确要求）。构建后 204 个页面 / 2,648 条链接，文件 1.91 MB → 2.0 MB。上一次构建停在 199 页版本（2026-09-18 约 19:0x），此后跨越两次改动：① 《叙事自我》ingest（+5 页，19:3x，当时按表逐条判断后明确地不构建）；② 本次项目升格（净增 0 页，但有 116 处引用变更）。构建后校验：旧 slug 在站内只剩文字说明（叙述与日志，非链接），无失效链接；新 slug 出现 279 次。

## [2026-09-18] query | 用户提问「反刍与反思的区分、边界及行动策略」—— 命中 emotion-awareness 缺口表第一条【阻塞】。检索四家外部文献（Trapnell 1999 / Treynor 等 2003 / Watkins 2008 / Kross 等）后归档为 analyses/rumination-vs-reflection.md。结论：分界线是三条判据（触发源 / 加工模式 / 立场），不是一条线。该页 sources 留空 —— 按 AGENTS.md 第 7 节「结论来自未收录来源时须显式标注缺口」处理

## [2026-09-18] edit | 回填与修正三页：① rumination.md —— 定义特征「回放性」降为常见形态（反刍的核心是被动、评价、去语境，不是向后看），Storoni 那条材料更换降级理由但保留结论；② emotion-awareness.md —— 缺口表关闭第一条【阻塞】、另记其派生的「补录文献素材」缺口（原缺口关闭但留尾巴，故另记一行）；③ cognitive-reappraisal.md —— 新增缺口：该页只覆盖「改内容」，未覆盖 Watkins 的「改过程」

## [2026-09-18] lint | 本轮 1 项机器可查问题：analyses/rumination-vs-reflection.md 未标注来源。**预期内** —— AGENTS.md 第 7 节允许「sources 留空并显式标注缺口」，该页已按此处理并在「来源与证据性质」一节逐节点列出。此提示的功能恰好是提醒补录文献

## [2026-09-18] ingest | 收录 Nolen-Hoeksema, Wisco & Lyubomirsky (2008) Rethinking Rumination（Perspectives on Psychological Science 3(5): 400-424）。25 页 / 156,776 字符 / 2,837 行（frontmatter 占 48 行）。源为作者自存版（drsonja.net），PDF 原件存 raw/assets/。本库第二份一手学术文献，也是第一份「理论提出者对自己理论的复核」——含对原始预测的自我修正。**首次由 LLM 直接写入 raw/**（人类明确指示收录，等同「人给链接、LLM 开工」的授权）。派生 wiki/sources/ 页与 entities/nolen-hoeksema、entities/ed-watkins 两页

## [2026-09-18] edit | 据新素材回填与修正五处：① analyses/rumination-vs-reflection.md 重写 —— 撤回「时间方向无效」的结论（该结论把「反刍 vs 担忧」的判据误当作「反刍 vs 反思」的判据来检验），新增 TABLE 1 四条对照与自我调节理论的「终止性」判据，sources 由空补上；② concepts/rumination.md 回滚「回放性」定义（v1 的推翻属误伤）；③ projects/emotion-awareness.md 关闭「补录文献」缺口并登记新缺口；④ concepts/cognitive-reappraisal.md 升级「改内容 vs 改过程」张力；⑤ analyses/cognitive-vs-somatic-paths.md 补第一条实验依据（8 分钟分心）。**新立补救规则**：sources 留空的页面，正文不得使用「某文献说 / 原文为」句式，只能写「据检索印象（未核实）」

## [2026-09-18] ingest | 《02_成长战略》（万维钢《现代思维工具》模块一）：20 份素材 + 28 个派生页；19 讲（15 正文 007–021 + 3 问答 + 1 收官直播）+ 2 份关联档案

## [2026-09-18] edit | 站点构建（按 AGENTS.md 4.1.1 逐条判断）。**五条命中三条**：①**新增一条主线** —— 「模块一 成长战略」是本项目第二条主线，「这个库在讲什么」变了；③**页面总数变化超 10**（204 → 256，**+52**）；④**一次大 ingest 收尾** —— 20 份素材同批收录、且单批派生 28 个新页（16 概念 + 12 实体），远超「≥5」门槛。**上一次构建停在 204 页版本（2026-09-18 约 21:08，文件 2.03 MB）**，此后跨越四次改动：① rumination 查询与归档（+1 分析页）；② Nolen-Hoeksema (2008) ingest（+3 页）；③ 据该素材回填与修正五处；④ 本次《02_成长战略》ingest（+52 页，含 20 sources + 28 派生页 + 20 raw）。重建后 **256 个页面 / 3,327 条链接**，文件 2.03 MB → 2.92 MB。

