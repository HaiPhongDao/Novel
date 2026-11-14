# Xuyên thành Trạng nguyên

Tên tạm. Truyện cổ đại giá không, chính văn tiếng Trung.

- SI đang dùng là [bản Đại Càn](gemini/si-dan-gemini.txt) từ đợt hiệu chuẩn ngày 13/11.
- Brief mở truyện đặt mốc hơn 2.500 chữ Hán. [Brief hiện tại](briefs/doan-001.md) ghi mốc này. [Brief lượt đầu](archive/doan-001-v1.brief.md) là prompt đã sinh ra bản dùng để biên tập.

## Trạng thái

| Đoạn | Chính văn | Bản nghe | Chốt |
| --- | --- | --- | --- |
| 001 | [Bản đã soát](chapters/doan-001.md) | [DocTTS](doc/lo-001.md) | Chờ tác giả nghe |
| 002 | [Bản đã soát](chapters/doan-002.md) | [DocTTS](doc/lo-002.md) | Chờ tác giả nghe |
| 003 | [Bản đã soát](chapters/doan-003.md) | [DocTTS](doc/lo-003-007.md) | Chờ tác giả nghe |
| 004 | [Bản đã soát](chapters/doan-004.md) | [DocTTS](doc/lo-003-007.md) | Chờ tác giả nghe |
| 005 | [Bản đã soát](chapters/doan-005.md) | [DocTTS](doc/lo-003-007.md) | Chờ tác giả nghe |
| 006 | [Bản đã soát](chapters/doan-006.md) | [DocTTS](doc/lo-003-007.md) | Chờ tác giả nghe |
| 007 | [Bản đã soát](chapters/doan-007.md) | [DocTTS](doc/lo-003-007.md) | Chờ tác giả nghe |

## Việc kế

Khi chốt xong một đoạn, commit và push ngay đoạn đó lên GitHub.
 Xem [ghi chú về thoại Hoài An](no-giong.md) khi soát thoại.

Tối 19 tháng 4, tiểu nhị Thẩm Ký vừa chuyển một chiếc chặn giấy bằng đồng cùng lời nhắn hẹn ở quán trà ngoài kho Thông Châu vào chiều hôm sau. Gemini viết tiếp từ hai đoạn gần nhất, [thẻ thiết lập](handoff/canon-card.md) và [state hiện hành](handoff/state.md).

Sau mỗi đoạn đã biên tập, giao subagent giữ state đối chiếu chính văn và cập nhật mốc `state-through` ở đầu file. Ghi điểm nối, việc hoặc số liệu còn hiệu lực, ai biết gì và các tình tiết độc giả đã đọc mà Writer dễ kể lại. Ở lượt đọc soát, đối chiếu đoạn mới với nguyên văn đoạn trước. Giữ các nhắc lại có tác dụng trong cảnh mới và chỉ sửa chỗ kể lại.
