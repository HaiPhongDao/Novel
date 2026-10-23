# Chạy Writer bằng Gemini API (`tools/gemini_write.py`)

Thay cho copy-dán qua AI Studio: một lệnh gửi SI + prompt cho Gemini và ghi bản thảo thẳng vào `chapters/`. Writer chỉ thấy đúng SI, gói bàn giao và prompt — không đọc được repo.

## Cài một lần (Windows)

1. Cài **Git** và **Python 3** (khi cài Python, tick "Add python.exe to PATH").
2. Clone repo và đứng đúng branch của truyện:
   ```powershell
   git clone https://github.com/HaiPhongDao/Novel.git
   cd Novel
   git checkout <branch-của-truyện>
   ```
3. Lấy key: vào https://aistudio.google.com → **Get API key** → **Create API key** → copy.
4. Lưu key vào máy (chạy một lần, rồi **đóng và mở lại** cửa sổ PowerShell):
   ```powershell
   setx GEMINI_API_KEY "dán-key-vào-đây"
   ```
5. Xem mã model key dùng được, chọn đúng model đang dùng trên AI Studio, rồi lưu lại:
   ```powershell
   python tools/gemini_write.py --models
   setx GEMINI_MODEL "mã-model"
   ```
   (Mã model cũng xem được ở nút **Get code** trong chat AI Studio.)

## Mỗi đoạn

```powershell
git pull
python tools/gemini_write.py lam-game 2 --push
```

- Script tự chọn gửi gì: đoạn đầu session → `handoff/session-start.md` (tự ghép); đoạn thứ hai → prompt, kèm lịch sử chat của đoạn trước; đủ 2 đoạn → session mới.
- `--push` commit + push riêng file bản thảo; báo Agent kéo về review.
- Đoạn hỏng: Agent chuyển bản cũ vào `archive/` và sửa prompt; chạy lại với `--moi` (session mới, đúng quy trình).
- `--thu`: chỉ in ra sẽ gửi gì, không gọi API (vẫn ghép lại `session-start.md`). `--thinking low|none`, `--temp 0.8`: đổi cấu hình.

## Lưu ý

- Hạn mức miễn phí của API tính theo model, theo phút và theo ngày, Google hay đổi — xem trong AI Studio (mục usage / rate limit). Mỗi đoạn tốn 1 lượt gọi. Báo `429` là hết hạn mức: đợi rồi chạy lại.
- Ở gói miễn phí, Google có thể dùng nội dung gửi qua API để cải thiện sản phẩm.
- Lịch sử chat nằm ở `<truyện>/handoff/gemini-session.json`, không commit (`.gitignore`). Đổi máy thì đoạn kế tiếp tự mở session mới bằng gói bàn giao.
- SI lấy theo dòng "SI đang dùng: `gemini/...`" trong README của truyện. Đổi SI giữa chừng → script tự mở session mới.

## Chạy trên Claude Code cloud (chỉ dùng điện thoại)

Agent chạy script trong session cloud; key cất ở **Network secret** của môi trường, không vào máy, không vào chat:
claude.ai/code → môi trường (vd. Novel) → Add secret → Secret type: header tuỳ chỉnh (không phải Bearer) · Allowed websites `generativelanguage.googleapis.com` · Path prefixes trống · Custom header `x-goog-api-key`, Prefix trống, giá trị = key. Lưu rồi mở **session mới**. Script không cần `GEMINI_API_KEY` — proxy tự gắn header.
