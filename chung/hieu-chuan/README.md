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

## Số đo để làm gì — và không để làm gì

**Đếm chữ không đo được tiểu thuyết.** Số đo ở đây chỉ là **kính lúp**: khi đọc thấy "sao nó lải nhải" hoặc "sao nó
cụt lủn", vài cột dưới đây chỉ ra nên nhìn chỗ nào. Nó **không** nói văn hay hay dở, và **không** được dùng làm đích
— đưa con số nhịp vào SI thì Writer tối ưu cho con số (đo được: SI ghi 18–26 ra 11–15 字/câu).

Bảng dưới là mô tả bộ mẫu, để biết "bình thường" của thể loại trông thế nào — không phải chuẩn để chấm:

| Chỉ số | TB | SD | Khoảng (TB ± 2SD) |
|---|---|---|---|
| 字/đoạn | 24,86 | 3,03 | 18,8 – 30,9 |
| 字/câu | 22,72 | 2,82 | 17,1 – 28,4 |
| lượt thoại | 39,13 | 13,35 | 12,4 – 65,8 |
| 字/lượt thoại | 12,59 | 3,85 | 4,9 – 20,3 |
| % đoạn có thoại | 35,03 | 9,21 | 16,6 – 53,5 |
| giảng huấn /1.000 | 1,50 | 1,00 | 0 – 3,5 |

Đây là chỗ tôi đã sai lần đầu: lấy **chương 1** làm chuẩn thì nó có 19,7 字/đoạn, nên bản sinh 26,7 bị coi là
lệch 36% — trong khi so với 30 chương thì 26,7 nằm trong khoảng thường gặp. Một chương chỉ là một mẫu thăm dò.

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

Vì sao nó vẫn báo ĐẠT: `so-sanh` đời đầu chỉ **in bảng rồi trả `exit 0`**, không có phán quyết; người chạy tự
kết luận theo ngưỡng nó tự nghĩ ("thoại 14–22 lượt", "20–30 字/lượt"). Bài học không phải "hãy thêm phán quyết
bằng số" — mà là **bỏ việc chấm bằng số**, để chỉ còn một người chấm: Tác giả đọc.

**Giảng huấn** là chỉ số mới: người kể giảng giải — chân lý chung, quy tắc nghề, giải thích ngành
(「编辑部的生存法则是冰冷的」, 「在这个年份，东京不会同情…」, 「一个新人作者通常需要…」). Đây là thứ
Tác giả gọi là "nói linh tinh", và trước giờ không cột nào đếm nó.

## Ca thứ hai: bốn bản `v1`/`v2-ch01-a·b` (manga-v7)

Chạy cùng một chương mẫu, đổi đúng một thứ: SI có con số nhịp hay không.

| | 字/đoạn | 字/câu | đoạn dài nhất | 字/lượt thoại | giảng huấn |
|---|---|---|---|---|---|
| Mẫu ch.1 | 19,7 | 21,9 | **93** | 8,8 | 1,28 |
| v1-a (SI: 10–25, median 15) | 10,4 | 11,2 | **21** | 8,1 | 0,98 |
| v1-b | 13,8 | 15,1 | **38** | 7,1 | 0,66 |
| v2-a (SI: 18–28, median 21) | 18,4 | 20,2 | **44** | 10,0 | 0,39 |
| v2-b | **21,6** | **23,0** | **54** | 12,2 | 1,2 |

Đọc bảng này cho đúng: **con số đúng bằng mẫu thì kéo được thống kê khớp mẫu gần như tuyệt đối** —
v2-b ra 21,6 / 23,0 so với 19,7 / 21,9. Nên câu "số làm Writer kém đi" là quá mạnh và **không đúng với số liệu**.
Điều đúng là:

- Con số *sai* (thấp hơn mẫu) kéo văn co lại theo (v1: 10–14 字/đoạn, không đoạn nào quá 21 chữ).
- Con số *đúng* kéo thống kê khớp mẫu **mà trang vẫn không mở ra**: đoạn dài nhất 44–54 so với 93 của mẫu.
- Và chính vì khớp số, bản v2 **được chấm ĐẠT** trong khi Tác giả đọc vẫn thấy chưa đạt.

**Kết luận:** số làm Writer tối ưu cho số. Khớp thống kê không phải khớp văn, và khớp thống kê tạo cảm giác an
toàn giả — đó mới là lý do bỏ nó, không phải "bỏ vì nó làm văn tệ hơn".

## Bỏ khối LENGTH

Tác giả quyết định 01/11: *"Con số đếm là vô nghĩa trong văn học, nó chỉ khiến Writer kém đi. Nếu phần SI khác
viết tốt, anchor đúng thì không cần khối Length."* Khối LENGTH đã bị xoá khỏi `writer/SI-template` (v6), và xoá
luôn **mọi** con số nhịp rải ở chỗ khác (PART 1 mục 1, phần thoại) — vì bỏ riêng LENGTH thì bốn chỗ còn lại vẫn
ra lệnh bằng số. Không thay bằng khối số khác: không có khối nào cả.

Nhịp do hai thứ gánh:

1. **Anchor**: mỗi nguyên tắc lời kể đi kèm một đoạn nguyên văn từ bộ mẫu có đúng nhịp muốn có, và **có cả đoạn
   ngắn lẫn đoạn mở ra**. Anchor chỉ toàn dòng ngắn thì dạy đúng cái tật đang muốn chữa — chọn anchor theo đó.
2. **Nguyên tắc viết bằng lời**, không bằng số: tả nhịp bằng cái người đọc thấy ("một đoạn mở ra chở sự việc và
   cái giá; quanh nó là những dòng ngắn"), không bằng "median 21 characters".

Nếu bản ra vẫn băm vụn mà anchor đã đủ loại cảnh thì vấn đề ở **chọn anchor**, không phải ở thiếu con số.

## Một việc thôi

| Việc | Ai làm |
|---|---|
| Viết có ra truyện không | **Tác giả đọc** `ghep-cap` → file đọc cặp |
| Chẩn đoán khi cần (không phải điểm, không phải cổng) | `so-sanh` in bảng, luôn `exit 0` |

`so-sanh` chỉ còn là **kính lúp**: nó in ra vài cột lệch để biết nhìn chỗ nào, rồi thôi. Không chấm ĐẠT/KHÔNG ĐẠT,
không dùng số làm đích, không đưa số vào SI. Chỗ duy nhất nó còn chặn là bản **cụt** (dưới 800 chữ Hán) — đó là lỗi
kỹ thuật, không phải lỗi văn.

## Quy trình

1. **Tách đáp án** — chọn một chương mẫu, ưu tiên chương 1 (mở truyện, cùng loại cảnh với đoạn sắp viết):

   ```
   python tools/hieu_chuan.py tach --file 我在泡沫东京画漫画.txt --chuong 1 --out chung/hieu-chuan/manga/ch01
   ```

2. **Viết `brief.md`** trong thư mục đó: chỉ **sự việc** của chương — ai, ở đâu, muốn gì, chuyện gì xảy ra, dừng
   ở đâu, và các con số. Không chép câu văn, không chép thoại, không chép độc thoại nội tâm, không chép phần
   giảng giải bối cảnh. Mẫu: `manga/ch01/brief.md`.

3. **Dựng SI** từ `writer/SI-template` v6 — **không có khối LENGTH, không có con số nhịp**. Anchor là chỗ duy nhất
   dạy nhịp, nên chọn anchor có **cả dòng ngắn lẫn đoạn mở ra**. Kiểm anchor:

   ```
   python .claude/skills/novel-craft/scripts/verify_anchors.py <si> 我在泡沫东京画漫画.txt
   ```

4. **Chạy Writer** bằng SI đó — **2 lần**, hai chat mới:

   ```
   python tools/aistudio_run.py --new --si <truyen>/gemini/si-dan-gemini.txt \
       --prompt chung/hieu-chuan/manga/ch01/brief.md --out <truyen>/gemini/test-giong/v1-ch01-a.md
   ```

5. **Ghép bản đọc cặp** (đây là việc chính, không phải bước phụ):

   ```
   python tools/hieu_chuan.py so-sanh --goc chung/hieu-chuan/manga/ch01/goc.txt \
       --sinh <truyen>/gemini/test-giong/v1-ch01-a.md --doc-cap <truyen>/gemini/test-giong/doc-cap.md
   ```

6. **Đọc `doc-cap.md`** — 12 cặp đoạn, mẫu bên trái, bản sinh bên phải. Chỗ nào bản sinh nói thứ mẫu không nói,
   hoặc bỏ thứ mẫu có, ghi thành việc cụ thể ("SI thiếu nguyên tắc về lượt thoại ngắn"), không ghi "văn chưa hay".

7. **Tác giả chấm.** Không ai khác chấm bước này. ĐẠT thì mới dựng bible. Chưa ĐẠT thì sửa **anchor hoặc nguyên tắc
   viết**, chạy lại — không sửa con số, vì không còn con số nào.

8. Ghi `can-thiep` + `phan-quyet` vào `chung/loi/` (kết luận có thể là `tac-gia-bac` kèm nguyên văn câu bác).

## Đích của bài kiểm tra

Không phải "giống mẫu từng câu" — nội dung sẽ khác vì Writer tự chọn cách đi. Đích là biết **SI có dạy được giọng
của bộ mẫu hay không**, trước khi tốn công dựng bible và dàn ý. Câu trả lời do Tác giả đọc mà ra; bảng số chỉ giúp
khoanh vùng để nhìn.

## Vì sao không dùng luôn đoạn 001 của truyện thật để thử

Vì lúc đó nội dung do bạn tự nghĩ ra, nên không có gì để so. Không có đáp án thì "hay/dở" là cảm nhận, và cảm
nhận không chỉ ra được phải sửa dòng nào trong SI. Bài kiểm tra này chỉ dùng để **chốt SI**; chất lượng truyện
thật vẫn phải đọc như mục 5 của `SKILL.md`.
