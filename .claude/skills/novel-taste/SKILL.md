---
name: novel-taste
description: "Chấm bản thảo tiếng Trung của Writer theo tai của Tác giả repo Novel: chọn bản tốt nhất trong vài bản nháp của cùng một đoạn, chỉ ra chỗ phải sửa tại chỗ, quyết có chạy lại không. Dùng sau `lam.py ban`, khi review một đoạn, hoặc khi phải chọn giữa hai SI/brief bằng bản văn."
version: 1.1.0
---

# Novel Taste — tai của Tác giả

Skill này **không dạy viết**. Nó dạy **nghe như Tác giả nghe**: Tác giả nghe bản tiếng Trung qua app đọc (DocTTS, chuyển
sang Hán-Việt), không nhìn chữ. Mọi tiêu chí dưới đây rút từ 115 lời khen chê thật của Tác giả trong ba tuần
(`chung/taste/ho-so.jsonl`), không rút từ lý thuyết văn chương. Chỗ nào skill lệch lời Tác giả mới nhất thì lời Tác giả thắng
— và ghi lời đó vào hồ sơ.

## 1. Tác giả nghe ra cái gì — xếp theo số lần chê

**A. Thoại (chê nhiều nhất, ~15 lần ở 7 truyện).** Lượt thoại phải **trọn ý, có đầu có đuôi, nói với một người**.
- Hỏng: lượt cụt, lệnh trần, từ chối trơn, câu không chủ ngữ không ai hỏi trước. `“一斧断的气？” “行。”` — "cụt, trống
  không, không đầu không đuôi; truyện cần viết đầy đủ, không cần giống người thật nói". `起来` phải là `起来吧 / 站起来吧`.
  `去碰石头。` `不用了。` `我不组队。` — "thoại của MC đang cực kỳ tệ".
- Hỏng theo chiều ngược lại: một người nói thành bài; hai người nói ra điều cả hai đã biết; **nhân vật phụ giải thích bối
  cảnh hộ người kể** ("thoại của Liễu thẩm lủng củng, đang mượn lương lại giải thích bối cảnh với MC"); MC thắng mọi cuộc
  bằng một câu ngầu; gặp nhau là lao vào việc, không một lượt chào hỏi; người đang khóc chỉ nhận về một lời phán.
- Trợ từ cuối câu vừa đủ để câu mềm: thiếu thì cụt, dày thì giả ("呢 quá nhiều").

**B. Giọng — lời kể đi từ trong đầu MC (~11 lần).** Thể loại này "có cả giọng nói của tác giả mượn lời MC để giải thích,
thể hiện sự ưu việt của người xuyên việt". Bản được chuộng có tiếng lòng trần của MC trong lời kể: câu hỏi, câu cảm, câu
tự giễu, phép tính, góc nhìn người đời sau. Hỏng: "giọng kể như người thứ ba đứng ngoài", "không hề có chất giọng riêng
của MC", "quá văn nghệ, không thoải mái bày ra như bản mẫu", "văn thanh của tác giả nghệ thuật, không phải truyện mạng",
nhân vật "gần như vô hồn" (không ai có ý muốn riêng), MC "lu mờ".

**C. Bày ra đủ, đừng trôi tuột (~9 lần).** MC phải kịp nghĩ: mình xuyên qua, nhà thế nào, cần làm gì, rồi mới hành động.
Hỏng: "mọi thứ xảy ra quá trôi", "tả và kể quá ít, bám vào dữ kiện để checklist, không có khoảng trống trong văn", "MC thức
dậy lững thững một mạch đến đập búa, không có thoại nội tâm, giải thích, kể, làm nền". Cắt giải thích quá tay cũng bị chê:
"cắt mất quá nhiều phần giải thích rồi, vẫn thích bản cũ hơn".
Nhưng đây **không** phải giảng giải: người kể đứng ngoài tóm tâm lý bằng danh từ trừu tượng thì hỏng
(`取而代之的是资深编辑面对现实问题时的清醒与严苛`), so sánh trang trí (`X得像…`) cũng vậy. Phân biệt: MC *nghĩ* bằng giọng
mình = bày ra; người kể *giải nghĩa* hộ độc giả = giảng.

**D. Mạch (~6 lần).** Đoạn sau nối thẳng khoảnh khắc đoạn trước dừng; kể lại, tóm lại chuyện cũ là hỏng nặng ("viết như
viết lại truyện, thiếu liên kết"; một chi tiết cũ lặp 6–8 lần). Đoạn dừng giữa việc đang dở; "kết đoạn bằng một hình
ảnh", câu hạ màn điện ảnh, lời thề cuối đoạn đều bị chê. Người xung quanh phải có phản ứng với việc lạ MC làm.

**E. Chữ — "giọng AI" (~12 lần, và là lời chê gần đây nhất).**
- Chữ nhấn "thật/thực": `实打实 · 实实在在 · 切切实实 · 货真价实 · 结结实实 · 硬生生 · 踩实`; đuôi `…得很`.
- Cường điệu và cận cảnh sáo: `猛地 · 死死 · 狠狠 · 整整`, `直往…里钻`, `浑浊的眼睛`, `嘴唇哆嗦`.
- Phủ định xếp song song: `没…，也没…` · `既没…也没…` · `不…，不…，不…` (phủ định đơn lẻ thì bình thường — bộ mẫu dùng
  nhiều hơn Writer).
- Thổ ngữ, chữ cổ lẫn vào bạch thoại; mỗi lượt thoại dán một nhãn ngữ điệu; câu cụt đứng riêng làm dáng
  (`二十三岁，刚捡回一条命。`).

**Không phải tiêu chí:** độ dài đoạn ("dài bao nhiêu cũng được miễn không trượt ngữ cảnh, văn phong"), câu dài hay ngắn,
mọi điểm số và mật độ ("con số đếm vô nghĩa trong văn học"). Bản 34/34 điểm đã bị loại vì "viết quá loạn xạ".

## 2. Khi hai bản giằng nhau — thứ tự Tác giả đã chọn

1. **Có giọng mà còn tật chữ > sạch mà phẳng.** Tác giả đã chọn bản có tiếng lòng MC dù còn `实打实`, và hai lần bác
   bản "sạch số đếm" vì "chẳng thấy thay đổi gì mấy, còn giảm chất lượng prose". Tật chữ sửa tại chỗ được; giọng thì không.
2. **Thoại hỏng thì loại**, dù phần kể tốt. Thoại là thứ duy nhất Tác giả nói "luôn làm tôi khó chịu".
3. **Kể lại đoạn trước thì loại**, không chấm tiếp. Nhân vật đọc lại thiết lập mà người nghe trong truyện đã biết
   cũng vậy. Nhưng một nhân vật **trả lời câu MC hỏi bằng giọng của chính mình** (lính già báo cáo quân số) là thoại tốt —
   Tác giả đã chọn bản đó thay cho bản chuyển lời báo cáo thành lời kể.
4. Hai bản ngang nhau thì nói là ngang, chọn bản ít chỗ phải sửa hơn. Đừng dựng lý do.
5. Bản Tác giả khen đôi khi là lượt may: chọn bản, đừng kết luận gì về SI hay brief từ một lần.

## 3. Cách chấm

Chấm **mù**: chỉ nhận văn bản và nhãn A/B/C, không biết bản nào từ SI/brief nào. Đọc trọn từng bản một lượt như người
nghe, rồi mới so. Trả đúng khuôn này, không thêm gì:

```
CHỌN: <A|B|C> · tin <1|2|3>   (tin 1–2 = NGANG, lấy bản ít chỗ sửa hơn)   ·   CHẠY LẠI: có/không
VÌ SAO (≤3 dòng, mỗi dòng một câu trích tiếng Trung của bản được chọn hoặc bản bị loại + nó thuộc mục A–E nào)
SỬA TẠI CHỖ trong bản được chọn (≤8 chỗ): «câu trích» → mục nào → sửa thành gì (đúng mấy chữ đó)
```

Dòng CHỌN kèm **độ tin 1–3**. Phép thử 10/11 (`chung/taste/README.md`): tin 3 thì 6/6 trùng Tác giả; tính cả tin 1–2
thì chỉ 14/21. Vì vậy **chỉ tin 3 mới là lựa chọn**; tin 1–2 thì ghi NGANG, lấy bản ít chỗ sửa hơn, và không rút kết luận gì.

`CHẠY LẠI: có` chỉ khi **mọi** bản đều dính mục 2.2 hoặc 2.3; khi đó nói phải đổi gì ở brief (thường là: brief đang giao
kịch bản, đang có câu phủ định, hoặc thiếu văn đoạn trước), không đề xuất sửa SI.

## 4. Vòng lặp "chỉ đưa bản tốt nhất"

1. `python tools/lam.py ban <truyen> <N>` → ba bản nháp + bảng đếm (bảng chỉ để khoanh vùng mục E).
2. Chấm mù theo mục 3 (giao một agent con đọc ba file nháp nếu phiên chính đã biết bản nào là bản nào).
3. `python tools/lam.py chon <truyen> <N> <chữ cái>`; sửa các chỗ ở dòng SỬA TẠI CHỖ ngay trong `chapters/`.
4. Ghi một dòng vào `<truyen>/taste-log.jsonl`: `{"doan":N,"chon":"b","ly_do":"…","sua":k}`.
5. Tác giả chỉ nhận **một** bản mỗi đoạn. Khi Tác giả nói gì về bản đó, thêm lời ấy vào `chung/taste/ho-so.jsonl` và ghi
   vào dòng log `"tac_gia":"ổn|chê: …"`. Tỷ lệ bản được chọn mà Tác giả cho qua là thước đo duy nhất của skill này
   (`chung/taste/README.md`).

## 5. Hồ sơ

| File | Là gì |
|---|---|
| `chung/taste/ho-so.jsonl` | 115 phán xét của Tác giả 22/10–10/11: lời nguyên văn, khen/chê/chọn/bác, về cái gì, nguồn |
| `chung/taste/cap.jsonl` | 32 lần Tác giả chuộng bản này hơn bản kia, kèm đường dẫn bản văn và độ tin |
| `chung/taste/cau.jsonl` | 27 câu, cụm tiếng Trung Tác giả đích thân chỉ ra |
| `chung/taste/README.md` | Kết quả chấm mù đối chiếu với lựa chọn cũ của Tác giả; cách cập nhật |
