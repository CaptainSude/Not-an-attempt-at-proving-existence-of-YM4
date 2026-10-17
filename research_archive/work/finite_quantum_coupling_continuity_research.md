# Real-coupling continuity of the actual finite local quantum map

17 October 2026. Research proof for independent audit. This is a finite-regulator continuity result for the homogeneous local macrostep already constructed in the common-domain and finite-induction modules. It supplies a necessary input for finite endpoint shooting. It proves neither a coupling sign nor endpoint crossing, and it does not identify the local sector with the full Wilson pushforward.

## 1. Fixed data and assertion

Fix one allowed finite macrostep: preceding classical depth M, current and output tori, R, J, the common angle radius b, the cardinality weight a0, the actual retained-coordinate chart and window, and all strict common-domain budgets. The input/output quotient spaces are those of finite_quantum_induction_research.md: families on connected finite carriers, modulo equality of their vacuum-normalized totals on the full product ball. In particular the quotient norm is an infimum of the anchored family norm, not a sup norm of total energies.

Let I be a compact interval contained in (0,g0], where g0 is small enough for all the common-domain, two-input comparison and finite-induction inequalities. Put

    T(g)=max(T0,A sqrt(log(1/g)))                         (1.1)

on an interval where this expression is defined, or use any positive continuous threshold satisfying the same budgets. Only continuity of T and boundedness of T on I are needed below. Let F_g denote the actual normalized finite quotient map with this threshold. Its decomposition is

    F_g(x)=T_cl x+Delta+Qdet+L_g(Q_x).                    (1.2)

Here T_cl is classical background transport, Delta and Qdet are the fixed pivot and covariance determinant terms, and Q_x is the inherited fluctuation difference. The stationary backgrounds, precision and chart are independent of g; the coupling is inserted INSIDE the nonlinear chart, as Phi_V(g xi).

**Theorem.** On the common admissible quotient ball, for example ||x||<=epsilon_bar/4, the map (g,x)->F_g(x) is jointly continuous for real g in (0,g0]. The topology on both activity arguments is the stated finite quotient norm at the SAME radius b and weight a0. The map

    (gamma,x) -> (gamma-beta_out(F_(gamma^(-1/2))(x)),
                  P_out F_(gamma^(-1/2))(x))             (1.3)

is therefore continuous wherever gamma>0 is in the weak range and the activity input is admissible. The finite beta_out and P_out are the actual finite reference-normalized maps, independent of g.

Constants in the fixed-input continuity proof may depend on the finite volume, even exponentially. No volume-uniform modulus, continuity at g=0, or continuous selection of near-minimal representatives is asserted.

## 2. The strict old-field margin

Fix a quotient input x in the stated ball and choose ONE admissible representative E. A near-minimal choice may have ||E||<epsilon_bar/2. Keep this choice fixed while varying g.

The proved joint-family construction in composite_macrostep_joint_family_research.md, Section4, and common_domain_macrostep_research.md, Section4, gives the actual inherited argument

    f_g(w,xi)=Omega_R(a_p(w),g xi),                      (2.1)

on the retained window. Under the strict budgets its whole absolute rooted family is at most b/4; hence

    ||a_p(w)||_infty<=b/4,
    ||f_g(w,xi)||_infty<=b/4                            (2.2)

for all ||w||_infty<b, g in I and all actual retained xi with each retained color vector of norm at most T(g). Fixed norm conversions are those already included in the common-domain constants. More generally the proof below only needs a fixed bound s b with s<1. We retain s=1/4 where (2.2) is available.

Write E_raw(A)=sum_H E_H(A|H). If V_in is the number of input J-cells, the anchored norm gives

    sum_H ||E_H||_b <= V_in ||E||_(a0;b).                (2.3)

Directional one-variable Cauchy on the product ball implies, for ||A||,||B||<=s b,

    |E_raw(A)-E_raw(B)|
      <= [V_in ||E||/((1-s)b)] ||A-B||_infty.            (2.4)

Indeed the line segment lies in the inner product ball and the derivative in any max-norm unit direction has a complex disk of radius at least (1-s)b. One can first use any smaller radius and pass to the limit. Sum the resulting bound using (2.3).

This establishes uniform continuity of inherited evaluations on the inner field domain using only bounded holomorphy on the ORIGINAL b ball. No extension of an arbitrary input E past b is required. Quotient null representatives may have different vacuum constants, but those cancel from the inherited difference below.

## 3. A fixed integration domain

Let D be the total finite number of real retained scalar coordinates, and let Xi_1 be the product of the actual centered unit retained link/color balls. This is a fixed compact subset of R^D. The actual window is Xi_(T(g))=T(g) Xi_1, by simultaneous scalar dilation. Its boundary convention is immaterial; it is Lebesgue-null.

Let A(w) be the retained precision and use its fixed analytic square-root determinant branch on the product ball. The normalized Gaussian expectation defining the logarithmic fluctuation contribution is exactly

    Z_g(w)= [det A(w)]^(1/2) (2pi)^(-D/2) T(g)^D
       integral_(Xi_1)
        exp{-T(g)^2 zeta^T A(w)zeta/2
             +V_base(w,T(g)zeta;g)
             +E_raw(f_g(w,T(g)zeta))-E_raw(a_p(w))}
        d zeta.                                        (3.1)

The background-only pivot/determinant factors in (1.2) may equivalently be kept outside this expression. No coupling-dependent raw vacuum factor is needed in (3.1); powers of g, compact gauge-insertion constants and fixed Haar constants have already been separated by the exact integral module. Their normalized-total contributions are zero.

Equation (3.1) is an ordinary real-variable change of coordinates. It does not deform a complex contour or replace the actual product link/color window by a Euclidean ball of a different radius. In particular the nonlinear factor remains Phi_V(g T(g)zeta), not g Phi_V(T(g)zeta).

The following bounds follow from the fixed independent classical domains used to construct the actual chart and base interactions:

* A(w), its determinant branch and the finitely many local analytic coefficient maps are bounded on ||w||<b.
* Their dependence on the local fluctuation argument is uniformly Lipschitz on a slightly larger fixed chart domain containing every g T(g)zeta under consideration.
* On the compact interval I, the exact base exponent V_base(w,T(g)zeta;g) is uniformly bounded and uniformly continuous in g, uniformly over ||w||<b and zeta in Xi_1.

For completeness, the last item can also be read directly from the exact local factors: the classical and gauge Taylor remainders enter as a fixed analytic function of g xi divided by g^2 after subtracting its constant, linear and quadratic terms; the remaining Haar/Jacobian factors are analytic in the same argument. On a compact positive g interval these expressions and their g derivatives are bounded on the fixed strict chart margin. Their removable singularities at g=0 are not needed here. The full classical remainder may have many strict-support terms, but at this finite regulator its anchored sum bounds its total by volume times its family bound.

Since a_p is independent of g, the second item and continuity of gT(g) give

    sup_(||w||<b,zeta in Xi_1)
      ||f_g(w,T(g)zeta)-f_g*(w,T(g*)zeta)|| -> 0.        (3.2)

Equation (2.4) then gives uniform convergence of the inherited exponent. The Gaussian term has the same property because T is continuous and A is bounded. Every exponent in (3.1) has a common finite absolute bound on I, depending on the regulator and E. Xi_1 has finite measure and the prefactor is uniformly bounded. Thus direct uniform domination gives

    ||Z_g-Z_g*||_(H-infty(b)) -> 0.                     (3.3)

The proof uses the supremum over the ENTIRE open b ball. Pointwise convergence or compact-subball convergence alone would not suffice for the quotient norm claimed in Section1.

## 4. Uniform nonvanishing and normalized logarithms

The strict Gaussian expansion gives a holomorphic nonvanishing Z_g throughout the b ball and a connected logarithm family with a common anchored bound H_I for g in I. Consequently its vacuum-normalized logarithm satisfies

    sup_(||w||<b) |log Z_g(w)-log Z_g(0)|
       <= 2 V_out H_I,                                 (4.1)

where V_out is the number of output J-cells. This statement is independent of the chosen raw logarithm constant.

Equation (3.3) at w=0 and nonvanishing imply that, after restricting to a compact positive interval around g* if needed,

    m0:=inf_(g in I)|Z_g(0)|>0.

Using (4.1),

    inf_(g in I,||w||<b)|Z_g(w)|
       >= m0 exp(-2 V_out H_I)=:m_I>0.                 (4.2)

This is a finite-volume lower bound; its volume dependence is not suppressed. Nonvanishing by itself would not imply (4.2) on the noncompact open b ball. The uniform connected-log bound is the essential additional input.

For g close enough to g* that ||Z_g-Z_g*||<m_I/2, set

    ell_g(w)=log[1+(Z_g(w)-Z_g*(w))/Z_g*(w)]

using the power series in the disk of radius 1/2. This is holomorphic on b and

    ||ell_g||_b <= 2 ||Z_g-Z_g*||_b/m_I.                (4.3)

If l_g denotes the selected analytic logarithm of Z_g, then l_g-l_g*-ell_g is constant in w, since its exponential is one on the connected product ball. Therefore

    ||[l_g-l_g(0)]-[l_g*-l_g*(0)]||_b
       <= 4 ||Z_g-Z_g*||_b/m_I ->0.                    (4.4)

This argument does not assume continuous choices of raw logarithm branches. Field-independent branch changes cancel from the normalized total.

## 5. Supremum convergence implies finite quotient convergence

Let H_all be the full connected output J-cell torus. If h is any bounded holomorphic vacuum-normalized total on that torus, assign h to the single carrier H_all and assign zero to every other carrier. This is a legitimate finite activity family, with

    ||[h]||_quotient <= exp(a0 V_out)||h||_b.            (5.1)

If h is the difference of locally gauge-invariant normalized totals, this representative has the same invariant total; no coefficientwise invariance assumption is needed.

The exterior terms T_cl x, Delta and Qdet in (1.2) are independent of g. Applying (5.1) to (4.4) therefore proves

    ||F_g(x)-F_g*(x)||_quotient ->0                     (5.2)

for every fixed admissible input class x. Equation (5.1) is deliberately crude and depends exponentially on volume. It is sufficient for finite endpoint continuity and avoids an unnecessary assertion about continuity of every canonical connected coefficient or of a chosen relocalized representative.

## 6. Joint continuity, extraction and finite histories

The two-input finite quotient estimate of finite_quantum_induction_research.md, Section2, is uniform for g in I:

    ||F_g(x)-F_g(y)||
       <= [B_T+C_quant sup_(g in I)(gT(g)/b)] ||x-y||.  (6.1)

It is proved using near-minimal representatives Y,D and X=Y+D within the strict family budget. Its hypotheses include the stronger two-input budget a_Q epsilon_bar<=eta_*/(128e). It neither requires nor constructs a continuous representative selection.

For (g,x) tending to (g*,x*), split

    F_g(x)-F_g*(x*)
       =[F_g(x)-F_g(x*)]+[F_g(x*)-F_g*(x*)].

The first term tends to zero by (6.1), and the second by (5.2). This proves joint quotient continuity. The bounded finite linear maps beta_out and P_out preserve it. Composing with the continuous real map gamma->gamma^(-1/2) proves (1.3).

Any fixed finite composition of these extracted updates is continuous on a set of initial data for which all intermediate couplings and activities remain in their common admissible domains. This is an elementary induction over the finitely many stages. One may restrict to a sufficiently small neighborhood of a trajectory lying strictly within those domains; alternatively the finite-induction envelope can provide uniform admissibility on a prescribed shooting interval.

The near-minimal representatives used to implement a trajectory may jump as its initial coupling varies. This does not affect continuity of its quotient classes or beta increments: exact finite-total descent proves that the represented map is independent of those choices. Raw vacuum factors can be tracked separately using the exact compensation identities; no continuous raw representative convention is needed for an endpoint statement about gamma.

## 7. Scope and the remaining shooting inputs

The theorem supplies continuity of the endpoint coupling for each fixed admissible finite history. Applying an intermediate-value argument additionally requires endpoints on opposite sides of the desired terminal value and control keeping the intervening histories within the weak range. Neither follows from continuity.

The current magnitude bound on each beta increment can keep a finite history weak by choosing its initial gamma sufficiently large, but that observation does not tune a fixed terminal coupling or prove the ultraviolet running trajectory. The present proof makes no claim of continuity at g=0, a regulator-independent modulus, positivity of the drift, convergence of raw vacuum normalizations, or a global measure interpretation beyond the already specified local analytic map and its legitimate continuation.

Primary inputs for this derivation are the exact finite formulas already proved in the companion workspace modules; no new external theorem or unverified source normalization is imported.
