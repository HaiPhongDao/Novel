"""Gửi câu hỏi / nhiệm vụ tới Argon (Gemini Web) qua extension Edge, lưu câu trả lời ra file.

Dùng:
    python tools/gemini_web_run.py --prompt <file> --out <file ra> [--think-out <file>] [--url <url>]
"""
import argparse
import hashlib
import json
import os
import sys
import threading
import time
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

EXT = Path(__file__).parent / "aistudio-ext"
DEFAULT_URL = "https://gemini.google.com/u/1/app?pageId=none"
PICKUP_S = 90


def log(msg):
    print(msg, file=sys.stderr, flush=True)


class Bridge:
    def __init__(self):
        self.cv = threading.Condition()
        self.jobs = {}

    def submit(self, job):
        with self.cv:
            self.jobs[job["id"]] = {"job": job, "picked": False, "result": None}
            self.cv.notify_all()

    def _free(self):
        return next((s for s in self.jobs.values() if not s["picked"]), None)

    def take(self, wait):
        with self.cv:
            self.cv.wait_for(self._free, timeout=wait)
            s = self._free()
            if s:
                s["picked"] = True
                self.cv.notify_all()
                return s["job"]
        return None

    def alive(self, jid):
        with self.cv:
            s = self.jobs.get(jid)
            return bool(s and s["result"] is None)

    def release(self, res):
        with self.cv:
            s = self.jobs.get(res.get("id"))
            if s and s["result"] is None:
                s["picked"] = False
                self.cv.notify_all()

    def finish(self, res):
        with self.cv:
            s = self.jobs.get(res.get("id"))
            if s:
                s["result"] = res
                self.cv.notify_all()

    def wait(self, jid, key, timeout):
        with self.cv:
            return self.cv.wait_for(lambda: self.jobs[jid][key], timeout=timeout)

    def drop(self, jid):
        with self.cv:
            return self.jobs.pop(jid, None)


def ext_hash():
    h = hashlib.sha1()
    for f in sorted(EXT.iterdir()):
        if f.is_file():
            h.update(f.name.encode() + f.read_bytes())
    return h.hexdigest()[:12]


def make_handler(bridge):
    code = ext_hash()

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def _from_web_page(self):
            if self.headers.get("Origin", "").startswith(("http://", "https://")):
                self.send_response(403)
                self.end_headers()
                return True
            return False

        def _send(self, status, obj=None):
            body = json.dumps(obj, ensure_ascii=False).encode("utf-8") if obj is not None else b""
            self.send_response(status)
            self.send_header("X-Ext-Hash", code)
            if body:
                self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self):
            if self._from_web_page():
                return
            u = urlparse(self.path)
            if u.path == "/alive":
                return self._send(200 if bridge.alive(parse_qs(u.query).get("id", [""])[0]) else 410)
            if u.path != "/job":
                return self._send(404)
            wait = min(float(parse_qs(u.query).get("wait", ["0"])[0]), 25)
            job = bridge.take(wait)
            self._send(200, job) if job else self._send(204)

        def do_POST(self):
            if self._from_web_page():
                return
            data = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))) or b"{}")
            if self.path == "/log":
                log(data.get("msg", ""))
            elif self.path == "/result":
                bridge.finish(data)
            elif self.path == "/release":
                log("extension reload bản mới, trả lại việc")
                bridge.release(data)
            else:
                return self._send(404)
            self._send(200, {})

    return Handler


def run_gemini_web(prompt_text, out_path, url=DEFAULT_URL, reuse_tab=True, timeout_min=20, think_out=None, thinking="High", port=8765):
    bridge = Bridge()
    try:
        server = ThreadingHTTPServer(("127.0.0.1", port), make_handler(bridge))
    except OSError as e:
        log(f"cổng {port} đang bận ({e})")
        return False, f"Cổng {port} đang bận"

    threading.Thread(target=server.serve_forever, daemon=True).start()
    jid = uuid.uuid4().hex
    job = {
        "id": jid,
        "url": url,
        "prompt": prompt_text,
        "reuseTab": reuse_tab,
        "thinking": thinking,
        "timeoutMin": timeout_min
    }
    bridge.submit(job)

    try:
        log(f"Đang chờ extension nhận việc (tối đa {PICKUP_S}s)...")
        if not bridge.wait(jid, "picked", PICKUP_S):
            raise RuntimeError(f"Extension không nhận việc sau {PICKUP_S}s. Hãy đảm bảo Edge đang mở và extension đã bật!")
        log(f"Extension đã nhận việc. Đang gửi câu hỏi tới Argon trên Gemini Web...")
        if not bridge.wait(jid, "result", timeout_min * 60 + 180):
            raise RuntimeError(f"Quá {timeout_min} phút chưa có kết quả từ Argon")
        res = bridge.jobs[jid]["result"]
    finally:
        bridge.drop(jid)
        server.shutdown()

    if not res.get("ok"):
        raise RuntimeError(res.get("error", "Lỗi không xác định từ extension"))

    text = res.get("text", "").strip()
    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text + "\n", encoding="utf-8")
    log(f"Đã lưu câu trả lời của Argon: {len(text)} ký tự -> {out_path}")

    if think_out and res.get("think"):
        th = res["think"].strip()
        tp = Path(think_out)
        tp.parent.mkdir(parents=True, exist_ok=True)
        tp.write_text(th + "\n", encoding="utf-8")
        log(f"Đã lưu thinking: {len(th)} ký tự -> {think_out}")

    return True, text


def main():
    ap = argparse.ArgumentParser(description="Chạy câu hỏi tới Argon trên Gemini Web qua extension")
    ap.add_argument("--prompt", required=True, help="Đường dẫn file chứa prompt")
    ap.add_argument("--out", required=True, help="Đường dẫn file xuất kết quả")
    ap.add_argument("--url", default=DEFAULT_URL, help="URL Gemini Web (mặc định: /u/1/app?pageId=none)")
    ap.add_argument("--no-reuse-tab", action="store_true", help="Không dùng lại tab đang mở mà mở tab mới")
    ap.add_argument("--thinking", default="High", help="Mức suy nghĩ (High / Medium / Low / on / off)")
    ap.add_argument("--think-out", help="Đường dẫn file lưu phần thinking (nếu có)")
    ap.add_argument("--timeout", type=int, default=20, help="Phút chờ tối đa")
    ap.add_argument("--port", type=int, default=8765, help="Port HTTP bridge")
    args = ap.parse_args()

    prompt_text = Path(args.prompt).read_text(encoding="utf-8")
    try:
        ok, res = run_gemini_web(
            prompt_text=prompt_text,
            out_path=args.out,
            url=args.url,
            reuse_tab=not args.no_reuse_tab,
            timeout_min=args.timeout,
            think_out=args.think_out,
            thinking=args.thinking,
            port=args.port
        )
        if ok:
            print(f"XONG: {args.out}")
            return 0
        return 1
    except Exception as e:
        log(f"LỖI: {e}")
        return 2


if __name__ == "__main__":
    sys.exit(main())
