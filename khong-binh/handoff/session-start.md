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
  "last_chapter": 2
 },
 "scene_bridge": {
  "time": "醒来第二天正午",
  "where": "督政官邸卧房门口",
  "present": "洛伦刚睡醒，系好督政官长袍最后一根皮绳跨出门；赫伯特眼镜歪斜，捧布包在前",
  "last_beat": "赫伯特报玛尔塔照图打成铁铰链和长轴，洛伦系紧长袍：带路，赫伯特，我们去铁匠铺验货",
  "pending": "铁匠铺组装风箱"
 },
 "timeline": {
  "relative_time": "醒来第二天正午；距秋税日约119天；秋收抢工将至；夏末",
  "chapter_log": [
   "1: 停尸房醒来，老仆喊诈尸；昏倒再醒装失忆；嫌饭问穷；问秋税；笑挂毯，见火指",
   "2: 问空瓶、魔视、禁令、底账；捏河砂识出磁铁矿砂；通宵画双动活塞风箱"
  ]
 },
 "already_told": [
  "洛伦魔力灌注后昏死三天，棺木已订",
  "官邸伙食：黑麦硬面包、盐水汤泡咸萝卜干；镇外平民吃橡子粉混草根",
  "前任督政官欠粮，入冬前被族长一道调令召回帝都，至今无口信",
  "后事花费：柏木棺材3银币、停尸白布40铜币",
  "锈河属地：帝国东南边缘，一万八千凡人，锈河镇+二十三村",
  "秋税日交一万二千袋大麦，剩一百二十天；去年只交八千四百袋，缺三千六百袋",
  "挂毯：初代族长格里芬·索恩于断矛山谷降天火全歼三万敌军",
  "测魔礼测出零，帝都称空瓶；族长为体面把他塞到偏远属地",
  "外环魔素稀薄，施法多花三倍冥想，加尔文每早头疼",
  "法师用魔视看人，平民是灰影",
  "凡人禁持长过一臂铁器、私结社杀头、全属地仅三张识字许可",
  "索恩家族向魔导议会缴魔晶配额，族长摊派到属地",
  "锈河水血红，平民不敢用，喝了腹痛；河滩红砂"
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
  },
  {
   "item": "卫兵",
   "value": "40名平民",
   "as_of": "ch2"
  },
  {
   "item": "库房",
   "value": "312金币",
   "as_of": "ch2"
  },
  {
   "item": "今年预计收成",
   "value": "约9500袋，缺2500袋=10000银币=500金币；库金全掏仍差188金币",
   "as_of": "ch2"
  }
 ],
 "deadlines": [
  {
   "what": "秋税日交12000袋大麦",
   "when": "120天后"
  },
  {
   "what": "秋收抢工，各村无闲人",
   "when": "快到了"
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
   "刚得知此世有魔法",
   "河砂黑粒是高品位磁铁矿砂，锈河是天然重选矿脉（未告诉任何人）",
   "全属地只一个天天头疼的二星法师看着——视为好消息"
  ]
 },
 "knowledge_map": [
  {
   "who": "赫伯特、加尔文",
   "knows": "洛伦醒后失忆",
   "not_know": "洛伦是穿越者、有前世记忆"
  },
  {
   "who": "赫伯特、加尔文",
   "knows": "洛伦捏河砂、通宵画图",
   "not_know": "砂铁矿判断、图纸是什么"
  }
 ],
 "characters": [
  {
   "name": "赫伯特",
   "role": "书记，凡人，56岁，管官邸账本",
   "notes": "黄铜眼镜，牛皮账册，胆小；私下担心灌注伤了洛伦神智",
   "speech": "称洛伦“大人”，自称“小人”，开口“回大人”；称加尔文“莫兰卫队长大人”"
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
  },
  {
   "name": "玛尔塔",
   "role": "锈河镇铁匠，寡妇，带两个学徒",
   "notes": "已照图打出铁铰链和长轴",
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
  },
  {
   "name": "锈河",
   "notes": "官邸下方，水赤红，漫滩暗红泥沙夹黑色铁砂，带铁锈味"
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
  },
  {
   "name": "双动活塞风箱图纸",
   "notes": "木箱、四根导轨、熟牛皮边活塞、单向阀；铁件交玛尔塔；洛伦未对人说名称"
  }
 ],
 "rules": {
  "world": [
   "1金币=20银币=2000铜币",
   "世界有魔法，法师贵族统治凡人",
   "1袋大麦=4银币",
   "帝国三环：核心环、中环、外环，越外魔素越稀",
   "凡人称无源者/平民"
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

## 5. Nguyên văn phần cuối đoạn 2 (để nối mạch và giữ giọng)

“回大人，帝国律法管得极严，平民可碰不得长过一臂的铁器啊。”
“私自结社更是杀头的大罪，至于认字念书，全属地也就三张文书许可罢了。”
说到识字两个字，老书记把脖子缩得极短，声音压得只剩一口气。
洛伦靠在粗麻织成的枕头上，迅速得出了一笔合算的账目。
法师嫌弃外环的环境，所以一万八千人口的领地上，只有一位天天头疼的二星卫队长看着。
这对他来说是个好消息。
“赫伯特，把官邸的账册翻开，念一念属地的底子。”
洛伦指了指那本牛皮封皮的旧账册。
赫伯特连忙从地上爬起来，推正鼻梁上的黄铜眼镜。
他把厚重的账册摊在膝盖上，干枯的指甲停在最上方的数字上。
“回大人，属地共有平民卫兵四十名，官邸库房里存着三百一十二枚金币。”
老书记清了清嗓子，指尖划向下一行：“今年的大麦收成，二十三个村子统共只能收上来九千五百袋左右呢。”
“秋税定额是一万两千袋，这么算下来，咱们还缺两千五百袋的窟窿啊。”
赫伯特的喉结上下动了动，额角的汗珠滚到了胡须边。
两千五百袋大麦，按照每袋四枚银币的官价，是一万枚银币。
二十枚银币换一枚金币，填补今年的缺口需要整整五百枚金币。
库房里存着三百一十二枚金币，账面上差了一百八十八枚，距离秋税日只剩下一百二十天。
督政官邸的金库底子，连还清今年窟窿的七成都不够。
“既然收成只有这么点，宗族为什么要定下一万两千袋的重税？”
洛伦掀开麻布被子，赤脚踏上了冰凉的石板地。
加尔文磕了磕烟斗里的残灰，嘴角撇出一个嘲弄的角度。
“索恩家族每年要向帝都的魔导议会上缴庞大的魔晶配额，族长手里吃紧，自然要把担子分摊到各个属地头上了嘛。”
“属地里能拿去换钱的产物，除了地里的大麦，还有什么东西？”
洛伦走到粗糙的木桌边，端起放凉的开水灌了一大口。
赫伯特弓着背翻动羊皮纸页，指尖划过零散的记录。
“回大人，只有河滩里的红砂，还有镇上一家铁匠铺子罢了。”
“铁匠铺是寡妇玛尔塔在支应着，手里带着两个年轻学徒，打些锄头镰刀还成呢。”
“那条大河淌的都是血红色的脏水，两岸平民连浇地都不敢用它，喝了肚子就要绞着疼的呀。”
赫伯特愁苦地叹了口气，脸上的皱纹堆在一起。
“秋收抢工的时节快到了，一万八千号人全得在麦田里泡着，想抽调人手去干其他营生也抽不出来啊。”
老书记揉了揉酸涩的眼眶，两只手在账册边缘搓来搓去。
“谁规定办成一件新差事，必须多添几个凡人的力气呢？”
洛伦走到敞开的窗台边，低头看着官邸下方蜿蜒穿过的赤红河水。
浑浊的赤色河流从远处平原切开一道深痕，两旁的漫滩堆满了暗红色的泥沙。
水流冲刷着石块，在河湾处留下一层厚重的暗色沉积物。
洛伦招手叫过门外值守的卫兵，吩咐对方去河滩抓一把新鲜的细砂送上来。
卫兵很快端着一只粗陶浅碟快步跑回卧房。
碟子里堆着半捧潮湿的红砂，散发着一股浓烈的生铁锈味。
洛伦端起陶碟走到蜡烛底下，伸出食指捏起一撮细砂碾磨。
沙砾粗粝沉重，在烛火下显出深褐的底色，中间夹杂着密密麻麻的细小黑粒。
前世地质选矿手册的图文在脑海里整页翻开，墨迹清晰可见。
高品位风化磁铁矿砂，伴生微量赤铁矿，含铁量甚至越过了普通贫铁矿石的底线。
所谓的血水只是铁离子氧化后的悬浮沉淀物，整条锈河就是一条天然露天的重选矿脉。
这一万八千人踩着一座露天铁矿饿了二十年，属地库房却还要为五百枚金币发愁。
“把官邸里存着的蜡烛都抱到书房去，赫伯特。”
洛伦端起桌上的油灯，抬腿朝门外走去。
赫伯特愣了一下，连忙抱着牛皮账册碎步跟上。
老书记的布鞋在走廊的石板上蹭出一阵阵急促的摩擦声。
加尔文靠在卧房门口，嘴里喷出一道辛辣的烟雾。
“少爷刚从停尸床上爬起来，半夜不歇息，倒要去书房看什么闲书呢？”
“莫兰卫队长大人，少爷这般折腾，怕是那次灌注当真伤到了神智啊。”
赫伯特压低了嗓门，脸上的法令纹显得愈发深刻。
加尔文嗤笑着摆了摆手，转身走回床边去拿自己的皮酒囊。
“总比死在停尸偏厅强，由着他折腾吧，反正一百二十天后也是宗族骑兵来收场罢了。”
书房的橡木长桌上，赫伯特一口气点起了三支粗大的牛油蜡烛。
劣质油脂燃烧的气味十分呛鼻，黑灰顺着火苗慢悠悠地爬上屋顶。
洛伦把督政官常服的领扣扯开两颗，繁琐的皮质束带勒得锁骨生疼。
这种为法师贵族设计的宽袍大袖，除了摆架子之外毫无用处。
他铺开一张干燥的硬羊皮纸，拿起鹅毛笔饱蘸黑墨。
要把河滩里的磁铁砂炼成铁水，单靠玛尔塔那座用皮囊吹风的慢火炉子可成不了事。
炉火必须烧到发白，铁砂里的杂质才能顺利熔解流出。
洛伦要画出来的第一件器械，是一座双动活塞风箱。
笔尖划过粗糙的羊皮纸，留下笔直而干脆的墨线。
方截面木制箱体，四根圆木导轨，中间是用硬杂木拼合而成的活动活塞板。
活塞四壁贴着打磨光滑的熟牛皮，浸透菜籽油以保证严密气密性。
箱体两侧各开两个进气单向阀，排气道并联通往前方的喷嘴。
传统的折叠皮囊拉开吸气、推拢出气，一半工时都浪费在空行程上。
双动活塞无论推还是拉，两侧气室都在交替进气与排气。
鼓风效率直接翻了一倍，送出的风量更是平稳连续。
箱体总装图画完，洛伦又换了一张羊皮纸，开始勾勒细部的金属构件。
两根直径两寸的熟铁传动长轴，四套固定箱体的角铁，六组连接阀门的铁铰链。
每一处孔径与插销的规格，都在图纸侧面标注了精确的公差尺寸。
烛火随着穿堂风微微晃动，桌上的草图一张接一张地叠了起来。
从木板榫卯接缝到牛皮阀门的剪裁展开图，整整铺满了半张书桌。
三支牛油蜡烛燃到了底座，铜烛台上凝固了一圈灰白色的油垢。
洛伦搁下被墨汁染黑的鹅毛笔，整条右臂酸麻得几乎抬不起来。
外面的天色泛起一层惨白的晨光。
洛伦把厚厚一叠图纸卷在一起，塞进守在门外的赫伯特怀里。
“把这个送到铁匠铺，让玛尔塔照着图样把连杆和铁铰链打出来，傍晚前我要验看。”
洛伦打了个长长的哈欠，转身走回卧房，一头扎在干草床垫上睡了过去。
这一觉直接睡到了正午。
夏末的烈日烤着官邸厚重的花岗岩外墙，房内闷热得叫人透不过气来。
门板猛地被撞开，赫伯特气喘吁吁地冲进了卧房，额头上的眼镜歪到了鼻翼旁边。
老书记两只手捧着布包，嘴皮子哆嗦得厉害。
“大人！玛尔塔照着图样打成了，铁铰链和长轴全都试过了，尺寸分毫不差啊！”
洛伦掀开亚麻粗被翻身坐起，伸手抓过床头那件缀满铜扣和皮绳的督政官长袍。
十几个绳结缠在腰侧，系起来繁琐得叫人发躁。
“带路，赫伯特，我们去铁匠铺验货。”
洛伦扯紧最后一根皮绳，大步跨过了房门。

(Đoạn 3 sẽ bắt đầu ngay sau chỗ này.)

---

## 6. Prompt đoạn tiếp theo

Viết đoạn thứ 3, khoảng 2500 chữ, bằng tiếng Trung.

【Thiết lập (để tham khảo, cái gì không dùng tới thì không cần viết ra)】
- 洛伦·索恩: 督政官 锈河属地, 19 tuổi, người xuyên việt, đang giả lú. Không có ma lực, không cảm thấy ma tố; anh chỉ biết pháp sư thấy gì qua lời họ nói. Bàn tay vàng: nhớ rõ từng chữ mọi trang sách kiếp trước từng đọc, như lật sách. Biết cách làm từ sách; tay anh không có nghề, phải có thợ.
- 玛尔塔: thợ rèn 锈河镇, 28 tuổi, góa chồng, giữ lò rèn của chồng bên bờ sông, có hai thợ phụ, con trai bảy tuổi. Gọi 洛伦 là 督政官大人 hoặc 大人.
- 加尔文·莫兰: 卫队长, pháp sư hai sao, theo 洛伦 ra ngoài với tư cách hộ vệ; tẩu đất nung, châm bằng lửa đầu ngón tay. Gọi 洛伦 là 洛伦少爷; 洛伦 gọi 莫兰卫队长. Mọi pháp sư có 魔视, nhìn thấy ma tố quanh người và vật; sắt, gỗ, đá hầu như không có gì.
- 赫伯特: 书记, 56 tuổi, kính gọng đồng, sổ da dê. Gọi 大人, tự xưng 小人, mở lời bằng 回大人.
- Thứ 洛伦 vẽ đêm qua: một chiếc 风箱 kiểu pít-tông hai chiều — ống gỗ, pít-tông bọc da, van da, kéo tới hay đẩy lui đều thổi gió. Lò của 玛尔塔 đang dùng bễ da kiểu cũ, bóp bằng tay.
- Tiền và giá: 1 金币 = 20 银币 = 2000 铜币; 1 袋 lúa mạch = 4 银币. Than củi 1 xe = 5 银币; lò 玛尔塔 đốt 2 xe một tuần, có bễ mới sẽ đốt 4 xe. Gương tay 2 金币 = 40 银币 = 8 xe than = 10 袋 lúa. Phần cống lương thiếu 2.500 袋 = 500 金币 = 250 gương tay.

【Chuyện xảy ra trong đoạn này】
洛伦 đi bộ từ 督政官邸 xuống 锈河镇, 赫伯特 đi trước dẫn đường, 加尔文 theo sau. Đây là lần đầu một 督政官 xuống lò rèn: người trong trấn đang làm việc dọc đường và quanh lò dừng tay đứng xem, có người lùi vào trong cửa. 赫伯特 đi trước vài bước báo cho lò rèn. 玛尔塔 và hai thợ phụ chào 督政官 theo phép phàm nhân trước khi nói tới linh kiện; con trai bảy tuổi của bà bị kéo ra sau lưng mẹ. 玛尔塔 bày ra những mảnh bà đã rèn theo bản vẽ.

Anh ngồi bệt xuống đất lắp chiếc 风箱 từ những mảnh 玛尔塔 rèn và thợ mộc đẽo, vừa lắp vừa chỉ cho hai thợ phụ chỗ nào khít, chỗ nào hở. Thợ phụ kéo thử; gió thổi cả lúc kéo tới lẫn lúc đẩy lui, lửa lò đổi màu sang trắng. 洛伦 chờ 加尔文 soi cái máy lạ bằng 魔视 rồi hỏi vặn, và đã nghĩ sẵn trong đầu một lời bịa. 加尔文 soi xong, bảo cái bễ "trống không", chẳng có tí ma tố nào, đồ chơi gỗ, rồi ra gốc cây ngồi hút tẩu. 洛伦 cất lời bịa đi.

玛尔塔 thì tính bằng chuyện của bà: lửa thế này đốt than gấp đôi, ai trả tiền than, và lò của chồng bà không phải chỗ cho cậu ấm chơi. 洛伦 đáp bằng phép tính trong thiết lập: thêm hai xe than mỗi tuần là 10 银币. Anh bảo đổ vào lò một mẻ cát bãi sông đã đãi trộn tro cây, nói lửa này nung cát thành thủy tinh, và một tấm gương tay làm từ thủy tinh ấy bán cho phu nhân pháp sư được 2 金币 — tám xe than, mười bao lúa. Mẻ cát đầu chảy ra thành một cục thủy tinh đục; con trai 玛尔塔 đòi một mảnh, còn 玛尔塔 cầm cục thủy tinh lên soi về phía mặt sông.

Qua tới bữa tối ở 督政官邸, 赫伯特 đã ngồi tính lời gương trên giấy, xin thêm giấy để tính tiếp; số trên giấy của ông đi tới 250 tấm. 洛伦 bảo ông: gương đắt vì hiếm; thương nhân thấy hai mươi tấm cùng một chỗ thì giá tấm thứ hai mươi không còn là 2 金币.

【Những điểm bắt buộc】
- Chuyện 加尔文 soi bễ ra "trống" kể từ mắt 洛伦: anh chỉ biết qua lời và vẻ mặt 加尔文.
- Phép tính than, gương, lúa đúng như thiết lập.
- Hôm nay mới ra thủy tinh đục; gương chưa làm được.

【Tự do sáng tạo】
Cách 洛伦 lắp và tự giễu cái tay vụng của mình, phản ứng của hai thợ phụ, lời mỉa của 加尔文, cục thủy tinh đục ra sao và 洛伦 nghĩ gì về nó, món ăn bữa tối, cách 赫伯特 tính — do bạn quyết.

【Mở đầu và chỗ dừng】
- Mở: 洛伦 vừa ra khỏi 督政官邸, áo 督政官 còn thắt lệch một dây, 赫伯特 dẫn đường xuống trấn.
- Dừng: cuối bữa tối, 洛伦 hỏi 赫伯特 có tiền rồi thì tiêu vào đâu trước; 赫伯特 còn đang nghĩ. Câu trả lời của 洛伦 thuộc đoạn sau.
