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
from collections import Counter, defaultdict
from datetime import date

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

META_FILES = {"index", "log", "overview", "conventions"}

REQUIRED_FM = ["title", "type", "slug"]

LINK_RE = re.compile(r"\[\[([^\[\]|]+)(?:\|([^\[\]]+))?\]\]")

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
    __slots__ = ("path", "relpath", "fm", "body", "slug", "title", "type", "links")

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
        self.links = []
        for m in LINK_RE.finditer(scan):
            target = m.group(1).strip()
            if target:
                self.links.append(target)
        # frontmatter 里的 related 也算出链
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


# ---------------------------------------------------------------- lint


def gap_table_rows(body):
    """返回「当前缺口」表里的数据行数。找不到该节、或表已清空时返回 0。

    这是「项目是否做到终点」的机器判据 —— 缺口表清空 = shipped（AGENTS.md 3.5）。
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

    # 项目生命周期：缺口表清空 = shipped（AGENTS.md 3.5）
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
        # 缺口表已清空但项目还开着 —— 按 AGENTS.md 3.5，可以收尾了
        for p in sorted(projects, key=lambda x: x.slug):
            if p.stage in ("planning", "active") and gap_table_rows(p.body) == 0:
                advisories.append(
                    "%s  「当前缺口」表已清空 —— 按 AGENTS.md 3.5，该项目可标 `stage: shipped`"
                    % p.relpath)
    elif len(knowledge) >= 10:
        advisories.append(
            "本库有 %d 个知识页但**没有任何项目页**。按 [[cybernetic-learning]] 的推论，"
            "没有目标就没有过滤器 —— 建议用 `new project <slug>` 建一个。" % len(knowledge))
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
    out.append("页面总数 **%d** ｜ 项目 **%d**（进行中 %d） ｜ raw 素材 **%d** 份 / 摘要页 **%d** 份 ｜ 最后更新 %s"
               % (total, n_proj, n_active,
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

    out.append("## 系统页")
    out.append("")
    out.append("- [[overview|总览]] — 这个知识库在讲什么")
    out.append("- [[log|日志]] — 按时间记录的所有操作")
    out.append("- [[conventions|使用约定]] — 人类的偏好设置")
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

> 三层架构中的规范层。任何 LLM Agent 进入本仓库后，先读本文件，再动手。

## 三层架构

| 层 | 位置 | 谁写 | 谁读 |
|---|---|---|---|
| 原始素材 | `raw/` | 人类 | LLM（只读，不可变） |
| 知识库 | `wiki/` | LLM | 人类 |
| 规范 | 本文件 + `wiki/conventions.md` | 共同演进 | LLM |

## 页面类型

- `projects/` 项目页：**入口层** —— 我在做什么、因此什么重要
- `sources/` 素材摘要页，一份素材一页
- `entities/` 实体页：人物、组织、工具、产品
- `concepts/` 概念页：理论、方法、模式、术语
- `analyses/` 分析页：对比、综述、回答归档

## Frontmatter

```yaml
---
title: 页面标题
type: concept
slug: page-slug
tags: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
related: []
confidence: high
status: active
---
```

项目页额外有 `goal` 与 `stage`。注意 `stage`（项目做到哪了）与 `status`（页面还新鲜吗）是两个维度。

## 工作流

**Ingest**：**先读 projects/ 判断这份素材服务于哪个项目、填哪个缺口** → 读素材
→ 与人类对齐要点 → 写 sources 页 → 拆 entities/concepts 页
→ 回填所有被影响的页面 → 更新 index.md → 写 log → 跑 lint。
一份素材通常触及 10-15 个页面。**服务不了任何项目的素材，先问该不该收。**

**Query**：先读 index.md 定位 → 必要时 `wiki.py search` → 带引用作答
→ 好答案归档进 analyses/。

**Lint**：`wiki.py lint` 查机器可查问题，再人工核查矛盾、过期、该建未建。

## 工具链

```bash
python3 tools/wiki.py lint | stats | search "<q>" | index | build | log | new | graph
```

## 铁律

1. `raw/` 不可变。
2. `[[link]]` 只能指向已存在的页面。
3. 没有来源的断言必须显式标注「（未验证）」。
4. 新素材与旧结论冲突时，必须显式标注矛盾，不得静默覆盖。
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

> 一句话概括这份素材讲了什么。

- **作者 / 来源**：
- **链接**：
- **发布时间**：
- **素材路径**：`raw/{{SLUG}}.md`

## 关键要点

1.
2.
3.

## 摘要

按素材自身的逻辑复述，不加入素材以外的判断。

## 与现有知识库的关系

- 印证了：[[ ]]
- 补充了：[[ ]]
- **与 [[ ]] 存在矛盾**：（如有，必须明确指出并列出双方证据）

## 新出现的实体 / 概念

- 实体：[[]]
- 概念：[[]]

## 待办

- [ ]

## 相关页面

- [[ ]]
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

    for name in ["index", "log", "overview", "conventions"]:
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
#sidebar{
  width:290px;flex:0 0 290px;background:var(--panel);border-right:1px solid var(--line);
  display:flex;flex-direction:column;overflow:hidden;
}
.brand{padding:18px 20px 12px;border-bottom:1px solid var(--line-soft)}
.brand h1{margin:0;font-size:15px;letter-spacing:.2px;font-weight:650}
.brand .sub{font-size:11.5px;color:var(--muted);margin-top:3px;font-variant-numeric:tabular-nums}
.searchwrap{padding:12px 16px 10px}
#search{
  width:100%;padding:8px 11px;border:1px solid var(--line);border-radius:8px;
  background:var(--bg);font-size:13px;color:var(--ink);outline:none;font-family:inherit;
}
#search:focus{border-color:var(--accent);background:#fff}
#nav{flex:1;overflow-y:auto;padding:4px 10px 24px}
.grp{margin-bottom:14px}
.grp h3{
  margin:0;padding:6px 10px;font-size:11px;font-weight:650;letter-spacing:.9px;
  color:var(--muted);text-transform:uppercase;display:flex;justify-content:space-between;
}
.grp h3 span{font-weight:400;font-variant-numeric:tabular-nums}
.nav-item{
  display:block;padding:5px 10px;border-radius:6px;cursor:pointer;font-size:13.2px;
  color:var(--ink);text-decoration:none;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;
  border-left:2px solid transparent;
}
.nav-item:hover{background:var(--line-soft)}
.nav-item.active{background:var(--accent-soft);border-left-color:var(--accent);font-weight:600;color:var(--accent)}
.nav-item .dot{display:inline-block;width:6px;height:6px;border-radius:50%;margin-right:8px;vertical-align:1px}
.res-count{font-size:11.5px;color:var(--muted);padding:4px 12px 8px}

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
</style>
</head>
<body>
<div id="app">
  <aside id="sidebar">
    <div class="brand">
      <h1>__SITE_TITLE__</h1>
      <div class="sub">__SITE_SUB__</div>
    </div>
    <div class="searchwrap"><input id="search" placeholder="搜索页面…" autocomplete="off"></div>
    <nav id="nav"></nav>
  </aside>
  <main id="main">
    <div id="tabs">
      <button data-view="browse" class="active">浏览</button>
      <button data-view="graph">图谱</button>
      <span class="spacer"></span>
      <span class="meta" id="tabmeta"></span>
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

function render(src){
  var codeBlocks = [];
  src = src.replace(/```[^\n]*\n([\s\S]*?)```/g, function(m, code){
    codeBlocks.push("<pre><code>"+esc(code.replace(/\n$/,""))+"</code></pre>");
    return "\u0000B"+(codeBlocks.length-1)+"\u0000";
  });

  var lines = src.split("\n"), out = [], i = 0;
  var listBuf = null, listType = null;

  function flushList(){
    if (listBuf){ out.push("<"+listType+">"+listBuf.join("")+"</"+listType+">"); listBuf=null; listType=null; }
  }

  while (i < lines.length){
    var line = lines[i];

    if (/^\u0000B\d+\u0000\s*$/.test(line.trim())){
      flushList();
      out.push(line.trim());
      i++; continue;
    }
    if (!line.trim()){ flushList(); i++; continue; }

    var h = /^(#{1,6})\s+(.*)$/.exec(line);
    if (h){ flushList(); out.push("<h"+h[1].length+">"+inline(h[2])+"</h"+h[1].length+">"); i++; continue; }

    if (/^(---|\*\*\*|___)\s*$/.test(line)){ flushList(); out.push("<hr>"); i++; continue; }

    if (/^>\s?/.test(line)){
      flushList();
      var buf = [];
      while (i < lines.length && /^>\s?/.test(lines[i])){ buf.push(lines[i].replace(/^>\s?/,"")); i++; }
      out.push("<blockquote>"+render(buf.join("\n"))+"</blockquote>");
      continue;
    }

    if (/^\|/.test(line) && i+1 < lines.length && /^\|[\s:|-]+\|/.test(lines[i+1])){
      flushList();
      var head = line.split("|").slice(1,-1).map(function(c){return c.trim();});
      i += 2;
      var rows = [];
      while (i < lines.length && /^\|/.test(lines[i])){
        rows.push(lines[i].split("|").slice(1,-1).map(function(c){return c.trim();}));
        i++;
      }
      var t = "<table><thead><tr>";
      head.forEach(function(c){ t += "<th>"+inline(c)+"</th>"; });
      t += "</tr></thead><tbody>";
      rows.forEach(function(r){
        t += "<tr>";
        for (var k=0;k<head.length;k++) t += "<td>"+inline(r[k]||"")+"</td>";
        t += "</tr>";
      });
      out.push(t+"</tbody></table>");
      continue;
    }

    var ul = /^(\s*)[-*+]\s+(.*)$/.exec(line);
    var ol = /^(\s*)\d+[.)]\s+(.*)$/.exec(line);
    if (ul || ol){
      var wantType = ul ? "ul" : "ol";
      if (listType !== wantType){ flushList(); listType = wantType; listBuf = []; }
      var content = (ul || ol)[2];
      var task = /^\[([ xX])\]\s+(.*)$/.exec(content);
      if (task){
        var checked = task[1].toLowerCase() === "x";
        listBuf.push('<li style="list-style:none;margin-left:-18px">'+
          '<input type="checkbox" disabled'+(checked?" checked":"")+'> '+inline(task[2])+'</li>');
      } else {
        listBuf.push("<li>"+inline(content)+"</li>");
      }
      i++; continue;
    }

    flushList();
    var para = [line];
    i++;
    while (i < lines.length && lines[i].trim() && !/^(#{1,6}\s|>|\||\s*[-*+]\s|\s*\d+[.)]\s|```)/.test(lines[i])){
      para.push(lines[i]); i++;
    }
    out.push("<p>"+inline(para.join(" "))+"</p>");
  }
  flushList();
  var html = out.join("\n");
  html = html.replace(/\u0000B(\d+)\u0000/g, function(m, n){ return codeBlocks[+n]; });
  return html;
}

/* ---------------- nav ---------------- */
var ORDER = ["project","meta","source","entity","concept","analysis"];
var nav = document.getElementById("nav");

function buildNav(){
  nav.innerHTML = "";
  ORDER.forEach(function(t){
    var items = PAGES.filter(function(p){ return p.type === t; });
    if (!items.length) return;
    var g = document.createElement("div"); g.className = "grp";
    g.innerHTML = "<h3>"+(TYPELABEL[t]||t)+"<span>"+items.length+"</span></h3>";
    items.forEach(function(p){
      var a = document.createElement("a");
      a.className = "nav-item"; a.href = "#"+p.slug; a.dataset.slug = p.slug;
      a.title = p.title;
      a.innerHTML = (t==="meta"?"":'<i class="dot" style="background:'+TYPECOLOR[t]+'"></i>')+
                    esc(p.title);
      a.addEventListener("click", function(e){ e.preventDefault(); go(p.slug); });
      g.appendChild(a);
    });
    nav.appendChild(g);
  });
}

function markActive(slug){
  [].forEach.call(nav.querySelectorAll(".nav-item"), function(el){
    el.classList.toggle("active", el.dataset.slug === slug);
  });
}

/* ---------------- page ---------------- */
var pageEl = document.getElementById("page");
var blEl = document.getElementById("backlinks");
var tabmeta = document.getElementById("tabmeta");

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

  pageEl.innerHTML = '<div class="pagemeta">'+chips+'</div>' + render(p.body);

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
  markActive(slug);
  document.getElementById("view-browse").scrollTop = 0;
  document.title = p.title + " · " + DATA.title;
}

/* ---------------- search ---------------- */
var searchEl = document.getElementById("search");
searchEl.addEventListener("input", function(){
  var q = searchEl.value.trim().toLowerCase();
  if (!q){ buildNav(); markActive((location.hash||"#").slice(1)); return; }
  var hits = PAGES.filter(function(p){
    return (p.title+" "+p.slug+" "+(p.tags||[]).join(" ")+" "+p.body).toLowerCase().indexOf(q) >= 0;
  });
  nav.innerHTML = "";
  var g = document.createElement("div"); g.className = "grp";
  g.innerHTML = "<h3>搜索结果<span>"+hits.length+"</span></h3>";
  if (!hits.length){
    var d = document.createElement("div"); d.className = "res-count"; d.textContent = "无匹配页面";
    g.appendChild(d);
  }
  hits.slice(0, 60).forEach(function(p){
    var a = document.createElement("a");
    a.className = "nav-item"; a.href = "#"+p.slug; a.dataset.slug = p.slug;
    a.innerHTML = '<i class="dot" style="background:'+(TYPECOLOR[p.type]||"#666")+'"></i>'+esc(p.title);
    a.addEventListener("click", function(e){ e.preventDefault(); go(p.slug); });
    g.appendChild(a);
  });
  nav.appendChild(g);
});

/* ---------------- tabs ---------------- */
var canvas = document.getElementById("canvas");
[].forEach.call(document.querySelectorAll("#tabs button"), function(b){
  b.addEventListener("click", function(){
    [].forEach.call(document.querySelectorAll("#tabs button"), function(x){ x.classList.remove("active"); });
    b.classList.add("active");
    var v = b.dataset.view;
    document.getElementById("view-browse").hidden = (v !== "browse");
    document.getElementById("view-graph").hidden = (v !== "graph");
    if (v === "graph") startGraph();
  });
});

/* ---------------- graph ---------------- */
var G = { nodes: [], edges: [], built: false, scale: 1, ox: 0, oy: 0, drag: null };
var ctx = canvas.getContext("2d");

function startGraph(){
  resize();
  if (!G.built) buildGraph();
  fitGraph();
  draw();
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
  relax(700);
}

function resize(){
  var dpr = window.devicePixelRatio || 1;
  canvas.width = canvas.clientWidth * dpr;
  canvas.height = canvas.clientHeight * dpr;
  ctx.setTransform(dpr,0,0,dpr,0,0);
}

function relax(steps){
  var nodes = G.nodes, edges = G.edges, n = nodes.length;
  var W = canvas.clientWidth, H = canvas.clientHeight;
  for (var s=0; s<steps; s++){
    var i, j, a, b, dx, dy, d2, d, ux, uy, f;
    for (i=0;i<n;i++){
      a = nodes[i];
      for (j=i+1;j<n;j++){
        b = nodes[j];
        dx = b.x-a.x; dy = b.y-a.y;
        d2 = dx*dx+dy*dy || 0.01; d = Math.sqrt(d2);
        f = 26000 / d2;
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
      if (a !== G.drag){ a.x += a.vx; a.y += a.vy; }
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

    if out_path is None:
        out_path = os.path.join(root, "site", "index.html")
    write_text(out_path, html)
    print("已生成浏览站点: %s（%d 个页面，%d 条链接）"
          % (os.path.relpath(out_path, root), len(pages),
             sum(len(v) for v in backlinks.values())))
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
