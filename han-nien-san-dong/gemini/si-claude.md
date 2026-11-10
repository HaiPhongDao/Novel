# SI Claude (10/11/2026) — viết lại từ đầu theo yêu cầu của Tác giả

Bản dán: [`si-claude.txt`](si-claude.txt) (4.691 ký tự; 67% là nguyên văn bộ mẫu). Dựng bằng
`python han-nien-san-dong/gemini/dung_si_claude.py` — phần lời nằm trong script, anchor cắt thẳng từ file bộ mẫu.
**Chưa là "SI đang dùng"**: `si-dan-gemini.txt` giữ nguyên cho tới khi Tác giả nghe lô 001–003 và quyết.

## Đọc bộ mẫu thấy gì

Đọc ch1–4, 9, 12, 30 của 《乱世荒年》, đặt cạnh bản 001 mới nhất của Writer (`test-giong/giong-v4/AT-001o-a.md`):

| | Bộ mẫu | Bản Writer (SI Argon/AT) |
|---|---|---|
| Người kể | Là tiếng lòng MC: câu hỏi, câu cảm, 啊/呢/吧, từ mạng (舔狗, 社畜, 送菜, 小本本) | Trung tính, nghiêm, không một câu cảm, không một câu đùa |
| Danh từ | Trần: 陶碗, 粟米粥, 兔子 | Câu nào cũng đeo tính từ: 粗陶碗, 发灰的粟米粥, 干瘪的粟米, 灰褐色的麻绳 |
| Cảm xúc | Nói thẳng bằng chữ thường: 不由一愣, 有些尴尬, 气笑了, 喜滋滋 | Tránh nói thẳng → tả cơ thể, cận cảnh |
| Bối cảnh | 2–3 dòng đúng lúc cần, quy ra lương thực (一只山鸡换十五斤粟米) | Đọc nguyên bảng giá trong brief, hết dòng này tới dòng khác |
| Thoại | Dày, ngắn, nhiều người chen vào, trẻ con nói kiểu trẻ con | Thưa, tới muộn |
| Câu | Một câu một dòng, có câu vụn (五十两啊！) | Câu viết dài, đủ thành phần |

"Giọng AI" Tác giả nghe ra là giọng văn chương mặc định của Gemini (tả kỹ, nghiêm, đủ ý). Bộ mẫu là 小白文: kể
nhanh, nói thẳng, đùa, tính sổ.

## Khác các SI trước ở đâu

1. **Viết bằng tiếng Trung, đúng giọng khẩu ngữ của bộ mẫu.** Các SI trước viết bằng tiếng Anh; Writer chép cả hình
   thức tu từ của SI (câu "No system voice, no chime" của SI cũ hiện nguyên trong bản Writer: «没有多余的提示，也没有任何声响»).
2. **Gọi đúng tên thể loại bằng chữ của nghề**: 番茄 · 小白文 · 爽文 · 听书. Model đã biết sẵn giọng đó; mô tả vòng bằng
   tiếng Anh ("light, brisk, matter-of-fact") thì nó tự diễn giải.
3. **Không có khối BANS, không liệt kê cụm từ cấm.** Tám nguyên tắc đều viết ở dạng "làm thế này". Tác giả đã bác BANS
   nêu đích danh (09/11); liệt kê từ cấm còn mồi chính từ đó.
4. **Cho phép "kể" thay vì "tả"**: cảm xúc nói thẳng bằng chữ thường (mục 四), đồ vật gọi trần (mục 三). Đây là chỗ
   chặn cận cảnh cơ thể và tính từ thừa mà không cần cấm.
5. **Brief không phải danh sách phải đọc hết** (mục 六): dữ kiện dùng được thì tách vào thoại và phép tính của MC,
   chưa dùng thì để đoạn sau.
6. **Anchor dài và liền cảnh** (5 đoạn, 362–691 字, tổng ~2.540 字) thay cho 4 mẩu ngắn: một mình lên núi làm việc ·
   đối phó kẻ ăn bám · bữa cơm nhà · tiếng lòng với lời ngoài miệng · cả nhà tính sổ chia đồ. Cắt bằng script nên
   khớp nguyên văn; `lam.py viet` cảnh báo nếu Writer chép câu nào trong SI.
7. Chữ cổ / thổ ngữ: một câu khẳng định (mục 七: cả truyện là phổ thông khẩu ngữ ngày nay) + dòng `Chữ cố định` trong
   brief và thẻ thiết lập, không danh sách "từ thời đại" dài.

## Đi kèm

- Brief 001 viết lại thành brief trơn (bỏ khối "Sổ đầu đoạn" — bảng giá 12 mục là thứ Writer đọc lại thành danh sách).
- `handoff/canon-card.md`: bỏ hai câu lộ trước (khế, 23 bước), thêm dòng `Chữ cố định`.

## Kết quả hai vòng (10/11) — chờ Tác giả nghe và chọn

Cùng brief 001 trơn, mỗi bản một lần chạy, chat mới. Số tật đếm bằng `tools/tat_ai.py dem --ds gemini/tat-giong-ai.txt`.

| Bản | 字 | Tật /1.000 字 | 猛地 | 后头·外头·上头 | 炕 | Câu "！" |
|---|---|---|---|---|---|---|
| Vòng 1 (nhãn 番茄 · 爽文 · 小白文; bản ở `archive/doan-001-v3.md`) | 4.761 | 6,09 | 1 | 7 | 11 | 42 |
| **Vòng 2 = `si-claude.txt`** → [`test-giong/claude/C-001.md`](test-giong/claude/C-001.md) | 3.729 | 5,63 | 4 | 8 | 1 | 24 |
| SI-AT, cùng brief → [`test-giong/claude/AT-001.md`](test-giong/claude/AT-001.md) | 2.627 | 0,00 | 0 | 0 | 0 | 0 |
| (SI v2 cũ, brief dài: `archive/doan-001-v2.md`) | 3.635 | 6,60 | | | | |

- Vòng 1 hỏng: nhãn thể loại kéo Writer về khuôn truyện báo thù đại trà (bà nội khóc, MC thề "xem ai chơi chết ai"), bịa
  quan hệ và triều đại, thổ ngữ quay lại. Vòng 2 bỏ nhãn, đặt Writer làm chính tác giả bộ mẫu, thêm "phản ứng viết nhỏ",
  "chỉ viết việc brief cho", một dòng chữ phổ thông để dùng.
- Vòng 2 so với SI-AT: **có giọng MC** (câu hỏi, câu cảm, câu đùa, thoại vào sớm), nhưng **còn cụm sáo và chữ cường điệu**
  (猛地 · 结结实实 · 实打实 · 落针可闻 · 划算得很), còn tính từ đeo vào đồ vật, câu kết kiểu điện ảnh, dài hơn brief xin ~50%.
  SI-AT sạch các tật đã đếm và đúng độ dài, nhưng giọng phẳng: không một câu cảm.
- Hai vòng chỉ dùng câu khẳng định đều không dứt được chữ cường điệu; SI-AT dứt được nhờ nêu đích danh trong BANS.
- Dừng ở hai vòng theo trần của `QUY-TRINH.md` mục 4. Nếu Tác giả thích giọng của C-001 mà vẫn nghe ra tật: bước kế là
  một bản ghép — SI này + đúng một dòng nêu đích danh nhóm chữ cường điệu lấy từ SI-AT.

## Thử brief trần (10/11, sau khi Tác giả nghe C-001)

Tác giả: "SI claude tốt hơn, nhưng chưa đủ. Writer vẫn thường xuyên dùng các từ như 'thật, chân, thực' để nhấn mạnh
(实打实, 实实在在, 切切实实, 货真价实). Vẫn dùng cấu trúc 'không…, không…, không', phủ định hơi nhiều. Vấn đề lớn nhất
có thể vẫn là brief" — prompt trơn một hai câu cho văn "khá ổn".

Brief trần ba câu: [`test-giong/claude/brief-tran-001.md`](test-giong/claude/brief-tran-001.md). Mỗi cấu hình một lần chạy.

| Bản | Brief | SI | 字 | Tật /1.000 | Chữ nhấn nhóm 实 | Dòng ≥2 phủ định /1.000 | 炕 |
|---|---|---|---|---|---|---|---|
| C-001 | trơn | `si-claude.txt` | 3.729 | 5,63 | 2 | 1,6 | 1 |
| T1-001 | trần | `si-claude.txt` | 4.094 | 5,37 | 0 | 2,0 | 7 |
| T2-001 | trần | `si-claude-b.txt` (+ dòng 十, 十一) | 4.972 | 5,43 | 1 | 2,4 | 8 |
| T0-001 | trần | `si-trong.txt` (một dòng) | 3.810 | 3,94 | 2 | 2,4 | 3 |
| AT-001 | trơn | SI-AT | 2.627 | 0,00 | 0 | 1,9 | 0 |

Đọc: brief trần không làm văn sạch hơn ở đề tài này — cả T1, T2 bi kịch hoá, thổ ngữ quay lại, dài gấp rưỡi tới gấp đôi.
Không SI (T0) thì ra văn chương nặng: tả cảnh dài, so sánh, có cả tên chương. Hai dòng thêm (十, 十一) chưa thấy tác dụng
(n=1). Phủ định chồng có cả khi brief không có chữ "không" nào → một phần là thói quen sẵn của Writer. Chỉ SI-AT (nêu
đích danh trong BANS) đưa số tật về 0. Chờ Tác giả đọc năm bản.

