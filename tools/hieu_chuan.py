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
    """Tách đoạn theo đơn vị thật của văn Trung: mỗi dòng `　　` là một đoạn.

    Bộ mẫu .txt và bản Writer trả về đều ngắt đoạn bằng dòng mới + hai khoảng trắng toàn
    giác, không có dòng trống. Nếu chỉ tách theo dòng trống thì 211 dòng thành 12 "đoạn"
    và cột 字/đoạn sai gấp 8 lần — đúng lỗi đã ghi ở manga-tokyo-1998/thu-v5-phat-hien.md.
    """
    t = re.sub(r"^<!--.*?-->\s*", "", text, flags=re.S)
    raw = [x for x in t.splitlines() if x.strip()]
    # Kiểm trên dòng THÔ: str.strip() ăn luôn U+3000, nên nếu strip trước rồi mới kiểm
    # "　　" thì không bao giờ khớp và cả chương bị gộp thành vài "đoạn" theo dòng trống.
    thut = sum(1 for x in raw if x.startswith("　　"))
    lines = [x.strip() for x in raw]
    if lines and thut >= max(3, len(lines) // 2):
        return lines
    paras = [p.strip() for p in re.split(r"\n\s*\n", t) if p.strip()]
    return paras if len(paras) > 1 else lines


def cau(text):
    return [x for x in re.split(r"(?<=[。！？…])", text) if han(x) >= 2]


def do(text: str) -> dict:
    paras = doan(text)
    body = "\n".join(paras)
    n_han = han(body) or 1
    c_list = cau(QUOTE.sub("。", body))
    turns = [q.strip() for q in QUOTE.findall(body) if han(q) > 0]
    gh = GIANG_HUAN.findall(body)
    dai = [han(x) for x in paras if han(x)]
    ngan = sum(1 for v in dai if v < 12)
    return {
        "han": n_han,
        "doan": len(paras),
        "han_doan": round(n_han / len(paras), 1) if paras else 0,
        # Đoạn dài nhất là chỉ số bắt bệnh "mỗi dòng một mệnh đề": bản băm vụn không bao
        # giờ có đoạn dài, dù trung bình có thể vẫn trong biên độ.
        "doan_max": max(dai) if dai else 0,
        "ti_le_ngan": round(ngan / len(dai) * 100, 1) if dai else 0,
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


# Biên độ lấy từ NHIỀU chương mẫu, không từ một chương. Một chương chỉ là một mẫu thăm dò:
# chương 1 của bộ mẫu có 19,7 字/đoạn trong khi trung bình 30 chương là 24,9 — lấy một
# chương làm chuẩn thì bản bình thường cũng bị coi là lệch, và ngược lại.
BANG_MAU = ROOT / "chung" / "hieu-chuan" / "bang-mau.json"
CHI_SO_GATE = ("han_doan", "han_cau", "luot", "han_luot", "giang_huan_1000", "doan_max")


def cmd_do_chuong(argv):
    ap = _ap("do-chuong", "Đo nhiều chương mẫu để lấy biên độ thật cho từng chỉ số")
    ap.add_argument("--file", required=True)
    ap.add_argument("--so-chuong", type=int, default=30)
    ap.add_argument("--out", default=str(BANG_MAU))
    a = ap.parse_args(argv)
    import json
    import statistics
    txt = Path(a.file).read_text(encoding="utf-8", errors="replace")
    rows = []
    for i in range(1, a.so_chuong + 1):
        try:
            rows.append(do(tach_mau(txt, i)))
        except SystemExit:
            break
    if len(rows) < 5:
        raise SystemExit("LỖI: cần ít nhất 5 chương để có biên độ")
    bang = {"nguon": Path(a.file).name, "so_chuong": len(rows), "chi_so": {}}
    print(f"đo {len(rows)} chương của {Path(a.file).name}")
    print(f"{'chỉ số':<20}{'TB':>9}{'SD':>8}{'dưới':>9}{'trên':>9}")
    for k in CHI_SO_GATE + ("ti_le_thoai",):
        xs = [r[k] for r in rows]
        m, sd = statistics.mean(xs), statistics.stdev(xs)
        duoi, tren = max(0.0, m - 2 * sd), m + 2 * sd
        bang["chi_so"][k] = {"tb": round(m, 3), "sd": round(sd, 3),
                             "duoi": round(duoi, 3), "tren": round(tren, 3)}
        print(f"{k:<20}{m:>9.2f}{sd:>8.2f}{duoi:>9.1f}{tren:>9.1f}")
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(bang, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
    print(f"\nđã ghi {a.out}")
    print("hai chỉ số tật (so sánh người kể, nhãn ngữ điệu) đo bằng `so_loi.py do-mau` trên cả bộ mẫu.")


def _doc_bang():
    import json
    if not BANG_MAU.is_file():
        raise SystemExit(
            f"LỖI: chưa có {BANG_MAU.name}. Chạy trước:\n"
            f"  python tools/hieu_chuan.py do-chuong --file 我在泡沫东京画漫画.txt")
    return json.loads(BANG_MAU.read_text(encoding="utf-8"))


def cmd_ghep_cap(argv):
    """Sinh file đọc cặp: đoạn mẫu và đoạn sinh ở cùng vị trí tương đối.

    Số đo chỉ ra chỗ lệch; muốn biết lệch thế nào phải ĐỌC hai bản cạnh nhau. File này ghép
    sẵn 12 điểm để đọc mất vài phút thay vì cuộn hai file.
    """
    ap = _ap("ghep-cap", "Ghép các cặp đoạn để đọc cạnh nhau")
    ap.add_argument("--goc", required=True)
    ap.add_argument("--sinh", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--diem", type=int, default=12)
    a = ap.parse_args(argv)
    g = doan(Path(a.goc).read_text(encoding="utf-8"))
    s = doan(Path(a.sinh).read_text(encoding="utf-8"))

    def tai(ps, ty):
        return ps[min(len(ps) - 1, int(ty * len(ps)))] if ps else ""

    L = ["# Đọc cặp — mẫu và bản sinh ở cùng vị trí", "",
         "Số đo chỉ chỉ ra chỗ lệch. Ở đây bày ra để đọc: chỗ nào bản sinh nói thứ mẫu không nói,",
         "hoặc bỏ thứ mẫu có, là chỗ SI chưa dạy được.", "",
         "| Vị trí | Nguyên văn mẫu | Bản sinh |", "|---|---|---|"]
    for i in range(a.diem):
        ty = (i + 0.5) / a.diem
        x = tai(g, ty)[:220].replace("|", "\\|")
        y = tai(s, ty)[:220].replace("|", "\\|")
        L.append(f"| {int(ty*100)}% | {x} | {y} |")
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")
    print(f"đã ghi {out} ({a.diem} cặp)")


def cmd_so_sanh(argv):
    ap = _ap("so-sanh", "So bản sinh với biên độ nhiều chương mẫu và PHÁN QUYẾT")
    ap.add_argument("--goc", required=True, help="nguyên văn một chương mẫu (để in cạnh)")
    ap.add_argument("--sinh", required=True)
    ap.add_argument("--doc-cap", default="", help="nếu có, ghi luôn file đọc cặp vào đây")
    a = ap.parse_args(argv)
    bang = _doc_bang()
    g = do(Path(a.goc).read_text(encoding="utf-8"))
    s = do(Path(a.sinh).read_text(encoding="utf-8"))
    if s["han"] < 800:
        print(f"LỖI: bản sinh chỉ có {s['han']} chữ Hán — cụt hoặc hỏng, không cần chẩn đoán.")
        return 1

    hang = [("字/đoạn", "han_doan"), ("字/câu", "han_cau"), ("lượt thoại", "luot"),
            ("字/lượt thoại", "han_luot"), ("% đoạn có thoại", "ti_le_thoai"),
            ("giảng huấn /1.000", "giang_huan_1000"), ("đoạn dài nhất", "doan_max")]
    print(f"biên độ: {bang['so_chuong']} chương của {bang['nguon']} (TB ± 2SD)\n")
    print(f"{'chỉ số':<20}{'mẫu ch.1':>10}{'bản sinh':>10}{'biên độ':>18}   phán")
    print("-" * 68)
    hong = []
    for nhan, k in hang:
        b = bang["chi_so"].get(k)
        if not b:
            continue
        y = s[k]
        trong = b["duoi"] <= y <= b["tren"]
        gate = k in CHI_SO_GATE
        if not trong and gate:
            hong.append(f"{nhan}: {y} ngoài [{b['duoi']}–{b['tren']}]")
        dau = "OK" if trong else ("LỆCH" if gate else "(tham khảo)")
        dai = f"{b['duoi']}–{b['tren']}"
        print(f"{nhan:<20}{g[k]:>10}{y:>10}{dai:>18}   {dau}")

    print()
    print("Hai chỉ số tật (so sánh người kể, nhãn ngữ điệu) không nằm trong bảng này —")
    print("đo bằng `so_loi.py quet` và so với `chung/loi/muc-tieu.jsonl`.")
    if a.doc_cap:
        cmd_ghep_cap(["--goc", a.goc, "--sinh", a.sinh, "--out", a.doc_cap])

    print()
    if hong:
        print("CHẨN ĐOÁN (không phải điểm, không phải cổng) — mấy chỗ này lệch khỏi bộ mẫu:")
        for h in hong:
            print("  ·", h)
        print("\nSố đo KHÔNG nói văn hay hay dở, và không được dùng làm đích trong SI:")
        print("đưa con số nhịp vào SI thì Writer tối ưu cho con số (đo được: SI ghi 18–26 ra 11–15).")
        print("Đọc `--doc-cap` rồi tự quyết. Muốn nhịp đúng thì sửa **anchor**, không sửa số.")
        return 0
    print("Chẩn đoán: các cột trên không lệch khỏi bộ mẫu. Đây cũng KHÔNG phải bằng chứng văn hay —")
    print("đếm chữ không đo được tiểu thuyết. Việc quyết định vẫn là đọc `--doc-cap`, và nhịp thì do")
    print("anchor gánh, không do khối số nào trong SI.")
    return 0


def _ap(ten, mo_ta):
    import argparse
    return argparse.ArgumentParser(prog=f"hieu_chuan.py {ten}", description=mo_ta)


LENH = {"tach": cmd_tach, "do-chuong": cmd_do_chuong,
        "so-sanh": cmd_so_sanh, "ghep-cap": cmd_ghep_cap}


def main(argv):
    if len(argv) < 2 or argv[1] not in LENH:
        print(__doc__)
        return 2
    return LENH[argv[1]](argv[2:]) or 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
