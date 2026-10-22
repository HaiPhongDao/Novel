# Kỵ sĩ (tên làm việc)

**Trạng thái 23/10/2026:** Đã tiếp nhận mẫu và lập bộ khởi động v0.1. Các tên, luật bảng, bối cảnh và dàn ý mới là **đề xuất**, chưa phải canon được Tác giả duyệt. Chưa có chính văn hoặc đoạn chốt.

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

- [SI tối thiểu v0.1](gemini/system-instruction.md): 2.914 ký tự, dựa `../writer/SI-template`; chưa chạy hoặc lưu lên AI Studio.
- [Kế hoạch thử](gemini/ke-hoach-thu.md), [trích mẫu hiệu chỉnh](gemini/mau-giong.md), [gói thử mở đầu](briefs/session-test-001.md).
- Các file này chuẩn bị cho bản thử; cập nhật sau phản hồi hướng truyện của Tác giả trước khi chạy. Mỗi lần thử dùng session riêng, lưu bản gốc vào archive.
- Checklist: [lỗi riêng](gemini/review-blacklist.md) cùng `../chung/review-blacklist.md`.
- Công cụ `build_pack.py` cần đã có chính văn; gói thử đầu được ghép riêng, không tạo đoạn giả.

## Trạng thái từng đoạn

| Đoạn | Prompt | Bản thảo | Review | Chốt |
|---|---|---|---|---|
| 001 | Bản thử v0.1, chưa gửi Writer | Chưa có | Chưa có | Chưa |

Luật chung: [AGENT.md](../AGENT.md). Trạng thái làm việc ở [handoff/state.md](handoff/state.md), quyết định và trạng thái duyệt ở [log.md](log.md).
