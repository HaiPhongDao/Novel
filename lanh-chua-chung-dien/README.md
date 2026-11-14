# Lãnh Chúa Chủng Điền (tên tạm)

> Tây huyễn trung cổ, MC xuyên việt nhận một lãnh địa nghèo, khai hoang – thu thuế – chiêu người – diệt cướp. Làm theo [`../QUY-TRINH.md`](../QUY-TRINH.md): brief trần, Writer tự quyết; canon ghi theo điều Writer đã viết.

- **Bộ mẫu:** 《词条种田：从北荒领主到帝皇》 (去码头整点玉米饼), file `mau/词条种田-从北荒领主到帝皇.txt` (313 chương, không commit; bản gốc `D:/Claude/TieuThuyetAI/拆文库/领主种田/原文/原文.txt`).
- **SI đang dùng:** [`gemini/si-dan-gemini.txt`](gemini/si-dan-gemini.txt) (5.833 ký tự, 73% là nguyên văn bộ mẫu), dựng bằng `python lanh-chua-chung-dien/gemini/dung_si.py`. Khung SI Claude như `manga-bong-bong` / `luu-dan`: lời tiếng Trung, Writer làm chính tác giả bộ mẫu, mười một thói quen viết dạng "làm thế này", không BANS, một dòng nêu nhóm chữ nhấn. Bảy anchor cắt bằng script từ ch1, ch2–3, ch5, ch6: bàn tay vàng hiện bằng 【】 + điều kiện kế · MC từ đâu tới, vì sao nhận đất · người bên cạnh đoán MC · tính sổ "mua không bằng thu thuế" · trở mặt thu hàng · bảng hàng và giá chợ · mẹo nghề nông nói đúng lúc.
- **Chạy đoạn:** `python tools/lam.py viet lanh-chua-chung-dien <N>` (hoặc `ban` để viết ba bản rồi chấm theo skill `novel-taste`).
- **Brief:** 001 ba dòng ([`briefs/doan-001.md`](briefs/doan-001.md), bản đề xuất); từ 002 là `Viết tiếp đoạn tiếp theo, khoảng 2.500 字, bằng tiếng Trung.` cộng tối đa một câu hướng đi.

## Việc kế

1. Tác giả duyệt (hoặc sửa) dòng 3 của brief 001: MC là ai, đang kẹt chuyện gì.
2. Bài hiệu chuẩn (QUY-TRINH mục 5): `lam.py ban lanh-chua-chung-dien 1` → hai bản, Tác giả nghe. Tối đa 2 vòng.
3. Ghi canon theo bản được chọn vào `handoff/canon-card.md`, rồi vào làn sản xuất.

## Trạng thái

| Đoạn | Prompt | Bản thảo | Review | Chốt |
|---|---|---|---|---|
| 001 | [`briefs/doan-001.md`](briefs/doan-001.md) (đề xuất) | — | — | — |
