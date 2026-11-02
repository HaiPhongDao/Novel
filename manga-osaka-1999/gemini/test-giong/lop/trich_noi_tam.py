"""Trích các đoạn lời kể (không thoại) có nhắc tới một nhân vật — để đọc nội tâm mà không phải đọc toàn văn."""
import re
import sys

ten = re.compile(sys.argv[1])  # vd: 'Kurokawa|黑川|^她'
for f in sys.argv[2:]:
    print(f'== {f}')
    for i, p in enumerate(l.strip() for l in open(f, encoding='utf-8')):
        if not p or p.startswith('<!--') or '“' in p:
            continue
        if ten.search(p):
            print(f'{i:3} {p[:110]}')
