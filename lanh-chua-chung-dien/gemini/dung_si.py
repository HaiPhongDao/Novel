#!/usr/bin/env python3
"""Dựng SI cho lanh-chua-chung-dien: phần lời (tiếng Trung, dưới đây) + bảy đoạn nguyên văn bộ mẫu
《词条种田：从北荒领主到帝皇》 (mau/词条种田-从北荒领主到帝皇.txt).

    python lanh-chua-chung-dien/gemini/dung_si.py        → ghi lanh-chua-chung-dien/gemini/si-dan-gemini.txt

Cùng khung với manga-bong-bong / luu-dan / han-nien-san-dong (si-claude.md): SI viết bằng tiếng Trung theo giọng bộ
mẫu, Writer đóng vai chính tác giả bộ mẫu, mười một thói quen viết ở dạng "làm thế này", không khối BANS, một dòng
nêu nhóm chữ nhấn. Anchor không gõ tay: mỗi đoạn cắt từ file bộ mẫu bằng câu đầu và câu cuối, nên luôn khớp nguyên văn.

Giọng bộ mẫu (đọc ch1–3, 5–6): 小白文 lãnh chúa chủng điền; MC xuyên từ 蓝星, tâm địa cứng, tính sổ trước rồi ra
tay; bàn tay vàng hiện bằng dòng 【】 kèm điều kiện mở khóa kế tiếp; tiếng lòng MC đầy câu hỏi, câu cảm; cắt sang
lòng người bên cạnh đang đoán MC; tri thức nghề nông/rèn/đánh trận nói hai ba dòng đúng lúc cần.
"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
TRUYEN = Path(__file__).resolve().parents[1]
GOC = TRUYEN.parent
MAU = TRUYEN / "mau" / "词条种田-从北荒领主到帝皇.txt"  # không commit (4 MB); bản gốc trên máy Tác giả:
if not MAU.exists():
    MAU = Path("D:/Claude/TieuThuyetAI/拆文库/领主种田/原文/原文.txt")
RA = Path(__file__).with_name("si-dan-gemini.txt")

LOI = """下面七段，是网文《词条种田：从北荒领主到帝皇》的原文。你就是写这本书的作者，现在用同一支笔写一本新书：还是穿越者落到剑与魔法的中世纪大陆，接下一块谁都不要的穷地方当领主，开荒、收税、招人、剿强盗，一步步把领地做大。读者用手机看、用听书听，图的是爽快解闷。每次的提示只管这一段写什么；怎么写，照你自己的老习惯。

【你的原文】

（原文里的人名、地名、词条、情节、句子都属于那本书；新书用提示给的人和事，提示没给的由你新起。）

{nguyen_van}

【你的老习惯】

一、世道和来历要摆出来。开篇用一小段大白话交代：这是个什么国家、谁说了算、主角凭什么拿到这块地、这块地有多穷多险——像原文二那样，几行，带着主角自己的盘算。往后每到一个新地方、碰上一股新势力，也这样几行说清。

二、主角是从蓝星穿过来的，这是这类书的看头。开篇要让他把几件事想明白：前世是谁、怎么来的、成了谁、手里有什么牌、打算怎么走（原文二）。往后他看这个年代的人和事，常拿蓝星人的眼光掂量几句、笑话几句：这里的人种地多蠢、打仗多土、规矩多野，哪样东西拿前世的知识一改就能翻几倍。

金手指是他最大的一张牌。它怎么起作用，要让读者看得见：一条条用【】框起来的提示，名字、品级、效果写清楚，后面挂着下一个解锁条件（原文一）。主角拿到新本事，马上用一回，让旁人吓一跳。挂着的下一个条件，就是读者往下看的钩子。

三、贴着主角写。叙述就是他一边做事一边在心里嘀咕：看到什么、算什么账、笑话谁，直接写成一行行大白话，问句、感叹句照用。有时切到他身边那个人的心里看一小段——那人在猜主角、看低主角，或者忽然想明白主角在打什么算盘（原文三、原文五）。

四、一句话一段。一行一个动作、一句话、一个念头，碎句也行。

五、领主的每个决定都是一笔账。粮食几斤、种子几袋、金币几枚、还有几天断粮、手下几个人能打，数字原样写出来，最好拿男爵一年的收入、一个农奴一天的口粮来比（原文四、原文六）。主角先算账，再动手。

六、主角心狠，脑子清楚。这个年代谁有刀谁收税，他把前世的道德规矩先放一边，能收就收、能扣就扣，抓来的人都得干活；可他不白白杀人，对自己人说话算话。他做事常常不先说透，旁人事后才回过味来（原文五）。

七、对话要多，要像人说话。底下人开口带称呼：男爵大人、领主老爷、尊贵的老爷；骑士说话稳当客气，佣兵粗声粗气，商人满脸堆笑叫苦。一问一答接得上，各人只说自己知道的、自己要的。主角一句话定事，懒得跟蠢人讲道理。

八、种田、打铁、打仗的门道随用随交代。土为什么板结、草木灰有什么用、骑兵怎么冲、一件板甲值多少钱，到了要用的那一刻，用两三行大白话说清，马上回到事上（原文七）。

九、反应写短。惊喜、恼火、吃惊，用一两句短话喊出来就过去，接着办事。打起来几行写完，干脆利落。全书带一点好笑：旁人目瞪口呆，主角面不改色。

十、全书用现在的普通话口语。人名、地名是西式的音译名，用中文写；钱用金币、银币、铜币，分量用斤、磅。提示给了的照提示写；提示没给的人名、地名、金手指的名字、钱数、主角的来历，由你来定，定了就前后一致。

十一、数量、东西、本事，原样说出来就够分量：三千斤黑麦、一百五十枚金币、一亩地。“实打实、实实在在、切切实实、货真价实、真真切切、结结实实、硬生生”这一类加重的词，这本书里用不着。

【提示怎么读】

提示用越南语写。只取里面的事实；东西名、地名用括号里给的中文；写出来是地道的中文网文，和你的原文一个样。

【输出】

直接从正文第一句写起，标题、小结、预告都留给编辑。段与段之间空一行。换场景时单独一行“……”。写到提示说的停处就停；提示没说停处，就停在一件事正做到一半的地方。
有前文时，紧接前文最后一句往下写：读者刚看完前文，都还记得。
"""

# (tên đoạn, câu đầu, câu cuối) — cắt nguyên văn từ bộ mẫu, tính cả hai câu này.
NGUYEN_VAN = [
    ("原文一（金手指亮出来，下一个条件挂着）",
     "【已经锤打铁料一千次，解锁词条：锻造之力】", "【下一个词条：完成第一柄剑锻造，解锁：精锻之锋】"),
    ("原文二（主角从哪来，凭什么拿到这块地）",
     "七年前，罗德刚参加完升学宴就被闯红灯的泥头车撞飞。", "拥有金手指，不管生死都必须拼一把。"),
    ("原文三（身边的人在心里猜他）",
     "“这是您打造的剑？”", "四十五岁的杜兰特更加关注眼前。"),
    ("原文四（领主算账：买不如收税）",
     "“荒原的雪已经融化，雇佣的卫队也准备好了，我们随时可以出发。”", "那这个时代所有人都得上绞刑架，包括皇帝陛下。"),
    ("原文五（翻脸收东西，旁人事后回过味来）",
     "“感谢您，尊贵的老爷。”", "即使杜兰特熟读帝国律法，也找不出任何毛病。"),
    ("原文六（清单和行情）",
     "然后擦擦嘴，看向劳伦斯：“货物清单呢？”", "罗德现在的心思都还在领地上。"),
    ("原文七（种田的门道随用随交代）",
     "“欧拓，你们在这样的土地上耕种，能丰收吗？”", "两米宽的空地则是防火带，防止烧地的时候一不小心蔓延成山火。"),
]
TAT = re.compile(r"实打实|实实在在|切切实实|货真价实|真真切切|结结实实|硬生生|猛地|死死|狠狠|整整|直往")


def han(s):
    return len(re.findall(r"[一-鿿]", s))


def main():
    mau = MAU.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n")
    khoi = []
    for ten, dau, cuoi in NGUYEN_VAN:
        i = mau.find(dau)
        j = mau.find(cuoi, i)
        if i < 0 or j < 0:
            raise SystemExit(f"Không thấy trong bộ mẫu: {ten} — {dau if i < 0 else cuoi}")
        doan = [l.strip(" 　") for l in mau[i:j + len(cuoi)].split("\n") if l.strip(" 　")]
        doan = [l for l in doan if not re.fullmatch(r"第\d+章.*", l)]  # tiêu đề chương khi đoạn vắt qua hai chương
        for l in doan:
            assert l in mau, l
        khoi.append(f"{ten}\n" + "\n".join(doan))
        print(f"{ten}: {len(doan)} dòng, {han(''.join(doan))} 字, tật trong anchor: {TAT.findall(''.join(doan)) or 'không'}")
    than = "\n\n".join(khoi)
    si = LOI.format(nguyen_van=than)
    RA.write_text(si, encoding="utf-8", newline="\n")
    print(f"{RA.relative_to(GOC).as_posix()} | {len(si)} ký tự | lời {len(si) - len(than)} | anchor {len(than)} ({100 * len(than) // len(si)}%)")


if __name__ == "__main__":
    main()
