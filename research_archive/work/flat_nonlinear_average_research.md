# A uniform complex ball for the complete corrected averaging iterate

16 October 2026. New proof, checked by a separate internal mathematical/source audit; retained as a research candidate, with no external certification or output promotion implied. Fixed identity reference background, fixed odd one-step ratio `L>=3`, refinement `M=L^j`, final physical scale one. This extends the quadratic-jet argument of `flat_full_constraint_current_research.md` to the full corrected nonlinear composition. Constants may depend on L, dimension, the fixed color norm, and the specified one-step prescription; they do not depend on j, M or compatible periodic volume. This is a theorem about the actual corrected composition in its fixed flat-reference logarithmic coordinates. It does not identify its derivative at a nonzero field with the separately left-trivialized source operator `Q(U)`.

## 1. Source input and a finite one-step analytic neighborhood

The exact deposited inputs are Raw I:24320--24325 (the corrected nonlinear operation is composed at every step, with the averaged reference background); I:24332--24336 (two final blocks suffice for its dependence); I:24344--24353 (logarithmic coordinate, flat linear part and quadratic remainder); I:24357--24369 (flat linearization is the normalized straight-string average). At identity reference background all intermediate reference backgrounds remain identity.

The input-coordinate bridge is I:47076--47087, using the maps defined at I:46965--46973. In the notation of the previous note it gives the explicit one-step map

\[
 F_L(X;c)=\frac1i\log\left[
 e^{-i\alpha_{c_-}(X)}e^{i\phi(X;c)}e^{i\alpha_{c_+}(X)}\right],
 \qquad DF_L(0)=LQ_L^{\rm st}.
 \tag{1.1}
\]

This is a local finite-dimensional analytic map on an identity logarithm branch. Its elementary group products, means and logarithms have a common complex neighborhood of zero for the fixed finite one-step geometry. Translations use the same local map; the finite set of orientation types only changes the constants. Consequently there exist `r_0>0`, `C_0<infinity` and `K_0<infinity` such that, writing

\[
 S_L(X)=F_L(X)-LQ_L^{\rm st}X,
\]

one has, for `||X||_infinity<r_0`,

\[
 |S_L(X;c)|\le C_0\|X\|_\infty^2,
 \qquad
 \|\partial_b S_L(X;c)\|\le K_0\|X\|_\infty
       \quad (b\in D_L(c)).                         \tag{1.2}
\]

Here `partial_b` is a finite color-space derivative and `D_L(c)` is the finite set of input bonds read by output c; the derivative is zero outside that set. One obtains (1.2) by bounding the second derivative on a smaller closed polydisc, using `S_L(0)=DS_L(0)=0`. These are only fixed-L local constants, not a multilevel complex-source theorem. Set

\[
 m_L=\sup_c|D_L(c)|,\qquad
 N_L=\sup_b\#\{c:b\in D_L(c)\}.
\]

On small periodic tori use the lifted local pattern with multiplicities; its coefficient sums still satisfy the same estimates. Analyticity and the exact source-coordinate match remain at the deposited-transcription level; the original CMP98 full paper has not been independently reverified here.

## 2. Physical scaling and the one-step derivative bounds

At input spacing h and output spacing Lh, the physical potential map is

\[
 \mathcal F_h(A)=(Lh)^{-1}F_L(hA)
       =Q_hA+R_h(A),\qquad
 R_h(A)=(Lh)^{-1}S_L(hA).                       \tag{2.1}
\]

The factor h makes all following sums convergent across refinement levels. Put

\[
 C=C_0/L,\quad D_\infty=m_LK_0/L,\quad
 D_2=K_0\sqrt{m_LN_L}\,L^{d/2-1}.
\]

For `h||A||_infinity<r_0`,

\[
 \|R_h(A)\|_\infty\le Ch\|A\|_\infty^2,
 \quad
 \|DR_h(A)\|_{\infty\to\infty}
       \le D_\infty h\|A\|_\infty,
 \quad
 \|DR_h(A)\|_{2,h\to2,Lh}
       \le D_2 h\|A\|_\infty.                 \tag{2.2}
\]

For the last estimate, each derivative matrix entry is at most
`K_0 h||A||_infinity/L`; its unweighted row sum is at most
`m_L K_0 h||A||_infinity/L`. Its column sum with physical adjoint normalization is at most `L^d N_L K_0 h||A||_infinity/L`. The weighted Schur bound is the square root of their product, which is exactly `D_2 h||A||_infinity`. No comparison of unnormalized fine dimensions is used.

The flat averages and their physical adjoints have nonnegative row sums one. Thus Q_h is a contraction in both physical L2 and bounded-field norm. This follows from the explicit formula

\[
 (Q_hA)_\mu(y)=L^{-d-1}\sum_{x\in B(y)}
                    \sum_{r=0}^{L-1}A_\mu(x+rh e_\mu):
\]

each fine bond is counted L times in its column, whose sum is `L^-d`, and the physical adjoint supplies the factor `L^d`. Counting multiplicities makes this valid on short compatible tori too.

## 3. A refinement-uniform nonlinear ball

Write `h_t=L^{t-j}`, `0<=t<=j`, and `S=1/(L-1)`. Let

\[
 A_0=A,\qquad A_{t+1}=\mathcal F_{h_t}(A_t),\qquad
 \mathcal F^{(j)}(A)=A_j.
\]

Choose a fixed radius rho satisfying

\[
 0<\rho<\min\{r_0/4,\,1/(4CS)\},                 \tag{3.1}
\]

where the second restriction is omitted if C=0. Then every iterate is defined and holomorphic for `||A||_infinity<rho`, and with `a=||A||_infinity`,

\[
 \|A_t\|_\infty
 \le\frac{a}{1-Ca\sum_{s<t}h_s}\le 2a.           \tag{3.2}
\]

To prove this without a circular bootstrap, set `u_t=a/(1-Ca sum_{s<t}h_s)`. The denominator is positive. If `||A_t||<=u_t`, the local domain holds because `h_t u_t<=2rho<r_0`. Also

\[
 u_t+Ch_tu_t^2\le\frac{u_t}{1-Ch_tu_t}=u_{t+1}.
\]

Induction proves the bound and simultaneously proves that each local map is evaluated inside its analytic domain. Strict margins in (3.1) give an open complex ball; the same constants work in every periodic volume and on the bounded-field Banach space of the infinite lattice.

Set `Q=Q_{j-1}...Q_0=Q_M^{st}` and
`R^{(j)}=mathcal F^{(j)}-Q`. The exact telescoping identity is

\[
 R^{(j)}(A)=\sum_{t=0}^{j-1}Q_{t+1:j}R_{h_t}(A_t).
\]

Consequently

\[
 \boxed{\quad
 \|\mathcal F^{(j)}(A)\|_\infty\le2a,\qquad
 \|R^{(j)}(A)\|_\infty\le C_Ra^2,
 \quad C_R=4CS.\quad}                           \tag{3.3}
\]

For `j=0` the map is the identity and the remainder vanishes. The uniform radius is a conclusion about the nonlinear composition itself, not merely its finite Taylor jet.

## 4. Differential control and all orders

For `p=2,infinity`, write D_p for the constants in (2.2), and use the physical L2 spaces at each intermediate spacing when p=2. The chain rule and (3.2) give

\[
 \|D\mathcal F^{(j)}(A)\|_{p\to p}
       \le\prod_t(1+2D_pa h_t)
       \le e^{2D_pSa},                          \tag{4.1}
\]

\[
 \boxed{\quad
 \|D\mathcal F^{(j)}(A)-Q\|_{p\to p}
       \le e^{2D_pSa}-1=: \delta_p(a).\quad}      \tag{4.2}
\]

Indeed, expand the difference between the product of `Q_t+DR_{h_t}(A_t)` and the product of Q_t, preserving their noncommutative order. Every nonempty selection of remainder factors is bounded by the corresponding term of `prod_t(1+2D_pa h_t)-1`. This proves (4.2); no unproved nonflat contraction is used.

Holomorphy of the local maps and the uniform bounds also make
`A -> D mathcal F^{(j)}(A)` analytic as a map from the bounded-field ball into `B(L2_eta,L2_1)`. One can first prove this on each finite torus; alternatively, for fixed j every output uses a finite translated local map and its derivative matrix has uniformly finite row/column incidence. The local Taylor expansions then converge in that operator norm. There is no dependence on the number of cells.

For `||A||<rho` and any `0<r<rho-||A||`, Banach-space Cauchy estimates imply, for `n>=1`,

\[
 \|D^n\mathcal F^{(j)}(A)[K_1,\ldots,K_n]\|_\infty
 \le 2\rho\,n!(e/r)^n\prod_i\|K_i\|_\infty.     \tag{4.3}
\]

For `n>=0`, with the n=0 case understood directly from (4.1),

\[
 \|D^{n+1}\mathcal F^{(j)}(A)[K_1,\ldots,K_n,B]\|_{2,1}
 \le n!(e/r)^n e^{2D_2S\rho}
         \|B\|_{2,\eta}\prod_i\|K_i\|_\infty.   \tag{4.4}
\]

For n>=1 these bounds follow by applying multivariable Cauchy on radii `r/n` after normalizing the directions, and using `n^n<=e^n n!`. Equation (4.4) permits one physical L2 input and bounded remaining inputs; it does not assert a multilinear L2 bound with every input in L2.

## 5. Uniform finite range and weighted operator bounds

If one physical step reads input bonds within distance at most `r_L h` of its output, all j-step dependencies have physical distance at most `r_L sum_t h_t<=r_L S`. Add fixed cell-diameter margins and let R_* be an integer unit-cell range that contains both the nonlinear derivative and Q. This is independent of j; the deposited sharper two-block property is more than is needed.

For the physical-cell Hilbert block Schur norm

\[
 \|T\|_\kappa=\max\left\{
  \sup_x\sum_y e^{\kappa|x-y|_1}\|T_{xy}\|,
  \sup_y\sum_x e^{\kappa|x-y|_1}\|T_{xy}\|\right\},
\]

put `chi_kappa=v(R_*)exp(kappa R_*)`, where v counts unit cells in that radius. Each cell block is bounded by the global L2 operator norm. Hence

\[
 \|DR^{(j)}(A)\|_\kappa
       \le\chi_\kappa\delta_2(a).                \tag{5.1}
\]

The same finite-range argument applies to the bounded-cell-fiber version using `delta_infinity(a)`. Local background derivatives inherit this finite spatial dependence, but no special ordered insertion-path formula is claimed. Periodic restrictions are controlled either directly by local multiplicities or by the same periodic cell distances; constants can be enlarged by a fixed range count, not by M.

The map `A -> DR^{(j)}(A)` is analytic into this weighted Schur algebra, not just into the unweighted Hilbert operator space. Indeed every coefficient derivative has the same finite cell range, and the bounded conversion from its global operator norm to the weighted Schur norm has the fixed factor chi_kappa. Thus the operator-valued local Taylor expansions and Cauchy estimates from Section 4 also converge in the weighted norm. This is the analyticity needed in the next section.

## 6. A uniform analytic straightening of the nonlinear constraint

Use the already proved source-compatible flat minimizing extension H, with

\[
 QH=I,\qquad \|H\|_{\infty\to\infty}\le k,
 \qquad \|H\|_\kappa\le k_\kappa.                \tag{6.1}
\]

Here k and k_kappa are uniform in M and volume; H is exactly the extension studied in Notebook08. Fix `0<r_A<rho` so small that

\[
 k C_Rr_A\le\tfrac14,\qquad
 k\delta_\infty(r_A)\le\tfrac12,\qquad
 k_\kappa\chi_\kappa\delta_2(r_A)\le\tfrac12.    \tag{6.2}
\]

For `xi in ker Q`, coarse B, and

\[
 u=\xi+HB,\qquad \|u\|_\infty<r_A/2,
\]

the equation

\[
 A=u-HR^{(j)}(A)                               \tag{6.3}
\]

is a strict contraction of the closed bounded-field ball of radius r_A into itself: the nonlinear term has norm at most `k C_R r_A^2<=r_A/4`, and its derivative has norm at most one half. It therefore has a unique solution there, denoted `A=mathcal A_j(xi,B)`. The fixed point depends holomorphically on `(xi,B)`; for example iterate the contraction uniformly on smaller parameter balls, or use the bounded analytic inverse of `I+H DR^{(j)}(A)`.

For precision the parameter Banach norm may be chosen as `||(xi,B)||_par=||xi+HB||_infinity`. It is a norm on `ker Q` direct sum the coarse field space: Q applied to u gives B. Moreover `||B||<=||u||` and `||xi||<=(1+k)||u||`, while `||u||<=||xi||+k||B||`, so its equivalence to the usual direct-sum norm is uniform in M and volume. All smaller parameter balls and their Cauchy radii can be understood in this norm.

Applying Q to (6.3) proves the exact nonlinear constraint and the exact retained fluctuation coordinate:

\[
 \mathcal F^{(j)}(\mathcal A_j(\xi,B))=B,
 \qquad (I-HQ)\mathcal A_j(\xi,B)=\xi.           \tag{6.4}
\]

Also `||A||<=2||u||` (because `||HR(A)||<=one-half ||A||` on this ball), and thus

\[
 \|\mathcal A_j(\xi,B)-\xi-HB\|_\infty
       \le4k C_R\|\xi+HB\|_\infty^2.           \tag{6.5}
\]

Conversely any A with `||A||<r_A/3` has
`xi=(I-HQ)A`, `B=mathcal F^{(j)}(A)` and
`u=A+HR^{(j)}(A)` of norm less than r_A/2; hence it belongs to this chart and is its unique fixed point. The chart is therefore a genuine local coordinate equivalence, not just a choice of one solution for each coarse field.

At a chart point define the ordinary-coordinate differential

\[
 Q_A=D\mathcal F^{(j)}(A)=Q+DR^{(j)}(A).
\]

Its analytic right inverse is

\[
 H_A=(I+H DR^{(j)}(A))^{-1}H
       =H(I+DR^{(j)}(A)H)^{-1},\qquad Q_AH_A=I.
 \tag{6.6}
\]

Both identities follow by the geometric series, with the same multiplication order as displayed. In the weighted physical-cell algebra,

\[
 \|H_A\|_\kappa\le2k_\kappa,\qquad
 \|(I+H DR^{(j)}(A))^{-1}\|_\kappa\le2.         \tag{6.7}
\]

The same estimates hold in the global bounded-field norm with k replacing k_kappa. These are the derivatives of the chart in B and xi, respectively. Thus the chart has uniform analytic derivatives and exponential spatial locality in the physical-cell Hilbert sense. Its dependence on the background A is analytic in bounded-field norm; Cauchy gives uniform factorial higher derivatives on smaller balls.

If xi also lies in the fixed flat gauge subspace `R D* xi=0`, the correction in (6.3) lies in ran H and the exact identity `R D*H=0` gives `R D*A=0`. This is the fixed flat gauge, not a moving-background gauge condition. On finite regulators this statement follows directly by continuity of the linear operators. On the infinite lattice it holds wherever the fixed linear gauge operator is defined, or by the bounded-cell extension of that operator; no new uniform bounded-field estimate for the order-zero gauge projection is being asserted.

## 7. What this settles and what remains separate

The actual fixed-L corrected nonlinear average has a complex bounded-field ball whose radius is independent of the refinement. Its full remainder is quadratic with a uniform constant, its physical L2 differential is uniformly bounded and differs from the flat straight average by O(||A||_infinity), and all bounded-direction derivatives obey uniform factorial estimates. Combining this with the already proved H gives an exact local analytic straightening of its constraint, with exponential physical-cell Hilbert locality.

These conclusions use the fixed flat-reference potential coordinate (1.1). They do not identify `D mathcal F^{(j)}(A)` with a nonflat source averaging operator defined through left multiplication of a group field, background-dependent endpoint corrections, or a moving gauge. Such an identification requires writing the coordinate Jacobians and checking the specific reference-background convention. Nor does the chart prove that its selected field minimizes the nonflat Yang--Mills action; it only straightens the averaging constraint along the flat minimizing-extension range. Nonflat elliptic stability, retained or mixed-scale geometry, and an interacting continuum limit remain separate tasks.
