# Audit of the same-limit reflection-positivity assembly

16 October 2026. The exact normalized Wilson slab gluing and the iterated diagonal/coordinate cell-fold inequality are now written in `diagonal_fold_research.md` and have been checked internally, including a final adversarial read for this audit. This note also uses the geometry in `two_frame_geometry_research.md`, the unnormalized numerator estimate in `transfer_schatten_research.tex`, and the paired local reduction in `gauge_layer_research.md`. The fold is no longer an outstanding conditional premise within this research derivation. These internal checks are not external mathematical certification. The conclusion is at **each fixed finite lattice coupling beta**, with volume taken to infinity before removal of the tilt. There is no uniqueness or uniform ultraviolet estimate here.

## 1. First comparison: a necessary normalization correction

Write Z_C(F), Z_D(F) for unnormalized Wilson integrals on the coordinate and adapted tori, respectively. The literal formula

\[
 Z_C(e^{tO})^{N_n}\le Z_D(e^{tV_n})
\]

is not the required unnormalized fold formula. At t=0 it already has incompatible powers of the partition functions. Applying a single-cell inequality and normalizing afterward also introduces an extensive pressure defect with the wrong coefficient.

Instead put a reflected copy of the real local observable O in **every** fine diagonal cell of C_n and D_n. Call the sums V_C and V_D. Integer-offset diagonal wall reflections are affine signed permutations preserving the coordinate Wilson measure, even though diagonal RP for that measure is not being assumed. Therefore

\[
 \mu_C(V_C)=N_n\mu_C(O),\qquad
 N_n=2n^4/h^4.
\]

The source arrays are periodic: both period lattices lie in the translation subgroup of the h-wall group. The full cell-fold inequality gives

\[
 Z_C(e^{tV_C})\le Z_D(e^{tV_D}),
 \tag{1}
\]

because the complete fold of every cell's reflected content is the same array V_D. This also avoids a genuine odd-h issue: translating by h/2 times a diagonal vector is not a lattice translation when h is odd. Purely reflected copies require no such translation. The fold auditor independently confirmed this interpretation.

Set b_n(t)=log Z_D(e^{tV_D}) and let mu_D,t be the tilted probability measure. Jensen, (1), and convexity give, for t>0,

\[
\begin{aligned}
 tN_n\mu_C(O)
 &\le \log Z_C(e^{tV_C})-\log Z_C(1)\\
 &\le b_n(t)-b_n(0)+\log Z_D(1)-\log Z_C(1)\\
 &\le tN_n\mu_{D,t}(O)+\log Z_D(1)-\log Z_C(1).
\end{aligned}
 \tag{2}
\]

The derivative identity b_n'(t)=N_n mu_D,t(O) uses invariance of the tilted D law under its fine wall group. Thus, writing delta_n=n^(-4)(log Z_D(1)-log Z_C(1)),

\[
 \mu_C(O)\le\mu_{D,t}(O)+\frac{h^4\delta_n}{2t}.
 \tag{3}
\]

Fixed-beta pressure equality gives delta_n -> 0. No division by a volume-dependent source density has been omitted: the fine cell volume is h^4/2.

## 2. Amplification: counts and the factor 2 in the source cost

Fix one clean coordinate link plane and one bounded local insertion operator X. Let G_X denote its continuous gauge-invariant crossing insertion. Its finite support, including all links needed by the insertion, is placed using the geometry note. Fix h,w,H before the volume limit; these scales may depend on the support of X and on the source O, but do not depend on n or t. The counts are

\[
 N_n=\frac{2n^4}{h^4},\qquad
 N'_n=\frac{2n^4}{H^4},\qquad
 N''_n=\frac{n^4}{w^4}.
 \tag{4}
\]

The coarse diagonal fold creates N'_n insertions. Its walls are fine-grid walls and preserve V_D, so the tilted diagonal RP/fold inequality gives

\[
 |\mu_{D,t}(G_X)|^{N'_n}
 \le \frac{Z_D(e^{tV_D}\prod_{g}G_X^{[g]})}
 {Z_D(e^{tV_D})}.
 \tag{5}
\]

The second fold has N''_n coordinate cells. Exactly N'_n of them contain a coarse insertion. Each occupied cell's complete coordinate fold has N''_n insertion copies; an empty cell has none. If m_c is the number of source copies wholly assigned to cell c, then

\[
 \sum_c m_c=N_n,
 \qquad\text{the complete fold of c has }N''_n m_c\text{ source copies}.
 \tag{6}
\]

Apply the **unnormalized** Schatten numerator estimate to that complete fold. It gives source cost exp(t N''_n m_c ||O||_infinity). For occupied cells its operator factor is ||X||^(N''_n). The latter follows by placing the disjoint operators at each cut and multiplying their norms; physical gauge projection is a contraction, and reflected/rotated operators have the same norm. The number of cuts J is even, and all positive gap lengths are integers in the fixed finite set {1,...,2w-1}. No pointwise positivity of C^(1/2) is used.

The coordinate fold takes exponent 1/N''_n for every cell. Therefore its total source and operator factors are exactly

\[
 e^{tN_n\|O\|_\infty}\|X\|^{N'_n}.
 \tag{7}
\]

Only now use the original denominator

\[
 Z_D(e^{tV_D})\ge e^{-tN_n\|O\|_\infty}Z_D(1).
 \tag{8}
\]

Combining (5)–(8), the pressure cancellation below, and the N'_n-th root gives

\[
 \limsup_{n\to\infty}|\mu_{D,t}(G_X)|
 \le e^{2t(N_n/N'_n)\|O\|_\infty}\|X\|
 =e^{2t(H/h)^4\|O\|_\infty}\|X\|.
 \tag{9}
\]

Thus the proposed factor and power are correct. Do not apply the already normalized formula (3) of the transfer note to each cell factor and then bound its tilted partition function a second time: that needlessly spends the denominator bound again and produces a larger constant (up to 4t). That larger constant would still disappear when t -> 0, but it is not the derivation of (9).

## 3. The pressure estimate is uniform over the required family

For a folded factor with coordinate time length N and spatial cross-section Gamma, the source-free transfer comparison is

\[
 \frac1J\sum_{j=1}^J\log Z_\Gamma(J\ell_j),
 \qquad \sum_j\ell_j=N.
\]

Every such torus has diverging side lengths with aspect ratios bounded by constants fixed by w and H. The gap lengths belong to a fixed finite set; the possible time directions are four. After the source factors are bounded away, offsets and source-cell patterns do not enter these unperturbed partition functions. A common pressure error epsilon_n -> 0 therefore gives

\[
 \left|\frac1J\sum_j\log Z_\Gamma(J\ell_j)
       -p_\beta|\Gamma|N\right|
 \le\epsilon_n|\Gamma|N.
 \tag{10}
\]

The cancellation is exact at leading order because J^(-1) sum_j J ell_j=N. All complete coordinate folds have total volume n^4. Averaging their logarithms with 1/N''_n leaves an error at most epsilon_n n^4, not N''_n times that error. The N'_n-th root turns it into epsilon_n H^4/2 -> 0. No finite-size rate is needed; a qualitative common pressure on the finite shape family suffices. Fixing h,w,H before this limit is essential.

## 4. One comparison law can satisfy all the required symmetries

Fix an original coordinate-torus subsequence converging locally weakly to nu. For each fixed t_j>0, t_j -> 0, extract a weak limit lambda_j of the tilted adapted-torus measures along a subsequence of that same original volume sequence. Compactness holds on SU(2)^E, a compact metrizable product over countably many lattice edges. Local observables are embedded in the tori once their finite neighborhoods fit.

Equation (3) gives nu(O) <= lambda_j(O). Every lambda_j retains invariance and RP at the chosen diagonal walls. Extract a weak limit lambda of lambda_j. Then nu(O) <= lambda(O), and the fixed target diagonal wall's positivity/invariance survive. The original coordinate limit is unchanged by these extractions.

For each fixed X, (9) passes first to lambda_j and then to lambda, yielding |lambda(G_X)| <= ||X||. The constant H can depend on the support of X; it need not be uniform over all X. All these inequalities hold for the **same** lambda because they hold along every cluster subsequence for each fixed test. Equivalently one can perform a countable dense diagonal extraction. There is no requirement to select a different state for each operator.

The unital functional L(X)=lambda(G_X) is Hermitian: apply its norm bound to I+i s A for self-adjoint finite-representation A, then let the real parameter s tend to zero from both signs. The identity insertion has G_I=1. The kernel adjoint relation and probability-measure conjugation then give reflection invariance on two-layer crossing insertions. Finite-representation kernel approximation extends this to every continuous gauge-invariant two-layer observable. Operator norms of the approximants may diverge: the required order is first t -> 0 for each fixed approximant, then the approximation index -> infinity.

The paired local reduction in `gauge_layer_research.md`, (8.2), has errors epsilon+C_epsilon t for both P and its reflected partner with the reflected same Y_epsilon. It therefore extends two-layer invariance to all local observables at the same clean plane. There are two fixed adjacent clean link planes in each coordinate direction. Applying this argument at all eight planes gives invariance under their pairwise compositions, namely translations by 2e_mu. Thus lambda is 2Z^4 invariant.

This uses fixed-beta constants only. If simultaneous n,t sequences are desired, choose n_j large enough that pressure errors divided by t_j vanish and finitely many convergence tests hold. Such a diagonal choice exists without a quantitative rate, but the ordered-limit formulation is cleaner. An arbitrary simultaneous sequence is not justified.

## 5. Convex separation: the observable-dependent comparison law is sufficient

Fix one lattice-preserving target diagonal mirror theta. Let R be the set of gauge-invariant probability laws invariant and reflection positive at theta. It is weakly compact and convex: the configuration space is compact; invariance is a family of closed linear equalities; and each RP inequality mu((theta F)F)>=0 is a closed affine half-space for continuous local half-observables, with the usual antilinear theta convention. One can also impose 2Z^4 invariance and the fixed-beta Wilson DLR identities; these are closed linear conditions, but neither addition is needed for the separation step.

For any real gauge-invariant local polynomial O, an even lattice translation moves its full support into an open diagonal cell having theta as one boundary wall. Choose h sufficiently large afterward, and choose the other wall offsets freely on their allowed integer/half-integer meshes. There is no parity obstruction: an even translation can move the normal height arbitrarily far, and the cell width can be arbitrarily large. The original law nu is invariant under all lattice translations. The comparison law lambda constructed for the translated observable is invariant under even translations. Hence the comparison is transported back to the original O, with lambda still belonging to the same fixed set R:

\[
 \text{for every real gauge-invariant local polynomial }O,
 \qquad \nu(O)\le\sup_{\lambda\in R}\lambda(O).
 \tag{11}
\]

The comparison law may depend on O. That is sufficient. If nu were outside R, weak separation of the compact convex set R would produce a real continuous separating function. Cylinder functions uniformly approximate it. Gauge averaging over the finite endpoint group of a cylinder leaves its expectation unchanged under all gauge-invariant laws, and finite Peter–Weyl polynomials uniformly approximate that gauge-invariant cylinder. The strict separation would then persist for a real gauge-invariant local polynomial, contradicting (11). Thus nu belongs to R.

If R is instead defined as a collection of particular comparison limits, replace it by its closed convex hull inside the preceding RP class. The RP and invariance properties survive that hull. No averaging over translated states is being used to manufacture positivity, and no uniqueness assertion enters.

## 6. Audit verdict and scope

The exact two-frame fold/slab lemma has now been supplied and internally checked. Its final adversarial read found no further flaw: odd diagonal widths keep unlike boundary spaces distinct until the integral paired translation; complex cell functions use conjugate reflection and even Schatten powers; each sequential fold restores the ordinary Wilson graph before the next classification; and the full reflected real source arrays have consistent period parity and the same complete fold. The coordinate step uses the companion mixed site/link representation, not positivity of the square-root convolution kernel.

With these checked dependencies, the same-limit assembly is consistent, with source coefficient 2(H/h)^4 and no hidden uniformity in beta. The essential requirements are: use full reflected arrays in the first Jensen comparison; apply unnormalized transfer bounds before the single original denominator; hold all auxiliary lengths fixed in each volume limit; remove the tilt before finite-rank approximation; and take separation in one fixed compact convex target-RP class. The local reduction and operator amplification together are necessary to obtain even translations of the comparison state.

The resulting research derivation establishes diagonal RP of each fixed-beta coordinate-torus infinite-volume limit for pure Wilson SU(2), subject to the usual possibility of errors not detected by these internal audits. It does not by itself construct a continuum measure, prove continuum rotations, establish uniform renormalized insertion estimates, or prove a mass gap; no external certification is claimed.
