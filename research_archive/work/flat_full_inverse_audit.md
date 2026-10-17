# Independent audit of the full flat gauge-fixed inverse

16 October 2026. Independent derivation and completed comparison with `flat_full_inverse_research.md`. The rank-one inverse formula, its exact central cancellations and the total-two-derivative physical-cell operator bounds are valid under the homogeneous flat assumptions below. The completed author's note passes the independent audit.

## 1. Precise operator and penalty scope

Let L=D^*D be the positive fine scalar Laplacian, K=d^*d the fine Maxwell precision, Q=Q_M^st the normalized straight one-form average and Q_0 the scalar average. Thus K=L I-DD^* and QD=d_cQ_0. Let R be the audited source orthogonal projection with ran R=L ker Q_0. The full flat fine precision is

    A_0=K+DRD^*+Q^*aQ,
    G_0=A_0^(-1).

Here a is a positive scalar homogeneous coarse penalty. For a scale-uniform statement it suffices to keep it fixed, or in a compact interval 0<a_-<=a<=a_+<infinity. In particular a lower bound cannot be omitted: the constant fine mode of G_0 at zero coarse momentum equals a^(-1)I. The source sequence of penalties and its normalization must be matched explicitly before invoking the uniform statement for that sequence.

All alias adjoints below are ordinary Hermitian adjoints on real momenta and their analytic bilinear continuations off the real torus. A minus superscript on an alias multiplier means evaluation at the negative physical alias momentum, not variable-dependent conjugation.

## 2. Rank-one reduction on nonzero fibers

For real nonzero coarse momentum, L is diagonal with positive eigenvalues P_r. The scalar source projection is

    I-R=L^(-1)Q_0^* W_2^(-1) Q_0 L^(-1),
    W_2=sum_r a_r a_r^-/P_r^2=D_s2/P_0^2.

Use a_r for the scalar alias average and a for the distinct coarse penalty. Put

    B=L I+Q^*aQ,
    v=L^(-1)D Q_0^*,
    v_(r,mu)=u_(r,mu)^+ a_r^-/P_r.

Then exactly

    A_0=B-v W_2^(-1)v^*.

This follows from K+DRD^*=L I-D(I-R)D^*. There is no commutation of G' and R in this step; only the already established homogeneous range formula for R is used.

## 3. The blocked Feynman inverse and its cancellation

Let F=B^(-1). It is diagonal in vector component. Introduce

    L_mu=R_mu+a^(-1),
    D_a,mu=g_mu+P_0 L_mu,
    k_mu=D_a,mu^(-1),
    E_a=A^(-1)-sum_mu b_mu L_mu/(g_mu D_a,mu).

As before A=a_0a_0^-, g_mu=omega_0,mu omega_0,mu^-, and R_mu is the high-alias vector covariance remainder. The exact identity is

    sum_mu b_mu k_mu=P_0 E_a.

For each component the ordinary Woodbury formula gives

    F_rs,mu=delta_rs/P_r
       -P_0 omega_r,mu^- omega_s,mu/(P_r P_s D_a,mu).

Its safe blockwise formulas are

    F_00,mu=L_mu k_mu,
    F_0s,mu=-omega_0,mu^- omega_s,mu k_mu/P_s,
    F_r0,mu=-omega_r,mu^- omega_0,mu k_mu/P_r,
    F_rs,mu=delta_rs/P_r
       -P_0 omega_r,mu^-omega_s,mu k_mu/(P_rP_s)
          for r,s nonzero.

All central P_0 denominators have canceled. These are holomorphic on the usual common strip after adding the positive denominator D_a.

## 4. The scalar Schur denominator and the beta vector

The cochain identity gives, componentwise,

    (Fv)_(r,mu)=u_(r,mu)^+ a_r^-/P_r^2
       -omega_r,mu^- d_mu^+ D_s2 k_mu/(P_r P_0).

Taking the analytic transpose product with v yields

    v^*Fv=W_2-D_s2^2 E_a/P_0^2,
    W_2-v^*Fv=D_s2^2 E_a/P_0^2.

For example, the first product sums to W_2 because sum_mu u_r,mu^-u_r,mu^+=P_r. The second uses u_r,mu^-omega_r,mu^-=a_r^-d_mu^- and then sum_mu b_mu k_mu=P_0E_a. These checks fix both the square of D_s2 and the power P_0^(-2).

Set beta=(P_0/D_s2)Fv. Its central cancellation is

    beta_(0,mu)=(u_(0,mu)^+/a_0)
       [L_mu k_mu-P_0 R_s2/D_s2],

and its high aliases are

    beta_(r,mu)=P_0 u_(r,mu)^+a_r^-/(P_r^2D_s2)
                -omega_r,mu^-k_mu d_mu^+/P_r.

The rank-one downdate inverse is therefore

    G_0=F+beta beta^-/E_a.

Here beta^- is the analytic row obtained from the negative-momentum alias vector; on real momenta it is beta^*. Its entries correspond to the alias -s at momentum -z. No conjugation of the complex argument is made. The resulting expression contains no central massless denominator.

## 5. Uniform real gaps and the zero sector

On an enlarged real cube |p_mu|<=K<2pi, the earlier high-alias gap and Parseval bounds give

    g_mu>=g_*>0,
    D_a,mu>=g_*,
    D_a,mu<=D_*:=1+dK^2(H_K^(-1)+a_-^(-1)).

With c_K=sin(K/2)/(K/2),

    E_a(p)=[sum_mu b_mu(p)/D_a,mu(p)]/P_0(p)
           >=c_K^2/D_*       for p nonzero,
    E_a(0)=1.

Also D_s2>=A>0. All relevant remainders and central functions are uniformly bounded on an initial complex tube. Successive Cauchy shrinkings first preserve D_a, D_s2, g_mu, A and then preserve E_a. This gives a common strip independent of M and of a in the stipulated interval. The old strip proof applies with R_mu replaced by R_mu+a^(-1); no new summation issue appears.

At zero momentum all high a_r and omega_r vanish. Beta is identically zero there. The formula gives a^(-1)I on the central bond modes and P_r^(-1)I on every high alias. Directly in the source operator, R is zero on the central scalar mode and identity on the high scalar modes. Thus K+DRD^* equals P_r I on high aliases and vanishes centrally, while Q^*aQ supplies aI centrally. The proposed zero-mode inverse is exactly correct. For M=1 the same formulas reduce to the inverse of the finite lattice Maxwell precision plus aI.

## 6. Operator bounds with at most two fine derivatives

For high aliases, |P_r|>=c(1+|r|)^2 and |u_r|<=C(1+|r|). The high diagonal of F is O(|r|^(-2)). The remaining blocks are bounded central blocks, rows/columns and rank-one terms with high vectors omega_r/P_r. Scalar and vector alias Parseval bound their Hilbert norms uniformly.

Put alpha output fine differences and beta input differences, where alpha,beta are nonnegative integers with alpha+beta<=2. The high diagonal becomes O(|r|^(alpha+beta-2)), hence is bounded. A high rank vector is bounded by C|omega_r||r|^(alpha-2), or the analogous input vector, and alpha,beta<=2. Its alias l2 norm is uniform. Central multipliers are bounded.

For the extra beta vector, a high derivative of order alpha<=2 is bounded by a sum of

    C|a_r^-||r|^(alpha-3)
       and C|omega_r^-||r|^(alpha-2).

Both have uniformly bounded alias l2 norms. The central beta formula and its finite fine-difference multipliers are uniformly bounded. Therefore the rank correction beta beta^-/E_a obeys the same sandwich estimate. This proves uniform holomorphic operator bounds for G_0 and every placement of at most two fine differences, including D G_0 D^*, L G_0 and G_0 L. The count is a cell-Hilbert operator statement; it is not a uniform pointwise bound on individual fine kernel entries.

## 7. Periodic reconstruction and coarse-cell locality

Reconstruct with the finite Fourier map F_M(z) on both sides, tensoring with the fixed vector-component space. It is unitary from alias counting measure to the physical fine-cell norm for real momentum. Its complex norm and inverse norm are uniformly bounded by the internal phase exp(-Im z.s/M). Thus the reconstructed symbols retain the uniform operator bounds without a growing-dimension factor.

On real overlapping charts, the original source inverse is coarse-periodic and its alias matrices transform by permutation. This also follows from the original B,v,W_2 formula away from the zero mode. Integer fine-site phases cancel the wrap on both sides. The canceled formulas agree on real overlaps and hence glue holomorphically. This applies to every fine-derivative sandwich too.

Contour shifting yields exponential decay of all these operator-valued coarse-cell kernels and uniform weighted Schur bounds, with constants independent of M. Finite compatible tori sample the same symbols; their kernels are exact periodizations and have uniform bounds in periodic coarse-cell distance, including short periods.

The computation proves a full flat fine inverse and its derivative locality, rather than merely the inverse of the already reduced coarse Maxwell form. Its source application still requires the stated homogeneous source Q, scalar R and penalty normalization. It does not cover nonflat independent-current families, holes or mixed histories by itself.

## 8. Comparison with the saved author's note

Read the completed author's Sections 1--10 in full. Every displayed cancellation agrees with the independent calculation above. In particular, the intermediate denominator is W_2^2 P_0^2 E_a=D_s2^2 E_a/P_0^2, not an expression linear in W_2; the beta central correction has the required negative P_0 R_s2/D_s2 term. The real-zero and M=1 calculations agree directly with the operator definition. The enlarged-chart argument, two Cauchy shrinkings, complex analytic transpose, growing alias dimension, physical cell reconstruction, periodic gluing, and finite-volume periodization all have the needed hypotheses.

The additional constrained minimization argument in Section 9 is correct: the Maxwell energy at fixed QA=B is minimized by H_src B, its source-gauge penalty vanishes, and the coarse penalty contributes a||B||^2. Thus q_0=q_M+aI and G_0Q^*q_0=H_src. This gives the exact zero-current extension needed by the auxiliary-current analysis, with the previously stated homogeneous normalization and source-Q convention.

I independently checked deposited Raw I:13583--13593. Its homogeneous Green-function definition sets the bond penalty a=ell^(-2); at unit physical block scale a=1. The distinct scalar penalty a' in G' must not be conflated with it. The author's Section 10 correctly isolates the different, unprinted a_n recursion instead of asserting uniformity for that sequence without proof. The source identification remains to the deposited transcription; no new claim of recovery of the original published argument is made here.

**Audit status: pass and ready for integration within the explicit homogeneous flat, compatible periodic, physical-cell L2 scope.** No correction to the saved mathematical argument was found. These estimates do not assert pointwise fine kernels, arbitrary backgrounds, mixed retained histories, Dirichlet restriction identities, or a Yang--Mills construction.
