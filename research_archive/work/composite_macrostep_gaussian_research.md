# The Gaussian of a composite ordinary macrostep

Research derivation, 17 October 2026. Fix a primitive odd ratio ell>=3 and a finite macro ratio R=ell^s, s>=1. The preceding classical depth is M=ell^k, k>=0. The current lattice has spacing one and the original fine lattice spacing is M^(-1). All constants below may depend on ell,s, equivalently on the fixed construction of R, but are uniform in old depth M and compatible periodic volume. This is the flat and small-background Gaussian module of the newly proposed composite macrostep. It is not a claim that the composite group average equals a direct-R ordinary average or that it equals a sequence of separately truncated quantum integrals.

The independent geometry proof is being supplied in the companion composite-macrostep geometry note. The exact facts it needs for this argument are also spelled out below. The real uniform gap is proved by an explicit local nullspace argument; it is not inferred from the mere finiteness of the chart.

## 1. Inputs already established at arbitrary old classical depth

Let S_M(a) be the ordinary homogeneous classical minimum action with current datum exp(i a), using the primitive ell hierarchy. Its flat Hessian q_M is the effective Maxwell form

    q_M(B)=inf_(Q_M^st A=B) ||d_(1/M) A||_(1/M)^2.

The preceding flat and nonlinear classical results establish, with current counting norms,

    ||d_1 B||_2^2 <= <B,q_M B> <= C_d ||B||_2^2,
    C_d=2^(d+6)(d−1),

for M>=1 (with the identity case M=1 included). They also establish positive kappa_q and finite K_q, independent of M and volume, such that the current-unit weighted Schur norms of q_M are bounded by K_q. Finally,

    DS_M(0)=0,
    ||DS_M(a)||_infinity <= C||a||_infinity,
    ||D²S_M(a)−q_M||_kappa <= C_kappa ||a||_infinity

on a common small product background ball. These are properties of the previously constructed homogeneous classical action; none depends on choosing R as the next physical source ratio. The current counting normalization has no additional M^d factor.

References within this project: the current-scale Gaussian module in `current_scale_gaussian_fragment.tex`; the q_M construction and local Maxwell gap in `flat_maxwell_gap_research.md`; its upper lift and uniform Fourier locality in the corresponding flat lift/decay notes; and the ordinary classical Hessian theorem of Notebook16.

## 2. The actual composite flat constraint

Define the group-valued constraint by the actual primitive composition

    F_R(V)=M_ell^s(V).

In this note C_R denotes its angle derivative at the identity:

    (C_R B)(c)=d/dt [log F_R(exp(i tB))(c)/i] at t=0.

Thus C_R maps unit-current link angles to final R-link angles. It is not divided by R. Its exact recursive formula is the product of the primitive angle derivatives C_ell at the successive nested lattices. Each primitive factor is ell Q_ell^flat in its own unit-lattice indexing.

### 2.1 Exact locality and covariance needed here

For a final coarse bond c=(y,y+R e_mu), the entire nonlinear output F_R(V)(c) reads current bonds contained in the union of the two endpoint R-blocks. To see this, a primitive output reads internal endpoint contours and the parallel/reference strings between its two endpoint blocks. All those bonds stay in their union. At the next composition level, the lower blocks centered at the intermediate sites tile the two larger endpoint blocks exactly. Induction gives the claim for every level. The same argument works in the periodic covering geometry with the prescribed lifted local paths; no endpoints or opposite interfaces are silently identified before the path is evaluated.

Every primitive map is gauge covariant with restriction to its block centers. Composition therefore gives

    F_R(V^g)=F_R(V)^(g restricted to R-centers).

With D phi(b)=phi(b_+)−phi(b_-), differentiating at the identity gives

    C_R D phi(c)=phi(y+R e_mu)−phi(y).                  (2.1)

This identity is in angle coordinates. For example, take the infinitesimal gauge g=exp(−it phi) to verify its sign with the convention V^g=g_- V g_+^(-1). Only the endpoint difference will be used in the positivity proof.

### 2.2 The actual pivot and retained insertion

For each final coarse bond select the positive unit bond p(c) crossing its R-block interface on the center line. For y=0 its endpoints are (R−1)e_mu/2 and (R+1)e_mu/2. At the first primitive step it is the primitive interface pivot between centers (R−ell)e_mu/2 and (R+ell)e_mu/2. It can affect only that primitive output bond. At level t the affected bond has endpoints (R−ell^t)e_mu/2 and (R+ell^t)e_mu/2 and is again the next primitive pivot. Hence it affects precisely the final equation c and no other final equation.

At flatness the primitive pivot angle coefficient is ell^(1−d) times the color identity. The chain rule along this unique affected output chain consequently gives

    (C_R)_(c,p(c'))=R^(1−d) I_color delta_(c,c').       (2.2)

Let E_f insert retained nonpivot coordinates and put

    (h_R w)(p(c))=R^(d−1)w(c),  h_R w=0 elsewhere,
    K_R=(I−h_R C_R)E_f.

Then C_R h_R=I, C_R K_R=0, K_R is the identity on retained coordinates, and its image is exactly ker C_R. Both h_R and K_R have fixed R-range. This is the actual flat pivot elimination for the composite constraint, not the pivot of a direct-R replacement average.

A fully explicit conservative upper bound follows from the primitive one-step norm. Put

    r_ell=1+2d(ell−1)/ell,
    c_R=[ell r_ell sqrt(2d+2)]^s,
    k_R²=1+R^(2d−2)c_R².

The already checked primitive row/column estimate gives ||C_ell||_(2->2)<=ell r_ell sqrt(2d+2); counting Hilbert norms compose between the successive angle spaces. Thus ||C_R||<=c_R and ||K_R||²<=k_R². Sharp constants are unnecessary.

### 2.3 Relation to the straight average, without identifying group maps

The previously proved exact cumulative endpoint-gauge identity relates the ordinary composition to the fixed-reference corrected composition. Differentiating it at the identity gives a finite-range scalar linear map beta_R such that

    C_R=R Q_R^st − partial_R beta_R,                    (2.3)

where partial_R is the unnormalized endpoint difference on final R-center bonds. Indeed the corrected composition has derivative R Q_R^st by the straight-average semigroup, while the infinitesimal cumulative endpoint gauge contributes beta_R(y)−beta_R(y'). One may define beta_R directly as the derivative of that cumulative gauge; this fixes its sign and normalization without guessing a direct-R contour identity.

Equation (2.3) does not say beta_R equals the direct-R averaged contour mean, and does not say C_R equals the derivative of a direct-R ordinary map. On gradients it gives beta_R D phi equal to the R-block mean of phi minus phi at the center, up to an irrelevant spatial constant; the direct primitive telescoping recursion gives this equality with the natural zero-at-zero normalization.

No part of the gap proof below requires (2.3). It requires only the actual locality and exact gradient identity (2.1), which were derived directly from the composite map.

## 3. Independent direct-R contour gauge

Choose the actual direct-R internal averaged-contour variable P_R solely as the independent gauge-fixing device. Its flat derivative is

    (T_R B)(y,x)=average_Gamma(y,x) sum_(b in Gamma) orientation(b) B_b,

for x in the R-block B_R(y), with the center row zero. The prescribed paths are block-internal. Therefore

    T_R D phi(y,x)=phi(x)−phi(y),
    T_R h_R=0.                                         (3.1)

The real absolute gauge action

    G_R(V)=sum_(y,x) [1−Re tr P_R(V;y,x)]

has zero constant and linear terms at V=1 and flat Hessian T_R^T T_R in normalized trace coordinates. This follows by expanding P_R(exp(i tB))=1+i tT_RB+O(t²); no assumption about the quadratic logarithmic coefficient is required.

The elementary Schur bound is

    ||T_R||² <= t_R²,
    t_R²=d(R−1)(R^d−1).                                (3.2)

It uses the maximum contour length d(R−1) and at most R^d−1 target rows through any internal bond. This is a bound on the actual averaged contours, not a replacement tree gauge.

## 4. A finite local matrix with proved trivial kernel

Let Omega be the ordinary rectangular cube made from the 3^d R-blocks with centers indexed by {-1,0,1}^d. Let E_Omega be all positive unit bonds whose endpoints lie in Omega and P_Omega all unit plaquettes whose vertices lie there.

Use all direct-R contour rows for the blocks inside Omega. Use all composite C_R rows for neighboring R-center pairs inside Omega. By the exact two-endpoint-block locality, each such row uses only E_Omega. Form the finite scalar real symmetric matrix

    M_R,Omega=d_Omega^T d_Omega
               +T_R,Omega^T T_R,Omega
               +C_R,Omega^T C_R,Omega,
    sigma_R=lambda_min(M_R,Omega).                     (4.1)

The coefficients are fixed finite numbers depending only on the selected composite geometry. The same matrix acts separately on each color.

**Lemma. sigma_R>0.** If the quadratic form in (4.1) vanishes, d_Omega B=0. The rectangular grid has no holes; discrete path independence, using its plaquette relations, gives B=D phi on all E_Omega. Equation (3.1) and T_R,Omega B=0 force phi to be constant on every R-block. For two neighboring block centers, the local form of (2.1) gives C_R,Omega B equal to the difference of these two block constants. Those rows vanish, so adjacent constants agree. The 3^d coarse block graph is connected. Hence phi is constant throughout Omega and B=0. This proves trivial kernel, and therefore strict positivity of the finite matrix.

The local gradient identity used here is valid without a global extension assumption on phi: extend phi arbitrarily beyond Omega, apply (2.1), and use the row's two-block locality to see that the result depends only on the original array.

This proof rules out all flat gradient and harmonic obstructions. It is the missing quantitative mechanism; the conclusion is not obtained simply by declaring that a local matrix is finite.

## 5. The uniform-volume and uniform-old-M lower bound

Apply the local inequality to each macro translate Omega_y. Every current bond lies in at least one patch. Every plaquette, contour row, and neighboring-center constraint row is counted at most 3^d times. Thus, for any square-summable current field,

    sigma_R ||B||² <= 3^d[||d_1B||²+||T_RB||²+||C_RB||²].     (5.1)

On periodic tori pull the field back to the ordinary cube in the covering lattice. If coordinates repeat, retain every repeated occurrence in the local array. Summing over patch centers gives the same at-most-3^d multiplicities. This proves (5.1) on the compatible original regulator family without requiring an embedded nonwrapping patch. The composite chart itself still uses the geometry assumptions of Section 2, including distinct source interfaces.

For B in ker C_R, combine (5.1) with the already proved lower bound for q_M:

    <B,q_M B>+||T_RB||² >= gamma_R ||B||²,
    gamma_R=sigma_R/3^d>0.                              (5.2)

No constant in sigma_R or this comparison depends on M. The corresponding upper bound on all current fields is

    <B,q_M B>+||T_RB||² <=(C_d+t_R²)||B||².              (5.3)

This establishes both sides of the comparison for the actual composite constraint and the independently selected gauge. No auxiliary axial constraint or equality with a direct-R averaging operator has been used.

## 6. The retained Gaussian and its normalization

At the flat background the action gradient and gauge gradient vanish. Therefore the nonlinear pivot chart's second derivative contributes no gradient-times-chart-curvature term at this point. The retained flat precision is exactly

    A_(M,R),0=K_R^T(q_M+T_R^T T_R)K_R.                  (6.1)

Since z is a coordinate restriction of K_Rz, ||K_Rz||>=||z||. Equations (5.2)–(5.3) and the upper insertion bound give

    gamma_R I <= A_(M,R),0 <= B_R I,
    B_R=(C_d+t_R²) k_R²,
    B_R^(-1) I <= A_(M,R),0^(-1) <= gamma_R^(-1) I.      (6.2)

There are d(R^d−1)dim(g) independent retained real coordinates per R-block. Their normalized flat Gaussian density is

    (2pi)^(-n/2) det(A_(M,R),0)^(1/2)
        exp[−z^T A_(M,R),0 z/2] dz,

so its counting covariance is A_(M,R),0^(-1). The coupling has been removed by the usual fluctuation scaling, and no original-fine volume factor M^d enters these current coordinates. Haar and nonlinear Jacobian terms remain interactions.

## 7. Weighted inverse from the real gap and the existing q_M decay

Group retained coordinates by R-blocks. The already proved weighted q_M bound can be regrouped into R-blocks with any positive exponent alpha satisfying alpha/R<=kappa_q. For example the elementary block estimate is

    ||q_M||_(Schur,alpha;R-blocks)
       <= R^d exp(alpha d) K_q(alpha/R).

K_R has finite range and uniform finite weighted row/column norms at every fixed exponent. T_R is block-internal. Weighted matrix multiplication therefore gives some alpha_R>0 and A_R^*<infinity, depending only on fixed R and the primitive geometry, such that

    ||A_(M,R),0||_(Schur,alpha_R)<=A_R^*                (7.1)

uniformly in M and volume.

For completeness the inverse bound can be proved without inferring it from the spectral sandwich alone. For a fixed block j use the positive block weight w_i=exp[t d(i,j)], and W=diag(w_i I). Its ratio satisfies w_i/w_k<=exp[t d(i,k)]. For 0<t<=alpha_R/2,

    ||W A W^(-1)−A||_(2->2)
       <=sup_i sum_k ||A_ik||(exp[t d(i,k)]−1)
       <=2t A_R^*/(e alpha_R),                         (7.2)

with the same bound for columns. The last inequality uses x exp(−alpha_R x/2)<=2/(e alpha_R). Choose

    t_R^loc=min(alpha_R/2, e alpha_R gamma_R/(4A_R^*)).

The perturbation is at most gamma_R/2. The inverse of W A W^(-1) has norm at most 2/gamma_R by the resolvent identity and (6.2). Taking its (i,j) block yields

    ||(A^(-1))_ij|| <=(2/gamma_R) exp[−t_R^loc d(i,j)]. (7.3)

On a finite torus W is bounded, and its periodic distance is 1-Lipschitz. On the infinite lattice use truncated distance weights, obtain the same uniform bounds, and pass to the limit in each block entry. A smaller exponent, for example kappa_R=t_R^loc/2, gives

    ||A_(M,R),0^(-1)||_(Schur,kappa_R)
       <=(2/gamma_R) sum_(z in Z^d) exp[−t_R^loc |z|_1/2].    (7.4)

The periodic sums are bounded by the same infinite-lattice sum using shortest representatives. This proves the required exponential retained covariance locality uniformly in old M and compatible volume. Both the real gap and the prior q_M weighted bound are essential inputs.

## 8. Small-background extension and what it does not identify

The geometry module supplies a finite-range analytic pivot chart Phi_a(z) for the composite relative constraint, retaining z exactly, with derivatives through the needed finite order bounded on a fixed small product ball. Let

    a_V(z)=log[exp(i Phi_a(z))exp(i a)]/i,
    A_(M,R)(a)=D_z²[S_M(a_V(z))+G_R(exp(i Phi_a(z))exp(i a))] at z=0.

Use the full absolute direct-R gauge action, including its residual gradient and Hessian away from P_R=1. The ordinary chain rule gives an action term

    (Da_V)^T D²S_M(a) Da_V
           +<DS_M(a),D²a_V>,

and the full gauge Hessian. The two chart curvature contributions—constraint straightening and ordinary-log conversion—are retained. Uniform current classical Hessian bounds from Section 1, finite-range coefficient sums of the fixed-R chart, and local Cauchy estimates consequently give, at a smaller fixed exponent,

    ||A_(M,R)(a)−A_(M,R),0||_(Schur,kappa_R)
       <=C_(R,kappa_R)||a||_infinity.                 (8.1)

The proof is the same finite-row/column contraction of local second derivatives used in the passed physical current precision module; every extensive scalar gradient is bounded in supremum before that local contraction. No factor of the total volume appears. A sufficiently small background ball therefore gives uniform complex accretivity, a holomorphic inverse, and its weighted Neumann bound.

Equation (8.1) is an analytic family statement. Centering of the physical integral still requires the physical stationary branch and the exact gauge-insertion normalization from the independent integral module. It does not remove any cutoff factor, prove a free-independent-current carrier, or identify this newly selected gauge with a historical deposited macro gauge. Strict background-support coefficients require the corresponding classical support composition, not merely (8.1).

## 9. Scope and remaining interfaces

For the actual composite map F_R=M_ell^s and independent direct-R contour gauge, the flat retained Gaussian has a proved real spectral sandwich and exponential inverse, uniform in old M and volume at fixed R. The exact composite angle derivative, its endpoint-gradient behavior and actual pivot are all explicitly used. The direct-R average has never been substituted for the composite average.

The Gaussian module therefore needs no additional unknown uniform-old-depth coercivity estimate once the companion exact geometry is verified. The remaining macrostep interfaces are the global or admissible-domain gauge insertion and normalization, the physical branch comparisons, precise cutoffs, supported interaction bounds, and their relation to any proposed stable analytic domain. Even after those finite-step modules, amplitude control and the other quantum-induction requirements remain open.
