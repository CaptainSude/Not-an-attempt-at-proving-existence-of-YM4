# Analytic transport around a local core with only the tail expanded

17 October 2026. Research lemma candidate for the next domain question. The abstract transport estimate below is proved from its displayed hypotheses. Its application to a full inherited quantum integral is not established. In particular, a core-amplitude margin is an assumption of the generic lemma, and the existing physical one-step rooted representative is not known to provide a common-radius contraction.

## 1. Data and norms

Let Lambda be an old carrier graph and Lambda' a target graph with bounded degree and uniform exponential sums

    S_delta=sup_z sum_y exp(-delta d(z,y))<infinity.

The primary scalar identity is on compatible finite periodic quotients; the usual shortest-representative bound gives the same S_delta. The coefficient and anchored activity estimates also make sense on infinite graphs, but a total infinite-volume scalar sum is not asserted. Let pi:Lambda->Lambda' have fibers of size at most F. Old activities E_H have connected finite carriers H, at most D scalar input coordinates per old cell, and are bounded holomorphic on the scalar product polydisc of radius b. Set e_H=||E_H||_b and assume

    sup_i sum_(H contains i) exp(a0 |H|) e_H <= epsilon.       (1.1)

All target fields w lie in a fixed product polydisc of radius r. Let f(w) be the current field to be substituted. For each H, write its restriction as

    f|H = f^0_H + v_H.                                     (1.2)

The core f^0_H is holomorphic and depends only on a declared connected target carrier K0(H) containing pi(H). Require constants c0,c1,h0, independent of H and volume, such that

    |K0(H)| <= c0+c1|H|,
    K0(H) subset {z:d(z,pi(H))<=h0},                        (1.3)
    sup_(||w||<r) ||f^0_H(w)||_infinity <= b-m,
    0<m<b.                                                  (1.4)

The halo condition in (1.3) is separate from the size bound. Size and connectedness alone do not control the distance of a declared core carrier from pi(H).

For each old scalar coordinate i,alpha occurring in H, the tail is represented by

    (v_H)_(i,alpha)(w)=sum_(nonempty X) v_(H;i,alpha;X)(w_X), (1.5)

with strict holomorphy, v_(H;i,alpha;X)(0)=0, and a uniform rooted bound

    sup_(H,i in H,alpha) sum_X
       exp[kappa tau({pi(i)} union X)]
       ||v_(H;i,alpha;X)||_r <= s.                          (1.6)

Here tau is graph Steiner length. The H dependence allows a chosen core adapted to a carrier, though in the application below the individual-coordinate split is common to all H. A stronger vector-fiber norm with the coordinate maximum inside the support sum may be used to supply (1.6). No exchange of that maximum and the sum is made. Put t=s/m<1 and

    alpha_D(t)=D log[1/(1-t)].                              (1.7)

## 2. The local-core/tail transport theorem

Fix output weights a_out,mu>=0, put beta=a_out+mu, and let delta>0. Assume

    beta+delta <= kappa,
    c1 beta+alpha_D(t) <= a0.                               (2.1)

On each finite regulator the exact composed total functional admits connected declared target-carrier coefficients

    sum_H E_H(f(w)|H)=sum_K U_K(w|K),                       (2.2)

with absolute convergence and

    sup_z sum_(K contains z)
       exp[a_out|K|+mu ell(K)] ||U_K||_r
       <= exp(beta c0+delta h0) F S_delta epsilon.          (2.3)

The connected carrier K may include connecting cells on which the coefficient does not actually depend; this is permitted strict support. Since K is connected, ell(K)=|K|-1 for the metric spanning-tree convention on graph vertices.

On an infinite graph, (2.3) states convergence in the anchored activity space and of its local coefficient sums; (2.2) is not a globally summable scalar identity without an additional summability or normalization hypothesis. For example constant singleton activities satisfy (1.1) but their global sum diverges.

The displayed bound is for the full coefficients, including possible constants. If f^0_H(0)=0 and E_H(0)=0, every coefficient can be chosen to vanish at w=0. For general E_H, the vacuum sum is sum_H E_H(0) under the same core-zero hypothesis, and subtracting coefficient values at zero costs at most a factor two in (2.3). Equivalently normalize the old activities first and use their normalized e_H. Vacuum subtraction must not be applied to functions of a still-unintegrated fluctuation variable as if they were scalar constants.

### Proof

At each complex target field w, expand only in the tail:

    E_H(f^0_H(w)+v_H(w))
       =sum_(nu in N^(D|H|)) c_(H,nu)(w|K0(H)) v_H(w)^nu,
    c_(H,nu)=1/nu! (partial^nu E_H)(f^0_H(w)).              (2.4)

Missing coordinates can be padded by dummy variables. The core margin (1.4) permits a scalar product polydisc of radius m about every core value. Multivariable Cauchy therefore gives

    ||c_(H,nu)||_r <= e_H m^(-|nu|).                       (2.5)

The coefficient is holomorphic in w and has support K0(H). This is not an expansion of the core in its scalar coordinates. Its full amplitude may be a fixed fraction of b without a D-dependent Cauchy cost.

Substitute (1.5) separately in each scalar occurrence of v_H^nu. Join each tail support X to its root pi(i) by a deterministic minimizing Steiner graph. Let T be the sum of all these graph lengths and define K as their union with K0(H). It is connected and contains all variable dependencies of the term. Because each joining graph is attached to K0(H),

    |K| <= |K0(H)|+T,
    z in K implies d(z,pi(H)) <= h0+T.                    (2.6)

The second inequality includes an anchor z in the core itself. It would be false with h0 omitted for a core halo. Consequently

    1_(z in K) exp[a_out|K|+mu ell(K)]
       <=exp(beta c0+delta h0) exp[-delta d(z,pi(H))]
             exp(beta c1|H|)
             product_occurrences exp[(beta+delta) tau(root union X)]. (2.7)

Use (1.6), (2.5), and beta+delta<=kappa. For fixed H the absolute sum over all tail support choices and scalar multiindices is bounded by

    e_H exp(beta c1|H|)
          sum_nu t^|nu|
       = e_H exp[(beta c1+alpha_D(t))|H|].                 (2.8)

Indeed sum_nu t^|nu|=(1-t)^(-D|H|). Ordered support choices in the repeated powers already account for all multiplicities; no additional factorial or polarization estimate is inserted. The core term nu=0 is included.

Finally

    exp[-delta d(z,pi(H))]
       <=sum_(i in H) exp[-delta d(z,pi(i))].              (2.9)

Use the old anchored bound (1.1), the budget (2.1), and the fiber bound F. Their sum is at most F S_delta epsilon, proving (2.3). Absolute convergence on smaller closed target polydiscs proves the analytic identity and justifies grouping equal K. Every coefficient reads only variables in K. This completes the proof.

## 3. What has and has not improved

The earlier Taylor-at-zero theorem paid D log[1/(1-s_full/b)] for the entire substituted field. Formula (2.1) pays D log[1/(1-s_tail/m)] only for its tail. The core instead costs its carrier geometry, c0,c1,h0, and the genuine amplitude margin m. This is a different bound, not a cancellation of the scalar-coordinate count in general analytic Taylor series.

Even when s_tail=0, the geometry requires c1 beta<=a0. A large core carrier cannot be declared at no weight cost. The halo control is also necessary for the rerooting constant; an arbitrary distant core carrier cannot be justified from its cardinality bound alone.

The prefactor in (2.3) need not be less than one, and the theorem says nothing about the source of the margin (1.4). A full quantum iteration still requires compatible actual domains, interaction/integration estimates, and control of the noncontracting relevant and marginal parts.

## 4. A rigorous core/tail split of an existing rooted series

Suppose a common field has a vector-valued rooted family on a unit graph,

    f_i(w)=sum_X f_(i;X)(w_X),
    sup_i sum_X exp[kappa_0 tau({i} union X)+A|X|]
                       ||f_(i;X)||_r <= S(r),             (4.1)

where each fiber norm takes its coordinate maximum before the X-sum. Fix ell>=0 and define

    f_i^0=sum_(X subset B_ell(i)) f_(i;X),
    f_i^tail=sum_(X not subset B_ell(i)) f_(i;X).          (4.2)

The core is holomorphic and finite range ell. Its actual component amplitude obeys ||f_i^0||<=S(r), independently of ell; no reconstruction by cancellation of the full field is used. If kappa_t<kappa_0, each tail label has tau({i} union X)>ell, and hence

    sup_i sum_X exp[kappa_t tau({i} union X)+A|X|]
                       ||f_(i;X)^tail||_r
       <=S(r) exp[-(kappa_0-kappa_t)ell].                 (4.3)

This statement also holds for complete Banach fibers with growing dimension: the proof uses the same maximum-inside-support norm. The core consumes the absolute family amplitude S(r), not merely a possibly smaller pointwise bound on the fully summed field.

For a pre-root-gauge representative, the newly proved family bound is S(r)=C_A r/R for R=L^s, with C_A and its domain independent of R at fixed base L. Therefore a *core* margin m=b/2 on a target ball r<=b is supplied if R>=2C_A, with all classical domains respected. The smaller pointwise full-field constant C_0 is not enough for this conclusion unless it also controls the chosen core. This uses the absolute supported constant C_A.

This geometric statement concerns the chosen pre-gauge representative. Its physical one-step stationary-germ identification is established only for s=1; a grouped R=L^s integral/branch has not been constructed by this lemma.

## 5. Grouping the local core and estimating the remaining tail

Let rho_J group the unit target/output graph into centered J-blocks, with J odd. Assume ell<=J-1. The projection of an ell-neighborhood of a unit cell lies within the coordinatewise one-neighbor halo of its J-block. In this paragraph let pi denote the composite projection into that macrograph and set P(H)=pi(H), without adding an uncontrolled connecting hull. If this projected set is connected, the declared core macro carrier can be chosen connected with

    K0(H) subset N_(graph d)(P(H)),
    |K0(H)| <=q |P(H)|,       q=3^d.                      (5.1)

This can be realized as P(H) together with the projections of the unit ell-balls at its original roots: each added projected ball is connected and meets P(H). If the projected old carrier has a known compression bound |P(H)|<=c0_old+c1_old|H|, then (1.3) holds with

    c0=q c0_old,       c1=q c1_old,       h0=d.            (5.2)

For identity macro projection, c0=0,c1=q is sufficient. A fixed modest enlargement of q or h0 is harmless when collars are used, but must be stated.

The tail support norm after grouping must still be checked. The safe projection inequality is

    tau_macro({rho_J i} union rho_J X)
       <= 2 tau_unit({i} union X)/J+d|X|.                (5.3)

For a desired fixed macro exponent kappa, take 2kappa/J<=kappa_t and use the old cardinal reserve A>=d kappa. Grouping output roots takes a maximum over J^d old root fibers inside a support sum; bounding it by their sum gives the safe factor J^d. Equations (4.3),(5.3) yield

    s_tail,macro(r)
       <= J^d S(r) exp[-(kappa_0-kappa_t)ell].             (5.4)

The core amplitude itself is an actual component supremum, so it retains the bound S(r), not J^d S(r). The J^d in (5.4) belongs to its absolute coefficient-family estimate. These are different norms.

Suppose the actual scalar-coordinate count of an input macrocell is bounded by D(J)<=D_* J^d R^d. Combining S(r)=C_A r/R with (5.4) gives the conservative estimate

    D(J) t <= D_* C_A (r/m) J^(2d) R^(d-1)
                    exp[-(kappa_0-kappa_t)ell].           (5.5)

For fixed R and bounded r/m, choose ell proportional to log J with a coefficient greater than 2d/(kappa_0-kappa_t), allowing an additional fixed offset for R and the remaining constants. Then D(J)t tends to zero, while ell/J tends to zero. Thus a finite J can meet both the small-tail Taylor budget and the bounded-core-halo condition. The dependence of the chosen input cardinal reserve and support radius is fixed before J; for a fixed desired macro kappa, A>=d kappa does not grow with J.

This proves consistency of these abstract fixed-parameter inequalities. It does not identify D(J) or all the needed core dependencies for a particular new Gaussian integral; those are application inputs.

## 6. A sample weight budget and the actual unresolved interface

For new connected Gaussian activities with reserve a_G=1/2, identity macro projection and q=3^4=81, take

    a_out=mu=1/4096,        beta=1/2048.

Then q beta=81/2048<1/2, leaving a fixed positive margin for alpha_D(t). Any fixed delta satisfying beta+delta<=kappa is admissible. A positive margin for the tail is therefore available without requiring the core amplitude divided by b to be of order 1/D. If the next inherited interaction theorem uses this smaller recovered a_out instead of 1/16, its physical L inequality must be redone with that value; one can choose a larger fixed L, but no unchanged numerical L is being claimed.

The remaining model-specific interfaces are:

1. Supply the actual common-domain core amplitude margin. The absolute pre-gauge family gives one for large R=L^s, but its s>1 macrostep physical branch and normalized integral still require proof. The known physical one-step L constants have not been shown to give C_A(L)<L/2.
2. Apply the core split to the same fields that occur in the inherited source insertion, including fluctuations when necessary. A statement only about the stationary background does not control the full fluctuation configuration.
3. Preserve the exact source Gaussian, pivot/Haar factors, absolute gauge penalty and sharp retained cutoff. Analytic continuation of a total gauge-invariant composition germ does not by itself identify a modified integral.
4. Verify the actual grouping and carrier map for each old/new activity family. The generic constants D,F,c0,c1,h0 must come from that map, not be chosen independently of it.
5. Control activity amplitudes and relevant/marginal terms. The bound (2.3) is generally not contractive even when it removes the strongest sufficient analytic-radius loss.

The candidate therefore supplies a precise replacement for the generic Taylor-at-zero radius estimate, conditional on a local core with margin and a sufficiently small supported tail. It does not yet prove a stable quantum analytic domain.
