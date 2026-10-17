# Independent audit of the composite macrostep Gaussian

17 October 2026. Audit of `composite_macrostep_gaussian_research.md`. Result: full pass at fixed R, uniformly in prior depth M and compatible periodic volume.

The angle derivative C_R is not divided by R. Its pivot coefficient is R^(1-d), its gradient output is the coarse endpoint difference, and K_R=(I-h_R C_R)E_f exactly parametrizes ker C_R while retaining every free coordinate. These agree with the separate nonlinear geometry proof. The stated primitive Schur bound is conservative and composes in counting angle spaces; it does not introduce an old-fine M factor.

The local patch matrix is genuinely positive: curl zero on the rectangular lifted patch implies a gradient; every internal contour row then reads the difference from its R-block center, so T_R=0 makes that scalar constant on each block; C_R=0 identifies adjacent block constants. The scalar is constant on the connected patch and the bond field vanishes. The only use of locality is to make each constraint row a legitimate patch row and to apply the gradient identity without a global extension assumption.

The translated-patch multiplicities are at most 3^d for plaquettes, contour rows and coarse rows; every bond appears. Periodic pullbacks preserve distinct occurrences in the local array. Summing over periodic patch centers therefore gives the same multiplicities even when a 3-block patch wraps around a two-block period. The separate geometry requirement distinguishing the opposite interfaces is correctly retained.

Combining this with q_M>=d_1^T d_1 yields gamma_R=sigma_R/3^d on ker C_R. Since ||K_R z||>=||z||, the retained lower precision is gamma_R; its upper bound gains the finite ||K_R||^2. At flatness both action and absolute-gauge gradients vanish, so no chart-curvature term is omitted. The retained dimension d(R^d-1) dim(g) and covariance A^-1 in current counting coordinates are correct.

The exponential inverse does not rely on the gap alone. The weighted q_M estimate and fixed-range K_R,T_R supply a weighted precision bound. For t<=alpha_R/2, the conjugation error is at most 2t A_R^*/(e alpha_R) in both row and column norms. The stated choice of t makes this at most gamma_R/2, giving the 2/gamma_R pointwise block bound. A smaller exponent makes it summable. Truncated distance weights justify the infinite-lattice argument, and shortest representatives bound periodic sums.

The nonflat extension retains both ordinary-log and constraint-chart curvature terms and the absolute gauge Hessian. Supremum bounds on the current classical gradient are contracted against finite-range second-derivative rows, so no volume factor is hidden. It is an analytic precision comparison, not a proof of centering or strict background support by itself.

No mathematical correction is requested. The cumulative gauge relation in Section 2.3 is not needed for the patch proof; its angle normalization is consistent with C_R=R Q_R^st-partial_R beta_R.
