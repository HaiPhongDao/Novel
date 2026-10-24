# Mở Edge bằng profile riêng cho tools/aistudio_run.py (Edge không cho cổng debug trên profile mặc định).
# Lần đầu: powershell -File tools/edge_debug.ps1 -Login  → đăng nhập 3 tài khoản Google, rồi đóng Edge.
#          (đăng nhập khi KHÔNG bật cổng debug, Google hay chặn đăng nhập trên trình duyệt đang bị điều khiển)
# Sau đó:  powershell -File tools/edge_debug.ps1          → Edge mở với cổng 9222, để chạy aistudio_run.py
param([switch]$Login, [int]$Port = 9222)

$edge = "${env:ProgramFiles(x86)}\Microsoft\Edge\Application\msedge.exe"
$dir = Join-Path $env:LOCALAPPDATA 'NovelEdge'
$common = @("--user-data-dir=$dir", '--no-first-run')

if ($Login) {
    Start-Process $edge ($common + 'https://accounts.google.com/AddSession')
    "Đăng nhập đủ 3 tài khoản (u/0, u/1, u/2 theo thứ tự), rồi đóng cửa sổ Edge này."
    exit 0
}

try {
    $v = Invoke-RestMethod "http://127.0.0.1:$Port/json/version" -TimeoutSec 2
    "Edge đã mở sẵn ở cổng $Port ($($v.Browser))"
    exit 0
} catch {}

Start-Process $edge ($common + "--remote-debugging-port=$Port" + 'https://aistudio.google.com/u/0/prompts/new_chat')
for ($i = 0; $i -lt 20; $i++) {
    Start-Sleep -Milliseconds 500
    try { $v = Invoke-RestMethod "http://127.0.0.1:$Port/json/version" -TimeoutSec 2; "Edge sẵn sàng ở cổng $Port ($($v.Browser))"; exit 0 } catch {}
}
throw "Edge không mở cổng $Port — đóng hết cửa sổ Edge của profile NovelEdge rồi thử lại"
