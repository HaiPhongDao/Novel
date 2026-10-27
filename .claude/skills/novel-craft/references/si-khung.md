# Khung SI copy-paste (mọi thể loại)

Vì sao có file này: SI chỉ viết **nguyên tắc khẳng định** thì model lấp chỗ trống bằng đúng mấy tật cũ —
`踩实`, `如裂帛`, `稳如铁铸`, so sánh của người kể. Đo được: SI 骑砍 v1 (2.338 ký tự, 0 lệnh cấm) → bản chạy
ra có `踩实` 1, so sánh 4, cụm bốn chữ 80. Đừng tin "viết khẳng định là đủ": phải có **khối 5 dòng cấm đo
được**, chép từ đây, rồi mới thêm phần riêng của thể loại.

## Khung (dán và điền) — Principle + Anchor + vì sao anchor hoạt động

Tác giả chốt cấu trúc này (25/10): mỗi nguyên tắc phải đi kèm **một anchor nguyên văn** và **một đoạn giải thích
cơ chế** của chính anchor đó. Lý do: model bắt chước câu mạnh hơn đọc nguyên tắc; nhưng nếu chỉ có câu mẫu thì
nó bắt chước cả tật và cả thiết lập. Đoạn "why" dạy nó *nhìn cái gì* trong câu mẫu.

```
SI — <tên truyện> (<thể loại>). Bản vN, <ngày>.

===== BẮT ĐẦU SI =====

You write <thể loại> Chinese web serial fiction. <một câu: độc giả đến để lấy gì>.

PRINCIPLE 1 — <một câu khẳng định, đo được bằng mắt>
ANCHOR (verbatim, same lane):
```
<đoạn 3–6 câu, nguyên văn, 0 hit tật>
```
WHY IT WORKS: <3–4 câu: câu mẫu làm gì với người đọc; cái gì nó KHÔNG làm; nếu làm ngược lại thì hỏng ở đâu>

PRINCIPLE 2 — ...  (mỗi nguyên tắc một anchor, 4–5 nguyên tắc)

BANS — measurable, checked by tools/soat_van.py
- No 实 after a verb.
- No narrator comparison (像/仿佛/好似/宛如/犹如).
- No paired negation as rhythm (没有…没有…, 不…不…).
- No tone labels on speech (语气平淡/淡淡地说/声音没有起伏).
- One adjective per noun; no run of four-character phrases.

LENGTH
- Câu 20–30 chữ; đoạn 2–3 câu; chương <khoảng>.
- Kết ở một con số lớn hơn hoặc một kẻ địch lớn hơn.

===== HẾT SI =====
```

Ngân sách: 4–5 nguyên tắc × (anchor 100–220 ký tự + why 2–4 câu) ≈ **4.000–6.000 ký tự** phần dán. Nhiều
anchor hơn 5 thì loãng; ít hơn 4 thì model quay về đọc nguyên tắc suông.

```
SI — <tên truyện> (<thể loại>). Bản v1, <ngày>.

===== BẮT ĐẦU SI =====

You write <thể loại> Chinese web serial fiction. <một câu nói độc giả đến để lấy gì>.

PRINCIPLES
1. <cảnh là chỗ phải giải quyết một việc trước khi hết đoạn>
2. <một đoạn một nhịp; câu 20–30 chữ; việc xong trước, giải thích sau>
3. <người muốn gì thì nói ra; lượt thoại trả lời lượt trước>
4. <thế giới đếm được: nước, tiền, ngày, đầu người>

POV — ai đang kể

5. Close third, **chỉ trong đầu MC**. Căn phòng là cái hắn nhìn thấy, tiếng là cái hắn nghe, cái giá là cái hắn
   đếm. Không tả thứ hắn không nhìn; không gọi tên cảm xúc hắn không có.
6. Trước khi hắn nói, người đọc phải biết hắn muốn gì và phải bỏ ra cái gì: **đúng một câu tính toán mỗi
   quyết định** (đếm người, đếm bước, thứ đang mất).
7. Thân thể hắn báo cảnh: lạnh ở ngón tay, chuôi trượt, vết thương hắn đang đứng lên. Đầu người khác đóng
   lại; chỉ mở đúng một đoạn ngắn trong đầu địch cho buồn cười.

BANS — đo được, kiểm bằng tools/soat_van.py
- No 实 after a verb (踩实/坐实/实打实/实实在在地).
- No narrator comparison (像/仿佛/好似/宛如/犹如/得像). A character may compare; the narrator may not.
- No paired negation as rhythm (没有…没有…, 不…不…, 既…也…). One negation per paragraph at most.
- No tone labels on speech (语气平淡/淡淡地说/声音没有起伏/听不出波澜).
- One adjective per noun; no string of four-character phrases.

LENGTH
- Sentence 20–30 characters, two or three clauses. Paragraph two or three sentences.
- <độ dài chương>

<PHẦN RIÊNG CỦA THỂ LOẠI: 3–6 mục, mỗi mục 1–3 dòng>

===== HẾT SI =====
```

## Vì sao phải có khối POV (bằng chứng)

SI 骑砍 v3 đủ 4 nguyên tắc + 5 lệnh cấm, tật về 0, nhịp khớp mẫu — mà Tác giả đọc xong nói: *"như người ngoài
cuộc kể chuyện, không nhập cảm với MC"*. Đúng: bản đó tả bảy đội trưởng, tả mặt kỵ sĩ *"脸皮涨得通红，硬生生把
反驳的话咽了回去"* (vào đầu người khác), và có nguyên một đoạn tableau mũi giáo không có MC trong đó. Thêm khối
POV + một dòng trong prompt ("ở mỗi quyết định, đúng một câu tính toán của hắn") thì bản sau mở bằng bàn tay
hắn, tự đếm *"账册上记着一千四百人，能握矛的只有九百二十个"*, và nói rõ cái giá trước khi ra lệnh. Kết luận:
thiếu POV thì mọi con số đẹp đều vô nghĩa — đây là lỗi không script nào bắt được.

## Ba lỗi hay mắc khi viết SI mới

- **Đoạn nào cũng mở bằng tên người là một tật đo được.** Bản chương 2 (SI v6) có **40/66 đoạn** mở bằng tên (61%): `领头汉子…`, `欧文…`, `艾斯…`. Đọc lên như biên bản. Cách đo: đếm đoạn khớp `^[tên nhân vật]` chia tổng đoạn; **trên 35% là tật**. Cách sửa: mở bằng cái giác quan bắt được trước — tiếng, vật, con số — rồi để tên vào giữa câu; câu thoại thì đứng trần, không kèm `X 说`; động tác thì đặt động tác lên trước (`磨石被放到脚边，残缺的手掌压在膝头。`). Sửa tay 17 chỗ: 61% → 17%.
- **Sửa thoại cụt dễ đẻ ra hai tật mới: nhãn lặp và thẻ thoại gộp.** Bản C (SI v5) đã thoại đủ câu nhưng ra
  `欧文在心底算了一笔账：…` **4 lần** và `艾斯指着狼头对欧文问道：…` **4/6 lượt** — vì prompt yêu cầu "một câu tính
  toán mỗi quyết định" mà không cấm biến nó thành nhãn. Luật bổ sung (một dòng, vào POV): tính toán xuất hiện
  như ý nghĩ hoặc như lời nói, **không thành công thức lặp**; và lời thoại đứng riêng hoặc sau **một** động tác,
  không gộp tên người nói + người nghe + cử chỉ vào một câu. Sau khi thêm, bản D ra 17 lượt thoại, 0 nhãn,
  0 thẻ — và có mặc cả thật (bốn bó củi khô đổi nửa bầu rượu thuốc).
- **Siết "lượt thoại tự đứng" quá tay thành thoại cụt.** Luật "a turn stands on its own feet" để chữa thoại thiếu chủ ngữ, nhưng áp mạnh thì ra `“一斧断的气？” “行。”` — Tác giả đọc thấy *"cụt, trống không, không đầu không đuôi"* và nói rõ: **truyện cần viết đầy đủ, không cần giống người thật nói**. Luật đúng: mỗi lượt là **câu đủ** — ai nói, muốn việc gì, nói với ai, khi cần thì vì sao; lượt đầu của cuộc trao đổi nói rõ chủ thể; trả lời một tiếng (`是`, `行`) chỉ được **sau một lượt đã nói rõ đang đồng ý việc gì**, và không bao giờ là toàn bộ câu trả lời cho một câu hỏi. Đây là chỗ *cố ý khác mẫu*: mẫu 爽文 viết thoại cụt, Tác giả không muốn thế.

1. **Chỉ có PRINCIPLES, không có BANS** → tật cũ quay lại trong 3 chương đầu. Luôn dán khối 5 dòng.
2. **Nhét dữ kiện vào SI** (ai gọi ai, ai chết chưa chôn, tỷ giá) → SI phình, luật mới ăn chú ý luật cũ.
   Dữ kiện thuộc prompt/glossary.
3. **Đưa câu mẫu tiếng Trung vào prompt để dạy nhịp** → model chép nguyên làm mở đoạn, điểm chấm thành
   điểm giả. Ví dụ nhịp phải viết bằng tiếng Việt.

## Kiểm trước khi chạy (60 giây)

- `grep -c "踩实\|实打实" <si>` phải bằng 0 (SI tự chứa tật là model bắt chước).
- Không có câu tiếng Trung nào dài quá 8 chữ trong prompt (trừ tên/thuật ngữ).
- SI có đúng 5 dòng BANS, không hơn: dài hơn thì model đọc thành checklist và bỏ sót.
- Chạy 1 probe ngắn trước, nếu bridge chết thì không mất 3 phút.
