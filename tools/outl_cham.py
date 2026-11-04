#!/usr/bin/env python3
"""Phan loai nhanh do phu noi dung cua ban Writer so voi "dap an" trich tu chuong mau (train Outliner).

Tai sao co (04/11/2026): train Outliner = viet brief tu noi dung chuong mau, cho Writer viet, xem Writer co viet du
noi dung khong. Doc het tung ban rat ton; script nay chi PHAN LOAI (tu khoa trong dap-an.json) de khoanh cho can doc.
Khong ket luan DAT: don vi "?" (khong thay tu khoa) phai doc tay roi moi coi la thieu; tu khoa trung khong co
nghia la dung y. Ket luan do doc, ghi vao chung/outliner-train/chNN/cham-vX.md.

Dung: python tools/outl_cham.py chung/outliner-train/ch09/dap-an.json ban1.md ban2.md ...
Dap-an: don_vi[{id, nhom BB|PH|TX, mo_ta, kw[], kw2[]?}] ; kw2 neu co thi phai trung CA kw LAN kw2 ; "dung" = id don vi danh dau diem dung.
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")


def doc_ban(p):
    t = Path(p).read_text(encoding="utf-8")
    return "\n".join(l for l in t.splitlines() if not l.strip().startswith("<!--")).strip()


def han(t):
    return len(re.findall(r"[一-鿿]", t))


NUM = re.compile(r"[一二三四五六七八九十百千万两〇零\d]{2,}(?:个|名|份|页|岁|年|天|分钟|位|条|部|次|张|支|串|杯|扎|日|月|号|楼|层|周|倍|成|円|日元|人)")


def so_cung(t):
    """Cac so cung >= 2 chu so trong ban (de Agent doi chieu voi brief: so nao brief khong trao la so Writer tu bia)."""
    return sorted(set(NUM.findall(t)))


def khop(t, kws):
    return [m.start() for k in kws for m in re.finditer(re.escape(k), t)]


def main():
    da = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    files = sys.argv[2:]
    cols = [Path(f).stem for f in files]
    txt = [doc_ban(f) for f in files]
    print(f"Chuong {da['chuong']} — {da.get('tieu_de','')} | goc {da.get('han_goc','?')} chu Han")
    print("| don vi | nhom | " + " | ".join(cols) + " | mo ta |")
    print("|---|---|" + "---|" * len(cols) + "---|")
    for u in da["don_vi"]:
        cells = []
        for t in txt:
            a = khop(t, u["kw"])
            ok = bool(a)
            if ok and u.get("kw2"):
                ok = bool(khop(t, u["kw2"]))
            cells.append(f"co({len(a)})" if ok else "?")
        print(f"| {u['id']} | {u['nhom']} | " + " | ".join(cells) + f" | {u['mo_ta'][:70]} |")
    print()
    dung = next((u for u in da["don_vi"] if u["id"] == da.get("dung")), None)
    for f, t in zip(cols, txt):
        dong = [l for l in t.splitlines() if l.strip()]
        thoai = sum(1 for l in dong if l.lstrip().startswith(("“", "「", "\"")))
        s = f"{f}: {han(t)} chu Han, {len(dong)} doan, {thoai} luot thoai"
        if dung:
            pos = khop(t, dung["kw"])
            if pos:
                sau = han(t[pos[-1]:])
                s += f", sau tu khoa cuoi cua '{dung['id']}' con {sau} chu Han"
            else:
                s += f", khong thay tu khoa diem dung '{dung['id']}'"
        print(s)
        print("   so cung:", " ".join(so_cung(t)) or "-")


main()
