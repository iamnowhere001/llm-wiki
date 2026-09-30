---
title: "Putting brain training to the test（把脑训练拿去检验：11,430 人的六周在线实验）"
author: Adrian M. Owen、Adam Hampshire、Jessica A. Grahn、Robert Stenton、Said Dajani、Alistair S. Burns、Robert J. Howard、Clive G. Ballard（八人署名完整；MRC 认知与脑科学部（剑桥）/ 伦敦国王学院精神病学研究所 / 曼彻斯特大学精神病学系）
url: https://www.nature.com/articles/nature09042
kind: paper
series: 无
published: 2010（Nature, 465(7299):775–778，2010-06-10；DOI 10.1038/nature09042；PMC 存档版 2010-12-10）
clipped: 2026-09-29
capture_quality: high
capture_method: >
  2026-09-29 从 PMC 开放获取全文抓取 HTML 转文本
  （https://pmc.ncbi.nlm.nih.gov/articles/PMC2884087/；PMCID PMC2884087 / EMSID UKMS29457 / PMID 20407435）。
  **本份是 PMC 存档的「作者稿」（author manuscript），不是 Nature 印刷版。**
  页内自述：「Nature. Author manuscript; available in PMC: 2010 Dec 10. Published in final edited form as:
  Nature. 2010 Jun 10;465(7299):775–778.」

  ⚠️ **同一内容存在多个载体**（PMC 作者稿 / Nature 印刷版 / 补充材料 PDF）——
  措辞与图表编号可能不同。**引用本份时只能引本份的话**，不得把 Nature 印刷版的表述记在本份账上。
  （同族坑见库内 [[2026-09-27-mcraven-make-your-bed-speech]] 的「演讲版 vs 成书版」。）

  抓取路径：`curl --http1.1` 取 HTML（177,947 字节）→ python 正则切出
  `<section class="body main-article-body">` 至「Similar articles」之前的正文区 →
  保留 h2/h3 标题层级与段落边界 → 去标签、解实体。
  **未使用 PDF 提取** —— PMC 的 PDF 链接（/articles/PMC2884087/pdf/ukmss-29457.pdf）对非浏览器请求
  返回 HTML 拦截页（实测两次，带浏览器 UA 与 Referer 均无效）；
  出版方 Nature 的 PDF（nature.com/articles/nature09042.pdf）为付费墙；作者实验室页的 PDF 链接已失效。
  另一条已试且失败的路径：Europe PMC 的 fullTextXML（HTTP 503）、NCBI 的 OA 打包服务（HTTP 404）。

  转出结果：**残留 HTML 标签 0、未解码实体 0**（python 正则核过，非肉眼）。
  已剔除的页面外壳（导航栏、作者检索链接、相关文章、Supplementary 文件清单、页脚）不属论文内容。

  已知缺失（四条）——
  1. **无页码坐标系。** HTML 无页边界，故本份不分 [p.N]，行号一律用文件绝对行号。
  2. **表格结构已失真。** Table 1–3 为数值表，HTML 转文本后单元格边界丢失（行内数字仍保留），
     要查表内数值须回 HTML 原文或 Nature 印刷版。
  3. **图只有图注。** Figure 1 / Figure 2 的图注文字在，图内数据点不在。
  4. **参考文献编号是上标数字形式**（如 `industry1`、`disease6-12`），HTML 里原本是 `<a>` 链接，
     转文本后编号与正文词粘连，**引用具体文献前须回原文核对该编号对应哪一条**。
capture_note: >
  **本字段只记「抓取事实」，不记「阅读结论」。**
  本素材的分层、关键要点、与库内已有主张的比对结果一律维护在
  wiki/sources/2026-09-29-brain-training-owen2010.md —— 它们随阅读深入而变，
  而本文件不可变，写在这里必然产生死结。**本文件不维护任何行区间。**

  行区间坐标系为**文件绝对行号**（`wc -l` 的坐标系）。正文行号 = 文件行号 − frontmatter 行数。
  引用前回文件核对。

  **素材性质**：同行评议期刊的原始实证研究（Nature Brief Communication），八作者署名完整，
  **无转述层、无 AI 加工痕迹**。本份在库内的位置是**反方证据** ——
  它检验的正是「认知/注意力可以被训练改善」这一类主张，结论为**否**（无迁移效应）。
  按 kind 取值表记为 `paper`。

  **利益披露**：原文脚注自陈「None of the authors has any competing interest.」。
  **这是作者自陈，本库未做独立核实。**
  **但需另记一条关系**：本研究的被试来自 BBC 科普节目《Bang Goes The Theory》的观众，
  由 BBC 网站承载训练与测评 —— 这是**样本来源**，不是商业利益，但它决定了样本是
  「自愿参与的电视观众」而非一般人群。此点写在 sources 页，不在本文件下判断。

  **版权性质**：Nature / Macmillan 出版。本文件以个人研究用途存档于本地 raw/，不对外发布。
---
## Abstract

‘Brain training’, or the quest for improved cognitive function through the regular use of computerised tests, is a multimillion pound industry1, yet scientific evidence to support its efficacy is lacking. Modest effects have been reported in some studies of older individuals2,3 and preschool children4, and video gamers out perform non-gamers on some tests of visual attention5. However, the widely held belief that commercially available computerised brain trainers improve general cognitive function in the wider population lacks empirical support. The central question is not whether performance on cognitive tests can be improved by training, but rather, whether those benefits transfer to other untrained tasks or lead to any general improvement in the level of cognitive functioning. Here we report the results of a six-week online study in which 11,430 participants trained several times each week on cognitive tasks designed to improve reasoning, memory, planning, visuospatial skills and attention. Although improvements were observed in every one of the cognitive tasks that were trained, no evidence was found for transfer effects to untrained tasks, even when those tasks were cognitively closely related.

To investigate whether regular brain training leads to any improvement in cognitive function, viewers of the BBC popular science programme ‘Bang Goes The Theory’ participated in a six-week online study of brain training. An initial ‘benchmarking’ assessment included a broad neuropsychological battery of four tests that are sensitive to changes in cognitive function in health and disease6-12. Specifically, baseline measures of reasoning6, verbal short-term memory (VSTM)7,12, spatial working memory (SWM)8-10, and paired-associates learning (PAL)11,13, were acquired. Participants were then randomly assigned to one of two experimental groups or a third control group and logged on to the BBC website to practise six training tasks for a minimum of 10 minutes a day, three times a week. In Experimental group 1, the six training tasks emphasised reasoning, planning and problem-solving abilities. In Experimental group 2, a broader range of cognitive functions was trained using tests of short-term memory, attention, visuospatial processing and mathematics similar to those commonly found in commercially available brain training devices. The difficulty of the training tasks increased as the participants improved to continuously challenge their cognitive performance and maximise any benefits of training. The control group did not formally practise any specific cognitive tasks during their ‘training’ sessions, but answered obscure questions from six different categories using any available online resource. At six weeks, the benchmarking assessment was repeated and the pre- and post-training scores were compared. The difference in benchmarking scores provided the measure of generalised cognitive improvement resulting from training. Similarly, for each training task, the first and last scores were compared to give a measure of specific improvement on that task.

Of 52,617 participants aged 18 to 60 who initially registered, 11,430 completed both benchmarking assessments and at least two full training sessions during the six-week period. On average, participants completed 24.47 (sd=16.95) training sessions (range = 1 to 188 sessions). The three groups were well matched in age (39.14 [11.91], 39.65 [11.83], 40.51 [11.79], respectively), and gender (F/M=5.5:1, 5.6:1 and 4.3:1, respectively).

Numerically, Experimental group 1 improved on four benchmarking tests and Experimental group 2 improved on three benchmarking tests (Figure 1), with standardised effect sizes varying from small (e.g. 0.35; 99% Confidence Interval [CI], 0.29-0.41) to very small (e.g. 0.01; 99% CI, −0.05-0.07). However, the control group also improved numerically on all four tests with similar effect sizes (Table 1). When the three groups were compared directly, effect sizes across all four benchmarking tests were very small (e.g. 0.01; 99% CI, −0.05-0.07 to 0.22; 99% CI, 0.15-0.28) (Table 2). In fact, for VSTM and PAL, the difference between benchmarking sessions was numerically greatest for the control group (Figure 1, Table 1 and Table 2). These results suggest an equivalent and marginal test-retest practice effect in all groups across all four tasks (Table 1). In contrast, the improvement on the tests that were actually trained was convincing across all tasks for both experimental groups. For example, for the tasks practised by Experimental group 1, differences were observed with large effect sizes of between 0.73; 99% CI, 0.68-0.79 and 1.63; 99% CI, 1.57-1.7 (Table 3 and Figure 2). Using Cohen’s14 notion that 0.2 represents a small effect, 0.5 a medium effect and 0.8 a large effect, even the smallest of these improvements would be considered large. Similarly, for Experimental group 2, large improvements were observed on all training tasks, with effect sizes of between 0.72; 99% CI, 0.67-0.78 and 0.97; 99% CI, 0.91-1.03 (Table 3 and Figure 2). Numerically, the control group also improved in their ability to answer obscure knowledge questions, although the effect size was small (0.33; 99% CI, 0.26-0.4) (Table 3 and Figure 2). In all three groups, whether these improvements reflected the simple effects of task repetition (i.e. practise), the adoption of new task strategies, or a combination of the two is unclear, but whatever the process effecting change, it did not generalise to the untrained benchmarking tests.

## Figure 1.

Open in a new tab

Benchmarking scores at baseline and after six weeks of training across the three groups of participants. VSTM = Verbal short-term memory, SWM = Spatial working memory, PAL = Paired-associates learning. Bars represent standard deviations.

## Table 1.

Within-test standardised effect sizes for changes in performance between pre-training and post-training benchmarking sessions

Exp group 1
Exp group 2
Control group

Reasoning

Mean difference
1.73
1.97
0.90

Effect size
0.31
0.35
0.16

99% CI
(0.26 - 0.36)
(0.29 - 0.41)
(0.09 - 0.23)

VSTM

Mean difference
0.15
0.03
0.22

Effect size
0.16
0.03
0.21

99% CI
(0.11 - 0.21)
(−0.02 - 0.09)
(0.14 - 0.28)

SWM

Mean difference
0.33
0.35
0.27

Effect size
0.24
0.27
0.19

99% CI
(0.19 - 0.29)
(0.21 - 0.33)
(0.12 - 0.26)

PAL

Mean difference
0.06
−0.01
0.07

Effect size
0.10
0.01
0.11

99% CI
(0.05 - 0.16)
(−0.05 - 0.07)
(0.04 - 0.18)

Open in a new tab

VSTM = Verbal short-term memory, SWM = Spatial working memory, PAL = Paired-associates learning. CI = confidence interval.

## Table 2.

Between-group standardised effect sizes for differences in performance between pre-training and post-training benchmarking sessions

Exp group 1 vs
Exp group 2
Exp group 1 vs
Control group
Exp group 2 vs
Control group

Reasoning

Mean difference
−0.231
0.831
1.062

Effect size
0.05
0.17
0.22

99% CI
(−0.01 – 0.1)
(0.1 – 0.23)
(0.15 – 0.28)

VSTM

Mean difference
0.130
−0.056
−0.186

Effect size
0.13
0.05
0.18

99% CI
(0.07 – 0.18)
(−0.01 – 0.12)
(0.11 – 0.24)

SWM

Mean difference
−0.028
0.057
0.085

Effect size
0.02
0.04
0.06

99% CI
(−0.04 – 0.07)
(−0.03 – 0.1)
(−0.01 – 0.12)

PAL

Mean difference
0.117
−0.012
−0.129

Effect size
0.10
0.01
0.11

99% CI
(0.04 – 0.15)
(−0.05 – 0.07)
(0.04 – 0.17)

Open in a new tab

VSTM = Verbal short-term Memory, SWM = Spatial working memory, PAL = Paired-associates learning. CI = confidence interval.

## Table 3.

Within-test standardised effect sizes for differences in performance between the first and the last training or control sessions

Test
Mean difference
Effect size
99% CI

Experimental

group 1

Reasoning 1
33.96
1.63
(1.57 - 1.7)

Reasoning 2
13.45
1.03
(0.98 - 1.09)

Reasoning 3
11.45
1.25
(1.19 - 1.31)

Planning 1
15.17
1.28
(1.23 - 1.34)

Planning 2
14.42
1.10
(1.05 - 1.16)

Planning 3
10.41
0.73
(0.68 - 0.79)

Experimental

group 2

Maths
18.15
0.90
(0.84 - 0.96)

Visuospatial
8.62
0.95
(0.89 - 1.02)

Attention 1
9.71
0.93
(0.87 - 0.99)

Attention 2
8.48
0.84
(0.78 - 0.9)

Memory 1
7.29
0.72
(0.67 - 0.78)

Memory 2
5.30
0.97
(0.91 - 1.03)

Control group

Questions
3.62
0.33
(0.26 - 0.40)

Open in a new tab

For description of tests, see Methods.

## Figure 2.

Open in a new tab

First and last training scores for the six tests used to train Experimental group 1 and Experimental group 2. The first and last scores for the control group are also shown. Bars represent standard deviations.

The relationship between the number of training sessions and changes in benchmark performance was negligible in all groups for all tests (largest Spearman’s rho = 0.059; Supplementary Figure 1). The effect of age was also negligible (largest Spearman’s rho = −0.073). Only two tests showed a significant effect of gender (PAL in Experimental group 1 and VSTM in Experimental group 2), but the effect sizes were very small (0.09; 99% CI, −0.01-0.2 and 0.09; 99% CI, −0.03-0.2, respectively).

These results provide no evidence for any generalised improvements in cognitive function following ‘brain training’ in a large sample of healthy adults. This was true for both the ‘general cognitive training’ group (Experimental group 2) who practised tests of memory, attention, visuospatial processing and mathematics similar to many of those found in commercial brain trainers, and for a more focused training group (Experimental group 1) who practised tests of reasoning, planning and problem solving. Indeed, both groups provided evidence that training-related improvements may not even generalise to other tasks that tap similar cognitive functions. For example, three of the tests practised by Experimental group 1 (Reasoning 1, 2 & 3) specifically emphasised abstract reasoning abilities, yet numerically larger changes on the benchmarking test that also required abstract reasoning were observed in Experimental group 2, who were not trained on any test that specifically emphasised reasoning. Similarly, of all the trained tasks, Memory 2 (based on the classic parlour game in which players have to remember the locations of objects on cards), is most closely related to the PAL benchmarking task (in which participants also have to remember the locations of objects), yet numerically, PAL performance actually deteriorated in the experimental group that trained on the Memory 2 task (Figure 1).

Could it be that no generalised effects of brain training were observed because the wrong types of cognitive tasks were used? This is unlikely because twelve different tests, covering a broad range of cognitive functions, were trained in this study. In addition, the six training tasks that emphasised abstract reasoning, planning and problem solving were included specifically because such tasks are known to correlate highly with measures of general fluid intelligence or ‘g’15-17, and were therefore most likely to produce an improvement in the general level of cognitive functioning. Indeed, functional neuroimaging studies have revealed clear overlap in frontal and parietal regions between similar tests of reasoning and planning to those used here15,17-19 and tests that are specifically designed to measure ‘g’15,20, while damage to the frontal lobe impairs performance on both types of task10,16,21.

Could it be that the benchmarking tests were insensitive to the generalised effects of brain training? This is also unlikely because the benchmarking tests were chosen for their known sensitivity to small changes in cognitive function in disease or following low-dose neuropharmacological interventions in healthy volunteers. For example, the SWM task is sensitive to damage to the frontal cortex10,22 and impairments are observed in patients with Parkinson’s disease23. On the other hand, low dose methylphenidate improves performance on the same task in healthy volunteers8,9. Similarly, the PAL task is highly sensitive to various neuropathological conditions, including Alzheimer’s disease11, Parkinson’s disease13 and schizophrenia24, while the alpha 2-agonists guanfacine and clonidine improve performance in healthy volunteers25.

Could it be that improvements in the experimental groups were ‘masked’ by the direct comparison with the control group, who were, arguably, also exercising attention, planning and visuospatial processes? This seems unlikely because there was a clear difference between the substantial improvements in both experimental groups across all trained tasks and the very modest improvement observed in the control group on their obscure knowledge test, suggesting that the experimental groups did benefit more from their training programmes, albeit only on the tasks that were actually being trained. In any case, in all three groups the standardised effect sizes of the transfer effects were, at best, small (Table 1), suggesting that any comparison (even with a control group who did nothing) would have yielded a negligible brain training effect in the Experimental groups.

Could it be that the amount of practise was insufficient to produce a measureable transfer effect of brain training? Given the known sensitivity of the benchmarking tests8-11,13,22-26, it seems reasonable to expect that 25 training sessions would yield a measurable group effect if one was present. More directly however, there was a negligible correlation between the number of training sessions and improvement in benchmarking scores (despite a strong correlation with improvement on training tasks - Supplementary Figure 2), confirming that the amount of practise was unrelated to any generalised brain training effect. That said, the possibility that an even more extensive training regime may have eventually produced an effect cannot be excluded.

To illustrate the size of the transfer effects observed in this study, consider the following representative example from the data. The increase in the number of digits that could be remembered following training on tests designed, at least in part, to improve memory (e.g., in Experimental group 2) was three hundredths of a digit. Assuming a linear relationship between time spent training and improvement, it would take almost four years of training to remember one extra digit. Moreover, the control group improved by two tenths of a digit, with no formal memory training at all.

In short, these results provide no evidence to support the widely held belief that the regular use of computerised brain trainers improves general cognitive functioning in healthy participants beyond those tasks that are actually being trained. Although we cannot exclude the possibility that more focused approaches, such as face-to-face cognitive training2, may be beneficial in some circumstances, these results confirm that six weeks of regular computerised brain training confers no greater benefit than simply answering general knowledge questions using the internet.

## Supplementary Material

1

NIHMS29457-supplement-1.pdf (596.5KB, pdf)

2

NIHMS29457-supplement-2.pdf (989.4KB, pdf)

3

NIHMS29457-supplement-3.pdf (544.5KB, pdf)

4

Supplementary Figure 1. The strongest relationship between number of sessions spent training over six weeks and change in benchmarking performance was observed in Experimental group 2 for the Reasoning test (Spearman’s rho = 0.059). This test is known to correlate with measures of general intelligence or g6, confirming that, at best, six weeks of brain training has a negligible transfer effect on general measures of cognitive function.

Supplementary Figure 2. An illustration of the relationship between number of sessions spent training over six weeks and change in performance (last training score – first training score) on one of the trained tasks (Reasoning 1) in Experimental group 1. A significant correlation was observed (Spearman’s rho = 0.52), confirming that the degree of improvement on this test correlates highly with the number of sessions spent training.

NIHMS29457-supplement-4.pdf (134KB, pdf)

## Acknowledgements

A.M.O., A.H. and J.A.G. are supported by the Medical Research Council (U.1055.01.002.00001.01 and U.1055.01.003.00001.01). C.G.B. and S.D. are supported by the Alzheimer’s Society (UK), who also funded key components of the study including data capture/extraction and components of recruitment. We thank Kathy Neal and Jimmy Tidey of the BBC Media Centre for their enormous contributions to the website and task design, data acquisition and project co-ordination.

## Appendix

### Methods

Participants

Of 11,430 participants who met the inclusion criteria, 4678 were randomly assigned to Experimental group 1, 4014 to Experimental group 2 and 2738 participants to the control group. The relatively reduced number of participants in the control group reflects a greater drop out between the pre-training and post-training benchmarking sessions in this group (equal numbers were assigned to each group at the point of registration), suggesting, perhaps, that the control tasks were less engaging overall than the training tasks. The participants in Experimental group 1 completed an average of 28.39 (sd=19.86) training sessions, compared with 23.86 (15.66) in Experimental group 2 and 18.66 (12.87) in the control group. The latter result suggests, again, that the control group’s task was less engaging than the specific training tasks given to the two experimental groups. In order that ‘first’ and ‘last’ scores for performance on the training sessions and the control task could be calculated without error, participants who did not complete at least two training or control sessions between the two benchmarking assessments were excluded from the analysis.Task Design

All three groups were given the same four benchmarking tests twice, once after registering for the trial, but before being shown the training or control tasks, and again six weeks later, irrespective of how many training or control sessions they had chosen to complete in between (subject to the caveat above). The four tests were adapted from a battery of publicly available cognitive assessment tools designed and validated at the Medical Research Council Cognition and Brain Sciences Unit (by A.H. and A.M.O) and made freely available at cambridgebrainsciences.com. The first test (Reasoning) was based on a grammatical reasoning test that has been shown to correlate with measures of general intelligence or g6. The participants had to determine, as quickly as possible, whether grammatical statements (e.g. the circle is not smaller than the square) about a presented picture (a large square and a smaller circle) were correct or incorrect and to complete as many trials as possible within 90 seconds. The outcome measure was the total number of trials answered correctly in 90 seconds, minus the number answered incorrectly. The second test (verbal short-term memory - VSTM) was a computerised version of the ‘digit span’ task which has been widely used in the neuropsychological literature and in many commercially available brain training devices to assess how many digits a participant can remember in sequence. The version used here was based on the ‘ratchet-style’ approach27 in which each successful trial is followed by a new sequence that is one digit longer than the last and each unsuccessful trial is followed by a new sequence that is one digit shorter than the last. In this way, an accurate estimate of digit span can made over a relatively short time period. The main outcome measure, average digit span, was the average number of digits in all successfully completed trials. Participants were allowed to make three errors in total before the test was terminated. Versions of the third task (spatial working memory – SWM) have been widely used in the human and animal working memory literature to assess spatial working memory abilities8-11,22,28-29. The version used here10 required participants to ‘search through’ a series of boxes presented on the screen to find a hidden ‘star’. Once found, the next star was hidden and participants had to begin a new search, remembering that a star would never be hidden in the same box twice. Participants were allowed to make three errors in total before the test was terminated. The main outcome measure was the average number of boxes in the successfully completed trials. The final test (paired associates learning - PAL), was based on a task that has been widely used in the assessment of cognitive deterioration in Alzheimer’s disease and related neurodegenerative conditions11,26. A series of ‘window shutters’ opened up on the screen to reveal a picture of a different object in each window (e.g. a hat or a ball). At the end of each sequence, the participants were shown a series of objects, one at a time, and had to select the correct window for each object. The version used here employed a ‘ratchet-style’ approach in which each completely successful trial was followed by a new trial involving one more window than the last and each unsuccessful trial was followed by a new trial involving one less window than the last. Participants were allowed to make three errors in total before the test was terminated. The main outcome measure was the average number of correct object-place associations (’paired associates’) in the trials that were successfully completed.

During the six-week training period the first experimental group were trained on six reasoning, planning and problem-solving tasks. In the first task (Reasoning 1), the participants had to use weight relationships, implied by the position of two seesaws with objects at each end, to select the heaviest object from a choice of three presented below. In the second task (Reasoning 2), the objective was to select the ‘odd one out’ from four shapes that varied in terms of colour, shape and solidity (filled/unfilled). In the third task (Reasoning 3), the participants had to move crates from a pile, each move being made with reference to the effect that it would have on the overall pattern of crates and how the result would affect future moves. In the fourth task (Planning 1), the objective was to draw a single continuous line around a grid, planning ahead such that current moves did not hinder later moves. In the fifth task (Planning 2), the participants had to move objects around between three jars until their positions matched a ‘goal’ arrangement of objects in three reference jars. In the sixth task (Planning 3), the objective was to slide numbered ‘tiles’ around on a grid to arrange them into the correct numerical order. In all three reasoning tasks and in Planning 2, each training session consisted of two ‘runs’ of 90 seconds and the main outcome measure was the total number of correct trials across the two runs. For Planning 1 and 3, the main outcome measure was the number of problems completed in 3 minutes.

During the six-week training period the second experimental group were trained on six tests of memory, attention, visuospatial processing and mathematical calculations. In the first task (Maths), the participants had to complete simple math sums (e.g. 17-9) as quickly as possible. In the second task (Visuospatial), the objective was to find the missing piece from a jigsaw puzzle by selecting from six alternatives. In the third task (Attention 1), symbols (e.g. blue stars) would appear rapidly and the participants were required to click on each symbol as quickly as possible, but only if it matched one of the ‘target’ symbols presented at the top of the screen. In the fourth task (Attention 2), the participants were shown a series of slowly moving, rotating, numbers. The objective was to select the numbers in order from the lowest to the highest. In the fifth task (Memory 1), the participants were shown a sequence of items of baggage moving down a conveyer belt towards an airport x-ray machine. The number of bags going in did not equal the number of bags coming out. After a short period the conveyor belt stopped and the participant had to respond with how many bags were left in the x-ray machine. In the sixth task (Memory 2), the participant was shown a set of cards and asked to remember the picture on each. The cards were then are flipped over and the user had to identify pairs of cards with identical objects on them. For all of these tasks, except Memory 1, each training session consisted of two ‘runs’ of 90 seconds each and the main outcome measure was the total number of correct trials across the two runs. For Memory 1, the main outcome measure was the number of problems completed in 3 minutes.

In each session, the control group were asked five obscure knowledge questions (e.g. What year did Henry VIII die?) from one of six general categories (population, history, duration, pop music, miscellaneous numbers and distance) and were asked to place answers in correct chronological order using any available online resource. Each session comprised three sets of five questions and 15 points were awarded for each answer in the correct chronological order.Data Analysis

The main outcome measures were the difference scores (post-training minus pre-training) for the four benchmarking tests in the two experimental groups and the control group in the ‘intention to treat’ population (i.e. those who completed baseline and six-week benchmarking assessments). Comparisons were then made between each of the experimental groups and the control group and between the two experimental groups themselves (Table 2 and Figure 1). Changes on the training test performance were also calculated by comparing the scores from the first training session with the scores from the final training session.

With such large sample sizes, statistical significance is easily reached, even when actual effect sizes are miniscule, making any numerical differences between two groups very difficult to interpret (as an example, the greater change in VSTM performance in the control group relative to both of the experimental groups is statistically significant, yet is counter to any reasonable hypothesis about brain training and, therefore, has no clear theoretical interpretation). To overcome this problem, the size of any observed differences was quantified by reporting effect sizes together with estimates of the likely margin of error (99% confidence intervals), for all comparisons between groups. Effect sizes provide a measure of the ‘meaningfulness’ of an effect, with 0.2 being generally taken to represent a ‘small’ effect, 0.5 a ‘medium’ effect and 0.8 a ‘large’ effect14. Thus, effect size quantifies the size of the difference between two groups, and may therefore be said to be a true measure of the significance of the difference.

### References

27.Bor D, Duncan J, Lee ACH, Parr A, Owen AM. Frontal Lobe Involvement In Spatial Span: Converging Studies Of Normal And Impaired Function. Neuropsychologia. 2005;44:229–237. doi: 10.1016/j.neuropsychologia.2005.05.010. [DOI] [PubMed] [Google Scholar]

28.Olton DS. In: Spatial Abilities. Potegal M, editor. Academic Press; New York: 1982. pp. 325–360. [Google Scholar]

29.Passingham R. Memory of monkeys (Macaca mulatta) with lesions in prefrontal cortex. Behavioral Neuroscience. 1985;99:3–21. doi: 10.1037//0735-7044.99.1.3. [DOI] [PubMed] [Google Scholar]

## Footnotes

None of the authors has any competing interest.

## References

1.Aamodt S, Wang A. Exercise on the Brain. The New York Times. [accessed January 20th, 2010]. 2007. http://www.nytimes.com/2007/11/08/opinion/08aamodt.html?_r=1.

2.Papp KV, Walsh SJ, Snyder PJ. Immediate and delayed effects of cognitive interventions in healthy elderly: a review of current literature and future directions. Alzheimers Dement. 2009;5:50–60. doi: 10.1016/j.jalz.2008.10.008. [DOI] [PubMed] [Google Scholar]

3.Smith GE, Housen P, Yaffe K, Ruff R, Kennison RF, Mahncke HW, Zelinski EM. A Cognitive Training Program Designed Based on Principles of Brain Plasticity: Results from the Improvement in Memory with Plasticity-based Adaptive Cognitive Training Study. Journal of the American Geriatrics Society. 2009;57:594–603. doi: 10.1111/j.1532-5415.2008.02167.x. [DOI] [PMC free article] [PubMed] [Google Scholar]

4.Thorell LB, Lindqvist S, Nutley SB, Bohlin G, Klingberg T. Training and transfer effects of executive functions in preschool children. Developmental Science. 2009;12:106–113. doi: 10.1111/j.1467-7687.2008.00745.x. [DOI] [PubMed] [Google Scholar]

5.Green CS, Bavelier D. Action video game modifies visual selective attention. Nature. 2003;423:534–7. doi: 10.1038/nature01647. [DOI] [PubMed] [Google Scholar]

6.Baddeley AD. A three-minute reasoning test based on grammatical transformation. Psychometric Science. 1968;10:341–342. [Google Scholar]

7.Conklin HM, Curtis CE, Katsanis J, Iacono WG. Verbal Working Memory Impairment in Schizophrenia Patients and Their First-Degree Relatives: Evidence From the Digit Span Task. Am J Psychiatry. 2000;157:275–277. doi: 10.1176/appi.ajp.157.2.275. [DOI] [PubMed] [Google Scholar]

8.Elliott R, Sahakian BJ, Matthews K, Bannerjea A, Rimmer J, Robbins TW. Effects of methylphenidate on spatial working memory and planning in healthy young adults. Psychopharmacology. 1997;131:196–206. doi: 10.1007/s002130050284. [DOI] [PubMed] [Google Scholar]

9.Mehta MA, Owen AM, Sahakian BJ, Mavaddat N, Pickard JD, Robbins TW. Methylphenidate enhances working memory by modulating discrete frontal and parietal lobe regions in the human brain. J Neurosci. 2000;20:RC65. doi: 10.1523/JNEUROSCI.20-06-j0004.2000. [DOI] [PMC free article] [PubMed] [Google Scholar]

10.Owen AM, Downes JD, Sahakian BJ, Polkey CE, Robbins TW. Planning and spatial working memory following frontal lobe lesions in Man. Neuropsychologia. 1990;28:1021–1034. doi: 10.1016/0028-3932(90)90137-d. [DOI] [PubMed] [Google Scholar]

11.Sahakian BJ, Morris RG, Evenden JL, Heald A, Levy R, Philpot M, Robbins TW. A comparative study of visuospatial memory and learning in Alzheimer-type dementia and Parkinson’s disease. Brain. 1988;111:695–718. doi: 10.1093/brain/111.3.695. [DOI] [PubMed] [Google Scholar]

12.Turner DC, Robbins TW, Clark L, Aron AR, Dowson J, Sahakian BJ. Cognitive enhancing effects of modafinil in healthy volunteers. Psychopharmacology (Berl) 2003;165:260–9. doi: 10.1007/s00213-002-1250-8. [DOI] [PubMed] [Google Scholar]

13.Owen AM, Beksinska M, James M, Leigh PN, Summers BA, Marsden CD, Quinn NP, Sahakian BJ, Robbins TW. Visuospatial memory deficits at different stages of Parkinson’s disease. Neuropsychologia. 1993;31:627–644. doi: 10.1016/0028-3932(93)90135-m. [DOI] [PubMed] [Google Scholar]

14.Cohen J. Statistical Power Analysis for the Behavioral Sciences. second ed. Lawrence Erlbaum Associates; 1988. [Google Scholar]

15.Gray JR, Chabris CF, Braver TS. Neural mechanisms of general fluid intelligence. Nature Neuroscience. 2003;6:316–322. doi: 10.1038/nn1014. [DOI] [PubMed] [Google Scholar]

16.Roca M, Parr A, Thompson R, Woolgar A, Torralva T, Antoun N, Manes F, Duncan J. Executive function and fluid intelligence after frontal lobe lesions. Brain. 2010;133:234–247. doi: 10.1093/brain/awp269. [DOI] [PMC free article] [PubMed] [Google Scholar]

17.Wright SB, Matlen BJ, Baym CL, Ferrer E, Bunge SA. Neural correlates of fluid reasoning in children and adults. Frontiers in Human Neuroscience. 2008;1:1–8. doi: 10.3389/neuro.09.008.2007. [DOI] [PMC free article] [PubMed] [Google Scholar]

18.Owen AM, Doyon J, Petrides M, Evans AC. Planning and spatial working memory examined with positron emission tomography (PET) European Journal Of Neuroscience. 1996;8:353–364. doi: 10.1111/j.1460-9568.1996.tb01219.x. [DOI] [PubMed] [Google Scholar]

19.Williams-Gray CH, Hampshire A, Robbins TW, Barker RA, Owen AM. COMT val158met genotype influences frontoparietal activity during planning in patients with Parkinson’s disease. Journal of Neuroscience. 2007;27:4832–4838. doi: 10.1523/JNEUROSCI.0774-07.2007. [DOI] [PMC free article] [PubMed] [Google Scholar]

20.Duncan J, Seitz RJ, Kolodny J, Bor D, Herzog H, Ahmed A, Newell FN, Emslie H. A neural basis for general intelligence. Science. 2000;289:457–60. doi: 10.1126/science.289.5478.457. [DOI] [PubMed] [Google Scholar]

21.Duncan J, Burgess P, Emslie H. Fluid intelligence after frontal lobe lesions. Neuropsychologia. 1995;33:261–8. doi: 10.1016/0028-3932(94)00124-8. [DOI] [PubMed] [Google Scholar]

22.Owen AM, Morris RG, Sahakian BJ, Polkey CE, Robbins TW. Double dissociations of memory and executive functions in working memory tasks following frontal lobe excisions, temporal lobe excisions or amygdalo-hippocampectomy in man. Brain. 1996;119:1597–1615. doi: 10.1093/brain/119.5.1597. [DOI] [PubMed] [Google Scholar]

23.Owen AM, James M, Leigh PN, Summers BA, Marsden CD, Quinn NP, Lange KW, Robbins TW. Frontostriatal cognitive deficits at different stages of Parkinson’s disease. Brain. 1992;115:1727–1751. doi: 10.1093/brain/115.6.1727. [DOI] [PubMed] [Google Scholar]

24.Wood SJ, Proffitt T, Mahony K, Smith DJ, Buchanan J, Brewer W, Stuart GW, Velakoulis D, McGorry PD, Pantelis C. Visuospatial memory and learning in first episode schizophreniform psychosis and established schizophrenia: a functional correlate of hippocampal pathology. Psychological Medicine. 2002;32:429–43. doi: 10.1017/s0033291702005275. [DOI] [PubMed] [Google Scholar]

25.Jäkälä P, Sirviö J, Riekkinen M, Koivisto E, Kejonen K, Vanhanen M, Riekkinen P., Jr. Guanfacine and clonidine, alpha 2-agonists, improve paired associates learning, but not delayed matching to sample, in humans. Neuropsychopharmacology. 1999;20:119–30. doi: 10.1016/S0893-133X(98)00055-4. [DOI] [PubMed] [Google Scholar]

26.Fowler KS, Saling MM, Conway EL, Semple J, Louis WJ. Computerized delayed matching to sample and paired associate performance in the early detection of dementia. Applied Neuropsychology. 1995;2:72–78. doi: 10.1207/s15324826an0202_4. [DOI] [PubMed] [Google Scholar]