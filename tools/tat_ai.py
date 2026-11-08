"""Tật "giọng AI" của Writer — tìm bằng so với bộ mẫu, rồi đếm trên từng bản.

Vì sao có file này: Tác giả đọc qua app DocTTS và bắt rất nhanh những cụm Writer lặp ở mọi bản
(实打实 · 语气平稳得很 · 浑浊的眼睛 · 直往鼻孔里钻 …) — bộ mẫu gần như không dùng. Cổng máy và soat_van.py
không có cột cho chúng. Tool này cho Agent thấy trước khi đưa bản cho Tác giả.

Hai lệnh:

  python tools/tat_ai.py quet --mau <file hoặc thư mục bộ mẫu> <bản Writer…> [--min-ban 8] [--gap 8] [--loai-chu <chữ>]
      In các cụm 2–4 chữ mà Writer dùng gấp ≥ --gap lần bộ mẫu và có ở ≥ --min-ban bản. Phần lớn là chữ nội dung của
      truyện (tên, đồ vật) — --loai-chu bỏ mọi cụm chứa một trong các chữ đó. Người đọc chọn cụm nào là tật.

  python tools/tat_ai.py dem --ds <danh sách> <bản Writer…> [--mau <bộ mẫu>] [--list]
      Đếm từng tật trong danh sách (mỗi dòng: nhóm<TAB>mẫu regex<TAB>ghi chú; dòng mẫu bắt đầu bằng 'LK:' chỉ đếm ở lời
      kể, ngoài “”). In số lần /1.000 字 theo nhóm cho mỗi bản; --mau in thêm mức của bộ mẫu; --list in từng chỗ kèm
      ngữ cảnh.

  python tools/tat_ai.py nguon --mau <bộ mẫu> --tu SI=<file SI> --tu prompt=<file prompt> [--tu glossary=…] <bản…>
      Mỗi cụm Writer dùng mà bộ mẫu hiếm/không có: nằm trong nguồn nào (SI, prompt, glossary…) hay "model tự đặt".
      Cụm đến từ SI/prompt thì sửa ở nguồn đó; cụm "model tự đặt" mới là việc của SI (anchor, cách nói) hay BANS.

Không phải trọng tài: số chỉ để biết bản nào nên chạy lại, câu ĐẠT vẫn do Tác giả.
Danh sách cấm từ trong SI đã bị Tác giả bác (I-0068, I-0071): dùng tool này để tìm nguồn, không để lập danh sách cấm.
"""
import argparse
import collections
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
HAN = re.compile(r"[一-鿿]")
QUOTE = re.compile(r"“[^”]*”")


def doc(p: Path) -> str:
    if p.is_dir():
        return "".join(x.read_text(encoding="utf-8") for x in sorted(p.glob("*.txt")))
    return re.sub(r"<!--.*?-->", "", p.read_text(encoding="utf-8"), flags=re.S)


def han(t: str) -> int:
    return len(HAN.findall(t)) or 1


def grams(t: str, n: int) -> collections.Counter:
    c = collections.Counter()
    for seg in re.findall(r"[一-鿿]+", t):
        for i in range(len(seg) - n + 1):
            c[seg[i:i + n]] += 1
    return c


def cmd_quet(a):
    mau = doc(Path(a.mau))
    W = [doc(Path(f)) for f in a.ban]
    Hm, Hw = han(mau), sum(han(w) for w in W)
    res = []
    for n in (2, 3, 4):
        gm = grams(mau, n)
        gw, df = collections.Counter(), collections.Counter()
        for w in W:
            g = grams(w, n)
            gw.update(g)
            df.update(set(g))
        for k, c in gw.items():
            if df[k] < a.min_ban or any(ch in a.loai_chu for ch in k):
                continue
            rw, rm = 1000 * c / Hw, 1000 * gm[k] / Hm
            if rw < 0.1:
                continue
            r = (rw + 0.003) / (rm + 0.003)
            if r >= a.gap:
                res.append((r, k, rm, rw, df[k]))
    res.sort(reverse=True)
    seen = []
    for r, k, rm, rw, d in res:
        if any(k in s or s in k for s, *_ in seen):
            continue
        seen.append((k, rm, rw, d))
    print(f"{len(W)} bản · bộ mẫu {Hm} 字 · Writer {Hw} 字 · {len(seen)} cụm (gấp ≥{a.gap}, ≥{a.min_ban} bản)")
    for k, rm, rw, d in seen[: a.top]:
        print(f"  {k:<6} mẫu {rm:5.2f} · Writer {rw:5.2f} /1000 · {d} bản")


def doc_ds(p: Path):
    out = []
    for line in p.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        nhom, pat = parts[0].strip(), parts[1].strip()
        lk = pat.startswith("LK:")
        out.append((nhom, re.compile(pat[3:] if lk else pat), lk))
    return out


def tim(t: str, pat, lk: bool):
    src = QUOTE.sub(lambda m: "　" * len(m.group(0)), t) if lk else t
    return [(m.start(), m.end()) for m in pat.finditer(src)]


def cmd_dem(a):
    ds = doc_ds(Path(a.ds))
    nhoms = list(dict.fromkeys(n for n, _, _ in ds))
    rows = []
    if a.mau:
        rows.append(("BỘ MẪU", doc(Path(a.mau))))
    rows += [(Path(f).name, doc(Path(f))) for f in a.ban]
    for ten, t in rows:
        H = han(t)
        by = collections.Counter()
        hits = []
        for nhom, pat, lk in ds:
            for s, e in tim(t, pat, lk):
                by[nhom] += 1
                hits.append((s, nhom, t[max(0, s - 8):e + 8].replace("\n", " ")))
        tong = sum(by.values())
        cols = " · ".join(f"{n} {1000 * by[n] / H:4.2f}" for n in nhoms)
        print(f"{ten:<20} {H:>6}字 · tổng {1000 * tong / H:5.2f} /1000 ({tong}) · {cols}")
        if a.list and ten != "BỘ MẪU":
            for s, nhom, ctx in sorted(hits):
                print(f"      [{nhom}] …{ctx}…")


def cmd_nguon(a):
    """Mỗi cụm lạ trong bản Writer (bộ mẫu hiếm hoặc không có) đến từ đâu: SI, prompt/brief, hay model tự đặt."""
    mau = doc(Path(a.mau))
    Hm = han(mau)
    nguon = {}
    for spec in a.tu:
        ten, _, p = spec.partition("=")
        nguon[ten] = doc(Path(p))
    W = [(Path(f).name, doc(Path(f))) for f in a.ban]
    gw, df = collections.Counter(), collections.Counter()
    for _, w in W:
        for n in (2, 3, 4):
            g = grams(w, n)
            gw.update(g)
            df.update(set(g))
    Hw = sum(han(w) for _, w in W)
    gm = collections.Counter()
    for n in (2, 3, 4):
        gm.update(grams(mau, n))
    hang = collections.defaultdict(list)
    seen = []
    for k, c in sorted(gw.items(), key=lambda x: -x[1]):
        if c < a.min_lan or df[k] < a.min_ban or any(ch in a.loai_chu for ch in k):
            continue
        rm = 1000 * gm[k] / Hm
        rw = 1000 * c / Hw
        if gm[k] > a.max_mau or rm * a.gap > rw:
            continue
        if any(k in s or s in k for s in seen):
            continue
        seen.append(k)
        o = [ten for ten, t in nguon.items() if k in t]
        hang[" + ".join(o) if o else "model tự đặt"].append(f"{k}({c}/{gm[k]})")
    print(f"{len(W)} bản · cụm Writer dùng ≥{a.min_lan} lần mà bộ mẫu dùng ≤{a.max_mau} lần · (số lần Writer / số lần bộ mẫu)")
    for o in sorted(hang, key=lambda x: (x == "model tự đặt", x)):
        print(f"## {o} — {len(hang[o])} cụm")
        print("  " + " · ".join(hang[o][: a.top]))


def main(argv):
    ap = argparse.ArgumentParser(prog="tat_ai.py")
    sub = ap.add_subparsers(dest="lenh", required=True)
    q = sub.add_parser("quet")
    q.add_argument("--mau", required=True)
    q.add_argument("ban", nargs="+")
    q.add_argument("--min-ban", type=int, default=8)
    q.add_argument("--gap", type=float, default=8)
    q.add_argument("--top", type=int, default=120)
    q.add_argument("--loai-chu", default="")
    d = sub.add_parser("dem")
    d.add_argument("--ds", required=True)
    d.add_argument("--mau")
    d.add_argument("--list", action="store_true")
    d.add_argument("ban", nargs="+")
    g = sub.add_parser("nguon")
    g.add_argument("--mau", required=True)
    g.add_argument("--tu", action="append", default=[], help="tên=file nguồn (SI, prompt, glossary…), lặp được")
    g.add_argument("--min-lan", type=int, default=2)
    g.add_argument("--min-ban", type=int, default=1)
    g.add_argument("--gap", type=float, default=8)
    g.add_argument("--max-mau", type=int, default=3, help="chỉ lấy cụm bộ mẫu dùng ≤ chừng này lần")
    g.add_argument("--top", type=int, default=80)
    g.add_argument("--loai-chu", default="")
    g.add_argument("ban", nargs="+")
    a = ap.parse_args(argv)
    {"quet": cmd_quet, "dem": cmd_dem, "nguon": cmd_nguon}[a.lenh](a)


if __name__ == "__main__":
    main(sys.argv[1:])
