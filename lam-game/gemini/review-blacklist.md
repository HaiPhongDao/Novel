# Danh sách lỗi riêng — lam-game (Agent soát khi review; KHÔNG đưa vào SI / prompt)

Soát cùng danh sách chung `chung/review-blacklist.md`. File này giữ lỗi gắn với thiết lập của truyện này — thêm dần qua review.

## Ranh giới Tác giả chốt (23/10) — soát mọi đoạn
- **Quốc gia / địa danh có thật:** 国、国内、国外、全国、国际、帝都, tên bất kỳ quốc gia hay thành phố có thật — kể cả trong hồi ức kiếp trước. Thế giới chỉ có 澜城 và các thành phố / tổ chức tự đặt.
- **Kim thủ chỉ:** hệ thống, giọng nói trong đầu, bảng 【】, vòng quay, phần thưởng từ trời, trí nhớ hoàn hảo, "金手指". MC nhớ kiếp trước ở mức người thường.
- **Game kiếp trước:** tên game, công ty, nhân vật game có thật; MC "nhớ lại một game kiếp trước rồi làm lại". MC chỉ dùng nguyên lý. (Truyện mẫu 全能游戏设计师 đi đúng đường này — Writer dễ bê sang.)
- **Bê thiết lập truyện mẫu:** 体验店、游戏设计大赛、D级/SSS级、手环、积分、抽奖、超级聚焦器、陈陌; "游戏设计师" như một nghề đã có sẵn (ở truyện này nghề chưa tồn tại).
- **Thuật ngữ trôi:** 全息 / VR头盔 / 游戏舱 thay cho 潜入舱; 登录 / 下线 thay cho 潜入 / 上浮; 出境 (nghĩa "xuất cảnh"). Hạng ngoài danh sách 见习、三级、二级、一级、特级.
- **Văn phong truyện mẫu cũ:** meme mạng dày (尼玛、狗带、战五渣、yy、辣鸡) — giọng tự giễu được, meme thì soát.

## Ghi nhận qua review
- (001 bản 1) Địa danh / nhãn hiệu có thật lọt qua chỗ trống prompt để ngỏ: "九寨沟", "微信", "国际会展中心". Cách chặn: prompt đặt sẵn tên cho mọi cảnh/app sẽ được nhắc (《云海栈道》, 短信).
- (001 bản 1) Lời kể bách khoa giảng thế giới giữa cảnh, không qua phản ứng của 许牧; thông tin xếp "第一条…第二条…第三条".
- (001 bản 1) Thoại "như anh đã biết": nhân vật giảng cho nhau điều cả hai đã rõ; MC đáp cụt, không hỏi lại.
- **Ngoại lệ của truyện này (Tác giả 23/10 muốn nhập vai):** câu tự hỏi, câu cảm thán ngắn của 许牧 đứng riêng một dòng trong lời kể là *giọng MC* → giữ. Chỉ bắt câu hỏi tu từ của người kể đứng ngoài (không thuộc ai) theo `chung/review-blacklist.md`.
- (001 bản 2) "国际汽车展会策划" — prompt liệt kê "展会策划" thì Writer gắn 国际 (hai bản liền). Prompt sau không đưa "展会".
- (001 bản 2) "二锅头" — nhãn rượu có gốc địa phương có thật; rượu gọi chung (白酒、啤酒).
- (001 bản 2) Lời kể mở bằng "在这个世界，…" rồi giảng luật — vẫn là giảng của người kể, kể cả khi SI đã sửa mục 3.
- (002–008, gemini-3.6-flash) Lời kể mở bằng "在这个世界，…" rồi giảng — lặp ở 004 dù SI v2.1. Đề xuất chỉnh SI (chờ Tác giả).
- (005 bản 1, 2) **Chỗ nhắn tin / trả tiền để trống thì Writer điền 微信 / 微信支付.** Prompt phải ghi sẵn "短信", "手机银行". Bản thử 001 (3.6) cũng lọt "微信支付".
- (004–007) "全真潜入" — thuật ngữ trôi; từ đúng: 潜入 / full-dive không có tên riêng trong chính văn.
- (006) Chữ hiện trong 《退潮》 ("【获得：…】") — trái thiết kế không giao diện; prompt ghi "trong 境 không có chữ hay bảng nào hiện lên".
- (005 bản 1) Lời kể vào đầu 姜禾 khi prompt chỉ cho hiện qua lời và việc. Cách giữ: đặt điểm nhìn trong câu sự việc + cho cô một hành động kết phản ứng.
- (007–008) Câu đúc kết sau mỗi nhịp: "这就是游戏机制的力量…", "游戏策划的核心技巧之一…".
- (005 bản 1, 2) "一字一顿" + lời khích kiểu "你就打算…" khi MC thuyết phục — nhịp kịch lặp; soát và cân nhắc khi biên tập.
- (005 bản 2) "全潜" — thuật ngữ trôi như "全真潜入".
