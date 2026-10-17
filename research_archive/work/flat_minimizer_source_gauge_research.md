# The source scalar gauge projection and the next locality interface

16 October 2026. This short source check follows the audited homogeneous flat precision and ultraviolet-limit results. All line references are to the deposited files at commit `e392ef45013a581664bab76b90867170b30fe10e`; `I` means `theorem_0_complete_account_raw_I.tex`, and `III` means its raw III counterpart. The original CMP99b PDF has not been independently recovered here, so the exact source citations below are identified as deposited transcriptions.

## 1. Exact scalar averaging and projection definitions

I:23909–23918, equations `4.6:eq-local-generators-1` and `-2`, gives

\[
 (Q'_n(U)\lambda)(y)=\sum_{x\in B^n(y)}L^{-nd}
       \operatorname{Ad}(U(\Gamma^{(n)}_{y,x}))\lambda(x).
\]

The deposit attributes this to CMP99b (3.18), (3.19), with the paths of CMP98 (58), (77). At the flat homogeneous background this is exactly the scalar centered block average `Q_0=Q_M^(0)`. With physical-volume measures, `Q_0 Q_0^*=I` and `Q_0^*Q_0` is the orthogonal projection onto block-constant fine scalar fields.

I:23937–23944, equations `4.6:eq-local-generators-3` through `-5`, gives the local Dirichlet versions of

\[
 \mathcal L_a=\mathcal L+Q_0^*a'Q_0,\qquad G'=\mathcal L_a^{-1},
\]
\[
 T'=Q_0G'^2Q_0^*,\qquad
 P=G'Q_0^*(T')^{-1}Q_0G',\qquad R=I-P.             \tag{1.1}
\]

Here `mathcal L` denotes the positive scalar flat Laplacian; the deposit calls the corresponding covariant object `Delta_U`. These formulas are attributed to CMP99b (3.24), (3.25). The same algebra is reproduced without local subscripts at I:24940–24942. I:25588–25592 explicitly identifies the one-scale scalar generator as the Laplacian plus `Q'^* a' Q'`.

These scalar operators must not be confused with the separate lower-order bond remainder also called `Delta'` at I:13617.

### 1.1 The source bond constraint is the corrected straight average at flatness

I:24349–24373 reproduces CMP98 (122)–(125). The source `Q(V_0)` is the linear part of the corrected **double-bar** group average, not the original rooted group average. Its leading term is

\[
 (Q(V_0)A)_c=\sum_{x\in B(c_-)}L^{-(d+1)}
                    (R_{0,c_-}A)([x,x'])+\text{corrections}.
                                                               \tag{1.2}
\]

At the trivial background, the logarithmic background variables `Y,Y_x` vanish and all transports equal the identity. Each correction bracket in I:24359–24365 then vanishes: the brackets of the first type become `g(0)g(0)^-1−1`, and the final bracket becomes `1−g(0)sum_x L^-d g(0)^-1`. No numerical value of `g(0)` beyond its stated invertibility is needed for these cancellations.

The contour convention is explicit at I:47124–47131: `x'=x+L e_mu`, and `[x,x']` is the straight translate of the coarse bond. Thus

\[
 Q(1)=Q_L^{\rm st}.
                                                               \tag{1.3}
\]

I:47046–47048 states that the higher `Q_j` are compositions of these one-step CMP98 (124) operators, citing CMP99b (3.15). The base-L digit/string composition already proved in `current_interface_research.md` Section 10.2 therefore gives

\[
 Q_j(1)=Q_{L^j}^{\rm st}.
                                                               \tag{1.4}
\]

Finally, I:47120–47123 explicitly distinguishes this corrected one-step map from the rooted fluctuation constraint: `Q_1=Q^flat+bar D_1 mathfrak a`, and identifies `Q_1` with CMP98 (124). This is precisely why the `Q` entering the fine minimizer and the later rooted `Q^flat` entering the pivot insertion must not be collapsed. Equations (1.3)–(1.4) establish the homogeneous flat bond-constraint match for the displayed source formulas, while leaving the nonflat and retained-history identifications outside the result.

## 2. The projection is not the elementary block-mean projection

On a real finite regulator, assume `mathcal L_a` is positive and invertible and `Q_0` is onto. Put `B=G'Q_0^*`. Then `T'=B^*B`, so (1.1) is exactly

\[
 P=B(B^*B)^{-1}B^*.
\]

Therefore

\[
 \operatorname{ran}P=\operatorname{ran}(G'Q_0^*),
 \qquad
 \operatorname{ran}R=\ker(Q_0G')
             =\mathcal L_a\ker Q_0=\mathcal L\ker Q_0.
                                                               \tag{2.1}
\]

The middle equality uses invertibility of `G'`, and the last uses `Q_0 lambda=0`. Equivalently,

\[
 R\rho=0
 \quad\Longleftrightarrow\quad
 \rho\in\operatorname{ran}(G'Q_0^*).
                                                               \tag{2.2}
\]

This is different from requiring `rho in ran Q_0^*`. In particular, a minimizing extension whose divergence lies in `ran Q_0^*` is in a natural block-mean gauge, but not automatically in the source gauge `R D^*H=0`.

In a nonzero coarse Bloch sector, the scalar Laplacian `mathcal L` is invertible. With `W_s=Q_0 mathcal L^-1 Q_0^*`,

\[
 G'Q_0^*=\mathcal L^{-1}Q_0^*(I+a'W_s)^{-1},
 \qquad
 \ker R=\operatorname{ran}(\mathcal L^{-1}Q_0^*).
                                                               \tag{2.3}
\]

The finite coarse factor is invertible by positive definiteness (or directly by the same massive scalar inverse); it changes the parametrization of the range, not the range. At coarse momentum zero this inverse-Laplacian notation must not be used. There the scalar averaging multiplier vanishes on every noncentral alias and reads only the fine constant scalar mode. The original penalized `G'` definition shows that `ker R` is the span of that constant mode, and `R` is the identity on the remaining scalar aliases. A constant one-form lift has zero divergence and automatically satisfies the source gauge.

For a concrete mismatch, take a one-dimensional periodic fine lattice with six sites, grouped into two adjacent blocks of three sites. Let `v` equal `+1` on the first block and `-1` on the second. Then `v in ran Q_0^*`, but its fine Laplacian is nonzero at the block interfaces and zero at each interior site, so `mathcal L v` is not block constant. The penalty `Q_0^* a'Q_0 v` is block constant and cannot repair this. If the finite-dimensional subspaces `ran G'Q_0^*` and `ran Q_0^*` were equal, their common subspace would be preserved by `G'` and its inverse `mathcal L_a`, contrary to this calculation. More specifically, if this `v` belonged to `ran G'Q_0^*`, then `mathcal L_a v` would be block constant, again a contradiction. Thus `Rv !=0`. Tensoring with constants in the other directions embeds the example in higher dimensions.

## 3. An exact gauge correction, with locality left explicit

There is a useful algebraic bridge. Let `D` be the fine scalar gradient, so `D^*D=mathcal L`, and suppose the one-form constraint `Q` under consideration obeys the exact cochain identity

\[
 QD=d_c Q_0.
                                                               \tag{3.1}
\]

Let `H` be an exact Maxwell minimizing extension with `QH=I`. Define

\[
 H_{\rm src}=(I-DG'RD^*)H.                         \tag{3.2}
\]

The definitions give

\[
 Q_0G'R=Q_0G'-Q_0G'^2Q_0^*(T')^{-1}Q_0G'=0.
                                                               \tag{3.3}
\]

Consequently `mathcal L G'R=R`, because
`mathcal L_a G'R=R` and `Q_0 G'R=0`. Thus

\[
 QH_{\rm src}=QH-d_cQ_0G'RD^*H=I,
\]
\[
 D^*H_{\rm src}=D^*H-RD^*H=PD^*H,
 \qquad RD^*H_{\rm src}=0.                         \tag{3.4}
\]

The correction is a fine gradient and hence leaves curl and Maxwell energy unchanged. Therefore (3.2) gives an exact feasible minimizer in the source scalar gauge for this same `Q`.

On a connected flat periodic lattice, the gauge-selected minimizer is unique. The difference of two Maxwell minimizers with the same datum has zero curl: the restriction of the positive quadratic energy to the affine constraint space has this null direction. Discrete Hodge decomposition writes that difference as `D lambda+c`, where `c` is a constant harmonic one-form. Applying `Q=Q_M^st` and (3.1), then taking the coarse mean, gives `c=0`. The remaining equation is `d_c Q_0 lambda=0`, so `Q_0 lambda` is a scalar constant. Subtract that same fine scalar constant from `lambda`; this does not change `D lambda` and arranges `Q_0 lambda=0`. Then `mathcal L lambda in ran R` by (2.1), while the difference of the source gauge equations gives `R mathcal L lambda=0`. Therefore `mathcal L lambda=0`, and connectedness gives `D lambda=0`. At coarse zero momentum the unique selected lift of a datum is its constant fine one-form. The analogous Dirichlet statement requires the specified scalar boundary domain and absence of extra harmonic modes.

This argument does not yet give scale-uniform exponential or derivative bounds for the correction. Such bounds require locality of `G'R` on the exact fine/coarse measures and of its composition with `D^*H`. The source itself names `Lambda=G'RD_U^*` at I:13629–13636; it quotes its weighted estimates rather than deriving them there.

The source bond-constraint identification in Section 1.1 resolves this particular match in the homogeneous flat corrected-average problem. Thus an exact Maxwell minimizer with `Q_M^st H=I` and `RD^*H=0` equals the source's gauge-selected flat `H_1` once that source map is identified as the minimizer of its displayed stationary quadratic action. Equality of the energy infima alone would not have established this; the actual constraint and the uniqueness argument are essential. This conclusion does not identify arbitrary nonflat or retained-history maps, nor the original rooted constraint without its correction.

## 4. The next source-locality bottleneck

The new flat covariance theorem controls the coarse quadratic action, but response bounds for the actual complex independent-current precision need localized fine response legs. The exact source loci are:

* I:13638–13655: `H_0=G_0Q^* q_0 ell^-1`, `q_0=(QG_0Q^*)^-1`, and `QH_0=ell^-1`. A normalized right inverse is `H_0 ell`, not `H_0` itself. The quoted kernel inputs occur at I:13569–13627; the covariance inverse bound is explicitly attributed there to a statement printed without proof.
* I:13678 and following, lemma `4.5:lem-free-current-operators`: the independent-current operators are built by adding the current-dependent gauge terms. Their source theorem cannot be replaced by a physical-current identity alone.
* III:36350–36366: the second jet of the constrained action is `H_1^* Delta_1 H_1`, with `H_1=G_1Q^*(QG_1Q^*)^-1` and `RD^*H_1=0`. The deposit attributes the quadratic action to CMP109 (2.8), CMP102b (174)–(177), and its covariance bounds to CMP99b (3.132).

A local fine minimizing extension, together with its first fine curl/gradient bound, would control the external legs in localized variations of this effective quadratic form. For example, in a real finite-dimensional stationary quadratic family with `QH=I` and `Delta H=Q^*q`, differentiation gives the exact identity

\[
 \dot q=H^*\dot\Delta H
          -H^*\dot Q^*q-q\dot QH.                 \tag{4.1}
\]

It follows by differentiating `q=H^*Delta H` and using
`Q dot H=−dot Q H`; no derivative estimate for `dot H` is needed in this first formula. Thus localized coefficient perturbations would produce two localized fine response legs if `H` and the derivatives appearing in the local quadratic form had suitable scale-uniform spatial bounds. Formula (4.1) is a conditional quadratic identity, not a declaration that every independent-current source carrier is stationary or has this representation.

The immediate concrete target is therefore a scale-uniform exponentially local fine minimizing extension in a specified compatible gauge, followed by the source-gauge correction (3.2) or a proof that the required first response is gauge independent. The required fine gradient/curl norms, the exact one-form constraint match, and the independent-current holomorphic domain must be retained. A merely global L2-bounded lift, or exponential decay of the coarse `q_M` alone, does not supply these localized fine legs.
