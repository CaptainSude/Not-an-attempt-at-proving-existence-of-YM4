$ErrorActionPreference = 'Stop'
$taskRoot = Split-Path -Parent $PSScriptRoot
$parts = @(
  'work/positive_drift_notebook_head.tex',
  'work/soft_penalty_physical_band_fragment.tex',
  'work/soft_scalar_complete_coefficient_fragment.tex',
  'work/actual_base_ward_heat_comparison_fragment.tex',
  'work/wilson_continuum_heat_comparison_fragment.tex',
  'work/actual_positive_beta_assembly_fragment.tex',
  'work/local_positive_drift_fragment.tex',
  'work/positive_drift_notebook_tail.tex'
)
$texts = foreach ($part in $parts) {
  [System.IO.File]::ReadAllText((Join-Path $taskRoot $part))
}
$combined = ($texts -join ([Environment]::NewLine + [Environment]::NewLine))
$labels = @([regex]::Matches($combined, '\\label\{([^}]+)\}') | ForEach-Object { $_.Groups[1].Value })
$refs = @([regex]::Matches($combined, '\\(?:eqref|ref)\{([^}]+)\}') | ForEach-Object { $_.Groups[1].Value })
$duplicates = @($labels | Group-Object | Where-Object Count -gt 1 | ForEach-Object Name)
$missing = @($refs | Where-Object { $_ -notin $labels } | Sort-Object -Unique)
$controls = [regex]::Matches($combined, '[\x00-\x09\x0B\x0C\x0E-\x1F]|\r(?!\n)').Count
$bareCommands = @([regex]::Matches($combined, '(?<![\\A-Za-z])(?:quad|qquad|frac|tfrac)(?![A-Za-z])') | ForEach-Object Value)
if ($duplicates.Count -or $missing.Count -or $controls -or $bareCommands.Count) {
  throw "Static failure: duplicates=$($duplicates -join ','); missing=$($missing -join ','); controls=$controls; bareCommands=$($bareCommands -join ',')"
}
$outPath = Join-Path $taskRoot 'outputs/ym4-positive-drift/main.tex'
if (-not (Test-Path -LiteralPath (Split-Path -Parent $outPath))) {
  throw 'Create the dedicated LaTeX project before assembly.'
}
[System.IO.File]::WriteAllText($outPath, $combined, [System.Text.UTF8Encoding]::new($false))
[pscustomobject]@{ Path=$outPath; Bytes=(Get-Item -LiteralPath $outPath).Length; Labels=$labels.Count; References=$refs.Count; Missing=$missing.Count; Duplicates=$duplicates.Count; Controls=$controls } | ConvertTo-Json
