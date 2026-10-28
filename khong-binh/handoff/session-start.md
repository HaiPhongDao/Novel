# Tài liệu bàn giao — tiếp tục viết truyện

Bạn là Writer của truyện này. Các đoạn trước bạn đã viết ở một session cũ; tài liệu dưới đây là toàn bộ những gì cần nhớ để viết tiếp đúng mạch và đúng giọng.

Đọc kỹ toàn bộ, rồi viết đoạn tiếp theo theo prompt ở phần cuối.


---

## 1. Thẻ thiết lập cố định

**Truyện:** 西幻·种田·争霸. 瑟兰魔导帝国 do pháp sư cai trị; ba vành 核心环/中环/外环, càng ra ngoài ma tố càng loãng. Phàm nhân (无源者, bị gọi 泥脚) bị cấm giữ vũ khí, cấm học chữ. Tiền: 1 金币 = 20 银币, 1 银币 = 100 铜币. Lúa mạch tính bằng 袋, 1 袋 = 4 银币.

**Nhân vật chính —** 洛伦·索恩, 19 tuổi, con thứ ba của 奥瑞克·索恩 (族长 索恩家族, pháp sư sáu sao, không mang tước). Đo 0 ma lực ở 测魔礼 (空瓶); bị cha cưỡng ép 灌注, cậu cũ chết, người xuyên việt tỉnh dậy. Giả lú, đổ cho 灌注. Làm 督政官 锈河属地. Trong đầu hay 吐槽, so với kiếp trước; nói ra thì gọn. Không dùng được phép.

**Bàn tay vàng —** nhớ tuyệt đối mọi trang sách, tài liệu, bản vẽ kiếp trước từng đọc, gọi lại như lật sách; không giao diện, không thứ gì phát sáng. 魔视 của pháp sư không thấy anh và máy anh làm: với họ chúng "trống".

**Nhân vật phụ**
- 赫伯特: 书记 phàm nhân 56 tuổi, kính gọng đồng, ôm sổ da dê; một trong ba người ở 锈河 có giấy phép biết chữ. Gọi 洛伦 là 大人, tự xưng 小人, mở lời bằng 回大人. Cẩn thận, hay sợ, thương dân.
- 加尔文·莫兰: 卫队长 của gia tộc, pháp sư hai sao, 34 tuổi, giáp da, tẩu đất nung, châm tẩu bằng lửa đầu ngón tay. Gọi 洛伦少爷; 洛伦 gọi 莫兰卫队长. Chán 外环, mỉa mai.
- 玛尔塔: thợ rèn 锈河镇, 28 tuổi, goá, giữ lò rèn của chồng, hai thợ phụ, con trai bảy tuổi. Nói thẳng.

**Địa danh**
- 锈河属地: rìa đông nam 外环; 18.000 phàm nhân ở 锈河镇 (~2.400) và 23 làng; sông 锈河 nước đỏ (dân gọi "nước máu", không dùng).
- 督政官邸: phòng ngủ treo thảm dệt 初代族长 格里芬·索恩 焚尽北境三万敌军于断矛山谷.
- 黑石属地 phía bắc (督政官 巴尔萨泽, ba sao); thành tự do 维林港 cuối sông.

---

## 2. State (JSON — sự thật và con số đã xảy ra, lấy đây làm chuẩn)

Đoạn tiếp theo viết từ ngay sau `scene_bridge.last_beat`. Những gì trong `already_told` người đọc đã biết: chỉ nhắc một chữ khi cần, không giải thích lại. Số liệu lấy theo `ledger`; ai biết bí mật nào theo `knowledge_map`.

{
 "meta": {
  "last_chapter": 1
 },
 "scene_bridge": {
  "time": "醒来当晚",
  "where": "督政官邸卧房",
  "present": "洛伦坐在床上僵住，盯着加尔文的手指；赫伯特跪在石板地上；加尔文靠床柱，叼陶烟斗吐烟",
  "last_beat": "洛伦问这世上当真有魔法，加尔文答：自然是有，洛伦少爷",
  "pending": "洛伦对魔法真实存在的反应，接着追问"
 },
 "timeline": {
  "relative_time": "醒来第一天夜；距秋税日120天",
  "chapter_log": [
   "1: 停尸房醒来，老仆喊诈尸；昏倒再醒装失忆；嫌饭问穷；问秋税；笑挂毯，见火指"
  ]
 },
 "already_told": [
  "洛伦魔力灌注后昏死三天，棺木已订",
  "官邸伙食：黑麦硬面包、盐水汤泡咸萝卜干；镇外平民吃橡子粉混草根",
  "前任督政官欠粮，入冬前被族长一道调令召回帝都，至今无口信",
  "后事花费：柏木棺材3银币、停尸白布40铜币",
  "锈河属地：帝国东南边缘，一万八千凡人，锈河镇+二十三村",
  "秋税日交一万二千袋大麦，剩一百二十天；去年只交八千四百袋，缺三千六百袋",
  "挂毯：初代族长格里芬·索恩于断矛山谷降天火全歼三万敌军"
 ],
 "ledger": [
  {
   "item": "秋税定额",
   "value": "12000袋大麦",
   "as_of": "ch1"
  },
  {
   "item": "去年实交",
   "value": "8400袋（缺3600袋）",
   "as_of": "ch1"
  },
  {
   "item": "距秋税日",
   "value": "120天",
   "as_of": "ch1"
  },
  {
   "item": "去年缺额折价",
   "value": "3600袋=720金币；今年定额12000袋=2400金币",
   "as_of": "ch1"
  }
 ],
 "deadlines": [
  {
   "what": "秋税日交12000袋大麦",
   "when": "120天后"
  }
 ],
 "main_character": {
  "name": "洛伦·索恩",
  "identity": "19岁，索恩家族族长奥瑞克三子，锈河属地督政官；测魔礼测出0魔力，被父亲强行灌注致原主死亡，穿越者附身",
  "traits": [
   "算账快，爱在心里吐槽、自嘲",
   "把难题当算术题"
  ],
  "status": [
   "对外装失忆，推说灌注烧坏脑子",
   "无魔力，不能用、感觉不到魔法"
  ],
  "knowledge": [
   "前世（现代）死于车祸；读过的书和图纸想起时逐字浮现，如翻书",
   "原主只记得名字",
   "刚得知此世有魔法"
  ]
 },
 "knowledge_map": [
  {
   "who": "赫伯特、加尔文",
   "knows": "洛伦醒后失忆",
   "not_know": "洛伦是穿越者、有前世记忆"
  }
 ],
 "characters": [
  {
   "name": "赫伯特",
   "role": "书记，凡人，56岁，管官邸账本",
   "notes": "黄铜眼镜，账册，胆小；管官邸账目二十年",
   "speech": "称洛伦“大人”，自称“小人”，开口“回大人”"
  },
  {
   "name": "加尔文·莫兰",
   "role": "家族卫队长，二星法师，34岁",
   "notes": "皮甲，陶烟斗，指尖燃火点烟；认为洛伦被灌注烧坏了脑子",
   "speech": "称洛伦“洛伦少爷”；洛伦称他“莫兰卫队长”"
  },
  {
   "name": "奥瑞克·索恩",
   "role": "洛伦之父，索恩家族族长，六星法师，无爵位",
   "notes": "强行灌注魔力",
   "speech": ""
  },
  {
   "name": "老仆",
   "role": "官邸擦洗尸体的老仆",
   "notes": "洛伦坐起时喊诈尸，撞门逃走",
   "speech": ""
  }
 ],
 "places": [
  {
   "name": "瑟兰魔导帝国",
   "notes": "法师贵族统治"
  },
  {
   "name": "锈河属地",
   "notes": "帝国东南边缘，锈河镇+23村，18000凡人"
  },
  {
   "name": "督政官邸",
   "notes": "有停尸偏厅；卧房墙挂索恩家族挂毯"
  }
 ],
 "objects": [
  {
   "name": "官邸账册",
   "notes": "牛皮账册，羊皮纸页，记23村丁口与秋税"
  },
  {
   "name": "索恩家族挂毯",
   "notes": "长袍老者推出天火烧三万军；赫伯特称初代族长格里芬为七星大魔导师"
  }
 ],
 "rules": {
  "world": [
   "1金币=20银币=2000铜币",
   "世界有魔法，法师贵族统治凡人",
   "1袋大麦=4银币"
  ],
  "mechanics": [
   "金手指：前世读过的书页想起时逐字浮现，如翻书；无界面、无发光"
  ],
  "hard_limits": [
   "洛伦无魔力，不能用也感觉不到魔法",
   "前世只说“前世”，不提真实地名",
   "无火药"
  ]
 },
 "open_threads": [
  "赫伯特称秋税日交不够，宗族惩戒骑兵会开进镇子 [ch1]"
 ],
 "conflicts": []
}

---

## 5. Nguyên văn phần cuối đoạn 1 (để nối mạch và giữ giọng)

“停尸房的白布花了四十枚铜币，要是少爷再多躺上两天，外面的坑都该挖好了。”
洛伦的腹部传出一阵沉闷的咕噜声。
三天水米未进的身板已经开始抗议。
“弄点吃的来，莫兰卫队长，我们稍后再谈棺材的事。”
赫伯特连忙应了一声快步跑出门去，不多时便端来一只粗陶大盘。
盘子里盛着半块黑麦硬面包，粗糙的表皮散发着松木锯末的气味。
旁边是一碗泛着灰白油花的盐水，泡着两截脱水的咸萝卜干与指甲盖大小的熏肉皮。
洛伦低头看着陶盘，眉头皱成一团。
前世即便是最简陋的养殖场，给牲口拌的麸皮饲料也比这碗汤水顺眼。
那块黑麦面包沉重得坠手，拿去当砌墙的石砖都嫌硬度过剩。
“督政官邸的厨房，每天就拿出这种东西招待主人么？”
赫伯特吓得弯下腰去，怀里的账册险些滑落到地上。
“回大人，这已经是官邸库房里最好的麦子磨出来的精粮了呀！镇子外的平民，整年都在吃橡子粉混野草根呢。”
“属地里二十三个村子的佃户，荒年里连发霉的黑麦糊都喝不上几口呢。”
加尔文咬着陶烟斗笑出了声。
“奥瑞克族长把你打发到锈河属地来，洛伦少爷，可不是让你来当贵族老爷享福的。”
洛伦端起陶盘，掰下一小块粗硬的面包放进嘴里。
面渣混着碎麦壳磨着牙龈，味道酸苦干涩，咽下去时喉管泛起一阵阵火辣辣的干疼。
他咽下面包，端起那碗飘着油脂的盐水汤灌了大半碗。
“锈河属地到底穷到什么地步，莫兰卫队长？”
加尔文从门边踱步走到窗台前，抬手推开了半扇木窗。
“瑟兰魔导帝国的东南边陲，除了烂泥滩就是含铁过重的红水，一万八千个凡人挤在镇子和村庄里刨食，连个齐整的铁匠铺都凑不齐。”
刺鼻的泥腥味顺着窗台涌进屋里，混杂着河道里铁锈氧化的微酸气味。
一万八千个凡人挤在二十三个村落和一个小镇里，光是维持温饱就已经耗尽了全部力气。
属地唯一的特产是河滩里捞出来的红泥，连低阶炼金学徒都懒得多看一眼。
洛伦将陶盘推到一旁，用粗麻袖口擦了擦嘴角。
肚里有了垫底的热气，思维开始按部就班地运转起来。
他需要弄清楚眼下最致命的危机。
“赫伯特，官邸账上最要紧的差事是什么？”
赫伯特慌忙翻开那本厚重的牛皮账册，枯瘦的手指在泛黄的羊皮纸页上划过。
“回大人，是秋税日的贡粮！距离秋税日只剩一百二十天了，今年属地要向宗族上缴一万两千袋大麦啊。”
老书记的额头渗出一层冷汗，指尖停在泛黑的墨迹上方。
“去年属地累死累活，也只凑出了八千四百袋，差额足足有三千六百袋呢。”
洛伦抬起眼帘看向老书记。
“去年差了三千六百袋，上一任督政官是怎么交差的？”
加尔文冷笑了一声，用烟斗柄指了指帝都的方向。
“上一任督政官大人欠下大笔粮食，入冬前就被族长的一道调令召回帝都了，至今连个口信都没传回锈河来呢。”
“帝都索恩堡的大门向来森严，那位前任是被扔进了水牢，还是在法师塔扫台阶，凡人谁能知道呢？”
赫伯特身子缩得更低，生怕厄运落到自己头上。
“大人，粮食收不上来，秋税日一到，宗族的惩戒骑兵就会开进镇子里，到时候大家都要倒霉的啊。”
洛伦靠在床头，目光落在那本陈旧的牛皮账册上。
一万两千袋是今年的定额，去年只收了八千四百袋，欠下的窟窿整整有三千六百袋大麦。
按照属地的官价，一袋大麦折算四枚银币，二十枚银币换一枚金币。
三千六百袋大麦折成现钱是一万四千四百枚银币，折合整整七百二十枚金币。
如果算上今年的应缴数额，官邸在四个月内必须交出价值两千四百枚金币的粮食。
对于一个只有一万八千凡人的荒凉边陲来说，这是一笔足以压断脊梁的重税。
在洛伦看来，这不过是一笔规模稍大的农业债务罢了。
一百二十天的时间虽然紧迫，但他脑海里存着海量的技术图纸与农耕典籍。
现代工业体系的零头，对付中世纪庄园经济绰绰有余。
改良深耕重犁能够提高荒地的翻耕效率，配制基础草木灰与骨粉足以催熟麦苗，借助水力磨坊更能缩短面粉加工周期。
只要把这一万八千个劳动力组织起来，七百二十枚金币的缺口完全可以在秋收前抹平。
解决眼前的债务危机只是第一步。
有了多余的粮食就能换来生铁与硫磺，有了铁器就能搭建水力车床与高炉。
要不了三年时间，锈河两岸就会建起连绵的厂房、矿坑与轨道。
到了那时候，什么宗族惩戒骑兵，在成排的线膛枪管面前都只是活动的肉靶子罢了。
视线从账册移开，洛伦打量起卧房的陈设。
正对床铺的粗石墙壁上，悬挂着一幅占满半面墙的厚重织锦挂毯。
挂毯用金线与深红丝线密织而成，画面正中央站着一名须发戟张的长袍老者。
老者脚踏焦黑岩石，双手高举向前推去，漫天狂暴的赤红烈焰席卷平原。
烈焰下方，密密麻麻的步兵与重甲骑兵在火海中翻滚哀嚎，断裂的长戟散落满地。
整座战场的惨烈氛围被织染得十分生动。
洛伦端详着那幅画面，嘴角扯出一抹好笑的弧度。
“这幅挂毯画得过于离奇了些，哪有人能凭空唤来漫天大火，一口气烧死三万大军呢？”
屋里的空气骤然凝滞了下来。
赫伯特吓得面色惨白，扑通一声跪倒在硬石板地上。
“大人，这话可万万说不得啊！”老书记以头抢地，膝盖骨撞在石板上咚咚作响。
“初代族长格里芬·索恩大人那是帝国记载的七星大魔导师，天火焚军是索恩家的立足根基，这怎么能说是夸张呢？”
加尔文握着陶烟斗，眼神里带着几分看待怪物的古怪神色。
“洛伦少爷，强行灌注魔力的反噬，看来真的把你的脑髓给烧糊涂了。”
洛伦只当是这帮落后的封建土著愚昧盲从，把祖辈的军功夸大成了神话。
没有内燃机与炸药的冷兵器时代，三万人列阵足以铺满整座平原。
单凭人体蕴藏的那点生物能，点燃一车干草都费劲，更遑论烧光装备精良的万人军团。
“三十个壮汉推着巨型投石机抛掷火油，也烧不出这种场面，除非那三万人排队站在干草堆里等着起风罢了。”
加尔文没有开口反驳。
他只是抬起右臂，在半空中打了一个清脆的响指。
噗的一声轻响。
加尔文的食指指尖上方，突兀地窜起一簇半寸高的赤红火苗。
火苗在微凉的穿堂风里欢快地跳跃，将男子粗糙的下巴映得一片通红。
加尔文神色自若地凑上前去，将烟斗里的干烟丝扣在火苗上方，深深吸了一口。
烟丝明灭间，蓝白色的辛辣烟雾在房梁下缓缓散开。
汉子甩了甩手指，那簇火焰随之消散在空气里。
洛伦浑身的骨节在这一瞬间彻底僵死。
脑海深处那些蒸汽轮机、高炉炼铁、流水线车间的精密图纸，在这一刻猛然卡壳。
他死死盯着加尔文焦黑的指尖，喉管干瘪地动了动。
“这世上……当真有魔法？”
加尔文吐出一口浓浊的烟圈，眼皮懒洋洋地耷拉下来。
“自然是有啊，洛伦少爷。”

(Đoạn 2 sẽ bắt đầu ngay sau chỗ này.)

---

## 6. Prompt đoạn tiếp theo

Viết đoạn thứ 2, khoảng 2500 chữ, bằng tiếng Trung.

【Thiết lập (để tham khảo, cái gì không dùng tới thì không cần viết ra)】
- 洛伦·索恩: 19 tuổi, người xuyên việt trong thân xác con thứ ba của 奥瑞克·索恩 (族长 索恩家族, pháp sư sáu sao, không mang tước). Đang giả lú, đổ cho lần 灌注. Không có ma lực, không dùng được phép, không cảm thấy ma tố. Bàn tay vàng: mọi trang sách kiếp trước từng đọc hiện ra rõ từng chữ khi anh nghĩ tới, như lật sách trong thư viện. Biết về đá và quặng từ những gì sách viết, không phải từ tay nghề.
- 赫伯特: 书记 phàm nhân, 56 tuổi, kính gọng đồng hai mắt, ôm sổ da dê; một trong ba người ở 锈河 có giấy phép biết chữ. Gọi 洛伦 là 大人, tự xưng 小人, mở lời bằng 回大人.
- 加尔文·莫兰: 卫队长 của gia tộc, pháp sư hai sao, 34 tuổi, giáp da, tẩu đất nung. Gọi 洛伦 là 洛伦少爷; 洛伦 gọi 莫兰卫队长; 赫伯特 gọi 莫兰卫队长 hoặc 卫队长大人.
- 玛尔塔: thợ rèn ở 锈河镇, 28 tuổi, góa chồng, giữ lò rèn của chồng.
- Thế giới: 瑟兰魔导帝国 do các gia tộc pháp sư cai trị, trên cùng là 魔导议会. Ba vành 核心环, 中环, 外环; càng ra ngoài ma tố càng loãng; pháp sư ở 外环 hồi ma chậm gấp ba và hay đau đầu. Pháp sư xếp bằng 星, một đến chín sao. Mọi pháp sư có 魔视: nhìn thấy ma tố quanh người và vật. Phàm nhân gọi là 无源者, bị cấm giữ vũ khí dài hơn cánh tay, cấm học chữ, cấm lập hội. Người đo ra 0 ở 测魔礼 bị gọi là 空瓶.
- Sổ của 锈河属地: 40 lính phàm nhân; kho bạc 312 金币; thu hoạch năm nay dự tính khoảng 9.500 袋; cống lương 12.000 袋; thiếu 2.500 袋. Mua bù: 1 袋 = 4 银币, 20 银币 = 1 金币, tức 2.500 袋 = 500 金币. Còn 120 ngày tới 秋税日.
- Sông 锈河: nước đỏ, dân gọi là "nước máu" và không dùng; đáy và bãi bồi là cát đỏ, nặng tay, lẫn hạt đen.

【Chuyện xảy ra trong đoạn này】
Mở ngay sau câu đáp của 加尔文 về phép thuật, cùng căn phòng ngủ, 洛伦 còn ngồi trên giường. Anh cười gượng cho qua cơn sững sờ: những gì kiếp trước coi là thường thức, sang đây còn đáng bao nhiêu thì anh chưa chắc. Rồi anh hỏi tiếp. Anh hỏi mình đã làm gì mà bị đưa tới chốn này; 加尔文 kể: 测魔礼 đo ra 0, giới pháp sư gọi anh là 空瓶, 族长 cần một chỗ để đặt cái tên. Anh hỏi ở đây có pháp sư nào khác không; 加尔文 kể ma tố ở 外环 loãng ra sao, đầu anh ta đau thế nào mỗi sáng, và pháp sư nhìn người bằng 魔视. 赫伯特 kể phần của phàm nhân: ba điều luật cấm; nói tới chữ thì ông nói nhỏ đi, vì ông là một trong ba người có giấy phép. Nghe xong, 洛伦 tự rút ra cho mình một tin tốt: pháp sư không ai muốn ở 外环, nên cả cái 属地 mười tám nghìn người này chỉ có một pháp sư canh, mà người ấy sáng nào cũng đau đầu.

Anh hỏi tới gia sản; 赫伯特 mở sổ da dê đọc từng mục, kèm phép tính phần thiếu. 洛伦 hỏi vì sao cống cao vậy; 加尔文 đáp: gia tộc nộp lên 魔导议会, phần ấy đẩy xuống thuộc địa. Anh hỏi 锈河 có gì bán được. 赫伯特 kể: lúa, cát sông, một lò rèn của bà góa 玛尔塔, con sông "nước máu" chẳng ai dùng. Muốn làm thêm thì không có người, đang mùa gặt; 赫伯特 nói nỗi lo ấy ra. 洛伦 đáp: ai bảo làm thêm thì phải thêm người. Anh ra cửa sổ nhìn con sông đỏ chảy qua dưới phủ, rồi sai một người lính mang lên một nắm cát bãi sông. Dưới ánh đèn anh xoa nắm cát giữa hai ngón tay, nhặt những hạt đen, đối chiếu với sách trong đầu, và hiểu con sông này là gì.

Anh ôm cây đèn sang phòng đọc, đòi thêm nến. 赫伯特 và 加尔文 ở lại trong phòng ngủ một lúc; 赫伯特 lo cho cậu chủ mới, 加尔文 bảo 灌注 làm cậu ta lú rồi. Qua đêm đó 洛伦 vẽ tới khi cháy hết nến: một chiếc 风箱 kiểu pít-tông hai chiều — ống gỗ, pít-tông bọc da, van da, kéo tới hay đẩy lui đều thổi gió. Lửa lò phải nóng hơn lò rèn thường thì cát kia mới thành được thứ gì; cái bễ là món đầu tiên anh cần. sáng ra anh trao xấp bản vẽ cho 赫伯特 mang ra lò rèn của 玛尔塔, rồi ngủ vùi.

【Những điểm bắt buộc】
- Các con số trong sổ đúng như thiết lập: 40 lính, 312 金币, khoảng 9.500 袋, thiếu 2.500 袋 = 500 金币.
- 洛伦 không nói cho ai biết anh nhận ra gì từ nắm cát; người đọc biết qua ý nghĩ của anh.
- Chuyện cậu chủ "lú" chỉ nằm trong lời của 赫伯特 và 加尔文 khi 洛伦 đã sang phòng đọc.

【Tự do sáng tạo】
Cách 赫伯特 đọc sổ, lời mỉa của 加尔文, những tính toán của 洛伦 về nắm cát, cách anh vẽ chiếc bễ (anh chưa nói tên nó với ai), những gì anh 吐槽 về ngọn nến, giấy da dê và bộ áo 督政官 — do bạn quyết.

【Mở đầu và chỗ dừng】
- Mở: ngay sau câu đáp của 加尔文, 洛伦 còn ngồi trên giường.
- Dừng: trưa hôm sau, 赫伯特 vào báo 玛尔塔 đã rèn xong linh kiện; 洛伦 bật dậy, vừa xỏ bộ áo 督政官 nhiều dây vừa bảo dẫn đường. Cảnh ở lò rèn thuộc đoạn sau.
