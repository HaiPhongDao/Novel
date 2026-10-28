# Test SI v1 + kiểu prompt trên chương 1 bộ mẫu (vòng mẫu 1, 29/10)

Tác giả: "chạy prompt trích xuất từ đoạn đầu văn mẫu để kiểm tra SI và cách prompt trước".

- **Cảnh:** chương 1 bộ mẫu (`goc-t1.txt`, tên đổi romaji), cảnh Kurokawa hút thuốc ở cửa sau 讲谈社 gặp Akiyama.
- **Prompt:** `prompt-t1.md`, cùng hình dạng brief 001 của truyện (mẫu A: một đoạn văn xuôi + chỗ dừng + State JSON ở cuối). Chỉ có sự việc, không dặn văn.
- **SI:** `si-test-v1.txt` = `gemini/si-v1.txt`, chỉ đổi ví dụ tên ở mục Names.
- **Chạy:** hai bản cùng prompt, chat mới, Gemini 3.8 Flash Thinking High: `T1-a.md` (/u/0, 139 giây), `T1-b.md` (/u/1, 147 giây). Raw: `*-raw.md`.
- **Giới hạn:** chương 1 nằm **trong** anchor của SI (anchor 2 và anchor 5 lấy từ chương này), nên phép đo nhịp bị lệch về phía mẫu, và Writer chép được nội dung anchor (xem mục 3). Mới có một cảnh, chưa có cảnh lời kể/số liệu loại thứ hai.

## 1. Bốn số giọng (`python do.py goc-t1.txt T1-a.md T1-b.md …`)

| bản | chữ Hán | câu | chữ/câu | lượt thoại | chữ/lượt | tỷ lệ thoại | dòng <15 chữ | so sánh/1000 |
|---|---|---|---|---|---|---|---|---|
| **gốc** | **2.191** | 118 | **18,6** | **46** | **8,4** | **18%** | **53%** | 0,91 |
| T1-a | 3.716 | 170 | 21,9 | 25 | 11,8 | 8% | 34% | 1,61 |
| T1-b | 4.851 | 212 | 22,9 | 38 | 15,7 | 12% | 40% | 3,92 |
| đoạn 001 thật (đối chiếu) | 3.271 | 155 | 21,1 | 23 | 22,0 | 15% | 40% | 2,14 |

## 2. Đọc ra gì

1. **Dài gấp 1,7–2,2 lần gốc.** Brief ghi "khoảng 2800 chữ" (chương gốc 2.858 ký tự kể cả dấu = 2.191 chữ Hán), bản ra 3.716 và 4.851 chữ Hán. Một phần do con số của mình đếm cả dấu; phần lớn do Writer kể dày từng beat.
2. **Thoại hỏi–đáp nhanh của mẫu biến thành lời kể giải thích.** Gốc có 46 lượt, 8,4 chữ/lượt: hai người ném qua ném lại từng câu ngắn, cái hài nằm ở nhịp đó. Bản sinh còn 25–38 lượt, mỗi lượt là một tràng giải thích, và chỗ trống được lấp bằng lời kể suy luận (Kurokawa tự giải thích vì sao đoán ra anh muốn gửi bài; Akiyama kể lể làm 16 tiếng một ngày). Brief không có dòng tỷ lệ thoại/lời kể (skill `si-test-tren-mau.md` mục 4); SI mục 5 thì dạy "một lượt nói trọn một ý", tức dạy lượt dài.
3. **Mất cú hài cuối của mẫu.** Gốc kết bằng "“你？” / 秋山悟惊叹于一个保洁还有这权利。": tới cuối anh vẫn tưởng cô là lao công. Cả hai bản đều để anh hiểu cô là người trong toà soạn, vì prompt không ghi "anh vẫn tưởng cô là nhân viên tạp vụ". Cú hài dựa trên một hiểu lầm phải nằm trong brief.
4. **Nhịp dòng chưa tới.** Dòng dưới 15 chữ: 34–40%, gốc 53%. Câu 21,9–22,9 chữ, gốc 18,6.
5. **Tật quen của model:** 倒吸了一口凉气, 瞳孔微微放大, 心里咯噔一下, 淡淡地说道, 语气平淡得像…; so sánh người kể 1,6–3,9/1000 (gốc 0,9).
6. **Chép nội dung anchor** (do cảnh nằm trong anchor): Yano, 大粪, 暴走族…返乡再就业, 长矛/械斗 đều có mặt ở T1-a/T1-b. A còn mở bằng "太阳缓缓西斜" — chép câu mở của anchor 1. Đoạn 001 thật không có những từ này.

**Đúng:** các beat theo đúng thứ tự brief, dừng đúng chỗ, cú đưa thuốc của Kurokawa giữ được, bối cảnh thời buổi nằm trong đầu cô.

## 3. Ba hướng sửa (mỗi hướng một bản, chờ Tác giả chọn)

| Hướng | Tầng | Sửa gì |
|---|---|---|
| A | brief | Độ dài ghi bằng chữ Hán đúng của mẫu (~2.200); thêm một dòng tỷ lệ "phần lớn cảnh ở quầy là hỏi–đáp ngắn qua lại"; ghi hiểu lầm cần giữ tới cuối đoạn |
| B | SI | Mục 5 (thoại) thêm một nhịp thứ hai: người lạ hỏi–đáp thì mỗi lượt một câu ngắn, anchor lấy từ đoạn hỏi–đáp của mẫu (chương 1 dòng 54–71 hoặc một cảnh ngoài chương 1) |
| C | SI | Rút SI về khoảng 9.000 ký tự (hiện 18.787; skill ghi SI chạy tốt ở 7.000–8.000) và thay các anchor lấy từ chương 1–3 bằng cảnh ở chương sau, để Writer khỏi chép nội dung |

Tác giả từng nói ở truyện khác: "truyện cần viết đầy đủ, không cần giống người thật nói" (`references/si-khung.md`). Hướng B đi ngược câu đó cho riêng lane này, nên cần Tác giả quyết.
