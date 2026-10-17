# One composite small-field step on a common analytic domain

17 October 2026. Integrated research theorem, under independent internal review. The theorem concerns the local holomorphic RG map defined by one chosen composite ordinary pushforward and its retained-coordinate small-field sector. It is uniform in the preceding homogeneous classical depth and compatible finite volume. It does not establish a volume limit, a stable amplitude recursion, a large-field estimate or an identification with all histories of the original Wilson measure.

The inputs are the proved homogeneous classical modules through the strict-support construction, the pre-gauge supported representative, and the following newly checked modules:

* composite_macrostep_geometry_research.md: actual composite constraint and local pivot geometry;
* composite_macrostep_gaussian_research.md: its actual retained flat Gaussian and small-background comparison;
* composite_macrostep_integral_research.md: exact compact gauge insertion, sector, Jacobians and continuation;
* inherited_joint_core_tail_research.md and composite_macrostep_joint_family_research.md: the inherited joint carrier estimate;
* common_domain_classical_support_fragment.tex: direct strict support in the next background before integration;
* the strictly local tunable Gaussian theorem, periodic extension, and the closed-chain determinant estimate from the auxiliary grouping module.

All norms below are absolute coefficient-family norms. Bounds on a total extensive functional are not substituted for those norms.

## 1. Geometry, domains and the statement

Fix dimension d=4, a compact matrix gauge group with its fixed trace/color norm, and an odd primitive ratio ell>=3. Later choose once a macro ratio R=ell^s and an auxiliary grouping J=ell^j. The old classical depth is M=ell^k, arbitrary. Current spacing is one; final spacing is R, reset to one after the step. The input and output angle radii are both the same number b.

The input activity graph consists of centered J-blocks of the current lattice. Each such cell has D_in=d J^d dim(g) scalar current-angle coordinates. The output graph consists of J-blocks of the next lattice, equivalently JR-blocks of the current lattice. It is also the graph used for Gaussian integration. Projection pi_R from input to output has fiber R^d, preserves connected images, and satisfies

    |pi_R H| <= 2^d + (2^d/k_R)|H|,
    k_R = 1+floor((R-3)/4).                              (1.1)

All tori are compatible with ell,R,J; the distinct lifted macro interfaces are retained. Passing to this cofinal regulator family is part of the present construction.

Let the total inherited functional have a connected activity representation

    E(a)=sum_H E_H(a|H),
    ||E||_(a0;b) :=
       sup_i sum_(H contains i) exp(a0 |H|)||E_H||_b
       <= epsilon,        a0=1/16.                       (1.2)

Each coefficient is holomorphic on the scalar-coordinate product ball b. Assume total E, not necessarily each E_H, is locally gauge invariant on the common original domain, with a compatible holomorphic logarithm branch if E was obtained as a logarithm. Assume epsilon is bounded by a prescribed finite epsilon_bar. Constants below can be chosen independently of epsilon<=epsilon_bar.

There are finite choices R,J, positive b and g_0, and a retained link/color-ball threshold T=T(g)>=1, such that for every 0<g<g_0 the chosen small-field step has a holomorphic continuation to the full next-angle ball b. Its factorization is

    rho_next(W) = N_(M,R,g) exp[-S_(MR)(W)/g^2+E_next(w)],
    W=exp(iw),   ||w||_infinity<b,                       (1.3)

as a local holomorphic germ and its specified continuation. N is field independent. The classical action is the same homogeneous ordinary minimum action at total depth MR, after the d=4 physical rescaling. No coupling renormalization has yet been performed.

The output has connected strict w-activities on the output J-cell graph with the SAME field radius b and cardinality exponent a0. Before optional vacuum normalization, a sufficient bound has the form

    ||E_next||_(a0;b)
      <= C_T epsilon
         + C_delta b + C_det b
         + C_G [ tau(T)+v(g,T)+q(epsilon,g,T,b) ],        (1.4)

where all constants are finite and uniform in M and volume after R,J are fixed,

    v(g,T) <= C_base (gT^3+gT+g^2T^2),
    q(epsilon,g,T,b)
       <= 16 C_T C_R (gT/b) epsilon.                    (1.5)

Here tau(T) tends to zero as T tends to infinity, and C_T is explicit below. A change in harmless fixed constants in (1.4) absorbs exponentiation of the small exponents. Subtracting each output coefficient's value at zero doubles the bound at most and changes only N.

This is not a claim that the amplitude on the right of (1.4) is <=epsilon. In particular C_T is generally greater than one.

## 2. Exact integral and the meaning of its continuation

Use the actual composite ordinary constraint F_R=M_ell^s and the independently chosen direct-R internal contour gauge P_R. Its pivot chart Phi_V has unchanged retained coordinates. The physical background is

    Vp(W)=M_ell^k U_(MR)(W),
    Vstar(W)=Vp(W)^u(W),       P_R(Vstar)=1,              (2.1)

where u is the rooted internal contour gauge. The two minimum comparisons prove

    S_M(Vstar(W))=S_M(Vp(W))=S_(MR)(W).                  (2.2)

The last equality includes the d=4 unit rescaling. The actual integration field is exp(i Phi_Vstar(g xi)) Vstar. Phi(g xi), not g Phi(xi), is used everywhere. The retained window is the product of the prescribed invariant link/color balls |xi(b)|<=T.

After the exact compact gauge insertion and ambient pivot change of variables, the field-dependent factor is

    D_R(Vstar) det A(w)^(-1/2)
       exp[-S_(MR)(W)/g^2+E_pre(w)] Z(w),               (2.3)

with

    A(w)=D_z^2[S_M(exp(i Phi_Vstar(z))Vstar)
                      +G_R(exp(i Phi_Vstar(z))Vstar)]_(z=0),
    E_pre(w)=E(a_p(w)),    a_p=log Vp/i,
    Z(w)=E_(A(w)^-1)[ chi_window(xi)
                      exp(V_base(w,xi)+Q_inh(w,xi)) ]. (2.4)

The remaining factors are precisely the field-independent
c(g)^(-n_s) h_0^(n_e-n_c) g^[dim(g)(n_e-n_c)]
(2pi)^[dim(g)(n_e-n_c)/2] and a chosen flat determinant/pivot normalization. They are included in N. The background-dependent pivot and Gaussian determinants are not included in N.

V_base is the centered classical/gauge cubic remainder plus the ambient straightening and Haar logarithms. Q_inh is the exact total difference

    E(f_1(w,xi))-E(f_0(w)),
    f_lambda(w,xi)=log[
        exp(i Ad_(u(w)^-1) Phi_Vstar(w)(lambda g xi))
                   Vp(w)]/i,                           (2.5)

with the source-endpoint adjoint on every link. At lambda=0, f_0=a_p. The link group identity giving (2.5) changes no integration variable xi.

On the common small overlap these expressions equal the actual chosen small-field integral. On the full b-ball they define its holomorphic continuation using old-domain evaluations at f_lambda. If an actual gauge-invariant current density is given on gauge orbits and its representation exp[-S_M/g^2+E] holds at these pre-gauge fields, then gauge covariance gives the same expression pointwise for the chosen macro sector throughout this ball. Without that extra measure identification, the conclusion is a continuation of the local RG germ. Holomorphic uniqueness by itself does not identify a density for every earlier quantum history or the full Wilson pushforward.

The one-shot measurable completion and sector are newly specified in the integral module. They are not identified with s sequentially gauge-fixed or truncated primitive sectors. Every additional original cutoff would have to be retained and estimated.

## 3. Parameter order without a radius cycle

The following order is sufficient.

### 3.1 Fixed exponents and the pre-gauge reserve

Set

    a0=1/16,   kappa_G=2,   m_G=3,   gamma=8,
    B=53/8,    delta=1,    kappa_tail=8.                 (3.1)

The tuned Gaussian density factor below obeys log Kcal_theta<=5/8, so B is at least 4+log Kcal_theta+kappa_G. Also kappa_tail>=B+delta.

Choose a fixed pre-gauge cardinal reserve A_in>=d kappa_tail, with any additional fixed spare desired. This is done before R. The complete-fiber pre-gauge theorem supplies constants C_A,kappa0>0 and a radius r_A, all fixed at primitive ell, such that

    sup_i sum_X exp[kappa0 tau({i} union X)+A_in |X|]
                 ||a_(p,i;X)||_r <= C_A r/R             (3.2)

for every r<=r_A, uniformly in s,k and volume. The maximum over all current links of one final R-block is inside the support sum.

### 3.2 The physical macro ratio

Choose R=ell^s large enough that

    R>=8 C_A,
    (5^d 2^d/k_R) B <= a0/2.                            (3.3)

Such a finite choice exists because C_A was fixed before R. The actual composite geometry, chart and Gaussian are then fixed. Their local radii and constants are allowed to depend on this R.

The real retained precision satisfies

    gamma_R I <= A_(M,R),0 <= B_R I,                    (3.4)

and its inverse has exponential R-block decay, all uniformly in M and volume. Let lambda_0=1/B_R and Lambda_0=1/gamma_R denote the baseline covariance bounds. No direct-R ordinary average is substituted for the composite constraint.

### 3.3 Classical support reserves and auxiliary grouping

The separate classical-only coefficients have arbitrary finite reserves on independent outer classical radii. After R is fixed, choose any further reserves needed for its finite-range chart and strict precision/scalar composition. These may depend on R. They do not replace A_in in (3.2), and do not change the C_A used in (3.3). This distinction avoids a circular choice of R.

The actual rooted field a_star(w) is a fixed-R local analytic function of a_p(w). It therefore has a complete-fiber support family with any required finite reserve and norm O_R(r) on a uniform old-depth radius. The classical precision composition lemma then gives strict individually symmetric pieces of A(w)-A_0, with both matrix indices included in their declared supports, of weighted row norm O_R(r).

Choose J=ell^j sufficiently large for the grouped precision and covariance exponents, including 32/J below the available precision Steiner exponent and the reserve 64 for target gamma=8. Increase J so that

    16/J <= kappa0/2.                                   (3.5)

Choose ell_tail=c log J plus a fixed offset, with c>4d/kappa0. Eventually ell_tail+2<=J. For the inherited core/tail construction the macro tail norm and margin are

    s_tail <= J^d (b/4) exp[-kappa0 ell_tail/2],
    m=b/2.                                              (3.6)

The entire xi collar and projected core lie in the coordinatewise two-neighbor halo. Hence

    c0=5^d 2^d,   c1=5^d 2^d/k_R,   h0=2d,
    F=R^d,   D(J)=d dim(g) J^d.                         (3.7)

Choose J and the tail offset so that t=s_tail/m<=1/2 and

    D(J) log[1/(1-t)] <= a0/2.                           (3.8)

This is possible because the left side is controlled by a constant times
J^(2d) exp[-kappa0 ell_tail/2], which tends to zero. Its sufficient bound does not depend on b. The fixed macro halo, not a long artificial connecting set, is essential.

### 3.4 Final field radius and Gaussian neighborhood

The macro Gaussian fiber has

    D_G=J^d d(R^d-1) dim(g)                              (3.9)

retained real coordinates. Choose theta=1/(4D_G), so

    Kcal_theta=[(1+theta)/(1-theta)^3]^(D_G/2),
    log Kcal_theta<=5/8,
    rho_theta=(1+theta)/(1-theta).                       (3.10)

All Gaussian spectral, edge and support-algebra constants are now fixed, uniformly in M and volume. In particular the tunable strictly local theorem has a positive common threshold eta_*. Shrink that threshold, if needed, so that eta_*<=1; this makes the elementary numerical exponentiation budgets below literal.

Choose b>0 once, after R,J, below every required independent classical, physical-branch and chart radius. The actual joint-fiber Taylor substitution requires, for its fixed-R local rho_R,N0,

    e N0 exp(2 kappa0) C_A b/(R rho_R) <= 1/2.            (3.11)

The strict precision perturbation norm nu(b)=O_(R,J)(b) must meet all tunable support-algebra thresholds. In particular it is enough to impose

    nu(b)<=gamma_R/2,
    nu(b)<=theta gamma_R^2/(4 B_R),                      (3.12)

as well as the explicitly stated u<=theta and
w<=theta/[(1+theta)Lambda_0] conditions of the strict density theorem. Its support-algebra u,w are continuous O(nu) quantities at zero, so this is possible. Equation (3.12) gives covariance deviation at most theta lambda_0/2 by Neumann inversion. Additional smallness for the determinant closed-chain series is also met by the same shrink.

No input inherited radius is being divided at this step. We select one b on which both the input and output theorem will be stated. It can be extremely small.

### 3.5 Cutoff and coupling

A bad macrocell for the actual product of link/color-ball windows implies that its full retained Euclidean norm exceeds T. The Gaussian theorem therefore uses the valid joint-tail bound

    tau(T)=Kcal_theta 2^(D_G/2)
              exp[-T^2/(4 rho_theta Lambda_0)].          (3.13)

No false replacement of the link window by a macro Euclidean ball is made. Choose T>=1 large enough that e^3 tau(T)<=eta_*/4.

The actual inherited lambda radius is

    Lstar=b/(8 C_R gT).                                  (3.14)

Choose gT small enough that Lstar>=2 and Lstar gT lies within the fixed local chart domain; the latter is an additional bound on the already chosen b. Also require gT^3 and (gT/b) epsilon_bar sufficiently small for the base and inherited interaction budgets in Section 5.

These choices can be made for every sufficiently small g. For example T(g) can be at least the fixed threshold and grow as a fixed multiple of sqrt(log(1/g)); then tau(T)->0, gT^3->0 and gT/b->0 for the fixed b. There is no attempt here to optimize the numerical range.

## 4. Actual strict support inputs on the common graph

### 4.1 Classical precision and base interactions

The scalar classical action has strict coefficient families including its pair-supported quadratic part, with arbitrary finite cardinality reserve and a positive spatial exponent. Compose it with the actual fixed-R current chart and ordinary-log map, and add the local absolute gauge action. Differentiating these scalar pieces retains both chart-curvature terms and gives individually symmetric precision pieces. The full current gradient is bounded before contraction with local chart derivatives, so no volume factor occurs.

For clarity, strict substitution of a supported a_star(w) into a piece with old support Y can be proved by scalar-coordinate Cauchy. Its background Taylor multiindices sum to

    (1-s(r)/b_cl)^(-D|Y|),                               (4.1)

where b_cl is an independent classical outer radius. The arbitrary old cardinal reserve pays this factor. Matrix row and column indices stay in Y, so a precision row estimate incurs no new anchor sum. For scalar pieces with spectator xi, retain Y as an xi carrier even at Taylor degree zero and attach each background-support tree to Y. Rerooting with a positive spatial spare gives an anchored connected joint carrier estimate. This is the proved cdc composition lemma, not an inference from a one-weight response estimate.

After J grouping, the actual precision perturbation has the strict norm O_(R,J)(b). The base exponent family, already in w and local xi, satisfies

    ||V_base||_B <= v(g,T)
       <= C_base(gT^3+gT+g^2T^2).                       (4.2)

The action/gauge remainder is centered by subtracting its constant, linear and quadratic Taylor terms before composition. On the physical branch the total linear term is zero; away from it the independent-background extension retains the subtraction. No off-stationary saddle claim is used.

These coefficients read the output w directly before Gaussian integration. Thus no second stationary substitution, and no second inherited-radius cost, is required after the Gaussian theorem.

### 4.2 Inherited background and fluctuation pieces

The actual local map

    Omega_R(a,zeta)=log[
       exp(i Ad_(u(a)^-1) Phi_(exp(ia)^u(a))(zeta))
                          exp(ia)]/i

has Omega_R(a,0)=a and fixed R-block range in zeta. Banach radial Cauchy and polarization on complete local background fibers give

    ||f_lambda-a_p||_(kappa0,A_in;b,T)
                      <= C_R |lambda| gT.              (4.3)

Each coefficient's xi dependence is confined to a fixed collar of its output root, regardless of its possibly distant w-support. The degree-n bound is geometric in
e N0 exp(2kappa0) C_A b/(R rho_R), so (3.11) controls its full degree sum without interchanging a root supremum and an order sum.

On the disk (3.14), (3.2) and (4.3) bound the entire absolute family by b/4. The local support truncation core also has amplitude at most b/4; use margin m=b/2. Its tail and halo are exactly (3.6)--(3.8). The joint core/tail theorem consequently gives canonical connected carriers U_(K,lambda) with

    sum_K U_(K,lambda)=E(f_lambda),
    ||U_lambda||_B <= C_T epsilon,
    C_T=exp(B 5^d 2^d+2d) R^d S_1.                      (4.4)

All assignments are fixed independently of lambda. The lambda-zero family is termwise xi-independent because the actual difference family vanishes termwise at zeta=0. It represents E_pre and is not a vacuum constant.

Banach-valued Cauchy, with the contour integral before the positive anchored sum, gives

    Q_K=U_(K,1)-U_(K,0),
    ||Q_inh||_B <= q :=
           C_T epsilon/(Lstar-1)
       <=16 C_T C_R (gT/b) epsilon.                     (4.5)

Empty background support terms created by the fluctuation map are included; they may depend on xi and must not be discarded. This is an anchored joint coefficient estimate, not an extensive Cauchy bound on the total functional.

## 5. Nonvanishing and the exact output correction

Equal-carrier base and inherited exponents may be grouped. For v=||V_base||_B and q=||Q_inh||_B their total multiplier norm is bounded by

    ||exp(V_base+Q_inh)-1||_B
                      <= exp(v+q)(v+q).                (5.1)

The notation means coefficientwise equal-carrier exponentiation; products on overlapping distinct carriers are handled by the overlap theorem. Define every multiplier on its actual carrier window and extend it by zero outside that window. This does not alter the global retained-window integral.

For example, impose v<=eta_*/(16e), q<=eta_*/(32e), and shrink g further if necessary. Then (5.1) is below the interaction quarter budget, while (3.13) supplies the bad-block quarter budget. The precision conditions were already imposed in (3.12). The tunable strictly local Gaussian theorem therefore proves that Z(w) is nonzero throughout the full b-ball, selects its analytic logarithm, and gives connected strict w-carriers of cardinality weight

    a_G=min(1/2,kappa_G/4)=1/2.                           (5.2)

It gives a finite anchored bound C_G[tau(T)+v+q], after harmless fixed small-exponent factors. The theorem is applied directly in w. Its conclusion is stronger than mere finite-cutoff holomorphy or positivity on the real slice.

A quantitative inherited-log difference can also be obtained without losing the q factor in the presence of base interactions. For q>0 multiply Q_inh by a complex parameter zeta and take

    |zeta|<L_Q=eta_*/(16e q).

With v<=eta_*/(16e), the total exponent bound remains <=eta_*/(8e), so the same Gaussian quarter budgets hold on this disk. If q<=eta_*/(32e), L_Q>=2. The uniform connected-log bound is at most a fixed multiple of eta_*; Banach Cauchy in zeta then yields

    ||log Z_with-inherited - log Z_base||_(a_G;b)
                                     <= C_G' q.         (5.3)

For q=0 the difference is zero. This argument also covers multiple factor types sharing one carrier and avoids dropping the harmless base exponential in a multiplier difference.

Define the two external background terms by

    Delta(w)=log[D_R(Vstar(w))/D_R(1)],
    Qdet(w)=-one_half log det[A(w) A_0^-1].              (5.4)

Delta is a sum of the actual local pivot log determinants composed with the supported stationary map. It has a strict connected scalar family of norm C_delta b with any required fixed output reserve. Qdet is expanded afresh in closed chains on the macro graph:

    Qdet = one_half sum_(n>=1) (-1)^n/n Tr[(C_0 B(w))^n],
    B(w)=A(w)-A_0.                                      (5.5)

Joining every entire precision label and every covariance path gives a connected carrier of cardinality at most its total tree/path length plus one. The established gamma=8 row norm and a rerooting spare give, with K_8 nu_8<1,

    ||Qdet||_(1/2;b)
       <= [D_G exp(1/2) S_1/2]
                K_8 nu_8/(1-K_8 nu_8)
       <= C_det b.                                     (5.6)

This includes the background dependence of det A. Field-independent flat factors have already been moved into N.

The correction in (1.3) is exactly

    E_next(w)=E_pre(w)+Delta(w)+Qdet(w)+log Z(w),          (5.7)

up to a chosen field-independent normalization. Its first term has B-weight by (4.4), its two determinant terms have at least 1/2 weight, and the Gaussian logarithm has weight 1/2. All therefore have the required output weight a0=1/16 on the same b-ball, and (1.4) follows.

No coefficientwise gauge invariance of the support decomposition is asserted or needed for this norm statement.

## 6. Local gauge invariance on the continued domain

The chosen retained sector is covariant under small real coarse gauge transformations. This is a property to verify, not a consequence of analytic continuation alone.

Let k be a small real site gauge at the final centers, and lift it to the current sites by making it constant on each final R-block. If Vstar(W) has P_R=1, its transform by this block-constant lift also has P_R=1 and has composite constraint W^k. The classical action is gauge invariant on the common comparison domain. Both configurations are constrained minima of the action plus the absolute gauge penalty. Uniqueness of the small physical branch therefore gives

    Vstar(W^k)=Vstar(W)^(block-constant k)                (6.1)

on a neighborhood of the identity. The relative retained chart transforms by source-endpoint adjoints because the constraint is covariant, the pivots are unchanged and the retained data determine its small solution uniquely.

On real fields these adjoints are orthogonal for the chosen color norm. They preserve the actual product link/color-ball window and have unit absolute retained-coordinate Jacobian. The original link Haar/delta formula, or equivalently all of its exact pulled-back factors, therefore gives equality of the small-field integral at W and W^k on the common near-origin domain. The inherited equality here is a total-functional equality using its stipulated compatible branch. It is not an equality of individual activity coefficients.

By (2.2), the extracted classical action is gauge invariant there as well. Since the Gaussian theorem supplies a nonzero integral and its analytic logarithm on the whole product ball, differentiating this real identity gives the coarse infinitesimal gauge Ward identity for E_next near the origin. Its coefficients are holomorphic functions of w. The holomorphic identity theorem on the connected finite-volume product ball extends that infinitesimal identity throughout ||w||<b. It integrates to invariance along any sufficiently small gauge path whose transformed backgrounds remain in that ball.

This does not assert equality between arbitrary endpoints whose connecting gauge path leaves the domain. Nor does it identify the continued germ with a global density without the orbit/measure hypothesis in Section 2. Vacuum normalization changes none of these statements.

## 7. What the theorem establishes, and what it does not

The input and output analytic angle radii are identical. The potentially noncontracting rooted physical background is handled using an actual pre-gauge representative inside the old ball, and the inherited coefficient cost is controlled by local core plus a small supported tail. All new classical and measure coefficients are substituted into w before Gaussian integration. Thus the newly generated Gaussian logarithm does not incur a second generic stationary transport or a second field-radius loss.

The output remains in the same connected-carrier weight a0, with constants independent of M and compatible finite volume. The construction is a local holomorphic one-step map; where a gauge-orbit current density representation is actually available it is the exact chosen small-field macro integral, and otherwise it is the verified continuation of that integral's local germ.

The amplitude estimate contains C_T epsilon rather than a contraction. No cancellation of vacuum, relevant or marginal jets has been used except an optional field-independent normalization. A repeated quantum theorem still needs a stable extraction/coupling scheme, a controlled activity recursion, large-field and mixed-history contributions, compatible global measure identities, and observables/continuum limits. This result does not supply those by invoking analyticity or gauge invariance.
