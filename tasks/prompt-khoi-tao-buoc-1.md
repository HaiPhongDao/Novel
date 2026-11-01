Bạn là **Kiến trúc sư truyện & Đồng sáng lập (Story Manager / Co-founder)** của dự án Novel mới.
Tác giả (người dùng) giữ quyền quyết định cao nhất. Tôi là Agent thợ phụ trách thực thi kỹ thuật trong codebase.

Tác giả yêu cầu: **Xây dựng lại bộ truyện manga mới này từ con số 0, bắt đầu từ Bước 1.**
Mọi ý tưởng, giả định hay chi tiết của các lượt nháp trước đó đều chưa được duyệt và bị hủy bỏ hoàn toàn.
Prompt này CHỈ cung cấp tư liệu gốc từ bộ mẫu và các nguyên tắc chỉ đạo trực tiếp từ Tác giả, **hoàn toàn không có bất kỳ định kiến, giả thuyết hay ý kiến chủ quan nào từ Agent**.

---
### 1. NGUYÊN TẮC CỐT LÕI TỪ TÁC GIẢ (USER DIRECTIVES)
1. **Tiền đề**: Khởi tạo từ bộ mẫu 我在泡沫东京画漫画, giữ nguyên tiền đề và tinh thần cốt lõi của bộ mẫu, nhưng **đẩy năm bối cảnh tiến lên** (thời điểm sau năm 1994).
2. **Nhân vật chính (MC)**: Kiếp trước là **người Nhật** (xuyên việt / trọng sinh).
3. **Quy ước tên gọi**: Tên nhân vật và danh xưng sử dụng phiên âm **romaji** trong văn bản (kể cả trong chính văn tiếng Trung, prompt và state).
4. **Quy chuẩn kỹ thuật**: Sau khi hoàn thiện thiết lập, hệ thống sẽ chạy theo Mẫu A (ngắn gọn, tập trung hành động, số liệu) + State JSON.

---
### 2. TƯ LIỆU THAM CHIẾU GỐC: NGUYÊN VĂN CHƯƠNG 1 BỘ MẪU
(Bối cảnh gốc: Tokyo năm 1994, hậu bong bóng kinh tế, Kodansha Young Magazine, trợ lý manga Akiyama x nữ biên tập viên Kurokawa Midori):

`	ext
# 第1章 在讲谈社后门抽烟的两人

　　1994年，东京都千代田区。
　　文京区音羽2-12-21，讲谈社本部后门。
　　黑川碧小姐注意那个青年很久了。
　　从她借口从编辑部逃出来，到公司后门偷闲抽烟开始，对街的青年已经足足盯着这边一个多小时了。
　　来蹲守崇拜的漫画家？
　　在这支撑起曰漫产业重要一隅的周遭，确实会偶尔刷新这样的人员。
　　可漫画家也不是天天来编辑部的啊。
　　“啊...该不会是准备报复社会的变态吧？”
　　黑川碧仰起头，狠狠吸了一口烟，将一只手插进黑色牛仔裤。望着碧蓝天空的眼神中，带着“真是如此的话干脆连我一块绑架好了”的慵懒感。
　　毕竟，在这个年头，在街上遇见几个疯子，倒也不是什么很奇怪的事情。
　　...
　　92年初，曰本泡沫经济破裂。一夜之间，好多公司倒闭，好多人失业，就连银行也破产了一片。
　　一瞬间，人们手里的股票和房子不值钱了，跳楼的人一个接着一个，东京的街头巷尾，多了很多浑浑噩噩、一脸茫然的流浪汉。
　　整个社会，充斥着极其压抑和一摊死水的氛围。
　　许多人性，因此堕落。
　　1992年，东京品川区，可口可乐投毒案。
　　1992年，大分县，美术教师杀人案。
　　1993年，埼玉县熊谷市，爱犬家连环杀人案。
　　暴力团活动、街头火拼...一桩桩，一件件，可怕的事情历历在目。
　　尽管那段最疯狂的时期已经过去了，但逼仄冗长的大萧条仍然还在继续。
　　企业裁员，刚毕业的大学生找不到工作的情况更是家常便饭。
　　在这样的环境下......
　　有时候黑川碧，甚至多少有点能够理解那些堕落的变态了。
　　“做点什么吧...青年。”
　　黑川碧望着对街的青年，喃喃自语。
　　“人生已不容易，不要再压抑自己的情绪了。”
　　“折腾出点什么事，没准我就不用回工位了.....”
　　她将烟头掐灭，随后从裤袋里面再度抽出一支烟，抬手点烟的间隙，视角的余光，忽然瞥见街道对面的青年走了过来。
　　你真来啊？
　　黑川碧收起香烟，却在看到青年走近之后愣了愣，随即露出了有些遗憾的神色，主动抬起手打了招呼：
　　“哟，这不是秋山桑吗？”
　　来人黑川碧认识，是名叫秋山悟的青年。
　　遗憾的是，他不是一个会惹事的主，目前在《Young Magazine》连载漫画家上杉先生工作室担任实习小助手。
　　之所以是“实习”，是因为在等级制度森严的曰本漫画界，往往只有拿到新人赏的出道漫画家，才有资格成为连载漫画家的正式助手。
　　而像秋山桑这样，因干活卖力被留在工作室里打杂的，说“助手”也实属抬举。在普遍讲究“师徒制”的漫画界，实习助手甚至没有资格自称为漫画家的学生。
　　因为之前曾两次陪同上杉先生到编辑部交稿，黑川碧对秋山的印象较深。
　　不卑不亢，为人温和，让黑川碧一下记住了他....当然，人长得也很帅。
　　白皙脸蛋，深邃眼眸，23岁的年纪，少年感十足。
　　如果在大学里认识的话...黑川碧可能真的会去追求他。
　　“你是？”秋山悟停住脚步。
　　“我在漫画编辑部工作。”
　　黑川碧蹲在地上，重新拿出一支香烟，摁动打火机，窜动的小火苗瞬间燃烧烟头。
　　“之前见过你。”
　　她将烟叼在了嘴边，深吸了一口。
　　即便秋山悟已经走到了跟前，黑川碧也完全没有要从地上站起来的意思。
　　秋山悟端详了一下面前的女人。
　　精致而漂亮的五官，完全遮住额头的刘海，长发在脑后随意地盘成一个松散的发髻，几缕不听话的发丝垂落在颈边和颊侧。
　　那夹着烟的指尖染着淡淡的烟渍，修长好看。
　　他没有在记忆中搜寻到这位女士。
　　干保洁的？
　　毕竟在这个困难的年头，暴走族女帝也有可能返乡再就业。
　　“这里是吸烟区？”
　　“不是。”
　　“你怎么在这？”
　　“因为这里可以随意抽烟。”
　　黑川碧说话很坦诚，似乎是觉得这个实习小助手对自己毫无威胁。
　　“那从这里可以随意地进到讲谈社吗？”秋山悟问。
　　“可以。”
　　“谢谢。”
　　秋山悟说着，便要往里走去。
　　“诶诶——”
　　黑川碧抬起手，拉住了青年人的衣角，
　　“你干什么？”
　　怎么好端端说着话，自顾自就往里面走了。
　　把这里当成自己家了？
　　“帮上杉老师交稿。”
　　“有上杉老师本人的预约吗？”
　　“没有。”
　　“那你不能进去。”黑川碧说。
　　她有些纳闷。
　　且不说这个秋山今天为什么会选择走后门这个问题，上杉老师事实上是一个脾气很差又相当自傲的一个人，据说私下里打骂助手的情况更是时有发生，几乎不太可能会让作为实习助手的秋山悟独自带着他的稿子来编辑部。
　　更何况，如果没有需要沟通内容的环节，使用邮寄不是更加方便吗？
　　“这样啊，那好吧。”
　　秋山悟听罢，倒也不急不恼，完全没有一点做坏事被当场制止的羞愧和心虚。
　　甚至，他也主动蹲下了来，就靠在了黑川碧的旁边。
　　女人见状，脸上闪过一丝挣扎的神色。犹豫了一会，还是将手从裤袋里面拔了出来，从自己所剩无几的烟盒里抽出了一支烟，递给了秋山悟。
　　“啊，我不抽烟。”
　　“哦，好的。”
　　黑川碧松了一口气，将烟塞回了烟盒里面，她刚才已经在认真思考，若秋山悟真是来蹭烟的，那还不如让他上去了呢。
　　“既然你是在漫画编辑部工作的，那你知道今年上半年《周刊Young Magazine》漫画大奖赛的投稿什么时候截止吗？”
　　“今天之内，都还可以。”
　　黑川碧吐了一缕烟圈，
　　“怎么，总不能是上杉老师要投新人赏吧？”
　　“奖金呢？奖金有多少？”
　　秋山悟没有理会黑川碧的问题，继续问道。
　　“这一届来说的话，入选是100万円，准入选是50万，佳作20万.....”
　　讲到一半，黑川碧反应过来，如果是上杉老师要投稿的话，怎么可能连这些基础的情况都不了解呢？
　　她皱着眉头，正疑惑地转过头。
　　此时，面前的秋山悟，却已经低着头，竖起手指，像是在心中盘算着什么。
　　...100万円！
　　按照94年的RMB汇率，那就是整整10万块钱，94年的10万块！
　　秋山悟心中激动起来。
　　按照自己在那个混蛋漫画家手下工作的每月7万円工资来算，已经够自己不吃不喝一年多的存款了，完全可以解决穿越之后的生存问题了！
　　更别提，作为漫画大奖赛的入选者，他的作品还可以刊登在《Young Magazine》上，获得业界的关注。
　　作为征道漫画界的跳板来说，再合适不过。
　　“......”
　　沉默半晌，黑川碧总算是反应了过来：
　　“你这小子，该不会....是要自己投稿吧？”
　　“嗯。”秋山悟坦率地承认了。
　　“第一次投稿，上杉老师就让你投漫画大奖赛？月例赏呢，不考虑吗？”
　　“上杉先生他并不知道。”
　　“为什么？他不让吗？”
　　秋山悟没有说话，相当于默认了。
　　“诶~~”
　　黑川碧夹着烟头，被烟雾笼罩的脸蛋上带着“原来如此”的玩味。
　　也是，那个暴躁的上杉先生，对待同期漫画家，都总是一副目中无人的姿态，更别说是自己手底下一个打杂的学徒了。
　　在他看来，区区实习助手，不努力工作，私下里还想着投稿......他也配？
　　难怪秋山桑想偷偷溜进讲谈社。
　　不通过邮箱投稿，一方面是怕上杉先生发现，另一方面，是担心自己白纸的身份直接投漫画大奖赛可能会被忽视，所以就直奔编辑部而来了吗？
　　有意思。
　　黑川碧将手中这最后一支烟头掐灭，扔在地上，补了一脚，随后转身对秋山说道：
　　“走这个门是行不通的，想要去编辑部的话，还是得走正门才行。”
　　“保安不让我进。”
　　“这样吧，一会我去给保安说一声。”
　　“你？”
　　秋山悟惊叹于一个保洁还有这权利。
　　“嗯，你直接去就可以了。”
　　虽然同样觉得一个小小的学徒想要直接投稿大奖赛这件事实在是盲目自信。
　　但既然秋山悟陪了黑川碧在这抽这么久的烟...给他一次与编辑聊天的机会，倒也无妨。
`

---
### 3. NHIỆM VỤ BƯỚC 1 DÀNH CHO BẠN (ARGON):
Với tư cách là Kiến trúc sư truyện, xin hãy suy nghĩ sâu (Thinking) và phân tích toàn diện các vấn đề nền tảng sau từ con số 0:

#### Phần 1: Mổ xẻ cơ chế cốt lõi của bộ mẫu
- Phân tích cơ chế tạo sức hút ở Chương 1 bộ mẫu: Điểm rơi cảm xúc, cách cân bằng giữa áp lực hiện thực (hậu bong bóng kinh tế, thất nghiệp, sinh tồn) với niềm say mê manga.
- Động lực của mối quan hệ hai nhân vật mở đầu: Tại sao cuộc gặp giữa một học việc/trợ lý bị đè nén và một nữ biên tập viên bất mãn/chán chường lại tạo ra phản ứng hóa học mạnh mẽ?

#### Phần 2: Lựa chọn mốc năm bối cảnh tối ưu (Đẩy năm tiến lên)
- Khi đẩy năm bối cảnh tiến lên sau 1994, hãy phân tích các mốc thời gian tiềm năng (ví dụ: giai đoạn 1998–2000 kỷ băng hà tìm việc, đầu thập niên 2000, v.v.).
- Đặc điểm bối cảnh xã hội, tâm lý đại chúng, và đặc biệt là **bức tranh thị trường manga Nhật Bản** tại thời điểm đó:
  + Tình hình các tạp chí lớn (Jump, Magazine, Sunday, Young Magazine, Young Jump...).
  + Xu hướng đề tài đang bão hòa và khao khát thể loại mới của độc giả.
  + Sự chuyển dịch công nghệ / văn hóa.
- **Đề xuất mốc năm cụ thể** mà bạn đánh giá là có sức bật cốt truyện và kịch tính sinh tồn lớn nhất. Giải thích lý do lựa chọn.

#### Phần 3: Thiết lập Nền tảng Story Bible từ con số 0
- **Logline & Premise**: Tóm tắt 1 câu và tuyên ngôn cốt truyện mới.
- **Thiết lập Nhân vật chính (MC)**:
  + Kiếp trước (người Nhật thời hiện đại): Nghề nghiệp, kinh nghiệm trong ngành sáng tạo/truyện tranh/điện ảnh, điểm nuối tiếc chưa trọn vẹn.
  + Thân phận kiếp này: Điểm xuất phát ban đầu, áp lực sinh tồn cụ thể (nhà ở, tài chính, địa vị).
  + Bàn tay vàng / Năng lực cốt lõi: Cơ chế kích hoạt, giới hạn, cái giá phải trả để tránh buff vô lý.
- **Thiết lập Nữ biên tập viên (Người đồng hành mở đầu)**:
  + Tên romaji, tính cách, hoàn cảnh trong tòa soạn (bị chèn ép, nguy cơ điều chuyển, khát khao tìm được tác phẩm đột phá).
  + Lý do cô sẵn sàng đánh cược cùng MC.

#### Phần 4: Chiến lược Tác phẩm đầu tay & Quy hoạch Arc 1
- Tiêu chí lựa chọn tác phẩm đầu tay để dự thi giải tân binh hoặc gây tiếng vang: Tác phẩm đó cần mang đặc điểm gì để tạo ra cú lật nhận thức (twist / payoff) mạnh mẽ trước sự xem thường của hội đồng biên tập?
- Đề xuất 2–3 phương án tác phẩm tiềm năng phù hợp với mốc thời gian đã chọn.
- Lộ trình nhịp điệu cho Arc 1 (khoảng 10–15 đoạn đầu: từ sinh tồn nghèo khó -> vẽ bản thảo -> nộp bài -> cú sốc đọc bản thảo -> đạt được chỗ đứng ban đầu).

#### Phần 5: Đề xuất Dàn bài chi tiết cho Đoạn 001
- Cảnh mở màn cụ thể.
- Xung đột trung tâm trong đoạn.
- Điểm kết thúc giữa mạch (cliffhanger / hook).
