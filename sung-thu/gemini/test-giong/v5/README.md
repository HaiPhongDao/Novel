# v5 — sửa ở tầng prompt, SI giữ nguyên v1

Tác giả 05/11 bác v4: "Đều không đạt. Tìm cách khắc phục đi".

**Vì sao chuyển sang prompt.** Năm bản SI (v1, v2, E, N, EN) × 2 lần chạy: dấu hiệu giọng MC trong lời kể không nhích
(！/？ lời kể 0–0,56 /1.000, gốc 5,32; ngôi một trong lời kể 0, câu thuật lại việc nghĩ 1–9). Ở v4, **không một chữ** của
ví dụ ch2 trong SI bị chép sang ch3 — Writer bỏ qua hẳn khối đó. Chỗ duy nhất từng ra giọng (v2–v3, 7/8 bản) là chỗ
**brief** ghi "một câu phản ứng trong đầu". Prompt lượt người dùng là một bản thuật tiếng Việt ngôi ba, và Writer dịch nó.

| Bản | Prompt (SI = v1 cho cả ba) | Thêm gì so với brief ch3 cũ |
|---|---|---|
| **P1** | `brief-P1.md` | khuôn brief thật của dự án: "Viết tiếp…", khối nối tiếp nguyên văn đuôi ch2 (【接上】, 328 字), bỏ câu "bài kiểm tra / viết lại chương" |
| **P2** | `brief-P2.md` | P1 + ví dụ brief → văn ch2 đặt **trong prompt** (khối GIỌNG MẪU), không trong SI |
| **P3** | `brief-P3.md` | P2 + bảy chỗ đánh dấu "trong đầu cậu bật ra một câu, bằng giọng cậu" (chỉ đánh dấu dịp, không giao lời) |

Ba bản xếp chồng: P1 so v1 = tác dụng của khối nối tiếp; P2 so P1 = ví dụ trong prompt; P3 so P2 = đánh dấu dịp.
P2/P3 có ~170 câu tiếng Trung (văn mẫu ch2) — cố ý theo chỉ dẫn Tác giả; kiểm chép bằng grep 占卜|珍珠|奶牛|虎鲸|星贝|面包.
