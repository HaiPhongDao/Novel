# manga-tokyo-1996 — Tân Binh & Chiếc Bàn Vẽ Nghiêng (1996)

**Logline:** Tháng 4/1996 tại Tokyo, cựu trợ lý manga 23 tuổi Kamishiro Ren sau khi bị từ chối 45 trang bản thảo mô phỏng kỹ thuật vô hồn đã nhận tối hậu thư từ Phó ban biên tập 《周刊少年SPARK》: 14 ngày để hoàn thành một oneshot 31 trang thế chỗ tác giả ngã bệnh cho số đặc biệt mùa hè, nếu thất bại phải cuốn gói về quê với 4.200 yên trong túi trước hạn nợ phòng trọ Koenji.

- **Trục:** Trục **Nghề Vẽ Manga & Cuộc Chiến Tuần San (Manga Workplace)**: Tập trung vào bản chất nghề vẽ truyện tranh thập niên 90 — âm thanh ngòi bút G, mực Kuretake, giấy Kent 135kg, kỹ thuật dán cạo tram, tâm lý độc giả và sự khốc liệt trên bàn duyệt bản thảo toà soạn.
- **Bàn tay vàng:** Không bàn tay vàng vô lý; sức bật đến từ kỹ năng rèn giũa 3 năm làm trợ lý bối cảnh, sự tự thức tỉnh về linh hồn tác phẩm và kỷ luật vẽ khắc nghiệt.
- **Bộ mẫu:** `../我在泡沫东京画漫画.txt` (440.232 chữ Hán). Đích đo sẵn: phủ định lặp 1,39/1.000 字, so sánh người kể 0,114, khuôn 实 0,034, nhãn ngữ điệu 0,030, thẻ thoại 1,329, lượt cụt 6,401.
- **Khung brief:** Mẫu A (`../.claude/skills/novel-craft/templates/brief-doan.md`), qua cổng `tools/soat_brief.py`.

## Writer

- SI đang dùng: `gemini/system-instruction-v1.md` — phần dán **7.911 ký tự** (`dung_si.py`), 4 anchor nguyên văn từ các chương 14, 21, 10, 22 của bộ mẫu, `verify_anchors.py` khớp 4/4; `anchor字` = 689 ký tự (9% phần dán ≤ 15%); PART 2 = 6 dòng (≤ 8); BANS đúng 5 dòng; neo độ dài câu 22–30 字. Bản dựng: `gemini/si-dan-gemini.txt`.
- Lỗi riêng để soát: `gemini/review-blacklist.md`.

## Trạng thái

| Đoạn | Brief | Bản thảo | Số chữ (字) | Review | Trạng thái |
|---|---|---|---|---|---|
| 001 | `briefs/doan-001-c.md` | `chapters/doan-001.md` | 2.324 字 | `reviews/doan-001.md` | ⏳ Đang chờ Tác giả duyệt chính văn |
| 002 | `briefs/doan-002.md` | `chapters/doan-002.md` | — | `reviews/doan-002.md` | Chờ duyệt đoạn 001 |
| 003 | `briefs/doan-003.md` | `chapters/doan-003.md` | — | `reviews/doan-003.md` | Chờ duyệt đoạn 001 |
