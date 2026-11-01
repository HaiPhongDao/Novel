"""Dựng bản SI đem dán từ bản nguồn có chú thích, và đo ngân sách.

Vì sao có file này: SI là vật có ngân sách (phần dán <= 8.000 ký tự), nhưng bản nguồn cần thêm chú thích
`<!-- I-xxxx -->` để biết mỗi dòng luật do can thiệp nào sinh ra. Nếu sửa tay thẳng vào bản đem dán thì
chú thích lọt vào prompt gửi model, còn nếu không có chú thích thì khi một can thiệp bị gỡ, không ai biết
phải xoá đúng dòng nào — đó là cơ chế làm SI chỉ phình ra.

Nên tách đôi:
    <truyen>/gemini/system-instruction-vN.md   nguồn, có chú thích, giữ mọi đời
    <truyen>/gemini/si-dan-gemini.txt          bản dựng, không chú thích, không sửa tay

Dùng:
    python tools/dung_si.py <truyen>                 # dựng từ đời vN cao nhất
    python tools/dung_si.py <truyen> --version 3     # dựng từ đời cụ thể
    python tools/dung_si.py <truyen> --check         # chỉ đo, không ghi

Mã trả về: 0 = trong ngân sách, 1 = cảnh báo (8.000–9.000), 2 = vượt trần (phải reset).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

NGAN_SACH = 8000
TRAN = 9000

BAT_DAU = re.compile(r"=====\s*BẮT ĐẦU SI\s*=====")
HET = re.compile(r"=====\s*HẾT SI")

CHU_THICH = re.compile(r"<!--.*?-->", re.S)
O_TRONG = re.compile(r"\[\[.*?\]\]", re.S)


def doc_nguon(truyen: Path, version: str | None) -> Path:
    gemini = truyen / "gemini"
    if not gemini.is_dir():
        sys.exit(f"LỖI: không thấy {gemini}")
    ung_vien = []
    for p in gemini.glob("system-instruction*.md"):
        m = re.search(r"-v(\d+)", p.stem)
        ung_vien.append((int(m.group(1)) if m else 0, p))
    if not ung_vien:
        sys.exit(f"LỖI: {gemini} không có file system-instruction*.md")
    if version:
        for v, p in ung_vien:
            if str(v) == version.lstrip("v"):
                return p
        sys.exit(f"LỖI: không thấy đời v{version}")
    ung_vien.sort(key=lambda x: (x[0], x[1].stat().st_mtime))
    return ung_vien[-1][1]


def phan_dan(text: str) -> str:
    """Chỉ phần giữa hai dòng =====, tức phần thật sự dán vào model."""
    a = BAT_DAU.search(text)
    b = HET.search(text)
    if a and b and b.start() > a.start():
        return text[a.end():b.start()]
    return text


def dem_muc(than: str) -> dict:
    """Đếm mục theo khung v5, chịu được tên mục khác nhau giữa các đời SI."""
    dong = than.splitlines()
    part2 = bans = 0
    che_do = None
    for l in dong:
        s = l.strip()
        if re.match(r"(?i)^(part\s*2\b|every paragraph)", s):
            che_do = "part2"
            continue
        if re.match(r"(?i)^bans\b", s):
            che_do = "bans"
            continue
        if re.match(r"(?i)^(part\s*[134]\b|length\b|role\b|fixed conventions\b|style\b|output\b"
                    r"|golden finger\b|narration\b|moments\b)", s):
            che_do = None
            continue
        if che_do and s.startswith("- "):
            if che_do == "part2":
                part2 += 1
            else:
                bans += 1
    return {
        "part2": part2,
        "bans": bans,
        # "Sample anchor:" (v5) hay "Anchor:" (đời tự dựng) đều là một khối anchor.
        "anchor": len(re.findall(r"(?im)^\s*(?:sample\s+)?anchor\s*[:：]", than)),
        # Đếm cả KHỐI LƯỢNG anchor, không chỉ số cái: một SI có 2 anchor dài 1.000 ký tự mỗi cái
        # vẫn nuốt 41% ngân sách (manga-tokyo-2000) dù "đạt" về số lượng.
        "anchor_char": sum(len(b) for b in re.findall(r"```.*?```", than, re.S)),
        "chu_thich": len(CHU_THICH.findall(than)),
    }


def main(argv):
    ap = argparse.ArgumentParser(prog="dung_si.py")
    ap.add_argument("truyen")
    ap.add_argument("--version", default=None)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)

    truyen = Path(a.truyen).resolve()
    if not truyen.is_dir():
        sys.exit(f"LỖI: không thấy thư mục {truyen}")

    nguon = doc_nguon(truyen, a.version)
    tho = nguon.read_text(encoding="utf-8")
    than_tho = phan_dan(tho)

    if O_TRONG.search(than_tho):
        con = O_TRONG.findall(than_tho)
        sys.exit(f"LỖI: còn {len(con)} ô [[...]] chưa điền trong {nguon.name}. "
                 f"Ô đầu tiên: {con[0][:60]}")

    than = CHU_THICH.sub("", than_tho).strip()
    so = dem_muc(than)
    n = len(than)

    dich = truyen / "gemini" / "si-dan-gemini.txt"
    if not a.check:
        dich.write_text(than + "\n", encoding="utf-8", newline="\n")

    print(f"nguồn     {nguon.relative_to(truyen.parent)}")
    print(f"bản dựng  {dich.relative_to(truyen.parent)}" + ("  (chỉ đo, không ghi)" if a.check else ""))
    print(f"phần dán  {n} ký tự   ngân sách {NGAN_SACH}  trần {TRAN}")
    print(f"PART 2    {so['part2']} dòng   (trần 8)")
    print(f"BANS      {so['bans']} dòng   (đúng 5)")
    print(f"anchor    {so['anchor']} cái   (4–5)")
    phan_tram = round(100 * so["anchor_char"] / n) if n else 0
    print(f"anchor字  {so['anchor_char']} ký tự = {phan_tram}% phần dán   (trần 15%)")
    print(f"chú thích {so['chu_thich']} cái đã bỏ")

    van_de = []
    if so["part2"] > 8:
        van_de.append(f"PART 2 {so['part2']} dòng > 8 — phải cắt trước khi thêm dòng mới")
    if so["bans"] != 5:
        van_de.append(f"BANS {so['bans']} dòng, khung quy định đúng 5")
    if not (4 <= so["anchor"] <= 5):
        van_de.append(f"{so['anchor']} anchor, khung quy định 4–5")
    if phan_tram > 15:
        van_de.append(f"anchor chiếm {phan_tram}% phần dán > 15% — cái ít mà dài cũng nuốt ngân sách")
    for v in van_de:
        print(f"  CẢNH BÁO: {v}")

    if n > TRAN:
        print(f"  VƯỢT TRẦN: {n} > {TRAN} — dấu hiệu luật tích tụ, phải reset về SI lõi rồi sửa bằng cắt")
        return 2
    if n > NGAN_SACH:
        print(f"  CẢNH BÁO: vượt ngân sách {n - NGAN_SACH} ký tự — thêm một dòng thì phải bỏ một dòng")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
