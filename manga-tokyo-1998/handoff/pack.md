# Tài liệu bàn giao — tiếp tục viết truyện

Bạn là Writer của truyện này. Các đoạn trước bạn đã viết ở một session cũ; tài liệu dưới đây là toàn bộ những gì cần nhớ để viết tiếp đúng mạch và đúng giọng.

**Lần này chưa viết chính văn.** Đọc kỹ toàn bộ, rồi trả lời ngắn bằng tiếng Việt đúng 3 dòng:
1. <Nhân vật chính> đang ở đâu, vừa làm gì.
2. <Nhân vật chính> biết gì về <bí mật chính>.
3. Các con số đang chạy (<người, lương, ngày…>).

Sau đó chờ prompt của đoạn tiếp theo.


---

## 1. Thẻ thiết lập cố định

**Truyện:** …

**Nhân vật chính —** …

**Bàn tay vàng —** …

**Nhân vật phụ**

**Địa danh**

---

## 2. State (JSON — sự thật và con số đã xảy ra, lấy đây làm chuẩn)

Đoạn tiếp theo viết từ ngay sau `scene_bridge.last_beat`. Những gì trong `already_told` người đọc đã biết: chỉ nhắc một chữ khi cần, không giải thích lại. Số liệu lấy theo `ledger`; ai biết bí mật nào theo `knowledge_map`.

{
 "meta": {
  "last_chapter": 6,
  "story": "我在泡沫东京画漫画，1998年11月起的东京；人名一律写罗马字（Fujimoto Ren、Shirakawa Mio、Takahashi），地名、杂志、出版社写汉字，银行写住友银行"
 },
 "scene_bridge": {
  "time": "11月下旬傍晚20点15分",
  "where": "高田马场老旧杂居楼三层 Takahashi 漫画工作室角落下手座",
  "present": "Fujimoto Ren 坐在下手画桌前，左手压稿纸右手握套橡胶套的G笔；Takahashi 先生在中央黑皮转椅上抽 Peace 烟敲铁皮烟灰缸",
  "last_beat": "Takahashi 先生在烟灰缸沿敲击烟蒂，Fujimoto Ren 手腕发力，金属笔尖在第一张棒球原稿空白球场背景上划出第一根笔直锐利的速度线",
  "pending": "Fujimoto Ren 通宵完成剩余14张原稿的透视背景与速度线"
 },
 "timeline": {
  "relative_time": "Fujimoto Ren 穿越后第3个月；距大奖赛初审见报还有18天；距明早交稿底线还有9小时45分钟",
  "chapter_log": [
   {
    "chapter": 1,
    "summary": "17:00讲谈社后门，Ren托Mio带稿，Mio指点正门前台"
   },
   {
    "chapter": 2,
    "summary": "17:10讲谈社四楼，遇前女友Sasaki，窗口位认出Mio"
   },
   {
    "chapter": 3,
    "summary": "17:40四楼，Mio读完64页《记忆碎片》惊艳，顶住Yano压力盖章推荐"
   },
   {
    "chapter": 4,
    "summary": "17:48四楼，Mio解说大奖赛评审与汇款流程，Ren下楼奔赴地铁站"
   },
   {
    "chapter": 5,
    "summary": "18:05神保町三省堂自垫100円买5册B4纸，挤东西线护纸，18:52赶回高田马场"
   },
   {
    "chapter": 6,
    "summary": "18:55进工作室交纸拿回100円，接15张通宵棒球背景任务，20:15划出第一笔"
   }
  ]
 },
 "already_told": [
  "《记忆碎片》双线倒叙与顺行性遗忘症设定（已在ch3详述，不再展开）",
  "大奖赛各档奖金与月例赏对比（150万/70万/30万 vs 10万，已在ch1、ch4详述）",
  "讲谈社与住友银行电汇/支票流程（已在ch4详述）",
  "三省堂B4原稿纸420円/册及调价（已在ch5详述）",
  "G笔燎火去防锈油、钢尺粘十円硬币防渗墨、图钉定位放射线手法（已在ch6详述）"
 ],
 "ledger": [
  {
   "item": "Fujimoto Ren 私人现金",
   "value": "4000日元（垫付100円后已由Takahashi补回）",
   "as_of": 6
  },
  {
   "item": "住友银行存折活期存款",
   "value": "320日元（压在出租屋床垫下）",
   "as_of": 4
  },
  {
   "item": "工作室实习津贴",
   "value": "8万日元/月，扣除3万房租到手5万",
   "as_of": 1
  },
  {
   "item": "伙食补贴",
   "value": "1.5万日元/月（明早六点前完不成15张则扣光）",
   "as_of": 6
  },
  {
   "item": "B4原稿纸耗材",
   "value": "三省堂购买5册共200张，已交付Takahashi",
   "as_of": 6
  },
  {
   "item": "今晚作画任务",
   "value": "棒球漫画背景15张（已完成第一笔）",
   "as_of": 6
  }
 ],
 "deadlines": [
  "完成15张棒球漫画背景与速度线｜次日早晨06:00｜Takahashi限定，延误扣1.5万伙食费",
  "讲谈社编辑部派人取稿｜次日早晨08:00｜印刷厂中午12:00开工",
  "大奖赛初审名单见报｜下个月15号《周刊Young Magazine》增刊｜Shirakawa Mio告知"
 ],
 "main_character": {
  "name": "Fujimoto Ren",
  "identity": "22岁，穿越者，Takahashi漫画工作室底层实习助手，住合宿床位",
  "traits": [
   "右手食指中指有常年握笔厚茧，指甲缝留开明墨水痕迹",
   "算账极清，绝不把希望押在只能勉强糊口的及格线上",
   "基本功扎实，掌握专业助手各种规避失误的小技巧"
  ],
  "status": [
   "连续奔波后双腿沉重，后背汗水干透，双袖卷起，正在画桌前画速度线"
  ],
  "knowledge": [
   "前世记忆中的经典影视与分镜结构（《记忆碎片》等）",
   "1998年东京物价、合租房租金行情与漫画家生存成本"
  ]
 },
 "knowledge_map": [
  {
   "secret": "Fujimoto Ren 投递了64页大奖赛短篇《记忆碎片》并持有讲谈社回执单",
   "knows": [
    "Fujimoto Ren",
    "Shirakawa Mio",
    "Yano"
   ],
   "not_known_to": [
    "Takahashi",
    "工作室其他助手"
   ]
  }
 ],
 "characters": [
  {
   "name": "Shirakawa Mio",
   "role": "《周刊Young Magazine》责任编辑，26岁，灰色西装，短发，抽烟，桌上有小仙人掌，独立推荐了Ren的稿子",
   "speech": "称Ren为Fujimoto桑，自称我",
   "last_seen": 4
  },
  {
   "name": "Takahashi",
   "role": "45岁连载漫画家，画周刊棒球漫画，乱发大眼袋，抽Peace香烟，脾气暴躁，压榨学徒",
   "speech": "称Ren为Fujimoto，自称老子/我",
   "last_seen": 6
  },
  {
   "name": "Yano",
   "role": "副编辑长，44岁，金属眼镜，读者统计夹，偏向成熟工作室",
   "speech": "称Mio为Shirakawa",
   "last_seen": 3
  },
  {
   "name": "Sasaki Yui",
   "role": "22岁实习编辑，Ren大学前女友，跟从Yano",
   "speech": "称Ren为Fujimoto君，称Mio为Shirakawa前辈",
   "last_seen": 3
  }
 ],
 "places": [
  "高田马场老旧大楼三层 Takahashi 工作室（无电梯，弥漫Peace烟味与开明墨水味）",
  "讲谈社（文京区音羽通）",
  "三省堂书店神保町总店（神田神保町）"
 ],
 "objects": [
  {
   "name": "讲谈社新人赏白色复写回执联",
   "holder": "Fujimoto Ren",
   "notes": "折叠整齐贴在Ren衬衫左胸口袋，带着体温"
  },
  {
   "name": "开明制图墨水、斑马牌G笔、粘有十日元硬币的钢制直尺、木画板与图钉",
   "holder": "Fujimoto Ren",
   "notes": "Ren画桌上的专业绘图工具"
  }
 ],
 "rules": {
  "world": [
   "1998年东京泡沫破裂后萧条期，就业困难，漫画为少数上升通道",
   "周刊连载截稿日极其严苛，延误会导致印刷厂停机损失"
  ],
  "mechanics": [
   "专业原稿纸B4 135kg，边缘不可折损；蘸水笔需用火燎除防锈油；直尺需垫高防渗墨"
  ],
  "hard_limits": [
   "Takahashi绝对不能知道Ren私下投稿大奖赛的事"
  ]
 },
 "open_threads": [
  "通宵完成15张背景 [ch6]",
  "次月15号大奖赛初审名单 [ch4]"
 ],
 "conflicts": []
}

---

## 4. Mẫu giọng (trích nguyên văn các đoạn đã duyệt — viết tiếp đúng giọng này)

---

## 5. Nguyên văn phần cuối đoạn 6 (để nối mạch và giữ giọng)

　　他用半截胶带将硬币粘在直尺的反面中心。
　　这样一来，直尺的边缘便与原稿纸保持了一毫米的空隙，墨水不会渗入尺底形成墨渍。
　　这些在专门学校里学不到的零碎办法，是他过去两年在工作室里挨骂换来的经验。
　　桌角的小闹钟无声地走动着，时间滑向了 19 点 40 分。
　　Fujimoto Ren 将十五张原稿按照难易程度重新排好了顺序。
　　第一张原稿是主角挥棒击球的高潮分镜，占据了画纸的大半个版面。
　　球棒击中棒球的瞬间，需要从触球点向外放射出密集的强力速度线。
　　每一根线条都必须从中心向外侧逐渐变细，线条与线条之间的间距不能超过半毫米。
　　一旦有一根线条因为手抖而出现弯折，整张原稿的动态感就会垮塌。
　　Fujimoto Ren 拿起削尖的 2B 铅笔，在画稿的外框边缘标出了消失点的位置。
　　他找来一枚金属图钉，轻轻压入木质画板的中心基准点，作为直尺滑动的定位轴心。
　　主工作台那边传来 Takahashi 先生粗重的呼吸声，以及铅笔划过纸面的沙沙声。
　　屋子里的空气依旧混浊，老式排风扇在窗框上吱呀转动着，却排不散那股浓重的烟味。
　　时间在沉默中流逝。
　　墙上的挂钟滑过 20 点 15 分，工作室里的温度随着夜色渐深而降了下来。
　　连轴转了三天的 Takahashi 先生烦躁地抓着花白的头发，桌角那包 Peace 香烟已经被抽空了大半。
　　当啷一声脆响。
　　Takahashi 先生再次拿起烧到过滤嘴的烟蒂，在满是灰烬的铁皮烟灰缸沿上用力敲打了几下。
　　干燥的烟灰在空气中散开，伴随着他一声低沉的咳嗽。
　　画桌角落里，Fujimoto Ren 的脊背挺得笔直。
　　他整个人微微前倾，左手手掌压在固定好的原稿纸边缘，右手稳稳握住了笔杆。
　　金属笔尖小心地探入墨水瓶中，沾取了三分之一深度的黑色墨水。
　　多余的墨滴在瓶口内侧轻轻刮去，笔锋泛着一层湿润的光泽。
　　Fujimoto Ren 将直尺的一侧对准了图钉的轴心与画面的透视点，笔尖悬停在距离纸面不到一毫米的位置。
　　在 Takahashi 先生敲击烟灰缸的当啷余音里，Fujimoto Ren 屏住呼吸，手腕骤然发力。
　　金属笔尖带着锐利的力道切入纸面。
　　伴随着笔尖划过硬质纸张的微细声响，一根笔直如锋刃、两端收紧的速度线，在空白的球场背景上平整地划开。

(Đoạn 7 sẽ bắt đầu ngay sau chỗ này.)
