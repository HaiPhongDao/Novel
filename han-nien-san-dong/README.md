# Hạn Niên Săn Đồng (tên tạm)

> Thể loại: cổ đại hoang niên · điền văn · săn bắt sơn dã · bảng kỹ nghệ thuần thục. Luật chung: [`../AGENT.md`](../AGENT.md).

**Logline:** Năm đại hạn thứ hai, cả núi Hắc Thạch bị quan bán cho nhà họ Lữ: vào núi phải có thẻ, săn được phải nộp bảy phần. Tần Dã nhập vào cậu thiếu niên bị đánh vì lén vào núi, nợ 240 văn tiền phạt hạn bảy ngày — và nhận ra khế bán núi chỉ ghi "từ mốc đá trở lên là núi", còn mảnh đậu xanh duy nhất của nhà cậu nằm dưới mốc đá hai mươi ba bước. Thú rừng xuống ăn đậu là hàng của chủ ruộng.

## Writer

- **SI đang dùng:** [`gemini/system-instruction.md`](gemini/system-instruction.md) = SI v2 của `co-dai` chép nguyên văn (7.895 ký tự); bản dán sẵn [`gemini/si-dan-gemini.txt`](gemini/si-dan-gemini.txt). Tác giả chỉ định dùng (08/11). **Chưa qua bài hiệu chuẩn ĐẠT.**
- **Mẫu prompt:** mẫu A (khung `.claude/skills/novel-craft/templates/brief-doan.md`). Brief 001 mang đủ thiết lập vì chưa có State; từ 002 trở đi Writer đọc State.
- **Lỗi riêng để soát:** `gemini/review-blacklist.md` (+ `../chung/review-blacklist.md`).

## Việc kế (bàn giao cho phiên mới — 08/11, Tác giả: "cứ ra brief và chạy, chi phí gần như miễn phí, tôi lười đọc brief")

Đã chạy 001 (v2) và 002; chờ Tác giả đọc và quyết ĐẠT. Còn **003–009**. Mỗi đoạn một lượt, **một phiên Writer mới** (gói bàn giao + brief), đọc, sửa tên riêng, cập nhật State, rồi mới sang đoạn kế:

1. Đọc `../AGENT.md` mục 5c → file này → `log.md` → `handoff/state.json` → `reviews/doan-002.md` (đừng đọc cả chương cũ).
2. `python -I -X utf8 tools/build_pack.py han-nien-san-dong --tail 2500 --prompt briefs/doan-00N.md` rồi
   `python tools/aistudio_run.py --new --si han-nien-san-dong/gemini/si-dan-gemini.txt --prompt han-nien-san-dong/handoff/session-start.md --out han-nien-san-dong/chapters/doan-00N.md --timeout 22` (chạy nền, **một** lệnh chờ; cần Edge mở với extension).
3. Gỡ dòng `<!-- ... -->` đầu file; `python tools/cong_doan.py <bản> --prompt <brief>`. **ĐỎ "bản cụt" (câu cuối kết bằng dấu phẩy) = lỗi mạng AI Studio: chuyển bản vào `archive/` rồi chạy lại** (đã gặp ở 002).
4. Đọc bản; sửa tên riêng sai bằng thay thế (được phép); ghi `reviews/doan-00N.md`; cập nhật `handoff/state.json` (scene_bridge, ledger, conflicts); **sửa brief N+1 cho khớp bản Writer vừa viết** (Writer tự đặt chi tiết rất nhiều); commit + push.
5. Chỉ ghi tên đã thấy trong cảnh; nếu Writer đặt tên trùng nhân vật khác trong bible (ví dụ 邱老栓) thì đổi tên bản Writer, không đổi bible.

Khuôn kiểm: brief giữ dạng tình huống + một dòng Khoá + Dừng ở; không thêm lời thoại mẫu, không liệt kê thông tin cho NPC "kể" (bài học Liễu thẩm).

## Trạng thái

| Đoạn | Prompt | Bản thảo | Review | Chốt |
|---|---|---|---|---|
| 001 | [`briefs/doan-001.md`](briefs/doan-001.md) | [`chapters/doan-001.md`](chapters/doan-001.md) (v2, 3.636 字; v1 ở `archive/`) | [`reviews/doan-001.md`](reviews/doan-001.md) — SỬA NHẸ | ⏳ chờ Tác giả đọc |
| 002 | [`briefs/doan-002.md`](briefs/doan-002.md) (trơn) | [`chapters/doan-002.md`](chapters/doan-002.md) (v2, 5.010 字; v1 ở `archive/`) | [`reviews/doan-002.md`](reviews/doan-002.md) — SỬA NHẸ | ⏳ chờ Tác giả đọc |
| 003 | [`briefs/doan-003.md`](briefs/doan-003.md) | — | — | ⏳ |
| 004 | [`briefs/doan-004.md`](briefs/doan-004.md) | — | — | ⏳ |
| 005 | [`briefs/doan-005.md`](briefs/doan-005.md) | — | — | ⏳ |
| 006 | [`briefs/doan-006.md`](briefs/doan-006.md) | — | — | ⏳ |
| 007 | [`briefs/doan-007.md`](briefs/doan-007.md) | — | — | ⏳ |
| 008 | [`briefs/doan-008.md`](briefs/doan-008.md) | — | — | ⏳ |
| 009 | [`briefs/doan-009.md`](briefs/doan-009.md) | — | — | ⏳ |
