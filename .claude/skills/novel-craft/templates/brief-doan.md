# Brief một đoạn — khung copy-paste (mẫu A, bản 29/10 sau kiểm toán `test-gemini-moi`)

Khung này là **mẫu A** (AGENT.md mục 4). Truyện đang chạy mẫu B giữ khung mẫu B; đổi mẫu giữa truyện cần Tác
giả duyệt.

Brief giao **tình huống**, không giao **kết quả**. Agent quyết: chuyện gì đang treo, người đối diện có gì trong
tay, chỗ dừng, tối đa một dòng `Khoá:`. Writer quyết: beat, thứ tự, ai nói gì, MC xoay xở thế nào, va chạm ngã
ngũ ra sao. Lý do — 5 đoạn `ky-kham-lanh-chua/gemini/test/test-gemini-moi/` (nhánh `test-gemini-moi`): brief ghi
sẵn kết cục, lý lẽ và hình ảnh thì Writer dịch nguyên văn (5–8 câu mỗi đoạn), MC thành người phát lệnh (22/32
lượt là mệnh lệnh), đối thủ nào cũng chịu thua trong 1–3 lượt, và sổ số không đổi theo quyết định của MC.

Brief đứng sau gói bàn giao: `build_pack.py` ghép State JSON + đuôi đoạn trước + brief thành một tin nhắn
(`tools/viet_doan.sh` làm cả lượt). Theo luật brief của Tác giả (28/10, SKILL mục 2): thiết lập — thân phận,
ngoại hình, xưng hô, nơi chốn, số đang chạy, định mức — nằm trong State, brief không chép lại và không xếp chúng
ở đầu; brief mở bằng "Viết tiếp đoạn tiếp theo…", không có mục `Mở` (chỗ mở là đuôi đoạn trước trong gói).
Viết tiếng Việt câu đầy đủ, tên Latin. `<...>` là chỗ điền; khối nào không dùng thì bỏ hẳn.

Trước khi chạy Writer:

```
python tools/soat_brief.py <truyen>/briefs/doan-XXX.md --prev-brief <truyen>/briefs/doan-<trước>.md \
    --bible <truyen>/bible/characters.md --glossary <truyen>/bible/glossary.md
python tools/soat_brief.py <truyen>/briefs/doan-XXX.md ... --mau-b     # truyện chạy mẫu B
```

Mã thoát: `0` xanh · `1` có dòng CHẶN · `2` **lỗi script** (không phải "bị chặn" — đừng sửa brief vì nó).
CHẶN = sửa brief, không chạy. CẢNH BÁO = đọc lại từng dòng; giữ thì ghi lý do vào review.
Cổng này **không thể XANH trên một brief mẫu B đúng khung** nếu thiếu `--mau-b`: nó đòi chữ `Dừng` và coi tên
khối `【Kết đoạn】` là "kết bằng hình ảnh".

```
Viết tiếp đoạn tiếp theo, <cửa sổ độ dài Tác giả chấp nhận, ví dụ 2.000–2.500> 字, bằng tiếng Trung.

Tình huống. <3–5 câu văn xuôi, như sự thật đang có: MC ở đâu, cần có được gì trước khi đoạn hết, cái gì cản
đường. Người đứng đối diện có gì trong tay (người, sổ, luật, món nợ) và muốn gì. Chuyện của đoạn trước chỉ ghi
khi cảnh này dùng tới, ghi đúng như văn đã chốt, kèm chữ "đã".>

Khoá: <tối đa một sự thật dàn ý buộc phải xảy ra trong đoạn này — viết như sự thật, không lý do, không cách thức>.

Dừng ở <một việc đang dở, hoặc một câu hỏi chưa ai trả lời>. <Việc X> thuộc đoạn sau.

Bảng (chỉ khi cảnh xoay quanh một con số vừa đổi; in một lần, đúng nguyên dạng từng dòng):
【宿主：…】
<số đầu đoạn lấy từ State; dòng sẽ đổi trong đoạn thì để …, Writer điền theo định mức trong State, Agent soát lại khi review>
```

Trước khi viết brief, kiểm State có đủ cho đoạn này: người có mặt (chép từ bible: `ai + vai + một dấu hiệu`), xưng
hô, sổ đầu đoạn kèm định mức theo khẩu phần đang dùng. Thiếu thì sửa State, không bù bằng brief.

Truyện chưa có State/gói: dán khối nối ở đầu brief (`【接上】` + `python tools/noi_doan.py <đoạn trước> --chars 300
--wrap` + `【接上完】`), rồi thêm sau `Dừng ở` ba dòng `Người có mặt (chép từ bible): …` · `Xưng hô: …` · `Sổ đầu
đoạn: …` (số riêng tư phải gắn rõ chủ thể biết: `chỉ mình <Tên> biết`). Sau khi chốt mỗi đoạn, quét các địa danh phụ/danh từ riêng mới do Writer vừa đặt trong đoạn đó để neo vào `Sổ đầu đoạn` hoặc `bible/glossary.md` trước khi chạy đoạn kế bằng `--new`.

Đoạn mở truyện: dòng đầu `Viết đoạn mở đầu cho truyện mới, …`; một dòng `Mở:` nêu khoảnh khắc mở
(`references/si-cau-truc.md` mục 5b) là chỗ duy nhất được đặt tính từ cảm giác.

## Brief không chứa — `soat_brief.py` chặn hoặc cảnh báo

| Không ghi | Đã ra gì ở `test-gemini-moi` | Ghi thay bằng |
|---|---|---|
| Số thứ tự sự việc (1. 2. 3.) | Văn chạy đúng 1→7; hành trình 8 ngày thành "第四天晚上…第六天傍晚…" | Một đoạn `Tình huống` |
| Nhãn tính cách ("bình tĩnh", "lạnh lùng", "thiết huyết", "tham lam") | "lạnh lùng/thiết huyết" thắng bible "không giỏi nói trước đám đông": 005 thành diễn văn 8 dòng | Một sự thật của người đó lúc này, lấy từ bible |
| Kết cục va chạm ("ép … phải giao nộp", "lạnh lùng từ chối", "không dám cự tuyệt") | Gerry, 代守, Cole đều chịu thua trong 1–3 lượt | Thứ mỗi bên có trong tay; ai thắng là việc của Writer, hoặc một dòng `Khoá:` |
| Số cuối đoạn, biến động chỉ số ("→ còn 497", "sĩ khí từ 41 xuống 29", "nhận 18 exp") | Hạ khẩu phần ở 003 mà 005 vẫn trừ 1.000 斤 một bữa | Số đầu đoạn + định mức trong State; số cuối đoạn Agent tính sau khi đọc |
| Lý lẽ, lời xin, câu thoại ("Hắn giải thích: nếu…", "lấy cớ…", `"Mua rìu?"`) | Bài nói của Adrian ở 005 là bản dịch câu brief; ba lý do xin tha thành ba lượt của Cole | Người đó cần gì, lo gì — họ tự tìm lời |
| Câu ý nghĩa ("nỗi sợ biến thành động lực", "thay vì rút chạy để mất 36 cọc", "vì … nên …") | Dịch thẳng thành câu người kể | Sự việc nhìn thấy được |
| Hình ảnh, tính từ cảm giác, "Kết đoạn: hoàng hôn buông…" | 002 khép bằng gió và cỏ khô | `Dừng ở` một việc đang dở |
| Câu tiếng Trung, tên người chữ Hán (巴特) | 005 ra 老科尔 | Tên người Latin; chữ Hán chỉ cho thuật ngữ đã có trong glossary và dòng bảng |
| Tên glossary đã đổi (Iron Ridge, Vilan, Baron Losa) | Văn theo brief, lệch glossary chốt 26/10 | Đúng cột "viết trong văn" của glossary |
| Quá 2 cảnh + 1 lần nhảy thời gian | 002: thị trấn + 8 ngày đường + pháo đài | Dời phần dư sang đoạn sau |
| Thẻ nhân vật tự gõ lại | Cole "đội trưởng cầm rìu" → "少有的壮汉"; Karl "hộ vệ" thay cho "phó quan" | State chép đúng bible |
| Cùng một hình dạng chỗ dừng ("có người chạy về báo") | 003 và 005 kết giống hệt nhau | Đổi kiểu dừng: một quyết định dở, một câu hỏi, một việc tay đang làm |

## Ví dụ — brief 005 viết lại theo khung

Cùng tình huống với `test-gemini-moi/prompt-005.md`. Thiết lập Karl/Cole/Bate, 488 người, 1.400 斤, khẩu phần
một bát cháo loãng, cọc 36/120, sĩ khí 41 nằm trong State — định mức khẩu phần phải sửa trong sổ trước, vì
`plot/so-lieu.md` của truyện này đang trừ 1.000 斤 mỗi lần bất kể khẩu phần.

```
Viết tiếp đoạn tiếp theo, 2.000–2.500 字, bằng tiếng Trung.

Tình huống. Tối ngày 1 ở 铁脊要塞. Bate đã vứt rìu chạy về phía pháo đài sau khi năm người đã chết, và Karl đã
trói được hắn trước khi sườn trái vỡ. Trong 488 người còn sống có vài chục người cùng làng với Bate; mẹ hắn còn ở
维兰, và Cole biết bà. Đây là lần đầu Adrian phải quyết số phận một người của mình trước mặt cả đoàn. Sáng mai
đoàn còn phải đốn cho đủ cọc bịt khẩu tường đông.

Khoá: Bate chết trong đoạn này.

Dừng ở sáng ngày 2, giữa lúc dựng cọc ở khẩu tường đông, khi Adrian là người đầu tiên thấy khói phía bắc. Khói của
ai thuộc đoạn sau.
```

## Luật đi kèm

- **State JSON là bộ nhớ của Agent, tuyệt đối không dán raw JSON vào brief.** Khi có `handoff/state.json`, brief được giải phóng hoàn toàn khỏi các khối nối tiếp, xưng hô, người có mặt và sổ số; brief trở lại nguyên dạng 3–5 câu tình huống + 1 dòng Khoá + 1 câu Dừng ở, giúp Writer tập trung 100% vào nhịp văn của SI.
- **Không có dòng nào bảo MC nghĩ gì, cảm thấy gì, hay "hãy thể hiện" điều gì.** Chỉ sự thật, thứ trong tay mỗi
  bên, chỗ dừng. Dòng "chỗ để cái đầu kiếp trước thắng" là bẫy: nó viết hộ cái đầu MC và lặp dữ kiện.
- **Người có mặt và xưng hô chép từ bible vào State**; nhân vật mới chưa có trong bible thì ghi vào State, chốt đoạn
  xong đưa vào bible. Thiếu xưng hô thì `大人` mọc lại ngay — kiểm State trước mỗi brief.
- **Kiểm sau khi chạy:** 4–5 câu đặc trưng của đuôi đoạn trước phải ra 0 trong bản mới; câu cuối phải trọn; khối
  【】 đủ dòng; mọi số trong văn khớp sổ (kể cả câu suy ra kiểu "撑不过两天"). Bản cụt thì bỏ, không đo, không commit.
