# Independent audit of the fixed-ratio Gaussian scaling and reduced Hessian

17 October 2026. Audited `work/one_step_gaussian_scaling_fragment.tex`. Mathematical result: pass. One notation correction was sent to the author before any edit: in the unit-retained-scale nonflat subsection, W(A_*) uses `Df_(1/L)`, not `Df_eta`, because the symbol eta there otherwise still denotes the original physical spacing.

## 1. Exact physical/counting conversion

For h=L eta, y=x/h and A_s=h A_phys, the physical first difference is h^(-2) times the 1/L-mesh difference of A_s. The equality of the d4 Maxwell actions is exact. The full Wilson action is unchanged because the link matrices and combinatorial plaquettes are unchanged under the relabeling.

The constrained scalar projection and linear homogeneous constraints transform to their fixed-L counterparts. The physical precision coordinate matrix is h^(-2) K_L and its variational inverse h^2 C_L. Multiplying by eta^(-4) to obtain the counting covariance, and by h^2 again to rescale the random potential, gives Cov_count(Z_s)=L^4 C_L exactly.

Thus the dimensionless field pair is `(Z_s/L, nabla_* Z_s/L^2)` and its covariance is `S_L C_L S_L^T`, with S_L understood as the stacked map `(L I; nabla_*)`. The fixed-L factor in the potential row is necessary; there is no remaining power of physical h. The previously proved value and derivative sandwiches bound the full positive block covariance, including its cross terms, uniformly in volume. The result is a fixed-ratio statement, not a refinement-uniform value bound when L is replaced by a growing total ratio M.

## 2. Reduced Hessian and the nonlinear constraint term

The displayed reduced form includes both ambient Wilson terms and the second derivative of the nonlinear constraint chart. In particular `-<m,D2F[v,u]>` is present with the correct sign and physical pairing. It follows from the exact chart second derivative and H_A^T E=m; omitting it would give a different Gaussian precision.

For complex background fields, `v=z-H DR(A_*)v` and the physical L2 smallness of DR imply uniform L2 and first-difference bounds in terms of the flat energy norm of z. These estimates do not use positivity of the complex background Hessian and therefore genuinely hold on the common complex ball.

The flat mixed terms vanish because H^T K z=0 for z in X_L. The remaining difference of Maxwell bilinear forms is exactly `<DR v,q DR u>`, of order b^2 relative to the two fixed flat energy norms. The Wilson coefficient term is order b, and the genuinely two-Hilbert-direction constraint Hessian estimate bounds the multiplier term by order b. These estimates prove the claimed bounded bilinear perturbation after conjugation by the fixed K_X inverse square root.

The resulting E_B is complex symmetric, has Hermitian operator norm O(b), and is holomorphic because the finite-dimensional reduced action and chart are holomorphic. The fixed square root is real positive; it is not a background-dependent branch. This distinction makes the relative quadratic hypothesis suitable for the separate complex Gaussian theorem.

## 3. Real comparison and tangent fluctuations

At real B, the relative bound gives `(1-epsilon)K_X <= B_B <= (1+epsilon)K_X`, so the inverse covariance comparison has exactly the displayed reversed constants. The chart-coordinate dimensionless covariance is therefore bounded by K_L/(1-epsilon).

For the linearized potential fluctuation T_A zeta, the bounded map `S_L T_A J_X K_X^(-1/2)` follows from the energy estimate. Inserting `(I+E_B)^(-1)` between this map and its transpose proves the claimed real covariance bound. The fine inclusions and physical/counting factors are consistent with the chart-coordinate calculation.

At a complex background the resulting normalized Gaussian is a complex functional. Fixed real-coordinate tests are admissible in the marginal theorem; moving complex tests inside an indicator need separate justification. The fragment correctly retains this boundary.

## 4. Domain and source limits

At the fixed mesh 1/L, the bounded-coordinate norm controls first differences and their sampled Hölder seminorms with constants depending on L and alpha. A global bound on all dimensionless value tests therefore controls the chart-coordinate N_alpha norm by C_(L,alpha) gR. For a selected subcollection of good blocks only the corresponding local collar norm is controlled; a global norm requires the covering collection. The fragment's following paragraph explicitly distinguishes the event that every cell is good from the joint bad-cell estimates needed on large volumes.

Choosing gR small is compatible with thresholds `(log(1/g))^p`, and gR^3 also tends to zero. These facts specify an admissible local Gaussian chart regime; they do not integrate a remainder or establish high probability of the global all-good event.

The application audited here is the first bare homogeneous Wilson step and its derived reduced Hessian. A later effective renormalization step can carry a different Maxwell precision and separate current terms. Those must be matched independently rather than replaced by the bare fixed-L form. Haar/Jacobian factors, nonlinear interactions, bad regions, and that later source identification remain outside this audit.
