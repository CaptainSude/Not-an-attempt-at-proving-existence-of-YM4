# Independent audit of assembled Notebook 09

16 October 2026. Reviewed `ym4-flat-current-candidate.tex` in its assembled form, including the added averaging formulas, zero-sector clarification, scalar Z lemma, repositioned response identities, and consolidated current section. Compared with the previously audited full-inverse, scalar/current-response, and auxiliary-current-neighborhood proofs. **Pass within the stated homogeneous flat auxiliary-family scope. No mathematical or cross-reference correction is required.** No output or candidate source was edited.

## 1. Mechanical completeness

- The assembled source contains 67 equation/theorem/section labels, all unique.
- All 39 explicit internal `ref`/`eqref` references resolve to a label in the document.
- The built-in LaTeX compiler reported success for the assembled candidate.
- Notebook 07 and Notebook 08 are explicitly declared prior inputs, rather than being treated as assertions proved again in this document. Their role is limited to the previously audited alias estimates, Maxwell precision locality, and exact source-gauge minimizing extension.

## 2. Explicit averages and source normalization

The new physical-space formulas are correctly normalized. The scalar average is `M^-d` times a centered block sum. The one-form average is `M^-d-1` times the centered block sum and an oriented `M`-bond straight string. Applying the latter to the physical fine gradient `D=M(T_eta-I)` telescopes the string and yields exactly `QD=d_c Q_0`, with no missing scale factor. Their displayed Fourier multipliers agree with these formulas, including the longitudinal phase, and obey the two stated cochain identities.

The document consistently distinguishes physical Maxwell precision `q_M`, penalized coarse precision `q_0=q_M+aI`, and scalar auxiliary penalty `a'`. The source identification `a=ell^-2=1` at normalized unit spacing is retained; uniformity for other penalties is restricted to a compact positive interval. No unverified `a_n` recursion has been inserted.

## 3. Full inverse and constant sector

The rank-one subtraction, both Woodbury steps, squared `W_2` denominator, central beta cancellation, and signs coincide with the independently passed full-inverse proof. The added explicit multipliers are compatible with its bilinear analytic-transpose convention. In particular, the central/high decomposition is only used on an enlarged chart, while the full reconstructed operator is glued periodically; no separate nonperiodic central term is asserted to be a torus symbol.

The constant scalar sector is now unambiguous. `R` is zero on the constant scalar alias and identity on its high aliases at zero coarse momentum. Consequently the constant one-form inverse is `a^-1 I`, the high inverse is `P_r^-1 I`, and no inverse constant scalar Laplacian is used. The independent `M=1` formula correctly reduces to the inverse of Maxwell plus the positive one-form penalty.

The proof retains the correct quantitative scope: all placements of at most two fine differences are bounded as physical-cell L2 operators, uniformly in refinement and compatible periodic volume. It does not promote these estimates to pointwise regularity or to arbitrary Dirichlet/multiscale geometry. The auxiliary fine gap is explicitly distinguished from a physical mass gap.

## 4. Inserted scalar lemma and current coefficient bound

The expansion of `Z=G'RG'` is the constrained inverse of the scalar squared Laplacian on `ker Q_0`. The restriction argument correctly eliminates the scalar penalty, and the zero and `M=1` sectors match the canceled aliases. The total-four-derivative estimate uses alias operator norms and bounded rank vectors before physical reconstruction, avoiding a growing cell-dimension factor.

The identities `Q_0G'R=0`, `L G'R=R`, and `RG'L=R` yield `Lambda=Z L D*` and `D Lambda=D Z L D*` with total derivative orders three and four. Thus the scalar lemma actually supplies every leg used in the current vertex bound.

The factorization `m_J=V_JD+D*V_J*` follows from the displayed polarized quadratic term. The current-linear maps `j_J,V_J` have fixed fine incidence and uniformly bounded physical-cell norms. The combined expression for `Theta'_J` places derivatives on `D Lambda`, not on `J`. Therefore the bounded-current hypothesis is sufficient even at cell discontinuities. For complex currents all transposes are stipulated analytic continuations, so this factorization remains complex linear.

## 5. Repositioned response identities

Placing the response identities after the common input bound introduces no circularity. They use only the already proved full inverse, source-gauge minimizing extension, and scalar identities. In detail, for `lambda=Zf`, one has `Q_0lambda=0`, `Llambda=RG'f`, and hence

    Delta_0 Dlambda=D R G'f=Lambda*f,  QDlambda=0.

Thus `G_0Lambda*=B_0Lambda*=DZ` and `Lambda DZ=Z` follow exactly. The later first extension derivative and quadratic precision derivative have the correct order, sign, and normalization. The auxiliary first precision derivative vanishes, but the first extension derivative is generally a nonzero fine gradient. The original source gauge is not claimed to persist for nonzero current.

## 6. Current neighborhood, all-order formulas, and scope

The constants `c=g b^2 q`, `e=g b q`, `t_0=g(1+c)`, and radius `[4g theta(1+c)]^-1` still control both Neumann inverses in their proper noncommuting order. The constrained covariance identities give the exact quadratic remainder, and its displayed bounds are valid on the entire stated ball.

The increment identities yield the factorial derivative chains with precisely `n-1` constrained propagators in the coarse-precision derivative. The source-support proof estimates products in the weighted algebra before taking their blocks; therefore it does not introduce an unaccounted borderline convolution. Finite-incidence offsets and the four terms per insertion cost only a fixed exponential in derivative order. Repeated source cells and short compatible periodic directions are covered.

The outside-factor resolvent identity correctly propagates the total-two-fine-difference estimates without differentiating the current. The document consistently uses the physical cell norm and does not infer a pointwise or Hölder carrier theorem.

The final scope statement agrees with the abstract and theorem: the proved family is `G_pi^J`, involving only `Theta'_J`. The distinct nonlinear-constraint term `Pi* Theta_J Pi` is explicitly excluded and its potentially nonzero first precision response is recorded. Nonflat backgrounds, retained histories, source pointwise norms, and the interacting ultraviolet construction remain separate. Consolidating the former duplicate sections has not erased any of these restrictions.

## 7. Result

The integration preserves the passed mathematical content and supplies its dependencies in a coherent order. It is ready for the parent's final document review within the explicitly stated scope. The check is an internal independent mathematical audit, not external certification or a novelty assessment.
