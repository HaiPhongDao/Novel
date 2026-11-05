# sung-thu — truyện mới, bộ mẫu 《神宠供应商》

- **Trạng thái:** làn mở truyện, **bước 0 — hiệu chuẩn SI** (`chung/hieu-chuan/README.md`). Chưa có bible, dàn ý,
  tên truyện: Tác giả đọc bài hiệu chuẩn và nói ĐẠT thì mới dựng.
- **Bộ mẫu:** 《神宠供应商》 — 轻泉流响, chương 1–140, `sung-thu/神宠供应商(1-140章).txt` (UTF-8, 516.707 ký tự).
  Tách được 138 chương; ch69 và ch86 có tiêu đề lệch khuôn. Chưa commit toàn văn (AGENT.md mục 2: không commit toàn
  văn truyện mẫu) — chỉ commit chương đáp án.
- **Thể loại bộ mẫu:** 御兽 + 繁育, thế giới biển sau mạt thế mưa lớn. MC xuyên việt, kiếp trước là thợ lai tạo thú
  cưng, có 「数据之眼」 nhìn ra thiên phú ẩn của biến dị thú; giọng nhanh, MC tự giễu, chuỗi giá/cấp tiến hoá, bảng
  【种族】… in khi nhìn một con thú.
- **SI đang thử:** `gemini/system-instruction-v1.md` → bản dán `gemini/si-dan-gemini.txt` (5.468 ký tự `len()`).
  Khung gọn L-13R0B của làn manga (FIXED + mục 1 + mục 3 + BANS 4 dòng + PART 3, không ROLE) + PART 4 bàn tay vàng.
  3 anchor nguyên văn: ch14 (mục 1), ch35 (mục 3), ch11 (PART 4) — `verify_anchors.py` 3/3, `soat_van.py` 0 tật.
- **Bài thử:** chương 3 「神宠供应商」 (2.822 字, ba tiệm bán 中位种). Đáp án + brief:
  `chung/hieu-chuan/than-sung/ch03/`. Bảng biên độ 30 chương của bộ mẫu: `chung/hieu-chuan/than-sung/bang-mau.json`.
- **Khung brief cho truyện thật:** chưa chọn (mẫu A hay B) — hỏi Tác giả sau khi SI ĐẠT. Ba đoạn đầu chạy theo
  `chung/hieu-chuan/prompt-agent-writer.md` (brief sáu khối, hai lần chạy, không sửa SI).

## Bài hiệu chuẩn

| Lần | SI | Brief | Bản sinh | Đọc cặp | Tác giả |
|---|---|---|---|---|---|
| v1 | v1 (5.468) | `ch03/brief.md` | `gemini/test-giong/v1-ch03-a.md` (3.646 字), `-b.md` (2.769 字) | **`gemini/test-giong/doc-v1-ch03.md`** (cùng sự việc, ba bản) · `gemini-doc-v1-ch03.md` (Gemini đọc, 51/51 trích thật) · `doc-cap-v1-ch03-a.md`, `-b.md` (theo vị trí) | chờ đọc |

Agent đọc v1: đúng chuỗi sự việc và số, bảng 【】 đúng; **sai giọng** — văn trang trọng, MC điềm tĩnh (淡然/平静 出言),
mất tiếng lòng hài của bộ mẫu (！/？ trong lời kể 2,8/2,5 → ~0 /1.000 字), câu dài gần gấp đôi. Thinking chỉ tự kiểm
BANS và số chữ. Đề xuất biến kế: bỏ BANS (chi tiết trong `doc-v1-ch03.md`).

## Số đo bộ mẫu (30 chương đầu, TB ± 2SD) — chỉ để khoanh vùng, không chấm

| Chỉ số | TB | Khoảng |
|---|---|---|
| 字/đoạn | 26,5 | 19,6 – 33,4 |
| 字/câu | 22,2 | 14,8 – 29,5 |
| lượt thoại | 40,7 | 16,6 – 64,8 |
| 字/lượt thoại | 17,0 | 6,5 – 27,6 |
| giảng huấn /1.000 | 0,30 | 0 – 1,0 |
| đoạn dài nhất | 84,0 | 57,7 – 110,3 |
| % đoạn có thoại | 37,9 | 20,1 – 55,7 |

`tools/hieu_chuan.py so-sanh` đọc bảng của bộ mẫu manga (`chung/hieu-chuan/bang-mau.json`), nên cột "biên độ" nó
in **không phải** của bộ mẫu này — so với bảng trên.
