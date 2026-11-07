# Mổ xẻ tổng quan — 乱世荒年：我每日一卦粮肉满仓！

- **Tác giả:** 风起于渊
- **Quy mô:** 174 chương — 307.418 chữ Hán (trung bình ~1.767 chữ Hán/chương).
- **Nền tảng & Thể loại:** 番茄/七猫 — 古代乱世荒年 / 山野猎户种田 / 每日卜卦流 / 积粮争霸.
- **File nguồn:** `co-dai/乱世荒年：我每日一卦粮肉满仓！⊙1-174.txt`

## 1. Thế giới & Bối cảnh thời đại
- **Triều đại & Niên hiệu:** Đại Chu (`大周`), năm Hưng Nghiệp thứ 18 (`兴业十八年`). Triều đình suy vi, chiến sự biên ải liên miên, thuế khóa nặng nề, cộng thêm đại hạn và mùa đông tuyết lớn làm mất mùa diện rộng.
- **Không gian khởi điểm:** Thôn Tam Sơn (`三山村`) thuộc huyện Vĩnh Niên (`永年县`), nằm dưới chân ba ngọn núi Đen (`小黑山`, `二黑山`, `大黑山`).
- **Áp lực sinh tồn:** Nạn đói hiện hữu ngay trong từng bát cháo kê loãng chỉ lác đác vài chục hạt (`粟米粥`), từng củi đốt sưởi ấm, và khoản nợ lương thực vay nặng lãi `九出十三归` (vay 10 cầm 9 trả 13). Không đi săn hoặc kiếm được thức ăn thì cả nhà 6 miệng ăn sẽ chết đói hoặc chết cóng trước khi qua mùa đông.

## 2. Cơ chế Kim thủ chỉ (Khối dữ liệu trạng thái phi văn tự sự)
- **Nguồn gốc:** Tấm quy giáp cổ phác (`古朴龟甲`) gia truyền họ Giang dung hợp vào thức hải Giang Trần khi xuyên không.
- **Định dạng hiển thị:** Luôn xuất hiện dưới dạng các dòng dữ liệu trạng thái đóng khung ngoặc vuông `【...】` độc lập, phi văn tự sự:
  - Dòng mệnh tinh (khi kiểm tra hoặc thăng cấp): `【当前命星：山民】` (về sau tiến hóa theo thế lực và địa vị).
  - Dòng vận thế tổng quan trong ngày: `【今日运势：平】` (hoặc `小吉`, `中吉`, `大吉`, `小凶`...).
  - Ba thẻ tre (`三根竹签` / `卦签`) hiện ra 3 lựa chọn hành động kèm mức cát/hung và địa điểm/thời gian cụ thể:
    - `【小吉：小黑山南边山腰，一只迷路的兔子撞死在雪地中，午时之前去或许会有所收获。】`
    - `【中吉：小黑山西边山脚，有一处野鸡窝，里面有三只野鸡，可前往抓捕。】`
    - `【大凶：二黑山深处，有一头刚生产完的母熊，极其狂暴，前往必死无疑！】`
- **Quy tắc vận hành:**
  1. Mỗi ngày chỉ bói được 1 lần (`每日一卦`) và chỉ được chọn **1 trong 3** thẻ tre.
  2. Khi chọn 1 thẻ, thẻ đó hóa thành luồng sáng truyền thẳng bản đồ/hình ảnh vị trí vào đầu Giang Trần; 2 thẻ còn lại lập tức biến mất, quy giáp tối sầm lại chờ qua ngày hôm sau.
  3. **Tính chất phi văn tự sự:** Quy giáp không có ý thức, không đối thoại, không giảng giải; toàn bộ việc cân nhắc rủi ro (tại sao không chọn `中吉` hay `大凶` mà chọn `小吉`) đều diễn ra trong chuỗi suy tính thực tế của Giang Trần sau khi nhìn quẻ.

## 3. Chỉ số nhịp tự nhiên của bộ mẫu (30 chương đầu & Hoàng Kim Tam Chương)

| Chỉ số | Chương 1 | Chương 2 | Chương 3 | Chương 4 | Baseline 30 chương đầu (TB ± SD [TB ± 2SD]) |
|---|---|---|---|---|---|
| Số chữ Hán (`han`) | 898 | 1.710 | 1.002 | 1.349 | 1.626,2 ± 273,3 [1.080 – 2.173] |
| Số đoạn | 46 | 88 | 45 | 66 | ~77 đoạn |
| Chữ Hán / đoạn (`han_doan`) | 19,5 | 19,4 | 22,3 | 20,4 | **21,12 ± 1,13 [18,8 – 23,4]** |
| Độ dài đoạn tối đa (`doan_max`) | 42 | 44 | 48 | 54 | **49,67 ± 9,79 [30,1 – 69,2]** |
| Chữ Hán / câu (`han_cau`) | 19,9 | 16,4 | 15,4 | 17,4 | **17,52 ± 1,56 [14,4 – 20,6]** |
| Số lượt thoại (`luot`) | 6 | 23 | 29 | 19 | **33,00 ± 12,02 [9,0 – 57,0]** |
| Chữ Hán / lượt thoại (`han_luot`) | 14,0 | 15,8 | 11,2 | 14,2 | **12,53 ± 2,49 [7,5 – 17,5]** |
| Tỷ lệ đoạn có thoại (`ti_le_thoai`) | 13% | 26% | 58% | 26% | **39,90% ± 13,03% [13,8% – 66,0%]** |
| Giảng huấn / 1.000 chữ | 0,0 | 0,0 | 1,0 | 0,0 | **0,11 ± 0,26 [0,0 – 0,6]** |
| Tật `so-sanh-nguoi-ke` / `khuon-shi` / `nhan-ngu-dieu` | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | Rất sạch (toàn bộ 174 chương: `nhan-ngu-dieu` 0,02/1000, `khuon-shi` 0,06/1000) |

## 4. Đặc trưng bút pháp & Ngữ khí
1. **Nhịp đoạn ngắn, một nhịp một đoạn (`One beat, one paragraph`):** Trung bình ~21 chữ Hán/đoạn, đoạn dài nhất chương chỉ ~45–50 chữ. Mỗi hành động nhỏ (cầm bát, chống nạng, nhìn tuyết, tính sổ nợ) tách thành một đoạn riêng.
2. **Độc thoại nội tâm trực tiếp không cần nhãn:** Các câu tự nhủ, tính toán của Giang Trần đặt thẳng trong ngoặc kép `“...”` đứng độc lập thành một đoạn hoặc hòa vào lời kể mà không dùng `他心想`, `他暗道`.
3. **Từ nối suy tính thực dụng:** Chuỗi suy luận sinh tồn nối bằng `可` (4,49/1000), `要是` (1,13/1000), `不过` (1,01/1000), `只是` (0,69/1000), `若是` (0,45/1000), `果然` (0,24/1000).
4. **Thẻ thoại mộc mạc:** Chủ yếu dùng `开口` (1,96/1000), `道：` (0,81/1000), `摇头` (0,29/1000), `问：` (0,27/1000), `说道` (0,23/1000), không đính kèm trạng từ chỉ ngữ điệu kiểu `淡淡地说`, `平静地开口`.
