# Log — 《我在西幻种地，把法师饿死了》

## 26/10/2026 — mở truyện

- Tác giả chốt thể loại: **tây huyễn, mở đầu hưu nhàn làm ruộng, MC xuyên việt dùng kiến thức hiện đại
  giảm chiều không gian đả kích**.
- Chỉ định lấy SI của `ky-kham-lanh-chua` (link Tác giả gửi trên GitHub) làm SI cho truyện mới.
- Dựng `bible/` (overview, world, glossary, 4 nhân vật), `plot/arcs.md` (黄金三章), SI v1, brief đoạn 001.
- **Khác biệt so với SI gốc, có chủ ý:** bỏ PART 4 骑砍面板 (truyện không có hệ thống/bảng) → thay bằng khối
  "kiến thức mang theo"; cắt hai dòng bảng trong anchor 4 và hai bullet PART 2 nói về 【】; đổi tên ví dụ sang
  canon mới. Lý do: nếu giữ bảng 骑砍 thì bàn tay vàng thành hệ thống, ngược với tiền đề. Chờ Tác giả duyệt.
- Chưa chốt: tên tiền (đang dùng 金币/银币/铜币, 1 银币 = 12 铜币), tên truyện chính thức.

## 26/10/2026 (tiếp) — Tác giả chốt thêm hệ thống

- Tác giả: *"nhớ thêm hệ thống dạng điểm kinh nghiệm như này để MC cày cuốc nhé. MC có thể dùng điểm kinh
  nghiệm để đào tạo dân"* → SI v2: PART 4 đổi thành **bảng việc** (宿主 / 技能 / 村民 / 士气 / 人数上限 /
  经验). 经验 kiếm bằng lao động (ngày công 5–8, đêm trắng 8–12, cứu người 20, sói/kẻ cướp 9), tiêu bằng
  đào tạo 村民 (一阶 100 经验 + ba ngày lương; 二阶 300). Bảng in `【】`, không nói.
- Tác giả yêu cầu **prompt đơn giản** → `briefs/doan-001.md` viết lại thành bản ngắn (~250 từ): bối cảnh +
  một đoạn sự việc + cái giá + danh sách số + một khối bảng + một dòng xưng hô + chỗ dừng. Bản chi tiết
  đánh số cảnh giữ ở `briefs/archive/`.
- Ba bản đoạn 001: `a` (SI v1, brief chi tiết) 2.170 字 · `b` (SI v1b, brief chi tiết) 1.695 字 ·
  `c` (SI v2 có bảng, brief ngắn v1) 1.244 字 · `d` (SI v2.1, brief ngắn v2 đích 1.900) 2.138 字 ·
  15 lượt thoại · 25,9 字/lượt · 0 so sánh người kể · 0 nhãn · cham 78. Bảng số ở `reviews/doan-001.md`.
- Kết luận tạm: prompt ngắn chạy tốt hơn brief đánh số cảnh; tật còn lại của `d` (người kể giảng cơ chế và
  giảng bảng, `神父大人`) thuộc tầng SI + sửa tay, chưa chốt.
- Bản `e`: brief ngắn v3 (~200 từ), **bỏ dòng đếm lượt thoại** theo yêu cầu Tác giả → 1.868 字 · 20,1 字/câu ·
  16 lượt/17,5 字/lượt · 1 phủ định · cham 72. Sửa tay 3 chỗ (Piet 10→7 tuổi, Ronan tự xưng `小的`→`我`,
  `淡淡答道`→`答道`) + chuẩn hoá dòng trống; bản Writer nguyên văn ở `archive/doan-001-e-raw.md`.

## 26/10/2026 (tiếp) — đổi tài khoản Writer + thí nghiệm prompt

- Acc `ohi.phong@gmail.com` (/u/0) hết quota; Writer chuyển sang `swenphong@gmail.com` (/u/1). Script đã có
  sẵn cơ chế xoay `/u/0 → /u/1 → /u/2` khi gặp Quota; state ghi `quota_account=0` cho hôm nay nên các lần
  `--new` sau tự thử /u/1 trước.
- Thí nghiệm prompt trong `gemini/test/`: `f` = prompt Tác giả (3 dòng), `h` = prompt Tác giả + 4 dòng dữ kiện.
  Số đo và 5 lỗi canon của `h` ở `reviews/doan-001.md` mục "Thí nghiệm prompt".
- Kết luận tạm: prompt kiểu đặt hàng (tag + chức năng giọng) sinh được giọng phán xét cũ/mới mà brief beat
  không sinh được; nhưng thiếu dữ kiện thì trôi canon, còn dữ kiện dạng danh sách số thì câu vụn.

## 26/10/2026 (tiếp) — SI v3, A+B cho đối thoại

- Tác giả duyệt A+B. SI v3: câu hỏi của MC mang dữ kiện + số (`一瓶圣水几个钱？`), câu từ chối nêu người
  trước mặt + lý do/số (`这钱我出不起`), thêm một bullet "lượt cầu–đáp đẩy một con số/điều kiện, một dòng đọc
  chen giữa hai lượt". SI 17.613 → 18.289 ký tự.
- Chạy lại đúng prompt `h` → `h2`: lượt ≤6 字 5 → 1, 字/lượt 13,8 → 17,5, câu hỏi rỗng 8 → 4, và cuộc thoại
  đổi tính chất (MC dùng 27 蒲式耳/3 蒲式耳 để bẻ 神父). Đổi lại: dài 3.004 字, 3 nhãn ngữ điệu mới, và một
  mâu thuẫn số do prompt thiếu tỷ giá (Marta có 80 铜币 mà kêu không có 2 银币).
- Bảng số + lỗi cụ thể: `reviews/doan-001.md` mục "A+B trên SI (v3)".

## 26/10/2026 (tiếp) — thử đoạn 002

- Tác giả: "Thử đoạn 02". 001 chưa chốt → nối từ `001-e` (bản duy nhất đã sửa hết lỗi canon, prompt ngắn).
- Brief `briefs/doan-002.md` theo dàn ý chương 2 (加压). Agent thêm chi tiết phụ (ghi log): Burchard cưỡi la,
  một người cầm sổ, hai lính mang giáo; thư của 神父 lên 圣廷 vì Marta kể khắp làng chuyện nồi vỏ liễu.
- `002-a` (SI v3, /u/1, 274 s): 1.652 字 · 18,6 字/câu · 15 lượt/17,2 字/lượt · 0 nhãn · cham 72 · cổng xanh.
  SỬA NHẸ: sửa tay `进阶` → đào tạo 村民 và `大人` → `管事大人`; bản Writer ở `archive/doan-002-a-raw.md`.
- Mâu thuẫn canon cần Tác giả chốt: `bible/characters/ronan.md` nói Ronan tự xưng 小的 với 神父/管事, nhưng
  review 001-e đã sửa `小的` → `我` khi nói với 神父. 002-a theo bible (小的 với 管事).
