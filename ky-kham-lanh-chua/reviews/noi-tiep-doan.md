# Sửa mối nối giữa các đoạn (26/10)

Tác giả: *"đoạn sau không hề được nối tiếp với đoạn trước"*. Đúng, và đo được: cả **5/5** mối nối của chuỗi
003–007 đều đứt, vì prompt của mỗi đoạn chỉ tả một cảnh tự thân — không câu nào nói đoạn này phải mở bằng việc
trả lời chỗ dừng của đoạn trước.

## Trước khi sửa (chuỗi 003-E … 007-A)

| mối | câu cuối đoạn trước | câu đầu đoạn sau |
|---|---|---|
| 002 → 003 | `比他们预计的时间整整提前了二十天！` | tả gió đêm qua khẩu 60 步 — không ai nói gì về "sớm hai mươi ngày" |
| 003 → 004 | `刚冲到半山腰…身后就传来了 Karl 扯着嗓子大喊的声音` | tả rừng thông; Adrian xuất hiện sau đó, tiếng gọi không được trả lời |
| 004 → 005 | `Karl 抓着他的腕甲` (Karl sắp nói) | `午后的日头斜照…` — bàn tay đó biến mất, 巴特 đã bị trói từ lúc nào không ai biết |
| 005 → 006 | bảng 【人数上限：500】 | `粗麻绳割断了巴特的声息` — mối duy nhất liền |
| 006 → 007 | bảng 【人数上限：600】 | tả gió đêm; cuộc hỏi đáp về 4阶 không có câu trả lời |

Nguyên nhân ở tầng brief, không phải SI: mỗi prompt là một danh sách "cần đúng những việc này" của **một cảnh**,
và Writer viết đúng như vậy — một cảnh tự thân.

## Cách sửa

Thêm **KHỐI NỐI TIẾP** vào đầu mọi prompt (đã ghi thành luật 0 trong `briefs/_mau-prompt-ngan.md`): mô tả chỗ
dừng của đoạn trước bằng tiếng Việt, đòi 200–300 字 đầu trả lời đúng chỗ đó, kèm danh sách việc đang treo.

Chạy lại 5 đoạn. Lần chạy đầu **tiếp session cũ** hỏng thêm một kiểu: bản mới trùng **77% nguyên văn** với bản
cũ (Writer đọc lại bản trước trong context rồi viết tiếp) → phải `--new` cho từng đoạn, mối nối do brief mang,
không do context.

## Sau khi sửa (chuỗi 003-G … 007-B) — cả 5 mối đều liền

| mối | câu cuối | câu đầu / hai câu đầu của đoạn sau |
|---|---|---|
| 002 → 003 | `…提早了二十天！` | `把火熄了。` + Karl đáp `连个像样的铜号角都没有` — trả lời đúng cái phát hiện đêm đó |
| 003 → 004 | `…距离前方的松树林只剩下一半的路程` | Karl đuổi kịp báo `后门留了三个老汉…林子里四十一个人` |
| 004 → 005 | `一把攥住了他的手腕` | `Karl 握着他的手腕…` rồi `先把死人弄回去` |
| 005 → 006 | `巴特的声音在半空中戛然而止——` | `麻绳拉得笔直…两只脚在半空中蹬了两下` |
| 006 → 007 | `把他们的名字记在羊皮纸上，回领地后发抚恤` | Karl: `今晚地皮冻得跟生铁一样硬，挖十一口深坑得砸烂三把铁锹` |

Số liệu vẫn khớp toàn chuỗi: 497→493→488→477 · lương 3.400→2.400→1.400→400→0 · 132 = 120 rào + 12 chông ·
481+18=499, +9=508 → 4阶（8/2000）· 士兵 63+117=180 → 41 二阶（80/100）, 436 一阶 · 上限 600 · 士气
22→41→29→52. Bảy dòng bảng đúng nguyên văn.

## Cái giá của cách sửa này (đo được)

| | chuỗi cũ (đứt nối) | chuỗi mới (liền nối) |
|---|---|---|
| 字 | 1.533–1.978 | 1.723–2.488 |
| lượt thoại | 3–15 | 6–32 |
| chữ/lượt | 26,0–35,7 | **12,2–22,7** |
| lượt cụt | 0–2 | 1–7 |
| cham_doan | 58–82 | 42–76 |

Vì khối nối tiếp của bản này viết *"Karl nói gì"* — đúng cái luật 2 cấm. Kết quả: nối liền nhưng thoại mỏng và
ngắn hơn, 003-G bị 5 phủ định lặp. Luật 0 đã ghi lại: **viết "ai làm gì", không viết "ai nói gì"** — nếu Tác
giả muốn cả hai (nối liền + thoại dày) thì chạy lại 5 đoạn với khối nối tiếp đã sửa, dự kiến 2 phút/đoạn.

## Trạng thái file

`chapters/` giờ chỉ còn chuỗi đang dùng: `doan-001-h` → `doan-007-b`. Các bản cũ (001-g, 003-e, 004-d, 005-a,
006-a, 007-a) nằm trong `chapters/archive/`, kèm `doan-003-f-lap-77.md` (bản lặp 77% — giữ làm bằng chứng cho
luật "đừng chạy tiếp session khi viết lại cùng một đoạn").
