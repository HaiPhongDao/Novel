# Decision Log — manga-tokyo-1996

## Hợp đồng lượt 01/11 (Tác giả: 'Mở một truyện manga mới, chạy trọn 3 đoạn đầu theo skill novel-craft 3.0')

| Ô | Nội dung |
|---|---|
| Kết quả | Truyện mới manga-tokyo-1996 có bible + SI v1 + 3 đoạn đã chốt và push, nối liền nhau |
| Kiểm chứng | Mỗi đoạn: soat_brief XANH + cong_doan xanh + review bằng đọc + git rev-list --count HEAD ^origin/<branch> = 0 |
| Không được đổi | Bible, dàn ý, SI, glossary sau khi đã chốt đoạn trước (chỉ thêm dữ kiện Writer vừa đặt) |
| Phạm vi | manga-tokyo-1996/ + README.md gốc + log.md; tài liệu chung commit riêng |
| Dừng và hỏi khi | Cần đổi canon/trục; một đoạn viết lại quá 2 lần; hết quota mọi acc; Tác giả nói 'để tôi duyệt' |

2026-11-01 | doi-truc | Tác giả phản hồi đoạn 1 cũ chưa đạt, mở đầu quá dồn dập số liệu kỹ thuật, không thích thể loại đồ chơi, chuyển hẳn sang thuần túy vẽ manga. Tác giả chọn Hướng 1: Tân binh & Chiếc bàn vẽ nghiêng — Cuộc chiến Oneshot 31 trang (Tokyo 1996) | Lý do: Tác giả nắm tối cao về nội dung và định hướng; quay về cốt lõi ma sát nghề vẽ truyện tranh | Duyệt: Tác giả
2026-11-01 | bible-v2 | Dựng lại Story Bible theo Hướng 1: overview.md (cuộc chiến Oneshot 31 trang 《野犬之刃》), glossary.md (bảng thể chế toà soạn Đại Đô Xã, giấy Kent 135kg, ngòi G-pen Zebra, tram IC Screen theo KN34), characters.md (Kamishiro Ren 23 tuổi, Nogami Shinji 32 tuổi BTV SPARK, Asakura Ken 20 tuổi trợ lý), world.md (Kanda Jimbocho và Koenji), plot (outline 001–003, arcs, threads, so-lieu) | Lý do: Đổi trục nội dung | Duyệt: Agent
2026-11-01 | si-v1-rebuild | Dựng lại `gemini/system-instruction-v1.md` khớp bối cảnh nghề vẽ manga tuần san: phần dán 7.911 ký tự, 4 anchor từ `我在泡沫东京画漫画.txt` khớp 4/4 (ch.14, 21, 10, 22), PART 2 = 6 dòng, BANS = 5 dòng, neo độ dài câu 22–30 字; `dung_si.py` sinh `si-dan-gemini.txt` exit 0 | Lý do: SKILL mục 7 | Duyệt: Agent
2026-11-01 | doan-001-v2 | Chạy batch 3 biến thể brief cho đoạn 001 mới: a (2.651 字, 13/18), b (2.500 字, 13/18), c (2.324 字, 15/18, 0 phủ định lặp, 0 khuôn 实, nhịp câu 24,2 字/câu). Chọn bản c làm chapters/doan-001.md vì nhịp điệu sinh hoạt và ma sát nghề vẽ xuất sắc, phản ánh đúng tinh thần nghề manga thập niên 90. Trình toàn văn để Tác giả duyệt theo yêu cầu | Lý do: Tác giả yêu cầu duyệt đoạn 1 trước khi làm tiếp | Duyệt: Chờ Tác giả
