# Ordinary reference averages from the fixed-reference corrected recursion

Status: independently cross-audited; see `nonflat_reference_averages_audit.md`. The argument is finite-dimensional at every finite volume and refinement. It uses the fixed-reference corrected-composition theorem already proved and audited in `flat_nonlinear_average_research.md`, plus the exact one-step endpoint-gauge identity and gauge covariance of the ordinary average. It does not identify the derivative of that fixed-reference composition with the separately based source operator Q(U).

All source line numbers below refer to the pinned deposit `theorem_0_complete_account_raw_I.tex` at commit e392ef45013a581664bab76b90867170b30fe10e. They identify the deposited transcription, not a fresh verification against the original CMP98 typesetting.

## 1. Exact distinctions and source interfaces

Write M for the ordinary group-valued average, and write C for the corrected relative average at reference configuration 1. For a near-identity configuration V define, at a coarse vertex y,

    alpha(V;y) = L^(-d) sum_{x in B(y)} (1/i) log V(Gamma_yx),
    a(V;y) = exp(i alpha(V;y)).

The exact one-step identity is

    C(V)(c) = a(V;c_-)^(-1) M(V)(c) a(V;c_+).                 (1.1)

This is Raw I 24313–24325 specialized to reference 1, equivalently the explicit coordinate bridge at 47082–47086. In the general-background bridge the final endpoint factor is conjugated by M(V_reference); that conjugation is the identity only when the reference is 1. The same passage expressly incorporates CMP98 (120), which the earlier passage at 24405 does not itself reproduce.

For our convention V^g(c)=g(c_-) V(c) g(c_+)^(-1), ordinary gauge covariance says

    M(V^g)=M(V)^(g restricted to coarse vertices).            (1.2)

Raw I 43018–43026 records this convention-free covariance with restriction to base points. Raw I 82901–82904 explicitly invokes CMP98 (11) for complexified gauge transformations. Near the identity, the complex identity also follows directly from products, similarity-equivariant analytic logarithms and group means, or by holomorphic extension of real gauge covariance. Our gauges below stay uniformly near 1, so no logarithm-branch change enters this use.

The ordinary map has rooted flat differential Q^flat. The corrected map has flat differential Q_st, the normalized straight-string average. In particular the previously proved contraction of Q_st must not be assigned to Q^flat. The proof below avoids this error by transporting the entire nonlinear configuration through (1.1).

## 2. Homogeneous setting and known corrected bound

Fix odd L>=3, j>=0, eta=L^(-j), and h_t=L^t eta, 0<=t<=j. Work on a compatible periodic lattice, or the full lattice with bounded fields. No mixed retained-history boundary is included. A is a globally defined, possibly complex Lie-algebra-valued physical bond field, and U=exp(i eta A) bondwise.

Let C_0=U and C_{t+1}=C(C_t). The fixed-reference theorem supplies analytic physical fields A_t satisfying

    C_t=exp(i h_t A_t),       ||A_t||_infinity <= 2a,
    a=||A||_infinity < rho,                                  (2.1)

with rho and every constant depending on fixed d,L and matrix-norm conventions, but not on j, volume or eta. Its one-step physical map F_h obeys

    A_{t+1}=F_{h_t}(A_t),
    ||D F_h(B)||_(infinity->infinity)
             <= 1+D_infinity h ||B||_infinity.               (2.2)

These statements are for the corrected recursion with reference 1 at each step. Ordinary reference backgrounds in the source are instead V_t=M^t(U). Their control is the purpose of the next section.

Use a fixed submultiplicative matrix norm for the estimates below. Constants can absorb equivalence with the source's finite-dimensional Lie-algebra norm.

## 3. Exact cumulative gauge and uniform ordinary connection amplitude

Let m_Gamma be the largest number of oriented bonds in any one-step contour Gamma_yx. It is finite at fixed L; the conservative source bound m_Gamma<=dL suffices. For a<=rho small enough that 2m_Gamma a<=log(3/2), (2.1) gives

    ||C_t(Gamma)-1|| <= exp(2m_Gamma h_t a)-1 <= 1/2.

The series for the logarithm therefore gives, conservatively,

    ||alpha(C_t;y)|| <= K_Gamma h_t a,
    K_Gamma=8m_Gamma.                                        (3.1)

Here one may use ||log(1+E)||<=2||E|| for ||E||<=1/2 and exp(s)-1<=3s/2 for 0<=s<=log(3/2). The displayed constant leaves slack.

Define vertex gauges recursively by

    g_0=1,
    g_{t+1}(y)=g_t(y) a(C_t;y),                              (3.2)

where y belongs to the next, nested coarse lattice, so g_t(y) is defined. Then the exact identity is

    V_t=M^t(U)=C_t^(g_t).                                   (3.3)

Indeed it is true at t=0. If it is true at t, (1.2) gives M(V_t)=M(C_t)^(g_t restricted). Rearranging (1.1) gives M(C_t)(c)=a_t(c_-) C_{t+1}(c) a_t(c_+)^(-1). Multiplication yields (3.3) at t+1 with precisely the order in (3.2). There is no commutation of gauge factors.

The geometric sum is exact:

    sum_{s<t} h_s=(h_t-eta)/(L-1).                           (3.4)

Writing each g_t and its inverse as ordered products of exponentials and using (3.1),

    ||g_t||, ||g_t^(-1)||
       <= exp(K_Gamma a(h_t-eta)/(L-1)),
    ||g_t-1||, ||g_t^(-1)-1||
       <= exp(K_Gamma a(h_t-eta)/(L-1))-1.                   (3.5)

The last inequalities follow by telescoping the product; unitarity is not used. Let

    K_V=2+2K_Gamma/(L-1).

Each bond of V_t is the product of the ordered exponential factors of g_t(c_-), exp(i h_t A_t(c)), and g_t(c_+)^(-1). Consequently

    ||V_t(c)-1|| <= exp(K_V a h_t)-1.                        (3.6)

After decreasing a so that K_V a<=log(3/2), define the analytic branch

    B_t(c)=(i h_t)^(-1)log V_t(c).

Then

    ||B_t||_infinity <= 3 K_V a.                            (3.7)

This is the desired depth-independent physical connection-amplitude bound. The ordinary references stay in a common fixed one-step coordinate neighborhood after one further fixed reduction of a. All intermediate definitions are legitimate inductively: C_t is controlled by the corrected theorem; the finite product (3.2) is controlled by (3.5); (3.6) places V_t in the one-step analytic neighborhood before M(V_t) is used.

The gauges and all maps are analytic on a common complex bounded-field ball. They are local in a final-scale neighborhood: a_t reads a one-step block of C_t, while C_t reads the two endpoint fine blocks. The total physical radius of these dependencies is bounded by a fixed multiple of sum_{s<t}h_s. Thus no growing physical range or dependence on the full torus is hidden in (3.2).

This argument obtains the amplitude input that `complex_averaging_research.md` had left conditional on the base-one use of CMP98 Proposition 6. It does not rely on that proposition's multilevel amplitude conclusion.

## 4. Curvature: a genuine regularity distinction

Small ||A||_infinity alone cannot imply a mesh-uniform bound on eta^(-2)||U(partial p)-1||: choose commuting A_2 alternating between +a and -a at neighboring sites in direction 1 and all other components zero. The plaquette angle has size 2eta a, so physical curvature has size comparable to a/eta. This already fails at level t=0.

There is a positive result if the initial physical first differences satisfy

    b=max_nu ||nabla_(eta,nu) A||_infinity < infinity.        (4.1)

The corrected one-step map is covariant under translations by one coarse lattice step Lh. Let T denote such a translation in one direction. The straight-line integral of its derivative gives

    ||F_h(TB)-F_h(B)||_infinity
       <=(1+D_infinity h||B||_infinity)||TB-B||_infinity.

Every interpolation between B and TB remains in the same bounded-field ball. Since T translates L fine steps,

    ||TB-B||_infinity/(Lh)
       <=||nabla_(h,nu)B||_infinity.

Using (2.1) and iterating,

    max_nu ||nabla_(h_t,nu) A_t||_infinity
       <= exp(2D_infinity a/(L-1)) b.                       (4.2)

This argument is compatible with periodization, including translations wrapping the torus; telescoping is on the periodic field. It uses only coarse translation covariance of the fixed block construction, not arbitrary fine translation covariance.

For any bond potential B on spacing h with ||B||<=2a and ||nabla_h B||<=b_t, pair the two parallel sides of a plaquette. The integral formula for the difference of two matrix exponentials bounds the contribution of opposite-side differences by C h^2 b_t. The residual product with constant values is a group commutator and differs from 1 by at most C h^2 a^2. Products and inverses have uniformly bounded norm. Hence

    ||C_t(partial p)-1|| <= C h_t^2(b_t+a^2).               (4.3)

By (3.3), plaquette transports are conjugated by g_t at their initial vertex. Combining (3.5), (4.2) and (4.3),

    h_t^(-2)||V_t(partial p)-1||
       <= C exp(Ca)(b+a^2),                                (4.4)

uniformly in refinement and volume. For real A the gauges are unitary and the conjugation loss can be omitted in a unitary-invariant norm. A bounded global physical connection and bounded first differences therefore give the required ordinary-reference curvature control. No derivative of the gauges is needed for (4.4).

There is also a uniform first-difference bound for the ordinary physical logarithm B_t itself. Here is the additional argument, which is stronger than needed for curvature. On the same coordinate ball the fixed contour formula has derivative bounds

    ||D_A alpha(exp(i h A))||_(infinity->infinity)<=C_alpha h,
    ||D_A a(exp(i h A))||_(infinity->infinity)<=C_alpha' h,  (4.5)

with constants depending only on the fixed contour length and the chosen radius. Differentiate the finite product along the contour: each differentiated exponential contributes h, the other factors have bounded product norm, and the analytic logarithm derivative is bounded on the half-unit ball. The final exponential has bounded derivative too. This proves (4.5), without a fine derivative loss.

If s<t, translation by h_t is a multiple of h_(s+1) and preserves the scale-s block construction. Thus (4.2), telescoping the input across h_t/h_s fine steps, and (4.5) give

    ||a(C_s;y+h_t e_nu)-a(C_s;y)||
          <= C h_s h_t exp(2D_infinity a/(L-1)) b.          (4.6)

The same estimate holds for inverse factors. Take the difference of the ordered product (3.2) at the two vertices and telescope its factors, bounding all undifferentiated products by (3.5). Summing h_s proves

    ||g_t(y+h_t e_nu)-g_t(y)||
       +||g_t(y+h_t e_nu)^(-1)-g_t(y)^(-1)||
          <= C exp(Ca) h_t^2 b.                            (4.7)

The corresponding difference of C_t(c)=exp(i h_t A_t(c)) is at most C exp(Ca) h_t^2 b by (4.2). Equation (3.3), differentiated by a finite difference of the bond starting point, therefore bounds the difference of V_t by the same quantity. Both values are in the ball ||V-1||<=1/2, where the logarithm is uniformly Lipschitz (integrate its derivative on the convex segment). Dividing that logarithm difference by h_t^2 gives

    max_nu ||nabla_(h_t,nu) B_t||_infinity
          <= C exp(Ca) b.                                  (4.8)

The case t=0 is the initial bound. There is no a/h_t term: the small gauge difference across adjacent level-t sites is of order h_t^2 b, rather than merely h_t a. This is exactly the scale factor needed for the ordinary physical C1 estimate.

Together (3.7), (4.4) and (4.8) prove connection, C1 and curvature control for the stated globally trivialized homogeneous small-field class. They are not theorems for arbitrary gauge-orbit small-plaquette fields, mixed domains, or independently chosen local frames.

## 5. Actual source bond averages: a summable perturbation

Let Q_h(V) be the physical one-step source bond operator obtained by linearizing the corrected relative map at zero increment with reference V held fixed. The exact general-background bridge at Raw I 47082–47086 makes this a finite, local analytic matrix of the background logarithms. Its formula is also transcribed at 24355–24369 from CMP98 (124). At V=1 it equals the normalized straight-string Q_st,h.

For an operator P from spacing h to Lh, define its absolute physical Schur norm by

    ||P||_av = max( sup_c sum_b ||P_cb||,
                    sup_b L^d sum_c ||P_cb|| ).             (5.1)

For more general spacings h to H, replace L^d by (H/h)^d. This is the maximum of the bounded-field norm of the absolute coefficient matrix and that of its physical adjoint. It is submultiplicative across scales, and bounds the physical L2 norm. Fixed-dimensional component-norm equivalences are absorbed once in the definition/constants; at the flat point the transport coefficient is the identity and the scalar nonnegative averaging weights have both physical row sums exactly one.

At fixed L, local analyticity, finite row/column incidence and Cauchy's estimate give a constant C_Q and a fixed near-identity radius r_Q such that

    ||Q_h(exp(iX))-Q_st,h||_av <= C_Q ||X||_infinity
                       for ||X||_infinity<r_Q.              (5.2)

The coefficients are independent of h after unit-lattice identification; the physical adjoint factor in (5.1) is always L^d. Therefore no eta-dependent factor enters C_Q. The flat equality ||Q_st,h||_av=1 follows by counting the L^d translated strings of length L: a fixed input bond occurs L times in the global rows, so its unweighted column sum is L^(-d).

The source states that the order-j bond operator is the product of its one-step operators at the ordinary backgrounds V_t=M^t(U), in Raw I 25147–25155 and 47046–47061 (CMP99b (3.15), CMP98 (124)). Taking this exact definition,

    Q_j(U)=Q_(h_(j-1))(V_(j-1)) ... Q_eta(V_0),
    Q_j(1)=Q_st,M.

Equation (3.7) gives ||log V_t||<=3K_V a h_t, so, putting C_*=3C_Q K_V,

    ||Q_j(U)||_av <= exp(C_* a/(L-1)),
    ||Q_j(U)-Q_j(1)||_av
            <= exp(C_* a/(L-1))-1 = O(a).                  (5.3)

For a partial product ending at spacing h_t the exponent improves to C_*a(h_t-eta)/(L-1). The difference follows by the exact telescoping product identity, with flat factors having norm one. Thus the estimate applies simultaneously to the bounded-field norm, physical-adjoint bounded-field norm and physical L2 norm.

This proof never equates Q_j(U) with D F^(j)(A). The variable-base differential and endpoint gauge corrections require the separate exact comparison being developed by theorem_audit. Here the source's actual product is controlled directly, using its analytic one-step coefficients and the newly established ordinary-reference bound.

## 6. Scalar averages

The scalar operator called Q'_j in the source and Q_0 in the flat homogeneous analysis is transcribed at Raw I 23913–23920:

    (Q'_j(U)lambda)(y)
       =L^(-jd) sum_{x in B^j(y)} Ad U(Gamma^(j)_yx) lambda(x).

The higher contour passes through the successive block centers. Raw I 17798–17810 explicitly describes its legs in terms of the level-p ordinary averaged configurations; each leg has at most dL bonds. Equations (3.6)–(3.7), or the corresponding product bound before taking a logarithm, therefore imply

    ||transport||, ||transport^(-1)|| <= exp(C a h_j),
    ||Ad transport-I|| <= exp(C a h_j)-1.                  (6.1)

Indeed the accumulated exponent is bounded by C a sum_{p<j}h_p. At a fixed level the blocks partition the fine vertices. Each input scalar vertex occurs in exactly one row, with weight L^(-jd); the physical adjoint multiplies by L^(jd). Consequently

    ||Q'_j(U)||_av <= exp(C a h_j),
    ||Q'_j(U)-Q'_j(1)||_av <= exp(C a h_j)-1.               (6.2)

This can also be obtained from the product of one-step covariant scalar averages. It requires no curvature bound, only the connection-amplitude bound. The scalar Q'_j is distinct both from the bond Q_j and from the main term denoted Q_0 in the single-step formula CMP98 (125).

## 7. Weighted physical-cell norms and exact scope

Partition all spaces into compatible physical cells of side one and equip each fine/coarse cell with its physical L2 measure. All one-step maps are local; their multilevel products read a uniformly bounded final-scale neighborhood. Source Raw I 23927–23930 and 24332–24336 give the sharper two-final-block support for bond averages. Thus only a fixed number N_R of physical cells can meet a row or column support.

Every cell block of P has operator norm at most its global L2 norm. For the exponentially weighted physical-cell Schur norm this gives

    ||P||_(kappa,cell) <= N_R exp(kappa R) ||P||_(2->2),     (7.1)

where R is a fixed support diameter. Apply this to the differences in (5.3) and (6.2). They are O(a) in weighted cell Schur norm, uniformly in refinement and compatible periodic volume. One can use an enlarged fixed N_R and periodic distance on small tori, counting cover multiplicities; periodization cannot increase this fixed locality bound. The same estimates hold holomorphically on a common small complex A ball.

Settled within this candidate's explicit algebraic inputs:

* ordinary intermediate physical connection amplitudes are uniformly small;
* ordinary curvature is uniformly controlled if initial physical first differences are controlled;
* actual source Q_j and scalar Q'_j are O(a) perturbations of their flat versions in physical L2 and weighted cell Schur norm;
* no equality between the moving-reference Q_j and the derivative of the corrected fixed-reference composition is used.

Still outside the result:

* exact original-paper verification of the deposited coordinate convention, beyond the explicit transcription bridge;
* nonflat covariant Hessian and the projected gauge inverse R(U), including their source weak norms;
* current terms and minimizing extensions at a nonflat background;
* mixed retained-history/Dirichlet geometries and compatibility of local frames;
* strict background-support expansions and an interacting ultraviolet limit.

The useful next interface is now concrete: with Q(U), Q'_j(U) controlled in a common weighted norm, derive the projected gauge operator from its scalar inverse and Schur complement and bound its perturbation without requiring fine derivatives of the background beyond the intended source norm.
