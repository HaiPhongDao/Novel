# manga-tokyo-2000 — 我在千禧东京画漫画

**Logline:** Tháng 10/2000 tại Tokyo, thời điểm chuyển giao thiên niên kỷ và bùng nổ internet ADSL, Hayakawa Ryo — một người xuyên việt mang theo tư duy phân cảnh điện ảnh đời sau, nhập vào chàng trai làm ca đêm quán manga café đang nợ tiền phòng trọ và 7 lần trượt bản thảo — tìm thấy cơ hội ở chỗ trống 32 trang one-shot của bán nguyệt san thanh niên 《青年世纪》, hợp tác cùng nữ biên tập viên tân binh Morishita Chinatsu đang đứng trước nguy cơ bị giáng chức.

- **Trục:** Cách mạng phân cảnh điện ảnh (电影级分镜) & giật gân hiện đại, phá vỡ khuôn mẫu Showa/Heisei cũ, sinh tồn bằng phiếu bầu điều tra độc giả của tạp chí thanh niên.
- **Bàn tay vàng:** Không hệ thống; kiếp trước là chuyên gia storyboard / phân cảnh điện ảnh, mang theo tư duy thị giác và nhịp cắt cảnh đời sau, tay vẽ của thân xác ở mức khá.
- **Bộ mẫu:** `../我在泡沫东京画漫画.txt` (214 chương, trung bình 2.045 字/chương, lời kể 80,1% / thoại 19,9%, câu kể 22,0 字, thẻ thoại/lượt 0,10).
- **Khung brief:** Mẫu A (`../.claude/skills/novel-craft/templates/brief-doan.md`), qua cổng `tools/soat_brief.py`.

## Writer

- SI đang dùng: `gemini/system-instruction-v1.md` — dựng từ `writer/SI-template` v5, phần dán 7.9xx ký tự, 4 anchor nguyên văn từ chương 7, 30, 25, 10 của bộ mẫu, `verify_anchors.py` 4/4 khớp, `soat_van.py` sạch. Bản dán: `gemini/si-dan-gemini.txt`.
- Khác biệt so với `manga-tokyo-1994` và `manga-tokyo-1998`: Genre context là thị trường tạp chí thanh niên năm 2000 (chuyển giao thiên niên kỷ, internet ADSL sơ khai, khủng hoảng tạp chí giấy trước đa phương tiện); anchor lấy từ các chương khác để tránh trùng lặp; quy ước tên Latin trong văn Trung.
- Lỗi riêng để soát: `gemini/review-blacklist.md`.

## Bảng trạng thái từng đoạn

| Đoạn | Brief | Bản thảo | Số chữ (字) | Review | Trạng thái |
|---|---|---|---|---|---|
| 001 | `briefs/doan-001-b.md` (chốt từ 3 bản) | `chapters/doan-001.md` | 2.917 字 | `reviews/doan-001.md` | ✅ ĐẠT |
| 002 | `briefs/doan-002.md` | `chapters/doan-002.md` | 2.244 字 | `reviews/doan-002.md` | ✅ ĐẠT |
| 003 | `briefs/doan-003.md` | `chapters/doan-003.md` | — | `reviews/doan-003.md` | Đang chạy |
