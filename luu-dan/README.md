# Lưu Dân (tên tạm)

> Thể loại: Lịch sử giá không · Quân lưu dân loạn thế (kiểu Khăn Vàng) · Bảng kỹ nghệ thuần thục. Quy trình: Writer-driven & State-kept.

**Logline:** Thời loạn thế lịch sử giá không, triều đình mục nát, nghĩa quân "Bình Thiên Đại tướng quân" cuốn theo biển người đói khát. Trần Hòa (người hiện đại) xuyên không thành thiếu niên lưu dân mười sáu tuổi gầy trơ xương, dựa vào đầu óc sắc sảo và bảng kỹ nghệ chỉ mình nhìn thấy, từ một mẩu bánh cám, một ngọn giáo gỗ hòe tự gọt nhọn, từng bước chém giết thoát hiểm, đoạt ngựa đoạt cung, gây dựng thế lực sinh tồn và quật khởi giữa thời loạn.

## Writer

- **SI đang dùng:** [`gemini/si-claude.txt`](gemini/si-claude.txt) (tiếng Trung, văn phong 《乱世荒年》 điều chỉnh bối cảnh lịch sử giá không/quân lưu dân), dán tại [`gemini/si-dan-gemini.txt`](gemini/si-dan-gemini.txt).
- **Mô hình làm việc:** **Writer-driven & State-kept**:
  - **Không cần bible:** Bỏ qua hoàn toàn việc tạo và duy trì các file bible cồng kềnh.
  - **Nội dung để Writer quyết:** Writer toàn quyền sáng tạo tình huống, hành động, thoại và diễn biến.
  - **Agent giữ dữ liệu bằng State:** Quản lý liên tục [`handoff/state.json`](handoff/state.json) và [`handoff/state.md`](handoff/state.md) (lương thực, vũ khí, điểm kỹ nghệ, biên chế, quan hệ xã hội), tạo Brief nạp dữ liệu State cho Writer và cập nhật State sau mỗi đoạn.

## Trạng thái (nhánh luu-dan)

| Đoạn | Prompt | Bản thảo | Review | Trạng thái |
|---|---|---|---|---|
| 001 | [`briefs/doan-001.md`](briefs/doan-001.md) | [`chapters/doan-001.md`](chapters/doan-001.md) (5.141 字, XANH) | Thức tỉnh MC Trần Hòa, kỹ nghệ 削木/扎枪, tam thúc Trần Tam Trụ | ✅ Đã chốt State |
| 002 | [`briefs/doan-002.md`](briefs/doan-002.md) | [`chapters/doan-002.md`](chapters/doan-002.md) (5.132 字, XANH) | Đâm thủng da trâu lập uy, nhận chức Trường thương thủ, quân lệnh trạng | ✅ Đã chốt State |
| 003 | [`briefs/doan-003.md`](briefs/doan-003.md) | [`chapters/doan-003.md`](chapters/doan-003.md) (4.957 字, XANH) | Giúp quân nhu sửa xe, đổi gỗ du đẽo giáo thứ 2, 【削木 52/100】, cướp vây | ✅ Đã chốt State |
| 004 | [`briefs/doan-004.md`](briefs/doan-004.md) | [`chapters/doan-004.md`](chapters/doan-004.md) (3.949 字, XANH) | Đâm chết 2 tên cướp, tống tiền Vương Lại Tử, cứu Tam thúc, nhổ trại Hắc Phong Khẩu | ✅ Đã chốt State |
| 005 | [`briefs/doan-005.md`](briefs/doan-005.md) | [`chapters/doan-005.md`](chapters/doan-005.md) (5.199 字, XANH) | Hỗn chiến đêm phá lũy, 【扎枪】 đột phá Thuần thục, phục binh kỵ binh xuất hiện | ✅ Đã chốt State |
| 006 | [`briefs/doan-006.md`](briefs/doan-006.md) | [`chapters/doan-006.md`](chapters/doan-006.md) (5.360 字, XANH) | Phục kích giết 2 thiết kỵ, thu phục Mã Đao Kiểm, đoạt chiến mã/cung tên/bạc vụn | ✅ Đã chốt State |
