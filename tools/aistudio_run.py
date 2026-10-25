"""Gửi một tin nhắn tới Gemini trong Google AI Studio qua extension Edge, lưu câu trả lời ra file.

Script mở server nhỏ ở 127.0.0.1:8765 và giao việc; extension tools/aistudio-ext (nạp vào Edge chính
bằng edge://extensions → Developer mode → Load unpacked) nhận việc, bấm nút trong một tab AI Studio riêng
rồi gửi câu trả lời về. Edge chỉ cần đang mở.

Dùng:
    # mở session mới (SI + session-start), tự đổi tài khoản /u/0 → /u/1 → /u/2 khi hết quota
    python tools/aistudio_run.py --new --si <file SI> --prompt <file> --out <file ra> [--note "..."]
    # gửi tiếp vào chat của lần chạy trước (đoạn kế, ghi chú sửa)
    python tools/aistudio_run.py --prompt <file> --out <file ra> [--chat <url>]

Mã thoát: 0 xong · 2 lỗi (trang, selector, extension không nhận việc) · 3 hết quota (mọi tài khoản đã thử,
hoặc đang gửi tiếp vào chat cũ)
"""
import argparse
import hashlib
import json
import sys
import threading
import time
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

STATE = Path(__file__).with_name(".aistudio_state.json")
EXT = Path(__file__).with_name("aistudio-ext")
BASE = "https://aistudio.google.com/u/{}/prompts/new_chat"
PICKUP_S = 90  # alarm của extension đánh thức mỗi 30s


def log(msg):
    print(msg, file=sys.stderr, flush=True)


class Bridge:
    """Một việc đang chờ extension nhận, và kết quả của nó."""

    def __init__(self):
        self.cv = threading.Condition()
        self.job = None
        self.picked = False
        self.result = None

    def submit(self, job):
        with self.cv:
            self.job, self.picked, self.result = job, False, None
            self.cv.notify_all()

    def take(self, wait):
        with self.cv:
            self.cv.wait_for(lambda: self.job and not self.picked, timeout=wait)
            if self.job and not self.picked:
                self.picked = True
                self.cv.notify_all()
                return self.job
        return None

    def release(self, res):
        with self.cv:
            if self.job and res.get("id") == self.job["id"] and self.result is None:
                self.picked = False
                self.cv.notify_all()

    def finish(self, res):
        with self.cv:
            if self.job and res.get("id") == self.job["id"]:
                self.result = res
                self.cv.notify_all()

    def wait(self, pred, timeout):
        with self.cv:
            return self.cv.wait_for(pred, timeout=timeout)


def ext_hash():
    """Hash các file extension; extension tự reload khi hash này khác lúc nó được nạp."""
    h = hashlib.sha1()
    for f in sorted(EXT.iterdir()):
        h.update(f.name.encode() + f.read_bytes())
    return h.hexdigest()[:12]


def make_handler(bridge):
    code = ext_hash()

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def _from_web_page(self):
            # Trang web bất kỳ cũng gọi được localhost; chỉ nhận yêu cầu từ extension (không có Origin http/https).
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
                job = bridge.job
                ok = job and job["id"] == parse_qs(u.query).get("id", [""])[0] and bridge.result is None
                return self._send(200 if ok else 410)
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
                log("extension tự nạp lại bản mới, giao lại việc")
                bridge.release(data)
            else:
                return self._send(404)
            self._send(200, {})

    return Handler


class Quota(Exception):
    pass


def run(bridge, job, timeout_min):
    job = dict(job, id=uuid.uuid4().hex, timeoutMin=timeout_min)
    bridge.submit(job)
    if not bridge.wait(lambda: bridge.picked, PICKUP_S):
        raise RuntimeError(f"extension không nhận việc sau {PICKUP_S}s — Edge có đang mở, "
                           "extension 'Novel AI Studio bridge' đã nạp và đang bật?")
    if not bridge.wait(lambda: bridge.result is not None, timeout_min * 60 + 180):
        raise RuntimeError(f"quá {timeout_min} phút chưa có kết quả")
    res = bridge.result
    if res.get("ok"):
        if res.get("warning"):
            log(f"cảnh báo trên trang: {res['warning'][:200]}")
        return res
    if res.get("kind") == "quota":
        raise Quota(res.get("error", ""))
    raise RuntimeError(res.get("error", "lỗi không rõ"))


def pick_text(dom, md):
    # Markdown giữ được định dạng; chỉ dùng khi khớp với chữ trên trang (cùng số chữ Hán ±2%).
    han = lambda s: sum(1 for c in s if "一" <= c <= "鿿")
    if md and abs(han(md) - han(dom)) <= max(5, han(dom) * 0.02):
        return md
    return dom


def save_state(state):
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding="utf-8")


def main():
    for s in (sys.stdout, sys.stderr):
        s.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--new", action="store_true", help="mở chat mới (cần --si)")
    ap.add_argument("--si")
    ap.add_argument("--chat", help="URL chat để gửi tiếp (mặc định: chat của lần chạy trước)")
    ap.add_argument("--accounts", default="0,1,2", help="thứ tự tài khoản /u/N thử khi hết quota")
    ap.add_argument("--model", default="gemini-3.8-flash")
    ap.add_argument("--thinking", default="High")
    ap.add_argument("--note", default="")
    ap.add_argument("--port", type=int, default=8765, help="phải khớp host_permissions của extension")
    ap.add_argument("--timeout", type=int, default=20, help="phút chờ tối đa cho một câu trả lời")
    ap.add_argument("--think-out", help="lưu phần thinking của Gemini ra file này (để đọc khi chỉnh SI)")
    args = ap.parse_args()
    if args.new and not args.si:
        ap.error("--new cần --si")

    prompt = Path(args.prompt).read_text(encoding="utf-8")
    state = json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {}

    bridge = Bridge()
    try:
        server = ThreadingHTTPServer(("127.0.0.1", args.port), make_handler(bridge))
    except OSError as e:
        log(f"cổng {args.port} đang bận — có lần chạy khác chưa xong? ({e})")
        return 2
    threading.Thread(target=server.serve_forever, daemon=True).start()

    start = time.time()
    base = dict(prompt=prompt, model=args.model, thinking=args.thinking)
    res = None
    try:
        if args.new:
            si = Path(args.si).read_text(encoding="utf-8")
            accounts = [a.strip() for a in args.accounts.split(",")]
            today = time.strftime("%Y-%m-%d")
            if state.get("quota_account") in accounts and state.get("quota_day") == today:
                i = accounts.index(state["quota_account"])
                accounts = accounts[i + 1:] + accounts[:i + 1]  # tài khoản hết quota hôm nay để cuối
            for n, acct in enumerate(accounts):
                try:
                    res = run(bridge, dict(base, mode="new", si=si, url=BASE.format(acct)), args.timeout)
                    break
                except Quota as q:
                    log(f"/u/{acct} hết quota: {str(q)[:200]}")
                    state.update(quota_account=acct, quota_day=today)
                    save_state(state)
                    if n == len(accounts) - 1:
                        raise
            state.update(account=acct)
        else:
            url = args.chat or state.get("chat")
            if not url:
                log("chưa có chat nào — dùng --new hoặc --chat")
                return 2
            res = run(bridge, dict(base, mode="continue", url=url), args.timeout)
    except Quota as q:
        log(f"HẾT QUOTA: {str(q)[:300]}")
        if not args.new:
            log("chat cũ thuộc một tài khoản; mở session mới bằng --new (session-start) để sang tài khoản khác")
        return 3
    except RuntimeError as e:
        log(f"LỖI: {e}")
        return 2
    finally:
        server.shutdown()

    text = pick_text(res["text"], res.get("md", ""))
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text((f"<!-- {args.note} -->\n\n" if args.note else "") + text + "\n", encoding="utf-8", newline="\n")
    if args.think_out:
        th = ((res or {}).get("think") or "").strip()
        tp = Path(args.think_out)
        tp.parent.mkdir(parents=True, exist_ok=True)
        tp.write_text(th + "\n", encoding="utf-8", newline="\n")
        log(f"thinking: {len(th)} ký tự → {args.think_out}")
    state.update(chat=res["url"])
    save_state(state)
    han = sum(1 for c in text if "一" <= c <= "鿿")
    print(f"{args.out} | {len(text)} ký tự | {han} chữ Hán | {'markdown' if text is res.get('md') else 'chữ trang'} "
          f"| {time.time() - start:.0f}s | {res.get('account', '?')} | {res['url']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
