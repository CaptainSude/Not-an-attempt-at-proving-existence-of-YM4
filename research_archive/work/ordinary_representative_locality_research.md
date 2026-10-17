# Weighted locality of the chosen ordinary-constraint representative

16 October 2026. Proof consequence independently audited; see `ordinary_representative_locality_audit.md`. This note concerns the explicit ordinary-feasible representative constructed by the cumulative-gauge transfer, not an arbitrary gauge choice. It removes the earlier locality caveat for that particular representative. It does not identify a separately moving source gauge or cover mixed retained histories.

## 1. The transfer map and its local inputs

Retain fixed odd `L`, refinement `M=L^j`, spacing `eta=1/M`, and finite compatible periodic volume. Fix `0<alpha<1`. Let `A_*(B)` denote the selected corrected-constraint minimizer in the fixed flat gauge. It is holomorphic from a uniform small coarse supremum ball into the complete fine potential space `N_alpha=C^(1,alpha)`.

The exact ordinary/corrected relation is

\[
 M^{(j)}(U)=C^{(j)}(U)^{b_j(U)},\qquad U=e^{i\eta A}.
                                                               \tag{1.1}
\]

The cumulative endpoint gauge `b_j` is uniformly bounded and holomorphic on a fixed global potential supremum ball, and `||b_j-I||_infinity<=C||A||_infinity`. Its coefficient at a final coarse vertex depends only on fine potential values in a neighborhood of fixed physical radius `R_b`. This follows from the endpoint product: each corrected intermediate field has physical dependency radius bounded by the sum of preceding one-step radii, and the final product uses a geometric sum of spacings. It holds uniformly in refinement and compatible volume, with lifted incidences on short tori.

Define on the common small logarithm branch

\[
 \omega(A)=\frac1i\log b_j(e^{i\eta A})^{-1}.
                                                               \tag{1.2}
\]

Then `omega(0)=0`, `||omega(A)||_infinity<=C||A||_infinity`, and the same finite physical dependency radius and uniform holomorphy hold for omega.

Let `E_pt` be the point-value extension from the ordinary-constraint transfer: take one fixed smooth bump `phi`, supported in `(-1/2,1/2)^d` with `phi(0)=1`, and periodize

\[
 (E_{\rm pt}c)(x)=\sum_{n\in\mathbb Z^d}\phi(x-n)c(n).
                                                               \tag{1.3}
\]

The gauge transfer is the ordinary potential map

\[
 \lambda(A)=E_{\rm pt}\omega(A),\qquad
 T(A)=\mathscr A_\eta(A,\lambda(A)),             \tag{1.4}
\]

where

\[
 \mathscr A_\eta(A,\lambda)(e)
 =\frac1{i\eta}\log
       (e^{i\lambda(e_-)}e^{i\eta A(e)}e^{-i\lambda(e_+)}).
                                                               \tag{1.5}
\]

Thus the selected ordinary representative is

\[
 A_{\rm ord}(B)=T(A_*(B)).                       \tag{1.6}
\]

All bases in this note are small in their unweighted global norms. A weight is placed on variations, never required of the background itself.

## 2. Weighted derivative of the cumulative gauge

Let `w(n)/w(m)<=exp(kappa d(n,m))`, for a fixed sufficiently small positive kappa. Weighted complete-field norms use unit-cell collars as in the constrained Schauder theorem.

On a smaller fixed complex potential ball, Banach-valued Cauchy gives a uniform row derivative estimate for omega. The weighted version is

\[
 \|D\omega(A)V\|_{\infty,w}
         \le C e^{\kappa R_b}\|V\|_{\infty,w}.
                                                               \tag{2.1}
\]

To prove it, fix a coarse output vertex n. Its value depends only on A in the radius-`R_b` neighborhood. Replace V by its restriction to that neighborhood. No derivative of V is taken: omega consumes bounded potential values only. This local direction has supremum at most `C exp(kappa R_b) w(n)^-1||V||_(infinity,w)`. Cauchy is applied to the whole output row as a bounded linear functional, not entrywise followed by a fine-dimensional sum. Multiplying by w(n) and taking the output supremum proves (2.1).

The same local-row Cauchy argument proves that

\[
 A\longmapsto D\omega(A)
 \quad\hbox{is holomorphic into}\quad
 \mathcal L(\ell^\infty_{f,w},\ell^\infty_{c,w})
                                                               \tag{2.2}
\]

with uniform bounds. It also gives one weighted direction in higher coefficient derivatives, with the other directions unweighted. This does not require a Hölder bound on a sharply restricted direction, since only its supremum is used in this step.

The point extension has a weighted smoothing bound

\[
 \|E_{\rm pt}c\|_{C^{2,\alpha}_w}
                     \le C_\kappa\|c\|_{\infty,w}.       \tag{2.3}
\]

Indeed every collar reads a fixed number of nearby coarse coefficients. Smooth bump derivatives through order three are uniformly bounded, and their coarse weights differ from the collar weight by only a fixed factor. Sampling and integral formulas for finite differences prove (2.3), including the second-difference Hölder member. Periodization preserves the finite overlap bound.

Consequently

\[
 \|D\lambda(A)V\|_{C^{2,\alpha}_w}
                   \le C_\kappa\|V\|_{\infty,w},
 \qquad
 \|\lambda(A)\|_{C^{2,\alpha}}
                   \le C\|A\|_\infty.           \tag{2.4}
\]

The second estimate is deliberately unweighted.

## 3. Weighted derivative of the fine gauge action

The physical regularity estimate for (1.5) has a local jet proof. Put `ell=lambda(e_-)` and `v=(lambda(e_+)-lambda(e_-))/eta`. Its group argument is

\[
 e^{i\eta\operatorname{Ad}_{e^{i\ell}}A(e)}
                 e^{i\ell}e^{-i(\ell+\eta v)}.    \tag{3.1}
\]

At eta zero this is identity for every small jet `(A,ell,v)`. Its logarithm divided by `i eta` therefore extends analytically at eta zero, with uniform finite-dimensional derivative bounds for `0<=eta<=1` on a smaller fixed complex jet ball. Thus (1.5) is a local analytic function of `(A,lambda,Dlambda)` with no inverse-mesh coefficient loss.

At an unweighted small base `(A,lambda)` in `N_alpha x C^(2,alpha)`, the derivative is a finite sum of products of analytic coefficient functions of that base jet and the variation jet `(V,mu,Dmu)`. The coefficients have uniformly bounded unweighted `C^(1,alpha)` norms. The complete-field discrete product estimate, with one factor weighted, proves

\[
 \|D\mathscr A_\eta(A,\lambda)[V,\mu]\|_{N_{\alpha,w}}
  \le C_\kappa
        (\|V\|_{N_{\alpha,w}}+\|\mu\|_{C^{2,\alpha}_w}).
                                                               \tag{3.2}
\]

For example a first output difference uses the first difference of the coefficient or the variation jet; the latter requires at most two differences of mu. The alpha-Hölder product bound uses the same derivatives and fixed collars. Finite shifts change weights by a fixed factor. No background field is assumed to have a finite growing-weight norm.

The coefficient argument also proves operator-valued holomorphy of this derivative with the background in its unweighted regularity domain. Combining (2.4) and (3.2) gives

\[
 \boxed{\quad
 \|DT(A)V\|_{N_{\alpha,w}}\le C_\kappa\|V\|_{N_{\alpha,w}}.
 \quad}                                                       \tag{3.3}
\]

The family `A -> DT(A)` is holomorphic into the indicated weighted operator norm, on a common smaller unweighted `N_alpha` ball. The proof uses the local row estimate for the only non-jet dependence, namely omega. Every other dependence is a fixed local analytic jet operation or the fixed finite-range smooth interpolation.

## 4. The correct leading extension

The weighted response theorem for the corrected minimizer supplies

\[
 \|D_BA_*(B)b\|_{N_{\alpha,w}}\le C_\kappa\|b\|_{\infty,w},
 \qquad D_BA_*(0)=H.                             \tag{4.1}
\]

By (1.6) and (3.3),

\[
 D_BA_{\rm ord}(B)=DT(A_*(B))D_BA_*(B),
\]
\[
 \|D_BA_{\rm ord}(B)b\|_{N_{\alpha,w}}
                      \le C_\kappa\|b\|_{\infty,w}.
                                                               \tag{4.2}
\]

Its leading extension is

\[
 \boxed{\ H_{\rm ord}=DT(0)H\ },                 \tag{4.3}
\]

which must not be replaced by H. An explicit sign check is useful. Write

\[
 \beta(A)=\frac1i\log b_j(e^{i\eta A}),\qquad
 B_{\rm cum}=D\beta(0).
\]

On the common branch `omega=-beta`. At `(A,lambda)=(0,0)`, the gauge action has derivative `V-Dmu`. Hence

\[
 DT(0)=I+D E_{\rm pt}B_{\rm cum},\qquad
 H_{\rm ord}=H+D E_{\rm pt}B_{\rm cum}H.         \tag{4.4}
\]

In particular `dH_ord=dH`: the linear correction is a fine gradient. The exact ordinary/corrected identity also gives

\[
 \mathcal F_{\rm ord}(T(A))=\mathcal F_{\rm corr}(A)
                                                               \tag{4.5}
\]

on the small potential branch, where the maps are the physical logarithms of their group outputs at final spacing one. Indeed the point restriction of the gauge in (1.4) is `b_j(U)^-1`, which cancels the cumulative coarse gauge in (1.1) in the correct order. Thus if `Q_ord=D mathcal F_ord(0)`, then `Q_ord DT(0)=Q`, and `Q_ord H_ord=I`. This is a check on (4.3), not an identification with a different source gauge extension.

The first response in (4.2) is holomorphic into the weighted operator norm on an unweighted complex coarse ball. Uniform operator Cauchy, or the directly differentiated local formulas, consequently yields on a fixed smaller ball

\[
 \|(D_BA_{\rm ord}(B)-H_{\rm ord})b\|_{N_{\alpha,w}}
       \le C_\kappa\|B\|_\infty\|b\|_{\infty,w}.
                                                               \tag{4.6}
\]

No weighted norm of the base minimizer or of its gauge is required.

## 5. Higher responses and finite localized changes

Let delta be the fixed distance of a smaller coarse background ball from the boundary of a ball where (4.2) holds holomorphically with a uniform bound. For every n>=1,

\[
 \boxed{\quad
 \|D_B^nA_{\rm ord}(B)[b_1,\ldots,b_n]\|_{N_{\alpha,w}}
 \le C_\kappa(n-1)!\left(\frac e\delta\right)^{n-1}
       \|b_1\|_{\infty,w}\prod_{i=2}^n\|b_i\|_\infty.
 \quad}                                                       \tag{5.1}
\]

For n>1, apply multivariable Cauchy to the first-response operator family with n-1 independent unweighted background directions, using polyradii approaching `delta/((n-1)||b_i||)`. The bound follows from `(n-1)^(n-1)<=e^(n-1)(n-1)!`. For n=1 it is (4.2). Symmetry allows any selected bounded direction to carry the weight.

If b_1 is supported in S and `w_S(n)=exp(kappa d(n,S))`, (4.2) and (5.1) give exponential response decay from S. If every b_i is supported in S_i, separate application with each weighted direction gives the valid output factor `exp(-kappa max_i d(n,S_i))`; no tree-length estimate is inferred.

For two coarse backgrounds in the common ball,

\[
 \|A_{\rm ord}(B')-A_{\rm ord}(B)\|_{N_{\alpha,w}}
               \le C_\kappa\|B'-B\|_{\infty,w}.   \tag{5.2}
\]

This follows by integrating (4.2) along the straight coarse segment. If their difference is supported in S, the same exponential decay follows. On complete infinite fields one may use bounded truncated weights and pass to the limit, exactly as for the corrected representative; finite total action is not assigned to arbitrary bounded infinite fields.

For arbitrary admissible weights which decay to zero on an infinite lattice, literal Fréchet derivatives are first asserted on globally bounded directions with finite weighted norm. The local formulas and weighted inverse define their bounded extension to the full weighted space. This distinction is unnecessary for the growing support weights `w_S>=1`.

## 6. Scope

The result proves weighted response locality for the **specific** ordinary-feasible representative obtained by the cumulative-gauge inverse and fixed bump extension in (1.2)–(1.6). A field-dependent gauge change does not preserve locality automatically; its locality was proved here through (2.1)–(3.3).

The same first-response, higher one-weight factorial, and finite-localized-change conclusions now hold for this representative as for the corrected fixed-slice representative, with its own leading extension `H_ord`. No claim is made about an arbitrary gauge-equivalent representative, the source's separately prescribed moving minimizer gauge, mixed retained geometries, or tree-length bounds. The existence and action-minimum statement remains that of the already proved finite homogeneous small-global-field theorem.
