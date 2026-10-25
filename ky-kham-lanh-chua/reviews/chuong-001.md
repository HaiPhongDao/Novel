# Chương 1 — review bản A (máy) + bản B (sửa tay)

- Brief: `briefs/chuong-001.md` · SI: `gemini/si-dan-gemini.txt` v2 · chạy `--new`, 125s
- Bản A (nguyên): `chapters/chuong-001-a.md` — 2.786 字
- Bản B (13 chỗ sửa tay + cắt 139 字): `chapters/chuong-001-b.md` — 2.647 字
- Thinking: `archive/thinking-001a.md`

## 1. Bảng số

| chỉ số | mẫu (886 ch) | mẫu ch1 | A | B |
|---|---|---|---|---|
| 字 | 2.122 (trung vị) | 2.273 | 2.786 | **2.647** |
| chữ / câu | 23,9 | 28,4 | 20,0 | **21,3** |
| lượt thoại | 20 | 14 | 47 | 47 |
| chữ / lượt | 22,4 | 29,6 | 20,2 | 19,9 |
| phủ định lặp | 0,3/ch | 0 | 1 | **0** |
| so sánh người kể | ~1/ch | 0 | **3** | **0** |
| nhãn ngữ điệu | ~0 | 0 | **3** | **0** |
| `实` | 0,3/ch | 0 | 0 | 0 |
| tự gọi 少爷 | 1,35/ch | 0 | 1 | 1 |
| dòng bảng `【】` | 0,06/ch | 6 | 2 khối (8 dòng) | 2 khối (8 dòng) |

## 2. Sáu chỗ phải sửa tay ở bản A (và đã sửa ở bản B)

| loại | bản A | bản B |
|---|---|---|
| so sánh người kể | `所有人都在冷风里瑟瑟发抖，像一窝挤在烂泥里的受惊鹌鹑` | cắt vế so sánh, giữ `呼出的白气聚成一片薄雾` |
| so sánh người kể | `身子晃荡得像风里的枯草` | `站都站不直` |
| so sánh người kể | `仿佛屋子里只是飞进了一只无关紧要的麻雀` | `一根手指压在铁脊隘口的位置上` |
| so sánh người kể | `卡尔的声音冷得像结了冰渣` | `卡尔报完，抬起眼看过来` |
| nhãn ngữ điệu | `阿德里安平静地说道` (×1), `语气没有半点起伏` (×1), `冷冷地开口…声音像深冬磨石般干涩` (×1) | bỏ nhãn, giữ động tác (`手里的银刀没有放下`) |
| phủ định lặp | câu mặc cả `语气没有半点起伏，“行就放人，不行…` | bỏ vế `没有半点起伏` |

Ba chỗ nữa **`soat_van.py` không bắt** (đã grep tay, ghi thành KN30): `目光如鹰隼般锐利` → bỏ vế so sánh;
`四指粗糙如铁钩` → `指节粗大`; `阿德里安平静地命令道` → `命令道`. Tổng cộng 13 chỗ.

Nhận xét: **hai tật này sống sót qua hai lần chạy liên tiếp** (test 01 sạch, ch1 bẩn) — tức chúng là
biến thiên của lần chạy chứ không phải lỗi SI. Sửa tay 10 chỗ rẻ hơn một vòng SI mới.

## 3. Đọc bằng lời (bản B)

**Mở** — `木桩被铁锤重重砸进冻土里` → `阿德里安睁开了眼`
- Vào bằng tiếng, rồi tới thân thể (`右臂缠着的粗麻布渗出两点暗红`), rồi mới tới nhà và sân — đúng nhịp mở
  chậm Tác giả đã yêu cầu, khác hẳn bản test 01 (mở bằng lời báo tin).
- Ai gặp nguy trong 300 字 đầu: 科尔, thòng lọng đã quàng, và chính MC (bị tống đi).
- Hạn chót: mặt trời mọc (treo 12 người), trưa (rời trang viên), 30 ngày (địch tới).

**Giữa** — cuộc mặc cả với 格里
- Có chất liệu xã hội ngoài việc: đám cưới của anh trai, lời mời uống rượu, người nông nô đang sốt — đúng thứ
  Author đòi ở cảnh hai người gặp nhau.
- Cái giá rõ: 30 金币 → 24 → còn 6. `24` và `6` được nói ra thành câu riêng, không nằm lẫn trong đoạn.
- Điểm yếu: 格里 giải thích luật hai lần (潜逃 + 双倍罚金); bản B đã nén một lần.

**Kết** — `拿这六枚金币去镇上的铁匠铺，全买伐木用的重刃铁斧。`
- Kết bằng quyết định + số (24 rìu, hoặc 0,72 ngày ăn), có người hỏi lại (`不买粮？`) — đúng kiểu hook.
- Chưa đủ mạnh: câu cuối là lý lẽ của MC, không phải một cái giá mới hay một kẻ địch mới. Cân nhắc cho ch2
  mở bằng tin 铁脊要塞 đã có người bỏ đi, hoặc bằng chính 24 cái rìu được rèn xong.

**Giọng:** có `他阿德里安少爷在家族账本上的价值，到此算是彻底结清了。` (tự gọi 少爷, 1 lần), có
`天崩开局也不过如此。` (câu trần trong đầu, không ngoặc) — hai thứ bản test 01 thiếu hoàn toàn.

## 4. Ba việc phải chốt trước chương 2

1. **Độ dài**: hai lần chạy liền ra +27% và +21% so với trần SI (2.200). Luật trong SI không kéo được con số
   này ⇒ **ghi số 字 vào brief** ("khoảng 2.100 字, không quá 2.300") mới là chỗ sửa.
2. **Lượt thoại 47** (mẫu 20) vì chương có ba cảnh thoại liền. Brief đã ghi dòng tỷ lệ nhưng Writer vẫn chẻ
   lời; lần sau ghi thẳng "ba cảnh, cảnh giữa phần lớn là lời kể" hoặc gộp cảnh cha vào cảnh sân.
3. **Canon mới do Writer tự đặt, cần chốt**: 科尔 là "瘦弱老头" (bible ghi 28 tuổi) → chốt **50 tuổi**; tốc độ
   exp "挥剑两万次 ≈ 19 点" → chốt tỷ giá (đề xuất **1 点 ≈ 400 次挥剑**, tức 19 点 ≈ 7.600 次, không phải
   2 万); 卡尔 tự xưng 老仆 của mẹ → thêm vào bible.

## 5. Verdict

**CẦN TÁC GIẢ ĐỌC.** Bản B sạch tật đo được, đúng nhịp mở, có cái giá và có hook quyết định; chưa duyệt thì
chưa viết chương 2. Ba con số còn lệch mẫu: 字 +21%, lượt thoại gấp đôi, câu 21,3 so với 23,9.
