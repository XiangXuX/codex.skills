param(
  [Parameter(Mandatory = $true)]
  [string]$HtmlPath,

  [Parameter(Mandatory = $true)]
  [string]$PdfPath
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$edgeCandidates = @(
  "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
  "C:\Program Files\Microsoft\Edge\Application\msedge.exe"
)

$edge = $edgeCandidates | Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $edge) {
  throw "Microsoft Edge not found."
}

$resolvedHtml = (Resolve-Path -LiteralPath $HtmlPath).Path
$resolvedPdf = [System.IO.Path]::GetFullPath($PdfPath)
$url = "file:///" + ($resolvedHtml -replace "\\", "/")

& $edge --headless --disable-gpu --virtual-time-budget=12000 --print-to-pdf="$resolvedPdf" --no-pdf-header-footer $url | Out-Null

if (-not (Test-Path $resolvedPdf)) {
  throw "PDF generation failed."
}

Write-Output "PDF written to $resolvedPdf"
