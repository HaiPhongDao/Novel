"""Chấm một đoạn theo ngưỡng lấy từ bản Tác giả đã khen (B) + canon.

Dùng: python tools/cham_doan.py <file.md> [--json]
Ngưỡng:
  chữ 1500-1800 | chữ/câu 22-30 | số câu >=45 | lượt thoại 14-22 | chữ/lượt 20-30
  phủ định <=2 | 实 0 | nhãn ngữ điệu 0 | so sánh người kể 0 | canon đủ
"""
import re, sys, json, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import soat_van as sv

CANON = {
    "回大人": (3, None),
    "小的": (2, None),
    "会长": (1, None),
    "老男爵": (0, None),
    "老老爷": (0, None),
    "老奴": (0, 0), "奴才": (0, 0), "属下": (0, 0), "末将": (0, 0), "陛下": (0, 0), "殿下": (0, 0),
}
NUMBERS = ["六十一", "四十", "九枚", "三百一十二", "五十六", "一百"]


def han(s):
    return sum(1 for c in s if "\u4e00" <= c <= "\u9fff")


def load(path):
    t = open(path, encoding="utf-8").read()
    return re.sub(r"^<!--.*?-->\s*", "", t, flags=re.S)


def measure(path):
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
    d["so_lieu_thieu"] = [n for n in NUMBERS if n not in t]
    d["moc"] = re.findall(r"[一二三四五六七八九十百]+天|[0-9]+天", t)
    d["hook"] = len(re.findall(r"但这还不是|然而，|更要命的是", t))
    return d


def score(d):
    parts = []

    def band(name, ok, weight, group):
        parts.append((name, ok, weight, group))
        return weight if ok else 0

    s = 0
    s += band("chữ 1500-1800", 1500 <= d["han"] <= 1800, 12, "nhịp")
    s += band("chữ/câu 22-30", 22 <= d["chu_cau"] <= 30, 18, "nhịp")
    s += band("số câu >=45", d["cau"] >= 45, 10, "nhịp")
    s += band("lượt thoại 14-22", 14 <= d["luot"] <= 22, 8, "nhịp")
    s += band("chữ/lượt 20-30", 20 <= d["chu_luot"] <= 30, 8, "nhịp")
    s += band("phủ định <=2", d["phu_dinh"] <= 2, 10, "văn")
    s += band("实 = 0", d["shi"] == 0, 6, "văn")
    s += band("nhãn ngữ điệu = 0", d["nhan"] == 0, 6, "văn")
    s += band("so sánh người kể = 0", d["so_sanh"] == 0, 6, "văn")
    s += band("không câu móc rẻ", d["hook"] == 0, 6, "văn")
    c = d["canon"]
    canon_ok = (
        c["回大人"] >= 3 and c["小的"] >= 2 and c["会长"] >= 1
        and c["老奴"] == 0 and c["奴才"] == 0 and c["属下"] == 0
        and c["末将"] == 0 and c["陛下"] == 0 and c["殿下"] == 0
        and not d["so_lieu_thieu"]
    )
    s += band("canon + số liệu", canon_ok, 10, "canon")
    return s, parts


def report(path):
    d = measure(path)
    s, parts = score(d)
    g = {}
    for n, ok, w, grp in parts:
        g.setdefault(grp, [0, 0])
        g[grp][1] += w
        if ok:
            g[grp][0] += w
    print(f"{os.path.basename(path)}  →  {s}/100   nhịp {g['nhịp'][0]}/{g['nhịp'][1]} · văn {g['văn'][0]}/{g['văn'][1]} · canon {g['canon'][0]}/{g['canon'][1]}")
    print(f"  chữ {d['han']} · câu {d['cau']} · chữ/câu {d['chu_cau']} · lượt {d['luot']} · chữ/lượt {d['chu_luot']}")
    print(f"  phủ định {d['phu_dinh']} · 实 {d['shi']} · nhãn {d['nhan']} · so sánh {d['so_sanh']} · thẻ {d['the']}")
    print(f"  canon {d['canon']} · thiếu số {d['so_lieu_thieu']} · mốc ngày {d['moc']}")
    miss = [n for n, ok, w, grp in parts if not ok]
    if miss:
        print("  chưa đạt: " + ", ".join(miss))
    return s, d


if __name__ == "__main__":
    for p in sys.argv[1:]:
        if p == "--json":
            continue
        report(p)
        print()
