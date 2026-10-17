# Auxiliary Gaussian grouping and recovery of a fixed support weight

Research proof candidate, 17 October 2026. This note separates the physical/source averaging ratio L from an auxiliary Gaussian grouping size J. It proves a consistent finite-step recovery of a fixed support-cardinality exponent for inherited and newly generated activities. It does not prove contraction of their amplitudes, stability of analytic radii, or a quantum RG induction. All constants are uniform in old refinement M and volume once the finite integers L,J have been selected; they may be very large functions of L,J.

One parameter correction is essential: Notebook18 requires 0<kappa_G<m_G. The choice kappa_G=2,m_G=1 would make its edge sum diverge. We use kappa_G=2,m_G=3 throughout, so the required covariance/precision weight is gamma_G=kappa_G+2m_G=8. This does not change its output cardinality reserve or the interaction re-entry weight below.

## 1. Four graphs and a fixed order of parameter choices

The physical source averaging ratio remains the fixed odd integer L. The current unit lattice is Lambda_cur. Its source blocks have side L; their index graph is Lambda_src, also the unit graph of the next current lattice after rescaling physical lengths by L.

Choose a further odd integer J, conveniently J=L^j. The Gaussian integration cells are groups of J^d source blocks, of physical side JL in current units. Call their graph Lambda_G. After rescaling by L, these are J-blocks of the next current lattice. At *every* RG stage the inherited quantum carriers are J-blocks of that stage's unit current lattice; denote the current carrier graph Lambda_Q.

Thus the two relevant projections have different purposes:

    rho_J: Lambda_src -> Lambda_G,
    pi_L:  Lambda_Q   -> Lambda_G.                              (1.1)

The first groups J source blocks per axis and is used only on the Gaussian, classical-precision and stationary-background ingredients. The second groups L quantum carrier cells per axis and is the actual coarsening of inherited activities. Its fiber is L^d, independent of J.

Centered odd cubes are compatible: a centered JL cube is both the union of J^d centered L cubes and the union of L^d centered J cubes. The two smaller tilings need not be nested inside one another. Their common JL tiling is enough. We work on compatible tori whose periods are multiples of JL, or a cofinal family of such tori. Taking J=L^j ensures compatibility with the original hierarchy on sufficiently large members. This is a restriction to a compatible cofinal regulator family, not a claim for every short incompatible torus.

The fiber dimensions are

    D_G=J^d d(L^d-1)dim(g),
    D_bg=d(JL)^d dim(g),
    D_in=dJ^d dim(g).                                           (1.2)

They count, respectively, the retained Gaussian variables in a macrocell, all its current background variables, and the background variables of one inherited J-current carrier cell. No physical averaging, pivot or cutoff coordinate is altered by the regrouping.

Parameter order:

1. Choose L sufficiently large to satisfy the explicit inherited carrier inequality in Section6, using the fixed target exponent a0=1/16.
2. At this fixed L, the existing flat and classical theorems give positive source-graph decay exponents, with no need to know their large-L asymptotics.
3. Choose the odd auxiliary J=L^j large enough to meet the finitely many decay-conversion inequalities below.
4. With L,J fixed, choose the product background radius, the density parameter theta, the coupling ceiling and cutoff budgets. The radius can be very small. No radius self-map is asserted.

This order removes the earlier circular attempt to force L a0(L) large while a0(L) was known only to be positive.

## 2. Proved covariance regrouping without changing its spectrum

Let C_0 be the real baseline covariance in the original fixed-L retained source coordinates. The existing theorem gives lambda I<=C_0<=Lambda_0 I and, for some gamma_0>0,

    K_src(gamma_0)=sup_i sum_j exp[gamma_0 d_src(i,j)]||(C_0)_ij||<infinity,

with the same column bound, uniformly M and volume. Regard the same matrix as acting on the direct sums of its source fibers inside each J-block. Its spectrum is unchanged; the grouping is an isometric coordinate rearrangement, not an averaging or a new covariance.

For any i in macrocell A and j in macrocell B,

    d_G(A,B)<=d_src(i,j)/J+d.                                   (2.1)

The inequality follows coordinatewise from the block projection and holds with periodic distances. A macroblock operator obeys ||C_AB||<=sum_(i in A,j in B)||C_ij||. Consequently

    K_G(gamma):=sup_A sum_B exp[gamma d_G(A,B)]||C_AB||
       <=J^d exp(gamma d) K_src(gamma/J).                       (2.2)

The column bound is identical. Thus any desired fixed macro exponent gamma is available once gamma/J<=gamma_0. Its constant grows at most by the displayed fixed J^d factor and the old weighted norm. No new spectral gap or decay theorem for the source ratio JL is being assumed. In particular take gamma=8 for the strict Gaussian theorem.

## 3. Classical precision and interaction labels can be regrouped at higher weights

For an arbitrary terminal set X, graph Steiner length satisfies

    tau_G(rho_J X)<=2 tau_src(X)/J+d(|X|-1).                    (3.1)

To prove this, project a source metric spanning tree and use (2.1) on each of its edges, then use ell_src(X)<=2 tau_src(X). Since ell_G<=2tau_G, the conservative useful bound is

    ell_G(rho_J X)<=4 tau_src(X)/J+2d|X|.                      (3.2)

The slightly sharper direct projected-MST bound is not needed.

Notebook21 supplies the original classical precision decomposition

    A(V)=A_0+sum_X B_X(a|X),

where each B_X is complex symmetric, with rows, columns and background support in X. On a sufficiently small product ball and for some fixed sigma_0>0, it supplies, with any prescribed finite cardinality reserve A_card,

    sup_i sum_(X contains i) sum_(j in X)
       exp[sigma_0 tau_src(X)+A_card|X|] ||(B_X)_ij|| <= C_A b. (3.3)

The radius may shrink with A_card but sigma_0 can be kept fixed: its origin is the fixed-L linear locality exponent, not the support-cardinality reserve. The initial fixed-L conversion from current cells to source blocks is included here and costs only fixed L constants.

Group labels by X'=rho_J X and group matrix rows/columns by macrocell. The result is still individually symmetric and strictly supported in the original background variables of X'. Equations (3.2)--(3.3) show that the macro precision norm at gamma_G=8 is finite and O(b) if

    32/J <= sigma_0,          A_card>=64       (d=4).           (3.4)

For its absolute block row sum, summing over the at most J^d source row cells gives the bound J^d C_A b. The same column bound follows by symmetry. Coefficients with equal projected support may be summed absolutely. No reserve from an inherited quantum activity is used in this step: this is the classical precision, whose construction permits arbitrary fixed reserve.

The same projection applies to the classical action remainder and the fixed-range Haar, straightening-Jacobian and gauge multipliers. Their original classical/local coefficients admit whatever fixed cardinality reserve is needed. Therefore their macro interaction norm at the target weight exp[4|Y|+kappa_G ell(Y)] Kcal_theta^|Y| is available on a smaller independent background ball, and their small fluctuation estimates remain O_(L,J)(gR^3+gR+g^2R^2). These terms tend to zero with g for a logarithmic cutoff. They are not inherited quantum coefficients being granted a new reserve.

## 4. Stationary-background regrouping: the output maximum is kept inside the sum

The actual one-step physical stationary background has source-graph support families

    a_i(w)=sum_X u_(i;X)(w|X),
    sup_i sum_X exp[kappa_0 tau_src({i} union X)+A_st |X|]
                       ||u_(i;X)||_r <= C_Ast r,               (4.1)

for some kappa_0>0 and any prescribed finite A_st, on a corresponding uniform product ball. The output fiber at i contains the current links of one source L-block, and the input labels are next-current unit cells. This is the actual matched source branch, not a conveniently chosen gauge.

Group both these roots and the w cells into J-blocks. For a macro root I and a macro support Z define the vector whose i-th source component is sum_(X:rho_J X=Z) u_(i;X), for all i in I. Its norm is the maximum over the whole current-background fiber of I. Bound that maximum by the sum over i in I *before* the support sum. This gives at most J^d old rooted sums; taking a supremum before that sum would not justify the estimate.

For rooted supports the projection inequality is

    tau_G({rho_J i} union rho_J X)
       <=2 tau_src({i} union X)/J+d|X|.                       (4.2)

Therefore the macro family has exponent kappa_st=4 and bound

    sup_I sum_Z exp[4 tau_G({I} union Z)]||u_(I;Z)||_r
       <=J^d C_Ast r=:C_st r                                (4.3)

provided 8/J<=kappa_0 and A_st>=16 in dimension four. Again the required reserve belongs to the classical stationary family, where it is available. One can add any fixed macro cardinality reserve by increasing A_st. The constants and radius depend on L,J, but not on M or volume. The actual number D_bg in (1.2) still appears later when a general quantum activity is Taylor-expanded; the Banach output maximum does not erase it.

## 5. New Gaussian and normalization terms have a common reserve 1/2

Choose kappa_G=2,m_G=3, gamma_G=8. The strict-support Gaussian theorem then gives connected macro activities with

    a_G=min(1/2,kappa_G/4)=1/2.                               (5.1)

Tune theta=1/(4D_G), so log Kcal_theta<=5/8. The new precision smallness conditions depend on theta, the macro weighted covariance norm and its inverse constants; Section3 gives an O(b) norm, so all can be met by shrinking b with fixed L,J. The edge constant worsens, but is finite. The actual product of retained link/color-ball cutoffs is unchanged. Its macro bad event is contained in {||xi_macro||_2>R}, so the joint Gaussian tail at the same threshold R bounds it. The good-event implication ||xi_macro||_2<=sqrt(number retained links)R cannot be used to improve the bad-event threshold. The chart displacement uses the original link supremum R.

The complete generated correction also has two fluctuation-independent normalization terms. They cannot be omitted from the activity space.

### 5.1 The pivot-delta normalization

The normalized logarithm log[D(V)/D(1)]=-sum_c Tr log pi_c(V) consists of fixed source-range analytic functions. After macro grouping each reads at most a fixed number of neighboring macrocells; the number of source terms anchored in a macrocell is O(J^d). It has an O_(L,J)(b) anchored norm with any fixed macro support weight, including a_G=1/2. This follows directly from its local formula, not from reusing an old low-weight quantum family.

### 5.2 A fresh macro determinant-chain decomposition

Let B=sum_Y B_Y be the regrouped local precision perturbation and C_0 the regrouped baseline. On a product ball with K_gamma nu_gamma<1, where gamma=8,

    Q(V)=-(1/2)log det(A(V)A_0^-1)
        =(1/2)sum_(n>=1)(-1)^n/n Tr[(C_0 B)^n].               (5.2)

Expand every B into its symmetric local labels. Join each label Y by a deterministic minimizing tree and each covariance endpoint pair by a shortest macro path. The closed matrix chain joins all these graphs into a connected declared carrier H. If T is the sum of all these lengths and b_1 its initial matrix index, then

    |H|<=T+1,       z in H implies d_G(z,b_1)<=T.              (5.3)

Fix a_Q=1/2 and delta_Q=1; a_Q+delta_Q=3/2<gamma. Consequently

    1_(z in H)exp(a_Q|H|)
       <=exp(a_Q) exp[-delta_Q d_G(z,b_1)] exp(gamma T).       (5.4)

The block trace is bounded by D_G times the product of block operator norms. At fixed b_1, summing the weighted length-n chain, and dropping its final closing constraint only in the positive majorant, is at most D_G(K_gamma nu_gamma)^n. This follows by alternating the covariance weighted row sum and the precision-label weighted row sum. Since tau(Y)<=ell(Y), the latter supplied norm pays every internal label tree. Summing b_1 in (5.4) gives S_deltaQ. Thus the connected determinant coefficients satisfy

    sup_z sum_(H contains z) exp(|H|/2)||Q_H||
       <=(D_G/2) exp(1/2) S_1
                    sum_(n>=1)(K_gamma nu_gamma)^n/n
       <=(D_G/2) exp(1/2) S_1 K_gamma nu_gamma/(1-K_gamma nu_gamma).
                                                                    (5.5)

Every coefficient reads only the union of its precision-label backgrounds, a subset of its declared H. The constant baseline carries no hidden background. Absolute convergence proves the equality and holomorphy. This is a rerun of the closed-chain proof on the macro C_0/B data; it does not amplify an old determinant expansion with only a small fixed reserve. It proves the needed common a_Q=1/2 with a finite O_(L,J)(b) norm. All field-independent Gaussian determinants and powers of g remain the separately tracked vacuum normalization.

Combining these terms with the cutoff/integration coefficients gives a new macro correction with reserve a_G=1/2 and norm epsilon_new bounded by O_(L,J)(b)+the stated Gaussian-expansion bound. Its smallness and iteration are separate from the support exponent.

## 6. Inherited interactions: the relevant projection remains ratio L

Assume the inherited quantum activities have connected carriers H in Lambda_Q, product background radius b, and norm

    sup_i sum_(H contains i)exp(a0|H|)||E_H||_b<=epsilon_old,
    a0=1/16.                                                    (6.1)

Use the actual source insertion F(a,g xi), and keep a independent during Gaussian integration. The proved directional Cauchy bound from `inherited_quantum_reentry_research.md` gives

    ||Delta E_H|| <= u ||E_H||_b,
    u=C_ch(L)|g|R/[b-b_- - C_ch(L)|g|R],                         (6.2)

on the stated positive chart margin. It has no J-dependent coordinate-count factor. The source chart itself still has ratio L; J groups its variables, not its equations.

Nonpivot outputs remain bond-local. Each pivot output reads only its two source L-blocks. After grouping those blocks into JL macrocells, the additional dependencies can add at most an adjacent macrocell to the one containing the original pivot. Since every source pivot starts in a unique macrocell, at most d outward neighboring macrocells can be added per projected block. Thus, for chi=d+1,

    Y(H) connected,     |Y(H)|<=chi|pi_L H|,
    1_(B in Y(H))<=sum_(i in H)1_(d_G(B,pi_L i)<=1).            (6.3)

This remains true even though source L-blocks and inherited J-current cells are not nested: both refine the same JL macrocell. The anchor multiplicity is N_near L^d, N_near=2d+1, with no extra J^d. The compression lemma is applied to H in the J-current carrier graph and pi_L of ratio L:

    |pi_L H|<=2^d+(2^d/k_L)|H|,
    k_L=1+floor((L-3)/4).                                      (6.4)

For kappa_G=2 and theta=1/(4D_G), the target coefficient is

    B_req=4+log Kcal_theta+kappa_G<=53/8.                       (6.5)

Therefore the inherited interaction weight is paid if

    (chi 2^d/k_L)(53/8)<=1/16.                                (6.6)

In dimension four, chi=5, so k_L>=8480 suffices. For example L=33921 attains equality, while L=33925 gives a strict margin. These deliberately crude integers only demonstrate a finite consistent choice; no useful numerical coupling bound is claimed.

After grouping equal Y, put Q_Y=sum_(H:Y(H)=Y)Delta E_H. As in the already audited conditional bridge,

    V_max=u N_near L^d epsilon_old,
    epsilon_int<=exp(V_max)u exp[(53/8)chi2^d]
                                      N_near L^d epsilon_old.       (6.7)

The full multiplier bound uses exp(||Q_Y||)||Q_Y||, not an ungrouped e_H bound. This is a finite O_L(epsilon_old gR/(b-b_-)) estimate on a smaller chart domain. The inherited and base factors can share a support as distinct labels. Under the previous quarter budgets their connected-log difference is bounded by 4 C_out epsilon_int. The exact fluctuation-independent old sum E_H(a) stays outside that integral.

Choosing L first in (6.6) is legitimate here because a0 is the fixed exponent recovered in Section7, not the unknown original a0(L). Only after fixing L do we choose J to amplify its positive primitive decay rates. This is the point of the auxiliary grouping.

## 7. Both new and inherited background terms return to exponent 1/16

The stationary macro family (4.3) has exponent kappa_st=4. Let b_common>0 be a common radius no larger than b_- from Section6 and every product radius on which the new Gaussian, determinant and delta-normalization coefficients are known. In particular b_common<=b, the inherited outer radius. Restricting the old activities to this smaller product ball preserves their norm bound. The outer radius b used in the inherited directional Cauchy estimate must not be silently assigned to the new coefficients, which were constructed only on b_- or a smaller common domain. Choose the quantum transport parameters

    beta=1/8,  a_out=mu=1/16,  delta_tr=1,
    t=s(r)/b_common=C_st r/b_common <=1/(16 D_bg).                 (7.1)

Then beta+delta_tr<=4 and alpha_Dbg(t)=D_bg log(1/(1-t))<=1/8. Newly generated Gaussian, determinant and delta-normalization activities already have carriers in Lambda_G and input reserve 1/2. Identity-projection transport gives output norm at most

    S_1 epsilon_new                                             (7.2)

at the required exponent a_out=1/16 (and the additional spatial weight mu). Their labels are J-blocks of the next current lattice, exactly the type of (6.1) at the next stage. There is no additional regrouping of these quantum coefficients and no spending of their reserve to amplify a spatial exponent.

The old fluctuation-independent term has a different indexing and must be included. Its input carriers lie in Lambda_Q, so its stationary transport uses pi_L, not the identity. Every old J-current output fiber is a restriction of its containing pi_L macro output fiber, so it inherits the same rooted bound (4.3), anchored at pi_L(i). Apply the compressed version of the exact transport theorem to the old activity restricted to b_common, with c0=2^d,c1=2^d/k_L and D=D_in. Its coefficient cost obeys

    c1 beta+alpha_Din(t)
       <=2/k_L+1/(8L^d) < 1/16                              (d=4)   (7.3)

for the chosen L, because D_in/D_bg=L^-d. Therefore the old term also returns to exponent 1/16, with norm at most

    exp(beta 2^d)L^d S_1 epsilon_old
       =e^2 L^d S_1 epsilon_old                              (d=4).  (7.4)

Its field-independent constants are tracked separately as vacuum terms, exactly as in the earlier transport theorem. No inherited quantum reserve beyond (6.1) is used. This direct compressed transport is necessary: treating the old term as if it already had reserve 1/2 on Gaussian macrocells would be unjustified.

The full updated correction is thus a connected activity family on J-blocks of the next current lattice with the same fixed exponent a0=1/16. A bound of the form

    epsilon_next <= e^2 L^d S_1 epsilon_old
                   +S_1 epsilon_new                           (7.5)

holds on the common smaller product domain, with the inherited fluctuation correction already included in epsilon_new via (6.7). This is recovery of the function-space weight and a bounded one-step estimate, not a contractive amplitude recursion.

## 8. Explicit sufficient choices of J and the remaining open domains

At the fixed L selected in (6.6), let gamma_0 be the baseline covariance exponent, sigma_0 the classical precision support exponent and kappa_0 the stationary-family exponent. All are positive by the already proved fixed-L theorems. It is sufficient to choose J=L^j so large that

    8/J<=gamma_0,
    32/J<=sigma_0,
    8/J<=kappa_0,                                               (8.1)

with strict inequalities if spare decay is convenient. Choose the classical cardinality reserves at least 64 for the precision and 16 for the stationary family, and any further fixed amount demanded by the classical interaction projection. Their construction allows this after shrinking the background radius. Equations (8.1) have a finite solution without knowing the large-L behavior of gamma_0,sigma_0,kappa_0, because L is already fixed. The constants in (2.2)--(7.5) are then fixed independently of M and volume.

The construction still does not give a stable analytic ball. In particular (7.1) asks for

    r<=b_common/(16D_bg C_st),    C_st=J^d C_Ast,                (8.2)

in addition to every previous chart/covariance radius. The old activity domain b may itself be the output of a previous step. No theorem here makes this radius loss a self-map or compares it with the actual running coupling domains. Smooth pre-gauge representatives and gauge-invariant analytic germs may help, but their fluctuation-integral and activity-norm interfaces remain separate.

Nor does (7.5) control amplitudes over arbitrarily many steps: its constant exceeds one, and the normalization contributions are O(b), not automatically O(g). Vacuum/relevant/marginal extraction and a coupling-flow estimate are still needed. The large-field complements, mixed histories and observable bounds are untouched.

What is settled conditionally on the already proved homogeneous classical ingredients is narrower and useful: one can fix L,J once, use the exact source coordinates and cutoff, and preserve one fixed positive connected-carrier exponent through the inherited fluctuation insertion, normalized Gaussian integration, determinant/delta normalization, and stationary transport. The previous circular support-weight test can be resolved by this auxiliary grouping without granting arbitrary reserve to quantum activities. The analytic-domain and amplitude induction remain open.
