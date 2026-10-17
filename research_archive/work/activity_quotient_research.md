# Analytic interactions modulo equality of their normalized totals

17 October 2026. Research proof for independent audit. This constructs a complete representation quotient, proves a continuous Maxwell coefficient and bounded full-reference extraction, and states a precise conditional classical contraction. It concerns infinite analytic interactions. It does not define a quantum update on the quotient or prove that such an update descends.

## 1. The activity Banach space

Fix the infinite current lattice, a partition into cells of side J, a finite number D of scalar field coordinates per cell, a cardinal exponent a>0, and a radius b>0. The scalar-coordinate maximum norm is used. Let C be the countable collection of nonempty finite connected sets of cells. A declared carrier H may be larger than the variables actually read by its coefficient.

For H in C let H_b(H) be the Banach space of bounded holomorphic functions on the open complex polydisc of radius b in the D|H| coordinates of H, with its supremum norm. Define

    A_(a,b) = {E=(E_H):
       ||E||_(a,b):=sup_i sum_(H contains i)
                         exp(a|H|)||E_H||_b < infinity}.       (1.1)

No invariance of individual coefficients is imposed. Constant functions are allowed. Every estimate below retains dependence on the fixed J,D,a. A fixed different number of coordinates in each cell, uniformly bounded by D, changes nothing.

This is a complex Banach space. Indeed a norm-Cauchy sequence is Cauchy in every H_b(H), since choosing any i in H bounds its component norm by exp(-a|H|) times the full norm. Let E_H be the component limits. For each finite collection of carriers, the corresponding weighted sums converge. Fatou first over all carriers at one root, then the supremum over roots, proves the full bound and convergence in (1.1). Bounded holomorphic functions are complete in the supremum norm on the open polydisc. No interchange of a supremum with an infinite order sum is needed.

For a finitely supported field A with ||A||_infinity<b, define the vacuum-normalized total

    Phi_E(A)=sum_H [E_H(A|H)-E_H(0)].                         (1.2)

If K is the finite cell support of A, only H meeting K contribute. Hence

    sum_H |E_H(A|H)-E_H(0)| <= 2 |K| ||E||_(a,b).             (1.3)

The series is locally normally convergent on every finite-coordinate polydisc. In particular Phi_E is analytic in every finite set of field coordinates, and evaluation at any fixed compact field is a bounded linear functional of E.

## 2. Closed equivalence kernel and complete quotient

Set

    N_(a,b)={E in A_(a,b): Phi_E(A)=0
                          for every compact A, ||A||<b}.      (2.1)

It is the intersection of the kernels of the bounded evaluations in (1.3), so it is a closed complex linear subspace. Define

    Q_(a,b)=A_(a,b)/N_(a,b),
    ||[E]||_Q=inf_(F in N_(a,b)) ||E+F||_(a,b).              (2.2)

The standard quotient-completeness proof applies: a summably Cauchy subsequence of classes admits successively chosen representatives whose norm differences are summable; their limit represents the class limit. Thus Q_(a,b) is a Banach space. A norm-minimizing representative is neither needed nor asserted.

Equation (2.1) removes all carrierwise constants, as well as nonconstant representation redundancies such as coboundaries. It removes no specified physical vacuum counterterm: a separately tracked vacuum density must stay in a separate sector if needed. Equality as germs on every finite-coordinate subspace is equivalent to (2.1), by analytic uniqueness on its connected polydisc.

Let I_(a,b) be the subspace of families whose normalized total is translation invariant, hypercubic invariant, globally adjoint invariant, and locally gauge invariant wherever the two compact configurations and their logarithmic gauge transform lie in the b domain. These are closed linear conditions: each is an equality of two bounded evaluations, or a locally uniform limit of them. Therefore I_(a,b) is closed and contains N_(a,b). Its quotient

    Q_inv=I_(a,b)/N_(a,b)                                 (2.3)

is a closed Banach subspace of Q_(a,b), with the same quotient norm. Reality on real fields specifies its closed real form. Spatial symmetries are imposed on totals, so the chosen cell partition need not act symmetrically on individual carriers.

## 3. Equality extends to summable fields

Use the cell norm ||A||_1=sum_i ||A|i||_infinity. Fix 0<rho<b. Directional Cauchy on the polydisc gives, for any segment whose endpoints have maximum norm at most rho,

    |E_H(A|H)-E_H(B|H)|
      <= ||E_H||_b/(b-rho) ||(A-B)|H||_infinity
      <= ||E_H||_b/(b-rho) sum_(i in H)||A_i-B_i||.           (3.1)

One first uses a Cauchy radius strictly smaller than (b-rho)/||A-B|| and then takes its limit. The convex segment remains in the rho polydisc. Summing at each cell gives

    |Phi_E(A)-Phi_E(B)|
       <= ||E||_(a,b)/(b-rho) ||A-B||_1.                   (3.2)

Consequently (1.2) extends by its absolutely convergent series to all summable fields with maximum at most rho. Finite truncations converge in this bound. If E belongs to N_(a,b), then this extension vanishes on all such summable fields. Thus the extension depends only on [E], with (3.2) valid after taking the quotient infimum.

This is important for background substitution: the image of a compact coarse field need not itself be compact. Equality only on compact fields would not by itself license evaluation at that image; (3.2) provides the missing continuity statement.

## 4. Total kernels and the Maxwell functional

All fixed-order total derivatives are obtained by termwise differentiation of (1.2) on finite coordinate sets. A kernel component with slots i1,...,in receives contributions only from carriers containing every slot. Scalar Cauchy, followed by the finite monomial count, gives for fixed n a constant C_n(a,D,J) such that

    sup_i1 sum_(i2,...,in) exp(sigma sum_(j>=2)|x_j-x_1|)
            |K_n(E;i1,...,in)|
       <= C_n b^(-n)||E||_(a,b),       n=1,2,3,4,          (4.1)

for a sufficiently small fixed sigma=sigma(a,J)>0. To see this explicitly, every nonzero term lies in H; connectedness gives each displacement at most c_d J|H|. Choose sigma so the exponential consumes at most exp(a|H|/2). The sum of ordered degree-n derivative magnitudes is at most

    (D|H|+n)^n b^(-n)||E_H||_b.

The remaining polynomial is absorbed by exp(a|H|/2). All spatial moments follow by another fixed exponent loss. This argument is for fixed orders; no dimension-free all-order absolute Taylor estimate is claimed.

Kernels depend only on [E], since every component can be tested by a finite-coordinate derivative of Phi_E. Applying (4.1) to E+F with F in N and taking its infimum gives the same bound with ||[E]||_Q.

For a simple gauge group and an invariant total, use the fixed trace-normalized color component and the positive-bond midpoint convention xi(x,mu)=x+e_mu/2. Translation invariance permits anchoring the first bond at zero. Define

    beta([E])=(1/2) partial_(p_nu)^2 Gamma_(2,mu mu)^E(0),
                    mu != nu.                           (4.2)

The invariant color form is understood. The exact infinite total Ward and point-symmetry algebra shows that the distinct pair in (4.2) is immaterial and that it is the Maxwell coefficient. For the normalized local Wilson reference it equals one. The same conclusion holds for the actual homogeneous classical reference whose flat symbol has that normalization. The proof in total_kernel_ward_extraction_research.md applies directly to the present infinite kernels: no subsequence is needed once the interaction in (1.2) is given.

Beta is a linear continuous functional on Q_inv, and is real on its real form. In particular

    |beta([E])| <= C_beta(a,D,J) b^(-2)||[E]||_Q.           (4.3)

For a concrete majorant, a second derivative component is at most 2 b^(-2)||E_H||, there are at most D|H| second slots, and the squared midpoint displacement is at most (c_d J|H|)^2. The factor 1/2 in (4.2) cancels the displayed 2. Thus one may take

    C_beta = D(c_d J)^2 sup_(m>=1) m^3 exp(-a m),          (4.4)

enlarged by the fixed color-normalization constant. This also proves continuity without relying on Fourier differentiation as an abstract operation. For a semisimple product use the finite vector of one coefficient per simple ideal and the corresponding finite family of references.

The factor b^(-2) in (4.3) is real and cannot be omitted. Uniformity in b belongs to the combined subtraction in the next section, not to beta alone.

## 5. Full-reference extraction is bounded uniformly in b

Suppose a normalized invariant reference class [S] has beta([S])=1 and admits a representative on each sufficiently small b with

    ||S||_(a,b) <= C_S b^2,                              (5.1)

where C_S is independent of b and, in a family of homogeneous models, independent of preceding refinement. Dependence on fixed J,a is allowed. The classical support theorem supplies such a hypothesis after fixing its support reserves and radius; it is not a consequence merely of beta(S)=1 or ellipticity. A simultaneous infinite-volume limit preserves (5.1) by Fatou, if the finite-regulator representatives obey it.

Here is an explicit realization from the existing classical estimate, which does not assume that each chosen reference coefficient has zero linear jet. Suppose a reference representation on one fixed radius rho satisfies ||S||_(a,rho)<=M_S uniformly in preceding refinement and its TOTAL vacuum-normalized functional has zero first derivative. Let P_n be the homogeneous phase projection of Section7 and replace each coefficient by

    S_H^(>=2)=sum_(n>=2) P_n S_H.

Its normalized total represents the same quotient class: the constant sector disappears from the definition, and the sum of its linear sector is zero. Homogeneity and the phase integral give ||P_n S_H||_b<=(b/rho)^n||S_H||_rho. Consequently, for 0<b<=rho/2,

    ||S^(>=2)||_(a,b)
       <= [(b/rho)^2/(1-b/rho)] ||S||_(a,rho)
       <= 2 M_S b^2/rho^2.                             (5.1a)

Thus C_S=2 M_S/rho^2 is independent of b and refinement. This is only a change of representative; it does not assert gauge invariance of its separate carrier coefficients or of a discarded linear coefficient. In the actual classical reference, the uniform fixed-rho support estimate and the total zero linear derivative are the needed inputs. The same construction may be performed before taking a joint subsequential limit.

Define the full-reference projection

    P_S[E]=[E]-beta([E])[S].                             (5.2)

Then beta(P_S[E])=0, P_S^2=P_S, and

    ||P_S[E]||_Q <= C_ext ||[E]||_Q,
    C_ext=1+C_beta C_S.                                 (5.3)

The constant is independent of small b. To prove this directly, take a representative within eta of the quotient infimum, use (4.3),(5.1), and send eta to zero. No bounded choice of a representative is required. The whole reference is subtracted, so local gauge invariance and its nonlinear Ward identities remain exact. Subtracting only a quadratic Taylor polynomial would not have this property.

## 6. When classical substitution descends

Fix an endpoint ratio L. Assume an actual infinite background map a_L from final fields to current fields is supplied on the final b ball, with a coherent complete-field support family

    a_L|i=sum_(X nonempty) a_(i,X)(w_X),
    a_(i,X)(0)=0,
    sup_i sum_X exp(kappa tau({i} union X)+A|X|)
                         ||a_(i,X)||_b <= C b/L,           (6.1)

and the amplitude bound ||a_L(w)||_infinity<=rho<b. The maximum over every whole current output fiber is inside the support sum. Coefficients on overlapping collars come from one assignment. The fields and scales are those of the pre-gauge map; no rooted-gauge amplitude contraction is substituted for this hypothesis.

For compact w supported in K, a nonzero term in (6.1) must have X meeting K, whence

    ||a_L(w)|i|| <= (C b/L) exp(-kappa dist(i,K)).         (6.2)

There are finitely many current coordinates per final fiber at fixed L. Summing (6.2) proves a_L(w) is summable. Therefore

    (T_L Phi_E)(w):=Phi_E(a_L(w))                        (6.3)

depends only on [E], by Section3. This proves algebraic descent of scalar classical substitution, without requiring individual carrier invariance.

To obtain a bounded map into an activity quotient, a representation theorem is still necessary. Precisely, suppose every E admits a strictly supported connected output family L_L E with total (6.3) and bound

    ||L_L E||_(a_out,b) <= B_L ||E||_(a,b).               (6.4)

Its assignment need not be canonical for quotient descent. Then T_L[ E ]=[L_L E] is well defined and has norm at most B_L. Different valid assignments give the same output class; input equivalence follows from (3.2),(6.2). The class map is linear even if no linear representative assignment is chosen, because its scalar normalized total is linear in E. Take near-minimal input representatives to obtain the quotient bound. The existing transport constructions provide (6.4) under their explicit core, tail, radius and carrier budgets; scalar amplitude alone does not imply it.

Preservation of invariant totals needs an additional hypothesis. For every compact w and allowed compact coarse gauge, the two summable outputs must be related by an actual infinite gauge transformation under which the chosen input total is invariant. One sufficient condition is approximation of the connecting gauge path by allowed compact gauges, with transformed fields converging in ell1 inside a common strict domain margin; then (3.2) passes the identity. Another is a joint finite-regulator invariant approximation of that particular interaction and the maps. An orbit relation alone, with no justification for applying the available gauge identity to its possibly noncompact gauge, is not enough. To assert an action on the entire invariant quotient this condition must hold for every class in that domain; a joint approximation of one chosen input establishes only its own identity. For infinite backgrounds the covariance and classical semigroup must likewise be obtained on one joint system or otherwise proved there. Unrelated subsequences and the finite-regulator semigroup alone do not define a universal invariant-quotient action.

The note analytic_interaction_compactness_research.md supplies simultaneous subsequential interactions and coherent maps for any fixed countable collection of parameters, as well as convergence of (6.3). Its hypotheses are the finite-regulator anchored bounds, complete supported norms, fixed finite fibers, compatible cofinal volumes, and common strict domain margins. It gives an available realization of (6.1) and of finite classical identities on a jointly chosen subsystem, not uniqueness of a universal map or quantum descent.

## 7. A conditional classical contraction in the quotient

Here all quantifiers matter. Fix J,a and the primitive block ratio. Assume, on a single joint infinite system, the following inputs for arbitrarily large allowed endpoint powers L and all preceding refinements under consideration:

1. A normalized full reference [S_M] with (5.1), uniformly in M,b. The output reference [S_(ML)] satisfies the same bound.
2. Exact invariant totals, the preceding beta prescription, and the uniform fixed-order kernel bounds (4.1).
3. The actual coherent pre-gauge families in the physical C^(1,alpha) norm, with primitive constants independent of L,M, as in pregauge_holder_prefix_research.md. Their fixed support/cardinality reserves satisfy the low-kernel transport budgets after J is chosen.
4. The low-kernel spatial relocalization theorem, including the repaired quadratic Laurent factorization, applies to these infinite kernels and coherent fields. Its constant C_low(J) is fixed after J and before L.
5. The high-jet background transport has its full core/tail budgets, with the same a,b in and out. Its constant C_high is independent of L after those fixed reserves are chosen. Increasing L weakens the compression restriction; the already fixed J and logarithmic tail cutoff remain admissible. The radius is selected after the final finite L so that b<=r_A/Lstar, Lstar=L/(8 C_A), and all other fixed classical margins hold.
6. Scalar substitution and preservation of the invariant input domain satisfy the extra gauge-identity requirement of Section6. For an operator assertion on the whole invariant quotient it is required for every class; a joint finite approximation may instead verify the pointwise estimate on a specified collection of classes. If one identifies substitution with a finite composition of elementary maps, all maps and identities are chosen jointly as just described.

For an invariant [E], let [F]=P_(S_M)[E]. Choose any representative F. Coefficientwise total homogeneous projections P_n, defined by a phase integral E_H(exp(it)A), have norm at most one and retain carrier H. The fifth-order remainder R5=I-sum_(n=0)^4 P_n has norm at most six. These operations also descend to the unrestricted quotient, since they may be applied to the zero analytic total, although they need not preserve gauge invariance separately.

The total first-order term of F is zero by global adjoint invariance, its vacuum is already removed, and beta(F)=0. The exact total Ward extraction therefore gives the low-kernel moment cancellations required by the spatial theorem. Apply that theorem to the total degree-two, three and four kernels, BEFORE assigning the new carriers. Applying (4.1) to the chosen representative makes its epsilon at most C_ker(J)||F||. Thus their substituted total has a connected representation of norm at most

    C_low(J) L^(-alpha)||F||.                            (7.1)

The coefficientwise R5 part has a representation of norm at most

    6 C_high L^(-1)||F||                                (7.2)

in dimension four. The first-order zero total remains zero after substitution by the summable-field extension; it need not vanish on each input carrier. All the infinite scalar identities are legitimate: the input polynomials and R5 lie in the same anchored space, their totals extend by Section3, and the constructed output families converge normally on compact fields.

Adding the two new representations and taking the infimum over representatives of [F] proves

    ||T_L P_(S_M)[E]||_Q
       <= [C_low(J)L^(-alpha)+6 C_high L^(-1)]
                                      C_ext ||[E]||_Q.  (7.3)

This is an estimate on the equivalence class, not on the originally selected sequential family. If desired, apply a full-reference extraction at the output:

    ||P_(S_(ML)) T_L P_(S_M)||
       <= C_ext,out C_ext,in
                    [C_low(J)L^(-alpha)+6 C_high L^(-1)]. (7.4)

There is no assertion that T_L automatically preserves the beta-zero subspace; the output projection in (7.4) addresses that point. Under the six hypotheses, first fix J, then choose a finite L=R^q large enough to make (7.4) smaller than one, and finally choose the common positive b. The constants in (7.4) do not deteriorate merely because b is reduced. The exact classical scalar semigroup permits this finite-q representation if its joint-limit hypotheses hold. It does not identify sequential quantum integrals with a one-shot integral.

## 8. Remaining boundaries

Sections1-5 are unconditional functional-analytic consequences of their stated activity/reference hypotheses. Section6 isolates the summability and representation requirements for classical descent. Section7 is a conditional contraction theorem whose concrete analytic inputs are the separately proved infinite-kernel, supported-background and spatial-relocalization modules; it spells out rather than suppresses their infinite-family and parameter-order interfaces.

No quantum map on Q_(a,b) has been defined here. Equality of vacuum-normalized infinite totals on compact fields need not, without a further theorem, identify finite-regulator exponentials, sharp restricted integrals, chosen vacuum normalizations, or their limits. Consequently this quotient does not yet authorize replacing the actual quantum output by an arbitrary equivalent family inside the next finite integration. Quantum descent, its continuity and normalization compatibility, a full amplitude recursion, and the coupling trajectory remain separate.
