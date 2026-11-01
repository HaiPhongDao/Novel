# manga-tokyo-2000 — 我在千禧东京画漫画

**Logline:** Tháng 10/2000 tại Tokyo, thời điểm chuyển giao thiên niên kỷ và bùng nổ internet ADSL, Hayakawa Ryo — một người xuyên việt mang theo tư duy phân cảnh điện ảnh đời sau, nhập vào chàng trai làm ca đêm quán manga café đang nợ tiền phòng trọ và 7 lần trượt bản thảo — tìm thấy cơ hội ở chỗ trống 32 trang one-shot của bán nguyệt san thanh niên 《青年世纪》, hợp tác cùng nữ biên tập viên tân binh Morishita Chinatsu đang đứng trước nguy cơ bị giáng chức.

- **Trục:** Cách mạng phân cảnh điện ảnh (电影级分镜) & giật gân hiện đại, phá vỡ khuôn mẫu Showa/Heisei cũ, sinh tồn bằng phiếu bầu điều tra độc giả của tạp chí thanh niên.
- **Bàn tay vàng:** Không hệ thống; kiếp trước là chuyên gia storyboard / phân cảnh điện ảnh, mang theo tư duy thị giác và nhịp cắt cảnh đời sau, tay vẽ của thân xác ở mức khá.
- **Bộ mẫu:** `../我在泡沫东京画漫画.txt` (214 chương, trung bình 2.045 字/chương, lời kể 80,1% / thoại 19,9%, câu kể 22,0 字, thẻ thoại/lượt 0,10).
- **Khung brief:** Mẫu A (`../.claude/skills/novel-craft/templates/brief-doan.md`), qua cổng `tools/soat_brief.py`.

## Writer

- SI đang dùng: `gemini/system-instruction-v3.md` (**4.749 ký tự** phần dán, **2 anchor**, chiếm 43% phần dán).
  Bản dán: `gemini/si-dan-gemini.txt` (dựng bằng `python tools/dung_si.py manga-tokyo-2000`, đừng sửa tay).
- **Lịch sử đời SI** (phục hồi 01/11 từ git; trước đó hai lần viết lại không đổi tên file nên đời thật không có tên):
  | Đời | Ký tự | Ghi chú |
  |---|---|---|
  | v1 (`f118d09`) | 8.156 | dựng từ `writer/SI-template` v5, 4 anchor, đủ BANS + LENGTH + PART 3 |
  | v2 (`5f0e8e7`) | 2.773 | "tinh gọn": bỏ PART 2, BANS, LENGTH, PART 3 |
  | v3 (`6bccaa3`) | 4.749 | v2 + anchor dài (1.080/877 ký tự), 2 anchor chiếm 43% phần dán |
- **Nợ cấu trúc phải trả trước khi thêm luật** (`dung_si.py` đang trả mã thoát 1): 0 dòng BANS (khung đòi đúng 5),
  0 dòng PART 2, chỉ 2 anchor, và **mất neo độ dài câu** — `si-test-tren-mau.md` gọi đó là con số an toàn duy nhất
  nên có trong SI. Phục hồi cần Tác giả duyệt (bảng phân quyền `AGENT.md` §8).
- Khác biệt so với `manga-tokyo-1994` và `manga-tokyo-1998`: Genre context là thị trường tạp chí thanh niên năm 2000 (chuyển giao thiên niên kỷ, internet ADSL sơ khai, khủng hoảng tạp chí giấy trước đa phương tiện); anchor lấy từ các chương khác để tránh trùng lặp; quy ước tên Latin trong văn Trung.
- Lỗi riêng để soát: `gemini/review-blacklist.md`.

## Bảng trạng thái từng đoạn

| Đoạn | Brief | Bản thảo | Số chữ (字) | Review | Trạng thái |
|---|---|---|---|---|---|
| 001 | `briefs/doan-001-b.md` (chốt từ 3 bản) | `chapters/doan-001.md` | 2.917 字 | `reviews/doan-001.md` | ✅ ĐẠT |
| 002 | `briefs/doan-002.md` | `chapters/doan-002.md` | 2.244 字 | `reviews/doan-002.md` | ✅ ĐẠT |
| 003 | `briefs/doan-003.md` | `chapters/doan-003.md` | 2.227 字 | `reviews/doan-003.md` | ✅ ĐẠT |
