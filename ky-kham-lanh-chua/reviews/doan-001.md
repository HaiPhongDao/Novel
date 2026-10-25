# Đoạn 001 — review bản A (máy) → B (sửa tật) → C (sửa thoại)

- Brief: `briefs/doan-001.md` · SI: `gemini/si-dan-gemini.txt` v2 · chạy `--new`, 125s
- Bản A (nguyên): `chapters/doan-001-a.md` — 2.786 字
- Bản B (13 chỗ sửa tay + cắt 139 字): `chapters/doan-001-b.md` — 2.647 字
- Thinking: `archive/thinking-001a.md`

## 1. Bảng số

| chỉ số | mẫu (886 ch) | mẫu ch1 | A | B |
|---|---|---|---|---|
| 字 (tham khảo, không phải tiêu chí) | 2.122 (trung vị) | 2.273 | 2.786 | 2.647 |
| chữ / câu | 23,9 | 28,4 | 20,0 | **21,3** |
| lượt thoại | 20 | 14 | 47 | 47 |
| chữ / lượt | 22,4 | 29,6 | 20,2 | 19,9 |
| phủ định lặp | 0,3/ch | 0 | 1 | **0** |
| so sánh người kể | ~1/ch | 0 | **3** | **0** |
| nhãn ngữ điệu | ~0 | 0 | **3** | **0** |
| `实` | 0,3/ch | 0 | 0 | 0 |
| tự gọi 少爷 | 1,35/ch | 0 | 1 | 1 |
| dòng bảng `【】` | 0,06/ch | 6 | 2 khối (8 dòng) | 2 khối (8 dòng) |

## 2. Sáu chỗ phải sửa tay ở bản A (và đã sửa ở bản B)

| loại | bản A | bản B |
|---|---|---|
| so sánh người kể | `所有人都在冷风里瑟瑟发抖，像一窝挤在烂泥里的受惊鹌鹑` | cắt vế so sánh, giữ `呼出的白气聚成一片薄雾` |
| so sánh người kể | `身子晃荡得像风里的枯草` | `站都站不直` |
| so sánh người kể | `仿佛屋子里只是飞进了一只无关紧要的麻雀` | `一根手指压在铁脊隘口的位置上` |
| so sánh người kể | `卡尔的声音冷得像结了冰渣` | `卡尔报完，抬起眼看过来` |
| nhãn ngữ điệu | `阿德里安平静地说道` (×1), `语气没有半点起伏` (×1), `冷冷地开口…声音像深冬磨石般干涩` (×1) | bỏ nhãn, giữ động tác (`手里的银刀没有放下`) |
| phủ định lặp | câu mặc cả `语气没有半点起伏，“行就放人，不行…` | bỏ vế `没有半点起伏` |

Ba chỗ nữa **`soat_van.py` không bắt** (đã grep tay, ghi thành KN30): `目光如鹰隼般锐利` → bỏ vế so sánh;
`四指粗糙如铁钩` → `指节粗大`; `阿德里安平静地命令道` → `命令道`. Tổng cộng 13 chỗ.

Nhận xét: **hai tật này sống sót qua hai lần chạy liên tiếp** (test 01 sạch, ch1 bẩn) — tức chúng là
biến thiên của lần chạy chứ không phải lỗi SI. Sửa tay 10 chỗ rẻ hơn một vòng SI mới.

## 3. Đọc bằng lời (bản B)

**Mở** — `木桩被铁锤重重砸进冻土里` → `阿德里安睁开了眼`
- Vào bằng tiếng, rồi tới thân thể (`右臂缠着的粗麻布渗出两点暗红`), rồi mới tới nhà và sân — đúng nhịp mở
  chậm Tác giả đã yêu cầu, khác hẳn bản test 01 (mở bằng lời báo tin).
- Ai gặp nguy trong 300 字 đầu: 科尔, thòng lọng đã quàng, và chính MC (bị tống đi).
- Hạn chót: mặt trời mọc (treo 12 người), trưa (rời trang viên), 30 ngày (địch tới).

**Giữa** — cuộc mặc cả với 格里
- Có chất liệu xã hội ngoài việc: đám cưới của anh trai, lời mời uống rượu, người nông nô đang sốt — đúng thứ
  Author đòi ở cảnh hai người gặp nhau.
- Cái giá rõ: 30 金币 → 24 → còn 6. `24` và `6` được nói ra thành câu riêng, không nằm lẫn trong đoạn.
- Điểm yếu: 格里 giải thích luật hai lần (潜逃 + 双倍罚金); bản B đã nén một lần.

**Kết** — `拿这六枚金币去镇上的铁匠铺，全买伐木用的重刃铁斧。`
- Kết bằng quyết định + số (24 rìu, hoặc 0,72 ngày ăn), có người hỏi lại (`不买粮？`) — đúng kiểu hook.
- Chưa đủ mạnh: câu cuối là lý lẽ của MC, không phải một cái giá mới hay một kẻ địch mới. Cân nhắc cho ch2
  mở bằng tin 铁脊要塞 đã có người bỏ đi, hoặc bằng chính 24 cái rìu được rèn xong.

**Giọng:** có `他阿德里安少爷在家族账本上的价值，到此算是彻底结清了。` (tự gọi 少爷, 1 lần), có
`天崩开局也不过如此。` (câu trần trong đầu, không ngoặc) — hai thứ bản test 01 thiếu hoàn toàn.

## 4. Ba việc phải chốt trước chương 2

1. **Độ dài**: hai lần chạy liền ra +27% và +21% so với trần SI (2.200). Luật trong SI không kéo được con số
   này ⇒ **ghi số 字 vào brief** ("khoảng 2.100 字, không quá 2.300") mới là chỗ sửa.
2. **Lượt thoại 47** (mẫu 20) vì chương có ba cảnh thoại liền. Brief đã ghi dòng tỷ lệ nhưng Writer vẫn chẻ
   lời; lần sau ghi thẳng "ba cảnh, cảnh giữa phần lớn là lời kể" hoặc gộp cảnh cha vào cảnh sân.
3. **Canon mới do Writer tự đặt, cần chốt**: 科尔 là "瘦弱老头" (bible ghi 28 tuổi) → chốt **50 tuổi**; tốc độ
   exp "挥剑两万次 ≈ 19 点" → chốt tỷ giá (đề xuất **1 点 ≈ 400 次挥剑**, tức 19 点 ≈ 7.600 次, không phải
   2 万); 卡尔 tự xưng 老仆 của mẹ → thêm vào bible.

## 5. Verdict

**CẦN TÁC GIẢ ĐỌC.** Bản B sạch tật đo được, đúng nhịp mở, có cái giá và có hook quyết định; chưa duyệt thì
chưa viết chương 2. Ba con số còn lệch mẫu: 字 +21%, lượt thoại gấp đôi, câu 21,3 so với 23,9.

## 6. Vòng 2 — Tác giả bắt: "MC nói chuyện chưa đầy đủ, giao tiếp còn trống không" (bản C)

Chẩn đoán trên bản B: 47 lượt thoại nhưng **19,9 字/lượt** (mẫu 22,4), và lượt của MC thì nêu việc mà
không nêu **vì sao / cho ai / bao nhiêu**. Ba chỗ nặng nhất:

| bản B | bản C |
|---|---|
| `“开个价吧。”` (3 字, không nói tiền ở đâu ra, không nói cái gì đang bị bán) | `“开个价。”阿德里安打断了他的推脱，“钱从我那份里出，走我私账。父亲的账本上不必有这一笔。”` |
| `“两枚金币一个。”…“行就放人，不行我现在就去父亲的房里…”` (không nói vì sao 2 là giá đúng) | MC dẫn lại chính luật 格里 vừa nói: `逃奴赎买是双倍罚金。一个农奴折一枚金币，翻倍就是两枚，十二个二十四枚。这个价你按律收得，我按律付得。` |
| 格里 mời uống rượu mừng → `阿德里安没理会他的试探` (**im lặng = trống không**) | `“喜酒就不喝了。”…“我这边五百张嘴，走到铁脊要塞要七天，先得把这七天喂饱。”` rồi biến lời mời thành cuộc mặc cả: 格里 khai ra **2.000 斤 thóc mốc không có trong sổ**, đổi lấy một câu nói đỡ trước mặt nam tước |

Ba chỗ khác đã làm đầy: lệnh cho 科尔 (`起来。回队伍里去，站第一排。让后面的人看清楚…`), mặc cả với cha
(`后山旧仓那批陈麦…到冬天按半价折钱还进公账` / `冬天之前还不上呢？` / `那今年就不用给我留门了`), và kết
chương bằng kế hoạch có số (`二十四把，五百个人。怎么分？` → `路上砍。七天路，每天砍一批，削尖一头。`).

Số sau khi sửa: **3.108 字 · 50 lượt · 33,0 字/lượt** (B: 2.647 · 47 · 19,9; mẫu: 2.122 · 20 · 22,4).
Tức mỗi lượt đã dày gấp rưỡi, nhưng chương dài thêm 461 字.

**Luật đơn vị (Tác giả chốt 26/10): đây là một ĐOẠN, không phải chương.** Chương tách ở khâu biên tập sau.
Đoạn dài bao nhiêu cũng được, miễn không trượt ngữ cảnh và văn phong ⇒ **3.108 字 không phải lỗi**, và số 字
bị bỏ khỏi bảng tiêu chí từ đây. Cái còn phải theo dõi là lượt thoại (50 so với 20 của mẫu) — nhưng đó là
tính chất của đoạn có ba cảnh, không phải tật.

## 7. Vòng 3 — Tác giả đọc bản C: "MC vẫn là 起来 thay vì 起来吧/站起来吧"

Vòng 2 mới sửa **nội dung** lượt thoại, chưa sửa **hình dạng lời nói**. Lệnh thoại của MC vẫn là động từ
trần: `起来。` `站第一排。` `开个价。` `不买粮。` — đó là chỉ dẫn sân khấu, không phải câu nói. Tiếng Trung
nói ra cần trợ từ và người nhận (吧 / 去 / 着 / 给我 + 你).

| bản C | bản D |
|---|---|
| `“起来。”…“回队伍里去，站第一排。让后面的人看清楚…”` | `“起来吧。”…“回队伍里去，站到第一排去。让后面的人都看清楚…”` |
| `“开个价。”` | `“你开个价吧。”` |
| `“那就写清楚。”…“写进我的名册。”` | `“那就写清楚吧。”…“写进我的名册里去。”` |
| `“不买粮。”` | `“粮不买了。”` |
| `“不分。”…“路上砍。”` | `“不用分。”…“路上砍。”` |
| `“行。”…“麦子今天就卸到车上，你自己派人去。”` | `“行啊。”…“麦子今天就卸到车上去，你派个人跟着。”` |
| `“拿这六枚金币去镇上的铁匠铺，全买…”` | `“把这六枚金币拿去镇上的铁匠铺，全换成…”` |
| `“你要是不认这个账，我现在就去书房…”` | `“你要是连这个账都不认，那咱们就去书房…”` |
| `“科尔年纪大了，腿脚不利索…”` (biện hộ bằng tuổi tác — không phải lý lẽ) | `“科尔替我母亲养了八年马。他要是想跑，八年前就跑了。”` |

Số bản D: **3.155 字 · 50 lượt · 34,0 字/lượt · 0 tật** (tool + grep tay). Lượt dưới 12 chữ còn đúng ba, và
cả ba đều là câu đủ nghĩa: `“二少爷……”` (bị cắt lời), `“那今年就不用给我留门了。”`, `“木矛挡不住兽人。”`.

Bài học (đã vào SI v5 + KN31): **nội dung một lượt và hình dạng một lượt là hai lỗi khác nhau.** Thêm lý do và
con số vào lượt thoại không làm nó thôi giống khẩu lệnh; phải thêm trợ từ và người nhận.
