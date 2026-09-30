---
title: "A Taxonomy of External and Internal Attention（外部注意与内部注意：一个按「注意力的对象」划分的分类）"
author: Marvin M. Chun、Julie D. Golomb、Nicholas B. Turk-Browne（三人署名完整；耶鲁大学心理学系与神经生物学系 / MIT McGovern 脑研究所 / 普林斯顿大学心理学系）
url: https://www.annualreviews.org/content/journals/10.1146/annurev.psych.093008.100427
kind: paper
series: 无
published: 2011（Annual Review of Psychology, 62:73–101；DOI 10.1146/annurev.psych.093008.100427；PDF 版式日期 2010-11-22）
clipped: 2026-09-29
capture_quality: high
capture_method: >
  2026-09-29 从作者公开镜像抓取 PDF（http://www.iapsych.com/articles/chun2011.pdf，
  513,787 字节 / 33 页，PDF 自带文本层，未做 OCR）。
  **非出版方直连** —— 出版方 Annual Reviews 为付费墙；该镜像用的是刊物最终版式
  （页眉带 Annu. Rev. Psychol. 2011.62:73-101、页脚带 University of Minnesota 的下载水印），
  但**不能据此断言与印刷版逐字一致**。

  用 pypdf 6.19.0 逐页提取转文本 —— 33 页 / 2467 行 / 126,603 字符，每页以 [p.N] 分隔。
  N 为 **PDF 页码**，不是期刊印刷页码（PDF 第 1 页 = 印刷第 73 页，二者差 72）。
  **PDF 原件未改动**，落盘为 raw/assets/2026-09-29-attention-taxonomy-chun2011.pdf。

  已知缺失（五条）——
  1. **硬换行未重组。** 保留印刷版视觉换行，一个句子常跨 2–3 行，关键词检索会漏。
     与库内既有 PDF 素材（dunlosky、choice-overload-meta-analysis）做法一致。
  2. **连字（ligature）未还原。** fi / fl 保留为 ﬁ / ﬂ 单字符（signiﬁcant、ﬁnding、inﬂuence）。
     检索时须用连字形式，或改用不含连字的片段（搜 `signif` 而非 `significant`）。
  3. **双栏排版。** 跨栏段落与脚注的先后关系需回 PDF 复核；引用长段落前核对 [p.N] 边界。
  4. **图未结构化保留，且本份的核心图是图。** Figure 1（外部/内部注意的分类示意图）只有图注文字，
     图内分栏与连线不在文本层 —— **引用该分类的图形结构前必须回 PDF 或回正文文字描述**。
  5. **页眉 / 页脚 / 下载水印逐页重复混入正文流**
     （`www.annualreviews.org • A Taxonomy of Attention 75`、`Annu. Rev. Psychol. 2011.62:73-101. Downloaded from ...`），
     检索噪声较大。第 20–29 页为参考文献、第 31–33 页为刊物征订页，均非论文正文。
capture_note: >
  **本字段只记「抓取事实」，不记「阅读结论」。**
  本素材的分层、关键要点、与库内已有主张的比对结果一律维护在
  wiki/sources/2026-09-29-attention-taxonomy-chun2011.md —— 它们随阅读深入而变，
  而本文件不可变，写在这里必然产生死结。**本文件不维护任何行区间。**

  行区间坐标系为**文件绝对行号**（`wc -l` 的坐标系）。正文行号 = 文件行号 − frontmatter 行数。
  引用前回文件核对。

  **素材性质**：同行评议期刊的综述专论（Annual Review of Psychology），三作者署名完整，
  **无转述层、无 AI 加工痕迹**。这是本库**第一份以「注意力」为主题的原始研究文献** ——
  此前该主题在库内只有通俗转述（见 [[attention]] 与 [[attention-what-it-is-and-how-to-improve]] 记录的五条进路）。
  按 kind 取值表记为 `paper`。

  **利益披露**：原文设有 DISCLOSURE STATEMENT，作者自陈无可能影响本综述客观性的
  隶属关系、会员资格、资助或财务持有。**这是作者自陈，本库未做独立核实。**

  **版权性质**：Annual Reviews 出版。本文件与 PDF 原件均以个人研究用途存档于本地 raw/，不对外发布。
---
[p.1]
PS62CH04-Chun ARI 22 November 2010 9:23
A Taxonomy of External
and Internal Attention
Marvin M. Chun,1 Julie D. Golomb,2
and Nicholas B. Turk-Browne3
1Departments of Psychology and Neurobiology, Yale University, New Haven,
Connecticut 06520; email: marvin.chun@yale.edu
2McGovern Institute for Brain Research, Massachusetts Institute of Technology,
Cambridge, Massachusetts 02139
3Department of Psychology, Princeton University, Princeton, New Jersey 08540
Annu. Rev. Psychol. 2011. 62:73–101
The Annual Review of Psychology is online at
psych.annualreviews.org
This article’s doi:
10.1146/annurev.psych.093008.100427
Copyright c© 2011 by Annual Reviews.
All rights reserved
0066-4308/11/0110-0073$20.00
Key Words
perception, cognitive control, memory, selection, consciousness
Abstract
Attention is a core property of all perceptual and cognitive operations.
Given limited capacity to process competing options, attentional mech-
anisms select, modulate, and sustain focus on information most relevant
for behavior. A signiﬁcant problem, however, is that attention is so ubiq-
uitous that it is unwieldy to study. We propose a taxonomy based on the
types of information that attention operates over—the targets of atten-
tion. At the broadest level, the taxonomy distinguishes between external
attention and internal attention. External attention refers to the selec-
tion and modulation of sensory information. External attention selects
locations in space, points in time, or modality-speciﬁc input. Such per-
ceptual attention can also select features deﬁned across any of these
dimensions, or object representations that integrate over space, time,
and modality. Internal attention refers to the selection, modulation, and
maintenance of internally generated information, such as task rules, re-
sponses, long-term memory, or working memory. Working memory,
in particular, lies closest to the intersection between external and in-
ternal attention. The taxonomy provides an organizing framework that
recasts classic debates, raises new issues, and frames understanding of
neural mechanisms.
73
Annu. Rev. Psychol. 2011.62:73-101. Downloaded from www.annualreviews.org
by University of Minnesota - Twin Cities - Wilson Library on 05/13/11. For personal use only.

[p.2]
PS62CH04-Chun ARI 22 November 2010 9:23
Contents
I N T R O D U C T I O N.................. 7 4
BASIC CHARACTERISTICS
AND FUNCTIONS OF
A T T E N T I O N.................... 7 5
L i m i t e dC a p a c i t y.................. 7 5
S e l e c t i o n.......................... 7 5
Modulation . . . . . . . . . . . . . . . . . . . . . . . . 75
Vigilance . . . . . . . . . . . . . . . . . . . . . . . . . . 76
AGAINST A UNITARY MODEL
O FA T T E N T I O N................ 7 6
A TAXONOMY OF EXTERNAL
AND INTERNAL
A T T E N T I O N.................... 7 6
E x t e r n a lA t t e n t i o n................. 7 8
I n t e r n a lA t t e n t i o n.................. 8 2
ISSUES AND FUTURE
D I R E C T I O N S.................... 8 6
Early Versus Late Selection:
Lavie’s Load Theory . . . . . . . . . . . . 86
V i s u a lS e a r c h...................... 8 7
Object Tracking and
Perceptual Stability . . . . . . . . . . . . . 88
Attention and Awareness . . . . . . . . . . . 88
Prospective Activity: Decoding
and Predicting Attentional States 89
Enhancing Attention With Emotion,
Reward, or Training . . . . . . . . . . . . 89
TOWARD A TAXONOMY
O FA T T E N T I O N................ 9 0
INTRODUCTION
William James famously declared that “Every-
one knows what attention is,” but paradoxically,
such colloquial understanding has impeded the
scientiﬁc study of attention. Case in point: the
extraordinary power and breadth of electronic
databases have now rendered “attention” use-
less as a term for reference searches. Try typing
“attention” into your favorite literature search
engine, such as PubMed, Web of Science, or
Scopus, and you will get hits in the hundreds
of thousands, signiﬁcantly more than other
general terms such as “memory.” Or imagine
yourself as an attendee in a scientiﬁc conference
wanting to learn what’s hot in attention re-
search. How should you plan your week when
“attention” yields hundreds of presentations
and dozens of sessions? How can you meaning-
fully categorize hundreds of abstracts that claim
“attention” as the primary keyword? Ironically,
scientists can’t use the term “attention” to
“select” relevant studies of interest.
The practical problem above happily reﬂects
breathtaking progress in attention research.
The concept of attention has now permeated
most aspects of perception and cognition re-
search. Growing consensus indicates that selec-
tion mechanisms operate throughout the brain
and are involved in almost every stage from sen-
sory processing to decision-making and con-
sciousness. Attention has become a catch-all
term for how the brain controls its own infor-
mation processing, and its effects can be mea-
sured through conscious introspection, overt
and implicit behaviors, electrophysiology, and
brain imaging.
Attention was not always such a widely
used concept. The modern birth of attention
research during the cognitive revolution grap-
pled with speciﬁc questions: Does selection
occur before perception or after semantic
identiﬁcation? What happens to unselected in-
formation? These questions continue to guide
much research, but they now apply to almost all
cognitive operations beyond perception. Infor-
mation processing is modulated by task goals
across all stages of sensation, object recogni-
tion, memory, emotions, and decision-making.
We should therefore abandon the view of
attention as a unitary construct or mechanism,
and consider attention as a characteristic and
property of multiple perceptual and cognitive
control mechanisms. And if ubiquitous, then
it becomes important to understand what’s
common and what’s different about these
multiple forms of attention.
When a group of related concepts and ideas
becomes unwieldy, a taxonomy proves use-
ful. Organizing and categorizing large col-
lections of ﬁndings brings clarity and under-
standing. The most famous Linnaean taxonomy
74 Chun · Golomb ·Turk-Browne
Annu. Rev. Psychol. 2011.62:73-101. Downloaded from www.annualreviews.org
by University of Minnesota - Twin Cities - Wilson Library on 05/13/11. For personal use only.

[p.3]
PS62CH04-Chun ARI 22 November 2010 9:23
has advanced our understanding of the natural
world, and these initial classiﬁcations based on
superﬁcial characteristics set the stage for a
deeper understanding of natural taxonomies
based on evolution and genetics. Within psy-
chology, memory research has long beneﬁtted
from a taxonomy of memory systems, divided
according to memory content or whether mem-
ory is consciously accessible or not ( Johnson
1983, Schacter & Tulving 1994, Squire et al.
1993).
Similarly, a global taxonomy of attention
can advance our understanding and stimulate
further research. This review aims for a
big-picture synthesis, by necessity, focusing
on global issues and features at the expense
of detail, pointing the readers to relevant
specialized reviews where possible. The value
of this taxonomy will not lie on whether it is
correct in its proposed form, but rather as a
starting point to sketch a big-picture frame-
work and to develop common language and
concepts. At a minimum, the taxonomy serves
as a portal for the attention literature, and at
its best, it can stimulate new research and more
integrative theories. The review begins with
core properties, followed by the taxonomy. We
close with a discussion of recent progress on
classic and future issues in attention research.
BASIC CHARACTERISTICS AND
FUNCTIONS OF ATTENTION
Limited Capacity
Attention is necessary because at any given
moment the environment presents far more
perceptual information than can be effectively
processed, one’s memory contains more
competing traces than can be recalled, and the
available choices, tasks, or motor responses are
far greater than one can handle. This constraint
of limited capacity applies to all nodes of our
taxonomy. Attentional mechanisms evolved
out of necessity to efﬁciently focus limited
processing capacity on the most important
information relevant to ongoing goals and
behaviors (Pashler et al. 2001).
Selection
Limited processing capacity dictates a need for
selection, and a primary goal of attention re-
search is to understand which information is
selected, how it is selected, and what happens to
both selected and unselected information. Se-
lection is a core function of all forms of atten-
tion considered in this review. Multiple stimuli
or options compete for selection, and the goal
of attention is to bias competition in favor of
a target object or expected event (Desimone &
Duncan 1995). For example, in vision, acuity is
limited to the fovea requiring eye movements
to targets of interest. In hearing, auditory en-
vironments typically present many competing
sounds, and one must select what’s most rele-
vant, such as a conversation with a friend at a
cocktail party. High-level cognitive operations
require selection also. Choosing between alter-
natives in decision-making represents a form of
selection. Selecting a memory from competing
memories should be viewed as an attentional
operation. The cost is that unattended infor-
mation may be missed, whether it is a gorilla
in a video (Simons & Chabris 1999), a trafﬁc
light while chatting on a cell phone during driv-
ing (Strayer & Johnston 2001), a boarding an-
nouncement at the airport while talking with a
friend (Cherry 1953), or the name of an old ac-
quaintance you chance to meet—only for it to
pop into your mind after you part (for a review
on memory failures, see Schacter 2001).
Modulation
Once a target object, event, or representation
is selected from competing options, attention
determines how well the target information is
processed, how fast and accurate a task and re-
sponse are executed, and whether the event will
be later remembered. Attention facilitates sen-
sory processing throughout cortex, even chang-
ing the qualia of how attended objects are per-
ceived (Carrasco et al. 2004). The distinction
between selection and modulation is that se-
lection entails that there are other competing
items. Modulation refers to what happens to
www.annualreviews.org • A Taxonomy of Attention 75
Annu. Rev. Psychol. 2011.62:73-101. Downloaded from www.annualreviews.org
by University of Minnesota - Twin Cities - Wilson Library on 05/13/11. For personal use only.

[p.4]
PS62CH04-Chun ARI 22 November 2010 9:23
the selected item, such that attention inﬂuences
the processing of items in the absence of overt
competition. Another way to think of this dis-
tinction is in terms of facilitation: As opposed
to modulation, selection alone does not en-
sure better behavioral performance or memory
(Levin & Simons 1997).
Vigilance
Vigilance is related to the modulatory effects
of attention. Here, we deﬁne modulation as the
current, immediate effects of attention on pro-
cessing, whereas vigilance refers to the ability
to sustain this attention over extended periods
of time. Perceptual and cognitive mechanisms
do not always operate at peak levels, but their
activation levels and efﬁciency ebb and ﬂow
(Berridge & Waterhouse 2003). If so, then one
should be able to use noninvasive methods such
as functional neuroimaging to measure the neu-
ral activity during the moments even before a
stimulus is presented (Kastner et al. 1999). Re-
markably, brain activity and mental state before
a trial commences can be predictive of many as-
pects of behavior, including how well subjects
remember a stimulus (Otten et al. 2002, Turk-
Browne et al. 2006) and prepare for or perform
a task (Leber et al. 2008, Weissman et al. 2006).
The ability to sustain attention and focus over
time is essential for practical domains such as
tumor detection in mammography or baggage
screening for airplanes (Wolfe et al. 2005), as
well as for daily functioning in work, school, and
social settings. Indeed, understanding how at-
tention is sustained can inform our understand-
ing of clinical disorders such as attention deﬁcit
disorder (Biederman & Faraone 2005).
AGAINST A UNITARY MODEL
OF ATTENTION
Is there a single mechanism that governs both
visual search and selective listening? Is the se-
lection of sensory inputs the same as selecting
which item to recall from memory or which
choice to make when confronted with multiple
alternatives? A strong conclusion of this review
is that the answer is a resounding no.
Attention is not unitary. Rather, attention
should be considered as a property of multiple,
different perceptual and cognitive operations
(Lavie et al. 2004, Parasuraman 1998, Pashler
1998). Hence, to the extent that these mecha-
nisms are specialized and decentralized, atten-
tion mirrors this organization. These mecha-
nisms are in extensive communication with each
other, and executive control processes help set
priorities for the system overall. However, such
priority setting is still independent of the ac-
tual nuts and bolts of selection and modulation
within the multiple mechanisms.
Evidence against unitary models of attention
comes from behavioral studies and from cog-
nitive neuroscience methods, including brain
imaging and neuropsychology that reveal some
degree of modularity in the brain. Clever tasks
and manipulations have enabled researchers to
carve out and map an architecture for percep-
tual and cognitive processing. Patterns of in-
terference or lack of interference between tasks
help to reveal which processes share capacity
and which do not.
A TAXONOMY OF EXTERNAL
AND INTERNAL ATTENTION
We propose that the core characteristics of at-
tention are shared across multiple systems: the
problem, that there is too much information to
process; the solution, to select and modulate in-
formation most relevant for behavior; and the
challenge, to sustain vigilance. Given these gen-
eral properties of all varieties of attention, our
goal here is to organize them into a taxonomy.
We categorize attention according to the
types of information that attention operates
over—the targets of attention. From this
perspective, it becomes immediately apparent
that there is a distinction between selecting
information coming in through the senses and
information that is already represented in the
mind, recalled from long-term memory or be-
ing maintained in working memory. Sitting at
your desk, you can focus on the information on
76 Chun · Golomb ·Turk-Browne
Annu. Rev. Psychol. 2011.62:73-101. Downloaded from www.annualreviews.org
by University of Minnesota - Twin Cities - Wilson Library on 05/13/11. For personal use only.

[p.5]
PS62CH04-Chun ARI 22 November 2010 9:23
the computer screen, a conversation in the hall-
way, or the taste of the stale coffee brew in your
cup. These examples of external attention can
be distinguished from how you could instead
be focusing your attention on your thoughts,
contemplating a talk you just heard, trying to
remember the author of a paper you want to ﬁnd
and cite, or trying to decide where to go to
lunch, all while staring at your computer screen
with conversations going on in the hallway.
Thus, our taxonomy makes a primary dis-
tinction between external attention and inter-
nal attention. External attention refers to the
selection and modulation of sensory informa-
tion, as it initially comes into the mind, gener-
ally in a modality-speciﬁc representation and
often with episodic tags for spatial locations
and points in time. This sensory information
can be organized by features or into objects,
which can themselves be targets of external
attention. Another way to think of external at-
tention is as perceptual attention. Internal at-
tention refers to the selection and modulation
of internally generated information, such as
the contents of working memory, long-term
memory, task sets, or response selection. In-
ternal attention includes cognitive control and
can also been referred to as central or reﬂec-
tive attention ( Johnson 1983, Miller & Cohen
2001).
This distinction is present in the expanded
William James quote, “Everyone knows what
attention is. It is the taking possession by the
mind, in clear and vivid form, of one out of what
seem several simultaneously possible objects or
trains of thought. Focalization, concentration,
of consciousness are of its essence.” William
James eloquently distinguishes the possession
of the mind by “objects,” which we interpret
as external attention, or “trains of thought,”
what we call internal attention. As empirical
support, increasing the load of perceptual in-
put has different effects than increasing the load
of working memory (Lavie et al. 2004). Per-
ceptual processing proceeds independent of de-
mands on working memory, response selection,
or task switching (Pashler 1994). More exam-
ples are reviewed below. Of course, the bound-
ary between perception and central cognition
is blurry, but this distinction is the most useful
and natural one.
We are certainly not the ﬁrst to distinguish
among different types of attention. Other
classiﬁcations are prominent and are discussed
here. Attention facilitates target processing
while inhibiting distraction and noise. Exoge-
nous, bottom-up, stimulus-driven attention
is distinct from endogenous, top-down,
goal-directed attentional control. Sustained at-
tention operates over a longer time course than
transient attention. Attention can move overtly
together with eye movements or covertly with
eyes ﬁxating. These distinctions are real and
useful—and hold places in our taxonomy—but
individually do not provide a broad organizing
principle as the external/internal axis we pursue
here. A main difference is that these previous
distinctions focus on differentiating speciﬁc
mechanisms or properties of attention—our
taxonomy is based on the targets of attention,
encompassing all of its mechanisms and
properties.
Figure 1 provides a schematic overview. Ex-
ternal and internal attention are on opposite
ends of an axis. Each box within this space rep-
resents a target of attention—a class of informa-
tion over which specialized selective and mod-
ulatory processes operate. Despite the implied
modularity, the axis should be viewed as con-
tinuous, and the boxes are massively interactive,
especially those depicted in the same or adjacent
levels. Along an orthogonal dimension, goal-
directed (top-down, endogenous) attention and
stimulus-driven (bottom-up, exogenous) atten-
tion characterize how different levels interact
(Egeth & Yantis 1997). For reasons explained
below, goal-directed attention can target any of
the levels in the taxonomy, whereas stimulus-
driven attention is by deﬁnition a property of
external attention.
The remainder of this review builds up this
taxonomy with inﬂuential studies in the atten-
tion literature. An important caveat is that when
studies appear in a different grouping or part
of the taxonomy below, it doesn’t mean that
the mechanisms involved are necessarily unique
www.annualreviews.org • A Taxonomy of Attention 77
Annu. Rev. Psychol. 2011.62:73-101. Downloaded from www.annualreviews.org
by University of Minnesota - Twin Cities - Wilson Library on 05/13/11. For personal use only.

[p.6]
PS62CH04-Chun ARI 22 November 2010 9:23
and separate. The taxonomy simply reﬂects the
fact that relevant studies can be grouped around
a certain set of issues and questions, such that
paper citations would be clustered. The goal is
not to strictly segregate the different topics of
attention, but rather to organize them better
so that connections between areas of study will
become more clear.
External Attention
External attention to the perceptual world can
be subdivided according to the focus of atten-
tion. First, attention can be directed to one or
several modalities, separable from each other
during initial neural processing. Second, in-
dependent of modality, attention is deployed
over space and over time, with separate issues
to consider for spatial versus temporal atten-
tion. In addition, attention can be allocated over
space, time, and modality according to stim-
ulus features or how they are organized into
objects. These dimensions are not exclusive of
each other, but they represent useful ways to
organize the mechanisms of attention, and they
represent lines along which studies have been
conducted.
Modality. Sensory processing is initially sep-
arate for the ﬁve modalities of vision, hearing,
touch, smell, and taste. Attention serves to
select and modulate processing within each of
the ﬁve modalities, and it directly impacts pro-
cessing within relevant sensory cortical regions.
Although the bulk of research reviewed and
categorized in this taxonomy stems from the
visual attention literature, these ﬁndings gener-
alize well to the other modalities. For example,
attention to visual stimuli enhances discrimina-
tion and activates relevant topographic areas in
retinotopic visual cortex (Tootell et al. 1998),
allowing observers to detect stimuli at lower
contrast or to make ﬁner discrimination. Atten-
tion to sounds enhances processing in auditory
cortex (Woldorff et al. 1993), allowing listeners
to detect fainter sounds or to discriminate ﬁner
pitch differences. Similar effects of attention
operate in somatosensory cortex, olfactory
cortex, and gustatory cortex ( Johansen-Berg
& Lloyd 2000, Veldhuizen et al. 2007, Wager
et al. 2004, Zelano et al. 2005).
One goal of research is to clarify how
independent these systems are and how they
interact. These different systems appear to
operate separately with independent capacity—
an inference that can be made by showing
that multiple signals coming from the same
modality interfere more with each other than
do signals coming in from across different
modalities (Arnell & Jolicoeur 1999, Duncan
et al. 1997, Potter et al. 1998). Interference
between modalities appears to occur at a more
central stage of processing.
Indeed, inputs from the different modalities
must converge at some stage to provide a coher-
ent representation of the environment (Driver
& Spence 1998). For example, based on a spa-
tial representation of the environment, infor-
mation from different modalities is linked ac-
cording to the locations and objects in which
the information arises in external space. Spatial
attention to a location enhances discrimination
responses across multiple modalities. For ex-
ample, sudden touches not only draw tactile at-
tention, but also visual and auditory attention
toward them. Redundant signals from different
modalities can enhance each other (Spence et al.
1998). Attention serves to bind simultaneously
presented signals across space into multisensory
objects (Busse et al. 2005).
Neural investigations are useful for under-
standing external attention to modality. When
a touch on the hand improves vision near that
hand, where do different modality signals con-
verge and how does attention cross modalities?
In the case of tactile enhancement of vision,
multimodal parietal areas appear to project at-
tentional signals to enhance unimodal visual
cortex (Macaluso et al. 2000). Brain mecha-
nisms such as the left superior temporal sul-
cus are sensitive to when audio-visual inputs
are matched versus when they’re discordant
(Calvert et al. 2000). Future work should con-
tinue to clarify how information from differ-
ent modalities can be integrated (Ghazanfar &
Schroeder 2006).
78 Chun · Golomb ·Turk-Browne
Annu. Rev. Psychol. 2011.62:73-101. Downloaded from www.annualreviews.org
by University of Minnesota - Twin Cities - Wilson Library on 05/13/11. For personal use only.

[p.7]
PS62CH04-Chun ARI 22 November 2010 9:23
Spatial attention. Spatial attention concerns
how to prioritize spatial locations in the envi-
ronment, and it is a prime example of the limited
capacity problem. Spatial attention is central to
vision, especially to deploy foveal acuity (eye
movements) to prioritized locations, and hence,
most of the work reviewed below involves visual
tasks. But as noted above, principles of spatial
attention generally apply to other modalities as
well.
Spatial attention is often compared to a
“spotlight” (Cave & Bichot 1999), an analogy
that by deﬁnition implies a single, limited locus,
although attention can be split across multiple
locations (Awh & Pashler 2000, McMains &
Somers 2004; c.f. Jans et al. 2010) or spread
across space with reduced effectiveness (Eriksen
& St James 1986). In vision, spatial attention
mechanisms evolved to guide and control eye
movements (Rayner 2009, Schall & Thompson
1999), so attention and eye movements are
tightly interlinked (Deubel & Schneider 1996,
Hoffman & Subramaniam 1995, Kowler et al.
1995). Spatial orienting and saccadic control
employ overlapping neural systems (Corbetta
et al. 1998). However, eye movements and
attention are dissociable (Hunt & Kingstone
2003, Juan et al. 2004). That is, spatial attention
can be overt, linked with the guidance of eye
movements, or covert, in that a location can be
attended without being foveated.
Both overt and covert spatial attention can
be modulated by exogenous and endogenous
cues (Corbetta & Shulman 2002, Egeth &
Yantis 1997). Posner et al. (1980) popularized
the distinction between exogenous cuing and
endogenous cuing. Exogenous, bottom-up,
stimulus-driven cuing draws attention to a
location by a cue, such as a ﬂashed stimulus,
appearing in the same location as the target.
Endogenous, top-down, goal-directed cuing
directs attention to a location with a symbolic
cue that instructs where to attend, using arrows
or left/right word cues that do not appear in the
same location as the target to attend (Hommel
et al. 2001). The distinction between exogenous
and endogenous attention is especially impor-
tant for understanding attentional deployment
when there are multiple objects and events in
the visual ﬁeld. When attention is focused on
a certain location, what are the mechanisms
involved in shifting attention to a new location
or a new object? Attention may be voluntarily
moved to a different location in a goal-directed
manner. Or attention may be “captured” by an
object or event occurring in a different, unat-
tended location in a stimulus-driven manner.
Goal-directed and stimulus-driven atten-
tion have different neural mechanisms, and it is
useful to study their interactions and the relative
timing of activity. Prefrontal neurons reveal tar-
get location processing ﬁrst during top-down
attention, whereas parietal areas are active ear-
lier, during bottom-up attention (Corbetta et al.
2008). When oscillatory frequencies are mea-
sured, there is stronger synchrony between
frontal and parietal areas in lower frequen-
cies for top-down attention and in higher fre-
quencies for bottom-up attention (Buschman
& Miller 2007). Spatial attention increases the
synchrony between posterior parietal cortex
and the medial temporal area (Saalmann et al.
2007), and direct microstimulation of frontal
eye ﬁelds enhances processing of sensory in-
put in extrastriate cortex, suggesting that top-
down modulation plays a causal role (Moore &
Armstrong 2003).
Spatial attention facilitates processing at
attended locations and inhibits neighboring
locations and items. Cuing improves target
detection and discrimination (Corbetta &
Shulman 2002, Yantis et al. 2002), and the time
course of facilitation reveals two modes of at-
tention. Attentional facilitation is greatest when
the cue precedes the target array by 70–150 ms,
and this transient attentional effect is largely
involuntary, beneﬁts the simplest of tasks, and
diminishes with increasing delay (Nakayama
& Mackeben 1989, Weichselgartner &
Sperling 1987). The transient component is
distinguished from a separate, slower com-
ponent that improves performance in more
difﬁcult tasks. This sustained component
persists over time but takes a few hundred
milliseconds to peak. Once attention is directed
to a location and then reoriented to a new
www.annualreviews.org • A Taxonomy of Attention 79
Annu. Rev. Psychol. 2011.62:73-101. Downloaded from www.annualreviews.org
by University of Minnesota - Twin Cities - Wilson Library on 05/13/11. For personal use only.

[p.8]
PS62CH04-Chun ARI 22 November 2010 9:23
location, processing at the original location is
now inhibited—i.e., inhibition of return. This
encourages orienting toward novel locations,
playing a useful role in search and foraging
behaviors (see Klein 2000 for a review).
In addition to being able to quickly reorient
to a novel event, attention must also suppress
distraction from task-irrelevant stimuli. Atten-
tional sets or attentional control settings allow
observers to focus on task-relevant items (Folk
et al. 1992), and there is ongoing debate on what
kinds of stimuli can distract people; factors in-
clude abrupt onsets, emotionally salient stimuli,
or the appearance of new objects (Phelps et al.
2006, Theeuwes 2004, Yantis & Egeth 1999).
Newly discovered cues that strongly demand
attention include moving or looming stimuli
(Abrams & Christ 2003, Franconeri & Simons
2003), especially those on a collision path with
the observer (Lin et al. 2008). When a distract-
ing stimulus matches some feature of the atten-
tional set, it captures attention by temporarily
shifting spatial attention to the distractor (Folk
et al. 2002).
Different neural mechanisms mediate ori-
enting to a cued location and reorienting to a
new location. The intraparietal sulcus, superior
frontal, and superior temporal cortex direct vol-
untary spatial shifts to task-relevant locations
(Yantis et al. 2002). The parietal cortex contains
representations useful for such spatial orienting
based on topographic maps of attentional foci
(Sereno et al. 2001, Silver et al. 2005). A dif-
ferent circuit, mainly the right temporoparietal
junction, is active when observers need to re-
orient to a target appearing in an unattended
location (Corbetta et al. 2008, Hopﬁnger et al.
2000).
Additionally, just as vision is limited by
the acuity (spatial resolution) of the eye, spa-
tial attention is limited by its own acuity
(Intriligator & Cavanagh 2001, Pelli & Tillman
2008; Vickery et al. 2010). Interestingly, atten-
tional acuity is much worse than visual acu-
ity, and as a result, the ability to individuate
(select) a target from neighboring items has a
coarse grain. Resolution deteriorates dramat-
ically moving out into the periphery (Intrili-
gator & Cavanagh 2001), affecting the ability
to individuate and identify two targets appear-
ing close to another. Surprisingly, two targets
spaced close to each other are more difﬁcult to
perceive than two targets spaced far apart, even
when low-level interference is controlled for
(Bahcall & Kowler 1999, Kristj ´ansson &
Nakayama 2002). The attentional limitation
occurs beyond primary visual cortex, based on
evidence that items can go unresolved by at-
tention but nevertheless produce signiﬁcant
orientation-speciﬁc aftereffects (He et al. 1996).
Temporal attention. Attention can also be
focused on stimuli appearing at different points
in time even in the same location (Coull &
Nobre 1998). Spatial and temporal attention
share many properties, yet appear to arise from
independent, dissociable mechanisms; they are
not affected by dual-task interference (Correa
& Nobre 2008), and their effects are additive
(Doherty et al. 2005). Just as the number of
objects that can be fully attended across space
is limited, the number of objects that can be
attended over time is constrained as well. That
is, the rate of information processing is lim-
ited. Temporal attention selects task-relevant
information to overcome these limitations in
t h er a t eo fp r o c e s s i n g .
Temporal attention can be studied in its
purest form by asking subjects to search for tar-
gets among distractors appearing in the same
location in rapid succession. Search for single
targets appearing in rapid serial visual presen-
tation tasks helped to reveal an impressive rate
of object recognition. Remarkably, viewers can
detect a categorically deﬁned target (e.g., wed-
ding scene) at rates of around 8–10 images per
second (Potter 1975), consistent with event-
related potential (ERP) evidence of how quickly
complex images are categorized (Thorpe et al.
1996).
However, the ability to retain and report tar-
gets presented in rapid serial visual presentation
is more severely constrained. This second-stage
limitation is best revealed by asking subjects
to search for two or more targets instead
of just one (Broadbent & Broadbent 1987,
80 Chun · Golomb ·Turk-Browne
Annu. Rev. Psychol. 2011.62:73-101. Downloaded from www.annualreviews.org
by University of Minnesota - Twin Cities - Wilson Library on 05/13/11. For personal use only.

[p.9]
PS62CH04-Chun ARI 22 November 2010 9:23
Chun & Potter 1995, Raymond et al. 1992).
Consider a simple search for letter targets
among digit distractors presented at rates of
10 per second. Report for the ﬁrst target (T1)
is usually high, whereas the ability to see and
report the second target (T2) is dramatically
impaired when T2 appears within half a
second of T1. This striking deﬁcit for the
second target is known as the attentional blink,
and Raymond et al. (1992) showed that it is
attentional because the deﬁcit for T2 does not
occur when T1 is absent or when there is a cue
that allows observers to ignore T1.
The attentional blink paradigm has spawned
much research focusing on questions essential
to the study of attention. When T2 is missed,
is its identity processed but not encoded? Or
is it not identiﬁed at all? This is one incarna-
tion of the early- versus late-selection debate
(Treisman 1960). Behavioral priming and neu-
roimaging evidence suggests that missed tar-
gets are processed up to their semantic identity
(Luck et al. 1996, Marois et al. 2004, Shapiro
et al. 1997).
Understanding what limits performance in
the attentional blink can inform how attention
gates perceptual awareness. One idea is that
encoding a target appearing amid interfering
items simply takes time during which other tar-
gets cannot be encoded. In other words, a rapid
identiﬁcation system in the ﬁrst stage of pro-
cessing that can handle input rates of at least
10 items per second (and likely higher) is fol-
lowed by a narrow limitation in a second stage
that consolidates targets into working mem-
ory and that supports awareness (Bowman &
Wyble 2007, Chun & Potter 1995, Jolicoeur
1999). This process of raising perceived items
into awareness and working memory is thought
to involve the fronto-parieto-temporal network
(Marois et al. 2000), especially synchroniza-
tion between these brain mechanisms (Dehaene
et al. 2003, Gross et al. 2004), and reentrant
processes (see Di Lollo et al. 2000 for related
substitution masking effects).
A newly emerging view is that the atten-
tional blink does not represent a capacity limita-
tion, but rather inhibitory processes that delay
the re-engagement of attention to other targets
or temporary loss of control (Di Lollo et al.
2005, Olivers & Meeter 2008). This is sup-
ported by evidence that attentional engagement
is delayed and diffused during the attentional
blink (Vul et al. 2008) and that the attentional
blink can be alleviated by cuing (Nieuwenstein
et al. 2005). The new view is more compati-
ble with the fact that impairments are lessened
for targets appearing in direct succession (e.g.,
Lag 1 sparing: Di Lollo et al. 2005), and it bet-
ter links mechanisms of temporal attention and
spatial attention.
Features and objects. Attention can be
directed to spatial locations, time points, or
modalities alone (as in preparatory cuing pre-
ceding a sensory event), or it can be directed
to features or objects that can be selected
across space, time, and modality. Features are
points in modality-speciﬁc dimensions, such as
color, pitch, saltiness, and temperature. One
of the primary mechanisms for selection is
via saliency in these feature dimensions—with
salience deﬁned as unusual or extreme values,
such as a single red item amid a ﬁeld of green,
a piercing baby’s scream, or an unexpectedly
hot faucet. Most models of visual search rely
on such bottom-up (exogenous) visual features
(Wolfe & Horowitz 2004), which can be
described computationally (Itti & Koch 2000).
Attention to features directly modulates
and enhances the processing within feature-
selective cortical regions (Kanwisher 2000,
Reynolds & Chelazzi 2004). Attention to ori-
entation enhances the gain of orientation pro-
cessing and the sensitivity of contrast detection
in V4 (McAdams & Maunsell 1999) and mod-
ulates processing in human visual cortex (Liu
et al. 2007). Feature attention can also facili-
tate motion processing in area MT (O’Craven
et al. 1997) and heighten blood-oxygen-level-
dependent activity for faces and scenes within
face-selective and scene-selective cortex, re-
spectively (Wojciulik et al. 1998). Importantly,
feature attention is not spatially restricted, lead-
ing to a global enhancement of features out-
side the spatial focus of attention (Treue &
www.annualreviews.org • A Taxonomy of Attention 81
Annu. Rev. Psychol. 2011.62:73-101. Downloaded from www.annualreviews.org
by University of Minnesota - Twin Cities - Wilson Library on 05/13/11. For personal use only.

[p.10]
PS62CH04-Chun ARI 22 November 2010 9:23
Mart´ınez Trujillo 1999). Feature-based selec-
tion can be distinguished from spatial selec-
tion, and the fronto-parietal network involved
in both types of selection contains subregions
devoted more exclusively to spatial or feature
selection (Giesbrecht et al. 2003). Going be-
yond demonstrations of modulation, current
research is now starting to elucidate the mi-
crocircuitry, functional connectivity, and com-
putational requirements by which attention
modulates feature-speciﬁc responses. Synchro-
nization between local neurons and more dis-
tant neuronal groups can strengthen signals and
enact selection (Fries et al. 2001, Womelsdorf
et al. 2007), even predicting the speed of change
detection (Womelsdorf et al. 2006). Comple-
menting such principles, recent studies suggest
that attention may improve performance by re-
ducing interneuronal correlations, effectively
reducing noise as a primary mechanism be-
yond what is predicted from the boost in signal
(ﬁring rates) per se (Cohen et al. 2009, Mitchell
et al. 2009).
Attention can be directed not just to features
but also to whole objects (Scholl 2001). The
distinction is that when objects are selected,
all of its features are selected together with
the object (O’Craven et al. 1999), including
information about the identity and history
of the object as it moves about or changes
over space and time (Kahneman et al. 1992).
Essential for individuating different objects
from each other, object-based representations,
known as object ﬁles, enjoy extensive empirical
support (Flombaum et al. 2009, Xu & Chun
2009). It’s easier to select two features coming
from the same object than to direct attention
to two features that span across two objects
(Duncan 1984). When one part of an object
is cued, then subjects are faster to respond to
a target appearing within the same object at
a different location than to an equally distant
target appearing within a different object (Egly
et al. 1994). Furthermore, shifting attention to
locations within objects evokes greater retino-
topic and parietal activity than do shifts of
identical distances across different objects
(Shomstein & Behrmann 2006). Such
object-based effects predict what patients
with hemispatial neglect will perceive (Driver
& Vuilleumier 2001), what information will
be remembered (Yi & Chun 2005), which
information dominates in binocular rivalry
tasks (Mitchell et al. 2004), and how well
subjects can track moving objects [Cavanagh
& Alvarez 2005 (reviewed more extensively
below), Scholl & Pylyshyn 1999]. Object-based
attention involves cortical circuitry similar to
that involved in spatial attention (Fink et al.
1997, Yantis & Serences 2003).
Internal Attention
Whereas external attention involves selection
of perceptual information coming through the
senses, much of cognition involves regulating
our internal mental life, such as planning what
to eat for dinner on the walk or drive home
from work, or trying to remember what’s in the
refrigerator. Just as in the case of external at-
tention, there are severe capacity limitations in
the number of items that can be maintained in
working memory, the number of choices that
can be selected, the number of tasks that can
be executed, and the number of responses that
can be generated at any given time. The pri-
mary function of cognitive (executive) control
mechanisms is to select between these compet-
ing alternatives, independent of sensory modal-
ity (Miller & Cohen 2001). Given trafﬁc ahead,
one can choose to stay on one’s route or de-
cide to navigate around it. When retrieving in-
formation from memory, one must select from
several competing alternatives: Did I park on
the fourth or third ﬂoor of this garage? To the
extent that there are limitations in the num-
ber of alternatives that can be considered at
any given time—and the even broader set of re-
sponses and choices that can be made to these
alternatives—cognitive control is intrinsically
attentional. Thus, it would be useful to under-
stand selective processes in executive/cognitive
control, while seeing what’s common and
different about these processes in compari-
son to those in perceptual selection—external
attention.
82 Chun · Golomb ·Turk-Browne
Annu. Rev. Psychol. 2011.62:73-101. Downloaded from www.annualreviews.org
by University of Minnesota - Twin Cities - Wilson Library on 05/13/11. For personal use only.

[p.11]
PS62CH04-Chun ARI 22 November 2010 9:23
We distinguish internal attention from ex-
ternal attention in two different ways. The ﬁrst
is just based on the content of selection. Internal
attention includes cognitive control processes
and operates over representations in working
memory, long-term memory, task rules, deci-
sions, and responses. Because the information
to be selected is internal, we deﬁne internal at-
tention as the set of operations that are focused
on such cognitive representations. External at-
tention has more proximal, modality-speciﬁc
referents to the external, perceptual world.
Second, behavioral evidence indicates that
many perceptual processes, even capacity-
limited ones, can proceed somewhat indepen-
dently of cognitive control. This does not imply
that perceptual processes are never inﬂuenced
by cognitive control. Clearly, executive pro-
cesses and working memory inﬂuence external
selection and biasing, as we review below.
However, the point is that internal attention
and external attention cannot be equated
and have independent capacities that can be
inferred from patterns of dual-task interference
and the general structure of neural systems.
Overall, a network of regions in pre-
frontal cortex and posterior parietal cortex
sets top-down signals for biasing selection of
information and competition for processing
resources (Buschman & Miller 2007, Miller &
Cohen 2001, Ridderinkhof et al. 2004). These
attentional sets, or task rules, thereby set up
perceptual ﬁlters and map perceptual features
onto motor responses. Once established, these
mappings can determine external selection
without interference from frontal lobe dysfunc-
tion (Rossi et al. 2007). An important question is
whether there is a core, central mechanism that
governs all executive functions or whether there
are speciﬁc mechanisms for different domains
of internal attention (Badre & Wagner 2004,
Duncan & Owen 2000, Rushworth et al. 2001,
Wager et al. 2004, Wojciulik & Kanwisher
1999). Behavioral analyses (Miyake et al. 2000)
and precise multivoxel pattern classiﬁcation
techniques in functional magnetic resonance
imaging (fMRI) have revealed speciﬁcity
for shifting visuospatial attention, switching
categorization rules, and shifting attention in
working memory (Esterman et al. 2009).
We ﬁrst discuss how internal attention is in-
dependent of external attention, especially for
response selection, task switching, and long-
term memory retrieval. Working memory is
considered as a separate internal attention pro-
cess (Rowe et al. 2000), but interfacing closely
with external attention.
Response and task selection. When asked to
make two simple responses or choices in suc-
cession, the ability to execute the second re-
sponse is delayed when it appears within half a
second of the ﬁrst. This delay is known as the
psychological refractory period (Pashler 1994).
The precise duration of this delay, as a func-
tion of the timing between the ﬁrst and sec-
ond task, exquisitely reveals a central bottle-
neck, independent of modality and task type,
although researchers debate the nature of the
limitation (Logan & Gordon 2001, Meyer &
Kieras 1997). Importantly, slowing down per-
ceptual processing does not affect the response
selection delay, indicating some degree of in-
dependence. Thus, response selection is cate-
gorized ﬁrmly under internal attention, distin-
guished from perceptual selection in external
attention. Imaging studies have dissociated re-
sponse selection limitations from other forms of
capacity limitations (Herath et al. 2001, Jiang
& Kanwisher 2003), while there is convergence
for a common processing bottleneck in the lat-
eral frontal cortex (Marois & Ivanoff 2005), es-
pecially for the psychological refractory period
and the attentional blink.
In addition to the impairment associ-
ated with consecutive responses, observers are
slower to switch from one kind of task to a dif-
ferent task, as compared to simply repeating
the same task (Rogers & Monsell 1995). These
task-switching costs reveal attentional limita-
tions that can be studied separately from the re-
sponse selection limitations above. The switch
cost is larger as the delay between the task
instruction and target appearance is shorter.
Yet, even with sufﬁcient delay, a small, resid-
ual switch cost is apparent, suggesting that the
www.annualreviews.org • A Taxonomy of Attention 83
Annu. Rev. Psychol. 2011.62:73-101. Downloaded from www.annualreviews.org
by University of Minnesota - Twin Cities - Wilson Library on 05/13/11. For personal use only.

[p.12]
PS62CH04-Chun ARI 22 November 2010 9:23
new task must actually be executed in order to
fully implement the switch. That is, there’s a
limit to how ﬂexibly and effectively one can pre-
pare for a new task before actually executing it
(Monsell 2003). Functional neuroimaging is
proving to be useful for identifying differ-
ent internal control mechanisms in prefrontal,
parietal, and basal ganglia regions (Braver
et al. 2003, Dove et al. 2000, Leber et al.
2008), for revealing different roles for switch-
ing between responses versus visual features
(Rushworth et al. 2002), and for demonstrat-
ing how foreknowledge and preparation may
facilitate task switching (Sohn et al. 2000).
More generally, response and task selection
require inhibition of competing options (Aron
et al. 2004, Nee et al. 2007). This is especially
true for simple behaviors such as withholding
a response or saccade when a stop signal ap-
pears (Aron et al. 2003, Boucher et al. 2007) or
in automated tasks such as Stroop interference,
where naming the color of a word is slowed by
the difﬁculty of suppressing the written word
when it is the name of a different color. In the
latter case, task representations or rules in pre-
frontal cortex need to prioritize color name re-
sponses over the more automatic written word
responses, regulated by the detection of conﬂict
at the response level by the anterior cingulate
cortex (Botvinick et al. 2001).
Response and task selection are clearly in-
ternal processes, yet importantly they exhibit
the basic characteristics of attention as deﬁned
above. They suffer from the limited-capacity
problem, solve it by selecting among alterna-
tives and modulating brain activity representing
the selected item, and are challenged to sus-
tain vigilance (Braver et al. 2003, Leber et al.
2008). Furthermore, these processes are known
to be affected in disorders such as attention-
deﬁcit hyperactivity disorder (Dibbets et al.
2010, Tamm et al. 2004).
Long-term memory. Long-term memory
can also be a target of internal attention. At-
tention helps determine which information is
encoded into long-term memory and how it is
retrieved (e.g., Chun & Turk-Browne 2007, Yi
& Chun 2005). People attend to all kinds of
information every day, but they do not encode
or remember all the things that they have at-
tended. Memory researchers have long known
that elaborative encoding enhances memory
(Craik & Lockhart 1972). Elaborative encoding
involves actively associating new information
with context and other information in the mind.
Assuming this process is capacity limited such
that people cannot encode an inﬁnite amount
of information, then understanding the role of
attention is essential.
To study memory encoding, one can ex-
amine how neural processing is different be-
tween when an item is later remembered com-
pared to when it is forgotten. Neuroimaging
methods have relied on this subsequent mem-
ory paradigm to show higher activation in pre-
frontal and temporal cortices during successful
memory formation of verbal and visual events
(Brewer et al. 1998, Wagner et al. 1998). Pre-
trial activations and patterns of neural oscilla-
tions also predict memory for both direct and
indirect measures of memory (Osipova et al.
2006, Otten et al. 2002, Polyn et al. 2005,
Turk-Browne et al. 2006).
In addition to these predictive effects of at-
tention on encoding, reﬂecting back on a re-
cent perceptual experience also beneﬁts long-
term memory. As opposed to working memory,
which involves sustained maintenance, such
reﬂective acts can be brief and transient. In
the multiple entry, modular (MEM) mem-
ory model ( Johnson 1983), this kind of re-
ﬂection corresponds to a component process
called refreshing. Similar to the implementa-
tion of task rules, refreshing is mediated by the
dorsolateral prefrontal cortex ( Johnson et al.
2005). The act of refreshing may help sal-
vage and enhance a decaying perceptual rep-
resentation or may itself be treated as a sec-
ond “perceptual” experience with the refreshed
concept. Correspondingly, refreshing activates
visual cortical regions selective for the con-
tents being refreshed ( Johnson et al. 2007),
enhancing encoding into both explicit and im-
plicit memory ( Johnson et al. 2002, Yi et al.
2008).
84 Chun · Golomb ·Turk-Browne
Annu. Rev. Psychol. 2011.62:73-101. Downloaded from www.annualreviews.org
by University of Minnesota - Twin Cities - Wilson Library on 05/13/11. For personal use only.

[p.13]
PS62CH04-Chun ARI 22 November 2010 9:23
Once encoded, retrieval from long-term
memory requires selection between speciﬁc
memories competing for recall (Badre et al.
2005, Ranganath et al. 2000). Indeed, forgetting
typically arises from memory retrieval failures
rather than the loss of the information per se,
and so it is important to understand the selec-
tion mechanisms involved in enhancing target
memories from distractor memories. Accord-
ingly, recent theories have drawn analogies be-
tween selection in the perceptual domain and
selection during memory retrieval (Cabeza et al.
2008, Wagner et al. 2005). A strong version of
this analogy—that the same posterior parietal
mechanisms that support goal-directed atten-
tion also support episodic memory retrieval—
is not well-supported (Hutchinson et al. 2009),
but the general notion of functional correspon-
dence between attention and retrieval deserves
further study.
The competitive nature of memory retrieval
is apparent in other ways. The act of retriev-
ing one item increases the likelihood of later
forgetting other unretrieved items that share
associative links (Anderson et al. 2004). This
retrieval-induced forgetting results from the
strengthening of associations during retrieval
combined with the weakening of associations
for unretrieved items. Such competitive inter-
actions during retrieval may be essential for
learning (Norman et al. 2007) and have the
adaptive beneﬁt of ultimately facilitating re-
trieval and reducing conﬂict (Kuhl et al. 2007).
Working memory. Working memory en-
ables the maintenance and manipulation of
information in the absence of sensory support
(D’Esposito et al. 1995, Smith & Jonides 1999).
Because it operates over internal representa-
tions (of what is no longer externally available),
we place it within internal attention. However,
working memory is truly at the interface be-
tween internal attention and external attention.
Baddeley’s (2003) inﬂuential model of working
memory posits a central executive mechanism
coupled with separate stores for visuospatial
information and phonological information.
Perceptual selection serves as a ﬁlter that
determines entry into working memory for
maintenance. Selection is critical because
working memory is limited in capacity. In the
case of vision, the capacity of working memory
is about four objects. The unit of storage is
important to characterize because multiple
features can be chunked into objects to increase
capacity (Luck & Vogel 1997). At the same
time, increasing the complexity of features
reduces overall capacity (Alvarez & Cavanagh
2004, Todd & Marois 2004, Xu & Chun 2006;
but see Awh et al. 2007). Verbal working mem-
ory (phonological loop) has a capacity of about
seven chunks (Miller 1956), and its effectiveness
is dependent on phonological characteristics
of acoustic input, words, and the names of pic-
tures being rehearsed (Baddeley 1992). Internal
attention includes cognitive control or central
executive mechanisms that prioritize which
perceptual information to encode and maintain
in working memory, while suppressing distrac-
tion (Most et al. 2005). These functions reside
in prefrontal cortex (Miller & Cohen 2001).
Working memory has been placed at the
interface between internal and external on
the basis of studies showing that mainte-
nance of information in working memory bi-
ases attention for similar kinds of information
and correspondingly guides eye movements
(Hollingworth et al. 2008). For example, main-
tenance of spatial locations in working memory
biases spatial attention to those locations (Awh
& Jonides 2001, Corbetta & Shulman 2002),
and these biases occur for speciﬁc shapes as
well (Downing 2000, Soto et al. 2005). Work-
ing memory maintenance directly modulates
processing in relevant sensory cortex (Harrison
& Tong 2009, Serences et al. 2009), and sup-
presses irrelevant information (Gazzaley et al.
2005).
These biasing effects are capacity-limited,
as revealed by speciﬁc patterns of interference.
For example, concurrent visual working mem-
ory load interferes with memory-based gaze
correction (Hollingworth et al. 2008). Also,
when performing visual search concurrently
with spatial working memory tasks, search
efﬁciency drops, suggesting shared capacity
www.annualreviews.org • A Taxonomy of Attention 85
Annu. Rev. Psychol. 2011.62:73-101. Downloaded from www.annualreviews.org
by University of Minnesota - Twin Cities - Wilson Library on 05/13/11. For personal use only.

[p.14]
PS62CH04-Chun ARI 22 November 2010 9:23
(Oh & Kim 2004, Woodman & Luck 2004).
However, object working memory does not
change search efﬁciency, indicating that shared
mechanisms are mostly spatial (Woodman et al.
2001). Such content-speciﬁc interference ef-
fects can even reduce the distracting effects of
nontargets. Verbal working memory load can
reduce word interference in a Stroop task (Kim
et al. 2005); likewise, holding faces in working
memory can reduce interference from incon-
gruent face stimuli but not scene stimuli, and
vice versa (Park et al. 2007).
Working memory tasks can cause general
interference for both internal and external
attention: Encoding and manipulating infor-
mation in working memory induces psycho-
logical refractoriness effects ( Jolicoeur 1998),
disrupts simple spatial orienting (Dell’Acqua
et al. 2006), and impairs search (Han & Kim
2004). The interaction is bidirectional: Work-
ing memory contents can inﬂuence perceptual
attention, but perceptual attention can also in-
ﬂuence what gets maintained in working mem-
ory (Lepsien et al. 2005). Maintaining a loca-
tion in working memory has been compared to
sustaining perceptual attention on that location
(Awh & Jonides 2001).
There has been a recent surge of interest
in understanding the neural mechanisms of
working memory and how working memory
relates to other types of internal and external
attention. A common thread has been that
working memory shares many properties with
external attention, yet it is also dissociable.
Selection of items in working memory has been
compared to selection of items in visual search
(Astle 2009). Overlapping brain networks for
controlling attention to external and internal
representations have been proposed, with a bias
toward internal representations in more frontal
regions and external representations in more
parietal regions (Nobre et al. 2004). In a partic-
ularly insightful study, Esterman and colleagues
(2009) compared brain activity associated with
switching spatial attention, switching task set,
and switching among memory representations.
They found that a region of superior parietal
cortex was involved in all types of attention
switching, but that they could train multi-
variate classiﬁers to differentiate between the
patterns evoked by internal and external types
of attention. Individual differences approaches
have similarly demonstrated both commonal-
ities and differences between working memory
and perceptual processes (Wager & Smith
2003).
ISSUES AND FUTURE
DIRECTIONS
Early Versus Late Selection:
Lavie’s Load Theory
Almost every textbook features the debate of
early versus late selection as a central issue
in attention research. When objects or events
go unattended and even inhibited, how deeply
are such ignored items processed? This ques-
tion remains useful for understanding the na-
ture of awareness and the processing archi-
tecture of the mind. And the problem seems
largely tractable. Support exists for both early
and late selection views, and research should fo-
cus on clarifying when unattended stimuli are
processed and when they are not. As proposed
in Treisman’s (1960) attenuation theory, the
debate should not be viewed as a dichotomy,
but rather as the two ends of a continuum. Re-
cent work has advanced our ability to determine
from task to task where selection processes fall
along this continuum.
Lavie’s (2005) load theory is a powerful
modern framework to predict the level of
processing for unattended stimuli. The basic
insight is that the amount of processing that
unattended stimuli receive is dependent on
how difﬁcult it is to process the attended target.
If the primary target task is easy, then excess at-
tentional resources will spill over to distractors,
and they will be identiﬁed, indicative of late se-
lection (Lavie 1995). If the primary task is very
difﬁcult, then as all of attention becomes de-
voted to the target, distractors become less well
processed, revealing patterns of early selection.
A classic ﬁnding relies on the Eriksen ﬂanker
task, in which a target is ﬂanked by distractors
86 Chun · Golomb ·Turk-Browne
Annu. Rev. Psychol. 2011.62:73-101. Downloaded from www.annualreviews.org
by University of Minnesota - Twin Cities - Wilson Library on 05/13/11. For personal use only.

[p.15]
PS62CH04-Chun ARI 22 November 2010 9:23
that are mapped to incompatible, competing
responses, slowing down responses to the target
(Eriksen & Eriksen 1974). When the number
of distractors is few, then the overall task is
easy, so distractors will slow down the target
response. Perceptual load can be increased by
having more distractors on the display, exceed-
ing the capacity of attention. Under such cases
of high load, distractors are less well processed,
resulting in less interference (Lavie 1995).
Increased perceptual load (difﬁculty) of a target
task attenuated neural processing of drifting
gratings in V1 (Chen et al. 2008), moving dots
in area MT (Rees et al. 1997) and scene stimuli
in the parahippocampal place area (Yi et al.
2004).
Task difﬁculty itself can be broadly catego-
rized in two different ways. Lavie’s overarch-
ing theory of attention distinguishes percep-
tual load and central limitations, which maps
onto our distinction between external and inter-
nal attention. Central (internal) load includes
increasing the number of items that must be
maintained in working memory or performing
other executive functions such as task switch-
ing (Lavie et al. 2004). Critically, effects of cen-
tral load manipulations on distractor processing
are the opposite of perceptual load manipula-
tions. Increased central load increased distrac-
tor processing because relevant executive pro-
cesses lose control over focusing attention on
the target task, resulting in attention spilling
over to distractors. As a speciﬁc example, in-
creased working memory load increased inter-
ference from distractors (de Fockert et al. 2001).
Most manipulations of central attention will re-
sult in late selection, that is, full perceptual iden-
tiﬁcation of ignored items.
Visual Search
In natural contexts, observers typically search
for a target amid many other competing stimuli
(Treisman & Gelade 1980, Wolfe & Horowitz
2004), and this is a complex skill that spans
across our taxonomy. Search difﬁculty varies
along a continuum from efﬁcient (easy) to in-
efﬁcient (hard), as determined by both visual
factors and nonvisual factors such as the num-
ber of distractors and their homogeneity. At-
tention is most efﬁciently directed to target ob-
jects that are salient and dissimilar from other
distractor objects (Duncan & Humphreys 1989,
Itti & Koch 2000). Beyond visual factors, visual
search is facilitated when targets appear in pre-
dictable locations, cued by background context
and past experience (Bar et al. 2004, Chun 2000,
Torralba et al. 2006).
Search strategies are maximized in a way that
directs eye movements toward regions of in-
terest based on scene statistics while minimiz-
ing demands on memory (Najemnik & Geisler
2005, Summerﬁeld et al. 2006). How much
memory is needed has been a matter of debate.
On one extreme, search has been described as
amnesic in the sense that searched items are not
tagged to be ignored. This claim is based on the
ﬁnding that search efﬁciency does not change
whether the search display is static or whether
the items move around (Horowitz & Wolfe
1998). However, most subsequent studies have
provided evidence for some role for memory
in search (Chun 2000, Shore & Klein 2001).
At a short time scale within trials, items that
were searched and rejected become momen-
tarily tagged with inhibition to prohibit search
through these items again (Klein 2000, Watson
& Humphreys 1997). From trial to trial, prim-
ing of features (priming of popout: Kristj´ansson
et al. 2005, Maljkovic & Nakayama 1994) or
learning of predictive context (contextual cue-
ing: Chun 2000) serves to facilitate search. As
direct evidence, Hollingworth & Henderson
(2002) have demonstrated that people retain
fairly detailed information from attended ob-
jects within scenes during search.
The visual search task has many practical ap-
plications, especially for understanding when
people make mistakes, for example, missing
dangerous items during baggage screening or
pathological tissue while viewing radiographs.
Beyond visual factors, a major source of difﬁ-
culty is cognitive (Chun & Wolfe 1996). Peo-
ple have difﬁculty detecting target events that
are rare in occurrence, known as the target
prevalence effect (Wolfe et al. 2005). However,
www.annualreviews.org • A Taxonomy of Attention 87
Annu. Rev. Psychol. 2011.62:73-101. Downloaded from www.annualreviews.org
by University of Minnesota - Twin Cities - Wilson Library on 05/13/11. For personal use only.

[p.16]
PS62CH04-Chun ARI 22 November 2010 9:23
giving observers the opportunity to conﬁrm
their search responses and to correct misses
may reduce error (Fleck & Mitroff 2007). Un-
derstanding visual search performance requires
characterizing every process, from sensation
and perception, to decision-making and moti-
vation, and motor execution.
Object Tracking and
Perceptual Stability
Objects and observers are frequently in motion,
and thus a fundamental task for attention is to
keep track of the locations of objects over time
and across change (Kahneman et al. 1992). A re-
lated operation called visual indexing provides a
way for attentional mechanisms to reference or
point to the object ﬁles or tokens that need to be
tracked (Pylyshyn 1989). Such object tracking
touches on core attention themes of capacity
limitation, selection, and vigilance. This abil-
ity is studied in multiple object tracking tasks
that require more than one target to be mon-
itored, often when there are no visual features
distinguishing targets to be tracked from other
moving distractors (Pylyshyn & Storm 1988).
Accuracy in this task declines abruptly when
more than about four items must be tracked
and is strongly inﬂuenced by how objects main-
tain their integrity and spatiotemporal continu-
ity (objecthood) as they move about (Scholl &
Pylyshyn 1999). Note that tracking and work-
ing memory have comparable capacity, known
as the magical number four (Cowan 2001);
however, this coincidence alone does not point
to a common mechanism (Fougnie & Marois
2006, Scholl & Xu 2001). Visuospatial and at-
tentional resolution also strongly affects track-
ing performance (Alvarez & Franconeri 2007).
Even when objects themselves are station-
ary, our eyes move constantly and drastically
change retinal input. Given this changing in-
put, it is remarkable that observers can maintain
a stable visual representation of the environ-
ment as the eyes move about (Cavanagh et al.
2010, Math ˆot & Theeuwes 2011). This feat is
intriguing because the locus of attention rela-
tive to ﬁxation and to one’s retinotopic frame of
reference necessarily changes as the eyes move
around a scene. For example, one still needs to
monitor a trafﬁc light and the car ahead while
driving, even while moving one’s eyes about
from car to car, dashboard to mirror, and so
on (Lleras et al. 2005).
Historically, most work suggested that it
was not possible to simultaneously make an
eye movement to one location while covertly
attending to another location (Deubel &
Schneider 1996, Hoffman & Subramaniam
1995, Kowler et al. 1995). However, recent
work has demonstrated otherwise, revealing
that visuospatial attention is maintained in
retinotopic coordinates and updated as nec-
essary with each eye movement according to
spatiotopic, world-centered reference frames.
When subjects must maintain attention on a
spatiotopic location, attention lingers at the
previous retinotopic location for a brief period
of time after an eye movement before updating
to the correct location (Golomb et al. 2008),
accompanied by corresponding fMRI and ERP
facilitation in human visual cortex (Golomb
et al. 2010).
Attention and Awareness
The relation between attention and conscious
awareness requires substantial review, available
elsewhere (Block 2005, Dehaene et al. 2006,
Koch & Tsuchiya 2007, Rees et al. 2002,
Rensink 2000). One basic point to make here
is that although attention plays a role in gating
which information reaches awareness, even
affecting the appearance of objects (Carrasco
et al. 2004), attention and awareness are not
the same (Lamme 2003). Attending to an
object and becoming aware of an object are
both correlated with higher activity in relevant
sensory processing regions (Ress & Heeger
2003). However, to attend to an object does
not ensure awareness (Levin & Simons 1997).
Magnetoencephalography reveals distinct sig-
nals for consciously seen stimuli, independent
of attention, while manipulations of spatial
attention modulate different types of oscilla-
tory brain activity, independent of whether
88 Chun · Golomb ·Turk-Browne
Annu. Rev. Psychol. 2011.62:73-101. Downloaded from www.annualreviews.org
by University of Minnesota - Twin Cities - Wilson Library on 05/13/11. For personal use only.

[p.17]
PS62CH04-Chun ARI 22 November 2010 9:23
the stimuli were consciously perceived or not
(Wyart & Tallon-Baudry 2008). Many demon-
strations of perceptual identiﬁcation without
awareness involved stimuli that were spatially
attended even when they weren’t reportable
(Dehaene et al. 2001), especially during tem-
poral selection tasks such as the attentional
blink (Luck et al. 1996, Marois et al. 2004).
Large-scale integration of neural activity
may be one path toward understanding the
neural correlates of consciousness (Dehaene
et al. 2006). Global awareness is correlated
with long-distance synchronization of gamma
oscillations across widely separated brain re-
gions (Melloni et al. 2007, Womelsdorf et al.
2007). Distinguishing aware states from un-
aware states remains a strong research priority
for the ﬁeld, and the attention taxonomy can
help map out how awareness integrates process-
ing across multiple systems.
Prospective Activity: Decoding
and Predicting Attentional States
Vigilance, that is, attentiveness, ﬂuctuates over
time. Behavioral methods can typically mea-
sure only the consequences of such variation,
whereas functional neuroimaging methods can
illuminate causal factors and the internal states
that precede changes in performance. Fur-
thermore, pattern classiﬁcation methods allow
researchers to decode what someone is attend-
ing to or anticipating (Haynes & Rees 2005,
Kamitani & Tong 2005, Stokes et al. 2009).
One only needs to examine the time periods
before a trial to look at antecedent states
that may explain performance ﬂuctuations.
EEG provides good temporal resolution to
study how synchronous activity may predict
enhanced visual perception (Hanslmayr et al.
2007). Conventional fMRI signal average
measures can explain lapses of attention with
reduced prestimulus activity in attentional
control regions, such as anterior cingulate and
right prefrontal cortex (Weissman et al. 2006),
along with less deactivation of the “default-
mode” network (Raichle et al. 2001). Leber
et al. (2008) predicted increased cognitive ﬂexi-
bility (smaller task switching costs) when fMRI
revealed higher levels of pretrial activity in
prefrontal and posterior parietal cortex, as well
as the basal ganglia. Prospective activity can
also predict susceptibility to attentional capture
(Leber 2010). Explaining variations in attention
and performance using fMRI or EEG measures
will yield novel insights into the mechanisms
of attention, accounting for variability in other
cognitive processes that depend on attention,
such as memory encoding (Otten et al. 2002,
Turk-Browne et al. 2006), or performance
impairments due to anxiety (choking) (Beilock
& Carr 2001). Ultimately, understanding
vigilance and attentiveness should open up new
ways to improve attention, as discussed below.
Enhancing Attention With Emotion,
Reward, or Training
The notion of enhancing attention appears cir-
cular. However, attention ﬂuctuates, so one of
the most practically useful and clinically im-
portant questions to ask is how high levels of
performance can be sustained. Numerous ap-
proaches can be considered here.
Emotional arousal enhances attention
(Phelps et al. 2006). That is, emotionally
charged stimuli capture attention (Anderson
& Phelps 2001, Most et al. 2005, Ohman
& Mineka 2001), facilitate visual perception
(Phelps et al. 2006), and improve memory, or at
least the feeling of remembering (Sharot et al.
2004). Although many of these effects may
be attributed to increased arousal, the valence
of mood and induced emotion can affect how
attention operates. For example, positive mood
widens the focus of attention (Rowe et al.
2007). As a complementary fact, attention
inﬂuences emotional evaluation as well. When
novel, otherwise neutral stimuli are actively
ignored, they are subsequently evaluated more
negatively than are previously attended or
novel patterns (Raymond et al. 2003).
Not just increased arousal but also med-
itation or relaxation affects attentional focus.
Subjects relaxed by music, pleasant pictures, or
simple instructions to be less focused showed
www.annualreviews.org • A Taxonomy of Attention 89
Annu. Rev. Psychol. 2011.62:73-101. Downloaded from www.annualreviews.org
by University of Minnesota - Twin Cities - Wilson Library on 05/13/11. For personal use only.

[p.18]
PS62CH04-Chun ARI 22 November 2010 9:23
reduced attentional blink deﬁcits (Olivers &
Nieuwenhuis 2005). Meditation and mindful-
ness beneﬁt sustained attention (Bishop et al.
2004, Lutz et al. 2008). Attentional tasks, espe-
cially those related to internal attention, im-
prove from physical exercise or even walks
through nature (Berman et al. 2008, Colcombe
& Kramer 2003).
Beyond explicit emotional cues, more gen-
eral social cues attract attention. Faces are read-
ily detected amid nonface stimuli (Hershler &
Hochstein 2005), gaze perception triggers ori-
enting (Driver et al. 1999), and animate objects
are detected more efﬁciently than nonanimate
objects (New et al. 2007). An especially con-
vincing example is the way in which dynamic
cues for animacy, such as perceived chasing, can
draw attention in displays composed of only
simple moving inanimate shapes (Gao et al.
2009).
Rewards, the outcomes of behavior (Schultz
2000), signiﬁcantly shape attention and per-
formance. When selection is reinforced with
reward, processing is enhanced for rewarded
items and locations and inhibited for unselected
items, relative to items that are not explicitly
rewarded (Libera & Chelazzi 2006, Serences
2008). The effects of reward and attention are
frequently confounded in studies, so clarifying
this relationship is an important area for future
research (Maunsell 2004).
Finally, overt training of attention repre-
sents an exciting area for further work. Playing
action video games enhances attentional skills
and even perceptual acuity (Green & Bavelier
2003, 2007). Clinical settings can beneﬁt from
attention training protocols. Individual differ-
ences in pathology such as anxiety disorder
predict how emotional stimuli capture atten-
tion (Bishop et al. 2004). Learning to ignore
disgusted faces using a cuing task has beneﬁcial
effects for social anxiety disorder (Bar-Haim
et al. 2007, Schmidt et al. 2009). Because atten-
tion controls what one perceives, and because
one’s mental and emotional life is fed by per-
ceptions of one’s social world (Ochsner et al.
2002), attention training protocols represent a
highly promising area for interdisciplinary and
translational research, countering the effects of
cognitive aging, facilitating development, and
treating clinical conditions including autism
and attention deﬁcit and hyperactivity disorder.
TOWARD A TAXONOMY
OF ATTENTION
In a well-known folk story, travelers prepared
a pot of boiling water containing nothing but
a large stone. Curious villagers that asked how
it tasted were invited to contribute ingredients
to further enhance the ﬂavor of the stone soup.
Is “attention” such a theoretical soup stone, a
construct with no intrinsic value but to simply
draw in more substantive, concrete descriptions
(Navon 1984)? If the principles of limited ca-
pacity, selection, modulation, and vigilance op-
erate throughout most perceptual and cognitive
processes, would it not be more concise just to
focus on the perceptual processes and cognitive
mechanisms themselves, rather than organizing
them into a loose taxonomy?
Our hope is that this broad review of the lit-
erature not only highlights the utility and need
for a taxonomy, but also the concept of atten-
tion itself. First, attention remains a powerful
general principle. Ultimately, attention refers
to what an individual is focused on, so it remains
practically useful to talk about what task, ob-
ject, event, or thought someone is attending to.
The taxonomy is useful for understanding the
details of which speciﬁc processes are at work,
but it would not be productive to fractionate
the mind in a way that loses sight of how the
holistic individual is behaving.
Second, insights, characteristics, and prin-
ciples from one part of the taxonomy general-
ize to other parts. Crowding effects and cuing
properties are similar in both spatial and tem-
poral selection. Modulatory and ﬁltering effects
are similar across the modalities. Hence, it re-
mains useful to talk about issues and mecha-
nisms of attention across different aspects of the
taxonomy.
Third, the different aspects of attention
interact extensively, and attention provides a
common currency by which information can be
90 Chun · Golomb ·Turk-Browne
Annu. Rev. Psychol. 2011.62:73-101. Downloaded from www.annualreviews.org
by University of Minnesota - Twin Cities - Wilson Library on 05/13/11. For personal use only.

[p.19]
PS62CH04-Chun ARI 22 November 2010 9:23
transacted between different systems and neural
mechanisms. Spatial effects in working mem-
ory inﬂuence spatial mechanisms of attention.
Task rules set by prefrontal executive control
mechanisms inﬂuence perceptual mechanisms
in posterior cortex. Attention is a useful con-
struct for developing an understanding across
these interacting systems. One of the most ex-
citing challenges for the next era of attention
research is to understand how all these differ-
ent mechanisms work together. In particular,
improved understanding of neural mechanisms
and systems should inform the taxonomy, and
vice versa.
Finally, the ﬁeld and literature lack a com-
mon language to communicate and connect
their work with each other. Drawing analogy
with another folk story, to abandon the term
attention would cause all blind men or women
to feel different parts of the elephant, not re-
alizing that they are touching the same animal.
Yet, to rely on the term attention alone has all of
the practical problems we started off with. With
this proposed taxonomy, we seek a way to mean-
ingfully categorize research ﬁndings and under-
lying processes and mechanisms. Constructive
debates about the taxonomy should yield inter-
esting experiments and more incisive theories.
Meanwhile, this taxonomy can serve as a portal
to help select relevant studies in the overwhelm-
ingly rich literature on attention.
We conclude that attention should continue
to serve researchers as a useful construct—after
all, everyone knows what it means.
DISCLOSURE STATEMENT
The authors are not aware of any afﬁliations, memberships, funding, or ﬁnancial holdings that
might be perceived as affecting the objectivity of this review.
ACKNOWLEDGMENTS
Golomb and Turk-Browne contributed equally to this work. The authors are grateful for support
from NIH EY EY014193, P30-EY000785 to Chun, and NIH F31-MH083374 and F32-EY020157
fellowships to Golomb.
LITERATURE CITED
Abrams RA, Christ SE. 2003. Motion onset captures attention. Psychol. Sci. 14:427–32
Alvarez GA, Cavanagh P. 2004. The capacity of visual short-term memory is set both by visual information
load and by number of objects. Psychol. Sci. 15:106–11
Alvarez GA, Franconeri SL. 2007. How many objects can you track? Evidence for a resource-limited attentive
tracking mechanism. J. Vis. 7:1–10
Anderson AK, Phelps EA. 2001. Lesions of the human amygdala impair enhanced perception of emotionally
salient events. Nature 411:305–9
Anderson MC, Ochsner KN, Kuhl B, Cooper J, Robertson E, et al. 2004. Neural systems underlying the
suppression of unwanted memories. Science 303:232–35
Arnell KM, Jolicoeur P. 1999. The attentional blink across stimulus modalities: evidence for central processing
limitations. J. Exp. Psychol.: Hum. Percept. Perform. 25:630–48
Aron AR, Fletcher PC, Bullmore ET, Sahakian BJ, Robbins TW. 2003. Stop-signal inhibition disrupted by
damage to right inferior frontal gyrus in humans. Nat. Neurosci. 6:115–16
Aron AR, Robbins TW, Poldrack RA. 2004. Inhibition and the right inferior frontal cortex. Trends Cogn. Sci.
8:170–77
Astle DE. 2009. Going from a retinotopic to a spatiotopic coordinate system for spatial attention.J. Neurosci.
29:3971–73
www.annualreviews.org • A Taxonomy of Attention 91
Annu. Rev. Psychol. 2011.62:73-101. Downloaded from www.annualreviews.org
by University of Minnesota - Twin Cities - Wilson Library on 05/13/11. For personal use only.

[p.20]
PS62CH04-Chun ARI 22 November 2010 9:23
Awh E, Barton B, Vogel EK. 2007. Visual working memory represents a ﬁxed number of items regardless of
complexity. Psychol. Sci. 18:622–28
Awh E, Jonides J. 2001. Overlapping mechanisms of attention and spatial working memory. Trends Cogn. Sci.
5:119–26
Awh E, Pashler H. 2000. Evidence for split attentional foci.J. Exp. Psychol.: Hum. Percept. Perform. 26:834–46
Baddeley A. 1992. Working memory. Science 255:556–59
Baddeley A. 2003. Working memory: looking back and looking forward. Nat. Rev. Neurosci. 4:829–39
Badre D, Poldrack RA, Par ´e-Blagoev EJ, Insler RZ, Wagner AD. 2005. Dissociable controlled retrieval and
generalized selection mechanisms in ventrolateral prefrontal cortex. Neuron 47:907–18
Badre D, Wagner AD. 2004. Selection, integration, and conﬂict monitoring: assessing the nature and generality
of prefrontal cognitive control mechanisms. Neuron 41:473–87
Bahcall DO, Kowler E. 1999. Attentional interference at small spatial separations. Vis. Res. 39:71–86
Bar M. 2004. Visual objects in context. Nat. Rev. Neurosci. 5:617–29
Bar-Haim Y, Lamy D, Pergamin L, Bakermans-Kranenburg MJ, Van Ijzendoorn MH. 2007. Threat-related
attentional bias in anxious and nonanxious individuals: a meta-analytic study. Psychol. Bull. 133:1–24
Beilock SL, Carr TH. 2001. On the fragility of skilled performance: What governs choking under pressure?
J. Exp. Psychol.: Gen. 130:701–25
Berman MG, Jonides J, Kaplan S. 2008. The cognitive beneﬁts of interacting with nature.Psychol. Sci. 19:1207–
12
Berridge CW, Waterhouse BD. 2003. The locus coeruleus-noradrenergic system: modulation of behavioral
state and state-dependent cognitive processes. Brain Res. Rev. 42:33–84
Biederman J, Faraone SV. 2005. Attention-deﬁcit hyperactivity disorder. Lancet 366:237–48
Bishop S, Duncan J, Lawrence AD. 2004. Prefrontal cortical function and anxiety: controlling attention to
threat-related stimuli. Nat. Neurosci. 7:184–88
Block N. 2005. Two neural correlates of consciousness. Trends Cogn. Sci. 9:46–52
Botvinick MM, Carter CS, Braver TS, Barch DM, Cohen JD. 2001. Conﬂict monitoring and cognitive control.
Psychol. Rev. 108:624–52
Boucher L, Palmeri TJ, Logan GD, Schall JD. 2007. Inhibitory control in mind and brain: an interactive race
model of countermanding saccades. Psychol. Rev. 114:376–97
Bowman H, Wyble B. 2007. The simultaneous type, serial token model of temporal attention and working
memory. Psychol. Rev. 114:38–70
Braver TS, Reynolds JR, Donaldson DI. 2003. Neural mechanisms of transient and sustained cognitive control
during task switching. Neuron 39:713–26
Brewer JB, Zhao Z, Desmond JE, Glover GH, Gabrieli JDE. 1998. Making memories: brain activity that
predicts how well visual experience will be remembered. Science 281:1185–87
Broadbent DE, Broadbent MHP. 1987. From detection to identiﬁcation: response to multiple targets in rapid
serial visual presentation. Percept. Psychophys. 42:105–13
Buschman TJ, Miller EK. 2007. Top-down versus bottom-up control of attention in the prefrontal and
posterior parietal cortices. Science 315:1860–64
Busse L, Roberts KC, Crist RE, Weissman DH, Woldorff MG. 2005. The spread of attention across modalities
and space in a multisensory object. Proc. Natl. Acad. Sci. USA 102:18751–56
Cabeza R, Ciaramelli E, Olson IR, Moscovitch M. 2008. The parietal cortex and episodic memory: an atten-
tional account. Nat. Rev. Neurosci. 9:613–25
Calvert GA, Campbell R, Brammer MJ. 2000. Evidence from functional magnetic resonance imaging of
crossmodal binding in the human heteromodal cortex. Curr. Biol. 10:649–57
Carrasco M, Ling S, Read S. 2004. Attention alters appearance. Nat. Neurosci. 7:308–13
Cavanagh P, Alvarez GA. 2005. Tracking multiple targets with multifocal attention.Trends Cogn. Sci. 9:349–54
Cavanagh P, Hunt AR, Afraz A, Rolfs M. 2010. Visual stability based on remapping of attention pointers.
Trends. Cogn. Sci. 14:147–53
Cave KR, Bichot NP. 1999. Visuospatial attention: beyond a spotlight model. Psychonom. Bull. Rev. 6:204–23
Chen Y, Martinez-Conde S, Macknik SL, Bereshpolova Y, Swadlow HA, Alonso JM. 2008. Task difﬁculty
modulates the activity of speciﬁc neuronal populations in primary visual cortex.Nat. Neurosci. 11:974–82
92 Chun · Golomb ·Turk-Browne
Annu. Rev. Psychol. 2011.62:73-101. Downloaded from www.annualreviews.org
by University of Minnesota - Twin Cities - Wilson Library on 05/13/11. For personal use only.

[p.21]
PS62CH04-Chun ARI 22 November 2010 9:23
Cherry EC. 1953. Some experiments on the recognition of speech, with one and with 2 ears. J. Acoust. Soc.
Am. 25:975–79
Chun MM. 2000. Contextual cueing of visual attention. Trends Cogn. Sci. 4:170–78
Chun MM, Potter MC. 1995. A two-stage model for multiple target detection in rapid serial visual presentation.
J. Exp. Psychol.: Hum. Percept. Perform. 21:109–27
Chun MM, Turk-Browne NB. 2007. Interactions between attention and memory. Curr. Opin. Neurobiol.
17:177–84
Chun MM, Wolfe JM. 1996. Just say no: How are visual searches terminated when there is no target present?
Cogn. Psychol. 30:39–78
Cohen MX, Schoene-Bake JC, Elger CE, Weber B. 2009. Connectivity-based segregation of the human
striatum predicts personality characteristics. Nat. Neurosci. 12:32–43
Colcombe S, Kramer AF. 2003. Fitness effects on the cognitive function of older adults: a meta-analytic study.
Psychol. Sci. 14:125–30
Corbetta M, Akbudak E, Conturo TE, Snyder AZ, Ollinger JM, et al. 1998. A common network of functional
areas for attention and eye movements. Neuron 21:761–73
Corbetta M, Patel G, Shulman GL. 2008. The reorienting system of the human brain: from environment to
theory of mind. Neuron 58:306–24
Corbetta M, Shulman GL. 2002. Control of goal-directed and stimulus-driven attention in the brain. Nat.
Rev. Neurosci. 3:201–15
Correa, Nobre AC. 2008. Spatial and temporal acuity of visual perception can be enhanced selectively by
attentional set. E x p .B r a i n .R e s .189:339–44
Coull JT, Nobre AC. 1998. Where and when to pay attention: The neural systems for directing attention to
spatial locations and to time intervals as revealed by both PET and fMRI. J. Neurosci. 18:7426–35
Cowan N. 2001. The magical number 4 in short-term memory: a reconsideration of mental storage capacity.
Behav. Brain. Sci. 24:87–114
Craik FIM, Lockhart RS. 1972. Levels of processing: a framework for memory research. J. Verbal Learn.
Verbal Behav. 11:671–84
D’Esposito M, Detre JA, Alsop DC, Shin RK, Atlas S, Grossman M. 1995. The neural basis of the central
executive system of working memory. Nature 378:279–81
Dehaene S, Changeux JP, Naccache L, Sackur J, Sergent C. 2006. Conscious, preconscious, and subliminal
processing: a testable taxonomy. Trends Cogn. Sci. 10:204–11
Dehaene S, Naccache L, Cohen L, Le Bihan D, Mangin JF, et al. 2001. Cerebral mechanisms of word masking
and unconscious repetition priming. Nat. Neurosci. 4:752–58
Dehaene S, Sergent C, Changeux JP. 2003. A neuronal network model linking subjective reports and objective
physiological data during conscious perception. Proc. Natl. Acad. Sci. USA 100:8520–25
Dell’Acqua R, Sessa P, Jolicœur P, Robitaille N. 2006. Spatial attention freezes during the attention blink.
Psychophysiology 43:394–400
Desimone R, Duncan J. 1995. Neural mechanisms of selective visual attention.Annu. Rev. Neurosci.18:193–222
Deubel H, Schneider WX. 1996. Saccade target selection and object recognition: evidence for a common
attentional mechanism. Vis. Res. 36:1827–37
Di Lollo V, Enns JT, Rensink RA. 2000. Competition for consciousness among visual events: the psychophysics
of reentrant visual processes. J. Exp. Psychol.: Gen. 129:481–507
Di Lollo V, Kawahara J, Ghorashi SMS, Enns JT. 2005. The attentional blink: resource depletion or temporary
loss of control? Psychol. Res. 69:191–200
Dibbets P, Evers EAT, Hurks PPM, Bakker K, Jolles J. 2010. Differential brain activation patterns in adult
attention-deﬁcit hyperactivity disorder (ADHD) associated with task switching. Neuropsychology 24:413–
23
Doherty JR, Rao A, Mesulam MM, Nobre AC. 2005. Synergistic effect of combined temporal and spatial
expectations on visual attention. J. Neurosci. 25:8259–66
Dove A, Pollmann S, Schubert T, Wiggins CJ, von Cramon DY. 2000. Prefrontal cortex activation in task
switching: an event-related fMRI study. Cogn. Brain Res. 9:103–9
Downing PE. 2000. Interactions between visual working memory and selective attention.Psychol. Sci. 11:467–
73
www.annualreviews.org • A Taxonomy of Attention 93
Annu. Rev. Psychol. 2011.62:73-101. Downloaded from www.annualreviews.org
by University of Minnesota - Twin Cities - Wilson Library on 05/13/11. For personal use only.

[p.22]
PS62CH04-Chun ARI 22 November 2010 9:23
Driver J, Davis G, Ricciardelli P, Kidd P, Maxwell E, Baron-Cohen S. 1999. Gaze perception triggers reﬂexive
visuospatial orienting. Vis. Cogn. 6:509–40
Driver J, Spence C. 1998. Attention and the crossmodal construction of space. Trends Cogn. Sci. 2:254–62
Driver J, Vuilleumier P. 2001. Perceptual awareness and its loss in unilateral neglect and extinction.Cognition
79:39–88
Duncan J. 1984. Selective attention and the organization of visual information.J. Exp. Psychol.: Gen.113:501–17
Duncan J, Humphreys GW. 1989. Visual search and stimulus similarity. Psychol. Rev. 96:433–58
Duncan J, Martens S, Ward R. 1997. Restricted attentional capacity within but not between sensory modalities.
Nature 387:808–10
Duncan J, Owen AM. 2000. Common regions of the human frontal lobe recruited by diverse cognitive
demands. Trends Neurosci. 23:475–83
Egeth HE, Yantis S. 1997. Visual attention: control, representation, and time course. Annu. Rev. Psychol.
48:267–97
Egly R, Driver J, Rafal RD. 1994. Shifting visual attention between objects and locations: evidence from
normal and parietal lesion subjects. J. Exp. Psychol.: Gen. 123:161–77
Eriksen BA, Ericksen CW. 1974. Effects of noise letters upon identiﬁcation of a target letter in a nonsearch
task. Percept. Psychophys. 16:143–49
Eriksen CW, St James JD. 1986. Visual attention within and around the ﬁeld of focal attention: a zoom lens
model. Percept. Psychophys. 40:225–40
Esterman M, Chiu Y, Tamber-Rosenau BJ, Yantis S. 2009. Decoding cognitive control in human parietal
cortex. Proc. Natl. Acad. Sci. USA 106:17974–79
Fink GR, Dolan RJ, Halligan PW, Marshall JC, Frith CD. 1997. Space-based and object-based visual attention:
shared and speciﬁc neural domains. Brain 120:2013–28
Fleck MS, Mitroff SR. 2007. Rare targets are rarely missed in correctable search. Psychol. Sci. 18:943–47
Flombaum JI, Scholl BJ, Santos LR. 2009. Spatiotemporal priority as a fundamental principle of object per-
sistence. In The Origins of Object Knowledge , ed. B Hood, L Santos, pp. 135–64. London: Oxford Univ.
Press
de Fockert JW, Rees G, Frith CD, Lavie N. 2001. The role of working memory in visual selective attention.
Science 291:1803–6
Folk CL, Leber AB, Egeth HE. 2002. Made you blink! Contingent attentional capture produces a spatial
blink. Percept. Psychophys. 64:741–53
Folk CL, Remington RW, Johnston JC. 1992. Involuntary covert orienting is contingent on attentional
control settings. J. Exp. Psychol.: Hum. Percept. Perform. 18:1030–44
Fougnie D, Marois R. 2006. Distinct capacity limits for attention and working memory: evidence from attentive
tracking and visual working memory paradigms. Psychol. Sci. 17:526–34
Franconeri SL, Simons DJ. 2003. Moving and looming stimuli capture attention. Percept. Psychophys. 65:999–
1010
Fries P, Reynolds JH, Rorie AE, Desimone R. 2001. Modulation of oscillatory neuronal synchronization by
selective visual attention. Science 291:1560–63
Gao T, Newman GE, Scholl BJ. 2009. The psychophysics of chasing: a case study in the perception of animacy.
Cogn. Psychol. 59:154–79
Gazzaley A, Cooney JW, Rissman J, D’Esposito M. 2005. Top-down suppression deﬁcit underlies working
memory impairment in normal aging. Nat. Neurosci. 8:1298–300
Ghazanfar AA, Schroeder CE. 2006. Is neocortex essentially multisensory? Trends Cogn. Sci. 10:278–85
Giesbrecht B, Woldorff MG, Song AW, Mangun GR. 2003. Neural mechanisms of top-down control during
spatial and feature attention. Neuroimage 19:496–512
Golomb JD, Chun MM, Mazer JA. 2008. The native coordinate system of spatial attention is retinotopic.
J. Neurosci. 28:10654–62
Golomb JD, Nguyen-Phuc AY, Mazer JA, McCarthy G, Chun MM. 2010. Attentional facilitation throughout
human visual cortex lingers in retinotopic coordinates after eye movements. J. Neurosci. 30:10493–506
Green CS, Bavelier D. 2003. Action video game modiﬁes visual selective attention. Nature 423:534–37
Green CS, Bavelier D. 2007. Action-video-game experience alters the spatial resolution of vision: research
article. Psychol. Sci. 18:88–94
94 Chun · Golomb ·Turk-Browne
Annu. Rev. Psychol. 2011.62:73-101. Downloaded from www.annualreviews.org
by University of Minnesota - Twin Cities - Wilson Library on 05/13/11. For personal use only.

[p.23]
PS62CH04-Chun ARI 22 November 2010 9:23
Gross J, Schmitz F, Schnitzler I, Kessler K, Shapiro K, et al. 2004. Modulation of long-range neural synchrony
reﬂects temporal limitations of visual attention in humans. Proc. Natl. Acad. Sci. USA 101:13050–55
Han S, Kim M. 2004. Visual search does not remain efﬁcient when executive working memory is working.
Psychol. Sci. 15:623–28
Hanslmayr S, Aslan A, Staudigl T, Klimesch W, Herrmann CS, B ¨auml K. 2007. Prestimulus oscillations
predict visual perception performance between and within subjects. Neuroimage 37:1465–73
Harrison SA, Tong F. 2009. Decoding reveals the contents of visual working memory in early visual areas.
Nature 458:632–35
Haynes JD, Rees G. 2005. Predicting the orientation of invisible stimuli from activity in human primary visual
cortex. Nat. Neurosci. 8:686–91
He S, Cavanagh P, Intriligator J. 1996. Attentional resolution and the locus of visual awareness. Nature
383:334–37
Herath PA, Klingberg TA, Young JA, Amunts K, Roland P. 2001. Neural correlates of dual task interference
can be dissociated from those of divided attention: an fMRI study. Cereb. Cortex 11:796–805
Hershler O, Hochstein S. 2005. At ﬁrst sight: a high-level pop out effect for faces. Vis. Res. 45:1707–24
Hoffman JE, Subramaniam B. 1995. The role of visual attention in saccadic eye movements.Percept. Psychophys.
57:787–95
Hollingworth A, Henderson JM. 2002. Accurate visual memory for previously attended objects in natural
scenes. J. Exp. Psych.: Hum. Percept. Perform. 28:113–36
Hollingworth A, Richard AM, Luck SJ. 2008. Understanding the function of visual short-term memory:
transsaccadic memory, object correspondence, and gaze correction. J. Exp. Psychol.: Gen. 137:163–81
Hommel B, Pratt J, Colzato L, Godijn R. 2001. Symbolic control of visual attention. Psychol. Sci. 12:360–65
Hopﬁnger JB, Buonocore MH, Mangun GR. 2000. The neural mechanisms of top-down attentional control.
Nat. Neurosci. 3:284–91
Horowitz TS, Wolfe JM. 1998. Visual search has no memory. Nature 394:575–77
Hunt AR, Kingstone A. 2003. Inhibition of return: dissociating attentional and oculomotor components.
J. Exp. Psychol.: Hum. Percept. Perform. 29:1068–74
Hutchinson JB, Uncapher MR, Wagner AD. 2009. Posterior parietal cortex and episodic retrieval: convergent
and divergent effects of attention and memory. Learn. Mem. 16:343–56
Intriligator J, Cavanagh P. 2001. The spatial resolution of visual attention. Cogn. Psychol. 43:171–216
Itti L, Koch C. 2000. A saliency-based search mechanism for overt and covert shifts of visual attention. Vis.
Res. 40:1489–506
Jans B, Peters JC, De Weerd P. 2010. Visual spatial attention to multiple locations at once: The jury is still
out. Psychol. Rev. 117:637–82
Jiang YH, Kanwisher N. 2003. Common neural mechanisms for response selection and perceptual processing.
J. Cogn. Neurosci. 15:1095–110
Johansen-Berg H, Lloyd DM. 2000. The physiology and psychology of selective attention to touch. Front.
Biosci. 5:D894–904
Johnson MK. 1983. A multiple-entry, modular memory system. In The Psychology of Learning and Motivation:
Advances in Research and Theory , ed. GH Bower, pp. 81–123. New York: Academic
Johnson MK, Raye CL, Mitchell KJ, Greene EJ, Cunningham WA, Sanislow CA. 2005. Using fMRI to investi-
gate a component process of reﬂection: prefrontal correlates of refreshing a just-activated representation.
Cogn. Affect. Behav. Neurosci. 5:339–61
Johnson MK, Reeder JA, Raye CL, Mitchell KJ. 2002. Second thoughts versus second looks: an age-related
deﬁcit in reﬂectively refreshing just-activated information. Psychol. Sci. 13:64–67
Johnson MR, Mitchell KJ, Raye CL, D’Esposito M, Johnson MK. 2007. A brief thought can modulate activity
in extrastriate visual areas: top-down effects of refreshing just-seen visual stimuli. Neuroimage 37:290–99
Jolicoeur P. 1998. Modulation of the attentional blink by on-line response selection: evidence from speeded
and unspeeded task-sub-1 decisions. Mem. Cogn. 26:1014–32
Jolicoeur P. 1999. Restricted attentional capacity between sensory modalities. Psychonom. Bull. Rev. 6:87–92
Juan CH, Shorter-Jacobi SM, Schall JD. 2004. Dissociation of spatial attention and saccade preparation.Proc.
Natl. Acad. Sci. USA 101:15541–44
www.annualreviews.org • A Taxonomy of Attention 95
Annu. Rev. Psychol. 2011.62:73-101. Downloaded from www.annualreviews.org
by University of Minnesota - Twin Cities - Wilson Library on 05/13/11. For personal use only.

[p.24]
PS62CH04-Chun ARI 22 November 2010 9:23
Kahneman D, Treisman A, Gibbs BJ. 1992. The reviewing of object ﬁles: object-speciﬁc integration of
information. Cogn. Psychol. 24:175–219
Kamitani Y, Tong F. 2005. Decoding the visual and subjective contents of the human brain. Nat. Neurosci.
8:679–85
Kanwisher N, Wojciulik E. 2000. Visual attention: insights from brain imaging. Nat. Rev. Neurosci. 1:91–100
Kastner S, Pinsk MA, De Weerd P, Desimone R, Ungerleider LG. 1999. Increased activity in human visual
cortex during directed attention in the absence of visual stimulation. Neuron 22:751–61
Kim SY, Kim MS, Chun MM. 2005. Concurrent working memory load can reduce distraction. Proc. Natl.
Acad. Sci. USA 102:16524–29
Klein RM. 2000. Inhibition of return. Trends Cogn. Sci. 4:138–47
Koch C, Tsuchiya N. 2007. Attention and consciousness: two distinct brain processes.Trends Cogn. Sci. 11:16–
22
Kowler E, Anderson E, Dosher B, Blaser E. 1995. The role of attention in the programming of saccades.Vis.
Res. 35:1897–916
Kristj´ansson A, Nakayama K. 2002. The attentional blink in space and time. Vis. Res. 42:2039–50
Kristj´ansson AK, Campana G. 2010. Where perception meets memory: a review of repetition priming in visual
search tasks. Atten. Percept. Psychophys. 72:5–18
Kuhl BA, Dudukovic NM, Kahn I, Wagner AD. 2007. Decreased demands on cognitive control reveal the
neural processing beneﬁts of forgetting. Nat. Neurosci. 10:908–14
Lamme VAF. 2003. Why visual attention and awareness are different. Trends Cogn. Sci. 7:12–18
Lavie N. 1995. Perceptual load as a necessary condition for selective attention. J. Exp. Psychol.: Hum. Percept.
Perform. 21:451–68
Lavie N. 2005. Distracted and confused?: Selective attention under load. Trends Cogn. Sci. 9:75–82
Lavie N, Hirst A, de Fockert JW, Viding E. 2004. Load theory of selective attention and cognitive control.
J. Exp. Psychol.: Gen. 133:339–54
Leber AB. 2010. Neural predictors of within-subject ﬂuctuations in attentional control.J. Neurosci. 30:11458–
65
Leber AB, Turk-Browne NB, Chun MM. 2008. Neural predictors of moment-to-moment ﬂuctuations in
cognitive ﬂexibility. Proc. Natl. Acad. Sci. USA 105:13592–97
Lepsien J, Grifﬁn IC, Devlin JT, Nobre AC. 2005. Directing spatial attention in mental representations:
interactions between attentional orienting and working-memory load. Neuroimage 26:733–43
Levin DT, Simons DJ. 1997. Failure to detect changes to attended objects in motion pictures.Psychonom. Bull.
Rev. 4:501–6
Libera CD, Chelazzi L. 2006. Visual selective attention and the effects of monetary rewards. Psychol. Sci.
17:222–27
Lin JY, Franconeri S, Enns JT. 2008. Objects on a collision path with the observer demand attention.Psychol.
Sci. 19:686–92
Liu T, Larsson J, Carrasco M. 2007. Feature-based attention modulates orientation-selective responses in
human visual cortex. Neuron 55:313–23
Lleras A, Rensink RA, Enns JT. 2005. Rapid resumption of interrupted visual search. Psychol. Sci. 16:684–88
Logan GD, Gordon RD. 2001. Executive control of visual attention in dual-task situations. Psychol. Rev.
108:393–434
Luck SJ, Vogel EK. 1997. The capacity of visual working memory for features and conjunctions. Nature
390:279–84
Luck SJ, Vogel EK, Shapiro KL. 1996. Word meanings can be accessed but not reported during the attentional
blink. Nature 383:616–18
Lutz A, Slagter HA, Dunne JD, Davidson RJ. 2008. Attention regulation and monitoring in meditation.Trends
Cogn. Sci. 12:163–69
Macaluso E, Frith CD, Driver J. 2000. Modulation of human visual cortex by crossmodal spatial attention.
Science 289:1206–8
Maljkovic V, Nakayama K. 1994. Priming of pop-out: I. Role of features. Mem. Cogn. 22:657–72
Marois R, Chun MM, Gore JC. 2000. Neural correlates of the attentional blink. Neuron 28:299–308
96 Chun · Golomb ·Turk-Browne
Annu. Rev. Psychol. 2011.62:73-101. Downloaded from www.annualreviews.org
by University of Minnesota - Twin Cities - Wilson Library on 05/13/11. For personal use only.

[p.25]
PS62CH04-Chun ARI 22 November 2010 9:23
Marois R, Ivanoff J. 2005. Capacity limits of information processing in the brain.Trends Cogn. Sci. 9:296–305
Marois R, Yi DJ, Chun MM. 2004. The neural fate of consciously perceived and missed events in the attentional
blink. Neuron 41:465–72
Math ˆot S, Theeuwes J. 2011. Visual attention and stability. Phil. Trans. R. Soc. B. In press
Maunsell JHR. 2004. Neuronal representations of cognitive state: reward or attention? Trends Cogn. Sci.
8:261–65
McAdams CJ, Maunsell JHR. 1999. Effects of attention on the reliability of individual neurons in monkey
visual cortex. Neuron 23:765–73
McMains SA, Somers DC. 2004. Multiple spotlights of attentional selection in human visual cortex. Neuron
42:677–86
Melloni L, Molina C, Pena M, Torres D, Singer W, Rodriguez E. 2007. Synchronization of neural activity
across cortical areas correlates with conscious perception. J. Neurosci. 27:2858–65
Meyer DE, Kieras DE. 1997. A computational theory of executive cognitive processes and multiple-task
performance: Part 2. Accounts of psychological refractory-period phenomena. Psychol. Rev. 104:749–91
Miller EK, Cohen JD. 2001. An integrative theory of prefrontal cortex function.Annu. Rev. Neurosci. 24:167–
202
Miller GA. 1956. The magical number seven, plus or minus two: some limits on our capacity for processing
information. Psychol. Rev. 63:81–97
Mitchell JF, Stoner GR, Reynolds JH. 2004. Object-based attention determines dominance in binocular
rivalry. Nature 429:410–13
Mitchell JF, Sundberg KA, Reynolds JH. 2009. Spatial attention decorrelates intrinsic activity ﬂuctuations in
macaque area V4. Neuron 63:879–88
Miyake A, Friedman NP, Emerson MJ, Witzki AH, Howerter A, Wager TD. 2000. The unity and diversity
of executive functions and their contributions to complex “frontal lobe” tasks: a latent variable analysis.
Cogn. Psychol. 41:49–100
Monsell S. 2003. Task switching. Trends Cogn. Sci. 7:134–40
Moore T, Armstrong KM. 2003. Selective gating of visual signals by microstimulation of frontal cortex.Nature
421:370–73
Most SB, Scholl BJ, Clifford ER, Simons DJ. 2005. What you see is what you set: sustained inattentional
blindness and the capture of awareness. Psychol. Rev. 112:217–42
Najemnik J, Geisler WS. 2005. Optimal eye movement strategies in visual search. Nature 434:387–91
Nakayama K, Mackeben M. 1989. Sustained and transient components of focal visual attention. Vis. Res.
29:1631–47
Navon D. 1984. Resources—a theoretical soup stone. Psychol. Rev. 91:216–34
Nee DE, Wager TD, Jonides J. 2007. Interference resolution: insights from a meta-analysis of neuroimaging
tasks. Cogn. Affect. Behav. Neurosci. 7:1–17
New J, Cosmides L, Tooby J. 2007. Category-speciﬁc attention for animals reﬂects ancestral priorities, not
expertise. Proc. Natl. Acad. Sci. USA 104:16598–603
Nieuwenstein MR, Chun MM, Van Der Lubbe RHJ, Hooge ITC. 2005. Delayed attentional engagement in
the attentional blink. J. Exp. Psychol.: Hum. Percept. Perform. 31:1463–75
Nobre AC, Coull JT, Maquet P, Frith CD, Vandenberghe R, Mesulam MM. 2004. Orienting attention to
locations in perceptual versus mental representations. J. Cogn. Neurosci. 16:363–73
Norman KA, Newman EL, Detre G. 2007. A neural network model of retrieval-induced forgetting. Psychol.
Rev. 114:887–953
O’Craven KM, Downing PE, Kanwisher N. 1999. fMRI evidence for objects as the units of attentional
selection. Nature 401:584–87
O’Craven KM, Rosen BR, Kwong KK, Treisman A, Savoy RL. 1997. Voluntary attention modulates fMRI
activity in human MT-MST. Neuron 18:591–98
Ochsner KN, Bunge SA, Gross JJ, Gabrieli JDE. 2002. Rethinking feelings: an fMRI study of the cognitive
regulation of emotion. J. Cogn. Neurosci. 14:1215–29
Oh S, Kim M. 2004. The role of spatial working memory in visual search efﬁciency. Psychonom. Bull. Rev.
11:275–81
www.annualreviews.org • A Taxonomy of Attention 97
Annu. Rev. Psychol. 2011.62:73-101. Downloaded from www.annualreviews.org
by University of Minnesota - Twin Cities - Wilson Library on 05/13/11. For personal use only.

[p.26]
PS62CH04-Chun ARI 22 November 2010 9:23
Ohman A, Mineka S. 2001. Fears, phobias, and preparedness: toward an evolved module of fear and fear
learning. Psychol. Rev. 108:483–522
Olivers CNL, Meeter M. 2008. A boost and bounce theory of temporal attention. Psychol. Rev. 115:836–63
Olivers CNL, Nieuwenhuis S. 2005. The beneﬁcial effect of concurrent task-irrelevant mental activity on
temporal attention. Psychol. Sci. 16:265–69
Osipova D, Takashima A, Oostenveld R, Fern´andez G, Maris E, Jensen O. 2006. Theta and gamma oscillations
predict encoding and retrieval of declarative memory. J. Neurosci. 26:7523–31
Otten LJ, Henson RNA, Rugg MD. 2002. State-related and item-related neural correlates of successful
memory encoding. Nat. Neurosci. 5:1339–44
Parasuraman R. 1998. The attentive brain: issues and prospects. In T h eA t t e n t i v eB r a i n, ed. R Parasuraman,
pp. 3–15. Cambridge, MA: MIT Press
Park S, Kim MS, Chun MM. 2007. Concurrent working memory load can facilitate selective attention: evidence
for specialized load. J. Exp. Psychol.: Hum. Percept. Perform. 33:1062–75
Pashler H. 1994. Dual-task interference in simple tasks: data and theory. Psychol. Bull. 116:220–44
Pashler H, Johnston JC, Ruthruff E. 2001. Attention and performance. Annu. Rev. Psychol. 52:629–51
Pashler HE. 1998. The Psychology of Attention . Cambridge, MA: MIT Press
Pelli DG, Tillman KA. 2008. The uncrowded window of object recognition. Nat. Neurosci. 11:1129–35
Phelps EA, Ling S, Carrasco M. 2006. Emotion facilitates perception and potentiates the perceptual beneﬁts
of attention. Psychol. Sci. 17:292–99
Polyn SM, Natu VS, Cohen JD, Norman KA. 2005. Neuroscience: category-speciﬁc cortical activity precedes
retrieval during memory search. Science 310:1963–66
Posner MI, Snyder CRR, Davidson BJ. 1980. Attention and the detection of signals. J. Exp. Psychol.: Gen.
109:160–74
Potter MC. 1975. Meaning in visual search. Science 187:965–66
Potter MC, Banks BS, Muckenhoupt M, Chun MM. 1998. Two attentional deﬁcits in serial target search: the
visual attentional blink and an amodal task-switch deﬁcit. J. Exp. Psychol.: Learn. Mem. Cogn. 24:979–92
Pylyshyn ZW. 1989. The role of location indexes in spatial perception: a sketch of the FINST spatial-index
model. Cognition 32:65–97
Pylyshyn ZW, Storm RW. 1988. Tracking multiple independent targets: evidence for a parallel tracking
mechanism. Spat. Vis. 3:179–97
Raichle ME, MacLeod AM, Snyder AZ, Powers WJ, Gusnard DA, Shulman GL. 2001. A default mode of
brain function. Proc. Natl. Acad. Sci. USA 98:676–82
Ranganath C, Johnson MK, D’Esposito M. 2000. Left anterior prefrontal activation increases with demands
to recall speciﬁc perceptual information. J. Neurosci. 20:1–5
Raymond JE, Fenske MJ, Tavassoli NT. 2003. Selective attention determines emotional responses to novel
visual stimuli. Psychol. Sci. 14:537–42
Raymond JE, Shapiro KL, Arnell KM. 1992. Temporary suppression of visual processing in an RSVP task:
an attentional blink. J. Exp. Psychol.: Hum. Percept. Perform. 18:849–60
Rayner K. 2009. Eye movements and attention in reading, scene perception, and visual search. Q. J. Exp.
Psychol. 62:1457–506
Rees G, Frith CD, Lavie N. 1997. Modulating irrelevant motion perception by varying attentional load in an
unrelated task. Science 278:1616–19
Rees G, Kreiman G, Koch C. 2002. Neural correlates of consciousness in humans.Nat. Rev. Neurosci. 3:261–70
Rensink RA. 2000. The dynamic representation of scenes. Vis. Cogn. 7:17–42
Ress D, Heeger DJ. 2003. Neuronal correlates of perception in early visual cortex. Nat. Neurosci. 6:414–20
Reynolds JH, Chelazzi L. 2004. Attentional modulation of visual processing. Annu. Rev. Neurosci. 27:611–47
Ridderinkhof KR, Ullsperger M, Crone EA, Nieuwenhuis S. 2004. The role of the medial frontal cortex in
cognitive control. Science 306:443–47
Rogers RD, Monsell S. 1995. Costs of a predictable switch between simple cognitive tasks. J. Exp. Psychol.:
Gen. 124:207–31
Rossi AF, Bichot NP, Desimone R, Ungerleider LG. 2007. Top-down attentional deﬁcits in macaques with
lesions of lateral prefrontal cortex. J. Neurosci. 27:11306–14
98 Chun · Golomb ·Turk-Browne
Annu. Rev. Psychol. 2011.62:73-101. Downloaded from www.annualreviews.org
by University of Minnesota - Twin Cities - Wilson Library on 05/13/11. For personal use only.

[p.27]
PS62CH04-Chun ARI 22 November 2010 9:23
Rowe G, Hirsh JB, Anderson AK. 2007. Positive affect increases the breadth of attentional selection. Proc.
Natl. Acad. Sci. USA 104:383–88
Rowe JB, Toni I, Josephs O, Frackowiak RSJ, Passingham RE. 2000. The prefrontal cortex: response selection
or maintenance within working memory? Science 288:1656–60
Rushworth MFS, Hadland KA, Paus T, Sipila PK. 2002. Role of the human medial frontal cortex in task
switching: a combined fMRI and TMS study. J. Neurophysiol. 87:2577–92
Rushworth MFS, Paus T, Sipila PK. 2001. Attention systems and the organization of the human parietal
cortex. J. Neurosci. 21:5262–71
Saalmann YB, Pigarev IN, Vidyasagar TR. 2007. Neural mechanisms of visual attention: how top-down
feedback highlights relevant locations. Science 316:1612–15
Schacter DL, Tulving E. 1994. Memory Systems. Cambridge, MA: MIT Press
Schacter DL. 2001. The seven sins of memory: how the mind forgets and remembers. Boston, MA: Houghton
Mifﬂin
Schall JD, Thompson KG. 1999. Neural selection and control of visually guided eye movements. Annu. Rev.
Neurosci. 22:241–59
Schmidt NB, Richey JA, Buckner JD, Timpano KR. 2009. Attention training for generalized social anxiety
disorder. J. Abnorm. Psychol. 118:5–14
Scholl BJ. 2001. Objects and attention: the state of the art. Cognition 80:1–46
Scholl BJ, Xu YD. 2001. The magical number 4 in vision. Behav. Brain Sci. 24:145–46
Scholl BJ, Pylyshyn ZW. 1999. Tracking multiple items through occlusion: clues to visual objecthood. Cogn.
Psychol. 38:259–90
Schultz W. 2000. Multiple reward signals in the brain. Nat. Rev. Neurosci. 1:199–207
Serences JT. 2008. Value-based modulations in human visual cortex. Neuron 60:1169–81
Serences JT, Ester EF, Vogel EK, Awh E. 2009. Stimulus-speciﬁc delay activity in human primary visual
cortex. Psychol. Sci. 20:207–14
Sereno MI, Pitzalis S, Martinez A. 2001. Mapping of contralateral space in retinotopic coordinates by a parietal
cortical area in humans. Science 294:1350–54
Shapiro K, Driver J, Ward R, Sorensen RE. 1997. Priming from the attentional blink: a failure to extract visual
tokens but not visual types. Psychol. Sci. 8:95–100
Sharot T, Delgado MR, Phelps EA. 2004. How emotion enhances the feeling of remembering.Nat. Neurosci.
7:1376–80
Shomstein S, Behrmann M. 2006. Cortical systems mediating visual attention to both objects and spatial
locations. Proc. Natl. Acad. Sci. USA 103:11387–92
Shore DI, Klein RM. 2001. On the manifestations of memory in visual search. Spat. Vis. 14:59–75
Silver MA, Ress D, Heeger DJ. 2005. Topographic maps of visual spatial attention in human parietal cortex.
J. Neurophysiol. 94:1358–71
Simons DJ, Chabris CF. 1999. Gorillas in our midst: sustained inattentional blindness for dynamic events.
Perception 28:1059–74
Smith EE, Jonides J. 1999. Storage and executive processes in the frontal lobes. Science 283:1657–61
Sohn M-H, Ursu S, Anderson JR, Stenger VA, Carter CS. 2000. The role of prefrontal cortex and posterior
parietal cortex in task switching. Proc. Natl. Acad. Sci. USA 97:13448–53
Soto D, Heinke D, Humphreys GW, Blanco MJ. 2005. Early, involuntary top-down guidance of attention
from working memory. J. Exp. Psychol.: Hum. Percept. Perform. 31:248–61
Spence C, Nicholls MER, Gillespie N, Driver J. 1998. Cross-modal links in exogenous covert spatial orienting
between touch, audition, and vision. Percept. Psychophys. 60:544–57
Squire LR, Knowlton B, Musen G. 1993. The structure and organization of memory. Annu. Rev. Psychol.
44:453–95
Stokes M, Thompson R, Nobre AC, Duncan J. 2009. Shape-speciﬁc preparatory activity mediates attention
to targets in human visual cortex. Proc. Natl. Acad. Sci. USA 106:19569–74
Strayer DL, Johnston WA. 2001. Driven to distraction: dual-task studies of simulated driving and conversing
on a cellular telephone. Psychol. Sci. 12:462–66
Summerﬁeld JJ, Lepsien J, Gitelman DR, Mesulam MM, Nobre AC. 2006. Orienting attention based on
long-term memory experience. Neuron 49:905–16
www.annualreviews.org • A Taxonomy of Attention 99
Annu. Rev. Psychol. 2011.62:73-101. Downloaded from www.annualreviews.org
by University of Minnesota - Twin Cities - Wilson Library on 05/13/11. For personal use only.

[p.28]
PS62CH04-Chun ARI 22 November 2010 9:23
Tamm L, Menon V, Ringel J, Reiss AL. 2004. Event-related fMRI evidence of frontotemporal involvement in
aberrant response inhibition and task switching in attention-deﬁcit/hyperactivity disorder. J. Am. Acad.
Child. Adolesc. Psychiatry 43:1430–40
Theeuwes J. 2004. Top-down search strategies cannot override attentional capture. Psychonom. Bull. Rev.
11:65–70
Thorpe S, Fize D, Marlot C. 1996. Speed of processing in the human visual system. Nature 381:520–22
Todd JJ, Marois R. 2004. Capacity limit of visual short-term memory in human posterior parietal cortex.
Nature 428:751–54
Tootell RBH, Hadjikhani N, Hall EK, Marrett S, Vanduffel W, et al. 1998. The retinotopy of visual spatial
attention. Neuron 21:1409–22
Torralba A, Oliva A, Castelhano MS, Henderson JM. 2006. Contextual guidance of eye movements and
attention in real-world scenes: the role of global features in object search. Psychol. Rev. 113:766–86
Treisman AM. 1960. Contextual cues in selective listening. Q. J. Exp. Psychol. 12:242–48
Treisman AM, Gelade G. 1980. Feature-integration theory of attention. Cogn. Psychol. 12:97–136
Treue S, Mart´ınez Trujillo JC. 1999. Feature-based attention inﬂuences motion processing gain in macaque
visual cortex. Nature 399:575–79
Turk-Browne NB, Yi D-Y, Chun MM. 2006. Linking implicit and explicit memory: common encoding factors
and shared representations. Neuron 49:917–27
Veldhuizen MG, Bender G, Constable RT, Small DM. 2007. Trying to detect taste in a tasteless solution:
modulation of early gustatory cortex by attention to taste. Chem. Senses 32:569–81
Vickery TJ, Shim WM, Chakravarthi R, Jiang YV, Luedeman RL. 2010. Supercrowding: Weakly masking a
target greatly enhances crowding. J. Vis. 9(2):12
Vul E, Hanus D, Kanwisher N. 2008. Delay of selective attention during the attentional blink. Vision Res.
48:1902–9
Wager TD, Rilling JK, Smith EE, Sokolik A, Casey KL, et al. 2004. Placebo-induced changes in fMRI in the
anticipation and experience of pain. Science 303:1162–67
Wager TD, Smith EE. 2003. Neuroimaging studies of working memory: a meta-analysis.Cogn. Affect. Behav.
Neurosci. 3:255–74
Wagner AD, Schacter DL, Rotte M, Koutstaal W, Maril A, et al. 1998. Building memories: remembering and
forgetting of verbal experiences as predicted by brain activity. Science 281:1188–91
Wagner AD, Shannon BJ, Kahn I, Buckner RL. 2005. Parietal lobe contributions to episodic memory retrieval.
Trends Cogn. Sci. 9:445–53
Watson DG, Humphreys GW. 1997. Visual marking: prioritizing selection for new objects by top-down
attentional inhibition of old objects. Psychol. Rev. 104:90–122
Weichselgartner E, Sperling G. 1987. Dynamics of automatic and controlled visual attention.Science 238:778–
80
Weissman DH, Roberts KC, Visscher KM, Woldorff MG. 2006. The neural bases of momentary lapses in
attention. Nat. Neurosci. 9:971–78
Wojciulik E, Kanwisher N. 1999. The generality of parietal involvement in visual attention.Neuron 23:747–64
Wojciulik E, Kanwisher N, Driver J. 1998. Covert visual attention modulates face-speciﬁc activity in the
human fusiform gyrus: fMRI study. J. Neurophysiol. 79:1574–78
Woldorff MG, Gallen CC, Hampson SA, Hillyard SA, Pantev C, et al. 1993. Modulation of early sen-
sory processing in human auditory cortex during auditory selective attention. Proc. Natl. Acad. Sci. USA
90:8722–26
Wolfe JM, Horowitz TS. 2004. What attributes guide the deployment of visual attention and how do they do
it? Nat. Rev. Neurosci. 5:495–501
Wolfe JM, Horowitz TS, Kenner NM. 2005. Cognitive psychology: rare items often missed in visual searches.
Nature 435:439–40
Womelsdorf T, Fries P, Mitra PP, Desimone R. 2006. Gamma-band synchronization in visual cortex predicts
speed of change detection. Nature 439:733–36
Womelsdorf T, Schoffelen J-M, Oostenveld R, Singer W, Desimone R, et al. 2007. Modulation of neuronal
interactions through neuronal synchronization. Science 316:1609–12
100 Chun · Golomb ·Turk-Browne
Annu. Rev. Psychol. 2011.62:73-101. Downloaded from www.annualreviews.org
by University of Minnesota - Twin Cities - Wilson Library on 05/13/11. For personal use only.

[p.29]
PS62CH04-Chun ARI 22 November 2010 9:23
Woodman GF, Luck SJ. 2004. Visual search is slowed when visuospatial working memory is occupied. Psy-
chonom. Bull. Rev. 11:269–74
Woodman GF, Vogel EK, Luck SJ. 2001. Visual search remains efﬁcient when visual working memory is full.
Psychol. Sci. 12:219–24
Wyart V, Tallon-Baudry C. 2008. Neural dissociation between visual awareness and spatial attention.
J. Neurosci. 28:2667–79
Xu YD, Chun MM. 2006. Dissociable neural mechanisms supporting visual short-term memory for objects.
Nature 440:91–95
Xu YD, Chun MM. 2009. Selecting and perceiving multiple visual objects. Trends Cogn. Sci. 13:167–74
Yantis S, Egeth HE. 1999. On the distinction between visual salience and stimulus-driven attentional capture.
J. Exp. Psychol.: Hum. Percept. Perform. 25:661–76
Yantis S, Schwarzbach J, Serences JT, Carlson RL, Steinmetz MA, et al. 2002. Transient neural activity in
human parietal cortex during spatial attention shifts. Nat. Neurosci. 5:995–1002
Yantis S, Serences JT. 2003. Cortical mechanisms of space-based and object-based attentional control. Curr.
Opin. Neurobiol. 13:187–93
Yi D-J, Chun MM. 2005. Attentional modulation of learning-related repetition attenuation effects in human
parahippocampal cortex. J. Neurosci. 25:3593–600
Yi D-J, Turk-Browne NB, Chun MM, Johnson MK. 2008. When a thought equals a look: Refreshing enhances
perceptual memory. J. Cogn. Neurosci. 20:1371–80
Yi D-J, Woodman GF, Widders D, Marois P, Chun MM. 2004. Neural fate of ignored stimuli: dissociable
effects of perceptual and working memory load. Nat. Neurosci. 7:992–6
Zelano C, Bensaﬁ M, Porter J, Mainland J, Johnson B, et al. 2005. Attentional modulation in human primary
olfactory cortex. Nat. Neurosci. 8:114–20
www.annualreviews.org • A Taxonomy of Attention 101
Annu. Rev. Psychol. 2011.62:73-101. Downloaded from www.annualreviews.org
by University of Minnesota - Twin Cities - Wilson Library on 05/13/11. For personal use only.

[p.30]
PS62CH04-Chun ARI 22 November 2010 9:23
Figure 1
A schematic overview of external and internal attention. Each box represents a target of attention.
www.annualreviews.org • A Taxonomy of Attention C-1
Annu. Rev. Psychol. 2011.62:73-101. Downloaded from www.annualreviews.org
by University of Minnesota - Twin Cities - Wilson Library on 05/13/11. For personal use only.

[p.31]
PS62-FrontMatter ARI 15 November 2010 17:50
Annual Review of
Psychology
Volume 62, 2011 Contents
Prefatory
The Development of Problem Solving in Young Children:
A Critical Cognitive Skill
Rachel Keen pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp 1
Decision Making
The Neuroscience of Social Decision-Making
James K. Rilling and Alan G. Sanfey ppppppppppppppppppppppppppppppppppppppppppppppppppppppp 23
Speech Perception
Speech Perception
Arthur G. Samuel pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp 49
Attention and Performance
A Taxonomy of External and Internal Attention
Marvin M. Chun, Julie D. Golomb, and Nicholas B. Turk-Browne pppppppppppppppppppppp 73
Language Processing
The Neural Bases of Social Cognition and Story Comprehension
Raymond A. Mar ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp 103
Reasoning and Problem Solving
Causal Learning and Inference as a Rational Process:
The New Synthesis
Keith J. Holyoak and Patricia W. Cheng ppppppppppppppppppppppppppppppppppppppppppppppppp 135
Emotional, Social, and Personality Development
Development in the Early Years: Socialization, Motor Development,
and Consciousness
Claire B. Kopp pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp 165
Peer Contagion in Child and Adolescent Social
and Emotional Development
Thomas J. Dishion and Jessica M. Tipsord pppppppppppppppppppppppppppppppppppppppppppppppp 189
vi
Annu. Rev. Psychol. 2011.62:73-101. Downloaded from www.annualreviews.org
by University of Minnesota - Twin Cities - Wilson Library on 05/13/11. For personal use only.

[p.32]
PS62-FrontMatter ARI 15 November 2010 17:50
Adulthood and Aging
Psychological Wisdom Research: Commonalities and Differences in a
Growing Field
Ursula M. Staudinger and Judith Gl¨uck ppppppppppppppppppppppppppppppppppppppppppppppppp 215
Development in the Family
Socialization Processes in the Family: Social and
Emotional Development
Joan E. Grusec pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp 243
Psychopathology
Delusional Belief
Max Coltheart, Robyn Langdon, and Ryan McKay ppppppppppppppppppppppppppppppppppppppp 271
Therapy for Speciﬁc Problems
Long-Term Impact of Prevention Programs to Promote Effective
Parenting: Lasting Effects but Uncertain Processes
Irwin N. Sandler, Erin N. Schoenfelder, Sharlene A. Wolchik,
and David P. MacKinnon pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp 299
Self and Identity
Do Conscious Thoughts Cause Behavior?
Roy F. Baumeister, E.J. Masicampo, and Kathleen D. Vohs ppppppppppppppppppppppppppppp 331
Neuroscience of Self and Self-Regulation
Todd F. Heatherton ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp 363
Attitude Change and Persuasion
Attitudes and Attitude Change
Gerd Bohner and Nina Dickel ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp 391
Cross-Country or Regional Comparisons
Culture, Mind, and the Brain: Current Evidence and Future Directions
Shinobu Kitayama and Ayse K. Uskul ppppppppppppppppppppppppppppppppppppppppppppppppppppp 419
Cognition in Organizations
Heuristic Decision Making
Gerd Gigerenzer and Wolfgang Gaissmaier pppppppppppppppppppppppppppppppppppppppppppppp 451
Structures and Goals of Educational Settings
Early Care, Education, and Child Development
Deborah A. Phillips and Amy E. Lowenstein pppppppppppppppppppppppppppppppppppppppppppppp 483
Contents vii
Annu. Rev. Psychol. 2011.62:73-101. Downloaded from www.annualreviews.org
by University of Minnesota - Twin Cities - Wilson Library on 05/13/11. For personal use only.

[p.33]
PS62-FrontMatter ARI 3 November 2010 10:34
Psychophysiological Disorders and Psychological Dimensions
on Medical Disorders
Psychological Perspectives on Pathways Linking Socioeconomic Status
and Physical Health
Karen A. Matthews and Linda C. Gallo pppppppppppppppppppppppppppppppppppppppppppppppppp 501
Psychological Science on Pregnancy: Stress Processes, Biopsychosocial
Models, and Emerging Research Issues
Christine Dunkel Schetter pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp 531
Research Methodology
The Development of Autobiographical Memory
Robyn Fivush pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp 559
The Disaggregation of Within-Person and Between-Person Effects in
Longitudinal Models of Change
Patrick J. Curran and Daniel J. Bauer ppppppppppppppppppppppppppppppppppppppppppppppppppp 583
Thirty Years and Counting: Finding Meaning in the N400
Component of the Event-Related Brain Potential (ERP)
Marta Kutas and Kara D. Federmeier pppppppppppppppppppppppppppppppppppppppppppppppppppp 621
Indexes
Cumulative Index of Contributing Authors, Volumes 52–62 ppppppppppppppppppppppppppp 000
Cumulative Index of Chapter Titles, Volumes 52–62 ppppppppppppppppppppppppppppppppppp 000
Errata
An online log of corrections to Annual Review of Psychology articles may be found at
http://psych.AnnualReviews.org/errata.shtml
viii Contents
Annu. Rev. Psychol. 2011.62:73-101. Downloaded from www.annualreviews.org
by University of Minnesota - Twin Cities - Wilson Library on 05/13/11. For personal use only.
