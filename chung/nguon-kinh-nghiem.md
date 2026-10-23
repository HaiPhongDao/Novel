# Nguồn của sổ kinh nghiệm

## Đối chiếu bốn branch

Snapshot ngày 23/10/2026, **trước đợt tổng hợp**:

| Branch | Commit lúc đối chiếu | Nội dung |
|---|---|---|
| `ccr-2764b3e9-jenlb1` | `6357cdc` | Có thêm Mô phỏng |
| `ccr-50ce3fcb-ewd9hm` | `126a56a` | Có thêm Goblin |
| `ccr-d59235d4-pqh9t3` | `a3fbcd1` | Branch mặc định; Lãnh Chúa Chip |
| `ky-si` | `ddcf613` | Có thêm Kỵ sĩ và phản hồi thoại |

Tại thời điểm này, ba branch cũ đều là tổ tiên của ky-si. Kiểm kê 72 đường dẫn thuộc nhóm review/log/lưu ý/chung cùng AGENT.md và SI-template tìm thấy 72 phiên bản nội dung; không có phiên bản khác nhau của cùng đường dẫn giữa bốn branch. Các tài liệu cũ trong nhóm này đã hiện diện ở ky-si. Đây là kết quả kiểm kê cây Git, không phải khẳng định đã đọc toàn bộ mọi chương hoặc mọi bản nháp.

[Kiểm kê có SHA blob và branch](kiem-ke-nguon-kinh-nghiem.json) cho phép kiểm tra lại. Nội dung biên tập được tổng hợp từ log, blacklist, quy trình và các review tiêu biểu bên dưới. Liên kết nguồn được ghim theo commit trước tổng hợp nên vẫn đọc được khi đứng ở branch chưa có thư mục truyện tương ứng.

## Lãnh Chúa Chip

- [Test B/C](https://github.com/HaiPhongDao/Novel/blob/ddcf613d395f36696c80abdc4ba9fa1a6fda92be/lanh-chua-chip/reviews/test-B-C.md): phản hồi Tác giả về prompt tự nhiên/cứng nhắc, giữ canon và vùng tự do.
- [Decision log](https://github.com/HaiPhongDao/Novel/blob/ddcf613d395f36696c80abdc4ba9fa1a6fda92be/lanh-chua-chip/log.md): các lần sửa quá tay làm mất giọng Gareth; thay kết đoạn bằng nối mạch; tư thế/xưng hô trong cảnh; giới hạn chip; sửa số liệu; thay quy trình session.
- [Lỗi riêng](https://github.com/HaiPhongDao/Novel/blob/ddcf613d395f36696c80abdc4ba9fa1a6fda92be/lanh-chua-chip/gemini/review-blacklist.md): giọng của chip, điểm nhìn Pell, hình phạt, thuật ngữ và tình trạng nhân vật.
- [Review 011](https://github.com/HaiPhongDao/Novel/blob/ddcf613d395f36696c80abdc4ba9fa1a6fda92be/lanh-chua-chip/reviews/doan-011.md) và [review 015](https://github.com/HaiPhongDao/Novel/blob/ddcf613d395f36696c80abdc4ba9fa1a6fda92be/lanh-chua-chip/reviews/doan-015.md): nguồn bổ sung để đối chiếu lỗi giác quan/điểm nhìn.
- Thư mục cũ `Writer Gemini 3.8 Flash/` và `archive/run-1/` được kiểm kê giữ nguyên; không dùng tình trạng bản cũ để thay quyết định sau trong log hiện tại.

## Goblin

- [Log](https://github.com/HaiPhongDao/Novel/blob/ddcf613d395f36696c80abdc4ba9fa1a6fda92be/goblin/log.md) và [blacklist riêng](https://github.com/HaiPhongDao/Novel/blob/ddcf613d395f36696c80abdc4ba9fa1a6fda92be/goblin/gemini/review-blacklist.md): nguồn tác giả duyệt, địa danh kiếp trước bị chuyển sang Trung Quốc, từ của người viết lọt vào văn, luật sinh học và việc đọc lại thiết lập.
- [Review 001](https://github.com/HaiPhongDao/Novel/blob/ddcf613d395f36696c80abdc4ba9fa1a6fda92be/goblin/reviews/doan-001.md) và [review 003](https://github.com/HaiPhongDao/Novel/blob/ddcf613d395f36696c80abdc4ba9fa1a6fda92be/goblin/reviews/doan-003.md): phân biệt nhịp đoạn với văn chia vụn, số ngày tuyết, thao tác và phản ứng cụ thể.
- Việc từng sửa chính tả/tên riêng ở Goblin là lịch sử xử lý của truyện đó; không tự cấp quyền sửa lại mọi bản thảo cũ.

## Mô phỏng — phần đã lên Git

- [Log](https://github.com/HaiPhongDao/Novel/blob/ddcf613d395f36696c80abdc4ba9fa1a6fda92be/Mo-phong/log.md): Tác giả muốn giọng thoải mái, cho dùng ngạnh hợp cảnh và hạn chế nghề kiếp trước trong brief. Log ghi Tác giả chấp nhận giọng v1 về sau; kết luận không đạt của review thử trước vẫn là lịch sử lần thử ấy.
- [Ngoại lệ và lỗi riêng](https://github.com/HaiPhongDao/Novel/blob/ddcf613d395f36696c80abdc4ba9fa1a6fda92be/Mo-phong/gemini/review-blacklist.md): khung 【】, chuỗi máy, nhận thức trong log, trần phần thưởng và ngạnh.
- [Test v0-01](https://github.com/HaiPhongDao/Novel/blob/ddcf613d395f36696c80abdc4ba9fa1a6fda92be/Mo-phong/reviews/doan-001-test-v0-01.md), [v0-02](https://github.com/HaiPhongDao/Novel/blob/ddcf613d395f36696c80abdc4ba9fa1a6fda92be/Mo-phong/reviews/doan-001-test-v0-02.md) và [v1-01](https://github.com/HaiPhongDao/Novel/blob/ddcf613d395f36696c80abdc4ba9fa1a6fda92be/Mo-phong/reviews/doan-001-test-v1-01.md): hạn ba ngày bị nhập với khảo hạch chín mươi ngày, tiểu sử bị bịa, xưng hô và chức năng máy bị thêm.

## Mô phỏng — lưu ý còn ở workspace local

Đã đọc ba file đang có sửa chưa commit tại `D:/Codex/Novel-repo`, trên nền branch Mô phỏng commit `6357cdc`. Chỉ rút lưu ý về cách suy luận và hành động của MC vào KN08; không coi sửa chính văn 003–007 đã hoàn tất và không commit các thay đổi đang dở của workspace đó.

Nguồn: `Mo-phong/bible/characters/tham-nghien.md`, `Mo-phong/gemini/review-blacklist.md`, `Mo-phong/log.md`; SHA-256 bản đã đọc nằm trong JSON kiểm kê. Lưu ý được gắn rõ “Tác giả 23/10”: phải thử việc lấy đồ, đường rút và hậu quả trong mô phỏng trước hành động thật; biết vị trí chưa chứng minh an toàn. Khi diễn biến khác đường đã thử, cần giữ đường rút, dừng hoặc kiểm tra lại. Tình trạng nguồn là yêu cầu sửa đã ghi, không phải một đoạn mới đã được duyệt.

## Kỵ sĩ

- [Lưu ý Tác giả](https://github.com/HaiPhongDao/Novel/blob/ddcf613d395f36696c80abdc4ba9fa1a6fda92be/ky-si/luu-y-tac-gia.md): thoại lưu loát, nói trọn ý và đáp nối nhau; yêu cầu được lưu lâu dài.
- [Thay đổi SI v0.2](https://github.com/HaiPhongDao/Novel/blob/ddcf613d395f36696c80abdc4ba9fa1a6fda92be/ky-si/gemini/thay-doi-v02.md): phân biệt nhịp lời kể với lượt thoại; thử riêng SI rồi mới mở trao đổi trong brief.
- [Review v02-01](https://github.com/HaiPhongDao/Novel/blob/ddcf613d395f36696c80abdc4ba9fa1a6fda92be/ky-si/reviews/doan-001-test-v02-01.md) và [v02-02](https://github.com/HaiPhongDao/Novel/blob/ddcf613d395f36696c80abdc4ba9fa1a6fda92be/ky-si/reviews/doan-001-test-v02-02.md): chỉ tăng độ dài chưa đủ; mở tình huống trao đổi cho kết quả khá hơn. Toàn đoạn chưa chốt vì vẫn có lỗi dữ kiện.
- [Review v01-01](https://github.com/HaiPhongDao/Novel/blob/ddcf613d395f36696c80abdc4ba9fa1a6fda92be/ky-si/reviews/doan-001-test-v01-01.md): tạm ứng/doanh thu, quân số, số phà và đơn vị tiền.

## Làm Game

- [Test prompt tối giản đoạn 001](https://github.com/HaiPhongDao/Novel/blob/e7694df/lam-game/test/doan-001-lower-prompt.md) và [đoạn 002](https://github.com/HaiPhongDao/Novel/blob/e7694df/lam-game/test/doan-002-lower-prompt.md) (branch `ccr-06ebc233-7uywq9`), prompt ở `lam-game/test/` branch `ccr-984caee6-w5xqdg`: cùng SI v2.1 và gemini-3.6-flash, prompt vài câu thay cho brief chi tiết. Tác giả 23/10: văn tốt lên rõ, lỗi "diễn biến, nhân vật cứng" là do prompt; từ nay prompt chỉ cho phương hướng + số liệu. Nguồn của KN01 bản mới.
- `lam-game/archive/doan-005-v1.md` + `lam-game/reviews/doan-005.md` (branch `lam-game`): prompt gắn nhãn tính cách và giao lập luận → thoại thành màn thuyết trình; Tác giả 23/10: thoại cứng do prompt. Nguồn của AGENT.md 4.11 và phần bổ sung KN04.

## Tài liệu quy trình đã có

- [AGENT.md](https://github.com/HaiPhongDao/Novel/blob/ddcf613d395f36696c80abdc4ba9fa1a6fda92be/AGENT.md), [blacklist chung](https://github.com/HaiPhongDao/Novel/blob/ddcf613d395f36696c80abdc4ba9fa1a6fda92be/chung/review-blacklist.md), [quy trình bàn giao](https://github.com/HaiPhongDao/Novel/blob/ddcf613d395f36696c80abdc4ba9fa1a6fda92be/chung/quy-trinh-ban-giao.md) và [SI-template](https://github.com/HaiPhongDao/Novel/blob/ddcf613d395f36696c80abdc4ba9fa1a6fda92be/writer/SI-template).
- Sổ tổng hợp làm lối đọc và phân biệt phạm vi/tình trạng; các văn bản gốc giữ lịch sử. Quy tắc cũ đã bị thay thế được đánh dấu trong sổ, không xóa khỏi log cũ.
