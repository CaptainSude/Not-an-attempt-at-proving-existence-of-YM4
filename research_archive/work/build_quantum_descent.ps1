$ErrorActionPreference = 'Stop'
$taskRoot = Split-Path -Parent $PSScriptRoot
$parts = @(
  'work/quantum_descent_notebook_head.tex',
  'work/classical_summable_gauge_fragment.tex',
  'work/periodic_interaction_descent_fragment.tex',
  'work/quantum_local_limit_fragment.tex',
  'work/zero_input_quadratic_force_fragment.tex',
  'work/extracted_macrostep_recurrence_fragment.tex',
  'work/quantum_descent_notebook_tail.tex'
)
$texts = foreach ($part in $parts) {
  [System.IO.File]::ReadAllText((Join-Path $taskRoot $part))
}
$combined = ($texts -join "`n`n")
$labels = @([regex]::Matches($combined, '\\label\{([^}]+)\}') | ForEach-Object { $_.Groups[1].Value })
$refs = @([regex]::Matches($combined, '\\(?:eqref|ref)\{([^}]+)\}') | ForEach-Object { $_.Groups[1].Value })
$duplicates = @($labels | Group-Object | Where-Object Count -gt 1 | ForEach-Object Name)
$missing = @($refs | Where-Object { $_ -notin $labels } | Sort-Object -Unique)
$controls = [regex]::Matches($combined, '[\x00-\x08\x0B\x0C\x0E-\x1F]').Count
if ($duplicates.Count -or $missing.Count -or $controls) {
  throw "Static failure: duplicates=$($duplicates -join ','); missing=$($missing -join ','); controls=$controls"
}
$outPath = Join-Path $taskRoot 'outputs/ym4-quantum-descent-notebook.tex'
[System.IO.File]::WriteAllText($outPath, $combined, [System.Text.UTF8Encoding]::new($false))
[pscustomobject]@{ Path=$outPath; Bytes=(Get-Item -LiteralPath $outPath).Length; Labels=$labels.Count; References=$refs.Count; Missing=$missing.Count; Duplicates=$duplicates.Count; Controls=$controls } | ConvertTo-Json
