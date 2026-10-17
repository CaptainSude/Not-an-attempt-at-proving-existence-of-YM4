# Uniform nonlinear constrained stationarity on the fixed flat gauge slice

16 October 2026. Research result, with Sections 1, 2, 4 and 5 passed by a separate internal audit. The new averaging estimates and the stationarity algebra below are proved directly. The equal-exponent constrained Green input has now been proved in `flat_constrained_schauder_research.md` and passed `flat_constrained_schauder_audit.md`; the earlier positive-loss estimate is not substituted for it. The normalized Wilson force input is proved in `wilson_nonlinear_force_research.md` and passed `wilson_nonlinear_force_audit.md`. Thus every analytic input of the local theorem below is now supplied and internally audited. The target here is a **local constrained minimizer on a fixed flat gauge slice**, first on finite compatible periodic regulators. It is not yet an unrestricted source minimizer modulo nonlinear gauge transformations, and no external certification is claimed.

Fix L, M=L^j, eta=M^-1, final coarse scale one, and `0<alpha<1`. Fine Hilbert pairings use physical volume eta^d. All constants below are independent of j, eta and periodic volume. Write

\[
 K=d^Td,\quad Q=Q_M^{\rm st},\quad q=q_M,\quad
 \mathcal F(A)=QA+R(A).
\]

Here F is the full fixed-reference corrected nonlinear average from the independently audited nonlinear-average note. The superscript T denotes the physical bilinear transpose, holomorphic at complex fields.

## 1. Two additional uniform estimates for the full averaging map

### 1.1. The physical adjoint of the nonlinear differential

Retain the local constants K_0,m_L,N_L of `flat_nonlinear_average_research.md`. Each matrix entry of the one-step derivative remainder has norm at most `K_0 h||A||_infinity/L`. Its physical-adjoint row sum therefore obeys

\[
 \|DR_h(A)^T\|_{\infty\to\infty}
    \le D_*h\|A\|_\infty,
 \qquad D_*=N_LK_0L^{d-1}.                    \tag{1.1}
\]

The factor L^d is exactly the physical coarse/fine measure ratio. Both Q_h and Q_h^T contract the bounded-field norm. For an input of norm a in the common nonlinear ball, every intermediate physical field has norm at most 2a. Transposing the ordered derivative chain and expanding its difference from the flat chain gives

\[
 \boxed{\quad
 \|DR(A)^T\|_{\infty\to\infty}
       \le e^{2D_*a/(L-1)}-1.\quad}            \tag{1.2}
\]

This is an absolute physical-column estimate; it is stronger than an unweighted global Hilbert bound. On a smaller ball one can write its right side as `c_* a`. The map `A -> DR(A)^T` is holomorphic into this bounded-operator space. It follows either by the finite one-step analytic chain, or by its absolutely convergent coefficient Taylor series in the physical row norm. Cauchy on a fixed larger ball then gives

\[
 \|DR(A)^T-DR(A')^T\|_{\infty\to\infty}
       \le c_{*,1}\|A-A'\|_\infty             \tag{1.3}
\]

uniformly on the smaller ball. None of these estimates requires a bounded-field norm for the gauge projection Pi.

### 1.2. The exact two-Hilbert-direction Hessian estimate

On the same fixed local complex neighborhood, let K_2 bound the local bilinear Hessian of F_L in the maximum norm of its two inputs. Physical scaling gives

\[
 |\langle w,D^2\mathcal F_h(A)[B,C]\rangle_{Lh}|
 \le k_2 h\|w\|_\infty\|B\|_{2,h}\|C\|_{2,h},
 \quad k_2=K_2N_LL^{d-1}.                    \tag{1.4}
\]

Indeed `D² mathcal F_h=(h/L) D²F_L(hA)`. Sum the two local input maxima using their local l2 norms, apply Cauchy--Schwarz over output bonds, count incidence N_L, and restore the fine physical measures. Unlike the earlier homogeneous quadratic coefficient, this is the full second derivative, so K_2 already includes its factor two.

Let P_t denote the derivative of the composition through stage t, and let T_t denote the derivative of the nonlinear suffix after stage t+1, evaluated along the actual intermediate trajectory. The exact second-order chain rule is

\[
 D^2\mathcal F(A)[B,C]
   =\sum_{t<j}T_t D^2\mathcal F_{h_t}(A_t)[P_tB,P_tC].
 \tag{1.5}
\]

The prefix physical L2 norms are bounded by `exp(2D_2aS)` and the suffix transpose bounded-field norms by `exp(2D_*aS)`, where S=(L-1)^-1. Pair with w, use (1.4), and sum h_t. This proves

\[
 \boxed{\quad
 |\langle w,D^2\mathcal F(A)[B,C]\rangle_1|
 \le k_2S e^{(4D_2+2D_*)aS}
       \|w\|_\infty\|B\|_{2,\eta}\|C\|_{2,\eta}.
 \quad}                                                   \tag{1.6}
\]

This is the uniform constraint-Hessian form bound needed for a minimum, not just an ordinary bounded-field Cauchy estimate.

## 2. Exact flat constrained identities and stationarity equation

Let H be the matched source-gauge flat minimizing extension. The flat identities are

\[
 QH=I,\qquad KH=Q^Tq,\qquad RD^TH=0.
 \tag{2.1}
\]

Let `X=ker Q intersect ker(RD^T)` be the real flat gauge/constraint slice, complexified when required. The constrained Green operator is

\[
 \mathcal C=\Pi\Gamma\Pi^T=\Gamma-DZD^T,
 \qquad \Gamma=G_0-H(q+a)^{-1}H^T.
 \tag{2.2}
\]

The fixed-mesh algebra yields

\[
 Q\mathcal C=0,\quad RD^T\mathcal C=0,\quad
 \mathcal C Q^T=0,\qquad \mathcal C K\xi=\xi\quad(\xi\in X).
 \tag{2.3}
\]

In particular `H^T K xi=q Q xi=0`. The difference between q and the positive coarse auxiliary precision q+a is essential: q occurs in the Maxwell stationarity equation, while q+a occurs only in Gamma's subtraction. The identities in (2.2)--(2.3) are fixed-flat identities; no nonflat projection is introduced here.

For given coarse B use the exact constraint chart

\[
 A=\xi+H[B-R(A)],\qquad \xi\in X.
 \tag{2.4}
\]

It has `F(A)=B` and `RD^TA=0`. Its derivative in xi is

\[
 T_A=(I+H DR(A))^{-1},
\]

restricted to X. Let the ordinary potential gradient of the normalized action be

\[
 E(A)=KA+N(A).
 \tag{2.5}
\]

Stationarity in this chart is equivalent to `C T_A^T E(A)=0`. On a finite real regulator, C is the positive inverse of K on X, so its kernel is X's orthogonal complement; the same algebraic equivalence holds after complexification. The exact ordered identity

\[
 T_A^T=I-DR(A)^T(I+H^TDR(A)^T)^{-1}H^T
\]

and (2.1)--(2.4) give

\[
 \boxed{\quad
 \xi=-\mathcal C N(A)
  +\mathcal C DR(A)^T(I+H^TDR(A)^T)^{-1}
       \{q[B-R(A)]+H^TN(A)\}.
 \quad}                                                   \tag{2.6}
\]

This is the exact reduced nonlinear equation. No term from the nonlinear constraint has been discarded.

## 3. Precisely the Green and force inputs required

Let

\[
 \|A\|_{\mathcal N_\alpha}
       =\|A\|_\infty+\|\nabla A\|_\infty
                         +[\nabla A]_{\alpha}
\]

with physical lattice differences and the physical periodic distance. Harmless fixed sums over components are included. This norm controls the complete C^alpha norm of A and of its first differences, uniformly in eta, by telescoping for distances below one and the bounded norm for larger distances.

The following uniform flat bounds are the exact analytic inputs:

\[
 H:\ell^\infty_{\rm coarse}\to\mathcal N_\alpha,
 \qquad \mathcal C:\ell^\infty_{\rm fine}\to\mathcal N_\alpha,
 \tag{3.1}
\]

\[
 \boxed{\quad
 \mathcal C S_{\rm jet}^T:C^\alpha_{\rm fine}\to\mathcal N_\alpha.
 \quad}                                                   \tag{3.2}
\]

The operator S_jet takes a potential to a finite list of local values and ordinary first differences, as in the Wilson plaquette jet. Its transpose contains at most one fine difference. **The equal exponent alpha in (3.2) is essential.** A bound `C^gamma -> N_beta` with gamma>beta would not close the following fixed point. The now-audited constrained-Green proof establishes (3.2) using Gamma's bounded pieces and the separate biharmonic cancellation for `DZD^T S_jet^T`, with the fourth/fifth heat moments and the separation-dependent time split. It is not inferred merely from G_0's bound.

Also use the already available rectangular physical-cell bounds to obtain

\[
 H^T:\ell^\infty_{\rm fine}\to\ell^\infty_{\rm coarse},\qquad
 H^TS_{\rm jet}^T=(S_{\rm jet}H)^T:
       C^\alpha_{\rm fine}\to\ell^\infty_{\rm coarse},
 \quad q:\ell^\infty_{\rm coarse}\to\ell^\infty_{\rm coarse}.
 \tag{3.3}
\]

For the second map it suffices to use the bounded norm of the input: one physical cell has fixed volume, and the weighted cell Hilbert transpose rows of S_jet H are summable. Thus this operation never differentiates a rough nonlinear force coefficient.

The normalized Wilson force module supplies, in ordinary potential coordinates,

\[
 N(A)=S_{\rm jet}^T f_\eta(S_{\rm jet}A),\qquad f_\eta(0)=Df_\eta(0)=0,
 \tag{3.4}
\]

with holomorphic finite-dimensional functions uniform in eta. On a fixed small N_alpha ball,

\[
 \|f_\eta(S_{\rm jet}A)\|_{C^\alpha}\le c_f\|A\|_{\mathcal N_\alpha}^2,
\]
\[
 \|f_\eta(S_{\rm jet}A)-f_\eta(S_{\rm jet}A')\|_{C^\alpha}
 \le c_f(\|A\|_{\mathcal N_\alpha}+\|A'\|_{\mathcal N_\alpha})
                        \|A-A'\|_{\mathcal N_\alpha}.
 \tag{3.5}
\]

The action convention is the normalized coupling-free Wilson density. `wilson_source_normalization_research.md` now matches this convention in d=4 to Raw I:464--479 and the physical pairing at I:12756--12760. The ordinary-potential force and the source left-exponential Hessian concern the same action but are different coordinate Hessians away from the flat point; the force proof works directly in the coordinate used here.

## 4. A closed fixed point with uniform radii

Use the proved inputs (3.1)--(3.5). All maps in this section are between the displayed complete Banach spaces. Shrink the fixed common ball so that

\[
 \|H\|_{\infty\to\mathcal N_\alpha}\,
       \|DR(A)\|_{\infty\to\infty}<\tfrac12,
 \quad
 \|H^T\|_{\infty\to\infty}\,
       \|DR(A)^T\|_{\infty\to\infty}<\tfrac12.
 \tag{4.1}
\]

The first inequality upgrades the original bounded-field chart to an N_alpha analytic chart by the same contraction, since R(A) is a bounded coarse field. In particular, writing `b=||B||_infinity`,

\[
 \|A(\xi,B)\|_{\mathcal N_\alpha}
       \le2(\|\xi\|_{\mathcal N_\alpha}+h_N b),
 \quad
 \|A(\xi,B)-A(\xi',B)\|_{\mathcal N_\alpha}
       \le2\|\xi-\xi'\|_{\mathcal N_\alpha},
 \tag{4.2}
\]

where `h_N=||H||_{infinity->N_alpha}`. These hold in a common sufficiently small ball, not on an unrestricted field space.

Define

\[
 m(A,B)=(I+H^TDR(A)^T)^{-1}
           \{q[B-R(A)]+H^TN(A)\}.
 \tag{4.3}
\]

By (1.2)--(1.3), (3.3)--(3.5), and the second inequality of (4.1), there are fixed constants such that, for fields of N_alpha norm at most r,

\[
 \|m(A,B)\|_\infty\le C(b+r^2),\qquad
 \|m(A,B)-m(A',B)\|_\infty
       \le C(b+r)\|A-A'\|_{\mathcal N_\alpha}.
 \tag{4.4}
\]

For the first inequality, use the inverse norm at most two, `||R(A)||<=C_Rr^2`, and `(S_jet H)^T f`. For the second, use the inverse difference identity together with (1.3); the difference of the braces is O(r||A-A'||), and the difference of the inverses is O(||A-A'||) multiplying O(b+r^2). This proves (4.4) without a derivative of f.

Let the right side of (2.6), with A=A(xi,B), be Phi_B(xi). Equations (3.1)--(3.5) and (4.4) give

\[
 \|\Phi_B(\xi)\|_{\mathcal N_\alpha}
       \le C(r^2+rb+r^3),
\]
\[
 \|\Phi_B(\xi)-\Phi_B(\xi')\|_{\mathcal N_\alpha}
       \le C(b+r)\|\xi-\xi'\|_{\mathcal N_\alpha},
 \tag{4.5}
\]

after a fixed reduction of r. To verify the constraint term, expand
`DR(A)^T m(A,B)-DR(A')^T m(A',B)` into its two factors; use (1.2) on the unchanged derivative, (1.3) on its difference, and (4.4) on the multiplier. The map C in (3.1), rather than a divergent fine derivative norm, then gives its N_alpha bound. Both terms in Phi_B belong to X by (2.3).

These inequalities supply an explicit uniform contraction construction. First choose a fixed small radius r_* making the constants in (4.1) and the Lipschitz constant in (4.5) less than one half on the chart image of an X-ball. Then choose b_* sufficiently small that h_N b_* is inside that chart and the first estimate in (4.5) maps that X-ball into itself. The contraction produces a unique small solution `xi(B)` for every complex `||B||<b_*`, holomorphic in B.

The sharper estimate is

\[
 \|\xi(B)\|_{\mathcal N_\alpha}\le C b^2,
 \quad
 \|A(B)-HB\|_{\mathcal N_\alpha}\le C b^2,
 \quad
 \|A(B)\|_{\mathcal N_\alpha}\le C b.          \tag{4.6}
\]

For a direct verification, use the ball `||xi||<=K b^2`; (4.2) gives r<=4h_Nb after reducing b, and the first inequality (4.5) is at most `C' b^2`. Choose K>2C' and reduce b again so that the Lipschitz constant is below one half and `K b^2<=h_Nb`. This smaller-ball solution equals the unique solution in the original fixed ball. The chart remainder `-HR(A)` proves the second bound in (4.6). Cauchy on smaller coarse bounded-field balls gives factorial analytic derivatives with constants independent of mesh and volume.

The independently proved equal-exponent estimate (3.2) and force module supply every input to this contraction. The averaging adjoints and nonlinear constraint curvature introduce no further mesh loss.

## 5. Why the real stationary point is a strict local minimum

For real data the Wilson density has ordinary-potential Hessian

\[
 D^2\mathcal S(A)=K+S_{\rm jet}^T W(A)S_{\rm jet},
 \qquad \|W(A)\|_\infty\le C\|A\|_{\mathcal N_\alpha}.
 \tag{5.1}
\]

This follows from the same finite-dimensional density whose nonlinear gradient is (3.4): its quadratic part is exactly the flat Maxwell density. It is an ordinary-coordinate identity and does not silently identify a left-exponential Hessian at a nonzero connection.

The flat full inverse's energy bound implies, for `z in X`,

\[
 \|z\|_{2,\eta}^2+\|\nabla z\|_{2,\eta}^2
       \le C_E\langle z,Kz\rangle_\eta.          \tag{5.2}
\]

Indeed the flat gauge and averaging penalties vanish on X, so its positive full precision has the same quadratic form as K there. Apply the bound on `(I,nabla)G_0(I,nabla)^T`. The q in (2.1) is positive semidefinite on real coarse fields.

Let z be an xi-direction, `v=T_Az`, and let `E_z=<z,Kz>`. The chart equation gives

\[
 v=z-H DR(A)v.
\]

The cross terms in its flat Maxwell form vanish since `H^T Kz=0`, so

\[
 \langle v,Kv\rangle
   =E_z+\langle DR(A)v,q DR(A)v\rangle\ge E_z.
 \tag{5.3}
\]

At the same time, the uniform physical L2 bound on DR(A), the H and first-derivative H Hilbert bounds, and a further smallness reduction yield

\[
 \|v\|_2\le2\|z\|_2,\qquad
 \|v\|_2^2+\|\nabla v\|_2^2\le C E_z.          \tag{5.4}
\]

These estimates use the positive energy control (5.2), not an invalid fine L2-to-pointwise comparison.

Differentiate the exact constraint a second time. The chart's second derivative is

\[
 A''=-H_A D^2\mathcal F(A)[v,v],
 \qquad H_A=(I+H DR(A))^{-1}H.
\]

Furthermore `H_A^T E(A)=m(A,B)` by (2.1), (2.4) and (4.3). Hence the Hessian of the reduced action is exactly

\[
 D^2_\xi[\mathcal S(A(\xi,B))][z,z]
  =\langle v,D^2\mathcal S(A)v\rangle
    -\langle m(A,B),D^2\mathcal F(A)[v,v]\rangle.
 \tag{5.5}
\]

The first term is bounded below by `(1-Cr)E_z`, by (5.1)--(5.4). The second term is bounded in absolute value by `C(b+r^2)E_z`, by (1.6), (4.4), and (5.4). Therefore throughout a sufficiently small real chart,

\[
 D^2_\xi[\mathcal S(A(\xi,B))][z,z]
       \ge\tfrac12\langle z,Kz\rangle
       \ge c\|z\|_{2,\eta}^2.                \tag{5.6}
\]

The constants do not depend on regulator volume or refinement. This proves strict local minimality and local uniqueness on the fixed flat gauge/constraint slice. It does not prove a global minimum among large fields, nor does it show that this slice covers every nonlinear gauge orbit preserving the target constraint.

## 6. Regulator and source scope

The action and minimum statement are first for finite compatible periodic regulators, with uniform constants. The same contraction can define a bounded infinite-lattice stationary field once the stated kernels act in the indicated spaces, but a bounded field generally has infinite total action. Without additional finite-energy assumptions only local stationarity and justified finite-support or decaying comparisons should be asserted there.

The source action prefactor and left-exponential/ordinary-coordinate relationship have been checked separately in `wilson_source_normalization_research.md`. The force proof avoids identifying those distinct coordinate Hessians by working directly in the global physical potential A. The gauge condition here remains `RD^T A=0` with the fixed flat R. A proof of nonlinear gauge-orbit coverage or the source's own nonlinear minimizer gauge is still required before identifying this local fixed-gauge solution with an unrestricted source minimizing field.
