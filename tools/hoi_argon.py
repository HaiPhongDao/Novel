"""Công cụ cầu nối: Gom bối cảnh dự án Novel, tự động hỏi Argon trên Gemini Web để nhận nhiệm vụ.

Dùng:
    # 1. Tự động gom bối cảnh để hỏi nhiệm vụ cho đoạn kế tiếp (ví dụ đoạn 002 của manga-tokyo-2000):
    python tools/hoi_argon.py --truyen manga-tokyo-2000 --doan 002

    # 2. Hoặc gửi một file prompt / câu hỏi kiến trúc tùy ý:
    python tools/hoi_argon.py --prompt tasks/cau-hoi-argon.md --out tasks/tra-loi.md
"""
import argparse
import json
import sys
from pathlib import Path

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

# Thêm tools vào sys.path để import gemini_web_run
sys.path.insert(0, str(Path(__file__).parent))
from gemini_web_run import run_gemini_web, DEFAULT_URL


def build_doan_context_prompt(repo_dir: Path, truyen: str, doan_num: str) -> str:
    truyen_dir = repo_dir / truyen
    if not truyen_dir.exists():
        raise FileNotFoundError(f"Không tìm thấy thư mục truyện: {truyen_dir}")

    # Đọc bible overview
    overview_file = truyen_dir / "bible" / "overview.md"
    overview = overview_file.read_text(encoding="utf-8") if overview_file.exists() else ""

    # Đọc log.md
    log_file = truyen_dir / "log.md"
    log_content = log_file.read_text(encoding="utf-8") if log_file.exists() else ""

    # Đọc review đoạn trước
    prev_num = f"{int(doan_num) - 1:03d}"
    prev_review_file = truyen_dir / "reviews" / f"doan-{prev_num}.md"
    prev_review = prev_review_file.read_text(encoding="utf-8") if prev_review_file.exists() else ""

    # Đọc state
    state_file = truyen_dir / "handoff" / "state.json"
    state_content = state_file.read_text(encoding="utf-8") if state_file.exists() else ""

    prompt = f"""Bạn là **Kiến trúc sư truyện & Đồng sáng lập (Story Manager / Co-founder)** của dự án Novel.
Tôi là **Agent thợ địa phương (Gemini Flash)** phụ trách thực thi trực tiếp trên repo `{truyen}`.
Vì Agent mode chạm limit tuần của Argon, tôi cần bạn (Argon bản chat) giữ vai trò Kiến trúc sư, hoạch định nhiệm vụ và duyệt canon cho **Đoạn {doan_num}**.

---
### 1. BỐI CẢNH TRUYỆN ({truyen})
{overview.strip()}

---
### 2. TRẠNG THÁI & KẾT QUẢ ĐOẠN TRƯỚC (Đoạn {prev_num})
{prev_review.strip()}

---
### 3. NHẬT KÝ QUYẾT ĐỊNH & ĐỊNH HƯỚNG GẦN NHẤT
{log_content.strip()}

---
### 4. STATE HIỆN TẠI
```json
{state_content.strip()[:2000]}
```

---
### NHIỆM VỤ CỦA BẠN (ARGON):
Xin hãy phân tích và đưa ra kế hoạch nhiệm vụ cụ thể cho **Đoạn {doan_num}**:

1. **Dàn ý từng nhịp (Beats & Cảnh)** cho đoạn {doan_num} (~2.000 - 2.500 chữ):
   - Mở đầu bằng sự kiện gì?
   - Thân đoạn triển khai xung đột / bối cảnh MC thế nào? (Lưu ý: đoạn 001 đã lỡ kể tên kiếp trước Kudo Shun và bàn tay vàng 【分镜库】, nên đoạn này cần tập trung vào: vì sao chọn truyện tranh, mẹ ở Niigata, quan hệ với Fujii, chuẩn bị cho One Cut of the Dead 《摄影机不要停！》).
   - Điểm dừng giữa mạch (hook / cliffhanger) ở cuối đoạn.

2. **Dự thảo Brief giao Writer** (theo Mẫu A ngắn gọn, tiếng Việt):
   - Ghi rõ hướng cảnh, số liệu, nhân vật có mặt, những điều CẤM (tránh lặp lại chi tiết đã kể ở đoạn 001).

3. **Cập nhật Canon & State**:
   - Những dữ kiện nào mới cần được thêm vào State JSON hoặc Story Bible?

4. **Nhiệm vụ bàn giao cho Agent thợ**:
   - Liệt kê dạng danh sách công việc [ ] để tôi (Agent Flash) tự động tạo file brief, cập nhật state, chạy Writer và kiểm tra.
"""
    return prompt


def main():
    ap = argparse.ArgumentParser(description="Hỏi nhiệm vụ từ Argon trên Gemini Web")
    ap.add_argument("--truyen", default="manga-tokyo-2000", help="Tên truyện (mặc định: manga-tokyo-2000)")
    ap.add_argument("--doan", help="Số đoạn cần xin chỉ đạo (ví dụ: 002)")
    ap.add_argument("--prompt", help="File chứa prompt tùy ý (nếu không dùng --doan)")
    ap.add_argument("--out", help="File lưu nhiệm vụ của Argon")
    ap.add_argument("--url", default=DEFAULT_URL, help="URL Gemini Web")
    ap.add_argument("--thinking", default="High", help="Mức suy nghĩ / Thinking (High / Medium / Low / on / off)")
    ap.add_argument("--think-out", help="File lưu riêng phần suy nghĩ của Argon")
    ap.add_argument("--timeout", type=int, default=20, help="Phút chờ tối đa")
    args = ap.parse_args()

    repo_dir = Path(__file__).resolve().parent.parent

    if args.prompt:
        prompt_text = Path(args.prompt).read_text(encoding="utf-8")
        out_path = args.out or f"tasks/argon-tra-loi.md"
    elif args.doan:
        doan_num = f"{int(args.doan):03d}"
        prompt_text = build_doan_context_prompt(repo_dir, args.truyen, doan_num)
        out_path = args.out or str(repo_dir / "tasks" / f"argon-nhiem-vu-doan-{doan_num}.md")
        # Lưu lại cả prompt đã gửi để theo dõi
        prompt_log = repo_dir / "tasks" / f"prompt-gui-argon-{doan_num}.md"
        prompt_log.parent.mkdir(parents=True, exist_ok=True)
        prompt_log.write_text(prompt_text, encoding="utf-8")
    else:
        ap.error("Cần cung cấp --doan <số> hoặc --prompt <file>")

    print(f"=== GIAO TIẾP VỚI ARGON (GEMINI WEB) ===")
    print(f"URL: {args.url}")
    print(f"Thinking: {args.thinking}")
    print(f"Đầu ra: {out_path}")
    print("Đang khởi động bridge và gửi việc sang Edge...")

    ok, res = run_gemini_web(
        prompt_text=prompt_text,
        out_path=out_path,
        url=args.url,
        reuse_tab=True,
        timeout_min=args.timeout,
        think_out=args.think_out,
        thinking=args.thinking
    )

    if ok:
        print("\n=== ĐÃ NHẬN NHIỆM VỤ TỪ ARGON ===")
        print(f"Xem chi tiết tại: {out_path}")
        print("Agent thợ đã sẵn sàng đọc file này và triển khai!")
        return 0
    else:
        print(f"\n[LỖI] Không nhận được phản hồi: {res}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
