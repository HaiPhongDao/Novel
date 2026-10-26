# Mẫu prompt cho truyện này (rút từ `gemini/test/Without prompt` của Tác giả)

## Vì sao đổi

Writer viết **không có prompt** (chỉ SI) ra thoại dày và mượt: 3.618 字, **42 lượt thoại**, MC 11 lượt, trong
đó `老子` 5 lần, `开玩笑…` 1 lần, và một cuộc nói chuyện với 卡尔 về quê cũ / đứa cháu mà không phục vụ sổ sách.

Ba prompt mình tự viết cho cùng đoạn 002 (cùng SI v7):

| prompt | lượt thoại | MC | điều mất đi |
|---|---|---|---|
| 6 beat đánh số + chỉ định nội dung từng lượt + dòng tỷ lệ thoại | 14 | 6 lượt, trung vị 25,7 字 | không có `老子`, không có câu đùa, 代守 từ chối theo kịch bản |
| ngắn, 4 đoạn văn + danh sách số | 8 | 5 lượt | vẫn ít lượt, nhưng MC tự chọn cách nhịn (thú vị hơn) |

⇒ Giọng không hỏng vì SI. Nó hỏng vì **prompt chỉ định nội dung từng lượt**: khi mình viết "hỏi một câu thật,
ví dụ ai ký lệnh", Writer chỉ còn việc đánh dấu vào checklist. Và số lượt thoại không do chỉ dẫn thoại quyết
định, mà do **phạm vi thời gian của đoạn** và **số người có mặt trong cảnh**.

## Mẫu

```
KHỐI NỐI TIẾP — đoạn trước dừng ở chỗ: <mô tả đúng sự việc cuối đoạn trước, ai đang ở đâu, ai vừa nói gì>.
200–300 字 đầu của đoạn này phải trả lời đúng chỗ đó (<việc phải xảy ra tiếp>), rồi mới chuyển cảnh.
Đang treo từ các đoạn trước: <những thứ chưa xử: người bị trói, xác chưa chôn, người bị thương, lời hứa, món nợ>.

Đoạn thứ N. <mốc thời gian: một đêm, một ngày, hai ngày> ở <địa điểm>.

Cần đúng những việc này: <3–5 sự việc, viết như sự thật đã xảy ra, không đánh số, không chia beat>.

<Sự thật ràng buộc về quyền lực / thân phận / cái giá — 1–2 câu, chỉ khi nó đổi cách nhân vật hành xử.>

Dừng ở chỗ <một việc đang xảy ra>.

Số: <danh sách số, có đơn vị và tỷ giá>.

Bảng: <các dòng 【】 đúng nguyên văn>.
```

## Luật

0. **Khối nối tiếp là bắt buộc, đứng đầu prompt.** Đo được trên 5 đoạn 003–007: prompt không có khối này thì
   đoạn sau mở bằng một cảnh mới toanh và **cả 5 mối nối đều đứt** — 003 hết ở giữa đường chạy vào rừng, 004 mở
   bằng tả rừng; 004 hết ở bàn tay Karl nắm cổ tay hắn, 005 mở bằng "buổi chiều" với 巴特 đã bị trói từ lúc nào
   không ai biết. Viết đúng chỗ dừng của đoạn trước **bằng tiếng Việt** (đừng trích câu tiếng Trung — Writer chép
   nguyên), kèm danh sách việc đang treo.
   **Viết "ai làm gì", không viết "ai nói gì".** Lượt đầu tiên của bản sửa có ghi "Karl nói gì" và cái giá đo
   được: 5/5 mối nối liền, nhưng thoại phình từ 3–15 lên 6–32 lượt và **chữ/lượt tụt từ 26–36 xuống 12–23**
   (006: 13 lượt · 12,2 字), kèm 1–7 lượt cụt mỗi đoạn — tức lại là Agent viết hộ thoại, chỉ khác chỗ đặt. Chỉ
   cần: "cảnh mở bằng một việc cụ thể xảy ra ngay sau chỗ dừng đó", và ai nói thì để Writer chọn.
1. **Không đánh số beat.** Số thứ tự biến mỗi beat thành một hành động và cả đoạn thành biên bản.
2. **Không chỉ định nội dung lượt thoại** ("hỏi một câu thật", "một lượt ngoài việc", "phải từ chối một lần").
   Đó là Agent viết hộ thoại; Writer sẽ thi hành đúng chữ và mất giọng.
3. **Không ghi tỷ lệ thoại/lời kể** trừ khi cảnh đã bị viết thành cuộc họp (đo được >30 lượt). Nó là van chữa
   bệnh, không phải mặc định.
4. **Mở rộng phạm vi thay vì thêm beat.** Muốn nhiều giọng thì cho đoạn trùm một ngày (đêm luyện → sáng chặt
   cây → chiều địch mò tới), và đưa thêm người có mặt: lính gác, đầu đàn nông nô, người báo tin, lính trên
   tường chê bai.
5. **Số và bảng là phần duy nhất được viết chi tiết** — chúng giữ độ khó, và Writer chép nguyên văn.
6. **Không nhắc lại luật văn phong trong prompt.** Luật nằm ở SI. Prompt mà dặn cách viết là đang đo prompt,
   không đo SI.

## Bản dài bao nhiêu?

Không đặt. Đoạn dài theo số sự việc. Ba đoạn đã chạy: 1.958 / 1.722 / 1.351 字 — đều ngắn hơn bản Writer tự
do (3.618 字), vì phạm vi mình giao hẹp hơn một chương.

## Chỗ đặt cho cái đầu kiếp trước (bắt buộc, một dòng mỗi brief)

Prompt phải chỉ ra **một việc** trong đoạn mà cách người bản địa làm sẽ hỏng, để hắn xử bằng một đơn vị/định mức
mang từ kiếp trước (suất ăn, ngày công, tỷ lệ hao, thời gian ủ, ca trực). Ghi như sự thật, không ghi "hãy thể hiện
sự ưu việt". Ba lần chạy đo được: không có dòng này thì 0/5 đoạn có dấu vết; có dòng này ở 003 thì hắn quy được
`热量消耗是静卧者的三倍` và mở cơ chế thay ca.

**Không mô tả tính cách MC** — không trong brief, không trong bible, không trong SI. Tác giả chốt 26/10: *"Đừng gán
tính cách vào MC, AI viết dở cái đấy. Tự writer quyết."* Tính cách phải lộ ra qua việc hắn làm và câu hắn nói
trong cảnh; Agent chỉ đưa **hoàn cảnh** (quyền, hạn chót, cái giá, người đối diện), không đưa nhãn tính cách.
