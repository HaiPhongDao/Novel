# Review — đoạn 001, SI v0.1, bản thử 02

**Kết luận: VIẾT LẠI trước khi chốt.** Đã sửa được số tiền, số phà và quân số so với bản 01; còn tự đặt dữ kiện vận hành ngoài brief và giọng chưa sát mẫu. Đây là bản thử để Tác giả đọc, chưa là chính văn được duyệt.

## Điều kiện chạy và nguyên bản

- Session mới, không nhắc lại bản lỗi cho Writer: [AI Studio](https://aistudio.google.com/prompts/1aC6MxGrvVXl7Ybjn13_X7bCRvyHPVEfZ).
- Gemini 3.8 Flash, Thinking High, Google Search Grounding tắt. Giữ nguyên SI v0.1, 2.914 ký tự; prompt vòng 02 dài 3.602 ký tự.
- [Bản nguyên văn](../archive/doan-001-test-v01-02.md), [prompt](../archive/doan-001-test-v01-02-prompt.md), [SI](../archive/doan-001-test-v01-02-si.md).
- 3.200 ký tự gồm xuống dòng; 2.472 chữ Hán. Lưu trực tiếp văn bản đã đọc từ model turn, bỏ nhãn điều khiển UI; đối chiếu chuỗi bằng nhau sau khi ghi file. Không biên tập câu chữ.

## Kết quả

| Mục | Kết quả | Ghi chú |
|---|---|---|
| Tám người gác, hai cựu binh và sáu người mới | ĐẠT | Cộng Rowan là chín; cuối bài vẫn gọi sáu người mới |
| 24 bạc/30 ngày, tạm ứng 12, vốn 20, tiền mặt 32 | ĐẠT | Ký tối hôm qua; dùng 银币; không có thu/chi trong cảnh |
| Toma 12 → 13, tích lũy 1 → 0 | ĐẠT | Có hai lần hiện bảng; động tác được thử lại, còn mệt |
| Một chiếc phà | ĐẠT | Không còn ba chiếc như bản 01 |
| Mở trong buổi tập | ĐẠT | Bị vướng rồi Rowan sửa cách tập |
| Thông tin Mira chỉ là bốn xe hẹn, sáu xe tới | KHÔNG ĐẠT | Tự thêm hàng, số la kéo, tải xe và sức chở |
| Dừng đúng lời hỏi | CẦN SỬA | Còn hai đoạn tạo không khí và dồn ánh nhìn sau câu hỏi |
| Giọng tự nhiên theo mẫu | CẦN SỬA | Lời kể nặng miêu tả thân thể, vẻ lạnh và giải thích ý nghĩa; hài ít |

## Những chỗ cụ thể

1. “运的是北边的灰麦和腌肉”, “四头并排的重挽骡子”, “一次最多稳妥装两辆”: đều là thông tin mới chưa giao cho 001. Những dữ kiện này sẽ ràng buộc tải xe, đường dẫn và cách giải quyết đoạn 002; chưa đưa vào bible.
2. “遇上超重的还得空出地方放压舱石”: giải pháp thêm tải khi đã nói quá tải thiếu thuyết phục. Không dùng làm thiết lập vận hành cho đoạn sau.
3. “浸满桐油和黑机油的围裙”: 黑机油 kéo từ vựng máy móc vào địa bàn chưa thiết lập công nghiệp máy. Nên mô tả đồ nghề và vật liệu mà bến đang thực sự dùng.
4. Hai cựu binh bị tự gọi thành “斥候老兵”; mới giao cựu binh, chưa giao nghề trinh sát. Không mặc định họ có bộ kỹ năng ấy ở đoạn tiếp.
5. “字迹…在Toma身侧浮现” và Toma “猛地打了个激灵”: dễ làm hiệu ứng bảng giống hiện tượng bên ngoài. Bản sau nên đặt trọng tâm vào Rowan quan sát lượt tập, không dựng hiệu ứng phép thuật.
6. “在他们眼里…冷硬”: lời kể vào đánh giá của cả nhóm trong cảnh vốn bám Rowan. Có thể thể hiện qua cách người gác trả lời và làm theo lệnh.
7. Lời giải thích “面板不过是把这些汗水变成了可以直接兑现的砝码” và “捏成一块像样的铁板” làm văn nặng ẩn dụ so với mẫu. Buổi luyện, tiền công và câu nói của người gác nên gánh phần giọng này.
8. Độ dài 2.472 chữ Hán cao hơn mục tiêu khoảng 2.000; có thể bớt cụm lý lịch và các lượt tả mồ hôi, cơ bắp, vết sẹo lặp.

## Hướng xử lý khi tiếp tục

Nếu Tác giả muốn tiếp tục hướng hiện tại, vòng mới dùng session mới và tập trung hai việc: để thông tin Mira đúng phần chị đã biết, và cho giọng tính toán/hài xuất hiện bằng việc làm, thoại. Không dùng các thông số phà hoặc hàng mà Writer tự đặt ở hai bản thử làm canon.
