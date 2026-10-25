# Phân tích bộ mẫu — `领主：我用骑砍系统肝经验`

Nguồn: `mau-tham-khao.txt` (bản sao của file txt trên Desktop, md5 `0b7e1a34…5d3d3`). Đo bằng script trên toàn bộ
sách, không đọc mẫu. Số dưới đây là số **của mẫu**, dùng làm mốc so cho bản mình viết.

## 1. Tình trạng file (đọc trước khi tin bất kỳ số nào)

| thứ | số | ghi chú |
|---|---|---|
| tiêu đề chương (`# 第N章`) | 935 | 49 chương thân chỉ ghi `下载失败` → **886 chương dùng được** |
| số chương duy nhất | 274 | số chương bị lặp/nhảy loạn, nhưng nội dung liền mạch một truyện (罗伯森 xuất hiện 17.674 lần, rải đều 9 khối 100 chương) |
| độ dài chương | trung vị **2.122 字** (min 2.010, max 12.908 — một chương gộp) | |
| tổng | 1.864.074 字 Hán | |

Kết luận: file **không hỏng nặng** như ghi chép cũ ("chỉ đọc được ch1 và ch8") — chỉ 49/935 chương mất thân.
Đánh số chương không dùng để tham chiếu; tham chiếu bằng **số chương + tên chương**.

## 2. Nhịp — bốn con số quyết định giọng

| chỉ số | mẫu (886 chương) | ch1 | ch8 |
|---|---|---|---|
| chữ / câu | **23,9** | 28,4 | 23,3 |
| dòng ≤ 30 字 | **65%** số dòng | 36% | 60% |
| lượt thoại / chương | **20** (trung vị) | 14 | 17 |
| chữ / lượt thoại | **22,4** | 29,6 | 19,6 |
| dòng là thoại (bắt đầu bằng `“`) | **23%** | | |

Đoạn của mẫu **ngắn và đều**: phần lớn là một dòng; dòng ≤ 6 字 đứng riêng để chốt một beat (`什么情况？`);
cứ vài beat mới có một đoạn 2–3 câu gánh một chuỗi lý lẽ hoặc một khối nền. Không có đoạn tableau tả cảnh.

## 3. Từ vựng — đo mật độ /1000 字 (quy ra /chương)

| dấu hiệu | tổng | /1000 字 | ~/chương |
|---|---|---|---|
| thẻ thoại `说道` | 2.292 | 1,06 | **2,2** |
| `问道` | 995 | 0,46 | 1,0 |
| `笑道` | 494 | 0,23 | 0,5 |
| `他罗伯森老爷` (tự gọi mình bằng 老爷) | 1.197 | 0,64 | **1,35** |
| câu hỏi tu từ / hỏi thẳng người đọc (`为什么…呢？`) | 697 | 0,37 | **0,79** |
| `毕竟` / `要知道` / `更别说` | 991 / 441 / 92 | 0,53 / 0,24 / 0,05 | 1,12 / 0,50 / 0,10 |
| `该死的` | 88 | 0,05 | 0,10 |
| dòng bảng `【…】` | 51 | 0,03 | **0,06** |
| dòng exp `“叮！…经验加300。”` | 40 | 0,02 | 0,05 |

Hai kết luận ngược với trực giác:

- **Thẻ thoại là chuẩn của mẫu, không phải tật.** Mỗi chương ~3,7 thẻ `说道/问道/笑道`. SI 騎砍 v9 cũ **cấm**
  thẻ thoại — đó là lý do bản cũ đọc như biên bản, và là một phần của "mất cảm xúc".
- **Bảng hệ thống in ra rất ít**: 51 dòng `【】` trong 886 chương (0,06/chương), tập trung ở ch1–20. Sau đó
  truyện **kể** bảng bằng lời ("面板上的士兵数据…"), không in. Thể loại này không sống bằng spam bảng.

## 4. Tật của mẫu (để đặt ngưỡng, không phải để bắt chước)

| mẫu | số | /1000 字 |
|---|---|---|
| `实` gắn sau động từ | 309 | 0,14 |
| so sánh của người kể (`像/仿佛/好似/宛如/犹如`) | 991 | 0,46 |
| phủ định song song (`没有…没有…`, `不是…而是…`, `既…也…`) | 299 | 0,14 |
| nhãn ngữ điệu (`语气平淡`, `淡淡地说`) | 4 | ~0 |

Tức mẫu cũng có tật, ở mật độ thấp: **~1 so sánh/chương, ~0,3 cặp phủ định/chương**. Ngưỡng đúng cho bản mình
là **bằng cỡ mẫu**, không phải 0 (xem `references/si-test-tren-mau.md` mục 3).

## 5. Cỗ máy truyện (cái làm nên "sướng" của mẫu)

1. **Bàn tay vàng = một cuốn sổ**, không phải một giọng nói: `【宿主：罗伯森.奥多金（3阶青铜骑士489/500）（无爵位）】`,
   `【士兵：二阶.500法兰克民兵（495/500）】`. Bảng chỉ in sự thật tại thời điểm đó; **lời kể** dịch con số thành
   giá trị ("男爵也就3，4阶的水平").
2. **Cày là có, không bình cảnh**: mỗi chương một bước leo (一阶农奴 → 二阶民兵 → 三阶步兵; 骑士八技 494/500 →
   完美). Bước leo phải **trả giá bằng thứ đếm được** (mua lương bằng tiền mình, ngày đêm huấn luyện).
3. **Hai sổ song song**: sổ công khai (tước vị, lời nói đạo nghĩa với quý tộc) và sổ riêng (exp, mạng, đường
   rút). Khoảng cách giữa hai sổ là **nguồn hài chính** — anh ta nói một đằng, người kể nói hộ cái anh ta đang
   đếm. Đây là thứ bản test thiếu nhiều nhất.
4. **Người kể là người dẫn chuyện**, đứng về phía MC: nén một cuộc chiến trong ba dòng, hỏi người đọc một câu
   rồi tự trả lời, châm biếm quý tộc, rồi bước lại vào cảnh. Ngôi limited omniscient: được cắt vào đầu
   nhân vật khác 1–2 đoạn (博杨 háo hức, 奥德 hoảng) rồi về.
5. **Đơn vị truyện là "cấp bậc + đầu người + thóc"**, không phải cảm xúc. Căng thẳng đến từ chênh lệch số.

## 6. Hình chương

- Mở bằng **tiếng nói giữa chừng** (`“这么快？”`), không bằng cảnh vật; 2–3 dòng đầu đã có người đang lo.
- Thân: một cảnh + một khối giải thích/lý lẽ, số chen vào chỗ quyết định.
- Kết: **một kẻ địch to hơn, một con số lớn hơn, hoặc một người mang tin vào** — cắt giữa mạch.
- Chuyển cảnh bằng một dòng `.......` rồi vào cảnh mới; không có đoạn chuyển.

**Cảnh báo khi bắt chước:** ch1 của mẫu mở bằng 5 đoạn bảng + giảng thiết lập (法兰克 ở đâu, orc đánh mấy chục
năm) trước khi có người gặp nguy. Nó **vi phạm 黄金三章** của repo (300 字 đầu phải có người có tên đang gặp
nguy + hạn chót). Chương 1 của mình không chép cách mở này.

## 7. Vòng đời truyện (để đặt kỳ vọng dài)

ch1–20: biên giới, đánh 豺狼人, lên cấp, nhận 500 nông nô + kỵ binh + cung → ch20–50: tước vị, phong đất, mở
đường thương mại; ch50–120: vương đô, chính trị, báo chí, hôn nhân; ch120+: chiến tranh vương quốc, giáo đình.
Bảng hệ thống **mờ dần** sau ch20 và truyện chuyển sang 领主 tranh bá. Nghĩa là: SI phải viết được cả cảnh
bàn giấy (ai được gì, mất gì) chứ không chỉ cảnh chém.

## 8. Bản đồ anchor của SI v1 (chép nguyên văn, có script kiểm)

| mục | chương | dạy cái gì |
|---|---|---|
| 1. cỡ đoạn | ch13 英雄，骑士博杨 | 0,5 dòng → beat 3 chữ → hành động → cảnh, mỗi thứ một đoạn |
| 2. so sánh thuộc nhân vật | ch17 订婚 | MC so trang viên hầu tước với 故宫 kiếp trước; đổi cách gọi = đổi thông điệp |
| 3. người kể về phía MC | ch19 高尚的罗伯森老爷 | quý tộc cảm động vì lời đạo nghĩa, dòng sau lộ sổ riêng (开玩笑，那能让你们抢了经验吗) |
| 4. cú bật | ch13 | 博杨 nghiêm túc hóa lệnh, bị chốt bằng một câu về giấc ngủ |
| 5. thoại có thẻ | ch14 罗伯森老爷的新兵们 | 4 lượt mỗi người, thẻ đủ, lời châm bằng dữ kiện, snark chen giữa hai lượt |
| 6. chuỗi giải thích | ch1 军官罗伯森佬爷 | 一阶农奴 → 二阶民兵 → 三阶步兵, kèm tiền lương và ngày công |
| 7. chuyển cảnh | ch17 | `.......` → hai chữ địa danh → cảnh mới đang chạy |

Không anchor nào lấy từ ch8 — chương dùng làm **bài test** (đáp án đã biết).
