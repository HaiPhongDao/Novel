# Gemini đọc thay Agent

Tác giả 05/11: "dự án này đốt token cực nhanh vì phải đọc … Có thể dùng model khác để đọc?" → chọn "Dựng lối Gemini đọc".

Gemini (AI Studio, qua extension Edge như Writer) đọc chữ Trung và báo bằng tiếng Việt; **mọi nhận định phải kèm câu
trích nguyên văn** `[NHÃN] «…»`, và `tools/doc_gemini.py` kiểm từng câu có thật trong nguồn. Không tốn token Claude;
tốn quota AI Studio chung với Writer.

| File | Việc |
|---|---|
| `si-doc.txt` | SI người đọc: không viết truyện, không chấm hay/dở, trích nguyên văn 4–40 chữ, báo tiếng Việt |
| `nhiem-vu/doc-cap.md` | So bản Writer với chương gốc: sự việc, tiếng lòng MC, nhân vật phụ, thoại, giảng giải, chỗ gần gốc |
| `nhiem-vu/tom-tat.md` | Tóm tắt từng chương bộ mẫu (≤120 từ/chương): sự việc, người, số/thiết lập, móc cuối, một câu giọng |
| `nhiem-vu/tim-anchor.md` | Đề xuất cửa sổ anchor theo chức năng; script tự cắt cửa sổ và chạy `soat_van.py` |

```
python tools/doc_gemini.py doc-cap --file GOC=<goc.txt> --file A=<ban-a.md> --file B=<ban-b.md> --out <bao-cao.md>
python tools/doc_gemini.py tom-tat --bo-mau <bo-mau.txt> --chuong 4-40 --out <bao-cao.md>
python tools/doc_gemini.py tim-anchor --bo-mau <bo-mau.txt> --chuong 4-60 --ghi-chu "<chức năng>" --out <bao-cao.md>
python tools/doc_gemini.py --chi-kiem <bao-cao.md>
```

Mã trả về `3` = có câu trích không thấy trong nguồn → coi cả báo cáo là không tin được, đọc lại hoặc chạy lại.
Prompt trên 150.000 ký tự bị chặn (chia nhỏ `--chuong`). Chạy nền: một lượt 2–5 phút.

Luật dùng:
- Gemini **khoanh vùng**, không chấm. Câu ĐẠT vẫn do Tác giả; Agent chỉ đọc đúng đoạn được trích.
- Gemini đọc bản do Gemini viết dễ dãi với chính nó: dùng mục 1–5 của `doc-cap` để biết nhìn đâu, đừng dùng mục 6
  ("gần gốc") làm bằng chứng ĐẠT.
- Báo cáo nằm cạnh bản được đọc (`gemini-doc-*.md`), commit cùng; file prompt ghép nằm ở thư mục tạm, không commit
  (chứa nguyên văn bộ mẫu).
