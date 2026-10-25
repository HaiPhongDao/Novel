# Lãnh Chúa Khoa Học

**Logline:** CEO ngành phân phối vật tư công nghiệp xuyên vào lãnh chúa trẻ của vùng đất chỉ có mỏ đá
xỉ vô giá trị, đúng lúc phép thuật vừa thành ngành công nghiệp: anh không làm nổi một chiếc đinh và
không hiểu vì sao đá chịu lửa, nhưng anh biết định giá sự chắc chắn.

**Trạng thái:** mở truyện 25/10/2026. **Đã chốt tiền đề:** Phương án A · thế giới riêng (không chung
canon với Lãnh Chúa Mang Chip) · MC kiếp trước là CEO thương mại/tài chính. Bible đã chốt. SI bản
`gemini/system-instruction-v1.md` — 6 anchor lấy nguyên văn từ hai truyện cùng dòng (12.192 ký tự),
**chờ Tác giả duyệt và bản viết thử**. Truyện tham khảo + nguồn anchor: `archive/truyen-tham-khao.md`.
Ba phương án tiền đề và lý do loại: `archive/phuong-an-tien-de.md`.

## Writer

- SI đang dùng: `gemini/system-instruction-v13.md` (bản lõi 4 nguyên tắc, 4 ràng buộc, 3 anchor — 4.557
  ký tự). Bản test trên truyện mẫu: `gemini/test-giong/` (SI đổi tên riêng, hai cảnh 女巫 ch.5 và ch.47).
- Lỗi riêng để soát: `gemini/review-blacklist.md` (+ `../chung/review-blacklist.md`).
- Đo: `python tools/soat_van.py <file>` để đếm, `--list` để in từng chỗ khớp.

## Điểm khác biệt so với Lãnh Chúa Mang Chip

| | Lãnh Chúa Mang Chip | Lãnh Chúa Khoa Học |
|---|---|---|
| Trục truyện | Sinh tồn: nước, lương, mùa đông | Thị trường: chuẩn, giá, hợp đồng |
| Bàn tay vàng | Chip K-07: phân tích, đếm, ghi nhớ | Không có gì; đọc giá, thẩm định bằng câu hỏi, cấu trúc hợp đồng |
| Việc tay chân | MC tự làm được nhiều | Người khác làm hết; MC trả tiền, ký bảo lãnh, chịu trách nhiệm |
| Kiến thức kỹ thuật | Chip cung cấp | Người làm nghề nói; MC nghe và quyết có dám cam kết |
| Phản diện | Kẻ đầu độc giấu mặt | Một phường hội đúng một nửa |
| Đơn vị sảng | Vượt một bài toán sinh tồn | Dựng được một chuẩn và bán được hàng |

## Trạng thái

| Đoạn | Prompt | Bản thảo | Review | Chốt |
|---|---|---|---|---|
| 001 | briefs v1–v21 | 24 bản: A 2.871 · B 2.866 · C 2.188 · D 1.834 · E 2.028 · F 1.666 · G 1.996 · H 1.908 · I 1.629 · J 2.117 · K 1.781 · L 2.269 · M 2.174 · N 1.599 · O 1.965 · R 1.630 · S 1.653 · T 1.588 · U 1.608 · V 1.459 · **W 1.826** · X 1.473 · Y 1.528 字 (P cũ 2.363 bị ghi đè) | `reviews/doan-001.md` — đo bằng `tools/cham_doan.py`: **W 88** (nhịp 44, văn 34, canon 10) · Y 74 · X 70 · U 60 · T 56 · V 34; Tác giả đọc V/W/Y thấy **cả ba đều đạt** | chốt họ prompt v17 (ba câu nhịp mẫu + khối dữ kiện); SI v13 đóng băng |
