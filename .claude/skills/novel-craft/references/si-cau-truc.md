# Cấu trúc SI và vòng thử–đo

Dùng khi soạn lại SI (nhất là khi SI đã dài, hoặc Tác giả bắt một tật lặp lại trong văn). Tài liệu gốc của Tác giả: `D:/Claude/builder/SI Builder.txt` + `builder knowledge.txt` — đọc lại nếu còn; nguyên tắc dưới đây rút từ đó và từ kết quả thử thật.

## 1. Khung SI

Khung để chép: `writer/SI-template` v5. Bảng dưới là tên các phần của khung đó.

| Phần | Nội dung | Giới hạn thực dụng |
|---|---|---|
| ROLE | 2–3 câu: thể loại, register, ngôn ngữ ra văn | ngắn; không nhãn tính cách MC |
| FIXED CONVENTIONS | ngôn ngữ prompt vs văn, quy ước tên theo glossary, `——`/`……` | **không được bỏ khi nén** — mất phần này là Writer phiên âm tên ngay |
| PART 1 — STYLE | NARRATION 3 nguyên tắc + MOMENTS tối đa 2, mỗi cái một anchor | 4–5 anchor |
| PART 2 — EVERY PARAGRAPH | chuẩn khi đang viết, chỉ cho hành vi model đã sai ở ≥2 lần chạy | **tối đa 8 dòng** |
| BANS | 5 dòng, nói thứ đúng trước, gọi tên lớp tật chứ không liệt kê từ | đúng 5 |
| LENGTH · PART 3 — OUTPUT | độ dài câu, mở nối, dừng giữa mạch | 2 + 3–4 dòng |

- **Ngân sách: phần dán ≤ 8.000 ký tự** (đếm bằng `len()`, không bằng `wc -m` — Git Bash đếm byte). Quá ngân sách thì **cắt dòng PART 2 và chữ nguyên tắc trước, giữ anchor**.
- Nguyên tắc phải cùng cỡ nhau: một mục dài gấp đôi sẽ chiếm chú ý của model ở đúng loại cảnh đó.
- Không nhãn phẩm chất để mô tả cách viết (plain, flat, concrete…): model diễn luôn phẩm chất vào câu văn.
- **Nguyên tắc ở PART 1 không có dòng canh ở PART 2 hay BANS thì chỉ là gợi ý** (một nguyên tắc "likeness belongs to a person", không dòng nào canh, bản ra vẫn 3 so sánh của người kể). Nhưng "thêm một dòng canh" là đường dẫn tới SI 20 dòng PART 2: **mọi dòng mới qua cổng ở template v5 hướng dẫn 6** — do brief/dữ kiện thì sửa brief/glossary; mới gặp một lần thì vào review-blacklist; lặp ở ≥2 lần chạy với brief khác nhau mới thành dòng PART 2, và dòng đó **thay** dòng yếu nhất, ghi vào `log.md`. Các "dòng thêm vào SI" trong mục 6–8, 12–13 dưới đây là ứng viên, cùng phải qua cổng này.

## 2. Tật AI bắt nguồn từ chính SI

Model chép **hình thức tu từ** của SI trước khi chép nội dung. Vì vậy:

- Không viết chuỗi phủ định song song trong SI. Câu kiểu "It has no voice, no speaker, no page, no list; nobody hands it to him" ra đúng khuôn ấy trong văn: `没有…，也没有…，只有…`, `既没有…也没有…，只是…`.
- Viết lại thành khẳng định: nói thứ **đang có** và nó hoạt động thế nào.
- Đặt trần bằng một dòng CONSTRAINTS, kèm khuôn thay thế: tả người bằng thứ tay đã làm, thứ mang theo, thứ đang giữ; **một cái thiếu trong một đoạn là dữ kiện, cái thứ hai thành danh sách**.
- Cùng nhóm tật: `不是 A，而是 B` đứng riêng như nhận định của người kể; so sánh của người kể gắn sau giọng nói/ánh nhìn. Cả hai đều có thể do anchor dạy — xem `si-anchors.md` mục 4.
- **Độ cụ thể giả bằng `实`**: 踩实、坐实、砸实、实实在在地、扎扎实实 — model thêm phó từ để tự bảo đảm "cụ thể" mà không thêm chi tiết nào. Viết thành một dòng CONSTRAINTS: việc hiện ra bằng kết quả nhìn thấy được (bản lề gãy làm hai, chân trượt, tay tê), động từ mang sức nặng. Đo bằng cột `khuon-shi`.

## 3. Độ dài một output

- Model Gemini mất mạch sau ~1.500 字: nửa sau dễ thành mảnh vụn, chú thích của người kể, lệch register.
- Xin 2.000 字 thường ra 2.800 字 (dồn beat, không dãn chữ). Cách chữa là **giảm số beat mỗi output**, không phải tăng độ dài.
- Thực dụng: đích 1.200–1.500 字, 2–3 beat, prompt có ranh giới cứng. Nếu repo/hợp đồng của truyện định nghĩa "đoạn" ~2.000 字 thì nêu rõ đây là quyết định của Tác giả, đừng tự đổi đơn vị đoạn. **Khi Tác giả chốt "đoạn dài bao nhiêu cũng được, chương tách sau" thì bỏ cả trần trong SI lẫn trần trong brief**, bỏ số 字 khỏi tiêu chí review, và giữ lại đúng hai tiêu chí: không trượt ngữ cảnh, không trượt văn phong.
- **Bỏ trần độ dài thì phải thêm sàn cho câu, nếu không model nén cả câu chứ không chỉ nén đoạn.** Ba đoạn chạy liền sau khi bỏ trần ra **15,5–16,0 字/câu** trong khi mẫu 23,9 và các bản cùng SI trước đó 19,4–20,0. Hai dòng phải thêm cùng lúc với luật "no character target": (a) câu giới hạn rõ "this governs the segment only — the sentences keep their own length"; (b) sàn độ dài câu — "the average sentence sits near twenty-three characters; a run of sentences under fifteen characters reads as a list of stage directions, merge them". Đo bằng `do_nhip_cau.py` hoặc đếm `字/câu` trên bản mới; dưới 18 字/câu so với mẫu là đã trượt.
- **Độ dài chỉ được nêu một con số, và SI với brief phải trùng nhau.** SI ghi 1200–1800 còn brief ghi 1400–1800 là hai cửa sổ cho model tự chọn, và bản ra vượt cả hai (1.965 字). Chốt một khoảng, chép y nguyên vào cả hai chỗ; khi review, so độ dài với **con số trong SI** chứ không chỉ con số trong brief.
- **Hiệu chuẩn đích**: xin 2.000 → ra 2.870; xin 1.500 → ra 1.834 / 2.028 / 2.188. Model trả **+20…+45%** so với đích, ổn định qua nhiều bản. Đặt đích thấp hơn mục tiêu thật ~30% (xin 1.400 khi muốn 1.900–2.000) thay vì siết câu chữ hay thêm "đúng N chữ".

## 4. Vòng thử–đo (mỗi vòng đổi MỘT biến)

1. Chạy 2 bản ở 2 chat riêng, **cùng SI + cùng prompt** → đo khác biệt do model, không do prompt.
2. Đổi SI hoặc prompt, không đổi cả hai; nếu buộc đổi cả hai thì ghi rõ trong review là không tách được nguyên nhân.
3. Đo bằng script, không bằng cảm nhận: `python tools/soat_van.py <các bản thảo>`; muốn soát từng lỗi thì `python tools/soat_van.py --list <bản thảo>` — in từng chỗ khớp kèm 30 ký tự hai bên, để review ra quyết định giữ/sửa cho từng câu thay vì tin vào con số tổng. Cột dùng khi review: `phu-dinh-lap-cau`, `phu-dinh-ba-lan`, `ji-ye`, `bu-shi-er-shi`, `so-sanh-nguoi-ke`, `khuon-shi`, `nhan-ngu-dieu`, `hien-dai-tu`, `median_para_han`; và bốn cột thoại `luot-thoai` / `tb-chu-luot` / `luot-cut` / `ti-le-thoai`.
4. So cùng nội dung giữa các bản; đừng so bản 1.800 字 với bản 2.900 字 rồi kết luận về mật độ.
5. Ghi kết quả vào `reviews/doan-XXX.md`: bảng số + bản nào ĐẠT + vì sao; và những gì đã sửa ở SI/prompt.
6. **Mỗi bản thảo một tên chưa dùng.** `--out` ghi đè im lặng; liệt kê `<story>/chapters/` bằng `ls/Glob` (target='files') trước khi chạy, và ghi `<!-- bản X · SI vN · prompt vM -->` ở đầu file. Đã có lần đặt trùng tên bản cũ và mất luôn bản nháp đã review.

### 4b. Nhiễu giữa các lần chạy — đo trước khi nhận công

16 bản cùng một cảnh, 10 đời SI (v1 → v10), mỗi bản một lần chạy:

| Chỉ số | Khoảng | Trung bình |
|---|---|---|
| phủ định lặp | 0–5 cặp/bản | 2,2 |
| so sánh người kể | 0–3 | 1,3 |
| độ dài | 1.599–2.871 字 | 2.078 |

- **Cùng một SI cho cả hai cực của chỉ số.** SI v10 ra một bản 0 cặp và một bản 5 cặp. Tương quan giữa đời SI và số tật **r = −0,16**: sửa SI không đổi phân bố, nên mọi verdict "ĐẠT" rút từ một lần chạy là đọc nhiễu. Trước đây đã báo ĐẠT cho ba bản mà tổng dữ liệu không hề tiến bộ.
- Tương quan dương mạnh, và là thứ giải thích dữ liệu: **số đoạn nền/giải thích ↔ phủ định lặp r = +0,69**, **độ dài ↔ phủ định r = +0,66**. 排比 và so sánh của người kể sống trong đoạn giải thích, nên luật "đừng phủ định song song" và yêu cầu "có nội tâm, có nền" kéo ngược nhau: bản Tác giả khen (12 đoạn nền) có 5 cặp phủ định, bản sạch phủ định (0 cặp) thì nền mỏng và mất cảnh mở. Đừng trình bày hai chuyện này như hai lỗi độc lập sửa được cùng lúc.
- Hệ quả: khi tương quan với đời SI ≈ 0 thì **dừng sửa SI**; muốn một phép đo tuyệt đối thay cho so sánh giữa các lần chạy thì dùng test trên nội dung truyện mẫu (mục 11). Còn hai đường, chọn một và ghi rõ là thí nghiệm đang chạy: (a) đổi **đúng một biến** — thay anchor ngoại lai bằng 2 đoạn đã được Tác giả duyệt của chính repo, giữ nguyên phần còn lại; (b) đổi **model**, cùng SI + cùng prompt. Không hạ được tật thì chuyển sang pass sửa tay trên bản nháp tốt nhất thay vì đốt thêm lượt chạy.

Tính bằng script, đừng nhẩm (`soat_van.py --json`):

```python
import json, subprocess, statistics as st
files = [...]            # các bản thảo cần so
rows = json.loads(subprocess.run(['python','tools/soat_van.py','--json']+files,
                                 capture_output=True, text=True, encoding='utf-8').stdout)
def r2(x, y):
    mx, my = st.mean(x), st.mean(y)
    return sum((a-mx)*(b-my) for a,b in zip(x,y)) / (
        (sum((a-mx)**2 for a in x)*sum((b-my)**2 for b in y))**0.5)
neg = [r['phu-dinh-lap-cau'] for r in rows]
den = [r['phu-dinh-lap-cau']/r['han']*1000 for r in rows]   # mật độ/1.000 chữ
```

- So **mật độ/1.000 chữ**, không so số tuyệt đối: bản 2.363 字 tự động nhiều lỗi hơn bản 1.599 字 dù văn ngang nhau.
- **Mọi bản thảo phải có dòng provenance** `<!-- bản X · SI vN · prompt vM -->` ở đầu file. `aistudio_run.py` không tự đánh dấu, nên bản không header bị gán nhầm đời SI khi phân tích và mọi tương quan tính ra đều vô nghĩa — kiểm header trước khi tính, thiếu thì bổ sung từ `log.md`.
- Dữ liệu tổng hợp lật lại verdict cũ thì **nói thẳng trong review là verdict cũ đọc nhiễu và sửa lại đúng mục đó**; đừng để hai kết luận trái nhau nằm cạnh nhau trong cùng file.

## 5. Prompt 5 slot

1. Trạng thái nhân vật 1–2 câu (chỉ thứ đoạn này cần).
2. 2–3 beat cụ thể, có thứ tự.
3. **Ranh giới cứng, viết khẳng định**: nói cái gì thuộc đoạn sau ("câu trả lời của anh và ngày hôm sau thuộc đoạn 002") và trạng thái sự thật của đoạn này ("mỏ đã bỏ hoang mười hai năm, không còn ai làm"). Prompt của Agent cũng là mẫu tu từ — ba vế "không viết A, không viết B, không cho biết C" ra đúng khuôn phủ định trong văn; giữ tối đa một câu phủ định. Thiếu ranh giới thì Writer tự mở tuyến của đoạn 6–8 ngay đoạn 1.
4. Số: tiền đang có, khoản phải trả, hạn, giá, **và đơn vị/tỷ giá** (thiếu tỷ giá là Writer tự đặt rồi tính mâu thuẫn với chính câu trước).
5. Độ dài đích.

Không đưa phẩm chất văn vào prompt ("viết nhẹ hơn", "thoại tự nhiên") — đó là việc của SI.

### 5b. Mức chi tiết: storyboard giết đoạn nền, cắt quá tay thì tật về

Hai brief cùng SI, cùng cảnh, khác nhau chỉ ở mức chi tiết:

| Brief | Bản ra | Đoạn nền trong 12 đoạn đầu | Phủ định lặp | So sánh người kể |
|---|---|---|---|---|
| 2.599 bytes, 33 dòng, storyboard 7 bước | 1.965 字 | **0** | 0 | 3 |
| 1.504 bytes, 6 khối nội dung | 2.363 字 | **5** | 5 | 3 |

Prompt dài trấn được tật nhưng giết nền: mỗi bước là một hành động nên mỗi đoạn là một hành động, và vì brief không nhắc tiền đề nên bản thảo **không có một câu nào** cho người đọc biết đây là truyện xuyên không. Prompt ngắn nuôi nền (mùi dầu cá voi trong nhà nguyện, quan tài chưa xức dầu, mộ anh cả rêu xanh, lão thợ rèn gãy chân còn nợ tiền thuốc) nhưng tật cũ quay lại. Cách đúng là prompt ngắn **cộng ba dòng chặn**:

1. **`Mở:` một dòng nêu khoảnh khắc mở.** Bỏ dòng này thì Writer lấy khối nội dung đầu tiên có hành động làm điểm mở — thinking ghi thẳng "I'm imagining his opening action with the gate hinge", bản ra mở bằng cú búa thứ ba rồi hồi tưởng ngược, mất cảnh tỉnh và mất nhịp chậm Tác giả thích.
2. **Tiền đề một dòng: ai từ đâu tới, biết gì, không biết gì.** Thiếu thì Writer bỏ luôn tiền đề, và không script nào bắt được — khi đọc bản thảo phải tự hỏi "người đọc đoạn 001 có biết đây là truyện xuyên không không".
3. **Số dư và khoản thiếu phải viết ra, không chỉ đưa số thô.** Đưa 9 vàng 37 bạc + 4 vàng 60 bạc mà không đưa số dư thì Writer **bỏ luôn beat tự cộng** (không có 剩余 / 还差), chứ không tự tính — mà beat ấy là thứ định nghĩa nhân vật biết đọc sổ. Số dư do Agent tính bằng máy rồi ghi vào brief.

Độ dài: `khoảng 1400–1800` bị đọc thành gợi ý — hai bản liên tiếp vượt trần (1.965 rồi 2.363 字). Viết thêm trần cứng (`không quá 1800`) ngay dòng đầu brief.

### 5c. Nối đoạn — dòng đầu brief quyết định mối nối

Ba vòng đo trên một chuỗi 5 đoạn viết liền (cùng SI, cùng sổ số liệu, mỗi đoạn một brief):

| vòng | khối nối tiếp trong brief | mối nối liền | thoại | chữ/lượt |
|---|---|---|---|---|
| 1 | không có | **0/5** | 3–15 lượt | 26,0–35,7 |
| 2 | có, nhưng viết "Karl nói câu gì", "Adrian đáp gì" | **5/5** | 6–32 lượt | **12,2–22,7** |
| 3 | có, viết "mở bằng một việc nhìn thấy được" | **5/5** | 5–37 lượt | 10,4–22,1 |

Kiểu đứt của vòng 1 — không phải lỗi văn, mà mỗi đoạn là một cảnh tự thân:

| mối | câu cuối đoạn trước | câu đầu đoạn sau |
|---|---|---|
| 002 → 003 | `…提早了二十天！` (phát hiện quân tới sớm) | tả gió đêm; không ai nhắc phát hiện đó |
| 003 → 004 | `…身后传来了 Karl 扯着嗓子大喊的声音` | tả rừng thông; tiếng gọi không được đáp |
| 004 → 005 | `Karl 抓着他的腕甲` (sắp nói) | "buổi chiều"; bàn tay biến mất, người bị trói từ lúc nào không rõ |

Kết luận đo được, đừng đọc sai:

- **Cái mỏng của thoại không do khối nối tiếp, mà do phạm vi cảnh.** Ghi "ai nói gì" trong khối nối kéo thoại xuống 12–23 字/lượt (đúng luật "prompt chỉ định lượt thoại là Agent viết hộ thoại") mà tật không giảm; đổi sang "ai làm gì" vẫn 10–22 字/lượt, vì cảnh trận đánh / dựng rào / đêm chỉ có 2–3 người và không có việc gì để bàn. Muốn thoại dày: **mở phạm vi thời gian + thêm người có mặt**, không sửa khối nối.
- **Mô tả chỗ dừng bằng tiếng Việt.** Trích câu tiếng Trung cuối đoạn trước vào prompt thì Writer chép nguyên làm câu mở.
- **Viết lại một đoạn đã có trong chat phải `--new`.** Chạy tiếp session thì Writer đọc lại bản cũ của chính nó: đo được **77% dòng trùng nguyên văn**, chỉ chèn thêm khối nối ở đầu. Đổi tên bản đó thành `-lap-77` và bỏ; số đo trên nó là số của bản cũ.
- Kiểm mối nối bằng máy, đừng bằng mắt: in dòng cuối bản trước + 3 dòng đầu bản sau cạnh nhau (`python` + so hai danh sách dòng), rồi mới đọc.

## 6. Thoại: cụt là lỗi prompt, nhãn ngữ điệu là lỗi SI

- **Lượt thoại cụt/thiếu tin thường vì prompt không cho người nói thứ gì để nói.** Ghi rõ người báo cáo phải nói ra cái gì: ai sẽ đến, còn bao nhiêu ngày, cái gì bị lấy nếu thiếu tiền, trong nhà còn gì bán được. Đo trên cùng cảnh: 25,7 → 33,6 chữ Hán/lượt, lượt cụt (≤6 chữ) 5 → 4.
- Nguyên tắc SI: người nói trả lời câu hỏi rồi **thêm dữ kiện người nghe chưa hỏi**; giữa hai lượt về cùng một việc, cho một lượt chạm thứ ngoài việc (trời lạnh, con đường, người chết mùa trước) rồi quay lại việc.
- Thẻ thoại ghi **ai nói + tay/mắt đang làm gì**; ngữ điệu nằm trong chữ họ chọn. `语气平淡`、`声音没有起伏`、`淡淡地说`、`面无表情地道` là nhãn thay cho nội dung — đo bằng `nhan-ngu-dieu`. Một lượt thoại chỉ để đọc lại con số đã có trên trang cũng là lỗi: cho nhân vật nói cái giá của nó thay vì đọc số.
- **Mỗi lượt một thẻ thoại là dấu hiệu chép thoại**, kể cả khi thẻ đúng chức năng: 25 lượt / 25 thẻ `说道`, 24 thẻ đứng đầu đoạn. Nguyên tắc SI: trao đổi chạy vài lượt bằng lời trần, tên quay lại khi người đọc sắp mất dấu ai nói, động từ nói thuộc về lượt có bàn tay đang làm việc. Đo bằng `the-thoai` (số thẻ) và `tag-dau-doan` (số đoạn mở bằng thẻ); mục tiêu thực dụng: thẻ ≤ 1/3 số lượt.
- **Mỗi lượt phải tự đứng bằng chân nó: chủ ngữ trong chữ + người nhận + tiền đề.** Hai lỗi hay gặp: câu trạng thái không ai hỏi trước (`站久了有些发眩。`) và báo việc mà không nói cho ai (`待会儿便送进书房`). Dạng đúng: `我站久了，有些发晕。` / `小的让灶房温了一锅燕麦糊，待会儿便给大人送进书房。` Nguyên tắc SI: người nói tự xưng trong chữ, nói việc mình đã hoặc sẽ làm, nói việc đó **cho ai** (小的…给大人…; 我…给您…); lượt nói có tiền đề là lượt trả lời câu người đọc vừa đọc, câu không có tiền đề thì đợi tới khi cảnh hỏi tới. Chép sẵn hai dạng câu đúng vào prompt để Writer không tự nghĩ ra.
- Đừng xin "thoại tự nhiên hơn" trong prompt; sửa dữ kiện (prompt) và chức năng thẻ thoại (SI), rồi đo lại bằng bốn cột thoại.

### 6b. Thoại đủ chủ ngữ mà vẫn rỗng — lượt của MC

Tác giả gọi đúng tên lỗi này: "MC nói chuyện chưa đầy đủ, giao tiếp còn trống không". Bản thảo không có lượt cụt, câu nào cũng đủ chủ ngữ, mà đọc vẫn rỗng. Ba dấu hiệu, đo được cả ba:

1. `tb-chu-luot` thấp hơn mẫu trong khi `luot-thoai` gần gấp đôi mẫu — nhiều lượt ngắn thay vì ít lượt có nội dung (một đoạn 3 cảnh: 47 lượt/19,9 字 so với mẫu 20 lượt/22,4 字).
2. Lượt của MC chỉ nêu **việc**, không nêu **vì sao / của ai / bao nhiêu**: `“开个价吧。”` `“两枚金币一个。”` `“不买粮。”` `“起来，回队伍里去。”` — người đọc phải tự suy ra lý do và con số, nên lượt nào cũng như một mệnh lệnh rời rạc.
3. MC **bỏ qua chủ đề ngoài việc** người kia đưa ra: người ta mời uống rượu mừng đám cưới của anh trai, MC im lặng, người kể viết "không để ý tới lời thăm dò" — hai người cùng cảnh mà không nói chuyện với nhau.

Hai dòng thêm vào SI, đặt ngay cạnh luật thẻ thoại:

- Lượt của MC mang nội dung: muốn gì, của ai, vì sao hoặc bao nhiêu; lượt dưới mười chữ chỉ để trả lời câu đã nêu rõ sự việc.
- Người kia đưa chủ đề ngoài việc (đám cưới, rượu, đường đi, thời tiết) thì MC đáp bằng lời của mình rồi mới quay về việc.

Sửa ở **ba tầng**, không phải một: SI hai dòng trên; brief ghi nội dung từng lượt của MC (muốn gì + con số + đổi/đe cái gì); sửa tay trên bản nháp — thay 3–4 lượt ngắn bằng 2 lượt đầy và **thêm một cuộc mặc cả thật** (dẫn lại luật người kia vừa nói, ra giá, nói ai trả tiền, nói hậu quả nếu không nhận). Số sau khi sửa: 50 lượt/33,0 字, dài thêm ~460 字 — nếu đơn vị là đoạn thì đó là cái giá phải trả, không phải lỗi.

Bẫy: đừng "chữa" bằng cách cho MC nói dài ở mọi lượt. Lượt ngắn đúng chỗ (đáp một tiếng sau câu đã nêu rõ đang đồng ý việc gì) vẫn đúng; chỉ lượt **nêu việc mà không nêu lý do** là lỗi.

### 6c. Hình dạng một lượt lệnh — nội dung đủ mà vẫn là khẩu lệnh

Sửa nội dung (6b) chưa đủ. Lượt của MC vẫn có thể là **động từ trần**: `起来。` `站第一排。` `开个价。` `不买粮。` — đọc ra như chỉ dẫn sân khấu, không phải lời nói, và Tác giả đọc tiếng Trung bắt được ngay dù lượt đã có lý do và con số. Tiếng Trung nói ra cần **trợ từ + người nhận**: `起来吧。` `站到第一排去。` `把麦子卸到车上去。` `你给我开个价。` `粮不买了。`

Dòng luật vào SI, đặt ngay cạnh luật thẻ thoại:

> An order or a request takes its spoken shape: the verb with 吧, 去 or 给我, and the person it is said to. A bare stem inside quotation marks is a stage direction, not a line of speech.

Đo: đếm lượt mở bằng cụm ≤5 chữ rồi hết câu (`^“[^”]{1,5}[。！]`) và đọc lại từng lượt còn lại — sau khi thêm luật, lượt ngắn còn lại phải là câu đủ nghĩa (bị cắt lời, câu đáp echo sau câu đã nêu rõ việc, câu thông báo). Chứng minh hiệu quả bằng lần chạy Writer với brief không đổi, không bằng bản Agent sửa tay: SKILL.md mục 3, luật 9.

### 6d. Câu hỏi của MC — lỗ hổng giữa 6b và 6c

6b sửa nội dung lượt, 6c sửa hình dạng lệnh, nhưng **câu hỏi** lọt cả hai: một cảnh cầu cứu ra 8 lượt có câu hỏi, trong đó **4 câu của MC là câu hỏi rỗng** — `Piet怎么了？` `他要多少钱？` `烧水？` `要那些烂铁做什么？` — mỗi câu hỏi thứ mà người đọc vừa đọc xong hoặc người đối diện vừa nói. Cùng bản đó còn `“先别买。”` — câu từ chối trần đúng loại luật từ chối đã cấm, lọt vì cảnh là người khác cầu xin chứ không phải hai người ngang vai.

Đo để bắt: `lượt ≤6 字` (5/34) + đọc riêng các lượt có `？`. Hai dòng vào SI, đặt cạnh luật lượt của MC:

> A question of his carries the fact he already has and the number he suspects — 你那口井还是老井？ · 一瓶圣水几个钱？ A bare 怎么了？ / 多少钱？ is a stage direction.
>
> A refusal names the man in front of him and the reason or number with it: 咱们不买 · 你我不去 · 这钱我出不起 — not a bare 先别买.

Dòng thứ ba, cho cảnh cầu xin: **giữa hai lượt, đúng một dòng người nghe quyết gì** (không phải hắn nói gì). Đây là kỹ thuật của anchor thoại duy nhất trong SI, và là thứ thiếu thì lượt ngắn đọc thành rỗng — xem `si-anchors.md` mục 7.

## 7. Nhịp câu: câu cụt và câu trượt dài

Một luật nhịp viết thiếu trần sẽ lật sang thái cực kia. Đây là chuỗi thật khi sửa cùng một cảnh:

| Luật trong SI | Kết quả đo |
|---|---|
| "mỗi beat một đoạn, thỉnh thoảng một dòng đứng riêng" (không có trần) | mệnh đề ≤4 chữ 20%, câu cụt `发凉。` `二十三岁，刚捡回一条命。` |
| thêm "mỗi đoạn là một câu; mệnh đề cụt gia nhập câu nó thuộc về" | câu cụt hết nhưng câu kể 39 chữ, thoại thành một trượt 6–7 mệnh đề |
| thêm "dấu chấm làm việc sau hai ba mệnh đề; mỗi lượt thoại 2–3 câu" | mệnh đề 11,7 chữ, ≤4 chữ 9%, câu 21 chữ — nhưng 25 thẻ thoại/25 lượt |
| thêm luật thẻ thoại (§6) | thẻ 6/31 lượt, mệnh đề 10,9 chữ, ≤4 chữ 13%, câu 32 chữ |

Viết luật nhịp thành **hai đầu**:

- Sàn: mỗi đoạn là một câu có chủ thể và hành động; mệnh đề cụt (một trạng thái, một con số) gia nhập câu nó thuộc về; câu đứng riêng chỉ 3–4 chỗ/đoạn, đặt ở chỗ ngoặt.
- Trần: sau hai ba mệnh đề thì hết câu; sáu mệnh đề trong một câu là đọc báo cáo; một lượt thoại 2–3 câu, mỗi câu một dữ kiện.
- Vùng đích đo được: 9–13% mệnh đề ≤4 chữ, 10–12 chữ/mệnh đề, 21–32 chữ/câu kể. Đo bằng `python .claude/skills/novel-craft/scripts/do_nhip_cau.py <bản thảo…>`.
- Mở cảnh: Tác giả thường thích nhịp chậm (tỉnh → cơ thể → nhà → sân) hơn là mở bằng hành động dứt khoát; đừng mặc định "vào thẳng việc" là hay hơn.
- Con số **an toàn duy nhất** trong SI là neo độ dài câu; neo số cho độ dài lượt thoại phản tác dụng — xem mục 11.

## 8. Nhịp gặp nhau (cảnh hai người)

Triệu chứng: hai nhân vật gặp nhau ở cửa/sân/phòng sổ mà lượt đầu đã là công việc; mọi lượt đều đẩy cốt truyện; người hầu chỉ có số liệu để báo. Nguyên nhân là SI chỉ có "lượt thoại đẩy cảnh", không có luật chào.

Nguyên tắc SI (đặt thành một mục riêng, không nhét vào mục thoại): trước khi nói việc, hai người xử lý cái gặp nhau — hỏi ngủ/ăn, nhà mấy hôm nay thế nào, một người mang cái gì vào tay rồi đặt xuống, chào, càu nhàu, mối cũ, chuyện ngoài đường; việc chỉ bắt đầu khi **một người mang nó ra**.

Prompt phải cấp chất liệu cho nhịp đó, nếu không SI cũng không có gì để viết: tang chưa tế, ai đến cửa ai vắng, đồ ăn đang đợi, một chuyện ngoài việc (con vật, hàng xóm chết vì rét) — kèm câu "rồi tự quay lại việc".

Đo: `tb-chu-luot` (chữ/lượt) và `luot-cut`; đọc thêm để chắc thoại có đời sống chứ không chỉ dài ra. Nhịp chào làm trung bình lượt ngắn lại — bù bằng dữ kiện ở phần việc, đừng bỏ nhịp chào.

## 9. Chẩn đoán bằng thinking của Gemini

Thêm `--think-out <story>/archive/thinking-XXX.md` vào lệnh chạy: extension bấm mở khối `ms-thought-chunk` rồi trả chữ về. Nếu file chỉ vài chục ký tự (`Thoughts / Expand to view model thoughts`) thì khối chưa mở — chạy lại, đừng kết luận là không lấy được.

Thinking là **bản tóm tắt** do AI Studio sinh, không phải reasoning thô, nhưng đủ để thấy model hiểu SI thế nào. Thinking viết bằng **tiếng Anh** kể cả khi truyện tiếng Trung: grep theo `open` / `length` / `word count` / `character count` — tìm bằng từ khoá tiếng Trung sẽ ra rỗng và dễ kết luận nhầm là file không có nội dung. Ba thứ đáng tìm, theo thứ tự tần suất gặp:

1. **Luật bị đọc thành checklist đếm được.** Thinking nhắc lại tên luật nhiều lần ("one-beat-per-paragraph" ×7, "each paragraph contains a single sentence" ×3) là dấu hiệu model đang tự kiểm tuân thủ thay vì đang viết — và văn ra đúng kiểu đếm: đoạn một câu hàng loạt. Chữa: bỏ con số khỏi luật nhịp, viết theo cấu trúc ("một câu, hoặc hai khi câu sau mang kết quả, ba khi là một cuộc trao đổi").
2. **Lẫn tên nhân vật** (MC bị gọi bằng tên gần âm của phường chủ, cảnh bị đặt ở trụ sở hội buôn). Chữa ở prompt: liệt kê nhân vật kèm vai ngay đầu prompt — ai là người đang viết, ai chỉ được nhắc tên và không có mặt trong cảnh; và đừng đặt hai tên gần âm cho hai vai lớn.
3. **Đua đủ số chữ** ("aiming to reach the character count", "Expanding the Scene" lặp lại): model kéo dài cảnh bằng đoạn đệm. Chữa: đưa **khoảng** (1400–1800) thay cho một con số, giữ beat ≤3.

Một vòng thử thật: thinking "single sentence" 3 → 1, "one-beat-per-paragraph" 7 → 0, bản ra 1.599 字 nằm trong khoảng xin.

Chỉ rút ra luật sửa SI/prompt và ghi một dòng vào `log.md`; đừng dán thinking vào review hay vào chat.

## 10. Luật tích tụ: khi nào phải reset SI

Triệu chứng Tác giả nêu: "SI và prompt chưa thật sự làm việc, chất lượng càng ngày càng tụt". Nguyên nhân thường không phải model mà là **cách sửa**: mỗi lỗi bị bắt thì thêm một luật.

Số đo của một chuỗi như vậy:

| | đầu chuỗi | cuối chuỗi |
|---|---|---|
| SI (phần dán) | 6.869 ký tự | 10.555 ký tự |
| prompt | 188 từ | 427 từ |

Và lỗi **luân chuyển** chứ không giảm — mỗi đời SI dồn model sang một thái cực khác:

| đời | phủ định lặp | `实` | nhãn ngữ điệu | so sánh người kể | thẻ/lượt |
|---|---|---|---|---|---|
| sạch phủ định | 0 | 0 | 0 | 1 | **25/25** |
| thêm luật thẻ | 3 | 0 | 1 | 2 | 6/31 |
| bỏ số khỏi luật nhịp | 3 | **2** | 0 | 0 | 0/25 |
| thêm luật đủ chủ ngữ | 0 | 0 | 1 | **3** | 1/26 |

Dấu hiệu phải reset: SI > ~9.000 ký tự; PART 2 vượt 8 dòng; có luật sinh ra để chữa đúng một bản thảo; sửa xong thì tật cũ biến mất nhưng tật khác xuất hiện; Tác giả nói chất lượng tụt.

Quy trình reset (một lần, ghi `log.md`):

1. **Chụp lại số đo** của toàn bộ bản cũ (`soat_van.py --json`) làm mốc, kèm độ dài SI/prompt từng đời.
2. **Viết SI lõi từ đầu theo `writer/SI-template` v5**, không sửa tiếp bản cũ: giữ nguyên tắc mang giọng thể loại (lời kể, người kể) và anchor của chúng, cắt phần vá. Trần ≤ 8.000 ký tự; SI lõi 4.100 ký tự đã chạy được. Bỏ mọi con số đếm khỏi luật (trừ độ dài câu); bỏ khối xưng hô (về `bible/glossary.md`), bỏ ví dụ câu (về prompt), bỏ luật sinh ra để chữa một bản. Ghi từng dòng bị bỏ đi đâu (vd. `ky-kham-lanh-chua/gemini/test/test-gemini-moi/si-v13-ghi-chu.md`). Cắt nhầm phần giọng là hỏng kiểu khác: SI "tinh gọn" của test-gemini-moi bỏ nguyên tắc người kể của v9, giữ luật đếm cỡ đoạn — giọng sổ kép mất ở cả 5 đoạn.
3. **Prompt về 150–250 từ** + một khối dữ kiện 4–6 dòng: nhân vật kèm vai (ai đang viết, ai chỉ được nhắc), tuổi/quan hệ, trạng thái canon (ai chết, đã chôn chưa), đơn vị tiền, độ dài khoảng + trần.
4. **Chạy 1–2 bản và đo lại.** SI lõi 4.100 ký tự đã cho bản 0 phủ định / 0 `实` / 0 nhãn / 0 so sánh người kể ở 1.653 字 — tức phần lớn luật cũ không đóng góp gì; cái thiếu là **dữ kiện**, không phải luật.
5. **Đóng băng SI lõi làm mốc.** Từ đó mỗi vòng chỉ được: cắt một luật, hoặc đổi một anchor, hoặc thêm dữ kiện vào prompt. Muốn thêm luật thì phải bỏ một luật khác và ghi lý do.

Bẫy đi kèm: cắt prompt quá tay thì lỗi **chuyển từ văn sang canon** — bản không có khối dữ kiện gọi cha là `老老爷` trong khi người kể gọi `老男爵`, cho nhân vật `下葬` khi canon là chưa tế, gọi phường chủ là `老爷` thay vì `会长`, và bỏ hẳn `回大人`. Các script đếm không bắt được nhóm lỗi này; chúng thuộc prompt/glossary, không thuộc SI.

## 11. Test trên nội dung truyện mẫu (đáp án đã biết)

Khi Tác giả nghi "SI và prompt chưa làm việc", soát bản thảo của chính mình không trả lời được: không có bản đúng để so, và nhiễu giữa các lần chạy (mục 4b) lớn hơn hiệu ứng cần đo. Cách đo tuyệt đối là chạy SI trên một cảnh của **truyện mẫu đã có nguyên văn**, rồi so bản ra với nguyên văn.

Tóm tắt điều đã đo được:

- **Neo độ dài câu là con số duy nhất nên có trong SI**: câu 39,5–47,8 chữ (không neo) → 28,3–28,8 (có neo "twenty to thirty characters"), gốc 28,1–34,0.
- **Neo độ dài lượt thoại phản tác dụng**: "one sentence of ten to twenty-five characters" làm số lượt 17→41 và 4→32, vì model chẻ lời thành nhiều lượt ngắn — bỏ số, giữ câu định tính và luật "phần giải thích ở lời kể".
- **Đích là mật độ của mẫu, không phải 0**: nguyên văn có 3–4 cặp phủ định và 1 so sánh mỗi cảnh.
- Khác biệt **điểm mở cảnh** không phải lỗi cần sửa: Tác giả thích mở chậm (xem mục 7).

Quy trình đầy đủ, prompt mẫu, bảng số và giới hạn của phép test: `si-test-tren-mau.md`.

## 12. Thẻ thoại và chủ ngữ lời kể (chuyển từ SKILL.md)

- **Luật "mọi lượt thoại có thẻ" + anchor gắn thẻ cả tám dòng = lượt nào cũng kết bằng `X 说道`**, kể cả hai ba lượt
  liền của một người (Tác giả đọc ra ngay). Luật đúng: thẻ chỉ ở chỗ cần biết ai nói, tối đa một lượt trong ba,
  không bao giờ hai lượt liền của một người cùng gắn thẻ — đo cùng truyện: 15 thẻ → 1. Lúc chép SI sang truyện
  mới, soát câu chữ của luật thẻ và lời bình anchor trước khi chạy.
- **Thước chủ ngữ người trong lời kể** (他/她 + tên MC mỗi 1000 字 lời kể): bộ 骑砍 mẫu trung vị 9,0 + 9,3 = 18,7. Luật SI
  đẩy Writer từ ~12 lên ~16 nhưng dao động giữa các lần chạy lớn hơn tác dụng luật; Tác giả chấp nhận mức 10–14 khi
  đoạn mở đi theo kiểu người kể tóm lại (`ky-kham-lanh-chua/gemini/test/vong-cn-1/ghi-chu.md`).

## 13. Trợ từ cuối lượt thoại: danh sách ví dụ bị nhồi, hạn mức thì hạ được

Đo trên khong-binh 005 (cùng gói, cùng brief, chỉ đổi SI): danh sách 13 trợ từ trong luật thoại → 呢 19/35 lượt, 30/35 lượt kết bằng trợ từ. Bỏ 呢 khỏi danh sách → vẫn 呢 11/29 (model tự thêm). Thêm câu "phần lớn lượt kết bằng chữ cuối, không trợ từ; 呢 tối đa hai lần một đoạn; hai lượt liền không cùng trợ từ" → 呢 1, 4/31 lượt có trợ từ, thoại vẫn trọn ý. Luật "trợ từ chỉ cho câu hỏi/nhờ/trêu" → 14/22 và số lượt tụt. Không có ví dụ (v1.2) thì ít trợ từ nhưng Tác giả đòi ví dụ để thoại có khẩu khí.

