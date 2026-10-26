# Xưng hô và đẳng cấp trong truyện Tây huyễn

Dùng khi mở truyện phong kiến/Tây huyễn (lãnh chúa, quý tộc, kỵ sĩ, giáo hội) hoặc khi review thấy thoại "không đứng đúng vị trí": người hầu nói với chủ mà không có kính ngữ, hoặc chỉ đổi từ gọi mà không đổi tư thế.

## 1. Chuẩn lấy từ truyện đã duyệt, không từ cảm giác

Đếm trong bản đã chốt của chính repo (`lanh-chua-chip/chapters/`, Tây huyễn, đã duyệt qua 15 đoạn):

| 少爷 | 领主大人 | 大人 | 小人 | 老爷 | 老奴 |
|---|---|---|---|---|---|
| 58 | 29 | 26 | 24 | 6 | **0** |

Suy ra register của repo: chủ là **大人 / 老爷 / 领主大人**; người hầu tự xưng **小的 / 小人**; dạng Trung Hoa đế quốc (老奴, 奴才, 属下, 末将) không thuộc bối cảnh này.

```bash
grep -oh "领主大人\|少爷\|大人\|小人\|老奴\|老爷\|爵士\|会长" <truyen>/chapters/*.md | sort | uniq -c | sort -rn
```

Chạy lệnh này trước khi viết bảng xưng hô cho truyện mới — nó cho cả tần số lẫn register đã được Tác giả chấp nhận.

## 2. Bảng đưa vào `bible/glossary.md` trước đoạn 001

| Vai | Được gọi | Tự xưng | Tư thế |
|---|---|---|---|
| Nam tước / lãnh chúa | 大人 (mặc định) · 老爷 (người nhà lâu năm) · 领主大人 (dân, người ngoài) | 我 | Ngồi trước; nói câu ngắn; không giải thích việc mình làm cho người hầu |
| Quản gia, người hầu | — | 小的 (quản gia lâu năm) · 小人 (kẻ thấp, xu nịnh) · có khi bỏ tự xưng | Đứng khi chủ ngồi; 垂手侍立 (hai tay buông hoặc khoanh trước bụng, thân hơi khom); dâng bằng hai tay, 奉过头顶; nói xong lùi nửa bước; mở mọi báo cáo bằng 回大人; không gọi tên chủ |
| Kỵ sĩ / hiệp sĩ | 爵士 (khi xưng chức danh) | 我 | Tay đặt chuôi kiếm khi thề; gọi chủ là 大人 |
| Tu sĩ | 神父 · 修士 | 我 | Gọi chủ là 大人; không cúi mình trước quý tộc như người hầu |
| Trưởng phòng hội | 会长 | 我 | Gọi chủ là 大人, hoặc 阁下 khi thế tiền ngang nhau |
| Trưởng thôn, già làng | 老丈 | 老朽 / 我 | Gọi chủ là 领主大人; cúi người, không quỳ |
| Người ngoài, khách | 先生 / 夫人 | 我 | — |

Giới hạn tước vị: 陛下 chỉ cho vua, 殿下 chỉ cho vương tử/công chúa. Một nam tước chỉ có 大人 / 老爷 / 领主大人.

## 3. Đẳng cấp không chỉ là từ gọi

Nếu chỉ sửa từ gọi, hai người vẫn đọc lên như ngang hàng. Tư thế là phần nửa còn lại:

- Người hầu **đứng** khi chủ ngồi; không ngồi trừ khi được bảo; không quay lưng.
- Dâng vật bằng hai tay; nhận lại rồi lùi về chỗ cũ, chắp tay đứng hầu.
- Mở báo cáo bằng 回大人 rồi mới tới nội dung — đây là dấu hiệu rẻ nhất và rõ nhất của đẳng cấp.
- Chủ nói câu ngắn, ra lệnh, không thanh minh; không đứng dậy đón người hầu.
- Nhà phục vụ hai đời giữ khoảng cách mấy ngày đầu và chỉ rút ngắn khi chủ rút ngắn — người hầu mới về không được gọi 少爷.

## 4. Lỗi thường gặp

- **老奴 / 奴才 / 属下**: dạng Trung Hoa đế quốc, ra khỏi register trang viên Tây. Đây là lỗi số một.
- **少爷** dùng cho quản gia vừa nhận chủ: 少爷 chỉ dành cho người nuôi chủ từ nhỏ.
- **陛下 / 殿下** cho nam tước, hoặc 大人 cho vua.
- **Tự xưng lẫn** trong cùng một cảnh (小的 / 老仆 / 我) — chốt một dạng rồi giữ.
- **Nhãn ngữ điệu thay kính ngữ**: "语气恭敬" không thay được 回大人 và tư thế; nó còn là nhãn ngữ điệu (đếm bằng `nhan-ngu-dieu`).
- **Chủ tự giải thích** việc mình làm cho người hầu, hoặc xin lỗi người hầu — mất đẳng cấp ngay ở câu đầu.

## 5. Đưa vào ba tầng

- `bible/glossary.md`: bảng ở mục 2 + giới hạn tước vị. Đây là nguồn sự thật.
- SI: một đoạn trong nguyên tắc "hai người gặp nhau" (đẳng cấp nằm trong từ họ chọn cho nhau, tư thế, ai ngồi ai đứng, 回大人, chủ nói câu ngắn) + danh sách chức danh 爵士 / 神父 / 会长 / 老丈.
- `briefs/doan-XXX.md`: chép thẳng cách gọi của đoạn này ("Osric gọi anh là 大人, tự xưng 小的, mở báo cáo bằng 回大人, đứng khi anh ngồi"), vì Writer không đọc glossary. Không đưa câu cấm dạng 老奴 vào SI — câu cấm nằm ở `chung/review-blacklist.md`.

## 6. Đo trước/sau

Đếm bằng grep các từ khoá, đưa vào review như một dòng số:

| | trước | sau |
|---|---|---|
| 老奴 | 3 | 0 |
| 回大人 | 0 | 8 |
| 垂手侍立 | 0 | 3 |
| thẻ thoại / lượt | 6/31 | 5/23 |
| lượt cụt (≤6 chữ) | 5 | 1 |

Mục tiêu thực dụng: 老奴 = 0; 少爷 = 0 nếu người hầu không nuôi chủ; 回大人 ≥ số lần báo cáo; 垂手/躬身 ≥ 1–2 lần mỗi cảnh có người hầu.

## 7. Bẫy khi chấm

Đừng cộng điểm register bằng số từ rồi kết luận. Phải đọc: có ai đứng dậy không, có ai chờ được phép nói không, có câu nào chủ phải giải thích không. Số từ chỉ để biết có luật hay không; tư thế phải nhìn trên trang.

## 8. Tên riêng và chức tước trong chính văn

Quy ước chốt (Tác giả): **chỉ tên người viết chữ Latin; chức tước, địa danh, gia tộc viết chữ Hán.**

| loại | viết | ghi chú |
|---|---|---|
| tên người | `Adrian 抬起手` · `Karl 点了点头` · `Gerry 翻开账册` · `Cole 跪在泥里` | luôn Latin, giống nhau mọi lần |
| người đã có tên Hán | 洛伦 | giữ nguyên |
| chức tước | 男爵 · 少爷 · 管事 · 爵士 · 长官 | **không** đặt chức bằng tiếng Anh |
| quý tộc gọi theo họ + tước | 洛萨男爵 | `Baron Losa` sai: baron = nam tước (男爵), `伯爵` mới là count |
| địa danh | 铁脊要塞 (Iron Ridge) · 维兰 (Vilan) · 巴罗尔 (Barol) | |
| gia tộc / trang viên | 洛萨家族 · 洛萨庄园 (House Losa) | |
| đơn vị in bảng | `【士兵：一阶.500 维兰农奴（0/100）】` | tên người Latin, đơn vị theo địa danh Hán |
| kẻ địch | 兽人王庭 · 豺狼人 | chữ Hán |

Vì sao: tước để tiếng Anh thì bị đọc sai bậc (baron → bá tước), và cụm tiếng Anh chèn giữa câu Hán làm câu văn gãy. Kiểm sau khi chạy:

```bash
grep -c 'Iron Ridge\|Vilan\|Barol\|House Losa\|Baron' <truyen>/chapters/doan-*.md   # phải 0
grep -o '少爷\|大人\|老爷\|小的\|小人' <truyen>/chapters/doan-*.md | sort | uniq -c
```

Ba tầng phải sửa cùng lúc: FIXED CONVENTIONS 2 của SI (kèm ví dụ + câu "a noble is named by title plus family"), bảng quy ước trong `bible/glossary.md`, và dòng tên riêng trong **mọi** brief (brief cũ giữ quy ước cũ sẽ kéo bản mới lệch lại).
