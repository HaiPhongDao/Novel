# Nhật ký

2026-10-26 | mở truyện | 《骑砍领主：铁脊要塞》 — 西幻领主 · 骑砍面板 · cày cấp. Mô phỏng bộ mẫu Tác giả đưa
(`领主：我用骑砍系统肝经验.txt` trên Desktop). Ghi chú: file mẫu **không hỏng nặng** — 886/935 chương dùng
được (chỉ 49 chương `下载失败`), số chương bị lặp nhưng nội dung liền mạch một truyện. | Tác giả yêu cầu:
phân tích → SI theo SI template → chạy thử 1 đoạn với prompt theo mẫu để so văn | Tác giả

2026-10-26 | phân tích mẫu | 1.864.074 字 / 886 chương; chương trung vị 2.122 字; câu 23,9 字; 20 lượt
thoại/chương; 22,4 字/lượt; 65% dòng ≤ 30 字; `说道` 2,2/chương; `他罗伯森老爷` 1,35/chương; hỏi người đọc
0,79/chương; dòng bảng `【】` chỉ 0,06/chương (bảng được **kể** nhiều hơn **in**). Tật mẫu: `实` 0,14/1000,
so sánh người kể 0,46/1000, phủ định lặp 0,14/1000. | Phát hiện quyết định: **thẻ thoại là chuẩn của mẫu,
không phải tật** — SI 骑砍 v9 cũ cấm thẻ thoại nên bản cũ đọc như biên bản | Agent

2026-10-26 | SI v1 | Dựng từ `writer/SI-template` v3 + khối BANS/LENGTH của `si-khung.md`: 11.776 ký tự, 7
nguyên tắc, mỗi nguyên tắc một anchor **chép nguyên văn** (ch1, ch13×2, ch14, ch17×2, ch19 — có script kiểm
khớp nguồn). Khác SI cũ: thẻ thoại được dùng, người kể là storyteller đứng về phía MC, anchor lấy cả chương
hài chứ không chỉ chương trận. | Chưa sửa theo test — chờ bảng số | Agent

2026-10-26 | test 01 | Chạy SI v1 trên cảnh chương 8 bộ mẫu (prompt chỉ có sự việc): 2.645 字 · 131 câu · 20,2
字/câu · 30 lượt thoại · 18,8 字/lượt · 0 tật. Mẫu ch8: 2.076 字 · 89 câu · 23,3 字/câu · 17 lượt · 19,6
字/lượt. **Cổng kỹ thuật đạt, giọng chưa đạt**: 0 câu tự gọi `老爷`, chỉ 1 câu châm, bảng in sai dạng (ép
`【士兵】` thành một dòng), dài +27%, dòng vụn hơn mẫu (77% so với 60% dòng ≤30 字). Bốn sửa cho SI v2 ghi ở
`reviews/test-mau-01.md` mục 4. | Chưa nhận công cho SI: một cảnh, một lần chạy, chưa đo biên độ nhiễu | Agent

2026-10-26 | chốt tiền đề | Tác giả: "tùy bạn" → chọn phương án A (con thứ nam tước, 500 nông nô, 铁脊要塞 30
ngày). Dựng `bible/characters.md` (5 tên) + `plot/arcs.md` (黄金三章: 入局–加压–承诺). SI v2 thêm 4 dòng PART 2
(sổ riêng sau câu đạo nghĩa, tự gọi 少爷 1 lần/chương, câu chửi đứng trần, mở cảnh bằng tiếng), PART 4 (exp in
thành dòng 叮！), LENGTH (2.000–2.200). | Theo 4 sửa của test 01 | Agent

2026-10-26 | đoạn 001 | Bản A 2.786 字 (chạy 125s), 6 tật: 3 so sánh người kể + 3 nhãn ngữ điệu + 1 phủ định.
Sửa tay 10 chỗ + cắt 123 字 → bản B 2.663 字, `soat_van.py` sạch (0/0/0/0). Giữ được: mở chậm (tiếng búa →
thân thể → sân), mặc cả có chất liệu xã hội (đám cưới anh trai, người sốt), cái giá 30→24→6 金币, câu tự gọi
`他阿德里安少爷`, kết bằng quyết định mua 24 cái rìu. Còn lệch mẫu: 字 +21%, 47 lượt thoại (mẫu 20), câu 21,3
(mẫu 23,9). Canon mới phải chốt: 科尔 50 tuổi (không phải 28), tỷ giá exp 400 lần vung = 1 点. | Sửa tay rẻ hơn
vòng SI mới vì hai tật đó là biến thiên lần chạy, test 01 đã sạch | Agent

2026-10-26 | đoạn 001 vòng 2 | Tác giả: "MC nói chuyện chưa được đầy đủ, giao tiếp còn trống không". Nguyên
nhân đo được: 47 lượt nhưng 19,9 字/lượt, và lượt của MC nêu việc mà không nêu vì sao/cho ai/bao nhiêu; chỗ
格里 mời rượu mừng thì MC im lặng. Sửa ba tầng: SI v3 thêm 2 dòng (lượt của MC phải mang nội dung + trả lời
chủ đề người kia đưa ra trước khi quay về việc), brief ch2 sẽ ghi rõ nội dung từng lượt, bản C sửa tay 10
đoạn thoại và thêm một cuộc mặc cả thóc mốc (2.000 斤) với 格里. Số: 3.108 字 · 50 lượt · 33,0 字/lượt. | Dài
+46% so với mẫu; đề xuất tách cảnh thư phòng sang đầu chương 2 | Agent

2026-10-26 | luật đơn vị | Tác giả: "chúng ta đang tạo đoạn không phải chương. chương tách sau, sửa sau. đoạn
dài bao nhiêu cũng được miễn là nó không trượt ngữ cảnh, văn phong." → Đổi toàn bộ sang đơn vị đoạn: `git mv`
briefs/chapters/reviews sang `doan-001*`; SI v4 bỏ trần 2.000–2.200 字 và bỏ "about 2,100 characters" ở PART 3,
thay bằng luật "đoạn dài theo số beat, không có chỉ tiêu 字"; số 字 rời khỏi bảng tiêu chí review. Đoạn 001 giữ
nguyên 3.108 字, không tách. | Chương chỉ ghép ở khâu biên tập | Tác giả

2026-10-26 | đoạn 001 vòng 3 | Tác giả đọc bản C: "MC vẫn là 起来 thay vì 起来吧/站起来吧". Nguyên nhân: vòng 2
mới sửa nội dung lượt thoại (thêm lý do, con số), chưa sửa hình dạng — lệnh vẫn là động từ trần. Sửa 15 lượt
sang dạng nói (吧/去/给我 + 你), đổi cả lý lẽ biện hộ cho 科尔 (养了八年马, muốn chạy thì đã chạy). SI v5 thêm
luật "spoken shape". Bản D: 3.155 字 · 50 lượt · 34,0 字/lượt · 0 tật. | KN31 | Agent

2026-10-26 | đoạn 001 vòng 4 | Tác giả đòi Writer tự viết lại thay vì Agent sửa tay. Chạy `--new` với SI v5 +
brief cũ (189s, 1.963 字): Writer tự ra `“把人给我放下来吧。”`, `“你开个价吧。”`, `“我不爱喝甜酒，还是留给
大哥慢慢享用吧。”`, `“拿这六个金币去镇上的铁匠铺，给我买二十四把伐木斧回来。”`, 科尔 tự xưng `小的`.
32 lượt · 24,0 字/lượt (mẫu 20 · 22,4) — sát mẫu hơn bản D sửa tay (50 · 34,0). Còn 1 tật: so sánh
`五百个农奴像木桩一样戳在寒风里`. Hai cảnh Agent tự thêm ở D (mặc cả thóc mốc, xin cha hoãn nợ) không có
trong brief nên Writer không viết — lỗi brief, không phải lỗi SI. | Luật SI hiệu quả hơn sửa tay ở tầng câu | Agent

2026-10-26 | đoạn 002 | Chạy tiếp session của 001 (107s, 1.439 字). Đủ beat: 497 người · 3.400 斤 = ba ngày ·
代守 bán lương 20 金币, dẫn 40 lão binh đi · tường 60 步, 120 根 cọc, 24 rìu × 3 = 72 根/ngày · 43 火头.
0 tật. Sửa tay 1 câu phủ định cặp. Nhịp câu 16,0 字 (mẫu 23,9). | Writer tự ra `“给我数数对面的火头。”` | Agent

2026-10-26 | đoạn 003 | Session mới, SI v5 (147s, 1.360 字). Trận đầu: 9 豺狼人, MC giết 2 = 18 点 → 499/500;
5 chết 8 thương → 492; treo kẻ bỏ chạy; kết `“今晚加练。”`. Sửa tay 3 chỗ (老骑士 → 卡尔; dòng bảng sai dạng
do brief của Agent ghi thiếu; `捆了个结实` khuôn 实). Nhịp câu 15,8 字. | SI v6 thêm sàn độ dài câu: bỏ chỉ tiêu
字 làm model nén cả câu chứ không chỉ nén đoạn | Agent

2026-10-26 | SI v7 + đoạn 002-b | Tác giả: "thoại của MC luôn làm tôi khó chịu". Đo 26 lượt của MC ở 001-E/002/
003: trung vị 8 字, 15/26 ≤8 字, 0 lượt hỏi thật/xin/cảm ơn/nói ngoài việc; thắng mọi cuộc bằng đe dù chưa có
quyền; ba đoạn ba câu ngầu. SI v7: quyền lực trong thoại + mỗi cảnh một câu hỏi thật & một lượt ngoài việc +
tối đa một câu ngầu và không ở cuối đoạn. Brief 002-v2 thêm khối 【Quyền lực trong cảnh】. Kết quả 002-b:
23,9 字/câu (mẫu 23,9), MC 6 lượt trung vị 25,5 字, 代守 từ chối được, MC mua bằng lời hứa thay vì đe, có hỏi
chuyện vợ con 卡尔, không kết bằng câu chốt. | Sửa ở SI+brief ăn ngay, không phải sửa câu | Agent

2026-10-26 | đổi cách viết prompt | Tác giả chỉ ra `gemini/test/Without prompt`: Writer viết tự do có thoại
mượt, giọng riêng; lỗi ở prompt của Agent. Đo cùng SI v7: no-prompt 42 lượt / MC 11 lượt 24,5 字 / 老子 ×5;
prompt cũ (6 beat + chỉ định từng lượt + tỷ lệ thoại) 14 lượt; prompt ngắn cùng cảnh 8 lượt; **prompt ngắn +
phạm vi một ngày (004-a)** 21,1 字/câu, 13 lượt, MC 23,4 字. Viết mẫu `briefs/_mau-prompt-ngan.md`, KN32, sửa
mục 4 của skill. | Số lượt do phạm vi thời gian + số người có mặt, không do chỉ dẫn thoại | Tác giả (bắt lỗi)

2026-10-26 | đoạn 004 | 2.233 字, 168s, SI v7, prompt ngắn phạm vi một ngày. Tự làm được: chuyện ngoài việc
(腿伤 của 卡尔), MC tính thành tiếng, lệnh dạng 吧/去/给我. Sửa tay: 老爷 → 少爷 ×3; `经验加80` ×3 mâu thuẫn
bảng 0/2000 → đổi sang điểm đơn vị (`队伍经验加9`); ghi luật exp + track 4阶 /2000 vào glossary. | 21,1 字/câu
khớp mẫu 21,2 | Agent

2026-10-26 | SI v9 + đoạn 001-f (viết lại từ đầu) | Tác giả: thêm giới hạn 2.000 字 vào prompt, tên riêng
bằng chữ Latin, viết lại từ đoạn 1, duyệt mới đi tiếp. SI v9: FIXED CONVENTIONS 2 đổi sang tên Latin
(Adrian · Karl · Gerry · Cole · Iron Ridge · Vilan · House Losa), bảng in cả tên Latin; câu về độ dài trong SI
nhường cho con số ghi trong prompt. Bản F: 1.746 字, 10 lượt, 26,0 字/lượt, 0 tật (sau 1 sửa tay), số khớp
toàn bộ. Writer tự làm: Gerry tự nêu giá bằng luật, MC xếp từng đồng vàng lên nắp thùng, câu chốt là câu hỏi
của Karl. | Lệch dàn ý: Karl thành hầu 16 tuổi (đã sửa), Cole 6 năm (đã sửa), **前任长官 đã bỏ chạy** → phải đổi
nội dung đoạn 002–003: thành rỗng + 40 lão binh bị bỏ lại | Agent

2026-10-26 | đoạn 001-G + archive chapters | Chạy lại đoạn 001 theo yêu cầu Tác giả: `--new`, SI v9, prompt `doan-001-v3.md` nguyên văn, 113s, **1.368 字**. Số liệu khớp toàn bộ; 0 nhãn ngữ điệu, 0 so sánh người kể; có lượt ngoài việc (ngựa già của Cole) và vẫn xếp từng đồng vàng lên mép máng cỏ. Tật: phủ định lặp 1, 实 1 (`真切`), thẻ thoại 4, câu 20,0 字 (F 26,5), hụt 32% so với mốc 2.000. Karl vẫn thành `年轻的随从` vì prompt v3 không có dòng thân phận. Đã `git mv` 12 bản cũ (001-a…f, 002-a/b/c, 003-a, 004-a, test-01) vào `chapters/archive/`. cham_doan 72/100. | Sửa ở prompt (mốc 2.000 không dưới 1.900 + dòng thân phận Karl), chưa sửa SI | Agent

2026-10-26 | bản H: prompt v4 + glossary 少爷 | Tác giả duyệt ba sửa đổi. `briefs/doan-001-v4.md` = v3 + `2.000 字, không dưới 1.900` + dòng thân phận Karl/`Gerry`/`Cole`; glossary mục 3 thêm `少爷` (người hầu gọi con trai nam tước, tự xưng `小的`). Chạy `--new` SI v9, 131s, **2.461 字** · 21,2 字/câu (mẫu 21,2) · 21 lượt · 28,5 字/lượt. Karl và Cole ra đúng canon (`三十四岁` · mất ngón út tay trái · `八年` chăn ngựa) — dòng thân phận hiệu quả. `少爷` ×9, `老爷` 0 cho Adrian; `小的` vẫn 0 (SI không có luật). Tật tăng theo độ dài: phủ định 6, so sánh người kể 3, nhãn 2, thẻ thoại 11; cham_doan 56/100. Lỗi số: `六枚金币…一千四百四十斤` (phải 720 斤, tự mâu thuẫn với lượt Karl); exp `迈进四阶` sai thanh /2000. | `không dưới 1.900` sửa quá tay → lần sau cửa sổ 1.900–2.000; muốn `小的` thì thêm luật vào SI | Agent

2026-10-26 | luật độ dài + đoạn 002-D | Tác giả: "Không cần sửa độ dài nếu không trượt văn phong. Khoảng 2000-3000 chữ thì không trượt được. Tiếp đoạn 2." → cửa sổ độ dài đoạn 2.000–3.000 字 ghi vào README, prompt từng đoạn, SI không có trần. `briefs/doan-002-v4.md` (thân phận từng người, quyền lực thuộc 代守, tỷ lệ thoại, cửa sổ 2.000–3.000). Chạy tiếp session bản H, 117s, **2.372 字 · 24,5 字/câu · 19 lượt · 33,5 字/lượt**; văn 34/34 (0 实, 0 nhãn, 0 từ hiện đại), phủ định 2 + 既…也 1, thẻ thoại 6, so sánh 3 (tool báo 0); cham_doan 70/100. Số khớp: 10.400 − 7.000 = 3.400 斤 = 3,4 ngày; 24×3 = 72 cây/ngày → 120 cây = 2 ngày; 43 火头 ≈ 300. Cần quyết 6 chỗ: `爵士` ×2, `小的` 0, câu `两年前…七天过去了`, `枝权` typo, 3 so sánh, 2 phủ định song song. 代守 dẫn 40 lão binh rời thành → đoạn 003 phải tính lại. | Giữ cửa sổ 2.000–3.000; register cần luật ở SI (chờ duyệt) | Agent

2026-10-26 | 5 đoạn liền: 003-E → 007-A | Tác giả: "Được rồi đấy, tạo tiếp 5 đoạn liên tiếp đi" (bản 002-D chấp nhận nguyên trạng). Dựng `plot/so-lieu.md` (chuỗi người/lương/điểm cho 003–007) rồi chạy tiếp cùng session, SI v9, mỗi đoạn một prompt mới. Kết quả 字: 1.865 · 1.662 · 1.677 · 1.978 · 1.533 (TB 1.743, đều dưới cửa sổ 2.000–3.000); cham: 58 · 82 · 72 · 70 · 64. Chuỗi số khớp 100%: 497→493→488→477; lương 3.400→2.400→1.400→400→0; 132 根 = 120 rào + 12 chông; 481+18=499, +9=508 → 4阶（8/2000）; 士兵 63+117=180 → 41 二阶（80/100）, 436 一阶; 上限 600; 士气 22→41→29→52. Register: `小的` đã vào văn ở 005 (Cole), Karl gọi 少爷 tự xưng 我. Tật/lỗi: 005 tự thêm `前世` (tiền đề xuyên không, bible không có); 007 `效率` (từ hiện đại); 004 `骑士老爷`; 实 2, nhãn 3, so sánh 3. Review: `reviews/doan-003-007.md`. | Cửa sổ số không giữ: model lấy cận dưới trừ hao → muốn giữa cửa sổ phải ghi đích + sàn (chờ Tác giả); `前世` và arcs chương 2 cần chốt | Agent

2026-10-26 | sửa mối nối 5 đoạn | Tác giả: "đoạn sau không hề được nối tiếp với đoạn trước". Đo: 5/5 mối đứt, nguyên nhân ở prompt (mỗi brief tả một cảnh tự thân, không có dòng nối). Thêm KHỐI NỐI TIẾP vào `briefs/_mau-prompt-ngan.md` (luật 0) + 5 brief v2. Lần chạy tiếp session cũ bị Writer chép lại 77% bản trước (`doan-003-f-lap-77.md`) → chuyển sang `--new` từng đoạn. Chuỗi mới 003-G…007-B: 2.488 · 1.723 · 2.000 · 2.262 · 1.780 字; 5/5 mối liền (mỗi đoạn mở bằng việc trả lời đúng câu cuối đoạn trước); số liệu khớp toàn chuỗi, 7 dòng bảng đúng. Cái giá: thoại 6–32 lượt, chữ/lượt tụt 26–36 → 12,2–22,7, lượt cụt 1–7, cham 42–76 (vì khối nối tiếp viết "Karl nói gì" — vi phạm luật 2). Đã ghi cảnh báo vào luật 0: viết "ai làm gì", không "ai nói gì". `chapters/` chỉ còn chuỗi đang dùng; bản cũ vào `chapters/archive/`. Review: `reviews/noi-tiep-doan.md`. | Mối nối là luật của brief, không của SI; chạy lại 5 đoạn với khối đã sửa nếu muốn thoại dày lại | Agent

2026-10-26 | đoạn 003-H (nối tiếp, khối 'việc' thay 'lời') | Tác giả chọn (2). `briefs/doan-003-v3.md`: khối nối tiếp đổi sang "mở bằng một việc cụ thể", bỏ chỉ định ai nói gì. `--new`, 143s, **3.178 字** · 24,6 字/câu · 37 lượt · 22,1 字/lượt (bản G: 19,8) · phủ định 2 · 实 1 · nhãn 1 · cham 58. Mở đúng chỗ dừng 002: hắn úp cây松明 vào thùng nước, tắt toàn bộ lửa trong thành. Cảnh báo: vượt trần 3.000 字 (3.178). | Đã push riêng đoạn này | Agent

2026-10-26 | đoạn 004-F (nối tiếp 003-H) | Khối nối tiếp "việc": mở bằng việc hắn **không** quay lại lấy khiên, chạy thẳng lên lưng đồi. `--new`, 126s, **2.173 字** · 26,8 字/câu · 5 lượt · 10,4 字/lượt · phủ định 1 · 实 1 · cham 56. Số khớp: 5 chết, 8 thương, 63/100, 499/500, 41 士气, 24 斧, 36 根 cọc. Kết đúng chỗ: bàn tay Karl nắm cổ tay. | Nối liền nhưng thoại quá mỏng (5 lượt · 10,4 字) | Agent

2026-10-26 | đoạn 005-C (nối tiếp 004-F) | Mở bằng việc hắn **không rút tay** khỏi bàn tay Karl, rồi mới xử 巴特. `--new`, 309s, **2.637 字** · 21,1 字/câu · 24 lượt · 17,7 字/lượt · phủ định 4 · 实 3 · nhãn 2 · cham 52. Số khớp: 1.400 斤, 132 根 = 36 + 96, 47 火头, 士气 29. Kết đúng: dây căng, tiếng 巴特 bị cắt. | Thoại dày lại so với 004-F (17,7 vs 10,4) nhưng tật tăng | Agent

2026-10-26 | đoạn 006-C (nối tiếp 005-C) | Mở bằng việc ngay sau tiếng dây: một nông nô khuỵu xuống nôn, không ai đỡ. `--new`, 150s, **2.560 字** · 25,9 字/câu · 10 lượt · 12,6 字/lượt · phủ định 1 · so sánh 3 · nhãn 1 · cham 58. Số khớp: 11 chết, 19 thương, 41 二阶（80/100）, 436 一阶, 4阶（8/2000）, 上限 600, 士气 52. Kết đúng: Karl hỏi có phải vừa lên bậc, hắn đáp `死了十一个人` | Thoại vẫn mỏng (10 lượt · 12,6 字) | Agent

2026-10-26 | đoạn 007-C (nối tiếp 006-C) | Mở bằng việc đêm: mười một xác bên miệng hố, hắn tự tay nhấc cây đà gãy khỏi rào. `--new`, 137s, **2.362 字** · 20,5 字/câu · 35 lượt · 17,1 字/lượt · 实 1 · nhãn 2 · cham 58. Kết đúng: đếm đủ 41 người ở cửa nam, ngoái nhìn Karl trên lớp rào mới. | Chuỗi 003-H→007-C nối liền 5/5 | Agent

2026-10-26 | SI v11 chốt làm SI hiện hành + đoạn 003-K | Tác giả: "Đừng gán tính cách vào MC, AI viết dở cái đấy. Tự writer quyết" + chọn phương án chốt SI v11 và thêm chỗ đặt trong brief. `si-dan-gemini.txt` = v11 (16.200 ký tự, PART 1B 5 dòng + 2 dòng về câu châm và sổ ngày); bản v9 giữ ở `gemini/system-instruction-v9.md`. Brief 003-v5 = v4 + dòng "chỗ đặt". 003-K: 1.561 字 · 15,1 字/câu · 31 lượt · 18,3 字/lượt · cham 58. **Giọng đã vào**: `在开拓领地的账本上，死四个农奴不需要多费一笔墨水` · `开玩笑，哪有匀出粮食给不能动的人等死的道理？` · `他Adrian少爷可不是来这里开善堂的` · `在算账这件事情上，老骑士从来算不过他`. Lỗi register: Karl/Cole gọi 大人 (brief 003 thiếu dòng xưng hô) → sửa tay 3 chỗ. | Câu ngắn đi rõ (15,1 字/câu) | Agent

2026-10-26 | đoạn 004-G (nối tiếp 003-K, SI v11) | Mở bằng `Adrian 没有回头去接那面盾牌`. 145s, **1.930 字** · 14 lượt · 10,9 字/lượt · sạch tật · cham 64 · 0 chỗ 大人/老爷 (register đã thêm vào brief). Số khớp: 5 chết, 8 thương, 63/100, 499/500, 41 士气. | Thoại quá ngắn (10,9 字/lượt) | Agent

2026-10-26 | đoạn 005-D (nối tiếp 004-G) + sửa register 003-K | 005-D: 310s, **2.573 字** · 25 lượt · 18,3 字/lượt · phủ định 3 · 实 1 · nhãn 1 · cham 52. Mở bằng `Adrian没有立刻抽回手…从指缝里挣脱`. Treo 巴特: Cole xưng 小的, 领主老爷 cho nam tước. Kết đúng: dây căng, tiếng 巴特 đứt giữa chừng. Sửa tay 003-K: 4 chỗ 大人 → 少爷 (brief 003 thiếu dòng xưng hô). | Đoạn nội tâm nhiều nên tật tăng | Agent

2026-10-26 | chạy lại từ đoạn 001 + dòng "người xuyên việt, giỏi tài chính" | Tác giả: "chạy lại từ đoạn 1… văn phong kém đi… chưa thấy MC nghĩ và nói nhiều hơn", rồi chỉ đúng dòng cần thêm: `thêm dòng MC là người xuyên việt, giỏi về tài chính`. Bỏ hẳn dòng "chỗ đặt" (Tác giả bắt lỗi: nó viết hộ cái đầu MC, mặc cả giá nô lệ không phải ưu thế người hiện đại, lặp dữ kiện, viết luật văn trong prompt). Brief 001-v7 = dữ kiện + dòng xưng hô + 1 dòng sự thật: `Adrian là người xuyên việt: kiếp trước làm nghề tài chính — sổ sách, lãi, tỷ giá, chi phí, dòng tiền`. Bible characters.md thêm cùng dòng đó. SI v12 (v9 + một đoạn 3 câu) thay v11. 001-L: 197s, **3.040 字** · 24,4 字/câu · 28 lượt · 23,9 字/lượt · cham 42 (văn 6/34: phủ định 7, 实 1, nhãn 1, so sánh 1). Giọng đã rõ: `在前世，他是个整天和资产负债表、贴现率与坏账准备打交道的精算师` · `这可是花了他两千四百斤粮食的代价赎回来的资产。死一个都是严重的资本折旧` · `三十枚启动资金…流动资金已经蒸发了百分之八十` · `这笔买卖在账面上亏了现金，在固定资产和控制权上却赚得盆满钵满`. Lỗi: `溢价了一倍` sai (2 金币 là giá trần, không phải gấp đôi), `小人` thay vì `小的`, phủ định 7. | Chờ Tác giả duyệt đoạn 001 rồi mới chạy 002 | Agent

2026-10-26 | back SI cũ (v9) + đoạn 001-M | Tác giả: "văn phong bị giảm đi rất nhiều. back lại bản SI cũ đi". `system-instruction.md` + `si-dan-gemini.txt` trả về **v9** (14.676 ký tự, không PART 1B); v10/v11/v12 giữ ở gemini/ làm bản thử, không dùng. Giữ dòng sự thật xuyên việt trong brief (dữ kiện, không phải luật văn). 001-M: 158s, **2.114 字** · 22,8 字/câu · 20 lượt · 22,6 字/lượt · phủ định 3 · 实 0 · nhãn 1 · so sánh 1 · **cham 60**. So: H (v9, brief cũ) 2.461/21,2/21/28,5 cham 56; L (v12, brief có dòng xuyên việt) 3.040/24,4/28/23,9 cham 42 phủ định 7. ⇒ v9 + dòng dữ kiện là tổ hợp sạch nhất; phần phình của v11/v12 chính là thứ làm văn xuống. Chuyển cả chuỗi cũ (001-H…007-C, 003-K, 004-G, 005-D, 006-D, 001-L) vào `chapters/archive/`, `chapters/` chỉ còn 001-M. | SI đời nào thêm luật là phải đo lại bằng 字/câu và phủ định | Agent

2026-10-26 | đoạn 001-N: sửa hình dạng câu từ chối + bỏ "giỏi tài chính" | Tác giả bắt: `“Không mua lương thực, một đồng tiền lúa mạch đều không mua.” Adrian lắc đầu nói rằng` — hai bệnh: phủ định trần ném vào không khí (không nói với Karl, không có 咱们/你), và thẻ `nói rằng` là người kể thuật lại chứ không phải thẻ nói. Sửa: (1) brief bỏ "giỏi tài chính", chỉ còn `Adrian là người xuyên việt.`; (2) SI v9 **sửa một dòng có sẵn** (luật spoken shape), không thêm luật: câu từ chối phải nói với người trước mặt và tính họ vào (`咱们不买粮 · 你我不去`), thẻ phải là `说道/摇头道/沉声道` không phải `nói rằng`. 001-N: 216s, **2.743 字** · 23 lượt · 20,2 字/lượt · **phủ định 0 · 实 0 · so sánh 0** · nhãn 1 · **cham 64**. Câu đã đúng hình: `“咱们不买麦子。”Adrian 摇头道。` | 0 tật sau khi sửa đúng chỗ; văn không phình | Agent

2026-10-26 | đổi quy ước tên + đoạn 002-E | Tác giả: `Baron Losa` bị đọc thành Bá Tước (baron là NAM tước). Chốt: **chỉ tên người viết Latin, chức tước và địa danh viết chữ Hán**. Sửa SI FIXED CONVENTIONS 2 (铁脊要塞 · 维兰 · 洛萨家族 · 巴罗尔 · 洛萨男爵, không viết Baron Losa) + glossary mục 5 thành bảng. Brief 002-v5 mang quy ước mới, số mới: 512 → 509 sau ba người chết dọc đường; panel `一阶.500 维兰农奴`, chín người ngoài trần 500 nói ra một câu. 002-E: 127s, **2.550 字** · 24,4 字/câu · 27 lượt · 18,6 字/lượt · phủ định 2 · 实 0 · nhãn 1 · so sánh 1 · thẻ 12 · cham 58. Không còn chữ Latin nào ngoài tên người. Số khớp: 24 rìu, 3.400 斤, 10.400 斤, 20 金币, 200 袋, 43 火头, 60 步. | Tên người Latin, địa danh Hán | Agent

2026-10-26 | đoạn 003-L | Quy ước tên mới (địa danh Hán), số mới 509 → 505. 131s, **1.993 字** · 21,9 字/câu · 23 lượt · 16,2 字/lượt · phủ định 1 · 实 0 · nhãn 0 · so sánh 2 · cham 64. Mở bằng việc hắn bóp tắt ngọn đuốc trên 垛口 rồi ra lệnh tắt hết lửa; kết đúng chỗ: Karl đuổi theo hét `您一个人去挡九只畜生？！` khi hắn đã xuống nửa dốc. Panel `一阶.500 维兰农奴`. | Nối liền, sạch tật | Agent

2026-10-26 | đoạn 004-H (có GIỌNG MẪU) | Tác giả: "nếu tạo session mới của writer thì nên đưa lại đoạn cuối của đoạn trước để giữ giọng văn". Brief 004-v7 mở bằng 7 dòng cuối của 003-L nguyên văn + câu "viết tiếp từ đây, không chép lại câu nào". 233s, **2.281 字** · 23,4 字/câu · 13 lượt · 13,7 字/lượt · phủ định 0 · 实 1 · nhãn 0 · so sánh 0 · cham 64. Kiểm chép mẫu: 0/5 câu của mẫu xuất hiện trong bản mới. Số khớp: 505→500, 481+18=499/500, 63/100, 41/100, 2.400 斤, 36 根, 9 头. Kết đúng: Karl nắm cổ tay sau khi hỏi chuyện vợ con của năm người chết. | Giọng mẫu giữ nhịp mà không bị chép | Agent

2026-10-26 | 5 đoạn 004–008 (mỗi đoạn 1 commit + push) | Tác giả duyệt 002/003 và xin 5 đoạn, thêm luật "session mới thì đưa lại đoạn cuối đoạn trước". Từ 004 trở đi mỗi brief mở bằng khối GIỌNG MẪU (7–10 dòng cuối nguyên văn) + KHỐI NỐI TIẾP. Kết quả: 004-H trận đầu 9 豺狼人 2.281 字/64; 005-E treo 巴特 1.939/66; 006-E dựng rào + trận 17 con, lên 4阶 2.289/64; 007-D hết lương + đi lấy 200 袋 2.602/66; 008-A cướp trạm nam, ba cột khói 2.488/52. Chuỗi số khớp: 505→500→499→488→484; lương 2.400→1.400→400→0; 132 = 120 rào + 12 chông; 481+18=499, +9=508 → 4阶 8/2000, +36 = 44/2000; 士兵 63+117=180 → 41 二阶 (80/100) + 447 一阶, +18 = 98/100; 上限 600; 士气 22→41→29→52→58. Không bản nào chép nguyên câu mẫu (kiểm 5 chuỗi). | Quy ước tên + giọng mẫu + khối nối tiếp = bộ ba giữ được giọng qua session mới | Agent

2026-10-26 | đoạn 009-A | Ba cột khói → về cứu thành. 110s, **2.574 字** · 33,7 字/câu · 11 lượt · 16,6 字/lượt · phủ định 1 · 实 0 · nhãn 0 · so sánh 2 · cham 72. Số khớp: 484→465 (19 chết, 30 thương), 30 豺狼人 (22 chết, 8 chạy), MC giết 6 = 54 → 4阶 98/2000, lính 16 = 144 → 二阶 98+144=242 → vượt 100, 37 người lên 三阶, dư 142 → 三阶.37（142/300）, 428 一阶. Đã ghi quy ước thanh đơn vị (一阶/100 · 二阶/100 · 三阶/300) vào glossary và sửa lỗi đếm của 008 (`二阶.41` → `二阶.37`). | Câu dài lên (33,7 字) | Agent
