# Review đoạn 002

## Bản a — đoạn 002

- Gốc: nối từ `chapters/doan-001-e.md` (001 chưa chốt; e là bản duy nhất đã sửa hết lỗi canon và theo đúng prompt ngắn).
- Brief: `briefs/doan-002.md` (khối 【接上】 5 dòng cuối 001-e + khối nối tiếp + luật + số + bảng + người có mặt + xưng hô + chỗ dừng).
- SI: `gemini/si-dan-gemini.txt` (v3, A+B). Writer: Gemini 3.8 Flash, Thinking High, chat mới, /u/1, 274 s.
- Cổng `tools/cong_doan.py`: XANH (không cụt, không chép mẫu/đuôi).

| bản | 字 | 字/câu | lượt · 字/lượt | phủ định | 实 | nhãn | so sánh | thẻ | cham |
|---|---|---|---|---|---|---|---|---|---|
| 001-e (mốc) | 1.868 | 20,1 | 16 · 17,5 | 1 | 0 | 0 | 0 | — | 72 |
| 002-a | 1.652 | 18,6 | 15 · 17,2 | 1 | 0 | 0 | 0 (tool) / 2 (tay) | 15 | 72 |

Nhịp câu (`do_nhip_cau.py`): 18 câu ≤5 字, 15% mệnh đề cụt — "câu vụn, câu trượt dài" (001-e: 15 câu ≤5 字, 11%).

### Canon & nhất quán
- ✅ Số: 27 蒲式耳 = 18 银币; Ronan nộp 2 银币, còn 1 银币 7 铜币; 5 亩 × 3 = 15, cần 6/亩; bảng 经验 74 in đúng khối.
- ✅ Luật trang viên: lấy đất trước, ba người đi mỏ; tên Ronan vào sổ, không được rời làng tới mùa xuân.
- ✅ Xưng hô: Ronan tự xưng 小的 với 管事 (đúng `bible/characters/ronan.md`).
- ⚠️ (đã sửa tay) `这点经验离进阶还差二十六点` — 进阶 sai: 74/300 còn xa bậc 2; 26 là phần thiếu để **đào tạo 村民** (100) → `离训练头一个村民还差二十六点`.
- ⚠️ (đã sửa tay) `但大人需批` → `但管事大人需批` (glossary: 管事大人).
- ⚠️ Ronan 21 tuổi bị gọi `少年` ×3 và `你这娃`; `原主在地里泡了大半辈子` lệch tuổi. Để nguyên, ghi vào blacklist riêng.
- ⚠️ Ronan đổ lúa vào đấu rồi lại nộp 2 银币 — hai cách nộp chồng lên nhau, đọc không rõ anh nộp bằng gì.
- ⚠️ `按市价` — canon là 官价 của trang viên.

### Cốt truyện
- ✅ Mở bằng một việc ở đống phân, nối liền chỗ dừng 001; nhảy hai ngày; đúng hai cảnh.
- ✅ Burchard giữ quyền, tự tính lợi hại (庄园 không lỗ), đặt điều kiện của mình; Marta mở lời trước cho cả làng.
- ✅ Dừng đúng chỗ: Osric báo thư lên 圣廷 vì Marta kể chuyện nồi vỏ liễu, 半月后 người tới.
- ⚠️ Điểm nhìn trượt vào đầu Burchard ba câu (`管事心里飞快拨打着算盘…`).

### Văn phong
- ⚠️ Mỗi lượt một thẻ `X 说道`, và cùng một người nói 2–3 lượt liền nhau, lượt nào cũng gắn thẻ (Burchard 54–55, Ronan 75–76, Osric 105–107) — lời bị chẻ thành lượt ngắn, đọc như biên bản. Cùng tật 17,5 字/lượt của 001-e: hệ quả đã biết của việc bỏ dòng đếm lượt.
- ⚠️ So sánh người kể tool bỏ sót: `字迹如同一道铁锁`, `金子般粮食`.
- ⚠️ Người kể giảng cơ chế ủ phân/苗床 (dòng 8, 20–21) và phán một câu (`对他这具单薄身板而言已是最好结局`).

**Kết luận: SỬA NHẸ.** Mạch, số và hook đều đúng; hai lỗi canon đã sửa tay (bản Writer nguyên văn ở
`archive/doan-002-a-raw.md`). Chỗ yếu là hình dạng thoại (thẻ lặp, lượt chẻ) — thuộc tầng SI/brief, không sửa
bằng tay. Nếu Tác giả muốn thoại dày hơn: mở phạm vi cảnh / thêm người có mặt, không thêm lại dòng đếm lượt.
