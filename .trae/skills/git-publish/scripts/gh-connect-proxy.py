#!/usr/bin/env python3
"""Local HTTP CONNECT proxy that bypasses github.com DNS pollution.

Per CONNECT to github.com:
  1. try a static list of known-good GitHub edge IPs
  2. if all fail, discover fresh A records via DNS-over-HTTPS (Cloudflare/Google)
  3. repeat discovery for up to 3 rounds

Only CONNECT requests to github.com are accepted.
Run:  python3 gh-connect-proxy.py        (listens on 127.0.0.1:8889)
Stop: kill the process / lsof -ti :8889 | xargs kill
"""
import json
import socket
import socketserver
import ssl
import threading
import urllib.request

LISTEN_PORT = 8889
ALLOWED_HOST = "github.com"
STATIC_IPS = [
    "20.27.177.113",   # Azure-backed edge, historically the most stable here
    "140.82.112.3",
    "140.82.112.4",
    "140.82.112.6",
    "140.82.113.3",
    "140.82.113.4",
    "140.82.114.3",
    "140.82.114.4",
    "140.82.121.3",
    "140.82.121.4",
]
DOH_URLS = [
    "https://1.1.1.1/dns-query?name=github.com&type=A",
    "https://1.0.0.1/dns-query?name=github.com&type=A",
    "https://8.8.8.8/resolve?name=github.com&type=A",
]
# Ignore environment proxies for DoH discovery; tolerate cert quirks on edge IPs.
_opener = urllib.request.build_opener(
    urllib.request.ProxyHandler({}),
    urllib.request.HTTPSHandler(context=ssl._create_unverified_context()),
)


def discover_ips():
    """Fresh github.com A records via DoH. Returns [] when every endpoint fails."""
    for url in DOH_URLS:
        try:
            req = urllib.request.Request(url, headers={"accept": "application/dns-json"})
            with _opener.open(req, timeout=8) as resp:
                data = json.load(resp)
            ips = [a["data"] for a in data.get("Answer", []) if a.get("type") == 1]
            if ips:
                print(f"DoH {url.split('/')[2]} -> {ips}", flush=True)
                return ips
        except OSError as exc:
            print(f"DoH {url.split('/')[2]} fail: {exc}", flush=True)
    return []


def connect_upstream(port):
    """Try static IPs, then DoH-discovered IPs, for up to 3 rounds."""
    extra = []
    for round_i in range(3):
        for ip in STATIC_IPS + extra:
            try:
                sock = socket.create_connection((ip, port), timeout=6)
                print(f"connect {ip} ok (round {round_i + 1})", flush=True)
                return sock
            except OSError as exc:
                print(f"connect {ip} fail: {exc}", flush=True)
        extra = discover_ips()
    return None


class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        data = b""
        while b"\r\n\r\n" not in data:
            chunk = self.request.recv(4096)
            if not chunk:
                return
            data += chunk
        line = data.split(b"\r\n", 1)[0].decode("latin1")
        parts = line.split()
        if len(parts) < 2 or parts[0].upper() != "CONNECT":
            self.request.sendall(b"HTTP/1.1 405 Method Not Allowed\r\n\r\n")
            return
        host, _, port_s = parts[1].rpartition(":")
        if host != ALLOWED_HOST:
            self.request.sendall(b"HTTP/1.1 403 Forbidden\r\n\r\n")
            return
        upstream = connect_upstream(int(port_s or "443"))
        if upstream is None:
            self.request.sendall(b"HTTP/1.1 502 Bad Gateway\r\n\r\n")
            return
        self.request.sendall(b"HTTP/1.1 200 Connection Established\r\n\r\n")

        def relay(src, dst):
            try:
                while True:
                    buf = src.recv(65536)
                    if not buf:
                        break
                    dst.sendall(buf)
            except OSError:
                pass
            finally:
                # Half-close only: a full bidirectional shutdown kills the
                # response still flowing back on the other direction.
                try:
                    dst.shutdown(socket.SHUT_WR)
                except OSError:
                    pass

        threading.Thread(
            target=relay, args=(upstream, self.request), daemon=True
        ).start()
        relay(self.request, upstream)


class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True
    daemon_threads = True


if __name__ == "__main__":
    with ThreadingTCPServer(("127.0.0.1", LISTEN_PORT), Handler) as srv:
        print(f"proxy listening on 127.0.0.1:{LISTEN_PORT} for {ALLOWED_HOST}", flush=True)
        srv.serve_forever()
