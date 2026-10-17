# Focused audit of the physical stationary background

17 October 2026. Independent cross-check of Section 5 of
`physical_current_pivot_precision_research.md`. This is narrower than an
audit of the complete source precision theorem.

The stationary-background construction passes under the previously proved
ordinary homogeneous minimum and coarse-action gauge-invariance theorems.
No correction was found.

1. Rescaling final spacing \(L\) to one changes the total refinement from
   \(M\) to \(ML\). In dimension four the coupling-free Wilson action is
   unchanged. Potential, derivative and Hölder norm comparisons cost fixed
   powers of \(L\), so the required common comparison radii are independent
   of \(M\) and volume.

2. Exact composition makes \(U_f(W)\) feasible for the current constraint at
   \(V_{\rm part}=\mathcal M^{(k)}U_f(W)\), and makes
   \(U_c(V_{\rm part})\) feasible for the full constraint at \(W\).
   Putting both fields in their respective established comparison balls
   gives the two opposite inequalities and hence equality of the actions.
   The same argument with a general small \(V\) satisfying
   \(\mathcal M_L(V)=W\) proves the required constrained minimum of the
   classical coarse action. No dynamic-programming theorem for arbitrary
   minimizers is being assumed.

3. With the convention \(V^u(b)=u(b_-)V(b)u(b_+)^{-1}\), the choice
   \(u(x)=P_{V_{\rm part}}(y,x)\), \(u(y)=1\), gives
   \(P_{V^u}(y,x)=1\). It fixes every block center and therefore preserves
   the ordinary next-coarse datum. The fixed-\(L\) local gauge has size
   \(O_L(\|\log V_{\rm part}\|_\infty)\).

4. Its blockwise current-site oscillation does not by itself supply a
   smooth original-fine gauge. The cited coarse-action invariance theorem
   supplies that missing step through its smooth fine point-interpolation
   lift. That result is exactly what is needed here. After shrinking the
   input radius, both \(V_{\rm part}\) and \(V_*\) remain in the same
   coarse comparison ball.

5. Real constrained stationarity follows from the actual minimum
   comparison. The constraints, the averaged-contour gauge identity and
   the vanishing pulled-back first derivative are holomorphic expressions
   on the stated uniform complex neighborhood. Their vanishing on the
   real open ball extends by the finite-dimensional identity theorem on
   each regulator. This asserts analytic identities, not complex
   minimality.

The subsequent uniqueness claim additionally uses the reduced-Hessian
estimate on an entire fixed pivot-coordinate ball, as explicitly supplied
in Section 7. A positive Hessian only at one point would not suffice for
its uniform version. The written note makes the stronger neighborhood
estimate, so the dependency is correctly exposed.

The source cutoff issue is recorded separately in
`pivot_cutoff_source_research.md`: the readable CMP116 integration uses
retained-bond windows, whereas any genuinely additional pivot indicators
must keep their exact pullback.
