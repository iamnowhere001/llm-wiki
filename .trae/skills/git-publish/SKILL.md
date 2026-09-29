---
name: git-publish
description: 提交并推送本仓库到 GitHub，自动绕过 github.com DNS 污染（健康 IP 探测、本地 CONNECT 代理、重试与远程 SHA 校验）。当用户要求提交、推送到 git 或 GitHub 时使用。
---

# Git Publish（llm-wiki 专用）

把工作区改动提交并推送到 `github.com/iamnowhere001/llm-wiki`。本机网络对 **github.com 有 DNS 污染**（解析到不可达 IP，443 超时），但 `api.github.com` 正常 —— 推送走「健康 IP + 本地 CONNECT 代理」，校验走 API。

## 1. 盘点与暂存

1. `git status --porcelain` 盘点，按目录/状态分类计数（本库一次改动常达数百文件，输出重定向到文件再聚合，不要直接刷屏）。
2. **本仓库约定**：`tools/_` 前缀脚本（`_backfill_*`、`_sync_*` 等）是含机器绝对路径的一次性工具，**不入库**。用 `git add -A` 后 `git reset -q <files>` 排除。
3. 提交前必须核对暂存范围：`git diff --cached --name-status | awk '{print $1}' | sort | uniq -c`，确认增/删/改计数与未暂存清单。
4. **并发会话可能存在**（另一个 agent/终端在写同一仓库，本库已实际发生）：
   - 遇 `.git/index.lock`：先 `ps aux | grep '[g]it'` 确认无活跃 git 进程、且锁文件时间戳陈旧（数分钟以上、0 字节），才可 `rm .git/index.lock`。
   - 提交后 `git log --oneline -5` 可能出现非本次产生的中间提交，属正常；推送前确认目标提交在 main 祖先链上（`git merge-base --is-ancestor`）。
5. 提交信息：Conventional Commits 前缀（`docs` / `chore` / `refactor`）+ 中文一行摘要，大批次附 body 列要点。仓库有提交钩子，可能改写消息或自行补提 —— 以 `git log` 实际结果为准，**不要 amend**。
6. 不代跑 wiki 内容流程（index / lint / build）——那些由内容任务负责，本技能只发布已存在的改动。

## 2. 推送（DNS 污染绕过）

1. 确认远程存在：`git remote -v`。缺失则 `git remote add origin https://github.com/iamnowhere001/llm-wiki.git`；若写全局/仓库配置被沙箱拒绝，不影响后续用完整 URL 推送。
2. 后台启动代理：`python3 <本技能目录>/scripts/gh-connect-proxy.py`
   - 监听 `127.0.0.1:8889`，日志打印每个连接选用的 IP。
   - 代理内置静态健康 IP 列表；全挂时自动走 DoH（Cloudflare / Google）发现新 IP。
3. 执行 `bash <本技能目录>/scripts/push-main.sh [branch]`（默认 main）：内置 8 次重试、强制 HTTP/1.1、500MB `postBuffer`、关闭低速超时。
4. **断流不等于失败**：出现 `Broken pipe` / `remote end hung up unexpectedly` 时，服务端可能已完成 ref 更新；重试输出 `Everything up-to-date` 即代表已成功。
5. 完成判定只认远程 SHA（api.github.com 不受污染）：
   - 本地：`git rev-parse HEAD`
   - 远程：`curl -sS https://api.github.com/repos/iamnowhere001/llm-wiki/branches/main` 取 `commit.sha`
   - 两者完全一致才算成功；不一致则继续重试推送。
6. 收尾：停掉代理进程。脚本常驻本技能的 `scripts/` 目录，**不要复制到 `/tmp`**（系统重启会清空，已踩过一次）。

## 3. 异常速查

- `CONNECT tunnel failed, response 502`：静态 IP 短时全部不可用。代理会自动 DoH 发现；仍失败就手动 `curl --resolve github.com:443:<ip> .../info/refs?service=git-receive-pack` 逐个探测，把新的健康 IP 加到代理脚本 `STATIC_IPS` 顶部。
- `invalid credentials` / `failed to get: 100013`：osxkeychain 在沙箱内不可用。推送脚本已用 `https://x-access-token:$(gh auth token)@github.com/...` 并加 `-c credential.helper=`，不要改用全局凭据配置。
- 首次推送超大仓库（数百 MB）在收尾反复断连：改为逐提交增量推 —— `git rev-list --reverse main` 从根提交开始，逐个 `push <sha>:refs/heads/main`（每个带重试，脚本可作模板）。
- 端口被占：`lsof -ti :8889 | xargs kill` 后重启代理。
- 判断网络是否还是同一症状：`curl -m 10 https://github.com` 超时、而 `curl -m 10 https://api.github.com` 返回 200，即仍是 DNS 污染，按本流程走。
