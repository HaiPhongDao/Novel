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

## 26/10/2026 (tiếp) — viết lại từ đầu: SI v4 + prompt kiểu Tác giả

- Tác giả chê 002-a (thoại nào cũng kết bằng `说道`, mất giọng người xuyên việt), yêu cầu sửa SI/prompt và viết
  lại từ đầu với prompt kiểu đặt hàng của Tác giả + dữ kiện.
- SI v4 (Tác giả yêu cầu): đổi 4 câu về thẻ thoại và hạn mức giọng tính toán của MC. Bản cũ: `gemini/system-instruction-v3.md`, `gemini/si-dan-gemini-v3.txt`.
- Bản 001 a–e và 002-a chuyển vào `chapters/archive/`; brief cũ vào `briefs/archive/`. Brief mới `briefs/doan-001.md`.
- `001-i`: 2.064 字 · 1 thẻ thoại (002-a: 15) · ~10 câu phán xét cũ/mới · SỬA NHẸ. Bảng số: `reviews/doan-001.md`.
- Chi tiết mới Writer đặt, chờ Tác giả: kiếp trước Ronan học "đại học nông nghiệp bảy năm".

## 26/10/2026 (tiếp) — bản j: một tình huống, dữ kiện làm bối cảnh

- Tác giả chê 001-i tả/kể quá ít, checklist theo dữ kiện. Prompt mới (`briefs/doan-001.md`): ba dòng Tác giả +
  một tình huống + "bối cảnh để giữ cho đúng, không cần kể hết" + dừng sớm (Ronan cầm chai 圣水 vào nhà Marta).
  Prompt 001-i cất ở `briefs/archive/doan-001-tac-gia-du-kien.md`. SI giữ v4.
- `001-j`: 3.092 字 · 19 đoạn kể ≥40 字 (i: 0) · SỬA NHẸ, sửa tay 4 chỗ canon. Writer tự đặt cách dùng chai 圣水
  làm "giấy phép" (rót thuốc vỏ liễu vào chai) — đề xuất nhận vào canon.
- Dàn ý: đêm chữa bệnh và giấy dán cửa chuyển sang đoạn 002 (chia đoạn, không đổi chương/sự kiện).
- Chờ Tác giả: 40 经验 sau 40 ngày vs 5–8 经验/ngày công trong glossary.

## 26/10/2026 (tiếp) — SI v4.1 + bản k; sửa extension treo khi bị từ chối quyền

- Tác giả bắt lời thoại khó chịu của Ronan với Marta (bản j). SI v4.1: câu ngầu chỉ nhắm người có quyền; với
  người đang sợ/đau thì đáp đúng điều họ nói rồi mới ra lệnh, lời phán để ở lời kể. Bản cũ: `gemini/system-instruction-v4.md`, `gemini/si-dan-gemini-v4.txt`.
- `001-k` (cùng prompt j): 2.467 字, 0 thẻ, 0 nhãn, cham 78; lời với Marta đỡ hơn nhưng còn 2/5 lượt là lời phán.
  Giả thuyết: dòng "Mượn lời của MC" đẩy câu phán ra miệng — chờ Tác giả duyệt đổi câu.
- Tác giả báo extension treo khi tài khoản bị permission deny → sửa `tools/aistudio-ext` (đọc lỗi trong lượt Model,
  xoay /u/ kế tiếp, thôi chờ khi request xong mà không có chữ). Edge nạp extension từ `D:\ClaudeCode\aistudio-ext` →
  đã chép bản mới sang (bản cũ: `D:\ClaudeCode\aistudio-ext.bak-2026-10-26`).

## 26/10/2026 (tiếp) — bản l: bỏ SI v4.1, đổi dòng chức năng giọng

- Tác giả: k không đạt, lỗi vặt văn phong, kém j → bỏ SI v4.1 (giữ file `-v4.1` làm bằng chứng), SI đang dùng
  trở lại **v4**. Prompt `briefs/doan-001.md`: "Mượn lời của MC" → "Mượn suy nghĩ của MC và lời người kể" (Agent
  đổi câu của Tác giả theo khuyến nghị đã nêu; Tác giả bảo "chạy lại đi").
- `001-l`: 2.886 字 · lỗi vặt 2 (k: 11) · 0 câu phán nói ra miệng · câu ngắn hơn j. SỬA NHẸ. Chờ Tác giả chọn j hay l.
- Đề xuất SI: `神父大人` ra ở cả j, k, l dù prompt ghi "gọi 神父 là 神父" — thêm một dòng xưng hô vào FIXED
  CONVENTIONS của SI (chờ Tác giả duyệt).
