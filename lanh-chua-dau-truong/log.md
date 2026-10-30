# Log — Quyết định và sự kiện

## 2026-10-31 | Khởi tạo truyện mới `lanh-chua-dau-truong`
- **Tiền đề:** Tây huyễn lãnh chúa + kinh doanh đấu trường; trục "kinh tế máu và tiền". Chọn trục này vì repo đã có hai truyện 领主 khác trục hoàn toàn: `lanh-chua-chip` (kỹ sư/hạ tầng, chip hỏng) và `lanh-chua-tien-don` (phòng thủ tiền đồn, binh công). Truyện mới bán vé và tỷ lệ cược, không xây tường trước.
- **Tổng hợp bộ mẫu:** đo 3 bộ mẫu có trong repo — goblin 500 chương dùng được (31,2 字/câu, thoại 19%, 0 khối 【】/chương), lam-game 1.038 chương (34,5 字/câu, thoại 24%, 1,9 khối 【】/chương), soi-xam 251 chương (20,6 字/câu, thoại 29%, 3,7 khối 【】/chương). Chọn register goblin (领主/种田, đám đông, bảng) + nhịp câu 22–30; mật độ 【】 đặt ở mức thấp (≤2 khối/đoạn) vì mẫu 领主 kể bảng nhiều hơn in bảng.
- **SI v1:** dựng từ `writer/SI-template` v5; 5 anchor nguyên văn từ goblin (ch.46, 44, 48, 47, 45); phần dán **7.887 ký tự**; PART 2 4 dòng; BANS 5 dòng; PART 4 bảng 【斗兽账房】 đúng mẫu số của `plot/so-lieu.md`.
- **Khung brief:** Mẫu A (tình huống + Khoá + Dừng + Bảng), qua `tools/soat_brief.py`.
- **Số khởi điểm:** nợ 120 vàng/40 ngày; quỹ 4 vàng 12 银; kho 12.000 斤 (11 ngày); 1.100 dân; 900/3.000 chỗ; vé 2/8 铜, 1 银.
- **Mục tiêu phiên:** chạy và chốt trọn vòng 3 đoạn đầu (001 → 003), push lên nhánh `thu-v5-manga-tokyo-1998`.

## 2026-10-31 | Anchor và cổng SI
- `verify_anchors.py`: 5/5 anchor khớp nguyên văn nguồn.
- `soat_van.py` từng anchor: 0 phủ định lặp, 0 so sánh người kể, 0 nhãn ngữ điệu, 0 khuôn 实, 0 từ hiện đại.
- Phần dán 8.478 → **7.887** ký tự sau khi cắt anchor 1/3/4 và 6 câu luật không cần.
2026-10-31 | doan-001 | Chốt đoạn 001 "Tờ khế trên cổng" (3.239 字, AI Studio 194s) | Vượt cửa sổ brief 30% (Writer tự nhẩm 2.200–2.400); giữ bản sau khi cắt khối tính sổ lặp; sửa 8 chỗ (số học 28 银, chuỗi tiền 5 vàng 2 银, tay trái Bram, 4 nhãn ngữ điệu, 3 từ hiện đại, 郡律/男爵大人) | Duyệt: Agent
