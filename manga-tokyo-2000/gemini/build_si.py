# Dung SI cho manga-tokyo-2000: lay writer/SI-tong-hop.txt, thay 9 anchor bang nguyen van bo mau
# (lay theo so dong de khong go tay), viet lai doan WHY sau moi anchor, them muc GENRE.
import re, sys
ROOT = r"D:\ClaudeCode\Novel"
L = open(ROOT + r"\我在泡沫东京画漫画.txt", encoding="utf-8").read().split("\n")
NAMES = [("秋山悟","Akiyama Satoru"),("黑川碧","Kurokawa Midori"),("雾越未麻","Kirigoe Mima"),("松田佑希","Matsuda Yuki"),
         ("上杉雄大","Uesugi Yudai"),("秋山","Akiyama"),("黑川","Kurokawa"),("上杉","Uesugi"),("松田","Matsuda"),
         ("矢野","Yano"),("未麻","Mima"),("留美","Rumi"),("田所","Tadokoro")]
def romaji(t):
    for a, b in NAMES:
        t = t.replace(a, b)
    return t
def lines(a, b):  # so dong 1-based, ca hai dau; ten nguoi doi sang romaji (Tac gia 29/10)
    return romaji("\n".join(L[a-1:b]).rstrip() + "\n")

NEW = [
 (lines(125, 130),
  "The evening gets one short line; the watch and the quicker step share one line, because the glance and the reaction are one instant. The errand and what a delay costs him get the longest paragraph. Then the reason arrives in two pieces: a half-line that hangs on `——`, and a short exclamation that is his own verdict on his wallet."),
 (lines(48, 53),
  "The woman is shown in nouns: fringe, bun, stray hair, a nicotine-stained finger. The comparison belongs to him: a guess in his own words (a cleaner, maybe a former biker-gang empress back in the job market), and it is wrong, which is the joke the next chapters cash in."),
 (lines(479, 485),
  "He has done the sum, and the narration walks through it in his order: why changing jobs is the worst option right now, what moving out would cost in the cheapest wards, how much starting money he would need. Then the turn: he is not without capital, and the capital gets a line of its own."),
 (lines(222, 228),
  "Inside the editor's head: three labels in a row, her verdict in four characters, then her own tired logic about her job and her boss, in her words. The outward smile stays on her face while the narration says what she really thinks."),
 (lines(76, 81),
  "He squats down next to her as if nothing happened. She gives him a cigarette only after a visible struggle, since her pack is nearly empty, and when he refuses she is relieved. The scene's comedy comes from what she wants (to keep her last cigarettes), and the last line is her own private bargain."),
 (lines(414, 423),
  "The payoff is told through the reader: she asks herself what the last line means, gets goosebumps, tries two theories and rejects them, flips back to reread. Only the last line turns to the author sitting calmly across the desk."),
 (lines(1003, 1011),
  "The editor speaks a whole thought: her confidence first, then the turn, then a question that sets up a number. The number gets its own line. Between turns the narration explains the scale in plain facts, and her next turn finishes the reasoning in her own voice."),
 (lines(229, 233),
  "How heavy the manuscript is, how many pages, what paper it needs, what the paper costs, what the whole thing costs: each fact builds on the last. The final line turns the sum into her own verdict, still expecting the worst."),
 (lines(194, 202),
  "One character's inner rant ends the scene; the `……` line closes it. The next paragraph names the new place in a few characters, the one after already has the office in motion, and the protagonist is already walking to the desk."),
]

si = open(ROOT + r"\writer\SI-tong-hop.txt", encoding="utf-8").read()
parts = re.split(r"(```\n.*?```\n\n[^\n]*\n)", si, flags=re.S)
anchors = [p for p in parts if p.startswith("```\n")]
assert len(anchors) == 9, len(anchors)
out, k = [], 0
for p in parts:
    if p.startswith("```\n"):
        a, why = NEW[k]; k += 1
        out.append("```\n" + a + "```\n\n" + why + "\n")
    else:
        out.append(p)
si = "".join(out)

# Doan "comparison" anchor 2 trong SI goc co hai anchor o muc 4 va 2 o muc 3: giu nguyen cau dan.
si = si.replace(
 "Sample anchor excerpts appear below as style anchors, taken from several benchmark novels in different genres.",
 "Sample anchor excerpts appear below as style anchors, taken from the benchmark novel of this lane (a transmigrated manga artist in 1990s Tokyo).")
si = si.replace(
 "2. Names. Personal names, place names, organizations and techniques go into the prose exactly as the prompt writes them, in one fixed form throughout: a name the prompt spells in Latin letters stays in those Latin letters alone (Leon抬起手 · Varen城); a name the prompt gives in Chinese characters stays in those characters (沈砚点了点头 · 《千灯巷》).",
 "2. Names. People's names are written in Latin letters (romaji), exactly as the prompt and the State spell them, in one fixed form throughout: Hayakawa抬起头 · Morishita小姐 · Hayakawa君. In narration a person is usually called by the family name alone (Hayakawa, Morishita); the full name appears when they are introduced. Place names, companies and magazines are written in Chinese characters as the State gives them (中野, 集英社, 《周刊Young Jump》). The country is written 日本. Titles of works go in 《》 exactly as the prompt or the State gives them.")
assert "written in Latin letters (romaji)" in si and "this lane" in si

GENRE = """
PART 3 — THIS LANE: A MANGA ARTIST AND THE PEOPLE WHO READ HIM

1. The readers carry the payoff. The protagonist hands over a manuscript; the payoff happens inside the person reading it — an editor, a rival, an assistant, a judge. When the segment prompt names a reader for a reading scene, the narration stays in that reader's head for the whole reading: what they expected from a newcomer, what the first pages make them think, the guesses they make about where it goes, the guess that turns out wrong, the reread. The protagonist sits across the desk and is seen from outside until the reading ends.

2. A work is shown the way it reads. Retell the manga as its pages arrive: a short paragraph of what the panels show, a line of a character in the manga in quotes, then the reader's reaction in their own words, then the next pages. Panel language is welcome (特写、远景、跨页、分镜、翻到下一页). The reader judges craft in an editor's terms: pacing, how a newcomer usually fails, whether it can be ended, whether it fits the magazine.

Sample anchor:

```
""" + lines(266, 277) + """```

A line from inside the manga, then what happens in it in two short paragraphs, then the reader's two-word reaction and a gesture, then her professional judgment in one line.

3. The industry is a set of numbers and ranks. Prize money, page rates, deadlines, survey rankings, print runs, rent and loan payments, the rank of every person in the editorial room. The protagonist knows the future and the other characters do not: he plans with what he remembers, and the others explain the present to him in their own terms.
"""
anchor_end = si.rfind("PART 2 —")
si = si[:anchor_end] + GENRE.lstrip("\n") + "\n" + si[anchor_end:]

head = "SI — 我在千禧东京画漫画 (manga-tokyo-2000). Bản v1, 2026-10-29. Dựng từ writer/SI-tong-hop.txt, thay 9 anchor bằng nguyên văn bộ mẫu 我在泡沫东京画漫画 (tên người đổi sang romaji theo Tác giả) + thêm PART 3 (lane).\n\n===== BẮT ĐẦU SI =====\n\n"
open(ROOT + r"\manga-tokyo-2000\gemini\si-dan-gemini.txt", "w", encoding="utf-8").write(head + si.strip() + "\n\n===== HẾT SI =====\n")
open(ROOT + r"\manga-tokyo-2000\gemini\si-v1.txt", "w", encoding="utf-8").write(si.strip() + "\n")
print(len(si))
