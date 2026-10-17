# Independent audit of locality for the ordinary representative

16 October 2026. Audited `work/ordinary_representative_locality_research.md` and the full `work/ordinary_representative_locality_fragment.tex`. Result: pass, with no mathematical correction requested. The locality belongs to the explicitly constructed representative and is not inferred merely from gauge equivalence.

## 1. Local dependence and weighted derivative of the cumulative gauge

The endpoint product defining b_j has a final physical dependency radius independent of refinement. Each endpoint factor reads an intermediate field in a fixed one-step pattern; the intermediate field's dependence on the fine field is controlled by the sum of preceding physical radii. The last-stage and all earlier contributions lie in a uniformly bounded final neighborhood because the physical spacings form a geometric series. Restriction to the new coarse root does not add an unbounded displacement.

The common holomorphic bounded-potential domain and b_j minus identity bound therefore transfer to omega=log(b_j inverse)/i on a smaller fixed branch. Cauchy for the whole output row yields a uniform bounded-direction derivative, and restricting a direction to that row's dependency neighborhood yields the weighted estimate. This restriction is legitimate because omega consumes only bounded field values, not derivatives of the direction. There is no coefficientwise Cauchy estimate followed by an uncontrolled fine-site count.

The same argument applies to higher background derivatives, hence gives operator-valued holomorphy in the weighted norm. Backgrounds themselves need only be small in their unweighted norm.

## 2. Smooth interpolation and fine gauge action

The fixed point-value bump extension has uniformly finite range. On a cell collar its derivatives through order three read a fixed number of nearby coarse coefficients, whose weights are comparable. Sampling and integral finite-difference formulas give the asserted weighted C2alpha norm with constants independent of eta, including at the smallest compatible periodic volumes.

The displayed local jet representation of the gauge action is exact. Its logarithm vanishes at eta zero for all small jet values, so division by eta is analytically removable. All coefficient derivatives are uniformly bounded on a fixed small jet ball. A base in N_alpha and a scalar gauge parameter in C2alpha make the coefficient functions uniformly C1alpha. The discrete product and composition estimates then bound the first variation in weighted N_alpha using the variation jet (V,mu,Dmu). At most two scalar differences of mu appear in a first output difference; the Hölder bound uses those same derivatives. No extra fine derivative or inverse mesh constant is hidden here.

Composing this gauge-action derivative with the weighted E_pt Domega estimate proves the stated bound for DT(A) on N_alpha,w. It also proves its operator-valued analyticity, since the only non-jet dependence has already been controlled in the weighted local-row norm.

## 3. Leading extension and its sign

The transfer gauge has omega=-beta on the common branch, where beta=log b_j/i. At the flat point the gauge-action derivative is V-Dmu. Consequently

`DT(0)=I+D E_pt B_cum`,

with `B_cum=D beta(0)`. The plus sign is correct, and the leading lift is `H_ord=DT(0)H`, not H in general. The difference is a fine gradient, so `d H_ord=d H` exactly.

The exact nonlinear identity `F_ord(T(A))=F_corr(A)` follows from ordinary covariance and the coarse point values of the chosen fine gauge, which cancel b_j in the correct order. Its derivative gives `Q_ord DT(0)=Q` and hence `Q_ord H_ord=I`. This verifies the claimed linear constraint and does not identify H_ord with an independently prescribed source moving-gauge extension.

## 4. Responses and all orders

The chain rule `D_B A_ord=DT(A_*)D_B A_*` combines two operators with the same admissible weight, so the common exponent is retained. The composed response is holomorphic with a uniform weighted norm on an unweighted complex background ball. Its value at zero is H_ord. Cauchy therefore gives the O(||B||) correction to H_ord and the displayed one-weight factorial bound at all orders.

The Cauchy count is correct: differentiate the first-response operator n minus one times and use polyradii approaching delta/(n-1), obtaining `(n-1)! (e/delta)^(n-1)`. Symmetry allows each bounded input separately to carry the weight. The resulting maximum-of-distances localization is a valid consequence, while a fixed-exponent tree-length estimate is explicitly not claimed.

Finite localized changes follow by integrating the first response along the coarse straight segment inside the common ball. On the full lattice bounded truncated growing weights justify passage to the full support weight. The final caveat correctly separates literal Fréchet derivatives in globally bounded directions from their linearized extension to weighted directions that can be unbounded when the weight decays to zero.

## 5. Scope

The result applies uniformly to the chosen ordinary-feasible representative at small global backgrounds, fixed-ratio homogeneous refinements, and finite periodic regulators, with the stated complete-field extensions. It does not apply automatically to arbitrary gauge-equivalent choices, independently selected moving gauges, mixed retained histories, or continuum quantum measures. All these limits are retained accurately in the fragment.

## 6. Integrated Notebook 16 check

Read the integrated overview, the edited ordinary-representative bridge, the classical-Hessian coordinate boundary, and the conclusion in `outputs/ym4-nonlinear-response-notebook.tex`. They are consistent with the audited modules.

The explicit definitions `F_ord(A)=log M^j(exp(i eta A))/i`, `F_corr=F`, and `N_alpha=mathcal N_alpha` resolve the notation changes without changing the proof. Describing H_ord as something that “can differ” from H is appropriately more precise than a universal inequality. The alias R_0=R likewise refers to the same fixed scalar projection, not to the nonlinear remainder.

The ordinary coarse-potential Hessian is correctly distinguished from a based left-exponential Hessian: the latter requires the coordinate Jacobians and a background-current second-derivative contribution. The overview states locality for both explicitly chosen representatives and preserves the one-weight limitation. The tail accurately leaves the full fluctuation geometry, Jacobians, fluctuation integration, large fields, iterated complex sources, connected insertion estimates, and continuum properties unresolved. No incompatible strengthening was introduced during consolidation.
