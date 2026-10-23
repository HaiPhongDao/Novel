# Sổ kinh nghiệm dùng chung — Novel

Bản tổng hợp ngày 23/10/2026 từ Lãnh Chúa Chip, Goblin, Mô phỏng và Kỵ sĩ. Đọc trước khi lập brief, chỉnh SI, chạy Writer hoặc review. [Nguồn và tình trạng](nguon-kinh-nghiem.md) ghi rõ bài học đến từ đâu; [cách đồng bộ](dong-bo-kinh-nghiem.md) giúp các branch dùng cùng bản.

Đây là kinh nghiệm làm việc và yêu cầu phong cách, không phải canon chung của bốn truyện. Yêu cầu hiện tại của Tác giả và luật/SI đã chốt của từng truyện quyết định cách áp dụng. Một kết quả thử chưa đủ thành quy luật cho mọi model, mọi thể loại.

## Những điều cần mang sang lần viết tiếp theo

| ID | Phát hiện và cách áp dụng | Nguồn / phạm vi |
|---|---|---|
| KN01 | **Prompt ngắn: phương hướng + số liệu, còn lại Writer tự do** (Tác giả 23/10, thay cách cũ). Vài câu nói nối từ đâu, chuyện đi về đâu, dừng ở đâu; thêm con số giữ độ khó (tiền, hạn, giá). Prompt dài, nhiều thiết lập và điểm bắt buộc làm nhiễu Writer: diễn biến và nhân vật cứng. Chỉ thêm câu khi đoạn trước đã hỏng đúng chỗ đó. Mẫu ở AGENT.md mục 4. | Làm Game: test prompt tối giản 001–002 (`lam-game/test/`), cùng SI và model; trước đó Lãnh Chúa Chip test B/C |
| KN02 | **Giao sự việc thay cho ý nghĩa muốn người đọc hiểu.** Thái độ đổi bằng việc làm, con số khai thật, vật trao tay hoặc quyết định; câu chỉ đạo kiểu “cho thấy đã kính phục” dễ bị kể lại thành lời giải thích. | Lãnh Chúa Chip 004–005; Goblin 001 |
| KN03 | **SI mô tả cách viết đúng; ví dụ lỗi để Agent soát.** Trong các lần thử của repo, từ bị cấm và ví dụ sai từng lọt lại vào văn. Cấp từ đúng, mô tả thao tác viết; tránh lặp tính từ phẩm chất khiến Writer diễn chúng vào câu. | Lãnh Chúa Chip; SI-template; đây là quan sát thử nghiệm của repo |
| KN04 | **Thoại nói trọn ý và đáp nối nhau.** Nhịp đoạn kể ngắn không là hạn mức lượt nói. Giải thích, báo cáo và bàn bạc cần đủ ý; khẩu lệnh có thể gọn. Brief phải tạo chỗ cho người nghe nêu khó khăn, hỏi lại hoặc góp ý. Chỉ kéo dài câu không giải quyết được thoại cụt. Cảnh bàn việc: prompt cho mỗi người mối bận tâm và câu hỏi thực tế, không gắn nhãn tính cách, không giao lập luận để trình bày — nếu không thoại thành màn thuyết trình (AGENT.md mục 4.11). | Gareth ở Lãnh Chúa Chip; phản hồi Tác giả và thử v02 của Kỵ sĩ; Làm Game lượt 2 đoạn 005 (Tác giả 23/10) |
| KN05 | **Giữ phần giải thích có chủ thể.** Phép tính và suy luận có thể thuộc MC; báo cáo thuộc người báo cáo. So sánh trong đầu/miệng nhân vật có thể giữ giọng. Không cắt sạch lời giải thích hoặc so sánh chỉ vì đã gặp một loại giải thích thừa. | Lãnh Chúa Chip: bản sửa quá tay làm mất giọng Gareth |
| KN06 | **Đoạn là phần của một mạch truyện.** Mở nối đúng khoảnh khắc trước, dừng giữa hành động/thoại/suy nghĩ; việc kế tiếp thuộc đoạn sau. Nhảy thời gian ở trong đoạn. Chỉ lấy khoảng hai cảnh và một lần nhảy làm giới hạn làm việc hiện tại của repo, không nhồi cả arc vào khoảng 2.000 chữ. | Lãnh Chúa Chip 005, 009+; Goblin 003, 006 |
| KN07 | **Giữ điểm nhìn và ranh giới hiểu biết ngay trong cảnh.** Ai được nghĩ, ai chỉ có lời và việc phải rõ. Điều mới nghe, suy đoán và điều đã kiểm chứng là ba mức khác nhau; tránh lời kể tự xác nhận âm mưu, lý lịch hoặc tải/phương tiện mà nhân vật chưa biết. | Pell ở Lãnh Chúa Chip; log Mô phỏng; Mira ở Kỵ sĩ |
| KN08 | **Thận trọng phải có căn cứ trong diễn biến.** Với MC được thiết lập cẩn trọng, việc biết vị trí món đồ chưa chứng minh lấy được và rút an toàn. Nếu truyện có mô phỏng, thử cả hành động, đường rút và hậu quả trước việc thật tương ứng. Áp dụng theo thiết lập MC, không biến mọi nhân vật thành cùng một kiểu hành động. | Yêu cầu sửa Mô phỏng 003–004; nguồn local chưa commit, tình trạng ở bảng nguồn |
| KN09 | **Con số phải gắn đơn vị, mốc và phép tính.** Tách tiền mặt, doanh thu, tạm ứng, chi phí dự toán và chi thật. Tách hạn nộp tiền, ngày khảo hạch, tuổi thọ. Quân số ghi rõ ai đã nằm trong nhóm. Khi MC tính sổ, brief cấp tổng và khung so sánh đúng; state giữ số Agent đã kiểm. | Lãnh Chúa Chip: củi/thịt/lương; Goblin: dân số/ngày tuyết; Mô phỏng: các hạn; Kỵ sĩ: tiền và quân số |
| KN10 | **Bàn tay vàng tuân theo hợp đồng riêng của truyện.** Kiểm tên, cách xưng, hình thức hiện, giác quan, chi phí và giới hạn mang về. Trình bày hay kỹ năng có trong mẫu không tự thành chức năng mới. Dòng máy cố định được cấp nguyên văn trong prompt. | Cả bốn truyện; xem bảng ngoại lệ bên dưới |
| KN11 | **Tham khảo kỹ thuật, không nhập thiết lập của mẫu.** Giữ trích mẫu nguyên văn và có nguồn để học nhịp, lời kể, thoại; soát tên, câu cửa miệng, cơ chế và tiểu sử bị bê sang. Chính văn tiếng Trung không xác định quê quán hoặc quốc tịch kiếp trước. Chỉ đưa thông tin quá khứ đoạn này cần dùng. | Goblin: địa danh kiếp trước; Mô phỏng: nghề cũ lặp; Kỵ sĩ: dữ kiện tự thêm |
| KN12 | **Giữ đúng trải nghiệm thể loại Tác giả chọn.** Ghi rõ yếu tố hài, ngạnh, lạnh hoặc căng thẳng được dùng thế nào trong từng truyện. Thêm một câu “viết vui” chưa bảo đảm đổi được nhịp cả cảnh; cần đọc kết quả thật. | Mô phỏng v0/v1; ngoại lệ về 梗; Goblin và Kỵ sĩ có register riêng |
| KN13 | **Thử có lưu dấu và kết luận đúng mức.** Lưu nguyên bản, SI, prompt, model/cấu hình, session và review. Giữ cùng prompt khi muốn xem riêng tác dụng SI; nếu đổi cả hai, ghi rõ. Độ dài, tỉ lệ thoại hoặc số từ lặp là tín hiệu, không tự là kết luận chất lượng. | Test B/C; Mô phỏng; Kỵ sĩ v02-01/v02-02 |
| KN14 | **Bàn giao là bộ nhớ đã kiểm.** Theo quy trình hiện tại, tối đa hai đoạn/session; đoạn hỏng thử lại ở session mới, giữ nguyên bản cũ. Gói cần luật, tóm tắt, state, mẫu giọng đã duyệt và đuôi đoạn trước. Chi tiết dự kiến hoặc Writer tự thêm chưa duyệt không ghi như sự kiện canon. | Lãnh Chúa Chip; quy trình bàn giao; Kỵ sĩ |

## Những điều chỉ áp dụng theo truyện

| Truyện | Cách áp dụng đúng | Không nâng thành quy tắc chung |
|---|---|---|
| Lãnh Chúa Chip | 小七 chỉ là giọng nói; giới hạn theo giác quan Leon; tên Latin; điểm nhìn bảo vệ bí mật Pell. | Không suy ra mọi bàn tay vàng đều cấm chữ trong tầm nhìn. |
| Goblin | Không có hệ thống game; luật bắt chước, Mẹ Ổ và đếm tới năm theo bible; xử lý đúng căn cước Khoa. | Không mang luật sinh học hoặc mức hài đen sang truyện khác. |
| Mô phỏng | Có log 【】 trong đầu, chuỗi và giá riêng; tên Hán theo quy ước truyện; ngạnh gắn tình huống được Tác giả cho phép. | Không dùng blacklist từ Lãnh Chúa Chip để bắt mọi khung 【】 hoặc mọi ngạnh. |
| Kỵ sĩ | Bản làm việc cho phép bảng số liệu riêng; hồ sơ luyện tập không chứng minh lòng trung thành; tiền và quyền hạn theo hợp đồng. | Chưa coi tên, thông số phà, thân phận Writer tự đổi hoặc mọi chi tiết bản thử là canon đã chốt. |

## Quyết định cũ đã được thay thế

Log cũ được giữ làm lịch sử. Khi tổng hợp, dùng quyết định sau cùng trong đúng phạm vi của nó.

| Cách làm cũ | Cách hiện dùng | Căn cứ |
|---|---|---|
| Brief chi tiết: thiết lập đầy đủ, điểm bắt buộc, mục tự do sáng tạo ("chốt sự thật và điểm đến, thả cách đi") | Prompt vài câu: phương hướng + số liệu, Writer tự do phần còn lại | Test Làm Game 23/10; Tác giả xác nhận văn tốt lên rõ |
| Kết đoạn bằng một hình ảnh khép lại | Mở nối thẳng và dừng giữa mạch | Phản hồi Tác giả ở Lãnh Chúa Chip 009+; AGENT.md mục 4.9 |
| Writer tự kiểm sau khi viết như khâu duyệt | Agent đọc bản thật và review; chuẩn viết nằm trong SI | Lãnh Chúa Chip; AGENT.md mục 4.10 |
| Chuyển session sau 2–3 đoạn | Tối đa hai đoạn/session theo quy trình repo hiện tại | Lãnh Chúa Chip 005; quy-trinh-ban-giao.md |
| Bỏ mọi phần giải thích hoặc so sánh | Giữ phần thuộc suy nghĩ/thoại nhân vật; bắt phần giải thích thừa đúng chỗ | Phản hồi về Gareth, Lãnh Chúa Chip |
| Bắt mọi bảng 【】, từ hệ thống hoặc meme chỉ vì có trong blacklist | Xét cơ chế, register và ngoại lệ của đúng truyện | Mô phỏng và Kỵ sĩ khác Lãnh Chúa Chip/Goblin |

## Dùng trong một lượt làm việc

1. Đọc sổ này và yêu cầu mới nhất của Tác giả, rồi README/log/state/review của truyện.
2. Chọn các KN liên quan. SI chỉ mang chuẩn văn phong; brief mang sự thật và việc đang xảy ra; checklist giữ ví dụ lỗi.
3. Review đối chiếu văn thật, ghi cả điều giữ được lẫn lỗi. Yêu cầu chạy thử không đồng nghĩa Tác giả duyệt bản thử.
4. Có phát hiện mới thì ghi nguồn, phạm vi, tình trạng và quyết định thay thế nếu có; tạo commit tài liệu chung riêng để đồng bộ. Xem [quy trình đồng bộ](dong-bo-kinh-nghiem.md).
