# A uniform neighborhood for the flat auxiliary current family

16 October 2026. This is a quantitative theorem for the fixed-flat-background family defined at deposited Raw I:13725–13731. Its fine-inverse input is stated explicitly in Section 1 and has now been proved in `flat_full_inverse_research.md` and independently checked in `flat_full_inverse_audit.md`. The current argument itself is independently checked in `flat_auxiliary_current_neighborhood_audit.md`. The hypotheses below remain explicit so the logical dependence is visible. The source average, scalar source projector, and normalized zero-current extension are those matched in Notebook 08. The current perturbation is **only** `Theta'_J`; the additional `Pi^*Theta_J Pi` in the actual full `G_1^J` is excluded.

## 1. Precise uniform inputs and norms

Fine fields are grouped into unit coarse cells and have the physical cell norm `M^{-d} sum |A|^2`. Coarse fields have their fixed orientation/color Hilbert fibers. Let `B_kappa` denote the block-matrix Schur algebra with norm

\[
 \|T\|_\kappa=
 \max\left\{
 \sup_x\sum_y e^{\kappa d(x,y)}\|T_{xy}\|,
 \sup_y\sum_x e^{\kappa d(x,y)}\|T_{xy}\|
 \right\}.
\]

Use `d(x,y)=|x-y|_1` in infinite volume and periodic distance on a finite compatible torus. Rectangular fine-to-coarse and coarse-to-fine matrices use the same definition. The norm is submultiplicative, and the identity has norm one. Fixed physical adjoint/transposition has the same norm. At complex current, transpose means the fixed analytic bilinear transpose.

Assume, uniformly in odd `M` and in all compatible periodic volumes,

\[
 \|G_0\|_\kappa\le g,\qquad
 \|Q\|_\kappa,\|Q^*\|_\kappa\le b,\qquad
 \|q_0\|_\kappa\le q,
 \tag{1.1}
\]

where

\[
 G_0=(K+DRD^*+Q^*aQ)^{-1},\quad
 q_0=(QG_0Q^*)^{-1},\quad E_0=G_0Q^*q_0.
\]

Here the `G_0` bound is the separately proved flat input. The `Q,Q^*` bounds follow from the explicit flat straight average and its fixed cell range with the physical measures. The bound for `q_0` follows from `q_0=q_M+a`, the earlier Maxwell precision locality, and a fixed uniformly bounded coarse penalty. The constants may depend on the specified penalty range, dimension, fixed color space, and `kappa`; they may not depend on `M` or volume.

The already checked scalar-current note supplies

\[
 \|\Theta'_J\|_\kappa\le\theta\|J\|_\infty,
 \tag{1.2}
\]

linearly in arbitrary complex fine-bond current `J`. No derivative of `J` is required. It also supplies the local factorization

\[
 \Theta'_J
 =\mathfrak j_J^*\Lambda+\Lambda^*\mathfrak j_J
  +\Lambda^*V_JD\Lambda+(D\Lambda)^*V_J^*\Lambda,
 \tag{1.3}
\]

where `mathfrak j_J,V_J` have fixed finite incidence and norm `O(||J||_infinity)`, while `Lambda,D Lambda` have uniform weighted bounds. For source-locality statements use one common positive `kappa` for all these inputs.

Finally, the exact flat source gauge gives

\[
 \Lambda E_0=0,\qquad E_0^*\Theta'_JE_0=0
 \tag{1.4}
\]

for every current. This is the algebra audited in `flat_current_locality_audit.md`.

## 2. One explicit neighborhood controls both inverses

Define

\[
 c=gb^2q,\qquad e=gbq,\qquad
 \varepsilon=\frac{1}{4g\theta(1+c)}.
 \tag{2.1}
\]

If `theta=0` the perturbation is zero and the assertions have no smallness restriction. Otherwise suppose `||J||_infinity<epsilon`, and abbreviate `Theta=Theta'_J`.

Since `||G_0Theta||_kappa<=1/4`, the fine inverse exists in the Schur algebra:

\[
 G_J=(I-G_0\Theta)^{-1}G_0,
 \qquad \|G_J\|_\kappa\le2g,
\]

\[
 \|G_J-G_0\|_\kappa
 \le2g^2\theta\|J\|_\infty.
 \tag{2.2}
\]

This is the displayed auxiliary `G_pi^J` wherever the original Neumann series is used. Let `W_J=QG_JQ^*`. Then

\[
 \|q_0(W_J-W_0)\|_\kappa
 \le2qb^2g^2\theta\|J\|_\infty
 <\frac{c}{2(1+c)}<\frac12.
\]

A second Neumann series gives

\[
 q_J=W_J^{-1}
   =[I+q_0(W_J-W_0)]^{-1}q_0,
 \qquad \|q_J\|_\kappa\le2q.
 \tag{2.3}
\]

Thus

\[
 E_J=G_JQ^*q_J,\qquad QE_J=I,
 \qquad \|E_J\|_\kappa\le4e.
 \tag{2.4}
\]

All Neumann series converge in operator norm in the same Schur algebra. They define holomorphic maps on the complex Banach ball `||J||_infinity<epsilon`, uniformly in `M` and volume. This is an actual uniform auxiliary-current neighborhood conditional on (1.1), not just separate finite-regulator derivatives.

## 3. Exact quadratic remainder and the correct inverse ordering

Set

\[
 B_0=G_0-E_0QG_0
     =G_0-E_0q_0^{-1}E_0^*,
 \qquad \|B_0\|_\kappa\le t_0:=g(1+c).
 \tag{3.1}
\]

It is the constrained covariance, is symmetric, and satisfies

\[
 QB_0=B_0Q^*=0,\qquad
 B_0\Delta_0=I-E_0Q.
\]

Apply `B_0` to `(Delta_0-Theta)E_J=Q^*q_J`. Using `QE_J=I` gives

\[
 E_J-E_0=B_0\Theta E_J.
\]

Therefore

\[
 E_J=E_0+(I-B_0\Theta)^{-1}B_0\Theta E_0.
 \tag{3.2}
\]

The ordering is `I-B_0Theta`, as displayed; no commutation is used. The chosen radius gives `||B_0Theta||<1/4`. Multiplication of the stationary equation by `E_0^*` gives

\[
 q_J=q_0-E_0^*\Theta E_J.
\]

Combining with (3.2) and (1.4),

\[
 \boxed{\quad
 q_J-q_0
 =-E_0^*\Theta(I-B_0\Theta)^{-1}B_0\Theta E_0.
 \quad}
 \tag{3.3}
\]

In particular,

\[
 \|q_J-q_0\|_\kappa
 \le2e^2\theta^2t_0\|J\|_\infty^2,
\]

\[
 \|E_J-E_0\|_\kappa
 \le2t_0\theta e\|J\|_\infty.
 \tag{3.4}
\]

No Cauchy estimate is needed for the quadratic remainder. At zero current the second derivative reduces to the previously proved expression with `Z=G'RG'`, because `B_0Lambda^*=DZ` and `Lambda DZ=Z`.

## 4. Exact derivatives at every point of the neighborhood

Define the current constrained covariance

\[
 B_J=G_J-E_JQG_J.
\]

It has uniform bound

\[
 \|B_J\|_\kappa\le t:=2g(1+4c).
 \tag{4.1}
\]

At a fixed point `J` in the ball, a sufficiently small increment `K` satisfies the exact identities

\[
 B_{J+K}=(I-B_J\Theta'_K)^{-1}B_J,
\]

\[
 E_{J+K}=(I-B_J\Theta'_K)^{-1}E_J,
\]

\[
 q_{J+K}=q_J-E_J^*\Theta'_K(I-B_J\Theta'_K)^{-1}E_J.
 \tag{4.2}
\]

The latter two follow from the stationary equations as in Section 3. The first is the resolvent identity for the restricted quadratic form on `ker Q`; equivalently it follows by subtracting the two constrained Green equations. It is an identity on all fine fields after extending the constrained inverses by zero on `ran Q^*`. No background or current variation of `Q` occurs.

For `n>=1`, expansion of (4.2) yields

\[
 \boxed{\quad
 D^nq_J[J_1,\ldots,J_n]
 =-\sum_{\sigma\in S_n}
 E_J^*\Theta'_{J_{\sigma(1)}}B_J
 \Theta'_{J_{\sigma(2)}}\cdots B_J
 \Theta'_{J_{\sigma(n)}}E_J.
 \quad}
 \tag{4.3}
\]

There are exactly `n-1` constrained covariance factors; for `n=1` there are none. The extension derivatives similarly contain `n` factors `B_JTheta'` followed by `E_J`, summed over permutations. In particular,

\[
 \|D^nq_J[J_1,\ldots,J_n]\|_\kappa
 \le n!(4e)^2\theta^n t^{n-1}
       \prod_i\|J_i\|_\infty,
 \tag{4.4}
\]

\[
 \|D^nE_J[J_1,\ldots,J_n]\|_\kappa
 \le n!(4e)(t\theta)^n\prod_i\|J_i\|_\infty.
 \tag{4.5}
\]

These are factorial constants for the auxiliary current map in the stated cell-Hilbert norm. They are not claims about arbitrary background derivatives or the source correlation coefficients of the full nonlinear construction. At `J=0`, the `n=1` precision expression is identically zero by (1.4).

## 5. Anchored locality of all current derivatives

Let `J_x` be supported on fine bonds with basepoint in cell `x`. Each coefficient map in (1.3) then reads and writes only a fixed neighboring-cell set of `x`; its restricted operator norm is `O(||J_x||_infinity)`. The remaining factors in (1.3) are among `I,Lambda,D Lambda` and their transposes, all uniformly bounded in the weighted algebra.

Insert (1.3) into a chain in (4.3). After restricting each coefficient vertex to its neighboring-cell set, the factors between consecutive vertices are products of the form

\[
 A B_J C^*,\qquad A,C\in\{I,\Lambda,D\Lambda\},
\]

with the appropriate fixed scalar/bond domains. Their cell block norms are bounded by a constant times `exp(-kappa d(x,y))`. The end factors similarly use `A E_J`. These statements are block-operator estimates in physical Hilbert norms; no sum over fine site coordinates is bounded entry by entry.

There are at most four choices from (1.3) per current insertion and a fixed number of neighboring cells. Absorbing those choices and offsets into constants gives

\[
 \begin{aligned}
 &\|D^nq_J[J_{x_1},\ldots,J_{x_n}](b,c)\|\\
 &\quad\le C_0 C_1^n\prod_i\|J_{x_i}\|_\infty
 \sum_{\sigma\in S_n}
 \exp\!\left[-\kappa\left(
 d(b,x_{\sigma(1)})
 +\sum_{i=1}^{n-1}d(x_{\sigma(i)},x_{\sigma(i+1)})
 +d(x_{\sigma(n)},c)\right)\right].
 \end{aligned}
 \tag{5.1}
\]

All constants are independent of `M`, volume and source locations. Repeated source cells are allowed. The corresponding extension derivatives have the same anchored-chain structure with their respective fine/coarse end fibers. The special zero-current Hessian formula with `Z` remains the more explicit expression for `n=2`.

The proof uses weighted operator norms of the propagators, rather than convoluting pointwise bounds at a borderline exponent. Hence it does not create an unaccounted polynomial in source separation. On finite tori the same argument uses periodic distance and includes the exact periodization already built into the input kernels.

## 6. Optional transfer of physical fine derivatives

This section is conditional on whatever fine-derivative bounds are actually established for `G_0`. It makes no new pointwise assertion. Suppose a specific output/input sandwich `D^alpha G_0 (D^*)^beta` is uniformly bounded in the same weighted cell-Hilbert algebra, as are the needed one-sided factors `D^alpha G_0` and `G_0(D^*)^beta`. Then the exact resolvent formula gives

\[
 \begin{aligned}
 D^\alpha G_J(D^*)^\beta
 ={}&D^\alpha G_0(D^*)^\beta\\
 &+(D^\alpha G_0)\Theta
       (I-G_0\Theta)^{-1}G_0(D^*)^\beta.
 \end{aligned}
 \tag{6.1}
\]

Thus that derivative sandwich remains uniformly bounded throughout the same current ball. Derivatives act on the outside propagator factors; no derivative of `J` occurs. If the separate flat inverse theorem proves all sandwiches of total order at most two, this gives exactly those sandwiches at nonzero auxiliary current. One-sided bounds also give the corresponding fine derivatives of `E_J=G_JQ^*q_J`.

The conclusion is in physical cell `L^2` operator norms. It does not identify the source account's pointwise, Hölder, or full analytic-carrier norms, and does not infer such norms by comparing dimensions of fine Hilbert spaces.

## 7. Exact scope and remaining input

The independent flat inverse proof and audit now supply (1.1) and the total-order-at-most-two sandwiches in Section 6. Thus Sections 2–6 hold within this homogeneous flat setup: a volume- and refinement-uniform complex current ball, weighted locality, an exact quadratic precision remainder, and factorial current derivatives with anchored spatial paths for the displayed auxiliary family. Optional derivative claims require precisely the additional sandwiches in Section 6.

The theorem does not establish the full `G_1^J`: its additional nonlinear-constraint term `Theta_J` must be analyzed separately. It also does not extend the background from `U=1`, cover multiscale retained-region boundaries, identify all current coefficient conventions in the eventual interacting expansion, or provide a Yang–Mills ultraviolet limit. Those restrictions are mathematical scope, not loss of the uniformity proved here.
