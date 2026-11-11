#!/usr/bin/env python3
"""Dựng SI cho manga-bong-bong: phần lời (tiếng Trung, dưới đây) + bảy đoạn nguyên văn bộ mẫu 《我在泡沫东京画漫画》.

    python manga-bong-bong/gemini/dung_si.py        → ghi manga-bong-bong/gemini/si-dan-gemini.txt

Anchor không gõ tay: mỗi đoạn cắt từ file bộ mẫu bằng câu đầu và câu cuối, nên luôn khớp nguyên văn.
Cùng khung với SI Claude của han-nien-san-dong / luu-dan (xem han-nien-san-dong/gemini/si-claude.md), viết lại theo giọng
bộ mẫu này: lời kể luân phiên giữa MC và người đối diện, người đối diện hay đoán sai về MC.
"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
GOC = Path(__file__).resolve().parents[2]
MAU = GOC / "我在泡沫东京画漫画.txt"
RA = Path(__file__).with_name("si-dan-gemini.txt")

LOI = """下面七段，是网文《我在泡沫东京画漫画》的原文。你就是写这本书的作者，现在用同一支笔写一本新书：还是穿越者落在日本漫画这一行里，从最底层一步步往上走。读者用手机看、用听书听，图的是轻松解闷。每次的提示只管这一段写什么；怎么写，照你自己的老习惯。

【你的原文】

（原文里的人名、作品、情节、句子都属于那本书；新书用提示给的人和事，提示没给的由你新起。）

{nguyen_van}

【你的老习惯】

一、世道和行情要摆出来。开篇，以及每到一个新地方、每进一个新行当，用一小段大白话交代：这是哪一年、世道怎么样、这一行眼下什么行情——像原文一那样，几行，带着人物自己的看法。

二、主角是从后来穿过来的，这是这类书的看头。开篇要让他把几件事想明白：自己从哪年来、成了谁、落在哪一年、手里有什么牌、打算怎么走（原文二、原文三）。往后他看这个年代的人和事，常拿后来人的眼光掂量几句、笑话几句：哪部作品日后会火、哪个行情要来、哪种做法过几年就没人用了。他做的选择旁人看不懂，他自己心里有数。

三、贴着人物写。叙述就是眼前这个人一边经历一边在心里嘀咕：看到什么、想起什么、算什么账、笑话谁，直接写成一行行大白话，问句、感叹句照用。大半篇幅跟着主角；有时切到他对面那个人的心里看一小段——那人多半把主角看低了、猜错了，在打自己的小算盘。主角嘴上说出来的是这个年代的人话。

四、一句话一段。一行一个动作、一句话、一个念头，碎句也行。

五、场景靠谁做了什么、说了什么、算了什么账往前走。重要人物出场，两三行写清年纪、穿着、长相、身份。东西直接叫名字。数字和动作原样写：七万円、六十页、看着、拿着。

六、反应写小，语气写轻。人物听到好事坏事，都是愣一下、皱皱眉、松一口气、嘟囔一句，用最平常的词一句带过，接着说话办事。日子紧巴，一两行说清，人物接着想办法。全书带一点好笑。

七、对话要多，要像人说话。开口、请求、解释，都是对着眼前的人说的完整句子，带称呼和客气话（桑、君、小姐、老师、先生）；回答可以短。一问一答接得上，会闲聊几句再说正事。各人只说自己知道的、自己要的。

八、事情有来有回。对面的人有自己的难处和打算，要掂量、要还价、要拖一拖；主角面上坦率客气、不急不恼，心里有后来人的眼光和自己的小算盘。好看的地方在旁人先看低他、再一点点改观。

九、行内的事随用随交代。奖金多少、稿纸多贵、助手和老师是什么规矩、编辑部怎么运转，到了要用的那一刻，用两三行大白话说清，马上回到事上。钱数最好换算成主角的工资和房租。

十、全书用现在的普通话口语。人名一律用罗马字写，不写汉字，和原文里一样：Sawada Kazuki、Mizuno 小姐、Hasegawa 老师；地名、出版社、杂志、作品名写中文，金额用円。提示给了的照提示写；提示没给的人名、杂志、作品、钱数、主角的来历，由你来定，定了就前后一致。

十一、数量、东西、本事，原样说出来就够分量：七万円、六十页、一份连载。“实打实、实实在在、切切实实、货真价实、真真切切、结结实实、硬生生”这一类加重的词，这本书里用不着。

【提示怎么读】

提示用越南语写。只取里面的事实；提示里的人名照罗马字原样写，东西名用括号里给的中文；写出来是地道的中文网文，和你的原文一个样。

【输出】

直接从正文第一句写起，标题、小结、预告都留给编辑。段与段之间空一行。换场景时单独一行“……”。写到提示说的停处就停；提示没说停处，就停在一件事正做到一半的地方。
有前文时，紧接前文最后一句往下写：读者刚看完前文，都还记得。
"""

# (tên đoạn, câu đầu, câu cuối) — cắt nguyên văn từ bộ mẫu, tính cả hai câu này.
NGUYEN_VAN = [
    ("原文一（这是哪一年，世道怎么样）", "92年初，曰本泡沫经济破裂。", "有时候黑川碧，甚至多少有点能够理解那些堕落的变态了。"),
    ("原文二（主角从哪来，怎么看这个年代）", "是的，秋山悟并不是属于这个时代的人...甚至不属于这个国家。", "明明是白景最为向往的年代，可真让他来，他还不乐意了！"),
    ("原文三（他手里的牌：后来的作品）", "但好在，秋山悟也不是毫无资本。", "现在，带着今敏老师3年后创作的这部轰动世界的作品，秋山悟来了。"),
    ("原文四（两个人头一回说话）", "“你是？”秋山悟停住脚步。", "若秋山悟真是来蹭烟的，那还不如让他上去了呢。"),
    ("原文五（对面的人在心里猜错了他）", "“真的是你呀...秋山君，真是好久不见了！”", "而且，谁会把学生时代的约定真当一回事啊？"),
    ("原文六（行内人看稿，顺手交代行情）", "接过稿纸，映入眼帘的，是封面的标题——", "嗯，精装大粪。"),
    ("原文七（吃饭闲聊）", "两人往烧鸟居酒屋里走去", "“那再来两杯生啤！”"),
]
TAT = re.compile(r"实打实|实实在在|切切实实|货真价实|结结实实|硬生生|猛地|死死|狠狠|整整|直往")


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
        doan = [l for l in doan if not re.fullmatch(r"[.…。]+", l)]  # dòng chấm chuyển cảnh của bộ mẫu
        for l in doan:
            assert l in mau, l
        khoi.append(f"{ten}\n" + "\n".join(doan))
        print(f"{ten}: {len(doan)} dòng, {han(''.join(doan))} 字, tật trong anchor: {TAT.findall(''.join(doan)) or 'không'}")
    than = "\n\n".join(khoi)
    # Tên riêng trong anchor đổi thành Romaji (ngẫu nhiên)
    for cu, moi in [
        ("秋山悟", "Sawada Kazuki"),
        ("秋山君", "Sawada 君"),
        ("秋山桑", "Sawada 桑"),
        ("黑川碧", "Mizuno Aya"),
        ("黑川老师", "Mizuno 老师"),
        ("黑川小姐", "Mizuno 小姐"),
        ("松田佑希", "Kondo Ryota"),
        ("矢野", "Taguchi"),
        ("上杉先生", "Hasegawa 先生"),
        ("上杉老师", "Hasegawa 老师"),
        ("上杉工作室", "Hasegawa 工作室"),
        ("秋山", "Sawada"),
        ("上杉雄大", "Hasegawa Daigo"),
        ("上杉", "Hasegawa"),
        ("白景", "Lin Yuan"),
        ("今敏", "Kon Satoshi"),
        ("鸟山明", "Toriyama Akira"),
        ("富坚义博", "Togashi Yoshihiro"),
        ("井上雄彦", "Inoue Takehiko"),
    ]:
        than = than.replace(cu, moi)
    than = re.sub(r'([\u4e00-\u9fff])([A-Za-z])', r'\1 \2', than)
    than = re.sub(r'([A-Za-z])([\u4e00-\u9fff])', r'\1 \2', than)
    than = than.replace("Kurokawa Midori“", "Kurokawa Midori “")
    than = than.replace("专业的 B4 原稿纸", "专业的B4原稿纸")
    than = than.replace("专业的 B4原稿纸", "专业的B4原稿纸")
    than = re.sub(r'  +', ' ', than)
    si = LOI.format(nguyen_van=than)
    RA.write_text(si, encoding="utf-8", newline="\n")
    print(f"{RA.relative_to(GOC).as_posix()} | {len(si)} ký tự | lời {len(si) - len(than)} | anchor {len(than)} ({100 * len(than) // len(si)}%)")


if __name__ == "__main__":
    main()
