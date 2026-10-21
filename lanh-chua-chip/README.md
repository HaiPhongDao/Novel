# Lãnh Chúa Mang Chip (tên tạm)

> Truyện thử nghiệm quy trình Agent ↔ Writer Gemini (xem `../AGENT.md`). Phạm vi test: **5 đoạn đầu**.

**Logline:** Một kỹ sư hiện đại xuyên vào thân xác cậu con thứ bị đày ra lãnh địa biên giới đổ nát, chỉ mang theo một con chip thần kinh nguyên mẫu đã hỏng 61% dữ liệu — và có 87 ngày trước khi mùa đông giết sạch lãnh dân.

## Trạng thái

Chính văn viết bằng **tiếng Trung**, theo **đoạn** (~2000 字), chia chương sau.

| Đoạn | Prompt | Bản thảo (Gemini) | Review | Chốt |
|---|---|---|---|---|
| test A/B/C | ✅ | B, C ✅ | ✅ `reviews/test-B-C.md` | — |
| 001 | ✅ bản cân bằng (tiếng Việt) | ✅ nháp 1 | ✅ SỬA NHẸ — chờ quyết vụ Pell | — |
| 002–005 | ⏳ (dàn ý có, prompt viết sau khi chốt mẫu ở đoạn 001) | — | — | — |

## Cách chạy

1. Gemini dùng system instruction 文风 riêng của Tác giả (không dán thêm hướng dẫn văn phong của Agent).
2. Dán `briefs/doan-XXX.md` vào Gemini → lưu kết quả vào `chapters/doan-XXX.md` (hoặc dán vào chat cho Agent).
3. Agent review → ghi `reviews/doan-XXX.md` (+ ghi chú sửa tiếng Trung nếu cần).
4. Chốt → Agent cập nhật bible, threads, log.

## Mục lục

- `bible/` — Story Bible (nguồn sự thật duy nhất)
- `plot/` — Arc, dàn ý, tuyến truyện mở
- `briefs/` — Prompt (tiếng Việt) giao Gemini; bản brief tiếng Việt v1 trong `archive/briefs-v1/`
- `gemini/test-prompts.md` — 3 prompt test vòng 1 + bảng chấm
- `reviews/test-B-C.md` — kết quả test vòng 1 và nguyên tắc prompt rút ra
- `log.md` — Nhật ký quyết định
