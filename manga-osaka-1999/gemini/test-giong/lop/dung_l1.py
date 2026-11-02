"""Dựng hai biến mục 1 mới (lời giao việc) trên nền lõi + mục 3: A = anchor ch24 cũ, B = anchor ch29 (佐藤文也)."""
import json
import sys
from pathlib import Path

ROOT = Path(sys.argv[1])
D = 'manga-osaka-1999/gemini/test-giong/lop'
l13 = (ROOT / D / 'si-L-13.txt').read_text(encoding='utf-8')
a = l13.index('1. A character exists')
b = l13.index('MOMENTS')
cu = l13[a:b]
anchor_cu = cu[cu.index('Sample anchor:'):].rstrip() + '\n\n'

LOI = '''1. The people on the page bring their own wants; the prompt does not supply them.

A segment prompt gives events, facts and who is present. What each person privately wants is your part of the job, in every segment, for every named person who stays on the page for more than a few lines. Before writing, settle for each of them one small want of their own that the plot is not using — to be thanked for once, to be proven right, to look capable in front of someone, to catch the last train home, to spare someone an embarrassment. Let it surface wherever the plot leaves a gap: a thought they would not say aloud, a guess about the other person that runs ahead of the facts and pulls their own stake into it, a remark to themselves, a small decision they make and take back. It happens in the scene, now, through what they think and do, and the reader works out who they are from it.

'''
ANCHOR_MOI = '''Sample anchor:

```
听到这话，佐藤文也犹豫了：
“这个啊....我的这个朋友，脾气有点古怪，想要跟他交流的话，可能会有些困难。”
佐藤文也脑补了一下秋山悟跟士郎正宗见面的画面.....
堪比地狱。
那个家伙的脾气...如果有新晋漫画家去找他请教的话，指不定要讲出什么难听的话。
到时候把秋山君贬得一无是处，佐藤文也一定会为了维护秋山君，忍不住跟他对骂起来的！
```

Asked for an introduction, an artist pictures the meeting going to hell and finds herself in the middle of it, quarrelling on his side.

'''
out = {}
for k, anc in (('L-1A3', anchor_cu), ('L-1B3', ANCHOR_MOI)):
    s = l13[:a] + LOI + anc + l13[b:]
    (ROOT / D / f'si-{k}.txt').write_text(s, encoding='utf-8', newline='\n')
    out[k] = len(s)
print(out)
jobs = [{'si': f'{D}/si-{k}.txt', 'prompt': f'{D}/brief-ch01-tron.md', 'out': f'{D}/tron-{k}-{x}.md',
         'think_out': f'{D}/thinking-tron-{k}-{x}.md', 'note': f'brief tron, {k} ({x})'}
        for k in out for x in 'ab']
(ROOT / D / 'jobs-l1.json').write_text(json.dumps(jobs, ensure_ascii=False, indent=1), encoding='utf-8')
print(len(jobs))
