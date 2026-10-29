# SI v13 — SI lõi dựng lại từ v9 theo `writer/SI-template` v5 (29/10)

**Trạng thái: bản đề xuất. SI đang dùng của truyện vẫn là v9** (`ky-kham-lanh-chua/gemini/si-dan-gemini.txt`). Đổi SI
hiện hành cần Tác giả đọc và duyệt, rồi ghi `log.md`.

## Số đo

| | ký tự | anchor | dòng PART 2 | BANS |
|---|---|---|---|---|
| v9 (đang dùng) | 15.185 | 7 | 20 | 5, có "checked by tools/soat_van.py" |
| `si.txt` (SI "tinh gọn" của 5 đoạn test) | 5.999 | 6 | 0 | 5, liệt kê từ + "Checked by machine tools" |
| **v13** | **7.997** | **5** | **6** | 5, khuôn thay thế, không liệt kê từ |

Ngân sách template v5: phần dán ≤ 8.000 ký tự, 4–5 anchor, PART 2 ≤ 8 dòng. Anchor: 5/5 khớp nguyên văn bộ mẫu
(`verify_anchors.py` trên `ky-kham-dan-thuong/mau-tham-khao.txt`), 0 tật (`soat_van.py`).

## Vì sao không phải "v9 + vá"

v9 có đủ mọi dấu hiệu phải reset ở `references/si-cau-truc.md` mục 10: quá 9.000 ký tự, PART 2 quá 8 dòng, nhiều dòng
sinh ra để chữa đúng một bản thảo (rượu mừng đám cưới, "steward whose ledger belongs to his father"). Bản "tinh gọn"
của test thì cắt nhầm: bỏ đúng nguyên tắc người kể đứng về phía MC (giọng thể loại), giữ luật đếm kích cỡ đoạn. v13
giữ phần mang giọng của v9 và cắt phần vá.

## Giữ từ v9

ROLE (gọn lại), FIXED CONVENTIONS (tên người Latin, địa danh và tước chữ Hán — glossary chốt 26/10), nguyên tắc 1
(nhịp đoạn), 3 (người kể đứng về phía MC + sổ kép), 6 (chuỗi lý lẽ), 4 (payoff) cùng anchor của chúng, BANS (khuôn
không liệt kê từ của v9), LENGTH (neo độ dài câu), PART 4.

## Mỗi thứ bỏ khỏi v9 đi đâu

| v9 | Ở v13 |
|---|---|
| Nguyên tắc 2 (so sánh thuộc nhân vật) + anchor 故宫 | BANS dòng 2 giữ luật. Anchor bỏ: nó cũng là mẫu "MC so bằng đời trước" — hướng PART 1B Tác giả đã gạt 26/10 |
| Nguyên tắc 7 (chuyển cảnh) + anchor | FIXED CONVENTIONS 3: dòng chấm đổi cảnh, đoạn sau đã ở trong cảnh mới |
| Nguyên tắc 5: "every spoken line carries a tag", anchor gắn thẻ hai lượt liền | Nguyên tắc 4 mới: thẻ ở chỗ cần, khoảng một lượt trong ba, không hai lượt liền một người; anchor mở đầu ch.8 |
| PART 2: thẻ thoại · lượt của MC mang nội dung · câu lệnh có 吧/去/给我 · câu từ chối nói với người trước mặt · lời chửi thầm đứng riêng | gộp vào nguyên tắc 4 |
| PART 2: "after a noble-sounding line…" · "one cool line to a segment" | gộp vào nguyên tắc 2 |
| PART 2: kế hoạch bằng phép tính · nền do người kể nói · mua bán ghi đơn vị | gộp vào nguyên tắc 3 |
| PART 2: định dạng bảng · bậc tăng từng bước | PART 4 |
| PART 2: "the men are the ledgers" | ROLE (accounts) |
| PART 2: danh sách xưng hô 大人/老爷/爵士/长官 | glossary + State — dữ kiện không nằm trong SI |
| PART 2: đáp chuyện ngoài việc (rượu mừng) | `chung/review-blacklist.md` mục "Nhân vật chỉ nói việc" + brief (chất liệu xã hội) |
| PART 2: mở cảnh bằng tiếng/mùi | bỏ — luật brief 28/10: chỗ mở là đuôi đoạn trước trong gói |
| LENGTH: "a speech turn is a complete sentence" | nguyên tắc 4 |
| LENGTH: "End on a bigger number, a bigger enemy, or a man walking in with news" | PART 3: dừng giữa động tác, khác kiểu dừng của đoạn trước (test 003 và 005 kết y hệt nhau) |
| PART 3: tên mục mẫu B (【Chuyện xảy ra…】【Những điểm bắt buộc】【Thiết lập】) | PART 3 chung cho mẫu A và B: tên/sự thật/số giữ nguyên, dòng cố định xảy ra như ghi, còn lại là của Writer |
| PART 3: "Character entrances: name, one line of identity, one physical feature" | nhân vật vào cảnh bằng việc đang làm, tên nằm trong câu hành động (test: 9 câu "那是 Cole。/来人是 Karl。" + tiểu sử) |
| PART 3: "This is fiction…" | bỏ — 5 đoạn test chạy cảnh treo cổ, chém giết không có dòng này |
| PART 4: khối mẫu 5 dòng; "new entry appears when…" | khối 3 dòng; thêm "chỉ in khi con số cảnh xoay quanh vừa đổi"; luật mục mới do Agent soát (blacklist mục Bàn tay vàng) |
| Anchor payoff: hai dòng bảng trong ngoặc kép “【…】” | cắt anchor trước hai dòng đó — ngược với PART 4 "no quotes" |

## Thêm mới (mỗi dòng có bằng chứng ≥2 lần)

- PART 2: MC chỉ nói điều đã thấy/nghe/đếm (test 002 "两百袋黑麦"; KN07: Pell, Mira).
- PART 2: người đứng đối diện dùng thứ mình có trước khi chịu thua (test: Gerry, 代守, Cole đều xếp trong 1–3 lượt;
  v9 đã có vế "may still refuse", v13 nói rõ hơn).
- BANS dòng 1: phó từ nhấn gắn vào **con số** (test: 整整/足足 = 3,0/1.000 字, mẫu ch.8: 0).
- BANS dòng 4: trạng từ trước động từ nói cũng là nhãn ngữ điệu (test: ~15 thẻ kiểu 低声/急促地/颤声 + 说道).
