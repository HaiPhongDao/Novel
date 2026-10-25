## Bản D — đoạn 002 — prompt v4 (cửa sổ 2.000–3.000 字, dòng thân phận, quyền lực trong cảnh)

Luật mới của Tác giả (26/10): **không sửa độ dài nếu không trượt văn phong; 2.000–3.000 字 là khoảng không
trượt**. Đã ghi vào `README.md`, con số nằm trong prompt, SI không có trần.

Chạy **tiếp session của bản H** (không `--new`), SI v9, prompt `briefs/doan-002-v4.md`, 117s, **2.372 字**.

| số đo | bản D | H (đoạn 001) | mẫu |
|---|---|---|---|
| 字/câu | 24,5 | 21,2 | 21,2 |
| lượt thoại · 字/lượt | 19 · **33,5** | 21 · 28,5 | ~20 · 22,4 |
| phủ định lặp · 既…也 · 实 · nhãn · thẻ thoại | 2·1·0·0·6 | 6·0·0·2·11 | — |

`cham_doan.py`: **70/100** — **văn 34/34** (0 `实`, 0 nhãn ngữ điệu, 0 từ hiện đại), nhịp 36/56, canon 0/10
(chấm theo register mặc định; xem dưới).

**Số khớp toàn bộ, kiểm bằng máy:** 500 − 3 = 497; 13 × 800 − 7 × 1.000 = 3.400 斤; 3.400 / 1.000 = 3,4 ngày;
24 × 3 = 72 cây/ngày → 120 cây cần 2 ngày; 43 火头 × 7–8 = 301–344 ≈ 300; 20 金币; 60 步. Bảng in đúng
nguyên dạng 4 dòng, 士气 22/100.

**Những chỗ Writer tự làm tốt:** Karl báo cáo đúng kiểu "tin trước, số sau, ý kiến sau cùng" (ba lượt liền:
đến nơi → sổ sách → đề nghị dựng bếp); lão binh có chuyện ngoài việc thật (`婆娘和两个娃` · `后槽牙崩掉了两颗` ·
`兽人箭伤的右腿`); 代守 có lý lẽ riêng và thắng cuộc (`公粮？狗屁的公粮！` + 半年 không lĩnh được lương);
Adrian thua đúng thế — hắn không có quân lệnh, không có vàng, và bản thảo nói ra điều đó.

**Sáu chỗ cần quyết (chưa sửa tay):**

| # | chỗ | vấn đề |
|---|---|---|
| 1 | `爵士` ×2 (代守 gọi Adrian) | ngoài glossary: `爵士` dành cho kỵ sĩ **có đất**; Adrian không đất, người dưới gọi `少爷` |
| 2 | `小的` = 0 | register người hầu/lính vẫn chưa vào văn; SI v9 không có luật này |
| 3 | `那是两年前山体滑坡压塌的东墙…七天过去了，依旧没人搬动过一块石头` | mâu thuẫn thời gian trong cùng một câu (两年前 ↔ 七天) |
| 4 | `削去枝权` | lỗi chữ, phải `枝杈` |
| 5 | so sánh người kể 3 chỗ: `像是一群瑟瑟发抖的灰耗子` · `像是一个张开的大嘴` · `寒风如野兽般呼啸` | tool báo 0; đúng như cảnh báo regex bỏ sót `像…`/`如…般` |
| 6 | phủ định: `既没有单膝下跪，也没有行军礼` · `没有能调动…军令，也没有多余的金币…管不到…` | hai câu phủ định song song, cách nhau 9 dòng |

**Ghi chú canon:** 代守 dẫn 40 lão binh **rời thành ngay trong đoạn này**, nên tuyến "40 người biết tường" đã
đóng — đoạn 003 phải tính lại: không còn ai trong thành ngoài 497 nông nô + Karl + Cole. Đây là hệ quả của
prompt v4 (không yêu cầu giữ họ lại), không phải Writer tự bỏ.
