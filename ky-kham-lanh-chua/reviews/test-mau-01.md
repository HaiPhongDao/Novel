# Test 01 — chạy SI v1 trên cảnh chương 8 của bộ mẫu

- SI: `gemini/si-test-mau.txt` (bản `system-instruction.md` đổi tên riêng sang tên mẫu; luật y nguyên)
- Prompt: `briefs/test-mau-01.md` — **chỉ có sự việc**, không dặn cách viết, không dặn độ dài câu, không có
  một câu tiếng Trung nào dài quá 8 chữ
- Bản ra: `chapters/test-01.md` (2.645 字, 155s, AI Studio, model mặc định của tài khoản)
- Nguyên văn để so: `mau/goc-t1-ch08.md` (cả chương 8, 2.076 字)
- Thinking: `archive/thinking-test-01.md`

## 1. Bảng số

| chỉ số | mẫu ch8 | SI v1 | lệch |
|---|---|---|---|
| 字 | 2.076 | **2.645** | +27% (SI ghi 2.100) |
| câu | 89 | 131 | +47% |
| **chữ / câu** | **23,3** | **20,2** | −3,1 (câu ngắn hơn mẫu) |
| dòng | 73 | 122 | +67% |
| **dòng ≤ 30 字** | 60% | **77%** | vụn hơn mẫu |
| **lượt thoại** | **17** | **30** | +76% |
| chữ / lượt thoại | 19,6 | 18,8 | ~khớp |
| thẻ thoại (`说道/问道/笑道/命令道`) | 5 | 5 | khớp |
| dòng bảng `【】` | 5 | 8 | |
| tự gọi `罗伯森老爷` | 2 | **0** | mất giọng |
| câu hỏi tu từ / hỏi người đọc | 3 | 1 | |
| tật `实` / so sánh người kể / phủ định lặp / nhãn ngữ điệu | 0/0/1/0 | **0/0/0/0** | sạch |

`tools/soat_van.py`: 0 phủ định lặp, 0 bộ ba, 0 `既…也`, 0 `不是…而是`, 0 so sánh người kể, 0 khuôn `实`,
0 nhãn ngữ điệu, 1 từ hiện đại (`魔晶`? — bỏ qua, là thuật ngữ truyện), 30 lượt thoại, 18,8 chữ/lượt.
Cổng kỹ thuật **đạt**; nhưng cổng kỹ thuật chỉ để bắt hồi quy, không phải chất lượng.

## 2. Đọc bản ra (bốn câu hỏi, ba đoạn)

**Mở** — *“五里！豺狼人距离营地只有五里了！”*
- Ai muốn gì: chưa ai. 罗伯森 muốn dẹp loạn trong trướng, nhưng người đọc chỉ thấy *"大帐里顿时乱作一团"* và
  ba câu hỏi của đám đông.
- Đổi gì: quyền chỉ huy về tay 罗伯森 sau *“都闭嘴。”*
- Đáng nhớ: *“五百名士兵…辎重营的破大车”* — có số, nhưng không có **cái giá nào của riêng anh ta**.
- Bỏ qua được: hai dòng tả 埃德 (`剑术在青铜阶里垫底…八成活不过一炷香`) — thông tin tốt, nhưng đứng ngoài
  sổ của MC.

**Giữa** — *“艾斯，把这八百人拆成九排。”*
- Ai muốn gì: MC muốn dựng tuyến; **không ai cản**, các đội trưởng chỉ tuân. Căng thẳng tụt từ đây.
- Đổi gì: 800 → 9 hàng → 120 + 70 người; có câu chửi các quý tộc đã huấn luyện đám này (*“王都那群老爷
  除了收地租，连怎么训兵都忘干净了。”*) — **đúng 1 câu snark trong cả đoạn**, mẫu dùng ~5–6 câu kiểu này.
- Bỏ qua được: `“就地掀翻，车轮朝上，木板并排插在土里当障碍。”` — ra lệnh như bản kỹ thuật, không ai đáp.

**Kết** — *“第一个撞开辕门的人，赏魔晶十颗！”*
- Ai muốn gì: 奥德 muốn cứu 800 quân tinh nhuệ (đoạn cắt vào đầu nó có, đúng kiểu mẫu).
- Đổi gì: địch nổi điên, toàn tuyến xung phong.
- Đáng nhớ: *“两百米！人类的弓手怎么可能打到两百米开外？”* — câu hỏi trong đầu địch.
- Bỏ qua được: ba dòng tả 嗜血豺狼人 (`身高都在两米以上，胸前套着厚重的熟牛皮甲`) — trang trí.

**Phán bằng lời:** bản này **viết được trận**, sạch tật, nhịp gần mẫu (20,2 so với 23,3). Nhưng nó là **biên
bản tác chiến**, không phải truyện của bộ mẫu: người kể trung tính, không châm, không hỏi người đọc, MC không
tự gọi mình là 老爷, và **không có cuốn sổ riêng** (exp, mạng, đường rút) — thứ làm nên cả giọng lẫn cái sướng
của mẫu. Ba chỗ cần sửa nằm ở SI, không ở prompt.

## 3. Nguyên nhân, đọc từ thinking

Thinking mở đầu: *"short paragraphs and a limited omniscient perspective, heavy on action nouns and verbs"*,
rồi tự nhắc *"removed tone labels and intensifiers, limiting paired negation and idioms"* — tức nó đọc SI thành
**checklist 5 dòng BANS**, và đọc cảnh thành *"tactical deployment"*. Không có dòng nào nhắc "người kể đứng về
phía MC", "sổ riêng", dù SI có nguyên tắc 3 — vì nguyên tắc 3 chỉ mô tả người kể, không nói **nó phải xuất
hiện bao nhiêu lần** và **nói về cái gì** (cái anh ta đang đếm). Bài học quen thuộc: luật viết dạng mô tả thì
model bỏ qua, luật viết dạng **đếm được** thì nó theo.

## 4. SI v2 — bốn sửa, một biến mỗi lần

| # | sửa gì | ở đâu | thay bằng gì (đếm được) |
|---|---|---|---|
| 1 | Người kể phải nói hộ sổ riêng | PART 2, thêm 2 dòng | "Sau tiếng nói công khai của MC, người kể nói một dòng cái anh ta thật sự đang đếm (exp, mạng, đường rút). Một lần mỗi cảnh." + "Một câu tự gọi 老爷 kiểu 他罗伯森老爷, một câu hỏi cho người đọc, mỗi chương." |
| 2 | Chống vụn dòng | LENGTH | "Hai dòng trong ba dưới ba mươi chữ; dòng còn lại chạy hai tới ba mệnh đề." (bản ra 77% dòng ngắn) |
| 3 | Bảng in đúng dạng | PART 4 | một entry một dòng, `宿主` giữ ngoặc tước vị; exp spam in thành dòng `叮！…经验加300。` tối đa 3 dòng rồi tóm một câu |
| 4 | Độ dài | LENGTH | 2.000–2.200 (bản ra 2.645 = +27%) |

Chưa sửa: số lượt thoại (30 so với 17). Theo `references/si-test-tren-mau.md` mục 4, đây là **dữ kiện của
prompt**, không phải luật SI — brief test cố ý không có dòng tỷ lệ, nên lần chạy này không dùng để kết luận
về thoại.

## 5. Giới hạn của lần test này

- Một cảnh, một lần chạy. Biên độ nhiễu giữa hai lần chạy cùng SI chưa đo — muốn nhận công cho SI v2 thì phải
  chạy lại đúng prompt này **hai lần** và so hai bản sinh với nhau trước khi so với mẫu.
- Brief cố ý bỏ động cơ cày exp của MC (để chỉ đo văn phong). Nên "thiếu sổ riêng" có phần lỗi của brief; lần
  chạy SI v2 sẽ thêm **một dòng dữ kiện** "hắn đang cày exp" vào brief để tách lỗi brief khỏi lỗi SI.
- Cảnh ch8 là cảnh trận; kết luận từ một cảnh trận không suy ra được cho cảnh bàn giấy (mẫu có rất nhiều cảnh
  bàn giấy về sau).
