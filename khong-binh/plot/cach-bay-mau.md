# Cách bộ mẫu bày nội dung — và cách viết prompt theo nó

Tác giả 28/10, sau khi đọc đoạn 001 viết theo nhịp ch1 mẫu (`gemini/test/doan-001-mau/Z2.md`): "Vậy ra là do prompt… bản theo mẫu này chất lượng nội dung tốt hơn hẳn khiến khi đọc văn cũng không cảm thấy không ổn nữa."

Bài học: phần lớn cái "không ổn" ở các vòng SI 1–3 nằm ở **nội dung prompt**, không ở SI. Cùng SI E1: prompt cũ ra Y2 (đọc được nhưng "thiếu thiếu"), prompt theo mẫu ra Z2 (Tác giả thấy ổn).

## Prompt cũ khác prompt mới ở đâu

| Prompt cũ (vòng SI 1–3) | Prompt theo mẫu (Z) |
|---|---|
| Liệt kê **thông tin** MC phải biết: mình là ai, bị đày, 12.000 袋, năm ngoái 8.400 | Liệt kê **việc xảy ra** chở thông tin đó: tỉnh dậy giữa lúc người ta khâm liệm → tai nạn → ngất → giả lú → đòi ăn → hỏi chuyện → nhìn tấm thảm |
| MC "để họ nói" → Writer cho hai người đọc báo cáo, MC hỏi cụt | MC có **cớ để hỏi** từng thứ (đói thì đòi ăn, ăn dở thì hỏi vì sao nghèo, thấy thảm thì cười) → thoại có đầu có đuôi |
| Một cú lật (lửa) đến không báo trước | MC **tin sai trước** (tranh là chuyện bịa, đây là trung cổ thường) rồi mới bị lật → cú lật có lực |
| Không có nhịp đời thường | Có nhịp hài vặt: 诈尸, bánh mì gõ cửa được, "几万桶鲸油" |
| Một cảnh | Hai lần tỉnh + một vật trong phòng làm ngòi |

## Bộ mẫu bày một chương thế nào (ch1–6)

| Ch | Mở | Các việc chở nội dung | Người phụ có phần riêng | Dừng |
|---|---|---|---|---|
| 1 穿越 | Tỉnh trên mái, bị tưởng nhảy lầu, ngã | Cây tri thức ập về; giả mất trí nhớ; ba người tự giới thiệu; đòi ăn, chê đồ Tây; hỏi khoản thuế 300→1000; nhận ra không phải lịch sử Trái Đất; tranh tường diệt rồng → cười | Tướng quỳ khóc "您不记得我啦" | "这个世界真的有龙？" — "当然…而且有很多" |
| 2 萌芽 | Cười gượng sau câu trả lời | Ba người **mỗi người góp một mảnh** về thế giới; MC hỏi gia sản (300 kỵ, 1000 lính, thu 1000 金币/năm); hỏi vì sao tăng thuế → 矛盾转嫁; hỏi đặc sản (辉铁, xưởng mộc, phí qua đường); bị cãi "không đủ người" → "ai nói phải đông người?"; bịa "thần chỉ đường" | Hai thần tử **bàn sau lưng** MC, lo anh điên | Nhảy qua đêm vẽ bản vẽ → sáng hôm sau linh kiện xong → "见证工业文明的奇迹吧" |
| 3 怎么把钱花光 | Ngồi bệt lắp máy | Máy chạy, thợ gọi là thần tích; thợ già **cãi bằng giá trị của họ** ("thiếu linh hồn"); MC đáp bằng **tính giá** (30 银币 vs 1 银币); bữa tối người phụ tính lời, MC dội nước lạnh (giá sẽ rơi) → bán máy mới là tiền → hạ phí đường, sửa đường | Từng người cười một kiểu theo mối quan tâm của mình | (nửa sau ch3 là văn khác tay, bỏ qua) |
| 4 赚钱 | **Điểm nhìn người phụ** (斯特里德 ngồi chờ khách) | Khách đầu tiên choáng trước 100 cái ghế giống nhau, **mơ mộng trong đầu khách**; người phụ biết giá vốn, thấy cắn rứt; tiền đổ vào; một quý tộc trẻ sờ chân ghế, hỏi "thủ đoạn gì" | Khách mơ được phong nam tước | Báo tên → gọi lãnh chúa tới |
| 5 大手笔 | Nối thẳng câu trước | Đề nghị đầu tư con số lớn; MC cười, kể một câu chuyện để nâng giá; hỏi "anh lấy gì ra"; dẫn đi xem vũ khí | Nhà đầu tư khó chịu vì tiền không mở được cửa | Đứng trước khẩu pháo |
| 6 四战之地 | Khói tan, nhìn sức phá | Người phụ tự tính lại ván cược trong đầu; chốt giá; trả trước, lo hộ thuế; thần tử hỏi "tin được không"; về trải bản đồ, từng người chỉ một hướng địch | Mỗi người giới thiệu một mặt bản đồ | Còn hai hướng chưa bàn |

Nhịp lặp lại: **vấn đề có con số → MC hỏi tài nguyên → người phụ phản đối bằng lý lẽ của họ → MC đáp bằng phép tính → làm ngay trong chương → nhảy thời gian → kết quả ló ra ở cuối chương.** Xen giữa là việc vặt đời thường để thở (ăn, ngủ nướng, mặc áo rườm rà).

## Công thức prompt từ giờ (khong-binh)

Giữ khung mục 4 AGENT.md. Phần 【Chuyện xảy ra】 viết thành văn xuôi, nhưng nội dung đổi như sau:
1. **Kể việc, không kể thông tin.** Mỗi thông tin MC cần biết gắn vào một việc làm cho nó được nói ra: một lời hỏi có cớ, một vật trong cảnh, một sự cố.
2. **Một sự cố hoặc nhịp đời thường** ở đầu hoặc giữa đoạn (tai nạn, bữa ăn, quần áo, ngủ nướng). Ghi việc, để Writer tự làm hài.
3. **MC tin sai một điều trước khi bị lật**, nếu đoạn có cú lật. Ghi cả điều MC tin lẫn vật làm nó lật.
4. **Người phụ có phần riêng:** mỗi người góp một mảnh, cãi bằng lý lẽ hoặc lợi ích của họ, hoặc bàn sau lưng MC. Ghi họ lo gì hay muốn gì, không ghi câu thoại.
5. **MC đáp phản đối bằng phép tính.** Brief cấp sẵn giá và tổng (KN09).
6. **Dừng ở một câu hỏi hoặc một vật vừa lộ ra**; câu đáp ngắn có thể nằm trong đoạn, phần giải thích thuộc đoạn sau.
7. Cấp **vật cụ thể** cho cú lật (tấm thảm, ngọn lửa đầu ngón tay) — Writer dựng cảnh quanh vật được cấp.

Còn để ngỏ: bộ mẫu dùng 3–4 cảnh và 2 lần nhảy thời gian mỗi chương; luật 8 AGENT.md giới hạn 2 cảnh + 1 lần nhảy. Z2 nằm trong giới hạn (hai lần tỉnh cùng một phòng). Dàn ý 002–006 bên dưới vẫn giữ giới hạn; nếu đoạn nào bị tóm tắt thì cân nhắc tách đôi.
