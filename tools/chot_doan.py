"""Chốt một đoạn đã ĐẠT: ghi review, cập nhật handoff/README/sessions/log, ghép gói, commit + push.

Dùng:  python tools/chot_doan.py <ten-truyen> <spec.py>

<spec.py> là file Python khai báo các biến (viết trong scratchpad, không commit):
    N           = "012"                         số đoạn
    REVIEW      = "# Review — ..."              ghi đè reviews/doan-N.md
    STORY       = "### Đoạn 12 — ...\\n..."      nối vào cuối handoff/story-so-far.md
    COMPRESS    = [("Đoạn 9 — tối Ngày 8", "tóm tắt 1–2 dòng")]   (tuỳ chọn) nén đoạn cũ: thay thân mục "### <tiêu đề>"
    STATE       = "## 3. Trạng thái hiện tại ..."   ghi đè handoff/state.md
    CANON_ADD   = "- ..."  hoặc None            (tuỳ chọn) nối vào handoff/canon-card.md
    VOICE_ADD   = "**...**\\n\\n“...”" hoặc None (tuỳ chọn) nối vào handoff/voice-anchor.md
    README_ROW  = "| 012 | ✅ | ✅ | ✅ ĐẠT | ✅ |"  thêm sau dòng đoạn cuối trong bảng README.md của truyện
    SESSIONS_REPLACE = (cũ, mới)                (tuỳ chọn) sửa một dòng trong handoff/sessions.md
    LOG         = "2026-10-23 | doan-012 | ..."  nối vào log.md
    COMMIT      = "doan-012: chốt — ..."         thông điệp commit (dòng Co-Authored-By tự thêm)

Chạy lại một spec đã chạy sẽ nối trùng story/log — nếu bước git hỏng thì chỉ chạy lại phần git bằng tay.
Quy trình: AGENT.md mục 3 bước 6; chung/quy-trinh-ban-giao.md.
"""
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
CO_AUTHOR = "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"


def run(*a):
    r = subprocess.run(a, cwd=REPO, capture_output=True, text=True, encoding="utf-8",
                       env={**os.environ, "PYTHONIOENCODING": "utf-8"})
    if r.returncode:
        raise SystemExit(f"{a} hỏng:\n{r.stdout}\n{r.stderr}")
    return r.stdout.strip()


def main():
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    story_name, spec_path = sys.argv[1], Path(sys.argv[2])
    D = REPO / story_name
    if not D.is_dir():
        raise SystemExit(f"Không có thư mục truyện {D}")

    def rd(p):
        return (D / p).read_text(encoding="utf-8")

    def wr(p, s):
        (D / p).write_text(s, encoding="utf-8", newline="")

    spec = {}
    exec(spec_path.read_text(encoding="utf-8"), spec)
    n = spec["N"]

    wr(f"reviews/doan-{n}.md", spec["REVIEW"].strip() + "\n")

    s = rd("handoff/story-so-far.md").rstrip("\n")
    for title, short in spec.get("COMPRESS") or []:
        s2 = re.sub(rf"### {re.escape(title)}\n.*?(?=\n\n### |\Z)", f"### {title}\n{short}", s, flags=re.S)
        if s2 == s:
            raise SystemExit(f"Không tìm thấy mục '### {title}' trong story-so-far.md")
        s = s2
    wr("handoff/story-so-far.md", s + "\n\n" + spec["STORY"].strip() + "\n")

    wr("handoff/state.md", spec["STATE"].strip() + "\n")

    for f, key in (("handoff/canon-card.md", "CANON_ADD"), ("handoff/voice-anchor.md", "VOICE_ADD")):
        if spec.get(key):
            wr(f, rd(f).rstrip("\n") + "\n\n" + spec[key].strip() + "\n")

    s = rd("README.md")
    rows = re.findall(r"^\| \d{3} \|.*$", s, flags=re.M)
    sep = re.search(r"^\| Đoạn \|.*\n(\|[-| ]+\|)$", s, flags=re.M)
    if rows:
        s = s.replace(rows[-1], rows[-1] + "\n" + spec["README_ROW"].strip())
    elif sep:
        s = s[:sep.end()] + "\n" + spec["README_ROW"].strip() + s[sep.end():]
    else:
        print("README.md chưa có bảng '| Đoạn |' — bỏ qua README_ROW")
    wr("README.md", s)

    if spec.get("SESSIONS_REPLACE"):
        old, new = spec["SESSIONS_REPLACE"]
        s = rd("handoff/sessions.md")
        if old not in s:
            raise SystemExit(f"sessions.md không có dòng: {old}")
        wr("handoff/sessions.md", s.replace(old, new))

    wr("log.md", rd("log.md").rstrip("\n") + "\n" + spec["LOG"].strip() + "\n")

    print(run(sys.executable, "tools/build_pack.py", story_name))
    gopped = run(sys.executable, "tools/gop_doan.py", story_name)
    if gopped.startswith("Đã gộp"):
        print(gopped)
    run("git", "add", story_name)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".txt", delete=False) as f:
        f.write(spec["COMMIT"].strip() + "\n\n" + CO_AUTHOR + "\n")
        msg = f.name
    try:
        run("git", "commit", "-q", "-F", msg)
    finally:
        os.unlink(msg)
    run("git", "push", "-q", "origin", "HEAD")
    print(run("git", "log", "--oneline", "-1"))
    print(run("git", "status", "-sb").splitlines()[0])


if __name__ == "__main__":
    main()
