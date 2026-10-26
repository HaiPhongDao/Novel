# Giọng MC + đầu óc người hiện đại — đo, thử, và chỗ đang thiếu (26/10)

Tác giả: *"thể loại này còn có cả giọng nói của tác giả mượn lời MC để giải thích, thể hiện sự ưu việt của người
xuyên việt, người hiện đại… MC đang lu mờ quá, 5 đoạn rồi vẫn chưa nổi bật được tính cách."*

## Đo trước khi sửa: đúng là 0

Đếm trên 5 đoạn đang dùng (003-H … 007-C), bằng regex:

| dấu hiệu | 003-H | 004-F | 005-C | 006-C | 007-C |
|---|---|---|---|---|---|
| chữ "kiếp trước / 前世 / 现代" | 0 | 0 | 0 | 0 | 0 |
| người kể mượn giọng hắn châm một câu (`开玩笑`/`狗屁`) | 0 | 0 | 0 | 0 | 0 |
| quy đổi ra đơn vị đo (`换算`/`折合`/`人均`) | 1 | 1 | 0 | 1 | 2 |
| nội tâm tự chửi | 1 | 0 | 1 | 0 | 1 |

Nguyên nhân: SI v9 có **nguyên tắc** ("the storyteller is on the protagonist's side", neo `开玩笑，那能让你们抢了
经验吗？`, neo `罗伯森前世见过的高楼大厦`) nhưng **không có hạn mức đếm được** — và theo đúng luật đã ghi trong
`chung/kinh-nghiem.md`, sự hiện diện của một giọng mà chỉ mô tả suông thì model bỏ qua sạch.

## Thử hai đời SI trên cùng brief (đoạn 003)

- **SI v10** (`gemini/system-instruction-v10.md`, 16.355 ký tự): thêm khối `PART 1B — THE HEAD FROM ANOTHER
  WORLD`, 5 dòng, mỗi dòng một hạn mức/đoạn (quy đổi thành đại lượng kiếp trước · một câu châm riêng dòng ·
  ưu thế phải nhỏ và địa phương · từ hiện đại chỉ trong đầu và miệng hắn · ai nói không có số thì hắn đáp bằng số).
- **SI v11** (16.836 ký tự): thêm 2 dòng nữa — câu châm đặt **ngay sau một quyết định** của hắn, và "sổ trong
  đầu" quy mọi lựa chọn ra ngày.

| bản | SI | 字 | 字/câu | lượt · 字/lượt | 前世 | câu châm | so sánh | cham |
|---|---|---|---|---|---|---|---|---|
| 003-H | v9 | 3.178 | 24,6 | 37 · 22,1 | 0 | 0 | 0 | 58 |
| 003-I | v10 | 2.378 | 22,4 | 33 · 23,2 | **1** | 0 | 1 | 58 |
| 003-J | v11 | 1.995 | 22,4 | 34 · 20,4 | 0 | 0 | 3 | **64** |

**Kết quả phải đọc bằng văn, không bằng regex.** 003-I có đúng một câu đúng kiểu cần:
`在他前世的账本里，重体力劳作在极寒天气下的热量消耗是静卧者的三倍以上，平均分配口粮等于让所有人一起慢性自杀。`
— quy vấn đề ra đại lượng, có số, không giảng khái niệm. 003-J **không** có chữ 前世 nhưng lại có cái đầu hiện đại
làm việc mạnh hơn: hắn đổi cách chia khẩu phần thành **suất theo ca** (`每人每天三斤干麦` cho 41 người vào rừng,
`半碗稀粥` cho 450 người ở lại) và mở một cơ chế **thay ca** —
`吃干饭的去流汗，喝稀汤的等死…想吃饱饭的，明天就去替那四十一个人的班`.
Câu đó là tính cách: hắn không thuyết phục bằng đạo lý, hắn mở một cửa và để người ta tự chọn.

⇒ Hai lần chạy, hai kiểu trúng khác nhau: hạn mức trong SI **có** ăn, nhưng chỉ ăn 1–2 chỗ/đoạn và không ổn định
(1 → 0 hit giữa hai lần). Muốn chắc thì phải **đặt chỗ** trong brief nữa, đúng luật "sửa cả ba tầng".

## Chỗ còn thiếu: tính cách chưa được định nghĩa

Bible hiện chỉ có: *giỏi tính, không giỏi nói trước đám đông, nói xong tự chửi mình trong đầu, tự gọi mình là
`Adrian 少爷` khi đang cay*. Ba dòng đó không đủ để Writer dựng một con người — nên 5 đoạn qua hắn chỉ **giải
quyết việc**, không có gì để người đọc nhớ. Ba hướng định nghĩa, mỗi hướng là một cách hắn khác người (Tác giả
chọn một, Agent ghi vào `bible/characters.md` rồi chạy lại):

**A. Kẻ mở sổ (khuyến nghị)** — hắn quy mọi thứ ra ngày công và suất ăn, kể cả lòng trung thành; hắn không nói
đạo lý, hắn nói giá. Tật: khi ai nói một câu không có số, hắn hỏi lại bằng số; khi bị gọi là "thiếu gia" mà
không có quyền, hắn cười và tự nhủ một câu chua. Cái hắn sợ: bị cha đem ra so với anh trai.
**B. Kẻ đi sửa đồ** — hắn không giỏi đánh, giỏi làm cho thứ hư chạy lại (cối xay, ống dẫn nước, chuồng ngựa,
dây cương); niềm vui duy nhất của hắn là một cái máy chạy được. Tật: hắn sờ vào mọi thứ đang hỏng trước khi
chào người.
**C. Kẻ đi thuê người** — hắn tin vào hợp đồng hơn tin vào lời thề; mua người bằng thứ người ta muốn (đất, tha
nợ, một chỗ trong sổ), và ghi nhớ ai nợ mình. Tật: hắn luôn hỏi "anh muốn gì" trước khi hỏi "anh biết gì".

Cả ba đều là "người hiện đại hơn người bản địa" nhưng ở ba nghề khác nhau: **kế toán** · **kỹ thuật** ·
**quản trị**. Chọn cái nào thì SI v10/v11 phải viết lại quanh cái đó (hiện khối PART 1B đang trung tính, chưa
neo vào nghề nào).
