# Cần lưu ý khi làm việc trên repo này

Gom từ skill `novel-craft`, các sổ `chung/` và log các truyện (28/10). Chi tiết và bằng chứng nằm ở nguồn ghi bên cạnh; file này chỉ để khỏi quên.

## Git và branch
- Mỗi phiên cloud đẩy lên một branch `ccr-*` riêng; `origin/HEAD` trỏ chỗ khác. Nội dung từng truyện nằm ở branch dài nhất chứa nó — xem [`ban-do-branch.md`](ban-do-branch.md). Không hỏi "file đâu" trước khi `git fetch --all` và tìm trên remote (Tác giả hay sửa thẳng trên GitHub). — skill mục 0
- Phần chung (AGENT.md, `chung/`, `tools/`, `.claude/`, `writer/`, `_mau-truyen/`) commit **riêng**, không trộn chương/bible. Không gộp cả branch truyện chỉ để lấy một bài học. — AGENT.md mục 10, 12
- Kiểm push bằng số, không bằng cảm giác: `git rev-list --count HEAD ^origin/<branch>` = 0 và `git status --short` không còn `?? <truyen>/`. — skill mục 1
- Đánh số `KN` ở `chung/kinh-nghiem.md` bị trùng giữa các branch (hai branch cùng ra KN15): khi gộp, đặt lại số mới, đừng ghi đè.

## Chạy Writer
- Một session Writer chỉ viết 2 đoạn; đoạn hỏng làm lại ở session mới. — AGENT.md 5c
- `--out` của `aistudio_run.py` **ghi đè im lặng**: đặt tên bản theo ký tự chưa dùng ở cả `chapters/` và `chapters/archive/`. — skill mục 1
- Đừng sửa `tools/aistudio-ext/` khi có job đang chạy (extension tự reload, job treo tới timeout). "Extension không nhận việc sau 90s" → tiến trình cũ giữ cổng 8765. Job treo >10 phút không file = tab rơi về trang đăng nhập Google, nhờ Tác giả đăng nhập. — skill mục 3
- `Failed to generate content` / `No tab with id` là lỗi tạm: chạy lại nguyên lệnh sau 20–45 giây. `Permission denied` = tài khoản hết quota (script tự xoay tài khoản).
- Edge nạp extension từ bản chép ở máy Tác giả (`D:\ClaudeCode\aistudio-ext`): sửa extension trong repo thì phải chép sang đó. — skill mục 3
- Gemini API qua cloud: key cất ở **Network secret** của môi trường (header tuỳ chỉnh, host `generativelanguage.googleapis.com`), không vào chat; gọi `streamGenerateContent` vì `generateContent` bị 502 qua proxy. — [`gemini-api.md`](gemini-api.md)

## Brief và SI
- Prompt ngắn: hướng đi + số liệu; thêm câu chỉ khi đoạn trước hỏng đúng chỗ đó. Số dẫn xuất tính bằng script, không nhẩm. — AGENT.md mục 4
- Prompt của Agent cũng là mẫu tu từ: ranh giới phủ định ba vế dạy Writer đúng khuôn đó; viết khẳng định. — KN22
- Agent con chép câu nguyên tắc vào brief làm MC lạnh và cụt: **brief do phiên chính viết**, agent con chỉ chạy/soát/chốt. — `.claude/agents/novel-doan.md`
- Mẫu là truyện xuyên việt mà MC không xuyên → brief phải có dòng "X sinh ra ở thế giới này". — skill mục 2
- SI: lời kể (70–85% văn bản) phải có nguyên tắc + anchor riêng, đứng trước cảnh đặc biệt; không bịa anchor, kiểm bằng `verify_anchors.py`; sửa SI cần Tác giả duyệt + ghi log. — skill mục 5, `writer/SI-template` v4
- Test một lỗi Tác giả bảo sửa: tối đa 3 hướng × 1 bản; Tác giả đọc ~4 bản một vòng. — skill mục 5

## Review
- Cổng máy (`cong_doan.py`) chỉ chặn hỏng rõ; xanh chưa phải ĐẠT. Câu kết `——` khi brief bảo dừng giữa cú lao là cổng bắt nhầm. — skill mục 1
- `soat_van.py` bỏ sót nửa số so sánh và nhãn ngữ điệu: grep tay trước khi tin cột số. — KN30
- Tác giả đổi tiền đề giữa chừng (`soi-xam` 26–27/10): ghi `log.md`, giữ đời cũ trong `archive/`, dựng lại bible + SI, không vá chồng.
