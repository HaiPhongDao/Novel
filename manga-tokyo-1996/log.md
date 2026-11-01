# Decision Log — manga-tokyo-1996

## Hợp đồng lượt 01/11 (Tác giả: 'Mở một truyện manga mới, chạy trọn 3 đoạn đầu theo skill novel-craft 3.0')

| Ô | Nội dung |
|---|---|
| Kết quả | Truyện mới manga-tokyo-1996 có bible + SI v5 + 3 đoạn đã chốt và push, nối liền nhau |
| Kiểm chứng | Mỗi đoạn: soat_brief XANH + cong_doan xanh + review bằng đọc + git rev-list --count HEAD ^origin/<branch> = 0 |
| Không được đổi | Bible, dàn ý, SI, glossary sau khi đã chốt đoạn trước (chỉ thêm dữ kiện Writer vừa đặt) |
| Phạm vi | manga-tokyo-1996/ + README.md gốc + log.md; tài liệu chung commit riêng |
| Dừng và hỏi khi | Cần đổi canon/trục; một đoạn viết lại quá 2 lần; hết quota mọi acc; Tác giả nói 'để tôi duyệt' |

2026-11-01 | khoi-dong | Mở truyện mới `manga-tokyo-1996` trên nhánh `manga-v6` theo lựa chọn của Tác giả: Phương án 1 — Tokyo tháng 3/1996, trục Media Mix & Ủy ban Sản xuất (Tác giả Manga — Hãng đồ chơi Teito — Đài truyền hình Tokai), MC Kamishiro Ren (25 tuổi, tiền kiếp giám chế IP qua đời năm 2024), cứu nguy bộ truyện và dòng đồ chơi cơ giới 《极速齿轮》 trước nguy cơ bị rút vốn và bồi thường 120万日元 | Lý do: khác trục hoàn toàn với 1994 (tuần san ranking), 1998 (giải seinen), 2000 (cách mạng storyboard bán nguyệt san); đưa vào thế lực thứ ba là tập đoàn đồ chơi và nhà máy khuôn đúc | Duyệt: Tác giả (chọn phương án), Agent (thiết kế)
2026-11-01 | do-mau | Chạy `python tools/so_loi.py do-mau manga-tokyo-1996 --file 我在泡沫东京画漫画.txt`: 440.232 chữ Hán; ghi 6 đích nguồn `mau`: phủ định lặp 1.390, so sánh người kể 0.114, khuôn 实 0.034, nhãn ngữ điệu 0.030, thẻ thoại 1.329, lượt cụt 6.401 | Lý do: Bước 2 SKILL 3.0 — đặt đích tự động từ bộ mẫu trước khi viết | Duyệt: Agent
2026-11-01 | bible | Dựng Story Bible: overview.md (logline, hợp đồng độc giả, quỹ kết cục), glossary.md (bảng thể chế + đơn vị đo theo KN34), characters.md + 4 hồ sơ nhân vật, world.md (luật cứng Media Mix và kinh tế đồ chơi 1996), plot (arcs.md, outline.md 001–003, so-lieu.md, threads.md) | Lý do: AGENT.md mục 11 | Duyệt: Agent
2026-11-01 | si-v1 | Dựng `gemini/system-instruction-v1.md` từ `writer/SI-template` v5: phần dán `len()` = **7.849 ký tự** (≤ 8.000), 4 anchor nguyên văn từ `我在泡沫东京画漫画.txt` — ch.14 (134 字), ch.21 (168 字), ch.10 (192 字), ch.22 (137 字); `verify_anchors.py` khớp 4/4; `soat_van.py` trên 4 anchor sạch; PART 2 = 6 dòng (≤ 8), BANS = 5 dòng, neo độ dài câu 22–30 字; `dung_si.py` sinh `gemini/si-dan-gemini.txt` mã thoát 0. Bốn anchor từ 4 chương khác nhau và không trùng với 1994 (11,16,27,93), 1998 (1,2,3,4,5), 2000 (6,7,8,9) | Lý do: SKILL mục 7 — ngân sách ≤ 8.000, anchor ≤ 15% (thực tế 9%), giữ neo độ dài câu | Duyệt: Agent (SI mới)
