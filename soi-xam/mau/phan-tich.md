# Phân tích văn mẫu — 《斩神：代理灰太狼，概念神也是神》

File: `mau/斩神：代理灰太狼，概念神也是神⊙1-255.txt` (1,9 MB · 247 chương có thân · tác giả 小小小落叶 · đồng nhân 《斩神》).
Đo ngày 26/10/2026 bằng script tách chương (chỉ đếm thân, bỏ dòng tiêu đề và dòng `第N节`).

## 1. Mẫu bị gãy giọng ở 第105章 — chỉ dùng 第一章–第105章

| Chương | thoại kiểu kịch bản `X：“…”` /10k 字 | `？？` /10k | `突然` /10k | chửi (艹/卧槽/他妈/草) /10k |
|---|---|---|---|---|
| 1–100 | 53–77 | 10–21 | 1–2,5 | 9–17 |
| 106–140 | 0–11 | 3–13 | 4–7 | 2–3 |
| 141–255 | 0–5 | 0–2 | 7–26 | 1–4 |

- Từ 第105章 số chương đổi từ chữ Hán sang chữ số, mất 第101–104章; từ 第107章 thoại kịch bản gần như biến mất, `突然` tăng gấp 5–10 lần,
  dấu ngoặc kép sai (`”…”`, `“…“`), câu kiểu văn máy ("灰太狼的耳朵警惕地竖成尖角，尾巴不自觉地绷直扫过地面"). Đây là người viết khác / văn máy.
- **Mẫu giọng, anchor, số đo: chỉ lấy file 001–099 (第一章–第105章).** Phần sau là ví dụ *lỗi* đáng đưa vào blacklist.
- File có rác watermark chen giữa dòng (`灵梦首发`, chuỗi `⑦零疤务是⑹…`), có khối quảng cáo QQ ở đầu và cuối. Trích anchor phải soát từng dòng.

## 2. Hình học (第一章–第105章, 99 chương)

| Chỉ số | Giá trị |
|---|---|
| 字/chương (thân) | trung vị 2.442 · tứ phân vị 2.172–2.688 |
| dòng/chương | 113 |
| 字/dòng | trung vị 19 · p25 10 · p75 32 |
| dòng ≤10 字 | 27% |
| dòng ≥60 字 | 2,8% |
| dòng kể (không thoại) | trung vị 17 字 |
| tỷ lệ chữ nằm trong dòng có thoại | 60% |
| dòng hệ thống `【】`/chương | 1,8 (dồn vào chương bàn tay vàng ra tay) |
| dòng phản ứng trơ (`X：“……”`, `“？？？”`)/chương | 10,3 |
| `！` / 1.000 字 | 25,8 |
| `？` / 1.000 字 | 19,0 |

So với lane 领主 của repo (20–34 字/câu): mẫu ngắn hơn hẳn → **không chấm bằng band của `cham_doan.py`**, chấm bằng bảng này.

## 3. Giọng — cơ chế, không phải tính từ

1. **Thoại kiểu kịch bản** `楚明：“……”` dày ở chương 1–100, nhưng chỉ dồn ở cảnh đặc định (cãi nhanh, gag lặp). **Tác giả 26/10: không dùng cho truyện mới** — số đếm cao không có nghĩa là luật cho cả đoạn. Thoại thường của mẫu: thẻ / động tác + `：“…”` hoặc `“…”X道`.
2. **Lời kể = giọng trong đầu MC.** Câu chửi, câu hỏi tu từ, meme mạng nằm thẳng trong lời kể (`我超市你的码！` · `牛波一啊！` · `起飞，这波绝对起大飞！`).
3. **Dựng–xì hơi.** Một câu nghiêm, câu sau tự giẫm lên (`要知道，概念神……而是一种概念！` → `呃……你可能觉得这是一句废话` → `好吧，这其实就是一句废话。`).
4. **Gag lặp ba bậc.** Cùng một động tác lặp, mỗi lần nặng hơn (bác sĩ ghi bệnh án: 抑郁症 → 躁郁症+反社会 → 精神失常), kết bằng một câu MC ngắn.
5. **Phá tường thứ tư.** `下一章`, `转场`, `作者`, `原着粉`, `代码就是这么写的` — logic hoạt hình/tiểu thuyết đặt vào thế giới nghiêm túc.
6. **Hệ thống có tính cách.** `【又寸！】` `【首先，本系统不接受许愿。】` — giọng nói đùa, không phải bảng số.
7. **So sánh nằm trong miệng nhân vật** và là trò đùa (`吕布骑典韦`), lời kể gần như không so sánh.
8. **Chửi thề có che** (`艹*`, `你**了个**`) khi dồn dập; bình thường thì viết thẳng `他妈`.
9. **Chuyển cảnh:** dòng `…………` rồi một cụm thời gian đứng riêng (`当天下午。`).

## 4. Động cơ (rút từ 30 chương đầu)

- **Khan hiếm:** sự gần gũi với người có năng lực (禁墟). Hệ thống chỉ tăng 羁绊值 khi MC *ở cạnh* họ → MC buộc phải bám dính nhân vật mạnh.
- **Ai định giá:** chính những người đó — sức chịu đựng của họ với MC. Mọi người coi MC là điên, nên lời thật của MC bị gạt đi → tấm khiên và cũng là nhà tù.
- **Nguồn hài lặp lại vô hạn:** năng lực là *luật hoạt hình* (转场 là hồi máu, không chết, 平底锅) va vào thế giới nghiêm túc. Mỗi năng lực mới = một luật hoạt hình mới để thử trong hiện thực.
- **Lỗ hổng của mẫu:** đồng nhân sống nhờ canon 《斩神》 (cảnh "和原着一样"); bỏ canon đi thì phải tự dựng nhóm nhân vật mạnh để MC bám.
