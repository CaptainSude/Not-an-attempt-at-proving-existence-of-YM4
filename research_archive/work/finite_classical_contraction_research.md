# Finite-regulator classical contraction after exact full-reference extraction

17 October 2026. Research proof for independent audit. This note closes the finite-torus version of the classical contraction estimate, using the already audited finite Ward extraction, actual finite classical background, and complete-field support estimates. It does not replace the actual finite classical reference by a canonical infinite-volume periodization. It does not prove a coupling trajectory or an indefinitely iterable quantum estimate.

## 1. Scales, spaces, and established inputs

Fix dimension four, a compact simple gauge group with the previously fixed real color coordinates, a primitive odd ratio ell, and 0<alpha<1. A finite number of simple factors is handled by the corresponding finite vector of reference coefficients. The one-reference notation below is for a simple group.

Fix the activity exponent a0>0 and an auxiliary grouping J. An endpoint ratio L is an allowed primitive power, and can in particular be L=R^q for a previously fixed macro ratio R. Write

    P=L N.

Here P is the INPUT current-unit torus period and N is the OUTPUT current-unit torus period. Both tori are cubic and compatible with every partition used; in particular J divides N. The preceding homogeneous depth M is arbitrary among the allowed primitive powers. All assertions are uniform in M and compatible N above a fixed threshold. Constants may depend on the fixed group, ell, alpha, a0 and J. The leading constants will be fixed before L and before the small analytic radius b.

For a torus of current period Q, let A_(Q;a0,b) be the Banach space of families indexed by nonempty connected carriers H in its J-cell graph, with

    ||E||_(Q;a0,b)
       =sup_i sum_(H contains i) exp(a0|H|)||E_H||_b.       (1.1)

The norm on a coefficient is its supremum on the complex scalar-coordinate b-polydisc. A declared carrier may include variables that the coefficient does not read. The normalized total is

    Phi_E(A)=sum_H [E_H(A|H)-E_H(0)].                     (1.2)

There are finitely many carriers and coordinates at each regulator. Quotient by equality of (1.2) on the full polydisc, and denote its norm by ||[E]||_(Q). This is a Banach quotient: the kernel is closed under the continuous finite-volume evaluations. We work on its closed subspace whose totals obey the established local gauge, translation, hypercubic and global color identities. Reality specifies a real form but is not needed for the norm estimates. A representative of an invariant class need not have invariant individual coefficients.

The following are inputs already proved in the indicated work notes and notebooks.

1. **Finite total kernels and finite Ward extraction.** For n=2,3,4, derivatives K_(n,Q)=D^n Phi_E(0) have, at a fixed mu=mu(J)>0,

       sup_(b1) sum_(b2,...,bn)
          exp[mu D_Q(b1,...,bn)] |K_(n,Q)(b1,...,bn)|
          <= C_n(J)b^(-n)||E||_(Q;a0,b).                (1.3)

   D_Q is the maximum pairwise torus l1 distance of bond midpoints, and all internal indices are summed. This is fixed-order coordinate Cauchy followed by the connected-carrier bound D_Q<=C J|H|; the fixed polynomial number of degree-n coordinates is absorbed by part of exp(a0|H|). It does not introduce a volume factor. The exact finite Ward equations and the symmetric short-lift estimates are in finite_volume_ward_extraction_research.md.

2. **Actual finite classical references.** S_(M,Q) is the normalized homogeneous classical action at preceding depth M, on the current torus Q. It has zero value and first derivative at zero, the same total symmetries, and strict connected reference families on one fixed radius rho, uniformly in M,Q. Its flat Hessian is the exact relative periodization of q_M; the latter has a uniform exponential kernel bound and midpoint Maxwell coefficient one. These are the flat locality and classical support results, not a supposition about a subsequential limit.

3. **Actual pre-gauge background and exact action identity.** The finite ordinary construction gives an analytic map a_(M,L,N)(w), from output current fields on T_N to input current angles on T_P, with a(0)=0. It is the partial ordinary average of the full ML-refined ordinary minimizer. The exact finite minimum comparisons and gauge invariance give

       S_(M,P)(a_(M,L,N)(w))=S_(ML,N)(w).              (1.4)

   Both sides are normalized to vanish at zero. In dimension four there is no extra dimensional prefactor. For real fields this is the two-minimum identity; the identity on the common complex small domain follows analytically. It does not identify quantum cutoff integrals.

4. **Coherent complete-field support family.** Given a fixed finite cardinal reserve A, the actual finite a has one global coefficient assignment whose restrictions to overlapping final-unit collars agree. With h=L^(-1),

       a|_i=sum_(X nonempty) a_(i,X)(w_X),
       a_(i,X)(0)=0,
       sup_i sum_X exp[kappa tau_N({i} union X)+A|X|]
                    ||a_(i,X)||_(complete C^(1,alpha);b)
                    <= C_* b/L.                       (1.5)

   The norm includes the entire current-field output fiber and its physical first-gradient Hölder quotients before the support sum. The collar can be enlarged once by a fixed physical amount. Constants kappa,C_* and a permissible radius are uniform in M,L,N. This is pregauge_holder_prefix_research.md and the classical support construction. Periodic fields use their consistent periodic lifts; tau_N is torus graph Steiner length.

5. **Fifth-order transport.** The supported pre-gauge construction transports a coefficientwise order-at-least-five family on the same b,a0 spaces with norm

       ||T_high E||_(N;a0,b)<=C_high ||E||_(P;a0,b)/L,  (1.6)

   where C_high=C0(8 C_A)^5 is independent of M,L,J,N once the fixed classical reserves are chosen. This is high_jet_background_transport_research.md. Its radius requirement is b Lstar<=r_A, Lstar=L/(8C_A), with Lstar>=2. The fixed J must meet the already stated tail and projection budgets.

The choices below strengthen the existing J and L inequalities if necessary. No arbitrary finite kernel is assumed to satisfy exact infinite lifted moments.

## 2. Uniform finite-reference projection

The uniform reference representation on radius rho can be made O(b^2) without assuming coefficientwise vanishing of the linear sector. Remove each coefficient's homogeneous degrees zero and one. The sum of the linear terms is zero because D S_(M,Q)(0)=0, and the constants vanish in (1.2). If the rho-radius family norm is at most M_S, the phase projections give, for 0<b<=rho/2,

    ||S_(M,Q)^(>=2)||_(Q;a0,b)
       <= M_S (b/rho)^2/[1-b/rho]
       <= C_S b^2,             C_S=2 M_S/rho^2.         (2.1)

C_S is independent of b,M,Q. This is a change of representative of the same normalized total.

For Q>=64, form the symmetric short lift of its quadratic kernel with cutoff floor(Q/16), and denote the lifted midpoint Hessian by Gamma_(2,Q). For distinct directions mu,nu put

    b_Q(E)=(1/2) partial_(p_nu)^2
                              Gamma_(2,Q;mu mu)^E(0).  (2.2)

The fixed invariant color normalization is understood. Hyperoctahedral symmetry makes the distinct pair immaterial. The flat reference identity gives

    |b_Q(S_(M,Q))-1|<=C(J) exp[-c(J)Q],                 (2.3)

uniformly in M. The comparison includes both the discarded infinite q_M tail and images of that tail folded into short torus displacements; it is not obtained merely from a limiting normalization. Increase a fixed Q0(J) until the denominator has modulus at least 1/2. Define the finite functional and projection

    beta_(M,Q)([E])=b_Q(E)/b_Q(S_(M,Q)),
    P_(M,Q)[E]=[E]-beta_(M,Q)([E])[S_(M,Q)].             (2.4)

The kernel derivative is determined by the normalized total, so this is well defined on the quotient. Kernel estimate (1.3), with a second spatial moment, gives

    |beta_(M,Q)([E])|<=C_beta(J)b^(-2)||[E]||_(Q).

Consequently

    beta_(M,Q)([S_(M,Q)])=1,
    P_(M,Q)^2=P_(M,Q),
    ||P_(M,Q)||<=C_ext(J):=1+C_beta(J) C_S.              (2.5)

This bound is independent of b,M,Q. It is the combined projection, not beta by itself, that is uniform in b.

Classical substitution defines a scalar linear map

    T_(M,L,N) Phi_E(w)=Phi_E(a_(M,L,N)(w)).              (2.6)

For sufficiently large L and sufficiently small b, ||a(w)||<b uniformly, so equality of finite normalized totals implies equality after substitution. The localization proved below supplies a bounded output representative.

Here is the finite-domain justification that T maps invariant classes to invariant classes. For a real output field and its sufficiently small local gauge transform, the two minimum comparisons give an actual connecting fine gauge close to the identity, by the already proved finite transfer and gauge-flow construction (the finite part of classical_summable_gauge_research.md). Both endpoint input angles have size at most rho0=C_A b/L. If V^g=U, the exact bond equation bounds the gauge edge increments by C(|U-I|+|V-I|). On the fixed near-identity logarithm chart it follows that |D log g|<=C rho0. The actual connecting gauge itself stays in this chart; no inference from its edge increments alone is needed. Therefore the whole real path exp(t log g), 0<=t<=1, transforms V into fields of scalar-coordinate size at most C_g rho0. Fixed conversions between the invariant matrix norm and the scalar color maximum norm are included in C_g. Choose L>C_g C_A with a strict margin. Every point of this path then lies inside the input b-domain, so the input local Ward identity integrates along it and gives equality of the two substituted totals. On a finite torus there is no gauge truncation or constant-at-infinity issue. Holomorphic continuation gives the local output Ward identity on the connected complex domain. The same finite minimum comparisons, or exact covariance where available, handle translations, signed permutations and global color transformations, with the same small-domain margin. Thus no unproved endpoint-only extension of gauge invariance is used.

From (1.4),

    T_(M,L,N)[S_(M,P)]=[S_(ML,N)],
    P_(ML,N) T_(M,L,N) P_(M,P)
                     =P_(ML,N) T_(M,L,N).              (2.7)

The second identity does not say that T preserves the beta-zero subspace. The output projection remains essential.

## 3. Graded short-lift errors for an extracted input

Let [F] have beta_(M,P)([F])=0. Choose an arbitrary representative with norm at most epsilon, as close to its quotient norm as desired. It need not be carrierwise invariant. Its total is invariant and its kernels satisfy (1.3).

Set T0=floor(P/16). On infinite bond tuples define

    Ktilde_n(b1,...,bn)
      =K_(n,P)(b1 mod P,...,bn mod P)
                    1{D_infinity(b1,...,bn)<=T0}.       (3.1)

This lift preserves slot symmetry, hypercubic and color covariance, reality when present, and midpoint parity. Relative periodization gives exactly

    K_(n,P)=Per_P Ktilde_n+Ktail_n,
    Ktail_n=K_(n,P) 1{D_P>T0}.                          (3.2)

Indeed a short tuple has a unique lift with its first bond fixed, and its pairwise lifted distances equal its torus distances. All fixed moments of the tail are bounded by

    C(J,m) epsilon b^(-n) exp[-c(J)P].                 (3.3)

The finite Ward operators are finite combinations of one-bond shifts, coincident-slot insertions and fixed color commutators. They commute with periodization. Their lifted defects have diameter at most T0+2, so relative periodization is injective on their support. The exact torus Ward identity therefore bounds the infinite lifted defect by the tail bounds.

It is important to keep the field-degree grading. Take b<=1. In the degree-n Ward equation, n<=4, only kernels of degrees 2,...,n occur. Hence its fixed-moment defect is bounded by

    delta_n=C(J) epsilon b^(-n) exp[-c(J)P], n=2,3,4.   (3.4)

The degree-two defect uses only K2. The cubic defect and its coefficient elimination use K3 and the already bounded K2 jets; both are bounded by delta_3 because b<=1. The quartic elimination similarly uses degrees at most four and is bounded by delta_4. Using a single degree-four bound for every degree would lose spurious powers of b and is not done.

The finite-dimensional Ward coefficient algebra now gives:

* every short-lift midpoint Hessian jet through momentum degree three is O(delta_2);
* every cubic short-lift jet through momentum degree one is O(delta_3);
* the quartic short-lift value at zero is O(delta_4).

Here b_P(F)=0 exactly by extraction. To recall the algebra, the Hessian has mass m and quadratic coefficients a,b,c in its hypercubic form. The Ward defect bounds m and, since b=0, bounds a,c by delta_2. Odd midpoint degrees vanish by parity. For the cubic linear polynomial A p+B q, the degree-two Ward identities make the independent p_mu q_sigma coefficients B small and then the q_nu p_sigma coefficients A small. The quartic leading Ward equation contracts its constant tensor with an arbitrary gauge momentum, and bounds that tensor by the cubic-linear and Hessian-mass errors. All inversions here are fixed finite-dimensional coefficient comparisons.

Multiplication by the fixed analytic midpoint phases and passage from p to z=exp(ip) preserve these finite-order bounds, with constants depending only on the fixed number of legs and directions. Thus the same orders of tail-coordinate Laurent jets are bounded by delta_n. Midpoint displacements and tail-coordinate displacements are not identified without these phase factors.

## 4. A bounded finite-range repair of the small jets

Anchor the first positive-bond tail at zero, retaining every internal tensor index, and let F_n(z) be the tail-coordinate Laurent symbol of Ktilde_n in d(n-1) independent variables. Put

    m_2=3,              m_3=1,              m_4=0.

Take the finite Taylor polynomial at the identity

    J_(m_n) F_n(z)
      =sum_(|gamma|<=m_n)
          [(partial_z^gamma F_n)(1)/gamma!] (z-1)^gamma. (4.1)

Its coefficients are O(delta_n). Its Laurent kernel R_n^raw has a fixed finite relative range depending only on d,n,m_n, and its absolute row norm is at most C delta_n.

Symmetrize this kernel over its n slots, translating the first slot back to the anchor after each permutation. This is an average of at most n! finite-range kernels; each translated relative range remains bounded by a fixed multiple of the original range, and its norm is still at most C delta_n. Denote the result by R_n. The corrected kernel

    Khat_n=Ktilde_n-R_n                                 (4.2)

retains slot symmetry and has exactly zero jets through degree m_n. To verify the last assertion, Ktilde_n is slot symmetric, while the residual from each transformed Taylor subtraction is a composition of F_n-J_(m_n)F_n with an analytic monomial change of the independent z variables that fixes z=1, possibly with a harmless analytic phase. Such a composition still vanishes to order m_n+1. Averaging preserves that order. No new uncontrolled low jets are introduced by reanchoring.

Reality and global color covariance are retained. Point symmetry is unnecessary for the subsequent spatial estimate; if desired it can be restored by another fixed finite average, using the same vanishing-order argument.

After decreasing an exponent sigma(J)>0 once, the corrected kernels obey

    sup_(first index) sum_(remaining indices and r's)
       exp[sigma sum_(j>=2)|r_j|] |Khat_n(0,r_2,...,r_n)|
       <= C(J) epsilon b^(-n),                         (4.3)

uniformly in P,M. They have the exact tail-coordinate moments needed by the spatial theorem: all Khat2 jets through degree three vanish; the constant and first moments of Khat3 vanish; the constant moment of Khat4 vanishes. The correction obeys

    ||R_n||_(absolute row)<=C(J) epsilon b^(-n)
                                      exp[-c(J)P],     (4.4)

with fixed finite range. Most importantly, the following is an exact finite polynomial identity:

    (1/n!) K_(n,P)(a,...,a)
      =(1/n!)(Per_P Khat_n)(a,...,a)
       +(1/n!)(Per_P R_n)(a,...,a)
       +(1/n!)Ktail_n(a,...,a).                        (4.5)

The correction and wrapping tail are retained and localized below. They are not separately claimed to satisfy Ward identities.

## 5. The spatially canceled estimate works directly on a finite torus

We prove the needed extension of low_kernel_spatial_transport_research.md, rather than assuming that the actual finite background is periodized from an infinite one.

For an infinite relative kernel Khat_n, evaluate

    (1/n!) sum_(x in T_P) sum_(r_2,...,r_n in Z^4)
                  Khat_n(r_2,...,r_n)
                    [a(x),a(x+r_2),...,a(x+r_n)],      (5.1)

with the arguments read periodically. This is exactly the polynomial of Per_P Khat_n. Its lifted kernel sums are absolutely convergent by (4.3). Repeated torus slots are counted with their ordinary multilinear multiplicity.

For the quadratic kernel let F(z)=sum_r Khat2(r)z^r. The ordered removable divided differences

    B_j F(z)=
      [F(1,...,1,z_j,...,z_d)
       -F(1,...,1,1,z_(j+1),...,z_d)]/(z_j-1)

give F-F(1)=sum_j(z_j-1)B_j F. A Laurent monomial contributes at most |r_j| divided-difference monomials, each with exponent length at most |r|. Thus the combined row Wiener norm loses at most [e(sigma-sigma')]^(-1). Since F vanishes through degree three, apply the formula twice and set

    Htilde_(rho,tau)(z)=-z_rho B_tau B_rho F(z).

Then

    F=sum_(rho,tau)(z_rho^(-1)-1)
                          Htilde_(rho,tau)(z)(z_tau-1),
    Htilde_(rho,tau)(1)=0,                             (5.2)

and its combined exponentially weighted row norm is at most

    [16 exp(sigma/2)/(e^2 sigma^2)] C(J)epsilon b^(-2)

at exponent sigma/2. The sum over rho,tau is inside the row norm.

Finite periodic summation by parts is exact. Using also the zero sum of Htilde, the quadratic term in (5.1) equals

    (1/2) sum_(x in T_P,r,rho,tau)
        [D_rho a(x)]^T Htilde_(rho,tau)(r)
                   [D_tau a(x+r)-D_tau a(x)].         (5.3)

There is no boundary term and no assumption that a is summable on an infinite lattice.

For cubic terms set ell_r(x)=sum_rho r_rho D_rho a(x) and

    Rem_r(x)=a(x+r)-a(x)-ell_r(x).

Substitute this identity for both shifted fields in (5.1). Exact lifted zeroth and first moments cancel the constant and one-ell terms. The six residual terms are the two a,a,Rem terms, the a,ell,ell term, the two a,ell,Rem terms, and the a,Rem,Rem term. For the quartic polynomial, subtract the all-anchor product using the zeroth moment and telescope the three shifted factors. These are algebraic identities for periodic a with integer lifted r; they do not require a globally defined affine function on the torus.

For total displacement m=sum|r_j|<=L, use one fixed enlarged final-unit collar and the coherent complete coefficients in (1.5). With h=1/L the family bounds are

    |a|<=C b h,       |D a|<=C b h^2,
    |D a(x+r)-D a(x)|<=C b h^(2+alpha)|r|^alpha,
    |Rem_r|<=C b h^(2+alpha)|r|^(1+alpha).              (5.4)

For a negative path traversal the positive difference is evaluated at its lower endpoint; the exact discrete Taylor proof therefore applies with either sign. These are weighted sums of coefficient norms, not bounds inferred only after summing the field. Products glue the support trees and preserve the reserve since union cardinality is subadditive.

The resulting near products are bounded by C b^2 h^(4+alpha)|r|^alpha for (5.3), C b^3 h^(4+alpha)(1+m)^6 for the cubic, and C b^4 h^5(1+m) for the quartic. Their kernel sums cancel b^n and cost only fixed sigma-dependent moments.

We spell out the carrier estimate because it is needed unchanged on the torus. Project the finite set of endpoint roots and each field-factor terminal set {root} union X to final J-cells. Choose short macro connecting graphs supplied by the projection bound, and take their connected union H. It need not contain the projection of an arbitrarily chosen full fine tree. For a fixed number n0 of endpoint roots and with torus Steiner lengths,

    |H|<=1+T_H,
    T_H <= (2/J)[tau_N(roots)
                  +sum_occ tau_N({root} union X)]
                     +4[n0+sum_occ |X|].              (5.5)

All these inequalities remain valid on periodic quotients: choose shortest periodic paths, or project lifted paths, and remove repetitions. Wrapping cannot increase the number of vertices. If z belongs to H and j(x) is the final J-cell containing x/L, then

    exp(a0|H|)1_(z in H)
       <=exp(a0) exp[-dist_N(z,j(x))]
                        exp[(a0+1)T_H].               (5.6)

In (5.5), tau_N is measured on final UNIT cells; in (5.6) and (5.8), dist_N is measured on final J-CELLS. Thus their side lengths are respectively N and N/J. This convention explains both the factor 1/J in (5.5) and the current-site count (JL)^4 in (5.8).

Choose the fixed reserves and J so that

    A>=4(a0+1),       2(a0+1)/J<=kappa.                (5.7)

This pays every attached-tree/cardinality weight in (5.6). A near summand's root tree has bounded length. The final anchor sum obeys

    sum_(x in T_P) exp[-dist_N(z,j(x))]
                       <=(JL)^4 S1,
    S1=sum_(y in Z^4)exp(-|y|_1).                      (5.8)

There are exactly (JL)^4 current anchor sites per final J-cell. The torus exponential sum is bounded by S1 by choosing one shortest lattice representative per coset. This is the only extensive anchor count in the norm proof.

For m>L keep endpoints at their own roots. The root-joining tree costs at most C(m/L+1); after (5.6) its additional factor is at most C exp[C'm/(JL)]. Quadratic first differences in (5.3) give C b^2 h^4 even far apart. Cubic and quartic residuals have the rough bounds C b^3 h^3(1+m)^2 and C b^4 h^4. Choose L0 after J so C'/(JL)<=sigma/8 for L>=L0. The remaining exponential kernel tail bounds all three far contributions by

    C(J)epsilon (L+2) exp[-sigma L/8]
                     <=C'(J)epsilon L^(-alpha).       (5.9)

All roots, sums and paths here are finite-periodic or lifted relative-kernel data; no infinite-field limit was used. Regrouping normally convergent summands by H gives connected holomorphic coefficients on the same b-polydisc, with

    || sum_(n=2)^4 (Per_P Khat_n)(a,...,a)/n! ||
                       _(output activity representative)
           <=C_low(J)epsilon L^(-alpha).              (5.10)

C_low(J) is fixed before L. This is the finite version of the repaired spatial argument.

## 6. Direct localization of wrapping tails with no loss of a0

An endpoint-product lemma handles both errors in (4.5). Suppose a torus n-kernel W, n<=4, has

    sup_(first slot) sum_(other slots)
                         exp(mu D_P)|W|<=A_n.          (6.1)

For each tuple choose the first current site x as anchor and one endpoint root per remaining slot. A shortest torus path from the first midpoint to each other midpoint gives a root tree of final-unit length at most C_n(D_P/L+1). Fixed midpoint/tail offsets change only the additive constant. Insert the actual complete support families of the endpoint fields and construct the connected output carrier by (5.5).

The rerooting inequality (5.6) now adds at most

    C exp[C_n'(a0+1)D_P/(JL)].

Choose L0 larger if needed so that its exponent coefficient is <=mu/4. The product field-family norm is at most (C b/L)^n. After the anchor sum (5.8),

    || W(a,...,a)/n! ||_(output representative)
           <=C(J,n) A_n b^n L^(4-n).                  (6.2)

If W is restricted to D_P>T0, the unspent exponential in (6.1) supplies, conservatively,

    || W1_(D_P>T0)(a,...,a)/n! ||
           <=C(J,n) A_n b^n L^(4-n) exp(-mu T0/2).    (6.3)

The target exponent is exactly a0. The extra carrier length is measured after compression by JL; it is not paid by discarding part of the input activity exponent at the old scale.

Apply (6.3) to Ktail_n, with A_n<=C(J)epsilon b^(-n). Since T0>=P/32,

    ||Ktail_n(a,...,a)/n!||_(output representative)
             <=C(J)epsilon L^(4-n) exp[-c(J)P].       (6.4)

Apply the same endpoint construction to Per_P R_n. Its relative range is a fixed constant and its absolute coefficient bound is (4.4); there is no wrapping multiplicity problem for sufficiently large P, and direct relative periodization in any case counts every occurrence correctly. This gives

    ||(Per_P R_n)(a,...,a)/n!||_(output representative)
             <=C(J)epsilon L^(4-n) exp[-c(J)P].       (6.5)

Summing n=2,3,4 yields

    ||all low-degree errors||_(output representative)
       <=C_err(J)epsilon (L^2+L+1) exp[-c(J)LN].        (6.6)

Every factor b^n has canceled the corresponding graded b^(-n), including for the jet corrections. The optional old-scale tail lemma in the finite Ward note loses cardinal exponent; it is not used here. Equations (6.3)-(6.6) are a separate output-scale localization and preserve a0.

## 7. High-degree part and the actual parameter order

On each circular coefficient polydisc, homogeneous phase projection has norm at most one. Thus

    R5 E=E-sum_(n=0)^4 P_n E,
    ||R5 E||<=6||E||.                                 (7.1)

Every coefficient of R5 E vanishes through degree four. The already proved high-jet transport yields

    ||T_high R5 E||_(N;a0,b)<=6 C_high epsilon/L.       (7.2)

Its constant can be used with L=R^q chosen after the fixed J. Indeed the high-jet proof fixes the classical reserves first, then one sufficiently large base R and J with its tail cutoff. Increasing only the endpoint L decreases the core-compression coefficient c1(L); its tail budget D(J)t and its projection inequalities are unchanged. The large field-scaling disk has radius L/(8C_A), so b is then decreased to satisfy b L/(8C_A)<=r_A. No new J growing with this endpoint is needed.

The coefficientwise degree-zero sector disappears from the normalized total. The degree-one TOTAL is zero by global adjoint invariance for a simple or semisimple group. It remains zero after substituting a; no individual coefficientwise vanishing or gauge invariance is asserted for those sectors. The low-degree TOTAL polynomials are exactly (4.5). Therefore (5.10), (6.6) and (7.2) represent the entire normalized classical substitution of the extracted input.

All output sums are ordinary finite-volume analytic sums or absolutely normally convergent support/relative-kernel expansions. Their equality is an equality of the full finite normalized totals on the same b-polydisc, not merely of a finite number of kernels.

## 8. Finite quotient contraction theorem

Let N>=N0(J), with N0 large enough for (2.3), the short-lift construction and the fixed physical collars. Fix J and its tail budgets as above. There are constants C_low(J), C_err(J), c(J)>0 and C_ext(J), and a constant C_high fixed by the classical family, all independent of L,b,M,N, such that for every allowed L>=L0(J) and every sufficiently small b chosen after L,

    ||P_(ML,N) T_(M,L,N) P_(M,LN)||
       <= C_ext(J)^2 [
             C_low(J)L^(-alpha)+6 C_high/L
              +C_err(J)(L^2+L+1) exp(-c(J)LN)].        (8.1)

The operator norm is between the finite invariant quotient spaces with the same a0,b. More generally retain separate input/output C_ext constants if the fixed reference conventions differ.

Proof: apply the preceding construction to an almost-minimal representative of the extracted class. Its norm can be taken arbitrarily close to ||P_in[E]||<=C_ext||[E]||. The resulting connected output representative is bounded by the bracket in (8.1). Applying P_out costs the second C_ext. Take the quotient infimum and then let the representative error tend to zero. No norm-minimizing or canonically chosen representative is required.

Equivalently, with constants renamed,

    ||P_out T P_in||
       <=A(J)L^(-alpha)+B(J)/L
                         +E(L,J)exp[-c(J)N].          (8.2)

The sharper estimate (8.1) displays the actual input period LN and its error. In particular, for any target theta>0 one may choose the allowed finite power L=R^q, after the fixed J, to make the first two terms at most theta/2; choose a finite compatible N0 larger so that the last term is at most theta/2 for every N>=N0; and then choose b satisfying the classical domain, b<=1, b<=rho/2 and high-jet dilation restrictions. This gives a genuine theta-contraction uniform in preceding M and all such finite regulators. The geometric inequalities can be fixed first; shrinking b changes none of their constants.

By the exact identity (2.7), the same bound applies to P_out T on invariant classes, with the input extraction implicit. This telescoping uses the full actual reference and its exact finite minimum identity, not an approximate equality of Hessians.

## 9. Scope and relation to the remaining recursion

This proof uses only finite normalized totals, actual finite classical representatives, and explicit periodic spatial algebra. It requires neither a coherent infinite-volume interaction limit nor evaluation of an infinite total at a non-summable periodic field. No finite regulator is treated as having exact lifted low jets: its exponentially small defects and wrapping tail are retained in (6.6).

The result produces small finite activity representatives that are exactly equivalent, on their full polydisc, to the extracted classical output. This removes the previously separate finite-regulator CLASSICAL relocalization issue. It does not say that the actual unmodified carrier assignment was small, nor that an arbitrary raw vacuum normalization has been preserved. Vacuum constants remain a separate sector.

The constants retain their J dependence. The order J fixed, then L=R^q, then the small b is essential to the noncircular estimate. A sequence of q quantum cutoff integrals is not identified with one direct macro cutoff integral. To insert (8.1) into a finite quantum recursion one must still use the established exact finite scalar descent and verify all intermediate actual analytic and Gaussian budgets, the running coupling bounds, and the chosen cutoff/history identities. None is implied merely by the classical norm contraction.

No convergence or sign of beta_(M,Q), large-field control, nontriviality, continuum construction, or uniform-infinite-step assertion is claimed here.
