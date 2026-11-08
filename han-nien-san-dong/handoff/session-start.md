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
  "last_chapter": 1,
  "story": "古代荒年种田文：老鸦坳，黑石岭被县里卖给吕家；人名、地名、头衔一律写汉字"
 },
 "scene_bridge": {
  "time": "第0天傍晚（大旱第二年初夏）；罚款限期还剩约六天半",
  "where": "老鸦坳秦家茅屋内",
  "present": "秦野刚下炕，站在门后柴堆旁，右手攥着整卷粗麻绳（在腕上绕了两圈），左手握着锈镰刀；奶奶坐在灶边摸地上的骨针，嘴里念叨“这可咋办”",
  "last_beat": "秦野握紧锈镰刀柄，把麻绳在腕子上绕了两圈，挺直脊梁",
  "pending": "秦野带绳和镰刀出门；他仍认定唯一活路是再进黑石岭，但想先去看吕六今早站的地方（豆田上方土梁）"
 },
 "timeline": {
  "relative_time": "第0天傍晚；第7天吕四来收罚款",
  "chapter_log": [
   {
    "chapter": 1,
    "summary": "秦野醒来读完原主记忆，否决煮盐酿酒；面板因绳结出现；柳婶借米换吕六量地消息；他拿绳和镰刀起身"
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
  "吕六拿绳在豆田上方土梁量地的消息"
 ],
 "ledger": [
  {
   "item": "铜钱（奶奶枕下布包）",
   "value": "11文",
   "as_of": 1
  },
  {
   "item": "掺糠粟米（泥陶罐）",
   "value": "约3斤半（4斤减去借给柳婶的小半斤）",
   "as_of": 1
  },
  {
   "item": "罚款",
   "value": "240文，限七天，今天是第1天",
   "as_of": 1
  },
  {
   "item": "山牌",
   "value": "80文/年（旧价30文）",
   "as_of": 1
  },
  {
   "item": "粟米价",
   "value": "9文/斤",
   "as_of": 1
  },
  {
   "item": "生肉价（县城）",
   "value": "10文/斤；三斤山兔30文；山门只给12文",
   "as_of": 1
  }
 ],
 "main_character": {
  "name": "秦野",
  "status": [
   "饥饿",
   "无刀无弓，铁丝套和柴刀被吕四收走",
   "暂时认定活路在黑石岭"
  ],
  "knowledge": [
   "原主全部记忆",
   "山牌、山课、秤、罚三倍的规矩",
   "界石曾被吕家往里挪三十步（王家）",
   "县城兔价与山门价差",
   "面板三行：陷阱入门41/100、剥皮未入门12/100、种田入门30/100",
   "柳婶说吕六拿结绳在豆地上方土梁量地"
  ]
 },
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
 ]
}

---

## 4. Mẫu giọng (trích nguyên văn các đoạn đã duyệt — viết tiếp đúng giọng này)

---

## 5. Nguyên văn phần cuối đoạn 1 (để nối mạch và giữ giọng)

一只三斤沉的肥野兔，若是能全须全尾送到县城大酒楼或者肉铺，少说能换三十文钱。
可要是过了吕四的手，七扣八扣，再加上那缺斤少两的铁秤，到猎户手里能剩下十二文就该烧高香了。
更别说眼下他连进山的八十文山牌都没有。
手头唯一的一把割柴刀和原主积攒的铁丝，还全被吕四收走了。
土炕头靠墙的地方，放着秦老太平时纳鞋底剩下的一卷粗麻绳。
秦野右手搭在身侧，指尖无意识地碰到了绳头。
原主从小就在山林边缘转悠，虽然没正经跟猎户学过大本事，但打小跟着村里老人看过不少野路子。
指骨有些发僵，但手指搭上粗麻绳的瞬间，指尖仿佛有了自己的记忆。
掐头、绕环、压扣、穿结。
粗糙发硬的麻皮蹭着掌心的薄茧，几下翻转，一个活络的兔子套结就顺畅地在手里成形。
只需轻轻一拽绳头，套圈便骤然勒紧。
就在绳扣收紧的那一刹那，秦野眼前冷不丁晃过一道微弱的白芒。
半空中虚虚浮现出几行整齐古朴的字迹，悬停在他视线正中：
【技艺：陷阱（入门 41/100）】
【技艺：剥皮（未入门 12/100）】
【技艺：种田（入门 30/100）】
秦野猛地眨了眨眼。
字迹没散，依然清清楚楚地定在眼前。
老太太正低着头拿骨针纳鞋底，压根没往这边瞧，仿佛那片光影根本不存在。
原主以前偷摸学着下的那些套子，还真留下了底子，直接就是入门四十一。
“只要有数，就能涨。”
没有柴刀，还有麻绳；没有铁丝，还能搓草绳设悬吊陷阱。
陷阱能涨，剥皮能涨，只要能套到猎物，七天二百四十文就不是绝路。
但绝不能让奶奶看出半点异样。
原主是个闷头愣脑的鲁莽性子，要是突然变得老道周全，在这迷信的荒村，没准会被当成孤魂野鬼上了身。
还没等他把手里的绳套收起来，外屋破旧的木门“吱呀”一声被推开了。
门没栓，连个敲门声都没有。
一道干瘦灰暗的身影裹着一阵干热的风直接迈了进来。
“秦婆婆，阿野醒了没？”
进门的是隔壁的柳婶。
四十岁出头的年纪，头发乱糟糟地用一根木荆条挽着，脸色枯黄得像秋天干透的落叶，眼眶深陷，颧骨高高耸着。
柳家男人前年服徭役死在了北边，留下她一个人拉扯三个半大孩子。
荒年里寡妇带娃，日子过得比秦家好不到哪儿去。
秦老太抬起头，眯着浑浊的眼睛辨认了一下，叹了口气：“他柳婶子啊，阿野刚醒，喝了口汤……快进来坐。”
柳婶没坐，脚下像生了钉子似的停在炕沿边，一双手死死绞着洗得发白的粗布围裙，目光落在炕头的空陶碗上，喉咙不自觉地吞咽了一下。
“秦婆婆……我、我也是实在没法子了才厚着脸皮来开口。”
柳婶声音发颤，眼圈一下子红透了：“我家二狗……吃了两天白鳝泥拌苦菜，那肚子涨得跟个小鼓似的，硬邦邦的，拉都拉不出来，在床上直打滚哼哼……”
“大夫说要是再没有一口能克化的谷气顺一顺肠胃，怕是……怕是今晚都熬不过去。”
“婆婆，您借我半斤，不，三两碎粟米成不成？救救二狗的命！”
秦老太捏着骨针的手僵在了半空。
老太太嘴唇抖了抖，没说话。
借米？
陶罐里统共就剩四斤掺糠的米，那是秦野养伤和他们祖孙俩接下来几天的活命粮。
荒年借粮，借出去就是肉包子打狗，柳家拿什么还？
借了，自家人早一天断粮；不借，眼睁睁看着隔壁二狗被泥巴胀破肠子。
炕上的秦野看着柳婶那双绝望的眼睛，心里也是沉甸甸的。
半斤糙粮，就能压死一个孩子。
柳婶见秦老太不应声，身子猛地一矮，差点就要跪下去，嘴里急忙道：
“婆婆！我不白借！我知道咱家也难，阿野又挨了吕四的打……我拿信儿来换！”
“今儿一早，我带大丫去后山坡扒草根，瞧见吕家的吕六了！”
秦野眼神一凝：“吕六？”
吕六是吕家大管事的远房侄子，平日里专管给吕家量地收租，最是个刁钻刻薄的狗腿子。
“对！就是吕六！”
柳婶急促地喘着气，压低了声音，像是怕隔墙有耳：
“他手里拿着一根打了结的丈量绳，就在咱家那三亩豆地上面的土梁上来回晃荡！”
“他一边拿眼睛往秦家豆地里瞅，一边在地上拉绳子比画……嘴里还跟旁边的伴儿念叨，说什么这块地平整，土质也肥，引山泉水也近，正好能跟吕家刚圈的东山坡连成一片！”
秦老太手里的骨针“啪嗒”一声掉在了鞋底上。
老太太脸色煞白：“他们……他们这是算准了咱们凑不齐二百四十文，连地契都还没到手，就先来量地了？”
“何止是算准。”
去年的王家，不就是这么没的吗？
吕家硬说后山的界石往里挪了三十步，硬生生把王家祖传的两亩水田划成了吕家的山林地界。
王家去找里正评理，里正拿出那份盖着官印的买山契，说界石在哪儿山就在哪儿。
王家老汉气得吐血，大儿子去吕家闹，被打断了一条腿，全家老小最后只能挑着烂铺盖卷，连夜逃荒出了村。
如今这套把戏，原封不动地落到了秦家头上。
吕四要二百四十文，限期七天，根本就没打算让人能还上。
他们要的就是那三亩豆地！
要是七天后交不出钱，地被收走，秦野和老太太连这个冬天都撑不过去。
屋里静得吓人。
秦老太呆呆地坐了片刻，浑浊的眼角滑下一滴浑泪，随后叹了口气，扶着炕沿挪下地。
“作孽啊……都是穷苦人，二狗那孩子才八岁。”
老太太颤巍巍地走到墙角的陶罐前，拿起一个缺口的破木勺，在见底的陶罐里狠心舀了小半勺掺糠的碎粟米。
倒在柳婶带来的破布巾上，约莫也就小半斤。
“拿去吧，赶紧回去给娃熬汤喝……别放苦菜了，光熬米汤，先把肠子顺开。”
柳婶双手死死攥着那包粟米，眼泪哗哗地往下淌，扑通一声磕了个响头：“秦婆婆，大恩大德……等二狗活过来，我让他来给您当牛做马！”
“快走吧，救娃要紧。”
秦老太摆了摆手，整个人像是又苍老了十岁。
柳婶抹了一把眼泪，揣着布包，转身跌跌撞撞地冲出了屋门，急匆匆地顺着土路往自家跑去。
木门在风里轻轻晃荡，发出空洞的吱呀声。
陶罐里的米，这下只剩三斤半了。
钱袋里只有十一文。
吕六已经在外头拉绳量地，吕四手里的水火棍七天后就要敲上门来。
秦老太坐在灶台边，低着头去摸掉在地上的骨针，嘴里无意识地念叨着：“这可咋办……这可咋办啊老天爷……”
秦野撑着炕板，慢慢坐直了身子。
左肋依然隐隐作痛，但骨头没断，皮肉伤要不了命。
二百四十文山牌罚款，还有那三亩豆地。
山里的野兔三十文一只。
只要能弄到肉，只要能凑齐银钱，就能把地保住。
秦野伸手抓起炕头那卷粗麻绳，紧紧攥在手心里。
翻身下炕，脚踩在冰凉夯实的黄土泥地上。
他走到门后阴暗的墙角处，伸手拎起了立在柴堆旁的那柄割草铁镰刀。
刀身锈迹斑斑，刃口微卷。
秦野握紧刀柄，把麻绳在腕子上绕了两圈，挺直了单薄干瘪的脊梁。

(Đoạn 2 sẽ bắt đầu ngay sau chỗ này.)

---

## 6. Prompt đoạn tiếp theo

Viết tiếp đoạn tiếp theo, 2.000–2.500 字, bằng tiếng Trung.

Tình huống. Chạng vạng ngày 0 đến rạng sáng ngày 1. Tần Dã bước ra khỏi nhà với cuộn dây gai và cái liềm, nghĩ rằng đường duy nhất của mình là lại vào núi, nhưng trước hết anh muốn xem chỗ Lữ Lục đã đứng ngó xuống sáng nay. Ruộng đậu ba mẫu ven mương Đông (东沟) nằm ngay trên lối anh đi. Cả thung lũng khô nứt, đây là mảnh xanh duy nhất, và thú rừng chỉ xuống chỗ có cây xanh; luống đậu có lối thỏ đi, phân thỏ và cây đậu bị gặm cụt. Từ ký ức nguyên chủ, anh biết mốc đá đầu tiên của nhà họ Lữ trên núi Hắc Thạch (黑石岭) nằm trên sườn dốc phía trên ruộng; anh chưa biết khế viết gì về ranh núi. Anh muốn có thịt trước khi ba cân rưỡi kê hết và muốn việc săn nằm ngoài tầm của Lữ Tứ; anh lo Lữ Lục, gia đinh nhà họ Lữ đi tuần trên sườn núi, nhìn thấy anh. Anh dừng lại ở ruộng, đo bước từ bờ ruộng lên tới mốc đá, đặt ba cái bẫy thòng lọng trên lối thỏ, rồi về nhà ngủ. Rạng sáng anh ra xem: hai cái có thỏ rừng nặng chừng ba cân, cái thứ ba đứt dây, đầu dây còn dính lông vàng. Anh lột da hai con thỏ ngay bên mương, lần đầu làm việc này bằng tay của thân xác này, rồi mang một con về cho bà nội nấu: đây là bữa có thịt đầu tiên của hai bà cháu từ đầu năm. Bà nội hỏi anh học cách đặt bẫy ở đâu.

Khoá: cả ba cái bẫy nằm trong ruộng nhà Tần, dưới mốc đá hai mươi ba bước.

Dừng ở lúc Tần Dã xách con thỏ còn lại ra khỏi cửa đi về phía nhà lý chính La, bà nội đứng ở cửa nhìn theo. Chuyện ở nhà lý chính thuộc đoạn sau.

Bảng (in một lần, sau khi lột da xong, đúng nguyên dạng từng dòng; số đầu đoạn lấy từ State, dòng sẽ đổi trong đoạn thì để …):
【技艺：陷阱（入门 …/100）】
【技艺：剥皮（未入门 …/100）】
