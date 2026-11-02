"""Tổng hợp số đo các bản ch01 của phép thử từng khối SI: mỗi cấu hình 2 lần chạy."""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(sys.argv[1])
LOP = ROOT / 'manga-osaka-1999/gemini/test-giong/lop'
GOC = 'chung/hieu-chuan/manga/ch01/goc.txt'
CFG = ['L', 'L-N', 'L-1', 'L-2', 'L-3', 'L-4', 'L-P2', 'L-B']
COT = ['字/đoạn', '字/lượt thoại', 'lượt thoại', 'giảng huấn /1.000', 'đoạn dài nhất']
QUET = ['phu-dinh-lap-cau', 'so-sanh-loi-ke', 'nhan-ngu-dieu', 'luot-cut']


def chay(*args):
    return subprocess.run([sys.executable, *args], cwd=ROOT, capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


def do(f):
    rel = f.relative_to(ROOT).as_posix()
    r = {}
    for line in chay('tools/hieu_chuan.py', 'so-sanh', '--goc', GOC, '--sinh', rel).splitlines():
        for c in COT:
            if line.startswith(c + ' '):
                r[c] = float(line[len(c):].split()[1])
    q = chay('tools/so_loi.py', 'quet', rel)
    for c in QUET:
        m = re.search(rf'{c}\s+(\d+) chỗ\s+([\d.]+)/1.000', q)
        if m:
            r[c] = float(m.group(2))
    t = f.read_text(encoding='utf-8')
    r['chữ Hán'] = len(re.findall(r'[一-鿿]', t))
    r['thẻ'] = len(re.findall(r'”[^“\n]*(?:说|问|道)[。，：:]?\s*$|(?:说|问|道)[：:]“', t, flags=re.M))
    r['trích'] = len(re.findall(r'\[\d+(?:,\s*\d+)*\]', t))
    return r


cols = ['chữ Hán'] + COT + QUET + ['thẻ', 'trích']
print('| cấu hình | lần | ' + ' | '.join(cols) + ' |')
print('|' + '---|' * (len(cols) + 2))
for k in CFG:
    for x in 'ab':
        f = LOP / f'ch01-{k}-{x}.md'
        if not f.exists():
            print(f'| {k} | {x} | (chưa có) |')
            continue
        r = do(f)
        print(f'| {k} | {x} | ' + ' | '.join(f"{r.get(c, '-'):g}" if isinstance(r.get(c), float) else str(r.get(c, '-')) for c in cols) + ' |')
