# A local limit of the actual quantum macrostep

17 October 2026. Research proof candidate. The purpose is to turn the finite common-domain macrostep into a map on analytic interaction classes, rather than assuming that a subsequential kernel limit is already an iterable quantum map. The finite periodization theorem below is an explicit input pending its separate proof. No coupling trajectory or large-field completion is asserted.

## 1. Fixed geometry and data

Fix the elementary ratio R, the auxiliary grouping J, the retained real link/color window, the classical depth M, and the common radius b from Notebook28. Work on compatible cubic tori exhausting the current and next lattices together. All macro cell dimensions are fixed once R,J are fixed. The Gaussian cutoff threshold T and positive coupling g are fixed in this limit.

The actual finite normalized correction is

    F_N(E_N)=T_N E_N + Delta_N + Qdet_N + L_N(Q_(E_N)),
    G_N(E_N)=Delta_N+Qdet_N+L_N(Q_(E_N)).                (1.1)

T_N is pre-gauge background substitution; Q_(E_N) is the inherited fluctuation difference in the actual selected chart. L_N is the strictly local Gaussian cluster logarithm with its fixed base factors and precision. The same cutoffs and field-independent normalization as Notebook28 are retained. Vacuum-normalized totals will be taken only after this expression is constructed.

Use the strict versions of all common-domain budgets, for example the quarter budgets of the high-jet quantum comparison, with a fixed margin. The scalar activity norm is the anchored connected norm at a0=1/16 and radius b. The joint exponent, precision weights and Gaussian marked bounds retain their larger reserves.

Call a sequence of local analytic coefficients locally normal if every fixed lifted finite carrier coefficient converges uniformly on compact subsets of its finite-dimensional background polydisc. For joint fluctuation coefficients require this convergence uniformly on the fixed real window of the finitely many fluctuation coordinates involved. Matrix coefficients converge in their finite-dimensional block norm. The final output norm bound will still hold on the full open b ball by Fatou; local normal convergence itself is only required on smaller compact subsets.

Assume the following fixed classical data have been chosen on one common subsequence:

1. Every fixed baseline covariance entry C_(0,N)(i,j) converges, with the uniform exponential Schur bounds and positive spectral lower bounds already used in the Gaussian theorem.
2. The strict precision labels B_(N,Y), base exponent labels, pivot-log factors, and coherent pre-gauge and joint chart support coefficients converge locally normally.
3. Their uniform stronger support norms, analytic margins, and all exact local scalar identities are those of the actual finite construction.

These assumptions are about a single input-independent classical system. They can be attained at fixed parameters by countable diagonal compactness of its strict families. Precision labels have finitely many matrix entries on every fixed Y. For chart/base coefficients on compact real windows, either use their existing holomorphic extension in the finite fluctuation variables or uniform Cauchy bounds on a common complex neighborhood; pointwise bounded measurable functions alone would not imply compactness in that norm. The actual chart construction supplies such analytic fluctuation dependence. Sharp indicators are fixed and are not differentiated or passed through a complex change of variables.

The flat covariance input is stronger than an arbitrary choice of finite baselines: the actual homogeneous flat formulas give compatible periodized kernels. At minimum, one may extract their entries jointly using their uniform exponential bounds, preserving every finite principal spectral inequality. No universal statement for a different sequence of baselines is claimed.

## 2. The required periodization input

For an invariant infinite class [E] in the quotient of Notebook29, assume a finite periodization Per_N[E] is available with:

* a connected radius-b representation of norm at most ||[E]||+eta, for any eta>0 after choosing an almost-minimal covariant representative;
* exact independence of that representative as a finite vacuum-normalized total;
* exact finite local gauge and spatial identities on the common logarithmic domain;
* for a fixed covariant representative E, local normal convergence of the periodized coefficients to E, with uniform anchored bounds.

The same construction is linear on representatives and on differences. These are the proposed conclusions of periodic_interaction_descent_research.md, not consequences of the quotient definition alone.

The finite periodization has a specified vacuum normalization. The original separately tracked pressure/normalization is not erased from the finite integral; equality of vacuum-normalized input totals means the two actual input insertions differ only by the separately accounted scalar factor.

## 3. Continuity of the strict Gaussian cluster construction

Here is the analytic lemma needed for the limit. Consider finite periodic instances of the strict overlapping Gaussian theorem with fixed cell dimension, fixed real windows, uniform strict precision and multiplier budgets, and locally normal convergence of the baseline entries, precision labels and multiplier coefficients. Fix deterministic connecting graphs that agree on every bounded lifted configuration once the period is sufficiently large. Then their canonical vacuum-normalized connected logarithm families have locally normal coefficient limits, with the same anchored bound.

The proof uses the construction, not merely its final norm bound:

(a) In the precision expansion C=C0-C0BC0+..., retain every precision label and every covariance-link endpoint. A fixed finite labelled term uses only finitely many baseline entries and analytic precision coefficients. It converges locally normally. The strict K nu<1 budget bounds the remaining precision order by a geometric series uniformly in the regulator.

(b) A Gaussian moment on a fixed set of fluctuation cells uses the finite principal covariance on that set. Its masked baseline and the degree-adapted endpoint perturbations retain a common accretive neighborhood. The determinant and inverse are therefore continuous holomorphic functions of those finitely many entries. The existing density majorant dominates the entire integral on R^(D|M|), including the determinant normalization. The fixed bad-block indicators are bounded measurable functions, so dominated convergence applies without differentiating them. The interaction multipliers on their compact windows converge uniformly.

(c) The support-algebra determinant and inverse expansions retain their precision labels before grouping. Their strict geometric budgets give normal convergence. Molecule expansions, covariance forests and Mayer connected sums are then controlled by the same positive rooted-tree majorants as in the finite theorem. In using local coefficient convergence, one must truncate both spatial extent and combinatorial order, rather than appeal to a bound on the final sum alone.

For spatial extent, keep the full marked construction before the final hull assignment. Its positive weights retain the fluctuation cells, every precision label and the endpoints of the covariance paths. Every finite term contributing to a fixed final carrier H has its terminal labels inside H. If an implementation instead groups a covariance chain only by its background labels and hides intermediate endpoints, retain those endpoints until the majorant truncation; their exponential Schur weights control excursions outside a large neighborhood. Such a retention is allowed by the established path/forest construction and changes only a fixed support reserve. No locality of a summed scalar function is being inferred.

For combinatorial order, a uniform strict margin allows a bookkeeping dilation of precision labels, interaction multipliers and bad-block marks by a factor 1+delta>1 while the same positive majorants remain summable. The retained forest and Mayer series are thus normally convergent in that dilation parameter, and their terms of total marked order >k have a uniform geometric tail. Covariance forest edges connect existing marked molecules; their number is controlled by molecule count. The density's own precision/determinant orders are controlled by their separate strict geometric budgets. There is no unmarked infinite combinatorial order left after these truncations.

After both truncations only finitely many support/endpoint choices remain. Their finite-dimensional Gaussian integrals and compact BKAR parameter integrals converge by (a),(b). The common normal tail bounds then pass the full coefficient. Grouping by fixed hulls preserves convergence. Winding configurations necessarily escape every fixed lifted neighborhood as the period grows; the same spatial tail estimate controls them.

Fatou at each radius r<b followed by r increasing to b preserves the original output norm. The limiting coefficients define an analytic interaction. The interaction compactness argument of Notebook29 then identifies the limit of the vacuum-normalized scalar logarithm on compact backgrounds. This gives a unique limit for the chosen limiting local data and deterministic assignments, not just existence of an arbitrary subsequential output.

The bookkeeping margin is substantive. If a theorem is stated exactly at the edge of its sufficient budgets, first impose stricter versions when selecting b,g,T. The parameter order in Notebook28 permits this. The lemma does not assert convergence in the global anchored norm from merely local coefficient convergence.

## 4. Applying the lemma to inherited insertions

For a fixed covariant input representative E, the core/tail joint transport uses a finite-dimensional analytic germ E_H evaluated in a strict interior of its radius-b domain, plus a normally convergent expansion in the small distant tail. All support assignments retain the projected input carrier and the relevant background/fluctuation supports. Consequently local normal convergence of Per_N E and the fixed classical/chart data implies local normal convergence of Q_(Per_N E), uniformly on every fixed real retained window.

More explicitly, truncate the input carrier size, spatial tail and tail-expansion degree. On the retained finite list, evaluations and derivatives of E_H converge uniformly on a smaller polydisc by Cauchy. The core and actual fluctuation chart remain in that fixed interior. The joint support norm and the strict tail budget bound the omitted part by the same positive geometric/exponential majorants as Notebook28. The complete output-fiber maximum is inside the family sum, so no hidden count of fine output coordinates is introduced.

The linear maps in the inherited input are exactly the same compatible maps as in the high-jet quantum-difference proof. Equal-carrier exponentiation preserves locally normal convergence on finite carriers and its uniform multiplier bounds. Section3 therefore applies to L_N. The external pivot factors converge by ordinary local analytic composition; Qdet converges by its strictly summable trace series in C0 B. Classical substitution converges by the summable-field result of Notebook29.

It follows that F_N(Per_N E), in the specified canonical representation, has an infinite connected family limit F(E) at the same a0,b. This is an actual local limit of the finite local quantum sector with its stated continuation. It is not an identification of that sector with the full Wilson measure or with histories containing large fields.

## 5. Descent and norm estimates

Suppose E and E' represent the same invariant input class, and both chosen representations satisfy the allowed norm bound. Their finite periodizations have the same vacuum-normalized total by Section2. Therefore their actual finite Gaussian insertions and inherited background terms yield the same finite output normalized total, with the same compatible logarithm branch. The finite canonical coefficient arrays need not agree.

Pass to their local limits using Section4 and the interaction compactness theorem. Their limiting normalized totals agree on every compact output field. Thus [F(E)]=[F(E')]. This proves a well-defined map F_g on the allowed invariant quotient ball. Its output gauge and spatial identities follow from the exact finite identities and their local normal limit. The same reasoning defines T on the quotient and the quantum remainder G_g=F_g-T.

There is a useful quantitative point concerning quotient infima. A bound proved for arbitrary coefficient representatives does not immediately become a two-input quotient bound by choosing two separate near-minimal representatives. Instead, for two classes x,y choose a representative Y of y and a representative D of x-y, then set X=Y+D. If ||x||,||y||<=epsilon_bar/4, these can be chosen with

    ||Y||<=epsilon_bar/4+eta,
    ||D||<=||x-y||+eta<=epsilon_bar/2+eta,
    ||X||<=3epsilon_bar/4+2eta<epsilon_bar.

Thus both complete inputs lie inside the finite comparison domain. Apply the same compatible finite construction and then take eta to zero.

The Gaussian comparison in Notebook28 never uses the high-jet condition in its logarithm estimate. It therefore gives, for all such differences,

    ||G_g(x)-G_g(y)||_Q
       <= C_quant (gT/b) ||x-y||_Q,                    (5.1)

where C_quant=1024 e S1 C_T C_R at the fixed geometry. The external Delta and determinant cancel. This is the small inherited-input dependence of the quantum remainder, not a bound for the whole unextracted background map.

The ordinary background transport bound gives

    ||F_g(x)-F_g(y)||_Q
       <= [B_R+C_quant(gT/b)] ||x-y||_Q,               (5.2)

with the previously established finite B_R. Fatou passes the finite norm bound to the output difference family; then taking the quotient and eta limits proves the displayed statements. The one-input force and normalization estimates also pass, but are not by themselves an invariant-ball estimate after extraction.

All constants remain uniform in preceding M when the actual fixed classical data and their support norms are uniform there. A simultaneous countable system in M can be chosen. The construction is relative to that chosen classical local limit; uniqueness across arbitrary systems is not asserted.

## 6. Remaining interface before iteration

Sections3-5 would establish universal quantum descent if the periodization theorem in Section2 and the local-normal continuity argument of Sections3-4 both pass independent audit. Neither is to be replaced by an unproved assertion that an anchored output bound implies continuity.

Even a quantum map on the quotient does not yet identify its iterates with the finite original Wilson recursion. For that, if varying finite inputs E_N converge locally normally to E with uniform budgets, the same continuity proof must apply to F_N(E_N), and the output must agree with F(E). The argument above is designed to have precisely that extension: Section4 uses local normal input convergence and uniform bounds, not only the name Per_N. It still requires exact compatible input domains and the fixed classical system. Establish this extension explicitly before using repeated steps.

Next one must retain the generated quantum terms in a finite block of q steps, extract the full reference, prove an invariant renormalized activity ball and an actual coupling trajectory, and then incorporate the remaining field sectors and observable limits. No such recurrence or continuum theorem is claimed in this note.

## 7. Audited amendments and completed varying-input theorem

This section supersedes the provisional language and indicated interfaces in Sections1-6. The independent audits are quantum_local_limit_theorem_audit.md and quantum_local_limit_provenance_audit.md. With the following explicit choices, they pass the local-limit, quotient-descent and varying-input arguments. The mathematical scope remains the actual homogeneous local quantum sector relative to a fixed jointly chosen classical system.

First, periodic_interaction_descent_research.md is now proved and independently audited. Its periodization has every property in Section2. For each fixed finite connected carrier K, the grouped raw coefficient is exactly E_K for all N>4 diam(K)+4: any connected preimage projecting to K lies in one of the disjoint nonadjacent copies K+Nz, and hence equals that copy.

Second, the inherited transport needs the strict margin

    delta_card = a0-c1 B-D(J)log(1/(1-t)) >= a0/2 > 0.  (7.1)

Choose the elementary ratio R large enough for c1(R)B<=a0/4. Next choose J and its logarithmic tail collar so D(J)log(1/(1-t))<=a0/4. The latter tends to zero as J^(2d) exp(-kappa0 ell_tail/2), independently of b. This respects the established R, then J, then b order. Input carriers larger than Q then contribute at most C epsilon exp(-delta_card Q) in the positive core/tail majorant. A further fixed zeta>1 with zeta t<1 and c1 B+D(J)log(1/(1-zeta t))<a0 gives a separate O(zeta^(-k)) tail above tail-expansion degree k. Thus the truncations asserted in Section4 have explicit uniform positive tails.

Third, primitive labels must be aggregated by carrier and type before limits. The actual construction has only finitely many types per fixed carrier: precision matrix, base exponent, inherited exponent and bad-block types. There is no infinite unbounded auxiliary label multiplicity without its own uniform tail.

Fourth, the actual precision locality is stronger than the alternative hidden-endpoint discussion of Section3. Each B_Y has both rows and columns in Y. Every intermediate index in a C0--B_Y--C0 chain belongs to a marked marginal cell or a retained precision carrier. The masked baseline inverse acts on finite M. The final hull H contains M union X, where X is the union of retained precision carriers. Consequently fixed H bounds every covariance-chain index and primitive spatial label. The external trace-log series has the same property. No hidden index excursion or change of support reserve is required.

Fifth, apply order bookkeeping to primitive positive weights: B_Y -> z B_Y, w_Y -> z w_Y, q_i -> z q_i. Strict budgets permit |z|<=1+delta. Every nonempty logarithm polymer contains a w or q occurrence, Mayer repetitions repeat those marks, and covariance forest edges number at most the molecule count minus one. Inverse and determinant density expansions count every B occurrence. Thus all remaining orders have a uniform O((1+delta)^(-k)) tail. For fixed H and bounded order there are finitely many label choices. Their Gaussian and BKAR integrals converge by the common accretive density majorant with sharp indicators untouched. Final anchored cardinality weights control large H and winding contributions when passing scalar totals on compact fields.

Sixth, choose the near-minimal Y and D in Section5 already translation-covariant, using the norm-preserving averaging theorem, and set X=Y+D. This preserves both the budget argument and the compatible linear core/tail assignment. The quotient Lipschitz estimates (5.1)-(5.2) follow as stated.

Finally, here is the full varying-input extension. Let finite E_N have exactly invariant normalized totals, uniform strict budgets and a locally normal limit E. Sections3-4 apply directly to this sequence, giving a local output family; they use local input convergence and uniform tails, not just canonical periodization. To identify its class, average E_N over the finite cell-translation group. This does not increase the norm and leaves its finite raw total exactly unchanged: normalized translation invariance implies raw invariance because zero is fixed. Extract a locally normal subsequence of these covariant averages, with limit E_cov. Analytic interaction compactness applied to their identical finite normalized totals gives [E_cov]=[E]. The averaged inputs and Per_N E_cov both converge locally normally to the same covariant family, so the local continuity theorem gives identical canonical limiting output families. Original and averaged inputs give identical finite output normalized totals, hence their limiting output classes agree. Therefore the original output class is F([E]), independent of the averaging subsequence. Canonical arrays themselves need not agree.

Induction now identifies every fixed finite number q of actual homogeneous local steps with the corresponding limiting quotient-map composition, provided every intermediate input stays in the uniform budgets and the classical systems and compatible regulators are chosen jointly. All intermediate cutoffs, Gaussian integrations, generated corrections and separately tracked vacuum factors remain present. This is finite-history compatibility; no infinite trajectory, invariant ball, mixed-history integration or full Wilson measure is concluded.
