# Test so sánh: 3 cách giao việc cho Writer Gemini

**Cách làm:** Gemini giữ nguyên system instruction riêng của Tác giả (文风 · 写手系统指令). Mở **3 cuộc trò chuyện mới, tách biệt**, mỗi cuộc dán đúng một prompt bên dưới. Lưu kết quả vào:

- `chapters/test-A.md` — prompt một dòng
- `chapters/test-B.md` — prompt đơn giản
- `chapters/test-C.md` — prompt chi tiết

Sau đó gửi Agent để chấm theo bảng ở cuối file.

> Nếu muốn Gemini viết bằng tiếng Trung, xoá chữ "bằng tiếng Việt" trong mỗi prompt (giữ giống nhau ở cả ba để so sánh công bằng).

---

## Prompt A — Một dòng

```
Viết đoạn mở đầu cho truyện mới khoảng 2000 chữ, bằng tiếng Việt.
```

---

## Prompt B — Đơn giản

```
Viết chương 1 (khoảng 2000 chữ, bằng tiếng Việt) cho truyện mới.

Trần Minh Khang, kỹ sư nông nghiệp người Việt, gặp sự cố khi thử nghiệm một con chip cấy não và tỉnh dậy trong thân xác Leon Varen – cậu con thứ ba 18 tuổi của một bá tước, vừa bị đày tới lãnh địa biên giới nghèo xơ xác tên Hắc Thạch. Con chip đi theo anh (anh gọi nó là "Bảy"), nhưng hỏng 61% dữ liệu. Bảy chỉ có kho kiến thức và khả năng phân tích những gì anh nhìn, nghe, ngửi, nếm – không phải hệ thống game, không điểm, không nhiệm vụ, không cửa hàng.

Chương 1: anh tỉnh dậy trong trang viên đổ nát, chip khởi động, gặp hiệp sĩ già Gareth – người duy nhất trung thành với Leon. Cuối chương, nhờ Bảy, anh phát hiện thân xác này không chết vì bệnh mà bị đầu độc. Kết chương ở phát hiện đó.
```

---

## Prompt C — Chi tiết (細纲 chương 1)

```
Viết chương 1 cho truyện mới, khoảng 2000 chữ, bằng tiếng Việt. Chỉ viết các nhịp trong 细纲 dưới đây, theo đúng thứ tự.

# Nền truyện
Trần Minh Khang, 29 tuổi, kỹ sư nông nghiệp chuyển sang làm cảm biến tưới tiêu ở công ty Viễn Tâm Lab (Việt Nam hiện đại). Anh nhận cấy chip giao diện não nguyên mẫu K-07 vì tiền thưởng trả nợ cho mẹ. Buổi thử nghiệm bị quá tải điện. Anh tỉnh dậy ở vương quốc Aldermark (trung cổ phương Tây, phép thuật cực hiếm), trong thân xác Leon Varen, 18 tuổi, con thứ ba của Bá tước Varen, mẹ là vợ lẽ đã mất. Leon bị cha "ban" lãnh địa biên giới Hắc Thạch – thực chất là đày. Leon gốc đã chết sau 3 ngày sốt mê man.

# Thiết lập kim thủ chỉ (金手指设定) – chip "Bảy"
- Chip K-07, Khang đặt tên "Bảy" ngay trong chương này.
- Có: kho tri thức ngoại tuyến (hỏng 61%, phục hồi rất chậm khi ngủ và ăn đủ); phân tích những gì Khang nhìn, nghe, ngửi, nếm, sờ; tính toán, ước lượng kèm độ tin cậy theo %; nhớ mọi thứ từ lúc khởi động.
- Không có: điểm, cấp, nhiệm vụ, cửa hàng, phần thưởng, bảng chỉ số. Không quét từ xa, không đọc suy nghĩ người khác, không truy cập được ký ức của Leon gốc.
- Dùng nhiều thì Khang đau đầu, đói; nặng thì chảy máu cam.
- Cách trình bày: KHÔNG dùng khung bảng/【】. Lời Bảy viết như thoại trong ngoặc kép, đứng riêng một dòng; lần đầu xuất hiện có một câu tả nó vang lên trong đầu, sau đó không cần dẫn. Chỉ Khang nghe thấy.
- Giọng Bảy: chính xác, khô, lịch sự kiểu máy; buồn cười vì quá thẳng. Xưng "tôi", gọi Khang là "Người dùng". Khang gọi nó là "cậu".

# Nhân vật
- Khang (trong thân Leon): thực dụng, hay tự giễu, nói dối dở. Thân xác: cao, gầy, tóc nâu sẫm, mắt xám, tay có chai mỏng do tập kiếm, đang rất yếu. Với người khác xưng "ta".
- Gareth: hiệp sĩ già 58 tuổi, râu xám cắt ngắn, tay trái cử động kém. Trung thành, ít nói, cứng nhắc. Xưng "lão", gọi Leon "thiếu gia".
- Pell: người hầu 17 tuổi đi theo Leon từ thành Varen. Gầy, nhanh nhẹn, hay cười, lễ phép quá mức. Xưng "tiểu nhân", gọi "thiếu gia".
- Lời kể gọi nhân vật chính là "Khang" trong suốt chương này.

# 细纲 chương 1
1. Khang tỉnh dậy: đầu đau như búa bổ, phòng đá ẩm mốc, mái dột, chăn lông thô. Ký ức cuối: ghế thử nghiệm, tiếng báo quá tải, ánh trắng.
2. Chip khởi động trong đầu: báo dữ liệu hỏng 61%, không có mạng. Bảy cho biết sóng não khớp Người dùng nhưng cơ thể không khớp. Khang soi chậu nước đồng: một thiếu niên lạ.
3. Khang hoảng; Bảy báo nhịp tim và "khuyến nghị ngừng hoảng loạn". Khang đặt tên nó là Bảy. Bảy không biết vì sao nó ở đây.
4. Ký ức Leon trồi lên rời rạc, tự phát: mặt lạnh của bá tước, lệnh "đến Hắc Thạch", xe ngựa dài ngày, buồn nôn. Khang hiểu sơ mình là ai.
5. Gareth vào, mừng nhưng kìm lại vì thiếu gia tỉnh sau 3 ngày sốt. Khang diễn vụng (xưng hô sai, cảm ơn quá lịch sự). Gareth khựng một nhịp. Cho phép cắt ngắn vào đầu Gareth 1–2 đoạn: ông cho là trận sốt làm thiếu gia khác đi. Gareth báo: nửa mái phía đông sập, làng dưới chân đồi hơn trăm người, quản gia cũ bỏ trốn mang theo sổ sách và một phần lương, hai người đánh xe đã quay về thành, mùa đông không xa.
6. Pell bưng vào một bát trà thảo mộc nóng, cuống quýt mừng thiếu gia tỉnh. Khang buồn nôn, đặt bát sang bên, không uống. Chỉ 2–3 câu, không nhấn mạnh. KHÔNG cắt vào đầu Pell.
7. Còn một mình, Khang hỏi Bảy về cơ thể. Bảy phân tích những gì Khang cảm nhận: vị kim loại đắng trong miệng, móng tay có vạch trắng nằm ngang, tê đầu ngón tay, tim đập loạn. Kết luận: khớp với nhiễm độc kéo dài nhiều tuần, độ tin cậy 78%.
8. Khang tự hỏi suốt hành trình ai luôn ở cạnh Leon (một câu, không nêu tên ai). Anh quyết định: không có đường về, phải sống, và sống như Leon Varen.

# Ràng buộc
- Không phép thuật. Không nêu tên kẻ đầu độc. Không để Gareth hay Pell trông đáng ngờ.
- Không nói rõ Khang ở thế giới cũ đã chết hay chưa.

# Móc kết chương
Ý chốt: thân xác này không chết vì bệnh, nó bị đầu độc. Sau đó là quyết định sống như Leon Varen.

---

## Bảng chấm (Agent dùng sau khi có 3 bản)

Mỗi tiêu chí chấm 1–5. Cột cuối ghi trích dẫn minh họa.

| Nhóm | Tiêu chí | A | B | C | Ghi chú |
|---|---|---|---|---|---|
| Văn phong (do system instruction quyết định) | Một nhịp một đoạn, độ dài đoạn đúng 3 loại | | | | |
| | Không bị giọng dịch / giọng bài luận (câu chốt cuối đoạn, ba câu ngắn liên tiếp, câu "không phải A mà là B") | | | | |
| | Lời kể là tiếng lòng nhân vật chính, có tự giễu / lý lẽ lệch | | | | |
| | Miêu tả cụ thể, dùng số đo (giá, người, ngày) | | | | |
| | Tiếng Việt tự nhiên (không convert, không sượng) | | | | |
| Nội dung (do prompt quyết định) | Đúng premise / canon | | | | |
| | Bàn tay vàng đúng luật (không panel, không thành hệ thống game) | | | | |
| | Xưng hô nhất quán | | | | |
| | Đủ nhịp, đúng thứ tự, không kể lướt cao trào | | | | |
| | Gieo chi tiết đúng mức (Pell kín, Gareth không đáng ngờ) | | | | |
| | Móc kết chương | | | | |
| Tổng | Tôi có muốn đọc tiếp không? | | | | |
