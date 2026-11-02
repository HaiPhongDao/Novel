"""SI bản E = bản D + ROLE viết lại không dùng cặp danh từ trừu tượng (bỏ trước cho E-PROSE-13). Test trên ch52 brief trơn."""
import json
import sys
from pathlib import Path

ROOT = Path(sys.argv[1])
D = 'manga-osaka-1999/gemini/test-giong/lop'
s = (ROOT / D / 'si-L-1D3.txt').read_text(encoding='utf-8')

cu1 = 'in the brisk, conversational, dryly ironic register of 起点 serials'
moi1 = 'in the conversational, dryly ironic register of 起点 serials'
cu2 = s[s.index('Tension and comedy rest on'):s.index('The anchors below')]
moi2 = ('Tension and comedy come from people at work who are busy with something of their own: a private errand, '
        'a guess about the person in front of them, what they say and what they keep to themselves. The trade\'s money '
        '— page rates, prize money, deadlines, wages, B4 paper — is one of the things they think about.\n\n')
assert s.count(cu1) == 1 and cu2
s = s.replace(cu1, moi1).replace(cu2, moi2)
(ROOT / D / 'si-L-1E3.txt').write_text(s, encoding='utf-8', newline='\n')
print(len(s))
jobs = [{'si': f'{D}/si-L-1E3.txt', 'prompt': f'{D}/ch52/brief-tron.md', 'out': f'{D}/ch52/L-1E3-{x}.md',
         'think_out': f'{D}/ch52/thinking-L-1E3-{x}.md', 'note': f'ch52 brief tron, L-1E3 ({x})'} for x in 'ab']
(ROOT / D / 'jobs-l1e.json').write_text(json.dumps(jobs, ensure_ascii=False, indent=1), encoding='utf-8')
