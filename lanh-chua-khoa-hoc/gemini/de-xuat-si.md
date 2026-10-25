# Đề xuất cải tiến System Instruction — Lãnh Chúa Khoa Học

> **Trạng thái 25/10:** tiền đề đã chốt (A, thế giới riêng, CEO thương mại/tài chính). Bản dán thử đầu
> tiên ở `system-instruction-v0.md` (ROLE + FIXED CONVENTIONS + PART 1–4, **chưa có anchor**). File này
> giữ phần lý do và các đề xuất, gồm một đề xuất sửa `../writer/SI-template` (mục 2).
> Nguyên tắc giữ: viết khẳng định, không câu cấm, không ví dụ sai trong SI (KN03); lỗi để Agent soát
> trong `review-blacklist`.

## 1. Vấn đề gốc của thể loại này

Ba lỗi sẽ xuất hiện ngay từ đoạn 001 nếu SI không chặn, vì chúng là phản xạ của mọi model viết
"xây dựng / bàn tay vàng":

1. **MC tự làm được.** Model mặc định nhân vật chính hành động bằng tay. Hậu quả: mất toàn bộ căng
   thẳng của tiền đề.
2. **Model viết nghề nó không biết.** Cảnh rèn/nung sẽ thành mô tả quy trình nghe hợp lý nhưng sai kỹ
   thuật, và luôn đúng ý MC — không có chỗ cho thử-sai. Với truyện này lỗi nặng hơn: MC **không có**
   kiến thức kỹ thuật, nên mọi câu kỹ thuật trong miệng anh là lỗi canon.
3. **Kiến thức vào bằng bài giảng.** MC giải thích nguyên lý cho người làng, người làng "ồ" → đoạn
   thành bài giảng kinh tế, mất nhịp.

## 2. Đề xuất A — sửa `../writer/SI-template` (dùng chung)

Template ghi "mục không dùng thì xoá cả mục". Với truyện **không có** bàn tay vàng, PART 4 bị xoá
trắng → model tự lấp chỗ trống bằng một dạng hệ thống (bảng, giọng nói, "trong đầu hiện ra"). Đề xuất:
**thay vì xoá, thay bằng một mục PART 4 khẳng định cái đang có.** Nguyên văn đã dùng trong
`system-instruction-v0.md`:

```
PART 4 — THE PROTAGONIST'S ONLY ASSET

He carries nothing but what he already knows, and it arrives the way memory arrives: in the middle of a
problem, in his own words, in the register of the rooms he learned it in. It has no voice, no speaker,
no page, no list; nobody hands it to him and nobody confirms it. His knowledge is a judgement he has to
act on before he can be sure of it — and the story shows the cost when the judgement is wrong.
```

Dòng cuối là phần quan trọng nhất: nó biến "không có hệ thống" từ khoảng trống thành đặc điểm kể
chuyện (không ai xác nhận → phải hành động khi chưa chắc).

## 3. Đề xuất B — bốn dòng chuẩn thêm vào PART 2 (riêng truyện này)

```
- Work that needs hands belongs to the person with the hands. He sets the requirement, names the price
  and the deadline, and is handed the result; the flaw is found by whoever held the tool.
- A craft is described through what the watching character can check — the ring of the metal, the
  colour at the break, the number on the scale, how long the heat held — not as a procedure he never
  performs, and not in technical terms he never learned.
- Technical statements belong to the person who does the trade, in their own words; he answers with a
  price, a term, or a question, and his own account of how something works carries a buyer's margin of
  error until a craftsman corrects it.
- Knowledge enters through a decision with a deadline on it: what to test first, what to refuse, what
  to promise and who carries the risk. Explanation covers the part he is deciding on right now.
```

## 4. Đề xuất C — mục "điểm nhấn" (PART 1 mục 4)

Truyện không có cảnh đánh nhau, nên điểm nhấn là **lúc một con số đứng vững**: hai bên cùng đong một
bao và ra cùng một số; một lô hàng qua được lần thử mà không ai tin là qua được; một chữ ký được người
mua nhận. Cơ chế: **nói giảm** (template 4b) — sự kiện được kể bằng đúng giọng đoạn văn quanh nó, sức
nặng đến từ phản ứng người chứng kiến: người thua phản ứng chậm hơn đáng lẽ, người mua ký mà không nói
gì, Halvard im.

KHÔNG dùng "bẻ giọng" cho truyện này: model sẽ biến mỗi con số thành câu chốt hạ, và đoạn nào cũng có
một câu chốt hạ thì không còn câu nào đáng nhớ.

## 5. Đề xuất D — vật mang chuẩn phải có tên cố định

Đấu chuẩn, cái cân, tấm lô đầu tiên là nhân vật phụ bằng gỗ và đá: chúng quay lại nhiều đoạn, mỗi lần
mang thêm nghĩa. Câu đã đưa vào FIXED CONVENTIONS mục 2 của SI v0:

```
Objects that carry a standard keep one name and one Latin spelling every time they appear, the same
way a person's name does.
```

## 6. Đề xuất E — thoại đàm phán (AGENT.md 4.11; SI không sửa được)

Cảnh bán hàng dễ thành màn thuyết trình. Khi viết brief: cho mỗi bên một mối bận tâm cụ thể (người mua
đang trễ một đơn khác; người bán còn 40 ngày; Sela sợ phải nói "không đạt"), không giao trình tự "MC
trình bày ưu điểm → đối phương bị thuyết phục".

## 7. Việc phải làm trước khi chốt SI

1. ~~Cần 2–3 đoạn mẫu (anchor)~~ **Xong 25/10**: đã lấy nguyên văn từ hai truyện cùng dòng và dán vào
   `system-instruction-v1.md`; 6/6 anchor đã đối chiếu tự động với nguồn, khớp từng chữ (xem
   `../archive/truyen-tham-khao.md`). Anchor lấy từ `放开那个女巫` ch.1, 12, 24, 36, 47 và
   `异界领主生活` ch.第一桶金4; đã chuẩn hoá `――`→`——`, không thêm thụt đầu dòng vì nguồn web không có.
2. Viết thử đoạn 001 hai bản ở hai session riêng với SI v1, để Tác giả đọc. Sau đó mới xét bỏ mục nào
   cả hai bản đã làm đúng.
3. Độ dài: SI v1 phần dán vào Gemini **12.192 ký tự** (SI lanh-chua-chip v2 khoảng 10.800, chạy ổn
   trên Gemini 3.8 Flash). Nếu cần ngắn lại thì nén chữ nguyên tắc, giữ anchor.
4. KHÔNG đưa vào SI: tên phường hội, số nợ, tên nhân vật phụ, hay bất kỳ chi tiết cốt truyện nào.
5. Cảnh báo khi dùng anchor: `放开那个女巫` có MC tự tay làm nghề và tự giảng kỹ thuật — truyện mình cấm
   đúng hai việc đó. Anchor chỉ mang nhịp, số, cách báo cáo, cách hỏi. Nếu bản thử cho thấy Writer bắt
   chước tật "MC làm tay", bỏ anchor mục 2 trước.

## 8. Bản v2 — làm lại theo `D:/Claude/builder` (25/10)

Hai file của Tác giả đổi cách làm SI, không chỉ đổi nội dung:

| Việc | Nguồn | Đã áp dụng |
|---|---|---|
| Ngân sách SI ~2.000 token, anchor tốn token ngang một nguyên tắc | KB §1.2 | SI v2 còn 7.231 ký tự (v1: 12.288), 3 anchor |
| Tối đa 2–3 anchor, mỗi anchor phải là mini-scene | KB §1.6 | chọn ch.1 (nhịp), ch.24 (báo cáo + phản đối), 异界 (giá) |
| PRINCIPLES khẳng định, CONSTRAINTS riêng, ≤8 luật | KB §1.3 | PART 1 bảy nguyên tắc; PART 2 sáu luật |
| Độ dài một output ~1.000 字, trần ~1.500; quá ngưỡng thì nửa sau trôi | KB §2.1 | đích 1.500 字; A/B xin 2.000 đều ra 2.870 |
| Prompt 5 slot: state → 2–3 beat → ranh giới cứng → số → độ dài | KB §5.1 | `briefs/doan-001-v3.md` |
| Không đưa phẩm chất văn vào prompt | KB §5.3 | prompt chỉ còn sự việc + số |

**Anchor đã bị loại sau khi quét `tools/soat_van.py`:**

- ch.1 bản cũ: chứa "都不见了 ×3" → dạy bộ ba phủ định. Thay bằng cửa sổ 4 đoạn sạch.
- 异界 bản cũ: chứa "而不是20枚" → dạy khuôn 不是 A 而是 B. Thay bằng đoạn trả giá khô.
- ch.12 (nung lò) và ch.47 (điều khoản): bỏ khỏi SI, đưa vào hàng chờ (dưới).

**Hàng chờ (chưa dán, thêm khi có mục tiêu rõ):**

- ch.47 契约 10/2 银龙 → cho đoạn bán hàng đầu tiên (khoảng đoạn 009).
- ch.36 (đoán sai động cơ người đối diện) → nếu Writer để MC đoán đúng người quá dễ.
- ch.12 (kiểm bằng tay, mắt, búa) → nếu Writer tả nghề mà không có ai kiểm.

**Đo sau khi đổi:** phủ định lặp 5 → 0; mật độ 没 7,3 → 3,8/1.000 chữ; độ dài 2.866 → 1.834; tên Latin
giữ đúng; phép tính đúng. Chi tiết: `../reviews/doan-001.md`.

**Lưu ý còn treo:** builder đề nghị 1 output ~1.000 字, repo đang định nghĩa đoạn ~2.000 字. Truyện này
tạm dùng 1.500. Nếu giữ 1.500 thì một "đoạn" của repo thành 1,5 output — cần Tác giả quyết có đổi đơn vị
đoạn cho cả repo hay chỉ cho truyện này.
