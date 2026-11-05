# Đọc bài hiệu chuẩn v4 — ch3, ba bản SI sửa người kể

Nền: brief gốc `chung/hieu-chuan/than-sung/ch03/brief.md` · thinking High · hai chat mới mỗi bản (AI Studio, 05/11/2026,
`jobs-v4-ch03.json`). Lý do dựng ba bản: `phan-tich-si-v1.md`.

| Bản | So với SI v1 | SI | Bản a | Bản b |
|---|---|---|---|---|
| **E** | + khối VÍ DỤ: brief mẫu ch2 → nguyên văn ch2 | `si-E.txt` (10.612) | `E-a.md` 3.104 字, 266 s | `E-b.md` 3.537 字, 266 s |
| **N** | sửa người kể: thêm mục 2 "lời kể là cái đầu của MC", mục 1 bỏ "storyteller reports", BANS dòng 2 | `si-N.txt` (6.168) | `N-a.md` 3.239 字, 264 s | `N-b.md` 3.564 字, 244 s |
| **EN** | cả hai | `si-EN.txt` (11.312) | `EN-a.md` 3.645 字, 229 s | `EN-b.md` 3.642 字, 239 s |

Bridge dán đủ SI dài (không báo lỗi dán); cổng máy XANH cả sáu bản. Gemini đọc cặp: `gemini-doc-E.md` (54/54 trích
thật) · `gemini-doc-N.md` (44/44) · `gemini-doc-EN.md` (49/49).

**Tác giả đã đọc (05/11): "Đều không đạt. Tìm cách khắc phục đi"** — cả ba bản không ĐẠT. Dưới đây là phần đo.

## Tóm tắt: sửa người kể trong SI chỉ nhích được câu cuối

- **Không bản nào có một câu ngôi một (我) trong lời kể** (gốc: «我信你个鬼。»). Tiếng lòng MC mất 3–5/5 chỗ; chỗ giữ được
  chỉ là **câu cuối** (đúng chỗ brief ghi "một câu phản ứng trong đầu") và từ 颜控 thay 颜狗. ！+？ lời kể TB: E 0 ·
  N 0,44 · EN 0,41 (v1 0,18; gốc 5,31). Ba can thiệp đều `vo-hieu`: I-0053 0,5× · I-0054 0,72× · I-0055 0,64×.
- **Ví dụ ch2 trong SI bị bỏ qua hẳn**: 0 dấu ch2 (占卜|珍珠|奶牛|虎鲸|星贝|面包|八刀流|渔晚) ở cả sáu bản; trùng 7-gram duy nhất
  là thuật ngữ 培育资质考核 (có cả ở N, vốn không có ví dụ). Không rò (E-CANON-05 = 0), nhưng cũng không học được giọng.
- **Luật viết ra thắng ví dụ**: E giữ nguyên BANS dòng 2, thinking E soát phủ định/so sánh 69/60 lần và tự nhắc
  "comparisons in the narration are moved into the protagonist's direct speech". Sửa câu đó (N, EN) làm thinking bớt
  soát (N 18/26, EN 6/2) — chú ý được giải phóng, nhưng không chuyển thành tiếng lòng.
- Nhân viên tiệm 疾风 **không có tiếng lòng ở cả sáu bản** (gốc «几千条还他妈不够你挑？！来挑事的吧！»).

Xếp theo mức lời kể nói bằng giọng nhân vật (chênh nhau nằm trong nhiễu): **EN ≥ N > E**.

## Số đo (kính lúp, không chấm) — a / b

| Chỉ số | Gốc | v1 | **E** ví dụ | **N** người kể | **EN** cả hai | Khoảng 30 ch. |
|---|---|---|---|---|---|---|
| 字 | 2.822 | 3.646 / 2.769 | 3.104 / 3.537 | 3.239 / 3.564 | 3.645 / 3.642 | — |
| 字/đoạn | 20,9 | 34,1 / 48,6 | 36,1 / **63,2** | 45,0 / 60,4 | 35,0 / 40,0 | 19,6–33,4 |
| 字/câu | 18,4 | 33,7 / 30,4 | 32,6 / 36,6 | 32,7 / 38,4 | 38,8 / 38,9 | 14,8–29,5 |
| lượt thoại | 49 | 14 / 18 | 13 / 14 | 16 / 15 | 12 / 13 | 16,6–64,8 |
| 字/lượt | 8,7 | 19,7 / 15,5 | 22,9 / 20,0 | 14,2 / 19,8 | 19,2 / 19,9 | 6,5–27,6 |
| ！ lời kể /1.000 | 2,83 | 0 / 0,36 | 0 / 0 | 0,31 / 0,28 | 0,27 / 0,27 | — |
| ？ lời kể /1.000 | 2,48 | 0 / 0 | 0 / 0 | 0 / 0,28 | 0,27 / 0 | — |
| **！+？ lời kể** (chỉ số sổ) | 5,31 | 0 / 0,36 | **0 / 0** | 0,31 / 0,56 | 0,55 / 0,27 | — |
| dòng lời kể có ！/？ (máy) | 10 | 0 / 1 | 0 / 0 | 1 / 2 | 1 / 1 | — |
| chỗ tiếng lòng giữ được /5 | 5 | 0 / 0 | 0 / 0 | 2 / 1 | 2 / 1 | — |
| **câu 我 trong lời kể** (mới) | 1 | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — |
| câu có 我\|自己 ngoài “” (mới) | 5 | 5 / 3 | 3 / 4 | 2 / 2 | 3 / 6 | — |
| **câu thuật lại việc nghĩ** (mới) | 1 | 6 / 4 | 4 / 6 | 3 / 3 | **0** / 3 | — |
| nhãn điềm tĩnh 淡然/平静/从容/木然/淡漠 | 0 | 5 / 2 | 1 / 0 | 1 / 0 | 0 / 1 | — |
| nhãn ngữ điệu (regex) | 0 | 0 / 0 | 0 / 1 | 1 / 1 | 0 / 2 | — |
| phủ định lặp (soat_van) | 5 | 2 / 0 | 3 / 0 | 0 / 0 | 0 / 4 | — |
| giảng huấn /1.000 | 0 | 0,82 / 0,36 | 0,64 / 0,57 | 0,93 / **1,12** | 0 / 0,82 | 0–1,0 |
| thinking soát phủ định/so sánh (grep) | — | — | 69 / 60 | 18 / 26 | 6 / 2 | — |

Đo bằng `hieu_chuan.do()` + `soat_van.scan()` như v3. Hai cột mới: "câu có 我|自己" phần lớn là 自己 phản thân ngôi ba
(«自己转头肯定会…»), nên cột **câu 我** mới là ngôi một thật; "thuật lại việc nghĩ" = câu lời kể có
心里|心底|心中|意识到|明白|暗想|思忖. "Chỗ tiếng lòng" dùng năm chỗ như v3 (骗小孩呢？！ · 一虫传三代，人走虫还在 ·
我信你个鬼 · 颜狗 · câu cuối 黑奴); 颜控 tính là giữ (cùng lớp từ mạng với 颜狗).

## E — ví dụ brief → văn ch2 trong SI

- Năm chỗ mất cả hai bản. Gốc «骗小孩呢？！» → a «洛羽在心底飞快拨拉着算盘», b «洛羽心底迅速拨弄着算盘»; «洛羽承认自己是一个
  颜狗。» → a «同样是个讲究长相的人», b «其实也极为看重相貌».
- Câu cuối phẳng: gốc «到底是在卖宠物，还是在卖黑奴？» → a «透着一股说不出的古怪»; b thành **thoại nói to** «“这帮岛上的大商人，
  榨取变异兽的手段真是一个比一个狠。”» — tiếng lòng biến thành lời.
- Ví dụ không để lại dấu nào (0 rò), còn BANS cũ thì có: thinking soát phủ định/so sánh nhiều nhất trong mọi bản đã chạy.
- Canon: a «冷雾蜥属于水冰双系» (gốc «冰系», lặp lỗi v3 B); b thêm «十五岁的洛羽», «御兽师管理局每月举行的培育资质考核».
  E-b 63,2 字/đoạn, gần gấp đôi trần khoảng.

## N — sửa người kể

- Câu cuối có giọng ở b: «这帮黑心肝的狗商贩，合着是拿活宠兽当免费蓄电池在死命吸血啊！» (gốc «大航海时代特色是吧！»); a thành phẫn nộ
  luân lý «这帮商人当真是什么丧尽天良的买卖都做得出来！» — có ！ nhưng mất cái đùa.
- a giữ được từ mạng: «洛羽在心底暗暗承认自己挑宠兽也是个实打实的颜控。» (b «注重卖相的俗人»).
- Chỗ khác vẫn thuật lại việc nghĩ: «骗小孩呢？！» → a «洛羽心头暗自冷笑», b «洛羽心底默默盘算了一番，暗自冷笑»; «我信你个鬼。» →
  a «心中立刻了然», b «心头早已明了就里».
- Nhân viên 疾风: a tả ngoài «硬生生把难听的话压在了牙缝里»; b **nói to** thay tiếng lòng «全岛顶好的货色尽数在此，客人若是瞧不上…».
- Canon/giọng: bịa hạn hợp đồng a «五年期», b «三年期满» (lặp v1/v3 A); MC a đáp cộc «讲。», «语气平静»; giảng huấn b 1,12 vượt khoảng.

## EN — cả hai

- Câu cuối có giọng **cả hai bản**: a «胸口蓦地腾起一声冷笑——合着这儿卖的虾，进门先当蓄电池使？！», b «居然连大虾放个屁都要把电量给充进
  电池里去！» (gốc «到底是在卖宠物，还是在卖黑奴？»). a giữ «他坦然承认自己骨子里是个实打实的颜控。».
- EN-a là bản duy nhất 0 câu thuật lại việc nghĩ và 0 giảng huấn theo regex — nhưng «我信你个鬼。» → a «思绪已然理顺了七八分»,
  b «心下却是一阵明晰»; «一虫传三代» mất cả hai.
- Thinking EN-a tự ghi "the benchmark style of weaving first-person introspection into third-person storytelling" — biết
  đích, nhưng bản ra 0 câu 我.
- Tệ ở chỗ khác: mở bằng giảng thế giới a «海啸淹没了整片陆地的灾后纪元», b «大雨季彻底淹没了旧时代的大陆»; câu dài nhất (38,8/38,9
  字/câu); thoại MC trang trọng a «“多谢引荐，在下手头并不拮据，打算现款结清。”» (gốc «“不用，我不差钱。”»); b thêm tên thiên
  phú thường «【厚实外皮】、【微弱嗅觉】».

## Đọc chung

1. Năm bản SI (v1, v2, E, N, EN) × 2 lần: ngôi một trong lời kể vẫn 0, tiếng lòng chỉ ra ở câu cuối. Ví dụ trong SI
   không được dùng; sửa câu chữ về người kể chỉ bớt việc soát BANS. Tầng SI coi như đã thử hết với brief này.
2. Chỗ có giọng ở cả bốn bản N/EN trùng chỗ brief đánh dấu "một câu phản ứng trong đầu" — cùng kết luận v3.
   Phiên chính đã chuyển sang **v5, sửa ở tầng prompt, SI giữ v1** (`../v5/README.md`).
3. SI dán vẫn là v1; E/N/EN chỉ nằm trong `v4/`, nên luật 4 của sổ (gỡ can thiệp vô hiệu) không có gì để gỡ.

Biên độ trong sổ = max(chênh hai bản v1 = 0,36; chênh hai bản của biến) như v3 — chênh hai bản E bằng 0 nên không chia
được nếu lấy riêng. Chênh N 0,25, EN 0,28.
