# Prompt mở phiên — `sung-thu` sau hiệu chuẩn: dựng truyện và chạy đoạn 001

Dán nguyên khối dưới vào một phiên Agent mới (Claude Code, Codex hoặc Hermes), không kèm ngữ cảnh nào khác.

---

Bạn là Agent đồng sáng lập của repo Novel, làm truyện mới `sung-thu`. Vai trò và phân quyền: `AGENT.md`.

## Lấy gốc

Làm ở `D:\ClaudeCode\Novel` (máy khác thì `git clone https://github.com/HaiPhongDao/Novel.git`), nhánh
`ccr-d59235d4-pqh9t3`. Chạy `git fetch --all` trước, kiểm `git log -1` khớp origin.

## Tiết kiệm token — bắt buộc (Tác giả: "dự án này đốt token cực nhanh vì phải đọc")

1. **Graphify trước, Read sau.**
   - Graph ở `graphify-out/` phủ thư mục `chung/` và đang cũ (dựng 04/11). **Việc đầu tiên của phiên:**
     `/graphify chung --update` — chỉ trích các file mới/đổi từ 04/11 (`chung/hieu-chuan/than-sung/`,
     `chung/doc-gemini/`, `chung/loi/`, `chung/kinh-nghiem.md` KN38…). Không dựng lại toàn bộ (lần đầu tốn ~1,26 triệu
     token).
   - Sau đó, mọi câu hỏi về luật, quy trình, kinh nghiệm, sổ lỗi trong `chung/`: chạy
     `graphify query "<câu hẹp>" --budget 1000` ở gốc repo, rồi chỉ Read đúng đoạn graph trỏ tới. Câu hỏi rộng ra
     nhiều node nhiễu — hỏi hẹp, dùng tên thuật ngữ.
   - Graph không phủ `AGENT.md`, `.claude/skills/`, `tools/`, thư mục truyện: Grep lấy số dòng rồi Read `offset/limit`,
     không đọc nguyên file.
2. **Chữ Trung giao Gemini đọc** (`chung/doc-gemini/README.md`):
   - Tóm tắt bộ mẫu cho bible/dàn ý: `python tools/doc_gemini.py tom-tat --bo-mau "sung-thu/神宠供应商(1-140章).txt"
     --chuong 1-40 --out <file>` (mỗi lần ≤150.000 ký tự; chia khoảng chương).
   - Mã trả về `3` = có câu trích không thấy trong nguồn → không tin báo cáo, chạy lại.
   - Đọc báo cáo và đúng đoạn được trích; không đọc nguyên bộ mẫu, không đọc nguyên thinking của Writer (grep).
3. **Một việc một phiên.** Repo là bộ nhớ; phiên dài thì mỗi lượt gửi lại toàn bộ ngữ cảnh.

## Đọc trước (theo thứ tự, ngắn)

- `AGENT.md` mục 3, 8, 11; khi viết brief thì `chung/mau-prompt.md`.
- `.claude/skills/novel-craft/SKILL.md`: Pipeline, mục 0, 3, 7, 9 (các mục khác tra khi cần).
- `sung-thu/README.md`, vài dòng cuối `sung-thu/log.md`.
- Comment đầu `sung-thu/gemini/system-instruction-v3.md`.
- `chung/kinh-nghiem.md` KN38 (tra bằng graphify).
- `sung-thu/gemini/test-giong/v6/khac/doc-ch05-ch08.md` — lỗi còn mở của SI.

## Trạng thái

- Hiệu chuẩn SI **ĐẠT** (Tác giả 05/11, đọc ch3/ch5/ch8). SI đang dùng: `sung-thu/gemini/system-instruction-v3.md` =
  nguyên văn SI của Argon Gemini; bản dán `sung-thu/gemini/si-dan-gemini.txt` (dựng bằng `python tools/dung_si.py
  sung-thu`, 7.630 ký tự).
- **Ba đoạn đầu không sửa SI** (SKILL, Pipeline bước 4). Ngoại lệ duy nhất cần Tác giả duyệt: FIXED 2 đang lấy tên bộ
  mẫu (洛羽 · 渔晚) làm ví dụ — khi truyện thật có tên nhân vật, đề xuất thay đúng hai tên ví dụ đó, ghi `log.md`.
- Lỗi còn mở cần soát ở mọi bản: dài hơn yêu cầu 50–90%; rò anchor (奶牛 · 虎鲸 · 珍珠 từ anchor ch2, 怪鳞鱼 từ ch11);
  rò tên bộ mẫu có trong anchor (洛羽, 渔晚, 陈卓, 七月, 地企鹅) — grep từng bản; ít thoại ở cảnh nhiều người.

## Việc của phiên

0. **Hỏi Tác giả trước khi dựng** — một lần, gộp, mỗi câu 2–3 phương án và khuyến nghị đứng đầu:
   - Tiền đề và trục truyện: giữ trục bộ mẫu (御兽 + 繁育, MC có mắt nhìn thiên phú ẩn) hay đổi; truyện mới phải khác
     **trục** các truyện đã có (bảng ở `README.md` gốc), không chỉ khác bối cảnh. Học kỹ thuật bộ mẫu, không nhập
     thiết lập, tên, cốt truyện của nó.
   - Tên truyện, tên MC và vài nhân vật chính.
   - Khung brief mẫu A hay B (AGENT.md mục 4: truyện mới phải hỏi).
1. Chép các thư mục còn thiếu từ `_mau-truyen/` vào `sung-thu/` — **không ghi đè** `README.md`, `log.md`, `gemini/`
   đang có.
2. Dựng theo AGENT.md mục 11, bước 1–5: `bible/overview.md` (logline, premise, hợp đồng độc giả, quỹ kết cục và bậc
   thang — `chung/xay-dung-truyen.md` mục 1, 3), `bible/glossary.md` (tên và xưng hô bằng chữ Hán), `bible/characters/`,
   `bible/world.md`, `plot/arcs.md` (kèm neo arc) → `plot/outline.md`. Mổ xẻ bộ mẫu chỉ lấy kỹ thuật
   (`chung/mo-xe-truyen.md`), đọc qua `doc_gemini.py tom-tat`.
3. Trình Tác giả bible + dàn ý. Duyệt rồi mới viết đoạn 001.
4. **Đoạn 001** theo `chung/hieu-chuan/prompt-agent-writer.md`: brief sáu khối; dựng cảnh quanh hợp đồng thể loại,
   không quanh tâm trạng (SKILL mục 3, QUY-TAC Q15); 黄金三章 (SKILL mục 9). Cổng `python tools/soat_brief.py`.
   Chạy **2 lần**, chat mới: `python tools/aistudio_run.py --new --si sung-thu/gemini/si-dan-gemini.txt --prompt
   sung-thu/briefs/doan-001.md --out sung-thu/chapters/doan-001-a.md` (chạy nền, cần Edge + extension, đừng poll).
   Cổng `python tools/cong_doan.py`. Push prose ngay. Đọc theo bốn việc trong `prompt-agent-writer.md`; câu ĐẠT là
   của Tác giả.

## Push — Tác giả đọc trên điện thoại

- Push ngay khi có: prose Writer, SI, bible, dàn ý, brief. Kiểm `git rev-list --count HEAD
  ^origin/ccr-d59235d4-pqh9t3` = 0.
- Báo cáo kèm link `https://github.com/HaiPhongDao/Novel/blob/ccr-d59235d4-pqh9t3/<đường dẫn>`, file nên đọc trước
  để lên đầu.
- Không commit toàn văn bộ mẫu `sung-thu/神宠供应商(1-140章).txt` (cố ý untracked), không commit `.log` có email.

## Ghi sổ và SKILL

- Cuối phiên chạy vòng học (SKILL mục 8): `python tools/so_loi.py quan-sat …`, `can-thiep …`, `bao-cao`, `kiem-tra`.
- Chỉ dẫn mới của Tác giả về **cách làm** ghi ngay vào `.claude/skills/novel-craft/SKILL.md` (commit riêng `skill: …`),
  không chỉ vào bộ nhớ riêng của Agent — Hermes và Codex chỉ đọc SKILL trong repo.

## Dừng và hỏi Tác giả khi

- Cần đổi SI, canon hay dàn ý đã duyệt.
- Một đoạn phải viết lại 2 lần.
- Tác giả nói không đạt — hỏi sai ở đâu, ghi nguyên văn vào sổ (`ket_luan: tac-gia-bac`).
- Hết quota mọi tài khoản AI Studio, hoặc tab rơi về trang đăng nhập.
