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

## 8. Vòng 4 — Writer tự viết lại với SI v5 (bản E), không sửa tay

Tác giả: "đó là bạn tự sửa? không phải Writer viết lại sao? test với prompt cho writer xem." → chạy lại
`--new` với **SI v5 + đúng brief cũ** (không thêm một dòng nào vào prompt), 189s, 1.963 字.

**Lệnh thoại do Writer tự ra, không có bàn tay Agent:**

| tình huống | bản E (Writer) | bản A/B (trước khi thêm luật) |
|---|---|---|
| cứu người | `“把人给我放下来吧。”阿德里安说道。` | `“开个价吧。”` rồi im |
| mặc cả | `“你开个价吧。”…“两个金币。”…“他们要是冻死在梁上，你连两个铜板都拿不到。”` | `“两枚金币一个。”` (nêu giá, không nêu lý do) |
| 格里 mời rượu mừng | `“我不爱喝甜酒，还是留给大哥慢慢享用吧。”` | `阿德里安没理会他的试探` (im lặng) |
| lệnh mua rìu | `“拿这六个金币去镇上的铁匠铺，给我买二十四把伐木斧回来。”` | `“不买粮。”` + `“拿这六枚金币去…全买…”` |
| nông nô tự xưng | `“小的没跑……小的只是去找掉进沟里的马草……”科尔悬在半空嘶声说道。` | không có lượt của 科尔 |
| câu chốt | `“斧子不能当饭吃，但能砍树，还能砍人。”` | `“买粮只能多撑半天…还能砍下兽人的脖子。”` |

Số: **1.963 字 · 32 lượt · 24,0 字/lượt** (mẫu 20 · 22,4; bản D sửa tay 50 · 34,0). Lượt thoại của bản E
**gần mẫu hơn bản sửa tay** — tức luật trong SI hiệu quả hơn việc Agent kéo dài từng câu.

Tật còn lại: **1** — `五百个农奴像木桩一样戳在寒风里` (so sánh của người kể). `soat_van` báo 0 nhưng grep tay
bắt được; ngoài ra 0 phủ định, 0 nhãn, 0 `实`.

Hai khác biệt so với bản D — **cả hai đều do brief, không do SI**:
1. E không có cuộc mặc cả thóc mốc (2.000 斤) với 格里, vì brief không có beat đó (Agent tự thêm khi sửa tay).
2. E không có đoạn xin cha hoãn nợ, cùng lý do.
⇒ Muốn giữ hai cảnh đó thì phải **đưa vào brief**, không phải viết lại câu trong bản thảo.

## 9. Đoạn 002 và 003 (chạy tiếp, không sửa tay nhiều)

| | mẫu | 002-a | 003-a |
|---|---|---|---|
| 字 | 2.122 (trung vị) | 1.439 | 1.360 |
| chữ/câu | 23,9 | **16,0** | **15,8** |
| lượt thoại | 20 | 19 | 8 (brief ghi "thoại ít") |
| chữ/lượt | 22,4 | 25,9 | 20,0 |
| tật | ~1 so sánh/chương | **0** | 1 (`捆了个结实` → sửa tay) |

**002** (nối session với 001, 107s): đủ 6 beat — 497 người, 3.400 斤 = ba ngày, 代守 bán lương lấy 20 金币
và dẫn 40 lão binh đi, 60 步 / 120 根 cọc / 24 rìu × 3 = 72 根/ngày, đêm thấy 43 火头. Câu cuối
`“给我数数对面的火头。”` đúng dạng nói. Tự sửa tay 1 câu: `城里连一粒麦子都没剩…也没用` (phủ định cặp).

**003** (session mới, SI v5, 147s): trận đầu 9 豺狼人 — 阿德里安 giết 2 (18 点 → 499/500), nhóm 卡尔 giết 3,
4 con chạy; 5 chết 8 bị thương → 492; treo kẻ bỏ chạy; câu cuối `“今晚加练。”`. Sửa tay 3 chỗ: `老骑士`
(卡尔 là cựu phó quan, không phải kỵ sĩ), `【士兵：一阶.492 农奴（士气涣散）】` → đúng dạng `维兰农奴（0/100）`,
và `捆了个结实` (khuôn 实). **Lỗi hình dạng bảng là do brief của Agent** — brief chỉ ghi "士兵 一阶.492",
không chép nguyên dòng bảng; từ đoạn sau brief phải chép nguyên cả dòng.

**Phát hiện quan trọng — trượt nhịp câu:** cả ba đoạn (001-e 15,5 · 002 16,0 · 003 15,8 字/câu) đều ngắn hơn
mẫu (23,9) và ngắn hơn chính các bản trước khi bỏ trần độ dài (A 20,0 · C 19,4). Bỏ chỉ tiêu 字 ⇒ model nén cả
câu, không chỉ nén đoạn. SI v6 thêm **sàn**: trung bình ~23 字/câu, chuỗi câu dưới 15 字 là danh sách chỉ dẫn.
Đây là chỗ phải đo lại ở đoạn 004 trước khi tin SI v6.

## 10. Đoạn 002-b — sửa gốc rễ thoại MC (SI v7)

Tác giả: "thoại của MC luôn làm tôi khó chịu." Chẩn đoán trên 26 lượt của MC ở 001-E/002/003: trung vị **8 字**,
15/26 lượt ≤8 字, không một lượt nào hỏi thật / xin / cảm ơn / nhận sai / nói chuyện ngoài việc; lượt nào cũng
ra lệnh hoặc phán; và hắn thắng mọi cuộc bằng đe dù chưa có quyền (19 tuổi, không lệnh bắt ai, mà 代守 cúi
đầu ngay). Ba câu ngầu liên tiếp ở ba đoạn (`斧子不能当饭吃…` / `今晚加练。` / `它们走累了。`) là tật thứ tư.

SI v7 thêm 3 dòng: (a) hắn chỉ ra lệnh khi đã trả giá mua quyền — với người không nợ hắn thì mua, hỏi, nịnh,
nhờ, và người kia có quyền từ chối; (b) mỗi cảnh một câu hỏi thật + một lượt ngoài việc; (c) mỗi đoạn tối đa
một câu ngầu, không đặt ở cuối đoạn. Brief 002-v2 thêm khối 【Quyền lực trong cảnh】 (hắn **không có** quyền
trên 代守; vũ khí duy nhất là tờ 委任状 và 497 cái bụng đói).

| | 002-a | 002-b (SI v7) |
|---|---|---|
| chữ/câu | 16,0 | **23,9** (mẫu 23,9) |
| lượt thoại | 19 | 14 |
| lượt của MC | 9 (trung vị 17 字) | 6 (trung vị **25,5** 字) |
| tật | 0 (sau 1 sửa tay) | 1 nhãn ngữ điệu (đã sửa: `平静地说道` → `把羊皮纸摊在他眼前`) |

Thay đổi trong thoại, cụ thể:

| | 002-a | 002-b |
|---|---|---|
| câu hỏi | `“你这是要走？”` | `“谁给你批的撤防文书？”` — câu hắn **không biết đáp án** |
| đối phương | 代守 giải thích rồi đi | `“粮册上全是死人和七年前的烂账，钥匙我有，凭什么白白给你？”` — 代守 **từ chối** |
| vũ khí của MC | `“少一样，你们今天谁也出不了这道门。”` (đe, không có quyền) | `“凭这个，这是我父亲亲笔签的换防委任状。”…“你拿着它走，路上要是撞见巡防骑兵，就说是我带兵接替了防务，我不会往上面报你私自弃守。”` — **mua bằng một lời hứa** |
| nhận thức quyền lực | chỉ có `士气` | tường thuật nói thẳng: `真要拔剑动手，这四十个杀过人的老残兵能把他的农奴队伍冲得七零八落` |
| ngoài việc | không có | `“你家里还有几口人留在巴罗尔城？”` → 卡尔: vợ, hai con, đứa lớn bảy tuổi → MC hứa ba ngày phép |
| kết đoạn | `“给我数数对面的火头。”` (câu chốt) | 卡尔 trèo lên mép tháp canh đếm lửa — **không có câu ngầu** |

Giới hạn: một cảnh, một lần chạy. Muốn nhận công thì phải chạy 002-b lần thứ hai và so hai bản sinh.
