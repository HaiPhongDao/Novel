# YÊU CẦU ARGON: XÂY DỰNG TOÀN DIỆN SYSTEM INSTRUCTION (SI) VÀ PROMPT BRIEF ĐOẠN 001 & 002

Gửi: **Argon (Master Architect / Story Co-founder)**  
Từ: **Đội ngũ dự án Novel**  
Ý kiến chỉ đạo từ Tác giả: **Duyệt định hướng phân tích Bước 1 của Argon. Yêu cầu Argon trực tiếp khởi tạo bản System Instruction (SI) hoàn chỉnh và soạn thảo Prompt Brief cho Đoạn 001 và Đoạn 002.**

---

### YÊU CẦU CỤ THỂ CẦN ARGON XUẤT RA:

#### HẠNG MỤC 1: BẢN SYSTEM INSTRUCTION (SI) CHÍNH THỨC
Dựa trên phong cách tả thực của bộ mẫu `我在泡沫东京画漫画` và bộ quy chuẩn kỹ thuật v5 vừa nâng cấp (xóa bỏ luật đếm câu cơ học, triệt tiêu rò rỉ State):
1. **ROLE & REGISTER:** Định vị giọng văn tiếng Trung (đời thường, chân thực, nhịp điệu nhà nghề, tự nhiên).
2. **FIXED CONVENTIONS:** Quy tắc tên riêng Romaji, dấu câu.
3. **STRICT INFORMATION BOUNDARY (ZERO EXPOSITION RULE):** Khóa góc nhìn hiện tại, cấm tóm tắt tiểu sử/kiếp trước cho độc giả, khóa băng thông nhận thức của MC vào tác vụ trước mắt.
4. **STYLE PRINCIPLES (Camera Focus Unit):**
   - Thay thế hoàn toàn "One beat, one paragraph" bằng cơ chế ngắt đoạn theo sự dịch chuyển trọng tâm chú ý của Camera (*Camera Focus Shift*).
   - Tả thực qua danh từ, động từ, con số vật lý (tiền bạc, dụng cụ, kích thước).
5. **BỘ ANCHORS TIỆT TRÙNG (Anchor Hygiene Protocol):**
   - Trích xuất và tiệt trùng các đoạn văn mẫu tiếng Trung tiêu biểu (từ phong cách bộ mẫu): lọc sạch câu mở đầu tóm tắt thiết lập, lọc sạch cấu trúc đối xứng giả tạo (`不是A，而是B`), lọc sạch nhãn thoại sáo rỗng (`冷冷地说`).
   - Phân bổ anchor theo vi thao tác (thao tác nghề nghiệp, tính toán chi phí, đối thoại va chạm đời thường, chuyển cảnh).

---

#### HẠNG MỤC 2: GÓI PROMPT BRIEF ĐOẠN 001 (KINETIC SCENE BRIEF)
Áp dụng Kiến trúc 3 tầng để Writer (~2000 chữ tiếng Trung) viết không bị State Dumping và không bị đói dung lượng:
1. `<read_only_ledger access="verify_only" narrate="false">`:
   - Bảng số liệu tĩnh: Tên nhân vật (Romaji), thân phận, vị trí hiện tại, bảng cân đối tài chính chi tiết (tiền thuê nhà đến hạn, tiền giấy manuscript, tiền mua screentone, tiền ăn...).
   - Tuyệt đối không chứa câu văn tự sự kích thích mô hình chép lại.
2. `<active_scene_brief target_length="2000_chars">`:
   - **Camera & Time Window:** Căn phòng trọ chật chội ở Tokyo năm 1999, khung thời gian 10–15 phút liên tục trước bàn vẽ.
   - **Props & Physical Inventory (Đạo cụ bắt buộc):** Bút G-pen, lọ mực, dao trổ dán screentone, tờ hóa đơn tiền nhà/hóa đơn vật tư, tập bản thảo vẽ dở.
   - **3 Kinetic Beats:** Phóng đại độ phân giải thao tác vật lý (kiểm tra nét vẽ, tính toán chi phí thâm hụt từng đồng, đấu tranh giữa việc vẽ gia công mệt nhoài và việc dồn sức cho bản thảo dự thi).
   - **Hard Camera Cut:** Điểm dừng vật lý dứt khoát kết thúc đoạn 001.
3. **Pre-Flight Directive:** Câu chỉ thị ngắn khóa luồng Thinking của Writer.

---

#### HẠNG MỤC 3: GÓI PROMPT BRIEF ĐOẠN 002 (KINETIC SCENE BRIEF)
Tiếp nối liền mạch từ điểm dừng của Đoạn 001:
1. `<read_only_ledger>` cập nhật: Trạng thái tiếp nối, những gì đã xuất hiện ở đoạn 001 (`already_told`), con số cần giữ nhất quán.
2. `<active_scene_brief target_length="2000_chars">`:
   - Cảnh tiếp theo (ví dụ: cuộc gặp gỡ/giao tiếp đời thường, nộp bản thảo gia công, hoặc tương tác với bên ngoài để mở ra cơ hội giải thưởng tân binh).
   - Props, 3 Kinetic Beats và Hard Camera Cut cho đoạn 002.
3. **Pre-Flight Directive** cho đoạn 002.

Xin Argon xuất toàn bộ nội dung chi tiết để Agent có thể lưu vào hệ thống và tiến hành sản xuất ngay lập tức!
