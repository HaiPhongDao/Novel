# Truyện vô não sảng văn (爽文) — dựng từ một bộ mẫu

Dùng khi Tác giả xin **truyện dễ viết, đọc cho sướng**, hoặc nói thể loại đang làm đã chán. Khác hẳn nhánh 领主/Tây huyễn: ở đó SI cấm đoạn cụt, cấm hệ thống, cấm số to — ở đây **chính những thứ đó là động cơ**. Bê SI cũ sang là hỏng ngay từ chương 1.

## 1. Đo bộ mẫu trước khi viết một chữ

Mẫu Tác giả tải lên nằm trong một thư mục riêng ở repo (ví dụ `vo-dich/`), thường là một file `.txt` rất lớn. Đọc **chương 1–3** rồi lập bảng dấu hiệu, đừng đọc cảm tính:

```bash
python - <<'EOF'
import re
t = open(r"<file mẫu>", encoding="utf-8", errors="ignore").read()
print(len(t), re.findall(r"第[0-9一二三四五六七八九十]+章", t)[:5])
print(t[t.find("第1章"):t.find("第1章")+1800])
EOF
```

Bảng dấu hiệu cần ghi (số đo thật của mẫu `全球游戏：我开挂无敌`, 301 chương / 703k 字):

| dấu hiệu | mẫu | cách đo trên bản mình |
|---|---|---|
| đoạn rất ngắn, có đoạn một cụm (实际上。/接着。) | ~15 字/đoạn | số đoạn, chữ Hán/đoạn, số đoạn ≤10 字 |
| dòng hệ thống 【】 đứng riêng, xếp chồng | 30+ dòng/chương | `len(re.findall(r"【[^】]+】", body))` |
| con số leo thang trong một chương | 725 → 44.500 → 100.000 | bắt các cú `X → Y` và số lớn |
| vòng lặp: tiêu tài nguyên → nổ → quét → nhặt → tiêu tiếp | mỗi chương một vòng | có đủ 4 pha trong chương không |
| 捧哏 hét thay độc giả (我靠！/这也行？) | có | số câu hét của nhân vật phụ |
| MC một câu tỉnh bơ rồi hành động | có | số câu châm (1–3/chương) |
| đổi POV sang nạn nhân vài dòng cho buồn cười | có | đoạn ngắn vào đầu quái/địch |
| hook cuối chương = thứ to hơn xuất hiện (boss, hộp, bảng xếp hạng) | có | câu cuối chương |
| cấu trúc dài: mỗi arc một loại phó bản/thế giới mới | 301 chương = nhiều arc | dàn ý có nguồn ý mới vô hạn không |

## 2. Viết SI bằng cách đảo ngược

Cấu trúc hiệu quả: **RHYTHM → THE ENGINE → ALLOWED HERE → FORBIDDEN → LANGUAGE**, và viết ALLOWED trước FORBIDDEN vì đây là thể loại cần bật, không phải cần chặn.

| việc | SI 领主/Tây huyễn | SI 爽文 |
|---|---|---|
| đoạn cụt, câu một cụm | cấm (mất nhịp đọc) | **cho phép**, dùng để đổi nhịp |
| hệ thống / bảng / giọng trong đầu | cấm tuyệt đối | **bắt buộc**, dòng 【】 đứng riêng |
| số to, dấu chấm than | cấm | **bắt buộc**, mỗi ~300 字 một lần đổi số |
| tả cảnh, hồi tưởng, do dự đạo đức | cần chất liệu đời sống | **cấm** — mỗi đoạn phải đổi được gì đó |
| MC một câu rồi thôi | cứng, thiếu tin | **đúng ý**: một câu, tỉnh bơ, rồi làm |
| đổi POV | cấm (close-third) | cho phép 3–4 dòng vào đầu địch |
| nhân vật phụ | người có việc riêng | **捧哏**: hét lên điều độc giả đang nghĩ, và hỏi để hệ thống có cớ giải thích (thay vì tác giả giảng) |

Ba luật cứng của SI 爽文, viết khẳng định:

1. Đoạn dài là lỗi, đoạn tả cảnh là lỗi, đoạn giải thích thế giới quá ba dòng là lỗi.
2. Cứ ba trăm chữ phải có một thứ đổi: một con số, một phẩm giai, một cái xác. Không đổi thì cắt.
3. MC không được thua quá một đoạn. Kết chương đúng lúc thứ to hơn xuất hiện.

## 3. Bible tối thiểu — động cơ thay cho thế giới

爽文 không cần bible sâu; nó cần **một cỗ máy sinh 爽点** định nghĩa rõ như một nền kinh tế:

- Bàn tay vàng viết thành **công thức tiêu–nhận** (ví dụ 【百倍返还】: thứ MC tự tay tiêu trong phó bản được trả lại ×100; không tiêu thì không có gì). Hệ quả bắt buộc: **tính cách MC phải là kẻ dám tiêu sạch** — đó là luật truyện, không phải sở thích.
- Nhân vật: MC + một 捧哏 + một phản diện giai đoạn (bị đánh ba chương một lần và loan tin MC mạnh). Không thêm.
- Thế giới: ba dòng sự thật (vì sao có phó bản, sức mạnh mang về thực tại bị giảm bao nhiêu, ai quản). Phần còn lại để phó bản tự nói.
- Đơn vị: chốt tên tiền/điểm và tỷ lệ ngay trong bible, vì chương nào cũng có số.

## 4. Dàn ý = vòng lặp, không phải cốt truyện

Mỗi chương một vòng, cùng một khuôn, đổi phó bản và món đồ:

```
sự cố ở thực tại (còi báo động / quái vào phố)
→ vào phó bản, chọn độ khó cao nhất (có lý do bằng số)
→ tiêu sạch vốn liếng → hệ thống báo 返还/kích hoạt
→ nổ sức mạnh, quét sân, con số nhảy ≥3 lần
→ có kẻ khác nhìn thấy và ngơ ngác → MC một câu
→ hook: boss / hộp thưởng / bảng xếp hạng
```

Dàn ý dài hạn: mỗi arc một loại phó bản mới (sinh tồn → 魔法 → 宇宙 → 修 tiên…). Đó là cách bộ mẫu chạy 301 chương mà không cạn ý; chép nguyên cách đó.

## 5. Prompt chương

- Cùng luật "không có câu tiếng Trung nào trong prompt": nêu số liệu và nội dung dòng hệ thống bằng tiếng Việt, để Writer tự render 【】.
- Ghi rõ: độ dài **1.900–2.200 字**, ≥3 cú nhảy số, ≥1 câu châm của MC, ≥1 dòng hệ thống, 1 đoạn ngắn đổi sang đầu quái cho buồn cười.
- Nêu cớ hành động cho từng bước (vì sao chọn 地狱: tỉ lệ rơi đồ ×10; vì sao tiêu sạch 10 点: để 10 点 cũng bằng chết). 爽文 không cần logic sâu, nhưng cần **một lý do bằng số** cho mỗi quyết định.

## 6. Chấm bản 爽文 — đừng dùng band của 领主

`tools/cham_doan.py` có band cho văn 领主 (chữ/câu 20–34, lượt thoại 10–22). Bản 爽文 ra **~15 字/đoạn** và hàng chục đoạn cụt nên sẽ bị chấm oan. Chấm bằng bảng dấu hiệu ở mục 1, và đọc trực tiếp bản thảo.

Số đo một bản đạt (mẫu tham chiếu): 2.086 字 · 139 đoạn · 15 字/đoạn · 48 đoạn ≤10 字 · 32 dòng 【】 · cú nhảy `10 → 0 → 1.000 → 0 → 12.400` · 22 câu thoại · hook boss + 【首杀奖励：S级宝箱】.

## 7. Nhánh 骑砍面板 (Mount & Blade) — khác 爽文 ở chỗ bảng là SỔ

Cùng là truyện có hệ thống, nhưng mẫu 骑砍 (`领主：我用骑砍系统肝经验`) chạy bằng một cơ chế khác hẳn 爽文: bảng **không nói**, không thưởng tức thì, chỉ ghi tiến độ. Dấu hiệu để dựng lane này:

| dấu hiệu | mẫu | cách viết |
|---|---|---|
| bảng là sổ, không phải giọng nói | 【宿主：…（3阶 489/500）（无爵位）】· 【技能：精通.骑士八技(494/500)】· 【士兵：二阶.500…(495/500)】· 【士气：69/100】· 【数量上限：500】 | mỗi dòng một mục, có bậc + tiến độ x/100 + thân phận; SI cấm hệ thống nói chuyện, đùa, hiến kế |
| cày có giá nhìn thấy được | 4.700 khúc củi đổi 11 điểm, rách tay bốn lần | nói rõ ba tháng đổi được bao nhiêu điểm **và đổi bằng cái gì** (chai tay, vai rách, ăn ít) |
| lính theo bậc + trần quân số | 农奴 → 民兵 → 步兵/弓箭手; 【数量上限】 | trần quân số là phần thưởng của chương, không phải chi tiết trang trí |
| trận đánh cụ thể | địa hình, cửa chuồng làm khiên, răng sói cắn bắp chân, garo bằng dây đai | một hiệp một đoạn, 3–5 câu; thắng bằng địa hình và sai lầm của địch, không bằng khẩu hiệu |
| 敌方构成 hiện số | 【侦测到敌对武装：黑林劫掠者（17人）】【敌方构成：1阶×14，2阶×3】【部队：0/10】 | hook bằng **thành phần quân địch**, không bằng lời đe |
| MC không phép | khe phép 1/2000, đá nghiệm không lên tia lửa | nói rõ hắn đã thử và trượt, để sau này không ai hỏi "sao không dùng phép" |

**Giọng của mẫu — đo, đừng đoán.** Trên cả 886 chương dùng được: `说道` 2,2/chương, `问道` 1,0, `笑道` 0,5 (thẻ thoại là chuẩn, 23% số dòng là thoại); `他罗伯森老爷` 1,35/chương (MC tự gọi mình bằng 老爷 với người đọc), câu hỏi cho người đọc 0,79/chương, `毕竟` 1,12, `要知道` 0,50. Nên **cấm thẻ thoại là bỏ mất register**, và muốn có giọng châm thì phải ghi hạn mức đếm được vào PART 2.

**Cỗ máy hài: hai cuốn sổ.** Sổ công khai (lời đạo nghĩa trước mặt quý tộc) và sổ riêng (exp, mạng, đường rút) — người kể thuật lại lời nói công khai rồi nói hộ con số anh ta đang đếm, không gọi anh ta là đạo đức giả. Thiếu vế thứ hai thì bản ra thành biên bản tác chiến dù nhịp và số đo đều khớp mẫu.

**Khác mẫu có chủ đích:** mẫu cho MC làm con trai thứ nam tước với 500 nông nô sẵn. Nếu Tác giả muốn **bắt đầu từ dân thường** (đúng cảm giác chơi Mount & Blade) thì MC không họ, không đất, không ai bảo kê; mở chương bằng một lưỡi rìu và ba tháng cày một kỹ năng — mọi thứ về sau mua bằng số.

Ngưỡng chương — **đo lại từ toàn bộ mẫu, đừng lấy từ hai chương**: 886 chương dùng được, trung vị **2.122 字** (min 2.010); câu **23,9 字**; **20 lượt thoại/chương**, 22,4 字/lượt; 65% dòng ≤30 字; **dòng bảng `【】` chỉ 0,06/chương** (51 dòng/886 chương, dồn vào ch1–20), dòng exp `“叮！…经验加300。”` 0,05/chương — bảng được **kể** nhiều hơn **in**. Đòi "≥3 khối bảng mỗi chương" là bịa theo hai chương đầu và làm bản ra khác mẫu; ngưỡng đúng là **1–2 lần in bảng, vài lần nhắc bảng, kết chương bằng một kẻ địch to hơn**. Đây là **mốc để so**, không phải trần phải ép: khi Tác giả viết theo đơn vị đoạn thì độ dài do số beat quyết định (SKILL.md mục 4).

Bảng cấp bậc của thế giới mẫu để tham chiếu: 1–3 阶 青铜, 4–6 白银, 7–9 黄金, 传奇; nam tước = 3–4 阶; lính 一阶农奴 → 二阶民兵 → 三阶步兵/弓箭手 → 四阶熟练步兵/熟练射手. Chương 1 của mẫu mở bằng năm đoạn giảng thiết lập trước khi có người gặp nguy — **vi phạm 黄金三章, đừng chép cách mở** (xem SKILL.md mục 8).

## 8. 赋形 — khi Tác giả chê sức mạnh vô lý thì đổi LUẬT THÂN THỂ, không đổi câu chữ

Lỗi hay gặp ở nhánh 全球游戏/副本: MC là người thường mà đấm xuyên tường bê tông, và Tác giả gọi đúng tên nó — vô lý. Sửa ở tầng thế giới, không phải tầng văn:

- **Vào phó bản thì bị gán hình, không giữ hình người.** Gán loài theo độ khó: càng khó, loài càng yếu và càng lệch (F gán sói/gấu, S gán giun/kiến/nòng nọc).
- **Sức mạnh là giải phẫu học**: nanh, vuốt, vỏ, cánh, mang, nọc, khối lượng. Mỗi bậc mạnh là một bộ phận mọc ra, trả bằng điểm, nhìn thấy được.
- **Chỉ cái đầu đi theo.** Con vật khác hoảng thì chạy, hắn hoảng thì tính — đó là toàn bộ lợi thế và đủ để biện minh cho chuỗi thắng.
- Ra ngoài trở lại hình người, chỉ một phần đọng lại (血脉). Chết trong phó bản là chết thật.

Số đo một bản đạt sau khi áp luật: 盲眼蝾螈 9,6 cm / 11 g / 力量 0.1 → 再生+100 (đuôi mọc trong một nhịp thở) → 酸腺+100 (tan xác 巨蚺 ba mét) → 1.000 → 12.400 点 → hook: đồng đội bị đại bàng tha + 三阶领主.

Áp luật này thì SI phải có mục **BODY RULE** riêng và câu cấm tuyệt đối: trong phó bản không nắm đấm, không đá, không võ thuật người, không kiếm mua sẵn.

## 9. Mẫu Tác giả đưa có thể hỏng — đọc được gì mô phỏng nấy, và nói rõ

File mẫu thường là `.txt` rất lớn, Tác giả tải về Desktop hoặc bỏ vào một thư mục trong repo (khi ở repo thì `git pull` trước rồi tìm). Trước khi lập bảng dấu hiệu:

- Đếm tiêu đề chương và **soát chỗ trống**: một mẫu có 977 đề mục nhưng phần lớn thân chương ghi `下载失败：未在响应中找到` — chỉ chương 1 và 8 đọc được.
- **Nhưng đừng tin ghi chép cũ về mẫu "hỏng": đo lại bằng script trước khi tin.** Một mẫu từng được ghi là "chỉ đọc được ch1 và ch8" thực tế có 886/935 chương dùng được (49 chương mất thân). Đo ba số: số tiêu đề, số chương có thân <800 字, số chương chứa `下载失败`.
- **Số chương trong file tải về có thể lặp và nhảy loạn trong khi nội dung vẫn liền mạch một truyện** (935 tiêu đề nhưng chỉ 274 số chương duy nhất). Kiểm bằng tần suất tên MC rải đều các khối, và tham chiếu chương bằng **số + tên chương** trong mọi review/anchor, đừng bằng số chương.
- Đọc hai chương còn nguyên (một đầu, một giữa) là đủ lấy dấu hiệu; đừng mô phỏng theo phần đã mất.
- Nói thẳng với Tác giả file hỏng ở đâu, mô phỏng trên chương nào, rồi **chép bản gốc vào thư mục truyện** (`<truyen>/mau-tham-khao.txt`) để session sau không phải đi tìm lại.

## 10. Bẫy

- **Bê SI cũ sang thể loại mới.** SI 领主 cấm đoạn cụt và cấm hệ thống — hai thứ 爽文 sống bằng. Viết SI mới từ bảng dấu hiệu của mẫu, đừng sửa SI cũ.
- **Viết 爽文 mà vẫn "có chiều sâu".** Thêm do dự, thêm nhân quả xã hội, thêm nhân vật có lý lẽ riêng là quay lại đúng cái Tác giả vừa chán.
- **Để MC thua liên tục cho "có trở lực".** Sai thể loại; trở lực của 爽文 là **con số to hơn ở chương sau**, không phải MC bị đánh.
- **Đoạn cụt không có chủ đích.** Đoạn một cụm chỉ để đổi nhịp (实际上。/下一秒。); nếu cả chương đều là cụm thì thành thơ, mất lực.
- **Giữ hệ thống im lặng cho "tự nhiên".** Hệ thống là nhịp tim của chương; thiếu 【】 là thiếu 爽点, không phải tinh tế.
