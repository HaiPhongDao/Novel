"""SI E+BANS+SW: như E+BANS+S, chỉ đổi anchor người kể sang đoạn chêm giọng ch104 dòng 16–26 (3年→30天, 4岁...没错). Test ch107."""
import json
import sys
from pathlib import Path

ROOT = Path(sys.argv[1])
D = 'manga-osaka-1999/gemini/test-giong/lop'
s = (ROOT / D / 'si-L-1E3BS.txt').read_text(encoding='utf-8')
goc = (ROOT / D / 'ch104/goc.txt').read_text(encoding='utf-8').splitlines()
cu = '\n'.join(l.strip() for l in goc[43:51])
moi = '\n'.join(l.strip() for l in goc[15:26])
cap_cu = "One flat line of dialogue, then the storyteller explains the editor's last weeks: the good news, the gossip, the colleague five metres away, and what she is afraid of."
cap_moi = ("Nobody in the room says any of this; the storyteller tells the reader, half laughing: a three-year plan "
           "that became thirty days, a pause before the reason, the reason in the boy's own shout, then his past "
           "told with a wink.")
assert cu in s and cap_cu in s
s = s.replace(cu, moi).replace(cap_cu, cap_moi)
(ROOT / D / 'si-L-1E3BW.txt').write_text(s, encoding='utf-8', newline='\n')
print(len(s))
jobs = [{'si': f'{D}/si-L-1E3BW.txt', 'prompt': f'{D}/ch107/brief-tron.md', 'out': f'{D}/ch107/L-1E3BW-{x}.md',
         'think_out': f'{D}/ch107/thinking-L-1E3BW-{x}.md', 'note': f'ch107 brief tron, L-1E3BW ({x})'} for x in 'ab']
(ROOT / D / 'jobs-ch107w.json').write_text(json.dumps(jobs, ensure_ascii=False, indent=1), encoding='utf-8')
