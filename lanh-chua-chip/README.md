# Lãnh Chúa Mang Chip (tên tạm)

> Truyện đầu tiên của xưởng, dùng để thử quy trình Agent ↔ Writer Gemini. Luật chung: `../AGENT.md`; quy trình bàn giao, chạy AI Studio, lỗi văn chung: `../chung/`.

**Logline:** Một kỹ sư hiện đại xuyên vào thân xác cậu con thứ bị đày ra lãnh địa biên giới đổ nát, chỉ mang theo một con chip thần kinh nguyên mẫu đã hỏng 61% dữ liệu — và có 87 ngày trước khi mùa đông giết sạch lãnh dân.

## Trạng thái — lượt 2 (SI v2)

Chính văn tiếng Trung, theo **đoạn** (~2000 字). Lượt 1 (đoạn 1–5, SI cũ) lưu ở `archive/run-1/`; bản hỏng của lượt 2 ở `archive/run-2/`.

## Writer

- SI đang dùng: `gemini/system-instruction-en-v2.md` (mục 3 Output đã sửa 22/10: mở nối liền, dừng giữa mạch). Bản lưu trên AI Studio tên **"Lanh chua chip - SI v2"** (10.823 ký tự). Bản cũ: `system-instruction-en.md`, `system-instruction.md`.
- Model: Gemini 3.8 Flash, thinking High, tắt Google Search (`../chung/ai-studio.md`).
- Lỗi riêng để soát: `gemini/review-blacklist.md` (+ `../chung/review-blacklist.md`).
- `handoff/quiz.md`: câu hỏi kiểm tra khi chỉ nạp gói.

| Đoạn | Prompt | Bản thảo | Review | Chốt |
|---|---|---|---|---|
| 001 | ✅ bản 4 | ✅ bản 4 (bản 1–3 → `archive/run-2/`) | ✅ ĐẠT | ✅ |
| 002 | ✅ | ✅ (S1) | ✅ ĐẠT | ✅ |
| 003 | ✅ (mở S2) | ✅ (S2) | ✅ ĐẠT | ✅ |
| 004 | ✅ bản 3 (mở S4) | ✅ bản 3 (S4); bản 1–2 → `archive/run-2/` | ✅ ĐẠT (bản 1–2 VIẾT LẠI) | ✅ |
| 005 | ✅ bản 2 (mở S5) | ✅ bản 2 (S5); bản 1 → `archive/run-2/` | ✅ ĐẠT (bản 1 VIẾT LẠI) | ✅ |
| 006 | ✅ (S5) | ✅ (S5) | ✅ ĐẠT | ✅ |
| 007 | ✅ (mở S6) | ✅ (S6) | ✅ ĐẠT | ✅ |
| 008 | ✅ (S6) | ✅ (S6) | ✅ ĐẠT | ✅ |
| 009 | ✅ (mở S7) | ✅ (S7) | ✅ ĐẠT | ✅ |
| 010 | ✅ (S7) | ✅ (S7) | ✅ ĐẠT | ✅ |
| 011 | ✅ bản 2 (mở S9) | ✅ bản 2 (S9); bản 1 → `archive/run-2/` | ✅ ĐẠT (bản 1 VIẾT LẠI) | ✅ |
| 012 | ✅ (S9) | ✅ (S9) | ✅ ĐẠT | ✅ |
| 013 | ✅ (mở S10) | ✅ (S10) | ✅ ĐẠT | ✅ |
| 014 | ✅ (S10) | ✅ (S10) | ✅ ĐẠT | ✅ |
| 015 | ✅ bản 2 (mở S12) | ✅ bản 2 (S12); bản 1 → `archive/run-2/` | ✅ ĐẠT (bản 1 VIẾT LẠI) | ✅ |

Cách chạy một đoạn: `../README.md` mục "Một vòng đoạn".

## Mục lục

- `bible/` — Story Bible (nguồn sự thật duy nhất)
- `plot/` — Arc, dàn ý, tuyến truyện mở
- `briefs/` — Prompt (tiếng Việt) giao Gemini; bản brief tiếng Việt v1 trong `archive/briefs-v1/`
- `gemini/system-instruction-en.md` — System Instruction của Writer, tiếng Anh (dịch từ `system-instruction.md`, anchor giữ nguyên)
- `gemini/test-prompts.md` — 3 prompt test vòng 1 + bảng chấm
- `reviews/test-B-C.md` — kết quả test vòng 1 và nguyên tắc prompt rút ra
- `handoff/` — Gói bàn giao chuyển session Gemini (`session-start.md` mở session; quy trình ở `../chung/quy-trinh-ban-giao.md`)
- `Writer Gemini 3.8 Flash/` — lượt chạy song song trước lượt 2 (đoạn 1–14, chờ Tác giả)
- `qwen/` — Modelfile thử Writer bằng Ollama
- `log.md` — Nhật ký quyết định
