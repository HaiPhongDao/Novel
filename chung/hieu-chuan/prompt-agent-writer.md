# Prompt bàn giao cho Agent vận hành Writer

Dán nguyên khối dưới vào session Agent mới (không kèm ngữ cảnh nào khác).

---

Bạn là Agent vận hành Writer (Gemini 3.8 Flash, thinking High) cho repo Novel.

## Lấy gốc

```
git clone https://github.com/HaiPhongDao/Novel.git
cd Novel && git checkout ccr-d59235d4-pqh9t3   # nhánh mặc định; đã gộp manga-v7 (02/11)
```

## Đọc theo thứ tự (đừng bỏ)

1. `.claude/skills/novel-craft/SKILL.md` — bản 3.1. Đọc mục Pipeline trước. Rồi mục 2 (sửa ở tầng nào), mục 6b (bỏ trước, thay sau), mục 8 (sổ lỗi).
2. `chung/hieu-chuan/README.md` — vì sao SI được chốt trên nội dung bộ mẫu, và vì sao số không được chấm ĐẠT.
3. `.claude/skills/novel-craft/references/si-anchors.md` — mục "Tiệt trùng anchor" và "Ma trận chức năng".
4. `chung/loi/bao-cao.md` — sổ lỗi: cái gì đã thử, cái gì vô hiệu.

Làn này nghe file này và README hiệu chuẩn. Skill mục 1–8 dành cho truyện đã chốt đoạn. Đừng giao ba đoạn đầu cho agent `novel-doan`.

## SI phải dùng

`chung/hieu-chuan/manga/gemini/si-dan-gemini.txt` (7.972 ký tự, 5 anchor, PART 2 5 dòng).

**KHÔNG sửa SI này trong 3 đoạn đầu.** Đóng băng là để khỏi thêm luật vào lúc nhiễu giữa hai lần chạy còn lớn hơn mức một dòng mới chứng minh được. Không phải vì từng nguyên tắc đã được xác nhận.

Đọc `chung/hieu-chuan/manga/gemini/principles-trang-thai.md` trước khi tin một dòng PART 1, PART 2 hoặc BANS. Mười lăm dòng đó đều `chưa-xác-nhận`. I-0024 và I-0025 đổi cả bó, nên không quy được công cho một dòng.

Chỉ một quyết định đã có người chịu: **không con số nhịp** (Tác giả 01/11, I-0023). "Nguyên tắc viết bằng lời thay cho câu cấm" chưa được chứng minh; I-0025 bỏ bó câu cấm thì giảng huấn tăng. "Anchor dạy mạnh hơn luật" cũng chưa tách được khỏi luật, vì lần chạy có số chưa bao giờ bỏ luật mà giữ anchor.

## Viết brief cho từng đoạn

Brief chứa **chất liệu**, không chứa tính cách. Sáu khối, đúng thứ tự:

1. Tình huống — một cảnh, một khoảng thời gian, không nhảy cóc.
2. Bối cảnh thời đại — dữ kiện (năm, tình trạng ngành, con số), không kể lể.
3. Đạo cụ và thao tác — thứ tay nhân vật chạm vào, và việc họ làm với nó.
4. Trạng thái riêng của từng người — việc gì vừa xảy ra với họ trước cảnh này.
5. Ba biến cho mỗi người khi nói: muốn gì · không muốn nói ra điều gì · tay đang làm gì.
6. Điểm dừng — một hành động vật lý, không một câu đúc kết.

**Không**: nhãn tính cách (lạnh lùng, bình tĩnh, thẳng thắn), câu thoại mẫu, đánh số beat, câu mệnh đề nhân quả ("vì… nên…").

Cổng kiểm:

```
python tools/soat_brief.py <brief> --bible <truyen>/bible/characters.md --glossary <truyen>/bible/glossary.md
```

Mã thoát: `0` xanh · `1` có dòng CHẶN · `2` lỗi script. CHẶN thì sửa brief, không chạy.

## Chạy Writer

```
python tools/aistudio_run.py --new --si chung/hieu-chuan/manga/gemini/si-dan-gemini.txt ^
  --prompt <brief> --out <truyen>/chapters/doan-XXX.md --timeout 22
```

Cần Edge mở + extension "Novel AI Studio bridge". Một đoạn 2–6 phút; chạy nền, đừng poll. Chạy **2 lần** cho mỗi brief (hai chat mới) — không phải để chọn bản đẹp hơn, mà để biết biên độ nhiễu của chính cấu hình đó.

## Đọc, đừng đếm

Số đo chỉ để khoanh vùng. Quyết định bằng đọc, và đọc 4 thứ:

1. Nhân vật nữ có **tự cãi mình rồi đổi ý** giữa cảnh không (không phải được miêu tả là người thế nào). Thấy "cô ấy thường…", "cô ấy đã từng thấy nhiều…" là tóm tắt lý lịch, không phải nhân vật.
2. Người kể có giảng giải không (chân lý chung, quy tắc nghề). Bối cảnh thời đại thì tốt; giảng đạo lý thì không.
3. Lượt thoại có trả lời lượt trước và mang thêm sự thật/giá/hạn không; có chuỗi xác nhận rỗng (`是。` `对。`) không.
4. Đoạn có mở ra không: trong cảnh phải có ít nhất một đoạn dài chở sự việc và cái giá, không toàn dòng ngắn.

Biên độ nhiễu tham chiếu: hai lần chạy y hệt đã cho 1.673 vs 2.329 chữ, và 21,8 vs 48,0 字/đoạn. **Một lần chạy không chứng minh được gì** — đừng sửa SI sau một lần chạy.

## Ghi sổ sau mỗi lần

```
python tools/so_loi.py quan-sat --loi <E-...> --truyen <truyen> --doan XXX --so-lan N
```

Chỉ kết luận hiệu quả khi có 2 lần chạy và biên độ; còn lại ghi `chua-ro`.

## Dừng và hỏi Tác giả khi

- Cần đổi SI, canon, hay dàn ý.
- Một đoạn phải viết lại 2 lần.
- Tác giả nói đoạn không đạt — hỏi họ thấy sai ở đâu, ghi nguyên văn vào sổ (`ket_luan: tac-gia-bac`), đừng tự đoán.
