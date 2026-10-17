# Bounded finite periodization of invariant analytic interaction classes

17 October 2026. Research proof candidate for independent audit. This constructs a canonical vacuum-normalized finite-periodic analytic functional from an infinite translation-invariant interaction class. Its finite carrier norm does not increase, wrapping is counted exactly, and local gauge invariance passes. This is a representation theorem, not an identification with the finite output of a previously performed quantum integration.

## 1. Setup and assertions

Use the infinite activity space A_(a,b) and quotient Q_(a,b) of `activity_quotient_research.md`: finite connected nonempty carriers H in the J-cell graph Z^d, at most D scalar link/color coordinates per cell, and

    ||E||_(a,b)=sup_i sum_(H contains i) e^(a|H|)||E_H||_b.

The class is determined by the normalized total Phi_E on compact fields. Fix a positive integer N and the cell torus Lambda_N=(Z/NZ)^d; the underlying current lattice has period NJ. The period is compatible with the field-coordinate partition. All formulas count oriented positive links and internal coordinate types by their actual identifications. One may restrict to N>=3 if desired to avoid degenerate graph notation; the incidence formulas themselves include multiplicities at shorter periods.

Write pi_N for cell and coordinate projection. A periodic finite field A is identified with its infinite periodic lift A^per. This is a bounded field, not an ell1 field. Holomorphic functions below use the original scalar product polydisc of radius b.

The claims are:

* Every class with J-cell-translation-invariant normalized total has a translation-covariant representative with no increase of the norm of a chosen input representative.
* Its periodic normalized energy is independent of that covariant representative and its vacuum convention.
* It has a strictly supported connected finite carrier family with the same exponent a and norm at most the original representative norm. Thus the induced map from the translation-invariant infinite quotient to the finite quotient has operator norm at most one.
* Every finite derivative tensor at zero is the exact relative periodization of its infinite total tensor.
* Total spatial, color and local gauge symmetries pass. The gauge assertion is proved on the logarithmic chart domain, without needing a noncompact infinite gauge path.

The last section records what these statements do not identify.

## 2. A covariant representative by translation averaging

Let tau_t act on a family by translation of its carrier, field slots and coefficient, for t in the J-cell lattice. It is an isometry of A_(a,b). If [E] has a translation-invariant normalized total, then [tau_t E]=[E] for every t. Choose centered Følner cubes F_m in Z^d and put

    E^(m)=|F_m|^-1 sum_(t in F_m) tau_t E.               (2.1)

Its norm is at most ||E||. For fixed s,

    ||tau_s E^(m)-E^(m)||
       <= |(F_m+s) symmetric_difference F_m|/|F_m| *||E||,
                                                               (2.2)
which tends to zero. Each fixed carrier coefficient is a uniformly bounded holomorphic function on a fixed finite-dimensional polydisc. The countable Montel/diagonal argument of `analytic_interaction_compactness_research.md` gives a locally uniform limit E^cov_H for every H. Fatou, first over finite carrier collections and smaller radii and then to the open radius b, gives

    ||E^cov||_(a,b)<=||E||_(a,b).                        (2.3)

Equation (2.2) passes coefficientwise and proves exact translation covariance. For a compact input K, the sum of carriers of size greater than Q meeting K is bounded by 2|K|||E||e^(-aQ), uniformly in m. The finite remaining collection converges. Since Phi_(E^(m))=Phi_E, its limit is Phi_(E^cov)=Phi_E. The covariant limit therefore represents the same class. It need not be unique; uniqueness of the periodic normalized functional is proved below.

This averaging uses only J-cell translations. If the total has additional unit-current translations, signed permutations or color symmetries, they need not be imposed on the representative and will pass later through its total kernels or local gradient.

## 3. Exact density formula and carrier orbits

For a covariant E define the raw periodic total by

    U_N^E(A)=sum_(i in Lambda_N) sum_(H contains i)
                      |H|^-1 E_H(A^per|H).             (3.1)

Choose any fixed cell representatives for Lambda_N in this formula. Translation covariance makes the formula independent of that choice. The double series converges absolutely and in the supremum norm on the full open b polydisc, since it is bounded by N^d||E||. The canonical normalized energy is

    Phi_N^[E](A)=U_N^E(A)-U_N^E(0).                    (3.2)

Consider the orbits O of finite carriers under translations by N Z^d. A nonempty finite carrier has no nonzero translation stabilizer. Its size is constant along an orbit. Every point of a representative H corresponds to exactly one incidence pair (i,H') with i in the chosen fundamental cell and H' in O containing i. Consequently

    sum_(i in Lambda_N) sum_(H' in O, i in H') |H'|^-1=1.
                                                               (3.3)

Covariance and periodicity make E_(H')(A^per) equal along an orbit. Hence (3.1) is exactly one summand per carrier orbit:

    U_N^E(A)=sum_O E_H(A^per|H),    H any representative of O.
                                                               (3.4)

No factor |pi_N H|/|H|, no extra winding multiplicity, and no assumption that H embeds injectively in the torus is present.

For a nonempty connected torus carrier K, group the orbit summands with pi_N H=K and define

    E_(N,K)(A|K)=sum_(O:pi_N H=K) E_H(A^per|H).          (3.5)

The map A|K -> A^per|H simply repeats identified scalar coordinates and has maximum-norm operator norm one. Every summand is strictly supported on K and holomorphic on its original b polydisc. Projection preserves connectedness, although different old cells can coincide in K.

Fix one torus cell j and its chosen infinite lift. Each orbit whose projection contains j has at least one representative containing that lift. Choose one such representative from each orbit. Distinct orbits give distinct chosen carriers. Since |pi_N H|<=|H| and translated coefficients have the same norm,

    sum_(K contains j) e^(a|K|)||E_(N,K)||_b
       <=sum_(O: j in pi_N H) e^(a|pi_N H|)||E_H||_b
       <=sum_(H contains chosen j) e^(a|H|)||E_H||_b
       <=||E||_(a,b).                                  (3.6)

This proves both normal convergence of (3.5) and the exact no-loss anchored estimate. All wrapping coincidences have been paid by selecting one incidence per orbit, not by discarding multiplicities in the energy. Identity (3.3) already counted the full energy correctly.

The raw grouped coefficients in (3.5) retain their constants and satisfy (3.6). If each coefficient is separately normalized at zero, its norm can increase by a factor at most two. It is unnecessary to do that: the quotient evaluates its raw family using the normalized total (3.2). A raw vacuum value U_N^E(0) is not fixed by the infinite normalized class.

For example E_{\{i\}}=c at every cell is the zero normalized class, but (3.1) gives the raw constant N^d c. This elementary example prevents replacing (3.2) by a canonical unnormalized exponential without an additional vacuum convention.

## 4. Exact derivative periodization

Let K_n^E(i1,alpha1;...;in,alphan) be the infinite total derivative kernel at zero, with cell index and internal coordinate type separated. It is the absolutely convergent sum of derivatives of carriers containing all slots. The connected activity norm supplies, for every fixed n, absolute anchored summability of K_n and a positive spatial exponent, by the fixed-order Cauchy/counting argument in the quotient note. Constants may depend on n,D,J,a,b; there is no claim of a dimension-free all-order Taylor norm.

Fix a lift i1 of the first finite coordinate. Differentiating (3.4) in a periodic coordinate differentiates each occurrence of that coordinate among the old slots of H. For the first derivative, translate each occurrence of i1+Nz1 to i1. Each carrier through i1 appears exactly once. After this reanchoring, the other differentiated slots run over all their N-periodic lifts. Thus

    D^n U_N^E(0)[e_(i1,alpha1),...,e_(in,alphan)]
       =sum_(z2,...,zn in Z^d)
           K_n^E(i1,alpha1;
                  i2+Nz2,alpha2;...;in+Nzn,alphan).     (4.1)

Repeated finite slots cause the usual ordered multilinear derivatives, and the right side includes their coincident and distinct infinite lifts. They are not silently collapsed. There is no sum over a first-slot image because it has been fixed by reanchoring. Absolute anchored summability justifies all rearrangements. Alternatively differentiating the uniformly convergent finite-dimensional series in (3.1) first and using (3.3) gives the same formula.

In particular, if E is a null class, all its infinite K_n vanish for n>=1. Every derivative of Phi_N at zero is zero. Since (3.2) is holomorphic on a finite-dimensional connected b polydisc and vanishes at zero, it is identically zero. If E and F are any two covariant representatives of the same normalized class, their periodic normalized totals agree by this argument. Different translation-averaging subsequences therefore give the same answer.

Let Q^N_(a,b) be the finite activity quotient, using all nonempty connected torus carriers and equality of normalized totals. Combining (2.3),(3.6), and a representative arbitrarily close to the infinite quotient infimum gives a canonical linear map

    Per_N: Q_trans_(a,b) -> Q^N_(a,b),
    ||Per_N||<=1.                                      (4.2)

Linearity follows from the linearity of the total kernels and the normalized periodic functional; the covariant representative selection itself need not be linear. The scalar evaluation estimate is

    |Phi_N^[E](A)|<=2N^d ||[E]||_Q.                    (4.3)

The map is defined on translation-invariant classes, with the raw carrier family retaining its vacuum sector as explained after (3.6). It is not a choice of an unnormalized exponential.

There is also exact consistency of these normalized scalar energies under tiling. If q is a positive integer and A on Lambda_N is repeated on Lambda_(qN), the density at each root in (3.1) is N-periodic. Therefore

    Phi_(qN)^[E](A tiled)=q^d Phi_N^[E](A).             (4.4)

The same identity holds for a rectangular multiple with its corresponding volume ratio. This concerns the prescribed periodic functionals; it does not impose equality of arbitrary finite carrier assignments or identify unrelated regulator histories.

The grouped coefficients also stabilize exactly on every fixed lifted carrier. Let K be a fixed finite connected infinite carrier, and take N>4 diam(K)+4 in cell distance, with K represented in a central copy. The sets K+Nz are then disjoint and nonadjacent. If a connected H satisfies pi_N H=pi_N K, it lies in the union of these copies. Connectedness forces it into one copy, and surjectivity of its projection forces H to equal that copy. Thus (3.5) contains exactly its one carrier orbit and, under the lifted coordinate identification,

    E_(N,pi_N K)=E_K                                   (4.5)

for every sufficiently large N. This is an identity of raw holomorphic coefficients on the full original b polydisc. It makes local normal convergence of canonically periodized inputs immediate; no winding-tail estimate is needed for a fixed carrier. It does not assert norm convergence of the whole family or stabilization on carriers growing with N.

## 5. A direct local-gradient proof and gauge invariance

This section also proves representative independence without summing the entire Taylor series. For a fixed infinite coordinate i, define at every bounded interior field ||A||_infinity<=rho<b

    G_i^E(A)=sum_(H containing cell(i)) partial_i E_H(A|H).
                                                               (5.1)

Scalar directional Cauchy gives

    |G_i^E(A)|<=||E||_(a,b)/(b-rho).                    (5.2)

If A and B agree on a Q-cell neighborhood of i, every differing summand has a connected carrier of size at least Q up to a fixed convention constant. Thus

    |G_i^E(A)-G_i^E(B)|
       <=2||E||_(a,b)/(b-rho) * exp(-c a Q).             (5.3)

This supplies continuity under compact truncation of any bounded field. On compact fields G_i is the actual derivative of Phi_E. Therefore a null class has G_i=0 for all compact fields, and then, by (5.3), for every bounded interior field. This statement does not require covariance of the representative.

For a covariant representative, differentiate the orbit sum at an arbitrary periodic interior field, and reanchor the first differentiated occurrence as in Section4. It yields the exact formula

    partial_i U_N^E(A)=G_i^E(A^per).                    (5.4)

Both sides are independent of the chosen lift of i. Formula (5.4) gives another immediate proof that a null class periodizes to a constant raw total, hence to zero after normalization.

Now assume the infinite normalized total is locally gauge invariant on its logarithmic coordinate domain. For a fixed unit-current site v, let L_v(A) be its infinitesimal gauge vector field: it has nonzero entries only on the finitely many bonds incident to v and reads those local bond potentials. On compact fields the Ward equation is

    sum_(i incident to v) G_i^E(A) L_(v,i)(A)=0.         (5.5)

Take compact truncations of any bounded interior A. The finite incident set and its local generator values stabilize, and (5.3) passes the gradient terms to the limit. Hence (5.5) holds for every bounded interior field, including periodic fields. For a periodic gauge parameter, identify incident bonds with their actual torus orientations and multiplicities. Equation (5.4), periodic covariance, and (5.5) show that the finite total has zero derivative in every torus gauge direction:

    D Phi_N^[E](A)[L_lambda,N(A)]=0.                   (5.6)

This proof does not apply an infinite noncompact gauge path to Phi_E. It extends only a local gradient Ward identity, whose sums are absolutely convergent and whose gauge-site test has finite support.

Holomorphy of the infinitesimal logarithmic gauge generator is needed. If the given b lies within its fixed coordinate chart radius, (5.6) holds on the whole open b polydisc. For an arbitrary analytic interaction radius, keep full-b holomorphy of the periodized interaction and restrict the gauge assertion, explicitly, to b_g=min(b/2,r_log/2), where r_log is any fixed radius on which that generator is holomorphic. In the actual small-field setup b was already chosen inside this chart. Finite gauge invariance follows by integrating (5.6) along any gauge path whose transformed fields remain in the common chart/domain. No assertion about large gauge paths leaving that domain is made.

For completeness, differentiating (5.6) at zero also yields all finite nonlinear Ward identities coefficientwise in field degree. Equivalently, differentiate the infinite compact-field identity first. Each fixed degree contains finitely many local generator coefficients, nearest-neighbor shifts and coincident-slot embeddings of total kernels. Relative periodization in (4.1) commutes with these operations: summing lifts turns the infinite coincidence condition into the exact periodic coincidence condition, including all images. Hence the infinite zero Ward tensors periodize to zero. This is an all-degree statement at fixed degree, justified by anchored summability, not an appeal to a uniform absolute all-degree coefficient norm.

## 6. Other total symmetries

Translation covariance at the J-cell level is already built into the construction. If the infinite total has finer unit-current translations, point hypercubic symmetries or global color symmetries, its total K_n have the corresponding tensor covariance. The exact periodization (4.1) commutes with every symmetry preserving the chosen finite torus. The finite normalized Taylor series and analytic uniqueness therefore give the same symmetry of Phi_N. For negative bonds the actual logarithmic reversal is the signed change of the corresponding positive-bond coordinate. No invariance of individual torus coefficients E_(N,K) is required.

Reality on real fields passes through the same argument or a real covariant representative. A real representative can be selected by averaging with its complex-conjugate reflection, which does not increase the norm and preserves its real normalized class.

## 7. Exact conclusion and remaining finite-regulator interface

At the infinite interaction level, bounded periodization is now a definite construction: translation averaging supplies a covariant representative; the rooted density is an exact one-orbit sum; wrapping does not increase the anchored carrier norm; the normalized energy depends only on the class; and local gauge invariance holds on the specified finite chart. No volume limit or approximate Ward error is needed for these canonically periodized functionals.

This does not identify an unrelated actual finite-regulator activity family with this canonical periodization. Two finite-volume sequences can have the same subsequential infinite interaction while differing by small winding-supported terms at every finite size. The compactness theorem discards such terms in the local limit; it does not assert their exact absence. Similarly it does not identify finite stationary backgrounds, retained windows, Gaussian normalizations or gauge insertion factors with a periodized infinite construction.

Consequently, using Per_N inside a finite quantum integral still requires a history/normalization comparison between that integral's actual total and the canonically periodized total, or an independent construction using these periodized inputs from the outset. If raw exponentials are compared, their vacuum constants must also be specified separately. This note proves no quantum integration identity, no continuity of the actual quantum update on the quotient, and no infinite induction.
