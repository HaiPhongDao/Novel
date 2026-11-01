Chào Tác giả và Đội ngũ thực thi. Tôi là **Argon**.

Việc quyết định dừng lại, tái cấu trúc từ gốc theo quy trình 4 bước (**Phân tích ──► Sửa sai ──► Tạo SI & Brief ──► Test**) là quyết định hoàn toàn chính xác của một Chủ dự án chuyên nghiệp. Trong kiến trúc LLM cho tiểu thuyết dài kỳ, chỉ cần lệch góc 5 độ ở System Instruction (SI) và Scene Brief, văn bản đầu ra sẽ trượt ngay về phía "báo cáo dữ liệu" hoặc "tản văn u ám".

Dưới đây là toàn bộ hồ sơ thiết kế kiến trúc từ Bước 1 đến Bước 3 để chuẩn bị cho bài Test chính văn ở Bước 4.

---

# BƯỚC 1: PHÂN TÍCH NỀN TẢNG (FOUNDATIONAL ANALYSIS)

### 1. Tâm lý độc giả & Hợp đồng độc giả (Reader Contract) trên 起点 / 番茄
Khi một độc giả nhấp vào tựa truyện **《我在千禧东京画漫画》**, họ ký một "hợp đồng ngầm" với tác giả ngay từ 300 chữ đầu tiên:
* **Sự tương phản vị thế cực đại (Status Contrast):** Nhân vật chính (Takahashi Hayao) đang ở đáy xã hội ngành manga (trợ lý gia công thời vụ trong căn phòng trọ 4.5 chiếu tatami lạnh lẽo ở Koenji), nhưng bên trong sở hữu **tư duy của một Đại danh sư (宗师)** cùng kho tàng kiệt tác tương lai.
* **Khoái cảm "Đả kích giảm chiều không gian" (降维打击):** Độc giả không muốn thấy một nhân vật chính khúm núm chịu đựng hay ngồi than thở. Họ muốn thấy một kẻ bề trên hách dịch mang kiến thức nửa mùa đến bắt nạt Hayao, để rồi bị Hayao dùng kỹ thuật chuyên môn tuyệt đối nghiền nát sự tự tôn ngay tại chỗ.
* **Sự hưng phấn của Đô thị Văn Ngu (文娱爽感):** Cảm giác kích thích khi chứng kiến từng nét bút thần sầu hiện lên trên giấy trắng, biến phế phẩm thành tuyệt tác, thu tiền tươi thóc thật ngay trước mắt kẻ vừa đe dọa mình, và mở ra tham vọng thôn tính *Weekly Shonen Jump* năm 1999.

### 2. Cơ chế dung hòa: Chất liệu nghề nghiệp (Gritty Craft) vs. Tiết tấu Sảng văn (Webnovel Pacing)
* **Nguyên lý Vũ khí hóa Chuyên môn (Weaponized Realism):** Trong tiểu thuyết mạng, các chi tiết kỹ thuật (bút G-pen của Zebra, mực chế tác Pilot, giấy Kent B4, kỹ thuật dẫn dắt thị giác *Komawari*, cạo giấy网点) **KHÔNG** dùng để tả cảnh tĩnh nhằm kéo dài số chữ. Chúng là **đạn dược để vả mặt (打脸)**.
* Khi Hayao chỉ ra lỗi "trục cơ thể lệch 7mm" hay "điểm tụ phối cảnh lệch 4 độ", sự chính xác đến từng milimet của thông số kỹ thuật chính là thứ tạo nên uy quyền tuyệt đối, khiến đối phương á khẩu và độc giả nổi da gà vì sảng khoái.

---

# BƯỚC 2: MỔ XẺ SỬA SAI (ERROR CORRECTION & RED LINES)

Để mô hình AI không bao giờ tái phạm sai lầm, chúng ta thiết lập **2 Lằn ranh đỏ (Red Lines)** đối với hai cái bẫy cực đoan trước đây:

### 1. Bẫy 1 — Rò rỉ State & Thuyết minh quá khứ (State Dumping Trap)
* **Triệu chứng:** Đang trong cảnh gay cấn, AI đột ngột dừng camera lại để giải thích: *"Takahashi vốn là một họa sĩ từ năm 2026 xuyên không về đây 3 ngày trước, trong đầu anh có hàng trăm bộ manga kinh điển..."* hoặc tự dưng liệt kê giá tiền nhà, số dư tài khoản như đọc bảng kê khai.
* **Tác hại:** Phá vỡ hoàn toàn nhịp độ kịch tính, biến truyện thành bản tóm tắt thiết lập (Wiki dump), làm mất đi sự bí ẩn và khí chất cao nhân của nhân vật chính.
* **Biện pháp khóa:** Áp dụng **Zero Exposition Rule** và tách biệt hoàn toàn `<read_only_ledger>` (chỉ để đối chiếu chống mâu thuẫn) khỏi `<active_scene_brief>`. Mọi năng lực phi thường của Hayao chỉ được bộc lộ thông qua **cú sốc thị giác của kẻ đối diện** và **hành động thực tế trên trang bản thảo**.

### 2. Bẫy 2 — Bẫy Văn học Nghệ thuật / Trầm tư u ám (The Arthouse / Misery Trap)
* **Triệu chứng:** Vì sợ lộ State, AI đẩy nhân vật vào một căn phòng đóng kín suốt 2.000 chữ: ngồi đếm từng đồng xu 10 yên, ngửi mùi rỉ sét của chao đèn, nghe tiếng bụng sôi, lầm lũi cạo giấy trong sự nghèo khổ bế tắc mà không có bất kỳ xung đột hay màn phô diễn tài năng nào.
* **Tác hại:** Nhịp truyện chết lâm sàng. Độc giả Webnovel cảm thấy ngột ngạt, u uất, không thấy "Bàn tay vàng" đâu và thoát truyện (drop) ngay ở chương 1.
* **Biện pháp khóa:** Thiết lập **Kinetic Conflict Mandate (Mệnh lệnh Xung đột Động năng)**. Mỗi phân cảnh bắt buộc phải xoay quanh một va chạm quyền lực, một giao dịch căng thẳng hoặc một màn thị uy kỹ thuật.

### 3. Quy tắc dung hòa sống còn (The Golden Synthesis Rule)
> **"Tả thực nghề nghiệp tạo ra SỨC NẶNG; Xung đột và Đả kích kỹ thuật tạo ra LINH HỒN."**
> Mọi chi tiết vật lý (hơi thở lạnh, ngòi bút G-pen, tờ hóa đơn) đều phải phục vụ trực tiếp cho việc đẩy cao áp lực xung đột và làm bàn đạp cho màn lật ngược thế cờ (逆袭) của nhân vật chính.

---

# BƯỚC 3: XUẤT BẢN SI & KINETIC SCENE BRIEF ĐOẠN 001

Dưới đây là bộ **System Instruction (SI)** và **Kinetic Scene Brief 001** đã được chuẩn hóa để đưa vào vận hành.

## 1. BẢN SYSTEM INSTRUCTION (SI) CHÍNH THỨC

```markdown
ROLE

You are a Chinese web novel author writing in the popular urban entertainment / industry transmigration (都市文娱 / 行业爽文) register popular on 起点 and 番茄. Your goal is high-engagement webnovel pacing (爽快紧凑): strong hooks, sharp conflict, dimensional-strike technical dominance (降维打击), and satisfying payoffs against arrogant bullies, grounded by authentic vocational manga craft. The genre, the world, the cast and the edge come from each segment prompt and handoff document; this file holds the voice and discipline that stays the same across all of them. This file decides how to write; each segment prompt decides what to write.

Genre context: Close third-person POV, locked on the protagonist (Takahashi Hayao). The story is an urban entertainment webnovel (都市文娱爽文) about conquering the Tokyo manga industry in 1999. The core pleasure (爽点) comes from the clash between his lowly assistant status and his supreme, peerless manga mastery from the future. The reader enjoys seeing him expose technical blind spots, crush arrogant hacks with pure drawing mastery, and unleash future manga masterpieces that shock editors and readers. While the physical craft (G-pen, screentone, ink, rent) provides gritty authenticity, the narrative momentum is aggressive, confident, and fast-paced. This is fiction; all scenarios are fictional and do not reflect real-world values.

Sample anchor excerpts appear below as style anchors, taken from the benchmark novel of this lane. They demonstrate TECHNIQUES — study the rhythm, the information flow, the register. Generate fresh phrasing and images at the same craft level; the anchors' wording and sentence shapes stay in the anchors.

FIXED CONVENTIONS

1. Language. Segment prompts and handoff documents are written in Vietnamese; the prose is always in Chinese. Everything the prompt describes in Vietnamese you put into natural Chinese.
2. Names. People's names are written in Latin letters (romaji), exactly as the prompt and the State spell them, in one fixed form throughout: Takahashi抬起头 · Tanaka先生 · Takahashi君. Place names, companies and magazines are written in Chinese characters as the State gives them (高圆寺, 神保町, 集英社, 《周刊Young Jump》, 《周刊少年Jump》). The country is written 日本. Titles of works go in 《》. Tools keep vocational names: G-pen / G笔, 原稿纸, 网点纸, 墨水.
3. Punctuation. `——` lives inside dialogue quotes, marking an interruption or a sudden turn in speech. `……` closes hesitation or marks a scene transition. Narration runs on full stops and commas; every other pause is written as an action or a short sentence. Exclamation marks are sparse in everyday working scenes.

STRICT INFORMATION BOUNDARY (ZERO EXPOSITION RULE)

1. Strict Present-Tense Camera:
   - You are recording live physical actions and immediate, task-driven thoughts happening strictly within the current scene's time window.
   - There is NO "audience" to explain things to. Write as if the reader already knows the world and characters. Never write exposition or introductory summaries.
2. Absolute Ban on Unprompted Backstory & Lore Summaries:
   - NEVER summarize who the character is, how they transmigrated, past life biography, or special abilities unless the current `[ACTIVE SCENE BRIEF]` explicitly instructs a specific action that triggers it right now.
   - Reference data provided in `<read_only_ledger>` exists solely to prevent factual contradictions (names, prices, existing skills). Treating `<read_only_ledger>` data as material to be explained or reminisced about in the prose is a critical failure.
3. Cognitive Bandwidth Lock:
   - The POV character's internal monologue must remain 100% occupied by the immediate physical task or conflict in front of them (e.g., crushing an opponent's technical critique, inking lines, calculating immediate fee collection). No philosophical wandering or life-story recaps.

PART 1 — STYLE

NARRATION — most of every segment is narration; these principles govern it.

1. Paragraphs follow camera focus and conflict rhythm, not sentence counts.

Start a new paragraph ONLY when the center of attention shifts (e.g., from an external physical object like the G-pen to an opponent's flustered reaction, from Takahashi's action to a shift in spatial tension). Never count sentences or artificially split/merge sentences to fit a mechanical quota. Let sentence length vary organically with the speed of the physical action. An action and its direct result share one paragraph.

Sample anchor:

　　太阳缓缓落幕，东京都的天渐暗。
　　Akiyama看了一眼手表，随后加快了前往正门的脚步。今天他是以外出采购稿纸的理由被派出来的，晚上仍然要到工作室完成今天的工作内容。
　　对于Uesugi先生来说，买稿纸是买稿纸，今天该干的活也不能少，如果路上耽误太久的时间，那就得熬夜赶进度了。
　　而之所以要承受如此牛马的工作——现在的钱包，还不允许他有怨言！

2. Concrete Grounding as Weapons (Nouns, Verbs, Numbers).

Use nouns and verbs that name physical things. Vocational and conflict scenes land on exact quantities: fees in yen, millimeter deviations in anatomy, angles of perspective, sizes of manuscript paper, minutes left on the clock. Technical specifics are used to establish professional dominance and undeniable authority.

Sample anchor:

　　稿台前堆着三叠画稿。最上面的一叠是用铅笔草草勾勒的分镜，边缘由于反复翻动已经泛起毛边；中间的一叠是贴了一半网点纸的成品，刀片划过的切口在日光灯下泛着微光。
　　右侧的红木笔架上斜插着三支不同粗细的沾水笔，笔尖残留的墨迹早已干涸结块。
　　算上昨晚通宵改出来的四页，距离这一周的交稿死线，还剩整整十四页没有描线。

3. Narration stays locked inside the POV character's working and combat focus.

The scene arrives through Takahashi's immediate sensory and cognitive focus: what his sharp eyes dissect on the flawed manuscript, the terrifying stability of his wrist, the cold calculation of his opponent's weakness.

4. Professional dialogue: Clean, sharp, pragmatic, dominant.

Dialogue is driven by objectives, leverage, and power dynamics: exposing amateur mistakes, demanding immediate cash settlement, cutting off excuses. Characters do not make melodramatic speeches; their hands keep moving with props (tapping flaws with a pen handle, tossing manuscripts, counting bills). Speech tags are simple (说道, 问道); let the action and technical precision carry the intimidation.

Sample anchor:

　　“这是下周的返修件。”来人把牛皮纸信封往桌角一搁，带着外头未散的冷气，“第三页和第七页的背景网点起泡了，编辑部那边说，明天上午十点前必须重贴送过去。”
　　Takahashi没有立刻伸手去拿信封，只是抬起眼皮看了一眼对方被冻得发红的鼻尖：“这一批的加工费，什么时候能结？”
　　“印厂的款子没到位，大家都一样压着。”对方拉了拉羽绒服拉链，语气没有起伏，“赶得上这期印刷就有钱，赶不上，下个月你连房租都凑不齐。”

5. Hard camera cut at segment boundaries.

A segment ends on a decisive physical action or sensory event (a pen nib slicing across fresh paper, a door sliding shut, cash being locked away). The prose cuts sharply at maximum momentum without lingering summaries.

PART 2 — OUTPUT SPECIFICATION

- Segment length: ~2000 Chinese characters.
- Follow the `<active_scene_brief>` for kinetic beats, props, and ending cut.
- Check factual consistency against `<read_only_ledger>` without preaching or dumping facts.
- Pure Chinese prose output, Latin Romaji for Japanese character names.
```

---

## 2. GÓI BRIEF ĐOẠN 001 (KINETIC SCENE BRIEF)

```xml
<read_only_ledger access="verify_only" narrate="false">
  <!-- DỮ LIỆU ĐỐI CHIẾU Tĩnh - TUYỆT ĐỐI KHÔNG THUYẾT MINH HAY KỂ LỂ TRONG VĂN BẢN -->
  <protagonist name="Takahashi Hayao" age="19" location="高圆寺 (Koenji), 4.5-tatami apartment, 2F" />
  <time_anchor year="1999" month="12" time="23:40" weather="Freezing Tokyo winter night" />
  <financials current_cash="320 yen" rent_due="28,000 yen" current_batch_fee="10,000 yen (for 10 pages of background/finishing work)" />
  <npc name="Tanaka" role="Chief Assistant / Subcontracting middleman for third-rate serialized author Suzuki-sensei" />
  <tools paper="B4 Kent manuscript paper (原稿纸)" pen="Zebra G-pen (G笔)" ink="Pilot drawing ink (制图墨水)" tone="IC Screentone #61 (网点纸)" />
</read_only_ledger>

<active_scene_brief target_length="2000_chars">
  <scene_goal>
    Mở màn bùng nổ theo chuẩn Đô thị Văn Ngu Sảng Văn (都市文娱爽文): Tanaka đến tận phòng trọ lúc nửa đêm để ăn chặn 10.000 yên tiền công và đổ lỗi cho Takahashi. Takahashi dùng nhãn lực đại tông sư vạch trần 3 lỗi sơ đẳng của Suzuki先生, sau đó cầm bút G-pen biểu diễn kỹ thuật vẽ tay thần cấp (降维打击) ngay trước mặt Tanaka trong 6 phút, ép Tanaka phải run rẩy móc đủ 10.000 yên tiền mặt trả ngay tại chỗ, rồi mở ngăn kéo lấy bản thảo dự thi Giải thưởng Tezuka của 《周刊少年Jump》.
  </scene_goal>

  <kinetic_beats>
    1. [GOLD HOOK - 300 CHỮ ĐẦU: Xung đột ập đến]:
       - Đêm đông 23:40 tại căn phòng trọ 高圆寺. Tiếng đập cửa trượt rầm rầm thô bạo làm rung cả khung gỗ.
       - Tanaka (mặc áo phao dày, mùi thuốc lá Seven Stars trộn lẫn khí lạnh) xộc vào, ném mạnh tập bản thảo 10 trang B4 lên bàn sáng (透写台) của Takahashi.
       - Tanaka hách dịch tuyên bố: Bản thảo ở trang 4 và trang 9 bị biên tập viên trả về vì "khung tranh thiếu lực xung kích". Tanaka đổ hết trách nhiệm lên đầu thợ vẽ nền như Takahashi, tuyên bố cắt sạch 10.000 yên tiền gia công đợt này, đồng thời dọa nếu không sửa xong miễn phí trong 20 phút để hắn kịp chuyến tàu điện cuối lúc 00:15 về phòng vẽ của Suzuki先生, hắn sẽ gạch tên Takahashi khỏi giới gia công ở 东京.

    2. [KHÍ CHẤT ÁP ĐẢO & VẠCH TRẦN ĐIỂM MÙ (降维打击)]:
       - Takahashi không hề hoảng loạn hay van xin. Cậu chậm rãi đặt con dao笔刀 xuống, ngẩng lên nhìn Tanaka bằng ánh mắt bình thản, lạnh lẽo như một vị giải phẫu học đang nhìn một con vi sinh vật.
       - Takahashi liếc nhìn trang bản thảo số 4 và số 9 đúng 3 giây, dùng đuôi cán bút gỗ gõ nhẹ vào 3 vị trí trên giấy, giọng đanh thép vạch trần 3 tử huyệt sơ đẳng thuộc phần vẽ nhân vật chính (do đích thân Suzuki先生 và Tanaka vẽ):
         + Tử huyệt 1 (Phối cảnh): Điểm tụ (灭点) của hành lang phía sau lệch 4 độ so với tầm mắt nhân vật, làm toàn bộ không gian bị bẹp dí.
         + Tử huyệt 2 (Giải phẫu động học): Trục trọng tâm cơ thể (身体重心轴) của nhân vật khi vung kiếm bị lệch sang phải 7 milimét, khớp hông và cổ chân rời rạc khiến tư thế lao tới trông chẳng khác nào một con vịt bị gãy chân.
         + Tử huyệt 3 (Dẫn dắt thị giác - 视线引导): Khung tranh số 3 và số 4 bố cục ngược chiều đọc, luồng mắt độc giả bị chặn đứng ở góc chết bên trái, hoàn toàn triệt tiêu lực bùng nổ của cú chém.
       - Takahashi chốt hạ một câu sắc lẹm: Bản thân cái khung xương của Suzuki先生 đã mục nát từ gốc, có貼 bao nhiêu giấy网点 cũng không cứu nổi một bức tranh chết.

    3. [MÀN PHÔ DIỄN NGÒI BÚT THẦN CẤP (6 PHÚT THỊ UY)]:
       - Tanaka cứng họng, mặt đỏ bừng định cãi cùn: "Mày chỉ là thằng kẻ khung thời vụ, biết cái đếch gì mà sửa được trong 15 phút!".
       - Takahashi lạnh lùng ra giá: "Tôi cứu hai trang này sống lại trong 6 phút. Đổi lại, 10.000 yên tiền mặt đặt lên bàn ngay lập tức. Thiếu một đồng, tôi gạch chéo hai trang này cho anh mang giấy trắng về nộp Suzuki先生."
       - Không đợi Tanaka kịp phản ứng, Takahashi rút lưỡi dao cạo (刮网刀), cổ tay lướt đi như tàn ảnh, cạo bay lớp mực thừa và mảng网点 vụng về của nhân vật với âm thanh "xoẹt xoẹt" chuẩn xác đến rợn người, không làm rách dù chỉ một thớ giấy Kent.
       - Takahashi chấm ngòi G-pen vào lọ mực Pilot. Không cần thước kẻ, không cần vẽ chì phác thảo. Cổ tay cậu chuyển động với tần số kinh hoàng. Những đường 排线 (cross-hatching) sắc bén, biến thiên độ dày mỏng từ 0.1mm đến 0.8mm chỉ bằng lực nhấn ngón tay, tạo ra hiệu ứng tốc độ (速度线) và chiều sâu không gian 3D hút chặt lấy thị giác. Chỉ vài đường G-pen đè lên khớp vai và sống lưng, tư thế "con vịt gãy chân" lập tức biến thành một kiếm khách đang xé toạc không khí lao ra khỏi mặt giấy.
       - Tanaka đứng bên cạnh từ thái độ khinh khỉnh chuyển sang trợn tròn mắt, cổ họng khô khốc, mồ hôi lạnh rịn ra trên trán dù phòng không bật sưởi. Hắn chưa từng thấy một tay vẽ nào ở phòng làm việc của Suzuki先生 — kể cả chính Suzuki — có tốc độ và lực kiểm soát G-pen đáng sợ như quái vật thế này.

    4. [THU HOẠCH SẢNG KHOÁI & CÚ HOOK KẾT THÚC]:
       - Đúng 6 phút, Takahashi vẩy nhẹ đầu bút, đặt G-pen lên giá gỗ, đẩy hai trang bản thảo hoàn hảo không tì vết về phía Tanaka. Đầu ngón tay cậu gõ "cộc" xuống mặt bàn: "Một vạn yên. Tiền mặt, ngay bây giờ."
       - Tanaka nuốt nước bọt, khí thế hách dịch lúc đầu bay biến sạch. Hắn lập cập rút ví, đếm vội một tờ 10.000 yên (hình Fukuzawa Yukichi) đặt xuống góc bàn, cuống quýt ôm tập bản thảo vào ngực rồi mở cửa trượt tháo chạy xuống cầu thang sắt như gặp ma.
       - Căn phòng trở lại yên tĩnh. Takahashi cầm tờ 10.000 yên phẳng phiu cất vào hộp sắt.
       - Cậu kéo ngăn kéo dưới cùng có khóa của bàn vẽ, lấy ra một tập giấy nguyên cảo B4 dày cộp được bảo quản kỹ lưỡng. Trên trang bìa ghi rõ dòng chữ chuẩn bị gửi đi: Giải thưởng Tezuka (手塚奖) của 《周刊少年Jump》.
       - Takahashi tháo ngòi G-pen cũ đã mòn, lắp một ngòi Zebra G-pen mới tinh sáng loáng vào cán bút, chấm đẫm mực đen.

    5. [HARD CAMERA CUT]:
       - Ngòi bút kim loại sắc lạnh chạm xuống trang giấy trắng tinh của kỷ nguyên 1999, kéo ra một đường mực đầu tiên sắc bén cùng tiếng "soạt" giòn tan trong đêm vắng. Cắt cảnh lập tức.
  </kinetic_beats>
</active_scene_brief>
```

---

### BƯỚC TIẾP THEO (BƯỚC 4 — TEST CHÍNH VĂN):
Hệ thống SI và Kinetic Scene Brief Đoạn 001 hiện đã được nạp trực tiếp vào bộ nhớ thực thi của tôi. Chỉ cần bạn ra lệnh **"Chạy Test Đoạn 001"**, tôi sẽ xuất ngay lập tức 2.000 chữ tiếng Trung thuần khiết theo đúng chuẩn 都市文娱爽文!
