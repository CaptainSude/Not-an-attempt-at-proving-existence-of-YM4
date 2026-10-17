# A Wilson Hessian decomposition and a conditional nonflat energy inverse

16 October 2026. Research proof, pending independent audit. The first result is an explicit local calculation for the normalized Wilson action near the trivial connection. The second is an abstract perturbation theorem for the full gauge-fixed inverse, including stability of the scalar compression used to define the gauge projection. It assumes smallness of both averaging operators and does not identify an arbitrary source Hessian or retained-history operator with the Wilson Hessian calculated here.

The inverse conclusion concerns the augmented energy block `(I,nabla) G_U (I,nabla)^T`. In particular, it includes one fine derivative on each side. It does **not** assert uniform one-sided second derivatives, pointwise nonflat Schauder estimates, or a neighborhood about an arbitrary nontrivial reference connection.

## 1. Conventions and normalization

Let the fine spacing be `eta=1/M`, with `0<eta<=1`. The coarse scale is one. Work on the full lattice or a compatible periodic lattice, retaining periodic incidences with their multiplicities. Fine sites, positive bonds and positive plaquettes have physical measure `eta^d`; coarse fields have counting measure. Lie algebra variables are Hermitian traceless matrices, with normalized trace

\[
 \tau(X)=N_c^{-1}\operatorname{Tr}X,
 \qquad \langle B,C\rangle_\eta
   =\eta^d\sum_e\tau(B_eC_e).
                                                        \tag{1.1}
\]

On real fields this is the real positive Hilbert pairing. Its complexification is bilinear. A superscript `T` below means its bilinear transpose, not conjugation of a complex background. At real unitary backgrounds the transposes agree with the appropriate real Hilbert adjoints. Matrix norm constants may depend on the fixed group and dimension.

For every positive plaquette `p=(x;mu,nu)`, `mu<nu`, let `P_p` be its based positively oriented holonomy. Define the coupling-free analytic Wilson action

\[
 \mathcal S_\eta(U)=\eta^{d-4}\sum_p
   \left\{1-\frac12\tau(P_p+P_p^{-1})\right\}.
                                                        \tag{1.2}
\]

On the unitary real slice this is `eta^(d-4) sum_p(1-Re tau P_p)`. No coupling factor `g^-2` or other source-dependent prefactor is hidden in (1.2). If a different action convention is used, its prefactor multiplies every Hessian below and must be matched explicitly.

The Hessian is defined by the simultaneous left exponential chart

\[
 U_e(s,t)=e^{i\eta(sB_e+tC_e)}U_e,
 \qquad
 \langle B,\Delta_U C\rangle_\eta
   =\partial_s\partial_t\mathcal S_\eta(U(s,t))\big|_{s=t=0}.
                                                        \tag{1.3}
\]

The ordinary scalar gradient is `D lambda(e)=eta^-1(lambda(e+)-lambda(e-))`. The ordinary curl is

\[
 (dB)_{\mu\nu}(x)
  =\eta^{-1}\{B_\mu(x)+B_\nu(x+\eta e_\mu)
                   -B_\mu(x+\eta e_\nu)-B_\nu(x)\}.
                                                        \tag{1.4}
\]

Thus the Hessian at the trivial connection is exactly `Delta_I=d^T d`, with coefficient one in these conventions.

Assume positive links have the fixed chart

\[
 U_e=e^{i\eta a_e},\qquad
 \epsilon_0=\sup_e\|a_e\|,
 \quad \epsilon_1=\sup_{e,\rho}\|\nabla_\rho a_e\|,
 \quad F=\epsilon_1+\epsilon_0^2.
                                                        \tag{1.5}
\]

Here `nabla_rho a_e` is the ordinary forward physical difference between translated positive bonds of the same orientation. Assume `epsilon_0<=c_0`, for a fixed constant; the estimates are analytic for complex `a` in this chart as well. Smallness of `epsilon_1` is used only when invoking the later perturbation theorem.

## 2. Plaquette curvature and the exact transported curl

**Lemma 2.1.** Uniformly in spacing and volume,

\[
 \|P_p-I\|+\|P_p^{-1}-I\|
       \le C\eta^2F.                              \tag{2.1}
\]

**Proof.** In

\[
 P_p=e^{i\eta a_\mu(x)}e^{i\eta a_\nu(x+\eta e_\mu)}
      e^{-i\eta a_\mu(x+\eta e_\nu)}e^{-i\eta a_\nu(x)},
\]

replace the two shifted coefficients by their values at `x`. The matrix exponential identity

\[
 e^X-e^Y=\int_0^1 e^{(1-s)X}(X-Y)e^{sY}\,ds
\]

shows that these replacements cost at most `C eta^2 epsilon_1`. The remaining expression is the group commutator of `e^{i eta a_mu(x)}` and `e^{i eta a_nu(x)}`. Applying the fundamental theorem of calculus to both exponential parameters, or the identity `[e^X,e^Y]=int_0^1 int_0^1 e^{sX}e^{tY}[X,Y]e^{(1-t)Y}e^{(1-s)X} dt ds` with the corresponding ordered factors, bounds its distance from identity by `C eta^2 epsilon_0^2`. Only that commutator bound, not a particular integral ordering, is needed. All transport and inverse transport norms are bounded by `exp(C eta epsilon_0)`. The inverse estimate follows from `P^-1-I=-P^-1(P-I)`. This proves (2.1).

For the plaquette loop `e_1,...,e_4`, put `V_i=U_{e_1}...U_{e_{i-1}}`. If `e` is a negative traversal of a positive bond `f`, define

\[
 B_e=-\operatorname{Ad}_{U_f^{-1}}B_f,
 \qquad C_e=-\operatorname{Ad}_{U_f^{-1}}C_f.       \tag{2.2}
\]

These are exact chart increments because

\[
 (e^{i\eta(sB_f+tC_f)}U_f)^{-1}
  =e^{i\eta(sB_e+tC_e)}U_f^{-1}.
\]

Define `X_i^B=Ad_{V_i}B_{e_i}`, and likewise `X_i^C`. Moving all insertions to the based plaquette gives the exact identity

\[
 P_p(s,t)=\prod_{i=1}^4
      e^{i\eta(sX_i^B+tX_i^C)}\,P_p.
                                                        \tag{2.3}
\]

Its transported linearized curl is

\[
 \mathcal C_U B=\eta^{-1}\sum_{i=1}^4X_i^B.
                                                        \tag{2.4}
\]

Every transport in (2.4) is a product of a bounded number of links and inverse links. Consequently

\[
 \mathcal C_U=d+E_U,
 \quad \|E_U\|_{\infty\to\infty}
        +\|E_U^T\|_{\infty\to\infty}\le C\epsilon_0.
                                                        \tag{2.5}
\]

Indeed each difference of a transport from identity is `O(eta epsilon_0)`, which cancels the `eta^-1` in (2.4); there are four terms per plaquette and a fixed number of incident plaquettes per bond. These are physical row and column estimates; their constants contain no factor from the number of sites in a coarse cell. They also imply weighted physical-cell `L2` Schur bounds with the same size, up to a fixed weight constant, because the maps have fixed fine range and bounded incidences.

The scalar gauge derivative in the compatible left chart is

\[
 D_U\lambda(e)=\eta^{-1}
  \{\operatorname{Ad}_{U_e}\lambda(e_+)-\lambda(e_-)\}
       =D\lambda+E_s\lambda,
 \qquad \|E_s\|+\|E_s^T\|\le C\epsilon_0,        \tag{2.6}
\]

in the same row, column and weighted physical-cell norms. A simultaneous reversal of the gauge-action sign reverses `D_U` and leaves the quadratic gauge-fixing term unchanged.

## 3. The Wilson Hessian: exact formula and small-form decomposition

Let `S_B=sum_i X_i^B`, and similarly `S_C`. Twice differentiating (2.3) gives

\[
 \partial_s\partial_t P_p(s,t)\big|_0
 =-\eta^2\left\{
   \frac12(S_BS_C+S_CS_B)
   +\frac12\sum_{i<j}
       ([X_i^B,X_j^C]+[X_i^C,X_j^B])\right\}P_p.
                                                        \tag{3.1}
\]

This follows by separating the same-factor terms
`(X_i^B X_i^C+X_i^C X_i^B)/2` from the ordered terms
`X_i^B X_j^C+X_i^C X_j^B`, `i<j`; their difference from half the anticommutator of the two sums is precisely the commutator sum in (3.1).

For the oriented density `-tau(P_p)`, the first term of its Hessian is

\[
 \eta^d\,\frac12\tau\!\left(
   [ (\mathcal C_U B)(\mathcal C_U C)
     +(\mathcal C_U C)(\mathcal C_U B)]P_p\right).
                                                        \tag{3.2}
\]

Since the trace of a commutator is zero, the remaining term is exactly

\[
 \eta^d\frac1{2\eta^2}\sum_{i<j}
 \tau\!\left(
    ([X_i^B,X_j^C]+[X_i^C,X_j^B])(P_p-I)\right).
                                                        \tag{3.3}
\]

The reversed loop has holonomy `P_p^-1` and curl
`-Ad_{P_p^-1} mathcal C_U`. In its principal quadratic term these two adjoint transports can be removed by cyclicity of trace. Therefore averaging the forward and reverse oriented densities in (1.2) yields the exact decomposition

\[
 \boxed{\ \Delta_U=\mathcal C_U^T M_U\mathcal C_U+V_U\ },
                                                        \tag{3.4}
\]

where the diagonal plaquette operator is defined by

\[
 \tau(X M_{U,p}Y)=\frac14\tau((XY+YX)(P_p+P_p^{-1})),
                                                        \tag{3.5}
\]

and `V_U` is the bilinear bond operator specified by one half of (3.3) plus one half of its reverse-loop version. Projection onto the fixed traceless Lie space is implicit in (3.5). It causes only a fixed norm constant. Both `M_U` and `V_U` are symmetric for the bilinear transpose; all formulas are holomorphic in the chosen complex background chart.

Lemma 2.1 and bounded plaquette incidence imply

\[
 \|M_U-I\|\le C\eta^2F,
 \quad \|V_U\|_{\infty\to\infty}
        +\|V_U^T\|_{\infty\to\infty}\le CF.
                                                        \tag{3.6}
\]

In particular, the operator

\[
 W_U=\Delta_U-\mathcal C_U^T\mathcal C_U
    =\mathcal C_U^T(M_U-I)\mathcal C_U+V_U
                                                        \tag{3.7}
\]

has ordinary bounded row and transpose-row norms at most `CF`: each curl contributes `O(eta^-1)`, exactly paid for by the factor `eta^2` in `M_U-I`. The same is true in a fixed weighted physical-cell Schur norm. This is the step that would fail if one only bounded a plaquette by `O(eta epsilon_0)`.

Combining (2.5) and (3.7) gives the exact small-form identity

\[
 \Delta_U-d^Td=d^TE_U+E_U^Td+E_U^TE_U+W_U.
                                                        \tag{3.8}
\]

Let `S_v=(I,nabla)` be the augmented ordinary fine-gradient operator on one-forms, with all component directions included. Since `d` is a fixed component combination of these gradients, (3.8) has the form

\[
 \boxed{\ \Delta_U-d^Td=S_v^T\mathcal V_{\rm kin}(U)S_v,
 \quad \|\mathcal V_{\rm kin}(U)\|_\kappa
       \le C_\kappa(\epsilon_0+\epsilon_1+\epsilon_0^2).\ }
                                                        \tag{3.9}
\]

All coefficient maps in this representation have fixed fine range. One can instead include `d` directly in `S_v`; the resulting energy norm is bounded by the full-gradient norm used here. Equation (3.9) is a concrete proved Wilson coefficient estimate, with no running-coupling or multiscale-minimizer identification assumed.

## 4. Weighted operator algebra and flat scalar inputs

For operators between physical fine-cell `L2` spaces or coarse-cell finite-dimensional spaces, use

\[
 \|T\|_\kappa=\max\left\{
  \sup_x\sum_y e^{\kappa d(x,y)}\|T_{xy}\|,
  \sup_y\sum_x e^{\kappa d(x,y)}\|T_{xy}\|\right\}.
                                                        \tag{4.1}
\]

The cell distance is the ordinary lattice distance, or its periodic counterpart. The same convention applies to rectangular augmented spaces. Products are bounded by the product of norms, by the triangle inequality for the distance; transpose preserves the norm. All fine-cell norms use physical volume, so this algebra does not insert powers of `M`.

The already established flat inverse theorem in `flat_full_inverse_research.md` supplies, for a fixed sufficiently small `kappa>0`,

\[
 \|S_vG_0S_v^T\|_\kappa\le K_v,
 \quad G_0=(d^Td+DR_0D^T+Q^TaQ)^{-1}.            \tag{4.2}
\]

Here `Q=Q_M^st` is the normalized flat straight-string average. The operators `Q` and `Q_0`, and their transposes, have uniform weighted cell bounds by their flat physical row/column contraction and fixed final-scale range; these bounds are included in the constants below. The penalties `a` and `a'` are positive real scalars in specified compact subintervals of `(0,infinity)`. In the matched unit-scale source convention the one-form penalty is `a=1`.

We also need the scalar flat operator

\[
 G'_0=(L+Q_0^Ta'Q_0)^{-1},\quad L=D^TD,
 \quad S_s=(I,D),
 \quad C_0=Q_0(G'_0)^2Q_0^T.                    \tag{4.3}
\]

The following scalar facts follow by the same canceled alias calculation, stated explicitly here because stability of `C_0^-1` is required.

Let `P_r` denote the fine Laplacian multipliers in the coarse Bloch fiber, `a_r` the centered scalar block-average multipliers, and `A=a_0a_0^-`. Write

\[
 R_{s,1}=\sum_{r\ne0}\frac{a_ra_r^-}{P_r},\qquad
 R_{s,2}=\sum_{r\ne0}\frac{a_ra_r^-}{P_r^2},
 \quad D_{s,2}=A+P_0^2R_{s,2},
\]
\[
 N=P_0+a'A+a'P_0R_{s,1}.
                                                        \tag{4.4}
\]

The scalar Woodbury formula, initially on real nonzero coarse fibers, is

\[
 (G'_0)_{rs}=\frac{\delta_{rs}}{P_r}
 -\frac{P_0a_r^-a_s}{P_rP_sD_{s,1}},
 \quad D_{s,1}=A+P_0(R_{s,1}+(a')^{-1})=N/a'.    \tag{4.5}
\]

Its central entry is `(R_s,1+(a')^-1)/D_s,1`; a central-to-high entry is `-a_0^-a_s/(P_sD_s,1)`, with the transpose formula for high-to-central entries. Thus every central pole is removed. High denominators are uniformly gapped and the alias `ell2` norms of `(a_r)` and `(a_r^-)` are uniformly bounded. Applying at most one fine difference on each side keeps the high diagonal bounded and keeps every rank row and column uniformly square summable. The canceled formulas consequently imply

\[
 \|S_sG'_0S_s^T\|_\kappa\le K_s.               \tag{4.6}
\]

More explicitly, `G'_0Q_0^T=L^-1Q_0^T/(1+a'W_1)`, where `W_1=A/P_0+R_s,1`; hence

\[
 C_0=\frac{W_2}{(1+a'W_1)^2}
     =\frac{D_{s,2}}{N^2},
 \qquad
 \boxed{\ C_0^{-1}=\frac{N^2}{D_{s,2}}\ },
 \quad W_2=A/P_0^2+R_{s,2}.                    \tag{4.7}
\]

On a slightly enlarged real Bloch cube, `A>=c>0`, `P_0>=0`, `R_s,j>=0`. Therefore `D_s,1`, `N` and `D_s,2` have uniform positive lower bounds and uniform upper bounds. The high-denominator gap and alias Parseval estimate give uniform holomorphic bounds in a preliminary open tube; a fixed Cauchy shrinking preserves these nonvanishing lower bounds. Equations (4.5)–(4.7), reconstructed in physical cell coordinates, glue periodically because they represent the actual flat operators on real fibers. Fourier contour shifting then gives

\[
 \|C_0\|_\kappa+\|C_0^{-1}\|_\kappa\le K_c.    \tag{4.8}
\]

This argument is the scalar specialization of the flat cancellation and physical-cell reconstruction proofs already given in `flat_covariance_decay_research.md` and `flat_full_inverse_research.md`; it uses their common enlarged open tube, not a closed real-box analyticity assertion. At zero coarse momentum `a_r=0` for every high alias, and (4.7) gives `C_0=(a')^-2`, correctly treating the scalar constant mode. At `M=1`, it gives `C_0=(P_0+a')^-2`. No inverse of the unpenalized Laplacian is assigned to its zero mode.

## 5. A form-resolvent lemma

**Lemma 5.1.** Suppose `G=A^-1` and `K=SGS^T` belong to the appropriate weighted algebra and `||K||_kappa<=K_*`. Let

\[
 A_V=A+S^TVS,\qquad K_*\|V\|_\kappa<1.
\]

Then

\[
 G_V=G-GS^TV(I+KV)^{-1}SG,                       \tag{5.1}
\]
\[
 SG_VS^T=K-KV(I+KV)^{-1}K,
\]
\[
 \|SG_VS^T\|_\kappa
   \le\frac{K_*}{1-K_*\|V\|_\kappa},
 \quad
 \|S(G_V-G)S^T\|_\kappa
   \le\frac{K_*^2\|V\|_\kappa}{1-K_*\|V\|_\kappa}.
                                                        \tag{5.2}
\]

Here `I` is included among the components of `S`, so `G`, `GS^T` and `SG` are subblocks of `K`. The Neumann series in the weighted algebra proves (5.1)–(5.2), and multiplication by `A_V` verifies the inverse identity at each fixed finite spacing. On the infinite lattice the same conclusion follows by bounded-operator multiplication at each fixed spacing. All displayed bounds are uniform in that spacing. Holomorphic coefficient dependence gives holomorphic inverses on this disk. For a real positive definite baseline `A`, the bound on `SGS^T` also bounds `||S A^-1/2||^2`; thus the same smallness gives the usual relative-form coercivity for real symmetric perturbations. No second derivative of coefficients is used.

## 6. Conditional nonflat theorem, including the scalar compression

Let the flat data satisfy (4.2), (4.6), and (4.8). Consider coefficient families

\[
 D_U=D+E_s,
 \qquad Q_s(U)=Q_0+F_s,
 \qquad Q_v(U)=Q+F_v,
                                                        \tag{6.1}
\]

and a symmetric one-form Hessian satisfying

\[
 \Delta_U=d^Td+S_v^TV_{\rm kin}S_v.
                                                        \tag{6.2}
\]

Assume, in one fixed weighted algebra (4.1),

\[
 \|E_s\|_\kappa+\|F_s\|_\kappa+\|F_v\|_\kappa
       +\|V_{\rm kin}\|_\kappa\le\varepsilon.
                                                        \tag{6.3}
\]

Since (4.1) includes both row and column sums, it also controls all displayed transposes. For analytic conclusions the families in (6.1)–(6.2) must be holomorphic in a common domain and (6.3) must hold throughout it. There is no assertion that a weak background norm automatically implies (6.3).

Define successively

\[
 B_s(U)=D_U^TD_U+Q_s(U)^Ta'Q_s(U),
 \qquad G'_U=B_s(U)^{-1},
\]
\[
 C_U=Q_s(U)(G'_U)^2Q_s(U)^T,
 \qquad
 R_U=I-G'_UQ_s(U)^TC_U^{-1}Q_s(U)G'_U,
                                                        \tag{6.4}
\]
\[
 A_U=\Delta_U+D_UR_UD_U^T+Q_v(U)^TaQ_v(U).
                                                        \tag{6.5}
\]

**Theorem 6.1.** There is `varepsilon_*>0`, depending only on the flat bounds, fixed penalties, dimension, group, and the chosen cell-weight exponent, such that if `varepsilon<=varepsilon_*`, then every inverse in (6.4)–(6.5) exists. Uniformly in odd refinement and compatible periodic volume,

\[
 \|S_sG'_US_s^T\|_\kappa+\|C_U^{-1}\|_\kappa
       +\|R_U\|_\kappa+\|S_vA_U^{-1}S_v^T\|_\kappa\le C,
                                                        \tag{6.6}
\]

and the differences of these four quantities from their flat counterparts have norm at most `C varepsilon`. The same conclusions hold on the infinite lattice. In a holomorphic coefficient domain the four operator families are holomorphic. On real symmetric data they are the ordinary real inverses and `R_U` is the orthogonal projection onto the complement of `ran(G'_U Q_s(U)^T)`.

**Proof.** The scalar precision difference is

\[
 B_s(U)-B_s(0)=D^TE_s+E_s^TD+E_s^TE_s
  +Q_0^Ta'F_s+F_s^Ta'Q_0+F_s^Ta'F_s.
                                                        \tag{6.7}
\]

All terms other than the first two are bounded coefficient maps and can be put in the `I,I` block. Hence (6.7) is `S_s^TV_sS_s` with `||V_s||_kappa<=C_s varepsilon` for `varepsilon<=1`. Lemma 5.1 and (4.6) give (6.6) and `O(varepsilon)` differences for the scalar energy block when `K_s C_s varepsilon<=1/2`. In particular `G'_U-G'_0` is bounded by `C varepsilon` in the weighted algebra.

Expanding the products defining `C_U` now gives

\[
 \|C_U-C_0\|_\kappa\le C'_s\varepsilon.          \tag{6.8}
\]

The flat inverse (4.8) is crucial: if `K_c C'_s varepsilon<=1/2`, then

\[
 C_U^{-1}=(I+C_0^{-1}(C_U-C_0))^{-1}C_0^{-1},
                                                        \tag{6.9}
\]

and its norm and difference are uniformly bounded. Substitution in (6.4) gives uniform bounds on `R_U` and `R_U-R_0`, the latter of size `C_R varepsilon`. Algebraically `R_U^2=R_U`; on real symmetric data the middle inverse is the Gram inverse of `G'_U Q_s(U)^T`, proving the orthogonal-projection statement. For complex data (6.4) is its bilinear holomorphic continuation, not a positivity assertion.

Next expand the gauge term without ever treating a bare fine derivative as a uniform bounded coefficient:

\[
 D_UR_UD_U^T-DR_0D^T
  =D(R_U-R_0)D^T+E_sR_UD^T
        +DR_UE_s^T+E_sR_UE_s^T.                 \tag{6.10}
\]

The divergence `D^T` on one-forms is a fixed shifted component combination of `nabla`; the backward shift has uniformly bounded weighted norm. Thus (6.10) has the form `S_v^TV_gS_v`, with `||V_g||_kappa<=C_g varepsilon`. The average-penalty difference

\[
 Q_v(U)^TaQ_v(U)-Q^TaQ
   =Q^TaF_v+F_v^TaQ+F_v^TaF_v                 \tag{6.11}
\]

is a bounded `I,I` coefficient of size `C_a varepsilon`. Combining (6.2), (6.10), and (6.11),

\[
 A_U=A_0+S_v^TV_{\rm tot}S_v,
 \quad \|V_{\rm tot}\|_\kappa\le C_v\varepsilon.
                                                        \tag{6.12}
\]

Lemma 5.1 with (4.2) proves the last assertion of (6.6), its difference estimate, and its holomorphic version if `K_v C_v varepsilon<=1/2`. One admissible threshold is the minimum of one and the three reciprocal bounds just specified. All products take place in the physical-cell algebra, so no estimate loses a power of the fine-cell dimension. This completes the proof.

The theorem gives exponential cell locality of `G_U`, `nabla G_U`, `G_U nabla^T`, and `nabla G_U nabla^T`. It does not propagate the flat theorem's one-sided second-difference estimate by the same argument: differentiating the outer factor `G_0S_v^T` twice would require an unavailable total third-order block. Such a stronger conclusion needs a separate regularity argument.

### 6.1. The gauge projection does not depend on the scalar penalty

There is a useful exact algebraic improvement. Fix a symmetric scalar kinetic operator `L_U=D_U^T D_U` and an averaging map `Q_s`. For any symmetric coarse penalty `b` for which the following inverses exist, put

\[
 G_b=(L_U+Q_s^TbQ_s)^{-1},\quad E_b=G_bQ_s^T,
 \quad P_b=E_b(E_b^TE_b)^{-1}E_b^T.              \tag{6.13}
\]

Then `P_b`, and hence `R_b=I-P_b`, is independent of `b`. Indeed

\[
 \operatorname{ran}E_b
   =\{v:L_Uv\in\operatorname{ran}Q_s^T\}.        \tag{6.14}
\]

The forward inclusion follows from
`L_U G_b Q_s^T=Q_s^T(I-bQ_sG_bQ_s^T)`.
For the converse, if `L_Uv=Q_s^Tw`, then
`v=G_b Q_s^T(w+bQ_sv)`.
Thus the range is independent of the penalty. The Gram inverse in (6.13) makes it a closed nondegenerate range, and `P_b` is the unique bilinear projection onto it along its orthogonal complement. This proves equality directly, also for complex data whenever the inverses and Gram inverses exist. On real data it is the familiar orthogonal projection.

It follows that the full gauge inverse in (6.5) can be constructed using the auxiliary choice `a'=1`. Its projection then equals a source projection with a different positive scalar or positive coarse-matrix penalty wherever that source formula is defined. No uniform bound on an unprinted scalar penalty sequence is needed for this **projection identification**. A uniform estimate for the scalar inverse `G'_U` itself at that other penalty is a different claim and still requires its own normalization bounds. On a finite periodic regulator every positive coarse penalty gives an invertible scalar precision once the common kinetic/average kernel is trivial; existence on an infinite lattice should be stipulated separately when making the identification there.

## 7. What is supplied by the Wilson calculation, and what remains a source interface

For the Wilson action (1.2) in the neartrivial chart (1.5), equations (2.6) and (3.9) prove the scalar-gradient and kinetic hypotheses in (6.3), with size at most `C(epsilon_0+epsilon_1+epsilon_0^2)`. No derivative of a current is used, and no erroneous `eta^-1 epsilon_0` coefficient occurs.

A scalar averaging operator of the explicit transported form

\[
 (Q_s(U)\lambda)(y)
   =\sum_{x\in B(y)}w_{yx}\operatorname{Ad}_{U(\Gamma_{yx})}\lambda(x),
 \quad w_{yx}\ge0,\quad\sum_xw_{yx}=1,
                                                        \tag{7.1}
\]

has `Q_s(U)-Q_0=O(epsilon_0)` in the weighted norm if: (i) every path has uniformly bounded physical length; (ii) the physical adjoint column sums of the weights are uniformly bounded; and (iii) path endpoints and the indexing coarse cell remain within a uniformly bounded coarse distance. Indeed `Ad_U(Gamma)-I=O(epsilon_0 length(Gamma))`; weighted row and physical column estimates follow directly and then imply the physical-cell Schur estimate. These conditions explicitly rule out an unnoticed dimension factor. For nested fixed-ratio paths whose normalized lengths form a geometric sum, the path-length condition is uniform. This observation proves an operator estimate for (7.1), not identification of every scalar averaging convention in a retained history.

The one-form hypothesis `||Q_v(U)-Q||_kappa=O(epsilon)` requires the exact derivative of the corrected averaging operation, with its actual intermediate backgrounds and physical adjoint normalization. It is not inferred merely from closeness of individual links or from scalar-average covariance. This hypothesis is now supplied for the homogeneous small global connection by the separate audited argument in `nonflat_reference_averages_research.md`, summarized in the next subsection.

### 7.1. An unconditional theorem for the explicitly defined homogeneous Wilson operator

Fix odd blocking ratio `L>=3`, let `M=L^j`, and take the actual deposited ordinary reference trajectory `V_t=mathcal M^t(U)`. Define `Q_v(U)` to be the product of the deposited one-step corrected relative derivatives at these ordinary references, and define `Q_s(U)` to be the deposited scalar transported block average. These definitions are those in Sections 5–6 of `nonflat_reference_averages_research.md`; they are not the differential of the fixed-reference nonlinear composition.

That note proves on a common complex bounded-field ball:

\[
 \|Q_v(U)-Q_M^{\rm st}\|_\kappa
   +\|Q_s(U)-Q_0\|_\kappa\le C\epsilon_0,       \tag{7.2}
\]

uniformly in refinement and compatible volume. Its quantitative mechanism is the ordinary-reference bound
`||log V_t||<=C h_t epsilon_0`, the local one-step analytic estimate of size `O(h_t epsilon_0)` with physical adjoint normalization, and the geometric sum `sum_{t<j}h_t<=1/(L-1)`. The scalar transports obey the same sum. Fixed final-scale support converts physical row/column bounds to (7.2).

Combining that independently proved averaging result with Sections 2–6 gives the following concrete corollary. Define `Delta_U` by the Wilson action (1.2) and chart (1.3), define `D_U` by (2.6), use these deposited homogeneous averages, choose auxiliary scalar penalty one to construct `R_U`, and fix a positive one-form penalty in a compact interval. Then there is a mesh- and volume-independent `rho>0` such that

\[
 \|a\|_\infty+\|\nabla a\|_\infty<\rho
 \quad\Longrightarrow\quad
\|(I,\nabla)(\Delta_U+D_UR_UD_U^T+Q_v(U)^Ta_{\rm pen}Q_v(U))^{-1}
                      (I,\nabla)^T\|_\kappa\le C.       \tag{7.3}
\]

Here `a_pen` is the constant one-form penalty, distinct from the bond background field `a` in `U=e^{i eta a}`. The inverse is holomorphic in this small complex global `C1` ball and differs from the flat inverse in the augmented energy norm by at most `C(||a||_infinity+||nabla a||_infinity)`. The assertion is unconditional for the explicitly defined Wilson operator and these deposited averaging maps, subject to their stated homogeneous periodic/full-lattice geometry. Identification with the source's exact `Delta` still requires matching its action and physical summation convention; (7.3) does not silently make that identification.

The deposited source currently checked is
`work/Yang--Mills-LLM-experiment/theorem_0_complete_account_raw_I.tex`:

* Lines 13583–13593 define the homogeneous full operator `Delta_a=Delta+D_U R D_U^*+Q^*aQ`, with `a=ell^-2`, and its inverse. At `ell=1` the one-form penalty is one.
* Lines 13617–13620 separately assert locality of `Delta'=Delta-D_U^*D_U` and its small bound. The exact source definition of the one-form covariant curl occurring there has not been fully checked against (2.4). The graded symbol `D_U` is also used for the scalar gradient; these are different maps.
* Lines 15474–15482 identify `Delta` as the symmetric quadratic term in the expansion of the lattice action. Matching its action prefactor and chart convention to (1.2)–(1.3) remains required before promoting the present Wilson calculation to that exact source operator.
* The positive part of that convention check is now explicit: lines 453–467 normalize `tr(1)=1`, count unoriented plaquettes once, and define the bare Wilson action as `sum_p(1-Re tr P_p)`; lines 472–481 place the coupling outside it. Thus the bare action is exactly (1.2) in dimension four. Line 15645 displays the left chart `mathsf A(e^{i eta A}U_0)`, and line 77577 gives the color pairing `tr AB`. What remains is a direct check that the reused `mathsf A` in the Hessian passage denotes that same bare action with the same physical summation convention, rather than a separately rescaled or effective functional.
* Lines 23909 onward give a transported scalar average with normalized block weights and axial/nested-center paths. Formula (7.1) explains the relevant quantitative estimate once its actual path and adjoint conventions are fixed.
* Lines 24320–24325 use ordinarily averaged background connections in the corrected nonlinear iteration. Lines 47046–47048 compose the one-step derivative maps. Therefore a proof for a different fixed-background iteration cannot silently substitute for the required `Q_v(U)` estimate.

These are citations to the deposited transcription, not newly recovered original journal proofs. The result proved here is a conditional analytic inverse theorem with an explicit Wilson kinetic input. It does not yet establish the source's full nonflat weak-norm/current neighborhood, arbitrary reference backgrounds, mixed histories, or any interacting Yang–Mills construction.
