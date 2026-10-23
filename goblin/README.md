# Goblin Khai Hoá (tên tạm)

> Truyện thứ hai của xưởng. Luật chung: `../AGENT.md`; quy trình bàn giao, chạy AI Studio, lỗi văn chung: `../chung/`. Truyện tham khảo (Tác giả tải lên 22/10): `tham-khao/` — xem `tham-khao/phan-tich.md`.

**Logline:** Một thầy giáo hoá từng làm kỹ sư lò cao tỉnh dậy trong thân một con goblin còi vừa nở, ở cái hang mà tù trưởng ăn con non mỗi khi đói — và giống loài của anh học được mọi thứ người ta làm trước mặt, trừ việc hiểu vì sao.

## Trạng thái

**Lượt 2** (Tác giả 23/10): viết lại từ đoạn 001 theo cách prompt ngắn — phương hướng + số liệu, Writer tự do phần còn lại (`../AGENT.md` mục 4). Lượt 1 (001–006 đã chốt, brief chi tiết) → `archive/luot-1/` (briefs, chapters, reviews, handoff).

⚠️ `bible/` và `plot/` giữ nguyên bản Tác giả duyệt 22/10. Những gì lượt 1 thêm vào (Mok, đống sỏi 112, "Ko" từ Yeg, giao kèo thịt nướng, nhóm năm = bốn ngón + lòng bàn tay) **không** tự sang lượt 2 — chỉ vào canon khi lượt 2 viết ra và qua review. `handoff/canon-card.md` chỉ còn phần thiết lập cố định; state/story-so-far/voice-anchor đã dựng lại theo lượt 2 (tới đoạn 002).

Từ đoạn 004 Agent tự chạy Writer: `python tools/gemini_write.py goblin <số đoạn> --model gemini-3.6-flash` (Tác giả 23/10: 3.8 không dùng được).

## Writer

- SI: `gemini/system-instruction.md` (nháp v0, 11.441 ký tự, 7 mục, 7 anchor từ truyện tham khảo). Đã lưu lên AI Studio 23/10, tên **"Goblin Khai Hoa - SI"**.
- Lượt 2 vẫn chạy SI v0 để so được với lượt 1 (chỉ đổi prompt). Đề xuất sửa SI sau 6 đoạn lượt 1 (`log.md` 23/10) vẫn chờ Tác giả.
- Session S1 lượt 2: đoạn 001 mở chat mới, dán `briefs/doan-001.md` (không cần gói bàn giao); đoạn 002 dán thẳng `briefs/doan-002.md` vào cùng chat.
- Lỗi riêng để soát: `gemini/review-blacklist.md` (+ `../chung/review-blacklist.md`).

| Đoạn | Prompt | Bản thảo | Review | Chốt |
|---|---|---|---|---|
| 001 | ✅ | ✅ (Tác giả chạy) | ⚠️ ĐẠT (sửa nhẹ) — chờ Tác giả 2 điểm canon | |
| 002 | ✅ | ✅ (Tác giả chạy) | ⚠️ ĐẠT (sửa nhẹ) | |
| 003 | ✅ | ✅ (Tác giả chạy) | ⚠️ ĐẠT (sửa nhẹ) | |
| 004 | ✅ | ✅ (Agent, API 3.6-flash) | ⚠️ ĐẠT (sửa nhẹ) | |
| 005 | ✅ | ✅ (Agent, API 3.6-flash) | ⚠️ ĐẠT (sửa nhẹ) | |
| 006 | ✅ | ✅ (Agent, API 3.6-flash) | ⚠️ ĐẠT (sửa nhẹ) | |
| 007 | ✅ | ✅ (Tác giả chạy) | ⚠️ ĐẠT (sửa nhẹ) | |
| 008 | ✅ | ✅ (Tác giả chạy) | ⚠️ ĐẠT (sửa nhẹ) | |
| 009 | ✅ | ⬜ file trống — chờ dán (cùng chat S4) | | |
| 010 | | ⬜ file trống | | |
| 011 | | ⬜ file trống | | |
| 012 | | ⬜ file trống | | |

Cách chạy một đoạn: `../README.md` mục "Một vòng đoạn".
