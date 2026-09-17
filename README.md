# llm-wiki

一套基于 [Karpathy 的 LLM Wiki 构想](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) 构建的、可直接运行的个人知识库系统。

**核心主张**：不要让 LLM 每次提问都从原始文档里重新检索。让它**增量编译**一份持久、互相链接的 Markdown 知识库 —— 知识编译一次，然后持续保鲜。

---

## 快速开始

```bash
# 1. 看一眼体检报告
python3 tools/wiki.py stats

# 2. 生成浏览站点（单文件 HTML，无需安装任何东西）
python3 tools/wiki.py build
open site/index.html

# 3. 全文检索
python3 tools/wiki.py search "复利"

# 4. 健康检查
python3 tools/wiki.py lint
```

用 Obsidian 打开本目录也可以直接浏览：双链跳转、反向链接、图谱视图全部可用（附件目录已预设为 `raw/assets`）。

---

## 三层架构

| 层 | 位置 | 谁写 | 谁读 | 内容 |
|---|---|---|---|---|
| 原始素材 | `raw/` | 人类 | LLM（只读） | 文章、论文、笔记、PDF、图片 |
| 知识库 | `wiki/` | LLM | 人类 | 摘要、实体、概念、分析、交叉引用 |
| 规范 | `AGENTS.md` | 共同演进 | LLM | 结构、约定、工作流 |

`raw/` **不可变** —— 它是事实来源。需要修正时，在 `wiki/` 里写清楚「素材原文如此，但应理解为 X」。

---

## 目录结构

```
llm-wiki/
├── AGENTS.md              # Schema 层：LLM 维护手册（先读这个）
├── README.md
├── raw/                   # 原始素材（人类写入，LLM 只读）
│   └── assets/            #   图片、附件
├── wiki/                  # LLM 生成并维护的知识库
│   ├── index.md           #   内容索引（自动生成）
│   ├── log.md             #   操作日志（append-only）
│   ├── overview.md        #   总览
│   ├── conventions.md     #   人类的使用偏好
│   ├── sources/           #   素材摘要页
│   ├── entities/          #   实体页
│   ├── concepts/          #   概念页
│   └── analyses/          #   分析页
├── tools/wiki.py          # 零依赖工具链
├── templates/             # 页面模板
└── site/index.html        # 生成的浏览站点
```

---

## 工具链

只依赖 Python 标准库，**不需要 pip install**。

```bash
python3 tools/wiki.py <command>

  init [path]              初始化一个新的知识库
  lint                     健康检查：断链、孤岛、缺 frontmatter、未收录素材
  stats                    统计：页面数、链接数、枢纽页
  search "<query>"         BM25 全文检索（中文按二字组切分）
  index                    从各页 frontmatter 重建 wiki/index.md
  build                    生成单文件浏览站点 site/index.html
  log <type> "<message>"   追加一条日志
  new <type> <slug>        按模板新建页面
  graph                    打印链接关系
```

---

## 三个操作

### Ingest —— 收录素材

```bash
cp my-article.md raw/2026-09-18-my-article.md
# 然后对 LLM 说：「收录这篇」
```

LLM 会：读素材 → 与你对齐要点（**特别指出与已有页面的矛盾**）→ 写摘要页 → 拆实体/概念页 → **回填所有被影响的旧页面** → 更新索引 → 写日志 → 跑 lint。

一份素材通常触及 **10-15 个页面**。只写摘要页是失败的做法。

### Query —— 查询

```bash
python3 tools/wiki.py search "RAG 和 wiki 的区别"
# 或者直接对 LLM 说：「对比一下 RAG 和 Wiki 模式」
```

先读 `wiki/index.md` 定位候选页，再深入阅读，**带引用**作答。

**好答案要归档。** 一次对比、一份分析、一个新发现的连接 —— 写入 `wiki/analyses/`，回填索引与日志。这样探索也会复利，而不是消失在聊天记录里。

### Lint —— 体检

```bash
python3 tools/wiki.py lint
```

脚本负责机器可查的部分（断链、孤岛、缺字段、未收录素材）；LLM 负责语义部分（矛盾、过期、该建未建）。体检同时是**选题引擎** —— 它会告诉你下一步该找什么素材、该问什么问题。

---

## 页面规范

每个页面都带 YAML frontmatter：

```yaml
---
title: 页面标题
type: concept            # source | entity | concept | analysis | meta
slug: page-slug          # 全库唯一，与文件名一致
tags: [知识库, 模式]
created: 2026-09-18
updated: 2026-09-18
sources: [2026-09-18-karpathy-llm-wiki]
related: [other-slug]
confidence: high         # high | medium | low
status: active           # active | draft | stale | deprecated
---
```

链接语法：`[[slug]]` 或 `[[slug|显示文本]]`。**只能链接已存在的页面**，`lint` 会报断链。

完整规范见 `AGENTS.md`。

---

## 当前内容

已收录 **2 份素材**，编译为 **21 个页面**（142 条交叉链接）：

- **素材**：Karpathy 的 LLM Wiki Gist、second-brain-skill 的仓库 README
- **概念**：LLM Wiki 模式、三层架构、三个操作、索引与日志、复利式知识积累、Wiki 体检、适用场景、纯文本与 Git
- **实体**：Andrej Karpathy、Vannevar Bush / Memex、Obsidian、qmd、NotebookLM
- **分析**：RAG 与 LLM Wiki 对比、second-brain-skill 评估

入口：`wiki/overview.md`

## 版本控制

本仓库就是一个 git 仓库 —— 正如 Gist 所说，wiki 只是一堆 Markdown 文件，版本历史、分支、协作都是白送的。

```bash
git log --oneline                    # 看知识库的演化
git diff HEAD~1 -- wiki/             # 看上次 ingest 改了什么
git checkout HEAD~1 -- wiki/foo.md   # 回退 LLM 改错的页面
```

`site/`（生成产物）与 `.workbuddy-ai/`（助手工作记忆）已通过 `.gitignore` 排除。

## 素材重抓

网页抓取会丢行内链接、把 `→` 转成 `->`。因此同一素材重新抓取时**不覆盖旧文件**，而是加 `-r2` 后缀并存：

```
raw/2026-09-18-karpathy-llm-wiki.md      # r1（丢失了行内链接）
raw/2026-09-18-karpathy-llm-wiki-r2.md   # r2（完整，引用时用这份）
```

两版差异记录在对应的 `wiki/sources/` 摘要页里。只要目标提供结构化端点（GitHub API、`gist.githubusercontent.com/.../raw`），就优先用它而不是抓渲染后的 HTML。

---

## 为什么这样可行

维护知识库真正累人的不是阅读和思考，而是**记账** —— 更新交叉引用、保持摘要新鲜、记录矛盾、维持几十个页面的一致性。人类放弃 wiki 是因为维护成本增长快于价值增长。

LLM 不会厌烦，不会忘记更新某个引用，能一次改动 15 个文件。**当维护成本接近零，wiki 才第一次变得可持续。**

人类负责挑素材、提问题、判断什么重要。其余全部交给 LLM。

---

## 致谢

- [Andrej Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) —— LLM Wiki 原始构想
- [Vannevar Bush](https://en.wikipedia.org/wiki/Vannevar_Bush) —— 1945 年的 Memex 构想

## License

MIT
