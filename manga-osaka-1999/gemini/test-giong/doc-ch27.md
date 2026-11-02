# Hiệu chuẩn ch27 sau khi gỡ I-0025 — Agent đọc bốn việc

SI: `../si-dan-gemini.txt` (8.210 ký tự). Brief: `chung/hieu-chuan/manga/ch27/brief.md`, giữ nguyên để SI là biến duy nhất.
Bản đọc cặp cho Tác giả: `doc-cap-ch27-a.md`, `doc-cap-ch27-b.md`. Ghi chú này không chấm ĐẠT.

| | a (2.254 字) | b (2.205 字) |
|---|---|---|
| 1. Nhân vật nữ tự cãi mình, đổi ý | Không. "黑川碧从未怀疑过…" là tóm tắt. Mẫu ở cùng vị trí (54%) có "…秋山桑都快要讨厌自己了吧？" | Không. "她打心底里认可…" là tóm tắt. Bật lửa tự dưng xuất hiện trong tay cô |
| 2. Người kể giảng giải | Có 3 câu: Tomie 1988 rồi "读者渴望…", "过审概率向来偏低", "一旦公式化…排名就会立刻下跌" | Đẩy phần giảng vào miệng Kurokawa; còn một câu tục ngữ nghề trong lời kể ("在业界多半会换来惨淡的结局") |
| 3. Lượt thoại trả lời và mang thêm sự thật | Có. Đặt thẻ thoại chỉ 2/16 lượt | Có, nhưng 14/22 lượt gắn thẻ "X说/问" ở cuối; hỏi lại chuyện unit hai lần liên tiếp |
| 4. Đoạn có mở ra | Có, nhiều đoạn chở sự việc (44 字/đoạn) | Gần như toàn dòng một câu; đoạn dài nhất 80 |

Hai lần chạy y hệt nhau mà lệch ở việc 3 và 4, đúng biên độ nhiễu đã biết. Việc 1 hỏng ở **cả hai** lần, cũng là chỗ Tác giả đã chê
lần trước ("nhân vật nữ vẫn chưa thể hiện được tính cách như mẫu"). Gỡ I-0025 không chạm tới việc 1.

Máy soát `so_loi.py quet` đếm thẻ thoại bản b = 0 trong khi đếm tay ra 14 (Q-0146, E-GATE-01).
