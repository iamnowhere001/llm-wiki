---
title: "Removing Noise, not Finding Gold: Quality Filtering for Large-Scale Pretraining（Nait Saada et al., ICML 2026）"
author: "Thiziri Nait Saada、Louis Bethune、Michal Klein、David Grangier、Marco Cuturi、Pierre Ablin（六人全部隶属 Apple；第一作者为 Apple 实习期间完成，学籍在牛津大学）"
url: https://arxiv.org/abs/2510.00866
kind: paper
series: 无
published: "2025-10-01 提交 arXiv（v1）；v4 2026-06-24；已接收于 ICML 2026"
clipped: 2026-09-29
capture_quality: high
capture_method: >
  2026-09-29 从 arXiv 抓取。PDF 原件落盘为 raw/assets/2026-09-29-quality-filtering-pretraining.pdf
  （3,962,000 字节，21 页，PDF 自带文本层，未做 OCR）。
  用 pypdf 6.13.1 逐页提取转文本 —— 21 页 / 1153 行 / 63,734 字节，
  每页以 [p.N] 分隔，N 为 PDF 页码。**PDF 原件未改动，仍为 raw/assets/ 下同名文件。**

  收录理由：2026-09-29 北洛就「训练效果是否与语料优质程度正相关、合成语料是否不如
  普通人原生内容」提问。本库检索后确认库内对「模型坍缩 / 合成数据 / 质量过滤」
  **零覆盖**（raw/ 与 wiki/ 全文逐行核过，均为 0 命中）。北洛裁定走「先收录素材、
  再据此建分析页」的路径，并在本库给出的候选清单中选定本份与
  [[2026-09-29-synthetic-data-pretraining]]（另一份为质量过滤）。
  **本份的用途是为一个查询答案提供可引来源** —— 这是本库第一次以「溯源」而非
  「填项目缺口」为收录理由；**八项目的缺口表逐条核过，均不对上**，归属判断见 sources 页。

  已知缺失（五条）——
  1. **硬换行未重组。** PDF 提取保留印刷版视觉换行，一个句子可能跨 2–3 行，
       关键词检索会漏。与库内既有 PDF 素材（choice-overload-meta-analysis、dunlosky）做法一致。
    2. **表格未结构化保留。** HTML 版含 6 个 <table>，文本层里表头与数值列会错位或丢列；查表内数值须回 PDF。
    3. **图未单独提取。** HTML 版 15 张图、PDF 内 22 张图，全部留在 PDF 原件里。
    4. **公式被线性化。** HTML 版含 186 处数学表达式，文本层按线性顺序输出，上下标与分式会走样。
    5. **参考文献与页眉页脚混入正文流。** 参考文献起于 [p.13]，页眉逐页重复，检索时噪声较大。
capture_note: >
  **本字段只记「抓取事实」，不记「阅读结论」。**
  本素材的分层、关键要点、与库内已有主张的比对结果一律维护在
  wiki/sources/2026-09-29-quality-filtering-pretraining.md —— 它们随阅读深入而变，
  而本文件不可变，写在这里必然产生死结。**本文件不维护任何行区间。**

  行区间坐标系为**文件绝对行号**（`wc -l` 的坐标系）。
  正文行号 = 文件行号 − 50。
  引用前回文件核对。

  **素材性质**：arXiv 预印本（已接收于 ICML 2026），六作者署名完整，无转述层、无 AI 加工痕迹。
    **本库第五份一手学术文献（期刊/会议论文层级）** —— 前四份为 Bjork 2014、Dunlosky et al. 2013、
    Nolen-Hoeksema 等的反刍综述、Chernev et al. 2015（元分析）。

    **利益披露（§3.4）**：**全部作者隶属 Apple**，通讯邮箱为 @apple.com（行 17–18）；
    第一作者的工作为 Apple 实习期间完成（行 5）。PDF 内并含 Apple 商标声明（行 38）。
    另注：本份的结论之一是「花钱做优质语料库的收益不如直接过滤海量网页数据」——
    **这与 Apple 自身的数据处境（不拥有大规模用户语料）方向一致，登记为潜在利益相关**，
    但**本库不对作者的动机下判断**，只登记事实。
---
[p.1]
Removing Noise, not Finding Gold:
Quality Filtering for Large-Scale Pretraining
Thiziri Nait Saada‡,§,Louis Bethune †,Michal Klein †,David Grangier †,Marco Cuturi †,Pierre Ablin †
‡Work done as an intern at Apple, §University of Oxford, †Apple
Large-scale models are pretrained on massive web-crawled datasets containing documents of mixed quality, making
data filtering essential. A popular method is Classifier-based Quality Filtering (CQF), which trains a binary classifier to
distinguish between pretraining data and a small, high-quality set. It assigns each pretraining document a quality score
defined as the classifier’s score and retains only the top-scoring ones. We provide an in-depth analysis of CQF. We show
that while CQF improves downstream task performance, it does not necessarily enhance language modeling on the high-
quality set. Importantly, we find that training on CQF-selected data can outperform training directly on the high-quality
set, even when the latter is sufficiently large. This finding alone is particularly striking, given the substantial effort and
cost recently devoted to augmenting high-quality data. We explain this paradox by the fact that CQF implicitly filters the
high-quality dataset as well as the low-quality one. Finally, we introduce an optimization-driven notion of data quality and
demonstrate that it can be reliably estimated using small-scale proxy experiments. Altogether, our results both elucidate
the mechanisms behind CQF and deepen our understanding of data selection methods widely used in practice.
Correspondence:Thiziri Nait Saada: naitsaadat@maths.ox.ac.uk; Louis Béthune: l_bethune@apple.com; Pierre Ablin: p_ablin@
apple.com
Date:June 25, 2026
1 Introduction
Large-scale models are pretrained on large amounts of data, and the quality of these data is a critical factor
in achieving state-of-the-art performance. Among various heuristics for leveraging data quality to improve on
downstream tasks, Classifier-based Quality Filtering (CQF) is recognized as a cornerstone of data processing.
CQF has now become widely adopted and is, for instance, part of established pretraining pipelines like those
of GPT3 (Brown et al., 2020), LLama (Touvron et al., 2023), and PALM (Chowdhery et al., 2023). It is
also a key component of several widely used public datasets, such as DCLM (Li et al., 2024) or the SmolLM
corpus (Ben Allal et al., 2024).
CQF, as illustrated in Figure 1, trains a binary classifier to distinguish documents from a large, low-quality
pretraining set (LQ set) from those of a small, high-quality dataset (HQ set). It then assigns a scalar quality
score to each document within the LQ set, defined by the classifier’s score. The filtered dataset is formed by
selecting the topkfraction of documents in the pretraining set, ranked by quality score.
The goal of this paper is to understand the mechanics behind CQF, its impact on downstream performance,
and to challenge the underlying notion of quality it defines. Concretely,does CQF truly select data that
resemble the HQ set, as it is commonly believed? Is collecting more HQ data always the optimal strategy for
improving downstream performance? What makes CQF potentially more effective than simply augmenting
HQ data? Do its quality scores reflect intuitive notions of data quality, or should we adopt a more principled,
optimization-driven definition that can be reliably estimated using small-scale proxies?
Apple and the Apple logo are trademarks of Apple Inc., registered in the U.S. and other countries and regions.
1
arXiv:2510.00866v4  [cs.LG]  24 Jun 2026
[p.2]
High-Quality Set
Pretraining Set Embed Score Pretraining Set
k=10%
Classifier score 
distribution 
k=25%
k=50%
0 1
Classifier
Select 
top k
CQF Set
k=5%
<latexit sha1_base64="WCulPo+PYVdQFN7dqfEOKsYxlB8=">AAAB/HicbVDLTgIxFL3jE/GFunTTSExYkRnja0l04xKNPBKYkE7pQEOnM2nvmBCCX+BWv8Cdceu/+AH+hwVmIeBJmpycc2/u6QkSKQy67rezsrq2vrGZ28pv7+zu7RcODusmTjXjNRbLWDcDargUitdQoOTNRHMaBZI3gsHtxG88cW1ErB5xmHA/oj0lQsEoWunBlDqFolt2pyDLxMtIETJUO4WfdjdmacQVMkmNaXlugv6IahRM8nG+nRqeUDagPd6yVNGIG380TTomp1bpkjDW9ikkU/XvxohGxgyjwE5GFPtm0ZuI/3mtFMNrfyRUkiJXbHYoTCXBmEy+TbpCc4ZyaAllWtishPWppgxtOXNXUNjA47ztxVtsYZnUz8reZfni/rxYuckaysExnEAJPLiCCtxBFWrAIIQXeIU359l5dz6cz9noipPtHMEcnK9frLaVPg==</latexit>
s (
<latexit sha1_base64="MV7TMx2o1t01RTckb/5+bypDu0Y=">AAAB+3icbVDJSgNBFOyJW4xb1KOXxiDoJcyI2zHoxWMCZoFkCD2dN0mTnoXuN0IY5gu86hd4E69+jB/gf9hJ5mASCxqKqvd41eXFUmi07W+rsLa+sblV3C7t7O7tH5QPj1o6ShSHJo9kpDoe0yBFCE0UKKETK2CBJ6HtjR+mfvsZlBZR+ISTGNyADUPhC87QSI2LfrliV+0Z6CpxclIhOer98k9vEPEkgBC5ZFp3HTtGN2UKBZeQlXqJhpjxMRtC19CQBaDddBY0o2dGGVA/UuaFSGfq342UBVpPAs9MBgxHetmbiv953QT9OzcVYZwghHx+yE8kxYhOf00HQgFHOTGEcSVMVspHTDGOppuFKyhM4KxkenGWW1glrcuqc1O9blxVavd5Q0VyQk7JOXHILamRR1InTcIJkBfySt6szHq3PqzP+WjByneOyQKsr1/R/5TC</latexit>
)
Figure 1Classifier-based Quality Filtering (CQF) pipeline. A document embedding model (e.g. sBert, Artic-
Embed or FastText) embeds documents from a high-quality dataset and the pretraining set. A binary classifier is
trained on those embeddings to distinguish the HQ set from the pretraining set. Scores assigned by the classifier are
used to rank documents from the pretraining set. The topkfraction of those documents constitutes the new filtered
CQF dataset.
We start by highlighting a paradox in how CQF works: although CQF consistently improves downstream
performance, it does not necessarily improve language modeling on the HQ set. This finding challenges the
widely held belief that CQF improves models by selecting training data that are similar to the HQ data.
Importantly, we show that training on CQF-selected data can outperform training directly on the HQ set
itself, even when the HQ set is sufficiently large—a striking result given the recent substantial effort and cost
typically devoted to augmenting high-quality data.
We explain this paradox by showing that CQF effectively performs an implicit filtering of theHQ setitself:
it upweights data in the HQ set that are far from the LQ set. This means that models trained with CQF
are not necessarily good at language modeling on the whole HQ set, but rather on a subset of it. Moreover,
we show that this filtering of the HQ set aligns with downstream tasks for most choices of HQ sets, which
explains the paradox. We then compare CQF to importance sampling methods (Xie et al., 2023; Grangier
et al., 2024), which explicitly attempt to resample the LQ set to match the distribution of the HQ set. We
highlight a stark difference between the two methods: importance sampling yields better language modeling
on the HQ set, but it does not benefit from the aforementioned implicit filtering of the HQ set that improves
downstream performance.
Beyond these paradoxes, we introduce a new lens to probe whether CQF induces a meaningful notion of
quality. Specifically, we formalize the notion ofdata-conditioning: along a true quality axis, training on
“clean” data should give better performance on “dirty” test distributions than training directly on the dirty
distribution. This property arises purely from optimization effects—if training were perfect, learning directly
on dirty data would always be optimal—so any observed advantage from filtering must come from the fact
that clean data are easier to optimize on in practice. Hence the term data-conditioning.
Crucially, we show that this optimization-driven notion of data quality can be reliably estimated using small-
scale proxy models, making it practical for guiding large-scale data selection. For instance, we demonstrate
that this property is clearly observed when constructing data mixtures of clean and dirty documents, as in-
spired by Kallini et al. (2024). In contrast, subsets selected by CQF fail to exhibit any such data-conditioning
ordering, suggesting that the notion of quality CQF captures is more limited and closely related to stylistic
or domain similarity—contexts in which “training cleaner” does not universally help.
1.1 Related Work
Recent surveys (Albalak et al., 2024; Longpre et al., 2024) provide comprehensive overviews of data selec-
tion pipelines and identify classifier- and perplexity-based filtering as the most widely used techniques, with
classifier-based methods being the most effective in practice (Li et al., 2024). A common underlying assump-
tion across these approaches is that pretraining on data resembling a small, trusted high-quality (HQ) set
(e.g., Wikipedia, books, curated instructions) improves downstream performance. This has motivated two
main strategies that operate at the document level: directly mimicking the HQ distribution via importance
sampling or indirectly approximating it through classifier-based filtering. In the first paradigm, Xie et al.
(2023) approximate the likelihood ratio between HQ and LQ data to guide resampling of the LQ set, while
2
[p.3]
Dataset # Documents
OpenOrca (Lian et al., 2023) 3M
Reddit ELI5 (Fan et al., 2019) 325k
OpenHermes (Teknium, 2023) 240k
KnowledgePile (Fei et al., 2024) 1M
openwebmath (Paster et al., 2023) 6.3M
ARC Easy (Clark et al., 2018) 2.25k
Table 1Overview of the “high-quality” datasets used for CQF.
CRISP (Grangier et al., 2024) uses clustering of the pretraining data to best match the HQ set.
CQF, on the other hand, uses a classifier to score LQ documents by learning boundaries between HQ and LQ
samples. CQF is widely adopted in state-of-the-art pipelines: GPT-3 (Brown et al., 2020) employs a classifier
with Pareto-biased sampling; LLaMA (Touvron et al., 2023) filters Common Crawl using Wikipedia as HQ;
GLaM (Du et al., 2022), PaLM (Chowdhery et al., 2023), and RedPajama (Weber et al., 2024) similarly
relies on Wikipedia and books. More recently, Li et al. (2024) introduced DCLM, a large-scale filtered
dataset centered on CQF, using ELI5 (Fan et al., 2019) and OpenHermes (Lian et al., 2023) as HQ sources.
Wang et al. (2025) study methods to build HQ sets, and Soldaini et al. (2024) propose the Dolma Toolkit,
where CQF is applied to the Dolma dataset itself. RefinedWeb (Penedo et al., 2023) and FineWeb (Penedo
et al., 2024) use classifiers to extract English documents. Artic-Embed (Merrick et al., 2024) is a popular
document embedder for training quality classifiers, underlying Python-edu and FineWebEdu (Ben Allal et al.,
2024) datasets. Recently, Mizrahi et al. (2025) analyzed how aggressive filtering should be as function of
model and data scales. Finally, classifiers can also be used to filter toxic content (Welbl et al., 2021).
Beyond CQF and importance sampling, recent works learn proxy scores directly linked to downstream per-
formance rather than assuming and imposing any fixed notion of quality. For example, Mizrahi et al. (2025)
train regressors to predict closeness to evaluation tasks, Zhuang et al. (2025) combine multiple quality di-
mensions into learned mixtures, and older methods rely on LLM perplexity (Wenzek et al., 2020). These
methods suggest that the best data may not necessarily resemble a specific HQ corpus, but rather satisfy
task-relevant criteria that can be discovered during training.
2 Classifier-based Quality Filtering
We describe the Classifier-based Quality-Filtering (CQF) method as it is used in the literature and in this
paper. CQF takes as inputs a high-quality (HQ) dataset,DHQ, a pretraining dataset that is generally of low
quality,D LQ, and a selection fractionkbetween0and100%.
Low-quality (LQ) dataset.This is a standard pretraining set, which, in the context of LLMs, contains
curated documents gathered from a large web crawl spanning diverse data sources. While the dataset is
huge—containing enough tokens to train large models without repetitions—it also includes many low-quality,
badly formatted, or uninformative documents. The overall goal of data selection is to find a subset of this
LQ set that leads to better model performance. In this paper, we take RedPajama-V2 as our LQ set, which
contains 32T tokens spanning multiple languages.
High-quality (HQ) dataset.This is a high-quality dataset made of documents from a highly curated
source. These documents are well formatted, have relevant content and are sometimes manually annotated.
They can be pretraining or instruction following data coming from humans, or sentences generated by a
sufficiently good language model. However, the HQ set itself is typically too small to train a model on.
Instead, it serves two key purposes to guide the data selection process: 1) as a target for selection, where
data in the LQ set that resemble the HQ set are considered high quality, and 2) as a benchmark to evaluate
the effectiveness of data selection, with models achieving low loss on this dataset considered to be performing
well. Table 1 gives an overview of HQ sets used in this work.
CQF is a widely used method for data selection that filters data from the LQ set, guided by the HQ set. We
now describe its practical implementation, illustrated in Figure 1.
3
[p.4]
50.0
60.0
Downstream Acc.
HQ set: OpenOrca
50.0
60.0
HQ set: KnowledgePile
50.0
60.0
HQ set: OH+ELI5
50.0
60.0
HQ set: openwebmath
50.0
60.0
HQ set: ARC Easy
2.75
3.00
3.25
LQ set loss 2.75
3.00
3.25
2.75
3.00
3.25
2.75
3.00
3.25
2.75
3.00
3.25
1%5%20%100%
2.75
2.80
2.85
HQ set loss
1%5%20%100%
2.90
2.95
1%5%20%100%
2.5
2.6
2.7
1%5%20%100%
2.6
2.8
1%5%20%100%
3.0
3.5
CQF Selection Fraction k
Figure 2Top row: Models trained on increasingly selective data show improved performance on downstream tasks.
Bottom row: When evaluated on the HQ dataset itself, these models do not necessarily improve as there is a non-
increasing relationship between downstream performance and loss on the HQ set.
Embedding.Each document in the HQ and LQ datasets is embedded in a vector spaceRp. Since the whole
LQ set has to be embedded, the embedding method needs to be scalable. In practice, we use sBert, with
p= 384. Another popular choice is FastText (Joulin et al., 2016).
Classifier training.A training set made ofnembeddings from the HQ set andnothers from the LQ
set is used to train an L2-regularized logistic regression. The regularization coefficient is taken as the one
maximizing accuracy on a held-out set. Once this classifier is trained, it defines theCQF scorefunction
s(x)∈[0,1], that, for any documentx, defines a scalar that measures how likely the classifier is to identify
this document as a member of the HQ set. This scores(x)is often called quality signal (Weber et al., 2024),
which is why, in the context of CQF, we will refer to it asquality of documentx. A goal of this paper is
to understand whether this definition of quality is appropriate.
“Quality” filtering.In order to estimate the distribution of the quality scores in the LQ dataset, a subset
of the LQ dataset is scored, which allows us to estimate the cumulative densityC(˜s) =P(s(x)≤˜s|x∈DLQ)
for all˜s∈[0,1]. Then, for a givenselection fractionk, only the topkfraction of documents in the LQ set
is kept, resulting in a filtered datasetDCQF ={x∈D LQ|C(s(x))≥1−k}.
This selects the documents in the LQ set that are most likely to belong to the HQ set, based on the score
defined by the classifier, and are therefore “higher-quality” documents. This dataset is then used to train
models in place of the low-quality pretraining set. One clear limitation of CQF is that the number of training
tokens available in the dataset isk×DwhereDis the total number of tokens in the LQ set. Too small values
ofklead to scarce datasets on which models cannot be trained without repeating data or even overfitting.
In this paper, we step away from this limitation and always use values ofksuch that there are
enough data inDCQF to train a model without repeating data.This allows us to focus solely on the
impact of data quality rather than on the effects of repeated training examples.
Evaluations.After pretraining, models are evaluated by scoring them on typical evaluation benchmarks,
such as general knowledge question answering. Performance on these datasets is indicative of the usefulness of
models after post-training. In this work, we consider evaluations on ARC-Easy, ARC-Challenge, MMLU, and
reward-bench. The bulk of our experiments is done on ARC-Easy, which has better-than-random performance
even at small scale. Implementation details can be found in Appendix F.
4
[p.5]
top 100%
top 80%
top 60%
top 40%
top 20%
top 1%
CQF scores
Dataset
CQF
Target Benchmark
RedPajamaV2
HQ set
ARC-Challenge
ARC-Easy
mmlu
reward-bench
KnowledgePile
OH+ELI5
OpenOrca
openwebmath
Figure 3Two-dimensional PCA projections of sBert embeddings from quality buckets defined by clas-
sifiers, each using a different HQ set.. Quality buckets across classifiers (CQF) used in the literature exhibit
alignment towards benchmark datasets. When considering the top 100%, we fall back to the original pretraining
dataset (RedPajama-V2) regardless of the HQ set used. The performance of a model trained on the LQ set is given
by the leftmost point in each figure, corresponding tok=100%.
3 CQF improves model evaluations
We begin with the observation that motivates the wide adoption of CQF. We train 350M models on CQF
datasets across different HQ datasets and values ofk. We then evaluate those models by computing their
accuracy on ARC-Easy. We also use ARC-Easy itself as the HQ set. We display the results in Figure 2,
top row. Among all HQ sets, using ARC-Easy leads to the best downstream performance. We observe that
accuracy generally improves as we select datasets of higher quality, with smaller values ofk. This occurs for
OpenOrca, KnowledgePile, OH+ELI5, and ARC-Easy, but for openwebmath, we observe a performance dip
if we select a value ofkthat is too small. A simple explanation is that CQF with openwebmath selects too
specialized documents. We confirm this alignment between data selected by CQF and common benchmarks
in Figure 3 by examining a 2D PCA of their latent space.
4 CQF does not select data that resemble the high-quality set
CQF ranks data based on likelihood ratios.Assuming that the binary classifier trained in CQF is Bayes-
optimal, the CQF quality score of a documentxiss(x) = pHQ(x)
pHQ(x)+pLQ(x) (Hastie et al., 2009). As such, scores
are an increasing function of thedensity ratio:s(x) =ϕ

pHQ(x)
pLQ(x)

withϕ(t) = t
t+1. The ordering of documents
implicitly defined by CQF is therefore that of the likelihood ratio: a documentxis of “higher quality” than a
documentyif pHQ(x)
pLQ(x) ≥ pHQ(y)
pLQ(y). This contrasts with the "importance sampling" ranking, which would rankx
higher thanysolely based on their likelihood under the HQ distribution, i.e., ifpHQ(x)≥p HQ(y). A simple
conclusion is that CQF does not select samples that are most likely to come from the HQ set only. Instead,
it prefers documents that are both likely under the HQ distribution (highpHQ(x)) and unlikely under the
LQ distribution (lowpLQ(x)). With CQF, data are filtered based on a trade-off between being close to the
HQ set and far from the LQ set. This phenomenon is clear from the score densities of data filtered by CQF
shown in Figure 4.
4.1 Kullback-Leibler divergence between datasets
For each model trained in section 3, we also compute its next-token prediction loss on the HQ set (Figure 2,
bottom row). We observe U-shaped curves for all HQ datasets except ARC-Easy. For these HQ sets, the
optimalkthat yields the smallest loss is often large. Remarkably, small values ofkcan result in models
that perform even worse on the HQ set than a model trained on the full LQ set, as seen with OpenOrca
or KnowledgePile. This behavior contrasts with using ARC-Easy as HQ set, where reducingkconsistently
improves both model performance and language modeling.
As a result, there is a clear discrepancy between the loss on the HQ set—which reflects how closely the
pretraining data resemble the HQ distribution—from the achieved downstream performance. This challenges
the standard belief that CQF filters data to get closer to the HQ set.
5
[p.6]
Joint PCA of CQF and HQ set
Domain
HQ set: OpenOrca
CQF in top 100%
CQF in top 25%
CQF in top 2%
CQF in top 1%
Figure 4CQF works by filtering out the low-quality data (red),notbecause the retained data (green) resemble
the HQ set (orange). We display a 2D PCA in sBert latent space. TSNE shows similar patterns in Appendix C.
Loss on the HQ set as a proxy for the distance between CQF and HQ set.The loss measured on the HQ set can be
interpreted as a measure of howdifferentthe filtered data are from the HQ set in terms of Kullback-Leibler
(KL) divergence, under the assumption that the model has infinite capacity (Cover, 1999). Indeed, in this
case, the model’s parametersθare such that the model trained on the filtered set by CQF would perfectly
represent its data distribution, i.e.,pθ(x)≈p CQF(x).
Evaluating this model on the HQ set yields a next-token prediction loss equal toEx∼DHQ [−logp CQF(x)].
This quantity can be decomposed as,
H(DHQ) + KL(DHQ∥DCQF),
whereH(D HQ)is the entropy of the HQ distribution (a constant when changingk), andKL(DHQ∥DCQF)is
the KL divergence from the HQ distribution and the distribution of data filtered by CQF. Hence, under the
hypothesis that the models trained in these experiments accurately representpCQF, the observed increase
in HQ loss for smallkmeans that the corresponding pretraining sets diverge further away from the HQ
distribution. To our knowledge, this phenomenon has not been previously identified. In the next section, we
investigate the reasons behind it.
4.2 CQF implicitly filters the high-quality dataset as well as the low-quality set
One way to interpret the CQF selection rule is that it is a reweighting of the distribution of the HQ set, with
non-uniform weights: it puts a larger weight on documents that are far from the LQ set.
As a result, CQF can be understood as 1) selecting data in the HQ set that are far from the LQ set and then
2) selecting data in the LQ set that are close tothatportion of the HQ set. To validate this interpretation,
we further partition the HQ set itself into 10 "quality" buckets according to their CQF scores. We then
measure the next-token prediction loss on these 10 domains achieved by models trained with CQF by varying
kin Figure 5. Interestingly, the loss on the top-scoring documents from the HQ set behaves very differently
than the loss on the bottom-scoring data from the same set. More precisely, the loss on the top-scoring HQ
data is monotonic withk, while the loss on the bottom-scoring HQ data rises sharply askdecreases. This
analysis decomposes the overall U-shaped loss reported in the previous section into the average loss across
different quality levels within the HQ set. Crucially, this implicit filtering of the HQ set itself is beneficial.
In fact, data in the HQ set that resemble data from the LQ set are likely to be of lower quality, since the LQ
set contains a significant amount of noisy data. This resolves the earlier paradox: top-scoring data within
the HQ set are more aligned with evaluation benchmarks than those from the HQ set with lowest scores; see
Figure 5.
We further validate that these top deciles of HQ sets are aligned with downstream evaluations by finetuning
a 1.3B model on them, as well as on the full HQ set. We report the corresponding gains in accuracy in
Figure 6. This again shows that the top decile of KnowledgePile is aligned with ARC-Easy, while the full set
is not. We now formalize this implicit filtering intuition.
6
[p.7]
1%2%5%20%100%
CQF selection fraction k
2.8
2.9
3.0
3.1
3.2
Loss
Full HQ set
HQ score deciles
Lowest← quality→Highest
1%20%40%60%80%100%
HQ score deciles
1.5
2.0
Distance to ARC Easy
the top bucket is closest
to ARC Easy
Lowest← quality→Highest
Figure 5CQF implicitly filters the HQ set. We split the HQ set (KnowledgePile) into10deciles of CQF scores.
Left. For each model trained with CQF at a given fractionk, we report the loss of the model on each of these
deciles. The reddest curve corresponds to the loss on the HQ elements with the bottom10%scores, while the greenest
curve corresponds to the top10%. Our findings indicate that only the high-quality deciles of the HQ set exhibit a
consistently decreasing loss. This suggests that the classifier effectively identifies and learns the features within these
deciles, enabling the models to make better predictions. However, on average over all the deciles (dotted line), the
loss is a U-curve, recovering the loss in Figure 2 (second row and column).Right. In sBert latent space, we compute
the distance between the barycenter of ARC-Easy to the barycenter of each HQ decile. This distance correlates well
with performance on ARC-Easy itself.
CQF as a reweighting of the HQ set.Lettingr(x) =pHQ(x)
pLQ(x) be the likelihood ratio, CQF selects data
in the LQ set such thatr(x)≥τ, whereτis calibrated so that only a fractionkof the LQ set is selected.
The CQF dataset’s density can be rewritten as
pCQF(x) = 1
Z 1r(x)≥τ pLQ(x) =w(x)pHQ(x),(4.1)
wherew(x)∝
1r(x)≥τ
r(x) , which means that it is a reweighted version of the HQ set density, with weightsw(x),
and whereZis a normalization constant. The most upsampled points in the HQ set, which have a high value
w(x), are therefore those such thatr(x)is aboveτwhile being small. This is akin to a filtering of the HQ
set based on the likelihood ratio valuer(x). This explains the results in Figure 5: as the fractionkreduces,
pCQF gets close to a filtered version ofpHQ where only top-scoring samples are kept.
MMLU, base: 25% ARC Easy, base: 60%ARC Challenge, base: 28%Reward Bench, base: 57%
0
1
2
3
4 Accuracy % vs base
KnowledgePile
Top 10% of KnowledgePile
OpenOrca
Top 10% of OpenOrca
Figure 6Finetuning a 1.3B model on HQ sets and on their top decile. We report the best performances
during fine-tuning; no bar means that fine-tuning on that set does not improve the performance on that benchmark.
Darker colors indicate finetuning on the top 10%of the HQ set according to the CQF classifier, while light colors
indicate finetuning on the whole HQ set. The same number of tokens is used in both scenarios. OpenOrca aligns
most closely with MMLU, whereas KnowledgePile shows stronger alignment with ARC-Easy, supporting the trend
observed in Figure 3.
7
[p.8]
2.7 2.8
50%
60%Downstream Acc.
HQ set: OpenOrca
3.0 3.5
HQ set: ARC Easy
Lowest← quality→Highest
Loss on HQ set
CQF CRISP on HQ set
Figure 7Performance comparison between CQF and importance sampling-based approach (CRISP).
CQF induces a data selection that is substantiallydifferentfrom the HQ set. Colors indicate more (green) or less
(red) filtering.
5 CQF is not importance sampling
A common belief behind the use of CQF is: “Ideally, we would train on the HQ set, but we don’t have enough
data. So we use CQF to mimic data from the HQ set.”
As we have seen in the previous section, assuming that the classifier is Bayes-optimal, CQF draws samples
from the LQ set following the densityw(x)pHQ(x), wherew(x)is not uniformly equal to1. On the other
hand, importance sampling methods try to sample elements from the LQ set that directly follow the density
pHQ. We use the CRISP method (Grangier et al., 2024) in order to implement importance sampling, with
the same models as in section 3, with OpenOrca and ARC-Easy as HQ sets. We report the loss on the HQ
set and the downstream accuracy in Figure 7, as well as those of the models trained with CQF. OpenOrca
being diverse and multi-topic, we found thatC= 4096clusters are sufficient to capture that distribution
well, whereas ARC-Easy requiresC= 260kclusters. We observe that importance sampling indeed leads to
good language modeling on the HQ set, which translates to better downstream performance when the HQ
set is the downstream task itself (right), but not when the HQ set is a curated dataset (left). In that case,
CQF leads to better downstream performance than importance sampling. This is fully consistent with our
previous findings: CQF does not simply mimic the HQ distribution, but instead performs an implicit filtering
of the HQ set itself that prefers examples aligned with common downstream benchmarks.
6 CQF can outperform data augmentation
A widely held assumption in data curation pipelines is that if we had enough data from the HQ set, we would
train models on the HQ set itself. We now argue that this is not necessarily the case:training on CQF-
filtered data can outperform direct training on the HQ set, even when the HQ set contains
enough tokens to support large-scale training without data scarcity.To demonstrate this, we design
an experiment where we recursively apply CQF to construct a HQ set sufficiently for training; see Figure 8.
We start from a base HQ set of limited size,Dbase
HQ ; in practice, we use OpenOrca. We construct an expanded
HQ dataset by applying CQF to the LQ corpus using this base HQ set as reference:DHQ = CQF(Dbase
HQ ,20%),
i.e. the CQF withk= 20%of the base HQ set. Now, this new high-quality set contains enough tokens to train
large-scale models without repetition, since it corresponds to a substantial fraction of the LQ corpus. We then
apply CQF again using this newly constructed HQ set as reference, and train a model on the top1%of the
resulting filtered dataD′
HQ. We compare it to a model trained directly onDHQ under the exact same training
conditions. Empirically, we observe that the model trained on the unlimited HQ set achieves an accuracy
8
[p.9]
Pretraining Set
High-Quality Set
DHQ
CQF(20%)
CQF(1%)
acc.: 53.8%acc.: 50.1%
D′ 
HQ
Figure 8Training with CQF can lead to higher downstream performance than training directly on the
HQ set, even if it is sufficiently large.Starting from a base HQ set, a CQF subset is selected and expanded into
a new HQ setDHQ, which now acts as an unlimited HQ data source that enables large scale training. A subsequent
CQF filtering on this new HQ set produces a refined training datasetD′
HQ, which yields models that outperform
those trained directly on the original HQ setDHQ.
of50.1%, while the model trained on the CQF-filtered dataset achieves53.8%. Thus, the CQF-trained
model outperforms direct HQ training, despite the HQ set being sufficiently large to avoid data scarcity
effects. Strikingly, these results show that CQF can construct training distributions that are more effective
for downstream performance than the HQ distribution itself. This illustrates that CQF should not be viewed
merely as a mechanism for approximating or reconstructing HQ data, but rather as a distribution-shaping
operator that produces optimization-efficient training datasets from large uncurated corpora. Given the
substantial resources typically devoted to HQ data augmentation, this finding provides a direct and practical
alternative: rather than expanding HQ datasets through costly data collection or synthetic generation, CQF
can be used to improve upon HQ sets themselves, offering a scalable and principled strategy for data selection
and pretraining.
7 Does CQF define a sound notion of quality?
The goal of this section is to offer a different perspective on the concept of quality by introducing a formal
definition based upon optimization considerations. Within this framework, we (i) explore a semi-synthetic
setting where quality can be clearly defined and controlled, (ii) show that the notion of data quality induced
by CQF does not align with data-conditioning, and crucially, (iii) demonstrate that our formalization is
practically relevant, as it can be reliably estimated using small-scale proxy experiments.
7.1 Data-quality as an optimization catalyst
Central to our analysis is the concept of data-conditioning, which we define as a desirable property of data
quality. Informally, a datasetDclean is better data-conditioned than another datasetDdirty if a model trained
onD clean outperforms a model trained onDdirty when evaluated onDdirty.
We describe it formally as follows. Given an objective functionℓand a datasetD, we define the loss
function asL(θ, D):=E x∼D[ℓ(x;θ)]. This loss is typically approximately minimized by running a stochastic
optimization algorithmAon the samplesx i:
θn
Ddirty ← A(xi),with(x i)n
i=1 ∼D dirty,(7.1)
wherex i’s areni.i.d. samples fromD dirty. Instead of training onDdirty, one can also train onDclean and
obtain parametersθ n
Dclean. We propose an axiomatic definition of quality:
Data-conditioning.We writeD clean ≻D dirty and say that a datasetD clean is better data-
conditioned thanD dirty, relative to the learning ruleAand the horizonn∈Nif
L(θn
Dclean , Ddirty)≤ L(θn
Ddirty, Ddirty).(7.2)
9
[p.10]
We coin this phenomenon “data-conditioning”, drawing from the optimization literature, whereconditioning
typically describes how easily a loss function can be minimized. In our context, data-conditioning captures
how the structure of a dataset accelerates optimization. Indeed, in standard large-scale settings, data are
seldom repeated, and models generalize well, which means that the training loss closely approximates the
validation loss. Therefore, if we had a perfect minimization oracle,A(xi) = arg minθ∈Θ 1
n
Pn
i=1 ℓ(xi, θ), we
would have by definition of the minimizerL(θn
Ddirty, Ddirty)≃ 1
n
Pn
i=1 ℓ(xi, θn
Ddirty)≤ 1
n
Pn
i=1 ℓ(xi, θn
Dclean )≃
L(θn
Dclean , Ddirty). This would forbid the existence of better data-conditioned datasets. However, the existence
of better-conditioned datasets has been reported many times in the literature, and is at the root of curriculum
learning (Bengio et al., 2009), dataset distillation (Wang et al., 2018), or mixture optimization (Zhang et al.,
2025; Shukor et al., 2025). Thus, our definition of quality arises from imperfect optimization.
We believe that data-conditioning can act as a guiding principle for data filtering. Indeed, if one has two
datasets such thatDclean ≻D dirty, there is no use in training onDdirty, if we have enough tokens inDclean,
because it would yield an inferior model even on the distribution it is trained on. This can therefore be seen
as a data-selection principle: how can we select a subset inDdirty that is better data-conditioned thanDdirty
itself?
7.2 CQF through the lens of data-conditioning
To illustrate this notion of data-conditioning, we explore different ways of creating a spectrum of “quality”,
using families of datasets indexed by one variablek∈[0,1], where, intuitively, lower values ofkcorrespond
to higher-quality datasets, and higher values indicate lower-quality.
First, we create semi-synthetic text datasets with varying levels of quality, inspired by Kallini et al. (2024).
Using RedPajama-V2 as our base dataset representing the highest quality, we simulate different quality
levels by constructing a family of datasetsPerm(k)fork∈[0,1]. EachPerm(k)is created by sampling
documents whose tokens are randomly permuted with probabilityk, or kept unchanged with probability
1−k. Similarly, we define another family of datasetsCQF(k), wherekdenotes the selection fraction, using
CQF with OpenOrca as the HQ set. We define Exclusive CQF by taking documents whose score lies in a
given interval.
We compare the scaling behaviors of models trained on these datasets, by varying the number of parameters
N, training tokensD, and the “quality” levelk. We report their next-token prediction loss on each “quality”
levelk ′.
50% 22% 12% 4% 1%
Test on top k'
50%
22%
12%
4%
1%
Train on top k
Perm
100% 30% 15% 5% 1%
Test on top k'
100%
30%
15%
5%
1%
CQF
70% 37% 17% 6% 1%
Test on top k'
70%
37%
17%
6%
1%
Exclusive CQF
0.10
0.05
0.00
0.05
0.10
 Loss vs Train on k'
Figure 9Data-conditioning experiment.We use three different ways to define an axis of “quality”, which are
datasets indexed by a scalark∈[0,1], wherek= 0means higher quality. Perm defines it as(1−k)wherekis the
probability of randomly permuting a document. CQF defines it as the fraction of documents kept in the pretraining
set, where the HQ set is OpenOrca. Exclusive CQF defines it as documents that have scores between two thresholds.
Each of these datasets is parameterized by a quality knob,k. We train models for a grid of valuesk, and compute
their test loss on the datasetk′,L(k, k′). The figure displays the matrices with entriesL(k, k′)− L(k′, k′). A negative
value for the coefficientk, k′ meansk≻k ′, as defined in Equation 7.2.
Static analysis.We begin by training models of a fixed size for a fixed number of iterations on each
10
[p.11]
50% 22% 12% 4% 1%
Test on top k'
50%
22%
12%
4%
1%
Train on top k
N=1B, D=20N
50% 22% 12% 4% 1%
Test on top k'
50%
22%
12%
4%
1%
N=1B, D=1000N
50% 22% 12% 4% 1%
Test on top k'
50%
22%
12%
4%
1%
N=D=+
0.02
0.00
0.02
 Loss vs Train on k'
Figure 10Data-conditioning is well approximated at small scale.We fit scaling laws in order to have a
dynamic view of Figure 9 (left). We then report the predicted loss of models of sizeNtrained withDtokens. When
N=D= +∞, we use the irreducible error termEpredicted by the scaling law as a proxy for the loss. We observe
that the regions of better data-conditioning (orange) are mostly kept the same as we scale models. When scaling in
the large D direction, we observe that the effect gets narrower.
quality bucketkin Figure 9. Each index(k, k ′)shows the valueL(k, k ′)− L(k′, k′), whereL(k, k′)is the
loss on quality bucketk′ for a model trained on quality bucketk. For the synthetic case (left), we observe
a mostly upper-triangular structure, which means that training on better quality domains also improves
models on lower quality domains, apart from the edge case of training on non-permuted tokens. In other
words, organizing data by quality deciles leads to structured performance gains in this controlled setting,
where higher-quality data results in greater improvements, aligning with our intuition of quality as a concept.
In contrast, the CQF case (middle) does not exhibit the upper-triangular organization that would make the
data-conditioning definition aligned with the notion of quality induced by CQF. In Appendix E we extend
our investigation of this data-conditioning binary relation.
7.3 Data conditioning can be reliably estimated using small-scale proxy models.
To validate the use of small-scale proxies for our definition, we first assess how sensitive it is to model and
dataset scale. For thePermquality axis, we repeat the previous experiment at different model scales and
training horizons, with model scales ranging from 125M to 1.3B parameters. Then, for each train/validation
pairk, k′, we fit a scaling law that predicts the lossL(k, k′)as a function ofN, the model size, andD, the
number of seen tokens. We fit the Chinchilla scaling law (Hoffmann et al., 2022):
L(k, k′)N,D =E+ A
N α + B
Dβ
where the parametersE, A, B, α, βdepend on the train/validation pairsk, k′. This enables us to obtain a
dynamic version of Figure 9 in 10, where the model sizes and number of tokens are variable. These findings
validate that data-conditioning is only mildly dependent on the model and data scale. It means that data-
conditioning can be validated through small-scale proxy models, and then leveraged with large-scale models.
Conclusion
Classifier-based Quality Filtering is a tool used to train most state-of-the-art models, yet our analysis shows
that its inner workings are more subtle than previously believed. While CQF reliably improves downstream
evaluations, these gains are not attributable to the fact that filtered data are closer to the high-quality set.
Instead, we uncover an implicit filtering phenomenon, where CQF emphasizes HQ examples that are far from
the bulk of the LQ set, and are therefore most likely to be of higher quality. This quality filtering is about
removing the “bad”, not only imitating the “good”.
Most importantly, our work offers two key practical contributions: (i) we show that while CQF improves
downstream performance, it does not do so by simply mimicking the high-quality distribution and we show-
11
[p.12]
cased concrete examples where training on CQF data even outperforms training directly on the HQ set when
data scarcity is not a limiting factor; (ii) we introduce an optimization-driven notion of dataset quality and
demonstrate that it can be accurately estimated using small-scale proxies, providing a practical tool for
dataset evaluation before large-scale training.
Finally, we challenge the notion of quality defined by CQF, demonstrating that it does not satisfy the
desirable property we introduce ofdata-conditioning: training on “better quality” data, according to CQF,
does not accelerate learning on lower quality subsets. CQF should only be seen as a way to better align with
downstream evaluations.
Recommendations
The primary value of quality filtering is removing bad data at scale, not carving out a tiny “golden” subset.
In general, small high-quality sets are more useful for quality-filtering than for pretraining, due to their lack
of diversity. CQF acts as a form of bootstrapping: the high-quality set provides signal, and the large corpus
provides coverage.
Impact Statement
This paper presents work whose goal is to advance the field of Machine Learning. There are many potential
societal consequences of our work, none which we feel must be specifically highlighted here.
References
Alon Albalak, Yanai Elazar, Sang Michael Xie, Shayne Longpre, Nathan Lambert, Xinyi Wang, Niklas Muennighoff,
Bairu Hou, Liangming Pan, Haewon Jeong, et al. A survey on data selection for language models.arXiv preprint
arXiv:2402.16827, 2024.
Loubna Ben Allal, Anton Lozhkov, Guilherme Penedo, Thomas Wolf, and Leandro von Werra. Smollm-corpus, July
2024. URLhttps://huggingface.co/datasets/HuggingFaceTB/smollm-corpus.
Yoshua Bengio, Jérôme Louradour, Ronan Collobert, and Jason Weston. Curriculum learning. InProceedings of the
26th annual international conference on machine learning, pages 41–48, 2009.
Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan,
Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are few-shot learners.Advances in neural
information processing systems, 33:1877–1901, 2020.
Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham,
Hyung Won Chung, Charles Sutton, Sebastian Gehrmann, et al. Palm: Scaling language modeling with pathways.
Journal of Machine Learning Research, 24(240):1–113, 2023.
Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot, Ashish Sabharwal, Carissa Schoenick, and Oyvind Tafjord.
Think you have solved question answering? try arc, the ai2 reasoning challenge.arXiv:1803.05457v1, 2018.
Thomas M Cover.Elements of information theory. John Wiley & Sons, 1999.
Nan Du, Yanping Huang, Andrew M Dai, Simon Tong, Dmitry Lepikhin, Yuanzhong Xu, Maxim Krikun, Yanqi
Zhou, Adams Wei Yu, Orhan Firat, et al. Glam: Efficient scaling of language models with mixture-of-experts. In
International conference on machine learning, pages 5547–5569. PMLR, 2022.
Angela Fan, Yacine Jernite, Ethan Perez, David Grangier, Jason Weston, and Michael Auli. ELI5: long form question
answering. In Anna Korhonen, David R. Traum, and Lluís Màrquez, editors,Proceedings of the 57th Conference
of the Association for Computational Linguistics, ACL 2019, Florence, Italy, July 28- August 2, 2019, Volume 1:
Long Papers, pages 3558–3567. Association for Computational Linguistics, 2019. doi: 10.18653/v1/p19-1346. URL
https://doi.org/10.18653/v1/p19-1346.
Zhaoye Fei, Yunfan Shao, Linyang Li, Zhiyuan Zeng, Hang Yan, Xipeng Qiu, and Dahua Lin. Query of cc: Unearthing
large scale domain-specific knowledge from public corpora.arXiv preprint arXiv:2401.14624, 2024.
12
[p.13]
David Grangier, Simin Fan, Skyler Seto, and Pierre Ablin. Task-adaptive pretrained language models via clustered-
importance sampling.arXiv preprint arXiv:2410.03735, 2024.
Trevor Hastie, Robert Tibshirani, Jerome Friedman, et al. The elements of statistical learning, 2009.
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and Jacob Steinhardt. Mea-
suring massive multitask language understanding. InInternational Conference on Learning Representations, 2021.
Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego
de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, et al. Training compute-optimal large language
models.arXiv preprint arXiv:2203.15556, 2022.
Armand Joulin, Edouard Grave, Piotr Bojanowski, Matthijs Douze, Hérve Jégou, and Tomas Mikolov. Fasttext. zip:
Compressing text classification models.arXiv preprint arXiv:1612.03651, 2016.
Julie Kallini, Isabel Papadimitriou, Richard Futrell, Kyle Mahowald, and Christopher Potts. Mission: Impossible
language models.arXiv preprint arXiv:2401.06416, 2024.
Nathan Lambert, Valentina Pyatkin, Jacob Morrison, LJ Miranda, Bill Yuchen Lin, Khyathi Chandu, Nouha Dziri,
Sachin Kumar, Tom Zick, Yejin Choi, Noah A. Smith, and Hannaneh Hajishirzi. RewardBench: Evaluating reward
models for language modeling. InFindings of the Association for Computational Linguistics: NAACL 2025, pages
1755–1797. Association for Computational Linguistics, April 2025. doi: 10.18653/v1/2025.findings-naacl.96.
Jeffrey Li, Alex Fang, Georgios Smyrnis, Maor Ivgi, Matt Jordan, Samir Yitzhak Gadre, Hritik Bansal, Etash Guha,
Sedrick Scott Keh, Kushal Arora, et al. Datacomp-lm: In search of the next generation of training sets for language
models.Advances in Neural Information Processing Systems, 37:14200–14282, 2024.
Wing Lian, Bleys Goodson, Eugene Pentland, Austin Cook, and Chanvichet Vong. Teknium.Openorca: An open
dataset of gpt augmented flan reasoning traces. https://https://huggingface. co/Open-Orca/OpenOrca, 2023.
Shayne Longpre, Gregory Yauney, Emily Reif, Katherine Lee, Adam Roberts, Barret Zoph, Denny Zhou, Jason Wei,
Kevin Robinson, David Mimno, et al. A pretrainer’s guide to training data: Measuring the effects of data age,
domain coverage, quality, & toxicity. InProceedings of the 2024 Conference of the North American Chapter of
the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), pages
3245–3276, 2024.
Luke Merrick, Danmei Xu, Gaurav Nuti, and Daniel Campos. Arctic-embed: Scalable, efficient, and accurate text
embedding models.arXiv preprint arXiv:2405.05374, 2024.
David Mizrahi, Anders Boesen Lindbo Larsen, Jesse Allardice, Suzie Petryk, Yuri Gorokhov, Jeffrey Li, Alex Fang,
Josh Gardner, Tom Gunter, and Afshin Dehghan. Language models improve when pretraining data matches target
tasks.arXiv preprint arXiv:2507.12466, 2025.
Keiran Paster, Marco Dos Santos, Zhangir Azerbayev, and Jimmy Ba. Openwebmath: An open dataset of high-quality
mathematical web text, 2023.
Guilherme Penedo, Quentin Malartic, Daniel Hesslow, Ruxandra Cojocaru, Hamza Alobeidli, Alessandro Cappelli,
Baptiste Pannier, Ebtesam Almazrouei, and Julien Launay. The refinedweb dataset for falcon llm: Outperforming
curated corpora with web data only.Advances in Neural Information Processing Systems, 36:79155–79172, 2023.
Guilherme Penedo, Hynek Kydlíček, Anton Lozhkov, Margaret Mitchell, Colin A Raffel, Leandro Von Werra, Thomas
Wolf, et al. The fineweb datasets: Decanting the web for the finest text data at scale.Advances in Neural
Information Processing Systems, 37:30811–30849, 2024.
Mustafa Shukor, Louis Bethune, Dan Busbridge, David Grangier, Enrico Fini, Alaaeldin El-Nouby, and Pierre Ablin.
Scaling laws for optimal data mixtures.arXiv preprint arXiv:2507.09404, 2025.
Luca Soldaini, Rodney Kinney, Akshita Bhagia, Dustin Schwenk, David Atkinson, Russell Authur, Ben Bogin, Khy-
athi Raghavi Chandu, Jennifer Dumas, Yanai Elazar, et al. Dolma: an open corpus of three trillion tokens for
language model pretraining research. InACL (1), 2024.
Teknium. Openhermes 2.5: An open dataset of synthetic data for generalist llm assistants, 2023. URLhttps://huggingface.
co/datasets/teknium/OpenHermes-2.5.
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste
Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, et al. Llama: Open and efficient foundation language models.
arXiv preprint arXiv:2302.13971, 2023.
13
[p.14]
Tongzhou Wang, Jun-Yan Zhu, Antonio Torralba, and Alexei A Efros. Dataset distillation.arXiv preprint
arXiv:1811.10959, 2018.
Yudong Wang, Zixuan Fu, Jie Cai, Peijun Tang, Hongya Lyu, Yewei Fang, Zhi Zheng, Jie Zhou, Guoyang Zeng,
Chaojun Xiao, et al. Ultra-fineweb: Efficient data filtering and verification for high-quality llm training data.arXiv
preprint arXiv:2505.05427, 2025.
Maurice Weber, Daniel Y. Fu, Quentin Anthony, Yonatan Oren, Shane Adams, Anton Alexandrov, Xiaozhong Lyu,
Huu Nguyen, Xiaozhe Yao, Virginia Adams, Ben Athiwaratkun, Rahul Chalamala, Kezhen Chen, Max Ryabinin,
Tri Dao, Percy Liang, Christopher Ré, Irina Rish, and Ce Zhang. Redpajama: an open dataset for training large
language models.NeurIPS Datasets and Benchmarks Track, 2024.
Johannes Welbl, Amelia Glaese, Jonathan Uesato, Sumanth Dathathri, John Mellor, Lisa Anne Hendricks, Kirsty
Anderson, Pushmeet Kohli, Ben Coppin, and Po-Sen Huang. Challenges in detoxifying language models. In
Findings of the Association for Computational Linguistics: EMNLP 2021, pages 2447–2469, 2021.
Guillaume Wenzek, Marie-Anne Lachaux, Alexis Conneau, Vishrav Chaudhary, Francisco Guzmán, Armand Joulin,
and Édouard Grave. Ccnet: Extracting high quality monolingual datasets from web crawl data. InProceedings of
the Twelfth Language Resources and Evaluation Conference, pages 4003–4012, 2020.
Sang Michael Xie, Shibani Santurkar, Tengyu Ma, and Percy S Liang. Data selection for language models via
importance resampling.Advances in Neural Information Processing Systems, 36:34201–34227, 2023.
Mozhi Zhang, Howe Tissue, Lu Wang, and Xipeng Qiu. Domain2vec: Vectorizing datasets to find the optimal
data mixture without training. InForty-second International Conference on Machine Learning, 2025. URLhttps:
//openreview.net/forum?id=kJ5i29FejW.
Xinlin Zhuang, Jiahui Peng, Ren Ma, Yinfan Wang, Tianyi Bai, Xingjian Wei, Jiantao Qiu, Chi Zhang, Ying Qian,
and Conghui He. Meta-rater: A multi-dimensional data selection method for pre-training language models.arXiv
preprint arXiv:2504.14194, 2025.
14
[p.15]
Appendix
A Appendix organization
The appendix is organized as follows:
•In Appendix B, we study how the optimal fractionkof selected data in CQF varies with model size
and training compute, the HQ set and the downstream task.
•In Appendix C, we highlight that CQF classifiers are prone to learning spurious features, such as
context length, and we evaluate the effectiveness of a simple mitigation strategy. This illustrates a
broader phenomenon: CQF can induce undesired biases that cause the selected pretraining data to
diverge significantly from the HQ set.
•In Appendix D, we reveal that no single HQ set leads to universally better downstream performance,
and that different classifiers implicitly align with different benchmarks, revealing task-specific inductive
biases.
•In Appendix E, we visualize the binary relation induced quality filtering as a graph, highlighting how
its structure evolves from the semi-synthetic setting to CQF used in practice.
•In Appendix F, we provide the reader with further implementation details.
B Optimal thresholds vary with compute
How to chose the optimalkwhen picking the topk%documents from CQF? To answer this, we conducted
a series of ablations overk, training models on the topk%of the pretraining data, as ranked by CQF, using
various HQ sets. These experiments span multiple model sizesNand training horizonsD(i.e., number of seen
tokens), such that the total training compute in FLOPs is measured as6N D. The results are summarized in
Figure 11, where we report downstream accuracy as a function of training FLOPs and highlight the optimal
kin each setting.
Although our setup directly illustrates CQF, making it more representative of real-world data filtering
pipelines, Mizrahi et al. (2025) concurrently explore a related direction. Their approach differs in that
they select LQ data based on direct proximity to target benchmarks, bypassing the need for a proxy HQ
dataset. Despite this, our findings do not align: we observe no clear trend once the noise level is accounted
for, leading to relatively inconclusive results. We also note that Mizrahi et al. (2025)’s conclusions rely on
extrapolation, which probably explains the divergence.
C Do classifiers used in CQF exhibit undesired biases?
Evenwhendownstreamperformanceimproves, theselecteddatacandriftfromtheintendedtargetdistribution—
revealing not only a failure to capture genuine quality, but also an undesirable inductive bias, where the
classifier overemphasizes unrelated features.
Whilst it is not trivial to exhibit such unwanted features among the learned ones by the classifier, we managed
to identify one of these for OpenOrca as HQ set: the classifier seems to associate quality with the sequence
length, and shorter sentences have higher chances to be classified as high quality ones, see Figure 13.
When sampling from the positive class (OpenOrca dataset) prior to training the corresponding classifier, we
subsample documents with an imposed sequence length of at least500or700. We then use this classifier to
produce a partition of RedPajama with an updated notion of quality, that we hope to be seemingly better
or at least not mistakenly taking sequence as a proxy for quality; see columns 3 and 4 of Figure 13. We
train 350M models on the resulting partitions of RedPajama and evaluate them on ARC (Clark et al., 2018),
MMLU (Hendrycks et al., 2021), and Reward Bench (Lambert et al., 2025). We show in Figure 14 the result
of such experiments, averaged across 3 runs.
15
[p.16]
0.24
0.26
OpenOrca
MMLU
0.24
0.26
0.28
MMLC
0.56
0.58
reward-bench
0.20
0.25
ARC-Challenge
0.3
0.4
0.5
0.6
ARC-Easy
0.24
0.26
OH+ELI5
0.24
0.26
0.28
0.30
0.56
0.58
0.20
0.25
0.30
0.4
0.5
0.6
1019 1020
FLOPs
0.23
0.24
0.25
0.26
KnowledgePile
1019 1020
FLOPs
0.24
0.26
0.28
1019 1020
FLOPs
0.56
0.58
1019 1020
FLOPs
0.15
0.20
0.25
0.30
1019 1020
FLOPs
0.3
0.4
0.5
0.6
100% 50% 10% 5% 2% 1%
Train on top
Model size
125M 350M 700M 1.3B
Figure 11The optimal topk%of pretraining data depends on available compute.For each setting, we
highlight the value ofkthat yields the best performance under a fixed compute budget.Rows: different HQ sets
used for CQF.Columns: various downstream performance metrics.
−10 −5 0
x
−10 −5 0
x
assign to buckets
Lowest ← quality→ Highest
CQF log-score
RedPajamaV2 OpenOrca
Figure 12CQF works by filtering out the low-quality data (red),notbecause the retained data (green) resemble
the HQ set (orange).
16
[p.17]
1%2%5%10%25%50%100%
500
600
700
800
900Effective sequence length
KnowledgePile
1%2%5%10%25%50%100%
200
400
600
800
OpenOrca
1%2%5%10%25%50%100%
200
400
600
800
OpenOrca debiased – Long positives
1%2%5%10%25%50%100%
200
400
600
OpenOrca debiased – Short negatives
0 1 2 3 4 5 6 7 8 9
Classiﬁer quality estimates for the Positives
Figure 13CQF classifiers suffer from inductive biases.Because the OpenOrca dataset (HQ set) contains shorter
sequences than RedPajama (LQ set), the classifier in CQF learns to use sequence length as proxy for quality scores
(second column). This bias persists even after filtering out long documents from OpenOrca (third column), and
only disappears when we subsample the negative class to match shorter sequence lengths (fourth column). In
contrast, the classifier from CQF using KnowledgePile as a HQ set (first column) does not exhibit this behavior.
The red dotted line indicate the effective sequence length in the HQ set, while the blue line shows the sequence length
of data filtered by CQF at different selection ratios along the x-axis. The HQ set is divided into 10 quality deciles,
and the sequence lengths for each decile are shown as solid horizontal lines, with color indicating quality level.
1%5%25%100%
Train on top
0.23
0.24
0.25
MMLU
1%5%25%100%
Train on top
0.255
0.260
MMLC
1%5%25%100%
Train on top
0.55
0.56
0.57
reward-bench
1%5%25%100%
Train on top
0.46
0.48
0.50
0.52
ARC-Easy
1%5%25%100%
Train on top
0.20
0.22
0.24
ARC-Challenge
OpenOrca OpenOrca debiased — Long positives OpenOrca debiased — Short negatives
Figure 14Performance after debiasing the classifier from CQF with OpenOrca as a HQ set.The classifier
was retrained with a subsampled HQ set (OpenOrca) using minimum sequence lengths, in an effort to remove length-
based bias in quality scores.
−10 −5 0 5 10 15 20
−10
−5
0
5
10 Benchmarks
mmlu
reward-bench
ARC-Easy
ARC-Challenge
Classiﬁers
mmlu
reward-bench
ARC-Easy
ARC-Challenge
Classiﬁers
mmlu
reward-bench
ARC-Easy
ARC-Challenge
Figure 15UMAP of sBert centroids for each (exclusive) quality bucket.Even when quality classifiers are
trained directly on the target data, they may still capture undesirable features. Consequently, the top-rated RedPa-
jama quality buckets (darker colors) are not always the closest to the target benchmark embeddings.
17
[p.18]
Figure 16PCA of sBert embeddings of (exclusive) quality buckets induced by different classifiers.Even
when quality classifiers are trained directly on the target downstream tasks, they may still capture undesirable
features. Consequently, the top-rated RedPajama quality buckets (darker colors) are not always the closest to the
target benchmark embeddings.
Beyond this specific case of sequence length bias, we investigate whether CQF classifiers exhibit similar
issues, when trained on HQ sets drawn directly from target benchmarks. To assess this, we compute sBert
embeddings for RedPajama documents grouped by CQF quality scores and compare them to embeddings
of the benchmark data. As shown in Figure 15, we visualize the centroids of each quality bucket using a
two-dimensional UMAP projection. Ideally, higher-quality buckets as ranked by CQF (darker colors) would
be closer to the benchmark embeddings. We provide the same visualization in Figure 16 using a PCA.
Surprisingly, this is often not the case, suggesting that classifiers may still rely on spurious correlations or
unrepresentative features of the entire HQ set.
Finally, we provide a 2D visualization of the sBert latent space using a tSNE from which similar conclusions
can be drawn in that only a subset of the HQ set is matched by the data retained from CQF.
Joint TSNE of CQF and HQ set
Domain
HQ set: OpenOrca
CQF in top 100%
CQF in top 25%
CQF in top 2%
CQF in top 1%
Figure 172D TSNE of sBert embeddings of OpenOrca and CQF samples. The TSNE reveals the same insights
as the 2D PCA in Figure 4. This method also shades lights on the difficulty of properly projecting and representing
in 2D a 384-dim geometry.
D No HQ set is superior to all others across all tasks
While various HQ sets are used in the literature for CQF, no single HQ consistently outperforms others across
all downstream tasks. Figure 18 shows that varying HQ sets yield various performance across tasks, with no
18
[p.19]
universal dominance. Downstream evaluations are noisy, but we observe the consistent trend that OH+ELI5
is a good baseline across tasks, confirming the findings of Li et al. (2024). We also notice that KnowledgePile,
despite poor diversity in the style, induce a bias toward data is are more heavily leaning toward knowledge
benchmarks like ARC.
This suggests that each HQ set imparts its own inductive biases, influencing which aspects of the data are
emphasized during filtering. To further understand these biases, we visualize the embedding space of the
data selected by each classifier in Figure 20. We observe that quality buckets across classifiers tend to
align with specific benchmark datasets, indicating that classifiers—implicitly or explicitly—favor data that
resembles their respective supervision targets. This aligns with recent concurrent work from Mizrahi et al.
(2025), who show that direct supervision using explicitly target benchmark data can boost performance on
that benchmark, though at the cost of generality. Taken together, these results highlight a central challenge
in CQF: quality is not a universal property, and each HQ set carries task-specific preferences that limit its
transferability.
1%2%5%10%25%50%100%
Train on top
0.24
0.26
MMLU
1%2%5%10%25%50%100%
Train on top
0.25
0.26
0.27
MMLC
1%2%5%10%25%50%100%
Train on top
0.54
0.56
0.58
reward-bench
1%2%5%10%25%50%100%
Train on top
0.45
0.50
0.55
ARC-Easy
1%2%5%10%25%50%100%
Train on top
0.20
0.25
ARC-Challenge
OpenOrca KnowledgePile OH+ELI5 openwebmath All targets
Figure 18Benchmark performance results from 350M modelstrained on documents ranked by quality according
to various CQF using various HQ sets.
All the manifold visualizations in Figure 19 and Figure 20 demonstrate the same trend: CQF selects data
closer to benchmarks as quality filtering goes.
Figure 19PCA embedding of (exclusive) buckets.This figure differs from Figure 3 by considering exclusive
buckets. Here, we see that the bottom 10% are quite different from each other, and the buckets of average quality (i.e
in the 70-30 range) tend to be similar across quality classifiers.
−5 0 5 10 15 20
−15
−10
−5
0
5
10
Benchmarks
mmlu
reward-bench
ARC-Easy
ARC-Challenge
Classiﬁers
OpenOrca
KnowledgePile
OH+ELI5
openwebmath
Classiﬁers
OpenOrca
KnowledgePile
OH+ELI5
openwebmath
Figure 20Each HQ set used in CQF appears to favor task-specific data.Two-dimensional UMAP of sBert
centroids for each (exclusive) quality bucket as defined by each classifier. Darker color indicates increasing selection
ratiok.
19
[p.20]
0.0
0.5
1.0
1.5
Loss improvement
0
20
40
60
80
100
Contamination (%)
Figure 21Data-conditioning≻on the Perm task.This graph exhibits the properties of a total ordering, closer
to an intuitive notion of quality. The only “backward” edge is linking the the two worse splits, and the loss difference
is within standard deviation.
E Data-conditioning
We revisit the experiments of Figure 9 by materializing the graph induced by the binary relation≻. For
an arbitrary algorithmAit is hard to characterize the datasetsD clean andD dirty. Therefore, we rely on
empirical measurements draw edges when the loss improvement is significant (e.g. bigger than the standard
deviation). The results are given in figures 21 and 22.
F Implementation details
Hyper-parameters relative to our training setup are detailed in Table 2.
Table 2Hyperparameters used for training models.
125M 350M 1.3B
Architecture
Vocab Size 32K 32K 32k
Embedding dim. 768 1,024 2,048
Latent dim. 3072 4,096 8,192
Num. heads 16 16 16
Depth 12 24 24
Context lenght 1,024 1,024 1,024
Optimization
Batch size (tokens) 115K 32K 115K
Learning rate scheduler lin. decay lin. decay lin. decay
Learning rate peak1e −4 1e−4 1e−4
Grad clipping 5.0 5.0 5.0
Steps 64K 256K 1M
Num. train tokens 8B 8B 120B
20
[p.21]
0.00
0.02
0.04
0.06
0.08
0.10
Loss improvement
0
20
40
60
80
100
CQF (%)
Figure 22Data-conditioning≻on OpenOrca CQF.On these exclusive buckets, there is no global ordering. The
bottom 30% (red) and the top 5% (green) are dominated by bucket of “average” quality (possibly with more diversity).
The node size is proportional to the number of examples in the bucket. On this graph, the relation is transitive, which
induces an ordering, but this ordering is not total.
21
