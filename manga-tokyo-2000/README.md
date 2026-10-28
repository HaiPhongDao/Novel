# 我在千禧东京画漫画 (manga-tokyo-2000)

**Logline:** Tokyo tháng 10/2000. Một người xuyên việt nhập vào cậu nhân viên ca đêm quán truyện tranh, người đã gửi bản thảo bảy lần và còn nợ tín dụng đen. Anh dùng những phân cảnh của tác phẩm đời sau hiện về trong mơ để bước vào giới truyện tranh, cùng một nữ biên tập viên chưa có lấy một tác giả đăng dài kỳ.

- Bộ mẫu: `../我在泡沫东京画漫画.txt` (214 chương, trung vị 2.354 字/chương, thoại ~22%). Tác giả chốt 29/10: giữ tiền đề như mẫu, đẩy năm lên.
- Prompt: **mẫu A + State JSON** (Tác giả chốt 29/10). Thiết lập nằm trong `handoff/state.json`.

## Writer

- SI: `gemini/si-v1.txt` (phần dán), `gemini/si-dan-gemini.txt` (kèm dấu BẮT ĐẦU/HẾT). Dựng từ `../writer/SI-tong-hop.txt`, thay 9 anchor bằng nguyên văn bộ mẫu (`verify_anchors.py` 10/10 khớp), thêm PART 3 cho lane truyện tranh.
- Đoạn 001: `handoff/session-start-001.md` = brief + State JSON.
- Lỗi riêng để soát: `gemini/review-blacklist.md` (+ `../chung/review-blacklist.md`).

## Trạng thái

| Đoạn | Prompt | Bản thảo | Review | Chốt |
|---|---|---|---|---|
| 001 | `briefs/doan-001.md` — chờ Tác giả đọc | — | — | — |
