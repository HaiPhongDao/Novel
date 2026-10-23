#!/usr/bin/env python3
"""Chạy Writer bằng Gemini API: gửi SI + prompt đoạn, lưu bản thảo vào chapters/ — dùng cho mọi truyện.

Dùng:  python tools/gemini_write.py <thu-muc-truyen> <so-doan> [--moi] [--push]
       python tools/gemini_write.py --models          (liệt kê mã model key của bạn dùng được)

Cần:   key Gemini (AI Studio → Get API key), theo một trong hai cách:
       - biến môi trường GEMINI_API_KEY (máy riêng);
       - Network secret của môi trường Claude Code cloud: header x-goog-api-key cho generativelanguage.googleapis.com
         (proxy tự gắn key, script không thấy key — để trống GEMINI_API_KEY).
       Mã model: --model, hoặc biến GEMINI_MODEL, mặc định MODEL_MAC_DINH bên dưới.

Session (giống chat AI Studio, tối đa 2 đoạn — chung/quy-trinh-ban-giao.md):
- Lưu ở <truyen>/handoff/gemini-session.json (không commit).
- Đoạn đầu session: tin nhắn là handoff/session-start.md (tự ghép bằng build_pack.py); truyện chưa có đoạn nào
  thì gửi thẳng briefs/doan-XXX.md.
- Đoạn thứ 2: gửi thẳng briefs/doan-XXX.md, kèm lịch sử chat của đoạn trước.
- Session đã đủ 2 đoạn, hoặc có --moi (viết lại đoạn hỏng), thì mở session mới.
Ra:    <truyen>/chapters/doan-XXX.md (dòng đầu là ghi chú <!-- model, session, giờ -->).
       Đã có file đó thì dừng: chuyển bản cũ vào archive/ trước khi viết lại.
--push: git add + commit + push riêng file bản thảo.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
API = os.environ.get("GEMINI_API_BASE", "https://generativelanguage.googleapis.com/v1beta")
MODEL_MAC_DINH = "gemini-3-flash-preview"
SO_DOAN_MOI_SESSION = 2


def goi_api(method, path, key, body=None, timeout=900):
    req = urllib.request.Request(
        f"{API}/{path}", method=method,
        data=json.dumps(body).encode("utf-8") if body is not None else None,
        headers={"Content-Type": "application/json", **({"x-goog-api-key": key} if key else {})})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        loi = e.read().decode("utf-8", "replace")
        if e.code == 429:
            raise SystemExit(f"429 — hết hạn mức của key (theo phút hoặc theo ngày). Đợi rồi chạy lại.\n{loi}")
        if e.code in (401, 403) and not key:
            raise SystemExit(f"{e.code} — không có key: chưa đặt GEMINI_API_KEY, và Network secret (header x-goog-api-key "
                             f"cho generativelanguage.googleapis.com) chưa có hoặc chưa nạp — mở session mới sau khi lưu.\n{loi}")
        if e.code == 404:
            raise SystemExit(f"404 — sai mã model? Chạy --models để xem mã đúng.\n{loi}")
        raise SystemExit(f"Lỗi API {e.code}:\n{loi}")


def liet_ke_model(key):
    data = goi_api("GET", "models?pageSize=200", key)
    for m in data.get("models", []):
        if "generateContent" in m.get("supportedGenerationMethods", []):
            print(f"{m['name'].removeprefix('models/'):45} {m.get('displayName', '')}")


def tim_si(story: Path) -> Path:
    """SI đang dùng: dòng 'SI đang dùng: `gemini/...`' trong README của truyện, không thì gemini/system-instruction*.md."""
    readme = story / "README.md"
    if readme.exists():
        m = re.search(r"SI đang dùng:\s*`(gemini/[^`]+)`", readme.read_text(encoding="utf-8"))
        if m and (story / m.group(1)).exists():
            return story / m.group(1)
    cands = sorted(story.glob("gemini/system-instruction*.md"))
    if not cands:
        raise SystemExit(f"Không tìm thấy SI trong {story}/gemini/")
    return cands[-1]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("story", nargs="?")
    ap.add_argument("doan", nargs="?", help="số đoạn, vd 3 hoặc 003")
    ap.add_argument("--model", default=os.environ.get("GEMINI_MODEL", MODEL_MAC_DINH))
    ap.add_argument("--thinking", default="high", help="high / low / none (none = không gửi thinkingLevel)")
    ap.add_argument("--temp", type=float, help="nhiệt độ; bỏ trống = mặc định của model")
    ap.add_argument("--si", help="đường dẫn SI trong thư mục truyện (mặc định: SI ghi ở README)")
    ap.add_argument("--moi", action="store_true", help="bắt buộc mở session mới")
    ap.add_argument("--push", action="store_true", help="commit + push bản thảo")
    ap.add_argument("--thu", action="store_true", help="chỉ in ra sẽ gửi gì, không gọi API")
    ap.add_argument("--models", action="store_true", help="liệt kê model")
    a = ap.parse_args()

    key = os.environ.get("GEMINI_API_KEY", "")
    if a.models:
        return liet_ke_model(key)
    if not (a.story and a.doan):
        ap.error("cần <thu-muc-truyen> và <so-doan>")

    story = (REPO / a.story).resolve()
    n = f"{int(a.doan):03d}"
    brief = story / "briefs" / f"doan-{n}.md"
    out = story / "chapters" / f"doan-{n}.md"
    if not brief.exists():
        raise SystemExit(f"Chưa có prompt {brief.relative_to(REPO)}")
    if out.exists():
        raise SystemExit(f"Đã có {out.relative_to(REPO)} — chuyển bản cũ vào archive/ trước khi viết lại (thường kèm --moi).")
    si_path = story / a.si if a.si else tim_si(story)

    ses_path = story / "handoff" / "gemini-session.json"
    ses = json.loads(ses_path.read_text(encoding="utf-8")) if ses_path.exists() else None
    moi = a.moi or not ses or len(ses["doan"]) >= SO_DOAN_MOI_SESSION or ses.get("si") != si_path.name

    if moi:
        truoc = sorted(story.glob("chapters/doan-*.md"))
        if truoc:
            so_cuoi = int(re.search(r"doan-(\d+)", truoc[-1].name).group(1))
            if so_cuoi != int(n) - 1:
                raise SystemExit(f"Đoạn cuối trong chapters/ là {so_cuoi:03d}, không phải {int(n) - 1:03d} — gói bàn giao sẽ nối sai chỗ.")
            subprocess.run([sys.executable, str(REPO / "tools" / "build_pack.py"), str(story),
                            "--prompt", f"briefs/doan-{n}.md"], check=True)
            tin = (story / "handoff" / "session-start.md").read_text(encoding="utf-8")
            cach = "session-start.md"
        else:
            tin = brief.read_text(encoding="utf-8")
            cach = brief.name
        ses = {"id": datetime.now().strftime("%Y%m%d-%H%M"), "si": si_path.name, "model": a.model,
               "doan": [], "contents": []}
    else:
        tin = brief.read_text(encoding="utf-8")
        cach = f"{brief.name} (tiếp session {ses['id']})"

    contents = ses["contents"] + [{"role": "user", "parts": [{"text": tin}]}]
    gen = {}
    if a.thinking != "none":
        gen["thinkingConfig"] = {"thinkingLevel": a.thinking}
    if a.temp is not None:
        gen["temperature"] = a.temp
    body = {"systemInstruction": {"parts": [{"text": si_path.read_text(encoding="utf-8")}]},
            "contents": contents, "generationConfig": gen}

    print(f"Model {a.model} · SI {si_path.name} · gửi {cach} ({len(tin)} ký tự) · "
          f"session {ses['id']} đoạn thứ {len(ses['doan']) + 1}")
    if a.thu:
        return

    t0 = time.time()
    data = goi_api("POST", f"models/{a.model}:generateContent", key, body)
    cand = (data.get("candidates") or [{}])[0]
    text = "".join(p.get("text", "") for p in cand.get("content", {}).get("parts", []) if not p.get("thought")).strip()
    if not text:
        raise SystemExit(f"Không có chữ trả về (finishReason={cand.get('finishReason')}, "
                         f"promptFeedback={data.get('promptFeedback')}). Chạy lại, nên kèm --moi.")

    out.parent.mkdir(parents=True, exist_ok=True)
    note = f"<!-- {a.model} · thinking {a.thinking} · session {ses['id']} · {datetime.now():%Y-%m-%d %H:%M} -->"
    out.write_text(f"{note}\n\n{text}\n", encoding="utf-8")
    ses["contents"] = contents + [{"role": "model", "parts": [{"text": text}]}]
    ses["doan"].append(n)
    ses_path.write_text(json.dumps(ses, ensure_ascii=False, indent=1), encoding="utf-8")

    han = len(re.findall(r"[一-鿿]", text))
    use = data.get("usageMetadata", {})
    print(f"{out.relative_to(REPO)} | {han} chữ Hán | {time.time() - t0:.0f}s | "
          f"token vào {use.get('promptTokenCount')} · ra {use.get('candidatesTokenCount')} · nghĩ {use.get('thoughtsTokenCount')} | "
          f"finishReason {cand.get('finishReason')}")
    if cand.get("finishReason") not in (None, "STOP"):
        print("Cảnh báo: model dừng không bình thường — bản thảo có thể bị cụt.")

    if a.push:
        rel = str(out.relative_to(REPO))
        for cmd in (["git", "add", rel],
                    ["git", "commit", "-q", "-m", f"draft: {a.story} doan-{n} (Gemini API, session {ses['id']})"],
                    ["git", "push", "-q", "origin", "HEAD"]):
            subprocess.run(cmd, cwd=REPO, check=True)
        print("Đã push.")


if __name__ == "__main__":
    main()
