# Review — Đoạn 001, vòng thử 1 (SI v1, 3 hình dạng prompt)

Bản: `gemini/test/doan-001/{a,b,c}.md`, prompt cùng thư mục. Gemini 3.8 Flash, /u/0 · /u/1 · /u/2, 28/10.
Lần chạy đầu 27/10 treo cả 3 tab vì "Permission denied" trong lượt Model mà extension không đọc khi request còn treo — đã vá extension, chạy lại.

| Bản | Prompt | 字 | Đoạn văn trung vị | Lượt thoại | 字/lượt | Phủ định/实/so sánh | Chép khung anchor |
|---|---|---|---|---|---|---|---|
| a | theo dàn ý | 2681 | 30 | 22 | 21,3 | 0/0/0 | A3 "这就是典型的政治流放了"; A1 cả khung "在洛伦看来…还有…还有…总之"; A1 "就在…的这段时间里"; A2 "要不了半年…甚至会有人拆…当柴烧" |
| b | + dòng thể loại/giọng | 2275 | 27 | 26 | 22,2 | 0/0/0 | A3 "这是典型的资产减值处理"; A2 "到了那时候…拆光…当柴火"; A1 "不过在洛伦看来" |
| c | + MC tính sổ trước | 2702 | 29 | 17 | 20,8 | 0/0/0 (1 nhãn) | A3 "这是一次典型的豪门坏账剥离"; A2 "在赫伯特看来…到了…" |
| mẫu ch1–150 | — | — | 62 | 9,0/1000字 | 22,6 | so sánh 0,66/1000字 | — |

## Lỗi chung (tầng SI)
1. **Anchor lời kể bị chép khung 3/3** — giống `chuyen-chuc` v4. Câu "典型的X" của A3 có ở cả ba bản.
2. **LAYOUT không ăn:** cả ba viết một câu một dòng, đoạn trung vị 27–30 字 (mẫu 62).
3. **赫伯特 tự xưng 属下** (a, b) — sai register; glossary cần 小人.
4. Writer tự đổi đơn vị sang 吨 và tính sai (a: 3.600 袋 ≈ 540 吨; c: 1,44 triệu cân ≈ 1.400 吨).

## Từng bản
- **a** — mạch gọn, mở bằng thân thể + trí nhớ, cảnh lửa và câu hỏi cuối tốt ("醒来之后的第四句话"). Đoạn kế hoạch nông cụ là chép khung A1.
- **b** — yếu nhất: 加尔文 nói "族长派我送你来锈河属地当卫队长" (lẫn vai); giọng hài không rõ hơn a dù có dòng thể loại.
- **c** — dày chất liệu nhất (42 con bò, 150 cày, 4 người kéo một cày, bóc vỏ cây du), MC ra lệnh đầu tiên (gom 7 thợ rèn đúc cày), cãi lại 加尔文 một câu. Sai canon: "公爵父亲", "西南边陲", "七个村落" (bible: 23 làng).

**Kết luận:** chưa chốt bản nào. Khuyến nghị: hình dạng prompt **c**, SI sửa lỗi 1–3 rồi chạy lại.
