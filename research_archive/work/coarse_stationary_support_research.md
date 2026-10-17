# Strict support transport to the physical stationary current background

Research result, 17 October 2026. This note constructs the physical stationary current background directly in the rooted support algebra. Its corrected majorant and colored-slot convention passed the separate internal reviews recorded in `coarse_stationary_support_provenance_audit.md` and `coarse_transport_audit.md`; the latter also checked the manuscript fragment. These checks are not external certification. The result concerns the homogeneous classical branch with arbitrary old refinement M, not closure of inherited quantum interactions or an iteration of quantum RG.

## 1. Target, scales, and the precise prior inputs

Fix odd L, d=4, color, and compatible periodic source geometry with the distinct block interfaces used in Notebook19. The current spacing is one, the old fine spacing is M^-1 with M=L^k, and the next-coarse spacing is L. Write

    W=exp(i w),      V=exp(i a).

Both w and a are dimensionless link angles in these expressions. In current physical units, a is the current potential and w/L is the next-coarse physical potential. In next-coarse unit coordinates w is the corresponding unit-spacing potential. The formulas below use w, not w/L. Their constants may depend on the fixed L, never on M or volume.

Group current variables into L-block cells, indexed by next-coarse cells. A block contains the retained nonpivot coordinates z of fixed real dimension

    D_z=d(L^d-1) dim(g),

and next-coarse link data of dimension D_w=d dim(g). Thus the joint variable u=(w,z) has fixed cell dimension D=D_w+D_z=d L^d dim(g). The retained z uses ordinary current-link logarithmic coordinates, before any fluctuation rescaling by a coupling. Maximum-coordinate, Euclidean-fiber and maximum-current-cell norms differ only by fixed L/color factors, which are absorbed into radii and constants. All scalar coordinate Cauchy estimates below are made after an explicit fixed-dimensional conversion to a product polydisc.

The authoritative inputs are:

* Notebook19 / `physical_current_pivot_precision_research.md`, Sections2--3: the actual ordinary average F_1(a)=log M_L(exp(i a))/i, the one-pivot-per-equation property, A_1=DF_1(0)=L Q_L^flat, the pivot right inverse h_1, and the retained kernel insertion K_L.
* The same note, Section5: an analytic physical branch V_old,*(W) with M_L(V_old,*)=W, actual averaged-contour variables P_V(y,x)=1, small current potential, and constrained classical minimality proved by the two-scale minimum comparisons. Section4 identifies the actual nonnegative exponential gauge action on real unitary fields.
* Notebooks07,17,19: the real flat retained precision and its inverse

      A_M,0=K_L^T(q_M+T_L^T T_L)K_L,       C_M,0=A_M,0^-1,
      gamma_* I<=A_M,0<=B_* I,                                      (1.1)

  with exponentially weighted row/column bounds for A_M,0 and C_M,0, uniformly M and volume.
* Notebook21 / `classical_support_localization_research.md`, Sections5--7: a strict scalar support expansion for S_M(a), the homogeneous ordinary constrained classical action, with arbitrary prescribed finite cardinality reserve on a fixed small product ball; this property survives any fixed-range analytic fixed-L current-coordinate substitution and the addition of the actual local gauge action. The radius may shrink with the requested reserve. The expansion is in original variable supports, and its coefficients may depend on the fixed regulator and flat baseline.

The result proved below is a uniform product ball in the next-coarse w variables and strictly supported families a_*;i,X(w|X) such that

    a_*(w)=sum_X a_*;X(w|X),
    sup_i sum_X exp[kappa tau({i} union X)+a_card |X|]
                     ||a_*;i,X||_r <= C_(a_card) r,                  (1.2)

with any prescribed finite a_card>=0. Here i is a current-field L-block, X contains next-coarse background labels, and both are in the same L-block index graph. Tau is graph Steiner length, allowing auxiliary vertices. The nonlinear part after subtracting the explicit flat linear extension is O(r^2) in the same norm. This supplies a genuine strict support transport, not merely a one-weight derivative bound.

## 2. A local affine pivot chart for nonzero coarse datum

Write the identity-background ordinary constraint as

    F_1(a)=A_1 a+C_1(a),     C_1(0)=DC_1(0)=0.

The source normalization is

    A_1=L Q_L^flat,       A_1 h_1=I,       A_1 K_L=0,
    h_1(c)=L^(d-1) I inserted at the pivot p(c).                      (2.1)

Indeed the pivot coefficient in Q_L^flat is L^-d, hence in A_1 it is L^(1-d). Nonpivot restriction of K_L is the identity and h_1 has no nonpivot entries. Seek a current potential with specified next-coarse datum w and specified retained coordinates z by

    a=K_L z+h_1 w-h_1 C_1(a).                                      (2.2)

For each coarse bond c, F_1(a;c) reads its own pivot p(c) and no other pivot. Thus (2.2) is a family of independent finite-dimensional Lie-algebra-block implicit equations, one per coarse bond, with the neighboring nonpivot z values as parameters. The derivative in the pivot block at zero is invertible. A finite-dimensional contraction on a common neighborhood gives a unique holomorphic solution

    a=mathfrak a(w,z),
    F_1(mathfrak a(w,z))=w,       mathfrak a(w,z)|nonpivots=z.         (2.3)

Its dependency neighborhood is the fixed two-block source neighborhood: iteration cannot spread to another pivot equation. There are finitely many local types. Consequently, uniformly in volume,

    ||mathfrak a(w,z)||_infinity <= C_L (||w||_infinity+||z||_infinity),
    mathfrak a(w,z)=K_L z+h_1 w+O((||w||+||z||)^2).                  (2.4)

Its higher local derivatives have the usual uniform finite-dimensional Cauchy bounds. The old refinement M does not enter this chart. Equivalently, this is the identity-background ambient source straightening applied to K_L z+h_1 w. It is the unique small solution with those retained coordinates, rather than an arbitrary parametrization of the same constraint surface.

## 3. The scalar action in this chart and its exact quadratic part

Let G(exp(i a)) be the actual averaged-contour exponential gauge action of Notebook19, with its coupling-free normalization. Define

    T_M(w,z)=S_M(mathfrak a(w,z))+G(exp(i mathfrak a(w,z))).           (3.1)

All chart and gauge dependencies have fixed L range. Notebook21's support composition theorem, followed by its fixed L-block regrouping, gives

    T_M(w,z)=sum_(nonempty X) T_X(w|X,z|X),                           (3.2)

with an anchored scalar bound on a fixed joint coordinate polydisc of radius rho:

    Kcal = sup_i sum_(X contains i)
                   exp[sigma tau(X)+A_card |X|] ||T_X||_rho < infinity. (3.3)

Here sigma>0 and A_card can be any prescribed finite positive reserve. The constants, rho and Kcal are uniform in M and volume. In this application each T_X begins at order at least two: the original scalar action coefficients begin at order two or higher, the chart vanishes at zero, and the local gauge action has zero constant and first derivative at the identity. No additive extensive constant needs to be differentiated.

Put P_M=q_M+T_L^T T_L. Since the full scalar action and gauge action are stationary at zero, the quadratic term depends only on the linear part of the chart:

    T_M^(2)(w,z)=(1/2)<K_L z+h_1 w, P_M(K_L z+h_1 w)>.

Consequently

    D_z T_M(w,z)=A_M,0 z+B_M w+N_M(w,z),                              (3.4)
    B_M=K_L^T P_M h_1=K_L^T q_M h_1,
    N_M(0,0)=DN_M(0,0)=0.                                           (3.5)

The simplification uses T_L h_1=0: every contour defining T_L is internal to a block and reads no pivot. In particular the retained Hessian is exactly the already bounded A_M,0 from (1.1), not a new matrix requiring a new gap proof. The rectangular B_M has uniform exponential block row/column bounds, since K_L,h_1 are fixed-range and q_M has the previously proved uniform decay.

All pairings in (3.4)--(3.5) are counting pairings in the stated angle coordinates. There is no extra L^4 transpose factor between z and w: w is a coordinate vector on the next-coarse bonds, not a physical-volume normalized scalar product variable. Using the next-coarse physical potential w/L simply replaces w by L times that variable, a fixed-L conversion.

## 4. Scalar support estimates imply an analytic mixed-slot gradient majorant

This is a necessary additional argument. It would be incorrect to apply the earlier finite-range vertex lemma to the unbounded supports X in (3.2). Crude polarization followed by |X|^n input-slot counting can introduce a factorial after spending a fixed cardinality reserve. The following coordinatewise Cauchy argument avoids that loss.

Choose a trace-orthonormal fixed scalar coordinate basis in each L-block cell. There are D coordinates of u=(w,z) per cell and D_z output coordinates of D_z T in one cell. Shrink rho by a fixed D-dependent norm equivalence if necessary so that each T_X is bounded by M_X=||T_X||_rho on the scalar coordinate polydisc |u_l|<rho, with D|X| scalar variables. Its Taylor coefficients obey

    |c_(X,beta)| <= M_X rho^(-|beta|).                               (4.1)

For one derivative coordinate alpha in the retained part of a cell i in X, the sum of the absolute Taylor coefficients, evaluated at common scalar radius t<rho, is bounded by

    sum_(beta >= e_alpha) beta_alpha |c_(X,beta)| t^(|beta|-1)
       <= (M_X/rho) (1-t/rho)^(-D|X|-1).                             (4.2)

This follows by differentiating the finite product of geometric series. For the vector gradient at cell i, sum its at most D_z scalar components. The symmetric multilinear Taylor coefficient distributes a scalar monomial coefficient among its ordered scalar slots with multinomial weights summing to one. Thus summing its multilinear cell operator norms over all ordered input-cell labels is bounded by the same absolute scalar coefficient sum, up to fixed cell norm constants already absorbed into D_z/rho. All these slots, and the output i, lie in X, so their rooted Steiner length is at most tau(X).

For any 0<kappa<=sigma, the supremum over the output cell of its all-order positive mixed-slot row series is therefore at most

    Gcal(t) = (D_z/rho) sup_i sum_(X contains i)
                 exp[kappa tau(X)] M_X (1-t/rho)^(-D|X|-1).           (4.3)

Choose t_0<rho/2 so that

    D log[1/(1-t_0/rho)] <= A_card/2.

Then Gcal(t_0)<=2 D_z Kcal/rho=:M_g, uniformly in M and volume. The supremum over output cells must not be interchanged with the sum over Taylor orders. If v_n is the supremum of the order-n mixed-slot row norm, the preceding bound implies the separate coefficient estimate v_n<=M_g t_0^-n. Remove the constant and linear Taylor degrees to obtain the positive generating majorant Phi=sum_(n>=2) v_n t^n of N_M. Thus, for 0<=t<=t_0/2,

    Phi(t) <= M_g (t/t_0)^2/[1-t/t_0],
    Phi'(t) <= 8 M_g t/t_0^2.                                       (4.4)

The first is the geometric sum of the separate coefficient bounds; differentiating that geometric series gives the second. This deliberate geometric factor avoids a false exchange of the order sum and the output supremum while retaining an analytic, quadratic majorant.

This is the required analytically summable mixed-insertion estimate, with no factorial loss and no dimension depending on M. The potentially large original carrier X is a fixed coefficient carrier at the flat baseline, not a new variable support. After substituting families for w and z, the actual variable support is the union of their input supports. Rooted trees may use X internally to connect the output and input roots; (4.3) has already paid that tree length. No nonlocal background is concealed in a Taylor coefficient.

## 5. A support-valued stationary solution with uniform next-coarse radius

Use the same rooted algebra as Notebook21, now with L-block roots and next-coarse w labels. For an arbitrary prescribed finite a_card>=0 set

    ||u||_(kappa,a_card;r)
      =sup_i sum_X exp[kappa tau({i} union X)+a_card |X|]
                        sup_(||w|X||<r) ||u_(i;X)(w|X)||.             (5.1)

The singleton data w have norm e^(a_card) r. Linear blocks act by their exponential row sums without changing variable supports. The gradient majorant (4.4), graph Steiner gluing, and union-submultiplicativity of the cardinality weight allow the same support substitution theorem as before.

For the joint insertion into N_M, use the maximum of the separate w- and z-family norms, and view the input slots as colored by their scalar coordinate and field type. This convention is justified directly by (4.1)--(4.3), whose positive majorant has already summed all scalar coordinates and both field types: each scalar-component support family is bounded by its corresponding vector-family norm. We do not assert that this maximum equals sum_X||(w_X,z_X)|| for a joint vector family; that latter norm could be larger. The colored-slot convention avoids silently exchanging these two norms in the radius estimate.

The retained stationarity equation is

    z=-C_M,0 B_M w-C_M,0 N_M(w,z).                                  (5.2)

Let c_0 be a common weighted block norm of C_M,0 and let

    ell_0 >= max(1, ||C_M,0 B_M||_kappa).

Choose

    r_star <= min(t_0/2, t_0^2/(16 c_0 M_g)),
    r <= r_star/(2 ell_0 exp(a_card)),                               (5.3)

and decrease these constants further when needed to stay within the evaluated common chart and prior uniqueness domains. On the support-family ball ||z||<=2 ell_0 exp(a_card) r, the joint tuple (w,z) has norm at most r_star. Equations (4.4) and (5.3) make the right-hand side a contraction with constant at most 1/2 and map this ball into itself. Hence there is a unique supported solution z_*(w) with

    ||z_*||_(kappa,a_card;r) <= 2 ell_0 exp(a_card) r,
    ||z_*+C_M,0 B_M w||_(kappa,a_card;r) <= C_(a_card) r^2.            (5.4)

Every nonlinear coefficient starts at degree two. Absolute support evaluation gives a genuine stationary solution on the finite regulator, holomorphic on a next-coarse product ball of uniform radius. The proof also gives a convergent rooted-tree construction with background leaves carrying the original w cells.

Apply the fixed-range analytic chart mathfrak a from Section2 to the supported pair (w,z_*(w)). The finite-range cell-vertex substitution lemma of Notebook21 applies here literally, because this chart has fixed L range. It yields

    a_*(w)=mathfrak a(w,z_*(w)),
    Hcur_M = h_1-K_L C_M,0 B_M,
    ||a_*||_(kappa,a_card;r) <= C_(a_card) r,
    ||a_*-Hcur_M w||_(kappa,a_card;r) <= C_(a_card) r^2.              (5.5)

The displayed Hcur_M is an actual current-angle extension, not the earlier original-fine minimizing extension H. It has a uniform exponential rectangular block bound and A_1 Hcur_M=I. Its gauge condition T_L Hcur_M=0 follows after the physical identification below (or by linearizing that identified branch). No gauge-zero conclusion is inferred from (5.2) alone.

The group fields exp(i a_*) and their inverses inherit the same strict support construction after subtracting their constant identity, by the local analytic power series. For present activity transport it is enough to retain the potential a_*. Its norm s(r)=C_(a_card)r tends to zero with the next-coarse radius, uniformly in M and volume. This is the estimate needed to substitute it into analytic background activities.

## 6. Identification with the actual physical gauge-zero branch

For real small w, Notebook19 already constructs V_old,*(W) by two minimum comparisons followed by the exact averaged-contour rooted gauge. It satisfies

    M_L(V_old,*)=W,       P_Vold,*(y,x)=1,
    ||a_old,*||_infinity <= C_L||w||_infinity,
    S_M(a)>=S_M(a_old,*)                                             (6.1)

for every sufficiently small real current a with M_L(exp(i a))=W, in the common comparison ball. This is the established variational statement, not an assumed dynamic-programming identity for arbitrary branches.

The actual gauge action is nonnegative on real unitary configurations and vanishes at P=1. Consequently

    S_M(a)+G(exp(i a)) >= S_M(a_old,*)+G(V_old,*),                    (6.2)

on that same feasible neighborhood. The affine chart of Section2 parametrizes every sufficiently small configuration with the given constraint by its retained absolute logarithmic coordinates. In particular

    z_old,* = a_old,*|nonpivots,
    a_old,* = mathfrak a(w,z_old,*).

Thus z_old,* is a critical point of T_M(w,z). This proves stationarity of a known gauge-zero branch; it does not try to deduce P=1 from a generic critical equation.

There is a uniform common uniqueness neighborhood. Either apply the complete chain-rule estimate of Notebook19 to the affine chart, or differentiate the scalar support expansion (3.2) with fixed Cauchy margins and cardinality reserve. The latter gives, including the absolute row and column sums,

    ||D_z^2 T_M(w,z)-A_M,0||_kappa
                       <= C_L (||w||_infinity+||z||_infinity).       (6.3)

For clarity, each scalar coefficient contributes its third derivative contracted with the bounded direction (w,z); summing the second retained matrix index costs only |X|, paid by a spare cardinality exponent. The output/input distance is bounded by tau(X). The actual chart and gauge curvature terms are all included because the differentiated object is the full scalar T_M. Symmetry provides the column estimate. No unproved ordinary-rooted adjoint occurs.

Choose a fixed real retained supremum ball and a next-coarse ball so that (6.3) is at most gamma_*/2. The real retained Hessian is then bounded below by gamma_*/2 throughout that convex ball, so T_M(w,.) has at most one critical point there. The two solutions z_*(w) from (5.2) and z_old,*(w) from (6.1) both lie in it after a further uniform shrink. They must coincide. Therefore

    exp(i a_*(w))=V_old,*(exp(i w)),
    M_L(exp(i a_*(w)))=exp(i w),
    P_exp(i a_*(w))(y,x)=1.                                         (6.4)

Both branches and all displayed maps are holomorphic on a uniform complex product neighborhood. Equality on an open real coordinate ball extends to that neighborhood on every finite regulator by the finite-dimensional identity theorem. This extends the exact identities, not real minimum inequalities, to complex w. Linearizing the last identity in (6.4) proves T_L Hcur_M=0 and supplies the claimed source gauge for the flat leading extension.

## 7. Support transport statement and limitations

Combining Sections5--6 proves the following uniform statement. For any fixed finite cardinality reserve a_card and sufficiently small positive kappa, there is a next-coarse product radius r>0 independent of M and volume on which the actual physical stationary current potential has strict support families in the original w labels satisfying (5.5). The scalar field-variable domain is the next-coarse angle domain, with the fixed-L physical conversion stated in Section1. Regrouping to current roots or next-coarse blocks costs only fixed L factors. The analytic stationary solution is the previously constructed physical gauge-zero branch; no separate gauge selection is silently substituted.

This result is stronger than an exponentially weighted response bound, because every coefficient reads only its declared w cells and the full support sum is convergent with arbitrary fixed cardinality reserve. Coefficients may depend on the fixed regulator M and periodic volume. Strict variable support alone does not assert their thermodynamic consistency.

It gives a mechanism for transporting a single analytic background-dependent classical or quantum activity through a_*(w). The preservation of a specified family of quantum activity norms, the exact support bookkeeping for unbounded carriers, and any loss of the available coarse/background radius must be proved separately. In particular (5.3) is one uniform step with fixed L. It is not a claim that repeated quantum integrations preserve a common radius or smallness budget indefinitely. No coupling-flow, mixed-history, boundary-orbit, or interacting continuum assertion is made.

There is a concrete reason not to infer a factor L^-1 contraction in the angle supremum domain from dimensional language. Take a sufficiently small coarse pure gauge W(y,y')=g_y g_y'^-1, and set the current-site gauge equal to g_y throughout each L-block. Its current link field V is the identity on internal links and equals W on links crossing the corresponding block boundary. It has P_V=1, ordinary average W and zero classical action (a pure gauge), so the uniqueness argument identifies it with the physical stationary branch. Its boundary-link angle is of order ||w||, not ||w||/L. The physical next-coarse potential is w/L, but the supported transport theorem concerns the angle variables in (2.2). It provides a small one-step domain and no automatic contracting supremum-domain self-map.
