# NHIỆM VỤ THIẾT KẾ BƯỚC 1: KHỞI TẠO NỀN MÓNG DỰ ÁN TIỂU THUYẾT MANGA MỚI TỪ CON SỐ 0

Gửi: **Argon (Master Architect / Story Co-founder)**  
Từ: **Đội ngũ dự án Novel**  
Mục đích: **Khởi động dự án mới từ con số 0. Phân tích nền móng và đề xuất phương án kiến trúc bước đầu tiên.**

---

### I. BỐI CẢNH & VAI TRÒ
- **Vai trò của bạn (Argon):** Master Architect & Story Co-founder — chịu trách nhiệm định hình tầm nhìn, phân tích bối cảnh, thiết kế cơ chế và kiến trúc truyện.
- **Tác giả (User):** Người quyết định cuối cùng, phê duyệt các phương án lớn.
- **Agent cục bộ:** Kỹ sư thực thi (quản lý file, chạy script, tuân thủ kỷ luật).

**Lưu ý quan trọng từ Tác giả:**
Tất cả các bản nháp thử nghiệm và các giả định nhân vật/cốt truyện tự phát trước đây (như tên nhân vật cũ, tác phẩm zombie, chi tiết kiếp trước...) **chưa từng được Tác giả phê duyệt và đã được loại bỏ hoàn toàn về kho lưu trữ**. Dự án hiện tại bắt đầu lại từ vạch xuất phát (Bước 1). Chúng tôi cam kết không đưa bất kỳ định kiến, ý kiến cá nhân hay kịch bản gài sẵn nào vào đây để bạn hoàn toàn tự do phân tích theo góc nhìn chuyên môn khách quan nhất.

---

### II. CÁC THÔNG SỐ CỐ ĐỊNH DUY NHẤT ĐÃ ĐƯỢC TÁC GIẢ DUYỆT
Dưới đây là toàn bộ những dữ kiện nền tảng đã được chốt:
1. **Thể loại:** Tiểu thuyết mạng tiếng Trung viết về đề tài sáng tác Manga tại Nhật Bản (Văn nghệ đô thị / Khởi nghiệp sáng tạo truyện tranh / Đời sống nghề nghiệp).
2. **Bộ sách tham chiếu kỹ thuật (Benchmark):** `我在泡沫东京画漫画` (Tokyo Bong bóng vẽ manga) — tác phẩm tham chiếu về phong cách tả thực, nhịp điệu sinh hoạt và không khí giới manga Nhật Bản. Bối cảnh gốc của bộ mẫu là năm 1994 (thời kỳ sau khi bong bóng kinh tế nổ).
3. **Định hướng bối cảnh thời gian:** Tác giả đã chốt hướng đi: Giữ tinh thần tả thực như bộ mẫu, nhưng **đẩy năm bối cảnh tiến lên** (khoảng thời kỳ cuối thập niên 90 hoặc đầu thập niên 2000 / Kỷ nguyên thiên niên kỷ).
4. **Nhân vật chính (MC):** Kiếp trước là **người Nhật** (không phải người nước ngoài xuyên việt).
5. **Quy ước tên riêng:** Tên người và địa danh Nhật Bản viết bằng Romaji (chữ Latin) trong chính văn tiếng Trung, prompt và state.
6. **Ngôn ngữ sản xuất:** Prompt và brief trao đổi bằng tiếng Việt; chính văn tiểu thuyết viết bằng tiếng Trung.

---

### III. YÊU CẦU PHÂN TÍCH BƯỚC 1 TỪ ARGON
Với tư cách là Kiến trúc sư trưởng của dự án, xin bạn phân tích sâu sắc các khía cạnh sau để trình Tác giả xem xét và lựa chọn:

#### 1. Khảo sát & Đề xuất Mốc Thời Gian (Timeline Analysis)
- Khi đẩy mốc thời gian tiến lên so với bộ mẫu (1994), hãy so sánh các mốc khả thi trong lịch sử manga Nhật Bản (ví dụ: 1997–1998, 1999–2000, 2001–2002...).
- Phân tích bối cảnh ngành truyện tranh tại các mốc đó:
  + Tình hình các tuần san lớn (Shonen Jump, Shonen Magazine, Shonen Sunday, Young Jump... đang trong giai đoạn nào: hậu Dragon Ball/Slam Dunk, sự trỗi dậy của thế hệ mới One Piece/Naruto, hay khủng hoảng tạp chí?).
  + Tình hình kinh tế - xã hội Nhật Bản ảnh hưởng thế nào đến túi tiền độc giả và đời sống họa sĩ trẻ?
  + Theo bạn, mốc năm cụ thể nào là lý tưởng nhất để tạo ra xung đột, cơ hội và ma sát thực tế nhất cho một người mới bước vào nghề?

#### 2. Xung đột cốt lõi & Động lực xuất phát điểm (Core Dilemma & Motive)
- Phân tích động lực ban đầu của nhân vật chính:
  + Áp lực sinh tồn (nợ nần, tiền thuê nhà, chi phí vật tư) nên ở mức độ nào để câu chuyện có sức nặng đời thường nhưng không bị bi kịch hóa quá mức?
  + Mâu thuẫn giữa "vẽ để kiếm cơm qua ngày" và "khát vọng sáng tạo / bước lên tạp chí lớn".
- **Hợp đồng độc giả (Reader Contract):** Độc giả dòng truyện này mong đợi điểm sướng (爽点 - Payoff) cốt lõi nào? Làm sao cân bằng giữa quy trình vẽ truyện chuyên nghiệp (tả thực) và tính sảng khoái của tiểu thuyết mạng?

#### 3. Định hình Nhân vật chính & Cơ chế Lợi thế (Protagonist & Advantage Mechanics)
- **Thân phận xuất phát:** Đề xuất 2–3 phương án xuất phát điểm cho nhân vật chính (VD: thợ vẽ trợ lý thâm niên, tác giả doujinshi tự do, cựu sinh viên mỹ thuật...) kèm ưu/nhược điểm tự sự của từng phương án.
- **Cơ chế Lợi thế ("Bàn tay vàng"):**
  + Làm sao thiết kế lợi thế của MC (dù là ký ức tương lai, năng lực chuyên môn hay cơ chế đặc thù) sao cho vừa tạo ra ưu thế cạnh tranh vượt trội, vừa giữ được sự tôn trọng với nghề vẽ, tránh biến câu chuyện thành việc "sao chép máy móc vô hồn"?

#### 4. Chiến lược Tác phẩm Khởi đầu (Debut Work Strategy)
- Tiêu chí để chọn tác phẩm đầu tay cho nhân vật chính:
  + Nên bắt đầu bằng thể loại gì (One-shot dự thi giải tân binh, truyện ngắn đăng tạp chí thanh niên, hay hướng đi nào khác)?
  + Đặc điểm của một tác phẩm mở màn đủ sức gây ấn tượng mạnh với biên tập viên và độc giả trong bối cảnh thời đại đó.

#### 5. Lộ trình triển khai kỹ thuật tiếp theo
- Sau khi Tác giả duyệt phương án bước 1, quy trình tiếp theo cần làm những gì để đưa dự án vào sản xuất theo đúng Kiến trúc 3 tầng (SI tiệt trùng -> JIT Passive State -> Kinetic Scene Brief đoạn 001)?

Xin hãy trình bày phân tích chi tiết, khách quan, mang tính cấu trúc cao để Tác giả có thể đánh giá và đưa ra quyết định sáng suốt nhất.
