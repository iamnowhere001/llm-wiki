#!/usr/bin/env python3
"""把 templates/*.md 同步进 tools/wiki.py 的 TEMPLATES 内联兜底模板。

为什么要有这个脚本：schema §1.8 要求「templates/ 与内联模板逐字节一致」，
`template-check` 会核这一条。手工两边抄一遍必然出错（2026-09-20 就是这么做的，
当时靠人抄），所以这里用「以文件为准、覆盖内联」的单向同步。

用法：
    python3 tools/_sync_inline_templates.py            # dry-run，只报告差异
    python3 tools/_sync_inline_templates.py --write    # 真的写回 wiki.py
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI_PY = os.path.join(ROOT, "tools", "wiki.py")
TYPES = ["source", "entity", "concept", "analysis", "project"]


def extract_inline(src, name):
    """返回 (起点, 终点) —— 内联模板正文的字符区间。"""
    head = 'TEMPLATES["%s"] = """' % name
    i = src.index(head)
    start = i + len(head)
    end = src.index('"""', start)
    return start, end


def main(argv):
    write = "--write" in argv
    with open(WIKI_PY, "r", encoding="utf-8") as fh:
        src = fh.read()

    changed = []
    # 逐个替换：每次替换都会改变长度，所以从后往前处理，避免区间错位。
    spans = []
    for name in TYPES:
        path = os.path.join(ROOT, "templates", "%s.md" % name)
        with open(path, "r", encoding="utf-8") as fh:
            disk = fh.read()
        if '"""' in disk:
            print("!! templates/%s.md 含三引号，会破坏 Python 字符串 —— 中止" % name)
            return 1
        start, end = extract_inline(src, name)
        inline = src[start:end]
        if inline == disk:
            print("  %-9s 已一致（%d 字符）" % (name, len(disk)))
        else:
            print("  %-9s 不一致：内联 %d 字符 → 文件 %d 字符" % (name, len(inline), len(disk)))
            changed.append(name)
        spans.append((start, end, disk, name))

    if not changed:
        print("\n无需改动。")
        return 0

    print("\n需同步：%s" % " / ".join(changed))
    if not write:
        print("（dry-run；加 --write 才真的写回）")
        return 0

    for start, end, disk, _name in sorted(spans, key=lambda x: -x[0]):
        src = src[:start] + disk + src[end:]

    with open(WIKI_PY, "w", encoding="utf-8") as fh:
        fh.write(src)
    print("\n已写回 %s" % os.path.relpath(WIKI_PY, ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
