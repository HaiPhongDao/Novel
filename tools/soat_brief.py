"""Soát một brief (prompt viết đoạn, tiếng Việt) TRƯỚC khi chạy Writer.

Dùng:
    python tools/soat_brief.py <brief.md> [<brief2.md> ...] [--prev-brief <brief đoạn trước>]
        [--bible <truyen>/bible/characters.md] [--glossary <truyen>/bible/glossary.md] [--mau-b] [--goi] [--json]

Nhiều brief liền nhau: brief đứng trước trong danh sách làm brief trước của brief sau (định mức lương,
tỷ giá, khẩu phần, số cũ, hình dạng chỗ dừng được mang theo).

--mau-b  truyện chạy mẫu B (AGENT §4): cho tính cách trong 【Thiết lập】, điểm bắt buộc và con số tổng; chỉ bắt
         thứ cả hai mẫu cùng cấm. Đổi mẫu của truyện đang chạy cần Tác giả duyệt — cổng không tự đổi.
--goi    brief chạy qua gói build_pack.py (State JSON + đuôi đoạn trước): không đòi dòng xưng hô và khối nối.
         Tự bật khi có <truyen>/handoff/state.json.

Bắt thứ brief giao cho Writer mà Writer sẽ dịch nguyên thành văn — kiểm toán test-gemini-moi 29/10,
khung và lý do ở `.claude/skills/novel-craft/templates/brief-doan.md`: beat đánh số, nhãn tính cách, kết cục
va chạm, số cuối đoạn, lời/lý lẽ soạn sẵn, câu ý nghĩa, hình ảnh kết đoạn, câu tiếng Trung, tên người chữ
Hán, quá nhiều cảnh, số học sai, thẻ nhân vật lệch bible.

CHẶN = sửa brief rồi mới chạy (mã thoát 1). CẢNH BÁO = đọc lại dòng đó. Cổng xanh chưa phải brief tốt.
"""
import json
import re
import sys
from pathlib import Path

CHAN, CANH = "CHẶN", "CẢNH BÁO"
HAN = r"一-鿿"
NUM = r"\d{1,3}(?:\.\d{3})+|\d+(?:,\d+)?"
# Chữ hay dùng để phiên âm tên Tây: một cụm toàn chữ này mà không có trong glossary thì gần như chắc là tên người.
PHIEN_AM = set("阿埃艾安奥巴贝比波伯布查达戴丹德迪蒂杜多恩法菲费弗盖格古哈汉赫亨霍吉基加贾杰金卡凯坎康科克肯库"
               "拉莱赖兰劳勒雷里利莉林琳卢鲁伦罗洛马玛麦曼梅蒙米莫姆穆纳娜内尼妮诺帕佩彭皮珀普奇齐乔琼切萨塞桑森沙"
               "莎尚施斯索塔泰坦汤唐特提托瓦万韦维温沃乌西希谢休雅亚扬伊因尤约泽扎詹兹")
LUONG_TU = "名袋只根把个辆斤步人条枚头匹座"


def w(*xs):
    return re.compile("|".join(xs), re.I)


LEXICON = {
    "nhan-tinh-cach": w(*[rf"(?<!\w){x}(?!\w)" for x in [
        "bình tĩnh", "quyết đoán", "lạnh lùng", "thiết huyết", "tham lam", "hèn nhát", "nhút nhát", "căm ghét",
        "gian xảo", "xảo quyệt", "kiêu ngạo", "ngạo mạn", "tàn nhẫn", "nhân từ", "hiền lành", "nóng nảy",
        "thẳng thừng", "kiệm lời", "trầm tính", "lão luyện", "đắc lực", "uy nghiêm", "khôn ngoan", "mưu mô",
        "ích kỷ", "trung thành", "dũng cảm", "can đảm", "tính toán thực tế", "khí thế áp đảo", "sắt đá"]]),
    "ket-cuc": w(r"(?<!\w)ép(?!\w).{0,40}?phải", "buộc phải", "giao nộp", "không dám", r"(?<!\w)đành(?!\w)",
                 "từ chối", "đầu hàng", "chịu thua", "bỏ chạy", "tháo chạy", "treo cổ", "chém đứt", "đâm chết",
                 "giết chết", r"tự tay (?:giết|chém)", "tử trận", "hy sinh", "đánh bại", "tiếp quản", "van xin",
                 "dập đầu", "quật ngã", "trói gô", "vội vã rời", "kết thúc nhanh", r"(?<!\w)chết(?!\w)",
                 r"(?<!chiến )(?<!\w)thắng(?!\w)"),
    "loi-soan-san": w(r"giải thích\s*(?:bằng|rằng|:)", "lấy cớ", "lập luận", "thuyết phục", "hỏi lại",
                      r"đáp (?:rằng|lại)", "nói rằng", r'"[^"\n]{1,60}"', r"“[^”\n]{1,60}”"),
    "menh-de-nghia": w(r"(?<!\w)Nếu(?!\w).{5,120}?(?<!\w)thì(?!\w)", *[rf"(?<!\w){x}(?!\w)" for x in [
        "khiến", "biến thành", "cho thấy", "thể hiện", "động lực", "nỗi sợ", "hưng phấn", "kinh sợ",
        "lạnh gáy", "thay vì", "như thể", "như chưa từng", "không ai dám", "không một ai dám", "kỷ luật sắt",
        "vốn liếng", "tột bậc", "tột độ", "đường cùng"]]),
    # "vì/nên" hay nằm trong câu sự thật trơn ("chết vì bệnh") — chỉ cảnh báo, không dồn thành chặn.
    "vi-nen": w(*[rf"(?<!\w){x}(?!\w)" for x in ["vì", "nên", "bởi vì", "do đó", "vì vậy"]]),
    "ket-hinh-anh": w("kết đoạn", "hoàng hôn buông", "chiều tà", "đứng lặng", "khép lại", "tà dương"),
    "hinh-anh": w("lạnh thấu xương", r"gió.{0,12}(?:rít|lùa|gào)", "mồ hôi", "hơi thở", "khói trắng", "co ro",
                  "bập bùng", "sáng rực", "đẫm máu", "thở hổn hển", "mặt mày", "run rẩy", "khóc lóc",
                  "ngơ ngác", "hoảng loạn", "nhe nanh", "gầm thét", "hung hãn", "thục mạng", "hớt hải",
                  "chi chít", "đung đưa", "hoang tàn", "trống hoác", "mở toang", "giá lạnh", "gian nan",
                  "khẩn trương", "khốc liệt"),
}
# Hình dạng chỗ dừng "có người chạy tới báo tin" — lặp lại trong 3 brief gần nhất là lặp khuôn kết đoạn.
MOC_BAO_TIN = re.compile(r"cấp báo|hớt hải|báo (?:tin|động)|(?<!\w)báo(?!\w).{0,20}phát hiện"
                         r"|phát hiện.{0,30}(?:đốm|toán|con)", re.I)
DA_XAY_RA = re.compile(r"(?<!\w)(?:đã|vừa|mới)(?!\w)|đoạn trước|hôm qua|trước đó|từ trước|trước đây"
                       r"|(?:ngày|tuần|tháng|năm|hôm|kiếp|lúc|mùa|đêm) trước", re.I)
SO_CUOI = [
    re.compile(rf"(?:{NUM})[^\n\d]{{0,20}}?(?<!-)(?:->|→|=>)(?!\s*(?:đủ|tức|=|khoảng))"),
    re.compile(rf"(?<!\w)từ\s*(?:{NUM})[^\n\d]{{0,20}}?(?:xuống|lên)\s*(?:còn\s*)?(?:{NUM})", re.I),
    re.compile(rf"(?:nhận|cộng)\s*(?:thêm\s*)?(?:{NUM})\s*(?:exp|điểm|点|经验)", re.I),
]
CON_SO = re.compile(rf"(?<!\w)còn\s*(?:đúng\s*)?(?:{NUM})\s*(?:người|cân|斤|kim tệ|金币|bạc|银币)", re.I)
MOC_GIO = {"sáng": r"sáng|bình minh|rạng đông", "trưa": r"trưa", "chiều": r"chiều",
           "tối": r"tối|đêm|hoàng hôn|chạng vạng"}
NHAY = re.compile(r"(?<!\w)(?:\d+|hai|ba|bốn|năm|sáu|bảy|tám|chín|mười)\s+ngày\s+(?:đường|trôi qua|sau|liền)"
                  r"|hành trình\s+\d+\s+ngày|nửa ngày trôi qua|hôm sau", re.I)
TIEN = {"金币": "vang", "kim tệ": "vang", "vàng": "vang", "银币": "bac", "bạc": "bac", "铜币": "dong", "đồng": "dong"}
DON_VI_TIEN = "|".join(sorted(TIEN, key=len, reverse=True))
LUONG = r"(?:cân|斤)"
STOP = set("là và của có gọi tự xưng tuổi người một hắn cho với những các đã không được trong khi ở từ này đó "
           "rồi thì mà nhưng cũng còn".split())

GOI_Y = {
    "danh-so": "Gộp thành một đoạn 'Tình huống' 3–5 câu; thứ tự sự việc để Writer chọn.",
    "nhan-tinh-cach": "Bỏ nhãn; ghi một sự thật của người đó lúc này (theo bible) — thái độ tự ra từ đó.",
    "ket-cuc": "Ghi thứ mỗi bên có trong tay; ai thắng là việc của Writer. Việc dàn ý buộc → một dòng 'Khoá:'.",
    "so-cuoi-doan": "Chỉ ghi sổ đầu đoạn + định mức; số cuối đoạn Agent tính sau khi đọc bản thảo.",
    "loi-soan-san": "Bỏ lời/lý lẽ soạn sẵn; ghi người đó cần gì, lo gì — họ tự tìm lời.",
    "menh-de-nghia": "Ghi sự việc nhìn thấy được, bỏ câu ý nghĩa/lập luận (AGENT §4.5).",
    "vi-nen": "Câu sự thật kèm 'vì… nên…' hay bị kể lại thành câu giải thích; tách thành hai sự thật.",
    "ket-hinh-anh": "Dừng ở một việc đang dở, không kết bằng hình ảnh.",
    "hinh-anh": "Tính từ cảm giác thành câu văn; chỉ giữ ở dòng 'Mở:' khi muốn mở đúng bằng nó.",
    "lap-cho-dung": "Cùng hình dạng chỗ dừng với một brief gần đây — đổi kiểu dừng.",
    "cau-tieng-trung": "Viết lại bằng tiếng Việt; chữ Hán chỉ cho thuật ngữ glossary và dòng bảng.",
    "chu-han-ngoai-glossary": "Thuật ngữ chưa có trong glossary/bible: thêm vào glossary hoặc viết tiếng Việt.",
    "ten-chu-han": "Tên người viết chữ Latin (Bate, không 巴特) — glossary mục 5.",
    "lech-glossary": "Glossary đã chốt cách viết khác — sửa brief (hoặc trình Tác giả sửa glossary).",
    "nhieu-canh": "Tối đa 2 cảnh + 1 lần nhảy thời gian; dời phần dư sang đoạn sau.",
    "so-hoc": "Tính lại bằng máy từ plot/so-lieu.md rồi chép số vào brief.",
    "doc-lai-so": "Số không đổi từ brief trước: chỉ giữ thứ đoạn này dùng tới.",
    "lech-bible": "Chép thẻ từ bible/characters.md.",
    "the-khong-tu-bible": "Vế này không có trong bible: chép đúng bible, hoặc trình Tác giả nếu là canon mới.",
    "chua-co-bible": "Nhân vật chưa có trong bible: ghi canon sau khi chốt đoạn.",
    "thieu": "Thiếu khối bắt buộc của khung brief.",
    "khoa": "Tối đa một dòng 'Khoá:'.",
}


def so(s):
    s = s.strip()
    if re.fullmatch(r"\d{1,3}(?:\.\d{3})+", s):
        s = s.replace(".", "")
    try:
        return float(s.replace(",", "."))
    except ValueError:
        return None


def words(s):
    return [x for x in re.findall(r"[^\W\d_]+", s.lower()) if x not in STOP and not re.search(f"[{HAN}]", x)]


def body_lines(text):
    """Bỏ khối nối tiếp (【接上】…【接上完】, GIỌNG MẪU … ---) và chú thích <!-- -->: không phải lời Agent gửi Writer."""
    out, skip = [], None
    for i, ln in enumerate(text.splitlines(), 1):
        s = ln.strip()
        if skip is None and "【接上】" in s:
            skip = "【接上完】"
        elif skip is None and s.startswith("GIỌNG MẪU"):
            skip = "---"
        elif skip is None and s.startswith("<!--"):
            skip = "-->"
        if skip:
            if (skip == "---" and s == "---") or (skip != "---" and skip in s):
                skip = None
            continue
        out.append((i, ln))
    return out


def is_panel(s):
    s = s.strip()
    return s.startswith("【") and ("：" in s or ":" in s.split("】")[0]) and re.search(f"[{HAN}]", s)


def strip_panel(s):
    return re.sub(r"【[^】\n]*[：:][^】\n]*】", " ", s)


def doc_bible(path):
    t = Path(path).read_text(encoding="utf-8")
    nv = {}
    for m in re.finditer(r"^##\s+(.+?)$\n(.*?)(?=^##\s|\Z)", t, flags=re.M | re.S):
        head = m.group(1)
        ten = re.split(r"\s+[—–-]\s+", head)[0].strip()
        age = re.search(r"(\d+)\s*tuổi", m.group(2))
        nv[ten] = {"tuoi": age.group(1) if age else None, "tu": set(words(head + " " + m.group(2)))}
    return nv, t


def doc_glossary(path):
    t = Path(path).read_text(encoding="utf-8")
    lat2han = {}
    for han, lat in re.findall(rf"([{HAN}]{{2,6}})\s*\(([A-Z][A-Za-z]+(?: [A-Z][A-Za-z]+)*)\)", t):
        lat2han[lat] = han
    cam = re.findall(r"không viết\s*`([^`]+)`", t)
    return lat2han, cam, t


def scan(path, ctx, bible=None, glossary=None):
    text = Path(path).read_text(encoding="utf-8")
    lines = body_lines(text)
    hits = []
    mau_b = ctx.get("mau_b")
    # Truyện chạy qua gói (build_pack.py: State JSON + đuôi đoạn trước): xưng hô và khối nối nằm trong gói.
    goi = ctx.get("goi") or (Path(path).resolve().parent.parent / "handoff" / "state.json").exists()
    # Mẫu B (AGENT §4) cho ghi tính cách trong 【Thiết lập】.
    thiet_lap, trong = set(), False
    for i, ln in lines:
        s = ln.strip()
        if s.startswith("【") and not is_panel(s):
            trong = "Thiết lập" in s
        elif trong:
            thiet_lap.add(i)

    def hit(check, level, i, s):
        hits.append({"check": check, "level": level, "line": i, "text": s.strip()[:90]})

    # 1. Beat đánh số.
    numbered = [(i, ln) for i, ln in lines if re.match(r"^\s*\d+[.)]\s+\S", ln)]
    if len(numbered) >= 2:
        for i, ln in numbered:
            hit("danh-so", CHAN, i, ln)

    # 2. Từ điển: nhãn, kết cục, lời soạn sẵn, câu nghĩa, hình ảnh.
    counts = {}
    for i, ln in lines:
        if is_panel(ln):
            continue
        s = strip_panel(ln)
        khoa = re.match(r"^\s*[-•]?\s*Kho[áa]\s*[:：]", s, re.I)
        mo = re.match(r"^\s*[-•]?\s*Mở\s*[:：]", s, re.I)
        for check, rx in LEXICON.items():
            if (check == "ket-cuc" and khoa) or (check in ("hinh-anh", "ket-hinh-anh") and mo):
                continue
            if mau_b and (check == "ket-cuc" or (check == "nhan-tinh-cach" and i in thiet_lap)):
                continue
            got = []
            for m in rx.finditer(s):
                # Thuật ngữ ngắn trong ngoặc ("大人", "回大人") là xưng hô, không phải câu thoại.
                if check == "loi-soan-san" and re.fullmatch(rf'["“][{HAN}]{{1,4}}["”]', m.group(0)):
                    continue
                if check == "ket-cuc":
                    a = max([s.rfind(c, 0, m.start()) for c in ",.;:()"] + [-1]) + 1
                    b = min([x for x in (s.find(c, m.end()) for c in ",.;:()") if x >= 0] + [len(s)])
                    if DA_XAY_RA.search(s[a:b]):
                        continue
                got.append(m.group(0) if len(m.group(0)) <= 40 else m.group(0)[:40] + "…")
            if got:
                counts[check] = counts.get(check, 0) + len(got)
                hit(check, None, i, " ".join(f"«{x}»" for x in got) + f" · {s.strip()}")
    for h in hits:
        if h["level"] is None:
            c = h["check"]
            if c in ("nhan-tinh-cach", "loi-soan-san", "ket-hinh-anh"):
                h["level"] = CHAN
            elif c == "ket-cuc":
                h["level"] = CHAN if counts[c] >= 3 else CANH
            elif c == "menh-de-nghia":
                h["level"] = CHAN if counts[c] >= 4 else CANH
            else:
                h["level"] = CANH

    # 3. Số cuối đoạn / biến động chỉ số (mẫu B cho đưa sẵn con số tổng — AGENT §4 mẫu B luật 18).
    for i, ln in lines:
        if is_panel(ln) or mau_b:
            continue
        s = strip_panel(ln)
        found = [m.group(0) for rx in SO_CUOI for m in rx.finditer(s)]
        if not re.match(r"^\s*Sổ", s):
            found += [m.group(0) for m in CON_SO.finditer(s)]
        if found:
            hit("so-cuoi-doan", CHAN, i, f"«{found[0].strip()}» · {s.strip()}")

    # 4. Chữ Hán: câu tiếng Trung, tên người chữ Hán, thuật ngữ ngoài glossary; tên Latin glossary đã đổi.
    allowed = (glossary[2] if glossary else "") + (bible[1] if bible else "")
    seen, ngoai = set(), []
    for i, ln in lines:
        if is_panel(ln):
            continue
        s = strip_panel(ln)
        for han, lat in re.findall(rf"([{HAN}]{{2,4}})\s*[（(]\s*([A-Z][a-z]+)\s*[)）]", s):
            if all(c in PHIEN_AM for c in han) and han not in allowed:
                hit("ten-chu-han", CHAN, i, f"«{han} ({lat})» · {s.strip()}")
                seen.add(han)
        co_dinh = "".join(re.findall(r"「[^」]*」|《[^》]*》", s))
        for run in re.findall(f"[{HAN}]+", s):
            if allowed and (run in allowed or run.lstrip(LUONG_TU) in allowed):
                continue
            if len(run) >= 6:
                if run in co_dinh:  # biển hiệu, tên sách, chuỗi cố định của bàn tay vàng (AGENT §4.8)
                    hit("cau-tieng-trung", CANH, i, f"«{run}» trong 「」/《》 — giữ nếu là chuỗi cố định · {s.strip()}")
                else:
                    hit("cau-tieng-trung", CHAN, i, f"«{run}» · {s.strip()}")
                continue
            core = run.lstrip(LUONG_TU) or run
            if core in seen or (allowed and core in allowed):
                continue
            seen.add(core)
            if 2 <= len(core) <= 4 and all(c in PHIEN_AM for c in core):
                hit("ten-chu-han", CANH, i, f"«{core}» có thể là tên phiên âm · {s.strip()}")
            elif allowed and len(core) >= 2:
                ngoai.append((i, core))
    if ngoai:
        hit("chu-han-ngoai-glossary", CANH, ngoai[0][0], " · ".join(c for _, c in ngoai))
    if glossary:
        lat2han, cam, _ = glossary
        for lat, han in lat2han.items():
            i = next((i for i, ln in lines if re.search(rf"(?<![A-Za-z]){re.escape(lat)}(?![A-Za-z])", ln)), None)
            if i:
                hit("lech-glossary", CANH, i, f"«{lat}» — glossary viết {han}")
        for x in cam:
            i = next((i for i, ln in lines if x in ln), None)
            if i:
                hit("lech-glossary", CANH, i, f"«{x}» — glossary ghi 'không viết {x}'")

    # 5. Số cảnh và lần nhảy thời gian.
    buckets, jumps = set(), set()
    for i, ln in lines:
        low = ln.lower()
        for k, rx in MOC_GIO.items():
            if re.search(rf"(?<!\w)(?:{rx})(?!\w)", low):
                buckets.add(k)
        jumps.update(m.group(0) for m in NHAY.finditer(low))
    if len(buckets) + len(jumps) >= 3:
        hit("nhieu-canh", CANH, 0, f"mốc: {', '.join(sorted(buckets))}; nhảy: {', '.join(sorted(jumps)) or '—'}")

    # 6. Số học: tỷ giá, nhân, trừ, định mức lương, khẩu phần.
    for i, ln in lines:
        s = strip_panel(ln)
        m = re.search(rf"1\s*({DON_VI_TIEN})\s*=\s*({NUM})\s*({DON_VI_TIEN})(?:\s*=\s*({NUM})\s*({DON_VI_TIEN}))?", s)
        if m:
            ctx["tien"][TIEN[m.group(1)]] = 1.0
            ctx["tien"][TIEN[m.group(3)]] = 1 / so(m.group(2))
            if m.group(4):
                ctx["tien"][TIEN[m.group(5)]] = 1 / so(m.group(4))
        parts = s.split("=")
        for a, b in zip(parts, parts[1:]):
            la = re.findall(rf"({NUM})\s*({DON_VI_TIEN})", a)
            rb = re.findall(rf"({NUM})\s*({DON_VI_TIEN})", b)
            if la and rb:
                (x, ux), (y, uy) = la[-1], rb[0]
                rx_, ry_ = ctx["tien"].get(TIEN[ux]), ctx["tien"].get(TIEN[uy])
                if rx_ and ry_ and abs(so(x) * rx_ - so(y) * ry_) > 0.01 * max(so(x) * rx_, 1e-9):
                    hit("so-hoc", CHAN, i, f"{x} {ux} ≠ {y} {uy} theo tỷ giá · {s.strip()}")
        for x, y, z in re.findall(rf"({NUM})[^\d×\n]{{0,14}}(?:×|\s[xX]\s)\s*({NUM})[^\d=\n]{{0,14}}=\s*({NUM})", s):
            if abs(so(x) * so(y) - so(z)) > 0.5:
                hit("so-hoc", CHAN, i, f"{x} × {y} = {so(x) * so(y):g}, brief ghi {z}")
        for x, y, z in re.findall(rf"({NUM})\s*[-−]\s*({NUM})\s*=\s*(?:còn\s*)?({NUM})", s):
            if abs(so(x) - so(y) - so(z)) > 0.5:
                hit("so-hoc", CHAN, i, f"{x} − {y} = {so(x) - so(y):g}, brief ghi {z}")
        for x, y, z in re.findall(rf"({NUM})[^\d\n]{{0,25}}?(?:->|→)\s*(?:trừ|trả|chết|mất|tiêu)\s*({NUM})"
                                  rf"[^\d\n]{{0,25}}?(?:->|→)\s*(?:còn\s*)?({NUM})", s):
            if abs(so(x) - so(y) - so(z)) > 0.5:
                hit("so-hoc", CHAN, i, f"{x} − {y} = {so(x) - so(y):g}, brief ghi {z}")
        m = re.search(rf"(?:trừ|tiêu hao|ăn hết|giảm thêm|giảm)\s*(?:đi\s*)?({NUM})[^\n]{{0,60}}?"
                      rf"từ\s*({NUM})[^\d\n]{{0,15}}xuống\s*(?:còn\s*)?({NUM})", s)
        if m and abs(so(m.group(2)) - so(m.group(1)) - so(m.group(3))) > 0.5:
            hit("so-hoc", CHAN, i, f"{m.group(2)} − {m.group(1)} ≠ {m.group(3)}")
        # Định mức lương (斤/ngày) mang qua các brief.
        m = re.search(rf"[Mm]ỗi ngày\s*(?:ăn|tiêu hao|tốn)\s*({NUM})\s*{LUONG}|({NUM})\s*{LUONG}\s*/\s*ngày", s)
        if m:
            ctx["dinh_muc"] = so(m.group(1) or m.group(2))
        r = ctx.get("dinh_muc")
        if r:
            for md in re.finditer(rf"đủ ăn\s*(?:hơn\s*|khoảng\s*)?({NUM})\s*ngày", s):
                # Số kho là số đứng sau "còn" hoặc "=" gần nhất phía trước; không có thì số lương gần nhất.
                truoc = s[:md.start()]
                kho = re.findall(rf"(?:còn|=)\s*(?:đúng\s*)?({NUM})\s*{LUONG}", truoc) or re.findall(rf"({NUM})\s*{LUONG}", truoc)
                if not kho:
                    continue
                d, x = md.group(1), so(kho[-1]) / r
                if abs(x - so(d)) > max(1.0, 0.15 * so(d)):
                    hit("so-hoc", CHAN, i, f"{kho[-1]} 斤 ÷ {r:g}/ngày = {x:.1f} ngày, brief ghi {d}")
            mn = re.search(rf"(?<!\w)({NUM})\s*ngày", s)
            mc = re.search(rf"(?:tiêu tốn|tiêu hao|ăn hết)\s*({NUM})\s*{LUONG}", s)
            if mn and mc and so(mn.group(1)) > 1:
                per = so(mc.group(1)) / so(mn.group(1))
                if abs(per - r) > 0.1 * r:
                    hit("so-hoc", CHAN, i, f"{mc.group(1)} 斤 / {mn.group(1)} ngày = {per:g}/ngày, định mức trước {r:g}")
            mc = re.search(rf"(?:tiêu hao|giảm thêm|ăn hết|trừ đi)\s*({NUM})\s*{LUONG}", s)
            if ctx.get("khau_phan_ha") and mc and abs(so(mc.group(1)) - r) <= 0.05 * r:
                hit("so-hoc", CHAN, i, f"khẩu phần đã hạ (brief trước) mà vẫn trừ đúng định mức cũ {r:g} 斤 · {s.strip()}")
        if re.search(r"hạ khẩu phần|giảm khẩu phần|khẩu phần giảm|chỉ được một bát", s, re.I):
            ctx["khau_phan_ha_sau"] = True

    # 7. Số cũ đọc lại (so với brief trước).
    def toks(t):
        out = set()
        for _, ln in body_lines(t):
            if is_panel(ln):
                continue
            for n, u in re.findall(rf"({NUM})\s*(bước|步|xe|cây rìu|rìu|把|kim tệ|金币|bạc|银币|lão binh|老兵|cọc|根"
                                   rf"|người|nông nô|cân|斤)", ln):
                u = {"步": "bước", "把": "rìu", "cây rìu": "rìu", "金币": "kim tệ", "银币": "bạc", "老兵": "lão binh",
                     "根": "cọc", "nông nô": "người", "斤": "cân"}.get(u, u)
                out.add(f"{so(n):g} {u}")
        return out
    if ctx.get("prev"):
        rep = sorted(toks(text) & toks(ctx["prev"]))
        if len(rep) >= 4:
            hit("doc-lai-so", CANH, 0, "; ".join(rep))

    # 8. Thẻ nhân vật so với bible.
    if bible:
        nv = bible[0]
        in_sec = False
        for i, ln in lines:
            s = ln.strip()
            if re.search(r"nhân vật|Người có mặt", s, re.I) and (s.startswith("【") or s.startswith("Người có mặt")):
                in_sec = True
                if not s.startswith("Người có mặt"):
                    continue
                s = s.split(":", 1)[-1]
            elif s.startswith("【") or (in_sec and not s):
                in_sec = False
            if not in_sec:
                continue
            for card in s.split(";"):
                m = re.match(rf"^\s*[-•*]?\s*([A-Z][A-Za-z]+(?: [A-Z][a-z]+)?|[{HAN}]{{2,4}})"
                             rf"(?:\s*[（(][A-Za-z]+[)）])?\s*[:：—–]\s*(.+)$", card)
                if not m:
                    continue
                ten, the = m.group(1), m.group(2)
                key = next((k for k in nv if k == ten or k.endswith(" " + ten)), None)
                if not key:
                    hit("chua-co-bible", CANH, i, f"«{ten}» · {card.strip()}")
                    continue
                age = re.search(r"(\d+)\s*tuổi", the)
                if age and nv[key]["tuoi"] and age.group(1) != nv[key]["tuoi"]:
                    hit("lech-bible", CHAN, i, f"{ten} {age.group(1)} tuổi, bible {nv[key]['tuoi']} tuổi")
                for ve in re.split(r"[,.;]", the):
                    if re.search(r"gọi|xưng|tuổi|nói về", ve, re.I):
                        continue
                    ws = words(ve)
                    if len(ws) >= 2 and sum(x in nv[key]["tu"] for x in ws) / len(ws) < 0.6:
                        hit("the-khong-tu-bible", CANH, i, f"{ten}: «{ve.strip()}»")

    # 9. Khối bắt buộc, dòng Khoá, hình dạng chỗ dừng.
    body = "\n".join(ln for _, ln in lines)
    if not re.search(r"Dừng", body):
        hit("thieu", CHAN, 0, "không có chỗ dừng ('Dừng ở …')")
    if not goi and not re.search(r"gọi\b.{1,40}?\blà\b|tự xưng|Xưng hô", body, re.I):
        hit("thieu", CANH, 0, "không có dòng xưng hô")
    if not re.search(rf"(?:{NUM})\s*(?:–|-|đến)\s*(?:{NUM})\s*(?:字|chữ)|khoảng\s*(?:{NUM})\s*(?:字|chữ)", body):
        hit("thieu", CANH, 0, "không có cửa sổ độ dài")
    if (not goi and re.search(r"Viết tiếp|đoạn tiếp theo", body, re.I)
            and not re.search(r"【接上】|GIỌNG MẪU|KHỐI NỐI TIẾP", text)):
        hit("thieu", CANH, 0, "viết tiếp mà không có khối nối tiếp")
    khoa = [i for i, ln in lines if re.match(r"^\s*[-•]?\s*Kho[áa]\s*[:：]", ln, re.I)]
    if len(khoa) > 1:
        hit("khoa", CHAN, khoa[1], f"{len(khoa)} dòng Khoá")
    # Chỗ dừng: dòng có "Dừng"/"đoạn kết" và các dòng ngay dưới nó (khi dòng đó chỉ là tiêu đề).
    dung, keo = [], 0
    for _, ln in lines:
        s = ln.strip()
        if re.search(r"Dừng|đoạn kết", s, re.I):
            dung.append(s)
            keo = 3
        elif keo and s and not s.startswith("【") and not re.match(r"\d+[.)]\s", s):
            dung.append(s)
            keo -= 1
        else:
            keo = 0
    dung = " ".join(dung)
    i_dung = next((i for i, ln in lines if re.search(r"Dừng", ln)), 0)
    bao_tin = bool(MOC_BAO_TIN.search(dung))
    if bao_tin and any(ctx["dung"][-3:]):
        hit("lap-cho-dung", CANH, i_dung, "lại dừng bằng 'có người chạy tới báo tin' như một brief gần đây")
    ctx["dung"].append(bao_tin)

    if ctx.pop("khau_phan_ha_sau", False):
        ctx["khau_phan_ha"] = True
    ctx["prev"] = text
    hits.sort(key=lambda h: (h["level"] != CHAN, h["line"]))
    verdict = CHAN if any(h["level"] == CHAN for h in hits) else (CANH if hits else "XANH")
    return {"file": path, "verdict": verdict, "hits": hits}


def main(argv):
    args, opt = [], {}
    it = iter(argv[1:])
    for a in it:
        if a in ("--prev-brief", "--bible", "--glossary"):
            opt[a] = next(it, None)
        elif a.startswith("--"):
            opt[a] = True
        else:
            args.append(a)
    if not args:
        print(__doc__)
        return 2
    bible = doc_bible(opt["--bible"]) if opt.get("--bible") else None
    glossary = doc_glossary(opt["--glossary"]) if opt.get("--glossary") else None
    ctx = {"tien": {}, "dung": [], "mau_b": opt.get("--mau-b"), "goi": opt.get("--goi")}
    if opt.get("--prev-brief"):
        scan(opt["--prev-brief"], ctx, bible, glossary)
    rows = [scan(a, ctx, bible, glossary) for a in args]
    if opt.get("--json"):
        print(json.dumps(rows, ensure_ascii=False, indent=1))
    else:
        for r in rows:
            n_c = sum(h["level"] == CHAN for h in r["hits"])
            print(f"== {Path(r['file']).name}  →  {r['verdict']}  ({n_c} chặn · {len(r['hits']) - n_c} cảnh báo)")
            for h in r["hits"]:
                ln = f"L{h['line']}" if h["line"] else "—"
                print(f"  [{h['level']}] {h['check']:<22} {ln:>4}  {h['text']}")
            for c in dict.fromkeys(h["check"] for h in r["hits"]):
                print(f"  → {c}: {GOI_Y[c]}")
            print()
    return 1 if any(r["verdict"] == CHAN for r in rows) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
