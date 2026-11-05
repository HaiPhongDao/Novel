# sung-thu — truyện mới, bộ mẫu 《神宠供应商》

- **Trạng thái:** làn mở truyện, **bước 0 — hiệu chuẩn SI** (`chung/hieu-chuan/README.md`). Chưa có bible, dàn ý,
  tên truyện: Tác giả đọc bài hiệu chuẩn và nói ĐẠT thì mới dựng.
- **Bộ mẫu:** 《神宠供应商》 — 轻泉流响, chương 1–140, `sung-thu/神宠供应商(1-140章).txt` (UTF-8, 516.707 ký tự).
  Tách được 138 chương; ch69 và ch86 có tiêu đề lệch khuôn. Chưa commit toàn văn (AGENT.md mục 2: không commit toàn
  văn truyện mẫu) — chỉ commit chương đáp án.
- **Thể loại bộ mẫu:** 御兽 + 繁育, thế giới biển sau mạt thế mưa lớn. MC xuyên việt, kiếp trước là thợ lai tạo thú
  cưng, có 「数据之眼」 nhìn ra thiên phú ẩn của biến dị thú; giọng nhanh, MC tự giễu, chuỗi giá/cấp tiến hoá, bảng
  【种族】… in khi nhìn một con thú.
- **SI đang dùng:** `gemini/system-instruction-v1.md` (5.468 ký tự `len()`) → bản dán `gemini/si-dan-gemini.txt`, dựng bằng
  `python tools/dung_si.py sung-thu --version 1` (luôn ghi `--version 1`: không có cờ thì script lấy v2). v2 (= v1 bỏ
  BANS, 5.025) giữ làm lưu trữ — I-0049 vô hiệu, đã gỡ 05/11.
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
| v2 | v2 = v1 bỏ BANS (5.025) | `ch03/brief.md` | `gemini/test-giong/v2-ch03-a.md` (4.180 字), `-b.md` (4.205 字) | **`gemini/test-giong/doc-v2-ch03.md`** (bảng v1 ↔ v2) · `gemini-doc-v2-ch03.md` (Gemini đọc, 45/45 trích thật) | chờ đọc |
| v3 A | v1 · **thinking Low** | `ch03/brief.md` | `gemini/test-giong/v3/A-a.md` (3.322 字), `A-b.md` (3.834 字) | **`gemini/test-giong/v3/doc-v3-ch03.md`** (bảng v1 · v2 · A · B · C) · `v3/gemini-doc-A.md` (44/44) | chờ đọc |
| v3 B | v1 · High | `v3/brief-B.md` = brief + **thẻ giọng** | `v3/B-a.md` (2.579 字), `B-b.md` (3.328 字) | `doc-v3-ch03.md` · `v3/gemini-doc-B.md` (54/54) | chờ đọc |
| v3 C | `v3/si-C.txt` = v1, **anchor mục 1 → ch16** (5.642) | `ch03/brief.md` | `v3/C-a.md` (3.280 字), `C-b.md` (3.498 字) | `doc-v3-ch03.md` · `v3/gemini-doc-C.md` (52/52) | chờ đọc |
| v4 E | `v4/si-E.txt` = v1 + **ví dụ brief → văn ch2** (10.612) | `ch03/brief.md` | `v4/E-a.md` (3.104 字), `E-b.md` (3.537 字) | **`gemini/test-giong/v4/doc-v4-ch03.md`** (bảng v1 · E · N · EN) · `v4/gemini-doc-E.md` (54/54) | **bác** ("Đều không đạt") |
| v4 N | `v4/si-N.txt` = v1 **sửa người kể** (6.168) | `ch03/brief.md` | `v4/N-a.md` (3.239 字), `N-b.md` (3.564 字) | `doc-v4-ch03.md` · `v4/gemini-doc-N.md` (44/44) | **bác** |
| v4 EN | `v4/si-EN.txt` = ví dụ + sửa người kể (11.312) | `ch03/brief.md` | `v4/EN-a.md` (3.645 字), `EN-b.md` (3.642 字) | `doc-v4-ch03.md` · `v4/gemini-doc-EN.md` (49/49) | **bác** |
| v5 P1 | v1 (5.468) | `v5/brief-P1.md` = "Viết tiếp" + **nối tiếp đuôi ch2** | `v5/P1-a.md` (3.367 字), `P1-b.md` (2.826 字) | **`gemini/test-giong/v5/doc-v5-ch03.md`** (bảng v1 · P1 · P2 · P3) · `v5/gemini-doc-P1.md` (63/63) | chờ đọc |
| v5 P2 | v1 | `v5/brief-P2.md` = P1 + **ví dụ ch2 trong prompt** | `v5/P2-a.md` (4.055 字), `P2-b.md` (3.548 字) | `doc-v5-ch03.md` · `v5/gemini-doc-P2.md` (40/40) | chờ đọc |
| v5 P3 | v1 | `v5/brief-P3.md` = P2 + **7 chỗ đánh dấu dịp nội tâm** | `v5/P3-a.md` (3.801 字), `P3-b.md` (3.110 字) | `doc-v5-ch03.md` · `v5/gemini-doc-P3.md` (49/49) | chờ đọc |
| **v6 X** | `v6/si-argon.txt` (Argon, 7.630) | `v6/brief-argon.md` (Argon) | **`v6/X-a.md`** (4.713 字), `X-b.md` (5.426 字) | **`gemini/test-giong/v6/doc-v6-ch03.md`** (bảng v1 · P3 · X · S · B, 7 chỗ kiểm, 8 câu đùa) · `v6/gemini-doc-X.md` (43/43) | chờ đọc |
| v6 S | `v6/si-argon.txt` | `ch03/brief.md` (gốc) | `v6/S-a.md` (4.460 字), `S-b.md` (4.279 字) | `doc-v6-ch03.md` · `v6/gemini-doc-S.md` (64/64) | chờ đọc |
| v6 B | v1 (5.468) | `v6/brief-argon.md` | `v6/B-a.md` (3.591 字), `B-b.md` (3.069 字) | `doc-v6-ch03.md` · `v6/gemini-doc-B.md` (46/46) | chờ đọc |

Agent đọc v1: đúng chuỗi sự việc và số, bảng 【】 đúng; **sai giọng** — văn trang trọng, MC điềm tĩnh (淡然/平静 出言),
mất tiếng lòng hài của bộ mẫu (！/？ trong lời kể 2,8/2,5 → ~0 /1.000 字), câu dài gần gấp đôi. Thinking chỉ tự kiểm
BANS và số chữ. Đề xuất biến kế: bỏ BANS (chi tiết trong `doc-v1-ch03.md`).

Agent đọc v2: bỏ BANS đổi phần bề mặt (so sánh, phủ định về gần gốc; nhãn điềm tĩnh 5/2 → 0/1) nhưng **không trả
lại tiếng lòng MC** (mất 4/5 sự việc; ！+？ lời kể 0,18 → 0,48 /1.000, gốc 5,31 — I-0049 `vo-hieu`, 0,83 biên độ),
và tệ hơn ở độ dài (+48%), 字/câu (34,1/39,4), giảng huấn (1,91/1,66, vượt khoảng). Chờ Tác giả: trả BANS về (luật 4
của sổ) hay giữ v2; Agent khuyến nghị về v1 rồi thử đổi anchor mục 1 (chi tiết trong `doc-v2-ch03.md`).

Agent đọc v3 (ba biến so với v1, mỗi biến hai chat): **không biến nào trả lại giọng riêng**. Tiếng lòng MC vẫn mất
4/5 chỗ ở cả sáu bản (C-a 5/5); nhân viên tiệm 疾风 không có tiếng lòng ở cả sáu, kể cả khi thẻ dặn; ！+？ lời kể
0,26–0,86 /1.000 (gốc 5,31) — I-0050 (Low) 0,28×, I-0051 (thẻ) 0,75×, I-0052 (anchor) 0,71×, đều `vo-hieu`. Xếp
B ≥ A > C: thẻ chỉ chuyển được từ khoá (靠 ở cả hai câu cuối), anchor ch16 làm đoạn dài ra (C-a 91 字/đoạn). Chỗ
duy nhất có giọng là chỗ brief ghi "một câu trong đầu" / "tự hỏi" → đề xuất biến kế ở tầng BRIEF: ghi các khoảnh
khắc của MC thành "một câu trong đầu cậu" thay vì "cậu tính ra" (chi tiết trong `v3/doc-v3-ch03.md`).

Agent đọc v4 (ba bản SI sửa người kể, mỗi bản hai chat; Tác giả bác cả ba): **0 câu ngôi một (我) trong lời kể** ở cả
sáu bản; tiếng lòng MC chỉ ra ở câu cuối (N-b, EN-a/b: 合着…) và từ 颜控; ！+？ lời kể TB E 0 · N 0,44 · EN 0,41 (gốc
5,31) — I-0053 0,5×, I-0054 0,72×, I-0055 0,64×, đều `vo-hieu`. Ví dụ ch2 trong SI bị bỏ qua (0 chữ rò, 0 giọng); E
giữ BANS nên thinking soát phủ định/so sánh 69/60 lần, N/EN bớt còn 18/26 · 6/2. Xếp EN ≥ N > E. SI dán vẫn v1; sửa
chuyển sang tầng prompt ở v5 (chi tiết trong `v4/doc-v4-ch03.md`).

Agent đọc v5 (sửa ở prompt, SI v1): **P3 (đánh dấu dịp nội tâm) là bản đầu tiên trả lại tiếng lòng MC** — giữ 4/5 và
3/5 chỗ của gốc (v1–v4 và P1/P2: 0–2), P3-b năm câu trong đầu ("合着在这儿等着我呢" · "靠，真就一个极品天赋都没有？"), P3-a
lần đầu có tiếng lòng nhân viên 疾风. Nhưng Writer đặt chúng trong ngoặc “” + thẻ 洛羽在心底暗骂, gốc viết trần trong lời kể,
nên chỉ số sổ (！+？ lời kể) không thấy: I-0056 P1 0,42×, I-0057 P2 0,11×, I-0058 P3 0,69×, đều `vo-hieu`. P1 không đổi
giọng (trừ câu cuối P1-b), P2 tệ nhất (0/5; ví dụ lại bị bỏ qua). Xếp P3 > P1 > P2. Biến kế gợi ý: giữ P3, thêm dòng
"câu trong đầu viết thẳng vào lời kể, không ngoặc kép, không thẻ" (chi tiết trong `v5/doc-v5-ch03.md`).

Agent đọc v6 (đề xuất Argon Gemini + hai đối chứng): **SI Argon là bản SI đầu tiên làm lời kể nói bằng giọng MC** —
！+？ lời kể X 2,33/3,13 · S 2,02/3,27 (gốc 5,31; mọi bản trước ≤ 0,56), tiếng lòng trần ngoài ngoặc, có 店员：？？？; B
(SI v1 + brief Argon) 0,28/0,33, tiếng lòng lại vào ngoặc. I-0059 X 3,19× `hieu-qua`, I-0060 S 1,98× `chua-ro`, I-0061 B
0,36× `vo-hieu`. Bảy chỗ kiểm Argon: X-a 7/7, X-b 6+1~, S 2–1, B 2. Lưu ý: brief Argon có bản Việt 8/8 câu đùa của gốc,
X-a dịch ngược ra 7/8 (ba câu gần nguyên văn) — phần đùa đúng gốc phần lớn là dịch từ brief; S (brief gốc) tự đặt câu
đùa riêng. Giá: X dài +67/+92% (chi tiết trong `v6/doc-v6-ch03.md`).

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
