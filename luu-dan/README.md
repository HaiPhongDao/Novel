# Lưu Dân (tên tạm)

> Thể loại: Lịch sử giá không · Quân lưu dân loạn thế (kiểu Khăn Vàng) · Bảng kỹ nghệ thuần thục. Quy trình: Writer-driven & State-kept.

**Logline:** Thời loạn thế lịch sử giá không, triều đình mục nát, nghĩa quân "Bình Thiên Đại tướng quân" cuốn theo biển người đói khát. Trần Hòa (người hiện đại) xuyên không thành thiếu niên lưu dân mười sáu tuổi gầy trơ xương, dựa vào đầu óc sắc sảo và bảng kỹ nghệ chỉ mình nhìn thấy, từ một mẩu bánh cám, một ngọn giáo gỗ hòe tự gọt nhọn, từng bước thoát khỏi kiếp bia thịt, sinh tồn và quật khởi giữa thời loạn.

## Writer

- **SI đang dùng:** [`gemini/si-claude.txt`](gemini/si-claude.txt) (tiếng Trung, văn phong 《乱世荒年》 điều chỉnh bối cảnh lịch sử giá không/quân lưu dân), dán tại [`gemini/si-dan-gemini.txt`](gemini/si-dan-gemini.txt).
- **Mô hình làm việc:** **Writer-driven & State-kept**:
  - **Không cần bible:** Bỏ qua hoàn toàn việc tạo và duy trì các file bible cồng kềnh.
  - **Nội dung để Writer quyết:** Writer toàn quyền sáng tạo tình huống, hành động, thoại và diễn biến.
  - **Agent giữ dữ liệu bằng State:** Quản lý liên tục [`handoff/state.json`](handoff/state.json) và [`handoff/state.md`](handoff/state.md) (lương thực, vũ khí, điểm kỹ nghệ, biên chế, quan hệ xã hội), tạo Brief nạp dữ liệu State cho Writer và cập nhật State sau mỗi đoạn.

## Trạng thái (nhánh luu-dan)

| Đoạn | Prompt | Bản thảo | Review | Trạng thái |
|---|---|---|---|---|
| 001 | [`briefs/doan-001.md`](briefs/doan-001.md) (tối giản 3 dòng) | [`chapters/doan-001.md`](chapters/doan-001.md) (5.141 字, cổng XANH) | Đạt: MC Trần Hòa, kỹ nghệ 削木/扎枪, tam thúc Trần Tam Trụ, kẻ thù Vương Lại Tử | ✅ Đã chốt State sau 001 |
| 002 | [`briefs/doan-002.md`](briefs/doan-002.md) (State-brief) | ⏳ Chờ chạy Writer | — | ⏳ Sẵn sàng chạy |
