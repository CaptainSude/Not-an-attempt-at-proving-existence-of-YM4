# Current-cell vertex bounds uniform through fine refinement

Research proof candidate, 17 October 2026. This note supplies concrete vertex inputs for a rooted support-valued localization theorem for the homogeneous classical minimizer. It does not assume that a previously proved one-weight response bound already supplies the required mixed-insertion norm. No output or repository file was edited.

The main conclusion is that the corrected-constraint stationarity equations admit a simultaneous fixed-point formulation with (i) uniformly analytic, finite-current-range nonlinear vertices and (ii) uniformly exponentially summable linear cell operators. The normalized local Wilson energy has the same vertex property. These assertions use physical cell Banach spaces and the physical fine measure; they do not sum absolute raw coefficients over M^4 independent fine coordinates.

There is also a concrete obstruction: the physical adjoint of the full ordinary rooted average is not uniformly bounded as refinement increases. It must not replace the corrected constraint in this fixed-point proof. Equality of the resulting scalar action with the ordinary constrained action is supplied separately by Notebook15's gauge transfer.

## 1. Spaces, normalization and previously proved inputs

Fix d=4, odd fixed L, M=L^j and fine spacing eta=M^-1, with final current spacing one. Fine pairings use eta^4 times counting measure, while current pairings use counting measure. Initially all operators are on compatible finite periodic tori; constants below are independent of M and volume. Source and field components use fixed finite-dimensional color norms.

Use complete fine-field spaces

    X_eta = N_alpha = { A : ||A||_infinity + ||nabla_eta A||_infinity
                                 +[nabla_eta A]_alpha < infinity },
    Y_eta = C^alpha for jet coefficient fields,
    Z_eta = bounded fine coefficient fields,
    E = bounded current bond fields,                                   (1.1)

where 0<alpha<1 is fixed and the Hölder seminorm uses physical distances on fixed collars. The local jet S=(I,nabla_eta), including the finite component selections needed by a plaquette, maps X_eta to Y_eta uniformly. No sharp cell indicator is differentiated.

The concrete sources already proved and audited in this workspace are:

* `wilson_nonlinear_force_research.md`, §§1–6: the exact density S_eta(A)=eta^4 sum_p L_eta(SA_p), with jointly analytic L_eta uniform in eta, quadratic part (1/2)|dA|², and nonlinear force S^T f_eta(SA), where f_eta begins at degree two and is analytic X_eta->Y_eta uniformly.
* `flat_nonlinear_average_research.md`, §§1–5: the actual full corrected map F(A)=QA+R(A), Q=Q_M^st, has a refinement-uniform complex supremum domain and a physical dependency radius R_* independent of j.
* `nonlinear_fixed_gauge_minimizer_research.md`, §1: the physical-adjoint row bound ||DR(A)^T||_(infinity->infinity)<=C||A||_infinity, with holomorphy in that operator norm. The transpose includes the fine physical measure, not an unnormalized matrix transpose.
* `flat_constrained_schauder_research.md`, §§1,3–6, and `nonlinear_minimizer_weighted_response_research.md`, §1: the exact constrained inverse C and extension H obey the equal-exponent weighted maps listed in Section5 below. These estimates are for complete fields and all admissible cell weights.
* Notebook15's simultaneous stationarity identities and Notebook16's action identity: the scalar ordinary constrained action is exactly the Wilson action at the corrected fixed-slice minimizer. The ordinary map's physical adjoint is not required for that identity.

The actual corrected one-step coordinate map is recorded at Raw I24320–24325, 24344–24369, with the exact ordinary/corrected bridge at 47076–47087. Its one-step physical scaling is F_h(A)=(Lh)^(-1)F_L(hA). The source normalization of the Wilson density and fine pairing was matched at the deposited-transcription level in `wilson_source_normalization_research.md`; no new independent claim about all original orbit domains is made here.

## 2. A legitimate current-cell decomposition of complete fields

Choose a smooth physical partition of unity {chi_i} indexed by unit current cells: sum_i chi_i(x)=1, supp chi_i lies in a fixed enlarged cell S_i, and derivatives through order three are uniformly bounded. One explicit construction is a nonnegative compactly supported smooth bump divided by the sum of its integer translates; periodization gives the same bounds on compatible tori, counting repeated supports with multiplicity. Every point, and every ball of a fixed physical radius, meets a bounded number of supports.

For each fine field type, let E_i be the Banach subspace of complete fields supported in S_i, with its global X_eta, Y_eta or Z_eta norm, as appropriate. Inclusion E_i into the complete global space is denoted I_i. Put P_i u=chi_i u. On current fields use the ordinary finite-dimensional coordinate restriction/insertion per current cell. Then

    u=sum_i I_i P_i u,
    ||P_i u||_(local block) <= C ||u||_(same norm on a fixed collar),    (2.1)

and the reconstruction map

    Rcal((u_i))=sum_i I_i u_i

has uniformly bounded norm from the block supremum space to the complete global space. There is no requirement that arbitrary cell restrictions admit an unproved extension: E_i consists of actual complete supported fields. The map P Rcal is a bounded projection onto compatible decompositions since Rcal P=I.

For X_eta, the multiplier estimate follows from the exact product rule

    nabla_eta(chi A)(x)=chi(x+eta e) nabla_eta A(x)
                            +(nabla_eta chi)(x) A(x).                  (2.2)

The smooth sampled chi and its first differences have uniform physical C^alpha bounds. The local C^alpha norm of A is controlled by N_alpha(A) by telescoping, with no eta^-alpha loss. The C^alpha product inequality then proves (2.1). The same argument is simpler for Y_eta and Z_eta. Finite overlap proves the reconstruction bound, also for pairs of points used in the local Hölder seminorm. Thus no field is abruptly set to zero before its derivatives are taken.

## 3. The stronger mixed-insertion vertex norm

For a complete local analytic map F, expand its cell output after reconstruction about zero:

    P_i F(Rcal u)=sum_(n>=0) sum_(j_1,...,j_n)
                  V_(n;i;j_1,...,j_n)[u_(j_1),...,u_(j_n)].             (3.1)

The coefficients include 1/n!, so that V_n is the symmetric Taylor coefficient rather than the derivative. Mixed field types are allowed by using a fixed finite direct sum of the block spaces. For a set of cell labels S let tau(S) be the minimum number/length of current lattice edges in a connected graph containing S, allowing additional, unmarked vertices. This is the graph Steiner length, not the metric minimum-spanning-tree length on S alone. Define

    v_n(kappa)=sup_i sum_(j_1,...,j_n)
       exp[kappa tau({i,j_1,...,j_n})] ||V_(n;i;j_1,...,j_n)||.          (3.2)

The norm is the multilinear operator norm of the indicated cell Banach spaces. This is a mixed-insertion norm: it sums every input cell label. It is stronger than bounding one weighted input direction with all others bounded.

**Finite-range analytic vertex lemma.** Suppose every output P_i F reads only cells j with d(i,j)<=R, at most D_R such labels; suppose F is analytic and bounded by M_F on a uniform global ball of radius r_F in the input complete space. If the reconstruction norm is C_P, then its coefficients satisfy

    v_n(kappa) <= M'_F [ e C_P D_R exp(kappa R)/r_F ]^n,                 (3.3)

after harmless fixed factors from output multiplication. If F starts at degree two, then v_0=v_1=0 and sum_n v_n t^n is analytic and quadratic at zero.

Proof. The reconstructed tuple lies in the analytic ball for block norm below r_F/C_P. For any normalized n directions, multivariable Cauchy on radii r_F/(n C_P) bounds the derivative by M'_F(n C_P/r_F)^n. Dividing by n! and using n^n/n!<=e^n gives the coefficient norm. Only D_R^n ordered tuples are nonzero. Joining i to every input label along shortest paths has length at most nR, so exp(kappa tau)<=exp(kappa nR). This proves (3.3). At a fixed small background the same proof gives uniform local Taylor coefficient bounds on a smaller margin, but its constant and linear terms need not vanish. No raw fine dimension occurs.

The same reasoning bounds a version rooted at one input and summed over the output and the other inputs: all output labels are in a fixed neighborhood of that input. Thus the finite-range vertices can be used with either rooted convention at the cost of fixed factors.

For support-family substitution the exact geometric inequality is

    tau({i} union X_1 union ... union X_n)
      <= tau({i,j_1,...,j_n}) + sum_r tau({j_r} union X_r).               (3.4)

It follows by joining the corresponding connected graphs at their roots. Auxiliary j_r remain allowed as unmarked vertices, so dropping their status as terminals causes no problem. The same assertion with metric minimum-spanning-tree length need not hold with constant one. If ell_MST is that latter convention, the standard doubled traversal and shortcut argument gives ell_MST(S)<=2 tau(S). Thus a final norm with exponent mu ell_MST is covered by a tau norm with exponent at least 2mu; this reserve must be made explicit when interfacing with the earlier polymer norms. Consequently (3.2), not merely a one-weight estimate, is the useful concrete input for the rooted support fixed point. The abstract summation/contraction theorem is being supplied separately.

### 3.1 Arbitrary fixed support-cardinality reserve

Suppose the rooted family norm further weights a true variable support X by exp(a|X|), with any prescribed fixed a>=0. The vertices above are Taylor coefficients at the fixed flat background. Their coefficients depend on the regulator and geometry, but introduce no additional variable-background support. After substitution the new support is the union of the input supports, so

    exp(a|union_r X_r|) <= product_r exp(a|X_r|).                        (3.5)

Together with (3.4), this leaves the vertex majorants (3.3) unchanged. A linear operator changes the root, not the variable support, and is also compatible with this reserve. Only the initial local source B_j, assigned support {j}, acquires the factor exp(a). The small source radius may therefore shrink with a while all estimates remain uniform in M and volume. This is sufficient at the concrete-input level to pay a fixed exponential support-cardinality cost in a later polymer theorem; small spatial decay alone would not pay such a cost.

This statement is about expansion from a fixed flat baseline. Re-expanding around a background-dependent minimizing solution and hiding that background in the coefficients would not automatically preserve strict support in the original variables. No such re-expansion is used in the input supplied here.

## 4. Concrete nonlinear vertices through arbitrary refinement

### 4.1 Wilson jet coefficient

Set Fnl_eta(A)=f_eta(SA). The local plaquette formula is

    P_eta(a,b,c,e)=exp(i eta a)exp(i eta b+i eta² c)
                     exp(-i eta a-i eta² e)exp(-i eta b),
    L_eta(z)=-(1/2)tau[((P_eta(z)-I)/eta²)^2 P_eta(z)^(-1)].              (4.1)

The eta=0 singularity is removable before any vertex derivative is taken. Joint analyticity on a fixed jet ball gives uniform coefficients. The jet map is uniformly bounded X_eta->Y_eta, and C^alpha is a Banach algebra at fixed alpha. Hence Fnl_eta:X_eta->Y_eta is analytic on a uniform ball, bounded there, and starts at degree two. Its output at a fine plaquette reads only a bounded physical neighborhood of that plaquette. After P_i localization, only a fixed number of neighboring current cells can occur in each input slot. Lemma3 therefore gives (3.3), uniformly in eta, for this genuine Wilson force vertex.

This reasoning keeps S^T outside the vertex. The pointwise force S^T Fnl_eta may have eta^-1 coefficients; no uniform fine supremum bound for that force is claimed. Its propagation is by the separately proved operator C S^T or (S H)^T, as in Section5.

### 4.2 The local Wilson energy: where the M^4 count goes

Define the current-cell energy

    E_i,eta(A)=eta^4 sum_(positive fine plaquettes p)
                              chi_i(x_p) L_eta((SA)_p).                 (4.2)

Then S_eta(A)=sum_i E_i,eta(A) exactly. Its quadratic term is the similarly partitioned Maxwell energy. The nonlinear energy remainder uses L_eta-L_2 and starts at degree three.

There are O(eta^-4) plaquettes in a fixed physical cell, but

    eta^4 sum_p |chi_i(x_p)| <= C_d,                                    (4.3)

uniformly in eta and i. The fine derivative is already inside the bounded jet norm. Therefore E_i,eta is a uniformly bounded analytic scalar map on a fixed N_alpha ball, with fixed current-cell dependency radius. Its Taylor coefficients obey (3.3); the same is true for the degree-three remainder. This proves the energy-density vertex bound required after substituting the minimizing field. It would be incorrect to drop eta^4 and sum M^4 absolute bare plaquette coefficients, or to expand each fine difference against unrelated fine variables with only their supremum norms.

The scalar action at the ordinary homogeneous minimizer equals this sum evaluated at the corrected fixed-slice minimizer, by Notebook15's exact gauge transfer and gauge invariance. Thus an ordinary-average adjoint need not be inserted into the energy localization argument.

### 4.3 Full corrected nonlinear constraint

The physical one-step map satisfies

    F_h(A)=(Lh)^(-1)F_L(hA)=Q_h A+R_h(A),
    ||R_h(A)||_infinity <= C h ||A||_infinity²,
    ||DR_h(A)||_(infinity->infinity) <= D h ||A||_infinity.              (4.4)

For h_t=L^{t-j}, sum_(t<j)h_t<=(L-1)^(-1). The proved Riccati bound keeps all intermediate physical fields in a fixed uniform ball. The resulting F=Q+R is analytic and uniformly bounded on that ball, with R quadratic at zero. Its physical dependency radius is at most r_L sum h_t, hence a fixed R_* independent of j. This is enough to apply Lemma3 to

    R:X_eta -> E,

using ||A||_infinity<=||A||_X. The sum over fine-scale stages has already been performed in (4.4); it is not repeated once per vertex coefficient. Higher mixed coefficients follow by Cauchy in the uniform domain, not by estimating an uncontrolled number of multilevel terms.

### 4.4 Physical-adjoint constraint vertex

The simultaneous stationarity equation also needs

    V_eta(A,m)=DR(A)^T m,       X_eta x E -> Z_eta.                      (4.5)

This requires more than ordinary holomorphy of R into bounded coarse fields, because the physical transpose includes eta^-4. The previously proved physical-row estimate supplies exactly the missing input. At one step the physical transpose row contains the measure ratio L^4 and satisfies

    ||DR_h(A)^T||_(infinity->infinity) <= D_* h ||A||_infinity,
    D_*=N_L K_0 L^(d-1).                                                (4.6)

Both Q_h and its physical adjoint contract the bounded norm. Transposing the nonlinear composition and using the intermediate-field bound gives

    ||DR(A)^T||_(infinity->infinity)
                 <= exp[2D_*||A||_infinity/(L-1)]-1.                   (4.7)

The map is holomorphic into this physical absolute-row operator space, uniformly over refinement. Consequently (4.5) is jointly analytic and O(||A|| ||m||) on a fixed product ball. Its output at a fine bond b reads coarse m within R_* and background A within 2R_*: every relevant coarse equation contains b and reads its own R_* neighborhood. Thus V_eta has fixed current range, starts at total degree two in (A,m), and satisfies (3.3). Cauchy is applied to the physical-row operator norm in (4.7), never to individual fine coefficients followed by a count of their number.

No Hölder bound for V_eta is needed: its output enters C or H^T, which accept bounded fine coefficients. This avoids differentiating the current m or a fine-scale constraint coefficient.

## 5. Exponentially summable cell blocks of the linear propagators

The proved complete-field estimates, for every admissible cell weight w with w(i)/w(j)<=exp(kappa_0 d(i,j)), are

    H:E_w -> X_eta,w,
    C:Z_eta,w -> X_eta,w,
    C S^T:Y_eta,w -> X_eta,w,
    H^T:Z_eta,w -> E_w,
    (S H)^T:Z_eta,w -> E_w,
    q:E_w -> E_w.                                                       (5.1)

For the fifth map it suffices to restrict its input to Y_eta; the stronger bounded-input estimate is useful. These are exactly the bounds used in the audited weighted-response proof. They include one physical fine derivative in S H and the equal-exponent constrained Schauder estimate for C S^T. They are not statements about an unbounded projection Pi acting on bounded fields.

Let T be any operator in (5.1) and form its cell block T_ij=P_i T I_j, where the source E_j consists of supported complete fields, or a finite-dimensional coarse cell. For source u_j use the weight

    w_j(n)=exp(kappa_0 d(n,j)).

Its weighted input norm is at most C exp(kappa_0 r_s)||u_j||, since the source is supported in a fixed collar. The complete weighted estimate gives

    ||T_ij|| <= C_T exp(-kappa_0 d(i,j)),                               (5.2)

with a fixed collar correction included in C_T. This is an operator norm between cell Banach spaces, not an entrywise assertion about a singular differentiated Green kernel. In particular the local block i=j is controlled by the equal-exponent Schauder estimate.

For any 0<kappa<kappa_0, polynomial cell growth gives

    max{sup_i sum_j e^(kappa d(i,j))||T_ij||,
        sup_j sum_i e^(kappa d(i,j))||T_ij||} <= C_T,kappa < infinity.    (5.3)

Both rows and columns follow from the common pointwise block envelope (5.2), without requiring self-adjointness in these Banach norms. Periodic-distance sums obey the same upper bound uniformly in volume.

The decomposition is exact. For example

    C S^T f = sum_j C S^T(chi_j f),                                     (5.4)

because sum chi_j=1 and S^T is linear. Every chi_j f is a complete C^alpha field; the derivative of the smooth cutoff is part of S^T(chi_j f), which is controlled by the same theorem. The cutoff derivative terms cancel in the sum. No sharp splitting or unproved bounded singular-kernel integral is used. Analogous statements hold for H^T and (S H)^T with their physical transpose normalization.

The derivative kernels needed in the nonlinear equations are already included: output fine derivatives and their Hölder seminorms are part of X_eta, while S^T acts through C S^T and (S H)^T. Taking separate absolute fine-coordinate derivatives of those kernels would be a different, generally stronger demand and is unnecessary for (3.2).

## 6. Exact simultaneous fixed point with only these vertices

Write N(A)=S^T f_eta(SA), use the corrected constraint F(A)=QA+R(A), and let the multiplier m be the one in Notebook15. The exact stationarity equations are equivalent near zero to

    A = H B - H R(A) - C S^T f_eta(SA) + C V_eta(A,m),
    m = q B - q R(A) + (S H)^T f_eta(SA) - H^T V_eta(A,m).              (6.1)

Indeed the second equation rearranges to

    (I+H^T DR(A)^T)m = q[B-R(A)] + H^T N(A),

and the first is A=H[B-R(A)]+xi with
xi=-C N(A)+C DR(A)^T m. These are the already proved chart and reduced stationarity formulas. Conversely C's exact constraints make xi lie in the fixed flat slice, and the small inverse in the multiplier equation recovers the original formulation. No extra critical points are introduced in the common small ball.

All nonlinear primitives in (6.1) are quadratic at zero:

    R(A),       f_eta(SA),       V_eta(A,m)=DR(A)^T m.

Sections3–4 prove their mixed-insertion generating norms analytic and quadratic, uniformly in M. Section5 proves the required linear block sums, with an exponent spare. On the compatible-decomposition space from Section2, apply P to (6.1) and reconstruct inputs with Rcal. Its fixed points reconstruct exactly to (6.1); the redundancy of overlapping smooth cells causes only fixed norm constants. Taking the product-space radius smaller absorbs these constants in the quadratic contraction.

This supplies the concrete data for a rooted support-family fixed-point theorem. It does not by itself replace the proof of that abstract theorem. In particular, summability of the full tree expansion, canonical bookkeeping of repeated supports, and subsequent localization of the scalar action are separate conclusions to be obtained from that theorem using (3.2),(3.4),(5.3) and the local energy vertices (4.2).

## 7. Why the full ordinary rooted derivative is not a uniform substitute

The ordinary full average is still analytic as a map from small complete physical connections to bounded current data, and has fixed physical dependency range. Notebook14's trajectory bound gives that assertion uniformly through refinement. Thus it has local analytic vertex estimates of the X_eta->E type. The problematic operation is its physical transpose acting on arbitrary bounded current fields.

Let Q_ord be the flat derivative of the full ordinary rooted average in physical potentials. Exact gauge covariance gives

    Q_ord D_eta lambda = D_1(lambda restricted to final centers),       (7.1)

with the same sign on both sides under either consistent gauge convention. Work on a torus large enough that a current vertex and its incident bonds do not coincide with their periodic copies. Take a fixed unit color vector, and lambda equal to that vector at one current-center fine site y and zero at every other fine site. Then D_eta lambda is nonzero on exactly 2d fine bonds, with magnitude eta^-1. Therefore

    ||D_eta lambda||_(2,eta) = sqrt(2d) eta^(d/2-1),
    ||D_eta lambda||_(1,eta) = 2d eta^(d-1).                            (7.2)

The right side of (7.1) has magnitude one on 2d current bonds. Consequently

    ||Q_ord||_(L2_eta->L2_1) >= eta^(1-d/2).                            (7.3)

Choose m equal to this coarse gradient, so ||m||_infinity=1 and
<Q_ord D_eta lambda,m>_1=2d. Physical transposition and (7.2) imply

    ||Q_ord^T||_(infinity->infinity) >= eta^(1-d).                        (7.4)

In dimension four these lower bounds are eta^-1 and eta^-3. They are a concrete obstruction, not an absence of an estimate in the available notes. The complete N_alpha norm of this fine gradient is large, so there is no contradiction with boundedness of Q_ord:X_eta->E.

The corrected flat derivative instead satisfies Q_M^st D_eta=D_1 Q_0, with the scalar block mean Q_0, and its physical transpose is a bounded-field contraction. This is why (6.1) uses the corrected map. A specially projected composition involving the ordinary adjoint could have cancellations, but none is assumed here.

The fixed-L current-step ordinary pivot chart proved in `physical_current_pivot_precision_research.md` is unaffected: its refinement ratio is fixed L, so the corresponding finite-dimensional constants are allowed to depend on L. The present obstruction concerns composing rooted averages through the unbounded total ratio M.

## 8. Exact status of the localization input

**Proved concrete input:** uniformly analytic finite-current-range Wilson jet, energy, corrected-constraint and physical-adjoint constraint vertices; mixed-insertion coefficient sums (3.2) with analytic majorants; exponentially summable linear cell blocks including all derivatives used in (6.1); exact simultaneous equations using only those objects.

**Stronger than the prior one-weight theorem:** the new cell localization and finite-neighborhood Cauchy argument actually sum all input labels in (3.2). The previous one-weight estimate is used only to construct the linear block envelopes (5.2), where one source label is appropriate.

**Not asserted:** raw fine-coordinate absolute Taylor coefficient norms without physical weights/regularity; uniform ordinary rooted-adjoint bounds; a full support-valued precision expansion before applying the abstract fixed-point and action-localization theorem; source independent-current or mixed-history hypotheses; quantum RG integration. Backgrounds remain in the homogeneous small global potential branch. The exact scalar gauge transfer, not a false replacement of ordinary and corrected coordinate derivatives, identifies its classical action with the ordinary branch.
