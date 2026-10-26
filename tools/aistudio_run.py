"""Gửi một tin nhắn tới Gemini trong Google AI Studio qua extension Edge, lưu câu trả lời ra file.

Script mở server nhỏ ở 127.0.0.1:8765 và giao việc; extension tools/aistudio-ext (nạp vào Edge chính
bằng edge://extensions → Developer mode → Load unpacked) nhận việc, bấm nút trong một tab AI Studio riêng
rồi gửi câu trả lời về. Edge chỉ cần đang mở.
Extension tự reload khi file trong tools/aistudio-ext đổi — nhưng reload nạp lại từ thư mục Edge đã Load unpacked.
Nạp từ bản chép nơi khác (27/10: D:\\ClaudeCode\\aistudio-ext) thì sửa ở đây không có tác dụng: chép sang đó, hoặc
nạp lại đúng thư mục này. Dấu hiệu: không thấy dòng "extension nhận việc, đang chạy N việc".

Dùng:
    # mở session mới (SI + session-start), tự đổi tài khoản /u/0 → /u/1 → /u/2 khi hết quota
    python tools/aistudio_run.py --new --si <file SI> --prompt <file> --out <file ra> [--note "..."]
    # gửi tiếp vào chat của lần chạy trước (đoạn kế, ghi chú sửa)
    python tools/aistudio_run.py --prompt <file> --out <file ra> [--chat <url>]
    # nhiều chat mới cùng lúc: mỗi tài khoản một tab, cùng rút việc từ danh sách (test SI/prompt)
    python tools/aistudio_run.py --batch <jobs.json> [--accounts 0,1,2]

Mã thoát: 0 xong · 2 lỗi (trang, selector, extension không nhận việc) · 3 hết quota (mọi tài khoản đã thử,
hoặc đang gửi tiếp vào chat cũ)
"""
import argparse
import hashlib
import json
import queue
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
    """Các việc đang chờ extension nhận / đang chạy, và kết quả của chúng (--batch chạy nhiều việc cùng lúc)."""

    def __init__(self):
        self.cv = threading.Condition()
        self.jobs = {}  # id → {"job", "picked", "result"}

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
                log("extension tự nạp lại bản mới, giao lại việc")
                bridge.release(data)
            else:
                return self._send(404)
            self._send(200, {})

    return Handler


class Quota(Exception):
    pass


def run(bridge, job, timeout_min):
    jid = uuid.uuid4().hex
    bridge.submit(dict(job, id=jid, timeoutMin=timeout_min))
    try:
        if not bridge.wait(jid, "picked", PICKUP_S):
            raise RuntimeError(f"extension không nhận việc sau {PICKUP_S}s — Edge có đang mở, "
                               "extension 'Novel AI Studio bridge' đã nạp và đang bật?")
        if not bridge.wait(jid, "result", timeout_min * 60 + 180):
            raise RuntimeError(f"quá {timeout_min} phút chưa có kết quả")
        res = bridge.jobs[jid]["result"]
    finally:
        bridge.drop(jid)
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


def write_out(res, out, note, think_out=None):
    text = pick_text(res["text"], res.get("md", ""))
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text((f"<!-- {note} -->\n\n" if note else "") + text + "\n", encoding="utf-8", newline="\n")
    if think_out:
        th = (res.get("think") or "").strip()
        tp = Path(think_out)
        tp.parent.mkdir(parents=True, exist_ok=True)
        tp.write_text(th + "\n", encoding="utf-8", newline="\n")
        log(f"thinking: {len(th)} ký tự → {think_out}")
    return text


def run_batch(bridge, args):
    """Mỗi tài khoản một luồng, cùng rút việc từ một hàng đợi; tài khoản hết quota thì nghỉ, việc trả về hàng."""
    jobs = json.loads(Path(args.batch).read_text(encoding="utf-8"))
    pending = queue.Queue()
    for j in jobs:
        pending.put(dict(j, tries=0))
    lock = threading.Lock()
    done, failed = [], []

    def worker(acct, delay):
        time.sleep(delay)  # mở tab lệch nhau vài giây
        while True:
            try:
                j = pending.get_nowait()
            except queue.Empty:
                return
            start = time.time()
            job = dict(prompt=Path(j["prompt"]).read_text(encoding="utf-8"), model=j.get("model", args.model),
                       thinking=args.thinking, mode="new", si=Path(j["si"]).read_text(encoding="utf-8"),
                       url=BASE.format(acct))
            try:
                res = run(bridge, job, args.timeout)
            except Quota as q:
                log(f"/u/{acct} hết quota, nghỉ: {str(q)[:150]}")
                pending.put(j)
                return
            except RuntimeError as e:
                j["tries"] += 1
                log(f"/u/{acct} lỗi {j['out']} (lần {j['tries']}): {str(e)[:200]}")
                if j["tries"] < 2:
                    pending.put(j)
                else:
                    with lock:
                        failed.append(j["out"])
                continue
            text = write_out(res, j["out"], j.get("note", ""), j.get("think_out"))
            han = sum(1 for c in text if "一" <= c <= "鿿")
            with lock:
                done.append(j["out"])
                print(f"{j['out']} | {han} chữ Hán | {time.time() - start:.0f}s | /u/{acct} | {res['url']}", flush=True)

    accounts = [a.strip() for a in args.accounts.split(",")]
    threads = [threading.Thread(target=worker, args=(a, 8 * i)) for i, a in enumerate(accounts)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    left = []
    while not pending.empty():
        left.append(pending.get()["out"])
    log(f"xong {len(done)}/{len(jobs)} | lỗi: {failed or 'không'} | chưa chạy (hết quota): {left or 'không'}")
    return 0 if len(done) == len(jobs) else (3 if left else 2)


def main():
    for s in (sys.stdout, sys.stderr):
        s.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt")
    ap.add_argument("--out")
    ap.add_argument("--batch", help="file JSON [{si, prompt, out, note?, think_out?, model?}]: mỗi việc một chat mới, "
                                    "các tài khoản trong --accounts chạy song song")
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
    if not args.batch and not (args.prompt and args.out):
        ap.error("cần --prompt và --out (hoặc --batch)")

    bridge = Bridge()
    try:
        server = ThreadingHTTPServer(("127.0.0.1", args.port), make_handler(bridge))
    except OSError as e:
        log(f"cổng {args.port} đang bận — có lần chạy khác chưa xong? ({e})")
        return 2
    threading.Thread(target=server.serve_forever, daemon=True).start()
    if args.batch:
        try:
            return run_batch(bridge, args)
        finally:
            server.shutdown()

    prompt = Path(args.prompt).read_text(encoding="utf-8")
    state = json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {}

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
                    log(f"/u/{acct} không dùng được (hết quota / bị từ chối quyền): {str(q)[:200]}")
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

    text = write_out(res, args.out, args.note, args.think_out)
    state.update(chat=res["url"])
    save_state(state)
    han = sum(1 for c in text if "一" <= c <= "鿿")
    print(f"{args.out} | {len(text)} ký tự | {han} chữ Hán | {'markdown' if text is res.get('md') else 'chữ trang'} "
          f"| {time.time() - start:.0f}s | {res.get('account', '?')} | {res['url']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
