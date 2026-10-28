"""Soát tật của Writer trong một đoạn chính văn — chạy ngay sau khi Writer trả bài, trước khi đọc.

Dùng:  python tools/soat_tat.py <chapters/doan-NNN.md> [<đoạn trước.md> ...]

In số đếm và những dòng đáng ngờ:
  - trợ từ cuối câu kể trong lời thoại (…呢。 …啊。 …吧。) — tật lan qua đuôi đoạn trước (khong-binh 011–014);
  - khung "典型" (anchor A3 của SI v1);
  - đơn vị và từ hiện đại (米, 公里, 小时, 分钟, 机油…), tên đất thật;
  - lượt thoại cụt (≤ 8 chữ Hán).
Có đoạn trước thì in thêm số của chúng để thấy tật đang tăng hay giảm.
Không phải trọng tài — chỉ để biết đọc kỹ chỗ nào.
"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

HAN = re.compile(r"[一-鿿]")
MODERN = ["米", "公里", "公斤", "小时", "分钟", "秒钟", "机油", "阿拉伯", "欧洲", "中国", "美国", "英国",
          "汽车", "电", "工厂流水线", "百分之"]
OK_MI = ["大米", "玉米", "小米", "米粒", "米饭", "米汤", "糙米"]  # 米 là gạo


def count(path):
    t = Path(path).read_text(encoding="utf-8")
    turns = re.findall(r"“([^”]*)”", t)
    tail_particle = [x for x in turns if re.search(r"[呢啊吧][。！]?$", x) and not x.endswith("？")]
    short = [x for x in turns if len(HAN.findall(x)) <= 8]
    modern = []
    for w in MODERN:
        for m in re.finditer(w, t):
            ctx = t[max(0, m.start() - 2):m.end() + 2]
            if w == "米" and any(o in ctx for o in OK_MI):
                continue
            modern.append(ctx.replace("\n", " "))
    return dict(han=len(HAN.findall(t)), turns=len(turns), tail=tail_particle, short=short,
                dianxing=t.count("典型"), modern=modern)


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    cur = count(sys.argv[1])
    print(f"{Path(sys.argv[1]).name}: {cur['han']} 字, {cur['turns']} lượt thoại")
    print(f"  trợ từ cuối câu kể: {len(cur['tail'])}" + (" ⚠️" if len(cur["tail"]) > 3 else ""))
    for x in cur["tail"][:8]:
        print(f"    “{x[-30:]}”")
    print(f"  lượt cụt (≤8 字): {len(cur['short'])}  {cur['short'][:6]}")
    print(f"  典型: {cur['dianxing']}" + (" ⚠️" if cur["dianxing"] else ""))
    print(f"  từ/đơn vị hiện đại: {len(cur['modern'])}" + (" ⚠️" if cur["modern"] else ""))
    for x in cur["modern"]:
        print(f"    …{x}…")
    for p in sys.argv[2:]:
        c = count(p)
        print(f"  (so: {Path(p).name} — trợ từ cuối câu kể {len(c['tail'])}, 典型 {c['dianxing']}, cụt {len(c['short'])})")


if __name__ == "__main__":
    main()
