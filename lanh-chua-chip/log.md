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
2026-10-21 | dự án | Thử chuyển session Writer ngay từ đoạn 003 (S2) | Gói bàn giao có lỗ hổng thì phát hiện sớm, sửa rẻ | Tác giả
2026-10-21 | dự án | Test chuyển session (S1→S2) qua: đoạn 003 giữ giọng, mạch, dùng đúng chi tiết trong state | Giữ quy trình handoff | Agent (ghi log)
2026-10-21 | doan-003 | Đạt; Gemini đã giải thích nguồn bẩn (cả sườn dốc) → đoạn sau bỏ "đi tìm nguồn bẩn" | Logic tốt | Agent (ghi log)
2026-10-21 | plot | Đoạn 004 = Leon lập quy củ bằng uy lãnh chúa (Tác giả yêu cầu "cứng rắn, uy nghiêm"); dàn ý dời một đoạn, test thành 7 đoạn | Yêu cầu của Tác giả | Tác giả
2026-10-21 | bible | Luật Aldermark: đất/giếng/rừng thuộc lãnh chúa, trái lệnh chịu lao dịch hoặc roi; nồi đồng lớn ở bếp trang viên; túi muối; hũ mật ong nhà Mira | Chi tiết nền phục vụ đoạn 004 | Agent (ghi log)
2026-10-21 | dự án | Bỏ chế độ ít thao tác (B), giữ quy trình hiện tại; hoàn tác cả các sửa cấp chữ đã làm theo B | Tác giả không cần | Tác giả
2026-10-21 | doan-004 | Đạt; nhận chi tiết: nồi đồng thau 30 người, đun sáng–tối, xà sồi ~12 m³, Hob chống gậy, gã to con chịu lao dịch | Chi tiết phụ | Agent (ghi log)
2026-10-21 | doan-005 | Trôi giọng (cảnh Hob tự giải thích, kết bằng câu chốt) → viết lại nửa cuối; nguyên nhân: prompt tả ý nghĩa thay vì sự việc, quá nhiều việc, đoạn thứ 3 trong session | Tác giả nhận xét | Tác giả
2026-10-21 | dự án | Prompt: tả sự việc không tả ý nghĩa, ≤2 cảnh + 1 nhảy thời gian, kết bằng hình ảnh, nhắc tự kiểm SI; session Writer chỉ 2 đoạn; gói bàn giao thêm "mẫu giọng" | Chặn trôi giọng | Agent (ghi log)
2026-10-21 | plot | Đề xuất: Hob nhận sai bằng việc khai thật 5800 pound (payoff đoạn 2); ý "đổi than lấy lương" từ đoạn 005 làm hướng giải bài toán lương thực | Gemini tự đề xuất, khớp tuyến T04 | ⏳ Chờ Tác giả
2026-10-22 | dự án | Đoạn hỏng thì làm lại ở session mới (gói bàn giao tới đoạn trước + prompt mới), không gửi prompt viết lại | Yêu cầu của Tác giả | Tác giả
2026-10-22 | doan-005 | Nháp 1 vào archive; prompt bản 2: 2 cảnh + 1 nhảy, thử than dời sang đoạn 6, Hob đổi thái độ bằng việc khai thật 5800 pound | Áp quy tắc prompt mới | Agent (ghi log)
2026-10-22 | doan-005 | Bản 2 (S3) đạt. Số củi Hob nói (30+ ngày) sai → state ghi ~65–75 ngày | Nhất quán | Agent (ghi log)
2026-10-22 | bible | Trang viên xây bằng đá bazan đen; độ tin cậy của 小七 thường 60–90% | Tránh lẫn với than; chặn số 98–99,9% | Agent (ghi log)
2026-10-22 | bible | 小七 hiện vạch xanh trong tầm nhìn (đoạn 005) — giữ hay bỏ? | Chạm luật bàn tay vàng | ⏳ Chờ Tác giả
2026-10-22 | dự án | SI của Writer (bản sửa `gemini/system-instruction.md`) dịch sang tiếng Anh → `system-instruction-en.md` (anchor, tên riêng, ví dụ tiếng Trung giữ nguyên); Writer đổi sang Gemini 3.8 Flash | Tiết kiệm token | Tác giả
2026-10-22 | dự án | Nháp SI v2 viết khẳng định (`system-instruction-en-v2.md`): bỏ mọi câu cấm và ví dụ sai khỏi SI; ví dụ sai chuyển sang `review-blacklist.md` cho Agent | SI cũ dùng phủ định nhiều, ví dụ sai mồi ngược (眸子, 一丝, 系统 lặp lại trong bản ra) | ⏳ Tác giả xem
2026-10-22 | dự án | Bỏ bước "tự kiểm sau khi viết" khỏi prompt và SI v2 (mục 4 đổi thành chuẩn khi đang viết) | Model trong chat viết một lượt, không đọc lại để sửa | Tác giả
2026-10-22 | dự án | Test SI v2 đoạn 1: Tác giả bắt 3 dấu vết AI (so sánh giải thích sau giọng nói, —— chêm giải thích, mùi "直往鼻孔里钻") → SI v2 thêm chuẩn khẳng định cho giọng nói, mùi, chi tiết, —— chỉ trong thoại, tên Latin kèm ví dụ; blacklist cập nhật | Tác giả đánh giá | Tác giả
