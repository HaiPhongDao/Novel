# Hạn Niên Săn Đồng (tên tạm)

> Thể loại: cổ đại hoang niên · điền văn · săn bắt sơn dã · bảng kỹ nghệ thuần thục. Quy trình: Writer-driven & State-kept.

**Logline:** Năm đại hạn thứ hai, cả núi Hắc Thạch bị quan bán cho nhà họ Lữ: vào núi phải có thẻ, săn được phải nộp bảy phần. Tần Dã nhập vào cậu thiếu niên bị đánh vì lén vào núi, nợ 240 văn tiền phạt hạn bảy ngày — và nhận ra khế bán núi chỉ ghi "từ mốc đá trở lên là núi", còn mảnh đậu xanh duy nhất của nhà cậu nằm dưới mốc đá. Thú rừng xuống ăn đậu là hàng của chủ ruộng.

## Writer

- **SI đang dùng:** [`gemini/si-claude.txt`](gemini/si-claude.txt) (tiếng Trung, phong cách 《乱世荒年》 do Claude viết lại từ đầu, dán tại [`gemini/si-dan-gemini.txt`](gemini/si-dan-gemini.txt)). Tác giả chỉ định dùng (10/11) trên nhánh `han-nien-writer-state`.
- **Mô hình làm việc:** **Writer-driven & State-kept**:
  - **Không cần bible:** Bỏ qua toàn bộ việc tạo và duy trì các file bible cồng kềnh.
  - **Nội dung để Writer quyết:** Writer toàn quyền sáng tạo diễn biến, hành động, thoại và tình huống theo ngòi bút tự nhiên.
  - **Agent giữ dữ liệu bằng State:** Quản lý liên tục `handoff/state.json` và `handoff/state.md` (tiền, kê, nợ phạt, bảng kỹ nghệ, ranh giới, đã kể). Brief mang dữ liệu State vào cho Writer và cập nhật State sau mỗi đoạn.
- **Lỗi riêng để soát:** `gemini/review-blacklist.md` (+ `../chung/review-blacklist.md`).

## Trạng thái (nhánh han-nien-writer-state)

| Đoạn | Prompt | Bản thảo | Review | Trạng thái |
|---|---|---|---|---|
| 001 | [`briefs/doan-001.md`](briefs/doan-001.md) | [`chapters/doan-001.md`](chapters/doan-001.md) (bản C-001, 3.729 字) | Chuẩn SI Claude | ✅ Đang dùng làm mốc xuất phát |
| 002 | [`briefs/doan-002.md`](briefs/doan-002.md) (State-brief) | ⏳ Chờ chạy Writer | — | ⏳ Sẵn sàng chạy |
| 003 | [`briefs/doan-003.md`](briefs/doan-003.md) | — | — | ⏳ Chờ đoạn 002 chốt State |
