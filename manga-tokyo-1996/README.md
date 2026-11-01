# manga-tokyo-1996 — Kỷ nguyên Media Mix & Cuộc chiến Đồ chơi 1996

**Logline:** Tháng 3/1996 tại Tokyo, họa sĩ manga kiêm nhà thiết kế cơ giới Kamishiro Ren — người tỉnh dậy sau khi chết ở tuổi 38 vào năm 2024 — tiếp quản một xưởng vẽ nợ nần và dự án Media Mix 《极速齿轮》 thuộc Ủy ban Sản xuất ba bên, buộc phải dùng tư duy thiết kế IP thế kỷ 21 cải tổ toàn diện cấu trúc đồ chơi và nhịp phân cảnh để đập tan nguy cơ bị hủy bộ truyện cùng án phạt bồi thường 1,2 triệu yên.

- **Trục:** Trục **Media Mix & Ủy ban Sản xuất (製作委員会)**: Cuộc chiến ba bên giữa Tác giả Manga — Hãng sản xuất Đồ chơi — Đài truyền hình, nơi trang truyện là ngòi nổ thương mại kích hoạt toàn bộ chuỗi sản xuất công nghiệp và doanh số đồ chơi ngoài đời thật.
- **Bàn tay vàng:** Không hệ thống; kiếp trước là giám đốc mỹ thuật kiêm tổng giám chế IP đồ chơi/media mix chết năm 2024, mang theo kinh nghiệm về module hóa đồ chơi, tâm lý bóc hộp của trẻ em và kỹ thuật phân cảnh điện ảnh.
- **Bộ mẫu:** `../我在泡沫东京画漫画.txt` (440.232 chữ Hán). Đích đo sẵn: phủ định lặp 1,39/1.000 字, so sánh người kể 0,114, khuôn 实 0,034, nhãn ngữ điệu 0,030, thẻ thoại 1,329, lượt cụt 6,401.
- **Khung brief:** Mẫu A (`../.claude/skills/novel-craft/templates/brief-doan.md`), qua cổng `tools/soat_brief.py`.

## Writer

- SI đang dùng: `gemini/system-instruction-v1.md` — phần dán **7.849 ký tự** (`dung_si.py`), 4 anchor nguyên văn từ các chương 14, 21, 10, 22 của bộ mẫu (khác hoàn toàn 1994, 1998, 2000), `verify_anchors.py` khớp 4/4; `anchor字` = 689 ký tự (9% phần dán ≤ 15%); PART 2 = 6 dòng (≤ 8); BANS đúng 5 dòng; neo độ dài câu 22–30 字. Bản dựng: `gemini/si-dan-gemini.txt`.
- Khác biệt so với ba truyện cũ: Genre context là **Media Mix đồ chơi 1996 + Ủy ban Sản xuất ba bên**; các dòng PART 2 về thử nghiệm mẫu cơ khí, quan sát phản ứng đối diện qua bàn họp, động tác vật lý (kìm bấm, bánh răng, phôi nhựa ABS); anchor không trùng lặp với bất kỳ truyện nào trước đó.
- Lỗi riêng để soát: `gemini/review-blacklist.md`.

## Trạng thái

| Đoạn | Brief | Bản thảo | Số chữ (字) | Review | Trạng thái |
|---|---|---|---|---|---|
| 001 | `briefs/doan-001.md` (chốt từ bản c) | `chapters/doan-001.md` | 2.176 字 | `reviews/doan-001.md` | ✅ ĐẠT (0 nhãn, 0 实, 25.9 字/câu) |
| 002 | `briefs/doan-002.md` | `chapters/doan-002.md` | 2.545 字 | `reviews/doan-002.md` | ✅ ĐẠT (0 nhãn, 0 实, 29.9 字/câu) |
| 003 | `briefs/doan-003.md` | `chapters/doan-003.md` | — | `reviews/doan-003.md` | Chờ |
