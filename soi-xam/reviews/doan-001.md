# Review đoạn 001 — vòng thử hình dạng prompt (26/10/2026)

SI v1 (`gemini/si-dan-gemini.txt`), Gemini trên AI Studio (acc sekanyuu, `/u/0`), mỗi bản một chat mới (`--new`).
Hai hình dạng prompt × 2 lần chạy để tách tác dụng của prompt khỏi nhiễu:

| Bản | Prompt | 字 | dòng | 字/dòng | ≤10字 | `X：“` | phản ứng trơ | 『』 | 【】 | ！/1k | ？/1k | cụm nhấn* | so sánh người kể | canon bàn tay vàng |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mẫu (ch.1–105) | — | 2.442 | 113 | 19 | 27% | ~14 | 10 | — | 1,8 | 25,8 | 19,0 | — | hiếm | — |
| a | tối giản | 3.047 | 202 | 17 | 28% | 44 | 11 | 20 | 5 | 57,1 | 14,4 | 20 | 0 | ❌ tự đặt `万物皆可蛀` |
| c | tối giản | 3.554 | 216 | 17 | 25% | 29 | 10 | 16 | 7 | 48,7 | 12,7 | 29 | 0 | ❌ tự đặt `概念级龋齿` + `牙菌斑` |
| b | đơn giản | 2.520 | 158 | 19 | 28% | 25 | 9 | 9 | 9 | 58,3 | 11,1 | 18 | 0 | ✅ 第1集 · 30 点 · 片尾复活 |
| d | đơn giản | 3.418 | 188 | 19 | 24% | 42 | 11 | 10 | 11 | 47,4 | 14,0 | 13 | 5 | ✅ 第1集 · 30 点 · 片尾复活 |

\* `瞬间 / 猛地 / 猛然 / 狠狠 / 轰然 / 死死`. `cong_doan.py` báo ĐỎ ở bản a vì câu cuối kết bằng `——`: bắt nhầm, đoạn dừng giữa cú lao đúng brief. Các band "chưa đạt" của `cong_doan` là band 领主, bỏ qua.

## Kết luận

- **Prompt đơn giản thắng ở canon**, cả hai lần: đúng tuổi kết khế 16, 30 收视点, 第1集, 片尾复活, kiếm 钟馗 của 唐棠, 土地公 của 马骁, 城北焚烧厂, hạn thứ Sáu.
- **Prompt tối giản để Writer tự dựng bàn tay vàng**, hai lần đều ra năng lực "làm sâu mọi thứ" và mượn chữ `概念` của mẫu; bản c còn đảo vai (马骁 thành 队长, 唐棠 thành 突击手) và lọt `天佑大夏` (tên nước trong 《斩神》). Giọng của hai bản này lại sống nhất (bản a: bác sĩ… → `两千八百块钱你让我讲什么义气？！`).
- **Lỗi chung cả bốn bản:**
  - `！` gấp ~2 lần mẫu.
  - Tỷ lệ thoại thấp hơn mẫu.
  - 13–29 cụm nhấn mỗi bản.
  - Ba bản quá dài (3.047–3.554 字, cửa sổ 2.000–2.400).
  - Mở đoạn bằng một khối kể tiểu sử dài 20–40 dòng.
- **Chọn gốc:** khuyến nghị **bản b** (độ dài đúng, canon đúng, 0 so sánh người kể); bản d có đoạn 齐乐 tính thiệt hơn ngay trước khi lao vào hay hơn b, nhưng lỗi so sánh người kể (`像是拿墨汁涂上去的`, `像一颗脱膛的人肉炮弹`, `如同一群…毒蛇`) và sai canon `只播了三集`.

## Lỗi canon / chi tiết từng bản

- a: kết khế "十八岁"; 唐棠 dùng `符文短刀`; 马骁 gọi `唐姐`; lương 2.800.
- b: một chữ `通` thừa đầu dòng 123 (lỗi Writer); lý lẽ "马骁一死…复评必然取消" rối; 马骁 gọi `唐队`.
- c: đảo vai 唐棠/马骁; `天佑大夏`; năng lực tự đặt; lương 3.500.
- d: phim "只播了三集" (canon: 26 tập); "1998重制版"; 5 so sánh người kể; dòng kết nhắc `精神病院`.

## Ý Writer tự đặt, đáng trình Tác giả

- 蛀牙大王 ngủ trong **chiếc răng hàm** của 齐乐, tỉnh dậy kèm cơn đau răng (a, c tự nghĩ ra, độc lập).
- Thông báo 【】 hiện như **chữ ghép bằng hạt kẹo / phụ đề** trên võng mạc (b, d).

## Đề xuất cho vòng sau (chưa áp dụng)

1. Giữ prompt đơn giản; thêm một câu sự thật "phim chiếu 26 tập thì bị cắt".
2. Ghi độ dài như cửa sổ ở đầu prompt và đặt đích thấp hơn (~1.900) vì Writer vượt.
3. Mở đoạn bằng việc đang xảy ra trong B2, tiểu sử 齐乐 để rải vào thoại (黄金三章: 300 字 đầu có người gặp nguy).
4. SI: hạ mật độ `！` (anchor đang dạy đúng, nhưng dòng LENGTH cần nói nhịp `！` theo cảnh) — cần Tác giả duyệt trước khi sửa.

**Kết luận review:** chưa chốt bản nào. Bản b là gốc khuyến nghị; chờ Tác giả đọc và chọn.

---

# Vòng 2 — SI v2 (bỏ thoại kiểu kịch bản) + prompt đơn giản v2

Tác giả 26/10: `X：“…”` chỉ dùng ở cảnh đặc định, bỏ đi. SI v2 đổi anchor 2–3 (ch.66, ch.29) và dòng LENGTH; prompt v2 thêm "26 tập", độ dài 1.800–2.200 (nhắm 1.900), mở thẳng vào lúc 第七组 bước ra.

| Bản | SI | thoại kịch bản thuần `名字：“` | thẻ thoại tách dòng (`道：`↵`“…”`) | 字 | ！/1k | cụm nhấn | so sánh người kể |
|---|---|---|---|---|---|---|---|
| a / b / c / d | v1 | 24 / 12 / 16 / 36 | — / 6 / — / — | 3.047–3.554 | 47–58 | 13–29 | 0–5 |
| e | v2 | 0 | 22 | 2.792 | 40,1 | 13 | 0 |
| f | v2 | 0 | 11 | 2.577 | 40,0 | 11 | 0 |
| mẫu | — | ít, chỉ ở cảnh cãi nhanh | ~0,4/chương | 2.442 | 25,8 | — | hiếm |

- **Đạt:** thoại kịch bản về 0 cả hai lần; `！` giảm 58 → 40; tiểu sử 齐乐 đi qua lời 马骁 thay vì khối kể đầu đoạn; "26 tập" đúng.
- **Tật mới:** thẻ thoại đứng riêng một dòng rồi câu nói xuống dòng — 11–22 lần/đoạn (mẫu ~0,4/chương). Chưa sửa SI.
- **Còn lệch:** vẫn vượt độ dài (2.577–2.792 khi nhắm 1.900); e cho kích hoạt 片尾复活 trừ 10 点 (canon: không tốn); `概念` vẫn lọt 1 lần/bản (anchor 4 có chữ `概念能力`).

**Tác giả 26/10 sau vòng này: đổi cốt truyện, 蛀牙大王 "nghe low quá".** Các bản a–f giữ làm bằng chứng đo SI; canon của chúng bị thay khi tiền đề mới được chốt.

---

# Vòng 3 — vỏ mới 特摄 (曜) · SI v3 · `briefs/doan-001-tokusatsu.md`

Tác giả 26/10 chọn hướng 1 (anh hùng 特摄 bị lãng quên). SI v3: ROLE/PRINCIPLE 4 đổi sang luật 特摄, thêm "thẻ thoại cùng dòng với câu nói".

| Bản | 字 | 字/dòng | ！/1k | thoại kịch bản thuần | thẻ tách dòng | cụm nhấn | so sánh | lỗi canon |
|---|---|---|---|---|---|---|---|---|
| e (v2, vỏ cũ) | 2.792 | 17 | 40,1 | 0 | 22 | 13 | 0 | — |
| f (v2, vỏ cũ) | 2.577 | 17 | 40,0 | 0 | 12 | 11 | 2 | — |
| **g** (v3) | 3.425 | 21 | **24,2** | 0 | **5** | 18 | 1 | ❌ 齐乐 xuyên không từ 地球, "上辈子在孤儿院"; đèn đỏ ở 2:30 (canon 2:00) |
| **h** (v3) | 3.199 | 16 | 33,4 | 0 | 6 | 21 | 2 | ✅ |
| mẫu | 2.442 | 19 | 25,8 | ít | ~0,4/chương | — | hiếm | |

- **Đạt:** thẻ thoại tách dòng 12–22 → 5–6; `！` của g xuống bằng mẫu; thoại trọn câu, 马骁 kể chuyện 复评 bằng lời của mình; giọng 曜 đúng thiết kế (`任何危害人类和平的存在，皆为怪兽！` · `长着电缆和锈铁的怪物，就是机械合成兽！`); cả hai dừng đúng ở tiếng hô 「光甲——着装！」.
- **Ý Writer tự đặt, đáng trình Tác giả:** g — "第1集 thiếu kinh phí kỹ xảo nên đèn đỏ sớm", "đạt điểm xấu hổ mới biến hình được" (`羞耻度判定`); h — 齐乐 là fan 特摄 hay lùng băng cũ ở chợ đồ cũ; 马骁 hay lén dúi đùi gà cho 齐乐 (lý do để lao vào).
- **Còn lệch:** vẫn vượt độ dài (3.199–3.425 khi nhắm 1.900); cụm nhấn 18–21; brief thiếu dòng "齐乐 sinh ra ở thế giới này" → g tự cho xuyên không.
- **Chọn gốc:** khuyến nghị **h** (canon sạch). g có thoại hay hơn nhưng phải bỏ vì lỗi xuyên không.

---

# Vòng 4 — nội dung mới (MC xuyên việt + phân thân điên) · SI v4 · `briefs/doan-001-phan-than.md`

Tác giả 27/10: giữ SI và thế giới, ai cũng thức tỉnh; MC xuyên việt, phân thân tính cách tâm thần cực độ, MC chỉ muốn sống yên. SI v4 chỉ đổi ROLE, PRINCIPLE 4, một dòng FIXED CONVENTIONS. Bản i chạy lần đầu gặp `Failed to generate content` (lỗi tạm), chạy lại y nguyên thì ra.

| Bản | 字 | 字/dòng | ！/1k | thoại kịch bản thuần | thẻ tách dòng | 【】 | cụm nhấn | so sánh |
|---|---|---|---|---|---|---|---|---|
| i | 3.161 | 19 | **25,6** | 0 | 9 | 4 (màn hình đồng hồ, hồ sơ) | 15 | 1 |
| **j** | **2.375** | 17 | **24,0** | 0 | 4 | 8 (đồng hồ, nhãn hộp) | 19 | 1 |
| mẫu | 2.442 | 19 | 25,8 | ít | ~0,4/chương | 1,8 | — | hiếm |

- **Đạt:**
  - `！` bằng mẫu ở cả hai bản; j lần đầu vào cửa sổ độ dài.
  - Giọng 齐乐 sống: nước kỷ tử, 「心若冰清，天塌不惊」, "活王八 ba năm", đồng hồ nhịp tim leo `98 → 115 → 127`.
  - Phân thân điên đúng hồ sơ: i `爹来陪你玩通宵了` + 大鹏展翅; j `老子来陪你玩捉迷藏了` + trượt vào khe cửa.
  - Thoại cùng dòng với thẻ.
- **Cả hai bản tự đi tới cùng một cái kết:** 唐棠 tưởng "小齐" xả thân, quay lại thấy 齐乐 thật đứng sau quầy với cốc nước nóng, nhịp tim 135–138. j: `那个……如果我说，刚才跳进去的那个神经病真不是我，你信吗？`
  - **Đây là quyết định canon của Tác giả:** bible đang ghi "người ngoài không phân biệt được hai đứa" và 齐乐 giấu năng lực; cái kết này cho 唐棠 biết có hai 齐乐 ngay đoạn 1.
- **Lệch canon / chi tiết:**
  - i tự nói nguồn gốc phân thân ("灵魂撕裂留下的后遗症") như sự thật (bible: để mở).
  - i cho phân thân từng ra một lần ba năm trước khi xem phim kinh dị (bible: 0 lần) — chi tiết hay, có thể nhận.
  - i dùng `异变者` thay cho 契主.
  - j cho phân thân đạp lõm mặt quầy gỗ (sát mép 一阶).
  - Cả hai in màn hình đồng hồ / nhãn hộp bằng `【】`; không có hệ thống nên chấp nhận được, nhưng ghi để theo dõi.
- **Chọn gốc:** khuyến nghị **j** (đúng độ dài, chặt, câu chốt đắt); i có phần mở dài hơn và gag tốt (`神态安详得能直接送去火化`) nếu Tác giả muốn mở chậm.
