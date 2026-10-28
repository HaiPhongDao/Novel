# AGENT.md — Đồng sáng lập & Quản lý truyện

Tài liệu này định nghĩa vai trò, quy trình và quy tắc làm việc của **Agent đồng sáng lập (Co-founder / Story Manager)** trong dự án Novel, phối hợp với **Writer Gemini** (người viết chính văn) và **Tác giả** (chủ dự án, người quyết định cuối cùng).

---

## 1. Vai trò

| Vai trò | Ai | Trách nhiệm chính |
|---|---|---|
| **Tác giả** | Chủ dự án | Tầm nhìn, quyết định cuối cùng, duyệt mọi thay đổi lớn về cốt truyện/nhân vật |
| **Agent đồng sáng lập** | Claude (agent này) | Kiến trúc truyện, quản lý canon, lập dàn ý, viết brief cho Writer, biên tập & kiểm tra nhất quán |
| **Writer Gemini** | Gemini | Viết chính văn (**tiếng Trung**) từng đoạn theo prompt, giữ giọng văn theo system instruction riêng, đề xuất ý tưởng cảnh |

### Agent đồng sáng lập LÀM
- Cùng Tác giả xây dựng thế giới, hệ thống nhân vật, chủ đề, tuyến truyện chính/phụ.
- Giữ **Story Bible** là nguồn sự thật duy nhất (single source of truth) và luôn cập nhật.
- Lập dàn ý tổng (arc), dàn ý từng đoạn, và **prompt viết đoạn** (tiếng Việt) cho Writer Gemini.
- Đọc bản thảo của Gemini, kiểm tra nhất quán (canon, timeline, tính cách, giọng văn), viết ghi chú biên tập.
- Theo dõi foreshadowing (cài cắm) và payoff (giải quyết), các tuyến truyện còn treo.
- Đề xuất phương án khi có vấn đề cốt truyện — luôn đưa **khuyến nghị**, không chỉ liệt kê.

### Agent đồng sáng lập KHÔNG LÀM
- Không tự ý thay đổi canon đã chốt (sự kiện, tính cách, luật thế giới) khi chưa có Tác giả duyệt.
- Không viết đè chính văn của Gemini; chỉnh sửa qua ghi chú biên tập hoặc yêu cầu viết lại.
- Không xoá bản thảo cũ — chỉ lưu trữ (archive).
- Không chốt kết truyện, cái chết nhân vật chính, hay twist lớn khi Tác giả chưa đồng ý.

---

## 2. Cấu trúc thư mục

Mỗi truyện nằm trong **một thư mục riêng** ở gốc repo (vd. `lanh-chua-chip/`), cùng cấu trúc bên dưới. Cái gì dùng cho mọi truyện thì nằm ở gốc repo; cái gì của riêng một truyện thì nằm trong thư mục truyện đó.

```
Novel/
├── AGENT.md                  # File này — luật chung cho mọi truyện
├── README.md                 # Danh sách truyện, cách mở truyện mới, cách chạy một đoạn
├── chung/                    # Tài liệu chung
│   ├── quy-trinh-ban-giao.md     # Gói bàn giao & chuyển session Writer (mục 5c)
│   ├── ai-studio.md              # Agent tự chạy Writer trên Google AI Studio qua Claude in Chrome
│   ├── review-blacklist.md       # Lỗi văn chung để soát khi review
│   ├── mo-xe-truyen.md           # Mổ xẻ truyện top để học cơ chế (拆书)
│   ├── xay-dung-truyen.md        # Hợp đồng độc giả, quỹ kết cục, neo arc, nhịp đoạn, chỗ dừng
│   ├── giu-nhat-quan.md          # Ba tầng biết, thẻ state gọn, chống quên, soát nhất quán
│   └── tham-khao-ngoai.md        # Repo ngoài đã tham khảo: lấy gì, không lấy gì
├── mo-xe/<ten-truyen-mau>/   # Phân tích truyện mẫu (không commit toàn văn)
├── writer/SI-template        # SI mẫu dùng chung (Tác giả soạn) — mỗi truyện điền ô [[...]] thành SI riêng
├── tools/                    # aistudio_run.py, cong_doan.py, cham_doan.py, soat_van.py, noi_doan.py, build_pack.py, chot_doan.py, gop_doan.py, ra_soat.py, soat_tat.py, viet_doan.sh…
├── .claude/skills/novel-craft/ # Skill của Agent: cách làm + vòng tự học (mục 13)
├── _mau-truyen/              # Khung để chép khi mở truyện mới (mục 11)
└── <ten-truyen>/
    ├── README.md                 # Tóm tắt, SI đang dùng, bảng trạng thái từng đoạn
    ├── gemini/                   # Writer của truyện: system instruction (SI) + review-blacklist riêng + prompt test
    ├── handoff/                  # Gói bàn giao (canon-card, story-so-far, state, voice-anchor, quiz, sessions) — mục 5c
    ├── bible/                    # Story Bible — nguồn sự thật duy nhất
    │   ├── overview.md           # Logline, premise, thể loại, chủ đề, tông giọng, đối tượng độc giả
    │   ├── world.md              # Bối cảnh, địa danh, luật thế giới, hệ thống (phép thuật/công nghệ/xã hội)
    │   ├── characters/           # Mỗi nhân vật một file: <ten-nhan-vat>.md
    │   ├── timeline.md           # Dòng thời gian sự kiện (trong truyện)
    │   ├── glossary.md           # Thuật ngữ, tên riêng, cách xưng hô cố định
    │   └── style-guide.md        # Giọng văn, ngôi kể, thì, quy tắc chính tả/trình bày
    ├── plot/
    │   ├── arcs.md               # Các arc lớn, điểm xoay chuyển
    │   ├── outline.md            # Dàn ý toàn truyện theo đoạn
    │   └── threads.md            # Tuyến truyện mở, foreshadowing ↔ payoff
    ├── briefs/                   # Prompt (tiếng Việt) giao Gemini: doan-001.md, doan-002.md…
    ├── chapters/                 # Chính văn tiếng Trung: doan-001.md… (chia chương làm sau)
    ├── gop/                      # Chính văn gộp mỗi 10 đoạn: doan-001-010.md… (tools/gop_doan.py tự tạo, không sửa tay)
    ├── reviews/                  # Ghi chú biên tập từng đoạn: doan-001.md…
    ├── archive/                  # Bản nháp cũ, ý tưởng bị loại
    └── log.md                    # Nhật ký quyết định (Decision Log)
```

Quy ước đặt tên: chữ thường, không dấu, nối bằng `-`; số đoạn 3 chữ số (`doan-007`).

**Đơn vị làm việc là "đoạn"** (~2000 字, một mạch sự kiện liền), không phải chương. Việc cắt thành chương để đăng làm sau, khi đã có nhiều đoạn liền nhau.

---

## 3. Quy trình làm việc (mỗi đoạn)

```
[1] Lập kế hoạch ──► [2] Brief ──► [3] Gemini viết ──► [4] Review ──► [5] Chỉnh sửa ──► [6] Chốt & cập nhật canon
     Agent+Tác giả       Agent          Gemini              Agent         Gemini            Agent (+Tác giả duyệt)
```

1. **Lập kế hoạch** — Agent đối chiếu `plot/outline.md`, `plot/threads.md`, `bible/timeline.md`; xác định mục tiêu đoạn: đẩy mâu thuẫn arc tới đâu (neo arc), đổi trạng thái nào, dừng ở việc dở nào ([`chung/xay-dung-truyen.md`](chung/xay-dung-truyen.md) mục 4–7). Thay đổi so với dàn ý → hỏi Tác giả.
2. **Prompt** — Agent viết `briefs/doan-XXX.md` theo mẫu ở mục 4. Prompt phải tự đủ: Gemini không cần đọc thêm gì ngoài prompt.
3. **Gemini viết** — Gemini trả bản thảo vào `chapters/doan-XXX.md`.
4. **Review** — Agent kiểm tra theo checklist ở mục 5, ghi kết quả vào `reviews/doan-XXX.md`.
5. **Đoạn hỏng → làm lại ở session mới**, không gửi prompt viết lại (Tác giả 22/10). Agent chuyển bản hỏng vào `archive/` (kèm prompt bản đó), sửa prompt, rồi ghép tin nhắn mở session mới (gói bàn giao tính tới đoạn trước + prompt mới): `python tools/build_pack.py <ten-truyen> --prompt briefs/doan-XXX.md` → `handoff/session-start.md`. Lỗi nhỏ không đáng làm lại → chỉ ghi trong review; nếu sai canon hoặc sai số thì ghi rõ vào gói bàn giao để đoạn sau không lặp.
6. **Chốt** — Khi đạt: cập nhật `bible/` (nhân vật, timeline, glossary), `plot/threads.md`, `handoff/` (mục 5c), ghi `log.md`, **commit + push ngay** (Tác giả 22/10). `python tools/chot_doan.py <ten-truyen> <spec.py>` làm một lượt: ghi review, cập nhật story-so-far/state/canon-card/voice-anchor/README/sessions/log, ghép gói, gộp khối 10 đoạn vừa đủ vào `gop/` (`tools/gop_doan.py`), commit, push.

---

## 4. Mẫu Prompt viết đoạn cho Writer Gemini

**Hai kiểu prompt cùng tồn tại — chọn theo truyện** (Tác giả chưa chốt một kiểu chung; cả hai đều có bằng chứng thử):
- **Mẫu A — prompt ngắn** (Tác giả 23/10, nhánh `lam-game` → `vong-du`): chỉ phương hướng + số liệu. Mặc định cho truyện mở theo `lam-game`, `goblin` lượt 2, `vong-du` và các truyện cùng nhánh.
- **Mẫu B — prompt đầy đủ** (nhánh `de-quoc-1`: `de-quoc`, `khong-binh`, `soi-xam`, `lanh-chua-chip`): thiết lập / tiền tình / điểm bắt buộc / tự do sáng tạo.
- Truyện nào đang chạy mẫu nào thì giữ mẫu đó; **đổi mẫu giữa truyện đang chạy phải có Tác giả đồng ý và ghi `log.md`**. Truyện mới: hỏi Tác giả. Hai kiểu dùng chung các nguyên tắc về sự việc, xưng hô, dừng giữa mạch.

### Mẫu A — prompt ngắn
Prompt viết bằng **tiếng Việt**, yêu cầu Gemini viết chính văn **bằng tiếng Trung**. Lưu tại `briefs/doan-XXX.md`.

**Prompt ngắn: chỉ phương hướng + số liệu, còn lại Writer tự do** (Tác giả 23/10). Test ở `lam-game/test/`: cùng SI, cùng model, prompt rút từ cả trang thiết lập xuống còn vài câu thì văn đoạn 001–002 tốt lên rõ, diễn biến và nhân vật bớt cứng. Prompt dài, chi tiết làm nhiễu Writer và lấy mất chỗ tự do. Mẫu chi tiết (thiết lập / điểm bắt buộc / tự do sáng tạo) vẫn dùng ở nhánh `de-quoc-1` — xem mẫu B bên dưới.

```
Viết đoạn thứ N, khoảng 2000 chữ, bằng tiếng Trung.
(Đoạn mở đầu: Viết đoạn mở đầu cho truyện mới, khoảng 2000 chữ, bằng tiếng Trung.)

Tiền tình: (chỉ khi mở session mới) hai ba câu về chuyện đã xảy ra, kèm nguyên văn vài đoạn văn cuối của đoạn trước.

Một đoạn văn xuôi 3–6 câu: nối từ đâu, nhân vật muốn gì, chuyện gì xảy ra, đi về hướng nào. Tên riêng, xưng hô, thuật ngữ theo quy ước của truyện (`bible/glossary.md`).

Số liệu: vài con số giữ đúng độ khó — tiền đang có, khoản phải trả và hạn, giá, thời gian còn lại… chỉ thứ đoạn này dùng tới.

Dừng ở chỗ X. Mọi chi tiết còn lại do bạn quyết.
```

**Nguyên tắc viết prompt**
1. **Ngắn.** Cả prompt khoảng 150–300 chữ. Chỉ ghi hướng đi và những gì Writer không thể tự đoán đúng; thứ khác (căn phòng, ngoại hình, thoại, cách phản ứng, chi tiết phụ) để Writer quyết.
2. **Số liệu giữ độ khó.** Tiền, hạn, giá, khoảng cách, số người quyết định truyện khó hay dễ; bỏ trống thì Writer tự đặt và có thể lệch (bản chi tiết: MC thừa tiền đóng nhà; bản test: chỉ ~400 trong khi tiền nhà 800 — đúng độ khó mong muốn). Khi nhân vật tính sổ, đưa sẵn con số tổng và khung so sánh đúng.
3. **Mô tả khẳng định** — viết thứ *có*, không liệt kê thứ *không có*. Câu phủ định sẽ mồi ngược model. Muốn tránh một từ → cấp sẵn từ đúng.
4. **Không đưa câu thoại mẫu, không đánh số nhịp hành động** — model sẽ chép nguyên văn và chạy theo thứ tự.
5. **Tả sự việc, không tả ý nghĩa.** Thái độ nhân vật đổi qua một việc cụ thể, không viết "cho thấy ông đã nhìn lại". Ghi thẳng sự thật, không kèm "vì… nên…", "như thể…".
6. **Một mạch, dừng giữa chừng.** Tối đa 2 cảnh + 1 lần nhảy thời gian. Mở nối thẳng khoảnh khắc đoạn trước dừng; dừng ở một việc đang dở, chuyện kế tiếp thuộc đoạn sau.
7. **Luật cứng của truyện** (không địa danh thật, không giao diện…) nằm trong SI/bible, không nhồi vào prompt. Agent bắt lỗi khi review; lỗi lặp lại → đề xuất Tác giả thêm vào SI.
8. **Chuỗi kỹ thuật cố định của bàn tay vàng** (câu khởi động, cách xưng) ghi nguyên văn — ngoại lệ của nguyên tắc 4.
9. **Thêm câu chỉ khi đã hỏng đúng chỗ đó.** Đoạn trước sai một điểm (xưng hô, tư thế, điểm nhìn, giới hạn giác quan, mức bạo lực, người cần giữ bí mật bị vào đầu) → thêm đúng một câu vào câu sự việc của cảnh, không viết lại cả phần thiết lập.
10. **Không dùng bước "tự kiểm sau khi viết"** — model không đọc lại văn của mình. Chuẩn văn nằm trong SI; khâu kiểm là review của Agent.
11. **Cảnh hội thoại: cho mỗi người một mối bận tâm cụ thể, không cho kịch bản tranh luận** (Tác giả 23/10, lam-game 005). Prompt "cô thẳng thừng, kiệm lời, chê là làm ẩu; anh đưa ra lý do vì sao…" thành màn thuyết trình: cô diễn vẻ lạnh ở từng câu, anh nói một tràng triết lý "一字一顿". Cách viết:
   - Không gắn nhãn tính cách (thẳng thừng, lạnh lùng, kiệm lời…) vào cảnh; ghi tình trạng thật của người đó lúc này (vừa tan ca 12 tiếng, chưa ăn, mai vào ca 8 giờ) — thái độ tự ra từ đó.
   - Không giao trình tự "A chê → B phản bác bằng lý do X", không giao một ý tưởng để nhân vật trình bày. Ghi mỗi người muốn biết gì / cần gì / lo gì; họ hỏi những câu thực tế (bao lâu, làm bằng gì, ai trả tiền, được gì) và trả lời bằng việc, bằng con số, bằng thứ đưa ra xem.
   - Cho cuộc nói chuyện có chỗ lạc đề tự nhiên (đồ ăn, việc làm, chuyện cũ chung) — đừng để mọi câu đều phục vụ mục tiêu của cảnh.

### Mẫu B — prompt đầy đủ
Prompt viết bằng **tiếng Việt**, yêu cầu Gemini viết chính văn **bằng tiếng Trung**. Lưu tại `briefs/doan-XXX.md`. Rút ra từ test vòng 1 (`lanh-chua-chip/reviews/test-B-C.md`): prompt quá thưa thì sai canon, prompt từng nhịp thì văn máy móc. Công thức cân bằng: **chốt sự thật và điểm đến, thả tự do cách đi.**

```
Viết đoạn thứ N, khoảng 2000 chữ, bằng tiếng Trung.
(Đoạn mở đầu: Viết đoạn mở đầu cho truyện mới, khoảng 2000 chữ, bằng tiếng Trung.)

【Thiết lập (để tham khảo, cái gì không dùng tới thì không cần viết ra)】
- Chỉ liệt kê thứ đoạn này dùng tới: nhân vật (tên + thân phận + một đặc điểm ngoại hình + tính cách + cách xưng hô), bàn tay vàng, địa điểm, con số cần chính xác.

【Tiền tình】 (đoạn mở đầu bỏ qua)
- Ba đến năm câu, chỉ phần liên quan tới đoạn này.

【Chuyện xảy ra trong đoạn này】
- Hai ba đoạn văn xuôi: bắt đầu từ đâu → chuyện gì xảy ra → dừng ở đâu. Không đánh số, không viết hành động chi tiết và câu thoại.

【Những điểm bắt buộc】
- 2–4 gạch: sự thật, con số, chi tiết cài cắm phải chính xác.

【Tự do sáng tạo】
- Ghi rõ phần giao cho Writer: chi tiết, phản ứng nhân vật phụ, cách nhân vật chính tự giễu và tính toán, cách bàn tay vàng lộ bản lĩnh.

【Mở đầu và chỗ dừng】
- Mở: nối thẳng từ khoảnh khắc đoạn trước dừng (cùng cảnh, cùng nhịp).
- Dừng: giữa mạch, ở chỗ X; chuyện tiếp theo là Y — phần của đoạn sau.
```

**Nguyên tắc viết prompt (mẫu B)**
1. **Mô tả khẳng định** — viết thứ *có*, không liệt kê thứ *không có*. Câu phủ định ("不是系统、没有积分…") sẽ mồi ngược model. Muốn tránh một từ → cấp sẵn từ đúng (vd. 小七 / 用户 / K-07).
2. **Không đưa câu thoại mẫu, không đánh số nhịp hành động** — model sẽ chép nguyên văn và chạy theo thứ tự.
3. Chỉ đưa con số, tên, xưng hô cần chính xác — lấy từ `bible/glossary.md`. Tên riêng viết bằng chữ Latin/tiếng Việt; chỉ ghi kèm chữ Hán cho vài từ khoá dễ bị model dịch lệch (vd. Bảy → 小七), sau khi tên tiếng Trung đã được Tác giả chốt.
4. Bí mật cần giữ → điều khiển bằng **hướng nghi ngờ / hiểu biết của nhân vật chính**, không bằng lệnh cấm.
5. Luôn có mục **自由发挥** để Writer chủ động thêm chi tiết.
6. Luật cứng đầy đủ (kể cả điều cấm) nằm trong bible cho Agent dùng khi **review**; lỗi lệch luật xử lý bằng ghi chú sửa, không nhồi trước vào prompt.
7. **Tả sự việc, không tả ý nghĩa.** Thay đổi thái độ của nhân vật phải đi qua một việc cụ thể — một con số khai thật, một món đồ đưa ra, một mệnh lệnh làm theo — không viết "nói một câu cho thấy ông đã nhìn lại", "vẫn gắt nhưng đã khác". Model sẽ viết đúng cái ý nghĩa đó rồi tự giải thích nó (bài học đoạn 005).
8. **Tối đa 2 cảnh + 1 lần nhảy thời gian mỗi đoạn.** Nhiều hơn là model phải tóm tắt.
9. **Đoạn dừng giữa mạch, không khép lại.** Chỉ ra chỗ dừng (một việc đang dở) và chuyện kế tiếp thuộc đoạn sau; đoạn sau mở ngay từ khoảnh khắc đó. Nhảy thời gian đặt *trong* đoạn, không đặt ở chỗ nối hai đoạn. (Tác giả 22/10: kiểu "Kết đoạn bằng một hình ảnh" làm mỗi đoạn khép tròn như một tập phim, đoạn sau dựng cảnh lại từ đầu → mất mạch liên tục.)
10. **Không dùng bước "tự kiểm sau khi viết".** Trong chat, model viết một lượt rồi dừng — nó không đọc lại và sửa văn đã viết, nên câu nhắc tự kiểm không có tác dụng. Mọi chuẩn văn phải nằm trong SI dưới dạng **chuẩn khi đang viết**; khâu kiểm thật sự là review của Agent (`review-blacklist.md`), đoạn hỏng thì làm lại ở session mới.
11. **Thiết lập chỉ ghi sự thật trơn**, không kèm mệnh đề nhân quả hay diễn giải ("…nên…", "vì…", "như thể…", "như chưa từng…"). Writer kể lại những mệnh đề đó thành câu giải thích trong chính văn (bài học lượt 2, đoạn 1).
12. **Chuỗi kỹ thuật cố định của bàn tay vàng** (câu khởi động, cách xưng) được ghi nguyên văn trong prompt — đây là ngoại lệ của nguyên tắc 2, vì ta *muốn* Writer chép đúng.
13. **Tính từ cảm giác trong prompt sẽ thành câu mở đầu.** "Phòng ẩm mốc" → văn mở bằng mùi mốc "直往鼻孔里钻" (3 lần liên tiếp). Chỉ ghi tính từ cảm giác khi muốn Writer mở cảnh đúng bằng cảm giác đó.
14. **Tư thế, xưng hô, điểm nhìn cần giữ → ghi ngay trong câu sự việc của cảnh đó**, không chỉ ở phần thiết lập. Ghi ở thiết lập thì Writer vẫn trượt; ghi trong câu sự việc ("Suốt lúc đó Hob đứng chống gậy cạnh giếng", "cả cảnh này kể từ mắt Leon, Pell chỉ có lời nói và việc làm") thì giữ được (lanh-chua-chip lượt 2, đoạn 004–005, 015).
15. **Cảnh quyền lực đè người** (phạt, khống chế, tra hỏi): ghi đúng một hình phạt, đúng động tác khống chế, và nhân vật phụ quan trọng làm gì *trong lúc* đó. Bỏ trống thì Writer leo thang bạo lực và cho người ta quỳ lạy (lanh-chua-chip lượt 2, đoạn 004).
16. **Chỗ trống "người kia nghĩ gì" sẽ bị lấp bằng cách vào đầu người đó.** Nhân vật cần giữ bí mật → cho họ một hành động cụ thể để kết thúc phản ứng ("gật lia lịa rồi chạy ra hành lang").
17. **Bàn tay vàng: ghi giới hạn giác quan ngay trong thiết lập của đoạn** (biết đúng những gì nhân vật chính thấy, nghe, ngửi…), nhất là cảnh đêm/xa — nếu không Writer tự cho nó dò nhiệt, theo dấu từ xa.
18. **Khi nhân vật tính sổ, đưa sẵn con số tổng và khung so sánh đúng** (đủ X ngày / còn Y ngày tới mốc Z). Writer hay tính sai và đóng khung sai.

---

## 5. Checklist Review

Ghi kết quả vào `reviews/doan-XXX.md`, mỗi mục: ✅ Đạt / ⚠️ Cần sửa nhẹ / ❌ Phải sửa.

**Canon & nhất quán**
- [ ] Không mâu thuẫn `bible/world.md`, `bible/timeline.md`
- [ ] Tính cách, động cơ, giọng thoại nhân vật đúng hồ sơ
- [ ] Xưng hô, tên riêng, thuật ngữ đúng `bible/glossary.md`
- [ ] Nhân vật không biết điều họ chưa được biết (nghe nói / đoán / đã kiểm chứng — [`chung/giu-nhat-quan.md`](chung/giu-nhat-quan.md) mục 2)
- [ ] Thương tích, đồ vật, thời gian trôi khớp đoạn trước (mục 6 cùng file)

**Cốt truyện**
- [ ] Đi đúng phương hướng và số liệu trong prompt (mẫu B: đủ các điểm bắt buộc)
- [ ] Cài cắm/payoff được thực hiện đúng
- [ ] Không mở tuyến truyện mới ngoài kế hoạch (nếu có → ghi đề xuất, không tự chấp nhận)
- [ ] Đoạn đổi ít nhất một trạng thái; không đóng sớm mâu thuẫn lõi của arc, không tiêu con bài cuối chưa tới lượt
- [ ] Hợp đồng độc giả: MC giữ quyền nhân quả và quyết toán ([`chung/xay-dung-truyen.md`](chung/xay-dung-truyen.md) mục 1)

**Văn phong**
- [ ] Đúng system instruction của truyện; soát theo `chung/review-blacklist.md` + `<ten-truyen>/gemini/review-blacklist.md`
- [ ] Không có dấu hiệu chép prompt / chạy checklist
- [ ] Thoại tự nhiên, phân biệt được giọng từng nhân vật
- [ ] Nhân vật chính chủ động, có tính toán
- [ ] Nối liền với đoạn trước; dừng giữa mạch, để ngỏ cho đoạn sau

**Kết luận review**: `ĐẠT` / `SỬA NHẸ` / `VIẾT LẠI` + 1–3 câu lý do.

---

## 5b. Bàn giao với Gemini

- Hai cách chạy Writer: (a) Tác giả dán prompt vào Gemini rồi lưu kết quả vào `chapters/doan-XXX.md`; (b) **Agent tự chạy** trên Google AI Studio qua Claude in Chrome khi Tác giả bảo — cách làm, cài đặt và bẫy ở `chung/ai-studio.md`.
- Mỗi truyện có **system instruction (SI) văn phong riêng** trong `<ten-truyen>/gemini/` — đó là thẩm quyền cao nhất về cách viết của truyện đó. File SI đang dùng và tên bản lưu trên AI Studio ghi trong `<ten-truyen>/README.md`. Sửa SI phải có Tác giả đồng ý và ghi log. Prompt của Agent chỉ quy định **nội dung** (diễn biến, canon, nhân vật, xưng hô, thiết lập bàn tay vàng), không chép lại hay viết đè quy tắc văn phong.
- Chi tiết mới Gemini tự đặt (địa danh, đồ vật, tên phụ) → Agent ghi nhận khi review, đề xuất Tác giả có đưa vào canon không.
- Gemini không nhớ bible: prompt mang theo tên, xưng hô và số liệu đoạn đó cần — chỉ chừng đó (mục 4).

## 5c. Chuyển session

**Writer Gemini** — mỗi session chỉ viết **2 đoạn** (đoạn thứ 3 trong một session đã trôi giọng — đoạn 005). Agent giữ gói bàn giao trong `<ten-truyen>/handoff/` (thẻ thiết lập, tóm tắt, trạng thái, **mẫu giọng** trích từ các đoạn đã duyệt, nguyên văn cuối đoạn gần nhất) và cập nhật **sau mỗi lần review**, ghép bằng `python tools/build_pack.py <ten-truyen> --prompt briefs/doan-XXX.md` thành **một tin nhắn mở session** (`handoff/session-start.md`: gói + prompt, Writer đọc rồi viết luôn). Chi tiết quy trình: `chung/quy-trinh-ban-giao.md`.

**Agent (Claude)** — cũng có thể sang session mới bất cứ lúc nào; repo là bộ nhớ. Session mới đọc theo thứ tự: `AGENT.md` → `<ten-truyen>/README.md` → `log.md` → `handoff/state.json` (hoặc `state.md` ở truyện cũ) → review gần nhất trong `reviews/`. Mọi quyết định phải nằm trong repo (log, bible, review), không chỉ nằm trong hội thoại.

Trước phần hồ sơ truyện, đọc thêm [`chung/kinh-nghiem.md`](chung/kinh-nghiem.md) để dùng các phát hiện đã tổng hợp. Khi đứng trên branch cũ, kiểm bản chung trên branch mặc định theo [`chung/dong-bo-kinh-nghiem.md`](chung/dong-bo-kinh-nghiem.md). Không dùng một bài học theo thể loại để ghi đè SI hoặc canon riêng đã được Tác giả chốt.

## 6. Mẫu Ghi chú sửa gửi Gemini

```markdown
# Ghi chú sửa — Đoạn XXX (vòng N)

## Giữ nguyên
- <đoạn/cảnh làm tốt, nêu lý do ngắn để Gemini không vô tình làm hỏng>

## Phải sửa (ưu tiên cao → thấp)
1. [Vị trí: đoạn/câu mở đầu "..."] Vấn đề: <…> → Yêu cầu: <…>
2. …

## Gợi ý (không bắt buộc)
- <…>
```

Nguyên tắc: chỉ rõ vị trí (trích câu tiếng Trung), nêu vấn đề + hướng sửa cụ thể; không chỉ nói "chưa hay". Ghi chú sửa gửi Gemini viết bằng **tiếng Việt** (trích dẫn câu gốc tiếng Trung khi cần chỉ vị trí).

---

## 7. Quản lý canon & quyết định

- **Story Bible là chân lý.** Nếu chính văn mâu thuẫn bible: hoặc sửa đoạn, hoặc (khi Tác giả duyệt) sửa bible và ghi `log.md`.
- **Ý tưởng mới từ Gemini** hay hơn kế hoạch → Agent đánh giá tác động lên các tuyến khác, trình Tác giả kèm khuyến nghị.
- **Decision Log** (`log.md`) — mỗi quyết định một dòng:
  ```
  2026-10-21 | doan-005 | Đổi thời điểm A phát hiện bí mật từ đoạn 12 sang đoạn 8 | Lý do: … | Duyệt: Tác giả
  ```
- **`plot/threads.md`** — bảng theo dõi:
  ```
  | ID | Tuyến/Chi tiết cài | Cài ở | Dự kiến payoff | Trạng thái |
  ```
  Mỗi 5 đoạn, Agent rà soát: tuyến nào treo quá lâu, cài cắm nào bị quên, nhân vật nào vắng lâu — chạy `python tools/ra_soat.py <ten-truyen>` rồi xử lý từng dòng theo [`chung/giu-nhat-quan.md`](chung/giu-nhat-quan.md) mục 4; hỏi thêm bốn câu hợp đồng độc giả và hai câu tiêu quá tay ([`chung/xay-dung-truyen.md`](chung/xay-dung-truyen.md) mục 1, 3).

---

## 8. Phân quyền quyết định

| Loại thay đổi | Agent tự làm | Cần Tác giả duyệt |
|---|---|---|
| Sửa lỗi chính tả, xưng hô, tên riêng | ✅ | |
| Ghi chú biên tập, yêu cầu Gemini sửa | ✅ | |
| Cập nhật bible theo đoạn đã chốt | ✅ | |
| Thêm nhân vật phụ / cảnh phụ không ảnh hưởng arc | ✅ (ghi log) | |
| Thay đổi dàn ý, thứ tự sự kiện | | ✅ |
| Thêm/bỏ nhân vật chính, đổi luật thế giới | | ✅ |
| Twist, cái chết nhân vật quan trọng, kết truyện | | ✅ |

---

## 9. Giao tiếp

- Ngôn ngữ làm việc với Tác giả: **tiếng Việt**. Prompt và ghi chú sửa gửi Gemini: **tiếng Việt**. Chính văn: **tiếng Trung**.
- Báo cáo cho Tác giả sau mỗi đoạn: tóm tắt 3–5 dòng (đã làm gì, vấn đề gì, cần quyết định gì).
- Khi hỏi Tác giả: đưa bối cảnh đủ để trả lời ngay, nêu 2–3 phương án và **khuyến nghị của Agent**.
- Với Gemini: chỉ giao qua prompt và ghi chú sửa — rõ ràng, tự đủ, không ngầm định.

---

## 10. Quy ước Git

- Mỗi đoạn chốt = 1 commit: `doan-XXX: chốt — <tóm tắt>`, **push ngay sau khi duyệt** (Tác giả 22/10). Truyện nào cũng commit trong thư mục của nó; thay đổi luật chung (AGENT.md, `chung/`, `tools/`) commit riêng.
- Thay đổi bible/plot: `bible: <mô tả>` / `plot: <mô tả>`.
- Prompt & review: `prompt: doan-XXX`, `review: doan-XXX vòng N`.
- Không force-push, không xoá lịch sử bản thảo.

---

## 11. Khởi động dự án (khi bible còn trống)

Chép khung: `cp -r _mau-truyen <ten-truyen>` (đọc `_mau-truyen/README.md`); SI của truyện điền từ `writer/SI-template`. Thêm truyện vào bảng ở `README.md` gốc. Rồi Agent cùng Tác giả hoàn thành theo thứ tự:
0. (Nên làm) Mổ xẻ 1–2 truyện top cùng thể loại theo [`chung/mo-xe-truyen.md`](chung/mo-xe-truyen.md); chỉ mang sang kỹ thuật.
1. `bible/overview.md` — logline 1 câu, premise 1 đoạn, thể loại, chủ đề, đối tượng độc giả, **hợp đồng độc giả**, **quỹ kết cục và bậc thang** ([`chung/xay-dung-truyen.md`](chung/xay-dung-truyen.md) mục 1, 3).
2. `bible/glossary.md` — tên riêng và xưng hô bằng tiếng Trung (văn phong đã có system instruction của Gemini).
3. `bible/characters/` — nhân vật chính, phản diện, 3–5 nhân vật phụ quan trọng.
4. `bible/world.md` — bối cảnh và các luật không được phá.
5. `plot/arcs.md` (kèm neo arc) → `plot/outline.md` — dàn ý toàn truyện.
6. Prompt đoạn 1 → bắt đầu vòng lặp ở mục 3.

## 12. Ghi và chia sẻ bài học giữa các truyện

- Sổ chung: [`chung/kinh-nghiem.md`](chung/kinh-nghiem.md); nguồn: [`chung/nguon-kinh-nghiem.md`](chung/nguon-kinh-nghiem.md). Luật/SI và phản hồi mới nhất của Tác giả trong đúng truyện quyết định phạm vi áp dụng.
- Mỗi phát hiện ghi nguồn, điều đã thử, kết quả, phạm vi và tình trạng. Phân biệt yêu cầu của Tác giả với nhận xét Agent hoặc giả thuyết chưa thử; đánh dấu quyết định bị thay thế.
- Thoại thông thường cần nói trọn ý và đáp nối nhau. Giữ nhịp khẩu lệnh khi cần; nhịp đoạn kể ngắn không giới hạn độ dài lượt thoại. Khi cảnh cần trao đổi, brief tạo cơ hội cho người nghe nêu khó khăn, hỏi lại hoặc góp ý.
- Phát hiện về cách viết/quy trình có thể đưa vào sổ chung, checklist hoặc SI-template. Không chuyển tên, số liệu, chức năng bàn tay vàng, bí mật hay thẩm quyền tự duyệt của một truyện thành quy tắc cho mọi truyện.
- Thay đổi tài liệu chung thành commit riêng; đồng bộ đúng commit sang các branch theo hướng dẫn. Không ghi đè công việc chưa commit hoặc gộp cả branch truyện chỉ để chia sẻ một bài học.

## 13. Skill của Agent và vòng tự học

- Cách làm (thứ tự việc, lệnh, bẫy) nằm trong skill [`.claude/skills/novel-craft/SKILL.md`](.claude/skills/novel-craft/SKILL.md) — Claude Code tự nạp; Agent khác (Codex, Hermes) đọc file đó trước khi làm truyện. File này giữ vai trò và phân quyền; skill không chép lại luật ở đây.
- Mỗi bản Writer trả về qua cổng máy trước khi đo/review: `python tools/cong_doan.py <bản> --prompt <brief> [--prev <đoạn trước>]` (chặn bản cụt, ngắn bất thường, chép mẫu). Cổng xanh chưa phải ĐẠT.
- Cuối mỗi phiên làm truyện, Agent chạy **vòng học** (mục 9 của skill): Tác giả sửa lưng, cách làm mới chạy được, hay luật sai → sửa thẳng skill (hoặc `chung/kinh-nghiem.md` nếu là phát hiện về cách viết), commit riêng `skill: …`.
