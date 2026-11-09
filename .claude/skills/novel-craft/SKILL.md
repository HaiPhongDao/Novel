---
name: novel-craft
description: "CHỈ cho làn chỉnh giọng của repo Novel (QUY-TRINH.md mục 4–5): dựng/sửa/hiệu chuẩn SI, đo một lần sửa có tác dụng không, sổ lỗi. Viết đoạn mới hằng ngày KHÔNG nạp skill này — đọc QUY-TRINH.md."
version: 3.1.0
---

# Novel Craft — cách làm truyện, và cách biết mình đã sửa đúng

> **Từ 10/11/2026 skill này là tài liệu của làn chỉnh giọng.** Viết đoạn mới theo `QUY-TRINH.md` (làn sản xuất:
> SI đóng băng, một bản mỗi đoạn, không sổ lỗi, không đo). Chỗ nào skill lệch `QUY-TRINH.md` thì `QUY-TRINH.md`
> thắng — kể cả trần của làn chỉnh giọng: một vấn đề, tối đa 2 phương án × 1 bản, Tác giả chọn là đóng.

Vai trò, phân quyền, cấu trúc thư mục ở `AGENT.md` — skill này không chép lại. Ở đây ghi **cách làm** và **cách
kiểm chứng**: thứ tự việc, lệnh chạy được, bẫy đã trả giá, và cách đo xem một lần sửa có thật sự làm văn tốt lên.

Ba câu định vị:

1. **Brief quyết nội dung, SI quyết cách viết, review quyết đúng sai.** Sửa lẫn ba chỗ là mất dấu nguyên nhân.
2. **Số đo là cổng, không phải điểm.** Bản 34/34 điểm vẫn bị Tác giả loại vì "viết quá loạn xạ" (KN36).
3. **Không có biên độ nhiễu thì không có kết luận.** Cùng một SI đã cho ra cả 0 và 5 cặp phủ định ở hai lần chạy.
   Hai lần chạy y hệt trên làn manga còn lệch 1.673 và 2.329 chữ.

## Pipeline — làm đúng làn

Hai làn. Trộn là mất dấu nguyên nhân.

**Làn mở truyện** (manga-v7 và truyện mới): làm theo `chung/hieu-chuan/README.md`, vận hành theo
`chung/hieu-chuan/prompt-agent-writer.md`.

1. Tách một chương bộ mẫu, viết brief chỉ có sự việc, dựng SI từ `writer/SI-template` **v6** (không khối LENGTH,
   không con số nhịp). Chạy Writer **hai chat mới**. Ghép `doc-cap`. **Tác giả đọc** rồi mới được gọi là ĐẠT.
   Khung Tác giả đã thấy "ổn" (03/11): bản gọn FIXED + mục 1 (nhân vật) + mục 3 (thoại) + BANS + PART 3, **không
   ROLE** (`chung/outliner-train/si-dong-bang.txt`). Tác giả bác mục 2, mục 4 và khối NARRATION (I-0039, I-0040,
   I-0041). Khung đó là của làn manga — **đừng mang chữ của nó sang bộ mẫu khác giọng**: `sung-thu` giữ chữ các mục,
   chỉ đổi anchor, năm lượt (I-0049…I-0058) đều ra giọng người đứng ngoài; SI viết lại cả bản từ giọng bộ mẫu (Argon,
   `sung-thu/gemini/system-instruction-v3.md`) mới ra (I-0059, Tác giả: "Đó, bản X…"). Bàn tay vàng thêm PART 4.
2. Chưa ĐẠT thì sửa anchor hoặc một nguyên tắc viết bằng lời (mục 6b). Không thêm số, không dựng bible.
3. Tác giả ĐẠT rồi mới có `bible/` và `plot/outline.md`. AGENT.md mục 11 làm bible trước — bước đó bỏ qua.
4. **Ba đoạn đầu không sửa SI đã chốt.** Nhiễu giữa hai lần chạy lớn hơn mức một dòng luật mới chứng minh được.
5. Brief sáu khối, mẫu `chung/hieu-chuan/manga/brief-doan-001-mau.md`: tình huống · bối cảnh thời đại · đạo cụ và
   thao tác · trạng thái riêng · ba biến khi nói · điểm dừng. Chất liệu, không nhãn tính cách.
6. Mỗi brief hai lần chạy. Đọc bốn việc trong prompt bàn giao. Số chỉ để khoanh vùng.
7. Ghi sổ (mục 8). Một lần sửa = một biến.

**Làn truyện đã chốt đoạn** (mẫu A hoặc B): vòng mục 1. Không đè SI hiệu chuẩn lên SI truyện đã duyệt.

Lệch nhau thì: làn mở truyện nghe prompt bàn giao và `hieu-chuan/README.md`; làn đã chạy nghe mục 1–8 file này.
Đừng giao ba đoạn đầu cho agent `novel-doan`: agent đó sửa tay chính văn và không đọc skill.

## 0. Năm phút đầu phiên

- Gốc repo = `git rev-parse --show-toplevel`; làm ở bản clone có commit mới nhất (`git log -1 --format=%ci`) và
  nói rõ đã ghi ở đâu. Bản local có thể cũ hơn GitHub — `git fetch --all` trước. Nhánh đang làm:
  `git for-each-ref --sort=-committerdate refs/remotes | head`; `origin/HEAD` thường trỏ chỗ cũ.
- Đọc theo thứ tự: `AGENT.md` → `chung/kinh-nghiem.md` → `python tools/so_loi.py bao-cao` → `<truyen>/README.md`
  → `log.md` → `handoff/state.md` → review gần nhất. Tác giả hay sửa thẳng trên GitHub web: không thấy file họ
  nói thì fetch rồi tìm trên remote trước khi kết luận.
- **Tiết kiệm token** (Tác giả 05/11: "Bạn phải dùng Graphify để tiết kiệm token"). Hỏi luật, quy trình, sổ lỗi
  trong `chung/` thì chạy `graphify query "<câu hẹp>" --budget 800–1500` ở gốc repo trước, rồi chỉ đọc đúng đoạn
  graph trỏ tới. Graph chỉ phủ `chung/` (dựng 04/11); file đổi sau đó: `/graphify chung --update`. File dài ngoài
  graph: Grep lấy số dòng rồi Read `offset/limit`, không đọc nguyên file. Thinking của Writer: grep, không đọc hết.
- **Chữ Trung giao Gemini đọc trước** (Tác giả 05/11 chọn "Dựng lối Gemini đọc"): `python tools/doc_gemini.py
  doc-cap | tom-tat | tim-anchor …` (`chung/doc-gemini/README.md`). Mọi nhận định kèm câu trích, script kiểm từng câu;
  mã `3` = có câu trích không thấy → không tin báo cáo. Agent đọc báo cáo và đúng đoạn được trích; câu ĐẠT vẫn do
  Tác giả. Lần thử đầu (sung-thu v1 ch3): 51/51 câu trích thật, khớp kết luận Agent đọc tay và bắt thêm hai chỗ.

## 1. Vòng một đoạn

Mỗi bước có một **cổng**: chưa qua thì không sang bước sau.

1. **Trạng thái + sổ số.** Số chép từ `<truyen>/plot/so-lieu.md`; số riêng tư gắn chủ thể biết (`chỉ mình <Tên>
   biết`); số dẫn xuất **tính bằng script, không nhẩm** — Writer chép nguyên số sai. Quét tên riêng Writer vừa
   đặt, neo vào `Sổ đầu đoạn` hoặc glossary trước khi chạy.
2. **Brief ngay trước khi chạy đoạn đó**, không viết trước cả lô (mục 3). Cổng:
   `python tools/soat_brief.py <brief> --prev-brief <brief trước> --bible <truyen>/bible/characters.md
   --glossary <truyen>/bible/glossary.md` + **`--mau-b` nếu truyện chạy mẫu B** (thiếu cờ thì cổng chấm brief B
   bằng thước của A và báo CHẶN oan). Mã thoát: `0` xanh · `1` có dòng CHẶN · `2` lỗi script — **`2` không phải
   "bị chặn"**. CHẶN = sửa brief, không chạy.
   Đoạn trước chưa duyệt mà Tác giả bảo viết tiếp: nối từ bản đã sửa hết lỗi canon gần nhất, ghi tên bản gốc
   vào review + `log.md`.
3. **Chạy Writer** (mục 4). Tên bản theo ký tự chưa dùng ở cả `chapters/` và `archive/` — `--out` ghi đè im lặng.
4. **Cổng máy**: `python tools/cong_doan.py <bản> --prompt <brief> [--prev <đoạn trước>]`. Đỏ = bỏ bản, đừng đo,
   đừng commit. Xanh chỉ là điều kiện cần (mục 6).
5. **Đo và đọc** (mục 5), ghi vào đúng `reviews/doan-XXX.md` kèm bảng số và kết luận ĐẠT / SỬA NHẸ / VIẾT LẠI.
6. **Ghi sổ lỗi** (mục 8): mỗi lỗi bắt được là một dòng quan sát — bước hay bị bỏ nhất.
7. **Chốt**: `python tools/chot_doan.py <truyen> <spec.py>` hoặc commit + push tay. Kiểm push bằng số:
   `git rev-list --count HEAD ^origin/<branch>` = 0 và `git status --short` không còn `?? <truyen>/`. Báo cáo Tác
   giả 3–5 dòng (số chữ, diễn biến, verdict, link), không dán cả bản 2.000 字 vào chat.

Đoạn hỏng → `git mv` vào `archive/`, sửa brief, chạy lại bằng **chat mới** (`--new`); không bảo Writer "viết lại"
trong cùng chat — nó chép lại 77% bản cũ của chính nó.

## 2. Sửa ở tầng nào — quyết định trước khi sửa

Sai ở đây thì mọi số đo sau đó vô nghĩa.

| Triệu chứng | Tầng | Sai tầng thì sao |
|---|---|---|
| Sai/thiếu **dữ kiện** (tuổi, giá, ai biết gì, ai có mặt) | **brief**, glossary, state | Luật SI ở lại, lỗi tái phạm ở cảnh khác |
| Sai **luật thế giới**, canon, quan hệ | **bible** (Tác giả duyệt) + `log.md` | Sửa văn để khớp bible sai |
| **Giọng, nhịp, khuôn câu** lặp ở ≥2 lần chạy với brief khác nhau | **SI**, một dòng PART 2 **thay** một dòng cũ | SI phình, luật mới lấy chú ý luật cũ, tổng lỗi không giảm |
| Lỗi **mới gặp một lần**, chưa rõ có hệ thống | **review-blacklist** + sổ lỗi | Thành luật SI sau một quan sát = overfit |
| Đo được nhưng **tool bỏ sót / bắt nhầm** | **tool**, hoặc grep tay rồi ghi vào review | Tin cột số 0 của tool (KN30) |

Thứ tự thử, rẻ tới đắt: **brief → glossary → đúng một câu trong prompt → SI → tool**. Dừng ở tầng đầu tiên chứng
minh được bằng số. Hai điều cấm:

- **Cấm sửa tay văn của Writer rồi trình bản đó như kết quả.** Bản sửa tay dùng để *tìm ra* luật; bằng chứng phải
  là một lần chạy lại đúng brief cũ, không thêm dòng nào (đo được: bản sửa tay 50 lượt/34,0 字 mỗi lượt so với bản
  Writer cùng SI 32 lượt/24,0 字 — luật trong SI ăn hơn việc kéo dài từng câu).
- **Cấm thêm dòng thứ hai diễn đạt cùng một ý.** Đọc lại chỗ định sửa; đã có thì làm mạnh câu cũ.

## 3. Brief

Hai hình dạng cùng tồn tại, ghi hình đang dùng ở `<truyen>/README.md`; đổi giữa chuyện phải có Tác giả đồng ý +
`log.md`. Truyện mới: hỏi Tác giả.

**Dựng cảnh quanh hợp đồng thể loại, không quanh tâm trạng** (Tác giả 04/11, `chung/outliner-train/QUY-TAC.md`
Q15). Brief lấy "hoang mang → lạnh dần" làm xương sống thì ra văn thanh, không ra truyện mạng. Trước khi điền
khung: vấn đề có hạn → MC phán và chọn dám → chỗ sướng → dừng ở việc đang dở; brief không chứa tính từ cảm giác.

- **A — ngắn**: vài câu phương hướng + số liệu + chỗ dừng. Mặc định cho làn manga, `lam-game`, `vong-du`.
- **B — đầy đủ**: thiết lập / tiền tình / điểm bắt buộc / tự do sáng tạo. Nhánh `de-quoc-1`, `lanh-chua-chip`.

**Ngân sách thật.** Tính trên **phần dặn cách viết**, không tính ba khối dữ kiện bắt buộc (`Người có mặt`,
`Xưng hô`, `Sổ đầu đoạn`). Đo 43 brief: phần dặn trung bình **468 từ**, **38/43 vượt 300** (mẫu A trung vị 444,
cao nhất 738). Nguyên nhân không phải viết dài dòng mà là ba khối dữ kiện được thêm sau và không được tính vào
ngân sách. Vì vậy: ghi số thật vào báo cáo, **đừng cắt xuống 300 từ bằng cách bỏ dữ kiện** — bỏ dữ kiện là đổi lỗi
văn thành lỗi canon (prompt 19 dòng ra bản sạch tật nhưng `回大人` 0, `会长` 0, cha chết "năm ngày"). Muốn ngắn
hơn thì cắt phần dặn cách viết, giữ hai dòng chặn quanh khối bảng và mọi dòng có số.

Luật còn lại:

- Mở bằng "Viết tiếp đoạn tiếp theo…" và chỉ ghi chỗ dừng. Một mục "Mở" làm Writer dựng lại cảnh như chương mới.
- **Khối nối tiếp đứng đầu brief: tiếng Trung nguyên văn** 250–350 字 của bản **Tác giả đã duyệt**, câu "viết tiếp
  từ đây, không chép lại câu nào", rồi mô tả bằng tiếng Việt chỗ dừng + việc đang treo. Cắt bằng
  `python tools/noi_doan.py <đoạn-trước> --chars 300 --wrap`, không gõ lại tay; sau khi chạy kiểm chép bằng 4–5
  câu đặc trưng (`grep -c '<câu>' <bản mới>` phải ra 0).
- **Một tình huống, không một chuỗi sự kiện.** Dữ kiện ghi là "bối cảnh để giữ cho đúng, không cần kể hết"; dừng
  sớm. Giao cả chương trong 2.000 字 thì mỗi dữ kiện thành một dòng, Tác giả đọc ra "checklist" (đoạn kể ≥40 字:
  0 → 19 khi chỉ còn một tình huống).
- **Khẳng định, không liệt kê cấm**; tối đa một câu phủ định. Ranh giới viết bằng sự thật thuộc đoạn sau ("câu
  trả lời của anh thuộc đoạn 002"), không bằng "không viết A, không viết B".
- **Không đánh số beat, không giao nội dung từng lượt thoại, không câu thoại mẫu.** Số lượt và độ dày thoại do
  **phạm vi thời gian và số người có mặt** quyết; muốn thoại dày thì mở phạm vi, thêm người (prompt 6 beat → 14
  lượt, MC 0 câu đùa; không prompt → 42 lượt, MC có giọng — KN32).
- **Không dán raw State JSON hay cả gói bàn giao**; riêng đoạn 001 tuyệt đối không dán Canon/State/Voice — model
  ngộ độc dữ kiện sẽ xả số liệu liên thanh và giải mã kịch bản (KN35).
- **Mỗi nhân vật có mặt một dòng thân phận** (ai + vai + một dấu hiệu), và **một dòng xưng hô** trong mọi brief.
  Thiếu thì Writer tự điền canon: phó quan 34 tuổi thành cậu hầu 16 tuổi.
- **Không câu tiếng Trung nào ngoài khối nối tiếp và tên/thuật ngữ ngắn** — câu mẫu bị chép nguyên làm mở đoạn,
  mọi điểm chấm trên bản đó thành điểm giả.
- **Brief phải đọc hiểu được ngay — Tác giả đọc brief như người viết đọc** (Tác giả 05/11, `sung-thu` đoạn 001: "Dở
  quá, nhiều từ ngữ bạn viết ra bằng tiếng việt nó khó hiểu quá? Đến tôi còn chẳng đang biết bạn muốn viết cái gì";
  E-BRIEF-09, I-0062). Brief sáu khối tiếng Việt chen chữ Hán giữa câu, nhãn khung ("Khoá", "Ba biến", "Sổ đầu
  đoạn"), câu dài nhiều mệnh đề là hỏng. **Đang thử** cùng nội dung bằng brief tiếng Trung và tiếng Anh
  (`sung-thu/briefs/doan-001-zh.md`, `-en.md`); khi Tác giả chấm thì sửa dòng này và dòng trên. `soat_brief.py`
  chỉ đọc brief tiếng Việt: với brief zh/en, CHẶN `cau-tieng-trung` và `thieu` (chỗ dừng) là do ngôn ngữ, không phải lỗi.
- **Dòng đếm tỷ lệ thoại/lời kể**: có thì thoại dày hơn, không có thì Writer chẻ lời thành nhiều lượt ngắn. Đánh
  đổi đã biết, không phải lỗi mới — cần thoại dày thì mở phạm vi cảnh. Bible là nguồn canon, không phải README.
- Ghi đầu brief **các mã lỗi brief này đang bù** (`Bù: E-CANON-03`): khi lỗi đó thôi tái phạm, dòng bù ấy là ứng
  viên cắt đầu tiên — không có dòng này thì brief chỉ phình ra.

Số đo + ngoại lệ: `references/brief-chi-tiet.md`; khung: `templates/brief-doan.md`.

## 4. Chạy Writer

```
python tools/aistudio_run.py --new --si <truyen>/gemini/si-dan-gemini.txt
    --prompt <truyen>/briefs/doan-XXX.md --out <truyen>/chapters/doan-XXX-<bản>.md
```

- Cần Edge mở + extension "Novel AI Studio bridge" (cổng 127.0.0.1:8765 do script mở — đừng curl thử bridge).
  Một đoạn 2–7 phút: **chạy nền**, chờ thông báo, đừng poll; chờ thì viết brief kế.
  `--batch jobs.json` để chạy nhiều bản; AI Studio để chat tạm nên **gửi tiếp vào chat cũ không được**.
- `--think-out <truyen>/archive/thinking-XXX.md` khi nghi SI bị hiểu sai: thinking cho thấy model đang tự kiểm
  cái gì (KN27). Đọc trước khi sửa SI.
- Lỗi tạm, chạy lại y nguyên sau 20–45 giây: `Failed to generate content`, `No tab with id`, "Extension không nhận
  việc sau 90s" (tiến trình cũ giữ cổng 8765: `netstat -ano | findstr :8765`, `Stop-Process`). Job treo >10 phút
  không file = tab rơi về trang đăng nhập: nhờ Tác giả, đừng sửa script. `LỖI: No current window` = Edge chỉ còn
  tiến trình nền: `Start-Process msedge -ArgumentList '--new-window','about:blank'`.
- Đừng sửa `tools/aistudio-ext/` khi có job chạy; sửa thì chép sang thư mục Edge **thật sự nạp** (`Secure
  Preferences` → `path`) và giữ bản cũ, nếu không extension reload code cũ. Quota: script xoay `/u/0 → /u/1 →
  /u/2`, ghi `tools/.aistudio_state.json` — ghi quota theo **email**, đừng theo số `/u/N`.

Bẫy chi tiết (quota, capture cụt, dòng trống): `references/chay-writer.md`.

## 5. Review và đo

- **Đích là mật độ của bộ mẫu, không phải 0.** Bộ mẫu manga: phủ định lặp **1,39**/1.000 字 (chương của mình
  0,31–0,59 = **dưới** mẫu), nhãn ngữ điệu **0,03** (0,11–0,62 = cao 4–20 lần mẫu). Nên 2–3 cặp phủ định mỗi
  đoạn là bình thường; so sánh người kể và nhãn ngữ điệu mới là tật. Đích đầy đủ: `chung/loi/muc-tieu.jsonl`.
- Đích có ba nguồn, phải ghi rõ: `mau` (bộ mẫu), `tac-gia` (Tác giả dặn — **thắng** mẫu), `noi-bo` (mốc của bản
  đã duyệt). Ba nguồn xung đột; không ghi rõ thì mỗi lần review là một lần tung đồng xu.
- **Số đo khoanh vùng, không chấm hay.** Phán chất lượng bằng **đọc**: mở/giữa/kết × (ai muốn gì · cái gì đổi ·
  câu đáng nhớ · chỗ người đọc bỏ qua), đặt cạnh mẫu — `references/doc-bang-doc.md`. Làn mở truyện: mật độ là kính
  lúp, câu ĐẠT chỉ do Tác giả (`chung/hieu-chuan/README.md`). Làn đã chạy: mật độ là cổng hồi quy, không phải điểm.
- **Cột 0 không phải bằng chứng sạch.** `soat_van.py` bỏ sót `如…般`, `如铁`, `如鹰隼`, nhãn `平静地命令道`. Grep tay
  `如.{1,8}般|如铁|如鹰` và `(平静|冷冷|淡淡|轻声)地(说|道|命令|问|开口)` trước khi báo ĐẠT (KN30).
- **Đo nhiễu trước khi nhận công.** Hai lần chạy y hệt lệch nhau ở độ dài và mật độ câu, gần như không lệch ở
  chi tiết — chi tiết trùng không phải "chép". Quy về mật độ/1.000 字; chỉ coi là có tác dụng khi ra khỏi biên độ.
- **Bản Tác giả khen có phần là lượt may**: chạy lại cùng prompt + SI không ra lại chất lượng đó — đừng coi
  prompt ấy là công thức chắc. **"Ngang nhau / đều đạt" là hết vòng tối ưu**: chốt một bản, ghi log, sang đoạn
  kế. **Tác giả chọn bản khác bản mình khuyên → lấy bản của họ làm gốc.**
- Tật register/xưng hô sửa ở ba tầng: glossary (bảng tra) + SI (luật cho nó xuất hiện) + một dòng prompt. Dòng
  glossary **không phải lệnh**: thêm `少爷` thì nó ra 9 lần, nhưng `小的` vẫn 0 vì không có luật nào ở SI.
  Muốn một cách xưng hô *xuất hiện*, phải có câu ở SI hay prompt — `references/register-tay-huyen.md`.

## 6. Bốn cổng soát — và cái chúng không bắt được

Mỗi cổng mù một phần: `cong_doan.py` không bắt văn loạn hay nhảy cóc dữ kiện; `soat_van.py` đếm được phủ định
lặp, 得像…, khuôn 实, phần lớn nhãn ngữ điệu nhưng **bỏ sót** `如…般`, `平静地命令道`, câu cụt và số học;
`soat_brief.py` bắt số học, lệch bible, chỗ dừng, tên chữ Hán nhưng **không** bắt ngân sách từ, tỷ lệ thoại, mức
"checklist", và bỏ qua bible với brief viết thẻ trong ngoặc (20/43); `cham_doan.py` chỉ có band làn 领主.
Không cổng nào trong bốn cổng này được phép kết luận ĐẠT — I-0020, Tác giả bác chấm bằng điểm.

**Tật "giọng AI" và thổ ngữ** (Tác giả 09/11: "văn mẫu viết bằng bạch thoại văn"; đọc 30 câu qua DocTTS đã bắt
实打实 · 语气平稳得很 · 直往鼻孔里钻 — "giọng AI… tồn tại cảm rất lớn"). Bốn cổng trên không có cột cho chúng.
`python tools/tat_ai.py quet --mau <bộ mẫu> <các bản Writer>` tìm cụm Writer dùng gấp nhiều lần bộ mẫu; `dem` đếm
một danh sách — **chỉ để khoanh vùng**. Đã thử và bị bác: một dòng BANS nêu đích danh ~15 cụm (SI-R, SI-R2) hạ số đếm
6,6–16 → 0,9–7,4 /1.000 字 nhưng Tác giả đọc: "Chẳng thấy thay đổi gì mấy, còn giảm chất lượng prose nữa chứ"
(I-0068, I-0071 `tac-gia-bac`). Thinking ghi "checking for banned phrases… replacing them with suitable alternatives":
cấm từ thì Writer thay từ, văn cứng đi, giọng AI vẫn còn. Số đếm giảm không phải bằng chứng đã chữa. Tìm nguồn trước khi cấm:
`tat_ai.py nguon --mau <bộ mẫu> --tu SI=<SI> --tu prompt=<gói/brief> <bản…>` cho biết mỗi từ lạ nằm sẵn trong SI, trong
gói, hay do Writer tự đặt. Ở `han-nien-san-dong`, chữ cổ (鱼鳞册 · 庄头 · 红契) chép từ danh sách từ trong SI; chữ "không biết từ
đâu" (套子 · 荒坡 · 界碑) là Writer tự đặt cho thứ brief tiếng Việt không ghi chữ Trung. Sửa: bảng chữ bộ mẫu
(`<truyen>/bible/tu-mau.md`) + dòng "Chữ cố định" trong brief + SI chỉ liệt kê chữ bộ mẫu dùng — từ lạ 12,6–18,9 → 0,6–3,2
/1.000 字 (I-0072).

## 6b. Sửa bằng bỏ trước, thay sau

SI đã chốt của làn manga nằm ở `chung/hieu-chuan/manga/gemini/si-dan-gemini.txt`. Trong ba đoạn đầu của truyện
thật, file đó đóng băng. Đóng băng không xác nhận principles: mười lăm dòng PART 1 / PART 2 / BANS đều
`chưa-xác-nhận` (`chung/hieu-chuan/manga/gemini/principles-trang-thai.md`).

Khi được phép sửa, theo thứ tự:

1. **Bỏ** đúng một dòng đang nghi dạy lỗi: con số nhịp, câu luật kiểu "short and snappy", anchor có tật, hoặc một
   dòng trong bó I-0025. I-0025 bỏ cả bó câu cấm và giữ hướng dẫn "nên làm"; giảng huấn tăng 0,82 → 1,86 /1.000 字.
   Bó đó phản tác dụng. Từng dòng trong bó vẫn chưa tách được.
2. **Thay** một dòng PART 2 bằng đúng một dòng khác chỉ sau khi bước bỏ đã chạy hai lần và vẫn lệch. Không thêm
   dòng thứ hai cùng ý. Dòng bị thay ghi vào `log.md` kèm mã can thiệp — cổng ở `writer/SI-template`, mục điền 6.
3. `vo-hieu` hoặc `phan-tac-dung` thì gỡ trong phiên đó (mục 8, luật 4).

## 7. SI: nguồn → bản dựng → phép thử

Khung đang điền: `writer/SI-template` **v6** (01/11, Tác giả: bỏ LENGTH và mọi con số nhịp; I-0023). Ngân sách,
số anchor, PART 2, BANS nằm trong file đó — không chép lại ở đây. v5 là đời cũ: còn neo độ dài câu, và neo đó
**không** được coi là số an toàn. Đo bằng
`python tools/dung_si.py <truyen>`: `len()` phần dán, số dòng từng mục, **và phần trăm ký tự anchor chiếm** — vì
anchor nhiều chữ cũng là cách vượt ngân sách (`manga-tokyo-2000`: 2 anchor nhưng chiếm 43% phần dán). Hiện 4 SI
v5 nằm ở 98,5–99,7% trần: ngân sách đang bị dùng như **hạn mức để lấp**.

**SI là nguồn + bản dựng, không phải một file văn xuôi.**

- `<truyen>/gemini/system-instruction-vN.md` là **nguồn**, có chú thích. Giữ **mọi đời** `vN`: hiện 4/5 truyện v5
  chỉ còn `v1`, và `manga-tokyo-2000` bị viết lại (7.913 → 4.749 ký tự, mất BANS, PART 3) mà **vẫn tên `v1`** —
  đời thật không có tên. Mất BANS hoặc PART 2 là nợ cấu trúc. Mất LENGTH thì không phục hồi.
- Mỗi dòng PART 2/BANS kết thúc bằng `<!-- I-xxxx -->` trỏ tới can thiệp đã sinh ra nó. Dòng không có mã là dòng
  chưa có bằng chứng — ứng viên cắt đầu tiên.
- `<truyen>/gemini/si-dan-gemini.txt` là **bản dựng** do `dung_si.py` sinh ra; không sửa tay. Đừng đưa
  `system-instruction-vN.md` thẳng cho `--si`: không có code nào cắt marker, cả khối "HƯỚNG DẪN ĐIỀN" sẽ bị dán
  vào model.
- Sửa SI đang chạy cần **Tác giả duyệt** + `log.md` ghi `Duyệt:` và số ký tự trước/sau. Đo 5 SI v5: **0 bản ghi
  có Tác giả duyệt**, 2 ghi "Duyệt: Agent", 3 không ghi. `Duyệt: Agent` chấp nhận được cho SI chưa có đoạn
  nào — nhưng phải ghi, và cập nhật số ký tự vào README **cùng commit**.

**Cổng xét luật mới vào SI** — **bỏ trước, thêm sau**: (1) **bỏ** dòng luật đang gây lỗi, chạy lại đúng brief cũ —
không tái phát thì xong (ngắn lại là tốt); (2) do brief/thiếu dữ kiện → sửa brief/glossary/state;
(3) mới gặp một lần → `review-blacklist` + ghi sổ; (4) lặp ở **≥2 lần chạy với brief khác nhau** → một dòng
PART 2 **thay** một dòng cũ, ghi `log.md` kèm mã can thiệp; (5) chưa có phép thử thì chưa được coi là đã chữa. Cổng có từ 29/10 mà **chưa lần nào được dùng đúng**: grep `gỡ|bỏ luật|thay dòng` trên mọi `log.md` ra
0 dòng theo khuôn, trong khi `ky-kham-lanh-chua` đã đi từ 15 lên 25 dòng PART 2.

**Phép thử SI**: chạy lại **đúng brief cũ**, chat mới, **2 lần**, không thêm dòng nào vào prompt; biên độ là
chênh lệch giữa hai lần đó; so mật độ với **đích của bộ mẫu** (mục 5, mục 8). Test trên cảnh mẫu có đáp án khi
nghi SI không làm việc, nhưng cảnh phải **ngoài anchor** và đổi tên — nếu không Writer chép lại chính anchor
(`references/si-test-tren-mau.md`).

Những điều đã biết, khỏi đo lại:

- Model **chép hình thức tu từ của chính SI**; anchor chứa đúng tật thì dạy lại tật. Luật đếm được (dải phần
  trăm, số lượt, 字/câu) bị đọc thành checklist. Số còn được phép trong SI là hạn mức một giọng bắt buộc phải
  xuất hiện ("once a segment at most") — đó là đếm sự kiện, không phải đo văn. Nhịp do anchor gánh
  (`references/si-anchors.md`, mục Tiệt trùng và Ma trận chức năng).
- Lời kể chiếm 70–85% văn bản. Câu "vì thế phải có nguyên tắc riêng, thiếu thì thành giọng báo cáo" là giả thuyết
  (`si-khung.md`), không phải phép thử bỏ một dòng. Trên SI manga, mọi principle đang `chưa-xác-nhận`:
  `chung/hieu-chuan/manga/gemini/principles-trang-thai.md`. Chốt cả tệp SI là Tác giả cho dùng tệp, không phải từng
  dòng đã có tác dụng, vô dụng, hay phản tác dụng. Phép thử một dòng: cùng brief, cùng anchor, bỏ đúng một khối
  chữ, hai lần chạy. Chất lượng tụt qua nhiều vòng → nghi **luật tích tụ**, cắt một dòng rồi đo, không thêm.

Đã trả giá ở `sung-thu` (05/11, KN38 — năm lượt SI vô hiệu, SI viết lại cả bản thì ra giọng, I-0059):

- **Dòng dấu câu dạy người kể đứng ngoài.** "Narration runs on full stops and commas … exclamation marks gather in
  the protagonist's inner lines" bị Writer đọc thành "lời kể chỉ dùng dấu chấm, dấu phẩy" (thinking v1). Bộ mẫu kể
  tiếng lòng trần thì FIXED 3 phải nói tiếng lòng nằm trần ngoài “”, và ？ ！ dùng ngay trong lời kể.
- **Anchor dạy giọng phải có tiếng lòng trần trong lời kể.** Anchor để câu tự nhủ trong ngoặc («“卧槽。”») dạy Writer
  đóng ngoặc tiếng lòng. Lọc anchor bằng `soat_van.py` = 0 loại oan các cửa sổ dày giọng nhất khi chính bộ mẫu có
  phủ định / so sánh trong giọng MC — đo mật độ của gốc trước khi dùng cổng đó làm bộ lọc.
- **Một biến mỗi lần để quy công, không để tìm lời giải.** ≥3 vòng một biến đều vô hiệu → lỗi do nhiều dòng cùng
  gây: viết lại cả SI từ giọng bộ mẫu, hoặc giao model khác một prompt chỉ có vấn đề + ràng buộc + đã thử
  (`sung-thu/prompt-argon.md`), rồi mới tách dòng nào ăn.
- **Đọc thinking theo từng dòng SI** (Writer hiểu dòng đó thành gì), không chỉ grep từ khoá. Đếm tiếng lòng cả trần
  lẫn trong ngoặc: chỉ số chỉ đếm ngoài “” đã bỏ sót v5 P3.
- Kết luận "prompt quyết, SI không" sau v4 là **sai**: SI Argon + brief chỉ có sự việc ra giọng (I-0060), brief Argon
  + SI cũ thì không (I-0061).

## 8. Sổ lỗi — vòng học bắt buộc

Mục này thay vòng học cũ ("thấy tín hiệu → chọn file → viết bài học"). Vòng cũ chỉ ghi **đã học gì**, không ghi
**đã thử gì, hiệu quả bao nhiêu, cái nào vô dụng** — nên sau 37 bài học, **0 can thiệp có đủ số đo**, và 14 luật
đã ghi vẫn tái phạm (`chung/loi/bao-cao.md`).

| File | Trả lời |
|---|---|
| `loai-loi.jsonl` | Có kiểu lỗi nào, mã `E-*` là gì |
| `quan-sat.jsonl` | Lần này Writer mắc lỗi đó **mấy chỗ** |
| `can-thiep.jsonl` | Đã sửa **gì, ở tầng nào, hiệu quả ra sao** |
| `muc-tieu.jsonl` | Đích của từng chỉ số, **do ai đặt** |
| `bao-cao.md` | Bảng tổng hợp — sinh tự động, không sửa tay |

Bốn lệnh cuối mỗi phiên làm truyện (mẫu đầy đủ ở `chung/loi/README.md`):

```
python tools/so_loi.py quan-sat --loi E-PROSE-03 --truyen X --doan 003 --so-lan 2
python tools/so_loi.py can-thiep --loi E-PROSE-03 --tang SI --chi-so <chỉ số> --truoc 0.6 --sau 0.1 --bien-do 0.1 --n 2
python tools/so_loi.py phan-quyet --id I-0021 --sau 0.1 --n 2
python tools/so_loi.py bao-cao && python tools/so_loi.py kiem-tra
```

Năm luật của sổ:

1. **Một lần sửa = một biến.** Cùng brief, hoặc cùng SI; đổi cả hai thì không quy được công cho cái nào.
2. **Hiệu quả đo bằng "số lần biên độ nhiễu"**: `|trước − sau| / biên độ`. ≥2 → `hieu-qua` · <1 → `vo-hieu` ·
   ngược chiều → `phan-tac-dung` · chưa đủ 2 lần chạy → `chua-ro`.
3. **Luật trong SKILL này chỉ tồn tại nếu** có một can thiệp `hieu-qua`, **hoặc** là chỉ dẫn trực tiếp của Tác
   giả. Mọi thứ khác là giả thuyết — nằm ở `review-blacklist` hoặc ở sổ. Đây là cơ chế giữ file này **ngắn lại**
   khi bằng chứng tăng, thay vì dài ra.
4. **`vo-hieu` / `phan-tac-dung` phải được gỡ ngay trong phiên đó** — gỡ dòng khỏi SI, gỡ câu khỏi brief, ghi lý
   do vào `log.md`. Một giải pháp vô hiệu để nằm lại sẽ được thêm lại lần sau bởi một Agent khác.
5. **Tác giả bác là bằng chứng hợp lệ, nhưng phải ghi nguyên văn câu bác** (`ket_luan: tac-gia-bac`); không có
   câu bác thì lần sau không ai biết vì sao nó bị bỏ.

Mỗi phiên kết bằng đọc bảng `bao-cao`: kiểu lỗi nào nhiều nhất, can thiệp nào đã đo, cái nào vô hiệu. Bảng không
đổi thì phiên này **không học được gì** — nói thẳng, đừng thêm một dòng KN cho có. Bài học tổng quát ghi vào
`chung/kinh-nghiem.md` (mục 12 `AGENT.md`), **phải trỏ tới một mã can thiệp**.

## 9. Nhiều đoạn, mở truyện, bàn giao

**Chạy N đoạn liền** — ghi hợp đồng vào đầu `log.md` rồi mới chạy: kết quả = N đoạn đã chốt + push, nối liền,
đúng dàn ý; kiểm chứng = mỗi đoạn qua cổng máy + review bằng đọc + kiểm push bằng số; **không được đổi** bible,
dàn ý, SI, glossary, luật chung (chỉ đề xuất); **dừng và hỏi** khi cần đổi canon/dàn ý, cùng một đoạn viết lại 2
lần, hết quota mọi acc, hoặc Tác giả nói "để tôi duyệt".

Mỗi đoạn trọn một vòng mục 1 rồi mới sang đoạn kế — gom cả lô thì lỗi đoạn ba kéo bốn đoạn. Lệch cấu trúc với dàn ý
(một beat không còn xảy ra được) → ghi bảng lệch, soạn lại 2–3 đoạn kế, trình Tác giả.

**Mở truyện — chốt SI trước, dựng truyện sau.** Trước `bible/` và `plot/outline.md` phải qua **bài kiểm tra SI
trên nội dung bộ mẫu**: tách chương 1, viết brief chỉ có sự việc, chạy Writer 2 lần, ghép `doc-cap` rồi **Tác giả
đọc cặp mẫu ↔ bản sinh**. **Không chấm bằng số:** con số nhịp trong SI chỉ khiến model tối ưu cho số (SI ghi
`Sentence 18–26` → bản ra 11–15 字/câu; ghi `median 15` → không đoạn nào quá 21 chữ). SI từ v6 **không có khối
LENGTH**; nhịp do **anchor** gánh, nên anchor phải có cả dòng ngắn lẫn đoạn mở ra. Quy trình:
`chung/hieu-chuan/README.md`.

Sau đó: đọc bảng truyện ở `README.md` gốc — truyện mới phải khác **trục**, không chỉ khác bối cảnh. Tác giả đã
nói thể loại / "tùy bạn" = đã chốt: dựng luôn, không mở form thứ hai. 黄金三章: 入局 → 加压 → 承诺; 300 字 đầu
có người có tên gặp nguy + hạn chót; không mở bằng sổ sách/đo đạc. Đoạn 001 chạy 3–4 bản để chọn **hình dạng
prompt**, không để chọn câu chữ; bảng số của cả các bản vào review.

**Bàn giao.** Mỗi session Writer tối đa **2 đoạn** (đoạn thứ 3 đã trôi giọng). Gói ở `<truyen>/handoff/`, ghép
bằng `python tools/build_pack.py <truyen> --prompt briefs/doan-XXX.md` thành **một tin nhắn mở session**.
Mọi quyết định phải nằm trong repo, không chỉ trong hội thoại.

## 10. Báo cáo và hỏi

Hỏi Tác giả thì nêu 2–3 phương án kèm khuyến nghị đứng đầu. Chốt đoạn thì tự commit + push; đổi canon/luật chung
thì hỏi. Commit: `doan-XXX: chốt — …` · `prompt: …` · `review: …` · `skill: …` · `so-loi: …`; tài liệu chung
commit riêng.

## Bản đồ file

| File | Khi nào đọc |
|---|---|
| `chung/loi/bao-cao.md` · `chung/loi/README.md` | đầu và cuối phiên; khi ghi sổ, khi phân vân một kết luận đã đủ bằng chứng chưa |
| `chung/review-blacklist.md` | khi review — lỗi để bắt, đối chiếu mã `E-*` |
| `brief-chi-tiet.md` · `chay-writer.md` · `git-va-ban-giao.md` | viết brief; bẫy bridge/quota/capture; push, branch, bàn giao |
| `do-va-hoc.md` | **trước khi kết luận** một lần sửa SI/prompt có tác dụng |
| `cham-diem-ban-thao.md` · `doc-bang-doc.md` | chấm và trình bày review |
| `chung/hieu-chuan/README.md` · `chung/hieu-chuan/prompt-agent-writer.md` | làn mở truyện: chốt SI, rồi vận hành Writer |
| `si-khung.md` · `si-cau-truc.md` · `si-anchors.md` · `si-test-tren-mau.md` · `si-ghi-chu.md` · `tai-dung-si.md` · `si-khong-ban-tay-vang.md` | dựng, sửa, test, tái dùng SI |
| `giong-mc-hien-dai.md` · `register-tay-huyen.md` · `mo-truyen-va-the-loai.md` · `mo-truyen-moi.md` · `sang-van.md` | giọng MC xuyên việt; xưng hô Tây huyễn; mở truyện, 黄金三章, 爽文, 骑砍 |
| `templates/brief-doan.md` · `templates/so-lieu-doan.md` | khung brief, sổ số liệu |
