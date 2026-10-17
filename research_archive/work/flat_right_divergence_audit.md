# Independent audit of the Hölder right-divergence estimates

16 October 2026. Independently examined the massive-subtraction approach before the note was saved, then read all six sections of `flat_right_divergence_research.md`. **Pass. No mathematical correction found.** The theorem is homogeneous, has input exponent gamma strictly greater than output exponent beta, and retains the bounded-current assumptions and source scope of the previous flat results.

## 1. Massive subtraction and the smooth remainder

Subtracting the genuine full-lattice comparison G_m=(L+1)^-1 removes the sole order-minus-two full-rank diagonal. In the high aliases, the difference is exactly

    1/P_r-1/(P_r+1)
       =integral_0^infinity (1-exp(-t)) exp(-tP_r) dt.

The extra factor is O(t) at small time. One input derivative, one output derivative, and an output beta-Hölder increment therefore give the integrable bound t^(-beta/2), which is more than sufficient for beta<1. Large times retain the established high-alias gap. The central subtraction is bounded and holomorphic after a uniform strip shrinking: P_0+1 is positive on the real chart and all relevant derivatives are uniformly bounded.

In the finite-rank terms, differentiating the input row once multiplies its high omega/P vector by O(|r|), leaving O(omega/|r|), and its beta-update row by the analogous factor, leaving O(a/|r|^2+omega/|r|). These rows are uniformly in alias l2. The output C^(1,beta) vectors are those already absolutely summed in the pointwise baseline theorem. Thus the argument really bounds R_m D* on arbitrary bounded data, with no derivative of the input and no growing cell-dimension factor. The completed operator is periodic; the separated chart pieces need not be. Gluing and contour shifting are used only for the completed remainder, as required.

## 2. Weighted heat moments above and below the mesh scale

The probability-kernel convention is consistent with physical-volume integration: converting probabilities to kernel densities cancels the fine volume in each absolute operator-row sum.

For eta^2<=t<=1, the exponential scale delta=kappa+t^-1/2 has lattice parameter eta delta bounded by a fixed constant. The elementary weighted variation estimate consequently has uniform constants, and its exponential cost is bounded by exp(C delta^2 t). Semigroup splitting into k equal pieces preserves this estimate with constants depending only on the fixed derivative order k. Multiplying by |v|^gamma is paid by t^(gamma/2) exp(|v|/sqrt(t)), exactly converting weight kappa to delta. This yields the required t^((gamma-k)/2) moment bound.

For t<eta^2, the fixed finite shift expansion has coefficient eta^-k. The dimensionless random walk has time less than one and uniformly bounded moments, including all the required shifted gamma moments and the bounded exponential tilt. Its physical moment contributes eta^gamma. Since k>gamma,

    eta^(gamma-k)<=t^((gamma-k)/2).

The inequality direction is correct. No continuum approximation at times below the mesh is assumed. At large time, a small fixed additional exponential weight absorbs the polynomial moment and keeps the heat growth below exp(t/2); the massive exp(-t) factor then supplies the integrable tail. The same reasoning handles the lower derivative members.

## 3. Cancellation and the Hölder loss

Every full-lattice derivative row sums to zero. Subtracting lambda(x) is therefore exact and occurs before the weighted estimate. The complete-field local Hölder norm gives the global increment bound in (4.2): nearby points use one enlarged collar, and distant points use weighted sup norms plus the bounded ratio between coarse-cell and physical-distance weights. No derivative of the spatial weight is taken.

The weighted gamma moments then give the second- and third-derivative estimates in (4.3). For the difference of the second-derivative output, the two valid bounds are its sup bound and the physical displacement times its first-difference bound. Telescoping along a fine lattice path inside a fixed enlarged collar preserves the weights up to a fixed factor. Interpolating gives

    [D^2 exp(-tL)lambda]_beta
       <=C t^(-1+(gamma-beta)/2)||lambda||_gamma.

The integral is exactly 2/(gamma-beta). The beta=0 convention is harmless. There is no claim of a uniform estimate as gamma decreases to beta. With gamma=beta+epsilon and beta<=beta_0<1, epsilon can be fixed so the whole input-exponent interval stays strictly below one and all constants are uniform in beta.

The field member of G_mD* uses only the integrable first heat derivative on bounded data. Its first-gradient and Hölder members use the cancellation just checked. Thus the resulting estimate is precisely the required N_beta bound. Periodic extension or direct periodization retains the derivative-row cancellation and the weight comparison with cover distance, including small tori and their multiplicities.

## 4. Transfer to the actual current inverses

The baseline decomposition G_0D*=G_mD*+R_mD* establishes the right-divergence datum in N and N_beta. The already audited K_J:N->N_beta contraction then applies unchanged to this datum. Its norm and hence the current radius depend on the current perturbation bound, not on the size of the new Hölder forcing constant. Fixing a smaller common spatial exponent if needed does not create a new refinement-dependent coupling restriction.

All later Neumann terms are controlled by the N contraction and one outside N->N_beta estimate. This proves the actual auxiliary and full current bounds, with holomorphic current dependence, without differentiating J. At each fixed refinement D*lambda is an actual bounded forcing for bounded Hölder lambda; the new argument improves its estimate uniformly rather than changing the operator being inverted.

## 5. Localization and source limits

The proof works on complete weighted Hölder fields. Localization uses smooth physical cutoffs with controlled first derivatives, whose sampled values have uniform Hölder product bounds. Sharp cell indicators would produce artificial eta^-gamma jumps and are correctly excluded. Output cutoff factors are likewise controlled by the ordinary Hölder product inequality on the fixed collars.

The result supplies the homogeneous flat source right-divergence members with input exponent beta+epsilon. It adds neither a current Laplacian estimate nor an endpoint gamma=beta theorem. Nonflat coefficients, retained-history geometries, and strict support-dependent walk expansions remain separate. Within these limits, the right-divergence obligation that was left open in the bounded-forcing pointwise note is now discharged.

## 6. Added constrained-current (J6) corollary

The subsequently added final section of `flat_right_divergence_fragment.tex` also passes. Raw I 13735 defines precisely tilde G^J=(I-tilde G_0 Theta_J)^(-1)tilde G_0; at the flat homogeneous normalization the passed earlier work identifies tilde G_0 with Gamma=G_0-H_src q_aux^(-1)H_src^*. The already proved Gamma:L-infinity->N_beta bound B_Gamma includes its supremum bound. Thus the n-th Neumann term has N_beta norm at most B_Gamma(B_Gamma tau_infinity C_v ||J||)^n||f||_infinity, with the same weighted norms. The stated common radius makes this geometric series bounded by 2B_Gamma. Every term starts on the left with Gamma, so Q Gamma=0 gives the claimed exact constraint, including after passage to the norm-convergent series. Analyticity and weighted locality follow from that same convergence. No additional derivative of J is required. The distinct scalar G' right-divergence obligation is correctly left separate.
