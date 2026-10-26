# Novel — xưởng viết truyện mạng

Agent (Claude) giữ canon, lập dàn ý, viết prompt và review; Writer (Gemini) viết chính văn tiếng Trung theo từng **đoạn** (~2000 字); Tác giả quyết. Luật làm việc: [`AGENT.md`](AGENT.md).

## Kinh nghiệm dùng chung

Đọc [sổ kinh nghiệm](chung/kinh-nghiem.md) trước khi lập brief, sửa SI, chạy Writer hoặc review. Bài học được tổng hợp từ cả truyện cũ và mới, có [nguồn và tình trạng](chung/nguon-kinh-nghiem.md), phân biệt quy tắc chung với ngoại lệ từng truyện. [Cách đồng bộ giữa các branch](chung/dong-bo-kinh-nghiem.md) dùng commit tài liệu chung riêng.

## Các truyện

| Thư mục | Truyện | Trạng thái |
|---|---|---|
| [`lanh-chua-chip/`](lanh-chua-chip/README.md) | Lãnh Chúa Mang Chip — kỹ sư xuyên vào cậu con thứ bị đày ra biên giới, mang theo một con chip hỏng 61% | Lượt 2: đã chốt đoạn 001–015 |
| [`lam-game/`](lam-game/README.md) | Chỉ Là Game, Cần Gì Thật — người làm 游戏策划 xuyên vào sinh viên vừa tốt nghiệp ở thế giới game full-dive tôn sùng độ chân thực; không kim thủ chỉ | Bible + dàn ý arc 1 + prompt đoạn 001 |
| [`goblin/`](goblin/README.md) | Goblin Khai Hoá — thầy giáo hoá từng làm kỹ sư lò cao xuyên vào con goblin còi vừa nở, ở cái hang mà tù trưởng ăn con non khi đói | Lượt 2 (prompt ngắn): prompt đoạn 001–002 |
| [`lanh-chua-khoa-hoc/`](lanh-chua-khoa-hoc/README.md) | Lãnh Chúa Khoa Học — CEO ngành sản xuất chính xác xuyên vào lãnh chúa trẻ vùng mỏ đá xỉ, đúng lúc phép thuật thành ngành công nghiệp; không hệ thống, không tự tay làm được nghề | Mới mở: 3 phương án tiền đề + bible nháp (overview, world, 5 nhân vật, arc 1) chờ Tác giả duyệt |
| [`ky-kham-lanh-chua/`](ky-kham-lanh-chua/README.md) | 骑砍领主：铁脊要塞 — con thứ nam tước biên bắc, 500 nông nô và một pháo đài sắp thất thủ trong ba mươi ngày; bảng 骑砍 trong đầu, cày là có | Pha đo giọng: phân tích mẫu 886 chương + SI v1 (7 anchor) + test 01 trên cảnh ch8; tiền đề chờ chốt |
| [`nong-trang-ma-phap/`](nong-trang-ma-phap/README.md) | 我在西幻种地，把法师饿死了 — tá điền xuyên việt ở làng 灰柳村, mở đầu hưu nhàn làm ruộng, bảng 经验 kiếm bằng ngày công và tiêu bằng đào tạo 村民 | Mới mở: bible + 黄金三章 + SI v2.1 + 4 bản đoạn 001 (`a`–`d`, bảng số ở `reviews/doan-001.md`) |

## Cấu trúc

| Ở đâu | Cái gì |
|---|---|
| `AGENT.md` | Luật chung: vai trò, quy trình mỗi đoạn, mẫu prompt + nguyên tắc, checklist review, git |
| `chung/quy-trinh-ban-giao.md` | Gói bàn giao và chuyển session Writer |
| `chung/ai-studio.md` | Agent tự chạy Writer trên Google AI Studio qua Claude in Chrome |
| `chung/review-blacklist.md` | Lỗi văn chung để soát khi review |
| `tools/` | `build_pack.py` (ghép gói / tin nhắn mở session), `chot_doan.py` (chốt đoạn + commit + push), `gop_doan.py` (gộp mỗi 10 đoạn thành `gop/doan-001-010.md`…), `set_clip.ps1` / `save_clip.ps1` (chuyển văn bản qua clipboard có kiểm), `aistudio_run.py` + `aistudio-ext/` (chạy Writer trên AI Studio qua extension Edge), `soat_van.py` (đếm lỗi văn đo được: phủ định lặp, so sánh người kể, độ dài đoạn), `gemini_write.py` (chạy Writer bằng Gemini API, ghi thẳng `chapters/` — [`chung/gemini-api.md`](chung/gemini-api.md)), `ollama_write.py` (chạy Writer bằng Ollama) |
| `writer/SI-template` | SI mẫu dùng chung — điền ô `[[...]]` cho từng truyện |
| `_mau-truyen/` | Khung thư mục để chép khi mở truyện mới |
| `<ten-truyen>/` | Mọi thứ của riêng một truyện: bible, plot, briefs, chapters, gop (khối 10 đoạn), reviews, handoff, SI + lỗi riêng (`gemini/`), archive, log |

## Mở truyện mới

```bash
cp -r _mau-truyen ten-truyen-moi
```

Rồi làm theo hướng dẫn ở đầu `ten-truyen-moi/README.md` (điền bible, điền SI từ `writer/SI-template`, quiz) và thêm một dòng vào bảng "Các truyện" ở trên.

## Một vòng đoạn

1. Viết `<truyện>/briefs/doan-XXX.md` theo mẫu ở AGENT.md mục 4.
2. Có Gemini API key: `python tools/gemini_write.py <truyện> <số đoạn> --push` làm luôn bước 2–3 ([`chung/gemini-api.md`](chung/gemini-api.md)). Không thì mở session mới: `python tools/build_pack.py <truyện> --prompt briefs/doan-XXX.md` → dán `handoff/session-start.md` vào Writer (đoạn thứ 2 trong cùng session thì dán thẳng prompt).
3. Lưu bản thảo vào `<truyện>/chapters/doan-XXX.md`, review theo AGENT.md mục 5.
4. Đạt: `python tools/chot_doan.py <truyện> <spec.py>`. Hỏng: chuyển bản hỏng + prompt vào `archive/`, sửa prompt, quay lại bước 2.
