# BAN-GIAO riêng — truyện từ tiền đề Tác giả (04/11/2026)

## 0. Trạng thái
- Truyện: `rieng/dong-kinh-1999/` (tiền đề `tien-de.md`: "MC xuyên qua đến Tokyo năm 1999 vẽ manga"). Chưa tạo bible.
- Tiền đề chỉ một dòng. Tên người, 5 sự thật cố định (`so.md`), 3 cảnh (`ke-hoach.md`) là Outliner chọn, **Tác giả chưa duyệt**.
- **Hợp đồng thể loại (Tác giả chỉ dẫn 04/11): 爽文 truyện mạng, không văn thanh.** Cảnh nào cũng dựng từ vấn đề có hạn → MC chủ động chọn dám → chỗ sướng → dừng ở việc đang dở (QUY-TAC Q15).
- Cảnh 1 (một người): v1 **KHÔNG ĐẠT** (Tác giả chê văn thanh; lỗi ở kế hoạch/brief của Outliner). v2 làm lại theo hợp đồng 爽: giọng đúng hướng, còn dư ~1/4 chữ tả phòng, khối phân tích như báo cáo, địa danh/số liệu bịa. **Tác giả chưa chấm v2.** Tệp: `canh-1/` (thuoc-v2, brief-v2, kiem-truoc-v2, v2, cham-v2; v1 giữ làm bằng chứng).
- Cảnh 2, 3: CHƯA LÀM. `ke-hoach.md` cảnh 2, 3 còn viết theo kiểu cũ (điều giấu/lộ), phải dựng lại theo Q15 trước khi viết brief.
- Brief dùng 东京 (từ tiền đề); không dùng "Tokyo", "manga/漫画", "连载" vì grep. Tất cả là GIẢ THUYẾT. SI `si-dong-bang.txt` đóng băng.

## Làm tiếp (phiên mới, một cảnh)
1. Hỏi Tác giả (một câu) v2 đạt chưa; nếu chưa, nghe nhận xét rồi sửa `ke-hoach.md`/brief, không tự đoán lần nữa.
2. Nếu đạt: dựng lại cảnh 2 theo Q15 (Ren chủ động, Noguchi là người coi thường rồi đổi mặt hay người đặt cược; chỗ sướng cụ thể), sửa `ke-hoach.md` cảnh 2 trước. Thứ tự: `thuoc` → `brief` → `kiem-truoc` → chạy 1 lần → `cham`.
3. Brief không đặt tên vật cần tả (Q14) và không đưa nội dung dạng danh sách (Q12): cho một phán quyết sắc và một chi tiết. Không tính từ cảm giác (mau-prompt 13). Có số liệu giữ độ khó (mau-prompt 2, 18).
4. Cảnh hai người cần lời đáp của người nghe (Q12). Tên Latin; không kanji.
5. grep brief: `Akiyama|Kurokawa|Okada|Tokyo|漫画|连载|未麻|上杉`, rỗng.
6. Cuối phiên: cập nhật NHAT-KY, QUY-TAC, file này; commit + push, không `think-*.md`, `run-*.log`.

## Chạy Writer
`python tools/aistudio_run.py --batch chung/outliner-train/rieng/dong-kinh-1999/canh-N/jobs-vN.json --timeout 22 > .../run-vN.log 2>&1 &` (từ gốc repo). Mỗi lần 3–4 phút.
