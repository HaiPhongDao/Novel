# Lưu ý của Tác giả

## Báo cáo gọn để tiết kiệm quota — 23/10/2026

Tác giả: “Để tiết kiệm quota bạn có thể không cần gửi text truyện hoặc thứ tương tự lên chat”.

- Chính văn, bản thử, SI, prompt và review đầy đủ lưu trong repo; chat chỉ báo ngắn kết quả, đường dẫn file, trạng thái Git và vấn đề cần Tác giả quyết định.
- Không dán lại truyện, prompt dài, review đầy đủ hoặc ảnh chụp Writer vào chat theo mặc định. Khi Tác giả yêu cầu trích/xem thì cung cấp đúng phần cần.
- Trong quá trình làm, tránh xuất lặp bản thảo hoặc nội dung dài qua công cụ. Khi chỉ kiểm lưu file/cấu hình thì báo độ dài, hash hoặc kết quả kiểm; vẫn đọc chính văn cần thiết để review thực chất.
- Việc truyền prompt và phần tiền tình cần thiết cho Writer vẫn thực hiện theo quy trình; yêu cầu này điều chỉnh lượng nội dung báo trên chat.

## Thoại phải lưu loát, nói trọn ý — 23/10/2026

Phản hồi nguyên văn: “Phần thoại của nhân vật đang bị cụt, không đủ lưu loát”. Tác giả yêu cầu lưu lại vào Git để áp dụng cho các lần viết và review truyện Kỵ sĩ tiếp theo.

- Mỗi lượt nói đi hết ý người nói cần truyền đạt. Lời giải thích, báo cáo hoặc đề nghị có thể nối nhiều câu tự nhiên.
- Câu đáp tiếp nhận điều vừa nghe, thể hiện ý muốn hoặc phản ứng của người trả lời và giúp cuộc trao đổi đi tiếp.
- Nhân vật cấp dưới có thể nêu khó khăn, hỏi lại, giải thích và góp ý phù hợp với quan hệ trong cảnh; không chỉ xác nhận đã nghe lệnh.
- Khẩu lệnh có thể ngắn. Lời trò chuyện, hướng dẫn và bàn bạc có nhịp riêng; không kéo dài mọi câu cho đủ chữ.
- Nhịp đoạn ngắn của lời kể không phải hạn mức cho lời thoại. Đặt hành động xen vào ở chỗ đổi ý tự nhiên, tránh chặt một ý đang nói dở.
- Brief phải tạo cơ hội để người nghe thực sự đáp lại, thay vì chỉ cho một người ra lệnh và những người còn lại làm theo.

Khi review, đọc liền các lượt nói để kiểm tra mạch hỏi–đáp. Không đánh giá độ lưu loát chỉ bằng số chữ hoặc số câu tăng lên.

Đã triển khai trong [SI v0.2](gemini/system-instruction.md), [ghi chú thay đổi](gemini/thay-doi-v02.md) và [checklist review](gemini/review-blacklist.md). Việc lưu yêu cầu này không đồng nghĩa đã duyệt toàn bộ bản thử hoặc các chi tiết Writer tự thêm.
