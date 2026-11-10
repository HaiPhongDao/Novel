# chung/taste — hồ sơ phán xét của Tác giả và phép thử giám khảo

Skill dùng hồ sơ này: [`.claude/skills/novel-taste/SKILL.md`](../../.claude/skills/novel-taste/SKILL.md).

| File | Là gì |
|---|---|
| `ho-so.jsonl` | 115 phán xét của Tác giả 22/10–10/11 (56 chê · 29 chỉ đạo · 14 khen · 9 chọn · 7 bác), gom từ mọi nhánh |
| `cap.jsonl` | 32 lần Tác giả chuộng bản này hơn bản kia; đường dẫn bản văn đã kiểm tồn tại; `do_tin` cao / vừa / thấp |
| `cau.jsonl` | 27 câu, cụm tiếng Trung Tác giả đích thân chỉ ra |
| `cham-mu-2026-11-10.json` | Khoá và kết quả thô của phép thử dưới đây |

## Phép thử 10/11: giám khảo có trùng lựa chọn cũ của Tác giả không

21 ca rút từ 16 cặp (độ tin cao và vừa). Mỗi ca hai bản văn, xoá tên file và ghi chú, xáo A/B. Hai nhóm giám khảo cùng
model (Claude Sonnet), mỗi nhóm ba agent: một nhóm đọc skill `novel-taste`, một nhóm chỉ được bảo "chọn văn truyện mạng
tốt hơn".

| Ca | Cặp | Đáp án (Tác giả) | Có skill | Không skill |
|---|---|---|---|---|
| ca-01 | P01 | A | A ✓ (tin 3) | A ✓ (tin 2) |
| ca-02 | P06 | A | A ✓ (tin 3) | A ✓ (tin 3) |
| ca-03 | P06 | B | B ✓ (tin 2) | B ✓ (tin 2) |
| ca-04 | P09 | B | B ✓ (tin 1) | A ✗ (tin 2) |
| ca-05 | P09 | B | B ✓ (tin 2) | B ✓ (tin 2) |
| ca-06 | P12 | A | A ✓ (tin 1, ngang) | A ✓ (tin 2) |
| ca-07 | P12 | A | A ✓ (tin 2) | A ✓ (tin 2) |
| ca-08 | P14 | A | B ✗ (tin 2) | A ✓ (tin 1, ngang) |
| ca-09 | P17 | A | A ✓ (tin 2) | B ✗ (tin 2) |
| ca-10 | P17 | A | A ✓ (tin 3) | A ✓ (tin 2) |
| ca-11 | P23 | B | B ✓ (tin 2) | A ✗ (tin 1, ngang) |
| ca-12 | P25 | B | A ✗ (tin 2) | A ✗ (tin 3) |
| ca-13 | P25 | B | A ✗ (tin 1, ngang) | A ✗ (tin 2) |
| ca-14 | P28 | A | A ✓ (tin 3) | B ✗ (tin 2) |
| ca-15 | P16 | B | A ✗ (tin 2) | B ✓ (tin 2) |
| ca-16 | P24 | B | B ✓ (tin 3) | B ✓ (tin 3) |
| ca-17 | P15 | B | B ✓ (tin 1, ngang) | B ✓ (tin 1, ngang) |
| ca-18 | P20 | A | B ✗ (tin 2) | B ✗ (tin 2) |
| ca-19 | P11 | B | A ✗ (tin 2) | B ✓ (tin 2) |
| ca-20 | P07 | A | A ✓ (tin 3) | A ✓ (tin 3) |
| ca-21 | P02 | A | B ✗ (tin 1, ngang) | A ✓ (tin 2) |

| | Có skill | Không skill |
|---|---|---|
| Cả 21 ca | 14/21 (67%) | 14/21 (67%) |
| 13 ca từ cặp độ tin **cao** | 11/13 (85%) | 10/13 (77%) |
| 8 ca từ cặp độ tin **vừa** (cặp do suy từ log) | 3/8 | 4/8 |
| Riêng các ca giám khảo tự nhận chắc (tin 3) | 6/6 | 3/4 |

**Đọc kết quả cho đúng:**

- **Skill chưa chứng minh được là hơn một biên tập viên chung chung.** 11 so với 10 trên 13 ca là trong vùng nhiễu.
- Trên các cặp Tác giả so trực tiếp (độ tin cao), giám khảo nào cũng trùng khoảng tám phần mười. Trên các cặp suy từ log thì
  như tung đồng xu — nhiều khả năng do chính nhãn của các cặp đó sai, không dùng chúng làm thước.
- Khi giám khảo có skill tự nhận chắc (tin 3) thì 6/6 trùng. Mẫu nhỏ, nhưng là căn cứ cho luật ở mục 3 của skill: chỉ hành
  động theo lựa chọn có độ tin 3; còn lại coi là ngang.
- Đây là **phép thử trong mẫu**: skill viết từ chính các lời chê này. Thước đo thật là phán xét mới của Tác giả
  (`<truyen>/taste-log.jsonl`, mục 4 của skill).
- Lỗi dữ liệu đã thấy: bản được chuộng ở ca-12 bị cắt cụt giữa câu trong repo; cặp P25 thực ra là lời "L2 vô dụng" (không
  thấy khác) chứ không phải chuộng bản nền; ca-09 và ca-10 dùng chung một bản.
- Chỗ skill chấm lệch có ích: P14 (bản 1.0 phạt Gareth "xả dữ kiện trong thoại" trong khi Tác giả thích chính giọng lính già
  đó) → mục 2.3 đã thu hẹp ở bản 1.1. P16, P11: Tác giả chọn bản thoại đầy hơn dù dài và nhiều trợ từ hơn.

## Cập nhật

- Tác giả nói gì về một bản văn → thêm một dòng vào `ho-so.jsonl` (giữ nguyên lời), và nếu là so hai bản thì thêm vào `cap.jsonl`.
- Sau mỗi 20 dòng `taste-log.jsonl` có trường `tac_gia`: đếm tỷ lệ bản được chọn mà Tác giả cho qua, ghi vào đây. Dưới
  bảy phần mười thì bỏ vòng ba bản, quay về một bản mỗi đoạn.
