"""Gói Writer gọn: brief tự đủ + đuôi nguyên văn; gói quản lý đầy đủ vẫn ở pack.md."""
import argparse
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
story = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("brief")
args = parser.parse_args()
chapter = sorted((story / "chapters").glob("doan-*.md"))[-1]
paragraphs = chapter.read_text(encoding="utf-8").strip().split("\n\n")
tail = []
for paragraph in reversed(paragraphs):
    tail.insert(0, paragraph)
    if sum(map(len, tail)) >= 350:
        break
prompt = (story / args.brief).read_text(encoding="utf-8").strip()
out = story / "handoff" / "session-start.md"
body = ("# Tiếp tục truyện Kỵ sĩ\n\nĐọc đuôi chính văn và brief tự đủ, rồi viết đoạn tiếp theo. "
        "Những sự thật và trạng thái cần dùng nằm trong brief. Giữ giọng SI hiện hành.\n\n"
        "## Nguyên văn cuối " + chapter.stem + "\n\n" + "\n\n".join(tail) +
        "\n\n## Brief đoạn tiếp theo\n\n" + prompt + "\n")
out.write_text(body, encoding="utf-8", newline="")
print(f"Gói gọn {len(body)} ký tự; nguồn {chapter.name} + {args.brief}")
