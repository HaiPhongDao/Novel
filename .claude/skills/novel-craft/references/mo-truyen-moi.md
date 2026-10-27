# Mở truyện mới từ `_mau-truyen/`

Dùng khi Tác giả muốn bắt đầu truyện mới, bible còn trống. Luật nền: `AGENT.md` mục 11.

## Trình tự

1. **Đọc trước:** `AGENT.md`, `README.md` gốc (bảng truyện), `chung/kinh-nghiem.md`, và bible của truyện gần nhất cùng thể loại để biết cái gì **không** nên lặp.
2. **Chép khung:** `cp -r _mau-truyen <ten-truyen>` — tên thư mục chữ thường, không dấu, nối bằng `-` (`lanh-chua-khoa-hoc`).
3. **Thảo luận tiền đề trước, viết bible sau:** 2–3 phương án (thế giới/trục truyện/kiểu MC), mỗi phương án nêu sức hút, rủi ro, độ khó viết, mức trùng với truyện đã có; kèm khuyến nghị. Lưu vào `<truyen>/archive/phuong-an-tien-de.md`. Chốt thì ghi `**ĐÃ CHỐT <ngày>: …**` ở đầu file đó (giữ phần đã loại làm hồ sơ) và ghi một dòng `log.md` (`| Duyệt: Tác giả`).
4. **Điền bible theo thứ tự:** `overview.md` → `glossary.md` → `characters/` → `world.md` → `plot/arcs.md` → `plot/outline.md`.
5. **README truyện** (logline, trạng thái, bảng so sánh với truyện cùng thể loại, bảng trạng thái đoạn) + **một dòng trong bảng truyện ở `README.md` gốc**.
6. **Handoff đoạn 0:** `canon-card.md` (thẻ thiết lập), `state.md` (số liệu khởi điểm), `quiz.md` (3 câu: ai / bí mật gì / con số gì).
7. **SI:** chỉ tạo khi tiền đề đã chốt; xem `si-khong-ban-tay-vang.md` nếu truyện không có hệ thống.
8. **Brief đoạn 001** theo `AGENT.md` mục 4 (150–300 chữ, chỉ phương hướng + số liệu). Đoạn 001 nên thiết lập luật riêng của truyện ngay cảnh đầu (ví dụ: MC làm hỏng một việc bằng tay).

## Nội dung bible phải có

- **overview:** logline 1 câu, premise 1 đoạn, thể loại, chủ đề, tông, độc giả, sức hút cốt lõi, **rủi ro đã biết + cách chặn**, và mục "khác truyện cũ ở đâu".
- **world:** luật cứng (cái gì không bao giờ xảy ra), kinh tế/tiền tệ, địa danh có con số, và **mục "năng lực của MC"** theo hợp đồng bàn tay vàng (KN10): cái anh có, cái anh không có, cái anh được phép sai.
- **characters:** mỗi file một nhân vật — tuổi, nghề, thứ họ giỏi, thứ họ không biết, động cơ, điểm yếu, giọng nói/xưng hô, vai trò trong arc 1. Phản diện phải có **lý lẽ đúng một nửa** để nuôi được 10–20 đoạn mà không cần đánh nhau.
- **glossary:** tên riêng Latin (chính văn giữ Latin) + cột 中文 tham khảo, thuật ngữ, **bảng xưng hô cố định** (ai gọi ai là gì, khi nào đổi).

## Số liệu phải có ngay ở `handoff/state.md` (đoạn 0)

Dân số · nợ và hạn · tiền mặt · lương/chi phí tháng · nguồn thu chính. Brief ngắn dựa hoàn toàn vào số, nên số phải được chốt trong bible/state trước khi viết đoạn 001 — nếu không Writer tự đặt và độ khó lệch.

## Pitfall: ghi đè file vừa chép từ template

`cp -r` tạo file mà phiên làm việc chưa đọc, nên công cụ ghi file từ chối ghi đè ("has not seen its full current content"). Cách đúng:

1. Đọc từng file sẽ ghi đè **trước khi** ghi.
2. Nếu vẫn bị từ chối với "last read with offset/limit pagination": dùng `patch` cho sửa cục bộ; hoặc khi thay **toàn bộ** nội dung bằng bản mình vừa viết, `mv` file cũ sang `$TMPDIR` rồi `write_file` vào đường dẫn mới.

Đừng dùng mẹo `mv` cho sửa một phần — mất phần còn lại của file.

## Không nên làm

- Viết bible chi tiết hết arc 1 khi tiền đề chưa được duyệt.
- Chép thiết lập của truyện đã có (địa danh, con số, nghề MC) sang truyện mới — KN11.
- Commit/push thay Tác giả khi chưa được bảo, nhất là trên branch lạ; nêu rõ trạng thái chưa commit thay vì tự quyết.
