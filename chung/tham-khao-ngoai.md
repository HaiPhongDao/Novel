# Tham khảo từ repo ngoài

Đọc ngày 23/10/2026 (bản clone nông, nhánh mặc định). Repo này **không chép mã hay văn bản** của họ; chỉ chuyển thể phương pháp sang quy trình đoạn/brief/review của mình. Mọi điều rút ra đang ở tình trạng **đề xuất chưa thử**; khi dùng thử trong một truyện và có review, ghi kết quả vào [kinh-nghiem.md](kinh-nghiem.md) theo mẫu ở [dong-bo-kinh-nghiem.md](dong-bo-kinh-nghiem.md).

| Repo | Giấy phép | Lấy gì | Vào đâu |
|---|---|---|---|
| [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) — bộ skill viết truyện mạng cho Claude Code: quét bảng xếp hạng, mổ xẻ, viết dài/ngắn, khử "mùi AI" | MIT | Quy trình mổ xẻ 6 giai đoạn (ba chương đầu, tóm tắt chương, đơn vị cốt truyện, nhịp ba trục, thẻ mô-đun cảm xúc, văn mẫu); hợp đồng độc giả, nợ mong chờ, quỹ kết cục; bảng móc chương; thẻ trạng thái bảy khối có giới hạn; hai dòng thời gian (tác giả / độc giả) | [mo-xe-truyen.md](mo-xe-truyen.md), [xay-dung-truyen.md](xay-dung-truyen.md), [giu-nhat-quan.md](giu-nhat-quan.md) |
| [leenbj/novel-creator-skill](https://github.com/leenbj/novel-creator-skill) — bộ nhớ dài hạn dạng file cho truyện trăm vạn chữ | không ghi giấy phép → chỉ đọc ý tưởng | Phanh chống giải quyết sớm, neo arc (phải đạt / chưa được lộ), luân phiên loại sự kiện, bảng cài cắm theo độ gấp | [xay-dung-truyen.md](xay-dung-truyen.md) mục 4, 6; mẫu `plot/threads.md` |
| [wordflowlab/novel-writer-skills](https://github.com/wordflowlab/novel-writer-skills) — skill kiểm nhất quán và nhắc phần tử bị quên | MIT | Ngưỡng nhân vật vắng / tuyến đứng yên / cài cắm chưa trả; nhóm soát nhất quán; hồ sơ giọng nhân vật | [giu-nhat-quan.md](giu-nhat-quan.md) mục 4, 6, 7; `tools/ra_soat.py`; mẫu hồ sơ nhân vật |
| [xindoo/ai-novel-lab](https://github.com/xindoo/ai-novel-lab) — thử cho AI viết 100 chương | MIT | Chỉ đọc làm đối chứng: nhất quán phân tầng (thiết lập vĩ mô + chi tiết vi mô). Không lấy gì cụ thể | — |

## Không mang sang

- **Tự động hoá viết + chấm điểm bằng model** (agent viết, agent tự kiểm, cổng chất lượng tự động): repo này giữ Writer Gemini viết, Agent review văn thật, Tác giả duyệt (AGENT.md mục 3, nguyên tắc 10).
- **JSON trạng thái là nguồn sự thật** sinh ra các file Markdown: hợp với hệ tự động; ở đây bible và handoff do Agent viết tay và Tác giả đọc được, nên giữ Markdown làm nguồn. Chỉ lấy *khuôn* (khối cố định, giới hạn sức chứa, ghi lại thứ bị rút).
- **Danh sách từ cấm đưa vào prompt**: trái KN03 / nguyên tắc 1 — mặt sai chỉ nằm trong blacklist cho review.
- **Công thức theo thể loại, số chương cố định cho một vòng vả mặt**: dùng như dữ liệu tham khảo khi mổ xẻ, không thành quy tắc cho truyện của mình.
