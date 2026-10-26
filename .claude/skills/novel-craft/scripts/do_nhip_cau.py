"""Đo nhịp câu của một bản thảo tiếng Trung (dùng khi Tác giả bắt lỗi câu cụt hoặc câu trượt dài).

Dùng:
    python scripts/do_nhip_cau.py <file.md> [<file2.md> ...]

Chỉ đo phần LỜI KỂ (bỏ thoại trong “ ”), vì nhịp thoại đã có `tools/soat_van.py`
(`luot-thoai`, `tb-chu-luot`, `luot-cut`, `the-thoai`).

Vùng đích rút từ nhiều vòng thử có đo:
    % mệnh đề <= 4 chữ : 9–13
    chữ / mệnh đề     : 10–12
    chữ / câu kể      : 21–32
    câu cụt (<=5 chữ) : 0–2 mỗi đoạn ~1.800 字
Lệch dưới = câu vụn ("发凉。" "二十三岁，刚捡回一条命。"); lệch trên = câu thành báo cáo một trượt.
"""
import re
import sys
from pathlib import Path


def han(s):
    return sum(1 for c in s if "\u4e00" <= c <= "\u9fff")


def stats(path):
    text = Path(path).read_text(encoding="utf-8")
    text = re.sub(r"^<!--.*?-->\s*", "", text, flags=re.S)
    narration = re.sub(r"“[^”]*”", "。", text)
    clauses = [c.strip() for c in re.split(r"[。！？；…\n，、]+", narration) if c.strip()]
    cl = [han(c) for c in clauses if han(c) > 0]
    sents = [s.strip() for s in re.split(r"[。！？；…\n]+", narration) if s.strip()]
    sl = [han(s) for s in sents if han(s) > 0]
    if not cl or not sl:
        return None
    return {
        "file": Path(path).name,
        "han": han(narration),
        "clauses": len(cl),
        "cl_mean": round(sum(cl) / len(cl), 1),
        "cl_short%": round(sum(1 for n in cl if n <= 4) / len(cl) * 100),
        "sents": len(sl),
        "sent_mean": round(sum(sl) / len(sl), 1),
        "sents<=5": sum(1 for n in sl if n <= 5),
    }


def verdict(row):
    flags = []
    if row["cl_short%"] < 9 or row["sent_mean"] < 21:
        flags.append("câu vụn")
    if row["cl_short%"] > 13 or row["sent_mean"] > 32:
        flags.append("câu trượt dài")
    return ", ".join(flags) or "trong vùng"


def main(argv):
    files = [a for a in argv[1:] if not a.startswith("--")]
    if not files:
        print(__doc__)
        return 2
    rows = [r for r in (stats(f) for f in files) if r]
    if not rows:
        print("không đọc được lời kể nào")
        return 2
    cols = list(rows[0].keys())
    w = max(len(c) for c in cols + ["đánh giá"]) + 2
    print("".join(c.ljust(w) for c in cols) + "đánh giá")
    for r in rows:
        print("".join(str(r[c]).ljust(w) for c in cols) + verdict(r))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
