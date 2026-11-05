# Góp ý khi nghe — phiếu từ app DocTTS

Viết 05/11/2026. Tác giả nghe văn Writer bằng app **DocTTS** (repo `HaiPhongDao/nghien-cuu`, thư mục `tts-app`,
bản từ v1.0.13): dán bản Trung, app convert sang Việt và đọc. Thấy chỗ nào không ổn thì đánh dấu ngay chỗ đó, gắn
nhãn + ghi chú, rồi gửi **phiếu** vào chat. Thay cho kiểu góp ý "đoạn giữa hơi lạ" mà Agent phải đoán là câu nào.

## Tác giả làm gì

- Bôi đen chữ → **📝 Đánh dấu**; hoặc đang nghe thì bấm **🚩** (trong app hay trên thông báo) = đánh dấu câu vừa đọc.
- Chọn nhãn nhanh và/hoặc gõ ghi chú. Nhãn: Giọng máy, Lặp, Khó hiểu, Lê thê, Thoại giả, Sai logic, Lệch nhân vật,
  Thừa, 👍 Hay.
- **📝 Góp ý → 📤 Gửi**: phiếu vào clipboard + bảng chia sẻ, dán cho Claude.

## Định dạng phiếu

```
# Góp ý khi nghe — 3 chỗ không ổn, 1 chỗ hay
Xuất lúc: 05/11/2026 21:40 · DocTTS

# Bản: 第七章 夜袭 | Chương 7 dạ tập          ← dòng đầu bản Trung | dòng đầu bản Việt

## 1 — đoạn 4, câu 14/120 — [Giọng máy, Lặp]
中: 他的声音平淡得像一潭死水                    ← đúng phần bôi đen, chữ Hán gốc
Câu 中: 他的声音平淡得像一潭死水，没有一丝波澜。   ← cả câu chứa nó (chỉ có khi khác dòng trên)
Việt: giọng hắn bình thản như một đầm nước chết
Ghi chú: câu nào cũng "như", nghe là biết máy
```

- `中:` dò ngược từ bản đồ convert. Không có `中:` = Tác giả nghe bản không qua convert → chỉ có `Việt:` / `Câu Việt:`.
- `[chưa gắn nhãn]` + `Ghi chú: (không ghi)` = chỗ bấm 🚩 lúc nghe, chưa kịp nói vì sao. Vẫn là tín hiệu thật:
  Tác giả thấy vấp ở đó.
- `đoạn N, câu M/T` đếm theo cách app chia câu, chỉ để tham khảo; vị trí thật lấy từ công cụ dò ở dưới.

## Agent nhận phiếu

1. **Lưu nguyên văn** vào `<truyện>/reviews/gop-y-<doan>-<yyyymmdd>.md` (không sửa chữ nào).
2. **Dò vị trí**: `python tools/gop_y.py <file phiếu> <truyện>` → mỗi chỗ ra `file:dòng`. Chỉ mở vài dòng quanh
   chỗ khớp (`Read` có offset/limit), **không đọc nguyên chương**. "KHÔNG THẤY" = bản Tác giả nghe khác bản trong
   repo (chưa push, hoặc đã sửa) → hỏi Tác giả bản nào.
3. **Ghi chú thắng nhãn.** Nhãn chỉ là hướng; lời Tác giả mới là yêu cầu. Chỗ chưa nhãn chưa ghi chú: tự chẩn bằng
   skill `novel-taste`, nêu giả thuyết một dòng trong báo cáo; không chắc thì hỏi kèm câu trích.
4. **👍 Hay = giữ nguyên.** Không sửa, không "làm cho hay hơn". Đó là mẫu tốt: ghi vào review của đoạn, cân nhắc
   làm anchor/ví dụ khi sửa SI.
5. **Quy về tầng sửa**: một chỗ lẻ → sửa câu trong chương; cùng một nhãn lặp ở ≥ 3 chỗ hoặc ≥ 2 đoạn → lỗi ở brief/SI,
   đưa vào vòng sửa prompt/SI, đừng vá từng câu. Chỗ nào quy được mã trong `chung/loi/loai-loi.jsonl` thì ghi một
   dòng quan sát: `python tools/so_loi.py quan-sat --loi <mã> --truyen <truyện> --doan <đoạn> --nguon "gop-y <ngày>"`.
6. **Báo lại** theo thứ tự phiếu: `#N → đã sửa / đưa vào brief / giữ (Hay) / cần Tác giả quyết`, ≤ 15 dòng.

## Nhãn → nơi tìm nguyên nhân (gợi ý, không phải luật)

| Nhãn | Thường là | Mã hay gặp |
|---|---|---|
| Giọng máy | khuôn câu máy: phủ định lặp, 不是…而是, so sánh của người kể, nhãn ngữ điệu, giọng trang trọng | E-PROSE-01…05, 13, 14 |
| Lặp | cùng chữ/hình ảnh/khuôn câu quay lại; Writer chép nguyên tắc SI thành tu từ | E-PROSE-01, 09, E-SI-01 |
| Khó hiểu | thiếu chủ ngữ/người nhận, nhảy điểm nhìn, thiếu bối cảnh | E-SCENE-02, 05, E-EDGE-07 |
| Lê thê | giải thích thừa, người kể giảng giải, lượt thoại dài | E-PROSE-08, 12, E-EDGE-06 |
| Thoại giả | thoại cụt, nhân vật chỉ nói việc, MC thuyết trình | E-SCENE-01, 03, 04 |
| Sai logic | số/phép tính, nhân vật biết điều chưa biết, bàn tay vàng vượt hợp đồng | E-CANON-01, 04, 06 |
| Lệch nhân vật | xưng hô/register sai, nhân vật vô hồn | E-CANON-02, E-SCENE-07 |
| Thừa | câu chốt ý cuối đoạn, đoạn khép tròn | E-PROSE-08, E-EDGE-02 |
