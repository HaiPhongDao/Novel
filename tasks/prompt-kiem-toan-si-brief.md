Bạn là **Kiến trúc sư hệ thống & Đồng sáng lập (Architect / Co-founder)** của xưởng viết tiểu thuyết AI.
Tác giả (người dùng) yêu cầu: **DỪNG VIỆC LẬP DÀN Ý CỐT TRUYỆN.**
Nhiệm vụ trọng tâm hiện tại của bạn là: **KIỂM TOÁN, TÌM RA THIẾU SÓT VÀ CẢI TIẾN TOÀN BỘ PHƯƠNG PHÁP LUẬN TẠO SI (System Instruction), PROMPT VÀ BRIEF.**

Xưởng hiện đang vận hành theo mô hình:
- **Agent (Co-founder)**: Quản lý canon, tạo SI, lập Brief tiếng Việt, quản lý State.
- **Writer (Gemini 3.8 Flash, Thinking High)**: Viết chính văn tiếng Trung theo từng đoạn (~2.000 chữ).

---
### I. HIỆN TRẠNG & CÁC VẤN ĐỀ NHỨC NHỐI CỦA XƯỞNG

#### 1. Khung System Instruction hiện tại (`writer/SI-template`):
- Gồm: ROLE -> FIXED CONVENTIONS -> PART 1 STYLE (NARRATION, MOMENTS) -> 8 ANCHORS.
- Hướng dẫn Writer: "One beat, one paragraph", "Description through nouns, verbs and numbers", "Narration stays with POV character".
- **Vấn đề đã gặp**:
  + Luật nhịp bị model hiểu nhầm thành "luật đếm" (khi đọc thinking thấy model tự kiểm "one-beat-per-paragraph" và "single sentence" -> sinh ra câu cụt, thoại cụt hoặc cố ý kéo dài câu để đua đủ số chữ).
  + Anchor mẫu nếu không làm sạch thì Writer học luôn tật của anchor (bộ ba phủ định, nhãn ngữ điệu sáo rỗng).
  + Thiếu cơ chế kiềm chế xuất thông tin (Information Suppression): SI chưa có điều khoản nào đủ mạnh để cấm Writer "tự ý giải thích bối cảnh/kiếp trước/bàn tay vàng" khi chưa có lệnh trong Brief.

#### 2. Khung Quản lý State hiện tại (`handoff/state.json` hoặc `state.md`):
- Chứa: `scene_bridge` (thời gian, địa điểm, nhân vật có mặt, last beat), `already_told`, `ledger` (tiền bạc, nợ nần), `characters`, `setting_cards`.
- **Vấn đề chí mạng (State Dumping / Backstory Leak)**:
  + Khi mở session mới, ta nạp State vào ngữ cảnh của Writer.
  + Writer thấy trong State có thông tin kiếp trước (Kudo Shun, 12 năm trợ lý, chết trên bàn vẽ) và bàn tay vàng (Phân cảnh khố) -> Ngay đoạn 001, dù Brief chỉ yêu cầu "tính tiền thưởng so với nợ và lương ở quầy thu ngân", Writer đã tự tiện viết nguyên một tràng 757 chữ xả sạch toàn bộ kiếp trước và bàn tay vàng!
  + Writer coi mọi thứ trong State là "thứ tôi cần khoe ra trong bài viết", thay vì hiểu State là "bộ nhớ ngầm chỉ để tham chiếu chống viết sai".

#### 3. Khung Brief / Prompt hiện tại (`AGENT.md` Mục 4):
- Đang giằng co giữa 2 mẫu:
  + **Mẫu A (Prompt ngắn)**: 3-6 câu văn xuôi phương hướng + danh sách số liệu. Ưu điểm: Văn tự nhiên, ít cứng. Nhược điểm: Quá thưa, Writer dễ tự ý lôi dữ liệu ngầm ra viết hoặc tự bịa tình tiết.
  + **Mẫu B (Prompt đầy đủ)**: Thiết lập + Tiền tình + Chuyện xảy ra + Điểm bắt buộc + Tự do sáng tạo. Ưu điểm: Ràng buộc chặt. Nhược điểm: Writer chạy theo checklist, nhân vật biến thành robot, văn phong gượng gạo.
- **Vấn đề về Thoại**:
  + Khi Brief giao kịch bản tranh luận hoặc gắn nhãn tính cách ("thẳng thắn", "lạnh lùng"), thoại biến thành màn thuyết trình báo cáo.
  + Khi không giao kịch bản, thoại lại thiếu thông tin, cụt lủn và không mang tải trọng cốt truyện.
- **Cạm bẫy phủ định**:
  + Khi Brief viết "không được viết kiếp trước, không được nhắc bàn tay vàng", hiện tượng Pink Elephant xảy ra: model càng dễ bị mồi ngược và nhắc tới thứ bị cấm.

---
### II. NHIỆM VỤ DÀNH CHO BẠN (ARGON):
Hãy suy nghĩ sâu (Thinking High) và thực hiện một bản **Kiểm toán Kỹ thuật & Đề xuất Cải tiến toàn diện** cho 3 khâu: SI, Brief/Prompt, và Quản lý State.

#### 1. Phân tích nguyên nhân gốc rễ (Root Cause Analysis):
- Tại sao cơ chế kết hợp giữa Agent (quản lý bối cảnh) và Writer Gemini (sinh văn) lại liên tục gặp lỗi rò rỉ State, văn chạy checklist hoặc thoại thuyết trình?
- Bản chất kiến trúc Prompting và cơ chế Attention của LLM trong quy trình này đang bị nghẽn ở đâu?

#### 2. Cải tiến Khâu System Instruction (SI):
- Làm thế nào để định hình giọng văn (voice) và nhịp điệu của truyện mẫu mà KHÔNG biến thành các "luật đếm" gây tật câu cụt?
- Cần bổ sung vào SI điều khoản kỷ luật xuất thông tin (Output Discipline / Information Boundary) như thế nào để Writer hiểu nguyên tắc: *"Chỉ viết những gì đang diễn ra trong phạm vi thời gian của cảnh, tuyệt đối không được tự ý tóm tắt lý lịch hay xả dữ liệu kiến thức ngầm"*?
- Tiêu chuẩn tuyển chọn và làm sạch Anchor mẫu (Anchor Hygiene) để Writer học đúng kỹ thuật mà không nhiễm tật văn của tác giả gốc.

#### 3. Tái cấu trúc Khâu Quản lý State (State Architecture):
- Làm thế nào để giải quyết dứt điểm lỗi "State Dumping"?
- Hãy thiết kế cơ chế phân tách rõ ràng giữa:
  + **Passive State (Dữ liệu nền / Hộp đen)**: Giúp Writer không viết sai tên, sai số tiền, sai luật thế giới, nhưng bị khóa kín, cấm không được chuyển hóa thành lời kể.
  + **Active Scene Scope (Phạm vi cảnh)**: Chỉ cấp đúng những thông tin và xung đột được phép diễn ra trong đoạn này.
- Nên dùng format nào (JSON hay Markdown siêu nén) và kỹ thuật dán nhãn ngữ cảnh ra sao để Writer tuân thủ nghiêm ngặt?

#### 4. Chuẩn hóa Mẫu Brief Mới (Next-Gen Brief Template):
- Đề xuất một **Mẫu Brief Mới** dung hòa và khắc phục triệt để nhược điểm của cả Mẫu A lẫn Mẫu B:
  + Cấu trúc các trường thông tin chuẩn xác.
  + Kỹ thuật giao thoại tự nhiên (giao động cơ, mục tiêu thực tế và góc nhìn của nhân vật thay vì giao kịch bản tranh luận).
  + Kỹ thuật viết Ranh giới an toàn (Safe Boundaries / Negative Constraints) bằng ngôn ngữ khẳng định, tránh bẫy mồi ngược.

#### 5. Bảng ma trận phân quyền 3 tầng (The 3-Tier Architecture):
- Định nghĩa rành mạch:
  + **Tầng 1 - SI**: Kiểm soát những gì? (Không chứa gì?)
  + **Tầng 2 - State**: Kiểm soát những gì? (Không chứa gì?)
  + **Tầng 3 - Brief**: Kiểm soát những gì? (Không chứa gì?)
- Quy trình phối hợp chuẩn giữa 3 tầng để khi đưa vào vận hành thực tế, Writer viết đoạn nào chắc đoạn đó.
