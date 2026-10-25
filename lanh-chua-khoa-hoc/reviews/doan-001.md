# Review — Đoạn 001 (bốn bản thử, 25/10/2026)

> Chạy `tools/aistudio_run.py --new`, gemini-3.8-flash, thinking High. A/B: SI v1 + prompt v1. C: SI v2 +
> prompt v2. D: SI v2.1 (thêm FIXED CONVENTIONS) + prompt v3 (thêm tỷ giá).
> Đo bằng `tools/soat_van.py`. Chưa chốt đoạn nào.

## Số đo

| | A | B | C | D |
|---|---|---|---|---|
| Chữ Hán | 2.871 | 2.866 | 2.188 | **1.834** |
| Đoạn | 95 | 84 | 55 | 51 |
| Phủ định lặp (câu) | 5 | 5 | 5 | **0** |
| Phủ định bộ ba | 2 | 0 | 0 | **0** |
| 既…也… | 0 | 1 | 0 | **0** |
| 不是…而是… | 0 | 0 | 1 | **0** |
| 没 / 1.000 chữ Hán | 6,3 | 7,3 | 5,0 | **3,8** |
| So sánh của người kể | 3 | 1 | 1 | 1 |
| Từ hiện đại lọt | 6 | 0 | 0 | 0 |
| Tên giữ chữ Latin | ✅ | ✅ | ❌ phiên âm | ✅ |
| Phép tính trong đoạn | ✅ | ❌ | ❌ | ✅ |

## Tật "…không có, không có, không có" — nguồn gốc

Anh chỉ đúng. Và nó **không phải lỗi ngẫu nhiên của model**: ba nguồn trong nhà mình đang dạy nó.

1. **Chính SI v1.** Mục PART 4 có câu: *"It has no voice, no speaker, no page, no list; nobody hands it
   to him and nobody confirms it."* — một chuỗi bốn phủ định liên tiếp, đúng hình thức bị bắt. Model chép
   hình thức của SI trước khi chép nội dung (KB §1.4: SI và văn cùng ngôn ngữ thì từ vựng của SI lọt
   vào văn).
2. **Anchor số 1 của v1** (ch.1 女巫): *"熟悉的屏幕不见了，办公桌不见了，贴满纸条的墙壁也不见了"* — ba
   "不见了" liền nhau. Anchor dạy register mạnh hơn chữ nguyên tắc (KB §4.2), nên nó dạy luôn cái tật.
3. **Anchor số 3 của v1** (异界): *"…说的是2枚铜币，而不是20枚"* — dạy luôn khuôn "不是 A，而是 B".

Tần suất trong bản B: cặp phủ định rơi đúng vào các chỗ **giới thiệu nhân vật và mô tả trạng thái** —
"没有握过剑柄，更没有摸过农具", "没有亲手打过铁，更没有亲手修过门", "没有嘲讽，也没有敬畏，只有…",
"既没有下令，也没有叹气，只是…". Tức là khi Writer cần nói "anh ta thiếu gì / không làm gì", model lấy
khuôn sẵn có. Cách chặn không phải cấm chữ 没, mà là **cho nó một khuôn khác để thay**: tả người bằng thứ
tay đã làm và thứ họ mang theo.

## Đã sửa (SI v2 → v2.1)

| Sửa | Vì sao |
|---|---|
| Xoá mọi chuỗi phủ định khỏi chính SI; PART 4 viết lại khẳng định | cắt nguồn mẫu số 1 |
| 6 anchor → 3, **lọc anchor bằng `soat_van.py`**: anchor nào chứa phủ định lặp / bộ ba / so sánh người kể thì loại | cắt nguồn mẫu số 2 và 3 |
| Thêm CONSTRAINTS #4: *"A person is drawn by what their hands have done and what they carry… One lack in a paragraph reads as a fact; a second turns it into a list."* | cho Writer khuôn thay thế, và đặt trần 1 phủ định/đoạn |
| Tách PRINCIPLES / CONSTRAINTS, cắt SI từ 12.288 → 7.231 ký tự | KB §1.2 ngân sách ~2.000 token; SI dài làm loãng chú ý |
| Độ dài đích 1.500 字 thay vì 2.000 | KB §2.1: quá ~1.500 thì nửa sau văn trôi; A/B đều ra 2.870 khi xin 2.000 |
| Prompt theo 5 slot: state → 2 beat → ranh giới cứng → số → độ dài | KB §5.1; bản B tự mở tuyến đá xỉ vì prompt không có ranh giới cứng |
| Prompt ghi rõ **1 vàng = 100 bạc** | C tự bịa "1 vàng = 20 bạc" rồi tính ra 4,40 từ 9 − 4,60 → mâu thuẫn trong cùng đoạn |

Kết quả đo: phủ định lặp **5 → 0**, mật độ 没 **7,3 → 3,8** trên 1.000 chữ, độ dài **2.866 → 1.834**.
B-và-D so cùng nội dung, D là bản duy nhất đúng cả phép tính, tên Latin và không còn khuôn phủ định.

## Bản D — kết luận: **ĐẠT, sửa nhẹ**

Giữ nguyên:

1. Cách giới thiệu Osric: *"指关节因为常年握笔和拨动算盘而显得异常粗大"* — tả người bằng thứ tay đã
   làm, đúng luật mới, không một chữ phủ định.
2. Câu của Osric: *"生铁吃不得冷硬的力气，您敲第二锤的时候声调就已经发空了"* — người làm nghề nói
   bằng dấu hiệu nghe được; Emeric không chen một câu kỹ thuật nào.
3. Khối tính sổ: 9 vàng → 4,60 → 4,40 → thiếu 56,60, tỷ giá 1:100 được nói ra một lần rồi dùng.
4. Kết đoạn: viết 40, gấp sổ, Osric còn đứng chờ — đúng chỗ dừng, không trả lời.

Phải sửa:

1. *"兄长死在南边平叛的泥潭里"* — canon: anh cả chết vì bệnh hai năm trước. Lỗi canon, sửa ở prompt
   lần sau bằng cách ghi rõ nguyên nhân.
2. *"加上矿区那批还没遣散的采石工"* — nhắc mỏ/thợ mỏ ở đoạn 001, mở tuyến sớm. Prompt phải đóng.
3. Khoảng trắng giữa tên Latin và chữ Hán (*"Emeric 的两副膝盖骨"*) — do tên Latin đứng riêng; chỉnh
   bằng một câu trong FIXED CONVENTIONS nếu lặp lại ở đoạn 002 (chưa đáng sửa SI).
4. Vẫn còn 1 so sánh của người kể (*"平得像一块干木板"* cho giọng Osric) — đúng loại đã ghi trong
   `chung/review-blacklist.md`. Sửa nhẹ.

## Bản E — sau phản hồi về thoại, nhãn ngữ điệu và khuôn "实"

Tác giả bắt trên bản C: (1) "mỗi踩实一步" — khuôn **động từ + 实** làm giả độ cụ thể; (2) prompt của
Agent vẫn viết "không…, không…, không…"; (3) thoại cứng, cụt, thiếu thông tin, câu nào cũng dán nhãn
ngữ điệu.

Đã sửa: SI v3 (nguyên tắc 5 + CONSTRAINTS #5/#6/#7) và prompt v4 (ranh giới viết khẳng định, còn đúng
một chữ "không"; thêm dữ kiện Osric buộc phải nói ra: ai đến, bao nhiêu ngày, cái gì bị lấy, còn gì bán
được).

| | C | D | E |
|---|---|---|---|
| Chữ Hán | 2.188 | 1.834 | 2.028 |
| Lượt thoại | 30 | 24 | 25 |
| Chữ Hán / lượt thoại | 25,7 | 27,7 | **33,6** |
| Lượt cụt (≤6 chữ) | 5 | 5 | **4** |
| Nhãn ngữ điệu | 4 | 1 | **1** |
| Khuôn 实 | 1 (踩实) | 2 | **0** |
| Phủ định lặp | 5 | 0 | 2 |
| So sánh của người kể | 1 | 1 | 2 |

**E ĐẠT, sửa nhẹ.** Điều đáng giữ nhất: thoại của Osric giờ mang thông tin — "来的是派洛斯郡的主管
税务官，按规矩会带着十二名骑兵和两名法庭公证吏", rồi mở dần hậu quả: mất quyền thu phí đèo → hội
buôn tiếp quản → bò, sắt, cối xay → niêm phong → hạ tước vị. Đó đúng là kỹ thuật mới: trả lời rồi thêm
dữ kiện người nghe chưa hỏi.

Còn phải sửa ở E:

1. **Độ dài** 2.028 字, vẫn vượt đích 1.500 dù đã xin đúng. Ba bản liền đều vượt 25–35% — đây là phản
   xạ của model với loại cảnh hai bước, không phải lỗi prompt. Xem mục "Độ dài" bên dưới.
2. **Hai nhãn ngữ điệu còn lại:** "语气平稳得像是在报一件与自己无关的事", "Osric 的语气条理分明，
   毫无起伏". Câu thứ nhất vừa là nhãn vừa là so sánh của người kể.
3. **Phủ định quay lại trong thoại:** "不是本月的新账，是前年…" (khuôn 不是 A 是 B), "既没有牛，也没有
   两个月". Trong miệng nhân vật thì đây là biện pháp thật của tiếng Trung; giữ 1–2 chỗ/đoạn là được,
   nhưng cần theo dõi để nó không thành khuôn chung của cả truyện.
4. **So sánh "枯木桩"** — lần thứ ba trong bốn bản (A "烂木桩", B "旧桩子", E "枯木桩"). Đây là mẫu
   bám của model, không phải của truyện. Đã ghi vào blacklist.
5. **Xưng hô:** Osric gọi "少爷" — glossary chốt 大人.

## Độ dài — số liệu ba lượt

| Yêu cầu trong prompt | Kết quả |
|---|---|
| 2.000 字 (A, B) | 2.871 · 2.866 (+43%) |
| 1.500 字 (C, D, E) | 2.188 · 1.834 · 2.028 (+22…+46%) |

Vượt đều và vượt nhiều, kể cả khi đã hạ đích. Theo `builder knowledge.txt` §2.1 thì trần có ích là
~1.500 字, quá ngưỡng đó nửa sau văn trôi — mà ba bản vượt đều không có dấu hiệu trôi rõ. Đề xuất: xin
**1.400 字** và chấp nhận kết quả 1.800–2.000; đoạn ~2.000 字 giữ nguyên như repo, không cần đổi đơn vị.

## B và C

- **B** (anh thích): chất liệu tay nghề tốt nhất trong bốn bản — *"铰链底座脆化的转角"*, *"死沉，而且
  脆"*. Nhưng sai phép tính (viết thiếu 52 vàng) và mở tuyến đá xỉ. Nếu lấy B làm gốc thì phải sửa hai
  chỗ đó; D đã tự sửa cả hai nên tôi đề xuất lấy **D** và giữ chất liệu của B cho đoạn 006.
- **C**: đúng hướng nhưng phiên âm tên (vì SI v2 bị nén mất phần quy ước tên — lỗi của tôi, đã thêm lại)
  và bịa tỷ giá (vì prompt thiếu — đã thêm).

## Việc tiếp

- Tác giả đọc D; nếu nhận, tôi chạy D một lần nữa ở chat mới với prompt đã đóng hai lỗi (nguyên nhân
  chết của anh cả, không nhắc thợ mỏ), rồi mới chốt.
- Chưa chốt gì, chưa commit.

## Bản F và G — nhịp gặp nhau (sau phản hồi "chỉ nói việc, thiếu chào hỏi")

Tác giả bắt: hai người gặp nhau là lao vào công việc, thoại thuần chức năng; lúc Osric xuất hiện cần
vài lượt chào hỏi; mở đoạn của E chưa bằng B.

**Nguồn gốc:** nguyên tắc 6 (cũ là 5) của SI — *"a speaker gets room… the reply picks up what it answers"*
— đọc như lệnh "mỗi lượt phải đẩy cảnh". Prompt cũng không cho Osric thứ gì để chào. Sửa ở cả hai:
SI v4 thêm **nguyên tắc 5 "Two people in a room meet each other first"** (hỏi thăm, đồ mang vào tay,
chuyện tang, ai đến ai vắng, chuyện ngoài đường; việc chỉ bắt đầu khi một người mang nó ra); prompt v5
mở theo nhịp B và cấp chất liệu xã hội (quan tài chưa tế, ai đến cửa, con mèo trong kho cỏ).

| | B | E | F | **G** |
|---|---|---|---|---|
| Chữ Hán | 2.866 | 2.028 | 1.666 | 1.996 |
| Lượt thoại | 24 | 25 | 32 | 27 |
| Chữ Hán / lượt | 24,0 | 33,6 | 23,5 | **31,3** |
| Lượt cụt (≤6 chữ) | 5 | 4 | 7 | 5 |
| Nhãn ngữ điệu | 1 | 1 | 1 | 1 |
| Khuôn 实 | 2 | 0 | 0 | **0** |
| Phủ định lặp | 5 | 2 | 0 | **0** |
| So sánh của người kể | 1 | 2 | 1 | **0** |

F có nhịp chào hỏi tốt nhưng đánh đổi bằng lượt thoại ngắn (23,5). G lấy được cả hai: chào hỏi đủ, và
khi vào việc thì Osric nói đủ ý (31,3 chữ/lượt, 5 lượt cụt, 0 phủ định lặp, 0 so sánh của người kể).

Nhịp mở của G (giữ được chất của B):

- *"脖颈后的冷汗还没干透，黏在粗麻布的领口上，发凉。"* → ngồi dậy, nhìn hai bàn tay, mới nhận ra mình
  23 tuổi và vừa thoát chết.
- Chào hỏi thật: *"醒了就出来吹风，骨头又要招凉。"* + khăn + *"厨房里热水烧开了，但老奴没叫他们煮燕麦，
  等您看过了再定。"*
- Chuyện tang: *"还在小祈祷堂里搁着…老奴和两个杂役轮流守了三夜…没请修道士做弥撒，隔壁教区的修士要
  三枚银币的车马钱。"*
- Ai đến: chủ hàng thịt đến đòi bốn cân mỡ muối; họ hàng ở Veyra và hai nam tước phía tây không cử ai.
- Chuyện ngoài việc: *"干草棚里那只狸花猫，昨夜下了四只崽子。冻死了两只…"* rồi tự quay lại việc.
- Rồi mới tới bản lề, rồi sổ, rồi hậu quả cụ thể: phong kho, dắt bò, tháo chuông, mất đèo.

**G ĐẠT, sửa nhẹ.** Còn lại:

1. **Độ dài** 1.996 字 (xin 1.400). Bảy bản liền vượt 20–45% — chấp nhận, hoặc xin 1.200 ở đoạn sau.
2. **Một nhãn ngữ điệu:** *"声音低沉而平稳"*.
3. **Tên hội:** G viết 燧石公会; glossary chốt 火石行会. Thống nhất một tên.
4. **Lỗi nhỏ:** "公国铸币厂" trong khi truyện là 王国.
5. **Thay đổi cốt truyện cần Tác giả duyệt:** G để Osric tiết lộ ngay ở đoạn 001 rằng Verrick đã ngỏ
   ý mua quyền thu phí đèo 5 năm với giá 60 vàng, lãi gộp, quá hạn thì 30 năm. Bible đang để Verrick xuất
   hiện ở đoạn 009–010. Đề xuất của tôi: **giữ** — nó cho Emeric một lối thoát giả ngay trước khi anh
   viết số 40, và biến phản diện thành người đã có mặt từ đầu. Nhưng đây là đổi dàn ý, cần anh quyết.

## Bản H, I, J — nhịp câu (sau phản hồi "câu cụt, mất nhịp đọc")

Tác giả bắt trên G: *"脖颈后的冷汗还没干透…发凉。"* và *"二十三岁，刚捡回一条命。"* — câu cụt, mất nhịp.

**Nguồn gốc:** nguyên tắc 1 cũ (*"most paragraphs are one or two sentences… every few beats a single
line stands alone"*) cấp phép không giới hạn cho đoạn một mệnh đề; anchor cũng có một dòng đứng riêng.

Sửa theo ba bước, mỗi bước một biến:

| Bước | Luật thêm vào SI | Kết quả |
|---|---|---|
| v5 | mỗi đoạn là một câu có chủ thể; mệnh đề cụt gia nhập câu nó thuộc về; câu đứng riêng 3–4 chỗ/đoạn | H: câu cụt hết nhưng câu kể dài 39 chữ, thoại thành một trượt 6–7 mệnh đề |
| v6 | dấu chấm làm việc sau hai ba mệnh đề; mỗi lượt thoại 2–3 câu, mỗi câu một dữ kiện | I: câu 21 chữ, mệnh đề ≤4 chữ 9%, câu cụt 3 — nhưng 25 thẻ thoại cho 25 lượt |
| v7 | trao đổi chạy vài lượt bằng lời trần; tên quay lại khi cần; động từ nói đi với việc tay chân | **J: 6 thẻ/31 lượt, 1 thẻ đầu đoạn** |

| | G | H | I | **J** |
|---|---|---|---|---|
| Chữ Hán | 1.996 | 1.908 | 1.629 | 2.117 |
| Chữ/mệnh đề | 9,6 | 12,5 | 11,7 | 10,9 |
| Mệnh đề ≤4 chữ | 20% | 6% | 9% | 13% |
| Chữ/câu kể | 23,0 | 39,0 | 21,1 | 32,1 |
| Câu cụt (≤5 chữ) | 5 | 1 | 3 | 4 |
| Thẻ thoại / lượt | 3/27 | 4/16 | 25/25 | **6/31** |
| Phủ định lặp | 2 | 0 | 0 | 3 |
| So sánh của người kể | 0 | 0 | 1 | 2 |

**J ĐẠT, sửa nhẹ.** Giữ: nhịp mở (tỉnh dậy → tay → nhà → sân), chào hỏi (*"我躺了几天？"* — *"整整四天，
后半夜汗下来了"*), quà của làng (củ cải khô, cá muối), con mèo, câu hồi chuyển (*"说回这铁门"*), rồi
mới tới sổ và hậu quả.

Còn phải sửa ở J:

1. **Hai so sánh của người kể:** *"脆得像干麦饼"*, *"平淡得像在数石板上的裂纹"* — cái đầu nằm trong
   miệng Osric thì được, cái sau là người kể.
2. **Ba cặp phủ định** (trong thoại: *"他虽不是贵族，但…"*).
3. **"削好的铅芯"** — bút chì, quá hiện đại; thay bằng than củi.
4. **Độ dài 2.117 字** (xin 1.400).

## Bản K — xưng hô và đẳng cấp (sau phản hồi "nhân vật không đứng đúng vị trí")

Tác giả bắt: thoại của Osric không có kính ngữ, cách hành động không ra quan hệ trang viên Tây.

**Bằng chứng trong repo** — `lanh-chua-chip` (Tây huyễn, đã duyệt 15 đoạn) dùng: 少爷 **58**, 领主大人
**29**, 大人 **26**, 小人 **24**, 老爷 **6**, và **老奴 0**. Tra cứu thêm cách dịch my lord: 陛下 (chỉ vua)
khác 大人 (người dưới nói với lãnh chúa), 阁下 (bán trang trọng), 主人 (quan hệ chủ tớ).

**Sai của hai bản trước:** J dùng 老奴 3 lần (dạng Trung Hoa đế quốc, không có trong register của repo),
Osric không tự hạ mình, không có 回大人, MC gọi thẳng tên mà không có tư thế.

Sửa: `bible/glossary.md` thêm bảng **Xưng hô theo đẳng cấp (Tây huyễn)** (nam tước → 大人/老爷/领主大人;
quản gia → tự xưng 小的, mở báo cáo 回大人, đứng khi chủ ngồi; kỵ sĩ → 爵士; tu sĩ → 神父; phường chủ →
会长; trưởng thôn → 老丈; cấm 陛下/殿下 vì Vaulx là nam tước). SI v8 thêm một đoạn vào nguyên tắc 5:
đẳng cấp nằm trong từ họ chọn cho nhau, tư thế, ai ngồi ai đứng, 回大人, và chủ nói câu ngắn.

Kết quả K (1.781 字):

| | J | **K** |
|---|---|---|
| 老奴 | 3 | **0** |
| 少爷 | 0 | **0** |
| 大人 | 3 | **9** |
| 回大人 | 0 | **8** |
| 垂手侍立 | 0 | **3** |
| Thẻ thoại / lượt | 6/31 | **5/23** |
| Thẻ đứng đầu đoạn | 1 | **0** |
| Lượt cụt | 5 | **1** |
| Chữ/lượt | 33,1 | 31,2 |

Những chỗ K làm đúng, đáng giữ:

- *"大人，您这身冷汗总算发出来了。"* + *"躬身行了个幅度极浅的礼"* — lời thăm hỏi đặt trong khuôn kính ngữ.
- *"垂手侍立在三步开外，身板微曲，规矩地只盯着面前的石板。"*
- Dâng sổ: *"上前双手捧着奉过头顶，待 Emeric 接过去后便重新退回原处垂手侍立。"*
- *"回大人，下河村送来的芜菁掺了半数冻烂的…"* — báo cáo mở bằng 回大人 rồi mới tới chuyện.
- Chuyện ngoài việc vẫn còn: con mèo, *"小的瞧着领地耗子多，作主留下了两只"*.
- MC không giải thích: *"Emeric 没去辩解自己手生砸错了力道，只言简意赅道，"把账本拿来。""*

Còn phải sửa ở K:

1. **Xưng hô chưa nhất quán:** Osric lúc 小的 (2), lúc 老仆 (1). Chốt một: **小的**.
2. **Ba cặp phủ định** (còn trong thoại và một câu của người kể).
3. **Hai so sánh của người kể:** *"嗓音干涩得像羊皮纸在石板上摩擦"*, *"阴冷沉静"* (nhãn).
4. Độ dài 1.781 字 (xin 1.400) — gần nhất tới nay.

## Bản N — sửa theo thinking của Gemini

`aistudio_run.py --think-out` lần đầu cho thấy ba thứ (chi tiết ở `chung/ai-studio.md`): luật nhịp bị đọc
thành "strict one sentence per paragraph" (7 lần "one-beat-per-paragraph", 3 lần "single sentence"),
MC bị gọi nhầm là "Errick" và cảnh bị đặt ở "Flint Guild", và model tự nhủ "aiming to reach the character
count" rồi mở rộng cảnh để đủ chữ.

Sửa: SI v9 (luật nhịp đổi thành một/hai/ba câu tuỳ beat, bỏ con số; độ dài thành 1400–1800) + prompt v8
(liệt kê nhân vật kèm vai). Bản N: 1.599 字, thinking chỉ còn 1 lần "single sentence", 回大人 8, 0 thẻ
thoại, 1 lượt cụt — nhưng vẫn còn **"实打实" 2 lần** và 3 cặp phủ định.

## Bản O — lượt thoại đủ chủ ngữ và có người nhận

Tác giả bắt trên K: *"站久了有些发眩。"* — MC nói câu không chủ ngữ, không ai hỏi trước, mọc từ đâu không
rõ; Osric nói *"待会儿便送进书房"* mà không nói cho ai.

SI v10 thêm vào nguyên tắc 6: *"A turn stands on its own feet… 小的让灶房温了一锅麦糊，待会便给大人送进
书房; 我站久了有些发晕… a line with no antecedent waits until the scene asks for it."* Prompt v9 chép
sẵn hai dạng câu đúng.

| | K | N | **O** |
|---|---|---|---|
| Chữ Hán | 1.781 | 1.599 | 1.965 |
| Lượt thoại | 23 | 25 | 26 |
| Chữ/lượt | 31,2 | 35,3 | 36,8 |
| Lượt cụt | 1 | 1 | 2 |
| Phủ định lặp | 3 | 3 | **0** |
| Khuôn 实 | 0 | 2 | **0** |
| 回大人 | 8 | 8 | **9** |
| So sánh của người kể | 2 | 0 | 3 |

O làm đúng hai chỗ được bắt:

- *"我站久了，有些发晕。"* — có chủ ngữ, có nguyên nhân, và nó nối tiếp câu Osric vừa nói về việc anh dậy sớm.
- *"回大人，小的让灶房温了一锅燕麦糊，待会儿便给大人送进书房。"* — tự xưng, việc đã làm, người nhận.

Còn phải sửa ở O:

1. **Ba so sánh của người kể** — *"脆得像块结冻的干酪"*, *"面皮被冷风吹得像块干透的硬皮革"*, *"语气干涩
   得像是在念悼词"*. Đây là tật kế tiếp, cùng họ với "cọc gỗ" trước đó.
2. **Độ dài 1.965 字** (khoảng xin 1400–1800).
3. **Thẻ thoại 1/26 lượt** — dễ đọc nhưng nên có vài chỗ đặt tên khi ba lượt liền không ai được gọi tên.




