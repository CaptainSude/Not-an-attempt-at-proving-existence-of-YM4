# Independent audit of the auxiliary Gaussian grouping proof

17 October 2026. Audited `auxiliary_gaussian_grouping_research.md` in full, with `auxiliary_polymer_grouping_audit.md` as the independent geometry check. No substantive mathematical correction is needed. This is an internal audit of the stated homogeneous finite-step result, not certification of a quantum Yang--Mills construction.

## 1. The graph and measure changes are legitimate

The physical averaging ratio stays L. The two different auxiliary partitions, current J-cells and source-Gaussian JL-cells, are both compatible with the centered odd JL partition. Source L-cells and current J-cells need not refine one another. Taking J=L^j preserves a cofinal compatible family of the original source tori; the stated restriction to stages with remaining periods divisible by JL is necessary and present.

The Gaussian operation is an isometric rearrangement of retained coordinates. Its spectrum and Euclidean normalization are unchanged. The displayed dimensions D_G, D_bg and D_in are distinct and correct. The inequality

    d_G(A,B)<=d_src(i,j)/J+d

and the conservative macroblock norm estimate yield exactly J^d exp(gamma d) K_src(gamma/J). No hidden J^d factor is omitted from the row sum, and no refinement-dependent fiber factor appears. The tuning theta=1/(4D_G) is allowed to depend on the fixed grouping and does not claim a uniform large-J analytic radius.

## 2. Precision and stationary support conversion

The terminal-tree projection bound, followed by ell<=2tau, gives

    ell_G(rho_J X)<=4 tau_src(X)/J+2d|X|.

Thus macro precision weight 8 is paid by 32/J spatial decay and cardinal reserve 16d=64 in four dimensions. The old classical construction permits that fixed reserve while keeping a positive fixed spatial exponent and shrinking the product radius. Matrix symmetry and strict background/row/column support survive grouping. Summing constituent source rows produces the explicit J^d norm factor.

For the stationary family the rooted projection inequality is stronger, with 2/J and d|X|. Target exponent4 therefore requires 8/J and cardinal reserve16. The proof keeps the output maximum inside the support sum and then bounds it by the sum over the J^d original roots. This correctly produces C_st=J^d C_Ast. It does not confuse a maximum of family norms with a family norm of a joint maximum.

## 3. The two normalization terms are actually included

The pivot-delta logarithm is a finite source-range analytic sum. Its macro anchored multiplicity is O(J^d), and its norm is O_(L,J)(b) at any fixed macro weight. It is correctly treated separately from the fluctuation-log theorem.

The fresh determinant-chain argument is valid. One may choose a terminal metric spanning tree for each B_Y support, realize its edges by fixed shortest paths, and join consecutive covariance indices by fixed shortest paths. The cyclic matrix chain makes the union connected and contains the initial trace index b_1. If T is the sum of those edge lengths, the union has at most T+1 vertices. For a carrier anchor z, its distance from b_1 is at most T. Consequently

    1_(z in H) exp(|H|/2)
       <=exp(1/2) exp(-d_G(z,b_1)) exp(8T).

This handles anchors on newly added covariance paths as well as anchors in precision-label supports. It would not be enough to mark only precision labels containing z; the written proof avoids that error.

The precision norm at 8 ell(Y) pays each internal label-tree length, and the covariance norm at8 pays its joining paths. The absolute block trace is at most D_G times the product of block operator norms. At fixed b_1 the positive chain sum is bounded by D_G(K_8 nu_8)^n after dropping its closing constraint. Summing b_1 gives S_1. Thus the stated D_G exp(1/2) S_1/2 times the logarithmic series is correct, including its factor1/n and determinant sign. No cyclic-mark cancellation or unproved trace-class assertion is used on the finite regulators. Absolute convergence supplies coefficient holomorphy and strict dependence only on the union of the B_Y backgrounds. The field-independent determinant stays in the vacuum normalization.

## 4. Inherited increment geometry and numerical budget

Every nonpivot output is bond-local. A source pivot's two physical L-blocks lie either in the same JL macrocell or in forward adjacent macrocells. Hence each projected inherited J-cell carrier adds at most d forward macro-neighbors, giving chi=d+1. Its anchor multiplicity is (2d+1)L^d on the J-cell graph, without an additional J^d. This is a different operation from the stationary regrouping of Section2.

The directional Cauchy increment bound consumes the original source chart displacement in link supremum. It has no D_in factor. Grouped exponents require the displayed exp(V_max) multiplier factor; the proof includes it. The retained link/color-ball cutoff is unchanged, and a bad macrocell is contained in the Euclidean event with the same threshold R, not a threshold increased by the square root of its dimension.

The strict density estimate log Kcal_theta<=5/8, kappa_G=2, m_G=3 gives B_req<=53/8. The inequality

    (80/k_L)(53/8)<=1/16

is precisely k_L>=8480. The examples L=33921 for equality and L=33925 for strict margin are correct; L=33919 would also reach equality but minimality is neither needed nor claimed. Choosing L first, then an auxiliary J for its already positive decay exponents, removes the earlier unsupported appeal to favorable large-L behavior of a0(L).

## 5. Both parts of the background term return to the same space

For newly generated terms, D_bg t<=1/16 implies alpha_Dbg(t)<=1/8. Together with beta=1/8, this is below the available input reserve1/2, while beta+delta_tr=9/8 is below stationary exponent4. Identity-projection transport gives S_1 epsilon_new.

For the inherited fluctuation-independent term, the proof correctly uses pi_L, fiber L^d and coordinate count D_in. Since D_in/D_bg=L^-d,

    (2^d/k_L) beta+alpha_Din(t)
       <=2/k_L+1/(8L^d)<1/16.

The compressed transport therefore costs exp(beta 2^d)L^d S_1=e^2L^d S_1 in dimension four. It does not assume that this old term has reserve1/2 on Gaussian macrocells. Vacuum constants are separately accounted for.

These checks establish the displayed one-step amplitude bound and recovery of carrier exponent1/16 on the persistent J-cell convention. They do not make the amplitude bound contractive.

## 6. Scope

The proof needs only finitely many fixed cardinal reserves and positive fixed-L decay exponents. Its background radius, coupling ceiling, cutoff threshold and constants can all depend on L,J; after those are fixed, they are uniform in the prior classical refinement M and compatible volume. The proof explicitly retains the shrinking radius r<=b/(16 D_bg C_st), large amplitude factor, restriction on remaining torus sizes, and missing relevant/marginal, running-coupling, large-field and observable estimates. No stable common analytic domain or complete iterative quantum theorem follows from this audit.

No output files were edited and no compilation was run for this audit.
