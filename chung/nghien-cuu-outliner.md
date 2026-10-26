# Nghiên cứu: các repo về xây dựng truyện — bài học cho khâu Outliner

Ngày 26/10/2026. Tác giả: "rào cản giờ không hoàn toàn là Writer nữa mà là Outliner." Tài liệu này khảo sát các repo/bài báo về **lập dàn ý truyện dài bằng AI**, rút ra kỹ thuật dùng được và **đề xuất** nâng cấp khâu dàn ý của repo. Đây là **nghiên cứu + đề xuất**, chưa phải luật: mọi thay đổi `AGENT.md`, mẫu dàn ý hay dàn ý của một truyện cần Tác giả duyệt (AGENT.md mục 8).

---

## 1. Chẩn đoán: dàn ý hiện tại thiếu gì

Dàn ý của repo (vd. `lam-game/plot/outline.md`) mỗi đoạn có: **chuyện xảy ra + chỗ Dừng**. `threads.md` có: cài ở / dự kiến payoff / trạng thái. Đối chiếu với các hệ thống bên dưới, dàn ý đang **mô tả việc xảy ra**, nhưng chưa trả lời:

| Câu hỏi dàn ý chưa trả lời | Hậu quả thấy được |
|---|---|
| Người đọc đi từ cảm xúc nào sang cảm xúc nào trong đoạn này? | Đoạn đúng sự kiện nhưng "chưa đúng ý" (lam-game 001: "tạm ổn, đoạn đầu chưa đúng ý") |
| MC chọn gì, và cái giá của lựa chọn là gì? | Đoạn quan sát/đi lại dài; MC thành người chứng kiến |
| Đoạn này nằm ở đâu trên đường áp lực (cao/thấp)? Các đoạn kề nhau có cùng một cảm xúc không? | Nhiều đoạn liền cùng một nhịp |
| Thông tin nào được *thả* ra ở đoạn này, thông tin nào phải *giữ*? | Writer lộ sớm hoặc giữ quá lâu |
| Đối thủ/áp lực đến từ ai, cách bao nhiêu đoạn thì xuất hiện lại? | Khoảng dài không có ai cản MC |
| Cài cắm nào đã tới hạn payoff? Cài cắm nào treo quá lâu mà không tiến triển? | `threads.md` chỉ có "dự kiến", không ai nhắc lúc tới hạn |
| Ai *được hưởng* thành quả của mỗi cao trào? | Phương án dễ trượt sang kiểu "người khác cứu MC" |

Đó là phần việc của Outliner, không phải của Writer: Writer viết tốt cỡ nào cũng không bù được một đoạn thiếu lựa chọn hay thiếu lý do để đọc tiếp.

---

## 2. Bản đồ các repo đã khảo sát

| Repo / bài báo | Là gì | Đáng học cho Outliner |
|---|---|---|
| **[worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode)** (MIT, ~6k★, cập nhật 26/10/2026) | Bộ skill viết **网文 tiếng Trung** cho Claude Code: quét bảng xếp hạng → phân tích sách mẫu → 大纲 → 卷纲 → 细纲 → 正文 → review/去AI味 | **Sát với repo mình nhất.** Mẫu 细纲 9 trường bắt buộc; 爽点 6 loại + cách tính ngược; "hợp đồng người đọc" 4 câu; phương pháp điểm then chốt 1/4–giữa–3/4; định vị chương + mức áp lực; kiểm tra nguồn cung trước mỗi lô dàn ý; chi tiết mới chia 3 mức xử lý; thẻ thể loại 游戏体育 |
| **[voocel/ainovel-cli](https://github.com/voocel/ainovel-cli)** (Apache-2.0) | Pipeline Go: Architect / Writer / Editor + Engine tất định | **Lập kế hoạch cuốn chiếu**: "la bàn" (hướng kết + tuyến mở + quy mô) + chỉ triển khai chi tiết arc hiện tại, arc sau chỉ có khung (mục tiêu + số chương ước tính). Khi mở arc mới: "coi chính văn đã viết là sự thật, coi khung là kế hoạch còn sửa được". Danh sách 6 câu kiểm tra trước khi kết truyện |
| **[NousResearch/autonovel](https://github.com/NousResearch/autonovel)** | Pipeline tự động: seed → world → characters → outline → sổ cài cắm → canon → voice → viết → sửa | Mỗi chương trong dàn ý có: POV, nhịp Save-the-Cat, % vị trí, cung cảm xúc, **chu trình thử–thất bại**, cài (plants), payoff, chuyển động nhân vật, **"lời nói dối" nhân vật tin**. Sổ cài cắm có cột **Củng cố**, khoảng cài→payoff ≥ 3 chương. Ghi nhận "nợ lan truyền" khi đổi một tầng. Dàn ý bị **gộp 24→19 chương** trong lúc viết. Review của Opus bắt được **"đơn điệu cấu trúc"** mà công cụ tự động bỏ sót |
| **[hanmengkai/novelagent](https://github.com/hanmengkai/novelagent)** (Novel Agent V2, MIT) | LangGraph: Director / Planner / Writer / Editor / Checker / Repair | **Máy trạng thái cài cắm**: BURIED → ACTIVE → DUE (đang trong cửa sổ payoff) → RESOLVED; mục DUE được đẩy thẳng vào kế hoạch chương. Planner phải nêu **mâu thuẫn muốn–sợ của nhân vật nào** được kích hoạt trong cảnh. Câu nhắc mềm kiểu "nhớ xử lý cài cắm" bị chìm khi số chương tăng → phải theo dõi thành đối tượng có trạng thái |
| **[shenminglinyi/PlotPilot](https://github.com/shenminglinyi/PlotPilot)** | Pipeline Trung: 部/卷/幕 → beat sheet từng màn → viết → hậu kỳ | **Đường cong căng thẳng** 0–10 mỗi chương, điểm trũng thì chẩn đoán; **tỉ lệ đóng cài cắm** làm chỉ số; trích sự kiện/bộ ba sau mỗi chương để truy chuỗi nhân quả |
| **[YILING0013/AI_NovelGenerator](https://github.com/YILING0013/AI_NovelGenerator)** | Tầng: quyển → arc → cảnh → kế hoạch chương | Xác nhận khung tầng; README ít chi tiết |
| **[Nigh/show-me-the-story](https://github.com/Nigh/show-me-the-story)** | Go + web UI: Tác giả duyệt dàn ý trước rồi mới viết | Mô hình human-in-the-loop giống mình; có "hướng dài hạn, ý định kết, review kế hoạch" |
| **[tdrml/auto-graph](https://github.com/tdrml/auto-graph)** | Mỗi chương là một PR trên GitHub | Quy trình git giống mình (commit/push mỗi đoạn) |
| **MaoXiaoYuZ/Long-Novel-GPT** | 大纲 → 剧情 → 正文, mỗi tầng có tạo/mở rộng/đánh bóng | Có thể nhập sách có sẵn để **tách ngược** ra dàn ý — giống việc mình học sách mẫu |
| **DOC** (Yang và cs., ACL 2023; `yangkevin2/doc-story-generation`) | Dàn ý chi tiết phân cấp + bộ điều khiển bám dàn ý | So với Re3 (lập kế hoạch → viết → viết lại): tính mạch lạc tăng 22.5%, bám dàn ý tăng 28.2%. **Dàn ý chi tiết hơn thì truyện mạch lạc hơn**, nếu Writer bám được dàn ý |
| **Agents' Room** (DeepMind, ICLR 2025) | Agent lập kế hoạch (nhân vật, xung đột, bối cảnh, điểm cốt truyện) tách khỏi agent viết từng phần, dùng chung một bảng nháp | Ủng hộ cách chia Agent/Writer của mình |
| **StoryWriter** (THU-KEG, 2025) | Dàn ý **dựa trên sự kiện** có quan hệ sự kiện↔sự kiện → agent kế hoạch chia sự kiện vào từng chương → agent viết nén lịch sử | Lên **chuỗi nhân quả** trước, rồi mới chia vào đoạn |
| **Dramatron** (DeepMind) | Viết kịch bản từ trên xuống: logline → nhân vật → điểm cốt truyện → địa điểm → thoại | Được thiết kế để người và AI cùng viết, không chạy tự động |

---

## 3. Các kỹ thuật đáng mang về (đã chọn lọc)

### 3.1 Thẻ đoạn (từ 细纲 của oh-story, rút gọn cho đơn vị "đoạn" ~2000 字)
Các trường bắt buộc của họ: 核心事件 · 目标情绪 (trước→sau, gắn một kết quả thấy được, không chỉ ghi nhãn như "nhiệt huyết") · 主角目标/关键选择 · 章首钩子 · 爽点 · 本章禁止提前释放. Thêm vào đó là bảng tình tiết có cột **执行边界 "禁＋放"**: mỗi điểm ghi điều *không được* thả và điều *được phép* làm tới đâu (vd. "được phép để MC tính ngay ra số tiền đó bằng mấy tháng tiền nhà"); mỗi chương có ít nhất một điểm "放". Ngoài ra có "写手自由区" (giống mục 自由发挥 của mình) và "复沓锚句", câu phải chép nguyên văn (giống nguyên tắc 12 của mình).

> Mẫu prompt AGENT.md mục 4 đã đúng hướng với họ (chốt sự thật, thả tự do cách đi). Phần thiếu nằm ở **tầng dàn ý phía trên prompt**.

### 3.2 Lựa chọn của MC và "hợp đồng người đọc" (契约四问)
1. MC có tự mình chọn mà giành được kết quả không? (quyền nhân quả + quyền quyết toán)
2. Thu hoạch/khoảnh khắc đẹp nhất có bị nhân vật phụ, cơ quan hay sự trùng hợp lấy mất mà không có trao đổi không?
3. Có dùng sớm một **lá bài cuối truyện** (đối thủ lớn nhất, sự thật cuối, đỉnh năng lực) không?
4. Kỳ vọng cũ đã được "trả lãi" chưa (có tiến triển, có thông tin mới)? Có kỳ vọng mới chưa? Bối cảnh/nhân vật/bí ẩn mới có đang được dùng để né lời hứa cũ không?

"MC chỉ nhận thưởng, được người khác cứu hoặc được sắp xếp thì coi như không có lựa chọn." Tính ngược khi lập dàn ý: chọn loại 爽点 trước, xác định người đọc đang chờ gì, rồi mới xếp phần chuẩn bị.

### 3.3 Định vị đoạn và đường áp lực
Áp lực 1–5: cao áp (15–20%; truyện nhịp nhanh có thể trên 30%), đẩy mạch (40–50%), luyện/thử sai, thu hồi quan hệ, sinh hoạt (≤10%), sắp xếp thông tin (≤5%, gộp được thì gộp). Hai điều tối thiểu: **mỗi đoạn có một lý do để đọc tiếp**; **một cảm xúc chủ đạo không kéo quá 2–3 đoạn liền**. Cao trào lớn (từ lúc dâng lên tới lúc thu hoạch): ~14–20 chương với nhịp nhanh. Đơn vị cốt truyện (剧情单元): 1.5–3 vạn chữ, khoảng 5–15 chương. Với đoạn ~2000 字 của mình thì một đơn vị ≈ **8–15 đoạn**.

### 3.4 Điểm then chốt 1/4 – giữa – 3/4
Mỗi tầng (cả truyện / arc / đơn vị) đặt một tình tiết then chốt ở 1/4, giữa và 3/4: *nghịch chuyển* (trong dự đoán, nhưng cách MC giải quyết khiến người đọc vỗ tay), *bước ngoặt* (ngoài dự đoán), *biến cố khơi mào*. Nếu có sách mẫu thì giữ **chuỗi cảm xúc và vị trí chức năng** của sách mẫu, còn người, cảnh và sự kiện thay toàn bộ (khớp với KN11 của mình).

### 3.5 Kiểm tra nguồn cung trước mỗi lô dàn ý (供给自查)
Sáu câu: ① đối thủ có tên có vắng mặt quá 2 đoạn không (đối thủ có thể là đồng minh hay người thân; đoạn về môi trường/quan hệ thì không cần thêm phản diện cho đủ khoảng cách)? ② nhân vật xuất hiện trong 3 đoạn tới đã có hồ sơ chưa? ③ năng lực mới có nối được với những gì MC đã có không? ④ **con số, quy chế, khoảng cách dùng tới đã có trong bible chưa** (phải tra đúng mục, không đoán)? ⑤ đặc điểm không gian của địa điểm đã ghi chưa? Có lặp cùng cảnh, cùng đối thủ, cùng cách thắng với đơn vị trước không? ⑥ tuyến nào được đẩy?
Chi tiết mới chia **ba mức**: *viết luôn* / *viết rồi báo* (ghi vào bible trước, rồi mới dùng) / *hỏi Tác giả trước*. Ba mức này khớp với bảng phân quyền mục 8 của mình.

### 3.6 Sổ cài cắm có trạng thái
Gộp autonovel và Novel Agent V2: cột **Cài ở · Củng cố ở · Cửa sổ payoff · Trạng thái (CÀI → ĐANG CHẠY → TỚI HẠN → ĐÃ TRẢ)**. Cài và trả cách nhau ≥ 3 đoạn. Mục **TỚI HẠN được đưa thẳng vào bước [1] lập kế hoạch** của đoạn kế. Luật của oh-story: **một thông tin bị giữ ≥ 3 đoạn mà không có tiến triển thì thả sớm hoặc bỏ**.

### 3.7 Lập kế hoạch cuốn chiếu và la bàn
"La bàn" gồm: hướng kết (một mệnh đề chủ đề, không phải tên chương), các tuyến dài đang mở, quy mô ước tính (một khoảng). Chỉ triển khai chi tiết arc/lô hiện tại; arc sau chỉ có *mục tiêu + số đoạn ước tính*. Khi triển khai arc tiếp, **chính văn đã chốt là sự thật**, còn khung thì sửa được. Dàn ý **đi theo bản thảo** (autonovel dựng lại outline từ chương đã viết, đã gộp 24→19 chương).

### 3.8 Chu trình thử–thất bại và "lời nói dối"
Đoạn giữa của một arc nên có kết quả cảnh kiểu **"Có, nhưng…"** hoặc **"Không, và…"**. Hồ sơ nhân vật chính có **Lời nói dối nhân vật tin → Muốn (giải pháp sai) → Cần (sự thật)**. Lưu ý chống mẫu của autonovel: *"Các nhịp đến đúng lịch"*. Dàn ý ghi "tò mò → phát hiện → sợ" thì chương ra đúng thứ tự ấy, máy móc. Đây là lý do mình **không đưa trường cảm xúc vào prompt cho Writer** (xem 5).

---

## 4. Soi thử arc 1 của lam-game

Áp các lăng kính ở mục 3 lên `lam-game/plot/outline.md` + `threads.md` (bản 23/10). **Đây là nhận xét của Agent, chưa phải quyết định.**

| # | Phát hiện | Lăng kính | Mức |
|---|---|---|---|
| A | **Phương án (a) lấy chứng nhận** ("giám khảo ở lại lâu đề cử đặc biệt") giao *quyền quyết toán* cho một giám khảo. Theo câu 1–2 của hợp đồng người đọc, đây là mức **cần gia cố**: MC phải là người tìm ra điều khoản và tự mang bằng chứng (số liệu 试映, hàng người ở 深蓝) tới; giám khảo chỉ làm nhân chứng | 3.2 | ⚠️ trước đoạn 018 |
| B | **T01 tiền nhà "老周 ứng"** là kiểu được người khác cứu. Khuyên: MC tự đàm phán ăn chia doanh thu 试映 với 老周 (một lựa chọn có giá), tiền nhà trả bằng khoản đó | 3.2 | ⚠️ trước đoạn 012 |
| C | **Thu hoạch thấy được đầu tiên rơi vào đoạn 008** (老周 ở trong 40 phút), tức khoảng 16.000 字. 001–003 là quan sát + hụt hẫng, ba đoạn áp lực thấp liền nhau, cùng một cảm xúc. Thông lệ 网文 (黄金三章, "主线开篇": nêu hoàn cảnh và mục tiêu → lần đầu đổi được chút thành quả) muốn có thắng lợi nhỏ trong khoảng 6.000 字 đầu. *Giả thuyết*: một phần lý do "đoạn đầu chưa đúng ý". Gợi ý: tới 003, MC có một **dự đoán đúng thấy được ngay** (vd. đoán trước khách nào sẽ ra sau ~18 phút và vì sao, 老周 kiểm đồng hồ khoang thấy đúng). Như vậy góc nhìn người làm game được chứng minh ngay, không cần bàn tay vàng | 3.1, 3.3 | ❓ hỏi Tác giả |
| D | **Đối thủ có tên đầu tiên là 顾辰 ở 015.** Từ 001 tới 014 áp lực chỉ đến từ tiền và hạn chót (áp lực môi trường thì luật nguồn cung chấp nhận). Có thể cài sớm một mặt người cho áp lực: 长庚 qua chỗ làm của 姜禾, hoặc một quán khác chê 《退潮》 trong lúc 试映 | 3.5 | 💡 gợi ý |
| E | **Ba mốc then chốt đã có sẵn và đúng chỗ**: 1/4 ≈ 006–007 (thử lần đầu: "Không, và…"), giữa ≈ 012–014 (试映 thành công: nghịch chuyển), 3/4 ≈ 018–021 (trượt 境评: bước ngoặt). Không cần sửa, chỉ cần ghi tên mốc vào dàn ý để giữ | 3.4 | ✅ |
| F | **Arc 1 ~26 đoạn ≈ 52.000 字**, tức khoảng hai đơn vị cốt truyện: (1) 001–011 "làm ra được một thứ", (2) 012–026 "chứng minh nó". Mỗi đơn vị nên có động cơ cảm xúc và màn thu hoạch riêng | 3.3 | 💡 |
| G | `threads.md` chưa có cột Củng cố / Cửa sổ payoff. T08 (晕潜 do không nhất quán) và T10 (mặt trăng) còn "chưa cài", nhưng payoff đã đặt ở 试映 và cuối arc → cần chọn đoạn để cài trước ~009 | 3.6 | ⚠️ |

---

## 5. Đề xuất (cần Tác giả duyệt)

**Khuyến nghị của Agent: làm P1 + P2 + P3 ngay cho lam-game, chạy thử trên lô 003–010. Sau 2–3 đoạn mới quyết có đưa vào AGENT.md / `_mau-truyen` không.**

| ID | Đề xuất | Đụng vào | Lý do |
|---|---|---|---|
| **P1** | **Thẻ đoạn trong `outline.md`** (chỉ Agent dùng, **không chép vào prompt**): *Sự kiện chính · Cảm xúc người đọc trước→sau (gắn một kết quả thấy được) · MC muốn gì / chọn gì / mất gì · Kết quả cảnh (Có-nhưng / Không-và / Có / Không) · Định vị + áp lực 1–5 · Thả / Giữ · Lý do đọc tiếp · Tuyến chạm (T-ID)*. Khi viết prompt, mỗi trường **dịch thành sự việc** theo nguyên tắc 7 và 11 (vd. "cảm xúc: nghi → tin" thành "老周 kiểm đồng hồ khoang: đúng 18 phút") | `<truyện>/plot/outline.md`, mẫu ở `_mau-truyen` | Lấp các khoảng trống ở mục 1 mà không phạm nguyên tắc "tả sự việc, không tả ý nghĩa" |
| **P2** | **Kiểm arc / đơn vị trước khi trình Tác giả**: hợp đồng người đọc 4 câu · ba mốc 1/4–giữa–3/4 · đường áp lực (không quá 2–3 đoạn liền cùng một cảm xúc) · kiểm nguồn cung 6 câu · lá bài cuối truyện nào bị khoá tới arc nào | Thêm một mục vào AGENT.md (bước [1]) | Bắt các lỗi kiểu A–D trước khi viết, rẻ hơn viết lại |
| **P3** | **`threads.md` có trạng thái**: thêm cột *Củng cố · Cửa sổ payoff*, trạng thái CÀI/ĐANG CHẠY/TỚI HẠN/ĐÃ TRẢ; luật "giữ ≥3 đoạn không tiến triển → thả hoặc bỏ"; mục TỚI HẠN tự vào bước [1]. `chot_doan.py` có thể in ra các mục tới hạn | `threads.md`, sau đó `tools/chot_doan.py` | Câu nhắc mềm bị chìm (Novel Agent V2); repo mình đã có bảng, chỉ thiếu trạng thái |
| P4 | **La bàn** ở đầu `arcs.md` (hướng kết · tuyến dài đang mở · quy mô) + quy ước cuốn chiếu: chi tiết tối đa ~10 đoạn tới, phần sau chỉ có mục tiêu + số đoạn | `arcs.md` | lam-game đang làm gần như vậy; viết rõ ra để session sau giữ được |
| P5 | Thử **tách ngược sách mẫu** (`全能游戏设计师.txt`) thành *chuỗi cảm xúc + vị trí chức năng* của 1–2 đơn vị đầu, rồi thay toàn bộ chất liệu. Hiện sách mẫu chỉ dùng để học văn cho SI | `lam-game/` | Phương pháp "对标节奏迁移" của oh-story; giữ KN11 (không nhập thiết lập) |
| P6 | (Tuỳ chọn) Cài thử skill `story-long-analyze` / `story-long-write` của oh-story trong một branch thử để so | ngoài repo | Đánh giá trực tiếp; không đưa vào luật nếu chưa thử |

Không đề xuất: chuyển sang pipeline tự động hoàn toàn (autonovel, ainovel-cli). Các hệ đó cho model tự chấm và tự duyệt, còn repo mình có Tác giả duyệt và Writer khác model. Chỉ lấy *cấu trúc dữ liệu* và *checklist* của họ.

---

## 6. Nguồn

- oh-story-claudecode: `skills/story-long-write/references/` — `workflow-outline.md` (mẫu 细纲, nguồn cung, ba mức), `plot-core-methods.md` (爽点, cao trào 5 bước, 禁止提前释放), `reader-contract-and-progression.md` (契约四问, lá bài cuối truyện), `workflow-volume.md` (định vị/áp lực, điểm then chốt, chuyển nhịp sách mẫu), `outline-methods.md` (động cơ đơn vị, vòng lặp theo thể loại), `genre-prose-cards/游戏体育.md`.
- ainovel-cli: `assets/prompts/architect-long.md` (la bàn, arc khung, danh sách kết truyện), `internal/domain/review.go` (ForeshadowEntry: planted/advanced/resolved).
- autonovel: `README.md`, `gen_outline_part2.py` (trường dàn ý mỗi chương, sổ cài cắm ≥15 tuyến, khoảng ≥3 chương), `CRAFT.md` (thử–thất bại, MICE, Lời nói dối/Muốn/Cần), `ANTI-PATTERNS.md` ("nhịp đến đúng lịch", "không hai chương nào kết cùng một kiểu").
- Novel Agent V2: [bài giới thiệu](https://www.besthub.dev/articles/novel-agent-v2-multi-agent-langgraph-pipeline-for-consistent-long-form-novels-4786e836e9c6).
- DOC: [arXiv 2212.10077](https://arxiv.org/abs/2212.10077) · Agents' Room: [arXiv 2410.02603](https://arxiv.org/abs/2410.02603) · StoryWriter: [arXiv 2506.16445](https://arxiv.org/abs/2506.16445) · Dramatron: [arXiv 2209.14958](https://arxiv.org/abs/2209.14958).
- Số sao và mô tả một số repo (PlotPilot, AI_NovelGenerator, show-me-the-story, Long-Novel-GPT, auto-graph) lấy từ README/trang tổng hợp, chưa đọc mã.
