# -*- coding: utf-8 -*-
"""wiki.py 的最小回归测试。

只覆盖 2026-10-19 修复过的判据：frontmatter 结构、type 默认值、证据层级、
缺口表行数，以及仓库自身的 doctor 一致性。测试不写任何文件。
"""

import contextlib
import importlib.util
import io
import os
import sys
import unittest
from types import SimpleNamespace

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_wiki():
    path = os.path.join(ROOT, "tools", "wiki.py")
    spec = importlib.util.spec_from_file_location("wiki_under_test", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


wiki = load_wiki()


class FrontmatterTests(unittest.TestCase):
    def test_valid_frontmatter(self):
        text = "---\ntitle: T\ntype: concept\nslug: s\ntags: [a, b]\n---\nbody\n"
        fm, body = wiki.parse_frontmatter(text)
        self.assertEqual(fm["title"], "T")
        self.assertEqual(fm["tags"], ["a", "b"])
        self.assertEqual(body, "body\n")
        self.assertEqual(wiki.detect_frontmatter_error(text), "")

    def test_escaped_start_is_an_error(self):
        text = "\\---\ntitle: T\ntype: analysis\nslug: s\n\\---\nbody\n"
        self.assertIn("转义", wiki.detect_frontmatter_error(text))

    def test_unclosed_frontmatter_is_an_error(self):
        text = "---\ntitle: T\ntype: concept\nslug: s\nbody\n"
        self.assertIn("未闭合", wiki.detect_frontmatter_error(text))

    def test_missing_type_is_unknown_not_concept(self):
        page = wiki.Page("/tmp/x.md", "wiki/concepts/x.md", {}, "body", "---\n---\nbody\n")
        self.assertEqual(page.type, "unknown")

    def test_valid_type_is_preserved(self):
        fm = {"title": "T", "type": "analysis", "slug": "x"}
        page = wiki.Page("/tmp/x.md", "wiki/analyses/x.md", fm, "body", "---\n---\nbody\n")
        self.assertEqual(page.type, "analysis")


class EvidenceTierTests(unittest.TestCase):
    def page(self, sources):
        return SimpleNamespace(sources=sources)

    def test_single(self):
        tier, n, _ = wiki.compute_evidence_tier(self.page(["a"]), {})
        self.assertEqual((tier, n), ("single", 1))

    def test_same_family(self):
        meta = {
            "a": {"author": "万维钢", "kind": "course-article"},
            "b": {"author": "得到《现代思维工具课》", "kind": "course-article"},
        }
        tier, n, families = wiki.compute_evidence_tier(self.page(["a", "b"]), meta)
        self.assertEqual((tier, n), ("crossed-same-family", 2))
        self.assertEqual(len(families), 1)

    def test_independent(self):
        meta = {
            "a": {"author": "作者甲", "kind": "essay"},
            "b": {"author": "作者乙", "kind": "essay"},
        }
        tier, n, _ = wiki.compute_evidence_tier(self.page(["a", "b"]), meta)
        self.assertEqual((tier, n), ("crossed-independent", 2))

    def test_primary(self):
        meta = {"a": {"author": "作者甲", "kind": "paper"}}
        tier, n, _ = wiki.compute_evidence_tier(self.page(["a"]), meta)
        self.assertEqual((tier, n), ("primary", 1))

    def test_confidence_note_detected(self):
        page = SimpleNamespace(fm={"confidence_note": "单源但为一手原文"})
        self.assertTrue(wiki.has_confidence_note(page))
        page = SimpleNamespace(fm={"confidence_note": "  "})
        self.assertFalse(wiki.has_confidence_note(page))


class GapTableTests(unittest.TestCase):
    def test_empty_gap_table(self):
        body = "## 当前缺口\n\n| 缺口 | 卡在哪 |\n|---|---|\n\n## 下一步\n"
        self.assertEqual(wiki.gap_table_rows(body), 0)

    def test_one_gap_row(self):
        body = "## 当前缺口\n\n| 缺口 | 卡在哪 |\n|---|---|\n| 缺素材 | 没有一手来源 |\n"
        self.assertEqual(wiki.gap_table_rows(body), 1)


class StatsTests(unittest.TestCase):
    def test_stats_prints_project_and_hubs(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            code = wiki.cmd_stats(ROOT)
        out = buf.getvalue()
        self.assertEqual(code, 0)
        self.assertIn("项目（按阶段）", out)
        self.assertIn("枢纽页 Top 5", out)


class RepoDoctorTests(unittest.TestCase):
    def test_doctor_has_no_inconsistency(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            code = wiki.cmd_doctor(ROOT)
        self.assertEqual(code, 0, buf.getvalue())


if __name__ == "__main__":
    unittest.main()
