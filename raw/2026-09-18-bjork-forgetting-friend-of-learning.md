---
title: "Forgetting as a Friend of Learning（专著章节，Robert A. Bjork，2014）"
author: Robert A. Bjork（University of California, Los Angeles；Distinguished Research Professor, Department of Psychology）
url: https://bjorklab.psych.ucla.edu/wp-content/uploads/sites/13/2016/11/RABjork_JacobyFestschriftChapterFigsEmbedded052014.pdf
kind: paper
published: 2014 —— PDF 首页标注 "(in press)"；出版方记为 2014-11-13
  （D. S. Lindsay, C. M. Kelley, A. P. Yonelinas, & H. L. Roediger III (Eds.),
  *Remembering: Attributions, processes, and control in human memory: Papers in honour of Larry L. Jacoby*.
  New York: Psychology Press. ISBN 9781848725546 / 9781315752808）
clipped: 2026-09-18
capture_quality: high
capture_method: >
  `curl -sL` 直接下载作者本人实验室（UCLA Bjork Learning and Forgetting Lab）官网公开的 PDF 原件，
  再用 pypdf 逐页提取文本 —— **未走任何 AI 中介、未做 OCR、未重写**。
  页数 **23** ｜ 正文 39,272 字符 / 687 行（含每页 `[p.N]` 分隔标记）。
  **文本层完好** —— 这是本库收录的第三份 PDF 素材里第一份「下载即用」的（另见 capture_note）。
  原件已 `cp` 至 `raw/assets/2026-09-18-bjork-forgetting-friend-of-learning.pdf`（1,758,409 字节）。
  **正文未做任何清洗** —— 每页的页眉（`FORGETTING AS A FRIEND OF LEARNING  N`）与制表符
  按 pypdf 提取的原样保留。按「raw 不可变」原则，抓到什么存什么。
capture_note: >
  **本字段只记「抓取事实」，不记「阅读结论」。**（`AGENTS.md` 1.1）
  本素材的分段、行区间、机制清单、与库内既有页面的校准结果一律维护在
  wiki/sources/2026-09-18-bjork-forgetting-friend-of-learning.md —— 它们会随阅读深入而变。

  **行区间坐标系：文件绝对行号**（`wc -l` 的坐标系）。引用前必须回文件 `sed -n` 核对。
  **注意**：本文件每页正文前有一个 `[p.N]` 标记行，**行号与 PDF 页码不是一回事**，不可混用。

  **已知缺失：** Figure 1（学习曲线 / 反应时曲线，11 种间隔序列）与 Figure 2
  （storage / retrieval strength 的增益函数示意）的**图内数值进不了文本层** ——
  两张图的**图注文字**均已提取（图 1 注在 p.3，图 2 注在 p.6–p.7），可作为图意的权威表述。
  另：全文图表共 2 幅，均为示意图而非数据表。

  **一条本库首次遇到的抓取事实（重要）：** 同一实验室官网上
  **Bjork & Bjork (1992)《A New Theory of Disuse》原文 PDF 是扫描件、无文本层** ——
  17 页、1.6 MB，pypdf 逐页提取结果全为空。**可下载 ≠ 可取回文本。**
  本素材（2014 章节）之所以被选中，正是因为它**有文本层且正面复述了 1992 理论的核心公式**。
  **推论：1992 原文若要入库，需 OCR 或另找有文本的版本 —— 这是本库第一条因技术形态而非内容被卡的文献。**

  **利益披露：** 无。作者为 UCLA 荣休杰出研究教授，本章为学术纪念文集（Festschrift）章节，
  无产品、课程或商业引流；全文未检出 UTM 参数。

---

[p.1]
FORGETTING	
  AS	
  A	
  FRIEND	
  OF	
  LEARNING	
   1	
  
	
  
 
Forgetting as a Friend of Learning 
[In D. S. Lindsay, C. M. Kelley, A. P. Yonelinas, & H. L. Roediger, III (Eds.) Remembering: 
Attributions, processes, and control in human memory: Papers in honour of Larry L. Jacoby. 
New York: Psychology Press. (in press)] 
Robert A. Bjork 
University of California, Los Angeles 
 
 
 
 
 
 
 
 
 
 
Correspondence: 
 Robert A. Bjork, Distinguished Research Professor 
 Department of Psychology 
 University of California 
 Los Angeles, CA 90095-1563 
 rabjork@psych.ucla.edu 
	
   	
  
[p.2]
FORGETTING	
  AS	
  A	
  FRIEND	
  OF	
  LEARNING	
   2	
  
Forgetting as a Friend of Learning 
It is natural to think that learning is a matter of building up skills or knowledge in one’s 
memory and that forgetting is a matter of losing some of what was built up.  From that 
perspective, learning is a good thing and forgetting is a bad thing.  The relationship between 
learning and forgetting is not, however, so simple, and in certain important respects is quite the 
opposite: Conditions that produce forgetting often enable additional learning, and learning or 
recalling some things can contribute to forgetting other things.  In this chapter I focus on why 
forgetting enables, rather than undoes, learning.   
Among his multitude of contributions to research on human learning and memory, Larry 
Jacoby was among the first to emphasize that forgetting can facilitate learning.  In an important 
early paper (Jacoby, 1978; also see Cuddy & Jacoby, 1982), Larry characterized restudying after 
not forgetting as “remembering the solution” and restudying after forgetting as “solving a 
problem”—that is, again carrying out activities that have the potential to enhance subsequent 
retention.  I discuss Larry’s arguments and results later in this chapter.   
My own interest in the relationship between forgetting and learning goes back to my 
graduate-student days at Stanford University, during the heyday of fitting learning and memory 
data with multi-state Markov models.  David Rumelhart and I (Bjork, 1966; Rumelhart, 1967) 
got caught up in the challenge of trying to account for the trial-by-trial short-term-memory and 
long-term-learning effects of any arbitrary spacing of successive inter-trial intervals during 
paired associate learning.  The idea behind what became my dissertation was to do away with the 
usual constraint that a given pair in a to-be-learned list of paired associates does not come up 
again until the next cycle through the list—a constraint that makes short and long intervals 
between successive presentations of a given item very infrequent.  Instead, I let each successive 
interval for a given pair be determined randomly from a uniform distribution of intervals, which 
[p.3]
FORGETTING	
  AS	
  A	
  FRIEND	
  OF	
  LEARNING	
   3	
  
led to highly variable inter-presentation sequences, such as the examples shown in Figure 1, 
where the proportion of correct responding and the latency of responding are shown as a function 
of trial number and the spacing between successive trials.  
 
 
Figure 1.  Learning curves and response-time curves as a function of 11 of the 21 different 
sequences of successive inter-presentation intervals used by Bjork (1966).  In contrast to the way 
that learning curves are typically plotted, successive trials are spaced on the abscissa in accord 
with the actual spacing between successive trials for a given sequence.  The curves illustrate how 
much performance can vary as a function of successive intervals, a variation that is averaged 
away when learning curves are plotted in the typical fashion.   
 

[p.4]
FORGETTING	
  AS	
  A	
  FRIEND	
  OF	
  LEARNING	
   4	
  
I was able to account in some detail for both the short-term and long-term effects of 
arbitrary sequences of inter-presentation intervals with a Markov model that assumed that a 
given pair could be in one of four states of knowledge: an initial unlearned state, a short-term 
memory state, a forgotten state, and a (permanently) learned state.  Of relevance to the present 
chapter—and shocking at the time—the best fitting estimate of the probability of transitioning to 
the learned state if an item was still in the short-term memory state from the prior trial, and had 
not been learned already, was exactly zero.  Thus, for learning to happen, the item needed to be 
forgotten from short-term memory prior to its next presentation.   
In the years that followed, my students, collaborators, and I found other instances where 
forgetting enabled learning, usually in the context of exploring some other issue.  Ted Allen and 
I, for example, in an experiment designed to discriminate between alternative explanations of the 
spacing effect (that long-term recall is enhanced by spacing, rather than massing, repeated study 
sessions), found that a more difficult intervening activity could both produce more forgetting and 
enhance learning (Bjork & Allen, 1970).  On each trial, participants studied a set of three words 
and then had to carry out an easy or difficult intervening task (shadowing aloud 3-digit or 5-digit 
numbers every 1.5 seconds, respectively).  On an unpredictable half of the trials they were asked 
to recall the set of words, whereas on the other trials they were presented the words again to 
restudy, after which there was a longer period of medium-difficulty shadowing (4-digit numbers 
every 1.5 second) before they were cued to recall the to-be-remembered words.   
We found, not surprisingly, that the more difficult intervening task caused more 
forgetting: 45 percent of the word trigrams were recalled correctly after 12 seconds of the easy 
task, whereas only 32 percent of the trigrams were recalled correctly after the difficult task.  
When the trigrams were presented again for restudy, however, rather than tested, and then tested 
[p.5]
FORGETTING	
  AS	
  A	
  FRIEND	
  OF	
  LEARNING	
   5	
  
after 30 seconds of the medium difficulty shadowing task, the relationship reversed: 70 percent 
of the trigrams were recalled correctly when the interval between presentations was filled with 
the easy task, whereas 77 percent of the trigrams were recalled correctly when the interval was 
filled with the more difficult task.  Thus, the more difficult task produced more forgetting, but 
enhanced learning. With respect to the main motivation for the study, the findings also argued 
against a consolidation interpretation of spacing effects (why should there be more consolidation 
of the first presentation during a difficult, versus easy, subsequent activity?).   
Not long thereafter, Steve Smith, Arthur Glenberg, and I found that changing the 
environmental context from study to test could also produce forgetting, but enhance learning.  
When materials were studied in one room on the University of Michigan campus and then, 3 
hours later, either tested in that room or a very different room, we found that changing the 
context from study to test impaired recall.  If, though, the materials were restudied, rather than 
tested, we then found that the change in context enhanced later recall, as measured by recall in a 
neutral room 3 hours after the second study session.   
Beyond the evidence that a more difficult intervening activity, or a change of 
environmental context, can both produce forgetting and enhance learning, there is, of course, the 
spacing effect, itself.  That is, there is 130 years or so of evidence that lengthening the interval 
from a first study opportunity to a test or second study opportunity can both increase forgetting, 
but enhance learning.  Melton (1967), for example, described the spacing effect as paradoxical—
because it suggested that forgetting can help memory.   
Conjectures as to Why Forgetting Enables Learning 
In the theoretical framework that Elizabeth Bjork and I refer to as “a new theory of disuse” 
(Bjork & Bjork, 1992), a framework that has guided much of our recent research, the fact that 
[p.6]
FORGETTING	
  AS	
  A	
  FRIEND	
  OF	
  LEARNING	
   6	
  
inducing forgetting can enhance learning is explained in terms the theory’s distinction between 
storage strength versus retrieval strength.  The retrieval strength of an item in one’s memory 
reflects its current ease of access—that is, how primed or activated it is in the context of current 
cues—whereas the storage strength of that item reflects how interassociated or “entrenched” it is 
with everything else in one’s memory.  Current retrieval strength is assumed to determine 
completely the probability that an item can be recalled, whereas storage strength acts as a latent 
variable that retards the loss or enhances the gain of retrieval strength.  Thus, many items in 
memory, as an old friend’s name, a street address we once had, or our high-school French, can 
be strongly registered in memory in the storage-strength sense, but be non-recallable because 
their retrieval strength, via disuse, has become too low to support recall.   
The distinction between storage strength and retrieval strength corresponds, in a general 
way, to the time-honored distinction between learning and performance (for a recent discussion 
of the learning-versus-performance distinction in the domains of cognitive/motor skills and 
verbal/conceptual learning, see Soderstrom & Bjork, 2013). What we can observe and measure is 
performance, which, in the theory, reflects retrieval strength; what we must infer is learning, 
which, in the theory, reflects storage strength.  Conceptually, the distinction is similar to Estes’ 
(1955) distinction between habit strength and response strength, to Melton’s (1963) distinction 
between trace storage and trace utilization, and to Tulving and Pearlstone’s (1966) distinction 
between availability and accessibility.   
Within the new-theory-of-disuse framework, the key to why forgetting can enable 
learning is the assumption that increments in storage strength are assumed to be a decreasing 
function of current retrieval strength.  That is, the more accessible an item in the retrieval-
strength sense, the smaller the increments (learning) caused by re-study in the storage-strength 
[p.7]
FORGETTING	
  AS	
  A	
  FRIEND	
  OF	
  LEARNING	
   7	
  
sense.  Thus, as shown in Figure 2, there is an asymmetry in terms of the interaction of storage 
strength and retrieval strength: Increments in retrieval strength due to re-study are larger the 
higher the current storage strength, but increments in storage strength due to re-study are smaller 
the higher the current retrieval strength.  
 
Figure 2. Illustration of the effects of a study trial assumed by the new theory of disuse (Bjork & 
Bjork, 1992).  Gains in retrieval strength are an increasing function of current storage strength, 
whereas gains in storage strength are a decreasing function of current retrieval strength.  
The new theory of disuse is not a process model. A number of mechanisms could 
underlie why increments in storage strength are a decreasing function of current retrieval strength.  
The leading contenders are summarized below. 
  

[p.8]
FORGETTING	
  AS	
  A	
  FRIEND	
  OF	
  LEARNING	
   8	
  
Encoding Variability  
As McGeoch (1932) might have been the first to emphasize, one contributor to forgetting 
is “altered stimulating conditions” (p. 365). That is, as a retention interval increases, so does—
typically—the discrepancy between the stimulus cues present at the time of test versus those that 
were present at the time of study.  Contextual cues, however, influence not only what is 
retrievable from memory, but also how information is encoded, so when to-be-learned 
information is re-presented, rather than tested, the altered cues provide opportunities for 
encoding that differ from, or add to, the original encoding.  That is, context change induces 
forgetting, but also can enhance learning via the to-be-remembered information becoming 
associated with a greater range of contextual cues.  Such increased encoding variability helps to 
sustain access to that information, especially at a delay and as contextual cues change.   
Estes (1955) formalized such a mechanism in his stimulus-fluctuation model, originally 
proposed to account for forgetting and spontaneous-recovery phenomena in animal learning.  
The model assumes that the animal samples from among the stimulus “elements” available at the 
time of a test trial and that the proportion of cues already associated to some target response 
determines the likelihood the response is executed.  Forgetting occurs in the model because the 
stimulus elements in the situation are assumed to fluctuate between being “available” for 
sampling and being “unavailable” for sampling, owing to changes in the animal’s orientation, 
body state, and so forth.  Elements conditioned to some target response can be replaced by 
unconditioned elements owing to such fluctuation, which decreases the probability of responding 
with the target response.  Such “replacements,” however, also make new elements available for 
conditioning—that is, can enhance learning by increasing the total number of elements 
conditioned to the target response, which is what will determine performance in the long term.  
From a formal standpoint, the proportion of conditioned elements in the currently available cues 
[p.9]
FORGETTING	
  AS	
  A	
  FRIEND	
  OF	
  LEARNING	
   9	
  
corresponds to retrieval strength in the new theory of disuse and the proportion of conditioned 
elements in total populations of elements corresponds, roughly, to storage strength.   
As already mentioned, Estes formulated the fluctuation model to account for various 
forgetting, spacing, and spontaneous-recovery findings in the animal-learning literature.   Gordon 
Bower (1972) extended and elaborated the model to account for a range of human-learning 
phenomena, and the basic fluctuation mechanism has been incorporated into more recent 
quantitative models (e.g., Glenberg, 1979; Mensink & Raiijimakers, 1988).  
Retrieval—and/or Reminding—as a Learning Event 
A basic fact about human memory is that retrieving information from long-term memory 
is fallible and probabilistic.  Another basic fact is that the act of retrieval is a learning event—or 
“memory modifier” (Bjork, 1975)—in the sense that the retrieved information becomes more 
recallable in the future than it would have otherwise.  In fact, retrieval is a powerful learning 
event, one that is substantially more powerful than is restudying (for a review of “test effects,” 
see Roediger & Karpicke, 2006b).   
Importantly, for present purposes, the more difficult or involved the act of retrieval the 
more it facilitates subsequent retrieval (e.g., Whitten & Bjork, 1977).  Thus, retrieval of 
procedures and skills from memory can be viewed as a kind of skill—one that, like other skills, 
profits from practice—and retrieval events during learning that are more difficult or involved, 
owing to forgetting (loss of retrieval strength) during the learning process itself, constitute better 
practice for later efforts to retrieve (Bjork, 1988; Thios & D’Agostino, 1976).  That is, as events 
pass and cues change across intervals during the acquisition of process, retrieval of what has 
been studied or practiced earlier during the acquisition process becomes more difficult, but also 
more like the retrieval processes required on the post-acquisition final test.  From that 
[p.10]
FORGETTING	
  AS	
  A	
  FRIEND	
  OF	
  LEARNING	
   10	
  
perspective, embedded tests during the acquisition process constitute better practice for the final 
test than do restudy opportunities, which helps to explain why testing, even without feedback, 
can produce better post-acquisition performance than does restudying, especially after a long 
retention interval.    
Restudying does, though, enhance later recall and—in the case of restudying—the 
argument is that the re-representation of the to-be-learned material triggers “reminding,” that is, 
recollecting—or reconstructing—the initial study episode (for discussions of the broader roles of 
reminding, see Benjamin & Ross, 2011; Benjamin & Tullis, 2010; and Hintzman, 2010, 2011).  
Again, the more difficult or involved such reminding is, provided it succeeds, the larger at the 
benefits, so forgetting, up to a point, enhances the benefits of reminding (e.g., Appleton-Knapp, 
Bjork, & Wickens, 2005; Cuddy & Jacoby, 1982), as measured by later recall.    
Solving a Problem versus Remembering the Solution 
Jacoby (1978) argued that fluent remembering of a prior presentation of some to-be-
learned material results in the learner bypassing processing activities that would otherwise be 
required, activities of the type that enhance later recall.  To illustrate, he used the following 
example (p. 649):  
“Suppose that you are asked to find the sum of 37 + 15 + 12.  After having obtained this 
sum you are immediately presented with the same problem.  The type of processing that 
you do will differ drastically on the repeated presentation.  On the first encounter you 
undoubtedly went through the process of addition to obtain the sum; on the second 
encounter, the sum is readily available and can be given without going back through the 
operation of adding the numbers.  Indeed, a full repetition of the processing activities 
may be difficult, if not impossible, without some delay.   
[p.11]
FORGETTING	
  AS	
  A	
  FRIEND	
  OF	
  LEARNING	
   11	
  
Jacoby goes on to argue that the effects of spacing repetitions of to-be-learned materials 
can act in a similar fashion.  Memorizing a list of words or paired associates can be thought of as 
confronting a series of problems: The learner must find processing activities that will make a 
given item recallable on a final test, such as creating an image of the referent of a to-be-recalled 
word.  In the case of a repeated presentation of a to-be-remembered word, however, it will be 
difficult or impossible to carry out additional productive processing if the processing of the 
initial presentation remains easily accessible.  That is, “remembering the solution” will impede 
“[re]solving the problem.”   
Jacoby (1978) and Cuddy and Jacoby (1982) went on to demonstrate in various ways that 
reducing the accessibility of the prior processing of a to-be-learned item—that is, inducing 
forgetting—enhanced the effectiveness of restudying the item, as measured by later recall.  The 
results of Jacoby’s (1978) Experiment 1, shown in Figure 4, provide a particularly dramatic 
example of how ineffective ”remembering the solution” can be for later recall. Participants had 
to learn paired associates that were either presented intact (e.g., FOOT: SHOE) or were 
presented with the cue word intact but with letters missing from the response word (e.g., FOOT: 
S**E), meaning that the response word had to be “constructed” from the cue word and letter 
cues.  After the study phase there was then a final cued-recall test (e.g., FOOT: __?__) for the 
studied pairs.   
As shown in Figure 4, when a given pair was presented only once, either in the “read” 
condition or the “construct” condition, final cued-recall test exhibited a very large generation 
benefit: The “construct” condition led to about twice the level of recall of the “read” condition.  
What is most striking though, is the pattern of findings for the pairs that were presented twice, 
either in a Read-Read condition (FOOT: SHOE; FOOT: SHOE) or in a Read-Construct 
[p.12]
FORGETTING	
  AS	
  A	
  FRIEND	
  OF	
  LEARNING	
   12	
  
condition (FOOT: SHOE; FOOT: S**E), and with either zero or twenty intervening trials on 
other pairs. With zero intervening pairs the Read-Construct condition, rather than combining the 
benefits of reading and constructing, resulted in a level of cued-recall performance that was 
much lower than the level produced by a single construct trial.  That is, when participants could 
simply remember the solution from the preceding trial, the benefits of constructing were minimal. 
When 20 trials—and, presumably, substantial forgetting—intervened between the initial study 
trial and the later construct trial, however, the construct again required “solving the problem,” 
which increased later recall substantially.  
 
Figure 3. Percent final cued recall of paired associates as a function of whether they were 
presented once, twice massed, or twice spaced.  On “Read” trials pairs were present intact (e.g., 
FOOT: SHOE), whereas on “Construct” trials the response word had to be constructed (e.g., 
FOOT: S**E).  Adapted from Jacoby (1978, Figure 1).   

[p.13]
FORGETTING	
  AS	
  A	
  FRIEND	
  OF	
  LEARNING	
   13	
  
Encoding the Gist, Rather than the Details 
In the context of inductive learning—that is, the learning of categories and concepts from 
examples—there is another conjecture as to why forgetting can enable learning.  Beginning with 
a study by Kornell and Bjork (2008), in which participants learned the styles of painters from 
examples of their paintings, there have now been a number of demonstrations that inductive 
learning, as measured by the ability to classify new examples, profits from interleaving and/or 
spacing the examples of different categories(e.g., Birnbaum, Kornell, Bjork, & Bjork, 2013; 
Kang & Pashler, 2012; Kornell, Castel, Eich, & Bjork, 2010; Vlach, Kornell, & Sandhofer, 2008; 
Wahlheim, Dunlosky, & Jacoby, 2011).  These findings have stirred considerable interest, not 
only because it would seem, a-priori, that blocking or massing the examples of a given category 
would make the commonalities across examples that define the category maximally apparent, but 
also because participants believe that blocking, not interleaving, facilitates learning (even after 
their final-test performance has demonstrated the opposite).   
When and why interleaving enhances inductive learning remains an active issue, but 
Vlach et al. (2008) proposed that spacing between successive exemplars of a given category 
induces forgetting and that forgetting promotes abstraction.  The basic idea is that massing can 
lead to the encoding of details shared by successive exemplars of a given category that then turn 
out not to be diagnostic of that category, versus other categories, whereas when events intervene 
between successive exemplars of a given category what will tend to again be activated are the 
central features or gist of the category.  Such more abstract encodings are then also more likely 
to be durable and support performance when new exemplars need to be categorized on the final 
test.  
  
[p.14]
FORGETTING	
  AS	
  A	
  FRIEND	
  OF	
  LEARNING	
   14	
  
Forgetting, Desirable Difficulties, and the Potential for Learners to Be Fooled 
As I mentioned at the outset, the very notion that forgetting might help learning is 
unintuitive, which can lead us to assume that conditions of learning that prevent forgetting are to 
be preferred.  Our judgments as to how we should optimize our own or others’ learning can also 
be misled, however, by our subjective experiences and objective performance during the learning 
process. Conditions of instruction that appear to create difficulties for the learner, causing 
forgetting during the acquisition process and slowing the rate of apparent learning (as measured 
by current performance), can optimize long-term retention and transfer, whereas conditions of 
instruction that make performance improve rapidly can fail to support long-term retention and 
transfer.  To the extent, therefore, that we consider current performance (retrieval strength) to be 
a reliable index of learning (storage strength) we become prone to choosing poorer conditions of 
instruction or practice over better conditions. Also, as Larry Jacoby was among the first to 
emphasize (see, e.g., Jacoby, Kelley, & Bjork, 1994), conditions that make performance improve 
rapidly are often conditions that also create a subjective sense of ease or fluency, which can 
contribute to our preference for such conditions.  
That we are indeed prone to interpreting our current performance and/or subjective sense 
of fluency as evidence of learning and comprehension has been documented in multiple studies 
involving what I have termed “desirable difficulties” (Bjork, 1994a, 1994b), but which learners 
tend not to desire (see, e.g., Baddeley & Longman, 1978; Benjamin, Bjork, & Schwartz, 1998; 
Cohen, Yan, Halamish, & Bjork, in press; Heulser & Metcalfe, 2012; Koriat & Bjork, 2005; 
Kornell & Bjork, 2008; Reder, 1987; Roediger & Karpicke, 2006a; Simon & Bjork, 2001; and 
Tauber, Dunlosky, Wahlheim, & Jacoby, 2013).  Examples of manipulations that induce 
“desirable difficulties” include varying the conditions of instruction or practice versus keeping 
[p.15]
FORGETTING	
  AS	
  A	
  FRIEND	
  OF	
  LEARNING	
   15	
  
them constant and predictable; distributing, rather than massing, repeated study opportunities; 
providing intermittent, rather than continuous, feedback to learners; using tests, rather than 
presentations, as learning events; and interleaving, rather than blocking, separate to-be-learned 
tasks.  
It needs to be stressed that the word “desirable” is important.  As Elizabeth Bjork and I 
have emphasized elsewhere (E. L. Bjork & R. A. Bjork, 2011; Bjork, 2011), such difficulties are 
desirable not because they create difficulties per se, but because responding to such 
manipulations—successfully—engages the very encoding and retrieval processes that support 
long-term recall and transfer.  If a given learner is not equipped—by virtue of his or her prior 
learning, for example—to overcome a given difficulty, that difficulty becomes an undesirable 
difficulty.  If a level of variation and/or spacing between successive learning trials is introduced 
that makes reminding fail, for example, such variation and/or spacing creates an undesirable 
difficulty (see, e.g., Appleton-Knapp et al., 2005). Jacoby’s (1978) experiment discussed earlier 
(see Figure 3) provides another possible example.  The need to generate “shoe” when presented 
FOOT: S**E created a desirable difficulty for Jacoby’s participants, but that finding was 
contingent on the generation succeeding; had the participants not know the English language, 
such “construct” trials would have created an undesirable difficulty.  
With respect to when difficulties are and are not desirable, it is important to emphasize 
that my definition of forgetting in the present chapter differs from the all-or-none way forgetting 
is often characterized—namely, that if some information or procedure can still be recalled, it has 
not been forgotten, whereas if that information or procedure cannot be recalled, it has been 
forgotten.  Instead, I am defining forgetting as a decrease in accessibility (retrieval strength)—
that is, a decrease in how readily accessible some information or procedure is at a given point in 
[p.16]
FORGETTING	
  AS	
  A	
  FRIEND	
  OF	
  LEARNING	
   16	
  
time and in the presence of current cues.  Thus, for example, some information or procedure may 
remain recallable, if with greater difficulty, at a delay, even though its retrieval strength has 
decreased.  Similarly, in the retrieval-strength sense, forgetting can continue past the point that 
some information or procedure becomes non-recallable.  That is, some information or procedure 
that does not have a current level of retrieval strength sufficient to support its being successfully 
retrieved can still be forgotten further, so to speak, across an additional delay and intervening 
events as its retrieval strength continues to decrease.   
Concluding Comments on the Importance of Forgetting 
In a recent chapter (Bjork, 2011), I argued that the human memory system is 
characterized by a unique symbiosis of learning, remembering, and forgetting.  Forgetting, rather 
than undoing learning, enables learning and focuses remembering; Remembering creates learning 
and produces forgetting; and Learning begets remembering, contributes to forgetting, and 
enables new learning. Among the definitions of symbiosis is “a relationship of mutual benefit or 
dependence” (American Heritage Dictionary, 2006).  The relationships among remembering, 
forgetting, and learning are indeed symbiotic, but also complex and unintuitive.  It is a system 
that is remarkably interesting and effective, if fallible, and is no less remarkable by virtue of 
being so frequently underappreciated and misunderstood by the user.  
In this chapter I have focused on forgetting as an enabler of learning, but forgetting plays 
other crucial roles as well.  Forgetting of out-of-date information and procedures is essential with 
respect to keeping our memories current, for example, and forgetting “focuses remembering” in 
the sense that accessing current information or procedures can produce retrieval-induced 
forgetting (Anderson, Bjork, & Bjork, 1994) of competing information or procedures.  Storm 
(2011) has emphasized, too, that such retrieval-induced forgetting also plays a role in any act of 
[p.17]
FORGETTING	
  AS	
  A	
  FRIEND	
  OF	
  LEARNING	
   17	
  
thinking and problem solving where it is necessary to “overcome the fixating consequences of 
interfering information” (p. 295).  
Forgetting, its adaptive roles notwithstanding, is not, of course always desirable or 
adaptive, and one goal of this Festschrift is to induce remembering, not forgetting.  As this 
volume documents, we are indebted to the unforgettable Larry L. Jacoby for his multifaceted and 
enduring contributions not only to our understanding of how and why we, as humans, remember 
or fail to remember, but also when and why we are subject to illusions of comprehension, 
competence, and remembering.   
  
[p.18]
FORGETTING	
  AS	
  A	
  FRIEND	
  OF	
  LEARNING	
   18	
  
 
References 
American Heritage Dictionary of the English Language (4th ed.). (2006). Boston, MA: 
Houghton-Mifflin. 
Anderson, M.C., Bjork, R.A., & Bjork, E.L. (1994). Remembering can cause forgetting: 
Retrieval dynamics in long-term memory. Journal of Experimental Psychology: Learning, 
Memory, and Cognition, 20, 1063–1087. 
Appleton-Knapp, S., Bjork, R. A., & Wickens, T. D. (2005). Examining the spacing effect in 
advertising: Encoding variability, retrieval processes and their interaction. Journal of 
Consumer Research, 32, 266-276. 
Baddeley, A.D., & Longman, D.J.A. (1978). The influence of length and frequency of training 
session on the rate of learning to type.  Ergonomics, 21, 627-635.  
Benjamin, A. S., Bjork, R. A., & Schwartz, B. L.  (1998).  The mismeasure of memory: When 
retrieval fluency is misleading as a metamnemonic index.  Journal of Experimental 
Psychology: General, 127, 55-68.  
Benjamin, A. S. & Ross, B. H. (2011). The causes and consequences of reminding. In A. S. 
Benjamin (Ed.), Successful remembering and successful forgetting: A Festschrift in 
honor of Robert A. Bjork (pp. 71-88). New York, NY: Psychology Press. 
Benjamin, A. S. & Tullis, J. G. (2010).  What makes distributed practice effective?  Cognitive 
Psychology, 61(3), 228-247. 
Birnbaum, M. S., Kornell, N., Bjork, E. L., & Bjork, R. A. (2013). Why interleaving enhances 
inductive learning: The roles of discrimination and retrieval. Memory & Cognition, 41, 
392-402. 
[p.19]
FORGETTING	
  AS	
  A	
  FRIEND	
  OF	
  LEARNING	
   19	
  
Bjork, E. L., & Bjork, R. A.  (2011).  Making things hard on yourself, but in a good way: 
Creating desirable difficulties to enhance learning.  In M. A. Gernsbacher, R. W. Pew, L. 
M. Hough, & J. R. Pomerantz (Eds.), Psychology and the real world: Essays illustrating 
fundamental contributions to society (pp. 56-64).  New York: Worth Publishers. 
Bjork, R. A.  (1966).  Learning and short-term retention of paired associates in relation to 
specific sequences of inter-presentation intervals. Technical Report No. 106, Institute for 
Mathematical Studies in the Social Sciences, Stanford University. 
Bjork, R. A.  (1975). Retrieval as a memory modifier.  In R. Solso (Ed.), Information processing 
and cognition:  The Loyola Symposium (pp. 123-144).  Hillsdale, NJ: Lawrence Erlbaum 
Associates.  
Bjork, R. A.  (1988).  Retrieval practice and the maintenance of knowledge. In M. M. Gruneberg, 
P. E. Morris, & R. N. Sykes  (Eds.), Practical aspects of memory II  (pp. 396-401).  
London: Wiley.   
Bjork, R.A.  (1994a).  Memory and metamemory considerations in the training of human beings.  
In J. Metcalfe and A. Shimamura (Eds.), Metacognition: Knowing about knowing 
(pp.185-205). Cambridge, MA: MIT Press.  
Bjork, R.A.  (1994b).  Institutional impediments to effective training.  In D. Druckman and 
R.A.Bjork (Eds.), Learning, remembering, believing: Enhancing human performance 
(pp.295-306). Washington, DC:  National Academy Press.  
Bjork, R. A. (2011). On the symbiosis of learning, remembering, and forgetting.  In A. S. 
Benjamin (Ed.), Successful remembering and successful forgetting: a Festschrift in honor 
of Robert A. Bjork (pp. 1-22). London, UK: Psychology Press. 
[p.20]
FORGETTING	
  AS	
  A	
  FRIEND	
  OF	
  LEARNING	
   20	
  
Bjork, R. A., & Allen, T. W.  (1970).  The spacing effect: Consolidation or differential 
encoding?  Journal of Verbal Learning and Verbal Behavior, 9, 567-572. 
Bjork, R. A., & Bjork, E. L.  (1992).  A new theory of disuse and an old theory of stimulus 
fluctuation.  In A. Healy, S. Kosslyn, & R. Shiffrin (Eds.),  From learning processes to 
cognitive processes:  Essays in honor of William K. Estes  (Vol. 2, pp. 35-67).  Hillsdale, 
NJ: Erlbaum.    
Bower, G. H. (1972).  Stimulus sampling theory of encoding variability.  In A. W. Mellon & E. 
Martin (Eds.), Coding processes in human memory.  Washington, DC: W. H. Winston 
and Sons.  
Cohen, M. S., Yan, V. X., Halamish, V., & Bjork, R. A. (2013).  Do students think that difficult 
or valuable material should be studied sooner, rather than later?  Journal of Experimental 
Psychology: Learning, Memory, & Cognition, 39, 1682-96. doi: 10.1037/a0032425.682-
96. 
Cuddy, L. J., & Jacoby, L. L. (1982). When forgetting helps memory: An analysis of repetition 
effects. Journal of Verbal Learning and Verbal Behavior, 21, 451-467. 
Estes, W. K. (1955).  Statistical theory of distributional phenomena in learning. Psychological 
Review, 62, 369-377. 
Glenberg, A. M. (1979).  Component-levels theory of the effects of spacing of repetitions on 
recall and recognition.  Memory & Cognition, 7, 95-112. 
Huelser, B. J. and Metcalfe, J. (2012). Making related errors facilitates learning, but learners do 
not know it. Memory and Cognition, 40, 514–27 
Hintzman, D.L. (2010). How does repetition affect memory? Evidence from judgments of 
recency. Memory & Cognition, 38, 102-115. 
[p.21]
FORGETTING	
  AS	
  A	
  FRIEND	
  OF	
  LEARNING	
   21	
  
Hintzman, D. L. (2011). Research strategy in the study of memory: Fads, fallacies, and the 
search for the “coordinates of truth.” Perspectives on Psychological Science, 8, 253-271. 
Jacoby, L. L. (1978). On interpreting the effects of repetition: Solving a problem versus 
remembering a solution. Journal of Verbal Learning and Verbal Behavior, 17, 649-667. 
Jacoby, L. L., Bjork, R. A., & Kelley, C. M.  (1994). Illusions of comprehension, competence, 
and remembering.  In D. Druckman and R. A. Bjork (Eds.), Learning, remembering, 
believing: Enhancing human performance (pp.57-80). Washington, DC: National 
Academy Press. 
Kang, S. H. K. & Pashler, H. (2012). Learning painting styles: Spacing is advantageous when it 
promotes discriminative contrast. Applied Cognitive Psychology, 26, 97-103. 
Koriat, A., & Bjork, R. A. (2005). Illusions of competence in monitoring one’s knowledge 
during study. Journal of Experimental Psychology: Learning, Memory, Cognition, 31, 
187-194.   
Kornell, N., & Bjork, R. A. (2008). Learning concepts and categories: Is spacing the 
"enemy of induction"? Psychological Science, 19, 585-592.  
Kornell, N., Castel, A. D., Eich, T. S., & Bjork, R. A. (2010). Spacing as the friend of both 
memory and induction in younger and older adults. Psychology and Aging, 25, 498-503. 
McGeoch, J. A. (1932).  Forgetting and the law of disuse.  Psychological Review, 39, 352-370. 
Melton, A. W. (1963). Implications of short-term memory for a general theory of memory. 
Journal of Verbal Learning and Verbal Behavior, 2, 1-21.  
Melton, A. W. (1967). Repetition and retrieval from memory. Science, 158, 532. 
 
[p.22]
FORGETTING	
  AS	
  A	
  FRIEND	
  OF	
  LEARNING	
   22	
  
Mensink, G-J., & Raaijimakers, J. G. (1988).  A model for interference and forgetting.  
Psychological Review, 95, 434-455.   
Reder, L. M.  (1987). Selection strategies in question answering.  Cognitive Psychology, 19, 90-
138. 
Roediger, H.L. & Karpicke, J.D. (2006a). Test-enhanced learning: Taking memory tests 
improves long-term retention. Psychological Science, 17, 249-255. 
Roediger, H. L., III, & Karpicke, J. D. (2006b). The power of testing memory: Basic research 
and implications for educational practice. Perspectives on Psychological Science, 1: 181-
210.  [doi: 10.1111/j.1745-6916.2006.00012.x] 
Rumelhart, D. E. (1967).  The effects of interpresentation interval on performance in a 
continuous paired-associate task. Technical Report No. 116, Institute for Mathematical 
Studies in the Social Sciences, Stanford University. 
Simon, D. A., & Bjork, R. A. (2001). Metacognition in motor learning. Journal of Experimental 
Psychology: Learning, Memory, and Cognition, 27, 907-912. 
Soderstrom, N. C., & Bjork, R. A. (2013).  Learning versus performance.  In D. S. Dunn 
(Ed.), Oxford bibliographies online: Psychology.  New York: Oxford University 
Press.  doi 10.1093/obo/9780199828340-0081 
Storm, B. C. (2011). The benefit of forgetting in thinking and remembering.  Current Directions 
in Psychological Science, 20, 291-295.  
Tauber, S. K., Dunlosky, J., Rawson, K. A., Wahlheim, C. N., & Jacoby, L. L. (2013). Self-
regulated learning of a natural category: Do people interleave or block exemplars during 
study? Psychonomic Bulletin & Review, 20, 356-363. 
Thios, S. J., & D’Agostino, P. R. (1976). Effects of repetition as a function of study-phase 
[p.23]
FORGETTING	
  AS	
  A	
  FRIEND	
  OF	
  LEARNING	
   23	
  
retrieval. Journal of Verbal Learning and Verbal Behavior, 15, 529–536. 
Tulving, E., & Pearlstone, Z. (1966). Availability versus accessibility in memory for words.  
Journal of Verbal Learning and Verbal Behavior, 5, 381-391.    
Vlach, H. A., Sandhofer, C. M., & Kornell, N. (2008). The spacing effect in children’s memory 
and category induction. Cognition, 109, 163-167. doi: 10.1016/j.cognition.2008.0  
Wahlheim, C. N., Dunlosky, J., & Jacoby, L. L. (2011). Spacing enhances the learning of natural 
concepts: An investigation of mechanisms, metacognition, and aging. Memory & Cognition, 
39, 750-763. 
Whitten, W. B., & Bjork, R. A.  (1977).  Learning from tests: The effects of spacing.  Journal of 
Verbal Learning and Verbal Behavior, 16, 465-478.   
 
 
