# SI cho truyện không hệ thống / MC không biết nghề

Dùng khi truyện có tiền đề "không bàn tay vàng" hoặc MC **biết nguyên lý mà không tự tay làm được**. Vấn đề gốc: model mặc định MC hành động bằng tay và tự tin về kỹ thuật.

## 1. Không xoá trắng PART 4

Template ghi "mục không dùng thì xoá". Với truyện không có bàn tay vàng, chỗ trống đó bị model lấp bằng một dạng hệ thống ngầm (bảng, giọng nói, "trong đầu hiện ra"). Thay bằng khối khẳng định:

```
PART 4 — THE PROTAGONIST'S ONLY ASSET

He carries what he already knows, and it arrives the way memory arrives: in the middle of a problem, in
his own words, in the register of the rooms he learned it in. It comes with a judgement he has to act
on before he can be sure of it, and the story shows the cost when the judgement is wrong.
```

Dòng cuối biến "không hệ thống" từ khoảng trống thành đặc điểm kể chuyện: không ai xác nhận → phải hành động khi chưa chắc.

**Đừng liệt kê thứ nó không có.** Bản cũ của khối này viết "It has no voice, no speaker, no page, no list; nobody hands it to him" — model chép đúng hình thức đó vào văn thành `没有…，也没有…，只有…`, và cả hai bản thử đều ra 5 cặp phủ định. Muốn chặn thì mô tả thứ **đang có**, rồi thêm trần ở PART 2:

## 2. Bốn dòng chuẩn vào PART 2

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

Dòng 3 là dòng dễ mất nhất khi truyện có MC thương mại: mọi câu kỹ thuật trong miệng anh là **lỗi canon**, không phải chi tiết hay.

## 3. Điểm nhấn dùng "nói giảm", không "bẻ giọng"

Khoảnh khắc sảng thường là **lúc một con số đứng vững** (hai bên cùng đong ra cùng số; lô hàng qua thử; chữ ký được nhận). Kể bằng đúng giọng đoạn văn quanh nó; sức nặng đến từ phản ứng người chứng kiến. Nếu cho mỗi con số một câu chốt hạ, đoạn nào cũng có câu chốt hạ thì không còn câu nào đáng nhớ.

## 4. Vật mang chuẩn giữ một tên

Đấu chuẩn, cái cân, tấm lô đầu tiên là nhân vật phụ bằng gỗ và đá: quay lại nhiều đoạn, mang thêm nghĩa. Thêm vào FIXED CONVENTIONS:

```
Objects that carry a standard keep one name and one Latin spelling every time they appear, the same
way a person's name does.
```

## 5. Thứ tự làm

1. ROLE + FIXED CONVENTIONS + PART 2/3/4 (không anchor) → viết thử đoạn 001 hai bản ở hai session riêng.
2. Có 2–3 đoạn mẫu thật đúng register → dán anchor vào PART 1; mục nào cả hai bản đã làm đúng thì bỏ.
3. Không đưa vào SI: tên phe phái, số nợ, tên nhân vật phụ, chi tiết cốt truyện. Nhãn tính cách MC cũng không ("lý trí, lạnh lùng") — model sẽ diễn nhãn đó vào câu văn.

## 6. Kiểm khi review

- Đếm tật bằng script trước khi đọc cảm tính: `python tools/soat_van.py <truyen>/chapters/doan-XXX*.md`.
- Chuỗi phủ định song song quá 2 cặp/đoạn, hoặc khuôn `phủ định + phủ định + 只有/只是`, hoặc `不是 A，而是 B` đứng riêng → trả lại cho Writer một khuôn khác (tả bằng thứ tay đã làm), không chỉ gạch bỏ.
- Có câu kỹ thuật nào trong miệng MC không? → giao lại cho người làm nghề, cùng cảnh, cùng nhịp.
- MC có tự phát hiện ra tính chất vật liệu/nguyên lý mới không? → sai canon; người phát hiện là thợ hoặc người dùng, phần của MC là định giá và chịu trách nhiệm.
- Sai của MC có hiện trên trang và có người sửa không? → nếu không, model đang viết MC toàn tri.
