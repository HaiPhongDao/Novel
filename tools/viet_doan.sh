#!/bin/bash
# Viết một đoạn thẳng vào chapters/: ghép gói (State JSON + đuôi đoạn trước) + brief, chạy Writer trên AI Studio, soát tật.
# Dùng (Git Bash, từ gốc repo):  bash tools/viet_doan.sh <ten-truyen> <NNN> <SI tương đối trong thư mục truyện> [tail=2500]
# Cần: Edge mở với extension "Novel AI Studio bridge"; tools/aistudio_run.py ở repo chính D:/ClaudeCode/Novel.
# Tài khoản thử theo thứ tự ACC (mặc định 2,0,1). Quá 11 phút không xong thì aistudio_run tự báo lỗi.
set -u
S=$1; N=$2; SI=$3; TAIL=${4:-2500}
ROOT=$(cd "$(dirname "$0")/.." && pwd -W)
cd "$ROOT" || exit 1
[ -f "$S/briefs/doan-$N.md" ] || { echo "Thiếu $S/briefs/doan-$N.md"; exit 1; }
[ -f "$S/chapters/doan-$N.md" ] && { echo "Đã có $S/chapters/doan-$N.md — không ghi đè"; exit 1; }
# Đoạn mở đầu: chưa có đoạn nào để ghép gói → gửi thẳng brief (như Z2 lần 1).
if ls "$S"/chapters/doan-*.md >/dev/null 2>&1; then
  python -I -X utf8 tools/build_pack.py "$S" --tail "$TAIL" --prompt "briefs/doan-$N.md" || exit 1
  PROMPT="handoff/session-start.md"
else
  PROMPT="briefs/doan-$N.md"
fi
J="$ROOT/$S/handoff/.jobs-$N.json"
python -I -X utf8 -c "
import json,sys
r,s,n,si,pr=sys.argv[1:6]
json.dump([{'si':f'{r}/{s}/{si}','prompt':f'{r}/{s}/{pr}','out':f'{r}/{s}/chapters/doan-{n}.md','note':''}],open(f'{r}/{s}/handoff/.jobs-{n}.json','w'))
" "$ROOT" "$S" "$N" "$SI" "$PROMPT"
(cd /d/ClaudeCode/Novel && python -I -X utf8 tools/aistudio_run.py --batch "$J" --timeout 8 --accounts "${ACC:-2,0,1}")
rm -f "$J"
F="$S/chapters/doan-$N.md"
[ -f "$F" ] || { echo "THIẾU $F — Writer không trả bài (xem dòng lỗi phía trên)"; exit 1; }
sed -i '1{/^<!--.*-->$/d}' "$F"; sed -i '1{/^$/d}' "$F"
P=$(printf "%03d" $((10#$N - 1)))
python -I -X utf8 tools/soat_tat.py "$F" $( [ -f "$S/chapters/doan-$P.md" ] && echo "$S/chapters/doan-$P.md" )
