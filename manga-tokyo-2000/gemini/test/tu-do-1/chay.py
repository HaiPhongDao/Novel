# Test "Writer tu do" (Tac gia 29/10): moi doan chi co "Viet tiep ~2000 chu" + State JSON + duoi doan truoc,
# chat moi moi doan (gia lap qua session). Agent chi cap nhat state.json giua cac doan, khong viet outline/brief.
# Dung: python chay.py 2   (doc doan-001.md + state.json, ghi prompt-002.md, chay Writer ra doan-002.md)
import json, re, subprocess, sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
D = Path(__file__).parent
ROOT = D.parents[3]
n = int(sys.argv[1])
prev = (D / f"doan-{n-1:03d}.md").read_text(encoding="utf-8")
prev = re.sub(r"<!--.*?-->", "", prev, flags=re.S)
paras = [p.strip() for p in prev.split("\n") if p.strip()]
out, tot = [], 0
for p in reversed(paras):          # duoi ~2500 chu, cat theo doan tron
    out.append(p); tot += len(p)
    if tot >= 2500: break
tail = "\n\n".join(reversed(out))
state = json.loads((D / "state.json").read_text(encoding="utf-8"))
prompt = ("Viết tiếp đoạn tiếp theo, khoảng 2000 chữ, bằng tiếng Trung.\n\n---\n\n"
          "## State (JSON — sự thật và con số đã xảy ra, lấy đây làm chuẩn; `already_told` là chuyện đã kể, không kể lại)\n\n"
          + json.dumps(state, ensure_ascii=False, indent=1)
          + "\n\n---\n\n## Nguyên văn phần cuối đoạn trước (để giữ giọng; viết tiếp ngay sau chỗ này, không chép lại câu nào)\n\n"
          + tail + "\n")
pp = D / f"prompt-{n:03d}.md"
pp.write_text(prompt, encoding="utf-8")
rel = lambda p: str(p.relative_to(ROOT)).replace("\\", "/")
cmd = [sys.executable, "tools/aistudio_run.py", "--new", "--si", "manga-tokyo-2000/gemini/si-v1.txt",
       "--prompt", rel(pp), "--out", rel(D / f"doan-{n:03d}.md"), "--note", f"tu-do-1 doan-{n:03d}"]
r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
print(r.stdout[-800:], r.stderr[-800:])
f = D / f"doan-{n:03d}.md"
s = f.read_text(encoding="utf-8")
(D / f"doan-{n:03d}-raw.md").write_text(s, encoding="utf-8")
lines, res = s.split("\n"), []
for l in lines:                    # chen dong trong giua cac doan (chi doi khoang trang)
    if l.strip() and res and res[-1].strip(): res.append("")
    res.append(l)
f.write_text("\n".join(res), encoding="utf-8")
g = subprocess.run([sys.executable, "tools/cong_doan.py", rel(f), "--prompt", rel(pp), "--prev", rel(D / f"doan-{n-1:03d}.md")],
                   cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
print(g.stdout[-600:])
