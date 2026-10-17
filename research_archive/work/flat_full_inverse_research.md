# The full flat source inverse: exact cancellation and uniform locality

16 October 2026. This note derives a uniformly local inverse for the homogeneous flat fine operator

\[
 \mathcal A_a=K+DRD^*+Q^*aQ,\qquad G_0=\mathcal A_a^{-1},
                                                               \tag{0.1}
\]

where `K=d^*d` is the fine Maxwell precision, `D` the fine scalar gradient, `Q=Q_M^st` the normalized straight-string average, and `R` the actual scalar source projection checked in `flat_minimizer_source_gauge_research.md`. The one-form penalty is a fixed positive scalar `a`. All bounds are uniform when

\[
 0<a_-\le a\le a_+<\infty                         \tag{0.2}
\]

with fixed endpoints, and in odd refinement `M` and compatible periodic volume. In fact several inverse bounds only use the lower endpoint, but (0.2) is retained as a simple complete hypothesis. No claim about an unverified sequence of source penalties is hidden here.

The conclusion is exponential coarse-cell locality in physical fine-cell L2 operator norms, including all fine difference sandwiches of total order at most two. It concerns the explicitly matched homogeneous flat operator, not an arbitrary background or retained-history inverse.

## 1. Measures, source projection, and alias notation

Fine spacing is `eta=1/M`, with physical volume measure `eta^d`; unit coarse fields have counting measure. In a coarse Bloch fiber, fine aliases are `p_r=z+2pi r`, `r in I_M^d`, with

\[
 u_{r,\mu}^{\pm}=M(e^{\pm ip_{r,\mu}/M}-1),
 \quad P_r=\sum_\mu u_{r,\mu}^+u_{r,\mu}^-,
 \quad d_\mu^\pm=e^{\pm iz_\mu}-1,
 \quad b_\mu=d_\mu^+d_\mu^-.
\]

Write `a_r=a_M(p_r)` for the centered scalar averaging multiplier and `omega_{r,mu}` for the one-form multiplier, including its additional longitudinal string factor. A superscript minus means evaluation at the negative full fine momentum. Thus

\[
 \omega_{r,\mu}u_{r,\mu}^+=a_r d_\mu^+,
 \qquad
 \omega_{r,\mu}^-u_{r,\mu}^-=a_r^-d_\mu^-.
                                                               \tag{1.1}
\]

The analytic transpose agrees with the real Hilbert adjoint on real momenta but never complex-conjugates a complex momentum variable. Alias space has counting Hilbert measure; no power of `M` belongs in the covariance alias sums with these physical-volume conventions.

For the source scalar gauge, let `L=D^*D` and

\[
 G'=(L+Q_0^*a'Q_0)^{-1},\quad
 P_{\rm src}=G'Q_0^*(Q_0G'^2Q_0^*)^{-1}Q_0G',
 \quad R=I-P_{\rm src}.
                                                               \tag{1.2}
\]

The scalar penalty `a'` here is distinct from the one-form penalty `a` in (0.1). On real nonzero coarse fibers,

\[
 \ker R=\operatorname{ran}(L^{-1}Q_0^*),\qquad
 P_{\rm src}=L^{-1}Q_0^*W_2^{-1}Q_0L^{-1},
 \quad W_2=Q_0L^{-2}Q_0^*=\sum_r\frac{a_ra_r^-}{P_r^2}.
                                                               \tag{1.3}
\]

This is an orthogonal range projection, so its value does not depend on the scalar penalty `a'`. The scalar zero fiber is handled separately in Section 6, using (1.2), not an inverse of `L` on its constants.

## 2. The Feynman inverse with the one-form penalty

Let

\[
 G_F=\operatorname{diag}_r(P_r^{-1}I_d),\qquad
 W=QG_FQ^*=\operatorname{diag}_\mu(c_\mu),
\]
\[
 c_\mu=\frac{g_\mu}{P_0}+R_\mu,\qquad
 g_\mu=\omega_{0,\mu}\omega_{0,\mu}^-,\quad
 R_\mu=\sum_{r\ne0}\frac{\omega_{r,\mu}\omega_{r,\mu}^-}{P_r}.
                                                               \tag{2.1}
\]

All formulas in this section are initially in real nonzero fibers. The fine Hodge identity is `K+DD^*=L I_d`. Define

\[
 \mathcal B=L I_d+Q^*aQ,\qquad F=\mathcal B^{-1}.
\]

The ordinary positive Woodbury identity gives

\[
 F=G_F-G_FQ^*(a^{-1}I+W)^{-1}QG_F.                \tag{2.2}
\]

For the rest of the proof put

\[
 \widehat R_\mu=R_\mu+a^{-1},\qquad
 D^a_\mu=g_\mu+P_0\widehat R_\mu,\qquad
 k_\mu=(D^a_\mu)^{-1}.
                                                               \tag{2.3}
\]

Thus `(a^-1 I+W)^-1=P_0 diag(k_mu)`, and `F` is diagonal in the orientation index:

\[
 F_{r\mu,s\nu}
 =\delta_{\mu\nu}\left[
 \frac{\delta_{rs}}{P_r}
 -\frac{P_0\omega_{r,\mu}^-\omega_{s,\mu}}
              {P_rP_sD^a_\mu}\right].             \tag{2.4}
\]

Its canceled central and mixed blocks are

\[
 F_{0\mu,0\nu}=\delta_{\mu\nu}\widehat R_\mu/D^a_\mu,
\]
\[
 F_{0\mu,s\nu}
 =-\delta_{\mu\nu}\frac{\omega_{0,\mu}^-\omega_{s,\mu}}
                             {P_sD^a_\mu},\quad s\ne0,
\]
\[
 F_{r\mu,0\nu}
 =-\delta_{\mu\nu}\frac{\omega_{r,\mu}^-\omega_{0,\mu}}
                             {P_rD^a_\mu},\quad r\ne0.
                                                               \tag{2.5}
\]

For the high-high block use (2.4), whose denominators are then all high. These identities remove every central `P_0^-1` from `F`.

## 3. The source projection is a rank-one subtraction

By (1.3) and the fine Hodge identity,

\[
 \mathcal A_a=\mathcal B-vW_2^{-1}v^-,
 \qquad v_{r,\mu}=u_{r,\mu}^+a_r^-/P_r,
 \qquad v_{r,\mu}^-=a_r u_{r,\mu}^-/P_r.
                                                               \tag{3.1}
\]

Here `v^-` denotes the row at the negative argument with the correct alias/orientation transpose. In a real fiber it is `v^*`. The subtraction is essential: `R=I-P_src`, so `K+DRD^*=L I-DP_srcD^*`.

For each real nonzero coarse momentum, the fine operator in (0.1) is positive definite. One direct proof is to set each of its three nonnegative quadratic terms to zero. Zero Maxwell energy gives a fine gradient plus a constant harmonic one-form. The zero coarse average removes the harmonic part and makes the scalar block mean constant; subtract that scalar constant. The remaining scalar lies in `ker Q_0`, so its Laplacian lies in `ran R`. The zero source-gauge term then kills its Laplacian and hence its gradient. This also proves invertibility at the zero fiber with the harmonic constraint retained.

The subtractive Woodbury formula is therefore

\[
 G_0=F+Fv\,[W_2-v^-Fv]^{-1}v^-F.                 \tag{3.2}
\]

We evaluate its denominator exactly. The cochain identities (1.1) imply

\[
 v^-G_Fv=W_2,\qquad QG_Fv=W_2d^+,
 \qquad v^-G_FQ^*=W_2d^-.
                                                               \tag{3.3}
\]

For example the `mu` component of `QG_Fv` is
`sum_r omega_{r,mu} u_{r,mu}^+ a_r^-/P_r²`
`=d_mu^+ sum_r a_r a_r^-/P_r²`.

Let `A=a_0a_0^-`. The central identity from the Maxwell proof is

\[
 \sum_\mu\frac{b_\mu}{g_\mu}=P_0/A.
\]

Define

\[
 E_a=A^{-1}-\sum_\mu
       \frac{b_\mu\widehat R_\mu}{g_\mu D^a_\mu}.
                                                               \tag{3.4}
\]

Subtracting `1/D^a_mu−1/g_mu` gives the exact cancellation identity

\[
 \sum_\mu b_\mu k_\mu=P_0E_a.
                                                               \tag{3.5}
\]

Equations (2.2), (3.3), and (3.5) now give

\[
 \begin{split}
 W_2-v^-Fv
 &=W_2^2 d^-(a^{-1}I+W)^{-1}d^+\\
 &=W_2^2 P_0^2E_a.
 \end{split}                                                   \tag{3.6}
\]

With

\[
 R_{s,2}=\sum_{r\ne0}a_ra_r^-/P_r^2,\qquad
 D_{s,2}=A+P_0^2R_{s,2},\qquad W_2=D_{s,2}/P_0^2,
\]

this is `D_{s,2}² E_a/P_0²`. The powers in this denominator are fixed by (3.3); replacing `W_2²` by `W_2` would give a different operator.

## 4. Complete pole-canceled formula

Set `beta=(P_0/D_{s,2})Fv`. Expanding (2.2) yields, before canceling its central entry,

\[
 \beta_{r,\mu}
 =\frac{P_0u_{r,\mu}^+a_r^-}{P_r^2D_{s,2}}
    -\frac{\omega_{r,\mu}^-k_\mu d_\mu^+}{P_r}.
                                                               \tag{4.1}
\]

For `r!=0`, (4.1) is already holomorphic on the high-alias strip. At the central alias, use

\[
 \omega_{0,\mu}^-k_\mu d_\mu^+
       =(u_{0,\mu}^+/a_0)g_\mu k_\mu,
\]
\[
 A/D_{s,2}=1-P_0^2R_{s,2}/D_{s,2},\qquad
 g_\mu k_\mu=1-P_0\widehat R_\mu k_\mu.
\]

The apparent central pole cancels exactly:

\[
 \boxed{\quad
 \beta_{0,\mu}
 =\frac{u_{0,\mu}^+}{a_0}
       \left(\widehat R_\mu k_\mu
                      -\frac{P_0R_{s,2}}{D_{s,2}}\right).
 \quad}                                                       \tag{4.2}
\]

Let `beta^-` be its analytic transpose at the negative arguments, obtained from the same construction for `v^-F`. The final answer is

\[
 \boxed{\qquad G_0=F+\beta E_a^{-1}\beta^- .\qquad} \tag{4.3}
\]

Here `F` uses (2.5) for central blocks and (2.4) for high-high blocks, and `beta` uses (4.2) centrally and (4.1) elsewhere. No term has a central massless denominator. The entire complex cone `P_0=0` has been removed, not merely the real point zero. The signs of both the positive Woodbury update in (4.3) and the negative `P_0R_{s,2}/D_{s,2}` term in (4.2) are determined by the preceding algebra.

## 5. A uniform common holomorphic strip

Choose a fixed enlarged real cube `|x_mu|<=K` with `pi<K<2pi`. Let

\[
 c_K=\frac{\sin(K/2)}{K/2}>0,
 \qquad H_K=\frac{4(2\pi-K)^2}{\pi^2}.
\]

The previously proved alias bounds give, uniformly in `M`,

\[
 A(x)\ge c_K^{2d},\quad
 g_\mu(x)\ge g_*:=c_K^{2d+2},\quad
 0\le R_\mu(x)\le H_K^{-1},\quad
 0\le R_{s,2}(x)\le H_K^{-2},
\]
\[
 P_0(x)\le dK^2,\qquad g_\mu(x)\le1,\qquad A(x)\le1.
\]

Consequently

\[
 g_*\le D^a_\mu(x)\le
 D_*:=1+dK^2(H_K^{-1}+a_-^{-1}),
\]
\[
 c_K^{2d}\le D_{s,2}(x)\le1+d^2K^4H_K^{-2}.
                                                               \tag{5.1}
\]

For `x!=0`, equation (3.5) gives

\[
 E_a(x)=\frac{\sum_\mu b_\mu(x)/D^a_\mu(x)}{P_0(x)}
            \ge c_K^2/D_*.
                                                               \tag{5.2}
\]

Use `sum b_mu>=c_K²|x|²` and `P_0<=|x|²`. At zero, (3.4) gives `E_a(0)=1`, so the same lower bound holds.

On an initial fixed complex neighborhood, every high denominator has positive real part and in fact `|P_r(z)|>=c|r|²`. Alias Parseval bounds the sums of absolute paired scalar or one-form averaging factors independently of the number of aliases. Hence `R_mu`, `R_{s,2}`, and all central multipliers are uniformly holomorphic and bounded there. The fixed interval (0.2) makes the added `a^-1` uniformly harmless.

Use nested real cubes with positive margins and Cauchy estimates exactly as in the audited flat precision proof. First shrink to keep `A`, `g_mu`, `D^a_mu`, and `D_{s,2}` away from zero, using (5.1). Formula (3.4) is now holomorphic and uniformly bounded. Shrink once more to preserve the real lower bound (5.2). This gives a strip of positive width independent of `M,a` on which all denominators in (2.5), (4.1)–(4.3) are uniformly nonzero. The real fundamental cube remains in the interior of the enlarged chart. Also `a_0^-1` is uniformly bounded because `a_0a_0^-=A` is separated from zero and both factors are bounded.

This proof does not use real positivity alone to infer complex invertibility: the uniform holomorphic bounds and the two separate shrinking steps supply the quantitative conclusion.

## 6. The zero mode and the case M=1

At coarse momentum zero,

\[
 a_0=\omega_{0,\mu}=1,\qquad
 a_r=\omega_{r,\mu}=0\quad(r\ne0),
\]
\[
 R_\mu=R_{s,2}=0,\quad
 A=g_\mu=D^a_\mu=D_{s,2}=E_a=1,\quad \beta=0.
\]

The canceled formulas give

\[
 (G_0)_{0\mu,0\nu}=a^{-1}\delta_{\mu\nu},\qquad
 (G_0)_{r\mu,s\nu}=\delta_{rs}\delta_{\mu\nu}/P_r
       \quad(r,s\ne0),
                                                               \tag{6.1}
\]

with zero mixed blocks. This is exactly the operator definition: the source `R` vanishes on scalar constants and is the identity on high scalar aliases; `Q` reads only constant one-forms. Thus the central precision is `aI`, while the high precision is `P_r I`. No harmonic mode was inverted incorrectly.

For `M=1`, there is a single alias, `Q=I`, `R=0`, and

\[
 D^a=1+P_0/a,\quad k=a/(P_0+a),\quad E_a=a/(P_0+a),
\]
\[
 F=(P_0+a)^{-1}I,\qquad \beta=d^+/(P_0+a).
\]

Therefore

\[
 G_0=(P_0+a)^{-1}I+
                  \frac{d^+d^-}{a(P_0+a)},         \tag{6.2}
\]

which is the direct inverse of `(P_0+a)I-d^+d^-`. This verifies the sign, the penalty normalization, and the rank-one coefficient independently. Its zero value is again `a^-1 I`. In particular, a uniform positive lower bound for `a` cannot be omitted.

## 7. Uniform alias Hilbert bounds and two fine derivatives

On the common strip,

\[
 |P_r|\ge c|r|^2\ (r\ne0),\qquad
 |u_{r,\mu}^\pm|\le C(1+|r|),
\]
\[
 \sum_r|a_r^\pm|^2+
       \sum_{r,\mu}|\omega_{r,\mu}^\pm|^2\le C_d.
                                                               \tag{7.1}
\]

The high-high part of `F` is a diagonal operator `P_r^-1` plus, for each orientation, a rank-one term whose vectors are `omega_{r,mu}^-/P_r` and `omega_{r,mu}/P_r`. Its central row and column use the same high vectors. These have uniform alias L2 norms by (7.1). The central finite-dimensional block is bounded by (2.5). Thus `F` has a uniformly bounded alias operator norm.

For high aliases, (4.1) gives the useful bound

\[
 |\beta_{r,\mu}|
 \le C\left(\frac{|a_r^-|}{|r|^3}
                   +\frac{|\omega_{r,\mu}^-|}{|r|^2}\right).
                                                               \tag{7.2}
\]

The central beta is bounded by (4.2), so beta and its analytic transpose have uniform alias L2 norms. Equation (4.3) proves a uniform alias operator bound for `G_0`.

More generally, multiply the output by any product of `alpha` fine difference multipliers, and the input by any product of `beta` such multipliers, where

\[
 \alpha+\beta\le2.                               \tag{7.3}
\]

On the high diagonal of `F`, the growth is at most `C|r|^(alpha+beta-2)`, hence bounded. Each high rank vector becomes `omega_r/P_r` times at most two powers of `|r|`, so (7.1) still bounds its alias L2 norm. The central-to-high and high-to-central pieces are identical in this respect. For the Woodbury term, (7.2) shows that beta with up to two output derivatives is bounded by `C(|a_r^-|/|r|+|omega_r^-|)` in the worst case; again it is uniformly square summable. The analogous row bound holds at the negative arguments. Hence every derivative sandwich (7.3) is uniformly bounded and holomorphic as an alias Hilbert operator. Orientation tensors contribute only a fixed dimensional factor.

In particular this controls the fine gradient on either side, the mixed first-gradient sandwich, and the fine curl sandwich. This is an operator estimate in cell L2, not a uniform pointwise fine-derivative assertion.

## 8. Physical-cell reconstruction, periodic gluing, and inverse identification

Let `s in I_M^d` index the within-cell fine sites and use

\[
 F_M(z)_{sr}=e^{i(z+2\pi r)\cdot s/M}.
\]

For real `z`, this maps alias counting L2 unitarily into physical cell L2 with weight `M^-d`. For complex `z=x+iy`, it is the real unitary followed by `diag_s(e^-{y dot s/M})`. Thus it and its holomorphic inverse have uniformly bounded norms on the fixed strip. Tensor it with the orientation identity. The reconstructed two-sided operator is

\[
 (G_0)_{\rm cell}(z)=F_M(z)G_0(z)F_M(z)^{-1}.
                                                               \tag{8.1}
\]

It and all derivative sandwiches of Section 7 inherit the uniform strip bounds.

The complete real operator (0.1), not necessarily its individually separated central pieces, is periodic up to alias permutation under `z -> z+2pi n`. Reconstruction cancels that permutation: a wrapped alias contributes `exp(i2pi s_nu)=1`. Therefore (8.1) is periodic. Enlarged-chart holomorphic formulas agree on the real overlaps, hence glue by the identity theorem. Fourier contour shifting gives, for some constants `C,rho>0`,

\[
 \|(\mathscr D_\alpha G_0\mathscr D_\beta)(n,m)\|
       _{\text{physical cell }2\to\text{physical cell }2}
 \le C e^{-\rho|n-m|_1},\qquad \alpha+\beta\le2.
                                                               \tag{8.2}
\]

Here each `mathscr D` is a specified fine forward/backward difference composition, or a fixed curl/divergence combination of the corresponding total order. Summing at any smaller exponent gives uniform weighted cell-Schur norms. The within-cell dimension grows with `M`, but no dimension factor entered either the alias operator proof or the unitary reconstruction.

On the infinite homogeneous lattice, the bounded inverse symbol defines an inverse of the stated fine operator: fiberwise multiplication gives identity, including the separately checked zero sector; for each fixed `M` the fine precision is itself bounded, though its unweighted norm can grow with `M`. Thus the inverse is an actual fine Hilbert-space operator, not only a formal kernel. The real inverse bound also yields a refinement-uniform positive spectral gap for (0.1).

For a compatible finite periodic regulator, the source operators have the same Bloch fibers on its momentum grid. Sampling (8.1) therefore gives their exact inverse. Its kernel is the absolutely convergent periodization of (8.2), including short periods and oriented-cell multiplicities. The weighted cell-Schur norms are bounded by the infinite norms, using periodic distance. This is homogeneous periodic identification; it is not a Dirichlet or retained-history restriction theorem.

## 9. The coarse inverse and the normalized source extension

Let `H_src` be the exact normalized Maxwell minimizer in the matched source scalar gauge, already proved to satisfy

\[
 QH_{\rm src}=I,\qquad RH_{\rm src}^{\rm div}
       =RD^*H_{\rm src}=0,
 \qquad H_{\rm src}^*K H_{\rm src}=q_M.
\]

For any fixed coarse datum `B`, the first term in (0.1) has minimum `B^*q_MB`, the source gauge term is nonnegative and vanishes on `H_src B`, and the penalty term is the constant `a||B||²`. Hence

\[
 \inf_{QA=B}\langle A,\mathcal A_a A\rangle
      =\langle B,(q_M+aI)B\rangle.
\]

The ordinary constrained Gaussian inverse formula and strict positivity give

\[
 \boxed{\quad
 q_0:=(QG_0Q^*)^{-1}=q_M+aI,
 \qquad G_0Q^*q_0=H_{\rm src}.
 \quad}                                                       \tag{9.1}
\]

If the source uses `QH_0=ell^-1`, its normalized extension is `H_0 ell`; thus `H_0 ell=H_src`. The identity is in the fixed physical-volume conventions. It is not an identification with the rooted next-step `Q^flat` used later for pivot elimination.

## 10. Penalty-source status and immediate next connections

The fixed homogeneous convention in Raw I:13583–13593 writes the one-form penalty as `a=ell^-2`; at unit physical block scale it is `a=1`. A different local-generator passage, I:23879–23881, introduces a sequence `a_n`, states `a_0=a_1=a`, and refers to CMP99b (3.23)–(3.24) for its recursion without printing it. The present proof does not assert a formula for that sequence. An application using it must verify the fixed positive interval (0.2) after the exact measure/scale conversion. Its lower endpoint is required by (6.1).

Combined with the separately proved flat weighted bound for `Theta'_J`, (8.2) gives a natural route to the auxiliary current Neumann series on a fixed small L-infinity current ball. A complete statement must still specify the analytic carrier, coordinate and normalization match and distinguish `G_pi^J` from the additional `Theta_J` term in `G_1^J`.

There is also a useful next curvature connection. The constrained fine Green operator is

\[
 \widetilde G_0=G_0-H_{\rm src}q_0^{-1}H_{\rm src}^*.
\]

Its locality follows from (8.2), the local source extension, and the already gapped/local coarse inverse. Identifying `d tilde G_0 d^*` as the orthogonal projection onto `closure(d ker Q)` would close the projection-locality input in `flat_curvature_response_research.md`. That projection identity is flagged here as a next connection rather than used in the proof above.

The established result is the full matched homogeneous flat source inverse and its first/two-sided derivative locality. General nonflat backgrounds, mixed histories, arbitrary domains and the final interacting construction remain outside this note.
