# Bản đồ branch

Cập nhật 2026-10-28. Branch mặc định: `ccr-d59235d4-pqh9t3` — giữ **tài liệu và công cụ dùng chung** (mọi thứ ở gốc repo + `.claude/`), không phải bản mới nhất của từng truyện. Phần chung đã gom về đây ngày 28/10 từ các branch bên dưới; từ nay sửa phần chung thì commit riêng ở đây (xem [`dong-bo-kinh-nghiem.md`](dong-bo-kinh-nghiem.md)).

## Branch giữ nội dung truyện (không xoá)

| Branch | Giữ gì | Ghi chú |
|---|---|---|
| `vong-du` | Nhánh dài nhất: `vong-du`, `chuyen-chuc`, `ky-kham-*`, `lanh-chua-khoa-hoc`, `nong-trang-ma-phap`, `toan-dan-pho-ban`, `tram-cuoi`, `vo-dich`… | Bản skill/tools/extension mới nhất ở đây (commit 28/10) — đã gom sang mặc định |
| `de-quoc` | Như `vong-du` trừ commit extension cuối | Lùi 1 commit so với `vong-du` |
| `de-quoc-1` | `de-quoc`, `khong-binh`, `soi-xam`… + agent `novel-doan`, `viet_doan.sh`, `soat_tat.py`, `state-extractor.md` | Đường phát triển riêng với State JSON; đã gom phần chung sang mặc định |
| `soi-xam` | `soi-xam` (xuyên việt + phân thân điên, SI v4) | Có ba bài học skill — đã gom |
| `lam-game` | `lam-game`, `goblin` | Truyện chưa nằm ở nhánh nào dài hơn |
| `mo-phong` / `ccr-2764b3e9-jenlb1` | `Mo-phong` | Cùng SHA `3f1ba78` |
| `ky-si` | `ky-si` | |
| `quet-kinh-cac` | `quet-kinh-cac` | |
| `lanh-chua-chip` | `lanh-chua-chip` gộp 001–010 | Cùng SHA với `claude/blissful-mayer-n29fgq` |
| `ccr-c7a945af-p2nhgt` | `bao-thuc-android` (APK báo thức) | Dự án phụ |

## Branch chỉ là tổ tiên hoặc bản sao — đã nằm trọn trong branch khác

| Branch | Nằm trong |
|---|---|
| `ccr-d2085077-uo0a5j` | `de-quoc`, `vong-du` |
| `ccr-c1f4a1ad-f0r3vj`, `ccr-eba1eaae-jpkac2`, `ccr-af860613-ltvtlq` | `lam-game`, `de-quoc`, `vong-du` |
| `ccr-06ebc233-7uywq9`, `ccr-984caee6-w5xqdg` | `lam-game` |
| `claude/blissful-mayer-n29fgq` | cùng SHA `lanh-chua-chip` |
| `ccr-1e58ca50-qbknn3` | cùng SHA `tai-lieu-chung` (đã gom `giu-nhat-quan`, `mo-xe-truyen`, `xay-dung-truyen`, `ra_soat.py`, mẫu truyện) |
| `ccr-c601460e-xuvt03` | đã gom `nghien-cuu-outliner.md`; phần còn lại (`gemini_write.py` bản 183 dòng) là bản cũ của bản 213 dòng |
| `ccr-50ce3fcb-ewd9hm` | đã gom (bản sao của `ccr-2764b3e9-jenlb1`) |

Các branch `ccr-*` là branch phiên làm việc tự sinh. Xoá được khi Tác giả đồng ý; **xoá branch là việc của Tác giả**, Agent không tự xoá.
