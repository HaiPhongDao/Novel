# Do bon so nhin thay giong (si-test-tren-mau.md muc 1.5) + nhip dong, cho goc va ban sinh.
# Dung: python do.py goc-t1.txt T1-a.md T1-b.md
import re, sys
sys.stdout.reconfigure(encoding="utf-8")
HAN = r"[一-鿿]"
def do(p):
    t = re.sub(r"<!--.*?-->", "", open(p, encoding="utf-8").read(), flags=re.S)
    t = re.sub(r"^#.*$", "", t, flags=re.M)
    lines = [l.strip() for l in t.split("\n") if l.strip()]
    han = len(re.findall(HAN, t))
    sents = [s for s in re.split(r"[。！？!?…]+[”」]?", t) if re.search(HAN, s)]
    turns = re.findall(r"“([^”]*)”", t)
    th = sum(len(re.findall(HAN, x)) for x in turns)
    lh = [len(re.findall(HAN, l)) for l in lines]
    so_sanh = len(re.findall(r"(?<!偶)像|仿佛|宛如|犹如|好似", t))
    return dict(chu=han, cau=len(sents), chu_cau=round(han / max(len(sents), 1), 1), luot=len(turns),
                chu_luot=round(th / max(len(turns), 1), 1), thoai=f"{th / max(han, 1):.0%}", dong=len(lines),
                dong_le15=f"{sum(1 for x in lh if x < 15) / len(lh):.0%}", dong_15_40=f"{sum(1 for x in lh if 15 <= x < 40) / len(lh):.0%}",
                so_sanh_1000=round(so_sanh * 1000 / max(han, 1), 2))
cols = None
for p in sys.argv[1:]:
    r = do(p)
    if cols is None:
        cols = list(r); print("| bản | " + " | ".join(cols) + " |"); print("|---" * (len(cols) + 1) + "|")
    print(f"| {p} | " + " | ".join(str(r[c]) for c in cols) + " |")
