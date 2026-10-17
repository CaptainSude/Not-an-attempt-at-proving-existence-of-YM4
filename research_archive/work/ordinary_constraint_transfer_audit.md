# Independent audit of the ordinary homogeneous constraint transfer

16 October 2026. Audited `work/ordinary_constraint_transfer_fragment.tex` in full. Result: pass, with no mathematical correction requested. The statement is a uniformly small global-potential minimum on finite homogeneous periodic regulators, not a global minimum over arbitrary lattice gauge fields.

## 1. Exact group identities and gauge order

The cumulative recursion `b_(t+1)=b_t|_(t+1) a(C_t)` agrees with the ordinary/corrected relation `M^t(U)=C_t^(b_t)`. Applying it to `U^g`, and substituting the one-step induced gauge `k_(t+1)=a(C_t^k_t)^(-1) k_t| a(C_t)`, cancels the two adjacent endpoint factors exactly. Induction therefore gives

`b_t(U^g) k_t = g|_t b_t(U)`.

The identity `k_j=b_j(U^g)^(-1) g|_j b_j(U)` has the correct noncommuting order. No invalid cocycle property of the logarithmic endpoint mean is assumed.

For an ordinary-feasible U, prescribing `k_j=b_j(U)` gives `C^j(U^g)=C^j(U)^(b_j(U))=D`. For the converse representative, `h|coarse=b_j(U_*)^(-1)` cancels the ordinary gauge on the left because `(V^b)^h=V^(h b)`. The two transformations are therefore directed correctly.

## 2. Uniform analytic domains

The gauge action's apparent inverse mesh factor is removable. With `ell=lambda(x)` and `v=nabla_mu lambda(x)`, the exact link product is

`exp(i eta Ad_exp(i ell) A) exp(i ell) exp(-i(ell+eta v))`.

At eta zero this is the identity for all small jet values. On a fixed small complex jet ball its logarithm is analytic and divisible by eta. Compactness of `eta in [0,1]`, followed by a fixed shrinkage of that ball, gives uniformly bounded coefficient derivatives. First differences of the resulting physical potential require A and lambda through first and second differences respectively; the complete Hölder product estimates close in the claimed `C1alpha × C2alpha -> C1alpha` spaces without an inverse-mesh loss. The real logarithm branch remains in the real Lie algebra in the unitary convention.

The cumulative b_j has uniformly bounded holomorphic maps on a common potential ball because its successive factors have size `O(h_t ||A||)` and the physical spacings are summable. Thus its evaluation at the gauge-transformed potential is valid after a fixed joint domain shrinkage. Evaluation of H_b theta at coarse vertices uses only its bounded norm and does not presume point interpolation.

The map K(A,theta) is consequently uniformly bounded and holomorphic into coarse bounded fields. Its derivative at the joint origin is exactly `Q0 H_b=I`; also K(A,0)=0 exactly. Banach-space Cauchy estimates on a larger common ball give the stated bound on `D_theta K-I`, independently of the number of variables. The resulting inverse contraction and estimate `||theta|| <= 2||omega||` are valid on fixed smaller balls. All logarithms occur on uniformly controlled identity branches.

## 3. Point interpolation and representative

The separate E_pt construction is necessary and correct. A compact smooth bump supported in `(-1/2,1/2)^d` and equal to one at zero gives exact coarse point values after translation. Periodizing its coefficients preserves this property even with one coarse cell in a periodic direction. The translated supports have uniformly bounded overlap, so continuum derivatives through order three are controlled by the coarse supremum norm. Sampling and the integral formula for physical finite differences give uniform scalar `C2alpha` bounds for every alpha below one, with no fine-dimension factor.

Using the principal logarithm of `b_j(U_*)^(-1)` followed by E_pt therefore gives an actual smooth fine gauge with the needed point values. The composed ordinary potential is holomorphic on a common coarse bounded-data ball and has norm `O(||B||)`. This does not rely on regularity of the coarse data beyond their supremum norm.

## 4. Minimum against the entire stated small field class

The reduced-Hessian result gives positive Hessian on one fixed convex ball in the linear xi-coordinate for every sufficiently small B. It therefore gives comparison with every xi in that ball, not only with infinitesimal competitors at the minimizer.

Every sufficiently small corrected-feasible fixed-slice field belongs to the chart, with exact coordinate `xi=(I-HQ)A`. Its norm is uniformly controlled because Q maps bounded fine data to bounded coarse data and H maps the latter into `C1alpha`.

The ordinary-to-corrected gauge map enlarges the potential norm by a fixed factor. The independently audited gauge flow into the fixed flat slice also has a fixed norm enlargement and preserves both action and the corrected constraint. Choosing the allowed ordinary field radius below these factors times the fixed chart radius ensures that every competitor in the theorem reaches the same convex xi-ball. Choosing the coarse B radius afterward makes the selected ordinary representative belong to the competitor class and places its minimizer coordinate in that ball. These are sequential uniform choices, not an implicit dependence on a particular competitor or regulator.

The action comparison and equality claim then follow. Equality forces the final slice field to equal U_*, by strict convexity. Both preceding operations and the representative construction are genuine gauge transformations, so the original competitor is gauge equivalent to U_ord. Since the two ordinary coarse fields coincide, ordinary gauge covariance implies that the coarse restriction of the connecting gauge stabilizes D. No uniqueness of that gauge is claimed or needed.

## 5. Scope retained

The proof applies to globally small complete `C1alpha` potentials, fixed-ratio homogeneous refinements, and finite compatible periodic regulators. It does not cover arbitrary fields specified only by small plaquette curvature, large gauge charts, topological sectors, mixed retained histories, or infinite-volume total action. It transfers the explicitly defined ordinary homogeneous average; broader source notation for heterogeneous averaging geometries is not silently identified with that map.

The source action normalization and separate ordinary/source-coordinate distinctions remain as recorded in the previous modules. Nothing in this transfer supplies an interacting continuum measure or a physical mass gap.
