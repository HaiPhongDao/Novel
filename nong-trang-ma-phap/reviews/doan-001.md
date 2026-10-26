# Review đoạn 001 — bốn bản

Đoạn mở truyện đầu tiên; mục đích của bốn lần chạy là chọn **hình dạng prompt + SI**, không phải chọn câu chữ.
Chấm bằng `tools/soat_van.py` + `scripts/do_nhip_cau.py` + `tools/cham_doan.py`; cột `cham` chỉ để soát hồi
quy, canon 0/10 là **nhiễu** (bộ chấm đòi `回大人` của lane 领主, truyện này dùng `神父` / `管事大人`).

| bản | SI | brief | 字 | 字/câu | lượt · 字/lượt | phủ định | so sánh | nhãn | bảng | cham |
|---|---|---|---|---|---|---|---|---|---|---|
| a | v1 (kiến thức, không bảng) | chi tiết, 7 cảnh đánh số | 2.170 | 19,5 | 19 · 18,7 | 1 | 1 | 0 | không | 54 |
| b | v1b (sửa 1 bullet) | chi tiết, 7 cảnh đánh số | 1.695 | 19,7 | 17 · 20,9 | 0 | 1 | 0 | không | 66 |
| c | v2 (bảng 经验) | ngắn v1 (~250 từ) | 1.244 | 16,4 | 15 · 9,7 | 0 | 0 | 0 | 1 khối | 52 |
| d | v2.1 (bảng 经验) | ngắn v2 (~330 từ, đích 1.900) | 2.138 | 21,3 | 15 · 25,9 | 2 | 0 | 0 | 1 khối | **78** |
| e | v2.1 (bảng 经验) | ngắn v3 (~200 từ, bỏ dòng đếm lượt thoại) | 1.868 | 20,1 | 16 · 17,5 | 1 | 1 | 0 | 1 khối | 72 |
| — | mốc so: `tram-cuoi/chapters/chuong-001-a.md` (Tác giả cho 100/100) | | 1.543 | 23,6 | 16 · 22,6 | 1 | 0 | 0 | — | — |

## Đọc năm bản

**a (2.170 字)** — cảnh làng tốt (dê, phân ủ, luống ươm, Osric kể chuyện ong và con trai ở mỏ), nhưng có **bốn
chỗ người kể giảng**:
- `前世最寻常的急性痢疾，落在这穷乡僻壤就能轻易要了人命。` (thuật ngữ y học hiện đại trong lời kể)
- `神父嘴里的圣水，不过是混了薄荷脑和微量魔晶碎屑的井水罢了。` (giải thích thành phần)
- `盐巴补回泄掉的力气，甜蜜能顶两顿稀饭，水烧开了才能阻断疫病。` (ba vế giảng cơ chế)
- `魔晶能换来成堆的金币，却丝毫变不出半粒口粮。` (giảng kinh tế thế giới)
Ngoài ra `早已看不出前世敲键盘的痕迹` — nghề kiếp trước trong bible là ngoài đồng, không phải dân văn phòng.
Nguyên nhân nằm ở chính bullet tôi viết trong PART 4 v1: *"the mechanism is named once in plain narrator's
words"* — câu đó **mời** người kể giảng.

**b (1.695 字)** — sạch nhất về văn: 0 phủ định, không giảng khoa học, câu 19,7 字 (vẫn cụt hơn mốc 23,6),
nhịp chậm đúng ý (sương → cơ thể → sân → dê → phân ủ → luống ươm → hàng xóm). Lỗi canon: `他穿越到这处领地
刚满四十天` (领地 sai — anh là tá điền thuê 5 亩), `Ronan 伸手将摊在泥地上的妇人扶起` (Marta lúc đó đang
đứng, Writer tự đặt cô ta nằm), một chỗ capture hỏng: `不一整口生铁大锅烧得翻滚冒泡`.

**c (1.244 字)** — bản đầu có bảng. Hụt 17% so với cửa sổ, câu cụt nhất (16,4 字; 15 lượt thoại chỉ 9,7
字/lượt). Bảng bị **giảng**: `救下男童换来二十点经验，照看火塘又添了八点经验。想把普通村民训练成一阶，
足需要一百点经验才行。` Có nhãn ngữ điệu `淡淡说道` (tool bỏ sót, đọc ra). Cảnh đổ 圣水 vào nồi bị bỏ —
Writer cho `圣水早被 Ronan 倒掉`.

**d (2.138 字)** — bản có bảng và văn dày nhất: 25,9 字/lượt (mốc 22,6), 0 câu so sánh của người kể, 0 nhãn
ngữ điệu, mở chậm đúng nhịp Tác giả thích (sương → cửa → dê nhai lại → phân ủ ấm → luống ươm nứt hạt), cái
giá in đủ (2 银币 · 8 捆 · nửa hũ mật · một đêm), 圣水 **được đổ vào nồi** đúng beat, kết bằng việc (vác cào
đi về đống phân) chứ không bằng câu ngầu. Lỗi còn lại, cụ thể:
1. `“神父大人行行好…”` — sai xưng hô (glossary: `神父`, không `神父大人`); `大人` xuất hiện 2 lần.
2. `圣水不过是掺了微量明矾的井水，只有彻底烧开才好放心饮用。` — người kể giải thích thành phần, cùng tật
   với bản a (bullet "the mechanism is shown by his hands" chưa chặn hết).
3. `想要靠面板训练出一阶村民，眼下还得凑足一百点经验和三天的嚼裹。` — người kể giải thích bảng; đúng ra
   để con số tự nói (68 经验 / 100).
4. `堆肥的规矩容不得偷懒，少翻一次土，整堆粪料开春就会烂成一摊死泥。` — một câu châm ngôn nghề, đọc như
   sách dạy; cắt được.
5. Dài 2.138 字, hơn trần 2.100 38 字.

## Kết luận

**e (1.868 字) — bản theo prompt ngắn nhất (v3, bỏ dòng đếm lượt thoại).** Đạt: mở chậm (sương → nệm rơm →
dê gầy đi một vòng → phân ủ ấm tay → luống ươm nứt hạt), 圣水 bị đổ vào nồi và Ronan nói câu che `圣水要经大火
滚透才显威能` — đúng kiểu "làm rồi nói một câu ngắn"; kết bằng việc (đi về đống phân). Lỗi, cụ thể:
1. Writer tự đặt Piet **mười tuổi** (canon 7) và cho **Ronan tự xưng `小的`** với 神父 (`这两枚银币小的替她
   垫上`) — hai lỗi này đã sửa tay, ghi rõ ở đây; bản Writer nguyên văn ở `archive/doan-001-e-raw.md`.
2. `神父淡淡答道` — nhãn ngữ điệu (sửa tay thành `答道`).
3. Người kể vẫn giảng bảng: `治好一场要命的急热给二十点经验，比在地里死磕强出数倍。加上照料麦苗和翻堆肥
   给的八点经验，手头的积攒总算涨到了六十八。训练一个一阶村民需要整整一百点经验…` — ba dòng liền.
4. `这所谓的圣水不过是一小口普通山泉水。` + `在上辈子的医书里却是退高热的天然好药。` — hai chỗ giải thích.
5. Lượt thoại ngắn: 17,5 字/lượt (d: 25,9; mốc 22,6) — hệ quả của việc bỏ dòng đếm lượt: Writer chia lời
   thành nhiều lượt ngắn thay vì một câu trọn ý.
6. Bản Writer in ra **không có dòng trống giữa các đoạn**; đã chuẩn hoá lại khoảng trắng (không đổi chữ).

- **Prompt ngắn chạy được**: bản d (ngắn ~330 từ, có bảng) cho văn dày nhất và giữ đúng beat; bản chi tiết
  đánh số 7 cảnh (a, b) không thắng được cột nào ngoài việc ra ít lỗi canon hơn.
- **Prompt ngắn + cửa sổ độ dài thấp thì hụt** (c: đích 1.500–1.800 → 1.244, −17%); nâng đích lên 1.900
  (cửa sổ 1.700–2.100) thì ra 2.138 (+2% trần) — tức đích trong prompt là **mốc trượt**, không phải trần.
- **Tật còn lại của d thuộc tầng SI**: người kể vẫn giải thích cơ chế/bảng khi có dịp. Sửa tiếp bằng cách
  cắt một luật (bullet nào đang mời giảng) chứ không thêm luật; đo lại bằng đúng brief này.
- Đề xuất: lấy **d** làm gốc, sửa tay 5 chỗ trên (xưng hô, 3 câu giảng, 38 字), rồi mới chạy đoạn 002.

## Thí nghiệm prompt (26/10) — prompt của Tác giả vs prompt của Agent

Tác giả đưa một prompt kiểu "đặt hàng": độ dài + tag thể loại + một câu về **chức năng giọng** ("mượn lời MC
phán xét chế độ cũ/mới"), không beat, không số. Chạy trong `gemini/test/`.

| bản | prompt | 字 | 字/câu | lượt · 字/lượt | so sánh | cham |
|---|---|---|---|---|---|---|
| f | prompt Tác giả, 3 dòng, không dữ kiện | 2.893 | **26,3** | 17 · 29,5 | 3 | 66 |
| h | prompt Tác giả + 4 dòng dữ kiện canon | 2.430 | 17,4 | 34 · 13,8 | 4 | 38 |
| d | brief Agent (7 cảnh đánh số) | 2.138 | 21,3 | 15 · 25,9 | 0 | 78 |
| e | brief Agent ngắn v3 | 1.868 | 20,1 | 16 · 17,5 | 1 | 72 |

Đọc `f`: giọng tác giả **có** — MC so sánh nông cụ kiếp trước với cày gỗ 8–9 斤, chế bánh mì đen "đập vỡ sống
mũi", chế học giả "nông nô mỗi năm làm trăm ngày". Đó là thứ 5 brief trước của Agent **không hề** sinh ra, vì
brief chỉ có beat và số. Nhưng `f` trôi canon: 18 tuổi (canon 21), 3 亩 (canon 5), 经验 48 (canon 40), và cho
管事 vào chương 1 đòi 3 银币 丁税 (beat chương 2).

Đọc `h` (thêm dữ kiện): canon giữ được 11/13 mục, nhưng đổi lại câu vụn nhất bảng (17,4 字/câu, 24 câu ≤5 字,
34 lượt thoại ở 13,8 字/lượt) và 5 chỗ sai số/định danh:
1. `两枚银币能买下整整四十蒲式耳的粗燕麦` — tỷ giá canon: 2 银币 = 24 铜币 = **3 蒲式耳**.
2. `Marta 差四蒲式耳` — canon 3 蒲式耳; và tên `老Tom` không có trong bible.
3. `抽取四成甚至五成的秋税` + `收取十一税` — canon: 什一税 1/10 + 1 蒲式耳 人头税.
4. `比教皇的法杖还要管用` — canon là 圣廷, không có 教皇.
5. `【叮！救治重热病童，挽回劳动力人口。】` — bảng **không được nói**; và tổng in `【经验：60】` thay vì 68.

Kết luận: prompt của Tác giả thắng ở **giọng**, thua ở **số**. Muốn cả hai thì prompt phải có dòng dữ kiện,
nhưng dữ kiện viết thành **câu sự thật** (ai, bao nhiêu, còn mấy ngày) chứ không thành danh sách số, và phải
nói rõ bảng in đúng khối đã cho.

## A+B trên SI (v3) — đo lại bằng đúng prompt `h`

Sửa SI (không thêm anchor): (a) câu hỏi của MC phải mang dữ kiện + con số nghi ngờ; (b) câu từ chối phải
nêu người trước mặt + lý do/số; (B) lượt cầu–đáp đẩy **một** con số hay **một** điều kiện, và **một** dòng
đọc chen giữa hai lượt. SI 17.613 → 18.289 ký tự (+676).

| bản | SI | 字 | 字/câu | lượt · 字/lượt | lượt ≤6 字 | câu hỏi | nhãn | cham |
|---|---|---|---|---|---|---|---|---|
| h | v2.1 | 2.430 | 17,4 | 34 · 13,8 | **5** | 8 | 0 | 38 |
| h2 | v3 (A+B) | 3.004 | 19,8 | 29 · 17,5 | **1** | 4 | 3 | — |

Đọc `h2`: cuộc nói chuyện đổi hẳn tính chất. MC không còn hỏi rỗng; hắn **dùng số để bẻ** 神父:
`全村九户人家，今年的秋粮总共还差二十七蒲式耳。` → `Marta 家分摊了三蒲式耳的缺口。要是 Piet 今天死了…
这三蒲式耳麦子就彻底没人交了。` → `管事要是收不齐麦子…明年的什一税，神父大人打算找谁去收？` — mỗi lượt
đẩy một con số, và 神父 nhượng bộ vì con số của chính ông ta. Marta cũng có phần của mình (`我只有八十枚铜币`).

Lỗi còn lại của `h2`:
1. **Mâu thuẫn số**: Marta có `八十枚铜币` nhưng lại kêu không nổi `两枚银币` (=24 铜币) — thừa tiền mà kêu
   thiếu. Lỗi này do prompt không có tỷ giá và không nói Marta sạch tiền.
2. Bảng vẫn tự nói và in sai tổng: `【救助患病幼童（完成），经验+20】` + `【当前经验：60】` (canon 68).
3. Ba nhãn ngữ điệu mới: `语气平淡地说道` · `冷声说道` · `沉声吩咐道`.
4. `神甫的异端审判所` · `神廷` — canon là 神父 / 圣廷.
5. `四十年的人生常识` trong đầu Marta — canon Marta 34 tuổi.
6. Dài 3.004 字 (prompt đòi 2.000, +50%).

## Viết lại từ đầu (26/10) — bản i: SI v4 + prompt kiểu Tác giả có dữ kiện

Tác giả chê 002-a: thoại lượt nào cũng kết bằng `X 说道`, và mất giọng người xuyên việt so với đoạn 1 →
viết lại từ đầu. Hai thay đổi cùng lúc (không phải thí nghiệm một biến, Tác giả yêu cầu cả hai):
- **SI v4** (đổi 4 câu, +242 ký tự): luật "Every spoken line carries a tag" → thẻ chỉ ở chỗ cần biết ai nói,
  không bao giờ hai lượt liền của một người cùng gắn thẻ; PART 2 "One tag per line at most" → tối đa một lượt
  trong ba có thẻ; lời bình của anchor "all tagged" → thẻ đổi theo hành vi; giọng tính toán của MC "One such
  line to a scene" → hai ba dòng mỗi cảnh, ít nhất một dòng đặt lề lối cũ cạnh cái anh biết, có số.
- **Prompt**: nguyên ba dòng của Tác giả (độ dài · tag · chức năng giọng) + dữ kiện viết thành câu sự thật
  (tuổi, ngày tới làng, tiền + tỷ giá, Marta sạch tiền, việc chữa, bảng in đúng khối, xưng hô, chỗ dừng).

| bản | SI · prompt | 字 | 字/câu | câu ≤5 字 | lượt · 字/lượt | thẻ | so sánh | cham |
|---|---|---|---|---|---|---|---|---|
| e | v2.1 · brief ngắn v3 | 1.868 | 20,1 | 15 | 16 · 17,5 | — | 1 | 72 |
| 002-a | v3 · brief ngắn | 1.652 | 18,6 | 18 | 15 · 17,2 | **15** | 2 | 72 |
| h2 | v3 · prompt Tác giả + 4 dòng danh sách | 3.004 | 19,8 | — | 29 · 17,5 | — | — | — |
| **i** | **v4 · prompt Tác giả + dữ kiện câu** | 2.064 | 22,1 | **7** | 13 · 12,4 | **1** | 1 | 64 |

(cham 64 thấp vì band độ dài 1.500–1.800 và band 字/lượt của lane 领主 — nhiễu, xem cột thật.)

**Giọng xuyên việt — có, dày:** `自称一声小的少不了二两骨头，面对握着宗教特权的寄生虫，没必要正面起冲突。` ·
`井水沉淀一夜换取两枚银币，哪怕前世最暴利的走私行业都比不上这等买卖。` · `人命在现代人眼里是宝贵的劳动力，
在封建册页上却只是一串随时抹去的墨迹。` · `这群庄稼汉若是明白把粪堆沤熟能增产两成，多半会当场跪下高呼神迹。`
— khoảng 10 câu phán xét cũ/mới trải đều ba cảnh (5 bản trước gần như không có).
**Thoại:** 13 lượt, chỉ 1 thẻ; lượt đứng trần hoặc mở bằng một việc. Hết tật `X 说道` cuối mỗi lượt.

Lỗi:
1. (đã sửa tay) `前年男人死在采石场` → `去年男人死在石桥镇的矿坑里` (canon Marta). Raw: `archive/doan-001-i-raw.md`.
2. `去年隔壁村有个…幼童` — canon: đứa trước là người trong làng, tháng này. Để nguyên.
3. `前世在农业大学泡了七年` — chi tiết kiếp trước Writer tự đặt (bible: kỹ thuật viên nông nghiệp). Chờ Tác giả nhận vào canon hay không.
4. `两枚银币足够一个壮劳力…苦熬两个月` — lệch kinh tế (một bữa ở chợ = 2 铜币, 2 银币 = 12 bữa).
5. Odilo béo, chai `绿玻璃瓶` (canon: chai gốm, nút sáp); `像吞了干沙` — so sánh người kể.
6. Người kể giảng: thuật ngữ y học (`水杨苷`, `电解质失衡`) và bốn câu giảng bảng sau khối 【】 (`一百点经验就能将一名普通流民训练成…`).
   Thuật ngữ y học lần này đi cùng giọng phán xét Tác giả muốn — Tác giả quyết giữ hay cắt.
7. Thoại mỏng: 12,4 字/lượt, nhiều lượt cụt (`去教堂。`).

**Kết luận: SỬA NHẸ** — đạt đúng hai điều Tác giả đòi (giọng xuyên việt, hết đuôi `说道`); chờ Tác giả đọc
trước khi viết 002 theo cùng kiểu prompt.

## Bản j (26/10) — prompt Tác giả + một tình huống, dữ kiện thành "bối cảnh để giữ cho đúng", dừng sớm

Tác giả chê 001-i: "Writer tả và kể quá ít, bám vào dữ kiện để checklist, không có khoảng trống trong văn."
Nguyên nhân ở prompt: 001-i giao **cả chuỗi sự kiện chương 1** (Osric báo → mua 圣水 → chữa cả đêm → Piet
khỏi → giấy dán cửa) + danh sách vật dụng trong ~2.000 字, nên mỗi dữ kiện thành một dòng rồi qua việc kế.
Bản j: giữ nguyên ba dòng Tác giả; **một tình huống** (Piet sốt, 神父 định trói, Marta sạch tiền); dữ kiện ghi
là "bối cảnh để giữ cho đúng, không cần kể hết"; **dừng sớm** ở lúc Ronan cầm chai 圣水 vào nhà Marta (đêm chữa
và giấy dán cửa sang đoạn 2). SI giữ v4 — một biến.

| bản | 字 | 字/câu | đoạn kể | đoạn kể có số | đoạn kể ≥40 字 | 字/đoạn kể | lượt · 字/lượt | thẻ | nhịp câu |
|---|---|---|---|---|---|---|---|---|---|
| i | 2.064 | 22,1 | 73 | 38% | **0** | 25 | 13 · 12,4 | 1 | câu vụn |
| **j** | 3.092 | 27,0 | 83 | 33% | **19** | 30 | 23 · 15,7 | 1 | trong vùng |

Đọc j: mở chậm (hơi thở trắng → sương trên mái → tiếng khóc bên kia hàng rào), cảnh 神父 trong nhà Marta có
chất liệu (mùi bia chua, mỡ cừu, đá chậu gốm), một khối nội tâm dài về giá 圣水 so với cuốc sắt và bột đại mạch,
nợ ân tình cũ (Marta từng dúi nửa củ cải đường khi anh mới tới), và một quyết định có tính toán: **mua chai
圣水 làm "giấy phép", đổ nước đi, rót thuốc vỏ liễu vào chính cái chai có dấu thánh giá** — để nếu Piet khỏi
thì khỏi nhờ 圣水, không ai tố 巫术. Giọng xuyên việt dày (`本质上不过是一场垄断了识字权与药物解释权的合法敲诈`,
`买的是瓶子，买的是教会盖了戳的免死金牌`).

Đã sửa tay (raw: `archive/doan-001-j-raw.md`; bản Writer không có dòng trống giữa đoạn — đã chuẩn hoá, chữ giữ nguyên):
1. `神父大人` ×4 → `神父` (glossary: không dùng 大人 cho 神父).
2. `抽走你四成的粮食` → `抽走你的什一税和人头税` (canon thuế 1/10 + 1 蒲式耳).
3. `黑石矿场` → `石桥镇的矿坑` (canon: mỏ ở 石桥镇).
4. `前世做工程审计的同行` → `前世那些查账的人` (bỏ nghề kiếp trước Writer tự đặt).

Còn lại, để Tác giả quyết:
1. Dài 3.092 字 (prompt ~2.000, +55%) — độ dài đi theo khoảng trống Tác giả đòi; muốn ngắn thì dừng sớm hơn, không cắt tả.
2. Thuật ngữ hiện đại trong đầu MC: `三十九度`, `对乙酰氨基酚`, `布洛芬`, `漂白粉`, `大肠杆菌`, `渗透压`, `全网通报`.
3. Hai nhãn ngữ điệu (`神色平淡地吩咐道`, `语气很平静`), hai so sánh (`像烙铁一样`, `拉风箱般`).
4. Chi tiết mới: cuốc sắt 18 铜币; Marta cứu Ronan lúc mới tới (củ cải đường — sau lại nói "麦饼"); Burchard cưỡi ngựa.
5. **Mâu thuẫn trong bible**: 40 ngày mới được 40 经验 (Writer suy ra 20 经验 = ba tuần), trong khi glossary ghi một
   ngày công 5–8 经验. Cần Tác giả chốt một trong hai.

**Kết luận: SỬA NHẸ** — đạt điều Tác giả đòi (tả và kể, có khoảng trống), giữ giọng xuyên việt và hết đuôi `说道`.

## Bản k (26/10) — SI v4.1, cùng prompt j: lời Ronan nói với Marta

Tác giả bắt câu `石柱绑不得，绑上去天亮就收尸了。` của bản j. Soát cả cảnh: mọi tính toán tử tế của Ronan nằm
trong đầu, còn ra miệng với một người mẹ đang khóc chỉ có lệnh (`别哭了` + nhãn `语气很平静`), một câu phán
không chủ ngữ báo trước cái chết của con bà, và việc phải làm — không đáp chuyện tiền, không nói anh sẽ làm gì.
SI v4.1 đổi 2 câu (+362 ký tự): (a) câu ngầu chỉ nhắm người có quyền với anh hoặc chính anh, không nhắm người
đang sợ/đau/nghèo hơn; (b) với người đang sợ/đau, đáp đúng điều họ vừa nói (tiền, đứa con, anh sẽ làm gì) bằng
câu trọn có 你/咱们 rồi mới ra lệnh; lời phán về thế giới để ở lời kể. Prompt giữ nguyên bản j — một biến.

Lời Ronan với Marta, đặt cạnh nhau:

| j (SI v4) | k (SI v4.1) |
|---|---|
| `别哭了，Marta大婶。` (+ `语气很平静`) | `哪来的恶灵，这不过是脏水和风寒激出来的内热。` — đáp đúng câu bà hỏi |
| `石柱绑不得，绑上去天亮就收尸了。` | `要是让你们知道几碗煮透的柳树皮水就能退烧，神父还怎么卖两枚银币一瓶的圣水？` — câu phán thế giới, vẫn nói ra miệng |
| `你在屋里待着，烧上一锅热水，…` | `别发懵了，老规矩向来不是为了救人立的。` — **vẫn câu châm ngôn với người đang khóc** |
| `谁叫门都别把孩子抱出去，等我回来。` | `把眼泪擦了，先进屋把孩子抱上炕，拿干草盖严实。` |
| | `这事交给我，天黑前神父不会来抢人。` — trấn an + cam kết |

| bản | 字 | 字/câu | lượt · 字/lượt | thẻ | nhãn | so sánh | đoạn kể ≥40 字 | cham |
|---|---|---|---|---|---|---|---|---|
| j | 3.092 | 27,0 | 23 · 15,7 | 1 | 2 | 1 | 19 | 50 |
| k | 2.467 | 25,4 | 20 · 16,8 | 0 | 0 | 0 | 12 | 78 |

Đọc k: tốt hơn một nửa — Ronan đáp câu hỏi của Marta và hứa một việc cụ thể; hết nhãn, hết so sánh, ngắn lại.
Nhưng **2/5 lượt với Marta vẫn là lời phán** (`老规矩向来不是为了救人立的`), và Writer tự thêm câu người kể
`Marta 听不懂那些宏大的道理` — tức nó biết anh đang giảng cho bà. Khối phán xét dài nhất (`旧时代的统治术从来就这一招：
让你穷，让你怕，让你跪`) nằm đúng chỗ: lời kể/nội tâm.

**Giả thuyết (chưa thử):** dòng prompt của Tác giả `Mượn lời của MC để … phán xét chế độ cũ với chế độ mới` —
Writer đọc "lời" là lời **nói ra**, nên đặt câu phán vào miệng Ronan dù SI bảo để ở lời kể. Thử: đổi thành
"mượn suy nghĩ của MC và lời người kể" — cần Tác giả duyệt vì là câu của Tác giả.

Đã sửa tay (raw: `archive/doan-001-k-raw.md`): `神父大人` ×3 → `神父`; Marta tự xưng `小的` với Ronan ×2 → `我`
(glossary: ngang vai xưng 我). Còn lại: chẩn đoán hiện đại `急性扁桃体炎`, đơn vị `两石麦子` (canon 蒲式耳),
`赎罪皮纸` có dấu nhà thờ (chi tiết mới), chai cuối đoạn đổ nước sạch (j: rót thuốc vào chai — j hay hơn ở chỗ này).
Khoảng trống ít hơn j (đoạn kể ≥40 字: 19 → 12) nhưng vẫn gấp nhiều lần i (0).

**Kết luận: SỬA NHẸ.**
