# Lưu Dân (tên tạm)

> Thể loại: Cổ đại · Lịch sử giá không · Quân lưu dân Đại Bình Quân (kiểu Khăn Vàng) · Bảng kỹ nghệ thuần thục. Quy trình: Writer-driven & State-kept.

**Logline:** Thời loạn thế lịch sử giá không, triều đình thối nát, quân khởi nghĩa "Đại Bình Quân" cuốn theo biển người đói khát. Trần Viễn (người hiện đại) xuyên không thành thiếu niên lưu dân mười sáu tuổi gầy trơ xương, dựa vào đầu óc sắc sảo và bảng kỹ nghệ chỉ mình nhìn thấy, từ một mẩu bánh cám, một cọc gỗ tạp mài nhọn, từng bước sinh tồn và quật khởi giữa thời loạn.

## Writer

- **SI đang dùng:** [`gemini/si-claude.txt`](gemini/si-claude.txt) (tiếng Trung, văn phong 《乱世荒年》 điều chỉnh bối cảnh lịch sử giá không/quân lưu dân), dán tại [`gemini/si-dan-gemini.txt`](gemini/si-dan-gemini.txt).
- **Mô hình làm việc:** **Writer-driven & State-kept**:
  - **Không cần bible:** Bỏ qua hoàn toàn việc tạo và duy trì các file bible cồng kềnh.
  - **Nội dung để Writer quyết 100%:** Brief chỉ gồm State và câu "Viết tiếp đoạn tiếp theo". Không mớm việc, không vẽ kịch bản, không chỉ cách viết.
  - **Agent giữ dữ liệu bằng State:** Quản lý liên tục [`handoff/state.json`](handoff/state.json) và [`handoff/state.md`](handoff/state.md) để bảo đảm sự nhất quán về số liệu, vật phẩm và chỉ số kỹ nghệ.

## Trạng thái (nhánh luu-dan)

| Đoạn | Prompt | Bản thảo | Review | Trạng thái |
|---|---|---|---|---|
| 001 | [`briefs/doan-001.md`](briefs/doan-001.md) (tối giản 3 dòng) | [`chapters/doan-001.md`](chapters/doan-001.md) (4.334 字, XANH) | MC Trần Viễn (16 tuổi), thức tỉnh 【削木 5/100】, lệnh công phá Hắc Sơn Bảo | ✅ Đã chốt State |
| 002 | [`briefs/doan-002.md`](briefs/doan-002.md) (chỉ State + Viết tiếp) | ⏳ Chờ chạy Writer | — | ⏳ Sẵn sàng chạy |
