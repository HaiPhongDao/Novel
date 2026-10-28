#!/usr/bin/env python3
"""Chuyen State JSON (chung/state-extractor.md) sang markdown cung noi dung, de dua cho Writer.

Vi sao (Tac gia 29/10): dua nguyen khoi JSON vao prompt co the keo Writer sang "che do code",
van ra kem hon. Ban markdown giu dung tung truong, chi doi hinh thuc: tieu de + gach dau dong.
Agent van sua state.json lam nguon; file .md sinh ra tu no.

Dung:  python tools/state_md.py <state.json> [--out <state.md>]
       (khong --out thi in ra man hinh)
Trong code:  from state_md import render; render(dict)
"""
import argparse
import json
import sys
from pathlib import Path


def _lines(items):
    return "\n".join(f"- {x}" for x in items if x)


def render(st: dict) -> str:
    out = []
    m = st.get("meta", {})
    if m.get("story"):
        out.append(f"**本书：** {m['story']}")
    if m.get("last_chapter") is not None:
        out.append(f"**已写到：** 第{m['last_chapter']}段")

    sb = st.get("scene_bridge", {})
    if any(sb.values()):
        rows = [("时间", sb.get("time")), ("地点", sb.get("where")), ("在场", sb.get("present")),
                ("上一段最后", sb.get("last_beat")), ("接下来要接上", sb.get("pending"))]
        out.append("## 场景衔接\n\n" + _lines(f"{k}：{v}" for k, v in rows if v))

    tl = st.get("timeline", {})
    log = [f"第{c['chapter']}段：{c['summary']}" for c in tl.get("chapter_log", [])]
    if tl.get("relative_time") or log:
        body = (f"现在：{tl['relative_time']}\n\n" if tl.get("relative_time") else "") + _lines(log)
        out.append("## 时间线\n\n" + body.strip())

    if st.get("already_told"):
        out.append("## 已经讲过（只可一笔带过，不再解释）\n\n" + _lines(st["already_told"]))
    if st.get("ledger"):
        out.append("## 账目\n\n" + _lines(f"{x['item']}：{x['value']}（第{x.get('as_of', '?')}段）" for x in st["ledger"]))
    if st.get("deadlines"):
        out.append("## 期限与承诺\n\n" + _lines(st["deadlines"]))

    mc = st.get("main_character", {})
    if mc:
        parts = [f"**{mc.get('name', '')}**：{mc.get('identity', '')}"]
        for key, label in (("traits", "固定特征"), ("status", "眼下状态"), ("knowledge", "他知道")):
            if mc.get(key):
                parts.append(f"{label}：\n" + _lines(mc[key]))
        out.append("## 主角\n\n" + "\n\n".join(parts))

    if st.get("knowledge_map"):
        rows = []
        for k in st["knowledge_map"]:
            r = f"{k['secret']}：知道的人 {'、'.join(k.get('knows', [])) or '无'}"
            if k.get("not_known_to"):
                r += f"；不知道的人 {'、'.join(k['not_known_to'])}"
            rows.append(r)
        out.append("## 谁知道什么\n\n" + _lines(rows))

    if st.get("characters"):
        rows = []
        for c in st["characters"]:
            r = f"**{c['name']}**：{c.get('role', '')}"
            if c.get("notes"):
                r += f"。{c['notes']}"
            if c.get("speech"):
                r += f"。称呼：{c['speech']}"
            rows.append(r)
        out.append("## 人物\n\n" + _lines(rows))

    if st.get("places"):
        out.append("## 地点\n\n" + _lines(st["places"]))
    if st.get("objects"):
        out.append("## 物品\n\n" + _lines(f"{o['name']}（在{o.get('holder', '?')}）：{o.get('notes', '')}" for o in st["objects"]))

    rules = st.get("rules", {})
    rr = [("世界", rules.get("world", [])), ("能力与器物", rules.get("mechanics", [])), ("不能写的", rules.get("hard_limits", []))]
    if any(v for _, v in rr):
        out.append("## 规则\n\n" + "\n\n".join(f"{k}：\n{_lines(v)}" for k, v in rr if v))

    if st.get("open_threads"):
        out.append("## 未解决\n\n" + _lines(st["open_threads"]))
    if st.get("conflicts"):
        out.append("## 前文矛盾（以箭头后为准）\n\n" + _lines(st["conflicts"]))
    return "\n\n".join(out) + "\n"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("state")
    ap.add_argument("--out")
    a = ap.parse_args()
    md = render(json.loads(Path(a.state).read_text(encoding="utf-8")))
    if a.out:
        Path(a.out).write_text(md, encoding="utf-8")
        print(f"{a.out}  ({len(md)} ký tự)")
    else:
        print(md)


if __name__ == "__main__":
    main()
