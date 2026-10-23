# Mổ xẻ truyện top (拆书) — học cơ chế từ truyện mẫu

Dùng khi Tác giả đưa một truyện mạng đang ăn khách để học: mở truyện, nhịp điểm sướng, cách móc giữa các chương, cách bàn tay vàng lộ dần, giọng văn. Kết quả phục vụ **lập kế hoạch** (overview, arcs, outline, brief) và **mẫu giọng tham khảo**; không đi thẳng vào SI hay canon.

Phương pháp chuyển thể từ `story-long-analyze` của oh-story-claudecode (MIT) — xem [tham-khao-ngoai.md](tham-khao-ngoai.md). Tình trạng: **đề xuất, chưa chạy thử trong repo**.

## 1. Ranh giới khi mổ xẻ

1. Chỉ kết luận từ văn đã đọc. Thiếu thì ghi "văn chưa nói rõ", không bịa để điền cho đủ ô.
2. Sự kiện cứng ghi kèm vị trí (chương + 5–15 chữ định vị). Suy luận thì ghi là suy luận.
3. Tách bốn thứ tự: **chuyện xảy ra lúc nào** / **văn tiết lộ lúc nào** / **độc giả biết tới đâu** / **nhân vật nào biết**. Phần hay của truyện top thường nằm ở khoảng lệch giữa bốn thứ này.
4. Tách ba trục khi nói về nhịp: sự kiện tiến bao nhiêu, cảm xúc người đọc ra sao, văn giãn hay nén. Điểm số không thay được lời giải thích.
5. **Chỉ rút cơ chế trừu tượng.** Không mang sang tên, thiết lập riêng, tổ hợp nhân vật, chuỗi sự kiện then chốt, cảnh biểu tượng hay câu văn (KN11). Không suy ngược kết quả thành "tác giả mẫu đã tính trước".

## 2. Lưu ở đâu

```
mo-xe/<ten-truyen-mau>/        # ở gốc repo — dùng chung cho mọi truyện của mình
├── tong-quan.md               # thông tin cơ bản, khung truyện, hợp đồng độc giả, bài học chính
├── 3-chuong-dau.md            # mổ xẻ chương 1–3 (mục 3)
├── tom-tat-chuong.md          # mỗi chương một dòng bảng (mục 4)
├── nhip-va-cam-xuc.md         # đơn vị cốt truyện, nhịp ba trục, thẻ mô-đun cảm xúc (mục 5)
├── nhan-vat-thiet-lap.md      # vai chức năng, cách bàn tay vàng lộ dần (mục 6)
└── van-mau.md                 # 4–6 trích đoạn 300–500 chữ có định vị (mục 7)
```

**Không commit toàn văn truyện mẫu.** Toàn văn để ở máy Tác giả hoặc trong `mo-xe/<ten-truyen-mau>/nguyen-van/` (đã có trong `.gitignore`); repo chỉ giữ phân tích và trích đoạn ngắn có định vị.

Chương truyện mạng thường 2.000–3.000 字, gần bằng một **đoạn** của repo. Khi rút số liệu nhịp (vd. "điểm sướng mỗi 3 chương") áp sang đoạn theo tỉ lệ đó, ghi rõ là quy đổi.

## 3. Ba chương đầu (黄金三章)

Mỗi chương một khối:

```markdown
### Chương N — ~X chữ — sự kiện lõi: <một câu>

**Móc mở** (500 chữ đầu): loại <hồi hộp / xung đột / tương phản / lệch thông tin / nhập vai> | làm bằng gì | hiệu quả <mạnh/vừa/yếu> vì …
**Nhân vật lên trang**: … | MC được dựng bằng <tả thẳng / thoại / việc làm / người khác nói> | ấn tượng đầu: …
**Thế giới**: lộ … | giấu … | qua <thoại / lời kể / sự kiện>
**Cấu trúc**: | khúc | chức năng (đệm / xung đột / sướng / thu) | ~chữ |
**Điểm sướng**: loại | đệm ~X chữ / xả ~Y chữ | đường cảm xúc
**Tầng phản ứng** (nếu có): nghi ngờ → sốc → người mạnh đánh giá lại → lan ra | ai, phản ứng gì, dài bao nhiêu
**Leo thang xung đột** (nếu có): lời nói → kinh tế → bạo lực …
**Chỗ dừng chương**: loại móc (bảng ở [xay-dung-truyen.md](xay-dung-truyen.md) mục 7) | dừng đúng ở nhịp nào
**Học được**: <kỹ thuật có thể dùng — viết dưới dạng thao tác, không chép cảnh>
```

Chương 2–3 xem thêm: mật độ thông tin, xung đột có leo hơn chương trước không, khoảng cách giữa hai điểm sướng (tính bằng chữ).

Truyện tình cảm: thay "điểm sướng" bằng nguồn căng thẳng quan hệ (hiểu lầm / chênh thân phận / ân oán / khế ước), quan hệ tiến một bước từ đâu tới đâu, độc giả đang chờ ai bày tỏ với ai. Đối thủ không phải người (thiên tai, mùa đông, dịch bệnh — gần với Lãnh Chúa Chip): ghi mặt đối kháng, nguồn gấp gáp, cơ chế leo thang và thứ thay cho "vả mặt".

## 4. Tóm tắt từng chương

Một dòng bảng mỗi chương, không viết văn xuôi dài:

| Ch | Sự kiện | Trạng thái đổi | Ai biết thêm gì | Chỗ dừng | Ghi chú |
|---|---|---|---|---|---|

**Trạng thái đổi** chọn trong bảy loại: mục tiêu / rủi ro / thông tin / quan hệ / tài nguyên / thân phận / lập trường cảm xúc. Chương không đổi trạng thái nào là chương "lót" — đếm xem truyện mẫu có bao nhiêu và đặt ở đâu.

## 5. Cốt truyện, nhịp, mô-đun cảm xúc

**Khung truyện** (một bảng ở đầu `nhip-va-cam-xuc.md`): loại khung (thăng cấp / báo thù / đơn nguyên / đa tuyến / trưởng thành / tình cảm / lai) · động cơ lõi một câu · mâu thuẫn trục · cơ chế nâng cấp (sức mạnh / địa vị / quan hệ) · chu kỳ nhịp điển hình (đệm → xung đột → sướng → hồ mới) · căn cứ ở chương nào.

**Đơn vị cốt truyện** — gộp chương thành từng mạch có mục tiêu riêng (30–100 chương thường ra 5–15 đơn vị). Mỗi đơn vị:

| Mục | Nội dung |
|---|---|
| Mục tiêu ban đầu | ai muốn gì, đo được |
| Trở ngại chính | người / luật / tài nguyên / thông tin / môi trường |
| Nguồn đổi cục diện | lựa chọn của ai, hay sự kiện ngoài — không mặc định là MC |
| Cục diện đổi | từ trạng thái nào sang trạng thái nào |
| Được – mất | ai được gì, ai trả giá gì |
| Hệ quả | đẩy, chặn hay ép hành động sau thế nào |
| Chức năng thông tin | độc giả nhận / chờ / hiểu sai / được xác nhận điều gì |
| Nhu cầu độc giả | an toàn / hơn người / chờ đợi / bù đắp cảm xúc / đảo nhận thức / bầu bạn |
| Chương | X–Y |

Mạch quá nhỏ (một sự kiện 1–2 chương) gộp vào mạch chứa nó; quá to (một chủ đề trăm chương) tách ra.

**Nhịp ba trục** cho từng đơn vị: sự kiện tiến 1–5 · cảm xúc người đọc (loại + cường độ 1–5, do đâu) · độ giãn văn 1–3 (giãn / nén / lược / lặp, để làm gì).

**Thẻ mô-đun cảm xúc** — ít nhất 3 thẻ cho 3 cơ chế mạnh nhất của truyện mẫu:

```markdown
### EM-01 <tên ngắn>
Khoảng trống: người đọc thiếu/muốn gì
Trì hoãn: văn giữ lại bằng cách nào, bao lâu
Xả: trả bằng việc gì, ai trả, ai chứng kiến
Dư âm: sau khi trả, người đọc được gì thêm, mở ra mong chờ nào
Có thể lặp lại khi: điều kiện để dùng lại trong truyện của mình
```

## 6. Nhân vật và thiết lập

- **Vai chức năng** của nhân vật phụ: người dẫn, người nghi ngờ, người chứng kiến, người bị vả, người giữ cửa, người bầu bạn… Rút vai, không rút người.
- **Bàn tay vàng lộ dần thế nào**: lần đầu lộ chức năng gì, giới hạn gì được nói ra lúc nào, mỗi lần mở khoá gắn với giá gì.
- **Quan hệ**: bảng quan hệ đổi theo đơn vị cốt truyện.

## 7. Văn mẫu

4–6 trích đoạn 300–500 chữ liền, không trùng nhau, mỗi đoạn ghi `chương + định vị`, không khí (căng / nặng / nhẹ / ấm / sục sôi) và **điểm minh hoạ** (nhịp câu, dấu câu, thoại có ẩn ý, hành động–phản ứng…). Dùng để bàn với Tác giả về giọng; muốn đưa vào SI hay voice-anchor phải qua Tác giả duyệt (AGENT.md mục 5b).

## 8. Từ mổ xẻ sang truyện của mình

Cuối `tong-quan.md` ghi "**Mang sang**": mỗi dòng một kỹ thuật, kèm chỗ sẽ dùng (`bible/overview.md` → hợp đồng độc giả; `plot/arcs.md` → neo arc; brief đoạn nào) và điều **không** mang sang (tên, thiết lập, cảnh biểu tượng). Kỹ thuật dùng thử trong brief rồi review mới đủ căn cứ ghi vào [kinh-nghiem.md](kinh-nghiem.md).

## Tra nhanh

| Loại điểm sướng | Là gì |
|---|---|
| Vả mặt | thực lực đè người đã coi thường |
| Lật ngược | tuyệt cảnh xoay chuyển |
| Cơ duyên | có được thứ người khác không có |
| Lệch thông tin | MC và độc giả biết điều người khác không biết |
| Thoả mãn tình cảm | quan hệ tiến, được công nhận, đoàn tụ |
| Giả heo ăn hổ | che thực lực rồi lộ ra |

Điểm sướng = va chạm hai logic: logic số đông (đối thủ không thể thắng) và logic MC (bình thản, đã chuẩn bị). Khoảng cách càng lớn càng sướng. Ba vai: người đứng ngoài có lập trường nâng đối thủ lên rồi phải đổi giọng; đối thủ đủ đáng ghét; MC lúc đệm thì kín, lúc xả thì gọn. Đạo cụ, người, thực lực phải chuẩn bị **trước** cú xả — thiếu thì độc giả lo lắng thay, sướng thành ngược.
