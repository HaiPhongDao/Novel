"""Gửi system instruction + prompt đoạn tới model Ollama trên máy, lưu bản thảo.

Dùng:
    python tools/ollama_write.py --si <file SI> --prompt <briefs/doan-XXX.md> --out <file ra>
        [--model huihui_ai/qwen3.8-abliterated:27b] [--ctx 16384] [--temp 0.8] [--think]
"""
import argparse
import json
import sys
import time
import urllib.request
from pathlib import Path

API = "http://localhost:11434/api/chat"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--si", required=True)
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--model", default="huihui_ai/qwen3.8-abliterated:27b")
    ap.add_argument("--ctx", type=int, default=16384)
    ap.add_argument("--temp", type=float, default=0.8)
    ap.add_argument("--think", action="store_true", help="bật chế độ suy nghĩ của Qwen")
    args = ap.parse_args()

    body = {
        "model": args.model,
        "messages": [
            {"role": "system", "content": Path(args.si).read_text(encoding="utf-8")},
            {"role": "user", "content": Path(args.prompt).read_text(encoding="utf-8")},
        ],
        "stream": True,
        "think": args.think,
        "options": {"num_ctx": args.ctx, "temperature": args.temp, "top_p": 0.95, "repeat_penalty": 1.05},
    }
    req = urllib.request.Request(API, data=json.dumps(body).encode("utf-8"),
                                 headers={"Content-Type": "application/json"})

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    text, thinking, stats = [], [], {}
    start = time.time()
    with urllib.request.urlopen(req, timeout=3600) as resp:
        for line in resp:
            chunk = json.loads(line)
            msg = chunk.get("message", {})
            if msg.get("thinking"):
                thinking.append(msg["thinking"])
            if msg.get("content"):
                text.append(msg["content"])
                sys.stdout.write(msg["content"])
                sys.stdout.flush()
            if chunk.get("done"):
                stats = chunk

    draft = "".join(text).strip()
    out.write_text(draft + "\n", encoding="utf-8")
    if thinking:
        out.with_suffix(".thinking.md").write_text("".join(thinking), encoding="utf-8")

    n_tok = stats.get("eval_count", 0)
    eval_s = stats.get("eval_duration", 0) / 1e9
    han = sum(1 for c in draft if "一" <= c <= "鿿")
    print(f"\n\n--- {args.model} | {han} chữ Hán | {n_tok} token | "
          f"{n_tok / eval_s if eval_s else 0:.1f} tok/s | tổng {time.time() - start:.0f}s → {out}")


if __name__ == "__main__":
    main()
