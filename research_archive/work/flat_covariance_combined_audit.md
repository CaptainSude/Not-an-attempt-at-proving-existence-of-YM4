# Audit of the combined flat-locality draft and refinement limit

16 October 2026. Independent audit by the theorem-audit agent. No output files or repository files were edited. The conclusions below are internal mathematical checks, not external certification of a Yang--Mills construction.

## 1. Combined locality candidate

Read `work/ym4-flat-locality-candidate.tex` in full, against `flat_covariance_decay_research.md`, its independent rotation audit, and the relevant deposited source passages. No mathematical correction was found in the combined main proof.

The alias covariance has the correct physical-volume normalization: the fiber energy sums aliases with coefficient one, and the one-form multiplier includes both its centered block factor and the extra longitudinal factor. The gauge quotient has the correct minus sign and removes the coarse gauge direction; treating the blocked Feynman inverse alone as Maxwell precision would be incorrect, but the draft does not do that. The zero coarse mode is handled separately by the constant fine field.

The factorization `sum b_mu/D_mu=P_0 E` and the canceled expression are exact. The enlarged real cube, uniform high-alias gap, alias Parseval estimate, first shrinking for `A,g,D`, and second shrinking for `E` are in the correct logical order. Their domains retain a real margin, so Cauchy estimates do not cross uncontrolled Brillouin boundaries. The analytic charts glue because the real quotient is periodic by alias permutation. No complex massless denominator remains in the final precision symbol.

The fixed-L insertion is finite range, and grouping unit-lattice coefficients into fixed blocks preserves a weighted exponential row sum with constants independent of refinement. Combining that additional spatial estimate with the real gap justifies the inverse-symbol strip. The finite-period covariance is the periodization of the infinite inverse kernel, equivalently the sample of the inverse Bloch symbol; it is not inferred by truncating an infinite covariance. The small-period statement uses periodic oriented-cell multiplicities consistently.

### Exact source-coordinate check

Raw I, lines 46977--46986, states

    L Qflat B=Phi_1^flat(V;B),
    (Qflat B)(c)=sum_b L^(-d) Qflat(V;c,b) B(b),
    C_flat(b0(c),b)=-pi_c^(-1) Qflat(V;c,b).

At flatness the pivot kernel is the identity, while the discrete matrix coefficient of `S_L=Qflat` is `L^(-d)` times that kernel. Therefore the actual insertion on free columns is exactly

    K_pivot=-L^d (S_L)_free.

There is no missing power of `L` or hidden nonlocal inverse in this map. Raw I 47568--47569 gives the reduced form as

    C_flat^T(P_Lambda T_1^(-1)P_Lambda-a+J[current]+G)C_flat.

On the homogeneous full domain at zero current, this is the action part `T_1^(-1)-a` plus the gauge form. The draft's conditional physical variational identification turns that action part into `q_M`, and the gauge derivative is `T_L^*T_L`. This justifies the stated source formula under the previously retained smooth-minimizer and coordinate match. It does not identify arbitrary retained-domain restrictions or arbitrary independent-current extensions with the homogeneous model.

The auxiliary identity `H_1^*Delta_1 H_1=(QG_1Q^*)^(-1)-a` is algebraically consistent with the listed defining relations: the `DRD^*` term vanishes on `H_1`, and `QH_1=I` leaves the `a` term. This auxiliary `G_1` should remain distinct from the convenient Feynman propagator used in the independent flat calculation; the draft explicitly makes that distinction.

The parent is incorporating the explicit L2 minimizing-fiber proof and the bond-midpoint expansion from the research note. The former supplies a direct infinite-lattice variational identification; it includes the central fine-gradient correction that restores the original coarse field after transverse representative minimization.

## 2. Refinement-limit note

Read `work/flat_covariance_limit_research.md` in full. The stated `O(M^-2)` convergence on a fixed smaller strip, and its transfer to weighted kernels and retained covariances, check.

The following points were independently verified:

1. For `pi<K<2pi`, a retained nonzero alias component has distance at least `(2pi-K)|r_mu|` from `2pi M Z`, including aliases next to a wrapped fine-zone boundary. This gives the displayed quadratic denominator lower bound. The complex real-part loss is bounded by `e^rho sum y_mu^2`, so the same fixed strip controls both finite and continuum high aliases.
2. The numerator is the paired product. Its longitudinal phases cancel exactly. Estimating the unpaired multipliers would introduce an unnecessary first-order phase error.
3. The exact relation `s_M(p)=s(p) f(p/(2M))`, with `f(w)=w/sin w`, is used on a fixed rectangle strictly inside the nonzero sine singularities at `±pi`. Its real extent is below `2pi/3` and imaginary extent at most `1/6`, including all retained aliases for `M>=3`. Thus the boundedness of `(f-1)/w^2` is valid uniformly; no small-`r/M` expansion is assumed.
4. The numerator error is bounded by `C M^(-2)|r|^2 W_r`. Division by a high-alias denominator cancels `|r|^2`. The difference of denominators is bounded by `C M^(-2)|r|^4`, and division by the product of two denominators cancels `|r|^4`. Both retained-alias errors are therefore bounded by `C M^(-2)W_r`, a summable product weight.
5. `sum_m(1+|m|)^(-2)=pi^2/3-1` is correct. The union-of-coordinate-tails argument gives the stated `2d B^(d-1)/(N+1)^3` bound after the denominator supplies two additional powers. Taking `N=(M-1)/2` makes the omitted continuum aliases `O(M^-3)`.
6. The limiting rational symbol is obtained on a smaller inherited common strip. Uniform lower bounds for the finite-`M` denominators pass to their limits; computing `E` and then the canceled precision is therefore noncircular. Coordinate-axis zeros are removable sinc values, and the limiting high remainder vanishes at the origin.
7. Uniform symbol convergence on a wider strip gives exponential weighted kernel convergence at any strictly smaller exponent, including the stated `O(M^-2)` rate. The retained maps are fixed, finite-range operators, so they preserve this rate. The uniform inverse decay gives bounded inverse weighted norms at a smaller exponent, and the resolvent identity yields the same covariance rate.
8. Periodization is an algebra homomorphism for the absolutely summable block kernels. Consequently the periodized infinite covariance is the exact inverse of the periodized finite-regulator precision. The weighted periodic norm is bounded by its infinite counterpart. This proves uniformity in compatible periodic volume, including small tori, and permits the two free limits to commute for fixed covariance entries.

For the weighted algebra statements, row and column norms should be interpreted using one common anchor metric for the unit and retained bonds, or equivalent fixed-L block metrics with constants absorbed. This is compatible with the note and introduces no refinement dependence.

## 3. Scope

These checks establish a convergent, exponentially local flat Gaussian reference in the explicitly normalized full-block setting, with rate `O(L^(-2k))` along `M=L^k`. Application to the deposited physical Gaussian retains the finite-level variational Hessian/source-coordinate identification. The analysis supplies no nonflat carrier derivatives, weighted precision perturbation theorem, large-field-history boundary identification, interacting ultraviolet limit or continuum Yang--Mills construction.
