"""SI E+BANS+S: thêm mục người kể (khung v6 ô 2, kiểu b storyteller), anchor ch104 dòng 44–51. Test ch107 brief trơn, so với E+BANS."""
import json
import sys
from pathlib import Path

ROOT = Path(sys.argv[1])
D = 'manga-osaka-1999/gemini/test-giong/lop'
eb = (ROOT / D / 'si-L-1E3B.txt').read_text(encoding='utf-8')
goc = (ROOT / D / 'ch104/goc.txt').read_text(encoding='utf-8').splitlines()
anchor = '\n'.join(l.strip() for l in goc[43:51])

muc = f'''2. A storyteller tells it, and the storyteller is on the protagonist's side.

The storyteller is a voice of its own on the page. Right after a line of dialogue or a small action, it steps in whenever the reader needs more than the scene shows: what a person's last weeks have been like and why this moment presses on them, how the trade works, what this year is like, and — through the protagonist's memory of a later world — what the people on the page will become, with years and figures. It talks to the reader, may wink, may ask a question and answer it, and then hands the page back to the scene. What it says is always about these people, this trade and this year.

Sample anchor:

```
{anchor}
```

One flat line of dialogue, then the storyteller explains the editor's last weeks: the good news, the gossip, the colleague five metres away, and what she is afraid of.

'''
s = eb.replace('MOMENTS', muc + 'MOMENTS', 1)
(ROOT / D / 'si-L-1E3BS.txt').write_text(s, encoding='utf-8', newline='\n')
print(len(eb), len(s))
jobs = [{'si': f'{D}/si-{k}.txt', 'prompt': f'{D}/ch107/brief-tron.md', 'out': f'{D}/ch107/{k}-{x}.md',
         'think_out': f'{D}/ch107/thinking-{k}-{x}.md', 'note': f'ch107 brief tron, {k} ({x})'}
        for k in ('L-1E3B', 'L-1E3BS') for x in 'ab']
(ROOT / D / 'jobs-ch107.json').write_text(json.dumps(jobs, ensure_ascii=False, indent=1), encoding='utf-8')
