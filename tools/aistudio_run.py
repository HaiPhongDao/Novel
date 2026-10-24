"""Gửi một tin nhắn tới Gemini trong Google AI Studio qua Edge đang mở sẵn (CDP), lưu câu trả lời ra file.

Edge phải chạy bằng profile riêng có cổng debug: toolsedge_debug.cmd
(lần đầu: toolsedge_debug.cmd -Login, đăng nhập 3 tài khoản Google rồi đóng Edge).

Dùng:
    # mở session mới (SI + session-start), tự đổi tài khoản /u/0 → /u/1 → /u/2 khi hết quota
    python tools/aistudio_run.py --new --si <file SI> --prompt <file> --out <file ra> [--note "..."]
    # gửi tiếp vào chat của lần chạy trước (đoạn kế, ghi chú sửa)
    python tools/aistudio_run.py --prompt <file> --out <file ra> [--chat <url>]

Mã thoát: 0 xong · 2 lỗi trang/selector · 3 hết quota (mọi tài khoản đã thử, hoặc đang gửi tiếp vào chat cũ)
"""
import argparse
import json
import re
import sys
import time
from pathlib import Path

from playwright.sync_api import TimeoutError as PWTimeout
from playwright.sync_api import sync_playwright

STATE = Path(__file__).with_name(".aistudio_state.json")
BASE = "https://aistudio.google.com/u/{}/prompts/new_chat"
QUOTA_RE = re.compile(r"quota|rate.?limit|resource.?exhausted|\b429\b|reached .{0,30}limit|try again later", re.I)

PROMPT_BOX = 'textarea[aria-label="Enter a prompt"]'
SI_CARD = "button.system-instructions-card"
SI_BOX = 'textarea[aria-label="System instructions"]'
RUN_BTN = "ms-run-button button"
MODEL_CARD = "button.model-selector-card"
THINKING = 'mat-select[aria-label="Thinking Level"]'
TURN = "ms-chat-turn"

# Bắt chuỗi mà nút "Copy as markdown" ghi ra, không đụng clipboard của máy.
HOOK_JS = """() => {
  if (window.__novelHook) return;
  window.__novelHook = true;
  navigator.clipboard.writeText = t => { window.__novelCopied = t; return Promise.resolve(); };
}"""

# Chữ của các lượt Model sau lượt User cuối, bỏ phần suy nghĩ.
LAST_REPLY_JS = """() => {
  const turns = [...document.querySelectorAll('ms-chat-turn')];
  const role = t => t.querySelector('[data-turn-role]')?.getAttribute('data-turn-role');
  let i = turns.length - 1;
  while (i >= 0 && role(turns[i]) !== 'User') i--;
  const models = turns.slice(i + 1).filter(t => role(t) === 'Model');
  const text = models.map(t => [...t.querySelectorAll('ms-text-chunk')]
      .filter(c => !c.closest('ms-thought-chunk, [class*="thought"]'))
      .map(c => c.innerText.trim()).join('\\n\\n')).join('\\n\\n').trim();
  return {n: turns.length, models: models.length, text,
          raw: models.map(t => t.innerText).join('\\n').slice(-600)};
}"""


class Quota(Exception):
    pass


def log(msg):
    print(msg, file=sys.stderr, flush=True)


def get_page(browser):
    ctx = browser.contexts[0]
    for p in ctx.pages:
        if "aistudio.google.com" in p.url:
            return p
    return ctx.new_page()


def goto(page, url):
    page.goto(url, wait_until="domcontentloaded")
    if "accounts.google.com" in page.url:
        raise RuntimeError(f"chưa đăng nhập: {url} → {page.url}")
    page.wait_for_selector(PROMPT_BOX, timeout=60_000)
    acct = page.locator("button.account-switcher-button").first.get_attribute("aria-label") or "?"
    log(f"mở {page.url} | {acct}")


def close_overlays(page):
    page.keyboard.press("Escape")
    btn = page.locator('[aria-label="Close panel"]')
    if btn.count() and btn.first.is_visible():
        btn.first.click()


def set_model(page, model):
    card = page.locator(MODEL_CARD)
    if model in card.inner_text():
        return
    card.click()
    page.locator("ms-model-carousel-row", has_text=model).locator("button.content-button").first.click()
    page.wait_for_timeout(800)
    close_overlays(page)
    if model not in page.locator(MODEL_CARD).inner_text():
        raise RuntimeError(f"không chọn được model {model}")


def set_thinking(page, level):
    sel = page.locator(THINKING)
    if not sel.count():
        log("không thấy ô Thinking Level — bỏ qua")
        return
    if sel.inner_text().strip() == level:
        return
    sel.click()
    page.locator("mat-option", has_text=re.compile(rf"^\s*{level}\s*$")).click()
    page.wait_for_timeout(300)
    if sel.inner_text().strip() != level:
        raise RuntimeError(f"không đặt được thinking {level}")


def set_si(page, text):
    page.locator(SI_CARD).click()
    box = page.locator(SI_BOX)
    box.wait_for(timeout=10_000)
    box.fill(text)
    if len(box.input_value()) != len(text):
        raise RuntimeError("SI dán không đủ")
    close_overlays(page)


def find_error(page):
    """Thông báo lỗi trên trang (snackbar, lỗi trong lượt Model), nếu có."""
    for sel in ("mat-snack-bar-container", ".mat-mdc-snack-bar-container", "ms-callout", ".error"):
        for el in page.locator(sel).all():
            if el.is_visible():
                t = el.inner_text().strip()
                if t:
                    return t
    return ""


def send(page, text, timeout_min):
    box = page.locator(PROMPT_BOX)
    box.fill(text)
    if len(box.input_value()) != len(text):
        raise RuntimeError("prompt dán không đủ")
    n_before = page.locator(TURN).count()
    page.locator(RUN_BTN).click()

    # Chờ bắt đầu (nút thành Stop hoặc có lượt mới), rồi chờ xong (nút về Run).
    deadline = time.time() + 60
    while time.time() < deadline:
        if "Stop" in page.locator(RUN_BTN).inner_text() or page.locator(TURN).count() > n_before:
            break
        if QUOTA_RE.search(find_error(page)):
            raise Quota(find_error(page))
        page.wait_for_timeout(500)
    else:
        raise RuntimeError(f"bấm Run nhưng không chạy: {find_error(page) or 'không rõ lý do'}")

    deadline = time.time() + timeout_min * 60
    while "Stop" in page.locator(RUN_BTN).inner_text():
        if time.time() > deadline:
            raise RuntimeError(f"quá {timeout_min} phút chưa xong")
        page.wait_for_timeout(2000)
    page.wait_for_timeout(1500)

    reply = page.evaluate(LAST_REPLY_JS)
    err = find_error(page)
    if not reply["text"]:
        msg = err or reply["raw"]
        if QUOTA_RE.search(msg):
            raise Quota(msg)
        raise RuntimeError(f"không có câu trả lời: {msg[-300:]}")
    if err:
        log(f"cảnh báo trên trang: {err[:200]}")
    return reply["text"], copy_markdown(page)


def copy_markdown(page):
    """Bản markdown qua nút 'Copy as markdown' của lượt cuối; '' nếu không lấy được."""
    try:
        page.evaluate(HOOK_JS)
        page.evaluate("() => { window.__novelCopied = null; }")
        last = page.locator(TURN).last
        last.hover()
        last.locator("ms-chat-turn-options button").first.click()
        page.get_by_role("menuitem", name=re.compile("Copy as markdown")).click()
        page.wait_for_function("() => window.__novelCopied !== null", timeout=5000)
        return page.evaluate("() => window.__novelCopied").strip()
    except Exception as e:  # noqa: BLE001 — chỉ là đường phụ
        log(f"copy markdown không được ({e.__class__.__name__}), dùng chữ trên trang")
        close_overlays(page)
        return ""


def pick_text(dom, md):
    # Markdown giữ được định dạng; chỉ dùng khi khớp với chữ trên trang (cùng số chữ Hán ±2%).
    han = lambda s: sum(1 for c in s if "一" <= c <= "鿿")
    if md and abs(han(md) - han(dom)) <= max(5, han(dom) * 0.02):
        return md
    return dom


def save(out, text, note):
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    hdr = f"<!-- {note} -->\n\n" if note else ""
    out.write_text(hdr + text + "\n", encoding="utf-8")


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
    ap.add_argument("--port", type=int, default=9222)
    ap.add_argument("--timeout", type=int, default=20, help="phút chờ tối đa cho một câu trả lời")
    args = ap.parse_args()
    if args.new and not args.si:
        ap.error("--new cần --si")

    prompt = Path(args.prompt).read_text(encoding="utf-8")
    state = json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {}

    with sync_playwright() as pw:
        try:
            browser = pw.chromium.connect_over_cdp(f"http://127.0.0.1:{args.port}")
        except Exception as e:  # noqa: BLE001
            log(f"không nối được Edge ở cổng {args.port} — chạy tools\edge_debug.cmd trước ({e})")
            return 2
        page = get_page(browser)
        page.set_default_timeout(30_000)
        start = time.time()
        try:
            if args.new:
                si = Path(args.si).read_text(encoding="utf-8")
                accounts = [a.strip() for a in args.accounts.split(",")]
                if state.get("quota_account") in accounts and state.get("quota_day") == time.strftime("%Y-%m-%d"):
                    i = accounts.index(state["quota_account"])
                    accounts = accounts[i + 1:] + accounts[:i + 1]  # tài khoản hết quota hôm nay để cuối
                for n, acct in enumerate(accounts):
                    try:
                        goto(page, BASE.format(acct))
                        set_model(page, args.model)
                        set_thinking(page, args.thinking)
                        set_si(page, si)
                        dom, md = send(page, prompt, args.timeout)
                        break
                    except Quota as q:
                        log(f"/u/{acct} hết quota: {str(q)[:200]}")
                        state.update(quota_account=acct, quota_day=time.strftime("%Y-%m-%d"))
                        STATE.write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding="utf-8")
                        if n == len(accounts) - 1:
                            raise
                state.update(account=acct)
            else:
                url = args.chat or state.get("chat")
                if not url:
                    log("chưa có chat nào — dùng --new hoặc --chat")
                    return 2
                goto(page, url)
                set_thinking(page, args.thinking)
                dom, md = send(page, prompt, args.timeout)
        except Quota as q:
            log(f"HẾT QUOTA: {str(q)[:300]}")
            if not args.new:
                log("chat cũ thuộc một tài khoản; mở session mới bằng --new (session-start) để sang tài khoản khác")
            return 3
        except (RuntimeError, PWTimeout) as e:
            log(f"LỖI: {e}")
            shot = Path(args.out).with_suffix(".error.png")
            try:
                page.screenshot(path=str(shot))
                log(f"ảnh màn hình: {shot}")
            except Exception:  # noqa: BLE001
                pass
            return 2

        text = pick_text(dom, md)
        save(args.out, text, args.note)
        state.update(chat=page.url)
        STATE.write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding="utf-8")
        han = sum(1 for c in text if "一" <= c <= "鿿")
        print(f"{args.out} | {len(text)} ký tự | {han} chữ Hán | {'markdown' if text is md else 'chữ trang'} "
              f"| {time.time() - start:.0f}s | {page.url}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
