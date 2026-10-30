# Tài liệu bàn giao — tiếp tục viết truyện

Bạn là Writer của truyện này. Các đoạn trước bạn đã viết ở một session cũ; tài liệu dưới đây là toàn bộ những gì cần nhớ để viết tiếp đúng mạch và đúng giọng.

Đọc kỹ toàn bộ, rồi viết đoạn tiếp theo theo prompt ở phần cuối.


---

# Canon Card — Lãnh Chúa Tiền Đồn

- **Thế giới:** Tây huyễn biên cảnh vương quốc Frank (法兰克王国). Tiền đồn 灰石哨所 ở cửa ngõ 狼牙峡谷.
- **Nhân vật:** Renard (chỉ huy, xuyên việt), Vane (lão phó quan), Barst (thợ rèn), Karl (đội trưởng dân binh).
- **Hệ thống:** Bảng 【领地兵工】 đo đếm công sự và rèn đúc, cấp kinh nghiệm thăng cấp binh chủng. Không nói chuyện.
- **Hạn chót:** 14 ngày tới gió bão mùa đông và bầy 霜狼 tràn xuống. Lương 18 ngày, tường nứt 3 chỗ.
- **Quy tắc tên:** Tên người Latin trong văn Trung (`Renard`, `Vane`, `Barst`, `Karl`). Địa danh, tước vị, danh từ viết chữ Hán.

---

## 2. State (JSON — sự thật và con số đã xảy ra, lấy đây làm chuẩn)

Đoạn tiếp theo viết từ ngay sau `scene_bridge.last_beat`. Những gì trong `already_told` người đọc đã biết: chỉ nhắc một chữ khi cần, không giải thích lại. Số liệu lấy theo `ledger`; ai biết bí mật nào theo `knowledge_map`.

{
 "meta": {
  "last_chapter": 1,
  "story": "西幻领主：灰石哨所，法兰克王国北部边境狼牙峡谷；人名一律写罗马字（Renard、Vane、Barst、Karl），地名、头衔、阵营写汉字"
 },
 "scene_bridge": {
  "time": "寒风季前第14天，夜幕降临",
  "where": "灰石哨所前院残破木栅与北墙裂隙处",
  "present": "Renard 手持短弩；Karl 与4名老兵握着新装上硬木柄的淬火三棱重矛；铁匠 Barst 守在滚烫的炭炉旁；副官 Vane 守在库房门前",
  "last_beat": "Barst 刚用铁钳夹起第一枚烧透的三棱重矛矛头，狼牙峡谷峭壁间传来凄厉狼嚎",
  "pending": "迎击顺着北风与炉烟摸入哨所的5只霜狼，封堵北墙缺口"
 },
 "timeline": {
  "relative_time": "Renard 穿越后第15天；距北境寒风季降临还有14天；库房黑麦面粉仅够支撑18天口粮",
  "chapter_log": [
   {
    "chapter": 1,
    "summary": "清晨清点灰石哨所家底，Vane报18天余粮，Barst抱怨破风箱与杂铁。Renard消耗120点经验修复风箱石灶并强化铁锤铁砧，打制出首批三棱重矛，峡谷深处传来狼嚎。"
   }
  ]
 },
 "already_told": [
  "Renard 穿越前为机械厂技术员，通宵猝死后接管开拓爵士次子荒凉哨所（ch1已述）",
  "哨所北墙鹅卵石与黏土冻裂3处裂隙，拒马仅存40米（ch1已述）",
  "黑麦面粉420斤、每日最低消耗23斤，仅够支撑18天（ch1已述）",
  "消耗80点经验修复石灶风箱、40点经验强化铁锤铁砧，经验资金池剩余30点（ch1已述）"
 ],
 "ledger": [
  {
   "item": "黑麦面粉储备",
   "value": "420斤（18天口粮）",
   "as_of": 1
  },
  {
   "item": "铁器与原料",
   "value": "劣质杂铁消耗约20斤，剩余120斤；首批锻打出6柄三棱重矛",
   "as_of": 1
  },
  {
   "item": "哨所人员编制",
   "value": "老兵7人，民夫12人，共19人（Renard亲率4名老兵与Karl守缺口）",
   "as_of": 1
  },
  {
   "item": "领地兵工系统资金池",
   "value": "经验资金池剩余 30点（仅 Renard 可见）",
   "as_of": 1
  }
 ],
 "named_entities": [
  {
   "name": "灰石哨所",
   "category": "location",
   "status": "破损度68%，北墙3处缺口，风箱石灶已修复"
  },
  {
   "name": "狼牙峡谷",
   "category": "location",
   "status": "霜狼顺风逼近"
  },
  {
   "name": "三棱重矛",
   "category": "gear",
   "status": "带有深血槽的步卒破兽利器，已制成6柄"
  }
 ]
}

---

# Voice Anchor — Mẫu giọng đã duyệt

**Mẫu giọng mở màn (theo bộ mẫu 领主：我用骑砍系统肝经验 ch.1 & ch.12):**

“法兰克边境，日落要塞，第五军团驻扎地。
罗伯森穿越过来也有大半年了。
来到这个异世界，幸好他有骑砍面板。
这个骑砍面板就是罗伯森闯荡异界的最大凭仗，他不仅可以凭借这个面板训练部队，提升部队等级，打造精兵强将。”

**Mẫu giọng doanh trại thực tế & tính toán (ch.33):**

“里奥子爵要脸，他罗伯森却是利益至上，脸皮养这么厚就是为了用的。
罗伯森虽然嘴上不说，但心里馋那批铁甲可不是一天两天了，现在别人都在免费帮他把这批铁甲送到安全距离了，他还不要岂不是天理难容？”

---

## 5. Nguyên văn phần cuối đoạn 1 (để nối mạch và giữ giọng)

　　白炽色的火焰笔直向上窜起两尺多高，灼热的气浪扑面而来，逼得老铁匠下意识向后退了半步。
　　塞在炭火深处的生铁疙瘩以极快的速度变红软化，表层的黑褐色杂质化作火星从风口疯狂喷溅。
　　Renard 的视线扫过架子上那些崩刃的铁锤与钝锉，心中再次划扣出了四十点经验值。
【经验资金池：30点】
　　光华隐没在铁砧与铁锤的表面，原本坑洼的锻锤平面变得平整规整，握柄处的松木也被压实加固。
　　“别发愣，趁着火候把生铁取出来，先打六把重型矛头。”Renard 挽起袖口沉声催促道。
　　Barst 回过神来，长年打铁养成的本能让他迅速压住心头的惊骇，抄起长柄火钳探入白热的炉膛深处。
　　烧成金红色的铁块被稳稳夹出炉灶，重重摔在平整坚硬的铁砧上方，溅起一圈密集的金色火花。
　　老铁匠单臂抡起那柄焕然一新的八角锻锤，借着沉重的惯性狠狠砸落在发软的铁胚正中央。
　　当的一声脆响震彻了整座棚子，锤头落下的手感沉稳厚重，铁胚内部的残渣顺着锤面迅速挤压崩落。
　　“这锤子吃铁吃得极稳，杂质全给震飞了出去。”Barst 咧开满是黑灰的大嘴赞叹了一声。
　　一锤接着一锤，沉重而富有韵律的打铁声在棚屋中不断回响，金红色的铁块迅速被延展成修长的三棱形状。
　　棚门外传来了杂乱的脚步声，Karl 领着两名青壮民夫扛着六根刚剥去树皮的硬木长杆快步赶了过来。
　　“大人，这是从后山砍回来的红松主干，已经用火烤干了油脂。”Karl 站在门口气喘吁吁地说道。
　　“把木杆尾部削平，前头套箍的位置留出两寸圆径，动作快点。”Renard 盯着铁砧上的矛胚头也不回地下令。
　　民夫们立刻蹲在棚子外的空地上忙碌起来，有了淬炼锋利的铁刀协助，硬木杆上的毛刺被迅速刮除干净。
　　铁砧上方，第一支重型三棱矛头已经初具雏形，长达一尺半的矛身在火光照耀下泛出冷冽的铁色。
　　这种带有三道深血槽的重矛是步卒对抗大型野兽的利器，只要刺入皮肉就能造成巨大的撕裂伤口。
　　只要能赶在十四天内打出三十把重矛，再配上加固完成的拒马桩，灰石哨所就拥有了正面抗击兽潮的底气。
　　Barst 伸出长钳夹住那枚烧得通红的矛头，手臂肌肉高高鼓起，准备将它从滚烫的炭火中猛力拔出。
　　就在铁钳刚刚上提的瞬间，狼牙峡谷深处耸立的陡峭岩壁之间，忽然顺着北风送来了一声凄厉而悠长的狼嚎。

(Đoạn 2 sẽ bắt đầu ngay sau chỗ này.)

---

## 6. Prompt đoạn tiếp theo

Viết tiếp đoạn tiếp theo, 2.000–2.500 字, bằng tiếng Trung.

Tình huống. Đêm ngày 1 ở 灰石哨所. Tiếng sói tru vừa dứt thì một toán 霜狼 gồm 5 con từ 狼牙峡谷 theo mùi khói lò rèn mò tới cửa rào. Hàng cọc cản ngựa cũ nát 40 mét bị con đầu đàn húc xiêu vẹo, đám dân phu lùi dạt về phía tường nứt. Renard cùng 4 lão binh và Karl đã có 5 ngọn thương sắt mới đúc gắn cán gỗ dài. Renard giương nỏ ngắn giữ chốt ở khe nứt tường bắc, chặn không cho người chạy vào kho lương; mỗi bên chỉ có vũ khí trong tay và bờ đá để dựa.

Khoá: Ba con sói bị đâm gục tại chỗ, hai con còn lại tháo chạy về hẻm núi.

Dừng ở lúc Karl định hò reo ăn mừng thì Renard cúi xuống nhổ một mũi tên xương cắm ở chân cọc gỗ. Chuyện dấu vết man tộc lùa sói thuộc đoạn sau.
