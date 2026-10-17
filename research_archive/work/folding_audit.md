# Independent audit of the same-limit RP assembly

16 October 2026. Audit by the gauge-layer subagent. This note records which implications have been checked and is not a substitute for the individual proofs.

## Checked inputs

1. `gauge_layer_research.md`: complete local gauge-invariant two-layer reduction, conditional on the independently checked SU(2) convolution lemma. The root agent has independently checked this derivation.
2. `transfer_schatten_research.tex`: normalized coordinate transfer operator, physical gauge projection, alternating site/link boundary gluing, and even-Schatten estimate. The physical factor at a link join is C^(1/2)P, whose contraction gives CP. At a site join the extra P in VP is absorbed by adjacent physical temporal cores. Clean sources do not read the abstract square-root variables. No positivity of the square-root kernel is required.
3. `two_frame_geometry_research.md`, especially §7: the period-index generators, reduction to the brick (2A,8A,4A,4A), even slab counts, and injection of coarse insertion boxes after quotienting all check out. Counts are N=2n^4/h^4, N'=2n^4/H^4, N''=n^4/w^4.
4. `diagonal_fold_research.md`: independently read in full. The diagonal graph classification, feature norm, exact boundary Haar/feature gluing, Hilbert–Schmidt estimate, odd-width boundary types, sheared closing trace, even-pair unitary cancellation, and sequential four-direction cellwise inequality agree with an independently reconstructed derivation. The strict cell-interior support hypothesis suffices for all source and insertion functions in this application. No unproved "standard folding" step remains in these finite-volume identities.

One corrected geometric overclaim: the original box has a margin greater than 2h in the coordinate cell, but a coarse image has an additional residual shift of magnitude less than 2h. Thus the original argument only proves strict inclusion for all images, not a uniform margin greater than 2h. Because the insertion cut is on the half-integer mesh, the resulting integer slab gaps still satisfy 1≤ell≤2w−1. This finite fixed set is sufficient for the pressure argument.

## Exact source and operator count after the two folds

Write Z_D(F) for the unnormalized Wilson integral, V for the reflected source array, and G=G_X. The proposed full folding lemma gives

    |μ_(D,t)(G)|^(N')
       ≤ Z_D(exp(tV) Π_g gG) / Z_D(exp(tV)).

In the coordinate-cell decomposition, exactly N' cells contain one insertion. Let m_c be the number of original source copies assigned to cell c; then Σ_c m_c=N. The full coordinate fold of cell c has N'' insertion copies if occupied, and N''m_c source copies.

Use the UNNORMALIZED version of the coordinate slab estimate. For an occupied cell its source cost is exp(|t|N''m_c||O||∞), and its operator norm product is ||X||^(N''). An empty cell has the same source cost without the operator factor. Reflection and lattice relabeling can replace X by its adjoint or unitary/antiunitary conjugate; all have norm ||X||.

The coordinate chessboard exponent 1/N'' and product over all cells consequently leave

    ||X||^(N') exp(|t|N||O||∞) exp(p_β Vol+o(Vol)).

The denominator is at least

    exp(−|t|N||O||∞) exp(p_β Vol+o(Vol)).

Taking the N'-th root gives

    limsup_n |μ_(D_n,t)(G_X)|
       ≤ exp(2|t|(H/h)^4||O||∞) ||X||.

The pressure error is uniform because, after the pointwise source bound, only finitely many unperturbed rectangular shapes occur: the possible integer gaps form a fixed finite set, and there are finitely many time directions. No uniform pressure theorem for tilted sources is needed. The coarse scale H depends on the support of X, not its operator norm, which suffices for the local unitization I+isA.

This assembly uses the FULL cellwise folding inequality; a single-slab Holder inequality alone would not be enough. That stronger statement is now explicitly proved in `diagonal_fold_research.md` and has passed this independent audit.

## Unital functional and reflection invariance

The final section of `transfer_schatten_research.tex` checks out provided the amplification bound includes the local unitization I+isA. A norm-one unital functional L obeys

    |1+isL(A)|²≤1+s²||A||²

for self-adjoint A and both signs of s, so Im L(A)=0. Linearity gives L(X*)=overline(L(X)). Because the comparison limit is a probability law, expectation commutes with complex conjugation. Together with the crossing-kernel swap identity, this proves ordinary reflection invariance of the G_X insertions.

The finite Peter–Weyl kernel approximants commute with endpoint gauge transformations and uniformly approximate every smooth gauge-invariant two-layer observable after division by the strictly positive electric kernel. Their operator norms need not be uniformly bounded; the tilt is removed for each fixed approximant first. The paired layer-reduction estimate then gives reflection invariance for gauge-invariant local observables. Gauge invariance of the law extends this to all local cylinder functions by endpoint Haar averaging, which commutes with the lattice reflection.

## Scope

All statements here are at a fixed finite β. This audit does not establish any estimate uniform in the ultraviolet cutoff, interchange thermodynamic and continuum limits, continuum rotation invariance, or a mass gap.

## Convex-separation closure and common-law quantifiers

No uniqueness statement is needed for the following closure. Fix the desired diagonal mirror through zero and let R be the set of probability laws on the infinite compact link configuration space that are gauge invariant, invariant under 2Z^4 translations, and reflection positive at that fixed mirror. Include reflection invariance explicitly if desired. This is a closed convex compact set: each condition is an equality or a nonnegative inequality for expectations of continuous cylinder functions.

For each real gauge-invariant local Peter–Weyl polynomial P, translate P by an even lattice vector into a sufficiently large diagonal source cell adjacent to the fixed mirror. Such a placement exists because the allowed even translations form a full-rank sublattice, while the cell size can be enlarged. The original coordinate-periodic limit ν is translation invariant. The first fold and the ordered limits volume→infinity, tilt→zero give a comparison law λ_P with

    ν(P)≤λ_P(P),

after translating back using λ_P's even translation invariance. The latter invariance follows by applying amplification at two adjacent clean link planes in each coordinate direction, using the unital-functional and paired layer-reduction arguments. Diagonal RP comes directly from the adapted tilted torus at the original fixed diagonal wall. Thus λ_P belongs to the same set R, even though its source-cell size and clean-plane locations may depend on P.

If ν were outside R, compact convex separation would provide a continuous real test with ν(P)>sup_(λ∈R)λ(P). Cylinder approximation, finite Peter–Weyl approximation, and endpoint gauge averaging preserve a strict separation, so such a test can be chosen among the preceding gauge-invariant local polynomials. This contradicts the comparison inequality. Therefore ν belongs to R.

The gauge averaging here concerns a TEST FUNCTION, not averaging translates of an RP state. It preserves the separating inequality because ν and every member of R are gauge invariant; it does not invoke the false claim that arbitrary translation averaging preserves RP.

The common-law quantifier is valid. First fix the separating source O and its h-cell array. For each fixed t>0, choose one weak subsequential law λ_t of the entire D_n,t family along the original coordinate-torus subsequence. The amplification inequality is a limsup bound for the full finite-volume family, separately valid for every fixed local X once the volume is large enough. Hence EVERY such λ_t satisfies ALL those bounds. The support-dependent widths w,H affect the proof of the bound but do not change D_n,t or require a new limiting law. Next choose one weak limit λ of λ_t as t decreases to zero. Every G_X is a bounded continuous cylinder function, so this same λ satisfies the norm inequality for all admissible X. No X-dependent extraction is used.

For I+isA, the insertion support is the same fixed support as A, so the geometric constants are independent of the functional argument s. The source tilt t and functional argument s must not be conflated. After t is removed, both signs of s are available for the unital-functional argument.

## Minor presentation repairs identified during audit

In §6 of the diagonal fold note, the proof can be carried out at the actual starting slab boundary. It should not suggest moving an odd-width slab to a reference boundary by a nonlattice pure-normal translation. The only required comparison translation is the integral paired displacement b v, already explicit in that proof.

The explicit inverse-convolution/layer-removal proof is SU(2)-specific. The diagonal feature proof applies to SU(N); its coordinate folding analogue also only needs a positive trace-class electric convolution, which follows directly from the same continuous positive feature kernel. Injectivity and polynomial inverse-convolution bounds are not needed for the finite folding identities. None of this extends the completed layer-removal argument to SU(N) without the separate spectral ratio input.
