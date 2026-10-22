# Save the draft currently in the clipboard (copied from AI Studio) as a chapter file, with a note line on top.
# Usage: powershell -File tools/save_clip.ps1 <out file> "<note>" [-ExpectLen N] [-ExpectHead "first chars"]
# The clipboard is shared with the whole machine: pass -ExpectLen/-ExpectHead so a clipboard
# overwritten by something else is refused instead of saved.
param([Parameter(Mandatory)][string]$Out, [string]$Note = '', [int]$ExpectLen = 0, [string]$ExpectHead = '')

$t = (Get-Clipboard -Raw).Replace("`r", '').Trim()
if ($ExpectLen -and [math]::Abs($t.Length - $ExpectLen) -gt 5) { throw "clipboard length $($t.Length) != expected $ExpectLen - not saved" }
if ($ExpectHead -and -not $t.StartsWith($ExpectHead)) { throw "clipboard starts with '$($t.Substring(0, [math]::Min(20, $t.Length)))' - not saved" }
$hdr = if ($Note) { "<!-- $Note -->`n`n" } else { '' }
[IO.File]::WriteAllText($Out, $hdr + $t + "`n", (New-Object Text.UTF8Encoding $false))
$han = ([regex]::Matches($t, '[一-鿿]')).Count
"$Out | $($t.Length) chars | $han han"
