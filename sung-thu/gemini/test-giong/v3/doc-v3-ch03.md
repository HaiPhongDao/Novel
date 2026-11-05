# Đọc bài hiệu chuẩn v3 — ch3, ba biến song song

Nền: SI v1 (`gemini/system-instruction-v1.md`, dán 5.468 ký tự) · brief gốc `chung/hieu-chuan/than-sung/ch03/brief.md` ·
thinking High. Mỗi biến đổi **một** thứ, hai chat mới (AI Studio, 05/11/2026, `jobs-v3-ch03.json`):

| Biến | Đổi gì | File | Bản a | Bản b |
|---|---|---|---|---|
| **A** | thinking High → **Low** (bridge đặt được, không cần Minimal) | `jobs-v3-ch03.json` | `A-a.md` 3.322 字, 101 s | `A-b.md` 3.834 字, 102 s |
| **B** | brief + khối **Thẻ giọng** (洛羽, nhân viên 疾风, nhân viên 冷雾蜥) | `brief-B.md` | `B-a.md` 2.579 字, 120 s | `B-b.md` 3.328 字, 263 s |
| **C** | anchor mục 1: ch14 → **ch16** (MC đọc thiên phú 蜜水蜂 rồi nghĩ lan man, đùa, ……, 产卵了！！) | `si-C.txt` | `C-a.md` 3.280 字, 232 s | `C-b.md` 3.498 字, 226 s |

Gemini đọc cặp: `gemini-doc-A.md` (44/44 trích thật) · `gemini-doc-B.md` (54/54) · `gemini-doc-C.md` (52/52).
Anchor C: `gemini-anchor.md` (Gemini đề xuất 5 cửa sổ, 10/10 trích thật) → chọn `gemini-anchor-cua-so/ch016-p059-chon.md`
(nguồn dòng 1907–1919, 328 字; cửa sổ 56–64 hay hơn nhưng nguồn thô có dòng rác 「小」「说」「网」 chen giữa nên
`verify_anchors` không khớp). `verify_anchors.py` 3/3, `soat_van.py` 0 ở bốn cột tật.

**Câu ĐẠT là của Tác giả — chờ Tác giả đọc.** Dưới đây là Agent đọc qua báo cáo Gemini + số đo.

## Tóm tắt: cả ba biến đều không trả lại giọng riêng

- Ở cả sáu bản, tiếng lòng MC vẫn mất **4/5** chỗ của gốc (C-a mất 5/5). Năm chỗ theo Gemini mục 2:
  骗小孩呢？！ · 一虫传三代，人走虫还在 · 我信你个鬼 · 颜狗 · câu cuối 黑奴. ！+？ trong lời kể 0,26–0,86 /1.000
  (gốc 5,31; v1 TB 0,18). Ba can thiệp đều `vo-hieu` (I-0050 0,28× · I-0051 0,75× · I-0052 0,71×).
- Nhân viên tiệm 疾风 **không có tiếng lòng ở cả sáu bản**, kể cả B (thẻ dặn "chửi một câu trong đầu").
- **Chỗ duy nhất có giọng là câu cuối** — đúng chỗ brief ghi "có một câu phản ứng trong đầu". C-a còn có một câu tự
  hỏi ở tiệm 冷雾蜥 (这究竟是…？), cũng đúng chỗ brief ghi "Cậu tự hỏi". Những chỗ brief viết "Lạc Vũ tính ra / cân /
  nhớ ra", Writer kể thành suy luận đứng đắn. 7/8 bản v2–v3 theo đúng khuôn này.
- Thinking của B và C **không nhắc thẻ giọng lần nào** và nhắc anchor 1 lần; vẫn soát phủ định/so sánh (B-b 22 lần,
  C-b 42 lần) và đếm chữ (C-b 19 lần). A (Low): AI Studio không trả khối thinking (0 ký tự).

Xếp theo mức có giọng riêng (chênh nhau nằm trong nhiễu): **B ≥ A > C**.

## Số đo (kính lúp, không chấm) — a / b

| Chỉ số | Gốc | v1 | v2 | **A** Low | **B** thẻ | **C** anchor | Khoảng 30 ch. |
|---|---|---|---|---|---|---|---|
| 字 | 2.822 | 3.646 / 2.769 | 4.180 / 4.205 | 3.322 / 3.834 | 2.579 / 3.328 | 3.280 / 3.498 | — |
| 字/đoạn | 20,9 | 34,1 / 48,6 | 55,0 / 50,1 | 61,5 / 49,2 | 43,0 / **32,6** | **91,1** / 59,3 | 19,6–33,4 |
| 字/câu | 18,4 | 33,7 / 30,4 | 34,1 / 39,4 | 35,5 / 33,7 | 32,5 / **29,7** | 36,3 / 35,5 | 14,8–29,5 |
| lượt thoại | 49 | 14 / 18 | 21 / 20 | 18 / 20 | 12 / 13 | 13 / 16 | 16,6–64,8 |
| 字/lượt | 8,7 | 19,7 / 15,5 | 12,6 / 17,0 | 16,7 / 14,9 | 17,1 / 18,2 | 23,5 / 19,0 | 6,5–27,6 |
| ！ lời kể /1.000 | 2,83 | 0 / 0,36 | 0,24 / 0,24 | 0 / 0 | 0,39 / 0,30 | 0 / 0,57 | — |
| ？ lời kể /1.000 | 2,48 | 0 / 0 | 0,24 / 0,24 | 0,30 / 0,26 | 0,39 / 0 | 0,30 / 0,29 | — |
| **！+？ lời kể** (chỉ số sổ) | 5,31 | 0 / 0,36 | 0,48 / 0,48 | 0,30 / 0,26 | 0,78 / 0,30 | 0,30 / 0,86 | — |
| dòng lời kể có ！/？ (máy) | 10 | 0 / 1 | 2 / 2 | 1 / 1 | 1 / 1 | 1 / 2 | — |
| chỗ tiếng lòng giữ được /5 (Gemini) | 5 | 0 / 0 | 1 / 1 | 1 / 1 | 1 / 1 | 0 / 1 | — |
| nhãn điềm tĩnh 淡然/平静/从容/木然/淡漠 | 0 | 5 / 2 | 0 / 1 | 0 / 0 | 0 / 1 | 1 / **3** | — |
| nhãn ngữ điệu (regex, v1/v2 đọc tay) | 0 | 3 / 1 | 2 / 3 | 1 / 3 | 2 / 2 | 1 / 4 | — |
| phủ định lặp (soat_van) | 5 | 2 / 0 | 8 / 5 | 4 / 5 | 1 / 0 | 2 / 1 | — |
| giảng huấn /1.000 | 0 | 0,82 / 0,36 | 1,91 / 1,66 | 0,90 / 0,26 | 0,78 / 0,30 | 0 / 0,86 | 0–1,0 |

Đo bằng `hieu_chuan.do()` + `soat_van.scan()`; ！/？ đếm trong lời kể sau khi bỏ phần trong “”, mẫu số = tổng chữ
Hán (như doc-v1/v2). "Chỗ tiếng lòng" dùng năm chỗ Gemini nêu ở mục 2 (doc-v2 dùng năm sự việc hơi khác nên v2 ghi
"mất 4/5" như nhau).

## A — thinking Low

- Tiếng lòng thành kể ngoài: «骗小孩呢？！» → «洛羽心头微微一哂»; «一虫传三代，人走虫还在» → «在御兽师漫长的一生里算是个
  极好的伙伴»; «洛羽承认自己是一个颜狗。» → «心里暗自承认自己挑宠兽也是看卖相的».
- Câu cuối: a «这家店连装都不愿意装一下了吗？» (hỏi nhẹ); b «这算什么……宠兽充电宝？» (đùa, gần ý «到底是在卖宠物，
  还是在卖黑奴？»).
- Nhân viên 疾风 chỉ tả ngoài: «店员手一僵，眼角猛地跳了两下» (gốc «几千条还他妈不够你挑？！»).
- Gần gốc: «998联盟币只是个首付» ~ «买虫的钱，不过是笔“首付”»; «那语气听着可一点也不像是欢迎自己回头的意思» ~ «听语气，
  可不怎么期待».
- Lỗi: a bịa hạn hợp đồng «三年» (lặp v1); cả hai mở bằng tiền kiếp + kỳ thi. Nhanh gấp đôi (~100 s); giọng như v1.

## B — thẻ giọng nhân vật

- Câu cuối có 靠 cả hai bản — **chữ lấy thẳng từ thẻ**: a «靠，这地方连活体蓄电池的买卖都做上了？！»; b «靠，这群黑心
  资本家连虾身上迸出的一丝静电都要敲骨榨髓。». b thêm «双高级天赋！» (thẻ: "thấy món hời: cảm thán ngắn").
- Phần còn lại vẫn trầm: «骗小孩呢？！» → a «心底已将这盘算盘打得噼啪作响», b «瞬间看透了其中的骨血关节»; «我信你个鬼。»
  → b «洛羽静静听着，心下了然».
- Thẻ nhân viên 疾风 ("bực thì chửi trong đầu, mặt vẫn cười") thành tả ngoài: b «硬生生把满嘴的咒骂咽回了喉咙» —
  nói là có chửi nhưng không cho đọc câu chửi.
- Thẻ nhân viên 冷雾蜥 ("như đọc thuộc") bị dịch thành nhãn: a «语调平直宛若背诵经文», b «嗓门平平，念诵着背熟的说辞».
- Được: B-a ngắn nhất (2.579 字), B-b 字/đoạn 32,6 (trong khoảng), giảng huấn thấp. Lỗi mới: cả hai làm 冷雾蜥 thành
  «水冰双系» (brief: hệ băng); b thêm «年轻女侍» và «一千零四十联盟币».

## C — anchor ch16 dày tiếng lòng MC

- Không bản nào lấy nhịp anchor (nghĩ lan man, đùa, tự hỏi dồn): «骗小孩呢？！» → a «洛羽在心中冷笑了一声。», b «心底早已
  冷笑出声»; «一虫传三代» → a «长寿基因利于长久陪伴御兽师».
- b chuyển «颜狗» thành thoại nói to: «自言自语道：“冷雾蜥看着像深青色的科莫多巨蜥，实在不讨喜。» — tiếng lòng thành lời.
- Câu cuối: a «这群大商队的掌柜真是一丁点油水都不肯放过。» (phẳng); b «这帮奸商连电费都要从宠兽身上榨出来？！».
- Tệ hơn ở hình thức: a 91,1 字/đoạn (gần gấp ba trần khoảng 33,4), b ba nhãn điềm tĩnh (神色平静 · 平静地 · 面色从容地)
  và bốn nhãn ngữ điệu (语气平淡地给出了答复 · 语气平稳地解释道 …). Nhân viên 疾风 ở a nói to thay tiếng lòng: «全都在这儿了，全岛除了我们疾风商队…».

## Đọc chung và đề xuất (chờ Tác giả)

1. Thinking thấp, thẻ giọng và anchor đều không làm Writer viết tiếng lòng ở chỗ brief không đòi. Ngược lại, chỗ nào
   brief ghi "một câu trong đầu" / "tự hỏi" thì 7/8 bản v2–v3 có. Giả thuyết kế (tầng BRIEF, một biến): giữ brief gốc,
   chỉ đổi **cách ghi các khoảnh khắc của MC** — chỗ đang viết "Lạc Vũ tính ra: …" ghi thành "một câu trong đầu cậu"
   kèm việc cậu nhận ra (không viết sẵn câu). Đây là đánh dấu chỗ, không phải giao lời thoại.
2. Thẻ giọng chỉ chuyển được **từ khoá** (靠, 双高级天赋！), không chuyển được cách nghĩ; với nhân viên, thẻ bị dịch thành
   câu tả. Nếu dùng tiếp thì dùng như một biến cộng thêm, không thay giả thuyết 1.
3. SI dán vẫn là v1; ba biến chỉ nằm trong `gemini/test-giong/v3/`, nên luật 4 của sổ (gỡ cái vô hiệu) không có gì để gỡ.

Biên độ trong sổ = max(chênh hai bản v1 = 0,36; chênh hai bản của biến). Lấy riêng chênh A (0,04) thì A ra 2,5× —
giả: tuyệt đối chỉ +0,10 so với khoảng cách 5,1 tới gốc.
