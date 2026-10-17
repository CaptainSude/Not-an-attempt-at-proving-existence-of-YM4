# Inherited quantum activities in the next actual fluctuation chart

Research candidate, 17 October 2026. This note identifies a concrete finite-step interaction bound and the remaining norm/domain obstruction to iteration. It uses the actual source pivot chart, not a replacement coordinate system. Statements labelled proved below follow from the already audited chart and elementary complex analysis. A specified large-block inequality is sufficient for re-entry into Notebook18, but the existing fixed-L estimates do not establish that this inequality can be met for the actual output constants as L varies. No new output artifact is promoted here.

## 1. Three different cell labels and the exact insertion

At the end of Notebook22's stationary substitution, the transported activities are functions of the next-coarse link potential w. At the following step rename this potential a: it is now a *unit-spacing current* potential. Its connected carriers H consist of current unit cells, with at most D_0=d dim(g) scalar link/color coordinates per cell. This is different from the preceding Gaussian representation, whose carriers were L-block cells of the previous current lattice.

For this following integration, group current variables into L-block Gaussian cells. The retained real Gaussian dimension is

    D_G=d(L^d-1)dim(g),                                              (1.1)

and the independent background fiber per such block has dimension

    D_bg=dL^d dim(g).                                                (1.2)

The next coarse datum is W=exp(i w), the matched physical stationary current field is V_*(W)=exp(i a_*(w)), and the actual fluctuation insertion is

    U=exp(i Phi_{V_*(W)}(g xi)) V_*(W).                              (1.3)

The retained cutoff is the original source window in xi; Phi preserves its retained coordinates exactly. There is no replacement by an all-link linear window. Any additional source indicators remain additional factors.

It is useful first to keep the current background independent. Define

    F(a,z)=log[exp(i Phi_{exp(i a)}(z)) exp(i a)]/i,
    F(a,0)=a,                                                       (1.4)
    Delta E_H(a,xi)=E_H(F(a,g xi)|H)-E_H(a|H).                       (1.5)

Then the exact actual-background decomposition is

    sum_H E_H(log U/i|H)
      =sum_H E_H(a_*(w)|H)+sum_H Delta E_H(a_*(w),xi).               (1.6)

The first term is fluctuation-independent and is transported by Notebook22. The second is the inherited interaction for the present integral. There is no factor g^-2 in (1.5): E_H is already a dimensionless quantum exponent, unlike the classical action divided by g^2. No claim that the quantum stationary point equals the classical one is needed for this exact splitting. Linear and quadratic terms of (1.5) may remain bounded interactions.

## 2. Proved local displacement estimate and dimension-free directional Cauchy

Assume the inherited activity is bounded holomorphic on the product scalar-coordinate domain |a|<b, with e_H=||E_H||_b and

    sup_i sum_(H contains i) exp(a0|H|) e_H <= epsilon,
    a0>0,    H connected.                                          (2.1)

The actual source chart is analytic on fixed product neighborhoods in (a,z), at fixed L. Its finite-range derivative bounds in `physical_current_pivot_precision_research.md`, Sections3 and6, imply constants b_ch,z_ch,C_ch(L)>0 with

    ||F(a,z)-a||_infinity <= C_ch(L)||z||_infinity                    (2.2)

for ||a||<b_ch and ||z||<z_ch, in scalar maximum coordinates. All fixed color/fiber norm conversions are included in these constants. They are uniform in old refinement M and volume; no large-L uniformity is asserted.

Choose b_-<min(b,b_ch), put m=b-b_->0, and impose

    |g|R<z_ch,
    delta=C_ch(L)|g|R < m.                                         (2.3)

On ||a||<b_- and the retained window ||xi||<=R, (2.2) implies

    ||Delta E_H|| <= u e_H,
    u=delta/(m-delta).                                              (2.4)

If delta<=m/2, then u<=2C_ch(L)|g|R/m.

Proof. For a fixed allowed (a,xi), let h=F(a,g xi)|H-a|H. The one-complex-variable function f(zeta)=E_H(a|H+zeta h) is holomorphic and bounded by e_H for |zeta|<m/delta. Its Taylor series therefore gives

    |f(1)-f(0)| <= e_H sum_(n>=1)(delta/m)^n
                 =e_H delta/(m-delta).

The same bound holds uniformly in the independent complex background. The actual map (1.4) is holomorphic in that background, so (1.5) is also holomorphic. No derivative of a real cutoff is taken. This proof is dimension-free because it estimates the value of one directional increment, not an absolute sum of multivariate Taylor coefficients. It does not contradict the D|H| coefficient cost in Notebook22's strict support substitution: these are different estimates.

On the whole real fluctuation space, multiply exp(Delta E_H)-1 by the cutoffs of all fluctuation cells it reads and extend by zero. This is the bounded measurable multiplier required by Notebook18. The displayed estimate is needed only on that cutoff region.

## 3. Proved projected support geometry of the actual pivot map

Use positive oriented current bonds and assign a bond to its initial current site. Let pi_L map current sites to centered L-blocks. A pivot p(c) for c=(y,y+L e_mu) is the positive current bond crossing the common interface on the line of the two block centers. Its initial site belongs to the y-block. In the source geometry with distinct interfaces, the exact constraint for c reads only this pivot, the nonpivot strings between these endpoint blocks, and the internal root contours in the same two blocks.

Two facts sharpen a generic fixed-radius enlargement:

1. If b is a nonpivot bond, Phi_V(z)(b)=z(b) exactly. Hence F(a,z)(b)=log[exp(i z(b))exp(i a(b))]/i reads only that bond's a and z coordinates.
2. If b=p(c), the output Phi_V(z)(p(c)) is the unique solution of its own finite-dimensional pivot equation. Its background and retained-variable dependencies lie in the two endpoint L-blocks of c. Iteration of that equation does not propagate through other pivots. The final logarithm in (1.4) is bondwise.

For an input carrier H, define the projected declared carrier

    Y(H)=pi_L(H) union
         {the other endpoint block of c: p(c) starts in H}.         (3.1)

Include every block's full independent background and retained fiber if necessary. Then Delta E_H(a,xi) reads only (a,xi)|Y(H). If H is connected, pi_L(H) is connected and every extra block is adjacent to a block already in pi_L(H); thus Y(H) is connected. In particular

    ell(Y(H))=|Y(H)|-1.                                             (3.2)

There are at most d outward pivot endpoint blocks per block in pi_L(H). Therefore, with chi=d+1,

    |Y(H)| <= chi |pi_L(H)|.                                        (3.3)

For any anchor block B,

    1_(B in Y(H)) <= sum_(i in H) 1_(d_block(B,pi_L(i))<=1).         (3.4)

The safe neighbor multiplicity in (3.4) is N_near=2d+1. With the positive oriented convention it could be reduced, but no such improvement is needed. If a different cell assignment reads both incoming and outgoing endpoints, replace chi by 2d+1; the argument remains a fixed-neighbor estimate.

This is stronger than replacing H by every current site in a radius-O(L) ball and then paying O(L^d)|H|. That crude enlargement can erase the useful geometric compression. The actual one-pivot incidence is what gives (3.3).

The construction keeps the independent background a. Substituting a_*(w) inside (1.5) before the Gaussian expansion creates generally nonlocal w dependence, so Y(H) alone would no longer be its strict *w*-support. Section7 explains the correct order of operations.

## 4. A precise sufficient Notebook18 interaction norm

Group equal carriers first, defining the exact holomorphic exponent

    Q_Y(a,xi)=sum_(H:Y(H)=Y) Delta E_H(a,xi).                        (4.0)

The anchored absolute bounds below justify this sum. Notebook18's tunable real-baseline strict-support theorem uses the sufficient interaction norm

    epsilon_int = sup_B sum_(Y contains B)
       v_Y Kcal_theta^|Y| exp[4|Y|+kappa ell(Y)],                    (4.1)

where v_Y=sup_cutoff|exp(Q_Y)-1| and

    Kcal_theta=((1+theta)/(1-theta)^3)^(D_G/2),
    0<theta<=1/4.                                                   (4.2)

The theorem also permits retaining H as separate interaction labels with the same support. We give the grouped version to make the exponent and multiplier distinction explicit. The strict version is used here; the non-strict analogue has the smaller density factor K_theta=((1+theta)/(1-theta))^(D_G/2).

Set

    B_req=4+log Kcal_theta+kappa.                                   (4.3)

By connectedness, the weight in (4.1) is at most exp(B_req |Y|). Equations (2.4) and (3.4) first give the unweighted anchored bound

    sup_B sum_(Y contains B)||Q_Y|| <= u N_near L^d epsilon=:V_max.

In particular every ||Q_Y||<=V_max, and the exact multiplier estimate is

    v_Y <= exp(||Q_Y||)||Q_Y|| <= exp(V_max)||Q_Y||.                 (4.4)

For odd L>=5 define k_L=1+floor(((L-1)/2-1)/2), as in the connected-carrier compression lemma. That lemma and (3.3) give

    |Y(H)| <= chi 2^d + (chi 2^d/k_L)|H|.                           (4.5)

Therefore the explicit sufficient weight inequality is

    (chi 2^d/k_L) B_req <= a0.                                     (4.6)

Under (2.3) and (4.6), the inherited increment obeys both

    sup_B sum_(Y contains B) exp[B_req |Y|] ||Q_Y||
       <= u exp(B_req chi 2^d) N_near L^d epsilon,
    epsilon_int
       <= exp(V_max) u exp(B_req chi 2^d) N_near L^d epsilon.        (4.7)

If V_max<=log2, the last prefactor exp(V_max) is at most two. For separate H labels it is enough to impose u epsilon<=log2 to obtain the same factor-two version directly. Grouping cannot be accompanied by the unjustified assertion that the supremum of each grouped exponent is still bounded by u epsilon; the safe bound is V_max.

Proof. Use (4.5) to dominate the target weight by exp(B_req chi 2^d)exp(a0|H|). Reroot (3.4) to current sites. At most N_near L^d current sites lie in blocks at graph distance at most one from B. Apply (2.1) at each such site. This proves (4.7). The coefficient is uniform in M and volume but can be enormous as a function of fixed L.

If further factors cost a polynomial in |H|, impose a strict margin rho=a0-(chi 2^d/k_L)B_req>0 and pay them with sup_k k^q exp(-rho k). No unmentioned reserve is assumed. The present first-order value estimate itself does not need this polynomial margin.

This is a genuine sufficient re-entry lemma, conditional on the numerical inequality (4.6). It handles the edge-geometry weight in (4.1), not only exp(4|Y|), because Y(H) is declared connected and (3.2) was used. For a nonconnected declaration, a separate spatial cost would be needed.

## 5. Dimension scaling, covariance neighborhood, and cutoff budget

Without the real-baseline refinement, the per-cell density factor in Notebook18 has log K_G of order D_G. Since D_G is of order L^d, its contribution to the left side of (4.6) is of order L^(d-1), rather than a small compression cost. Merely choosing large blocks would therefore not solve the sufficient norm inequality by that crude bound.

The tunable estimate changes this particular dimension problem. For theta<=1/4,

    log Kcal_theta <= (5/2)D_G theta.

Choosing theta=1/(4D_G) gives

    log Kcal_theta <=5/8,
    B_req <= 37/8+kappa.                                           (5.1)

This removes the artificial exponential-in-D_G interaction cost. It does not remove all dimension dependence:

* The covariance-edge Cauchy radius is proportional to theta, and its inverse constant grows at least like D_G.
* The actual covariance and its strict local precision expansion must lie in the strengthened O(theta) neighborhood of the real baseline. Notebooks19 and21 allow a sufficiently small independent current-background ball for each fixed theta and fixed L, but give no common large-L domain here.
* The bad-cell probability still contains 2^(D_G/2). Its cutoff must satisfy the explicit Gaussian tail smallness condition, for example R^2/(4 rho_theta Lambda_0) exceeding (D_G/2)log2 plus the required logarithmic budget. Here rho_theta=(1+theta)/(1-theta) and Lambda_0 is the baseline covariance upper bound.
* Keep the two directions of the cutoff comparison separate. For the actual linkwise color-ball window chi_B=product_(b in B)1{|xi_b|<=R}, its bad event is contained in {||xi_B||_2>R}. Thus a joint Euclidean-block Gaussian tail with threshold R is a valid upper bound. The good event only implies ||xi_B||_2<=sqrt(n_B)R, where n_B=d(L^d-1) is the number of retained links. That latter bound cannot be used to replace the bad-event threshold by sqrt(n_B)R. The chart uses scalar/link supremum and therefore uses the original R directly in (2.3). If a separate theorem instead imposes a Euclidean block window, the exact indicator must be retained or compared in the correct direction, not silently identified with the linkwise window. Fixed color-coordinate polydisc conversions are included in the chart constants.

For a fixed chosen L, these are finite constants. A logarithmically growing R(g) is compatible with gR(g)->0 as g->0, so (2.3) and a fixed required tail threshold can be met after choosing g sufficiently small. This does not supply the actual all-scale coupling recursion or show that its values meet the same inequalities at every step.

## 6. What is not proved by selecting a large L

The compression coefficient in (4.6) is O(1/L), but the activity reserve supplied by an actual previous integration is a0=a0(L), not an independently prescribed constant. The current Gaussian/locality proofs establish a positive reserve for each fixed L. They do not provide a quantitative lower bound ensuring

    k_L a0(L) > chi 2^d [4+log Kcal_theta(L)+kappa(L)].               (6.1)

For example, the abstract assertion a0(L)>0 for every L is consistent with a0(L)=exp(-L); that assertion alone cannot imply (6.1) for any sufficiently large L. This is a limitation of the available estimates, not a counterexample to the actual Yang--Mills model. A quantitative source-covariance/locality estimate as L varies, or a sharper integration theorem with smaller fixed carrier cost, is a concrete next input.

The old activity radius is equally significant. To use the current source chart, choose b_-<b and then a next coarse radius r with

    ||a_*(w)||_infinity <= C_a(L) r <= b_-.

Notebook22's coefficient-level transport generally asks for a stronger shrink, roughly C_a(L)r/b of order a0/D_bg. No L^-1 contraction in angle supremum follows from the physical units. The already identified pure-gauge branch can have current boundary-link angle of order w, rather than w/L. Thus repeated domain stability is not supplied by the one-step estimates. A decreasing domain sequence can be defined formally, but no existing theorem says it is compatible with all subsequent quantum contours, cutoffs, and observable domains.

Moreover the multiplicative constant in (4.7), and the constants in stationary transport, need not be below one. Relevant and marginal sector extraction remains necessary for any actual induction claim. The bare existence of a bounded analytic substitution is not an RG contraction.

## 7. Correct order of strict support operations

The following finite-step order is justified by the present results.

1. Treat a as an independent current product background. Build the actual baseline covariance and the classical, measure, gauge and inherited multipliers in their exact source coordinates. The inherited pieces (1.5) have strict joint (a,xi) support Y(H) and satisfy (4.7) if its budget holds.
2. Apply the strict-support version of Notebook18 uniformly on that independent background ball, with the actual retained cutoff and all stated covariance/locality hypotheses. It produces analytic coefficients in the original a variables.
3. Evaluate at the actual stationary a=a_*(w), and transport the resulting coefficients by Notebook22. This is an exact substitution of an already holomorphic identity; the connected-carrier and radius costs of that transport remain explicit.

Equivalently, (1.6) separates the old fluctuation-independent contribution from the new integral. The old part is transported as an activity family; it is not discarded as a constant unless it is actually independent of w.

If instead a_*(w) is inserted before applying the Gaussian theorem, the covariance and the inherited increment generally have nonlocal w dependence. One can expand that dependence in the rooted support algebra, but the connecting background trees then cost their own spatial/cardinality reserve. The carrier Y(H) in Section3 alone is not a strict w-support. In particular a small available background exponent kappa cannot automatically pay the exp(4|X|) input norm for enlarged joint carriers. Applying the uniform independent-background identity first avoids this unnecessary interchange; it does not avoid the later Notebook22 radius and weight losses.

The parameter xi may be held fixed while applying a support substitution, but its w-independent Taylor terms are still functions of xi. Such terms belong to the fluctuation interaction with their original xi carrier; they are not vacuum constants. This is another reason to keep the two stages distinct.

## 8. A conditional small interaction comparison and the remaining target

Suppose the covariance hypotheses of Notebook18 hold on the chosen independent-background ball. Let eta_* be its common smallness threshold, let eta_base be the sum of its tail contribution and the existing classical/measure/gauge interaction norm, and write its output estimate in the form ||U||_out<=C_out eta whenever eta<=eta_*. Here the output is the exact canonical connected strict-background support norm at the theorem's displayed positive exponent, not merely a bound on the scalar logarithm.

Assume eta_base<=eta_*/4 and epsilon_int<=eta_*/4. Multiply only each inherited bounded multiplier w_Y=chi_Y(exp(Q_Y)-1) by a complex parameter lambda, keeping the base family fixed. The integral is the base integral at lambda=0 and the actual integral at lambda=1. It is not necessary to replace Q_Y by lambda Q_Y. Base and inherited factors sharing one carrier remain distinct labelled hyperedges, which the overlap theorem permits; there is no cancellation or division by a base factor. On the disk

    |lambda| <= R_lambda=eta_*/(2 epsilon_int) >=2,

the total budget is at most 3eta_*/4. The canonical connected coefficient vector U(lambda) is therefore holomorphic in the output Banach space and has norm at most C_out eta_*. Banach-valued Cauchy gives

    ||U(1)-U(0)||_out
      <= C_out eta_*/(R_lambda-1)
      <=4 C_out epsilon_int.                                      (8.1)

If epsilon_int=0 this is immediate. Thus the same expansion integrates the inherited multipliers, and their contribution to the generated *connected logarithm coefficients* is O(epsilon_int) in the precise strict-support norm. The original fluctuation-independent sum E_H(a) remains outside this comparison integral. It is transported after evaluation at a_*(w), together with the new coefficients, on their common smaller product domain. The constants and the output exponent depend on the same fixed covariance and support budgets; no iteration is inferred.

The resulting finite-step picture is therefore:

* old background term: bounded stationary transport of epsilon, with the explicit Notebook22 domain and support loss;
* new inherited fluctuation effect: O_L(epsilon gR/(b-b_-)) under the explicit re-entry weight inequality (4.6);
* existing classical/measure/gauge integral: already treated by the previous notebooks;
* remaining induction obligations: quantitative a0(L) and covariance locality, stable domains, extracted relevant/marginal couplings, and large-field/observable sectors.

The first focused next lemma is quantitative rather than formal: determine an actual lower bound for the available connected-carrier reserve a0(L), together with the covariance-edge scale, strong enough to test (6.1). If (6.1) fails for the available constants, improve the fixed carrier cost in the Gaussian expansion or use a different explicitly controlled localization/blocking scheme. It would be incorrect simply to assume that an unspecified sufficiently large L cures the mismatch.
