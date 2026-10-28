# Danh sách lỗi chung — Agent soát khi review mọi truyện (KHÔNG đưa vào SI / prompt của Writer)

SI viết khẳng định: Writer chỉ thấy mặt đúng; Agent giữ mặt sai ở đây để bắt lỗi. Mỗi truyện có thêm danh sách riêng ở `<ten-truyen>/gemini/review-blacklist.md` (lỗi gắn với nhân vật, bàn tay vàng, canon của truyện đó).

Nguồn: gom từ SI cũ (mục 三, 四, 五) của `lanh-chua-chip` và các lần Tác giả / Agent bắt lỗi khi chạy truyện đó. Ví dụ trích dẫn mang tên nhân vật lanh-chua-chip, nhưng kiểu lỗi là chung.

Đọc cùng [sổ kinh nghiệm](kinh-nghiem.md). Đây là danh sách để phát hiện và đối chiếu, không phải lệnh cấm một từ trong mọi ngữ cảnh. Cơ chế, điểm nhìn và register riêng của truyện quyết định việc đó có thật sự là lỗi; nguồn và ngoại lệ ở [bảng nguồn](nguon-kinh-nghiem.md).

## Thoại lưu loát (Tác giả 23/10, Kỵ sĩ; liên hệ bài học Gareth)

- Lượt nói chưa trọn ý đã bị chặt bởi động tác, thẻ thoại hoặc đổi đoạn.
- Câu đáp chỉ xác nhận, không tiếp câu hỏi/khó khăn/đề nghị trước đó, dù tình huống cần trao đổi.
- Lời báo cáo hoặc hướng dẫn bị rút thành khẩu lệnh; nội dung lại do người kể giải thích thay người nói.
- Nhân vật cấp dưới chỉ còn “是，大人”, không có chỗ nêu điều mình chưa hiểu hoặc cần người trên quyết.
- Câu dài thêm nhưng chỉ lặp dữ kiện; lời qua lại không tiến lên.

Khẩu lệnh ngắn có thể đúng chức năng. Đọc liền cuộc trao đổi để xét mạch ý; không chấm bằng hạn mức số chữ. Nếu brief chỉ cho một người ra lệnh và người khác thực hiện, cần sửa cơ hội đối đáp trong cảnh, không chỉ thêm tính từ “lưu loát” vào SI.

## Kết đoạn / cấu trúc
- Câu chốt, câu đúc kết, câu "nâng tầm" cuối đoạn; hồi ứng "khéo" cuối đoạn.
- Câu giải thích cảm xúc mà hành động đã thể hiện (解释潜台词).
- Câu thu gọn, hành động chuyển cảnh, lời người kể báo trước, thoại thêm vào chỉ để kết.
- Cao trào bị kể lướt ("一番激战后……").
- Nhân vật chính ngồi một mình suy tính dài.

## Câu chữ (tiếng Trung)
- Ba câu ngắn liên tiếp: "打不过，跑不掉，也躲不住".
- Châm ngôn "不在 A，在 B".
- So sánh kiểu tiếng Anh: "比在场所有人都好".
- Cảnh im lặng vạn năng: "一下子没了声音，只剩柴火噼啪响".
- Câu liệt kê trơ trọi; danh từ cảm thán đứng một đoạn ("某某男爵！"); câu hỏi tu từ đứng một đoạn ("真要打？""凭什么？").
- Mỗi động tác một đoạn (chia quá vụn).
- Lượng từ mơ hồ: 一丝、几分、某种、淡淡的. Danh từ trừu tượng: 命运、重量、意味.
- Sáo ngữ của truyện mẫu: 嘴角微微上扬、眸子、毛骨悚然、死神的镰刀.
- Thẻ thoại văn hoa: "语气很和善地".
- Meme mạng, từ hiện đại dày đặc ("新手村", "全息游戏").

## Tác giả bắt được (test SI v2, đoạn 1)
- Câu so sánh giải thích gắn sau lời giới thiệu giọng nói / âm thanh: "平淡得像是在宣读一份报废仪器的检测清单".
- Dấu —— trong lời kể để chêm câu giải thích: "——那是握剑留下的痕迹".
- Mùi "chui / xộc" vào mũi: "直往鼻孔里钻", "直冲鼻腔", "直冲面门", "钻进鼻腔" — gần như đoạn nào cũng có.

## Tác giả bắt được (lượt 2, đoạn 1): "giải thích thừa"
- Giọng nói + "得像…": "平板得像在念一份讣告", "平稳得像是一条直线", "干瘪得像两片干枯的树叶在摩擦", "平淡得听不出喜怒".
- So sánh diễn giải: "那眼神不像…倒像是个…冷血商人", kết đoạn "宛如从始至终都未曾有人碰过".
- "不是 A，而是 B" cho cảm giác: "不是饥饿的痉挛，而是一种源自内脏深处的剧烈反胃".
- Lời kể giải thích lý lịch / động cơ: "那是早年在战场上落下的残疾，所有动作都只靠右手完成", "这具身体残存的记忆太碎，他需要确切的数字", "不过是…的表象罢了".
- "空气骤然冷了几分".
- **Nguồn gốc phần lớn từ prompt của Agent:** câu thiết lập có mệnh đề nhân quả / diễn giải ("tay trái buông thõng **nên** mọi việc làm bằng tay phải", "**như chưa từng** đụng tới") bị Writer kể lại nguyên văn thành câu giải thích.

## Tác giả: bản 2 lượt 2 "cắt mất quá nhiều phần giải thích", thích Gareth bản 1 hơn
- Phân biệt: **so sánh trong đầu / miệng nhân vật** ("像只受惊的鹌鹑", "倒像是个坐在账台后面…的冷血商人" của Gareth) là **giọng nhân vật → giữ**. **So sánh của người kể gắn vào giọng nói, ánh nhìn, mùi** ("平板得像在念一份讣告", "直往鼻孔里钻") là **giải thích thừa → bắt**.
- Báo cáo của cấp dưới phải là **thoại của chính người đó**, không bị tóm thành lời kể ("低声汇报起来。情况烂得超出了想象。" + liệt kê bằng lời kể = mất giọng Gareth).
- Kiến thức / quy tắc / lý lịch: được, nếu đi qua phép tính của Leon hoặc lời nhân vật.

## Tác giả: "…rất thực" (lượt 2, đoạn 1 bản 3)
- Từ chỉ phẩm chất mà SI dùng để *mô tả cách viết* lọt vào chính văn: "扎得极实", "实在账", "机械平直的声音", "平板无波", "硬邦邦". SI v2 lúc đó lặp plain ×7, concrete ×4, straight ×4, exact ×3, flat ×2 và cho ví dụ "平板" → Writer "diễn" luôn phẩm chất đó vào câu văn. Đã gỡ khỏi SI.

## Agent bắt thêm (cùng bản test)
- Tên bị phiên âm kèm ngoặc: "莱昂·瓦伦（Leon Varen）", "加雷斯（Gareth）", "佩尔（Pell）".
- Lời nghĩ của nhân vật phụ để trong ngoặc đơn '…'.
- Biểu cảm khuôn mẫu: "嘴角扯出一抹极度森冷的讥诮", "眼底的寒意越来越浓", "掠过一丝波动".

## Bàn tay vàng (truyện có hệ thống / chip / kim thủ chỉ)
- Bảng hệ thống, khung 【】, chữ 系统 / 宿主, hình ảnh trong tầm nhìn **khi trái cơ chế hoặc cách gọi đã chốt của truyện**. Lãnh Chúa Chip chỉ có giọng; Mô phỏng có log 【】 trong đầu; bản làm việc Kỵ sĩ có bảng số liệu. Không áp lệnh cấm giao diện của truyện trước lên truyện sau.
- Bàn tay vàng tự có giác quan riêng mà thiết lập không cho: dò nhiệt, theo dấu thứ nhân vật chính không thấy, đọc nhịp tim người khác từ xa ("侦测到低矮热源", "林区核心热源主体未移动").
- Bàn tay vàng gọi sai cách xưng đã chốt (vd. 宿主 thay cho cách gọi của truyện).

## Mạch nối giữa các đoạn (Tác giả 22/10, lanh-chua-chip)
- Đoạn khép tròn như một tập phim: câu cuối đúc kết / tả không khí ("残阳彻底沉入地平线", "谁也没有往后退哪怕半步", "得在…之前，找到…"). Đoạn phải dừng giữa mạch.
- Đoạn sau dựng cảnh lại từ đầu bằng mốc thời gian + tả cảnh ("第八天的清晨，迷雾森林的边缘…") thay vì nối thẳng từ khoảnh khắc đoạn trước dừng.
- Câu chốt ý giữa đoạn của người kể ("活命的温度，比神明更实在", "狼吃人，那是老天爷定下的规矩。可现在，规矩好像变了。").

## Điểm nhìn
- Lời kể vào đầu nhân vật mà prompt chỉ cho hiện qua mắt nhân vật chính (tay sai, người của phe địch) — rất dễ lộ bí mật ("城里那位大人预想的…"). Writer hay lấp bằng cách này khi cảnh có chỗ trống "người kia nghĩ gì".
- Câu hỏi tu từ của người kể đứng một mình ("…到底有什么？").

## Phủ định song song (Tác giả bắt 25/10, Lãnh Chúa Khoa Học)
- Ba cụm phủ định liền nhau để mô tả một người hoặc một trạng thái: "没扶过犁，没挥过铁镐，更没…",
  "没有握过剑柄，更没有摸过农具", "没有回旋余地，没有体面借口".
- Khuôn "phủ định + phủ định + 只有/只是" để nâng nhân vật: "没有嘲讽，也没有敬畏，只有…", "既没有下令，
  也没有叹气，只是…".
- Khuôn "不是 A，而是 B" đứng một mình như một câu nhận định của người kể.
- **Nguồn có thể nằm trong nhà:** SI từng chứa chuỗi phủ định bốn vế, và anchor từng chứa "都不见了 ×3".
  Khi văn lặp lại một khuôn mà SI/anchor cũng dùng, sửa SI/anchor trước khi bắt Writer.
- Cách thay: tả người bằng thứ tay đã làm, thứ mang theo, thứ đang giữ; mỗi đoạn một cái thiếu, gắn với
  cái giá của nó.

## Khuôn "thật/实" (Tác giả bắt 25/10, Lãnh Chúa Khoa Học)
- Động từ + 实 để tự bảo đảm "cụ thể": "每踩实一步", "把袖口攥实", "把话说实", 坐实/砸实/压实.
- Cụm nhấn cùng họ: 实实在在地, 实打实, 结结实实, 真真切切, 扎扎实实, 落到实处.
- Đây là độ cụ thể **giả**: nó không thêm chi tiết, chỉ thêm phó từ. Cách thay: cho kết quả nhìn thấy
  được (bản lề gãy làm hai, chân trượt, tay tê) và để động từ mang sức nặng.
- Đếm bằng `python tools/soat_van.py <file>` — cột `khuon-shi`.

## Nhãn ngữ điệu gắn vào lời nói (Tác giả bắt 25/10)
- "语气平淡" "声音没有任何起伏" "语调生硬" "淡淡地说" "面无表情地道": nhãn thay cho nội dung.
- Câu nói nào cũng có nhãn thì người đọc không còn phân biệt được giọng ai với ai.
- Thẻ thoại đúng chức năng: **ai nói + tay/mắt đang làm gì**; ngữ điệu nằm trong chữ họ chọn.
- Đếm bằng cột `nhan-ngu-dieu`; xem thêm cột `tb-chu-luot`, `luot-cut` để biết thoại có mang tin không.

## Thoại không chủ ngữ, không tiền đề (Tác giả bắt 25/10, Lãnh Chúa Khoa Học)
- Nhân vật chính nói một câu trạng thái không ai hỏi trước, không có chủ ngữ: *"站久了有些发眩。"* —
  người đọc không biết ai đang nói với ai, và câu mọc từ đâu.
- Người hầu báo việc mà không nói việc đó **cho ai**: *"待会儿便送进书房"* — thiếu "给大人".
- Dạng đúng: *"我站久了，有些发晕。"* · *"小的让灶房温了一锅燕麦糊，待会儿便给大人送进书房。"*
- Kiểm: mỗi lượt thoại có chủ ngữ trong chữ (我 / 小的 / 大人), và có người nhận (给大人 / 给您), hoặc là
  câu trả lời cho lượt ngay trước.

## Register xưng hô sai bối cảnh (Tác giả bắt 25/10, Lãnh Chúa Khoa Học)
- Người hầu trong trang viên Tây huyễn nói bằng dạng Trung Hoa đế quốc: "老奴", "奴才", "属下", "末将".
- Người hầu gọi chủ bằng "少爷" khi không phải người nuôi chủ từ nhỏ; gọi thẳng tên chủ.
- Đẳng cấp chỉ hiện ở từ gọi mà thiếu tư thế: không đứng khi chủ ngồi, không dâng bằng hai tay, không
  lùi nửa bước, không mở báo cáo bằng 回大人, chủ tự giải thích việc mình làm cho người hầu.
- Register đúng của repo (theo `lanh-chua-chip`): 大人 / 老爷 / 领主大人; tự xưng 小的 / 小人; 爵士;
  会长; 神父; 老丈. 陛下 chỉ cho vua, 殿下 chỉ cho vương tử.

## Câu cụt (Tác giả bắt 25/10, Lãnh Chúa Khoa Học)
- Một trạng thái hoặc một con số đứng thành câu riêng: "发凉。", "二十三岁，刚捡回一条命。", "冻死了两只。"
  — đọc lên mất nhịp, như người kể đang đọc phiếu.
- Dấu hiệu: nhiều mệnh đề ≤4 chữ; nhiều đoạn chỉ một mệnh đề; câu kể trung bình dưới 20 chữ.
- Chặn cả hai đầu: mệnh đề cụt gia nhập câu nó thuộc về; dấu chấm làm việc sau hai ba mệnh đề.
- Đếm: `soat_van.py` chưa có cột riêng — dùng script tạm (mệnh đề ≤4 chữ, độ dài câu kể) hoặc đọc.

## Thẻ thoại mở đầu mọi lượt (Tác giả bắt 25/10)
- "Osric 微微躬身说道，“…”" ở 24/25 lượt; mỗi đoạn thoại mở bằng tên + 说道.
- Cách thay: vài lượt chạy bằng lời trần, tên quay lại khi cần phân biệt; động từ nói đi với việc tay chân.
- Đếm: cột `the-thoai` (số thẻ) và `tag-dau-doan` (số đoạn mở bằng thẻ).

## Nhân vật chỉ nói việc (Tác giả bắt 25/10, Lãnh Chúa Khoa Học)
- Hai người gặp nhau ở cửa, ở sân, ở phòng sổ mà lượt đầu tiên đã là "vì sao cái bản lề gãy": không chào,
  không hỏi thăm, không có gì ngoài công việc.
- Dấu hiệu: mọi lượt thoại đều đẩy cốt truyện; không lượt nào nói về người, về nhà, về chuyện đang xảy
  ra quanh họ; người hầu chỉ có số liệu để báo.
- Khi gặp: hỏi sức khỏe, đồ ăn, người chết, ai đến ai vắng, một chuyện ngoài việc (con vật, thời tiết,
  hàng xóm), rồi việc mới bắt đầu.
- Đo bằng `tb-chu-luot` và `luot-cut` cùng việc đọc: thoại dài ra không đồng nghĩa có đời sống, nhưng
  thoại toàn 5–6 chữ thì gần như chắc chắn là hội họp.

## Mẫu bám của model (không phải của truyện)
- So sánh tư thế đứng bằng "cọc gỗ": "烂木桩" (A), "旧桩子" (B), "枯木桩" (E) — ba bản bốn lần, không
  có trong bible lẫn prompt. Khi một hình ảnh lặp qua nhiều bản độc lập, đó là mẫu của model.
- Giọng người kể + "得像…" để tả giọng nói (đã có ở mục lỗi chung), và "像两块磨石在蹭" cho giọng khàn.

## Số liệu
- Writer tính sai phép tính đơn giản (vd. 143 pound thịt chia 146 người thành "thêm ba ngày rưỡi"; thiếu lương "trước mốc" bị viết thành "thiếu giữa mùa đông"). Agent kiểm mọi con số; state giữ số đúng.
- Số Ả Rập trong lời kể chỉ ngày ("第6天", "第3天") — lời kể dùng chữ Hán.
- Độ tin cậy vượt khung truyện cho phép (nếu truyện có khung).
