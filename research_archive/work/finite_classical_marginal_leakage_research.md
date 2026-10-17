# Uniform disappearance of finite classical marginal leakage

17 October 2026. Research proof for independent audit. This is a qualitative uniform statement along the standard nested compatible period family. It does not supply an exponential rate and does not assert exact finite marginal preservation. The preceding depth M is allowed to vary arbitrarily with the period.

## 1. Period family and claim

Fix the primitive ell, one admissible macro ratio R=ell^s, grouping J, activity exponent a0 and one common positive analytic radius b. All these are fixed. Let N run through the usual compatible nested source periods, for example N=2 ell^k with sufficiently large k. More generally require this cofinal divisibility property:

    for every fixed endpoint power L=R^q,
    L divides all sufficiently late periods N.          (1.1)

The proof below uses (1.1) to extract all the finite comparisons needed for an arbitrarily long endpoint semigroup in one joint limiting system. For arbitrary increasing multiples of J with bounded ell-adic valuation, an additional volume-extension comparison would be needed; that larger period class is not asserted here.

Let T_(M,R,N) map the finite input torus RN to the finite output torus N, using the actual pre-gauge background. Let beta_(M,RN) and beta_(MR,N) be the actual finite short-lift ratios normalized by their respective finite references. Define

    Lambda_(M,R,N)
       =beta_(MR,N) T_(M,R,N)-beta_(M,RN).              (1.2)

This is a linear functional on the invariant finite activity quotient. On an extracted input it is the ordinary finite classical leakage. All the activity spaces use the same a0,b.

Then

    omega_R,J,b(K)
       :=sup_{M, N>=K in the period family}
           sup_{x invariant, ||x||<=b^2}
                       |Lambda_(M,R,N)x|
              tends to zero as K tends to infinity.   (1.3)

Equivalently, the dual operator norm multiplied by b^2 tends uniformly to zero. The function omega is finite and decreasing for sufficiently large K. Uniform one-step classical and beta bounds already give omega<=C_beta(B_R+1), independent of M,N.

The index M can be any allowed preceding homogeneous depth, and need not stay fixed or have a finite subsequential limit. The proof explicitly handles sequences M_n tending to infinity.

## 2. Compactness of arbitrary finite input classes

Suppose M_n is any such sequence, N_n tends to infinity in the family, and x_n is invariant with ||x_n||<=b^2. Choose finite representatives E_n whose norms are at most b^2+epsilon_n with epsilon_n tending to zero.

Average E_n over the finite translations by J-cells, translating the carrier and its arguments simultaneously. The activity norm does not increase because each translation permutes the root sums. Its normalized total remains exactly the same because x_n is translation invariant. The resulting array is covariant under J-cell translations; its total still has all the original unit-translation, point and gauge identities. Individual coefficients need not be gauge invariant.

The no-radius-loss analytic-interaction compactness argument applies to this sequence on the SAME radius b. On every fixed embedded connected carrier, Montel compactness gives locally uniform convergence of its finite-dimensional coefficient function. A countable diagonal extraction gives a family E_infinity, and diagonal Fatou over finite rooted carrier collections, followed by supremum radii increasing to b, gives

    ||E_infinity||_(a0,b)<=b^2.                         (2.1)

Compact-field normalized totals converge. The large-carrier remainder is uniformly small by anchored cardinal decay; fixed carriers eventually embed without wrapping. Local gauge and spatial identities pass on their common compact-field domains, using the same local-gradient or finite-total continuity arguments as in the interaction compactness theorem. Thus E_infinity represents an invariant infinite class x_infinity.

Fixed-order total kernels converge locally:

    K_(n,N_n)(x_n) -> K_n(x_infinity),                 (2.2)

with the common exponential row bounds obtained from the fixed activity norm. In particular their second moments are uniformly summable. None of this requires M_n to be fixed: M_n is not an input to the compactness proof for E_n.

## 3. A varying-depth joint classical system

The classical maps and references must be extracted jointly with E_n. For every fixed nonnegative depth shift j and fixed endpoint power L=R^q, take the actual finite data at preceding depth M_n R^j and an appropriate compatible period obtained from RN_n by finitely many divisions by R and L. These endpoint powers alone suffice for the marginal-preservation limit. Property (1.1) ensures that all these data exist for sufficiently large n.

All relevant observed variables live on current lattices. For a fixed endpoint L, a current output fiber contains L^4 times a fixed number of link/color coordinates, independently of the preceding refinement M_n. The classical action families and pre-gauge maps have:

* a common positive holomorphic radius;
* uniform strict support and cardinal bounds;
* uniform complete C^(1,alpha) bounds and the exact 1/L amplitude;
* the actual finite reference transport and comparison identities;
* uniform finite small-gauge construction bounds.

These are the established estimates uniform in preceding depth, not estimates only for a selected fixed M. Apply the analytic-interaction compactness proof to the reference families and the analogous complete-output-family compactness proof to each fixed-endpoint map. A diagonal subsequence includes the countable set of depth shifts and endpoints.

Denote its limiting references by S_j^* and its maps by a_(j,q)^*, T_(j,q)^*, where the second index q means endpoint L=R^q. Thus T_(j,q)^* maps the scale-j quotient Q_j^* into Q_(j+q)^*. The first index j records the relative depth shift; no assertion S_j^*=S_(M_*R^j) for a finite M_* is made. The uniform q_M Hessian estimate implies beta(S_j^*)=1: the true reference Maxwell normalization is uniformly one before taking the limit.

The fixed-radius reference bound, exact reference transport, and scalar semigroup pass exactly as in the previously proved joint classical-system construction. For compact fields, anchored tails justify passing normalized reference values rather than extensive unnormalized energies. For the scalar semigroup on every invariant input class, the finite near-identity connecting gauges and endpoint estimates are uniform in M_n. Their compact group extraction and the summable-gauge argument therefore apply unchanged to this varying-depth sequence. No step of that argument uses that the label M is numerically fixed. Equivalently, for each fixed endpoint pair first obtain the finite comparison germ, pass it with its actual small-gauge data, and use the common holomorphic domain for continuation.

The resulting structural system satisfies precisely the hypotheses of classical_marginal_transport_research.md:

    T_(j,q)^* S_j^*=S_(j+q)^*,
    T_(j+q,r)^* T_(j,q)^*=T_(j,q+r)^*,

for all fixed q,r>=0, and it has the same uniform quadratic-only spatial estimate at fixed b for arbitrarily large endpoints R^q. Consequently that proof gives

    beta(T_(0,1)^* x)=beta(x).                          (3.1)

for every invariant class x in the limiting system.

This is the crucial varying-M step. It is not an invocation of a theorem that only constructs a local limit at one fixed M, and it is not an assumption that every different limiting classical system is identical. Every possible varying-depth structural limit has the property (3.1), which is all the contradiction argument needs.

## 4. Passage of the actual transported Hessian

Only the linearized pre-gauge response is needed for the leakage. Let

    H_n=D a_(M_n,R,N_n)(0).

Its matrix entries map output current angles on T_(N_n) to input current angles on T_(R N_n). They are ordinary coordinate derivatives, so the Hessian chain rule below uses counting transposes. All physical scaling is already inside the actual angle map a; no fine-refinement physical measure is to be inserted again.

The complete support-family estimate and Cauchy at zero give a pointwise bound

    |H_n(b,c)|<=C_R exp[-kappa_R dist(root(b),c)],       (4.1)

uniformly in M_n,N_n. Here root(b) is the final-unit cell containing the input bond b/R, and internal link/color conventions are absorbed into C_R. One can retain the amplitude factor 1/R, but R is fixed here. Each root has only O(R^4) input coordinates, so (4.1) gives both row and column exponential Schur bounds with constants depending on fixed R but not M_n or volume. Alternatively the row bound follows directly from the support reserve, and the pointwise bound supplies the column bound.

Joint local holomorphic convergence gives H_n -> H_* locally. Since the input total linear derivative vanishes by semisimple color invariance, its transported Hessian is exactly

    K2_out,n = H_n^T K2_in,n H_n.                       (4.2)

There is no D Phi(0) D^2a term. The exponential bounds for the two H legs and for K2_in yield a uniform exponential row bound on K2_out,n on the output current lattice, with an exponent depending on the fixed R,J. For example the triangle inequality through the two input roots lets one spend a fixed fraction of the minimum input/response exponent, and the remaining geometric sums are bounded by their infinite-lattice sums. The finite O(R^4) fiber multiplicity is fixed. There is no dependence on the old fine dimension M_n^4.

The same bounds prove local convergence in (4.2): truncate both intermediate root sums to a fixed neighborhood, use entrywise convergence on that finite sum, and then use the common exponential majorant for the discarded part. They also give uniform summability of the second displacement moments. Thus the infinite limit is

    K2_out,*=H_*^T K2(x_infinity)H_*,

which is the Hessian of T_(0,1)^*x_infinity.

## 5. Convergence of the finite coefficient functionals

For locally convergent torus kernels with a uniform exponential row bound, the short-lift second moments converge to the true infinite second moment. Indeed restrict first to a fixed displacement radius. Those finitely many terms converge locally. The remaining second-moment sum is bounded uniformly by C exp(-c times that radius), using the exponential row bound. The cutoff floor(N_n/16) tends to infinity, so it causes no extra term in the limit. Midpoint phases have fixed bounded shifts and are treated with the same majorant.

The finite reference denominators tend uniformly to one by the q_M periodization estimate, even for varying M_n. Therefore

    beta_(M_n,RN_n)(x_n) -> beta(x_infinity),           (5.1)
    beta_(M_n R,N_n)(T_(M_n,R,N_n)x_n)
                      -> beta(T_(0,1)^*x_infinity).    (5.2)

This uses the actual finite reference in each denominator. It does not replace its full nonlinear action by a canonical periodization. No convergence of extensive scalar totals is needed.

## 6. Uniform contradiction and consequences

If (1.3) failed, there would be delta>0 and sequences M_n,N_n,x_n as above with

    |Lambda_(M_n,R,N_n)x_n|>=delta

for all n. Apply Sections2-5 to a subsequence. By (5.1)-(5.2) its limit is

    |beta(T_(0,1)^*x_infinity)-beta(x_infinity)|=0

by (3.1), a contradiction. This proves the uniform disappearance claimed in (1.3).

For extracted classes the same conclusion reads

    sup_{M,N>=K} sup_{beta_(M,RN)x=0, ||x||<=b^2}
            |beta_(MR,N)(T_(M,R,N)x)| ->0.             (6.1)

The unextracted form (1.3) is slightly stronger and requires no projection-loss factor. Homogeneity yields a bound omega(K)b^-2||x|| for arbitrary invariant inputs at the same radius.

This result is qualitative. It does not show an exponential rate, does not prove summability of the leakage over infinitely many changing periods, and does not set any finite leakage identically to zero. It does show that for any fixed tolerance the period threshold can be chosen independently of preceding M and independently of the admissible input class.

For a fixed PER-STEP drift tolerance no summability is required: choose K so omega(K) is at most that tolerance. Every step of an admissible finite history whose output period remains at least K then has the same leakage bound on b^2-norm inputs, uniformly in the history length. On an envelope ||x||<=C_int b^2, multiply the tolerance by C_int, or choose K with omega(K)<=the desired tolerance/C_int. This is a magnitude bound, not a sign or an accumulated-drift assertion.

The divisibility hypothesis (1.1) is part of the result. It is satisfied by the standard nested source tori. Extending to arbitrary growing compatible multiples with no increasing endpoint divisibility would require an additional uniform period-extension/local-volume comparison; it is not obtained merely from the fact that N tends to infinity.

The limiting argument does not identify different classical systems. Exact beta preservation holds for each possible structural limit separately, and hence rules out a nonzero finite leakage subsequence. No quantum coupling sign, determinant coefficient, infinite physical trajectory, or global measure assertion follows from this compactness result.
