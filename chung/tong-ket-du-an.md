# Tổng kết toàn diện dự án Novel

> **Thời điểm tổng kết:** 07/11/2026  
> **Kho lưu trữ:** `HaiPhongDao/Novel`  
> **Branch mặc định hiện tại:** `ccr-d59235d4-pqh9t3`  
> **Cơ chế vận hành:** Claude Agent (giữ canon, brief, dàn ý, review) + Gemini Writer (sinh chính văn tiếng Trung theo đoạn ~2000 chữ) + Tác giả phê duyệt.

---

## 1. Bảng kiểm kê tiến độ 28 bộ truyện / dự án

Dưới đây là thống kê chi tiết toàn bộ các bộ truyện và phân hệ nội dung trên toàn bộ các branch của repository:

| STT | Thư mục | Tên truyện / Phân hệ | Vị trí branch mới nhất | Tiến độ chốt | Số file | Tình trạng & Ghi chú |
|:---:|---|---|---|:---:|:---:|---|
| 1 | `lanh-chua-chip` | **Lãnh Chúa Mang Chip** | `ccr-d59235d4-pqh9t3` | **Đoạn 001–015** | 179 | Lượt 2 hoàn chỉnh; bộ truyện kỳ cựu đã có hệ thống canon & brief chuẩn |
| 2 | `ky-si` | **Kỵ Sĩ** | `ky-si` | **Đoạn 001–026** | 285 | Bộ truyện dài nhất về số đoạn; lưu giữ toàn bộ dữ liệu review và writer |
| 3 | `lam-game` | **Làm Game** | `lam-game` | **Đoạn 001–010** | 107 | Bản 2 bắt đầu tay không; có đầy đủ chuỗi brief và bài test API |
| 4 | `khong-binh` | **Không Binh** | `de-quoc-1` | **Đoạn 001–009** | 218 | Vận hành với SI v1.4, chốt đoạn 009; tích hợp hệ thống State JSON |
| 5 | `Mo-phong` | **Mô Phỏng Nhân Sinh** | `mo-phong` | **Đoạn 001–007** | 68 | Chốt đoạn 007 ("Một hồ rượu đổi câu hỏi về Hạm Thạch Pháp") |
| 6 | `manga-tokyo-1998` | **Manga Tokyo 1998** | `ccr-d59235d4-pqh9t3` | **Đoạn 001–006** | 69 | Hoàn tất hợp đồng 004–006, test thành công bộ mẫu Sanseido |
| 7 | `lanh-chua-dau-truong` | **Lãnh Chúa Đấu Trường** | `ccr-d59235d4-pqh9t3` | **Đoạn 001–003** | 43 | Chốt trọn vẹn Hoàng Kim Tam Chương (001–003), SI v5 7.887 ký tự |
| 8 | `lanh-chua-tien-don` | **Lãnh Chúa Tiền Đồn** | `ccr-d59235d4-pqh9t3` | **Đoạn 001–003** | 40 | Mở truyện từ đầu, dùng SI v5, chốt trọn vòng 3 đoạn đầu |
| 9 | `manga-tokyo-1994` | **Manga Tokyo 1994** | `ccr-d59235d4-pqh9t3` | **Đoạn 001–003** | 61 | Chốt trọn vẹn Hoàng Kim Tam Chương (001–003), SI v5 7.974 ký tự |
| 10 | `manga-tokyo-2000` | **Manga Tokyo 2000** | `ccr-d59235d4-pqh9t3` & `manga` | **Đoạn 001–003** | 75 | Default có 001–003 chốt; nhánh `manga` có thêm bản nháp test tự do 2 |
| 11 | `sung-thu` | **《弃宠收容站》 Trạm Thu Dung Thú Bỏ** | `ccr-d59235d4-pqh9t3` | **Đoạn 001–002** | 172 | Hiệu chuẩn SI Argon v3 ĐẠT; thử nghiệm brief zh/en; chốt đoạn 001-002 |
| 12 | `tiem-sung-thu` | **《深海饲育屋》 Tiệm Bồi Dục Biển Sâu** | `ccr-d59235d4-pqh9t3` | **Đoạn 001–002** | 48 | Chung SI Argon v3; hoàn thành Arc 1, brief 001, chốt đoạn 001-002 |
| 13 | `soi-xam` | **Sói Xám** | `soi-xam` | **Đoạn 001** | 60 | Đổi cốt truyện: MC xuyên việt + phân thân điên; bible mới, SI v4 |
| 14 | `manga-tokyo-1996` | **Manga Tokyo 1996** | `manga-v6` | **Đoạn 001 c** | 45 | Tái cấu trúc theo Hướng 1 (nghề vẽ manga), hoàn thành đoạn 001 bản c |
| 15 | `goblin` | **Bộ Lạc Goblin** | `ccr-d59235d4-pqh9t3` | **Đoạn 016** | 99 | Nhánh phát triển thử nghiệm AI Studio ban đầu; lưu trữ đoạn 001–016 |
| 16 | `quet-kinh-cac` | **Quét Kinh Các** | `quet-kinh-cac` | **Đoạn 001** | 27 | Chạy thử nghiệm qua `aistudio_run.py` + review vòng đầu |
| 17 | `ky-kham-lanh-chua` | **Kỳ Khảm Lãnh Chúa** | `test-gemini-lanh-chua` | **Đoạn 005** | 14 | Nhánh thử nghiệm hiệu chuẩn Gemini; có bản SI v13 đề xuất |
| 18 | `lanh-chua-khoa-hoc` | **Lãnh Chúa Khoa Học** | `vong-du` / `ccr-d2085077` | Đoạn 001–002 | 141 | Lưu giữ trên nhánh cũ `vong-du` |
| 19 | `nong-trang-ma-phap` | **Nông Trang Ma Pháp** | `vong-du` / `ccr-d2085077` | Đoạn 001–002 | 65 | Lưu giữ trên nhánh cũ `vong-du` |
| 20 | `chuyen-chuc` | **Chuyển Chức** | `vong-du` / `de-quoc` | Đoạn 001–002 | 136 | Lưu giữ trên nhánh cũ `vong-du` |
| 21 | `ky-kham-dan-thuong` | **Kỳ Khảm Dân Thường** | `vong-du` / `ccr-d2085077` | Khởi tạo | 84 | Dàn ý, bible và công cụ nối đuôi đoạn |
| 22 | `toan-dan-pho-ban` | **Toàn Dân Phó Bản** | `vong-du` / `ccr-d2085077` | Khởi tạo | 36 | Luật Phó Bản, SI v2, chương 1 bản B |
| 23 | `tram-cuoi` | **Trạm Cuối** | `vong-du` / `ccr-d2085077` | Khởi tạo | 30 | Tận thế - căn cứ, bible, Hoàng Kim Tam Chương, SI v1 |
| 24 | `vong-du` | **Võng Du** | `vong-du` / `de-quoc` | Khởi tạo | 2 | Thư mục nền tảng nhánh Võng Du |
| 25 | `de-quoc` | **Đế Quốc** | `de-quoc-1` | Tài liệu mẫu | 2 | File truyện mẫu 《我的帝国》 |
| 26 | `vo-dich` | **Vô Địch** | `vong-du` / `ccr-d2085077` | Khởi tạo | 2 | Thư mục khởi tạo truyện mẫu |
| 27 | `manga-osaka-1999` | **Manga Osaka 1999** | `ccr-d59235d4-pqh9t3` | Thử nghiệm 001 | 173 | Tạm dừng do Tác giả chê brief, giữ lại làm tư liệu phân tích |
| 28 | `bao-thuc-android` | **App Báo Thức Android** | `ccr-c7a945af-p2nhgt` | Hoàn thành APK | 8 | Dự án phụ hỗ trợ Tác giả canh giờ chạy Writer |

---

## 2. Bảng phân loại và đối chiếu 29 Branch trên GitHub

| Nhóm Branch | Tên Branch | Ahead / Behind so với Default | Trạng thái nội dung | Khuyến nghị hành động |
|---|---|:---:|---|---|
| **Branch Default** | `ccr-d59235d4-pqh9t3` | **0 / 0** | Giữ tài liệu dùng chung, công cụ và các truyện vận hành chính | **Giữ làm nhánh default** (hoặc đổi tên thành `main`) |
| **Nhánh truyện độc lập** | `ky-si` | +54 / -182 | Chứa `ky-si` đoạn 001–026 | Giữ nguyên hoặc gộp thư mục `ky-si/` về default |
| | `lam-game` | +88 / -179 | Chứa `lam-game` đoạn 001–010 (107 files) | Giữ nguyên hoặc gộp thư mục `lam-game/` về default |
| | `de-quoc-1` | +72 / -169 | Chứa `khong-binh` đoạn 001–009 (218 files) | Giữ nguyên hoặc gộp thư mục `khong-binh/` về default |
| | `soi-xam` | +11 / -170 | Chứa `soi-xam` phiên bản mới (60 files) | Giữ nguyên hoặc gộp thư mục `soi-xam/` về default |
| | `manga` | +22 / -165 | Chứa bản nháp Tokyo 2000 & `tasks/` | Giữ nguyên làm nhánh nháp manga |
| | `manga-v6` | +10 / -122 | Chứa `manga-tokyo-1996` đoạn 001 c | Giữ nguyên hoặc gộp `manga-tokyo-1996/` về default |
| | `mo-phong` | +20 / -182 | Chứa `Mo-phong` đoạn 001–007 (68 files) | Giữ nguyên hoặc gộp `Mo-phong/` về default |
| | `quet-kinh-cac` | +22 / -182 | Chứa `quet-kinh-cac` test 001 | Giữ nguyên |
| | `vong-du` | +223 / -179 | Nhánh kho lưu trữ 9 truyện cũ | Giữ làm nhánh archive nội dung cũ |
| | `test-gemini-lanh-chua` | +228 / -179 | Chứa Kỳ khảm lãnh chúa đoạn 005 | Giữ làm tư liệu thử nghiệm |
| | `test-gemini-moi` | +229 / -179 | Chứa đề xuất SI v13 Kỳ khảm | Giữ làm tư liệu thử nghiệm |
| | `ccr-c7a945af-p2nhgt` | +14 / -179 | Chứa `bao-thuc-android` + workflow CI | Giữ làm nhánh công cụ di động riêng |
| **Nhánh thử nghiệm đã tích hợp** | `manga-v7` | **+0** / -108 | Đã tích hợp đầy đủ vào default | **Có thể xoá an toàn** |
| | `thu-v5-manga-tokyo-1998` | **+0** / -126 | Đã tích hợp đầy đủ vào default | **Có thể xoá an toàn** |
| **Nhánh phiên tạm / bản sao cũ** | `ccr-2764b3e9-jenlb1` | +20 / -182 | Cùng SHA với `mo-phong` | Có thể xoá (đã có branch `mo-phong`) |
| | `ccr-50ce3fcb-ewd9hm` | +12 / -182 | Bản sao của `mo-phong` | Có thể xoá |
| | `ccr-1e58ca50-qbknn3` | +3 / -181 | Cùng SHA với `tai-lieu-chung` | Có thể xoá (đã gom về default) |
| | `tai-lieu-chung` | +3 / -181 | Tài liệu chung cũ ngày 23/10 | Có thể xoá (đã gom về default) |
| | `claude/blissful-mayer-n29fgq` | +2 / -181 | Cùng SHA với `lanh-chua-chip` (001–010) | Có thể xoá (default đã có đoạn 015) |
| | `lanh-chua-chip` | +2 / -181 | Bản cũ đoạn 001–010 | Có thể xoá (default đã có đoạn 015) |
| | `ccr-06ebc233-7uywq9` | +60 / -179 | Nháp prompt đoạn 002 `lam-game` | Có thể xoá (nằm trong `lam-game`) |
| | `ccr-984caee6-w5xqdg` | +69 / -179 | Update đoạn 005 `lam-game` | Có thể xoá (nằm trong `lam-game`) |
| | `ccr-c1f4a1ad-f0r3vj` | +11 / -179 | Mở session S3 `lam-game` | Có thể xoá (nằm trong `lam-game`) |
| | `ccr-af860613-ltvtlq` | +9 / -179 | Thử nghiệm secret proxy `gemini_write` | Có thể xoá (tool đã gom về default) |
| | `ccr-c601460e-xuvt03` | +12 / -179 | Nghiên cứu Outliner | Có thể xoá (`nghien-cuu-outliner.md` đã có) |
| | `ccr-d2085077-uo0a5j` | +207 / -179 | Sửa dòng extension | Có thể xoá (tool đã gom về default) |
| | `de-quoc` | +222 / -179 | Tổ tiên nhánh `vong-du` | Có thể xoá (đã có nhánh `vong-du`) |
| | `soat-brief` | +230 / -179 | Nhánh thử nghiệm công cụ soát brief | Có thể xoá (tool đã gom về default) |

---

## 3. Hệ thống Công cụ & Kỹ năng trên Branch Default

Branch default hiện sở hữu toàn bộ hệ sinh thái công cụ hoàn thiện nhất từ trước đến nay:

1. **Bộ kỹ năng tác vụ (`.claude/skills/novel-craft/`):**
   - Phiên bản hiện hành: **v3.1.0** (áp dụng mô hình một pipeline, quy chuẩn anchor thoại/kể, nguyên tắc SI không nhồi số nhịp).
   - Đầy đủ hệ thống tham chiếu: `brief-chi-tiet.md`, `chay-writer.md`, `do-va-hoc.md`, `giong-mc-hien-dai.md`, `si-anchors.md`, `si-cau-truc.md`, `si-test-tren-mau.md`, `soat-loi.md`, `state-extractor.md`.
2. **Bộ công cụ tự động hóa (`tools/`):**
   - `gop_y.py`: Tự động nhận diện phiếu góp ý nghe từ app DocTTS và định vị chính xác file:dòng trong repo.
   - `soat_brief.py`: Cổng soát tự động brief trước khi giao Writer (hỗ trợ mẫu A, mẫu B, kiểm tra cấm kết quả).
   - `build_pack.py` & `chot_doan.py`: Tự động đóng gói ngữ cảnh mở session và đóng dấu nghiệm thu đoạn văn bản.
   - `aistudio_run.py` & extension Chrome/Edge: Tự động chạy hàng loạt trên Google AI Studio, luân phiên tài khoản khi hết quota.
   - `gemini_write.py`: Writer tự động kết nối trực tiếp qua Gemini API.
   - `viet_doan.sh`, `cong_doan.py`, `soat_van.py`, `soat_tat.py`, `cham_doan.py`, `noi_doan.py`, `ra_soat.py`: Hệ thống cổng chấm điểm, đếm tật văn, kiểm tra blacklist và nối mạch câu.
3. **Mẫu SI dùng chung (`writer/SI-template`):**
   - Đã chốt loại bỏ khối LENGTH cứng nhắc, tập trung vào cấu trúc nhịp tự nhiên của bộ mẫu và anchor đặc thù nhân vật.

---

## 4. Đề xuất lộ trình tiếp theo cho Tác giả

Tùy theo nhu cầu quản trị repo của Tác giả, có 3 bước chuẩn hóa có thể thực hiện:

### Bước 1: Gộp các thư mục truyện độc lập về branch default (Khuyên dùng)
- Thay vì gộp cả branch (dễ gây xung đột do khác biệt lịch sử commit cũ), sử dụng lệnh checkout an toàn từng thư mục truyện:
  ```powershell
  # Đứng tại branch default:
  git checkout origin/ky-si -- ky-si
  git checkout origin/lam-game -- lam-game
  git checkout origin/de-quoc-1 -- khong-binh
  git checkout origin/soi-xam -- soi-xam
  git checkout origin/mo-phong -- Mo-phong
  git checkout origin/manga-v6 -- manga-tokyo-1996
  git checkout origin/quet-kinh-cac -- quet-kinh-cac
  git checkout origin/vong-du -- chuyen-chuc lanh-chua-khoa-hoc nong-trang-ma-phap ky-kham-dan-thuong toan-dan-pho-ban tram-cuoi
  ```
- **Lợi ích:** Tất cả 28 truyện sẽ tập trung đầy đủ trên 1 branch duy nhất; không bị mất bất kỳ file truyện nào, và tuyệt đối không làm ảnh hưởng đến bộ công cụ/skill dùng chung trên default branch.

### Bước 2: Đổi tên branch mặc định từ `ccr-d59235d4-pqh9t3` thành `main`
- Hiện branch default đang mang tên phiên làm việc cũ (`ccr-d59235d4-pqh9t3`).
- Có thể tạo nhánh `main` từ default hiện tại, đẩy lên GitHub và thiết lập làm default branch:
  ```powershell
  git checkout -b main
  git push -u origin main
  gh repo edit --default-branch main
  ```

### Bước 3: Dọn dẹp các nhánh phiên làm việc `ccr-*` tạm
- Sau khi Tác giả duyệt, có thể tiến hành xoá các nhánh phiên tạm đã liệt kê ở Mục 2 trên GitHub để repo gọn gàng, chỉ giữ lại các nhánh tính năng hoặc nhánh lưu trữ cần thiết.
