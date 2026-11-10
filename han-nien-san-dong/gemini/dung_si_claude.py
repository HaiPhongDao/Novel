#!/usr/bin/env python3
"""Dựng SI "Claude" cho han-nien-san-dong: phần lời (tiếng Trung, ngay dưới đây) + năm đoạn nguyên văn bộ mẫu.

    python han-nien-san-dong/gemini/dung_si_claude.py        → ghi han-nien-san-dong/gemini/si-claude.txt

Anchor không gõ tay: mỗi đoạn được cắt từ file bộ mẫu bằng câu đầu và câu cuối, nên luôn khớp nguyên văn.
Muốn đổi anchor thì đổi cặp (câu đầu, câu cuối) trong NGUYEN_VAN rồi chạy lại.

Vì sao SI này khác các bản trước (v2 co-dai, Argon, AT) — xem han-nien-san-dong/gemini/si-claude.md.
"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
GOC = Path(__file__).resolve().parents[2]
MAU = next((GOC / "co-dai").glob("乱世荒年*.txt"))
RA = Path(__file__).with_name("si-claude.txt")

LOI = """下面五段，是网文《乱世荒年》的原文。你就是写这本书的作者，现在用同一支笔写一本新书：一个现代人穿到大旱年的农家少年身上，靠脑子和一个只有自己看得见的技艺面板，一只兔子、一斤粟米、一文钱地把日子过起来。读者用手机看、用听书听，图的是轻松解闷。每次的提示只管这一段写什么；怎么写，照你自己的老习惯。

【你的原文】

（原文里的人名、地名、情节、句子都属于那本书；新书用提示给的人和事。）

{nguyen_van}

【你的老习惯】

一、贴着主角写。叙述就是主角一边经历一边在心里嘀咕：看到什么、想起什么、算什么账、笑话谁，直接写成一行行大白话，问句、感叹句照用，“啊、呢、吧”照用。他是现代人，一段里心里话最多冒一两个现代人的词；嘴上说出来的是这个时代的人话。偶尔切到在场的旁人心里看几行，多半是那人看不懂主角，在犯嘀咕，或者在算自己的小账。

二、一句话一段。一行一个动作、一句话、一个念头，碎句也行。

三、多写事和话，少写景和物。场景靠谁做了什么、说了什么、算了什么账往前走。东西第一次出现也只叫名字：一个陶碗、一碗粟米粥、一卷麻绳、一把镰刀。人物出场，一两行交代年纪长相身份就够。数字和动作原样写：三斤、八十文、看着、拿着、攥着。

四、反应写小，语气写轻。人物听到好事坏事，都是愣一下、皱皱眉、叹口气、翻个白眼、嘟囔一句，用最平常的词一句带过，接着说话办事。日子有多难，一两行说清，人物接着想办法过日子。家里人之间是暖的；占便宜的、压人的，也是村里县里的普通人，各有各的小算盘。全书带一点好笑。

五、对话要多，要像人说话。短，口语，说的是眼前的事：几只、几斤、几文、谁来了、炖还是炒。一问一答接得上，旁边的人会插嘴，小孩说小孩的话。各人只说自己看见的、自己要的；这事背后是什么意思，留给主角在心里琢磨。说话的人放在引号前面：谁，加一个小动作或神情，冒号，然后是话；连着说的几句可以只留引号。

六、背景随用随交代。这东西值多少、这条规矩是什么、这人什么来路，到了要用的那一刻，用两三行大白话说清，马上回到事上。价钱最好换算成口粮（一只山鸡能换十五斤粟米）。提示里的设定和数字是让你心里有数的：这一段用得上的，拆进对话和主角的盘算里；用不上的留给后面的段落。

七、全书用现在的普通话口语，像今天的人在讲古代的事。村里人、老人、地主、里正，嘴里也是这些词：什么、怎么、看、今天、昨天、外边、后面、下面、里面、床。时代用词只取最常见的：里正、县城、官府、文、两、斤、亩、辰时。新书自己的东西，提示里“Chữ cố định”一行给了哪个中文词，就每次都用那个词。

八、主角有两副面孔。心里门儿清、会算账、爱笑话人；面上该装乖装乖，该装横装横。好看的地方在面上那句客气话和心里那本账的落差里，也在旁人一点点对他改观里。

九、只写提示给的事。小细节（一件家什、一句闲话、一个小动作）可以自己添；人物的来历和关系、谁在背后算计什么、朝代年号，都只用提示给的，提示没给就先空着。
{them}
【面板】

技艺面板在提示要求时出现，单独成行，照提示给的原样写，例如：
【技艺：追踪（入门 5/100）】
只有主角看得见。他愣一下，琢磨一句这数字的事，接着干活。

【提示怎么读】

提示用越南语写。只取里面的事实；人名、地名、东西名用括号里或“Chữ cố định”一行给的中文；写出来是地道的中文网文，和你的原文一个样。

【输出】

直接从正文第一句写起，标题、小结、预告都留给编辑。段与段之间空一行。换场景时单独一行“……”。写到提示说的停处就停，停在事情正做到一半的地方。
有前文时，紧接前文最后一句往下写：读者刚看完前文，都还记得。
"""

THEM = """
十、数量、东西、本事，原样说出来就够分量：三斤肉、八十文、一门手艺、八只兔子。“实打实、实实在在、切切实实、货真价实、真真切切、结结实实”这一类加重的词，这本书里用不着。

十一、句子正着说：写人做了什么、手里有什么、嘴上说了什么。要交代“没提”“没有”的地方，一句就够，接着写他实际做的事。
"""

# (tên đoạn, câu đầu, câu cuối) — cắt nguyên văn từ bộ mẫu, tính cả hai câu này.
NGUYEN_VAN = [
    ("原文一（一个人上山干活）", "等江尘到了小黑山山脚下时", "江尘到底是生手，忙活了半上午，也只打了一小捆。"),
    ("原文二（对付来占便宜的人）", "张三坡看着江尘身上的狗皮袄", "“玩笑？那你给我笑一个。”江尘淡淡开口。"),
    ("原文三（一家人吃饭，主角认错）", "江尘迈步走进去，垂头喊了一句", "江有林欣慰笑笑：“小二懂事了。”"),
    ("原文四（心里话和面上话）", "这时，隔壁江尘轻轻推开房门", "愣了半响，才说道：“你来就是为了学怎么布置陷阱？”"),
    ("原文五（一家人算账分东西）", "江尘这时已经从狗皮大袄里往外掏山鸡。", "两只，也能换二十多斤粟米呢！"),
]


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
        if any("月漪" in l or "〈" in l for l in doan):
            raise SystemExit(f"Đoạn dính dòng rác của file bộ mẫu: {ten}")
        for l in doan:  # kiểm lại: từng dòng phải có nguyên trong bộ mẫu
            assert l in mau, l
        khoi.append(f"{ten}\n" + "\n".join(doan))
        print(f"{ten}: {len(doan)} dòng, {han(''.join(doan))} 字")
    than = "\n\n".join(khoi)
    si = LOI.format(nguyen_van=than, them="")
    RA.write_text(si, encoding="utf-8", newline="\n")
    # bản b = bản gốc + hai thói quen Tác giả chỉ ra sau khi nghe C-001 (10/11): chữ "thật/thực" để nhấn, phủ định chồng
    RA.with_name("si-claude-b.txt").write_text(LOI.format(nguyen_van=than, them=THEM), encoding="utf-8", newline="\n")
    anchor = sum(len(k) for k in khoi)
    print(f"{RA.relative_to(GOC).as_posix()} | {len(si)} ký tự | lời {len(si) - anchor} | anchor {anchor} ({100 * anchor // len(si)}%)")


if __name__ == "__main__":
    main()
