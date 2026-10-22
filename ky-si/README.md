# Kỵ sĩ (tên làm việc)

**Trạng thái 23/10/2026:** Có bốn bản thử đoạn 001. Theo phản hồi thoại cụt, đã sửa SI v0.2 và mở trao đổi trong brief. Bản mới nhất [v02-02](archive/doan-001-test-v02-02.md) có lời giải thích và lượt đáp nối ý tốt hơn; còn lỗi dữ kiện vận hành nên chưa chốt đoạn.

**Hướng đề xuất:** Kỵ sĩ vừa giải ngũ nhận giữ bến phà, dùng bảng luyện tập tổ chức tám người gác thành đội quân đầu tiên. Phát triển từ giữ bến → giữ đường → giữ đất.

## Đọc để trao đổi

1. [Phân tích mẫu](tham-khao/phan-tich.md): động lực phát triển, giọng, nhịp, điểm lấy và những lựa chọn còn mở.
2. [Tổng quan truyện mới](bible/overview.md): logline, premise và phạm vi arc đầu.
3. [Luật thế giới và bảng](bible/world.md): quân số, quyền hạn, cơ chế và dự toán tháng đầu.
4. [Dàn ý 12 đoạn](plot/outline.md) và [brief 001](briefs/doan-001.md).

## Nguồn tham khảo

- [流浪骑士开局：我有简易数据面板.txt](流浪骑士开局：我有简易数据面板.txt), Tác giả tải lên ở commit `b95e3e7`; giữ nguyên tại vị trí tải lên.
- [Chỉ mục chương/dòng](tham-khao/chi-muc.md) giúp đối chiếu phân tích.
- Mới đọc phần đầu và các trích đoạn chọn lọc; phạm vi ghi trong bản phân tích, không coi đã đọc toàn bộ truyện.

## Writer

- **Đọc trước khi lập brief, chạy Writer hoặc review:** [Lưu ý của Tác giả](luu-y-tac-gia.md), đặc biệt yêu cầu thoại nói trọn ý, lưu loát và đáp nối nhau.
- [SI đang thử v0.2](gemini/system-instruction.md): 5.282 ký tự, Gemini 3.8 Flash, Thinking High, Grounding tắt. Bản lưu AI Studio mới nhất: `Kỵ sĩ - SI v0.2 thoại test02`. SI v0.1 được giữ trong snapshot của hai bản đầu.
- [Thay đổi về thoại](gemini/thay-doi-v02.md): tách nhịp lời kể với lượt nói, thêm trích mẫu nối lời và mở cơ hội trao đổi trong cảnh tập.
- [Kế hoạch thử](gemini/ke-hoach-thu.md), [trích mẫu hiệu chỉnh](gemini/mau-giong.md), [gói thử mở đầu](briefs/session-test-001.md).
- Mỗi bản thử dùng session riêng, bản gốc nằm trong archive. Phản hồi Tác giả cho phép sửa thoại và chạy lại; chưa suy thành duyệt các chi tiết vận hành Writer tự thêm.
- Checklist: [lỗi riêng](gemini/review-blacklist.md) cùng `../chung/review-blacklist.md`.
- Công cụ `build_pack.py` cần đã có chính văn; gói thử đầu được ghép riêng, không tạo đoạn giả.

## Trạng thái từng đoạn

| Đoạn | Prompt | Bản thảo | Review | Chốt |
|---|---|---|---|---|
| 001 / thử 01 | Đã chạy | [Nguyên văn](archive/doan-001-test-v01-01.md) | [VIẾT LẠI](reviews/doan-001-test-v01-01.md) | Chưa |
| 001 / thử 02 | Đã chạy, làm rõ dữ kiện | [Nguyên văn](archive/doan-001-test-v01-02.md) | [VIẾT LẠI trước khi chốt](reviews/doan-001-test-v01-02.md) | Chưa |
| 001 / v02-01 | Chỉ đổi SI, giữ prompt thử 02 | [Nguyên văn](archive/doan-001-test-v02-01.md) | [Thoại chưa đạt](reviews/doan-001-test-v02-01.md) | Chưa |
| 001 / v02-02 | Giữ SI v0.2, mở đối đáp trong brief | [Nguyên văn mới nhất](archive/doan-001-test-v02-02.md) | [Thoại cải thiện; còn lỗi nội dung](reviews/doan-001-test-v02-02.md) | Chưa |

Luật chung: [AGENT.md](../AGENT.md). Trạng thái làm việc ở [handoff/state.md](handoff/state.md), quyết định và trạng thái duyệt ở [log.md](log.md).
