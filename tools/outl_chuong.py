#!/usr/bin/env python3
"""Tach mot chuong tu bo mau 我在泡沫东京画漫画.txt ra chung/outliner-train/chNN/goc.txt.

Tai sao co: train Outliner (viet brief) can ban goc de lap "dap an noi dung" va cham do phu cua Writer
(chung/outliner-train/README.md). Dung: python tools/outl_chuong.py 9
"""
import re, sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
REPO = Path(__file__).resolve().parent.parent
SRC = REPO / "我在泡沫东京画漫画.txt"


def main():
    n = int(sys.argv[1])
    lines = SRC.read_text(encoding="utf-8").splitlines()
    heads = [i for i, l in enumerate(lines) if re.match(r"^# 第\d+章", l)]
    for k, i in enumerate(heads):
        if re.match(rf"^# 第{n}章", lines[i]):
            j = heads[k + 1] if k + 1 < len(heads) else len(lines)
            body = "\n".join(lines[i:j]).strip() + "\n"
            out = REPO / "chung" / "outliner-train" / f"ch{n:02d}" / "goc.txt"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(body, encoding="utf-8")
            han = len(re.findall(r"[一-鿿]", body))
            print(f"ch{n}: {j-i} dong, {han} chu Han -> {out}")
            return
    print("khong thay chuong", n)
    sys.exit(1)


main()
