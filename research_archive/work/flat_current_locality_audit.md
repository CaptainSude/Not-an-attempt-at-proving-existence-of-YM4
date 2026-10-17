# Independent audit: flat auxiliary current response and scalar gauge locality

16 October 2026. Reviewed in full: `flat_free_current_response_research.md` and `flat_scalar_gauge_locality_research.md`. Also checked the defining deposited formulas at Raw I:13690–13740, I:13767–13780, I:13811–13821, and the scalar projector formulas at I:23906–23946. The flat averaging and source-gauge identification is the internally checked identification used in Notebook 08; the original CMP articles have not been reverified here.

**Result:** no mathematical correction is required for the stated flat auxiliary-current conclusions. The exact first and second derivatives, the uniform physical-cell Hilbert bounds through four fine derivatives of `Z`, the periodic gluing, and the weighted bound on `Theta'_J` without a derivative of `J` all pass. This is an internal audit, not an independent certification of the source account or of a Yang–Mills construction. The two notes correctly exclude nonflat backgrounds, the additional `Theta_J` term in `G_1^J`, and a uniform analytic current neighborhood.

## 1. Finite-regulator algebra and the exact current derivatives

All adjoints in this section use the stated physical lattice measures at the real flat reference. Complexification uses the resulting bilinear transpose, not a newly parameter-dependent Hermitian adjoint.

Set `G=G'`, `Z=GRG`, and use

\[
 Q_0GR=0,\qquad LGR=R,\qquad RG L=R.
\]

The last identity is the transpose of the second; it does not require `G` and `R` to commute. Therefore

\[
 Q_0Z=0,\quad LZ=RG,\quad ZL=GR,\quad
 \Lambda=ZLD^*=GRD^*.
\]

For `lambda=Zf`, the full flat penalized precision obeys

\[
 \Delta_aD\lambda
 =(K+DRD^*+Q^*aQ)D\lambda
 =DRL\lambda=DRGf=\Lambda^*f,
\]

because `KD=0`, `QD=d_cQ_0`, and `Q_0lambda=0`. Thus

\[
 G_0\Lambda^*=DZ,\qquad QDZ=0,
 \qquad \widetilde G_0\Lambda^*=DZ.
\]

The source gauge gives `Lambda E_0=0`. Consequently

\[
 \Theta'_jE_0=\Lambda^*\mathfrak j_jE_0,
 \qquad E_0^*\Theta'_jE_0=0,
\]

and exact differentiation of the finite inverses yields

\[
 Dq_0[j]=0,\qquad
 DE_0[j]=DZ\mathfrak j_jE_0.
\]

Moreover `Lambda DZ=Z`, so a second differentiation gives precisely

\[
 D^2q_0[j_1,j_2]
 =-(\mathfrak j_{j_1}E_0)^*Z(\mathfrak j_{j_2}E_0)
  -(\mathfrak j_{j_2}E_0)^*Z(\mathfrak j_{j_1}E_0).
\]

In a repeated real direction the factor is `-2`, and the result is negative semidefinite. No factor of two is missing. The first extension derivative is a fine gradient, has zero coarse average and zero curl, and need not satisfy the original source gauge. Indeed

\[
 RD^*DE_0[j]=RG\mathfrak j_jE_0
\]

need not vanish.

One normalization distinction should remain explicit when these formulas are consolidated: `q_0=(QG_0Q^*)^{-1}` includes the coarse averaging penalty. With the displayed physical normalization,

\[
 q_0=q_M+a
\]

at zero current, where `q_M` is the unpenalized constrained Maxwell precision of the earlier Fourier notes. The normalized minimizing extension is the same, because the penalty is constant on each affine constraint fiber. The penalty is independent of current and does not alter any of the derivative formulas above. The rightmost source factor in `H^J=E_J ell^{-1}` is also retained correctly.

The full family contains `Pi^*Theta_J Pi`. Since `Pi E_0=E_0`, its first coarse-precision derivative retains

\[
 -E_0^*\Theta_j^{[1]}E_0.
\]

The notes correctly avoid applying the auxiliary cancellation to this remaining term.

## 2. The constrained biharmonic inverse and central cancellation

The identity

\[
 Z=G^2-G^2Q_0^*(Q_0G^2Q_0^*)^{-1}Q_0G^2
\]

is the constrained inverse of `G^{-2}` on `ker Q_0`. On that subspace,

\[
 \langle\lambda,G^{-2}\lambda\rangle
 =\|G^{-1}\lambda\|^2=\|L\lambda\|^2.
\]

Thus it is exactly the constrained biharmonic inverse and is independent of `a'`. Its range lies in `ker Q_0` and it annihilates `ran Q_0^*`; this justifies “extended by zero on the orthogonal complement.” In particular `ZL^2lambda=lambda` for `lambda` in `ker Q_0`.

For a real nonzero Bloch sector the usual constrained-inverse formula is

\[
 Z_{rs}=\frac{\delta_{rs}}{P_r^2}
 -\frac{a_r^-a_s}{P_r^2P_s^2W_2},\qquad
 W_2=\frac{A}{P_0^2}+R_{s,2}.
\]

Putting `D_{s,2}=A+P_0^2R_{s,2}` gives

\[
 Z_{00}=\frac{R_{s,2}}{D_{s,2}},\quad
 Z_{0s}=-\frac{a_0^-a_s}{P_s^2D_{s,2}},\quad
 Z_{r0}=-\frac{a_r^-a_0}{P_r^2D_{s,2}},
\]

\[
 Z_{rs}=\frac{\delta_{rs}}{P_r^2}
 -\frac{P_0^2a_r^-a_s}{P_r^2P_s^2D_{s,2}}
 \quad(r,s\ne0).
\]

Every central denominator cancels. This includes the complex null cone of `P_0`, not merely the real origin. At zero coarse momentum the high averaging coefficients vanish, leaving zero on the central scalar mode and `P_r^{-2}` on the high aliases. For `M=1`, the constraint is the identity and `Z=0`. Both exceptional cases are consistent with the constrained form.

## 3. Four-derivative sandwiches do not lose fine-cell dimension

Fix the common enlarged complex chart and smaller strip already established for the flat source extension. There

\[
 |P_r|\ge c|r|^2\ (r\ne0),\qquad
 \sum_r|a_r|^2+\sum_r|a_r^-|^2\le C,
\]

and `D_{s,2}` is bounded away from zero uniformly in odd `M`. Central fine differences are bounded; high fine difference multipliers satisfy `|u_{r,nu}^{\pm}|<=C(1+|r|)`. These are the physical differences containing the factor `eta^{-1}=M`.

Let `U_alpha` and `V_beta` be products of respectively `alpha` output and `beta` input fine difference multipliers. For `alpha+beta<=4`:

* The high diagonal of `U_alpha Z V_beta` is bounded by `C|r|^{alpha+beta-4}`.
* Its high rank-one vectors are bounded by `C|a_r^-||r|^{alpha-4}` and `C|a_r||r|^{beta-4}`. Since each order is at most four, their alias `ell^2` norms are bounded by the preceding Parseval estimate.
* The central-to-high row and high-to-central column use the same vectors. The central entry and its differences are uniformly bounded.

For a complex rank-one matrix `vw^T`, `||vw^T||<=||v||_2||w||_2`; analytic transposition does not invalidate the estimate. This proves the claimed holomorphic Hilbert operator bounds, with no count of aliases. Fixed sums or orientation components only change a constant depending on `d`.

Laplacians count as two differences. Thus `Lambda=ZLD^*` has total order three, and `D Lambda` has order four. Both satisfy the claimed uniform strip bounds. This argument proves Hilbert bounds, not arbitrary fine-site supremum bounds for four derivatives.

## 4. Physical-cell reconstruction, periodicity and finite tori

For fine sites `s` in a centered cell, the reconstruction matrix

\[
 F_M(z)_{sr}=e^{i(z+2\pi r)\cdot s/M}
\]

is unitary from alias counting `ell^2` to the physical norm `M^{-d}\sum_s|v_s|^2` on real fibers. Its inverse therefore contains the finite-Fourier normalization `M^{-d}`. That factor must not be replaced by an unweighted matrix transpose.

For complex `z`, multiplication by `exp(-Im(z) dot s/M)` and its inverse have uniformly bounded norms because `|s_nu/M|<1/2`. Both reconstruction maps are holomorphic on the chart. Hence `F_M Z F_M^{-1}`, and every differentiated sandwich above, has the same kind of uniform operator bound in the physical cell spaces. Bond orientations only add a fixed finite factor.

On a real overlap, shifting a coarse momentum by `2pi` permutes fine aliases modulo `M`. The wrapped phase is `exp(i2pi s_nu)=1`; it cancels in the reconstructed operator. The reconstructed matrices, unlike an isolated central/high split, are periodic. Agreement on an open real overlap determines the holomorphic continuation, so the enlarged charts glue. Operator-valued Fourier contour shifting now gives a coarse-cell exponential kernel bound directly in operator norm. Taking this norm before the Fourier integral introduces no dimension factor.

Finite periodic operators are obtained by exact Fourier sampling, hence exact periodization of those kernels. Weighted Schur estimates descend uniformly using periodic distance and the sum over all lifted images. This remains valid for short periods: coincident lifted contributions must be added with their multiplicities. The zero-sector interpretation in Section 2 is compatible with that sampling.

## 5. Explicit factorization of the current form without differentiating J

The source formulas give

\[
 c^{(1)}(A,\lambda)(b)
 =\frac i2[\lambda(b_-)+\lambda(b_+),A(b)],
\]

and

\[
 2c^{(2)}(\lambda_1,\lambda_2)(b)
 =\frac1{2i}\big([\lambda_1(b_-),D\lambda_2(b)]
                 +[\lambda_2(b_-),D\lambda_1(b)]\big).
\]

Define the finite-incidence map `V_J` from bonds to sites by

\[
 \langle\lambda,V_J A\rangle
 =\frac1{2i}\langle[\lambda(b_-),A(b)],J(b)\rangle.
\]

Then, in form sense,

\[
 \mathfrak m_J=V_JD+D^*V_J^*.
\]

Both `V_J` and `mathfrak j_J` have physical fine-Hilbert operator norm at most `C_d c_br ||J||_infinity`. Site and bond sums have the same fine volume weight. Each site has at most `2d` incident bonds and each bond has two endpoints; the incidence estimate therefore has no power of `M`. Their cell kernels have fixed finite range and the same uniform weighted Schur bound.

Consequently the exact form factorization is

\[
 \Theta'_J
 =\mathfrak j_J^*\Lambda+\Lambda^*\mathfrak j_J
  +\Lambda^*V_JD\Lambda+(D\Lambda)^*V_J^*\Lambda.
\]

All four terms are products of operators already bounded in the weighted cell-Schur algebra. Therefore

\[
 \|\Theta'_J\|_\kappa\le C_\kappa\|J\|_\infty.
\]

The derivative always acts on a scalar leg through `D Lambda`. No derivative of the current has been taken, even when `J` jumps across a cell boundary. At complex current, use the fixed bilinear transpose; the norm estimates still hold with absolute values. This proves the claimed flat bounded perturbation, but does not alone prove a uniform Neumann neighborhood for the whole fine inverse.

## 6. Two localized current legs

The two `E_0` factors have the uniform exponential cell-Hilbert kernels proved in Notebook 08. If `J_x` is supported on bonds based in coarse cell `x`, then `mathfrak j_{J_x}` reads only that cell and has output in a fixed neighboring-cell set. Applying the `Z` block estimate between the two such sets gives

\[
 \begin{aligned}
 \|D^2q_0[J_x,J_y](b,c)\|
 \le C\|J_x\|_\infty\|J_y\|_\infty\big[&
 e^{-\rho(|b-x|+|x-y|+|y-c|)}\\
 &+e^{-\rho(|b-y|+|x-y|+|x-c|)}\big].
 \end{aligned}
\]

The neighbor offsets are bounded independently of `M`, so their finite sum changes only the constant. For `0<kappa<rho`, the triangle inequality bounds the kernel weight by the same three-leg path. Summation and the row/column suprema yield

\[
 \|D^2q_0[J_x,J_y]\|_\kappa
 \le C_\kappa\|J_x\|_\infty\|J_y\|_\infty
       e^{-(\rho-\kappa)|x-y|}.
\]

This proof has no hidden sum over all intermediate cells: the local vertices restrict that sum to fixed neighboring-cell sets. The same reasoning applies with periodic distance after exact periodization.

## 7. Minor editorial corrections and scope

1. The high-high display in scalar note (2.2) has literal `quad`; it should be `\quad`.
2. The scalar note's first citation for the `m_3+D^*m_4` decomposition should be Raw I:13717–13718, not I:13711–13713. Its detailed citation I:13811–13821 is correct.
3. The free-current note's source warning is at Raw I:13774, not I:13773.
4. At consolidation, distinguish the penalized `q_0=q_M+a` from unpenalized Maxwell `q_M`, even though their current derivatives agree for a fixed penalty.

No stronger claim follows merely from these checks. The result concerns fixed flat background, homogeneous full periodic/infinite geometry, the matched corrected source average and scalar source projector, and the auxiliary `Theta'_J` family. It does not cover retained multiscale boundaries, nonflat background derivatives, the separate constraint-curvature term, or the complete interacting source theorem.
