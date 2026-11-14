# Nhà Thiết Kế Game (tên tạm)

> Đô thị · thế giới song song · làm game: người làm game xuyên sang một thế giới giống kiếp trước chín phần, riêng ngành game khác hẳn; dùng game và con mắt kiếp trước đi từ đáy lên thành nhà thiết kế game vĩ đại nhất. Làm theo [`../QUY-TRINH.md`](../QUY-TRINH.md): brief trần, Writer tự quyết; canon ghi theo điều Writer đã viết.

- **Bộ mẫu:** 《全能游戏设计师》, file [`../lam-game/全能游戏设计师.txt`](../lam-game/) (đã có trong repo). File mất chữ ở ch1, ch2, ch5; anchor tránh mấy chỗ đó.
- **SI đang dùng:** [`gemini/si-dan-gemini.txt`](gemini/si-dan-gemini.txt) (4.787 ký tự, 71% nguyên văn bộ mẫu), dựng bằng `python nha-thiet-ke-game/gemini/dung_si.py`. Khung SI Claude như `lanh-chua-chung-dien` / `toan-dan-chuyen-chuc`: lời tiếng Trung, Writer làm chính tác giả bộ mẫu, mười một thói quen viết dạng "làm thế này", không BANS, một dòng nêu nhóm chữ nhấn. Tám anchor cắt bằng script từ ch0–3, ch5–6: MC kiếp trước là ai · thế giới này khác ở đâu · vào nghề thế nào, MC đang khó ra sao · bàn tay vàng và tính tiền · liệt kê điều kiện trước khi làm game · luật trong nghề nói đúng lúc · giám khảo khinh trước · người trong nghề chơi tới nghiện mà vẫn nhìn ra cái hay.
- **Khác truyện `lam-game` cũ** (nhánh `lam-game`, chốt 001–010 bằng SI kiểu cũ): cùng bộ mẫu, đây là truyện mới chạy theo QUY-TRINH hiện tại.
- **Chạy đoạn:** `python tools/lam.py viet nha-thiet-ke-game <N>` (hoặc `ban` để viết ba bản rồi chấm theo skill `novel-taste`).
- **Brief:** 001 ba dòng ([`briefs/doan-001.md`](briefs/doan-001.md), bản đề xuất); từ 002 là `Viết tiếp đoạn tiếp theo, khoảng 2.500 字, bằng tiếng Trung.` cộng tối đa một câu hướng đi.

## Việc kế

1. Tác giả duyệt (hoặc sửa) dòng 3 của brief 001: MC là ai, đang kẹt chuyện gì.
2. Bài hiệu chuẩn (QUY-TRINH mục 5): `lam.py ban nha-thiet-ke-game 1` → hai bản, Tác giả nghe. Tối đa 2 vòng.
3. Ghi canon theo bản được chọn vào `handoff/canon-card.md`, rồi vào làn sản xuất.

## Trạng thái

| Đoạn | Prompt | Bản thảo | Review | Chốt |
|---|---|---|---|---|
| 001 | [`briefs/doan-001.md`](briefs/doan-001.md) (đề xuất) | — | — | — |
