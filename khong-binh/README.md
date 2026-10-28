# 空瓶督政官 (tên tạm)

**Logline:** Con trai thứ ba của một gia tộc pháp sư sinh ra với ma lực bằng không, bị đày làm 督政官 thuộc địa phàm nhân nghèo nhất đế quốc, có 120 ngày để nộp đủ 12.000 袋 cống lương — và mang theo cả nền công nghiệp của một thế giới khác, thứ mắt pháp sư không nhìn thấy.

Bộ mẫu: [`../de-quoc/`](../de-quoc/) 《我的帝国》 (龙灵骑士), đo ch1–150. Tiền đề đã chốt: [`archive/phuong-an-tien-de.md`](archive/phuong-an-tien-de.md).

## Writer

- SI đang dùng (lần 2, từ đoạn 001 bản 2): `gemini/si-dan-gemini-v1.3.txt` = E1 (luật thoại M3 có ví dụ xưng hô + trợ từ trong ngoặc) bỏ anchor A3, danh sách trợ từ mở rộng: 呢, 么, 吧, 啊, 嘛, 呀, 哦, 啦, 罢了, 而已, 不成, 来着, 着呢 (Tác giả 28/10). Đoạn 001 bản 1, 002, 003 viết bằng v1.2 (= v1.1 bỏ A3).
- Lần 1, từ đoạn 016: `gemini/si-dan-gemini-v1.1.txt` = E1 bỏ ví dụ trong luật thoại M3 (Tác giả 28/10, vì Writer chép danh sách trợ từ 呢/啊 vào mọi câu). Đoạn 001–015 viết bằng `gemini/test/vong-si-3/si-E1.txt` (= v1 + luật thoại M3 mới; hồ sơ đo: `gemini/system-instruction-v1.md`, anchor `gemini/anchors.json`). Chạy qua `tools/aistudio_run.py`.
- Cách viết prompt: `plot/cach-bay-mau.md` (kể việc chở thông tin, theo cách bộ mẫu bày chương).
- Lỗi riêng để soát: `gemini/review-blacklist.md` (+ `../chung/review-blacklist.md`).

## Trạng thái

Lần 2 (viết lại từ đầu, 28/10). Bản lần 1 (đoạn 001–019) ở `archive/lan-1/`.

| Đoạn | Prompt | Bản thảo | Review | Chốt |
|---|---|---|---|---|
| 001 | ✅ | ✅ | ✅ ĐẠT | ✅ |
| 002 | ✅ | ✅ | ✅ ĐẠT | ✅ |
| 003 | ✅ | ✅ | ✅ ĐẠT | ✅ |
| 004 | ✅ | ✅ | ✅ ĐẠT | ✅ |
| 005 | ✅ | ✅ | ✅ ĐẠT | ✅ |
| 006 | ✅ | ✅ | ✅ ĐẠT | ✅ |
