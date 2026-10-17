# Finite-volume total-kernel extraction with exponentially small defects

17 October 2026. Proof candidate for independent audit. This is a finite-regulator repair of the limiting-kernel algebra in `total_kernel_ward_extraction_research.md`. It constructs a definite finite-volume beta and quantitative approximate low-momentum cancellation. It does not claim exact vanishing on a torus or a completed bounded localization of the principal spatial remainder.

## 1. Quantitative hypotheses and notation

Work on the cubic torus T_N=(Z/NZ)^d, d=4, with N>=64 and all the compatible partition divisibilities. Fields use positive unit bonds and Hermitian color coordinates. Let E_N be a real analytic total functional with local gauge invariance, translations and the full signed-permutation group. Let K_(n,N)=D^n E_N(0), n=2,3,4. The one-point kernel vanishes by semisimplicity. Treat a negative bond by reversing its sign in each tensor slot.

Write xi(b)=x+e_mu/2 for a positive bond b=(x,x+e_mu), and use the induced torus l1 distance between bond midpoints. Let D_N(b1,...,bn) be their maximum pairwise distance. Suppose for some 0<mu<=1,

    sup_b1 sum_(b2,...,bn) exp(mu D_N(b1,...,bn))
                  |K_(n,N)(b1,...,bn)| <= A_n.          (1.1)

Color indices are included; all constants are uniform in N and preceding refinement. The present connected J-cell activity norm supplies (1.1) at each fixed n by coordinate Cauchy and an exponent loss. Crucially mu=mu(J)>0 and A_n=A_n(J,b,D,epsilon) may depend on J. No constant independent of J is inferred.

A reference S_N has the same symmetries and Ward identities, and analogous bounds A_n^S. The normalized local Wilson action is the simplest reference. A more general classical reference is allowed with the finite-volume normalization condition in Section4.

All midpoint Fourier conventions and Ward generators are exactly those of the total-kernel note. Mixed bond/site tuples appearing in a Ward defect use the same physical metric, with a scalar gauge slot at a site.

## 2. A symmetric short-range lift

Put T=floor(N/16). On infinite-lattice bond tuples define

    Ktilde_(n,N)(b1,...,bn)
       =K_(n,N)(b1 mod N,...,bn mod N)
             1{D_infinity(b1,...,bn)<=T},               (2.1)

where D_infinity is the maximum l1 midpoint separation of the lifted tuple. The formula is translation invariant and has finite relative range. It preserves slot permutations, signed-permutation covariance, global color covariance and reality. In midpoint Fourier variables it therefore preserves the exact parity Gamma_n(-p)=(-1)^n Gamma_n(p).

The definition does not depend on choosing one preferred anchor for the cutoff. To form an anchored Fourier series, set one positive bond tail to zero only after (2.1). Reanchoring then translates the entire lifted tuple, preserving the cutoff.

There is a unique lifted representative, with the first bond fixed, for every torus tuple with D_N<=T. Indeed each other midpoint has a unique coordinatewise lift within T of the first midpoint, because 2T<N. Each pair of such lifts differs by at most 2T<N/2 in every coordinate, so its ordinary separation is the torus separation. The pairwise diameter condition is therefore satisfied simultaneously. Conversely every tuple in (2.1) projects to such a short torus tuple. Consequently relative periodization gives

    K_(n,N)=Per_N Ktilde_(n,N)+Ktail_(n,N),
    Ktail_(n,N)=K_(n,N) 1{D_N>T}.                       (2.2)

No image multiplicity is hidden in this identity.

For every fixed moment order m>=0,

    ||Ktail_(n,N)||_m
       :=sup_b1 sum_(b2,...,bn)(1+D_N)^m |Ktail_(n,N)|
       <= A_n B_m(mu) exp(-mu T/2),
    B_m(mu)=(1+2m/mu)^m,       B_0=1.                  (2.3)

This follows by spending half the exponential to absorb the polynomial. Since T>=N/32, the right side is bounded by A_n B_m(mu) exp(-mu N/64). All fixed powers of N can thus be absorbed with a further exponent loss if needed.

## 3. Ward defects of the lift are exponentially small

Let W_2,W_3,W_4 be the linear combinations of total tensors in the exact Ward equations:

    W2=K2(A,d lambda),
    W3=K3(A,B,d lambda)
                  -K2(A,L_lambda B)-K2(B,L_lambda A),
    W4=K4(A,B,C,d lambda)
          -sum_cyclic K3(A,B,L_lambda C)
          -2 sum_cyclic K2(A,Q_lambda(B,C)),            (3.1)

with L,Q in the total-kernel note. These equations are linear in the list (K2,K3,K4), although the test-field notation is multilinear. On the torus W_n(K_N)=0 exactly.

In coordinate kernels each W is a fixed finite sum of nearest-neighbor shifts, color commutators and coincident-slot embeddings. It never introduces a long-range summation. Permutation symmetry permits anchoring every term at an output field bond. Thus for each fixed m,

    ||W_n(Ktail)||_m
       <= C_(d,g,n,m) sum_(j=2)^n ||Ktail_j||_m,        (3.2)

where replacing m moments by (1+D)^m absorbs the bounded endpoint shifts. The constant includes only finite color structure constants and the fixed number of shifted/merged slots, not N or any count of fine bonds.

Ward operations commute with relative periodization. Hence

    Per_N W_n(Ktilde)=-W_n(Ktail).                      (3.3)

Every tuple in W_n(Ktilde) has mixed bond/site diameter at most T+2. In particular all relative components have magnitude below N/2. Its relative periodization is injective: two lifts with the same anchored torus tuple cannot both lie in this range. Thus (3.3), (3.2) and (2.3) bound the **infinite lifted** defect, rather than merely its values at periodic Fourier momenta:

    ||W_n(Ktilde)||_m
       <= C_(d,g,n,m) B_m(mu)
                  (sum_(j=2)^n A_j) exp(-mu N/64).     (3.4)

Equivalently, every fixed Fourier derivative of the Ward defect at zero is exponentially small; its bound follows from (3.4), with an additional fixed factor depending on n,m for the anchored phase. Taking m<=3 suffices for the extraction below. The same statements hold for the reference.

This is why a symmetric diameter cutoff, with a genuine interior margin, is preferable to separately truncating each displacement relative to an arbitrarily selected slot. The latter can break permutation or reanchoring identities.

## 4. A definite finite-volume coefficient

Let Gamma_n^E,N and Gamma_n^S,N be the midpoint Fourier vertices of the short lifts. They are entire functions of the independent momenta, though midpoint phases can be quasiperiodic away from zero. Their parity and point symmetries are exact.

For a simple gauge group, exact global adjoint covariance reduces each Hessian color block to its invariant form. Write

    Gamma_2^E,N(p)=m_E I+P2_E(p)+O(|p|^4),
    (P2_E)_(mu mu)=a_E p_mu²+b_E sum_(nu!=mu)p_nu²,
    (P2_E)_(mu nu)=c_E p_mu p_nu,        mu!=nu.          (4.1)

The same form holds for S. Define

    b_E=(1/2) partial_(p_nu)^2 Gamma_(2,mu mu)^E,N(0),
    b_S=(1/2) partial_(p_nu)^2 Gamma_(2,mu mu)^S,N(0),
    beta_N=b_E/b_S,            mu!=nu,                  (4.2)

provided |b_S|>=1/2. Symmetry makes the distinct pair immaterial. Reality makes beta_N real. It is a definite finite-torus prescription, not a subsequential limit.

For normalized local Wilson S and T larger than its fixed kernel range, the lifted reference is its usual infinite kernel and b_S=1 exactly. For the actual homogeneous classical reference S_(MR), an additional already established flat input is available: its finite-torus Hessian is the exact periodization of the uniformly exponentially decaying q_(MR), whose midpoint quadratic coefficient is one. The comparison pays both the discarded infinite-kernel tail and long images folded into the short torus lift. Every noncentral image folded into a displacement of size at most T has original size at least N-T, and its folded second moment is bounded by its original absolute second moment. Thus (2.3), with a fixed exponent loss, shows |b_S-1|<=C(J)exp(-c mu N). In particular |b_S|>=1/2 for all sufficiently large N, uniformly in MR. A mere assertion that some subsequential reference limit is normalized would not supply this exponential comparison and is not used here.

Since b_E is bounded by one half the appropriate second midpoint moment, beta_N is uniformly bounded by C(mu)A_2^E. Set

    F_N=E_N-beta_N S_N,
    A_* =sum_(n=2)^4(A_n^E+|beta_N|A_n^S),
    delta_N=C_(d,g,mu) A_* exp(-mu N/64),              (4.3)

with C large enough to cover the finitely many moments through order three. Constants retain their J dependence through mu,A_n. F_N is still exactly gauge invariant on the finite torus. Its short lifted kernels have Ward defects at most delta_N, and their transverse quadratic coefficient b_F is zero exactly by (4.2).

## 5. Quantitative approximate cancellation through degree four

The following argument is finite-dimensional coefficient algebra, not a limit argument. Apply the lifted quadratic Ward relation with defect to Gamma_2^F,N(p) hat p, where hat p_mu=2 sin(p_mu/2). Its degree-one coefficient is m_F p, so |m_F|<=C delta_N. The degree-three coefficient is

    P2_F(p)p-(m_F/24)(p_mu³)_mu.

Since b_F=0, coefficients of p_mu³ and p_mu p_nu² give |a_F|+|c_F|<=C delta_N. Thus every quadratic-kernel Taylor coefficient of momentum degree zero or two is O(delta_N).

For the cubic vertex, exact parity leaves a linear polynomial P1 plus terms of degree at least three. The degree-two lifted cubic Ward relation has defect O(delta_N). Its Hessian terms involve only the degree-zero and degree-two Hessian coefficients and bounded derivatives of the cosine generator, all O(delta_N). Therefore P1 is transverse in each leg up to coefficients O(delta_N).

Eliminate the third momentum by k=-p-q and write

    P1_(mu nu rho)=sum_sigma
               A_(mu nu rho;sigma)p_sigma
                +B_(mu nu rho;sigma)q_sigma.

In p-transversality the coefficients of p_mu q_sigma give B=O(delta_N); in q-transversality the coefficients of q_nu p_sigma give A=O(delta_N). This is the quantitative version of the exact polynomial lemma; no dimension-dependent inversion of a lattice operator is involved.

For the quartic vertex, parity leaves a constant tensor P0 plus terms of degree at least two. The degree-one quartic Ward relation has right side O(delta_N): the cubic-linear tensors are O(delta_N), and the Q term contains the O(delta_N) Hessian mass multiplied by one sine factor. The defect is also O(delta_N). Its left side contracts P0 with an arbitrary gauge momentum, so P0=O(delta_N).

Let T_(n,m)^F be the absolute midpoint moments of the lifted residual kernels as defined in the total-kernel note. Taylor's real-ray remainder now gives, for real sufficiently small simultaneous momenta,

    |Gamma_2^F,N(p)|
       <=C delta_N(1+|p|²)+C T_(2,4)^F |p|^4,
    |Gamma_3^F,N(p1,p2,p3)|
       <=C delta_N p_*+C T_(3,3)^F p_*³,
    |Gamma_4^F,N(p1,p2,p3,p4)|
       <=C delta_N+C T_(4,2)^F p_*²,                   (5.1)

where p_*=max_j|p_j|. Norm conventions only change fixed d/color constants. The original periodic tensors differ from the periodization of these lifted tensors by their exponentially small tails. Thus (5.1) describes their short-range part, with a separately controlled wrapping remainder; it is not an exact finite-torus zero-jet assertion.

For a semisimple product use one coefficient/reference per simple ideal, as in the exact theorem. A single beta is not asserted unless the simple-ideal coefficients coincide.

## 6. The discarded polynomial tail can itself be localized

This optional consequence concerns only fixed field degrees n<=4. Suppose the input has the actual connected J-cell coefficient family with exponent a0>0 and radius b. Expand E_H in scalar monomials of total degree n, and retain as the tail polynomial those monomials whose n differentiated bond slots have torus midpoint diameter>T. Keep the original declared carrier H.

For a connected J-cell carrier, its current-unit diameter is at most C_d J |H|, including fixed bond/cell collars. Hence a nonzero retained monomial requires |H|>=T/(C_d J). Cauchy's scalar monomial count gives its absolute coefficient norm on radius r<=b at most

    binom(D|H|+n-1,n)(r/b)^n ||E_H||_b.                 (6.1)

Choose any a_out<a0. Spend half of a0-a_out to absorb this fixed polynomial in |H|, and the other half on the lower bound for |H|. The resulting strict connected-carrier tail family satisfies

    ||Tail_n E||_(a_out;r)
       <= C(n,D,a0-a_out)(r/b)^n epsilon
             exp[-(a0-a_out)T/(2 C_d J)].               (6.2)

The full symmetrized derivative expansion reconstructs exactly the degree-n torus kernel tail in (2.2). This is a legitimate localization of the wrapping polynomial error, not a claim that the individual tail coefficients are gauge invariant. The same construction applies to an available strict reference family.

The principal short-range, Ward-canceled spatial remainder still requires its own bounded relocalization argument. Formula (6.2) does not supply that argument or an unchanged-cardinality-exponent estimate.

## 7. Settled scope and remaining interfaces

The finite-volume construction gives a real beta_N, an exact full invariant subtraction F_N=E_N-beta_N S_N, and exponentially small low-momentum defects for a symmetric short-range lift. It does not require an infinite-volume kernel subsequence. Its error constants explicitly retain the fixed grouping J.

The small defects are not literally zero at fixed N. No claim is made that they can be discarded under infinitely many ultraviolet steps without an additional summation or wrapping-sector argument. Along a geometric RG sequence the current torus lengths change, so exponential size errors may be summable; such bookkeeping must be proved in the chosen recursion.

Nothing here proves convergence of beta_N as N varies, regulator consistency of the activity family, a positive beta-function drift, or a norm contraction for the extracted quantum map. The remaining analytic issue is a bounded spatial remainder localization in a norm whose constants can be controlled after fixing J, possibly using the separately proved finite-q classical background semigroup.
