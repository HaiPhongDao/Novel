#!/usr/bin/env python3
"""Ghép gói bàn giao (handoff pack) để mở session Writer Gemini mới.

Dùng:  python3 tools/build_pack.py <thu-muc-truyen> [--tail 900] [--prompt briefs/doan-XXX.md]
Ra:    <thu-muc-truyen>/handoff/pack.md
       (có --prompt) <thu-muc-truyen>/outbox.md = gói bàn giao + prompt, dán một lần vào session Gemini mới
"""
import argparse
import re
from pathlib import Path

HEADER = """# Tài liệu bàn giao — tiếp tục viết truyện

Bạn là Writer của truyện này. Các đoạn trước bạn đã viết ở một session cũ; tài liệu dưới đây là toàn bộ những gì cần nhớ để viết tiếp đúng mạch và đúng giọng.

Đọc kỹ toàn bộ, rồi viết đoạn tiếp theo theo prompt ở cuối tài liệu.
"""


def latest_segment(story: Path) -> Path:
    segs = sorted(story.glob("chapters/doan-*.md"))
    if not segs:
        raise SystemExit("Chưa có đoạn nào trong chapters/")
    return segs[-1]


def tail_text(path: Path, n_chars: int) -> str:
    text = re.sub(r"<!--.*?-->", "", path.read_text(encoding="utf-8"), flags=re.S).strip()
    paras = [p for p in text.splitlines() if p.strip()]
    out, total = [], 0
    for p in reversed(paras):
        out.append(p)
        total += len(p.strip())
        if total >= n_chars:
            break
    return "\n".join(reversed(out))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("story")
    ap.add_argument("--tail", type=int, default=900, help="số ký tự cuối đoạn gần nhất")
    ap.add_argument("--prompt", help="prompt đoạn tiếp theo (đường dẫn trong thư mục truyện) — ghép vào outbox.md")
    args = ap.parse_args()

    story = Path(args.story)
    ho = story / "handoff"
    seg = latest_segment(story)
    seg_no = int(re.search(r"doan-(\d+)", seg.name).group(1))

    parts = [HEADER]
    for name in ("canon-card.md", "story-so-far.md", "state.md"):
        parts.append((ho / name).read_text(encoding="utf-8").strip())
    parts.append(
        f"## 4. Nguyên văn phần cuối đoạn {seg_no} (để nối mạch và giữ giọng)\n\n"
        + tail_text(seg, args.tail)
        + f"\n\n(Đoạn {seg_no + 1} sẽ bắt đầu ngay sau chỗ này.)"
    )

    pack = "\n\n---\n\n".join(parts) + "\n"
    out = ho / "pack.md"
    out.write_text(pack, encoding="utf-8")
    print(f"{out}  ({len(pack)} ký tự, tail từ {seg.name})")

    if args.prompt:
        prompt = (story / args.prompt).read_text(encoding="utf-8").strip()
        outbox = story / "outbox.md"
        outbox.write_text(pack + "\n---\n\n## 5. Prompt đoạn tiếp theo\n\n" + prompt + "\n", encoding="utf-8")
        print(f"{outbox}  (session mới: gói + prompt)")


if __name__ == "__main__":
    main()
