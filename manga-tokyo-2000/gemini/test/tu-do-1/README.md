# Test "Writer tự do" (Tác giả 29/10)

Tác giả chạy SI v1 với prompt duy nhất "Viết đoạn mở đầu cho truyện mới khoảng 2000 chữ" → `doan-001.md`, thấy rất tốt. Lô này: mỗi đoạn sau chỉ có "Viết tiếp đoạn tiếp theo, khoảng 2000 chữ" + State + ~2.500 chữ cuối đoạn trước, chat mới mỗi đoạn (`chay.py`). Agent không viết dàn ý, không viết brief; chỉ cập nhật State theo đúng chữ Writer đã viết.

- `doan-002.md` … `doan-005.md`: State dạng **JSON** (`prompt-00N.md`). `state.json` là bản sau đoạn 004.
- `doan-002-md-a.md`, `doan-002-md-b.md`: cùng đoạn 002, State sau 001 (`state-001.json`) đổi sang **markdown** bằng `tools/state_md.py` (`state-001.md`, `prompt-002-md.md`). Tác giả nghi khối JSON kéo Writer sang chế độ code.
- `state.md`: State hiện tại (sau 004) dạng markdown.

## Số (`python ../vong-mau-1/do.py …`)

| bản | State | chữ Hán | câu | chữ/câu | lượt thoại | chữ/lượt | thoại | so sánh/1000 |
|---|---|---|---|---|---|---|---|---|
| 001 (Tác giả) | — | 2.814 | 113 | 24,9 | 11 | 15,5 | 6% | 1,78 |
| 002 | JSON | 4.481 | 222 | 20,2 | 41 | 17,4 | 16% | 1,79 |
| 002-md-a | markdown | 3.286 | 156 | 21,1 | 27 | 17,6 | 14% | 3,35 |
| 002-md-b | markdown | 3.317 | 170 | 19,5 | 26 | 13,1 | 10% | 0,60 |
| 003 | JSON | 3.922 | — | 20,6 | 62 | 25,1 | — | — |
| 004 | JSON | 3.462 | — | 22,3 | 57 | 17,0 | — | — |
| 005 | JSON | 3.419 | — | 20,3 | 20 | 12,7 | — | — |

Bản markdown ngắn hơn bản JSON khoảng 1.200 chữ (hai bản markdown sát nhau: 3.286 / 3.317); hướng truyện như nhau (đi tàu → 集英社 → biên tập đọc 《消失的四十分钟》 bị choáng). Mới n=1 bản JSON so với n=2 bản markdown, chưa đủ để kết luận về chất lượng — Tác giả đọc.

## Lỗi Writer tự đặt (ghi vào `conflicts`)
- 001 mưa 梅雨 trong khi là tháng Mười; kiếp trước "mười mấy năm" (001) vs "hai mươi năm" (003); tiền thưởng nhận "giữa tháng sau" (002) vs "thứ Năm tuần sau" (003).
- 002-md-a: 3×500 + 4×100 + 10 yên Writer cộng ra 910 (đúng là 1.910).
- Biên tập mỗi bản một tên (Sasai / Yamashita / Sasagawa) vì 001 chưa có ai ở 集英社.
- Cảnh "vẽ cực nhanh, cả phòng sững sờ" lặp ở 001 và 004.
