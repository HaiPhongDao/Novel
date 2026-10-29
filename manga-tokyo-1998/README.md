# manga-tokyo-1998 — Phép thử hệ thống SI-template v5 + brief mẫu A + soat_brief

- **Logline:** Tháng 11/1998 tại Tokyo thời suy thoái hậu bong bóng, Fujimoto Ren — một người xuyên việt nhập vào cậu trợ lý thực tập nghèo trong xưởng manga tuần san — lén mang tập bản thảo 64 trang 《记忆碎片》 đi nộp giải thưởng lớn 150 vạn yên ngay ngày hạn chót, tình cờ bắt cặp với Shirakawa Mio, nữ biên tập viên đang đứng chót bảng thành tích của tòa soạn.
- **Bộ mẫu:** `../我在泡沫东京画漫画.txt` (214 chương, trung bình 2.045 字/chương, trung vị 1.910 字/chương; lời kể 80,1% / thoại 19,9% theo 字; độ dài câu kể trung bình 22,0 字/câu, trung vị 19,0 字/câu; thẻ thoại/lượt = 0,10; khối `【】` = 0,45 lần/chương).
- **SI đang dùng:** `gemini/system-instruction-v1.md` (bản dán `gemini/si-dan-gemini.txt`: **7.938 ký tự** `len()`, 5 anchor nguyên văn từ chương 1, 2, 3, 4, 5 của bộ mẫu, `verify_anchors.py` 5/5 khớp, `soat_van.py` 0 tật).
- **Khung brief:** Mẫu A (`templates/brief-doan.md`), qua cổng `tools/soat_brief.py`.

## Bảng trạng thái từng đoạn

| Đoạn | Brief | Bản thảo | Số chữ (字) | Review | Trạng thái |
|---|---|---|---|---|---|
| Mốc (chỉ SI) | `briefs/doan-000-moc.md` | `archive/doan-000-moc.md` | 2.938 字 | Đối chiếu trong `reviews/doan-001.md` | ✅ Đã chạy mốc |
| 001 | `briefs/doan-001.md` | `chapters/doan-001.md` | 3.390 字 | `reviews/doan-001.md` | ✅ ĐẠT |
| 002 | `briefs/doan-002.md` | `chapters/doan-002.md` | — | `reviews/doan-002.md` | Chờ chạy |
| 003 | `briefs/doan-003.md` | `chapters/doan-003.md` | — | `reviews/doan-003.md` | Chờ chạy |
