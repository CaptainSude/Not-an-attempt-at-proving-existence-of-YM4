# Independent audit of the local quantum limit and quotient descent

17 October 2026. Auditor: theorem_audit. Full read of quantum_local_limit_research.md, together with the actual strict Gaussian construction in overlapping_interaction_cutoff_research.md Sections 9–14, the joint core/tail proof, and the periodization proof.

Verdict: the local-continuity and quotient-descent mechanism passes for the actual stated, input-independent classical data and the strict margins detailed below. Two points need to be explicit in the research statement: a positive inherited cardinality margin, and the finite translation-average argument for general asymmetric varying input families. Both are available under the existing parameter order; neither requires a new model estimate. This audit supplies the precise arguments rather than inferring continuity from the final activity norm.

## 1. Fixed classical data and topology

The local data must be selected once, independently of the inherited interaction. The required objects are the baseline covariance entries, strict symmetric precision coefficients whose matrix rows and columns lie in their label support, coherent stationary/chart coefficients, external local pivot factors, and classical base multipliers. Their analytic domains and norm bounds are uniform along the selected regulator subsequence.

At fixed R,J,M, every fixed coefficient has finitely many background, output-fiber and retained fluctuation coordinates. The actual unwindowed chart/base functions have a common complex neighborhood of the real retained window. Thus coefficientwise Montel/Cauchy compactness gives uniform convergence on each compact real window after extraction. Mere bounded measurability would not give this topology. The sharp window indicators are fixed; they are neither differentiated nor moved by a complex coordinate substitution.

The baseline principal covariances retain a positive lower spectral bound, and their Schur bound supplies a uniform upper bound. Every finite masked principal matrix and its allowed endpoint perturbation therefore has the same accretive neighborhood required in the Gaussian density estimates.

## 2. Exact spatial finiteness of the actual precision expansion

For the actual precision decomposition, a matrix entry of B_Y is zero unless both matrix indices belong to Y. A covariance Neumann term

    C0(b,u1) B_Y1(u1,v1) C0(v1,u2) ... B_Yr(ur,vr) C0(vr,c)

therefore has every intermediate endpoint in the union X of its precision labels; b,c belong to the moment roots M. The strict final carrier contains M union X. Density inverses of the masked marginal have matrix indices in the finite set M. The same endpoint statement holds for the external determinant trace chains, whose endpoints lie in their precision labels.

Consequently, for a fixed final finite carrier, all endpoint choices are finite. There is no hidden unbounded walk excursion in this actual implementation. The baseline C0 is used as its full kernel entry, not as an unrecorded walk expansion. Thus the speculative paragraph about repairing an implementation with hidden endpoints can be replaced by this actual support fact; no additional spatial weight is needed for that purpose.

The inherited joint transport likewise retains the projected original carrier and every attached background/fluctuation support. Deterministic hull choices agree on bounded lifted configurations once the period is large. Wrapping configurations cannot contribute to a fixed bounded lifted carrier for arbitrarily large periods. For convergence of totals on compact backgrounds, the separate uniform final anchored cardinality bound controls the discarded large final carriers.

## 3. Combinatorial order, Gaussian integration and normal convergence

The positive overlap, endpoint-tree and Mayer estimates can be evaluated after multiplying precision labels, interaction multipliers and bad-block marks by a common number 1+delta greater than one, provided the original sufficient inequalities have a strict margin. This is legitimate for the bad indicators as well: multiplying their bounded bad-block factors only multiplies the corresponding joint-tail activity weight. It does not require a new probability estimate or differentiation of an indicator.

Every nonempty molecule contains an interaction or bad-block mark. Forest edge count is controlled by molecule count. Repeated polymers in a Mayer cluster therefore increase marked order. The remaining precision inverse/determinant orders are controlled by their strict geometric budgets. Hence the sum of terms of total marked order above k has a regulator-uniform geometric bound, with an additional geometric precision-order bound if the two truncations are kept separate.

After restricting to a fixed final carrier and bounded marked/precision order, there are finitely many discrete choices. Each remaining term is an integral over a fixed finite Gaussian coordinate space and compact forest parameters. Its covariance entries and analytic factors converge locally normally. The established accretive density majorant is integrable on the whole real Gaussian space and independent of the regulator. The bounded measurable cutoff factors cause no difficulty for dominated convergence; the analytic multiplier factors converge uniformly on their fixed retained windows. The same statement holds uniformly on compact background polydiscs, or follows there by the uniform bounds and uniqueness of the holomorphic limit.

These finite-term limits plus the geometric tails prove unique local coefficient limits for the selected limiting local data and assignments. This is stronger than an output norm bound or arbitrary subsequential compactness. Fatou retains the original full open b norm afterward.

## 4. Explicit inherited cardinality and tail-order margins

The original common-domain displays use

    c1(R) B <= a0/2,
    D(J) log(1/(1-t)) <= a0/2.

Those weak inequalities only imply a nonnegative margin. For the local-limit proof choose, under the same permitted parameter order,

    c1(R) B <= a0/4,
    D(J) log(1/(1-t)) <= a0/4.

Here c1(R)=5^d 2^d/k_R tends to zero as R grows, after C_A and B have been fixed. Then J and the logarithmic tail offset are chosen; their sufficient bound is a constant times J^{2d} exp(-kappa0 ell_tail/2), which tends to zero. Neither choice depends on the subsequently selected b. Thus

    delta_card = a0 - c1(R)B - D(J)log(1/(1-t))
               >= a0/2 > 0.

The proof of the actual joint transport then gives a tail at original carrier size greater than Q bounded by C epsilon exp(-delta_card Q). This follows before summing the original rooted carrier norm.

There is also a tail-degree margin. Since the two displayed terms use at most a0/2, choose a fixed zeta>1 close enough to one that zeta t<1 and

    c1(R)B + D(J)log(1/(1-zeta t)) < a0.

The same positive scalar-multiindex calculation with zeta t bounds terms of tail-expansion degree above k by a constant times zeta^{-k}. If t=0 that expansion has no nonzero tail degrees. Fixed support-radius truncation is controlled by the rooted exponential weight and the strict spatial budget kappa_tail > B+delta used in the actual numbers.

On the resulting finite list, all inherited evaluations and their scalar Cauchy derivatives occur in a fixed interior of the old b polydisc. Local normal input convergence therefore passes through the core evaluations, tail expansion and bounded fluctuation windows. Equal-carrier exponentiation preserves the resulting convergence and multiplier bounds.

## 5. Quotient descent and the Lipschitz estimate

For near-minimal input and difference representatives, first choose covariant representatives Y and D, which the proved averaging theorem allows without norm increase, and set X=Y+D. This preserves the compatible linear inherited assignment and gives the displayed three-quarter input budget. Choosing two unrelated near-minimal representatives would not directly bound their representative difference by the quotient distance.

Equal invariant input classes have exactly equal finite vacuum-normalized periodizations. Their inherited fluctuation differences are therefore equal as actual finite scalar insertions; their background terms differ only by the separately handled constant if raw conventions differ. The same finite Gaussian integral and compatible logarithm branch give equal normalized output totals. Canonical carrier arrays need not agree. Local coefficient convergence and compact-total convergence then give equal limiting quotient classes.

The Gaussian logarithm comparison does not use the fifth-order condition on the input difference. The external pivot and determinant terms are input independent and cancel. Thus the established bound

    ||G_g(x)-G_g(y)||_Q
      <= 1024 e S1 C_T C_R (gT/b) ||x-y||_Q

passes by Fatou on the compatible difference family and by the representative infimum. Adding the bounded classical background transport gives the full Lipschitz bound stated in the note. These constants refer to the same original majorants and fixed geometry; the local-continuity argument does not replace them with a new cutoff normalization.

## 6. General varying finite inputs

Suppose actual finite invariant inputs E_N converge locally normally to E with uniform budgets. The direct continuity argument gives an output limit from that specific possibly asymmetric carrier family. To identify its class with the canonical quotient map, use the following additional argument.

Average each finite E_N over its finite cell-translation group. The resulting covariant family has no larger anchored norm and exactly the same finite normalized total, because the finite total is translation invariant. Its actual finite quantum output therefore has the same normalized total as the original output.

Extract a locally normal subsequence of these averaged families. Finite covariance passes to a covariant infinite limit E_cov. Compact-total convergence for both the original and averaged inputs shows Phi_{E_cov}=Phi_E. Apply the proven local construction continuity to the averaged finite inputs. Their limiting local data are E_cov and the already fixed classical data. The canonical periodizations of E_cov have the same local data and uniform bounds, so their output coefficient limits agree for the chosen construction. These outputs represent F_g([E]).

Passing the finite output-total equality identifies the direct output limit from E with that same quotient class. The original and averaged canonical carrier arrays need not coincide. Every subsequence of averaged families admits this argument, so no interaction-dependent change of the fixed classical system is needed.

This proves the varying-input extension at the normalized total/quotient level. It still requires exact invariant finite inputs, compatible chart and gauge-orbit insertion domains, common strict margins, and the fixed input-independent local classical data.

## 7. Remaining limits of the result

The construction is a map for the selected homogeneous local sector and chosen infinite classical system. It does not prove uniqueness across arbitrary classical subsequences, identify a one-shot macro integral with a sequence of differently cut off quantum integrals, supply a stable renormalized amplitude ball, determine the coupling trajectory, or cover mixed/large-field histories and observables.

Subject to the explicit strict-cardinality choice and varying-input argument above, no further mathematical obstruction was found in the local-continuity and quotient-descent proof. No output files were changed and no compilation was run.

## Amended research and fragment check

The appended Section 7 of quantum_local_limit_research.md faithfully incorporates every required clarification above. It supplies the positive cardinality and tail-degree margins, aggregation by carrier and finite type, actual precision endpoint containment, primitive mark dilation, covariant near-minimal representatives and the complete finite-averaging proof for varying asymmetric inputs. It supersedes the earlier provisional text rather than leaving those interfaces as unproved conclusions.

The integrated quantum_local_limit_fragment.tex places those arguments in proof order and omits the obsolete conditional discussion. It additionally states the finite-history boundary explicitly: each intermediate actual finite family must meet the uniform budgets and insertion domains; an infinite quotient relocalization does not itself control actual finite winding remainders. Finite reference subtraction, if later included, needs local normal convergence and convergence of the extraction coefficients, not equality with canonical periodization. Vacuum factors remain separately tracked, and no convergence of extensive vacuum energies is asserted.

Self-check: 25 unique qll labels, 11 references resolved with the pid fragment, balanced braces and no control characters. No compile was run. Independent fragment fidelity review has been requested.
