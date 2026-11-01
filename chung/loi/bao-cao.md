# Sổ lỗi — bảng sinh tự động

Sinh bằng `python tools/so_loi.py bao-cao`. Đừng sửa tay; sửa file `.jsonl` rồi sinh lại.

- Kiểu lỗi: **42** · Lần quan sát: **132** · Can thiệp: **20** · Đích đã đặt: **12**

## Tỉ lệ có bằng chứng

- Can thiệp đã đo: **0/20** (0%)

- Hiệu quả (≥2.0 biên độ): **0** · Vô hiệu (<1.0 biên độ): **0** · Phản tác dụng: **0** · Bị Tác giả bác: **4** · Chưa đo: **16**


## Kiểu lỗi, số lần, và cái gì đã được thử

| Mã | Kiểu lỗi | Số chỗ | Số đợt | Can thiệp (tầng · kết luận · biên độ) |
|---|---|---|---|---|
| E-PROSE-01 | Phủ định lặp / song song | 66 | 30 | I-0001 · SI · chưa rõ · chưa đo |
| E-PROSE-06 | Thẻ thoại mở đầu mọi lượt | 61 | 18 | I-0009 · SI · chưa rõ · chưa đo |
| E-PROSE-03 | So sánh của người kể | 49 | 21 | — |
| E-PROSE-11 | Từ hiện đại lọt bối cảnh | 35 | 19 | — |
| E-PROSE-05 | Nhãn ngữ điệu thay nội dung | 27 | 19 | I-0004 · SI · chưa rõ · chưa đo |
| E-SI-03 | Neo đếm được bị đọc thành checklist | 24 | 2 | I-0011 · SI · chưa rõ · chưa đo<br>I-0014 · SI · chưa rõ · chưa đo |
| E-PROSE-07 | Câu cụt, chia đoạn quá vụn | 20 | 1 | I-0008 · SI · chưa rõ · chưa đo |
| E-BRIEF-02 | Brief đánh số beat hoặc giao nội dung thoại | 14 | 1 | I-0016 · BRIEF · chưa rõ · chưa đo |
| E-PROSE-04 | Khuôn 'động từ + 实' | 12 | 8 | I-0003 · SI · chưa rõ · chưa đo |
| E-CANON-03 | Thiếu đơn vị đo / thể chế trong glossary | 6 | 1 | — |
| E-PROSE-02 | Khuôn tương phản 不是…而是 / 既…也 | 6 | 6 | — |
| E-SCENE-01 | Thoại cụt, chưa trọn ý | 5 | 1 | I-0005 · BRIEF · chưa rõ · chưa đo<br>I-0019 · SI · Tác giả bác · chưa đo |
| E-SI-01 | Luật trong SI bị chép thành hình thức tu từ | 5 | 1 | — |
| E-CANON-02 | Xưng hô / register sai bối cảnh | 3 | 1 | I-0010 · SI · chưa rõ · chưa đo |
| E-GATE-01 | Máy soát bỏ sót | 3 | 1 | I-0015 · TOOL · chưa rõ · chưa đo |
| E-SCENE-04 | MC thuyết trình, văn chạy checklist | 3 | 1 | I-0017 · BRIEF · Tác giả bác · chưa đo |
| E-GATE-02 | Cổng xanh nhưng văn hỏng | 1 | 1 | I-0020 · TOOL · Tác giả bác · chưa đo |

### Chưa từng có quan sát (25 kiểu)

Kiểu lỗi đã đăng ký nhưng chưa có lần nào được ghi. Hoặc chưa gặp, hoặc gặp mà không ghi — cả hai đều là lỗ hổng của sổ, không phải bằng chứng là đã hết lỗi.

`E-BRIEF-01` Brief chứa mệnh đề nhân quả/diễn giải · `E-BRIEF-03` Brief dán raw State JSON / cả gói bàn giao · `E-BRIEF-04` Brief có câu tiếng Trung dài · `E-BRIEF-05` Brief thiếu khối nối tiếp · `E-BRIEF-06` Brief thiếu thân phận / dòng xưng hô · `E-BRIEF-07` Brief thiếu tỷ lệ thoại / lời kể · `E-CANON-01` Số liệu hoặc phép tính sai · `E-CANON-04` Bàn tay vàng vượt hợp đồng · `E-CANON-05` Tên riêng sai hoặc mượn từ anchor · `E-CANON-06` Nhân vật biết điều chưa được biết · `E-EDGE-01` Mối nối đứt giữa hai đoạn · `E-EDGE-02` Kết đoạn khép tròn · `E-EDGE-03` Độ dài lệch cửa sổ brief · `E-EDGE-04` Nhịp câu lệch chuẩn bộ mẫu · `E-EDGE-05` Đoạn mở bằng tên người quá dày · `E-PROSE-08` Giải thích thừa, câu chốt ý cuối đoạn · `E-PROSE-09` Sáo ngữ bộ mẫu và lượng từ mơ hồ · `E-PROSE-10` Từ phẩm chất của SI lọt vào văn · `E-SCENE-02` Thoại không chủ ngữ, không người nhận · `E-SCENE-03` Nhân vật chỉ nói việc · `E-SCENE-05` Điểm nhìn vượt ranh giới · `E-SCENE-06` Cảnh quyền lực leo thang sai · `E-SI-02` Anchor chứa đúng tật đang muốn chữa · `E-SI-04` Luật tích tụ, SI phình, chú ý loãng · `E-SI-05` SI thiếu nguyên tắc cho lời kể

## Giải pháp đã bị Tác giả bác (không gỡ thì sẽ được thêm lại)

| Can thiệp | Lỗi | Tầng | Mô tả | Nguồn |
|---|---|---|---|---|
| I-0017 | E-SCENE-04 | BRIEF | Giữ SI, viết lại prompt theo cách bộ mẫu bày chương (việc chở thông tin, MC tin sai trước khi bị lật) | KN33 · Tác giả thấy 'ổn' sau khi đổi prompt |
| I-0018 | E-SI-04 | SI | SI v4 → v4.1: thêm hai câu về lời thoại (+362 ký tự) | do-va-hoc.md · Tác giả chấm 'không đạt, kém hơn bản trước'; đã trả SI về v4 |
| I-0019 | E-SCENE-01 | SI | Siết 'lượt thoại tự đứng' quá tay thành thoại cụt | si-khung.md · Tác giả: 'cụt, trống không' |
| I-0020 | E-GATE-02 | TOOL | Dùng điểm số làm kết luận ĐẠT; thêm bước đọc tương tác hành vi trước khi báo cáo | KN36 · 'Càng không đạt, viết quá loạn xạ' |

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
