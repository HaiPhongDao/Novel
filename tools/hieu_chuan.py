"""Hiệu chuẩn SI trên nội dung bộ mẫu — biết SI có làm việc không TRƯỚC khi dựng truyện.

Vì sao có file này: quy trình cũ dựng bible → dàn ý → SI → viết đoạn 001, rồi tranh luận
xem văn hay hay dở. Lúc đó có quá nhiều biến cùng lúc (nhân vật mới, cảnh mới, SI mới),
nên không biết chỗ hỏng nằm ở đâu. Cách tách được biến: lấy **chính nội dung bộ mẫu** —
đã có đáp án — đưa cho Writer viết lại từ một brief chỉ có sự việc, rồi so bản sinh với
nguyên văn mẫu. Khác biệt giữa hai bên chính là phần SI chưa dạy được.

Dùng:
    python tools/hieu_chuan.py tach --file <bo-mau.txt> --chuong 1 --out chung/hieu-chuan/manga/ch01
    python tools/hieu_chuan.py so-sanh --goc chung/hieu-chuan/manga/ch01/goc.txt --sinh <ban.md>

`so-sanh` in bảng số của hai bên cạnh nhau + chỉ số "giảng huấn" (người kể giảng giải:
chân lý chung, quy tắc nghề, giải thích ngành). Chỉ số đó không có trong soat_van.py vì
nó cần đọc, nhưng đếm được — và nó là thứ Tác giả gọi là "nói linh tinh".
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

# Người kể giảng giải: câu chân lý chung, quy tắc nghề, giải thích ngành.
# Đây là lớp tật si-khung.md gọi là "câu chân lý chung" và review-blacklist gọi là
# "lời kể giải thích lý lịch / động cơ" — trước giờ không có cột nào đếm.
GIANG_HUAN = re.compile(
    r"法则|铁律|规律|规矩|道理|潜规则|行业里|这一行|编辑部里|通常|往往|总是|从来|一律"
    r"|意味着|也就是说|换句话说|说白了|本质上|事实上"
    r"|不会同情|不会因为|不会为|没有人会|谁都|谁都明白"
    r"|教会了他|让他懂得|他明白|他清楚|他知道，这"
)

QUOTE = re.compile(r"“([^”]+)”")


def han(s):
    return sum(1 for c in s if "\u4e00" <= c <= "\u9fff")


def doan(text):
    t = re.sub(r"^<!--.*?-->\s*", "", text, flags=re.S)
    paras = [p.strip() for p in re.split(r"\n\s*\n", t) if p.strip()]
    # Bộ mẫu .txt ngắt đoạn bằng dòng mới + hai khoảng trắng toàn giác, không có dòng trống.
    # Không có nhánh này thì cả chương thành 1 đoạn, và mọi cột "字/đoạn", "% đoạn có thoại"
    # đều vô nghĩa (đúng lỗi đã ghi ở manga-tokyo-1998/thu-v5-phat-hien.md mục 4).
    if len(paras) <= 1:
        paras = [p.strip() for p in t.splitlines() if p.strip()]
    return paras


def cau(text):
    return [x for x in re.split(r"(?<=[。！？…])", text) if han(x) >= 2]


def do(text: str) -> dict:
    paras = doan(text)
    body = "\n".join(paras)
    n_han = han(body) or 1
    c_list = cau(QUOTE.sub("。", body))
    turns = [q.strip() for q in QUOTE.findall(body) if han(q) > 0]
    gh = GIANG_HUAN.findall(body)
    return {
        "han": n_han,
        "doan": len(paras),
        "han_doan": round(n_han / len(paras), 1) if paras else 0,
        "cau": len(c_list),
        "han_cau": round(sum(han(x) for x in c_list) / len(c_list), 1) if c_list else 0,
        "luot": len(turns),
        "han_luot": round(sum(han(t) for t in turns) / len(turns), 1) if turns else 0,
        "ti_le_thoai": round(sum(1 for p in paras if "“" in p) / len(paras) * 100) if paras else 0,
        "giang_huan": len(gh),
        "giang_huan_1000": round(len(gh) / n_han * 1000, 2),
        "giang_huan_vd": gh[:6],
    }


def tach_mau(text: str, so: int) -> str:
    hs = list(re.finditer(r"(?m)^\s*#?\s*第(\d+)章[^\n]*$", text))
    for i, h in enumerate(hs):
        if int(h.group(1)) == so:
            dau = h.end()
            cuoi = hs[i + 1].start() if i + 1 < len(hs) else len(text)
            return text[dau:cuoi].strip("\n")
    raise SystemExit(f"LỖI: không thấy chương {so} (tìm được {len(hs)} chương)")


def cmd_tach(argv):
    ap = _ap("tach", "Tách một chương của bộ mẫu ra file đáp án")
    ap.add_argument("--file", required=True)
    ap.add_argument("--chuong", type=int, required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    src = Path(a.file)
    if not src.is_file():
        raise SystemExit(f"LỖI: không thấy {src}")
    chuong = tach_mau(src.read_text(encoding="utf-8", errors="replace"), a.chuong)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "goc.txt").write_text(chuong + "\n", encoding="utf-8", newline="\n")
    d = do(chuong)
    print(f"chương {a.chuong} → {out / 'goc.txt'}")
    print(f"  {d['han']} chữ Hán · {d['doan']} đoạn · {d['han_cau']} 字/câu · "
          f"{d['luot']} lượt thoại · {d['han_luot']} 字/lượt · giảng huấn {d['giang_huan_1000']}/1.000")
    print("\nViệc tiếp theo: viết `brief.md` trong cùng thư mục — CHỈ sự việc của chương này "
          "(ai, ở đâu, muốn gì, chuyện gì xảy ra, dừng ở đâu), không chép câu văn, không chép thoại.")


def cmd_so_sanh(argv):
    ap = _ap("so-sanh", "So bản sinh với nguyên văn mẫu")
    ap.add_argument("--goc", required=True)
    ap.add_argument("--sinh", required=True)
    a = ap.parse_args(argv)
    g = do(Path(a.goc).read_text(encoding="utf-8"))
    s = do(Path(a.sinh).read_text(encoding="utf-8"))

    hang = [
        ("chữ Hán", "han", ""),
        ("số đoạn", "doan", ""),
        ("字/đoạn", "han_doan", ""),
        ("số câu", "cau", ""),
        ("字/câu", "han_cau", ""),
        ("lượt thoại", "luot", ""),
        ("字/lượt thoại", "han_luot", ""),
        ("% đoạn có thoại", "ti_le_thoai", "%"),
        ("giảng huấn /1.000", "giang_huan_1000", ""),
    ]
    print(f"{'':<18}{'mẫu':>9}{'bản sinh':>11}{'lệch':>9}")
    print("-" * 47)
    for nhan, k, dv in hang:
        x, y = g[k], s[k]
        lech = (y / x - 1) * 100 if x else 0
        print(f"{nhan:<18}{str(x)+dv:>9}{str(y)+dv:>11}{lech:>8.0f}%")
    print()
    if s["giang_huan_vd"]:
        print("chỗ giảng huấn trong bản sinh (mẫu để trống thì đó là tật):")
        for v in s["giang_huan_vd"]:
            print("  ·", v)
    if g["giang_huan_vd"]:
        print("mẫu cũng có (đừng coi là tật):", " · ".join(g["giang_huan_vd"]))
    print("\nĐọc thêm bằng mắt: mở hai file cạnh nhau, so 3 đoạn đầu và 3 đoạn cuối — "
          "chỗ nào bản sinh nói thứ mẫu không nói, đó là chỗ SI chưa dạy được.")


def _ap(ten, mo_ta):
    import argparse
    return argparse.ArgumentParser(prog=f"hieu_chuan.py {ten}", description=mo_ta)


LENH = {"tach": cmd_tach, "so-sanh": cmd_so_sanh}


def main(argv):
    if len(argv) < 2 or argv[1] not in LENH:
        print(__doc__)
        return 2
    return LENH[argv[1]](argv[2:]) or 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
