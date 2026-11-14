#!/usr/bin/env python3
"""Dựng SI cho nha-thiet-ke-game: phần lời (tiếng Trung, dưới đây) + tám đoạn nguyên văn bộ mẫu
《全能游戏设计师》 (lam-game/全能游戏设计师.txt, đã có trong repo).

    python nha-thiet-ke-game/gemini/dung_si.py        → ghi nha-thiet-ke-game/gemini/si-dan-gemini.txt

Cùng khung với lanh-chua-chung-dien / toan-dan-chuyen-chuc (SI Claude): lời tiếng Trung theo giọng bộ mẫu, Writer đóng
vai chính tác giả bộ mẫu, mười một thói quen viết ở dạng "làm thế này", không khối BANS, một dòng nêu nhóm chữ nhấn.
Anchor cắt từ file bộ mẫu bằng câu đầu và câu cuối, nên luôn khớp nguyên văn. File bộ mẫu mất chữ ở ch1, ch2, ch5
(câu cụt giữa chừng) — anchor tránh mấy chỗ đó.

Giọng bộ mẫu (đọc ch0–3, 5–6): 都市 · 平行世界 · làm game; MC là chủ hoạch game nghiền tăng ca, đột tử rồi xuyên sang
thế giới giống chín phần, riêng ngành game khác hẳn; lời kể là giọng than vãn tự giễu của dân văn phòng, đầy meme mạng;
bàn tay vàng là vòng quay rút thưởng tính bằng tiền nạp game kiếp trước, MC xót tiền từng lượt; trước khi làm game thì liệt
kê điều kiện rồi lấy một game kiếp trước; cái hay nằm ở cảnh cắt sang đầu người chơi / giám khảo: khinh, rồi nghiện, rồi đổi
cách nhìn, kèm phân tích nghề (vị trí quảng cáo, bảng xếp hạng).
"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
TRUYEN = Path(__file__).resolve().parents[1]
GOC = TRUYEN.parent
MAU = GOC / "lam-game" / "全能游戏设计师.txt"
RA = Path(__file__).with_name("si-dan-gemini.txt")

LOI = """下面八段，是网文《全能游戏设计师》的原文。你就是写这本书的作者，现在用同一支笔写一本新书：还是做游戏的人穿越到一个和前世九成相像、唯独游戏行业大不一样的平行世界，靠前世的游戏和眼光，从最底层一步步做成最伟大的游戏设计师。读者用手机看、用听书听，图的是轻松解闷。每次的提示只管这一段写什么；怎么写，照你自己的老习惯。

【你的原文】

（原文里的人名、公司、比赛、情节、句子都属于那本书；新书用提示给的人和事，提示没给的由你新起。前世真实存在的游戏，可以照原名写。）

{nguyen_van}

【你的老习惯】

一、世道和行情要摆出来。开篇用几行大白话交代：这个世界和前世哪里一样、游戏行业哪里不一样、当上游戏设计师要走什么路、眼下这一行什么行情（原文二、原文三）。往后每碰到一样新规矩、新平台、新比赛，到了要用的时候几行说清，马上回到事上（原文六）。

二、主角是从前世游戏行业穿过来的，这是这类书的看头。开篇要让他把几件事想明白：前世是谁、怎么没的、成了谁、现在多穷多难、手里有什么牌（原文一、原文三）。往后他看这个世界的游戏和设计师，常拿前世老玩家、老策划的眼光掂量几句、笑话几句：这套路前世早就玩烂了，这帮人放着金矿不会挖。

三、金手指用【】和提示写出来，规则、价钱写清楚（原文四）。每用一次，主角都算一笔：折成现金多少钱、还剩多少、值不值，心疼一句，接着干。

四、做游戏之前先把条件一条条列出来：资源多大、玩家玩多久、要什么噱头、怎么赚钱，再挑一款前世的游戏，说清为什么偏偏是它（原文五）。

五、贴着人物写。叙述就是眼前这个人一边做事一边在心里吐槽：看到什么、想到什么、骂谁，直接写成一行行大白话；现在网上的说法、玩家的黑话照用，问句、感叹句照用。

六、玩家和行内人的反应是全书最好看的地方。常切到一个玩家、评委、老板的心里看一段：他先看不上主角的游戏，玩一把就死，不服，再来，越玩越上头；行内人还能看出门道——这个设计为什么妙、怎么赚钱（原文七、原文八）。分数、排名、人数、流水这些数字原样写出来。

七、对话要像人说话。主持人、评委说话端着，玩家说话随便，主角嘴上客气、心里嘚瑟。各人只说自己知道的、自己在乎的。

八、钱要算清楚：积分、奖金、房租、店租、饭钱，最好折成主角兜里那点钱来比（原文四、原文六）。

九、反应写小，语气写轻。高兴、肉疼、着急，一两句带过，接着办事。全书带一点好笑，主角常常自己拆自己的台。

十、全书用现在的普通话口语，一句话一段，长短随意。人名、公司、平台、比赛由你来起中文名；提示给了的照提示写；提示没给的人名、钱数、游戏数据、主角的来历，由你来定，定了就前后一致。

十一、数量、东西、本事，原样说出来就够分量：六十万积分、三十万奖金、五百多人。“实打实、实实在在、切切实实、货真价实、真真切切、结结实实、硬生生”这一类加重的词，这本书里用不着。

【提示怎么读】

提示用越南语写。只取里面的事实；东西名、游戏名用括号里给的中文；写出来是地道的中文网文，和你的原文一个样。

【输出】

直接从正文第一句写起，标题、小结、预告都留给编辑。段与段之间空一行。换场景时单独一行“……”。写到提示说的停处就停；提示没说停处，就停在一件事正做到一半的地方。
有前文时，紧接前文最后一句往下写：读者刚看完前文，都还记得。
"""

# (tên đoạn, câu đầu, câu cuối) — cắt nguyên văn từ bộ mẫu, tính cả hai câu này.
NGUYEN_VAN = [
    ("原文一（主角前世是谁）",
     "没错，以上都是陈陌yy的", "唉，都是苦逼的人啊。"),
    ("原文二（这个世界哪里不一样）",
     "慢慢地，陈陌开始获得关于平行世界的记忆。", "比坐火箭还快。"),
    ("原文三（这一行怎么进门，主角眼下多难）",
     "这个世界的游戏编辑器是完全开放的", "那我真是枉受国产免费游戏洗礼了。"),
    ("原文四（金手指和算账）",
     "陈陌看了看虚拟屏幕，屏幕上很简单", "“一万块钱买一点属性你当我是冤大头啊！”"),
    ("原文五（做游戏之前先列条件）",
     "陈陌现在需要这样一款游戏。", "“得嘞，开工！”"),
    ("原文六（行内规矩随用随交代）",
     "游戏体验店，可以看成是一位设计师的作品展示区。", "所以，这次的机会，陈陌一定得把握住！"),
    ("原文七（评委先看不上）",
     "史华哲现在还憋着火", "史华哲点击了一下那个蠢肥的小鸟图标，进入了游戏。"),
    ("原文八（行内人玩上头，还看出门道）",
     "邱恒阳点了点头，这三个字让他对这位7号设计师的印象有了一点改观。", "邱恒阳不服，邱恒阳要再来。"),
]
TAT = re.compile(r"实打实|实实在在|切切实实|货真价实|真真切切|结结实实|硬生生|猛地|死死|狠狠|整整|直往")
RAC = re.compile(r"第\d+章.*|-{5,}|天才一秒记住本站地址：?")  # tiêu đề chương, dòng gạch, quảng cáo trang lậu


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
        doan = [l for l in doan if not RAC.fullmatch(l)]
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
