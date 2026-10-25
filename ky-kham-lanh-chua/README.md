# 骑砍领主：铁脊要塞

Truyện mới, mở 26/10/2026 — **chưa chốt tiền đề**. Đang ở pha đo giọng: phân tích bộ mẫu → SI v1 → chạy
thử một cảnh của bộ mẫu để so.

## Tài liệu

| ở đâu | cái gì |
|---|---|
| `mau/phan-tich-mau.md` | phân tích bộ mẫu `领主：我用骑砍系统肝经验` (886 chương dùng được): nhịp, từ vựng, cỗ máy, hình chương |
| `mau/goc-t1-ch08.md` | nguyên văn chương 8 của mẫu — cảnh dùng làm bài test |
| `../ky-kham-dan-thuong/mau-tham-khao.txt` | bản đầy đủ bộ mẫu (6,8 MB, md5 `0b7e1a34b7c3e78677d73410d3e345d3`) — trùng file trên Desktop, không chép thêm một bản 7 MB vào git |
| `bible/overview.md` | tiền đề v0 + 2 phương án khác, **chờ Tác giả chốt** |
| `bible/glossary.md` | 阶级 / 兵种 / 爵位 / xưng hô / tiền, v0 |
| `gemini/system-instruction.md` | SI v1, dựng từ `writer/SI-template` v3 (7 anchor chép nguyên văn) |
| `gemini/si-dan-gemini.txt` | phần dán được của SI v1 |
| `gemini/si-test-mau.txt` | SI v1 đổi tên sang tên bộ mẫu — dùng cho test |
| `briefs/test-mau-01.md` | prompt test 01: chỉ có sự việc, không dặn cách viết |
| `chapters/test-01.md` | bản ra test 01: 2.645 字 |
| `chapters/chuong-001-a.md` · `-b.md` · `-c.md` | ch1: bản máy 2.786 字 → sửa tật 2.647 → sửa thoại 3.108 |
| `reviews/test-mau-01.md` | bảng số + đọc bốn câu hỏi + 4 sửa cho SI v2 |
| `reviews/so-sanh-test-01.md` | **so nguyên văn ↔ bản SI từng đoạn** (mở cảnh, ra lệnh, cung thủ chậm, bảng exp, kết cảnh) |
| `archive/thinking-test-01.md` | thinking của lần chạy (đọc khi SI bị hiểu sai) |

## Trạng thái

- [x] Phân tích bộ mẫu (số đo toàn sách)
- [x] SI v1 theo template, 7 anchor nguyên văn
- [x] Test 01 trên cảnh ch8: cổng kỹ thuật đạt, **giọng chưa đạt** (thiếu sổ riêng của MC, thiếu câu châm,
      bảng in sai dạng, dài +27%) → so nguyên văn từng đoạn ở `reviews/so-sanh-test-01.md`
- [x] Chốt tiền đề A + SI v2 (4 sửa) + bible (`characters.md`) + 黄金三章 (`plot/arcs.md`)
- [x] Chương 1: bản A (2.786 字, 6 tật) → bản B sửa tay (2.663 字, 0 tật) → `reviews/chuong-001.md`
- [ ] **Tác giả đọc bản C** — duyệt mới viết chương 2
- [x] Bản C: sửa thoại MC theo bắt lỗi "nói chưa đầy đủ, giao tiếp trống không" (SI v3 thêm 2 dòng luật thoại)
- [ ] Trước chương 2: ghi số 字 vào brief (2.100, không quá 2.300) + gộp cảnh để hạ lượt thoại 47 → ~25
