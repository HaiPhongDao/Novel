# Novel — xưởng viết truyện mạng

Agent viết brief và giữ canon; Writer (Gemini trên AI Studio) viết chính văn tiếng Trung theo từng **đoạn**
(~2.000–2.500 字); Tác giả nghe, chê, chốt.

**Bắt đầu ở [`QUY-TRINH.md`](QUY-TRINH.md)** — một trang, đủ để làm ra đoạn mới. Nhánh làm việc duy nhất: `main`.

```bash
python tools/lam.py viet <truyen> <N>               # ghép prompt, chạy Writer, thay chữ, cổng máy
python tools/lam.py doc  <truyen> <N1> <N2>         # một file cho Tác giả nghe
python tools/lam.py chot <truyen> <N1> <N2> -m "…"  # README + log + commit + push
python tools/lam.py bang --ghi                      # cập nhật bảng dưới đây
```

## Tiến độ

Sinh bằng `python tools/lam.py bang --ghi`; không sửa tay. "Đã chốt tới" đọc từ bảng trạng thái trong README của
từng truyện. Truyện cũ ở nhánh khác (ky-si 001–026, lam-game 001–010, khong-binh 001–009, Mo-phong 001–007…):
[`chung/ban-do-branch.md`](chung/ban-do-branch.md).

<!-- bang:dau -->
| Truyện | Đã viết tới | Đã chốt tới | Tổng 字 | Đụng tới gần nhất |
|---|---|---|---|---|
| [`han-nien-san-dong/`](han-nien-san-dong/README.md) | 003 | — | 13.697 | 2026-11-09 |
| [`co-dai/`](co-dai/README.md) | 001 | — | 3.696 | 2026-11-07 |
| [`manga-tokyo-2000/`](manga-tokyo-2000/README.md) | 003 | 003 | 7.388 | 2026-10-31 |
| [`manga-tokyo-1994/`](manga-tokyo-1994/README.md) | 003 | 003 | 6.632 | 2026-10-31 |
| [`lanh-chua-dau-truong/`](lanh-chua-dau-truong/README.md) | 003 | 003 | 7.325 | 2026-10-31 |
| [`lanh-chua-tien-don/`](lanh-chua-tien-don/README.md) | 003 | 003 | 8.708 | 2026-10-30 |
| [`manga-tokyo-1998/`](manga-tokyo-1998/README.md) | 006 | 006 | 17.882 | 2026-10-29 |
| [`lanh-chua-chip/`](lanh-chua-chip/README.md) | 015 | 015 | 47.514 | 2026-10-23 |
<!-- bang:cuoi -->

## Ở đâu có gì

| Ở đâu | Cái gì | Khi nào đọc |
|---|---|---|
| `QUY-TRINH.md` | Hai làn (sản xuất / chỉnh giọng), vòng một lô 3 đoạn, cách xử lý lời chê, git | Mọi phiên |
| `<truyen>/README.md` | Trạng thái từng đoạn + "Việc kế" | Mọi phiên làm truyện đó |
| `<truyen>/` | `briefs/` · `chapters/` · `doc/` (file gửi Tác giả nghe) · `handoff/canon-card.md` · `gemini/` (SI, `thay-chu.txt`) · `no-giong.md` · `bible/` · `plot/` · `log.md` · `archive/` | |
| `AGENT.md` | Vai trò và phân quyền (mục 1, 7, 8, 9) | Khi cần quyết ai được đổi gì |
| `tools/lam.py` | Lệnh của làn sản xuất; gọi `aistudio_run.py` + `aistudio-ext/` (Edge), `cong_doan.py`, `gop_doan.py` | |
| `tools/gop_y.py` · `chung/gop-y-khi-nghe.md` | Phiếu góp ý DocTTS → đúng file:dòng | Khi Tác giả gửi phiếu |
| `.claude/skills/novel-craft/` · `chung/hieu-chuan/` · `writer/SI-template` · `tools/dung_si.py` | Dựng, sửa, hiệu chuẩn SI | Chỉ ở làn chỉnh giọng / mở truyện |
| `chung/loi/` · `chung/kinh-nghiem.md` · các file `chung/` khác | Sổ lỗi và bài học của ba tuần thử nghiệm | Tra cứu khi chỉnh giọng; không đọc ở làn sản xuất |
| `_mau-truyen/` | Khung thư mục chép khi mở truyện mới (QUY-TRINH.md mục 5) | |
