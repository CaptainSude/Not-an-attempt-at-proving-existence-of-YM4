# Independent audit: local gauge covariance of the chart integral

17 October 2026. Reviewed `small_field_gauge_covariance_research.md` against the actual ordinary-average/pivot definitions in `physical_current_pivot_precision_research.md`, the Haar and straightening formulas in `physical_pivot_measure_fragment.tex`, the normalized integral in `classical_step_integration_fragment.tex`, and the proved classical gauge invariance in `classical_coarse_action_fragment.tex`. No output or Notebook23 file was edited. This is internal review, not external certification.

**Verdict:** the local classical-reference covariance and the resulting total Ward identity are supported by those inputs. The inherited-interaction extension needs an explicit nonvanishing/logarithm hypothesis in addition to convergence. The cutoff norm should be stated to be adjoint invariant, as the actual retained-bond norm is intended to be.

## 1. Existing action invariance really covers the block lift

The classical coarse-action proof allows an arbitrary sufficiently small current site field omega in supremum norm. It requires no additional current regularity: current spacing is one, and its first differences are bounded by twice that norm. Its fine extension uses the smooth point-value map E_pt at the current physical scale, with C^(2,alpha) norm controlled independently of M. Hence the blockwise constant current lift of a small next-coarse site gauge is included. Jumps between L-blocks are current-scale jumps, not jumps at the old fine mesh spacing M^-1.

The available theorem does require the original and transformed fields, and the comparison configurations, to lie in its common smaller domain. Choosing the next-coarse gauge and background norms small enough ensures this uniformly in M; it is not enough to assert equality merely because a formal group action exists. The candidate explicitly imposes these common-domain restrictions.

Internal averaged contours transform by u(y) P_V(y,x) u(y)^-1 under the block lift. The ordinary average transforms by its usual coarse endpoint gauges. Thus the absolute gauge penalty is invariant and the P=1 condition is preserved. Transporting constrained stationarity through the gauge diffeomorphism is legitimate because both the classical action and that actual absolute penalty are invariant in an open neighborhood. The known uniform common-chart uniqueness then identifies the transformed physical branch with V_*(W^u). Gauge-zero is not deduced from criticality alone.

## 2. The exact nonlinear relative chart transforms correctly

For the left-relative field X and v=u^up,

    exp(i Ad_(v(b_-))X(b)) V^v(b) = (exp(iX)V)^v(b).

The left-relative product of its coarse average with the inverse background average therefore transforms by conjugation at the initial coarse endpoint. Conjugacy covariance of the common small logarithm proves equation (3) of the candidate. Its nonlinear pivot solution is unique for prescribed retained coordinates; restriction of the adjoint action to those coordinates is precisely D_u. Therefore equation (4), Phi_(V^v)(D_u z)=R_u Phi_V(z), follows at the full nonlinear level.

For real small gauges, D_u is orthogonal in the invariant trace norm, and its determinant is +1. The latter follows from continuity of the real adjoint representation on a connected compact group. No independent assumption that the flat insertion K_L commutes with the local gauge is used or needed.

**Cutoff clarification:** a retained rectangle here must mean the product over retained bonds of balls in an Ad-invariant color norm, for example the trace Euclidean norm used by the source cutoff. A componentwise scalar cube in an arbitrary color basis would not in general be invariant under D_u. The current proof is valid for the actual product of bond-norm cutoffs; stating that convention explicitly removes the ambiguity in the word rectangle.

## 3. Gaussian, Haar and delta/straightening normalizations

The full identity T_(V^v)(D_u z)=T_V(z) uses the actual absolute gauge penalty and the classical action, including their nonlinear coordinate conversions. Differentiating twice gives

    D_u^T A_M(V^v) D_u=A_M(V),

and hence A_M(V^v)=D_u A_M(V)D_u^T for real gauges. The counting Gaussian transforms exactly by this real orthogonal change of variables. Its determinant and normalization are unchanged. Constant, linear and quadratic Taylor parts transform separately, so the centered analytic extension is covariant even where the first derivative is not zero. At the physical branch it agrees with the actual centered fluctuation factor.

Haar pullback density is adjoint invariant because Haar measure is conjugacy invariant and det Ad_u=1. It remains true on eliminated pivots because the full nonlinear chart, not only its retained part, obeys equation (4).

Differentiating the relative constraint in the pivot gives the candidate's two-sided adjoint transformation of A_(V,c,p). Both adjoint determinants equal one. This proves invariance of each pivot determinant and the separated product D(V). At the nonlinear pivot solution the same transformation proves invariance of the denominator in the exact ambient determinant ratio. Thus the normalized straightening factor is preserved. Its identification uses the square ambient Jacobian formula, not a determinant of the rectangular D Phi_V.

The baseline A_(M,0) need not transform under the local gauge. It appears only through the fixed scalar det A_(M,0) in Q_M; det A_M(V^v)=det A_M(V) suffices. Likewise D(1) is a fixed scalar reference. These normalizations therefore create no missing field-dependent gauge factor.

All change-of-variable arguments are on the real retained window. Complex-background covariance follows by holomorphic identity on the common small parameter domain, not by applying a complex adjoint transformation to the sharp indicator.

## 4. Logarithms, especially the inherited correction

For the classical-reference integral the previous integration theorem already supplies nonvanishing and a canonical holomorphic logarithm on the specified product domain. The local determinant factors are nonvanishing on their fixed small neighborhoods, with branches normalized at the identity. Real positivity also supplies compatible real branches. Thus its total correction can be made exactly invariant, not merely invariant modulo 2 pi i.

For an additional holomorphic, gauge-invariant current functional E(U), the real change of variables still proves invariance of the integral whenever the substituted integral exists and the whole common domain is respected. But holomorphy and convergence alone do not imply that the resulting integral has no zeros. Its logarithm therefore needs an additional hypothesis:

* the inherited-interaction normalized integral is nonzero on the relevant connected common domain, with a chosen holomorphic branch of its logarithm;
* that branch is compatible at the identity gauge and along the small gauge path, or equivalently comes from the common canonical zero-free expansion.

Under these hypotheses, log Z(V^u)-log Z(V) is a continuous 2 pi i integer on the small connected gauge-parameter domain and is zero at u=1, so it vanishes. If one has only the integral, only covariance of that integral is established. Positivity can justify this on the real slice for a real-valued E, but it does not replace a complex zero-free-domain argument. This is the only additional substantive hypothesis needed in the inherited-log extension as written.

## 5. Ward identity and its limit scope

For the semisimple Lie algebra, invariance under small constant gauges implies DF(0)=0: each bond component of that covector is adjoint invariant, and the dual fixed space is zero. Differentiating local gauge invariance in a site parameter and then in w gives D^2F(0)[v,D_1 lambda]=0. The derivative of the nonlinear gauge generator is multiplied by DF(0) and therefore vanishes. The sign convention for the gradient does not affect this zero identity.

This is a statement about the total functional, not an arbitrary chosen support coefficient. It does not classify the gauge-invariant quadratic form or identify one marginal coefficient.

The optional Fourier conclusion is correctly conditional on a translation-invariant infinite-volume kernel with uniform exponential summability and actual convergence. Those assumptions allow passage of the lattice Ward identity to the infinite kernel and its analytic Fourier multiplier. Setting p=t e_mu gives K(t e_mu)e_mu=0 for nonzero small t, hence K(0)=0 by continuity. A finite periodic regulator alone would not justify this continuous-momentum step. No mass-gap or beta-function statement follows from this quadratic identity.

## 6. Earlier norm patch confirmed

The maximum-over-field-types-inside-the-support-sum convention is present in `classical_support_localization_fragment.tex` immediately after `cl-family-norm`, and in Section3 of `classical_support_localization_research.md`. The wording explicitly distinguishes it from a maximum of separate family norms and specifies joint-cell Taylor norms plus a component-sum linear source bound. Rebuilding Notebook21 from those work files carries the requested clarification. The alternative colored-slot convention in the stationary theorem is separately justified by its scalar-coordinate majorant.
