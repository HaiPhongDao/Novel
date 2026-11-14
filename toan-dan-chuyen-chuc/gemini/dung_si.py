#!/usr/bin/env python3
"""Dựng SI cho toan-dan-chuyen-chuc: phần lời (tiếng Trung, dưới đây) + bảy đoạn nguyên văn bộ mẫu
《全民转职：我神器词条无限叠加》 (飞雪连夭).

    python toan-dan-chuyen-chuc/gemini/dung_si.py        → ghi toan-dan-chuyen-chuc/gemini/si-dan-gemini.txt

Bộ mẫu không commit (3,7 MB). Script đọc `mau/全民转职：我神器词条无限叠加.txt`; nếu không có thì lấy thẳng từ lịch sử
git (commit 3b9d02d trên nhánh vong-du, nơi file từng được tải lên 27/10), nên clone nào cũng dựng lại được.

Cùng khung với lanh-chua-chung-dien / manga-bong-bong (SI Claude): lời tiếng Trung theo giọng bộ mẫu, Writer đóng vai
chính tác giả bộ mẫu, mười một thói quen viết ở dạng "làm thế này", không khối BANS, một dòng nêu nhóm chữ nhấn.
Anchor cắt từ file bộ mẫu bằng câu đầu và câu cuối, nên luôn khớp nguyên văn.

Giọng bộ mẫu (đọc ch1–4, 8): 小白文 toàn dân chuyển chức; dòng rất ngắn, một ý một dòng; thế giới và luật chơi nói
thẳng bằng lời kể và bằng lời người trong truyện (thị trưởng phát biểu, người qua đường bàn tán); bàn tay vàng và
trang bị hiện bằng bảng 【】 với con số, MC tính ngay mạnh gấp mấy lần người khác; tiền tính tới từng đồng; đám đông
xem thường MC rồi bị một con số trên bảng thông báo vả mặt.
"""
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
TRUYEN = Path(__file__).resolve().parents[1]
GOC = TRUYEN.parent
MAU = TRUYEN / "mau" / "全民转职：我神器词条无限叠加.txt"
MAU_GIT = "3b9d02d:vong-du/全民转职：我神器词条无限叠加.txt"
RA = Path(__file__).with_name("si-dan-gemini.txt")

LOI = """下面七段，是网文《全民转职：我神器词条无限叠加》的原文。你就是写这本书的作者，现在用同一支笔写一本新书：还是穿越者落到一个人人十八岁转职、魔兽横行、靠刷副本升级的世界，开局职业不被看好，凭一样谁也不知道的金手指一路升级、刷怪、发财、打脸。读者用手机看、用听书听，图的是爽快解闷。每次的提示只管这一段写什么；怎么写，照你自己的老习惯。

【你的原文】

（原文里的人名、地名、职业、装备、情节、句子都属于那本书；新书用提示给的人和事，提示没给的由你新起。）

{nguyen_van}

【你的老习惯】

一、世道和规矩要摆出来。开篇用几行大白话交代：这个世界是什么样、转职是怎么回事、职业分几等、副本和金币怎么回事、普通人和有背景的人差在哪（原文一）。也可以借台上讲话的人、台下闲聊的人嘴里说出来。往后每碰到一样新规矩、新地方，到了用的时候几行说清，马上回到事上（原文四）。

二、主角是从地星穿过来的，这是这类书的看头。开篇要让他把几件事想明白：前世是谁、在这个世界活了多少年、现在是什么身份、处境多难、手里有什么牌（原文二）。往后他看这个世界的人和事，常拿地星人、老玩家的眼光掂量几句、笑话几句：这套路前世游戏里见多了，这帮人放着好东西不会用。

三、金手指和装备用【】写出来：名字、等级、品质、属性、效果，一条一行，数字写清楚（原文五）。主角看完马上算一笔：比别人强几倍、能打多大范围、要花多少材料，再在心里喊一句“这也太离谱了吧”。

四、一行一句。一个动作、一句话、一个念头就是一行，句子可以断成几截，读起来快。

五、钱和材料要算账。余额多少，买什么花多少，剩多少，用【】写交易提示（原文六）。主角心疼一句，马上想明白值不值，接着干。

六、旁人先看低他，再被打脸（原文三、原文七）。围观的学生、老师、路人七嘴八舌，一人一句：有人可惜、有人幸灾乐祸、有人吹自己家的天才、有人猜来猜去全猜错。打脸要靠摆出来的东西：一条公告、一块记录碑、一个通关时间，旁人当场脑子宕机。主角本人话少，心里有数，不急着解释。

七、对话要多，要像现在的年轻人说话：卧槽、就这？、离谱。老师和领导说话端着，学生说话随便。各人只说自己知道的、自己在乎的。

八、打怪、刷副本写得快：几行交代怪物和难度，主角一出手就结束，然后是掉落、经验、升级的提示。

九、反应写短。惊喜、心疼、吃惊，一两句短话喊出来就过去，接着办事。

十、全书用现在的普通话口语。人名是中文名，城市、学校、协会、副本用中文起名；钱用金币。提示给了的照提示写；提示没给的人名、职业、装备、数值、钱数、主角的来历，由你来定，定了就前后一致，数值前后对得上。

十一、数量、东西、本事，原样说出来就够分量：一万金币、六秒、一百米范围。“实打实、实实在在、切切实实、货真价实、真真切切、结结实实、硬生生”这一类加重的词，这本书里用不着。

【提示怎么读】

提示用越南语写。只取里面的事实；东西名、地名用括号里给的中文；写出来是地道的中文网文，和你的原文一个样。

【输出】

直接从正文第一句写起，标题、小结、预告都留给编辑。段与段之间空一行。换场景时单独一行“……”。写到提示说的停处就停；提示没说停处，就停在一件事正做到一半的地方。
有前文时，紧接前文最后一句往下写：读者刚看完前文，都还记得。
"""

# (tên đoạn, câu đầu, câu cuối) — cắt nguyên văn từ bộ mẫu, tính cả hai câu này.
NGUYEN_VAN = [
    ("原文一（这个世界怎么运转）",
     "这个世界魔兽横行，万族林立，人族只是其中一个种族。", "而是需要通过不断升级，获得提升。"),
    ("原文二（主角从哪来，手里有什么牌）",
     "前世，他是地星的人。", "那应该不会太差吧？"),
    ("原文三（旁人看低他，提示弹出来）",
     "“唉，好端端的一个苗子，怎么觉醒的武装者？”", "【武装者已晋升为：神装者】"),
    ("原文四（规矩随用随交代）",
     "被划分在B级的战斗职业。", "不能以道理计算。"),
    ("原文五（看面板，当场算一笔）",
     "“巨剑类神器……”", "相当于每次平A，都是别人5倍的伤害。"),
    ("原文六（花钱算账）",
     "“对于60级的二转大地法师而言，五万金币或许不算什么。”", "九万金币，可以买一件神器的话，这已经算是血赚了。"),
    ("原文七（众人议论，记录碑打脸）",
     "【哭泣森林（噩梦难度）——副本最快通关记录已刷新！】", "这怎么做到的？"),
]
TAT = re.compile(r"实打实|实实在在|切切实实|货真价实|真真切切|结结实实|硬生生|猛地|死死|狠狠|整整|直往")


def han(s):
    return len(re.findall(r"[一-鿿]", s))


def doc_mau():
    if MAU.exists():
        return MAU.read_text(encoding="utf-8", errors="replace")
    r = subprocess.run(["git", "-C", str(GOC), "show", MAU_GIT], capture_output=True)
    if r.returncode:
        raise SystemExit(f"Không có {MAU} và không lấy được {MAU_GIT} từ git (git fetch origin vong-du?)")
    return r.stdout.decode("utf-8", errors="replace")


def main():
    mau = doc_mau().replace("\r\n", "\n")
    khoi = []
    for ten, dau, cuoi in NGUYEN_VAN:
        i = mau.find(dau)
        j = mau.find(cuoi, i)
        if i < 0 or j < 0:
            raise SystemExit(f"Không thấy trong bộ mẫu: {ten} — {dau if i < 0 else cuoi}")
        doan = [l.strip(" 　") for l in mau[i:j + len(cuoi)].split("\n") if l.strip(" 　")]
        doan = [l for l in doan if not re.fullmatch(r"第\d+章.*|-{5,}", l)]  # tiêu đề chương, dòng gạch của bộ mẫu
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
