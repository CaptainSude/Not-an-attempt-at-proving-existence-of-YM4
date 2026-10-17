# A direct flat Maxwell gap for the one-step fluctuation space

Research note, 16 October 2026. The repository and output notebooks were not modified. The averaging contraction and the local Poincare inequality below are proved directly. Their match to the actual effective Hessian is stated precisely for the whole-lattice, full-block small-field minimizer at the trivial background. No claim is made here about general large-field histories, the complex free-current family, or the missing upper/locality estimates for the full precision.

## 1. Result

The flat gauge bridge can obtain its axial lower bound directly, without importing the full primary axial covariance proof. The ingredients are:

1. The linearized straight-string average is a contraction on curvature when the lattice-spacing factors are retained.
2. The actual contour-based average differs from it by a coarse gradient, so it has the same curvature identity.
3. On a fixed L-block tree-axial slice with zero next-scale straight-string average, curl controls the entire bond field by a constant depending only on d,L.

Consequently the flat effective Wilson Hessian obeys a scale-independent axial lower bound. Combining it with the explicit averaged-contour gauge bridge in `exponential_gauge_bridge_research.md` gives a positive lower bound for the actual flat exponential-gauge quadratic form, conditional only on the stated Hessian identification and averaging convention. The direct proof is given below, including a finite matrix whose smallest eigenvalue supplies the constant.

## 2. Normalized cochain identity

Let the fine lattice spacing be h and the coarse spacing H=Mh, with M odd. The lattice may be infinite or periodic. B_M(y) is the centered M-block of fine sites around a coarse site y, with M^d sites. Fine potentials A_mu(x) are physical gauge-potential coordinates, so the bond group element is exp(i h A_mu(x)). Define the lattice curl by

    (d_h A)_{mu nu}(x)
      = [A_nu(x+h e_mu)-A_nu(x)
         -A_mu(x+h e_nu)+A_mu(x)]/h,       mu<nu.

The straight-string average is

    (Q_M^st A)_mu(y)
      = M^(-d-1) sum_{x in B_M(y)} sum_{r=0}^{M-1}
                         A_mu(x+r h e_mu).                   (2.1)

This is normalized as a physical coarse potential, not as an unscaled line integral. Define the two-form average

    (Q_M^(2) F)_{mu nu}(y)
      = M^(-d-2) sum_{x in B_M(y)} sum_{r,s=0}^{M-1}
                         F_{mu nu}(x+r h e_mu+s h e_nu).      (2.2)

Then the exact identity is

    d_H Q_M^st = Q_M^(2) d_h.                               (2.3)

Proof. Expand the four coarse-potential terms around one H-plaquette and use the bijection B_M(y+H e_mu)=B_M(y)+H e_mu. The four string sums form the oriented boundary of the M by M fine-plaquette square with starting point x. Discrete Stokes writes its line sum as h times the sum of d_h A over those M^2 plaquettes. The coarse curl contributes a factor 1/H=1/(Mh), leaving M^(-d-2), exactly as in (2.2). This proves (2.3), with orientations fixed by the displayed curl formula.

The factor 1/h in d_h is essential. Using unscaled plaquette sums for d_h would introduce an extra power of M and invalidate the claimed contraction.

## 3. Exact weighted L2 contraction

Use the physical volume norms

    ||F||_h^2=h^d sum_x sum_{mu<nu}|F_{mu nu}(x)|^2,
    ||G||_H^2=H^d sum_y sum_{mu<nu}|G_{mu nu}(y)|^2.

Each row of Q_M^(2) has nonnegative coefficients summing to one: there are M^d M^2 terms. Its total column weight is M^(-d). Indeed, for a fixed fine plaquette position z and each ordered pair r,s, the base point x=z-rh e_mu-sh e_nu lies in exactly one block. Thus there are exactly M^2 preimages, counted with multiplicity on a torus. Jensen's inequality and H^d M^(-d)=h^d give

    ||Q_M^(2)F||_H^2 <= ||F||_h^2.                       (3.1)

The same argument with M strings instead of M^2 surface elements proves the corresponding one-form contraction for Q_M^st. No Fourier transform, positivity assumption on F, or nonwrapping hypothesis is needed; periodic multiplicities give the same counting identity.

## 4. Match to the actual contour-based average

Let T_h A(y,x) be the physical rooted path integral, namely h times the average of the oriented sums of A along the prescribed paths from y to x. Write aT_h A(y)=M^(-d) sum_{x in B_M(y)}T_h A(y,x). Linearizing the actual contour-based group average at the trivial configuration gives

    Q_M^flat A = Q_M^st A - D_H aT_h A,                 (4.1)

where D_H is the coarse scalar gradient divided by H. This is the spacing-restored version of the flat identity proved in the gauge-bridge note. It follows by expanding the two endpoint contours, the translated straight string, and the final reference coarse transporter; the reference term cancels exactly.

Since d_H D_H=0,

    d_H Q_M^flat A = Q_M^(2) d_h A.                    (4.2)

This uses only the first derivative of the group average at the identity. For the symmetric group average of CMP109, that derivative is the arithmetic contour average; see [CMP109](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf), (0.8), (0.11), (0.12), pp.253--254. Equation (4.1) also matches the explicitly distinguished Q^flat and Q_1 conventions in raw II, lines 9045--9285.

For a k-level composition, apply (4.2) successively. Each two-form average is an L2 contraction in its appropriate volume norm. Therefore, if Q_k is the actual derivative of the composed group average from spacing eta=L^(-k) to spacing one,

    ||d_1 Q_k A||_1 <= ||d_eta A||_eta.                (4.3)

For this rooted contour-based average, no potential-level equality with Q_(L^k)^st is used. Possible gauge-gradient differences at intermediate levels are harmless because curl kills them. If a different multilevel averaging definition is used, one must check its first derivative or its stepwise decomposition before applying (4.3).

### 4.1 Distinguish the corrected operator in Notebook03

The operator called Q_M in Notebook03 comes from the corrected one-step operation displayed in raw I, lines 24355--24375, rather than directly from the rooted Q^flat of CMP109. At the trivial background its parallel transports are identities and each of the four correction brackets vanishes. Its flat derivative is Q_M^st exactly.

Straight-string averages do have the exact potential-level semigroup law. If Q_M^st maps spacing h to Mh and Q_N^st maps spacing Mh to NMh, then

    Q_N^st Q_M^st = Q_(NM)^st.                         (4.4)

Proof: a centered NM-block is uniquely the union of centered M-blocks around the sites of the centered N-block of the intermediate lattice. Write its base point as a_M+M a_N in fine lattice units. Independently, a longitudinal string index is uniquely r_M+M r_N, with 0<=r_M<M and 0<=r_N<N. These two bijections turn the iterated sums into the single sum, and their coefficients multiply to (MN)^(-d-1). The two-form averages have the analogous semigroup law with two independent string indices.

Thus the corrected flat operator and the rooted flat operator both satisfy the needed curvature contraction, but they are not the same one-form constraint. Which one parametrizes the actual effective minimizer must be identified from its definition or from its stated gauge correction. Merely calling both operators Q would not be a valid source match.

### 4.2 Gauge adjustment between the two flat constraints

For completeness, their gradient difference can also be propagated through a hierarchy. Q_M^st maps a fine gradient D_h lambda to D_H of the scalar block average of lambda, while Q_M^flat maps it to D_H of lambda restricted to block centers. Using (4.1) and these identities inductively gives

    Q_k^rooted A = Q_(L^k)^st A + D_1 Psi_k(A)          (4.5)

for a linear scalar map Psi_k. No norm bound on Psi_k is asserted here. If Q_(L^k)^st A=B, extend the prescribed coarse-center values -Psi_k(A) to any fine site function lambda. Nested center restriction gives

    Q_k^rooted D_eta lambda = -D_1 Psi_k(A).

Consequently A+D_eta lambda satisfies the rooted constraint B and has exactly the same curl energy. Conversely, scalar block averaging has an elementary right inverse (blockwise constant functions), so a gradient adjustment also corrects a rooted-feasible lift to a straight-feasible one without changing its curl. Hence the quadratic energy infima for the two constraints agree, whenever both full-block flat operators are indeed the source operators being compared. This is an equality of energy infima, not an estimate on the gauge-adjusted potential, its analytic radius, or its cutoff coordinates.

## 5. Flat Wilson Hessian and effective minimization

For the Wilson action with physical normalization

    S_eta(U)=eta^(d-4) sum_p [1-Re tr U(partial p)],

write U_b(t)=exp(i eta t A_b). At the trivial field, the first derivative is zero. The first plaquette phase is i t eta^2(d_eta A)_p, and its second trace coefficient gives

    D^2 S_eta(1)[A,A] = eta^d sum_p |(d_eta A)_p|^2
                     = ||d_eta A||_eta^2.              (5.1)

The norm is the invariant Lie-algebra norm induced by the normalized trace. A different fixed action normalization multiplies every bound below by its corresponding positive constant. At quadratic order the colors decouple, so all finite scalar matrix constants also hold componentwise for the Lie algebra.

Let U_k(V) be the actual local branch of full-block constrained minimizers, with U_k(1)=1 in the chosen gauge. Assume it is twice continuously differentiable near the trivial datum (an analytic branch suffices) and that its coarse constraint is the stated composed averaging map. Write

    U_k(exp(i t B)) = exp(i eta[t L_k B+O(t^2)]).

Differentiating its constraint gives Q_k L_k B=B. Since the fine action is stationary at 1, the second derivative of the minimizer chart does not contribute to the effective Hessian. Hence, for f_k(V)=S_eta(U_k(V)),

    q_eff,k(B) := D^2[f_k(exp(i B))]_(B=0)[B,B]
                = ||d_eta L_k B||_eta^2
                >= ||d_1 B||_1^2.                    (5.2)

No preexisting effective gap is used. The Hessian identity follows directly from the chain rule, and its lower bound uses only the first derivative of the constraint. For a merely differentiable branch, the same computation supplies the quadratic Peano expansion, but additional regularity is needed before calling that coefficient a classical Hessian.

The equivalent quadratic variational statement is

    q_eff,k(B) = inf_{Q_k A=B} ||d_eta A||_eta^2,        (5.3)

when every tangent-feasible field has a feasible nonlinear curve and the stated branch minimizes the nonlinear action. To prove this, compare the minimizer to such a curve with derivative A and divide the action comparison by t^2/2. Conversely L_k B is tangent-feasible. Equation (5.2) does not require invoking the stronger equality (5.3).

At the flat background q_eff,k annihilates all infinitesimal gauge directions by gauge invariance and stationarity. Current-dependent corrections to the nonlinear constraint chart vanish at (U,J)=(1,0). These facts identify the quadratic physical action part used by the flat gauge bridge. They do not identify an arbitrary independent-current extension with a physical action Hessian.

## 6. A finite-matrix proof of the axial Poincare bound

Return to the unit lattice and fixed odd L. Let Omega be the cube consisting of 3^d adjacent L-blocks, indexed by {-1,0,1}^d. Let E_Omega be all positively oriented bonds whose endpoints lie in Omega, and P_Omega all plaquettes with all vertices in Omega.

For each block choose the coordinate-ordered rooted spanning tree. Let T_0,Omega contain all its root-to-site path-integral rows. Let Q_st,Omega contain the straight-string rows (2.1), with M=L,h=1, for all neighboring block-center pairs inside Omega. Each such string lies in the union of its two endpoint blocks, so it reads only E_Omega.

Form the finite real symmetric matrix

    M_L = d_Omega^* d_Omega
          + T_0,Omega^* T_0,Omega
          + Q_st,Omega^* Q_st,Omega,

and define

    sigma(d,L)=lambda_min(M_L).                        (6.1)

This is a completely specified finite matrix with rational entries. It is strictly positive.

Proof. If a bond field B has zero quadratic form, then d_Omega B=0. On the rectangular grid Omega, discrete path independence implies B=D phi: swaps of adjacent coordinate steps are justified by the zero plaquette curls. The equations T_0,Omega B=0 force phi to be constant on each L-block. For a neighboring pair of blocks, Q_st,Omega B equals the difference of those constants divided by L, since every translated string telescopes. Its vanishing forces equality of adjacent block constants. The coarse 3^d block graph is connected, so phi is constant on all of Omega and B=0. Thus the finite matrix has trivial kernel, proving sigma(d,L)>0. This is a proof of the gap, not an assumption that a smallest singular value is positive.

For a global bond field B satisfying T_0 B=0 and Q_1 B=Q_st B=0, restrict it to every translated copy Omega_y. All local T_0 and Q_st rows vanish there, so

    sum_{b in E_(Omega_y)} |B_b|^2
       <= sigma(d,L)^(-1) sum_{p in P_(Omega_y)} |(d_1 B)_p|^2.

Every global bond lies in at least one such cube. Every plaquette lies in at most 3^d cubes. Summing gives

    ||B||_2^2 <= [3^d/sigma(d,L)] ||d_1 B||_2^2,
    ||d_1 B||_2^2 >= gamma_loc ||B||_2^2,
    gamma_loc := sigma(d,L)/3^d >0.                    (6.2)

The same proof works on the exact periodic regulator. Pull the periodic field back to each ordinary local cube Omega_y in the covering lattice, allowing repeated coordinates when the torus is small. The local inequality holds for that pulled-back array. Summing the local arrays counts each plaquette at most 3^d times with multiplicity, exactly as above. There is no requirement to replace the torus or enlarge its periods. The argument does not require a nonwrapping cube.

For an infinite field use finite sums or square summability, then monotone convergence. The constant is independent of volume, scale and color dimension. It may be very small as a function of fixed d,L, which is immaterial for a uniform-in-scale existence statement.

## 7. The resulting flat exponential-gauge lower bound

Combine (5.2) and (6.2): on ker Q_1 intersect ker T_0,

    q_eff,k(B)>=gamma_loc ||B||^2                       (7.1)

uniformly in k and volume. Thus the axial lower bound in the gauge-bridge note can be taken to be gamma_ax=gamma_loc in full bond-field norm; no conversion from a quoted independent-coordinate axial gap is needed.

Let h_*=d(L-1), n=L^d,

    d_0=2sqrt(d),
    t_0=sqrt(h_*(n-1)),
    gamma_T=gamma_loc/(1+d_0 t_0)^2,
    gamma_exp=1/(gamma_T^(-1)+d_0^2).

The exact averaged-contour decomposition and the constraint-compatible tree conversion proved in the bridge note then yield, for B in ker Q^flat,

    q_eff,k(B)+||T B||^2 >= gamma_exp ||B||^2.          (7.2)

After the actual flat pivot elimination B=K_flat z, the retained variables are a coordinate restriction of B, so

    K_flat^*[q_eff,k+T^*T]K_flat >= gamma_exp I.         (7.3)

This is a lower bound on the real flat precision. It does not prove a uniform upper precision bound, complex accretivity on the free-current carrier, exponential kernel bounds, or a local precision perturbation expansion. Those are separate operator and source-matching requirements for the Gaussian cutoff modules.

## 8. Exact scope of the source identification

The necessary match is narrow: the whole-lattice effective action at the trivial background must be the action of the differentiable constrained minimizer with the specified normalized group average. The primary source identifies this effective action and its quadratic Gaussian term in CMP109, (0.21)--(0.22), (2.6)--(2.11), pp.256 and 266--267. Raw II, `8.2:not-small-field-step`, around lines 73870--74020, records the same variables and elimination. The derivative of the group average is fixed by its stated first-order property and by the contour definition, not inferred from gauge covariance alone. The corrected fluctuation averaging operation in raw I 24355--24375 has the straight derivative of Section 4.1. If that operation is substituted for the original constraint, its relation to the effective minimizer must be checked; (4.5) explains why a proved full-block gauge equivalence preserves the flat quadratic infimum.

This note checks the linear averaging algebra and supplies the missing elementary flat gap estimate. It does not reprove the nonlinear minimizer existence/differentiability theorem. It also does not transfer the argument to domains with holes, frozen boundary bonds, mixed histories, or a different averaging normalization. Such changes require their own constraint and boundary check.

For the unmarked Gaussian cutoff contribution to the coupling increment, a flat reference is the relevant one: raw I evaluates the carrier Hessian at (U,J)=(1,0). A positive flat reference precision is therefore useful, but the analytic carrier responses and the required covariance/locality bounds remain to be proved independently. No arbitrary-reference background locality is inferred from this flat calculation.
