# A controlled local curvature-metric response of the flat Maxwell action

16 October 2026. This is a proved perturbation lemma for the fixed normalized straight-string constraint. It uses the audited local minimizing curl from `flat_minimizer_locality_research.md`. It is not an identification of the non-Abelian background variation, independent-current carrier, or a varying averaging operator.

## 1. Hilbert spaces and exact scope

Let B be the coarse bond Hilbert space with unit coarse volume measure, A the fine bond Hilbert space with physical measure eta^d, and F the fine plaquette Hilbert space with the same physical measure. Work either on a compatible finite periodic lattice or on the homogeneous infinite lattice with square-integrable fields. For fixed eta=1/M, let D_curl:A->F be the physical fine curl and Q:A->B the fixed normalized straight-string average.

Let H:B->A be an exact bounded flat minimizing right inverse, QH=I. Its gauge selection is immaterial here, because all exact minimizers have the same curvature. Put

    F_0=D_curl H,
    q_0=F_0^*F_0,
    K=closure{D_curl zeta: zeta in A, Q zeta=0},

and let P_K be the orthogonal projection onto K. The audited construction gives a uniform bound ||F_0||^2<=C_E(d), for example C_E(d)=2^(d+6)(d-1), together with an exponentially local cell kernel independent of M. The original least-field-norm lift and the source-compatible lift have the same F_0.

For any coarse datum B, all feasible curvatures are F_0 B+D_curl ker Q. Their closure is F_0 B+K. Flat minimality implies

    P_K F_0=0.

Indeed, differentiating the real flat energy along any feasible variation gives orthogonality to D_curl ker Q, and continuity gives orthogonality to its closure. Closure is harmless for the infimum of every bounded strictly positive quadratic form. On a finite torus K is already finite dimensional and closed.

## 2. Exact perturbed action

Let v:F->F be a bounded selfadjoint curvature operator. For real tau with |tau| ||v||<1, define

    <B,q_tau B>
       =inf_(Q A=B) <D_curl A,(I+tau v)D_curl A>.

Since I+tau v is strictly positive, the same infimum is obtained over F_0 B+K. Write a candidate curvature as F_0 B+k. Stationarity in K gives

    [I_K+tau P_K v P_K] k=-tau P_K v F_0 B.

The bracket is invertible by a norm-convergent Neumann series. Completing the square or substituting this minimizing k proves the exact operator identity

    q_tau=q_0+tau F_0^*vF_0
       -tau^2 F_0^*v P_K
          [I_K+tau P_K v P_K]^(-1)
          P_K vF_0.                                      (2.1)

Every occurrence of the inverse is on K. Equivalently use the full-space inverse of I+tau P_KvP_K between the two projections. The signs and powers of tau in (2.1) are exact.

The same expression extends holomorphically to complex tau on |tau| ||v||<1. In that extension no complex infimum is asserted. More generally it is holomorphic for bounded complex V with ||V||<1 after replacing tau v by V. The two V factors in the second-order term are V, not V^*: conjugating the parameter would destroy holomorphy. Real selfadjoint V recovers the original minimizing action.

## 3. Uniform norm control and first derivative

Because ||P_K||=1,

    ||q_tau-q_0-tau F_0^*vF_0||
       <=|tau|^2 ||F_0||^2 ||v||^2/(1-|tau| ||v||).

Thus

    Dq(0)[v]=F_0^*vF_0,                               (3.1)

as a Fréchet derivative in bounded-operator norm. All constants and the norm radius are uniform in M and volume once ||v|| is uniformly bounded. No derivative estimate for the perturbed minimizing map is needed. This is a variation of the curvature quadratic form at fixed Q, not a derivative of the full Yang--Mills effective Hessian.

## 4. Local cell operators and the two-leg bound

Partition the fine plaquette bases into unit coarse cells. Let Pi_y denote the orthogonal projection onto the curvature variables in cell y, using physical fine volume measure. These projections are mutually orthogonal and sum to the identity. A plaquette is assigned by its base point; the fact that its vertices can straddle a cell wall does not change the Hilbert-space partition.

Let v_y=Pi_y v_y Pi_y be a bounded cell operator and write v_* =sup_y ||v_y||. Then the direct sum

    v=sum_y v_y

defines a bounded operator with ||v||=v_*; in infinite volume the sum is interpreted strongly. No factor depending on the number of cells or on the fine cell dimension occurs. The same statement holds for complex or selfadjoint cell operators as appropriate.

The local minimizing curl has a cell operator kernel satisfying

    ||Pi_y F_0 I_b||<=C exp(-kappa |b-y|_1),

where I_b includes the finitely many coarse bond components with base b. Its constants are uniform in M and volume. Equation (3.1) therefore gives the pointed first response

    ||[Dq(0)[v_y]](b,b')||
       <=C^2 ||v_y||
          exp[-kappa(|b-y|_1+|b'-y|_1)].             (4.1)

The adjoint in F_0^* is measured in the same physical fine volume norm used for v_y and Pi_y F_0. An unnormalized counting norm on the growing fine cell would not justify this scale-uniform estimate.

## 5. Uniform weighted Schur bound after summing cells

For 0<kappa'<kappa, set

    S_delta=sum_(z in Z^d) exp(-delta |z|_1),
    delta=kappa-kappa'.

By the triangle inequality |b-b'|_1<=|b-y|_1+|b'-y|_1 and (4.1),

    sup_b sum_b' exp(kappa'|b-b'|_1)
                       ||[Dq(0)[v]](b,b')||
       <=C^2 v_* S_delta^2.                          (5.1)

The same bound holds for column sums. In detail, sum first over b' relative to y and then over y relative to b. Absolute convergence justifies exchanging these sums and the local operator series. This proves that bounded cell coefficients produce an exponentially local first response in a fixed weighted Schur norm, uniformly in M and volume.

On a finite torus use shortest periodic block distance. Its triangle inequality gives the same proof, and sums of exp(-delta distance) are bounded by the full Z^d sum by choosing shortest representatives. Periodized curl kernels retain uniform constants. No thermodynamic-limit estimate for a surface free energy is involved.

## 6. What is not proved by the resolvent formula

Formula (2.1) alone provides higher derivatives and an operator-norm analytic radius, but does not by itself establish their spatial locality. Beginning at second order, the projection P_K links local insertions. One must not replace the norm bound ||P_K||=1 by a spatial decay claim. Sections 8--10 below now supply that missing spatial estimate using the separately audited full flat inverse; Sections 1--5 did not require it.

Similarly, the lemma keeps the averaging map Q fixed. A varying constraint contributes additional first-response terms, and a genuine non-Abelian background variation can alter covariant derivatives, gauge conditions, lower-order terms and the current. The statement here is only the curvature-metric perturbation for an explicitly fixed linear constraint.

If cell supports overlap with uniformly bounded multiplicity, a corresponding operator-norm bound needs an explicit overlap estimate. The simple equality ||v||=sup_y||v_y|| proved above uses the disjoint cell decomposition and is not automatically valid for arbitrary overlapping local operators.

## 7. Concrete result

The local flat minimizing curl alone supplies a scale-uniform, exponentially localized first derivative of the effective action under arbitrary bounded curvature-metric perturbations supported in one coarse cell. Bounded collections of such perturbations give a uniform weighted Schur bound. An exact Schur-complement formula controls the full perturbation in ordinary operator norm on a uniform analytic disk. The additional full-inverse input below upgrades this to all-order weighted locality. Actual Yang--Mills background and source matching remain separate.

## 8. Identify the curvature projection using the full source inverse

This section uses the independently audited theorem in `flat_full_inverse_research.md`: for a fixed positive homogeneous penalty a (in particular the matched unit-scale source value a=1),

    A_a=D_curl^*D_curl+D R D^*+Q^*aQ,
    G_0=A_a^(-1)

has uniform exponential physical-cell L2 kernels, including all fine-difference sandwiches of total order at most two. Here D is the scalar fine gradient, L=D^*D, Q_0 is the scalar average, and R is the actual flat source projection. To avoid confusion with the unpenalized action q_0 in Section 1, denote the auxiliary coarse precision by

    q_aux=(QG_0Q^*)^(-1)=q_0+aI.

The audited identities give H=G_0Q^*q_aux=H_src and

    Gamma=G_0-H q_aux^(-1)H^*,
    Q Gamma=0=Gamma Q^*.

Gamma is the inverse of the restriction of the strictly positive form A_a to ker Q, extended by zero on ran Q*. This follows either from the constrained Gaussian inverse formula or from Gamma A_a=I-HQ. All statements hold in finite compatible periodic volume and on the homogeneous infinite Hilbert space.

We prove the exact identity

    P_K=D_curl Gamma D_curl^*.                         (8.1)

For f in the curvature Hilbert space, let zeta=Gamma D_curl^* f. Then Q zeta=0, and zeta uniquely minimizes on ker Q the strictly convex functional

    ||D_curl zeta||^2+||R D^* zeta||^2
                        -2 Re <f,D_curl zeta>.

The coarse penalty vanishes on this constraint. Put r=R D^* zeta. The scalar source identities are

    Q_0 G'R=0,      L G'R=R,
    G'=(L+Q_0^*a'Q_0)^(-1).

They were proved in the scalar source-gauge audit; equivalently G'R=ZL. Consequently lambda=G'r belongs to ker Q_0, and L lambda=r. The fine vector D lambda belongs to ker Q because QD=d_coarse Q_0, has zero curl, and satisfies R D^*D lambda=r. Testing the stationary equation with D lambda gives ||r||^2=0. This test is legitimate at each fixed refinement because all fine difference operators are bounded; the uniform conclusion below uses the already proved sandwich bounds, not a bound on their individual norms.

The remaining stationary equation is

    <D_curl zeta-f,D_curl xi>=0 for all xi in ker Q.

Thus D_curl zeta belongs to K and f-D_curl zeta is orthogonal to K. It is exactly P_K f, proving (8.1). This also directly verifies that the right side is selfadjoint and idempotent. No assertion that the gauge penalty vanishes for an arbitrary feasible field was needed: it vanishes for this constrained forced minimizer by the scalar test above.

## 9. Projection locality and a weighted analytic disk

Choose a positive Schur exponent kappa below the common decay rates of the audited inverse and minimizing curl. Let

    f_kappa=||F_0||_kappa,
    g_2,kappa=||D_curl G_0 D_curl^*||_kappa,
    w_kappa=||QG_0Q^*||_kappa.

All constants are independent of M and compatible periodic volume. Equation (8.1) gives

    P_K=D_curl G_0 D_curl^*
                   -F_0 q_aux^(-1)F_0^*,
    ||P_K||_kappa<=g_2,kappa+f_kappa^2 w_kappa=:p_kappa.
                                                            (9.1)

Here q_aux^(-1)=QG_0Q^* is already local, so no inverse of the massless Maxwell precision q_0 has been taken. Increase p_kappa to at least 1 if necessary.

For any bounded complex curvature operator V in this weighted algebra with p_kappa||V||_kappa<1, the exact continuation of the perturbed action is

    q(V)=q_0+F_0^* V(I+P_K V)^(-1)F_0.              (9.2)

Expanding the inverse and using P_K^2=P_K shows that (9.2) is precisely (2.1), with tau v replaced by V. On the real selfadjoint slice, ||V||<1 and it agrees with the positive-form infimum. Off that slice (9.2) is the explicitly defined holomorphic continuation, not a complex minimization.

The Neumann series converges in the weighted algebra, and

    ||q(V)-q_0||_kappa
       <=f_kappa^2 ||V||_kappa/(1-p_kappa||V||_kappa),
    ||q(V)-q_0-F_0^*VF_0||_kappa
       <=f_kappa^2 p_kappa ||V||_kappa^2
                                      /(1-p_kappa||V||_kappa).

For the disjoint cell operators of Section 4, ||V||_kappa=sup_y||V_y||. Thus (9.2) supplies a volume- and refinement-uniform complex neighborhood for those bounded cell coefficients. The same argument covers any explicitly bounded finite-range or weighted-Schur curvature perturbation, with its actual algebra norm in the smallness condition.

## 10. All-order local curvature responses

At V=0, the nth derivative of (9.2), n>=1, is

    D^n q(0)[V_1,...,V_n]
      =(-1)^(n-1) sum_(sigma in S_n)
         F_0^* V_sigma(1) P_K V_sigma(2) ...
                                  P_K V_sigma(n) F_0.       (10.1)

There are n-1 projection factors. Therefore

    ||D^n q(0)[V_1,...,V_n]||_kappa
      <=n! f_kappa^2 p_kappa^(n-1)
                                    product_i ||V_i||_kappa.

If V_i is supported wholly in curvature cell x_i, the block from coarse cell b to coarse cell c has the stronger anchored bound

    ||D^n q(0)[V_1,...,V_n](b,c)||
      <=f_kappa^2 p_kappa^(n-1) product_i||V_i||
        sum_(sigma in S_n) exp[-kappa(
           d(b,x_sigma(1))
           +sum_(i=1)^(n-1) d(x_sigma(i),x_sigma(i+1))
           +d(x_sigma(n),c))].                         (10.2)

Indeed each current-free end is a block of F_0 or its adjoint, each interior link is a block of P_K, and the cell-supported insertions introduce no sum over intermediate fine sites outside their physical cell operator products. The weighted algebra bounds give these block estimates without a convolution at a borderline exponent. Repeated cells are allowed. On compatible finite tori use periodic distance, with the same constants.

This proves the previously missing higher-order locality for curvature-metric perturbations at fixed Q. It remains separate from a non-Abelian background variation: such a variation can also change the constraint, gauge projection, covariant derivatives, lower-order terms, or the current. No identification of those extra terms is made here.
