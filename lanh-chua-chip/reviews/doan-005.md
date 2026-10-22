# Review — Đoạn 005 (bản nháp 1) · session S2, đoạn thứ 3 trong session

**Kết luận: HỎNG → làm lại ở session mới (S3).** Bản nháp chuyển vào `archive/doan-005-v1.md`. Tác giả quyết định: không gửi prompt viết lại; đoạn hỏng thì mở session mới. Tác giả nhận xét: chất văn trôi, cảnh trưởng làng "như AI viết". Agent đồng ý.

## Triệu chứng
- **Cảnh Hob:** "他没有下跪，也没有说那些谄媚的废话" → chép gần nguyên câu trong prompt ("Ông không xin lỗi, cũng không tâng bốc"). Rồi lời kể tự giải thích: "这是一句平实的陈述，不带任何修饰。这老头把领主们看透了，但他承认……" — đúng lỗi 解释潜台词 mà SI cấm. Câu thoại "您跟以前那些Varen家的人，不太一样" chung chung, ai nói cũng được.
- **Kể lướt:** "两天后…最直观的改变是…奇迹般地淡了下去" — ba ngày công việc thành một đoạn tóm tắt.
- **Kết đoạn có câu chốt + thu gọn:** "老天饿不死会算账的人。燃料的问题，解决了。接下来，该……" — 段末金句 + 收尾癖 (SI mục 四).
- Sáo ngữ: 宝山, 黑色黄金, 愚昧的农奴.
- 小七 trôi giọng: "结果可信度：99.9%" (quá chắc, không giống chip đang hỏng 61%).
- Chữ **系统** lại lọt vào lời kể ("经不起系统高强度的地形测算") — lần thứ ba.
- "把那些**黑石头**全搬下来…砌井沿" — đá tường trang viên bị gọi là 黑石头, lẫn với than.
- Màn tránh trà của Pell lặp đúng khuôn đoạn 2 (sai Pell đi lấy đồ → đổ trà).

## Nguyên nhân (Agent tự nhận phần mình)
1. **Prompt đoạn 5 của Agent mô tả *ý nghĩa* thay vì *sự việc*:** "Mira báo tin theo kiểu của cô — vẫn gắt, nhưng đã khác", "Hob nói một câu cho thấy ông đã chịu nhìn lại". Model viết ra đúng cái ý nghĩa đó rồi giải thích nó. Đoạn 1–4 tốt vì prompt toàn là việc cụ thể (bát trà, con số, mệnh lệnh).
2. **Prompt quá nhiều việc cho ~2000 字:** Tobi + Mira + Pell + hố xí + rãnh + thành giếng + 3 ngày nhảy cóc + Hob + thử than + cảnh báo khí độc → buộc phải tóm tắt.
3. **Đoạn thứ 3 trong cùng session:** S1 (đoạn 1–2), S2 đoạn 3–4 đều tốt; đoạn thứ 3 của S2 bắt đầu trôi. Context dài + nhiều prompt tiếng Việt → giọng SI loãng dần.

## Đã làm để chặn (xem AGENT.md mục 4, 5c)
- Nguyên tắc prompt mới: tả **giao dịch / sự việc cụ thể**, không tả cảm xúc hay ý nghĩa; tối đa **2 cảnh + 1 lần nhảy thời gian** mỗi đoạn; kết đoạn bằng **một hình ảnh cụ thể**; cuối prompt nhắc tự kiểm theo SI mục 四.
- Mỗi session Writer chỉ **2 đoạn**.
- Gói bàn giao thêm phần **"Mẫu giọng"**: trích nguyên văn những đoạn đã duyệt hay nhất (Leon mặc cả ở kho lương, Hob bị ép nhận trách nhiệm) để session mới nghe lại đúng giọng.

## Làm tốt (giữ)
- Nửa đầu: Mira báo tin ("Tobi睁眼了…今天早上拉出来的东西也不带血了") cụ thể, đúng giọng; Kael (tên gã to con) đào hố; 小七 tính rãnh chữ V sâu 40 cm → Leon chảy máu cam, lau bằng lót áo choàng.
- Thử than: vạch vệt đen trên gạch, nhẹ hơn granite, 5 phút mới bén, lửa vàng–xanh, mùi lưu huỳnh; suy ra lão Jim chết vì khí than trước rồi nhà mới cháy — tốt.
- Ý mới: than có thể đem bán khắp miền bắc → **đổi than lấy lương** (đề xuất nhận làm hướng truyện — chờ Tác giả).

## (Không dùng) Ghi chú sửa — giữ lại để tham khảo
```
Viết lại phần cuối đoạn 5, từ dòng "两天后。" đến hết. Phần trước giữ nguyên, chỉ sửa 2 chữ:
- "根本经不起系统高强度的地形测算" → đổi "系统" thành "小七".
- "把那些黑石头全搬下来" → đá tường rào của trang viên gọi là "碎墙石", để khỏi lẫn với than.

Phần viết lại:
1. Hai ngày công việc: viết bằng một hai cảnh cụ thể đang diễn ra (Kael vác đá, rãnh vừa đào xong thì mưa xuống và nước chảy vòng qua giếng…), con số người bệnh mới trong ngày do Hob báo.
2. Cảnh Hob: Hob chống gậy tới bên giếng, đứng một lúc, rồi khai thật: kho lương của làng chỉ có chừng 5800 pound, hôm trước ông nói thêm 200. Leon đáp gọn rằng anh biết từ hôm đó. Hob sững lại một nhịp. Để lời thoại và động tác tự nói; lời kể dừng ở cái sững người của Hob.
3. Cảnh thử than giữ như bản cũ, riêng độ tin cậy kết luận than đá để 96%.
4. Kết đoạn: Leon mở cửa sổ nhìn sườn đồi phía đông, nhẩm nhanh một phép tính: than này đem ra ngoài đổi được bao nhiêu lương. Rồi anh bật cười. Đoạn kết thúc ở tiếng cười đó.

Viết xong tự kiểm theo mục 四、写完自查.
```

## Prompt làm lại (`briefs/doan-005.md`, bản 2)
- Rút còn 2 cảnh + 1 lần nhảy: sáng Ngày 3 bên giếng (đào bới, Mira báo tin) → chiều tối Ngày 5 bên giếng (Hob khai thật 5800 pound).
- Thử đốt than dời sang đầu đoạn 6.
- Thái độ đi qua việc cụ thể: Mira đáp lễ bằng một món đồ; Hob khai thật con số.
- Kết bằng hình ảnh: Hob đứng im bên thành giếng mới, tay siết đầu gậy.

---

# Review — Đoạn 005 bản 2 · session S3 (đoạn đầu của session)

**Kết luận: ĐẠT.** Tốt hơn hẳn bản 1. Quy tắc prompt mới có tác dụng: không còn chép prompt, không còn câu chốt cuối đoạn, kết đúng hình ảnh.

## Làm tốt
- "这要是不得病，简直对不起大自然的重力" — giọng tự giễu của Leon trở lại.
- Mệnh lệnh "三件事" ngắn, rõ; "饭减半"; vào đầu Hob ("自己这把老骨头也得跟着劈柴搬砖") cụ thể.
- Mira đáp lễ bằng **tấm da thỏ xám đã thuộc** ("本来是准备留给Tobi做冬鞋填料的") — đúng kiểu "thái độ qua đồ vật".
- Hob khai 5800 → Leon nói tiếp con số trước khi Hob nói hết → Hob chết sững. Đúng điểm bắt buộc.
- Chảy máu cam đúng cái giá của 小七; ngày thứ sáu Bram chưa về.

## Còn lỗi (nhỏ, không làm lại)
- **Số củi sai:** Hob nói xà gỗ "还剩下一半…还能烧三十几天" — mâu thuẫn với 70–80 ngày (mới đun 3 ngày). Gói bàn giao ghi số đúng: còn ~65–75 ngày.
- **小七 hiện vạch xanh trong tầm nhìn** ("蓝色高亮虚线") — lần đầu chip có hình ảnh kiểu bảng hệ thống. → *Cần Tác giả quyết.*
- **Độ tin cậy 98%** — quá cao cho chip hỏng 61%. Gói bàn giao thêm: độ tin cậy thường ở 60–90%.
- Cảnh Hob còn vài câu kể thay: "带上了彻底臣服的意味" (quá tay — Hob mới mềm đi, chưa thần phục), "脸上的皱纹似乎舒展了不少", "一丝" ×2, câu kết "仿佛那是他此刻唯一能依靠的东西".
- "灰色的**眸子**" (SI cấm).
- Đá tường trang viên gọi là "黑岩石" — lẫn với than. Lỗi gốc ở bible (trang viên ghi "nhà đá đen"). → Agent chốt: trang viên xây bằng **đá bazan đen** nặng, cứng; than là đá giòn, nhẹ.

## Chi tiết mới → canon
- Kael: tên gã to con; lưng sưng đỏ (bị phạt).
- Ba hố xí dưới dốc 30 bước, che ván và rơm; rãnh hình chữ 八 phía trên giếng 5 bước, rộng 1 thước, sâu 1,5 thước, kéo dài 20 bước mỗi bên; thành giếng cao 2 thước.
- Số ca mới: hai (Ngày 3) → một (Ngày 4) → không (Ngày 5); mười mấy người đang bệnh, bảy tám người đã đi làm lại được.
- Leon nhận tấm da thỏ, để trong túi áo choàng cạnh mẩu than.
