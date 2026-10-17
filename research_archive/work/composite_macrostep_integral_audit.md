# Independent audit of the composite macrostep integral

17 October 2026. Read-only mathematical audit of `composite_macrostep_integral_research.md`, especially Sections 2--4 and 6. Result: the stated finite-regulator identities pass, with the scope and separate inputs retained in that note. This is an internal audit, not external certification.

## 1. Global completion and gauge insertion

The normalized-tuple completion preserves the selected local source mean. For endpoint transformation U_j -> g U_j h^-1 and T=U_1, every U_j T^-1 is conjugated by g. The good set is invariant, its analytic formula transforms by g on the left and h^-1 on the right, and the fallback T has that same covariance. Compact unitary conjugation preserves the chosen logarithm neighborhood. The analogous completion of the ordinary map, followed by composition, therefore has exact root-fixed gauge invariance. No equality with a prescribed different large-field completion follows.

For u(y)=1 at R-centers, each contour variable is P(V;y,x)u(x)^-1. The product Haar integral factors into exactly n_s copies of c(g). This justifies the insertion with c(g)^(-n_s), including on arbitrary real link fields after the stated completion. A noninvariant sector is introduced afterward; the note correctly retains the complementary sector and does not apply the identity separately to a nongauge-invariant window.

## 2. Physical branch and domains

The two minimum comparisons use exact primitive composition. The full-refinement minimizer is feasible for the current constrained problem, and the current minimizer with datum V is feasible for the full composite problem whenever F_R(V)=W. Their minimum classes can be matched by a fixed-R shrink: converting physical potential and Holder bounds introduces fixed powers of R, not old-depth M factors. The existing minimum theorem is among all sufficiently small global fields, which is essential here.

The contour gauge preserves F_R, makes every P_R equal to identity and preserves S_M on the common gauge-invariance domain. Hence it gives a minimum of S_M+G_R. Positive reduced Hessian, supplied by the separate Gaussian proof, then identifies the local stationary branch. Stationarity alone is not used to infer gauge zero. Complex continuation concerns identities and criticality, not a complex minimum.

## 3. Density normalization

The powers of h_0 are correct: one per current group link and one inverse per constrained coarse group link. The group delta in relative logarithmic coordinates samples j(F) at zero, so no nonconstant coarse Haar density remains. Right translation by the background preserves current-link Haar measure.

The square ambient straightening satisfies F(psi(B))=A B and retains all nonpivot coordinates. Its pivot derivative block is diagonal by the exact nonlinear incidence. Differentiating the constraint gives det Dpsi = product det A_p / det D_pF(psi(B)); integration of delta(A B) contributes product det A_p^-1. Thus the unrearranged factor is precisely product det D_pF(Phi(z))^-1. There is no rectangular determinant of DPhi.

After z=g xi, the factor is g^[q(n_e-n_c)]. The normalized Gaussian convention contributes (2pi)^[q(n_e-n_c)/2] det A^-1/2. The nonlinear chart is evaluated at g xi everywhere. Gauge and action linear terms vanish at the identified physical branch; their full quadratic term is the stated A. Background-dependent pivot and Gaussian determinants are correctly not classified as vacuum constants.

## 4. Pre-gauge extension

The link identity follows directly from Vstar=u_- Vp u_+^-1 and exp(i Ad_(u_-^-1)X)=u_-^-1 exp(iX)u_-. It changes no xi integration variable and hence introduces neither an adjoint Jacobian nor a transformed cutoff. The pre-gauge value is an actual old-domain evaluation; outside the original rooted domain it continues only the common germ. A logarithmic identity requires a compatible nonvanishing logarithm branch, as explicitly assumed.

The bounds C_a b/R+C_R gT and the lambda disk are uniform in old depth and volume at fixed R. Uniform complex nonvanishing does not follow from finite-cutoff holomorphy; the note correctly leaves it to the cluster theorem. Its initially separate actual joint-support input is now supplied by `composite_macrostep_joint_family_research.md`, audited separately.

No mathematical correction is requested.
