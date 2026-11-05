# Đọc bài hiệu chuẩn v2 — ch3 「神宠供应商」

SI v2 (`gemini/system-instruction-v2.md` = v1 bỏ BANS, một biến; bản dán 5.025 ký tự) · cùng brief
`chung/hieu-chuan/than-sung/ch03/brief.md`, cùng 3 anchor · hai chat mới, AI Studio, 05/11/2026:
bản a 4.180 字 (142 s, /u/0), bản b 4.205 字 (191 s, /u/1). Gốc 2.822 字.
Gemini đọc cặp: `gemini-doc-v2-ch03.md` (45/45 câu trích có thật). Kết quả v1: `doc-v1-ch03.md`.

**Câu ĐẠT chỉ do Tác giả — chờ Tác giả đọc.** Dưới đây là Agent đọc, để Tác giả biết nhìn chỗ nào.

## Tóm tắt: bỏ BANS không trả lại tiếng lòng MC

- **Đổi được:** so sánh và phủ định quay về gần mật độ gốc (这地方冷得像个停尸房 · 如同工厂流水线上的零件; gốc có
  停尸房一样冷 · 流水线一样). Nhãn điềm tĩnh giảm 5/2 → 0/1.
- **Không đổi:** tiếng lòng MC vẫn mất ở 4/5 sự việc. ！/？ trong lời kể ~0,24 mỗi dấu (gốc 2,83/2,48). Nhân viên
  tiệm sâu vẫn chỉ được tả từ ngoài. Chỉ có câu cuối là giọng trong đầu, và ở b thì gần gốc (合着…？).
- **Tệ hơn:** dài hơn 48% (4.180/4.205 字), câu dài hơn (34,1/39,4 字/câu), giảng huấn vượt khoảng bộ mẫu
  (1,91/1,66 so với 0–1,0), và cả hai mở bằng kể lại thiết lập (a 11 đoạn, b 8 đoạn trước khi vào tiệm thứ nhất;
  gốc vào thẳng «镇郊，疾风宠兽店。»). Giảng huấn tăng khi bỏ câu cấm lặp lại I-0025 ở làn khác (0,82 → 1,86).
- **Thinking:** không còn tự kiểm BANS. Bản a tự đặt đích «around 2,800 Chinese characters» rồi viết 4.180;
  bản b có một câu về giọng («The tone must be cynical»), còn lại là theo dõi sự việc và độ dài. Không chỗ nào nhắc
  tới tiếng lòng hài hay mong muốn riêng của nhân vật (mục 1).

## Số đo v1 ↔ v2 (kính lúp, không chấm)

| Chỉ số | Gốc ch3 | v1 a | v1 b | **v2 a** | **v2 b** | Khoảng 30 chương |
|---|---|---|---|---|---|---|
| 字 | 2.822 | 3.646 | 2.769 | 4.180 | 4.205 | — |
| 字/đoạn | 20,9 | 34,1 | 48,6 | **55,0** | **50,1** | 19,6–33,4 |
| 字/câu | 18,4 | 33,7 | 30,4 | **34,1** | **39,4** | 14,8–29,5 |
| lượt thoại | 49 | 14 | 18 | 21 | 20 | 16,6–64,8 |
| 字/lượt | 8,7 | 19,7 | 15,5 | 12,6 | 17,0 | 6,5–27,6 |
| ！ trong lời kể /1.000 | 2,83 | 0 | 0,36 | 0,24 | 0,24 | — |
| ？ trong lời kể /1.000 | 2,48 | 0 | 0 | 0,24 | 0,24 | — |
| nhãn điềm tĩnh (淡然/平静/从容/木然/淡漠) | 0 | 5 | 2 | 0 | 1 | — |
| nhãn ngữ điệu, đọc tay (E-PROSE-05) | 0 | 3 | 1 | 2 | 3 | — |
| phủ định lặp (soat_van) | 5 | 2 | 0 | 8 | 5 | — |
| so sánh 像/犹如/仿佛… | 5 | 0 | 1 | 5 | 3 | — |
| giảng huấn /1.000 | 0 | 0,82 | 0,36 | **1,91** | **1,66** | 0–1,0 |

Đo bằng `hieu_chuan.do()` + `soat_van.scan()` như v1; ！/？ đếm trong lời kể sau khi bỏ phần trong “”. Giảng huấn
v2: 铁律 · 规律 · 从来 · 通常 · 规矩 · 往往 (a); 换句话说 · 往往×3 · 通常 · 意味着 (b).

## Cùng năm sự việc (Agent đọc đúng các đoạn này)

| Sự việc | Gốc | v2 a | v2 b |
|---|---|---|---|
| MC nhìn ra mánh "tặng sâu" | 洛羽一琢磨……骗小孩呢？！ | 洛羽扯了扯嘴角，没接话，心底的账盘却转得飞快。 + đoạn giảng 吐丝是极度损耗… | 心底冷笑了一声。 + hai đoạn giảng 吐丝… / 御兽空间… |
| Soát hết mấy nghìn con | 竟没有一只超越高级天赋的个体。/ 靠。 | 视野里依旧是一片令人失望的灰白数据。 | 生怕刚才走马观花漏掉了蜷缩在深处的某个个体。 |
| Hỏi "chỉ mấy nghìn con?" | 店员：？？？ / 几千条还他妈不够你挑？！ | 喉结狠狠上下滑动… “……客人，整整三千多只，还不够您挑的？” | 青筋狠狠跳动… “……是的，后院的幼苗还没到出栏标准，目前就这些。” |
| Nhân viên tiệm 冷雾蜥 giải thích | “？？？” / 我信你个鬼。 | 脑海中浮现出镜月岛的现状。 + đoạn giảng về từ trường | 心底掠过一丝了然。 + đoạn giảng về từ trường |
| Câu cuối | 到底是在卖宠物，还是在卖黑奴？大航海时代特色是吧！ | 这帮开店的王八蛋，连…电荷都要榨得干干净净！ | 合着这岛上的中位种，全都是给各大商船队打黑工的活体电池？ |

So với v1: nhân viên tiệm sâu ở a giờ nói to được một câu gần ý gốc (还不够您挑的？), nhưng vẫn là thoại, không phải
tiếng lòng; câu cuối của cả hai bản có cảm thán/hỏi tu từ (v1 không có).

## Gemini đọc (`gemini-doc-v2-ch03.md`)

- **Sự việc:** kể lại thiết lập (15 tuổi, kỳ thi «后天上午»); a lại làm 冷雾蜥 thành «水冰双系» (brief: hệ băng,
  lặp lỗi v1 a); cả hai bỏ chi tiết mua về «收入研究所». Gemini còn nêu "đặt tên 「数据之眼」" — tên này có trong
  SI PART 4 và brief, không phải lỗi.
- **Tiếng lòng MC:** mất ở 骗小孩呢？！ · 一虫传三代，人走虫还在 · 我信你个鬼 (thành trầm ngâm, tính toán, suy ngẫm
  bối cảnh); câu cuối còn giữ, a thành chửi đổng, b thành câu hỏi tu từ.
- **Nhân vật phụ:** nhân viên tiệm sâu mất tiếng lòng (几千条还他妈不够你挑？！), chỉ còn động tác ngoài.
- **Thoại:** nhãn giọng đều đều (语气平淡 · 神情平静地拒绝 · 用平板而冷漠的语调解释道); gốc cắt ngang không cho
  nhân viên đáp, hai bản thêm một lượt đáp.
- **Giảng giải:** mở bằng đoạn mạt thế; a thêm câu đúc kết «但世上从来没有便宜的捷径。».
- **Gần gốc nhất:** «首付» · «不用了…我不缺钱» · lời tiễn khách không thật lòng.

## Sổ lỗi

Quan sát Q-0177…Q-0182 (E-PROSE-14 ×4/×4, E-PROSE-05 ×2/×3, E-SCENE-07 ×1/×1). Can thiệp **I-0049** "bỏ BANS",
chỉ số ！+？ lời kể /1.000: trước 0,18 (TB v1) → sau 0,48 (TB v2), biên độ 0,36 (chênh hai bản v1; hai bản v2
bằng nhau nên chênh v2 = 0), n = 2 → **0,83 biên độ = `vo-hieu`**. Ngoài chỉ số đích, giảng huấn đi ngược chiều
(TB 0,59 → 1,79).

## Việc chờ Tác giả

1. Đọc hai bản v2 và nói ĐẠT hay không (Agent đọc: chưa — giọng vẫn là người kể ngoài).
2. SKILL mục 8 luật 4: can thiệp `vo-hieu` phải gỡ trong phiên. Ở đây "gỡ" = trả BANS về (dùng lại v1). Đổi SI cần
   Tác giả duyệt nên Agent **chưa** gỡ; `si-dan-gemini.txt` đang là bản v2. **Khuyến nghị:** trả về v1 làm nền
   (BANS giữ văn ngắn hơn và giảng huấn thấp hơn), rồi thử biến kế trên nền đó: đổi anchor mục 1 sang một cửa sổ dày
   tiếng lòng MC (giả thuyết 2 trong `doc-v1-ch03.md`). Hai lần bỏ BANS/câu cấm (I-0025, I-0049) đều làm giảng
   huấn tăng — nếu Tác giả đồng ý, đó là ứng viên cho một dòng blacklist "bỏ câu cấm thì giảng huấn tăng".
