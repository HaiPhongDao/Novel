# Goblin Khai Hoá (tên tạm)

> Truyện thứ hai của xưởng. Luật chung: `../AGENT.md`; quy trình bàn giao, chạy AI Studio, lỗi văn chung: `../chung/`. Truyện tham khảo (Tác giả tải lên 22/10): `tham-khao/` — xem `tham-khao/phan-tich.md`.

**Logline:** Một thầy giáo hoá từng làm kỹ sư lò cao tỉnh dậy trong thân một con goblin còi vừa nở, ở cái hang mà tù trưởng ăn con non mỗi khi đói — và giống loài của anh học được mọi thứ người ta làm trước mặt, trừ việc hiểu vì sao.

## Trạng thái — khởi động (AGENT.md mục 11)

| Bước | Trạng thái |
|---|---|
| Phân tích truyện tham khảo | ✅ `tham-khao/phan-tich.md` |
| `bible/overview.md` | ✅ Tác giả duyệt 22/10 |
| `bible/glossary.md` | ✅ — tên tiếng Trung chốt sau đoạn 001 |
| `bible/characters/` | ✅ `khoa.md`, `bo-lac-hang-doi.md` |
| `bible/world.md` | ✅ luật goblin là luật cứng |
| `plot/arcs.md` → `plot/outline.md` | ✅ arc 1 chi tiết 16 đoạn |
| SI | ✅ duyệt v0 `gemini/system-instruction.md` — chờ viết thử đoạn 001 |
| `handoff/` | 📝 canon-card, state (đoạn 0), quiz |
| Prompt đoạn 001 | ✅ `briefs/doan-001.md` — chờ chạy Writer |

## Writer

- SI: `gemini/system-instruction.md` (nháp v0, 11.441 ký tự, 7 mục, 7 anchor từ truyện tham khảo). Đã lưu lên AI Studio 23/10, tên **"Goblin Khai Hoa - SI"**.
- Theo `../writer/SI-template` (hướng dẫn 1): viết thử đoạn 001 vài bản ở session riêng trước khi chốt SI.
- Lỗi riêng để soát: `gemini/review-blacklist.md` (+ `../chung/review-blacklist.md`).

| Đoạn | Prompt | Bản thảo | Review | Chốt |
|---|---|---|---|---|
| 001 | ✅ | ✅ | ⚠️ sửa nhẹ — Tác giả duyệt | ✅ |
| 002 | ✅ | ✅ | ✅ ĐẠT | ✅ |
| 003 | ✅ | ✅ | ✅ ĐẠT | ✅ |
| 004 | ✅ | ✅ | ✅ ĐẠT | ✅ |
| 005 | ✅ | ✅ | ⚠️ ĐẠT (sửa nhẹ) | ✅ |

Cách chạy một đoạn: `../README.md` mục "Một vòng đoạn".
