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

## Đo được gì — và không đo được gì

**Đếm chữ không đo được tiểu thuyết.** Số đo ở đây trả lời đúng một câu hẹp: *bản này có lệch khỏi bộ mẫu ở
những chỗ SI tuyên bố điều khiển không* (nhịp đoạn, độ dài lượt thoại, lượng giảng giải). Nó **không** nói được
văn hay hay dở, cảnh có sức không, nhân vật có sống không.

**Biên độ lấy từ nhiều chương, không từ một chương.** Đo 30 chương đầu bộ mẫu:

| Chỉ số | TB | SD | Biên độ (TB ± 2SD) |
|---|---|---|---|
| 字/đoạn | 24,86 | 3,03 | 18,8 – 30,9 |
| 字/câu | 22,72 | 2,82 | 17,1 – 28,4 |
| lượt thoại | 39,13 | 13,35 | 12,4 – 65,8 |
| **字/lượt thoại** | **12,59** | **3,85** | **4,9 – 20,3** |
| % đoạn có thoại | 35,03 | 9,21 | 16,6 – 53,5 |
| **giảng huấn /1.000** | **1,50** | **1,00** | **0 – 3,5** |

Đây là chỗ tôi đã sai lần đầu: lấy **chương 1** làm chuẩn thì nó có 19,7 字/đoạn, nên bản sinh 26,7 bị coi là
lệch 36% — trong khi so với 30 chương thì 26,7 nằm **trong** biên độ. Một chương chỉ là một mẫu thăm dò.

## Ca thật: `manga-tokyo-1996`

Agent dựng bible + dàn ý + SI rồi mới viết đoạn 001, đổi 3 hình dạng brief, chốt một bản và **chấm ĐẠT**. So với
biên độ trên:

| Chỉ số | Bản 1996 | Biên độ | Kết luận |
|---|---|---|---|
| 字/lượt thoại | **31,8** | 4,9 – 20,3 | **ngoài, ≈5 SD** |
| giảng huấn /1.000 | **3,87** | 0 – 3,5 | **ngoài, ≈2,4 SD** |
| 字/đoạn | 26,7 | 18,8 – 30,9 | trong |
| lượt thoại | 21 | 12,4 – 65,8 | trong |

Nghĩa là chỗ hỏng thật là **lượt thoại bị kéo dài** và **người kể giảng giải** — không phải "đoạn quá dài".

Vì sao nó vẫn báo ĐẠT: `so-sanh` đời đầu chỉ **in bảng rồi trả `exit 0`**, không có phán quyết. Một cổng không
phán quyết thì người chạy tự kết luận, và nó kết luận theo ngưỡng nó tự nghĩ ("thoại 14–22 lượt",
"20–30 字/lượt") chứ không theo bộ mẫu. Giờ cổng trả `exit 1` kèm danh sách chỉ số lệch.

**Giảng huấn** là chỉ số mới: người kể giảng giải — chân lý chung, quy tắc nghề, giải thích ngành
(「编辑部的生存法则是冰冷的」, 「在这个年份，东京不会同情…」, 「一个新人作者通常需要…」). Đây là thứ
Tác giả gọi là "nói linh tinh", và trước giờ không cột nào đếm nó.

## Hai việc, đừng trộn

| Việc | Ai làm | Căn cứ |
|---|---|---|
| Cổng cơ học: chỉ số có nằm trong biên độ mẫu không | Máy | `so-sanh` → `exit 0/1` |
| Phán quyết: viết có ra truyện không | **Tác giả đọc** | `ghep-cap` → file đọc cặp |

Không có ngưỡng số nào thay được việc đọc. Một bản trong biên độ mọi cột vẫn có thể là văn chết; một bản lệch
một cột vẫn có thể hay. Vì vậy chỉ được dựng bible sau khi **Tác giả đọc cặp và đồng ý**, không phải sau khi máy
báo xanh.

## Quy trình

1. **Lấy biên độ** (một lần cho mỗi bộ mẫu, ghi ra `bang-mau.json`):

   ```
   python tools/hieu_chuan.py do-chuong --file 我在泡沫东京画漫画.txt --so-chuong 30
   ```

2. **Tách đáp án** — chọn một chương mẫu, ưu tiên chương 1 (mở truyện, cùng loại cảnh với đoạn sắp viết):

   ```
   python tools/hieu_chuan.py tach --file 我在泡沫东京画漫画.txt --chuong 1 --out chung/hieu-chuan/manga/ch01
   ```

3. **Viết `brief.md`** trong thư mục đó: chỉ **sự việc** của chương — ai, ở đâu, muốn gì, chuyện gì xảy ra, dừng
   ở đâu, và các con số. Không chép câu văn, không chép thoại, không chép độc thoại nội tâm, không chép phần
   giảng giải bối cảnh. Mẫu: `manga/ch01/brief.md`.

4. **Chạy Writer** bằng SI đang muốn chốt — **2 lần**, hai chat mới:

   ```
   python tools/aistudio_run.py --new --si <truyen>/gemini/si-dan-gemini.txt \
       --prompt chung/hieu-chuan/manga/ch01/brief.md --out <truyen>/gemini/test-giong/v1-ch01-a.md
   ```

5. **Cổng số** (máy phán, `exit 1` = lệch):

   ```
   python tools/hieu_chuan.py so-sanh --goc chung/hieu-chuan/manga/ch01/goc.txt \
       --sinh <truyen>/gemini/test-giong/v1-ch01-a.md --doc-cap <truyen>/gemini/test-giong/doc-cap.md
   ```

6. **Đọc cặp** — mở `doc-cap.md`, đọc 12 cặp đoạn. Chỗ nào bản sinh nói thứ mẫu không nói, hoặc bỏ thứ mẫu có,
   ghi thành việc cụ thể ("SI thiếu luật về lượt thoại ngắn"), không ghi "văn chưa hay".

7. **Tác giả chấm.** Cổng số xanh **không** phải chốt SI. Chỉ Tác giả đọc cặp rồi nói ĐẠT mới dựng bible.

8. **Sửa SI một biến, chạy lại 2 lần**, ghi `can-thiep` + `phan-quyet` vào `chung/loi/`.

## Đích của bài kiểm tra — và giới hạn của nó

Không phải "giống mẫu từng câu": nội dung sẽ khác vì Writer tự chọn cách đi. Đích của phần **máy** là phân bố
(字/đoạn, 字/lượt thoại, số lượt, tỉ lệ đoạn có thoại, mật độ giảng huấn) — lệch phân bố nghĩa là SI không điều
khiển được thứ nó tuyên bố điều khiển.

Nhưng phân bố không nói được văn hay. Thứ quyết định vẫn là đọc. Đừng biến bảng số thành bảng điểm: nó chỉ nói
"có lệch chỗ này", không nói "bản này kém bản kia".

## Vì sao không dùng luôn đoạn 001 của truyện thật để thử

Vì lúc đó nội dung do bạn tự nghĩ ra, nên không có gì để so. Không có đáp án thì "hay/dở" là cảm nhận, và cảm
nhận không chỉ ra được phải sửa dòng nào trong SI. Bài kiểm tra này chỉ dùng để **chốt SI**; chất lượng truyện
thật vẫn phải đọc như mục 5 của `SKILL.md`.
