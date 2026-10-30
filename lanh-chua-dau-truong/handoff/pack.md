# Tài liệu bàn giao — tiếp tục viết truyện

Bạn là Writer của truyện này. Các đoạn trước bạn đã viết ở một session cũ; tài liệu dưới đây là toàn bộ những gì cần nhớ để viết tiếp đúng mạch và đúng giọng.

**Lần này chưa viết chính văn.** Đọc kỹ toàn bộ, rồi trả lời ngắn bằng tiếng Việt đúng 4 dòng:
﻿# Quiz — ba câu kiểm canon (Writer trả lời trước khi viết)

1. **Ai đang gặp nguy, và ai đang cầm quyền?** — Grik (goblin, vật thế chấp) sắp bị chở đi bán; quyền trên giấy thuộc Orin (nam tước), nhưng quyền thật đang nằm trong tay Voss (khế nợ + 12 kỵ binh) và 执事 Aldric (ấn 判斗).
2. **Bí mật nào chưa ai biết?** — Voss đã mua chuộc con trai người đánh xe để dàn xếp trận đầu; 执事 có quỹ người nghèo riêng và một sổ tên người; Orin thấy tỷ lệ thắng thật.
3. **Con số nào quyết định đoạn này?** — 120 vàng nợ, hạn 40 ngày; quỹ 4 vàng 12 银; 900 chỗ ngồi bán được; 3 vàng 赏金 + 2 vàng lệ phí ấn; 1 vàng = 20 银 = 400 铜.

Sau đó chờ prompt của đoạn tiếp theo.


---

﻿# Canon card — thẻ thiết lập (đoạn 0)

## Truyện
- Tên: **Lãnh Chúa Đấu Trường** (领主：从破产斗兽场开始).
- Thể loại: Tây huyễn lãnh chúa + kinh doanh đấu trường + bảng sổ cái.
- Trục: kinh tế máu và tiền; MC thắng bằng thiết kế trận, giá vé, tỷ lệ cược.

## Người
- **Orin** — nam tước 锈环领, 24 tuổi, người xuyên việt (nghề cũ: sản xuất sự kiện/giải đấu). Nhẫn ấn cha quấn dây da.
- **Bram** — 51 tuổi, cựu vô địch, một mắt, cụt hai ngón trái, giữ danh sách đấu sĩ.
- **Grik** — goblin 17 tuổi, 1,2 mét, sẹo qua tai trái, vật thế chấp được mua đứt 1 vàng.
- **Sabine** — 41 tuổi, quản kho lương, chùm chìa khoá ở thắt lưng.
- **Voss** — 35 tuổi, trung sĩ quận, cầm khế nợ, 12 kỵ binh.
- **Aldric** — 46 tuổi, 执事 圣堂, giữ ấn 判斗 và quỹ người nghèo.

## Nơi
- 锈环镇 (780 dân) + hai xóm (320 dân) · 锈环斗兽场 (3.000 chỗ, dùng được 900) · 灰角城 (quận, 40 里).

## Số khởi điểm (ngày 0)
- Khế nợ **120 vàng** (100 gốc + 20 lãi), hạn 秋分, **còn 40 ngày**.
- Quỹ **4 vàng 12 银**. Kho **12.000 斤** mạch, định mức 1 斤/người/ngày → 11 ngày.
- Đội tuần 40, 26 thương, 9 nỏ. Đấu sĩ trong danh sách: 6.
- Giá vé: 站席 2 铜 · 座席 8 铜 · 包厢 1 银. Lệ phí ấn 2 vàng. 赏金 3 vàng/phiên nhỏ.

## Luật phải nhớ
- 判斗 hợp pháp khi có ấn 执事, trong ngày hội, mặc định đến nhận thua/chảy máu.
- 抽水 1/10 quỹ cược. 穷人捐 1/10 赏金.
- 1 vàng = 20 银 = 400 铜. 1 斤 mạch = 1 铜.
- Không súng, không phép cho người thường, không ai biết tương lai.

## Giọng
- Người kể đứng về phía Orin, châm một câu mỗi đoạn; câu 22–30 chữ; số phải có đơn vị.

## Đoạn 001 — bổ sung canon
- Grik được mua đứt với giá 1 和ng, không còn là vật thế chấp; Orin tuyên bố nó là "đấu sĩ ăn lúa của đấu trường".
- Gươm nghi lễ của cha Orin: bán cho Voss 1 和ng 10 银 (Voss mặc cả từ 1 和ng 4 银).
- Bảng 【斗兽账房】 hiện lần đầu ngay sau khi Grik được thả; in 5 dòng; chỉ Orin thấy.
- Từ mới của Writer (đã vào glossary): 判斗节, 黑鹰印, 火漆印, 郡律.
- Bram cụt hai ngón tay **trái**; mắt trái mù.

---

## 2. State (JSON — sự thật và con số đã xảy ra, lấy đây làm chuẩn)

Đoạn tiếp theo viết từ ngay sau `scene_bridge.last_beat`. Những gì trong `already_told` người đọc đã biết: chỉ nhắc một chữ khi cần, không giải thích lại. Số liệu lấy theo `ledger`; ai biết bí mật nào theo `knowledge_map`.

{
 "meta": {
  "last_chapter": 1,
  "story": "西幻领主 / 竞技经营：锈环镇，埃斯特兰王国南境；人名一律写罗马字（Orin、Bram、Grik、Sabine、Voss、Aldric），地名、头衔、术语写汉字"
 },
 "scene_bridge": {
  "time": "秋分前第40天，清晨至上午",
  "where": "锈环斗兽场北门、砂地、门洞前的黑板",
  "present": "Orin 站在黑板前；Grik 提着短铁矛站在砂地上；Bram 拄卷刃阔剑堵在门道，手里是六人名单；Sabine 捧着红木匣站在男爵身侧；Voss 已骑马返回灰角城",
  "last_beat": "北门打开，Grik 提矛迈过门槛，Bram 堵在门道中央，名单在寒风里翻卷",
  "pending": "三天后第一场判斗；执事 Aldric 的印还没送到；六名打手还没见到赏金；Voss 回灰角城交印费"
 },
 "timeline": {
  "relative_time": "秋分前 40 天；距第一场判斗 3 天",
  "chapter_log": [
   {
    "chapter": 1,
    "summary": "清晨 Voss 在斗兽场北门宣读 120 金币债契，抵押物第七项是地精 Grik。Orin 从铁箱取特权卷轴，确认判斗节条款与秋分期限；以 1 金币 10 银把老男爵仪仗剑卖给 Voss，付 1 金币买断 Grik、2 金币执事印费，金库剩 3 金币 2 银。Grik 获得释放，被定为斗兽场打手；斗兽账房首次显现，登记第一场 Grik 对车夫之子；Orin 在黑板写下对局，北门打开，Grik 走上砂地，Bram 持六人名单堵在门道。"
   }
  ]
 },
 "already_told": [
  "金库 4 金币 12 银，卖剑得 1 金币 10 银，付赎金 1 金币、印费 2 金币，余 3 金币 2 银（ch1 已述）",
  "Grik 已买断，不再是抵押物，被定为斗兽场打手；铁链已解开（ch1 已述）",
  "斗兽账房首次显现：900/3000 席、票价 2 铜/8 铜/1 银、Grik 对车夫之子 58%/42%、抽水一成（ch1 已述，仅 Orin 可见）",
  "判斗节每年四场，秋分前不办则失特权；执事印章尚未送到（ch1 已述）"
 ],
 "ledger": [
  {
   "item": "债契",
   "value": "120 金币（100 本金 + 20 利息），秋分到期，债权人：灰角郡伯爵 Gremont",
   "as_of": 1
  },
  {
   "item": "金库",
   "value": "3 金币 2 银（其中 3 金币为第一场赏金，2 银为零钱）",
   "as_of": 1
  },
  {
   "item": "粮仓",
   "value": "黑麦 12,000 斤，每人每日 1 斤，1,100 人可撑 11 天",
   "as_of": 1
  },
  {
   "item": "斗兽场",
   "value": "3,000 席，可售 900 席；北门已开；东西石梯坍塌；北半场积水待排",
   "as_of": 1
  },
  {
   "item": "斗兽账房",
   "value": "已激活；第一场已登记未开赛；账上 3 金币 2 银；仅 Orin 可见",
   "as_of": 1
  }
 ],
 "named_entities": [
  {
   "name": "车夫之子",
   "category": "person",
   "status": "斗兽场打手，第一场对手，已被 Voss 收买（Orin 尚不知）"
  },
  {
   "name": "判斗节",
   "category": "law",
   "status": "每年四场，执事印章验明，门票归领地，投注池抽一成"
  },
  {
   "name": "黑鹰印",
   "category": "gear",
   "status": "灰角郡伯爵的债契印，盖在羊皮债契上"
  }
 ]
}

---

# Voice anchor — câu đã duyệt làm mẫu giọng

Chưa có đoạn nào được duyệt. Sau khi chốt đoạn 001, chép vào đây 8–12 câu ngắn (nguyên văn tiếng Trung) đại diện cho:
- một câu mở đoạn bằng vật/số, không mở bằng tên;
- một lượt thoại có thẻ bằng hành động;
- một câu người kể châm;
- một dòng 【】 của 斗兽账房.

**Mở bằng vật, không bằng tên; số đi trước cảm xúc**
> 锈环斗兽场北门外的砂地上，铺着一层白生生的冷盐霜。

**Một lượt thoại có thẻ bằng hành động, không nhãn ngữ điệu**
> Voss 把羊皮纸卷起来，皮靴在石阶边缘重重磕掉沾着的干泥块。

**Câu người kể châm, rơi vào Orin**
> Orin 抬起眼皮，问的是买卖牲口下水的行市口吻。

**Câu chốt của đoạn**
> “进了这个门，你就不是等死的抵押品，是吃斗兽场麦子的打手。”

---

## 5. Nguyên văn phần cuối đoạn 1 (để nối mạch và giữ giọng)

　　Orin 俯视着它。
　　“进了这个门，你就不是等死的抵押品，是吃斗兽场麦子的打手。”
　　“打赢了有肉吃，打输了横着抬出来埋进荒原，听懂没有？”
　　Grik 抹掉眼角的脏黄泥，眼眶通红，咬着牙死命点头。
　　就在铁锁脱落的一瞬间，Orin 的视线右上方微微一闪。
　　空气中浮现出一张淡金色账页，墨黑字迹排布得整整齐齐。
【场次：第1场 · 三日后午时】
【看台：可用 900 / 3,000 席 · 票价 站席2铜 座席8铜 包厢1银】
【对局：Grik 对 车夫之子 · 真实胜率 58% / 42%】
【投注池：0 金币 · 抽水一成】
【账上：3金币 2银】
　　账面上清清楚楚，扣掉一金币赎身、两金币印费，手里还余下三枚金币两枚银币。
　　三枚金币压在擂台正下方的铁箱子里充作赏金，多出来的两枚银币能去集市换两口袋粗盐。
　　斗兽场原本能容纳三千人，但东西两侧的石梯早年坍塌，如今只剩北面九百个还能落脚的木席；站席两铜、座席八铜，坐满一半，收上来的现钱就能把领地的窟窿堵上一大半。
　　更要紧的是那一成抽水。
　　Orin 转身走向北门门洞旁的大黑木板。
　　木板上落着厚厚一层白鸽粪和沙灰，他扯过斗篷粗糙的一角用力抹开，拾起旁边的一截白石灰石。
　　石灰石在干燥的硬木板上划出粗粝的摩擦声。
　　第一行对局的名字，被清晰地描在了木板的正上方。
　　Grik 对 车夫之子。
　　Voss 摸着腰间的新佩剑，斜着眼瞅了一眼黑板，嘴里不屑地哼笑一声，翻身上鞍，踏着碎石扬长而去。
　　“开门。”
　　Orin 随手扔掉手里的半截石灰，拍掉掌心里沾着的粉末。
　　两名老仆合力推转沉重的绞盘，粗麻绳绷得笔直，锈环斗兽场闭锁了三年的北门发出一声沉重钝响。
　　两扇裹着厚铁皮的木门缓缓向内侧退开，门轴上的黑铁锈渣大片大片往下掉落。
　　门洞后面，是一片被寒霜封冻的宽阔沙地，暗褐色的干涸血迹在沙坑深处若隐若现。
　　Grik 捡起地上那柄磨钝了尖角的短铁矛，光着生满老茧的宽脚掌，一瘸一拐越过门槛迈向粗砂。
　　冰冷的白霜沾在它的绿脚趾上，它紧紧握着长矛，肩胛骨在晨风中微微耸动。
　　Bram 拄着卷刃阔剑，高大的身躯堵在半开的门道中央，断了二指的右手稳稳抓着那份名单。
　　六个沾着干墨汁的名字写在羊皮纸的最上方，在早晨刮起的荒原寒风中翻卷作响。

(Đoạn 2 sẽ bắt đầu ngay sau chỗ này.)
