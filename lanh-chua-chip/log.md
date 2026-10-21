# Decision Log

Định dạng: `Ngày | Phạm vi | Quyết định | Lý do | Duyệt`

2026-10-21 | dự án | Khởi tạo truyện test: lãnh chúa + xuyên không + chip hỗ trợ | Yêu cầu của Tác giả | Tác giả
2026-10-21 | bible | Chip là công nghệ thật (nguyên mẫu K-07), KHÔNG phải "hệ thống" game: không điểm, không cửa hàng, không nhiệm vụ | Tạo khác biệt với dòng hệ thống; thắng lợi đến từ tri thức + hành động của MC | ⏳ Chờ Tác giả
2026-10-21 | bible | MC: Trần Minh Khang, 29, kỹ sư nông nghiệp – IoT; xuyên vào Leon Varen, 18 tuổi | Kỹ năng thực tế hợp thể loại xây lãnh địa | ⏳ Chờ Tác giả
2026-10-21 | bible | Bối cảnh: lục địa trung cổ phương Tây, phép thuật hiếm (giới quý tộc), quái vật ở rừng | Chuẩn thể loại lãnh chúa | ⏳ Chờ Tác giả
2026-10-21 | plot | Leon gốc bị đầu độc kéo dài trên đường đi; kẻ đầu độc là Pell (lộ cuối arc 1) | Tuyến bí ẩn xuyên arc 1 | ⏳ Chờ Tác giả
2026-10-21 | plot | "Hắc Thạch" = mỏ than lộ thiên, dân coi là đá nguyền | Lời giải cho bài toán chất đốt mùa đông | ⏳ Chờ Tác giả
2026-10-21 | dự án | Phạm vi test mở rộng lên 5 chương đầu | Yêu cầu của Tác giả | Tác giả
2026-10-21 | plot | Ch4: em trai Hob chết trong vụ cháy "đá nguyền"; sự cố ngộ độc khí than nhà Dunn (không ai chết) | Cho Hob động cơ cá nhân và lý do đổi ý thuyết phục | ⏳ Chờ Tác giả
2026-10-21 | plot | Ch5: bầy sói mắt đỏ "đang chạy trốn" thứ gì đó trong rừng (vết cào lạ) | Móc kết đợt test + bí ẩn dài hạn | ⏳ Chờ Tác giả
2026-10-21 | dự án | Gemini dùng system instruction riêng của Tác giả; system-prompt v1 của Agent chuyển vào archive/ | Tránh hai bộ quy tắc văn phong xung đột | Tác giả
2026-10-21 | dự án | Chạy test A/B/C (1 dòng / đơn giản / chi tiết) cho chương mở đầu | Đánh giá ảnh hưởng của prompt lên chất lượng | Tác giả
2026-10-21 | dự án | Chính văn viết bằng tiếng Trung | Viết tiếng Việt AI bị kẹt giọng báo chí | Tác giả
2026-10-21 | dự án | Giao việc theo "đoạn" (~2000 字), không chia chương | Yêu cầu của Tác giả | Tác giả
2026-10-21 | dự án | Prompt không liệt kê điều cấm (vd. "không phải hệ thống game") — mô tả khẳng định | Câu phủ định mồi ngược model (bản B dùng 系统/宿主) | Tác giả
2026-10-21 | dự án | Test vòng 1: B tự nhiên, C máy móc → prompt cân bằng (chốt sự thật + điểm đến, thả cách đi) | Xem reviews/test-B-C.md | Tác giả
2026-10-21 | bible | Tên tiếng Trung: 陈明康 / 莱昂·瓦伦 / 小七 / 加雷斯 / 佩尔 / 黑石领 … (glossary.md) | Chốt để prompt và review nhất quán | ⏳ Chờ Tác giả
2026-10-21 | bible | Lấy từ bản B: tên 小七; nghi ngờ của MC hướng về phủ bá tước | Tự nhiên hơn; bảo vệ bí mật Pell | ⏳ Chờ Tác giả
2026-10-21 | dự án | Prompt và ghi chú sửa cho Gemini viết bằng tiếng Việt; tên tiếng Trung chốt sau đoạn 001 | Tiếng Trung của Agent không đạt | Tác giả
2026-10-21 | dự án | Tên riêng trong chính văn giữ chữ Latin, không phiên âm chữ Hán (thêm vào SI của Gemini) | Tránh mỗi lần dịch một kiểu (里昂/莱昂) | Tác giả
2026-10-21 | doan-001 | Nháp 1 đạt mức SỬA NHẸ; Leon nghi Pell ngay đoạn 1 → giữ (phương án A: Leon biết Pell là tay sai, giả vờ, lần ra chủ mưu) | Logic: MC thông minh + bát trà + phát hiện độc → nghi là tất yếu | Tác giả
2026-10-21 | bible | Nhận chi tiết từ đoạn 001: kho trang viên <200 pound lúa mạch mốc; dân là nông nô; Gareth mặc giáp lưới; giọng Leon lạnh, tính sổ, miệng độc trong đầu | Chi tiết phụ, khớp canon | Agent (ghi log)
2026-10-21 | plot | Dàn ý 5 chương cũ → 6 đoạn (ch2 cũ tách thành đoạn 2 + 3) | Ch2 cũ quá nhiều sự kiện cho ~2000 字 | Agent (ghi log)
2026-10-21 | dự án | Writer Gemini chuyển session mỗi 2–3 đoạn; Agent giữ gói bàn giao (handoff/) cập nhật sau mỗi review | Không thể viết 100+ đoạn trong một session | Tác giả
2026-10-21 | doan-002 | Đạt; Leon gần như đoán ra đá đen từ đoạn 2 → đoạn 4 thành xác nhận | Hợp lý với kỹ sư | Agent (ghi log)
2026-10-21 | plot | Người chết cháy là "lão Jim" (đoạn 2) ≠ dàn ý cũ "em trai Hob" → đề xuất lão Jim là em trai/em rể của Hob | Giữ được động cơ cá nhân của Hob ở đoạn 5 | ⏳ Chờ Tác giả
