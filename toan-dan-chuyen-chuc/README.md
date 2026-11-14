# Toàn Dân Chuyển Chức (tên tạm)

> Võng du / toàn dân chuyển chức: MC xuyên việt tới thế giới mười tám tuổi chuyển chức, quái thú hoành hành, cày phó bản lên cấp; nghề khởi đầu bị coi thường, dựa vào bàn tay vàng mà thăng cấp, kiếm tiền, vả mặt. Làm theo [`../QUY-TRINH.md`](../QUY-TRINH.md): brief trần, Writer tự quyết; canon ghi theo điều Writer đã viết.

- **Bộ mẫu:** 《全民转职：我神器词条无限叠加》 (飞雪连夭). Không commit (3,7 MB): bản trên máy ở `mau/`, bản gốc trong lịch sử git `3b9d02d:vong-du/全民转职：我神器词条无限叠加.txt` (nhánh `vong-du`, tải lên 27/10) — script tự lấy từ đó khi thiếu file.
- **SI đang dùng:** [`gemini/si-dan-gemini.txt`](gemini/si-dan-gemini.txt) (5.031 ký tự, 72% nguyên văn bộ mẫu), dựng bằng `python toan-dan-chuyen-chuc/gemini/dung_si.py`. Khung SI Claude như `lanh-chua-chung-dien`: lời tiếng Trung, Writer làm chính tác giả bộ mẫu, mười một thói quen viết dạng "làm thế này", không BANS, một dòng nêu nhóm chữ nhấn. Bảy anchor cắt bằng script từ ch1–4, ch8: thế giới vận hành ra sao · MC từ 地星 tới, trong tay có gì · đám đông xem thường rồi bảng 【】 bật ra · luật chơi nói đúng lúc · xem bảng thần khí, tính ngay mạnh gấp mấy · tiêu tiền tính sổ · đám đông bàn tán, bia kỷ lục vả mặt.
- **Chạy đoạn:** `python tools/lam.py viet toan-dan-chuyen-chuc <N>` (hoặc `ban` để viết ba bản rồi chấm theo skill `novel-taste`).
- **Brief:** 001 ba dòng ([`briefs/doan-001.md`](briefs/doan-001.md), bản đề xuất); từ 002 là `Viết tiếp đoạn tiếp theo, khoảng 2.500 字, bằng tiếng Trung.` cộng tối đa một câu hướng đi.

## Việc kế

1. Tác giả duyệt (hoặc sửa) dòng 3 của brief 001: MC là ai, đang kẹt chuyện gì.
2. Bài hiệu chuẩn (QUY-TRINH mục 5): `lam.py ban toan-dan-chuyen-chuc 1` → hai bản, Tác giả nghe. Tối đa 2 vòng.
3. Ghi canon theo bản được chọn vào `handoff/canon-card.md`, rồi vào làn sản xuất.

## Trạng thái

| Đoạn | Prompt | Bản thảo | Review | Chốt |
|---|---|---|---|---|
| 001 | [`briefs/doan-001.md`](briefs/doan-001.md) (đề xuất) | — | — | — |
