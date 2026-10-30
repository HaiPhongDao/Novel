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
| `chung/kinh-nghiem.md`, `chung/nguon-kinh-nghiem.md` | Sổ bài học dùng chung và nguồn của chúng ([`dong-bo-kinh-nghiem.md`](chung/dong-bo-kinh-nghiem.md) — cách đồng bộ) |
| `chung/gemini-api.md` | Chạy Writer bằng Gemini API (`tools/gemini_write.py`) |
| `chung/state-extractor.md` | Quy tắc trích State JSON sau mỗi đoạn |
| `chung/xay-dung-truyen.md`, `chung/mo-xe-truyen.md`, `chung/giu-nhat-quan.md`, `chung/tham-khao-ngoai.md`, `chung/nghien-cuu-outliner.md` | Xây dựng truyện dài, mổ xẻ truyện mẫu, giữ nhất quán, tham khảo ngoài, nghiên cứu khâu Outliner |
| `chung/can-luu-y.md` | Những điều cần lưu ý khi làm việc trên repo này (bẫy môi trường, quy ước) |
| `chung/ban-do-branch.md` | Bản đồ branch: branch nào giữ gì, cái nào đã gộp |
| `.claude/skills/novel-craft/` | Skill của Agent: cách làm + vòng tự học (`SKILL.md` và `references/`) |
| `.claude/agents/novel-doan.md` | Agent con chạy liền một lô đoạn từ brief đã viết sẵn |
| `tools/` | `build_pack.py` (ghép gói / tin nhắn mở session), `chot_doan.py` (chốt đoạn + commit + push), `gop_doan.py` (gộp mỗi 10 đoạn), `aistudio_run.py` + `aistudio-ext/` (chạy Writer trên AI Studio qua extension Edge), `gemini_write.py` (Writer qua Gemini API — [`chung/gemini-api.md`](chung/gemini-api.md)), `viet_doan.sh` (một đoạn: ghép gói → chạy → soát), `cong_doan.py` / `soat_van.py` / `soat_tat.py` / `cham_doan.py` / `noi_doan.py` / `ra_soat.py` (cổng máy, đếm tật, chấm, nối, rà soát), `bao_thuc.py`, `set_clip.ps1` / `save_clip.ps1`, `ollama_write.py` |
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
