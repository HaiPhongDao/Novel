# Vấn đề cần giải quyết: Writer không kể bằng giọng nhân vật

## Bối cảnh

Dự án viết truyện mạng tiếng Trung. Repo công khai: https://github.com/HaiPhongDao/Novel (nhánh `ccr-d59235d4-pqh9t3`).

Ba vai:
- **Tác giả**: người quyết định; người duy nhất chấm đạt / không đạt, bằng cách đọc.
- **Agent** (Claude): viết System Instruction (SI), viết brief, chạy Writer, báo cáo.
- **Writer**: Gemini 3.8 Flash trên Google AI Studio, thinking High. Mỗi lần viết là một chat mới gồm SI (tiếng Anh) và
  một tin nhắn người dùng là brief (tiếng Việt). Writer trả về văn tiếng Trung.

Truyện mới `sung-thu` dùng bộ mẫu 《神宠供应商》 (轻泉流响). Trước khi dựng truyện, dự án kiểm SI như sau: lấy một chương
của bộ mẫu (chương 3, 2.822 字), viết một brief tiếng Việt chỉ có sự việc của chương đó, cho Writer viết lại, rồi Tác
giả đọc bản của Writer cạnh nguyên văn.

## Vấn đề — lời Tác giả

- "Đang không hề có chất giọng riêng của MC/ nhân vật."
- "Giọng kể Narrator đang như người thứ 3 tác giả đứng ngoài, không hề kể bằng giọng của nhân vật."

Cùng một sự việc, nguyên văn chương 3 và bản Writer (SI v1, bản a):

| Sự việc | Nguyên văn chương 3 | Bản Writer |
|---|---|---|
| Nhân viên mời chương trình tặng sâu miễn phí kèm hợp đồng bán tơ | 洛羽一琢磨……骗小孩呢？！ | 大量吐丝对于幼虫而言是极重的消耗，频繁透支体力注定会导致躯干发育迟滞。 |
| Hỏi tiệm có mỗi mấy nghìn con thôi à | 店员：？？？ / 几千条还他妈不够你挑？！ / 来挑事的吧！ | 店员捧着肉虫的五指一颤，面皮不由自主地抽搐了一下。 |
| Nhân viên tiệm 冷雾蜥 nói lũ thằn lằn đang luyện dị năng | 洛羽旁边的店员一本正经道。 / “？？？” / 我信你个鬼。 | 洛羽听着这番说辞，心底迅速闪过岛上的真实态势。 |

## Việc cần giải quyết

1. Tìm nguyên nhân Writer kể bằng giọng người đứng ngoài thay vì giọng của nhân vật.
2. Đưa ra cách sửa dùng được ngay: SI và/hoặc khuôn brief, viết **toàn văn**, để Writer kể bằng giọng nhân vật như bộ
   mẫu.
3. Nêu cách kiểm: chạy trên brief chương 3 thì đọc những chỗ nào để biết đã sửa được.

## Ràng buộc Tác giả đã chốt

- Không đưa con số nhịp / độ dài câu / độ dài đoạn vào SI (01/11).
- Không bắt brief của mỗi đoạn phải viết từng động tác, từng câu thoại của nhân vật (03/11).
- Writer vẫn là Gemini trên AI Studio: mỗi lần viết = SI + một tin nhắn, chat mới; gửi tiếp vào chat cũ không dùng được.
- Brief viết tiếng Việt; văn ra tiếng Trung.
- Câu đạt / không đạt chỉ do Tác giả.

## Đã thử — chỉ liệt kê, không kết luận

Mọi lần đều trên brief chương 3, mỗi cấu hình chạy 2 lần, chat mới.

| Lần | Đổi gì | File | Tác giả |
|---|---|---|---|
| v1 | SI khung gọn: FIXED + mục 1 (nhân vật) + mục 3 (thoại) + BANS + PART 3 + PART 4 (bảng 【种族】), 3 anchor nguyên văn bộ mẫu | `sung-thu/gemini/system-instruction-v1.md` | "Đang không hề có chất giọng riêng của MC/ nhân vật" (đọc v1 + v2) |
| v2 | v1 bỏ khối BANS | `sung-thu/gemini/system-instruction-v2.md` | như trên |
| v3 A | v1, thinking Low | `sung-thu/gemini/test-giong/v3/` | "Khó quá hãy thử cách đưa brief mẫu + kết quả mẫu cho Writer vào SI" |
| v3 B | v1, brief thêm thẻ giọng cho từng nhân vật | `v3/brief-B.md` | như trên |
| v3 C | v1, đổi anchor mục 1 sang chương 16 | `v3/si-C.txt` | như trên |
| v4 E | v1 + khối ví dụ trong SI: brief mẫu chương 2 + nguyên văn chương 2 | `sung-thu/gemini/test-giong/v4/si-E.txt` | "Đều không đạt" |
| v4 N | v1, thêm mục "lời kể là cái đầu của nhân vật chính", sửa một câu mục 1, sửa BANS dòng 2 | `v4/si-N.txt` | như trên |
| v4 EN | E + N | `v4/si-EN.txt` | như trên |
| v5 P1 | SI v1; brief theo khuôn "viết tiếp" + đuôi chương 2 nguyên văn ở đầu | `sung-thu/gemini/test-giong/v5/brief-P1.md` | chưa đọc |
| v5 P2 | P1 + ví dụ brief mẫu → nguyên văn chương 2 đặt trong brief | `v5/brief-P2.md` | chưa đọc |
| v5 P3 | P2 + bảy chỗ trong brief ghi "trong đầu cậu bật ra một câu, bằng giọng cậu" | `v5/brief-P3.md` | chưa đọc |

Bản Writer của mỗi lần nằm cạnh file cấu hình (`*-a.md`, `*-b.md`).

## Tài liệu

Gốc link: `https://github.com/HaiPhongDao/Novel/blob/ccr-d59235d4-pqh9t3/` + đường dẫn.

- SI v1 đang dán vào AI Studio: `sung-thu/gemini/si-dan-gemini.txt`
- SI v1 bản nguồn có ghi chú: `sung-thu/gemini/system-instruction-v1.md`
- Brief chương 3: `chung/hieu-chuan/than-sung/ch03/brief.md`
- Nguyên văn chương 3: `chung/hieu-chuan/than-sung/ch03/goc.txt` · chương 2: `chung/hieu-chuan/than-sung/ch02/goc.txt`
- Bản Writer v1: `sung-thu/gemini/test-giong/v1-ch03-a.md`, `sung-thu/gemini/test-giong/v1-ch03-b.md`
- Khung SI chung của dự án: `writer/SI-template`
- Toàn văn bộ mẫu (140 chương) không có trên repo — cần thì Tác giả đính kèm file `神宠供应商(1-140章).txt`.

## Định dạng trả lời

1. Nguyên nhân — mỗi ý một đoạn ngắn, chỉ ra dòng hoặc chữ cụ thể trong SI / brief / cách chạy.
2. SI đề xuất — toàn văn, dán thẳng được vào AI Studio.
3. Khuôn brief đề xuất (nếu đổi brief) — toàn văn, áp cho chương 3.
4. Cách kiểm trên chương 3.
