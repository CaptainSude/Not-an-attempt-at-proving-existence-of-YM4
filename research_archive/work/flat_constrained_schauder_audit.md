# Independent audit of the constrained equal-exponent Green bound

16 October 2026. Full audit of `flat_constrained_schauder_research.md`. All sections pass; no mathematical correction found. This supplies the equal-exponent Green hypothesis in the nonlinear fixed-gauge minimizer module, within the homogeneous flat setting and the already matched source conventions.

## Exact algebra

The identities `LZL=R`, `ZL²Z=Z` and `G0 Lambda^T=DZ` check directly. For the last one, `A0 DZ=D R LZ=D LZ=Lambda^T`, while the averaging term vanishes by Q0 Z=0. The source-gauge condition on H removes the H subtraction in Gamma Lambda^T. Consequently expansion of Pi Gamma Pi^T leaves exactly Gamma-DZD^T, with one subtraction.

The cochain identity QD=D_c Q0 gives QPi=Q. Also `R D^T Pi=R D^T-RLZLD^T=0`. The two constraints on C and their transposes follow. On the fixed slice, A0 xi=Kxi and D^TK=0, hence C Kxi=xi. The relation `KH=Q^T(q_aux-a_pen)` gives C K H=0. Positivity and symmetry on finite real regulators identify C with the variational inverse on the constrained slice, as claimed.

## Gamma with a differentiated datum

The exact transpose identity in (3.4) moves the input divergence onto H in the subtraction. The already established C1alpha kernel of H, its first-derivative transpose, the coarse exponentially summable q_aux inverse, and physical fine-cell volume one give the claimed bounded-input estimate with no M-dimensional factor. Combining this with the separately audited equal-exponent G0 divergence theorem proves the Gamma assertion. The proof uses complete input fields where their Hölder norm is required.

## The smoother scalar remainder

The canceled aliases in (4.2) agree with the constrained inverse of L²: the central entry is R_s2/D_s2 and the high rank coefficient is P0²/(D_s2). Subtracting the massive diagonal `(P_r+1)^{-2}` gives precisely the heat factor `t(1-e^{-t})`. For D(Z-Z_m)D^T nabla^T the maximum output-Hölder heat order is 4+alpha, so the small-time row integrand is bounded by t^{-alpha/2}; it is integrable. High-mode large times are uniformly gapped, and the removed central mode has bounded small-time derivatives in cell coordinates.

The rank output vectors acquire at most 2+alpha alias powers. Their weighted product decay is `prod(1+|r_nu|)^{-1}(1+|r|)^{-2+alpha}`, whose dyadic shell sum is uniformly finite. Two input derivatives leave an l2 alias row bounded by `|a_s|/(1+|s|)^2`. The physical-cell reconstruction converts this to bounded-input estimates without a fine dimension loss. Only the complete reconstructed operator is periodically glued; the note correctly avoids claiming that each central chart piece is periodic by itself.

## Massive biharmonic cancellation

The derivative moments (5.3) are valid both above and below the mesh time. Above eta², semigroup splitting into a fixed number of factors, the first-difference variation estimate, and the exponential scale kappa+t^{-1/2} yield the derivative factor t^{-k/2}; the polynomial moment contributes t^{alpha/2}. Below eta², the finite shift expansion bounds the moment by eta^{alpha-k}, which is at most t^{(alpha-k)/2} since k>alpha. This checks the direction of the sub-mesh inequality.

Every positive derivative kernel has zero row sum. Thus subtracting f(x) yields the required alpha-moment instead of differentiating f. For the output gradient, the fourth and fifth derivatives multiplied by the biharmonic time factor have exponents -1+alpha/2 and -3/2+alpha/2. Splitting at the square of the output separation gives respectively `(2/alpha) r^alpha` and at most `(2/(1-alpha))r^alpha`; the massive long-time contribution is Lipschitz and therefore also alpha-Hölder. The argument takes the separation-dependent split before the Hölder supremum and has no logarithmic endpoint loss for 0<alpha<1.

The undifferentiated datum needs only bounded norm: the maximum heat order is 3+alpha, and `t*t^{-(3+alpha)/2}` is integrable exactly in the stated alpha<1 range. This supplies C:L∞ to N_alpha as well as C S_jet^T:C^alpha to N_alpha.

## Weights, finite volume and identities on complete fields

The weighted difference inequality (5.4) follows from the local collar Hölder estimate for short displacements and the admissible weight ratio plus bounded norm for long displacements. The path used in the output difference stays in a fixed enlarged collar. There is no differentiation of a weight or sharp partition in the Hölder part. A small fixed exponential moment leaves mass-decay slack for the large-time integral.

The remainder and extension pieces have exact periodic Bloch reconstruction and exponential cell locality; the massive part has full-lattice heat cancellation and exact periodic restriction. Thus compatible small tori are covered with multiplicities. The fixed-mesh algebra extends to complete bounded or admissibly weighted fields through absolutely convergent cell kernels; allowing fixed-mesh norm-equivalence constants for this identity step does not damage the separate uniform estimates.

The theorem proves precisely the constrained homogeneous flat Green module needed by the minimizer proof. It does not establish a moving-background Schauder theorem or a retained-domain result, and it makes no alpha=0 or alpha=1 claim.
