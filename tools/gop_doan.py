"""Gộp chính văn theo khối 10 đoạn: chapters/doan-001…010.md → gop/doan-001-010.md.

Dùng:  python tools/gop_doan.py <ten-truyen> [--co 10]

Chỉ gộp khối đã đủ cả 10 đoạn liền nhau (001–010, 011–020…); khối đang dở thì bỏ qua.
Chạy lại bao nhiêu lần cũng được: mỗi lần ghi lại toàn bộ các khối đủ từ chapters/,
nên sửa chính văn ở chapters/ rồi chạy lại là file gộp theo kịp. Không sửa tay file trong gop/.
tools/chot_doan.py tự gọi script này trước khi commit, nên đoạn thứ 10 chốt xong là có file gộp.
"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
HAN = re.compile(r"[一-鿿]")
COMMENT = re.compile(r"\A\s*<!--.*?-->\s*", re.S)


def prose(path):
    """Chính văn của một đoạn, bỏ các dòng chú thích <!-- … --> ở đầu file."""
    s = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    while (m := COMMENT.match(s)):
        s = s[m.end():]
    return s.strip()


def gop(story_name, size=10):
    """Ghi mọi khối đủ `size` đoạn; trả về danh sách file đã ghi."""
    D = REPO / story_name
    chapters = {int(m[1]): p for p in (D / "chapters").glob("doan-*.md")
                if (m := re.fullmatch(r"doan-(\d{3})\.md", p.name))}
    if not chapters:
        return []
    title = story_name
    readme = D / "README.md"
    if readme.exists() and (m := re.search(r"^# (.+)$", readme.read_text(encoding="utf-8"), re.M)):
        title = m[1].strip()

    written = []
    for start in range(1, max(chapters) + 1, size):
        nums = range(start, start + size)
        missing = [n for n in nums if n not in chapters]
        if missing:
            if len(missing) < size and max(chapters) >= nums[-1]:
                print(f"Khối {start:03d}–{nums[-1]:03d} thiếu đoạn {', '.join(f'{n:03d}' for n in missing)} — bỏ qua")
            continue
        parts = [(n, prose(chapters[n])) for n in nums]
        total = sum(len(HAN.findall(t)) for _, t in parts)
        out = D / "gop" / f"doan-{nums[0]:03d}-{nums[-1]:03d}.md"
        body = [f"# {title} — Đoạn {nums[0]:03d}–{nums[-1]:03d}",
                f"<!-- Gộp tự động bằng tools/gop_doan.py từ chapters/; {total:,} chữ Hán. "
                "Sửa chính văn ở chapters/ rồi chạy lại, không sửa file này. -->"]
        for n, t in parts:
            body += [f"## Đoạn {n:03d}", t]
        out.parent.mkdir(exist_ok=True)
        text = "\n\n".join(body) + "\n"
        if not out.exists() or out.read_text(encoding="utf-8") != text:
            out.write_text(text, encoding="utf-8", newline="")
            written.append(out)
            print(f"Đã gộp {out.relative_to(REPO).as_posix()} ({total:,} chữ Hán)")
    return written


def main():
    args = sys.argv[1:]
    size = 10
    if "--co" in args:
        i = args.index("--co")
        size = int(args[i + 1])
        del args[i:i + 2]
    if len(args) != 1 or not (REPO / args[0]).is_dir():
        raise SystemExit(__doc__)
    if not gop(args[0], size):
        print("Không có khối mới hoặc thay đổi để gộp")


if __name__ == "__main__":
    main()
