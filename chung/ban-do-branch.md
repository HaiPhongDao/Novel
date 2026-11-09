# Bản đồ branch

Cập nhật: 10/11/2026.
**Branch mặc định và nhánh làm việc duy nhất: `main`** (từ 10/11; = `han-nien-san-dong` + `co-dai` + `QUY-TRINH.md` + `tools/lam.py`). Mọi việc mới commit thẳng lên `main` — xem [`../QUY-TRINH.md`](../QUY-TRINH.md) mục 6.
Các bảng dưới là ảnh chụp 07/11: chỗ nào ghi "branch mặc định `ccr-d59235d4-pqh9t3`" thì nay là nhánh cũ, nội dung của nó đã nằm trong `main`. `han-nien-san-dong` và `co-dai` cũng đã nằm trong `main`.
Máy Tác giả: push bằng tài khoản HaiPhongDao lưu trong Windows Credential Manager (`D:/Claude/Novel` đã đặt `credential.https://github.com.helper = manager` trong config riêng của repo); `gh` đang đăng nhập DHaiPhong chỉ đọc được.

---

## 1. Branch mặc định: `ccr-d59235d4-pqh9t3`
- **Vai trò:** Trung tâm điều hành repo, chuẩn hóa toàn bộ công cụ tự động hóa, kỹ năng `novel-craft` (v3.1.0), mẫu SI v5/v6, và các truyện đang chạy thử nghiệm / hiệu chuẩn mới nhất.
- **Các truyện hiện có trên branch này:**
  * `sung-thu` (Trạm Thu Dung Thú Bỏ — SI Argon v3 ĐẠT, đoạn 001–002, 172 files)
  * `tiem-sung-thu` (Tiệm Bồi Dục Biển Sâu — khởi tạo Arc 1, brief 001, đoạn 001–002, 48 files)
  * `lanh-chua-chip` (Lãnh Chúa Mang Chip — lượt 2: chốt đoạn 001–015, 179 files)
  * `manga-tokyo-1998` (Manga Tokyo 1998 — chốt đoạn 001–006, 69 files)
  * `lanh-chua-dau-truong` (Lãnh Chúa Đấu Trường — chốt đoạn 001–003, 43 files)
  * `lanh-chua-tien-don` (Lãnh Chúa Tiền Đồn — chốt đoạn 001–003, 40 files)
  * `manga-tokyo-1994` (Manga Tokyo 1994 — chốt đoạn 001–003, 61 files)
  * `manga-tokyo-2000` (Manga Tokyo 2000 — chốt đoạn 001–003, 58 files)
  * `manga-osaka-1999` (Manga Osaka 1999 — 173 files)
  * `goblin` (99 files)
  * `mo-xe` (tài liệu giải phẫu truyện mẫu)
  * `lam-game`, `soi-xam` (bản khung stub, nội dung đầy đủ nằm tại branch riêng)

---

## 2. Branch giữ nội dung truyện độc lập (chưa gộp vào default)

Các branch này chứa văn bản chính thức, dàn ý và tài liệu riêng của từng bộ truyện chưa được đồng bộ hết vào branch default:

| Branch | Bộ truyện chính | Tiến độ & Số file | Ghi chú |
|---|---|---|---|
| `co-dai` | `co-dai` | Khởi tạo nhánh mới (26 files), sẵn sàng khung bible & SI-template v6 | Nhánh truyện cổ đại mới mở từ default |
| `ky-si` | `ky-si` | Đã chốt đến **đoạn 026** (285 files) | Bộ truyện dài nhất về số đoạn; độc lập hoàn toàn |
| `lam-game` | `lam-game` | Đã chốt **đoạn 001–010** (107 files) | Bản 2 bắt đầu tay không; nhiều bản thử nghiệm Writer |
| `de-quoc-1` | `khong-binh`, `de-quoc`, `soi-xam` | `khong-binh` chốt **đoạn 009** (218 files) | Phát triển nhánh riêng với State JSON, brief Tác giả |
| `soi-xam` | `soi-xam` | Đổi mới nội dung: MC xuyên việt + phân thân điên (60 files) | SI v4, brief 001 bản i/j + review vòng 4 |
| `manga` | `manga-tokyo-2000`, `ky-kham-lanh-chua` | 75 files `manga-tokyo-2000` + thư mục `tasks/` | Chứa bản nháp mở rộng, test tự do 2 |
| `manga-v6` | `manga-tokyo-1996` | Đã xong **đoạn 001 c** (45 files) | Hướng 1 (nghề vẽ manga) |
| `mo-phong` | `Mo-phong` | Đã chốt **đoạn 001–007** (68 files) | Cùng SHA `3f1ba78` với `ccr-2764b3e9` |
| `quet-kinh-cac` | `quet-kinh-cac` | Test 001 v0-01 (27 files) | Chạy thử bằng `aistudio_run.py` |
| `vong-du` | `vong-du`, `chuyen-chuc`, `lanh-chua-khoa-hoc`, `nong-trang-ma-phap`, `toan-dan-pho-ban`, `tram-cuoi`, `vo-dich`, `ky-kham-*` | Nhánh lưu trữ tổng hợp 9 truyện cũ (875 files) | Nhánh dài nhất lịch sử trước đợt tách 28/10; toàn bộ tool đã gom về default |
| `test-gemini-lanh-chua` | `ky-kham-lanh-chua` | Hoàn thành đoạn 005 | Nhánh kiểm nghiệm Gemini trên Kỳ khảm |
| `test-gemini-moi` | `ky-kham-lanh-chua` | Đề xuất SI v13 theo SI-template v5 | Thử nghiệm cấu trúc SI |
| `ccr-c7a945af-p2nhgt` | `bao-thuc-android` | App APK báo thức lặp + GitHub Action (8 files) | Dự án công cụ phụ trợ |

---

## 3. Branch thử nghiệm đã tích hợp trọn vẹn (Ahead = 0)

Các branch này không còn commit nào chưa có trên default branch:
- `manga-v7`: Thử nghiệm skill 3.1 pipeline (đã vào default).
- `thu-v5-manga-tokyo-1998`: Cập nhật anchor từ chương 2 & 3 bộ mẫu (đã vào default).

---

## 4. Branch phiên làm việc tự sinh (`ccr-*`) và bản sao cũ

> **Nguyên tắc quản lý:** Các branch `ccr-*` là branch phiên làm việc tự sinh của Claude Code / Agent. Xoá branch là quyền của Tác giả, Agent không tự xoá.

| Branch | Trạng thái tích hợp | Khuyến nghị xử lý |
|---|---|---|
| `claude/blissful-mayer-n29fgq` | Cùng SHA với `lanh-chua-chip` (đoạn 001–010) | Có thể xoá an toàn (default đã có đoạn 015) |
| `ccr-1e58ca50-qbknn3` | Cùng SHA với `tai-lieu-chung` | Có thể xoá an toàn (tài liệu đã gom về default) |
| `ccr-2764b3e9-jenlb1` | Cùng SHA với `mo-phong` | Có thể xoá an toàn (đã có branch `mo-phong`) |
| `ccr-50ce3fcb-ewd9hm` | Bản sao của `ccr-2764b3e9` | Có thể xoá an toàn |
| `ccr-06ebc233-7uywq9` | Bản nháp prompt đoạn 002 `lam-game` | Đã nằm trong `lam-game` |
| `ccr-984caee6-w5xqdg` | Update đoạn 005 `lam-game` | Đã nằm trong `lam-game` |
| `ccr-c1f4a1ad-f0r3vj` | Mở session S3 `lam-game` | Đã nằm trong `lam-game` |
| `ccr-af860613-ltvtlq` | Sửa proxy `gemini_write.py` | Đã gom vào `tools/` trên default |
| `ccr-c601460e-xuvt03` | Nghiên cứu Outliner | Đã gom `chung/nghien-cuu-outliner.md` |
| `ccr-d2085077-uo0a5j` | Bản sửa extension | Đã gom vào extension trên default |
| `soat-brief` | Thử nghiệm công cụ `soat_brief.py` | Đã gom công cụ lên default |
| `de-quoc` | Tổ tiên lùi 1 commit so với `vong-du` | Đã bao trùm bởi `vong-du` và `de-quoc-1` |
