# Put a UTF-8 text file on the clipboard and confirm it stuck (Set-Clipboard sometimes loses to a browser holding the clipboard).
# Usage: powershell -File tools/set_clip.ps1 <file>
param([Parameter(Mandatory)][string]$File)

Add-Type -AssemblyName System.Windows.Forms
$t = [IO.File]::ReadAllText($File)
for ($i = 0; $i -lt 10; $i++) {
    try { [System.Windows.Forms.Clipboard]::SetText($t) } catch {}
    Start-Sleep -Milliseconds 200
    if ([System.Windows.Forms.Clipboard]::GetText() -eq $t) { "clipboard ok | $(($t -replace "`r", '').Length) chars"; exit 0 }
}
throw "clipboard did not take $File"
