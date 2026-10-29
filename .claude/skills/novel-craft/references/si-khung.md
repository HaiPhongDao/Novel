# Khung SI — vì sao nó như vậy (mọi thể loại)

**Khung để chép là `writer/SI-template` v5** — một chỗ duy nhất định cấu trúc, ngân sách, số anchor, PART 2 và BANS.
File này giữ bằng chứng đằng sau khung; đừng dựng SI từ một bộ khung chép ở đâu khác. (Bản cũ của file này có hai bộ
khung riêng và khối BANS liệt kê từ, trái với template v4 "SI không có câu cấm" — ba tài liệu, ba luật; đã gộp 29/10.)

Tóm tắt khung v5: ROLE · FIXED CONVENTIONS · PART 1 (NARRATION 3 nguyên tắc + MOMENTS tối đa 2, mỗi nguyên tắc một
anchor nguyên văn + 1–2 câu "vì sao") · PART 2 tối đa 8 dòng · BANS đúng 5 dòng · LENGTH · PART 3 · PART 4 nếu có bàn
tay vàng. **Phần dán ≤ 8.000 ký tự, 4–5 anchor.**

## Vì sao phải có BANS — và vì sao BANS không liệt kê từ

SI chỉ viết nguyên tắc khẳng định thì model lấp chỗ trống bằng đúng mấy tật cũ: SI 骑砍 v1 (2.338 ký tự, 0 lệnh cấm)
ra `踩实` 1, so sánh 4, cụm bốn chữ 80. Nên khung có 5 dòng BANS. Nhưng hai cách viết BANS đã hỏng:

- **Liệt kê từ** — SI cũ cấm `眸子、一丝、系统` thì bản ra lại có đúng mấy chữ đó: chữ trong SI là mẫu để chép.
- **Báo cho Writer biết có máy soát** — SI test (`ky-kham-lanh-chua/gemini/test/test-gemini-moi/si.txt`) liệt kê từ
  và ghi "Checked by machine tools": 实 = 0 nhưng `整整/足足/死死/彻底` = 3,0/1.000 字 (mẫu ch.8: 0), `得像` = 0 nhưng
  có `风箱一般`, `语气平淡` = 0 nhưng ~15 thẻ kiểu `低声/急促地/颤声 + 说道`. Writer tối ưu cho regex, không cho văn.

Cách đúng: mỗi dòng nói **thứ đúng** trước (sức nặng nằm ở con số hoặc kết quả; so sánh thuộc nhân vật; ngữ điệu nằm
trong chữ), rồi mới nói lớp tật không có — gọi tên lớp, không gọi tên từ. Danh sách từ để bắt nằm ở
`chung/review-blacklist.md` cho Agent.

## Vì sao có ngân sách và trần anchor

- Template v4 chưa điền đã 12.300 ký tự phần dán; SI điền từ nó (ky-kham-lanh-chua v9) ra 15.000 ký tự, 7 anchor, 20 dòng
  PART 2. SI đã đo chạy tốt nằm ở 7.000–8.000 ký tự với 3 anchor (`si-anchors.md`); quá 9.000 là dấu hiệu luật tích tụ
  (`si-cau-truc.md` mục 10). Bản 12.000 ký tự vẫn chạy nhưng loãng chú ý và dễ sinh tật hình thức.
- 4–5 anchor: ít hơn 4 thì model quay về đọc nguyên tắc suông; nhiều hơn 5 thì loãng, và anchor nào cũng có thể bị
  bắt chước nguyên chi tiết.
- Mỗi lỗi bắt được từng thành một dòng PART 2 mới (template v4 mục 9 chỉ có đường thêm). v5 đặt trần 8 dòng và cổng:
  brief/glossary → review-blacklist → SI, dòng mới phải thay một dòng cũ.

## Lời kể phải có nguyên tắc riêng — và đứng trước

Lời kể chiếm 70–85% mọi đoạn (bộ 全民转职 mẫu 68–72%, ba bản thử chuyen-chuc 75–87%). Nếu nguyên tắc chỉ dạy cảnh đặc
biệt (trận đánh, mua bán, bia kỷ lục) thì **không nguyên tắc nào dạy giọng người kể**, Writer lấp bằng giọng báo cáo —
mỗi dòng một sự kiện kèm số — và thoại nhiễm theo thành lời kể trong ngoặc kép (chuyen-chuc SI v1, Tác giả chê; thêm
anchor thoại chỉ đổi vài lượt). Vì vậy v5 có 3 nguyên tắc NARRATION bắt buộc, mỗi cái một anchor thuần lời kể, đứng
trước MOMENTS.

- Đo tỷ lệ lời kể / thoại / hệ thống của sample trước khi viết SI.
- Cắt SI thì cắt MOMENTS và PART 2 trước; nguyên tắc người kể là phần mang giọng thể loại. Bản "tinh gọn" của test
  test-gemini-moi cắt đúng nguyên tắc người kể của v9 mà giữ luật đếm cỡ đoạn — giọng sổ kép biến mất ở cả 5 đoạn.

## Vì sao phải có giọng người kể gắn với MC (bằng chứng)

SI 骑砍 v3 đủ 4 nguyên tắc + 5 lệnh cấm, tật về 0, nhịp khớp mẫu — mà Tác giả đọc xong nói: *"như người ngoài cuộc kể
chuyện, không nhập cảm với MC"*. Bản đó tả bảy đội trưởng, tả mặt kỵ sĩ *"脸皮涨得通红，硬生生把反驳的话咽了回去"* (vào
đầu người khác), và có nguyên một đoạn tableau không có MC trong đó. Thêm khối POV + một dòng trong prompt ("ở mỗi quyết
định, một câu tính toán của hắn") thì bản sau mở bằng bàn tay hắn, tự đếm *"账册上记着一千四百人，能握矛的只有九百二十
个"*, và nói rõ cái giá trước khi ra lệnh. Thiếu nó thì mọi con số đẹp đều vô nghĩa — lỗi không script nào bắt được.
Ở v5 đây là nguyên tắc 2 (giọng người kể) và câu "a decision is preceded by this arithmetic" ở nguyên tắc 3.

## Ba lỗi hay mắc khi viết SI mới

- **Đoạn nào cũng mở bằng tên người là một tật đo được.** Bản chương 2 (SI v6) có **40/66 đoạn** mở bằng tên (61%).
  Đếm đoạn khớp `^[tên nhân vật]` chia tổng đoạn; **trên 35% là tật**. Sửa: mở bằng cái giác quan bắt được trước — tiếng,
  vật, con số — rồi để tên vào giữa câu (`磨石被放到脚边，残缺的手掌压在膝头。`). Sửa tay 17 chỗ: 61% → 17%.
- **Sửa thoại cụt dễ đẻ ra nhãn lặp và thẻ gộp.** Prompt đòi "một câu tính toán mỗi quyết định" mà không nói nó không
  thành công thức thì ra `欧文在心底算了一笔账：…` 4 lần và `艾斯指着狼头对欧文问道：…` 4/6 lượt. Tính toán xuất hiện
  như ý nghĩ hoặc lời nói, không thành công thức lặp; lời thoại đứng riêng hoặc sau **một** động tác.
- **Siết "lượt thoại tự đứng" quá tay thành thoại cụt** (`“一斧断的气？” “行。”` — Tác giả: *"cụt, trống không"*). Mỗi
  lượt là câu đủ: ai nói, muốn việc gì, nói với ai, khi cần thì vì sao; trả lời một tiếng chỉ sau một lượt đã nói rõ
  đang đồng ý việc gì. Đây là chỗ cố ý khác mẫu: mẫu 爽文 viết thoại cụt, Tác giả không muốn thế.

Cả ba là chuẩn để **soát** (review-blacklist, review); chỉ vào SI qua cổng PART 2 khi lặp ở ≥2 lần chạy.

## Kiểm trước khi chạy (60 giây)

- Phần dán ≤ 8.000 ký tự — đếm bằng `len()` trên phần giữa hai dòng `=====`; `wc -m` trong Git Bash đếm byte.
- 4–5 anchor, `verify_anchors.py` khớp hết, `soat_van.py` trên từng anchor ra 0 tật.
- PART 2 ≤ 8 dòng; BANS đúng 5 dòng, không liệt kê từ, không nhắc công cụ soát.
- SI không chứa tên mục của brief, dữ kiện truyện (xưng hô, tỷ giá), nhãn tính cách, chuỗi `踩实/实打实`.
- Không có câu tiếng Trung nào dài quá 8 chữ trong prompt (trừ tên/thuật ngữ) — `tools/soat_brief.py` bắt.
