# Review test vòng 1 — Prompt B (đơn giản) vs Prompt C (chi tiết)

Cả hai: Gemini + system instruction 文风, prompt tiếng Việt, đầu ra tiếng Trung. Bản gốc: `chapters/test-B.md`, `chapters/test-C.md`.

**Tác giả nhận xét:** B tự nhiên hơn, nhiều chi tiết hơn; C kiểm soát được nhiều thứ nhưng máy móc. → Cần cân bằng.

## Agent đồng ý — và đây là nguyên nhân

| | B | C |
|---|---|---|
| Prompt cho Gemini | Mục tiêu + kết đoạn, gần như không có nhịp | 8 nhịp chi tiết, có cả câu thoại mẫu |
| Gemini làm gì | Tự lấp chỗ trống bằng logic thể loại mà system instruction giỏi: **算账**, khoe bàn tay vàng bằng việc cụ thể | Thực thi đúng từng nhịp theo thứ tự (system instruction dặn "只写细纲分配的节拍") → **tích checklist** |
| Bàn tay vàng | Dùng **chủ động** 3 lần (chăn → cháo mốc → vị trong miệng), mỗi lần ra một kết quả có ích → độc giả *thấy* chip mạnh ở đâu | Chỉ xuất hiện khi nhịp gọi tới; phân tích độc tố bị liệt kê từng dòng, MC xác nhận từng dòng |
| Nhân vật chính | Có hành động: hỏi tài nguyên, hỏi địa hình, ra lệnh luộc thịt muối → ra dáng lãnh chúa | Bị động, chỉ phản ứng đến tận câu cuối |
| Đúng canon | Lệch nhiều | Đúng gần hết |

**Kết luận:** prompt chi tiết từng hành động giết sự chủ động của Writer; prompt quá thưa thì sai canon. Cân bằng = **chốt sự thật và điểm đến, thả tự do cách đi**.

## Lỗi của B (cần chặn bằng prompt)
- Gọi chip là **系统**, gọi MC là **宿主**; có câu meta "没有小说里那种……系统面板" — chính là do prompt của Agent có câu phủ định "không phải hệ thống game" → **mồi ngược**. (Tác giả đã chỉ ra.)
- Gareth gọi "男爵大人" (phải là 少爷); mắt **湛蓝** (canon: xám); **帝国** (canon: vương quốc); "不到两百个农奴" (canon: hơn trăm, 143).
- Chip kết luận quá chắc và quá cụ thể (乌头碱 + 砒霜, "致死剂量", dùng từ "蓝星"), không có độ tin cậy.
- Ký ức nguyên chủ đến **trọn gói** ngay câu đầu (canon: rời rạc).
- Thiếu Pell → mất cài cắm vụ đầu độc.
- Lỗi văn theo chính checklist của system instruction: 一丝欣慰, 一丝寒意 (lượng từ mơ hồ), 湛蓝的眼底.

## Lỗi của C
- Câu chữ bị **chép từ prompt** ("建议：立即停止恐慌"); nhịp chạy đúng thứ tự Agent liệt kê.
- Báo cáo của Gareth thành 4 dòng song song + câu liệt kê "缺粮，漏雨，人跑了，没钱没物资" (đúng loại 光秃秃的清单句 mà system instruction cấm).
- Tên MC thành **"康"** một chữ — vì prompt bảo "gọi là Khang". Cần chốt tên tiếng Trung.
- "新手村" — meme game, system instruction không khuyến khích.
- Dùng "……" để bọc đoạn vào đầu Gareth (system instruction: "……" chỉ dùng khi chuyển cảnh).
- **Pell bị lộ**: "是谁每天端茶倒水" chỉ thẳng vào người hầu → lỗi do nhịp 8 của Agent ("ai luôn ở cạnh Leon").
- Vẫn dùng "系统重启完毕" → từ mặc định của model; phải **cho sẵn từ vựng đúng** thay vì cấm.

## Ý hay từ B đề xuất đưa vào canon (⏳ chờ Tác giả)
1. Tên chip **小七** — tự nhiên hơn 七号, khớp với "Bảy".
2. Cách giới thiệu chip: phân tích đồ vật tầm thường (chăn, cháo) trước khi phân tích cơ thể → cảnh trình diễn tự nhiên. Đưa vào "vùng tự do" của prompt thay vì ép.
3. Cháo cám mốc của Gareth → cụ thể hoá mức nghèo.
4. MC chủ động hỏi tài nguyên/địa hình ngay khi tỉnh → giữ làm nét tính cách.
5. Nghi ngờ hướng về **phủ bá tước** (thay vì người cạnh Leon) → đánh lạc hướng tốt, bảo vệ bí mật Pell.

## Nguyên tắc prompt rút ra (đã ghi vào AGENT.md)
1. ~~Viết prompt bằng tiếng Trung~~ → Tác giả quyết định: **prompt bằng tiếng Việt**, chính văn tiếng Trung. Tên riêng dùng Latin/tiếng Việt, chốt tên tiếng Trung sau.
2. **Mô tả khẳng định**, không liệt kê điều cấm. Muốn tránh từ nào thì **cấp sẵn từ thay thế** (小七 / 用户 / K-07).
3. Giao **theo đoạn** (~2000 字), không chia chương.
4. Cấu trúc: thiết lập (tham khảo) → chuyện xảy ra trong đoạn (kể bằng văn xuôi, không đánh số) → 2–4 điểm bắt buộc → vùng tự do → kết đoạn.
5. Không đưa câu thoại mẫu; chỉ đưa con số và sự thật cần chính xác.
6. Bí mật cần giữ → điều khiển bằng **hướng nghi ngờ** của MC, không bằng lệnh cấm.
