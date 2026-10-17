# Independent audit of scalar source-gauge locality

16 October 2026. Audited `flat_scalar_gauge_locality_research.md`, Sections 1--4 and 6, together with the algebraic input in `flat_free_current_response_research.md`, Sections 3--5. **These statements pass.** The only correction reported was a missing backslash before the spacing command in the high-high Z display. The locality claims here are physical cell-Hilbert operator bounds; they are not pointwise bounds on fine kernel entries.

## 1. The exact constrained inverse

With L=D^*D, G'=(L+Q_0^*a'Q_0)^(-1) and the source orthogonal projection R,

    Z=G'RG'=G'^2-G'^2Q_0^*(Q_0G'^2Q_0^*)^(-1)Q_0G'^2.

This is the standard inverse of the quadratic form with precision G'^(-2) restricted to N=ker Q_0. For lambda in N, G'^(-1)lambda=Llambda. Polarization therefore identifies the restricted form with ||Llambda||^2. Thus Z is the constrained biharmonic inverse, independent of the auxiliary penalty. In particular Q_0Z=0 and ZL^2lambda=lambda for lambda in N. The scalar constant mode is excluded by the constraint and is never inverted as a Laplacian zero mode.

In a nonzero coarse fiber this gives

    Z_rs=delta_rs/P_r^2-a_r^-a_s/(P_r^2P_s^2 W_2),
    W_2=D_s2/P_0^2.

The displayed central cancellation is correct in every block:

    Z_00=R_s2/D_s2,
    Z_0s=-a_0^-a_s/(P_s^2D_s2),
    Z_r0=-a_r^-a_0/(P_r^2D_s2),
    Z_rs=delta_rs/P_r^2-P_0^2a_r^-a_s/(P_r^2P_s^2D_s2)
             for r,s nonzero.

At zero coarse momentum the high a_r vanish, so Z is zero on the central mode and equals P_r^(-2) on the high modes. For M=1 it vanishes. These are precisely the constrained inverse values. The cancellation removes the complex null cone, not merely the real zero.

## 2. Uniform operator bounds and derivative counting

On the common strip, the high diagonal is bounded by C|r|^(-4). The two rank vectors a_r^-/P_r^2 and a_r/P_r^2 have uniformly bounded alias l2 norms by scalar Parseval and the high denominator gap. The central row and column obey the same bounds. Therefore the operator norm is uniform in the growing alias dimension.

For an output derivative order alpha and input order beta, with nonnegative integers alpha+beta<=4, the high diagonal is O(|r|^(alpha+beta-4)). The rank vectors are bounded by C|a_r^-||r|^(alpha-4) and C|a_r||r|^(beta-4). Each exponent is nonpositive, so the same l2 estimates apply. The central multipliers are uniformly bounded. This proves the claimed sandwich bound for every indicated derivative placement, including Laplacians counted as two differences.

The identities LG'R=R and its adjoint RG'L=R give

    ZL=G'R,
    Lambda=ZLD^*=G'RD^*.

Thus Lambda has total derivative count three and D Lambda count four. Their use is within the proved bound. No commutation of G' and R was used or assumed.

## 3. Reconstruction and periodic locality

The reconstruction F_M(z) is unitary for real momentum between alias counting measure and the fine-cell physical norm M^(-d) sum_s |v_s|^2. For complex momentum its diagonal exponential and inverse are uniformly bounded because s/M stays in a fixed physical cell. Both are holomorphic, so

    Z_cell(z)=F_M(z) Z(z) F_M(z)^(-1)

is a uniformly bounded holomorphic cell operator. There is no output-dimension factor. The same argument covers all derivative sandwiches.

Alias permutation under a coarse-period shift is canceled on both sides by reconstruction. The wrapped phases are exp(2pi i s_nu)=1 for the integer fine offsets. Enlarged momentum charts therefore glue holomorphically. Fourier contour shifts give exponentially decaying coarse-cell operator kernels and uniform weighted Schur bounds. Finite periodic sampling gives exact periodizations, including short periods. This proves cell-L2 operator locality, not a uniform bound on each unweighted fine matrix entry.

## 4. Algebraic second-current response

The separate current note keeps the auxiliary carrier and its full physical extension distinct. For the auxiliary carrier, Theta'_j E_0=Lambda^* j_j E_0 and Lambda E_0=0 imply

    Dq_0[j]=0.

If lambda=Zf, then Q_0lambda=0 and Llambda=RG'f. Hence the source bond precision satisfies Delta_a Dlambda=Lambda^*f, so

    G_0 Lambda^*=D Z,
    dot E[j]=D Z j_j E_0.

Also Lambda D Z=Z. Differentiating Dq_J[j]=-E_J^*Theta'_jE_J and using that identity yields exactly

    D^2q_0[j_1,j_2]
       =-(j_j1 E_0)^*Z(j_j2 E_0)
        -(j_j2 E_0)^*Z(j_j1 E_0).

The sign, lack of an extra factor, normalization E_0=H_0 ell and use of Z rather than a commuting replacement all check. For a repeated real direction the result is negative semidefinite. This is an auxiliary-current Hessian and does not cancel the extra nonlinear-constraint current term in the full physical carrier.

## 5. Localized source legs and weighted sums

Given the stated finite-incidence cell bound for j_J and the already audited E_0 kernel, restricting a current to cell x places the vertex input in x and its output in a fixed neighboring set. Inserting the Z block kernel between the two vertices proves the two paths

    exp[-rho(|b-x|+|x-y|+|y-c|)]

and its source-interchanged counterpart, with a uniform constant absorbing the finitely many neighboring offsets. Every factor uses the physical fine-cell Hilbert norm, so no fine-site count is lost.

For a weighted Schur exponent kappa<rho, the triangle inequality spends kappa against the three path segments. Summing the remaining c tail and taking the supremum over b gives a constant times exp[-(rho-kappa)|x-y|]; the column estimate is identical. The stated global weighted norm bound follows alternatively from the weighted Schur algebra. The periodic version uses the same triangle inequality and uniform exponential sums in periodic distance.

The note's local-vertex/source assertions are explicit inputs to this final estimate. The audit verifies the propagation of those bounds, the exact algebraic current formula, and all scalar locality steps. It does not promote a whole complex current neighborhood, nonflat background response, pointwise fine-derivative estimate or full cutoff-coefficient identification.
