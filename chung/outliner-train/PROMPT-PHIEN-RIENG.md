# Prompt mở phiên "truyện riêng" (kiểm Outliner tự tạo brief, không có chương mẫu để chép)

Khác `PROMPT-PHIEN-MOI.md`: không có chương gốc, không có bible. Brief sinh ra từ tiền đề của Tác giả. Dán nguyên văn, điền tiền đề ở cuối. Mở phiên với thư mục làm việc `D:\ClaudeCode\Novel`. Trạng thái nằm ở `chung/outliner-train/rieng/BAN-GIAO.md` (phiên đầu tự tạo).

```
Bạn là Agent Outliner thử việc cho repo Novel (D:\ClaudeCode\Novel). Trả lời tôi bằng tiếng Việt, ngắn.

Mục đích: kiểm bạn TỰ TẠO được brief cho Writer (Gemini, SI đóng băng) từ tiền đề truyện riêng của tôi, không có chương gốc để chép. Truyện này KHÔNG liên quan bộ mẫu 泡沫东京 của các phiên trước. Chưa tạo bible. Bắt đầu ngay; chỉ hỏi tôi khi cần một quyết định của tôi.

1. Đọc đúng ba thứ, theo thứ tự (đừng đọc SKILL.md, README.md, nghien-cuu-outliner.md; AGENT.md đã tự nạp): chung/outliner-train/QUY-TAC.md → MAU-BRIEF-Q.md → 15 dòng cuối NHAT-KY.md. Nếu chung/outliner-train/rieng/BAN-GIAO.md đã có, đọc nó TRƯỚC (trạng thái nằm ở đó). KHÔNG đọc ch09/, ch22/, ch30/, ch45/, ch54/ và file .txt bộ mẫu: đó là nội dung bộ mẫu, đọc là chép.
2. Nạp get_usage bằng ToolSearch "select:mcp__ccd_session_mgmt__get_usage", gọi đầu phiên và mỗi ~60 lượt. Context > 250k token, hoặc xong một cảnh: dừng, cập nhật bàn giao, nói tôi MỘT dòng để mở phiên mới.
3. Phiên đầu: tạo chung/outliner-train/rieng/<ten-truyen>/ gồm tien-de.md (chép tiền đề dưới đây), so.md (≤ 15 dòng: tên người viết Latin, xưng hô, 3–5 sự thật cố định; không bible), ke-hoach.md (3 cảnh, mỗi cảnh ≤ 5 dòng: ai muốn gì, chuyện lật, điều chỉ lộ ở cuối, người đọc mang gì ra khỏi cảnh). Ba cảnh khác loại nhau (một cảnh hai người có điều giấu, một cảnh một người một mình, một cảnh ≥ 3 người). Mỗi phiên làm MỘT cảnh, theo ke-hoach.md và rieng/BAN-GIAO.md.
4. Một cảnh, theo thứ tự:
   a. canh-N/thuoc.md — thước chấm của chính bạn, viết TRƯỚC khi có bản Writer: các ý bắt buộc (BB), nội tâm cần có (NT: ai nghĩ gì, ở đâu), điều không được xuất hiện (cơ chế, số liệu, tên ngoài kế hoạch), điểm dừng.
   b. canh-N/brief.md — theo khung MAU-BRIEF-Q, thêm mục Nội tâm dạng RÚT GỌN (QUY-TAC Q13): mỗi chỗ một câu nội dung + dạng (dòng ngắn, tự hỏi…) + vị trí + "chỉ trong đầu, không nói ra"; không viết sẵn lời văn. Điều then chốt ghi bằng câu, kèm lời đáp của người nghe (Q11, Q12). Không chép nguyên một câu nào từ MAU-BRIEF-Q.md ngoài tên mục.
   c. canh-N/kiem-truoc.md — tự kiểm 6 câu, câu nào sai thì viết lại brief trước khi chạy: (1) mỗi chi tiết trong brief lấy được từ tiền đề/kế hoạch, không từ bộ mẫu hay khung; (2) có mục Nội tâm cho từng người có mặt, mỗi chỗ đủ nội dung/dạng/vị trí; (3) điều chỉ lộ ở cuối khai riêng, ngoài hồ sơ; (4) điều thuộc cảnh sau chỉ gọi tên; (5) điểm dừng nêu bằng sự việc hoặc câu cụ thể; (6) không có nhãn trần ("lý do an toàn", "mắng") ở chỗ cần nội dung. Chạy thêm grep brief tìm Akiyama|Kurokawa|Okada|Tokyo|漫画|连载|未麻|上杉: phải rỗng.
   d. Chạy Writer 1 lần (jobs.json: si = chung/outliner-train/si-dong-bang.txt, prompt, out = canh-N/v1.md, think_out = canh-N/think-v1.md).
   e. canh-N/cham.md — đối chiếu thước, rồi ĐỌC TAY: ý đủ/thiếu; nội tâm có không (trích 2–3 dòng); chi tiết Writer tự bịa (số, cơ chế, tên); có tên bộ mẫu lọt vào không (anchor SI). Kết luận ghi nhãn n/m cảnh, GIẢ THUYẾT.

Luật cứng:
- SI đóng băng. Mỗi lần chỉ đổi brief. Mỗi brief chạy 1 lần.
- Tự viết brief trong phiên chính, không giao agent con. Agent con chỉ để đọc/khoanh. Gọi Opus (Agent, model: opus) chỉ khi đã thử ≥ 2 cách mà chưa xong: brief ≤ 40 dòng, báo cáo ≤ 200 từ.
- Chạy Writer ở nền: python tools/aistudio_run.py --batch <jobs.json> --timeout 22 > <log> 2>&1 &. Chờ bằng MỘT vòng for … ls file (không pgrep, không Monitor, không đáp từng thông báo nền). Không đọc tools/.aistudio_state.json. Không xem ảnh.
- Không sửa SKILL.md, AGENT.md, SI.

Cuối phiên: ghi NHAT-KY (≤ 6 dòng, nhãn ĐÃ CHẠY / CHƯA KIỂM), cập nhật QUY-TAC (n/m), tạo/viết lại rieng/BAN-GIAO.md (mục 0 trạng thái, "Làm tiếp"). Rồi commit + push lên nhánh hiện tại các file tôi cần đọc (brief, bản Writer, cham, thuoc, kiem-truoc, tien-de, ke-hoach, QUY-TAC, NHAT-KY, BAN-GIAO; KHÔNG think-*.md, run-*.log). Báo tôi ≤ 10 dòng, kèm LINK GitHub (https://github.com/HaiPhongDao/Novel/blob/<nhánh>/<đường dẫn>; nhánh lấy bằng git branch --show-current), không gửi đường dẫn máy: tôi đọc trên điện thoại.

TIỀN ĐỀ (Tác giả dán 3–5 dòng: nhân vật chính, bối cảnh, mâu thuẫn; nếu còn dòng dưới thì hỏi tôi đúng một câu "tiền đề?"):
<<DÁN TIỀN ĐỀ Ở ĐÂY>>
```
