# A small pre-root-gauge representative and its strict supports

17 October 2026. Research proof, using the internally checked homogeneous classical theory in Notebooks14--16 and21. This note proves an amplitude and support statement for a selected representative. It does not establish a stable quantum RG domain. The exact physical one-step background is compared only for one base step; no direct large-block chart is silently identified with an iterated ordinary average.

## 1. Fixed base ratio, two independent depths

Fix the base odd integer L, dimension d=4 and 0<alpha<1. Put

    M=L^k,       R=L^s,       N=MR=L^(k+s),
    eta=N^-1,   h_t=L^t eta,  h_k=R^-1.                         (1.1)

Coordinates in this note have final next-coarse spacing one. Thus the current lattice after the first k averages has spacing h=1/R. In the usual current-unit coordinates its links have length one and its next-coarse spacing is R. The datum W=exp(iw) is a group datum; w is its angle, not w/R.

Let A_c,N(w) be Notebook15's corrected fixed-gauge minimizer, and let T_N be the explicit ordinary-representative transfer of Notebook16:

    U_N(w)=exp(i eta A_o,N(w)),
    A_o,N(w)=T_N(A_c,N(w)),
    M_L^(k+s)(U_N(w))=W.                                      (1.2)

Here M_L^t means t iterations of the same fixed-L ordinary average. The minimum and transfer theorems give, on a common complex product ball,

    ||A_o,N(w)||_(N_alpha) <= C_o ||w||_infinity,              (1.3)

uniformly in k,s and compatible finite periodic volume. Constants depend on L, alpha, the fixed group and norms. Define the pre-root-gauge partial average

    V_p,k,s(w)=M_L^k(U_N(w)),
    a_p,k,s(w)=log V_p,k,s(w)/i.                               (1.4)

Exact composition, without a semigroup assertion for a separately defined direct-R average, gives

    M_L^s(V_p,k,s(w))=W.                                      (1.5)

For s=1, this is precisely an allowed choice of V_part in `physical_current_pivot_precision_research.md` Section5. For s>1 it is a representative for the iterated constraint in (1.5). The existing one-step physical chart and its gauge-zero stationary branch do not by themselves identify it with a direct-R construction.

## 2. The amplitude factor is exactly 1/R

The ordinary-trajectory theorem in `nonflat_reference_averages_research.md` Sections2--3 is prefix-uniform. If U=exp(i eta A), a=||A||_infinity is sufficiently small, and V_t=M_L^t(U), it proves

    ||log V_t/i||_infinity <= 3 K_V h_t a,
    K_V=2+2K_Gamma/(L-1),       K_Gamma=8m_Gamma,             (2.1)

where m_Gamma is the fixed one-step contour-length bound. In particular the only accumulated scale sum is

    sum_(q<t) h_q=(h_t-eta)/(L-1).                            (2.2)

These constants refer to the fixed base L, not to the endpoint ratio R. Apply (2.1) with A=A_o,N(w) and t=k. On a smaller fixed w-ball independent of k,s,

    ||a_p,k,s(w)||_infinity <= C_0 ||w||_infinity/R,
    C_0=3 K_V C_o.                                           (2.3)

The estimate is valid for complex fields on the common small logarithm branch. For k=0 it simply reads log U_N/i=eta A_o,N with eta=1/R, providing a normalization check. This factor is not a claim that the source gauge-zero representative V_*(W) has small angles of order w/R.

The ordinary trajectory also supplies a uniformly holomorphic physical map

    P_k,N(A)=(i h_k)^-1 log M_L^k(exp(i eta A))              (2.4)

from a fixed bounded-potential ball to bounded fields on the h_k lattice. Its norm is at most 3K_V||A||_infinity. Every output reads a fine-field neighborhood of physical radius at most c_L h_k: the actual averaging ranges sum geometrically. This is an ordinary, not corrected, output map. No physical adjoint of this map is used.

## 3. A strict support family with the same small factor

All support labels now denote final unit cells, the cells carrying w. Let tau be graph Steiner length in their periodic graph. Fix an admissible spatial exponent kappa from Notebook21 and any fixed cardinality reserve a>=0.

For a current h-lattice output, collect all bond components whose initial sites lie in one final unit cell i into a Banach fiber E_(h,i), with the maximum component norm. Its dimension grows like R^d, but the norm below is a Banach output norm, never a sum over those components. An output support family has norm

    ||u||_(kappa,a;r)
       =sup_i sum_(nonempty X) exp[kappa tau({i} union X)+a|X|]
                       sup_(||w_X||<r) ||u_(i,X)(w_X)||_(E_(h,i)).      (3.1)

The output maximum is inside the X-sum. This is stronger than interchanging that sum with a component supremum. The complete fine-field families use Notebook21's smooth partition and complete N_alpha cell spaces.

**Claim.** There are r_a>0 and C_a<infinity, depending on the fixed reserve a and fixed base data, but not on k,s or volume, and holomorphic strict families

    a_p,k,s(w)|_i=sum_(nonempty X) a_(p;i,X)(w_X),
    a_(p;i,X)(0)=0,
    ||a_p,k,s||_(kappa,a;r) <= C_a r/R,       0<r<=r_a.         (3.2)

There is also a linear supported operator H_p,k,s, uniformly bounded in the same rooted norm, such that

    ||a_p,k,s-h_k H_p,k,s w||_(kappa,a;r) <= C_a r^2/R.         (3.3)

Here H_p,k,s=D[P_k,N T_N](0) H_N, with H_N the corrected linear minimizing extension; it need not be the source gauge-zero extension.

**Proof.** Notebook21 already gives A_c,N(w) as a strict complete-field family of norm at most C_(a,0)r, uniformly N and volume, with a linear part and an O_a(r^2) remainder. The transfer T_N is uniformly holomorphic N_alpha->N_alpha on a fixed ball, vanishes at zero, and has fixed final-physical dependency radius. These precise inputs are proved in `ordinary_representative_locality_research.md` Sections1--3: the cumulative endpoint gauge reads a fixed physical neighborhood, E_pt is a fixed local smooth interpolation, and the fine gauge action is a local analytic removable-eta jet expression. Consequently the composite

    F_k,N=P_k,N o T_N                                      (3.4)

is uniformly bounded and holomorphic from a fixed N_alpha ball into the physical bounded output field, vanishes at zero, and has fixed final-physical dependency radius. For a whole output fiber E_(h,i), the union of all dependency neighborhoods is contained in a fixed collar of i, uniformly even though the fiber contains O(R^d) components.

Apply the finite-range analytic vertex lemma of `classical_local_vertex_bounds_research.md` Section3 to this Banach-valued map. If rho is a common input radius, C_rec the smooth reconstruction norm, D_0 the fixed number of input cell labels in the output collar, and R_0 its graph radius, then its symmetric Taylor coefficients satisfy

    v_n <= K [e C_rec D_0 exp(kappa R_0)/rho]^n,    n>=1.     (3.5)

Here K bounds the physical output fiber in the analytic ball. Neither K nor D_0 counts current bonds inside that fiber. The uniform bound (2.4) is precisely what permits this dimension-free output estimate. The coefficient norm is the output maximum before the sum over input cell slots, so no supremum/order or supremum/support interchange is made.

Set c=e C_rec D_0 exp(kappa R_0)/rho. The support-union and rooted Steiner gluing inequalities from Notebook21 imply that substitution into a family of norm t has norm at most

    sum_(n>=1) K c^n t^n=Kct/(1-ct).                       (3.6)

For t<=1/(2c), this is at most 2Kct. The support cardinality factor causes no additional vertex cost: every new variable support is the union of its input supports, so exp(a|union X_q|)<=product exp(a|X_q|). The local map's fixed coefficients are not variable supports. Choose r_a so C_(a,0)r_a<=1/(2c), also respecting all prior evaluated-branch domains. All these choices are independent of R. Finally a_p=h_k F_k,N(A_c,N), proving (3.2). Separate the linear terms in the two analytic series to obtain (3.3). Absolute support convergence justifies all rearrangements and identifies the evaluated sum with (1.4).

This argument does not use the nonuniform physical adjoint of the full ordinary rooted average. It also does not infer tree locality from a one-weight response bound. It explicitly invokes bounded finite-range analytic maps and Notebook21's convergent support-valued algebra.

Spatial decay in (3.1) is in final unit cells. In current-unit distances this corresponds to a length scale R, not to an R-independent exponent in the old metric. The constants are uniform for R=L^s while the base ratio L stays fixed; changing the base L changes the primitive constants and is a different assertion.

## 4. Exact relation to the one-step source background

Set s=1. Notebook19 chooses the rooted current-site gauge

    u(y)=1 at next-coarse centers,
    u(x)=P_(V_p)(y,x) inside the L-block of y,
    V_*(W)=V_p(W)^u.                                      (4.1)

The actual averaged-contour covariance gives P_(V_*)=1 and M_L(V_*)=W. The fixed-L contour map is analytic and satisfies

    ||log u/i||_infinity <= C_L ||a_p||_infinity <= C'_L ||w||_infinity. (4.2)

Both configurations and the gauge path are in the common classical domains after a fixed shrink. Notebook16's action invariance then gives S_M(V_*)=S_M(V_p). Notebook19's variational and uniqueness argument identifies this V_* with the physical centered branch. Gauge-zero is obtained by (4.1) and that comparison, not inferred merely from stationarity.

The gauge size in (4.2) is not of order w/L. A pure next-coarse gauge can therefore have a smooth small-angle representative V_p and a rooted representative V_* with boundary angles of order w. This is fully consistent with Notebook22's counterexample; that counterexample rules out a supremum contraction for V_*, not for every representative of its gauge orbit.

For s>1 the amplitude and strict-support conclusions (2.3),(3.2) remain proved. Identifying a separately defined direct-R rooted gauge-zero branch, its chart, cutoff and normalized integral requires the corresponding macrostep construction. In particular M_L^s must not be replaced by an unverified direct-R averaging identity, and fixed-L minimum-comparison margins are not automatically uniform macrostep margins.

## 5. Gauge-invariant corrections: an honest extension of a germ

Let E(a) be a holomorphic total current-field functional on the angle product ball ||a||<b. Assume its local gauge invariance whenever the two configurations and the small gauge transformation lie in its common invariance domain. Gauge invariance is an assumption on E's sum, not on arbitrary support coefficients E_H.

For s=1 define

    E_p(w)=E(a_p,k,1(w)).                                (5.1)

By (2.3), this is a holomorphic function on the product ball

    ||w|| < min(r_class, Lb/C_0),                        (5.2)

with a strict inequality or smaller margin as needed. On a sufficiently small overlap around w=0, E(a_*(w)) is also defined, (4.1) lies in the common invariance domain, and

    E_p(w)=E(a_*(w)).                                    (5.3)

For real data this follows from the actual gauge relation; complex equality follows from holomorphic uniqueness. Therefore E_p is an analytic continuation of the originally defined stationary-composition germ. This is a precise larger-domain construction even when a_*(w) itself lies outside E's original ball. It does not claim that E was already defined at that latter argument. The continuation is unambiguous as a germ on this connected product ball.

If E is itself a logarithm of an inherited normalized integral, E must first be supplied as a nonvanishing compatible holomorphic logarithm on its original domain. Local symmetry of a possibly vanishing integral alone does not supply such a logarithm. No additional logarithm is needed to compose an already given holomorphic E in (5.1).

The same statement for s>1 applies to E(a_p,k,s) as an analytic composition. Its identification with a particular macrostep stationary germ is conditional on the missing macrostep branch/gauge comparison described in Section4.

In particular, for any fixed R=L^s>C_0 the representative itself maps a sufficiently small angle ball of radius b into the strictly smaller current angle ball of radius C_0 b/R, provided b is below the uniform classical radius. This geometric domain inclusion is proved and does not require E to be invariant. Gauge invariance is used to identify the composition with the original one-step stationary germ, or with a future verified macrostep germ. No activity-norm contraction follows merely from this inclusion.

## 6. What the existing activity transport actually yields

Suppose, more specifically, that E=sum_H E_H has the connected-carrier activity hypotheses of `quantum_activity_transport_research.md`: each E_H is holomorphic in a scalar-coordinate polydisc of radius b, at most D old scalar coordinates occur per old cell, and

    sup_i sum_(H contains i) exp(a_0 |H|) ||E_H||_b <= epsilon.          (6.1)

Let pi project the actual old activity cells to final cells, with fiber size at most F_R, preserving connected images. From (3.2) each old scalar component has a rooted spatial support norm at most s(r)=C_a r/R. With beta=a_out+mu and delta>0, the earlier transport theorem applies when

    beta+delta <= kappa,
    beta+D log[1/(1-C_a r/(Rb))] <= a_0.                   (6.2)

It gives output activity norm at most F_R S_delta epsilon. Here the spatial exponent is measured in final cells, and D is the actual old-cell coordinate count; it is not automatically the output fiber dimension used in Section3.

Thus the small angle has a genuine effect on the analytic argument s(r)/b. However it does not remove the coordinate-Taylor cost in (6.2). If the chosen Gaussian/background grouping has D of order R^d, its small-r sufficient condition is still

    r/b <= const * R/D = O(R^(1-d)),                       (6.3)

up to the fixed cardinality budget. If old cells retain a fixed coordinate count, that particular D-loss is absent, but the projection fiber can grow like R^d and the transported norm is still not automatically contractive. The chosen reserve a only affects the available r_a and C_a; both are uniform R, but neither is asserted small. Ordinary analytic-domain inclusion and a useful polymer-norm induction are distinct requirements.

Fixed regrouping from old unit cells to old Gaussian cells must be stated explicitly. The family in (3.1) is a Banach maximum over a final block; this proves no miraculous sum-over-output estimate cancelling F_R or D.

## 7. Remaining integral and RG interface

There is a plausible exact pointwise identity on the original common domain for an inherited factor at a fluctuation configuration. With s=1 and V_*=V_p^u,

    (exp(iB) V_*)^(u^-1)
       =exp(i Ad_(u(b_-)^-1) B(b)) V_p.                    (7.1)

For real u the adjoint is an isometry in the invariant color norm; on the small complex gauge domain it is uniformly bounded. Consequently one can try to define the inherited insertion on the right of (7.1), with B=Phi_(V_*)(g z), and retain the small background a_p. The coupling belongs inside the nonlinear chart; in general Phi_V(g z) is not g Phi_V(z). This is not yet a theorem about the complete fixed-cutoff Gaussian integral on a larger domain. It needs uniform chart/fluctuation control there, holomorphic domination and a norm estimate for the transported interactions, and equality of the two analytic integrals on a nonempty overlap. The actual Gaussian, pivot/Haar factors, gauge penalty and cutoff arguments must remain the exact ones; merely moving the argument of the inherited total E does not identify a differently normalized integral.

The results proved here are the uniform pre-gauge amplitude, its strict support expansion, and the one-step analytic continuation of a gauge-invariant total-composition germ. They remove the specific pure-gauge amplitude obstruction for this representative. They do not yet prove an invariant analytic ball for successive quantum steps, relevant/marginal extraction, running coupling control, large-field estimates, or an interacting continuum limit.
