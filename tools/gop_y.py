"""Dò phiếu "Góp ý khi nghe" (app DocTTS) ra đúng file:dòng trong bản thảo.

Tại sao có (05/11/2026): Tác giả nghe văn Writer bằng app DocTTS (repo nghien-cuu, tts-app),
bôi đen chỗ không ổn, gắn nhãn + ghi chú rồi gửi phiếu. Phiếu có câu chữ Hán gốc; công cụ này
grep câu đó trong các chương để Agent mở đúng vài dòng quanh chỗ khớp, KHÔNG phải đọc nguyên
chương (luật tiết kiệm token). Định dạng phiếu: chung/gop-y-khi-nghe.md.

Dùng:
    python tools/gop_y.py <phieu.md | ->                 # dò trong mọi */chapters/*.md
    python tools/gop_y.py <phieu.md> goblin              # chỉ trong thư mục truyện goblin
    python tools/gop_y.py <phieu.md> goblin/chapters/doan-007.md

Khớp theo thứ tự: nguyên câu 中 đã bôi → cả câu 中 chứa nó → mẩu chữ Hán dài nhất (≥4 chữ).
Không khớp được chỗ nào thì in "KHÔNG THẤY" và thoát mã 1.
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FIELDS = {
    "中": "zh",
    "Câu 中": "ctx_zh",
    "Việt": "vi",
    "Câu Việt": "ctx_vi",
    "Ghi chú": "note",
}


def parse(text):
    """Trả về danh sách dict: so, vi_tri, nhan, zh, ctx_zh, vi, ctx_vi, note, ban."""
    marks, cur, ban = [], None, ""
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("# Bản:"):
            ban = line[len("# Bản:"):].strip()
            continue
        m = re.match(r"^##\s+(\d+)(.*)$", line)
        if m:
            cur = {"so": int(m.group(1)), "ban": ban, "vi_tri": "", "nhan": "",
                   "zh": "", "ctx_zh": "", "vi": "", "ctx_vi": "", "note": ""}
            rest = m.group(2)
            t = re.search(r"\[([^\]]*)\]\s*$", rest)
            if t:
                cur["nhan"] = t.group(1)
                rest = rest[:t.start()]
            cur["vi_tri"] = rest.strip(" —-")
            marks.append(cur)
            continue
        if cur is None:
            continue
        for key, field in FIELDS.items():
            if line.startswith(key + ":"):
                cur[field] = line[len(key) + 1:].strip().replace(" ⏎ ", "\n")
                break
    return marks


def files_for(args):
    if not args:
        return sorted(glob.glob(os.path.join(ROOT, "*", "chapters", "*.md")))
    out = []
    for a in args:
        p = a if os.path.isabs(a) else os.path.join(ROOT, a)
        if os.path.isdir(p):
            for ext in ("md", "txt"):
                out += glob.glob(os.path.join(p, "**", "*." + ext), recursive=True)
        elif os.path.isfile(p):
            out.append(p)
    # chương trước, archive sau cùng
    return sorted(set(out), key=lambda f: ("archive" in f, "chapters" not in f, f))


HAN = re.compile(r"[㐀-鿿]+")


def needles(m):
    """Các chuỗi để dò, từ chắc nhất tới lỏng nhất."""
    out = []
    zh = m["zh"].split("\n")[0].strip()
    if zh:
        out.append(("nguyên câu", zh))
    ctx = m["ctx_zh"].split("\n")[0].strip()
    if ctx and ctx != zh:
        out.append(("cả câu", ctx))
    runs = sorted(HAN.findall(m["zh"] or m["ctx_zh"]), key=len, reverse=True)
    for r in runs[:2]:
        if len(r) >= 4 and r != zh:
            out.append(("mẩu " + str(len(r)) + " chữ", r))
    return out


def locate(m, files, cache):
    for how, nd in needles(m):
        hits = []
        for f in files:
            lines = cache.get(f)
            if lines is None:
                try:
                    with open(f, encoding="utf-8") as fh:
                        lines = fh.read().splitlines()
                except (OSError, UnicodeDecodeError):
                    lines = []
                cache[f] = lines
            for i, ln in enumerate(lines, 1):
                if nd in ln:
                    hits.append((f, i))
        if hits:
            return how, hits
    return None, []


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 2
    src = argv[0]
    text = sys.stdin.read() if src == "-" else open(src, encoding="utf-8").read()
    marks = parse(text)
    if not marks:
        print("Phiếu không có mục '## N' nào — có đúng là phiếu Góp ý khi nghe không?")
        return 2
    files = files_for(argv[1:])
    if not files:
        print("Không có file nào để dò:", " ".join(argv[1:]) or "*/chapters/*.md")
        return 2
    cache, missing = {}, 0
    for m in marks:
        head = "#%d [%s]" % (m["so"], m["nhan"] or "chưa nhãn")
        if m["vi_tri"]:
            head += " " + m["vi_tri"]
        print(head)
        if m["note"] and m["note"] != "(không ghi)":
            print("   ghi chú:", m["note"].replace("\n", " / "))
        if not (m["zh"] or m["ctx_zh"]):
            print("   (phiếu không có câu chữ Hán — bản nghe chưa convert; dò bằng Việt:", m["vi"][:60] + ")")
            missing += 1
            continue
        how, hits = locate(m, files, cache)
        if not hits:
            print("   KHÔNG THẤY trong", len(files), "file — 中:", (m["zh"] or m["ctx_zh"])[:60])
            missing += 1
            continue
        for f, i in hits[:3]:
            print("   -> %s:%d  (%s)" % (os.path.relpath(f, ROOT).replace("\\", "/"), i, how))
        if len(hits) > 3:
            print("   ... thêm %d chỗ khớp (câu quá chung, xem Câu 中)" % (len(hits) - 3))
        print("   中:", m["zh"][:80] or m["ctx_zh"][:80])
    print("\n%d chỗ, %d dò được, %d không" % (len(marks), len(marks) - missing, missing))
    return 1 if missing else 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
    sys.exit(main(sys.argv[1:]))
