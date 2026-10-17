# Strict-support transport of holomorphic quantum activities

Research candidate, 17 October 2026. This note proves a bounded, finite-step substitution theorem. Its actual stationary-background input is the rooted support expansion constructed in `coarse_stationary_support_research.md` (or any precisely matching family); that candidate is a separate theorem with its own audit. No convenient replacement background is substituted for the source background. No quantum induction, common domain under repeated steps, or contraction of a renormalization map is claimed.

The principal point is that the input quantum activities need only one fixed positive support-cardinality reserve. There is no assumption of arbitrary reserve and no dimension-free absolute Taylor estimate. The number of scalar Taylor coordinates is proportional to the input carrier size, and its exact cost is displayed below. The old refinement M and compatible periodic volume do not enter the constants. The blocking factor L is fixed.

## 1. Geometry, input activities, and the assumed actual background

Let Lambda be the current-cell graph and Lambda' its next-coarse block graph. Let pi:Lambda -> Lambda' map current cells to L-blocks. More generally, the proof needs only these properties:

* Every fiber has at most F cells; for L-cube blocking, F=L^d.
* The image pi(H) of a connected current carrier H is connected and nonempty.
* Lambda' is a compatible periodic lattice, with graph distance d'. Thus, for delta>0,

      S_delta = sup_z sum_j exp[-delta d'(z,j)]
              <= sum_(j in Z^d) exp[-delta |j|_1] < infinity.          (1.1)

Short periodic directions do not spoil (1.1): choose one minimal-distance representative of each periodic site in Z^d. If the activities are already indexed by the same block graph as the new background, take pi=identity and F=1.

**Actual Notebook18/21 convention.** The normalized Gaussian output activities in the present physical application are already carried by L-blocks of the current unit lattice. The next-coarse w labels are that same L-block index graph. For this transport, therefore, pi=identity and F=1. The background fiber contains all current links assigned to an L-block, so its scalar dimension is D_bg=d L^d dim(g), with the stated fixed norm conversion. It is not the retained Gaussian dimension D_z=d(L^d-1)dim(g). The nontrivial pi_L projection of Section 6 becomes relevant only when these transported next-current activities are regrouped into the following integration's L-block Gaussian cells. It must not be counted as an extra coarsening gain during the present substitution.

Each old cell carries at most D scalar complex background coordinates. An activity E_H(a|H) is bounded and holomorphic on the coordinate product polydisc

      |a_i^alpha| < b,   i in H, 1<=alpha<=D,                         (1.2)

and H is a nonempty connected set. Put e_H=||E_H||_b and assume only

      sup_i sum_(H contains i) exp(a0 |H|) e_H <= epsilon,
      a0>0 fixed.                                                    (1.3)

Unused coordinates can be included in (1.2) without changing the function. If the original domain is a product of fixed-dimensional Euclidean balls of radius b_E, use the scalar polydisc radius b=b_E/sqrt(D), or the corresponding fixed norm-equivalence constant. The letter D always counts actual scalar background coordinates per old carrier cell; it is not the number of retained Gaussian coordinates unless those are the coordinates in (1.2).

The next-coarse field w has a product domain of radius r. Assume that the *actual* stationary background has an exact expansion

      a_i^alpha(w) = sum_(nonempty X subset Lambda') u_(i,alpha;X)(w|X),
      u_(i,alpha;X)(0)=0,                                            (1.4)

where every summand is strictly a function of its displayed variables. Let tau be graph Steiner length on Lambda': auxiliary vertices are allowed. Suppose, for a fixed kappa>0,

      sup_(i,alpha) sum_X exp[kappa tau({pi(i)} union X)]
                          ||u_(i,alpha;X)||_r <= s(r),
      s(r) <= C_a r.                                                 (1.5)

It is enough to have (1.5) with a common vector-coordinate maximum norm, which bounds every scalar component. A stronger rooted norm with exp(a|X|), supplied by the classical support construction, is allowed but not used in this theorem. In particular it is not silently transferred to the quantum activities.

If the support family has only a_i(0)=0 after summation, replace u_X by u_X-u_X(0). Absolute convergence shows that the sum is unchanged, each summand now vanishes at zero, and s increases by at most a factor two. Incorporate that factor in C_a. When the stationary branch is expanded about a nonzero reference a_ref instead, (1.2) must be centered at that reference and (1.4) must represent a-a_ref; the available distance to the analytic boundary replaces b.

The background support theorem naturally groups all old cells in one next-coarse block into one fixed-dimensional fiber. Its maximum-coordinate estimate gives (1.5) for every old i without summing over that fiber. Conversely, one may first group input carriers by pi(H); the anchored norm then costs at most F, and the coordinate count becomes the full fixed block dimension. The direct formulation here avoids that unnecessary enlargement of D and retains the original H for the refined geometric estimate in Section 6.

## 2. The transport theorem and explicit loss budget

Choose a_out>=0, mu>=0 and delta>0, and set

      beta = a_out+mu,
      t = s(r)/b < 1,
      alpha(t) = D log(1/(1-t)).                                      (2.1)

Assume

      beta+delta <= kappa,
      beta+alpha(t) <= a0.                                          (2.2)

Then there are holomorphic activities E'_K(w|K), indexed by nonempty connected next-coarse carriers K, with E'_K(0)=0, and a field-independent vacuum constant Vac_Lambda, such that

      sum_H E_H(a(w)|H) = Vac_Lambda + sum_K E'_K(w|K),
      Vac_Lambda = sum_H E_H(0).                                    (2.3)

The equality and the sums converge absolutely on the next product domain. With ell(K) the metric minimum spanning-tree length,

      sup_z sum_(K contains z) exp[a_out |K|+mu ell(K)] ||E'_K||_r
          <= F S_delta epsilon.                                    (2.4)

In particular the resulting support weight is explicitly limited by (2.2). An input exponent a0<=1/2 does not automatically produce a later required exponent 4. Formula (2.4) is bounded transport; its constant can exceed one.

One convenient strictly positive choice, without any geometric improvement, is

      beta = min(a0/4,kappa/4),
      a_out=mu=beta/2,  delta=kappa/4,
      s(r)/b <= min(1/2,a0/(8D)).                                   (2.5)

Indeed alpha(t)<=2Dt<=a0/4, so both conditions have spare margin. Thus it suffices to take

      r <= (b/C_a) min(1/2,a0/(8D)),                                (2.6)

as well as any radius restriction needed to construct (1.4). All norm-equivalence or centering factors must be included in C_a or b before using (2.6). This explicitly displays the loss of background radius. A fixed L-dependent C_a need not be less than one.

## 3. Exact construction and the coefficient count

Expand E_H at zero in the actual D|H| scalar coordinates:

      E_H(a|H) = sum_(nu in N^(D|H|)) c_(H,nu) a^nu,
      |c_(H,nu)| <= e_H b^(-|nu|).                                 (3.1)

The estimate follows by coordinatewise Cauchy on smaller polydiscs followed by a limit. There is no polarization factor, missing factorial, or bound that is independent of |H|. For every occurrence of a scalar coordinate in a^nu insert its support series (1.4). A resulting decoration consists of H, nu, and one support X for every scalar occurrence, with root pi(i) inherited from that scalar coordinate.

For each rooted support ({pi(i)} union X), fix a deterministic minimizing connected tree T(i,X) in Lambda'. Its length is tau({pi(i)} union X). Ties may be broken by any fixed finite-volume rule. Put

      K = pi(H) union union_(all occurrences) vertices T(i,X),
      T_tot = sum_(all occurrences) tau({pi(i)} union X).             (3.2)

The original projected carrier pi(H) is retained even if many of its variables do not occur in the monomial. It is connected, and each added tree has a root in pi(H). Therefore K is connected, contains every actual variable support, and

      |K| <= |pi(H)|+T_tot,
      z in K  implies  d'(z,pi(H)) <= T_tot.                         (3.3)

The second fact uses the length of the individual attached tree containing z; its length is at most T_tot. An edge tree of length t has at most t new vertices after attaching at its root, which proves the first fact even when trees overlap or wrap around a torus.

Every nonconstant decorated term is a strictly supported holomorphic function of w|K and vanishes at zero. Define E'_K to be the sum of these terms with carrier K. Define the vacuum from the nu=0 terms separately. It is permitted that a function assigned to K actually reads a smaller set: K is its declared connected carrier, not a claim of minimal dependence. This harmless enlargement is crucial. Dropping the original H or the connecting vertices would lose the anchored estimate.

Because K is a connected set of lattice vertices, its metric MST length is exactly |K|-1. A spanning tree of the connected induced graph gives the upper bound; every metric tree has |K|-1 edges, each of distance at least one, giving the lower bound. Thus

      exp[a_out |K|+mu ell(K)] <= exp(beta |K|).                     (3.4)

The use of graph Steiner length for the attached forests is essential: deleting intermediate roots from a terminal metric MST need not decrease its length. No false MST-union inequality is used. At the output, we deliberately keep the connecting vertices, so the exact connected-carrier identity just used supplies the stated MST norm.

## 4. Anchored estimate and absolute convergence

Write h=|pi(H)| and k=|H|. From (3.3), for any fixed output anchor z,

      1_(z in K) exp[a_out |K|+mu ell(K)]
        <= exp(beta h) exp[-delta d'(z,pi(H))]
           product_(occurrences) exp[(beta+delta) tau({pi(i)} union X)].
                                                                         (4.1)

If z is absent the inequality is automatic. Otherwise insert
1<=exp[delta(T_tot-d'(z,pi(H)))] into (3.4). Since beta+delta<=kappa, summing each scalar occurrence over its support X is bounded by s(r), using (1.5). Summing the scalar multiindices exactly gives

      sum_nu t^|nu| = product_(Dk coordinates) (1-t)^(-1)
                    = exp[alpha(t) k].                              (4.2)

For nu!=0 the corresponding sum is exp[alpha(t)k]-1, and it is bounded by (4.2). The total absolute contribution from a fixed input H to the anchored output norm is consequently at most

      e_H exp[beta h+alpha(t)k] exp[-delta d'(z,pi(H))].               (4.3)

Use h<=k and (2.2). The remaining rerooting cost is summable because

      exp[-delta d'(z,pi(H))]
        <= sum_(i in H) exp[-delta d'(z,pi(i))].                     (4.4)

Hence the sum of (4.3) over H is at most

      sum_i exp[-delta d'(z,pi(i))]
             sum_(H contains i) exp(a0 |H|) e_H
        <= F S_delta epsilon.                                      (4.5)

This proves (2.4). It also proves absolute convergence of the positive majorant for every coefficient grouping. At finite volume the sum over output anchors bounds the total absolute sum; the exact substitutions and regroupings are therefore justified. Normal convergence on the product domain, or first on every smaller polydisc, gives holomorphy of each E'_K. The statement is uniform in finite volume and old refinement. It does not imply consistency of the particular chosen support coefficients between different volumes; such consistency requires compatible input families and choices.

The proof counts scalar monomials before grouping identical support carriers. It never bounds a degree-n coefficient by |H|^n and then omits the resulting factorial. The factor exp[alpha(t)|H|] is precisely the cost that the fixed input reserve pays.

## 5. Vacuum normalization and a sharper radius-dependent bound

The vacuum in (2.3) obeys

      |Vac_Lambda| <= |Lambda| epsilon.                             (5.1)

A local density assignment is

      v_i = sum_(H contains i) E_H(0)/|H|,
      Vac_Lambda=sum_i v_i,  |v_i|<=epsilon.                         (5.2)

Grouping these densities into next-coarse blocks costs at most F. Field-independent vacuum normalization is therefore explicit; it is not lost inside a nonconstant activity estimate.

If there is strict reserve

      rho = a0-beta-alpha(t)>0,                                    (5.3)

the nonconstant family satisfies the sharper bound

      ||E'||_(a_out,mu;r)
        <= F S_delta epsilon alpha(t) C_rho,
      C_rho = sup_(k>=1) k exp(-rho k) <= 1/(e rho).                 (5.4)

Indeed exp(alpha k)-1<=alpha k exp(alpha k), and insert the spare exp(-rho k) in (4.3). One may use the smaller of (2.4) and (5.4). This shows that a vacuum-subtracted family becomes small on a sufficiently smaller w domain. It is not a scale contraction at a common analytic radius. In particular (2.6) must not be iterated without proving a compatible domain recursion for the actual stationary background.

## 6. Optional gain from connected-carrier compression

The general proof retains h=|pi(H)| in (4.3). Suppose a geometric estimate gives

      |pi(H)| <= c0+c1 |H|                                        (6.1)

for all connected H. Replace the second condition of (2.2) by

      c1 beta+alpha(t) <= a0.                                     (6.2)

The same construction then proves

      ||E'||_(a_out,mu;r) <= exp(beta c0) F S_delta epsilon,          (6.3)

still subject to beta+delta<=kappa. The sharper nonconstant bound (5.4) also holds with the prefactor exp(beta c0) and rho=a0-c1 beta-alpha(t)>0.

For fixed odd L>=5, `connected_carrier_coarsening_research.md` proves

      r_L=(L-1)/2,  s_L=floor((r_L-1)/2),  k_L=s_L+1,
      |pi(H)| <= 2^d max(1,|H|/k_L)
               <= 2^d+(2^d/k_L)|H|.                              (6.4)

Thus c0=2^d and c1=2^d/k_L are available. For completeness, choose a maximal subset of H separated by at least r_L in the sup metric. The sup balls of radius r_L-1 cover H and each meets at most 2^d coarse blocks. If there is more than one center, their graph balls of radius s_L are disjoint. A connecting path in H to another center supplies at least k_L vertices in each such ball. This proves (6.4), including on compatible short periodic tori by the same periodic-distance argument.

Consequently sufficiently large fixed L can pay a stronger output cardinality reserve from a smaller input a0. However the attached stationary-background trees must also support beta+delta<=kappa at the *next-coarse* scale. A small existing kappa cannot be enlarged merely by assertion. If a separate block-regrouping argument supplies a stronger stationary-background exponent, its cardinality and domain costs must be included first. Formula (6.3) alone does not close the Notebook18 input/output norm loop. Its constant exp(beta 2^d)L^d S_delta can be large.

For the actual convention identified in Section 1, current stationary substitution uses pi=identity. Subsequent regrouping of its connected carriers K for the *following* integration can use (6.4) as a distinct operation. There is no second projection hidden inside (2.3), and no gain may be counted twice. A proposed induction must state at each stage which graph labels the activities, their background coordinates, and the Gaussian blocks before applying either estimate.

## 7. Necessary assumptions and limits of the result

**Connected input carriers.** This hypothesis is genuinely used. Without it, let the identity background map act on an activity supported on two sites at arbitrarily large separation, with fixed size and fixed nonzero coefficient. A cardinality-only input norm does not penalize the separation. Any connected output carrier must have size at least their distance plus one, so no positive connected-carrier weight can be uniformly bounded. Alternatively a spatially decaying input norm could pay that cost, but it is not assumed here.

**No automatic contraction.** If E_{ {i} }=c is a constant singleton activity at each old cell, coarsening sums F such constants in a full next block. This already rules out a contraction of the full activity norm by geometry alone. After removing the vacuum, the identity background map and a linear singleton activity have no strict contraction at the same radius. The small factor in (5.4) comes from an explicit radius loss, not from a proof that relevant and marginal sectors contract.

**Actual background required.** The theorem applies to a_*(w) only after its exact source chart, gauge-zero representative, stationarity, and rooted family (1.4)--(1.5) are established on the stated domain. A one-weight response estimate for a_* alone does not supply this family. The current theorem is an exact conditional bridge from that family, not a replacement construction of a_*.

**Finite-step quantum boundary.** The theorem transports already supplied quantum activities. It does not prove that the interacting quantum stationary point equals the classical stationary branch, nor does it absorb inherited interactions into a new classical minimization unless a separate argument does so. It gives neither an all-scale running-coupling recursion nor control of large-field pieces or observable insertions. Uniform volume bounds do not imply a thermodynamic or continuum limit.

**What is now actionable.** Once the actual stationary family is verified, its radius r may be chosen using (2.6), and the inherited activity family has the explicit lower-weight norm (2.4). If stronger target support weights are needed for the next Gaussian integration, use the exact budget (6.2) together with a separately verified next-scale background exponent and domain. Those are concrete remaining interfaces; the bounded substitution itself has no hidden factorial or volume loss.
