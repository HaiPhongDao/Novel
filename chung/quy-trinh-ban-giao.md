# Chuyển session Writer — quy trình chung cho mọi truyện

Một session Writer chỉ viết **2 đoạn** (đoạn thứ 3 trong một session đã trôi giọng — `lanh-chua-chip/reviews/doan-005.md` lượt 1). Khi mở session mới, Writer không nhớ gì ngoài system instruction → phải nạp lại bằng **gói bàn giao**.

## Gói bàn giao gồm gì

Mỗi truyện giữ các file sau trong `<ten-truyen>/handoff/`:

| Phần | File | Mục đích |
|---|---|---|
| 1. Thẻ thiết lập cố định | `canon-card.md` | Nhân vật, bàn tay vàng, địa danh, xưng hô — chỉ những gì **đã lên trang** + luật cố định |
| 2. Tóm tắt đã viết | `story-so-far.md` | Diễn biến từng đoạn |
| 3. Trạng thái hiện tại | `state.md` | Đang ở đâu, ai biết gì, con số đang chạy, đồ vật/chi tiết đã xuất hiện, tuyến đang mở |
| 4. Mẫu giọng | `voice-anchor.md` | Trích nguyên văn vài khúc hay nhất đã duyệt. Agent thay khi có khúc tốt hơn |
| 5. Nguyên văn cuối đoạn gần nhất | `chapters/doan-XXX.md` (~900 ký tự cuối, tự lấy) | Nối mạch câu chữ và **giữ giọng** — tóm tắt không truyền được giọng, nguyên văn thì được |
| (tuỳ chọn) | `quiz.md` | Câu hỏi kiểm tra khi chỉ nạp gói mà chưa viết (`pack.md`). Không có thì dùng câu hỏi mặc định |

Ghép tự động:
- `python tools/build_pack.py <ten-truyen>` → `handoff/pack.md` (chỉ nạp gói, Writer trả lời quiz rồi chờ).
- `python tools/build_pack.py <ten-truyen> --prompt briefs/doan-XXX.md` → `handoff/session-start.md` = gói + prompt đoạn kế, Writer đọc rồi viết luôn. **Đây là cách mở session thường dùng.**

## Quy trình

**Sau mỗi đoạn đạt (Agent, lúc chốt):**
1. Thêm đoạn mới vào `story-so-far.md`; nén đoạn cũ (xem quy tắc giữ gói gọn).
2. Ghi đè `state.md` theo trạng thái cuối đoạn.
3. Chi tiết nào đã chốt thành canon → thêm vào `canon-card.md`.
4. Ghép lại `pack.md`. → Gói luôn sẵn sàng, chuyển session lúc nào cũng được.
5. Commit + push (`tools/chot_doan.py` làm cả bước 1–5 từ một file spec).

**Khi chuyển session:**
1. Mở chat mới, vẫn dùng system instruction của truyện.
2. Dán toàn bộ `session-start.md`. Writer đọc rồi viết luôn.
3. Agent review, ghi `handoff/sessions.md` (session nào viết đoạn nào, kết quả).

Cũng dùng đúng cách này khi **một đoạn bị hỏng**: Agent chuyển bản hỏng vào `archive/`, sửa prompt, ghép `session-start.md` tính tới đoạn trước đó → viết lại đoạn đó trong session mới. Không gửi prompt "viết lại" vào session cũ.

## Quy tắc giữ gói gọn

- `story-so-far.md`: **3 đoạn gần nhất** viết chi tiết (5–8 dòng/đoạn); đoạn cũ hơn nén còn 1–2 dòng; hết một arc thì gộp thành một đoạn "Arc N".
- `state.md` là ảnh chụp, **ghi đè** chứ không cộng dồn. Đồ vật/chi tiết không còn dùng thì xoá khỏi state (vẫn còn trong `bible/`).
- Mục tiêu: `pack.md` dưới ~15.000 ký tự.
- **Con số trong state là số đúng do Agent tính**, kể cả khi chính văn tính sai — ghi rõ khung (vd. "đủ X ngày / còn Y ngày tới mốc Z"), để Writer không lặp phép tính sai.
- **Không đưa bí mật tương lai vào gói** (kẻ chủ mưu, quá khứ nhân vật chưa lộ…). Writer biết điều gì thì sẽ có xu hướng viết điều đó ra. Bí mật chỉ vào prompt của đúng đoạn cần dùng.
- Viết khẳng định, giống prompt: mô tả cái *có*, không liệt kê cái cấm.

## Vì sao Agent giữ gói, không để Writer tự tóm tắt
Writer tự tóm tắt sẽ trôi dần: quên quyết định của Tác giả, giữ lại chi tiết sai đã bị sửa, bỏ sót con số. Agent đọc mọi đoạn khi review và đối chiếu với `bible/`, nên gói do Agent giữ luôn là bản đã kiểm.
