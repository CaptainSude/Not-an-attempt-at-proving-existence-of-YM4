# Ultraviolet limit of the homogeneous flat Gaussian baseline

16 October 2026. This note proves the ultraviolet limit of the homogeneous flat Maxwell quotient and, under the already identified fixed-step coordinate formula, its reduced Gaussian covariance. The independently audited common-strip theorem in `flat_covariance_decay_research.md` and `flat_covariance_decay_audit.md` is an input. All estimates below are uniform in odd refinement factor `M`, including aliases whose size is comparable to `M`. The result concerns the free flat baseline, not an interacting ultraviolet limit or a nonflat retained-history covariance.

Independent audit by `theorem_audit` passed: alias wrapping and complex denominator bounds, the uniform comparison rectangle, the rate and tail constants, the inherited nonzero denominators, weighted Schur inversion and exact small-torus periodization were checked without correction.

## 1. Statement and conventions

Fix dimension `d`, an odd next-step block size `L`, and a number `pi<K<2pi`. The original fine spacing is `1/M`, with odd `M` tending to infinity; in the renormalization sequence, `M=L^k`. Coarse physical spacing is one. Put

\[
 I_M=\{-(M-1)/2,\ldots,(M-1)/2\}^{d},\qquad
 p_r(z)=z+2\pi r,
\]
\[
 s_M(w)=\frac{\sin(w/2)}{M\sin(w/(2M))},\qquad
 s(w)=\frac{\sin(w/2)}{w/2},\quad s(0)=1.
                                                        \tag{1.1}
\]

The ratio defining `s_M` has its removable values when necessary. On the complex boxes used below, its denominator can vanish only at `w=0`, where the removable value is one. Define

\[
 P_{M,r}(z)=4M^2\sum_\nu\sin^2\frac{p_{r,\nu}(z)}{2M},
 \qquad P_{\infty,r}(z)=\sum_\nu p_{r,\nu}(z)^2,
                                                        \tag{1.2}
\]
\[
 N_{M,r,\mu}(z)=s_M(p_{r,\mu}(z))^2
                    \prod_\nu s_M(p_{r,\nu}(z))^2,
\]
\[
 N_{\infty,r,\mu}(z)=s(p_{r,\mu}(z))^2
                    \prod_\nu s(p_{r,\nu}(z))^2.
                                                        \tag{1.3}
\]

The averaging multiplier itself has the longitudinal phase
`exp(i(M-1)p_mu/(2M))`, which converges to `exp(i p_mu/2)`. The analytic covariance numerator is the multiplier at `p` times the multiplier at `-p`; these phases cancel, giving (1.3). No complex modulus occurs in (1.2)--(1.3), and no factor `M^-d` belongs in the alias covariance sum with physical-volume Fourier normalization.

Let `q_M` be the Maxwell quotient symbol already derived from the averaged Feynman covariance. There exist `rho_*>0` and constants independent of `M` such that, on a smaller common periodic complex strip,

\[
 \sup_{|\operatorname{Im}z_\nu|\le\rho_*}
       |q_M(z)-q_\infty(z)|\le C M^{-2}.             \tag{1.4}
\]

Here `q_infinity` is given explicitly in Section 4. Consequently, for some fixed positive `kappa`,

\[
 \|q_M-q_\infty\|_\kappa\le C_\kappa M^{-2}          \tag{1.5}
\]

in exponentially weighted Schur norm. The same estimate holds uniformly over compatible periodic volumes. With the fixed source coordinate maps `K_L,T_L`, define

\[
 A_M=K_L^*(q_M+T_L^*T_L)K_L,
 \qquad C_M=A_M^{-1}.
                                                        \tag{1.6}
\]

The established uniform real gap and locality imply, at a possibly smaller fixed `kappa>0`,

\[
 \|A_M-A_\infty\|_\kappa+
 \|C_M-C_\infty\|_\kappa\le C_{d,L,\kappa}M^{-2}.
                                                        \tag{1.7}
\]

The proof follows. The rate is a convenience, not an assumed source estimate.

## 2. Uniform high-alias denominators and summable weights

Work first on

\[
 \mathcal B_{K,\rho}=
 \{z=x+iy:|x_\nu|\le K,\ |y_\nu|\le\rho\},
\]

where `rho<=1` will be fixed independently of `M`. Set

\[
 a=2\pi-K>0,\qquad c_0=4a^2/\pi^2.
\]

For a nonzero component `r_nu` in the retained alias range, the distance of `x_nu+2pi r_nu` to `2pi M Z` is at least `a|r_nu|`. To see this for `r_nu>=1`, both possible nearest distances obey

\[
 2\pi r_\nu-K\ge a r_\nu,
\]
\[
 2\pi(M-r_\nu)-K\ge2\pi(r_\nu+1)-K\ge a r_\nu;
\]

negative indices follow by symmetry. Since the principal distance is at most `pi M`, the elementary sine lower bound gives

\[
 P_{M,r}(x)\ge c_0 |r|_2^2,\qquad r\ne0.
                                                        \tag{2.1}
\]

The complex correction satisfies

\[
 \operatorname{Re}P_{M,r}(x+iy)
 \ge P_{M,r}(x)-e^\rho\sum_\nu y_\nu^2.
\]

Choose `rho>0` such that `d e^rho rho^2<=c0/2`. Then

\[
 |P_{M,r}(z)|\ge\operatorname{Re}P_{M,r}(z)
                 \ge(c_0/2)|r|_2^2\quad(r\ne0).
                                                        \tag{2.2}
\]

For every integer alias, not only the retained ones,

\[
 \operatorname{Re}P_{\infty,r}(z)
 =\sum_\nu(x_\nu+2\pi r_\nu)^2-\sum_\nu y_\nu^2
 \ge(c_0/2)|r|_2^2\quad(r\ne0).                     \tag{2.3}
\]

Indeed each nonzero-index component has real magnitude at least `a|r_nu|`, and `a^2>=c0`.

There is a constant `C_s=C_s(K,rho)` such that

\[
 |s(p_{r,\nu}(z))|\le\frac{C_s}{1+|r_\nu|}
                                                        \tag{2.4}
\]

for all aliases. For `r_nu=0`, the integral representation of `s` bounds it by `exp(rho/2)`. For a nonzero index use `|sin((z_nu+2pi r_nu)/2)|=|sin(z_nu/2)|<=cosh(rho/2)` and `|z_nu+2pi r_nu|>=a|r_nu|`.

For retained aliases, the same bound holds for `s_M`, with a different fixed constant. One direct proof combines the preceding sine numerator bound with

\[
 |M\sin(p_{r,\nu}(z)/(2M))|
 \ge |M\sin((x_\nu+2\pi r_\nu)/(2M))|
 \ge (a/\pi)|r_\nu|.
\]

The zero-index bound follows from the centered finite exponential average. This proof already handles `|r_nu|` comparable to `M`; no expansion in `r/M` has been assumed.

Write

\[
 W_{r,\mu}=(1+|r_\mu|)^{-2}
                      \prod_\nu(1+|r_\nu|)^{-2}.
\]

Equations (2.2)--(2.4) imply

\[
 \left|\frac{N_{M,r,\mu}}{P_{M,r}}\right|
 +\left|\frac{N_{\infty,r,\mu}}{P_{\infty,r}}\right|
 \le C\frac{W_{r,\mu}}{|r|_2^2},\qquad r\ne0,       \tag{2.5}
\]

where the first term is considered only for retained aliases. The right side is summable over `Z^d\{0}`. More explicitly, with

\[
 B=\sum_{m\in\mathbb Z}(1+|m|)^{-2}=\pi^2/3-1,
\]

the tail satisfies

\[
 \sum_{|r|_\infty>N}\frac{W_{r,\mu}}{|r|_2^2}
 \le\frac{2d B^{d-1}}{(N+1)^3}.                    \tag{2.6}
\]

For the proof discard the extra orientation factor, use `|r|_2>=N+1`, and sum over the union of the `d` coordinate tails; `sum_{|m|>N}(1+|m|)^-2<=2/(N+1)`.

## 3. Quantitative convergence of the alias remainder

Define

\[
 R_{M,\mu}(z)=\sum_{r\in I_M\setminus\{0\}}
                    \frac{N_{M,r,\mu}(z)}{P_{M,r}(z)},
\quad
 R_{\infty,\mu}(z)=\sum_{r\in\mathbb Z^d\setminus\{0\}}
                    \frac{N_{\infty,r,\mu}(z)}{P_{\infty,r}(z)}.
                                                        \tag{3.1}
\]

The second sum is normally convergent on the interior of the box by (2.5), hence holomorphic there and continuous uniformly on the closed box. Fixed-alias convergence and domination already prove `R_M→R_infinity` uniformly. The following uniform comparison proves the rate.

Let `f(w)=w/sin w`, with `f(0)=1`. For every retained alias with `M>=3`,

\[
 \left|\operatorname{Re}\frac{p_{r,\nu}}{2M}\right|
 \le\frac\pi2+\frac{K-\pi}{6}<\frac{2\pi}3,
 \qquad
 \left|\operatorname{Im}\frac{p_{r,\nu}}{2M}\right|
 \le\frac16.
                                                        \tag{3.2}
\]

The fixed rectangle on the right contains no nonremovable zero of `sin`. Therefore `f` is bounded there, and `(f(w)-1)/w^2` is bounded there after filling its removable value at zero. In particular

\[
 s_M(p)=s(p)f(p/(2M)),\quad
 |f(p/(2M))-1|\le C|p|^2/M^2.                       \tag{3.3}
\]

All constants in this section depend on `d,K,rho`, but not on `M,r,z`. For `r!=0`,

\[
 \sum_\nu|p_{r,\nu}(z)|^2\le C|r|_2^2.
\]

Telescoping the fixed number `2d+2` of factors in (1.3), using the bound on `f` and (2.4), yields

\[
 |N_{M,r,\mu}-N_{\infty,r,\mu}|
          \le\frac{C}{M^2}|r|_2^2 W_{r,\mu}.         \tag{3.4}
\]

Likewise, the analytic function

\[
 \frac{(\sin w/w)^2-1}{w^2}
\]

is bounded on the same rectangle after its removable value at zero is filled. Consequently

\[
 |P_{M,r}-P_{\infty,r}|
       \le\frac{C}{M^2}\sum_\nu|p_{r,\nu}|^4
       \le\frac{C}{M^2}|r|_2^4.                    \tag{3.5}
\]

Combining (2.2)--(2.3) with (3.4)--(3.5) gives the key retained-alias estimate

\[
 \left|\frac{N_{M,r,\mu}}{P_{M,r}}
       -\frac{N_{\infty,r,\mu}}{P_{\infty,r}}\right|
          \le\frac{C}{M^2}W_{r,\mu}.               \tag{3.6}
\]

For clarity, the numerator-difference term uses (3.4) divided by `(c0/2)|r|^2`. The reciprocal-denominator difference is bounded by `CM^-2`, because its numerator in (3.5) grows as `|r|^4` and the product of the two denominator lower bounds grows as `|r|^4`; multiplying by `|N_infinity|<=CW` gives the other term. Thus the estimate remains valid near the edge of the fine Brillouin zone, although its pointwise numerator comparison need not be small there.

Sum (3.6), using `sum_r W_{r,mu}<=B^d`, and bound the missing aliases with (2.6), taking `N=(M-1)/2`. This proves

\[
 \boxed{\quad
 \sup_{z\in\mathcal B_{K,\rho}}
 |R_{M,\mu}(z)-R_{\infty,\mu}(z)|\le C M^{-2}.
 \quad}                                               \tag{3.7}
\]

The omitted continuum tail is actually `O(M^-3)`. The retained discretization error is what gives the displayed `M^-2` rate. The exceptional case `M=1` has no high aliases and is irrelevant to the limiting assertion; it can be included in a bound valid for all positive odd `M` by enlarging its constant.

## 4. Explicit limiting Maxwell precision and removable axes

Put

\[
 P(z)=\sum_\nu z_\nu^2,\qquad
 A(z)=\prod_\nu s(z_\nu)^2,
 \qquad g_\mu(z)=A(z)s(z_\mu)^2,
\]
\[
 d_\mu(z)=e^{iz_\mu}-1,\quad d_\mu^-(z)=e^{-iz_\mu}-1,
 \quad b_\mu=d_\mu d_\mu^-,
\]
\[
 D_\mu(z)=g_\mu(z)+P(z)R_{\infty,\mu}(z),
 \qquad h_\mu(z)=D_\mu(z)^{-1},
\]
\[
 E(z)=A(z)^{-1}-\sum_\mu
        \frac{b_\mu(z)R_{\infty,\mu}(z)}{g_\mu(z)D_\mu(z)}.
                                                        \tag{4.1}
\]

Then the explicit limiting symbol is

\[
 \boxed{\quad
 q_\infty(z)=P(z)\operatorname{diag}(h_\mu(z))
  -\frac{[\operatorname{diag}(h_\mu(z))d(z)]
          [d^-(z)\operatorname{diag}(h_\mu(z))]}{E(z)}.
 \quad}                                               \tag{4.2}
\]

On real nonzero momenta this is equivalently the Maxwell quotient of the continuum alias Feynman covariance

\[
 c_{\infty,\mu}(x)=
 \sum_{r\in\mathbb Z^d}
 \frac{s(x_\mu+2\pi r_\mu)^2
             \prod_\nu s(x_\nu+2\pi r_\nu)^2}
      {\sum_\nu(x_\nu+2\pi r_\nu)^2},
                                                        \tag{4.3}
\]

namely `diag(c)^-1-(diag(c)^-1 d)(d^-diag(c)^-1)/(d^-diag(c)^-1d)`. Formula (4.3) is not used at `x=0`, where its principal Feynman term is singular. Formula (4.2) is the canceled expression that remains meaningful there and on the complex null cone `P(z)=0`.

To justify nonvanishing and convergence without circularity, use the common-strip theorem already proved for finite `M`. Choose a closed smaller box inside its open holomorphic domain, still containing the real fundamental cube in its interior. On this box finite-`M` quantities `g_M,D_M,E_M` have positive modulus lower bounds independent of `M`. Equation (3.7) and (3.3) at the principal alias give

\[
 P_{M,0}\to P,\quad A_M^{\rm symbol}\to A,\quad
 g_{M,\mu}\to g_\mu,\quad D_{M,\mu}\to D_\mu,
 \quad E_M\to E
                                                        \tag{4.4}
\]

uniformly, all with error `O(M^-2)`. Here `A_M^{symbol}` is the principal scalar averaging weight, not the retained-coordinate precision (1.6). The denominator lower bounds pass to the limits. The rational canceled formula is Lipschitz on this bounded domain separated from its denominators' zeros, proving (1.4).

Every apparent one-variable zero at `z_nu+2pi r_nu=0` is filled by the entire sinc function. If `z_nu=0` and `r_nu!=0`, the corresponding sinc factor is zero, so that alias term vanishes; the total high-alias denominator remains nonzero by (2.3). Thus coordinate axes create no singularity or exceptional summation rule. At `z=0`, every high numerator vanishes, so `R_infinity,mu(0)=0`; moreover `A(0)=g_mu(0)=D_mu(0)=E(0)=1` and `P(0)=d(0)=0`. Hence

\[
 q_\infty(0)=0.
\]

The principal scalar identity `sum_mu b_mu/g_mu=P/A` follows by canceling the one-variable sinc factors with their removable values. It is exactly the limit of the finite-`M` cochain identity. It explains the removal of the whole complex null cone, not merely the point zero.

Although the separated central and high-alias terms need not be periodic individually, the finite-`M` canceled quotient is a periodic holomorphic symbol. Uniform convergence on its common periodic tube therefore makes (4.2) periodic too. Equivalently, on real momenta one can reindex the absolutely convergent full sum (4.3); holomorphic gluing then follows from the identity theorem.

## 5. Exponentially weighted kernel convergence

Let `rho_*>0` be a closed strip width on which the common periodic symbols and (1.4) are bounded. Choose `0<kappa<rho_0<rho_*`. Shifting each Fourier contour by `-rho_0 sign(x_nu)` or the opposite sign according to the Fourier-transform convention gives

\[
 |(q_M-q_\infty)(x)|
                 \le C M^{-2}e^{-\rho_0|x|_1}.
                                                        \tag{5.1}
\]

The precise sign of the shift is immaterial to the bound; it is chosen so that the Fourier exponential decays. The symbols are finite-dimensional matrices in orientation and color, so any entrywise-to-operator norm factor is fixed. Therefore

\[
 \|q_M-q_\infty\|_\kappa
 \le\frac{C}{M^2}
    \left(\frac{1+e^{-(\rho_0-\kappa)}}
               {1-e^{-(\rho_0-\kappa)}}\right)^d.
                                                        \tag{5.2}
\]

This proves (1.5), including a uniform rate. The argument also proves weighted convergence of any fixed finite number of lattice derivatives or other bounded local matrix compositions; none are needed for (1.7).

## 6. Actual retained-coordinate precision and covariance

Work first on the infinite homogeneous lattice, with the fixed `L`-periodic retained-bond convention. The source reconstruction and finite-range bounds are those of `flat_covariance_source_research.md`. Since the gauge term does not depend on `M`,

\[
 A_M-A_\infty=K_L^*(q_M-q_\infty)K_L,
\qquad
 \|A_M-A_\infty\|_\kappa
 \le\|K_L\|_\kappa^2\|q_M-q_\infty\|_\kappa.
                                                        \tag{6.1}
\]

The already established `A_M>=gamma I`, with `gamma>0` independent of `M`, passes to the operator-norm limit. Thus `A_infinity>=gamma I`. The uniform exponentially weighted Schur bounds and this gap yield uniform Combes--Thomas estimates for `C_M=A_M^-1` and `C_infinity=A_infinity^-1`. At a fixed smaller weight exponent,

\[
 \sup_M\|C_M\|_\kappa+\|C_\infty\|_\kappa\le C_\kappa.
                                                        \tag{6.2}
\]

To obtain a Schur bound from a pointwise Combes--Thomas bound, choose `kappa` strictly below its exponential decay exponent and sum the remaining exponential over the lattice. The bounded number of retained coordinates per fixed `L` cell introduces only a fixed constant.

The resolvent identity now gives

\[
 C_M-C_\infty=C_M(A_\infty-A_M)C_\infty,
\]
\[
 \|C_M-C_\infty\|_\kappa
 \le\|C_M\|_\kappa\|A_M-A_\infty\|_\kappa
                         \|C_\infty\|_\kappa
 \le C_{d,L,\kappa}M^{-2}.                           \tag{6.3}
\]

Weighted Schur matrices form an algebra by the triangle inequality for the coordinate distance, so these products require no extra summability or limit interchange. For `M=L^k`, the error is `O(L^-2k)`.

## 7. Exact periodic regulators and volume-uniform convergence

For the unit-translation-invariant `q_M`, the actual finite periodic Fourier multiplier is the restriction of the same symbol to the torus momentum grid. Its kernel is therefore the absolutely convergent periodization of the infinite kernel. The same holds for the limit. If `Gamma` is the physical period lattice, then

\[
 (q_M^\Gamma-q_\infty^\Gamma)(x,y)
 =\sum_{\gamma\in\Gamma}(q_M-q_\infty)(x-y+\gamma).
                                                        \tag{7.1}
\]

Since periodic distance is no greater than the distance to any chosen image, the periodic weighted Schur norm of (7.1) is bounded by the infinite weighted Schur norm in (5.2), independently of the volume.

For the actual retained operators require compatibility with the next-step blocks, namely periods in `L Z^d` and the same periodic pivot convention. Grouping coordinates into fixed `L` cells makes `K_L,T_L,A_M,C_M` translation invariant with finite-dimensional cell fibers. Their exponentially summable kernels can be periodized. Periodization commutes with multiplication of such periodic block kernels: expand both absolutely convergent sums, then group the intermediate point into one fundamental domain and its images. Therefore periodizing `A_M C_M=I=C_M A_M` proves

\[
 C_M^\Gamma=(A_M^\Gamma)^{-1},
                                                        \tag{7.2}
\]

where `C_M^Gamma` is the periodized infinite covariance and `A_M^Gamma` is exactly the operator formed from the finite periodic source matrices. Uniqueness of the inverse gives the equality; no separate infinite-volume selection or boundary state is needed. Absolute convergence also handles small tori and coincident geometric incidences, provided the source convention counts periodic images with their proper multiplicities.

It follows that (6.1)--(6.3) hold uniformly over all these compatible periodic volumes. If the shortest nonzero period tends to infinity, the uniform decay also allows the thermodynamic limit at fixed `M` or after `M→infinity`, and the two limits commute for fixed finite-coordinate covariance entries. Merely increasing volume while retaining a bounded periodic direction would instead give a cylindrical limit. This statement uses exact homogeneous periodization; it is not a claim that an arbitrary Dirichlet or retained-history effective operator is a compression or periodization of the homogeneous one.

## 8. Scope and next interface

The theorem supplies a canonical homogeneous ultraviolet limit of the flat reduced Gaussian baseline, with exponentially weighted kernel convergence. It improves a family of uniform flat estimates to an actual convergent family. When the already stated finite-level minimizer/source identification applies, these are precisely the order-zero source Gaussian covariances in the fixed retained integration coordinates.

It does not prove an interacting Yang--Mills continuum limit, a covariance limit at arbitrary nonflat background, a uniform free-current derivative theorem, or a retained-history boundary identification. In particular, the independent-current analytic response estimates needed to compare the actual precision to this baseline remain separate. No choice of a gauge-dependent moving cutoff domain is made here.
