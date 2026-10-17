# Strict support localization of the homogeneous classical action

Research result, 17 October 2026, checked in two separate internal audits: `classical_support_localization_audit.md` and `classical_support_localization_provenance_audit.md`. This note supplies a support-valued fixed-point theorem and applies it to the already proved homogeneous small-field classical branch. These internal checks are not external certification. It does not infer a tree bound from a one-weight response bound, and it makes no quantum Yang--Mills construction claim.

The result is uniform in the old refinement M=L^j and compatible finite periodic volume, with fixed odd L, dimension four, fixed color space and fixed 0<alpha<1. The source variable is the original current-cell potential B, on a product supremum ball. Fine pairings retain the physical factor eta^4, eta=M^-1. Constants may depend on L, alpha, the requested positive spatial exponent and the requested fixed support-cardinality reserve. The radius of the product ball may shrink with these constants.

## 1. Statement and exact input map

There are positive refinement-independent radii and spatial exponents with the following properties.

1. The corrected constrained minimizer A(B), its multiplier m(B), and the scalar classical action S_M(B) have absolutely convergent expansions whose coefficients depend only on their explicitly assigned original background cells. The coefficients have summable rooted tree weights. An arbitrary prescribed finite weight exp(a|X|) on the number of background cells can be included by shrinking the background radius.
2. The classical action has a decomposition

   S_M(B) = (1/2)<B,q_M B> + sum_(nonempty Y) W_Y(B|Y),                 (1.1)

   where every W_Y is holomorphic on the same product ball, starts at order three, and, for suitable mu>0 and any fixed a>=0,

   sup_i sum_(Y contains i) exp(mu tau(Y)+a|Y|) ||W_Y||_b <= C b^3.     (1.2)

   Here tau is the graph Steiner length defined below. The norm is the supremum for all complex ||B|Y||_infinity<b. This is an exact scalar-action decomposition on a finite regulator, not merely a decomposition of a response estimate.
3. Differentiating each scalar coefficient gives individually complex-symmetric matrix coefficients, with rows, columns and background dependence all in Y. On a smaller ball their absolute-row support norm is O(b), uniformly in M. This supplies the strict background-support hypothesis of Notebook18 for the nonlinear part of the coarse classical Hessian.
4. Composing the scalar action with the actual fixed-L current pivot/exponential-coordinate chart, and adding the actual local exponential gauge action, preserves these conclusions after a fixed enlargement of supports. Consequently the physical retained precision A_M(V)-A_M(1) has a strict support expansion of row norm O(||log V||_infinity). Its classical Taylor remainder after z -> gz has a strictly localized interaction norm O(g R^3) on the retained window ||z||_infinity<=R, provided gR is in a fixed small domain.

The last conclusion uses the fixed-L physical current chart and source identification proved in `physical_current_pivot_precision_research.md`; it is not a new identification of arbitrary independent source currents or mixed histories. It concerns the homogeneous classical action plus the specified local gauge term. Additional effective interactions in a later quantum RG step remain separate inputs.

The exact simultaneous stationarity equations are

 A = H B - H R(A) - C S^T f_eta(S A) + C V(A,m),
 m = q B - q R(A) + (S H)^T f_eta(S A) - H^T V(A,m),                  (1.3)
 V(A,m) = DR(A)^T m.

Here F(A)=QA+R(A) is the full **corrected** fixed-reference average, H is the flat source-gauge minimizing extension, C is the constrained flat inverse, q=q_M, and S is the local first-difference jet. The transpose is the physical bilinear transpose. The three nonlinear primitives R, f_eta(S A), V all start at total degree two. Equation (1.3) is algebraically equivalent to Notebook15's chart and stationary equation in their common small domain: the second line solves the multiplier inverse, and the first then equals A=H[B-R(A)]+xi with xi=-C N(A)+C DR(A)^T m in the fixed flat slice.

All concrete analytic and localization inputs for (1.3) are proved in `classical_local_vertex_bounds_research.md`, Sections 2--6. In particular its physical-adjoint estimate is essential. The full ordinary rooted-average adjoint is not a permissible uniform primitive; that note gives a counterexample. The exact scalar action equality from Notebook15 transfers the corrected result to the ordinary homogeneous constrained branch without inserting that adjoint.

## 2. Geometry and complete cell spaces

Let Lambda be the finite current-cell periodic graph with graph distance d. For a nonempty finite set X define tau(X) as the minimum number of graph edges in a connected subgraph containing X; unmarked intermediate cells are allowed. This is graph Steiner length, not the metric minimum spanning-tree length ell used in Notebook18. They obey

 tau(X) <= ell(X) <= 2 tau(X),       |X| <= tau(X)+1.                  (2.1)

The upper comparison follows by traversing a minimizing connected tree and shortcutting its tour in the metric. These facts hold also on short periodic tori. Most importantly,

 tau({i} union X) <= d(i,j)+tau({j} union X),
 tau({i} union X_1 ... union X_n)
   <= tau({i,j_1,...,j_n}) + sum_r tau({j_r} union X_r).              (2.2)

The intermediate roots j_r need not be final support labels. This is the reason to use tau in the fixed-point algebra. The corresponding inequality with metric MST length and deleted intermediate roots is not valid in general. At the end, an estimate with exponent sigma on tau supplies the Notebook18 estimate with any exponent at most sigma/2 on ell.

Use a smooth fixed-physical-scale partition of unity chi_i on fine fields. Its supports lie in uniformly enlarged current cells, it has finite overlap, and its physical derivatives are uniformly bounded. For fine complete field spaces use

 X_eta = N_alpha,     Y_eta = C^alpha,     Z_eta = bounded fields;

for current fields use one fixed-dimensional cell space E_i. Let E_i^X,E_i^Y,E_i^Z be spaces of actual complete fields supported in the corresponding enlarged cell, with their global norms. Restriction/localization P_i u=chi_i u and reconstruction Rcal(u_i)=sum_i u_i are uniformly bounded. In particular Rcal P=I. The product rule and the complete Hölder norm make this legitimate uniformly in eta; a sharp cell cut would not do so.

The equations will be written in these possibly redundant block coordinates. Applying P to (1.3) and reconstructing all inputs gives an exact equivalent fixed point on the compatible image. Every right-hand side lies in that image, so the solution obtained below is compatible automatically.

For each of the linear maps H,q,C,C S^T,H^T,(S H)^T, the existing complete-field weighted estimates and a localized complete input give block envelopes

 ||T_ij|| <= C_T exp[-kappa_0 d(i,j)].                                (2.3)

The local diagonal block of C S^T is bounded by the proved equal-exponent Schauder theorem. It is not bounded by taking the absolute integral of a singular differentiated kernel. For each 0<kappa<kappa_0,

 L_T(kappa)=sup_i sum_j exp[kappa d(i,j)] ||T_ij|| < infinity          (2.4)

uniformly in refinement and volume. The same column bound follows from (2.3). This step legitimately uses a one-weight estimate for a linear map with one source cell. The nonlinear mixed-slot summation is an additional step below.

## 3. Rooted strict-support algebra and nonlinear substitution

For a product background ball of radius b, a support family u consists of functions u_(i;X)(B|X) taking values in the cell block E_i. They are bounded and holomorphic, and X is a nonempty set of original current cells. Define

 ||u||_(kappa,a;b)
   = sup_i sum_X exp[kappa tau({i} union X)+a|X|]
                   sup_(||B|X||<b) ||u_(i;X)(B|X)||.                 (3.1)

For several field types, take their maximum in each coefficient norm before summing supports: the joint family norm is sup_i sum_X weight(X,i) max_type ||u_type;i,X||, with the displayed background supremum understood. It is not the maximum of the separate type-family norms. The Taylor operator norms use this same joint cell space with its maximum norm; a joint linear-source bound can be taken as the sum of its component block bounds. Thus only fixed finite sums occur. Families with finite norm form a Banach space. Repeated constructions with the same support are added in that support slot. Evaluation sum_X u_(i;X)(B|X) converges absolutely and defines a genuine cell field, uniformly on smaller product balls. All dependence is on the original B variables; no background-dependent baseline is hidden in a coefficient.

A linear block operator acts without changing X. Inequality (2.2) and (2.4) give

 ||T u||_(kappa,a;b) <= L_T(kappa) ||u||_(kappa,a;b).                 (3.2)

Suppose a nonlinear analytic cell map has Taylor coefficients, including 1/n!,

 N_i(u) = sum_(n>=2) sum_(j_1,...,j_n)
                    N_(n;i;j_1,...,j_n)[u_j1,...,u_jn],

with mixed-insertion norms

 v_n = sup_i sum_(j_1,...,j_n)
          exp[kappa tau({i,j_1,...,j_n})] ||N_(n;i;j_1,...,j_n)||,
 Phi(t)=sum_(n>=2) v_n t^n < infinity for t<t_0.                       (3.3)

Substitute support families and assign each resulting term the union X=X_1 union ... union X_n. The second inequality in (2.2) and |union X_r|<=sum|X_r| give

 ||N(u)||_(kappa,a;b) <= Phi(||u||_(kappa,a;b)),
 ||N(u)-N(v)|| <= Phi'(r)||u-v||,   ||u||,||v||<=r<t_0.              (3.4)

This proves convergence of every sum involved. The estimate counts all ordered cell slots, all support unions, and all repetitions. It neither assumes disjoint input supports nor discards repeated labels. The cardinality reserve a changes none of the nonlinear majorants: a flat Taylor coefficient adds no variable support.

For completeness, a uniformly analytic local map with dependency radius R and at most D_R possible input cells in each slot supplies (3.3). If it is bounded by M_0 on an input ball r_0, the reconstruction norm is C_P, and output localization has a fixed norm, polarization/Cauchy gives

 v_n <= M_1 [e C_P D_R exp(kappa R)/r_0]^n.                          (3.5)

Indeed the derivative in n normalized directions is at most M_1(n C_P/r_0)^n; division by n! and n^n/n!<=e^n give the Taylor coefficient, and there are at most D_R^n nonzero ordered cell tuples. This is a current-cell count. No factor M^4 or count of independent fine coordinates appears. The physical-row holomorphy of DR(A)^T supplies this assertion for V(A,m); mere holomorphy of R into a supremum norm would not suffice for its transpose.

## 4. Convergent support-valued minimizer

Apply (3.3)--(3.5) to the three nonlinear primitives in (1.3) and then (3.2) to their linear propagators. The resulting nonlinear map on u=(A,m) has a positive analytic majorant Phi, quadratic at zero, uniform in M and volume. For example, after increasing two constants v,c,

 Phi(t) <= v (c t)^2/(1-c t),
 Phi'(t) <= 8 v c^2 t   when c t<=1/2.                              (4.1)

The local source B has the singleton family B_(i;{i})=B_i. Its norm is e^a b. If L_0 bounds the map B -> (H B,q B), the linear term has norm at most L_0 e^a b. Choose

 r_* <= min{1/(2c), 1/(16vc^2)},
 b_* <= r_*/(2 L_0 e^a).                                           (4.2)

Also choose r_* small enough that evaluation and reconstruction of this family ball lie in the previously established classical branch's uniqueness ball. Their norms are uniformly bounded, so this is a further refinement-independent shrink.

Then u -> (H B,qB)+N(u) is a contraction with Lipschitz constant at most 1/2 on the support-family ball of radius 2L_0e^a b, for b<=b_*. Its unique fixed point satisfies

 ||(A,m)||_(kappa,a;b) <= 2L_0 e^a b,
 ||(A-HB,m-qB)||_(kappa,a;b) <= C_a b^2.                             (4.3)

Evaluation is a continuous homomorphism for all these substitutions. Evaluating the fixed point therefore gives (1.3), and uniqueness of the already established small classical branch identifies it with the actual minimizer and multiplier. It is not a different formal solution.

Picard iteration starting with the singleton source provides a precise rooted-tree expansion if desired: each internal vertex is one Taylor coefficient of a local nonlinear primitive, each propagator edge is one block of a fixed flat linear map, and leaves carry the original B_i. The proof above establishes absolute convergence of the complete tree sum rather than merely writing it formally. Branching, all orders, and depth growing with M are already contained in (3.4). The refinement dependence occurs in uniformly bounded vertices, not in an additional count of RG levels.

Every coefficient of A-HB and m-qB has Taylor degree at least two. This follows either by the tree construction or by homogeneous-degree induction. In particular the bounds in (4.3) hold for all sufficiently small b with the same constants, which will be used for a cubic action bound.

## 5. Scalar action, strict supports, and symmetric Hessian pieces

Notebook16 proves on the finite regulator

 D S_M(B)=m(B),  S_M(0)=0,  D^2 S_M(0)=q_M.                          (5.1)

It also identifies this scalar action with the ordinary homogeneous constrained action through the exact gauge transfer. Define n=m-qB and use its support family from Section4. The exact envelope identity gives

 S_M(B)-(1/2)<B,qB>
      = int_0^1 sum_i <B_i,n_i(tB)> dt.                             (5.2)

Assign the summand involving n_(i;X) the support Y={i} union X and add all summands with the same Y:

 W_Y(B|Y)=sum_({i} union X=Y) int_0^1 <B_i,n_(i;X)(tB|X)> dt.        (5.3)

Each coefficient is scalar, strictly local in its stated original background support, holomorphic, and of degree at least three. The current pairing has cell volume one and fixed fiber dimension. For 0<mu<kappa, rerooting at b in Y gives

 exp[mu tau(Y)+a|Y|]
  <= e^a exp[kappa tau(Y)+a|X|]
                   exp[-(kappa-mu)d(i,b)].                          (5.4)

The periodic distance sum S_delta=sup_b sum_i exp[-delta d(i,b)] is bounded by the infinite-lattice sum uniformly in volume. Consequently

 sup_b sum_(Y contains b) exp[mu tau(Y)+a|Y|] ||W_Y||_b
       <= e^a S_(kappa-mu) b ||n||_(kappa,a;b)
       <= C_(mu,a) b^3.                                           (5.5)

This proves (1.2). It is the rerooted sum over supports containing an arbitrary cell, not only a norm at the original output anchor. There is no volume factor in this local norm. Summing all supports of course gives an extensive finite-volume action.

For a smaller product ball define

 B_Y(B|Y)=D^2 W_Y(B|Y),                                             (5.6)

extended by zero in cell rows and columns outside Y. Each B_Y is complex symmetric, because it is the Hessian of a scalar holomorphic function. It depends only on B|Y. Termwise differentiation is justified by uniform convergence on the larger product ball and the estimates below.

Take the action estimate on radius 2b, the Hessian on radius b, and reserve a small epsilon>0 of cardinality weight. Banach-space Cauchy/polarization gives for each cell block r,s in Y

 ||(B_Y)_(r,s)||_b <= (2 e^2/b^2) ||W_Y||_(2b).                     (5.7)

This bound is independent of |Y| and of the fine dimension. The row sum introduces at most |Y|. Since sup_(n>=1) n exp(-epsilon n)<infinity, (5.5) gives

 sup_r sum_(Y contains r) sum_(s in Y)
       exp[mu tau(Y)+(a-epsilon)|Y|] ||(B_Y)_(r,s)||_b
       <= C b.                                                     (5.8)

Thus D^2 S_M(B)=q_M+sum_Y B_Y(B|Y) has the precise strict-support row property; individual coefficients, not only their sum, are symmetric. This scalar route avoids trying to symmetrize an arbitrary response decomposition after the fact. Choosing mu>=2(kappa_ob+2m_ob) supplies Notebook18's metric-MST weight exp[(kappa_ob+2m_ob)ell(Y)]. The allowed positive ob exponents may be selected small enough to fit the established linear decay.

## 6. Finite-range substitution into the actual current pivot chart

This section states explicitly the interface with `physical_current_pivot_precision_research.md`. At fixed current ratio L, its maps are holomorphic on a fixed product neighborhood in the current potential a=log V/i and the retained coordinate z. Write

 F_cur(a,z)=log[e^(i Phi_V(z)) e^(i a)]/i,   F_cur(a,0)=a,             (6.1)

where Phi_V is the actual nonlinear ordinary-constraint pivot parametrization. Every output cell of F_cur depends only on a,z in a fixed radius R_c, and

 ||F_cur(a,z)||_infinity <= C_L (||a||_infinity+||z||_infinity).        (6.2)

Its coefficients include both the nonlinear constraint curvature and the exponential-coordinate curvature. They must not be replaced by the linear retained extension. Let G_cur(a,z) be the actual local exponential gauge action evaluated at e^(i Phi_V(z))V. Its finite-range analytic dependence is also uniform at fixed L. At the physical background with rooted contour mean one it has the expected quadratic gauge form; on the product background ball it is the full local action, including its curvature terms.

Set

 T_M(a,z)=S_M(F_cur(a,z))+G_cur(a,z).                                 (6.3)

The scalar-action series needed for this composition includes the quadratic baseline. Split (1/2)<B,qB> into scalar pair-supported coefficients. Exponential locality of q gives an anchored support bound of order r^2 with any fixed cardinality reserve and a sufficiently small positive spatial exponent. Add (5.3). Hence S_M itself has an anchored scalar support family S_Y with norm O(r^2) on a fixed small product ball.

Let Gamma Y be the union of the radius-R_c dependency neighborhoods of all cells in Y. There are constants N_c,c_c depending only on R_c and dimension such that

 |Gamma Y| <= N_c |Y|,
 tau(Gamma Y) <= tau(Y)+c_c |Y|.                                   (6.4)

To prove the second inequality, join Y by a minimizing connected graph and attach a fixed finite tree covering each radius-R_c neighborhood. Periodic identifications can only reduce the edge count. In particular no estimate proportional to the total periodic volume is used.

Substitute F_cur into each S_Y, assign support X=Gamma Y, and group equal supports. The coefficient depends only on (a,z)|X. A fixed target weight exp[sigma tau(X)+a_out|X|] is dominated by

 exp[sigma tau(Y)+(sigma c_c+a_out N_c)|Y|].                         (6.5)

The arbitrarily large but fixed input cardinality reserve supplied by Section4 pays (6.5). Rerooting a cell of Gamma Y to a cell of Y costs only the fixed number of cells in a radius-R_c ball. Shrink the joint product radius so that (6.2) lies in the source-action ball. The local gauge coefficients are added directly. We obtain an exact decomposition

 T_M(a,z)=sum_X T_X(a|X,z|X)                                        (6.6)

with a uniform anchored norm for any prescribed fixed a_out and a sufficiently small positive sigma. Supports carry both the original current-background variables and the original retained-coordinate variables; neither is replaced by a background-dependent support.

At z=0 define

 A_X(a|X)=D_z^2 T_X(a|X,0)-D_z^2 T_X(0,0).                          (6.7)

These are complex symmetric retained matrices with rows and columns in X and background dependence only on X. Cauchy with fixed margins in the joint (a,z) ball, followed by integration in t along ta, gives an O(b) estimate for each Hessian difference on ||a||<b. Summing the retained columns costs |X|, which is paid by a cardinality reserve exactly as in (5.8). Thus, for suitable sigma>0,

 sup_r sum_(X contains r) sum_(s in X)
       exp[sigma tau(X)] ||(A_X)_(r,s)||_b <= C_L b.                 (6.8)

The baseline sum sum_X D_z^2 T_X(0,0) is exactly A_M(1), the already identified retained precision K_L^T(q_M+T_L^T T_L)K_L. Consequently

 A_M(V)=A_M(1)+sum_X A_X((log V/i)|X)                                (6.9)

is a strict support-valued expansion on the full small current-background product ball. It is stronger than the previously proved weighted matrix bound for their sum. Its baseline covariance is background-independent and has the uniform spectrum/decay established in the flat notebooks. Choosing ob exponents so that 2(kappa_ob+2m_ob)<sigma and then shrinking b makes (6.8) as small as the precise ob/otg density algebra requires.

The use of an actual action Hessian in (6.7) is essential: it retains the multiplier/constraint-current curvature and the ordinary-coordinate curvature automatically. The argument does not identify an independent arbitrary current parameter with this physical Hessian. It also does not assume that an all-bond nonlinear sharp cutoff becomes a retained product window; the source cutoff issue is separate, as recorded in `pivot_cutoff_source_research.md`.

## 7. A genuinely localized classical interaction remainder

For real retained z in the fixed product window ||z||<=R and small g with gR below a fixed analytic margin, define coefficientwise

 U_X(a;z) = -g^-2 [T_X(a,gz)-T_X(a,0)
                   -g D_z T_X(a,0)[z]
                   -(g^2/2)D_z^2 T_X(a,0)[z,z]].                    (7.1)

The sign is chosen for an action in exp(-g^-2 T); changing that convention changes only the sign, not the estimates. Taylor's integral remainder or one-variable Cauchy along z/R gives

 sup_i sum_(X contains i) exp[sigma tau(X)+a_out|X|]
                sup_(||a||<b,||z||<=R) |U_X(a;z)| <= C g R^3.      (7.2)

No |X|^3 occurs: the direction z|X has product supremum norm at most R, and Cauchy is applied to that Banach-space direction. If one instead differentiates individual coordinates and sums them, the extra support factors can also be paid by reserve, but this is unnecessary.

At a physical stationary background the sum of the linear terms in (7.1) vanishes. On the larger product background domain those linear terms need not vanish; (7.1) remains an exact definition of the cubic remainder and makes no false saddle claim there. The quadratic sum is the actual A_M(V), with (6.9).

For a fixed retained product cutoff put chi_X(z)=product_(i in X) chi_i(z_i) and w_X=chi_X(exp(U_X)-1). Then

 v_X:=sup |w_X| <= exp(||U_X||)||U_X||.

Choose a_out greater than 4+log K_hat plus a positive spare, where K_hat is the fixed density factor in the intended ob/otg theorem. Use ell<=2tau and select kappa_ob with 2kappa_ob<=sigma. Equation (7.2) gives the required interaction norm

 sup_i sum_(X contains i) v_X K_hat^|X| exp[4|X|+kappa_ob ell(X)]
       <= C exp(C g R^3) g R^3.                                    (7.3)

Thus the actual homogeneous classical cubic remainder supplies a usable small interaction input, not just an unweighted extensive remainder. In particular a logarithmically growing cutoff R as g goes to zero is compatible with both gR remaining in the analytic domain and gR^3 tending to zero. The independent Gaussian bad-block tail and the exact ob/otg smallness constants still have to be imposed; this result provides their classical-interaction input and precision-background support input.

### 7.1 Fixed L-block Gaussian cells

The construction so far labels unit current cells. The retained Gaussian theorem may instead use one cell per L-block, with D=d(L^d-1)dim(g) retained real coordinates in the standard pivot convention. Let pi send a unit current cell to its L-block, and regroup every support Y to pi(Y), adding coefficients with the same image. Strict background dependence is preserved. Each unit graph edge either stays in one block or crosses to an adjacent block, hence

 tau_block(pi(Y)) <= tau_unit(Y),   |pi(Y)|<=|Y|.

For a block anchor beta, the sum over Y with beta in pi(Y) is bounded by the sum of the unit-cell anchored norms over the at most L^d cells in beta. Thus all anchored scalar norms acquire at most the fixed factor L^d. For matrix rows, bound a block matrix norm by the sum of its constituent unit-cell block norms, and then sum the at most L^d row cells; the same fixed-factor conclusion holds for absolute row norms. The coordinate rearrangement is fixed at L, and the usual maximum-cell versus Euclidean-block norm equivalence has constants depending only on L and color. A ball radius or cutoff radius may be decreased by this fixed equivalence constant. No M-dependent dimension is introduced. The ob/otg density and tail constants may therefore use the fixed D above after this explicit regrouping.

## 8. Scope, exact dependencies, and checks against overclaiming

* The nonlinear fixed point is expanded about the fixed flat baseline in the original current-cell variables. Coefficients never absorb a nonlocal minimizing background. This is what makes their support strict.
* Arbitrary fixed cardinality reserve is a proved part of the construction, paid by a smaller source ball. A small positive spatial exponent alone would not pay Notebook18's exp(4|X|) or density factor.
* Fine dimension never enters the support counting. Wilson vertices use the complete first-difference jet, smooth cell decomposition and the physical eta^4 sum. The constraint-current vertex uses the already proved physical-adjoint absolute-row norm. The ordinary rooted adjoint is excluded.
* The linear differentiated Green operator is localized between complete Hölder cell spaces using its actual Schauder bound. The proof does not replace that bound by an unjustified absolute singular-kernel integral.
* The corrected scalar action equals the ordinary homogeneous constrained action by the independently established small-field gauge transfer. The actual current pivot chart has fixed ratio L, so its finite dependency radius and coefficient constants are uniform in the old refinement M. Its source identification is exactly the one in the physical-current precision note.
* Finite periodic regulators are primary. Short-period graph estimates hold, but actual source chart incidence still uses the admissible compatible current tori assumed in the physical-chart proof. No thermodynamic consistency of an arbitrarily chosen regrouping, mixed-history source theorem, beta-function estimate, running effective-coupling control, or interacting continuum limit is asserted.
* The result supplies strict-support precision and classical interaction coefficients on one fixed small homogeneous current-background ball. A full iterative quantum theorem also needs preservation of the appropriate domains and bounds for all additional effective polymer/current terms. Those conclusions do not follow from the present classical theorem alone.

All inputs above are explicitly available in the named research proofs and Notebooks15--18. The new work here is the support-family contraction, arbitrary cardinality reserve, scalar-envelope rerooting/differentiation, and fixed-range current-chart transfer. Both internal audits checked these four steps. The manuscript fragment is `classical_support_localization_fragment.tex`; its standalone wrapper compiled successfully.
