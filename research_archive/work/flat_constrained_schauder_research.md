# A constrained flat inverse with equal-exponent Schauder bounds

16 October 2026. Proof module independently audited; see `flat_constrained_schauder_audit.md`. This note supplies the flat constrained Green operator needed by the nonlinear fixed-gauge minimizer argument. It uses the established flat source-gauge identities, fine pointwise inverse bounds, equal-exponent heat estimates, and localized minimizing extension. It does not assert a nonflat Schauder theorem.

## 1. Definitions and the precise assertion

Use fine spacing `eta=1/M`, physical fine measure `eta^d`, unit coarse cells, and the previously matched homogeneous flat operators

\[
 K=d^Td,\quad L=D^TD,\quad
 A_0=K+DRD^T+Q^Ta_{\rm pen}Q,\quad G_0=A_0^{-1}.
                                                               \tag{1.1}
\]

Here `D` is the scalar fine gradient, `d` the one-form curl, `Q=Q_M^st` the normalized one-form straight-string average, and `Q_0` the scalar block average. The fixed positive one-form penalty belongs to a compact positive interval; it is one in the unit-scale source normalization. Define

\[
 q_{\rm aux}=(QG_0Q^T)^{-1},\qquad
 H=G_0Q^Tq_{\rm aux},\qquad
 \Gamma=G_0-Hq_{\rm aux}^{-1}H^T.                \tag{1.2}
\]

The already proved source-gauge extension satisfies `QH=I` and `RD^TH=0`. The scalar gauge operators obey

\[
 G'=(L+Q_0^Ta'Q_0)^{-1},\quad
 R=I-G'Q_0^T(Q_0(G')^2Q_0^T)^{-1}Q_0G',\quad
 Z=G'RG',
\]
\[
 \Lambda=ZLD^T=G'RD^T,\qquad \Pi=I-D\Lambda.
                                                               \tag{1.3}
\]

The scalar penalty can be fixed to one because `R` is independent of that auxiliary penalty. All transposes are for physical measure. Initially identities are real Hilbert identities; their complex linear extensions use the bilinear transpose.

Write `S_jet=(I,nabla)`, where `nabla` includes all ordinary fine first differences of bond components. Thus `S_jet^T(f_0,f_1)=f_0+nabla^T f_1`. Curl and other finite component contractions are included by choosing components of `f_1`.

For a fixed `0<alpha<1`, let `||f||_(alpha,varpi)` be the weighted supremum plus local alpha-Hölder seminorm of a complete fine field on fixed unit-cell collars. The admissible coarse-cell weight satisfies

\[
 \varpi(n)/\varpi(m)\le e^{\kappa d(n,m)}.        \tag{1.4}
\]

Let `N_(alpha,varpi)(A)` contain the weighted field supremum, first-difference supremum, and alpha-Hölder seminorm of the first differences on those collars. The collar sizes are fixed; changing them by a fixed enlargement changes constants only. No field is sharply cut into cells before taking its derivatives.

**Theorem 1.1.** For some fixed sufficiently small `kappa>0` and every fixed `0<alpha<1`, the constrained flat operator

\[
 \boxed{\ \mathcal C=\Pi\Gamma\Pi^T
                   =\Gamma-DZD^T\ }             \tag{1.5}
\]

obeys, uniformly in refinement and compatible periodic volume,

\[
 N_{\alpha,\varpi}(\mathcal C f)
       \le C_\alpha\|f\|_{\infty,\varpi},       \tag{1.6}
\]
\[
 N_{\alpha,\varpi}(\mathcal C S_{\rm jet}^T(f_0,f_1))
       \le C_\alpha
          (\|f_0\|_{\infty,\varpi}
                         +\|f_1\|_{\alpha,\varpi}).       \tag{1.7}
\]

In particular (1.7) gives the requested map from a `C^alpha` jet into `N_alpha`, with no exponent loss. The exact constraints and inverse identities are

\[
 Q\mathcal C=0,\qquad RD^T\mathcal C=0,
                                                               \tag{1.8}
\]
\[
 \mathcal C K\xi=\xi\quad
   (Q\xi=0,\ RD^T\xi=0),\qquad
 \mathcal C KH=0.                                  \tag{1.9}
\]

The same assertions hold on the full lattice, with complete weighted fields. There is no assertion at `alpha=0` or `alpha=1`. The constants may diverge at those endpoints.

## 2. Exact constrained algebra

The established scalar identities are

\[
 Q_0Z=0,\quad LZL=R,\quad ZL^2Z=Z,
 \quad G_0\Lambda^T=DZ.                           \tag{2.1}
\]

For completeness, `LZL=R` follows from `LG'R=R` and its transpose. The identity `ZL^2Z=Z` expresses that `Z` is the inverse of the form `||L lambda||^2` on `ker Q_0`. The last identity was proved with the flat gauge inverse and is also obtained by multiplying its two sides by `A_0`.

Since `Lambda H=G'RD^TH=0`, (1.2) and (2.1) imply

\[
 \Gamma\Lambda^T=DZ,\qquad
 \Lambda\Gamma=ZD^T,\qquad
 \Lambda\Gamma\Lambda^T
     =\Lambda DZ=ZL^2Z=Z.                         \tag{2.2}
\]

Expanding `(I-DLambda) Gamma (I-Lambda^T D^T)` now gives exactly (1.5), with one surviving subtraction, not two.

The flat cochain identity `QD=D_cQ_0` and (2.1) imply `QPi=Q`. Also

\[
 RD^T\Pi=RD^T-RLZLD^T=RD^T-R^2D^T=0.            \tag{2.3}
\]

Since `QGamma=0`, the factorized form in (1.5) gives (1.8). The operator `C` is symmetric; hence it also annihilates the transpose constraint ranges.

The constrained covariance identities are

\[
 \Gamma A_0=I-HQ,\qquad A_0H=Q^Tq_{\rm aux}.     \tag{2.4}
\]

If `Qxi=RD^Txi=0`, then `A_0xi=Kxi`, so `Gamma Kxi=xi`. Moreover `D^TK=0`, because `dD=0`. Applying (1.5) proves the first identity in (1.9). Since `QH=I` and `RD^TH=0`, the second identity in (2.4) gives

\[
 KH=Q^T(q_{\rm aux}-a_{\rm pen}I).
                                                               \tag{2.5}
\]

Now `C Q^T=0` proves the last identity in (1.9).

On real finite regulators `Gamma` is nonnegative, so `C=Pi Gamma Pi^T` is nonnegative. Its range lies in
`V=ker Q intersect ker(RD^T)`. For any `xi in V`, symmetry and (1.9) give

\[
 \langle\xi,K\mathcal Cf\rangle
       =\langle\xi,f\rangle.                     \tag{2.6}
\]

The restriction of `K` to `V` is positive definite: there it equals the positive form `A_0`. Thus `C` is exactly the variational inverse on this fixed constrained slice. This characterization explains why the constraints needed by the nonlinear minimizer are preserved.

## 3. The simpler term: Gamma with a differentiated datum

The established flat Schauder result is

\[
 N_{\alpha,\varpi}(G_0\nabla^Tf)
       \le C_\alpha\|f\|_{\alpha,\varpi},
                                                               \tag{3.1}
\]

for any selected ordinary fine divergence, with finite orientation contractions allowed. Its proof is the global massive heat-kernel cancellation and the separation-dependent time split audited in `flat_schauder_scalar_audit.md` and promoted to Notebook 12. The same baseline proof gives `G_0:infinity -> N_alpha`.

The localized minimizing extension has cellwise kernel bounds

\[
 \|H(\cdot,b)\|_{C^{1,\alpha}(\text{collar }n)}
     \le C_\alpha e^{-\rho d(n,b)},               \tag{3.2}
\]

and `q_aux^-1=QG_0Q^T` has a uniformly exponentially summable coarse kernel. Therefore

\[
 Hq_{\rm aux}^{-1}(\nabla H)^T:
       \ell^\infty_{\varpi}\longrightarrow N_{\alpha,\varpi}
                                                               \tag{3.3}
\]

has uniform norm for a sufficiently small fixed weight exponent. To see the input estimate directly, the physical transpose sums `eta^d (nabla H)^T f`; each cell has physical volume one, and (3.2) bounds that row sum without a fine-dimension factor. The two coarse exponential kernels and the output bound (3.2) can then be convolved with their fixed weight slack.

At fixed spacing the exact transpose identity yields

\[
 \Gamma\nabla^T=G_0\nabla^T
        -Hq_{\rm aux}^{-1}(\nabla H)^T.            \tag{3.4}
\]

Combining (3.1)–(3.4),

\[
 N_{\alpha,\varpi}(\Gamma\nabla^Tf)
      \le C_\alpha\|f\|_{\alpha,\varpi}.         \tag{3.5}
\]

The undifferentiated version similarly gives `Gamma:infinity -> N_alpha`.

## 4. The scalar subtraction: a smoother remainder

Set `Z_m=(L+1)^-2`. We claim

\[
 N_{\alpha,\varpi}
       (D(Z-Z_m)D^T\nabla^Tf)
       \le C_\alpha\|f\|_{\infty,\varpi}.        \tag{4.1}
\]

The canceled scalar aliases are, with
`A=a_0a_0^-`, `R_s,2=sum_(r!=0)a_ra_r^-/P_r^2`, and
`D_s,2=A+P_0^2R_s,2`,

\[
 Z_{00}=R_{s,2}/D_{s,2},\qquad
 Z_{0s}=-a_0^-a_s/(P_s^2D_{s,2}),\qquad
 Z_{r0}=-a_r^-a_0/(P_r^2D_{s,2}),
\]
\[
 Z_{rs}=\frac{\delta_{rs}}{P_r^2}
      -\frac{P_0^2a_r^-a_s}{P_r^2P_s^2D_{s,2}}
                   \quad(r,s\ne0).              \tag{4.2}
\]

They are bounded and holomorphic on a refinement-independent enlarged tube. The massive denominator `P_0+1` remains bounded away from zero after a fixed further shrinking, and the high massive denominators are uniformly gapped.

The high diagonal of `Z-Z_m` has the exact representation

\[
 P_r^{-2}-(P_r+1)^{-2}
   =\int_0^\infty t(1-e^{-t})e^{-tP_r}\,dt,
                         \qquad r\ne0.          \tag{4.3}
\]

The operator in (4.1) has one external output derivative, two external input derivatives, and at most one further output derivative plus an alpha-Hölder increment. Thus the greatest heat order required is `4+alpha`. The absolute small-time row bound is

\[
 t(1-e^{-t})\,t^{-(4+\alpha)/2}
      \le t^{-\alpha/2},\qquad 0<t\le1,          \tag{4.4}
\]

which is integrable. The complex Bloch image-kernel estimates and fixed-order semigroup splitting used in the earlier pointwise proof apply through order five here. Subtracting the central heat mode adds only a bounded term on this time interval. Large times use the high-alias spectral gap, also uniform in the fixed small complex tube.

Every remaining term of (4.2) is central or finite rank. A high rank output vector is `a_r^-/P_r^2`. The external `D`, the output first difference, and an alpha-Hölder increment multiply it by at most `C(1+|r|)^(2+alpha)`. Consequently its absolute alias sum is bounded by the sum of

\[
 C\prod_\nu(1+|r_\nu|)^{-1}(1+|r|)^{-2+\alpha}.
                                                               \tag{4.5}
\]

On dyadic max-norm shell `2^j<=|r|_infinity<2^(j+1)`, the product of one-dimensional weights sums to at most `C(1+j)^(d-1)`. The sum of (4.5) is therefore bounded by
`C sum_j(1+j)^(d-1)2^(-j(2-alpha))`, uniformly in `M`.
The two input differences leave the rank input row bounded by
`C|a_s|(1+|s|)^-2`, hence uniformly bounded in alias `ell2`. Central rows and columns are bounded. Physical cell `L2` is dominated by the cell supremum with no dimension factor.

These estimates give uniform holomorphic bounded-input to output-`C^(1,alpha)` cell blocks. Only the fully reconstructed operator is glued periodically and contour-shifted; individual central chart pieces need not be periodic. The resulting exponential cell estimates, summed with weight slack, prove (4.1). They periodize exactly on compatible finite tori. Sharp cell support of `f` causes no problem in (4.1), because its datum needs no Hölder regularity and both input differences have already been placed on the kernel.

## 5. Massive biharmonic cancellation with no Hölder loss

It remains to show

\[
 N_{\alpha,\varpi}(DZ_mD^T\nabla^Tf)
      \le C_\alpha\|f\|_{\alpha,\varpi}.         \tag{5.1}
\]

All factors in this expression commute with the translation-invariant scalar heat semigroup, except for fixed orientation contractions, which only change constants. Since

\[
 Z_m=\int_0^\infty t e^{-t}e^{-tL}\,dt,          \tag{5.2}
\]

the output field uses three ordinary fine differences of the heat kernel, and its output gradient uses four.

The heat estimates extend to every fixed integer derivative order. We need the following weighted alpha-moment bounds through order five:

\[
 \sum_v e^{\kappa|v|_1}|v|_1^\alpha
       |\nabla_\eta^k p_t^\eta(v)|
    \le C_{k,\alpha} t^{(\alpha-k)/2},
       \qquad 0<t\le1,\quad k=4,5.              \tag{5.3}
\]

Here `p_t^eta` is the probability heat kernel; use of its density against physical volume gives exactly the same operator row sum. For `t>=eta^2`, split the semigroup into `k` equal factors and apply the established weighted first-difference variation bound with exponential scale `delta=kappa+t^-1/2`, increasing fixed constants for the split times. The exponential moment is bounded by `exp(C delta^2 t)`, and the derivative row bound is `C_k t^-k/2`. The polynomial moment is paid by an additional `exp(|v|/sqrt t)`, giving (5.3).

For `0<t<eta^2`, expand `nabla_eta^k` into its fixed finite list of shifts by at most `k eta`, with coefficients bounded by `C_k eta^-k`. The dimensionless random walk has time less than one and uniformly bounded fixed moments. This gives `C eta^(alpha-k)`, which is at most `C t^((alpha-k)/2)` since `alpha-k<0`. This also proves (5.3) at sub-mesh times. For large times one chooses a fixed small extra exponential moment so that its growth is dominated by half of the mass factor `e^-t`.

Every positive-order heat derivative has exact zero row sum. A complete weighted Hölder field satisfies

\[
 \varpi(n_x)|f(x-v)-f(x)|
  \le C\|f\|_{\alpha,\varpi}
                   e^{\kappa|v|_1}|v|_1^\alpha.       \tag{5.4}
\]

For short displacements this is the collar Hölder bound; for longer displacements use the weighted supremum and the weight ratio. Subtracting `f(x)` in each derivative row and using (5.3) therefore gives, for `t<=1`,

\[
 \|t\nabla^4e^{-tL}f\|_{\infty,\varpi}
      \le C t^{-1+\alpha/2}\|f\|_{\alpha,\varpi},
\]
\[
 \|t\nabla^5e^{-tL}f\|_{\infty,\varpi}
      \le C t^{-3/2+\alpha/2}\|f\|_{\alpha,\varpi}.
                                                               \tag{5.5}
\]

For two output points in a fixed collar at distance `eta<=r<=1`, use twice the first bound for `t<r^2`, and telescope the finite difference along a fine path using `r` times the second bound for `t>=r^2`. The path length is at most a fixed dimensional multiple of `r`; it stays in an enlarged fixed collar. After integrating (5.2), the output-gradient difference is bounded by

\[
 C\|f\|_{\alpha,\varpi}
 \left(\int_0^{r^2}t^{-1+\alpha/2}\,dt
     +r\int_{r^2}^1t^{-3/2+\alpha/2}\,dt+r\right)
 \le C\left(\frac2\alpha+\frac2{1-\alpha}+1\right)
           r^\alpha\|f\|_{\alpha,\varpi}.        \tag{5.6}
\]

The last `r` is the massive large-time tail. Distances above one use the supremum bound. The gradient supremum uses the first integral in (5.5), which is finite for `alpha>0`. The field supremum is easier: the absolute third-difference heat row multiplied by `t` is `O(t^-1/2)` and is integrable even for bounded input. This proves (5.1). It is essential to split before taking the Hölder supremum; integrating a fixed alpha-Hölder operator bound down to zero would falsely suggest a logarithmic loss.

Combining (4.1) and (5.1) gives

\[
 N_{\alpha,\varpi}(DZD^T\nabla^Tf)
       \le C_\alpha\|f\|_{\alpha,\varpi}.       \tag{5.7}
\]

The already established scalar smoothing estimate gives
`DZD^T:infinity -> N_alpha`; it can also be seen by removing one input derivative above. Its small-time absolute row integrand is `t*t^(-(3+alpha)/2)`, integrable for `alpha<1`. Rank terms become easier. Together with Section 3 and (1.5), these estimates prove (1.6)–(1.7).

## 6. Infinite volume, constraints on complete fields, and application boundary

Every bound was proved with a fixed positive spatial exponent and physical cell measure. For remainder and extension terms it follows from holomorphic cell reconstruction and exponential kernel bounds. For the massive part it follows directly from the full-lattice weighted heat estimates and cancellation. Thus (1.6)–(1.7) apply to complete fields and their localized smooth-cutoff versions without an inverse power of the fine spacing from artificial cell boundaries. Compatible periodic kernels are exact periodizations; periodic distance and fixed cover multiplicities preserve the bounds, including small periods.

The exact identities (1.8)–(1.9) first hold on finite regulators and square-summable fields by the preceding algebra. At each fixed spacing all required operator products are exponentially summable in cell coordinates. In particular `R=LZL`, and the fixed-spacing equivalence of finite cell norms is enough to justify absolute convergence on bounded complete fields; its constant need not be uniform for this identity argument. Truncation with tails then extends the identities to the bounded and admissibly weighted fields used above. No assertion that the gauge projection is a local operator is required.

For `xi` in the constrained `N_alpha` space, interpret `Kxi=d^Td xi` either at the fixed discrete spacing or as a first-divergence datum with Hölder coefficients. Estimate (1.7) applies to the latter interpretation and the exact identity agrees with both. Consequently the theorem supplies the Green module assumed in Section 3 of `nonlinear_fixed_gauge_minimizer_research.md`: a source-compatible constrained inverse with both exact constraints, a bounded-forcing estimate, and an equal-exponent jet-forcing estimate.

It does not alone establish the nonlinear variational equations. Those require the separately verified action remainder and nonlinear constraint derivatives. The present result is homogeneous and flat; it does not claim moving-gauge/nonflat Schauder regularity, mixed retained-history domains, or an interacting continuum limit.
