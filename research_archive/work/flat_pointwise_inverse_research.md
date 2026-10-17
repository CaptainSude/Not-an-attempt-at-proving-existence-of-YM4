# Pointwise regularity of the full homogeneous flat inverse

16 October 2026. This note proves a pointwise strengthening of the independently audited full flat inverse theorem. Bounded forcing on arbitrary fine bonds, with no regularity or coarse origin assumed, produces a uniformly bounded discrete C^{1,alpha} field for every alpha<1. The estimate has exponential coarse-cell locality and includes a bounded componentwise fine Laplacian. An explicit example shows why alpha=1 and individual second-difference bounds cannot be added uniformly. This is a theorem about the fixed homogeneous flat source operator; matching every original weak norm remains separate.

## 1. Operator, pointwise norms, and conclusion

Use fine spacing eta=1/M, odd M, unit coarse cells, the physical fine measure eta^d, and the notation of `flat_full_inverse_research.md`:

    A_a=d^*d+D R D^*+Q^*aQ,       G_0=A_a^(-1).

Here d is the fine curl, D the scalar gradient, Q=Q_M^st, R the matched flat scalar source projection, and a belongs to a fixed positive compact interval. The homogeneous normalized source value a=1 is included. Work on the infinite homogeneous lattice or any compatible periodic regulator. The matrix/color fibers have fixed finite dimension.

For a scalar or vector field on fine points in a bounded cell patch, define

    ||u||_(1,alpha;patch)
      =||u||_infinity
       +sum_mu ||D_mu^+ u||_infinity
       +sum_mu sup_(x!=y)
           |D_mu^+u(x)-D_mu^+u(y)|/|x-y|_1^alpha.

The difference bases x,y lie in the stated patch; its fixed one-step collar supplies the forward differences. Backward differences satisfy the same result. The seminorm is a discrete pointwise seminorm on actual fine-grid points, not an interpolated continuum derivative. Enlarging a unit output cell by a fixed number of neighboring coarse cells only changes constants.

**Theorem.** For each 0<alpha<1 there are C_alpha,rho>0, independent of M and compatible periodic volume, such that the inverse block from forcing supported in coarse cell m to the field in a fixed collar of coarse cell n obeys

    ||G_0(n,m)||_(fine l-infinity -> discrete C^(1,alpha))
            <=C_alpha exp(-rho |n-m|_1).                 (1.1)

The componentwise positive fine Laplacian L=D^*D on each vector component also satisfies

    ||(L G_0)(n,m)||_(fine l-infinity -> fine l-infinity)
            <=C exp(-rho |n-m|_1).                       (1.2)

On tori use periodic coarse-cell distance. The corresponding weighted row and column block sums are bounded at every smaller exponent. In particular arbitrary bounded fine forcing has uniformly bounded field, first differences, and local alpha-Hölder first differences, as well as bounded componentwise Laplacian. None of these assertions requires the forcing to arise from a coarse lift.

Proofs below are self-contained apart from the already audited algebraic full-inverse formula and its common complex strip. No pointwise conclusion is inferred from a growing-dimensional Hilbert norm.

## 2. Fine-cell Bloch reconstruction and the scalar term

On the enlarged common complex Bloch chart write z=x+iy, with real fundamental cube strictly inside a fixed cube |x_mu|<K<2pi. Fine aliases are p_r=z+2pi r, r in I_M^d. Put

    u_(r,mu)^+=M(exp(i p_(r,mu)/M)-1),
    P_r=sum_mu u_(r,mu)^+u_(r,mu)^-,
    F_M(z)_(s,r)=exp(i(z+2pi r).s/M).

The physical-cell reconstruction is F_M T F_M^(-1). For real z it is unitary from alias counting l2 to fine physical-cell L2. On the complex chart both directions have uniformly bounded physical L2 norms. Each Fourier coefficient of a fine-cell forcing f is therefore bounded by C||f||_infinity, and its alias l2 norm is at most C||f||_infinity.

The full formula is

    G_0=F+beta E_a^(-1) beta^-,

with F and beta as in the audited full-inverse note. Separate the orientation-diagonal scalar part

    T_r=1/P_r for r!=0,      T_0=0.                    (2.1)

The difference F-T consists of a fixed number of rank-one terms per vector orientation: a central block, two mixed central/high blocks, and one high/high rank term. Their high vectors are omega_(r,mu)^-/P_r and their analytic transpose partners. All remaining scalar coefficients are uniformly bounded and holomorphic on the smaller common chart. Thus the only genuinely full-rank pointwise question is the scalar operator (2.1).

## 3. Elementary weighted discrete heat estimates

Let p_s(n) be the continuous-time nearest-neighbor heat kernel on Z with generator

    (Delta_discrete f)(n)=f(n+1)+f(n-1)-2f(n).

It is the law of the difference of two independent rate-one Poisson processes, so

    sum_n p_s(n)=1,
    sum_n exp(t n)p_s(n)=exp(2s(cosh t-1)).          (3.1)

It is symmetric and decreases with n>=0. Here is a direct proof of the latter fact, avoiding a special-function assertion. Put q_n=p_s(n)-p_s(n+1), n>=0. Then

    q_0'=q_1-3q_0,
    q_n'=q_(n-1)+q_(n+1)-2q_n for n>=1,

with initial q_0=1 and q_n=0 for n>0. This bounded cooperative system preserves nonnegativity: add a sufficiently large scalar multiple of the identity to make every matrix entry nonnegative and expand its exponential. Therefore q_n>=0.

The Fourier formula and sin(t/2)>=|t|/pi on |t|<=pi give

    p_s(0)=(2pi)^(-1) integral_(-pi)^pi
                      exp(-4s sin^2(t/2)) dt
           <=C(1+s)^(-1/2).                          (3.2)

For 0<=r<=r_0, monotonicity and summation by parts yield

    sum_n exp(r|n|)|p_s(n+1)-p_s(n)|
      =(1+exp r)[p_s(0)
           +(1-exp(-r))sum_(n>=1)exp(r n)p_s(n)]
      <=C[(1+s)^(-1/2)+r exp(2s(cosh r-1))].       (3.3)

The zeroth weighted norm is at most 2 exp(2s(cosh r-1)), by (3.1). Let physical time be t, s=M^2t, and take r=delta/M for fixed small delta. Multiplying the difference by M gives

    sum_n exp(delta|n|/M)|D_eta p_(M^2t)(n)|
       <=C(t^(-1/2)+delta) exp(C delta^2 t).        (3.4)

This remains valid for t<eta^2: the trivial M bound is then no larger than t^(-1/2). The weight exp(r|n|) is submultiplicative. Applying (3.4) twice to p_s=p_(s/2)*p_(s/2) gives the second-difference weighted norm bound C(t^(-1)+delta^2)exp(C delta^2t). Tensor products give the same estimates in d dimensions, for any specified one or two forward/backward differences, with fixed-dimensional constants.

In particular, for 0<t<=1, the d-dimensional fine heat kernel has weighted physical operator L1 derivative norms

    sum_n exp(delta|n|_1/M)|D_eta^k p_(M^2t)(n)|
                    <=C t^(-k/2),       k=0,1,2.     (3.5)

Here the displayed p is the probability kernel. If written as a density against physical volume M^(-d), its density acquires M^d and the physical summation removes that factor. The estimate therefore has exactly the normalization needed for bounded fine forcing.

## 4. Complex-twisted cell heat kernels and the high-mode inverse

The finite-cell heat operator with symbol exp(-tP_r(z)) has the exact image-sum kernel

    H_z(t;s,s')=sum_(k in Z^d)
          exp(-iz.k) p_(M^2t)(s-s'+kM).             (4.1)

Its kernel convention is ordinary summation in the fine-cell index s'; equivalently divide by physical volume when writing a density. Equation (4.1) follows either by finite Fourier inversion or by the Bloch boundary condition. It remains valid for complex z by absolute convergence of the heat-kernel exponential moment. Fine output differences are the corresponding physical differences of the infinite heat kernel in this sum.

For s in a fixed output-cell collar and s' in the input cell,

    |exp(-iz.k)|<=C exp(delta|s-s'+kM|_1/M),

where delta bounds |Im z| and the constant depends only on the fixed collar. Summing (3.5) over s' and image indices k therefore proves

    ||D_eta^k H_z(t)||_(l-infinity -> l-infinity)
                      <=C t^(-k/2),     0<t<=1,
                      k=0,1,2.                       (4.2)

These are bounds on actual rows of the kernel, not bounds on the number of its entries.

For x,y fine output points in the fixed collar, telescope along a coordinate path. The difference between the first-gradient rows is bounded both by Ct^(-1/2) and by C|x-y|_1 t^(-1). Since min(A,B)<=A^(1-alpha)B^alpha,

    ||H_z(t)||_(l-infinity -> C^(1,alpha))
                    <=C_alpha t^(-(1+alpha)/2),
                      0<t<=1.                       (4.3)

Subtracting the central rank-one heat mode changes this bound only by a fixed constant: P_0 and u_0 are bounded on the chart, and the central output is exp(iz.s/M).

For t>=1, use the high-alias gap Re P_r(z)>=c|r|^2, r!=0. Each input Fourier coefficient is bounded by C||f||_infinity, and the output mode has C^(1,alpha) norm at most C(1+|r|)^(1+alpha). Consequently

    ||H_z(t)-exp(-tP_0)Pi_0(z)||_(infinity -> C^(1,alpha))
      <=C sum_(r!=0)(1+|r|)^(1+alpha)exp(-ct|r|^2)
      <=C_alpha exp(-ct/2).                          (4.4)

The high-mode inverse is exactly

    T(z)=integral_0^infinity
           [H_z(t)-exp(-tP_0)Pi_0(z)]dt.             (4.5)

Integrating (4.3) is legitimate precisely for alpha<1:

    integral_0^1 t^(-(1+alpha)/2)dt=2/(1-alpha).

Together with (4.4), this proves a uniform holomorphic l-infinity-to-C^(1,alpha) bound for the reconstructed scalar operator (2.1). For each M the spaces are finite dimensional and analyticity follows entrywise; the bounds just established are uniform in those growing-dimensional Banach norms.

## 5. The finite-rank corrections have the required pointwise regularity

The elementary centered-average factors obey, on the same enlarged complex chart,

    |a_r|+|a_r^-|<=C w(r),
    |omega_(r,mu)|+|omega_(r,mu)^-|
          <=C w(r)/(1+|r_mu|),
    w(r)=product_nu (1+|r_nu|)^(-1).                (5.1)

For a nonzero component r_nu, use the quotient sin((z_nu+2pi r_nu)/2)/(M sin((z_nu+2pi r_nu)/(2M))); its numerator is bounded and its denominator is bounded below by c|r_nu| on this chart. The zero component is uniformly bounded. The vector average contains one additional longitudinal factor. This proves (5.1), including aliases at the fine-zone edge.

On a dyadic max-norm shell 2^j<=|r|_infinity<2^(j+1),

    sum_shell w(r)<=C_d(j+1)^(d-1).                 (5.2)

To see this, choose one coordinate attaining the maximal scale. The sum of (1+|r_nu|)^(-1) over that coordinate's dyadic shell is O(1), while every other coordinate contributes at most O(j+1). Sum the d possible choices. Therefore sum_(r!=0)w(r)(1+|r|)^(-epsilon) is finite uniformly in M for every epsilon>0.

For the high output vectors v_(r,mu)=omega_(r,mu)^-/P_r,

    sum_(r!=0)(1+|r|)^(1+alpha)|v_(r,mu)|
             <=C sum_(r!=0)w(r)(1+|r|)^(alpha-1)
             <C_alpha.                              (5.3)

Their reconstructed fields consequently have uniform C^(1,alpha) norms, by absolute Fourier summation. The central vector has this property trivially. The full inverse's beta vector satisfies

    |beta_(r,mu)|
       <=C[|a_r^-|/(1+|r|)^3
                       +|omega_(r,mu)^-|/(1+|r|)^2],
                        r!=0,                       (5.4)

so exactly the same weighted summation applies to beta. Its canceled central component is uniformly bounded with all fixed low-mode differences.

Every input rank row has uniform alias l2 norm, as already proved in the full-inverse audit. If f is arbitrary bounded fine-cell forcing, Cauchy--Schwarz in the physical cell gives

    |rank_row(f)|<=C||f||_(physical L2)<=C||f||_infinity.

No factor M^(d/2) occurs because the physical cell has volume one. Thus all the finite-rank corrections map arbitrary fine l-infinity forcing to discrete C^(1,alpha), uniformly on the complex chart. Combining this with Section 4 gives the same bound for the whole reconstructed G_0.

## 6. The componentwise Laplacian is also bounded pointwise

For the scalar diagonal high-mode term, LT=I-Pi_0, whose l-infinity norm is bounded on the chart. Applying L to a high rank vector v_(r,mu) gives omega_(r,mu)^- for r!=0. Its full alias reconstruction is the physical Q^* profile, minus its bounded central mode.

The explicit physical adjoint formula is, for fine x=n+s/M and s in the centered cell,

    (Q^* B)_mu(x)=b_s B_mu(n)+(1-b_s)B_mu(n-e_mu),
    b_s=(s_mu+h+1)/M,       M=2h+1.                 (6.1)

The two weights are nonnegative and sum to one. For a coarse Bloch datum its profile is b_s+(1-b_s)exp(-iz_mu). Thus the reconstructed full omega^- vector is uniformly bounded in fine l-infinity on the complex chart and on any fixed collar. Absolute alias summation of omega itself is not needed and would give an incorrect logarithmic loss.

For beta, multiplication of its high formula by P_r gives

    (L beta)_(r,mu)
       =P_0 u_(r,mu)^+ a_r^-/(P_r D_s2)
                           -omega_(r,mu)^- k_mu d_mu^+.
                                                            (6.2)

The first term is bounded by C w(r)/(1+|r|), whose absolute alias sum is uniform by (5.2). The second is a bounded coefficient times the Q^* profile just discussed, with its central subtraction. The canceled central Laplacian component is bounded directly. Hence L beta is uniformly bounded pointwise as well.

The input rows retain the physical L2-to-scalar estimates of Section 5. Applying L to each finite-rank term, and adding LT, proves a uniform holomorphic l-infinity-to-l-infinity bound for L G_0 on the common complex chart. This does not prove Hölder continuity of the Laplacian: the Q^* profiles can have transverse coarse-block jumps. It also does not prove pointwise bounds for each individual second difference, which need not enjoy the Laplacian cancellation.

## 7. From chart estimates to exponential coarse-cell locality

The full reconstructed inverse, together with its output differences and Laplacian, is periodic in coarse momentum. The proof is the audited alias permutation and integer phase-wrap argument: under z->z+2pi n, reconstruction cancels the alias relabeling. Individual central/high pieces need not be periodic; they were used only to bound the full symbol on each chart. The enlarged holomorphic charts agree on real overlaps because they equal the same inverse, and therefore glue.

For output collars, include finitely many adjacent-cell copies with their coarse Bloch phases exp(iz.n). These phases are uniformly bounded on the common strip. Thus the same periodic holomorphic symbol takes values in the Banach operators from a fine-cell l-infinity space into the discrete C^(1,alpha) output-collar space, or into the Laplacian l-infinity space. Fourier contour shifting in each coarse coordinate gives (1.1)--(1.2), with constants independent of the dimensions of these finite spaces.

In infinite volume the resulting absolutely summable blocks define the inverse on bounded forcing and agree with the previously proved Hilbert inverse on their common domain, for example finitely supported fine forcing. The inverse identity then extends to bounded forcing through absolute convergence of the exponentially summable operator products at each fixed M. In particular the apparently nonlocal source projection causes no gap here: R=L Z L has exponentially summable physical-cell L2 blocks by the scalar theorem, and finite-cell norm equivalence converts them to summable pointwise blocks for each fixed M. This identity argument does not require that last conversion to be uniform in M; the uniform pointwise inverse bound was proved directly above. On compatible finite tori, sampling the same symbol gives exact periodization, as in the Hilbert theorem. The weighted bounds use periodic distance and retain the uniform constants, including short periods and the correct multiplicities.

Summing cell blocks gives a global bounded field and first differences, and uniform Hölder bounds on every fixed cell collar. These imply the global discrete alpha-Hölder estimate for the first differences: points within a unit physical distance are covered by one of finitely enlarged collars, while points farther apart use twice the uniform gradient bound. The same conclusion holds in periodic physical distance.

## 8. A demonstrated obstruction at alpha=1

For d>=2 there cannot be a refinement-uniform bound from bounded fine forcing to Lipschitz first differences, nor to each individual second difference. It already fails on the compatible torus consisting of one unit coarse cell.

On that torus the coarse momentum is zero. The audited zero-fiber formula says that G_0 is a^(-1) on the central constant mode and P_r^(-1) on every high alias, independently in each vector component. Therefore on fine mean-zero forcing it is exactly the inverse scalar periodic fine Laplacian.

Choose a smooth cutoff chi supported in a small ball inside the unit continuum torus and equal to one near its center. In local coordinates, let

    u_epsilon(x)=chi(x) x_1 x_2
                             (1/2)log(|x|^2+epsilon^2).

Subtract its torus mean if desired. The cutoff-region derivatives are uniformly bounded because its support there stays away from zero. Near zero, put P=x_1x_2 and f(r)=(1/2)log(r^2+epsilon^2). Since P is harmonic and homogeneous of degree two,

    Delta(P f)=P[f''+(d+3)f'/r]
       =P[(d+2)r^2+(d+4)epsilon^2]
                                  /(r^2+epsilon^2)^2.

Because |P|<=r^2/2, the continuum Laplacian is bounded by a fixed constant independent of epsilon. But

    partial_1 partial_2 u_epsilon(0)=log epsilon.

For each fixed epsilon>0, sample this smooth periodic function on increasingly fine odd grids, and subtract its exact discrete mean. Define the fine forcing f_(M,epsilon)=L_eta u_(M,epsilon). Its mean is zero, and Taylor convergence gives ||f_(M,epsilon)||_infinity<=C+1 once M is sufficiently large (depending on epsilon). The exact full source inverse on this one-cell torus returns u_(M,epsilon). Meanwhile its mixed second fine difference at the central lattice point converges to log epsilon.

Choosing first epsilon arbitrarily small and then M sufficiently large produces uniformly bounded forcing with arbitrarily large mixed second differences of G_0 f. A uniform Lipschitz seminorm for the first differences would bound those mixed differences and is therefore impossible. The same example can be placed in one fixed vector/color component. It does not contradict (1.2), because only the sum of the diagonal second differences is the Laplacian and that sum has the required cancellation.

Thus the restriction alpha<1 in the pointwise theorem is substantive. No endpoint estimate should be inferred by taking alpha to one in its constants.

## 9. Scope for the source program

The proof supplies pointwise fine-field, first-difference, alpha-Hölder first-difference, and componentwise-Laplacian estimates for the actual homogeneous flat inverse matched in the previous notes, with arbitrary bounded fine forcing and exponential coarse-cell locality. The matching value a=1 is included. This strengthens the physical-cell L2 inverse theorem without introducing a fine-dimension loss.

It does not yet identify every numerical factor and every term of the source's weak norms, establish nonflat uniform estimates, handle general retained-history domains, or control the full interacting current carrier. Those applications require their own exact norm and source-coordinate checks. In particular the false endpoint of Section 8 must not be smuggled into a source norm through an implicit claim that C^(1,alpha) controls every second derivative.
