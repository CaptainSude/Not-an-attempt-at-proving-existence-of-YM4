# Independent audit: uniform-depth strict support localization

17 October 2026. Independently audited:

* classical_local_vertex_bounds_research.md, Sections 1–8;
* classical_support_localization_research.md, Sections 1–8;
* their use of the already audited corrected-constraint fixed point, weighted Green bounds, ordinary-action gauge transfer, and exact fixed-L physical pivot chart.

The candidates were not edited by this auditor. This is an internal mathematical audit, not external certification or a continuum Yang–Mills theorem.

## Result

Pass. The two notes supply an actual support-valued contraction, uniformly in the preceding homogeneous classical refinement M and compatible periodic volume. The proof does not infer a multiple-support norm from one-weight response bounds. It constructs the stronger nonlinear mixed-cell insertion norm separately, uses the one-weight results only for linear cell propagators, and never substitutes the nonuniform ordinary rooted-average adjoint for the corrected physical adjoint.

The resulting scalar action decomposition has a small positive spatial tree exponent and any prescribed fixed support-cardinality reserve, with a correspondingly smaller background radius. It yields individually symmetric strict-support Hessian pieces. Its transfer through the actual fixed-L current chart supplies both the physical retained precision expansion and a localized classical cubic interaction with O(gR^3) norm.

One harmless precision was communicated: when choosing the abstract contraction radius in localization (4.2), also require its evaluated image to lie in the previously established classical branch's uniqueness ball. This is available by decreasing the same radius and changes no estimate. The note already works in the common small analytic domain; the clarification makes the later identification sentence completely literal.

## 1. Smooth complete cell spaces and physical normalization

The fine block spaces are spaces of complete supported fields, with the global N_alpha, C^alpha or supremum norm. They are not arbitrary cell restrictions requiring an unproved extension. Multiplication by a sampled smooth physical partition obeys a uniform N_alpha bound by the exact discrete product rule, uniform physical derivatives of the partition, and the complete Hölder norm. Reconstruction is uniformly bounded by finite overlap. For local Hölder pairs only finitely many neighboring supports matter; for separated pairs the supremum bound suffices. Periodization preserves these bounds when repeated occurrences are counted.

Thus C S^T can be applied to a localized C^alpha input without differentiating a sharp cell indicator. In the identity C S^T f=sum_j C S^T(chi_j f), all cutoff derivatives are part of the exact S^T operation and cancel in the reconstructed sum. This is a legitimate use of the equal-exponent constrained Schauder theorem.

The local Wilson energy is eta^4 times its fine plaquette sum. A fixed current cell has O(eta^-4) fine plaquettes, so its physical weighted count is bounded. The first differences are already in the bounded complete jet norm. No raw sum over M^4 unrelated fine coefficient variables is used.

## 2. The nonlinear vertex norm is genuinely stronger than one-weight response

After localization and reconstruction, a finite-range output reads at most D_R current input cells in each Taylor slot. Multivariable Cauchy on n directions at radii r/(n C_P), followed by division by n!, gives a coefficient norm at most C(e C_P/r)^n. Summing the D_R^n ordered cell tuples and paying a root-to-slot path of length at most R in each slot yields exactly the displayed analytic mixed-insertion majorant.

The estimate is a Banach-space estimate. Its constants do not depend on the dimension of a fine supported field space. It sums every input cell label, including repetitions; it is not a claim about a single weighted direction with all other directions treated globally.

The required primitives satisfy its hypotheses:

* The Wilson jet coefficient is a uniformly analytic N_alpha-to-C^alpha local map, with its eta singularity removed at the density level and degree at least two.
* The full corrected remainder R is uniformly analytic and quadratic, and its physical dependency radius is bounded by the geometric sum of one-step radii.
* DR(A)^T m uses the separately proved physical absolute-row estimate. Its transpose includes the fine physical volume ratio. The finite-dimensional holomorphic family has a uniform bound in this operator norm; Banach Cauchy therefore controls its local Taylor coefficients. Its output reads m within the corrected-map dependency radius and A within twice that radius. It starts at total degree two.

The last point is essential: bounded holomorphy of R into a coarse supremum norm alone would not justify a uniform bound on its physical transpose. The note uses the additional estimate rather than assuming it.

## 3. Linear cell propagators and the exact simultaneous equation

A complete input supported in a fixed collar of cell j has uniformly bounded norm in the exponentially growing weight centered at j. The previously proved complete-field weighted operator bounds therefore give the block envelope C exp(-kappa_0 d(i,j)). A smaller exponent yields summable rows and columns by polynomial cell growth. Both follow from this common envelope; no Banach-space self-adjointness is assumed.

This use of a one-source weight is appropriate because the maps are linear. In particular, the diagonal block of the differentiated constrained inverse is controlled by the actual equal-alpha Schauder estimate, not by an absolute singular-kernel integral.

The simultaneous equations

\[
 A=HB-HR(A)-CS^Tf(SA)+C DR(A)^Tm,
\]
\[
 m=qB-qR(A)+(SH)^Tf(SA)-H^TDR(A)^Tm
\]

have exactly the signs and order of the audited constrained stationarity equations. Rearranging the second equation recovers the multiplier inverse. The first then reconstructs the nonlinear constraint chart with its constrained-slice correction. There is no missing nonlinear-constraint term.

The redundant smooth block representation causes no extra solution: every right-hand side is the localization of a complete field. Each coefficient family, and hence the fixed point, is in the compatible image. Evaluation reconstructs the original equation.

## 4. The rooted support Banach algebra closes

The geometric choice is correct. Graph Steiner length permits the auxiliary input roots to remain vertices of a joining graph even when they are not final variable-support labels. Therefore

\[
 \tau(\{i\}\cup\bigcup_rX_r)
 \le \tau(\{i,j_1,\ldots,j_n\})
       +\sum_r\tau(\{j_r\}\cup X_r)
\]

has constant one. Metric MST length would not have this property after deleting intermediate roots. The final conversion ell_MST<=2 tau is explicitly paid by a spatial exponent reserve.

For the rooted family norm, linear propagation follows by adding a root-to-root path. Nonlinear substitution follows from the displayed Steiner inequality and |union X_r|<=sum|X_r|. Absolute summation over input cell labels, support labels, ordered Taylor slots and repeated labels gives the same analytic majorant as the ordinary Banach contraction. Grouping identical union supports is justified by that absolute convergence.

No coefficient introduces hidden background variables: all Taylor vertices are taken at the fixed flat baseline. Hence the support-cardinality weight exp(a|X|) is submultiplicative under union and does not change the nonlinear majorant. The initial singleton source alone incurs exp(a). Any prescribed finite a is consequently available by shrinking b, uniformly in M and volume. This is a genuine arbitrary fixed reserve, not an attempt to deduce exp(a|X|) from weak spatial decay.

The displayed majorant derivative bound is valid: for Phi(t)<=v(ct)^2/(1-ct), ct<=1/2 gives Phi'(t)<=8vc^2t. The stated radius ensures Lipschitz constant at most one half and invariance of the radius-2L_0 exp(a)b ball. The correction to the linear singleton family is O(b^2), coefficient by coefficient starts at degree two, and the evaluated fixed point agrees with the already established small branch by uniqueness.

## 5. Scalar envelope, re-rooting, and symmetric Hessian pieces

The action equality and envelope identity use the corrected-constraint multiplier, followed by the already proved exact gauge transfer to the ordinary action. They do not require the ordinary rooted-average physical adjoint.

Inserting the support family for n=m-qB into

\[
 S_M(B)-\tfrac12\langle B,qB\rangle
       =\int_0^1\sum_i\langle B_i,n_i(tB)\rangle\,dt
\]

gives a scalar coefficient with support Y={i} union X. It is holomorphic in precisely those original background variables and has degree at least three. To anchor at an arbitrary cell j in Y, tau(Y)>=d(i,j) pays the loss of spatial exponent. The resulting sum over old output roots is a uniformly summable exp(-delta d(i,j)) lattice sum. The cardinality increase is at most one and costs exp(a). Thus the O(b^3) scalar anchored norm, including its stated cardinal reserve, follows without a volume factor.

Cauchy on radius 2b gives an O(b^-2) bound on each second derivative block on radius b. This has no support-size factor because its two directions are normalized in the product supremum norm; the displayed 2e^2 constant is a safe bound. Summing the output matrix columns then costs at most |Y|, which the explicitly reserved positive cardinality exponent absorbs. The result is an O(b) strict-support row norm.

Each coefficient is a scalar Hessian and is therefore individually complex symmetric. Its rows and columns lie in Y and it reads only B|Y. This is the exact structure required by the precision support theorem; it is stronger than a symmetric sum of coefficients or an unstructured response decomposition. Uniform convergence on the larger domain justifies termwise differentiation.

## 6. The actual current chart and the classical remainder

The scalar quadratic baseline has pair supports {i,j}. The exponential row bound on q_M yields its anchored support estimate, with any finite cardinal reserve because a pair contains at most two cells. Adding the cubic scalar support family gives a complete action expansion on a fixed small product ball.

The actual fixed-L map

\[
 F_{\rm cur}(a,z)=\log(e^{i\Phi_V(z)}e^{ia})/i
\]

is finite range in both a and retained z and obeys a uniform small-field bound. Substituting it into a scalar coefficient enlarges its support from Y to Gamma Y. The bounds |Gamma Y|<=N_c|Y| and tau(Gamma Y)<=tau(Y)+c_c|Y| follow by attaching fixed trees to each old terminal. The arbitrarily large fixed cardinal reserve pays this enlargement. Re-rooting from a cell of Gamma Y to a cell of Y costs only a fixed neighbor count. Regrouping equal enlarged supports preserves absolute convergence and strict dependence.

The full local absolute gauge action can be added in the same product domain. It is not replaced by a relative penalty away from the physical gauge-zero branch. Hence differentiating the composed scalar coefficients in z retains both the constraint-current curvature and ordinary-log-coordinate curvature, as well as the off-branch gauge residual.

Subtracting each coefficient's flat z-Hessian gives individually symmetric precision pieces that vanish at a=0. Fixed-domain Cauchy bounds for the mixed derivative in a and twice in z, integrated along ta, give their O(b) size. A cardinal reserve pays the matrix column count. Their flat sum is the previously identified A_M(1); the inverse baseline is independent of every variable background and has the already proved uniform spectral and decay bounds.

For the cubic interaction, Cauchy or Taylor along the single direction z/R bounds the third remainder by C|g|R^3 times the coefficient's fixed-domain majorant. There is no unavoidable |X|^3 because that direction is normalized in the product norm. The resulting anchored scalar norm can carry exp[(4+log K_hat+spare)|X|], paid by the chosen reserve. Together with the explicit Steiner-to-MST exponent loss this gives the actual ob/otg interaction norm.

At physical backgrounds the sum of the subtracted linear terms vanishes. The product-domain extension correctly keeps these subtractions as its definition elsewhere. No unmodified off-stationary integral identity is claimed.

## 7. The ordinary-adjoint obstruction is correctly isolated

For the full ordinary rooted map, gauge covariance gives Q_ord D_eta lambda=D_1(lambda restricted to final centers). Taking lambda supported at one center gives fine L2 norm sqrt(2d)eta^(d/2-1) and fine L1 norm 2d eta^(d-1), while the coarse gradient has fixed size. Thus the lower bounds eta^(1-d/2) for the L2 operator and eta^(1-d) for its physical transpose on bounded fields are correct. In d=4 they are eta^-1 and eta^-3.

This counterexample does not contradict the complete-field regularity statements because that fine spike has a large N_alpha norm. It does rule out an unjustified replacement of the corrected adjoint in the fixed point. The notes avoid that replacement and transfer only the scalar action by the exact gauge argument. The fixed-ratio-L current pivot chart is unaffected by the obstruction because its constants may depend on L.

## 8. Scope of the result

The result is uniform through homogeneous classical refinement and compatible periodic volume. Its strict supports refer to the independent current background variables; it is not an independent-free-current theorem or a mixed-history boundary theorem. The current chart still uses the admissible incidence geometry already assumed in its proof. Periodic graph estimates do not remove that geometry condition.

The localized classical precision and cubic remainder can now be supplied to the Gaussian integration module at every homogeneous classical depth, alongside the separately proved measure terms and cutoff conditions. Prior quantum effective interactions, their propagation through changing backgrounds, large-field complements, running-coupling estimates and continuum reconstruction remain separate obligations. No such conclusion is implied solely by this localization result.

## 9. Audit of the integration corollary

Also read classical_step_integration_fragment.tex in full. Its substantive mathematics passes. Fixed-L regrouping of current cells changes dependency neighborhoods, finite coordinate counts, row norms and exponents by fixed constants only. The cell fluctuation dimension remains d(L^d-1)dim(g), independent of earlier classical depth. The support theorem's cardinal reserve pays the Gaussian density multiplier cost, while its spatial reserve can be chosen to satisfy both the baseline covariance and precision-localization exponents.

The precision smallness conditions can be imposed using one background radius before the coupling ceiling is chosen: the entire family has a common real flat spectral interval, a common weighted baseline inverse bound, and precision label norm Cb. The classical, normalized Jacobian and Haar multipliers then have the common O(gR^3) norm for R>=1. The rectangular bad event is still controlled by the cell Gaussian norm tail. Thus the same strict tunable theorem, including its comparison with the cutoff-only expansion and its periodic extension, applies with constants independent of M.

The determinant closed-chain proof does not require bounded label sizes. A precision label already carries its full tree-length weight in the row norm. Joining its input and output through a tree containing the entire support is therefore paid by that norm. The union with covariance-link paths is connected, has at most one plus the total chosen edge length vertices, and contains every background read by the trace term. The rooted bound D(K_t nu_t)^n and the subsequent rerooting sum are unchanged. Absolute convergence supplies connected, strict local determinant activities with anchored O(b) norm, uniformly in M.

The exact constrained chart integral has the same Haar, delta, coupling-scaling and Gaussian factors as in the independently audited bare case, with S_1 replaced by the explicitly defined classical reference action S_M and A_0 by A_M,0. The fixed chart and the local measures are independent of earlier depth; no prior quantum determinant or interaction is implicitly claimed to be included. The physical stationary family makes the separated linear sum zero and the gauge constant zero. The formula is exact for that defined classical-reference integral, not for an already iterated quantum marginal.

One additional scope clarification was sent to the parent and adopted in the ci fragment: any gauge-insertion identity outside this chart requires S_M itself, as well as the contour and average maps, to be defined and gauge invariant on the chosen rooted-gauge-invariant domain. The bare Wilson action had that global invariance automatically; the present theorem constructs S_M on a small potential branch. No extension to an arbitrary large gauge orbit is needed for the chart identity. This qualification does not alter the integration or support theorem. With that correction adopted, the integration corollary passes without an outstanding requested change.
