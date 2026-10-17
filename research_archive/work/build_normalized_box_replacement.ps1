$ErrorActionPreference = 'Stop'
$taskRoot = Split-Path -Parent $PSScriptRoot
$parts = @('work/normalized_box_replacement_head.tex', 'work/normalized_box_replacement_fragment.tex')
$nl = [Environment]::NewLine
$combined = (($parts | ForEach-Object { [System.IO.File]::ReadAllText((Join-Path $taskRoot $_)) }) -join ($nl + $nl)) + $nl + '\end{document}' + $nl
$labels = @([regex]::Matches($combined, '\\label\{([^}]+)\}') | ForEach-Object { $_.Groups[1].Value })
$refs = @([regex]::Matches($combined, '\\(?:eqref|ref)\{([^}]+)\}') | ForEach-Object { $_.Groups[1].Value })
$duplicates = @($labels | Group-Object | Where-Object Count -gt 1 | ForEach-Object Name)
$missing = @($refs | Where-Object { $_ -notin $labels } | Sort-Object -Unique)
if ($duplicates.Count -or $missing.Count) { throw "Invalid labels or references" }
$outPath = Join-Path $taskRoot 'outputs/ym4-normalized-box-replacement/main.tex'
[System.IO.File]::WriteAllText($outPath, $combined, [System.Text.UTF8Encoding]::new($false))
[pscustomobject]@{Path=$outPath;Bytes=(Get-Item -LiteralPath $outPath).Length;Labels=$labels.Count;References=$refs.Count} | ConvertTo-Json
