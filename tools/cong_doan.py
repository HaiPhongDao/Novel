"""Cổng máy cho một bản thảo Writer: chặn bản hỏng rõ ràng trước khi đo/review/commit.

Dùng:
    python tools/cong_doan.py <bản.md> --prompt <brief.md> [--prev <đoạn-trước-đã-duyệt.md>]

Đỏ (exit 1) khi:
  - bản cụt: câu cuối không kết bằng dấu câu;
  - ngắn bất thường: < 60% cận dưới cửa sổ 字 ghi trong brief ("2.000–3.000 字", "khoảng 2000 chữ");
  - chép mẫu: một câu tiếng Hán >= 10 chữ của brief (kể cả khối giọng mẫu/接上) hay của đuôi đoạn trước
    xuất hiện nguyên văn trong bản.
Vàng (chỉ cảnh báo): chưa chuẩn hoá dòng trống giữa các đoạn.
Xanh không có nghĩa là văn đạt — chỉ là bản đáng để đọc. Sau đó in số đo của cham_doan.py để tham khảo.
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cham_doan

HAN = re.compile(r"[一-鿿]")
END_OK = "。！？”」』…）】!?\"'"


def han(s):
    return len(HAN.findall(s))


def load(path):
    t = open(path, encoding="utf-8", errors="replace").read()
    return re.sub(r"^<!--.*?-->\s*", "", t, flags=re.S)


def sentences(text, min_han=10):
    out = []
    for s in re.split(r"[。！？；…\n“”「」]+", text):
        s = s.strip(" 　，、")
        if han(s) >= min_han:
            out.append(s)
    return out


def target_floor(brief):
    nums = lambda s: int(s.replace(".", "").replace(",", ""))
    m = re.search(r"(\d[\d.,]{2,})\s*[–\-~—]\s*(\d[\d.,]{2,})\s*(字|chữ)", brief)
    if m:
        return nums(m.group(1))
    m = re.search(r"(?:khoảng|chừng|~)\s*(\d[\d.,]{2,})\s*(字|chữ)", brief)
    return nums(m.group(1)) if m else None


def gate(draft_path, prompt_path, prev_path=None):
    t = load(draft_path)
    brief = open(prompt_path, encoding="utf-8").read()
    red, warn = [], []

    last = t.rstrip()[-1:] if t.strip() else ""
    if last not in END_OK:
        red.append(f"bản cụt: câu cuối kết bằng '{last}' — capture hỏng, chạy lại ở chat mới")

    n = han(t)
    floor = target_floor(brief)
    if floor and n < 0.6 * floor:
        red.append(f"ngắn bất thường: {n} 字, brief đòi từ {floor} 字 — nghi capture hỏng")

    sources = sentences(brief)
    if prev_path:
        prev = load(prev_path)
        sources += sentences(prev[-1500:])
    copied = sorted({s for s in sources if s in t}, key=len, reverse=True)
    if copied:
        red.append("chép mẫu: " + " | ".join(s[:24] for s in copied[:5]))

    lines = [l for l in t.split("\n") if l.strip()]
    if sum(1 for l in lines if l.startswith("　　")) > 5 and not re.search(r"\n\s*\n", t):
        warn.append("chưa có dòng trống giữa các đoạn — lưu raw vào archive/ rồi chuẩn hoá trước khi đo nhịp đoạn")

    name = os.path.basename(draft_path)
    if red:
        print(f"{name}  →  ĐỎ")
        for r in red:
            print("  ✗ " + r)
    else:
        print(f"{name}  →  XANH ({n} 字) — đáng để đọc, chưa phải ĐẠT")
    for w in warn:
        print("  ! " + w)
    return not red


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("draft")
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--prev")
    ap.add_argument("--modern", action="store_true")
    a = ap.parse_args()
    ok = gate(a.draft, a.prompt, a.prev)
    if ok:
        print()
        cham_doan.report(a.draft, a.prompt, None, a.modern)
    sys.exit(0 if ok else 1)
