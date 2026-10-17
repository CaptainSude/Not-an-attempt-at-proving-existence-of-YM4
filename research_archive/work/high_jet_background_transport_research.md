# Contraction of the background transport after coefficientwise degree-four subtraction

17 October 2026. Research proof. This is a finite-step theorem for the inherited **background** E(a_p(w)), using the actual supported pre-gauge representative. It does not concern the fluctuation increment, prove gauge-invariant marginal extraction, or close quantum induction. The contraction is uniform in preceding homogeneous depth M and compatible volume once the finite macro ratio and auxiliary grouping are fixed.

## 1. Spaces and the exact jet condition

Fix a primitive odd ratio ell and dimension d. Let R=ell^s be the composite ratio. Old quantum carriers H are connected sets of J-blocks of the current lattice. The output graph consists of J-blocks of the next current lattice, equivalently JR-blocks of the current lattice. The projection pi_R has fiber R^d and takes connected sets to connected sets. Work on compatible original tori, for example periods 2 ell^N with N>=s+j when J=ell^j. The established connected compression gives

    |pi_R H| <= 2^d+(2^d/k_R)|H|,
    k_R=1+floor((R-3)/4), R>=5.

Let a0>0 and b>0. The input family is holomorphic on the scalar-coordinate radius-b product polydisc and satisfies

    ||E||_(a0,b)=sup_i sum_(H contains i) e^(a0 |H|)||E_H||_b <= epsilon.

Each old J-cell has D(J)=d dim(g) J^d scalar coordinates. Assume the **coefficientwise total-degree condition**

    D^n E_H(0)=0 for every H and n=0,1,2,3,4.                 (1.1)

These are full symmetric Taylor tensors in all field coordinates of H, including mixed derivatives. The condition is not merely vanishing on a one-dimensional special field family, and is stronger than cancellations in the total sum over H.

We construct a deterministic linear support transport T_(R,J) such that

    sum_K (T_(R,J)E)_K(w_K)=sum_H E_H(a_p(w)|H),              (1.2)

with connected output carriers K. The target norm is the **same activity exponent a0**, not the larger Gaussian multiplier exponent.

## 2. The supported pre-gauge input and parameter order

Fix delta=1 and a desired macro tail exponent kappa>=a0+1. Choose a finite classical cardinality reserve A>=d kappa before choosing R. The proved pre-gauge family, with whole output-cell maximum inside the support sum, gives constants C_A,kappa0,r_A>0 at the fixed primitive ell, independent of R,M and volume, such that

    a_p,i(w)=sum_X a_(i;X)(w_X),  a_(i;X)(0)=0,
    sup_i sum_X exp[kappa0 tau({i} union X)+A|X|]
                          ||a_(i;X)||_r <= C_A r/R          (2.1)

for 0<r<=r_A. The source/final-unit fiber i contains the entire current field in one R-block with its maximum norm. This is a stated established input; the 1/R is the actual pre-gauge estimate, not an assumed contraction of the rooted P_R=1 representative.

Set

    Lstar=R/(8 C_A),  Lstar>=2,
    0<b<=r_A/Lstar.                                       (2.2)

At a chosen final b, any additional classical or composite chart restrictions can also be imposed. Define

    f_lambda(w)=a_p(lambda w), |lambda|<Lstar.              (2.3)

Its absolute rooted family norm on ||w||<b is at most b/8, uniformly on this disk. Every support truncation therefore has component amplitude <=b/8 without using cancellation. Its complete family, core and tail all vanish at lambda=0 termwise.

Choose a support truncation length ell_tail. Core terms have X contained in B_(ell_tail)(i). At exponent kappa0/2 the remaining tail obeys

    ||tail||_(kappa0/2,A) <= (b/8) exp[-kappa0 ell_tail/2].  (2.4)

Group the final-unit roots by J. If 2 kappa/J<=kappa0/2, the geometric projection bound and A>=d kappa give

    s_tail <= J^d (b/8) exp[-kappa0 ell_tail/2].             (2.5)

The factor J^d comes from summing old roots before the complete macro output maximum. Each old J-current input fiber is a restriction of a containing JR macro output fiber, so no additional scalar-coordinate sum occurs at this stage.

Take ell_tail<=J and the conservative coordinatewise two-neighbor core halo

    K0(H)=N_(infinity,2)(pi_R H).

It contains all core w dependencies, is connected, and has

    |K0(H)| <= c0+c1|H|,
    c0=5^d 2^d, c1=5^d 2^d/k_R,
    K0(H) subset N_(h0)(pi_R H), h0=2d.                   (2.6)

There are no fluctuation variables in this theorem. This halo is deliberately conservative and does not need optimization.

Use component margin m=b/2. Then t=s_tail/m is bounded by

    t <= (1/4) J^d exp[-kappa0 ell_tail/2].                (2.7)

Choose R large enough for c1 a0<=a0/2. Choose J=ell^j large and ell_tail=ceil(c log J+C) with c>4d/kappa0, so ell_tail<=J and

    t<=1/2,  D(J) log[1/(1-t)]<=a0/2.                    (2.8)

This is possible because D(J)t is bounded by a fixed constant times J^(2d) exp[-kappa0 ell_tail/2], which tends to zero. Larger J required by a separate Gaussian module can be used as well, with its corresponding logarithmic ell_tail. These choices are independent of b. Thus the order is: fixed reserve and its C_A,kappa0,r_A; then R; then J and ell_tail; then b. No hidden J-dependent prefactor remains in the transport estimate below.

## 3. A uniform transport family on the large lambda disk

For each H, split f_lambda|H=c_(H,lambda)+v_(H,lambda) into its core and strict supported tail. The core depends only on K0(H) and lies at distance at least m from the boundary of the old b-polydisc. Expand

    E_H(c_lambda+v_lambda)
       =sum_nu (partial^nu E_H)(c_lambda)/nu! * v_lambda^nu.

The coefficient bound is ||E_H||_b m^(-|nu|). Substitute each tail's strict support family and attach every support to its projected input root by a deterministic minimizing Steiner graph. These choices are fixed independently of lambda. The resulting carrier K is connected. If T is the sum of added tree lengths, then

    |K|<=c0+c1|H|+T,
    z in K implies dist(z,pi_R H)<=h0+T.

The root norm with exponent kappa>=a0+1 pays the target weight and the rerooting reserve. The scalar-coordinate multiindex sum is exactly (1-t)^(-D(J)|H|). Conditions (2.8) and c1 a0<=a0/2 pay it from the original exponent a0. Rerooting costs S1 and the projection fiber costs R^d. We obtain normally convergent canonical coefficients U_(K,lambda) satisfying

    sum_K U_(K,lambda)=sum_H E_H(a_p(lambda w)|H),
    ||U_lambda||_(a0,b) <= C0 R^d epsilon,
    C0=exp[a0 5^d 2^d+2d] S1,
    S1=sum_(z in Z^d) exp[-|z|_1].                        (3.1)

The periodic sum is bounded by this same infinite-lattice sum. C0 is independent of R,J,M and volume. All R dependence in (3.1) is the explicit R^d. The construction is linear in the input family E, even though its fixed background substitution is nonlinear. Boundedness and normal convergence on smaller lambda disks give an anchored-activity Banach-valued holomorphic map U_lambda.

## 4. The fifth-order zero survives the canonical carrier decomposition

This step is stronger than knowing that the total functional has a fifth-order zero. Let q=|nu| be the tail Taylor degree in an individual canonical summand. Core and tail functions both vanish at lambda=0.

If q<=4, condition (1.1) implies that partial^nu E_H(a) has total field degree at least 5-q near a=0. Therefore (partial^nu E_H)(c_lambda) is O(lambda^(5-q)), while the q tail factors are O(lambda^q). If q>=5, those tail factors alone contribute order at least five, and the remaining derivative is holomorphic. The q=0 core term is covered by the first case. Hence every summand has lambda Taylor coefficients of orders zero through four equal to zero.

Normal convergence on smaller lambda disks permits differentiation through the sum and grouping by deterministic carriers. Thus

    D_lambda^n U_(K,lambda)|0=0, n=0,...,4, for every K,    (4.1)

and the same holds as derivatives in the anchored activity Banach space. No cancellation between distinct carriers is invoked. The output functions have field jets through degree four zero as well: every summand is formed by the same analytic operations on a_p(w), whose support coefficients vanish at w=0.

## 5. Banach Schwarz gives the contraction

An elementary Banach-valued generalized Schwarz lemma states: if a holomorphic F on |lambda|<L is bounded by M and has derivatives of orders 0,...,p-1 zero at zero, then

    ||F(lambda)|| <= M (|lambda|/L)^p.                    (5.1)

For a proof, F(lambda)/lambda^p has a removable singularity at zero. On each circle of radius rho<L, its norm is at most M/rho^p. The maximum principle applied to every bounded linear functional gives the same interior norm bound; send rho to L. This avoids the extra geometric-series factor in a coefficient-by-coefficient Cauchy estimate.

Apply (5.1) with p=5 to (3.1),(4.1). At lambda=1,

    ||T_(R,J)E||_(a0,b)
      <= C0 R^d Lstar^(-5) epsilon
      = C0 (8 C_A)^5 R^(d-5) epsilon.                    (5.2)

In d=4 this is

    ||T_(R,J)E||_(a0,b) <= C0 (8 C_A)^5 epsilon/R.         (5.3)

Therefore, for any desired 0<q_contr<1, choose a sufficiently large power R=ell^s, in addition to the earlier compression conditions, with

    R >= C0 (8 C_A)^5/q_contr.                            (5.4)

Then the background transport is a genuine q_contr contraction on the coefficientwise fifth-order ideal. R is chosen before J and b, and the latter choices do not change this contraction constant. The output again belongs to that same coefficientwise ideal. The estimate is uniform in old M and compatible regulator volume.

The constants are enormous: for d=4 and a0=1/16, C0=exp(633) S1 using this conservative halo. No practical scale estimate is claimed; the theorem only requires a finite choice. The Gaussian interaction theorem uses a different, larger exponent. Formula (5.3) concerns transport of the inherited background only, not the new quantum correction or the fluctuation difference.

## 6. Degree-four subtraction itself is bounded without dimension loss

On a circular product polydisc define the total homogeneous Taylor projection

    (P_n E_H)(a)=(1/(2pi)) integral_0^(2pi)
                        exp(-int) E_H(exp(it)a) dt.       (6.1)

It equals the total-degree-n Taylor polynomial. Its support remains H and

    ||P_n E_H||_b <= ||E_H||_b.

This follows from the phase integral, without summing individual coordinate monomials. In particular it has no factor D(J)|H|. For

    R_(>=5) E_H=E_H-sum_(n=0)^4 P_n E_H,

we have the anchored norm bound

    ||R_(>=5) E||_(a0,b)<=6||E||_(a0,b).                 (6.2)

Every resulting coefficient satisfies (1.1). Hence (5.3) also gives

    ||T_(R,J) R_(>=5) E||_(a0,b)
       <=6 C0 (8 C_A)^5 ||E||_(a0,b)/R.                  (6.3)

No input-radius shrink or cardinal reserve is needed for this elementary projection. The unchanged carrier H can be retained even if a projected polynomial actually reads fewer variables. A degree-zero piece is handled separately as a vacuum when assembling a full action; the projection estimate does not identify it with a physically normalized vacuum counterterm.

## 7. What this does and does not establish

This proves a finite-step contraction for the exact background transport after coefficientwise removal of total field jets through degree four. It uses the actual pre-gauge ordinary representative and the existing support theorem, not a rooted-gauge amplitude contraction. The same incoming/outgoing b and a0 are used. Its hypothesis and conclusion concern each coefficient, not only the total functional.

The subtraction in Section 6 is not a gauge-invariant extraction scheme. Local gauge transformations act nonlinearly and affinely in a link-potential chart; total homogeneous degree is not preserved by that action. Even if the total inherited functional is gauge invariant, its low-degree part and its high-degree remainder need not be separately invariant. Individual activities need not be gauge invariant in the first place. The actual rooted/pre-gauge equality may therefore only be applied to the complete inherited functional before such a noninvariant split.

Nor do the low jets automatically lie in a finite-dimensional coupling space. They include kernels across arbitrarily many carrier geometries and distances, although their anchored norm is controlled. Classifying them by local gauge-invariant operators, separating low momentum from field degree, supplying nonlinear Ward-compatible completions, and obtaining the required marginal/relevant estimates remain open. New quantum coefficients can regenerate low jets. The contraction here does not by itself close the activity recursion, determine a beta function, control large fields or produce a continuum Yang--Mills theory.
