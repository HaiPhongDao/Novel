# Review đoạn 001 — vòng thử hình dạng prompt (26/10/2026)

SI v1 (`gemini/si-dan-gemini.txt`), Gemini trên AI Studio (acc sekanyuu, `/u/0`), mỗi bản một chat mới (`--new`).
Hai hình dạng prompt × 2 lần chạy để tách tác dụng của prompt khỏi nhiễu:

| Bản | Prompt | 字 | dòng | 字/dòng | ≤10字 | `X：“` | phản ứng trơ | 『』 | 【】 | ！/1k | ？/1k | cụm nhấn* | so sánh người kể | canon bàn tay vàng |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mẫu (ch.1–105) | — | 2.442 | 113 | 19 | 27% | ~14 | 10 | — | 1,8 | 25,8 | 19,0 | — | hiếm | — |
| a | tối giản | 3.047 | 202 | 17 | 28% | 44 | 11 | 20 | 5 | 57,1 | 14,4 | 20 | 0 | ❌ tự đặt `万物皆可蛀` |
| c | tối giản | 3.554 | 216 | 17 | 25% | 29 | 10 | 16 | 7 | 48,7 | 12,7 | 29 | 0 | ❌ tự đặt `概念级龋齿` + `牙菌斑` |
| b | đơn giản | 2.520 | 158 | 19 | 28% | 25 | 9 | 9 | 9 | 58,3 | 11,1 | 18 | 0 | ✅ 第1集 · 30 点 · 片尾复活 |
| d | đơn giản | 3.418 | 188 | 19 | 24% | 42 | 11 | 10 | 11 | 47,4 | 14,0 | 13 | 5 | ✅ 第1集 · 30 点 · 片尾复活 |

\* `瞬间 / 猛地 / 猛然 / 狠狠 / 轰然 / 死死`. `cong_doan.py` báo ĐỎ ở bản a vì câu cuối kết bằng `——`: bắt nhầm, đoạn dừng giữa cú lao đúng brief. Các band "chưa đạt" của `cong_doan` là band 领主, bỏ qua.

## Kết luận

- **Prompt đơn giản thắng ở canon**, cả hai lần: đúng tuổi kết khế 16, 30 收视点, 第1集, 片尾复活, kiếm 钟馗 của 唐棠, 土地公 của 马骁, 城北焚烧厂, hạn thứ Sáu.
- **Prompt tối giản để Writer tự dựng bàn tay vàng**, hai lần đều ra năng lực "làm sâu mọi thứ" và mượn chữ `概念` của mẫu; bản c còn đảo vai (马骁 thành 队长, 唐棠 thành 突击手) và lọt `天佑大夏` (tên nước trong 《斩神》). Giọng của hai bản này lại sống nhất (bản a: bác sĩ… → `两千八百块钱你让我讲什么义气？！`).
- **Lỗi chung cả bốn bản:**
  - `！` gấp ~2 lần mẫu.
  - Tỷ lệ thoại thấp hơn mẫu.
  - 13–29 cụm nhấn mỗi bản.
  - Ba bản quá dài (3.047–3.554 字, cửa sổ 2.000–2.400).
  - Mở đoạn bằng một khối kể tiểu sử dài 20–40 dòng.
- **Chọn gốc:** khuyến nghị **bản b** (độ dài đúng, canon đúng, 0 so sánh người kể); bản d có đoạn 齐乐 tính thiệt hơn ngay trước khi lao vào hay hơn b, nhưng lỗi so sánh người kể (`像是拿墨汁涂上去的`, `像一颗脱膛的人肉炮弹`, `如同一群…毒蛇`) và sai canon `只播了三集`.

## Lỗi canon / chi tiết từng bản

- a: kết khế "十八岁"; 唐棠 dùng `符文短刀`; 马骁 gọi `唐姐`; lương 2.800.
- b: một chữ `通` thừa đầu dòng 123 (lỗi Writer); lý lẽ "马骁一死…复评必然取消" rối; 马骁 gọi `唐队`.
- c: đảo vai 唐棠/马骁; `天佑大夏`; năng lực tự đặt; lương 3.500.
- d: phim "只播了三集" (canon: 26 tập); "1998重制版"; 5 so sánh người kể; dòng kết nhắc `精神病院`.

## Ý Writer tự đặt, đáng trình Tác giả

- 蛀牙大王 ngủ trong **chiếc răng hàm** của 齐乐, tỉnh dậy kèm cơn đau răng (a, c tự nghĩ ra, độc lập).
- Thông báo 【】 hiện như **chữ ghép bằng hạt kẹo / phụ đề** trên võng mạc (b, d).

## Đề xuất cho vòng sau (chưa áp dụng)

1. Giữ prompt đơn giản; thêm một câu sự thật "phim chiếu 26 tập thì bị cắt".
2. Ghi độ dài như cửa sổ ở đầu prompt và đặt đích thấp hơn (~1.900) vì Writer vượt.
3. Mở đoạn bằng việc đang xảy ra trong B2, tiểu sử 齐乐 để rải vào thoại (黄金三章: 300 字 đầu có người gặp nguy).
4. SI: hạ mật độ `！` (anchor đang dạy đúng, nhưng dòng LENGTH cần nói nhịp `！` theo cảnh) — cần Tác giả duyệt trước khi sửa.

**Kết luận review:** chưa chốt bản nào. Bản b là gốc khuyến nghị; chờ Tác giả đọc và chọn.
