# Giọng MC trong lane 穿越/重生: "đầu óc người hiện đại" và câu châm của người kể

Dùng khi Tác giả nói dạng: *"thể loại này còn có giọng tác giả mượn lời MC để giải thích, thể hiện sự ưu việt của
người xuyên việt"*, hoặc *"MC lu mờ quá, mấy đoạn rồi chưa nổi bật"*.

**Cấu hình đã được Tác giả duyệt (giữ cái này trước): SI cũ nguyên bản + đúng một dòng sự thật `X là người xuyên
việt.` trong brief.** Không thêm khối vào SI cho giọng này; không kèm nghề cũ; không đặt "chỗ thắng" cho cảnh.

## 1. Luật nền: không gán tính cách

Tác giả chốt nguyên văn: *"Đừng gán tính cách vào MC, AI viết dở cái đấy. Tự writer quyết."* Nghĩa là:

- Không viết mục tính cách trong `bible/characters.md`, không thêm "hắn là kẻ…" vào SI hay brief.
- Không mở form 2–3 "hướng tính cách" cho Tác giả chọn. Cái cần cung cấp là **hoàn cảnh**: ai đang giữ quyền,
  hạn chót, cái giá, người đối diện, ai có quyền từ chối.
- Đừng lấy cảnh "thiếu cá tính" rồi đặt nhãn (`kẻ mở sổ`, `kẻ đi sửa đồ`) — nhãn ấy sẽ vào văn thành lời tự sự
  giả. Tính cách lộ ra ở **việc hắn làm và câu hắn nói**; Agent đo bằng trích dẫn, không bằng nhãn.

## 2. Dòng sự thật trong brief — trơn, không nghề, không "chỗ thắng"

Đúng một câu, viết như dữ kiện:

> Adrian là người xuyên việt.

**Không** thêm nghề cũ hay chữ "giỏi". Tác giả chốt: *"Prompt nên chỉ để MC là người xuyên việt thôi, bỏ giỏi
tài chính đi."* Dòng có nghề (`kiếp trước làm nghề tài chính — sổ sách, lãi, tỷ giá, chi phí, dòng tiền`) đẩy
Writer sang giọng máy tính tiền: 7 câu phủ định, văn 6/34, và MC đọc lên vẫn "trống không". Nghề cũ thuộc bible,
không thuộc prompt.

Cũng **không** viết "chỗ thắng" cho từng cảnh. Bản đầu tôi viết *"Đoạn này có đúng một chỗ để cái đầu kiếp trước
thắng: hắn định giá mười hai mạng thành 24 金币 (80% vốn)… Không giảng khái niệm"* và Tác giả bắt lỗi ngay, đúng
ở bốn điểm:

1. Nó chỉ định **nội dung suy nghĩ**, tức viết hộ cái đầu MC — cùng lỗi với chỉ định lượt thoại, chỉ đổi hình thức.
2. Mặc cả giá nô lệ **không phải** ưu thế người hiện đại — quản sự bản địa cũng làm thế; nó dạy Writer viết MC
   thành cái máy tính tiền, đúng thứ làm hắn lu mờ.
3. Nó **lặp** dữ kiện đã có trong brief (30 → 24 → 6, "tám năm chăn ngựa"), nên chỉ thêm lệnh, không thêm thông tin.
4. Nó **viết luật văn trong prompt** ("Không giảng khái niệm"), vi phạm luật 6 của mẫu prompt.

Đoạn nào không có tình huống để kiến thức cũ thắng thì **để trống** — đừng bịa một chỗ cho đủ form. Cái quyết định
"có phải ưu thế hiện đại hay không" là **cơ chế** (suất ăn, ca trực, tải trọng, ngày hỏng), không phải giá cả.

## 3. Đừng thêm khối vào SI — số đo ba đời

SI cũ đã có đủ chỗ cho giọng này (người kể đứng về phía MC, neo `开玩笑，那能让你们抢了经验吗？`, neo
`罗伯森前世见过的高楼大厦`). Vấn đề chỉ là thiếu **hạn mức**, và cách chữa rẻ nhất là dòng sự thật trong brief.
Mọi lần thêm khối vào SI đều kéo văn xuống:

| đời SI | ký tự | kết quả cùng cảnh |
|---|---|---|
| v9 (không khối) | 14.676 | 3.178 字 · 24,6 字/câu |
| v10 (khối 5 dòng) | 16.355 | 2.378 字 · 22,4 字/câu, 1 hit `前世` |
| v11 (khối 7 dòng) | 16.836 | 1.995 字 · 22,4 字/câu, 0 hit |
| v11 + brief "chỗ thắng" | — | **1.561 字 · 15,1 字/câu** — Tác giả: "văn phong kém đi nhiều" |
| v9 + dòng sự thật (duyệt) | 14.676 | **2.743 字 · 24,4 字/câu · 0 phủ định · cham 64** |

Nếu về sau vẫn thấy 0 hit ở ba đoạn liền thì chữa ở **cảnh** (mở phạm vi, thêm người có mặt, cho hắn một việc phải
tính), không phải bằng khối luật mới. Lý do kỹ thuật: luật đánh số trong SI bị đọc thành checklist, model nén câu
để đủ ý — thấy ngay ở cột `字/câu`, nên **soát `do_nhip_cau.py` ngay sau mỗi lần sửa SI**.

## 4. Câu từ chối, và cái thẻ thoại

Luật spoken shape của SI chỉ nói về **mệnh lệnh** (`起来吧 · 开个价 · 你给我…`), nên câu **từ chối** lọt: bản ra
`“不买麦子，一粒也不买。”` — một phủ định trần ném vào không khí — kèm thẻ `lắc đầu nói rằng` (người kể thuật lại,
không phải người đang nói). Tác giả bắt đúng chỗ này: *"MC vẫn nói kiểu trống không"*, và gợi ý dạng đúng
(`Chúng ta không mua lương thực…`).

Cách sửa đã đo: **amend một dòng có sẵn** của luật spoken shape, không thêm bullet mới —

> A refusal or a flat no is said to the man standing in front of him and takes him in: 咱们不买粮 · 你我不去, not a
> bare 不买麦子 stated to the air. The tag stays a spoken one (说道 · 摇头道 · 沉声道); 说 that / 说 rằng is the
> narrator summarising, not a man talking.

Bản sau khi sửa: `“咱们不买麦子。”Adrian 摇头道。` — 2.743 字, **0 phủ định**, 0 `实`, cham 64 (bản trước 2.114 字,
3 phủ định, cham 60). Cùng luật này dùng cho mọi câu từ chối trong truyện phong kiến, không riêng lane xuyên việt.

## 5. Bảng số đầy đủ để đọc lại về sau (đoạn 001, cùng brief gốc)

| bản | SI | brief | 字 | 字/câu | lượt · 字/lượt | phủ định | 实 | cham |
|---|---|---|---|---|---|---|---|---|
| H | v9 | dữ kiện | 2.461 | 21,2 | 21 · 28,5 | 6 | 0 | 56 |
| L | v11 | dữ kiện + dòng **có nghề** | 3.040 | 24,4 | 28 · 23,9 | 7 | 1 | 42 |
| M | v9 | dữ kiện + dòng **có nghề** | 2.114 | 22,8 | 20 · 22,6 | 3 | 0 | 60 |
| N | v9 (amend 1 dòng) | dữ kiện + **dòng trơn** | 2.743 | 24,4 | 23 · 20,2 | **0** | **0** | **64** |

Đọc bảng: dòng sự thật **trơn** + SI cũ là tổ hợp sạch nhất; dòng **có nghề** là thứ sinh phủ định (L, M); khối SI
là thứ làm câu vụn. Đừng cộng hai cái "mạnh" lại — chúng triệt nhau.

## 6. Bẫy khi đo

- **Đừng lấy từ khoá làm cổng.** Một bản không có chữ `前世` nào mà vẫn là bản cái đầu hiện đại mạnh nhất: hắn đổi
  cách chia khẩu phần thành suất theo ca (`每人每天三斤干麦` cho 41 người vào rừng, `半碗稀粥` cho 450 người ở lại)
  và mở cơ chế thay ca (`想吃饱饭的，明天就去替那四十一个人的班`). Bản có `前世` lại chỉ là một câu. Đọc ba đoạn
  (mở/giữa/kết) rồi mới kết luận.
- **Đừng để khối giọng biến thành bài giảng.** Dấu hiệu: câu dài ra, có mệnh đề "vì ở thời của hắn…", hoặc hắn
  giải thích khái niệm cho người bản địa. Câu đúng là câu **làm** (chia suất, mở cửa thay ca, nói ngày hỏng), không
  phải câu **giảng**.
- **Register phải có trong brief, không chỉ trong glossary**, và phải có ở **mọi** brief: thiếu thì Writer rơi về
  `大人`/`老爷` dù glossary đã chốt `少爷`, và lỗi ở đoạn đầu của chuỗi lặp sang các đoạn sau.

## 7. Hình dạng prompt khi Tác giả muốn "giọng tác giả": đặt hàng, không phải bảng việc

Bốn hình dạng prompt, cùng một cảnh nông nghiệp/đời thường, cùng SI:

| prompt | 字 | 字/câu | lượt · 字/lượt | canon |
|---|---|---|---|---|
| Tác giả, 3 dòng: `Viết đoạn mở đầu khoảng 2000 字` + tag thể loại + **một câu chức năng giọng** (`mượn lời MC phán xét chế độ cũ/mới`) | 2.893 | **26,3** | 17 · 29,5 | trôi: sai tuổi, sai 亩, sai 经验, kéo beat chương 2 vào chương 1 |
| như trên **+ 4 dòng dữ kiện dạng danh sách số** | 2.430 | 17,4 | 34 · 13,8 | gần đúng (11/13) |
| brief Agent đánh số 7 cảnh | 2.138 | 21,3 | 15 · 25,9 | đúng |
| brief Agent ngắn (~200 từ), không beat | 1.868 | 20,1 | 16 · 17,5 | đúng |

Đọc bảng: **chỉ prompt của Tác giả đạt band nhịp của SI (22–30 字/câu)**; mọi prompt liệt kê beat/đánh số sự việc đều ra 20–21 字/câu và bị `do_nhip_cau.py` chấm "câu vụn". Câu chức năng giọng là thứ duy nhất sinh ra đoạn "người kể phán xét": so sánh nông cụ kiếp trước với cày gỗ 8–9 斤, chế bánh mì đen "đập vỡ sống mũi", chế học giả "nông nô mỗi năm làm trăm ngày". Brief beat không sinh được câu nào trong số đó, vì nó chỉ nói *việc gì xảy ra*, không nói *ai đứng ra phán*.

Cái giá: không dữ kiện thì Writer tự đặt canon (tuổi, diện tích, 经验, và kéo beat chương sau vào chương 1); còn dữ kiện **dạng danh sách số** thì câu vụn và lượt thoại mỏng (17,4 字/câu, 34 lượt/13,8) — danh sách số đọc như checklist, đúng cơ chế đã đo ở mục 3.

Cấu hình đề xuất: **prompt 3 dòng của Tác giả + 3–5 dòng dữ kiện viết thành câu sự thật ngắn** (ai, bao nhiêu, còn mấy ngày, tỷ giá, khối bảng in nguyên dạng), không beat, không đếm lượt thoại, không phán "chỗ thắng". Sau khi chạy, kiểm bốn chỗ Writer tự đặt khi thiếu dữ kiện: tuổi/tuổi nghề, diện tích hay số người, tỷ giá tiền–hàng, và beat nào bị kéo từ chương sau vào.


## 8. Bài học thực chiến từ Manga Tokyo 2000 (Đoạn 001: Tam giác sai lầm qua 3 lần chạy)

Ghi nhận ngày 31/10/2026 trên truyện `manga-tokyo-2000` (đô thị văn ngu, xuyên việt Tokyo 2000, SI v5):

### Bảng số đo và lỗi qua 3 lần chạy

| Lần | Hình dạng Prompt / Brief | 字 | 字/câu | Điểm văn (`soat_van.py`) | Hiện tượng & Lỗi gặp phải | Đánh giá của Tác giả |
|---|---|---|---|---|---|---|
| **v1** (bản A/B/C) | Brief thuần dữ kiện sự việc + SI v5 kìm nén (không có chức năng giọng) | 2.917 | 24,1 | 34/34 | **Trôi tuột, thiếu sảng điểm:** MC thụ động như khúc gỗ ngầu lòi, Morishita tự kinh ngạc tự cược cả tiền thưởng cuối năm; thiếu hẳn góc nhìn tương lai, tucao thời đại cũ. | *“Mọi thứ xảy ra quá trôi... MC là người xuyên việt nhưng không thấy góc nhìn từ hắn nhiều lắm? Cái điểm sảng... không phải là biết trước xu hướng, góc nhìn ưu việt của người tương lai, đánh giá châm chọc thời đại cũ sao?”* |
| **v2** (bản sửa) | Brief nhồi kịch bản chi tiết: chỉ đạo MC chê 3 điểm, Morishita bắt bẻ bằng 7 thư từ chối, MC dồn ép đe dọa mất ghế + sửa SI PART 1 §2 | 3.850 | 25,3 | 34/34 | **Soạn sẵn kịch bản, nhồi rác vào prompt:** Prompt phình lên 4.000 từ. Agent viết hộ thoại và cảm xúc. MC biến thành loa phát thanh diễn thuyết, mất tính tự nhiên. | *“Brief này đang phạm lỗi 'soạn sẵn kịch bản / sổ kết quả' và nhồi rác vào prompt... Chuyển toàn bộ số liệu vào state.json. Viết lại brief tối giản để Writer và SI tự đấu trí.”* |
| **v3** (bản tối giản + pack) | Brief 3 câu tình huống tối giản + dán nguyên gói Handoff Pack (Canon Card + Voice Anchor + State JSON thô 120 dòng) | 2.238 | 23,5 | 34/34 | **Ngộ độc dữ kiện, văn loạn xạ nhảy cóc:** Model Gemini bị quá tải thông tin, coi State JSON như checklist cần thanh lý. Hai nhân vật xa lạ lúc 2h45 sáng vừa gặp nhau đã xả liên thanh: 36 tiếng, 38 vạn bản, 50% tiền cọc 88.000, cấu trúc kịch bản 2 tầng, Kurosawa Daiki... Thoại nhảy cóc liên tục, không có nhịp thở hay tương tác hành vi người thật. | *“Càng không đạt, viết quá loạn xạ.”* |

### Cơ chế đằng sau: Vì sao sửa lỗi này lại đẻ ra lỗi kia?

1. **Từ Trôi tuột sang Soạn sẵn kịch bản (v1 → v2):**
   - Khi phát hiện văn thiếu ma sát và thiếu điểm sảng, Agent có xu hướng 'cầm tay chỉ việc', viết hộ từng đòn đánh tâm lý của MC vào brief.
   - Hậu quả: Prompt biến thành kịch bản phân cảnh đóng đinh, tước đoạt quyền tự suy luận của Writer và kích hoạt chế độ 'dịch từng gạch đầu dòng' của LLM.
2. **Từ Soạn sẵn kịch bản sang Ngộ độc dữ liệu / Loạn xạ (v2 → v3):**
   - Khi được yêu cầu tối giản brief và chuyển dữ liệu sang State JSON, Agent đã thực hiện máy móc bằng cách gom cả Canon card, Voice anchor và bảng JSON thô vào tin nhắn mở đầu (`session-start.md`).
   - Ở đoạn 001, model chưa có ngữ cảnh chạy trước. Khi nhìn thấy một bảng JSON đầy ắp số liệu chi tiết và mối quan hệ, cơ chế 'chú ý' (attention) của LLM bị phân tán: nó cố gắng nhét tất cả các con số vào cuộc đối thoại đầu tiên để 'không bỏ sót dữ kiện'.
   - Kết quả: Nhân vật hành xử như hai nhân viên văn phòng đang đọc báo cáo tài chính lúc nửa đêm, các chủ đề nhảy từ hạn in kẽm sang cấu trúc kịch bản rồi sang phó tổng biên tập chỉ trong 4-5 lượt thoại.

### Quy tắc chốt (Actionable Rules)

1. **Đoạn mở đầu (001) tuyệt đối không dán raw State JSON vào prompt:**
   - State JSON chỉ là kho lưu trữ của Agent để đối chiếu sau khi sinh văn.
   - Prompt đoạn 001 chỉ cần: Dòng tag thể loại + chức năng giọng (mượn đầu óc hiện đại tucao/giáng chiều) + 3 câu tình huống sống tại chỗ (vật lý, tiền nợ trước mắt, người đối diện mang vấn đề gì đến).
2. **Ma sát thật phải đi từ hành vi vật lý đến nghề nghiệp, không đi từ thuyết trình:**
   - Bước 1: Giao dịch vật lý (lon cà phê, tiền thối, ngón tay ám mực).
   - Bước 2: Quan sát và buột miệng một câu nghề nghiệp (chỉ ra một vết gạch chéo hoặc chi tiết nhỏ, không nói hết bức tranh lớn).
   - Bước 3: Nghi ngờ và phòng thủ tự nhiên của người đối diện (không phải màn bắt bẻ hùng biện).
   - Bước 4: Lật giở sản phẩm thật (bản vẽ/trang giấy) để hình ảnh tự thuyết phục, không để MC giảng bài về lý thuyết làm phim.
3. **Cổng kỹ thuật (34/34 văn phong) không chứng minh cảnh viết đạt:**
   - Điểm soát từ ngữ và nhịp câu chỉ là điều kiện cần. Phải luôn đọc thẩm định cảnh theo tương tác hành vi trước khi báo cáo.
