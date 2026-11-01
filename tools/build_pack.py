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
import json
import re
import sys
import unicodedata
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

# Cắt state theo cảnh (JIT pruning). Lý do: mọi thứ nằm trong context của Writer đều
# được coi là "có việc để dùng", và cái gì không dùng được cho cảnh thì nó sẽ kể ra —
# đo được ở KN35 (đoạn 001 dán cả gói State: model xả số liệu liên thanh, giải mã kịch bản).
# Không đưa dữ liệu vào prompt là cách duy nhất chặn rò rỉ mà không cần thêm luật cấm.
GIU_LUON = {"story", "segment", "timeline", "location", "scene_bridge", "already_told",
            "ledger", "knowledge_map", "pov", "meta"}
# Trong một mục được giữ, mấy khoá này giữ nguyên dù brief không nhắc (để không mất danh tính).
GIU_TRONG_MUC = {"name", "age", "role", "status", "action", "pov"}


def _tok(s) -> set:
    s = unicodedata.normalize("NFD", str(s).lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return {w for w in re.split(r"[^a-z0-9]+", s) if len(w) > 2}


def _gia_tri(obj):
    if isinstance(obj, dict):
        for v in obj.values():
            yield from _gia_tri(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from _gia_tri(v)
    elif obj is not None:
        yield str(obj)


def _co_nhac(muc, brief_tok: set, ten_khoa: str) -> bool:
    if _tok(ten_khoa) & brief_tok:
        return True
    for v in _gia_tri(muc):
        if _tok(v) & brief_tok:
            return True
    return False


def cat_theo_canh(state: dict, brief: str) -> tuple[dict, list[str]]:
    """Trả (state đã cắt, danh sách đường dẫn bị bỏ)."""
    brief_tok = _tok(brief)
    giu, bo = {}, []
    for k, v in state.items():
        khoa_chuan = k.lower()
        if khoa_chuan in GIU_LUON:
            giu[k] = v
            continue
        if not _co_nhac(v, brief_tok, k):
            bo.append(k)
            continue
        if isinstance(v, dict):
            con, bo_con = {}, []
            for k2, v2 in v.items():
                if k2.lower() in GIU_TRONG_MUC or _co_nhac(v2, brief_tok, k2):
                    con[k2] = v2
                else:
                    bo_con.append(k2)
            giu[k] = con
            bo += [f"{k}.{x}" for x in bo_con]
        else:
            giu[k] = v
    return giu, bo


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
    ap.add_argument("--giu-het", action="store_true",
                    help="tắt cắt state theo cảnh (mặc định: chỉ nạp phần cảnh dùng tới)")
    args = ap.parse_args()

    story = Path(args.story)
    ho = story / "handoff"
    seg = latest_segment(story)
    seg_no = int(re.search(r"doan-(\d+)", seg.name).group(1))

    parts = [header(story)]
    # Có handoff/state.json (chung/state-extractor.md) thì nó thay story-so-far.md + state.md.
    sj = ho / "state.json"
    names = ("canon-card.md", "voice-anchor.md") if sj.exists() else ("canon-card.md", "story-so-far.md", "state.md", "voice-anchor.md")
    for name in names:
        if (ho / name).exists():
            parts.append((ho / name).read_text(encoding="utf-8").strip())
    if sj.exists():
        state = json.loads(sj.read_text(encoding="utf-8"))
        bo = []
        if args.prompt and not args.giu_het:
            brief = (story / args.prompt).read_text(encoding="utf-8") if (story / args.prompt).exists() else ""
            if brief:
                state, bo = cat_theo_canh(state, brief)
        parts.insert(2, "## 2. State (JSON — sự thật và con số đã xảy ra, lấy đây làm chuẩn)\n\n"
                     "Đoạn tiếp theo viết từ ngay sau `scene_bridge.last_beat`. Những gì trong `already_told` "
                     "người đọc đã biết: chỉ nhắc một chữ khi cần, không giải thích lại. Số liệu lấy theo `ledger`; "
                     "ai biết bí mật nào theo `knowledge_map`.\n\n"
                     + json.dumps(state, ensure_ascii=False, indent=1))
        if bo:
            print(f"cắt theo cảnh: bỏ {len(bo)} mục — {', '.join(bo)}")
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
