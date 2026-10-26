#!/usr/bin/env python3
"""Kiem anchor trong file SI so voi nguyen van nguon.

Dung:
    python verify_anchors.py <file-si.md> <nguon1.json|nguon1.txt> [...]

- Tach moi block ```...``` trong file SI (moi block = mot anchor).
- Nguon .json: ghep moi value chuoi; .txt: doc ca file.
- Bo moi khoang trang, doi '――' thanh '——' o ca hai phia truoc khi so.
- In OK/MISS tung anchor; MISS thi in cho lech dau tien va do dai phan dan SI.
"""
import difflib
import json
import re
import sys


def flat(s):
    return re.sub(r"\s+", "", s.replace("――", "——"))


def load_sources(paths):
    buf = []
    for p in paths:
        if p.lower().endswith(".json"):
            data = json.load(open(p, encoding="utf-8"))
            if isinstance(data, dict):
                buf += [v for v in data.values() if isinstance(v, str)]
            elif isinstance(data, list):
                buf += [v for v in data if isinstance(v, str)]
            else:
                buf.append(str(data))
        else:
            buf.append(open(p, encoding="utf-8", errors="ignore").read())
    return flat("\n".join(buf))


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2

    si = open(sys.argv[1], encoding="utf-8").read()
    src = load_sources(sys.argv[2:])
    blocks = re.findall(r"```\n(.*?)\n```", si, re.S)
    if not blocks:
        print("Khong thay anchor nao (block ```) trong file SI.")
        return 2

    bad = 0
    for i, b in enumerate(blocks, 1):
        nb = flat(b)
        if nb and nb in src:
            print("anchor %d: OK  (%d ky tu, khong tinh khoang trang)" % (i, len(nb)))
            continue

        bad += 1
        print("anchor %d: MISS (%d ky tu)" % (i, len(nb)))
        head = nb[:12]
        best, ratio = None, 0.0
        for m in re.finditer(re.escape(head), src):
            seg = src[m.start():m.start() + len(nb)]
            r = difflib.SequenceMatcher(None, nb, seg).ratio()
            if r > ratio:
                ratio, best = r, seg
        if best is None:
            print("  khong tim duoc doan gan nhat - kiem lai da nap dung nguon chua")
            continue
        print("  doan gan nhat khop %.3f; khac o:" % ratio)
        for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, nb, best).get_opcodes():
            if tag != "equal":
                print("    %s: SI=%r nguon=%r" % (tag, nb[i1:i2], best[j1:j2]))

    start, end = si.find("BẮT ĐẦU SI"), si.find("HẾT SI")
    if start != -1 and end != -1 and end > start:
        print("do dai phan dan: %d ky tu" % (end - start))
    print("ket qua: %d/%d anchor khop" % (len(blocks) - bad, len(blocks)))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
