"""Lưu một đoạn đã được Agent đọc và review; không tự chấm chất lượng văn.

Chạy từ repo: python ky-si/gemini/luu-doan.py <spec.json>
Spec đặt ngoài repo; chứa n, attempt, session_url, prompt_file, review,
state, summary, ledger {before, after, receipts, expenses}, log, decision.
Nguyên văn đã lấy từ DOM phải có trong archive/doan-N-writer-AA.md.
decision là 'ĐẠT' hoặc 'SỬA NHẸ'; không gán Tác giả đã duyệt.
"""

import hashlib
import json
import re
import shutil
import subprocess
import sys
from decimal import Decimal
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[2]
STORY = ROOT / "ky-si"


def write(path, value):
    path.write_text(value.rstrip() + "\n", encoding="utf-8", newline="")


def main():
    spec = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    n = f"{int(spec['n']):03d}"
    attempt = f"{int(spec['attempt']):02d}"
    if spec["decision"] not in ("ĐẠT", "SỬA NHẸ"):
        raise ValueError("Chỉ giữ đoạn sau khi Agent review; bản hỏng ở archive")
    chapter = STORY / "chapters" / f"doan-{n}.md"
    if chapter.exists():
        raise FileExistsError("Không ghi đè chính văn đã có: " + str(chapter))
    previous = sorted((STORY / "chapters").glob("doan-*.md"))[-1]
    if int(re.search(r"doan-(\d+)", previous.name)[1]) + 1 != int(n):
        raise ValueError("Đoạn phải nối đúng số kế tiếp")
    ledger = spec["ledger"]
    amount = lambda value: Decimal(str(value))
    if (amount(ledger["before"]) + sum(map(amount, ledger["receipts"]))
            - sum(map(amount, ledger["expenses"]))) != amount(ledger["after"]):
        raise ValueError("Số dư tiền không khớp")
    old_progress = STORY / "handoff" / "progress.json"
    if old_progress.exists():
        old = json.loads(old_progress.read_text(encoding="utf-8"))
        if amount(old["cash"]) != amount(ledger["before"]):
            raise ValueError("Tiền đầu không khớp checkpoint trước")
    stem = f"doan-{n}-writer-{attempt}"
    archive = STORY / "archive" / (stem + ".md")
    raw = archive.read_bytes()
    prose = raw.decode("utf-8").rstrip("\r\n")
    if len(re.findall(r"[\u4e00-\u9fff]", prose)) < 1000:
        raise ValueError("Bản thảo quá ngắn; kiểm tra lấy đủ chính văn")
    prompt = ROOT / spec["prompt_file"]
    si = STORY / "gemini" / "system-instruction.md"
    shutil.copyfile(prompt, archive.with_name(stem + "-prompt.md"))
    shutil.copyfile(si, archive.with_name(stem + "-si.md"))
    meta = dict(model="Gemini 3.8 Flash", thinking="High", googleSearchGrounding=False,
                sessionUrl=spec["session_url"], sessionSegment=spec["session_segment"],
                status="agent_reviewed_" + spec["decision"], authorApproved=False,
                proseCharacters=len(prose), hanCharacters=len(re.findall(r"[\u4e00-\u9fff]", prose)),
                fileSha256=hashlib.sha256(raw).hexdigest(),
                promptCharacters=len(prompt.read_text(encoding="utf-8")),
                systemInstructionCharacters=len(si.read_text(encoding="utf-8")),
                retrieval="Rendered DOM prose; saved verbatim; byte equality checked.",
                ledger=ledger)
    write(archive.with_name(stem + "-meta.json"), json.dumps(meta, ensure_ascii=False, indent=2))
    chapter.write_bytes(raw)
    assert chapter.read_bytes() == raw
    write(STORY / "reviews" / f"doan-{n}.md", spec["review"])
    write(STORY / "handoff" / "state.md", spec["state"])
    sofar = STORY / "handoff" / "story-so-far.md"
    write(sofar, sofar.read_text(encoding="utf-8").rstrip() + "\n\n" + spec["summary"])
    for relative, addition in spec.get("append", {}).items():
        path = (STORY / relative).resolve()
        if not path.is_relative_to(STORY.resolve()):
            raise ValueError("Đường dẫn ngoài thư mục truyện")
        write(path, path.read_text(encoding="utf-8").rstrip() + "\n\n" + addition)
    readme = STORY / "README.md"
    body = readme.read_text(encoding="utf-8")
    body = re.sub(r"\*\*Trạng thái 23/10/2026:\*\*[^\n]*",
                  f"**Trạng thái 23/10/2026:** Đã viết tới [đoạn {n}](chapters/doan-{n}.md), "
                  f"{meta['hanCharacters']:,} chữ Hán; [review {spec['decision']}](reviews/doan-{n}.md). "
                  "Agent đang viết tiếp theo yêu cầu; chưa ghi Tác giả duyệt từng bản mới.", body)
    row = f"| {n} | [Brief](briefs/doan-{n}.md) | [Chính văn](chapters/doan-{n}.md) | [" + spec["decision"] + f"](reviews/doan-{n}.md) | Agent review |"
    lines = body.splitlines()
    last = max(i for i, line in enumerate(lines) if line.startswith("| ") and line.endswith("|"))
    lines.insert(last + 1, row)
    write(readme, "\n".join(lines))
    sessions = STORY / "handoff" / "sessions.md"
    write(sessions, sessions.read_text(encoding="utf-8").rstrip() + "\n" +
          f"| [{n} lượt {attempt}]({spec['session_url']}) | {n} | {meta['promptCharacters']} ký tự | "
          f"{spec['decision']}; đoạn {spec['session_segment']}/2 của session |")
    log = STORY / "log.md"
    write(log, log.read_text(encoding="utf-8").rstrip() + "\n\n2026-10-23 | " + n + " | " +
          spec["log"] + " | Yêu cầu tiếp tục liên tục của Tác giả; Agent review, không gán duyệt riêng |")
    write(old_progress, json.dumps(dict(latest=int(n), cash=ledger["after"],
          receivables=spec.get("receivables", []), sessionUrl=spec["session_url"],
          sessionSegments=spec["session_segment"], decision=spec["decision"],
          authorApproved=False), ensure_ascii=False, indent=2))
    subprocess.run([sys.executable, "tools/build_pack.py", "ky-si"], cwd=ROOT, check=True,
                   capture_output=True, encoding="utf-8")
    print(json.dumps(dict(saved=n, han=meta["hanCharacters"], cash=ledger["after"],
                          archiveEqualsChapter=True, decision=spec["decision"]), ensure_ascii=False))


if __name__ == "__main__":
    main()
