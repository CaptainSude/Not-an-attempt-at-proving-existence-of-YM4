# Independent audit of the Gaussian strict-support construction

16 October 2026. Audited `gaussian_cutoff_locality_research.md`, especially Sections 3, 5, and 7, against the marked Gaussian cluster mechanism. Also checked the integrated direct-Hessian result and thermodynamic-limit argument in Section 6 of `outputs/ym4-current-cutoff-notebook.tex`. No substantive mathematical error was found under the explicitly stated hypotheses. This is an audit of the abstract statements, not a verification of the deposited Yang--Mills precision or background domains.

## 1. Canonical support series and factorization

There is a consistent canonical interpretation of all support-valued operations. In finite volume, attach one independent formal scalar variable t_Y to each V_Y. Expand the covariance, marginal density, forest formula, and logarithm at t=0, retaining their multidegrees. A monomial has the background support given by the union of its Y labels. Grouping monomials by that union is multiplicative for union convolution. The absolute support-norm bounds in Sections 3--5 permit this grouping and evaluation at all t_Y=1.

For a forest with distinct marked components S_i, setting cross-component covariance entries to zero makes the full marginal matrix block diagonal as an identity in the formal t variables. Its normalized Gaussian density factors coefficientwise, even when the blocks involve some of the same t_Y or background coordinates. Thus the forest moment factorization is valid before support grouping and remains valid after grouping. The exact polymer compatibility is disjointness of the marked sets S_i. Replacing it by disjointness of the background supports would change the gas and is unjustified.

The support algebra for a larger marked root set contains the smaller-root algebra by a norm-decreasing map, since adding roots can only shorten the attachment forest. Consequently componentwise factorization and the subsequent logarithmic products can all be interpreted in a common algebra without a hidden norm loss.

## 2. Covariance paths and the inverse norm

For each covariance Neumann path, the covariance links and trees on the perturbation supports form a connected graph joining the marginal endpoints. Its length bounds both the attachment length and endpoint distance. The weighted row/column sums therefore give exactly K^(j+1) nu^j at perturbation order j, and the bound v=K^2 nu/(1-K nu) in (3.3) is valid.

The crucial distinction in Section 5 is correct: the inverse M_0^{-1} is a matrix on the marked root set S, with no variable background support. Its ordinary Schur bound L is sufficient. Multiplying it into support-valued matrices only combines entries whose supports have already been attached to S; no new attachment distance must be paid. A fast inverse decay exponent is not silently substituted for the original covariance decay.

The inverse estimate itself is uniform in S, the tree, the interpolation point, and the complex Cauchy parameters. For s<=m/2, the conjugation error is at most 2s Kbar/(e m), so the displayed choice of s makes it at most a/2. The resulting L=(4/lambda) sum_z exp(-s|z|) is legitimate, albeit possibly large. Its size is explicitly paid in the smallness conditions on nu.

## 3. Full density and constants

The determinant and inverse are both expanded in the support algebra. With u=L v_1, the trace-log bound is D|S|[-log(1-u)], and the inverse difference is bounded by w=L^2 v_1/(1-u). The row-and-column Schur bound also gives the required support-norm estimate on the quadratic form x^T(M^{-1}-M_0^{-1})x; it is not merely an estimate after evaluating the support series.

The constants in the density domination are conservative and consistent. From Herm M_0>=lambda/2 and ||M_0||<=2 Lambda_0 one gets Herm M_0^{-1}>=1/V with V=8 Lambda_0^2/lambda. The determinant lower bound, u<=1/2, and w<=1/(2V) yield domination by (8V/lambda)^(D|S|/2) times the real Gaussian density with covariance 2V I. The exponential Markov tail for each block then gives

    tau_hat_R = (16V/lambda)^(D/2) exp(-R^2/(8V)).

The Cauchy degree cost is also correct: the product over edges of max(d_b,d_c) is at most the product over vertices d_b^(d_b), which is at most e^(2|S|-2) times the product of d_b!. Thus the factor (e^2/delta)^(|S|-1) in (6.1) has no missing factor of two. The choice B_0=8e^2 A_kappa/delta safely exceeds the factorial tree constant 27e^2 A_kappa/(4delta).

The cutoff condition tau_hat_R <= [2e^2 max(1,B_0)]^(-1) gives a marked Kotecky--Preiss bound after spending two factors exp(|S|). It leads to the stated 2e^2 tau_hat_R anchored logarithm bound.

## 4. Paying for all support roots

For a connected marked cluster, the tree lengths and rooted attachment lengths are subadditive in precisely the direction needed in (7.1). The deterministic paths used to form H add at most the total metric length L, while every point of H is within distance L of any selected marked point. The inequality (7.3) therefore follows for a_* = min(1/2,kappa/4).

Summing over all possible marked anchors deliberately overcounts the cluster. Combining that overcount with (7.1) gives the finite lattice sum in (7.4). This pays for roots lying in an added background support or in a connecting path; no root is left uncontrolled. Supports outside a nonconvex finite region can be treated as labels in the ambient lattice hull, with the coefficient still reading only the original background coordinates.

## 5. Scope that must remain explicit

* The theorem establishes local variable-background dependence, holomorphy, and a weighted connected-support bound. The coefficients may depend on the entire fixed baseline covariance and need not agree between volumes.
* A product background domain, or an independently justified substitute for its local-function algebra, is assumed. A weak gauge-field chart ball is not automatically such a domain.
* Canonical shortest-path choices can be made translation-equivariant on the lattice but can break discrete rotation symmetry. The theorem does not claim that its individual activities preserve rotations or gauge symmetry.
* Even a symmetric total functional does not by itself imply that each displayed activity is gauge invariant. Any required activity-level symmetry needs an equivariant construction or a justified averaging step that preserves the actual domain, support convention, and norm. Finite discrete symmetry averaging is available when those objects are invariant, but those hypotheses must be checked; local gauge averaging needs its own domain and support check.
* Matching the actual constrained variables, precision perturbation norm, running-coupling domain, and interaction terms remains outside the theorem.

## 6. Integrated direct-Hessian result

The integrated Section 6 matches the independently audited Hessian argument: the common majorant is uniform over the two covariance directions, the mixed Cauchy coefficient has no extra factorial, and the finite-support precision response constants are unchanged. The nonlinear second-precision term is explicitly retained as a separate required estimate.

The thermodynamic-limit paragraph is valid with its stated entrywise convergence assumption, fixed cutoffs and local geometric identification. The finite inclusion--exclusion identity identifies each fixed marked-union coefficient. For omitted unions, dist(x,X)+ell(X)>=L; spending kappa/2 of the available decay leaves an integrable anchor sum and gives the stated uniform exponentially small tail. Uniform bounds alone do not imply this entrywise convergence, and the text correctly says so.
