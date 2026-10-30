# manga-tokyo-1994 — Kẻ trở về từ năm 2024

**Logline:** Tháng 5/1994, hoạ sĩ tuần san Kisaragi Souta — người tỉnh dậy trong thân xác này sau khi chết ở tuổi 39
vào năm 2024 — bị toà soạn báo cắt truyện ngay tuần cuối của bộ truyện duy nhất anh có, và phải giành lại một chỗ
đứng bằng đúng thứ toà soạn đang coi thường: một bộ truyện đại chúng mà độc giả bỏ phiếu cho, không phải một tác
phẩm để ban giám khảo trao giải.

- **Trục:** sống sót bằng độ phổ cập (`顺位` của độc giả), không phải xin vào nghề bằng giải thưởng.
- **Bàn tay vàng:** không hệ thống; kiếp trước là hoạ sĩ manga Nhật chết năm 2024, mang theo ba mươi năm hậu kiến về
  nghề và thị trường, cùng một bàn tay chỉ ở mức khá của thân xác này. Không chép được tác phẩm nào — 1994 là Nhật
  thật, các hit đều có chủ.
- **Bộ mẫu:** `../我在泡沫东京画漫画.txt` (214 chương, trung bình 2.045 字/chương, trung vị 1.910; lời kể 80,1% /
  thoại 19,9%; câu kể trung bình 22,0 字; thẻ thoại/lượt 0,10 — số đo đầy đủ trong `../manga-tokyo-1998/README.md`,
  cùng bộ mẫu). Dùng chung số đo, **khác trục và khác loại tác phẩm trong truyện**.
- **Khung brief:** mẫu A (`../.claude/skills/novel-craft/templates/brief-doan.md`), qua cổng `tools/soat_brief.py`.

## Writer

- SI đang dùng: `gemini/system-instruction-v1.md` — phần dán **7.974 ký tự** (`len()`, `verify_anchors.py` báo 7.974),
  4 anchor nguyên văn từ chương 27, 16, 93, 11 của bộ mẫu, `verify_anchors.py` khớp 4/4; `soat_van.py` trên từng anchor
  sạch (A1, A2 = 0 tật; A3, A4 = 1 câu phủ định đơn trong lời thoại, giữ nguyên văn). Bản dán: `gemini/si-dan-gemini.txt`.
- Khác biệt so với SI của `manga-tokyo-1998` (cùng bộ mẫu): genre context là **thị trường tuần san 1994 + cuộc chiến
  mainstream với giải thưởng**; ba dòng PART 2 về đọc `分镜稿` trên giấy, động tác nhỏ trong cảnh làm việc, và hậu kiến
  không được kể thành tương lai; anchor lấy từ chương khác để giọng không trùng truyện cũ; bỏ anchor mục 5 (dùng 4 anchor).
- Lỗi riêng để soát: `gemini/review-blacklist.md`.

## Trạng thái

| Đoạn | Brief | Bản thảo | Số chữ (字) | Review | Trạng thái |
|---|---|---|---|---|---|
| 001 | `briefs/doan-001-c.md` (chốt từ 4 bản) | `chapters/doan-001.md` | 2.593 字 | `reviews/doan-001.md` | ✅ ĐẠT (sửa chính tả `覚書`) |
| 002 | `briefs/doan-002-b.md` (chốt từ 2 bản) | `chapters/doan-002.md` | 1.903 字 | `reviews/doan-002.md` | ✅ ĐẠT |
| 003 | `briefs/doan-003-c.md` (chốt từ 3 bản) | `chapters/doan-003.md` | 2.136 字 | `reviews/doan-003.md` | ✅ ĐẠT (ghi chú 2 so sánh + 2 nhãn) |
