#!/usr/bin/env python3
"""Rà soát định kỳ (mỗi 5 đoạn) — nhân vật vắng lâu, tuyến đứng yên, cài cắm quá hạn.

Dùng:  python tools/ra_soat.py <thu-muc-truyen> [--vang 10] [--dung 8]
Đọc:   <truyen>/bible/glossary.md (bảng "Tên riêng") + <truyen>/chapters/doan-*.md
       <truyen>/plot/threads.md (bảng có cột ID)
Ra:    báo cáo in ra màn hình; không sửa file nào.
Ngưỡng và cách xử lý: chung/giu-nhat-quan.md mục 4.

Tên quét trong chính văn lấy từ glossary: chữ Latin trong cột Tiếng Việt (bỏ họ dùng chung nhiều dòng,
vd. Varen) + các tên trong cột 中文. Tuyến: cột "Chạm gần nhất" và "Hạn payoff" (số đoạn); threads.md
kiểu cũ không có hai cột này thì chỉ đoán số đoạn từ "Cài ở" / "Dự kiến payoff".
"""
import argparse
import re
import sys
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

DONG = ("đã trả", "đã đóng", "đóng", "xong", "bỏ", "huỷ", "hủy")
GAC = ("để sau", "tạm gác", "gác")


def tables(text: str):
    """Trả về các bảng markdown: list of (header, rows), mỗi row là list ô."""
    out, cur = [], None
    for line in text.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            cur = None
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if cur is None:
            cur = (cells, [])
            out.append(cur)
        elif not all(re.fullmatch(r":?-+:?", c) for c in cells if c):
            cur[1].append(cells)
    return out


def segments(story: Path):
    segs = {}
    for p in sorted(story.glob("chapters/doan-*.md")):
        m = re.fullmatch(r"doan-(\d+)", p.stem)
        if m:
            segs[int(m.group(1))] = p.read_text(encoding="utf-8")
    return segs


def name_rows(story: Path):
    g = story / "bible" / "glossary.md"
    if not g.exists():
        return []
    text = g.read_text(encoding="utf-8")
    part = text.split("## Tên riêng", 1)[-1].split("\n## ", 1)[0]
    rows = []
    for header, body in tables(part):
        for r in body:
            if len(r) < 2 or not r[0]:
                continue
            latin = re.findall(r"(?<![\w-])[A-Z][a-z]{2,}(?![\w-])", r[0])
            zh = [z for z in re.split(r"[（）()/、，,\s]+", r[1]) if re.search(r"[一-鿿]", z)]
            rows.append((r[0], latin, zh))
    shared = Counter(w for _, latin, _ in rows for w in set(latin))
    return [(label, [w for w in latin if shared[w] == 1] + zh) for label, latin, zh in rows]


def first_int(cell: str, loose=True):
    """Số đoạn trong ô. loose=False (threads.md kiểu cũ): chỉ nhận "đoạn N" / "chN", bỏ "arc N"."""
    pat = r"\d+" if loose else r"(?:đoạn|doan-|ch)\s*(\d+)"
    m = re.search(pat, cell or "", flags=re.I)
    return int(m.group(m.lastindex or 0)) if m else None


def col(header, *keys):
    for i, h in enumerate(header):
        hl = h.lower()
        if any(k in hl for k in keys):
            return i
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("story")
    ap.add_argument("--vang", type=int, default=10, help="nhân vật vắng từ N đoạn trở lên")
    ap.add_argument("--dung", type=int, default=8, help="tuyến không được chạm từ N đoạn trở lên")
    args = ap.parse_args()
    story = Path(args.story)
    segs = segments(story)
    if not segs:
        raise SystemExit("Chưa có đoạn nào trong chapters/")
    now = max(segs)
    print(f"# Rà soát {story.name} — hết đoạn {now:03d}\n")

    print(f"## Nhân vật / tên riêng vắng ≥ {args.vang} đoạn\n")
    found = False
    for label, aliases in name_rows(story):
        if not aliases:
            continue
        hits = [n for n, t in segs.items() if any(a in t for a in aliases)]
        if not hits:
            print(f"- {label}: chưa lên trang (quét: {', '.join(aliases)})")
            found = True
        elif now - max(hits) >= args.vang:
            print(f"- {label}: lần cuối đoạn {max(hits):03d}, vắng {now - max(hits)} đoạn")
            found = True
    print("" if found else "(không có)\n")

    th = story / "plot" / "threads.md"
    if not th.exists():
        return
    print("## Tuyến / cài cắm\n")
    overdue, stale, guessed = [], [], False
    for header, body in tables(th.read_text(encoding="utf-8")):
        i_id = col(header, "id")
        i_st = col(header, "trạng thái")
        if i_id is None or i_st is None:  # bảng "Đã trả" không có cột trạng thái → bỏ qua
            continue
        i_name = col(header, "tuyến", "chi tiết")
        i_touch = col(header, "chạm")
        i_due = col(header, "hạn")
        old_style = i_due is None or i_touch is None
        if i_due is None:
            i_due = col(header, "payoff")
        guessed = guessed or (old_style and bool(body))
        i_plant = col(header, "cài ở")
        for r in body:
            get = lambda i: r[i] if i is not None and i < len(r) else ""
            st = get(i_st).lower()
            if any(k in st for k in DONG):
                continue
            label = f"{get(i_id)} — {get(i_name)[:70]}"
            due = first_int(get(i_due), loose=not old_style)
            if due and due < now and not any(k in st for k in GAC):
                overdue.append(f"- {label} (hạn đoạn {due}, trạng thái: {get(i_st) or '—'})")
            touch = first_int(get(i_touch)) if i_touch is not None else None
            if touch is None and i_touch is None:
                touch = first_int(get(i_plant), loose=False)
            if touch and now - touch >= args.dung and not any(k in st for k in GAC):
                stale.append(f"- {label} (chạm gần nhất đoạn {touch}, {now - touch} đoạn trước)")
    print("**Quá hạn payoff**")
    print("\n".join(overdue) or "(không có)")
    print(f"\n**Đứng yên ≥ {args.dung} đoạn**")
    print("\n".join(stale) or "(không có)")
    if guessed:
        print("\n> threads.md chưa có cột \"Chạm gần nhất\" / \"Hạn payoff\": số đoạn được đoán từ chữ trong ô, "
              "có thể lệch (vd. \"ch5\" kiểu đánh số cũ). Mẫu cột mới: _mau-truyen/plot/threads.md.")


if __name__ == "__main__":
    main()
