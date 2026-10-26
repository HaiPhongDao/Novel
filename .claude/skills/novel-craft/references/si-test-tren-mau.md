# Test giọng trên nội dung truyện mẫu (đáp án đã biết)

Dùng khi Tác giả nghi "SI và prompt chưa thật sự làm việc". Soát bản thảo của chính mình không trả lời được câu đó: không có bản đúng để so, và nhiễu giữa các lần chạy (`si-cau-truc.md` mục 4b, r ≈ 0 giữa đời SI và số tật) lớn hơn hiệu ứng cần đo. Cách đo tuyệt đối: chạy SI trên **nội dung truyện mẫu đã có nguyên văn**, rồi so bản ra với nguyên văn.

## 1. Quy trình

1. Chọn **1–2 cảnh ngoài anchor**, khác loại nhau: một cảnh đối thoại/giải thích, một cảnh khế ước/số liệu. Cảnh phải chưa nằm trong PART 1 của SI, nếu không là đo lại anchor.
2. Viết prompt tiếng Việt 150–200 từ, **chỉ có sự việc**: dữ kiện (ai, vai, chuyện gì đã xong trước cảnh), 3–5 beat theo thứ tự, điểm dừng. Không dặn cách viết và không dặn độ dài câu — nếu không thì đang đo prompt chứ không đo SI. Nhưng **động cơ của MC là dữ kiện, không phải dặn cách viết**: nếu cảnh gốc sống bằng việc MC đang cày exp, đang giấu một khoản, đang sợ mất ghế, thì ghi một dòng sự thật đó vào khối sự việc — bỏ nó đi thì bản ra thiếu động cơ, và ta quy lỗi cho SI trong khi lỗi ở prompt.
3. **Đổi dòng tên riêng trong một bản copy của SI** sang tên truyện mẫu (Roland · Barov · Carter …), giữ nguyên mọi luật khác; cất bản test riêng (`gemini/si-test-vN.txt`), đừng sửa SI thật.
4. Cắt **nguyên văn đúng cảnh đó** ra `goc-tN.txt` — từ đầu cảnh tới đúng điểm dừng ghi trong prompt, bỏ chrome của trang đọc.
5. So **bốn số nhìn thấy giọng**: số câu, chữ/câu, số lượt thoại, chữ/lượt. Các cột tật chỉ để tham khảo; mốc của chúng ở `si-cau-truc.md` mục 4b.
6. Ghi vào `<truyen>/gemini/test-giong/README.md`: prompt, bảng số, kết luận. Kết quả chỉ nằm trong chat là mất.

## 2. Bảng đã đo (cùng prompt, hai đời SI)

| cảnh | bản | chữ | câu | chữ/câu | lượt | chữ/lượt |
|---|---|---|---|---|---|---|
| đối thoại/giải thích | **gốc** | 1.512 | 40 | **28,1** | 17 | **22,9** |
| đối thoại/giải thích | SI trước | 1.798 | 27 | 39,5 | 19 | 38,5 |
| đối thoại/giải thích | SI + neo câu | 2.395 | 26 | **28,3** | **41** | 40,4 |
| đối thoại/giải thích | SI bỏ neo lượt | 1.963 | 38 | **30,5** | 28 | 28,8 |
| khế ước/số liệu | **gốc** | 1.998 | 54 | **34,0** | **4** | 40,0 |
| khế ước/số liệu | SI trước | 1.762 | 17 | 47,8 | 19 | 49,9 |
| khế ước/số liệu | SI + neo câu | 2.187 | 28 | **28,8** | **32** | 43,2 |
| khế ước/số liệu | SI bỏ neo lượt, brief như đối thoại | 2.000 | 44 | 21,5 | **41** | 25,7 |
| khế ước/số liệu | SI bỏ neo lượt, brief ghi "phần lớn là lời kể" | 1.896 | 44 | **39,6** | **6** | 25,5 |

## 3. Ba kết luận

- **Neo độ dài câu là con số duy nhất nên có trong SI.** Một câu "in this register it lands around twenty to thirty characters; a longer one carries a list or a calculation" đưa câu về 28,3–28,8 chữ, sát gốc (28,1–34,0). Trước đó SI không có neo nào thì câu 39,5–47,8 chữ.
- **Neo độ dài lượt thoại thì phản tác dụng, và nó không phải nguyên nhân chính.** "a turn runs one sentence of ten to twenty-five characters" làm số lượt 17→41 và 4→32, tổng chữ cũng tăng: model đạt chỉ tiêu bằng cách **chẻ lời thành nhiều lượt ngắn** rồi thêm lời kể giữa các lượt. Bỏ con số thì cảnh đối thoại về 28 lượt (gốc 17) nhưng cảnh khế ước **vẫn 41 lượt** — tức con số không phải chỗ hỏng: brief của cảnh đó đã viết như một cuộc trao đổi. Chữa ở brief, xem mục 4.
- **Đích là mật độ của mẫu, không phải 0.** Nguyên văn có 4 cặp phủ định ở cảnh đối thoại, 3 cặp + 1 so sánh ở cảnh khế ước — cùng cỡ với bản bị coi là bẩn. "0 cặp" không phải thành tích: so mật độ/1.000 chữ với mẫu, chỉ coi là lỗi khi lệch quá ~2 lần mẫu.

## 4. Mật độ thoại là dữ kiện của brief, không phải luật của SI

Cùng một SI, cùng một cảnh khế ước: brief viết như cuộc trao đổi (Carter hỏi, Roland đáp) → **41 lượt**; brief ghi "phần lớn là lời kể: việc Roland làm với cái máy, cách anh tính, điều khoản anh đặt ra; chỉ vài lượt thoại — câu hỏi của Carter và câu đáp ngắn" → **6 lượt** (gốc 4), 1.896 字, 39,6 chữ/câu. Nên **mỗi brief phải có một dòng tỷ lệ** ("phần lớn là lời kể" hoặc "phần lớn là thoại qua lại"), và khi số lượt thoại sai thì **sửa dòng đó**, không thêm luật vào SI: SI quyết hình dạng một lượt, brief quyết cảnh có bao nhiêu lượt.

Bảng chọn tầng sửa:

| triệu chứng | tầng sửa |
|---|---|
| câu quá dài / quá ngắn / mất nhịp | SI — neo độ dài câu |
| số lượt thoại nhiều hoặc ít, cảnh thành cuộc họp | brief — dòng tỷ lệ thoại/lời kể |
| lượt thoại cụt, thiếu chủ ngữ hay người nhận | SI — "a turn stands on its own feet" |
| xưng hô, tước vị, tiền tệ, ai còn sống, đã chôn chưa | `bible/glossary.md` + khối dữ kiện trong brief |
| tật từ vựng rải rác (phủ định lặp, 实, nhãn ngữ điệu, so sánh người kể) | review từng chỗ; lặp ở ≥3 bản mới động SI, và sửa bằng cách **cắt** một luật khác |

Hai cảnh hai loại là mức tối thiểu: neo độ dài câu đạt 28,3–30,5 ở cảnh thoại dày nhưng cảnh lời kể đo được 21,5 khi bị thoại lấn, và 39,6 khi brief đúng — đừng kết luận SI hỏng (hay đạt) từ một cảnh.

## 5. Bẫy: khác biệt về điểm mở cảnh không phải lỗi

Bản sinh mở bằng cửa sổ, mùi, ánh sáng; nguyên văn mở bằng một đoạn định luật chép ra giấy hoặc một câu tóm tắt ("这一个星期来，边陲镇还算平静。"). Nhưng Tác giả của mình **thích mở chậm** (tỉnh → cơ thể → nhà → sân) và đã chê cảnh mở bằng hành động dứt khoát. Vì vậy chỉ lấy mẫu làm chuẩn cho **nhịp câu và mật độ thoại**; điểm mở theo lời Tác giả. Bảng số lệch ở trục nào Tác giả đã có ý kiến thì hỏi lại, đừng "sửa cho giống mẫu".

## 6. Giới hạn của phép test

- Nó đo **văn phong**, không đo canon: tên, xưng hô, trạng thái nhân vật vẫn phải kiểm bằng prompt/glossary.
- Một cảnh một lần chạy vẫn có nhiễu; muốn chắc thì chạy hai lần cùng prompt, so hai bản sinh với nhau trước khi so với gốc.
- Cột `paragraphs` / `median_para_han` của `soat_van.py` chia theo **dòng trống**, còn bản thảo repo dùng một dòng một đoạn — nên nó gộp hơn trăm dòng thành vài khối và hai cột đó vô nghĩa khi so nhịp. Đo cỡ đoạn, cỡ dòng, tỉ lệ dòng ≤30 字 bằng script riêng (đếm dòng, đếm câu), đừng đọc hai cột đó.
- Truyện mẫu khác thể (đô thị, tiên hiệp) thì bảng số không dùng làm mốc — chỉ dùng cảnh cùng thể loại, cùng register.
- **Đừng dạy nhịp bằng câu mẫu tiếng Trung trong prompt** (kể cả khi ghi rõ "nhịp mẫu, không chép"): Writer chép nguyên vào bài và khi đó mọi số đo chỉ là số đo của văn Agent. Ví dụ nhịp viết bằng tiếng Việt; cổng phát hiện và cách chấm: `cham-diem-ban-thao.md`.

## 7. Đo mẫu trước khi viết BANS — luật chép từ truyện khác sẽ cấm đúng cái mẫu sống bằng

Trước khi viết khối BANS, đếm **trong chính bộ mẫu**, trên toàn sách, quy ra /1000 字 và /chương: thẻ thoại (`说道/问道/笑道/回道`), câu tự giễu hoặc tự gọi của MC, câu hỏi cho người đọc, số dòng bảng in ra, và bốn tật chuẩn (`实`, so sánh của người kể, phủ định song song, nhãn ngữ điệu).

- **Cấm thứ mẫu dùng dày là bỏ register, không phải dọn tật.** Một đời SI cấm sạch `说道/问道` trong khi mẫu chạy 3,7 thẻ/chương (`说道` 1,06/1000, `问道` 0,46, `笑道` 0,23); bản ra 0 tật, nhịp khớp, mà Tác giả đọc thấy "như biên bản". Lệnh cấm đúng là cấm **thẻ chồng** (tên + người nghe + cử chỉ trong một câu) và cấm **nhãn ngữ điệu**, không cấm thẻ.
- **Ngưỡng là mật độ của mẫu, không phải 0**: mẫu cùng loại có 0,14 `实`/1000, 0,46 so sánh người kể/1000, 0,14 cặp phủ định/1000, ~0 nhãn ngữ điệu.
- **Giọng người kể cũng phải đếm**: mẫu có `他罗伯森老爷` 1,35/chương, câu hỏi cho người đọc 0,79/chương, `毕竟` 1,12/chương, `该死的` 0,10/chương — đó là hạn mức để viết vào PART 2, không phải chuyện cảm tính.
- **Bảng in ra hay kể lại cũng phải đo**: bảng `【】` in 0,06 dòng/chương (51 dòng/886 chương) nhưng được nhắc trong lời kể 0,5–0,7 lần/chương, dòng exp `“叮！…经验加300。”` 0,05/chương. Đòi in dày là làm bản ra khác mẫu; đòi in đúng dạng (một entry một dòng) mới là chỗ siết.

## 8. Trả kết quả: Tác giả muốn **đọc văn**, không đọc bảng số

Bảng số + link file là chưa trả lời — câu tiếp theo sẽ là "đoạn viết so với mẫu đâu?". Sau mỗi lần chạy test:

- Tạo `<truyen>/reviews/so-sanh-<bản>.md`: từng beat (mở cảnh, ra lệnh, chỗ hay nhất, bảng hệ thống, kết cảnh), **nguyên văn mẫu ↔ bản sinh**, trích đúng chữ, mỗi cặp một dòng nói khác ở đâu; cuối file một khối "bốn thứ lặp lại ở mọi mục" — đó là phần Tác giả dùng để quyết.
- Dán **2–3 cặp ngắn nhất** vào chat kèm kết luận; cả bản thì để link. Đủ để quyết mà không đổ 2.500 字 vào context.
- Nói rõ giới hạn của lần đo (một cảnh, một lần chạy, brief có/không có dòng tỷ lệ thoại) trước khi Tác giả hỏi, và đừng nhận công cho đời SI nào từ một lần chạy.

## 9. Từ test sang chương thật: sửa tay hay mở vòng SI

Test sạch là tin tốt về SI, không phải giấy bảo hành cho chương sau: cùng một đời SI, bản test trên cảnh mẫu ra 0 tật, chương thật chạy ngay sau đó ra 6 tật (3 so sánh người kể + 3 nhãn ngữ điệu trên 2.600 字) — sửa tay 13 chỗ là sạch, không cần vòng SI mới.

Cách quyết, trước khi động vào SI:

1. **So số tật của hai lần chạy gần nhất** (bản test và chương thật, hoặc hai bản cùng cảnh). Lệch từ 0 lên ≥3 trên cùng một đời SI là **biến thiên của lần chạy**, không phải lỗi luật (`si-cau-truc.md` mục 4b: r ≈ 0 giữa đời SI và số tật).
2. **Sửa tay khi số tật ≤ ~10 và đều là tật từ vựng** (so sánh, nhãn, phủ định, `实`): mỗi chỗ là một câu thay thế, 10–15 phút; một vòng SI tốn 3 phút chạy + đọc lại cả chương, mà lần chạy mới lại có biên độ riêng.
3. **Mở vòng SI khi tật lặp ở ≥3 bản độc lập**, hoặc khi lỗi là **hình dạng** (số lượt thoại, độ dài, thiếu sổ riêng của MC) — sửa tay không chữa được hình dạng.
4. Sửa tay xong vẫn phải chạy `soat_van.py --list` **và** grep tay `如.{1,8}般` / `(平静|冷冷|淡淡)地(说|道|命令|问)` (SKILL.md mục 5.3): bản sửa tay đã được tool báo 0 mà vẫn còn 1 nhãn vì regex không khớp.

Ghi vào review: bản máy (A) giữ nguyên làm bản đối chứng, bản sửa tay (B) là bản Tác giả đọc — không ghi đè A; liệt kê **từng cặp câu trước → sau**, vì đó là thứ chứng minh công sửa và để lần sau biết Writer hay mắc đúng tật nào.
