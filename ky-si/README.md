# Kỵ sĩ (tên làm việc)

**Trạng thái 23/10/2026:** Đã viết tới [đoạn 011](chapters/doan-011.md), 2,454 chữ Hán; [review SỬA NHẸ](reviews/doan-011.md). Agent đang viết tiếp theo yêu cầu; chưa ghi Tác giả duyệt từng bản mới.

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

## Vòng tiếp tục tự động

Lịch giờ đã tạm dừng sau khi Tác giả làm rõ: viết liên tục ngay tới giới hạn quota. Checkpoint: [progress.json](handoff/progress.json); lịch: [tu-dong-viet.json](handoff/tu-dong-viet.json). Công cụ ghép gói/lưu đoạn giảm thao tác lặp, Agent vẫn đọc review. Cấu hình và trạng thái Writer lấy từ checkpoint gần nhất; không chạy lại đoạn đã lưu.

## Writer

- **Đọc trước khi lập brief, chạy Writer hoặc review:** [Lưu ý của Tác giả](luu-y-tac-gia.md), đặc biệt yêu cầu thoại nói trọn ý, lưu loát và đáp nối nhau.
- [SI đang thử v0.2](gemini/system-instruction.md): 5.282 ký tự, Gemini 3.8 Flash, Thinking High, Grounding tắt. Bản lưu AI Studio mới nhất: `Kỵ sĩ - SI v0.2 tiếp đoạn 002`; [session bản 002 giữ để đọc](https://aistudio.google.com/prompts/15-RsuX5OmhUNgFZvlTqETUci_Qc8ezU-). SI v0.1 được giữ trong snapshot của hai bản đầu.
- [Thay đổi về thoại](gemini/thay-doi-v02.md): tách nhịp lời kể với lượt nói, thêm trích mẫu nối lời và mở cơ hội trao đổi trong cảnh tập.
- [Kế hoạch thử](gemini/ke-hoach-thu.md), [trích mẫu hiệu chỉnh](gemini/mau-giong.md), [gói thử mở đầu](briefs/session-test-001.md).
- Bốn bản thử 001 dùng session riêng, bản gốc nằm trong archive. Ngày 23/10, Tác giả chọn bản mới nhất để viết tiếp; [review ghi quyết định dùng 001](reviews/doan-001.md). Các review thử vẫn giữ làm lịch sử.
- Checklist: [lỗi riêng](gemini/review-blacklist.md) cùng `../chung/review-blacklist.md`.
- Đã có chính văn 001; gói bàn giao được ghép bằng `tools/build_pack.py`. Archive giữ nguyên văn, SI, prompt và metadata của mỗi lượt Writer.

## Trạng thái từng đoạn

| Đoạn | Prompt | Bản thảo | Review | Chốt |
|---|---|---|---|---|
| 001 / thử 01 | Đã chạy | [Nguyên văn](archive/doan-001-test-v01-01.md) | [VIẾT LẠI](reviews/doan-001-test-v01-01.md) | Chưa |
| 001 / thử 02 | Đã chạy, làm rõ dữ kiện | [Nguyên văn](archive/doan-001-test-v01-02.md) | [VIẾT LẠI trước khi chốt](reviews/doan-001-test-v01-02.md) | Chưa |
| 001 / v02-01 | Chỉ đổi SI, giữ prompt thử 02 | [Nguyên văn](archive/doan-001-test-v02-01.md) | [Thoại chưa đạt](reviews/doan-001-test-v02-01.md) | Chưa |
| 001 / v02-02 | Giữ SI v0.2, mở đối đáp trong brief | [Bản được chọn](chapters/doan-001.md) | [Quyết định dùng và ghi chú nối](reviews/doan-001.md) | Tác giả chọn dùng |
| 002 / lượt 01 | Đã chạy cùng session 001 | [Archive](archive/doan-002-writer-01.md) | [VIẾT LẠI](reviews/doan-002-writer-01.md) | Loại khỏi mạch chính |
| 002 / lượt 02 | Session mới, gói đầy đủ | [Archive](archive/doan-002-writer-02.md) | [VIẾT LẠI](reviews/doan-002-writer-02.md) | Loại khỏi mạch chính |
| 002 / lượt 03 | Session mới, gói gọn | [Archive](archive/doan-002-writer-03.md) | [VIẾT LẠI](reviews/doan-002-writer-03.md) | Loại khỏi mạch chính |
| 002 / lượt 04 | Session mới, phạm vi rõ | [Bản giữ để đọc](chapters/doan-002.md) | [SỬA NHẸ](reviews/doan-002.md) | Bản thảo, chưa ghi Tác giả duyệt |
| 003 | [Brief](briefs/doan-003.md) | [Chính văn](chapters/doan-003.md) | [SỬA NHẸ](reviews/doan-003.md) | Agent review |
| 004 | [Brief](briefs/doan-004.md) | [Chính văn](chapters/doan-004.md) | [SỬA NHẸ](reviews/doan-004.md) | Agent review |
| 005 | [Brief](briefs/doan-005.md) | [Chính văn](chapters/doan-005.md) | [SỬA NHẸ](reviews/doan-005.md) | Agent review |
| 006 | [Brief](briefs/doan-006.md) | [Chính văn](chapters/doan-006.md) | [SỬA NHẸ](reviews/doan-006.md) | Agent review |
| 007 | [Brief](briefs/doan-007.md) | [Chính văn](chapters/doan-007.md) | [SỬA NHẸ](reviews/doan-007.md) | Agent review |
| 008 | [Brief](briefs/doan-008.md) | [Chính văn](chapters/doan-008.md) | [SỬA NHẸ](reviews/doan-008.md) | Agent review |
| 009 | [Brief](briefs/doan-009.md) | [Chính văn](chapters/doan-009.md) | [SỬA NHẸ](reviews/doan-009.md) | Agent review |
| 010 | [Brief](briefs/doan-010.md) | [Chính văn](chapters/doan-010.md) | [SỬA NHẸ](reviews/doan-010.md) | Agent review |
| 011 | [Brief](briefs/doan-011.md) | [Chính văn](chapters/doan-011.md) | [SỬA NHẸ](reviews/doan-011.md) | Agent review |

Luật chung: [AGENT.md](../AGENT.md). Trạng thái làm việc ở [handoff/state.md](handoff/state.md), quyết định và trạng thái duyệt ở [log.md](log.md).
