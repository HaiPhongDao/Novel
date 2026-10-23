# Chỉ Là Game, Cần Gì Thật — 《游戏而已，何必当真》 (tên tạm)

> Luật chung: `../AGENT.md`. Kinh nghiệm chung: `../chung/kinh-nghiem.md`.

**Logline:** Một người làm 游戏策划 chín năm xuyên vào thân một sinh viên vừa tốt nghiệp ở thế giới đã có game full-dive, nơi nhà làm game được tôn như nghệ sĩ và được xếp hạng theo độ *chân thực* — còn thứ gọi là "luật chơi" thì chưa ai coi là một nghề.

Đô thị giá không (không quốc gia) · không kim thủ chỉ · không chép game kiếp trước · tình cảm nhẹ · tông lai (arc 1 thực tế, sảng dần từ arc 2).

## Writer

- SI đang dùng: `gemini/system-instruction.md` (v2.1 — mục 3 nhập vai, mục 5 thoại đời thường, bỏ dòng "Character entrances"; v1 = commit 6a2b99c; điền từ `../writer/SI-template` v3; anchor nguyên văn từ sách mẫu). **Chưa kiểm chứng** — theo hướng dẫn template, viết thử đoạn 001 vài bản ở các chat riêng rồi Tác giả đọc. Bản lưu trên AI Studio: `Lam game - SI` (chưa tạo).
- Sách mẫu: `全能游戏设计师.txt` — chỉ học kỹ thuật văn, không lấy thiết lập (truyện mẫu có kim thủ chỉ và chép game kiếp trước).
- Lỗi riêng để soát: `gemini/review-blacklist.md` (+ `../chung/review-blacklist.md`).
- Model Writer: **gemini-3.6-flash** từ đoạn 002 bản 2 (Tác giả 23/10; 3.8 lúc đó quá tải). Chạy kèm `--model gemini-3.6-flash`.
- Chạy Writer: `python tools/gemini_write.py lam-game <số đoạn> --model gemini-3.6-flash --push` (`../chung/gemini-api.md`). Chạy tay trên AI Studio: đoạn đầu session dán `handoff/session-start.md` (`python tools/build_pack.py lam-game --prompt briefs/doan-XXX.md`), đoạn thứ hai dán thẳng prompt.

## Trạng thái

| Đoạn | Prompt | Bản thảo | Review | Chốt |
|---|---|---|---|---|
| 001 | ✅ bản 2 | ✅ bản 2 (S2); bản 1 → `archive/` | ✅ ĐẠT (bản 1 VIẾT LẠI) | ✅ |
| 002 | ✅ | ✅ bản 2 (S4, gemini-3.6-flash); bản 1 (3-flash) → `archive/` | ✅ ĐẠT | ✅ |
| 003 | ✅ | ✅ (S4, gemini-3.6-flash) | ✅ ĐẠT (lỗi nhẹ) | ✅ |
| 004 | ✅ | ✅ (S5, gemini-3.6-flash) | ✅ ĐẠT (lỗi nhẹ) | ✅ |
| 005 | ✅ v3 | ✅ bản 3 (S7); bản 1, 2 → `archive/` | ✅ ĐẠT (bản 1, 2 VIẾT LẠI) | ✅ |
| 006 | ✅ | ✅ (S7) | ✅ ĐẠT (lỗi nhẹ) | ✅ |
| 007 | ✅ | ✅ (S8) | ✅ ĐẠT (lỗi nhẹ) | ✅ |
| 008 | ✅ | ✅ (S8, mã 3.5-flash → 3.6) | ✅ ĐẠT (lỗi nhẹ) | ✅ |

## Mục lục

- `bible/` — overview, world, glossary, timeline, style-guide, `games.md` (thiết kế các game của MC), `characters/`
- `plot/` — `arcs.md`, `outline.md` (chi tiết 001–008), `threads.md`
- `briefs/` — prompt tiếng Việt · `chapters/` — chính văn · `reviews/` — review
- `handoff/` — gói bàn giao (`../chung/quy-trinh-ban-giao.md`)
- `log.md` — nhật ký quyết định
