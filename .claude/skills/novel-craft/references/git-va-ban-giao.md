# Bàn giao, báo cáo và git (chi tiết)

Chi tiết của mục Báo cáo + Git trong SKILL.md. Đọc khi push, khi bàn giao session, khi Tác giả nói không thấy file.

## Báo cáo cho Tác giả
  4. Prompt for Author decision: *"Duyệt chốt đoạn hay cần sửa gì?"*
- **Reading the draft:** gửi **link GitHub** (`.../blob/<branch>/<truyen>/chapters/doan-XXX.md`) — Tác giả đọc trên đó. Đừng đính kèm file `.md` trừ khi họ xin: "gửi link github là được rồi".
- **Nhưng khi lần chạy là để so với bộ mẫu, hay Tác giả chưa từng thấy chữ nào của bản nháp, thì link + bảng số chưa phải câu trả lời.** Câu hỏi tiếp theo sẽ đúng là "đoạn viết so với mẫu đâu?". Phải có file **so từng đoạn** (nguyên văn ↔ bản sinh, trích đúng chữ, mỗi cặp một dòng nói khác ở đâu) rồi dán 2–3 cặp ngắn vào chat; cả bản 2.500 字 thì vẫn để link. Mẫu: `<truyen>/reviews/so-sanh-<bản>.md`; quy trình ở `references/si-test-tren-mau.md` mục 8.

## 2. Git & Finalization Workflow
When the Author approves a segment (e.g. *"Duyệt"*, *"Chốt và push"*):
1. Execute finalization via `tools/chot_doan.py` (or stage, commit, and `git push origin HEAD`).
2. Update `handoff/story-so-far.md`, `state.md`, `log.md`, and `README.md`.
3. Push directly to GitHub remote repository.
4. Reply trong chat with the commit hash and GitHub link to the chapter.

## Git
### Kiểm push trước khi tin, và bàn giao sang session khác

- **Commit hash + link không chứng minh có nội dung.** Truyện mới nằm trong thư mục con vừa tạo nên nó là untracked: commit phần còn lại vẫn thành công, link vẫn mở được, mà không có một chữ của truyện. Sau khi push, chạy `git status --short` + `git log --oneline -1` và xác nhận đường dẫn truyện đã vào commit; còn `?? <truyen>/` thì `git add <truyen>/` rồi commit lại và nói rõ với Tác giả là link trước đó không có truyện.
- **Kiểm push bằng số, không bằng mắt.** `git fetch -q origin` → `git rev-list --count HEAD ^origin/<branch>` phải bằng 0 (khác 0 nghĩa là còn commit chưa lên), rồi `git ls-tree -r --name-only origin/<branch> | grep -c '^<truyen>/'` phải khớp số file trên đĩa. Chỉ sau hai phép đếm đó mới được báo "đã push".
- **Tác giả có thể thêm file thẳng trên GitHub, nên "không tìm thấy đường dẫn Tác giả nói" chưa phải kết luận.** `find` trên đĩa rỗng thì `git fetch -q --all` rồi `git ls-tree -r --name-only origin/<branch> | grep -i <từ khoá>` — file có thể chỉ nằm trên remote (commit kiểu "Create <tên file>" do Tác giả bấm trên web). Khi branch chỉ đang `behind N`: `git merge --ff-only origin/<branch>`, **đừng `git pull --rebase`** trên branch `ccr-*` — rebase đụng commit cũ của chính mình và dừng giữa đường ở một conflict không liên quan, trong khi `--ff-only` chỉ cần đúng lúc branch đi sau. **Nhưng `--ff-only` chỉ đúng khi branch đi sau một chiều:** Tác giả commit thẳng trên GitHub web (commit kiểu "Create <file>") ngay trên commit nền của mình thì hai nhánh rẽ đôi và nó báo `Not possible to fast-forward, aborting` — lúc đó `git log --oneline -3 HEAD` + `-3 origin/<branch>` xác nhận chỗ rẽ, rồi `git rebase origin/<branch>` (chỉ một commit local) và push lại; không `reset --hard`, không bỏ commit của mình.
- **`origin/HEAD` hay trỏ về một branch khác** (mỗi session đẩy lên một branch `ccr-*` riêng), nên push thành công vẫn không thấy truyện mới trên trang repo mặc định. Đưa Tác giả link theo branch (`.../tree/<branch>/<truyen>`) và link file (`.../blob/<branch>/...`), đừng đưa link repo; không tự đổi default branch.
- `git push` treo rồi báo `could not read Username for 'https://github.com'` → `gh auth status` xác nhận tài khoản có scope `repo`, rồi `gh auth setup-git --hostname github.com` và push lại. Chẩn đoán nhanh bằng `GIT_TERMINAL_PROMPT=0 git push …` để nó fail trong vài giây thay vì treo vài phút — skill `github` có mục riêng cho lỗi này trong reference auth.
- **Tài liệu chung đang `M` phải commit riêng** (`chung/kinh-nghiem.md`, `chung/review-blacklist.md`, `README.md`, `tools/`) theo `AGENT.md`; đừng gộp vào commit của đoạn.
- **Bàn giao: file trên đĩa là bản chính, link chỉ để định vị commit.** Session tiếp nhận `git pull` rồi đọc `<truyen>/chapters/doan-XXX.md` — đọc trên file để còn chạy được `soat_van.py` trên đúng bản đó — cùng `reviews/doan-XXX.md`, `log.md`, `handoff/state.md`; không đọc nội dung qua GitHub.
- **Kết luận không ghi vào file thì mất.** Session kia nghĩ gì, loại bản nào, vì sao, không truyền sang session mới. Trước khi push phải ghi verdict + bảng số + quyết định vào `reviews/doan-XXX.md` và `log.md`.
- Chat đang chờ bàn giao thì **không `/new`**: giữ session, chờ một câu "xong rồi" là vào việc. `/new` xoá context hội thoại nhưng giữ memory, skills và file trên đĩa.
