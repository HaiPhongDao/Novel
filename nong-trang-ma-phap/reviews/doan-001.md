# Review đoạn 001 — bốn bản

Đoạn mở truyện đầu tiên; mục đích của bốn lần chạy là chọn **hình dạng prompt + SI**, không phải chọn câu chữ.
Chấm bằng `tools/soat_van.py` + `scripts/do_nhip_cau.py` + `tools/cham_doan.py`; cột `cham` chỉ để soát hồi
quy, canon 0/10 là **nhiễu** (bộ chấm đòi `回大人` của lane 领主, truyện này dùng `神父` / `管事大人`).

| bản | SI | brief | 字 | 字/câu | lượt · 字/lượt | phủ định | so sánh | nhãn | bảng | cham |
|---|---|---|---|---|---|---|---|---|---|---|
| a | v1 (kiến thức, không bảng) | chi tiết, 7 cảnh đánh số | 2.170 | 19,5 | 19 · 18,7 | 1 | 1 | 0 | không | 54 |
| b | v1b (sửa 1 bullet) | chi tiết, 7 cảnh đánh số | 1.695 | 19,7 | 17 · 20,9 | 0 | 1 | 0 | không | 66 |
| c | v2 (bảng 经验) | ngắn v1 (~250 từ) | 1.244 | 16,4 | 15 · 9,7 | 0 | 0 | 0 | 1 khối | 52 |
| d | v2.1 (bảng 经验) | ngắn v2 (~330 từ, đích 1.900) | 2.138 | 21,3 | 15 · 25,9 | 2 | 0 | 0 | 1 khối | **78** |
| — | mốc so: `tram-cuoi/chapters/chuong-001-a.md` (Tác giả cho 100/100) | | 1.543 | 23,6 | 16 · 22,6 | 1 | 0 | 0 | — | — |

## Đọc bốn bản

**a (2.170 字)** — cảnh làng tốt (dê, phân ủ, luống ươm, Osric kể chuyện ong và con trai ở mỏ), nhưng có **bốn
chỗ người kể giảng**:
- `前世最寻常的急性痢疾，落在这穷乡僻壤就能轻易要了人命。` (thuật ngữ y học hiện đại trong lời kể)
- `神父嘴里的圣水，不过是混了薄荷脑和微量魔晶碎屑的井水罢了。` (giải thích thành phần)
- `盐巴补回泄掉的力气，甜蜜能顶两顿稀饭，水烧开了才能阻断疫病。` (ba vế giảng cơ chế)
- `魔晶能换来成堆的金币，却丝毫变不出半粒口粮。` (giảng kinh tế thế giới)
Ngoài ra `早已看不出前世敲键盘的痕迹` — nghề kiếp trước trong bible là ngoài đồng, không phải dân văn phòng.
Nguyên nhân nằm ở chính bullet tôi viết trong PART 4 v1: *"the mechanism is named once in plain narrator's
words"* — câu đó **mời** người kể giảng.

**b (1.695 字)** — sạch nhất về văn: 0 phủ định, không giảng khoa học, câu 19,7 字 (vẫn cụt hơn mốc 23,6),
nhịp chậm đúng ý (sương → cơ thể → sân → dê → phân ủ → luống ươm → hàng xóm). Lỗi canon: `他穿越到这处领地
刚满四十天` (领地 sai — anh là tá điền thuê 5 亩), `Ronan 伸手将摊在泥地上的妇人扶起` (Marta lúc đó đang
đứng, Writer tự đặt cô ta nằm), một chỗ capture hỏng: `不一整口生铁大锅烧得翻滚冒泡`.

**c (1.244 字)** — bản đầu có bảng. Hụt 17% so với cửa sổ, câu cụt nhất (16,4 字; 15 lượt thoại chỉ 9,7
字/lượt). Bảng bị **giảng**: `救下男童换来二十点经验，照看火塘又添了八点经验。想把普通村民训练成一阶，
足需要一百点经验才行。` Có nhãn ngữ điệu `淡淡说道` (tool bỏ sót, đọc ra). Cảnh đổ 圣水 vào nồi bị bỏ —
Writer cho `圣水早被 Ronan 倒掉`.

**d (2.138 字)** — bản có bảng và văn dày nhất: 25,9 字/lượt (mốc 22,6), 0 câu so sánh của người kể, 0 nhãn
ngữ điệu, mở chậm đúng nhịp Tác giả thích (sương → cửa → dê nhai lại → phân ủ ấm → luống ươm nứt hạt), cái
giá in đủ (2 银币 · 8 捆 · nửa hũ mật · một đêm), 圣水 **được đổ vào nồi** đúng beat, kết bằng việc (vác cào
đi về đống phân) chứ không bằng câu ngầu. Lỗi còn lại, cụ thể:
1. `“神父大人行行好…”` — sai xưng hô (glossary: `神父`, không `神父大人`); `大人` xuất hiện 2 lần.
2. `圣水不过是掺了微量明矾的井水，只有彻底烧开才好放心饮用。` — người kể giải thích thành phần, cùng tật
   với bản a (bullet "the mechanism is shown by his hands" chưa chặn hết).
3. `想要靠面板训练出一阶村民，眼下还得凑足一百点经验和三天的嚼裹。` — người kể giải thích bảng; đúng ra
   để con số tự nói (68 经验 / 100).
4. `堆肥的规矩容不得偷懒，少翻一次土，整堆粪料开春就会烂成一摊死泥。` — một câu châm ngôn nghề, đọc như
   sách dạy; cắt được.
5. Dài 2.138 字, hơn trần 2.100 38 字.

## Kết luận

- **Prompt ngắn chạy được**: bản d (ngắn ~330 từ, có bảng) cho văn dày nhất và giữ đúng beat; bản chi tiết
  đánh số 7 cảnh (a, b) không thắng được cột nào ngoài việc ra ít lỗi canon hơn.
- **Prompt ngắn + cửa sổ độ dài thấp thì hụt** (c: đích 1.500–1.800 → 1.244, −17%); nâng đích lên 1.900
  (cửa sổ 1.700–2.100) thì ra 2.138 (+2% trần) — tức đích trong prompt là **mốc trượt**, không phải trần.
- **Tật còn lại của d thuộc tầng SI**: người kể vẫn giải thích cơ chế/bảng khi có dịp. Sửa tiếp bằng cách
  cắt một luật (bullet nào đang mời giảng) chứ không thêm luật; đo lại bằng đúng brief này.
- Đề xuất: lấy **d** làm gốc, sửa tay 5 chỗ trên (xưng hô, 3 câu giảng, 38 字), rồi mới chạy đoạn 002.
