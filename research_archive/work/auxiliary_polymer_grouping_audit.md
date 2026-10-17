# Independent derivation: auxiliary grouping closes the carrier-weight test

17 October 2026. This note independently derives the proposed auxiliary grouping result and audits the complete `auxiliary_gaussian_grouping_research.md` candidate. The physical ordinary-average/source blocking factor remains L. No renormalization map, source pivot, integration variable, or sharp cutoff is replaced. The result addresses the support-weight budget of inherited interactions; stable analytic domains and a complete quantum induction remain separate.

## 1. Conclusion and parameter order

The proposed route is valid under the already proved fixed-L, uniform-in-refinement classical and covariance inputs. It removes the particular unverified requirement that the original connected activity exponent a0(L) decay slowly enough as L grows. One may instead:

1. Fix an odd physical source factor L with k_L>=8480; the concrete choice L=33919 suffices.
2. Use the positive covariance, precision-localization and stationary-map exponents already established for this fixed L.
3. Choose a fixed odd auxiliary J, for example a sufficiently large power of L, to amplify all needed spatial exponents in auxiliary-cell units.
4. Choose the finite classical cardinality reserves required below, then shrink the independent background ball.
5. Set the Gaussian theorem exponents kappa_G=2 and m_G=3, use its tunable parameter theta=1/(4D_macro), and choose the coupling/cutoff within the resulting finite fixed budgets.

The Gaussian connected-support exponent is then 1/2, and stationary transport can return an exponent 1/16 in the same type of auxiliary carrier at the next scale. The inherited-interaction support test is satisfied by the chosen L. Constants and radii may be extremely unfavorable; this is an existence of fixed finite parameters, not a practical or uniform-in-L estimate.

## 2. Three nested partitions and the exact regulator

Current unit sites have two relevant cell partitions. The source Gaussian coordinates are grouped first into the physical L-blocks. Auxiliary Gaussian cells are unions of J^d such source blocks, hence have physical current side JL. Inherited activities are carried by J-blocks of current unit sites. A JL block is also the union of L^d such inherited J-blocks.

For centered odd cubes this nesting is exact: the union of odd J-blocks with centers J r, |r_mu|<=(L−1)/2, is the centered JL block, and likewise with J and L interchanged. Thus no boundary collar or partial cell is required. Under the physical rescaling by L, an auxiliary Gaussian JL block becomes a J-block of the next-current lattice. Repeating the next step therefore projects inherited J-block carriers to Gaussian JL-block carriers at ratio L, not at ratio JL or J.

The exact source tori must remain compatible with these partitions. Taking J=L^j, for a fixed integer j, preserves the original periods 2L^N whenever N is sufficiently large for the desired number of steps. For any fixed finite number of integrations this is a cofinal subfamily of the original thermodynamic regulators, not a new torus family. The same finite-block estimates apply at every step for which the remaining current periods are divisible by JL. This does not by itself deal with final small infrared volumes or assert a full finite-volume induction to the last scale.

The auxiliary Gaussian dimension and background dimension are

    D_macro=J^d d(L^d−1) dim(g),
    D_bg,macro=J^d dL^d dim(g).

Both are fixed after L,J are selected and remain independent of prior classical refinement M and volume. Grouping changes neither the Euclidean inner product on the retained coordinates nor the Gaussian spectrum.

## 3. Covariance decay after grouping

Let C_ij be the source-cell covariance blocks and assume a uniform weighted source Schur bound K_sigma at a positive exponent sigma. For source cells i in macro A and j in macro B,

    d_macro(A,B) <= d_source(i,j)/J+d.

For any gamma with gamma/J<=sigma, regard C_AB as an operator between direct sums of source-cell fibers. The elementary estimate ||C_AB||<=sum_(i in A,j in B)||C_ij|| gives

    sup_A sum_B e^(gamma d_macro(A,B)) ||C_AB||
       <= J^d e^(gamma d) K_(gamma/J).

The column bound is identical. This proof is intentionally conservative but avoids an unstated dimension-independent block norm comparison. It works with compatible periodic distances as well.

The source spectral sandwich lambda_L I<=C<=Lambda_L I is exactly preserved. Consequently any prescribed finite macro Schur exponent is available by taking J sufficiently large after L. In particular, the strict Gaussian choice kappa_G=2, m_G=3 requires the baseline weight kappa_G+2m_G=8; a sufficiently large J supplies it. The strict inequality kappa_G<m_G is respected. The invalid choice m_G=1 would not meet that theorem and is not used here.

All enlarged Schur constants are finite and uniform in M and compatible volume. They may grow rapidly with L and J, which only tightens the later smallness thresholds.

## 4. Regrouping the strictly local precision and classical interactions

Let tau denote graph Steiner length. For a finite terminal set X in source-cell units, terminal-tree projection gives

    tau_macro(pi_J X) <= 2 tau_source(X)/J+d(|X|−1).

Indeed project a source terminal metric spanning tree, use the preceding distance inequality on each edge, and use ell_source(X)<=2 tau_source(X). Also ell_macro<=2 tau_macro. Thus the conservative bound

    ell_macro(pi_J X) <= 4 tau_source(X)/J+2d(|X|−1)

is sufficient. The strict precision weight 8 ell_macro is paid by a source spatial exponent at least 32/J and a source cardinal reserve at least 16d, which is 64 in dimension four. A direct terminal-MST estimate can improve these constants, but no improvement is needed.

The Notebook21 classical precision decomposition has arbitrary fixed source cardinal reserve on a sufficiently small product background ball. Choose J so that 32/J is below its available positive spatial exponent, then choose the stated finite cardinal reserve and reduce the background radius. Group labels by pi_J X and sum the original matrix entries into macro blocks. The same sum over J^d possible output source cells as in Section 3 bounds the resulting anchored matrix-label norm. Symmetry and strict dependence on the declared background cells are preserved. Its norm remains O_(L,J)(b), so the full tunable strict precision smallness conditions can be met on a smaller positive ball.

The classical, Haar, straightening and gauge interactions are treated with their already proved arbitrary-cardinality bounds. For example, using the conservative projection inequality, the macro multiplier weight

    exp[(4+log Kcal_theta)|pi_J X|+2 ell_macro(pi_J X)]

costs at most source spatial weight 8/J and cardinal weight 4+log Kcal_theta+4d. The same source reserve 64 is more than sufficient in d=4 after tuning log Kcal_theta<=5/8. Grouped logarithmic exponents must be exponentiated with the explicit exp(sup grouped exponent) factor; choosing g small makes that factor bounded, as in the earlier inherited-interaction audit.

The background-only delta normalization and Gaussian logdet correction should be included at the same macro output exponent before transporting the total correction. The former is finite-range in source cells: each pivot determinant reads two adjacent source blocks, hence at most two adjacent macro cells, and at most O_d(J^d) source pivots contribute to a fixed macro anchor. Its exponent-1/2 norm is therefore O_(L,J)(b).

For the logdet, expand Tr log(I+C_0 B) into closed chains, retaining every local precision label. Join each covariance edge by a shortest macro path and join each precision support by a terminal spanning tree. A resulting connected hull has at most 1+T vertices, where T is the sum of covariance distances and internal support-tree lengths. If a hull contains an anchor z, its distance to the selected first chain index x is at most T. For output exponent a=1/2 and a re-rooting reserve delta=1/2,

    1_(z in hull) exp(a|hull|)
       <= exp(a) exp(−delta d(z,x)) exp[(a+delta)T].

The weighted matrix-label sums bound the remaining ordered n-chain by (K_1 nu_1)^n, and the trace costs at most D_macro. Summing x gives the finite lattice sum S_(1/2); summing n with its 1/n coefficient gives a bound of order D_macro S_(1/2)[−log(1−K_1 nu_1)]. This is O_(L,J)(b) when K_1 nu_1 is small. The available precision and covariance weight 8 is more than sufficient. Thus these separate background factors have the same macro output exponent 1/2. They are not literally terms supplied by the Gaussian fluctuation-log theorem and should be stated separately in an assembled proof.

## 5. Regrouping the actual stationary support series

The stationary map has a rooted source family on the graph of next-current unit cells. Its output at a source root i is the complete old-current L-block background fiber. Suppose its fixed-L bound is

    sup_i sum_X exp[sigma_s tau({i} union X)+A|X|] ||a_i;X||_r <= C_A r,

for any prescribed finite A on a suitably smaller r-domain. This is the already proved actual stationary series, not a consequence inferred from one-weight response bounds.

Group both output roots and input cells into J-blocks. Define each macro coefficient by putting all source output entries with pi_J(i)=A into one vector and grouping input support labels by Y=pi_J X. Then

    tau_macro({A} union Y) <= 2 tau_source({i} union X)/J+d|X|.

For a desired macro rooted exponent kappa_s, choose 2kappa_s/J<=sigma_s and an old cardinal reserve at least kappa_s d plus any desired new reserve. The sum over supports of the maximum over the J^d output roots is bounded by the sum over those roots. Therefore the precise safe macro bound has a factor J^d C_A r.

This factor must not be omitted by interchanging a root supremum with a support sum. It only worsens a fixed constant and the final radius. Each grouped support coefficient still vanishes at zero. The macro background map is the same actual stationary map, with a positive rooted exponent at least 2 available after choosing J.

## 6. Fixed output carrier exponents

Apply the strict tunable Gaussian theorem with kappa_G=2 and m_G=3. Its connected macro-carrier exponent is

    a_G=min(1/2,kappa_G/4)=1/2.

For the ensuing stationary substitution, Gaussian macro roots and next-current J-block roots are the same graph. Thus the projection is the identity and its fiber factor is one. The full scalar coordinate count is D_bg,macro, not D_macro. Use a common input radius b_common no greater than the independent background radius b_- and every radius available for the new Gaussian and normalization coefficients. The old inherited activities may be restricted to this same ball without increasing their norm. Their original outer radius b, used to obtain the directional fluctuation margin b−b_-, is not automatically a domain of the new coefficients. This distinction was requested in the audit and adopted in the candidate.

Choose output cardinal and spatial exponents a_out=mu_out=1/16, so beta=a_out+mu_out=1/8. With a stationary rooted exponent at least 2 one may choose delta=1/2. Then beta+delta<=2. On a small enough coarse domain enforce

    t=s(r)/b_common <= 1/(16 D_bg,macro).

Since t<=1/2,

    D_bg,macro log(1/(1−t)) <= 2D_bg,macro t <=1/8.

Hence beta plus this Cauchy cost is at most 1/4, strictly less than the input a_G=1/2. The transport theorem therefore yields connected J-block activities with the fixed reserve a0,out=1/16, independently of L and J. Its norm constant and permitted radius are not independent of those parameters. The output also retains the stated positive spatial exponent, though only its cardinal reserve is needed for the next compression test.

There is a separate transport for the fluctuation-independent inherited term E_H(a_*(w)). Its input carriers are already J-blocks of the current lattice, so its projection to next-current J-blocks has ratio L and fiber L^d. It must not be treated as the identity projection used for the new Gaussian output. Restricting the macro background family to an individual input J-cell gives a rooted family anchored at its projected macro cell, with the same safe family bound. The coordinate count is D_input=dJ^d dim(g).

The compressed transport theorem uses c0=2^d and c1=2^d/k_L. To return the same output reserve and spatial exponent 1/16, its budget is

    c1(1/8)+D_input log(1/(1−t)) <=1/16.

For d=4 and k_L>=8480, choose t<=1/(64D_input); then the second term is at most 1/32 and the first is 2/k_L<1/32. The same positive rooted exponent pays the attachment trees. Hence this old background term also returns reserve 1/16, with norm constant at most exp((1/8)2^d)L^d S_(1/2) times its input norm. Its radius must be reduced to meet this additional condition. This step is necessary for a support-weight loop for the total correction; it remains a bounded, generally noncontractive transport.

## 7. Inherited source geometry on the persistent J-block lattice

At the next step, an inherited carrier H consists of J-blocks of current unit sites. Its activity reads at most dJ^d dim(g)|H| scalar coordinates. Directional Cauchy remains a value estimate and does not introduce this coordinate count.

A nonpivot source output reads its own link. A source pivot reads the two endpoint physical L-blocks. Every such L-block is contained in a Gaussian macro JL block. If the pivot starts in a macro A, its second endpoint block is either still inside A or inside the forward neighboring macro A+e_mu. This statement uses the nested partitions in Section 2 and does not require replacing the physical L-pivot by a new JL-pivot.

The declared macro carrier is therefore the projection pi_L H, plus at most its forward neighbor in each direction for the source pivots that cross macro interfaces. It is connected and satisfies

    |Y(H)| <= (d+1)|pi_L H|.

Here pi_L acts on the inherited J-block index graph, with ratio L. The anchor inequality consequently costs at most (2d+1)L^d input J-cells. There is no additional J^d anchor factor in this inherited-interaction step. The root-family J^d cost in Section 5 is a different regrouping operation.

The original retained window is unchanged: in a macro cell it is the product of its linkwise color-ball indicators. A bad macro cell implies that its full Euclidean norm exceeds the same link threshold R, so the joint Gaussian tail with dimension D_macro and threshold R applies. The chart displacement bound still uses the original link supremum and constant C_ch(L), not a Euclidean norm growing with J.

## 8. The formerly open inequality is now satisfied

For the macro Gaussian theorem choose

    theta=1/(4D_macro).

The tunable strict density cost obeys log Kcal_theta<=5/8, so with kappa_G=2,

    B_req=4+log Kcal_theta+2 <=53/8.

The inherited re-entry inequality on the J-cell carrier graph is exactly

    [(d+1)2^d/k_L] B_req <= a0,out.

In d=4 and with a0,out=1/16, it is sufficient that

    (80/k_L)(53/8) <=1/16,
    equivalently k_L>=8480.

Since k_L=floor((L+1)/4) for odd L, L=33919 satisfies it. This L is chosen first. The possibly very small positive fixed-L spatial exponents then determine how large J must be; they need no quantitative lower bound as L varies. The use of arbitrary finite classical cardinal reserves is essential to this order of choices.

The covariance-edge constants, the local precision neighborhood, the bad-cell tail threshold, and all norm conversion constants are fixed only after L and J are chosen. They are finite. Shrinking b and then g supplies their required smallness because b can tend to zero, R(g) can grow, and gR(g)^3 can tend to zero. None of those choices asserts that an actual running coupling sequence meets the budgets at every scale.

## 9. Remaining scope

This closes a support-weight compatibility test for a persistent auxiliary carrier convention, rather than merely assuming that a0(L) has a favorable large-L asymptotic. It does not prove a contraction of the inherited background term, a stable common analytic radius, or a full RG induction. The stationary transport still shrinks its sufficient domain by constants involving J^d and D_bg,macro. The multiplier and projection constants can be enormous. Relevant and marginal extraction, running coupling estimates, the handling of final small volumes, large fields, and observables remain separate.

The complete candidate was read after this independent derivation. Its choice kappa_st=4 and delta_transport=1 is stronger than the sufficient choices above; its common t<=1/(16D_bg,macro) simultaneously pays the old background Cauchy cost by alpha_Dinput<=1/(8L^d). Its fresh macro determinant proof and separate pivot-delta proof agree with Section 4. The proposed choices L=33921 (sufficient equality in the conservative test) or L=33925 (a spare margin) are valid; L=33919 above is only a slightly smaller sufficient odd integer.

One substantive domain-notation repair was adopted: the candidate now uses b_common, rather than the inherited outer radius b, in both transport steps and the final sufficient radius. It also explicitly identifies the old J-current output fibers as restrictions of their containing macro fibers. With these repairs, the full research candidate passes. No remaining geometry, matrix norm, support-norm, or parameter-order obstruction was found within its fixed-parameter finite-step scope. No output notebook was edited by this audit.
