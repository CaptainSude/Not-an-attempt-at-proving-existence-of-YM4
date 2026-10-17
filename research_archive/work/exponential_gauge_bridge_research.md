# The flat axial-to-exponential Gaussian bridge

Research note, 16 October 2026. The repository and output notebooks were not modified. This note proves finite-dimensional bridge statements and checks their algebraic match to the actual gauge-fixing term. It does not assert the remaining uniform bounds for the deposited free-current operator family.

## 1. Source match and conclusion

The actual exponential gauge fixing in [CMP109](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf), pp.253--255, (0.11), (0.14)--(0.16), uses the averaged contour variable from a block center y to x. Its quadratic part is stated at p.266, (2.5). The reduced precision is identified at pp.267--268, (2.11)--(2.13). These are different operations from imposing one chosen tree contour by a delta function.

The quadratic gauge penalty at the trivial configuration is exactly

    G_2(B) = (1/2) ||T B||^2,

in the Lie-algebra norm fixed by the normalized trace, where T averages the oriented path integrals over the prescribed shortest contours. On a tree-axial representative B_ax plus a rooted gradient D lambda, this becomes (1/2)||T B_ax + lambda||^2, not generally (1/2)||lambda||^2. A bounded triangular change of the gauge coordinate gives the latter diagonal expression.

There is also a constraint distinction: the center-rooted constraint Q^flat of CMP109 and the block-mean constraint Q_1 of CMP99b agree on the averaged-contour axial slice, but not on every bond field. Section 3 below gives the exact flat relation and a transfer that respects it.

The deposit already treats these issues algebraically: raw II, lines 9045--9285, defines the contour derivative, both constraints and their covariance identities; lines 9380--9560 derive the Ward/BCH almost-invariance identity. Those local algebraic derivations check out. Its later exponential-gauge proposition still takes a separate quantitative covariance result by statement. The independent contribution here is the explicit flat bridge and its constants, together with the precise scope of its extension away from flatness.

## 2. Fixed block geometry and the true penalty

Work on a unit lattice, with a partition into L-blocks B(y), each containing n=L^d sites and a distinguished center y. Count each unoriented nearest-neighbor bond once in a fixed positive orientation. Let the real Lie algebra carry the invariant norm |X|^2=tr(X^2) in Hermitian coordinates. Alternative fixed normalizations only change constants.

For each x in B(y), let P(y,x) be the family of monotone shortest paths used in the average. Set

    (T B)(y,x) = average over Gamma in P(y,x) of sum_{b in Gamma} epsilon_b B_b,
    (T B)(y,y) = 0.

Choose also a single rooted spanning tree in each block, and let T_0 denote its root-to-site path integral. Choose the tree so its paths have length at most h=d(L-1); the usual coordinate-ordered tree has this property. Every averaged contour also has length at most h.

Let (D lambda)_b=lambda(b_+)-lambda(b_-). Then path telescoping gives

    T D lambda = T_0 D lambda = d lambda,
    (d lambda)(y,x)=lambda(x)-lambda(y).                       (2.1)

On the rooted site subspace R={lambda: lambda(y)=0 at every center}, d is the identity after identifying site coordinates with pairs (y,x), x!=y. Thus T D lambda=lambda on R.

The quadratic penalty follows directly from the linearization of the group average at the identity. Each contour product has the expansion 1+i t integral_Gamma B+O(t^2), and the average has first variation equal to the arithmetic average of these integrals. If Omega(t)=exp(i[t T B+O(t^2)]), then

    1-Re tr Omega(t) = (t^2/2) |T B|^2 + O(t^3).

The second-order coefficient of the logarithm of Omega does not enter this expression. Summing over y,x gives the displayed G_2. In particular the result does not require a guessed penalty on a tree coordinate.

Uniform elementary bounds are

    ||D||_{2->2} <= d_0 := 2 sqrt(d),
    ||T||_{2->2}, ||T_0||_{2->2} <= t_0 := sqrt(h(n-1)).     (2.2)

For D, sum |lambda(v)-lambda(w)|^2<=2|lambda(v)|^2+2|lambda(w)|^2 over bonds. For T, the absolute coefficient row sum is at most h and the column sum is at most n-1: each target path uses a given bond at most once, and averaging preserves this bound. The Schur test proves (2.2). The same reasoning applies to T_0.

The identity T B_ax=0 need not hold on the tree slice ker T_0. In two dimensions, take an off-tree edge closing a square and give only that edge a nonzero value. One of the two coordinate-order paths to the opposite corner uses that edge and the other does not. The tree path integral vanishes while their average does not. Thus the shear in Section 4 is essential if a tree slice is used.

## 3. Exact flat relation between the two averaging constraints

Let c=(y,y+L e_mu) be a coarse bond and let [x,x+L e_mu] be its translated straight string, with x in B(y). Define

    (Q_st B)(c) = L^(-d-1) sum_{x in B(y)} integral_[x,x+L e_mu] B,
    (a T B)(y) = L^(-d) sum_{x in B(y)} (T B)(y,x),
    (D_1 f)(c) = L^(-1)[f(y+L e_mu)-f(y)].

At the trivial background, the linearization of the contour-based average in CMP109 (0.12) gives

    Q^flat B = Q_st B - D_1 a T B,
    Q_1 := Q^flat + D_1 a T = Q_st.                       (3.1)

Indeed the logarithm of the closed contour contributes T_yx B plus the translated straight string minus T_{y',x'} B minus the reference coarse string. Multiplication by the final reference coarse transporter cancels the last term. Averaging x and dividing by L gives (3.1). Only the first derivative of the group average is used. This also explains why the block-mean operator Q_1 at flatness is independent of the choice of rooted contours used for gauge fixing.

Consequently

    Q^flat D lambda = D_1(lambda restricted to block centers),
    Q_1 D lambda = D_1(block mean of lambda).              (3.2)

In particular rooted gauge directions preserve ker Q^flat, and block-mean-zero gauge directions preserve ker Q_1. These are different statements. On ker T, the two constraints agree by (3.1).

For B in ker Q^flat, put

    xi = T B, viewed as a rooted site field,
    B_T = B-D xi.

Equations (2.1), (3.2) imply

    T B_T=0,   Q^flat B_T=0,   Q_1 B_T=0.                (3.3)

Conversely, B_T in ker Q_1 intersect ker T and arbitrary rooted xi determine B=B_T+D xi in ker Q^flat, with T B=xi. Thus this is a genuine linear bijection, not a dimension-counting argument.

To compare with a tree-axial slice, use the site subspace N of block-mean-zero fields. The map d:N->functions on pairs (y,x), x!=y is invertible. For f extended by f(y,y)=0, its inverse is

    (d^{-1}f)(x)=f(y,x)-L^(-d) sum_{z in B(y)} f(y,z).

Moreover ||d^{-1}f||_2<=||f||_2, by subtracting the orthogonal blockwise constant component. Therefore

    B_0 = B_T-D d^{-1}T_0 B_T

lies in ker Q_1 intersect ker T_0. It differs from B_T by a block-mean-zero gradient. Conversely, since T B_T=0,

    B_T = B_0-D d^{-1}T B_0.                             (3.4)

The inverse sign follows from 0=T B_0+d lambda when B_T=B_0+D lambda. Hence

    ||B_T||_2 <= (1+d_0 t_0)||B_0||_2.                  (3.5)

This is the needed constraint-compatible comparison with a delta tree gauge. It avoids substituting Q^flat for Q_1 without justification.

## 4. Proved quantitative flat coercivity transfer

Let q be a real symmetric quadratic form on bond fields such that

    q(B+D lambda)=q(B)                                   (4.1)

for all relevant gauge directions. Assume the axial lower bound

    q(B_0)>=gamma_ax ||B_0||_2^2

on ker Q_1 intersect ker T_0. The meaning of gamma_ax here is the norm of the full constrained bond field. If the available primary statement is instead q(K_ax z)>=gamma_free||z||^2 in independent coordinates, it suffices to establish ||K_ax||<=M_ax and use gamma_ax=gamma_free/M_ax^2. That coordinate conversion must not be omitted.

Define

    gamma_T = gamma_ax/(1+d_0 t_0)^2.

Equations (3.4)--(3.5) and gauge invariance give q(B_T)>=gamma_T||B_T||^2. For every B in ker Q^flat, its exact decomposition (3.3) yields

    q(B)+||T B||^2 = q(B_T)+||xi||^2
                  >= gamma_T||B_T||^2+||xi||^2
                  >= gamma_exp ||B||^2,
    gamma_exp = 1/(gamma_T^(-1)+d_0^2).                  (4.2)

The last inequality is weighted Cauchy--Schwarz applied to ||B||<=||B_T||+d_0||xi||. The Gaussian exponent is minus one half of the left side, in the convention of CMP109 (2.11). A fixed positive penalty coefficient a changes gamma_exp to 1/(gamma_T^(-1)+d_0^2/a); the unmodified source has a=1 after the stated coupling rescaling.

For a direct tree decomposition B=B_ax+D lambda in a common preserved constraint, the penalty is ||T B_ax+lambda||^2. The shear mu=lambda+T B_ax yields B=B_ax+D(mu-T B_ax), so the form becomes q(B_ax)+||mu||^2. This is the same mechanism, but (3.3)--(3.4) are needed when transferring between the actual two different constraints.

If q has an axial upper bound q(B_0)<=M_q||B_0||^2, the projections in Section 3 also give an upper bound on q(B)+||T B||^2 on ker Q^flat, with constants depending only on M_q,d,L. For example, ||B_0||<=(1+d_0t_0)^2||B|| yields the upper bound [M_q(1+d_0t_0)^4+t_0^2]||B||^2. After pivot elimination B=K_flat z, the lower precision bound remains gamma_exp because z is a coordinate restriction of B, and the upper bound gains ||K_flat||^2. Uniform covariance accretivity requires this upper bound as well as the lower one.

### 4.1 Explicit flat pivot-extension constants

The pivot bound can also be proved in the stated flat geometry. For each positively oriented coarse bond c choose b_0(c) to be its unit bond crossing the interface between the two blocks, on the line through their centers. No contour in T contains this interblock bond. In the straight-string average Q_st(c), precisely L starting sites x contribute b_0(c): their transverse coordinates are fixed and their longitudinal coordinate ranges over the first block. Its coefficient in Q_st and Q^flat is therefore L times L^(-d-1), namely L^(-d). No other coarse equation contains this pivot. Thus the full pivot coefficient matrix is L^(-d)I, and

    B_pivot = -L^d Q_f z,
    ||K_flat||^2 <= 1+L^(2d)||Q^flat||^2.                (4.3)

Here Q_f is the restriction to the remaining bond columns, and K_flat inserts the displayed pivot values while retaining z unchanged. This is the actual linear elimination at the trivial configuration.

For Q_st the absolute row sum is one. A fine bond participates in straight strings for at most two coarse bonds. Thus its absolute column sum is at most two, giving ||Q_st||<=sqrt(2). The crude bound suffices. For Q^flat, put r=1+2h/L. Equation (3.1) bounds its absolute row sum by r. An internal fine bond can enter contour terms only through its own block, which has 2d incident coarse bonds, and straight strings add at most two coarse equations. Each coefficient is bounded by the row sum r. Therefore the column sum is at most (2d+2)r, and

    ||Q^flat|| <= r sqrt(2d+2),
    ||K_flat||^2 <= 1+L^(2d)(2d+2)r^2.                  (4.4)

On the tree-axial slice the tree bonds vanish and the same pivot elimination applies to Q_1=Q_st; all pivots lie outside the block trees. Hence one can take

    ||K_ax||^2 <= 1+2L^(2d),
    gamma_ax = gamma_free/(1+2L^(2d))                   (4.5)

whenever the source axial estimate is stated in these free tree-and-pivot coordinates. These conservative constants are independent of scale and volume. They use the ordinary coarse tiling, with distinct block interfaces; they do not assert a bound for a different pivot scheme without checking its coefficient matrix.

## 5. Why gauge invariance is exact at the flat reference

Let f be the actual gauge-invariant action as a function of its bond data; for the effective step this is f(V)=A(U_k(V)), assuming the stated minimizer construction. At the trivial datum f has a stationary minimum, since the Wilson action is nonnegative and vanishes at the trivial field. Hence its gradient vanishes there. Differentiating gauge invariance shows that its Hessian annihilates all infinitesimal gauge directions. Section 6 gives the full formula, including its current correction away from stationarity.

At a stationary point, a nonlinear chart with derivative equal to the identity has the same Hessian as the original chart: the usual gradient-times-second-chart-derivative term is zero. Therefore the nonlinear constraint linearization does not create an extra flat quadratic term. The actual flat Gaussian action part is the invariant Hessian q, and the gauge part is precisely ||T B||^2. The current-dependent correction in the source form vanishes at (U,J)=(1,0).

Thus (4.2) applies to the actual flat exponential Gaussian once the appropriate flat axial estimate and its independent-coordinate extension bound have been supplied. This establishes the gauge/coercivity bridge; it does not reproduce the primary scale-uniform axial estimate from scratch.

## 6. Proved Ward Hessian identity, with conventions

Use Hermitian Lie-algebra coordinates, U'(b)=exp(i eta B_b)U_b. Let

    f_U(B)=f(exp(i eta B)U),
    f_U(B)=f(U)+<J_U,B>+(1/2)H_U(B,B)+O(||B||^3).

Choose gauge convention U^g(v,w)=g(v)^(-1)U(v,w)g(w), with g_t=exp(i t lambda). Put a=lambda(v), b'=Ad_{U(v,w)}lambda(w), and

    (D_U lambda)_(v,w)=(b'-a)/eta.

In the mixed two-parameter family g_t(v)^(-1)exp(i eta s B)U g_t(w), the logarithmic coordinate relative to U is

    s B+t D_U lambda+(i s t/2)[B,a+b']+O(s^2 t+s t^2)+terms independent of s.

This follows from one half of the pairwise commutators of -it a, i eta s B, and it b'. Gauge invariance and comparison of the mixed coefficient imply

    H_U(B,D_U lambda)=-(i/2)<J_U,[B,a+b']>.              (6.1)

The first variation also gives <J_U,D_U lambda>=0. Setting B=D_U lambda gives the pure-gauge Hessian. Equivalently, the second derivative of the pure gauge coordinate is

    -(i/eta)[a,b'],

and (6.1) gives H_U(D_U lambda,D_U lambda)=(i/eta)<J_U,[a,b']>, in agreement with the pure-gauge second derivative. This independently checks the sign and the eta normalization.

For real unitary U, let c_br satisfy |[X,Y]|<=c_br|X||Y| in the chosen norm, and let j_*=sup_b|J_U(b)|. With one positive orientation per bond,

    |H_U(B,D_U lambda)|
       <= c_br sqrt(d) j_* ||B||_2 ||lambda||_2.         (6.2)

Indeed the square sum of |lambda(v)|+|lambda(w)| over bonds is at most 4d||lambda||^2. At unit lattice spacing ||D_U||<=2sqrt(d), and expansion of the quadratic form gives

    |H_U(B+D_U lambda,B+D_U lambda)-H_U(B,B)|
       <= 2 c_br sqrt(d) j_* ||B|| ||lambda||
          +2 c_br d j_* ||lambda||^2.                  (6.3)

Thus fixed-block gauge changes produce a bounded O(j_*) form perturbation. For a complex background, replace unitarity by explicit uniform bounds on the relevant adjoint maps; the algebraic identity persists holomorphically, but the real norm constants cannot be copied unchanged.

The raw manuscript uses the opposite convention U^v=v(v)Uv(w)^(-1); changing lambda to -lambda reconciles the signs. Its raw II almost-invariance formula is the same second-order identity for f(V)=A(U_B(V)), with current j=H_1^*J. It is not valid for an arbitrary independent current merely because that current is given the same name. Any extension to free J must be justified through the actual displayed operator dependence and a small perturbation estimate.

## 7. A stronger physical-fiber observation and its limitation

Suppose f is gauge invariant, the averaging level set M(V)=W is preserved by rooted gauges, V is a critical point of f restricted to that level set, and psi is any smooth local parametrization of the level set with derivative the identity on K=ker DM_V. Then the Hessian of f composed with psi annihilates rooted gauge tangent directions exactly.

Proof: express the gauge transform of psi(sB) in the psi chart. The mixed derivative of gauge invariance has the Hessian pairing plus the first derivative of f composed with psi applied to the mixed chart derivative. The latter vanishes at the constrained critical point. Therefore the Hessian pairing is zero.

This applies to the complete physical constrained Hessian, including its constraint-curvature/current correction, when all its source identifications hold. It can be stronger than estimating the separate unconstrained Hessian by (6.3). It does not extend automatically to the independent-current analytic carrier, where the current need not be the gradient of a constrained critical action. Nor does it establish an axial gap without the separate axial estimate.

## 8. What the quadratic cutoff coefficient actually needs

Raw I, lines 3780--3837, defines the deposited coefficient through the carrier Hessian at (U,J)=(1,0), contracted with the first normalized response of B->(U_j,J_j)(exp(iB)) at B=0, followed by the whole-lattice moment sum. Thus, for the pure Gaussian cutoff part of that coefficient, a genuinely flat baseline and a fixed normalized analytic neighborhood of the trivial background/current can suffice. Uniform locality around every arbitrary real background is a stronger requirement than this quadratic coefficient alone asks for.

More precisely, the direct Hessian route needs the actual flat reduced covariance, its first and second carrier responses in the fixed independent cutoff coordinates, the normalized response bounds, and the thermodynamic identification. The full strict-support route needs a small local precision expansion on a suitable neighborhood of (1,0), with constants uniform in scale and volume. Both routes still need identification with the particular cutoff contribution in the deposited coefficient. The interaction ratio and Gaussian normalizer are separate terms.

In contrast, choosing C_0=C_0(U_ref) separately at each real reference makes the locality theorem local only in the varying perturbation coordinates. Its activities may depend on all of U_ref through that baseline. Such a construction does not prove locality in the full background carrier without a further localization of the reference dependence. The fixed flat reference avoids this particular logical problem for the quadratic coefficient, but not the remaining precision/covariance source match.

## 9. Remaining interfaces

1. Verify the exact primary axial gap and upper bound at flatness in its stated independent-coordinate convention. Section 4.1 supplies the conversion for the indicated tree-and-pivot convention. The deposited proposition assumes quantitative exponential-gauge inputs; it cannot be cited as an independent completion of the primary axial estimate.
2. Match the old flat block-mean operator to Q_st with the exact averaging convention. Formula (3.1) proves the match for the contour-based CMP109 average; any changed operator convention must be checked, not renamed.
3. Match the chosen pivot convention to the explicit flat construction of Section 4.1. The fixed normalized-coordinate extension bound is then proved by (4.4); away from flatness the coefficient matrix and its analytic perturbation still require control.
4. Establish scale-uniform weighted perturbation/response estimates for the actual complex free-current family near (1,0). The Ward identity identifies physical current corrections but does not supply this independent-current theorem.
5. Preserve the fixed real integration domain and sharp cutoff coordinates under these comparisons. A coercivity proof may change coordinates algebraically; it does not license moving the cutoff domain without tracking that change.

The established outcome is an exact and quantitative flat gauge bridge, with the true averaged-contour penalty and the two constraints explicitly distinguished. The model-wide free-current and locality inputs remain separate.
