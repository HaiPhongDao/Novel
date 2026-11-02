"""Đếm nhãn thái độ trừu tượng (的XX与XX) theo nhóm cấu hình SI."""
import collections
import re
from pathlib import Path

pat = re.compile(r'的[一-鿿]{2}与[一-鿿]{2}')
G = collections.defaultdict(lambda: [0, 0, 0])


def nhom(b):
    if b.startswith(('ch01-co', 'ch01-khong', 'ch27-')) or 'chan-doan' in b:
        return 'SI day du (co BANS)'
    if '-L-B-' in b:
        return 'loi + BANS'
    return 'loi khong BANS'


for f in Path('manga-osaka-1999/gemini/test-giong').rglob('*.md'):
    b = f.name
    if b.startswith(('thinking', 'doc-cap', 'hoi-L1-cau', 'hoi-L1-tra', 'doc-ch')) or 'brief' in b:
        continue
    t = f.read_text(encoding='utf-8')
    h = len(re.findall(r'[一-鿿]', t))
    g = G[nhom(b)]
    g[0] += len(pat.findall(t)); g[1] += h; g[2] += 1
for k, (n, h, c) in G.items():
    print(f'{k}: {c} ban, {n} cho, {n / h * 1000:.2f}/1000')
