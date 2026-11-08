Bạn là Agent đồng sáng lập truyện của repo Novel (đọc `AGENT.md` mục 1, 3, 5c, 8 và 9 trước). Trả lời tiếng Việt, ngắn.

Việc: chạy tiếp truyện `han-nien-san-dong` (nhánh `han-nien-san-dong`, thư mục worktree `D:\ClaudeCode\Novel-han-nien-san-dong`, GitHub `HaiPhongDao/Novel`). Dùng Git Bash; đặt `PYTHONIOENCODING=utf-8`, chạy python bằng `python -I -X utf8` khi gọi tools.

Đọc theo thứ tự, đừng đọc cả chương cũ: `han-nien-san-dong/README.md` (mục "Việc kế") → `log.md` → `handoff/state.json` → `plot/outline.md` → `reviews/doan-002.md`.

Đã xong (chưa chốt, chờ Tác giả đọc): đoạn 001 (v2) và 002 trong `chapters/`, State cập nhật tới 002. SI = `gemini/si-dan-gemini.txt`, **không sửa**. Bản thử brief trơn của 001 ở `test/brief-tron/` (kết quả đọc tự nhiên hơn, nhưng Writer bịa tên nhiều hơn).

Tác giả (08/11): "chi phí chạy Writer gần như miễn phí, cứ ra brief và chạy; tôi lười đọc brief; brief dài của bạn chán, làm brief trơn đơn giản". Chạy **một bản** mỗi đoạn.

Làm lần lượt đoạn 003 → 009 theo `plot/outline.md`. Mỗi đoạn:
1. Viết brief trơn (khoảng 150–250 chữ, tiếng Việt, tên Latin): một đoạn tình huống (ai, ở đâu, ngày mấy, số liệu cần chính xác), bảng kỹ nghệ nếu có, `Dừng ở …`. Không câu thoại mẫu, không liệt kê thông tin cho NPC "kể", không nhãn tính cách, không tính từ cảm giác. Có thể thêm một dòng cuối "Tên cố định: lý chính họ La (罗里正); huyện là 县城 (không phải 镇); Khâu Lão Thuyên (邱老栓) còn sống; núi Hắc Thạch (黑石岭)". Lưu `briefs/doan-00N.md` (thay brief cũ; brief cũ vào `archive/`).
2. `python tools/soat_brief.py <brief> --goi`; rồi `python -I -X utf8 tools/build_pack.py han-nien-san-dong --tail 2500 --prompt briefs/doan-00N.md`; rồi `python tools/aistudio_run.py --new --si han-nien-san-dong/gemini/si-dan-gemini.txt --prompt han-nien-san-dong/handoff/session-start.md --out han-nien-san-dong/chapters/doan-00N.md --timeout 22` chạy nền, **một** lệnh chờ (cần Edge mở với extension). Quá ~6 phút không ra file thì kiểm log.
3. Gỡ dòng `<!-- -->` đầu file; `python tools/cong_doan.py <bản> --prompt <brief>`. ĐỎ "bản cụt" (câu cuối kết bằng dấu phẩy, lỗi mạng AI Studio) thì chuyển bản vào `archive/` rồi chạy lại.
4. Đọc bản; chỉ sửa **tên riêng** sai bằng thay thế (Writer đặt tên trùng nhân vật khác hoặc sai tên núi/lý chính/huyện); không viết đè văn. Ghi `reviews/doan-00N.md` ngắn; cập nhật `handoff/state.json` (scene_bridge, ledger, conflicts); thêm dòng vào `log.md`; commit + push. **Không chốt đoạn**: ĐẠT do Tác giả quyết.
5. Chi tiết Writer tự đặt hay thì nhận (ghi `log.md`), chi tiết làm hỏng dàn ý thì chỉnh brief đoạn sau.

Tiết kiệm token (bắt buộc): gọi `get_usage` đầu phiên và mỗi ~60 lượt; context > ~250k thì dừng, cập nhật README mục "Việc kế" rồi báo Tác giả mở phiên mới. Không SendUserFile; báo bằng link GitHub (`https://github.com/HaiPhongDao/Novel/blob/han-nien-san-dong/...`), tối đa ~15 dòng.
