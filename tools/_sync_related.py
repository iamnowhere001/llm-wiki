#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把本轮回填节里新出现的 [[链接]] 同步进各目标页的 related 字段。
只加**已存在**的页；不存在的报 MISSING，不写入。幂等。"""
import re, os, sys, glob

ROOT = '/Users/yongxu/Documents/llm-wiki'
SEC_MARK = '## 2026-09-20 回填（模块五 参与者 · 本批 13 份清单）'

# 全库已有 slug
slugs = set()
for p in glob.glob(os.path.join(ROOT, 'wiki/**/*.md'), recursive=True):
    m = re.search(r'^slug:\s*(.+)$', open(p, encoding='utf-8').read(), re.M)
    if m:
        slugs.add(m.group(1).strip())

TARGETS = [
 'wiki/concepts/credible-commitment.md','wiki/concepts/goodharts-law.md',
 'wiki/concepts/skin-in-the-game.md','wiki/concepts/self-determination-theory.md',
 'wiki/concepts/tacit-knowledge.md','wiki/entities/michael-polanyi.md',
 'wiki/concepts/situated-cognition.md','wiki/concepts/social-capital.md',
 'wiki/concepts/positional-goods.md','wiki/concepts/selection-bias.md',
 'wiki/entities/stephen-covey.md','wiki/concepts/adaptive-cycle.md',
 'wiki/concepts/narrative-reframing.md','wiki/concepts/cognitive-reappraisal.md',
 'wiki/concepts/entrustability.md',
 'wiki/concepts/ritual-as-protocol.md','wiki/concepts/social-status.md',
 'wiki/concepts/common-knowledge.md','wiki/concepts/scapegoat-mechanism.md',
 'wiki/concepts/market-for-lemons.md','wiki/concepts/legibility.md',
 'wiki/concepts/unintended-consequences.md','wiki/concepts/soft-budget-constraint.md',
 'wiki/concepts/state-formation.md','wiki/concepts/slow-variables.md',
]

LINK_RE = re.compile(r'\[\[([^\[\]|]+)(?:\|([^\[\]]+))?\]\]')


def main():
    dry = '--write' not in sys.argv
    missing = set()
    for rel in TARGETS:
        p = os.path.join(ROOT, rel)
        t = open(p, encoding='utf-8').read()
        i = t.find(SEC_MARK)
        if i < 0:
            print('NOSEC    ', rel); continue
        j = t.find('\n## ', i + 1)
        sec = t[i: j if j > 0 else len(t)]
        linked = [m.group(1).strip() for m in LINK_RE.finditer(sec)]
        new = [s for s in linked if s in slugs]
        for s in linked:
            if s not in slugs:
                missing.add((rel, s))
        m = re.search(r'^related:\s*\[(.*)\]\s*$', t, re.M)
        if not m:
            print('NORELATED', rel); continue
        cur = [x.strip() for x in m.group(1).split(',') if x.strip()]
        add = [s for s in dict.fromkeys(new) if s not in cur]
        if not add:
            print('NOCHANGE ', rel.split('/')[-1]); continue
        out = cur + add
        t = t[:m.start()] + 'related: [%s]' % ', '.join(out) + t[m.end():]
        if dry:
            print('DRY      %-40s +%d %s' % (rel.split('/')[-1], len(add), add[:6]))
        else:
            open(p, 'w', encoding='utf-8').write(t)
            print('OK       %-40s +%d' % (rel.split('/')[-1], len(add)))
    if missing:
        print('\nMISSING（未写入）:')
        for r, s in sorted(missing):
            print('   ', r, '->', s)
    else:
        print('\n无悬空引用。')


main()
