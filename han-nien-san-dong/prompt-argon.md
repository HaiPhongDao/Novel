# Vấn đề cần giải quyết: văn của Writer có "giọng AI", lẫn thổ ngữ và chữ cổ, trong khi bộ mẫu viết bạch thoại

## Bối cảnh

Dự án viết truyện mạng tiếng Trung. Repo công khai: https://github.com/HaiPhongDao/Novel (nhánh `han-nien-san-dong`).

Ba vai:
- **Tác giả**: người quyết định; người duy nhất chấm đạt / không đạt, bằng cách đọc. Tác giả nghe văn qua app đọc truyện
  (chữ Trung → bản dịch Việt kiểu convert) và đã sửa "giọng AI" ở nhiều nơi khác, nên bắt rất nhanh.
- **Agent** (Claude): viết System Instruction (SI), viết brief, chạy Writer, báo cáo.
- **Writer**: Gemini 3.8 Flash trên Google AI Studio, thinking High. Mỗi lần viết là một chat mới gồm SI (tiếng Anh) và
  một tin nhắn người dùng. Tin nhắn đó là brief tiếng Việt (đoạn 001), hoặc gói bàn giao (thẻ thiết lập + State JSON +
  đuôi đoạn trước) cộng brief (đoạn 002 trở đi). Writer trả về văn tiếng Trung, mỗi đoạn khoảng 2.000–5.000 字.

Truyện `han-nien-san-dong` (tên tạm Hạn Niên Săn Đồng): cổ đại năm đại hạn. Núi Hắc Thạch 黑石岭 bị quan huyện bán cho nhà họ Lữ;
秦野 là người hiện đại nhập vào thân xác một thiếu niên bị đánh vì lén vào núi, nợ 240 văn tiền phạt hạn bảy ngày, rồi
nhận ra khế bán núi chỉ tính "từ mốc đá trở lên". Bàn tay vàng: bảng độ thuần thục 【技艺：…】.

Bộ mẫu: 《乱世荒年：我每日一卦粮肉满仓！》 (风起于渊, 174 chương) — văn **bạch thoại** hiện đại, nhẹ, MC xuyên việt có cái đầu
hiện đại, lời kể đi vào đầu người trong cảnh. SI đang dùng do Agent viết lại từ giọng bộ mẫu này.

## Vấn đề — lời Tác giả

- "Đang bị vấn đề ở cả brief và SI: Đều thỉnh thoảng xuất hiện tiếng bản địa(?), chữ cổ(?). Văn mẫu viết bằng bạch thoại
  văn mà. Nhiều chỗ trong writer tôi đọc thấy cấn cấn."
- "Writer đang dùng từ 'thật sự / đắc nhận'" — tức 实打实 và 得很 (ảnh chụp app: 有实打实的劲道 · 气血实打实充盈些 · 语气平稳得很).
- "'thẳng hướng trong lỗ mũi chui', 'thẳng hướng trong xxx chui' được sử dụng quá nhiều, hầu như ở bản nào cũng có" —
  tức 直往鼻孔里钻 / 直往…里钻.
- "Mới đọc khoảng 30 câu đã xuất hiện rất nhiều từ kiểu này. Nó giống kiểu 'giọng AI' ấy… nó tồn tại cảm rất lớn và rất
  khó chịu."
- Về bản sửa gần nhất (SI-R2, cấm đích danh các cụm): "Chẳng thấy thay đổi gì mấy, còn giảm chất lượng prose nữa chứ."
- Về thoại: "Phần thoại hơi ổn rồi. Để về sau test thêm." — đừng làm hỏng thoại.

Câu Writer, nguyên văn:

| Kiểu | Câu Writer |
|---|---|
| chữ đệm 实打实 | 肚子里有了那一海碗滚烫的兔肉汤，昨夜还酸软发虚的双腿终于有了实打实的劲道。 · 数值没变，但身体里的气血实打实充盈了些。 |
| …得很 trong lời kể tả giọng | 秦野把那只肥兔往罗里正的碗边推了推，语气平稳得很：“…” |
| 直往…里钻 | 兔肉泛着诱人的粉光，冷气直往鼻孔里钻。 · 村道上的浮土被日头晒得发烫，一脚踩下去，黄烟直往裤管里钻。 |
| chữ nhấn | 整整三斤精肉！ · 四条腿上的紧实精肉透着一股子新鲜的血气，足有三斤沉。 · 眼睛死死盯在他的脚底板下。 |
| chữ cổ / thổ ngữ | “老夫手里可没有多余的糠皮借你…别在老夫院里嚎丧！” · 村里半大后生都爱围着他转。 · 远远地跟在后头指指点点。 |

Agent đếm trên 25 bản Writer so với 182 chương bộ mẫu (cụm Writer dùng gấp ≥8 lần bộ mẫu và lặp ở ≥8 bản): 整整 · 实打实 ·
紧实 · 沉甸甸 · 猛地 · 死死 · 狠狠 · 硬生生 · 清清楚楚 · 浑浊的眼睛 · 干瘪 · 枯瘦的 · 嘴唇哆嗦 · 颤巍巍 · 喉结 · 眼珠子 · 眉头拧成疙瘩 ·
清了清嗓子 · 冷不丁 · 静得能听见… · 白纸黑字 · 朝…方向狂奔而去 · 老夫 · 后生 · 俺 · 瞅 · 外头 / 后头 / 底下 (bộ mẫu viết 外边 /
后面 / 下面). Bộ mẫu: tổng 0,44 lần /1.000 字; Writer: 6,6–16,2. Danh sách đầy đủ kèm số:
`han-nien-san-dong/gemini/tat-giong-ai.txt`. Số đếm chỉ để khoanh vùng — Tác giả nghe "giọng AI" ở cả những chỗ không
có trong danh sách.

## Việc cần giải quyết

1. Tìm nguyên nhân Writer viết ra "giọng AI" (chữ đệm, cận cảnh sáo, thổ ngữ, chữ cổ) trong khi bộ mẫu viết bạch thoại
   gọn, và vì sao cấm đích danh các cụm lại làm văn kém đi.
2. Đưa ra cách sửa dùng được ngay: SI và/hoặc khuôn brief / gói bàn giao, viết **toàn văn**, để văn của Writer đọc như bộ
   mẫu.
3. Nêu cách kiểm: chạy trên đoạn 001 và 003 thì đọc những chỗ nào để biết đã sửa được.

## Ràng buộc Tác giả đã chốt

- Không đưa con số nhịp / độ dài câu / độ dài đoạn vào SI (01/11).
- Không bắt brief của mỗi đoạn phải viết từng động tác, từng câu thoại của nhân vật (03/11).
- Brief ngắn, trơn — "brief dài chán, làm brief trơn" (09/11).
- Writer vẫn là Gemini trên AI Studio: mỗi lần viết = SI + một tin nhắn, chat mới. Gửi tiếp vào chat cũ: có thể (runner có
  `--chat`), nhưng chưa dùng.
- Brief viết tiếng Việt; văn ra tiếng Trung.
- Câu đạt / không đạt chỉ do Tác giả.
- Đừng làm hỏng thoại (Tác giả: "hơi ổn rồi").

Ngoài phạm vi lần này: đoạn 002/003 kể lại chuyện đoạn trước (Tác giả sẽ xử lý sau khi giọng ổn).

## Đã thử — chỉ liệt kê, không kết luận

Mọi lần chạy chat mới. Đoạn 003 dùng đúng gói đầu vào đã viết ra bản 003 đầu tiên (`gemini/test-giong/thoai-v1/prompt-003.md`).

| Lần | Đổi gì so với SI đang dùng | Bản ra | Tác giả |
|---|---|---|---|
| SI đang dùng | SI v2, Agent viết lại từ giọng bộ mẫu (4 anchor nguyên văn ch9 · ch30 · ch12 · ch7) | `chapters/doan-001..003.md` | "Dialog chưa đạt"; "tiếng bản địa, chữ cổ… cấn cấn" |
| thoại A / AB | mục 3 thoại viết lại + anchor ch6; AB thêm nhãn lạnh vào BANS | `gemini/test-giong/thoai-v1/` | — |
| thoại E | mục 3: "điều cả hai đã biết nằm trong đầu, MC nói ít nhất"; PART 2 bỏ "or mouth" | `gemini/test-giong/thoai-v2/` | — |
| bài ch3 | SI đang dùng trên chương 3 bộ mẫu, brief chỉ sự việc | `gemini/test-giong/thoai-v3/` | "Phần thoại hơi ổn rồi" |
| brief nước đi | brief 003 viết thành chuỗi nước đi giữa người với người, SI đang dùng | `gemini/test-giong/thoai-v4/` | — |
| SI-R | ROLE bỏ "earthy … village"; FIXED 1 thêm "plain modern 白话 of the anchors… no 俺, 瞅, 后生, 老汉, 老夫, 外头, 做甚"; BANS thay dòng tiếng động bằng dòng cấm 8 cụm sáo/chữ nhấn; nhánh RP cắt đuôi gói còn 300 字 | `gemini/test-giong/giong-v1/` | đọc R-003-a: 实打实 · 语气平稳得很 — "giọng AI" |
| SI-R2 | SI-R + dòng cấm nới thêm 实打实 · 紧实 · 沉甸甸 · 清清楚楚 · 干瘪 · 喉结滚动 · 冷不丁, "let the number carry the weight"; nhãn lạnh thêm 神色平静 · 语气平稳得很; viết 外边/后面/下面/昨天 | `gemini/test-giong/giong-v2/` | "Chẳng thấy thay đổi gì mấy, còn giảm chất lượng prose nữa chứ" |

Thinking của SI-R2 ghi: "carefully checking for banned phrases and words… replacing them with suitable alternatives".

## Tài liệu

Gốc link: `https://github.com/HaiPhongDao/Novel/blob/han-nien-san-dong/` + đường dẫn.

- SI đang dán vào AI Studio: `han-nien-san-dong/gemini/si-dan-gemini.txt`
- SI-R2 (bản bị bác gần nhất): `han-nien-san-dong/gemini/test-giong/giong-v2/si-R2.txt`
- Gói đầu vào đoạn 003 (thẻ + State JSON + đuôi đoạn 002 + brief): `han-nien-san-dong/gemini/test-giong/thoai-v1/prompt-003.md`
- Brief đoạn 001: `han-nien-san-dong/briefs/doan-001.md`
- Bản Writer: `han-nien-san-dong/chapters/doan-001.md`, `han-nien-san-dong/chapters/doan-003.md`; bản Tác giả đọc thấy 实打实/得很:
  `han-nien-san-dong/gemini/test-giong/giong-v1/R-003-a.md`, `han-nien-san-dong/gemini/test-giong/thoai-v1/A-003-a.md`
- Danh sách tật đếm được: `han-nien-san-dong/gemini/tat-giong-ai.txt`
- Một chương bộ mẫu để so giọng: `chung/hieu-chuan/loan-the/ch03/goc.txt` (và bản Writer cùng sự việc:
  `han-nien-san-dong/gemini/test-giong/thoai-v3/V2-ch03-a.md`)
- Khung SI chung của dự án: `writer/SI-template`
- Toàn văn bộ mẫu (174 chương, 1,2 MB) nằm ở nhánh `co-dai`, file `co-dai/乱世荒年：我每日一卦粮肉满仓！⊙1-174.txt` — cần
  thì Tác giả đính kèm.

## Định dạng trả lời

1. Nguyên nhân — mỗi ý một đoạn ngắn, chỉ ra dòng hoặc chữ cụ thể trong SI / gói bàn giao / brief / cách chạy.
2. SI đề xuất — toàn văn, dán thẳng được vào AI Studio.
3. Khuôn brief / gói bàn giao đề xuất (nếu đổi) — toàn văn, áp cho đoạn 003.
4. Cách kiểm trên đoạn 001 và 003.
