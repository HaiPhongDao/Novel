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

---

# Vòng 2 — anchor thoại (27/10)

Tác giả: a/b/c **không đạt** — thoại như giọng kể. Nguyên nhân trong SI v1: P4 dặn đám đông "nói câu đầy đủ, so bằng tên và con số" → mỗi lượt đọc một chỉ số. SI v2 = v1 bỏ câu đó + luật DIALOGUE mới (người nói với nhau, lượt sau phản ứng lượt trước, số nằm trong phản ứng) + PRINCIPLE 5 với một anchor thoại nguyên văn bộ mẫu, mỗi bản một anchor. Prompt chung: hình b + tiền 3.260 金币 + 霜语者. SI: `gemini/test/vong-001-thoai/si-D{1,2,3}.txt`.

| | b (v1) | d — D1 ch1 thầy giáo tán chuyện | e — D2 ch14 nghi bia hỏng | f — D3 ch6 học sinh cãi nhau |
|---|---|---|---|---|
| 字 | 1.793 | 1.821 | 1.665 | 1.700 |
| Lượt thoại | 21 | 26 | 29 | 36 |
| Lượt đọc số trơn (có số, không hỏi/cảm thán/tiểu từ) | 6 | 5 | 7 | 3 |
| Lượt có phản ứng (hỏi, 吗/吧/呢, ……) | 1 | 5 | 4 | 5 |

Đọc: có cải thiện ở chỗ hỏi–đáp (d: "你那时候在北城？" → "我叔父死在墙根下…" — một người hỏi, người kia trả lời bằng chuyện nhà mình). Nhưng phần lớn đám đông vẫn là chuỗi lượt mỗi lượt một sự kiện (e dòng 33–41: năm lượt liền đọc số thú triều). Anchor thoại một mình không đủ: phần lời kể quanh thoại — 75–87% văn bản — không có nguyên tắc nào, nên giọng báo cáo của lời kể lan sang thoại. Tác giả chỉ ra đúng chỗ đó → vòng 3: nguyên tắc lời kể.

---

# Vòng 3 — nguyên tắc lời kể (27/10)

Tác giả: SI thiếu nguyên tắc cho phần lời kể (phần lớn văn bản). SI v3 theo `writer/SI-template` v4: NARRATION N1–N4 trước (chuỗi bước → dòng chốt về MC; giải thích là chuỗi lời nói có từ nối; ý nghĩ MC chảy vào lời kể bằng câu hỏi; người kể có giọng, 按理说…但…), MOMENTS sau (trận đánh, lý do bằng số / tiêu tiền / bia kỷ lục, thoại). Ba hướng chia anchor, cùng prompt vòng 2. SI: `gemini/test/vong-001-loike/si-v3{A,B,C}.txt`.

| | b (v1) | f (v2-D3) | g — v3A: anchor lời kể + anchor cảnh (6) | h — v3B: chỉ anchor lời kể (4) | i — v3C: chỉ anchor cảnh (2), lời kể là luật |
|---|---|---|---|---|---|
| SI (ký tự) | 5.125 | 5.806 | 6.629 | 5.832 | 4.426 |
| 字 | 1.793 | 1.700 | 2.043 | 1.851 | 1.811 |
| Dòng lời kể | 114 | 122 | 140 | 156 | 143 |
| Dòng lời kể mở bằng từ nối (至于/但/而且/所以/要知道/也就是说/按理说/不过…) | 0 | 4 | 9 | 10 | 5 |
| Câu hỏi trong lời kể (ý nghĩ MC) | 0 | 0 | 0 | 2 | 3 |
| Lượt thoại / lượt đọc số trơn | 21 / 6 | 36 / 3 | 28 / 2 | 11 / 1 | 16 / 1 |
| Chép nguyên anchor (chữ trùng 8-gram) | — | — | **95** | 0 | 0 |
| Tật máy đo | 0 | 0 | 0 | 0 | 0 |

## Đọc

- **g** — Lời kể có giọng ("这就是边城的现实。城墙如果破了，谁都活不下去。"), nhưng **chép khung anchor N1** gần nguyên câu (在进行转职之前。普通人的四项基础属性…也就是说。寻常学生…学校也是从这方面去推算…在他们看来…) và chạy từ nối như checklist (至于…确实…但…而且…所以… liền năm dòng). Sai canon: MC "tới thành này ba năm", "全校前十", gọi 6 điểm là "满值". **Loại.**
- **h** — Người kể nói với người đọc thật: 要知道。临渊城坐落在帝国最北端; 按理说…但去年…; dòng chốt "3名S级。丢进面对100,000头凶兽的战场上，连填战壕都不够。" Đoạn tính tiền đi bằng giá đồ (50 / 1.500 / 15.000) và kết ở "chỉ đủ mua hai món 白银". Ý nghĩ MC khi thấy X级 chảy vào lời kể: "这X级……到底算什么等阶？" Thoại ít (11 lượt). Sai: "五年前来到这个世界" (bible: xuyên lúc sơ sinh).
- **i** — Tốt nhất. Mở bằng giác quan rồi mới tới số ("从裂缝里刮出来的风，带着陈年腐尸的腥味"). Lời phán đúng tông nghiêm: "按理说，这种底子有很大希望拿到B级职业。但在临渊城，B级也只是高级些的炮灰。" MC tính bằng số đúng kiểu nhân vật: 800 抚恤 + 2.460 tự kiếm = 3.260, "只要备齐穿甲箭，30天内…也能在兽潮前升到10级" — và chính phép tính đó là cái X级 sắp đập vỡ. Canon khớp (18 năm, 3.260 金币, 1 金币 = 100 银币). Lệch nhỏ: 韩擎 ghi 二中 (bible: 一中).

## Kết luận

Nguyên tắc lời kể có tác dụng: cả ba bản v3 có giọng người kể (từ nối, lời phán, câu hỏi trong lời kể), ba bản trước có 0. Anchor lời kể **không cần**: i (luật lời kể, không anchor lời kể) hay nhất và 0 chữ chép; g (đủ anchor) chép 95 chữ. Mỗi hướng n=1, nên mới là dấu hiệu.

Đề xuất: **SI v3C** làm SI của truyện; **bản i** làm gốc đoạn 001 (sửa 二中 → 一中). Chờ Tác giả đọc.
