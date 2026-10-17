# Independent normalization and formula audit: determinant Maxwell trace

17 October 2026. Read the complete determinant_maxwell_trace_research.md, including the classical vertex subsection, and compared its definitions with composite_macrostep_integral_research.md Section4, physical_current_pivot_precision_research.md Sections2/6, and physical_pivot_measure_research.md Sections2/3. Result: pass. No mathematical correction requested.

## Exact measure factors

The exact constrained integral has the background pivot factor product(det C_(c,p))^(-1) and the Gaussian factor det(A)^(-1/2). Dividing each by its flat value gives precisely Delta=-sum log det pi and Qdet=-one_half log det(A A0^(-1)). The angle-column factor R^(1-d) is field independent and cancels in the pivot ratio.

Relative link Haar coordinates are exp(i Phi_a(z)) exp(i a). Haar translation invariance gives j(Phi_a(z)); it does not introduce j(a). Likewise the normalized ambient straightening determinant equals one at zero fluctuation. Consequently neither factor produces an additional background contribution at g=0. The compact gauge-insertion constant, Haar origin constants, g powers and flat determinant remain vacuum factors. The signs and trace measures in (1.4) match the previously audited exact finite formula.

This is fidelity to the actual chosen composite local macrostep. The underlying primitive source formulas are the retained pivot straightening and left-relative Haar convention already traced to CMP109 and CMP116. The new one-shot composite sector is not being represented as a published direct-R averaging identity or as a product of primitive cutoff sectors.

## Hessian chain rule and symmetry cancellation

The logarithmic determinant identity gives

    D2 log det A[u,v]
       =Tr(C0 A_uv-C0 A_u C0 A_v),

with matrix order retained. The pivot formula is the same identity with flat matrix I. The physical second response B_uv occurs exactly through the independent-background scalar derivative D d_M(0)[B_uv].

Constant color conjugation acts orthogonally on the retained coordinates and by similarity on every pivot block. The unique local constraint chart is equivariant. Thus both independent-background scalar logarithms are globally color invariant. For a semisimple Lie algebra their linear functionals vanish in every individual current-bond color slot. This removes B_uv after taking the scalar traces, separately in the pivot and Gaussian terms.

It does not remove the operator derivatives A_1 or pi_1, nor current-times-chart-curvature terms inside A_1/A_2. The note correctly retains the full chain rule for groups with abelian factors.

## Stationary lift and precision vertices

The affine constraint chart has derivatives h in the coarse datum and K in retained coordinates. The full flat Hessian is P_M=q_M+T_R^T T_R. Since T_R h=0, the cross block is K^T q_M h. Solving the retained linear critical equation gives H=h-K C0 K^T q_M h. This uses angle/counting coordinates throughout and requires no extra M^4 or R^4 factor.

Twice differentiating retained stationarity gives (4.5); differentiating the affine implicit chart gives (4.6). These are correct derivative formulas, not Taylor coefficients.

For Xi_a(B)=log(exp(iB)exp(ia))/i, the left-trivialized exponential differential is J_a, so D_B Xi_a(0)=J_a^(-1). The second chart response has both

    -J_a^(-1) h_a F_a''[K_a u,K_a v]

and the ordinary-log conversion Xi_a''[K_a u,K_a v]. Equation (5.3) is therefore the full pullback Hessian. Differentiating it once and twice gives exactly (5.4)-(5.5): the four W3/E1 terms, two W2/E2 terms, two mixed W2/E1 terms, W3[p,q,T0], and both W2[p,T1[q]] terms are all present. W1=0 is the sole reason its second derivative times T disappears.

The absolute contour gauge is retained inside W_M on the independent background domain. It is not silently replaced by a relative quadratic penalty.

The simultaneous corrected fixed-slice system has V(0)=DV(0)=0. Its derivatives Y2=V2[L,L] and Y3=V3[L,L,L]+three V2[Y2,L] terms are correct with no missing factorial. The envelope identity DS_M=m then gives the action's cubic and quartic derivatives in (5.9). Physical fine transposes remain inside that system; they are not inserted again into the current retained-coordinate trace.

## Absolute sums and the Maxwell coefficient

The strict precision decomposition has both matrix endpoints and its background variables inside the same carrier. Cauchy differentiation at source x therefore selects carriers containing x, and a spare spatial exponent bounds row distance from x. For two sources another spare exponent bounds their separation. These facts justify the absolute-entry estimates (6.2), not merely an operator-norm estimate.

In Tr(C0 A_x C0 A_y), the source-root weights and a covariance edge provide a path from x to y; the remaining factors are absolutely summable. The same argument applies after the exponentially decaying stationary lift. Thus the displayed trace expressions define local infinite kernels without asserting existence of an extensive infinite log determinant.

For a diagonal orientation, the midpoint shifts cancel. If K_mumu(p)=beta sum_(nu!=mu) p_nu^2+O(p^4), then differentiating its Fourier sum twice yields beta=-one_half sum_r r_nu^2 K_mumu(r). This verifies the sign and factor in (7.2), and hence the plus one_half pivot and plus one_quarter Gaussian prefactors in (7.3). No color sum is needed when one trace-orthonormal color is fixed.

The finite trace identity remains exact, but its finite beta is the short-lift moment divided by the actual finite reference moment. The latter is only 1+O(exp(-cN)). The note correctly separates this finite normalization from infinite Ward classification and makes no sign, universal-coefficient, old-depth-limit or running-trajectory assertion.

## TeX fidelity addendum

Read the full determinant_maxwell_trace_fragment.tex after the research audit. It faithfully preserves all checked formulas and scope: actual relative constraint and absolute gauge; both determinant signs and vacuum separation; full and reduced Hessian chain rules; affine stationary response; both chart-curvature contributions and every precision vertex multiplicity; the physical fine fixed-point recursion; absolute source-root trace estimates; and the finite versus infinite Maxwell normalization. No transcription correction found. No compilation was performed.
