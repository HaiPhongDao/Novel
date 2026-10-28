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
  "time": "第二天正午",
  "where": "督政官邸卧房门口",
  "present": "洛伦刚睡醒，边扣督政官制服的皮带铜扣边往外走；赫伯特官帽歪斜在门口",
  "last_beat": "赫伯特报玛尔塔把铁件全打出来了，洛伦一跃而起，边系制服边说：带路，去铁匠铺",
  "pending": "铁匠铺组装风箱"
 },
 "timeline": {
  "relative_time": "醒来第二天正午；距秋税日约119天；约十天后开镰抢收",
  "chapter_log": [
   "1: 洛伦停尸间醒来吓翻杂工，前世记忆涌入昏倒；再醒装失忆，问账，见火指",
   "2: 问清空瓶、魔视、凡人禁令、底账；捏河砂识出砂铁矿；通宵画双动活塞风箱"
  ]
 },
 "already_told": [
  "洛伦魔力灌注后昏死三天，棺木已订",
  "锈河属地：帝国东南边缘，一万八千凡人，锈河镇+二十三村",
  "秋税日交一万二千袋大麦，剩一百二十天；去年只交八千四百袋，缺三千六百袋",
  "前任督政官随帝都使者回了帝都，此后音讯全无",
  "挂毯：初代先祖于断矛山谷降天火全歼三万敌军",
  "官邸伙食：大麦硬饼、风干牛肉、芜菁汤",
  "测魔礼测出零，帝都法师称洛伦空瓶，族长把他发到偏僻处",
  "外环魔素稀薄，冥想恢复慢三倍，加尔文每早头疼",
  "法师有魔视，看见万物魔素光芒",
  "凡人（无源者）禁持长于一臂铁刃、禁结社、禁私习文字；属地仅三张总督府识字文牒",
  "索恩家族向魔导议会上缴供奉，族长对各属地摊派提了两成",
  "锈河水红，称血水，牲口喝了拉稀；河滩红砂"
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
   "item": "卫兵",
   "value": "40人（无源者壮丁）",
   "as_of": "ch2"
  },
  {
   "item": "库房",
   "value": "312金币、70银币、铜币800余",
   "as_of": "ch2"
  },
  {
   "item": "今年预计收成",
   "value": "约9500袋（缺2500袋=500金币；库金全掏仍差188金币）",
   "as_of": "ch2"
  }
 ],
 "deadlines": [
  {
   "what": "秋税日交12000袋大麦",
   "when": "120天后"
  },
  {
   "what": "开镰抢收，各村无闲人",
   "when": "约十天后"
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
   "锈河红砂中黑粒为砂铁矿（磁铁矿、赤铁矿），淘洗即可入炉（未告诉任何人）",
   "属地只有加尔文一名法师，且他每早头疼——洛伦视为好消息"
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
   "knows": "洛伦盯着河砂发愣、通宵画图",
   "not_know": "砂铁矿判断、图纸是什么"
  }
 ],
 "characters": [
  {
   "name": "赫伯特",
   "role": "书记，凡人，56岁，管官邸账本",
   "notes": "黄铜眼镜，羊皮账册，胆小；私下担心洛伦脑子烧坏",
   "speech": "称洛伦“大人”，自称“小人”，开口“回大人”；称加尔文“莫兰卫队长/卫队长大人”"
  },
  {
   "name": "加尔文·莫兰",
   "role": "家族卫队长，二星法师，34岁",
   "notes": "皮甲，铜嘴烟斗，指尖燃火点烟；认为洛伦被灌注烧坏了脑子",
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
  },
  {
   "name": "玛尔塔",
   "role": "锈河镇铁匠，寡妇，守亡夫的炉子",
   "notes": "已照图打出铁连杆和导轨",
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
   "notes": "官邸南面，水赭红，滩涂红砂含黑色砂铁"
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
  },
  {
   "name": "双动活塞风箱图纸",
   "notes": "七张零件图：木壳、皮边活塞、四个皮舌阀；推拉都出风；洛伦未说名称；铁件交玛尔塔，木件交官邸木匠"
  }
 ],
 "rules": {
  "world": [
   "1金币=20银币=2000铜币",
   "世界有魔法，法师贵族统治凡人",
   "帝国三环：核心环、中环、外环，越外魔素越稀",
   "法师按星分级；凡人称无源者"
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
  "洛伦盘算深耕铁犁、水力磨坊、堆肥增产",
  "测魔礼时间：加尔文说三年前（待定）"
 ],
 "conflicts": []
}

---

## 5. Nguyên văn phần cuối đoạn 2 (để nối mạch và giữ giọng)

整整一万八千人口的属地只有一名二星法师驻守，而且这位卫队长每天早晨还犯着严重的偏头痛。
这里山高皇帝远，根本没有多余的眼睛盯着他的举动。
“赫伯特，把底账念一念。”洛伦拍了拍床边的木板。
老书记官连忙翻开那本沉重的羊皮册子，干瘪的指尖在发黄的页码上逐行划过。
“回大人，官邸现有驻防卫兵四十人，全是从二十三村抽调的无源者壮丁。”
“库房现存金币三百一十二枚，银币七十枚，铜子八百有余。”
“各村的大麦收成大致在九千五百袋上下。”
洛伦靠在床架上，指尖在膝盖上无声地敲打。
定额是一万二千袋，预期收成九千五百袋，账面上的缺口足足有两千五百袋大麦。
按市价折算，一袋大麦卖四个银币，二十个银币兑换一枚金币。
买齐两千五百袋的亏空，需要整整五百枚金币。
而官邸的金库里总共只有三百一十二枚金币，全部掏空也还差着一百八十八枚金币的窟窿。
“秋税的定额怎么定得这样高？”洛伦问了一句。
“索恩家族每年要向魔导议会上缴固定的供奉份额，”加尔文吐出一圈烟雾，“族长把各属地的摊派提了两成，底下交不上来，苦差事就得落在督政官头上。”
大人物在上头挥霍，账单最终还是由最底层的泥腿子买单。
在前世的报表里，这种转嫁成本的手段屡见不鲜，结局往往是底层供应商的资金链彻底断裂。
“属地除了大麦，还有什么能换钱的东西？”
赫伯特苦着脸叹气，手指在账册边缘搓出细微的声响。
“回大人，这地方除了麦子就是沿河的红砂，集镇上有个铁匠铺子，是玛尔塔那个寡妇在守着她男人的破炉子。”
“至于外头那条锈河，流出来的全是血水，牲口喝了都拉稀，根本派不上用场。”
“再过十天全境就要开镰抢收，各村抽不出闲散壮丁，想多折腾点出产也缺人手。”
“谁说多干活就得添人？”洛伦掀开亚麻被褥，翻身下了床。
粗劣的皮拖鞋套在脚上，冰凉的石板触感透过脚底传上来。
他走到卧房那扇窄小的拱形窗前，推开沉重的木质窗板。
夜色中的锈河在领地南面蜿蜒流淌，浑浊的河水泛着暗沉的赭红。
两岸连绵的滩涂在月光下泛着沉重的暗色，一直延伸到下游的荒原深处。
“莫兰卫队长，”洛伦没有回头，“叫门外的卫兵去河滩抓一把干砂子上来。”
加尔文挑了挑眉毛，虽然觉得这位少爷犯了病，还是朝门外的走廊吹了一声口哨。
不多时，一名身穿皮背心的年轻卫兵端着一块碎瓦片快步走进房间，瓦片上堆着半捧红褐色的河砂。
洛伦端过瓦片放在桌案的油灯旁边。
他伸出食指与拇指，捏起一撮河砂在指肚之间缓缓揉搓。
砂粒的质地异样沉重，指尖能感受到坚硬的粗糙棱角，细密的粉末染红了指纹的沟壑。
他凑近微弱的火光，从暗红色的石英碎屑里挑出了几颗乌黑发亮的不规则硬粒。
前世在矿冶资料室看过的地质图谱在脑海中逐页翻开，墨迹与标注清晰可见。
上游断裂带风化剥落的铁矿石经过水流千万年的冲刷，细碎的磁铁矿与赤铁矿碎粒在流速变缓的滩涂上常年沉积。
这条被凡人视为不祥的血水之河，底下沉睡的是储量惊人的高品位河道砂铁矿。
那些黑色的重砂颗粒甚至不需要经过复杂的破碎工序，只要淘洗干净就能直接送入熔炉。
缺粮需要铁铧深耕，赚钱需要铁器贸易，而原材料就在城门外大片大片地晒着太阳。
“把灯给我，再抱两捆牛油蜡烛去隔壁的书房。”洛伦端起那盏油灯，瓦片留在了桌角。
赫伯特赶紧躬身应命，抓起账册一路小跑去外间张罗蜡烛。
加尔文依旧斜倚在衣柜边，铜烟斗在掌心慢悠悠地转着圈。
房门被洛伦带上的那一刻，老书记官抱着粗蜡烛折返回来，额头上挂满虚汗。
“卫队长大人，”赫伯特压低了嗓门，“大人翻看了半天账本，又对着一把泥砂发愣，脑子怕是真给烧坏了。”
“六星法师的灌注威能，连一头双头岩蜥都能直接撑爆。”加尔文吐出一口冷气，收起烟斗。
“他能站着走路已经算奥瑞克老爷手下留情，随他去折腾，横竖一百二十天后挨罚的不是咱们。”
书房里的空气混杂着陈年羊皮纸的酸腐气味。
洛伦将油灯搁在宽大的栎木长桌正中，点燃了三根粗糙的牛油蜡烛。
蜡烛燃烧时冒出刺鼻的黑烟，油脂在劣质棉线的顶端哔啵作响。
这副督政官的身子骨还很虚弱，后脑勺隐隐作痛，但手头的账目容不得拖延。
要熔化高品位的砂铁，现有的敞开式土炉温度根本达不到要求。
传统皮囊单向风箱每次拉开都有漫长的进气间歇，炉温在间隙里骤降，敲出来的只能是满是杂质的脆铁渣。
他从桌底翻出几张泛黄的硬质羊皮纸，拿起裁割整齐的炭条。
脑海中泛黄的技术档案迅速展开，那是冶铁名著与近代机械制图的合成装订版。
炭条在粗涩的皮纸表面划过，沙沙的摩擦声在寂静的深夜格外清晰。
第一张图纸是长方形的密闭木质风箱壳体，标注着严密无缝的榫卯搭接结构。
第二张图纸落在了内部的核心构件上：矩形木质活塞板，周边留出了压嵌熟羊皮密封气流的凹槽，连杆从壳体正中的导向孔穿出。
第三张图纸画满了风箱内壁的阀门分布，四个薄皮革贴合的单向舌阀分别悬挂在两端的进气与排气风道口。
活塞向前推压，前端气门关闭排气，后端气门开启吸气；活塞向后拉拽，两组气阀反向动作。
每一次推拉都在产生恒定连续的高压气流，炉温将在烈风的压榨下直奔铸铁的熔点。
天色在草图中逐渐转白，窗外传来了早起役工挑水的木桶磕碰声。
三根粗壮的牛油蜡烛彻底燃成了薄薄的蜡油硬壳，长桌上散落着七张工整的零件分解图。
洛伦揉了揉酸涩的眼眶，将炭条随手扔进笔筒。
门外传来了急促的脚步声，老赫伯特顶着两个乌青的眼圈，端着铜制洗脸盆小心翼翼地推门而入。
“赫伯特，把这些图纸收好。”洛伦指着桌面上吹干炭粉的羊皮纸。
“大人，这是……”老书记官瞪圆了眼睛看着密密麻麻的墨线与标注。
“拿去镇上的铁匠铺，让那个叫玛尔塔的寡妇照着最后两张图上的尺寸把铁连杆和导轨打出来，木工部件让官邸的木匠照着做。”
洛伦打了个哈欠，径直朝着卧房走去。
“天塌下来也别吵我，我得补个觉。”
老赫伯特双手哆嗦，小心翼翼地把图纸揣进粗麻布袋，匆匆奔出了官邸大门。
正午刺目的阳光透过窄窗照在床铺上。
洛伦在沉重的闷热中睁开眼，肚腹里传来一阵饥肠辘辘的轰鸣。
门外突然传来了重重的拍门声，伴随着赫伯特上气不接下气的呼喊。
“大人！大人醒醒！”老书记官直接推开了半掩的木门，官帽歪在了一边，“玛尔塔把铁件全打出来了！”
洛伦从床上一跃而起。
他抓起搭在椅背上的督政官制服，这件衣服缀着繁复的皮质系带与黄铜搭扣，繁琐的贵族剪裁让他低声骂了一句。
他一边手忙脚乱地扣紧胸前的排扣，一边大步跨过门槛。
“带路，去铁匠铺。”

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
洛伦 tới lò rèn của 玛尔塔 bên bờ sông, 加尔文 theo sau, con trai 玛尔塔 chạy quanh đống linh kiện. Anh ngồi bệt xuống đất lắp chiếc 风箱 từ những mảnh 玛尔塔 rèn và thợ mộc đẽo, vừa lắp vừa chỉ cho hai thợ phụ chỗ nào khít, chỗ nào hở. Thợ phụ kéo thử; gió thổi cả lúc kéo tới lẫn lúc đẩy lui, lửa lò đổi màu sang trắng. 洛伦 chờ 加尔文 soi cái máy lạ bằng 魔视 rồi hỏi vặn, và đã nghĩ sẵn trong đầu một lời bịa. 加尔文 soi xong, bảo cái bễ "trống không", chẳng có tí ma tố nào, đồ chơi gỗ, rồi ra gốc cây ngồi hút tẩu. 洛伦 cất lời bịa đi.

玛尔塔 thì tính bằng chuyện của bà: lửa thế này đốt than gấp đôi, ai trả tiền than, và lò của chồng bà không phải chỗ cho cậu ấm chơi. 洛伦 đáp bằng phép tính trong thiết lập: thêm hai xe than mỗi tuần là 10 银币. Anh bảo đổ vào lò một mẻ cát bãi sông đã đãi trộn tro cây, nói lửa này nung cát thành thủy tinh, và một tấm gương tay làm từ thủy tinh ấy bán cho phu nhân pháp sư được 2 金币 — tám xe than, mười bao lúa. Mẻ cát đầu chảy ra thành một cục thủy tinh đục; con trai 玛尔塔 đòi một mảnh, còn 玛尔塔 cầm cục thủy tinh lên soi về phía mặt sông.

Qua tới bữa tối ở 督政官邸, 赫伯特 đã ngồi tính lời gương trên giấy, xin thêm giấy để tính tiếp; số trên giấy của ông đi tới 250 tấm. 洛伦 bảo ông: gương đắt vì hiếm; thương nhân thấy hai mươi tấm cùng một chỗ thì giá tấm thứ hai mươi không còn là 2 金币.

【Những điểm bắt buộc】
- Chuyện 加尔文 soi bễ ra "trống" kể từ mắt 洛伦: anh chỉ biết qua lời và vẻ mặt 加尔文.
- Phép tính than, gương, lúa đúng như thiết lập.
- Hôm nay mới ra thủy tinh đục; gương chưa làm được.

【Tự do sáng tạo】
Cách 洛伦 lắp và tự giễu cái tay vụng của mình, phản ứng của hai thợ phụ, lời mỉa của 加尔文, cục thủy tinh đục ra sao và 洛伦 nghĩ gì về nó, món ăn bữa tối, cách 赫伯特 tính — do bạn quyết.

【Mở đầu và chỗ dừng】
- Mở: 洛伦 vừa tới lò rèn, áo 督政官 còn thắt lệch một dây, 赫伯特 dẫn đường.
- Dừng: cuối bữa tối, 洛伦 hỏi 赫伯特 có tiền rồi thì tiêu vào đâu trước; 赫伯特 còn đang nghĩ. Câu trả lời của 洛伦 thuộc đoạn sau.
