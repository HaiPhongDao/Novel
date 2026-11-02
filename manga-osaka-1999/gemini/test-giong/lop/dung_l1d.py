"""SI bản D: ROLE sửa (chuyện người trước, chuyện tiền sau) + mục 1 tách dòng + anchor ch01 (hút thuốc) và ch27 (nghẹn lời) + mục 3. Test trên ch27 brief trơn."""
import json
import sys
from pathlib import Path

ROOT = Path(sys.argv[1])
D = 'manga-osaka-1999/gemini/test-giong/lop'
base = (ROOT / D / 'si-L-1C3.txt').read_text(encoding='utf-8')
goc1 = (ROOT / 'chung/hieu-chuan/manga/ch01/goc.txt').read_text(encoding='utf-8').splitlines()
goc27 = (ROOT / '我在泡沫东京画漫画.txt').read_text(encoding='utf-8').splitlines()[2962:2967]

old_ctx = base[base.index('Genre context:'):base.index('The anchors below')]
new_ctx = ('Genre context: limited omniscient — narration stays with the POV character and steps into another person\'s head '
           'when a scene turns on how a manuscript, a situation, or a person is misjudged. Tension and comedy rest on the '
           'friction between ordinary human preoccupations and workplace reality: personal agendas during work hours, how '
           'people size each other up, polite masks versus private thoughts, alongside trade accounts (page rates, prize '
           'categories, deadlines, wages, B4 paper costs).\n\n')
s = base.replace(old_ctx, new_ctx)

a1 = '\n'.join(l.strip() for l in goc1[2:10]) + '\n```\n\n```\n' + '\n'.join(l.strip() for l in goc1[22:31])
a2 = '\n'.join(l.strip() for l in goc27)
m1 = f'''1. Writing the people is your job; the prompt only gives what happens.

The prompt says what happens and who is there. Who these people are is yours to build, in every scene, for everyone who stays on the page:

- What they want out of this moment that the plot does not need.
- How they read, or misread, the person in front of them, and what they think but keep to themselves.
- What their hands are doing while they wait or talk, and what they notice first.
- Background facts reach the page through someone's head — what those facts mean to that person, today — rather than through the storyteller.

By the end of the scene the reader knows each of them from what they did and thought, without having been told.

Sample anchor:

```
{a1}
```

An editor hiding from her desk guesses at a stranger, talks herself out of it, lets the bad times feed a selfish hope, and is let down when he turns out ordinary.

'''
a = s.index('1. Writing the people')
b = s.index('MOMENTS')
s = s[:a] + m1 + s[b:]
(ROOT / D / 'si-L-1D3.txt').write_text(s, encoding='utf-8', newline='\n')
print(len(s))
jobs = [{'si': f'{D}/si-L-1D3.txt', 'prompt': f'{D}/brief-ch27-tron.md', 'out': f'{D}/tron27-L-1D3-{x}.md',
         'think_out': f'{D}/thinking-tron27-L-1D3-{x}.md', 'note': f'brief ch27 tron, L-1D3 ({x})'} for x in 'ab']
(ROOT / D / 'jobs-l1d.json').write_text(json.dumps(jobs, ensure_ascii=False, indent=1), encoding='utf-8')
