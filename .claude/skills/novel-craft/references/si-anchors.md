# Anchor cho SI: tìm sách mẫu, chép nguyên văn, kiểm

Dùng khi SI cần 2–3 đoạn mẫu (anchor) tiếng Trung thật, đúng register. Template cấm bịa và cấm dịch, nên anchor phải lấy từ sách đã đọc được nguyên văn.

## 1. Chọn sách mẫu

- Cùng **thể loại + kiểu MC + trục truyện**, không chỉ cùng bối cảnh. Ví dụ trục "lãnh chúa + thương mại, không hệ thống" thì mẫu phải bán hàng/đàm phán/ghi sổ, không phải mẫu đánh nhau.
- Tìm: `<tên truyện> 第一章 免费阅读`, `类似 <truyện mốc>`, `<thể loại> 推荐 无金手指`.
- Ghi vào `<truyen>/archive/truyen-tham-khao.md`: bảng truyện · vì sao cùng dòng · **đã đọc nguyên văn hay chỉ biết qua giới thiệu**. Cột cuối là bắt buộc — đừng trích dẫn sách chưa từng mở.

## 2. Lấy nguyên văn

- Ưu tiên site trả danh sách chương bằng HTML thường. Cổng tải TXT và aggregator có Cloudflare thường trả body rỗng → đổi site, đừng cố.
- Mẫu đường dẫn đã dùng được:
  - uukan.org: `https://www.uukan.org/book/<bookid>.html` → `…/chapter/<bookid>.html` (danh sách) → `…/chapter/<bookid>/<chid>.html` (chương).
  - m.14xsw.com: `https://m.14xsw.com/new/<id>.html` → `https://m.14xsw.com/read/<id>/<chid>.html`.
- Lấy text bằng innerText của container, giữ nguyên đoạn:

```
js("(() => { const c = document.querySelector('#content,.content,article') || document.body; return c.innerText; })()")
```

- Lưu mỗi chương thành JSON trong workspace ngay khi lấy, để còn đối chiếu. Không chép tay từ màn hình — lỗi một chữ là lỗi hay gặp nhất.

## 3. Chuẩn hoá

- Site hay hiển thị gạch dài thành `――` → đưa về `——`.
- Site canh lề bằng CSS, **không** có `　　` đầu đoạn → giữ ngắt dòng, không tự thêm thụt; ghi chú cách chuẩn hoá vào file nguồn.
- Không cắt giữa câu: mỗi anchor ≥3 câu, giữ nguyên thứ tự đoạn.

## 4. Chọn anchor theo kỹ thuật, không theo cốt truyện

| Mục SI | Kỹ thuật phải thấy trong đoạn | Dấu hiệu trong mẫu |
|---|---|---|
| Nhịp đoạn | ba cỡ đoạn nằm sát nhau | một dòng · hai dòng · một khối dài |
| Tả sự vật | danh từ, động từ, **số** | kích thước, giá, số người, thời gian — không tính từ phẩm chất |
| Lời kể | bám điểm nhìn, có chỗ **đoán sai** | nhân vật nghĩ sai về người đối diện rồi hành động vì cái sai đó |
| Điểm nhấn | nói giảm | một con số/sự thật đứng vững, sức nặng ở phản ứng người ngoài |
| Thoại | có lời kể xen, lượt đáp nối ý | báo cáo bằng số + lệnh + một câu phản đối thực tế |
| Giải thích | chuỗi câu nêu giá/điều khoản | điều khoản bằng số, rồi câu hỏi thật của cấp dưới mở phần giải thích |
| Chuyển cảnh | dòng `……` | không có mẫu đúng thì **bỏ anchor**, giữ quy ước trong FIXED CONVENTIONS |

- **Tổng 2–3 anchor cho cả SI**, mỗi mục tối đa 1; lấy từ chương khác nhau. Nhiều anchor hơn không dạy thêm kỹ thuật mà chiếm chỗ chú ý của model và tăng nguy cơ bị bắt chước chi tiết.
- **Quét anchor theo đúng tật đang muốn bỏ** trước khi dán. Cùng một script đang dùng cho bản thảo (`tools/soat_van.py`) chạy được trên đoạn mẫu: anchor nào chứa chuỗi phủ định song song, `不是 A 而是 B`, hay so sánh của người kể thì loại — anchor dạy register mạnh hơn chữ nguyên tắc, nên nó cũng dạy luôn tật. Trong cùng chương gần như luôn tìm được cửa sổ sạch.
- Cách tìm cửa sổ sạch: duyệt các cửa sổ 4–6 đoạn liên tiếp, giữ cửa sổ có đủ ba cỡ đoạn (một đoạn ≤25 字 và một đoạn ≥90 字) và **0 hit** của các mẫu tật; in ra rồi chọn bằng mắt, đừng cắt tay từng đoạn.
- **Kiểm MC của sách mẫu có làm đúng thứ truyện mình cấm không.** Sách có MC kỹ sư tự rèn, tự giảng kỹ thuật sẽ dạy Writer đúng cái mình cấm. Nếu vẫn dùng: chỉ lấy phần nhịp/số/báo cáo/cách hỏi, và ghi cảnh báo vào `gemini/de-xuat-si.md` kèm chỉ dẫn "bản thử mà Writer bắt chước tật làm tay thì bỏ anchor nào trước".

## 5. Kiểm (bắt buộc)

```
python .claude/skills/novel-craft/scripts/verify_anchors.py <truyen>/gemini/system-instruction-vN.md <nguon.json|nguon.txt> ...
```

Script tách mọi block ``` trong file SI, bỏ khoảng trắng, đổi `――`→`——` rồi so với nguồn; in OK/MISS từng anchor và chỉ ra chỗ lệch đầu tiên. Sửa xong chạy lại tới khi đủ `n/n anchor khớp`.

Độ dài: SI đang chạy tốt ở **7.000–8.000 ký tự** phần dán vào Gemini (3 anchor). Bản 12.000 ký tự vẫn chạy nhưng loãng chú ý và dễ sinh tật hình thức; cần dài hơn thì nén chữ nguyên tắc trước, giữ anchor — xem `si-cau-truc.md` mục 1.

## 6. Ghi lại

- `log.md` một dòng: sách + chương đã dùng, số anchor, kết quả kiểm, độ dài SI, ai duyệt.
- `gemini/de-xuat-si.md`: vì sao chọn từng anchor, chuẩn hoá đã làm, cảnh báo register và thiết lập của sách mẫu (học kỹ thuật, không nhập thiết lập — KN11).

## 7. Audit anchor thoại trước khi đổ lỗi cho model

Tác giả chê một cảnh hai người nói với nhau "không ưng" thì việc đầu tiên là **đo anchor thoại của chính SI**, không phải sửa prompt. Đếm mỗi anchor: số lượt, trung vị 字/lượt, số thẻ thoại.

```
python - <<'PY'
import re, statistics, pathlib
si = pathlib.Path("<truyen>/gemini/si-dan-gemini.txt").read_text(encoding="utf-8")
for n, a in enumerate(re.findall(r'```\n(.*?)\n```', si, re.S), 1):
    turns = re.findall(r'“([^”]*)”', a)
    if turns:
        L = [len(x) for x in turns]
        print(n, len(turns), statistics.median(L), max(L), len(re.findall(r'(说道|问道|笑道|答道|回道)', a)))
PY
```

Kết quả trên một SI 7 anchor: **chỉ 1 anchor dạy thoại thật** — 4 lượt, trung vị 11,5 字, 3 thẻ, một dòng tự nhủ chen giữa. Đoạn đó dạy: thẻ sau mệnh đề trọn, lượt ngắn vẫn có nội dung **vì lời kể chen giữa mang phần đọc** (khen lịch sự trong miệng, chê thật trong đầu), lượt sau bám đúng thứ lượt trước nói.

Hệ quả: nếu cảnh cần lượt **25–35 字 mang một con số và một điều kiện** (mặc cả, xin việc, báo giá) thì SI **không có mẫu nào** cho hình dạng đó — model chỉ có mẫu lượt ngắn, nên lượt ngắn ra đúng kiểu "rỗng" dù prompt đầy dữ kiện. Mẫu có sẵn (đo trên `mau-tham-khao.txt`): chương 粮食交易 4 lượt · trung vị 26,5 字; chương có biến cố 33 lượt · trung vị 28 · 14 thẻ; chương chào hỏi xã giao 22 lượt · trung vị 12 (dùng để so, không dùng làm mẫu cho cảnh mặc cả).

Hai cách chữa, chọn theo ngân sách: (a) **amend hai câu luật có sẵn** — câu hỏi của MC mang dữ kiện hắn đã có + con số hắn nghi; câu từ chối gọi tên người trước mặt kèm lý do/con số; thêm một dòng "giữa hai lượt, một dòng người nghe *quyết* gì"; (b) **thêm một anchor thật** cắt từ chương mặc cả của mẫu — đắt hơn: SI đang 17,6k ký tự, thêm anchor là +800 và bài học cũ là SI phình thì văn tụt (xem `si-cau-truc.md` mục 10). Ghi rõ chọn cách nào và vì sao vào `log.md` trước khi chạy lại.
