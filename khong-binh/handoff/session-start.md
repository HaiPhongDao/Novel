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
  "time": "洛伦第二次醒来，当日夜里",
  "where": "督政官邸，洛伦卧房",
  "present": "洛伦靠坐床头，手边账册；赫伯特跪在床边；加尔文站在衣柜旁抽烟斗",
  "last_beat": "加尔文指尖燃火点烟斗，洛伦问世上真有魔法，加尔文答：当然有，不然你父亲凭什么高高在上",
  "pending": "洛伦尚不知魔法如何运作"
 },
 "timeline": {
  "relative_time": "灌注后第三天；距秋税日120天",
  "chapter_log": [
   "1: 洛伦停尸间醒来吓翻杂工，前世记忆涌入昏倒；再醒装失忆，问账，见火指"
  ]
 },
 "already_told": [
  "洛伦魔力灌注后昏死三天，棺木已订",
  "锈河属地：帝国东南边缘，一万八千凡人，锈河镇+二十三村",
  "秋税日交一万二千袋大麦，剩一百二十天；去年只交八千四百袋，缺三千六百袋",
  "前任督政官随帝都使者回了帝都，此后音讯全无",
  "挂毯：初代先祖于碎石岗降天火全歼三万敌军",
  "官邸伙食：大麦硬饼、风干牛肉、芜菁汤"
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
   "notes": "头发稀疏，胆小谨慎，紧抱硬皮账册，常冒冷汗",
   "speech": "称洛伦“大人”，自称“小人”，开口“回大人”"
  },
  {
   "name": "加尔文·莫兰",
   "role": "家族卫队长，二星法师，34岁",
   "notes": "高大，石楠木烟斗，靴沾泥；对此地不耐烦；指尖燃蓝火点烟",
   "speech": "称洛伦“洛伦少爷”；洛伦称他“莫兰卫队长”"
  },
  {
   "name": "奥瑞克·索恩",
   "role": "洛伦之父，索恩家族族长，六星法师，无爵位",
   "notes": "强行灌注魔力",
   "speech": ""
  },
  {
   "name": "老杂工",
   "role": "官邸擦洗尸体的杂工",
   "notes": "洛伦坐起时吓得撞翻木架逃走",
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
   "notes": "羊皮，单式记账，含23村丁口地亩册及总督府转交调令"
  },
  {
   "name": "索恩家族挂毯",
   "notes": "黑袍法师召流星天火烧三万军，荆棘徽记"
  }
 ],
 "rules": {
  "world": [
   "1金币=20银币=2000铜币",
   "世界有魔法，法师贵族统治凡人"
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
  "加尔文称交不够粮的督政官通常被发配苦役矿坑（一般说法，前任下落无人知）",
  "洛伦盘算深耕铁犁、水力磨坊、堆肥增产"
 ],
 "conflicts": []
}

---

## 5. Nguyên văn phần cuối đoạn 1 (để nối mạch và giữ giọng)

脑海里的工业资料安稳待在意识深处，而属于这具十九岁肉身的过往，只剩下一个名字。
除去知晓自己叫做洛伦·索恩，其余的人际关系与世俗常识全是一片空白。
“我头疼得厉害，”洛伦靠在床板上，抬手指了指自己的脑袋，“很多旧事想不起来了。”
宣称失忆是最稳妥的伪装，能合理掩饰所有言行疏漏，也能顺理成章地向旁人套取情报。
靠在柜边的男人吐出一口浊气，取下烟斗在掌心敲打：“能在六星强者的魔力灌注下留住性命，脑子里烧掉点东西很公道，洛伦少爷。”
“莫兰卫队长说的是，”老头跪在地上往前挪了半步，“回大人，小人是赫伯特，一直替官邸管着账本。”
洛伦的视线在两人之间转了一圈。
一个胆小谨慎的凡人账房，一个拿钱办事的护卫队长，这处宅邸的权力结构比预料中更简单。
“我昏睡了多久？”洛伦扶着被褥坐直身子。
“整整三天，大人，”老赫伯特抹了一把脑门上的冷汗，“大家都以为您熬不过去了，连棺木都订好了。”
“先弄点吃的过来，”洛伦按了按空瘪的胃部，“有什么端什么。”
端上来的食物放在粗陶盘子里。
一块黑褐色的大麦硬饼，切口处混着粗糙的谷壳碎屑，边缘还嵌着两粒石磨剥落的细砂。
两根风干牛肉条黑亮坚硬，表面结着一层泛黄的粗盐颗粒。
旁边的木碗里盛着半碗芜菁杂烩汤，几片菜叶沉在碗底，汤面上浮着厚重的牛油冷凝结块。
洛伦掰下一块大麦饼塞进嘴里，粗粝的谷物把牙床磨得生疼。
这顿饭的成本大概只有一枚铜币，粗盐里的苦味杂质直冲舌根。
在粗放的庄园经济里，缺少酵母发酵的面团只能烤成板砖，风干腌肉也带着刺鼻的腥气。
这种食物在现代养殖场只能充当饲料，在这里却属于统辖万人的领主特供餐食。
洛伦就着温热的菜汤把面饼硬块吞进胃里，肚腹里那股强烈的饥饿感总算平复了下去。
只要搭一座带温控风门的砖窑，再引种发酵面团的麦芽酵母，食物的口感就能翻上好几倍。
不过在填饱肚子之前，得先搞清楚自己脚下的这块地盘。
洛伦推开陶盘，擦了擦嘴角：“赫伯特，把账本递给我。”
老书记官弓着腰上前，双手把发黑的羊皮账册奉到床沿。
“回大人，这是属地内二十三个村庄的丁口与地亩册，还有总督府转交的调令。”
洛伦翻开账本，单式记账法记录的条目杂乱无章，数字旁边画满了各种防伪的草签符号。
但在他的注视下，散落的数据迅速在脑海中归类重组，拼成一张清晰的资产负债表。
这里是锈河属地，帝国东南边缘的一处偏远领地。
全境共计一万八千名领民，分布在锈河镇和周边的二十三个自然村落里。
这一万八千个凡人，尽数缺乏魔力天赋，世代在这个泥泞的河谷里给远方的法师贵族种麦子。
“今年要交多少粮食？”洛伦手指划过账册末页。
“回大人，”赫伯特的身子缩得更低了，“秋税日的定量是一万二千袋大麦。”
“还有多少天开征？”
“回大人，距秋税日还有一百二十天。”
洛伦翻到了前一年的结算记录：“去年收成怎样？”
“去年……去年只收上来八千四百袋大麦，”老书记官声音发颤，额头渗出大颗汗珠，“缺了三千六百袋。”
“前任督政官去哪儿了？”洛伦抬头看着老头。
“回大人，公文下来的第二天，前任大人就随帝都派来的使者回了帝都，”赫伯特抹了一把汗巾，“往后帝都那边音讯断绝，大伙谁都不晓得前任大人的去向。”
倚着衣柜的加尔文轻嗤一声，在靴底上敲打着铜嘴烟斗。
“法师议会治下的规矩很明白，交不够粮草的督政官，通常会被剥夺俸禄发配到苦役矿坑去砸石头。”
“莫兰卫队长觉得我也该去砸石头？”洛伦靠向身后的松木靠背。
“洛伦少爷是奥瑞克族长的血脉，顶多是面子上难看一些。”加尔文吐出一口带烟草味的浊气。
洛伦合上手里的账册，眼底闪过一丝精细的盘算。
一万二千袋大麦的任务，一百二十天的倒计时，还有去年欠下的三千六百袋亏空。
在缺乏机械动力的世界里，这笔账在别人眼里是催命符，在他眼里只是一道加减算术题。
一万八千名劳动力散布在二十三个村子里，平均每个村子承担五百二十多袋的额度。
按一百二十天计算，全属地每天只要产出一百袋大麦就能交差。
现有的单牛木犁入土只有三寸，深耕图谱里的双轮重型铁犁能直接把冻土翻开一尺深。
再加上河道边的水力磨坊，配合翻转堆肥把腐殖土利用起来，产粮效率提升五成轻而易举。
只要在铁匠铺敲出十套标准的熟铁犁铧，就能在三个月内把荒芜的草甸变成产粮的熟地。
把粮食从地里刨出来，总比在前世的流水线上抢进度容易得多。
洛伦心里有了底，视线从账册移开，落在了正前方的灰石墙壁上。
那面墙上挂着一幅尺幅庞大的织锦挂毯，丝线有些褪色，边角积着一层常年未曾清扫的蛛网。
挂毯正中绣着一个立在断崖顶端的黑袍法师，法袍下摆绣着索恩家族的荆棘徽记。
法师单手指向阴云密布的长空，无数赤红色的流星从云端砸落，把整座山谷化为滔天火海。
火海中沉浮着成千上万披甲执矛的士兵，盾牌在熔融的高温中扭曲变形，旗帜化为灰烬。
“那是索恩家族初代老祖宗的功业，”老赫伯特顺着领主的视线看过去，两手紧紧贴在膝头，“当年老祖宗在碎石岗一战降下神罚，全歼了三万敌军。”
洛伦靠在床头，嘴角扯动了一下。
这种封建领主抬高身价的套路他见得太多了，古往今来的贵族总喜欢在族谱里给自己编排几个斩龙屠魔的先祖。
单凭一个人挥挥手就能召来天火烧毁三万人马，纯粹是乡野文人替统治者炮制的神话吹嘘。
要是真有这种毁天灭地的个人伟力，世界格局早就彻底颠覆，底层的平民根本不需要按部就班地靠大麦纳税。
“先祖的故事听听就算了，”洛伦笑了一声，“画得再吓人，也顶替不了一万二千袋大麦。”
加尔文从衣柜边直起身子，从皮囊里捏出一小撮切碎的干烟草，塞进烟斗的陶土内胆里。
男人并未挪步去桌边引燃蜡烛，只是随手抬起右手的食指。
啪的一声脆响，食指指尖凭空窜起一簇半寸高的幽蓝火苗，在昏暗的卧房里散发出清冷的光。
加尔文把烟斗凑到指尖上方，吧嗒吧嗒吸了两口，青白色的草药烟雾在房间里弥漫开来。
随后男人反手一抖，指尖的火苗瞬间凭空消散，手指表面甚至找寻不到一丝烧焦的黑痕。
洛伦整个人僵在了木床上。
脑海里刚刚建立完毕的水车连杆图纸、高炉鼓风机速比表，在这一刻瞬间被按下了暂停键。
那簇违背了常理的火焰在空气中燃烧的情形，直接击碎了所有关于古典封建社会的预想。
“莫兰卫队长，”洛伦盯着男人那根完好无损的食指，手指按在被沿上，“这个世界上，真有魔法？”
加尔文吐出一团规整的青色烟圈，垂下眼帘看向床上的年轻少爷。
“当然有，洛伦少爷，不然你以为你的父亲凭什么高高在上？”

(Đoạn 2 sẽ bắt đầu ngay sau chỗ này.)

---

## 6. Prompt đoạn tiếp theo

Viết đoạn thứ 2, khoảng 2500 chữ, bằng tiếng Trung.

【Thiết lập (để tham khảo, cái gì không dùng tới thì không cần viết ra)】
- 洛伦·索恩: 19 tuổi, người xuyên việt trong thân xác con thứ ba của 奥瑞克·索恩 (族长 索恩家族, pháp sư sáu sao, không mang tước). Đang giả lú, đổ cho lần 灌注. Không có ma lực, không dùng được phép, không cảm thấy ma tố. Bàn tay vàng: mọi trang sách kiếp trước từng đọc hiện ra rõ từng chữ khi anh nghĩ tới, như lật sách trong thư viện. Biết về đá và quặng từ những gì sách viết, không phải từ tay nghề.
- 赫伯特: 书记 phàm nhân, 56 tuổi, kính gọng đồng, ôm sổ da dê; một trong ba người ở 锈河 có giấy phép biết chữ. Gọi 洛伦 là 大人, tự xưng 小人, mở lời bằng 回大人.
- 加尔文·莫兰: 卫队长 của gia tộc, pháp sư hai sao, 34 tuổi, giáp da, tẩu đất nung. Gọi 洛伦 là 洛伦少爷; 洛伦 gọi 莫兰卫队长.
- 玛尔塔: thợ rèn ở 锈河镇, 28 tuổi, góa chồng, giữ lò rèn của chồng.
- Thế giới: 瑟兰魔导帝国 do các gia tộc pháp sư cai trị, trên cùng là 魔导议会. Ba vành 核心环, 中环, 外环; càng ra ngoài ma tố càng loãng; pháp sư ở 外环 hồi ma chậm gấp ba và hay đau đầu. Pháp sư xếp bằng 星, một đến chín sao. Mọi pháp sư có 魔视: nhìn thấy ma tố quanh người và vật. Phàm nhân gọi là 无源者, bị cấm giữ vũ khí dài hơn cánh tay, cấm học chữ, cấm lập hội. Người đo ra 0 ở 测魔礼 bị gọi là 空瓶.
- Sổ của 锈河属地: 40 lính phàm nhân; kho bạc 312 金币; thu hoạch năm nay dự tính khoảng 9.500 袋; cống lương 12.000 袋; thiếu 2.500 袋. Mua bù: 1 袋 = 4 银币, 20 银币 = 1 金币, tức 2.500 袋 = 500 金币. Còn 120 ngày tới 秋税日.
- Sông 锈河: nước đỏ, dân gọi là "nước máu" và không dùng; đáy và bãi bồi là cát đỏ, nặng tay, lẫn hạt đen.

【Chuyện xảy ra trong đoạn này】
Mở ngay sau câu đáp của 加尔文 về phép thuật, cùng căn phòng ngủ, 洛伦 còn ngồi trên giường. Anh cười gượng cho qua cơn sững sờ: những gì kiếp trước coi là thường thức, sang đây còn đáng bao nhiêu thì anh chưa chắc. Rồi anh hỏi tiếp. Anh hỏi mình đã làm gì mà bị đưa tới chốn này; 加尔文 kể: 测魔礼 đo ra 0, giới pháp sư gọi anh là 空瓶, 族长 cần một chỗ để đặt cái tên. Anh hỏi ở đây có pháp sư nào khác không; 加尔文 kể ma tố ở 外环 loãng ra sao, đầu anh ta đau thế nào mỗi sáng, và pháp sư nhìn người bằng 魔视. 赫伯特 kể phần của phàm nhân: ba điều luật cấm; nói tới chữ thì ông nói nhỏ đi, vì ông là một trong ba người có giấy phép. Nghe xong, 洛伦 tự rút ra cho mình một tin tốt.

Anh hỏi tới gia sản; 赫伯特 mở sổ da dê đọc từng mục, kèm phép tính phần thiếu. 洛伦 hỏi vì sao cống cao vậy; 加尔文 đáp: gia tộc nộp lên 魔导议会, phần ấy đẩy xuống thuộc địa. Anh hỏi 锈河 có gì bán được. 赫伯特 kể: lúa, cát sông, một lò rèn của bà góa 玛尔塔, con sông "nước máu" chẳng ai dùng. Muốn làm thêm thì không có người, đang mùa gặt; 赫伯特 nói nỗi lo ấy ra. 洛伦 đáp: ai bảo làm thêm thì phải thêm người. Anh ra cửa sổ nhìn con sông đỏ chảy qua dưới phủ, rồi sai một người lính mang lên một nắm cát bãi sông. Dưới ánh đèn anh xoa nắm cát giữa hai ngón tay, nhặt những hạt đen, đối chiếu với sách trong đầu, và hiểu con sông này là gì.

Anh ôm cây đèn sang phòng đọc, đòi thêm nến. 赫伯特 và 加尔文 ở lại trong phòng ngủ một lúc; 赫伯特 lo cho cậu chủ mới, 加尔文 bảo 灌注 làm cậu ta lú rồi. Qua đêm đó 洛伦 vẽ tới khi cháy hết nến; sáng ra anh trao xấp bản vẽ cho 赫伯特 mang ra lò rèn của 玛尔塔, rồi ngủ vùi.

【Những điểm bắt buộc】
- Các con số trong sổ đúng như thiết lập: 40 lính, 312 金币, khoảng 9.500 袋, thiếu 2.500 袋 = 500 金币.
- 洛伦 không nói cho ai biết anh nhận ra gì từ nắm cát; người đọc biết qua ý nghĩ của anh.
- Chuyện cậu chủ "lú" chỉ nằm trong lời của 赫伯特 và 加尔文 khi 洛伦 đã sang phòng đọc.

【Tự do sáng tạo】
Tin tốt 洛伦 tự rút ra, cách 赫伯特 đọc sổ, lời mỉa của 加尔文, thứ 洛伦 vẽ (anh chưa nói tên nó với ai), những gì anh 吐槽 về ngọn nến, giấy da dê và bộ áo 督政官 — do bạn quyết.

【Mở đầu và chỗ dừng】
- Mở: ngay sau câu đáp của 加尔文, 洛伦 còn ngồi trên giường.
- Dừng: trưa hôm sau, 赫伯特 vào báo 玛尔塔 đã rèn xong linh kiện; 洛伦 bật dậy, vừa xỏ bộ áo 督政官 nhiều dây vừa bảo dẫn đường. Cảnh ở lò rèn thuộc đoạn sau.
