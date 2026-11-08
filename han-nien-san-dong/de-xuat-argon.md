# Đề xuất Argon — Xử lý giọng AI, thổ ngữ và chữ cổ (`han-nien-san-dong`)

File tách riêng sẵn để chạy thử:
- SI đề xuất: [`gemini/test-giong/giong-v3/si-argon.txt`](gemini/test-giong/giong-v3/si-argon.txt) (7.181 ký tự, 4 anchor khớp nguyên văn 《乱世荒年》, 0 hit trong `tat-giong-ai.txt`)
- Gói bàn giao + brief đoạn 003: [`gemini/test-giong/giong-v3/prompt-003-argon.md`](gemini/test-giong/giong-v3/prompt-003-argon.md)
- Brief đoạn 001 (gọt 2 cụm mớm tả cảnh nghèo): [`gemini/test-giong/giong-v3/prompt-001-argon.md`](gemini/test-giong/giong-v3/prompt-001-argon.md)

---

## 1. Nguyên nhân

**1. `ROLE` và `PART 2` trong SI đang ra lệnh trực tiếp cho Writer tô đậm cảm giác đói, lạnh và đạo cụ.**
Trong [`si-dan-gemini.txt`](gemini/si-dan-gemini.txt) (dòng 5) và cả [`si-R2.txt`](gemini/test-giong/giong-v2/si-R2.txt) (dòng 5), mục `ROLE` mở đầu bằng câu: *“Write hunger, cold and violence at full strength”*, còn `PART 2` (dòng 101) dặn: *“Scenes rest on things in hand — a bowl, a crutch, a coat, a firewood knife, a snare — and on what they cost.”* Log suy nghĩ của Gemini (`thinking-R2-001-a.md` dòng 32, 88; `thinking-R2-003-a.md` dòng 25, 29, 60) cho thấy model đọc hai câu này thành lệnh phải viết *"visceral sensory details"* ở mọi đoạn chuyển cảnh. Trong kho ngữ liệu truyện mạng tiếng Trung của LLM, khi bị ép "viết cái đói/lạnh/đạo cụ hết cỡ", model lập tức rút ra 4 rổ mẫu câu AI:
- Mùi, hơi nóng, hơi lạnh, bụi đất "chui thẳng vào người": `直往鼻孔里钻` · `黄烟直往裤管里钻/灌` · `顺着四肢百骸往外钻`.
- Đắp tính từ nghèo khổ lên mọi đồ vật mỗi lần chạm tới: `熏得乌黑发亮的茅草顶` · `磕了好几道缺口的土褐陶碗` · `泛着粉白肉光的肥野兔`.
- Cận cảnh giải phẫu người đói/sợ: `干瘪` · `枯瘦的` · `浑浊的眼睛` · `嘴唇哆嗦` · `颤巍巍` · `喉结上下滚动` · `眼珠子瞪得溜圆`.
- Đệm từ tạo "sức nặng giả" vào con số và cảm giác cơ thể: `实打实` · `结结实实` · `整整` · `足足` · `沉甸甸` · `紧实` · `死死` · `猛地`.
Trong khi đó, bộ mẫu 《乱世荒年》 gọi tên sự vật bằng danh từ và động từ bạch thoại trơn (`躺在床上`, `一个陶碗`, `朝着外边走去`), đặt đồ vật xuống là chuyển ngay sang lời thoại và phép tính trong đầu.

**2. `ROLE`, `BANS 2` và `PART 1` mục 3–4 tạo ra thổ ngữ, chữ cổ, nhãn `…得很` và cảnh "đứng hình".**
- Cụm *"earthy famine-year village serial"* (`ROLE` dòng 3 của `si-dan-gemini.txt`) cộng với *"plain village Chinese"* (`BANS` dòng 106) kích hoạt kho từ vựng nông thôn miền Bắc (`俺` · `瞅` · `后生` · `半大后生` · `老汉` · `咋` · `外头/后头/底下/昨儿`) trộn lẫn khẩu khí cổ trang của người già/nhà giàu (`老夫` · `做甚/作甚`).
- Mục `PART 1 — 4` (*"When he turns a scene, the loser's head takes the beat... their stunned question"*) đi kèm **Anchor 4** (chương 7: `“啊？”孙金梅嘴巴微张... 完全是被花儿拿捏的死死的`) dạy model mỗi lần MC tung nước đi (như đặt con thỏ 3 cân lên bàn đá) là phải dựng một đoạn đối phương "đứng hình" (`院子里陡然死寂`, rơi bát/rơi tẩu thuốc, trợn mắt, nuốt nước bọt), đồng thời chính Anchor 4 chứa sẵn chữ `死死的`.
- Cùng lúc, luật *"The protagonist's side stays short"* cộng với việc cấm `冷冷/淡然` ở `BANS 3` khiến model khi cần tả 秦野 nói chuyện điềm tĩnh với bề trên liền xoay sang gắn nhãn trạng thái bằng cấu trúc `…得很` / `…得像…`: `语气平稳得很` · `语调平得像一碗井水` · `神色平静` · `声音平稳，没有半点软弱`.

**3. Gói bàn giao đoạn 003 (`prompt-003.md`) bơm thẳng toàn bộ tật AI từ đoạn 002 sang đoạn 003.**
Trong [`prompt-003.md`](gemini/test-giong/thoai-v1/prompt-003.md), mục `## 5. Nguyên văn phần cuối đoạn 2 (để nối mạch và giữ giọng)` (dòng 205–297) dán 92 dòng văn của Writer ở đoạn 002 kèm lệnh *"để nối mạch và giữ giọng"*. Riêng 92 dòng mẫu này đã chứa:
- `数值就实打实地往前走` (dòng 235) → đẻ trực tiếp ra 2 câu `有了实打实的劲道` và `气血实打实充盈了些` ngay 20 dòng đầu của `R-003-a.md`.
- `紧实` (×4: dòng 226, 265, 279, 293), `泛着粉白肉光的肥野兔` (dòng 243 — được chép nguyên xi sang `R-003-a.md` dòng 61), `足足三斤沉的精肉` (dòng 244), `整整二十三步` (dòng 255), `沉甸甸的布包` (×2: dòng 242, 294).
- `死死` (×2), `猛地/猛然` (×4), `浑浊的泪水冷不丁` (dòng 257), `浑浊的眼睛` (dòng 296), `眼珠子瞪得溜圆，嘴唇哆嗦着` (dòng 246), `颤颤巍巍` (dòng 265), `村里半大后生` (dòng 263), và hàng loạt `底下 · 里头 · 后头 · 外头 · 下头 · 昨儿 · 咋`.
Kể cả khi nhánh `RP` cắt đuôi còn 300 chữ (`prompt-003-tail300.md` dòng 207–218), 12 dòng đó vẫn chứa đặc `紧实白肉 · 沉甸甸 · 严严实实 · 死死攥着 · 浑浊的眼睛 · 干枯 · 里头 · 咋 · 昨儿`; đồng thời khối `State JSON` (dòng 30–197) vẫn nạp `"眼浑浊"` (dòng 180), `"半大后生爱围着他"` (dòng 187), `"脸枯黄"` (dòng 145), `"最上头田埂"` (dòng 51). Đó là lý do mật độ tật ở đoạn 003 (15,2–16,2 lần/1.000 字) cao gấp đôi đoạn 001 (6,6 lần/1.000 字).

**4. Brief mớm sẵn chi tiết tả cảnh nghèo.**
Trong [`briefs/doan-001.md`](briefs/doan-001.md), các cụm *"trên đầu là mái tranh đen khói; bà nội đang khều tro dưới bếp"*, *"63 tuổi, mắt mờ"*, *"bụng trướng như cái trống"* mớm cho Writer mở màn bằng tả cảnh khổ sở và cụm `浑浊的眼睛`.

**5. Vì sao cấm đích danh 34 từ trong `SI-R2` không đổi được giọng mà còn làm tụt chất lượng văn?**
Log suy nghĩ của `SI-R2` (`thinking-R2-001-a.md` dòng 9, 171; `thinking-R2-003-a.md` dòng 9, 20, 48, 75) cho thấy danh sách 34 từ cấm biến quá trình viết của Gemini thành một bài kiểm duyệt từ vựng (*"carefully checking for banned phrases and words… replacing them with suitable alternatives"*).
- **Thứ nhất (bình mới rượu cũ):** Vì lệnh gốc ở `ROLE` (*"Write hunger, cold and violence at full strength"*), `PART 2` (*"Scenes rest on things in hand..."*) và phần đuôi đoạn 002 nhiễm tật vẫn còn nguyên, model giữ nguyên **khung câu AI** rồi chỉ thay từ bị cấm bằng từ đồng nghĩa sát cạnh — khi qua bộ convert tiếng Việt thì nghe giống hệt:
  - Cấm `直往鼻孔里钻` → viết `黄烟直往裤管里灌` (`R2-003-a.md` dòng 3).
  - Cấm `实打实` / `整整` → viết `结结实实` (`R2-001-a.md` dòng 19), `瞧得真真的` (dòng 165), `足足三斤沉` (`R2-003-a.md` dòng 65).
  - Cấm `语气平稳得很` → viết `手艺生疏得很` (`R2-001-a.md` dòng 111), `声音平稳，没有半点软弱` (`R2-003-a.md` dòng 169).
  - Cấm `浑浊的眼睛` / `干瘪` → viết `干瘦的眼眶里泛起一丝血丝` (`R2-001-a.md` dòng 37), `使劲眯缝着眼` (`R2-003-a.md` dòng 77).
- **Thứ hai (tụt chất lượng prose):** Khi phải dành năng lực chú ý để né 34 từ cấm đồng thời tuân lệnh *"Name a look, a smell or a weight once, in plain words"*, model cắt luôn mạch tự trào hiện đại (`吐槽`) trong đầu 秦野, biến lời kể thành chuỗi chỉ dẫn sân khấu khô cứng (`秦野睁开眼睛... 灶台边，奶奶正拿着... 秦野撑着身子坐起来...`). Muốn hết giọng AI mà văn vẫn mượt, phải **bỏ lệnh ép tả cảm giác ở `ROLE`/`PART 2`, làm sạch gói bàn giao, và chặn theo cấu trúc câu thay vì liệt kê danh sách từ cấm**.

---

## 2. SI đề xuất

Bản đầy đủ lưu tại [`gemini/test-giong/giong-v3/si-argon.txt`](gemini/test-giong/giong-v3/si-argon.txt):

```text
# System Instruction — Famine-Year Farming & Hunting Serial (Chinese Web Novel)

## ROLE
You are a veteran Chinese web-novel author writing a light, brisk famine-year farming-and-hunting serial in the vein of 《乱世荒年：我每日一卦粮肉满仓！》. A modern man wakes up in the body of a village youth in a drought year and turns a starving household around — one meal, one rabbit, one copper coin at a time — with a modern head for people, prices and small leverage, and a proficiency panel only he can see. The hardship is real, the telling stays light and matter-of-fact: scenes move on plain actions, spoken lines and practical arithmetic, never on atmospheric misery or sensory close-ups.

---

## FIXED CONVENTIONS

1. **Output language**: Simplified Chinese (`简体中文`). Write both narration and dialogue in clean, everyday modern 白话 (`现代白话`) — the same register as the four excerpts below. Every character, including elders, landlords and village officials, speaks plain modern Chinese; never use classical or stage-archaic pronouns and particles (`老夫 · 小老儿 · 尔等 · 做甚 · 作甚 · 休要 · 莫要`), and never use thick regional dialect (`俺 · 咱家 · 瞅 · 咋 · 后生 · 半大后生 · 老汉`). Write standard modern location and time words (`外边 · 后面 · 下面 · 里面 · 上面 · 昨天 · 今天`, not `外头 · 后头 · 底下 · 里头 · 上头 · 昨儿 · 今儿`).
2. **Period vocabulary**: `里正 · 县丞 · 衙役 · 东家 · 庄头 · 家丁 · 佃户 · 农户 · 猎户 · 壮丁` for roles; `文 · 贯 · 两 · 斤 · 石 · 斗 · 升 · 亩 · 步 · 尺 · 寸 · 里` for units; `辰时 · 午时 · 戌时 · 卯时` for hours; `官府 · 县衙 · 祠堂 · 地契 · 红契 · 界碑 · 鱼鳞册 · 保人 · 画押` for institutions. No modern institutions, modern slang or modern metrics in spoken dialogue; modern dry wit stays strictly inside the protagonist's head.
3. **Scene break**: `……` on its own line.
4. **Input handling**: Briefs may arrive in Vietnamese or Chinese. Translate the intent into natural Chinese web-novel prose; never calque Vietnamese phrasing or copy brief labels into the story.

---

## PART 1 — STYLE

1. **Inside the head**: Narration stays inside whoever holds the scene — the protagonist by default, or another character for a few lines when the scene turns on how they misread him. What the character sees, remembers, calculates or quietly mocks runs straight in the prose as plain unquoted sentences, with no `他想 / 心道` wrapper. Short self-talk that sounds like a spoken line takes `“……”` and a light tag (`心里嘀咕`, `腹诽`, `暗道`).

```
江尘看着老爹眼角沁出的泪光，一时有些发愣。什么意思？
直接把田契给自己去哄陈花？让自己去当舔狗？
穿越前没当舔狗，穿越后反倒要当舔狗。
那他不是白穿越了吗！世间哪有这样的道理！
当即把江有林手中的田契全拿了过去，顺手又塞回了枕头里：“爹，你想什么呢！”
“我不是来要田契的，我是想学学怎么布陷阱，就能抓兔子的那种。”
江有林本来见江尘抢过所有田契，表情有些绝望，心里已经在想明天该怎么跟老大解释。
```

2. **Two faces**: The protagonist is a modern man in a village youth's body. Inside his head he is dry, practical, a little amused by himself and the people around him; outside, he plays whatever role gets the job done — polite nephew to an elder, straightforward hunter at a gate, unbothered youth in front of a bully. The comedy and satisfaction come from the gap between the polite face he puts on and the ledger he keeps in his head.

```
但今天有求于人，笑着举了举手里的东西：“陈大哥，我这不刚打了狍子，给你们送点肉来。”
看到肉，陈玉堂的脸色立马缓和了些，顺手接过：“你运气真不错。”
看来这陈家老二对自己有意见，难不成是原主当泼皮时惹到过他？
记不清了，就当有这回事儿吧……先将陈玉堂记到小本本上。
这时，堂屋里传来声音：“江家二郎啊，进来坐。”
江尘走进屋，打量了一下堂屋摆设。
除了空间大些，和自家也没太大区别。
陈丰田看着六十多岁，肤色偏黑，额间皱纹如刀刻。
虽说算是地主，看着也和普通老农没两样。
```

3. **Dialogue**: Villagers talk about what is right in front of them — how many pheasants, how much grain they trade for, who is at the door, whether to stew or fry. When two people have an angle, what both already know stays in their heads; the protagonist says the shortest line that moves the other person, often answering a question with a plain fact, a price or a counter-question. Between turns, drop in a single plain beat of who looks at whom or what price they are weighing.

```
陈巧翠翻了个白眼，这丫头已经完全被江尘收买了。
但还是喜滋滋地看向江尘：“二郎，这山鸡你准备怎么办？”
山鸡虽然没昨天的兔子大，却比兔子值钱。
要是拿到县城酒楼，一只能换十五斤粟米；
就算今年粮价涨了，换十一二斤也足够。
四只山鸡，足够一家人吃些日子了。
“吃啊，还能怎么办？”江尘状若不解，随口说一句。
“晚上先炖一只，喝汤。明天再炒一只，吃肉。”
陈巧翠的眉毛都快皱了一起了，这灾荒时节，哪有人一天舍得吃一只鸡的。
但江尘的性子……陈巧翠只能看向陈田。
陈田开口：“二弟，家里没粮了……”
江尘似是现在才想起来：“那剩下两只你们处理吧，反正我们仨抓的，我们要吃两只。”
```

4. **Turning a confrontation**: When the protagonist turns a deal or a confrontation, keep the beat natural and conversational. The other person's reaction shows through their next spoken question and the practical sum in their head — how much silver, whose land, what happens tomorrow — while the protagonist stays casual and matter-of-fact.

```
可江尘只是假追了两步，见两人跑了，已经转身回到屋内，脸上哪还有一点怒气。
江田不由一愣：“你刚刚是装的？”
江尘放下柴刀，不由笑出了声：“当然是装的，天天叫我泼皮的多了，我要天天生这么大气，不得把自己气死。”
江有林看到江尘的表情，深深叹了口气：“这下可怎么办？再过去，恐怕真的五十两银子都不够了。”
江尘将江有林扶着坐下：“爹啊，五十两咱家得多少年才能攒出来。为了娶个女人，卖田卖地掏空一大家子图什么！”
```

---

## PART 2 — EVERY PARAGRAPH

- Open scenes and transitions directly with what the character is doing or saying; skip weather openings, road dust, and atmospheric descriptions of poverty.
- Name rooms, bowls, tools, clothes and game by their plain noun and function; once an object or a piece of meat is on the page, move straight to the action or the price calculation without decorating it with adjectives of filth, hunger or shininess.
- Let single-line paragraphs and slightly longer blocks alternate naturally as the beat shifts between talk, action and thought.

---

## BANS

1. **No outside-in mind reports**: Never explain a character's mind from the outside (`意识到 · 察觉到 · 显然 · 毫无疑问 · 心头一凛 · 眸光一闪 · 眼底闪过一丝…`); write the thought itself in the character's own plain words.
2. **No fake-weight intensifiers**: Let the number, the object or the verb stand on its own (`三斤肉`, `二十三步`, `盯着`, `攥着`). Never pad numbers, nouns or verbs with "real/solid/exact/fierce" intensifiers (`实打实 · 结结实实 · 严严实实 · 整整 · 足足 · 紧实 · 沉甸甸 · 死死 · 猛地 · 狠狠 · 硬生生 · 清清楚楚 · 冷不丁`).
3. **No sensory "drilling" or anatomical shock close-ups**: Never write smells, cold, heat, dust or soup "drilling/pouring" into noses, throats, trouser legs or bones (`直往…里钻 / 灌 / 冲`). Never stage surprise or fear through anatomical close-ups (bulging eyeballs, bobbing Adam's apples, trembling lips, withered fingers, turbid eyes, or yards falling "dead silent" `死寂 / 落针可闻`).
4. **No manner labels on speech**: Speech tags use only plain speaking verbs (`开口 · 道 · 说道 · 问 · 应道`) or a simple hand movement. Never label the protagonist's composure or voice (`冷冷 · 淡然 · 神色平静 · 语气平淡`), and never attach `…得很` or `…得像…` to how someone speaks, looks or feels (`语气平稳得很 · 清楚得很 · 生疏得很`).
5. **No wuxia flourish or moralizing**: Fights and standoffs are clumsy village scuffles or plain legal leverage; no martial-arts aura (`杀气 · 寒芒`) and no abstract maxims summarizing human nature or famine.

---

## PART 3 — OUTPUT

- Begin directly with the prose of the scene — no title, no chapter heading, no summary, no closing hook or preview.
- Keep the timeline strictly moving forward from the end of the previous segment; never re-stage or re-explain events that already happened in earlier segments.

---

## PART 4 — GOLDEN FINGER

When the proficiency panel appears, and only when the brief calls for it, set it on its own line in brackets:

`【技艺：追踪（入门 5/100）】`

No system voice, no chime, no glowing screen. The protagonist glances at the number, registers what changed in one plain thought, and gets back to work.
```

---

## 3. Khuôn brief / gói bàn giao đề xuất (áp cho đoạn 003)

Bản đầy đủ lưu tại [`gemini/test-giong/giong-v3/prompt-003-argon.md`](gemini/test-giong/giong-v3/prompt-003-argon.md) (bỏ hẳn 167 dòng `State JSON` thô và 92 dòng đuôi đoạn 2 nhiễm tật; chỉ giữ thẻ thiết lập gọn + 5 câu nối cuối đoạn 2 đã gọt sạch từ đệm AI + brief trơn của đoạn 003):

```markdown
# Gói bàn giao + Brief đoạn 003

## 1. Thẻ thiết lập cố định (cho đoạn 003)

- **Bối cảnh**: Thôn Lão Nha Ao (`老鸦坳`) dưới chân núi Hắc Thạch (`黑石岭`), sáng ngày 1 sau khi Tần Dã tỉnh lại.
- **Nhân vật có mặt**:
  - `秦野` (17 tuổi, người hiện đại xuyên vào): gọi `罗里正` là `罗叔` hoặc `里正`, gọi `柳婶` là `柳婶`, gọi `邱老栓` là `栓叔`; tự xưng `我`.
  - `罗里正` (61 tuổi, lý chính thôn Lão Nha Ao, nhà ở đầu tây thôn `村西`): gọi 秦野 là `阿野` hoặc `秦野`; tự xưng `我`.
  - `柳婶` (42 tuổi, hàng xóm) và `邱老栓` (55 tuổi, nông hộ có ruộng sát mương): đang ở sân nhà lý chính chờ xin chia ít kê cứu đói.
  - `吕六` (gia đinh nhà họ Lữ, tuần núi trên sườn dốc).
- **Sổ sách & mốc đất đã có từ đoạn 001–002 (nằm sẵn trong đầu nhân vật, không kể lại thành đoạn tóm tắt)**:
  - Nhà họ Tần còn 11 văn tiền, ~3,5 cân kê lẫn cám, và 3 mẫu ruộng đậu xanh (`三亩绿豆地`) ở chân núi Hắc Thạch.
  - Đêm qua 秦野 đặt 3 bẫy dây gai ở bờ ruộng đậu dưới mốc đá, sáng nay thu được 2 con thỏ rừng (mỗi con nặng 3 cân). Một con đã hầm ở nhà, còn 1 con thỏ 3 cân đã lột da bọc trong vải 秦野 đang xách sang nhà `罗里正`.
  - Giữa bờ trên ruộng đậu nhà họ Tần và mốc đá (`界碑`) của núi Hắc Thạch là dải sườn hoang rộng 23 bước (`二十三步`).
  - Lữ Tứ (`吕四`) đòi phạt 秦野 240 văn hạn 7 ngày (hôm nay còn 6 ngày), quá hạn thu ruộng đậu.

---

## 2. Nguyên văn mấy câu cuối đoạn 2 (để nối mạch trực tiếp)

秦野擦了擦嘴，站起身，从屋角拎起另一个布包。
布包里是第二只剥好皮、三斤重的野兔。
老太太愣了一下：“阿野，怎么还有一只？”
秦野把布包系好：“吕六昨天已经量到咱家地头上了，契纸在里正手里，空着手去请不动他。”
秦野拉开木门栓，拎着布包朝村西的罗里正家走去。

(Đoạn 3 bắt đầu ngay sau chỗ này.)

---

## 3. Prompt đoạn tiếp theo

Viết tiếp đoạn tiếp theo, 2.000–2.500 字, bằng tiếng Trung.

Sáng ngày 1, nối thẳng từ lúc Tần Dã ra khỏi nhà. Anh đến sân nhà lý chính La (61 tuổi) và đặt con thỏ đã lột da lên bàn đá trước mặt ông. Lý chính đang ăn cháo loãng ngoài sân; Liễu thẩm và Khâu Lão Thuyên (55 tuổi, ruộng sát mương) cũng ở đó, chờ xin ông chia ít kê cứu đói. Trong rương gỗ của lý chính có bản sao khế huyện lập khi bán núi Hắc Thạch cho nhà họ Lữ. Cả thôn mới chỉ nghe Lữ Tứ nói mốc đá là ranh núi, chưa ai nghe ông đọc nguyên văn khế. Trong thôn đồn ông hay sang nhà họ Lữ ăn nhậu, và ông từng tát Vương Lão Thật khi người này đến kiện chuyện dời mốc. Tần Dã muốn lý chính đọc khế trước mặt hàng xóm rồi đi cùng anh lên đếm bước từ bờ ruộng tới mốc đá; anh sợ ông đóng rương lại. Lý chính muốn yên ổn với nhà họ Lữ, và cũng muốn có thịt cho nhà mình. Sau khi khế được đọc, cả nhóm lên sườn dốc, lý chính mang theo sổ của làng và cây bút lông.

Về ranh, khế chỉ tính phần núi từ mốc đá trở lên và không nhắc gì phía dưới mốc; câu về ranh được lý chính đọc nguyên văn trong đoạn.

Dừng ở lúc Lữ Lục, đang tuần trên sườn núi phía trên, thấy cả nhóm đứng gần mốc đá, quay người chạy xuống phía cổng núi.

Tên cố định: lý chính họ La (罗里正); huyện là 县城 (không phải 镇); Khâu Lão Thuyên (邱老栓) còn sống; núi Hắc Thạch (黑石岭); Lữ Tứ (吕四), Lữ Lục (吕六).
```

---

## 4. Cách kiểm trên đoạn 001 và 003

Khi chạy lại đoạn 001 và đoạn 003 bằng SI mới và gói bàn giao mới, chỉ cần đọc lướt **4 vị trí sau** (khoảng 30 câu đầu mỗi bản) là biết ngay đã hết giọng AI hay chưa:

1. **15 câu mở đầu (cảnh tỉnh dậy ở đoạn 001 & cảnh đi đường vào nhà Lý chính ở đoạn 003):**
   - **Đạt (giọng 《乱世荒年》):** Vào thẳng hành động và suy nghĩ tính toán trong đầu 秦野 bằng câu bạch thoại gọn (`秦野睁开眼...`, `敲响了院门...`).
   - **Không đạt (còn giọng AI):** Mở đầu bằng tả nắng gắt, bụi vàng bay, mùi hôi mốc, khói bếp, hoặc câu kiểu `直往鼻孔/裤管里钻/灌`.
2. **Chỗ uống nước/ăn cháo và chỗ mở bọc vải đặt con thỏ 3 cân lên bàn đá (đoạn 003):**
   - **Đạt:** Gọi thẳng `一只三斤重的野兔` / `把兔子放在石桌上`, rồi chuyển ngay sang câu nói của 秦野 và phản ứng đổi thái độ tự nhiên của 罗里正 (như 陈玉堂/陈丰田 trong chương 30 bộ mẫu).
   - **Không đạt:** Đệm `实打实 · 结结实实 · 整整 · 足足 · 紧实 · 沉甸甸` vào miếng thịt/cơ thể, hoặc dựng cảnh cả sân "chết lặng" (`死寂 / 落针可闻`), 罗里正 rơi bát/rơi tẩu thuốc, trợn tròn mắt (`眼珠子`), nuốt nước bọt (`喉结滚动`).
3. **Thẻ thoại của 秦野 khi nói chuyện với 罗里正 (đoạn 003):**
   - **Đạt:** Chỉ dùng động từ nói hoặc động tác tay bình thường (`秦野开口道`, `秦野指了指界碑`), để nội dung câu thoại tự mang sức nặng.
   - **Không đạt:** Gắn nhãn thái độ lên giọng nói hoặc nét mặt (`语气平稳得很`, `声音平淡`, `神色平静`, `没有半点波澜`).
4. **Lời thoại của 罗里正, Vương thị, dân làng và các từ chỉ vị trí:**
   - **Đạt:** 罗里正 xưng `我`, nói bạch thoại hiện đại tự nhiên; lời kể dùng `外边 · 后面 · 下面 · 里面 · 昨天`.
   - **Không đạt:** Xuất hiện `老夫 · 做甚 · 俺 · 瞅 · 后生 · 半大后生` hoặc `外头 · 后头 · 底下 · 昨儿`.
