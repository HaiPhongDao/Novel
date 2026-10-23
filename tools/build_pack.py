#!/usr/bin/env python3
"""Ghép gói bàn giao (handoff pack) để mở session Writer mới — dùng cho mọi truyện.

Dùng:  python tools/build_pack.py <thu-muc-truyen> [--tail 900] [--prompt briefs/doan-XXX.md]
Ra:    <thu-muc-truyen>/handoff/pack.md
       (có --prompt) <thu-muc-truyen>/handoff/session-start.md = tin nhắn đầu tiên của session Writer mới:
       gói bàn giao + prompt đoạn kế, Writer đọc rồi viết luôn
Câu hỏi kiểm tra trong pack.md lấy từ <thu-muc-truyen>/handoff/quiz.md nếu có, không thì QUIZ_MAC_DINH.
Quy trình: chung/quy-trinh-ban-giao.md
"""
import argparse
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

INTRO = """# Tài liệu bàn giao — tiếp tục viết truyện

Bạn là Writer của truyện này. Các đoạn trước bạn đã viết ở một session cũ; tài liệu dưới đây là toàn bộ những gì cần nhớ để viết tiếp đúng mạch và đúng giọng.
"""

QUIZ_MAC_DINH = """1. Nhân vật chính đang ở đâu, vừa làm gì.
2. Những bí mật và tuyến đang mở mà nhân vật chính biết.
3. Các con số đang chạy."""


def header(story: Path) -> str:
    q = story / "handoff" / "quiz.md"
    quiz = q.read_text(encoding="utf-8").strip() if q.exists() else QUIZ_MAC_DINH
    n = len([l for l in quiz.splitlines() if l.strip()])
    return (f"{INTRO}\n**Lần này chưa viết chính văn.** Đọc kỹ toàn bộ, rồi trả lời ngắn bằng tiếng Việt đúng {n} dòng:\n"
            f"{quiz}\n\nSau đó chờ prompt của đoạn tiếp theo.\n")


def latest_segment(story: Path) -> Path:
    # bỏ qua file trống tạo sẵn để dán chính văn
    segs = sorted(s for s in story.glob("chapters/doan-*.md") if s.read_text(encoding="utf-8").strip())
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
    ap.add_argument("--prompt", help="prompt đoạn kế (đường dẫn trong thư mục truyện) → handoff/session-start.md")
    args = ap.parse_args()

    story = Path(args.story)
    ho = story / "handoff"
    seg = latest_segment(story)
    seg_no = int(re.search(r"doan-(\d+)", seg.name).group(1))

    parts = [header(story)]
    for name in ("canon-card.md", "story-so-far.md", "state.md", "voice-anchor.md"):
        if (ho / name).exists():
            parts.append((ho / name).read_text(encoding="utf-8").strip())
    parts.append(
        f"## 5. Nguyên văn phần cuối đoạn {seg_no} (để nối mạch và giữ giọng)\n\n"
        + tail_text(seg, args.tail)
        + f"\n\n(Đoạn {seg_no + 1} sẽ bắt đầu ngay sau chỗ này.)"
    )

    out = ho / "pack.md"
    out.write_text("\n\n---\n\n".join(parts) + "\n", encoding="utf-8")
    print(f"{out}  ({len(out.read_text(encoding='utf-8'))} ký tự, tail từ {seg.name})")

    if args.prompt:
        head = INTRO.rstrip() + "\n\nĐọc kỹ toàn bộ, rồi viết đoạn tiếp theo theo prompt ở phần cuối.\n"
        prompt = (story / args.prompt).read_text(encoding="utf-8").strip()
        start = ho / "session-start.md"
        start.write_text("\n\n---\n\n".join([head] + parts[1:] + ["## 6. Prompt đoạn tiếp theo\n\n" + prompt]) + "\n", encoding="utf-8")
        print(f"{start}  ({len(start.read_text(encoding='utf-8'))} ký tự, mở session mới)")


if __name__ == "__main__":
    main()
