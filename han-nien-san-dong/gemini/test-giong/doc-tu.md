# Từ lạ — đến từ đâu, sửa thế nào (09/11)

Tác giả: "vẫn chưa trừ được hết mấy từ linh tinh không biết dùng từ đâu? Lỗi này do đâu? Fix được không? Fix như nào?
Không fix bằng cách khác được mới dùng BANS."

## 1. Lỗi do đâu

Dò từng từ trên hai bản đoạn 003 chạy bằng SI Argon (`tools/tat_ai.py nguon`). Mỗi từ lạ — bộ mẫu dùng ≤ 2 lần — được tra
xem nằm sẵn trong SI, trong gói / brief, hay do Writer tự đặt. Ba nguồn:

| Nguồn | Từ (Writer / bộ mẫu) |
|---|---|
| **Danh sách "từ thời đại" trong SI Argon** | 鱼鳞册 9/0 · 家丁 5/0 · 庄头 3/0 · 红契 3/0 · 农户 2/0 |
| **Thẻ bàn giao Argon viết** | 界碑 15/0 (glossary ghi 界石) · 契纸 21/0 · 绿豆地 13/1 |
| **Writer tự đặt**, vì brief tiếng Việt ("mốc đá", "bẫy", "khế") không kèm chữ Trung | 荒坡 15/0 · 山梁 5/0 · 套子 4/0 · 下套 3/0 · 底契 4/0 · 公文 · 宣纸 |

Với cùng những thứ ấy, bộ mẫu dùng ổn định một chữ: 套索 (25 lần, 套子 0) · 设陷阱 · 山坡 · 文书 · 册子 · 床 (炕 0). Có những
thứ bộ mẫu không bao giờ nhắc tới (mốc đá, ruộng đậu, cổng núi). Với những thứ đó, mỗi lần chạy Writer lại chọn một chữ khác.

Câu chụp «坡田上下套子» là "在坡田上 · 下套子". App convert tách nhầm "上下" thành "trên dưới". Chữ 套子 thì đúng là lạ: bộ mẫu
không dùng.

## 2. Sửa thế nào (không dùng BANS)

1. **Bảng chữ bộ mẫu** [`bible/tu-mau.md`](../../bible/tu-mau.md): mỗi thứ trong truyện gọi bằng chữ bộ mẫu dùng nhiều nhất,
   có số đếm. Thứ truyện có mà bộ mẫu không có thì chọn một chữ bạch thoại, giữ cố định.
2. **Brief và thẻ bàn giao thêm dòng "Chữ cố định"**, ghi chữ Trung của những thứ cảnh cần lấy từ bảng trên. Glossary Writer
   không đọc, nên phải nằm trong brief.
3. **SI**: danh sách "từ thời đại" chỉ giữ chữ bộ mẫu thật sự dùng (bỏ 11 chữ bộ mẫu dùng 0 lần), kèm một câu: thứ của
   truyện thì dùng đúng chữ trong dòng "Chữ cố định", không đổi sang chữ đồng nghĩa → [`giong-v4/si-AT.txt`](giong-v4/si-AT.txt)
   (7.311 ký tự). Còn lại giữ nguyên chữ của SI Argon.

## 3. Kết quả (mỗi bản hai lần chạy, chat mới)

| /1.000 字 | SI cũ | SI Argon | **SI-AT + Chữ cố định** | bộ mẫu |
|---|---|---|---|---|
| từ lạ (chữ cổ + chữ tự đặt), đoạn 003 | — | 12,6 · 18,9 | **0,6 · 3,2** | |
| tật giọng AI, đoạn 003 | 16,2 · 15,2 | 4,93 · 1,95 | **0,30 · 1,17** | 0,44 |
| tật giọng AI, đoạn 001 | 6,6 · 6,8 | 0,30 (1 bản) | **1,05 · 0,37** | 0,44 |

Bản SI-AT dùng đúng 界石 (24 · 27 lần), 文书, 册子, 山坡, 套索, 设陷阱. Còn sót 荒坡 · 下套 · 套子 · 公文 · 原身 · 麸皮 · 灶台.
Những chữ này đã được thêm vào bảng (dùng 山坡 · 设陷阱 · 套索 · 文书 · 原主 · 糠 · 厨房).

Sổ: I-0072 hiệu quả. Đây vẫn là số đếm máy; câu "đọc có thuận không" chỉ Tác giả trả lời được.

**Lỗi chạy:** brief 001 bản Argon (`giong-v3/prompt-001-argon.md`) làm Writer treo ở cả 8/8 lần, trên mọi tài khoản. Brief
001 gốc thì chạy bình thường (cả với SI Argon lẫn SI-AT), nên đoạn 001 ở đây dùng brief gốc kèm dòng "Chữ cố định". Chưa
rõ vì sao bản Argon treo.

## 4. Đọc

- Đoạn 003, bản ít tật nhất: [`giong-v4/AT-003-a.md`](giong-v4/AT-003-a.md) (bản còn lại: `AT-003-b.md`)
- Đoạn 001: [`giong-v4/AT-001o-b.md`](giong-v4/AT-001o-b.md) (bản còn lại: `AT-001o-a.md`)
- So với SI Argon cùng đoạn: [`giong-v3/AR-003-a.md`](giong-v3/AR-003-a.md)
