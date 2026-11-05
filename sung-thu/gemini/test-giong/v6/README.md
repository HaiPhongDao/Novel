# v6 — đề xuất của Argon Gemini

Tác giả giao Argon Gemini prompt `sung-thu/prompt-argon.md` (chỉ vấn đề, ràng buộc, đã thử). Argon trả về chẩn đoán,
một SI và một brief chương 3; Tác giả dán lại cho Agent 05/11. SI và brief lưu **nguyên văn**:

- `si-argon.txt` — 7.630 ký tự: ROLE + FIXED (dấu câu mới: tiếng lòng trần ngoài “”) + mục 1 (lời kể từ trong đầu MC) +
  mục 2 (luật, giá, mánh đi bằng MC tính kèo) + mục 3 (thoại) + PART 2 + BANS 5 dòng + PART 3 + PART 4.
  4 anchor: ch2 (bói ra bò sữa, cá voi), ch30, ch35, ch11 — khớp nguyên văn (anchor ch2 khớp
  `chung/hieu-chuan/than-sung/ch02/goc.txt`; nguồn thô có dòng rác chen giữa).
- `brief-argon.md` — brief chương 3 viết lại: tách "Thiết lập đã biết", thêm dòng "Mở:", xưng hô mới. `soat_brief.py`:
  XANH (0 chặn, 0 cảnh báo).

Ghi để đọc kết quả cho đúng (sự thật, không phán): brief Argon chứa bản tiếng Việt của 8/8 câu đùa trong nguyên văn
chương 3 — 骗小孩呢 · 店方也不是慈善家 · 一分别想带回家 · 免费的才是最贵的 · 商人的心真黑 · 一虫传三代，人走虫还在 ·
几千条还他妈不够你挑？！来挑事的吧 · 可以和萦风虫坐一桌了. Brief gốc không có câu nào trong số đó.

| Bản | SI | Brief | Để biết |
|---|---|---|---|
| **X** | `si-argon.txt` | `brief-argon.md` | đề xuất của Argon, đúng như gửi |
| **S** | `si-argon.txt` | `chung/hieu-chuan/than-sung/ch03/brief.md` (brief gốc) | phần do SI |
| **B** | `sung-thu/gemini/si-dan-gemini.txt` (v1) | `brief-argon.md` | phần do brief |

Mỗi bản 2 lần, chat mới, thinking High.
