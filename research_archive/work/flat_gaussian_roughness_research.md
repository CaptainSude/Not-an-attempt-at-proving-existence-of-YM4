# Ultraviolet roughness of the homogeneous constrained flat Gaussian

Research result for the already identified homogeneous flat operator, not an interacting construction. The proof below is finite-dimensional on every compatible periodic regulator and uses only the established flat identities and aliases. No external Gaussian-field regularity theorem is imported.

## 1. Exact field, measure and covariance normalization

Fix d=4, fine spacing eta=M^{-1}, odd M>=3, and a compatible periodic coarse lattice of unit spacing. Let n_c be its number of sites and n_f=M^d n_c the number of fine sites. Positive fine bonds and unoriented fine plaquettes are counted once, so there are d n_f bonds and binom(d,2)n_f plaquettes. Work first with one real color component in a basis orthonormal for the normalized trace. At the flat point all color components are identical independent copies. The full Lie-algebra result has N_color=N_c^2-1 copies.

The physical one-form Hilbert pairing is

    <A,B>_eta = eta^d sum_(positive fine bonds e) A_e B_e.

Let K=d^T d be the ordinary physical Maxwell precision, where

    (dA)_(x;mu,nu)=nabla_mu A_nu(x)-nabla_nu A_mu(x), mu<nu.

Let Q=Q_M^st, Q_0 the scalar block mean, and R the matched scalar source projection. Define the constrained slice and its covariance by

    X=ker Q intersect ker(R D^T),
    C=Gamma-D Z D^T=J_X (J_X^T K J_X)^(-1) J_X^T.

Here J_X is the isometric inclusion of X, and the second equality is the proved variational characterization of the selected covariance. The auxiliary penalty used to construct G_0 does not remain in the quadratic form on X. Let Z_f be the centered Gaussian on X with density proportional to

    exp[-(1/2)<Z_f,K Z_f>_eta]

relative to its physical Euclidean Lebesgue measure. The notation Z_f denotes the random field and must not be confused with the earlier scalar operator Z=G'RG'. Its covariance operator is C:

    E[<f,Z_f>_eta <Z_f,h>_eta]=<f,C h>_eta.

If C^{coord}_{ef} is the matrix that maps bond values to bond values, then

    E[Z_f(e) Z_f(f)] = eta^{-d} C^{coord}_{ef}.       (1.1)

This factor is essential. Equivalently, an orthonormal physical coordinate vector is eta^{-d/2} delta_e; the kernel of the physical sum representation is the actual point covariance. For any fine linear differential L with the same physical measure on its output coordinates,

    E ||L Z_f||_{2,eta}^2 = Tr(L C L^T).             (1.2)

The source bare action has quadratic term (1/2)<A,KA>_eta, as checked at Raw I:464–479,12756–12760,15643–15648. Thus a coupling factor exp[-S/g^2] makes the quadratic physical fluctuation A_fluc=g Z_f, with covariance g^2 C. No additional eta, factor two or color-normalization factor belongs in this statement. This identifies the selected homogeneous flat constrained Gaussian; it does not identify an interacting fluctuation law with this Gaussian.

## 2. Exact dimension of the constrained slice

For one color,

    dim X=(d-1)(n_f-n_c).                            (2.1)

Proof: Q is onto because its already constructed flat extension satisfies QH=I. Hence dim ker Q=d(n_f-n_c). The scalar source projection has

    ran R=(ran G' Q_0^T)^perp,
    G'=(L+a' Q_0^T Q_0)^(-1), L=D^T D, a'>0.

The block mean Q_0 is onto and G' is invertible, so rank R=n_f-n_c. Moreover

    L(ker Q_0)=ran R.                               (2.2)

For the inclusion, if Q_0 phi=0, then

    <L phi,G'Q_0^T c>
      =<phi,[I-a'Q_0^T Q_0 G']Q_0^T c>=0.

The restriction of L to ker Q_0 is injective, because the only periodic scalar Laplacian kernel consists of constants and a nonzero constant has nonzero block mean. Both spaces in (2.2) have dimension n_f-n_c, proving equality. For phi in ker Q_0, the cochain identity gives QD phi=D_c Q_0 phi=0, while

    R D^T D phi=R L phi=L phi.

Thus RD^T:ker Q -> ran R is onto. Rank-nullity now proves (2.1). The argument covers short compatible tori with the usual oriented incidence multiplicities. For M=1, Q=I and X={0}; all fluctuation claims below correctly vanish in that degenerate case.

## 3. Potential variance: averaged lower and uniform pointwise upper bounds

The fine Maxwell symbol obeys 0<=K<=4d M^2 I. Therefore every eigenvalue of its positive compression K_X is at most 4dM^2, and

    Tr C >= dim X/(4dM^2).

By (1.1)–(1.2), the average variance of one real color component over positive fine bonds is

    v_A := (d n_f)^(-1) sum_e E[Z_f(e)^2]
         = Tr C/(d n_c).

In d=4 this gives the explicit lower bound

    v_A >= (3/64)(M^2-M^(-2)).                      (3.1)

There is also a uniform pointwise upper bound

    E[Z_f(e)^2] <= C M^2                            (3.2)

for every fine bond, refinement, and compatible periodic volume. Here is a direct proof from the established canceled aliases.

In a real coarse Bloch fiber z in [-pi,pi]^d, take r in I_M^d, p_r=z+2pi r, and

    P_r=4M^2 sum_mu sin^2(p_(r,mu)/(2M)).

For r!=0, |p_(r,mu)|>=pi |r_mu| whenever r_mu!=0 and |p_(r,mu)/(2M)|<=pi/2. Thus

    P_r >= (4/pi^2)|p_r|^2 >=4|r|^2.              (3.3)

The earlier full inverse formula gives C<=Gamma<=G_0 and, fiberwise,

    G_0=F+beta E_a^(-1) beta^*,
    F=(L I+Q^T a Q)^(-1),

with fixed a>0. Its canceled central block F_00 is bounded uniformly; its high block satisfies F_hh<=diag_(r!=0)(P_r^(-1)I_d); and E_a>=c>0. The canceled beta formula has a bounded central entry and

    |beta_(r,mu)| <= C[|a_r|/|r|^3+|omega_(r,mu)|/|r|^2], r!=0.

The real scalar and bond averaging factors satisfy

    |a_r|+|omega_(r,mu)| <= C prod_nu(1+|r_nu|)^(-1).

For example this follows directly from the centered sine quotient, with the additional string average in omega bounded by one. Consequently sum_r |beta_(r,mu)|<=C: on the shell 2^k<=|r|_infinity<2^(k+1), the sum of the product envelope is O((1+k)^d), and the extra |r|^(-2) makes the shell series summable.

Evaluation at a within-cell fine point has alias coordinates v_r of modulus one in its selected orientation. Positivity of F gives

    v^*Fv <=2 v_0^*F_00 v_0+2 v_h^*F_hh v_h
           <=C+2 sum_(r!=0) P_r^(-1).

The beta term is at most C(sum_r |beta_(r,mu)|)^2<=C. In d=4, (3.3) and shell counting give sum_(r!=0)P_r^(-1)<=CM^2. This proves the fiber evaluation bound CM^2. Averaging it over the coarse Bloch grid proves (3.2).

For clarity about normalization, physical-cell Fourier reconstruction has F_M(z)_{sr}=exp(i p_r dot s/M), inverse M^{-d}F_M(z)^*. The factor M^{-d} in its coordinate diagonal is canceled by eta^{-d} in (1.1). Therefore the point covariance is precisely the average of v^*C(z)v over the coarse Bloch grid; no additional power of M occurs. The zero coarse fiber uses the already canceled formulas, with high P_r>0 and no central pole.

Combining (3.1)–(3.2), for M>=3,

    c eta^(-2) <= v_A <= C eta^(-2).              (3.4)

This proves an averaged lower bound and an upper bound at every point. It does not assert that every within-cell bond has the same variance or a pointwise lower bound at every bond. Coarse translation symmetry does make the within-cell variance pattern repeat.

## 4. Exact curl variance and first-difference variance

The variational inverse yields the exact trace identity

    Tr(K C)=Tr(K_X K_X^(-1))=dim X.                (4.1)

Since every positive plaquette is counted once,

    v_curl := [binom(d,2)n_f]^(-1)
                   sum_p E[(d Z_f)(p)^2]
            = dim X/[binom(d,2)n_c]
            = (2/d)(M^d-1).

In d=4,

    v_curl=(M^4-1)/2.                             (4.2)

This is for one real color component. Taking the normalized trace of the squared Lie-algebra curl multiplies the result by N_color. It is an exact identity on every compatible periodic volume, not merely an asymptotic alias calculation.

Let nabla contain all d physical first differences of all d bond components. The elementary inequality ||dA||_2^2<=2||nabla A||_2^2 implies

    Tr(nabla C nabla^T)>=dim X/2.

On the other hand, positivity C<=G_0 and the proved uniform derivative sandwich give

    ||nabla C nabla^T||_{2->2}<=C.

Thus its trace is at most C d^2 n_f. Dividing as in (1.2) proves

    c M^4 <= (d^2 n_f)^(-1)
        sum_(x,mu,nu) E[(nabla_mu Z_(f,nu)(x))^2]
        <= C M^4,                                (4.3)

for M>=3. The same operator bound and (1.1) give the stronger pointwise upper bound

    E[(nabla_mu Z_(f,nu)(x))^2] <= C eta^(-4)       (4.4)

for every fine first-difference coordinate. At least one curl coordinate has variance no smaller than (4.2), and at least one first-difference coordinate has variance of order eta^{-4}. No independence of such coordinates is required.

## 5. A fixed physical smooth ball has vanishing Gaussian probability

Choose one real color component and a plaquette whose curl variance is at least (4.2). If the complete physical norm N_alpha(g Z_f) is at most r, its selected curl coordinate has absolute value at most C_color r. A centered one-dimensional Gaussian of variance sigma^2 has

    P(|Y|<=t)<=min(1,sqrt(2/pi)t/sigma).

It follows that, uniformly in the periodic volume and M>=3,

    P(N_alpha(g Z_f)<=r)
          <=min(1,C r eta^2/g).                   (5.1)

Already the potential variance lower bound gives P(||g Z_f||_infinity<=r)<=min(1,C r eta/g). The curl estimate (5.1) is stronger for the smooth ball. It uses just one deterministic selected Gaussian marginal; no correlation, concentration or independence assumption is concealed.

For any fixed g>0 and fixed r, (5.1) tends to zero as eta decreases. The same conclusion holds for any positive coupling sequence satisfying g(eta)/eta^2 -> infinity, including logarithmically decreasing examples if one assumes such a trajectory. No running-coupling theorem is claimed here. The estimate does not make that conclusion for arbitrary much faster vanishing couplings.

This explicitly explains the integration boundary: a small smooth classical background and typical fine quantum fluctuations are different objects. The uniform N_alpha minimizer ball proved earlier cannot be used as a domain containing typical quadratic fluctuations at a fixed or slowly decreasing coupling.

The same bound (5.1) holds with N_alpha(A_0+g Z_f) for any deterministic background A_0, uniformly in A_0. The selected Gaussian curl is then restricted to an interval with the same length and a shifted center; the maximum-density estimate is independent of that center. This strengthened form is used in the independently audited qg- fragment.

## 6. Natural microscopic rescaling and its limits

Equations (3.2),(4.4) show that the local dimensionless variables

    eta Z_f(e),        eta^2 nabla_mu Z_(f,nu)(x)

have uniformly bounded variances, and their averaged variances are bounded below by positive constants. For the physical fluctuation g Z_f their root-mean-square sizes are O(g). The first variable is the linearized fine link angle; eta^2 g dZ_f is the linearized plaquette angle. This statement is linear Gaussian power counting, not a control of the full nonlinear plaquette.

In microscopic coordinates a natural complete norm is

    ||eta Z_f||_infinity + ||eta^2 nabla Z_f||_infinity
                        +eta^(2+alpha)[nabla Z_f]_alpha.       (6.1)

On a fine lattice the last term is at most twice the second (up to fixed orientation/collar constants), since distinct sampled points are separated by at least eta. On a fixed microscopic block containing a fixed number of fine sites, all coordinates in (6.1) form a fixed-dimensional Gaussian vector with uniformly bounded covariance and moments. Multiplication by g scales these estimates by g.

A unit physical coarse cell contains M^4 fine sites; it is not such a fixed-dimensional block. From the uniform pointwise upper bounds alone, a union bound gives, for any set of N tested rescaled value/first-difference/color coordinates,

    P(max |rescaled coordinate|>t)<=2N exp(-c t^2).             (6.2)

Consequently a whole physical-cell supremum can be controlled from above at a scale O(sqrt(log M)), with suitable constants, and a whole finite regulator introduces its total tested coordinate count. This is an upper tail bound, not an independence-based matching lower estimate. It does not produce a cutoff polymer expansion, strict background locality, a nonflat covariance theorem or a Yang–Mills quantum continuum construction.

## 7. Proof dependencies and remaining boundary

The only substantive previous inputs are: the matched variational covariance C on X; QH=I and QD=D_cQ_0; the scalar source projection formula; the canceled full G_0 aliases and their real bounds; and the uniform first-derivative G_0 sandwich. These were proved in the flat inverse, scalar gauge and constrained-Schauder modules. The rank argument and exact curl trace require no Fourier asymptotic. Original-source action/pairing normalization was checked in `wilson_source_normalization_research.md` at the pinned deposit.

This note establishes the ultraviolet roughness of that explicit homogeneous flat constrained Gaussian. It does not identify the covariance at arbitrary nonflat minimizing backgrounds, integrate Haar/Jacobian factors, bound nonlinear gauge interactions on typical rough fields, or prove the source's full retained-domain Gaussian matching. Those are the next genuinely quantum interfaces.
