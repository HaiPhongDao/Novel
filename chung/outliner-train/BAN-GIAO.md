# Bàn giao train Outliner (04/11/2026)

## 0. Trạng thái (cập nhật 04/11/2026, sau phiên 2)
- Làm xong: khung `chung/outliner-train/`, `tools/outl_chuong.py` (tách chương), `tools/outl_cham.py` (phân loại độ phủ theo từ khoá + liệt kê số cứng), ba chương thử: ch09 (C/M/K/P), ch22 (P/K/Q), ch54 (Q, hai cảnh + bài giảng). SI đóng băng `si-dong-bang.txt`.
- Rút ra: `QUY-TAC.md` (12 dòng, đều giả thuyết; Q11 nhãn→nhãn, Q12 nội dung dòng hồ sơ→danh sách là mới). Mẫu hiện tốt nhất: `MAU-BRIEF-Q.md` (chưa sửa theo Q11/Q12; sửa khi có thêm 1 chương xác nhận).
- 04/11 (theo Tác giả): đọc v2-Q/v1-Q không thấy **nội tâm** → thêm Q13 (13 dòng), `ch22/brief-dau.md` + `v3-dau.md` + `cham-v3.md`; tên lại kanji sai chữ. Việc kế đầu tiên: thử brief nội tâm **rút gọn**, và thêm nhóm NT vào mọi `dap-an.json`.
- ch54 v1-Q: BB 10 ✔ / 5 ~ / 2 ✘ trên 17 (`ch54/cham-v1.md`). Thư mục `ch30/`, `ch45/` chỉ có `goc.txt` (đã tách sẵn, chưa lập đáp án).
- Chưa commit (thư mục + 2 script untracked). Hỏi Tác giả rồi commit riêng: `outliner-train: …`.

## 1. Làm tiếp
1. Chọn chương **khác loại**: gợi ý ch30 "连载会议上的核武器！" (hội nghị, nhiều người nói — thử Q4/Q12 mạnh nhất; `goc.txt` đã có) hoặc ch45 "黑川碧的选择" (một người, nội tâm/quyết định; `goc.txt` đã có). Đã dùng: ch09, ch22, ch54. Tránh chương 1, 24, 27, 29, 52, 104, 107 (anchor / đã dùng hiệu chuẩn).
   Khi viết brief áp Q11/Q12 để xem có sửa được: nội dung then chốt bằng câu (không nhãn), dạng câu của câu cuối, nội dung dài kèm lời đáp/câu hỏi của người nghe, tên người chỉ Latin, ghim mốc thời gian nếu canon cần.
2. `python tools/outl_chuong.py N` → `chNN/goc.txt`; đọc gốc; lập `dap-an.json` (mẫu `ch22/dap-an.json`, nhóm BB/PH/TX, `dung` = đơn vị dừng).
3. Viết `brief-Q.md` theo `MAU-BRIEF-Q.md`. Chạy **1 lần** (Tác giả 04/11: không cần 2 lần):
   - `jobs-vX.json` mẫu ở `ch22/jobs-v2.json`; lệnh: `python tools/aistudio_run.py --batch <jobs> --timeout 22 > <log> 2>&1 &` (cần Edge mở + extension; ~4 phút/lượt, chạy song song được).
   - Chờ bằng MỘT vòng `for … ls file`; **đừng** dùng `pgrep` (Git Bash trên máy này không có, vòng chờ thoát sớm).
4. `python tools/outl_cham.py chNN/dap-an.json chNN/vX-*.md` để khoanh, rồi **đọc tay**; ghi `chNN/cham-vX.md` theo mẫu `ch22/cham-v1.md`.
5. Cập nhật `QUY-TAC.md` (nhãn n/m chương) và `NHAT-KY.md` (≤ 6 dòng).

## 2. Cảnh báo
- Đừng đọc `tools/.aistudio_state.json` (bị chặn là thông tin đăng nhập).
- Cùng brief, độ dài dao động 1.377–2.271: không dùng độ dài làm tiêu chí.
- Nếu Q hỏng ở chương mới, tách từng thay đổi (Chỉ lộ cuối / một câu / hình ảnh / Nhịp cảnh) trên chính chương đó; còn bị kẹt sau 2 cách thì gọi Opus (Agent `model: opus`, brief ≤ 40 dòng, báo cáo ≤ 200 từ).
- Brief Novel không giao agent con viết (memory `novel-brief-khong-giao-agent-con`); agent con chỉ để đọc/khoanh.

## 3. Mở phiên mới
Dán `PROMPT-PHIEN-MOI.md` (nguyên văn; chương bộ mẫu) hoặc `PROMPT-PHIEN-RIENG.md` (truyện riêng, không chương gốc, điền tiền đề). Mỗi phiên một chương; xong thì cập nhật mục 0 và 1 ở trên rồi mở phiên mới.
