# Tài liệu bàn giao — tiếp tục viết truyện

Bạn là Writer của truyện này. Các đoạn trước bạn đã viết ở một session cũ; tài liệu dưới đây là toàn bộ những gì cần nhớ để viết tiếp đúng mạch và đúng giọng.

Đọc kỹ toàn bộ, rồi viết đoạn tiếp theo theo prompt ở phần cuối.


---

## 1. Thẻ thiết lập cố định

**Truyện:** Hạn Niên Săn Đồng (tên tạm). Cổ đại hoang niên, thôn Lão Nha Ao dưới núi Hắc Thạch, năm đại hạn thứ hai, đầu hạ. Núi đã bị huyện bán cho nhà họ Lữ; thẻ núi 80 văn/năm, thú săn trong núi nộp bảy phần ở cổng núi. Cái cân của người gác núi hụt hai lạng mỗi cân.

**Nhân vật chính —** Tần Dã (秦野), 17 tuổi, người thời hiện đại nhập vào thân xác cậu thiếu niên bị người gác núi đánh vì lén vào núi; sống với bà nội; nợ phạt 240 văn hạn ngày thứ bảy.

**Bàn tay vàng —** bảng kỹ nghệ (技艺熟练度面板) chỉ mình Tần Dã thấy. In một dòng 【技艺：名称（境界 数值/上限）】 mỗi kỹ năng, không lời thoại, không lời khuyên. Kỹ năng lên số khi cậu làm việc thật. Chỉ in khi cậu chủ động xem hoặc khi qua bậc, tối đa hai lần một đoạn.

**Nhân vật phụ** (chi tiết ở `bible/characters.md`): bà nội (奶奶), Liễu thẩm (柳婶), lý chính La (罗里正), Khâu Lão Thuyên (邱老栓), Ngưu Nhị (牛二), Lữ Tứ (吕四) người gác núi, Lữ Lục (吕六) gia đinh, Lữ Đức Tường (吕德祥) đại quản sự.

**Địa danh:** Lão Nha Ao (老鸦坳), Hắc Thạch (黑石岭), mương Đông (东沟), cổng núi (山门), huyện (县城, cách thôn 30 dặm).

**Luật cứng:** khế bán núi tính núi từ mốc đá trở lên; dưới mốc đá là ruộng dân. Mốc đá của ruộng nhà Tần cách bờ ruộng hai mươi ba bước. Tần Dã chưa có cung, chưa có dao củi.

---

## 2. State (JSON — sự thật và con số đã xảy ra, lấy đây làm chuẩn)

Đoạn tiếp theo viết từ ngay sau `scene_bridge.last_beat`. Những gì trong `already_told` người đọc đã biết: chỉ nhắc một chữ khi cần, không giải thích lại. Số liệu lấy theo `ledger`; ai biết bí mật nào theo `knowledge_map`.

{
 "meta": {
  "last_chapter": 2,
  "story": "古代荒年种田文：老鸦坳，黑石岭被县里卖给吕家；人名、地名、头衔一律写汉字"
 },
 "scene_bridge": {
  "time": "第1天清晨（天已大亮）；罚款限期还剩约六天",
  "where": "老鸦坳秦家院门口，正出门往村西罗里正家去",
  "present": "秦野手臂上缠着粗布，包着一整只洗净的兔肉（约三斤）；怀里有两张兔皮；奶奶扶着晃荡的木门框，望着他的背影，久久没挪步",
  "last_beat": "秦野拉开门栓，拎着布包走向村西罗里正家",
  "pending": "秦野到罗里正家，要请里正拿出山契、当众读原文并作证"
 },
 "timeline": {
  "relative_time": "第0天傍晚；第7天吕四来收罚款",
  "chapter_log": [
   {
    "chapter": 1,
    "summary": "醒来读记忆，否决煮盐酿酒；面板因绳结出现；柳婶借米换吕六量地消息；拿绳和镰刀起身"
   },
   {
    "chapter": 2,
    "summary": "黄昏顺东沟到自家豆地，见兔爪印和兔粪，从最上头田埂数二十三步到青石界石；下三个套；清晨两兔一断套，东沟底剥皮，面板更新；骗奶奶说是以前看赵老栓下套；整只炖汤；带第二只兔去罗里正家"
   }
  ]
 },
 "already_told": [
  "秦野穿越与死因",
  "原主因舍不得八十文被吕四打并罚三倍",
  "山牌价与山课七成",
  "吕四秤少二两",
  "兔子山门十二文县城三十文",
  "吕家挪界石吞王家地",
  "煮盐酿酒皆不可行",
  "面板首次出现及三行内容",
  "柳婶借米与二狗病情",
  "吕六拿绳在豆田上方土梁量地的消息",
  "秦野数出界石到豆地最上头田埂二十三步",
  "兔道与兔粪的发现",
  "三个套的位置与第一次剥皮、面板更新",
  "给奶奶的“看赵老栓下套”借口",
  "第一顿兔肉汤（整只炖了）"
 ],
 "ledger": [
  {
   "item": "铜钱（奶奶布包）",
   "value": "11文",
   "as_of": 2
  },
  {
   "item": "掺糠粟米",
   "value": "约3斤半",
   "as_of": 2
  },
  {
   "item": "罚款",
   "value": "240文，限七天，今天是第1天清晨（还剩约6天）",
   "as_of": 2
  },
  {
   "item": "兔",
   "value": "已吃一只（整只炖汤，祖孙分食）；另一只净肉约三斤，粗布包着在秦野手臂上；兔皮两张在秦野怀里",
   "as_of": 2
  },
  {
   "item": "面板",
   "value": "陷阱 入门45/100；剥皮 未入门18/100；种田 入门30/100",
   "as_of": 2
  },
  {
   "item": "价格",
   "value": "粟米9文/斤；县城肉10文/斤，兔30文；山门兔12文；山牌80文；山课七成；秤少二两；县城大酒楼两只兔六十文；兔皮一张三五文",
   "as_of": 2
  }
 ],
 "knowledge_map": [
  {
   "secret": "秦野是穿越者",
   "knows": [
    "秦野"
   ],
   "not_known_to": [
    "奶奶",
    "柳婶",
    "吕四",
    "吕六"
   ]
  },
  {
   "secret": "技艺面板",
   "knows": [
    "秦野"
   ],
   "not_known_to": [
    "奶奶",
    "柳婶",
    "吕四",
    "吕六",
    "里正"
   ]
  },
  {
   "secret": "山契原文（界石算不算在豆地之下）",
   "knows": [
    "里正"
   ],
   "not_known_to": [
    "秦野",
    "全村"
   ]
  }
 ],
 "characters": [
  {
   "name": "柳婶",
   "role": "邻居，寡妇",
   "notes": "四十出头，脸枯黄，三个孩子；二狗八岁腹胀；用吕六的消息换米",
   "speech": "叫奶奶“秦婆婆”，叫秦野“阿野”",
   "last_seen": 1
  },
  {
   "name": "吕四",
   "role": "吕家守山人（未出场）",
   "notes": "带大狗，用水火棍打人，秤杆灌铅，抽山课七成",
   "speech": "",
   "last_seen": 1
  },
  {
   "name": "吕六",
   "role": "吕家大管事的远房侄子（未出场）",
   "notes": "专管给吕家量地收租；今早拿结绳在秦家豆地上方土梁比画",
   "speech": "",
   "last_seen": 1
  },
  {
   "name": "王家",
   "role": "已逃荒的村民（提及）",
   "notes": "两亩水田被挪界石吞没；大儿子被打断腿；里正出示买山契不管",
   "speech": "",
   "last_seen": 1
  },
  {
   "name": "里正",
   "role": "村长（提及）",
   "notes": "手握谁也没见过的买山契",
   "speech": "",
   "last_seen": 1
  },
  {
   "name": "奶奶",
   "role": "秦野祖母；旁人叫秦婆婆；叙述中也称秦老太",
   "notes": "六十三岁，背驼，眼浑浊；怕秦野再进山；已信“以前看赵老栓下套”",
   "speech": "叫秦野“阿野”，自称“奶奶”",
   "last_seen": 2
  },
  {
   "name": "赵老栓",
   "role": "村里老光棍（Writer 新设，活人）",
   "notes": "年轻时进过山打猎，如今瘸腿，整天在东沟放羊割草，半大后生爱围着他；秦野拿他当看人下套的借口（Writer 原写邱老栓，已改，避免与 Khâu Lão Thuyên 混）",
   "speech": "",
   "last_seen": 2
  }
 ],
 "conflicts": [
  "[ch1] 山名误写“大青山” → 已改黑石岭",
  "[ch2] 邱老栓被 Writer 写成瘸腿老光棍放羊人，与 bible 邱老栓（55岁，ruộng sát mương）不合 → 已改成赵老栓（活人）",
  "[ch2] MC 记忆里已‘记得’契书内容，与 knowledge_map 里‘契书原文只有里正知道’有张力 → 003 当众读原文来验证，不改 bible"
 ]
}

---

## 4. Mẫu giọng (trích nguyên văn các đoạn đã duyệt — viết tiếp đúng giọng này)

---

## 5. Nguyên văn phần cuối đoạn 2 (để nối mạch và giữ giọng)

秦野擦了擦嘴，站起身，从屋角的干草堆里拎起了另一个布包。
那里头，包着第二只收拾得干干净净、分量毫不逊色的三斤肥兔。
老太太愣了一下：“阿野，这……这咋还有一只？”
“这只不能吃。”
秦野把布包在手臂上缠紧，遮得严严实实：“吕六昨儿已经量到咱家地头上来了，光靠这二十三步的规矩，拦不住恶狗硬抢。”
契纸在里正手里捏着。
吕家要想挪界石吞地，得过里正的眼；吕四要是借着罚款硬抢豆地，也得里正点头画押。
空着手去找里正，连门槛都进不去。
荒年里，三十文钱一只的紧实白肉，比县城大官的嘴皮子都管用。
秦野整了整粗布褂子，拎着沉甸甸的布包拉开了门栓。
晨光大亮，惨白的日光打在他单薄却挺直的脊背上。
秦老太扶着晃荡的木门框，布满老茧的干枯手掌死死攥着围裙角，浑浊的眼睛望着孙子迈向村西罗里正家的背影，久久没敢挪开步子。

## 6. Prompt đoạn tiếp theo

Viết tiếp đoạn tiếp theo, 2.000–2.500 字, bằng tiếng Trung.

Sáng ngày 1, nối thẳng từ lúc Tần Dã ra khỏi nhà. Anh đến sân nhà lý chính La (61 tuổi) và đặt con thỏ đã lột da lên bàn đá trước mặt ông. Lý chính đang ăn cháo loãng ngoài sân; Liễu thẩm và Khâu Lão Thuyên (55 tuổi, ruộng sát mương) cũng ở đó, chờ xin ông chia ít kê cứu đói. Trong rương gỗ của lý chính có bản sao khế huyện lập khi bán núi Hắc Thạch cho nhà họ Lữ. Cả thôn mới chỉ nghe Lữ Tứ nói mốc đá là ranh núi, chưa ai nghe ông đọc nguyên văn khế. Trong thôn đồn ông hay sang nhà họ Lữ ăn nhậu, và ông từng tát Vương Lão Thật khi người này đến kiện chuyện dời mốc. Tần Dã muốn lý chính đọc khế trước mặt hàng xóm rồi đi cùng anh lên đếm bước từ bờ ruộng tới mốc đá; anh sợ ông đóng rương lại. Lý chính muốn yên ổn với nhà họ Lữ, và cũng muốn có thịt cho nhà mình. Sau khi khế được đọc, cả nhóm lên sườn dốc, lý chính mang theo sổ của làng và cây bút lông.

Về ranh, khế chỉ tính phần núi từ mốc đá trở lên và không nhắc gì phía dưới mốc; câu về ranh được lý chính đọc nguyên văn trong đoạn.

Dừng ở lúc Lữ Lục, đang tuần trên sườn núi phía trên, thấy cả nhóm đứng gần mốc đá, quay người chạy xuống phía cổng núi.

Tên cố định: lý chính họ La (罗里正); huyện là 县城 (không phải 镇); Khâu Lão Thuyên (邱老栓) còn sống; núi Hắc Thạch (黑石岭); Lữ Tứ (吕四), Lữ Lục (吕六).
