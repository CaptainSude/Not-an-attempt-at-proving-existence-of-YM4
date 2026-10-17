# Independent audit: physical current-step pivot precision

17 October 2026. Audited work/physical_current_pivot_precision_research.md, including the added fixed-chart convexity estimate (7.2a) and exact gauge simplification (4.4). The candidate was not edited by this auditor. This is an internal mathematical and source-scope audit, not external certification.

## Result

The construction passes on its stated homogeneous periodic small-global-potential branch. It supplies the actual current-scale retained-coordinate Hessian at a physical stationary background, including both chain-rule curvature terms, and an analytic weighted neighborhood of its covariance. It does not establish independent-free-current extensions, arbitrary source orbit domains, mixed histories, or a strictly local background decomposition of the precision.

Two clarifications were requested and adopted or communicated:

1. Positivity at one stationary point alone did not justify agreement with every critical field in a fixed common neighborhood. The added (7.2a) proves uniform convexity on one fixed retained-coordinate chart ball and resolves this.
2. To apply Notebook18's stated covariance-closeness theorem directly, convert the precision perturbation to covariance closeness. The existing Neumann estimate does this; an explicit sufficient inequality is recorded below.

## 1. The exact local chart and normalization

The pivot geometry used in the candidate is the source's next-step geometry, with distinct block interfaces. Every root-to-site contour is internal to one block. A current bond crossing the chosen interface belongs only to the corresponding parallel-string/reference-string coarse equation. Thus the entire nonlinear equation F_c sees its own pivot and no other pivot; this is stronger than diagonalization merely at the trivial background.

At flatness exactly L translated strings contain the pivot. The coefficient in Q_flat is L^{-d}; with the source kernel convention

\[
 Q^\flat B(c)=L^{-d}\sum_b Q^\flat(c,b)B(b)
\]

its pivot kernel is I. Since F'_V=LQ^\flat_V, its actual pivot coefficient is L^{1-d}pi_c. Therefore

\[
 h_V(c)=L^{d-1}\pi_c^{-1},\qquad F'_Vh_V=I,
\]

and

\[
 (K_Vz)(p(c))=-\pi_c^{-1}
             \sum_{b\ {\rm retained}}Q^\flat_V(c,b)z(b)
\]

has exactly the correct normalization. There is no missing L factor.

The equation

\[
 \widetilde D_V(B)=C_V(B-h_V\widetilde D_V(B))
\]

decouples between coarse output equations. Each unknown component changes only its own pivot, which no other equation reads. Its analytic implicit solution consequently remains in a fixed two-block neighborhood; iterating it does not spread support.

The resulting chart

\[
 \Phi_V(z)=K_Vz-h_V\widetilde D_V(K_Vz)
\]

solves the actual nonlinear ordinary constraint and is the identity on every retained coordinate. Uniqueness of the small pivot solution identifies it with the source chart, rather than only with some parametrization of the same fiber.

Its first two derivatives are

\[
 D\Phi_V(0)=K_V,\qquad
 D^2\Phi_V(0)[u,v]
  =-h_VD^2F_V(0)[K_Vu,K_Vv].
\]

With C_V^(2) denoting the degree-two bilinear coefficient, this is -2h_V C_V^(2). The sign and factor are correct.

The fixed number of inputs per local equation and equations per input supplies the claimed weighted row/column bounds. Contracting a local second derivative against a bounded current has only this fixed incidence cost, not a volume factor.

## 2. The absolute exponential gauge function

The candidate uses the actual absolute averaged-contour penalty, analytically continued with P+P^{-1}, not a penalty silently centered at an arbitrary background. On its source slice P_V=I, its first derivative vanishes and its Hessian is T_V^T T_V. The normalized trace expansion has coefficient one half, so this is the precision contribution after taking the second derivative.

The further simplification (4.4) is exact. Internal contour functions do not read interblock pivots, whereas all nonlinear chart corrections are pivot-supported. Hence

\[
 \mathcal G(e^{i\Phi_V(z)}V)=
                 \mathcal G(e^{iE_{\rm free}z}V),\qquad T_Vh_V=0.
\]

The gauge factor is therefore local in the unchanged retained coordinates. At arbitrary nearby backgrounds its Hessian may still have a residual from the nonlinear contour map because the absolute gauge gradient need not vanish. The candidate correctly retains that residual. The particular formal term involving the gauge gradient times D²Phi vanishes because it points only along pivots.

## 3. The physical stationary background

The two local minimum comparisons in Section5 are valid with uniform margins:

* The full ordinary minimizer U_f(W) is feasible for the current problem at V_part=M^k(U_f(W)), giving S_M(V_part)<=S(U_f(W)).
* The current ordinary minimizer U_c(V_part) is feasible for the full problem by exact composition of the same ordinary averaging operation, giving the reverse inequality.
* For any sufficiently small current V with M_L(V)=W, the same U_c(V) is a full feasible competitor. Thus V_part is a local constrained minimum of the current classical action.

Only a finite number of bounds relating the current and final-spacing-L comparison balls is used. L is fixed; the already proved minimizer bounds are uniform in the earlier depth M. One can choose the current comparison radius first and then the smaller next-coarse data radius, independently of M and volume. This does not assume a dynamic-programming identity for arbitrary minimizers.

The rooted gauge u(x)=P_Vpart(y,x), u(y)=I, has the correct order under the candidate's convention V^u=u_-Vu_+^{-1}:

\[
 P_{V^u}(y,x)=u(y)P_V(y,x)u(x)^{-1}=I.
\]

The ordinary coarse constraint is unchanged because the gauge is identity at block centers. The prior local gauge invariance theorem for S_M applies after shrinking the same uniform margins; it includes the smooth fine extension needed for the comparison of underlying Wilson actions. This establishes the physical gauge-zero stationary family.

The proof uses real minima only. Its uniform analytic maps and real identities extend to a complex neighborhood by finite-dimensional holomorphic uniqueness. It does not call a complex configuration a minimum.

The added (7.2a) repairs the only initial uniqueness gap. On a fixed Phi_V chart, all derivatives at z obey

\[
 D\Phi_V(z)=K_L+O(\|a\|_\infty+\|z\|_\infty),\qquad
 \|a_V(z)\|_\infty\le C_L(\|a\|_\infty+\|z\|_\infty).
\]

The classical Hessian and current bounds, plus local second chart derivatives and the actual gauge function, give

\[
 \|D_z^2(S_M(a_V(z))+\mathcal G(e^{i\Phi_V(z)}V))
                      -A_{M,0}\|_\kappa
 \le C_{L,\kappa}(\|a\|_\infty+\|z\|_\infty).
\]

The real Hessian is uniformly positive throughout a fixed convex z-ball. Any sufficiently small field on the same fiber is in this chart, by the unique pivot solution. Therefore there is at most one critical field there. The claim remains confined to this common small neighborhood.

## 4. Both action curvature terms and the physical current

The conversion from source left-relative coordinates to ordinary potential coordinates is

\[
 \Xi_a(B)=i^{-1}\log(e^{iB}e^{ia}),\qquad
 D\Xi_a(0)=\mathcal J_a^{-1},
\]

where

\[
 \mathcal J_a X=\int_0^1\operatorname{Ad}(e^{ita})X\,dt.
\]

This normalization follows by differentiating the exponential and right multiplying by e^{-ia}. It has no spacing factor at current unit scale. Analyticity and Xi_0(B)=B give D²Xi_a(0)=O(||a||).

Consequently

\[
 D^2a_V(0)[u,v]
 =\mathcal J_a^{-1}D^2\Phi_V(0)[u,v]
   +D^2\Xi_a(0)[K_Vu,K_Vv].
\]

The pulled-back action Hessian is exactly its ordinary Hessian contracted with the two tangent derivatives plus the ordinary gradient contracted with this whole second derivative. Both the nonlinear-constraint curvature and the change-of-exponential-coordinate curvature are retained.

Writing j_rel=J_a^{-T}m_M(a), the constraint term is

\[
 -2\langle j_{\rm rel},
                 h_V C_V^{(2)}(K_Vu,K_Vv)\rangle.
\]

This matches the source vertex's sign and factor. Its current is the derivative of this same classical action, not an independently assigned field.

Stationarity only gives K_V^T j_rel=0. Since I-h_V A_V maps into ker A_V, it follows that j_rel=A_V^T h_V^T j_rel. This identity does not kill the displayed curvature term. The note correctly does not confuse stationary restriction with a vanishing ambient gradient.

## 5. Precision, covariance and the exact remaining interface

The preceding local row/column bounds and Notebook16's estimates

\[
 \|m_M(a)\|_\infty\le C\|a\|_\infty,\qquad
 \|D^2S_M(a)-q_M\|_\kappa\le C_\kappa\|a\|_\infty
\]

give

\[
 \|A_M(V)-A_{M,0}\|_\kappa\le C_{L,\kappa}\|a\|_\infty.
\]

This uses the extensive gradient only through its uniform supremum and fixed local Hessian incidence. It is uniform in prior depth M and volume. Symmetry is bilinear, while the lower bound at complex arguments is correctly a Hermitian numerical-range bound against the real positive baseline.

The candidate's spectral and weighted Neumann inequalities follow. For a direct application of Notebook18's covariance-closeness version, write C_0=A_{M,0}^{-1}. Its minimum eigenvalue is at least 1/B_*. The existing estimate

\[
 \|A_M(V)^{-1}-C_0\|\le2C_*^2 C_{L,\kappa}\|a\|_\infty
\]

therefore meets that theorem's theta-budget whenever

\[
 2C_*^2 C_{L,\kappa}\|a\|_\infty\le\theta/(2B_*).
\]

Alternatively, a relative precision perturbation of norm epsilon gives a relative covariance perturbation of norm at most epsilon/(1-epsilon). Thus there is no mathematical obstruction to the tuned marked Gaussian neighborhood; the parameter conversion must be stated with the theorem's covariance convention.

This is not a strictly local decomposition of A_M(V) in background variables. Weighted decay of a fluctuation kernel and local dependence of K_V,h_V,T_V do not make the classical Hessian H_M(a) read only a finite background support. Nor does restriction to the physical stationary family give a product domain of independent free currents.

## 6. Primary source and cutoff scope

I independently read the primary [CMP109 article](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf), pp.253--255 and265--268. Its averaged contours, ordinary average, absolute gauge penalty, pivot-only straightening, and covariance reduction agree with the candidate. The text following (2.9) explains the resulting bounds on eliminated pivot variables. The exact product subscript in (2.9) is not legible in the accessible OCR.

The primary [CMP116 article](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-4penm4k7hc.pdf), p.12, defines the bond set with the pivots deleted immediately before its cutoff decomposition (2.3). This supports the retained-coordinate product used here.

Because Phi_V(gz)=gz on retained links, that rectangular cutoff argument is preserved exactly. Any additional pivot, contour or reconstructed-field indicator must retain its exact pullback. The candidate explicitly does so; it does not identify such extra indicators with the retained rectangle. RawII's less precise all-bonds wording must not override this distinction.

## Final scope

Promotable as an internally audited finite-regulator theorem on the stated homogeneous small-global-potential branch, with the adopted uniform-convexity clarification. It identifies the physical source chart and Gaussian quadratic part within that branch. The independent-current extension, source orbit domains on arbitrary polymers, strict background-supported precision activities, all interaction coefficients, mixed-history boundaries and quantum iteration remain separate.
