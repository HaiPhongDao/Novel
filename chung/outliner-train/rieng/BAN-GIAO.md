# BAN-GIAO riêng — truyện từ tiền đề Tác giả (04/11/2026)

## 0. Trạng thái
- Truyện: `rieng/dong-kinh-1999/` (tiền đề `tien-de.md`: "MC xuyên qua đến Tokyo năm 1999 vẽ manga"). Chưa tạo bible.
- Tiền đề chỉ một dòng. Tên người, 5 sự thật cố định (`so.md`), 3 cảnh (`ke-hoach.md`) là Outliner chọn, **Tác giả chưa duyệt**.
- Cảnh 1 (một người): XONG, 1 lần chạy. `canh-1/`: thuoc.md → brief.md → kiem-truoc.md → v1.md → cham.md. Kết quả: BB 8/8 ✔, NT 3/3, chưa có điểm hỏng nặng; xem `cham.md`.
- Cảnh 2 (hai người có điều giấu), cảnh 3 (≥ 3 người): CHƯA LÀM.
- Brief tránh các chữ "Tokyo", "manga/漫画", "连载" vì grep (tiền đề có hai chữ đầu); thành phố chưa được nêu trong brief cảnh 1.
- Tất cả là GIẢ THUYẾT, 1 cảnh. SI `si-dong-bang.txt` đóng băng, không sửa.

## Làm tiếp (phiên mới, một cảnh)
1. Nếu Tác giả sửa tiền đề / tên / sự thật cố định: sửa `so.md`, `ke-hoach.md` trước, rồi mới viết brief.
2. Cảnh 2: đọc `QUY-TAC.md` (Q6, Q11, Q12, Q13, Q14), `so.md`, `ke-hoach.md` cảnh 2. Làm đúng thứ tự: `canh-2/thuoc.md` → `brief.md` → `kiem-truoc.md` → chạy 1 lần → `cham.md`. Cảnh hai người cần lời đáp của người nghe (Q12) và điều giấu khai riêng ở "Chỉ lộ ở câu cuối" (Q6). Khai nội tâm cho cả Ren và Noguchi; thử viết ý trần (không thành câu hoàn chỉnh) để đo ngưỡng Q13.
3. Nhịp hài: ghi bằng một sự việc buồn cười cụ thể, đừng ghi nhãn (Q3).
4. Tên Latin: Ren, Noguchi (cảnh 2); thêm Ebina, Hayama ở cảnh 3. Không kanji.
5. grep brief: `Akiyama|Kurokawa|Okada|Tokyo|漫画|连载|未麻|上杉`, rỗng.
6. Cuối phiên: cập nhật NHAT-KY, QUY-TAC, file này; commit + push các file đọc được, không `think-*.md`, `run-*.log`.

## Chạy Writer
`python tools/aistudio_run.py --batch chung/outliner-train/rieng/dong-kinh-1999/canh-N/jobs.json --timeout 22 > .../run-vN.log 2>&1 &` (từ gốc repo). Cảnh 1 mất 172 s.
