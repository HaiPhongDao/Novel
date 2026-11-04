# Train Outliner — viết brief cho Writer, thử trên chương bộ mẫu

Bắt đầu 04/11/2026. Hôm 03/11 nghiên cứu SI không giải được câu "bảo Writer viết gì". Giờ **đóng băng SI**, chỉ đổi **brief**.

## Câu hỏi

Cho một chương bộ mẫu (đã biết nó chứa gì), Outliner viết brief; Writer (Gemini, SI đóng băng) viết lại. **Writer có viết đủ nội dung không**, và brief mỏng đến mức nào thì còn đủ?

## Quy trình mỗi chương

1. `python tools/outl_chuong.py N` → `chNN/goc.txt`.
2. Đọc gốc, lập `chNN/dap-an.json`: các đơn vị nội dung, nhóm `BB` (bắt buộc: truyện sau cần), `PH` (phụ nhưng có ích), `TX` (chất liệu tự do), kèm từ khoá để phân loại nhanh và `dung` = đơn vị đánh dấu điểm dừng.
3. Viết brief theo **thang độ chi tiết** (cùng một chương, cùng dữ kiện nền, chỉ đổi độ chi tiết):
   - `C` chuỗi sự việc đầy đủ (cận trên — gần như chép lại gốc),
   - `M` các mốc phải có, không thứ tự, không thoại,
   - `K` chỉ tình huống + kết quả phải đạt + điểm dừng.
4. Chạy Writer 1 lần mỗi brief (Tác giả 04/11: không cần 2 lần) (`jobs-vX.json`, SI = `si-dong-bang.txt` = `lop/si-L-13R0B.txt`, sha1 `ecf51335b8cd`).
5. `python tools/outl_cham.py chNN/dap-an.json chNN/vX-*.md` phân loại nhanh; **đọc tay** các ô `?` và ô nghi, ghi `chNN/cham-vX.md`: mỗi đơn vị ✔ đủ / ~ mờ-lệch / ✘ thiếu, thêm số bịa mâu thuẫn, độ dài so với gốc, đoạn nào đọc như checklist.
6. Ghi `NHAT-KY.md` (≤ 6 dòng/lần) và, khi một mẫu lặp qua ≥ 2 chương, vào `QUY-TAC.md` với nhãn `ĐÃ ĐO` hay `GIẢ THUYẾT`.

## Ranh giới

- Một lần sửa = một biến. Không đổi SI, không đổi dữ kiện nền giữa các mức.
- Mỗi brief chạy 1 lần (Tác giả 04/11). Một lần không chứng minh được gì: mẫu nào chỉ thấy một chương thì ghi GIẢ THUYẾT, chờ chương sau.
- Script chỉ phân loại; **kết luận do đọc**.
- Chương đã làm anchor của SI hoặc đã dùng hiệu chuẩn SI (1, 24?, 27, 29, 52, 104, 107) tránh dùng — Writer có thể chép anchor.
