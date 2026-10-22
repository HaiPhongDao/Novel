# Lãnh Chúa Mang Chip (tên tạm)

> Truyện thử nghiệm quy trình Agent ↔ Writer Gemini (xem `../AGENT.md`). Phạm vi test: **7 đoạn đầu** (tương đương 5 chương cũ).

**Logline:** Một kỹ sư hiện đại xuyên vào thân xác cậu con thứ bị đày ra lãnh địa biên giới đổ nát, chỉ mang theo một con chip thần kinh nguyên mẫu đã hỏng 61% dữ liệu — và có 87 ngày trước khi mùa đông giết sạch lãnh dân.

## Trạng thái — lượt 2 (SI v2)

Chính văn tiếng Trung, theo **đoạn** (~2000 字). Writer dùng `gemini/system-instruction-en-v2.md`. Lượt 1 (đoạn 1–5, SI cũ) lưu ở `archive/run-1/`.

| Đoạn | Prompt | Bản thảo | Review | Chốt |
|---|---|---|---|---|
| 001 | ✅ bản 3 | bản 1, 2 → `archive/run-2/` | ❌ bản 1 giải thích thừa · ❌ bản 2 cắt quá tay, mất giọng Gareth | — |

## Cách chạy

1. Gemini dùng system instruction 文风 riêng của Tác giả (không dán thêm hướng dẫn văn phong của Agent).
2. Dán `briefs/doan-XXX.md` vào Gemini → lưu kết quả vào `chapters/doan-XXX.md` (hoặc dán vào chat cho Agent).
3. Agent review → ghi `reviews/doan-XXX.md` (+ ghi chú sửa tiếng Trung nếu cần).
4. Chốt → Agent cập nhật bible, threads, log.

## Mục lục

- `bible/` — Story Bible (nguồn sự thật duy nhất)
- `plot/` — Arc, dàn ý, tuyến truyện mở
- `briefs/` — Prompt (tiếng Việt) giao Gemini; bản brief tiếng Việt v1 trong `archive/briefs-v1/`
- `gemini/system-instruction-en.md` — System Instruction của Writer, tiếng Anh (dịch từ `system-instruction.md`, anchor giữ nguyên)
- `gemini/test-prompts.md` — 3 prompt test vòng 1 + bảng chấm
- `reviews/test-B-C.md` — kết quả test vòng 1 và nguyên tắc prompt rút ra
- `handoff/` — Gói bàn giao chuyển session Gemini (`pack.md` dán thẳng)
- `log.md` — Nhật ký quyết định
