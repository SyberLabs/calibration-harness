# Copyright (c) 2026 sykosyber (mateorobles100@icloud.com)
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
"""A loopback proxy that lets the Runvil gateway reach OpenAI's reasoning models.

Runvil's harness client speaks the convention of self-hosted servers (vLLM,
llama.cpp): "no thinking" is `chat_template_kwargs.enable_thinking = false`,
and the output limit is `max_tokens`. OpenAI's reasoning models, such as
gpt-6-luna, refuse all three of those with a 400: an unknown parameter, a
renamed one, and any `temperature` but 1 unless reasoning is switched off with
`reasoning_effort = "none"`. paperweight's Lua asks for temperature 0.3.

The proxy sits between the gateway and api.openai.com and rewrites only the
request body (`rewrite_request`); responses, streamed or not, pass through
byte for byte. It holds the API key, read once from an environment variable,
so the gateway's endpoint key is a placeholder and the real key exists in one
process only. It binds to loopback and is meant for calibration runs, not
production.

    uv run python -m calibrate.openai_proxy --port 18090 --key-env OPENAI_API_KEY_V2
"""

from __future__ import annotations

import argparse
import http.client
import json
import logging
import os
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit

log = logging.getLogger("calibrate.openai_proxy")

UPSTREAM = "https://api.openai.com"
DEFAULT_PORT = 18090
UPSTREAM_TIMEOUT_SECONDS = 600
CHUNK_BYTES = 8192
# Response headers that describe the upstream connection, not the body.
HOP_HEADERS = frozenset({"connection", "transfer-encoding", "keep-alive", "content-length",
                         "content-encoding"})


def rewrite_request(body: dict) -> dict:
    """The chat request as OpenAI's reasoning models accept it.

    - `chat_template_kwargs` is dropped. When it does not ask for thinking,
      `reasoning_effort` becomes "none" unless the caller set one; when it
      does, the model's own default effort stands.
    - `max_tokens` becomes `max_completion_tokens`.
    Everything else passes through unchanged.
    """
    out = dict(body)
    kwargs = out.pop("chat_template_kwargs", None)
    wants_thinking = isinstance(kwargs, dict) and kwargs.get("enable_thinking") is True
    if not wants_thinking:
        out.setdefault("reasoning_effort", "none")
    if "max_tokens" in out:
        out.setdefault("max_completion_tokens", out["max_tokens"])
        del out["max_tokens"]
    return out


class _Counter:
    def __init__(self) -> None:
        self.lock = threading.Lock()
        self.requests = 0
        self.failures = 0

    def add(self, ok: bool) -> tuple[int, int]:
        with self.lock:
            self.requests += 1
            self.failures += 0 if ok else 1
            return self.requests, self.failures


def make_handler(api_key: str, upstream: str = UPSTREAM) -> type[BaseHTTPRequestHandler]:
    target = urlsplit(upstream)
    counter = _Counter()

    class Handler(BaseHTTPRequestHandler):
        # HTTP/1.0: the connection closes after each response, so a streamed
        # body needs no length and no chunked framing.
        protocol_version = "HTTP/1.0"

        def log_message(self, format: str, *args: object) -> None:  # noqa: A002 - stdlib signature
            return None

        def _forward(self, method: str, body: bytes | None) -> None:
            conn = http.client.HTTPSConnection(target.hostname or "", target.port or 443,
                                               timeout=UPSTREAM_TIMEOUT_SECONDS)
            headers = {"Authorization": f"Bearer {api_key}", "Accept": self.headers.get("Accept", "*/*")}
            if body is not None:
                headers["Content-Type"] = "application/json"
            try:
                conn.request(method, self.path, body=body, headers=headers)
                resp = conn.getresponse()
                self.send_response(resp.status)
                for name, value in resp.getheaders():
                    if name.lower() not in HOP_HEADERS:
                        self.send_header(name, value)
                self.end_headers()
                while chunk := resp.read1(CHUNK_BYTES):
                    self.wfile.write(chunk)
                    self.wfile.flush()
                n, failed = counter.add(resp.status < 400)
                if resp.status >= 400 or n % 25 == 0:
                    log.info("%s %s -> %d (%d requests, %d failed)", method, self.path, resp.status, n, failed)
            except OSError as error:
                # One failed call is reported to the caller and counted; the proxy keeps serving.
                counter.add(False)
                log.warning("%s %s failed upstream: %s", method, self.path, error)
                self.send_error(502, "upstream unreachable")
            finally:
                conn.close()

        def do_GET(self) -> None:
            self._forward("GET", None)

        def do_POST(self) -> None:
            raw = self.rfile.read(int(self.headers.get("Content-Length", "0")))
            try:
                body = json.loads(raw)
            except json.JSONDecodeError:
                self.send_error(400, "request body is not JSON")
                return
            if self.path.rstrip("/").endswith("/chat/completions") and isinstance(body, dict):
                body = rewrite_request(body)
            self._forward("POST", json.dumps(body).encode("utf-8"))

    return Handler


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="openai-proxy: %(message)s")
    parser = argparse.ArgumentParser(description="Loopback proxy from the Runvil gateway to OpenAI.")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    parser.add_argument("--key-env", default="OPENAI_API_KEY", help="environment variable holding the API key")
    args = parser.parse_args()
    api_key = os.environ.get(args.key_env, "").strip()
    if not api_key:
        raise SystemExit(f"openai-proxy: {args.key_env} is not set")
    server = ThreadingHTTPServer(("127.0.0.1", args.port), make_handler(api_key))
    log.info("listening on 127.0.0.1:%d, forwarding to %s", args.port, UPSTREAM)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
