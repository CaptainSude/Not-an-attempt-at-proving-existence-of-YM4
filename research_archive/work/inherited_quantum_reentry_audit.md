# Independent audit: inherited quantum interaction re-entry

17 October 2026. Audited `inherited_quantum_reentry_research.md`, especially Sections 2–4 and 8, against the exact source chart in `physical_current_pivot_precision_research.md`, the connected-carrier compression proof, and the labelled overlapping-interaction and tunable strict-support Gaussian theorem. No repository or output notebook was edited.

## Result

The finite-step re-entry estimate passes, conditional on its displayed weight inequality and the complete independent-background covariance/precision hypotheses. Its actual source geometry, directional Cauchy estimate, grouped multiplier estimate, and coefficient-level logarithm comparison are valid. The estimate does not establish that any blocking factor satisfies the inequality for the previously generated constants, nor does it establish a stable iteration domain.

One cutoff clarification was requested and adopted in the research note and fragment: the Euclidean block radius enclosing a retained linkwise window must not be confused with the threshold controlling its bad event. The correct distinction is recorded in Section 6 below; it changes no claimed bound when the original linkwise threshold is used.

## 1. The actual source pivot dependency

At current spacing one, write the centered blocks as B_L(y), with odd L. For the positive coarse bond c=(y,y+L e_mu), the ordinary source average reads internal root contours in these two blocks, the straight strings from x to x+L e_mu for x in B_L(y), and the center reference string. Every such string stays inside the union of the two endpoint blocks and crosses their common interface once. Every internal root contour stays within one block.

The selected pivot is the interface bond on the line of the centers. Its positive initial site belongs to the y-block. No contour includes a pivot. No string for a different coarse bond includes this selected pivot: either its orientation differs or its pair of adjacent endpoint blocks differs. On the source tori with distinct interfaces, this remains true even when different endpoint blocks are neighbors in more than one periodic direction. Thus the nonlinear equation for c contains precisely its own pivot variable among all eliminated pivot variables.

Solving that equation by the local implicit function theorem cannot propagate its dependence through other pivot unknowns. Its coefficients and its solution read only the full background and retained fibers of the two endpoint blocks. This is stronger than a generic finite-range assertion and follows from the displayed source average, not from a replacement chart or a flat linearization.

For a retained bond b, the exact identity Phi_V(z)(b)=z(b) means the ordinary final angle F(a,z)(b) reads only a(b) and z(b). The final logarithm is bondwise. Consequently the proposed declared carrier

    Y(H)=pi_L(H) union {the forward endpoint block of c : p(c) starts in H}

is sufficient for both the fluctuation and independent-background variables of the inherited increment. Positive oriented current bonds are assigned to their initial sites. This convention is essential to the stated d+1 bound; an alternative convention may require the larger safe neighbor count already mentioned in the note.

## 2. Carrier size, connectivity, and anchors

The image pi_L(H) of a connected nearest-neighbor current carrier is connected. Each added endpoint block is adjacent to a block already in that image, so Y(H) is connected. Its metric spanning-tree length is therefore exactly |Y(H)|−1. At most d outgoing coarse pivots have their initial sites in any projected block. Hence

    |Y(H)| <= (d+1)|pi_L(H)|.

For a fixed anchor block B, membership B in Y(H) implies that some i in H has pi_L(i)=B or a block adjacent to B. Therefore the displayed anchor inequality is valid, and summing over at most (2d+1)L^d possible current sites is safe. Periodic identifications only reduce these counts. The chart itself retains its original distinct-interface hypothesis; the audit does not enlarge its regulator class by geometric analogy alone.

The earlier connected-carrier packing lemma gives

    |pi_L(H)| <= 2^d + (2^d/k_L)|H|,
    k_L=1+floor((((L−1)/2)−1)/2).

Combining the two estimates gives exactly (4.5). There is no O(L^d)|H| support enlargement hidden in the actual pivot map. There is an L^d anchor multiplicity, which the norm estimate explicitly retains.

## 3. Directional Cauchy without a dimension factor

The fixed-L local analytic chart has a uniform displacement bound in scalar maximum coordinates,

    ||F(a,z)−a||_infinity <= C_ch(L)||z||_infinity.

It is uniform in prior classical depth and volume. No bound uniform in L is assumed. Fixed color-norm conversions are included in C_ch.

Let the old activity be bounded by e_H on its scalar coordinate polydisc of radius b. For ||a||<b_-, put m=b−b_-, h=F(a,g xi)|H−a|H, and delta=C_ch |g|R<m. The scalar function f(zeta)=E_H(a|H+zeta h) is bounded by e_H on |zeta|<m/delta. Its coefficient bounds give

    |E_H(a+h)−E_H(a)| <= e_H delta/(m−delta).

The delta=0 case is immediate. This is genuinely independent of the number of coordinates in H: it estimates one directional value increment. It is not a bound on the sum of all multivariate coefficients and does not remove the D|H| cost in the distinct stationary-support substitution theorem.

The bound is uniform over the independent complex background and over the real retained cutoff. The interaction is measurable in the real fluctuation variables and holomorphic in the background. Multiplying its bounded multiplier by all cell cutoffs it reads, then extending by zero, is legitimate for the Gaussian theorem: on the global retained window it leaves the exact original integrand unchanged. It neither differentiates nor moves a sharp indicator.

There is no g^(−2) prefactor for an inherited dimensionless quantum exponent. Its linear and quadratic fluctuation terms can remain bounded interactions. The exact splitting into the old background value and the relative fluctuation increment does not require a new quantum stationary point.

## 4. The grouped interaction norm

Grouping equal Y before exponentiating is correctly handled. Absolute anchoring gives

    sup_B sum_(Y contains B)||Q_Y|| <= V_max,
    V_max=u(2d+1)L^d epsilon,
    u=delta/(m−delta).

Thus every grouped Q_Y has norm at most V_max, and

    ||exp(Q_Y)−1|| <= exp(V_max)||Q_Y||.

It would be incorrect to replace V_max by u epsilon after grouping; the saved argument does not do so. Alternatively the overlap theorem explicitly permits distinct interaction labels with the same support, so retaining H labels is also legitimate and has the smaller per-label exponent bound indicated in the note.

The strict tunable Gaussian theorem requires the inherited multiplier norm with weight

    Kcal_theta^|Y| exp(4|Y|+kappa ell(Y)).

Connectedness bounds this by exp(B_req |Y|), where

    B_req=4+log Kcal_theta+kappa.

The explicit sufficient budget

    [(d+1)2^d/k_L] B_req <= a0

then pays the full target weight, including its spatial term. The additive compression constant costs exp[B_req(d+1)2^d]. Re-rooting costs (2d+1)L^d. These are precisely the factors in (4.7). No polynomial |H| factor was lost: the value-increment estimate needs none. If later operations introduce one, a strict additional exponent margin is necessary, as the note states.

Each increment still reads only the independent background and fluctuation cells in Y. That is exactly the strict-support input of the Gaussian theorem. Substitution of a_*(w) before this theorem would destroy that assertion; the note correctly postpones it until after the independent-background expansion.

## 5. Meaning of theta and the conditional comparison

Here theta is the tunable small complex-covariance/density parameter of the real-baseline strict-support theorem. It is not a background radius, a cutoff radius, or a free support exponent. The strict theorem uses the full displayed local precision conditions, including its determinant and inverse-density budgets, and the endpoint covariance Cauchy radius proportional to theta. Merely having a covariance operator close to its baseline does not establish strict background locality.

Its dimension cost is

    log Kcal_theta = (D_G/2)[log(1+theta)−3log(1−theta)]
                  <= (5/2)D_G theta,  0<theta<=1/4.

Consequently theta=1/(4D_G) gives log Kcal_theta<=5/8 and B_req<=37/8+kappa. This verifies the stated dimension tradeoff. The strengthened precision neighborhood and the smaller endpoint Cauchy radius must still be met. The baseline spectral and decay constants may depend on L, and no such dependence has been suppressed in the conclusion.

For Section 8, treat the base and inherited multipliers as separate labelled interaction families, even if some supports coincide. The overlap theorem permits this. Multiplying only inherited bounded multipliers by lambda leaves the base family fixed and interpolates exactly between the base and actual integrals. It does not require exponentiating lambda Q_Y.

If eta_base<=eta_*/4 and epsilon_int<=eta_*/4, the disk radius R_lambda=eta_*/(2 epsilon_int)>=2 has total budget at most 3eta_*/4. The same canonical connected support expansion, with the same fixed carrier assignments, is holomorphic as an output Banach-space vector and bounded by C_out eta_*. Cauchy therefore yields

    ||U(1)−U(0)||_out <= C_out eta_* /(R_lambda−1)
                       <=4 C_out epsilon_int.

This compares actual connected-logarithm coefficients, not only scalar logarithms. The positive uniform support majorant justifies the Banach-valued holomorphy and countable-label limits. The separately transported old background contribution remains outside this comparison and is not discarded as a vacuum.

## 6. Retained cutoff and Gaussian tail clarification

For the actual linkwise color-ball window in one Gaussian cell,

    chi_B(xi_B)=product_(b retained in B) 1{|xi_b|_g<=R},

one has

    {chi_B=0} subset {||xi_B||_2>R}.

Thus the correlated Euclidean-block joint tail applies to every selected bad cell with the same threshold R. This is the appropriate use of the earlier centered real Gaussian tail theorem. Independence of the cells is unnecessary.

By contrast, inside the good rectangle one only knows ||xi_B||_2<=sqrt(N_retained_links)R. That larger enclosing radius is useful if an estimate is formulated in the full block norm, but it is not a valid larger threshold for the bad-event probability. In particular the rectangular cutoff must not be assigned the falsely stronger tail obtained by inserting sqrt(D_G)R in the bad-event estimate.

The present displacement estimate uses the scalar supremum norm, so |g|R is its direct input without any growing block factor. The note's numerical tail threshold with R is valid. The original Gaussian proof extends from a block ball to this rectangle because it uses only the pointwise domination of each bad indicator by its block-norm threshold event. Any additional source indicators would still need their own treatment.

## 7. What this closes and what remains

For each fixed L satisfying the displayed weight inequality and the other Gaussian/chart hypotheses, this proves a real inherited-interaction re-entry estimate of order

    O_L(epsilon |g|R/(b−b_-))

on the independent background ball, followed by the separately controlled stationary transport. At fixed constants the new fluctuation contribution can be made small with gR tending to zero. The old background contribution is still only bounded by the stationary transport map; no generic contraction of it has been proved.

The previous output reserve is a0(L), not an independent positive constant. Positivity of a0(L) for every fixed L does not imply that k_L a0(L) eventually dominates (d+1)2^d B_req(L). The note correctly leaves the existence of such an L unproved. The further domain shrink b_-<b and the stationary-substitution radius losses also remain. These are explicit quantitative induction interfaces, not failures of the finite-step Cauchy or source-geometry lemma.

The full inherited_quantum_reentry_fragment.tex was also checked for fidelity. Its mathematics matches the corrected note. A missing backslash before one qquad was reported, together with a request to state odd L>=5 explicitly when citing the compression lemma (the original source choice L>11 already suffices). No mathematical correction was found in the stated conditional re-entry theorem or its coefficient comparison.
