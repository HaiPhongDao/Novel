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
