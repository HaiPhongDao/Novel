# Hiệu chuẩn SI trên nội dung bộ mẫu

**Chốt SI trước, dựng truyện sau.** Thư mục này giữ bài kiểm tra dùng để chốt SI: lấy một chương
của **bộ mẫu** (đã có đáp án), viết một brief chỉ có sự việc, cho Writer viết lại, rồi so với nguyên văn.

## Vì sao phải làm trước khi dựng bible

Dựng xong bible + dàn ý + SI rồi mới viết đoạn 001 là **đổi bốn biến cùng lúc**: nhân vật mới,
cảnh mới, dàn ý mới, SI mới. Khi bản ra dở, không biết lỗi ở đâu — và cách chữa thường thấy trong
repo là đoán: đổi brief, đổi model, thêm luật SI. Đo trên `manga-tokyo-1996`: đổi 3 hình dạng brief,
chấm 3 bản, rồi chốt một bản lệch bộ mẫu 20–55 lần biên độ.

Bài kiểm tra này tách được biến: **nội dung là của mẫu, chỉ có SI là biến.** Nếu Writer viết lại
nội dung quen thuộc mà vẫn lệch xa nguyên văn, thì SI chưa dạy được — sửa SI, chưa cần dựng truyện.

## Đo được gì

`manga-tokyo-1996` là ca thật. Chương 1 bộ mẫu so với đoạn 001 nó viết:

| Chỉ số | Mẫu (đáp án) | Bản Agent viết | Lệch |
|---|---|---|---|
| 字/đoạn (trung vị) | **15** | 24 | +60% |
| lượt thoại | **45** | 21 | −53% |
| 字/lượt thoại | **8,8** | **31,8** | **+261%** |
| giảng huấn /1.000 字 | 1,28 | **3,87** | **+202%** |
| so sánh người kể /1.000 | 0,114 | 1,29 | +1.030% |
| nhãn ngữ điệu /1.000 | 0,030 | 0,86 | +2.767% |

Hai dòng cuối đã có đích sẵn và Agent **không nhìn**; nó tự đặt ngưỡng tay ("thoại 14–22 lượt",
"20–30 字/lượt") rồi chấm ĐẠT. Đó là lý do phải so với **nguyên văn**, không so với ngưỡng tự nghĩ.

**Giảng huấn** là chỉ số mới: người kể giảng giải — chân lý chung, quy tắc nghề, giải thích ngành
(「编辑部的生存法则是冰冷的」, 「在这个年份，东京不会同情…」, 「一个新人作者通常需要…」). Đây là thứ
Tác giả gọi là "nói linh tinh", và trước giờ không cột nào đếm nó.

## Quy trình

1. **Tách đáp án** — chọn một chương của bộ mẫu, ưu tiên chương 1 (mở truyện, cùng loại cảnh với
   đoạn bạn sắp viết):

   ```
   python tools/hieu_chuan.py tach --file 我在泡沫东京画漫画.txt --chuong 1 --out chung/hieu-chuan/manga/ch01
   ```

2. **Viết `brief.md`** trong thư mục đó: chỉ **sự việc** của chương — ai, ở đâu, muốn gì, chuyện gì
   xảy ra, dừng ở đâu, và các con số. Không chép câu văn, không chép thoại, không chép độc thoại
   nội tâm, không chép phần giảng giải bối cảnh. Mẫu: `manga/ch01/brief.md`.

3. **Chạy Writer** bằng SI đang muốn chốt:

   ```
   python tools/aistudio_run.py --new --si <truyen>/gemini/si-dan-gemini.txt \
       --prompt chung/hieu-chuan/manga/ch01/brief.md \
       --out <truyen>/gemini/test-giong/v1-ch01.md
   ```

4. **So**:

   ```
   python tools/hieu_chuan.py so-sanh --goc chung/hieu-chuan/manga/ch01/goc.txt \
       --sinh <truyen>/gemini/test-giong/v1-ch01.md
   ```

5. **Đọc cạnh nhau** — so 3 đoạn đầu và 3 đoạn cuối. Chỗ nào bản sinh nói thứ mẫu không nói, đó là
   chỗ SI chưa dạy được. Ghi thành việc cụ thể: "SI thiếu luật X", không ghi "văn chưa hay".

6. **Sửa SI một biến, chạy lại 2 lần**, ghi `can-thiep` + `phan-quyet` vào `chung/loi/`. Chỉ khi
   các cột chính (字/lượt, giảng huấn, so sánh người kể, nhãn ngữ điệu) **vào vùng mẫu** mới coi là
   SI đã chốt. Đạt vùng mẫu là điều kiện để được dựng bible và dàn ý.

## Đích của bài kiểm tra

Không phải "giống mẫu từng câu" — nội dung sẽ khác vì Writer tự chọn cách đi. Đích là **phân bố**:
字/đoạn, 字/lượt thoại, số lượt, tỉ lệ đoạn có thoại, và các mật độ tật. Lệch nội dung là bình
thường; lệch phân bố nghĩa là SI không điều khiển được thứ nó tuyên bố điều khiển.

## Vì sao không dùng luôn đoạn 001 của truyện thật để thử

Vì lúc đó nội dung do bạn tự bịa, nên không có gì để so. Không có đáp án thì "hay/dở" là cảm nhận,
và cảm nhận không nói được phải sửa dòng nào trong SI. Bài kiểm tra này chỉ dùng để **chốt SI**;
chất lượng truyện thật vẫn phải đọc như mục 5 của `SKILL.md`.
