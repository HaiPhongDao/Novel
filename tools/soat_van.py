"""Soát lỗi văn có thể đếm được trong một đoạn chính văn tiếng Trung.

Dùng:
    python tools/soat_van.py <file.md> [<file2.md> ...] [--json]

Đếm các mẫu mà review phải bắt bằng mắt (AGENT.md mục 5, chung/review-blacklist.md):
phủ định排比 (没有…没有…, 不…不…, 既…也…), tương phản 不是…而是…, so sánh của người kể
(得像/仿佛/好似/如同), khuôn "实" (踩实/坐实/实实在在), nhãn ngữ điệu gắn vào lời nói
(语气平淡, 淡淡地说), từ hiện đại lọt vào bối cảnh, phân bố độ dài đoạn và độ dài lượt thoại.

Không phải trọng tài chất lượng — chỉ là bộ đếm để so hai bản và để biết SI có tác dụng không.
"""
import json
import re
import sys
from pathlib import Path

NEG = r"(?:没有|没|不曾|不|未|无)"

PATTERNS = {
    "phu-dinh-lap-cau": re.compile(
        rf"{NEG}[^，。；！？\n]{{0,12}}[，、][^。！？\n]{{0,8}}{NEG}"
    ),
    "phu-dinh-ba-lan": re.compile(rf"(?:{NEG}[^，。；！？\n]{{0,10}}[，、]){{2}}"),
    "ji-ye": re.compile(r"既[^，。\n]{0,14}[，]?\s*也[^，。\n]{0,14}"),
    "bu-shi-er-shi": re.compile(r"不是[^。\n]{0,20}[，]?\s*而是"),
    "so-sanh-nguoi-ke": re.compile(r"(?:得像|得如同|仿佛|好似|宛如|犹如|像一[个只根块])"),
    # Khuôn "thật/实": động từ + 实, và các cụm nhấn "làm cho thật/cụ thể".
    "khuon-shi": re.compile(
        r"(?:踩|坐|砸|压|攥|捏|顶|夯|握|摸|按|踏|落|问|查)实"
        r"|实打实|实实在在地?|结结实实|真真切切|真切|扎扎实实|扎得[^，。]{0,3}实"
        r"|结实|扎实|踏实"
    ),
    # Nhãn ngữ điệu: "语气平淡" "声音没有起伏" "淡淡地说" "面无表情地道".
    "nhan-ngu-dieu": re.compile(
        r"(?:语气|声音|语调|口气)[^，。！？\n]{0,10}"
        r"(?:平淡|平静|冷淡|冰冷|生硬|依旧|没有|毫无|不带|听不出|不变|很轻|很慢|平稳|漠然)"
        r"|(?:淡淡|冷冷|轻轻|慢慢|干巴巴|硬邦邦|平静|平淡|阴沉)地(?:说|道|答|问|回答|开口)"
        r"|(?:面无表情|不动声色|毫无起伏)地?(?:说|道|答|问|回答)"
    ),
    "hien-dai-tu": re.compile(
        r"(?:气焊|扳手|套筒|工单|流程|系统|数据|效率|成本控制|质量体系|KPI|流程化|标准化作业)"
    ),
    # Thẻ thoại lặp: mỗi lượt đều kèm 说道/问道/答道, và thường đứng đầu đoạn.
    "the-thoai": re.compile(r"(?:说道|问道|答道|应道|笑道|嚷道|开口说)"),
    "tag-dau-doan": re.compile(r"^[^“\n]{2,24}(?:说道|问道|答道|应道|笑道|嚷道)"),
}

MODERN_HINTS = "từ hiện đại: chỉ báo khi bối cảnh không cho phép (ký ức kiếp trước thì được)"

QUOTE = re.compile(r"“([^”]+)”")


def paragraphs(text):
    text = re.sub(r"^<!--.*?-->\s*", "", text, flags=re.S)
    return [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]


def han(s):
    return sum(1 for c in s if "\u4e00" <= c <= "\u9fff")


def scan(path):
    text = Path(path).read_text(encoding="utf-8")
    paras = paragraphs(text)
    body = "\n".join(paras)
    counts = {k: len(v.findall(body)) for k, v in PATTERNS.items()}
    # Đếm theo đoạn: thẻ thoại đứng đầu đoạn (mở đầu bằng tên + 说道/问道…).
    counts["tag-dau-doan"] = sum(
        1 for p in paras if re.match(r"[^“\n]{2,24}(?:说道|问道|答道|应道|笑道|嚷道)", p)
    )
    lens = [han(p) for p in paras]
    lens_sorted = sorted(lens)
    median = lens_sorted[len(lens_sorted) // 2] if lens_sorted else 0

    turns = [q.strip() for q in QUOTE.findall(body)]
    turn_lens = [han(t) for t in turns if han(t) > 0]
    mean_turn = round(sum(turn_lens) / len(turn_lens), 1) if turn_lens else 0

    # So sánh trong lời kể (bỏ phần trong ngoặc thoại — nhân vật nói ví von thì không phải tật của người kể).
    narration = QUOTE.sub("。", body)
    counts["so-sanh-loi-ke"] = len(PATTERNS["so-sanh-nguoi-ke"].findall(narration))

    return {
        "file": path,
        "han": han(body),
        "paragraphs": len(paras),
        "median_para_han": median,
        "short_paras": sum(1 for n in lens if n <= 20),
        "long_paras": sum(1 for n in lens if n >= 120),
        **counts,
        "luot-thoai": len(turn_lens),
        "tb-chu-luot": mean_turn,
        "luot-cut": sum(1 for n in turn_lens if n <= 6),
        "ti-le-thoai": round(sum(1 for p in paras if "“" in p) / len(paras) * 100) if paras else 0,
    }


def list_hits(path, keys=None):
    """In từng chỗ khớp kèm ngữ cảnh — để review theo từng lỗi, không chỉ đếm."""
    text = Path(path).read_text(encoding="utf-8")
    body = "\n".join(paragraphs(text))
    keys = keys or [k for k in PATTERNS if k != "tag-dau-doan"]
    print(f"== {Path(path).name}")
    total = 0
    for k in keys:
        for m in PATTERNS[k].finditer(body):
            s = max(0, m.start() - 30)
            ctx = body[s:m.end() + 30].replace("\n", " ")
            print(f"  [{k}] …{ctx}…")
            total += 1
    print(f"  → {total} chỗ khớp\n")
    return total


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        return 2
    if "--list" in argv:
        for a in args:
            list_hits(a)
        return 0
    rows = [scan(a) for a in args]
    if "--json" in argv:
        print(json.dumps(rows, ensure_ascii=False, indent=1))
        return 0
    cols = ["file", "han", "paragraphs", "median_para_han", "short_paras", "long_paras",
            "phu-dinh-lap-cau", "phu-dinh-ba-lan", "ji-ye", "bu-shi-er-shi", "so-sanh-nguoi-ke",
            "khuon-shi", "nhan-ngu-dieu", "hien-dai-tu",
            "luot-thoai", "tb-chu-luot", "luot-cut", "ti-le-thoai"]
    w = max(len(c) for c in cols) + 2
    print("".join(c.ljust(w) for c in cols))
    for r in rows:
        print("".join(str(r[c]).ljust(w) for c in cols))
    print(f"\n({MODERN_HINTS})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
