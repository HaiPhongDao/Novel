# Hạn Niên Săn Đồng (tên tạm)

> Thể loại: cổ đại hoang niên · điền văn · săn bắt sơn dã · bảng kỹ nghệ thuần thục. Luật chung: [`../AGENT.md`](../AGENT.md).

**Logline:** Năm đại hạn thứ hai, cả núi Hắc Thạch bị quan bán cho nhà họ Lữ: vào núi phải có thẻ, săn được phải nộp bảy phần. Tần Dã nhập vào cậu thiếu niên bị đánh vì lén vào núi, nợ 240 văn tiền phạt hạn bảy ngày — và nhận ra khế bán núi chỉ ghi "từ mốc đá trở lên là núi", còn mảnh đậu xanh duy nhất của nhà cậu nằm dưới mốc đá hai mươi ba bước. Thú rừng xuống ăn đậu là hàng của chủ ruộng.

## Writer

- **SI đang dùng:** [`gemini/system-instruction.md`](gemini/system-instruction.md) = SI v2 của `co-dai` chép nguyên văn (7.895 ký tự); bản dán sẵn [`gemini/si-dan-gemini.txt`](gemini/si-dan-gemini.txt). Tác giả chỉ định dùng (08/11). **Chưa qua bài hiệu chuẩn ĐẠT.**
- **Mẫu prompt:** mẫu A (khung `.claude/skills/novel-craft/templates/brief-doan.md`). Brief 001 mang đủ thiết lập vì chưa có State; từ 002 trở đi Writer đọc State.
- **Lỗi riêng để soát:** `gemini/review-blacklist.md` (+ `../chung/review-blacklist.md`).

## Việc kế (chờ Tác giả)

1. Duyệt tên truyện, tên nhân vật (`bible/glossary.md`), premise (`bible/overview.md`) và dàn ý arc 1 (`plot/outline.md`).
2. Đọc brief 001–008 trong `briefs/` (tám brief đã qua cổng `tools/soat_brief.py --goi`: XANH; chỉ 007 còn một cảnh báo "hai cảnh").
3. Chạy 001 (`python tools/aistudio_run.py --new --si han-nien-san-dong/gemini/si-dan-gemini.txt --prompt han-nien-san-dong/briefs/doan-001.md --out han-nien-san-dong/chapters/doan-001.md`), Tác giả đọc; rồi dựng `handoff/state.json` theo `chung/state-extractor.md` và **sửa brief 002–008 cho khớp bản thảo** trước khi chạy tiếp (mỗi session Writer chỉ 2 đoạn).

## Trạng thái

| Đoạn | Prompt | Bản thảo | Review | Chốt |
|---|---|---|---|---|
| 001 | [`briefs/doan-001.md`](briefs/doan-001.md) | — | — | ⏳ chưa chạy |
| 002 | [`briefs/doan-002.md`](briefs/doan-002.md) | — | — | ⏳ |
| 003 | [`briefs/doan-003.md`](briefs/doan-003.md) | — | — | ⏳ |
| 004 | [`briefs/doan-004.md`](briefs/doan-004.md) | — | — | ⏳ |
| 005 | [`briefs/doan-005.md`](briefs/doan-005.md) | — | — | ⏳ |
| 006 | [`briefs/doan-006.md`](briefs/doan-006.md) | — | — | ⏳ |
| 007 | [`briefs/doan-007.md`](briefs/doan-007.md) | — | — | ⏳ |
| 008 | [`briefs/doan-008.md`](briefs/doan-008.md) | — | — | ⏳ |
