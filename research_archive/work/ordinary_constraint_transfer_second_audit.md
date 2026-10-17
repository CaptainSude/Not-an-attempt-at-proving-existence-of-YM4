# Independent mathematical audit: transfer to the ordinary constraint

16 October 2026. Audited `work/ordinary_constraint_transfer_fragment.tex`, including its use of the reduced-Hessian estimate in `nonlinear_fixed_gauge_minimizer_research.md`, the gauge-flow module, and the scalar extension from the constrained Green analysis. Status: pass; no mathematical correction needed before promotion within the stated finite homogeneous scope.

## 1. Exact cumulative gauge and factor order

With the convention `U^g=g_- U g_+^-1`, two successive actions satisfy `(U^b)^h=U^(hb)`. The ordinary and corrected iterates obey

`b_(t+1)(U)=b_t(U)|_(t+1) a(C_t)`,

`M^t(U)=C_t^(b_t(U))`.

For a fine gauge `g`, the corrected induced gauge satisfies

`k_(t+1)=a(C_t^(k_t))^-1 k_t|_(t+1) a(C_t)`.

Multiplying this last formula on the left by `b_(t+1)(U^g)` cancels the two adjacent endpoint-mean factors before using the induction hypothesis. This proves the identity of gauge functions themselves,

`b_t(U^g) k_t = g|_t b_t(U)`,

and hence `k_j=b_j(U^g)^-1 g|_j b_j(U)` in precisely the displayed order. The argument does not infer equality of gauge functions merely from equality of their actions on a connection, which would leave a stabilizer ambiguity. It also does not require a logarithmic-mean cocycle.

The uniform bound on `b_j-I` follows from the already established product bound with summable physical spacings. A coarse supremum bound is sufficient throughout this transfer; no unproved coarse derivative estimate on this cumulative gauge is needed.

## 2. Fine gauge action in the physical regularity norm

For one bond, set `ell=lambda(e_-)` and `v=(lambda(e_+)-lambda(e_-))/eta`. The identity

`exp(i ell) exp(i eta A) exp(-i(ell+eta v))`

`=exp(i eta Ad_(exp(i ell)) A) exp(i ell) exp(-i(ell+eta v))`

has the correct factor order. At eta zero the final product is identity for every small jet `(A,ell,v)`. Its small-branch logarithm is therefore divisible by eta analytically. One may take eta in a fixed complex neighborhood of the interval `[0,1]` and the jet in a sufficiently small fixed complex ball, so the resulting finite-dimensional derivative bounds are uniform in the real lattice spacing.

The fine ordinary potential after gauge transformation is consequently a uniformly analytic function of the local jet `(A,lambda,Dlambda)`. For `A` in `C^(1,alpha)` and `lambda` in `C^(2,alpha)`, all entries of that jet have uniform `C^(1,alpha)` bounds. Discrete product, shift, and composition estimates control the output in the same potential norm. In particular, one output difference differentiates lambda at most twice; its Hölder increment is covered by the assumed scalar norm. This proves the stated gauge-action bound without a false eta-inverse loss.

The same local analytic construction preserves the real Lie algebra on the real slice and stays on the common group-logarithm branch after a fixed reduction of the radii.

## 3. Prescribing the corrected induced gauge

The map

`K(A,theta)=(1/i) log k_j(exp(i eta A), exp(i H_b theta))`

is uniformly bounded and holomorphic on a fixed product ball. This follows from the exact cumulative-gauge identity, the preceding fine gauge-action estimate, `H_b:coarse infinity -> scalar C^(2,alpha)`, and the uniform holomorphy of the cumulative gauges on the ordinary potential ball. The restriction of `H_b theta` to coarse vertices costs at most its supremum norm; it does not assert point interpolation by `H_b`.

The two key identities are correct:

`K(A,0)=0`,

`D_theta K(0,0)=G_0 H_b=Q_0 H_b=I`.

Uniform Banach-valued Cauchy estimates bound the change of this derivative by `C(||A||_(C1alpha)+||theta||_infinity)`. These estimates are independent of the dimension of the finite coarse field space because they follow from a common holomorphic ball and supremum bound, with directional Cauchy estimates. They do not arise from estimating individual matrix entries and summing a volume-dependent number of entries.

The displayed contraction has a uniform radius. On a smaller product ball its Lipschitz constant is at most one half, and `K(A,0)=0` gives the solution bound `||theta||<=2||omega||`. Uniform holomorphic dependence follows from the same contraction or the analytic implicit-function theorem. Real coefficients give a real solution for real data.

If `M^j(U)=D`, then `C^j(U)^(b_j(U))=D`. Prescribing the induced gauge to be exactly `b_j(U)` therefore sends the field to the corrected constraint. Its fine gauge parameter has norm bounded by `C||A||_(C1alpha)`, and so does the transformed potential. The common small branches also identify the group equality with the corresponding corrected potential target `B` when required by the minimizer chart.

## 4. A distinct point-value extension is necessary and is provided

The bump construction `E_pt` is a genuine right inverse of restriction to the coarse vertices. At an integer vertex only the bump centered there contributes. The periodic sum is well defined and has uniformly bounded overlap, including the smallest coarse periods. Sampling a fixed smooth periodic interpolation and applying the integral formulas for finite differences proves uniform scalar `C^(2,alpha)` control from the coarse supremum norm. A third continuous derivative bound supplies the second-difference Hölder estimate for every fixed alpha below one.

This operator is correctly kept distinct from `H_b`, which is a right inverse of the scalar block average, not of point restriction.

For the corrected minimizer `U_*`, take the coarse point value `h_*|=b_j(U_*)^-1`. Since

`M^j(U_*)=D^(b_j(U_*))`,

ordinary gauge covariance gives

`M^j(U_*^(h_*))=(D^(b_j(U_*)))^(b_j(U_*)^-1)=D`.

The inverse gauge is on the left in the composite action, as required. The potential bound and holomorphic extension follow from the analytic corrected minimizer, the logarithm of the uniformly near-identity cumulative gauge, the bounded linear point extension, and the analytic fine gauge action.

## 5. The fixed small-ball action comparison is justified

The stronger conclusion is not being inferred from strict minimality at a single point. Section 5 of `nonlinear_fixed_gauge_minimizer_research.md` proves the reduced Hessian lower bound throughout a sufficiently small real chart:

`D_xi^2 S(A(xi,B))[z,z] >= (1/2)<z,Kz>`.

The domain can be chosen as a fixed ball in the linear `xi` Banach space, hence it is convex. For all sufficiently small `B`, the chart is defined on this same ball and its image remains in the uniform estimate domain. Integrating the Hessian bound along the straight segment from the stationary coordinate to any other coordinate in the ball proves a strict action comparison on the whole ball, independently of regulator volume or refinement.

Every sufficiently small corrected-feasible field in the flat gauge is represented by this chart: its coordinate is exactly `xi=(I-HQ)A`, because `F(A)=QA+R(A)=B`. The fixed gauge is retained since `RD^T H=0`. The bounds `Q:infinity -> coarse infinity` and `H:coarse infinity -> C^(1,alpha)` give a uniform bound on this coordinate.

To make the radii explicit in principle, let C_1 be the ordinary-to-corrected norm factor, C_2 the subsequent gauge-flow norm factor, and C_3 the norm of `I-HQ` on the potential space. Choose `r_0` so that `C_1 r_0` lies in the flow domain, `C_1 C_2 r_0` lies in the chart domain, and `C_1 C_2 C_3 r_0` lies strictly inside the fixed convex coordinate ball. All three constants and domains are uniform. Choose `b_0` smaller so that the ordinary representative is in the `r_0` class and the minimizer coordinate is inside the same convex ball. These are simultaneous fixed-radius choices, not choices depending on a comparison field or on volume.

Both operations preserve the Wilson action and are actual fine gauge transformations. The corrected slice comparison therefore proves the minimum among all ordinary-feasible fields in the stated global `C^(1,alpha)` ball. Equality forces the final slice representative to be `U_*`; composing the genuine gauge transformations proves that the original comparison field is gauge equivalent to the ordinary representative.

Because both endpoints satisfy the same ordinary constraint, ordinary gauge covariance implies that the connecting gauge restricts to a stabilizer of that coarse field. Thus the resulting gauge transformation preserves the ordinary constraint. No uniqueness of its parameter is needed or claimed.

## 6. Scope

The conclusion is valid for the explicitly defined homogeneous ordinary iteration on finite compatible periodic regulators and within one fixed small global potential class. The argument does not establish a global minimum over large fields, an arbitrary local-frame constraint, a mixed retained history, or a quantum continuum measure. These limitations are stated accurately in the fragment.
