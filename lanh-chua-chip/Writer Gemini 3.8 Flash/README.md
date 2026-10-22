# Writer Gemini 3.8 Flash — lượt chạy song song

Lượt viết lại "Lãnh Chúa Mang Chip" từ đầu bằng **Gemini 3.8 Flash** (thinking High) trên Google AI Studio, chạy tự động qua Claude in Chrome (Edge). Lượt cũ ở thư mục cha dùng Gemini 3.1 Pro. Cùng SI 文风 (`../gemini/system-instruction.md`, bản đã bỏ phần thừa từ dự án khác + thêm quy tắc tên Latin).

Quy trình như `AGENT.md`, khác hai điểm theo yêu cầu Tác giả: **mỗi session Gemini 3 đoạn**; đoạn được duyệt thì commit + push ngay.

## Trạng thái

| Đoạn | Ngày truyện | Nội dung | Session | Review |
|---|---|---|---|---|
| 001 | 1 | Tỉnh dậy, trúng độc, giữ Pell | W1 | ĐẠT |
| 002 | 2 | Trà, Hob, đá nguyền, kho 5800 / 41 ngày / 87 ngày | W1 | ĐẠT |
| 003 | 2 | 秋季病, Mira–Tobi, giếng bẩn, lệnh đun nước | W1 | ĐẠT (lần 1 bị chặn "Prohibited content", chạy lại) |
| 004 | 2 | Luật lãnh chúa, Hoag, nồi đồng, nước muối mật | W2 | ĐẠT |
| 005 | 3–5 | Hố xí, rãnh, thành giếng; Hob khai 5800 | W2 | ĐẠT |
| 006 | 5–6 | Than đá, ba quy tắc | W2 | ĐẠT |
| 007 | 7 | Nhà Dunn ngộ độc khí than; Hob đổi ý; Mira xin tìm cha | W3 | ĐẠT |
| 008 | 8 | Rừng Sương Mù, Bram, "chúng đang chạy trốn" | W3 | ĐẠT |
| 009 | 9 | Kế hoạch rào bắc, chậu than | W3 | ĐẠT |
| 010 | 12–13 | Đợt sói dò bị rào chặn | W4 | ĐẠT |
| 011 | 13–15 | Bột hạt sồi, đập bắt cá | W4 | ĐẠT |
| 012 | 17 | Quản sự Morris; Pell nhận túi bột mới | W4 → **W5** | Bản 1 VIẾT LẠI (lộ chủ mưu) · bản 2 ĐẠT |
| 013 | 18–20 | Morris đi với sổ cũ; gian xông khói; thiếu muối | W5 | ĐẠT |
| 014 | 22 | Liều độc tăng, máu cam thật; luyện giáo | W5 → **W6** | Bản 1 VIẾT LẠI (lộ chủ mưu) · bản 2 ĐẠT |

**Dừng sau đoạn 014** — các đoạn sau cần Tác giả quyết (xem `plan-de-xuat.md`).

## Thư mục
- `chapters/` chính văn · `briefs/` prompt đã gửi · `reviews/` review từng đoạn · `handoff/` gói bàn giao (đã cập nhật tới hết đoạn 014) · `archive/` bản bị loại.
- `plan-de-xuat.md` — dàn ý đề xuất từ đoạn 010 và các câu hỏi chờ Tác giả.

## Công cụ
- `../../tools/build_pack.py "lanh-chua-chip/Writer Gemini 3.8 Flash" --prompt briefs/doan-XXX.md` → `handoff/session-start.md`.
- `../../tools/set_clip.ps1 <file>` / `save_clip.ps1 <file ra> "<ghi chú>" -ExpectLen N -ExpectHead "..."` — chuyển văn bản qua clipboard có kiểm tra (clipboard dùng chung cả máy, từng bị chương trình khác ghi đè).
