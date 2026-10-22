# Danh sách lỗi chung — Agent soát khi review mọi truyện (KHÔNG đưa vào SI / prompt của Writer)

SI viết khẳng định: Writer chỉ thấy mặt đúng; Agent giữ mặt sai ở đây để bắt lỗi. Mỗi truyện có thêm danh sách riêng ở `<ten-truyen>/gemini/review-blacklist.md` (lỗi gắn với nhân vật, bàn tay vàng, canon của truyện đó).

Nguồn: gom từ SI cũ (mục 三, 四, 五) của `lanh-chua-chip` và các lần Tác giả / Agent bắt lỗi khi chạy truyện đó. Ví dụ trích dẫn mang tên nhân vật lanh-chua-chip, nhưng kiểu lỗi là chung.

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
- Bảng hệ thống, khung 【】, chữ 系统 / 宿主, hình ảnh hiện trong tầm nhìn.
- Bàn tay vàng tự có giác quan riêng mà thiết lập không cho: dò nhiệt, theo dấu thứ nhân vật chính không thấy, đọc nhịp tim người khác từ xa ("侦测到低矮热源", "林区核心热源主体未移动").
- Bàn tay vàng gọi sai cách xưng đã chốt (vd. 宿主 thay cho cách gọi của truyện).

## Mạch nối giữa các đoạn (Tác giả 22/10, lanh-chua-chip)
- Đoạn khép tròn như một tập phim: câu cuối đúc kết / tả không khí ("残阳彻底沉入地平线", "谁也没有往后退哪怕半步", "得在…之前，找到…"). Đoạn phải dừng giữa mạch.
- Đoạn sau dựng cảnh lại từ đầu bằng mốc thời gian + tả cảnh ("第八天的清晨，迷雾森林的边缘…") thay vì nối thẳng từ khoảnh khắc đoạn trước dừng.
- Câu chốt ý giữa đoạn của người kể ("活命的温度，比神明更实在", "狼吃人，那是老天爷定下的规矩。可现在，规矩好像变了。").

## Điểm nhìn
- Lời kể vào đầu nhân vật mà prompt chỉ cho hiện qua mắt nhân vật chính (tay sai, người của phe địch) — rất dễ lộ bí mật ("城里那位大人预想的…"). Writer hay lấp bằng cách này khi cảnh có chỗ trống "người kia nghĩ gì".
- Câu hỏi tu từ của người kể đứng một mình ("…到底有什么？").

## Số liệu
- Writer tính sai phép tính đơn giản (vd. 143 pound thịt chia 146 người thành "thêm ba ngày rưỡi"; thiếu lương "trước mốc" bị viết thành "thiếu giữa mùa đông"). Agent kiểm mọi con số; state giữ số đúng.
- Số Ả Rập trong lời kể chỉ ngày ("第6天", "第3天") — lời kể dùng chữ Hán.
- Độ tin cậy vượt khung truyện cho phép (nếu truyện có khung).
