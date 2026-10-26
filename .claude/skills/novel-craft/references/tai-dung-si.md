# Tái dùng một SI đã duyệt cho truyện khác lane

Dùng khi Tác giả gửi link SI của một truyện cũ ("lấy SI của link này") và bảo chạy truyện mới khác thể loại.
Mục tiêu: giữ nguyên phần đã được đo là tốt, chỉ đổi phần **nghĩa** (canon, bàn tay vàng), rồi đo ngay ba bốn bản
đầu để chọn hình dạng prompt.

## 0. Đọc SI từ đĩa, không từ raw URL

- Link `.../blob/<branch>/<truyen>/gemini/si-dan-gemini.txt` là để **định vị commit**. `raw.githubusercontent.com`
  trả `404: Not Found` trong khi file nằm sẵn trong bản clone là chuyện thường (branch của session khác, đời file
  khác). Trước khi kết luận "không có file": `ls <truyen>/gemini/` và đọc file mới nhất trên đĩa.
- Chỉ khi đĩa rỗng mới `git fetch -q --all` rồi `git ls-tree -r --name-only origin/<branch> | grep -i si-dan`.
- **Đọc file chưa đủ — phải xác định đời nào rồi nói lại với Tác giả.** Mỗi truyện giữ cả bộ `si-dan-gemini.txt`
  + `-v1…-v12`, và bản trên đĩa không chắc là bản trong link họ đang nhìn. Nhận diện bằng một dấu hiệu văn bản
  (quy ước tên: `阿德里安` = đời cũ dùng tên Hán, `Adrian` = đời mới dùng tên Latin; hoặc một câu luật chỉ đời đó
  có), rồi trả lời bằng **tên đời + 3–4 khác biệt** so với bản họ dán/link. Dùng im lặng một đời khác thì câu
  tiếp theo là "có phải đang là SI này không" và cả lượt chạy thành nghi vấn.

## 1. Giữ gì, đổi gì

| phần | xử lý |
|---|---|
| ROLE | đổi thể loại + register (một câu), giữ tinh thần "nhịp nhanh, có giọng" |
| FIXED CONVENTIONS 1 (ngôn ngữ) | giữ |
| FIXED CONVENTIONS 2 (tên) | đổi tên người Latin + chức tước/địa danh Hán sang canon mới, **kèm một dòng in bảng mẫu** |
| FIXED CONVENTIONS 3 (dấu câu) | giữ |
| PART 1 (7 anchor) | giữ **nguyên văn** — anchor dạy nhịp, không dạy canon; tên trong anchor thuộc sách mẫu |
| PART 2 (bullet từng đoạn) | giữ, chỉ đổi các bullet nói về bảng cho khớp nghĩa mới |
| PART 3 (output) | giữ |
| PART 4 (bàn tay vàng) | **đổi nghĩa, không xoá** |
| LENGTH / BANS | giữ nguyên 5 dòng BANS |

Bỏ PART 4 vì "truyện mới không có hệ thống" là quyết định của Agent. Tác giả nói "lấy SI này" thường là lấy
**cả cỗ máy cày cuốc**; họ sẽ đòi lại bằng một câu ("thêm hệ thống điểm kinh nghiệm … để MC cày cuốc") và mọi bản
đã chạy phải bỏ.

## 2. Đổi nghĩa bảng sang lane mới (骑砍 quân → nông trại)

Giữ đúng hình dạng entry của bản gốc — mỗi entry một dòng, trong 【】, bậc trước, tiến độ `hiện/tổng`, khối ≤6
dòng, bảng không nói không đùa — chỉ đổi **đơn vị** đo:

| dòng gốc | dòng mới |
|---|---|
| `【宿主：X（3阶青铜骑士 481/500）（男爵次子）】` | `【宿主：Ronan（1阶 佃农 40/300）（灰柳村佃户）】` |
| `【技能：精通.骑士八技（494/500）】` | `【技能：育苗（12/100）· 沤肥（6/100）】` |
| `【士兵：一阶.500 …（0/100）】` | `【村民：一阶.3 …（60/100）】` |
| `【士气：69/100】【人数上限：500】` | giữ nguyên tên dòng, `人数上限` theo năng lực trang trại (đất, kho, mái) |
| (không có) | `【经验：40】` — số **chưa tiêu**, in cả lúc kiếm và lúc tiêu |

Định giá để vòng cày cuốc đóng kín (chốt trong `bible/glossary.md` trước đoạn 001):

- Kiếm: một ngày lao động 5–8 · một đêm trắng 8–12 · cứu một người 20 · một con sói/kẻ cướp 9.
- Tiêu: đào tạo `一阶 村民` = **100 经验 + ba ngày lương**; `二阶` = **300 经验**, làm bằng ba người.
- `宿主` là tổng 经验 đã kiếm (không giảm); `经验` là số chưa tiêu. Hai con số phải khớp phép tính trong đoạn.

## 3. Bốn bản thử đầu — dùng để chọn prompt, không để chọn câu chữ

| bản | SI | brief | 字 | 字/câu | lượt · 字/lượt | tật |
|---|---|---|---|---|---|---|
| a | v1, PART 4 = kiến thức (không bảng) | chi tiết, 7 cảnh đánh số | 2.170 | 19,5 | 19 · 18,7 | 1 phủ định, 1 so sánh, 4 đoạn giảng |
| b | v1b, sửa 1 bullet | như a | 1.695 | 19,7 | 17 · 20,9 | 0 phủ định, 1 so sánh |
| c | v2, có bảng | ngắn ~250 từ, đích 1.500–1.800 | 1.244 | 16,4 | 15 · 9,7 | hụt 17%, bảng bị giảng |
| d | v2.1 | ngắn ~330 từ, đích 1.900 | 2.138 | 21,3 | 15 · 25,9 | 2 phủ định, 1 câu giải thích bảng |
| e | v2.1 | ngắn ~200 từ (bỏ dòng đếm lượt thoại) | 1.868 | 20,1 | 16 · 17,5 | bảng bị giảng 3 câu, 1 câu giải thích 圣水 |

Mốc so là chương 1 đã được Tác giả khen của truyện khác trong repo (1.543 字 · 23,6 字/câu · 22,6 字/lượt).

Chọn bản theo thứ tự: (1) có đủ khối bảng **đúng nguyên dạng từng dòng**; (2) `字/câu` và `字/lượt` gần mốc đã
duyệt; (3) đọc ba đoạn mở/giữa/kết, không có câu người kể giảng cơ chế.

Ladder này đọc ra một đánh đổi: rút prompt xuống ~200 từ thì **độ dài và nhịp câu vào cửa sổ** (e: 1.868 字,
20,1 字/câu) nhưng **lượt thoại mỏng đi** (d 25,9 → e 17,5 字/lượt) — vì dòng "phần lớn là lời kể, khoảng 12–16
lượt thoại" chính là thứ giữ lượt dài. Tác giả đòi bỏ dòng đó thì bỏ, ghi cái giá vào review, và khi cần thoại
dày thì mở phạm vi cảnh hoặc thêm người có mặt — đừng cài lại dòng đếm.

## 4. Bẫy

- **Prompt ngắn thì Writer tự đặt tuổi và tự đổi người tự xưng.** Brief ~200 từ bỏ dòng thân phận là ra `十岁的
  Piet` (canon 7) và **MC tự xưng `小的` với 神父** — vai tá điền nói với tu sĩ phải là `我`. Hai lỗi này mọi script
  đếm đều bỏ qua, nên sau mỗi lần chạy grep `岁|小的|大人|神父大人` và đối chiếu `bible/characters/` trước khi báo
  ĐẠT; sửa tay một chữ thì ghi rõ trong review là **Agent sửa**, giữ bản Writer nguyên văn ở `archive/`.
- **Cắt prompt thì giữ hai dòng chặn quanh khối bảng** (câu sau khối chỉ nói con số đáng gì; "sau khối bảng là
  một việc anh làm tiếp theo"). Bản rút mất hai dòng đó giảng lại bảng bằng ba câu liền, đúng tật mà SI vừa sửa.
- **Register trượt ngay ở bản có bảng**: `神父大人` xuất hiện dù glossary đã chốt `神父`; sau mỗi lần chạy grep
  `神父大人|大人|老爷|小的` và đếm, đừng tin glossary.
- **Câu "comparison to his old life … at most once" bị dùng thành nghề kiếp trước sai canon** (`前世敲键盘` khi
  bible ghi nghề ngoài đồng): nghề cũ thuộc bible, brief chỉ có một dòng trơn `X là người xuyên việt.`
- **Capture đôi khi dính ký tự lạ** (`不一整口生铁大锅…`): đọc câu cuối + hai câu giữa trước khi đo, bản hỏng thì bỏ.
- **Khối nối tiếp chỉ dán đuôi của bản đã duyệt thuộc chính truyện đó** — đuôi của truyện khác mang canon khác.
- **Đích độ dài trong brief là mốc trượt, không phải trần**: đích 1.500–1.800 ra 1.244, đích 1.900 ra 2.138. Ghi
  đích thấp hơn mục tiêu thật ~15–20% hoặc chép nguyên cửa sổ Tác giả chấp nhận, rồi đọc số chứ đừng tin lời.
