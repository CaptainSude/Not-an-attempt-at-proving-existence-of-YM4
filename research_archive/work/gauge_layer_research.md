# Gauge-invariant layer removal for pure Wilson SU(2)

16 October 2026. This note settles the local gauge-descent interface left open in `work/same_limit_rp_research.md`, conditional only on its already proved SU(2) convolution lemma. It does **not** establish the separate chessboard amplification or same-limit reflection-positivity theorem.

The main simplification is to keep all links on and above the next slice unchanged. A gauge transformation at the lower vertices proves an identity for the observable, but we never gauge fix the probability measure. We then condition on the upper spatial links and apply the convolution identity directly.

## 1. Scope and conventions

Let G=SU(2), β>0, and

    kβ(g)=exp[(β/2)Tr g].

Trace is real on SU(2). The finite-volume Wilson law is proportional to the product of kβ around all unoriented elementary plaquettes, times product normalized Haar measure on independent positively oriented links. For a reverse link, U_(y,x)=U_(x,y)^−1. Gauge transformations act by

    U_(x,y) ↦ g_x U_(x,y) g_y^−1.

The proof applies on any periodic or skew-periodic finite lattice in which the finite neighborhoods used below embed without identifications. It is local: no global coordinate slicing of the torus is required. It also applies under Wilson DLR conditional distributions. The coupling is fixed and finite; none of the constants below is asserted uniform as β tends to infinity.

Write vertices as (j,x), where j is the coordinate to be reduced and x∈Z^(d−1). A function is supported in a vertex slab [a,b] if all links on which it depends have both endpoints in that slab. In particular, an observable supported on or above j may depend on spatial links at height j and temporal links from j to j+1, but on no incoming temporal link from j−1.

Initially P is a finite Peter–Weyl polynomial in finitely many link variables, invariant under all endpoint gauge transformations. Continuous gauge-invariant local observables follow by uniform approximation in §7.

## 2. Exact observable identity in temporal-gauge coordinates

Let S be the finite set of positively oriented spatial edges e=(x,y) whose copies at height j occur in P. Let T be the set of x for which the temporal link from (j,x) to (j+1,x) occurs in P. Enlarge T to a finite set I containing T and all endpoints of S. Introduce

    b_e = U_((j,x),(j,y)),
    a_x = U_((j,x),(j+1,x)),
    v_e = U_((j+1,x),(j+1,y)),
    u_e = a_x^−1 b_e a_y,                 e=(x,y)∈S.

The variables a_x are allowed to be auxiliary links not originally read by P. Apply the gauge transformation

    g_(j,x)=a_x^−1  for x∈I,
    g_z=1           at every other vertex.

It sends a_x to 1 for x∈I and sends b_e to u_e. Every link with both endpoints at height at least j+1 remains unchanged. Other links meeting the transformed lower vertices also change, but P does not read any of them except the displayed b_e and its outgoing temporal links. Gauge invariance therefore gives the pointwise identity

    P(U)=P̃(u_S, U_≥j+1),                  (2.1)

where P̃ is obtained by setting the original outgoing temporal arguments to 1 and replacing the original bottom spatial arguments by u. This is an identity of functions on the full link configuration space. No change of variables in the Wilson law, gauge-fixing determinant, or assertion about the exterior measure is involved.

P̃ is still finite Peter–Weyl in its arguments. It has a finite expansion

    P̃(u,v,η)=Σ_i f_i(u) P_i(v,η),         (2.2)

where each f_i is a finite Peter–Weyl polynomial on G^S. Here v denotes the upper copies of S, and η comprises finitely many other links with both endpoints at height at least j+1. If P originally did not read some v_e, its coefficients simply do not depend on that argument.

If S is empty, (2.1) already expresses P entirely in upper links, and no integration is needed. Gauge invariance removes any otherwise dangling bottom temporal dependence.

### Endpoint covariance

For an arbitrary gauge transformation of the original configuration,

    a_x' = g_(j,x) a_x g_(j+1,x)^−1,
    b_e' = g_(j,x) b_e g_(j,y)^−1.

Consequently

    u_e' = g_(j+1,x) u_e g_(j+1,y)^−1.   (2.3)

The transported bottom variable and its upper partner v_e transform under exactly the same upper endpoint gauges. All lower endpoint gauges cancel. Equivalently, gauge transformations preserving the displayed temporal gauge have equal transformations at paired lower and upper endpoints. Their action on P̃ is the ordinary endpoint gauge action on its u and upper variables.

## 3. Every action factor containing an upper integration link

Condition on all link variables except v_e, e∈S. The down-going temporal plaquette containing v_e has an oriented holonomy

    b_e a_y v_e^−1 a_x^−1.

Cyclic invariance of trace gives

    Tr(b_e a_y v_e^−1 a_x^−1)=Tr(u_e v_e^−1).

Since kβ is invariant under inversion, its weight is exactly

    kβ(v_e u_e^−1).

This is the only plaquette involving v_e and links strictly below height j+1. Every other plaquette containing v_e is one of the following:

* A spatial plaquette lying entirely at height j+1. It can contain more than one selected v edge and is included only once.
* The up-going temporal plaquette from j+1 to j+2. If c_x is the temporal link from (j+1,x) to (j+2,x), and w_e the spatial edge at j+2, its holonomy may be written

      v_e c_y w_e^−1 c_x^−1.

Let W(v;η) be the product of exactly these other plaquette weights. Thus W is a smooth strictly positive function of selected v and a finite family η of links on or above j+1, reaching at most j+2. It includes complete plaquette factors, so it is gauge invariant when v and η transform together.

All remaining plaquette weights form a factor H of the exterior configuration. In particular, bottom spatial plaquettes, plaquettes from j−1 to j, and down-going plaquettes for unselected upper spatial links are in H. None depends on any selected v.

The full Wilson density therefore factors exactly as

    H(exterior) K_S(v,u) W(v;η),
    K_S(v,u)=Π_(e∈S) kβ(v_e u_e^−1).       (3.1)

For a fixed finite S, W and W^−1 are bounded, as are all their derivatives of any fixed order, uniformly over all exterior group variables and all sufficiently large ambient volumes. This follows from compactness and the finite number of complete plaquettes used in W. The constants may depend on β and S.

Equation (3.1) accounts explicitly for the action couplings to both the eliminated slice and the next slice. No independence of lower variables is assumed: all their couplings remain in H and in the parameter u.

## 4. Conditional layer-removal identity

On G^S, let C_S be convolution with K_S and put

    T_f=C_S^−1 M_f C_S.

The convolution lemma proved in §3 of the preceding note says that, for finite Peter–Weyl f, T_f is a continuous operator C∞(G^S)→C∞(G^S) with finite Sobolev derivative loss, and

    C_S T_f B = f C_S B.                  (4.1)

Because K_S(v,u)=K_S(u,v), this means

    f(u) ∫ K_S(v,u) B(v)dv
       = ∫ K_S(v,u) (T_f B)(v)dv.         (4.2)

Apply (4.2) term by term to (2.2), with B=W P_i. Define

    Q(v,η)=W(v;η)^−1 Σ_i T_(f_i)[W(·;η)P_i(·,η)](v).    (4.3)

Then, for every fixed exterior configuration,

    ∫ K_S(v,u) W(v;η) P̃(u,v,η)dv
       = ∫ K_S(v,u) W(v;η) Q(v,η)dv.       (4.4)

Dividing by the same positive conditional normalizer proves

    E_μ[P | all links outside v_S]
       = E_μ[Q | all links outside v_S],
    E_μ P=E_μ Q.                          (4.5)

The formula is independent of the chosen finite tensor expansion: the assignment f⊗B↦T_f B is bilinear and defines a linear map on the algebraic tensor product. One may also use a fixed Peter–Weyl basis in the lower variables.

Q is a bounded smooth local function. It reads only original upper arguments and the plaquettes entering W; all of its links have both endpoints at height at least j+1. Its support reaches at most max(b,j+2) if P was supported in [j,b]. Spatially it expands by at most the local plaquette star of the selected edge set, besides original upper support.

Q need not be a finite Peter–Weyl polynomial. No such assertion is used.

### Gauge invariance of Q

For an upper gauge transformation h, let A_h denote pullback under

    v_e ↦ h_x v_e h_y^−1,  e=(x,y)∈S.

The product convolution C_S commutes with A_h. Indeed its kernel is invariant under the same left and right endpoint multiplication of both variables, and Haar measure is invariant. It follows that

    T_(A_h f)(A_h B)=A_h(T_f B).            (4.6)

This holds even though different selected edges share endpoint gauges, because C_S in fact commutes with independent left/right multiplication on each selected edge.

By (2.3), P̃ is invariant when u,v and the exterior upper arguments η undergo their simultaneous upper endpoint gauge transformation. W is invariant under that same transformation. Applying the equivariance (4.6) to (4.3) shows

    Q(h·v,h·η)=Q(v,η).                    (4.7)

Gauge transformations at other vertices act only on the parameter arguments and give the same conclusion. Thus Q is an ordinary gauge-invariant local observable on the upper subgraph. It is already expressed in the original upper link variables, which were never changed. There is no further ungauging operation and no reintroduction of a_x, b_e, or any lower link.

The map commutes with complex conjugation, since C_S has real kernel. In particular Q can be taken real whenever P is real. It need not preserve pointwise positivity, which is not required for (4.5).

## 5. A bounded sparse local tilt

Let

    dμ_(n,t) ∝ exp(t V_n) dμ_n,
    V_n=Σ_α O_(n,α),     0≤t≤1,

where the sources are real smooth local functions. Assume uniform local overlap and derivative bounds: for every fixed finite link set, only a bounded number of source copies read those links, and their derivatives of every required finite order have bounds independent of n. Fixed-spacing arrays of translates and lattice reflections of a fixed local polynomial satisfy this assumption. Gauge invariance of the sources is natural for the intended application but is not needed for the numerical error estimate below.

Split V_n=R_n(v;ζ)+V_(n,0)(ζ), where R_n is the sum of source copies that read at least one selected v_e, and ζ denotes all exterior variables they use. These may include bottom or lower links. There are only a uniformly bounded number of such sources. V_(n,0) factors out of the conditional integral.

Using (4.2), with all ζ frozen, gives the exact replacement

    Q_(n,t)=W^−1 e^(−tR_n)
               Σ_i T_(f_i)[e^(tR_n) W P_i].             (5.1)

Thus E_(μ_n,t) P=E_(μ_n,t) Q_(n,t). Formula (5.1) is allowed to depend on lower variables through R_n; those variables are only frozen parameters in the convolution identity. The unperturbed Q from (4.3) remains independent of them.

The finite derivative loss of T_(f_i), compactness, and the uniform local bounds imply

    ||Q_(n,t)−Q||∞ ≤ C_P t,    0≤t≤1,                 (5.2)

with C_P independent of n. Explicitly, subtract (4.3) from (5.1). The two terms involve e^(−tR_n)−1 and T_(f_i)[(e^(tR_n)−1)W P_i]. Their C^m norms are O(t) for the finite m required by the Sobolev estimate. All other factors have uniform local derivative bounds.

Consequently

    |E_(μ_n,t) P−E_(μ_n,t) Q| ≤ C_P t.               (5.3)

No operator amplification estimate, uniqueness, clustering, or global reflection symmetry of μ_(n,t) was used. This estimate is uniform in the volume for a fixed β, source family, and finite input observable.

## 6. Top-layer removal and support control

There is a symmetric top-layer step, either by reversing the coordinate or directly as follows. For a top spatial edge b_e at height j, let a_x be the temporal link from (j−1,x) to (j,x), and let v_e be its spatial partner at height j−1. Transport the top edge down by

    u_e=a_x b_e a_y^−1.

The gauge transformation g_(j,x)=a_x at the top vertices sets a_x to 1 while leaving every link at or below j−1 unchanged. The crossing plaquette has trace Tr(v_e u_e^−1). Conditional integration over the lower partners v_e gives the same formula as above, with W made of the spatial plaquettes at j−1 and temporal plaquettes from j−2 to j−1.

It removes height j, produces a gauge-invariant observable supported at or below j−1, and reaches down at most to j−2. The same O(t) estimate holds.

To reduce an arbitrary finite support to the prescribed two-slice slab [a,a+1], start with an enclosing interval

    [l,h]=[min(original lower height,a), max(original upper height,a+1)].

First remove bottom heights l,l+1,...,a−1. At every such step j+2≤a+1≤h, so the top bound h is retained. The result is supported in [a,h]. Then remove top heights h,h−1,...,a+2. At every such step j−2≥a, so the established lower bound a is retained. The final support is in [a,a+1]. Empty layers cause no difficulty; the observable may simply remain unchanged at that step.

Each step enlarges spatial support only by a finite plaquette neighborhood. The number of steps is finite, so the final support is finite. It may be substantially larger than the original support; no uniform support bound over all input sizes is asserted.

## 7. Gauge-invariant polynomial approximation between steps

After a step, Q is smooth but generally not finite Peter–Weyl. Let F be a finite edge set containing its support, with all edges in the remaining slab. Finite Peter–Weyl polynomials are uniformly dense in C(G^F). Choose A with

    ||A−Q||∞<δ.

Average A over the compact endpoint gauge group G^(V(F)):

    A_G(U)=∫ A(g·U) dg.

Since Q is gauge invariant, ||A_G−Q||∞≤δ. Moreover A_G remains a finite Peter–Weyl polynomial: endpoint left/right multiplication preserves each finite representation space on each edge, and integration is a finite-dimensional linear projection. This averaging changes no support and introduces no removed links. Reality can be preserved by first replacing A with its real part when Q is real.

Replace Q by A_G and apply the next exact polynomial step. In expectation this replacement costs at most δ for every probability law. Large operator norms in later steps do not amplify an earlier expectation error: the estimate telescopes through the actual sequence of observables. The constants in subsequent O(t) estimates may grow, but each is finite and their finite sum is independent of volume.

For a continuous initial P, the same gauge-averaged uniform approximation is used before the first step. Choosing the finitely many approximation tolerances with total below ε gives the following conclusion.

## 8. Result established by the local argument

**Two-layer reduction proposition.** Fix β>0 and a sparse smooth source family satisfying the uniform local bounds of §5. For every continuous gauge-invariant local observable P, every integer a, and every ε>0, there exist a continuous gauge-invariant local observable Y_ε supported in the two-slice slab [a,a+1], a finite constant C_ε, and a finite local neighborhood, all independent of n and t, such that whenever that neighborhood embeds in the finite volume,

    |E_(μ_n,t) P−E_(μ_n,t) Y_ε| ≤ ε+C_ε t,
    0≤t≤1.                                               (8.1)

Y_ε may be chosen a finite Peter–Weyl polynomial by a final gauge-averaged approximation. If P is real, Y_ε may be chosen real. The proof applies to the original Wilson probability measure; it does not first replace it by a gauge-fixed measure.

For the unperturbed Wilson law, the one-step replacement (4.3) is exact for polynomial P. The final two-layer reduction for arbitrary P is an ε approximation because polynomial approximations are used between successive steps.

### Reflected observable pair

Fix a coordinate reflection θ about the target link plane a+1/2. Mirror the unperturbed elimination/approximation construction to produce θY_ε from θP. The Wilson plaquette formula and convolution identity are preserved by this reflection, including orientation reversal. The tilted error proof can be applied to both constructions using the same original source family. It only needs uniform local derivative bounds near each finite support; it does not require the source family or tilted measure to be θ-invariant.

Consequently, after enlarging C_ε if necessary, both

    |E_(μ_n,t) P−E_(μ_n,t) Y_ε| ≤ ε+C_ε t,
    |E_(μ_n,t) θP−E_(μ_n,t) θY_ε| ≤ ε+C_ε t             (8.2)

hold simultaneously. Reflection here can be interpreted on the finitely supported lattice observables; the torus need only embed both finite neighborhoods. This is the paired estimate needed to transfer two-layer reflection invariance of a comparison limit to arbitrary local observables.

## 9. What this does and does not close

This proves the gauge-specific local descent, the bounded-tilt error, and finite repeated reduction. It removes the gauge-descent caveat in §§4–5 of `same_limit_rp_research.md` for SU(2), provided the previously proved convolution lemma is accepted.

It does not establish the operator amplification inequality, its transfer-kernel normalization, mixed site/link boundary gluing, or two-frame cell placement. Those are independent global interfaces. It also does not prove bounds uniform in β or in ultraviolet-dependent source normalizations, and it gives no mass gap or continuum rotation theorem.

The special SU(2) input is the finite-derivative-loss conjugation lemma. For other compact gauge groups, the same oriented-link and covariance proof applies if the corresponding Wilson convolution has the required positive injective spectrum and polynomial finite-band eigenvalue-ratio bounds. Finite-volume reflection positivity alone does not supply those bounds.
