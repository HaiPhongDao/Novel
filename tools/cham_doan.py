"""Chấm một đoạn theo ngưỡng lấy từ bản Tác giả đã khen (B) + canon.

Dùng: python tools/cham_doan.py <file.md> [--json]
Ngưỡng:
  chữ 1500-1800 | chữ/câu 22-30 | số câu >=45 | lượt thoại 14-22 | chữ/lượt 20-30
  phủ định <=2 | 实 0 | nhãn ngữ điệu 0 | so sánh người kể 0 | canon đủ
"""
import re, sys, json, os

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import soat_van as sv

# Từ phong kiến bị cấm trong truyện hiện đại. "小的" chỉ tính khi là tự xưng, không tính "窄小的…".
CANON_MODERN = {
    "大人": r"大人", "老爷": r"老爷", "少爷": r"少爷", "属下": r"属下",
    "奴才": r"奴才", "老奴": r"老奴", "陛下": r"陛下", "殿下": r"殿下",
    "小的": r"(?<![窄细瘦矮短小])小的(?=[，。！？、”\s]|$)",
}
CANON = {
    "回大人": (3, None),
    "小的": (2, None),
    "会长": (1, None),
    "老男爵": (0, None),
    "老老爷": (0, None),
    "老奴": (0, 0), "奴才": (0, 0), "属下": (0, 0), "末将": (0, 0), "陛下": (0, 0), "殿下": (0, 0),
}
# Số liệu bắt buộc: truyền vào bằng --numbers "六十一,四十,九枚" (mỗi đoạn một khác).
NUMBERS = []


def han(s):
    return sum(1 for c in s if "\u4e00" <= c <= "\u9fff")


def load(path):
    t = open(path, encoding="utf-8", errors="replace").read()
    return re.sub(r"^<!--.*?-->\s*", "", t, flags=re.S)


def paragraphs(text):
    return [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]


def check(path, prompt_path=None, numbers=None, modern=False):
    t = load(path)
    paras = paragraphs(t)
    body = "\n".join(paras)
    v = sv.scan(path)
    h = v["han"]

    # Số câu = số dấu chấm, hỏi, than trong lời kể
    sentences = re.split(r"[。！？\n]+", body)
    sentences = [s.strip() for s in sentences if han(s) > 0]
    n_sent = len(sentences)
    chu_cau = round(h / n_sent, 1) if n_sent else 0

    scores = {}
    # 1. Độ dài (cửa sổ brief ghi trong prompt_path, hoặc mặc định 1500-1800)
    lo, hi = 1500, 1800
    if prompt_path and os.path.exists(prompt_path):
        m = re.search(r"(\d[\d.,]{2,})\s*[–\-~—]\s*(\d[\d.,]{2,})\s*(字|chữ)", open(prompt_path, encoding="utf-8").read())
        if m:
            nums = lambda s: int(s.replace(".", "").replace(",", ""))
            lo, hi = nums(m.group(1)), nums(m.group(2))
    scores["chu"] = (h, lo <= h <= hi, f"{lo}-{hi}")

    # 2. Nhịp câu
    scores["chu_cau"] = (chu_cau, 22 <= chu_cau <= 30, "22-30")
    scores["so_cau"] = (n_sent, n_sent >= 45, ">=45")

    # 3. Thoại
    lt = v["luot-thoai"]
    tb_t = v["tb-chu-luot"]
    scores["luot_thoai"] = (lt, 14 <= lt <= 22, "14-22")
    scores["tb_chu_luot"] = (tb_t, 20 <= tb_t <= 30, "20-30")

    # 4. Văn phong (soat_van)
    scores["phu_dinh"] = (v["phu-dinh-lap-cau"], v["phu-dinh-lap-cau"] <= 2, "<=2")
    scores["khuon_shi"] = (v["khuon-shi"], v["khuon-shi"] == 0, "0")
    scores["nhan_ngu_dieu"] = (v["nhan-ngu-dieu"], v["nhan-ngu-dieu"] == 0, "0")
    scores["so_sanh_loi_ke"] = (v["so-sanh-loi-ke"], v["so-sanh-loi-ke"] == 0, "0")

    # 5. Canon xưng hô
    canon_spec = CANON_MODERN if modern else CANON
    canon_hits = {}
    for k, pat in canon_spec.items():
        if modern:
            m = len(re.findall(pat, body))
            canon_hits[k] = (m, m == 0)
        else:
            lo_c, hi_c = pat
            m = len(re.findall(k, body))
            ok_c = (lo_c is None or m >= lo_c) and (hi_c is None or m <= hi_c)
            canon_hits[k] = (m, ok_c)
    scores["canon"] = canon_hits

    # 6. Số liệu
    num_hits = {}
    for n in (numbers or NUMBERS):
        m = len(re.findall(re.escape(n), body))
        num_hits[n] = (m, m >= 1)
    scores["so_lieu"] = num_hits

    return scores


def report(path, prompt_path=None, numbers=None, modern=False):
    s = check(path, prompt_path, numbers, modern)
    name = os.path.basename(path)

    def icon(b): return "✓" if b else "✗"
    total, pass_ = 0, 0

    print(f"== {name}")
    print("Văn phong & nhịp:")
    for k in ["chu", "chu_cau", "so_cau", "luot_thoai", "tb_chu_luot", "phu_dinh", "khuon_shi", "nhan_ngu_dieu", "so_sanh_loi_ke"]:
        val, ok, expect = s[k]
        total += 1
        if ok: pass_ += 1
        print(f"  {icon(ok)} {k:16} = {val:<6} (chuẩn {expect})")

    print("Canon xưng hô:")
    for k, (cnt, ok) in s["canon"].items():
        total += 1
        if ok: pass_ += 1
        print(f"  {icon(ok)} {k:10} = {cnt}")

    if s["so_lieu"]:
        print("Số liệu bắt buộc:")
        for k, (cnt, ok) in s["so_lieu"].items():
            total += 1
            if ok: pass_ += 1
            print(f"  {icon(ok)} {k:10} = {cnt}")

    pct = round(100 * pass_ / total) if total else 0
    print(f"Tổng: {pass_}/{total} tiêu chí ({pct}%)")
    return pct >= 80


if __name__ == "__main__":
    args = sys.argv[1:]
    prompt_path, numbers, modern = None, None, False
    if "--modern" in args:
        modern = True
        args = [a for a in args if a != "--modern"]
    if "--prompt" in args:
        i = args.index("--prompt")
        prompt_path = args[i + 1]
        args = args[:i] + args[i + 2:]
    if "--numbers" in args:
        i = args.index("--numbers")
        numbers = [x.strip() for x in args[i + 1].split(",") if x.strip()]
        args = args[:i] + args[i + 2:]
    for p in args:
        if p == "--json":
            continue
        report(p, prompt_path, numbers, modern)
        print()
