# Review — đoạn 001 (vòng thử hình dạng prompt)

SI v1 (`gemini/si-dan-gemini-v1.txt`), cùng model, mỗi bản một chat mới, 27/10. Prompt: `gemini/test/vong-001/prompt-{a,b,c}.txt`.

| | a — sự việc tuần tự | b — khung đặt hàng (thể loại · thế giới · MC · hôm nay) | c — tối giản |
|---|---|---|---|
| Prompt (từ) | 248 | 283 | 119 |
| 字 | 1.973 | 1.793 | 1.530 |
| Dòng / 字 mỗi câu | 177 / 11,1 | 149 / 12,1 | 154 / 10,1 |
| Dòng 【】 | 9 | 14 | 9 |
| Lượt thoại | 34 | 21 | 12 |
| Dòng mở bằng 江野 | 9 | 7 | 9 |
| Tật đo được (phủ định, 实, nhãn, so sánh, thẻ) | 0 | 0 | 0 (+1 `不是…是…` tách dòng, máy không bắt) |
| Lệch canon | "三年前" ×3 (canon: năm năm), tiền tệ 联盟币/铜币 | 苏清寒 ra 极寒法师 (bible: 霜语者); `拿著` (chữ phồn) | "三年前", 联盟币 + 元, 手环, 基因药剂, 少校军衔 — thế giới trôi sang hiện đại; chuyển chức ở sân trường thay quảng trường |
| Tiền MC | 金币X4 银币X20 | 3 银币 40 铜币 | 312 联盟币 |

Cả ba bản sai tiền vì **brief không đưa số tiền và tên tiền tệ** — lỗi của brief, không của Writer (bible: 3.260 金币).

## Đọc

- **a** — Mở đúng: loa 镇守府, 30 ngày, rồi số thú triều; đám đông có người cụ thể (một lính đánh thuê cụt tay, một lão thợ săn) nói bằng số, đúng nguyên tắc 4. Đoạn đời MC dài và nhiều số (11.420 xác, 7 đồng một con) — chắc nhưng hơi kê sổ. Cảnh thức tỉnh C级 lạnh đúng tông: người tuyển mộ gạch tên anh. Sai năm.
- **b** — Đúng canon nhất (năm năm, 4,1 vạn học sinh, 镇渊军 tử 2,1 vạn). Có thêm câu tính toán trước khi lên đài ("总和24点… 韩擎 26点… 十二万金币淬体魔药"). Nhịp giống bộ mẫu nhất: 14 dòng 【】, màn hình lớn hiện kết quả công khai cho cả quảng trường. Kết bằng "chỉ anh thấy" hai dòng hệ thống. Thêm cảnh 苏清寒 thức tỉnh (prompt không bảo) — chấp nhận được, sai tên nghề.
- **c** — Giọng MC mạnh nhất: đoạn "他在计算" tự tính 30 ngày chỉ lên được cấp 8, 56 điểm, "活不过一分钟" — đúng kiểu MC lạnh tính bằng số. Kết bằng thời gian ngừng lại, ngầu. Nhưng prompt quá mỏng nên Writer tự dựng một thế giới hiện đại (tiền 元, vòng tay, thuốc gen, quân hàm thiếu tá) — sai register của bible.

## Kết luận về hình dạng prompt

**Hình dạng b** cho canon chắc nhất mà vẫn để Writer tự do cảnh: khối thế giới + khối MC + "hôm nay" làm Writer dựng đúng thế giới; prompt tối giản (c) cho giọng hay nhưng thế giới trôi. Dùng **b** cho các đoạn sau, và thêm vào khối số liệu: **tiền MC + tên tiền tệ (金币/银币), nghề của mọi người có tên trên đài**.

Bản đề xuất làm gốc: **b** (sửa nhỏ khi chốt: 极寒法师 → 霜语者, 拿著 → 拿着, tiền → theo bible hoặc đổi bible theo bản). Chờ Tác giả chọn.

---

# Vòng 2 — anchor thoại (27/10)

Tác giả: a/b/c **không đạt** — thoại như giọng kể. Nguyên nhân trong SI v1: P4 dặn đám đông "nói câu đầy đủ, so bằng tên và con số" → mỗi lượt đọc một chỉ số. SI v2 = v1 bỏ câu đó + luật DIALOGUE mới (người nói với nhau, lượt sau phản ứng lượt trước, số nằm trong phản ứng) + PRINCIPLE 5 với một anchor thoại nguyên văn bộ mẫu, mỗi bản một anchor. Prompt chung: hình b + tiền 3.260 金币 + 霜语者. SI: `gemini/test/vong-001-thoai/si-D{1,2,3}.txt`.

| | b (v1) | d — D1 ch1 thầy giáo tán chuyện | e — D2 ch14 nghi bia hỏng | f — D3 ch6 học sinh cãi nhau |
|---|---|---|---|---|
| 字 | 1.793 | 1.821 | 1.665 | 1.700 |
| Lượt thoại | 21 | 26 | 29 | 36 |
| Lượt đọc số trơn (có số, không hỏi/cảm thán/tiểu từ) | 6 | 5 | 7 | 3 |
| Lượt có phản ứng (hỏi, 吗/吧/呢, ……) | 1 | 5 | 4 | 5 |

Đọc: có cải thiện ở chỗ hỏi–đáp (d: "你那时候在北城？" → "我叔父死在墙根下…" — một người hỏi, người kia trả lời bằng chuyện nhà mình). Nhưng phần lớn đám đông vẫn là chuỗi lượt mỗi lượt một sự kiện (e dòng 33–41: năm lượt liền đọc số thú triều). Anchor thoại một mình không đủ: phần lời kể quanh thoại — 75–87% văn bản — không có nguyên tắc nào, nên giọng báo cáo của lời kể lan sang thoại. Tác giả chỉ ra đúng chỗ đó → vòng 3: nguyên tắc lời kể.

---

# Vòng 3 — nguyên tắc lời kể (27/10)

Tác giả: SI thiếu nguyên tắc cho phần lời kể (phần lớn văn bản). SI v3 theo `writer/SI-template` v4: NARRATION N1–N4 trước (chuỗi bước → dòng chốt về MC; giải thích là chuỗi lời nói có từ nối; ý nghĩ MC chảy vào lời kể bằng câu hỏi; người kể có giọng, 按理说…但…), MOMENTS sau (trận đánh, lý do bằng số / tiêu tiền / bia kỷ lục, thoại). Ba hướng chia anchor, cùng prompt vòng 2. SI: `gemini/test/vong-001-loike/si-v3{A,B,C}.txt`.

| | b (v1) | f (v2-D3) | g — v3A: anchor lời kể + anchor cảnh (6) | h — v3B: chỉ anchor lời kể (4) | i — v3C: chỉ anchor cảnh (2), lời kể là luật |
|---|---|---|---|---|---|
| SI (ký tự) | 5.125 | 5.806 | 6.629 | 5.832 | 4.426 |
| 字 | 1.793 | 1.700 | 2.043 | 1.851 | 1.811 |
| Dòng lời kể | 114 | 122 | 140 | 156 | 143 |
| Dòng lời kể mở bằng từ nối (至于/但/而且/所以/要知道/也就是说/按理说/不过…) | 0 | 4 | 9 | 10 | 5 |
| Câu hỏi trong lời kể (ý nghĩ MC) | 0 | 0 | 0 | 2 | 3 |
| Lượt thoại / lượt đọc số trơn | 21 / 6 | 36 / 3 | 28 / 2 | 11 / 1 | 16 / 1 |
| Chép nguyên anchor (chữ trùng 8-gram) | — | — | **95** | 0 | 0 |
| Tật máy đo | 0 | 0 | 0 | 0 | 0 |

## Đọc

- **g** — Lời kể có giọng ("这就是边城的现实。城墙如果破了，谁都活不下去。"), nhưng **chép khung anchor N1** gần nguyên câu (在进行转职之前。普通人的四项基础属性…也就是说。寻常学生…学校也是从这方面去推算…在他们看来…) và chạy từ nối như checklist (至于…确实…但…而且…所以… liền năm dòng). Sai canon: MC "tới thành này ba năm", "全校前十", gọi 6 điểm là "满值". **Loại.**
- **h** — Người kể nói với người đọc thật: 要知道。临渊城坐落在帝国最北端; 按理说…但去年…; dòng chốt "3名S级。丢进面对100,000头凶兽的战场上，连填战壕都不够。" Đoạn tính tiền đi bằng giá đồ (50 / 1.500 / 15.000) và kết ở "chỉ đủ mua hai món 白银". Ý nghĩ MC khi thấy X级 chảy vào lời kể: "这X级……到底算什么等阶？" Thoại ít (11 lượt). Sai: "五年前来到这个世界" (bible: xuyên lúc sơ sinh).
- **i** — Tốt nhất. Mở bằng giác quan rồi mới tới số ("从裂缝里刮出来的风，带着陈年腐尸的腥味"). Lời phán đúng tông nghiêm: "按理说，这种底子有很大希望拿到B级职业。但在临渊城，B级也只是高级些的炮灰。" MC tính bằng số đúng kiểu nhân vật: 800 抚恤 + 2.460 tự kiếm = 3.260, "只要备齐穿甲箭，30天内…也能在兽潮前升到10级" — và chính phép tính đó là cái X级 sắp đập vỡ. Canon khớp (18 năm, 3.260 金币, 1 金币 = 100 银币). Lệch nhỏ: 韩擎 ghi 二中 (bible: 一中).

## Kết luận

Nguyên tắc lời kể có tác dụng: cả ba bản v3 có giọng người kể (từ nối, lời phán, câu hỏi trong lời kể), ba bản trước có 0. Anchor lời kể **không cần**: i (luật lời kể, không anchor lời kể) hay nhất và 0 chữ chép; g (đủ anchor) chép 95 chữ. Mỗi hướng n=1, nên mới là dấu hiệu.

Đề xuất: **SI v3C** làm SI của truyện; **bản i** làm gốc đoạn 001 (sửa 二中 → 一中). Chờ Tác giả đọc.

---

# Vòng 4 — prompt một dòng, không nội dung (27/10)

Tác giả: v3 vẫn chưa đạt, thoại vẫn như cũ; thử prompt cực đơn giản. Prompt: "Viết đoạn mở đầu cho truyện mới, khoảng 2000 chữ, bằng tiếng Trung." + SI v3A/B/C. Bản: `gemini/test/vong-001-trong/T-{A,B,C}.md`.

| | T-A (v3A) | T-B (v3B) | T-C (v3C) |
|---|---|---|---|
| 字 | 2.339 | 2.281 | 1.520 |
| Lượt thoại | 13 | 14 | 14 |
| Chép nguyên anchor (8-gram) | 16 | 68 | 90 (cả câu 砰！嗡——轰轰轰轰轰轰！漫天的伤害数字纷飞！ của anchor trận đánh) |

Không có nội dung, SI tự lộ ra ba việc:

1. **Anchor thành khuôn cốt truyện.** T-A và T-B dựng lại nguyên khung anchor N1: "在进行觉醒之前…学校也是通过这些数据…而陈牧。力量10点…" — MC lại có bốn chỉ số 10 như 陆苍. T-B chép tiếp N3 (瞳孔微微缩起。这……) và N2 (至于…确实有卖。但…林越买不起。).
2. **Danh sách từ nối trong luật N2–N4 thành checklist.** T-C (không anchor lời kể) gom cả danh sách vào một đoạn theo đúng thứ tự trong SI: 至于… / 确实… / 但… / 而且… / 所以… / 要知道… / 也就是说… / 这……真的…？ / 岂不是…？ / 按理说…
3. **SI chứa dữ kiện của truyện.** Cả ba bản đều có bức tường, thú triều và "còn 30 ngày" dù prompt không nói gì — vì luật N4 viết "the wall, the dead, the thirty days".

**Thoại**: nhóm đông vẫn là người vô danh nói ra luật thế giới ("法师前期技能太少，施法还要原地站桩，单人根本没法练级。"). Chỗ thoại sống duy nhất là cảnh có **hai người có tên, mỗi người một mối bận tâm**: chủ nhiệm muốn xếp hai đàn anh kèm MC, MC từ chối ("学校可以安排两个二转的狂战士学长带你…" / "不用。" / "荒原上的变异兽不认人…" / "我心里有数。"). Bộ mẫu cũng vậy: ch1 hai thầy giáo có tên, xưng hô với nhau (刘主任). Kết luận: thoại hỏng chủ yếu vì **cảnh do brief giao là đám đông vô danh bình luận** và vì luật tông "grave, no jokes" bị áp cả lên nhân vật — đám đông của bộ mẫu sống nhờ cái thô, cái tục, cái khinh (你懂个屁, 啧啧), SI đã gọt hết.

---

# Vòng 5 — ba hướng sửa thoại X1/X2/X3 (27/10)

- **X1 (j)**: SI v4 (tông nghiêm chỉ cho người kể, nhân vật được thô; luật lời kể tả cơ chế, bỏ danh sách từ nối; bỏ dữ kiện truyện khỏi SI; anchor lời kể ch6, anchor thoại đám đông thô ch8) + prompt b cũ.
- **X2 (k)**: SI v3C + prompt có hai người có tên và mối bận tâm (赵小川 cần nghề chiến đấu để vào 镇渊军 lĩnh lương nuôi em; 何老 tới tuyển người cho hiệp hội).
- **X3 (l)**: SI v4 + prompt X2.

| | i (v3C, vòng 3) | j — X1 | k — X2 | l — X3 |
|---|---|---|---|---|
| 字 | 1.811 | 2.591 | 1.937 | 2.108 |
| Lượt thoại | 16 | 33 | 25 | 22 |
| Lượt đọc số trơn | 1 | 4 | 2 | 1 |
| Lượt có phản ứng (hỏi, tiểu từ, chửi, ……) | 3 | 10 | 6 | 4 |
| Chép anchor (8-gram) | 0 | 8 | 0 | 28 + **chép khung cả đoạn** |

## Đọc thoại

- **j** — Lần đầu đám đông thành người: "操，三十天，老天爷这是要逼死我们。" → "你还想切皮？先看看自己能不能转出战斗系吧。" → "要是转个F级的裁缝…你上去给蛮牛补裤头？" → "滚你妈的。" Mỗi lượt đáp lượt trước. Chỉ đổi SI (prompt cũ) mà thoại đã đổi → nguyên nhân chính là luật tông "nghiêm" bị áp lên nhân vật. Sai canon: "独自生活了十八年" (bố mẹ mất năm năm trước).
- **k** — Có người có tên nhưng 赵小川 kể hoàn cảnh nhà mình cho bạn thân vốn đã biết ("我家里还有三个弟妹，我父亲断了腿…") — lại là lời kể trong ngoặc. 何老 chỉ đứng nhìn, không nói. Prompt có người mà SI cũ không cho họ thô thì vẫn là báo cáo.
- **l** — Thoại hay nhất từ đầu tới giờ. 赵小川: "我要是转成个农夫，从钟楼跳下去能领抚恤吗？" / 江野: "领不到。" "镇守府刚改了告示，自绝的人扣发全额粮饷。" / "狗官。" Sau khi ra B级: "但我听说前线的治疗兵死得最快。" "魔兽专挑穿白袍的扑。" / "有军饷拿。" "先活到领钱的那天。" / "对，老子下个月能领二十枚金币了。" Đám đông: "三十万打底，有钱人家的孩子，命在娘胎里就标好价了。" **Lỗi**: chép khung anchor lời kể ch6 nguyên cả đoạn (觉醒了之后。他们就要考虑如何… / 一般这个时候。相熟的同学，就会凑在一起组队… / 家境优渥的，则是根据…特招要求… / 而底层的穷学生。则是打算…冲级 / 等级冲得越高…也就越大。); 何老 "四十一岁" lẫn với cấp 41.

## Kết luận

Thoại sửa được nhờ **cả hai**: SI cho nhân vật được thô (j) và prompt cho người có tên, có cái để lo (l). Còn lại một lỗi của SI: anchor lời kể bị chép thành khuôn đoạn (vòng 4 cũng thấy). Đề xuất **SI v4.1 = v4 bỏ anchor lời kể** (giữ luật N1–N4), chạy lại với prompt X2.

## Vòng 6 (27/10) — SI v4.1 (bỏ anchor lời kể N, giữ N1–N4) + prompt X2b

Prompt X2b = X2, chỉ sửa 何老 thành "từng lên tới cấp 41, nay ngoài năm mươi tuổi". Bản **m**: 1.754 字 (ngắn), 145 dòng: kể 105 · thoại 30 · hệ thống 10.

| | l (v4 + X2) | m (v4.1 + X2b) |
|---|---|---|
| Lượt thoại / đọc số trơn | 22 / 1 | 30 / 8 |
| 8-gram trùng SI | chép khung cả đoạn N | 0 |
| 何老 nói | không | không |

- Hết chép khung: bỏ anchor N là đúng chỗ. Tuổi 何老 đúng (53).
- Thoại tụt lại: 赵小川 lại kể hoàn cảnh nhà cho bạn ("我爸去年在城外矿坑断了腿…一个月领15枚银币"); đám đông lại thành người đọc bảng giá ("一件20级黄金重甲就要三十万金币…"). Còn sống: "赵家这小子走运了", "韩擎的动静太大，后面这些平民看着真乏味。"
- Lời kể đọc lại brief: "临渊城的货币分量很沉。/1枚金币能兑换100枚银币。"; "四项属性能够全满6点" sai (max 10).
- Kết đoạn tốt: C级 → 何老 nhổ thuốc → 【天赋：X级】 → 【您的职业正在进化……】.

**Kết luận.** Một bản không tách được "anchor N giúp thoại" với nhiễu giữa các lần chạy. l và m chỉ khác anchor N, nhưng thoại chênh 1 vs 8 lượt đọc số — cần ≥2 bản mỗi SI mới kết luận được.

## Vòng 7 (27/10) — tách nhiễu: SI v4 ×2 (n, o), SI v4.1 ×2 (p, q), cùng prompt X2b

| Bản | SI | 字 | Thoại / đọc số trơn | Chép từ anchor |
|---|---|---|---|---|
| l | v4 | 2.108 | 22 / 2 | khung đoạn N |
| n | v4 | 1.855 | 31 / 5 | khung đoạn N ("如果是战系。/哪怕只是个D级或者C级…要是不幸…") + nguyên câu anchor T "你懂个屁，有背景的人升级有多快，你根本想不到。" |
| o | v4 | 2.093 | 25 / 3 | khung đoạn N ("只要觉醒出…/哪怕仅仅是一个普通的B级…若是转职失败…") |
| m | v4.1 | 1.754 | 30 / 8 | 0 |
| p | v4.1 | 1.975 | 23 / 2 | 0 |
| q | v4.1 | 2.169 | 35 / 8 | 0 |

**Kết luận.**
1. Anchor lời kể N bị chép khung **3/3** bản v4, bỏ đi thì **0/3**. Lỗi do anchor, không phải nhiễu. → SI chốt là v4.1.
2. Chất thoại không đi theo anchor: v4.1 cho cả bản tốt nhất (p) lẫn hai bản tệ (m, q). Đây là nhiễu giữa các lần chạy → chọn bản, không sửa SI thêm.
3. Lỗi lặp 4/6 bản: 赵小川 kể hoàn cảnh nhà cho bạn đã biết (M3 đã cấm, không ăn). Ở o và p hoàn cảnh nằm trong lời kể, thoại thành hỏi–đáp có việc.
4. Lỗi prompt: "MC là người xuyên việt" không nói lúc nào → o "三年前", q "整整五年". Brief sau ghi "xuyên lúc sơ sinh, không nhắc".

**Bản tốt nhất: p.**
- Đám đông: "慌有个屁用，转出个生活职业，下个月照样去运滚木。"/"运滚木总比顶在城头送命强。"/"城墙要是塌了，躲在地窖里也得让凶兽嚼烂。"
- Hai tuyến người nối nhau: 赵小川 hỏi "后方医治营能预支军饷吗？", 江野: "去找何老，协会的野队收随队医师，一趟给3枚金币。" — cậu đi thẳng tới lều của 何老.
- 何老 nhìn MC: ba năm, hơn 700 xe, "C级赏金猎人。/跟他当年一模一样。"
- Cần sửa: "响起一片咽口水的声音" (tật của bộ mẫu); "四年前在渊口外围断了整条左臂" (canon: cụt tay, chưa định năm — để vậy được); "几十万人口" ≠ 600 vạn.

## Chốt (27/10) — Tác giả chọn **q** (q > o > các bản khác)

Tác giả: "Bản o với q tốt hơn, q > o". Agent đã đề xuất p — **lệch khẩu vị**, ghi lại để không lặp:
- Thước "lượt thoại đọc số trơn" chấm q tệ (8) nhưng Tác giả xếp q đầu. Thoại có số trong q mang ghen tị/khinh ("那又怎么样，人家生在苏家。" / "换你天天吃雪魄丹，你也成不了S级。" / "哪有闲钱养他这种穷鬼。") — thước đếm máy không phân biệt được. **Không dùng thước này để chọn bản nữa**; chỉ dùng để dò lỗi.
- Hai bản được chọn (o 2.093, q 2.169 字) dài và dày lời kể hơn p, m, n: thế giới có chất liệu cụ thể (loa phòng không đọc thông cáo, 韩擎 ra lệnh "下午我要进野狼谷", 何老 kể con 暴熊 50级 đập nát tay, giá sách kỹ năng 300 金币, sinh hoạt phí 8 金币/tháng).
- 赵小川 kể hoàn cảnh trong lời kể, thoại chỉ là cầu xin ngắn ("我求个C级就行，哪怕是挑大盾的也行。").

Sửa khi chốt: bỏ "穿越到这个世界整整五年。" (luật: xuyên lúc sơ sinh, không nhắc); thống nhất ba dòng 【转职成功：…】 thành 【恭喜您觉醒职业——…】. Ra `chapters/doan-001.md`, 2.167 字. SI chốt: v4.1 (`gemini/si-dan-gemini-v41.txt`).
