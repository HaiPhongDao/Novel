# Giữ nhất quán khi truyện dài

Repo đã có bộ nhớ ba lớp: `bible/` (sự thật lâu dài), `handoff/` (gói bàn giao Writer — [quy-trinh-ban-giao.md](quy-trinh-ban-giao.md)) và review. Tài liệu này bổ sung những gì bắt đầu gãy khi truyện qua vài chục đoạn: biết–không biết, nhân vật và tuyến bị quên, ràng buộc trôi khỏi gói.

Chuyển thể từ oh-story-claudecode (`tracking-transaction`: thẻ trạng thái bảy khối, hai dòng thời gian), novel-writer-skills (`forgotten-elements`, `consistency-checker`) và novel-creator-skill (`foreshadowing_tracker`, `character_tracker`) — xem [tham-khao-ngoai.md](tham-khao-ngoai.md). Tình trạng: **đề xuất, chưa thử trong repo**, trừ `tools/ra_soat.py` đã chạy trên Lãnh Chúa Chip.

## 1. Mỗi sự thật một chỗ ở

| Loại | Ở đâu | Ghi khi nào |
|---|---|---|
| Luật thế giới, thiết lập cố định | `bible/world.md`, `bible/characters/` | khi Tác giả chốt |
| Sự kiện đã lên trang | `bible/timeline.md` | lúc chốt đoạn |
| Lời hứa / cài cắm còn nợ | `plot/threads.md` | lúc chốt đoạn |
| Ảnh chụp hiện tại cho Writer | `handoff/state.md` (ghi đè) | lúc chốt đoạn |
| Kế hoạch tương lai | `plot/arcs.md`, `plot/outline.md` | khi lập kế hoạch |
| Quyết định | `log.md` | ngay khi quyết |

Kế hoạch tương lai **không** ghi vào timeline hay state như chuyện đã xảy ra. "Đoạn X sẽ lộ" thuộc outline; timeline chỉ nhận điều đã lên trang.

## 2. Ba tầng biết

Nhiều lỗi khó thấy nhất là lỗi *biết*: nhân vật biết điều chưa được biết, lời kể xác nhận điều MC mới nghi (KN07), hoặc bí mật lọt vào gói rồi Writer viết ra. Timeline tách ba cột:

| Thời điểm | Sự thật (Tác giả biết) | Độc giả biết tới đâu | Ai trong truyện biết | Đoạn |
|---|---|---|---|---|

- Sự thật chưa lộ: cột "độc giả" ghi *chưa lộ*; chỉ nằm trong bible/timeline cho Agent, **không vào gói bàn giao** (quy tắc sẵn có).
- Lộ một phần: ghi đúng phần đã lộ và đoạn lộ.
- "Ai biết" phân biệt **nghe nói / đoán / đã kiểm chứng** — ba mức khác nhau (KN07).

## 3. Thẻ trạng thái giữ gọn

`handoff/state.md` là thẻ "nóng" — thứ Writer cần để viết đúng đoạn kế. Khối cố định (mẫu ở `_mau-truyen/handoff/state.md`):

1. Thời điểm, địa điểm, ai có mặt, tư thế
2. **Ràng buộc dài hạn** — tối đa 6 dòng, viết khẳng định (vd. "小七 chỉ là giọng nói trong đầu Leon")
3. Nhân vật đang hoạt động — tối đa 6 người, mỗi người: thân phận · ở đâu · đang muốn gì · tình trạng · đang cầm/có gì · biết gì
4. MC biết
5. Con số đang chạy (khung đúng, KN09)
6. Lệnh đang chạy, đồ vật đã xuất hiện
7. Tuyến đang mở — tối đa 8

Giới hạn là sức chứa của *thẻ nóng*, không phải của truyện: ai/tuyến bị đẩy ra khỏi thẻ vẫn nằm đủ trong bible và threads. Muốn thêm ràng buộc thứ 7: gộp hai dòng trùng ý hoặc hỏi Tác giả bỏ dòng nào — không lặng lẽ xoá. Dòng nào rút khỏi thẻ thì ghi một dòng `log.md` ("rút khỏi state: … — lý do"), để còn tra lại.

## 4. Chống quên — ngưỡng và rà soát mỗi 5 đoạn

AGENT.md mục 7 đã yêu cầu rà soát mỗi 5 đoạn. Chạy:

```bash
python tools/ra_soat.py <ten-truyen>            # mặc định: vắng ≥10 đoạn, đứng yên ≥8 đoạn
python tools/ra_soat.py <ten-truyen> --vang 6 --dung 5
```

Công cụ chỉ báo, không sửa gì. Nó quét tên riêng trong `bible/glossary.md` qua chính văn, và cột "Chạm gần nhất" / "Hạn payoff" trong `plot/threads.md`. Với mỗi dòng báo, Agent chọn một trong ba và ghi vào review/threads:

- **Đưa vào kế hoạch** — đoạn nào sẽ chạm lại (một câu nhắc, một lần xuất hiện, một bước tiến).
- **Tạm gác có chủ ý** — đổi trạng thái thành "Tạm gác", ghi đoạn dự kiến quay lại. Công cụ bỏ qua dòng này.
- **Đóng** — đã trả hoặc bỏ; bỏ một cài cắm đã lên trang thì cần Tác giả duyệt.

Ngưỡng gợi ý (đơn vị đoạn ~2000 字): nhân vật quan trọng vắng 10 đoạn; tuyến không tiến 8 đoạn; cài cắm chưa trả 15 đoạn hoặc quá hạn. Truyện nhịp nhanh hạ ngưỡng.

Cùng lúc rà soát, hỏi thêm bốn câu hợp đồng độc giả và hai câu tiêu quá tay ([xay-dung-truyen.md](xay-dung-truyen.md) mục 1, 3).

## 5. threads.md — cột mới

```
| ID | Loại | Tuyến / chi tiết | Cài ở | Chạm gần nhất | Hạn payoff | Độ quan trọng | Trạng thái |
```

- **Loại**: *Cài cắm* (chi tiết sẽ trả) · *Mong chờ* (lời hứa với người đọc — nợ mong chờ) · *Bí ẩn* (câu hỏi dài hạn).
- **Chạm gần nhất / Hạn payoff**: ghi **số đoạn** (`doan-012` hoặc `12`), để công cụ đọc được. Chưa định hạn thì để `—`.
- **Trạng thái**: Kế hoạch (chưa lên trang) · Đã cài · Đang chạy · Tạm gác · Đã trả · Bỏ.
- Cập nhật lúc chốt mỗi đoạn: đoạn nào nhắc tới tuyến thì sửa "Chạm gần nhất"; trả xong thì ghi đoạn trả và cách trả.

threads.md kiểu cũ vẫn chạy được (công cụ đoán số đoạn từ chữ "đoạn N"/"chN"), nhưng báo kém chính xác. Chuyển sang cột mới khi tiện — đó là việc sửa bảng theo dõi, Agent tự làm được và ghi log.

## 6. Soát nhất quán trong review

Bổ sung cho checklist mục 5 AGENT.md — những thứ hay trôi khi truyện dài:

| Nhóm | Soát |
|---|---|
| Thân thể | ngoại hình, thương tích, sức khoẻ — vết thương ở đoạn trước còn không, lành theo thời gian hợp lý không |
| Đồ vật | đang cầm gì, tiêu hao gì; vật đã cho/đốt/vỡ không xuất hiện lại |
| Thời gian | ngày trong truyện, khoảng đường đi, thời gian trôi giữa hai cảnh |
| Hiểu biết | ba tầng biết (mục 2) |
| Giọng thoại | xưng hô, tật nói, cấp độ ngôn ngữ đúng hồ sơ nhân vật; đổi giọng phải có việc gây ra (KN02) |
| Luật thế giới | bàn tay vàng, phép tắc, xã hội — kể cả giới hạn giác quan (nguyên tắc 17) |

Mức: ❌ phải sửa (nhân vật biết điều không được biết, phá luật cứng, sai số) · ⚠️ sửa nhẹ (giọng lệch, thời gian nén) · ghi chú (cần để mắt).

## 7. Hồ sơ nhân vật nên có gì

Mẫu ở `_mau-truyen/bible/characters/_mau-nhan-vat.md`. Ngoài thân phận và tính cách, hai phần hay thiếu khi truyện dài:

- **Giọng**: xưng hô với từng người, tật nói/câu cửa miệng, cấp độ ngôn ngữ, khi giận/khi sợ nói thế nào — viết bằng mô tả, trích câu đã duyệt từ chính văn làm ví dụ.
- **Các giai đoạn**: giọng và quan hệ đổi theo arc (vd. Hob lạnh nhạt → giữ sổ cho Leon). Mỗi giai đoạn ghi đoạn bắt đầu và **việc cụ thể** gây ra thay đổi.
