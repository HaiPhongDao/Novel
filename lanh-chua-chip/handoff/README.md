# Chuyển session Writer Gemini

Một session Gemini chỉ viết **2–3 đoạn**. Khi mở session mới, Gemini không nhớ gì ngoài system instruction → phải nạp lại bằng **gói bàn giao** (`pack.md`).

## Gói bàn giao gồm gì

| Phần | File nguồn | Mục đích |
|---|---|---|
| 1. Thẻ thiết lập cố định | `canon-card.md` | Nhân vật, bàn tay vàng, địa danh, xưng hô — chỉ những gì **đã lên trang** + luật cố định |
| 2. Tóm tắt đã viết | `story-so-far.md` | Diễn biến từng đoạn |
| 3. Trạng thái hiện tại | `state.md` | Đang ở đâu, ai biết gì, con số đang chạy, đồ vật/chi tiết đã xuất hiện, tuyến đang mở |
| 4. Nguyên văn cuối đoạn gần nhất | `chapters/doan-XXX.md` (~900 ký tự cuối) | Nối mạch câu chữ và **giữ giọng** — tóm tắt không truyền được giọng, nguyên văn thì được |

`pack.md` được ghép tự động: `python3 tools/build_pack.py lanh-chua-chip`; thêm `--prompt briefs/doan-XXX.md` để ra `outbox.md` (gói + prompt, dán một lần).

## Quy trình

**Sau mỗi đoạn (Agent, lúc review):**
1. Thêm đoạn mới vào `story-so-far.md`.
2. Ghi đè `state.md` theo trạng thái cuối đoạn.
3. Chi tiết nào đã chốt thành canon → thêm vào `canon-card.md`.
4. Ghép lại `pack.md`. → Gói luôn sẵn sàng, chuyển session lúc nào cũng được.

**Khi chuyển session (Tác giả):**
1. Mở session Gemini mới, vẫn dùng system instruction 文风.
2. Dán khối `▶ SESSION MỚI` Agent đưa (= `outbox.md`: gói bàn giao + prompt đoạn tiếp theo). Gemini đọc rồi viết luôn.
3. Mang chính văn về cho Agent như mọi vòng. Agent kiểm tra mạch/giọng khi review và ghi vào `sessions.md`.

## Quy tắc giữ gói gọn

- `story-so-far.md`: **3 đoạn gần nhất** viết chi tiết (5–8 dòng/đoạn); đoạn cũ hơn nén còn 1–2 dòng; hết một arc thì gộp thành một đoạn "Arc N".
- `state.md` là ảnh chụp, **ghi đè** chứ không cộng dồn. Đồ vật/chi tiết không còn dùng thì xoá khỏi state (vẫn còn trong `bible/`).
- Mục tiêu: `pack.md` dưới ~15.000 ký tự.
- **Không đưa bí mật tương lai vào gói** (kẻ chủ mưu, thứ trong rừng, quá khứ nhân vật chưa lộ…). Writer biết điều gì thì sẽ có xu hướng viết điều đó ra. Bí mật chỉ vào prompt của đúng đoạn cần dùng.
- Viết khẳng định, giống prompt: mô tả cái *có*, không liệt kê cái cấm.

## Vì sao Agent giữ gói, không để Gemini tự tóm tắt
Gemini tự tóm tắt sẽ trôi dần: quên quyết định của Tác giả, giữ lại chi tiết sai đã bị sửa, bỏ sót con số. Agent đọc mọi đoạn khi review và đối chiếu với `bible/`, nên gói do Agent giữ luôn là bản đã kiểm.
