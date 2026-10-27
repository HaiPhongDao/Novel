# Review — đoạn 001 (vòng thử hình dạng prompt)

SI v1 (`gemini/si-dan-gemini-v1.txt`), cùng model, mỗi bản một chat mới, 27/10. Prompt: `gemini/test/vong-001/prompt-{a,b,c}.txt`.

| | a — sự việc tuần tự | b — khung đặt hàng (thể loại · thế giới · MC · hôm nay) | c — tối giản |
|---|---|---|---|
| Prompt (từ) | 248 | 283 | 119 |
| 字 | 1.973 | 1.793 | 1.530 |
| Dòng / 字 mỗi câu | 177 / 11,1 | 149 / 12,1 | 154 / 10,1 |
| Dòng 【】 | 9 | 14 | 9 |
| Lượt thoại | 34 | 21 | 12 |
| Dòng mở bằng 江野 | 9 | 7 | 9 |
| Tật đo được (phủ định, 实, nhãn, so sánh, thẻ) | 0 | 0 | 0 (+1 `不是…是…` tách dòng, máy không bắt) |
| Lệch canon | "三年前" ×3 (canon: năm năm), tiền tệ 联盟币/铜币 | 苏清寒 ra 极寒法师 (bible: 霜语者); `拿著` (chữ phồn) | "三年前", 联盟币 + 元, 手环, 基因药剂, 少校军衔 — thế giới trôi sang hiện đại; chuyển chức ở sân trường thay quảng trường |
| Tiền MC | 金币X4 银币X20 | 3 银币 40 铜币 | 312 联盟币 |

Cả ba bản sai tiền vì **brief không đưa số tiền và tên tiền tệ** — lỗi của brief, không của Writer (bible: 3.260 金币).

## Đọc

- **a** — Mở đúng: loa 镇守府, 30 ngày, rồi số thú triều; đám đông có người cụ thể (một lính đánh thuê cụt tay, một lão thợ săn) nói bằng số, đúng nguyên tắc 4. Đoạn đời MC dài và nhiều số (11.420 xác, 7 đồng một con) — chắc nhưng hơi kê sổ. Cảnh thức tỉnh C级 lạnh đúng tông: người tuyển mộ gạch tên anh. Sai năm.
- **b** — Đúng canon nhất (năm năm, 4,1 vạn học sinh, 镇渊军 tử 2,1 vạn). Có thêm câu tính toán trước khi lên đài ("总和24点… 韩擎 26点… 十二万金币淬体魔药"). Nhịp giống bộ mẫu nhất: 14 dòng 【】, màn hình lớn hiện kết quả công khai cho cả quảng trường. Kết bằng "chỉ anh thấy" hai dòng hệ thống. Thêm cảnh 苏清寒 thức tỉnh (prompt không bảo) — chấp nhận được, sai tên nghề.
- **c** — Giọng MC mạnh nhất: đoạn "他在计算" tự tính 30 ngày chỉ lên được cấp 8, 56 điểm, "活不过一分钟" — đúng kiểu MC lạnh tính bằng số. Kết bằng thời gian ngừng lại, ngầu. Nhưng prompt quá mỏng nên Writer tự dựng một thế giới hiện đại (tiền 元, vòng tay, thuốc gen, quân hàm thiếu tá) — sai register của bible.

## Kết luận về hình dạng prompt

**Hình dạng b** cho canon chắc nhất mà vẫn để Writer tự do cảnh: khối thế giới + khối MC + "hôm nay" làm Writer dựng đúng thế giới; prompt tối giản (c) cho giọng hay nhưng thế giới trôi. Dùng **b** cho các đoạn sau, và thêm vào khối số liệu: **tiền MC + tên tiền tệ (金币/银币), nghề của mọi người có tên trên đài**.

Bản đề xuất làm gốc: **b** (sửa nhỏ khi chốt: 极寒法师 → 霜语者, 拿著 → 拿着, tiền → theo bible hoặc đổi bible theo bản). Chờ Tác giả chọn.
