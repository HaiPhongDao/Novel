#!/usr/bin/env python3
"""Một lệnh cho mỗi bước của làn sản xuất (QUY-TRINH.md).

    python tools/lam.py viet <truyen> <N> [--lai] [--truoc 2] [--gia-lap FILE]
        Ghép prompt (văn nguyên của các đoạn trước + thẻ thiết lập + brief), chạy Writer trên AI Studio,
        thay chữ theo <truyen>/gemini/thay-chu.txt, qua cổng máy, in một bảng tóm tắt.
        --lai       đã có bản: cất bản cũ + brief của nó vào archive/ rồi chạy lại
        --truoc K   dán nguyên văn K đoạn liền trước vào prompt (mặc định 2; 0 = chỉ gửi brief)
        --gia-lap   không gọi Writer, lấy FILE làm bản Writer trả (Tác giả dán tay, hoặc để thử lệnh)
    python tools/lam.py doc <truyen> <N1> [N2]
        Ghép các đoạn N1…N2 thành một file <truyen>/doc/lo-N1-N2.md để Tác giả nghe một lần.
    python tools/lam.py chot <truyen> <N1> [N2] -m "tóm tắt một câu" [--khong-push]
        Ghi README + log.md của truyện, gộp khối 10 đoạn, commit, pull --rebase, push.
    python tools/lam.py bang [--ghi]
        Bảng tiến độ mọi truyện (số đoạn đã có, đoạn đã chốt, ngày đụng tới gần nhất). --ghi: chép vào README.md gốc.

Mã thoát của viet: 0 xanh · 1 cổng máy đỏ (bản vẫn nằm ở chapters/ để xem) · 2 lỗi chạy · 3 hết quota mọi tài khoản.
"""
import argparse
import contextlib
import datetime
import io
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    _s.reconfigure(encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "tools"))
import cong_doan  # noqa: E402
import gop_doan  # noqa: E402

HAN = re.compile(r"[一-鿿]")
CO_AUTHOR = "Co-Authored-By: Claude <noreply@anthropic.com>"
BANG_DAU, BANG_CUOI = "<!-- bang:dau -->", "<!-- bang:cuoi -->"


def han(s):
    return len(HAN.findall(s))


def chet(msg, code=2):
    print(msg, file=sys.stderr)
    sys.exit(code)


def thu_muc(ten):
    d = REPO / ten
    if not (d / "briefs").is_dir():
        chet(f"Không có truyện '{ten}' (thiếu {ten}/briefs/). Truyện đang có: {', '.join(t.name for t in ds_truyen())}")
    return d


def ds_truyen():
    return sorted(p.parent for p in REPO.glob("*/chapters") if p.is_dir() and not p.parent.name.startswith(("_", ".")))


def doan(d, n):
    return d / "chapters" / f"doan-{n:03d}.md"


def co_chu(p):
    return p.exists() and p.read_text(encoding="utf-8").strip() != ""


def git(*a, check=True):
    r = subprocess.run(("git",) + a, cwd=REPO, capture_output=True, text=True, encoding="utf-8")
    if check and r.returncode:
        chet(f"git {' '.join(a)} hỏng:\n{r.stdout}{r.stderr}")
    return r.stdout.strip()


# ---------------------------------------------------------------- viet

def ten_chua_dung(d, mau):
    """archive/doan-004-v{k}.md với k nhỏ nhất chưa dùng."""
    k = 1
    while any((d / "archive" / mau.format(k=k)).with_suffix(duoi).exists() for duoi in (".md", ".brief.md")):
        k += 1
    return d / "archive" / mau.format(k=k), k


def cat_ban_cu(d, n, kieu="v"):
    src = doan(d, n)
    (d / "archive").mkdir(exist_ok=True)
    dst, k = ten_chua_dung(d, f"doan-{n:03d}-{kieu}{{k}}.md")
    shutil.move(str(src), str(dst))
    brief = d / "briefs" / f"doan-{n:03d}.md"
    if kieu == "v" and brief.exists():
        # brief đã sinh ra bản cũ là bản đã commit; file trên đĩa thường vừa được sửa để chạy lại
        r = subprocess.run(("git", "show", f"HEAD:{brief.relative_to(REPO).as_posix()}"), cwd=REPO, capture_output=True)
        cu = r.stdout if r.returncode == 0 else brief.read_bytes()
        (d / "archive" / f"doan-{n:03d}-v{k}.brief.md").write_bytes(cu)
    return dst


def ghep_prompt(d, n, truoc):
    brief = (d / "briefs" / f"doan-{n:03d}.md").read_text(encoding="utf-8").strip()
    cu = [m for m in range(max(1, n - truoc), n) if co_chu(doan(d, m))]
    if not cu:
        return brief + "\n", ""  # đoạn mở đầu: chỉ brief (dán thẻ/State vào đoạn 001 làm Writer xả dữ kiện)
    van = "\n\n".join(gop_doan.prose(doan(d, m)) for m in cu)
    khoang = f"{cu[0]:03d}" if len(cu) == 1 else f"{cu[0]:03d}–{cu[-1]:03d}"
    parts = [
        "Dưới đây là phần truyện đã viết xong, nguyên văn. Đọc để nắm mạch, giọng kể và mọi chi tiết đã có.",
        f"=== TRUYỆN ĐÃ VIẾT (đoạn {khoang}) ===\n\n{van}\n\n=== HẾT PHẦN ĐÃ VIẾT ===",
    ]
    the = d / "handoff" / "canon-card.md"
    if co_chu(the):
        parts.append("=== THẺ THIẾT LẬP (để giữ đúng tên và số; phần lớn người đọc đã biết) ===\n\n"
                     + the.read_text(encoding="utf-8").strip())
    parts.append("=== VIỆC CỦA ĐOẠN NÀY ===\n\n" + brief)
    parts.append("Viết tiếp ngay sau câu cuối của phần đã viết. Người đọc vừa đọc xong phần trên và còn nhớ hết; "
                 "đoạn mới chỉ gồm việc mới. Trả về chính văn tiếng Trung của đoạn mới.")
    return "\n\n".join(parts) + "\n", van


def doc_thay_chu(d):
    f = d / "gemini" / "thay-chu.txt"
    cap = []
    if f.exists():
        for line in f.read_text(encoding="utf-8").splitlines():
            line = line.split("#", 1)[0].strip()
            if "=>" in line:
                sai, dung = (x.strip() for x in line.split("=>", 1))
                if sai and sai != dung:
                    cap.append((sai, dung))
    return cap


def hau_ky(d, out):
    """Bỏ dòng chú thích đầu file, thay chữ theo bảng của truyện. Trả về [(sai, đúng, số lần)]."""
    t = out.read_text(encoding="utf-8").replace("\r\n", "\n")
    t = re.sub(r"\A\s*(<!--.*?-->\s*)+", "", t, flags=re.S).strip() + "\n"
    da_thay = []
    for sai, dung in doc_thay_chu(d):
        c = t.count(sai)
        if c:
            t = t.replace(sai, dung)
            da_thay.append((sai, dung, c))
    out.write_text(t, encoding="utf-8", newline="\n")
    return da_thay


def cau_lap(van_truoc, ban, min_han=12):
    """Câu của các đoạn trước xuất hiện nguyên văn trong bản mới = Writer kể lại thay vì viết tiếp."""
    lap = {s for s in cong_doan.sentences(van_truoc, min_han) if s in ban}
    return sorted(lap, key=len, reverse=True)


def chay_writer(a, d, prompt_file, out):
    if a.gia_lap:
        shutil.copyfile(a.gia_lap, out)
        return 0
    si = Path(a.si) if a.si else d / "gemini" / "si-dan-gemini.txt"
    if not si.exists():
        chet(f"Thiếu SI: {si} (dựng bằng python tools/dung_si.py {d.name}, hoặc chỉ bằng --si)")
    cmd = [sys.executable, "-X", "utf8", str(REPO / "tools" / "aistudio_run.py"), "--new", "--si", str(si),
           "--prompt", str(prompt_file), "--out", str(out), "--timeout", str(a.timeout), "--accounts", a.accounts]
    return subprocess.run(cmd, cwd=REPO).returncode


def cmd_viet(a):
    d, n = thu_muc(a.truyen), int(a.doan)
    brief = d / "briefs" / f"doan-{n:03d}.md"
    out = doan(d, n)
    if not co_chu(brief):
        chet(f"Thiếu brief: {brief.relative_to(REPO).as_posix()} — viết brief trước (QUY-TRINH.md mục 2)")
    if a.gia_lap and not Path(a.gia_lap).exists():
        chet(f"Không thấy file --gia-lap: {a.gia_lap}")
    if n > 1 and a.truoc and not co_chu(doan(d, n - 1)):
        chet(f"Chưa có đoạn {n - 1:03d} trong chapters/ — viết theo thứ tự, hoặc --truoc 0 nếu cố ý")
    if co_chu(out):
        if not a.lai:
            chet(f"Đã có {out.relative_to(REPO).as_posix()} — thêm --lai để cất bản cũ vào archive/ rồi chạy lại")
        print(f"cất bản cũ → {cat_ban_cu(d, n).relative_to(REPO).as_posix()}")

    prompt, van_truoc = ghep_prompt(d, n, a.truoc)
    (d / "handoff").mkdir(exist_ok=True)
    prompt_file = d / "handoff" / "prompt-gui.md"
    prompt_file.write_text(prompt, encoding="utf-8", newline="\n")
    out.parent.mkdir(exist_ok=True)

    for lan in (1, 2):
        rc = chay_writer(a, d, prompt_file, out)
        if rc == 3:
            chet("HẾT QUOTA mọi tài khoản — dừng lô, báo Tác giả.", 3)
        if rc or not co_chu(out):
            chet("Writer không trả bài (xem dòng lỗi phía trên). Lỗi tạm thì chạy lại y nguyên lệnh sau 30 giây.", 2)
        da_thay = hau_ky(d, out)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            xanh = cong_doan.gate(str(out), str(brief), str(doan(d, n - 1)) if co_chu(doan(d, n - 1)) else None)
        cong = buf.getvalue().strip()
        if not xanh and "bản cụt" in cong and lan == 1 and not a.gia_lap:
            print(f"bản cụt (lỗi mạng AI Studio) → {cat_ban_cu(d, n, 'cut').relative_to(REPO).as_posix()}; chạy lại một lần")
            continue
        break

    ban = out.read_text(encoding="utf-8")
    lap = cau_lap(van_truoc, ban) if van_truoc else []
    si = Path(a.si) if a.si else d / "gemini" / "si-dan-gemini.txt"
    chep_si = cau_lap(si.read_text(encoding="utf-8"), ban, 10) if si.exists() else []
    print("\n" + "─" * 60)
    print(f"{out.relative_to(REPO).as_posix()} | {han(ban)} 字 | prompt {len(prompt)} ký tự ({han(van_truoc)} 字 văn trước)")
    print(cong)
    if da_thay:
        print("thay chữ: " + ", ".join(f"{s}→{g} ×{c}" for s, g, c in da_thay))
    if lap:
        print(f"⚠ kể lại: {len(lap)} câu của đoạn trước xuất hiện nguyên văn — " + " | ".join(s[:20] for s in lap[:3]))
    if chep_si:
        print(f"⚠ chép SI: {len(chep_si)} câu của SI/anchor xuất hiện nguyên văn — " + " | ".join(s[:20] for s in chep_si[:3]))
    print("Việc kế: đọc lướt (tên, số, ai biết gì, chỗ dừng) rồi viết brief đoạn sau. Xanh chưa phải đạt.")
    sys.exit(0 if xanh else 1)


# ---------------------------------------------------------------- doc

def khoang(a):
    n1 = int(a.n1)
    n2 = int(a.n2) if a.n2 else n1
    if n2 < n1:
        chet("N2 phải ≥ N1")
    return n1, n2


def cmd_doc(a):
    d = thu_muc(a.truyen)
    n1, n2 = khoang(a)
    thieu = [f"{n:03d}" for n in range(n1, n2 + 1) if not co_chu(doan(d, n))]
    if thieu:
        chet(f"Chưa có đoạn: {', '.join(thieu)}")
    parts, tong = [], 0
    for n in range(n1, n2 + 1):
        t = gop_doan.prose(doan(d, n))
        tong += han(t)
        parts.append(f"【{n:03d}】\n\n{t}")
    (d / "doc").mkdir(exist_ok=True)
    f = d / "doc" / (f"lo-{n1:03d}.md" if n1 == n2 else f"lo-{n1:03d}-{n2:03d}.md")
    f.write_text("\n\n".join(parts) + "\n", encoding="utf-8", newline="\n")
    print(f"{f.relative_to(REPO).as_posix()} | {n2 - n1 + 1} đoạn | {tong} 字 — gửi Tác giả nghe (DocTTS); phiếu góp ý: python tools/gop_y.py <phiếu> {d.name}")


# ---------------------------------------------------------------- chot

def cmd_chot(a):
    d = thu_muc(a.truyen)
    n1, n2 = khoang(a)
    thieu = [f"{n:03d}" for n in range(n1, n2 + 1) if not co_chu(doan(d, n))]
    if thieu:
        chet(f"Chưa có đoạn: {', '.join(thieu)}")
    hom_nay = datetime.date.today()
    dau = f"✅ chốt {hom_nay:%d/%m}"

    readme = d / "README.md"
    if readme.exists():
        s = readme.read_text(encoding="utf-8")
        for n in range(n1, n2 + 1):
            m = re.search(rf"^\| {n:03d} \|.*$", s, flags=re.M)
            if m:
                o = [c.strip() for c in m.group(0).strip().strip("|").split("|")]
                o[-1] = dau
                s = s[:m.start()] + "| " + " | ".join(o) + " |" + s[m.end():]
            else:
                rows = list(re.finditer(r"^\| \d{3} \|.*$", s, flags=re.M))
                dong = f"| {n:03d} | [`briefs/doan-{n:03d}.md`](briefs/doan-{n:03d}.md) | [`chapters/doan-{n:03d}.md`](chapters/doan-{n:03d}.md) | — | {dau} |"
                if rows:
                    s = s[:rows[-1].end()] + "\n" + dong + s[rows[-1].end():]
                else:
                    s = s.rstrip("\n") + "\n\n## Trạng thái\n\n| Đoạn | Prompt | Bản thảo | Review | Chốt |\n|---|---|---|---|---|\n" + dong + "\n"
        readme.write_text(s, encoding="utf-8", newline="\n")

    ten = f"doan-{n1:03d}" if n1 == n2 else f"doan-{n1:03d}–{n2:03d}"
    log = d / "log.md"
    cu = log.read_text(encoding="utf-8").rstrip("\n") if log.exists() else "# Nhật ký quyết định"
    log.write_text(f"{cu}\n{hom_nay:%Y-%m-%d} | {ten} | Chốt — {a.m} | Duyệt: Tác giả\n", encoding="utf-8", newline="\n")

    gop_doan.gop(d.name)  # tự in "Đã gộp …" khi vừa đủ một khối 10 đoạn
    git("add", "--", d.name)
    git("commit", "-q", "-m", f"{d.name} {ten}: chốt — {a.m}\n\n{CO_AUTHOR}")
    if not a.khong_push:
        if git("status", "--porcelain", "--untracked-files=no"):
            print("còn thay đổi chưa commit ở chỗ khác → bỏ qua pull --rebase, chỉ push")
        else:
            git("pull", "-q", "--rebase")
        git("push", "-q", "origin", "HEAD")
    print(git("log", "--oneline", "-1"))
    print(git("status", "-sb").splitlines()[0])


# ---------------------------------------------------------------- bang

def tien_do():
    rows = []
    for d in ds_truyen():
        ns = sorted(int(m[1]) for p in (d / "chapters").glob("doan-*.md")
                    if (m := re.fullmatch(r"doan-(\d{3})\.md", p.name)) and co_chu(p))
        if not ns:
            continue
        chot = 0
        readme = d / "README.md"
        if readme.exists():
            for m in re.finditer(r"^\| (\d{3}) \|.*\|\s*([^|]*?)\s*\|\s*$", readme.read_text(encoding="utf-8"), flags=re.M):
                if "✅" in m.group(2):
                    chot = max(chot, int(m.group(1)))
        ngay = git("log", "-1", "--format=%cs", "--", f"{d.name}/chapters", f"{d.name}/briefs", check=False) or "—"
        tong = sum(han(gop_doan.prose(doan(d, n))) for n in ns)
        rows.append((ngay, d.name, ns[-1], chot, tong))
    return sorted(rows, reverse=True)


def cmd_bang(a):
    rows = tien_do()
    lines = ["| Truyện | Đã viết tới | Đã chốt tới | Tổng 字 | Đụng tới gần nhất |", "|---|---|---|---|---|"]
    for ngay, ten, cuoi, chot, tong in rows:
        lines.append(f"| [`{ten}/`]({ten}/README.md) | {cuoi:03d} | {f'{chot:03d}' if chot else '—'} | {tong:,}".replace(",", ".")
                     + f" | {ngay} |")
    bang = "\n".join(lines)
    print(bang)
    if a.ghi:
        f = REPO / "README.md"
        s = f.read_text(encoding="utf-8")
        if BANG_DAU not in s or BANG_CUOI not in s:
            chet(f"README.md gốc thiếu cặp dấu {BANG_DAU} … {BANG_CUOI}")
        s = s[:s.index(BANG_DAU) + len(BANG_DAU)] + "\n" + bang + "\n" + s[s.index(BANG_CUOI):]
        f.write_text(s, encoding="utf-8", newline="\n")
        print("\nđã ghi vào README.md")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="lenh", required=True)

    v = sub.add_parser("viet")
    v.add_argument("truyen")
    v.add_argument("doan")
    v.add_argument("--lai", action="store_true")
    v.add_argument("--truoc", type=int, default=2)
    v.add_argument("--gia-lap")
    v.add_argument("--si")
    v.add_argument("--accounts", default=os.environ.get("ACC", "0,1,2"))
    v.add_argument("--timeout", type=int, default=10)
    v.set_defaults(f=cmd_viet)

    for ten, f in (("doc", cmd_doc), ("chot", cmd_chot)):
        p = sub.add_parser(ten)
        p.add_argument("truyen")
        p.add_argument("n1")
        p.add_argument("n2", nargs="?")
        p.set_defaults(f=f)
        if ten == "chot":
            p.add_argument("-m", required=True, help="tóm tắt một câu")
            p.add_argument("--khong-push", action="store_true")

    b = sub.add_parser("bang")
    b.add_argument("--ghi", action="store_true")
    b.set_defaults(f=cmd_bang)

    a = ap.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
