# Giọng chữ — thổ ngữ, chữ cổ, cụm sáo (09/11)

## Mới nhất: SI-R2

Tác giả gửi ảnh DocTTS: "thật sự" = **实打实** (有实打实的劲道 · 气血实打实充盈些), "đắc nhận" = **得很** (语气平稳得很).
Bản đó là R-003-a, tức SI-R vẫn còn tật. Bộ mẫu cũng dùng 得很, nhưng chỉ trong lời nhân vật (眼馋得很 · 肉疼得很); Writer
gắn nó vào lời kể tả giọng.

- **Danh sách 40 tật**, lấy từ số liệu (cụm Writer dùng gấp ≥8 lần bộ mẫu, lặp ở ≥8/25 bản):
  [`../tat-giong-ai.txt`](../tat-giong-ai.txt). Đếm bằng `tools/tat_ai.py`.
- **SI-R2** = SI-R, thêm:
  - dòng cụm sáo nới thêm 实打实 · 紧实 · 沉甸甸 · 清清楚楚 · 干瘪 · 喉结滚动 · 冷不丁, và câu "để con số mang sức nặng";
  - dòng nhãn lạnh thêm 神色平静 · 语气平稳得很;
  - FIXED 1: viết 外边 · 后面 · 下面 · 昨天, như bộ mẫu.

  Phần dán 8.293 ký tự. File [`giong-v2/si-R2.txt`](giong-v2/si-R2.txt).

| Tổng tật /1.000 字 | Bộ mẫu | SI đang dùng | SI-R | **SI-R2** |
|---|---|---|---|---|
| đoạn 001 | 0,44 | 6,60 · 6,76 | — | **1,12 · 0,89** |
| đoạn 003 | 0,44 | 16,23 · 15,24 | 11,28 · 9,50 · 5,70 · 9,41 | **2,25 · 7,43** |

I-0071 hiệu quả. Bản 7,43 (R2-003-b) còn 猛地 ×4 · 硬生生 ×3 · 后头 ×3 · 白纸黑字 ×2. Hai lần chạy cùng SI vẫn lệch 3 lần,
nên đề xuất thêm **cổng đếm**: sau mỗi lần chạy, đếm bằng `tat_ai.py`; bản nào cao hơn ~3 /1.000 thì chạy lại chat mới,
không sửa tay. Quét lại 4 bản SI-R2 không thấy Writer đổi sang chữ thay thế mới.

Bản đầy đủ: [`giong-v2/`](giong-v2/) — `R2-003-a/b`, `R2-001-a/b`.

---

Phần dưới là lượt trước (SI-R).

Tác giả: "thỉnh thoảng xuất hiện tiếng bản địa, chữ cổ. Văn mẫu viết bằng bạch thoại văn… 'thẳng hướng trong lỗ mũi
chui' được dùng quá nhiều, hầu như bản nào cũng có." Thoại: "hơi ổn rồi, để về sau test thêm."

## 1. Đếm được gì

Đếm trên 21 bản Writer của truyện, so với 182 chương bộ mẫu. Số là lần trên 1.000 字.

| Nhóm | Chữ | Bộ mẫu | Writer |
|---|---|---|---|
| thổ ngữ phương Bắc / chữ cổ | 俺 · 瞅 · 后生 · 老汉 · 老夫 · 老子 · 做甚 | ≈ 0 | 老夫 0,27 · 老子 0,28 · 瞅 0,22 · 俺 0,19 · 后生 0,15 |
| chữ chỉ chỗ | 外头 · 后头 · 底下 | 0 · 0 · 0,02 (mẫu viết 外边 · 后面 · 下面) | 0,28 · 0,40 · 1,27 |
| cường điệu | 猛地 · 死死 · 狠狠 · 硬生生 · 整整 · 结结实实 · 紧实 | 0,12 · 0,03 · 0,02 · 0,03 · 0,02 · 0 · 0 | 1,37 (21/21 bản) · 0,84 (19/21) · 0,37 · 0,23 · 0,63 · 0,14 · 0,29 |
| cụm cận cảnh sáo | 浑浊的眼 · 嘴唇哆嗦 · 颤巍巍 · 眼珠子 · 直往鼻孔里钻 | ≈ 0 | 浑浊的眼 có ở 16/21 bản, 嘴唇哆嗦 12/21 |

**Nguồn:**

- **SI**: câu mở viết "light, **earthy** famine-year **village** serial", BAN 2 viết "plain **village** Chinese". Hai chữ
  này mời Writer viết giọng thổ ngữ.
- **Gói bàn giao**: dán kèm ~2.500 ký tự đuôi đoạn trước, mà đó là văn Writer chưa duyệt. Riêng đuôi trong gói 003 đã có
  浑浊 ×4 · 猛地 ×3 · 后生 ×2 · 死死 ×2 · 外头 · 后头 · 底下. Thêm State JSON (老夫, 后生).

## 2. Đã thử: SI-R, hai nhánh, mỗi nhánh hai chat, cùng gói đầu vào đoạn 003

SI-R sửa ba chỗ so với SI đang dùng, không thêm dòng mới:

1. Câu mở bỏ "earthy … village".
2. FIXED 1: văn là 白话 hiện đại như anchor; chỉ tên, chức, đơn vị là cổ; không ai nói tiếng địa phương hay câu văn cổ.
3. BAN 4 (cấm tiếng động đứng thành dòng — dòng này đang bị vi phạm ở 10/21 bản) thay bằng: nói một lần, bằng chữ thường;
   không cụm cận cảnh hay chữ cường điệu lặp từ cảnh này sang cảnh khác, nêu đích danh các chữ ở bảng trên.

Nhánh **R** giữ nguyên gói. Nhánh **RP** cắt đuôi gói còn ~300 字.

| /1.000 字 (đoạn 003) | SI đang dùng (2 bản) | SI-R (4 bản) | Sổ |
|---|---|---|---|
| cường điệu | 5,15 · 5,85 | 3,49 · 0,79 · 0,71 · 2,90 | I-0068 **hiệu quả** |
| cụm cận cảnh sáo | 1,39 · 1,46 | 0,81 · 0,53 · 0,47 · 0 | |
| thổ ngữ rõ (老夫, 俺, 后生, 作甚…) | 2,38 · 1,25 | 0,81 · 0 · 0,47 · 0,72 | I-0069 chưa rõ |
| chữ chỉ chỗ (外头 · 后头 · 底下) | 2,97 · 1,67 | 1,88 · 2,64 · 2,14 · 1,21 | không đổi |

Cắt đuôi gói (RP) không thêm tác dụng gì về giọng (I-0070 vô hiệu). Thoại giữ ngang SI cũ (20–30 % số đoạn có thoại).

Lời lý chính, cùng cảnh:

- SI đang dùng: «老夫手里可没有多余的糠皮借你…别在老夫院里嚎丧！» · «你他娘的吃了熊心豹子胆！»
- SI-R: «“自家地里？”罗里正眉毛拧了起来，“你家东沟那三亩干豆地，能长出这号东西？”» · «送这么大一份礼，总不至于是为了听老头子夸你两句。»

Còn sót: 后头 có ở cả 4 bản; 整整 còn 1 lần mỗi bản (trước 3–4); 老夫 / 后生 / 瞅 / 做甚 thỉnh thoảng còn.

Bản đầy đủ: [`giong-v1/`](giong-v1/) — `R-003-a/b`, `RP-003-a/b`; SI `si-R.txt`.

## 3. Cần Tác giả quyết

1. Dùng **SI-R2** làm SI đang chạy không? (Đổi SI phải có Tác giả duyệt, AGENT.md mục 8.) Phần dán 7.895 → 8.293 ký
   tự, hơi vượt ngân sách 8.000 nhưng dưới trần 9.000.
2. Có dùng cổng đếm `tat_ai.py` (bản cao thì chạy lại) cho mọi đoạn từ giờ không?
3. ~~"Thật sự / đắc nhận" là chữ nào?~~ Đã rõ qua ảnh: 实打实 · 得很.
