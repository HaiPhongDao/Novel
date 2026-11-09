# Phân tích lại SI co-dai từ đầu (08/11/2026)

Tác giả: "Phân tích lại SI từ đầu, xem cách bộ sủng thú làm như nào." Đọc nhánh `co-dai` trên GitHub (commit
`631593d`), bộ mẫu 《乱世荒年：我每日一卦粮肉满仓！》 ch1–12, ch16, ch30, ch33, và toàn bộ hồ sơ hiệu chuẩn `sung-thu`.

## Tóm tắt

1. **SI đang chạy có cùng bệnh với SI v1 của sung-thu.** Nó được điền từ SI-template v6 nhưng **bỏ mất ô "giọng người
   kể"** (mục 2 của khung). Vì vậy không dòng nào nói lời kể là cái đầu của nhân vật. Bản Writer đoạn 001 ra người kể đứng
   ngoài, thêm giọng võ hiệp. Bản Writer gốc chỉ có hai câu là tiếng của chính MC 陆青, và cả hai đều đã bị sửa tay xoá
   khỏi bản hiện tại.
2. **Làn mở truyện bị bỏ bước.** Có brief `test-hieu-chuan-001.md` nhưng không có bản sinh, không có đọc cặp, không có
   Tác giả đọc ĐẠT. Dù vậy bible và đoạn 001 đã làm xong. `chapters/doan-001.md` hiện tại là **bản đã sửa tay hai lượt**,
   không phải bản Writer.
3. **Đề xuất:** viết lại cả SI từ giọng bộ mẫu, đúng cách sung-thu đã làm được (SI Argon, I-0059). Bản đề xuất:
   `test-giong/v2/si-v2.md`. Sau đó chạy bài thử ch4 hai chat mới, có đối chứng SI cũ, rồi Tác giả đọc.

## 1. Bộ mẫu kể thế nào

Truyện kể ngôi ba nhưng **lời kể là cái đầu của người trong cảnh**, trước hết là 江尘, một 社畜 hiện đại trong thân xác
kẻ lêu lổng năm đói. Năm thủ pháp, mỗi cái kèm câu trích:

| Thủ pháp | Câu gốc |
|---|---|
| MC **lẩm bẩm một mình trong “”**, câu đứng riêng, thường không có thẻ | «“还不小！”» · «“都是兔子脚印，看来这附近有一窝兔子啊……”» (ch4) · «“退亲，好事啊！”» (ch5) |
| **Câu thầm trần** trong lời kể, có ？！, khẩu ngữ, thỉnh thoảng có chữ hiện đại | «无他，不会而已。» (ch4) · «老狼王也是狼王啊！他疯了才会这么做。那不是去狩猎，是去送菜。» (ch2) · «让自己去当舔狗？…那他不是白穿越了吗！» (ch9) |
| **Bước vào đầu người bị tác động**, cho họ một hai câu trần | 张三坡 «这三斤的兔子，够他好好吃一顿了！» (ch5) · 孙金梅 «当面叫破了又有什么事？这就辱你了？» (ch7) · 陈巧翠 «两只，也能换二十多斤粟米呢！» (ch12) |
| **Luật, giá, nợ** đi qua người đang tính, có cái nhìn của người đó | «一两半…… 一千五百文。…买错了可就亏大了» (ch33) · «“大哥还是太老实。”江尘腹诽，“这种地主，就等着荒年买田。”» (ch30) |
| **Đánh nhau trơn, nhanh**, cái sắc của MC nằm ở câu mỉa | «江尘已经拔出腰间柴刀，抵住了张三坡的脖子。» · «“玩笑？那你给我笑一个。”» (ch4) |

Số đo 30 chương đầu bằng script của phiên này. Số chỉ để khoanh vùng, không dùng để chấm:

| Chỉ số (/1.000 字 trừ khi ghi khác) | TB | Khoảng |
|---|---|---|
| ！+？ trong lời kể (ngoài “”) | 2,27 | 0 – 8,48 |
| trợ từ 啊吧呢嘛 trong lời kể | 1,03 | 0 – 3,41 |
| % đoạn có thoại | 39,8 % | 13 – 60 % |
| lượt thoại / chương | 33 (≈ 20 /1.000 字) | 6 – 55 |
| 字 / chương | 1.626 | 898 – 1.987 |
| thẻ tâm lý + ngoặc (腹诽 / 暗忖 / 心想 … “) | 7 lần trong 48.785 字 — hiếm | |
| chữ hiện đại (舔 · 穿越 · 前世 · 社畜 · 送菜 · 懵逼 …) | ~30 lần / 30 chương | |

**Khác sủng thú ở một chỗ quan trọng.** 《神宠供应商》 để tiếng lòng trần, ngoài ngoặc. Bộ này có **cả hai dạng**: lẩm bẩm
trong “” và câu thầm trần. Vì thế **không chép nguyên** FIXED 3 hay BANS dòng 1–2 của SI Argon. SI Argon cấm đặt tiếng
lòng trong ngoặc, còn ở bộ này ngoặc lại là đúng. Bản mổ xẻ `mo-xe/loan-the-hoang-nien/tong-quan.md` mục 4.2 ghi "độc
thoại nội tâm đặt thẳng trong ngoặc kép" — nhận xét này chỉ đúng một nửa.

## 2. SI đang chạy dạy Writer điều gì

SI đang chạy là `system-instruction.md` (8.703 ký tự phần dán). Đọc từng chỗ đối chiếu với mục 1:

| Chỗ | Chữ trong SI | Vì sao kéo ra người kể đứng ngoài |
|---|---|---|
| ROLE | "earthy survival register … Third-person limited on the protagonist" | Không nói lời kể là cái đầu MC. Không nói MC mang đầu óc hiện đại, nên trong bản 陆青 không có một chữ hiện đại nào. |
| FIXED 3 | "Narration uses full stops and commas; `？`, `！` … land on finds, calculations" | Đây chính là dòng đã dạy người kể đứng ngoài ở sung-thu (thinking v1 đọc thành "lời kể chỉ dùng chấm, phẩy" — KN38). Bản Writer có 16 dấu ！？ trong lời kể, nhưng tất cả là câu cảm thán của người kể về số hoặc đòn đánh: «三斤八两高高的！» · «眼前骤然掠过一道耀眼的寒白！». |
| Mục 1 | "Narration rides with his eyes, stomach, and calculations without `他心想`" | Có nửa "không 他心想", thiếu nửa "viết chính câu đang nghĩ". Ô GIỌNG NGƯỜI KỂ của khung bị bỏ: SI nhảy từ mục 1 sang "Rules…" và đánh số lại thành 2. |
| Mục 2 | "Rules, accounts and decisions arrive as a chain of statements" | Chép nguyên tiêu đề khung, dạy giọng báo cáo. Bản Writer: «五十文钱换作平日…谁手里有余钱买柴？活路只在苍龙岭里。山里的野味和皮张，送到镇上酒楼当铺，当场就能换得现钱与干粮。» — đọc như một bài giải thích. |
| Mục 4 | "Payoffs land fast against an even voice" | Câu ví dụ của SI-template, chép nguyên, không đo từ bộ mẫu. "Even voice" nghĩa là giọng đều. Bộ mẫu ngược lại: payoff nổ trong đầu người thua (孙金梅, 张三坡). |
| Anchor | ch89, ch90, ch28, ch70; 3.122 ký tự = **36 %** phần dán (trần 15 %) | Dài, phần lớn là chợ cá và đầu nhân vật phụ, rất ít câu thầm của MC. Anchor ch28 **không khớp nguyên văn** (gốc «江有林听到动静从屋里走出来…也吃了一惊» bị cắt; `verify_anchors.py` MISS). |
| Chú thích anchor | "Setting out fish baskets…, clubbing and weighing a seven-catty catfish…" | Chú thích tóm tắt cốt truyện thay vì gọi tên thủ pháp, nên Writer học nội dung: «三斤八两高高的！» lấy từ anchor «七斤二两高高的». |
| BANS 2–4 | "narration names the thing … without narrator similes" · "One negation to a paragraph" · "no tone label or adverb before the verb" | Dòng 2 là dạng N đã thử ở sung-thu (I-0054 vô hiệu). Bộ mẫu không giới hạn phủ định theo đoạn và có dùng 笑着开口 · 喜滋滋地应下 · 闷闷回了一句. Các dòng này kéo chú ý của Writer vào những chỗ không phải lỗi. |
| PART 4 | 技**艺**熟练度面板 | `log.md` ghi 【技**能**熟练度面板】, brief đoạn 001 ghi cả hai. |
| Đời SI | `system-instruction.md` không có số đời; `system-instruction-v1.md` là bản nháp cũ hơn | `python tools/dung_si.py co-dai` không có `--version` sẽ dựng từ v1 (8.843 ký tự) và đè lên `si-dan-gemini.txt`. Phiên này đã lỡ chạy một lần và đã `git checkout` trả lại. |

## 3. Bản Writer đoạn 001 cho thấy gì

So bản Writer gốc (commit `59d1447`) với 30 chương đầu của bộ mẫu:

| | Bản Writer gốc | Bộ mẫu (TB) |
|---|---|---|
| 字 | 3.930 (brief đòi 3.000) | 1.626 |
| % đoạn có thoại | 15,2 % | 39,8 % |
| lượt thoại /1.000 字 | 8,7 | ≈ 20 |
| trợ từ 啊吧呢嘛 trong lời kể | 0 | 1,03 |
| câu lẩm bẩm hoặc câu thầm của MC | **2**: một câu lẩm bẩm phẳng «“是只成年的野鸡。”» và một câu thầm trần nằm trong khối popup — cả hai bị sửa tay xoá | ch4 gốc: 3 câu lẩm bẩm, ~10 câu thầm trần |

Những dạng hỏng đã thấy (SI v2 lấy chúng làm BANS):

- Võ hiệp: «眼前骤然掠过一道耀眼的寒白！» · «贴着刘三水的鼻尖劈斩而下！» · «通身透着一股山里独狼般的凶蛮狠劲».
- MC lạnh lùng: «陆青冷冷注视着那道身影跑入风雪。»
- Tả tâm lý từ bên ngoài: «显然嗅到了浓厚的野物血腥» · «眼底闪过恶念».
- Tiếng động đứng thành dòng thoại: «“崩！”» «“噗！”» «“呼！”» «“咄！”».
- Kết bằng phán quyết: «这片浩瀚凶险的苍龙岭，自今日起，真正成了他安身立命的粮仓。»

**Sửa tay.** Sau `59d1447` bản chương bị sửa tay hai lượt:

- `729e952`: viết lại khối 【】, xoá bốn khối popup, thêm câu mới «熟练地续上两具单扣地伏套索».
- `631593d`: gộp lượt thoại (lượt của 刘三水 thành ~70 字, trong khi bộ mẫu trung bình 12,5 字/lượt); thay câu lẩm bẩm
  «“是只成年的野鸡。”» bằng câu kể «看那蹄爪与啄痕，分明是只成年的野鸡。»; thêm nhãn «恶狠狠嚷道».

SKILL mục 2 cấm sửa tay rồi trình bản đó như kết quả. Ở đây sửa tay còn kéo bản **xa** bộ mẫu thêm. Câu có giọng MC duy
nhất của bản gốc, «亲自动手摆弄猎具，经验便能往上涨！», bị xoá cùng popup.

**Brief đoạn 001** cũng mắc các lỗi Tác giả đã bác ở sung-thu (E-BRIEF-09): giao cả chuỗi sự kiện của một chương (tỉnh
dậy → mài dao → bẫy → đột phá → bắn → 刘三水 → xuống núi), chữ Hán chen giữa câu Việt, có tính từ cảm giác ("ánh mắt
cực kỳ tỉnh táo"). Nhưng sửa brief trước là sai thứ tự. Ở sung-thu, brief Argon đi với SI cũ vẫn vô hiệu (I-0061); chỉ
khi đổi SI giọng mới ra (I-0059).

**Bible.** `bible/characters.md` đang là nhân vật của bộ mẫu (江尘…), không phải của truyện (陆青…). Trong đó 张三坡
ghi 22 tuổi, nhưng bộ mẫu ghi hơn 江尘 hai tuổi, tức 20.

## 4. Sủng thú đã làm thế nào

- **Năm lượt một biến đều vô hiệu** (I-0049…I-0058): khung gọn + đổi anchor; bỏ BANS; thinking Low; thẻ giọng; đổi anchor;
  ví dụ brief→văn đặt trong SI; sửa người kể; sửa brief ba kiểu. Lượt nào cũng ra người kể đứng ngoài.
- **SI Argon viết lại cả bản từ giọng bộ mẫu** → lần đầu lời kể nói bằng giọng MC (I-0059 `hieu-qua`, 3,19× biên độ).
  Tác giả đọc: "Đó, bản X…"; ch5/ch8: "Đạt".
- Những chỗ SI Argon khác SI cũ:
  - ROLE nói lời kể đi từ trong đầu MC.
  - FIXED 3 dành chỗ cho tiếng lòng đúng như bộ mẫu viết.
  - Mục 1 có nửa "bỏ động từ thuật lại, viết chính câu đang nghĩ".
  - Mục 2: luật và giá đi qua MC tính kèo.
  - Chú thích anchor gọi tên thủ pháp, có trích chữ.
  - BANS kể ra các dạng hỏng đã thấy, trích đúng chữ.
- Bài học đã vào SKILL (Pipeline bước 1, mục 7): đi ≥3 vòng một biến mà vô hiệu thì viết lại cả SI; **đừng mang chữ
  SI của bộ khác giọng sang**.
- co-dai chưa chạy vòng nào, nên không cần lặp lại năm vòng đó. Đi thẳng sang bước viết lại cả SI, dựng từ giọng của
  **bộ mẫu này**, không chép chữ của Argon.

## 5. SI v2 đề xuất

Nguồn có ghi chú: `test-giong/v2/si-v2.md`. Bản dán: `test-giong/v2/si-v2.txt`. **Chưa dán** vào
`si-dan-gemini.txt`.

| | SI đang chạy | SI v2 | SI Argon (sung-thu v3) |
|---|---|---|---|
| Phần dán | 8.703 | **7.895** | 7.630 |
| Anchor | 5 · 3.122 ký tự = 36 % | **4 · 886 = 11 %** | 4 · 780 = 10 % |
| Anchor khớp nguyên văn | 3/4 (anchor 5–6 là mẫu định dạng bảng) | **4/4** | 4/4 |
| PART 2 / BANS | 4 / 5 | 4 / 5 | 3 / 5 |

Thay đổi chính (chi tiết trong comment đầu `si-v2.md`):

- **ROLE:** lời kể đi từ trong đầu người trong cảnh, trước hết là MC — "a modern mind waking up in a famine-year body".
  Giọng nhẹ vì các cái đầu sống động, không vì thế giới hiền.
- **FIXED 3:** bỏ "Narration uses full stops and commas". Tách hai dạng tiếng lòng: lẩm bẩm trong “” đứng riêng, và câu
  thầm trần trong lời kể. ？！ dùng ở lời kể như ở thoại.
- **Mục 1:** thêm "giọng kể là MC đang nghĩ tại chỗ; bỏ động từ thuật lại" và "bước vào đầu người bị tác động một hai
  nhịp". Anchor ch9 (田契 → 舔狗).
- **Mục 2:** "somebody sizing up the deal": một hai sự thật trần, rồi cái nhìn của người đang tính, kết bằng một câu nói
  thẳng. Anchor ch30 (九出十三归).
- **Mục 3:** thoại việc nhà, có lý do và con số; giữa các lượt là một câu trần của cái đầu đang phản ứng. Anchor ch12 (chia gà).
- **Mục 4:** "When he turns a scene, the loser's head takes the beat". Anchor ch7 (孙金梅).
- **BANS:** năm dạng hỏng của mục 3 phía trên, trích đúng chữ: tả tâm lý từ ngoài · võ hiệp · MC lạnh lùng · tiếng động
  thành dòng thoại · kết bằng phán quyết.
- **PART 4:** giữ bảng 【技艺】, thêm "chỉ mình MC thấy" và "ý MC về con số đến sau, bằng giọng MC".

Anchor không lấy từ ch4 (chương thử). Cũng tránh ch5, vì ch5 nối tiếp ch4 (张三坡, con thỏ). Chưa dòng nào có mã can
thiệp: cả SI đổi một lượt, giống I-0059. Tách xem dòng nào có tác dụng là việc làm sau khi Tác giả đọc ĐẠT.

## 6. Bài thử

- **Chương 4 「守株待兔，张三坡」** (1.358 字). Cùng tình huống với đoạn 001 của truyện (lên núi nhặt mồi, kẻ lêu lổng chặn
  đòi), nên Tác giả so được thẳng. Chương này không có bảng bàn tay vàng.
- Brief chỉ có sự việc: `chung/hieu-chuan/loan-the/ch04/brief.md` (`soat_brief` XANH). Đáp án: `goc.txt` cùng thư mục.
- Chạy 4 chat mới. Biến duy nhất là SI: `V2-ch04-a/b` (SI v2) và `CU-ch04-a/b` (SI đang chạy, đối chứng):

  ```
  python tools/aistudio_run.py --batch co-dai/gemini/test-giong/v2/jobs-ch04.json
  ```

- **Chín chỗ đọc**, mỗi chỗ ghi theo gốc ch4:
  1. tuyết không dấu thú — có câu MC tự nói "hôm nay không cần săn thật" không;
  2. dấu thỏ — câu lẩm bẩm trong “” hay câu kể "他判断…";
  3. không biết đặt bẫy — câu tự giễu trần (gốc «无他，不会而已。»);
  4. nhặt thỏ — lẩm bẩm + câu trần về hai đứa cháu;
  5. luật chặt cây — một hai sự thật rồi cái nhìn của người đang làm;
  6. 张三坡 rủ cầm áo — câu nhận xét trần của MC;
  7. đầu 张三坡 (ghen chiếc áo; ngẩn ra vì bị đáp trả) — câu trong đầu hắn hay chỉ tả mặt;
  8. bị giật thỏ — MC tức quá hóa cười bằng câu trần, ý "thân xác đã đổi chủ";
  9. kề dao — đòn trơn hay võ hiệp; câu mỉa ngắn.

  Kiểm thêm:
  - dừng đúng câu của 张三坡;
  - khối 【技艺】 tự in (phải là 0);
  - các dạng BANS;
  - độ dài (sung-thu dài hơn gốc +50–90 %).
- Câu ĐẠT do Tác giả nói. Sau khi ĐẠT:
  1. thử thêm ch3 (cảnh gia đình, 58 % đoạn có thoại), giống sung-thu đã thử thêm ch5/ch8;
  2. đổi sang `system-instruction-v2.md`, chạy `dung_si.py`, ghi `log.md` (`Duyệt:`, ký tự 8.703 → 7.895);
  3. viết lại brief đoạn 001 thành một tình huống, chạy lại bằng chat mới.

## 7. Cần Tác giả quyết

1. Cho chạy bài thử ch4 (SI v2 + đối chứng SI cũ, 4 chat)?
2. Tên bàn tay vàng: 技艺熟练度面板 hay 技能熟练度面板?
3. 陆青 kiếp trước là ai? SI v2 dựa vào "đầu óc hiện đại trong thân xác năm đói". Nếu 陆青 không xuyên từ thời hiện đại
   thì phải đổi ROLE.
4. Đoạn 001 hiện tại: Agent khuyên **không chốt** (bản đã sửa tay, giọng người đứng ngoài); viết lại sau khi SI ĐẠT.
5. Toàn văn bộ mẫu (1,2 MB) đang commit trên nhánh `co-dai`, trong khi AGENT.md mục 2 ghi không commit toàn văn. Giữ hay gỡ?
