# Nhật ký train Outliner

Mỗi mục ≤ 6 dòng: việc làm · kết quả (ĐÃ CHẠY / CHƯA KIỂM) · việc kế.

## 04/11/2026

- Dựng khung `chung/outliner-train/` + `tools/outl_chuong.py` (tách chương) + `tools/outl_cham.py` (phân loại độ phủ theo từ khoá). SI đóng băng = `si-dong-bang.txt` (bản sao `lop/si-L-13R0B.txt`, 5.210 ký tự). CHƯA KIỂM: script cham trên bản thật.
- Chọn chương train đầu tiên: ch09 (bữa tối biên tập mời, 1.738 chữ Hán, hai người, kết bằng tuyên bố cược lớn). Lập `dap-an.json` 11 đơn vị. Viết ba mức brief C/M/K (cùng dữ kiện nền). Tác giả bảo bỏ chạy 2 lần: gửi 3 lượt (mỗi mức 1).
- ĐÃ CHẠY ch09 v1 (C/M/K, mỗi mức 1 lần, Agent đọc cả ba; chi tiết `ch09/cham-v1.md`): C phủ 7/7 bắt buộc; M 7/7 nhưng đọc như checklist (sáu gạch → sáu đoạn đúng thứ tự), tên kanji sai, rò `上杉明菜` từ anchor SI; K giữ kết cục nhưng mất 2 bắt buộc (gọi món/uống bia, bị hỏi học kinh dị), tự bịa ~10 số cứng + cả cơ chế phạt/ban giám khảo, biến cảnh ăn đùa thành buổi trình bày thủ tục. Giọng đùa của gốc chỉ còn ở C.
- Giả thuyết (CHƯA KIỂM, 1 chương): (1) chất liệu "tính cách/giọng" phải đi bằng sự việc nhỏ cụ thể, mốc không chở được; (2) cơ chế/số liệu để Writer tự đặt thì nó bịa → brief phải ghi "chỉ gọi tên, chi tiết thuộc đoạn sau"; (3) Hồ sơ nhân vật theo dạng "dịp + hành vi" dùng lại được giữa các đoạn, không phải chép từ gốc. Thử dạng P (đường chính + nhịp cảnh + hồ sơ chọn dùng) trên ch09.
- ĐÃ CHẠY ch09 v2-P và ch22 v1 (P, K) + v2-Q (chi tiết `ch09/cham-v1.md`, `ch22/cham-v1.md`). K lặp lại ở ch22: kết quả đúng, mất cú đảo vai, bịa ~15 số cứng + cả quy trình hội nghị. P giữ được đảo chiều; hỏng mới: lộ bí mật sớm (12 dòng tự sự) và khai triển dữ kiện cho (tiền → liệt kê khoản). Q sửa đúng hai hỏng đó (1 lần chạy, gộp 4 thay đổi).
- Việc kế (phiên mới): thử mẫu Q (`MAU-BRIEF-Q.md`) trên chương khác loại — nhiều người / xung đột (gợi ý ch54 hoặc ch33); chỉ tách ablation khi Q hỏng ở chương mới. Đọc `QUY-TAC.md` và `BAN-GIAO.md` trước.
- Context phiên này chạm 268k lúc chốt; hạn mức tuần 46%. Chưa commit gì (tools/outl_*.py + chung/outliner-train/ đang untracked).

## 04/11/2026 (phiên 2)

- ĐÃ CHẠY ch54 v1-Q (hai cảnh: giáo sư giảng cho Oda + quán nướng; 1 lần; chi tiết `ch54/cham-v1.md`): BB 10 ✔ / 5 ~ / 2 ✘ trên 17; giữ cú đổi mặt hài, "Chỉ lộ ở câu cuối" không lộ sớm và không bịa điều bị giấu, dừng đúng. Hỏng: A2 chỉ nhãn "因为安全", A5/A10 mất (Oda không đáp), câu cuối thành câu hỏi mềm, dựng một câu cơ chế Bộ trả lại, "共事半年" trái canon.
- Giả thuyết mới (CHƯA KIỂM, 1 chương): Q11 chỗ chỉ ghi nhãn → Writer trả nhãn/đổi lý do; Q12 nội dung để thành dòng hồ sơ → chép gần nguyên văn, nén thành loạt (bài giảng thành danh sách). Q9: tên Latin là theo SI Quy tắc 2; kèm kanji làm Writer cân nhắc ≥ 10 vòng, kết quả không đổi.
- Việc kế: ch30 (hội nghị nhiều người) hoặc ch45 (độc thoại nội tâm); viết lại brief theo Q11/Q12 (nội dung bằng câu, kèm lời đáp của người nghe, tên chỉ Latin) rồi xem có sửa được các ô ~/✘ không.
- Chưa commit gì (thư mục + `tools/outl_*.py` vẫn untracked). Context phiên ~150k; hạn mức tuần 47%.
