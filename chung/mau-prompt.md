# Mẫu prompt viết đoạn cho Writer (AGENT.md mục 4)

Tách khỏi `AGENT.md` ngày 02/11/2026 để các phiên không phải nạp ~11 KB mỗi lần. Số mục giữ nguyên: mọi chỗ ghi "AGENT.md mục 4", "mục 4.9", "mục 4.10" đều trỏ vào file này (nguyên tắc đánh số 1, 2, 3… của từng mẫu).

Truyện nào đang chạy mẫu nào thì giữ mẫu đó; đổi mẫu giữa chừng phải có Tác giả đồng ý và ghi `log.md` (xem `AGENT.md` mục 4).

### Mẫu A — prompt ngắn
Prompt viết bằng **tiếng Việt**, yêu cầu Gemini viết chính văn **bằng tiếng Trung**. Lưu tại `briefs/doan-XXX.md`.

**Prompt ngắn: chỉ phương hướng + số liệu, còn lại Writer tự do** (Tác giả 23/10). Test ở `lam-game/test/`: cùng SI, cùng model, prompt rút từ cả trang thiết lập xuống còn vài câu thì văn đoạn 001–002 tốt lên rõ, diễn biến và nhân vật bớt cứng. Prompt dài, chi tiết làm nhiễu Writer và lấy mất chỗ tự do. Mẫu chi tiết (thiết lập / điểm bắt buộc / tự do sáng tạo) vẫn dùng ở nhánh `de-quoc-1` — xem mẫu B bên dưới.

```
Viết đoạn thứ N, khoảng 2000 chữ, bằng tiếng Trung.
(Đoạn mở đầu: Viết đoạn mở đầu cho truyện mới, khoảng 2000 chữ, bằng tiếng Trung.)

Tiền tình: (chỉ khi mở session mới) hai ba câu về chuyện đã xảy ra, kèm nguyên văn vài đoạn văn cuối của đoạn trước.

Một đoạn văn xuôi 3–6 câu: nối từ đâu, nhân vật muốn gì, chuyện gì xảy ra, đi về hướng nào. Tên riêng, xưng hô, thuật ngữ theo quy ước của truyện (`bible/glossary.md`).

Số liệu: vài con số giữ đúng độ khó — tiền đang có, khoản phải trả và hạn, giá, thời gian còn lại… chỉ thứ đoạn này dùng tới.

Dừng ở chỗ X. Mọi chi tiết còn lại do bạn quyết.
```

**Nguyên tắc viết prompt**
1. **Ngắn.** Cả prompt khoảng 150–300 chữ. Chỉ ghi hướng đi và những gì Writer không thể tự đoán đúng; thứ khác (căn phòng, ngoại hình, thoại, cách phản ứng, chi tiết phụ) để Writer quyết.
2. **Số liệu giữ độ khó.** Tiền, hạn, giá, khoảng cách, số người quyết định truyện khó hay dễ; bỏ trống thì Writer tự đặt và có thể lệch (bản chi tiết: MC thừa tiền đóng nhà; bản test: chỉ ~400 trong khi tiền nhà 800 — đúng độ khó mong muốn). Khi nhân vật tính sổ, đưa sẵn con số tổng và khung so sánh đúng.
3. **Mô tả khẳng định** — viết thứ *có*, không liệt kê thứ *không có*. Câu phủ định sẽ mồi ngược model. Muốn tránh một từ → cấp sẵn từ đúng.
4. **Không đưa câu thoại mẫu, không đánh số nhịp hành động** — model sẽ chép nguyên văn và chạy theo thứ tự.
5. **Tả sự việc, không tả ý nghĩa.** Thái độ nhân vật đổi qua một việc cụ thể, không viết "cho thấy ông đã nhìn lại". Ghi thẳng sự thật, không kèm "vì… nên…", "như thể…".
6. **Một mạch, dừng giữa chừng.** Tối đa 2 cảnh + 1 lần nhảy thời gian. Mở nối thẳng khoảnh khắc đoạn trước dừng; dừng ở một việc đang dở, chuyện kế tiếp thuộc đoạn sau.
7. **Luật cứng của truyện** (không địa danh thật, không giao diện…) nằm trong SI/bible, không nhồi vào prompt. Agent bắt lỗi khi review; lỗi lặp lại → đề xuất Tác giả thêm vào SI.
8. **Chuỗi kỹ thuật cố định của bàn tay vàng** (câu khởi động, cách xưng) ghi nguyên văn — ngoại lệ của nguyên tắc 4.
9. **Thêm câu chỉ khi đã hỏng đúng chỗ đó.** Đoạn trước sai một điểm (xưng hô, tư thế, điểm nhìn, giới hạn giác quan, mức bạo lực, người cần giữ bí mật bị vào đầu) → thêm đúng một câu vào câu sự việc của cảnh, không viết lại cả phần thiết lập.
10. **Không dùng bước "tự kiểm sau khi viết"** — model không đọc lại văn của mình. Chuẩn văn nằm trong SI; khâu kiểm là review của Agent.
11. **Cảnh hội thoại: cho mỗi người một mối bận tâm cụ thể, không cho kịch bản tranh luận** (Tác giả 23/10, lam-game 005). Prompt "cô thẳng thừng, kiệm lời, chê là làm ẩu; anh đưa ra lý do vì sao…" thành màn thuyết trình: cô diễn vẻ lạnh ở từng câu, anh nói một tràng triết lý "一字一顿". Cách viết:
   - Không gắn nhãn tính cách (thẳng thừng, lạnh lùng, kiệm lời…) vào cảnh; ghi tình trạng thật của người đó lúc này (vừa tan ca 12 tiếng, chưa ăn, mai vào ca 8 giờ) — thái độ tự ra từ đó.
   - Không giao trình tự "A chê → B phản bác bằng lý do X", không giao một ý tưởng để nhân vật trình bày. Ghi mỗi người muốn biết gì / cần gì / lo gì; họ hỏi những câu thực tế (bao lâu, làm bằng gì, ai trả tiền, được gì) và trả lời bằng việc, bằng con số, bằng thứ đưa ra xem.
   - Cho cuộc nói chuyện có chỗ lạc đề tự nhiên (đồ ăn, việc làm, chuyện cũ chung) — đừng để mọi câu đều phục vụ mục tiêu của cảnh.

### Mẫu B — prompt đầy đủ
Prompt viết bằng **tiếng Việt**, yêu cầu Gemini viết chính văn **bằng tiếng Trung**. Lưu tại `briefs/doan-XXX.md`. Rút ra từ test vòng 1 (`lanh-chua-chip/reviews/test-B-C.md`): prompt quá thưa thì sai canon, prompt từng nhịp thì văn máy móc. Công thức cân bằng: **chốt sự thật và điểm đến, thả tự do cách đi.**

```
Viết đoạn thứ N, khoảng 2000 chữ, bằng tiếng Trung.
(Đoạn mở đầu: Viết đoạn mở đầu cho truyện mới, khoảng 2000 chữ, bằng tiếng Trung.)

【Thiết lập (để tham khảo, cái gì không dùng tới thì không cần viết ra)】
- Chỉ liệt kê thứ đoạn này dùng tới: nhân vật (tên + thân phận + một đặc điểm ngoại hình + tính cách + cách xưng hô), bàn tay vàng, địa điểm, con số cần chính xác.

【Tiền tình】 (đoạn mở đầu bỏ qua)
- Ba đến năm câu, chỉ phần liên quan tới đoạn này.

【Chuyện xảy ra trong đoạn này】
- Hai ba đoạn văn xuôi: bắt đầu từ đâu → chuyện gì xảy ra → dừng ở đâu. Không đánh số, không viết hành động chi tiết và câu thoại.

【Những điểm bắt buộc】
- 2–4 gạch: sự thật, con số, chi tiết cài cắm phải chính xác.

【Tự do sáng tạo】
- Ghi rõ phần giao cho Writer: chi tiết, phản ứng nhân vật phụ, cách nhân vật chính tự giễu và tính toán, cách bàn tay vàng lộ bản lĩnh.

【Mở đầu và chỗ dừng】
- Mở: nối thẳng từ khoảnh khắc đoạn trước dừng (cùng cảnh, cùng nhịp).
- Dừng: giữa mạch, ở chỗ X; chuyện tiếp theo là Y — phần của đoạn sau.
```

**Nguyên tắc viết prompt (mẫu B)**
1. **Mô tả khẳng định** — viết thứ *có*, không liệt kê thứ *không có*. Câu phủ định ("不是系统、没有积分…") sẽ mồi ngược model. Muốn tránh một từ → cấp sẵn từ đúng (vd. 小七 / 用户 / K-07).
2. **Không đưa câu thoại mẫu, không đánh số nhịp hành động** — model sẽ chép nguyên văn và chạy theo thứ tự.
3. Chỉ đưa con số, tên, xưng hô cần chính xác — lấy từ `bible/glossary.md`. Tên riêng viết bằng chữ Latin/tiếng Việt; chỉ ghi kèm chữ Hán cho vài từ khoá dễ bị model dịch lệch (vd. Bảy → 小七), sau khi tên tiếng Trung đã được Tác giả chốt.
4. Bí mật cần giữ → điều khiển bằng **hướng nghi ngờ / hiểu biết của nhân vật chính**, không bằng lệnh cấm.
5. Luôn có mục **自由发挥** để Writer chủ động thêm chi tiết.
6. Luật cứng đầy đủ (kể cả điều cấm) nằm trong bible cho Agent dùng khi **review**; lỗi lệch luật xử lý bằng ghi chú sửa, không nhồi trước vào prompt.
7. **Tả sự việc, không tả ý nghĩa.** Thay đổi thái độ của nhân vật phải đi qua một việc cụ thể — một con số khai thật, một món đồ đưa ra, một mệnh lệnh làm theo — không viết "nói một câu cho thấy ông đã nhìn lại", "vẫn gắt nhưng đã khác". Model sẽ viết đúng cái ý nghĩa đó rồi tự giải thích nó (bài học đoạn 005).
8. **Tối đa 2 cảnh + 1 lần nhảy thời gian mỗi đoạn.** Nhiều hơn là model phải tóm tắt.
9. **Đoạn dừng giữa mạch, không khép lại.** Chỉ ra chỗ dừng (một việc đang dở) và chuyện kế tiếp thuộc đoạn sau; đoạn sau mở ngay từ khoảnh khắc đó. Nhảy thời gian đặt *trong* đoạn, không đặt ở chỗ nối hai đoạn. (Tác giả 22/10: kiểu "Kết đoạn bằng một hình ảnh" làm mỗi đoạn khép tròn như một tập phim, đoạn sau dựng cảnh lại từ đầu → mất mạch liên tục.)
10. **Không dùng bước "tự kiểm sau khi viết".** Trong chat, model viết một lượt rồi dừng — nó không đọc lại và sửa văn đã viết, nên câu nhắc tự kiểm không có tác dụng. Mọi chuẩn văn phải nằm trong SI dưới dạng **chuẩn khi đang viết**; khâu kiểm thật sự là review của Agent (`review-blacklist.md`), đoạn hỏng thì làm lại ở session mới.
11. **Thiết lập chỉ ghi sự thật trơn**, không kèm mệnh đề nhân quả hay diễn giải ("…nên…", "vì…", "như thể…", "như chưa từng…"). Writer kể lại những mệnh đề đó thành câu giải thích trong chính văn (bài học lượt 2, đoạn 1).
12. **Chuỗi kỹ thuật cố định của bàn tay vàng** (câu khởi động, cách xưng) được ghi nguyên văn trong prompt — đây là ngoại lệ của nguyên tắc 2, vì ta *muốn* Writer chép đúng.
13. **Tính từ cảm giác trong prompt sẽ thành câu mở đầu.** "Phòng ẩm mốc" → văn mở bằng mùi mốc "直往鼻孔里钻" (3 lần liên tiếp). Chỉ ghi tính từ cảm giác khi muốn Writer mở cảnh đúng bằng cảm giác đó.
14. **Tư thế, xưng hô, điểm nhìn cần giữ → ghi ngay trong câu sự việc của cảnh đó**, không chỉ ở phần thiết lập. Ghi ở thiết lập thì Writer vẫn trượt; ghi trong câu sự việc ("Suốt lúc đó Hob đứng chống gậy cạnh giếng", "cả cảnh này kể từ mắt Leon, Pell chỉ có lời nói và việc làm") thì giữ được (lanh-chua-chip lượt 2, đoạn 004–005, 015).
15. **Cảnh quyền lực đè người** (phạt, khống chế, tra hỏi): ghi đúng một hình phạt, đúng động tác khống chế, và nhân vật phụ quan trọng làm gì *trong lúc* đó. Bỏ trống thì Writer leo thang bạo lực và cho người ta quỳ lạy (lanh-chua-chip lượt 2, đoạn 004).
16. **Chỗ trống "người kia nghĩ gì" sẽ bị lấp bằng cách vào đầu người đó.** Nhân vật cần giữ bí mật → cho họ một hành động cụ thể để kết thúc phản ứng ("gật lia lịa rồi chạy ra hành lang").
17. **Bàn tay vàng: ghi giới hạn giác quan ngay trong thiết lập của đoạn** (biết đúng những gì nhân vật chính thấy, nghe, ngửi…), nhất là cảnh đêm/xa — nếu không Writer tự cho nó dò nhiệt, theo dấu từ xa.
18. **Khi nhân vật tính sổ, đưa sẵn con số tổng và khung so sánh đúng** (đủ X ngày / còn Y ngày tới mốc Z). Writer hay tính sai và đóng khung sai.
