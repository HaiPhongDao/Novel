"""Đo giọng người kể: tỷ lệ đoạn thoại, dấu người kể chêm vào, số dữ kiện kiếp trước được dùng, nhãn thái độ."""
import re
import sys

KE = r'事实上|没错|毕竟|谁能想到|说起来|要知道|说白了|换句话说|可想而知|不得不说'
SU = ['5.1', '吉尼斯', '128', '纪念日', '多大了', '死了吗', '1995', '1997', '吾辈义不容辞', '2026', '3小时', '三小时']
NHAN = re.compile(r'的[一-鿿]{2}与[一-鿿]{2}')
for f in sys.argv[1:]:
    t = open(f, encoding='utf-8').read()
    ps = [p.strip() for p in t.splitlines() if p.strip() and not p.startswith('<!--')]
    h = len(re.findall(r'[一-鿿]', t))
    thoai = sum('“' in p for p in ps)
    ke = len(re.findall(KE, t))
    su = [s for s in SU if s in t]
    print(f'{f.split("/")[-1]}: {h} chu | doan thoai {thoai}/{len(ps)} = {thoai / len(ps):.0%} | dau nguoi ke {ke} '
          f'| du kien kiep truoc {len(su)}/{len(SU)} | nhan {NHAN.findall(t)}')
