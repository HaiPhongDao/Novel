# QUY-TRINH.md — cách làm truyện hằng ngày

Trang này là **toàn bộ** thứ một Agent (Claude, Codex, Antigravity, Kimi, Hermes) cần đọc để làm ra đoạn mới.
Chỗ nào trang này lệch với `AGENT.md`, skill `novel-craft` hay `chung/` thì **trang này thắng**; lời Tác giả trong
phiên thắng tất cả. Vai trò và phân quyền (ai được quyết gì) vẫn ở [`AGENT.md`](AGENT.md) mục 1, 7, 8.

**Thước đo duy nhất: số đoạn Tác giả đã nghe và chốt mỗi tuần.** Bảng tiến độ: `python tools/lam.py bang`.

## 0. Vì sao có trang này (10/11/2026)

Ba tuần, 778 commit, 29 truyện, hơn 30 nhánh. Từ 29/10 không truyện nào qua đoạn 006. Sổ lỗi ghi 72 lần can
thiệp vào SI/brief: 10 lần đo được là có tác dụng, và lần đứng đầu bảng (I-0071, gấp 35 lần biên độ nhiễu) Tác
giả nghe xong vẫn bác. Vòng lặp cũ biến mỗi lời chê thành một đợt thí nghiệm (SI mới × 2 bản × đo × sổ lỗi × sửa skill) rồi chờ
Tác giả đọc — truyện đứng yên ở đoạn 001–003. Quy trình mới tách hẳn **viết** khỏi **chỉnh giọng** và đặt trần cho
việc chỉnh giọng.

## 1. Hai làn, không trộn

| | Làn SẢN XUẤT (mặc định) | Làn CHỈNH GIỌNG |
|---|---|---|
| Khi nào | Mọi phiên, trừ khi Tác giả nói khác | Mở truyện mới; Tác giả bảo "sửa giọng"; hoặc tới mốc 10 đoạn |
| SI | **Đóng băng** | Được đổi, theo mục 4 |
| Đọc gì | Trang này + `<truyen>/README.md` + brief và bản thảo đoạn trước | Thêm skill `novel-craft` và file nó trỏ tới |
| Không làm | Sổ lỗi, đo mật độ, chạy 2 bản, đọc thinking, sửa SI, đọc `chung/` | Viết đoạn mới của truyện |

## 2. Làn sản xuất — một lô 3 đoạn

Trước khi làm: `git pull --rebase` trên nhánh `main`. Lặp ba lần các bước 1–3, rồi 4–6 một lần cho cả lô.

1. **Brief trơn** `<truyen>/briefs/doan-NNN.md`, viết ngay trước khi chạy đoạn đó (không viết trước cả lô):
   - dòng đầu: `Viết tiếp đoạn tiếp theo, 2.000–2.500 字, bằng tiếng Trung.`
   - một đoạn văn 4–8 câu **chỉ gồm việc mới**: ai có mặt, mỗi người muốn gì / lo gì, chuyện gì xảy ra. Việc
     đoạn trước đã kể thì không nhắc lại — Writer đọc nguyên văn đoạn trước ở ngay trên brief.
   - `Dừng ở lúc …` (một việc đang dở).
   - `Tên cố định: …` — tên người, địa danh, đồ vật kèm chữ Trung. Thứ gì brief gọi bằng tiếng Việt mà không kèm
     chữ Trung thì Writer tự đặt chữ, mỗi lần một khác.
   - Không đánh số nhịp, không câu thoại mẫu, không nhãn tính cách, không dặn cách viết (đó là việc của SI).
2. **Chạy**: `python tools/lam.py viet <truyen> <N>` (2–7 phút, chạy nền, đừng poll). Lệnh tự ghép prompt = nguyên
   văn 2 đoạn liền trước + `handoff/canon-card.md` + brief; mở chat mới; thay chữ theo `gemini/thay-chu.txt`; qua
   cổng máy; bản cụt do mạng thì tự chạy lại một lần; cảnh báo nếu Writer chép lại câu của đoạn trước.
   Đoạn 001 chỉ gửi brief. Cần Edge đang mở với extension "Novel AI Studio bridge".
3. **Đọc lướt một lần** (Agent): tên, số, ai biết gì, có kể lại chuyện cũ không, dừng đúng chỗ không.
   - Sai tên / chữ lạ → sửa tại chỗ; chữ nào sai lần thứ hai → thêm một dòng `sai => đúng` vào `gemini/thay-chu.txt`.
   - Sai số, sai canon một câu → sửa đúng câu đó.
   - Hỏng mạch (sai cảnh, lộ bí mật, kể lại cả đoạn trước) → sửa brief, `python tools/lam.py viet <truyen> <N> --lai`.
     **Tối đa 2 lần chạy lại một đoạn**; lần thứ ba thì dừng lô và hỏi Tác giả.
   - Chi tiết mới Writer tự đặt mà đoạn sau cần → một dòng vào `handoff/canon-card.md`.
4. **Gửi Tác giả một file**: `python tools/lam.py doc <truyen> <N1> <N2>` → `<truyen>/doc/lo-N1-N2.md`; commit
   `"<truyen> NNN–MMM: nháp lô"`, push, báo 3–5 dòng kèm link. Không trình bản a/b, không dán chính văn vào chat.
5. **Tác giả nghe** (DocTTS) rồi trả lời "ổn" hoặc gửi phiếu góp ý. Xử lý phiếu theo bảng mục 3
   (`python tools/gop_y.py <phiếu> <truyen>` ra đúng file:dòng).
6. **Chốt**: `python tools/lam.py chot <truyen> <N1> <N2> -m "<một câu>"` — ghi README + log, gộp khối, commit, push.
   Rồi cập nhật `handoff/canon-card.md` nếu lô này đổi điều gì cố định, và làm lô kế.

Tác giả vắng mặt thì Agent **không chờ**: làm tiếp lô sau trên bản nháp, tối đa 2 lô (6 đoạn) chưa chốt. Phiếu góp ý
về sau áp vào các đoạn đó bằng sửa tại chỗ.

## 3. Tác giả chê — phân loại trong một phút, không mở thí nghiệm

| Tác giả chê | Làm ngay | Không làm |
|---|---|---|
| Một chữ, một câu, một cụm (từ lạ, cụm sáo, câu "giọng máy") | Sửa đúng câu đó trong `chapters/`. Chữ lặp lại → `thay-chu.txt` hoặc dòng `Tên cố định` | Sửa SI, chạy lại cả đoạn |
| Sai tên, sai số, sai canon | Sửa tại chỗ + một dòng vào `canon-card.md` | |
| Một đoạn hỏng mạch / lặp ý / cảnh sai | Sửa brief, chạy lại đoạn đó một lần (`--lai`) | Chạy lại các đoạn khác |
| Giọng toàn cục (thoại, nhịp, "giọng AI" khắp nơi) | Ghi một dòng vào `<truyen>/no-giong.md`: ngày · lời Tác giả nguyên văn · một câu trích. **Viết tiếp.** | Thử SI mới ngay, dừng sản xuất |
| 👍 Hay | Giữ nguyên; chép câu đó vào `no-giong.md` mục "giữ" | "Làm cho hay hơn" |

Sửa tại chỗ là sửa **đúng những chữ bị chê**, không viết lại cả đoạn văn. Bản đã sửa là bản chính thức; bản gốc
của Writer còn trong lịch sử git.

## 4. Làn chỉnh giọng — có trần

Mở khi: (a) mở truyện mới; (b) Tác giả bảo; (c) đã 10 đoạn từ lần chỉnh trước **và** `no-giong.md` có từ 3 dòng
cùng một loại. Mỗi lần mở:

- **Một vấn đề** (dòng nhiều nhất trong `no-giong.md`), **tối đa 2 phương án**, mỗi phương án **1 bản** trên cùng
  một brief đã có. Tác giả nghe 3 bản (hiện tại + 2 phương án) và chọn. Chọn "giữ nguyên" cũng là xong.
- Chọn xong là **đóng làn**: ghi `log.md` một dòng, đổi SI nếu có, quay về sản xuất. Không có vòng hai cho cùng
  một vấn đề trước mốc 10 đoạn kế.
- Phương án nào cần hơn 2 vòng sửa từng dòng thì bỏ: viết lại cả SI từ giọng bộ mẫu (xem dưới), không vá tiếp.

**Đã có bằng chứng — dùng luôn, đừng thử lại:**

- SI viết lại **cả bản** từ giọng bộ mẫu (cách Argon: `sung-thu/gemini/system-instruction-v3.md`, `han-nien-san-dong/de-xuat-argon.md`) ra giọng; vá từng dòng SI năm lượt liền thì không (I-0049…I-0059).
- Brief trơn, ngắn, chỉ sự việc. Brief sáu khối, brief dài, brief chen chữ Hán giữa câu đều bị Tác giả bác (I-0062, 09/11).
- Chữ Trung cố định cho từng thứ (bảng `bible/tu-mau.md`, dòng `Tên cố định`) trị từ lạ; cấm bằng BANS thì không (I-0072).
- Mỗi đoạn một chat mới chỉ kèm State JSON + 2.500 ký tự đuôi làm Writer kể lại đoạn trước (09/11). Vì vậy
  `lam.py viet` dán nguyên văn 2 đoạn trước và không dán State JSON. **Cách ghép này chưa có bản nào Tác giả nghe
  xác nhận — lô đầu tiên chạy bằng nó chính là phép thử.**

**Đã chết — đừng thử lại:** BANS nêu đích danh cụm từ (Tác giả: "chẳng thấy thay đổi gì mấy, còn giảm chất lượng
prose"); con số nhịp / khối LENGTH trong SI; chấm ĐẠT bằng điểm số hay mật độ; thêm dòng luật vào SI sau một lần
quan sát; bảo Writer "viết lại" trong cùng chat.

## 5. Mở truyện mới

Khuyến nghị: **không mở truyện mới khi truyện đang chạy chưa tới đoạn 30** — lỗi của truyện dài (mạch, canon, giọng
trôi) chỉ lộ ra khi đi xa, và chưa truyện nào trong repo đi tới đó bằng quy trình hiện tại. Quyền quyết là của Tác giả.

1. Tác giả chọn bộ mẫu. Agent dựng SI cả bản từ giọng bộ mẫu (mục 4), `python tools/dung_si.py <truyen>`.
2. Một bài hiệu chuẩn: 1 brief chỉ sự việc từ một chương bộ mẫu, 2 bản, Tác giả nghe. Tối đa 2 vòng; vòng 2 chưa
   được thì đổi bộ mẫu hoặc đổi model Writer, không vào vòng 3.
3. `cp -r _mau-truyen <truyen>`; điền tối thiểu: `bible/overview.md`, `bible/glossary.md` (kèm chữ Trung),
   `bible/characters.md`, `handoff/canon-card.md` (≤ 40 dòng, chỉ điều cố định), dàn ý 9 đoạn ở `plot/outline.md`.
4. Vào làn sản xuất. Ba lô đầu (9 đoạn) không đụng SI.

## 6. Git — một nhánh

- Mọi việc commit thẳng lên **`main`** và push ngay. Không tạo nhánh cho truyện hay cho thử nghiệm; bản thử nằm
  trong `<truyen>/gemini/test-giong/`.
- Phiên cloud tự sinh nhánh `ccr-*` / `claude/*`: cuối phiên gộp về `main` rồi xoá nhánh đó.
- Truyện cũ nằm ở nhánh cũ ([`chung/ban-do-branch.md`](chung/ban-do-branch.md)); lấy lại một truyện:
  `git checkout origin/ky-si -- ky-si`. Khi Tác giả cho dọn, mỗi nhánh cũ thành tag `kho/<tên nhánh>` rồi xoá nhánh.
- Thông điệp commit: `<truyen> NNN–MMM: nháp lô` · `<truyen> NNN–MMM: chốt — …` · `quy-trinh: …` · `tools: …`.

## 7. Trạng thái nằm ở đâu

| File | Ai ghi, khi nào |
|---|---|
| `<truyen>/README.md` | Bảng trạng thái từng đoạn (`lam.py chot` tự ghi) + mục "Việc kế" 3–5 dòng, cập nhật cuối phiên |
| `<truyen>/handoff/canon-card.md` | Thẻ thiết lập ≤ 40 dòng: điều cố định Writer cần ở mọi đoạn. Sửa khi canon đổi |
| `<truyen>/gemini/thay-chu.txt` | `sai => đúng`, thêm khi một chữ sai lần thứ hai |
| `<truyen>/no-giong.md` | Lời chê về giọng, chờ mốc chỉnh giọng |
| `<truyen>/log.md` | Mỗi quyết định một dòng (`lam.py chot` tự thêm dòng chốt) |
| `handoff/state.json`, `reviews/`, `chung/loi/` | Không bắt buộc ở làn sản xuất. Agent ghi khi tự thấy cần sổ số (tiền, hạn, ai biết gì) |

Cuối phiên: mục "Việc kế" trong README truyện đủ để phiên sau làm tiếp mà không cần hỏi lại.
