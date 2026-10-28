# <Tên truyện> (tên tạm)

> Khung chép từ `_mau-truyen/`. Luật chung: `../AGENT.md`. Xoá khối hướng dẫn này khi đã điền xong.
>
> **Việc phải làm khi mở truyện mới (AGENT.md mục 11):**
> 0. Đọc [sổ kinh nghiệm chung](../chung/kinh-nghiem.md) và [cách đồng bộ branch](../chung/dong-bo-kinh-nghiem.md); chọn bài học phù hợp với truyện mới.
> 1. (Nên làm) Mổ xẻ 1–2 truyện top cùng thể loại theo [`../chung/mo-xe-truyen.md`](../chung/mo-xe-truyen.md). Rồi điền `bible/` theo thứ tự overview (có hợp đồng độc giả, quỹ kết cục — [`../chung/xay-dung-truyen.md`](../chung/xay-dung-truyen.md)) → glossary → characters (mẫu `bible/characters/_mau-nhan-vat.md`) → world → `plot/arcs.md` (neo arc) → `plot/outline.md`.
> 2. SI: chép `../writer/SI-template` thành `gemini/system-instruction.md`, điền mọi ô `[[...]]` theo hướng dẫn ở cuối file mẫu, xoá phần hướng dẫn và mọi `[[...]]` trước khi dán vào Gemini (`grep "\[\[" gemini/system-instruction.md` phải ra rỗng). SI do Tác giả duyệt.
> 3. `handoff/quiz.md`: 3 câu kiểm tra hợp với truyện (ai, bí mật gì, con số gì).
> 4. Thêm truyện vào bảng ở `../README.md`.

**Logline:** …

## Writer

- SI đang dùng: `gemini/system-instruction.md` (điền từ `../writer/SI-template`) — bản lưu trên AI Studio tên `<Tên truyện> - SI`.
- Lỗi riêng để soát: `gemini/review-blacklist.md` (+ `../chung/review-blacklist.md`).

## Trạng thái

| Đoạn | Prompt | Bản thảo | Review | Chốt |
|---|---|---|---|---|
