# Review — Đoạn 001

## Bản 2 (SI v2 + prompt v2, session S2) — `chapters/doan-001.md`

**Kết luận: ĐẠT** (Tác giả 23/10: "vẫn chưa đúng những gì tôi muốn lắm, đặc biệt đoạn đầu. Nhưng tạm ổn rồi"). ~2,550 chữ Hán.

### Canon & nhất quán
- ✅ Mọi con số đúng: 1,500元 trước 九月十号; 2,316元 → 816元 / 27 ngày ≈ 30元 một ngày (phép tính đúng); 九月三十号, 46小时; 14 hồ sơ; 58/60, 真实度 21/40; 860万人次; 20元 nửa giờ; sau khi trả còn 2,296元.
- ✅ Lời phê nguyên văn; kiếp trước đủ ba điều (nghề, chín năm, buổi họp).
- ❌ "国际汽车展会策划" — lại có 国际 (bản 1 cũng vậy, đều từ chữ "展会策划" trong prompt). Không viết lại vì lỗi một chữ; gói bàn giao không nhắc tới, các prompt sau không liệt kê "展会".
- ⚠️ "二锅头" — tên rượu có gốc địa phương có thật. Ghi blacklist.
- ⚠️ Writer thêm: chủ nhà 王阿姨; 许牧 gốc xem 《千灯巷》 "四五回"; "两千多盏红灯笼"; 许牧 gốc đêm qua uống bia rẻ đọc thư từ chối. Nhận làm canon (không ảnh hưởng arc).

### Cốt truyện
- ✅ Đủ diễn biến: tỉnh dậy → điện thoại từng món → bảng điểm → tin 《千灯巷》 → trang tuyển dụng → "策划" ra tổ chức sự kiện → bật cười → 深蓝 → 《千灯巷》.
- ✅ Gieo được "复游率" — 许牧 buột miệng, 老周 hỏi lại "复啥？". Chưa nằm trong kế hoạch nhưng hợp tuyến T07 (để dùng ở đoạn 003).

### Văn phong
- ✅ Nhập vai khá hơn bản 1: cơ thể đi trước ký ức ("掌心连常年握鼠标磨出来的薄茧都没有"); tính sổ trong đầu ("前提是别生病，别买水，别出门坐公共交通。"); "得，连吃饭的工具都快被收走了。"
- ✅ Thoại đời thường, có đối đáp: 许牧 đùa lảng ("大厂嘛，流程长…正互相考察呢"), 老周 bóc ("得了吧你，跟我还打马虎眼。"), 许牧 hỏi lại chuyện quán, 老周 than 《云海栈道》 bằng chuyện của ông.
- ⚠️ Đoạn đầu (Tác giả chưa ưng): khoảnh khắc xuyên không vẫn kể tóm tắt ("上一世，他当了九年游戏策划…高层一句话说砍就砍"), và vẫn có hai đoạn lời kể giảng thế giới ("在这个世界，大约一年零十个月前…", "在这个世界，评测一个境全靠四个指标…"). Đó là lỗi giảng của người kể, không phải dòng nghĩ của 许牧.
- ⚠️ "鼻腔里钻进来一股…怪味" — mẫu mùi "chui vào mũi" của blacklist chung.
- ✅ Dừng giữa mạch: "躺平别乱动啊！半小时一到自动上浮——".

## Bản thử API gemini-3.6-flash (SI v2.1 + prompt v2, session riêng, 23/10) — `archive/doan-001-thu-api-gemini-3.6-flash-20261023-0442.md`

Tác giả muốn thử gemini-3.8-flash, nhưng lúc đó 3.8 và 3.7 trả 503 "quá tải" rồi 502 liên tục; mã `gemini-3.5-flash` thì Google trả về modelVersion gemini-3.6-flash. Tác giả chọn chạy 3.6 (gọi streaming; kiểu gọi thường bị 502 qua proxy). 2,320 chữ Hán, thinking high.

**Kết luận: nhỉnh hơn bản thử 3-flash, nhưng có lỗi cứng — không thay bản 2.**
- ✅ Đủ con số, lời phê nguyên văn; tính sổ đúng (816 / 27 ngày ≈ hơn 30 đồng/ngày); kiếp trước đúng ba điều (+ ba năm dự án, khớp brief).
- ✅ 许牧 hỏi lại sao quán vắng; 老周 than đúng giọng (tiền, điện, 《云海栈道》 tuần trước); giọng MC nhập vai tốt ("十四连败，达成成就", "同行全灭，还是降维打击？").
- ✅ Dừng đúng chỗ: nắp khoang số 3 khép, 老周 nói vọng vào.
- ❌ "【微信支付收款，20元。】" — nhãn hiệu có thật (lỗi bản 1 tái phát) và bảng 【】; tin nhắn/thông báo đều đóng trong 【】.
- ❌ Rác token: "四十 writ五岁"; lỗi chữ "评审眼眼里".
- ⚠️ Lời kể giảng thế giới khi MC bật cười ("这个世界在一年十个月前发明了民用潜入舱…") — vẫn cùng dạng lỗi "在这个世界".
- ⚠️ 老周 tự nói ra luận điểm của truyện ("不好看也不好玩"), lấy mất phát hiện của MC.
- ⚠️ Sai cảnh: "网吧里昏暗的光线"; 老周 nói "系统会自动弹出来" thay vì 上浮.

## Bản thử API (SI v2.1 + prompt v2, session riêng, 23/10) — `archive/doan-001-thu-api-20261023-0418.md`

Chạy thử theo yêu cầu Tác giả để xem SI v2.1 qua Gemini API (gemini-3-flash-preview, thinking high, chỉ gửi prompt). Không thay bản 2 đã chốt. 1,975 chữ Hán.

**Kết luận: không hơn bản 2 — giữ bản 2.**
- ✅ Đủ con số và lời phê nguyên văn; kiếp trước đúng ba điều; không quốc gia, không tên game có thật; tính sổ tiền/ngày đúng (816 → khoảng 30 ngày).
- ❌ Lời kể giảng thế giới hai lần bằng "在这个世界，…" (算力, 潜入舱) — lỗi bản 2 vẫn còn dưới SI v2.1.
- ❌ Kết bằng 【载入中……】 — bảng 【】 (ranh giới kim thủ chỉ) và vượt quá chỗ dừng.
- ⚠️ Tin trên điện thoại lại xếp "第一条…第二条…" (lỗi bản 1).
- ⚠️ Thuật ngữ trôi: "全潜入技术".
- ⚠️ Cảnh quán: 许牧 không hỏi sao quán vắng, 老周 tự than; lời kể khen giá "简直是慈善" nhưng 老周 lại nói quán "给有钱人消遣" — tự mâu thuẫn.
- ⚠️ Mảng ký ức về những đêm làm 《晾衣街》 chỉ có một câu.

## Bản 1 — `archive/doan-001-v1.md` (prompt `archive/doan-001-brief-v1.md`)

**VIẾT LẠI** (Tác giả: thoại chưa tự nhiên, thiếu cảm giác ở trong đầu nhân vật). Chi tiết: commit b276e22 — lời kể đứng ngoài, thông tin xếp "第一条…第二条…", thoại "như anh đã biết", MC đáp cụt; lỗi canon 九寨沟, 微信, 国际会展中心. Nguyên nhân phía Agent: anchor mục 3 của SI v1 là đoạn đọc hợp đồng; PART 2 "cảm xúc chỉ qua tay chân"; anchor thoại trịnh trọng; prompt v1 xếp dữ kiện liền nhau.
