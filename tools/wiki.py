#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
wiki.py -- LLM Wiki 零依赖工具链

只使用 Python 标准库，无需 pip install。

  python3 tools/wiki.py init [path]        初始化一个新的知识库
  python3 tools/wiki.py lint               健康检查：断链、孤岛、缺 frontmatter
  python3 tools/wiki.py stats              统计页面数、链接数、枢纽页
  python3 tools/wiki.py search "<query>"   BM25 全文检索（支持中文二字组）
  python3 tools/wiki.py index              从 frontmatter 重建 wiki/index.md
  python3 tools/wiki.py build              生成单文件浏览站点 site/index.html
                                           （同时写 site/.build-manifest.json 作为构建基准）
  python3 tools/wiki.py buildcheck         对比构建基准，报「新建 / 更新」页数
                                           （供 schema §2.1 判据 3 判断要不要构建）
  python3 tools/wiki.py chapter-audit [-v] source 页的「正文 / 账目」分布审计（只读）
  python3 tools/wiki.py log <type> "msg"   追加一条日志
  python3 tools/wiki.py new <type> <slug>  按模板新建页面
                                           type: project | source | entity | concept | analysis
  python3 tools/wiki.py graph              打印链接关系
"""

import json
import math
import os
import re
import sys
import hashlib
from collections import Counter, defaultdict
from datetime import date

# 标签准入规则（见 wiki/schema.md §1.7）。缺失时降级为「不检查标签」，不让工具链挂掉。
try:
    from tags_vocab import REMOVE
except ImportError:  # pragma: no cover
    REMOVE = frozenset()

# ---------------------------------------------------------------- 常量

PAGE_DIRS = {
    "source": "sources",
    "entity": "entities",
    "concept": "concepts",
    "analysis": "analyses",
    "project": "projects",
}

TYPE_LABEL = {
    "source": "素材摘要",
    "entity": "实体",
    "concept": "概念",
    "analysis": "分析",
    "project": "项目",
    "meta": "系统",
}

# 项目的进展状态。注意与 frontmatter 的 status（页面健康度）是**两个维度**：
#   status 回答「这页还新鲜吗」（active / draft / stale / deprecated）
#   stage  回答「这件事做到哪了」（planning / active / paused / shipped / abandoned）
PROJECT_STAGES = ("planning", "active", "paused", "shipped", "abandoned")
STAGE_LABEL = {
    "planning": "筹划",
    "active": "进行中",
    "paused": "暂停",
    "shipped": "已交付",
    "abandoned": "已放弃",
}

# ------------------------------------------------------- source 页的「正文 / 账目」
#
# 一页 source 的自然形状是三段：上款（标题·提要·出处卡）→ 正文 → 账目。
# 「账目」是**为维护者写的**那一半（分层表、引注核查表、回填清单、定级理由……）。
# 实测 127 页 source 里账目章节占全部章节的 **47%** —— 读者要找「这份素材讲了什么」，
# 得先翻过等量的记账。站点侧因此给账目一个可折叠的边界（默认收起，文字一个不删）。
#
# 这三张表是**唯一真源**：`build` 把它们注入渲染器（见 cmd_build），
# `chapter-audit` 直接读它们。**不要在 JS 里另抄一份** ——
# [[conventions]] 的原话：「同一件事有两个版本，早晚会互相矛盾」。
#
# 「来源」「相关页面」只做**精确**匹配：当子串用会误伤
# 「术语归属专段：…三个心法名的**来源**要分开说」。
# 判定顺序 = 精确名 → 正文字串 → 账目子串 → **默认正文**。
# 默认正文是故意的：误折一个正文章节（读者会以为库里没这段）
# 比漏折一个账目章节（多划一屏）代价大得多。
READ_EXACT = ["来源", "相关页面"]
READ_H2 = [
    # 「TL;DR」已于 2026-09-20 并入「关键要点」并全库取消（见 schema §1.8）。
    # 故意不留在表里：兜底默认就是 read，删掉它行为不变，
    # 但将来若有人重新引入该章节名，--audit 会把它报进「走兜底」清单。
    "关键要点", "要点", "摘要", "段摘要", "逐节摘要", "逐段摘要",
    "与本库", "与现有", "与既有", "与库内", "与其他页面", "与素材",
    "待办", "开放问题", "新出现的实体", "适用边界", "派生页",
]
LEDGER_H2 = [
    "分层表", "素材分层", "引注", "数字与引注", "数字清单", "回填", "新建 / 回填",
    "归属", "定级理由", "定级变更", "定级的理由", "证据性质", "证据层级",
    "confidence", "置信度", "仍然收录的原因",
    "AI 加工", "AI 段", "AI 生成", "核查", "核对", "校准", "回指", "核实",
    "素材基本信息", "版本与捕获", "版本与获取", "抓取", "已知缺失", "已知缺陷",
    "行号坐标系", "关键行号", "映射表", "对照表", "讲次总表", "内嵌资源",
    "token 对照", "附段", "文档后段", "定语：", "校验", "台账",
    "采集质量", "权威性", "分段（", "结构（", "取舍", "记账", "性质判定", "同源判定",
]


def classify_h2(title):
    """章节属正文还是账目。与渲染器里的 classifyH2 同口径。"""
    t = re.sub(r"<[^>]+>", "", str(title)).strip()
    if t in READ_EXACT:
        return "read"
    if any(k in t for k in READ_H2):
        return "read"
    if any(k in t for k in LEDGER_H2):
        return "ledger"
    return "read"


# 章节同义异名。**只用于审计报表，不用于批量改名** ——
# 本库有 330 处页内指向引用（见下 / 见上 / 上表 / 「见下『素材基本信息』」），
# 改名会让指名引用指空。所以这里只把「哪些页用了哪个名字」摆出来给人看，
# 改不改由人决定。
SECTION_FAMILIES = [
    ("关系", ["与本库既有页面的关系", "与现有知识库的关系", "与现有库的关系",
              "与其他页面的关系", "与既有页面的关系", "与本库的关系", "与库内既有页面的关系"]),
    ("要点", ["关键要点", "要点"]),
    ("待办", ["待办 / 开放问题", "待办", "开放问题"]),
    ("分层表", ["素材分层表", "分层表"]),
    ("核查表", ["引注核查表", "数字与引注核查表", "引注与内容核查", "回填清单"]),
]

META_FILES = {"index", "log", "overview", "conventions"}

REQUIRED_FM = ["title", "type", "slug"]

# 证据层级（2026-09-19 引入）—— 回答「这页的结论站得多稳」，与 confidence 是两个维度：
#   confidence  是 LLM 的**主观**判断（high / medium / low），会随阅读而变，无法机器校验
#   evidence_tier 是**可计算**的事实：由支撑素材的数量与类型推导，lint 能校验它与事实是否一致
# 三档取值：
#   single   恰好 1 份素材支撑 —— 孤证。可读，但引用时必须带着「只有一份来源」这个前提
#   crossed  ≥2 份素材支撑，且不含一手文献 —— 交叉了，但可能只是同源转述（见同源提示）
#   primary  至少 1 份 kind=paper 的素材支撑 —— 有可独立核验的一手文献
EVIDENCE_TIERS = ("single", "crossed", "primary")

# 被视为「可独立核验的一手文献」的素材 kind
PRIMARY_KINDS = ("paper",)

# 需要证据层级的页面类型。source 页本身就是一份素材，不适用；
# project / meta 不由素材派生，也不适用。
EVIDENCE_TYPES = ("concept", "entity", "analysis")

LINK_RE = re.compile(r"\[\[([^\[\]|]+)(?:\|([^\[\]]+))?\]\]")

# 正文链接密度（2026-09-19 引入）—— 回答「这页是在论述，还是在罗列」。
# `related` 字段是结构化挂靠，正文内链才是论述过程中真正发生的引用。一页很长却几乎
# 不在正文里引用别的页，通常是「清单式挂靠」：页面被挂进了知识网，但没有参与论证。
# 阈值 1.5 不是理论值，是实测出来的：素材页密度中位数从 09-18 批次的 1.68 掉到
# 09-19 批次的 1.08（低于 1.5 的占比 40% → 83%），1.5 正好落在两个批次之间。
BODY_LINK_DENSITY_MIN = 1.5     # 条 / 千字正文
BODY_LINK_MIN_CHARS = 1000      # 短页密度波动大，不参与该项检查

# ---------------------------------------------------------------- 基础工具


def find_root(start=None):
    """向上查找知识库根目录（含 AGENTS.md 或 wiki/ 的目录）。"""
    cur = os.path.abspath(start or os.getcwd())
    while True:
        if os.path.isfile(os.path.join(cur, "AGENTS.md")) or os.path.isdir(
            os.path.join(cur, "wiki")
        ):
            return cur
        parent = os.path.dirname(cur)
        if parent == cur:
            return os.path.abspath(start or os.getcwd())
        cur = parent


def _unquote(s):
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in ("'", '"'):
        return s[1:-1]
    return s


def _scalar(s):
    s = _unquote(s)
    if s.startswith("[") and s.endswith("]"):
        inner = s[1:-1].strip()
        if not inner:
            return []
        return [_unquote(p) for p in inner.split(",") if p.strip()]
    if s.lower() in ("true", "false"):
        return s.lower() == "true"
    return s


def parse_frontmatter(text):
    """极简 YAML frontmatter 解析，返回 (dict, body)。"""
    if not text.startswith("---"):
        return {}, text
    lines = text.split("\n")
    if lines[0].strip() != "---":
        return {}, text
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return {}, text

    data = {}
    key = None
    for raw in lines[1:end]:
        if not raw.strip() or raw.strip().startswith("#"):
            continue
        stripped = raw.strip()
        if stripped.startswith("- ") and key:
            if not isinstance(data.get(key), list):
                data[key] = []
            data[key].append(_scalar(stripped[2:]))
            continue
        if ":" in stripped:
            k, _, v = stripped.partition(":")
            k = k.strip()
            v = v.strip()
            key = k
            data[k] = [] if v == "" else _scalar(v)
    body = "\n".join(lines[end + 1:])
    return data, body


class Page(object):
    __slots__ = ("path", "relpath", "fm", "body", "slug", "title", "type",
                 "links", "body_links")

    def __init__(self, path, relpath, fm, body):
        self.path = path
        self.relpath = relpath
        self.fm = fm
        self.body = body
        self.slug = fm.get("slug") or os.path.splitext(os.path.basename(path))[0]
        self.title = fm.get("title") or self.slug
        self.type = fm.get("type") or ("meta" if self.slug in META_FILES else "concept")
        # 提取链接前先剥掉代码块与行内代码 —— 文档里的示例（`[[x]]`）不是真链接
        scan = re.sub(r"```[\s\S]*?```", "", body)
        scan = re.sub(r"`[^`\n]*`", "", scan)
        self.body_links = []
        for m in LINK_RE.finditer(scan):
            target = m.group(1).strip()
            if target:
                self.body_links.append(target)
        # 出链 = 正文内链 + frontmatter 的 related。
        # 两者要分开记：related 是结构化挂靠，正文内链才是论述中真发生的引用，
        # 密度检查（BODY_LINK_DENSITY_MIN）只认后者。
        self.links = list(self.body_links)
        for r in self.fm.get("related") or []:
            if isinstance(r, str) and r.strip():
                self.links.append(r.strip())

    @property
    def tags(self):
        t = self.fm.get("tags") or []
        return t if isinstance(t, list) else [t]

    @property
    def sources(self):
        s = self.fm.get("sources") or []
        return s if isinstance(s, list) else [s]

    @property
    def status(self):
        return self.fm.get("status") or "active"

    @property
    def stage(self):
        """项目进展状态。非项目页返回空串。"""
        if self.type != "project":
            return ""
        s = self.fm.get("stage") or "planning"
        return s if s in PROJECT_STAGES else "planning"

    @property
    def goal(self):
        """项目的一句话目标（可验收）。"""
        return (self.fm.get("goal") or "").strip()

    @property
    def summary(self):
        """取正文第一段非标题非引用的文字，作为一行摘要。"""
        for block in self.body.split("\n\n"):
            b = block.strip()
            if not b or b.startswith("#") or b.startswith("---"):
                continue
            if b.startswith(">"):
                b = re.sub(r"^>\s?", "", b, flags=re.M).strip()
                # 去掉 callout 标记。摘要是一行文字，`[!warning]` 这种结构标记
                # 在这里只会变成噪声 —— index 里曾出现「— [!warning] 2026-09-18 同日推翻」。
                b = re.sub(r"^\[![A-Za-z]+\][+-]?\s*", "", b).strip()
                if b:
                    return _clip(b, 90)
                continue
            b = LINK_RE.sub(lambda m: (m.group(2) or m.group(1)), b)
            b = re.sub(r"[*`_]", "", b).replace("\n", " ").strip()
            if b:
                return _clip(b, 90)
        return ""


def _clip(s, n):
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= n else s[: n - 1] + "…"


def load_pages(root):
    wiki = os.path.join(root, "wiki")
    pages = []
    if not os.path.isdir(wiki):
        return pages
    for dirpath, dirnames, filenames in os.walk(wiki):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for fn in sorted(filenames):
            if not fn.endswith(".md"):
                continue
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, root)
            with open(full, "r", encoding="utf-8") as fh:
                text = fh.read()
            fm, body = parse_frontmatter(text)
            pages.append(Page(full, rel, fm, body))
    pages.sort(key=lambda p: (p.type, p.slug))
    return pages


def write_text(path, text):
    d = os.path.dirname(path)
    if d and not os.path.isdir(d):
        os.makedirs(d)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


# ---------------------------------------------------------------- 证据层级


def load_raw_meta(root):
    """扫描 raw/*.md，返回 {slug: {"kind":..., "author":...}}。

    只取 frontmatter 的两个字段 —— 判证据层级只需要素材的**类型**与**作者**。
    重抓版（-r2/-r3）沿用基础 slug 的元数据：它们抓的是同一份素材。
    """
    meta = {}
    raw_dir = os.path.join(root, "raw")
    if not os.path.isdir(raw_dir):
        return meta
    base = {}
    for fn in sorted(os.listdir(raw_dir)):
        if not fn.endswith(".md"):
            continue
        slug = fn[:-3]
        with open(os.path.join(raw_dir, fn), "r", encoding="utf-8") as fh:
            text = fh.read()
        fm, _ = parse_frontmatter(text)
        rec = {
            "kind": (fm.get("kind") or "").strip(),
            "author": (fm.get("author") or "").strip(),
        }
        meta[slug] = rec
        b = re.sub(r"-r\d+$", "", slug)
        if b not in base:
            base[b] = rec
    for slug, rec in list(meta.items()):
        b = re.sub(r"-r\d+$", "", slug)
        if b != slug and b in base:
            meta[slug] = base[b]
    return meta


# 来源族归并规则：(关键词元组, 族名)。命中任一关键词即归入该族。
# 本库 2026-09-19 的现实：约 60/97 份素材来自同一套得到课程，但它们的 author 字段
# 写法五花八门（「万维钢（讲稿）…」「未署名 —— 飞书 wiki…正文为得到课程文章」
# 「得到《现代思维工具课》问答…」）。若只按 author 字符串比较，会把同源拆成三族，
# 于是「交叉验证」会被严重高估。这条规则表的存在就是为了不让这件事发生。
FAMILY_RULES = (
    (("万维钢", "得到", "dedao", "dedao.cn"), "wanweigang-dedao"),
)


# 未署名素材里，「真正的作者」常常藏在分号之后的说明里：
#   「未署名 —— 飞书 wiki 文档未标注整理者；书籍内容为斯坦尼斯拉斯·迪昂原著」
# 这类素材若只按整理者归并，会把迪昂的书和格兰特的书并成一族 —— 那是**假阳性**，
# 会把真正的交叉验证误判成同源。所以必须把原著作者挖出来。
ORIGINAL_AUTHOR_RE = re.compile(r"(?:书籍内容|书中正文|正文|内容)?为?([^；;，,]{2,20}?)(?:原著|所著|著)")


def source_family(author, kind, slug=""):
    """把一份素材归到一个「来源族」。同一族内的多份素材不构成独立交叉验证。

    归并失败时的默认策略是「各自独立」而不是「并成一族」—— 判不了就别判。
    因为把真交叉误判成同源（冤枉一个其实站得住的页面）比漏报同源的代价更大。
    """
    blob = (author or "") + " " + (kind or "")
    for keys, name in FAMILY_RULES:
        for k in keys:
            if k in blob:
                return name
    a = (author or "").strip()
    if a.startswith("未署名") or "未标注" in a:
        m = ORIGINAL_AUTHOR_RE.search(a)
        if m:
            return "未署名整理 · 原著：%s" % m.group(1).strip()
        # 挖不出原著 —— 不并族，各自独立，避免把不同作者的书混为一谈
        return "未署名整理（原著不明）· %s" % (slug or a[:12])
    a = re.sub(r"（[^）]*）|\([^)]*\)", "", a).strip()
    a = re.split(r"[；;。]", a)[0].strip(" —-")
    return a or "(未署名)"


def compute_evidence_tier(page, raw_meta):
    """计算一个知识页的证据层级，返回 (tier, 支撑素材数, 来源族集合)。

    判据全部来自可计算的事实，不含主观判断 —— 这样 lint 才能校验它。
    page 的 sources 里可能有重复与非素材项，这里都做了处理。
    """
    srcs = []
    for s in page.sources:
        if not s or s in srcs:
            continue
        srcs.append(s)
    if not srcs:
        return ("none", 0, set())
    families = set()
    has_primary = False
    for s in srcs:
        rec = raw_meta.get(s, {})
        if rec.get("kind") in PRIMARY_KINDS:
            has_primary = True
        families.add(source_family(rec.get("author", ""), rec.get("kind", ""), s))
    if has_primary:
        return ("primary", len(srcs), families)
    return (("single" if len(srcs) == 1 else "crossed"), len(srcs), families)


# ---------------------------------------------------------------- lint


def gap_table_rows(body):
    """返回「当前缺口」表里的数据行数。找不到该节、或表已清空时返回 0。

    这是「项目是否做到终点」的机器判据 —— 缺口表清空 = shipped（wiki/schema.md §1.6）。
    注意判的是**表里还有没有数据行**，不是「有没有【阻塞】标记」：
    一条缺口都没标【阻塞】，只能说明没做优先级排序，不能说明项目做完了。
    """
    m = re.search(r"^##\s*当前缺口\s*$(.*?)(?=^##\s|\Z)", body, re.M | re.S)
    if not m:
        return 0
    rows = 0
    for line in m.group(1).splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        if re.match(r"^\|[\s:\-|]+\|$", s):   # 分隔行 |---|---|
            continue
        if "缺口" in s and "卡在哪" in s:      # 表头行
            continue
        rows += 1
    return rows


def cmd_lint(root):
    pages = load_pages(root)
    if not pages:
        print("wiki/ 下没有找到任何页面。")
        return 0

    by_slug = {}
    dupes = []
    for p in pages:
        if p.slug in by_slug:
            dupes.append((p.slug, by_slug[p.slug].relpath, p.relpath))
        else:
            by_slug[p.slug] = p

    inbound = defaultdict(list)
    broken = []
    for p in pages:
        for t in set(p.links):
            if t in by_slug:
                inbound[t].append(p.slug)
            else:
                broken.append((p.slug, t))

    problems = 0

    def section(title, items):
        nonlocal problems
        if not items:
            return
        problems += len(items)
        print("\n" + title + "  (%d)" % len(items))
        for it in items:
            print("  - " + it)

    print("=" * 62)
    print("LLM Wiki 体检报告  |  根目录: %s" % root)
    print("=" * 62)
    # 与 build / stats 用同一口径：只计「目标存在且非自指」的链接。
    # 旧口径 sum(len(set(p.links))) 会把自指链接与断链也算进去，
    # 于是 lint 与 build 报出的「链接总数」长期不一致（差 17，即 16 个 source 页的自指 + 1）。
    valid_links = sum(len({t for t in p.links if t in by_slug and t != p.slug}) for p in pages)
    self_links = sum(1 for p in pages if p.slug in set(p.links))
    print("页面总数: %d   链接总数: %d（自指链接 %d 条已剔除）"
          % (len(pages), valid_links, self_links))

    section("重复 slug", ["%s  →  %s 与 %s" % (s, a, b) for s, a, b in dupes])
    section("断链（指向不存在的页面）",
            ["%s  →  [[%s]]" % (src, tgt) for src, tgt in broken])

    no_fm = []
    slug_mismatch = []
    for p in pages:
        miss = [k for k in REQUIRED_FM if not p.fm.get(k)]
        if miss:
            no_fm.append("%s  缺少 %s" % (p.relpath, ", ".join(miss)))
        stem = os.path.splitext(os.path.basename(p.path))[0]
        if p.fm.get("slug") and p.fm["slug"] != stem:
            slug_mismatch.append("%s  slug=%s 与文件名不一致" % (p.relpath, p.fm["slug"]))
    section("frontmatter 缺字段", no_fm)
    section("slug 与文件名不一致", slug_mismatch)

    # 孤岛：忽略 index.md 的入链（index 链接一切，否则永远没有孤岛）
    orphans = []
    for p in pages:
        if p.type == "meta":
            continue
        srcs = [s for s in inbound.get(p.slug, []) if s != "index"]
        if not srcs:
            orphans.append("%s" % p.relpath)
    section("孤岛页（除 index.md 外无入链）", orphans)

    no_out = []
    for p in pages:
        if p.type in ("meta", "source"):
            continue
        if not [t for t in p.links if t in by_slug and t != p.slug]:
            no_out.append(p.relpath)
    section("无出链页", no_out)

    no_src = []
    for p in pages:
        # 项目页豁免：项目由「目标」派生，不是由素材派生。
        # 它的来源是人的意图，没有 raw/ 素材可指。
        if p.type in ("meta", "project"):
            continue
        if not p.sources:
            no_src.append("%s" % p.relpath)
    section("未标注来源的页面", no_src)

    # ---- 证据层级（2026-09-19 引入）----
    # confidence 是主观的、lint 校验不了；evidence_tier 是从素材推导的事实，能校验。
    # 所以这里不只查「有没有写」，还查「写的是不是和素材对得上」—— 否则字段会腐烂。
    raw_meta = load_raw_meta(root)
    tier_missing = []
    tier_mismatch = []
    for p in pages:
        if p.type not in EVIDENCE_TYPES:
            continue
        t, n, _fams = compute_evidence_tier(p, raw_meta)
        if t == "none":          # 没有支撑素材的页由上一条「未标注来源」管，不重复报
            continue
        declared = (p.fm.get("evidence_tier") or "").strip()
        if not declared:
            tier_missing.append("%s  缺 evidence_tier（按素材推算应为 %s，%d 份支撑）"
                                % (p.relpath, t, n))
        elif declared != t:
            tier_mismatch.append("%s  声明 %s，但按素材推算是 %s（%d 份支撑）"
                                 % (p.relpath, declared, t, n))
    section("知识页缺少 evidence_tier", tier_missing)
    section("evidence_tier 与支撑素材不符", tier_mismatch)

    # 标签准入 —— 规则见 wiki/schema.md §1.7，移除集见 tools/tags_vocab.py。
    # 这条只拦一件事：**「这页自己是什么」不该做标签**（素材形态 / 核查状态 / 生成方式 / 抓取元数据）。
    # 它**不**拦「主题词多而杂」—— 那是导航的自然结果，不是错误；也不再校验频次门槛。
    if REMOVE:
        bad_tags = []
        for p in pages:
            for t in p.tags:
                if t in REMOVE:
                    bad_tags.append("%s  标签「%s」属于移除集（素材形态 / 核查状态 / 生成方式 / 抓取元数据）"
                                    % (p.relpath, t))
        section("标签属于移除集", bad_tags)

    # ---- 项目层检查 ----
    projects = [p for p in pages if p.type == "project"]
    knowledge = [p for p in pages
                 if p.type in ("source", "entity", "concept", "analysis")]

    empty_goals = []
    bad_stage = []
    for p in projects:
        if not p.goal:
            empty_goals.append("%s  缺少可验收的 goal" % p.relpath)
        if p.fm.get("stage") and p.fm["stage"] not in PROJECT_STAGES:
            bad_stage.append("%s  stage=%s（可选 %s）"
                             % (p.relpath, p.fm["stage"], " / ".join(PROJECT_STAGES)))
    section("项目页缺少 goal", empty_goals)
    section("项目页 stage 取值非法", bad_stage)

    # 项目页必须出链到知识页 —— 否则是一个没有知识支撑的空壳
    hollow = []
    for p in projects:
        if not [t for t in p.links if t in by_slug
                and by_slug[t].type in ("entity", "concept", "analysis")]:
            hollow.append("%s  未链接任何知识页（实体/概念/分析）" % p.relpath)
    section("空壳项目（未链接任何知识页）", hollow)

    # 项目生命周期：缺口表清空 = shipped（wiki/schema.md §1.6）
    # 已 shipped 却还留着缺口 —— 说明它其实没做完，是假 shipped
    fake_shipped = []
    for p in projects:
        n = gap_table_rows(p.body)
        if p.stage == "shipped" and n > 0:
            fake_shipped.append(
                "%s  已 shipped，但「当前缺口」表仍有 %d 行（缺口清空才是 shipped 的判据；"
                "决定不做的条目应移入「不做什么」）" % (p.relpath, n))
    section("已 shipped 但缺口表未清空", fake_shipped)

    # ---- 语义提示（不计入问题数）----
    advisories = []
    if projects:
        covered = set()
        for p in projects:
            for t in p.links:
                if t in by_slug and by_slug[t].type in ("entity", "concept", "analysis"):
                    covered.add(t)
        uncovered = sorted(p.slug for p in knowledge
                           if p.type != "source" and p.slug not in covered)
        if uncovered:
            advisories.append(
                "以下 %d 个知识页未被任何项目引用 —— 按「项目是过滤器」的约定，"
                "它们要么该挂到某个项目下，要么该考虑是否值得继续维护：" % len(uncovered))
            for s in uncovered[:12]:
                advisories.append("    %s" % s)
            if len(uncovered) > 12:
                advisories.append("    …… 另有 %d 个" % (len(uncovered) - 12))
        # 「名义交叉，实质同源」—— 有多份支撑素材，但全来自同一来源族。
        # 这类页面最容易骗人：sources 字段看着有三四份，其实是一个人的转述被拆成了几份。
        same_family = []
        for p in pages:
            if p.type not in EVIDENCE_TYPES:
                continue
            t, n, fams = compute_evidence_tier(p, raw_meta)
            if t == "crossed" and len(fams) == 1:
                same_family.append((p.slug, n, next(iter(fams))))
        if same_family:
            advisories.append(
                "以下 %d 个页面有 ≥2 份支撑素材，但**全部来自同一来源族** —— 名义上交叉验证，"
                "实质是同源转述的重复计数，引用时不能当作独立佐证：" % len(same_family))
            for s, n, f in sorted(same_family)[:10]:
                advisories.append("    %-36s %d 份，全部来自 %s" % (s, n, f))
            if len(same_family) > 10:
                advisories.append("    …… 另有 %d 个" % (len(same_family) - 10))
        # 正文链接密度过低 —— 文章很长，却几乎不在正文里引用别的页。
        # 典型成因是批量建页时的「清单式挂靠」：related 字段写满了，正文里一句没提。
        # 这类页面进了知识网却没参与论证，链接总数上看不出来，只能按密度查。
        thin = []
        for p in pages:
            # meta 页是目录 / 规范 / 日志，它们的链接本就是罗列，不适用密度判据
            if p.type == "meta" or len(p.body) < BODY_LINK_MIN_CHARS:
                continue
            n = len({t for t in p.body_links if t in by_slug and t != p.slug})
            d = n / (len(p.body) / 1000.0)
            if d < BODY_LINK_DENSITY_MIN:
                thin.append((d, p.slug, len(p.body), n))
        if thin:
            thin.sort()
            advisories.append(
                "以下 %d 个页面正文链接密度 < %s 条/千字 —— 文章很长却几乎不在正文里引用其他页，"
                "通常是「清单式挂靠」（只写进 `related` 字段）而不是论述性引用，"
                "页面进了知识网但没有参与论证："
                % (len(thin), BODY_LINK_DENSITY_MIN))
            for d, s, nc, n in thin[:12]:
                advisories.append("    %-46s %.2f 条/千字（%s 字，%d 条）"
                                  % (s, d, format(nc, ","), n))
            if len(thin) > 12:
                advisories.append("    …… 另有 %d 个" % (len(thin) - 12))
        # 缺口表已清空但项目还开着 —— 按 wiki/schema.md §1.6，可以收尾了
        for p in sorted(projects, key=lambda x: x.slug):
            if p.stage in ("planning", "active") and gap_table_rows(p.body) == 0:
                advisories.append(
                    "%s  「当前缺口」表已清空 —— 按 wiki/schema.md §1.6，该项目可标 `stage: shipped`"
                    % p.relpath)
    elif len(knowledge) >= 10:
        advisories.append(
            "本库有 %d 个知识页但**没有任何项目页**。按 [[cybernetic-learning]] 的推论，"
            "没有目标就没有过滤器 —— 建议用 `new project <slug>` 建一个。" % len(knowledge))
    # HFQ（人类先问）检查已于 2026-09-18 移除 —— 北洛裁定：全面移除该前置条件，后续不再要求。
    # 原实现：检查 source 页是否有 `## 人类先问` 节、且节内不含「待人类亲笔」占位。
    # 保留这段注释作为历史痕迹；不要因为看到注释就恢复检查。

    if advisories:
        print("\n语义提示（不计入问题数）")
        for a in advisories:
            print("  " + a if a.startswith("    ") else "  - " + a)

    # raw 素材是否已收录
    raw_dir = os.path.join(root, "raw")
    raw_files = []
    if os.path.isdir(raw_dir):
        for fn in sorted(os.listdir(raw_dir)):
            if fn.endswith(".md"):
                raw_files.append(os.path.splitext(fn)[0])
    ingested = set()
    for p in pages:
        if p.type == "source":
            ingested.add(p.slug)
        for s in p.sources:
            ingested.add(s)
    pending = []
    for r in raw_files:
        # 重抓版（-r2 / -r3 ...）由基础素材页覆盖，不算未收录
        base = re.sub(r"-r\d+$", "", r)
        if base in ingested or base in by_slug or r in ingested or r in by_slug:
            continue
        pending.append(r)
    section("raw/ 中尚未收录的素材", pending)

    stale = [p.relpath for p in pages if p.status in ("stale", "deprecated")]
    if stale:
        print("\n标记为 stale / deprecated 的页面  (%d)" % len(stale))
        for s in stale:
            print("  - " + s)

    # 枢纽页
    print("\n枢纽页 Top 5（按入链数）")
    hubs = sorted(((len([s for s in v if s != "index"]), k) for k, v in inbound.items()),
                  reverse=True)[:5]
    for n, slug in hubs:
        if n:
            print("  - %-34s %d 条入链" % (slug, n))

    print("\n" + "-" * 62)
    if problems:
        print("机器可查问题合计: %d 项。语义问题（矛盾 / 过期 / 该建未建）请 LLM 继续人工核查。" % problems)
    else:
        print("机器可查问题: 0 项。建议继续人工核查语义层面（矛盾、过期、该建未建）。")
    return problems


# ---------------------------------------------------------------- stats


def cmd_stats(root):
    pages = load_pages(root)
    by_slug = {p.slug: p for p in pages}
    inbound = Counter()
    outbound = Counter()
    for p in pages:
        for t in set(p.links):
            if t in by_slug and t != p.slug:
                inbound[t] += 1
                outbound[p.slug] += 1

    print("=" * 62)
    print("LLM Wiki 统计  |  %s" % root)
    print("=" * 62)
    counts = Counter(p.type for p in pages)
    for t in ["project", "source", "entity", "concept", "analysis", "meta"]:
        if counts.get(t):
            print("  %-10s %-6s %d" % (t, TYPE_LABEL.get(t, ""), counts[t]))
    print("  %-10s %-6s %d" % ("合计", "", len(pages)))
    edges = sum(outbound.values())
    print("\n有效链接: %d 条（平均每页 %.1f 条出链）"
          % (edges, edges / len(pages) if pages else 0))
    raw_dir = os.path.join(root, "raw")
    n_raw = len([f for f in os.listdir(raw_dir) if f.endswith(".md")]) if os.path.isdir(raw_dir) else 0
    print("raw 素材: %d 份" % n_raw)
    words = sum(len(p.body) for p in pages)
    print("wiki 正文总字符: %d" % words)
    tags = Counter(t for p in pages for t in p.tags)
    if tags:
        print("\n高频标签: " + ", ".join("%s(%d)" % (t, c) for t, c in tags.most_common(8)))

    # 证据层级分布 —— 这是「库有多完备」的机器口径，比页面总数有意义得多
    raw_meta = load_raw_meta(root)
    tiers = Counter()
    fam_only = 0
    for p in pages:
        if p.type not in EVIDENCE_TYPES:
            continue
        t, _n, fams = compute_evidence_tier(p, raw_meta)
        if t == "none":
            continue
        tiers[t] += 1
        if t == "crossed" and len(fams) == 1:
            fam_only += 1
    if tiers:
        total = sum(tiers.values())
        print("\n证据层级（知识页 %d 个）" % total)
        for t in ("primary", "crossed", "single"):
            if tiers.get(t):
                print("  %-10s %3d  (%.0f%%)" % (t, tiers[t], 100.0 * tiers[t] / total))
        if fam_only:
            print("  其中 %d 个 crossed 页的全部支撑素材来自同一来源族 —— 名义交叉，实质同源"
                  % fam_only)

    projects = [p for p in pages if p.type == "project"]
    if projects:
        print("\n项目（按阶段）")
        order = {s: i for i, s in enumerate(PROJECT_STAGES)}
        for p in sorted(projects, key=lambda x: (order.get(x.stage, 9), x.slug)):
            print("  - [%-4s] %-28s %s"
                  % (STAGE_LABEL.get(p.stage, p.stage), p.slug, _clip(p.goal, 46) or "（未写目标）"))

    print("\n枢纽页 Top 5:")
    for slug, n in inbound.most_common(5):
        print("  - %-34s %d" % (slug, n))
    return 0


# ---------------------------------------------------------------- search (BM25)

CJK_RE = re.compile(r"[\u4e00-\u9fff]+")
WORD_RE = re.compile(r"[a-z0-9_]+")


def tokenize(text):
    text = text.lower()
    toks = WORD_RE.findall(text)
    for m in CJK_RE.finditer(text):
        s = m.group()
        if len(s) == 1:
            toks.append(s)
        else:
            for i in range(len(s) - 1):
                toks.append(s[i:i + 2])
    return toks


def cmd_search(root, query, top=10, type_filter=None):
    pages = load_pages(root)
    if type_filter:
        pages = [p for p in pages if p.type == type_filter]
    docs = []
    for p in pages:
        head = " ".join([str(p.title), " ".join(p.tags), p.slug])
        text = (head + " ") * 3 + p.body
        docs.append(tokenize(text))
    if not docs:
        print("没有可检索的页面。")
        return 0

    q = tokenize(query)
    if not q:
        print("查询为空。")
        return 0

    N = len(docs)
    avgdl = sum(len(d) for d in docs) / N
    df = Counter()
    for d in docs:
        for t in set(d):
            df[t] += 1

    k1, b = 1.5, 0.75
    scored = []
    for i, d in enumerate(docs):
        tf = Counter(d)
        dl = len(d)
        s = 0.0
        for t in q:
            if t not in tf:
                continue
            idf = math.log(1 + (N - df[t] + 0.5) / (df[t] + 0.5))
            s += idf * (tf[t] * (k1 + 1)) / (tf[t] + k1 * (1 - b + b * dl / avgdl))
        if s > 0:
            scored.append((s, pages[i]))
    scored.sort(key=lambda x: -x[0])

    if not scored:
        print("没有匹配结果：%s" % query)
        return 0

    print("搜索: %s   （%d 条结果）\n" % (query, len(scored[:top])))
    for s, p in scored[:top]:
        print("%-40s  %5.2f  [%s]" % (p.relpath, s, TYPE_LABEL.get(p.type, p.type)))
        print("    %s" % p.title)
        if p.summary:
            print("    %s" % p.summary)
        print("")
    return 0


# ---------------------------------------------------------------- index


def cmd_index(root):
    pages = load_pages(root)
    groups = defaultdict(list)
    for p in pages:
        if p.type == "meta":
            continue
        groups[p.type].append(p)

    today = date.today().isoformat()
    out = []
    out.append("---")
    out.append("title: 索引")
    out.append("type: meta")
    out.append("slug: index")
    out.append("created: %s" % today)
    out.append("updated: %s" % today)
    out.append("status: active")
    out.append("---")
    out.append("")
    out.append("# 索引")
    out.append("")
    out.append("> 本文件由 `python3 tools/wiki.py index` 从各页 frontmatter 自动生成。")
    out.append("> 每次 ingest 后重新生成。查询时先读本页定位候选页面，再深入阅读。")
    out.append("")
    total = sum(len(v) for v in groups.values())
    n_proj = len(groups.get("project", []))
    n_active = len([p for p in groups.get("project", []) if p.stage in ("planning", "active")])
    # 口径说明：本行的「页面总数」**不含 meta 页**（wiki/ 根下的 index / log / overview /
    # conventions / schema / decisions 等系统文件），而 `lint` 与 `build` 报的页面数**含 meta**。
    # 两者恒差 meta 页数 —— 该数由下方 n_meta 动态算出，**不要在这里写死**（曾写死「4」，随
    # 2026-09-19 新增 schema / decisions 而失效），不是 index 滞后。
    # 2026-09-18 巡检时曾把这两个数当成同一个口径，误判「index 停在 140 页、落后 10 页」，
    # 实际 140 = 144 − 4，index 一直是准的。故在此显式标注，避免重复踩坑。
    n_meta = len([p for p in pages if p.type == "meta"])
    out.append("页面总数 **%d**（不含 %d 个系统页；`lint` 报的数含它们） ｜ 项目 **%d**（进行中 %d） ｜ raw 素材 **%d** 份 / 摘要页 **%d** 份 ｜ 最后更新 %s"
               % (total, n_meta, n_proj, n_active,
                  len([f for f in os.listdir(os.path.join(root, "raw"))
                       if f.endswith(".md")]) if os.path.isdir(os.path.join(root, "raw")) else 0,
                  len(groups.get("source", [])),
                  date.today().isoformat()))
    out.append("")

    # 项目排在最先 —— 它是本库的入口，决定什么素材值得收
    projs = sorted(groups.get("project", []),
                   key=lambda p: (PROJECT_STAGES.index(p.stage) if p.stage in PROJECT_STAGES else 9,
                                  p.slug))
    if projs:
        out.append("## 项目 (%d)" % len(projs))
        out.append("")
        out.append("> 入口层。**收录素材前先读这里** —— 判断这份素材服务于哪个项目、填哪个缺口。")
        out.append("")
        for p in projs:
            stage = STAGE_LABEL.get(p.stage, p.stage)
            goal = p.goal or "（未写目标）"
            out.append("- [[%s|%s]] `%s` — %s" % (p.slug, p.title, stage, goal))
        out.append("")

    for t in ["source", "entity", "concept", "analysis"]:
        items = sorted(groups.get(t, []), key=lambda p: p.slug)
        if not items:
            continue
        out.append("## %s (%d)" % (TYPE_LABEL[t], len(items)))
        out.append("")
        for p in items:
            tags = ("  `" + "` `".join(p.tags) + "`") if p.tags else ""
            flag = ""
            if p.status in ("stale", "deprecated"):
                flag = " ⚠️" + p.status
            out.append("- [[%s|%s]] — %s%s%s" % (p.slug, p.title, p.summary, tags, flag))
        out.append("")

    # 系统页导航。**从 meta 页动态生成**，不再硬编码 —— 曾因硬编码而在新增
    # schema / decisions 两页后静默漏掉它们（2026-09-19）。
    # 本表只提供「说明文字」与「排序」；未登记的 meta 页会以自身摘要兜底，排在其后。
    meta_nav = {
        "overview": "这个知识库在讲什么",
        "log": "按时间记录的所有操作",
        "schema": "页面规范与工作流（按需读）",
        "decisions": "每条规则为什么这么定（按需读）",
        "conventions": "人类的偏好设置",
    }
    meta_order = {s: i for i, s in enumerate(meta_nav)}
    metas = [p for p in pages if p.type == "meta" and p.slug != "index"]
    metas.sort(key=lambda p: (meta_order.get(p.slug, 99), p.slug))
    out.append("## 系统页")
    out.append("")
    for p in metas:
        desc = meta_nav.get(p.slug) or p.summary or ""
        out.append("- [[%s|%s]]%s" % (p.slug, p.title, (" — " + desc) if desc else ""))
    out.append("")

    path = os.path.join(root, "wiki", "index.md")
    write_text(path, "\n".join(out))
    print("已重建 %s（%d 个页面）" % (os.path.relpath(path, root), total))
    return 0


# ---------------------------------------------------------------- log


def cmd_log(root, kind, message):
    path = os.path.join(root, "wiki", "log.md")
    today = date.today().isoformat()
    entry = "## [%s] %s | %s\n\n" % (today, kind, message)
    if not os.path.isfile(path):
        header = (
            "---\n"
            "title: 日志\n"
            "type: meta\n"
            "slug: log\n"
            "created: %s\n"
            "updated: %s\n"
            "status: active\n"
            "---\n\n"
            "# 日志\n\n"
            "> 只追加，不改写。格式固定，便于 `grep \"^## \\[\" wiki/log.md | tail -5`。\n\n"
        ) % (today, today)
        write_text(path, header + entry)
    else:
        with open(path, "a", encoding="utf-8") as fh:
            fh.write(entry)
    print("已记录: %s" % entry.strip())
    return 0


# ---------------------------------------------------------------- new


def cmd_new(root, ptype, slug, title=None):
    if ptype not in PAGE_DIRS:
        print("未知页面类型: %s（可选 %s）" % (ptype, " / ".join(PAGE_DIRS)))
        return 1
    tpl_path = os.path.join(root, "templates", "%s.md" % ptype)
    if os.path.isfile(tpl_path):
        with open(tpl_path, "r", encoding="utf-8") as fh:
            tpl = fh.read()
    elif ptype in TEMPLATES:
        tpl = TEMPLATES[ptype]
    else:
        print("缺少模板 %s" % tpl_path)
        return 1
    today = date.today().isoformat()
    text = (tpl.replace("{{TITLE}}", title or slug)
               .replace("{{SLUG}}", slug)
               .replace("{{DATE}}", today))
    path = os.path.join(root, "wiki", PAGE_DIRS[ptype], "%s.md" % slug)
    if os.path.exists(path):
        print("已存在，未覆盖: %s" % os.path.relpath(path, root))
        return 1
    write_text(path, text)
    print("已创建 %s" % os.path.relpath(path, root))
    return 0


# ---------------------------------------------------------------- graph


def cmd_graph(root):
    pages = load_pages(root)
    by_slug = {p.slug: p for p in pages}
    inbound = Counter()
    print("链接关系（→ 表示指向）\n")
    for p in sorted(pages, key=lambda x: x.slug):
        targets = sorted({t for t in p.links if t in by_slug and t != p.slug})
        for t in targets:
            inbound[t] += 1
        print("%-34s → %s" % (p.slug, ", ".join(targets) if targets else "(无)"))
    print("\n入链排行:")
    for slug, n in inbound.most_common(10):
        print("  %-34s %d" % (slug, n))
    return 0


# ---------------------------------------------------------------- init


INIT_AGENTS = """# AGENTS.md -- LLM Wiki 维护手册（Schema 层）

> **必读总纲。** 任何 LLM Agent 进入本仓库后，先读本文件，再动手。
> 细则**按需读**：规则在 `wiki/schema.md`，人类裁定史在 `wiki/decisions.md`，人类偏好在 `wiki/conventions.md`。
>
> **本文件必须薄。** 它每次会话都进上下文 —— 写在里面的每一行，都在每一次任务里被付费。
> 因此这里只放**任何任务都要遵守的东西**；只在特定动作时才需要的细则，一律写进 `wiki/schema.md`。

## 三层架构

| 层 | 位置 | 谁写 | 谁读 |
|---|---|---|---|
| 原始素材 | `raw/` | 人类 | LLM（只读，不可变） |
| 知识库 | `wiki/` | LLM | 人类 |
| 规范 | 本文件 + `wiki/schema.md` + `wiki/decisions.md` + `wiki/conventions.md` | 共同演进 | LLM |

## 目录

- `projects/` 项目页：**入口层** —— 我在做什么、因此什么重要
- `sources/` 素材摘要页，一份素材一页
- `entities/` 实体页：人物、组织、工具、产品
- `concepts/` 概念页：理论、方法、模式、术语
- `analyses/` 分析页：对比、综述、回答归档

## 硬约束

**这一节是「任何任务都要遵守」的部分，不可省略。** 违反其中任何一条，产物即失效。

1. `raw/` **不可变** —— 不修改、不重命名、不删除。需要修正时在 `wiki/` 里写「原文如此，但应理解为 X」。
2. `[[link]]` 只能指向**已存在**的页面；每页至少 1 条出链、1 条入链。
3. 没有来源的断言必须显式标注「（未验证）」，并降 `confidence`。
4. 新素材与旧结论冲突时，必须**显式标注矛盾**，不得静默覆盖。
5. **收录前先读 `projects/` 的缺口表** —— 填不上任何缺口的素材，**现在还不该收**。
6. **一份素材通常触及 10-15 个页面。只写摘要页是失败的做法。**
7. 说「**库里没有 X**」之前，必须先在库内检索，并写明**检索了哪几段**。
8. `sources` 字段必须指向**真正包含该内容**的素材，不允许悬空引用。
9. **每次改动后**：`index` → `lint`。

## 指路

| 我要做什么 | 读哪里 |
|---|---|
| 建 / 改一个页面 | `wiki/schema.md` |
| 收录一份素材 | `wiki/schema.md` |
| 查询并归档答案 | `wiki/schema.md` |
| 体检 | `wiki/schema.md` |
| 追问「这条规则为什么这么定」 | `wiki/decisions.md` |
| 人类希望我怎么回答 | `wiki/conventions.md` |

## 工具链

```bash
python3 tools/wiki.py lint | stats | search "<q>" | index | build | log | new | graph
```
"""


INIT_SCHEMA = """# 维护细则

> **规则层**：页面怎么写、素材怎么收、答案怎么归档、体检查什么。
> 必读总纲是 `AGENTS.md`；本页**按需读**。「为什么这么定」记在 `wiki/decisions.md`。

## 页面类型

| type | 目录 | 一页是什么 |
|---|---|---|
| `project` | `projects/` | 我在做的一件事：目标、当前缺口、消耗的知识、产出 |
| `source` | `sources/` | 一份素材的结构化摘要 |
| `entity` | `entities/` | 一个具体的人 / 组织 / 工具 / 产品 |
| `concept` | `concepts/` | 一个抽象的理论 / 方法 / 模式 / 术语 |
| `analysis` | `analyses/` | 一次对比 / 综述 / 回答归档 |
| `meta` | `wiki/` 根 | index / log / overview / schema / decisions / conventions |

**判定规则**：能被指着一张照片说「这是它」的 → entity；只能被描述、不能被拍照的 → concept。
**创建阈值**：一个名字在 ≥2 份素材中出现，或在一份素材里是核心论点 → 独立成页。

## Frontmatter

```yaml
---
title: 页面标题
type: concept            # source | entity | concept | analysis | project | meta
slug: page-slug          # 全库唯一，与文件名一致（不含 .md）
tags: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []              # 支撑本页的 raw 素材 slug
related: []
evidence_tier: single    # single | crossed | primary —— 由 sources 推导，lint 校验
confidence: high         # high | medium | low —— 主观判断
status: active           # active | draft | stale | deprecated
---
```

**`evidence_tier` 与 `confidence` 是两个维度**：前者是「有几份来源」（可计算，`lint` 校验），
后者是「我信多少」（主观）。一页可以有多份来源（`crossed`）但仍然 `confidence: low`（全是转述）。
多份素材也不等于多个独立佐证 —— **同源转述的重复计数不算交叉验证**。

项目页额外有 `goal`（**必须可验收** —— 看到它能回答「做完了没有」）与
`stage`（`planning` / `active` / `paused` / `shipped` / `abandoned`）。
**注意 `stage`（这件事做到哪了）与 `status`（这页还新鲜吗）是两个维度，不要混用。**

## 工作流

**Ingest**：**先读 projects/ 判断这份素材服务于哪个项目、填哪个缺口** → 读素材
→ 与人类对齐要点 → 写 sources 页 → 拆 entities/concepts 页
→ 回填所有被影响的页面 → 更新 index.md → 写 log → 跑 lint。
一份素材通常触及 10-15 个页面。**服务不了任何项目的素材，先问该不该收。**

**Query**：先读 index.md 定位 → 必要时 `wiki.py search` → 带引用作答
→ 好答案归档进 analyses/。

**Lint**：`wiki.py lint` 查机器可查问题，再人工核查矛盾、过期、该建未建。

## 写作约定

- 文件名：全小写，单词用 `-` 连接，英文 slug。标题用中文写在 `title` 字段里。
- 素材文件名：`YYYY-MM-DD-slug.md`，日期用**收录日**。
- 语气：直接、信息密度高。不要「值得注意的是」「综上所述」这类填充词。
- 长度：概念页 60-200 行。超过 300 行说明该拆页。
- 数字与事实必须能追溯到 `sources`。**没有来源的断言要显式标注**：`（未验证）`。
"""


INIT_DECISIONS = """# 裁定档案

> **人类对 schema 做过的裁定，以及被它们推翻的旧做法。** 正序，只追加、不覆盖。

这里放的是「**为什么这么定**」。规则本身在 `wiki/schema.md`，人类偏好在 `wiki/conventions.md`。

**本页按需读。** 追问某条规则的来历、或要推翻它之前，先来这里看有没有前案。
单独成页的理由：schema 的演进史是**给需要判断的人看的**，不是给每个会话看的。

## 记录

（尚无裁定。）

每条建议写清四件事：**日期 ｜ 裁定了什么 ｜ 推翻了什么 ｜ 为什么**。
若某条规则有先例（某份素材是它第一次被用上的地方），一并记下 —— 先例是这条规则最好的说明书。
"""


TEMPLATES = {}

TEMPLATES["source"] = """---
title: {{TITLE}}
type: source
slug: {{SLUG}}
tags: []
created: {{DATE}}
updated: {{DATE}}
sources: [{{SLUG}}]
related: []
confidence: high
status: active
---

# {{TITLE}}

> 提要：这份素材讲了什么、为什么值得收。
> **行号、坐标系、核查过程不写在这里** —— 那是账目区的事。站点侧会把这一段渲染成独立的提要面板。

<!-- 上款：站点侧把这些 `- **标签**：值` 渲染成一张出处卡。读者第一眼要看到的就是它。 -->
- **作者 / 来源**：
- **链接**：
- **发表**：
- **素材路径**：`raw/{{SLUG}}.md`

<!-- ================= 正文区：给读者看的，站点侧不折叠 ================= -->

## 关键要点

1.
2.
3.

## 摘要

按素材自身的逻辑复述，不加入素材以外的判断。

## 与本库既有页面的关系

- 印证了：[[ ]]
- 补充了：[[ ]]
- **与 [[ ]] 存在矛盾**：（如有，必须明确指出并列出双方证据）

## 新出现的实体 / 概念

- 实体：[[ ]]
- 概念：[[ ]]

## 待办 / 开放问题

- [ ]

## 相关页面

- [[ ]]

<!-- ================= 账目区：给维护者看的，站点侧默认折叠成卡片 =================
     这里放分层表 / 引注核查表 / 回填清单 / 归属判断 / 定级理由 / 证据性质 /
     AI 加工段判定 / 素材基本信息 / 行号坐标系之类的东西。
     放这里不代表不重要 —— 只是读「这份素材讲了什么」的人不需要先翻过它。
     判定词表见 wiki/schema.md §1.8；对账用 `python3 tools/wiki.py chapter-audit`。 -->

## 素材基本信息

## 素材分层表（文件绝对行号）

## 引注核查表

## 归属判断

## 定级理由

<!-- ================= 页脚 ================= -->

## 来源

- [[{{SLUG}}]]
"""

TEMPLATES["entity"] = """---
title: {{TITLE}}
type: entity
slug: {{SLUG}}
tags: []
created: {{DATE}}
updated: {{DATE}}
sources: []
related: []
evidence_tier: single
confidence: medium
status: active
---

# {{TITLE}}

> 一句话说明这是什么、为什么值得单独一页。

- **类型**：人物 / 组织 / 工具 / 产品
- **别名**：
- **外部链接**：

## 是什么

## 关键事实

| 时间 | 事实 | 来源 |
|---|---|---|
|  |  |  |

## 在本知识库中的角色

为什么它会反复出现，与哪些页面强相关。

## 相关概念

- [[ ]]

## 来源

- [[ ]]
"""

TEMPLATES["concept"] = """---
title: {{TITLE}}
type: concept
slug: {{SLUG}}
tags: []
created: {{DATE}}
updated: {{DATE}}
sources: []
related: []
evidence_tier: single
confidence: medium
status: active
---

# {{TITLE}}

> 一句话定义。读者只看这一行也能知道这页在讲什么。

## 要点

-
-

## 定义与背景

## 机制 / 原理

## 边界与反例

什么情况下不成立、容易与什么混淆。

## 与其他页面的关系

- 区别于 [[ ]]：
- 是 [[ ]] 的前置：
- 与 [[ ]] 互补：

## 开放问题

- [ ]

## 来源

- [[ ]]
"""

TEMPLATES["analysis"] = """---
title: {{TITLE}}
type: analysis
slug: {{SLUG}}
tags: []
created: {{DATE}}
updated: {{DATE}}
sources: []
related: []
evidence_tier: single
confidence: medium
status: active
---

# {{TITLE}}

> 一句话说明这份分析得出的结论。

- **触发问题**：
- **结论**：

## 对比 / 论证

| 维度 | A | B |
|---|---|---|
|  |  |  |

## 证据

每条证据标注来源页。

## 结论与适用条件

什么情况下该选 A，什么情况下该选 B。

## 遗留问题

- [ ]

## 来源

- [[ ]]
"""

TEMPLATES["project"] = """---
title: {{TITLE}}
type: project
slug: {{SLUG}}
tags: []
created: {{DATE}}
updated: {{DATE}}
goal: 一句话目标，要能被判断「完成没有」
stage: planning
started: {{DATE}}
sources: []
related: []
confidence: high
status: active
---

# {{TITLE}}

> 一句话：这个项目要产出什么。

- **目标（可验收）**：写得具体到能判断完成与否。反例「学习 Rust」；正例「用 Rust 写一个能跑的命令行工具并发布到 GitHub」
- **验收判据**：写清楚满足什么条件就算达成 —— 这是判断 shipped 的依据
- **终点**：「当前缺口」表清空即 `shipped`。之后若新素材开的是新缺口，**另开一个项目**，本项目不复活
- **阶段**：planning
- **起始**：{{DATE}}
- **目标完成**：

## 当前缺口

> 这一节是控制论里的**误差信号**，也是全页最重要的部分 —— **它决定下一步该找什么素材**。
> 每次 ingest 之前先读这里：这份素材填的是哪个缺口？填不上就不收。
> 标 **【阻塞】** 的条目直接挡住 `goal` 的验收条件，必须先解；未标的是可选或可延后。
> **决定不做的缺口要移入「不做什么」一节**，不要留在表里 —— 表清不空，项目就永远不能收尾。

| 缺口 | 卡在哪 | 需要什么素材 / 信息 |
|---|---|---|
|  |  |  |

## 知识（本项目消耗的页面）

> 项目与知识库之间的正向连接。这里链到的页面，就是「服务于本项目」的页面。

- [[ ]]

## 产出（外向回路）

> 知识库的价值在这里流出。**没有产出的项目是死项目**（见「共同笔记簿」页的「燃料而非收藏」）。

| 产出 | 形态 | 位置 |
|---|---|---|
|  |  |  |

## 决策记录

> 项目里做过的判断 —— 这是 AI 拿不到的部分，也是本库存在的核心理由（见「为什么在 AI 时代仍然需要 PKMS」页）。

| 日期 | 决定 | 理由 |
|---|---|---|
|  |  |  |

## 不做什么（反范围）

> 明确排除什么，避免范围蔓延。

- 

## 开放问题

- [ ]

## 相关页面

- [[ ]]
"""


def cmd_init(target=None):
    root = os.path.abspath(target or os.getcwd())
    for sub in ["raw/assets", "wiki/projects", "wiki/sources", "wiki/entities",
                "wiki/concepts", "wiki/analyses", "tools", "templates", ".obsidian"]:
        os.makedirs(os.path.join(root, sub), exist_ok=True)

    ag = os.path.join(root, "AGENTS.md")
    if not os.path.exists(ag):
        write_text(ag, INIT_AGENTS)

    for name, text in TEMPLATES.items():
        p = os.path.join(root, "templates", "%s.md" % name)
        if not os.path.exists(p):
            write_text(p, text)

    today = date.today().isoformat()

    def meta_fm(title, slug):
        return ("---\ntitle: %s\ntype: meta\nslug: %s\ncreated: %s\nupdated: %s\n"
                "status: active\n---\n\n" % (title, slug, today, today))

    for name in ["index", "log", "overview", "schema", "decisions", "conventions"]:
        path = os.path.join(root, "wiki", "%s.md" % name)
        if os.path.exists(path):
            continue
        if name == "index":
            write_text(path, meta_fm("索引", "index")
                             + "# 索引\n\n> 由 `python3 tools/wiki.py index` 生成。\n")
        elif name == "log":
            write_text(path, meta_fm("日志", "log")
                             + "# 日志\n\n> 只追加，不改写。\n\n"
                             + "## [%s] init | 知识库初始化\n\n" % today)
        elif name == "overview":
            write_text(path, meta_fm("总览", "overview")
                             + "# 总览\n\n> 这个知识库在讲什么。\n\n## 范围\n\n## 核心线索\n\n"
                             + "## 页面地图\n\n- 项目：`projects/`（入口层）\n- 素材：`sources/`\n"
                             + "- 实体：`entities/`\n- 概念：`concepts/`\n- 分析：`analyses/`\n")
        elif name == "schema":
            write_text(path, meta_fm("维护细则", "schema") + INIT_SCHEMA)
        elif name == "decisions":
            write_text(path, meta_fm("裁定档案", "decisions") + INIT_DECISIONS)
        else:
            write_text(path, meta_fm("使用约定", "conventions")
                             + "# 使用约定\n\n> 记录人类的使用偏好。\n\n"
                             + "## 回答风格\n\n- 语言：中文\n- 标注来源：是\n\n"
                             + "## 收录偏好\n\n- 一次一份素材\n- 冲突必须显式标注\n")

    obs = os.path.join(root, ".obsidian", "app.json")
    if not os.path.exists(obs):
        write_text(obs, '{\n  "attachmentFolderPath": "raw/assets"\n}\n')

    print("已初始化知识库: %s" % root)
    print("下一步：把素材放进 raw/，然后让 LLM 执行 ingest 工作流。")
    return 0


# ---------------------------------------------------------------- build (站点)


HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__SITE_TITLE__</title>
<style>
:root{
  --bg:#faf9f7; --panel:#ffffff; --ink:#1b1c1e; --muted:#75736d;
  --line:#e8e6e1; --line-soft:#f1efeb; --accent:#0f766e; --accent-soft:#e6f2f0;
  --code-bg:#f5f4f1;
  --c-project:#7c3aed; --c-source:#0f766e; --c-entity:#b45309; --c-concept:#4338ca; --c-analysis:#be123c; --c-meta:#6b7280;
}
*{box-sizing:border-box}
html,body{margin:0;padding:0;height:100%}
body{
  background:var(--bg); color:var(--ink);
  font:15px/1.72 -apple-system,BlinkMacSystemFont,"PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;
  -webkit-font-smoothing:antialiased;
}
#app{display:flex;height:100vh;overflow:hidden}

/* ---------- sidebar ---------- */
/* 左侧栏的横向基准线：组头文字与条目文字都落在 36px 处。
   组头 padding-left 20 + caret 9 + gap 7 = 36；
   条目 nav padding 10 + 左边框 2 + padding 10 + dot 6 + gap 8 = 36。 */
#sidebar{
  width:296px;flex:0 0 296px;background:var(--panel);border-right:1px solid var(--line);
  display:flex;flex-direction:column;overflow:hidden;
}
.brand{padding:17px 20px 11px;border-bottom:1px solid var(--line-soft)}
.brand h1{margin:0;font-size:15px;letter-spacing:.2px;font-weight:650}
.brand .sub{font-size:11.5px;color:var(--muted);margin-top:3px;font-variant-numeric:tabular-nums}
.searchwrap{position:relative;padding:11px 16px 9px}
#search{
  width:100%;padding:8px 30px 8px 11px;border:1px solid var(--line);border-radius:8px;
  background:var(--bg);font-size:13px;color:var(--ink);outline:none;font-family:inherit;
  transition:border-color .14s,box-shadow .14s,background .14s;
}
#search:focus{border-color:var(--accent);background:#fff;box-shadow:0 0 0 3px var(--accent-soft)}
#search::placeholder{color:#a8a5a0}
#searchclear{
  position:absolute;right:24px;top:calc(50% - 1px);transform:translateY(-50%);
  width:18px;height:18px;padding:0;border:0;border-radius:50%;
  background:var(--line-soft);color:var(--muted);cursor:pointer;display:none;
  font-family:inherit;font-size:11px;line-height:1;
}
#searchclear.on{display:block}
#searchclear:hover{background:var(--line);color:var(--ink)}
.navtools{display:flex;align-items:center;gap:2px;padding:0 16px 8px}
.navtools .lbl{font-size:10.5px;font-weight:650;letter-spacing:1.1px;color:#a8a5a0}
.navtools .sp{flex:1}
.navtools button{
  border:0;background:transparent;font:inherit;font-size:11.5px;color:var(--muted);
  cursor:pointer;padding:3px 7px;border-radius:6px;transition:background .12s,color .12s;
}
.navtools button:hover{background:var(--line-soft);color:var(--accent)}
#nav{flex:1;overflow-y:auto;overflow-x:hidden;overscroll-behavior:contain;padding:0 10px 32px}
.nav-item{
  display:flex;align-items:center;gap:8px;padding:6px 10px;border-radius:6px;cursor:pointer;
  font-size:13.2px;line-height:1.45;color:var(--ink);text-decoration:none;
  overflow:hidden;border-left:2px solid transparent;
  transition:background .12s,color .12s;
}
.nav-item:hover{background:var(--line-soft)}
.nav-item.active{background:var(--accent-soft);border-left-color:var(--accent);font-weight:600;color:var(--accent)}
.nav-item:focus-visible{outline:2px solid var(--accent);outline-offset:-2px}
.nav-item .dot{flex:0 0 6px;width:6px;height:6px;border-radius:50%}
.nav-item .t{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.res-count{font-size:11.5px;color:var(--muted);padding:4px 12px 8px}
/* 搜索结果：dot 与标题首行基线对齐，摘要/元信息缩进到标题列。
   旧版 dot 是 inline-block、标题是 block，dot 会被挤成单独一行。 */
.nav-item.res{
  display:grid;grid-template-columns:6px 1fr;column-gap:8px;align-items:start;
  white-space:normal;padding:7px 10px;
}
.nav-item.res .dot{grid-row:1 / span 3;margin-top:7px}
.nav-item.res .r-title{grid-column:2;font-size:13.2px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.nav-item.res .r-snip{
  grid-column:2;font-size:11.8px;color:var(--muted);line-height:1.5;
  max-height:3em;overflow:hidden;
}
.nav-item.res .r-meta{grid-column:2;font-size:11px;color:var(--muted);font-variant-numeric:tabular-nums}
.nav-item.res mark,.nav-item.res.active mark{background:#fde68a;color:inherit;border-radius:2px;padding:0 1px}
/* 必须在 .nav-item.res 之后：隐藏规则与 display:flex/grid 同级，靠顺序决胜 */
.nav-item[hidden]{display:none}
.res-more{
  display:block;width:100%;text-align:left;border:0;background:transparent;font:inherit;
  font-size:12px;color:var(--accent);cursor:pointer;padding:6px 12px;
}

/* ---------- 一级分组（侧栏不再有二级） ---------- */
/* 只有 6 个类型组，组内平铺。此前按 tag 切的二级分类已删除 —— 一页平均 5.6 个 tag，
   强行互斥归类必然错配，分类本身比不分类更难用。
   替代方案是「组内筛选框」（组大到 20 页以上才出现）：收敛交给用户输入，不交给猜测。
   组头 sticky：长列表滚到哪儿都知道自己在哪个类型里。
   展开状态写 localStorage（file:// 下不可用时静默降级为「本次会话有效」）。 */
.grp{margin-bottom:2px}
.grp + .grp{border-top:1px solid var(--line-soft)}
.grp h3{
  height:30px;margin:0 -10px;padding:0 20px;
  display:flex;align-items:center;justify-content:space-between;gap:8px;
  font-size:11px;font-weight:650;letter-spacing:.5px;color:var(--muted);
  position:sticky;top:0;z-index:2;cursor:pointer;user-select:none;
  background:var(--panel);   /* 必须不透明：渐变会让下方条目透出来，sticky 时糊成一片 */
  transition:color .12s,background .12s;
}
.grp h3:hover{color:var(--ink);background:var(--line-soft)}
.grp h3 .gl{display:flex;align-items:center;min-width:0}
.grp h3 .caret{
  flex:0 0 9px;width:9px;margin-right:7px;color:#a5a29b;
  transition:transform .16s ease;
}
.grp.collapsed h3 .caret{transform:rotate(-90deg)}
.grp h3 .gtxt{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.grp h3 .n{
  flex:0 0 auto;font-size:10.5px;font-weight:500;letter-spacing:0;color:#a8a5a0;
  background:var(--line-soft);border-radius:20px;padding:1px 7px;font-variant-numeric:tabular-nums;
}
.grp.collapsed .grpbody{display:none}
.grpfind{position:sticky;top:30px;z-index:1;padding:6px 0;background:var(--panel)}
.gfbox{position:relative;display:block}
.grpfind input{
  width:100%;padding:5px 56px 5px 10px;border:1px solid var(--line);border-radius:6px;
  background:var(--bg);font-family:inherit;font-size:12px;color:var(--ink);outline:none;
  transition:border-color .14s,background .14s;
}
.grpfind input:focus{border-color:var(--accent);background:#fff}
.grpfind input::placeholder{color:#a8a5a0}
/* 命中数放在输入框内侧右端：筛选时组头可能已经 sticky 出界，只有这里能告诉你收窄到几条 */
.gfbox.on input{background:var(--accent-soft);border-color:#bcd9d4}
.fcount{
  position:absolute;right:9px;top:50%;transform:translateY(-50%);
  font-size:10.5px;color:var(--accent);font-variant-numeric:tabular-nums;pointer-events:none;
}
.fcount[hidden]{display:none}
.grpempty{padding:6px 10px 12px;font-size:12px;color:var(--muted)}
.grpempty[hidden]{display:none}
.res-tip{font-size:11.5px;color:#a8781f;background:#fdf6e6;border:1px solid #f2e3bd;
  border-radius:6px;padding:6px 9px;margin:2px 10px 8px;line-height:1.5}
/* ---------- TOC ---------- */
#toc{
  display:block;position:fixed;top:92px;right:16px;width:190px;max-height:calc(100vh - 140px);
  overflow-y:auto;font-size:12px;line-height:1.65;padding-left:2px;
}
#toc[hidden]{display:none}
#toc a{
  display:block;padding:2px 8px;color:var(--muted);text-decoration:none;
  border-left:2px solid transparent;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;
}
#toc a:hover{color:var(--accent)}
#toc a.on{color:var(--accent);border-left-color:var(--accent);font-weight:600}
#toc a.lv3{padding-left:20px;font-size:11.3px}

/* ---------- main ---------- */
#main{flex:1;display:flex;flex-direction:column;overflow:hidden}
#tabs{
  height:46px;flex:0 0 46px;display:flex;align-items:center;gap:6px;
  padding:0 20px;border-bottom:1px solid var(--line);background:var(--panel);
}
#tabs button{
  border:0;background:transparent;font:inherit;font-size:13px;color:var(--muted);
  padding:6px 12px;border-radius:7px;cursor:pointer;
}
#tabs button:hover{background:var(--line-soft)}
#tabs button.active{background:var(--accent-soft);color:var(--accent);font-weight:600}
#tabs .spacer{flex:1}
#tabs .meta{font-size:12px;color:var(--muted);font-variant-numeric:tabular-nums}

#view-browse{flex:1;overflow-y:auto;padding:34px 0 90px}
#wrap{max-width:760px;margin:0 auto;padding:0 40px}
article h1{font-size:27px;line-height:1.32;margin:0 0 6px;letter-spacing:-.3px}
article h2{font-size:18.5px;margin:34px 0 10px;padding-bottom:6px;border-bottom:1px solid var(--line-soft)}
article h3{font-size:15.5px;margin:24px 0 8px}
article p{margin:11px 0}
article ul,article ol{margin:11px 0;padding-left:24px}
article li{margin:4px 0}
article blockquote{
  margin:16px 0;padding:12px 16px;background:var(--accent-soft);
  border-left:3px solid var(--accent);border-radius:0 7px 7px 0;color:#204b46;
}
article blockquote p{margin:4px 0}
article code{background:var(--code-bg);padding:1.5px 5px;border-radius:4px;
  font:12.8px/1.5 ui-monospace,SFMono-Regular,Menlo,monospace}
article pre{background:var(--code-bg);padding:14px 16px;border-radius:9px;overflow-x:auto;
  border:1px solid var(--line)}
article pre code{background:none;padding:0;font-size:12.6px}
article table{border-collapse:collapse;width:100%;margin:16px 0;font-size:13.6px}
article th,article td{border:1px solid var(--line);padding:7px 11px;text-align:left;vertical-align:top}
article th{background:var(--line-soft);font-weight:650}
article hr{border:0;border-top:1px solid var(--line);margin:26px 0}
article a{color:var(--accent);text-decoration:none;border-bottom:1px solid #b9d8d3}
article a:hover{border-bottom-color:var(--accent)}
a.wl{border-bottom:1px dotted #9cc7c1;cursor:pointer}
a.wl.broken{color:#b91c1c;border-bottom:1px dashed #e0a0a0}
/* 引文块内文字本身是深青色，链接需要更强的区分度 */
article blockquote a{color:#0b5f57;font-weight:600;border-bottom:1px solid #7fbcb4}
article blockquote a:hover{border-bottom-color:#0b5f57}

/* ==================================================================
   素材页（source）阅读层
   ------------------------------------------------------------------
   设计意图：一页 source 是一份**可追溯的凭据**，不是一个章节容器。
   它的自然形状是三段而不是一列：

       上款  标题 / 提要（一句话内容）/ 出处卡（作者·链接·路径）
       正文  关键要点 / 摘要 / 与本库的关系 / 派生页
       账目  分层表 / 引注核查表 / 归属判断 / 定级理由 / 回填清单

   旧版把这三段平铺成同一种 `## 标题 + 段落`，于是一张 40 行的行号表
   夹在「要点」和「摘要」之间 —— 读者要找「这份素材讲了什么」，
   得先翻过记账。改革点只有一处：**给账目一个可折叠的边界**，
   并且默认收起。文字一个不删，只是不再挡路。

   另注：不做「账目统一搬到页尾」的自动重排 —— 实测本库 sources 里有
   330 处页内指向引用（见下 138 / 见上 38 / 下文 57 / 上表 16 / 下表 6 …），
   重排会让它们全部指错。置底做成用户可以自己按的开关，见 #ledgctl。
   ================================================================== */

/* ---- 上款 ---- */
article blockquote.lead{
  margin:20px 0 20px;padding:15px 20px 15px 22px;font-size:15.2px;line-height:1.78;
  background:linear-gradient(180deg,#e9f4f2,#e3efed);border-left:3px solid var(--accent);
  color:#1e4a45;border-radius:0 10px 10px 0;
}
.lead-eb{
  display:flex;align-items:center;gap:8px;margin:0 0 9px;
  font-size:10px;font-weight:700;letter-spacing:1.5px;color:#0b5f57;opacity:.72;
}
.lead-eb::before{content:"";width:14px;height:1px;background:currentColor}
.lead-eb::after{content:"";flex:1;height:1px;background:currentColor;opacity:.35}
article blockquote.lead p{margin:6px 0}
article blockquote.lead p:first-of-type{margin-top:0}
article blockquote.lead p:last-of-type{margin-bottom:0}

/* 出处卡：作者 / 链接 / 发表 / 素材路径。旧版是一个和正文一样样的 <ul>，
   于是「这份东西是什么、谁写的、原文在哪」和一条普通要点长得完全相同。 */
.prov{
  margin:0 0 26px;padding:13px 16px;background:var(--panel);
  border:1px solid var(--line);border-radius:11px;
}
.prov .pv{display:grid;grid-template-columns:88px minmax(0,1fr);gap:12px;padding:6px 0}
.prov .pv.wide{grid-template-columns:minmax(0,1fr)}
.prov .pv.wide .v{grid-column:1}
.prov .pv + .pv{border-top:1px solid var(--line-soft)}
.prov .pv:first-child{padding-top:2px}
.prov .pv:last-child{padding-bottom:2px}
.prov .k{
  font-size:11.5px;line-height:1.75;color:var(--muted);letter-spacing:.2px;
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis;padding-top:1px;
}
.prov .v{font-size:13.6px;line-height:1.72;min-width:0;overflow-wrap:anywhere}
.prov .v > p:first-child{margin-top:0}
.prov .v > p:last-child{margin-bottom:0}
.prov .v code{font-size:12.4px;background:var(--code-bg);padding:1.5px 5px;border-radius:4px;
  border:1px solid var(--line-soft)}
.prov .v a{border-bottom:1px solid #b9d8d3}
.prov .v a:hover{border-bottom-color:var(--accent)}
.prov .v blockquote{margin:9px 0 3px;font-size:13px;padding:9px 13px;background:#fdf6e6;
  border-left:3px solid #d9a441;color:#6b4c14;border-radius:0 7px 7px 0}
.prov .v blockquote a{color:#8a5a06;border-bottom-color:#dcbc86}

/* ---- 关键要点：悬挂序号。序号退到正文左侧的空白里，正文左缘保持一条直线 ---- */
ol.keypoints{list-style:none;counter-reset:kp;margin:14px 0 20px;padding:0 0 0 36px}
ol.keypoints > li{position:relative;margin:0 0 11px;padding:0}
ol.keypoints > li::before{
  counter-increment:kp;content:counter(kp);
  position:absolute;left:-36px;top:.15em;width:22px;text-align:right;
  font-size:12.5px;font-weight:700;line-height:1.7;color:var(--accent);opacity:.55;
  font-variant-numeric:tabular-nums;
}
ol.keypoints > li:last-child{margin-bottom:0}
/* 嵌套的编号表回落成普通十进制标号：悬挂序号只对顶层有意义，
   套进子层之后 left:-36px 会按子层的行盒算，缩进会算重。
   注意必须把 list-style 补回来、把 counter-increment 关掉 ——
   子层 li 同样是 `ol.keypoints > li`，不关掉就会偷走外层的计数，
   外层编号会跳号（1, 2, 4 …）。 */
ol.keypoints ol.keypoints{list-style:decimal;padding-left:22px}
ol.keypoints ol.keypoints > li{padding-left:0}
ol.keypoints ol.keypoints > li::before{content:none;counter-increment:none}

/* ---- 待办清单 ---- */
ul.checklist{list-style:none;margin:13px 0 20px;padding:0}
ul.checklist > li.task{display:flex;gap:10px;align-items:flex-start;margin:0;padding:4px 0}
ul.checklist > li.task::marker{content:none}
ul.checklist input[type=checkbox]{
  appearance:none;-webkit-appearance:none;flex:0 0 15px;width:15px;height:15px;
  margin:5px 0 0;border:1.5px solid #cbc7bf;border-radius:4.5px;background:#fff;
  display:block;position:relative;cursor:default;
}
ul.checklist input[type=checkbox]:checked{background:var(--accent);border-color:var(--accent)}
ul.checklist input[type=checkbox]:checked::after{
  content:"";position:absolute;left:4px;top:.5px;width:4px;height:8px;
  border:solid #fff;border-width:0 1.8px 1.8px 0;transform:rotate(42deg);
}
ul.checklist > li.task > .tx{min-width:0;flex:1}
ul.checklist > li.task.done > .tx{
  color:var(--muted);text-decoration:line-through;
  text-decoration-color:#cfccc6;text-decoration-thickness:1px;
}

/* ---- callout：> [!note] / [!warning] / [!important] / [!success]
       旧版完全没渲染，`[!warning]` 当字面文本印在正文里，且标题被并进后一段。 ---- */
details.callout{
  margin:17px 0;border:1px solid var(--co-line);border-radius:10px;
  background:var(--co-bg);overflow:hidden;
}
details.callout > summary{
  list-style:none;cursor:pointer;display:flex;align-items:flex-start;gap:9px;
  padding:11px 15px;font-size:13.6px;font-weight:650;line-height:1.62;color:var(--co-ink);
}
details.callout > summary::-webkit-details-marker{display:none}
details.callout > summary::before{
  content:"";flex:0 0 17px;width:17px;height:17px;margin-top:1.5px;border-radius:5px;
  background:var(--co-ink);display:flex;align-items:center;justify-content:center;
  font-size:11px;font-weight:700;color:#fff;line-height:1;
}
/* 分隔线挂 .co-bd 上而不是 summary 上：只有标题、没有正文的 callout 不该拖一条悬空的横线 */
.co-bd{padding:11px 15px 13px 41px;font-size:14.2px;line-height:1.76;color:#2b2c2f;
  border-top:1px solid var(--co-line)}
.co-bd > p:first-child{margin-top:0}
.co-bd > p:last-child{margin-bottom:0}
.co-bd table,.co-bd .tbl{font-size:12.9px}
.co-bd .tbl{margin:11px 0}
.co-bd blockquote{margin:11px 0;font-size:13.4px}
details.co-tip{--co-ink:#0b5f57;--co-bg:#eaf4f2;--co-line:#bcd9d4}
details.co-tip > summary::before{content:"i";font-family:Georgia,serif;font-style:italic}
details.co-warn{--co-ink:#8a5a06;--co-bg:#fdf6e6;--co-line:#eedcb4}
details.co-warn > summary::before{content:"!"}
details.co-key{--co-ink:#3730a3;--co-bg:#eef0fb;--co-line:#d2d6f1}
details.co-key > summary::before{content:"★";font-size:9.5px}
details.co-ok{--co-ink:#12693a;--co-bg:#ecf6ee;--co-line:#c8e2ce}
details.co-ok > summary::before{content:"✓"}
details.co-bad{--co-ink:#9f1239;--co-bg:#fdedef;--co-line:#f1ccd4}
details.co-bad > summary::before{content:"✕";font-size:9.5px}
article blockquote a{color:#0b5f57}
details.callout a{color:var(--co-ink);border-bottom:1px solid currentColor;font-weight:600}

/* ---- 表格：行号表是本库的主体证据，窄列里五列会挤成一片 ----
   .tbl 自成一个滚动区：一是横向能滚，二是表头能 sticky 住（40 行表不用再上下对表头）。 */
.tbl{
  margin:18px 0;border:1px solid var(--line);border-radius:11px;
  background:var(--panel);overflow:auto;overscroll-behavior-x:contain;
}
.tbl table{margin:0;border:0;border-collapse:separate;border-spacing:0;width:100%;font-size:13.4px}
.tbl th,.tbl td{
  border:0;border-bottom:1px solid var(--line-soft);border-right:1px solid var(--line-soft);
  padding:8px 12px;text-align:left;vertical-align:top;
}
.tbl th:last-child,.tbl td:last-child{border-right:0}
.tbl tbody tr:last-child td{border-bottom:0}
.tbl thead th{
  position:sticky;top:0;z-index:1;background:#f4f2ee;color:#4a4842;
  font-weight:650;font-size:12.5px;letter-spacing:.2px;
}
.tbl tbody tr:nth-child(even){background:#fcfbf9}
.tbl.tall{max-height:76vh}
.tbl.tall thead th{box-shadow:0 1px 0 var(--line)}
.tbl.num th:first-child,.tbl.num td:first-child{
  white-space:nowrap;font-variant-numeric:tabular-nums;color:#57544e;
}
.tbl code{font-size:12.1px}

/* ---- 账目章节：可折叠的「凭据附件」 ---- */
section.sec{scroll-margin-top:16px}
section.ledger{
  border:1px solid #eae7e1;border-radius:11px;background:#fbfaf8;
  margin:16px 0;padding:0 16px 6px;
}
section.ledger > h2{
  display:flex;align-items:center;gap:9px;
  margin:0 -16px;padding:11px 16px;
  font-size:13.2px;font-weight:650;letter-spacing:.2px;color:#6a6760;
  background:linear-gradient(180deg,#f7f6f3,#f2f0ec);
  border-bottom:1px solid #eae7e1;border-radius:11px 11px 0 0;
  cursor:pointer;user-select:none;transition:color .12s;
}
section.ledger > h2:hover{color:var(--ink)}
/* 箭头用 CSS 画，不写字符 —— 标题的 textContent 会被右侧目录读走，
   塞一个「▾」进去，目录里就会出现「▾引注核查表」。 */
section.ledger > h2::before{
  content:"";flex:0 0 9px;width:7px;height:7px;margin-right:1px;
  border-right:1.7px solid #a5a29b;border-bottom:1.7px solid #a5a29b;
  transform:rotate(45deg) translate(-1px,-1px);transition:transform .16s ease;
}
section.ledger.collapsed > h2::before{transform:rotate(-45deg) translate(-1px,1px)}
section.ledger.collapsed{padding-bottom:0}
section.ledger.collapsed > .lg-bd{display:none}
section.ledger .lg-bd{padding:2px 0 0}
section.ledger .lg-bd h3{font-size:14.2px;margin:18px 0 7px}
section.ledger .lg-bd > p,section.ledger .lg-bd > ul,
section.ledger .lg-bd > ol,section.ledger .lg-bd > blockquote{font-size:14px}
.lg-peek{
  display:none;margin:10px 0 12px;font-size:12.6px;line-height:1.68;color:var(--muted);
  overflow:hidden;text-overflow:ellipsis;white-space:nowrap;
}
section.ledger.collapsed > .lg-peek{display:block}

/* ---- 来源页脚：把一条 [[slug]] 变成一枚可点的凭据 chip ---- */
section.prov-sec{margin:34px 0 0;padding:18px 0 0;border-top:1px solid var(--line)}
section.prov-sec > h2{
  border:0;margin:0 0 11px;padding:0;font-size:10.5px;font-weight:700;
  letter-spacing:1.3px;color:var(--muted);
}
section.prov-sec ul{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:8px}
section.prov-sec li{margin:0}
section.prov-sec a{
  display:inline-block;margin:0;padding:5px 11px;border-radius:8px;
  background:var(--panel);border:1px solid var(--line);font-size:12.6px;
  color:var(--ink);border-bottom:1px solid var(--line);
}
section.prov-sec a:hover{border-color:var(--accent);color:var(--accent)}

/* ---- 阅读进度 + 账目开关 ---- */
#tabs{position:relative}
#prog{
  position:absolute;left:0;bottom:-1px;height:2px;width:0;
  background:var(--accent);border-radius:0 2px 2px 0;transition:width .1s linear;
}
.segctl{display:flex;border:1px solid var(--line);border-radius:8px;overflow:hidden;margin-right:12px}
.segctl[hidden]{display:none}
.segctl button{
  border:0;background:transparent;font:inherit;font-size:11.8px;color:var(--muted);
  padding:4px 10px;cursor:pointer;transition:background .12s,color .12s;
}
.segctl button + button{border-left:1px solid var(--line)}
.segctl button:hover{background:var(--line-soft)}
.segctl button.on{background:var(--accent-soft);color:var(--accent);font-weight:600}

/* ---- TOC 双分组 ---- */
#toc .tglbl{
  display:block;padding:9px 9px 3px;font-size:9.5px;font-weight:700;
  letter-spacing:1.3px;color:#a8a5a0;
}
#toc .tg-ledger .tglbl{color:#a8781f}
#toc .tg-ledger a{opacity:.82}

/* ---- 阅读度量 ---- */
article{text-wrap:pretty}
article h1,article h2,article h3{text-wrap:balance}
article p{overflow-wrap:break-word}

@media (prefers-reduced-motion:reduce){
  *{transition-duration:.01ms !important;animation-duration:.01ms !important}
}
@media print{
  #sidebar,#tabs,#toc,.segctl,#prog{display:none !important}
  #view-browse{overflow:visible;padding:0}
  section.ledger{border-color:#ddd;break-inside:avoid}
  section.ledger.collapsed > .lg-bd{display:block}  /* 打印时账目一律展开 */
  section.ledger .lg-peek{display:none !important}
  details.callout{break-inside:avoid}
}
.pagemeta{
  display:flex;flex-wrap:wrap;gap:7px;align-items:center;margin:0 0 22px;
  padding-bottom:16px;border-bottom:1px solid var(--line-soft);
}
.chip{font-size:11px;padding:2.5px 9px;border-radius:20px;background:var(--line-soft);
  color:var(--muted);border:1px solid var(--line)}
.chip.t{color:#fff;border-color:transparent}
.chip.tag{background:#fff;color:var(--muted)}
.chip.stale{background:#fdecec;color:#b91c1c;border-color:#f5c2c2}
#backlinks{
  max-width:760px;margin:40px auto 0;padding:20px 40px 0;border-top:1px solid var(--line);
}
#backlinks h4{margin:0 0 10px;font-size:12px;letter-spacing:.9px;color:var(--muted);text-transform:uppercase}
#backlinks a{display:inline-block;margin:0 8px 8px 0;padding:5px 11px;border-radius:7px;
  background:var(--panel);border:1px solid var(--line);font-size:12.6px;color:var(--ink);text-decoration:none}
#backlinks a:hover{border-color:var(--accent);color:var(--accent)}

/* ---- 宽屏适配：正文列宽 + 目录占位 ----
   旧版：目录是 position:fixed，不占布局宽度；正文在 #main 里居中，右缘算出
   `296 + (W-296)/2 + 420`，而目录左缘是 `W - 206`。两者之间永远夹着一条等宽的
   假空白，屏幕越宽越大 —— 1728px 下右侧空 296px、2K（2560px）下空 546px，
   同时左侧空 752px。**结果是正文被挤在偏左的位置，右边一整片是空的。**
   修法两条：
   ① 目录宽度在所有宽屏下都从布局里扣掉（padding-right），正文改为在「扣除侧栏
      与目录」的区间里居中 —— 左右留白自然对称，正文也不再被目录压住；
   ② 正文列宽随视口增长，上限 1180px。760px 是单栏阅读的舒适宽度，但本库 sources
      页有五列行号表，窄列下会挤成一片；再宽则中文单行超过 70 字，回视成本上升。
   公式里的 160px = 正文两侧各留 80px 呼吸：屏幕变宽时先涨留白，涨满才轮到正文。 */
@media (min-width:1001px){
  #view-browse{padding-right:206px}   /* 目录：宽 190 + 距右缘 16 */
  #wrap,#backlinks{max-width:clamp(760px, calc(100% - 160px), 1180px)}
}

/* ---------- graph ---------- */
#view-graph{flex:1;position:relative;overflow:hidden;background:var(--panel)}
#canvas{display:block;width:100%;height:100%;cursor:grab}
#canvas.drag{cursor:grabbing}
#graph-hint{
  position:absolute;left:16px;bottom:14px;font-size:11.5px;color:var(--muted);
  background:rgba(255,255,255,.9);padding:5px 10px;border-radius:7px;border:1px solid var(--line);
}
#legend{position:absolute;right:16px;top:14px;background:rgba(255,255,255,.92);
  border:1px solid var(--line);border-radius:9px;padding:9px 12px;font-size:11.5px;color:var(--muted)}
#legend div{margin:2px 0}
#legend i{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:7px}
.empty{color:var(--muted);text-align:center;padding:80px 20px;font-size:14px}
::-webkit-scrollbar{width:9px;height:9px}
::-webkit-scrollbar-thumb{background:#dcd9d3;border-radius:5px}
::-webkit-scrollbar-thumb:hover{background:#c6c2ba}
::-webkit-scrollbar-track{background:transparent}

/* ---------- 窄屏：侧栏改抽屉 ---------- */
#burger{
  display:none;border:0;background:transparent;font:inherit;font-size:15px;line-height:1;
  color:var(--muted);cursor:pointer;padding:6px 9px;border-radius:7px;margin-right:2px;
}
#burger:hover{background:var(--line-soft)}
#mask{display:none;position:fixed;inset:0;background:rgba(0,0,0,.26);z-index:8}
#mask.on{display:block}
@media (max-width:1000px){
  #sidebar{
    position:fixed;z-index:9;left:0;top:0;height:100vh;
    transform:translateX(-100%);transition:transform .18s ease;box-shadow:0 0 26px rgba(0,0,0,.14);
  }
  #sidebar.open{transform:translateX(0)}
  #burger{display:inline-block}
  #toc{display:none}
  #wrap{padding:0 20px}
  #backlinks{padding:20px 20px 0}
}
</style>
</head>
<body>
<div id="app">
  <aside id="sidebar">
    <div class="brand">
      <h1>__SITE_TITLE__</h1>
      <div class="sub">__SITE_SUB__</div>
    </div>
    <div class="searchwrap">
      <input id="search" placeholder="搜索页面…（空格分词，按 / 聚焦）" autocomplete="off">
      <button id="searchclear" type="button" title="清空搜索">✕</button>
    </div>
    <div class="navtools">
      <span class="lbl">目录</span><span class="sp"></span>
      <button id="expandall" type="button">展开全部</button>
      <button id="collapseall" type="button">折叠全部</button>
    </div>
    <nav id="nav"></nav>
  </aside>
  <main id="main">
    <div id="tabs">
      <button id="burger" title="目录">☰</button>
      <button data-view="browse" class="active">浏览</button>
      <button data-view="graph">图谱</button>
      <span class="spacer"></span>
      <div class="segctl" id="ledgctl" hidden>
        <button data-lg="collapse" class="on">账目收起</button>
        <button data-lg="expand">账目展开</button>
        <button data-lg="end">账目置底</button>
      </div>
      <span class="meta" id="tabmeta"></span>
      <div id="prog"></div>
    </div>
    <div id="view-browse">
      <div id="wrap"><article id="page"></article></div>
      <div id="backlinks"></div>
    </div>
    <div id="view-graph" hidden>
      <canvas id="canvas"></canvas>
      <div id="graph-hint">拖拽节点 · 滚轮缩放 · 点击打开</div>
      <div id="legend"></div>
    </div>
  </main>
</div>
<div id="mask"></div>
<nav id="toc"></nav>
<script>
var DATA = __WIKI_DATA__;
var TYPECOLOR = {project:"#7c3aed",source:"#0f766e",entity:"#b45309",concept:"#4338ca",analysis:"#be123c",meta:"#6b7280"};
var TYPELABEL = {project:"项目",source:"素材摘要",entity:"实体",concept:"概念",analysis:"分析",meta:"系统"};
var PAGES = DATA.pages, BYSLUG = {};
PAGES.forEach(function(p){ BYSLUG[p.slug] = p; });

/* ---------------- markdown ---------------- */
function esc(s){ return s.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;"); }

function inline(s){
  var out = esc(s);
  out = out.replace(/`([^`]+)`/g, function(m,c){ return "<code>"+c+"</code>"; });
  out = out.replace(/!\[([^\]]*)\]\(([^)]+)\)/g, function(m,a,u){ return '<img alt="'+a+'" src="'+u+'" style="max-width:100%">'; });
  out = out.replace(/\[\[([^\]|]+)(?:\|([^\]]+))?\]\]/g, function(m,slug,text){
    slug = slug.trim(); var label = (text||slug).trim();
    if (BYSLUG[slug]) return '<a class="wl" data-slug="'+slug+'">'+label+'</a>';
    return '<span class="wl broken" title="页面不存在">'+label+'</span>';
  });
  out = out.replace(/\[([^\]]+)\]\(([^)]+)\)/g, function(m,t,u){
    if (/^https?:/.test(u)) return '<a href="'+u+'" target="_blank" rel="noopener">'+t+'</a>';
    return '<a href="'+u+'">'+t+'</a>';
  });
  out = out.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
  out = out.replace(/(^|[^*])\*([^*\n]+)\*/g, "$1<em>$2</em>");
  out = out.replace(/~~([^~]+)~~/g, "<del>$1</del>");
  return out;
}

/* [!type] → 5 种语气。本库实际只用了 note / warning / important / success 四种；
   收成 5 种语气是为了「一眼分得清这是提示、警示还是结论」，不是为了穷举 Obsidian 的类型表。 */
var CO_TONE = {
  note:"tip", info:"tip", tip:"tip", hint:"tip", abstract:"tip", summary:"tip", todo:"tip",
  question:"tip", quote:"tip", example:"tip", cite:"tip",
  success:"ok", check:"ok", done:"ok",
  important:"key", key:"key",
  warning:"warn", caution:"warn",
  danger:"bad", error:"bad", fail:"bad", failure:"bad", missing:"bad", bug:"bad"
};
var CO_LABEL = {tip:"提示", warn:"警示", key:"重要", ok:"结论", bad:"问题"};

/* 代码块池：一次整页渲染共享一份，递归调用不会丢 */
var _codePool = [];

function mkCallout(type, folded, title, bodyLines){
  var tone = CO_TONE[type] || "tip";
  var body = bodyLines.length ? render(bodyLines.join("\n")) : "";
  return '<details class="callout co-'+tone+'"'+(folded ? "" : " open")+'>' +
           '<summary>'+(title ? inline(title) : CO_LABEL[tone])+'</summary>' +
           (body ? '<div class="co-bd">'+body+'</div>' : "") +
         '</details>';
}

function render(src){
  src = String(src).replace(/```[^\n]*\n([\s\S]*?)```/g, function(m, code){
    _codePool.push("<pre><code>"+esc(code.replace(/\n$/,""))+"</code></pre>");
    return "\u0000B"+(_codePool.length-1)+"\u0000";
  });

  var lines = src.split("\n"), out = [], i = 0;
  var RE_LIST = /^(\s*)([-*+]|\d+[.)])\s+(.*)$/;
  var RE_QUOTE = /^\s*>\s?/;
  var RE_PARA_STOP = /^(#{1,6}\s|\s*>|\||\s*[-*+]\s|\s*\d+[.)]\s|```)/;

  /* 列表：按缩进还原层级。
     旧版忽略缩进，本库 99 行嵌套条目被拍平成同级 —— 「这三条属于上一条」这层信息直接丢了。 */
  function parseList(start, base){
    var kind = null, items = [], i = start, guard = 0;
    while (i < lines.length && guard++ < 50000){
      var m = RE_LIST.exec(lines[i]);
      if (!m){
        if (!items.length || !kind) break;
        /* ① 缩进的续行 = 上一条的正文。markdown 里列表项常常写两三行，
              续行缩进 2-3 格、不以列表符号开头。旧版把它当成「列表结束」，
              结果是：条目被从中间劈开，续行变成列表外的独立段落，
              而且整节的编号断成一串 `1. 1. 1.`（narrative-self 的「关键要点」
              六条全中）。带 > | # ``` 的缩进行不算续行 —— 那是嵌套引用/表格，另有渲染路径。 */
        if (/^\s+\S/.test(lines[i]) && !/^\s*(>|\||#{1,6}\s|```)/.test(lines[i])){
          items[items.length-1].txt += " " + lines[i].trim();
          i++; continue;
        }
        /* ② 空行之后还是同类型同级的列表项 = 同一个列表（CommonMark 的 loose list）。
              不认这一条，中间隔了一个空行的编号表会被拆成两个 <ol>，编号从 1 重新数。 */
        var j = i;
        while (j < lines.length && !lines[j].trim()) j++;
        if (j < lines.length && RE_LIST.test(lines[j])){
          var m2 = RE_LIST.exec(lines[j]);
          var ind2 = m2[1].replace(/\t/g, "  ").length;
          if (ind2 === base && (/^\d/.test(m2[2]) ? "ol" : "ul") === kind){ i = j; continue; }
        }
        break;
      }
      var ind = m[1].replace(/\t/g, "  ").length;
      if (ind < base) break;
      if (ind > base){
        if (!items.length) break;
        var sub = parseList(i, ind);
        if (!sub || sub.next <= i) break;
        items[items.length-1].sub.push(sub.html);
        i = sub.next; continue;
      }
      var t = /^\d/.test(m[2]) ? "ol" : "ul";
      if (kind === null) kind = t; else if (t !== kind) break;
      items.push({ txt: m[3], sub: [] });
      i++;
    }
    if (!items.length || !kind) return null;
    var hasTask = items.some(function(x){ return /^\[[ xX]\]\s/.test(x.txt); });
    var body = items.map(function(it){
      var task = /^\[([ xX])\]\s+([\s\S]*)$/.exec(it.txt);
      if (task){
        var done = task[1].toLowerCase() === "x";
        return '<li class="task'+(done ? " done" : "")+'">' +
                 '<input type="checkbox" disabled'+(done ? " checked" : "")+'>' +
                 '<span class="tx">'+inline(task[2])+'</span>' + it.sub.join("") + '</li>';
      }
      return "<li>"+inline(it.txt)+it.sub.join("")+"</li>";
    }).join("");
    return { html: "<"+kind+(hasTask ? ' class="checklist"' : "")+">"+body+"</"+kind+">", next: i };
  }

  while (i < lines.length){
    var line = lines[i].replace(/\s+$/,"");

    if (/^\u0000B\d+\u0000$/.test(line)){ out.push(line); i++; continue; }
    if (!line.trim()){ i++; continue; }

    var h = /^(#{1,6})\s+(.*)$/.exec(line);
    if (h){ out.push("<h"+h[1].length+">"+inline(h[2])+"</h"+h[1].length+">"); i++; continue; }

    if (/^(---|\*\*\*|___)\s*$/.test(line)){ out.push("<hr>"); i++; continue; }

    if (RE_QUOTE.test(line)){
      var buf = [];
      while (i < lines.length && RE_QUOTE.test(lines[i])){
        buf.push(lines[i].replace(/^\s*>\s?/, "").replace(/\s+$/,"")); i++;
      }
      while (buf.length && !buf[buf.length-1].trim()) buf.pop();
      while (buf.length && !buf[0].trim()) buf.shift();
      /* 引用块首行是 [!type] 即 callout，其余仍是普通引用。
         旧版一律走 blockquote：`[!warning]` 当字面文本印在页面上，
         而且标题行与紧随的正文被合进同一个 <p> —— 标题等于没有。 */
      var co = /^\[!([A-Za-z]+)\]([+-]?)\s*([\s\S]*)$/.exec((buf[0] || "").trim());
      if (co) out.push(mkCallout(co[1].toLowerCase(), co[2] === "-", co[3].trim(), buf.slice(1)));
      else out.push("<blockquote>"+render(buf.join("\n"))+"</blockquote>");
      continue;
    }

    if (/^\|/.test(line) && i+1 < lines.length && /^\|[\s:|-]+\|/.test(lines[i+1])){
      var cells = function(s){
        /* 转义竖线 \| 先藏起来再切，否则 17 处含竖线的单元格会被切成两格 */
        return s.replace(/\\\|/g, "\u0001").split("|").slice(1,-1)
                .map(function(c){ return c.replace(/\u0001/g, "|").trim(); });
      };
      var head = cells(line), j = i + 2, rows = [];
      while (j < lines.length && /^\|/.test(lines[j])){ rows.push(cells(lines[j])); j++; }
      /* 表格从「一根线都不画的裸 table」变成自带滚动区的 .tbl：
         横向能滚，表头 sticky —— 本库分层表常有 40 行，上下对表头是纯浪费。
         只在行数多时限高，短表不给自己造第二个滚动条。 */
      var isNum = head.length && /^(行|序号|#|编号|讲次|模块|步骤|页码|日期)/.test(head[0]);
      var t = '<div class="tbl'+(rows.length >= 22 ? " tall" : "")+(isNum ? " num" : "")+'">' +
              "<table><thead><tr>";
      head.forEach(function(c){ t += "<th>"+inline(c)+"</th>"; });
      t += "</tr></thead><tbody>";
      rows.forEach(function(r){
        t += "<tr>";
        for (var k = 0; k < head.length; k++) t += "<td>"+inline(r[k]||"")+"</td>";
        t += "</tr>";
      });
      out.push(t+"</tbody></table></div>");
      i = j; continue;
    }

    if (RE_LIST.test(line)){
      var lm = RE_LIST.exec(line);
      var lst = parseList(i, lm[1].replace(/\t/g, "  ").length);
      if (lst){ out.push(lst.html); i = lst.next; continue; }
    }

    var para = [line];
    i++;
    while (i < lines.length && lines[i].trim() && !RE_PARA_STOP.test(lines[i])){
      para.push(lines[i].replace(/\s+$/,"")); i++;
    }
    out.push("<p>"+inline(para.join(" "))+"</p>");
  }
  return out.join("\n");
}

/* ==================== 素材页（source）布局 ====================
   一页 source 的自然形状是三段，不是一列：

       上款   标题 / 提要（一句话内容）/ 出处卡（作者·链接·路径）
       正文   关键要点 / 摘要 / 与本库的关系
       账目   分层表 / 引注核查表 / 归属判断 / 定级理由 / 回填清单

   旧版把三段平铺成同一种「## 标题 + 段落」，于是一张 40 行的行号表
   夹在「要点」和「摘要」之间。这里只做一件事：**给账目一个可折叠的边界**，
   默认收起。文字一个不删，只是不再挡路。

   不做「账目自动搬到页尾」：实测本库 sources 内有 330 处页内指向引用
   （见下 138 / 见上 38 / 下文 57 / 上表 16 / 下表 6 …），重排会让它们全部指错。
   置底做成用户自己按的开关，见 #ledgctl。 */

/* 账目章节判定表由 build 从 wiki.py 的 READ_EXACT / READ_H2 / LEDGER_H2 注入 —— 
   只此一份，不在 JS 里另抄。判定顺序即优先级：精确名 → 正文字串 → 账目子串 → 默认正文。 */
var READ_EXACT = __READ_EXACT__, READ_H2 = __READ_H2__, LEDGER_H2 = __LEDGER_H2__;

function classifyH2(title){
  var t = String(title).replace(/<[^>]+>/g, "").trim();
  for (var e = 0; e < READ_EXACT.length; e++) if (t === READ_EXACT[e]) return "read";
  for (var i = 0; i < READ_H2.length; i++) if (t.indexOf(READ_H2[i]) >= 0) return "read";
  for (var j = 0; j < LEDGER_H2.length; j++) if (t.indexOf(LEDGER_H2[j]) >= 0) return "ledger";
  return "read";
}

/* 成对标签的切片（要处理 <ul> 里再套 <ul>，正则数不出来） */
function cutTag(html, tag, from){
  var s = html.indexOf("<"+tag, from || 0);
  if (s < 0) return null;
  var re = new RegExp("<\\/?"+tag+"\\b[^>]*>", "g");
  re.lastIndex = s;
  var depth = 0, m;
  while ((m = re.exec(html))){
    if (m[0].charAt(1) === "/"){ depth--; if (!depth) break; } else depth++;
  }
  if (!m) return null;
  return { start: s, end: re.lastIndex, html: html.slice(s, re.lastIndex) };
}

function plainText(s){
  return String(s).replace(/<[^>]+>/g, " ").replace(/\u0000B\d+\u0000/g, " ")
                  .replace(/&[a-z]+;/g, " ").replace(/\s+/g, " ").trim();
}

/* 出处卡的数据来自**原文**而不是渲染后的 HTML。
   原文里的元信息常被「续行」打断（`- **素材路径**：…` 下一行缩进两格继续写），
   渲染成 HTML 后会被切成好几个 <ul> + 中间的 <p>。所以从 markdown 读，
   并且把缩进续行并回上一条 —— 否则「（1,701 行；frontmatter 1–68）」这类
   补充说明会变成悬在卡片外面的孤儿段落。 */
function provFromBody(body){
  var lines = String(body).split("\n"), items = [], keyed = 0;
  for (var i = 0; i < lines.length; i++){
    var L = lines[i];
    if (/^##\s/.test(L)) break;
    if (/^\s*>/.test(L) && !/^\s+\S/.test(L)) continue;   /* 顶格的引用是提要/警示，不是元信息 */
    if (/^\s*$/.test(L)){
      if (items.length && i + 1 < lines.length && /^\s+\S/.test(lines[i+1])) { items[items.length-1].v += "\n"; continue; }
      if (items.length) break;
      continue;
    }
    var m = /^[-*+]\s+\*\*(.+?)\*\*\s*[：:]\s*(.*)$/.exec(L);
    if (m){ items.push({ k:m[1].trim(), v:m[2] }); keyed++; continue; }
    if (/^\s+\S/.test(L) && items.length){                 /* 缩进续行 → 并回上一条 */
      items[items.length-1].v += (items[items.length-1].v ? "\n" : "") + L.trim();
      continue;
    }
    if (items.length) break;                                /* 顶格正文 = 元信息块结束 */
  }
  return keyed >= 2 ? items : null;
}

function provValue(it){
  if (it.raw) return it.v;                       /* 从提要抽出来的段落已经是 HTML */
  var v = it.v;
  /* 裸 URL 自动成链（本库 60 份素材的「链接」行大多是裸 URL，旧版是死文本） */
  if (v.indexOf("](") < 0) v = v.replace(/(^|[\s（(【])(https?:\/\/[^\s)）】]+)/g, "$1[$2]($2)");
  return render(v);
}

function renderProv(items){
  return '<div class="prov">' + items.map(function(it){
    return '<div class="pv'+(it.k ? "" : " wide")+'">' +
             (it.k ? '<span class="k">'+esc(it.k)+'</span>' : "") +
             '<span class="v">'+provValue(it)+'</span>' +
           '</div>';
  }).join("") + '</div>';
}

function sourceLayout(html, p){
  /* ① 切成「上款 + 每个 ## 一节」。
        在代码块还原之前做，所以正文里不可能出现 <h2> 字面量。 */
  var parts = html.split(/(?=<h2>)/);
  var head = parts.shift() || "";
  var secs = parts.map(function(chunk){
    var m = /^<h2>([\s\S]*?)<\/h2>/.exec(chunk);
    var inner = m ? m[1] : "";
    return {
      title: plainText(inner),
      inner: inner,
      body: m ? chunk.slice(m[0].length) : chunk,
      kind: classifyH2(plainText(inner))
    };
  });

  /* ② 提要：H1 之后的第一个引用块。
        同时把「本页坐标系」这类声明抽出来 —— 它 57 页都有，是**维护者需要、
        读者不需要**的元信息，却往往占提要一整段。抽走之后提要才是提要。 */
  var lb = cutTag(head, "blockquote"), coordRows = [];
  if (lb){
    var innerQ = lb.html.replace(/^<blockquote[^>]*>/, "").replace(/<\/blockquote>$/, "");
    var stripped = innerQ.replace(
      /<p><strong>(本页坐标系|行号坐标系|坐标声明)<\/strong>([：:]?[\s\S]*?)<\/p>/g,
      function(m, label, rest){
        coordRows.push({ k: label, v: rest.replace(/^\s*[：:]\s*/, ""), raw: true });
        return "";
      });
    /* 抽空了就退回去：宁可提要里留一段坐标系，也不能把提要抽成空白 */
    if (plainText(stripped).length >= 12) innerQ = stripped; else coordRows = [];
    head = head.slice(0, lb.start) +
           '<blockquote class="lead"><div class="lead-eb">提要</div>' + innerQ + '</blockquote>' +
           head.slice(lb.end);
  }

  /* ③ 出处卡：把「作者 / 链接 / 发表 / 素材路径」从一条普通 <ul> 里提出来。
        旧版这几行和一条普通要点长得完全一样 —— 而它们回答的是
        「这是什么东西、谁写的、原文在哪」，是整页最该被一眼看到的信息。

        元信息块常被续行切成好几截（<ul> … <p>…</p> … <ul>），所以取的是
        「提要之后的第一个 <ul>」到「最后一个 <ul>」这一整段，中间的续行段落
        一并收走 —— 否则那些补充说明会变成悬在卡片外的孤儿。
        校验用「所有标签名都在这一段里出现」，不靠数 <li>：数量对不上就原样保留，
        绝不吞掉内容。 */
  var pv = provFromBody(p.body), provHtml = "";
  if (pv){
    var from = lb ? lb.end : 0, uls = [], c;
    while ((c = cutTag(head, "ul", from))){ uls.push(c); from = c.end; }
    if (uls.length){
      var rs = uls[0].start, re2 = uls[uls.length-1].end;
      var seg = plainText(head.slice(rs, re2));
      var keys = pv.filter(function(it){ return it.k; });
      var hit = keys.filter(function(it){ return seg.indexOf(it.k) >= 0; }).length;
      if (hit >= 2 && hit === keys.length) head = head.slice(0, rs) + head.slice(re2);
      else pv = null;
    } else pv = null;
  }
  if (pv && coordRows.length) pv = pv.concat(coordRows);
  else if (coordRows.length) pv = coordRows;
  if (pv) provHtml = renderProv(pv);

  /* ④ 逐节包装 */
  var out = [];
  secs.forEach(function(s){
    var isProv = (s.title === "来源");
    var isKey = /^(关键)?要点$/.test(s.title) || s.title.indexOf("关键要点") === 0;
    /* 全部顶层 <ol> 都要拿悬挂序号，不能只replace第一个 ——
       一个「关键要点」节里常有被段落打断成两段的编号表（dunlosky 就是），
       只改第一个会让第二段退回浏览器默认的深色行内标号。 */
    if (isKey) s.body = s.body.replace(/<ol>/g, '<ol class="keypoints">');
    if (isProv){
      out.push('<section class="sec prov-sec"><h2>'+s.inner+'</h2>'+s.body+'</section>');
      return;
    }
    if (s.kind === "ledger"){
      var peek = plainText(s.body);
      if (peek.length > 96) peek = peek.slice(0, 96) + "…";
      out.push('<section class="sec ledger collapsed" data-kind="ledger">' +
                 '<h2>'+s.inner+'</h2>' +
                 '<div class="lg-bd">'+s.body+'</div>' +
                 (peek ? '<p class="lg-peek">'+esc(peek)+'</p>' : "") +
               '</section>');
      return;
    }
    out.push('<section class="sec" data-kind="read"><h2>'+s.inner+'</h2>'+s.body+'</section>');
  });

  /* 出处卡插在提要之后（没有提要则紧跟标题） */
  if (provHtml){
    if (/<\/blockquote>/.test(head)) head = head.replace(/<\/blockquote>/, "</blockquote>\n"+provHtml);
    else if (/<\/h1>/.test(head)) head = head.replace(/<\/h1>/, "</h1>\n"+provHtml);
    else head = head + provHtml;
  }
  return head + "\n" + out.join("\n");
}

/* 整页渲染：递归共享同一个代码块池，最后一次性还原 */
function renderPage(p){
  _codePool = [];
  var html = render(p.body);
  if (p.type === "source") html = sourceLayout(html, p);
  return html.replace(/\u0000B(\d+)\u0000/g, function(m, n){ return _codePool[+n]; });
}
/* ---------------- nav ---------------- */
var ORDER = ["project","meta","source","entity","concept","analysis"];
var nav = document.getElementById("nav");
var COLLAPSE_MIN = 8;    /* 一级组超过这个页数默认折叠 —— 让 6 个组头一屏看全 */
var FIND_MIN = 20;       /* 组内页数达到这个量级才挂筛选框，小复组不必多一层控件 */
var LS_KEY = "llmwiki.navstate";

function loadState(){ try { return JSON.parse(localStorage.getItem(LS_KEY) || "{}") || {}; } catch(e){ return {}; } }
function saveState(){
  try {
    var s = {}, els = nav.querySelectorAll("[data-key]");
    for (var i = 0; i < els.length; i++) s[els[i].dataset.key] = els[i].classList.contains("collapsed");
    localStorage.setItem(LS_KEY, JSON.stringify(s));
  } catch(e){}
}

/* 组内筛选。二级分类按 tag 切过一版，结论是不可用：一页平均 5.6 个 tag，互斥归类必然错配，
   用户拿到的是「猜错的分组 + 折叠状态」两层额外成本。改成让用户自己输入关键词收敛。
   匹配面 = 标题 + slug + tags，比只匹配标题宽容一档，且不隐藏「为什么它在这儿」。 */
function filterGroup(g, body, q){
  q = (q || "").trim().toLowerCase();
  var links = body.querySelectorAll(".nav-item"), hit = 0;
  for (var i = 0; i < links.length; i++){
    var p = BYSLUG[links[i].dataset.slug];
    var hay = p ? (p.title + " " + p.slug + " " + (p.tags || []).join(" ")).toLowerCase() : "";
    var ok = !q || hay.indexOf(q) >= 0;
    links[i].hidden = !ok;
    if (ok) hit++;
  }
  body.querySelector(".grpempty").hidden = hit > 0;
  var box = body.querySelector(".gfbox"), n = box.querySelector(".fcount");
  box.classList.toggle("on", !!q);
  n.textContent = hit + "/" + links.length;
  n.hidden = !q;
}

function groupOf(el){ return el.closest ? el.closest(".grp") : null; }

function setAllGroups(collapsed){
  [].forEach.call(nav.querySelectorAll(".grp[data-key]"), function(g){
    g.classList.toggle("collapsed", collapsed);
  });
  saveState();
}

function mkLink(p){
  var a = document.createElement("a");
  a.className = "nav-item"; a.href = "#" + p.slug; a.dataset.slug = p.slug;
  a.title = p.title;
  /* 每个条目都带类型点（含 meta）—— 组内没有二级标题，颜色点是唯一的类型提示；
     缺了它，系统组的条目会比别的组整体左移 14px。 */
  a.innerHTML = '<i class="dot" style="background:' + (TYPECOLOR[p.type] || "#999") + '"></i>' +
                '<span class="t">' + esc(p.title) + '</span>';
  return a;
}

function buildNav(){
  var st = loadState();
  nav.innerHTML = "";
  ORDER.forEach(function(t){
    var items = PAGES.filter(function(p){ return p.type === t; });
    if (!items.length) return;
    var key = "t:" + t;
    var g = document.createElement("div"); g.className = "grp"; g.dataset.key = key;
    var collapsed = (st[key] === undefined) ? (items.length > COLLAPSE_MIN) : !!st[key];
    if (collapsed) g.classList.add("collapsed");

    var h = document.createElement("h3");
    h.innerHTML = '<span class="gl"><span class="caret">▾</span>' +
                  '<span class="gtxt">' + esc(TYPELABEL[t] || t) + '</span></span>' +
                  '<span class="n">' + items.length + '</span>';
    g.appendChild(h);

    var body = document.createElement("div"); body.className = "grpbody";
    if (items.length >= FIND_MIN){
      var fi = document.createElement("input");
      fi.type = "text"; fi.autocomplete = "off";
      fi.placeholder = "在「" + (TYPELABEL[t] || t) + "」内筛选…";
      fi.addEventListener("input", function(){ filterGroup(g, body, fi.value); });
      var fc = document.createElement("span"); fc.className = "fcount"; fc.hidden = true;
      var box = document.createElement("div"); box.className = "gfbox";
      box.appendChild(fi); box.appendChild(fc);
      var fw = document.createElement("div"); fw.className = "grpfind";
      fw.appendChild(box); body.appendChild(fw);
    }
    var list = document.createElement("div"); list.className = "grplist";
    items.forEach(function(p){ list.appendChild(mkLink(p)); });
    body.appendChild(list);
    var emp = document.createElement("div");
    emp.className = "grpempty"; emp.textContent = "没有匹配的页面"; emp.hidden = true;
    body.appendChild(emp);

    g.appendChild(body);
    nav.appendChild(g);
  });
}

/* 事件委托：384 个条目各挂一个 listener 是浪费，也拖慢重建。
   h3 只在一级分组上生效（搜索结果那块 h3 没有 data-key，自然不响应折叠）。 */
nav.addEventListener("click", function(e){
  var h = e.target.closest ? e.target.closest("h3") : null;
  if (h){
    var box = h.parentNode;
    if (box.dataset.key){ box.classList.toggle("collapsed"); saveState(); }
    return;
  }
  var a = e.target.closest ? e.target.closest(".nav-item") : null;
  if (a && a.dataset.slug){ e.preventDefault(); go(a.dataset.slug); closeDrawer(); }
});

function markActive(slug){
  [].forEach.call(nav.querySelectorAll(".nav-item"), function(el){
    el.classList.toggle("active", el.dataset.slug === slug);
  });
}

/* 从搜索结果或反向链接跳进来时，目标可能躺在折叠组里（或被组内筛选挡住）—— 先把它变可见 */
function revealActive(slug){
  var a = nav.querySelector('.nav-item[data-slug="' + slug + '"]');
  if (!a) return;
  var g = a.closest(".grp");
  if (!g) return;
  if (a.hidden){
    var fi = g.querySelector(".grpfind input");
    if (fi){ fi.value = ""; filterGroup(g, g.querySelector(".grpbody"), ""); }
  }
  if (g.classList.contains("collapsed")){ g.classList.remove("collapsed"); saveState(); }
  try { a.scrollIntoView({ block: "nearest" }); } catch(e){}
}

/* ---------------- page ---------------- */
var pageEl = document.getElementById("page");
var blEl = document.getElementById("backlinks");
var tabmeta = document.getElementById("tabmeta");
var vb = document.getElementById("view-browse");

/* ---------------- TOC ---------------- */
/* 长页（本库最长 46KB）没有目录等于没有地图。标题少于 3 个时不显示，避免噪音。
   素材页的目录**分两组**：正文目录 / 账目目录。一页 source 有 5-8 个账目章节，
   平铺会把正文目录冲没 —— 而正文才是来这页要读的东西。 */
var tocEl = document.getElementById("toc");
var tocHs = [], tocRaf = 0, tocLedgerFrom = -1;

function tocScrollTo(h){
  /* 不用 offsetTop：章节被 <section> 包起来之后 offsetParent 变成了 body，
     offsetTop 不再等于「相对滚动容器的距离」。直接用矩形差，跟 DOM 结构解耦。 */
  var lg = h.closest ? h.closest("section.ledger") : null;
  if (lg && lg.classList.contains("collapsed")) lg.classList.remove("collapsed");
  var top = h.getBoundingClientRect().top - vb.getBoundingClientRect().top + vb.scrollTop;
  vb.scrollTo({ top: top - 18, behavior: "smooth" });
}

function buildToc(root){
  tocHs = [].slice.call(root.querySelectorAll("h2,h3"));
  tocEl.hidden = tocHs.length < 3;          /* 少于 3 个标题的页不值得挂目录 */
  if (tocHs.length < 3){ tocEl.innerHTML = ""; return; }
  tocHs.forEach(function(h, i){ if (!h.id) h.id = "sec-" + i; });

  var read = [], ledger = [];
  tocHs.forEach(function(h, i){
    var rec = { i: i, h: h };
    (h.closest && h.closest("section.ledger") ? ledger : read).push(rec);
  });
  var link = function(r){
    return '<a class="' + (r.h.tagName === "H3" ? "lv3" : "") + '" href="#" data-i="' + r.i + '">' +
           esc(r.h.textContent) + '</a>';
  };
  var html = "";
  if (read.length) html += read.map(link).join("");
  if (ledger.length){
    html += '<div class="tg-ledger"><span class="tglbl">账目 ' + ledger.length + '</span>' +
            ledger.map(link).join("") + '</div>';
  }
  tocEl.innerHTML = html;
  tocLedgerFrom = read.length ? 1 : 0;      /* 仅用于统计，不参与逻辑 */
  [].forEach.call(tocEl.querySelectorAll("a"), function(a){
    a.addEventListener("click", function(e){
      e.preventDefault();
      var h = tocHs[+a.dataset.i];
      if (h) tocScrollTo(h);
    });
  });
  updateToc();
}

function updateToc(){
  if (!tocHs.length) return;
  var cur = -1;
  for (var i = 0; i < tocHs.length; i++){
    if (tocHs[i].getBoundingClientRect().top <= 110) cur = i; else break;
  }
  [].forEach.call(tocEl.querySelectorAll("a"), function(a, i){
    a.classList.toggle("on", +a.dataset.i === cur);
  });
  var h = pageEl.offsetHeight - vb.clientHeight;
  var pct = h > 40 ? Math.min(100, Math.max(0, vb.scrollTop / h * 100)) : 0;
  progEl.style.width = pct + "%";
}

/* ---------------- 账目模式 ---------------- */
/* 原地折叠是默认：不改章节顺序，所以 330 处「见下 / 见上 / 上表」全部仍然成立。
   置底是给「想一口气读完正文」的人准备的开关，不是默认行为。 */
var LG_KEY = "llmwiki.ledger";
var ledgctl = document.getElementById("ledgctl");
var progEl = document.getElementById("prog");
var lgMode = "collapse";
try { lgMode = localStorage.getItem(LG_KEY) || "collapse"; } catch(e){}

function markLedgerButtons(){
  [].forEach.call(ledgctl.querySelectorAll("button"), function(b){
    b.classList.toggle("on", b.dataset.lg === lgMode);
  });
}

function applyLedgerMode(){
  var secs = [].slice.call(pageEl.querySelectorAll("section.ledger"));
  ledgctl.hidden = secs.length === 0;
  if (!secs.length) return;
  if (lgMode === "end"){
    var anchor = pageEl.querySelector("section.prov-sec");
    secs.forEach(function(s){
      s.classList.add("collapsed");
      if (anchor) pageEl.insertBefore(s, anchor); else pageEl.appendChild(s);
    });
  } else {
    /* 还原必须**按 idx 降序**：每个账目章节要插回它的原始后继 __next 之前，
       而那个后继通常正是下一个账目章节 —— 先还原后面的，前面的插入点才是
       已经归位的节点。升序还原会把第一个账目章节留在页尾
       （用纯数组模型跑过：升序得到「关键要点, 核查表, 适用边界, … 分层表, 来源」）。 */
    secs.slice().sort(function(a, b){ return (+b.dataset.idx) - (+a.dataset.idx); })
        .forEach(function(s){
          s.classList.toggle("collapsed", lgMode === "collapse");
          if (s.__next && s.__next.parentNode === pageEl) pageEl.insertBefore(s, s.__next);
          else pageEl.appendChild(s);
        });
  }
  markLedgerButtons();
}

ledgctl.addEventListener("click", function(e){
  var b = e.target.closest ? e.target.closest("button") : null;
  if (!b) return;
  lgMode = b.dataset.lg;
  try { localStorage.setItem(LG_KEY, lgMode); } catch(e2){}
  applyLedgerMode();
});

vb.addEventListener("scroll", function(){
  if (tocRaf) return;
  tocRaf = requestAnimationFrame(function(){ tocRaf = 0; updateToc(); });
});

function go(slug){
  var p = BYSLUG[slug];
  if (!p){ return; }
  location.hash = slug;
  var chips = '<span class="chip t" style="background:'+(TYPECOLOR[p.type]||"#666")+'">'+
              (TYPELABEL[p.type]||p.type)+'</span>';
  if (p.status && p.status !== "active") chips += '<span class="chip stale">'+p.status+'</span>';
  if (p.updated) chips += '<span class="chip">更新 '+p.updated+'</span>';
  if (p.sources && p.sources.length) chips += '<span class="chip">来源 '+p.sources.length+'</span>';
  (p.tags||[]).forEach(function(t){ chips += '<span class="chip tag">#'+esc(t)+'</span>'; });

  pageEl.className = "ptype-" + p.type;
  pageEl.innerHTML = '<div class="pagemeta">'+chips+'</div>' + renderPage(p);

  /* 记下账目章节的原始位置，供「回到原位」使用 */
  [].forEach.call(pageEl.querySelectorAll("section.ledger"), function(s, i){
    s.dataset.idx = i; s.__next = s.nextElementSibling;
  });
  /* 点账目章节头 = 展开 / 收起**这一张**。
     刻意不改 lgMode：模式按钮描述的是「整页怎么排」，单卡点开是临时动作 ——
     把它写回 localStorage 会让下一张页面莫名其妙地全部展开。 */
  [].forEach.call(pageEl.querySelectorAll("section.ledger > h2"), function(h){
    h.addEventListener("click", function(){
      h.parentNode.classList.toggle("collapsed");
    });
  });
  applyLedgerMode();

  [].forEach.call(pageEl.querySelectorAll("a.wl"), function(a){
    a.addEventListener("click", function(e){ e.preventDefault(); go(a.dataset.slug); });
  });

  var bl = DATA.backlinks[slug] || [];
  if (bl.length){
    blEl.style.display = "block";
    blEl.innerHTML = "<h4>反向链接 ("+bl.length+")</h4>" +
      bl.map(function(s){
        var q = BYSLUG[s];
        return '<a href="#'+s+'" data-slug="'+s+'">'+esc(q?q.title:s)+'</a>';
      }).join("");
    [].forEach.call(blEl.querySelectorAll("a"), function(a){
      a.addEventListener("click", function(e){ e.preventDefault(); go(a.dataset.slug); });
    });
  } else {
    blEl.style.display = "none";
  }

  tabmeta.textContent = p.relpath;
  markActive(slug); revealActive(slug);
  vb.scrollTop = 0;
  buildToc(pageEl);
  document.title = p.title + " · " + DATA.title;
}
/* ---------------- search ---------------- */
/* 打分与 `tools/wiki.py search` 同为 BM25。站点侧在此之上做了三处修正，都是 376 页规模逼出来的：
   ① 候选收敛 —— 先只用「有区分度的词」圈定候选集。旧版是二字组 OR，
      「注意力机制」被切成 注意/意力/力机/机制，「机制」满库都是，结果命中 309/376 页，等于没搜。
   ② 最长命中加成 —— 命中完整短语的页必须压过只命中碎片的页，否则长文档靠词频霸榜。
   ③ 系统页降权 —— log / index 这类系统页不该占前排。 */
var CJK_TEST = /[\u4e00-\u9fff]/;
var STOP_RATIO = 0.30;     /* 出现在超过 30% 页面里的词视为噪声词，不参与收敛候选 */
var META_DEMOTE = 0.55;

/* 一次性预处理：小写文本 + 文档长度 */
var NDOC = PAGES.length, AVGDL = 0;
PAGES.forEach(function(p){
  p._h = (p.title + " " + (p.tags||[]).join(" ") + " " + p.slug).toLowerCase();
  p._b = p.body.toLowerCase();
  p._dl = p.body.length;
  AVGDL += p._dl;
});
AVGDL = AVGDL / (NDOC || 1);

var DFCACHE = {};
function dfOf(t){
  if (DFCACHE[t] !== undefined) return DFCACHE[t];
  var c = 0;
  for (var i = 0; i < NDOC; i++){
    if (PAGES[i]._b.indexOf(t) >= 0 || PAGES[i]._h.indexOf(t) >= 0) c++;
  }
  DFCACHE[t] = c; return c;
}
function countOf(s, t){
  var c = 0, i = s.indexOf(t);
  while (i >= 0){ c++; i = s.indexOf(t, i + t.length); if (c > 400) break; }
  return c;
}

/* 分层切词：整串 → 逐级降长的子串。整串排在最前，后面 ① 会优先拿它去收敛。 */
function splitFragments(raw){
  return raw.split(/[\s,，、;；:：()（）\/]+/).filter(function(s){ return s.length > 0; });
}
function termsOf(raw){
  var out = [], seen = {};
  function add(t){ if (!seen[t]){ seen[t] = 1; out.push(t); } }
  splitFragments(raw).forEach(function(f){
    if (CJK_TEST.test(f)){
      add(f);
      for (var L = Math.min(f.length - 1, 6); L >= 2; L--)
        for (var i = 0; i + L <= f.length; i++) add(f.substr(i, L));
    } else add(f);
  });
  return out;
}
function hl(text, needles){
  var lc = text.toLowerCase(), ranges = [];
  needles.forEach(function(n){
    if (!n) return;
    var i = lc.indexOf(n), guard = 0;
    while (i >= 0 && guard++ < 40){ ranges.push([i, i + n.length]); i = lc.indexOf(n, i + n.length); }
  });
  if (!ranges.length) return esc(text);
  ranges.sort(function(a, b){ return a[0] - b[0]; });
  var merged = [];
  ranges.forEach(function(r){
    var last = merged[merged.length - 1];
    if (last && r[0] <= last[1]) last[1] = Math.max(last[1], r[1]); else merged.push([r[0], r[1]]);
  });
  var out = "", pos = 0;
  merged.forEach(function(r){
    out += esc(text.slice(pos, r[0])) + "<mark>" + esc(text.slice(r[0], r[1])) + "</mark>";
    pos = r[1];
  });
  return out + esc(text.slice(pos));
}
function snippet(p, needles){
  var b = p._b, cands = [];
  for (var i = 0; i < needles.length; i++){
    var n = needles[i], from = 0, k, guard = 0;
    while ((k = b.indexOf(n, from)) >= 0 && guard++ < 60){ cands.push(k); from = k + n.length; }
  }
  if (!cands.length) return "";
  cands.sort(function(x, y){ return x - y; });
  var best = cands[0];
  /* 命中落在开头标题行时意义不大 —— 往正文里挪一处 */
  for (var j = 0; j < cands.length; j++){ if (cands[j] > 80){ best = cands[j]; break; } }
  var start = Math.max(0, best - 34), end = Math.min(p.body.length, best + 130);
  var txt = p.body.slice(start, end)
    .replace(/\s+/g, " ")
    .replace(/^#+\s+/, "")
    .replace(/>\s?/g, "")
    .replace(/\*\*/g, "")
    .replace(/\[\[([^\]\|]+)(?:\|[^\]]+)?\]\]/g, "$1")
    .replace(/\[([^\]]+)\]\([^)]*\)/g, "$1")
    .replace(/\[!\w+\]/g, "")
    .replace(/\[\[|\]\]/g, "")
    .replace(/\|/g, " ")
    .replace(/\s*-{3,}\s*/g, " ")
    .replace(/\s{2,}/g, " ")
    .replace(/^\s*[-*+]\s+/, "");
  return (start > 0 ? "…" : "") + hl(txt, needles) + (end < p.body.length ? "…" : "");
}

var searchEl = document.getElementById("search");
var SEARCH_CAP = 30, WIDE_AT = 60, lastHits = [], lastNeedles = [], lastMode = "";
var lastRaw = "", lastExactMiss = false;

function renderHits(cap){
  var top = lastHits.length ? lastHits[0].s : 0;
  /* 阈值：低于最高分 25% 的长尾视为噪声，不默认展示（可展开）。
     旧版用 18%，在 376 页规模下会把上百条弱相关一起放出来。 */
  var shown = lastHits.filter(function(x){ return x.s >= Math.max(1.2, top * 0.25); });
  nav.innerHTML = "";
  var g = document.createElement("div"); g.className = "grp";
  if (!shown.length){
    g.innerHTML = "<h3>搜索结果<span>0</span></h3>";
    var d = document.createElement("div"); d.className = "res-count"; d.textContent = "无匹配页面";
    g.appendChild(d); nav.appendChild(g); return;
  }
  g.innerHTML = "<h3>搜索结果<span>" + shown.length + "</span></h3>";
  /* 整串在库里一次都没出现过 —— 明说。否则「搜了个不存在的词却出来 116 条」会让人误判为搜到了 */
  if (lastExactMiss){
    var em = document.createElement("div"); em.className = "res-tip";
    em.textContent = "「" + lastRaw + "」在本库没有完整匹配，以下是分词命中的近似结果，相关度普遍偏低。";
    g.appendChild(em);
  } else if (shown.length > WIDE_AT){
    /* 候选过宽时也明说，而不是让用户在一百条弱相关里自己捞 */
    var tip = document.createElement("div"); tip.className = "res-tip";
    tip.textContent = "命中 " + shown.length + " 页，结果过宽。这一 query 的词在本库过于常见，补充更具体的词会显著收敛。";
    g.appendChild(tip);
  }
  shown.slice(0, cap).forEach(function(x){
    var p = x.p, sn = snippet(p, lastNeedles);
    var a = document.createElement("a");
    a.className = "nav-item res"; a.href = "#" + p.slug; a.dataset.slug = p.slug;
    a.innerHTML = '<i class="dot" style="background:' + (TYPECOLOR[p.type]||"#666") + '"></i>' +
      '<span class="r-title">' + hl(p.title, lastNeedles) + '</span>' +
      (sn ? '<span class="r-snip">' + sn + '</span>' : '') +
      '<span class="r-meta">' + (TYPELABEL[p.type]||p.type) + ' · 相关度 ' + x.s.toFixed(1) + '</span>';
    g.appendChild(a);
  });
  if (shown.length > cap){
    var more = document.createElement("button");
    more.className = "res-more";
    more.textContent = "显示其余 " + (shown.length - cap) + " 条较弱结果";
    more.addEventListener("click", function(){ renderHits(shown.length); });
    g.appendChild(more);
  }
  nav.appendChild(g);
  markActive((location.hash||"#").slice(1));
}

function runSearch(){
  var raw = searchEl.value.trim().toLowerCase();
  if (!raw){ buildNav(); markActive((location.hash||"#").slice(1)); revealActive((location.hash||"#").slice(1)); return; }
  lastRaw = raw;

  var terms = termsOf(raw).map(function(t){ return { t: t, df: dfOf(t) }; })
                          .filter(function(x){ return x.df > 0; });
  var fragsAll = splitFragments(raw);
  lastExactMiss = fragsAll.length > 0 && fragsAll.every(function(f){ return dfOf(f) === 0; });
  if (!terms.length){ lastHits = []; lastNeedles = []; renderHits(SEARCH_CAP); return; }

  /* ① 候选收敛 */
  var discr = terms.filter(function(x){ return x.df / NDOC <= STOP_RATIO; });
  var cand, mode;
  if (discr.length){
    mode = "收敛";
    cand = PAGES.filter(function(p){
      return discr.some(function(x){ return p._b.indexOf(x.t) >= 0 || p._h.indexOf(x.t) >= 0; });
    });
  } else {
    /* 全部词都是高频词（例如「为什么」）——退化到最长片段的整串命中 */
    mode = "短语";
    var longest = terms.slice().sort(function(a, b){ return b.t.length - a.t.length; })[0];
    cand = PAGES.filter(function(p){
      return p._b.indexOf(longest.t) >= 0 || p._h.indexOf(longest.t) >= 0;
    });
  }

  var frags = splitFragments(raw).filter(function(f){ return f.length >= 2; });
  var scored = cand.map(function(p){
    var s = 0, maxLen = 0;
    terms.forEach(function(x){
      var f = countOf(p._b, x.t) + countOf(p._h, x.t) * 3;   /* 标题/标签命中加权 */
      if (!f) return;
      if (x.t.length > maxLen) maxLen = x.t.length;
      var df = x.df || 1, idf = Math.log(1 + (NDOC - df + 0.5) / (df + 0.5));
      s += idf * (f * 2.5) / (f + 1.5 * (1 - 0.75 + 0.75 * p._dl / AVGDL));
    });
    s += maxLen * 3.5;                                        /* ② 最长命中加成 */
    if (p.title.toLowerCase().indexOf(raw) >= 0) s += 30;
    else if (frags.some(function(f){ return p.title.toLowerCase().indexOf(f) >= 0; })) s += 16;
    if (p.type === "meta") s *= META_DEMOTE;                  /* ③ 系统页降权 */
    return { p: p, s: s };
  }).filter(function(x){ return x.s > 0; });
  scored.sort(function(a, b){ return b.s - a.s; });

  lastHits = scored;
  lastNeedles = terms.map(function(x){ return x.t; });
  lastMode = mode;
  renderHits(SEARCH_CAP);
}
var sTimer = null;
searchEl.addEventListener("input", function(){
  syncClear();
  if (sTimer) clearTimeout(sTimer);
  sTimer = setTimeout(runSearch, 110);
});
searchEl.addEventListener("keydown", function(e){
  if (e.key === "Escape"){ searchEl.value = ""; syncClear(); runSearch(); }
});

/* 清空按钮：只在有字时露出，避免空框里挂一个永远按不动的控件 */
var clearBtn = document.getElementById("searchclear");
function syncClear(){ clearBtn.classList.toggle("on", searchEl.value.length > 0); }
clearBtn.addEventListener("click", function(){
  searchEl.value = ""; syncClear(); runSearch(); searchEl.focus();
});
/* j/k 或 ↑↓ 在当前可见列表里前后翻页。搜索框聚焦时不抢键。 */
function stepNav(d){
  var list = [].filter.call(nav.querySelectorAll(".nav-item"), function(el){ return !el.hidden; });
  if (!list.length) return;
  var cur = (location.hash || "#").slice(1), i = -1;
  for (var k = 0; k < list.length; k++){ if (list[k].dataset.slug === cur){ i = k; break; } }
  var n = list[Math.max(0, Math.min(list.length - 1, i + d))];
  if (n){ go(n.dataset.slug); try { n.scrollIntoView({ block: "nearest" }); } catch(e){} }
}
document.addEventListener("keydown", function(e){
  var tag = document.activeElement ? document.activeElement.tagName : "";
  var typing = /^(INPUT|TEXTAREA)$/.test(tag);
  if (e.key === "/" && !typing){
    e.preventDefault(); searchEl.focus(); searchEl.select(); return;
  }
  if (e.key === "Escape"){ closeDrawer(); return; }
  if (typing) return;
  if (e.key === "j" || e.key === "ArrowDown"){ e.preventDefault(); stepNav(1); }
  else if (e.key === "k" || e.key === "ArrowUp"){ e.preventDefault(); stepNav(-1); }
});

/* ---------------- tabs ---------------- */
var canvas = document.getElementById("canvas");
var sidebar = document.getElementById("sidebar"), mask = document.getElementById("mask");
function openDrawer(){ sidebar.classList.add("open"); mask.classList.add("on"); }
function closeDrawer(){ sidebar.classList.remove("open"); mask.classList.remove("on"); }
document.getElementById("burger").addEventListener("click", function(){
  sidebar.classList.contains("open") ? closeDrawer() : openDrawer();
});
mask.addEventListener("click", closeDrawer);

/* 选择器必须限定 [data-view]：否则汉堡按钮会被当成视图切换键，点了会切走 browse */
[].forEach.call(document.querySelectorAll("#tabs button[data-view]"), function(b){
  b.addEventListener("click", function(){
    [].forEach.call(document.querySelectorAll("#tabs button[data-view]"), function(x){ x.classList.remove("active"); });
    b.classList.add("active");
    var v = b.dataset.view;
    document.getElementById("view-browse").hidden = (v !== "browse");
    document.getElementById("view-graph").hidden = (v !== "graph");
    tocEl.hidden = (v !== "browse") || tocHs.length < 3;   /* 图谱页不该挂着正文目录 */
    if (v === "graph") startGraph();
    else closeDrawer();
  });
});

/* ---------------- graph ---------------- */
var G = { nodes: [], edges: [], built: false, scale: 1, ox: 0, oy: 0, drag: null };
var ctx = canvas.getContext("2d");

function startGraph(){
  resize();
  /* buildGraph 内部以分帧方式算布局，此处不能再调 fitGraph/draw，否则会画到未收敛的坐标 */
  if (!G.built) buildGraph();
  else { fitGraph(); draw(); }
}

function radius(n){ return 4 + Math.min(9, n.deg * 1.5); }

function buildGraph(){
  /* meta 页是导航件而非知识节点，不进入图谱 —— 否则无边的它们会飘到外圈撑大包围盒 */
  var nodes = PAGES.filter(function(p){ return p.type !== "meta"; }).map(function(p){
    return { slug: p.slug, title: p.title, type: p.type, deg: 0, x: 0, y: 0, vx: 0, vy: 0 };
  });
  var index = {}; nodes.forEach(function(n, i){ index[n.slug] = i; });
  var edges = [];
  PAGES.forEach(function(p){
    if (p.type === "meta") return;
    (p.links||[]).forEach(function(t){
      if (t !== p.slug && index[t] !== undefined){
        edges.push([index[p.slug], index[t]]);
        nodes[index[p.slug]].deg++; nodes[index[t]].deg++;
      }
    });
  });
  var W = canvas.clientWidth || 900, H = canvas.clientHeight || 600;
  var R = Math.min(W,H)*0.40;
  nodes.forEach(function(n, i){
    var a = i / nodes.length * Math.PI * 2;
    n.x = W/2 + Math.cos(a)*R;
    n.y = H/2 + Math.sin(a)*R;
  });
  G.nodes = nodes; G.edges = edges; G.built = true;
  var legend = document.getElementById("legend");
  legend.innerHTML = ["project","source","entity","concept","analysis"].map(function(t){
    return '<div><i style="background:'+TYPECOLOR[t]+'"></i>'+TYPELABEL[t]+'</div>';
  }).join("");
  relaxAsync(700);
}

/* 370 节点 × 700 步的 O(n²) 力导向实测 265ms，同步跑会结结实实卡一次主线程。
   切成 24 帧边算边画：用户看到的是布局收敛的过程，而不是一段白屏。 */
function relaxAsync(steps, done){
  var FRAMES = 36;                                   /* 每帧 ~10ms，压在 60fps 预算内 */
  var per = Math.max(12, Math.ceil(steps / FRAMES)), s = 0;
  (function frame(){
    relax(Math.min(per, steps - s));
    s += per;
    fitGraph(); draw();
    if (s < steps) requestAnimationFrame(frame);
    else if (done) done();
  })();
}

function resize(){
  var dpr = window.devicePixelRatio || 1;
  canvas.width = canvas.clientWidth * dpr;
  canvas.height = canvas.clientHeight * dpr;
  ctx.setTransform(dpr,0,0,dpr,0,0);
}

var MAX_F = 60;      /* 斥力上限 */
var MAX_STEP = 14;   /* 单步位移上限 */

function clampStep(v, m){ return v > m ? m : (v < -m ? -m : v); }

/* 坐标发散的最后防线：真的炸了就复位成环形重排，总好过整张图画不出来 */
function sanitizeGraph(){
  var i, ok = true;
  for (i = 0; i < G.nodes.length; i++){
    if (!isFinite(G.nodes[i].x) || !isFinite(G.nodes[i].y)){ ok = false; break; }
  }
  if (ok) return false;
  var W = canvas.clientWidth || 900, H = canvas.clientHeight || 600;
  var R = Math.min(W, H) * 0.40;
  for (i = 0; i < G.nodes.length; i++){
    var a = i / G.nodes.length * Math.PI * 2;
    G.nodes[i].x = W/2 + Math.cos(a) * R;
    G.nodes[i].y = H/2 + Math.sin(a) * R;
    G.nodes[i].vx = 0; G.nodes[i].vy = 0;
  }
  return true;
}

function relax(steps){
  var nodes = G.nodes, edges = G.edges, n = nodes.length;
  var W = canvas.clientWidth || 900, H = canvas.clientHeight || 600;
  for (var s=0; s<steps; s++){
    var i, j, a, b, dx, dy, d2, d, ux, uy, f;
    for (i=0;i<n;i++){
      a = nodes[i];
      for (j=i+1;j<n;j++){
        b = nodes[j];
        dx = b.x-a.x; dy = b.y-a.y;
        d2 = dx*dx+dy*dy || 0.01; d = Math.sqrt(d2);
        f = 26000 / d2;
        /* 不设上限时，403 个节点挤在初始圆上会让合力指数发散：
           实测每 5 步放大约 2 万倍，700 步后溢出成 NaN，整张图画不出来。 */
        if (f > MAX_F) f = MAX_F;
        ux = dx/d; uy = dy/d;
        a.vx -= ux*f; a.vy -= uy*f; b.vx += ux*f; b.vy += uy*f;
      }
    }
    for (i=0;i<edges.length;i++){
      a = nodes[edges[i][0]]; b = nodes[edges[i][1]];
      dx = b.x-a.x; dy = b.y-a.y;
      d = Math.sqrt(dx*dx+dy*dy) || 0.01;
      f = (d - 168) * 0.03;
      ux = dx/d; uy = dy/d;
      a.vx += ux*f; a.vy += uy*f; b.vx -= ux*f; b.vy -= uy*f;
    }
    for (i=0;i<n;i++){
      a = nodes[i];
      a.vx = (a.vx + (W/2 - a.x) * 0.0012) * 0.78;
      a.vy = (a.vy + (H/2 - a.y) * 0.0012) * 0.78;
      if (a !== G.drag){
        a.x += clampStep(a.vx, MAX_STEP);
        a.y += clampStep(a.vy, MAX_STEP);
      }
    }
    /* 硬性去重叠：保证节点之间留得下标签 */
    for (i=0;i<n;i++){
      a = nodes[i];
      for (j=i+1;j<n;j++){
        b = nodes[j];
        dx = b.x-a.x; dy = b.y-a.y;
        d = Math.sqrt(dx*dx+dy*dy) || 0.01;
        var need = radius(a) + radius(b) + 58;
        if (d < need){
          var push = (need - d) / 2;
          ux = dx/d; uy = dy/d;
          if (a !== G.drag){ a.x -= ux*push; a.y -= uy*push; }
          if (b !== G.drag){ b.x += ux*push; b.y += uy*push; }
        }
      }
    }
  }
  sanitizeGraph();
}

function fitGraph(){
  if (!G.nodes.length) return;
  var pad = 58;
  var minX=1e9, maxX=-1e9, minY=1e9, maxY=-1e9;
  G.nodes.forEach(function(n){
    minX = Math.min(minX, n.x - radius(n) - pad);
    maxX = Math.max(maxX, n.x + radius(n) + pad);
    minY = Math.min(minY, n.y - radius(n) - pad);
    maxY = Math.max(maxY, n.y + radius(n) + pad);
  });
  var W = canvas.clientWidth, H = canvas.clientHeight;
  var bw = Math.max(1, maxX-minX), bh = Math.max(1, maxY-minY);
  G.scale = Math.min(W/bw, H/bh, 1.6);
  G.ox = (W - bw*G.scale)/2 - minX*G.scale;
  G.oy = (H - bh*G.scale)/2 - minY*G.scale;
}

function draw(){
  var W = canvas.clientWidth, H = canvas.clientHeight;
  ctx.clearRect(0,0,W,H);
  ctx.save();
  ctx.translate(G.ox, G.oy); ctx.scale(G.scale, G.scale);
  var nodes = G.nodes;
  ctx.strokeStyle = "#e2dfd9"; ctx.lineWidth = 1;
  G.edges.forEach(function(e){
    var a = nodes[e[0]], b = nodes[e[1]];
    ctx.beginPath(); ctx.moveTo(a.x,a.y); ctx.lineTo(b.x,b.y); ctx.stroke();
  });
  nodes.forEach(function(n){
    var r = radius(n);
    ctx.beginPath(); ctx.arc(n.x, n.y, r, 0, Math.PI*2);
    ctx.fillStyle = TYPECOLOR[n.type] || "#888"; ctx.fill();
    if (n.type === "meta"){ ctx.strokeStyle = "#fff"; ctx.lineWidth = 2; ctx.stroke(); }
  });
  ctx.font = "11.5px -apple-system,PingFang SC,sans-serif";
  ctx.textAlign = "center";
  nodes.forEach(function(n){
    if (n.deg < 1 && G.scale < 1.15) return;
    var label = n.title.length > 16 ? n.title.slice(0,15)+"…" : n.title;
    var w = ctx.measureText(label).width;
    ctx.fillStyle = "rgba(255,255,255,.82)";
    ctx.fillRect(n.x - w/2 - 3, n.y + 9, w + 6, 14);
    ctx.fillStyle = "#4b4a46";
    ctx.fillText(label, n.x, n.y + 20);
  });
  ctx.restore();
}

function pick(ev){
  var rect = canvas.getBoundingClientRect();
  var x = (ev.clientX - rect.left - G.ox) / G.scale;
  var y = (ev.clientY - rect.top - G.oy) / G.scale;
  for (var i=G.nodes.length-1;i>=0;i--){
    var n = G.nodes[i];
    var r = radius(n) + 4;
    if ((n.x-x)*(n.x-x) + (n.y-y)*(n.y-y) < r*r) return n;
  }
  return null;
}

var downPt = null;
canvas.addEventListener("mousedown", function(ev){
  var n = pick(ev);
  if (n){ G.drag = n; canvas.classList.add("drag"); }
  else { downPt = {x: ev.clientX, y: ev.clientY, ox: G.ox, oy: G.oy}; canvas.classList.add("drag"); }
});
window.addEventListener("mousemove", function(ev){
  if (G.drag){
    var rect = canvas.getBoundingClientRect();
    G.drag.x = (ev.clientX - rect.left - G.ox) / G.scale;
    G.drag.y = (ev.clientY - rect.top - G.oy) / G.scale;
    draw();
  } else if (downPt){
    G.ox = downPt.ox + (ev.clientX - downPt.x);
    G.oy = downPt.oy + (ev.clientY - downPt.y);
    draw();
  }
});
window.addEventListener("mouseup", function(ev){
  if (G.drag && Math.abs(G.drag.vx) < 40){ }
  if (G.drag){
    var n = G.drag; G.drag = null;
    var moved = Math.abs(ev.movementX) + Math.abs(ev.movementY);
    if (moved < 3) go(n.slug);
    else { relax(140); draw(); }
  }
  downPt = null; canvas.classList.remove("drag");
});
canvas.addEventListener("wheel", function(ev){
  ev.preventDefault();
  var rect = canvas.getBoundingClientRect();
  var mx = ev.clientX - rect.left, my = ev.clientY - rect.top;
  var f = ev.deltaY < 0 ? 1.1 : 0.9;
  G.ox = mx - (mx - G.ox) * f;
  G.oy = my - (my - G.oy) * f;
  G.scale *= f;
  draw();
}, {passive:false});

window.addEventListener("resize", function(){ if (G.built) { resize(); fitGraph(); draw(); } });

/* ---------------- boot ---------------- */
buildNav();
document.getElementById("expandall").addEventListener("click", function(){ setAllGroups(false); });
document.getElementById("collapseall").addEventListener("click", function(){ setAllGroups(true); });
window.addEventListener("hashchange", function(){ go((location.hash||"#").slice(1)); });
var start = (location.hash||"#").slice(1);
if (!BYSLUG[start]) start = DATA.startSlug;
if (start) go(start);
</script>
</body>
</html>
"""


def cmd_build(root, out_path=None):
    pages = load_pages(root)
    by_slug = {p.slug: p for p in pages}
    backlinks = defaultdict(list)
    for p in pages:
        for t in set(p.links):
            if t in by_slug and t != p.slug:
                backlinks[t].append(p.slug)

    data = {
        "title": os.path.basename(root.rstrip("/")),
        "generated": date.today().isoformat(),
        "startSlug": "overview" if "overview" in by_slug else (pages[0].slug if pages else None),
        "backlinks": {k: sorted(set(v)) for k, v in backlinks.items()},
        "pages": [
            {
                "slug": p.slug,
                "title": p.title,
                "type": p.type,
                "relpath": p.relpath,
                "tags": p.tags,
                "status": p.status,
                "updated": str(p.fm.get("updated") or ""),
                "sources": p.sources,
                "links": sorted({t for t in p.links if t in by_slug and t != p.slug}),
                "body": p.body,
            }
            for p in pages
        ],
    }

    html = HTML_TEMPLATE.replace("__WIKI_DATA__", json.dumps(data, ensure_ascii=False))
    title = os.path.basename(root.rstrip("/"))
    html = html.replace("__SITE_TITLE__", title)
    html = html.replace("__SITE_SUB__",
                        "%d 个页面 · %s 生成" % (len(pages), date.today().isoformat()))
    # 章节判定词表从 Python 常量注入，保证站点与 chapter-audit 同口径（见常量区注释）
    for ph, tbl in (("__READ_EXACT__", READ_EXACT), ("__READ_H2__", READ_H2),
                    ("__LEDGER_H2__", LEDGER_H2)):
        assert ph in html, "模板缺少占位符 %s" % ph
        html = html.replace(ph, json.dumps(tbl, ensure_ascii=False))

    if out_path is None:
        out_path = os.path.join(root, "site", "index.html")
    write_text(out_path, html)

    # 构建基准：记下本次构建时每个页面的内容指纹。
    # 它是 [[schema]] §2.1 判据 3（「更新页面 > 5 或 新建页面 > 3」）唯一可执行的依据 ——
    # `site/` 被 .gitignore 排除，git 给不出基准；文件 mtime 又分不开「新建」与「更新」。
    manifest = {
        "built": date.today().isoformat(),
        "pages": len(pages),
        "links": sum(len(v) for v in backlinks.values()),
        "digests": {p.slug: page_digest(p) for p in pages},
    }
    write_text(os.path.join(root, "site", ".build-manifest.json"),
               json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=1))

    print("已生成浏览站点: %s（%d 个页面，%d 条链接）"
          % (os.path.relpath(out_path, root), len(pages),
             sum(len(v) for v in backlinks.values())))
    return 0


# ---------------------------------------------------------------- buildcheck

# 判据 3 的口径（见 [[schema]] §2.1）。改这两个数字要同步改 schema 与 decisions。
BUILD_NEW_MAX = 3      # 新建页面 **大于** 此数即构建
BUILD_UPD_MAX = 5      # 更新页面 **大于** 此数即构建
# 自动生成页：每次改动都会变，且它们的更新是别的改动的**后果**、不是里程碑信号。
# 计入会把阈值架空（每次 +2），故排除。
BUILD_MANIFEST_SKIP = frozenset({"index", "log"})


def page_digest(p):
    """页面内容指纹。直接读原文 —— frontmatter 的键序变化也算一次更新。"""
    try:
        with open(p.path, "r", encoding="utf-8") as fh:
            raw = fh.read()
    except OSError:  # pragma: no cover
        raw = p.body
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()[:16]


def cmd_buildcheck(root):
    man_path = os.path.join(root, "site", ".build-manifest.json")
    if not os.path.isfile(man_path):
        print("没有构建基准（%s 不存在）。" % os.path.relpath(man_path, root))
        print("说明：尚未构建过，或 site/ 被清理。**无法判断判据 3** —— 请先 build 一次建立基准。")
        return 1
    with open(man_path, "r", encoding="utf-8") as fh:
        man = json.load(fh)
    old = man.get("digests") or {}

    new, changed, cur = [], [], {}
    for p in load_pages(root):
        if p.slug in BUILD_MANIFEST_SKIP:
            continue
        d = page_digest(p)
        cur[p.slug] = d
        if p.slug not in old:
            new.append(p.slug)
        elif old[p.slug] != d:
            changed.append(p.slug)
    gone = [s for s in old if s not in cur and s not in BUILD_MANIFEST_SKIP]

    print("=" * 62)
    print("构建判据 3 核验  |  基准：%s（%s 页 / %s 链接）"
          % (man.get("built"), man.get("pages"), man.get("links")))
    print("=" * 62)
    print("新建页面: %d（阈值 > %d）" % (len(new), BUILD_NEW_MAX))
    for s in sorted(new):
        print("    + %s" % s)
    print("更新页面: %d（阈值 > %d）" % (len(changed), BUILD_UPD_MAX))
    for s in sorted(changed):
        print("    ~ %s" % s)
    if gone:
        print("已删除页面: %d（不单独触发构建，但站点会留下指向它们的断链）" % len(gone))
        for s in sorted(gone):
            print("    - %s" % s)

    hit_new = len(new) > BUILD_NEW_MAX
    hit_upd = len(changed) > BUILD_UPD_MAX
    print("-" * 62)
    print("判据 3a 新建页面 > %d ：%s（%d）" % (BUILD_NEW_MAX, "**命中**" if hit_new else "不命中", len(new)))
    print("判据 3b 更新页面 > %d ：%s（%d）" % (BUILD_UPD_MAX, "**命中**" if hit_upd else "不命中", len(changed)))
    if hit_new or hit_upd:
        print("→ **判据 3 命中，应构建。**（另请照 §2.1 逐条核判据 1/2/4/5）")
    else:
        print("→ 判据 3 不命中。（另请照 §2.1 逐条核判据 1/2/4/5 —— 都不命中才「明确地不构建」）")
    if gone:
        print("→ ⚠️ 有页面被删除：站点内可能留下断链，属「内容已错误」，**必须构建**。")
    return 0


# ---------------------------------------------------------------- chapter-audit


def cmd_chapter_audit(root, verbose=False):
    """source 页的「正文 / 账目」分布审计。**只读，不改任何文件。**

    站点侧会按同一张词表把账目章节折叠起来（见常量区注释）。这份报表是给人看的
    对账表：哪些页折了多少、哪些章节名落在词表之外（= 走了「默认正文」这条兜底）
    —— 兜底命中的那些最值得人工确认，它们要么该补进词表，要么确实是正文。

    **不做批量改名。** 本库有 330 处页内指向引用（见下 / 上表 /「见下『素材基本信息』」），
    改名会让指名引用指空。同义异名只摆出来，改不改由人裁定。
    """
    pages = load_pages(root)
    src = [p for p in pages if p.type == "source"]
    if not src:
        print("没有 source 页")
        return 1

    name_kind = Counter()          # 章节名 → 计数（按判定分桶）
    fallback = Counter()           # 走兜底（默认正文）的章节名 → 计数
    per_page = []
    for p in sorted(src, key=lambda x: x.slug):
        titles = re.findall(r"^##\s+(.+)$", p.body, flags=re.M)
        read = led = 0
        unk = []
        for t in titles:
            t = t.strip()
            k = classify_h2(t)
            name_kind[(k, t)] += 1
            if k == "read":
                read += 1
                if not any(x in t for x in READ_H2) and t not in READ_EXACT:
                    unk.append(t)
            else:
                led += 1
        for t in unk:
            fallback[t] += 1
        per_page.append((p.slug, read, led, unk))

    tot_r = sum(x[1] for x in per_page)
    tot_l = sum(x[2] for x in per_page)
    print("source 页 %d ｜ 正文章节 %d ｜ 账目章节 %d ｜ 账目占比 %.1f%%"
          % (len(src), tot_r, tot_l, 100.0 * tot_l / max(1, tot_r + tot_l)))
    n_l = sum(1 for x in per_page if x[2] == 0)
    counts = sorted(x[2] for x in per_page)
    print("每页账目数：中位 %d ｜ 最多 %d ｜ 零账目的页 %d（这些是早期简单页，正常）"
          % (counts[len(counts) // 2], counts[-1], n_l))

    if verbose:
        print("\n=== 逐页 ===")
        for slug, r, l, unk in per_page:
            print("  %-44s 正文 %2d / 账目 %2d%s" % (slug, r, l, ("  ← " + " ｜ ".join(unk)) if unk else ""))

    print("\n=== 走兜底（默认正文）的章节名 TOP20 —— 最值得人工确认的一批 ===")
    if not fallback:
        print("  （无）")
    for t, n in fallback.most_common(20):
        print("  %3d  %s" % (n, t))
    if len(fallback) > 20:
        # 静默截断会让人把「没列出来」读成「不存在」—— 这正是本库记过的
        # 「测不了 ≠ 不命中」。所以把省略数写出来，并指明可靠的核法。
        print("  ……另有 %d 个兜底名未列出（多为只出现 1 次的页内特有名）。" % (len(fallback) - 20))
        print("     本表是**截断**的，不能用来下「某个名字不存在」的结论。")
        print("     要确认某个**特定名字**（例如已废除的 `TL;DR`）是否被重新引入，")
        print("     用 `python3 tools/wiki.py chapter-audit -v` 逐页看。")

    print("\n=== 账目判定词表（%d 条子串 + %d 条精确名）===" % (len(LEDGER_H2), len(READ_EXACT)))
    print("  正文精确：" + "、".join(READ_EXACT))
    print("  正文字串：" + "、".join(READ_H2))
    print("  账目子串：" + "、".join(LEDGER_H2))

    print("\n=== 同义异名的用法分布（只报告，不改名）===")
    for label, names in SECTION_FAMILIES:
        rows = [(t, n) for (k, t), n in name_kind.items() if t in names]
        if rows:
            print("  【%s】%s" % (label, " ｜ ".join("%s ×%d" % (t, n) for t, n in sorted(rows, key=lambda x: -x[1]))))
    return 0


# ---------------------------------------------------------------- main


USAGE = __doc__


def main(argv):
    if len(argv) < 2:
        print(USAGE)
        return 1
    cmd = argv[1]

    if cmd in ("-h", "--help", "help"):
        print(USAGE)
        return 0

    if cmd == "init":
        return cmd_init(argv[2] if len(argv) > 2 else None)

    root = find_root()

    if cmd == "lint":
        return cmd_lint(root)
    if cmd == "stats":
        return cmd_stats(root)
    if cmd == "index":
        return cmd_index(root)
    if cmd == "build":
        return cmd_build(root, argv[2] if len(argv) > 2 else None)
    if cmd == "buildcheck":
        return cmd_buildcheck(root)
    if cmd == "chapter-audit":
        return cmd_chapter_audit(root, verbose=("-v" in argv or "--verbose" in argv))
    if cmd == "graph":
        return cmd_graph(root)
    if cmd == "search":
        if len(argv) < 3:
            print("用法: wiki.py search \"<query>\" [--type concept]")
            return 1
        tf = None
        if "--type" in argv:
            i = argv.index("--type")
            if i + 1 < len(argv):
                tf = argv[i + 1]
        return cmd_search(root, argv[2], type_filter=tf)
    if cmd == "log":
        if len(argv) < 4:
            print("用法: wiki.py log <type> \"<message>\"")
            return 1
        return cmd_log(root, argv[2], " ".join(argv[3:]))
    if cmd == "new":
        if len(argv) < 4:
            print("用法: wiki.py new <type> <slug> [title]")
            return 1
        return cmd_new(root, argv[2], argv[3], argv[4] if len(argv) > 4 else None)

    print("未知命令: %s\n" % cmd)
    print(USAGE)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
