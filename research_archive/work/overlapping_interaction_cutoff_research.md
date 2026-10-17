# Overlapping interactions in the Gaussian cutoff expansion

Research note, 17 October 2026. The root and theorem-audit agents independently checked this abstract derivation; the saved audits are overlapping_interaction_cutoff_audit.md and overlapping_interaction_tunable_audit.md. A harmless intermediate decay exponent was corrected after review. This is an internally audited research proof, not external certification. It extends the disjoint-cell theorem in interaction_cutoff_research.md. All hypotheses concern a fixed-dimensional cell Gaussian and explicitly bounded local multipliers. No claim is made that the deposited Yang--Mills fluctuation variables or coefficients satisfy them.

## 1. Conclusion and the issue resolved

Overlapping interaction supports can be handled without making the Gaussian cell dimension depend on their size. First group the chosen interaction factors by overlap connectivity. Then apply the covariance forest formula to the resulting disjoint molecules, but expand each forest derivative into its original cell endpoints before using Cauchy's estimate.

The factorial at a molecule is then the product of factorials of its individual cell degrees. Summing endpoint assignments at a molecule of size m and degree d gives the rising factorial (m)_d, rather than the crude m^d d!. Its rooted-tree generating function costs only an exponential in m. A fixed exponential support weight in the interaction norm therefore suffices, even for arbitrarily large supports.

The theorem below proves a convergent logarithm, a support-summable bound, and an O(interaction norm) comparison with the pure Gaussian cutoff logarithm. The support labels identify fluctuation cells. Strict locality in a background-dependent covariance is a separate issue.

## 2. Explicit hypotheses and statement

Let Lambda be a finite set of cells with metric d. Every cell has D real coordinates, where D is fixed. Let A range in an open complex background domain. The complex symmetric covariance C(A) is holomorphic and satisfies

\[
 \operatorname{Herm}C(A)\ge\lambda I,\qquad
 \|C(A)\|\le\Lambda_0,\qquad 0<\lambda\le\Lambda_0.
 \tag{2.1}
\]

For distinct cells suppose

\[
 \|C_{ij}(A)\|\le J_{ij}=J_{ji},\qquad
 A_\kappa=\sup_i\sum_{j\ne i}e^{\kappa d(i,j)}J_{ij}<\infty.
 \tag{2.2}
\]

Put J_ii=0. All bounds are uniform in volume and background. For a finite nonempty set S, ell(S) denotes minimum metric spanning-tree length, with ell({i})=0.

The cutoff is fixed on the real integration variables:

\[
 \chi_i(x_i)=\mathbf1_{\{\|x_i\|_2\le R\}},\qquad
 \chi_Y=\prod_{i\in Y}\chi_i.
\]

There is a finite family of labelled nonempty supports Y and interactions V_Y(A,x_Y), measurable in real x_Y and holomorphic in A on the cutoff region. Distinct labels may have the same support. Assume the uniform bounds

\[
 v_Y=\sup_{A,\;\chi_Y=1}|e^{V_Y(A,x_Y)}-1|<\infty.
 \tag{2.3}
\]

No real-field derivatives are assumed, and V_Y need not be defined outside its cutoff region. Define w_Y=chi_Y(e^{V_Y}-1), extended by zero.

Use the normalized complex Gaussian density and its analytic determinant branch as in gaussian_cutoff_cluster_research.md. Set

\[
 \delta=\lambda/2,\qquad V_*=8\Lambda_0^2/\lambda,\qquad
 K_G=(2V_*/\lambda)^{D/2},
\]
\[
 p_R=2^{D/2}e^{-R^2/(4V_*)},\qquad
 \tau=K_Gp_R,\qquad c_G=e^2/\delta,
\]
\[
 \epsilon=\sup_i\sum_{Y\ni i}
       v_Y K_G^{|Y|}e^{4|Y|+\kappa\ell(Y)},\qquad
 \eta=e^3\tau+\epsilon,
\]
\[
 \eta_*=\frac1{4\max(1,c_GA_\kappa)}.
 \tag{2.4}
\]

The interaction sum counts labels. This is an explicit sufficient norm, not an optimal one.

**Theorem.** If eta <= eta_*, then

\[
 Z_V(A)=\mathbb E_{C(A)}
       \left[\prod_{i\in\Lambda}\chi_i\,
                    \exp\Big(\sum_YV_Y\Big)\right]
\]

is nonzero and has the logarithm determined by a convergent expansion

\[
 \log Z_V(A)=\sum_{\varnothing\ne X\subset\Lambda}U_V(X;A),
\]
\[
 \sup_i\sum_{X\ni i}
 e^{\kappa\ell(X)+|X|}\|U_V(X;\cdot)\|_\infty
 \le 2\eta.                                      \tag{2.5}
\]

The proof actually yields eta on the right; the factor 2 leaves a harmless reserve. All constants are independent of the number and sizes of supports.

If, more strongly,

\[
 e^3\tau\le\eta_*/4,\qquad \epsilon\le\eta_*/4,
 \tag{2.6}
\]

then the canonical activities from the same expansion satisfy

\[
 \sup_i\sum_{X\ni i}e^{\kappa\ell(X)+|X|}
       \|U_V(X;\cdot)-U_0(X;\cdot)\|_\infty
 \le 8\epsilon,                                  \tag{2.7}
\]

where U_0 is the pure Gaussian cutoff expansion. These statements also hold for a countable labelled interaction family by absolutely convergent finite-family limits under the same norm bound, defining the integrand by the product of its bounded multipliers on the cutoff. This does not assert convergence of the chosen logarithms V_Y themselves; their values can differ by integer multiples of 2 pi i.

## 3. Exact preliminary expansion into disjoint molecules

Write q_i=-1_bad,i. The exact identity

\[
 \prod_i\chi_i\,e^{\sum_YV_Y}
   =\prod_i(1+q_i)\prod_Y(1+w_Y)                 \tag{3.1}
\]

holds pointwise. Any term containing both q_i and w_Y with i in Y vanishes.

For a nonempty support S define the bounded molecule functional

\[
 a_S(x_S)=
 \sum_{\substack{\mathcal F\ne\varnothing:\;
       \cup_{Y\in\mathcal F}Y=S\\
       \mathcal F\text{ overlap-connected}}}
       \prod_{Y\in\mathcal F}w_Y(x_Y),
\]
\[
 M_S=
 \sum_{\substack{\mathcal F\ne\varnothing:\;
       \cup_{Y\in\mathcal F}Y=S\\
       \mathcal F\text{ overlap-connected}}}
       \prod_{Y\in\mathcal F}v_Y.                  \tag{3.2}
\]

The families in these finite sums use each interaction label at most once. Connectivity means the intersection graph on the chosen supports is connected. Then |a_S|<=M_S. Define f_S=a_S for nonsingletons and f_{ {i} }=a_{ {i} }+q_i. Equation (3.1) becomes exactly

\[
 \sum_{\mathcal P\ {\rm pairwise\ disjoint}}
                         \prod_{S\in\mathcal P}f_S(x_S).
 \tag{3.3}
\]

Every nonzero original term has a unique such grouping: the overlap components of its interaction family, together with its bad singleton marks. There is no replacement of the original Gaussian variables by a larger-dimensional block estimate.

The useful primitive numerical weights are

\[
 b(S)=K_G^{|S|}M_S+\tau\mathbf1_{\{|S|=1\}}.
 \tag{3.4}
\]

### Lemma 3.1: the overlap-animal bound

If epsilon<=1, then

\[
 \sup_i\sum_{S\ni i}b(S)e^{\kappa\ell(S)+3|S|}
 \le e^3\tau+\epsilon=\eta.                       \tag{3.5}
\]

**Proof.** Put

\[
 u_Y=v_YK_G^{|Y|}e^{3|Y|+\kappa\ell(Y)}.
\]

For an overlap-connected family, trees on its individual supports combine to a connected graph on their union. Consequently

\[
 \ell(\cup Y)\le\sum_Y\ell(Y),\qquad
 |\cup Y|\le\sum_Y|Y|.
\]

Since K_G>=1, the interaction part of the left side of (3.5) is bounded by the sum of products of u_Y over overlap-connected families whose union contains i.

Dominate each such family by all rooted spanning trees of its intersection graph, choosing a root support containing i, and then drop the distinct-label restriction. The usual exponential generating series for these nonnegative rooted trees has majorant

\[
 T_Y=u_Y\exp\left(\sum_{Z:\,Z\cap Y\ne\varnothing}T_Z\right).
 \tag{3.6}
\]

This identity can instead be read as monotone iteration starting with T_Y^(0)=u_Y, so no convergence is presumed. If T_Z<=u_Z e^{|Z|}, then

\[
 \sum_{Z:\,Z\cap Y\ne\varnothing}T_Z
 \le\sum_{j\in Y}\sum_{Z\ni j}u_Ze^{|Z|}
 \le\epsilon |Y|\le |Y|.
\]

Thus T_Y<=u_Ye^{|Y|} at every iteration and at the limit. Summing over root supports containing i gives at most epsilon. A connected family is counted at least once by this rooted-tree majorant; additional roots, spanning trees and repeated labels only increase it. Adding the bad singleton contribution proves (3.5). ∎

## 4. Covariance forests with cell-resolved derivatives

Fix pairwise disjoint nonempty primitive supports S_1,...,S_n. Between distinct molecules introduce one covariance parameter s_ab multiplying every block C_ij with i in S_a, j in S_b; retain every covariance block internal to each S_a.

A partition mask in these molecule parameters gives a direct sum of actual principal submatrices of C. Its convex hull therefore preserves (2.1). The BKAR forest formula applies on this convex hull. At a forest mask the covariance is block diagonal over the forest components, so the product of the functions f_{S_a} factorizes exactly. This gives the usual cumulant identity, now for the disjoint primitive supports.

Consider a tree T on the n molecules. Expand each derivative with respect to s_ab into its individual cell endpoint derivatives:

\[
 \partial_{s_{ab}}=\sum_{i\in S_a,\;j\in S_b}
                                     \partial_{z_{ij}}.
 \tag{4.1}
\]

Here z_ij multiplies just C_ij and C_ji. Choose one endpoint pair for every tree edge, and let d_i be the number of chosen pairs incident on cell i. No endpoint pair is repeated, since the molecule graph is a tree and the supports are disjoint.

At the real BKAR mask allow independent complex increments of radii

\[
 r_{ij}=\frac{\delta}{\max(d_i,d_j)J_{ij}}          \tag{4.2}
\]

for the chosen pairs; an edge with J_ij=0 has zero derivative and is omitted. Each block row and column of the total covariance perturbation has sum at most delta. Its operator norm is at most delta. Thus every covariance on this product polydisc obeys

\[
 \operatorname{Herm}M\ge\lambda I/2,\quad
 \|M\|\le2\Lambda_0,\quad
 \operatorname{Herm}M^{-1}\ge V_*^{-1}I,\quad
 |\det M|\ge(\lambda/2)^{D|\cup S_a|}.
 \tag{4.3}
\]

The density modulus is bounded by K_G to the number of cells times an independent product Gaussian of covariance V_*I in each cell. Non-singleton molecule functions are bounded by M_S. For a singleton use |f_i|<=M_i+1_bad,i and the independent Gaussian tail bound p_R. Therefore, on this entire product polydisc,

\[
 \left|\mathbb E_M\prod_a f_{S_a}\right|
 \le\prod_a b(S_a).                              \tag{4.4}
\]

Cauchy's estimate, with each chosen covariance edge differentiated once, gives

\[
 \left|\partial_{T,\ {\rm endpoints}}
                   \mathbb E_{C(s)}\prod_a f_{S_a}\right|
 \le c_G^{n-1}\prod_a b(S_a)
                 \prod_i d_i!\prod_{ij\in T}J_{ij}.
 \tag{4.5}
\]

Indeed max(d_i,d_j)<=d_i d_j for positive endpoint degrees, so the product of the max factors is at most product_i d_i^{d_i}. Use d^d<=e^d d! and sum_i d_i=2(n-1). Degree-zero cells contribute 0!=1.

This is the essential refinement. Neither the radius assignment nor the factorial in (4.5) uses the degree of a whole molecule.

The mixed derivative is of the Gaussian covariance only. The cutoff indicators and real-field interaction multipliers are never differentiated. All bounds therefore hold for the merely measurable bounded multipliers in Section 2.

## 5. Exact regrouping into Gaussian-connected polymers

Apply the molecule forest formula to every term of (3.3). Its forest components give disjoint unions X. Grouping each component by its union gives activities zeta(X) and the exact hard-core gas

\[
 Z_V=\sum_{\mathcal Q\ {\rm pairwise\ disjoint}}
                                        \prod_{X\in\mathcal Q}\zeta(X).
 \tag{5.1}
\]

For each X, zeta(X) is the sum over partitions of X into disjoint primitive supports and over trees on that primitive family, with the BKAR integrals of their mixed derivatives. A singleton primitive family uses its un-interpolated expectation.

The next lemma is a positive tree estimate, applied to the absolute bound (4.5). It proves convergence uniformly without assuming a maximum primitive support size.

### Lemma 5.1: rooted endpoint-factorial trees

Let b(S)>=0 satisfy

\[
 \sup_i\sum_{S\ni i}
      b(S)e^{\kappa\ell(S)+3|S|}\le\eta.
 \tag{5.2}
\]

If eta<=1/[4 max(1,c_G A_kappa)], then the activities in (5.1) satisfy

\[
 \sup_i\sum_{X\ni i}
      |\zeta(X)|e^{\kappa\ell(X)+2|X|}\le\eta.      \tag{5.3}
\]

**Proof.** At a rooted tree on the primitive supports, retain its incoming endpoint cell at every nonroot molecule. For now permit repetitions and overlaps of primitive supports. Dropping the original disjointness restrictions only enlarges the positive majorant.

Put

\[
 \widehat b(S)=b(S)e^{\kappa\ell(S)+2|S|},\qquad
 \widehat J_{ij}=e^{\kappa d(i,j)}J_{ij}.
\]

The support and edge weights dominate the desired union weight: join spanning trees of the S's with the chosen covariance edges. Thus ell(union S) is at most the sum of their internal lengths and endpoint edge lengths; also |union S|<=sum |S|.

Let F_i majorize planted trees whose root molecule contains cell i and has one extra incoming half-edge at i. Its extra half-edge has no covariance weight; it only increments the degree at i. If

\[
 t_k=c_G\sum_j\widehat J_{kj}F_j,
\]

then the exact vertex generating function gives the recursive majorant

\[
 F_i=\sum_{S\ni i}\widehat b(S)
             \frac1{1-t_i}\prod_{k\in S}\frac1{1-t_k}.
 \tag{5.4}
\]

For completeness, if a vertex has n_k outgoing child edges at cell k, its unordered-child factor cancels the n_k! coming from their permutations. The cell-degree factorial is n_k! at an ordinary cell and (n_i+1)! at the incoming cell. The residual factors are respectively 1 and n_i+1. Summing the nonnegative geometric series gives (5.4). Equivalently, start with ordered children weighted by 1/(total child number)!, sum their endpoint assignments, and group them by the counts n_k. This is the standard rooted labelled-tree exponential generating series. Repeated labels and overlaps are allowed only in the majorant.

Define the series by height truncation. If every F_j<=2eta, then

\[
 t_k\le2c_GA_\kappa\eta\le1/2.
\]

Consequently

\[
 F_i\le 2\sum_{S\ni i}\widehat b(S)2^{|S|}
 \le2\sum_{S\ni i}\widehat b(S)e^{|S|}
 \le2\eta.
 \tag{5.5}
\]

This proves convergence of all planted majorants. At the unplanted root there is no extra incoming half-edge, so its generating function is only product_k(1-t_k)^(-1). Summing unplanted root molecules containing i is therefore bounded by

\[
 \sum_{S\ni i}\widehat b(S)2^{|S|}\le\eta.         \tag{5.6}
\]

For the original disjoint primitive family whose union contains i, exactly one primitive support contains i. Root the tree there. Its contribution is included in (5.6). This proves (5.3).

One way to see directly why this differs from the failed large-block estimate is to take all t_k=t. For a molecule of m cells the unplanted generating function is (1-t)^(-m). The coefficient at total degree d is (m)_d/d!, rather than m^d. The planted version is (1-t)^(-m-1). ∎

## 6. The logarithm and the quantitative interaction comparison

Apply Lemmas 3.1 and 5.1. The effective gas satisfies (5.3), with eta<=1/4. For the weighted activities

\[
 z'(X)=|\zeta(X)|e^{\kappa\ell(X)+|X|},
\]

the Kotecky--Preiss condition with size function a(X)=|X| follows:

\[
 \sum_{Y:\,Y\cap X\ne\varnothing}z'(Y)e^{|Y|}
 \le |X|\eta\le |X|.                             \tag{6.1}
\]

Its absolutely convergent Mayer logarithm, grouped by the union of its polymers, defines U_V. A connected overlap cluster has union length at most the sum of its polymer lengths, and union size at most their summed sizes. To anchor the union at i, sum over a distinguished polymer containing i. The pinned cluster estimate gives

\[
 \sup_i\sum_{X\ni i}e^{\kappa\ell(X)+|X|}
                   |U_V(X)|
 \le\sup_i\sum_{Y\ni i}
        |\zeta(Y)|e^{\kappa\ell(Y)+2|Y|}
 \le\eta.
 \tag{6.2}
\]

These estimates apply with the uniform background supremum taken at every stage. They prove holomorphy by locally uniform convergence, and identify Z_V with the exponential of this logarithm. In particular Z_V is nonzero. This proves (2.5).

For the comparison, replace each w_Y by t w_Y, retaining q_i. This interpolates bounded interaction multipliers, not a possibly unbounded exponent. The partition function equals Z_0 at t=0 and Z_V at t=1. Its weighted interaction norm is |t|epsilon. If epsilon>0 choose

\[
 \rho=\eta_*/(2\epsilon)\ge2.
\]

Under (2.6), all previous bounds hold uniformly for |t|<=rho because eta(t)<=3eta_*/4. The canonical activity vector U(t) is holomorphic in the Banach space with the rooted norm in (2.5), and its norm is at most 2eta_*. Banach-valued Cauchy gives

\[
 \|U(1)-U(0)\|
 \le\frac{2\eta_*}{\rho-1}
 \le8\epsilon.
 \tag{6.3}
\]

If epsilon=0 the comparison is immediate. At t=0, only bad singleton primitives remain, so this is exactly the pure Gaussian cutoff forest/Mayer construction, not an arbitrary alternative logarithm.

## 7. Scope, uses and remaining interfaces

1. Finite-range interactions are covered, but finite range is not required. Arbitrarily large and overlapping supports are allowed under the explicit weighted norm (2.4). If u_Y=sup_cutoff|V_Y|<=1, the bound v_Y<=2u_Y converts a weighted interaction estimate into the theorem's hypothesis.

2. The constants depend on the fixed original cell dimension D, the covariance spectrum, and A_kappa. They do not acquire an additional dependence on D|Y| beyond the explicitly budgeted factor K_G^|Y| in the activity norm. Choosing one microscopic cell whose dimension grows with the ultraviolet regulator would not meet the stated uniform hypotheses.

3. The proof does not differentiate real-field interaction factors. Thus bounded measurable cutoff-local multipliers suffice. Background holomorphy is needed only for the analytic conclusion and comparison; a fixed-background version needs only the stated sup bounds.

4. The covariance may depend on the entire background. The support X here denotes the cells used by the fluctuation observable/expansion, not automatically the background variables on which U_V(X) depends. Exponential covariance decay alone cannot imply strict background locality, as already explained in gaussian_cutoff_cluster_research.md.

5. Sections 9--11 prove the strict-background-support extension under the explicit small-local-precision and product-domain hypotheses stated there, with each interaction reading background only in its support. They check that the density support algebra and formal forest identities do apply to molecule masks and cell-resolved perturbation polydiscs. This does not verify those extra hypotheses for an actual Yang--Mills precision matrix.

6. For the actual Yang--Mills application one must separately exhibit independent fixed-dimensional fluctuation cells, the uniform complex covariance spectrum and summability, and the weighted local multiplier bound at the precise cutoff and background domain. Neither current pointwise inverse estimates nor a global interaction stability estimate alone verifies this full package. Moving domains, constraints and determinant normalizations remain part of that match.

7. This proof does not use the CMP116 specialized resummation. It supplies an abstract alternative when the stronger bounded-multiplier weighted norm is available. Whether that norm is natural or economical for the deposited activities is a separate source calculation.

## 8. Sources and proof provenance

The only imported general expansion tools are the covariance forest formula and the hard-core polymer convergence theorem. The density estimate, molecule expansion, endpoint factorial count and two rooted-tree majorants are explicitly proved above, using the already audited Gaussian constants.

- A. Abdesselam and V. Rivasseau, Trees, forests and jungles: a botanical garden for cluster expansions, arXiv:hep-th/9409094. https://arxiv.org/abs/hep-th/9409094
- A. Abdesselam, BKAR formula notes, Theorem 1, pp. 1--3; in particular the convex hull of partition masks is the relevant interpolation domain. https://mabdesselam.github.io/BKAR.pdf
- R. Kotecky and D. Preiss, Cluster expansion for abstract polymer models, Communications in Mathematical Physics 103 (1986), 491--498. https://doi.org/10.1007/BF01211762
- Local antecedents: gaussian_cutoff_cluster_research.md, Sections 3--8, and interaction_cutoff_research.md, Sections 4--6 and 9.

No original Yang--Mills source theorem has been silently used to assert the actual coefficient or coordinate hypotheses.

## 9. Strict background support: exact additional hypotheses

The extension anticipated in Section 7.5 can be proved under the already used small-local-precision assumptions. This section checks the mask and algebra interfaces, rather than treating them as automatic. The notation for the precision perturbations is changed to B_Y to distinguish them from interaction exponents V_Y.

Let

\[
 P(A)=P_0+\sum_Y B_Y(A|_Y),\qquad C_0=P_0^{-1},
\]

where the baseline C_0 is complex symmetric, independent of every background coordinate, and

\[
 \operatorname{Herm}C_0\ge\lambda I,\qquad \|C_0\|\le\Lambda_0.
 \tag{9.1}
\]

The background domain is a product domain. Each B_Y is complex symmetric, has rows and columns in Y, and reads only background coordinates in Y. Fix 0<kappa<m and assume

\[
 K=\sup_b\sum_c e^{(\kappa+2m)d(b,c)}\|(C_0)_{bc}\|<\infty,
\]
\[
 \nu=\sup_b\sum_{Y\ni b}\sum_{c\in Y}
       e^{(\kappa+2m)\ell(Y)}\|(B_Y)_{bc}\|_\infty<\infty.
 \tag{9.2}
\]

These are the baseline and precision norms of gaussian_cutoff_locality_research.md. Symmetry also bounds columns. Define

\[
 \delta=\lambda/4,\quad V_*=8\Lambda_0^2/\lambda,\quad
 J_{bc}=K e^{-m d(b,c)}\ (b\ne c),
\]
\[
 A_\kappa=K\sum_{z\ne0}e^{-(m-\kappa)|z|},\qquad
 \bar K=K+\delta,\qquad a=\lambda/2,
\]
\[
 s=\min\{m/2,\;aem/(4\bar K)\},\qquad
 L=\frac4\lambda\sum_{z\in\mathbb Z^d}e^{-s|z|}.
 \tag{9.3}
\]

Require K nu<1 and, with

\[
 v=\frac{K^2\nu}{1-K\nu},\quad
 v_1=v(1+\delta/K),\quad u=Lv_1,\quad
 w=\frac{L^2v_1}{1-u},
\]

require

\[
 v_1\le\lambda/4,\qquad u\le1/2,\qquad w\le1/(2V_*).
 \tag{9.4}
\]

These conditions are fixed before increasing the cutoff. Let C(A)=P(A)^(-1), defined by its convergent Neumann series.

In addition to the multiplier assumptions in Section 2, each V_Y must read background only in Y. Set

\[
 \widehat K_G=(8V_*/\lambda)^{D/2},\qquad
 \widehat p_R=2^{D/2}e^{-R^2/(8V_*)},\qquad
 \widehat\tau=\widehat K_G\widehat p_R,
\]
\[
 \widehat\epsilon=\sup_i\sum_{Y\ni i}
    v_Y\widehat K_G^{|Y|}e^{4|Y|+\kappa\ell(Y)},\qquad
 \widehat\eta=e^3\widehat\tau+\widehat\epsilon,
\]
\[
 c_G=e^2/\delta,\qquad
 \widehat\eta_*=[4\max(1,c_GA_\kappa)]^{-1}.
 \tag{9.5}
\]

**Strict-support theorem.** Under (9.1)--(9.4) and
widehat eta<=widehat eta_*, there are connected lattice supports H and
holomorphic functions E_{Lambda,H}(A|_H) such that

\[
 \log Z_V(A)=\sum_H E_{\Lambda,H}(A|_H),\qquad
 \sup_b\sum_{H\ni b}e^{a_*|H|}\|E_{\Lambda,H}\|_\infty
 \le2S_{\kappa/2}\widehat\eta,
\]
\[
 a_*=\min(1/2,\kappa/4),\qquad
 S_{\kappa/2}=\sum_{z\in\mathbb Z^d}e^{-(\kappa/2)|z|}.
 \tag{9.6}
\]

The support may be taken in the lattice hull of Lambda if needed. Under the quarter budgets
e^3 widehat tau<=widehat eta_*/4 and widehat epsilon<=widehat eta_*/4, the same canonical choice satisfies

\[
 \sup_b\sum_{H\ni b}e^{a_*|H|}
       \|E_{\Lambda,H,V}-E_{\Lambda,H,0}\|_\infty
 \le8S_{\kappa/2}\widehat\epsilon .
 \tag{9.7}
\]

These are bounds on variable background support, not volume consistency or an actual Yang--Mills source match.

## 10. Why the density algebra applies to molecule masks

For a nonempty moment support M and finite background support X, let ell_M(X) be minimum forest length on M union X with every component meeting M. Define the root algebra

\[
 \|F\|_{\mathcal B_M}
    =\sum_X e^{\kappa\ell_M(X)}\|F_X\|_\infty,\qquad
 (FG)_Z=\sum_{X\cup X'=Z}F_XG_{X'}.
 \tag{10.1}
\]

Every F_X reads only A|_X. The product-domain assumption makes its supremum well defined independently of omitted coordinates. Root inclusion is contractive, and union convolution is submultiplicative because ell_M is subadditive under support union.

Expand the precision inverse in its B_Y terms, retaining their labels. For endpoints b,c in M, the path estimate gives

\[
 \max\left\{\sup_b\sum_{c\in M},\;\sup_c\sum_{b\in M}\right\}
 e^{2m d(b,c)}
       \|[C(A)-C_0]_{bc}\|_{\mathcal B_M}
 \le v.                                             \tag{10.2}
\]

This shorthand denotes the maximum of the two weighted row/column sums. To verify it, a term C_0 B_{Y_1} C_0 ... B_{Y_j} C_0 connects all its background labels to its two endpoints. If its covariance-link distances and the internal support tree lengths sum to L_path, then ell_M(union Y)<=L_path and d(b,c)<=L_path. The total weight is bounded by exp[(kappa+2m)L_path], so successive weighted matrix sums give K^(j+1)nu^j; summing gives v. No assumption on the number of primitive molecules is involved.

At a molecule BKAR point, let sigma_bc be its induced mask on the individual cells of M. It is one on each primitive molecule and has the BKAR values between molecules. Every molecule partition mask is exactly a cell partition mask whose blocks are unions of primitive molecules. Consequently sigma is in the convex hull of cell partition masks; also 0<=sigma_bc<=1.

Now choose a cell endpoint pair for each molecule-tree edge and introduce the radii (4.2), using the present delta and J. The chosen endpoint graph on M need not be connected and need not span all cells. It does satisfy the only degree property needed below: the number of chosen incident pairs at cell b is d_b. Let M_0 be the masked baseline including these complex increments. Then

\[
 \operatorname{Herm}M_0\ge\lambda I/2,\qquad
 \|M_0\|\le2\Lambda_0,\qquad
 \|M_0\|_{\operatorname{Schur},m}\le K+\delta.
 \tag{10.3}
\]

The first two bounds use partition-mask accretivity and an ordinary perturbation norm at most delta. For the third, the original masked baseline has weighted row/column norm at most K. A selected edge contributes

\[
 e^{m d(b,c)}|z_{bc}|\|(C_0)_{bc}\|
 \le\frac{\delta}{\max(d_b,d_c)}
             e^{-\kappa d(b,c)}
 \le\frac{\delta}{\max(d_b,d_c)}.
\]

Summing incident edges costs at most delta. This argument never used a spanning-tree property on the cell set.

Weighted conjugation at rate s in (9.3) gives the ordinary inverse Schur bound

\[
 \|M_0^{-1}\|_{\rm Schur}\le L.
 \tag{10.4}
\]

Indeed the conjugation changes M_0 in operator norm by at most
2s(K+delta)/(em)<=a/2, whereas its Hermitian part is at least a. The inverse entries are bounded by (2/a)e^(-s d), and summing gives L.

Apply the same mask and increments to Delta C=C(A)-C_0. Its support-algebra matrix E satisfies

\[
 \|E\|_{\operatorname{Schur}(\mathcal B_M)}
 \le v+\delta v/K=v_1.                              \tag{10.5}
\]

The mask part costs at most v. The selected edge part follows from (10.2):
|z_bc|v e^(-2md)<= (delta v/K)e^(-md)/max(d_b,d_c).
Again only cell-degree row sums are used.

Thus the complete determinant/inverse expansion from the local-precision proof applies without alteration:

\[
 p_{M_0+E}(x)=p_{M_0}(x)
 \exp\!\left[-\frac12\operatorname{Tr}\log(I+M_0^{-1}E)
 -\frac12x^T((M_0+E)^{-1}-M_0^{-1})x\right].
 \tag{10.6}
\]

By (9.4), its norm in B_M is bounded by

\[
 \|p_{M_0+E}(x)\|_{\mathcal B_M}
 \le \widehat K_G^{|M|}\,p_{2V_*I}(x_M).
 \tag{10.7}
\]

For clarity, the inverse-difference Schur norm is at most w; the trace-log norm is at most D|M|[-log(1-u)]. The latter costs at most 2^(D|M|/2), and the former uses at most half of the baseline Gaussian decay. These give exactly the prefactor in (10.7).

An interaction factor on Y inside M is an algebra element supported on Y. Its support length ell_M(Y) is zero, and its norm is at most v_Y. Therefore a molecule a_S, S subset M, has algebra norm at most M_S. For a bad singleton, its background support is empty and its real-field absolute majorant is the bad indicator. Multiplication and integration of (10.7) now give, on the entire endpoint polydisc,

\[
 \left\|\mathbb E_{M_0+E}\prod_a f_{S_a}\right\|_{\mathcal B_M}
 \le\prod_a\left(\widehat K_G^{|S_a|}M_{S_a}
                   +\widehat\tau\mathbf1_{\{|S_a|=1\}}\right).
 \tag{10.8}
\]

This checks the only density input used in the overlapping-support tree proof.

## 11. Formal factorization, logarithm and conversion to connected support

All covariance entries in (10.6) are their explicit Neumann series in the precision labels B_Y. Retain independent formal scalar tags on those labels until convergence is established; interaction labels can be retained likewise. At a molecule forest mask the complete Gaussian marginal matrix is block diagonal over its components. Its normalized density is therefore the product of the normalized block densities as a formal power-series identity, including both inverse and determinant factors. This remains true if the components' background supports overlap. Grouping formal coefficients by the union of their background labels respects multiplication.

The density expansion for a component uses its actual marginal and its own root set. Its injection into the algebra with all moment roots is contractive. Thus the forest factorization is exact in the support representation, not merely after evaluating A.

Banach-valued Cauchy applied to (10.8) now gives (4.5) in the root algebra. The overlap-animal bound and endpoint-tree recursion use nonnegative scalar majorants and therefore give

\[
 \sup_i\sum_{M\ni i,X}
  e^{\kappa\ell(M)+\kappa\ell_M(X)+2|M|}
                 \|\zeta(M;X)\|_\infty\le\widehat\eta .
 \tag{11.1}
\]

The gas remains hard core in the marked supports M, not in the enlarged background supports X. For a connected logarithmic cluster, root inclusion and subadditivity give

\[
 \ell(\cup M_a)\le\sum_a\ell(M_a),\qquad
 \ell_{\cup M_a}(\cup X_a)\le\sum_a\ell_{M_a}(X_a).
\]

The same pinned Mayer estimate therefore yields a canonical expansion

\[
 \log Z_V=\sum_{M\ne\varnothing,X}U(M;X)(A|_X),
\]
\[
 \sup_i\sum_{M\ni i,X}
  e^{\kappa[\ell(M)+\ell_M(X)]+|M|}
                     \|U(M;X)\|_\infty\le2\widehat\eta .
 \tag{11.2}
\]

Choose deterministic minimizing trees/forests and shortest lattice paths to form a connected hull H(M,X) containing M union X. With L_*=ell(M)+ell_M(X),

\[
 |H|\le |M|+L_*,\qquad d(a,b)\le L_*
             \quad(a\in M,\ b\in H).
\]

For a_*=min(1/2,kappa/4),

\[
 e^{a_*|H|}
 \le e^{|M|+\kappa L_*}e^{-(\kappa/2)d(a,b)}.
 \tag{11.3}
\]

Group U by this fixed hull. To root its sum at b in H, overcount by all a in M and use (11.2). The lattice convolution costs only S_{kappa/2}, proving (9.6). The interpolation w_Y -> t w_Y is analytic in this same support representation, so its Banach-valued Cauchy estimate followed by the bounded hull map proves (9.7).

The labels can be chosen translation equivariantly when the underlying data allow it, but a deterministic shortest-path choice need not preserve all discrete rotations. Nor do arbitrary local precision and interaction decompositions make each resulting activity gauge invariant. These additional symmetry requirements need an admissible equivariant construction or averaging argument in any application. None affects the locality, holomorphy and norm theorem proved here.

## 12. Updated status

The abstract overlap gap and its strict-background-support extension are both closed under their displayed hypotheses. The former needs only the uniform complex covariance spectrum/decay and the weighted bounded interaction multipliers. The latter additionally needs the fixed background-independent baseline, product domain and sufficiently small local precision decomposition (9.1)--(9.4), plus truly local background dependence of each interaction.

No moving gauge chart, history-uniform precision decomposition, or regulator-uniform choice of independent fixed-dimensional fluctuation cells has been deduced from these assumptions. In particular, allowing a baseline chosen separately for each arbitrary background would prove locality only in the perturbation away from that reference, not locality in the reference itself.

## 13. Tunable density cost around a real baseline

The prefactors K_G and widehat K_G above can cost exp(cD) per interaction cell. If an application chooses cells with a large, albeit fixed, dimension D, that cost need not fit its available support-decay exponent. A real baseline permits a tunable cost exp(O(theta D)). This section and the next give an independent refinement; no covariance diagonalization or independence of the dominating cells is required.

### Relative-density lemma

Let C_r be a real symmetric positive covariance in N real dimensions, and write

\[
 M=C_r^{1/2}(I+F)C_r^{1/2},\qquad F^T=F,\qquad \|F\|\le\theta<1.
\]

Then

\[
 |p_M(x)|
 \le\left(\frac{1+\theta}{1-\theta}\right)^{N/2}
                                      p_{(1+\theta)C_r}(x).
 \tag{13.1}
\]

**Proof.** The determinant factor is at most
(det C_r)^(-1/2)(1-theta)^(-N/2). Moreover

\[
 (1+\theta)\operatorname{Herm}(I+F)-(I+F)^*(I+F)
 =\theta I-(1-\theta)\operatorname{Herm}F-F^*F\ge0.
\]

Indeed Herm F<=theta I and F*F<=theta^2 I. Congruence by (I+F)^(-1) proves

\[
 \operatorname{Herm}(I+F)^{-1}\ge(1+\theta)^{-1}I.
\]

The resulting Gaussian exponential bound, followed by its exact real normalization, proves (13.1). ∎

### Correlated joint-tail lemma

If a centered real Gaussian G on D-dimensional cells has covariance at most L I, then for every finite cell set B,

\[
 \mathbb P\bigl(\|G_i\|_2>R\text{ for every }i\in B\bigr)
 \le \left(2^{D/2}e^{-R^2/(4L)}\right)^{|B|}.
 \tag{13.2}
\]

On this event, sum_{i in B}||G_i||^2>|B|R^2. Exponential Markov with parameter 1/(4L) and the Gaussian quadratic-exponential formula give

\[
 e^{-|B|R^2/(4L)}
       \det\left(I-\frac{C_B}{2L}\right)^{-1/2}
 \le e^{-|B|R^2/(4L)}2^{D|B|/2}.
\]

This proves (13.2) without independence. Expanding the choices of bad singleton factors therefore proves, for any nonnegative numbers a_i,

\[
 \mathbb E\prod_{i\in I}(a_i+\mathbf1_{\mathrm{bad},i})
 \le\prod_{i\in I}(a_i+p_R),\qquad
 p_R=2^{D/2}e^{-R^2/(4L)}.
 \tag{13.3}
\]

More generally, for any fixed 0<sigma<=1, Markov with parameter sigma/[2(1+sigma)L] proves the same formulas with

\[
 p_{\sigma,R}(L)=(1+\sigma)^{D/2}
       e^{-\sigma R^2/[2(1+\sigma)L]}.
 \tag{13.3a}
\]

The displayed constants below take sigma=1, but any common choice of sigma can replace their tail factors. Taking sigma of order 1/D also removes the exp(cD) bad-cell prefactor, at the cost of a tail exponent of order R^2/D.

### A small complex covariance family

Let a fixed background-independent real baseline C_r satisfy
lambda I<=C_r<=Lambda_0 I, and let a holomorphic symmetric family satisfy

\[
 \sup_A\|C(A)-C_r\|\le\theta\lambda/2,\qquad
                         0<\theta\le1/4.             \tag{13.4}
\]

Assume the actual covariance blocks C_ij(A) have the majorant J and weighted sum A_kappa in Section 2. In the overlapping-support theorem replace the constants by

\[
 \delta_\theta=\theta\lambda/2,\qquad
 K_\theta=\left(\frac{1+\theta}{1-\theta}\right)^{D/2}
          =e^{D\operatorname{artanh}\theta},
\]
\[
 p_{\theta,R}=2^{D/2}
        e^{-R^2/[4(1+\theta)\Lambda_0]},\qquad
 \tau_\theta=K_\theta p_{\theta,R},\qquad
 c_\theta=e^2/\delta_\theta,
\]
\[
 \epsilon_\theta=\sup_i\sum_{Y\ni i}
       v_YK_\theta^{|Y|}e^{4|Y|+\kappa\ell(Y)},\qquad
 \eta_\theta=e^3\tau_\theta+\epsilon_\theta,\qquad
 \eta_{\theta,*}=[4\max(1,c_\theta A_\kappa)]^{-1}.
 \tag{13.5}
\]

**Tunable mark theorem.** The conclusions (2.5) and (2.7) hold with these constants and their corresponding smallness/quarter budgets.

**Proof of the changed input.** A partition mask is a direct-sum pinching. It contracts the operator norm of C(A)-C_r; its convex combinations do likewise. Thus at a molecule BKAR mask the actual covariance differs from the real masked baseline by at most theta lambda/2. The cell endpoint polydisc, using delta_theta and the actual majorant J, adds a perturbation of norm at most theta lambda/2. The total perturbation relative to the real masked baseline has norm at most theta. Equation (13.1) applies. The dominating real covariance is at most (1+theta)Lambda_0 I, so (13.2)--(13.3), after expanding the singleton bad choices, give exactly the product bound (4.4), with

\[
 b_\theta(S)=K_\theta^{|S|}M_S+
                           \tau_\theta\mathbf1_{\{|S|=1\}}.
\]

Nothing else in the endpoint-tree, overlap-animal or logarithm proof changes. In particular no independence of the dominating Gaussian was needed. For a covariance identically equal to the real baseline, the full budget delta_theta=theta lambda is allowed, since there is no background deviation. ∎

The operator-closeness assumption is sufficient for the marked theorem because pinching is contractive. It does not imply strict background locality. That requires the next additional local precision package.

## 14. Tunable strict-support theorem

Assume Sections 9--11 with C_0 real symmetric positive, rather than merely complex accretive. Keep its K, nu, v and product-domain/locality hypotheses, but fix 0<theta<=1/4 and replace the precision constants and smallness conditions by

\[
 \delta=\theta\lambda,\qquad
 \bar K=K+\delta,\qquad a=\lambda/2,\qquad
 s=\min\{m/2,\;aem/(4\bar K)\},\qquad
 L=\frac4\lambda\sum_z e^{-s|z|},
\]
\[
 v_1=v(1+\delta/K),\qquad u=Lv_1,\qquad
 w=\frac{L^2v_1}{1-u},\qquad
 u\le\theta,\qquad
 w\le\frac{\theta}{(1+\theta)\Lambda_0}.
 \tag{14.1}
\]

As before K nu<1. One may retain v_1<=lambda/4 explicitly; it already follows from u<=theta and L>=4/lambda. The constants are fixed before the cutoff radius and interaction smallness are chosen.

Define

\[
 \rho_\theta=\frac{1+\theta}{1-\theta},\qquad
 \mathcal K_\theta=
       \left(\frac{1+\theta}{(1-\theta)^3}\right)^{D/2},
\qquad
 \mathcal p_{\theta,R}=2^{D/2}
                 e^{-R^2/(4\rho_\theta\Lambda_0)}.
 \tag{14.2}
\]

Use Section 9's J=K e^(-md), A_kappa, c_G=e^2/delta, and replace its widehat K_G, widehat p_R by mathcal K_theta, mathcal p_theta,R in (9.5). Then the strict-support conclusions (9.6)--(9.7) remain valid with these new constants.

**Proof of the changed density bound.** Let C_{r,M} be the real masked baseline at a molecule forest point. It is between lambda I and Lambda_0 I. Let M_0 add only the selected complex endpoint perturbations of the baseline covariance. The operator norm of that perturbation is at most theta lambda, so (13.1) gives

\[
 |p_{M_0}(x)|
 \le K_\theta^{|M|}p_{(1+\theta)C_{r,M}}(x).
 \tag{14.3}
\]

The previous support-algebra bounds (10.2)--(10.6) are unchanged with the present delta,L,v_1. In particular the source-dependent determinant costs at most (1-u)^(-D|M|/2), and the inverse difference costs at most exp(w||x||^2/2). Since C_{r,M}<=Lambda_0 I,

\[
 \|x\|^2\le\Lambda_0 x^T C_{r,M}^{-1}x.
\]

The second condition in (14.1) consequently gives

\[
 p_{(1+\theta)C_{r,M}}(x)\,
          e^{w\|x\|^2/2}
 \le\left(\frac{\rho_\theta}{1+\theta}\right)^{D|M|/2}
                                  p_{\rho_\theta C_{r,M}}(x).
\]

Combining this with u<=theta and (14.3) proves the support-valued density bound

\[
 \|p_{M_0+E}(x)\|_{\mathcal B_M}
 \le\mathcal K_\theta^{|M|}
                              p_{\rho_\theta C_{r,M}}(x).
 \tag{14.4}
\]

The dominating Gaussian is real and correlated, with covariance at most rho_theta Lambda_0. Expand bad singleton choices and apply (13.2). This yields (10.8) with the new constants, and all endpoint, formal factorization, Mayer and hull arguments in Sections 10--11 apply verbatim. The interaction difference uses the same bounded-multiplier interpolation. ∎

### Dimension dependence and its limit

For theta<=1/4,

\[
 \log K_\theta\le\frac{16}{15}D\theta,\qquad
 \log\mathcal K_\theta
  =\frac D2[\log(1+\theta)-3\log(1-\theta)]
  \le\frac52D\theta.
\]

Choosing theta=1/(4D) bounds the unmarked per-cell density costs by e^(4/15) and e^(5/8), respectively, independent of D. The covariance-edge constant worsens like theta^(-1), and the allowed local precision perturbation must satisfy the strengthened conditions (14.1). If the other baseline constants stay fixed, these are a polynomial loss in D in the edge budget and a smaller precision neighborhood, rather than an exp(cD) support cost.

The bad-cell tail still carries 2^(D/2); the cutoff radius must be large enough to dominate it. No claim is made that a source covariance family admits the required O(theta) neighborhood in its actual coordinates or that its scale-dependent dimension/cutoff satisfy this joint-tail budget. The result removes a specific artificial interaction support cost; it does not replace those source estimates.
