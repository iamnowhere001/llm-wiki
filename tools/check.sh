#!/usr/bin/env bash
# 仓库统一门禁：本地 pre-commit 与 CI 都跑这一份，避免两套规则漂移。
set -euo pipefail
cd "$(dirname "$0")/.."

python3 -m py_compile tools/wiki.py
python3 -m unittest discover -s tests -p 'test_*.py'

python3 tools/wiki.py lint
python3 tools/wiki.py doctor
python3 tools/wiki.py rawcheck
python3 tools/wiki.py overview-stats
python3 tools/wiki.py template-check
python3 tools/wiki.py readme-check
python3 tools/wiki.py proposals
