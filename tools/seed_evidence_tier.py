#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""给全部知识页写入 evidence_tier 字段（2026-09-19）。幂等：可反复运行。

2026-09-21：不再往正文插「孤证 / 名义交叉」样板警示块。
判据：那两句话是 `evidence_tier: single` 的逐字复述 —— 全库 235 页各抄一遍同一段，
读者每打开一页都要先读一遍「本页只有一份来源」。信息没有丢：字段仍在 frontmatter，
`lint` 会校验它与素材是否一致，站点在页头渲染徽标（见 wiki/schema.md §1.2）。
`strip_callouts` 保留 —— 它负责撤除存量，也负责将来有人重新引入时清掉。

用法：
    python3 tools/seed_evidence_tier.py          # 只打印会做什么（dry run）
    python3 tools/seed_evidence_tier.py --write  # 真正写入
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wiki  # noqa: E402

ROOT = wiki.find_root(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

TIER_NOTE = {
    "single": (
        "> [!warning] 孤证 —— 本页仅 %d 份素材支撑\n"
        "> 支撑本页的只有 %s，尚未获得第二份独立来源的交叉验证。\n"
        "> **引用本页结论时应带着这个前提**，或先补一份独立来源把它升到 `crossed`。"
    ),
    "samefam": (
        "> [!warning] 名义交叉，实质同源\n"
        "> 本页有 %d 份支撑素材，但**全部来自同一来源族** —— 相当于同一处转述被拆成几份，\n"
        "> 不构成独立交叉验证。引用时不能把它们算作多个佐证。"
    ),
}

MARK_SINGLE = "孤证 —— 本页仅"
MARK_SAMEFAM = "名义交叉，实质同源"
MARK_HEADS = ("> [!warning] " + MARK_SINGLE, "> [!warning] " + MARK_SAMEFAM)


def extract_callouts(text):
    """返回文本中本脚本插入过的警示块原文（按出现顺序）。

    幂等判断必须拿**剥离前**的原文来比 —— 先删再判会永远判成「没有」，
    于是每次运行都以为要重写一遍。
    """
    blocks = []
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        if any(lines[i].startswith(h) for h in MARK_HEADS):
            j = i
            while j < len(lines) and lines[j].startswith(">"):
                j += 1
            blocks.append("\n".join(lines[i:j]))
            i = j
        else:
            i += 1
    return blocks


def strip_callouts(text):
    """移除本脚本插入过的全部警示块。判据变了以后旧警示可能是错的，必须能撤。"""
    lines = text.split("\n")
    out = []
    i = 0
    removed = 0
    while i < len(lines):
        if any(lines[i].startswith(h) for h in MARK_HEADS):
            while i < len(lines) and lines[i].startswith(">"):
                i += 1
            while i < len(lines) and lines[i].strip() == "":
                i += 1
            removed += 1
            continue
        out.append(lines[i])
        i += 1
    return "\n".join(out), removed


def build_callout(tier, n, fams, srcs):
    """2026-09-21 起恒定返回 None —— 正文不再插样板块（见模块 docstring）。

    保留函数签名是因为调用方与「撤除」路径都依赖它：返回 None 即「本页不需要警示块」，
    `need_body` 因此只在**存量块还在**时才为真，于是重跑本脚本＝清掉存量。
    """
    return None


def main(write):
    pages = wiki.load_pages(ROOT)
    raw_meta = wiki.load_raw_meta(ROOT)
    planned = []
    for p in pages:
        if p.type not in wiki.EVIDENCE_TYPES:
            continue
        tier, n, fams = wiki.compute_evidence_tier(p, raw_meta)
        if tier == "none":
            continue
        declared = (p.fm.get("evidence_tier") or "").strip()
        need_fm = declared != tier
        callout = build_callout(tier, n, fams, [s for s in p.sources if s])
        text = open(p.path, encoding="utf-8").read()
        existing = extract_callouts(text)
        want = [callout] if callout else []
        # 需要正文改动 = 现有警示块与期望的不一致（多了、少了、或内容变了）
        need_body = existing != want
        if need_fm or need_body:
            planned.append((p, tier, need_fm, callout, need_body))

    print("=" * 62)
    print("evidence_tier 播种  |  %s" % ("写入模式" if write else "DRY RUN（加 --write 才真正改文件）"))
    print("=" * 62)
    print("需要改动: %d 个页面" % len(planned))
    from collections import Counter
    print("按层级:", dict(Counter(t for _p, t, _a, _b, _c in planned)))
    print("其中需要正文警示: %d 个" % sum(1 for x in planned if x[4]))

    if not write:
        for p, tier, need_fm, callout, need_body in planned[:3]:
            print("\n--- %s ---" % p.relpath)
            print("  frontmatter: evidence_tier: %s%s" % (tier, "" if need_fm else " (已是该值)"))
            if need_body and callout:
                print("  正文插入:")
                for line in callout.split("\n"):
                    print("    " + line)
            elif need_body:
                print("  正文：撤除过时警示（判据变更后本页不再属于孤证 / 同源）")
        print("\n（仅显示前 3 个，加 --write 执行全部）")
        return 0

    done_fm = done_body = done_rm = 0
    for p, tier, need_fm, callout, need_body in planned:
        text = open(p.path, encoding="utf-8").read()
        text, removed = strip_callouts(text)
        done_rm += removed
        if need_fm:
            if re.search(r"^evidence_tier:", text, re.M):
                text = re.sub(r"^evidence_tier:.*$", "evidence_tier: %s" % tier,
                              text, count=1, flags=re.M)
            else:
                # 插到 confidence 之前：事实在前，主观判断在后
                m = re.search(r"^confidence:", text, re.M)
                if not m:
                    m = re.search(r"^status:", text, re.M)
                anchor = m.start() if m else None
                if anchor is None:
                    print("  跳过（找不到插入锚点）: %s" % p.relpath)
                    continue
                text = text[:anchor] + "evidence_tier: %s\n" % tier + text[anchor:]
            done_fm += 1
        if need_body and callout:
            m = re.search(r"^## ", text, re.M)
            if not m:
                print("  跳过（正文无二级标题，无处插警示）: %s" % p.relpath)
            else:
                text = text[:m.start()] + callout + "\n\n" + text[m.start():]
                done_body += 1
        open(p.path, "w", encoding="utf-8").write(text)
    print("\n已写入 evidence_tier: %d 个页面" % done_fm)
    print("已插入正文警示: %d 个页面" % done_body)
    print("已撤除过时警示: %d 处" % done_rm)
    return 0


if __name__ == "__main__":
    sys.exit(main("--write" in sys.argv))
