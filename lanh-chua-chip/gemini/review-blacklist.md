# Danh sách lỗi để Agent soát khi review (KHÔNG đưa vào SI / prompt của Writer)

Gom từ SI cũ (mục 三, 四, 五) khi SI chuyển sang viết khẳng định (`system-instruction-en-v2.md`). Writer chỉ thấy mặt đúng; Agent giữ mặt sai để bắt lỗi.

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

## Agent bắt thêm (cùng bản test)
- Tên bị phiên âm kèm ngoặc: "莱昂·瓦伦（Leon Varen）", "加雷斯（Gareth）", "佩尔（Pell）".
- Lời nghĩ của nhân vật phụ để trong ngoặc đơn '…'.
- Biểu cảm khuôn mẫu: "嘴角扯出一抹极度森冷的讥诮", "眼底的寒意越来越浓", "掠过一丝波动".

## Bàn tay vàng
- Bảng hệ thống, khung 【】, chữ 系统 / 宿主, hình ảnh hiện trong tầm nhìn.

## Riêng truyện lanh-chua-chip (ghi nhận qua review)
- 小七 báo độ tin cậy 95–99,9% (chip đang hỏng 61%).
- Vào đầu Pell làm lộ kẻ chủ mưu.
- Lặp khuôn cảnh giữa các đoạn (màn tránh trà).
