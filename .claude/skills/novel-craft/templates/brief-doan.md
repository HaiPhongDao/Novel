# Brief một đoạn — khung copy-paste (bản 29/10, sau kiểm toán `test-gemini-moi`)

Brief giao **tình huống**, không giao **kết quả**. Agent quyết: chuyện gì đang treo, ai có mặt và có gì trong
tay, sổ đầu đoạn, chỗ dừng, tối đa một dòng `Khoá:`. Writer quyết: beat, thứ tự, ai nói gì, MC xoay xở thế nào,
va chạm ngã ngũ ra sao. Lý do — 5 đoạn `ky-kham-lanh-chua/gemini/test/test-gemini-moi/`: brief ghi sẵn kết cục,
lý lẽ và hình ảnh thì Writer dịch nguyên văn (5–8 câu mỗi đoạn), MC thành người phát lệnh (22/32 lượt là mệnh
lệnh), đối thủ nào cũng chịu thua trong 1–3 lượt, và sổ số không đổi theo quyết định của MC.

Thứ tự khối giữ như bản cũ đã kiểm: khối nối tiếp đứng đầu, sự việc trước, số sau — đặt số lên trước thì model
bám số và viết thành biên bản. Tên khối nối không quan trọng (`【接上】…【接上完】` hay `GIỌNG MẪU — … ---`).
`<...>` là chỗ điền; khối nào không dùng thì bỏ hẳn, không để rỗng.

Trước khi chạy Writer:

```
python tools/soat_brief.py <truyen>/briefs/doan-XXX.md --prev-brief <truyen>/briefs/doan-<trước>.md \
    --bible <truyen>/bible/characters.md --glossary <truyen>/bible/glossary.md
```

CHẶN = sửa brief, không chạy. CẢNH BÁO = đọc lại từng dòng; giữ thì ghi lý do vào review.

```
Viết tiếp đoạn <N>, <cửa sổ độ dài Tác giả chấp nhận, ví dụ 2.000–2.500> 字, bằng tiếng Trung, tiếp tục từ đây, không chép lại câu nào:

【接上】
<7–10 dòng cuối của bản đã duyệt — python tools/noi_doan.py <đoạn trước> --chars 300 --wrap>
【接上完】

Tình huống. <3–5 câu văn xuôi, như sự thật đang có: MC ở đâu, cần có được gì trước khi đoạn hết, cái gì cản
đường. Người đứng đối diện có gì trong tay (người, sổ, luật, món nợ) và muốn gì. Chuyện của đoạn trước chỉ ghi
khi cảnh này dùng tới, ghi đúng như văn đã chốt, kèm chữ "đã".>

Người có mặt (chép từ bible): <Tên — vai — một dấu hiệu nhìn thấy được>; <…>.
<MC> là người xuyên việt.
Xưng hô: <ai gọi ai là gì, tự xưng gì — một dòng>.

Sổ đầu đoạn (chép từ plot/so-lieu.md, đã tính bằng máy): <người · lương + định mức tiêu hao theo khẩu phần đang
dùng · tiền + tỷ giá · điểm + định mức điểm>. Chỉ số đoạn này dùng tới.

Bảng (chỉ khi cảnh xoay quanh một con số vừa đổi; in một lần, đúng nguyên dạng từng dòng):
【宿主：…】
<số đầu đoạn; dòng sẽ đổi trong đoạn thì để …, Writer điền theo định mức ở Sổ, Agent soát lại khi review>

Khoá: <tối đa một sự thật dàn ý buộc phải xảy ra trong đoạn này — viết như sự thật, không lý do, không cách thức>.

Dừng ở <một việc đang dở, hoặc một câu hỏi chưa ai trả lời>. <Việc X> thuộc đoạn sau.
```

Đoạn mở truyện: dòng đầu `Viết đoạn mở đầu cho truyện mới, …`; thay khối `【接上】` bằng một dòng `Mở:` (khoảnh
khắc mở — `references/si-cau-truc.md` mục 5b). Dòng `Mở:` là chỗ duy nhất được đặt tính từ cảm giác.

## Brief không chứa — `soat_brief.py` chặn hoặc cảnh báo

| Không ghi | Đã ra gì ở `test-gemini-moi` | Ghi thay bằng |
|---|---|---|
| Số thứ tự sự việc (1. 2. 3.) | Văn chạy đúng 1→7; hành trình 8 ngày thành "第四天晚上…第六天傍晚…" | Một đoạn `Tình huống` |
| Nhãn tính cách ("bình tĩnh", "lạnh lùng", "thiết huyết", "tham lam") | "lạnh lùng/thiết huyết" thắng bible "không giỏi nói trước đám đông": 005 thành diễn văn 8 dòng | Một sự thật của người đó lúc này, lấy từ bible |
| Kết cục va chạm ("ép … phải giao nộp", "lạnh lùng từ chối", "không dám cự tuyệt") | Gerry, 代守, Cole đều chịu thua trong 1–3 lượt | Thứ mỗi bên có trong tay; ai thắng là việc của Writer, hoặc một dòng `Khoá:` |
| Số cuối đoạn, biến động chỉ số ("→ còn 497", "sĩ khí từ 41 xuống 29", "nhận 18 exp") | Hạ khẩu phần ở 003 mà 005 vẫn trừ 1.000 斤 một bữa | Sổ đầu đoạn + định mức; số cuối đoạn Agent tính sau khi đọc |
| Lý lẽ, lời xin, câu thoại ("Hắn giải thích: nếu…", "lấy cớ…", `"Mua rìu?"`) | Bài nói của Adrian ở 005 là bản dịch câu brief; ba lý do xin tha thành ba lượt của Cole | Người đó cần gì, lo gì — họ tự tìm lời |
| Câu ý nghĩa ("nỗi sợ biến thành động lực", "thay vì rút chạy để mất 36 cọc", "vì … nên …") | Dịch thẳng thành câu người kể | Sự việc nhìn thấy được |
| Hình ảnh, tính từ cảm giác, "Kết đoạn: hoàng hôn buông…" | 002 khép bằng gió và cỏ khô | `Dừng ở` một việc đang dở |
| Câu tiếng Trung, tên người chữ Hán (巴特) | 005 ra 老科尔 | Tên người Latin; chữ Hán chỉ cho thuật ngữ đã có trong glossary và dòng bảng |
| Tên glossary đã đổi (Iron Ridge, Vilan, Baron Losa) | Văn theo brief, lệch glossary chốt 26/10 | Đúng cột "viết trong văn" của glossary |
| Quá 2 cảnh + 1 lần nhảy thời gian | 002: thị trấn + 8 ngày đường + pháo đài | Dời phần dư sang đoạn sau |
| Thẻ nhân vật tự gõ lại | Cole "đội trưởng cầm rìu" → "少有的壮汉"; Karl "hộ vệ" thay cho "phó quan" | Chép đúng bible |
| Cùng một hình dạng chỗ dừng ("có người chạy về báo") | 003 và 005 kết giống hệt nhau | Đổi kiểu dừng: một quyết định dở, một câu hỏi, một việc tay đang làm |

## Ví dụ — brief 005 viết lại theo khung

Cùng tình huống với `test-gemini-moi/prompt-005.md`. Số khẩu phần để trống vì `plot/so-lieu.md` hiện trừ 1.000 斤
mỗi lần bất kể khẩu phần — sửa sổ trước khi chạy.

```
Viết tiếp đoạn 005, 2.000–2.500 字, bằng tiếng Trung, tiếp tục từ đây, không chép lại câu nào:

【接上】
<đuôi out-doan-004>
【接上完】

Tình huống. Tối ngày 1 ở 铁脊要塞. Bate đã vứt rìu chạy về phía pháo đài sau khi năm người đã chết, và Karl đã
trói được hắn trước khi sườn trái vỡ. Trong 488 người còn sống có vài chục người cùng làng với Bate; mẹ hắn còn ở
维兰, và Cole biết bà. Đây là lần đầu Adrian phải quyết số phận một người của mình trước mặt cả đoàn. Sáng mai
đoàn còn phải đốn cho đủ cọc bịt khẩu tường đông.

Người có mặt (chép từ bible): Karl — phó quan, tay trái còn bốn ngón, biết chữ và biết tính sổ; Cole — 50 tuổi, lưng còng, chân trái đi cà nhắc; Bate — nông nô 30 tuổi, đang bị trói.
Xưng hô: nông nô gọi Adrian là 少爷, tự xưng 小的; Karl gọi 少爷, tự xưng 我.

Sổ đầu đoạn: 488 người · lương 1.400 斤, khẩu phần một bát cháo loãng mỗi người mỗi bữa (<斤 mỗi bữa — từ sổ đã
sửa>) · cọc 36/120, 24 rìu × 3 cọc mỗi ngày · sĩ khí 41/100.

Khoá: Bate chết trong đoạn này.

Dừng ở sáng ngày 2, giữa lúc dựng cọc ở khẩu tường đông, khi Adrian là người đầu tiên thấy khói phía bắc. Khói của
ai thuộc đoạn sau.
```

## Luật đi kèm

- **Không có dòng nào bảo MC nghĩ gì, cảm thấy gì, hay "hãy thể hiện" điều gì.** Chỉ sự thật, thứ trong tay mỗi
  bên, sổ, chỗ dừng. Dòng "chỗ để cái đầu kiếp trước thắng" là bẫy: nó viết hộ cái đầu MC và lặp dữ kiện.
- **Mỗi người có mặt một dòng thân phận chép từ bible** (`ai + vai + một dấu hiệu`); người vắng không liệt kê.
  Nhân vật chưa có trong bible: ghi một dòng, chốt đoạn xong thì đưa vào bible.
- **Một dòng xưng hô trong mọi brief**, kể cả khi glossary đã chốt: thiếu nó thì `大人` mọc lại ngay.
- **Kiểm sau khi chạy:** 4–5 câu đặc trưng của khối nối phải ra 0 trong bản mới; câu cuối phải trọn; khối 【】 đủ
  dòng; mọi số trong văn khớp sổ (kể cả câu suy ra kiểu "撑不过两天"). Bản cụt thì bỏ, không đo, không commit.
