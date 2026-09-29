#!/bin/bash
# Retry-push a branch of llm-wiki to GitHub through the local pollution-bypass
# CONNECT proxy (scripts/gh-connect-proxy.py must already be running on :8889).
#
# Usage: bash push-main.sh [branch]      # default: main
#
# "Everything up-to-date" on a retry after a broken pipe means the earlier
# attempt actually succeeded server-side. Always verify with the remote SHA
# afterwards (see SKILL.md).
set -u

BRANCH="${1:-main}"
REPO="iamnowhere001/llm-wiki"
cd "$(git rev-parse --show-toplevel)" || exit 2

if ! nc -z 127.0.0.1 8889 2>/dev/null; then
  echo "proxy not listening on 127.0.0.1:8889 — start scripts/gh-connect-proxy.py first" >&2
  exit 2
fi

TOKEN="$(gh auth token)" || { echo "gh auth token failed; run: gh auth login" >&2; exit 2; }
URL="https://x-access-token:${TOKEN}@github.com/${REPO}.git"
export HTTPS_PROXY="http://127.0.0.1:8889"
export HTTP_PROXY="http://127.0.0.1:8889"

GIT_OPTS=(
  -c credential.helper=
  -c http.version=HTTP/1.1
  -c http.postBuffer=524288000
  -c http.lowSpeedLimit=0
  -c http.lowSpeedTime=999999
)

for n in $(seq 1 8); do
  echo "=== push ${BRANCH} attempt ${n} $(date +%H:%M:%S) ==="
  if git "${GIT_OPTS[@]}" push --progress "$URL" "$BRANCH" 2>&1; then
    echo "PUSH_OK"
    exit 0
  fi
  echo "attempt ${n} failed; retrying in 8s ..." >&2
  sleep 8
done

echo "PUSH_FAILED after 8 attempts — check proxy log and probe healthy IPs" >&2
exit 1
