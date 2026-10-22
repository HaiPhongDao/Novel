# Review — Lượt 2 · Đoạn 001

## Bản 1 (SI v2) — LÀM LẠI
Bản nháp: `archive/run-2/doan-001-v1.md`. Prompt bản 1: `archive/run-2/brief-doan-001-v1.md`.

**Tác giả:** "vẫn bị lỗi giải thích thừa". Agent đồng ý.

### Giải thích thừa
- Giọng nói + "得像…": "平板得像在念一份讣告", "平稳得像是一条直线", "干瘪得像两片干枯的树叶在摩擦", "平淡得听不出喜怒".
- So sánh diễn giải: "那眼神不像…倒像是个…冷血商人"; câu kết "宛如从始至终都未曾有人碰过".
- "不是饥饿的痉挛，而是一种源自内脏深处的剧烈反胃".
- Lời kể giải thích: "那是早年在战场上落下的残疾，所有动作都只靠右手完成", "这具身体残存的记忆太碎，他需要确切的数字", "不过是…的表象罢了"; "空气骤然冷了几分".

### Nguyên nhân phía Agent
- Thiết lập trong prompt có mệnh đề nhân quả / diễn giải → Writer kể lại thành câu giải thích:
  - "tay trái thương cũ buông thõng **nên** mọi việc đều làm bằng tay phải" → "那是早年…残疾，所有动作都只靠右手完成".
  - Kết đoạn "**như chưa từng** đụng tới" → "宛如从始至终都未曾有人碰过".
  - "Gareth… **tự tìm một lý do để giải thích** cho mình" → cả đoạn hành lang diễn giải ánh mắt Leon.
- SI v2 cho phép so sánh ở mọi cảnh ("a few comparisons" trong cảnh đánh nhau nhưng không giới hạn chỗ khác) → model dùng "得像" khắp nơi.

### Lỗi khác
- 小七 vẫn "叮", "系统重启完成", "宿主感知通道" — prompt chỉ cho cách xưng, chưa cho câu khởi động.
- "私生子" (dù prompt ghi 庶子) và "大夫人" xuất hiện cùng lúc.
- Tính sai: 200 pound ÷ (140 × 1,5) < 1 ngày, văn viết "一天半".

### Làm tốt (giữ hướng)
- Bốn dấu hiệu độc đọc đúng qua cảm giác Leon; "米氏线" đúng y khoa; chảy máu cam đúng giá.
- Kết bằng hành động đặt bát trà vào vệt nước cũ — đúng hướng.
- Tên Latin (Leon, Gareth, Pell, Varen) giữ được trong lời kể.

### Đã sửa
- **SI v2:** so sánh (像、仿佛、宛如、好似、如同) chỉ dùng trong cảnh đánh nhau, mỗi nhịp tối đa một; lời kể kể việc đang diễn ra, lý lịch/động cơ đi qua thoại hoặc hành động; cảm giác gọi tên một lần, trực tiếp.
- **AGENT.md nguyên tắc 11–12:** thiết lập chỉ ghi sự thật trơn; chuỗi kỹ thuật của chip ghi nguyên văn.
- **Prompt bản 2** (`briefs/doan-001.md`): bỏ mọi mệnh đề "nên / như thể"; cho câu khởi động 「K-07重启完成。离线知识库受损61%。」; mẹ Leon là 妾; khẩu phần 1 pound/người/ngày; Gareth ở hành lang chỉ "dừng lại nhìn cánh cửa".

## Bản 2 (SI v2 sau khi giới hạn so sánh) — LÀM LẠI
Bản nháp: `archive/run-2/doan-001-v2.md`.

**Tác giả:** "cắt mất quá nhiều phần giải thích rồi, vẫn thích Gareth bản cũ hơn."

### Agent đối chiếu bản 1 ↔ bản 2
- **Gareth bản 1** báo cáo bằng **thoại của chính ông** (5 câu thoại, mỗi câu một việc) và có đoạn nội tâm bằng **lời của một lính già**: "像只受惊的鹌鹑", "倒像是个坐在账台后面、冷眼盘算着每笔进出的冷血商人", "就算是泥人也该被逼出几分硬气来了". → Đó là giọng nhân vật, không phải giải thích thừa.
- **Gareth bản 2**: "低声汇报起来。情况烂得超出了想象。" rồi lời kể liệt kê thay ông → mất giọng; nội tâm chỉ còn câu hỏi chung chung "回光返照，还是…被逼成了个大人？".
- Agent đã **sửa quá tay** ở SI: cấm so sánh ngoài cảnh đánh nhau + "lời kể không kể lý lịch" đã giết luôn so sánh mang giọng nhân vật và phần giải thích thế giới mà thể loại cần.
- Vẫn còn lỗi cũ: "直往鼻孔里钻" (câu mở đầu), "像决堤的泥浆", "虚弱得像一根泡软的芦苇", "就像有一根通红的铁钎", "封地——黑石领" (—— trong lời kể), câu giải thích "生物电的反噬直接作用在了大脑毛细血管上".

### Làm tốt
- 小七 đúng câu khởi động, đúng 用户感官数据, bốn dấu hiệu, 置信度 78%. Không còn 系统 / 宿主 / 私生子.
- Lý luận về Pell gọn: "Pell不过是一只递毒碗的手。"
- Kết đúng: bát đặt lại vào vòng nước cũ.

### Đã sửa
- **SI v2:** so sánh thuộc về đầu và miệng nhân vật (lời của chính họ); người kể nói thẳng giọng/ánh nhìn/mùi. Phần nền (thế giới, giá cả, chuyện cũ) được hoan nghênh, đi qua phép tính của Leon hoặc lời nhân vật; báo cáo của cấp dưới là thoại từng câu của người đó.
- **Prompt bản 3:** Gareth báo cáo bằng thoại của mình; ở hành lang ông nhớ lại một chuyện cụ thể về Leon trước kia.

## Bản 3 (prompt bản 3, bỏ "ẩm mốc")
Bản nháp: `archive/run-2/doan-001-v3.md`.

**Tác giả:** vẫn có câu kiểu "…rất thực". Hỏi: do anchor hay do đầu vào nhiều token?

### Chẩn đoán
- **Không phải anchor:** anchor chỉ có 着实、严严实实、其实 — dùng bình thường.
- **Không phải do nhiều token:** đây là tin nhắn đầu của session mới, đầu vào chỉ SI + prompt (vài nghìn token). Hiện tượng trôi theo độ dài chỉ xuất hiện khi một session viết nhiều đoạn (lượt 1, đoạn 5).
- **Nguyên nhân gần nhất: từ vựng của SI lọt vào văn.** SI v2 tả cách viết bằng các tính từ phẩm chất — plain ×7, concrete ×4, straight ×4, exact ×3, flat ×2 — và cho sẵn "平板" làm ví dụ giọng. Writer "diễn" các phẩm chất đó thành chữ: "扎得极实", "实在账", "机械平直的声音", "硬邦邦". Cùng cơ chế với câu phủ định mồi ngược.
- Đã sửa: gỡ toàn bộ tính từ phẩm chất khỏi SI (còn 0), thay bằng mô tả thao tác (danh từ, động từ, con số; câu riêng; một từ trong thẻ thoại).

### Lỗi canon
- **Sai mùa:** "北境的春耕还要等到下个月底", "去年地里剩下的草根和冻坏的芜菁" → thành cuối đông/đầu xuân. Canon: **cuối thu, mùa đông sắp tới**. Lỗi phía Agent: prompt bản 1–3 không ghi mùa. Đã thêm vào prompt.

### Lỗi văn còn lại
- Người kể vẫn so sánh: "像两块粗砂纸在互相摩擦", "抖得像片风里的枯叶", "热络得像是刚从死神手里把主子抢回来一样".
- "钻进了鼻腔", "寒气直往骨头缝里钻"; "——黑石领" (—— trong lời kể); "一丝极淡的酸涩气味".

### Làm tốt — bản tốt nhất tới giờ
- **Gareth** báo cáo bằng 6 câu thoại của chính ông, giọng lính già; ở hành lang nhớ một chuyện cụ thể: năm 14 tuổi Leon khóc cả buổi chiều vì người hầu làm đổ nửa ly rượu mâm xôi đen lên áo nhung.
- Mở đầu bằng cơn đau đầu, không còn mở bằng mùi.
- Trà có "酸涩铁腥味" — manh mối tốt. Chip đúng câu khởi động, đúng bốn dấu hiệu, 78%.
- Kết có tính sổ kiểu Leon: không hắt trà, không đập bát vì "连一个完好的陶碗和木碗都是资产".
- Nghi phạm sau Pell: bá tước hoặc hai người anh.

## Bản 4 — CHỐT
Chính văn: `chapters/doan-001.md`. Prompt: `briefs/doan-001.md` (bản 4, thêm mùa).

**Tác giả:** tốt nhất trong mọi lần; kết đoạn (đặt bát lại đúng vòng nước) do prompt nên hơi vô nghĩa.

### Kết đoạn
Lỗi phía Agent: prompt bắt một hành động mà chưa cho nó lý do. **Gỡ ở đoạn 2:** đêm đó Leon đổ trà đi rồi đặt bát rỗng lại đúng vòng nước cũ — sáng ra Pell thấy bát rỗng nằm đúng chỗ, tin là thiếu gia đã uống. Hành động cuối đoạn 1 thành bước đầu của màn kịch với Pell.

### Ghi nhận
- Đúng mùa (秋收遭了霜冻, 收割月 vừa tròn, ba tháng sau tuyết phong núi).
- Gareth: 5 câu thoại báo cáo; nhớ chuyện 2 tháng trước — Leon gốc khóc ba ngày vì con chim ưng chết, **quất người hầu thân cận rách da** vì hai vết bùn trên ủng.
- Phép tính đúng: 140 người > 100 pound/ngày → không đủ 2 ngày; 3 người × 1 pound → hơn hai tháng.
- Còn sót: "眸底", "灰色的眸子", "平板死板的电子音", "——黑石领"? (không — lần này không có), so sánh của người kể ("像决了堤的泥石流", "弱得像张浸透了水的烂纸"), "冰冷、干瘪、没有任何起伏的声音…" (tả giọng chip). Mở đầu vẫn bằng mùi ("发馊的霉味呛醒").
- Chi tiết mới: Leon bị gọi là "年轻的男爵"; "雪一下就是整整半年"; Pell nói thảo dược nhờ "一个老妇人trong làng" hái; tiền thưởng "五十万信用点"; trang viên hiện có 3 người (Leon, Gareth, Pell).
