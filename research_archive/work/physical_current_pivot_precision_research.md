# The physical current-step pivot chart and reduced precision

Research proof candidate, 17 October 2026. This note concerns the homogeneous periodic small-global-potential branch. It uses the proved classical action and ordinary minimizer of Notebooks 15–16 and the flat retained-coordinate Gaussian of Notebook 17. It does not assert the independent-free-current carrier or the mixed retained-history boundary version. No repository or output file was edited.

## 1. Statement and normalization

Set the current lattice spacing to one, the original spacing to 1/M with M=L^k, and the next spacing to fixed odd L. The original CMP109 convention has L>11; our local arguments work for odd L>=3. Use compatible periodic tori with the ordinary block/corridor geometry (in particular the usual source tori, with distinct interfaces). Count positive current bonds and trace-orthonormal real color coordinates once. All current pairings below are counting pairings. Transposes after complexification are bilinear; accretivity uses the Hermitian pairing.

Write S_M(a) for the coupling-free classical Wilson action evaluated at the Notebook15 ordinary minimizer with current datum V=exp(i a). Notebook16 proves, on a complex supremum ball independent of M and volume,

    m_M(a)=D S_M(a),       ||m_M(a)||_infinity <= C ||a||_infinity,
    H_M(a)=D² S_M(a),      ||H_M(a)-q_M||_kappa <= C_kappa ||a||_infinity.       (1.1)

Here ||.||_kappa is the maximum of the exponentially weighted absolute row and column sums, grouped into fixed-size cells. It is a matrix algebra norm. We choose kappa below the common locality exponent of Notebooks07 and16. Passing between current unit cells and fixed L-blocks changes constants/exponents by fixed factors only.

The flat source retained coordinates are z on all current bonds except the one middle-interface pivot p(c) for each next-coarse bond c. Their insertion is K_L, and the averaged root-to-site contour derivative is T_L. Notebook17 proves

    A_M,0 = K_L^T [q_M+T_L^T T_L] K_L,
    gamma_* I <= A_M,0 <= B_* I,
    ||A_M,0||_kappa + ||A_M,0^(-1)||_kappa <= C_*.                         (1.2)

All constants in this note may depend on L, dimension, the fixed color normalization and kappa, but not on M or volume.

**Conclusion.** There is an analytic choice of physical stationary background V_*(W), for each sufficiently small next-coarse datum W=exp(i w), such that

    M_L(V_*)=W,       P_V*(y,x)=1,       ||log(V_*)/i||_infinity <= C_L ||w||_infinity. (1.3)

Here P_V is precisely the averaged contour variable used in CMP109, not a chosen tree transporter. The exact source pivot chart Phi_V(z) is constructed below and keeps every retained coordinate unchanged. At V=V_* the actual action-plus-exponential-gauge Hessian in these coordinates satisfies

    ||A_M(V)-A_M,0||_kappa <= C_L,kappa ||log(V)/i||_infinity.              (1.4)

The Hessian includes the nonzero ordinary action gradient contracted with the second derivative of the constraint/exponential chart. Thus (1.4) does not discard the physical current term. Its inverse has a uniform weighted bound on a smaller ball. The same coordinates support the original retained-coordinate sharp cutoff without a change of its argument.

This is a statement about the classical Gaussian part of the actual homogeneous step. Haar density, the Jacobian of straightening, and the previously integrated interaction E_k remain in the interaction. The result does not prove those interactions satisfy the full source orbit-domain hypotheses.

## 2. Exact local source maps

Primary source: [Bałaban, CMP109, pp.253–255 and265–268, (0.11)–(0.16), (2.3)–(2.13)](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf). The deposited equations are Raw I 46952–47000 and Raw II 9045–9095, 73865–73945, at the pinned commit e392ef4. The formulas below specify the maps directly; our estimates do not import the deposit's general-background quantitative theorem.

For a block center y and x in its block, P_V(y,x) is the analytic group mean of the prescribed shortest root-to-x contour products. Its ingredients have the following properties near the identity: the group mean is analytic, its derivative at equal identity inputs is their arithmetic mean, and it is equivariant under multiplication at the two endpoints. Thus

    P_(V^u)(y,x)=u(y) P_V(y,x) u(x)^(-1),
    V^u(b)=u(b_-) V(b) u(b_+)^(-1).                                      (2.1)

All contour edges are internal to the block. Let c=(y,y+L e_mu), x'=x+L e_mu, and let R_c(V) be the straight transporter from y to y+L e_mu. The ordinary average of CMP109 (0.12) is

    U_x(V)=P_V(y,x) V([x,x']) P_V(y+L e_mu,x')^(-1),
    M_L(V)(c)=exp{ L^(-d) sum_(x in B(y)) log[U_x(V) R_c(V)^(-1)] } R_c(V). (2.2)

The logarithm is the small branch. Formula (2.2) is the ordinary rooted average. It is not the fixed-reference corrected average of Notebook13. It reads only the two endpoint blocks, their connecting parallel strings and the fixed reference string. In particular

    M_L(V^u)=M_L(V)^(u restricted to block centers).                       (2.3)

Define the relative maps, in the source's left-exponential bond coordinates,

    F_V(B;c)=(1/i)log[M_L(exp(i B)V)(c) M_L(V)(c)^(-1)],
    Grel_V(B;y,x)=(1/i)log[P_(exp(i B)V)(y,x) P_V(y,x)^(-1)].               (2.4)

They vanish at B=0. Put

    A_V=D_B F_V(0)=L Q_V^flat,       T_V=D_B Grel_V(0).                    (2.5)

The symbol A_V here denotes the rectangular linear constraint derivative; the reduced precision is always written A_M(V). At V=1 these derivatives are L Q_L^flat and T_L. In the source kernel convention

    (Q_V^flat B)(c)=sum_b L^(-d) Q_V^flat(c,b) B(b).                       (2.6)

All assertions below are valid on a common complex product ball in the link potential a=log(V)/i and fluctuation B. Analyticity is elementary here: each local map uses a fixed finite number of products, inverses, exponentials, local group means and logarithms on their common small domains.

### 2.1 The pivot incidence is exact, including nonlinear dependence

The pivot p(c) is the single current bond on the line through the two centers crossing their common block interface. No internal root contour contains any pivot. A parallel string or reference string for a different coarse bond c' does not cross this interface at this pivot: its orientation or its pair of endpoint blocks differs. Therefore the full nonlinear equation F_V(B;c) depends on p(c) and on no other pivot p(c'). This is a statement about the source graph, before linearization.

At V=1, the straight-string average contains p(c) for exactly L starting sites x: its transverse coordinates are fixed, while the longitudinal starting coordinate ranges over the first block. The rooted contour terms do not contain it. Its coefficient in Q_L^flat is L^(-d), and its coefficient in A_1 is L^(1-d). Consequently

    pi_c(V):=Q_V^flat(c,p(c))=I+O(||a||_infinity),
    h_V(c):=L^(d-1) pi_c(V)^(-1),       A_V h_V=I.                        (2.7)

The operator h_V inserts only at the pivot belonging to c. On a small fixed ball all pi_c are invertible and h_V is local and uniformly bounded. This is exactly the source right inverse, including its factor L^(d-1).

The linear constraint insertion K_V retains every nonpivot coordinate and inserts

    (K_V z)(p(c))=-pi_c(V)^(-1) sum_(b not a pivot) Q_V^flat(c,b) z(b).    (2.8)

Thus A_V K_V=0, K_1=K_L, and restriction to the nonpivots is a left inverse of K_V. Formula (2.8) has no missing L factor: the common L^(1-d) in A_V cancels.

## 3. Exact source straightening and its local estimates

Write F_V(B)=A_V B+C_V(B), with C_V(0)=D C_V(0)=0. The source map Dtilde_V satisfies

    Dtilde_V(B)=C_V(B-h_V Dtilde_V(B)).                                  (3.1)

For each output c, the right side depends on Dtilde(c) alone, since changing another pivot never changes F_c. A finite-dimensional contraction, or the analytic implicit function theorem with derivative I at B=0, solves (3.1) uniquely on a uniform small ball. There are finitely many local cell types, so the radius does not shrink with volume. Moreover the output Dtilde(c) reads only the input links and background links in the same two-block source neighborhood as F_c. Iteration does not spread the support to neighboring equations.

Set

    Phi_V(z)=K_V z-h_V Dtilde_V(K_V z).                                  (3.2)

Then

    F_V(Phi_V(z))=0,        Phi_V(z)(b)=z(b) for every nonpivot b.         (3.3)

This is the unique small solution of the nonlinear ordinary constraint for the specified nonpivot values. Consequently it is the source chart, not an alternative chart of the same fiber. The direct equation F_c(B)=0 solved for p(c) gives the same chart by uniqueness. Its exact first two derivatives at zero are

    D Phi_V(0)=K_V,
    D² Phi_V(0)[u,v]=-h_V D²F_V(0)[K_Vu,K_Vv]
                    =-2 h_V C_V^(2)(K_Vu,K_Vv).                         (3.4)

Here C_V^(2) is the symmetric bilinear coefficient whose diagonal is the degree-two homogeneous term, rather than the Hessian itself.

### 3.1 Quantitative local derivative bounds

For completeness, the finite-dimensional argument supplies uniform weighted bounds, not merely qualitative analyticity. Let N_L bound the number of scalar link/color coordinates read by any local output, and let I_L bound the number of output neighborhoods containing a fixed link. Both are finite and independent of volume. Let ell_L bound their current physical diameter. Shrink a product polydisc so that its closure lies in all the analytic domains above, and the implicit contraction has norm at most 1/2. Cauchy on a smaller polydisc bounds every coordinate derivative of total order at most three by a fixed C_L. In particular, with b=||a||_infinity,

    ||K_V||_kappa+||h_V||_kappa+||T_V||_kappa <= C_L,kappa,
    ||K_V-K_L||_kappa+||h_V-h_1||_kappa+||T_V-T_L||_kappa <= C_L,kappa b. (3.5)

For z in a fixed smaller ball, D_z Phi_V has finite range ell_L and weighted row/column norm at most C_L,kappa. Its coefficient difference from D_z Phi_1 at the same z is at most C_L,kappa b. At z=0 the sharper comparison is (3.5). Second derivatives have coefficient arrays supported on triples within distance at most 2 ell_L, with uniform absolute coefficient sums. Their difference from the corresponding V=1 arrays is O(b). The same statements hold for the first and second derivatives in the background variables and for mixed derivatives allowed by the order-three bound. Uniform boundedness of a second background derivative follows directly from Cauchy even when no difference estimate is requested.

Here is the elementary conversion used for those statements. If |D² f_r/(da_i da_j)|<=C_L and this coefficient can be nonzero only when i,j belong to a neighborhood of at most N_L coordinates, then

    |D²f_r[u,v]| <= C_L (sum_(i in N(r))|u_i|)(sum_(j in N(r))|v_j|).

For a bounded output field s, define the contracted Hessian H_s by <u,H_s v>=sum_r s_r D²f_r[u,v]. For each i, at most I_L outputs r contain i, and at most N_L choices of j occur for each r. Therefore

    ||H_s||_kappa <= C_L I_L N_L exp(2 kappa ell_L) ||s||_infinity.        (3.6)

The column estimate is identical (or follows from Hessian symmetry). First-derivative Schur bounds follow from the same incidence count. Background Lipschitz bounds follow by integrating the bounded next derivative along ta. These estimates explain why contraction against an extensive action gradient does not create a volume factor.

### 3.2 The sharp cutoff is kept in its actual coordinates

After the source scaling B=g K_V z, its relative original link field is exactly Phi_V(g z). Equation (3.3) gives

    Phi_V(g z)(b)=g z(b)   on every retained nonpivot link.               (3.7)

Thus a product of retained-link indicators |B'(b)|<r becomes exactly |z(b)|<r/|g|. It is not replaced by a norm of K_Vz or by a gauge-selected fine field. CMP109 p.267 explains that the separately bounded retained links imply bounds on the eliminated pivots, and CMP116 (2.3) specifies its retained-coordinate product. RawII 73889–73892 describes (2.9) less precisely as a product over bonds; that wording must not be used to silently remove any extra factors. If an application retains additional pivot, contour or reconstructed-field indicators, their exact pullback through Phi_V(gz) remains present. Nothing proved here equates those extra characteristic functions with a rectangular retained cutoff.

## 4. The actual exponential-gauge factor

Use the normalized trace tau with tau(I)=1 and Hermitian Lie coordinates. The analytic gauge function is

    G(V)=sum_y sum_(x in B(y), x!=y)
            {1-(1/2)tau[P_V(y,x)+P_V(y,x)^(-1)]}.                       (4.1)

For real unitary fields this is the source sum of 1-Re tau P_V. The exponent in the step is -g^(-2)G(V), with its field-independent normalization and any source contour indicators kept separately.

If P_V(y,x)=1, then for Omega(B)=P_(exp(i B)V)(y,x)=exp(i Grel_V(B;y,x)),

    G(V)=0,       D_B G(exp(i B)V)|_(B=0)=0,
    D_B² G(exp(i B)V)|_(B=0)[u,v]=<T_Vu,T_Vv>.                          (4.2)

Indeed 1-(1/2)tau(e^(iX)+e^(-iX))=(1/2)tau(X²)+O(X^4), and the first derivative of Grel is T_V. The nonlinear part of Grel does not enter the quadratic coefficient. Pulling back through (3.2) gives

    D_z² G(exp(i Phi_V(z))V)|_(z=0)=K_V^T T_V^T T_V K_V.                 (4.3)

The source gauge function therefore compares with K_L^T T_L^T T_L K_L by O(b) in weighted Schur norm. This is the averaged-contour penalty, not a tree-axial penalty.

In fact its dependence on the pivot chart simplifies exactly. Every contour in P is block-internal, and therefore reads no pivot. If E_free extends z by zero on the pivots, (3.3) gives

    G(exp(i Phi_V(z))V)=G(exp(i E_free z)V),
    T_V h_V=0,       T_V K_V=T_V E_free.                                (4.4)

Thus the exponential gauge factor is literally a local function of the unchanged retained coordinates. This also explains the source's use of a gauge remainder with argument gB rather than the full nonlinear pivot insertion. It does not remove any other cutoff factors.

All derivatives here are controlled by the finite-range bounds in Section3. Locally in z the remainder after (4.3) is bounded by C_L times the sum over gauge-output neighborhoods of the cube of the local supremum of |z|. After z->g z and division by g² it is O(g) times that cubic local sum. This bound requires |g| ||z||_infinity below the fixed chart radius; it is not a statement on unrestricted Gaussian fields.

For background a not satisfying P_V=1, the same actual expression (4.1) remains analytic. Its gradient is generally nonzero. Its full Hessian has the extra residual from the nonlinear contour map, and still differs from its flat value by O(b), by local Cauchy estimates. The formal gradient-times-D²Phi contribution is zero by (4.4), since D²Phi is supported on pivots. This supplies an analytic extension on a full background product ball; one must not replace (4.1) by a relative penalty and call that replacement the actual gauge factor away from P_V=1.

## 5. A physical stationary background on the source gauge slice

We now prove that the gauge-zero stationary backgrounds needed above exist within the previously established homogeneous branch. Only real fields are used for minimum comparisons; analyticity then extends the resulting identities.

Let W=exp(i w) be the next-coarse datum and b_out=||w||_infinity. Apply Notebook15 with final spacing L and original spacing 1/M. This is the unit-spacing theorem rescaled by x'=x/L, with total ratio ML. In d=4 the coupling-free Wilson action has no extra scale factor. The physical potential and its first differences acquire fixed powers of L under this rescaling; all resulting constants below may depend on L, never on M. Write U_f(W) for this ordinary minimizer and set

    V_part(W)=M^k(U_f(W)).                                               (5.1)

Exact composition gives M_L(V_part)=W. Notebook14's ordinary-reference trajectory and Notebook15's potential estimate give

    ||log(V_part)/i||_infinity <= C_L b_out,
    ||A_f(W)||_(N_alpha, current physical units) <= C_L b_out.             (5.2)

Let U_c(V) be the Notebook15 ordinary minimizer to current datum V, so S_M(log V/i)=S(U_c(V)). Choose b_out and a common current comparison radius delta small enough that all of the following hold: U_f(W) lies in the current-scale minimum ball; U_c(V) for ||log V/i||<delta lies in the final-spacing-L minimum ball; V_part lies within that delta-ball; all logarithms and local gauge actions remain in the earlier common domains. These are finitely many conditions of the form C_L delta<r_0 and C_L b_out<delta/2. They have a positive solution independent of M and volume.

The current minimum at V_part gives

    S_M(log V_part/i) <= S(U_f(W)).                                      (5.3)

Conversely U_c(V_part) is feasible for the full ordinary constraint by composition, and is in its common minimum ball. Thus the full minimum gives the reverse inequality. Therefore

    S_M(log V_part/i)=S(U_f(W)).                                         (5.4)

For any V in the current comparison ball with M_L(V)=W, U_c(V) is a full feasible competitor, so

    S_M(log V/i)>=S(U_f(W))=S_M(log V_part/i).                            (5.5)

This establishes constrained stationarity without assuming a dynamic-programming identity for arbitrary minimizers or backgrounds.

To impose the actual source gauge, define a rooted current-site gauge

    u(y)=1 at each block center,
    u(x)=P_Vpart(y,x) for x in B(y).                                    (5.6)

The values agree at centers because P(y,y)=1. By (2.1), the configuration

    V_*(W)=V_part(W)^u                                                   (5.7)

satisfies P_V*=1 exactly. By (2.3), M_L(V_*)=W. At fixed L, (5.6) is local analytic with ||log u/i||<=C_L||log V_part/i||. Notebook16's local coarse gauge invariance applies after shrinking the common margins, hence S_M(V_*)=S_M(V_part). The already established comparison (5.5) shows that V_* is a constrained minimum. The gauge transformation here is on the current lattice; its fixed-L site oscillation is harmless. The Notebook16 proof supplies the smooth fine extension needed for equality of the underlying classical actions.

All maps in (5.1),(5.6),(5.7) are analytic on a uniform complex ball in w. The constraints, P_V*=1 and the vanishing of the pulled-back first derivative hold for real w and hence hold as analytic identities on a smaller complex ball. This is not a complex minimum statement.

There is also a local uniqueness check matching the critical-orbit selection in CMP109 (2.3). At a real V_* the reduced action-plus-gauge Hessian proved in Section7 is positive. Hence V_* is the unique sufficiently nearby critical configuration on its exact pivot chart. A source critical configuration in the same small homogeneous neighborhood and gauge slice agrees with this one. More generally gauge-related fine minimizer representatives have the same classical action; no choice of a Landau instead of axial fine representative changes S_M. This identification is confined to the common homogeneous small-global-potential branch, not the full original plaquette/orbit domain.

## 6. Exact physical Hessian, with both curvature terms

Let a=log V/i. To evaluate the ordinary-coordinate classical action in the source relative chart, define bondwise

    Xi_a(B)=(1/i)log[exp(iB) exp(i a)],
    a_V(z)=Xi_a(Phi_V(z)).                                               (6.1)

If J_a X=int_0^1 Ad(exp(i t a))X dt is the left logarithmic differential, then

    D Xi_a(0)=J_a^(-1),        ||J_a^(-1)-I|| <= C ||a||,
    D² Xi_a(0)=O(||a||).                                                 (6.2)

The second assertion follows also directly from analyticity and Xi_0(B)=B. It is a bondwise finite-dimensional identity, with no lattice-spacing loss. Put K_a=J_a^(-1)K_V. Chain differentiation gives

    D a_V(0)=K_a,
    D² a_V(0)[u,v]=J_a^(-1)D²Phi_V(0)[u,v]
                    +D²Xi_a(0)[K_Vu,K_Vv].                             (6.3)

The ordinary action Hessian in retained source coordinates is exactly

    D²[S_M(a_V(z))]_(z=0)[u,v]
       =<K_a u,H_M(a)K_a v> + <m_M(a),D²a_V(0)[u,v]>.                   (6.4)

For V=V_*(W), adding (4.3) gives the actual reduced precision

    A_M(V)=K_a^T H_M(a)K_a + Curv_M(V) + K_V^T T_V^T T_V K_V,
    <u,Curv_M(V)v>=<m_M(a),D²a_V(0)[u,v]>.                              (6.5)

There are two curvature contributions in (6.3): nonlinear constraint straightening and the conversion from left-relative exponential to ordinary log coordinates. They are both retained.

For comparison with the explicit source current vertex, put

    j_rel=J_a^(-T)m_M(a),
    H_left=J_a^(-T) H_M(a) J_a^(-1)+<m_M(a),D²Xi_a(0)>.

Equations (3.4),(6.5) become

    <u,A_M(V)v>=<K_Vu,H_left K_Vv> + <T_VK_Vu,T_VK_Vv>
                   -2<j_rel,h_V C_V^(2)(K_Vu,K_Vv)>.                    (6.6)

This has exactly the sign and factor of the source vertex at Raw I46993–46996. The physical j_rel is the derivative of the same classical action with respect to its left-relative current datum. If the fine action is differentiated through a source minimizing extension, the chain rule writes it as H_1^T J; pure gauge terms in that derivative pair to zero by gauge invariance. Equation (6.6) does not promote J to an independent parameter.

Constrained stationarity says K_V^T j_rel=0, not j_rel=0. Indeed A_V h_V=I implies

    j_rel=A_V^T lambda,       lambda=h_V^T j_rel,                        (6.7)

because I-h_V A_V has range ker A_V. This does not annihilate h_V C_V^(2), and therefore cannot justify dropping the final term of (6.6).

## 7. Uniform O(b) precision and covariance neighborhood

Let b=||a||_infinity. The local estimates give

    ||K_a-K_L||_kappa <= C_L,kappa b,
    ||K_a||_kappa+||K_V||_kappa+||T_V||_kappa <= C_L,kappa.               (7.1)

Use (1.1), the weighted algebra inequality and the uniform norm of q_M to compare K_a^T H_M(a)K_a with K_L^T q_M K_L. The difference is at most C_L,kappa b. For Curv_M, apply (3.6) to the local second-derivative tensor (6.3), then use ||m_M(a)||_infinity<=Cb. This gives

    ||Curv_M(V)||_kappa <= C_L,kappa b.                                  (7.2)

Its ordinary-coordinate conversion part is actually O(b²); that improvement is unnecessary. The gauge term differs from its flat value by O(b) through (3.5). This proves (1.4).

The formula with the actual gauge function, as in the last paragraph of Section4, defines the same reduced Hessian on a full complex current-background ball and obeys the same O(b) estimate there. It need not be a centered Gaussian at an arbitrary background because its first derivative may be nonzero. Centering at the physical V_*(W) removes that first derivative by Sections4–5. This distinction separates analytic covariance bounds from the saddle-point identity.

There is a useful uniform version for the uniqueness assertion in Section5. Keep one fixed chart Phi_V and evaluate its full pulled-back Hessian at z rather than zero. Local Cauchy gives D Phi_V(z)=K_L+O(b+||z||_infinity), bounded second derivatives, and ||a_V(z)||_infinity<=C_L(b+||z||_infinity). Equation (1.1) and the complete ordinary-coordinate chain rule then give

    ||D_z²{S_M(a_V(z))+G(exp(i Phi_V(z))V)}-A_M,0||_kappa
                                      <= C_L,kappa(b+||z||_infinity).    (7.2a)

For the gauge term this uses the actual absolute function (4.1), including its contour-curvature residual away from P=1; (4.4) removes only the pivot-chart contribution. At real V,z in a fixed smaller supremum ball, (7.2a) is positive with lower bound gamma_*/2. That ball is convex in retained coordinates. Hence the pulled-back action is strictly convex there, and has at most one critical point. Any sufficiently small configuration on the same fiber is in this chart because its retained relative coordinates determine its pivots uniquely. The uniqueness radius is therefore independent of M and volume; no global minimum outside this neighborhood is inferred.

Let D_M(V)=A_M(V)-A_M,0. Decrease b so that

    C_L,kappa b <= gamma_*/2,       C_* C_L,kappa b <= 1/2.               (7.3)

Then, even at complex backgrounds,

    Re <z,A_M(V)z>_Herm >= (gamma_*/2)||z||²,
    ||A_M(V)^(-1)||_kappa <= 2 C_*,
    ||A_M(V)^(-1)-A_M,0^(-1)||_kappa <= 2 C_*² C_L,kappa b.              (7.4)

The first line uses ||D_M||_(2->2)<=||D_M||_kappa and the real positive baseline. The other two are the Neumann series in the weighted matrix algebra. In particular the current-coordinate counting covariance is uniformly bounded independently of the old depth M. For any desired epsilon>0 one may impose

    b <= epsilon gamma_*/C_L,kappa

to obtain

    ||A_M,0^(-1/2)D_M(V)A_M,0^(-1/2)||_(2->2) <= epsilon.                (7.5)

The direct covariance interface to Notebook18 is as follows. Put C_0=A_M,0^(-1), so its real spectral bounds are lambda_cov=1/B_* and Lambda_cov=1/gamma_*. Fix any 0<theta<=1/4 before choosing the coupling, and decrease the physical background ball further so that

    2 C_*² C_L,kappa b <= theta/(2 B_*).                                 (7.5a)

Then (7.4) implies ||A_M(V)^(-1)-C_0||_(2->2)<=theta lambda_cov/2, exactly the covariance closeness in Notebook18's otg-close condition. The weighted inverse bound gives a common entry majorant J_ij=2C_* exp(-kappa d(i,j)). Its weighted row sum A_kappa' is finite uniformly in periodic volume for any smaller exponent 0<kappa'<kappa, by the polynomial growth of the current lattice. Thus the required covariance majorant and row-summability inputs are also available. This meets the Gaussian neighborhood part of the tunable marked theorem. The local interaction hypotheses and, for its strictly local version, a support-valued precision expansion on a product background domain remain separate. The independent-current source domain is not supplied here.

Alternatively (7.5) gives relative covariance error at most epsilon/(1-epsilon) by the inverse resolvent identity. Condition (7.5a) is the more direct match to the stated Notebook18 theorem.

The exact rescaled integrand has classical exponent

    -g^(-2){S_M(a_V(gz))+G(exp(i Phi_V(gz))V)}
       =-g^(-2)S_M(a) -(1/2)<z,A_M(V)z> + terms of positive order in g,  (7.6)

locally where |g| ||z||_infinity is below the fixed chart radius. The linear term is zero only for the physical centered family. The local chart and gauge Taylor remainders are uniformly controlled as above; a complete weighted expansion of the classical remainder and all Haar/Jacobian/prior-action terms is a further interaction theorem, not a consequence of the precision estimate alone.

## 8. Scope and next interfaces

1. **Established here within the earlier homogeneous classical theory:** exact source relative/pivot chart; one-equation locality; preserved retained cutoff argument; exact averaged-contour gauge factor; physical constrained stationary family; both current/chart-curvature terms; uniform weighted O(b) reduced-precision comparison and inverse.
2. **Background locality has two meanings.** Phi_V, h_V, K_V and T_V read finite neighborhoods of the current configuration V. The map W->V_*(W) is a minimizing response and need not have strictly finite support. The present weighted kernel estimate concerns fluctuation input/output coordinates. It does not imply a strict support-valued expansion in W or in every original fine link.
3. **Source provenance:** formulas (2.2)–(3.2),(4.1) are the actual CMP109 maps, with RawI/II spelling out their normalization. Notebook15 and the minimum comparisons identify the homogeneous action branch. The full original orbit/reconstruction hypotheses of CMP116, including restrictions of backgrounds to arbitrary polymers, have not been verified by this note.
4. **Independent free current:** the physical current is constrained by the action and stationarity. Replacing it by an independent J in the source analytic carrier requires the separate source operator estimates; (6.6) does not prove that extension.
5. **Cutoff factors:** the retained rectangular factor is unchanged exactly. Any additional pivot/contour/reconstructed-field factor stays at its exact pulled-back argument. No assertion is made that these factors can be discarded, or that an axial fine covariance may replace the exponential-gauge retained covariance.
6. **Histories and interaction:** mixed-scale boundaries, arbitrary Dirichlet histories, the full interaction coefficient theorem, and quantum RG iteration remain separate. The present estimates concern one homogeneous current step with arbitrary preceding classical depth M.
