# The zero-input quantum force on a fixed outer field domain

17 October 2026. Research proof for independent audit. This concerns the actual homogeneous local macrostep on the jointly chosen classical system of the quantum local-limit theorem. It does not estimate a coupling drift sign, prove a full RG trajectory, or identify the local sector with the entire Wilson measure.

## 1. Fix the outer construction before restricting its field radius

Fix the primitive ratio, the actual composite ratio R, the auxiliary grouping J, the trace/color normalization, and the output carrier exponent a=1/16. All constants below may depend on those fixed choices, but are uniform in preceding homogeneous depth M and compatible volume. The group is semisimple; in particular SU(2) satisfies the assumption used to remove the linear total.

The purely classical precision, pivot, base-interaction and stationary-map data have independent outer product domains. Select one radius rho>0 on which all of their strict support and precision-neighborhood budgets hold, with a fixed margin. This radius is chosen after R,J. No inherited interaction is present in the present construction.

For a fixed real retained threshold T>=1 and sufficiently small positive g, the zero-input correction is

    G_(M,g,T)(0;w)=Delta_M(w)+Qdet_M(w)+L_(M,g,T)(w),   (1.1)

where Delta is the normalized background pivot logarithm, Qdet is the normalized Gaussian determinant logarithm, and

    L_(M,g,T)=log E_(C_M(w))[chi_T(xi) exp V_base(w,xi;g)].

The cutoff is the actual product of retained link/color balls. The precision C_M(w) is independent of g. The stationary backgrounds and charts in (1.1) are the actual ones and are also independent of g. Field-independent powers of g, Haar constants, flat determinants and the compact gauge-insertion normalization remain in the separately tracked vacuum normalization.

The common-domain construction, now applied on rho, gives a strict output family with

    ||G_(M,g,T)(0)||_(a,rho)
      <= H(rho,g,T)
      :=(C_Delta+C_det)rho
        +2 S_1 [e^3 tau(T)+exp(v(g,T)) v(g,T)],          (1.2)

after enlarging harmless fixed constants if necessary. Here

    v(g,T)<=C_base(gT^3+gT+g^2T^2).

Choose T=T(g)>=1 and g_0>0 so that the bad-block and base-factor budgets hold on rho for every 0<g<=g_0, with the same strict margins. For example a sufficiently large fixed multiple of sqrt(log(1/g)), with a fixed lower threshold, has tau(T(g))->0 and gT(g)^3->0. Then

    sup_(M, 0<g<=g0) H(rho,g,T(g)) <= H_*<infinity.     (1.3)

The important assertion is a bound on an anchored coefficient family on one fixed outer radius. It is not a supremum bound on an extensive finite-volume total. All infinite statements use the same input-independent classical local-limit system; the outer families are passed to that limit and then restricted. Unrelated subsequences selected at different radii are not silently identified.

## 2. Exact inner/outer compatibility and the vanishing linear total

For any 0<b<rho, the zero-input finite-regulator integral on the b ball is the restriction of the integral in (1.1). The actual chart, constraint, Gaussian covariance, threshold T(g), and all measure factors are unchanged. A radius enters only the estimates, not the defining integral. Its selected logarithm is the continuation of the same near-origin branch. Thus the normalized finite totals agree exactly on b.

One may fix the outer support assignments and simply restrict every coefficient. Alternatively, two valid assignments obtained from the same finite integral have the same normalized total and hence the same quotient class after the established local-limit theorem. The first procedure directly proves compatibility without a second compactness selection. The same reasoning holds for all fixed preceding depths on the jointly chosen system.

The total in (1.1) is globally adjoint invariant. This follows either from the actual retained-window change of variables or from the local gauge theorem of the common-domain macrostep. Its total linear derivative at w=0 vanishes for a semisimple Lie algebra: fixing one link slot, this derivative is an invariant linear functional on the adjoint representation; it vanishes on all commutators, and [g,g]=g. At finite volume the argument applies slot by slot, and the infinite compact-field total inherits it by local convergence. Individual carrier coefficients need not have a vanishing linear jet or be gauge invariant.

The constant total is a vacuum normalization. The present quotient removes it; the corresponding physical scalar factor is still recorded separately. For a group with an abelian factor the adjoint argument alone would not remove a linear total, and the following conclusion would require that removal as an additional hypothesis.

## 3. Quadratic inner-radius forcing

Let P_n denote coefficientwise homogeneous phase projection in all background coordinates of a carrier. For a coefficient holomorphic on the rho polydisc,

    ||P_n E_H||_b <= (b/rho)^n ||E_H||_rho.             (3.1)

Use radii strictly below rho in Cauchy's formula and then take their limit; no boundary regularity is assumed. Phase projection retains the carrier. Replace the outer zero-input family by

    G_H^(>=2)=sum_(n>=2) P_n G_H.                       (3.2)

The normalized total is unchanged: the constant sector is removed by normalization and the sum of the linear sectors is zero by Section2. This statement is about the total; it does not delete a nonzero linear term from a physical density without compensation.

Summing the positive bound in (3.1) first over n for each carrier and then over anchored carriers gives

    ||[G_(M,g,T)(0)]||_(Q,a,b)
      <= (b/rho)^2/[1-b/rho] H(rho,g,T)
      <= C_F b^2,    C_F=2H_*/rho^2,  b<=rho/2.        (3.3)

There is no interchange of an order sum and a root supremum. The same inequality holds on every compatible finite volume for the represented normalized total, before a quotient limit. The constant C_F is independent of the inner radius b, M and volume.

Let S_(MR) be the actual normalized full reference, with beta(S_(MR))=1 and ||[S_(MR)]||_(Q,b)<=C_S b^2. The full-reference projection P_(MR)=I-S_(MR) beta has norm

    ||P_(MR)||<=p=1+C_beta C_S,                         (3.4)

independent of b. Therefore the extracted force obeys

    ||P_(MR) G_(M,g,T)(0)||_(Q,b)<=C_0 b^2,
    C_0=p C_F.                                         (3.5)

The Maxwell increment of the unprojected force satisfies

    |beta(G_(M,g,T)(0))|<=C_beta C_F.                    (3.6)

The b^(-2) in beta's norm is present and is cancelled by the proven b^2 factor. It has not been discarded. One may instead apply beta directly on the outer domain, giving the analogous C_beta rho^(-2) H_* estimate.

## 4. Parameter order and an explicit finite-block envelope

Use the reference transport and projected recurrence notation of extracted_macrostep_recurrence_rotation_research.md. Fix J,R, then a finite q for which the projected q-step classical product has norm at most 1/4. Let B>=1 bound the one-step projected classical map, K=B+1, and L_q=sum_(l=0)^(q-1) K^l. These constants are fixed before choosing the final inner radius b. The outer radius rho and H_* can be chosen independently of that final b; making rho smaller to cover any fixed finite list of classical margins is harmless.

The quantum remainder difference satisfies, on the admissible quotient neighborhood,

    ||P(G_g(x)-G_g(y))||<=nu ||x-y||,
    nu<=p C_quant gT(g)/b.                              (4.1)

Fix an admissible family ceiling epsilon_bar>0. Select

    K_amp=max(1,2 C_0 L_q),  r(b)=K_amp b^2.             (4.2)

Choose b<=rho/2, below the direct R^q classical domain, and so small that

    [K^q K_amp+C_0 L_q]b^2 < epsilon_bar/4.             (4.3)

For this fixed b, lower g_0 further until

    nu<=min(1,1/[4qK^(q-1)])                            (4.4)

and all inherited-interaction budgets hold on the radius-epsilon_bar family ball. In particular, if a_Q=16 C_T C_R gT/b is the inherited exponent coefficient, a sufficient requirement is

    a_Q epsilon_bar <= eta_*/(128e),                   (4.5)

together with the separate fixed base and bad-block budgets. The denominator 128e is the stronger two-input comparison budget used for the quotient Lipschitz estimate, not merely the single-output 32e budget. Thus an admissibility condition of the form epsilon_bar<=eta_*/(constant a_Q) creates no radius cycle: g is chosen after b and epsilon_bar. This argument is for fixed finite geometric constants, however large.

For an initial extracted class of norm at most r(b), the elementary recurrence gives each intermediate norm, for 0<=k<=q, at most

    K^k r(b)+C_0 b^2 sum_(l<k)K^l
      <= [K^q K_amp+C_0 L_q]b^2 < epsilon_bar/4.        (4.6)

The q-step map has Lipschitz constant at most 1/2 by the Duhamel estimate. Its value at zero has norm at most C_0 L_q b^2<=r(b)/2. Hence it maps the radius-r(b) extracted ball into itself. The maximum in K_amp also supplies a positive radius when C_0=0. The argument can be applied uniformly over a prescribed weak coupling sequence, or along an actual coupling sequence for as long as that sequence stays in the established weak-coupling range.

Intermediate amplitudes are O(b^2), not merely bounded by a b-independent epsilon_bar. The unprojected one-step map has bounded classical part, force (3.3), and quantum Lipschitz part (4.1). Consequently beta of its value is uniformly O(1) along this envelope. This gives an absolute bound on a single inverse-coupling increment, with no sign. It does not control infinitely many increments or differences between maps evaluated at different couplings.

## 5. Why the full force is not thereby O(g^2)

Delta and Qdet in (1.1) are fluctuation-independent but background-dependent terms. They have no small factor g. Removing their constant and total linear jets gives an O(b^2) representative, not an O(g^2) representative. Neither gauge invariance nor the norm estimates prove a cancellation of their quadratic or higher total. Thus a statement that the entire generated correction is O(g^2) would require a new subtraction or a proved cancellation. The present result needs neither.

There is a useful separate fixed-threshold parity statement. Keep T fixed while complexifying g. Every centered classical/gauge remainder has the form

    -g^(-2)[F(g xi)-F(0)-g DF(0)xi-g^2 D^2F(0)[xi,xi]/2],

with a removable singularity at g=0. Its n-th coupling coefficient is a homogeneous fluctuation polynomial of degree n+2. The straightening and Haar factors depend analytically on g xi. Hence, as a total exact exponent,

    V_base(-g,xi)=V_base(g,-xi).                         (5.1)

The centered Gaussian and the actual product window are invariant under xi->-xi even for complex background covariance, since their densities remain quadratic/even. Therefore Z(-g,T;w)=Z(g,T;w), and the normalized logarithm is even on a sufficiently small complex g disk, by its common branch at g=0. The background determinant and pivot terms are also even because they are independent of g.

The actual strict base estimates hold for complex g with |g|T small and give v<=C(|g|T^3+|g|T+|g|^2T^2). Choose a fixed c>0 so that for all T>=T_0 the entire disk |g|<=c T^(-3) stays inside the strict base budgets and the local charts. The zero-input cluster construction then supplies a carrier family analytic in g on that disk with a uniform anchored outer-rho bound H_L*. Symmetrize this family under g->-g, which does not increase its norm and preserves its total; it is coefficientwise even. Subtract its value at g=0. Coupling Cauchy and a geometric sum yield, for |g|T^3<=c/2,

    ||[L_(g,T)-L_(0,T)]||_(Q,a,rho)
       <= 2 H_L* (|g|T^3/c)^2.                         (5.2)

This estimate does not require each original carrier coefficient to be even. The symmetrized representative provides the needed coefficientwise parity. The same fixed-support construction is holomorphic in g: it uses local analytic factors with removable singularities, finite Gaussian moments and uniformly normally convergent strict cluster sums. Indicators stay fixed while g is complexified.

At g=0, V_base=0 and L_(0,T) is the Gaussian cutoff logarithm, of anchored norm at most C tau(T). Thus on the outer domain

    [G_(g,T)(0)]=[Delta+Qdet]+O_Q(tau(T)+g^2T^6).       (5.3)

For the chosen physical diagonal T=T(g), evaluate this two-parameter estimate afterward. With T(g) proportional to sqrt(log(1/g)), the latter term is O(g^2 log(1/g)^3); the tail can be made a prescribed positive power of g by its fixed threshold coefficient. This is not an assertion that the g-dependent cutoff function is holomorphic in g, nor that the full correction has order g^2. It isolates the bounded zero-coupling determinant/pivot contribution and proves no beta sign or coefficient.

## 6. Scope

The core result is the uniform O(b^2) zero-input forcing (3.3)-(3.6), supplied by the existing outer-domain macrostep and its exact symmetry. Section4 combines it with the independently proved finite-block recurrence. Section5 is an additional parity refinement of the actual centered Gaussian factor; its fixed-T complex-coupling hypotheses and exact window symmetry are explicit.

The exact density identity still requires gamma_next=gamma-beta(F_g(x)), gamma=g^(-2), with the sign fixed by exp(-gamma S+F). No positivity or averaged positive drift has been proved here. The map comparison is at prescribed equal couplings, not a contraction in the joint coupling/activity variables. Uniform bounds on actual finite-regulator histories, the remaining field sectors, vacuum densities and continuum observables are separate from this local quotient envelope.
