# Sổ lỗi — cách ghi để biết lần sửa nào có tác dụng

Sổ này trả lời bốn câu mà `chung/kinh-nghiem.md` không trả lời được:

1. **Mỗi kiểu lỗi đã xảy ra bao nhiêu lần?**
2. **Đã đưa ra những giải pháp nào, ở tầng nào?**
3. **Cái nào hữu hiệu, hữu hiệu bao nhiêu?** (đo bằng "số lần biên độ nhiễu", không bằng cảm nhận)
4. **Cái nào vô dụng hoặc phản tác dụng, và đã gỡ chưa?**

Chạy `python tools/so_loi.py bao-cao` để xem bảng trả lời cả bốn câu. Bảng đó **sinh tự động**; đừng sửa tay.

## Vì sao phải có sổ riêng

Vòng học cũ ghi "đã học được gì" vào `chung/kinh-nghiem.md`. Nó thiếu hai thứ khiến mọi kết luận không kiểm được:

- **Không có mã lỗi ổn định.** KN17, KN22 và KN08 cùng nói về một họ lỗi (prompt của Agent thành mẫu tu từ) nhưng
  không có gì nối chúng, nên không đếm được tái phạm.
- **Không có kết cục của can thiệp.** Bài học được ghi lúc đang tin nó đúng. Khi một lần sửa hoá ra vô hiệu, không
  có chỗ nào ghi điều đó — nên lần sau nó được thêm lại.

Đo trên dữ liệu cũ: 37 dòng KN, chỉ 15 dòng có dấu vết số đo, và **0 dòng** có đủ `trước/sau/biên độ/n` để tính hiệu
quả. 14 luật vẫn tái phạm sau khi đã được ghi thành luật.

## Bốn file

| File | Nội dung | Ghi bằng |
|---|---|---|
| `loai-loi.jsonl` | Danh mục kiểu lỗi, mã ổn định `E-<MIỀN>-<nn>` | `so_loi.py them-loi` |
| `quan-sat.jsonl` | Mỗi lần Writer mắc lỗi: lỗi nào, truyện nào, đoạn nào, **mấy chỗ** | `so_loi.py quan-sat` |
| `can-thiep.jsonl` | Mỗi lần sửa: lỗi nào, **tầng nào**, sửa gì, số trước/sau, biên độ, n, kết luận | `so_loi.py can-thiep` |
| `muc-tieu.jsonl` | Đích của từng chỉ số, **do ai đặt** (`mau` / `tac-gia` / `noi-bo`) | `so_loi.py muc-tieu` |
| `bao-cao.md` | Bảng tổng hợp — sinh tự động | `so_loi.py bao-cao` |

Mỗi dòng JSONL là một sự kiện, chỉ thêm, không sửa lịch sử. **Ngoại lệ duy nhất:** `phan-quyet` điền số `sau` vào
một can thiệp đã có — vì lúc đề xuất chưa có kết quả.

## Mã kiểu lỗi

`E-<MIỀN>-<nn>`, bảy miền:

| Miền | Nghĩa | Sửa ở đâu |
|---|---|---|
| `BRIEF` | Lỗi do Agent viết brief | brief, glossary, state |
| `SI` | Lỗi do luật trong system instruction | SI |
| `CANON` | Sự thật, số, nhất quán, xưng hô | brief hoặc bible (tuỳ) |
| `PROSE` | Câu chữ: phủ định, so sánh, nhãn, khuôn | brief → SI → review-blacklist |
| `SCENE` | Dựng cảnh, thoại, điểm nhìn | brief trước, SI sau |
| `EDGE` | Nối đoạn, độ dài, nhịp, mở đoạn | brief |
| `GATE` | Chính khâu đo sai: tool bỏ sót, cổng xanh mà văn hỏng | tool, hoặc quy trình review |

Mã **không đổi** khi cách sửa đổi. Muốn đổi tên thì đổi `ten`, giữ `id` — lịch sử gắn vào `id`.

## Ba trạng thái của một can thiệp

```
de-xuat  →  dang-thu  →  hieu-qua | vo-hieu | phan-tac-dung | chua-ro
                     ↘  tac-gia-bac   (Tác giả đọc và bác; cần nguyên văn câu bác)
```

### Đo hiệu quả bằng "số lần biên độ nhiễu"

```
số lần biên độ = |trước − sau| / biên độ
```

| Kết quả | Kết luận | Được làm gì |
|---|---|---|
| ≥ 2 biên độ | `hieu-qua` | Được nâng thành luật trong `SKILL.md` (kèm mã can thiệp) |
| < 1 biên độ | `vo-hieu` | **Phải gỡ** trong cùng phiên; ghi `log.md` |
| đi ngược chiều | `phan-tac-dung` | **Phải gỡ**; ghi lại để không ai thêm lại |
| chưa đủ 2 lần chạy | `chua-ro` | Không được nâng thành luật, chỉ nằm ở sổ |

**Biên độ lấy từ đâu:** hai lần chạy **y hệt** (cùng SI, cùng brief) trong hai chat mới. Chênh lệch giữa hai lần đó
là nhiễu. Chưa có hai lần chạy thì chưa có biên độ, tức là chưa có kết luận — chỉ được ghi `chua-ro`.

Lý do phải khắt khe: cùng một SI đã cho ra cả **0 và 5 cặp phủ định** ở hai lần chạy; một lần sạch hơn gần như luôn
là rút thăm may. Chi tiết và số đo: `../.claude/skills/novel-craft/references/do-va-hoc.md`.

### Vì sao cần `muc-tieu` — đích không phải số 0

Trước khi nói một chỉ số "cao", phải biết đích của nó. Đo bộ mẫu `我在泡沫东京画漫画.txt` (440.232 字 Hán):

| Chỉ số | Bộ mẫu (đích) | Ba truyện manga-tokyo | Đọc thế nào |
|---|---|---|---|
| `phu-dinh-lap-cau` | **1,39** /1.000 字 | 0,31–0,59 | **dưới** mẫu 4–6 lần — không phải tật, đừng chữa |
| `so-sanh-loi-ke` | 0,11 | 0–0,21 | ngang mẫu hoặc hơi trên |
| `khuon-shi` | 0,03 | 0–0,16 | một truyện cao **4,7 lần** mẫu |
| `nhan-ngu-dieu` | 0,03 | 0,11–0,62 | cao **3,7–20 lần** mẫu — đây là tật thật |

Ba bộ mẫu khác cũng cho `phu-dinh-lap-cau` ở 1,37–1,78. Nghĩa là **2–3 cặp phủ định mỗi đoạn là văn bình thường**
của truyện mạng Trung Quốc; đích "0 cặp" là đích sai, và mọi can thiệp chữa về 0 đều đang chữa một thứ không bệnh.

Đích có ba nguồn, và **phải ghi rõ nguồn** vì chúng xung đột nhau:

- `mau` — đo từ bộ mẫu của truyện. Đích mặc định.
- `tac-gia` — Tác giả dặn. **Thắng** `mau`.
- `noi-bo` — mốc của bản Tác giả đã duyệt. Dùng khi không có bộ mẫu.

## Quy trình một phiên

1. Review bản thảo, mỗi lỗi bắt được → `quan-sat` (một dòng, ghi rõ `so_lan` và `do_bang`).
2. Phân loại tầng sửa theo mục 2 của `SKILL.md`.
3. Sửa **một biến** → `can-thiep` (ghi `truoc`, `chi_so`; để trống `sau`).
4. Chạy lại 2 lần y hệt → `phan-quyet --sau … --n 2`.
5. Đọc `bao-cao`; can thiệp `vo-hieu`/`phan-tac-dung` → gỡ ngay.
6. `kiem-tra` phải sạch trước khi commit.

**Mở truyện mới: đặt đích bằng một lệnh, đừng đo tay.**

```
python tools/so_loi.py do-mau <truyen> --file <bo-mau.txt>
```

Nó chạy `soat_van.py` trên bộ mẫu, quy về mật độ/1.000 chữ Hán, và ghi 6 đích kèm nguồn `mau`. Làm bước này
**trước** khi viết brief đầu tiên; không có đích thì mọi nhận xét "chỉ số cao/thấp" ở review đều không kiểm được.
Biên độ mặc định = 50% giá trị đích — đó là số tạm, thay bằng số thật khi có hai lần chạy y hệt.

Chạy lại lệnh này cho các truyện đã có thì nó **ghi đè** đích nguồn `mau` của đúng truyện đó, không đụng truyện khác.

## Dữ liệu lịch sử trong sổ này

- 13 dòng `quan-sat` đầu là **đọc từ review và sổ kinh nghiệm** (nguồn ghi `KNxx`), không phải máy đo.
- 119 dòng tiếp là **máy đo**: `soat_van.py` quét 60 bản đã duyệt trong 6 truyện (2026-11-01).
- 20 dòng `can-thiep` là **lịch sử dựng lại** từ KN và review. Tất cả đều `chua-ro` hoặc `tac-gia-bac` vì repo
  không ghi đủ `n` và biên độ. Đây không phải lỗi của dữ liệu cũ — nó cho thấy đúng vấn đề: **chưa lần nào được đo
  đủ để tính hiệu quả**. Sổ mới bắt đầu có số từ phiên đầu tiên áp dụng quy trình này.

Đừng xoá các dòng `chua-ro` đó. Chúng là mức nền để so: nếu sau nhiều phiên mà tỉ lệ `hieu-qua` không tăng thì
quy trình vẫn chưa chạy, chứ không phải "đã ổn".
