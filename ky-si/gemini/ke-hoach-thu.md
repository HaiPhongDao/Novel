# SI và kế hoạch thử — 23/10/2026

**Trạng thái:** Đã chạy SI v0.1 theo yêu cầu Tác giả, hai session độc lập. File thực dùng là `system-instruction.md`; chưa có giọng hoặc đoạn được Tác giả chọn.

Dựa trên `writer/SI-template`: mở bằng ROLE, quy ước cố định và OUTPUT. Đây là bản tối thiểu; chưa nạp bảy mục STYLE dài khi chưa thấy Writer trượt chỗ nào. Bổ sung nhịp đoạn đo được và quy ước thoại vào phần cố định để bản thử bám yêu cầu mẫu.

1. Xác nhận hướng thiết lập với phản hồi Tác giả; cập nhật glossary/world/brief đồng bộ nếu cần.
2. Chạy cùng brief 001 ở hai session thử riêng, cùng cấu hình; lưu bản gốc riêng vào archive, không chốt chương.
3. Review theo bốn điểm: giọng khẩu ngữ tự nhiên; thu hoạch nhỏ đã nhìn thấy; tám người và tiền/điểm đúng; dừng đúng chỗ để đoạn sau nối được.
4. So với mẫu bằng kỹ thuật kể; không lấy tên, cảnh hoặc cách diễn đạt của mẫu.
5. Chỗ Writer trượt mới thêm chuẩn hoặc anchor từ `mau-giong.md`, ghi phiên bản và chạy lại ở session mới.
6. Tác giả chọn giọng và hướng nội dung rồi mới đưa bản đạt vào chapters và cập nhật canon.

Gói test độc lập: `../briefs/session-test-001.md`. `tools/build_pack.py` hiện yêu cầu đã có ít nhất một file chapters/doan-*.md; không tạo chương giả để chạy công cụ khi truyện chưa có đoạn đầu.

Kết quả 23/10: bản 01 có 2.156 chữ Hán, sai tiền và số phà; sửa brief, giữ SI để chạy bản 02 có 2.472 chữ Hán. Bản 02 sửa được số tiền/quân/phà nhưng tự thêm thông số vận hành và giọng còn nặng miêu tả. Đây là hai lần thử sửa lỗi nội dung, chưa phải hai bản cùng prompt để so sánh giọng có kiểm soát. Xem reviews trước lần chạy tiếp.
