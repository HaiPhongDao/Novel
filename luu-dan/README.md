# Lưu Dân (tên tạm)

> Thể loại: Lịch sử giá không · Loạn thế lưu dân (kiểu Khăn Vàng) · Bảng kỹ nghệ thuần thục. Quy trình: Writer-driven & State-kept.

**Logline:** Thời loạn thế lịch sử giá không, triều đình mục nát, các cánh quân lưu dân nổi dậy cuốn theo biển người đói khát. Một người hiện đại xuyên không thành thiếu niên lưu dân dưới đáy đang co ro bên lề bãi trại đói lả, dựa vào cái đầu thực tế và bảng kỹ nghệ chỉ mình nhìn thấy, từ một mẩu bánh cám, một ngọn giáo gỗ, từng đồng tiền còm mà sinh tồn và từng bước gây dựng thế lực giữa thời loạn.

## Writer

- **SI đang dùng:** [`gemini/si-claude.txt`](gemini/si-claude.txt) (tiếng Trung, văn phong 《乱世荒年》 điều chỉnh bối cảnh lịch sử giá không/lưu dân), dán tại [`gemini/si-dan-gemini.txt`](gemini/si-dan-gemini.txt).
- **Mô hình làm việc:** **Writer-driven & State-kept**:
  - **Không cần bible:** Bỏ qua hoàn toàn việc tạo và duy trì các file bible cồng kềnh.
  - **Nội dung để Writer quyết:** Writer toàn quyền sáng tạo tên nhân vật, tình huống, hành động, thoại và diễn biến.
  - **Agent giữ dữ liệu bằng State:** Quản lý liên tục [`handoff/state.json`](handoff/state.json) và [`handoff/state.md`](handoff/state.md) (lương thực, vũ khí, điểm kỹ nghệ, deadline, các sự kiện đã kể), tạo Brief nạp dữ liệu State cho Writer và cập nhật State sau mỗi đoạn.

## Trạng thái (nhánh luu-dan)

| Đoạn | Prompt | Bản thảo | Review | Trạng thái |
|---|---|---|---|---|
| 001 | [`briefs/doan-001.md`](briefs/doan-001.md) | ⏳ Chờ chạy Writer | — | ⏳ Sẵn sàng chạy |
