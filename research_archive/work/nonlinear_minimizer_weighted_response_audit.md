# Independent audit: weighted responses of the corrected minimizer

16 October 2026. Audited `work/nonlinear_minimizer_weighted_response_research.md`, especially Sections 2–6, against the already audited constrained Schauder, nonlinear averaging, and fixed-slice minimizer modules.

Status: the mathematical estimates and stated localization consequences pass. One functional-domain clarification for arbitrary decaying weights on the infinite lattice is recorded in Section 7 below; it does not affect the localized-source conclusions or finite-volume assertions.

## 1. Physical transpose and the doubled background radius

The full corrected nonlinear average has a fixed physical dependency radius, independent of refinement. Consequently an output row of its physical transpose at a fine bond b reads only coarse bonds c within that radius. The coefficient belonging to c depends on the background only in the dependency set of c, so the union relevant to the row lies within twice the radius of b. The doubled radius in (2.3) is correct and cannot generally be replaced by the original radius without additional geometry.

The physical row estimate is the appropriate one for Cauchy. The fixed-L coefficient proof controls the absolute physical transpose row sum, not just individual entries. Its one-step normalization contains the fixed factor L^d; composition produces the sum of spacings, rather than a growing fine dimension. At each finite regulator the map into this finite-dimensional physical-row norm is holomorphic, and the uniform bound on a fixed complex background ball gives a uniform derivative bound by Banach-valued Cauchy. There is no uncontrolled sum after coefficientwise Cauchy.

For one row, replacing the direction V by its restriction to the row's union of dependency sets does not change the derivative. This restriction is legitimate: the coefficient map consumes bounded field values and no fine derivative of V is taken. Its supremum is at most `exp(2 kappa R_*) w(b)^-1 ||V||_(infinity,w)`. Multiplication by w(b), followed by the already bounded physical row acting on the unweighted multiplier m, proves (2.3). Neither a derivative cutoff nor a hidden weighted norm of m occurs. Periodic lifted incidences do not alter the fixed-radius argument.

The same reasoning yields a weighted input bound for `D_A` and `D_A^T` with the single dependency radius. It also gives the required mixed operator-valued analyticity with one weighted coefficient direction and other unweighted directions.

## 2. Exact chart and multiplier variations

Differentiating the chart gives

`v=(I+H D_A)^-1 (z+H b_1)`.

The weighted norm of `H D_A` is small because H accepts bounded coarse weighted input and `D_A` consumes only the values of the variation. Background smallness is measured in the unweighted norm. The physical weighted norm of `H^T D_A^T` is small by the same reasoning.

Differentiating the defining multiplier equation

`(I+H^T D_A^T)m=q(B-R(A))+H^T N(A)`

gives exactly

`delta m=(I+H^T D_A^T)^-1 {q(b_1-D_Av)+H^T N'(A)v-H^T(D_A^T)'[v]m}`.

The operator order and sign of the last term are correct. It would be missing in a naive differentiation treating the transpose coefficients as fixed. Its weighted norm is covered precisely by Section 2's mixed estimate, using the unweighted bound on m.

The force variation is handled through its jet coefficients. The constrained Schauder operator acts on `S_jet^T` without differentiating the coefficient in a pointwise norm, while the H transpose uses `(S_jet H)^T`. Thus all estimates retain the same Hölder exponent and do not introduce derivatives of a rough nonlinear coefficient.

These bounds give (3.6) with the stated dependence on `r+b+r^2`. The base fields A, B and m are never required to have finite norm for a growing weight.

## 3. Weighted implicit inverse and the flat leading term

The exact fixed-point differential is

`delta Phi=-C N'(A)v+C{(D_A^T)'[v]m+D_A^T delta m}`.

Its three terms have the bounds used in (4.3): respectively `O(r)||v||_w`, `O(b+r^2)||v||_w`, and `O(r)(||b_1||_w+(r+b+r^2)||v||_w)`. For a fixed small r these combine into `C_kappa((r+b)||v||_w+r||b_1||_w)`.

The range lies in the fixed constraint/gauge slice because C is outside every term. The linearized chart then gives a uniform strict contraction in the weighted tangent space after one fixed shrinkage of the background radii. No uniformly bounded pointwise norm of the separate gauge projection is presumed.

At finite regulators the weighted Neumann inverse is the derivative of the already selected unweighted analytic minimizer by uniqueness of the linearized equation. On complete fields this identification also holds for directions in the common bounded and weighted domain: the same partial Neumann sums converge pointwise to both solutions. The formula defines a bounded extension to the full weighted domain when needed.

At the actual solution `r=O(||B||_infinity)`, the source term in the xi response is `O(||B||_infinity)||b_1||_w`. Also `P_A-I=-P_A H D_A` has that small order. These facts prove both estimates in (4.6), including `D_B A(B)-H=O(||B||_infinity)` in the weighted response norm.

## 4. Finite localized changes

For a source supported in S, `w_S(n)=exp(kappa d(n,S))` is admissible. Its weighted source norm equals the ordinary supremum norm up to the stated fixed orientation/collar constant. The response estimate therefore gives the exponential decay (5.1) with no source-size factor.

If two small coarse backgrounds differ only in S, their straight segment remains in the common ball. Integrating the derivative estimate gives (5.2). On the infinite lattice, one can first replace a growing weight by `min(w,R)`. The truncated weight remains admissible and is bounded above, so an unweighted analytic solution is automatically a weighted one for this intermediate step. The derivative estimate is independent of R. Passing to the increasing weight limit yields the stated difference estimate without assuming that either individual background or minimizer decays.

The same argument handles a general finite weighted difference by bounded truncations of the weight. It is the difference of the solutions, not the individual solutions, that is placed in the weighted space.

## 5. Operator-valued holomorphy and factorial derivatives

The formula for the first response is holomorphic into the weighted operator norm on a fixed smaller complex background ball. The factors are the fixed weighted Green operators, local analytic coefficient maps with the physical-row bounds above, the unweighted analytic background solution and multiplier, and uniformly convergent weighted Neumann inverses. This justifies an operator-valued Cauchy estimate rather than merely pointwise holomorphy of individual entries.

For n>1, applying multivariable Cauchy to `B -> D_B A(B)` with n-1 unweighted background directions and radii approaching `delta/((n-1)||b_i||)` gives

`C_kappa ((n-1)/delta)^(n-1) ||b_1||_w product_(i>=2)||b_i||`.

The elementary inequality `m^m<=e^m m!` yields exactly (6.1). No extra factorial is needed: each of the n-1 independent complex variables is differentiated once. For n=1 the result is the first-response estimate. The margin delta and constants are uniform after the fixed weighted-radius shrinkage.

The background directions used in this Cauchy argument are unweighted bounded directions. Consequently no weighted smallness is being imposed on the background in order to differentiate it.

## 6. What the support corollary proves

Symmetry of the higher derivatives on bounded directions allows each selected localized direction to carry its own weight. Applying the estimate once for each insertion gives the same factorial and product-of-supremum factor, multiplied by `exp(-kappa d(n,S_i))`. Taking the smallest of these bounds gives exactly

`exp(-kappa max_i d(n,S_i))`.

This is valid and has no extra factor of n. It is not a tree-length estimate joining all source sets and the output; the note correctly avoids that stronger conclusion. The chosen corrected fixed-slice representative is retained throughout. Locality of the separately gauge-transferred ordinary representative is not inferred from gauge equivalence.

## 7. One precise domain clarification

For an arbitrary admissible weight on the infinite lattice, the weight may decay to zero. Then a field with finite weighted supremum norm can be globally unbounded, so it is not literally a direction in the original unweighted coarse background Banach space.

A precise formulation is: first state the Fréchet response and its symmetry for globally bounded directions having the selected finite weighted norm. The weighted Neumann formula then defines its bounded linear extension to the full weighted space. The first-response operator-valued holomorphy can be stated for that extension. Higher-response symmetry is first read on bounded directions, which includes every localized direction used in the support corollary.

All weights `w_S` in the localization assertions satisfy `w_S>=1`; their finite-norm directions are automatically bounded. Thus this clarification changes none of the stated exponential locality, finite localized-change, or one-weight factorial conclusions. It only prevents an overly literal interpretation of the word derivative outside the original background domain.
