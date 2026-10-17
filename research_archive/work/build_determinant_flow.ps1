$ErrorActionPreference = 'Stop'
$taskRoot = Split-Path -Parent $PSScriptRoot
$parts = @(
  'work/determinant_flow_notebook_head.tex',
  'work/finite_classical_marginal_leakage_fragment.tex',
  'work/finite_quantum_coupling_continuity_fragment.tex',
  'work/determinant_maxwell_trace_fragment.tex',
  'work/determinant_gauge_bridge_fragment.tex',
  'work/classical_one_loop_cocycle_fragment.tex',
  'work/finite_block_drift_transfer_fragment.tex',
  'work/finite_trajectory_shooting_fragment.tex',
  'work/determinant_flow_notebook_tail.tex'
)
$texts = foreach ($part in $parts) {
  [System.IO.File]::ReadAllText((Join-Path $taskRoot $part))
}
$combined = ($texts -join ([Environment]::NewLine + [Environment]::NewLine))
$labels = @([regex]::Matches($combined, '\\label\{([^}]+)\}') | ForEach-Object { $_.Groups[1].Value })
$refs = @([regex]::Matches($combined, '\\(?:eqref|ref)\{([^}]+)\}') | ForEach-Object { $_.Groups[1].Value })
$duplicates = @($labels | Group-Object | Where-Object Count -gt 1 | ForEach-Object Name)
$missing = @($refs | Where-Object { $_ -notin $labels } | Sort-Object -Unique)
$controls = [regex]::Matches($combined, '[\x00-\x08\x0B\x0C\x0E-\x1F]|\r(?!\n)').Count
$bareSpacing = @([regex]::Matches($combined, '(?<![\\A-Za-z])(?:quad|qquad)(?![A-Za-z])') | ForEach-Object Value)
if ($duplicates.Count -or $missing.Count -or $controls -or $bareSpacing.Count) {
  throw "Static failure: duplicates=$($duplicates -join ','); missing=$($missing -join ','); controls=$controls; bareSpacing=$($bareSpacing -join ',')"
}
$outPath = Join-Path $taskRoot 'outputs/ym4-determinant-flow-notebook.tex'
[System.IO.File]::WriteAllText($outPath, $combined, [System.Text.UTF8Encoding]::new($false))
[pscustomobject]@{ Path=$outPath; Bytes=(Get-Item -LiteralPath $outPath).Length; Labels=$labels.Count; References=$refs.Count; Missing=$missing.Count; Duplicates=$duplicates.Count; Controls=$controls } | ConvertTo-Json
