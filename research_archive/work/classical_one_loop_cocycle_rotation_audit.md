# Independent audit: the actual finite leading determinant cocycle

17 October 2026. Full read of classical_one_loop_cocycle_research.md, including its corrected Section 6. Internal mathematical audit, not external certification. **Pass.**

## Actual gauge groups and local extension

The based gauge groups split by their site-coordinate sets: the kernel uses non-intermediate sites, and the embedded intermediate group uses intermediate centers except final centers. Their normalized Haar measures form the product measure. Their action is free because a link-preserving gauge fixed at a site is fixed everywhere on the connected graph. No uncomputed orbit-volume factor is introduced by this decomposition.

For two small endpoint configurations related by a final-based gauge, the bond equation controls neighboring gauge values. A path of length at most a fixed multiple of \(RL\) to a final center then makes the gauge uniformly near identity after shrinking the small field ball. The logarithm has controlled edge differences. The interpolation through its small logarithm keeps all link fields in the existing action domain; its gauge parameters can also be kept in the Ward domain by the same fixed-\(RL\) shrinkage. Thus the action agrees at the two small representatives. This proves that its saturation extension is well defined, rather than assuming a globally defined classical action.

The actual endpoint-covariant contour map supplies a local analytic slice \(P_{RL}=I\). Its derivative in the based gauge coordinate is invertible, and the orbit intersection with that slice is unique. The actual ordinary maps extend equivariantly on this tube, with the original local values on overlaps. No alternative mean is substituted. Only a fixed finite regulator and fixed ratios are needed for these local assertions.

## Common auxiliary cutoff and exact disintegration

The compact target germ and compact based gauge groups permit a compact orbit-tube cutoff equal to one near all relevant conditional minimizing orbits. Conditional minima and the outer minimum vary continuously, so successive smaller neighborhoods can enforce this property simultaneously. Positive quotient Hessians and local uniqueness give a phase gap outside a smaller saddle neighborhood within the chosen support. No ultraviolet-uniform error is inferred.

Exact pushforward composition follows from testing against a final test function and ordinary finite-dimensional Fubini. Local submersivity follows from the actual invertible pivot blocks and equivariance. The intermediate density is with respect to product group Haar, and its outer conditional measure is the corresponding coarea density. This prevents an unnoticed change of target density convention.

The corrected Section 6 now states exactly the invariance obtained from this auxiliary cutoff: \(H_L\) invariance of the intermediate density and leading amplitude. This suffices to replace the outer gauge-zero saddle by its pre-gauge representative. Full local output gauge invariance of the actual determinant correction is separately cited from the previously established zero-input leading limit.

## Laplace coefficient and normalization

The elementary finite-dimensional parameter-dependent Laplace estimate is valid on the chosen compact real target germ. The uniform quadratic lower bound controls the scaled chart integral, and the positive phase gap controls the rest of its compact support. Its use with an additional smooth amplitude or a uniformly converging relative amplitude is justified by the same domination.

Inserting the exact contour-gauge Haar identity reduces the constrained orbit integral to the actual retained chart. The absolute gauge penalty is nonnegative and has its unique zero on each based orbit at the specified contour slice. The unique quotient minimizing orbit thus gives the unique leading gauge-fixed saddle. The measure at that saddle is precisely the inverse pivot product times the fixed Haar constants; the retained Hessian is the actual action-plus-gauge precision, with both chart-curvature effects included. Target group Haar introduces no factor \(j(\log W)\).

Consequently the normalized leading amplitude is exactly the existing \(\exp(\Delta+\mathcal Q_{\det})\). Field-independent factors cancel in the ratio at the identity, including compact gauge integrals, powers of \(g\), flat determinants and Haar constants. Their separate asymptotic powers need not be guessed or matched.

The actual sharp retained window has this same leading amplitude when \(T\to\infty\) and \(gT^3\to0\), by the already proved centered parity/cutoff bounds. This identifies a leading coefficient only; it does not assert equality of the auxiliary orbit-tube integral, the direct sharp sector and the sequential sharp sectors at positive coupling.

## Cocycle and scope

The inner uniform Laplace expansion supplies the smooth amplitude \(\exp D_{M,R}\) to the outer integral. The outer stationary phase evaluates it at the existing classical minimum; it carries no inverse-coupling factor and does not shift the leading phase. The two-minimum comparisons identify the same direct classical phase in dimension four. Normalizing direct and sequential expressions at the identity cancels all scalar prefactors and proves
\[
 D_{M,RL}=\mathcal T_{MR,L}D_{M,R}+D_{MR,L}.
\]
Positive real logarithms remove branch ambiguity on the real germ. The already established holomorphic common domains then extend the identity; the auxiliary Laplace germ may be smaller without changing those domains.

For jointly extracted infinite systems the anchored analytic bounds permit passage of this scalar identity on compact fields. True infinite Maxwell preservation yields additive Maxwell coefficients there. A finite short-lift ratio cannot simply remove the transport term, and the note does not do so.

No sign, numerical coefficient, old-depth convergence, full-sector identity, or infinite physical coupling trajectory is obtained. Those limitations are correctly retained.

## Final fragment and substantive re-audit

Read the complete classical_one_loop_cocycle_fragment.tex after its preparation. **Fidelity and substantive proof pass.** The fragment carries the corrected based-\(H_L\) invariance statement and explicitly establishes a combined quotient/gauge phase gap before applying finite Laplace.

Rechecked the following points against the proof foundations:

* The based action is free, and the kernel of the intermediate restriction is exactly the inner based group. Product site Haar is therefore the actual measure used in the insertion, not an unspecified quotient volume.
* Small endpoint fields related by a final-based gauge have a uniformly small logarithm at the fixed \(RL\), with controlled neighboring differences. The entire logarithmic gauge path can be kept inside the upstream Ward domain. This supplies a consistent local saturated action; it is not inferred merely from equality of two minimum values.
* The actual contour slice is transverse to the based action. Positive retained action-plus-gauge Hessian implies positive quotient constrained Hessian there. The implicit-function construction and continuity of the conditional minimizing maps allow one compact auxiliary cutoff to equal one near all inner and outer saddles relevant to a smaller target germ.
* Outside a smaller saddle neighborhood the compact quotient phase gap, together with the nonnegative contour penalty and its unique orbit zero, excludes another contribution at the same leading phase. This is the needed domination for the inner and outer parameter-dependent Laplace arguments; no ultraviolet-uniform remainder is assumed.
* The coarea densities are taken relative to product group Haar. At the saddle the actual chart gives \(h_0^{n_e-n_c}d_K(V_*)\) and the full retained Hessian. There is no omitted target Haar factor, background Haar factor or uncomputed orbit-volume function. Dimension-four action normalization is the one already fixed by the two-minimum comparisons.
* The inner uniform relative remainder can be used as an outer amplitude; its leading value is evaluated at the unshifted classical saddle. Scalar normalization at the identity cancels all coupling-dependent but background-independent prefactors.

The fragment's infinite-system passage, true Maxwell additivity and finite-leakage caveat match the research. Direct versus sequential positive-coupling sharp sectors are explicitly not identified. No further correction is requested.
