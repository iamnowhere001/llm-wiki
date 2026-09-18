---
title: "Rethinking Rumination（重新思考反刍）"
author: Susan Nolen-Hoeksema, Blair E. Wisco, Sonja Lyubomirsky（三人署名完整；Yale University / University of California, Riverside）
url: https://doi.org/10.1111/j.1745-6924.2008.00088.x
kind: paper
published: 2008-09（Perspectives on Psychological Science, 3(5), 400–424；SAGE / Association for Psychological Science）
clipped: 2026-09-18
capture_quality: high
capture_method: >
  curl -sL 直连下载作者自存版 PDF —— 源
  https://drsonja.net/wp-content/themes/drsonja/papers/NWL2008.pdf
  （第二作者 Sonja Lyubomirsky 本人的官方站点；正式出处 DOI 10.1111/j.1745-6924.2008.00088.x）。

  转文本用 pypdf 6.16.2 逐页提取（PDF 自带文本层，未做 OCR）—— **25 页 / 156,776 字符**，
  每页以 `[p.N]` 分隔，N 与 PDF 页码一致（PDF 第 1 页 = 印刷第 400 页，PDF 第 25 页 = 印刷第 424 页，
  页码与卷期连续，已核对末页刊眉「424 Volume 3—Number 5」）。
  PDF 原件（application/pdf, 269,833 字节）→ raw/assets/2026-09-18-nolen-hoeksema-rethinking-rumination.pdf

  已知缺失（两条）——
  1. **PDF 文本层有字距伪影**：大写字母后偶发多余空格（`W ood` / `V olume` / `T .B.`），
     并有少量标点前空格（`behavior , and`）。提取时**未做清洗**，以免改动正文行序 ——
     引用具体措辞前须回 PDF 核对。
  2. **图与表的本体未进入文本层**：图注文字在，图内数据点与表格线框不在。
     （本文图表数量少，影响有限，但若引用 Table 1 的分级需回 PDF。）
capture_note: >
  **本字段只记「抓取事实」，不记「阅读结论」。**（`AGENTS.md` 1.1）
  本素材的分段、行区间、核查表一律维护在
  wiki/sources/2026-09-18-nolen-hoeksema-rethinking-rumination.md —— 它们随阅读深入而变，
  而本文件不可变，写在这里必然产生死结。**本文件不维护任何行区间。**

  行区间坐标系为**文件绝对行号**（`wc -l` 的坐标系）。引用前回文件核对。

  **素材性质 —— 本库第二份一手学术文献。** 同行评议综述刊（Perspectives on Psychological Science
  为 APS 旗舰综述刊）的综述性专论，三作者署名完整，**第一作者为反应风格理论的提出者本人** ——
  本文是她对该理论近二十年证据的**自我复核**，含对原始预测的明确修正
  （例如：反刍更稳定地预测抑郁的**发作**而非**持续时间**；正性分心在相关研究中
  并**未**如原始预测那样稳定地与更低抑郁症状相关）。无 AI 生成痕迹，无转述层。

  **这一点使它在库内的证据地位特殊**：不是转述、不是外围研究，而是**该理论的一手权威来源**，
  且自带对自身早期主张的修正 —— 引用时不应把它当成「又一份支持性材料」。

  **收录理由 ——** 服务于 [[emotion-awareness]] 缺口表那条「补录反刍 / 反思文献素材」：
  [[rumination-vs-reflection]] 的全部依据此前均为未收录的外部文献，本份是该缺口最经济的补法
  （一份覆盖定义、反刍-担忧关系、与反思的区分、干预四个面向）。

  **版权性质 ——** SAGE / Association for Psychological Science 出版；下载源为作者自存版本。
  本文件与 PDF 原件均以个人研究用途存档于本地 `raw/`，不对外发布。
---

[p.1]

Rethinking Rumination
Susan Nolen-Hoeksema,1 Blair E. Wisco, 1 and Sonja Lyubomirsky2
1Yale University and 2University of California, Riverside
ABSTRACT— The response styles theory (Nolen-Hoeksema,
1991) was proposed to explain the insidious relationship
between rumination and depression. We review the aspects
of the response styles theory that have been well-sup-
ported, including evidence that rumination exacerbates
depression, enhances negative thinking, impairs problem
solving, interferes with instrumental behavior , and erodes
social support. Next, we address contradictory and new
ﬁndings. Speciﬁcally , rumination appears to more consis-
tently predict the onset of depression rather than the du-
ration, but rumination interacts with negative cognitive
styles to predict the duration of depressive symptoms.
Contrary to original predictions, the use of positive dis-
tractions has not consistently been correlated with lower
levels of depressive symptoms in correlational studies, al-
though dozens of experimental studies show positive dis-
tractions relieve depressed mood. Further , evidence now
suggests that rumination is associated with psychopa-
thologies in addition to depression, including anxiety ,
binge eating, binge drinking, and self-harm. We discuss the
relationships between rumination and worry and between
rumination and other coping or emotion-regulation
strategies. Finally , we highlight recent research on the
distinction between rumination and more adaptive forms
of self-reﬂection, on basic cognitive deﬁcits or biases in
rumination, on its neural and genetic correlates, and on
possible interventions to combat rumination.
It is said that human beings are the only species who can reﬂect
upon themselves. Self-reﬂection, the process of focusing on
one’s experiences, thoughts, and feelings, has been the topic of a
great deal of research in recent years (see reviews by Ingram,
1990; Mor & Winquist, 2002; Papageorgiou & W ells, 2004).
Much of this research has been concerned with maladaptive
forms of self-reﬂection in people prone to depression, anxiety, or
other forms of psychopathology. In their meta-analysis of the
literature on self-focused attention, Mor and Winquist (2002)
concluded that rumination was the form most strongly and
consistently related to depressive symptoms.
The conceptualization and operationalizations of rumination in
the response styles theory (Nolen-Hoeksema, 1991) have been
used in much of the research on depressive rumination. According
to the response styles theory, rumination is a mode of responding to
distress that involves repetitively and passively focusing on
symptoms of distress and on the possible causes and consequences
of these symptoms. Rumination does not lead to active problem
solving to change circumstances surrounding these symptoms.
Instead, people who are ruminating remain ﬁxated on the problems
and on their feelings about them without taking action.
The content of ruminative thought in depressed people is
typically negative in valence, similar to the automatic thoughts,
schema, and negative cognitive styles that have been studied
extensively by cognitive theorists (e.g., Beck, 1967). W e deﬁne
rumination, however, as the process of thinking perseveratively
about one’s feelings and problems rather than in terms of the
speciﬁc content of thoughts. Still, rumination is correlated with a
variety of maladaptive cognitive styles, including negative in-
ferential or attributional styles, dysfunctional attitudes, hope-
lessness, pessimism, self-criticism, low mastery, dependency,
sociotropy, neediness, and neuroticism (Ciesla & Roberts, 2002;
Flett, Madorsky, Hewitt, & Heisel, 2002; Lam, Smith, Checkley,
Rijsdijk, & Sham, 2003; Lyubomirsky & Nolen-Hoeksema,
1995; Lyubomirsky, Tucker, Caldwell, & Berg, 1999; Nolen-
Hoeksema & Davis, 1999; Nolen-Hoeksema & Jackson, 2001;
Nolen-Hoeksema, Larson, & Grayson, 1999; Robinson & Alloy,
2003; Spasojevic & Alloy, 2001), even after controlling for
levels of depression (Lam et al., 2003; Nolen-Hoeksema et al.,
1994; Nolen-Hoeksema, Parker, & Larson, 1999; Roberts,
Gilboa, & Gotlib, 1998). Rumination appears to have a unique
relationship to depression over and above its relationship to
negative cognitive styles and continues to be related to de-
pression after statistically controlling for neuroticism, pessi-
mism, perfectionism, and several other negative cognitive styles
(Flett et al., 2002; Nolen-Hoeksema et al., 1994; Spasojevic &
Alloy, 2001). Indeed, rumination has been found to partially or
fully mediate the relationship between depression and neurot-
icism, negative inferential styles, dysfunctional attitudes, self-
criticism, dependency, and neediness (Ito & Agari, 2003; Nolan,
Roberts, & Gotlib, 1998; Nolen-Hoeksema et al., 1994; Spas-
ojevic & Alloy, 2001).
Address correspondence to Susan Nolen-Hoeksema, Department of
Psychology, Yale University, P .O. Box 208205, New Haven, CT
06520; e-mail: susan.nolen-hoeksema@yale.edu.
PERSPECTIVES ON PSYCHOLOGICAL SCIENCE
400 V olume 3—Number 5Copyright r 2008 Association for Psychological Science

[p.2]

According to the response styles theory (Nolen-Hoeksema,
1991), rumination exacerbates and prolongs distress, particu-
larly depression, through several mechanisms. First, rumination
enhances the effects of depressed mood on thinking, making it
more likely that people will use the negative thoughts and
memories activated by their depressed mood to understand their
current circumstances. Second, rumination interferes with
effective problem solving, in part by making thinking more
pessimistic and fatalistic. Third, rumination interferes with in-
strumental behavior, leading to increases in stressful circum-
stances. In addition, Nolen-Hoeksema and Davis (1999) argued
that people who chronically ruminate will lose social support,
which in turn will fuel their depression. These consequences of
rumination then make it more likely that the initial symptoms
of depression will become more severe and evolve into episodes
of major depression. In addition, they could prolong current
depressive episodes.
An adaptive and instrumental alternative is to use pleasant or
neutral distractions to lift one’s mood and relieve one’s depres-
sive symptoms. Then, if necessary, one can commence problem
solving (Nolen-Hoeksema, 1991). Distracting responses are
thoughts and behaviors that help divert one’s attention away
from one’s depressed mood and its consequences and turn it to
pleasant or benign thoughts and activities that are absorbing,
engaging, and capable of providing positive reinforcement
(Csikszentmihalyi, 1990; Nolen-Hoeksema, 1991): for example,
going for a run or a bike ride, seeing a movie with friends, or
concentrating on a project at work. Effective distractions do not
include inherently dangerous or self-destructive activities, such
as reckless driving, heavy drinking, drug abuse, or aggressive
behavior, that may take attention away from current problems in
the short-term but are harmful in the long run.
In this article, we concisely review the evidence for this
conceptualization of rumination and its effects. W e conclude
that many of the arguments of the original response styles theory
have been well-supported. Still, ﬁndings contradicting the
original theory require the rethinking of rumination and its
consequences and functions. W e also address a number of
questions that have arisen in the last 15 years about rumina-
tion—the range of psychopathologies it might affect, its rela-
tionship to worry and other coping or emotion-regulation
strategies, possible subtypes of self-reﬂection, the basic cogni-
tive deﬁcits or biases that may underlie rumination, its neural
and genetic correlates, and how it can be overcome.
THE EFFECTS OF RUMINATION
According to the original response styles theory, rumination
maintains and exacerbates depression by enhancing negative
thinking, impairing problem solving, interfering with instru-
mental behavior, and eroding social support. W e will brieﬂy
review the large body of evidence supporting these claims (for
more extensive reviews, see Lyubomirsky & Tkach, 2004; Mor &
Winquist, 2002; Nolen-Hoeksema, 2004b).
Rumination and Depression
To assess individual differences in the tendency to ruminate,
Nolen-Hoeksema and Morrow (1991) developed the Ruminative
Responses Scale of the Response Styles Questionnaire. Re-
spondents are asked to indicate how often they engage in each of
22 ruminative thoughts or behaviors when they feel sad, blue, or
depressed.1 These 22 items describe responses to depressed
mood that are self-focused (e.g., ‘‘I think ‘Why do I react this
way?’’’), symptom-focused (e.g., ‘‘I think about how hard it is to
concentrate’’), and focused on the possible consequences and
causes of one’s mood (e.g., ‘‘I think ‘I won’t be able to do my job if
I don’t snap out of this’’’). This scale has high internal consis-
tency and acceptable convergent validity (Butler & Nolen-
Hoeksema, 1994; Nolen-Hoeksema & Morrow, 1991).
The tendency to ruminate is relatively stable even in indi-
viduals who experience signiﬁcant change in their levels of
depression (Bagby, Rector, Bacchiochi, & McBride, 2004; Just
& Alloy, 1997; Kuehner & W eber, 1999; Nolen-Hoeksema,
Morrow, & Fredrickson, 1993; Nolen-Hoeksema et al., 1994).
For example, in a longitudinal study of recently bereaved people
spanning 18 months (Nolen-Hoeksema & Davis, 1999), the in-
traclass correlation for the Ruminative Responses Scale across 5
interviews was .75 ( p < .0001), despite the fact that levels of
depression dropped precipitously in the 18 months following the
bereavement.2
Prospective longitudinal studies using this scale have shown
that people who engage in rumination when distressed have
more prolonged periods of depression and are more likely to
develop depressive disorders (Just & Alloy, 1997; Kuehner &
W eber, 1999; Nolan et al., 1998; Nolen-Hoeksema, 2000; No-
len-Hoeksema et al., 1999; Nolen-Hoeksema et al., 1993, 1994;
Roberts et al., 1998; Sarin, Abela, & Auerbach, 2005;
Segerstrom, Tsao, Alden, & Craske, 2000; Spasojevic & Alloy,
2001; W ood, Saltzberg, Neale, Stone, & Rachmiel, 1990); sim-
ilar results were found in samples of adolescents or children
(Abela, Brozina, & Haigh, 2002; Nolen-Hoeksema, Stice, W ade,
1Slightly different versions of the rumination scale have been used in various
studies over the years. Because our unpublished data suggest that these other
versions correlate very highly with the 22-item version currently recommended
for use (Treynor, Gonzalez, & Nolen-Hoeksema, 2002), we will not separately
review studies that have used different versions of the scale.
2Bagby et al. (2004) distinguished between absolute stability (i.e., when the
participants’ scores did not change signiﬁcantly over time) and relative stability
(i.e., when the participants’ rank ordering of scores remained stable but their
actual scores varied over time). Rumination scores tend to decline as levels of
depression decline, suggesting that they do not show absolute stability (Bagby
et al., 2004; Kasch, Klein, & Lara, 2001). Bagby et al. (2004), however, found
evidence for relative stability of rumination scores even among patients being
treated with antidepressants for a major depressive episode. In addition, they
found that pretreatment rumination scores predicted posttreatment rumination
scores even after accounting for changes in depression levels over the course of
treatment, suggesting that changes in rumination scores were not simply a
function of changes in levels of depression due to treatment.
V olume 3—Number 5 401
Susan Nolen-Hoeksema, Blair E. Wisco, and Sonja Lyubomirsky

[p.3]

& Bohon, 2007; J.A.J. Schwartz & Koenig, 1996) and in samples
outside the United States (Ito & Agari, 2002; Kuehner & W eber,
1999; Raes, Hermans, & Eelen, 2003; Sakamoto, Kambara, &
Tanno, 2001). 3 Other measures of rumination—in particular,
those assessing a perseverative focus on the self and one’s
problems—have demonstrated similar links to depression
(Luminet, 2004; Mor & Winquist, 2002; Siegle, Moore, & Thase,
2004). In addition, scores on the Ruminative Responses Scale
correlated signiﬁcantly with scores on alternative measures of
negative rumination (Siegle et al., 2004). Thus, although much
of the work on rumination has relied on the Ruminative Re-
sponses Scale, the relationship between rumination and de-
pression has been found with different measures of rumination.4
Experimental studies testing the effects of rumination have
generally used the rumination induction developed by Nolen-
Hoeksema and Morrow (1993). Participants are asked to focus
on the meanings, causes, and consequences of their current
feelings for 8 min (e.g., ‘‘Think about the level of motivation you
feel right now,’’ ‘‘Think about the long-term goals you have set’’).
Because these are emotionally neutral prompts, they are ex-
pected to have no effect on the moods of nondysphoric people.
But because dysphoric or depressed people have more negative
feelings and cognitions, this ruminative self-focus is expected to
lead them to become signiﬁcantly more dysphoric. The con-
trasting distraction induction is meant to take participants’
minds off themselves and their problems temporarily. In this
condition, participants’ attention is focused on non-self-relevant
images (e.g., ‘‘Think about a fan slowly rotating back and forth,’’
‘‘Think about the layout of your local shopping center’’). These
distracting prompts are expected to have no effect on the moods
of nondysphoric people but are expected to lead dysphoric
people to become signiﬁcantly less depressed for a short time.
W e have conducted dozens of studies using these rumination
and distraction manipulations and have found that the rumi-
nation induction signiﬁcantly increases dysphoric mood in
dysphoric participants but not in nondysphoric participants.
The distraction induction decreases dysphoric mood in dys-
phoric participants but has no effect on mood in nondysphoric
participants (Lyubomirsky, Caldwell, & Nolen-Hoeksema,
1998; Lyubomirsky & Nolen-Hoeksema, 1993, 1995;
Lyubomirsky et al., 1999; Morrow & Nolen-Hoeksema, 1990;
Nolen-Hoeksema & Morrow, 1993). Other investigators using
our rumination and distraction inductions have found similar
effects in clinically depressed participants (Donaldson & Lam,
2004; Lavender & W atkins, 2004; W atkins & Baracaia, 2002;
W atkins & Moulds, 2005; W atkins & Teasdale, 2001).
Negative Thinking
Rumination appears to lead dysphoric or clinically depressed
people to think more negatively about the past, the present, and
the future. Dysphoric participants induced to ruminate sponta-
neously retrieve more negative memories from their recent past
and recall negative events as having occurred more frequently in
their lives than do dysphoric participants induced to distract
from negative thoughts (Lyubomirsky et al., 1998; McFarland &
Buehler, 1998; Pyszczynski, Hamilton, Herring, & Greenberg,
1989).
With regard to current events in their lives, dysphoric par-
ticipants induced to ruminate spontaneously talk about trou-
bling problems, such as conﬂict with families or ﬁnancial woes,
whereas dysphoric participants induced to distract from nega-
tive thoughts and the nondysphoric participants tend to talk
about more cheerful situations they are facing (Lyubomirsky
et al., 1999). Dysphoric ruminators are also more negative, more
self-critical, and more likely to blame themselves for their
current problems, and they express reduced self-conﬁdence and
optimism in overcoming those problems. When presented with
hypothetical negative life events, dysphoric ruminators choose
more negatively biased and distorted interpretations of those
events (e.g., minimizing their successes and overgeneralizing
from their failures; Lyubomirsky & Nolen-Hoeksema, 1995;
Lyubomirsky et al., 1999; see also Greenberg, Pyszczynski,
Burling, & Tibbs, 1992).
Finally, in their predictions about the future, dysphoric rumi-
nators are more gloomy, with low expectations for positive events
(Lyubomirsky & Nolen-Hoeksema, 1995; see also Pyszczynski,
Holt, & Greenberg, 1987), solutions to their problems (Lyubomir-
sky et al., 1999), or for fun activities (L yubomirsky & Nolen-
Hoeksema, 1993). In all of these studies, dysphoric participants
instructed to distract for 8 min were no more pessimistic or
negative in their thinking than were nondysphorics (see also
Pyszczynski et al., 1987, 1989). Similarly, studies using people
meeting criteria for major depressive disorder have found that
those induced to ruminate subsequently show more negative
thinking about themselves and the future than do those in other
induction conditions (Lavender & W atkins, 2004; Rimes &
W atkins, 2005).
Poor Problem Solving
People prone to rumination often say they are trying to under-
stand and solve their problems (Papageorgiou & W ells, 2001,
2003). Unfortunately, however, rumination in the context of
dysphoria seems to interfere with good problem solving. Ex-
perimental studies show that inducing dysphoric participants to
ruminate prompts them to appraise their problems as over-
whelming and unsolvable (Lyubomirsky et al., 1999) and to fail
3The Ruminative Responses Scale has been translated into German (Ku-
ehner & W eber, 1999), Japanese (Ito & Agari, 2002; Sakamoto et al., 2001), and
Dutch (Raes et al., 2003) for studies in those languages, and it has also been
adapted for investigations with children by simplifying the language (Abela
et al., 2002).
4The Adaptive Forms of Self-Reﬂection section of this article offers further
discussion of alternative conceptualizations and operationalizations of rumi-
nation. Readers interested in the assessment of rumination are referred to
Luminet (2004), which details the psychometric properties of some of the most
commonly used measures.
402 V olume 3—Number 5
Rethinking Rumination

[p.4]

to come up with effective problem solutions (Lyubomirsky &
Nolen-Hoeksema, 1995; Lyubomirsky et al., 1999). Similar re-
sults have been found in samples of clinically depressed pa-
tients. (e.g., Donaldson & Lam, 2004; W atkins & Baracaia,
2002; W atkins & Moulds, 2005).
Even when a depressed ruminator generates a worthwhile
solution to a problem, rumination may impede him or her from
implementing it. In one laboratory study, dysphoric students
who ruminated came up with perfectly good solutions to pressing
problems (e.g., ‘‘study harder’’ or ‘‘spend less money’’) but
showed a reduced likelihood of actually implementing those
plans (Lyubomirsky et al., 1999). In a quasi-experimental study,
participants prone to rumination expressed less conﬁdence in a
solution they had generated to a complex problem (e.g., how to
improve their school’s curriculum), asked for more time to work
on the solution before they committed to it, and were less con-
ﬁdent in their oral presentation of their solutions (W ard,
Lyubomirsky, Sousa, & Nolen-Hoeksema, 2003).
Inhibition of Instrumental Behavior
One of the ways that ruminative responses to depressed mood
can interfere with successful problem solving is by sapping
people’s motivation and initiative. Rumination maintains one’s
focus on one’s depressive symptoms, which may convince dys-
phoric people that they lack the efﬁcacy and wherewithal to
engage in constructive behavior, such as participation in mood-
alleviating activities. Indeed, the results of several studies
suggest that people who focus on themselves and their feelings
in the context of a negative mood show reduced motivation to
initiate instrumental behavior. For example, one study revealed
that although dysphoric ruminators recognized that pleasant,
distracting activities would lift their mood, they were unwilling
to try them (Lyubomirsky & Nolen-Hoeksema, 1993; see also
W enzlaff, W egner, & Roper, 1988).
The consequences of ruminative thinking for the inhibition of
instrumental action can be troublesome or inconvenient at best
and serious or dangerous at worst. In the domain of health,
laboratory and ﬁeld studies show that women with chronic ru-
minative styles suffer heightened distress upon discovering
potential health symptoms (e.g., a breast lump) and, conse-
quently, delay seeking a diagnosis (Lyubomirsky, Kasri, Chang,
& Chung, 2006). For example, women ruminators with breast
cancer reported having delayed the presentation of their initial
cancer symptoms to a physician more than 2 months longer than
did nonruminators (Lyubomirsky, Kasri, et al., 2006). Further-
more, the effect of ruminative style on delay was moderated in
part by the experience of positive mood at the time of
symptom discovery—women ruminators who were relatively
upbeat when they detected their symptom were less
likely to delay. Similarly, in correlational studies, a tendency
towards rumination was related to low compliance with a med-
ical regimen among a diverse set of cancer patients in Germany
(Aymanns, Filipp, & Klauer, 1995), and emotion-focused ru-
mination among ﬁrst-time patients predicted rehospitalization 4
months after a coronary event such as a heart attack (Fritz,
1999).
Reduction of Social Support
Chronic ruminators appear to behave in ways that are counter-
productive to their relationships with family, friends, and even
strangers. In a study of bereaved adults, ruminators were more
likely to reach out for social support after their loss, but they
reported more social friction and less emotional support from
others (Nolen-Hoeksema & Davis, 1999). Anecdotal reports
from ruminative participants suggest that friends and family
members become frustrated with their continued need to talk
about their loss and its meanings for their lives many months
after the loss (Nolen-Hoeksema & Larson, 1999). Other studies
suggest that ruminators are perceived less favorably by others
(J.L. Schwartz & McCombs, 1995).
Rumination is associated with several undesirable personal-
ity characteristics, including both a dependent, clingy inter-
personal style and aggressive tendencies that may lead to this
loss of social support. Ruminators suffer from unmitigated
communion (i.e., the tendency to assume undue responsibility
for the well-being of others; Nolen-Hoeksema & Jackson, 2001),
dependency, neediness (Spasojevic & Alloy, 2001), and so-
ciotropy (Gorski & Y oung, 2002). Rumination is also associated
with the desire for revenge after an interpersonal transgression
or slight (e.g., ‘‘I want to see her hurt and miserable’’;
McCullough, Bellah, Kilpatrick, & Johnson, 2001; McCullough
et al., 1998) and with increased aggression following a provo-
cation (Collins & Bell, 1997).
Thus, a large number of studies from our laboratories and
those of other investigators have shown that rumination is as-
sociated with the experience of depressive symptoms and that
rumination in the context of depressed mood or major depression
is associated with more negative thinking, poorer problem
solving, diminished instrumental behavior, and reduced social
support. Many of these studies have used experimental designs,
and many of the effects have been found both with dysphoric and
with clinically depressed individuals.
CHALLENGES TO THE RESPONSE STYLES THEORY
Not all of the predictions of the original response styles theory
have been supported. In this section, we address two central
predictions that have frequently failed to gain support.
Duration Versus Onset of Depression
Nolen-Hoeksema (1991) originally suggested that rumination
should predict the duration of depressed mood or depressive
episodes more than it should predict their onset. This argument
V olume 3—Number 5 403
Susan Nolen-Hoeksema, Blair E. Wisco, and Sonja Lyubomirsky

[p.5]

has been directly tested in several studies. 5 In a sample of ap-
proximately 1,300 adults randomly drawn from the community,
Nolen-Hoeksema (2000) found that rumination scores at a ﬁrst
assessment predicted new onsets of major depressive episodes
(assessed with a structured clinical interview) over the next year
among people who were not initially in a major depressive ep-
isode. Among people who were already in a major depressive
episode at the ﬁrst assessment, however, rumination scores did
not predict whether they would still be in a depressive episode 1
year later. Just and Alloy (1997) found that college students’
rumination scores at the beginning of a study predicted which
students would show new onsets of signiﬁcant depressive
symptoms over 18 months, but the scores did not predict the
duration of depressive symptoms in already-depressed students.
Similarly, Lara, Klein, and Kasch (2000) assessed rumination
in 84 college students who met criteria for major depression at
the beginning of the study and found that it did not predict
duration of their depression or time to remission over a 6-month
follow-up.
Other studies have found that rumination does not predict
duration of episodes of major depression in patients being
treated for major depression (Arnow, Spangler, Klein, & Burns,
2004; Bagby & Parker, 2001; Park, Goodyer, & Teasdale, 2004;
Schmaling, Dimidjian, Katon, & Sullivan, 2002). W e do not
believe this is an appropriate test of the response styles theory,
however, as it does not make predictions about the effects of
rumination on change in depression in patients who are un-
dergoing pharmacotherapy or psychotherapy speciﬁcally de-
signed to relieve their depression. In addition, it seems
unreasonable to expect that pretreatment levels of rumination
should predict responses to treatments that may have direct
effects on patients’ levels of rumination.
Some studies have found that rumination predicts the duration
of depressive episodes. Kuehner and W eber (1999) assessed
rumination in patients at the end of their treatment for depres-
sion and found that it predicted which patients would be in an
episode of major depression 3 months later, as well as their
levels of depression at 3 months postdischarge. Two studies
found that the interaction of rumination and negative cognitive
styles predicted the duration of diagnosed depressive episodes:
one study used an untreated sample (Robinson & Alloy, 2003)
and one study used a sample that had been given psychoedu-
cational treatment (Ciesla & Roberts, 2002). These ﬁndings
suggest that the combination of negatively biased, irrational
thoughts with a passive and repetitive focus on such thoughts
can maintain depressive episodes.
There may be simple statistical reasons why rumination
scores do not consistently predict the duration of depression in
people already meeting criteria for major depression. People
susceptible to developing major depression appear to be highly
likely to ruminate (Just & Alloy, 1997; Nolen-Hoeksema, 2000),
so samples of already-depressed people may be relatively ho-
mogeneous for rumination, reducing variance in scores and thus
reducing the statistical power for rumination to predict duration
of depression. In addition, most studies have statistically con-
trolled for initial levels of depressive symptoms in already-
depressed participants in analyses to predict the duration of their
symptoms; because rumination is likely to be correlated with
initial levels of depression in already-depressed participants,
this statistical control procedure further reduces the power of
rumination to predict the duration of depressive symptoms.
A more interesting possibility is that rumination contributes
to an individual ‘‘crossing the line’’ from dysphoria into a major
depressive episode, but once an individual is in an episode,
other autonomous self-perpetuating processes emerge that de-
termine the duration of episodes. There are several neurobiol-
ogical processes that appear to be state-dependent in major
depression, including elevated peripheral levels of norepi-
nephrine metabolites, increased phasic REM sleep, poor sleep
maintenance, hypercortisolism, decreased cerebral blood ﬂow
and glucose metabolism within anterior cortical structures, and
increased blood ﬂow and glucose metabolism in paralimbic
regions (Thase, Jindal, & Howland, 2002). These processes may
help to maintain the symptoms of depression once they begin,
even if they did not trigger the symptoms initially. For example, a
person who ruminates over the loss of a close loved one may
develop a severe enough grief reaction to meet criteria for a
diagnosis of major depression, but the duration of the symptoms
may depend on the functioning of these neurobiological systems
in the individual.
The evidence that rumination predicts onsets of depression
but does not always predict its duration parallels ﬁndings
emerging from large nationally representative epidemiological
studies that women’s greater rates of depression are due to
gender differences in ﬁrst onsets, but not in duration of the
episodes (Eaton et al., 1997; Kessler, McGonagle, Swartz, Bla-
zer, & Nelson, 1993). This is particularly interesting because
the response styles theory was originally proposed, in part, to
explain women’s greater vulnerability to depression (Nolen-
Hoeksema, 1987). Several studies have found that women are
more likely to engage in rumination than men are (Butler &
Nolen-Hoeksema, 1994; Grant et al., 2004; Nolen-Hoeksema &
Larson, 1999; Nolen-Hoeksema et al., 1993, 1999; Roberts
et al., 1998; Ziegart & Kistner, 2002), and the gender difference
in rumination has been found to mediate the gender difference in
depression in some studies (Grant et al., 2004; Nolen-Hoeksema
et al., 1999; Roberts et al., 1998). Thus, since the original for-
mulation of the response styles theory, the pattern of ﬁndings
that has emerged is consistent with the argument that gender
5Most longitudinal studies have only tested whether rumination scores taken
at one point in time predict change in depression scores from that time to a
second assessment in the future. These analyses (which are usually regression
analyses) cannot distinguish whether rumination is predicting the onset of new
depressive symptoms, the maintenance of existing depressive symptoms, or the
degree of reduction of depressive symptoms.
404 V olume 3—Number 5
Rethinking Rumination

[p.6]

differences in rumination help to account for the gender
differences in depression.
Distraction as an Adaptive Alternative to Rumination
The original response styles theory argued that using positive
distractions was an adaptive alternative to rumination and
suggested that these two response styles were orthogonal, if not
in direct opposition (Nolen-Hoeksema, 1991). Studies using
the distraction subscale of the Response Styles Questionnaire,
however, have found inconsistent relationships to depressive
symptoms and rumination (e.g., Knowles, Tai, Christensen, &
Bentall, 2005). Sometimes distraction is negatively correlated
with depression and rumination (Bagby & Parker, 2001; Chang,
2004; Lam et al., 2003; Nolen-Hoeksema et al., 1994), some-
times it is positively correlated (Schmaling et al., 2002), and
sometimes it is uncorrelated (Abela et al., 2002; Arnow et al.,
2004; Just & Alloy, 1997; Kuehner & W eber, 1999; Nolen-
Hoeksema et al., 1993).
The inconsistent ﬁndings across studies may be due to
differences in populations (e.g., younger vs. older, clinical vs.
community). W e also suspect a problem with the way positive
distraction is operationalized on the distraction subscale of
the Response Styles Scale (and on related distraction scales).
The distraction subscale asks people how often they use each of
11 activities, such as ‘‘go to a favorite place to get your mind off
your feelings’’ and ‘‘do something you enjoy,’’ in response to a
sad or depressed mood. Respondents’ scores are then summed
across all 11 items, so high scores on this scale can indicate that
a respondent engages in several distracting activities fairly of-
ten. Although it makes intuitive sense, at least initially, that
engaging in more distracting activities is adaptive, this may not
be true. Some people who engage in lots of distracting activities
may be ﬂitting from one to another, desperately trying to get their
minds off their negative mood and ruminations. They may not,
however, pour their attention fully into any one of these activities
and thus ﬁnd that none of them provide relief. This could explain
why some studies have found distraction to be positively cor-
related cross-sectionally with both rumination and depression.
In contrast, people who use distraction effectively may have
one or two activities they engage in when they are feeling upset
or overwhelmed with concerns, and they may absorb themselves
fully in these activities. For example, when they are feeling sad
or blue, they may automatically pick up a hobby (knitting,
playing the piano) or engage in a physical activity (a vigorous
tennis game, playing basketball with friends) that is engrossing,
distracting, and uplifting.
Thus, laboratory studies have reliably shown that inducing
depressed people to focus on positive or benign distractions
reduces their negative affect. Self-report measures of distrac-
tion, however, have not produced clear or consistent correla-
tions. W e encourage development of better methods to assess the
everyday use of positive distractions as a mood-management
technique. These new methods should assess not only the
number of distractions and frequency of use, but also people’s
ability to maintain their attention on these distracters.
OTHER PSYCHOPATHOLOGIES PREDICTED BY
RUMINATION
The original response styles theory focused only on the rela-
tionship between rumination and depression. However, rumi-
nation might be expected to predict additional forms of
psychopathology. Heatherton, Baumeister, and colleagues
(Abramson, Bardone-Cone, V ohs, Joiner, & Heatherton, 2006;
Heatherton & Baumeister, 1991) argue that some people prone
to high levels of aversive self-awareness, as are people who
ruminate, turn to escapist behaviors such as binge eating or
binge drinking to temporarily quell their self-directed thoughts.
On the basis of this work, we hypothesized that individual
differences in rumination would predict binge drinking and
related symptoms of alcohol abuse, as well as binge eating and
related symptoms of bulimia nervosa. Two prospective studies of
adults have found that rumination predicts increases in binge
drinking and/or symptoms of alcohol abuse over time (Nolen-
Hoeksema & Harrell, 2002; Nolen-Hoeksema & Larson, 1999).
Similarly, Nolen-Hoeksema et al. (2007) found that adolescent
girls with high rumination scores were more likely to develop not
only depression, but also symptoms of alcohol abuse, and they
were also more likely to meet diagnostic criteria for alcohol
abuse over a 4-year period. Adolescent girls prone to rumination
were also more likely to develop symptoms of bulimia nervosa,
especially binge eating, over the 4 years of the study. It is im-
portant to note that rumination did not predict changes in ex-
ternalizing symptoms (e.g., aggression, delinquency) in these
girls, providing evidence for the speciﬁcity of rumination in
predicting internalizing symptoms and escapist behaviors.
Future investigations that test the self-reﬂective conse-
quences of bulimic behaviors and substance abuse should be
conducted to determine whether these behaviors actually do
provide an escape from ruminative self-awareness. In addition,
future research should also seek to determine what distinguishes
those ruminators who turn to escapist behaviors from those who
do not. Body dissatisfaction and acceptance of social norms for
thinness have been found to predict excessive dieting and other
behaviors designed to avoid gaining weight (e.g., self-induced
vomiting; see Stice, 2002). Perhaps rumination interacts with
these attitudinal variables to predict which individuals develop
bulimia nervosa. Similarly, positive expectancies for the effects
of alcohol (e.g., that alcohol will improve one’s mood) predict
drinking behavior (Cooper, Russell, & George, 1988; Cooper,
Russell, Skinner, Frone, & Mudar, 1992). Perhaps rumination
interacts with these positive expectancies to predict who will
engage in excessive alcohol consumption. These and other hy-
potheses could be tested to determine what combination of
V olume 3—Number 5 405
Susan Nolen-Hoeksema, Blair E. Wisco, and Sonja Lyubomirsky

[p.7]

conditions are necessary for rumination to trigger signiﬁcant
symptoms of eating disorders or substance abuse.
Other studies should investigate additional forms of escapist
behavior that may be related to rumination, such as self-inju-
rious behaviors. Some theorists have argued that these behaviors
are reinforced by the reductions in aversive emotions and
thoughts that occur when an individual engages in them (e.g.,
Hayes, Wilson, Gifford, Follette, & Strosahl, 1996; Nock &
Prinstein, 2004). This would suggest that some people who en-
gage in self-harming behavior may do so to quiet ruminations.
Rumination was signiﬁcantly related to nonsuicidal self-injury
behaviors in a cross-sectional study of adolescent girls (Hilt,
Cha, & Nolen-Hoeksema, 2008), and it predicted increases in
suicidal ideation over time in two samples of adults (Miranda &
Nolen-Hoeksema, 2007; Smith, Alloy, & Abramson, 2006).
Findings of further links between rumination and self-harming
behaviors would suggest that interventions to prevent self-harm
might beneﬁt from targeting the tendency to ruminate. Dialec-
tical behavior therapy (Linehan, Cochran, & Kehrer, 2001),
which has been shown to be helpful in reducing suicidal and
impulsive behavior, emphasizes the development of more
adaptive emotion-regulation skills. It would also be interesting
to determine whether this therapy reduces ruminative responses
to distress and whether this is one of its mechanisms of action.
Given the high comorbidity between depression and anxiety,
rumination might be expected to increase risk for anxiety
disorders as well as depression. Indeed, longitudinal prospec-
tive studies have found that people prone to rumination also
have higher levels of general anxiety and posttraumatic stress
symptoms (Fritz, 1999; Nolen-Hoeksema, 2000; Nolen-
Hoeksema & Morrow, 1991; J.A.J. Schwartz & Koenig, 1996;
Segerstrom et al., 2000; for signiﬁcant cross-sectional rela-
tionships between rumination and anxiety, see Abbott & Rapee,
2004; Fresco, Frankel, Mennin, Turk, & Heimberg, 2002; Ha-
rrington & Blankenship, 2002; Kocovski, Endler, Rector, &
Flett, 2005; Muris, Roelofs, Rassin, Franken, & Mayer, 2005).
Anxiety disorders, however, are typically characterized by a
different form of perseverative thought: worry. The distinctions
between rumination and worry and the proposed functions of
each style of thought are discussed below.
RUMINATION AND WORRY
W orry has been deﬁned as follows:
[A] chain of thoughts and images, negatively affect-laden and
relatively uncontrollable; it represents an attempt to engage in
mental problem-solving on an issue whose outcome is uncertain
but contains the possibility of one or more negative outcomes;
consequently worry relates closely to the fear process (Borkovec,
Robinson, Pruzinsky, & DePree, 1983, p. 10).
W orry is regarded as the central deﬁning feature of General-
ized Anxiety Disorder (American Psychiatric Association,
2000) and is present in most of the anxiety disorders (Barlow,
2002).
Rumination and worry are signiﬁcantly correlated with each
other (Fresco et al., 2002; Muris, Roelofs, Meesters, & Booms-
ma, 2004; Segerstrom et al., 2000; W atkins, 2004; W atkins,
Moulds, & Mackintosh, 2005), and they share many character-
istics (McLaughlin, Sibrava, Behar, & Borkovec, 2006). Both are
repetitive, perseverative forms of thought that are self-focused
(Barlow, 2002; Borkovec, Alcaine, & Behar, 2004; Segerstrom
et al., 2000). Rumination and worry share an abstract, over-
general thinking style (Sto¨ ber, 1996; W atkins & Teasdale, 2001;
W atkins, Teasdale, & Williams, 2000). Both are associated
with cognitive inﬂexibility and difﬁculty in switching attention
from negative stimuli (Davis & Nolen-Hoeksema, 1999; Haz-
lett-Stevens, 2001). Performance deﬁcits, difﬁculties in con-
centration and attention, poor problem solving, and inadequate
solution implementation are consequences of both rumination
and worry (Davey, 1994; Lyubomirsky & Nolen-Hoeksema,
1995; Lyubomirsky et al., 1999; W ard et al., 2003; W atkins &
Baracaia, 2002; W atkins & Moulds, 2005). Finally, both rumi-
nation and worry are associated with and exacerbate depression
and anxiety (Abbott & Rapee, 2004; Barlow, 2002; Fresco et al.,
2002; Harrington & Blankenship, 2002; Kocovski et al., 2005;
Muris et al., 2005; Nolen-Hoeksema, 2000; Nolen-Hoeksema &
Morrow, 1991; J.A.J. Schwartz & Koenig, 1996).
Still, studies directly comparing measures of rumination and
worry ﬁnd that they are statistically distinguishable (e.g., they
load on different factors; Fresco et al., 2002; Hong, 2007; Muris
et al., 2004; Segerstrom et al., 2000; W atkins et al., 2005). Key
features differentiate worry and rumination (see Table 1).
First, several theorists have noted differences in the time
orientation of worry versus that of rumination (e.g., Alloy, Kelly,
Mineka, & Clements, 1990; Barlow, 2002; Beck, 1967;
McLaughlin, Borkovec, & Sibrava, 2007; Mineka, W atson, &
Clark, 1998; W atkins, Moulds, & Mackintosh, 2005). W orry
tends to be future-oriented and focuses on threats that might
occur but have not yet occurred. Even when people worry about
something that has happened in the past, such as a faux pas they
made in a social situation, they are often worrying about the
implications of this event for the future (e.g., ‘‘Will everyone now
see me as an idiot?’’; Barlow, 2002). In contrast, although ru-
mination can involve concerns about possible threats in the
future, it predominantly involves going over past events, won-
dering why they happened, and thinking about the meanings of
those events (e.g., ‘‘How could my lover have cheated on me?’’;
Lyubomirsky et al., 1999; McLaughlin et al., 2007; W atkins,
2004; W atkins et al., 2005). W e suggest that the distinct theme of
rumination is loss, whether through fate, one’s own failure, or the
failure of others to live up to expectations.
People report that worry helps them to anticipate and prepare
for threat (Borkovec, Hazlett-Stevens, & Diaz, 1999). Those
prone to worry tend to feel uncertain they can control events and
cannot tolerate this uncertainty (Dugas, Gagnon, Ladouceur, &
406 V olume 3—Number 5
Rethinking Rumination

[p.8]

Freeston, 1998; Freeston, Rheaume, Letarte, Dugas, & Lad-
ouceur, 1994). W orry helps them feel that they have anticipated
possible threats and taken action against them. Because these
threats are unlikely to occur, worry is reinforced by the nonoc-
currence of the threats (Borkovec et al., 2004).
In contrast to the conscious functions of worry, Borkovec and
colleagues (Borkovec, 1979; Borkovec et al., 2004) argue that
the nonconscious function of worry is to avoid confronting core
negative affect and aversive images. The linguistic, verbal na-
ture of worry limits conscious access to vivid or painful images,
and the avoidance of these images then reinforces the worrying.
W orrying may also be reinforced by reductions in physiological
arousal associated with distressing images. Inducing individu-
als to worry before the presentation of an anxiety-producing
image reduces autonomic responses to these images (Borkovec
& Hu, 1990; Borkovec, Lyonﬁelds, Wiser, & Deihl, 1993;
Hoehn-Saric & McLeod, 1990).
In contrast, when ruminating, people report feeling that they
are gaining insight into the meanings of their feelings and
problems, trying to draw the connections between their prob-
lems, attempting to discern the reasons that things happen to
them, and trying to make sense of unhappy memories
(Lyubomirsky & Nolen-Hoeksema, 1993; Papageorgiou &
W ells, 2001; W atkins & Baracaia, 2002). Thus, rumination ap-
pears to be associated with sustained processing of negative
emotional material (McLaughlin et al., 2007). Further evidence
for this link comes from functional magnetic resonance imaging
studies that show that rumination is associated with increased
amygdala activity during the processing of emotional stimuli
(Ray et al., 2005; Siegle, Ingram, & Matt, 2002).
W e suggest that the content of rumination often focuses on the
very kind of core negative affect and concerns that worry seems
intended to avoid. Thus, it would appear that the nonconscious
avoidant functions of rumination are different from the non-
conscious avoidant functions of worry. What might rumination
serve to avoid? Behavioral theorists have argued that rumination
helps depressed individuals avoid engaging in the aversive
environment that surrounds them by preoccupying their atten-
tion and time (Ferster, 1973; Martell, Addis, & Jacobson, 2001).
W e go beyond this behavioral argument to suggest a more
complex avoidant function for rumination: Rumination serves to
build a case that the individual is facing a hopelessly uncon-
trollable situation and so he or she is not able to take action to
overcome the situation. That is, rumination is not just a cognitive
activity that removes people from aversive situations. Rather,
rumination provides depressed individuals with the evidentiary
base to justify withdrawal and inactivity. When people ruminate,
they build a mountain of evidence that all is hopeless and that
they might as well give up. This certainty that all their efforts are
fruitless may actually be less aversive than the uncertainty
about whether they can control situations. In turn, this sense of
certainty may help to reinforce rumination and the conclusions
drawn from rumination (Lyubomirsky & Nolen-Hoeksema,
1993). In addition, the case that is built through rumination
provides a rationale for avoiding taking action or responsibility
for situations and for withdrawing instead. In turn, the with-
drawal and inactivity that is justiﬁed by ruminations is rein-
forced because it reduces exposure to an aversive environment
(Ferster, 1973; Martell, Addis, & Jacobson, 2001).
W e take our clues for this line of argument from several
sources. Reductions in activity, anhedonia, and social with-
drawal are hallmarks of depression and are, indeed, symptoms
that set depression apart from anxiety (Clark & W atson, 1991).
Behavioral theories suggest that these symptoms are responses
to environments that are deﬁcient in positive reinforcers and full
of punishments. Thus, inactivity and withdrawal are reinforced
because they remove the individual from an aversive environ-
ment (Ferster, 1973; Lewinsohn & Graf, 1973). Evolutionary
theories, however, suggest that anhedonia, inactivity, and social
withdrawal function to conserve resources and reduce action in
situations where further action is futile or dangerous (Barlow,
2002; Nesse, 2000). The symptoms of depression also signal the
social environment to provide support rather than make de-
mands on the individual (W atson & Andrews, 2002). In turn, the
provision of social support by others reinforces the depressive
behavior (Ferster, 1973; Jacobson, Martell, & Dimidjian, 2001).
However, many social and environmental pressures operate
against the individual completely withdrawing and becoming
inactive (W atson & Andrews, 2002). People in the depressed
individual’s social network may not accept the conclusion that
all is lost and instead urge the depressed person to take action, to
fulﬁll his or her responsibilities (e.g., to take care of children), to
solve problems, or simply to lift his or her mood. Thus, depressed
people may need to convince important others that they should
TABLE 1
Distinguishing Features of Worry and Rumination
W orry Rumination
More future-oriented More past-/present-oriented
Focused on anticipated threats Focused on issues of self-worth, meaning, themes of loss
Conscious motive is to anticipate and prepare
for threat
Conscious motive is to understand the deep meanings of events, gain
insight, and solve problems
Nonconscious motive is to avoid core negative affect
and painful images
Nonconscious motive is to avoid aversive situations and the
responsibility to take action
V olume 3—Number 5 407
Susan Nolen-Hoeksema, Blair E. Wisco, and Sonja Lyubomirsky

[p.9]

not be expected to meet responsibilities or that problems are
unsolvable. Rumination may be motivated by this need.
Often depressed mood arises in the absence of an obviously
aversive or hopeless environment. Even when the depressed
person acknowledges there is ‘‘no good reason’’ for his or her
depression, evolutionary theories would suggest that depressed
mood would still signal to the individual that he or she has ex-
perienced a loss or is facing a hopeless situation (see also
Teasdale, 1985). This felt sense of loss and futility may in turn
activate nonconscious agendas to determine what has been lost.
This kind of agenda would lead to the kind of biased reﬂective
processing observed in depression, as the individual selectively
retrieves and rehearses negative recent events that match the
sense of loss and hopelessness and notes similarities across
them (e.g., ‘‘Every time I try to talk to my husband, it turns into a
ﬁght’’). The felt sense that all is hopeless may also bias the in-
dividual to selectively reﬂect on obstacles to possible solutions
to problems (e.g., ‘‘I could ask my husband what is wrong with
our marriage, but he probably won’t tell me’’).
W e are not suggesting that people consciously engage in ru-
mination to build a case that they should not be held responsible
for changing their situation. Nonetheless, rumination is rein-
forced by the reductions in distress that come from withdrawing
from aversive situations, from being relieved of responsibility,
and from a sense of certainty about one’s conclusions. Further,
rumination supports the social signaling function of depression
by providing reasons for others to come to the depressed person’s
aid (see also Jacobson et al., 2001).
Several of the studies already reviewed in this article support
our proposed functions of rumination. First, although rumina-
tors say they are trying to solve their problems, rumination leads
people to see obstacles to the implementation of solutions
(Lyubomirsky et al., 1999), to be less willing to commit to im-
plementing the solutions they generate (W ard et al., 2003), and
to be more likely to disengage from real-life problems than to
continue trying to solve them (Hong, 2007). Notably, these
patterns of results are observed even when the effects of de-
pressed mood are statistically controlled, suggesting that they
are linked to rumination per se. Similarly, rumination leads
people to be less willing to engage in pleasant activities to lift
their moods when given the chance (Lyubomirsky & Nolen-
Hoeksema, 1993). Thus, rumination appears to be effective at
convincing depressed individuals that they cannot take action
and overcome their problems.
Research on self-veriﬁcation theory (Swann, 1990) shows
that having one’s self-view veriﬁed is reinforcing, even when that
self-view is negative. Swann and colleagues have found that
people selectively solicit, attend to, recall, and believe feedback
from others that conﬁrms their self-concept (Giesler, Josephs, &
Swann, 1996; Swann, Grifﬁn, Predmore, & Gaines, 1987; Swann
& Read, 1981a, 1981b). In applications of this theory to de-
pression, researchers have found that depressed people selec-
tively seek criticism and other feedback from others that
conﬁrms their negative views of themselves (Joiner, 2002;
Swann, W enzlaff, Krull, & Pelham, 1992; Swann, W enzlaff, &
Tafarodi, 1992). The selective processing of negative informa-
tion seen in rumination would serve to verify depressed people’s
views of themselves as being unable to control important out-
comes, and this veriﬁcation could be highly reinforcing.
Regarding the social signaling function of depressive rumi-
nation, we have found that bereaved people prone to rumination
will reach out to others for social support more often than those
not prone to rumination (even after controlling for differences
between ruminators and nonruminators in depression levels;
Nolen-Hoeksema & Davis, 1999). In turn, positive social sup-
port is even more beneﬁcial to bereaved ruminators than to
bereaved nonruminators: Bereaved ruminators who receive
positive emotional support just after their loss show signiﬁcant
declines in depressive symptoms, whereas bereaved people who
are not ruminators show no relation between the degree of
emotional support received and changes in depressive symp-
toms. This suggests that rumination that is effective in signaling
to the social environment that the ruminator needs support may
eventually prove beneﬁcial to the ruminator and thus may be
reinforced. On the other hand, bereaved ruminators in our study
received more criticism from others for their inability to cope
than did nonruminators, suggesting the social signaling function
of rumination may backﬁre, making the environment even more
aversive and perhaps thereby motivating even more social
withdrawal.
If worry and rumination serve different functions, how can we
understand their comorbidity? Both worry and rumination are
associated with concerns about control and uncertainty
(Freeston et al., 1994; W ard et al., 2003). W e suggest that when
people are worrying, they are uncertain about their ability to
control important outcomes, but they have some belief that they
could control those outcomes if they just try (or worry) hard
enough (Alloy et al., 1990; Barlow, 1988). In contrast, when
people are ruminating, they are more certain that important
outcomes are deﬁnitely uncontrollable (Lyubomirsky et al.,
1999). Thus, worry and rumination differ in the degree of un-
certainty and uncontrollability people perceive in the environ-
ment: W orry occurs when people are less certain but see events
as potentially controllable, whereas rumination occurs when
people are more certain and see events as not controllable.
In turn, these perceptions of uncertainty and uncontrollability
can wax and wane depending on actual events. For example, a
man who has been worrying that he might lose his job may move
into rumination about the meanings of job loss when he receives
a poor performance review from his boss (e.g., ‘‘I’m a total failure
at life’’). The poor review increases his certainty that he can do
nothing to avoid losing his job, so he is more certain that the
situation is uncontrollable. In contrast, if some event were to
challenge his certainty that he will lose his job (for example, the
boss himself gets ﬁred), the man might move from rumination
into worry, as his level of certainty about job loss decreases and
408 V olume 3—Number 5
Rethinking Rumination

[p.10]

his belief in the potential controllability of losing his job in-
creases.
People may also shift from rumination to worry when their
inaction and withdrawal are not being reinforced by others, as
when there are demands on individuals to continue to do their
job, tend to their children, interact socially, and so on. Similarly,
some berate themselves for ruminating and for becoming de-
pressed and immobilized (see Campbell-Sills, Barlow, Brown, &
Hoffman, 2006; Papageorgiou & W ells, 2001). To be able to
engage in some action, people may attempt to avoid their
thoughts of hopelessness and futility by worrying. For example,
individuals with Generalized Anxiety Disorder say that worrying
helps them avoid thinking about more aversive emotional topics
(Borkovec & Roemer, 1995). Thus, worry may help people avoid
rumination about the certain lack of control in their lives. Those
who have ruminated a lot in the past, however, may easily slip
back into rumination because they have rehearsed thoughts of
hopelessness a great deal, making them highly accessible. With
minor triggers, including a mild depressed mood that signals
futility, rumination is reignited (e.g., Persons & Miranda, 1995).
Our arguments about the distinctions between rumination and
worry, and about the avoidant functions of rumination, neces-
sitate more research. As we argue below, however, we believe
they hold important implications both for understanding self-
reﬂection and for clinical interventions with ruminators.
RUMINATION IN RELATION TO OTHER COPING AND
EMOTION-REGULATION STRATEGIES
When Nolen-Hoeksema (1987, 1991) proposed the response
styles theory of rumination in the late 1980s and early 1990s,
models of coping were popular in personality, social, and clin-
ical psychology (e.g., Carver, Scheier, & W eintraub, 1989;
Endler & Parker, 1994; Folkman & Lazarus, 1980, 1986; Moos
& Billings, 1982). Whether one considers rumination a coping
strategy depends on how one deﬁnes coping—as any response,
adaptive or maladaptive, that might affect the outcome of a
situation, or only as a response aimed at producing positive
outcomes to stressful situations. Nolen-Hoeksema (1991) elec-
ted to deﬁne rumination as a maladaptive response to distressing
situations, regardless of the intentions people have for engaging
in rumination.
Coping theorists, however, have catalogued the various ways
people could cope with stressful situations. For example, a
common distinction has been made between problem-focused
coping strategies that can change an aversive situation and
emotion-focused coping strategies that manage the individual’s
emotional reactions to the situation. Problem-focused coping
tends to be correlated with positive psychological outcomes,
although the results have been somewhat mixed (see Lam et al.,
2003; Skinner, Edge, Altman, & Sherwood, 2003, for a review).
The relationships between emotion-focused coping strategies
and psychological outcomes have also been quite inconsistent
across studies, in part because measures of emotion-focused
coping contain a disparate collection of responses to negative
moods, including reappraisal, wishful thinking, a desire for
social support, denial, and avoidance (see Stanton, Danoff-Burg,
Cameron, & Ellis, 1994, for a critique of these scales). Reap-
praisal coping tends to be associated with positive psychological
outcomes (e.g., less depression and anxiety), whereas wishful
thinking (which has similarities to rumination) and avoidance of
emotions tend to be associated with negative psychological
outcomes (see Carver et al., 1989; Skinner et al., 2003). Even
within the construct of avoidance coping, the omnibus coping
measures comprise a number of subscales tapping different
types of avoidance, including cognitive denial (e.g., ‘‘I refuse to
believe that it has happened’’), dangerous escapist behaviors
(e.g., ‘‘I use alcohol or drugs to make myself feel better’’), and
behavioral disengagement (e.g., ‘‘I admit to myself that I can’t
deal with it and quit trying’’; Carver et al., 1989). Although
dangerous escapist behaviors have been consistently associated
with poor psychological outcomes, cognitive denial and be-
havioral disengagement have been less consistently related to
poor outcomes. These strategies may be adaptive in the short
term to manage initial distress. But these behaviors may be
maladaptive in the long run if they prevent the individual from
dealing with the situations that cause distress.
In the 1990s and 2000s, theories of emotion-regulation pro-
liferated (see reviews in Gross, 2007; Mennin & Farach, 2007).
One of the most inﬂuential emotion-regulation models is Gross’s
(1998) model of antecedent-focused and response-focused
emotion regulation. Antecedent-focused strategies, such as re-
appraisal, attempt to modify the likelihood or experience of a
stressor to prevent or reduce the amount of distress it creates.
Response-focused strategies, such as suppression, attempt to
modify one’s emotional response to a stressor once it has oc-
curred. In experimental studies, Gross and colleagues (see
Gross & Thompson, 2007) have found that instructing partici-
pants to reappraise a distressing image lowers subjective dis-
tress, whereas instructing participants to suppress their
emotional expressions in response to a distressing image in-
creases sympathetic arousal. Using self-report measures, Gross
and John (2003) found that people who often use reappraisal
experience more positive well-being and interpersonal func-
tioning, whereas people who often use emotional suppression
experience less positive well-being and interpersonal func-
tioning.
How does rumination relate to the several coping and emo-
tion-regulation constructs that have been studied most inten-
sively over the last 30 years? Figure 1 presents our best
conjectures, based on existing studies. As reviewed earlier,
experimental studies reveal that rumination is associated with a
relatively weak problem-solving orientation, poorer problem
solving, and with more negative appraisals of situations. Cor-
relational studies show that rumination is positively related to
suppression or avoidance of distressing feelings and thoughts
V olume 3—Number 5 409
Susan Nolen-Hoeksema, Blair E. Wisco, and Sonja Lyubomirsky

[p.11]

(Moulds, Kandris, Starr, & W ong, 2007; Nolen-Hoeksema &
Morrow, 1991; W enzlaff & Luxton, 2003). People who ruminate
may seek to escape from aversive self-focus by suppressing
negative feelings and thoughts cognitively or by engaging in
behaviors to avoid self-awareness. In turn, we speculate in
Figure 1 that attempts to suppress or avoid ruminative thoughts
mediate the link between rumination and binge eating, binge
drinking, and self-harm (Hilt, Cha, & Nolen-Hoeksema, 2008;
Miranda & Nolen-Hoeksema, 2007; Nolen-Hoeksema et al.,
2007).
W enzlaff and Luxton (2003) suggest that suppression and
avoidance can also fuel rumination. Suppression often backﬁres,
increasing the availability of unwanted thoughts (W egner,
1994). Depressed people try valiantly to suppress their negative
thoughts but experience rebounding of these thoughts, which
could contribute to rumination (W enzlaff et al., 1988). Indeed,
W enzlaff and Luxton (2003) followed people who were initially
high or low on suppression, but uniformly low on rumination, for
10 weeks and found that the high-suppression people who ex-
perienced stressful events showed increases in rumination over
time, whereas the low-suppression people did not. Engaging in
behavioral avoidance (e.g., binge eating) can also contribute to
rumination when these behaviors create more problems in in-
dividuals’ lives, as suggested by our ﬁndings that adolescent
girls who engage in binge eating display increases in rumination
over time (Nolen-Hoeksema et al., 2007).
In contrast, our experimental studies show that inducing
dysphoric people to distract from negative thoughts leads to
relatively more positive appraisals of situations, better problem
solving, and less distress. These are short-term effects of dis-
traction. Chronic use of distraction without subsequently en-
gaging in reappraisal or problem solving, however, may morph
into avoidance of negative emotions through maladaptive
avoidance behaviors.
One emotion-focused coping response not shown in Figure 1
is emotional expression. In a long line of impressive research,
Pennebaker and colleagues (see reviews by Frattaroli, 2006;
Niederhoffer & Pennebaker, 2002) have shown that people
prompted to express distressing emotions about difﬁcult or
traumatic events through writing about them or talking to others
experience more positive physical and psychological health
outcomes. Stanton and colleagues (Stanton, Kirk, Cameron, &
Danoff-Burg, 2000) have extended Pennebaker’s work to in-
vestigate emotional processing as a mechanism by which emo-
tional expression impacts physical health. They deﬁne
emotional processing as active attempts to acknowledge, explore
meanings, and come to an understanding of one’s emotions
(Stanton et al., 2000). Longitudinal studies have found that
emotional processing predicts improved emotional well-being
over time, but there are important moderators of these rela-
tionships (see Austenfeld & Stanton, 2004, for a review).
W e have omitted emotional expression or processing from Fig-
ure 1 because the evidence about its relationships to rumination is
mixed. Pennebaker (1989) suggested that emotional disclosure
can reduce rumination, and Pennebaker and O’Heeron (1984)
found that the widows of men who committed suicide showed less
rumination about their tragedy over time if they shared their ex-
perience with friends. On the other hand, Stanton and colleagues
(2000) found that emotional processing was related to more ru-
mination, but only in men. In a cross-sectional correlational study
of 186 undergraduates, we found that Stanton and colleague’s
emotional processing scale was signiﬁcantly positively correlated
with rumination, with no gender differences in the size of this
correlation (Nolen-Hoeksema & Jacobs, 2007).
Rumination 
Distress 
Suppression 
Positive
Appraisals 
Problem
Solving 
Avoidance /
Escape
Binge Eating,
Binge Drinking,
Self-harm
Distraction 
+
LT+ 
ST+
ST–
+
+
+
+
–
+
–
–
+
+
LT+
+
ST+
Fig. 1. A conceptual model of the relationships between rumination and other coping or emotion-
regulation constructs. 15 positive relationship; /C05 negative relationship; ST 5short-term;
LT5long-term.
410 V olume 3—Number 5
Rethinking Rumination

[p.12]

Pennebaker (1989) argued that emotional disclosure reduces
rumination, and ultimately distress, only when it leads to a
change in individuals’ understanding of the sources of their
distress. Sometimes, people may attempt to understand their
emotions through disclosure and processing, but instead fall into
rumination. Austenfeld and Stanton (2004) and Pennebaker
(1989) suggest that the interpersonal context may be important
in determining whether emotional expression and processing are
helpful or unhelpful. When others are supportive of emotional
expression and help individuals understand their distressing
situations in new ways, rumination may decline. When others
are unsupportive or critical of individuals’ emotional expres-
sions, rumination may be fueled by this negative response. The
results of our bereavement study support these contentions
(Nolen-Hoeksema & Davis, 1999). Bereaved ruminators whose
social networks were supportive of their expressions of grief
evidenced declines in depression over time. In contrast, be-
reaved ruminators whose social networks were unsupportive and
critical of their continued need to talk about their loss experi-
enced less decline in depression over time.
Several researchers are currently trying to clarify when self-
reﬂection, including the acknowledgement and processing of
emotions, is adaptive and when it turns into rumination. W e
discuss these important efforts later in this article.
COGNITIVE AND NEURAL CORRELATES OF
RUMINATION
Researchers have recently been exploring the possible cognitive
and neural correlates of rumination. Certain cognitive deﬁcits,
biases or changes in neural activity may be both causes and
consequences of rumination.
Cognitive Deﬁcits and Biases in Depressive Rumination
Deﬁcits in concentration and memory are common in depres-
sion, particularly on tasks in which attention is not constrained
by the task (Hertel & Hardin, 1990, Hertel & Rude, 1991) and
when attention is easily redirected to personal concerns or ir-
relevant information (Ellis, Thomas, & Rodriguez, 1984). Ru-
mination may further impair concentration and memory for
neutral stimuli by distracting the attention of depressed indi-
viduals during cognitive tasks, thus impairing overall perfor-
mance. In a series of three experimental laboratory studies,
dysphoric students who ruminated about their feelings and
personal characteristics reported diminished concentration on
academic tasks, needed additional time during reading and test
taking, and displayed impaired work strategies and performance
(Lyubomirsky, Boehm, Kasri, & Zehm, 2007; see also Kuhl,
1981; Strack, Blaney, Ganellen, & Coyne, 1985). Rumination
alone, in the absence of a depressed mood, did not produce
impaired concentration in these studies.
Rumination may also be associated with deﬁcits in retrieval of
nonvalenced information from memory. Hertel (1998) tested
recall for lists of words in dysphoric and nondysphoric indi-
viduals. After learning the words, participants were induced to
ruminate, to distract themselves, or they were given no in-
structions at all. The dysphoric participants performed worse
than the nondysphoric ones in the rumination and control con-
ditions, but no difference emerged between the groups in the
distraction condition.
Ruminators may have a general deﬁcit in the ability to switch
from unhelpful to helpful strategies for performing a task. W e
found that people who score high on our self-report scale of
rumination show more perseverative errors on the Wisconsin
Card Sort Task than do people who score low on rumination, even
after controlling for group differences in levels of depression
(Davis & Nolen-Hoeksema, 2000). Similarly, W atkins and
Brown (2002) found that depressed patients induced to ruminate
showed a signiﬁcant increase in the tendency toward stereo-
typed counting responses in a random-number generation task
(thought to reﬂect a tendency to perseverate on a nonoptimal
strategy) in comparison with depressed patients induced to
distract or nondepressed controls. Whitmer and Banich (2007)
noted that such difﬁculties could be caused by the participant
either having trouble switching to the new strategy or having
difﬁculty inhibiting the previously useful strategy. Using a set-
switching task to distinguish these two possibilities, the re-
searchers found that ruminators, who scored high on our mea-
sure of depressive rumination, were particularly impaired in
their ability to inhibit previously useful strategies. This effect
held even when statistically controlling for depressive symp-
toms. Thus, people prone to rumination may have general deﬁ-
cits in the ability to inhibit nonoptimal strategies currently in
use in order to adopt new, potentially more useful strategies for
solving tasks.
Rumination may also be associated with biases in information
processing, speciﬁcally a tendency to attend to and remember
negative information rather than positive information. W e have
already summarized the evidence that inducing depressed
people to ruminate leads to negative biases in tests of relatively
explicit cognitive processes, such as the retrieval of autobio-
graphical memories or the generation of predictions about the
future (Lyubomirsky et al., 1998). Recent work also suggests
that depressed ruminators show biases towards negative infor-
mation in tests of basic attention and implicit memory and show
difﬁculties in inhibiting negative information when it is irrele-
vant (Joormann, 2004, 2005; Siegle, Steinhauer, Thase, Stenger,
& Carter, 2002). For example, self-reported rumination pre-
dicted bias for negative words on a commonly used attention
measure, the dot probe task, even when statistically controlling
for depressive symptoms (Donaldson, Lam, & Mathews, 2007).
And Joormann (2006) investigated the inhibition of emotional
stimuli, both positive and negative, in ruminators. She found
that individuals who scored high on our measure of rumination
showed greater deﬁcits in inhibiting emotional information than
did individuals who scored low in rumination. This ﬁnding
V olume 3—Number 5 411
Susan Nolen-Hoeksema, Blair E. Wisco, and Sonja Lyubomirsky

[p.13]

remained signiﬁcant when individual differences in dysphoria
(which were correlated with rumination) were statistically con-
trolled. Of particular interest is the ﬁnding that ruminators have
difﬁculty inhibiting negative information. People who ﬁnd it
difﬁcult to inhibit negative information when necessary, and for
whom irrelevant negative information intrudes upon and inter-
feres with processing, may ﬁnd it easy to jump from one negative
thought to another and become drawn into rumination. On the
other hand, rumination on negative information may make it
difﬁcult to inhibit irrelevant negative stimuli, which in turn
feeds rumination.
Deﬁcits in the inhibition of negative information may make it
difﬁcult for ruminators to use positive distracters to successfully
manage negative moods (Joormann, 2005). W enzlaff and col-
leagues (1988) found that dysphoric people tend to use negative
distracters (e.g., thoughts of a car accident) when trying to turn
their attention away from distressing information, whereas
nondysphoric people tend to use positive distracters (e.g.,
thoughts of winning a sweepstakes). In addition, even when
experimenters provided participants with positive and negative
distracters, dysphoric participants were less likely to use the
positive distracters and more likely to use the negative dis-
tracters than were nondysphoric participants. These results
were obtained despite the fact that dysphoric participants ac-
knowledged that positive distracters are more useful than neg-
ative distracters in redirecting attention away from distressing
material. Thus, the dysphoric participants understood the utility
of positive distracters but they had more difﬁculty using them
when it was beneﬁcial to do so.
Again, this difﬁculty in inhibiting negative information and
maintaining attention to positive distracters may be even more
pronounced among depressed people who are ruminating
(Hertel & Gerstle, 2003). Joormann and Seimer (2004) found
that dysphoric individuals induced to ruminate were slower to
recall positive autobiographical memories to repair their moods
when instructed to do so than were dysphoric people induced to
distract or nondysphoric controls, suggesting they had more
difﬁculty retrieving these memories. Similarly, McFarland and
Buehler (1998) found that dysphoric participants prompted to
focus on their negative moods were less likely to use positive
memories to overcome their negative moods than were dysphoric
people distracted from self-focus. W e found that dysphoric
people induced to ruminate rated themselves as being signiﬁ-
cantly less likely to engage in positive distracting activities in
comparison with the dysphoric/distraction group and the two
nondysphoric groups (Lyubomirsky & Nolen-Hoeksema, 1993).
Notably, the dysphoric ruminators rated these activities as being
just as useful for lifting one’s mood as did the other groups. In
other words, they acknowledged that it would lift their mood to
engage in these activities, but they were less inclined to actually
engage in them. The inability to successfully use positive dis-
tracters to relieve rumination and negative mood may motivate
ruminators to turn to escapist behaviors, such as binge eating or
binge drinking, to escape from aversive self-awareness. That is,
fundamental deﬁcits in inhibiting negative information may
both make it more difﬁcult for ruminators to suppress negative
thoughts and make it more likely they turn to maladaptive be-
haviors to escape from these thoughts, contributing to the links
between rumination and maladaptive behaviors such as binge
eating and binge drinking (e.g., Nolen-Hoeksema et al., 2007).
Deﬁcits in inhibiting negative information could also con-
tribute to the interpersonal problem-solving deﬁcits observed in
dysphoric and clinically depressed people induced to ruminate
(Lyubomirsky & Nolen-Hoeksema, 1995; W atkins & Moulds,
2005). Even when dysphoric ruminators generate good solutions
to problems, they appear more reluctant to move forward into
implementing those solutions, expressing less conﬁdence in the
solutions and wanting more time to think about them (W ard
et al., 2003). This may be because they have difﬁculty inhibiting
thoughts about the ways the solutions could go awry.
Neural and Genetic Correlates of Rumination
Rumination involves both attention to negative affect and self-
referential processing (Lyubomirsky et al., 1999). Furthermore,
as we just reviewed, emerging evidence suggests that rumination
may be associated with deﬁcits in inhibitory processes, perhaps
especially for negative information (Joormann, 2005). Thus,
rumination would be expected to be associated with altered
activation in neural areas involved in attention to negative
affect, self-referential processing, and inhibition of negative
information.
Neuroimaging studies have consistently shown that tasks that
arouse negative affect or require participants to focus on nega-
tive affect are associated with activity in the amygdala (Cun-
ningham, Raye, & Johnson, 2004, 2005; Sanfey, Rilling,
Aronson, Nystrom, & Cohen, 2003). By contrast, self-referential
processing is associated with increased activity in a number of
areas, including the anterior medial cortex (medial frontal gyrus
and/or anterior cingulate cortex) and posterior medial cortex
(posterior cingulate cortex and/or precuneus; see Johnson et al.,
2006; Macrae, Moran, Heatherton, Banﬁeld, & Kelley, 2004;
Ochsner et al., 2005, for reviews of ﬁndings focusing on medial
frontal areas and see Cavanna & Trimble, 2006; V ogt & Laureys,
2005, for reviews focusing on medial posterior areas). Finally,
deﬁcits in the inhibition of negative emotional stimuli have been
associated with activity in the rostral subdivision of the anterior
cingulate cortex (Davidson, Pizzagalli, Nitschke, & Putnam, 2002).
In turn, the few neuroimaging studies of rumination show
differences between ruminators and nonruminators in these
areas of the brain when performing tasks that are emotional,
involve self-referential thought, or require inhibition of emotion.
Two studies have revealed that participants who score higher on
trait rumination show greater amygdala activity in response to
negative stimuli (Siegle, Steinhauer, Thase, Stenger, & Carter,
2002) or when asked to appraise negative photos in ways that
412 V olume 3—Number 5
Rethinking Rumination

[p.14]

would increase their negative affect (Ray et al., 2005). In ad-
dition, Ray and colleagues (2005) found that ruminators showed
more activity in the medial prefrontal cortex (PFC) when in-
structed to use appraisal to enhance their negative affect, sug-
gesting that they were increasing their negative affect by
interpreting negative photos as self-relevant. When participants
high on rumination were simply told to look at negative photos,
they showed greater activity in the medial PFC than they did
when they were told to change negative affect in response to
these photos, suggesting that they may chronically recruit me-
dial prefrontal regions associated with negative self-referential
processing even when instructed simply to look at photos. Ray
et al. (2005) also found increased activity in the left ventrolateral
PFC when ruminators were looking at negative photos without
instructions to regulate their response. This area of the brain has
been associated with representing changes in the affective rel-
evance of stimuli, and the increased activity in this area among
ruminators suggests they chronically recruit brain regions as-
sociated with updating the affective salience of stimuli, even
when not instructed to regulate their affect.
Joormann and Gotlib (2005) found that greater activity in the
rostral anterior cingulate cortex was associated with greater
ability to inhibit negative distracters in depressed and nonde-
pressed participants. Moreover, participants who scored higher
on rumination, regardless of their depression status, showed
lower rostral anterior cingulate activity when attempting to in-
hibit negative distracters. This suggests that the deﬁcits in in-
hibition of negative stimuli seen in dysphoric rumination could
be associated with decreased anterior cingulate activity.
Johnson, Nolen-Hoeksema, Mitchell, and Levin (2008) in-
duced dysphoric and nondysphoric participants to ruminate or
distract while they were undergoing neuroimaging. In addition,
individual difference measures of rumination were obtained for
all participants. They found that both dysphoric individuals and
individuals high on rumination showed lower activity in the
anterior medial PFC during the rumination task than did non-
dysphoric and low ruminating individuals. As the anterior PFC
is associated with thinking about approach-related goals
(Johnson et al., 2006), this suggests that dysphoric ruminators
were less likely to recruit areas associated with positive self-
referential processing when ruminating. Dysphoric individuals
and ruminators showed greater activity than did nondysphoric
and nonruminative individuals in both the anterior and posterior
medial PFC during the distraction trials, suggesting sustained
self-referential processing even when they were supposed to be
engaging in distracting thoughts. This is consistent with the
previously reviewed behavioral evidence asserting that rumi-
nation is associated with difﬁculty in disengaging from self-
focused thoughts when it would be appropriate to do so.
Finally, a recent study examined genetic variants associated
with rumination (Hilt, Sander, Nolen-Hoeksema, & Simen,
2007). This study focused on a single nucleotide polymorphism
in the brain-derived neurotropic factor (BDNF) gene resulting in
a valine-to-methionine substitution at codon 66 (V al66Met),
which has been associated with childhood-onset mood disorders
(e.g., Strauss et al., 2004). Preclinical and human work has
suggested that BDNF plays a role in hippocampal functioning,
in synaptic plasticity in times of stress, and in PFC functioning
(for a review, see Egan et al., 2003). In turn, depression is as-
sociated with alterations in the structure and functioning of the
hippocampus and PFC (Davidson et al., 2002), and as noted
above, rumination is associated with biased memory processes
and with altered activity in prefrontal areas. W e reasoned that
rumination may be a mediator between the BDNF gene and
depressive symptoms. Researchers interviewed 200 young ad-
olescent girls and their mothers to assess depressive symptoms
and rumination and drew blood samples to extract DNA. The
V al/V al genotype for BDNF was associated with greater rumi-
nation in the girls and with more childhood-onset depression,
and in turn, rumination was a signiﬁcant mediator of the rela-
tionship between the V al/V al genotype and childhood-onset
depressive symptoms.
Understanding more about the neural and genetic correlates of
rumination can shed light on possible contributors to the tendency
to ruminate. Such studies also can provide information on the
mechanisms by which rumination contributes to depression.
ADAPTIVE FORMS OF SELF-REFLECTION?
Are there adaptive forms of rumination, or more generally, of self-
reﬂection? Several alternative conceptualizations of rumination and
self-reﬂection and many new measures of various types of self-
reﬂective thought have recently appeared in the literature (see
Luminet, 2004; Mor & Winquist, 2002;Segerstrom, Stanton, Alden,
& Shortridge, 2003; Siegle et al., 2004; W atkins, 2008). Some re-
searchers have attempted to understand the differences between
adaptive and maladaptive forms of self-reﬂection by conducting
meta-analyses of the literature (Mor & Winquist, 2002; W atkins,
2008) or by administering several different measures of self-
reﬂection to large samples of participants and using statistical
procedures to reveal underlying dimensions (Segerstrom et al.,
2003; Siegle et al., 2004). These studies have consistently
shown that the type of self-reﬂection we deﬁne as rumination—
an abstract, evaluative self-reﬂection, particularly one focused
on negative content—is associated with depression and other
types of negative affect (W atkins, 2008). Less clarity exists about
what types of self-reﬂection are adaptive or, at least, benign.
W e review the results of this growing and somewhat confusing
literature, organizing this section according to prominent al-
ternative theories about what makes rumination maladaptive
and what types of self-reﬂection may be adaptive.
Rumination Versus Intellectual Self-Reﬂection
One approach to understanding the differences between adap-
tive and maladaptive self-reﬂection has been to distinguish
V olume 3—Number 5 413
Susan Nolen-Hoeksema, Blair E. Wisco, and Sonja Lyubomirsky

[p.15]

between ruminative thought as a perseverative focus on negative
moods and problems versus an intellectual curiosity about the
self. Trapnell and Campbell (1999) developed separate mea-
sures of rumination and intellectual self-reﬂection. Their ru-
mination measure includes items like ‘‘I always seem to be
rehashing in my mind why I do things,’’ whereas their reﬂection
measure includes items like ‘‘I love analyzing why I do things.’’
Rumination was found to be associated with neuroticism and
reﬂection with openness to experience (Teasdale & Green, 2004;
Trapnell & Campbell, 1999). However, reﬂection was also sig-
niﬁcantly correlated with neuroticism, and rumination and re-
ﬂection were signiﬁcantly correlated with each other, suggesting
they share common variance (Teasdale & Green, 2004). Trapnell
and Campbell’s rumination subscale has also been found to be
positively associated with current depressive symptoms, but
the reﬂection subscale was found to be uncorrelated with de-
pressive symptoms (e.g., Siegle et al., 2004). Thus, this rumi-
nation subscale seems to consistently tap into a maladaptive
form of self-reﬂection, but the reﬂection subscale assesses a
form of self-reﬂection that is unclear in its adaptive value.
Several investigators have used factor analysis to reveal un-
derlying dimensions in the Ruminative Responses Scale of the
Response Styles Questionnaire, including symptom focus, self-
blame, isolation/introspection, and problem-solving analysis
(Bagby & Parker, 2001; Bagby et al., 2004; Conway, Csank,
Holm, & Blake, 2000; Lam et al., 2003; Roberts et al., 1998).
Symptom focus, self-blame, and isolation/introspection have
generally been positively correlated with depressive symptoms,
whereas problem-solving analysis, the measure of intellectual
self-reﬂection, has not (e.g., Lam et al., 2003). The Ruminative
Responses Scale has been aptly criticized, however, for having
items that overlap in content with depression items (e.g., ‘‘I think
about how alone I feel’’ and ‘‘I think about how hard it is to
concentrate’’). These items often fall on the symptom-focus sub-
scale in factor analyses, so it is not surprising that this subscale
tends to correlate most highly with depressive symptoms.
Treynor et al. (2003) attempted to correct this problem by
purging the Ruminative Responses Scale of items that could be
argued to overlap with depression items and submitting the re-
maining items to a factor analysis. The two factors obtained
paralleled Trapnell and Campbell’s (1999) conceptualization of
rumination and reﬂection and were labeled brooding and pon-
dering. Brooding tapped negative aspects of self-reﬂection, in-
cluding a focus on abstract ‘‘why me?’’ issues (e.g., ‘‘I think,
‘What am I doing to deserve this?’’’) and a focus on obstacles to
overcoming problems (e.g., ‘‘I think, ‘Why can’t I handle prob-
lems better?’’’). The brooding factor was positively correlated
with depression scores in a large sample both concurrently and
longitudinally over one year (Treynor et al., 2003; see also Siegle
et al., 2004).
The pondering scale included items that suggested a more
general self-reﬂective tendency (e.g., ‘‘I go someplace alone to
think about my feelings.’’) and other items that suggested a
problem-solving orientation to problems (e.g., ‘‘I analyze re-
cent events to try to understand why I am depressed’’). It was
positively correlated with depression concurrently but nega-
tively correlated with depression longitudinally (Treynor et al.,
2003).
Joormann, Dkane, and Gotlib (2006) examined the results of
the brooding and pondering subscales from the Ruminative
Responses Scale from participants with current major depres-
sion, remitted major depression, social phobia, and no psycho-
pathology. They found that participants with current major
depression had the highest brooding scores of all the groups and
that the remitted major depression and social phobia groups had
brooding scores that were signiﬁcantly higher than controls, but
not different from one another. As for the pondering scale,
participants with current major depression had signiﬁcantly
higher scores than control participants, with no other group
differences found. Next, Joormann and colleagues administered
the dot probe task to assess attentional bias toward negative
faces and used the self-referent encoding task to assess nega-
tive memory biases. Those scoring higher on brooding showed
more negative attentional and memory biases; furthermore, the
correlation between brooding and attentional biases (but not
memory biases) remained signiﬁcant after controlling for de-
pressive symptom scores. Greater pondering was associated
with more memory bias, but not more attentional bias, and the
association with memory bias was no longer signiﬁcant after
controlling for depression scores. The pattern of results from this
study suggests that brooding is associated with higher current
levels of depression, with a history of depression, and with at-
tentional biases (and to a lesser extent memory biases) toward
negative stimuli. Brooding was also linked to a diagnosis of
social phobia, which is in line with previous studies showing
rumination predicts anxiety as well as depression.
Joormann et al.’s (2006) ﬁndings that pondering is associated
with greater depression and with more negative memory biases
raise questions about its adaptiveness. Several other studies
examining the concurrent relationship between depressive
symptoms and the pondering subscale (or a slightly different
version of the scale) have also revealed positive correlations
(Fresco et al., 2002; Lam et al., 2003; Roberts et al., 1998; Siegle
et al., 2004). Treynor et al. (2003) found that, although pon-
dering was associated with more depression concurrently, it was
associated with less depression over time. Thus, it may be that
pondering is a form of self-reﬂection that may be emotionally
distressing in the short run, but adaptive in the long run because
it leads to successful problem solving.
Self-Regulation Theories
Self-regulation theories (Carver & Scheier, 1998; Duval &
Wicklund, 1972; Martin & Tesser, 1996; Pyszczynski &
Greenberg, 1987) argue that self-focused rumination is initiated
by perceived discrepancies between one’s current state or sit-
414 V olume 3—Number 5
Rethinking Rumination

[p.16]

uation and a goal or desired state. For example, if a woman has
the goal of a positive relationship with her husband but has been
having frequent arguments with him, she is likely to focus on the
discrepancy between her goal (a positive relationship) and her
current state (hostility between the couple; Martin & Tesser,
1996). The woman’s self-focused thinking will end either when
she takes action to overcome the discrepancies (e.g., talks with
her husband in an effort to repair the relationship) or when she
relinquishes the desired goal (e.g., decides her husband is im-
possible to live with and ﬁles for divorce). In this case, the
woman’s thoughts are instrumental and lead to a resolution of her
goal discrepancies. In contrast, if she simply continues to
perseverate on the discrepancies between the current state and
the desired state, the discrepancy will remain and she will ex-
perience negative affect. In this case, her ruminations
will have a deleterious outcome. Thus, self-regulation theories
suggest that rumination can be adaptive when it leads to problem
solving or the abandonment of unattainable goals, but it is
maladaptive when the individual only perseverates on dis-
crepancies.
A number of studies have supported the self-regulation the-
ories’ arguments that perseverating on self-discrepancies en-
genders negative affect (for reviews, see Carver & Scheier, 1998;
Martin, Shrira, & Startup, 2004; Martin & Tesser, 1996; W at-
kins, 2008). In particular, Pyszczynski and Greenberg (1987)
applied self-regulation models to depression, arguing that de-
pressed people tend to self-focus after failures, but not after
positive events. They found support for this argument in a
number of experimental studies (for a review, see Pyszczynski &
Greenberg, 1987). Similarly, chronically unhappy individuals
have been found to be more inclined than their happier peers to
dwell excessively about themselves after failures and, subse-
quently, to experience impaired concentration and performance
on important academic tasks (Lyubomirsky et al., 2007).
The results of a meta-analysis of studies on self-focus and
negative affect show that perseverating on negative self-content
is maladaptive (Mor & Winquist, 2002). The researchers ex-
amined 226 effect sizes across experimental and correlational
studies that used a variety of manipulations and measures and
concluded that self-focus after failure was associated with in-
creased negative affect but that self-focus after positive events
was associated with reduced negative affect. In a different effort
to make sense of the proliferation of self-report scales of self-
reﬂection and rumination in recent years, Segerstrom and col-
leagues (2003) administered six measures of repetitive thought
to 978 undergraduates and used multidimensional scaling to
reveal two underlying dimensions across the measures: positive
versus negative content and searching versus resolving. Re-
petitive thought with negative content was associated with more
negative affect than was repetitive thought with positive content.
Thus, the results of several studies support the idea that
perseverating on negative self-content is associated with nega-
tive affect, whereas focusing on positive self-content is associ-
ated with positive affect. These results generally map onto the
arguments of the self-regulation theories that self-reﬂection
leads to negative affect when it involves perseverating on self-
discrepancies.
However, the adaptiveness of other forms of self-reﬂection,
including a problem-solving orientation, is less clear. Segerst-
rom and colleagues (2003) did not ﬁnd a consistent relationship
between the searching/resolving dimension of repetitive thought
and negative affect. Similarly, Siegle and colleagues (2004)
administered 16 different measures of rumination to under-
graduates, depressed adults, and healthy adults across different
studies and concluded that two general constructs of negative
rumination and problem-solving rumination could be distin-
guished but that these two constructs are highly intercorrelated
and both generally related to dysphoria. W e note that studies of
the relationship of self-report measures of problem-solving
coping to depression have found mixed results (e.g., Lam et al.,
2003), suggesting that a problem-solving orientation does not
always lead to positive outcomes.
The mixed evidence about the adaptiveness of attempts
to understand and solve one’s problems raises the question of
when and how people take an effective problem-solving ap-
proach to self-discrepancies and when attempts to problem-
solve devolve into perseverative rumination. Clues to this
question come from our experimental studies of interpersonal
problem solving. Inducing dysphoric or depressed participants
to distract from their moods and ruminations for just 8 min leads
them to generate solutions to problems that are just as effective
as nondepressed participants’ solutions and signiﬁcantly more
effective than those generated by dysphoric participants in-
duced to ruminate. The short distraction induction also leads
dysphoric and depressed participants to express more control
and self-efﬁcacy, to appraise the causes of problems more op-
timistically, and to have more conﬁdence in their ability to
overcome their problems than do dysphoric people induced to
ruminate. By contrast, the nondysphoric participants in our
studies generate effective problem solutions and are positive
and efﬁcacious in their cognitions about their problems, re-
gardless of whether they have just undergone a rumination or
distraction induction.
These results suggest that attempts to resolve self-discrep-
ancies will be more successful and less likely to devolve into
perseverations about problems if individuals are either in a
neutral or positive mood or if they ﬁrst use neutral or positive
distractions to lift their moods and interrupt ongoing rumina-
tions. Is it simply that relieving an individual’s negative mood by
any means before they engage in self-reﬂection will allow that
self-reﬂection to be positive and efﬁcacious? The recent work by
W atkins, Teasdale, and colleagues, reviewed in the next section,
suggests that the answer to this question is ‘‘no’’: To affect the
quality of depressed people’s problem solving, it is critical to
interrupt the ruminative way they think about themselves and
their problems.
V olume 3—Number 5 415
Susan Nolen-Hoeksema, Blair E. Wisco, and Sonja Lyubomirsky

[p.17]

Abstract/Analytical Rumination Versus Experiential
Mindfulness
W atkins (2008) and colleagues (Teasdale, Segal, & Williams,
1995; W atkins, 2004; W atkins & Teasdale, 2001) have
distinguished between two types of rumination: one that
involves abstract, evaluative thoughts about the self or emotion
and current circumstances, and another that involves a
nonevaluative awareness of present experiences, which
W atkins and colleagues have referred to as concrete rumination
or mindful experiencing/being. Similar distinctions have
been made between monitoring and evaluating one’s mood and
the ability to be aware of and label one’s moods without evalu-
ating them (Reeves, W atson, Ramsey, & Morris, 1995; Swinkels
& Giuliano, 1995). In an impressive review of the literature on
various forms of repetitive thought, W atkins (2008) provides
evidence that more abstract, evaluative rumination is uncon-
structive, particularly when it is negatively valenced, in com-
parison with a more concrete focus on present situations and
experiences.
For example, W atkins and colleagues (W atkins, 2004; W at-
kins & Teasdale, 2001) induced an analytical focus or an ex-
periential focus in depressed patients, using the rumination
stimuli developed by Nolen-Hoeksema, Lyubomirsky, and col-
leagues in previous studies. In the analytical focus condition,
patients were instructed to think about the causes, meanings,
and consequences of their feelings. In the experiential focus
condition, the same stimuli were presented to participants, but
they were instructed to ‘‘think about the concrete experience of
x.’’ The researchers found that although the experiential in-
duction did not lift depressed participants’ negative moods, it
led to less overgeneral (i.e., categoric) autobiographical memory
than did the analytical rumination induction. Other studies
using these inductions have shown that the experiential in-
duction prompts depressed participants to engage in less global
negative self-judgments (Rimes & W atkins, 2005) and better
social problem solving (W atkins & Moulds, 2005) than did the
analytical rumination induction.
The neuroimaging study of rumination described earlier
(Johnson et al., 2008) also supports a distinction between ana-
lytical and experiential ruminations. In this study, there were
two rumination conditions, an analytical condition (e.g., think
about why things turn out the way they do, what your feelings
mean), and an experiential condition (e.g., think about your
current physical sensations, how motivated you feel). In both
dysphoric and nondysphoric individuals, the analytical rumi-
nation condition tended to result in more medial PFC activity
than did the experiential rumination condition, suggesting it
induced greater self-referential thinking. However, dysphoric
participants and those high in rumination showed greater re-
duction in activity in the anterior medial PFC, which is asso-
ciated with approach-related goals, in the analytical rumination
condition than they did in the experiential rumination condition,
suggesting the dysphorics and ruminators were thinking less
about approach-related goals when engaging in analytical ru-
mination than when engaging in experiential rumination.
The behavioral work of W atkins and colleagues and our recent
neuroimaging ﬁndings suggest that the maladaptive component
of rumination may be its abstract analytical aspects, whereas a
more experiential form of self-reﬂection is not maladaptive.
Furthermore, our distraction induction’s positive effects on
thinking may not be solely due to improvements in participants’
moods, because W atkins’ experiential induction does not lift
participants’ depressed moods, but it does improve the quality of
their thinking. This work clearly has important implications for
therapeutic interventions for people prone to depressive rumi-
nation.
INTERVENTIONS TO OVERCOME RUMINATION
The consistent evidence from experimental studies that short
periods of positive distractions improve not only depressed
people’s moods, but also the quality of their thinking and
problem solving, suggests the importance of teaching people
prone to depressive rumination to engage in neutral or pleasant
distractions as a short-term strategy when they ﬁnd themselves
caught in ruminative thinking. Once individuals’ moods are
lifted through positive distractions, they may engage in problem
solving or reappraisal to address the situations contributing to
their moods.
The kinds of activities that might serve as distractions (e.g.,
going jogging, getting together with friends) are similar to ac-
tivities recommended in behavioral activation interventions for
depression (Jacobson et al., 1996; Lewinsohn, Antonuccio,
Brekenridge, & Turi, 1984), and studies have afﬁrmed the efﬁ-
cacy of these interventions for depression (Jacobson et al., 1996,
2001). Behavioral activation may work by countering the action
tendency that is central to depression—namely, withdrawal and
inactivity.6 Our research suggests that these strategies also re-
lieve depression by teaching depressed people how to break
their habitual ruminative cycle.
Some people may chronically attempt to distract themselves
from or suppress their moods and problems. Depressed indi-
viduals do engage in more suppression than do nondepressed
ones (Beevers, W enzlaff, Hayes, & Scott, 1999), but it is difﬁcult
to maintain. Negative thoughts tend to rebound with greater
force after attempts to suppress (W egner & W enzlaff, 1996). As
noted earlier, depressed people, particularly depressed rumi-
nators, ﬁnd it difﬁcult to inhibit negative thoughts and tend to
choose the wrong cognitive activities to distract themselves (i.e.,
they focus on negative thoughts and memories rather than pos-
itive ones; Joormann & Siemer, 2004; W enzlaff et al., 1988).
Although depressed ruminators may engage in distracting be-
haviors to suppress their thoughts, our work suggests that they
6W e thank David Barlow for calling attention to this mechanism.
416 V olume 3—Number 5
Rethinking Rumination

[p.18]

may sometimes turn to maladaptive behaviors, such as binge
eating and binge drinking (e.g., Nolen-Hoeksema et al., 2007).
Recent conceptualizations of behavioral activation interven-
tions (Jacobson et al., 1996) suggest that effective behavioral
strategies not only distract individuals from their moods and
increase positive reinforcers in the short-term, but that they also
increase positive reinforcers for the long-term by helping to
overcome problems in their lives. Indeed, if people simply avoid
their problems through constant distraction, these problems are
likely to recur. Thus, it is critical that behavioral interventions
encourage depressed people to engage in problem solving after
engaging in short-term distractions and/or to focus on activities
that increase the probability that their environments will be
improved.
In light of the effectiveness of distraction and behavioral ac-
tivation interventions for rumination and depression, it seems
paradoxical that interventions designed to focus attention on
distressing emotions and thoughts, such as experiential or
mindfulness therapies, also have positive effects on depression
in some studies. Mindfulness therapy (Segal, Williams, &
Teasdale, 2002; Teasdale et al., 2000) and acceptance-based
approaches (Hayes et al., 2003) teach depressed people to no-
tice their feelings and thoughts without judging them or be-
coming embroiled in them. Mindfulness interventions have been
shown to reduce relapse following remission in people with re-
current depression (Teasdale et al., 2000) and to reduce de-
pressive symptoms in patients with residual depression despite
having undergone pharmacotherapy (W atkins et al., 2007).
Mindfulness training may help depressed people gain attentio-
nal control and reduce the activation of associative networks of
negative thoughts, allowing depressive thoughts to enter and
leave consciousness without spiraling the individual into de-
pressive rumination (Segal et al., 2002; Teasdale et al., 1995).
Over time, mindfulness practices may thus reduce the links
between depressive thoughts in the associative network.
Our functional analysis of rumination also suggests another
mechanism by which mindfulness may help to reduce or prevent
relapse in depression. If rumination serves to build a case for
hopelessness, mindfulness techniques may reduce ruminations
by challenging the validity of this case. Mindfulness strategies
teach individuals that their thoughts are not necessarily true and
do not control their actions and that they should instead to view
their thoughts as outside of or distant from themselves (Segal
et al., 2002). Thus, these techniques may challenge the validity
of the case the ruminations have built for hopelessness and may
train individuals not to mechanically accept the felt sense of
hopelessness that comes with depression. Mindfulness or ex-
periential interventions are thought to reduce worry and anxiety
by reducing avoidance of painful images and negative emotions
and by aiding in the processing of these images and emotions
(Kabat-Zinn et al., 1992; Miller, Fletcher, & Kabat-Zinn, 1995;
Roemer, Salters-Pedneault, & Orsillo, 2006). These interven-
tions may have similar effects on rumination, to the extent that it
serves similar emotional avoidance functions (W atkins et al.,
2007).
The cognitive restructuring techniques of cognitive therapy
(Beck, Rush, Shaw, & Emery, 1979) might seem to engage de-
pressed people in a form of rumination, in that they focus at-
tention on the stream of negative thoughts passing through the
depressed person’s mind. Cognitive therapy, however, teaches
depressed people, including depressed ruminators, methods for
challenging these thoughts rather than passively replaying or
accepting them. Barber and DeRubeis (1989) and Teasdale et al.
(1995) suggest that cognitive therapy works not by changing the
content of depressed people’s cognitions, but by teaching them
methods for standing apart from those cognitions and ques-
tioning them when they occur. In other words, the key to therapy
is for people to stop automatically accepting the truth value of
their negative thoughts and to choose to substitute these
thoughts with more rational or adaptive ones. This argument
suggests that cognitive therapies may also be effective in part
because they counter the avoidant functions of ruminations in
developing a case that individuals cannot do anything to change
their environments.
Finally, interpersonal therapy (Klerman & W eissman, 1986;
W eissman & Markowitz, 2002) and social problem-solving
therapies (e.g., Arean, Perri, Nezu, & Schein, 1993; D’Zurilla,
Nezu, & Maydeu-Olivares, 2004; Nezu, 1986) have also been
shown to be helpful in depression and may have positive effects
on rumination. People prone to rumination report more inter-
personal conﬂict, even when they are not currently depressed
(Nolen-Hoeksema & Davis, 1999), and interpersonal conﬂict
may both contribute to and result from rumination. Under-
standing the role of close relationships in their depression,
making changes in unsatisfying relationships, and improving
their social skills may help depressed ruminators to overcome
their interpersonal problems.
The various interventions we have discussed are based on
quite different theories of the causes of depression and target
different problems in depression. Y et studies directly comparing
the efﬁcacy of various types of therapy generally do not ﬁnd
consistent differences among them (see review by Hollon,
Thase, & Markowitz, 2002). Similarly, the few studies that have
examined whether diverse treatments have differential effects
on rumination among depressed people have found that they do
not (Arnow et al., 2004; Schmaling et al., 2002).
An intriguing possibility is that one reason all these inter-
ventions are effective is because all of them provide depressed
ruminators with an explanation for why they are depressed and a
set of steps to overcome their depression. As long as ruminators
believe the explanation the therapist is delivering, they have
answers to ruminative questions about what is wrong with their
lives and a set of strategies for facing the future. Even if the
explanation provided by the therapist is wrong, giving depressed
ruminators a plausible rationale for their depression and the hope
they can overcome it by following the therapist’s prescriptions
V olume 3—Number 5 417
Susan Nolen-Hoeksema, Blair E. Wisco, and Sonja Lyubomirsky

[p.19]

may go a long way in interrupting the depression–rumination–
inaction cycle (Frank, 1973).
CONCLUSIONS AND FUTURE RESEARCH DIRECTIONS
After rethinking the construct of rumination in light of existing
evidence, we conclude that many aspects of the original re-
sponse styles theory have been supported but some of them need
revision. Rumination does predict depressive symptoms and
disorders and does impair thinking, problem solving, instru-
mental behavior, and social relationships. Inducing rumination
prolongs the experience of negative mood in dysphoric indi-
viduals, but self-reported rumination does not reliably predict
duration of episodes of major depression. Similarly, experi-
mental manipulations of distraction have the predicted effects
on mood, but self-report measures of distraction do not. In ad-
dition, new evidence reveals that rumination predicts not only
depression, but anxiety, substance abuse, eating disorders, and
possibly self-harm.
W e have outlined the similarities and differences between
rumination and worry and have suggested that rumination pro-
vides depressed individuals with evidence that their situations
are uncontrollable and that further action is futile; in turn, ru-
mination is reinforced when individuals can avoid aversive
situations and responsibility for action and when it successfully
signals to others that the ruminating individual needs help. W e
have also proposed a model of how rumination relates to other
coping and emotion-regulation constructs. W e see our hypoth-
eses about the avoidant functions of rumination and about how
rumination relates to other coping and emotion-regulation
constructs as important foci for future research.
W e have highlighted some exciting new areas of research that
are shedding light on the cognitive deﬁcits and neural processes
correlated with rumination and on adaptive versus maladaptive
forms of self-reﬂection. Several questions about rumination,
however, remain to be fully answered: What are the develop-
mental antecedents of individual differences in rumination? How
can depressed people avoid falling into rumination when they are
trying to understand their very real problems? What makes it so
difﬁcult to break free of rumination once it has begun? And what
are the most effective strategies for combating rumination in
depressed people? Answering these questions will be critically
important to the development of more effective prevention and
intervention programs for depressive rumination.
Acknowledgments— The authors thank David Barlow, four
anonymous reviewers, and the members of our lab group, par-
ticularly Katie McLaughlin, Frank Farach, and Lori Hilt, for
their insightful suggestions for improvements in this article.
This work was supported by National Institute of Health Grants
R01 MH51817, R01 MH43760, and K02 MH01480.
REFERENCES
Abbott, M.J., & Rapee, R.M. (2004). Post-event rumination and neg-
ative self-appraisal in social phobia before and after treatment.
Journal of Abnormal Psychology , 113, 136–144.
Abela, J.R.Z., Brozina, K., & Haigh, E.P . (2002). An examination of
the response styles theory of depression in third- and seventh-
grade children: A short-term longitudinal study. Journal of Ab-
normal Child Psychology , 30, 515–527.
Abramson, L.Y., Bardone-Cone, A.M., V ohs, K.D., Joiner, T .E., Jr., &
Heatherton, T .F . (2006). Cognitive vulnerability to bulimia. In
L.B. Alloy & J.H. Riskind (Eds.), Cognitive vulnerability to
emotional disorders (pp. 329–364). Mahwah, NJ: Erlbaum.
Alloy, L., Kelly, K., Mineka, S., & Clements, C. (1990). Comorbidity in
anxiety and depressive disorders: A helplessness/hopelessness
perspective. In J.D. Maser & C.R. Cloninger (Eds.), Comorbidity
of mood and anxiety disorders (pp. 3–12). W ashington, DC:
American Psychiatric Association Press.
American Psychiatric Association. (2000). Diagnostic and statistical
manual of mental disorders (4th ed., text rev.). W ashington, DC:
American Psychiatric Association.
Arean, P .A, Perri, M.G., Nezu, A.M., & Schein, R.L. (1993). Com-
parative effectiveness of social problem-solving therapy and
reminiscence therapy as treatments for depression in older
adults. Journal of Consulting and Clinical Psychology , 61, 1003–
1010.
Arnow, B.A., Spangler, D., Klein, D.N., & Burns, D.D. (2004). Ru-
mination and distraction among chronic depressives in treatment:
A structural equation analysis. Cognitive Therapy and Research ,
28, 67–83.
Austenfeld, J.L., & Stanton, A.L. (2004). Coping through emotional
approach: A new look at emotion, coping, and health-related
outcomes. Journal of Personality , 72, 1335–1363.
Aymanns, P ., Filipp, S.H., & Klauer, T . (1995). Family support and
coping with cancer: Some determinants and adaptive correlates.
British Journal of Social Psychology , 34, 107–124.
Bagby, R.M., & Parker, J.D.A. (2001). Relation of rumination and
distraction with neuroticism and extraversion in a sample of
patients with major depression. Cognitive Therapy and Research ,
25, 91–102.
Bagby, R.M., Rector, N.A., Bacchiochi, J.R., & McBride, C. (2004).
The stability of the response styles questionnaire rumination
scale in a sample of patients with major depression. Cognitive
Therapy and Research , 28, 527–538.
Barber, J.P ., & DeRubeis, R.J. (1989). On second thought: Where the
action is in cognitive therapy for depression. Cognitive Therapy
and Research , 13, 441–457.
Barlow, D.H. (1988). Anxiety and its disorders: The nature and treat-
ment of panic . New Y ork: Guilford Press.
Barlow, D.H. (2002). Anxiety and its disorders: The nature and treat-
ment of anxiety and panic (2nd ed.). New Y ork: Guilford.
Beck, A.T . (1967). Depression: Clinical, experimental and theoretical
aspects. New Y ork: Harper & Row.
Beck, A.T ., Rush, A.J., Shaw, B.F ., & Emery, G. (1979). Cognitive
therapy of depression . New Y ork: Guilford.
Beevers, C.G., W enzlaff, R.M., Hayes, A.M., & Scott, W .D. (1999).
Depression and the ironic effects of thought suppression: Ther-
apeutic strategies for improving mental control. Clinical Psy-
chology: Science and Practice , 6, 133–148.
Borkovec, T .D. (1979). Extensions of two-factor theory: Cognitive
avoidance and autonomic perception. In N. Birbaumer & H.D.
418 V olume 3—Number 5
Rethinking Rumination

[p.20]

Kimmel (Eds.), Biofeedback and self-regulation (pp. 139–148).
Hillsdale, NJ: Erlbaum.
Borkovec, T .D., Alcaine, O., & Behar, E. (2004). Avoidance theory of
worry and generalized anxiety disorder. In R.G. Heimberg, C.L.
Turk, & D.S. Mennin (Eds.), Generalized anxiety disorder: Ad-
vances in research and practice (pp. 77–108). New Y ork: Guilford
Press.
Borkovec, T .D., Hazlett-Stevens, H., & Diaz, M.L. (1999). The role of
positive beliefs about worry in generalized anxiety disorder and
its treatment. Clinical Psychology & Psychotherapy , 6, 126–138.
Borkovec, T .D., & Hu, S. (1990). The effect of worry on cardiovascular
response to phobic imagery. Behaviour Research and Therapy, 28,
69–73.
Borkovec, T .D., Lyonﬁelds, J.D., Wiser, S.L., & Deihl, L. (1993). The
role of worrisome thinking in the suppression of cardiovascular
response to phobic imagery. Behaviour Research and Therapy, 31,
321–324.
Borkovec, T .D., Robinson, E., Pruzinsky, T ., & DePree, J.A. (1983).
Preliminary exploration of worry: Some characteristics and pro-
cesses. Behaviour Research & Therapy , 21, 9–16.
Borkovec, T .D., & Roemer, L. (1995). Perceived functions of worry
among generalized anxiety disorder subjects: Distraction from
more emotional topics? Journal of Behavior Therapy and Exper-
imental Psychiatry, 26, 25–30.
Bushman, B.J., Bonacci, A.M., Pedersen, W .C., V asquez, E.A., &
Miller, N. (2005). Chewing on it can chew you up: Effects of
rumination on triggered displaced aggression. Journal of Per-
sonality and Social Psychology , 88, 969–983.
Butler, L.D., & Nolen-Hoeksema, S. (1994). Gender differences in
responses to depressed mood in a college sample. Sex Roles, 30,
331–346.
Campbell-Sills, L., Barlow, D.H., Brown, T .A., & Hoffman, S.G.
(2006). Acceptability and suppression of negative emotion in
anxiety and mood disorders. Emotion, 6, 587–595.
Carver, C.S., & Scheier, M.F . (1998).On the self-regulation of behavior.
New Y ork: Cambridge University Press.
Carver, C.S., Scheier, M.F ., & W eintraub, J.K. (1989). Assessing
coping strategies: A theoretically based approach. Journal of
Personality and Social Psychology , 56, 267–283.
Cavanna, A.E., & Trimble, M.R. (2006). The precuneus: A review of its
functional anatomy and behavioural correlates. Brain: A Journal
of Neurology, 129, 564–583.
Chang, E.C. (2004). Distinguishing between ruminative and distrac-
tive responses in dysphoric college students: Does indication of
past depression make a difference? Personality and Individual
Differences, 36, 845–855.
Ciesla, J.A., & Roberts, J.E. (2002). Self-directed thought and re-
sponse to treatment for depression: A preliminary investigation.
Journal of Cognitive Psychotherapy , 16, 435–453.
Clark, L.A., & W atson, D. (1991). Tripartite model of anxiety and
depression: Psychometric evidence and taxonomic implications.
Journal of Abnormal Psychology , 100, 316–336.
Collins, K., & Bell, R. (1997). Personality and aggression: The Dis-
sipation-Rumination Scale. Personality and Individual Differ-
ences, 22, 751–755.
Conway, M., Csank, P .A.R., Holm, S.L., & Blake, C.K. (2000). On
individual differences in rumination on sadness. Journal of
Personality Assessment , 75, 404–425.
Cooper, M.L., Russell, M., & George, W .H. (1988). Coping, expec-
tancies, and alcohol abuse: A test of social learning formulations.
Journal of Abnormal Psychology , 97, 218–230.
Cooper, M.L., Russell, M., Skinner, J.B., Frone, M.R., & Mudar, P .
(1992). Stress and alcohol use: Moderating effects of gender,
coping, and alcohol expectancies. Journal of Abnormal Psy-
chology, 101, 139–152.
Csikszentmihalyi, M. (1990). Flow: The psychology of optimal experi-
ence. New Y ork: Harper & Row.
Cunningham, W .A., Raye, C.L., & Johnson, M.K. (2004). Implicit and
explicit evaluation: fMRI correlates of valence, emotional in-
tensity, and control in the processing of attitudes. Journal of
Cognitive Neuroscience , 16, 1717–1729.
Cunningham, W .A., Raye, C.L., & Johnson, M.K. (2005). Neural cor-
relates of evaluation associated with promotion and prevention
regulatory focus. Cognitive, Affective, & Behavioral Neuroscience ,
5, 202–211.
Davey, G.C.L. (1994). W orrying, social problem solving abilities, and
problem-solving conﬁdence. Behaviour Research & Therapy , 32,
327–330.
Davidson, R.J., Pizzagalli, D., Nittschke, J.B., & Putnam, K. (2002).
Depression: Perspectives from affective neuroscience. Annual
Review of Psychology , 53, 545–574.
Davis, R.N., & Nolen-Hoeksema, S. (2000). Cognitive inﬂexibility
among ruminators and nonruminators. Cognitive Therapy & Re-
search, 24, 699–711.
Donaldson, C., & Lam, D. (2004). Rumination, mood and social
problem-solving in major depression. Psychological Medicine, 34,
1309–1318.
Donaldson, C., Lam, D., & Mathews, A. (2007). Rumination and at-
tention in major depression. Behaviour Research and Therapy, 45,
2664–2678.
Dugas, M.J., Gagnon, F ., Ladouceur, R., & Freeston, M.H. (1998).
Generalized anxiety disorder: A preliminary test of a conceptual
model. Behaviour Research & Therapy , 36, 215–226.
Duval, S., & Wicklund, R.A. (1972). A theory of objective self aware-
ness. Oxford, England: Academic Press.
D’Zurilla, T .J., Nezu, A.M., & Maydeu-Olivares, A. (2004). Social
problem solving: Theory and assessment. In E.C. Chang, T .J.
D’Zurilla, & L.J. Sanna (Eds.), Social problem solving: Theory,
research, and training (pp. 11–27). W ashington, DC: American
Psychological Association.
Eaton, W .W ., Anthony, J.C., Gallo, J., Cai, G., Tien, A., Romanoski, A.,
et al. (1997). Natural history of Diagnostic Interview
Schedule/DSM-IV major depression: The Baltimore epidemio-
logic catchment area follow-up. Archives of General Psychiatry ,
54, 993–999.
Egan, M.F ., Kojima, M., Callicott, J.H., Goldberg, T .E., Kolachana,
B.S., Bertolino, A., et al. (2003). The BDNF val66met polymor-
phism affects activity-dependent secretion of BDNF and human
memory and hippocampal function. Cell, 112, 257–269.
Ellis, H.C., Thomas, R.L., & Rodriguez, I.A. (1984). Emotional mood
states and memory: Elaborative encoding, semantics processing,
and cognitive effort. Journal of Experimental Psychology:
Learning, Memory, and Cognition , 10, 470–482.
Endler, N.S., & Parker, J.D.A. (1994). Assessment of multidimensional
coping: Task, emotion, and avoidance strategies. Psychological
Assessment, 6, 50–60.
Ferster, C.B. (1973). A functional analysis of depression. American
Psychologist, 28, 857–870.
Flett, G.L., Madorsky, D., Hewitt, P .L., & Heisel, M.J. (2002). Per-
fectionism cognitions, rumination, and psychological distress.
Journal of Rational-Emotive and Cognitive Behavior Therapy , 20,
33–47.
V olume 3—Number 5 419
Susan Nolen-Hoeksema, Blair E. Wisco, and Sonja Lyubomirsky

[p.21]

Folkman, S., & Lazarus, R.S. (1980). An analysis of coping in a
middle-aged community sample. Journal of Health and Social
Behavior, 21, 219–239.
Folkman, S., & Lazarus, R.S. (1986). Stress processes and depressive
symptomatology. Journal of Abnormal Psychology , 95, 107–113.
Frank, J. (1973). Persuasion and healing: A comparative study of
psychotherapy (2nd ed.). Baltimore: Johns Hopkins University
Press.
Frattaroli, J. (2006). Experimental disclosure and its moderators: A
meta-analysis. Psychological Bulletin , 132, 823–865.
Freeston, M.H., Rheaume, J., Letarte, H., Dugas, M.J., & Ladouceur,
R. (1994). Why do people worry? Personality & Individual
Differences, 17, 791–802.
Fresco, D.M., Frankel, A.N., Mennin, D.S., Turk, C.L., & Heimberg,
R.G. (2002). Distinct and overlapping features of rumination and
worry: The relationship of cognitive production to negative
affective states. Cognitive Therapy and Research , 26, 179–188.
Fritz, H.L. (1999). The role of rumination in adjustment to a ﬁrst
coronary event. Dissertation Abstracts International: Section B.
Sciences & Engineering , 60(1-B), 0410.
Giesler, R.B., Josephs, R.A., & Swann, W . (1996). Self-veriﬁcation in
clinical depression: The desire for negative evaluation. Journal of
Abnormal Psychology, 105, 358–368.
Gorski, J., & Y oung, M.A. (2002). Sociotropy/autonomy, self-construal,
response style, and gender in adolescents. Personality and In-
dividual Differences , 32, 463–478.
Grant, K.E., Lyons, A.L., Finkelstein, J.S., Conway, K.M., Reynolds,
L.K., O’Koon, J.H., et al. (2004). Gender differences in rates of
depressive symptoms among low-income, urban, African Amer-
ican youth: A test of two mediational hypotheses. Journal of Y outh
and Adolescence, 33, 523–533.
Greenberg, J., Pyszczynski, T ., Burling, J., & Tibbs, K. (1992). De-
pression, self-focused attention, and the self-serving attributional
bias. Personality and Individual Differences , 13, 959–965.
Gross, J.J. (1998). Antecedent- and response-focused emotion regu-
lation: Divergent consequences for experience, expression, and
physiology. Journal of Personality and Social Psychology , 74,
224–237.
Gross, J.J. (Ed.). (2007). Handbook of emotion regulation . New Y ork:
Guilford.
Gross, J.J., & John, O.P . (2003). Individual differences in two emotion
regulation processes: Implications for affect, relationships, and
well-being. Journal of Personality and Social Psychology , 85,
348–362.
Gross, J.J., & Thompson, R.A. (2007). Emotion regulation: Conceptual
foundations. In J.J. Gross (Ed.), Handbook of emotion regulation
(pp. 3–26). New Y ork: Guilford.
Harrington, J.A., & Blankenship, V . (2002). Ruminative thoughts and
their relation to depression and anxiety. Journal of Applied Social
Psychology, 32, 465–485.
Hayes, S.C., Strosahl, K.D., & Wilson, K.G. (2003). Acceptance and
commitment therapy: An experiential approach to behavior change.
New Y ork: Guilford.
Hayes, S.C., Wilson, K.G., Gifford, E.V ., Follette, V .M., & Strosahl, K.
(1996). Experiential avoidance and behavioral disorders: A
functional dimensional approach to diagnosis and treatment.
Journal of Consulting and Clinical Psychology , 64, 1152–1168.
Hazlett-Stevens, H. (2001, August). Cognitive ﬂexibility deﬁcits in
generalized anxiety disorder . Paper presented at the Annual
Convention of the American Psychological Association, San
Francisco, CA.
Heatherton, T .F ., & Baumeister, R.F . (1991). Binge eating as escape
from self-awareness. Psychological Bulletin , 110, 86–108.
Hertel, P .T . (1998). Relation between rumination and impaired mem-
ory in dysphoric moods. Journal of Abnormal Psychology , 107,
166–172.
Hertel, P .T ., & Gerstle, M. (2003). Depressive deﬁcits in forgetting.
Psychological Science , 14, 573–578.
Hertel, P .T ., & Hardin, T .S. (1990). Remembering with and without
awareness in a depressed mood: Evidence of deﬁcits in initiative.
Journal of Experimental Psychology: General , 119, 45–59.
Hertel, P .T ., & Rude, S.S. (1991). Depressive deﬁcits in memory: Fo-
cusing attention improves subsequent recall. Journal of Experi-
mental Psychology: General , 120, 301–309.
Hilt, L.M., Cha, C.B., & Nolen-Hoeksema, S. (2008). Non-suicidal
self-injury in young adolescent girls: Moderators of the distress-
function relationship. Journal of Consulting and Clinical Psy-
chology, 76, 63–71.
Hilt, L.M., Sander, L.C., Nolen-Hoeksema, S., & Simen, A.A. (2007).
The BDNF V al66Met polymorphism predicts rumination and
depression differently in young adolescent girls and their moth-
ers. Neuroscience Letters , 429, 12–16.
Hoehn-Saric, R., & McLeod, D.R. (1990). The peripheral sympathetic
nervous system: Its role in normal and pathological anxiety.
Psychiatric Clinics of North America , 11, 375–386.
Hoehn-Saric, R., McLeod, D.R, & Zimmerli, W .D. (1989). Somatic
manifestations in women with generalized anxiety disorder. Ar-
chives of General Psychiatry , 46, 1113–1119.
Hollon, S.D., Thase, M.E., & Markowitz, J.C. (2002). Treatment and
prevention of depression. Psychological Science in the Public
Interest, 3, 39–77.
Hong, R.Y. (2007). Differential associations with anxious and de-
pressive symptoms and coping behavior. Behaviour Research and
Therapy, 45, 277–290.
Ingram, R.E. (Ed.). (1990). Contemporary psychological approaches to
depression: Theory, research, and treatment . New Y ork: Plenum
Press.
Ito, T ., & Agari, I. (2002). A prospective study of the relationship
between negative rumination and a depressive state. Japanese
Journal of Counseling Science , 35, 40–46.
Ito, T ., & Agari, I. (2003). The relationship between negative rumi-
nation trait and the Big Five of personality. Japanese Journal of
Counseling Science , 36, 1–9.
Jacobson, N.S., Dobson, K.S., Truax, P .A., Addis, M.E., Koerner, K.,
Gollan, J.K., et al. (1996). A component analysis of cognitive-
behavioral treatment for depression. Journal of Consulting and
Clinical Psychology, 64, 295–304.
Jacobson, N.S., Martell, C.R., & Dimidjian, S. (2001). Behavioral
activation treatment for depression: Returning to contextual
roots. Clinical Psychology: Science and Practice , 8, 255–270.
Johnson, M.K., Nolen-Hoeksema, S., Mitchell, K.J., & Levin, Y.
(2008). Emotional distress, rumination, and medial cortex activity
during self-reﬂection . Manuscript submitted for publication.
Johnson, M.K., Raye, C.L., Mitchell, K.J., Touryan, S.R., Greene, E.J.,
& Nolen-Hoeksema, S. (2006). Dissociating medial frontal and
posterior cingulate activity during self-reﬂection. Social Cogni-
tive and Affective Neuroscience , 1, 56–64.
Joiner, T .E., Jr. (2002). Depression in its interpersonal context. In I.H.
Gotlib & C.L. Hammen (Eds.), Handbook of depression (pp. 295–
313). New Y ork: Guilford Press.
Joormann, J. (2004). Attentional bias in dysphoria: The role of in-
hibitory processes. Cognition and Emotion , 18, 125–147.
420 V olume 3—Number 5
Rethinking Rumination

[p.22]

Joormann, J. (2005). Inhibition, rumination, and mood regulation in
depression. In R.W . Engle, G. Sedek, U. von Hecker, & D.N.
McIntosh (Eds.), Cognitive limitations in aging and psychopa-
thology: Attention, working memory, and executive functions (pp.
275–312). New Y ork: Cambridge University Press.
Joormann, J. (2006). Differential effects of rumination and dysphoria
on the inhibition of irrelevant emotional material: Evidence from
a negative priming task. Cognitive Therapy and Research , 30,
149–160.
Joormann, J., Dkane, M., & Gotlib, I.H. (2006). Adaptive and mal-
adaptive components of rumination? Behavior Therapy, 37, 269–
280.
Joormann, J., & Gotlib, I.H. (2005, November). Inhibitory dysfunction,
rumination, and mood regulation in depression . Paper presented
at the annual meeting of the Association for the Advancement of
Behavior Therapy, W ashington, DC.
Joormann, J., & Siemer, M. (2004). Memory accessibility, mood reg-
ulation, and dysphoria: Difﬁculties in repairing sad mood with
happy memories? Journal of Abnormal Psychology , 113, 179–
188.
Just, N., & Alloy, L.B. (1997). The response styles theory of depres-
sion: Tests and an extension of the theory. Journal of Abnormal
Psychology, 106, 221–229.
Kabat-Zinn, J., Massion, A.O., Kristeller, J., Peterson, L.G., Fletcher,
K.E., Pbert, L., et al. (1992). Effectiveness of a meditation-based
stress reduction program in the treatment of anxiety disorders.
American Journal of Psychiatry , 149, 936–943.
Kasch, K.L., Klein, D.N., & Lara, M.E. (2001). A construct validation
study of the response styles questionnaire rumination scale in
participants with a recent-onset major depressive episode. Psy-
chological Assessment , 13, 375–383.
Kessler, R.C., McGonagle, K.A., Swartz, M., Blazer, D.G., & Nelson,
C.B. (1993). Sex and depression in the National Comorbidity
Survey: I. Lifetime prevalence, chronicity and recurrence. Jour-
nal of Affective Disorders , 29, 85–96.
Klerman, G.L., & W eissman, M.M. (1986). The interpersonal approach
to understanding depression. In T . Millon & G.L. Klerman (Eds.),
Contemporary directions in psychopathology: Toward the DSM-IV
(pp. 429–456). New Y ork: Guilford Press.
Knowles, R., Tai, S., Christensen, I., & Bentall, R. (2005). Coping with
depression and vulnerability to mania: A factor analytic study of
the Nolen-Hoeksema (1991) Response Styles Questionnaire.
British Journal of Clinical Psychology , 44, 99–112.
Kocovski, N.L., Endler, N.S., Rector, N.A., & Flett, G.L. (2005). Ru-
minative coping and post-event processing in social anxiety.
Behaviour Research and Therapy , 43, 971–984.
Kuehner, C., & W eber, I. (1999). Responses to depression in
unipolar depressed patients: An investigation of Nolen-Hoe-
ksema’s response styles theory. Psychological Medicine , 29,
1323–1333.
Kuhl, J. (1981). Motivational and functional helplessness: The mod-
erating effect of state versus action orientation. Journal of Per-
sonality and Social Psychology , 40, 155–170.
Lam, D., Smith, N., Checkley, S., Rijsdijk, F ., & Sham, P . (2003).
Effect of neuroticism, response style and information processing
on depression severity in a clinically depressed sample. Psy-
chological Medicine , 33, 469–479.
Lara, M.E., Klein, D.N., & Kasch, K.L. (2000). Psychosocial predic-
tors of the short-term course and outcome of major depression: A
longitudinal study of a nonclinical sample with recent-onset
episodes. Journal of Abnormal Psychology , 109, 644–650.
Lavender, A., & W atkins, E. (2004). Rumination and future thinking in
depression. British Journal of Clinical Psychology , 43, 129–142.
Lewinsohn, P .M., Antonuccio, D.O., Breckenridge, J.S., & Teri, L.
(1984). The coping with depression course . Eugene, OR: Castalia.
Lewinsohn, P .M., & Graf, M. (1973). Pleasant activities and depres-
sion. Journal of Consulting and Clinical Psychology , 41, 261–
268.
Linehan, M.M., Cochran, B.N., & Kehrer, C.A. (2001). Dialectical
behavior therapy for borderline personality disorder. In D.H.
Barlow (Ed.), Clinical handbook of psychological disorders: A step-
by-step treatment manual (3rd ed., pp. 470–522). New Y ork:
Guilford Press.
Luminet, O. (2004). Measurement of depressive rumination and as-
sociated constructs. In C. Papageorgiou & A. W ells (Eds.), De-
pressive rumination: Nature, theory and treatment (pp. 187–215).
New Y ork: Wiley.
Lyubomirsky, S., Caldwell, N.D., & Nolen-Hoeksema, S. (1998). Ef-
fects of ruminative and distracting responses to depressed mood
on retrieval of autobiographical memories. Journal of Personality
and Social Psychology , 75, 166–177.
Lyubomirsky, S., Boehm, J.K., Kasri, F ., & Zehm, K. (2007). The
cognitive and hedonic costs of unwarranted dwelling . Manuscript
submitted for publication.
Lyubomirsky, S., Kasri, F ., Chang, O., & Chung, I. (2006). Ruminative
response styles and delay of seeking diagnosis for breast cancer
symptoms. Journal of Social and Clinical Psychology , 25, 276–
304.
Lyubomirsky, S., & Nolen-Hoeksema, S. (1993). Self-perpetuating
properties of dysphoric rumination. Journal of Personality and
Social Psychology, 65, 339–349.
Lyubomirsky, S., & Nolen-Hoeksema, S. (1995). Effects of self-focused
rumination on negative thinking and interpersonal problem
solving. Journal of Personality and Social Psychology , 69, 176–
190.
Lyubomirsky, S., & Tkach, C. (2004). The consequences of dysphoric
rumination. In C. Papageorgiou & A. W ells (Eds.), Depressive
rumination: Nature, theory, and treatment (pp. 21–42). New Y ork:
Wiley.
Lyubomirsky, S., Tucker, K.L., Caldwell, N.D., & Berg, K. (1999). Why
ruminators are poor problem solvers: Clues from the phenome-
nology of dysphoric rumination. Journal of Personality and Social
Psychology, 77, 1041–1060.
Macrae, C.N., Moran, J.M., Heatherton, T .F ., Banﬁeld, J.F ., & Kelley,
W .M. (2004). Medial prefrontal activity predicts memory for self.
Cerebral Cortex , 14, 647–654.
Martell, C.R., Addis, M.E., & Jacobson, N.S. (2001). Depression in
context: Strategies for guided action . New Y ork: W .W . Norton.
Martin, L.L., Shrira, I., & Startup, H.M. (2004). In C. Papageorgiou &
A. W ells (Eds.), Depressive rumination: Nature, theory, and
treatment (pp. 153–176). New Y ork: Wiley.
Martin, L.L., & Tesser, A. (1996). Some ruminative thoughts. In R.S.
Wyer Jr. (Ed.), Ruminative thoughts (pp. 1–47). Mahwah, NJ:
Erlbaum.
McCullough, M.E., Bellah, C.G., Kilpatrick, S.D., & Johnson, J.L.
(2001). V engefulness: Relationships with forgiveness, rumina-
tion, well-being, and the Big Five. Personality and Social Psy-
chology Bulletin , 27, 601–610.
McCullough, M.E., Rachal, K.C., Sandage, S.J., W orthington, E.L. Jr.,
Brown, S.W ., & Hight, T .L. (1998). Interpersonal forgiving in
close relationships: II. Theoretical elaboration and measurement.
Journal of Personality and Social Psychology , 75, 1586–1603.
V olume 3—Number 5 421
Susan Nolen-Hoeksema, Blair E. Wisco, and Sonja Lyubomirsky

[p.23]

McFarland, C., & Buehler, R. (1998). The impact of negative affect on
autobiographical memory: The role of self-focused attention to
moods. Journal of Personality and Social Psychology , 75, 1424–
1440.
McLaughlin, K., Borkovec, T .D., & Sibrava, N.J. (2007). The effect of
worry and rumination on affective states and cognitive activity.
Behavior Therapy, 38, 23–38.
McLaughlin, K., Sibrava, N., Behar, E., & Borkovec, T .D. (2006).
Recurrent negative thinking in emotional disorders: W orry, de-
pressive rumination, and trauma recall. In S. Sassaroli, G. Rug-
gerio, & R. Lorenzini (Eds.), Worry, need of control, and other core
cognitive constructs in anxiety and eating disorders (pp. 37–67).
Milan, Italy: Raphael Cortina.
Mennin, D.S., & Farach, F .J. (2007). Emotion and evolving treatments
for adult psychopathology. Clinical Psychology: Science and
Practice, 14, 329–352.
Miller, J.J., Fletcher, K., & Kabat-Zinn, J. (1995). Three-year follow-
up and clinical implications of a mindfulness meditation-based
stress reduction intervention in the treatment of anxiety disor-
ders. General Hospital Psychiatry , 17, 192–200.
Mineka, S., W atson, D., & Clark, L.A. (1998). Comorbidity of anxiety
and unipolar mood disorders. Annual Review of Psychology , 49,
377–412.
Miranda, R., & Nolen-Hoeksema, S. (2007). Brooding and reﬂection:
Rumination predicts suicidality at one-year follow up in a com-
munity sample. Behavior Research and Therapy , 45, 3088–3095.
Moos, R.H., & Billings, A.G. (1982). Conceptualizing and measuring
coping resources and processes. In L. Goldberger & S. Breznitz
(Eds.), Handbook of stress: Theoretical and clinical aspects (pp.
212–230). New Y ork: Free Press.
Mor, N., & Winquist, J. (2002). Self-focused attention and negative
affect: A meta-analysis. Psychological Bulletin , 128, 638–662.
Morrow, J., & Nolen-Hoeksema, S. (1990). Effects of responses to
depression on the remediation of depressive affect. Journal of
Personality and Social Psychology , 58, 519–527.
Moulds, M.L., Kandris, E., Starr, S., & W ong, A.C.M. (2007). The
relationship between rumination, avoidance and depression in a
non-clinical sample. Behaviour Research and Therapy , 45, 251–
261.
Muris, P ., Roelofs, J., Meesters, C., & Boomsma, P . (2004). Rumination
and worry in nonclinical adolescents. Cognitive Therapy and
Research, 28, 539–554.
Muris, P ., Roelofs, J., Rassin, E., Franken, I., & Mayer, B. (2005).
Mediating effects of rumination and worry on the links between
neuroticism, anxiety, and depression. Personality and Individual
Differences, 39, 1105–1111.
Nesse, R.M. (2000). Is depression an adaptation? Archives of General
Psychiatry, 57, 14–20.
Nezu, A.M. (1986). Efﬁcacy of a social problem-solving therapy ap-
proach for unipolar depression. Journal of Consulting and Clin-
ical Psychology, 54, 196–202.
Niederhoffer, K.G., & Pennebaker, J.W . (2002). Sharing one’s story: On
the beneﬁts of writing or talking about emotional experience. In
C.R. Snyder & S.J. Lopez (Eds.), Handbook of positive psychology
(pp. 573–583). New Y ork: Oxford University Press.
Nock, M.K., & Prinstein, M.J. (2004). A functional approach to the
assessment of self-mutilative behavior. Journal of Consulting and
Clinical Psychology, 72, 885–890.
Nolan, S.A., Roberts, J.E., & Gotlib, I.H. (1998). Neuroticism and
ruminative response style as predictors of change in depressive
symptomatology. Cognitive Therapy and Research , 22, 445–455.
Nolen-Hoeksema, S. (1987). Sex differences in unipolar depression:
Evidence and theory. Psychological Bulletin , 101, 259–282.
Nolen-Hoeksema, S. (1991). Responses to depression and their effects
on the duration of depressive episodes. Journal of Abnormal
Psychology, 100, 569–582.
Nolen-Hoeksema, S. (2000). The role of rumination in depressive
disorders and mixed anxiety/depressive symptoms. Journal of
Abnormal Psychology, 109, 504–511.
Nolen-Hoeksema, S. (2004). The response styles theory. In C. Papa-
georgiou & A. W ells (Eds.),Depressive rumination: Nature, theory,
and treatment (pp. 107–124). New Y ork: Wiley.
Nolen-Hoeksema, S., & Davis, C.G. (1999). ‘‘Thanks for sharing that’’:
Ruminators and their social support networks. J ournal of Per-
sonality and Social Psychology , 77, 801–814.
Nolen-Hoeksema, S., & Harrell, Z.A. (2002). Rumination, depression,
and alcohol use: Tests of gender differences. Journal of Cognitive
Psychotherapy, 16, 391–403.
Nolen-Hoeksema, S., & Jackson, B. (2001). Mediators of the gender
difference in rumination. Psychology of Women Quarterly, 25, 37–
47.
Nolen-Hoeksema, S., & Jacobs, R. (2007). Adaptive and maladaptive
forms of rumination and self-reﬂection: Tests of different theories .
Unpublished manuscript.
Nolen-Hoeksema, S., & Larson, J. (1999). Coping with loss . Mahwah,
NJ: Erlbaum.
Nolen-Hoeksema, S., Larson, J., & Grayson, C. (1999). Explaining the
gender difference in depressive symptoms. Journal of Personality
and Social Psychology , 77, 1061–1072.
Nolen-Hoeksema, S., & Morrow, J. (1991). A prospective study of
depression and posttraumatic stress symptoms after a natural
disaster: The 1989 Loma Prieta earthquake. Journal of Person-
ality and Social Psychology , 61, 115–121.
Nolen-Hoeksema, S., & Morrow, J. (1993). Effects of rumination and
distraction on naturally occurring depressed mood. Cognition
and Emotion , 7, 561–570.
Nolen-Hoeksema, S., Morrow, J., & Fredrickson, B.L. (1993). Re-
sponse styles and the duration of episodes of depressed mood.
Journal of Abnormal Psychology , 102, 20–28.
Nolen-Hoeksema, S., Parker, L., & Larson, J. (1994). Ruminative
coping with depressed mood following loss. Journal of Personality
and Social Psychology , 67, 92–104.
Nolen-Hoeksema, S., Stice, E., W ade, E., & Bohon, C. (2007). Re-
ciprocal relations between rumination and bulimic, substance
abuse ad depressive symptoms in female adolescents. Journal of
Abnormal Psychology, 116, 198–207.
Ochsner, K.N., Beer, J.S., Robertson, E.R., Cooper, J.C., Gabrielli,
J.D., Kihlstrom, J., et al. (2005). The neural correlates of direct
and reﬂected self-knowledge. NeuroImage, 28, 797–814.
Papageorgiou, C., & W ells, A. (2001). Metacognitive beliefs about
rumination in recurrent major depression. Cognitive and Behav-
ioral Practice , 8, 160–164.
Papageorgiou, C., & W ells, A. (2003). An empirical test of a clinical
metacognitive model of rumination and depression. Cognitive
Therapy and Research , 27, 261–273.
Papageorgiou, C., & W ells, A. (Eds.). (2004). Depressive rumination:
Nature, theory, and treatment . New Y ork: Wiley.
Park, R.J., Goodyer, I.M., & Teasdale, J.D. (2004). Effects of induced
rumination and distraction on mood and overgeneral autobio-
graphical memory in adolescent major depressive disorder and
controls. Journal of Child Psychology and Psychiatry , 45, 996–
1006.
422 V olume 3—Number 5
Rethinking Rumination

[p.24]

Pennebaker, J.W . (1989). Confession, inhibition and disease. In L.
Berkowitz (Ed.), Advances in experimental social psychology (V ol.
22, pp. 211–244). San Diego, CA: Academic Press.
Pennebaker, J.W ., & O’Heeron, R.C. (1984). Conﬁding in others and
illness rate among spouses of suicide and accident-related vic-
tims. Journal of Abnormal Psychology , 93, 473–476.
Persons, J.B., & Miranda, J. (1995). The search for mode-speciﬁc ef-
fects of cognitive and other therapies: A methodological sug-
gestion. Psychotherapy Research , 5, 102–112.
Pyszczynski, T ., & Greenberg, J. (1987). Self-regulatory perseveration
and the depressive self-focusing style: A self-awareness theory
of reactive depression. Psychological Bulletin , 102, 122–138.
Pyszczynski, T ., Hamilton, J.C., Herring, F .H., & Greenberg, J. (1989).
Depression, self-focused attention, and the negative memory
bias. Journal of Personality and Social Psychology , 57, 351–357.
Pyszczynski, T ., Holt, K., & Greenberg, J. (1987). Depression, self-
focused attention, and expectancies for positive and negative
future life events for self and others. Journal of Personality and
Social Psychology, 52, 994–1001.
Raes, F ., Hermans, D., & Eelen, P . (2003). The Dutch version of the
Ruminative Response Scale (RRS-NL) and the Rumination on
Sadness Scale (RSS-NL). Gedragstherapie, 36, 97–104.
Ray, R.D., Ochsner, K.N., Cooper, J.C., Robertson, E.R., Gabrielli,
J.D.E., & Gross, J.J. (2005). Individual differences in trait ru-
mination and the neural systems supporting cognitive reap-
praisal. Cognitive, Affective, and Behavioral Neuroscience, 5, 156–
168.
Reeves, A.L., W atson, P .J., Ramsey, A., & Morris, R.J. (1995).
Private self-consciousness factors, need for cognition, and
depression. Journal of Social Behavior and Personality , 10,
431–443.
Rimes, K.A., & W atkins, E. (2005). The effects of self-focused rumi-
nation on global negative self-judgments in depression. Behavi-
our Research and Therapy , 43, 1673–1681.
Roberts, J.E., Gilboa, E., & Gotlib, I.H. (1998). Ruminative response
style and vulnerability to episodes of dysphoria: Gender, neu-
roticism, and episode duration. Cognitive Therapy and Research ,
22, 401–423.
Robinson, L.A., & Alloy, L.B. (2003). Negative cognitive styles
and stress-reactive rumination i nteract to predict depression:
A prospective study. Cognitive Therapy and Research , 27, 275–
292.
Roemer, L., Salters-Pedneault, K., & Orsillo, S.M. (2006). Incorpo-
rating mindfulness- and acceptance-based strategies in the
treatment of generalized anxiety disorder. In R.A. Baer (Ed.),
Mindfulness-based treatment approaches: Clinician’s guide to ev-
idence base and applications (pp. 51–74). San Diego, CA: Elsevier
Academic Press.
Sakamoto, S., Kambara, M., & Tanno, Y. (2001). Response styles and
cognitive and affective symptoms of depression. Personality and
Individual Differences , 31, 1053–1065.
Sanfey, A.G., Rilling, J.K., Aronson, J.A., Nystrom, L.E., & Cohen,
J.D. (2003). The neural basis of economic decision-making in the
Ultimatum Game. Science, 300, 1755–1758.
Sarin, S., Abela, J.R.Z., & Auerbach, R.P . (2005). The response styles
theory of depression: A test of speciﬁcity and causal mediation.
Cognition & Emotion , 19, 751–761.
Schmaling, K.B., Dimidjian, S., Katon, W ., & Sullivan, M. (2002).
Response styles among patients with minor depression and dys-
thymia in primary care. Journal of Abnormal Psychology , 111,
350–356.
Schwartz, J.A.J., & Koenig, L.J. (1996). Response styles and negative
affect among adolescents. Cognitive Therapy and Research , 20,
13–36.
Schwartz, J.L., & McCombs, T .A. (1995). Perceptions of coping re-
sponses exhibited in depressed males and females. Journal of
Social Behavior and Personality , 10, 849–860.
Segal, A., Williams, J.M.G., & Teasdale, J.D. (2002). Mindfulness-
based cognitive therapy for depression: A new approach to pre-
venting relapse . New Y ork: Guilford.
Segerstrom, S.C., Stanton, A.L., Alden, L.E., & Shortridge, B.E.
(2003). A multidimensional structure for repetitive thought:
What’s on your mind, and how much? Journal of Personality and
Social Psychology, 85, 909–921.
Segerstrom, S.C., Tsao, J.C.I., Alden, L.E., & Craske, M.G. (2000).
W orry and rumination: Repetitive thought as a concomitant and
predictor of negative mood. Cognitive Therapy and Research , 24,
671–688.
Siegle, G.J., Ingram, R.E., & Matt, G.E. (2002). Affective interference:
An explanation for negative attention biases in dysphoria. Cog-
nitive Therapy and Research , 26, 73–87.
Siegle, G.J., Moore, P .M., & Thase, M.E. (2004). Rumination: One
construct, many features in healthy individuals, depressed indi-
viduals, and individuals with lupus. Cognitive Therapy and Re-
search, 28, 645–668.
Siegle, G.J., Steinhauer, S.R., Thase, M.E., Stenger, V .A., & Carter,
C.S. (2002). Can’t shake that feeling: Event-related fMRI as-
sessment of sustained amygdala activity in response to emotional
information in depressed individuals. Biological Psychiatry, 51,
693–707.
Skinner, E.A., Edge, K., Altman, J., & Sherwood, H. (2003). Searching
for the structure of coping: A review and critique of category
systems for classifying ways of coping. Psychological Bulletin ,
129, 216–269.
Smith, J.M., Alloy, L.B., & Abramson, L.Y. (2006). Cognitive vulner-
ability to depression, rumination, hopelessness, and suicidal
ideation: Multiple pathways to self-injurious thinking. Suicide
and Life-Threatening Behavior , 36, 443–454.
Spasojevic, J., & Alloy, L.B. (2001). Rumination as a common
mechanism relating depressive risk to depression. Emotion, 1,
25–37.
Stanton, A.L., Danoff-Burg, S., Cameron, C.L., & Ellis, A.P . (1994).
Coping through emotional approach: Problems of conceptual-
ization and confounding. Journal of Personality and Social Psy-
chology, 66, 350–362.
Stanton, A.L., Kirk, S.B., Cameron, C.L., & Danoff-Burg, S. (2000).
Coping through emotional approach: Scale construction and
validation. Journal of Personality and Social Psychology , 78,
1150–1169.
Stice, E. (2002). Risk and mainte nance factors for eating pathol-
ogy: A meta-analytic review. Psychological Bulletin , 128, 825–
848.
Sto¨ ber, J. (1996). Anxiety and the regulation of complex problem sit-
uations: playing it safe? In W . Battmann & S. Dutke (Eds.),
Processes and the molar regulation of behavior (pp. 105–118).
Scottsdale, AZ: Pabst.
Strack, S., Blaney, P .H., Ganellen, R.J., & Coyne, J.C. (1985).
Pessimistic self-preoccupation, performance deﬁcits, and de-
pression. Journal of Personality and Social Psychology , 49,
1076–1085.
Strauss, J., Barr, C.L., George, N., King, S., Shaikh, S., Devlin, B.,
et al. (2004). Association study of brain-derived neurotrophic
V olume 3—Number 5 423
Susan Nolen-Hoeksema, Blair E. Wisco, and Sonja Lyubomirsky

[p.25]

factor in adults with a history of childhood onset mood disorder.
American Journal of Medical Genetics: Part B. Neuropsychiatric
Genetics, 131B, 16–19.
Swann, W .B., Jr. (1990). To be known or to be adored: The interplay of
self-enhancement and self-veriﬁcation. In E.T . Higgins & R.M.
Sorrentino (Eds.), Handbook of motivation and cognition (V ol. 2,
408–444). New Y ork: Guilford Press.
Swann, W .B., Jr, Grifﬁn, J.J., Predmore, S., & Gaines, B. (1987). The
cognitive-affective crossﬁre: When self-consistency confronts
self-enhancement. Journal of Personality and Social Psychology ,
52, 881–889.
Swann, W .B., Jr., & Read, S.J. (1981a). Acquiring self-knowledge: The
search for feedback that ﬁts. Journal of Personality and Social
Psychology, 41, 1119–1128.
Swann, W .B., Jr., & Read, S.J. (1981b). Self-veriﬁcation processes:
How we sustain our self-concepts. Journal of Experimental Social
Psychology, 17, 351–372.
Swann, W .B., Jr., W enzlaff, R.M., Krull, D.S., & Pelham, B.W . (1992).
Allure of negative feedback: Self-veriﬁcation strivings among
depressed persons. Journal of Abnormal Psychology , 101, 293–
305.
Swann, W .B., Jr., W enzlaff, R.M., & Tafarodi, R.W . (1992). Depression
and the search for negative evaluations: More evidence of the role
of self-veriﬁcation strivings. Journal of Abnormal Psychology ,
101, 314–317.
Swinkels, A., & Giuliano, T .A. (1995). The measurement and con-
ceptualization of mood awareness: Monitoring and labeling one’s
mood states. Personality and Social Psychology Bulletin , 21,
934–949.
Teasdale, J.D. (1985). Psychophysiological treatments for depression:
How do they work? Behaviour Research and Therapy , 23, 157–
165.
Teasdale, J.D., & Green, H.A.C. (2004). Ruminative self-focus and
autobiographical memory. Personality and Individual Differences,
36, 1933–1943.
Teasdale, J.D., Segal, Z., & Williams, J.M.G. (1995). How does cog-
nitive therapy prevent depressive relapse and why should at-
tentional control (mindfulness) training help? Behaviour Research
and Therapy, 33, 25–39.
Teasdale, J.D., Segal, Z., Williams, J.M.G., Ridgeway, J.A., Sousby,
J.M., & Lau, M.A. (2000). Prevention of relapse/recurrence in
major depression by mindfulness-based cognitive therapy. Jour-
nal of Consulting and Clinical Psychology , 68, 615–623.
Thase, M.E., Jindal, R., & Howland, R.H. (2002). Biological aspects of
depression. In I.H. Gotlib & C.L. Hammen (Eds.), Handbook of
depression (pp. 192–218). New Y ork: Guilford Press.
Trapnell, P .D., & Campbell, J.D. (1999). Private self-consciousness
and the ﬁve-factor model of personality: Distinguishing rumina-
tion from reﬂection. Journal of Personality and Social Psychol-
ogy, 76, 284–304.
Treynor, W ., Gonzalez, R., & Nolen-Hoeksema, S. (2003). Rumination
reconsidered: A psychometric analysis. Cognitive Therapy and
Research, 27, 247–259.
V ogt, B.A., & Laureys, S. (2005). Posterior cingulate, precuneal and
retrosplenial cortices: Cytology and components of the neural
network correlates of consciousness. Progress in Brain Research ,
150, 205–217.
W ard, A., Lyubomirsky, S., Sousa, L., & Nolen-Hoeksema, S. (2003).
Can’t quite commit: Rumination and uncertainty.Personality and
Social Psychology Bulletin , 29, 96–107.
W atkins, E. (2004). Appraisals and strategies associated with rumi-
nation and worry. Personality and Individual Differences , 37,
679–694.
W atkins, E. (2008). Constructive and unconstructive repetitive thought.
Psychological Bulletin , 134, 163–206.
W atkins, E., & Baracaia, S. (2002). Rumination and social problem-
solving in depression. Behaviour Research and Therapy , 40,
1179–1189.
W atkins, E., & Brown, R.G. (2002). Rumination and executive func-
tion in depression: An experimental study. Journal of Neurology,
Neurosurgery, and Psychiatry, 72, 400–402.
W atkins, E., & Moulds, M. (2005). Distinct modes of ruminative self-
focus: Impact of abstract versus concrete rumination on problem
solving in depression. Emotion, 5, 319–328.
W atkins, E., Moulds, M., & Mackintosh, B. (2005). Comparisons be-
tween rumination and worry in a non-clinical population. Be-
haviour Research and Therapy , 43, 1577–1585.
W atkins, E.R., Scott, J., Wingrove, J., Rimes, K.A., Bathurst, N.,
Steiner, H., et al. (2007). Rumination-focused cognitive behavi-
our therapy for residual depression: A case series. Behaviour
Research and Therapy , 45, 2144–2154.
W atkins, E., & Teasdale, J.D. (2001). Rumination and overgeneral
memory in depression: Effects of self-focus and analytic thinking.
Journal of Abnormal Psychology , 110, 353–357.
W atkins, E., Teasdale, J.D., & Williams, R.M. (2000). Decentering and
distraction reduce overgeneral autobiographical memory in de-
pression. Psychological Medicine , 30, 911–920.
W atson, P .J., & Andrews, P .W . (2002). Toward a revised evolutionary
adaptionist analysis of depression: The social navigation hy-
pothesis. Journal of Affective Disorders , 72, 1–14.
W eissman, M.M., & Markowitz, J.C. (2002). Interpersonal psycho-
therapy for depression. In I.H. Gotlib & C.L. Hammen (Eds.),
Handbook of depression (pp. 404–421). New Y ork: Guilford Press.
W egner, D.M. (1994). Ironic processes of mental control.Psychological
Review, 101, 34–52.
W egner, D.M., & W enzlaff, R.M. (1996). Mental control. In E.T . Hig-
gins & A.W . Kruglanski (Eds.), Social psychology: Handbook of
basic principles (pp. 466–492). New Y ork: Guildford Press.
W enzlaff, R.M., & Luxton, D.D. (2003). The role of thought suppres-
sion in depressive rumination. Cognitive Therapy and Research ,
22, 293–308.
W enzlaff, R.M., W egner, D.M., & Roper, D.W . (1988). Depression and
mental control: The resurgence of unwanted negative thoughts.
Journal of Personality and Social Psychology , 55, 882–892.
Whitmer, A.J., & Banich, M.T . (2007). Inhibition versus switching
deﬁcits in different forms of rumination. Psychological Science ,
18, 546–553.
W ood, J.V ., Saltzberg, J.A., Neale, J.M., Stone, A.A., & Rachmiel, T .B.
(1990). Self-focused attention, coping responses, and distressed
mood in everyday life. Journal of Personality and Social Psy-
chology, 58, 1027–1036.
Ziegert, D.I., & Kistner, J.A. (2002). Response styles theory: Down-
ward extension to children. Journal of Clinical Child and Ado-
lescent Psychology, 31, 325–334.
424 V olume 3—Number 5
Rethinking Rumination
