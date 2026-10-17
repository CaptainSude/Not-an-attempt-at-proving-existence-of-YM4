# Second independent audit of nonlinear gauge coverage

16 October 2026. Audited `work/nonlinear_gauge_slice_research.tex` in full, with particular attention to scalar regularity, the gauge-fixing differential, and whether the limiting field belongs to the original constraint-preserving gauge orbit. Status: pass; no correction needed.

## 1. Scalar operators and regularity

The canceled formulas for `T=Z L=G'R_0` have the correct central and mixed factors. Its high diagonal is `1/P_r`; its rank output is `a_r^-/P_r^2`, with input row `a_s/P_s`. Subtracting `(L+1)^-1` leaves a high heat factor `1-e^-t`. Two output differences and an alpha-Hölder increment give the integrable small-time bound `t^(-alpha/2)`. The massive part maps `C^alpha` to full `C^(2,alpha)` through the previously audited second/third heat-moment bounds and the separation-dependent `r^2` split. This controls all mixed second differences, not merely the scalar Laplacian.

The projection formula `R_0=I-chi chi^-/D_s,2`, with `chi_0=a_0^-` and `chi_r=P_0a_r^-/P_r`, is algebraically correct. The subtracted projection maps bounded data into `C^(1,beta)` for every beta below one: its output aliases are absolutely summable after `1+beta` differences and its input row is uniformly square summable. It follows that `R_0` is bounded on scalar `C^alpha`, so its range is a closed Banach subspace.

The scalar right inverse `H_b` is correctly normalized: summing `a_r(H_b)_r` gives `(A+P_0^2R_s,2)/D_s,2=1`. Its high output `P_0^2a_r^-/P_r^2` has uniform absolute alias sums after `2+alpha` differences (indeed after `3+beta` for beta below one). Thus arbitrary bounded coarse data map to scalar `C^(2,alpha)` without a refinement factor. The distinction from the scalar extension formed using `G'^2` is mathematically appropriate.

Periodic physical-cell reconstruction and contour shifting apply to the complete operators, with fixed tube and fine-volume normalization. No isolated nonperiodic central term is independently shifted. The zero sector and the degenerate `M=1` case are consistent with the canceled formulas.

## 2. Induced gauge and generator

Direct multiplication confirms `k(U,g)=a(U^g)^-1 g a(U)` at each coarse vertex. Differentiating this expression gives precisely the displayed one-step `T_U`: the logarithm derivative contributes `J_Y^-1`, the endpoint exponential contributes `J_barY`, and the final conjugation is `Ad_(a^-1)`. At the identity the two copies of the root value cancel and only the normalized scalar average remains.

The absolute physical column factor is the fixed one-step ratio `L^d`. The perturbations are `O(h||A||)`, so their product along corrected iterates is controlled by the geometric sum of spacings. This avoids a growing refinement factor. The corrected trajectory is the correct trajectory for this induced gauge; it is not substituted for the ordinary-reference trajectory defining the separate source bond average.

The sign and units of the ordinary gauge generator are correct. A fine gauge `g=e^(is lambda)` gives left link velocity `-i eta D_U lambda`, hence potential velocity `-J_(eta A)^-1 D_U lambda`. The same negative sign occurs at the coarse output, yielding the displayed intertwining identity after cancellation. No physical-spacing factor should be added to the angle parameter lambda.

## 3. Invertible gauge-fixing differential

The map `F_A=G_A-Q_0` has small bounded-field norm. Composing with `H_b:infinity -> C^(2,alpha)` makes `I+H_bF_A` invertible on the scalar regularity space. Applying `Q_0` to its defining equation proves `G_A T_A^s psi=0` whenever `Q_0psi=0`.

The coefficient `(Ad_(exp(i eta A))-I)/eta` has a uniform analytic extension at eta zero and controlled `C^(1,alpha)` norm. The coefficient `J_(eta A)^-1-I` is `O(eta||A||_(C1alpha))`. Ordinary discrete product rules, including fixed shifts, therefore prove `(X_A-D):C^(2,alpha) -> C^(1,alpha)` with norm `O(||A||_(C1alpha))`, without an inverse-spacing loss.

The decisive perturbation can be written explicitly as

`M_A-I = R_0 D^T [(X_A-D) T_A^s T + D(T_A^s-I)T]`

on `ran R_0` in scalar `C^alpha`. Every factor has the asserted uniform Banach-space norm, and both bracket terms have size `O(||A||_(C1alpha))`. The range remains in `ran R_0`, so its Neumann inverse is a genuine inverse on the fixed closed space. This proves both correction identities and the stronger estimate in terms of the residual `R_0D^T v`.

The constrained tangent decomposition follows exactly: the correction is in the kernel of the induced coarse gauge and is therefore tangent to the nonlinear constraint; subtracting it cancels the flat gauge residual. It does not require the gauge projection Pi to be bounded on arbitrary bounded data.

## 4. Flow and genuine orbit coverage

The vector field is uniformly locally Lipschitz in the complete `C^(1,alpha)` potential norm. Along the flow its scalar residual solves the exact equation `r'(t)=-r(t)`. The induced-gauge kernel identity makes the nonlinear constraint derivative exactly zero. The negative sign in the flow is the actual fine gauge velocity, so the Wilson action is constant by gauge invariance.

The speed is at most `C exp(-t)||r(0)||_(C^alpha)`. If the operator domain has radius R and the residual map has norm C_0, an initial radius r with `(1+C C_0)r<R` suffices for global continuation inside that domain. This is a uniform choice. The same argument centered at a slice field uses its zero residual and gives total displacement at most a constant times the distance from that slice field.

The scalar gauge parameter is integrable even in `C^(2,alpha)`. Integrating `g'(t)=i lambda(t)g(t)` produces unitary gauges on every finite regulator. Its integrable supremum norm gives a uniform limiting unitary gauge. The exact relation between the link flow and this gauge then persists at the limit. Thus the limiting slice field lies in the original gauge orbit; equality of action alone is not being substituted for orbit membership.

For sufficiently nearby input fields with the same nonlinear constraint, the limiting slice representative stays inside the strict slice-minimum neighborhood. Its action equals the input action. Strict slice minimality therefore yields local minimality on the full constraint, and equality implies gauge equivalence to the slice minimizer. This proves the claimed local coverage and minimum modulo constraint-preserving gauge transformations.

The stated scope is essential and correctly retained: finite compatible periodic regulators, globally small potential fields, a fixed flat gauge slice, and the fixed-reference corrected nonlinear constraint. No global orbit theorem, arbitrary plaquette-small field claim, topological classification, or infinite-volume total action is used.
