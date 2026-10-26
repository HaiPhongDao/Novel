# Chấm điểm một bản thảo (thay cho cảm nhận)

Dùng khi phải so nhiều bản của cùng một đoạn, hoặc khi vòng thử–sửa đã dài mà không biết bản nào hơn. Mục đích không phải "cho điểm văn hay" — script chỉ đếm cái đếm được — mà là **chốt ngưỡng trước khi đọc bản mới**, để không tự lừa mình bằng ấn tượng.

## 1. Lệnh

```bash
python tools/cham_doan.py --prompt <truyen>/briefs/doan-XXX.md \
       --numbers "六十一,四十,九枚,三百一十二" \
       <truyen>/chapters/doan-XXX-*.md
```

- `--prompt <brief>`: bắt buộc khi muốn cổng chép mẫu (mục 2). Không truyền thì cổng đó không chạy.
- `--numbers`: **số liệu bắt buộc của riêng đoạn đó**, viết đúng chuỗi Hán sẽ xuất hiện trong văn. Đừng để danh sách chung cho mọi đoạn: đoạn 002 không có lý do phải nhắc lại nợ 61 vàng, và một script bắt toàn cục sẽ báo "thiếu số" oan rồi đẩy Agent đi sửa brief không có lỗi.
- Đầu ra ba nhóm: `nhịp` (56) · `văn` (34) · `canon` (10) = 100.

## 2. Hai cổng chặn (veto) trước khi tin điểm

1. **Chép mẫu.** Bất kỳ câu tiếng Hán ≥8 chữ nào của prompt xuất hiện nguyên văn trong bản thảo → in `HỎNG` và điểm về 0, bất kể các cột khác đẹp thế nào. Đây là lỗi đã xảy ra thật: prompt có "ba câu nhịp mẫu", Writer chép nguyên làm ba đoạn mở, bản đó được 88/100 và được khen — toàn bộ là văn của Agent. Chữa gốc: prompt không chứa câu tiếng Trung nào (SKILL.md mục 4).
2. **Canon.** `回大人 ≥ 3` (đoạn có quản gia), không có `老奴 / 奴才 / 属下 / 末将 / 陛下 / 殿下`, và đủ `--numbers`. Canon sai thì sửa brief/glossary rồi chạy lại — đừng sửa câu trong văn để script hết báo.
   - Truyện **hiện đại/đô thị/mạt thế**: thêm `--modern`, script đổi sang bộ cấm `大人 / 小的 / 老爷 / 少爷 / 属下 / 奴才 / 老奴 / 陛下 / 殿下` và **không** đòi `回大人`.
   - `小的` phải đếm bằng lookbehind (`(?<![窄细瘦矮短小])小的`): "窄小的通道" là tính từ, không phải tự xưng; đếm trơn sẽ báo oan và đẩy Agent đi sửa một câu không sai.
   - **Cổng canon cố định theo register trang viên cổ điển, nên `canon 0/10` có thể là báo oan khi truyện đã chốt bảng xưng hô riêng.** Một bản sạch ra `回大人` 0 · `小的` 0 vẫn có thể đúng canon nếu glossary chốt `少爷` cho người thừa kế và `老爷` cho gia chủ (`Gerry` nói `男爵老爷`, `老爷定过规矩` — đúng, vì đang nói về nam tước). Trước khi kết luận: `grep` từng chỗ khớp + đọc dòng register trong `bible/glossary.md`. Lệch thật thì sửa glossary rồi prompt; **không** sửa câu trong văn cho script hết báo.

## 2b. Band này KHÔNG dùng cho 爽文

Bảng ở mục 3 giả định văn 领主: câu 20–34 字, thoại 10–22 lượt. Bản **爽文/无敌流** ra ~15 字/đoạn, hàng chục đoạn cụt, 30+ dòng 【】 — chấm bằng band này là báo hỏng oan. Với thể loại đó, chấm bằng bảng dấu hiệu của mẫu: `references/sang-van.md` mục 1 và 6.

## 3. Ngưỡng đang dùng, và vì sao là những số đó

| cột | ngưỡng | điểm | neo |
|---|---|---|---|
| chữ | 1500–1800 | 12 | độ dài một đoạn theo `AGENT.md` |
| chữ/câu | 20–34 | 18 | mẫu gốc 28,1 và 34,0; bản Tác giả khen 21–28 |
| số câu | ≥45 | 10 | bản khen có 45–66 câu / 1.500–1.800 字 |
| lượt thoại | 10–22 | 8 | brief quyết (xem `si-test-tren-mau.md` mục 4) |
| chữ/lượt | 16–30 | 8 | mẫu 22,9–40,0 |
| phủ định lặp | ≤4 | 10 | **mẫu gốc có 3–4 cặp mỗi cảnh** — ngưỡng 0 là sai |
| khuôn 实 | 0 | 6 | không có trong văn mẫu |
| nhãn ngữ điệu | 0 | 6 | mẫu 0 |
| so sánh người kể (ngoài ngoặc thoại) | 0 | 6 | mẫu 0–1; so sánh trong lời nhân vật không tính |
| câu mào rẻ ("nhưng đó chưa phải là…") | 0 | 6 | mẫu 0 |
| canon + số liệu | đủ | 10 | mục 2 |

Ba điều rút ra khi lập bảng này:

- **Ngưỡng lấy từ mẫu và từ bản Tác giả đã khen, không lấy từ cảm giác "sạch".** Đặt 0 cho phủ định lặp là đặt mục tiêu chặt hơn chính truyện mẫu, và cái giá là mỗi vòng lại "phát hiện" một lỗi mới để đuổi.
- **Đừng siết ngưỡng sau khi đã thấy điểm.** Đổi band giữa hai lần so là mọi so sánh trước đó vô nghĩa; muốn đổi thì chấm lại toàn bộ bản cũ bằng band mới rồi mới nói bản nào hơn.
- **Chênh ≤8 điểm giữa hai bản sạch là nhiễu**, không phải thứ tự hạng. Cùng bộ ngưỡng, cùng model, một lần chạy; quyết định khi đó thuộc về người đọc bản thảo.

## 4. Cách đọc kết quả

- 90–100 và canon đủ: dùng được làm bản chuẩn của đoạn; sửa tay những chỗ lẻ (một so sánh của người kể, một câu mào) thay vì chạy lại.
- 70–89: xem cột nào rơi. Hỏng `chữ/câu` hoặc `lượt thoại` → brief (dòng tỷ lệ thoại, số beat); hỏng `phủ định`/`so sánh` mà các cột khác sạch → sửa tay 1–2 câu, rẻ hơn một lần chạy 3 phút.
- Dưới 70 hoặc `HỎNG`: bỏ bản, sửa prompt, chạy lại. Đừng cộng dồn bản hỏng vào bảng so sánh.
- **Bảng điểm phải vào `reviews/doan-XXX.md`**, kèm band đã dùng; chat chỉ là nơi báo cáo.
- **Cột `chữ` chấm theo band mặc định (1500–1800), nên khi Tác giả đã chốt một cửa sổ khác cho truyện — ví dụ 2.000–3.000 字 cho lane 领主 — cột đó báo hỏng oan.** Đọc nó là thông tin; chỉ tính là lỗi khi vượt cửa sổ Tác giả đã chốt, và ghi cửa sổ đó vào dòng band trong review để lần so sau còn hiệu lực.

## 5. Bẫy khi tự viết script chấm

- Đếm so sánh/ nhãn ngữ điệu trên **toàn văn** sẽ bắt oan lời nhân vật ("脆得像干饼" là Osric nói, không phải người kể) — tính trên phần đã bỏ ngoặc thoại.
- Đếm "câu" bằng `re.split` trên dấu câu sẽ gộp cả dòng thoại vào lời kể nếu không xoá ngoặc trước.
- Số câu và chữ/câu là hai cột khác nhau: bản câu ngắn mà ít câu (đoạn gộp) vẫn sai nhịp; cả hai phải cùng đạt.
- Cột `khuon-shi` đếm **mọi** chữ 实, kể cả tính từ thường (`厚实的皮袍`, `笑容变得真切了一些`) — một hit không đồng nghĩa với khuôn độ-cụ-thể-giả. Mở `--list` đọc ngữ cảnh; là tính từ bình thường thì ghi vào review là báo oan, đừng sửa câu cho cột về 0.
- Script không thấy: câu mào do model tự chế, mâu thuẫn thời gian ("ba ngày" ở đoạn này, "bốn ngày" ở đoạn kia), và mọi lỗi canon không nằm trong danh sách `--numbers`. Đọc bản thảo vẫn là bước cuối, không được bỏ.
