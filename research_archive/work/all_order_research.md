# All-order growth from fixed-side chessboards

Research note, 16 October 2026. This is a conditional analytic and geometric reduction. It does not establish the required Yang–Mills source estimates, rotational covariance, a nonzero limit, or a mass gap.

## 1. What is proved

The fixed-grid difficulty in Section 6A of the companion compactness note can be removed without increasing the cell side with the number of insertions. Partition each source into patches of radius proportional to 1/n. For each selected n-tuple of patches choose one translated reflection grid, retain that grid for every subset of the tuple, and shrink the complex source radius using a radial Schwarz estimate for the face counterterms.

Under the explicit hypotheses below, for every eta>0 and n>=2 the connected functions at pairwise separated supports satisfy

\[
 |\kappa_n(f_1,\ldots,f_n)|
 \le [C_\eta(1+R)^4]^n (n!)^{6+\eta}
       [1+H_p(\delta)]\prod_i\|f_i\|_{C^1}.                 \tag{1}
\]

Here each support lies in a ball of radius R, the ball centers are arbitrary, delta is the minimum distance between supports, and

\[
 H_p(t)=\sum_{j\ge0}(1+j)^p L^{4j}e^{-ctL^j}
 \le C(1+t^{-4})[1+\log^+(1/t)]^p.                       \tag{2}
\]

The stronger exponent 6+eta uses the anchored polymer estimate with its actual shrinking-ball radius. If the input is known only for unit anchoring balls, exactly the same method gives exponent 10+eta instead.

The centered full moments then obey, for supports in arbitrary translates of unit balls and 0<delta<=1,

\[
 |S_n(f_1\otimes\cdots\otimes f_n)|
 \le C_\eta^n(n!)^{6+\eta}\delta^{-3n}
       \prod_i\|f_i\|_{C^1}.                             \tag{3}
\]

A separate elementary tensor-extension argument proves

\[
 |S_n(\Psi)|\le C_\eta^n(n!)^{18+\eta}q_{15n}(\Psi),
 \quad
 q_m(\Psi)=\max_{|\alpha|\le m}\sup_X
        (1+|X|^2)^{m/2}|\partial^\alpha\Psi(X)|,           \tag{4}
\]

on Schwartz functions flat to all orders at every partial diagonal. Consequently constants C independent of n can be chosen with

\[
 |S_n(\Psi)|\le C(n!)^{19}q_{15n}(\Psi).                  \tag{5}
\]

With unit-ball anchoring only, replace 18+eta and 19 by 22+eta and 23. These exponents are deliberately generous and are not asserted optimal.

The global constants in (4)--(5) do not hide support-radius dependence: the tensor argument uses only translates of unit balls, and sums their positions with an explicit integrable weight. Reflection positivity passes from a common centered limiting hierarchy to the usual positive-time flat test spaces by density, as proved in Section 9. Neither this fact nor (5) is full OS reconstruction.

## 2. Precise additional hypotheses

Use the source-independent normalization, denominator lower bound, complex source stability, and local counterterm decomposition of Sections 2, 4 and 5 of the companion note. The following uniformities are essential, rather than conclusions of unsourced stability.

1. Fix a physical stopping spacing h and a cell side ell that is an admissible integer multiple of h. Work on tori tiled by these cells with the parity/divisibility needed for the original Wilson chessboard estimate. In coarse units, V/M is the fixed cell volume v=(ell/h)^4. The constants C_+, C_- do not depend on cutoff, volume, n, source positions, or the chosen admissible grid translate.

2. The RG stopping grid and its source estimates may be translated together with the reflection grid. Admissible grid origins form a mesh of size at most C_lat a in each coordinate, where a is the bare spacing. All constants are uniform over these translates. Translating the stopping lattice is an extra uniformity assumption; shifting a chessboard alone does not prove it.

3. There is a fixed radius r_*>0 such that, for disjoint normalized profiles and their reflected copies, all required source weights with max_i |z_i| nu_i<r_* are admissible, where nu_i is the C^1 norm of the profile. The local counterterms are holomorphic functionals of the complex weight, independent of its presentation as a sum of real profiles. In particular, multiplying a fixed complex reflected weight by an arbitrary complex scalar is an allowed holomorphic family whenever its norm stays inside the same source ball.

4. Each local source term vanishes at zero source and depends only on the weight on its enlarged support. For every anchoring ball B_R, every t>0, and every scale ell_j=L^{-j}, assume

\[
 \sum_{\substack{X:X^+\cap B_R\ne\varnothing\\
                         {\rm diam}\,X^+\ge t}}
     \sup_{w\ {\rm admissible}} |e_{a,j}(X;w)|
 \le A(R+\ell_j)^4\ell_j^{-4}(1+j)^p e^{-ct/\ell_j}.      \tag{6}
\]

The constants A,c,L,p are fixed, with p>=0 without loss of generality. For the improved exponent in (1), (6) is uniform also as R decreases; the conservative version needs only R bounded by one. The anchored estimate applies to the relevant original and replicated weights. The support convention must ensure that a polymer which reaches a cell face from a source buffered by b has enlarged diameter at least a fixed multiple of b, and that a polymer meeting two supports separated by delta has enlarged diameter at least a fixed multiple of delta. Fixed enlargement factors can be incorporated in c.

5. The many-cell chessboard estimate applies to the local complex exponentials on the original measure. The recentered bulk average is defined, on a fixed grid, as a functional of the complete source weight, with zero summands in empty cells. It is not redefined when coefficients are set to zero.

The usual disjoint-support sup/Lipschitz norm argument supplies hypothesis 3 from a presentation-independent source theorem on arbitrary real profiles: group the real and imaginary parts, and group the even and odd reflected copies. This costs only a fixed factor in radius. It cannot be inferred from a theorem whose counterterms depend on the chosen source presentation.

All estimates below are required only eventually in the cutoff for each fixed n and fixed finite test family. A common bound for every n at one fixed a is unnecessary for subsequential continuum extraction.

## 3. Radial Schwarz estimate for face energies

If F is holomorphic on a complex norm ball of radius r_*, F(0)=0, and |F|<=B there, then

\[
 |F(w)|\le B\|w\|/r_* .                                 \tag{7}
\]

Indeed, apply the one-variable Schwarz lemma to lambda -> F(lambda r_* w/||w||)/B on the unit disc, first with a slightly smaller radius and then by a limit.

The same estimate can be applied term by term in an absolutely summable local counterterm series. For a source family with tau=max_i |z_i| nu_i, the bound in (6) therefore acquires a factor tau/r_*. The actual chessboard weight depends on z and conjugate z, but this causes no problem in (7): freeze that weight and vary lambda times the entire complex weight. This is why hypothesis 3 explicitly requires holomorphy beyond the subfamily of physical conjugate-reflection weights.

For patches of radius R_n and face buffer b_n with R_n<=C_0 b_n<=1, the full face sum per source is bounded by

\[
 J_n
 =C\sum_{j\ge0}(1+j)^p(1+R_n/\ell_j)^4 e^{-c b_n/\ell_j}
 \le C[1+\log^+(1/b_n)]^{p+1}.                           \tag{8}
\]

To prove the last inequality, split at the last j with ell_j>=b_n. In this range the ratio R_n/ell_j is bounded, so the sum is O((1+log(1/b_n))^{p+1}). Write j=J+k in the remaining range. The summand is bounded by

\[
 C(1+J)^p(1+k)^p L^{4k}e^{-c' L^k},
\]

whose sum over k is finite uniformly in J. If only a unit anchoring ball is available, the weaker bound J_n<=C H_p(b_n) follows instead.

Thus the actual face term, and the normalized reflected face terms summed over occupied cells, each cost at most

\[
  (\tau/r_*)\,|B| J_n                                  \tag{9}
\]

for every subset B of a selected patch tuple.

## 4. One shifted grid per selected tuple

Take a smooth nonnegative partition of unity (chi_s^epsilon) on R^4, each member supported in

\[
 \epsilon s+[-\epsilon,\epsilon]^4,
\]

with uniformly bounded overlap and |partial chi_s^epsilon|<=C/epsilon. Let

\[
 \epsilon_n=\min\{1,\ell\}/(64n).
\]

Select one patch f_{i,s_i}=chi_{s_i}^{epsilon_n} f_i for each i=1,...,n. Its projection in each coordinate is an interval of length at most 2 epsilon_n.

For one coordinate, a grid phase modulo ell is forbidden if a grid face comes within 2 epsilon_n of one of these intervals. The union of the forbidden phase intervals has length at most 6n epsilon_n<ell. Choose a phase outside it. Rounding to an admissible grid origin changes the phase by at most C_lat a. For a<=epsilon_n/C_lat, with a harmless further fixed factor if necessary, every selected patch still has face buffer at least epsilon_n. Make the four coordinate choices independently.

Each selected patch is therefore inside one cell of the same fixed-side grid. Several patches may share a cell, but the number q of occupied cells is at most n. The patch radius is at most 2 epsilon_n in the Euclidean norm, while the buffer is at least epsilon_n, so (8) applies.

Fix this grid and all subtraction data for the entire chosen n-tuple and every one of its subsets. Restriction consistency is needed only within this finite family. Different selected tuples in the multilinear expansion are allowed to use different grids, since their bounds are summed after they have been proved separately.

If f is supported in a ball of radius R, elementary counting and the product rule give

\[
 \sum_s\|\chi_s^{\epsilon_n}f\|_{C^1}
 \le C(1+R)^4\epsilon_n^{-5}\|f\|_{C^1}
 \le C_\ell(1+R)^4 n^5\|f\|_{C^1}.                     \tag{10}
\]

The constants are independent of the ball center. Only first derivatives of this partition are used. Multiplication by a partition member does not reduce the separation between distinct original supports.

## 5. Coherent holomorphic functions and cumulants

For one selected n-tuple use its fixed grid to define E_B^# and

\[
 h_B(z_B)=e^{-E_B^\#(z_B)}Z(w_B)/Z(0)
\]

for every subset B. Empty-cell terms vanish, so

\[
 h_I(z_B,0)=h_B(z_B),\qquad h_B(0)=1.                    \tag{11}
\]

Choose

\[
 D_n=1+2J_n,\qquad r_n=r_*/D_n,\qquad
 Q=\exp[(C_++C_-)v+1].                                 \tag{12}
\]

The many-cell chessboard root costs q(C_++C_-)v. The transported bulk averages cancel its bulk counterterms in the real part of E_B^#. By (9), the combined remaining face cost at max_i|z_i|nu_i<r_n is at most |B|. Since q<=|B|,

\[
 |h_B(z_B)|\le Q^{|B|}
\]

on that product polydisc, with Q independent of n.

For completeness, the needed formal-logarithm bound is

\[
 |\partial_I\log h_I(0)|
 \le n!(2Q/r_n)^n\prod_{i\in I}\nu_i.                   \tag{13}
\]

Product Cauchy gives |partial_B h_B(0)|<=(Q/r_n)^{|B|} product_{i in B}nu_i. In the moment-cumulant identity, the sum of absolute coefficients is

\[
 \sum_{k=1}^n(k-1)!S(n,k)
 \le n!\sum_{k=1}^n {n-1\choose k-1}/k
 \le n!2^n.
\]

The middle inequality counts ordered set partitions by positive block sizes. This proves (13). A logarithm is used only locally near h_I(0)=1; a zero-free product polydisc is not assumed.

The full mixed derivative of E_I^# costs at most

\[
 C H_p(\delta)r_*^{-n}\prod_i\nu_i.                     \tag{14}
\]

For a face term, locality annihilates the derivative unless the enlarged polymer meets all n supports, so it has diameter at least delta; anchor at the first patch and use (6) and product Cauchy at the base radius r_*. For bulk averages, if at least two cells are occupied, each average depends on a proper subset of source variables and contributes zero. If exactly one cell is occupied, apply the same anchored argument in each reflected copy and average. The normalized average introduces no volume factor. This proof is for n>=2, as needed for the centered hierarchy.

Equations (13)--(14) and multilinearity now give

\[
 |\kappa_n(f_1,\ldots,f_n)|
 \le [C(1+R)^4]^n[1+H_p(\delta)]\,
        n!\,n^{5n}[1+\log n]^{(p+1)n}
        \prod_i\|f_i\|_{C^1}.                           \tag{15}
\]

For every eta>0, [1+log n]^{p+1}<=C_eta n^eta, and n^n<=e^n n!. This proves (1). Under unit-ball anchoring, r_n^{-1}<=C n^4[1+log n]^p, which gives the conservative exponent 10+eta.

The restrictions a<=c/n and torus compatibility do not obstruct a common continuum subsequence: for each fixed n the restriction holds eventually, and the extraction is countable in n. Nothing here asserts simultaneous admissible grids for every n at a fixed ultraviolet cutoff.

## 6. Centering and full moments

Center the lattice observable before taking limits. Its cumulants of order >=2 are unchanged and its first cumulant vanishes. The centered moment formula uses only partitions with block size at least two.

Write A_delta=1+H_p(delta)>=1. If the connected bound is

\[
 |\kappa_k|\le C^k(k!)^s A_\delta\prod\nu_i,\quad s>=1,
\]

then each partition of n has at most n/2 nonzero blocks, giving a factor at most A_delta^{n/2}. There is no extra n! loss from summing partitions. Indeed,

\[
 \sum_{\pi}\prod_{B\in\pi}(|B|!)^s
 \le(n!)^{s-1}\sum_{\pi}\prod_{B\in\pi}|B|!
 \le 2^{n-1}(n!)^s.                                    \tag{16}
\]

For the second inequality, ordered partitions with k block sizes n_1,...,n_k contribute n!/k! for each positive composition, hence at most n! times the number 2^{n-1} of compositions. Dropping the restriction excluding singletons only enlarges the bound.

For 0<delta<=1, (2) implies A_delta<=C_p delta^{-6}; the two extra powers absorb the fixed logarithmic power. Thus A_delta^{n/2}<=C^n delta^{-3n}, proving (3). For delta>=1 one instead has a uniform constant. We use the resulting local product estimate only for supports in balls of radius at most one, with constants uniform over all translations.

## 7. Quantitative extension to joint flat tests

This section is independent of the source construction. Suppose an off-diagonal distribution S_n is already obtained from a common subsequential hierarchy and satisfies

\[
 |S_n(f_1\otimes\cdots\otimes f_n)|
 \le C^n(n!)^s \min(1,\delta)^{-3n}
                      \prod_i\|f_i\|_{C^1},             \tag{17}
\]

whenever the supports lie in arbitrary translates of unit balls and are pairwise separated by delta. Initially real tests suffice; complexification changes C only by a fixed factor.

Let Delta_n be the union of all pair diagonals, and let S_flat consist of Schwartz functions whose complete jets vanish on Delta_n. We prove

\[
 |S_n(\Psi)|\le C^n(n!)^{s+12}q_{15n}(\Psi),
 \qquad \Psi\in S_{\rm flat}.                           \tag{18}
\]

### 7.1 A dyadic decomposition using only bounded-order cutoff derivatives

Choose a fixed smooth nondecreasing eta_0 on [0,infinity), zero on [0,2] and one on [4,infinity). Its radial extension is smooth because it is constant near zero. Put epsilon_j=2^{-j} and

\[
 F_j(X)=\prod_{a<b}\eta_0(|x_a-x_b|/\epsilon_j),
 \quad \chi_0=F_0,\quad\chi_j=F_j-F_{j-1}\ (j>=1).
\]

The chi_j are nonnegative and sum to one off Delta_n. If j>=1 and X belongs to the support of chi_j, then every pair has distance at least 2 epsilon_j, and some pair has distance at most 8 epsilon_j. The same statements hold on the supports of derivatives of chi_j. The j=0 term has all pair distances at least two.

At each j localize every variable by a fixed smooth lattice partition with mesh rho_j=epsilon_j/64. Partition supports have Euclidean radius at most 2rho_j. Choose enlarged bumps beta_i, equal to one on these supports, with radius at most 4rho_j. A product chart meeting supp chi_j has its enlarged one-variable supports pairwise separated by at least epsilon_j. The bounds (17) therefore apply to all tensor factors used below. The unit-ball restriction is automatic.

### 7.2 Fourier factorization on a product chart

Write H=chi_j Psi times the product of the chart partition members, rescale x_i=c_i+rho_j y_i, and extend by zero to a fixed periodic cube in each y_i. Fourier expansion followed by multiplication by the beta_i gives

\[
 H(X)=\sum_{m_1,\ldots,m_n} a_m
       \prod_i\bigl[\beta_i(x_i)
          e^{i\omega m_i\cdot(x_i-c_i)/\rho_j}\bigr],
\]

where the harmless frequency factor omega is fixed. Each factor has C^1 norm at most C rho_j^{-1}(1+|m_i|). Applying (1-Delta_{y_i})^3 for each i to estimate the Fourier coefficients yields

\[
 \sum_m |a_m|\prod_i(1+|m_i|)
 \le C^n\max_{\substack{|\alpha_i|\le6\\1\le i\le n}}
                       \|\partial_y^\alpha H\|_\infty, \tag{19}
\]

because the sum over m in Z^4 of (1+|m|)(1+|m|^2)^{-3} is finite. The periodic cube, its normalizations, and the finite expansion of these differential operators contribute only C^n.

There is no hidden arbitrary derivative of order 6n on a fixed bump. Each one-variable partition bump receives at most six derivatives. Each pair factor eta_0(|x_a-x_b|/epsilon_j) receives at most twelve, because it depends only on x_a,x_b. Thus fixed C^12 bounds on eta_0 and fixed C^6 bounds on the spatial bumps suffice. Sequential use of the product rule over at most n(n-1)/2 pair factors gives the safe bound

\[
 C^n n^{12n}
\]

for all the cutoff derivatives in (19). Rescaling contributes rho_j^m and each radial derivative costs epsilon_j^{-m}; their ratio is bounded. This is the step that avoids unjustified assumptions on high derivatives of an arbitrary smooth partition.

### 7.3 Flatness compensates for the collision and chart sums

For j>=1, at every point relevant to a derivative of H some pair distance is at most 8 epsilon_j. Move one member of that pair onto the other, keeping every other coordinate fixed. For every derivative partial^alpha Psi with total order at most 6n, Taylor's formula of order 9n along this segment, and complete flatness at its initial endpoint, give

\[
 |\partial^\alpha\Psi(X)|
 \le C^n\epsilon_j^{9n}
      q_{15n}(\Psi)\prod_i(1+|c_i|^2)^{-3}.              \tag{20}
\]

To see the weight explicitly, the segment changes only one coordinate by at most eight, and all chart coordinates are a bounded distance from their centers. Hence the product of (1+|c_i|^2)^3 is at most C^n times the product at a point of that segment, which is at most C^n(1+|Y|^2)^{3n}. This is dominated by the weight in q_{15n}. Directional Taylor expansion costs at most C^{9n}; its factorial denominator may be discarded. The derivative order is 6n+9n=15n.

In bounding the product-rule expansion, first restrict to supp chi_j; outside it all derivatives of H vanish. This matters because the separate terms F_j and F_{j-1} need not individually have a close pair outside that support.

Combining (17), the C^1 factor norms, (19), and (20), the contribution of one chart is at most

\[
 C^n(n!)^s n^{12n}\,
 \epsilon_j^{-3n}\rho_j^{-n}\epsilon_j^{9n}
 q_{15n}(\Psi)\prod_i(1+|c_i|^2)^{-3}.                  \tag{21}
\]

Since in four dimensions

\[
 \sum_{c\in\rho_j\mathbb Z^4}(1+|c|^2)^{-3}
 \le C\rho_j^{-4},
\]

summing the charts contributes at most C^n epsilon_j^{-4n}. The total remaining scale factor is

\[
 \epsilon_j^{9n-3n-n-4n}=\epsilon_j^n.
\]

Its dyadic sum is uniformly bounded for n>=2. The j=0 contribution uses the same argument without Taylor or a small scale factor; all pair separations and mesh sizes are fixed. Finally n^{12n}<=e^{12n}(n!)^{12}, proving (18).

### 7.4 Existence and uniqueness of the extension

First apply the preceding estimates to compactly supported smooth functions away from Delta_n, where S_n already exists. All chart and Fourier sums converge absolutely in the estimates. Their value agrees with the existing distribution by local smooth Fourier convergence.

Compactly supported smooth functions away from Delta_n are dense in S_flat with its induced Schwartz topology. To verify this, cut off at spatial infinity, then multiply by F_J. For any fixed seminorm, derivatives of 1-F_J cost a fixed power of 2^J, while Taylor flatness of arbitrarily high order supplies an arbitrarily larger negative power. The region involved contains a pair at distance O(2^{-J}); the same short-segment weight comparison as above applies. Thus the cutoff error tends to zero in every Schwartz seminorm.

Equation (18) gives a unique continuous extension to S_flat. Equivalently the absolutely convergent dyadic sum defines it there. No coincident contact-term extension to all Schwartz tests has been chosen.

## 8. The numerical linear-growth condition

Insert s=6+eta in (18) to obtain (4). For a fixed positive gamma, C^n<=(constant)(n!)^gamma; this follows at once from the factorial growth. Choosing eta=1/2 and absorbing C_eta^n with gamma=1/2 gives (5), with a prefactor independent of n. The unit-ball-only variant gives exponent 23 in the same way.

For comparison, Adamo--Moriwaki--Tanimoto, arXiv:2407.18222v2, Section 2.5, printed page 18, equations (20) and (22), use this precise type of Schwartz seminorm and state their OS0' condition with a fixed factorial power and seminorm order sn. Their Section 3.2 gives another local-to-joint extension argument. This citation identifies the numerical regularity target; their two-dimensional VOA theorem does not establish any Yang--Mills hypothesis here.

Primary source: https://arxiv.org/pdf/2407.18222, pages 17--18 and Section 3.2.

## 9. Reflection positivity on the extended hierarchy

Assume the off-diagonal functions S_n were extracted from one common sequence of centered lattice moments, with the centering compatible with the original reflection, and that the original measures are reflection positive for the selected reflection.

Take finitely many smooth positive-time joint test functions compactly supported inside the strict ordered-time chambers. Subdivide their supports into product boxes whose one-variable time intervals are disjoint and positive. Finite sums of tensor tests in these boxes approximate the joint tests in every required finite smooth norm; local Fourier expansions provide an explicit approximation.

For finite tensor sums, the OS matrix entries are limits of the corresponding centered lattice moment matrices. The latter are positive semidefinite because their observables depend only on the positive half-space and centering preserves the reflected algebra. Inside each group all insertions are separated by the ordered-time supports; between a reflected negative-time group and a positive-time group there is a strict time gap. Every entry is therefore an already controlled off-diagonal moment. A finite positive semidefinite matrix remains positive semidefinite under entrywise limits. Passing through the tensor approximations proves positivity for the compact joint tests.

Now use the standard positive-time Schwartz space whose complete jets vanish outside the strict ordered-time chamber. Compactly supported tests in the interior of that chamber are dense: spatial cutoffs and cutoffs at each chamber wall converge in every Schwartz seminorm by the same flatness/Taylor argument used in Section 7.4. For fixed m,n, tensor product and reflected conjugation are continuous in the Schwartz topology, and the resulting test belongs to S_flat on m+n variables. In particular, a collision between negative and positive time groups can occur only on a time-zero wall, where the jets vanish. Equation (18) therefore gives entrywise convergence of the OS matrices for these approximations.

This proves reflection positivity on the extended ordered positive-time flat test space. It uses both the common limiting hierarchy and the joint continuity estimate. A growth bound for an unrelated family of distributions would not imply positivity.

The same reasoning preserves permutation and translation identities already established for the common off-diagonal hierarchy. It does not produce a new diagonal reflection, full rotations, clustering, a spectral gap, or nontriviality.

## 10. Remaining verification targets

The geometry and combinatorics are no longer the bottleneck if the hypotheses in Section 2 hold. The model-specific tasks remain:

* Verify the fixed-physical-scale complex source estimate and its common source-independent normalization with the denominator bound.
* Verify uniform translated stopping-grid constructions, admissible cell tilings, and presentation-independent source holomorphy on the norm ball used by radial Schwarz.
* Verify the anchored polymer estimate uniformly for shrinking balls if the improved exponent is desired; the conservative result avoids this stronger radius uniformity.
* Check enlarged source-support conventions so face travel and distinct-support travel imply the diameter lower bounds used above.
* Establish the needed symmetries in one limiting state, including any additional tilted reflection, and prove a nonzero observable witness.

No uniqueness, comparison of two ultraviolet cutoffs, or simultaneous all-n finite-cutoff geometry is used. The result is a conditional proof of all-order flat-test regularity, not a construction of four-dimensional Yang--Mills theory.
