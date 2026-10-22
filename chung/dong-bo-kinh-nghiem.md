# Đồng bộ kinh nghiệm giữa các branch

## Nơi đọc chung

Nguồn dùng chung là `chung/kinh-nghiem.md`; bảng nguồn ở `chung/nguon-kinh-nghiem.md`. Branch mặc định hiện tại là `ccr-d59235d4-pqh9t3`. Khi làm việc trên branch truyện, có thể đọc bản mới từ branch mặc định mà chưa phải đổi checkout:

```powershell
git fetch origin
git show origin/ccr-d59235d4-pqh9t3:chung/kinh-nghiem.md
```

Git không tự chia sẻ thay đổi giữa các branch. Có cùng tên file không có nghĩa nội dung ở mọi branch luôn giống nhau. Bản tổng hợp cần được cập nhật có chủ đích sau mỗi phát hiện mới.

## Cách cập nhật

1. Ghi bài học với nguồn, ngày, phạm vi và tình trạng: yêu cầu Tác giả / kết quả thử / nhận xét Agent / đề xuất chưa duyệt.
2. Dữ kiện cốt truyện và luật riêng để trong thư mục truyện. Trong sổ chung chỉ ghi cách nhận diện và xử lý vấn đề có thể tái dùng; nêu ngoại lệ cần giữ.
3. Tạo **commit riêng chỉ chứa bộ tài liệu chung**. Không trộn với chương, bible hoặc SI đang chạy của một truyện. Commit có thể được đọc và áp dụng độc lập.
4. Đưa commit chung lên branch mặc định, rồi lấy đúng commit đó sang các branch truyện bằng `git cherry-pick -x <sha-commit-chung>`. Nếu nhánh nguồn khác branch mặc định, dùng SHA của bản commit đã nằm trên branch mặc định khi phát tán tiếp.
5. Trước khi lấy commit, kiểm tra `git status`; nếu đang có việc chưa commit thì đọc bản nguồn bằng `git show` hoặc dùng checkout riêng. Không reset, stash hoặc ghi đè công việc đang dở để ép đồng bộ.
6. Nếu có xung đột, đối chiếu từng thay đổi và nguồn; không thay nguyên file bằng bản mới nhất chỉ vì ngày mới hơn. Sau đồng bộ, kiểm các file chung có cùng nội dung ở các branch cần áp dụng.

`<sha-commit-chung>` là chỗ điền SHA thật của commit đã kiểm tra, không phải tên một branch truyện.

## Bộ file chung của lần tổng hợp này

- `AGENT.md`: đường đọc và quy trình ghi bài học.
- `README.md`: lối vào tài liệu chung; chỉ đồng bộ thay đổi liên kết, giữ bảng truyện riêng trên từng branch.
- `chung/kinh-nghiem.md`, `chung/nguon-kinh-nghiem.md`, `chung/kiem-ke-nguon-kinh-nghiem.json`, file này.
- `chung/review-blacklist.md`: mục thoại và cách áp dụng ngoại lệ.
- `writer/SI-template`: chuẩn thoại trọn ý cho SI mới; không tự thay SI đang dùng của truyện cũ.
- `_mau-truyen/README.md`: yêu cầu đọc sổ chung trước khi khởi tạo.

Không lấy toàn bộ một branch chỉ để mang sang một bài học. Việc gộp tất cả truyện vào branch mặc định, đổi tên branch thành `main` hoặc xóa branch là công việc quản lý repo riêng, không cần làm để chia sẻ sổ kinh nghiệm.

## Mẫu một phát hiện mới

```text
ID / ngày:
Vấn đề nhìn thấy trong văn:
Nguồn (commit + file/review; hoặc ghi rõ chưa commit):
Điều đã thử và kết quả:
Yêu cầu trực tiếp của Tác giả, nếu có:
Cách áp dụng / phạm vi / ngoại lệ:
Tình trạng: đã yêu cầu / đã thử / chưa kiểm chứng / đã thay thế bởi ...
```
