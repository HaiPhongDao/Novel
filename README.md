# Novel — xưởng viết truyện mạng

Agent (Claude) giữ canon, lập dàn ý, viết prompt và review; Writer (Gemini) viết chính văn tiếng Trung theo từng **đoạn** (~2000 字); Tác giả quyết. Luật làm việc: [`AGENT.md`](AGENT.md).

## Kinh nghiệm dùng chung

Đọc [sổ kinh nghiệm](chung/kinh-nghiem.md) trước khi lập brief, sửa SI, chạy Writer hoặc review. Bài học được tổng hợp từ cả truyện cũ và mới, có [nguồn và tình trạng](chung/nguon-kinh-nghiem.md), phân biệt quy tắc chung với ngoại lệ từng truyện. [Cách đồng bộ giữa các branch](chung/dong-bo-kinh-nghiem.md) dùng commit tài liệu chung riêng.

## Các truyện

| Thư mục | Truyện | Trạng thái |
|---|---|---|
| [`lanh-chua-chip/`](lanh-chua-chip/README.md) | Lãnh Chúa Mang Chip — kỹ sư xuyên vào cậu con thứ bị đày ra biên giới, mang theo một con chip hỏng 61% | Lượt 2: đã chốt đoạn 001–015 |

## Cấu trúc

| Ở đâu | Cái gì |
|---|---|
| `AGENT.md` | Luật chung: vai trò, quy trình mỗi đoạn, mẫu prompt + nguyên tắc, checklist review, git |
| `chung/quy-trinh-ban-giao.md` | Gói bàn giao và chuyển session Writer |
| `chung/ai-studio.md` | Agent tự chạy Writer trên Google AI Studio qua Claude in Chrome |
| `chung/review-blacklist.md` | Lỗi văn chung để soát khi review |
| `chung/mo-xe-truyen.md` | Mổ xẻ truyện top (拆书): ba chương đầu, đơn vị cốt truyện, nhịp, mô-đun cảm xúc, văn mẫu → lưu ở `mo-xe/<truyen-mau>/` |
| `chung/xay-dung-truyen.md` | Hợp đồng độc giả, nợ mong chờ, quỹ kết cục, neo arc, trạng thái đổi mỗi đoạn, bảng chỗ dừng |
| `chung/giu-nhat-quan.md` | Ba tầng biết, thẻ state gọn, ngưỡng chống quên, soát nhất quán khi truyện dài |
| `chung/tham-khao-ngoai.md` | Repo ngoài đã tham khảo, giấy phép, lấy gì / không lấy gì |
| `tools/` | `build_pack.py` (ghép gói / tin nhắn mở session), `chot_doan.py` (chốt đoạn + commit + push), `ra_soat.py` (rà soát mỗi 5 đoạn: nhân vật vắng, tuyến đứng yên, cài cắm quá hạn), `set_clip.ps1` / `save_clip.ps1` (chuyển văn bản qua clipboard có kiểm), `ollama_write.py` (chạy Writer bằng Ollama) |
| `writer/SI-template` | SI mẫu dùng chung — điền ô `[[...]]` cho từng truyện |
| `_mau-truyen/` | Khung thư mục để chép khi mở truyện mới |
| `<ten-truyen>/` | Mọi thứ của riêng một truyện: bible, plot, briefs, chapters, reviews, handoff, SI + lỗi riêng (`gemini/`), archive, log |

## Mở truyện mới

```bash
cp -r _mau-truyen ten-truyen-moi
```

Rồi làm theo hướng dẫn ở đầu `ten-truyen-moi/README.md` (điền bible, điền SI từ `writer/SI-template`, quiz) và thêm một dòng vào bảng "Các truyện" ở trên.

## Một vòng đoạn

1. Viết `<truyện>/briefs/doan-XXX.md` theo mẫu ở AGENT.md mục 4.
2. Mở session mới: `python tools/build_pack.py <truyện> --prompt briefs/doan-XXX.md` → dán `handoff/session-start.md` vào Writer (đoạn thứ 2 trong cùng session thì dán thẳng prompt).
3. Lưu bản thảo vào `<truyện>/chapters/doan-XXX.md`, review theo AGENT.md mục 5.
4. Đạt: `python tools/chot_doan.py <truyện> <spec.py>`. Hỏng: chuyển bản hỏng + prompt vào `archive/`, sửa prompt, quay lại bước 2.
5. Mỗi 5 đoạn: `python tools/ra_soat.py <truyện>` ([cách xử lý](chung/giu-nhat-quan.md)).
