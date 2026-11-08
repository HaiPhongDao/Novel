# Nhật ký quyết định

`ngày | đoạn/phạm vi | quyết định | lý do | ai duyệt`

2026-11-08 | khởi tạo | mở truyện mới `han-nien-san-dong` trên nhánh `han-nien-san-dong` (cắt từ nhánh mặc định) | Tác giả yêu cầu: dùng SI v2 của co-dai, tạo truyện mới, chỉ chuẩn bị nội dung 5–10 đoạn đầu | Tác giả (yêu cầu); tên truyện, tên nhân vật, dàn ý chờ duyệt
2026-11-08 | gemini/ | SI = `co-dai/gemini/test-giong/v2/si-v2` chép nguyên (7.895 ký tự, không sửa chữ nào); chưa qua bài hiệu chuẩn ĐẠT | Tác giả chỉ định dùng SI này | Tác giả
2026-11-08 | briefs/ | chọn mẫu A (AGENT.md mục 4), khung `.claude/skills/novel-craft/templates/brief-doan.md` | truyện mới nên hỏi Tác giả; chọn mặc định theo khung 29/10, Tác giả đổi được | chờ Tác giả
2026-11-08 | briefs/ + plot/outline.md | viết lại brief 001 theo nhịp ch1–ch3 bộ mẫu: Tình huống mang cái đầu của MC (người hiện đại, chết thế nào, đã đọc ký ức nguyên chủ, lỗi của nguyên chủ, nhà còn gì, hạn gì, hậu quả quá hạn, thử mẹo xuyên không rồi bỏ, bảng hiện có ngòi); phần ruộng tách sang 002 nên dàn ý thành 9 đoạn; mọi brief 002–009 thêm dòng MC muốn gì/lo gì | Tác giả chỉ ra brief 001 không nhắc MC xuyên qua, không nói nhà thế nào, cần làm gì | Tác giả (yêu cầu sửa); dàn ý mới chờ duyệt
2026-11-08 | doan-001 | chạy một bản (163s, 3.279 字), review SỬA NHẸ; dựng state.json nháp; sửa brief 002 (lật tin sai 'lên núi' bằng luống đậu) và 003 (lý chính bị đồn ăn nhậu nhà họ Lữ); thêm Vương Lão Thật vào glossary | Tác giả: 'Chạy đi, 1 bản thôi' | chờ Tác giả đọc và chốt
2026-11-08 | briefs/doan-001 (+002) | sửa đoạn Liễu thẩm: bỏ 'kể hết mọi chuyện về núi'; bà xin nửa cân kê cho con và trả bằng tin Lữ Lục cầm dây thừng đo sườn dốc; luật núi/giá chuyển thành phép tính trong đầu MC; 002 thêm lý do ra ruộng (xem chỗ Lữ Lục ngó xuống). Bản 001 lần 1 sẽ vào archive/ khi chạy lại | Tác giả: 'Thoại của Liễu thẩm lủng củng, đang mượn lương lại giải thích bối cảnh với MC' | chờ Tác giả đọc brief rồi mới chạy lại
