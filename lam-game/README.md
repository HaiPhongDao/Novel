# Chỉ Là Game, Cần Gì Thật — 《游戏而已，何必当真》 (tên tạm)

> Luật chung: `../AGENT.md`. Kinh nghiệm chung: `../chung/kinh-nghiem.md`.

**Logline:** Một người làm 游戏策划 chín năm xuyên vào thân một sinh viên vừa tốt nghiệp ở thế giới đã có game full-dive, nơi nhà làm game được tôn như nghệ sĩ và được xếp hạng theo độ *chân thực* — còn thứ gọi là "luật chơi" thì chưa ai coi là một nghề.

Đô thị giá không (không quốc gia) · không kim thủ chỉ · không chép game kiếp trước · tình cảm nhẹ · tông lai (arc 1 thực tế, sảng dần từ arc 2).

## Writer

- SI đang dùng: `gemini/system-instruction.md` (v2 — mục 3 nhập vai, mục 5 thoại đời thường; v1 = commit 6a2b99c; điền từ `../writer/SI-template` v3; anchor nguyên văn từ sách mẫu). **Chưa kiểm chứng** — theo hướng dẫn template, viết thử đoạn 001 vài bản ở các chat riêng rồi Tác giả đọc. Bản lưu trên AI Studio: `Lam game - SI` (chưa tạo).
- Sách mẫu: `全能游戏设计师.txt` — chỉ học kỹ thuật văn, không lấy thiết lập (truyện mẫu có kim thủ chỉ và chép game kiếp trước).
- Lỗi riêng để soát: `gemini/review-blacklist.md` (+ `../chung/review-blacklist.md`).
- Đoạn 001 mở session bằng SI + dán thẳng `briefs/doan-001.md` (chưa có đoạn trước nên chưa ghép gói). Từ đoạn 003: `python tools/build_pack.py lam-game --prompt briefs/doan-XXX.md`.

## Trạng thái

| Đoạn | Prompt | Bản thảo | Review | Chốt |
|---|---|---|---|---|
| 001 | ✅ bản 2 | bản 1 → `archive/` | bản 1 VIẾT LẠI | |

## Mục lục

- `bible/` — overview, world, glossary, timeline, style-guide, `games.md` (thiết kế các game của MC), `characters/`
- `plot/` — `arcs.md`, `outline.md` (chi tiết 001–008), `threads.md`
- `briefs/` — prompt tiếng Việt · `chapters/` — chính văn · `reviews/` — review
- `handoff/` — gói bàn giao (`../chung/quy-trinh-ban-giao.md`)
- `log.md` — nhật ký quyết định
