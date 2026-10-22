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
