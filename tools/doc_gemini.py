"""Cho Gemini (AI Studio) đọc chữ Trung thay Agent, rồi kiểm từng câu trích.

Vì sao có file này: đọc nguyên văn bộ mẫu và bản Writer là chỗ đốt token nhất của Agent (Tác giả 05/11:
"dự án này đốt token cực nhanh vì phải đọc"). Gemini qua AI Studio không tốn token Claude, nhưng có thể bịa.
Nên script làm ba việc:
  1. ghép một nhiệm vụ (chung/doc-gemini/nhiem-vu/*.md) + ghi chú + các văn bản có nhãn thành một prompt;
  2. chạy tools/aistudio_run.py với SI người đọc (chung/doc-gemini/si-doc.txt), một chat mới;
  3. kiểm MỌI câu trích [NHÃN] «…» trong báo cáo có thật trong nguồn — câu không thấy là dấu báo cáo bịa.
Với nhiệm vụ tim-anchor: cắt luôn cửa sổ theo hai câu trích và chạy tools/soat_van.py trên từng cửa sổ.

Gemini chỉ khoanh vùng. Câu ĐẠT vẫn do Tác giả; Agent đọc đúng đoạn được trích, không đọc lại cả chương.

Dùng:
    python tools/doc_gemini.py doc-cap --file GOC=chung/hieu-chuan/than-sung/ch03/goc.txt \
        --file A=sung-thu/gemini/test-giong/v1-ch03-a.md --out sung-thu/gemini/test-giong/gemini-doc-v1-a.md
    python tools/doc_gemini.py tom-tat --bo-mau "sung-thu/神宠供应商(1-140章).txt" --chuong 4-20 --out <file>
    python tools/doc_gemini.py tim-anchor --bo-mau <txt> --chuong 4-60 --ghi-chu "nội tâm MC hài" --out <file>
    python tools/doc_gemini.py doc-cap ... --chi-ghep          # chỉ ghép prompt, in cỡ, không chạy
    python tools/doc_gemini.py --chi-kiem <file đã chạy>        # kiểm lại câu trích (đọc nguồn từ dòng meta)

Mã trả về: 0 = mọi câu trích có thật · 3 = có câu trích không thấy (đừng tin báo cáo) · 1 = lỗi chạy.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
THU_MUC = ROOT / "chung" / "doc-gemini"
SI = THU_MUC / "si-doc.txt"
TOI_DA = 150_000

CN = {"零": 0, "〇": 0, "一": 1, "二": 2, "两": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9}
DAU_CHUONG = re.compile(r"^\s*第([0-9一二三四五六七八九十百千零〇两]+)章[：:\s]?(.*)$")
RAC = re.compile(r"「」|「小」|速读谷|suduguu|前往必搜索|首发|请收藏")
TRICH = re.compile(r"(?:\[([^\]\n]{1,20})\]\s*)?«([^»\n]{1,200})»")
META = re.compile(r"<!--\s*doc-gemini\s+(\{.*?\})\s*-->", re.S)


def so_chuong(s: str) -> int:
    if s.isdigit():
        return int(s)
    n = cur = 0
    for ch in s:
        if ch in CN:
            cur = CN[ch]
        elif ch in "十百千":
            n += (cur or 1) * {"十": 10, "百": 100, "千": 1000}[ch]
            cur = 0
    return n + cur


def tach_chuong(path: Path) -> dict[int, dict]:
    """Tách bộ mẫu .txt thành {số: {title, paras}}; chịu được số chữ Hán và tiêu đề lặp trong thân chương."""
    lines = path.read_text(encoding="utf-8", errors="replace").split("\n")
    heads = [(i, so_chuong(m.group(1)), m.group(2).strip())
             for i, l in enumerate(lines) if (m := DAU_CHUONG.match(l))]
    out: dict[int, dict] = {}
    for k, (i, n, title) in enumerate(heads):
        j = heads[k + 1][0] if k + 1 < len(heads) else len(lines)
        than = [l.strip().replace("　", "").strip() for l in lines[i + 1:j]]
        than = [l for l in than if l and not RAC.search(l) and l.strip("：:…. ")]
        if n in out:
            out[n]["paras"] += than
        else:
            out[n] = {"title": title, "paras": than}
    return out


def chon_chuong(spec: str) -> list[int]:
    so = []
    for phan in spec.split(","):
        phan = phan.strip()
        if "-" in phan:
            a, b = phan.split("-")
            so += list(range(int(a), int(b) + 1))
        elif phan:
            so.append(int(phan))
    return so


def bo_chu_thich(t: str) -> str:
    return re.sub(r"<!--.*?-->", "", t, flags=re.S).strip()


def chuan(s: str) -> str:
    return re.sub(r"\s+", "", s.replace("――", "——").replace("　", ""))


def nap_nguon(files: list[str], bo_mau: str | None, chuong: str | None):
    """Trả (khối văn bản theo thứ tự, {nhãn: văn bản chuẩn hoá}, {số chương: paras})."""
    khoi, nguon, cac_chuong = [], {}, {}
    for f in files:
        if "=" not in f:
            sys.exit(f"LỖI: --file phải dạng NHAN=đường_dẫn, nhận '{f}'")
        nhan, p = f.split("=", 1)
        t = bo_chu_thich((ROOT / p).read_text(encoding="utf-8") if not Path(p).is_absolute()
                         else Path(p).read_text(encoding="utf-8"))
        khoi.append(f"===== [{nhan}] {p} =====\n{t}")
        nguon[nhan] = chuan(t)
    if bo_mau:
        tat_ca = tach_chuong(ROOT / bo_mau if not Path(bo_mau).is_absolute() else Path(bo_mau))
        for n in chon_chuong(chuong or ""):
            if n not in tat_ca:
                print(f"  (bỏ qua: không tách được chương {n})")
                continue
            c = tat_ca[n]
            khoi.append(f"===== [CH {n}] {c['title']} =====\n" + "\n".join(c["paras"]))
            nguon[f"CH {n}"] = chuan("".join(c["paras"]))
            cac_chuong[n] = c["paras"]
    return khoi, nguon, cac_chuong


def ghep(nhiem_vu: str, ghi_chu: str, khoi: list[str]) -> str:
    p = Path(nhiem_vu)
    tep = p if p.suffix == ".md" and p.exists() else THU_MUC / "nhiem-vu" / f"{nhiem_vu}.md"
    if not tep.exists():
        sys.exit(f"LỖI: không thấy nhiệm vụ {tep}")
    phan = [tep.read_text(encoding="utf-8").strip()]
    if ghi_chu:
        phan.append(f"GHI CHÚ CỦA BIÊN TẬP VIÊN: {ghi_chu}")
    return "\n\n".join(phan + khoi) + "\n"


def kiem_trich(bao_cao: str, nguon: dict[str, str]):
    """Mỗi câu «…» phải có nguyên văn trong nguồn mang nhãn đó (không nhãn: trong bất kỳ nguồn nào)."""
    ok, sai = [], []
    tat_ca = "".join(nguon.values())
    for m in TRICH.finditer(bao_cao):
        nhan, q = (m.group(1) or "").strip(), m.group(2)
        nhan = re.sub(r"^CH\s*", "CH ", nhan)
        cq = chuan(q)
        if len(re.findall(r"[一-鿿]", q)) == 0:
            continue  # trích không có chữ Hán (tên tiếng Việt, số) — không kiểm
        dich = nguon.get(nhan, tat_ca)
        if cq in dich:
            ok.append((nhan, q))
        elif all(chuan(x) in dich for x in re.split(r"…+|\.{3,}", q) if chuan(x)):
            ok.append((nhan, q + "  [ghép quanh dấu …]"))
        else:
            sai.append((nhan or "?", q))
    return ok, sai


def cat_cua_so(bao_cao: str, cac_chuong: dict[int, list[str]], thu_muc: Path) -> list[Path]:
    """tim-anchor: mỗi dòng có hai câu trích cùng chương → cắt cửa sổ đoạn liên tiếp."""
    ra = []
    mau = re.compile(r"\[CH\s*(\d+)\]\s*«([^»]+)»\s*→\s*(?:\[CH\s*(\d+)\]\s*)?«([^»]+)»")
    for m in mau.finditer(bao_cao):
        n = int(m.group(1))
        n2 = int(m.group(3)) if m.group(3) else n
        if n != n2 or n not in cac_chuong:
            continue
        paras = cac_chuong[n]
        ca, cb = chuan(m.group(2)), chuan(m.group(4))
        i = next((k for k, p in enumerate(paras) if ca in chuan(p)), None)
        if i is None:
            continue
        j = next((k for k in range(i, len(paras)) if cb in chuan(paras[k])), None)
        if j is None or not (2 <= j - i <= 12):
            continue
        thu_muc.mkdir(parents=True, exist_ok=True)
        f = thu_muc / f"ch{n:03d}-p{i:03d}.md"
        f.write_text("\n\n".join(paras[i:j + 1]) + "\n", encoding="utf-8", newline="\n")
        ra.append(f)
    return ra


def ghi_ket_qua(out: Path, meta: dict, noi_dung: str, ok, sai, cua_so: list[Path]) -> None:
    L = [f"<!-- doc-gemini {json.dumps(meta, ensure_ascii=False)} -->", "", noi_dung.strip(), "",
         "## Kiểm trích (máy)", "",
         f"- {len(ok)}/{len(ok) + len(sai)} câu trích có nguyên văn trong nguồn."]
    for nhan, q in sai:
        L.append(f"- KHÔNG THẤY: [{nhan}] «{q}»")
    if cua_so:
        L.append(f"- Cửa sổ đã cắt: {len(cua_so)} file trong `{cua_so[0].parent.relative_to(ROOT).as_posix()}/`")
    out.write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="doc_gemini.py")
    ap.add_argument("nhiem_vu", nargs="?", help="doc-cap | tom-tat | tim-anchor | đường dẫn .md")
    ap.add_argument("--file", action="append", default=[], help="NHAN=đường_dẫn (lặp được)")
    ap.add_argument("--bo-mau", help="file .txt bộ mẫu")
    ap.add_argument("--chuong", help="vd 4-20 hoặc 4-10,14,35")
    ap.add_argument("--ghi-chu", default="")
    ap.add_argument("--out")
    ap.add_argument("--timeout", type=int, default=20)
    ap.add_argument("--accounts", default="0,1,2")
    ap.add_argument("--chi-ghep", action="store_true")
    ap.add_argument("--chi-kiem", metavar="FILE")
    ap.add_argument("--toi-da", type=int, default=TOI_DA, help="trần ký tự của prompt")
    a = ap.parse_args(argv)

    if a.chi_kiem:
        out = Path(a.chi_kiem)
        t = out.read_text(encoding="utf-8")
        m = META.search(t)
        if not m:
            sys.exit("LỖI: file không có dòng meta doc-gemini")
        meta = json.loads(m.group(1))
        _, nguon, cac_chuong = nap_nguon(meta["file"], meta.get("bo_mau"), meta.get("chuong"))
        than = t.split("## Kiểm trích (máy)")[0]
        ok, sai = kiem_trich(META.sub("", than), nguon)
        print(f"{len(ok)}/{len(ok) + len(sai)} câu trích có thật")
        for nhan, q in sai:
            print(f"  KHÔNG THẤY [{nhan}] «{q}»")
        return 3 if sai else 0

    if not a.nhiem_vu:
        ap.error("thiếu nhiệm vụ")
    khoi, nguon, cac_chuong = nap_nguon(a.file, a.bo_mau, a.chuong)
    if not khoi:
        ap.error("không có văn bản nào (--file hoặc --bo-mau + --chuong)")
    prompt = ghep(a.nhiem_vu, a.ghi_chu, khoi)
    if len(prompt) > a.toi_da:
        sys.exit(f"LỖI: prompt {len(prompt):,} ký tự > trần {a.toi_da:,} — chia nhỏ --chuong hoặc nâng --toi-da")
    tmp = Path(tempfile.gettempdir()) / "doc_gemini"
    tmp.mkdir(exist_ok=True)
    ten = Path(a.out).stem if a.out else a.nhiem_vu
    pfile = tmp / f"{ten}-prompt.md"
    pfile.write_text(prompt, encoding="utf-8", newline="\n")
    print(f"prompt {len(prompt):,} ký tự · {len(khoi)} văn bản · {pfile}")
    if a.chi_ghep:
        return 0
    if not a.out:
        ap.error("thiếu --out")
    out = (ROOT / a.out) if not Path(a.out).is_absolute() else Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "aistudio_run.py"), "--new", "--si", str(SI),
                        "--prompt", str(pfile), "--out", str(out), "--timeout", str(a.timeout),
                        "--accounts", a.accounts, "--note", f"doc-gemini {a.nhiem_vu}"], cwd=ROOT)
    if r.returncode != 0 or not out.exists():
        print("LỖI: aistudio_run không ra file")
        return 1
    noi_dung = bo_chu_thich(out.read_text(encoding="utf-8"))
    ok, sai = kiem_trich(noi_dung, nguon)
    cua_so = []
    if Path(a.nhiem_vu).stem == "tim-anchor" and cac_chuong:
        cua_so = cat_cua_so(noi_dung, cac_chuong, out.parent / f"{out.stem}-cua-so")
    meta = {"nhiem_vu": a.nhiem_vu, "file": a.file, "bo_mau": a.bo_mau, "chuong": a.chuong, "ghi_chu": a.ghi_chu}
    ghi_ket_qua(out, meta, noi_dung, ok, sai, cua_so)
    print(f"{out.relative_to(ROOT).as_posix()} · {len(ok)}/{len(ok) + len(sai)} câu trích có thật")
    for nhan, q in sai:
        print(f"  KHÔNG THẤY [{nhan}] «{q}»")
    if cua_so:
        subprocess.run([sys.executable, str(ROOT / "tools" / "soat_van.py"), *map(str, cua_so)], cwd=ROOT)
    return 3 if sai else 0


if __name__ == "__main__":
    sys.exit(main())
