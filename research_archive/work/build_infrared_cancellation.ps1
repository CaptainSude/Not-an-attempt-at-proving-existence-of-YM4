$ErrorActionPreference = 'Stop'
$taskRoot = Split-Path -Parent $PSScriptRoot
$parts = @(
  'work/infrared_cancellation_notebook_head.tex',
  'work/joint_scalar_infrared_fragment.tex',
  'work/physical_vector_spectral_fragment.tex',
  'work/covariant_corrected_scalar_fragment.tex',
  'work/physical_quotient_localization_fragment.tex',
  'work/mean_zero_gauge_spectral_fragment.tex',
  'work/covariant_mean_zero_density_fragment.tex',
  'work/infrared_cancellation_notebook_tail.tex'
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
$outPath = Join-Path $taskRoot 'outputs/ym4-infrared-cancellation-notebook.tex'
[System.IO.File]::WriteAllText($outPath, $combined, [System.Text.UTF8Encoding]::new($false))
[pscustomobject]@{ Path=$outPath; Bytes=(Get-Item -LiteralPath $outPath).Length; Labels=$labels.Count; References=$refs.Count; Missing=$missing.Count; Duplicates=$duplicates.Count; Controls=$controls } | ConvertTo-Json
