# Scalar source-gauge locality and the quadratic current response

16 October 2026. This note proves uniform coarse-cell locality of the flat scalar operator `Z=G'RG'` and uses it in the exact free-current second derivative established in `flat_free_current_response_research.md`. It also records the derivative bounds sufficient for the flat `Theta'_J` perturbation. All source identifications are those of `flat_minimizer_source_gauge_research.md`; no nonflat or whole independent-current neighborhood theorem is inferred.

## 1. The constrained biharmonic inverse

Use the flat scalar Laplacian `L=D^*D`, scalar block average `Q_0`, and real source operators

\[
 G'=(L+Q_0^*a'Q_0)^{-1},\quad
 R=I-G'Q_0^*(Q_0G'^2Q_0^*)^{-1}Q_0G',\quad Z=G'RG'.
                                                               \tag{1.1}
\]

Then

\[
 Z=G'^2-G'^2Q_0^*(Q_0G'^2Q_0^*)^{-1}Q_0G'^2,
 \qquad Q_0Z=0=ZQ_0^*.
                                                               \tag{1.2}
\]

This is the inverse of the quadratic form `||L lambda||²` restricted to `ker Q_0`, extended by zero on the orthogonal complement. Indeed the standard constrained Gaussian inverse formula applied to `(G')^-2` gives (1.2). For `lambda in ker Q_0`,

\[
 \|(G')^{-1}\lambda\|^2
 =\|(L+Q_0^*a'Q_0)\lambda\|^2=\|L\lambda\|^2.
\]

Therefore the restricted forms coincide. In particular, `Z` is independent of the auxiliary penalty `a'` once the constraint and measures are fixed. Equivalently, `Z L² lambda=lambda` for `lambda in ker Q_0`. The scalar constant null mode of `L` is not in `ker Q_0`, so no inverse is assigned to that mode.

In a nonzero coarse Bloch sector, `L` is diagonal with eigenvalues `P_r`; the scalar averaging row is `(a_r)_r`. Hence

\[
 Z_{rs}(z)=\frac{\delta_{rs}}{P_r(z)^2}
 -\frac{a_r^-(z)a_s(z)}{P_r(z)^2P_s(z)^2 W_2(z)},
 \qquad W_2=\sum_r\frac{a_ra_r^-}{P_r^2}.
                                                               \tag{1.3}
\]

As before, `a_r=a_M(z+2pi r)`, `a_r^-=a_M(-z-2pi r)`, and all stars have become the specified analytic bilinear transpose. Formula (1.3) is first proved on real nonzero fibers; its canceled form below defines the continuation.

## 2. Cancel the entire central pole

Let

\[
 A=a_0a_0^-,\qquad
 R_{s,2}=\sum_{r\ne0}\frac{a_ra_r^-}{P_r^2},\qquad
 D_{s,2}=A+P_0^2R_{s,2}.
                                                               \tag{2.1}
\]

The same alias Parseval and high-denominator estimates used for the source-gauge extension give a common complex strip on which `R_{s,2}` and `D_{s,2}` are bounded and `D_{s,2}` is bounded away from zero. This also follows directly: the high remainder is holomorphic and uniformly bounded; on the enlarged real cube `D_{s,2}>=A>=c>0`; a fixed Cauchy shrinking preserves the lower bound. The central factors are uniformly bounded. All constants are independent of odd `M`.

Since `W_2=D_{s,2}/P_0²`, formula (1.3) cancels to

\[
 Z_{00}=R_{s,2}/D_{s,2},
\]
\[
 Z_{0s}=-\frac{a_0^-a_s}{P_s^2D_{s,2}}\quad(s\ne0),
 \qquad
 Z_{r0}=-\frac{a_r^-a_0}{P_r^2D_{s,2}}\quad(r\ne0),
\]
\[
 Z_{rs}=\frac{\delta_{rs}}{P_r^2}
  -\frac{P_0^2a_r^-a_s}{P_r^2P_s^2D_{s,2}}\quad(r,s\ne0).
                                                               \tag{2.2}
\]

There is no central denominator remaining, including on the complex null cone of `P_0`. At zero coarse momentum all high `a_r` vanish. The formula becomes zero on the central scalar mode and the diagonal inverse `P_r^-2` on the nonzero aliases, precisely the inverse on `ker Q_0` from Section 1. At `M=1`, `Q_0=I`, and `Z=0`; (2.2) has the same interpretation.

## 3. Dimension-independent alias operator bounds

On the fixed smaller enlarged strip,

\[
 |P_r|\ge c|r|_2^2\quad(r\ne0),\qquad
 \sum_r|a_r|^2+\sum_r|a_r^-|^2\le C.
                                                               \tag{3.1}
\]

The first bound includes aliases at the fine-zone edge. Write the high-high block of (2.2) as a diagonal operator plus a rank-one operator. Its diagonal norm is bounded by `sup_{r!=0}|P_r|^-2<=C`. Each high rank vector `(a_r^-/P_r²)` or `(a_r/P_r²)` has uniformly bounded alias `ell²` norm by (3.1). The central-to-high and high-to-central rows/columns have the same bounds. Thus

\[
 \sup_z\|Z(z)\|_{\ell^2(I_M^d)\to\ell^2(I_M^d)}\le C,
                                                               \tag{3.2}
\]

uniformly in `M`. For a complex bilinear rank-one matrix `v w^T`, its Hilbert operator norm is bounded by `||v||_2||w||_2`; complex conjugation of the analytic symbol is not needed.

There is a useful derivative strengthening. A product of `alpha` fine difference multipliers on the output and `beta` on the input obeys the same operator bound whenever

\[
 \alpha+\beta\le4.                               \tag{3.3}
\]

Indeed `|u_{r,nu}^±|<=C(1+|r|)` and the central multipliers are bounded. The high diagonal becomes bounded by `C|r|^{alpha+beta-4}`. The high rank vectors are bounded componentwise by `C|a_r^-||r|^{alpha-4}` and `C|a_r||r|^{beta-4}`, so (3.1) bounds their `ell²` norms. The central row and column are treated in exactly the same way. Laplacian factors count as two differences because `P_r=sum u_r^+u_r^-`. The number of orientation components is fixed in `d`.

All these multiplied symbols remain holomorphic. This proves, in particular, uniform strip bounds for `Z`, `LZ`, `ZL`, `DZL`, and the operators

\[
 \Lambda=ZLD^*=G'RD^*,\qquad D\Lambda.
                                                               \tag{3.4}
\]

For the equality in (3.4), use `LG'R=R` and transpose it to get `RG'L=R`; therefore `ZL=G'RG'L=G'R`. The total derivative counts are three for `Lambda` and four for `D Lambda`. Here `D Lambda` is the fine gradient of the scalar output, not a derivative with respect to background or current.

## 4. Reconstruction gives genuine spatial locality

For within-cell fine sites `s in I_M^d`, let

\[
 F_M(z)_{sr}=\exp(i(z+2\pi r)\cdot s/M).
\]

For real `z`, this is unitary from alias counting `ell²` into the physical cell norm `M^-d sum_s |v_s|²`. For complex `z=x+iy`,

\[
 F_M(x+iy)=\operatorname{diag}_s(e^{-y\cdot s/M})F_M(x),
\]

so both its norm and its inverse norm are bounded independently of `M`. Its inverse is the fixed finite Fourier inverse followed by `diag(e^{-iz dot s/M})`, hence it too is holomorphic. The reconstructed two-sided scalar symbol is

\[
 Z_{\rm cell}(z)=F_M(z)Z(z)F_M(z)^{-1}.
                                                               \tag{4.1}
\]

The same reconstruction applies to the derivative operators, with their fixed orientation fibers. Equations (3.2)–(3.4) therefore give dimension-independent holomorphic operator bounds on physical cell Hilbert spaces.

On real momenta a shift by `2pi` permutes aliases modulo `M`. The reconstruction cancels this permutation on both sides; wrapping adds `exp(i2pi s_nu)=1` on fine lattice sites. Hence (4.1) is periodic. The holomorphic enlarged-chart versions agree on real overlaps and glue by the identity theorem. Fourier contour shifting yields, for some fixed `rho>0`,

\[
 \|Z_M(n-m)\|_{\text{cell }2\to\text{cell }2}
 \le C e^{-\rho|n-m|_1},                          \tag{4.2}
\]

and the same statement for the derivative operators in (3.3). For every fixed `0<kappa<rho`, their exponentially weighted coarse-cell Schur norms are uniformly bounded. The growing within-cell dimension does not enter these estimates because (3.2) and the reconstruction bounds are operator-norm bounds.

Compatible periodic operators are exact periodizations of these kernels, by finite Fourier sampling. Their weighted estimates are uniform in the periods and use periodic distance, including short periods and the correct multiplicities. The algebraic identities may also be read fiberwise on those regulators, with the scalar zero sector as specified after (2.2).

## 5. Local current vertices in cell Hilbert norms

At flatness the BCH mixed term is

\[
 c^{(1)}(A,\lambda)(b)
   =\frac i2[\lambda(b_-)+\lambda(b_+),A(b)].
\]

The current vertex `mathfrak j_J` is its transpose pairing with `J`. It is a finite-incidence operator from fine bonds to fine sites and contains no negative power of the fine spacing. If the fixed Lie bracket norm obeys `|[X,Y]|<=c_br|X||Y|`, a conservative estimate is

\[
 \|\mathfrak j_J\|_{2\to2}
 \le C_d c_{\rm br}\|J\|_\infty.                  \tag{5.1}
\]

For example, sum the at most `2d` incident-bond contributions at a site using Cauchy–Schwarz and then sum with fine volume weight; each bond is counted at most twice. The source and target weights are the same fine physical volume. The estimate is independent of `M`.

In coarse-cell coordinates its matrix has a fixed finite range, so it has the same type of weighted Schur bound. More precisely, if `J_x` is supported on bonds with basepoint in cell `x`, the input of `mathfrak j_{J_x}` reads that cell only, and its output lies in the fixed neighboring-cell set `N(x)`. All restricted block operator norms obey (5.1); no pointwise-to-Hilbert factor growing with the number of fine sites is needed.

The transpose vertex `mathfrak k_J` has the same bounds. Polarization of `c^(2)` expresses `mathfrak m_J` in form sense as a sum of fixed-incidence coefficient maps of size `C||J||_infinity` composed with one fine derivative on either leg. The derivative is on the scalar leg, not on `J`: this is the decomposition into `m_3+D^*m_4` transcribed at Raw I:13717–13718 and expanded at I:13811–13821.

Together with the weighted bounds for `Lambda,D Lambda`, this proves

\[
 \|\Theta'_J\|_{\kappa,\,\text{cell }2\to\text{cell }2}
 \le C_\kappa\|J\|_\infty.                       \tag{5.2}
\]

For precision, the `Lambda^* m_J Lambda` term is rewritten as a sum of products of `Lambda`, `D Lambda`, and those bounded finite-range coefficient maps, using the adjoint to move the derivative on the other leg. The weighted Schur algebra then proves (5.2). No derivative or regularity assumption on `J` appears. This is a flat perturbation bound, not yet a convergence theorem for the current Neumann series: the latter would additionally require a compatible uniform bound for the full fine `G_0` and a suitably fixed analytic carrier.

## 6. The exact second current derivative has localized source legs

Let `E_0=H_0 ell` be the normalized flat source minimizer, already identified with the source-gauge extension. Its cell-L2 kernel has a uniform exponential bound by `flat_minimizer_locality_research.md`, Section 10. The previously proved identity is

\[
 D^2q_0[J_1,J_2]
 =-(\mathfrak j_{J_1}E_0)^*Z(\mathfrak j_{J_2}E_0)
  -(\mathfrak j_{J_2}E_0)^*Z(\mathfrak j_{J_1}E_0).
                                                               \tag{6.1}
\]

All factors now have uniform weighted cell-Schur bounds, so

\[
 \|D^2q_0[J_1,J_2]\|_\kappa
 \le C_\kappa\|J_1\|_\infty\|J_2\|_\infty.        \tag{6.2}
\]

For currents supported in individual cells `x,y`, the stronger explicit kernel bound is

\[
 \begin{split}
 \|D^2q_0[J_x,J_y](b,c)\|
 \le C\|J_x\|_\infty\|J_y\|_\infty\big[&
 e^{-\rho(|b-x|_1+|x-y|_1+|y-c|_1)}\\
 &+e^{-\rho(|b-y|_1+|x-y|_1+|x-c|_1)}\big].
 \end{split}                                                   \tag{6.3}
\]

Here `b,c` label coarse input/output cells (with their fixed orientation/color fibers). The neighboring-cell offsets from the local vertices are absorbed into `C` and, if necessary, a smaller fixed `rho`. To prove (6.3), restrict the two `E_0` legs to cells `x,y`; the two vertex outputs range only over `N(x),N(y)`, whose sizes are fixed. Apply the corresponding `Z` block bound and sum that finite set. This gives the first exponential path; interchange the sources for the second.

For `0<kappa<rho`, summing (6.3) against the output/input weight also gives

\[
 \|D^2q_0[J_x,J_y]\|_\kappa
 \le C_\kappa\|J_x\|_\infty\|J_y\|_\infty
                  e^{-(\rho-\kappa)|x-y|_1}.        \tag{6.4}
\]

The proof uses `|b-c|<=|b-x|+|x-y|+|y-c|`, then sums the remaining exponential in `c` and takes the supremum in `b`, and likewise for columns. The same estimates hold in periodic distance on compatible finite tori.

These are source-locality bounds for one exact auxiliary current Hessian. The full `G_1^J` includes the additional nonlinear-constraint term `Theta_J`; its first derivative is not canceled by (6.1). Nonflat background responses, a whole uniform current neighborhood, and the final physical cutoff-coefficient match remain separate.
