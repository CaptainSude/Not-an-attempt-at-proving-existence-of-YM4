# Classical stationary substitution before Gaussian integration

17 October 2026. Research bridge. This note isolates the support estimates needed to use the Gaussian theorem directly with the next background w. It uses the existing arbitrary-reserve classical action families and a supported stationary map for a fixed composite ratio R. It does not assume arbitrary reserve for inherited quantum activities.

## 1. A precision composition lemma

On one fixed unit cell graph, suppose

    B(a)=sum_Y B_Y(a|Y)

is a symmetric precision perturbation, with each B_Y symmetric, matrix rows/columns in Y, and B_Y(0)=0. Let D be the finite scalar-coordinate count per a-cell and b_cl its independent analytic radius. Suppose

    sup_i sum_(Y contains i) sum_(j in Y)
      exp[sigma tau(Y)+A |Y|] ||(B_Y)_ij||_(b_cl) <= N_B.

Assume a_i(w)=sum_X u_(i,X)(w_X), u_(i,X)(0)=0, and its whole-cell maximum is inside the support sum:

    sup_i sum_X exp[kappa tau({i} union X)+a |X|]
      ||u_(i,X)||_r <= s(r).

At a fixed geometry, D is finite and all bounds may depend on it. Let 0<kappa'<min(sigma,kappa), choose A'>=0 with a>=A', and set t=s(r)/b_cl. If t<1 and

    A'+D log[1/(1-t)]+rho <= A,    rho>0,

then substitution gives symmetric strict pieces B'_Z(w|Z), with their matrix rows/columns in Z, and

    sup_i sum_(Z contains i) sum_(j in Z)
      exp[kappa' tau(Z)+A' |Z|] ||(B'_Z)_ij||
      <= N_B alpha_D(t) sup_(n>=1) n exp(-rho n),
    alpha_D(t)=D log[1/(1-t)].

In particular this is O(r) when s(r)=O(r) and the displayed margins are fixed.

Proof. Expand each entry of B_Y on its scalar-coordinate polydisc, with Cauchy coefficient bound ||(B_Y)_ij|| b_cl^(-|nu|). The zero multiindex is absent. For each occurrence of a coordinate rooted at k in Y, substitute its strict X-family. Declare Z=Y union all X. It contains all variable and matrix supports. The gluing inequality

    tau(Z)<=tau(Y)+sum_occurrences tau({k} union X)

and |Z|<=|Y|+sum |X| give the asserted spatial and cardinal weights. The absolute scalar multiindex sum is (1-t)^(-D|Y|)-1, bounded by alpha_D(t)|Y| exp(alpha_D(t)|Y|). The reserve rho pays |Y|. For a fixed nonzero matrix row i, necessarily i belonged to the original Y, and the only nonzero column indices remain in that Y. Hence no rerooting loss is required for this precision row norm. Taylor coefficients of a symmetric matrix are symmetric, so every constructed piece is symmetric. Absolute convergence justifies grouping equal Z. If the original decomposition only has sum_Y B_Y(0)=0, first subtract its individual constants, using their absolutely convergent zero sum and at most doubling the input norm.

This lemma concerns rooted-field support and the precision's weighted row sum. It does not infer a bound on sum_(Z contains i) ||B'_Z|| as whole global matrices.

## 2. Application at fixed composite ratio

First group the current-unit classical families into source R-block cells. The number of current variables in each such cell is finite because R is now fixed. Existing classical support constructions give the independent-background precision B(a)=A_M(a)-A_M,0 with arbitrary prescribed finite cardinal reserve, some positive spatial exponent, and constants uniform in old M and compatible volume. Fixed-range composite chart operations preserve this property, once the chart and old-M-uniform flat Gaussian have been established.

The actual stationary map a_*(w) is obtained from the supported pre-gauge map by the explicit fixed-R local analytic contour gauge. Banach-valued Cauchy composition supplies a rooted strict family with any fixed cardinal reserve, positive spatial exponent and norm O_R(r), uniformly in M. Its output fiber is the entire R-block field with maximum norm.

Apply Section1 with a sufficiently small radius r. The resulting precision is now a strict function of w, with the same retained matrix indices and a symmetric strict decomposition; its norm is O_R(r). The classical input radius b_cl is fixed independently of any inherited quantum radius.

Group source roots and w-cells by an independent J. The projection inequalities

    tau_macro(rho Z)<=2 tau_unit(Z)/J+d |Z|,
    ell_macro(rho Z)<=4 tau_unit(Z)/J+2d |Z|

show that a target macro precision exponent gamma=8 is paid by 32/J<=kappa' and A'>=64 in d=4. Grouping matrix rows costs at most J^d. Thus the strict Gaussian precision hypothesis holds with norm O_(R,J)(r), and its small theta-dependent neighborhood can be met by choosing the final fixed background radius b<=r after R,J have been selected. Nothing forces this b to be a fixed fraction of the inherited b at each later step: it is selected once.

## 3. Classical and measure multipliers with spectator fluctuations

The same support substitution can retain local xi as spectator variables. Let a classical or measure exponent family V_Y(a|Y,xi|Y) be holomorphic on a fixed independent-background ball, measurable on the actual retained cutoff, and bounded there in a fixed weighted family norm. The only dependence on xi is in Y. Substitute a_*(w) into its a-slots by the Taylor expansion, keeping every coefficient's xi-support Y. Join Y and all substituted w-supports by deterministic trees. These are strict joint (w,xi) carriers.

Here is an explicit anchored bound, including nonconnected Y. Suppose the source family has norm

    sup_i sum_(Y contains i) exp[sigma tau(Y)+A |Y|]
      ||V_Y||_(b_cl,cutoff) <= epsilon_cl.

Let rho_J group the source graph into J-cells. Join rho_J Y by a deterministic Steiner graph and attach each substituted rho_J X to the corresponding root rho_J k, k in Y. The resulting connected macro carrier K contains the entire xi-support rho_J Y, as well as every w-support. With T the sum of all joining lengths,

    |K|<=1+T,
    T <= (2/J)tau(Y)+d|Y|
         +sum_occurrences [(2/J)tau({k} union X)+d|X|].

An anchor z in K obeys d(z,rho_J Y)<=T. Thus a target cardinal weight B is paid, with a rerooting exponent delta>0, by

    2(B+delta)/J <= min(sigma,kappa),
    a >= d(B+delta),
    A >= d(B+delta)+alpha_D(t),    t=s(r)/b_cl<1.

The scalar multiindex factor is exactly exp[alpha_D(t)|Y|]. Summing anchors through the J^d source cells of a macrocell gives

    sup_z sum_(K contains z) exp(B|K|)||V'_K||
      <= exp(B) J^d S_delta epsilon_cl.

Every term is a strict joint (w,xi) function. The construction includes the zero Taylor term; an original xi-supported coefficient independent of w remains an interaction. These inequalities avoid assuming an unavailable large unit-graph spatial exponent: J is chosen after the actual positive fixed-R exponents, while the finite cardinal reserves are fixed in advance. No cardinal reserve is assumed for inherited quantum activities beyond their separate stated norm.

In particular the classical cubic remainder, local pivot logarithm, Haar density logarithm and gauge remainder retain their small factors

    O_(R,J)(|g| T^3+|g| T+g^2 T^2)

on the retained link threshold T, provided all chart and Taylor domains are respected. Apply exp(V_K)-1 only after equal-carrier exponents have been grouped; the anchored exponent bound bounds each ||V_K|| and gives the multiplier bound e^(Vmax)||V_K||. A logarithm independent of w but depending on xi is not a vacuum term.

This paragraph is a specialization of the existing strict classical integration and support-composition proofs. Its inputs are actual independent-background coefficient bounds, not a scalar bound on the summed exponent.

## 4. Output and limitations

The precision and base multipliers now read background w directly on the same auxiliary Gaussian graph. If the separate inherited joint-support estimate meets the Gaussian interaction budget, the Gaussian theorem outputs connected w-activities on next-current J-cells directly. It is unnecessary to transport those activities again through a_*(w). The determinant chain and local pivot-delta normalization can likewise be expanded with the stationary-substituted precision and actual stationary local functions on this graph.

This ordering preserves exact integration variables, covariance, normalization and cutoff; it changes only when a convergent support substitution is performed. All equality statements are initially on common small domains and then on their established holomorphic continuations.

This bridge addresses the shrinking-domain issue. It neither controls the inherited amplitude recurrence nor identifies the running gauge-action coefficient. The complete composite macrostep inputs and their joint-family and Gaussian estimates must be checked before this observation is promoted to a common-domain quantum-step theorem.
