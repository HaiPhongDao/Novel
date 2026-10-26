"""Cắt phần cuối của đoạn trước để dán vào prompt đoạn sau (giữ giọng khi --new mở chat trắng).

Dùng:
    python tools/noi_doan.py <file.md> [--chars 320] [--wrap] [--out <file>]

- Cắt theo **đoạn trọn vẹn** (không cắt giữa câu): lấy các đoạn cuối cho tới khi đủ ~N chữ Hán.
- --wrap: bọc trong 【接上】 … 【接上完】 để cham_doan.py bỏ qua khi kiểm chép mẫu.
"""
import argparse
import re
from pathlib import Path

HAN = re.compile(r"[\u4e00-\u9fff]")


def han(s):
    return len(HAN.findall(s))


def tail(path, chars=320):
    text = Path(path).read_text(encoding="utf-8")
    text = re.sub(r"^<!--.*?-->\s*", "", text, flags=re.S)
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    if not paras:
        paras = [p.strip() for p in text.split("\n") if p.strip()]
    picked, total = [], 0
    for p in reversed(paras):
        picked.append(p)
        total += han(p)
        if total >= chars:
            break
    return "\n".join(reversed(picked))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--chars", type=int, default=320)
    ap.add_argument("--wrap", action="store_true")
    ap.add_argument("--out")
    a = ap.parse_args()
    t = tail(a.file, a.chars)
    if a.wrap:
        t = "【接上】\n" + t + "\n【接上完】"
    if a.out:
        Path(a.out).write_text(t + "\n", encoding="utf-8", newline="\n")
        print(f"{a.out} | {han(t)} chữ Hán")
    else:
        print(t)


if __name__ == "__main__":
    main()
