# Agent tự chạy Writer trên Google AI Studio (qua Claude in Chrome)

Dùng khi Tác giả bảo Agent "tự động tạo truyện". Viết 22–23/10/2026 sau khi chạy `lanh-chua-chip` lượt 2, đoạn 003–015.

## Cài đặt mỗi session (chat mới)

- Trình duyệt: **Claude in Chrome** (Chrome, đã đăng nhập Google). Edge từng đứng ở trang đăng nhập Google.
- `https://aistudio.google.com/prompts/new_chat`
- Model **Gemini 3.8 Flash** · **Thinking level: High** · **tắt Grounding with Google Search**.
- System instructions: chọn bản đã lưu của truyện (tên ghi trong `<ten-truyen>/README.md`). Bản lưu nằm trong local storage của trình duyệt — mất thì dán lại từ file SI của truyện. Sau khi chọn, kiểm độ dài textarea `System instructions` khớp số ký tự của file (bỏ `\r`).
- Một chat = một session Writer = tối đa **2 đoạn**. Đoạn hỏng → chat mới.

## Đưa văn bản vào

1. `powershell -ExecutionPolicy Bypass -File tools/set_clip.ps1 <file>` (tự kiểm clipboard đã nhận).
2. Bấm vào ô `Enter a prompt` → `ctrl+v` → kiểm `textarea[aria-label="Enter a prompt"].value.length` khớp số ký tự set_clip báo.
3. Bấm nút **Run** (toạ độ hoặc `find` "Run button"). `ctrl+Enter` lúc ăn lúc không — không tin.

Mở session: dán `handoff/session-start.md`. Đoạn thứ 2 trong cùng session: dán thẳng `briefs/doan-XXX.md`.

## Chờ và lấy bản thảo ra

- Mỗi đoạn ~1,5–2 phút (thinking High). Còn chạy khi chưa thấy nút bắt đầu bằng `Run`. **Đừng** dò chữ "Stop" trong toàn trang — SI có chữ "Stop" nên khớp nhầm.
- AI Studio render lười: cuộn khung `ms-autoscroll-container` xuống đáy (gán `scrollTop = scrollHeight` vài lần, mỗi lần chờ 1 s) rồi mới đọc `innerText` của `ms-chat-turn` cuối.
- Bỏ đầu `edit/more_vert` và đuôi `thumb_up/thumb_down` khỏi `innerText`.
- `navigator.clipboard.writeText` bị treo. Cách chạy được: JS gán văn bản vào một `<textarea>` ẩn, `focus()` + `select()`, rồi gửi phím thật `ctrl+c` bằng công cụ trình duyệt.
- `powershell -ExecutionPolicy Bypass -File tools/save_clip.ps1 <truyện>/chapters/doan-XXX.md "<ghi chú session>" -ExpectLen <độ dài>` — từ chối lưu nếu clipboard bị thứ khác ghi đè. Đối số `-ExpectHead` không dùng được với chữ bắt đầu bằng ngoặc kép cong (PowerShell vỡ chuỗi).

## Sau khi lưu

Review (AGENT.md mục 5) → đạt thì `tools/chot_doan.py` (ghi sổ + commit + push); hỏng thì `archive/` + sửa prompt + `build_pack.py --prompt` + chat mới. Đóng tab Chrome khi xong đợt.

## Bẫy đã gặp

- Click chọn SI ngay sau khi trang vừa tải có lúc trượt → chờ 1 s giữa các bước, và luôn kiểm độ dài SI trước khi dán prompt.
- Chat mới mặc định Thinking `Medium`; Grounding đôi khi bật sẵn.
- Kết quả Writer thỉnh thoảng bị chặn "Prohibited content" (lượt Gemini 3.8 Flash, đoạn 003) → chạy lại ở chat mới.
