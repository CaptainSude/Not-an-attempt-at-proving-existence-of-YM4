# Independent audit: equal-exponent and scalar Schauder fragment

16 October 2026. Audited `work/flat_schauder_scalar_fragment.tex` against the proved heat-kernel and alias estimates in `flat_right_divergence_research.md` and the flat inverse notes. Status: pass; no correction needed.

1. For `0<alpha<1`, the cancellation bounds for second and third physical fine differences of the massive heat semigroup are `t^(-1+alpha/2)` and `t^(-3/2+alpha/2)`, including `t<eta^2`. For output separation `r>=eta`, the finite lattice path gives the minimum of the first bound and `r` times the second. Integrating separately below and above `r^2` yields precisely `C(2/alpha+2/(1-alpha)+1)r^alpha`. Weight ratios along the path are bounded in a fixed collar. Thus the fixed-exponent estimate does not need the positive Hölder loss in the earlier sufficient estimate.

2. The massive large-time tail contributes `O(r)`, hence `O(r^alpha)` for `r<=1`; distances above one use the supremum bound. The field and gradient supremum members are integrable as stated. The current transfer uses the already proved contraction on the complete-field `N` space and its smoothing into `N_alpha`; it does not shrink its radius because of the datum constant `C_alpha`.

3. The scalar Woodbury formula has the correct denominator `D_s,1=A+P_0((a')^-1+R_s,1)` and correct central/mixed cancellations. On an enlarged real chart it has a uniform positive lower bound; the previous high-alias bounds and Cauchy shrinking give a common holomorphic tube, uniformly for `a'` in the specified compact positive interval.

4. For the scalar massive subtraction, the high diagonal gains the factor `1-e^-t`. The rank output `a_r/P_r` remains absolutely summable after `1+alpha` physical differences because its dyadic shell sum is bounded by `C(1+n)^(d-1)2^(-n(1-alpha))`. A single input derivative leaves a uniformly square-summable alias row. The physical-cell normalization therefore has no refinement loss. Periodic gluing is applied only to the reconstructed operator, not an individual nonperiodic central chart term.

5. The scalar and one-form operators remain explicitly distinct. The scalar penalty interval is an honest hypothesis for the scalar inverse estimate; penalty-independence of a separate source projection would not remove that hypothesis from the estimate for `G'` itself. The fragment correctly avoids both endpoint exponents and arbitrary bounded-data second-difference claims.

This audit covers the flat and already-established flat-current operators. It is not a proof of a nonflat pointwise inverse or of matching an unspecified scalar penalty sequence.
