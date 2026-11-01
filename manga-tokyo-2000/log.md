# Decision Log — manga-tokyo-2000

## Hợp đồng lượt 31/10 (Tác giả: 'Mở truyện từ đầu, dựng SI v5, chạy và chốt trọn vòng 3 đoạn đầu 001 → 003')

| Ô | Nội dung |
|---|---|
| Kết quả | Truyện mới manga-tokyo-2000 có bible + SI v5 + 3 đoạn đã chốt và push, nối liền nhau |
| Kiểm chứng | mỗi đoạn: soat_brief XANH + cong_doan xanh + review bằng đọc + git rev-list --count HEAD ^origin/<branch> = 0 |
| Không được đổi | bible, dàn ý, SI, glossary sau khi đã chốt đoạn trước (chỉ thêm dữ kiện Writer vừa đặt) |
| Phạm vi | manga-tokyo-2000/ + README.md gốc + log.md; tài liệu chung commit riêng |
| Dừng và hỏi khi | cần đổi canon/trục; một đoạn viết lại quá 2 lần; hết quota mọi acc |

2026-10-31 | khoi-dong | Mở truyện mới `manga-tokyo-2000` trên nhánh `thu-v5-manga-tokyo-1998` theo yêu cầu của Tác giả (manga năm 2000 trở lên, MC xuyên qua). Bối cảnh tháng 10/2000 Tokyo, nhà xuất bản hư cấu 白圆社 + bán nguyệt san thanh niên 《青年世纪》, MC Hayakawa Ryo (23 tuổi), trục "cách mạng phân cảnh điện ảnh & giật gân giải cứu nguyệt san trước làn sóng thiên niên kỷ" | Duyệt: Tác giả (đơn đặt hàng), Agent (phương án)
2026-10-31 | do-mau | Dùng lại số đo bộ mẫu 我在泡沫东京画漫画.txt (214 chương, 2.045 字/chương trung bình, lời kể 80,1%, câu kể 22,0 字, thẻ thoại 0,10/lượt) | Duyệt: Agent
2026-10-31 | doan-001 | Chạy 3 bản chọn hình dạng prompt (A: 2.817 字, B: 2.917 字, C: 3.728 字). Chốt Bản B làm chapters/doan-001.md (74/100, canon 10/10, 0 thiếu số, 0 so sánh, median đoạn 33 chữ sát mẫu) | Review đạt | Duyệt: Agent
2026-10-31 | doan-002 | Chạy Writer Gemini bản 1 (2.294 字, 144s, acc /u/0). Sửa nhẹ 6 so sánh người kể + 2 nhãn ngữ điệu theo BANS SI v5 -> văn 34/34 tuyệt đối, 27,2 字/câu, chốt làm chapters/doan-002.md (2.244 字) | Kurosawa ra điều kiện 5 ngày nộp 32 trang mực hoàn chỉnh có dán lưới (18:00 ngày 24/10) | Duyệt: Agent
2026-10-31 | doan-003 | Chạy Writer Gemini bản 1 (2.227 字, 209s, acc /u/0). 0 so sánh, 0 实, 0 nhãn ngữ điệu, văn 34/34 tuyệt đối, số học khớp 100% (4.600 + 88.000 - 72.000 = 20.600 日元). Hoàn thành trọn vẹn 黄金三章 (001 -> 003) | Duyệt: Agent
2026-11-01 | si-doi | Phục hồi đủ chuỗi đời SI từ git sau hai lần viết lại trong ngày 01/11 không đổi tên file (đời thật không có tên). `system-instruction-v1.md` (f118d09, 8.156 ký tự, đủ BANS+LENGTH+PART 3) · `v2` (5f0e8e7, 2.773, bỏ BANS/LENGTH/PART 2/PART 3) · `v3` (6bccaa3, 4.749, thêm anchor dài). Bản đang chạy = **v3**. `tools/dung_si.py` giờ trả mã thoát 1 (đang nợ cấu trúc: 0 BANS, 0 PART 2, 2 anchor = 43% phần dán, mất neo độ dài câu) | Lý do: đổi SI mà không ghi log/README/đổi tên đời làm câu hỏi "thêm dòng đó có tác dụng không" không trả lời được; neo độ dài câu là con số an toàn duy nhất nên có trong SI (`si-test-tren-mau.md`) | Duyệt: Agent (phục hồi đúng nội dung lịch sử, không đổi luật nào đang chạy)
