"""Dựng SI lõi (ROLE + FIXED + PART 3) và các biến thể lõi + đúng một khối, cho phép thử từng khối trên ch01."""
import json
import sys
from pathlib import Path

ROOT = Path(sys.argv[1])
src = (ROOT / 'manga-osaka-1999/gemini/test-giong/si-truoc-go-I0025.txt').read_text(encoding='utf-8')
L = src.split('\n')


def seg(a, b):
    return '\n'.join(L[a - 1:b - 1]).strip('\n')


role = seg(1, 15)
part1h = 'PART 1 — STYLE'
narr = seg(17, 34)
m1 = seg(34, 51)
m2 = seg(51, 66)
mom = seg(66, 68).strip()
m3 = seg(68, 84)
m4 = seg(84, 99)
p2 = seg(99, 107)
bans = seg(107, 115)
p3 = '\n'.join(L[114:]).strip('\n')
assert role.startswith('ROLE') and narr.startswith('NARRATION') and m1.startswith('1.') and m2.startswith('2.')
assert mom.startswith('MOMENTS') and m3.startswith('3.') and m4.startswith('4.') and p2.startswith('PART 2')
assert bans.startswith('BANS') and p3.startswith('PART 3')

# mục 1: anchor đang lấy từ ch01 — ch01 là bài kiểm tra, nên đổi sang anchor ch24 (bản trước 11454e0)
old_a = m1[m1.index('```'):]
new_a = '''```
如果上杉明菜有一个在某集团担任会长的亲爹，以他这势利眼和欺软怕硬的性格，确实会是这样的姿态。
......不，要是秋山悟一早知道，上杉明菜是富二代的话，说不定只会比这家伙还要舔！
瞬间，秋山悟的脑海中，脑补出了一个劲爆大戏：作为集团千金大小姐的上杉明菜为了追逐梦想，独自来到漫画家叔叔的工作室打杂。首富老爷子却一心想要让她继承家族企业，不惜派人堵门，哪怕使用暴力，也要将她接回。
```

The observer invents a whole absurd drama about someone across the room and half-believes it; the invention, not a verdict, is what shows a mind at work.'''
m1 = m1.replace(old_a, new_a)
assert '做点什么' not in m1

V = {
    'L': [], 'L-N': [part1h, narr], 'L-1': [part1h, m1], 'L-2': [part1h, m2],
    'L-3': [part1h, mom, m3], 'L-4': [part1h, mom, m4], 'L-P2': [p2], 'L-B': [bans],
}
out = ROOT / 'manga-osaka-1999/gemini/test-giong/lop'
out.mkdir(parents=True, exist_ok=True)
rel = 'manga-osaka-1999/gemini/test-giong/lop'
jobs = []
for k, blocks in V.items():
    t = '\n\n'.join([role] + blocks + [p3]) + '\n'
    (out / f'si-{k}.txt').write_text(t, encoding='utf-8', newline='\n')
    print(f'{k:5} {len(t):5} ký tự')
    for x in 'ab':
        jobs.append({'si': f'{rel}/si-{k}.txt', 'prompt': 'chung/hieu-chuan/manga/ch01/brief.md',
                     'out': f'{rel}/ch01-{k}-{x}.md', 'think_out': f'{rel}/thinking-ch01-{k}-{x}.md',
                     'note': f'lop {k} ({x})'})
Path(sys.argv[2]).write_text(json.dumps(jobs, ensure_ascii=False, indent=1), encoding='utf-8')
print(len(jobs), 'việc')
