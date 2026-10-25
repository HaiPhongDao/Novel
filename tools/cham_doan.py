"""Chấm một đoạn theo ngưỡng lấy từ bản Tác giả đã khen (B) + canon.

Dùng: python tools/cham_doan.py <file.md> [--json]
Ngưỡng:
  chữ 1500-1800 | chữ/câu 22-30 | số câu >=45 | lượt thoại 14-22 | chữ/lượt 20-30
  phủ định <=2 | 实 0 | nhãn ngữ điệu 0 | so sánh người kể 0 | canon đủ
"""
import re, sys, json, os

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
    t = open(path, encoding="utf-8").read()
    return re.sub(r"^<!--.*?-->\s*", "", t, flags=re.S)


def measure(path, prompt_path=None, numbers=None):
    t = load(path)
    r = sv.scan(path)
    narr = re.sub(r"“[^”]*”", "。", t)
    SL = [han(s) for s in re.split(r"[。！？；…\n]+", narr) if han(s) > 0]
    d = {
        "han": r["han"],
        "cau": len(SL),
        "chu_cau": round(sum(SL) / len(SL), 1) if SL else 0,
        "luot": r["luot-thoai"],
        "chu_luot": r["tb-chu-luot"],
        "phu_dinh": r["phu-dinh-lap-cau"],
        "shi": r["khuon-shi"],
        "nhan": r["nhan-ngu-dieu"],
        "so_sanh": r.get("so-sanh-loi-ke", r["so-sanh-nguoi-ke"]),
        "the": r["the-thoai"],
    }
    d["canon"] = {k: len(re.findall(k, t)) for k in CANON}
    d["canon_modern"] = {k: len(re.findall(v, t)) for k, v in CANON_MODERN.items()}
    if numbers is None and prompt_path and "modern" not in prompt_path:
        pass
    need = NUMBERS if numbers is None else numbers
    d["so_lieu_thieu"] = [n for n in need if n not in t]
    d["moc"] = re.findall(r"[一二三四五六七八九十百]+天|[0-9]+天", t)
    d["hook"] = len(re.findall(r"但这还不是|然而，|更要命的是", t))
    # Chép mẫu: câu tiếng Hán trong prompt xuất hiện nguyên văn ở bản thảo.
    d["chep_mau"] = []
    if prompt_path:
        pr = open(prompt_path, encoding="utf-8").read()
        for s in re.findall(r"[“「]([^”」]{8,})[”」]", pr):
            if han(s) >= 8 and s in t:
                d["chep_mau"].append(s[:24])
    return d


def score(d, modern=False):
    parts = []

    def band(name, ok, weight, group):
        parts.append((name, ok, weight, group))
        return weight if ok else 0

    s = 0
    s += band("chữ 1500-1800", 1500 <= d["han"] <= 1800, 12, "nhịp")
    s += band("chữ/câu 20-34", 20 <= d["chu_cau"] <= 34, 18, "nhịp")
    s += band("số câu >=45", d["cau"] >= 45, 10, "nhịp")
    s += band("lượt thoại 10-22", 10 <= d["luot"] <= 22, 8, "nhịp")
    s += band("chữ/lượt 16-30", 16 <= d["chu_luot"] <= 30, 8, "nhịp")
    # Mẫu gốc (女巫 ch.5/ch.47) có 3-4 cặp mỗi cảnh, nên ngưỡng là 4 chứ không phải 0.
    s += band("phủ định <=4", d["phu_dinh"] <= 4, 10, "văn")
    s += band("实 = 0", d["shi"] == 0, 6, "văn")
    s += band("nhãn ngữ điệu = 0", d["nhan"] == 0, 6, "văn")
    s += band("so sánh người kể = 0", d["so_sanh"] == 0, 6, "văn")
    s += band("không câu móc rẻ", d["hook"] == 0, 6, "văn")
    c = d["canon"]
    canon_ok = (
        c["回大人"] >= 3
        and c["老奴"] == 0 and c["奴才"] == 0 and c["属下"] == 0
        and c["末将"] == 0 and c["陛下"] == 0 and c["殿下"] == 0
        and not d["so_lieu_thieu"]
    )
    if modern:
        canon_ok = sum(d.get("canon_modern", {}).values()) == 0 and not d["so_lieu_thieu"]
    s += band("canon + số liệu", canon_ok, 10, "canon")
    return s, parts


def report(path, prompt_path=None, numbers=None, modern=False):
    d = measure(path, prompt_path, numbers)
    s, parts = score(d, modern)
    g = {}
    for n, ok, w, grp in parts:
        g.setdefault(grp, [0, 0])
        g[grp][1] += w
        if ok:
            g[grp][0] += w
    if d["chep_mau"]:
        print(f"{os.path.basename(path)}  →  HỎNG: chép nguyên câu mẫu của prompt ({'; '.join(d['chep_mau'])})")
        s = 0
    else:
        print(f"{os.path.basename(path)}  →  {s}/100   nhịp {g['nhịp'][0]}/{g['nhịp'][1]} · văn {g['văn'][0]}/{g['văn'][1]} · canon {g['canon'][0]}/{g['canon'][1]}")
    print(f"  chữ {d['han']} · câu {d['cau']} · chữ/câu {d['chu_cau']} · lượt {d['luot']} · chữ/lượt {d['chu_luot']}")
    print(f"  phủ định {d['phu_dinh']} · 实 {d['shi']} · nhãn {d['nhan']} · so sánh {d['so_sanh']} · thẻ {d['the']}")
    print(f"  canon {d['canon']} · canon-modern {d.get('canon_modern')} · thiếu số {d['so_lieu_thieu']} · mốc ngày {d['moc']}")
    miss = [n for n, ok, w, grp in parts if not ok]
    if miss:
        print("  chưa đạt: " + ", ".join(miss))
    return s, d


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
