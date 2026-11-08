# Hạn Niên Săn Đồng (tên tạm)

> Thể loại: cổ đại hoang niên · điền văn · săn bắt sơn dã · bảng kỹ nghệ thuần thục. Luật chung: [`../AGENT.md`](../AGENT.md).

**Logline:** Năm đại hạn thứ hai, cả núi Hắc Thạch bị quan bán cho nhà họ Lữ: vào núi phải có thẻ, săn được phải nộp bảy phần. Tần Dã nhập vào cậu thiếu niên bị đánh vì lén vào núi, nợ 240 văn tiền phạt hạn bảy ngày — và nhận ra khế bán núi chỉ ghi "từ mốc đá trở lên là núi", còn mảnh đậu xanh duy nhất của nhà cậu nằm dưới mốc đá hai mươi ba bước. Thú rừng xuống ăn đậu là hàng của chủ ruộng.

## Writer

- **SI đang dùng:** [`gemini/system-instruction.md`](gemini/system-instruction.md) = SI v2 của `co-dai` chép nguyên văn (7.895 ký tự); bản dán sẵn [`gemini/si-dan-gemini.txt`](gemini/si-dan-gemini.txt). Tác giả chỉ định dùng (08/11). **Chưa qua bài hiệu chuẩn ĐẠT.**
- **Mẫu prompt:** mẫu A (khung `.claude/skills/novel-craft/templates/brief-doan.md`). Brief 001 mang đủ thiết lập vì chưa có State; từ 002 trở đi Writer đọc State.
- **Lỗi riêng để soát:** `gemini/review-blacklist.md` (+ `../chung/review-blacklist.md`).

## Việc kế — thoại trước (09/11, Tác giả: "sửa này trước chốt đã")

Giọng chữ (thổ ngữ, chữ cổ, cụm sáo, "giọng AI"): SI-R, SI-R2 **Tác giả bác** ("chẳng thấy thay đổi gì mấy, còn giảm chất lượng prose") — Tác giả chọn giao Argon: [`prompt-argon.md`](prompt-argon.md) → đã có [`de-xuat-argon.md`](de-xuat-argon.md) kèm SI và gói bàn giao sạch tại [`gemini/test-giong/giong-v3/`](gemini/test-giong/giong-v3/); đếm tật bằng `python tools/tat_ai.py dem --ds han-nien-san-dong/gemini/tat-giong-ai.txt <bản>` — [`gemini/test-giong/doc-giong.md`](gemini/test-giong/doc-giong.md). Thoại: Tác giả "hơi ổn rồi, để về sau test thêm". Bốn lượt thử thoại: [`gemini/test-giong/doc-thoai.md`](gemini/test-giong/doc-thoai.md). Chờ Tác giả đọc bản ch3 và trả lời: thoại kiểu đó có đạt không. SI đang dùng không đổi. Việc giữ mạch (dưới đây) làm sau khi thoại chốt.

## Việc kế — giữ mạch giữa các đoạn (cập nhật 09/11 — DỪNG chạy Writer, chờ Tác giả duyệt cách sửa)

**Vấn đề (xem `log.md`, dòng 09/11 'VẤN ĐỀ'):** 002 và 003 hiện có viết lại/tóm tắt lại chuyện đoạn trước, lặp ý, thiếu liên kết. Nguyên nhân: mỗi đoạn chạy phiên Writer mới (`--new`) chỉ với State + 2.500 ký tự cuối; brief nhắc lại việc cũ; `canon-card.md` lộ sẵn '23 bước' và nội dung khế.

**Hướng sửa đề xuất (chưa chạy, chờ Tác giả):**
1. Gỡ hai câu lộ trước khỏi `handoff/canon-card.md` ('khế bán núi tính núi từ mốc đá trở lên…', 'mốc đá cách bờ ruộng hai mươi ba bước').
2. Viết lại brief 002/003 chỉ ghi **việc mới**, mở bằng hành động nối ngay câu cuối đoạn trước; không nhắc 240 văn, kê, Lữ Lục, chuyện nhà Vương nếu đoạn trước đã kể.
3. Chạy 002 và 003 **trong cùng một chat** (`aistudio_run.py --new …` cho 002, rồi `--chat <URL chat đó>` cho 003; 2 đoạn/phiên theo `../AGENT.md` mục 5c); 004+005 một chat mới, cứ thế.
4. Review thêm một mục 'tóm tắt lại / lặp ý đoạn trước'. Bản 002/003 hiện tại giữ nguyên, chuyển `archive/` khi chạy lại (bản 002 v1 và State sau 002 v1 đã có ở `archive/`).

**Trạng thái brief:** 002, 003, 004 là brief trơn (cần sửa theo mục 2); 005–009 vẫn là bản dài cũ — viết lại trơn rồi mới chạy. Chưa chạy 004 (không có file). Đã đọc/ghi: 002 (5.010 字), 003 (5.054 字), State tới 003.

Quy trình mỗi đoạn (vẫn dùng): `build_pack.py … --tail 2500 --prompt briefs/doan-00N.md` rồi `aistudio_run.py` (chạy nền, **một** lệnh chờ; cần Edge mở với extension); gỡ dòng `<!-- -->` đầu file; `cong_doan.py`; đỏ 'bản cụt' (câu cuối kết bằng dấu phẩy) = lỗi mạng AI Studio, chuyển bản vào `archive/` rồi chạy lại. Chỉ sửa **tên riêng** sai bằng thay thế; ghi review, State, log; commit + push; không tự chốt ĐẠT. Nếu Writer đặt tên trùng nhân vật khác trong bible thì đổi tên trong bản Writer, không đổi bible.

## Trạng thái

| Đoạn | Prompt | Bản thảo | Review | Chốt |
|---|---|---|---|---|
| 001 | [`briefs/doan-001.md`](briefs/doan-001.md) | [`chapters/doan-001.md`](chapters/doan-001.md) (v2, 3.636 字; v1 ở `archive/`) | [`reviews/doan-001.md`](reviews/doan-001.md) — SỬA NHẸ → đề xuất VIẾT LẠI (09/11) | ⏳ chờ Tác giả |
| 002 | [`briefs/doan-002.md`](briefs/doan-002.md) (trơn) | [`chapters/doan-002.md`](chapters/doan-002.md) (v2, 5.010 字; v1 ở `archive/`) | [`reviews/doan-002.md`](reviews/doan-002.md) — SỬA NHẸ → đề xuất VIẾT LẠI (09/11) | ⏳ chờ Tác giả |
| 003 | [`briefs/doan-003.md`](briefs/doan-003.md) (trơn) | [`chapters/doan-003.md`](chapters/doan-003.md) (5.054 字) | [`reviews/doan-003.md`](reviews/doan-003.md) — SỬA NHẸ → đề xuất VIẾT LẠI (09/11) | ⏳ chờ Tác giả |
| 004 | [`briefs/doan-004.md`](briefs/doan-004.md) | — | — | ⏳ |
| 005 | [`briefs/doan-005.md`](briefs/doan-005.md) | — | — | ⏳ |
| 006 | [`briefs/doan-006.md`](briefs/doan-006.md) | — | — | ⏳ |
| 007 | [`briefs/doan-007.md`](briefs/doan-007.md) | — | — | ⏳ |
| 008 | [`briefs/doan-008.md`](briefs/doan-008.md) | — | — | ⏳ |
| 009 | [`briefs/doan-009.md`](briefs/doan-009.md) | — | — | ⏳ |
