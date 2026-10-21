# Lãnh Chúa Mang Chip (tên tạm)

> Truyện thử nghiệm quy trình Agent ↔ Writer Gemini (xem `../AGENT.md`). Phạm vi test: **chương 1–5**.

**Logline:** Một kỹ sư hiện đại xuyên vào thân xác cậu con thứ bị đày ra lãnh địa biên giới đổ nát, chỉ mang theo một con chip thần kinh nguyên mẫu đã hỏng 61% dữ liệu — và có 87 ngày trước khi mùa đông giết sạch lãnh dân.

## Trạng thái

| Chương | Brief | Bản thảo (Gemini) | Review | Chốt |
|---|---|---|---|---|
| 001 | ✅ | ⏳ | — | — |
| 002 | ✅ | ⏳ | — | — |
| 003 | ✅ | ⏳ | — | — |
| 004 | ✅ | ⏳ | — | — |
| 005 | ✅ | ⏳ | — | — |

## Cách chạy vòng test

0. **Đang làm:** test so sánh 3 kiểu prompt — xem `gemini/test-prompts.md`.
1. Gemini dùng system instruction riêng của Tác giả (không dán thêm hướng dẫn văn phong của Agent).
2. Dán `briefs/ch-001.md` → nhận chương → lưu vào `chapters/ch-001.md`.
3. Gọi Agent review → Agent ghi `reviews/ch-001.md` và (nếu cần) ghi chú sửa để dán lại cho Gemini.
4. Chốt chương → Agent cập nhật bible, threads, log. Lặp lại với ch-002 → ch-005.

## Mục lục

- `bible/` — Story Bible (nguồn sự thật duy nhất)
- `plot/` — Arc, dàn ý, tuyến truyện mở
- `briefs/` — Brief giao Gemini
- `gemini/test-prompts.md` — 3 prompt test A/B/C + bảng chấm
- `log.md` — Nhật ký quyết định
