# Lãnh Chúa Chủng Điền (tên tạm)

> Tây huyễn trung cổ, MC xuyên việt nhận một lãnh địa nghèo, khai hoang – thu thuế – chiêu người – diệt cướp. Làm theo [`../QUY-TRINH.md`](../QUY-TRINH.md): brief trần, Writer tự quyết; canon ghi theo điều Writer đã viết.

- **Bộ mẫu:** 《词条种田：从北荒领主到帝皇》 (去码头整点玉米饼), file `mau/词条种田-从北荒领主到帝皇.txt` (313 chương, không commit; bản gốc `D:/Claude/TieuThuyetAI/拆文库/领主种田/原文/原文.txt`).
- **SI đang dùng:** [`gemini/si-dan-gemini.txt`](gemini/si-dan-gemini.txt) (5.833 ký tự, 73% là nguyên văn bộ mẫu), dựng bằng `python lanh-chua-chung-dien/gemini/dung_si.py`. Khung SI Claude như `manga-bong-bong` / `luu-dan`: lời tiếng Trung, Writer làm chính tác giả bộ mẫu, mười một thói quen viết dạng "làm thế này", không BANS, một dòng nêu nhóm chữ nhấn. Bảy anchor cắt bằng script từ ch1, ch2–3, ch5, ch6: bàn tay vàng hiện bằng 【】 + điều kiện kế · MC từ đâu tới, vì sao nhận đất · người bên cạnh đoán MC · tính sổ "mua không bằng thu thuế" · trở mặt thu hàng · bảng hàng và giá chợ · mẹo nghề nông nói đúng lúc.
- **Chạy đoạn:** `python tools/lam.py viet lanh-chua-chung-dien <N>` (hoặc `ban` để viết ba bản rồi chấm theo skill `novel-taste`).
- **Brief:** [đoạn 001](briefs/doan-001.md) có điểm dừng ngay khi chuẩn bị bữa tối đầu tiên. Tên riêng trong chính văn viết bằng chữ Latin. Brief các đoạn sau cũng ghi sự việc cần đạt và điểm dừng của đoạn.
- **Soát bản Writer:** một sub-agent đánh dấu lỗi chữ, dùng từ khó nghe và mẫu câu theo [blacklist chung](../chung/review-blacklist.md). Một sub-agent khác sửa tại chỗ theo giọng của đoạn và ghi vị trí cùng câu trước/sau để Tác giả đối chiếu. Blacklist dùng ở bước soát.

## Việc kế

1. Đoạn 001 đã được Tác giả duyệt. [Bản đọc đoạn 001](doc/lo-001.md).
2. Tác giả nghe các bản đọc từ [002](doc/lo-002.md) đến [011](doc/lo-011.md). Rian chỉ đạo luyện kim và rèn 20 món quân giới, mở khóa 【百炼精钢】; trang bị giáo dài huấn luyện đội hình 20 người theo 【百战精锐】; dẫn toàn quân xuất kích cứu 50–60 nô lệ mỏ sắt đang bị bầy khủng lang 30 con truy đuổi.
3. Tiếp tục sản xuất các đoạn tiếp theo trong lô.

## Trạng thái

| Đoạn | Prompt | Bản thảo | Review | Chốt |
|---|---|---|---|---|
| 001 | [`briefs/doan-001.md`](briefs/doan-001.md) | [`chapters/doan-001.md`](chapters/doan-001.md) | Đã nghe | ✅ Chốt 14/11 |
| 002 | [`briefs/doan-002.md`](briefs/doan-002.md) | [`chapters/doan-002.md`](chapters/doan-002.md) | Chờ Tác giả nghe | — |
| 003 | [`briefs/doan-003.md`](briefs/doan-003.md) | [`chapters/doan-003.md`](chapters/doan-003.md) | Chờ Tác giả nghe | — |
| 004 | [`briefs/doan-004.md`](briefs/doan-004.md) | [`chapters/doan-004.md`](chapters/doan-004.md) | Chờ Tác giả nghe | — |
| 005 | [`briefs/doan-005.md`](briefs/doan-005.md) | [`chapters/doan-005.md`](chapters/doan-005.md) | Chờ Tác giả nghe | — |
| 006 | [`briefs/doan-006.md`](briefs/doan-006.md) | [`chapters/doan-006.md`](chapters/doan-006.md) | Chờ Tác giả nghe | — |
| 007 | [`briefs/doan-007.md`](briefs/doan-007.md) | [`chapters/doan-007.md`](chapters/doan-007.md) | Chờ Tác giả nghe | — |
| 008 | [`briefs/doan-008.md`](briefs/doan-008.md) | [`chapters/doan-008.md`](chapters/doan-008.md) | Chờ Tác giả nghe | — |
| 009 | [`briefs/doan-009.md`](briefs/doan-009.md) | [`chapters/doan-009.md`](chapters/doan-009.md) | Chờ Tác giả nghe | — |
| 010 | [`briefs/doan-010.md`](briefs/doan-010.md) | [`chapters/doan-010.md`](chapters/doan-010.md) | Chờ Tác giả nghe | — |
| 011 | [`briefs/doan-011.md`](briefs/doan-011.md) | [`chapters/doan-011.md`](chapters/doan-011.md) | Chờ Tác giả nghe | — |
