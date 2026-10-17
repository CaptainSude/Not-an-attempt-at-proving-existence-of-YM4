# Actual joint background/fluctuation support family for the composite macrostep

17 October 2026. Research proof using the completed local composite geometry and the already audited pre-gauge supported representative. This supplies the joint-family input of `inherited_joint_core_tail_research.md`. All identities are on finite compatible regulators. Primitive ratio ell is fixed, R=ell^s is a fixed macro ratio, preceding refinement M=ell^k is arbitrary, and auxiliary grouping J is chosen later. Constants may depend on the fixed ell,R and support reserves, never on M or volume. No quantum amplitude contraction is asserted.

## 1. The known pre-gauge family and the local Banach fibers

Use the final unit graph, whose cells are R-blocks of the current lattice. A fiber at i consists of all positively oriented current link potentials whose initial sites lie in that R-block, with the maximum of their fixed color-coordinate norms. This is a finite-dimensional Banach fiber with dimension of order d R^d dim g. Crucially its norm is a maximum, not a sum over those current links.

The proved pre-gauge ordinary partial average has a strict family

    a_p,i(w)=sum_X a_(i;X)(w_X),
    sup_i sum_X exp[kappa0 tau({i} union X)+A |X|]
                    ||a_(i;X)||_b <= C_A b/R.             (1.1)

For any prescribed finite A, kappa0>0 and C_A can be fixed at the primitive ratio ell before choosing s. Its domain radius is uniform in s,k and volume. The complete output-fiber maximum is inside the support sum. Every coefficient vanishes at w=0. The scalar field w has the final coarse link coordinates; grouping them below does not change their componentwise radius b.

For an independent current potential a in a small product ball, define

    V(a)=exp(ia),
    u(a;y)=1,  u(a;x)=P_R(V(a);y,x),
    Vstar(a)=V(a)^u(a).

The actual composite retained chart Phi_(Vstar(a)) exists on a fixed R-dependent complex product ball. Define the local map

    Omega_R(a,zeta)(b)
      =log[ exp(i Ad_(u(a;b_-)^-1)
                       Phi_(Vstar(a))(zeta)(b)) exp(ia(b)) ]/i,
    Delta_R(a,zeta)=Omega_R(a,zeta)-a.                    (1.2)

All group products, logarithms and chart equations here are the actual specified maps. By construction

    Omega_R(a,0)=a,  Delta_R(a,0)=0.                      (1.3)

This construction does not assume a is stationary. Gauge zero of Vstar(a) follows from P_R covariance; its composite constraint is F_R(V(a)). Stationarity is used only when a=a_p(w) to identify the physical branch.

## 2. Exact finite range in the fluctuation variable

The output at a nonpivot link uses zeta only at that retained link. Its background dependence consists of the link background and the rooted endpoint gauge, which is internal to its R-block. A selected pivot output solves one composite equation and reads retained variables and background links in the two endpoint R-blocks. The gauges used to form Vstar on those links are themselves internal to those same blocks. Thus the whole output fiber at root i depends on a and zeta in a fixed finite set N(i) of neighboring R-blocks.

With the positive-oriented initial-site assignment one may use the root block and its outward neighbors. To avoid orientation conventions, fix the conservative radius-two graph neighborhood N(i)=B_2(i); it contains every required block. Put N0=sup_i |N(i)| and r0=2. These constants depend only on dimension, not on M,R or volume, with repeated periodic labels counted if necessary. In particular no long-range dependence on zeta is created by the stationary background's remote w-dependence.

The map (1.2) is bounded holomorphic from the local a-fibers and retained zeta-fibers to the whole output fiber. There are rho_R>0 and C_R^loc such that

    ||Delta_R(a,zeta)_i|| <= C_R^loc ||zeta|N(i)||_infinity
      for ||a|N(i)||<rho_R, ||zeta|N(i)||<rho_R.           (2.1)

To prove the linear factor, take the local analytic map on a slightly larger polydisc, use (1.3), and integrate its zeta derivative along t zeta. Uniform finite-dimensional Cauchy bounds give that derivative bound. The output maximum over all current links is retained throughout. Fixed R permits constants depending on R; no sum over M-refined variables enters the map at all.

## 3. Dimension-independent Taylor substitution in the local background fibers

Fix zeta in the above local ball. Expand Delta_R in its local Banach background input a:

    Delta_R(a,zeta)_i=sum_(n>=0) V_(i,n)(zeta)[a,...,a],
    V_(i,n)=D_a^n Delta_R(0,zeta)_i/n!.

Scalar radial Cauchy bounds the diagonal homogeneous polynomial by C_R^loc ||zeta|| rho_R^(-n). Complex polarization gives, after a harmless radius shrink,

    ||V_(i,n)(zeta)||_multilinear
      <= C_R^loc ||zeta|| (e/rho_R)^n.                    (3.1)

The elementary polarization factor n^n/n! is at most e^n. This is a Banach-space estimate; it does not sum the R^d current coordinate directions. The coefficients are holomorphic in zeta and vanish at zeta=0. The zeroth coefficient V_(i,0)(zeta)=Delta_R(0,zeta)_i is generally nonzero for nonzero zeta.

Decompose each input slot over its at most N0 neighboring fibers, then substitute (1.1) into every slot. Assign to a resulting term the union X of its background supports, leaving intermediate neighboring roots as Steiner vertices. The joining inequality is

    tau({i} union union_l X_l)
       <=sum_l [tau({j_l} union X_l)+d(i,j_l)],
    |union_l X_l|<=sum_l |X_l|.                           (3.2)

Consequently the absolute rooted family norm of the degree-n terms is at most

    C_R^loc ||zeta|| [ e N0 exp(kappa0 r0)
                              (C_A b/R)/rho_R ]^n.       (3.3)

Choose b, once R and A are fixed, so that the bracket is at most 1/2. Summing all n gives a strict family

    Delta_R(a_p(w),zeta)_i=sum_X d_(i;X)(w_X,zeta|N(i)),
    sup_i sum_X exp[kappa0 tau({i} union X)+A|X|]
                         ||d_(i;X)|| <= C_R ||zeta||,     (3.4)

where C_R=2 C_R^loc is enlarged if needed for the fixed norms. The complete output-fiber maximum is inside this support sum. No interchange of a supremum and an all-order coefficient sum is used: (3.3) bounds each degree separately by one geometric majorant.

The empty support coefficient from n=0 is included and reads the local zeta variables. It is independent of w but is not a vacuum constant. Every d_(i;X) vanishes when zeta=0, because all V_(i,n)(0) vanish. Deterministic choices of support grouping and joining trees are fixed before choosing zeta, lambda or the fields.

## 4. The actual lambda family and its absolute amplitude

Let xi range over the actual product of retained link/color balls of radius T. Define zeta=lambda g xi and

    f_lambda(w,xi)=Omega_R(a_p(w),lambda g xi).            (4.1)

This is exactly the pre-gauge argument of the inherited insertion from the integral note. Combining (1.1),(3.4),

    ||a_p||_(kappa0,A;b) <= C_A b/R,
    ||f_lambda-a_p||_(kappa0,A;b,T)
                       <= C_R |lambda| |g|T,             (4.2)

on the common fixed classical domain. The supremum includes the real cutoff values of xi; in fact the same local estimates hold on the corresponding small complex zeta-polydisc. Every output-root coefficient reads xi only in N(i), independently of its possibly distant w-support X.

Fix the finite reserve A before R. Choose R>=8 C_A and then a sufficiently small b satisfying the original pre-gauge domain and (3.3). Require

    Lstar=b/(8 C_R |g|T)>=2,
    Lstar |g|T < rho_R.                                  (4.3)

The latter is another fixed upper bound on b. On |lambda|<Lstar the absolute whole-family norm of f_lambda is at most b/4. Hence every truncation by its w-support labels has actual component amplitude at most b/4. This conclusion uses the absolute family estimate, not cancellation in the full field.

At lambda=0 the family is exactly the original a_p family and is independent of xi. The difference family is zero termwise. Thus the later canonical activity expansion can also be chosen xi-independent at lambda=0; no false vacuum subtraction of local fluctuation terms is required.

The lambda disc and these estimates are uniform in M and volume. They do not compare activity amplitudes at different RG scales.

## 5. Local core, supported tail, and the actual macro xi collar

Take kappa_t=kappa0/2 and choose an integer ell_tail>=0. In each rooted family f_(lambda;i;X), put all X contained in B_(ell_tail)(i), including X empty, in the core. The remainder is the tail. Its stronger-to-weaker exponential estimate is

    sup_i sum_(X not subset B_ell(i))
      exp[kappa_t tau({i} union X)+A|X|] ||f_(lambda;i;X)||
        <= (b/4) exp[-(kappa0/2) ell_tail].              (5.1)

The core has actual component amplitude at most b/4. All core and tail terms still read xi only in N(i). This xi dependence does not grow with ell_tail or with the distant support X.

Group the final unit/source roots into centered odd J-blocks. These are Gaussian integration macrocells of physical side JR current units, and J-blocks of the next current lattice. Choose compatible tori and, conveniently, J=ell^j. Current quantum carriers are J-blocks of the current lattice; their projection to Gaussian JR macrocells has ratio R and fiber R^d. Both tilings refine their common centered JR tiling.

For a fixed desired macro tail exponent kappa, the projection inequality

    tau_macro({rho_J i} union rho_J X)
       <= 2 tau_unit({i} union X)/J+d|X|

is paid if 2kappa/J<=kappa_t and A>=d kappa. Summing the at most J^d old output roots before the macro output maximum gives the safe tail norm

    s_tail <= J^d (b/4) exp[-(kappa0/2)ell_tail].          (5.2)

Each old J-current input fiber is a restriction of the containing whole JR Gaussian macro output fiber. Thus it inherits (5.2) rooted at its projected macrocell. This is the actual fiber relation; it introduces no additional input-coordinate sum.

Suppose ell_tail+r0<=J. For a macro output root I, all projected core w-dependencies and its entire xi collar lie in a fixed neighbor halo of I. Use the conservative coordinatewise two-neighbor halo. For a connected old carrier H define

    K0(H)=N_(infinity,2)(pi_R H).

It is connected, contains all the core dependencies and all xi dependencies of every tail term for outputs in H, and satisfies

    |K0(H)|<=5^d |pi_R H|,
    K0(H) subset N_(graph,2d)(pi_R H).                    (5.3)

Here using the entire halo only enlarges the declared support and is allowed. It proves the joint-support hypothesis explicitly: a tail coefficient with background label X reads w on X and xi only in K0(H). It does not read xi on a distant background support.

The usual connected-carrier compression gives

    |pi_R H|<=2^d+(2^d/k_R)|H|,
    k_R=1+floor((R-3)/4).

Thus the core/tail theorem has c0=5^d 2^d, c1=5^d 2^d/k_R, h0=2d and F=R^d. Its component margin can be m=b/2, since the core amplitude is at most b/4. Its input scalar-coordinate count is the actual old quantum-cell value D(J)=d J^d dim g, not the retained Gaussian dimension.

## 6. Consistent parameter order and the anchored increment

Fix a target exponent B dominating 4+log Kcal_theta+kappa_G by a bound independent of the later R,J choices, and fix a positive delta. For example kappa_G=2, m_G=3 and the eventual choice theta=1/(4D_G) give log Kcal_theta<=5/8 for every Gaussian block dimension, so B=53/8 can be fixed now. The eventual dimension changes theta, not this target B. Pick a desired macro tail exponent kappa>=B+delta, and fix A>=d kappa in (1.1) **before** choosing R. Then C_A and kappa0 are fixed at primitive ell. Choose R=ell^s so large that

    R>=8 C_A,
    (5^d 2^d/k_R) B <= a0/2.                             (6.1)

Choose J=ell^j large enough for 2kappa/J<=kappa0/2 and the other classical/Gaussian regrouping conditions. Let ell_tail=c log J plus a fixed offset, with c>4d/kappa0. Then ell_tail+r0<=J eventually, while

    D(J) (s_tail/m)
       <= (d dim g/2) J^(2d)
                      exp[-(kappa0/2)ell_tail] -> 0.      (6.2)

Increase J and its fixed offset if necessary to have s_tail/m<=1/2 and D(J)log[1/(1-s_tail/m)]<=a0/2. These choices are independent of b, because the tail-to-margin ratio cancels b. Now choose b once below all classical and chart bounds, including (3.3) and (4.3), and finally choose |g|T small enough for Lstar>=2 and the interaction budget.

All hypotheses of the joint core/tail lemma are now supplied by the actual map (4.1). For input activity norm epsilon, its canonical connected coefficient family U_(K,lambda) obeys

    sup_z sum_(K contains z) exp(B|K|)||U_(K,lambda)||
       <= C_T epsilon,
    C_T=exp[B 5^d 2^d+delta(2d)] R^d S_delta.

The same carriers are used throughout the lambda disc. Banach-valued Cauchy therefore gives

    ||U_1-U_0||_B <= C_T epsilon/(Lstar-1)
       <= 16 C_T C_R (|g|T/b) epsilon.                    (6.3)

The second inequality uses Lstar>=2. The exact multiplier norm is at most exp(q)q, with q the first bound in (6.3). These are strict joint (w,xi) carriers on the Gaussian macro graph and satisfy the full target weight B. They are not merely extensive total-functional estimates.

The lambda=0 total is the separately retained background functional E(a_p(w)). It obeys the same stronger carrier bound here and has no xi dependence with the chosen decomposition. It is not removed as a vacuum unless its scalar value is explicitly subtracted. Since B is stronger than the inherited target a0, this background term can be kept in the same activity class.

## 7. Scope

This proves the actual joint-family input and the resulting anchored inherited increment for the chosen composite one-shot macrostep, conditional only on the separately proved composite local chart, the existing pre-gauge supported representative, and the stated input inherited activity/gauge-invariance hypotheses. No fine-coordinate l1 counting, inverse mesh factor, or assumption of a rooted 1/R angle contraction is used.

Purely classical stationary-substituted precision and base multipliers must also be placed in strict joint/background carrier norms on this graph before invoking the Gaussian theorem. They have independent classical radii and arbitrary finite support reserves, but that integration interface still has to be assembled explicitly. The exact finite-regulator identity and its pre-gauge continuation are in the companion integral note. Uniform nonvanishing follows only after all cluster budgets are met.

This common-domain estimate is a finite-step result. Its constants can be extremely large, and the activity update is not contractive. It does not prove a running-coupling induction, relevant/marginal extraction, the large-field complement or a continuum Yang--Mills measure.
