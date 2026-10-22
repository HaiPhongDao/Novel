# Trăm Lần Chết Mới Lên Luyện Khí (tên tạm)

> Truyện thứ ba của xưởng. Luật chung: `../AGENT.md`; quy trình bàn giao, chạy AI Studio, lỗi văn chung: `../chung/`. Truyện tham khảo (Tác giả tải lên 23/10): `tham-khao/` — xem `tham-khao/phan-tich.md`.

**Logline:** Một tester game xuyên vào thân tạp dịch ngũ linh căn của Thanh Lam Tông, còn 90 ngày nữa là bị bán xuống mỏ — và có một máy mô phỏng cho anh sống thử cả đời mình, chết, rồi mang về đúng một thứ.

## Trạng thái — khởi động (AGENT.md mục 11)

| Bước | Trạng thái |
|---|---|
| Phân tích truyện tham khảo | ✅ `tham-khao/phan-tich.md` |
| `bible/overview.md` | 📝 đề xuất — chờ Tác giả |
| `bible/glossary.md` | 📝 đề xuất tên chữ Hán + chuỗi cố định của máy mô phỏng |
| `bible/characters/` | 📝 `tham-nghien.md`, `nhan-vat-phu.md` |
| `bible/world.md` | 📝 8 luật cứng của máy mô phỏng |
| `plot/arcs.md` → `plot/outline.md` | 📝 arc 1 "Chín mươi ngày" 16 đoạn (011–013 để ngỏ) |
| SI | 📝 v1 `gemini/system-instruction.md` — đã test bản 1; chưa đạt, xem `reviews/doan-001-test-v1-01.md` |
| `handoff/` | 📝 canon-card, state (đoạn 0), quiz |
| Prompt đoạn 001 | Đã soạn `briefs/doan-001.md` để test theo yêu cầu Tác giả |

## Writer

- SI hiện tại: `gemini/system-instruction.md` **v1**, tông 轻松爽文、无敌流, mục 4 hướng dẫn dùng 梗; 7 mục + PART 4 máy mô phỏng, giữ 9 anchor. V0 đã lưu `archive/system-instruction-v0.md`. V1 đã nạp và test trên AI Studio trong browser tích hợp; 12936 ký tự LF. Bản test vẫn nặng nề và sai cơ chế máy, chưa chốt SI.
- Theo `../writer/SI-template` (hướng dẫn 1): viết thử đoạn 001 vài bản ở session riêng trước khi chốt SI.
- Lỗi riêng để soát: `gemini/review-blacklist.md` (+ `../chung/review-blacklist.md`).

| Đoạn | Prompt | Bản thảo | Review | Chốt |
|---|---|---|---|---|
| 001 test v0-01 | `briefs/doan-001.md` | `archive/doan-001-test-v0-01.md` | `reviews/doan-001-test-v0-01.md`: VIẾT LẠI | Chưa chốt |
| 001 test v0-02 | `archive/doan-001-test-v0-02-prompt.md` | `archive/doan-001-test-v0-02.md` | `reviews/doan-001-test-v0-02.md`: VIẾT LẠI | Chưa chốt |
| 001 test v1-01 | `archive/doan-001-test-v1-01-prompt.md` | `archive/doan-001-test-v1-01.md` | `reviews/doan-001-test-v1-01.md`: VIẾT LẠI | Chưa chốt |
| 001 | `briefs/doan-001.md` | `chapters/doan-001.md` | `reviews/doan-001.md`: ĐẠT | ✅ |
| 002 | `briefs/doan-002.md` | `chapters/doan-002.md` | `reviews/doan-002.md`: ĐẠT | ✅ |
| 003 | `briefs/doan-003.md` | `chapters/doan-003.md` | `reviews/doan-003.md`: ĐẠT | ✅ |
| 004 | `briefs/doan-004.md` | `chapters/doan-004.md` | `reviews/doan-004.md`: ĐẠT | ✅ |

Test 23/10: Chrome báo permission denied; browser tích hợp chạy thành công Gemini 3.8 Flash / High / Search tắt. Bản test 2943 chữ Hán, có lỗi canon và điểm nhìn; giữ SI v0, chưa bắt đầu tiến độ chính thức.

Cách chạy một đoạn: `../README.md` mục "Một vòng đoạn".

## Tiến độ chính thức

Đã chốt đến đoạn **004**. Tác giả duyệt giọng SI v1; Agent tự duyệt canon và push từng đoạn theo yêu cầu 23/10. Xem `handoff/state.md`.
