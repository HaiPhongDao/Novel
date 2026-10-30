# Sổ số liệu đoạn 001–003 (Agent dựng, chờ Tác giả duyệt)

Mọi con số trong brief chép từ đây. Mọi dòng bảng 【】 trong brief phải khớp phép tính dưới đây.
Đơn vị: **1 vàng = 20 银 = 400 铜**; 1 斤 mạch = 1 铜.

## 1. Dòng thời gian và người

| đoạn | thời gian | người sống | chết | quỹ tiền | lương (斤) |
|---|---|---|---|---|---|
| 001 | ngày 0, sáng → chiều | 1.100 | — | 4 vàng 12 银 → 3 vàng 2 银 | 12.000 (11 ngày) |
| 002 | ngày 0 tối → ngày 3 | 1.100 (1 đấu sĩ gãy tay) | — | 3 vàng 2 银 → 3 vàng 12 银 | 8.700 → khẩu phần 0,6 斤 (13 ngày) |
| 003 | ngày 4 → ngày 10 | 1.100 | — | 3 vàng 12 银 → 10 vàng 8 银 | 4.080 (6 ngày) |

Phép tính (铜):
- **001:** `1.840 + 600 − 400 − 800 = 1.240` = **3 vàng 2 银**.
  (bán gươm nghi lễ 1 vàng 10 银 = 600; mua Grik 1 vàng = 400; lệ phí ấn 2 vàng = 800)
- **002:** vé `250×2 + 55×8 + 5×20 = 1.040`; 抽水 `12 vàng ÷ 10 = 1 vàng 2 银 = 480`; doanh thu `1.520`;
  trả 赏金 `3 vàng = 1.200`; 穷人捐 `1.200 ÷ 10 = 120`.
  → `1.240 + 1.520 − 1.200 − 120 = 1.440` = **3 vàng 12 银**.
- **003:** vé `1.180×2 + 190×8 + 30×20 = 4.480`; 抽水 `42 vàng ÷ 10 = 4 vàng 2 银 = 1.680`; doanh thu `6.160`;
  赏金 `6 vàng = 2.400`; 穷人捐 `240`; sửa một cổng ngày 4–9 `800`.
  → `1.440 − 800 + 6.160 − 2.400 − 240 = 4.160` = **10 vàng 8 银**.

## 2. Số ghế

- Ngày 0: 3.000 chỗ, chỉ dùng được **900** (3/4 cổng sập, nửa sân ngập).
- Ngày 4–9: sửa một cổng, kê thêm khán đài gỗ → **1.500** chỗ.
- 秋分: mở đủ **3.000** chỗ (mục tiêu arc 1, chưa làm trong 003).

## 3. Bảng in ra ở từng đoạn

- **001** — lúc ghi phiên 1 lên bảng:
```
【场次：第1场 · 三日后午时】
【看台：可用 900 / 3,000 席 · 票价 站席2铜 座席8铜 包厢1银】
【对局：Grik 对 车夫之子 · 真实胜率 58% / 42%】
【投注池：0 金币 · 抽水一成】
【账上：3金币 2银】
```
- **002** — lúc kết phiên 1:
```
【场次：第1场 · 已结】
【看台：310 / 900 席 · 门票 2金币 12银】
【投注池：12 金币 · 抽水 1金币 2银】
【账上：3金币 12银】
【名声：臭】
```
- **003** — lúc kết phiên 2:
```
【场次：第2场 · 已结】
【看台：1,400 / 1,500 席 · 门票 11金币 4银】
【投注池：42 金币 · 抽水 4金币 2银】
【账上：10金币 8银】
【名声：响】
```

## 4. Cái giá và hook từng đoạn

- **001:** cái giá — bán gươm nghi lễ của cha cho Voss giá rẻ (1 vàng 10 银), mua Grik 1 vàng, đóng ấn 2 vàng;
  hook — phiên 1 niêm yết, Grik bước ra cát.
- **002:** cái giá — ngày hội 1 lỗ, khẩu phần cắt từ 1 斤 xuống 0,6 斤, một đấu sĩ gãy tay, 名声 "臭";
  hook — Bram cởi huy hiệu vô địch đặt lên bảng, nhận đánh Grik.
- **003:** cái giá — Bram mất đầu gối trái (đi cà nhắc từ đây), Grik gãy hai xương sườn;
  hook — bảng in phiên 秋分: Grik 9% trước quán quân quận.

## 5. Những thứ phải giữ qua các đoạn

- Tên đã xuất hiện: Orin, Bram, Grik, Sabine, Voss, Aldric, 车夫之子 (biệt danh, không phải tên riêng).
- Grik: mua đứt ngày 0 giá 1 vàng, không còn là vật thế chấp; vòng sắt cổ chân tháo ngày 10.
- Bram: mắt trái mù, cụt hai ngón tay trái; đầu gối trái sưng sau đoạn 003.
- Aldric: thu 穷人捐 mỗi phiên; điều kiện "đến nhận thua hoặc chảy máu đầu tiên"; cấm "đấu thú" — Grik là *người*, không phải thú, nên hợp lệ.
- Quận: Voss cầm khế nợ; bá tước Gremont chưa lộ mặt; 12 kỵ binh đóng ở xóm ngoài.
- 秋分赛: trợ cấp 60 vàng, quận lấy nửa tiền vé, quán quân quận vào thẳng chung kết — 003 mới nghe đề nghị, chưa chốt.
- Thuộc đoạn sau: tên quán quân quận, giá chuộc nợ, vụ dàn xếp của Voss (chưa ai biết), cái chết đầu tiên trên cát.
