# Manga Bong Bóng (tên tạm)

> Đô thị Nhật Bản thập niên 90, nghề manga, MC xuyên qua. Làm theo [`../QUY-TRINH.md`](../QUY-TRINH.md): brief trần, Writer tự quyết; canon ghi theo điều Writer đã viết.

- **SI đang dùng:** [`gemini/si-dan-gemini.txt`](gemini/si-dan-gemini.txt), dựng bằng `python manga-bong-bong/gemini/dung_si.py` từ bộ mẫu 《我在泡沫东京画漫画》: bảy đoạn nguyên văn (có khối bối cảnh thời đại, đoạn MC từ đời sau tới, đoạn "quân bài trong tay"), tên người trong anchor đổi sang Romaji.
- **Chạy đoạn:** `python tools/lam.py viet manga-bong-bong <N>` (hoặc `ban` để viết ba bản rồi chấm theo skill `novel-taste`).
- **Brief:** 001 ba dòng; từ 002 là `Viết tiếp đoạn tiếp theo, khoảng 2.500 字, bằng tiếng Trung.` cộng tối đa một câu hướng đi.

## Việc kế

Tác giả nghe đoạn 001 rồi quyết viết tiếp hay đổi. Chưa viết 002, 003 (Tác giả dặn 11/11).

## Trạng thái

| Đoạn | Prompt | Bản thảo | Review | Chốt |
|---|---|---|---|---|
| 001 | [`briefs/doan-001.md`](briefs/doan-001.md) | [`chapters/doan-001.md`](chapters/doan-001.md) (3.837 字; lần 2, bản b trong hai bản nháp; lần 1 ở `archive/doan-001-v1.md`) | giám khảo `novel-taste`: b, tin 2 (ngang); đã sửa 10 chỗ tại chỗ | ⏳ chờ Tác giả nghe |
