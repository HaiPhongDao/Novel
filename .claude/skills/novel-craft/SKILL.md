---
name: novel-craft
description: "Làm truyện trong repo Novel: brief, chạy Writer, review, chốt, SI, mở truyện — và tự học sau mỗi phiên"
version: 2.0.0
---

# Novel Craft — Agent quản lý truyện tự cải thiện

Vai trò, phân quyền và cấu trúc thư mục nằm trong `AGENT.md` của repo — skill này không chép lại. Skill này
ghi **cách làm**: thứ tự việc, lệnh chạy được, và những bẫy đã trả giá. Mỗi luật ở đây là một câu + lý do ngắn;
số đo và câu chuyện đằng sau nằm trong `references/` (bản đồ ở cuối).

Skill này do Agent tự bảo trì (mục 9); bài học tích luỹ từ `novel-craft` 1.7 (209 lần vá).

## Khi nào dùng

- Viết brief, chạy Writer, review bản thảo, chốt/push một đoạn hay N đoạn liền.
- Soạn/sửa SI, đo SI trên mẫu, tái dùng SI cho truyện khác.
- Mở truyện mới, đổi thể loại.
- Cuối mọi phiên làm truyện → mục 9 (vòng học).

## 0. Định vị trước khi ghi một file

- Gốc repo = `git rev-parse --show-toplevel`. Có thể có nhiều bản clone trên một máy; làm ở bản có commit mới nhất
  (`git log -1 --format=%ci`) và nói rõ đã ghi ở đâu.
- Mỗi session đẩy lên một branch `ccr-*` riêng, `origin/HEAD` thường trỏ chỗ khác. Tìm branch đang làm bằng
  `git for-each-ref --sort=-committerdate refs/remotes` + `git ls-tree -r --name-only <branch> | grep <truyen>/`.
  Đưa Tác giả link theo branch (`.../blob/<branch>/...`), không tự đổi default branch.
- Tác giả hay sửa thẳng trên GitHub web: không thấy file họ nói thì `git fetch --all` rồi tìm trên remote trước khi kết luận.
- Đọc theo thứ tự: `AGENT.md` → `chung/kinh-nghiem.md` → `<truyen>/README.md` → `log.md` → `handoff/state.md` → review gần nhất.

## 1. Vòng một đoạn

1. **Trạng thái + sổ số.** Mọi con số trong brief chép từ `<truyen>/plot/so-lieu.md` (mẫu `templates/so-lieu-doan.md`); số riêng tư trong `Sổ đầu đoạn` phải gắn rõ chủ thể biết (`chỉ mình <Tên> biết`); sau khi chốt đoạn trước, quét các địa danh phụ/danh từ riêng mới do Writer vừa đặt để neo vào `Sổ đầu đoạn` hoặc `glossary.md` trước khi chạy `--new`;
   số dẫn xuất (còn lại bao nhiêu, sau N ngày) tính bằng script, không nhẩm — Writer chép nguyên số sai.
2. **Brief** ngay trước khi chạy đoạn đó, không viết trước cả lô (mục 2; khung `templates/brief-doan.md`).
   Đoạn trước chưa có bản được duyệt mà Tác giả bảo viết tiếp: nối từ bản đã sửa hết lỗi canon gần nhất, ghi
   tên bản gốc vào review + `log.md` — đoạn sau phụ thuộc vào bản đó, đổi bản gốc là phải chạy lại.
   **Cổng brief**: `python tools/soat_brief.py <brief> --prev-brief <brief trước> --bible <truyen>/bible/characters.md
   --glossary <truyen>/bible/glossary.md` (truyện mẫu B thêm `--mau-b`). CHẶN = sửa brief, không chạy — brief ghi
   sẵn kết cục, lý lẽ, nhãn tính cách thì Writer dịch nguyên thành văn (kiểm toán `test-gemini-moi`).
3. **Chạy Writer** (mục 3). Đặt tên bản theo ký tự chưa dùng ở cả `chapters/` và `chapters/archive/` — `--out` ghi đè im lặng.
4. **Cổng máy và cổng người**: `python tools/cong_doan.py <bản> --prompt <brief> [--prev <đoạn trước đã duyệt>]` và `soat_van.py` chỉ là điều kiện cần (chặn sáo rỗng, từ cấm, nhịp câu vụn). Bản đạt 34/34 điểm văn phong vẫn có thể bị loại vì "viết quá loạn xạ" do nhân vật nhảy cóc dữ kiện hoặc thiếu tương tác người thật (KN36). Đỏ = bỏ bản
   (cụt, chép mẫu), đừng đo, đừng commit. Cổng chỉ chặn hỏng rõ — không thay việc đọc. Câu cuối kết bằng `——`
   khi brief bảo dừng giữa một cú lao là cổng bắt nhầm: đọc ba dòng cuối, đủ cảnh thì giữ và ghi vào review.
5. **Review bằng đọc** (mục 4), ghi vào đúng `reviews/doan-XXX.md` của đoạn đó, kèm bảng số.
6. **Chốt**: `python tools/chot_doan.py <truyen> <spec.py>` hoặc commit + push tay; tài liệu chung commit riêng.
   **Kiểm push bằng số**: `git rev-list --count HEAD ^origin/<branch>` = 0 và `git status --short` không còn `?? <truyen>/`
   (thư mục truyện mới là untracked — commit vẫn thành công mà không có truyện).
7. **Báo cáo** 3–5 dòng: số chữ, diễn biến, verdict, link GitHub. Không dán cả bản 2.000 字 vào chat. Khi so với mẫu
   hay Tác giả chưa thấy chữ nào của bản nháp, kèm 2–3 cặp trích (nguyên văn ↔ bản sinh).
8. **Vòng học** (mục 9).

Đoạn hỏng → `git mv` vào `archive/`, sửa brief, chạy lại bằng chat mới (`--new`); không bảo Writer "viết lại" trong
cùng chat — nó chép lại 77% bản cũ của chính nó.

## 2. Luật brief (luôn áp dụng)

- **Ngắn ở phần dặn cách viết, cách ly Writer khỏi raw State JSON.** Dữ kiện thiết lập (thân phận, xưng hô, nơi chốn, số đang chạy) nằm trong State JSON — đây là bộ nhớ của Agent, tuyệt đối không dán raw JSON vào brief; brief chỉ rút 1–2 sự thật sống của cảnh đó thành 3–5 câu tiếng Việt tự nhiên. Nhồi quá nhiều việc hoặc dán raw JSON khiến Writer chạy theo checklist, kích hoạt chế độ mặc định của LLM (so sánh sáo rỗng, phình độ dài). Đặc biệt ở **đoạn mở đầu (001)**, tuyệt đối không dán cả gói Canon/State/Voice đồ sộ vào prompt: model bị ngộ độc dữ liệu sẽ biến nhân vật thành máy đọc checklist, vừa gặp đã xả liên thanh toàn bộ số liệu và giải mã kịch bản, làm văn nhảy cóc và loạn xạ (KN35).
- **Ma sát thật phải xuất phát từ hành vi vật lý, không phải thuyết trình.** Tạo xung đột bằng vật trao tay (tiền thối, lon cà phê, vết mực trên ngón), thái độ nghi ngờ nghề nghiệp, và mồi nhử một điểm nhỏ. Tuyệt đối không soạn sẵn lý lẽ chê bai hay để MC diễn thuyết giảng đạo; để hình ảnh trên bản vẽ tự thuyết phục người xem.
- **Brief mở bằng "Viết tiếp đoạn tiếp theo…" và chỉ ghi chỗ dừng.** "Mở ngay sau câu X" hay mục "Mở" làm Writer
  dựng lại cảnh như chương mới; chỗ mở đã là đuôi đoạn trước trong gói.
- **Viết tiếng Việt câu đầy đủ, tên Latin, danh xưng đủ chữ** ("phủ lãnh chúa", "cô có hai thợ phụ"); hạn chế chữ Hán,
  để Writer tự đặt tên vật. Gạch đầu dòng cụt và chữ rút gọn được dịch thành từ lạ: "phủ" → 官邸 dùng như bộ máy,
  máy dịch ra "biệt thự định giá". Glossary phải có từ cho cả nơi ở, bộ máy cai trị, **đơn vị đo và thể chế** — thiếu thì Writer lấy 六合/磅, 公国/行省 của Tàu (KN34).
- **Không dặn "đáp bằng phép tính"** — Writer ném nguyên bài toán vào văn; đưa con số như sự thật của cảnh.
- **Khối nối tiếp do gói cấp** (`build_pack.py` dán đuôi đoạn trước; truyện cũ dùng `noi_doan.py`): 7–10 dòng cuối (~150–200 字) của bản **đã duyệt** (`python tools/noi_doan.py <đoạn-trước> --chars 300 --wrap`),
  câu "viết tiếp từ đây, không chép lại câu nào", rồi mô tả bằng tiếng Việt chỗ dừng + việc đang treo. Chép khối này bằng script, không gõ lại tay — gõ lại làm lệch nguyên văn, Writer nối lệch. Thiếu khối này thì 5/5 mối nối đứt.
- **Không câu tiếng Trung nào trong brief** ngoài tên riêng/thuật ngữ ngắn — Writer chép nguyên làm mở đoạn, mọi điểm thành điểm giả.
- **Không đánh số beat, không giao nội dung từng lượt thoại** — giọng chết ở prompt. Số lượt và độ dày thoại do phạm vi
  thời gian + số người có mặt quyết; muốn thoại dày thì mở phạm vi, thêm người.
- **Khẳng định, không liệt kê cấm**: tối đa một câu phủ định — ba vế "không A, không B" ra đúng khuôn phủ định trong văn.
- **Ranh giới viết ra**: "việc X thuộc đoạn sau" + trạng thái sự thật; thiếu thì Writer mở tuyến của đoạn 6–8 ngay đoạn 1.
- **Độ dài là con số của brief**, không của SI: chép nguyên cửa sổ Tác giả chấp nhận, không đặt sàn (model đệm cho qua sàn).
  Khi Tác giả nói độ dài tuỳ beat, số 字 chỉ là thông tin trong báo cáo.
- **Khối định dạng 【】 chép nguyên cả dòng**; câu ngay sau khối chỉ nói con số đáng gì, rồi một việc anh làm tiếp.
  Ghi sẵn nghĩa của số đó bằng một câu sự thật ("74, còn thiếu 26 để đào tạo một 村民") — để trống thì người kể
  tự đặt mốc và đặt sai (gọi phần thiếu cho 村民 là `进阶`).
- **MC trong lane xuyên việt**: đúng một dòng sự thật trơn (`X là người xuyên việt.`), không nghề cũ, không "chỗ thắng",
  không gán tính cách — tính cách do Writer quyết.
- **Mẫu là truyện xuyên việt mà MC của mình không xuyên** → brief phải có một dòng `X sinh ra ở thế giới này.`; bible
  ghi thôi không đủ — Writer kéo motif xuyên không của mẫu vào ("上辈子", "从地球穿越") ngay khi brief im lặng.
- **Giọng xuyên việt sống nhờ dòng chức năng giọng ở đầu prompt** (khung đặt hàng của Tác giả: độ dài · tag ·
  "mượn lời MC phán xét cũ/mới"), không nhờ dòng sự thật ở cuối brief bảng việc. Tác giả đưa khung thì dùng nguyên.
- **Một đoạn = một tình huống; dữ kiện ghi là "bối cảnh để giữ cho đúng, không cần kể hết".** Giao cả chuỗi sự
  kiện của chương trong ~2.000 字 thì Writer kể mỗi dữ kiện thành một dòng rồi qua việc kế — Tác giả đọc ra
  "checklist, không có khoảng trống" (đoạn kể ≥40 字: 0 → 19 khi chỉ còn một tình huống và dừng sớm). Đo:
  `references/brief-chi-tiet.md` cuối file.
- **Bible là nguồn canon**, không phải README; thấy lệch thì báo Tác giả.

Chi tiết + số đo: `references/brief-chi-tiet.md`, `references/si-cau-truc.md` mục 5–8.

## 3. Chạy Writer

```
python tools/aistudio_run.py --new --si <truyen>/gemini/si-dan-gemini.txt --prompt <truyen>/briefs/doan-XXX.md --out <truyen>/chapters/doan-XXX-<bản>.md
```

- `--si` nhận nguyên file: tách phần dán (giữa `===== BẮT ĐẦU SI =====` và `===== HẾT SI =====`) ra file riêng.
- Cần Edge mở + extension "Novel AI Studio bridge" (`tools/aistudio-ext`, cổng 127.0.0.1:8765 do chính script mở —
  đừng curl để thử bridge). Một đoạn mất 2–7 phút: **chạy nền** (Bash `run_in_background`), chờ thông báo, đừng poll;
  trong lúc chờ thì viết brief kế.
- Đừng sửa `tools/aistudio-ext/` khi có job chạy (extension tự reload, job treo tới timeout). Nghi bridge hỏng →
  probe 1 dòng SI + 1 dòng prompt, `--out tools/.probe/out.md`.
- **Nhiều bản cùng lúc**: `--batch jobs.json` ([{si, prompt, out, note?, model?, thinking?}]), mỗi tài khoản /u/0–2 một tab.
  Edge nạp extension từ `D:\ClaudeCode\aistudio-ext` (bản chép): sửa extension thì chép sang đó. AI Studio đang để chat
  tạm (URL giữ `new_chat`), nên **gửi tiếp vào chat cũ không được** — đoạn kế chạy `--new` kèm tiền tình + nguyên văn cuối đoạn trước.
- `Failed to generate content` / `No tab with id` là lỗi tạm: chạy lại y nguyên lệnh sau 20–45 giây.
- "Extension không nhận việc sau 90s" sau một lần bị cắt → tiến trình cũ giữ cổng 8765: `netstat -ano | grep :8765`, `Stop-Process`.
- Job treo >10 phút không file = tab rơi về trang đăng nhập Google: nhờ Tác giả đăng nhập, đừng sửa script.
- `LỖI: No current window` = Edge chỉ còn tiến trình nền (startup boost), không có cửa sổ: mở một cửa sổ
  (`Start-Process msedge -ArgumentList '--new-window','about:blank'`) rồi chạy lại y nguyên lệnh.
- Quota: script xoay `/u/0 → /u/1 → /u/2`, ghi vào `tools/.aistudio_state.json`; đọc dòng `Google Account:` để biết acc nào.
  Số `/u/N` ứng với tài khoản khác nhau trên mỗi máy — ghi quota theo email trong `log.md`, đừng theo số.
- Extension được nạp từ thư mục ghi trong Edge (`Secure Preferences` → `path`), có thể là bản chép ngoài repo
  (máy này: `D:\ClaudeCode\aistudio-ext`). Script tính hash từ `tools/aistudio-ext/` nên sửa trong repo vẫn làm
  extension reload — nhưng nạp lại **code cũ**: sửa xong phải chép sang thư mục Edge nạp (giữ bản cũ để lùi).
- Tài khoản bị từ chối quyền: lỗi in ngay trong lượt Model, không ở thanh thông báo; extension (từ 26/10) đọc lỗi đó,
  xếp như hết quota và script xoay `/u/` kế tiếp. Vẫn treo → thử logic trên trang giả trước khi đụng tài khoản thật.
- Bản ra không có dòng trống giữa đoạn: lưu raw vào `archive/`, chèn dòng trống trước dòng bắt đầu bằng `　　` (chỉ đổi khoảng trắng).
- `--think-out <truyen>/archive/thinking-XXX.md` khi nghi SI bị hiểu sai — đọc thinking trước khi sửa SI.

Chi tiết: `references/chay-writer.md`.

## 4. Đo và review

- **Số đo là cổng, không phải điểm.** Một bản 88/100 từng là ba câu Agent dán vào prompt. Số dùng để: bắt chép mẫu,
  kiểm canon/số học, soát hồi quy khi sửa SI. Phán chất lượng bằng đọc: mở/giữa/kết × (ai muốn gì · cái gì đổi ·
  câu đáng nhớ · chỗ người đọc bỏ qua), đặt cạnh mẫu — `references/doc-bang-doc.md`.
- Công cụ: `tools/soat_van.py [--list]` (tật văn, bốn cột thoại), `tools/cham_doan.py --prompt <brief> --numbers "…" [--modern]`,
  `.claude/skills/novel-craft/scripts/do_nhip_cau.py` (nhịp câu). Band của `cham_doan` là của lane 领主 — truyện có register
  hay cửa sổ độ dài riêng thì báo cột số thật, nói rõ cột nào là nhiễu; 爽文 không chấm bằng band này.
- **Cột 0 không phải bằng chứng sạch**: grep tay `如.{1,8}般|如铁|如鹰` và `(平静|冷冷|淡淡|轻声)地(说|道|命令|问|开口)` trước khi báo ĐẠT.
- **Đo nhiễu trước khi nhận công**: cùng SI + prompt đã ra 0 và 5 cặp phủ định. Quy về mật độ/1.000 字, chỉ ĐẠT khi ra khỏi
  biên độ hai lần chạy y hệt. Tật sinh từ đoạn nền/nội tâm, không từ số 字.
- **Bản Tác giả khen có phần là lượt may**: cùng prompt + SI chạy lại không ra lại được chất lượng đó; đừng coi prompt ấy là công thức chắc, so ít nhất một lần chạy lại.
- **Lỗi tầng luật chứng minh bằng một lần chạy Writer** cùng brief cũ ở chat mới, không bằng bản Agent sửa tay.
- **Tác giả nói "ngang nhau / đều đạt" là hết vòng tối ưu** — chốt một bản, ghi log, sang đoạn kế.
- **Tác giả chọn bản khác bản mình khuyên → lấy bản của họ làm gốc.**
- Tật register/xưng hô sửa ở ba tầng: glossary (bảng tra) + SI (luật cho nó xuất hiện) + một dòng prompt — `references/register-tay-huyen.md`.

Chi tiết: `references/do-va-hoc.md`, `references/cham-diem-ban-thao.md`.

## 5. SI của truyện

- **Lời kể (70–85% văn bản) phải có nguyên tắc + anchor riêng, đứng trước mọi cảnh đặc biệt** — SI chỉ dạy cảnh đặc biệt thì Writer kể bằng giọng báo cáo và thoại nhiễm theo (`references/si-khung.md`, `writer/SI-template` v5).
- Sửa SI phải có Tác giả duyệt + ghi `log.md`. Dựng SI mới từ `writer/SI-template` v5 — **phần dán ≤ 8.000 ký tự, 4–5 anchor,
  PART 2 ≤ 8 dòng, 5 dòng BANS gọi tên lớp tật, không liệt kê từ, không nhắc máy soát** (Writer né regex bằng từ họ hàng:
  实 → 整整/死死); giữ mọi đời cũ `system-instruction-vN.md`.
- **Lỗi mới không tự thành luật SI**: do brief/dữ kiện → sửa brief/glossary; gặp một lần → review-blacklist; lặp ≥2 lần
  chạy với brief khác nhau → một dòng PART 2 **thay** một dòng cũ (template v5 hướng dẫn 6).
- **Chất lượng tụt qua nhiều vòng thì nghi luật tích tụ**: đo độ dài SI và prompt qua các đời; nếu cùng phình thì reset về
  SI lõi và từ đó sửa bằng **cắt** một luật, không thêm — `references/si-cau-truc.md` mục 10.
- Model chép hình thức tu từ của chính SI (chuỗi phủ định trong SI ra chuỗi phủ định trong văn).
- Luật nhịp viết cả sàn và trần; luật dạng đếm được thì model đọc thành checklist — trừ khi cần một giọng **xuất hiện**
  (câu tự giễu, câu châm): khi đó phải cho hạn mức đếm được.
- Lệnh cấm đo từ chính bộ mẫu (thẻ thoại, số dòng bảng…), không chép từ đời SI hay truyện khác.
- **Dấu hiệu đếm được dày trong mẫu có thể chỉ dồn ở một loại cảnh** — xem nó ở đâu trước khi nâng thành luật (`references/si-cau-truc.md`).
- **Danh sách ví dụ trợ từ (呢, 吧…) trong luật thoại bị Writer nhồi vào mọi lượt**; bỏ một chữ khỏi danh sách không đủ — phải có hạn mức (phần lớn lượt không trợ từ, 呢 ≤2/đoạn). Luật thẻ thoại, thước chủ ngữ, số đo: `references/si-cau-truc.md` mục 12–13.
- Không bịa anchor; kiểm bằng `scripts/verify_anchors.py` — `references/si-anchors.md`.
- Nghi SI "không làm việc" → test trên cảnh mẫu có đáp án, hai cảnh khác loại — `references/si-test-tren-mau.md`.
- Tác giả gửi link SI: repo private, đọc từ bản clone và nói rõ đời nào (+3–4 khác biệt).
- **Test một lỗi Tác giả bảo sửa: 3 hướng khác nhau, mỗi hướng 1 bản, chỉ gửi 3 bản** (vd luật trong SI / neo nguyên văn
  bộ mẫu / dồn vào prompt). Máy soát trước (tên lọt, số, thước đo của lỗi đó); bản chưa qua máy thì chạy lại, không gửi.
  Tác giả đọc tối đa ~4 bản một vòng; 10–12 bản (2 lần × mỗi biến thể) là quá nhiều (27/10, ky-kham-lanh-chua).

Chi tiết: `references/si-ghi-chu.md`, `references/tai-dung-si.md`, `references/si-khong-ban-tay-vang.md`, `references/giong-mc-hien-dai.md`.

## 6. Mở truyện, thể loại

- Đọc bảng truyện ở `README.md` gốc trước: truyện mới phải khác **trục**, không chỉ khác bối cảnh.
- Tác giả đã nói thể loại / "tùy bạn" = đã chốt: dựng luôn (bible → SI → đoạn 001), không mở form thứ hai.
- 黄金三章: 入局 → 加压 → 承诺; 300 字 đầu có người có tên gặp nguy + hạn chót; không mở bằng sổ sách/đo đạc.
- Đoạn 001: chạy 3–4 bản để chọn **hình dạng prompt**, không để chọn câu chữ; bảng số của cả các bản vào `reviews/doan-001.md`.
- Mỗi thể loại một SI dựng từ dấu hiệu đo được của bộ mẫu; mẫu tải về có thể hỏng — đếm thân chương trước.
- **Dàn ý sau đoạn mở cũng bám từng chương bộ mẫu**: mỗi đoạn một màn phô diễn → người chứng kiến hiểu sai theo cách
  nghĩ của họ → MC thắng thấy rõ, một con số lớn. Đoạn chỉ có mua bán, ký kết, đếm sổ thì Tác giả đọc ra "bình bình,
  một đống thiết lập" dù văn sạch; luật bible chặn công nghệ đi nhanh là nguyên nhân gốc — chặn bằng giá, đừng chặn bằng nhịp.
- **Đoạn mở lane xuyên việt: chép thứ tự của chương 1 bộ mẫu, không dựng cảnh tỉnh dậy** (骑砍: nơi chốn → bao
  lâu → bảng → một nhận định tự giễu → số liệu → cảnh đang chạy). Đưa nghề kiếp trước vào prompt thì Writer nhắc lại
  2–8 lần/bản. Thứ tự đầy đủ + prompt chạy được: `references/mo-truyen-va-the-loai.md`.

Chi tiết: `references/mo-truyen-va-the-loai.md`, `references/mo-truyen-moi.md`, `references/sang-van.md`.

## 7. Chạy N đoạn liên tiếp — hợp đồng

Khi Tác giả nói "chạy tiếp N đoạn", ghi hợp đồng vào đầu `log.md` của lượt đó (kiểu `/goal` của Hermes) rồi mới chạy:

| Ô | Nội dung mặc định |
|---|---|
| Kết quả | N đoạn mới đã chốt + push, nối liền nhau, đúng dàn ý |
| Kiểm chứng | mỗi đoạn: `cong_doan.py` xanh + review bằng đọc ĐẠT/SỬA NHẸ + kiểm push bằng số |
| Không được đổi | bible, dàn ý, SI, glossary, luật chung (chỉ đề xuất) |
| Phạm vi | thư mục truyện đó + `log.md`; tài liệu chung commit riêng |
| Dừng và hỏi khi | cần đổi canon/dàn ý; cùng một đoạn VIẾT LẠI 2 lần; hết quota mọi acc; Tác giả nói "để tôi duyệt" |

Mỗi đoạn trọn một vòng mục 1 (brief → chạy → cổng → review → push) rồi mới sang đoạn kế — gom cả lô thì lỗi đoạn ba
kéo bốn đoạn. Độ dày mỏng dần qua các đoạn là thật: cửa sổ độ dài và tỷ lệ thoại/lời kể ghi ở mọi brief.
Lệch cấu trúc với dàn ý (một beat không còn xảy ra được) → ghi bảng lệch, soạn lại 2–3 đoạn kế, trình Tác giả.

## 8. Báo cáo và hỏi

- Hỏi Tác giả: bối cảnh đủ trả lời ngay, 2–3 phương án, khuyến nghị đứng đầu.
- Chốt đoạn thì tự commit + push, không hỏi lại; đổi canon/luật chung thì hỏi.
- Kết luận không ghi vào file thì mất: verdict + bảng số + quyết định vào `reviews/` và `log.md` trước khi push.

Chi tiết: `references/git-va-ban-giao.md`.

## 9. Vòng học cuối phiên (bắt buộc)

Chạy khi: chốt xong một đoạn/lô, Tác giả sửa lưng, hoặc trước khi kết thúc phiên làm truyện. Đây là bản tay của
background review của Hermes.

1. **Quét tín hiệu** trong phiên — một tín hiệu là đủ để phải ghi:
   - Tác giả chê văn, cách làm, cách báo cáo ("đừng…", "lại thế", "không có cảm xúc") — tín hiệu mạnh nhất.
   - Một cách làm/fix/lệnh mới chạy được sau khi cách cũ hỏng.
   - Một luật trong skill này hoặc trong `chung/` tỏ ra sai, thiếu bước, lỗi thời.
2. **Chọn chỗ ghi**, cái đầu tiên phù hợp:
   1. Sửa đúng câu sai/thiếu trong `SKILL.md` này (luật luôn áp dụng) — sửa tại chỗ, không viết "UPDATE:" bên dưới.
   2. Mở rộng một `references/<chủ đề>.md` đã có (chi tiết, số đo, bảng).
   3. Phát hiện về **cách viết truyện** dùng chung cho mọi Agent (Codex, Hermes) → `chung/kinh-nghiem.md` theo mục 12 `AGENT.md`.
   4. Sự thật riêng một truyện (tên, số, quyết định) → bible/log của truyện đó, **không** vào skill.
3. **Cách viết một bài học**: luật tổng quát dạng mệnh lệnh + một vế "vì sao" (cơ chế), gắn vào bước nó ảnh hưởng.
   Đọc lại chỗ định ghi trước — đã có thì làm mạnh câu cũ, không thêm bản thứ hai. Không ghi ngày, số commit, câu
   trích dài; số đo chỉ giữ khi nó là bằng chứng của luật (và đặt ở reference, không ở `SKILL.md`).
4. **Không ghi**: lỗi môi trường đã tự khỏi (chạy lại là được), câu kiểu "công cụ X hỏng", chuỗi thử thất bại chưa tìm
   ra cách đúng, việc một lần.
5. **Giữ dáng**: `SKILL.md` dưới ~20.000 ký tự (`wc -m`); vượt thì đẩy chi tiết sang reference. Không tạo reference
   theo ngày/sự cố. "Không có gì để ghi" là được, nhưng không phải mặc định.
6. Commit riêng: `skill: <điều vừa học>` và push cùng lượt.

## Bản đồ references

| File | Khi nào đọc |
|---|---|
| `brief-chi-tiet.md` | viết brief, nhất là khi bản ra lệch canon/số/mối nối |
| `chay-writer.md` | lỗi bridge, quota, capture cụt, chuẩn hoá dòng trống |
| `do-va-hoc.md` | trước khi kết luận một lần sửa SI/prompt có tác dụng |
| `cham-diem-ban-thao.md` · `doc-bang-doc.md` | chấm và trình bày review |
| `si-cau-truc.md` | khung SI, vòng thử–đo, thoại, nhịp, reset SI |
| `si-khung.md` · `si-anchors.md` · `si-test-tren-mau.md` | dựng SI mới, anchor, test trên mẫu |
| `si-ghi-chu.md` · `tai-dung-si.md` · `si-khong-ban-tay-vang.md` | sửa/tái dùng SI, truyện không hệ thống |
| `giong-mc-hien-dai.md` · `register-tay-huyen.md` | giọng MC xuyên việt; xưng hô, tước, tên riêng Tây huyễn |
| `mo-truyen-va-the-loai.md` · `mo-truyen-moi.md` · `sang-van.md` | mở truyện, 黄金三章, 爽文, 骑砍 |
| `git-va-ban-giao.md` | push, branch, bàn giao session |
| `templates/brief-doan.md` · `templates/so-lieu-doan.md` | khung brief, sổ số liệu |
