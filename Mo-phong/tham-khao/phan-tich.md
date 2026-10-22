# Phân tích truyện tham khảo — 《疯了吧？我刚先天他就仙帝了！》

> File gốc: `疯了吧？我刚先天他就仙帝了！.txt` (Tác giả tải lên 23/10/2026), mã hoá **GBK**, xuống dòng CRLF. Đọc bằng: `python3 -I -c "import sys;print(open(sys.argv[1],'rb').read().decode('gb18030','replace'))" <file>` (có 6 byte hỏng ở phần quảng cáo đầu file, không ảnh hưởng chính văn).
>
> Dùng để **tham khảo thể loại, cơ chế máy mô phỏng, nhịp và giọng văn** (mẫu giọng cho SI). Không chép tên, địa danh, sự kiện, công pháp hay câu chữ vào truyện của ta.
>
> Agent đọc kỹ chương 1–4, 13, 16, 225–226, lướt các chương khác, đọc toàn bộ tên 1261 chương và đo số liệu bằng script trên toàn file.

## 1. Thông tin chung

| Mục | Nội dung |
|---|---|
| Độ dài bản tải | 1261 chương, ~2,63 triệu chữ (chương trung vị ~2.070 字 — gần đúng một "đoạn" của xưởng) |
| Thể loại | 玄幻 · 穿越 · **人生模拟器** · võ hiệp → tu tiên → tiên giới (thăng cấp vô hạn) |
| Nhân vật chính | 陆长生 — thanh niên "nằm thẳng" thế kỷ 21, chết vì xe tải, xuyên thành ăn mày → tạp dịch → kế toán → con nuôi chủ tiêu cục 广胜镖局 |
| Bàn tay vàng | **大道模拟器** — chính là bản hack MC tự viết cho game "仙途" ở kiếp trước, đi theo khi xuyên. Mỗi lần mô phỏng chạy cả đời MC từ hiện tại tới khi chết, hiện thành nhật ký 【】; hết mô phỏng chọn **giữ một** trong hai: 【修行境界】 hoặc 【修行经验】 |
| Ý tên truyện | "Điên rồi à? Tôi vừa tới Tiên Thiên thì hắn đã thành Tiên Đế" — khoảng cách nực cười giữa MC ở đời thật và "MC trong mô phỏng" |

## 2. Cơ chế máy mô phỏng (bản gốc)

1. **Kích hoạt** ở chương 1 khi MC bị đánh dấu nội khí (异种能量) — đúng lúc bị ép, tặng một lần miễn phí.
2. **Chi phí:** "金钱" nạp bằng tiền đời thật (bạc → 元石 → 源石 → 法则之砂 → 源晶 → 仙石 → 仙玉…). Giá **tăng theo cảnh giới của MC**: 1 → 10 → 100 金钱… Lần đầu đòi tiền thì đồng xu không nhận, phải bạc — một màn hài + bài toán tiền ngay chương 2.
3. **Nội dung mô phỏng:** người trong mô phỏng hành động theo đúng tính cách và hiểu biết hiện tại của MC; mỗi dòng một mốc (第二日 / 三个月后 / 二十六岁…), chạy tới chết (bị giết, bệnh, già). Biết thêm → lần sau mô phỏng đi đường khác.
4. **Giữ một:** cảnh giới (sức mạnh, như "level") hoặc kinh nghiệm (công pháp, đao pháp, luyện đan, kinh nghiệm chiến đấu). Ch 16 phát hiện "bug": thiên tài địa bảo dùng trong mô phỏng cải thiện tư chất và mang về được.
5. **Thông tin tương lai:** log lộ âm mưu (黑虎帮 chờ 圣教, vật cần tìm ở nhà họ Vương), kẻ phản bội, cơ duyên → MC ra tay ở đời thật.

## 3. Nhịp phát triển

| Chương | Diễn biến | Ghi chú |
|---|---|---|
| 1 | Bang chủ 黑虎帮 đòi 500 lạng, gieo nội khí vào tim MC → kích hoạt, mô phỏng miễn phí | Mở bằng ép buộc cụ thể + con số |
| 2 | Log lần 1: vào võ quán, 3 tháng không nhập môn, bị đuổi, bị đấm chết → chọn kinh nghiệm. Đồng xu không nạp được; đêm đào 20 lạng giấu dưới gốc liễu | Chết vì lý do "ngu" — hài |
| 3 | Lần 2–3: chạy tới 52 tuổi, nhồi đan lên 内气 rồi thổ huyết chết → giữ cảnh giới; giá tăng ×10; lần 3 học đao pháp với ông già phế võ, 43 tuổi "ba đao chém 雷虎" | Mô phỏng cho cả **mục tiêu** lẫn **cách làm** |
| 4 | Đời thật: một đêm mang dao chặt củi tới tổng đàn 黑虎帮, chém sạch, 雷虎 bỏ chạy — kèm cảnh cắt sang phe địch đang họp | Payoff ở đời thật, qua mắt kẻ thù |
| 5–72 | Võ hiệp: diệt nhà họ Vương (giàu → nạp tiền), 龙王帮, 魔教, 太古龙象诀 nhiều lần, lên 先天, tông sư, nhất thống giang hồ | Mỗi 2–4 chương: một lần mô phỏng → một payoff thật |
| 73–220 | Tu tiên, thần thông, phi thăng thượng giới | Log dần chiếm nhiều hơn |
| 220–1261 | **Gần như 100% là log 【】** — truyện thành bản tóm tắt cả đời mô phỏng | Thoái hoá |

## 4. Số đo văn phong

Đo bằng script; mỗi đoạn văn (paragraph) thụt đầu dòng `　　`, không dòng trống.

| Chỉ số | Ch 1–30 | Ch 101–130 | Toàn truyện |
|---|---|---|---|
| Độ dài đoạn văn trung vị | **24 字** | 25 | 24 |
| <15 字 / 15–40 / 40–80 / >80 | 24,7% / 56,2% / 18,6% / 0,5% | 20,5 / 60,3 / 18,9 / 0,3 | 16,1 / 68,5 / 14,5 / 0,8 |
| Log 【】 (theo số chữ) | **~27%** | ~19% | ~83% |
| Dòng log trung vị | 31 字 | 36 | 24 |
| Đoạn văn mở bằng thoại | 14% | 12% | 2,6% |
| ！ / ？ / …… (trên 1000 字) | 5,4 / 3,2 / 1,4 | 5,4 / 3,5 / 0,8 | 4,7 / 2,7 / 0,6 |
| —— | 0,13 | 0,12 | 0,57 |
| So sánh (像/如同/仿佛/似的) | ~0,7 | ~0,6 | ~1,0 |
| 宿主 / 系统 | ~0,06 mỗi từ — rất ít; máy gọi MC là 宿主 chỉ ở dòng nạp tiền | | |

Phần đáng học là **ch 1–60**: log chiếm khoảng một phần tư, phần còn lại là cảnh đời thật.

## 5. Kỹ thuật đáng học

1. **Đọc log như xem phim đời mình.** Sau mỗi cụm log là phản ứng của MC: chê mình, khen mình ("不愧是我"), tính sổ, rút ra lý do chết. Hài nằm ở **phản ứng**, log chỉ kể việc.
2. **Log xen phản ứng giữa chừng.** Hai dòng log → MC chen một câu ("看来…今晚不会找自己麻烦，可以睡个好觉了") → log tiếp. Tạo cảm giác "đang xem trực tiếp", tránh khối tóm tắt dài.
3. **Chết ngu, chết đa dạng.** Bị đuổi khỏi võ quán rồi bị đấm chết; nhồi đan lên cảnh giới rồi thổ huyết; báo thù quá sớm bị vây đánh chết; kết nghĩa huynh đệ bị đâm sau lưng. Mỗi cái chết là một "bug report" cho lần sau.
4. **Chi phí tăng → bài toán tiền liên tục.** Giá ×10 khi lên cảnh giới, đồng xu không nạp được, đào tiền giấu dưới gốc liễu, diệt nhà giàu thu 32 vạn lạng. Mạnh lên kéo theo nghèo đi.
5. **Lựa chọn giữ một có lý lẽ.** MC giải thích ngắn vì sao chọn cảnh giới hay kinh nghiệm — người đọc học luật qua lựa chọn, không qua bảng giới thiệu.
6. **Payoff ở đời thật, qua mắt người khác.** Ch 4: cắt sang phe 黑虎帮 đang họp, tự tin, rồi một thiếu niên cầm dao chặt củi bước vào; "không ai thấy hắn ra tay".
7. **Bathos.** "他是一个有良知的人。……好吧，他的真实想法是，真的和这些愤怒的死者家属杠上，倒霉的一定是他。" — dựng câu nghiêm rồi hạ ngay.
8. **Luật đi qua phép tính của MC.** Tuổi thọ tiên thiên, sức lực tính bằng cân (一头龙象之力 = 一万斤…), "也就是说…" — chuỗi mệnh đề nối nhau, có số.

## 6. Điểm yếu — không lấy

1. **Thăng cấp vô hạn, log nuốt truyện.** Từ ch ~220 gần như toàn là 【】: không cảnh, không thoại, không nhân vật phụ có giọng. Lý do: giữ cảnh giới mang về không giới hạn → đời thật không còn việc gì. → Truyện ta **chặn trần thứ mang về** và đặt **log ≤ khoảng 1/3 mỗi đoạn**.
2. **Tiêu đề chương kiểu clickbait, tên chiêu thức dồn dập** (无量神通、浑源圣体…) — mất trọng lượng nhanh.
3. **Meme mạng, chửi thề** (鹅厂、tnnd、拼夕夕) — ít hơn truyện goblin nhưng vẫn có; giữ giọng tự giễu, bỏ meme.
4. **Nhân vật phụ là công cụ** (宁悠悠 chỉ để sai vặt và đỏ mặt); phản diện thông báo âm mưu cho MC nghe lén.
5. **Lỗi chữ và rác web lậu** ("小主，这个章节后面还有哦…", 时/再/他里) — anchor trong SI chỉ lấy câu sạch.
6. **Bàn tay vàng là "hack do MC tự viết"** — tiện nhưng làm MC biết hết luật từ đầu, mất phần khám phá.

## 7. Lấy gì cho truyện mới

| Lấy (khung thể loại) | Đổi (cho truyện ta) — xem `../bible/world.md` |
|---|---|
| Mô phỏng cả đời từ hiện tại tới chết, log 【】 ngôi 你 | Giữ — đây là chữ ký của thể loại |
| Chọn giữ một khi kết thúc | Ba lựa chọn: tu vi / kinh nghiệm / **một đoạn ký ức sống** (chi tiết mà log chỉ tóm tắt) |
| Giữ cảnh giới không giới hạn | **Trần:** tu vi mang về không vượt quá đỉnh đại cảnh giới hiện tại → đột phá đại cảnh giới phải làm ở đời thật |
| Chi phí tăng theo cảnh giới | Giữ, trả bằng linh thạch — đời tạp dịch luôn thiếu linh thạch |
| MC biết hết luật vì tự viết hack | MC **tự lần ra luật** bằng thói quen nghề cũ: kiểm thử game (tái hiện lỗi, ghi bước, đổi một biến mỗi lần) |
| Payoff qua mắt kẻ thù | Giữ, dùng có chừng mực |
| Đoạn văn ngắn, log xen phản ứng | Dùng làm mẫu giọng cho SI (`../gemini/system-instruction.md`) |

## 8. Dùng làm mẫu giọng (SI)

SI nháp lấy anchor từ ch 1, 2, 4 và 13 (ch 4 hai chỗ). Chọn vì kỹ thuật (nhịp ba cỡ đoạn, bathos, MC đọc đời mô phỏng của mình, thoại xen lời kể, chuyển cảnh `……`, log xen phản ứng), né câu có lỗi chữ và các từ trong blacklist chung (一丝, 嘴角, 直冲…). Tên riêng trong anchor thuộc truyện tham khảo; SI đã ghi rõ.
