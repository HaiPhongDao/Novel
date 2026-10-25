# Test giọng trên nội dung truyện mẫu (25/10/2026)

Mục đích: kiểm tra SI bằng **nội dung đã biết đáp án**. Lấy hai cảnh của `放开那个女巫` **không nằm trong
anchor**, viết prompt chỉ có sự việc (không dặn cách viết), chạy qua SI của truyện, rồi so bản ra với
nguyên văn — vì nguyên văn là thứ duy nhất tôi biết chắc giọng phải ra sao.

## Thiết kế

- SI dùng để test: `../si-test-v12.txt` / `../si-test-v13.txt` — đúng SI của truyện, chỉ đổi dòng tên
  riêng (Emeric · Osric … → Roland · Barov · Carter · Anna · Border Town). Mọi luật khác giữ nguyên.
- Prompt: `prompt-t1.md` (cảnh 理由, ch.5: Barov hỏi vì sao cứu nữ vu; Roland giải thích bằng vị thế
  thừa kế và cách đánh vào giáo hội; dặn Barov tổng hợp thương mại–thuế–xưởng trong ba ngày) và
  `prompt-t2.md` (cảnh 市场与循环, ch.47: điều khoản khế ước cho thuê máy phay — 10 đồng bạc/bộ bánh răng,
  2 đồng bạc/tuần tiền thuê, nguyên liệu lâu đài cấp; Carter hỏi sao không ghi 8; Roland giải thích quy
  ước nghề và vòng tuần hoàn).
- Nguyên văn đối chiếu: `goc-t1.txt` (1.512 字), `goc-t2.txt` (1.998 字).

## Kết quả

| cảnh | bản | chữ | số câu | tb chữ/câu | lượt thoại | chữ/lượt | phủ định | so sánh người kể |
|---|---|---|---|---|---|---|---|---|
| ch5 | **gốc** | 1.512 | 40 | **28,1** | 17 | **22,9** | 4 | 0 |
| ch5 | v11 | 1.798 | 27 | 39,5 | 19 | 38,5 | 4 | 1 |
| ch5 | v12 | 2.395 | 26 | **28,3** | **41** | 40,4 | 5 | 1 |
| ch5 | **v13** | 1.963 | 38 | **30,5** | 28 | 28,8 | 2 | 1 |
| ch47 | **gốc** | 1.998 | 54 | **34,0** | **4** | 40,0 | 3 | 1 |
| ch47 | v11 | 1.762 | 17 | 47,8 | 19 | 49,9 | 1 | 0 |
| ch47 | v12 | 2.187 | 28 | **28,8** | **32** | 43,2 | 2 | 0 |
| ch47 | v13 (T2) | 2.000 | 44 | 21,5 | **41** | 25,7 | 2 | 0 |
| ch47 | **v13 (T2b)** | 1.896 | 44 | 39,6 | **6** | 25,5 | 0 | 0 |

## Bốn phát hiện

**1. Neo độ dài câu trong SI thì hiệu quả.** v11 viết câu 39,5 và 47,8 chữ; thêm một câu "in this
register it lands around twenty to thirty characters" thì xuống 28,3–30,5 và 39,6 — gốc là 28,1 và 34,0.
Đây là chỗ duy nhất con số trong SI làm đúng việc.

**2. Neo độ dài lượt thoại thì phản tác dụng.** v12 nói "a turn runs one sentence of ten to twenty-five
characters" và số lượt thoại nhảy 17 → **41** (ch5), 4 → **32** (ch47): model đạt mục tiêu bằng cách
**chẻ lời nói thành nhiều lượt ngắn** và thêm lời kể giữa các lượt, nên tổng chữ cũng tăng. Đã bỏ con số
này ở v13 — chạy lại thì lượt về 28 (T1) và 41 (T2), tức con số cũ không phải nguyên nhân duy nhất.

**3. Chuẩn "0 lỗi" tôi đặt ra là sai.** Nguyên văn ch.5 có **4 cặp phủ định** và ch.47 có **3 cặp + 1 so
sánh**; tức chính truyện mẫu dùng khuôn đó ở mật độ vài chỗ mỗi đoạn. Tôi đã dồn các bản thử về 0, rồi
lại bắt lỗi khi nó quay lại — trong khi đích đúng là **mật độ và vị trí giống mẫu**, không phải bằng
không.

**4. Mật độ thoại do prompt quyết, không do SI.** Cùng SI v13, cùng cảnh ch47: prompt viết như đối thoại
(T2) → **41 lượt**; prompt ghi rõ "phần lớn là lời kể, chỉ vài lượt thoại" (T2b) → **6 lượt**, gần gốc 4.
Số lượt thoại là dữ kiện của brief, không phải luật của SI.

## Kết luận cho cách làm

- Trong SI chỉ giữ **một** neo số: độ dài câu (20–30 chữ). Các chỗ khác dùng ví dụ và anchor, không dùng
  con số — vì con số bị "đạt cho xong" theo cách khác với ý muốn.
- Mật độ thoại thuộc về **prompt** ("cảnh này phần lớn là lời kể, chỉ vài lượt thoại"), không thuộc SI.
- Review so với **mật độ của mẫu** (bảng trên), không so với 0. Lệch quá 2 lần mẫu mới là lỗi.
- v13 so với gốc: chữ 0,95–1,3×, số câu 0,8–0,95×, chữ/câu 1,09–1,16×, lượt thoại 1,5× ở cảnh lời kể và
  1,6× ở cảnh đối thoại. Đủ để coi v13 là mốc; chỉnh tiếp bằng brief, không chỉnh SI.

## Việc còn lại

1. ~~Chạy lại T1/T2 với v13~~ — xong: xem bốn dòng v13 trong bảng.
2. Chạy đoạn 001 của truyện mình một bản duy nhất với v13 + prompt có khối dữ kiện và tỷ lệ thoại, rồi
   chốt làm bản chuẩn của chương 1.
