# Kỵ sĩ (tên làm việc)

**Trạng thái 23/10/2026:** Đã chạy Writer theo yêu cầu Tác giả, có hai bản thử đoạn 001 và review riêng. Bản 02 sửa được tiền, quân số và số phà; còn lỗi tự đặt dữ kiện vận hành và giọng cần chỉnh. Các thiết lập vẫn là bản làm việc; chưa chốt đoạn.

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

- [SI tối thiểu v0.1](gemini/system-instruction.md): 2.914 ký tự, đã chạy trên AI Studio với Gemini 3.8 Flash, Thinking High, Grounding tắt. Bản SI của session 01 đặt tên `Kỵ sĩ - SI v0.1`.
- [Kế hoạch thử](gemini/ke-hoach-thu.md), [trích mẫu hiệu chỉnh](gemini/mau-giong.md), [gói thử mở đầu](briefs/session-test-001.md).
- Hai bản thử dùng session riêng, bản gốc nằm trong archive. Tác giả yêu cầu chạy Writer là cho phép thử thiết lập này; chưa suy thành duyệt mọi chi tiết Writer thêm.
- Checklist: [lỗi riêng](gemini/review-blacklist.md) cùng `../chung/review-blacklist.md`.
- Công cụ `build_pack.py` cần đã có chính văn; gói thử đầu được ghép riêng, không tạo đoạn giả.

## Trạng thái từng đoạn

| Đoạn | Prompt | Bản thảo | Review | Chốt |
|---|---|---|---|---|
| 001 / thử 01 | Đã chạy | [Nguyên văn](archive/doan-001-test-v01-01.md) | [VIẾT LẠI](reviews/doan-001-test-v01-01.md) | Chưa |
| 001 / thử 02 | Đã chạy, làm rõ dữ kiện | [Nguyên văn](archive/doan-001-test-v01-02.md) | [VIẾT LẠI trước khi chốt](reviews/doan-001-test-v01-02.md) | Chưa |

Luật chung: [AGENT.md](../AGENT.md). Trạng thái làm việc ở [handoff/state.md](handoff/state.md), quyết định và trạng thái duyệt ở [log.md](log.md).
