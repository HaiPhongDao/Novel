"""Sổ lỗi: quan sát -> can thiệp -> phán quyết, có đếm và có đo.

Vì sao có file này: review và sổ kinh nghiệm cũ ghi *đã học được gì*, nhưng không ghi
*đã thử gì, hiệu quả bao nhiêu, cái nào vô dụng*. Không có số thì không thể nói một lần
sửa SI/prompt có tác dụng, và mọi luật mới chỉ là một phỏng đoán đứng cạnh luật cũ.

Ba bản ghi, ba câu hỏi khác nhau:
    loai-loi.jsonl  một kiểu lỗi có tồn tại và đếm được không  (danh mục, id ổn định)
    quan-sat.jsonl  lần này Writer mắc lỗi đó mấy chỗ          (đếm -> tần suất)
    can-thiep.jsonl đã sửa cái gì, ở tầng nào, hiệu quả ra sao (đo -> phán quyết)
    muc-tieu.jsonl  đích của từng chỉ số là bao nhiêu, do ai đặt (mẫu / Tác giả / nội bộ)

Hiệu quả đo bằng "số lần biên độ nhiễu" (|trước - sau| / biên độ), không bằng cảm nhận:
cùng một SI đã cho ra cả 0 và 5 cặp phủ định ở hai lần chạy, nên một lần sạch hơn chưa
phải là nhân quả. Dưới 1 biên độ là vô hiệu, kể cả khi nhìn thấy đẹp hơn.

Dùng:
    python tools/so_loi.py bao-cao                 # in bảng tổng hợp + ghi chung/loi/bao-cao.md
    python tools/so_loi.py kiem-tra                # soát toàn vẹn dữ liệu, liệt kê lỗ hổng
    python tools/so_loi.py quan-sat --loi E-PROSE-01 --truyen lanh-chua-chip --doan 001 --so-lan 4
    python tools/so_loi.py can-thiep --loi E-PROSE-01 --tang SI --mo-ta "..." --chi-so phu-dinh-lap-cau \
        --truoc 7.3 --sau 3.8 --bien-do 0.8 --n 2
    python tools/so_loi.py phan-quyet --id I-0003 --sau 3.8 --n 2
    python tools/so_loi.py muc-tieu --truyen manga-tokyo-2000 --chi-so nhan-ngu-dieu --nguon mau --gia-tri 0.03
    python tools/so_loi.py quet <ban.md> [...]     # đo bản nháp và so với đích đã đặt

Không cần thư viện ngoài. Ghi UTF-8 không BOM, mỗi sự kiện một dòng, chỉ thêm (append).
"""
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
SO = ROOT / "chung" / "loi"

LOAI = SO / "loai-loi.jsonl"
QUAN_SAT = SO / "quan-sat.jsonl"
CAN_THIEP = SO / "can-thiep.jsonl"
MUC_TIEU = SO / "muc-tieu.jsonl"
BAO_CAO = SO / "bao-cao.md"

MIEN = ("BRIEF", "SI", "CANON", "PROSE", "SCENE", "EDGE", "GATE")
TANG = ("BRIEF", "SI", "GLOSSARY", "BIBLE", "REVIEW", "TOOL")
# Nhóm phán quyết:
#   de-xuat / dang-thu           chưa có kết luận
#   hieu-qua / vo-hieu / chua-ro phán quyết BẰNG SỐ (cần trước/sau/biên độ/n)
#   phan-tac-dung                số đi ngược chiều tốt, hoặc làm tật khác mọc lên
#   tac-gia-bac                  Tác giả đọc và bác — bằng chứng hợp lệ, không cần số,
#                                nhưng phải ghi nguyên văn câu bác để không thành truyền miệng
KET_LUAN = ("de-xuat", "dang-thu", "hieu-qua", "vo-hieu", "phan-tac-dung", "tac-gia-bac", "chua-ro")
CAN_SO = ("hieu-qua", "vo-hieu")                      # cần n>=2 và có biên độ
CAN_BAND = ("hieu-qua", "vo-hieu", "phan-tac-dung")   # cần số trước/sau/biên độ
NGUON_DICH = ("mau", "tac-gia", "noi-bo")

# Ngưỡng phán quyết, tính theo biên độ nhiễu. Một lần sửa phải vượt biên độ mới được coi
# là có tác dụng; đây là con số bảo vệ khỏi việc nhận công cho một lần rút thăm may.
NGUONG_HIEU_QUA = 2.0
NGUONG_VO_HIEU = 1.0

NHAN = {
    "de-xuat": "đề xuất", "dang-thu": "đang thử", "hieu-qua": "hiệu quả",
    "vo-hieu": "vô hiệu", "phan-tac-dung": "phản tác dụng",
    "tac-gia-bac": "Tác giả bác", "chua-ro": "chưa rõ",
}


# ---------------------------------------------------------------- đọc/ghi

def doc(path: Path) -> list[dict]:
    if not path.exists():
        return []
    out = []
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError as e:
            sys.exit(f"LỖI {path.name} dòng {i}: JSON hỏng ({e})")
    return out


def them(path: Path, rec: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def ghi_lai(path: Path, recs: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def ma_tiep(recs: list[dict], tien_to: str, rong: int = 4) -> str:
    n = 0
    for r in recs:
        idd = str(r.get("id", ""))
        if idd.startswith(tien_to):
            try:
                n = max(n, int(idd[len(tien_to):]))
            except ValueError:
                pass
    return f"{tien_to}{n + 1:0{rong}d}"


# ---------------------------------------------------------------- phán quyết

def quy_doi_hieu_qua(truoc=None, sau=None, bien_do=None) -> tuple[float | None, str | None]:
    """Trả (số lần biên độ, kết luận gợi ý). Thiếu số thì trả (None, None)."""
    if truoc is None or sau is None or not bien_do:
        return None, None
    delta = abs(float(truoc) - float(sau))
    so_bien_do = delta / float(bien_do)
    if so_bien_do >= NGUONG_HIEU_QUA:
        return round(so_bien_do, 2), "hieu-qua"
    if so_bien_do < NGUONG_VO_HIEU:
        return round(so_bien_do, 2), "vo-hieu"
    return round(so_bien_do, 2), "chua-ro"


def co_tac_dung(c: dict) -> str:
    """Có tác dụng theo chiều tốt, hay chỉ là thay đổi trong nhiễu."""
    so = c.get("so_bien_do")
    if so is None:
        return c.get("ket_luan", "chua-ro")
    if c.get("ket_luan") == "phan-tac-dung":
        return "phan-tac-dung"
    if so < NGUONG_VO_HIEU:
        return "vo-hieu"
    if so >= NGUONG_HIEU_QUA:
        return "hieu-qua"
    return "chua-ro"


# ---------------------------------------------------------------- lệnh

def cmd_quan_sat(argv):
    ap = _ap("quan-sat", "Ghi một lần Writer mắc lỗi")
    ap.add_argument("--loi", required=True)
    ap.add_argument("--truyen", required=True)
    ap.add_argument("--doan", default="")
    ap.add_argument("--ban", default="")
    ap.add_argument("--so-lan", type=int, default=1)
    ap.add_argument("--don-vi", default="cho")
    ap.add_argument("--do-bang", default="doc")
    ap.add_argument("--nguon", default="")
    ap.add_argument("--ghi-chu", default="")
    a = ap.parse_args(argv)
    loai = {r["id"] for r in doc(LOAI)}
    if a.loi not in loai:
        sys.exit(f"LỖI: chưa có kiểu lỗi {a.loi}. Chạy `them-loi` trước, hoặc `kiem-tra` để xem danh mục.")
    recs = doc(QUAN_SAT)
    rec = {
        "id": ma_tiep(recs, "Q-"),
        "loi": a.loi, "truyen": a.truyen, "doan": a.doan, "ban": a.ban,
        "ngay": date.today().isoformat(), "so_lan": a.so_lan, "don_vi": a.don_vi,
        "do_bang": a.do_bang, "nguon": a.nguon, "ghi_chu": a.ghi_chu,
    }
    them(QUAN_SAT, rec)
    print(f"đã ghi {rec['id']}: {a.loi} × {a.so_lan} {a.don_vi} ({a.truyen} {a.doan or '-'})")


def cmd_can_thiep(argv):
    ap = _ap("can-thiep", "Ghi một lần sửa, kèm số trước/sau")
    ap.add_argument("--loi", required=True)
    ap.add_argument("--tang", required=True, choices=TANG)
    ap.add_argument("--mo-ta", required=True)
    ap.add_argument("--file", default="")
    ap.add_argument("--chi-so", default="")
    ap.add_argument("--truoc", type=float)
    ap.add_argument("--sau", type=float)
    ap.add_argument("--bien-do", type=float)
    ap.add_argument("--n", type=int, default=1)
    ap.add_argument("--ket-luan", choices=KET_LUAN, default="")
    ap.add_argument("--nguon", default="")
    ap.add_argument("--truyen", default="")
    a = ap.parse_args(argv)
    loai = {r["id"] for r in doc(LOAI)}
    if a.loi not in loai:
        sys.exit(f"LỖI: chưa có kiểu lỗi {a.loi}.")
    so, goi_y = quy_doi_hieu_qua(a.truoc, a.sau, a.bien_do)
    ket_luan = a.ket_luan or goi_y or ("dang-thu" if a.n < 2 else "chua-ro")
    recs = doc(CAN_THIEP)
    rec = {
        "id": ma_tiep(recs, "I-"),
        "loi": a.loi, "tang": a.tang, "mo_ta": a.mo_ta, "file": a.file,
        "chi_so": a.chi_so, "truoc": a.truoc, "sau": a.sau, "bien_do": a.bien_do,
        "so_bien_do": so, "n": a.n, "ket_luan": ket_luan,
        "ngay": date.today().isoformat(), "truyen": a.truyen, "nguon": a.nguon,
    }
    them(CAN_THIEP, rec)
    print(f"đã ghi {rec['id']}: {rec['tang']} cho {a.loi} -> {ket_luan}"
          + (f" ({so} biên độ)" if so is not None else " (chưa có số)"))
    if rec["n"] < 2:
        print("  nhắc: n<2 nên chưa đủ bằng chứng; ghi 'chua-ro', đừng nâng thành luật.")


def cmd_phan_quyet(argv):
    ap = _ap("phan-quyet", "Điền số sau cho một can thiệp đã ghi")
    ap.add_argument("--id", required=True)
    ap.add_argument("--sau", type=float, required=True)
    ap.add_argument("--n", type=int)
    ap.add_argument("--bien-do", type=float)
    ap.add_argument("--ket-luan", choices=KET_LUAN)
    a = ap.parse_args(argv)
    recs = doc(CAN_THIEP)
    for r in recs:
        if r.get("id") == a.id:
            r["sau"] = a.sau
            if a.n is not None:
                r["n"] = a.n
            if a.bien_do is not None:
                r["bien_do"] = a.bien_do
            so, goi_y = quy_doi_hieu_qua(r.get("truoc"), r["sau"], r.get("bien_do"))
            r["so_bien_do"] = so
            r["ket_luan"] = a.ket_luan or goi_y or "chua-ro"
            ghi_lai(CAN_THIEP, recs)
            print(f"{a.id}: sau={a.sau} n={r['n']} -> {r['ket_luan']}"
                  + (f" ({so} biên độ)" if so is not None else ""))
            return
    sys.exit(f"LỖI: không thấy can thiệp {a.id}")


def cmd_muc_tieu(argv):
    ap = _ap("muc-tieu", "Đặt đích cho một chỉ số của một truyện")
    ap.add_argument("--truyen", required=True)
    ap.add_argument("--chi-so", required=True)
    ap.add_argument("--nguon", required=True, choices=NGUON_DICH)
    ap.add_argument("--gia-tri", type=float, required=True)
    ap.add_argument("--bien-do", type=float)
    ap.add_argument("--don-vi", default="lần/1.000 chữ")
    ap.add_argument("--ghi-chu", default="")
    a = ap.parse_args(argv)
    recs = doc(MUC_TIEU)
    rec = {
        "truyen": a.truyen, "chi_so": a.chi_so, "nguon": a.nguon,
        "gia_tri": a.gia_tri, "bien_do": a.bien_do, "don_vi": a.don_vi,
        "ngay": date.today().isoformat(), "ghi_chu": a.ghi_chu,
    }
    recs = [r for r in recs if not (r["truyen"] == a.truyen and r["chi_so"] == a.chi_so)]
    recs.append(rec)
    ghi_lai(MUC_TIEU, recs)
    print(f"đích {a.truyen}/{a.chi_so} = {a.gia_tri} ({a.nguon})")


def cmd_them_loi(argv):
    ap = _ap("them-loi", "Đăng ký một kiểu lỗi mới")
    ap.add_argument("--id", required=True)
    ap.add_argument("--ten", required=True)
    ap.add_argument("--mien", required=True, choices=MIEN)
    ap.add_argument("--mo-ta", required=True)
    ap.add_argument("--do", default="doc")
    ap.add_argument("--trang-thai", default="dang-theo",
                    choices=("dang-theo", "nghi-ngo", "da-bo"))
    a = ap.parse_args(argv)
    if {r["id"] for r in doc(LOAI)} & {a.id}:
        sys.exit(f"LỖI: {a.id} đã có")
    them(LOAI, {"id": a.id, "ten": a.ten, "mien": a.mien, "mo_ta": a.mo_ta,
                "do": a.do, "trang_thai": a.trang_thai, "ngay": date.today().isoformat()})
    print(f"đã đăng ký {a.id} — {a.ten}")


def cmd_quet(argv):
    """Đo một bản nháp và so với đích đã đặt. Đây là cổng dùng được ngay trong review."""
    a = _ap("quet", "Đo bản nháp theo đích từng truyện").parse_args(argv)
    if not a.files:
        sys.exit("LỖI: cần ít nhất một file")
    sys.path.insert(0, str(ROOT / "tools"))
    from soat_van import scan
    dich = {(r["truyen"], r["chi_so"]): r for r in doc(MUC_TIEU)}
    for f in a.files:
        r = scan(f)
        han = r["han"] or 1
        print(f"== {f}  ({r['han']} chữ Hán)")
        for chi_so in ("phu-dinh-lap-cau", "so-sanh-loi-ke", "khuon-shi",
                       "nhan-ngu-dieu", "the-thoai", "luot-cut"):
            dens = round(r[chi_so] / han * 1000, 2)
            print(f"   {chi_so:<20}{r[chi_so]:>4} chỗ   {dens:>6.2f}/1.000   ", end="")
            if a.truyen and (a.truyen, chi_so) in dich:
                d = dich[(a.truyen, chi_so)]
                bd = d.get("bien_do") or max(0.05, d["gia_tri"] * 0.5)
                lech = (dens - d["gia_tri"]) / bd
                co = "TRÊN ĐÍCH" if lech > 1 else ("dưới đích" if lech < -1 else "trong đích")
                print(f"đích {d['gia_tri']} ({d['nguon']})  lệch {lech:+.1f} nhiễu -> {co}")
            else:
                print("(chưa đặt đích)")
        print(f"   tb-chu-luot={r['tb-chu-luot']}  luot-thoai={r['luot-thoai']}  ti-le-thoai={r['ti-le-thoai']}%")


def cmd_kiem_tra(argv):
    _ap("kiem-tra", "Soát toàn vẹn sổ").parse_args(argv)
    loai = doc(LOAI)
    qs = doc(QUAN_SAT)
    ct = doc(CAN_THIEP)
    mt = doc(MUC_TIEU)
    loi_ids = {r["id"] for r in loai}
    van_de = []
    if len(loi_ids) != len(loai):
        van_de.append("loai-loi.jsonl có id trùng")
    q_ids = [r.get("id") for r in qs]
    c_ids = [r.get("id") for r in ct]
    if len(set(q_ids)) != len(q_ids):
        van_de.append("quan-sat.jsonl có id trùng")
    if len(set(c_ids)) != len(c_ids):
        van_de.append("can-thiep.jsonl có id trùng")
    for r in qs:
        if r.get("loi") not in loi_ids:
            van_de.append(f"{r.get('id')}: trỏ tới kiểu lỗi lạ {r.get('loi')}")
    for r in ct:
        if r.get("loi") not in loi_ids:
            van_de.append(f"{r.get('id')}: trỏ tới kiểu lỗi lạ {r.get('loi')}")
    for r in ct:
        if r.get("ket_luan") in CAN_SO and r.get("n", 0) < 2:
            van_de.append(f"{r.get('id')}: kết luận '{r['ket_luan']}' với n={r.get('n')} < 2")
        if r.get("ket_luan") in CAN_BAND and r.get("so_bien_do") is None:
            van_de.append(f"{r.get('id')}: kết luận '{r['ket_luan']}' nhưng thiếu trước/sau/biên độ")
        if r.get("ket_luan") == "tac-gia-bac" and not r.get("nguon"):
            van_de.append(f"{r.get('id')}: bị Tác giả bác nhưng không ghi nguồn câu bác")

    print(f"kiểu lỗi: {len(loai)}   quan sát: {len(qs)}   can thiệp: {len(ct)}   đích: {len(mt)}")
    if van_de:
        print(f"\n{len(van_de)} vấn đề:")
        for v in van_de:
            print("  - " + v)
    else:
        print("\nkhông thấy vấn đề toàn vẹn.")

    # Lỗ hổng nội dung: cái gì chưa được đo
    chua_do = [r["id"] for r in ct if r.get("so_bien_do") is None]
    khong_qs = [r["id"] for r in loai if not any(q["loi"] == r["id"] for q in qs)]
    that_bai = [r["id"] for r in ct if r.get("ket_luan") in ("vo-hieu", "phan-tac-dung")]
    if chua_do:
        print(f"\ncan thiệp chưa có số (không được coi là đã chứng minh): {', '.join(chua_do)}")
    if khong_qs:
        print(f"\nkiểu lỗi chưa từng có quan sát nào: {', '.join(khong_qs)}")
    if that_bai:
        print(f"\ncan thiệp thất bại (phải gỡ hoặc không được nâng thành luật): {', '.join(that_bai)}")
    return 1 if van_de else 0


def cmd_bao_cao(argv):
    _ap("bao-cao", "Sinh bảng tổng hợp").parse_args(argv)
    loai = doc(LOAI)
    qs = doc(QUAN_SAT)
    ct = doc(CAN_THIEP)
    mt = doc(MUC_TIEU)

    theo_loi: dict[str, list[dict]] = {}
    for c in ct:
        theo_loi.setdefault(c["loi"], []).append(c)

    dem = {r["id"]: sum(q.get("so_lan", 1) for q in qs if q["loi"] == r["id"]) for r in loai}
    lan = {r["id"]: sum(1 for q in qs if q["loi"] == r["id"]) for r in loai}

    L = []
    L.append("# Sổ lỗi — bảng sinh tự động\n")
    L.append("Sinh bằng `python tools/so_loi.py bao-cao`. Đừng sửa tay; sửa file `.jsonl` rồi sinh lại.\n")
    L.append(f"- Kiểu lỗi: **{len(loai)}** · Lần quan sát: **{len(qs)}** · Can thiệp: **{len(ct)}** · Đích đã đặt: **{len(mt)}**\n")

    da_do = [c for c in ct if c.get("so_bien_do") is not None]
    hieu = [c for c in da_do if co_tac_dung(c) == "hieu-qua"]
    vo = [c for c in da_do if co_tac_dung(c) == "vo-hieu"]
    tac = [c for c in da_do if co_tac_dung(c) == "phan-tac-dung"]
    bac = [c for c in ct if c.get("ket_luan") == "tac-gia-bac"]
    chua = [c for c in ct if c.get("so_bien_do") is None and c.get("ket_luan") not in ("tac-gia-bac",)]
    L.append("## Tỉ lệ có bằng chứng\n")
    L.append(f"- Can thiệp đã đo: **{len(da_do)}/{len(ct)}**"
             + (f" ({round(100*len(da_do)/len(ct))}%)" if ct else "") + "\n")
    L.append(f"- Hiệu quả (≥{NGUONG_HIEU_QUA} biên độ): **{len(hieu)}** · "
             f"Vô hiệu (<{NGUONG_VO_HIEU} biên độ): **{len(vo)}** · "
             f"Phản tác dụng: **{len(tac)}** · Bị Tác giả bác: **{len(bac)}** · Chưa đo: **{len(chua)}**\n")

    L.append("\n## Kiểu lỗi, số lần, và cái gì đã được thử\n")
    L.append("| Mã | Kiểu lỗi | Số chỗ | Số đợt | Can thiệp (tầng · kết luận · biên độ) |")
    L.append("|---|---|---|---|---|")
    co_qs = [r for r in loai if lan.get(r["id"], 0) > 0]
    khong_qs = [r for r in loai if lan.get(r["id"], 0) == 0]
    for r in sorted(co_qs, key=lambda x: (-dem.get(x["id"], 0), x["id"])):
        cs = theo_loi.get(r["id"], [])
        if cs:
            mo = "<br>".join(
                f"{c['id']} · {c['tang']} · {NHAN.get(co_tac_dung(c), co_tac_dung(c))}"
                + (f" · {c['so_bien_do']}×" if c.get("so_bien_do") is not None else " · chưa đo")
                for c in cs)
        else:
            mo = "—"
        L.append(f"| {r['id']} | {r['ten']} | {dem.get(r['id'], 0)} | {lan.get(r['id'], 0)} | {mo} |")
    if khong_qs:
        L.append(f"\n### Chưa từng có quan sát ({len(khong_qs)} kiểu)\n")
        L.append("Kiểu lỗi đã đăng ký nhưng chưa có lần nào được ghi. Hoặc chưa gặp, hoặc gặp mà không ghi — "
                 "cả hai đều là lỗ hổng của sổ, không phải bằng chứng là đã hết lỗi.\n")
        L.append(" · ".join(f"`{r['id']}` {r['ten']}" for r in sorted(khong_qs, key=lambda x: x["id"])))

    if that_bai := (vo + tac):
        L.append("\n## Giải pháp vô hiệu hoặc phản tác dụng — phải gỡ, không được nâng thành luật\n")
        L.append("| Can thiệp | Lỗi | Tầng | Trước → Sau | Biên độ | Kết luận |")
        L.append("|---|---|---|---|---|---|")
        for c in that_bai:
            L.append(f"| {c['id']} | {c['loi']} | {c['tang']} | {c.get('truoc')} → {c.get('sau')} "
                     f"| {c.get('bien_do')} | {co_tac_dung(c)} |")

    if bac:
        L.append("\n## Giải pháp đã bị Tác giả bác (không gỡ thì sẽ được thêm lại)\n")
        L.append("| Can thiệp | Lỗi | Tầng | Mô tả | Nguồn |")
        L.append("|---|---|---|---|---|")
        for c in bac:
            L.append(f"| {c['id']} | {c['loi']} | {c['tang']} | {c.get('mo_ta','')} | {c.get('nguon','')} |")

    if hieu:
        L.append("\n## Giải pháp đã chứng minh — được phép thành luật trong SKILL\n")
        L.append("| Can thiệp | Lỗi | Tầng | Trước → Sau | Biên độ | Hiệu quả | n |")
        L.append("|---|---|---|---|---|---|---|")
        for c in sorted(hieu, key=lambda x: -(x.get("so_bien_do") or 0)):
            L.append(f"| {c['id']} | {c['loi']} | {c['tang']} | {c.get('truoc')} → {c.get('sau')} "
                     f"| {c.get('bien_do')} | {c['so_bien_do']}× | {c.get('n')} |")

    if mt:
        L.append("\n## Đích của từng chỉ số (nguồn: mẫu / Tác giả / nội bộ)\n")
        L.append("| Truyện | Chỉ số | Đích | Nguồn |")
        L.append("|---|---|---|---|")
        for r in mt:
            L.append(f"| {r['truyen']} | {r['chi_so']} | {r['gia_tri']} {r.get('don_vi','')} | {r['nguon']} |")

    vanban = "\n".join(L) + "\n"
    BAO_CAO.parent.mkdir(parents=True, exist_ok=True)
    BAO_CAO.write_text(vanban, encoding="utf-8", newline="\n")
    print(vanban)
    print(f"\nđã ghi {BAO_CAO.relative_to(ROOT)}")


def _ap(ten, mo_ta):
    import argparse
    p = argparse.ArgumentParser(prog=f"so_loi.py {ten}", description=mo_ta)
    if ten == "quet":
        p.add_argument("files", nargs="+")
        p.add_argument("--truyen", default="")
    return p


LENH = {
    "them-loi": cmd_them_loi,
    "quan-sat": cmd_quan_sat,
    "can-thiep": cmd_can_thiep,
    "phan-quyet": cmd_phan_quyet,
    "muc-tieu": cmd_muc_tieu,
    "quet": cmd_quet,
    "kiem-tra": cmd_kiem_tra,
    "bao-cao": cmd_bao_cao,
}


def main(argv):
    if len(argv) < 2 or argv[1] in ("-h", "--help"):
        print(__doc__)
        return 0 if len(argv) < 2 else 2
    ten = argv[1]
    if ten not in LENH:
        sys.exit(f"LỖI: không có lệnh '{ten}'. Có: {', '.join(LENH)}")
    return LENH[ten](argv[2:]) or 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
