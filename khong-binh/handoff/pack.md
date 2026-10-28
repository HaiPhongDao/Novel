# Tài liệu bàn giao — tiếp tục viết truyện

Bạn là Writer của truyện này. Các đoạn trước bạn đã viết ở một session cũ; tài liệu dưới đây là toàn bộ những gì cần nhớ để viết tiếp đúng mạch và đúng giọng.

**Lần này chưa viết chính văn.** Đọc kỹ toàn bộ, rồi trả lời ngắn bằng tiếng Việt đúng 3 dòng:
1. 洛伦 đang ở đâu, vừa thấy gì.
2. 洛伦 đang giả vờ điều gì, đổ cho cái gì.
3. Các con số đang chạy (cống lương, ngày còn lại, năm ngoái nộp).

Sau đó chờ prompt của đoạn tiếp theo.


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
