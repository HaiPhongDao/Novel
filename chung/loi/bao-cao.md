# Sổ lỗi — bảng sinh tự động

Sinh bằng `python tools/so_loi.py bao-cao`. Đừng sửa tay; sửa file `.jsonl` rồi sinh lại.

- Kiểu lỗi: **48** · Lần quan sát: **170** · Can thiệp: **48** · Đích đã đặt: **20**

## Tỉ lệ có bằng chứng

- Can thiệp đã đo: **15/48** (31%)

- Hiệu quả (≥2.0 biên độ): **5** · Vô hiệu (<1.0 biên độ): **8** · Phản tác dụng: **2** · Bị Tác giả bác: **8** · Chưa đo: **25**


## Kiểu lỗi, số lần, và cái gì đã được thử

| Mã | Kiểu lỗi | Số chỗ | Số đợt | Can thiệp (tầng · kết luận · biên độ) |
|---|---|---|---|---|
| E-PROSE-07 | Câu cụt, chia đoạn quá vụn | 448 | 3 | I-0008 · SI · chưa rõ · chưa đo<br>I-0022 · SI · đề xuất · chưa đo<br>I-0023 · SI · Tác giả bác · chưa đo<br>I-0027 · SI · đề xuất · chưa đo |
| E-PROSE-06 | Thẻ thoại mở đầu mọi lượt | 105 | 22 | I-0009 · SI · chưa rõ · chưa đo<br>I-0038 · SI · phản tác dụng · 1.69× |
| E-PROSE-01 | Phủ định lặp / song song | 66 | 30 | I-0001 · SI · chưa rõ · chưa đo<br>I-0037 · SI · hiệu quả · 14.17× |
| E-PROSE-03 | So sánh của người kể | 55 | 23 | I-0036 · SI · hiệu quả · 2.94× |
| E-PROSE-11 | Từ hiện đại lọt bối cảnh | 35 | 19 | — |
| E-PROSE-05 | Nhãn ngữ điệu thay nội dung | 31 | 21 | I-0004 · SI · chưa rõ · chưa đo<br>I-0029 · SI · đề xuất · chưa đo |
| E-SI-03 | Neo đếm được bị đọc thành checklist | 24 | 2 | I-0011 · SI · chưa rõ · chưa đo<br>I-0014 · SI · chưa rõ · chưa đo |
| E-PROSE-12 | Nguoi ke giang giai (chan ly chung, giai thich nganh) | 22 | 6 | I-0025 · SI · phản tác dụng · 0.95×<br>I-0033 · SI · vô hiệu · 0.04×<br>I-0034 · SI · vô hiệu · 0.9×<br>I-0039 · SI · Tác giả bác · chưa đo |
| E-EDGE-06 | Luot thoai dai, thieu nhip trao doi | 21 | 1 | I-0021 · SI · đề xuất · chưa đo |
| E-SCENE-01 | Thoại cụt, chưa trọn ý | 17 | 2 | I-0005 · BRIEF · chưa rõ · chưa đo<br>I-0019 · SI · Tác giả bác · chưa đo<br>I-0024 · SI · hiệu quả · 9.0×<br>I-0028 · BRIEF · đề xuất · chưa đo |
| E-BRIEF-02 | Brief đánh số beat hoặc giao nội dung thoại | 14 | 1 | I-0016 · BRIEF · chưa rõ · chưa đo<br>I-0032 · BRIEF · chưa rõ · chưa đo |
| E-SCENE-07 | Nhan vat vo hon (chi day kich ban) | 14 | 7 | I-0030 · SI · đề xuất · chưa đo<br>I-0042 · SI · đang thử · chưa đo<br>I-0043 · SI · vô hiệu · 0.0×<br>I-0044 · SI · vô hiệu · 0.0× |
| E-PROSE-04 | Khuôn 'động từ + 实' | 12 | 8 | I-0003 · SI · chưa rõ · chưa đo |
| E-CANON-05 | Tên riêng sai hoặc mượn từ anchor | 10 | 4 | — |
| E-PROSE-13 | Nhan thai do bang danh tu truu tuong | 9 | 5 | I-0045 · SI · hiệu quả · 11.75×<br>I-0046 · SI · vô hiệu · 0.51× |
| E-EDGE-07 | Thieu boi canh thoi dai va nghe o doan mo | 8 | 1 | I-0031 · BRIEF · đề xuất · chưa đo |
| E-CANON-03 | Thiếu đơn vị đo / thể chế trong glossary | 6 | 1 | — |
| E-PROSE-02 | Khuôn tương phản 不是…而是 / 既…也 | 6 | 6 | — |
| E-SI-01 | Luật trong SI bị chép thành hình thức tu từ | 5 | 1 | — |
| E-GATE-01 | Máy soát bỏ sót | 4 | 2 | I-0015 · TOOL · chưa rõ · chưa đo |
| E-CANON-02 | Xưng hô / register sai bối cảnh | 3 | 1 | I-0010 · SI · chưa rõ · chưa đo |
| E-SCENE-04 | MC thuyết trình, văn chạy checklist | 3 | 1 | I-0017 · BRIEF · Tác giả bác · chưa đo |
| E-BRIEF-08 | Brief cho người lạ trò chuyện ngay, không có lý do để người kia chịu nghe | 1 | 1 | — |
| E-EDGE-04 | Nhịp câu lệch chuẩn bộ mẫu | 1 | 1 | I-0013 · SI · chưa rõ · chưa đo<br>I-0035 · SI · hiệu quả · 2.64×<br>I-0041 · SI · Tác giả bác · chưa đo |
| E-GATE-02 | Cổng xanh nhưng văn hỏng | 1 | 1 | I-0020 · TOOL · Tác giả bác · chưa đo |

### Chưa từng có quan sát (23 kiểu)

Kiểu lỗi đã đăng ký nhưng chưa có lần nào được ghi. Hoặc chưa gặp, hoặc gặp mà không ghi — cả hai đều là lỗ hổng của sổ, không phải bằng chứng là đã hết lỗi.

`E-BRIEF-01` Brief chứa mệnh đề nhân quả/diễn giải · `E-BRIEF-03` Brief dán raw State JSON / cả gói bàn giao · `E-BRIEF-04` Brief có câu tiếng Trung dài · `E-BRIEF-05` Brief thiếu khối nối tiếp · `E-BRIEF-06` Brief thiếu thân phận / dòng xưng hô · `E-BRIEF-07` Brief thiếu tỷ lệ thoại / lời kể · `E-CANON-01` Số liệu hoặc phép tính sai · `E-CANON-04` Bàn tay vàng vượt hợp đồng · `E-CANON-06` Nhân vật biết điều chưa được biết · `E-EDGE-01` Mối nối đứt giữa hai đoạn · `E-EDGE-02` Kết đoạn khép tròn · `E-EDGE-03` Độ dài lệch cửa sổ brief · `E-EDGE-05` Đoạn mở bằng tên người quá dày · `E-PROSE-08` Giải thích thừa, câu chốt ý cuối đoạn · `E-PROSE-09` Sáo ngữ bộ mẫu và lượng từ mơ hồ · `E-PROSE-10` Từ phẩm chất của SI lọt vào văn · `E-SCENE-02` Thoại không chủ ngữ, không người nhận · `E-SCENE-03` Nhân vật chỉ nói việc · `E-SCENE-05` Điểm nhìn vượt ranh giới · `E-SCENE-06` Cảnh quyền lực leo thang sai · `E-SI-02` Anchor chứa đúng tật đang muốn chữa · `E-SI-04` Luật tích tụ, SI phình, chú ý loãng · `E-SI-05` SI thiếu nguyên tắc cho lời kể

## Giải pháp vô hiệu hoặc phản tác dụng — phải gỡ, không được nâng thành luật

| Can thiệp | Lỗi | Tầng | Trước → Sau | Biên độ | Kết luận |
|---|---|---|---|---|---|
| I-0026 | E-SCENE-03 | BRIEF | 23.0 → 28.5 | 6.5 | vo-hieu |
| I-0033 | E-PROSE-12 | SI | 0.73 → 0.67 | 1.45 | vo-hieu |
| I-0034 | E-PROSE-12 | SI | 1.255 → 0.68 | 0.64 | vo-hieu |
| I-0043 | E-SCENE-07 | SI | 0.0 → 0.0 | 0.5 | vo-hieu |
| I-0044 | E-SCENE-07 | SI | 0.0 → 0.0 | 0.5 | vo-hieu |
| I-0046 | E-PROSE-13 | SI | 0.35 → 0.0 | 0.69 | vo-hieu |
| I-0047 | E-SI-05 | SI | 0.0 → 1.0 | 2.0 | vo-hieu |
| I-0048 | E-SI-05 | SI | 1.0 → 0.5 | 2.0 | vo-hieu |
| I-0025 | E-PROSE-12 | SI | 0.82 → 1.86 | 1.1 | phan-tac-dung |
| I-0038 | E-PROSE-06 | SI | 0.5 → 14.0 | 8.0 | phan-tac-dung |

## Giải pháp đã bị Tác giả bác (không gỡ thì sẽ được thêm lại)

| Can thiệp | Lỗi | Tầng | Mô tả | Nguồn |
|---|---|---|---|---|
| I-0017 | E-SCENE-04 | BRIEF | Giữ SI, viết lại prompt theo cách bộ mẫu bày chương (việc chở thông tin, MC tin sai trước khi bị lật) | KN33 · Tác giả thấy 'ổn' sau khi đổi prompt |
| I-0018 | E-SI-04 | SI | SI v4 → v4.1: thêm hai câu về lời thoại (+362 ký tự) | do-va-hoc.md · Tác giả chấm 'không đạt, kém hơn bản trước'; đã trả SI về v4 |
| I-0019 | E-SCENE-01 | SI | Siết 'lượt thoại tự đứng' quá tay thành thoại cụt | si-khung.md · Tác giả: 'cụt, trống không' |
| I-0020 | E-GATE-02 | TOOL | Dùng điểm số làm kết luận ĐẠT; thêm bước đọc tương tác hành vi trước khi báo cáo | KN36 · 'Càng không đạt, viết quá loạn xạ' |
| I-0023 | E-PROSE-07 | SI | Tac gia bac huong 'lay so do nhip lam cong chot SI': bo khoi LENGTH khoi writer/SI-template (v6), khong thay bang khoi so nao. Nhip do anchor va nguyen tac viet bang loi ganh | Tac gia 01/11: 'Con so dem la vo nghia trong van hoc. No chi khien Writer kem di thoi. Neu phan SI khac viet tot, Anchor dung thi khong can den khoi Length do.' |
| I-0039 | E-PROSE-12 | SI | Muc 2 PART 1 (luat, so, quyet dinh thanh chuoi cau) them vao SI loi. Tac gia doc 02/11: 'L2 vo dung, co khi con phan tac dung'. Giang huan 0,15 -> 0,65 (1,7 bien do, cung chieu) | manga-osaka-1999/gemini/test-giong/lop/ch01-L-2-a/b, ch01-L-4-a/b (bang-so.md) |
| I-0040 | E-SI-04 | SI | Muc 4 PART 1 (cu bat roi nhanh) them vao SI loi. Tac gia doc 02/11: 'L4 la cua prompt ma' — cu bat do brief quyet, khong can khoi SI | manga-osaka-1999/gemini/test-giong/lop/ch01-L-2-a/b, ch01-L-4-a/b (bang-so.md) |
| I-0041 | E-EDGE-04 | SI | Khoi NARRATION (nhip doan) keo 字/doan ve khoang mau (I-0035) nhung Tac gia bac ca huong: 'Con so khong quan trong, cau dai hay ngan khong anh huong den chat luong van. Khong can SI ve van de nay.' Khong dua khoi NARRATION vao SI | Tac gia 02/11 sau I-0035 |

## Giải pháp đã chứng minh — được phép thành luật trong SKILL

| Can thiệp | Lỗi | Tầng | Trước → Sau | Biên độ | Hiệu quả | n |
|---|---|---|---|---|---|---|
| I-0037 | E-PROSE-01 | SI | 0.85 → 0.0 | 0.06 | 14.17× | 2 |
| I-0045 | E-PROSE-13 | SI | 0.29 → 0.76 | 0.04 | 11.75× | 2 |
| I-0024 | E-SCENE-01 | SI | 9.0 → 4.5 | 0.5 | 9.0× | 2 |
| I-0036 | E-PROSE-03 | SI | 1.06 → 0.0 | 0.36 | 2.94× | 2 |
| I-0035 | E-EDGE-04 | SI | 47.2 → 29.75 | 6.6 | 2.64× | 2 |

## Đích của từng chỉ số (nguồn: mẫu / Tác giả / nội bộ)

| Truyện | Chỉ số | Đích | Nguồn |
|---|---|---|---|
| manga-tokyo-1994 | phu-dinh-lap-cau | 1.39 lần/1.000 chữ Hán | mau |
| manga-tokyo-1994 | so-sanh-loi-ke | 0.114 lần/1.000 chữ Hán | mau |
| manga-tokyo-1994 | khuon-shi | 0.034 lần/1.000 chữ Hán | mau |
| manga-tokyo-1994 | nhan-ngu-dieu | 0.03 lần/1.000 chữ Hán | mau |
| manga-tokyo-1998 | phu-dinh-lap-cau | 1.39 lần/1.000 chữ Hán | mau |
| manga-tokyo-1998 | so-sanh-loi-ke | 0.114 lần/1.000 chữ Hán | mau |
| manga-tokyo-1998 | khuon-shi | 0.034 lần/1.000 chữ Hán | mau |
| manga-tokyo-1998 | nhan-ngu-dieu | 0.03 lần/1.000 chữ Hán | mau |
| manga-tokyo-2000 | phu-dinh-lap-cau | 1.39 lần/1.000 chữ Hán | mau |
| manga-tokyo-2000 | so-sanh-loi-ke | 0.114 lần/1.000 chữ Hán | mau |
| manga-tokyo-2000 | khuon-shi | 0.034 lần/1.000 chữ Hán | mau |
| manga-tokyo-2000 | nhan-ngu-dieu | 0.03 lần/1.000 chữ Hán | mau |
| manga-tokyo-2000 | the-thoai | 1.329 lần/1.000 chữ Hán | mau |
| manga-tokyo-2000 | luot-cut | 6.401 lần/1.000 chữ Hán | mau |
| manga-tokyo-1996 | phu-dinh-lap-cau | 1.39 lần/1.000 chữ Hán | mau |
| manga-tokyo-1996 | so-sanh-loi-ke | 0.114 lần/1.000 chữ Hán | mau |
| manga-tokyo-1996 | khuon-shi | 0.034 lần/1.000 chữ Hán | mau |
| manga-tokyo-1996 | nhan-ngu-dieu | 0.03 lần/1.000 chữ Hán | mau |
| manga-tokyo-1996 | the-thoai | 1.329 lần/1.000 chữ Hán | mau |
| manga-tokyo-1996 | luot-cut | 6.401 lần/1.000 chữ Hán | mau |
