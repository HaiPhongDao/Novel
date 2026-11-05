# Đọc bài hiệu chuẩn v5 — ch3, ba prompt xếp chồng (SI giữ v1)

Nền: SI v1 (`gemini/si-dan-gemini.txt`, 5.468 ký tự) · thinking High · hai chat mới mỗi bản (AI Studio, 05/11/2026,
`jobs-v5-ch03.json`). Lý do và ba prompt: `README.md`.

| Bản | Prompt | Thêm gì so với bản trước | Bản a | Bản b |
|---|---|---|---|---|
| **P1** | `brief-P1.md` | khuôn "Viết tiếp…" + khối nối tiếp nguyên văn đuôi ch2 (【接上】…【接上完】) | `P1-a.md` 3.367 字, 279 s | `P1-b.md` 2.826 字, 256 s |
| **P2** | `brief-P2.md` | P1 + ví dụ brief → văn ch2 **trong prompt** (khối GIỌNG MẪU) | `P2-a.md` 4.055 字, 286 s | `P2-b.md` 3.548 字, 206 s |
| **P3** | `brief-P3.md` | P2 + bảy chỗ đánh dấu "trong đầu cậu bật ra một câu, bằng giọng cậu" | `P3-a.md` 3.801 字, 239 s | `P3-b.md` 3.110 字, 245 s |

Cổng máy XANH cả sáu. Gemini đọc cặp: `gemini-doc-P1.md` (63/63 trích thật) · `gemini-doc-P2.md` (40/40; lượt đầu mã 3,
chạy lại) · `gemini-doc-P3.md` (49/49).

**Câu ĐẠT là của Tác giả — chờ Tác giả đọc.**

## Tóm tắt: đánh dấu dịp (P3) là thứ đầu tiên trả lại tiếng lòng MC, nhưng Writer đặt nó trong ngoặc “”

- **P3 giữ 4/5 và 3/5 chỗ tiếng lòng của gốc** (v1–v4: 0–2/5). P3-b có năm câu trong đầu MC, hai câu có 我:
  «“合着在这儿等着我呢。”洛羽心底冷笑了一声。» · «“靠，真就一个极品天赋都没有？”洛羽在心底暗骂了一句。» ·
  «“这算盘打得我在店门口都听见了……”洛羽在心底暗自发笑。» · «“贵是真贵，帅也是真帅。”» (gốc: «骗小孩呢？！» · «靠。» ·
  «我信你个鬼。»). P3-a là bản đầu tiên trong cả năm lần thử cho **nhân viên 疾风 có tiếng lòng**: «“…你小子在这儿纯粹数虫子
  消遣爷爷呢？！”伙计心头暗骂» (gốc «几千条还他妈不够你挑？！来挑事的吧！»).
- **Nhưng hình thức khác gốc**: gốc viết tiếng lòng trần trong lời kể, không ngoặc, không thẻ; P3 viết như thoại —
  “…” + 洛羽在心底暗骂/冷笑/发笑. Vì chỉ số sổ (！+？ lời kể) bỏ phần trong “”, nó không thấy chỗ tăng này: P3 0,53/0,32
  → `vo-hieu`. Tính cả tiếng lòng trong “” thì 0,79/0,96 (gốc 5,31) — vẫn xa.
- **P1 (nối tiếp đuôi ch2)** không đổi giọng, trừ câu cuối P1-b — câu duy nhất trong cả năm lần thử có tiếng lòng **trần
  trong lời kể** như gốc: «好家伙，这岛上的大商队，合着全把宠兽当成自产自销的蓄电池在用？».
- **P2 (ví dụ trong prompt) tệ nhất**: 0/5 cả hai bản, ！+？ 0/0,28 — giống ví dụ trong SI ở v4 (E). Ví dụ vẫn bị bỏ qua
  về giọng; chỉ để lại một tên riêng (洛水研究所, P2-b).

Xếp theo mức lời kể nói bằng giọng nhân vật: **P3 > P1 > P2**.

## Kiểm chép

- **Đuôi ch2 (khối nối tiếp)**: 0 câu chép lại. Tên 二尾沧猊 xuất hiện ở P1-a, P2-b như việc nối tiếp («二尾沧猊的事情暂且
  搁置，眼下最要紧的是后天的考核。») — đúng ý "viết tiếp". Trùng 7-gram với đuôi ch2: P2-a 1 cụm («满载货物的商船»), còn lại 0.
  绝育手术 · 缅因猫 · 异瞳鸳鸯眼: 0.
- **Ví dụ ch2 (P2, P3)**: 占卜|珍珠|奶牛|虎鲸|星贝|面包 = 0; 7-gram ngoài thuật ngữ 培育资质考核 = 0. Một chỗ mượn từ **brief**
  ví dụ: P2-b «培育资质证明关系到洛水研究所的归属» (洛水研究所 chỉ có trong khối ví dụ, đúng canon bộ mẫu) → E-CANON-05 × 1.

## Số đo (kính lúp, không chấm) — a / b

| Chỉ số | Gốc | v1 | **P1** nối tiếp | **P2** + ví dụ | **P3** + đánh dấu | Khoảng 30 ch. |
|---|---|---|---|---|---|---|
| 字 | 2.822 | 3.646 / 2.769 | 3.367 / 2.826 | 4.055 / 3.548 | 3.801 / 3.110 | — |
| 字/đoạn | 20,9 | 34,1 / 48,6 | **32,4 / 30,4** | **67,6** / 47,9 | 40,0 / 51,8 | 19,6–33,4 |
| 字/câu | 18,4 | 33,7 / 30,4 | 30,7 / 28,8 | 35,7 / 27,4 | 38,2 / 32,4 | 14,8–29,5 |
| lượt thoại | 49 | 14 / 18 | 13 / 14 | 18 / 17 | **24 / 21** | 16,6–64,8 |
| 字/lượt | 8,7 | 19,7 / 15,5 | 18,3 / 12,6 | 20,7 / 20,3 | 29,3 / 13,7 | 6,5–27,6 |
| ！ lời kể /1.000 | 2,83 | 0 / 0,36 | 0,30 / 0 | 0 / 0,28 | 0,53 / 0,32 | — |
| ？ lời kể /1.000 | 2,48 | 0 / 0 | 0 / 0,35 | 0 / 0 | 0 / 0 | — |
| **！+？ lời kể** (chỉ số sổ) | 5,31 | 0 / 0,36 | 0,30 / 0,35 | 0 / 0,28 | 0,53 / 0,32 | — |
| ！+？ kể cả tiếng lòng trong “” | 5,31 | 0 / 0,36 | 0,30 / 0,35 | 0 / 0,28 | **0,79 / 0,96** | — |
| chỗ tiếng lòng giữ được /5 | 5 | 0 / 0 | 1 / 1 | 0 / 0 | **4 / 3** | — |
| tiếng lòng MC đặt trong “” + thẻ 心底 | 0 | 0 / 0 | 0 / 0 | 0 / 0 | **1 / 5** | — |
| tiếng lòng nhân viên 疾风 | có | 0 / 0 | 0 / 0 | 0 / 0 | **1** / 0 | — |
| câu 我 trong lời kể | 1 | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 (b: 2 câu 我 trong “”) | — |
| 靠/卧槽/好家伙 lời kể / tổng | 2 / 2 | 0 / 0 | 0 / 0 · **1 / 1** | 0 / 0 | 0 / 1 · 0 / 1 | — |
| câu thuật lại việc nghĩ | 1 | 6 / 4 | 3 / 2 | 5 / 6 | 6 / 5 | — |
| nhãn điềm tĩnh 淡然/平静/从容/木然/淡漠 | 0 | 5 / 2 | 1 / 0 | 2 / **4** | 0 / 1 | — |
| nhãn ngữ điệu (regex) | 0 | 0 / 0 | 0 / 2 | 0 / 0 | 1 / 0 | — |
| phủ định lặp (soat_van) | 5 | 2 / 0 | 0 / 0 | 1 / 2 | 0 / 2 | — |
| giảng huấn /1.000 | 0 | 0,82 / 0,36 | 0,59 / **1,06** | 0,49 / 0,85 | 0,79 / 0,64 | 0–1,0 |
| thinking soát phủ định/so sánh (grep) | — | — | 9 / 4 | 47 / 11 | 29 / 43 | — |

Đo bằng cùng script như v4 (`hieu_chuan.do()` + `soat_van.scan()`). "Tiếng lòng trong “”" = câu trong ngoặc có thẻ
心头/心底/暗骂… của MC đứng trước hoặc sau; v1-b, E-a, E-b có câu MC **nói khẽ** (自语/嘀咕) — không tính. "Chỗ tiếng lòng"
dùng năm chỗ như v3/v4; 颜值党/颜控 tính là giữ.

## P1 — khuôn "Viết tiếp" + nối tiếp đuôi ch2

- Mở cảnh nối liền đuôi ch2 (xe đạp, tờ truy nã) thay vì «洛羽终于赶到目的地。», nhưng lời kể vẫn thuật lại việc nghĩ:
  «骗小孩呢？！» → a «脑海中瞬息推演出了整套算盘», b «洛羽眼皮都没抬一下»; «我信你个鬼。» → a «洛羽暗自颔首», b «洛羽心头一片通透».
- Câu cuối: b «好家伙，这岛上的大商队，合着全把宠兽当成自产自销的蓄电池在用？» (trần, đúng kiểu gốc); a «洛羽心头猛然一紧：
  这群家伙分明把活生生的宠兽当成了发电的电池！» (có ！ nhưng nghiêm).
- Nhân viên 疾风 chỉ tả ngoài: a «紧紧咬住后槽牙，竭力压制着翻涌的闷气», b «将涌上喉头的恶言压了回去».
- Hình thức gần khoảng nhất trong mọi bản đã chạy: 字/đoạn 32,4/30,4 (khoảng 19,6–33,4), 字/câu 30,7/28,8. Lỗi: a lại làm
  冷雾蜥 thành «水冰双系»; a thêm «恒温暖箱…租金便高达数百联盟币»; b giảng huấn 1,06.

## P2 — + ví dụ brief → văn ch2 trong prompt

- Năm chỗ mất cả hai bản: «骗小孩呢？！» → a «心头泛起一丝冷笑», b «洛羽在心里冷笑一声»; «我信你个鬼。» → a «洛羽平静地收回目光»,
  b «洛羽微微点头，眼底却掠过一丝了然».
- Câu cuối phẳng: a «这帮大商队当真是把变异兽身上的每一点油水都榨取到了极致。», b «这地方的老板，下手恐怕比上一家开制冰厂的还要
  狠辣几分。» (gốc «到底是在卖宠物，还是在卖黑奴？»).
- Ví dụ không chuyển giọng mà kéo thêm thứ khác: a 67,6 字/đoạn (gấp đôi trần), b bốn nhãn điềm tĩnh; thinking P2-a soát
  phủ định/so sánh 47 lần. Mượn tên 洛水研究所 từ brief ví dụ (b); a bịa con số «一共两千四百六十只», «满打满算剩下一千五百块联盟币».

## P3 — + bảy chỗ đánh dấu dịp nội tâm

- Tiếng lòng ra ở đúng các dịp được đánh dấu: «骗小孩呢？！» → a «…能正常长大才见鬼呢？», b «“合着在这儿等着我呢。”»;
  «我信你个鬼。» → a «你们东家做生意的脑子真是转得飞快», b «“这算盘打得我在店门口都听见了……”»; «颜狗» → a «颜值党», b «颜控».
- Câu cuối: a «“好家伙，这又是拿活生生的宠兽当全天候生物电池使唤呢！”» (giọng có, nhưng trong ngoặc như lời nói); b quay về thuật
  lại «暗骂这帮资本家简直连宠兽骨髓里的一丝电力都不肯放过».
- Nhân viên 疾风 ở a có tiếng lòng lần đầu («…消遣爷爷呢？！”伙计心头暗骂»); b vẫn tả ngoài «心底的不耐终于攀上顶峰».
- Hình thức: tiếng lòng biến thành lượt thoại (lượt thoại 24/21, cao nhất các bản) với thẻ «洛羽在心底暗骂了一句» — gốc không
  có thẻ nào kiểu này. Vẫn còn nhãn «洛羽淡然回绝», «声调平淡地开口介绍»; b đổi giá 冷雾蜥 «九千八百联盟币» (gốc ~一万), bịa hạn
  «往后两年» và «三百克»; «一虫传三代» mất cả hai.

## Đọc chung và đề xuất (chờ Tác giả)

1. **Đánh dấu dịp trong brief có tác dụng lên nội dung tiếng lòng** (4/3 trong 5 chỗ, so với 0–2 ở mười bản v1–v4 và P1/P2)
   — khớp quan sát v3: chỗ nào brief ghi "một câu trong đầu" thì Writer viết ra. Ví dụ (trong SI hay trong prompt) và
   khối nối tiếp không làm được việc đó.
2. Còn thiếu **hình thức**: tiếng lòng phải nằm trần trong lời kể (không “”, không thẻ 心底暗骂). Biến kế gợi ý (một
   biến, giữ P3): thêm một dòng ở chỗ đánh dấu hoặc SI — "câu trong đầu viết thẳng vào lời kể, không ngoặc kép, không
   thêm 他心想/在心底…" — rồi đo lại bằng cả hai chỉ số.
3. Chỉ số sổ (！+？ lời kể, bỏ phần trong “”) không thấy được tác dụng của P3 vì hình thức sai; ghi `vo-hieu` theo số,
   nhưng không nên đọc là "đánh dấu vô ích". Cột "chỗ tiếng lòng /5" mới là chỗ thấy khác — chưa đưa vào sổ vì đặt sau khi
   xem dữ liệu.

Biên độ trong sổ = max(chênh hai bản v1 = 0,36; chênh hai bản của biến) như v3/v4 — lấy riêng chênh P1 (0,05) thì P1 ra
2,9× "hiệu quả" giả trên mức tăng 0,15. Chênh P2 0,28, P3 0,21.
