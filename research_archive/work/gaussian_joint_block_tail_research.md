# Joint microscopic bad-block bounds for the constrained Gaussian

17 October 2026. Proof candidate passed a separate internal audit, recorded in `gaussian_joint_block_tail_provenance_audit.md`, and a further root read. The real joint-tail theorem below follows from a counting-coordinate covariance operator bound and does not assume independent blocks. The homogeneous flat derivative field supplies that bound uniformly over refinements. A single fixed-ratio bare Wilson step also supplies it for the pair of rescaled potentials and derivatives. The complex extension is an explicitly relative quadratic-perturbation theorem, not an identification of an unproved interacting or complex-source law.

All primary statements are on finite compatible periodic regulators. Constants depend on the fixed color dimension, the fixed microscopic block geometry, and the stated covariance or perturbation constants, but not on the number of tested blocks, regulator volume, or refinement where uniformity is asserted.

## 1. The exact derivative covariance supplied by the flat construction

Work in d=4 with fine spacing eta=M^(-1), final coarse spacing one, and the source-matched homogeneous flat slice

\[
 X=\ker Q\cap\ker(RD^T),\qquad K=d^Td.
\]

The real Gaussian Z on X has density proportional to `exp[-<Z,KZ>_eta/2]`, where the physical pairing is eta^4 times the normalized trace sum. Its physical covariance operator is C, the positive variational inverse of K on X. In coordinate values,

\[
 \operatorname{Cov}_{\rm count}(Z)=\eta^{-4}\mathcal C.
                                                               \tag{1.1}
\]

Let nabla include all ordinary physical first differences of all bond/color components, and define the microscopic derivative field

\[
 Y=\eta^2\nabla Z.
\]

Its counting-coordinate covariance is exactly

\[
 \boxed{\quad
 \Sigma_Y=\operatorname{Cov}_{\rm count}(Y)
       =\nabla\mathcal C\nabla^T.
 \quad}                                                       \tag{1.2}
\]

Both the input and output fine Hilbert spaces have the same physical scalar measure eta^4. Thus the operator norm of the displayed coordinate matrix is the same in counting and physical Hilbert norms. The proved real order `0<=C<=Gamma<=G0` and the proved full-inverse first-derivative sandwich give a constant K_D such that

\[
 0\le\Sigma_Y\le K_DI                            \tag{1.3}
\]

uniformly in M and compatible periodic volume. This is stronger than a bound on each coordinate variance. It is the input that permits a joint estimate.

The color basis is real and orthonormal for the normalized trace. Flat color copies have the same covariance, so passing to all finitely many colors does not increase the scalar covariance operator bound; conversion to a matrix/color norm only changes fixed norm-equivalence constants.

By contrast, the rescaled potential alone has

\[
 \operatorname{Cov}_{\rm count}(\eta Z)=\eta^{-2}\mathcal C.
                                                               \tag{1.4}
\]

There is no refinement-uniform counting-operator bound for (1.4) at fixed final physical scale. For example, at zero coarse Bloch momentum choose fine alias r=e_1 and a transverse bond polarization e_2. The scalar block average vanishes on this mode, so Q annihilates it; its ordinary divergence is zero. It lies in X and K acts on it with eigenvalue `P=4M^2 sin^2(pi/M)<=4pi^2`. Hence C has eigenvalue at least `1/(4pi^2)` there, and the covariance in (1.4) has norm at least `M^2/(4pi^2)`. Real sine/cosine modes give the same conclusion. Pointwise variances of eta Z can still remain bounded; that is a different statement. No macroscopic joint potential tail is inferred from pointwise bounds.

## 2. A general real Gaussian block theorem

Let Y=(Y_i) be any centered real Gaussian vector, possibly singular, with counting-coordinate covariance

\[
 0\le\Sigma\le K I,
\]

where K>0. For each block b let I_b be a nonempty set of scalar tested coordinates. Assume

\[
 |I_b|\le m,\qquad
 \sup_i\#\{b:i\in I_b\}\le\nu.                  \tag{2.1}
\]

Here m and nu are fixed. Define the bad event

\[
 \mathsf B_b(R)=\{\max_{i\in I_b}|Y_i|>R\}.
\]

**Theorem 2.1.** For every finite set S of k blocks and R>0,

\[
 \boxed{\quad
 \mathbb P\!\left(\bigcap_{b\in S}\mathsf B_b(R)\right)
 \le\left[m\sqrt2\exp\!\left(-\frac{R^2}{4\nu K}\right)\right]^k.
 \quad}                                                       \tag{2.2}
\]

The right side may be replaced by its minimum with one. A second valid prefactor is `2^(m/2)` in place of `m sqrt2`; one can take the smaller of the two prefactors.

Proof. Choose one coordinate i_b from each I_b. The k-vector W=(Y_(i_b)) has covariance bounded by nu K times the identity: the coordinate-selection map, with repeated coordinates allowed, has squared operator norm at most nu. Diagonalizing its nonnegative covariance, including possible zero eigenvalues, gives

\[
 \mathbb E\exp(t|W|^2)
   =\det(I-2t\Sigma_W)^{-1/2}
   \le(1-2t\nu K)^{-k/2},\qquad 0\le t<(2\nu K)^{-1}.
                                                               \tag{2.3}
\]

On the event that all chosen coordinates exceed R in absolute value, `|W|^2>kR^2`. At `t=1/(4nu K)`, Markov's inequality gives `2^(k/2) exp[-kR^2/(4nu K)]`. There are at most m^k choices, and their union contains the event in (2.2). This proves the theorem without independence.

For the alternative prefactor, collect all coordinates of all selected blocks, retaining repetitions. The resulting vector has at most mk entries and covariance norm at most nu K. On the all-bad event its squared norm is at least kR^2. The same exponential-square calculation gives the prefactor `2^(mk/2)`.

The overlap parameter counts repetitions of the *tested Y coordinates*. It is not necessary to regard neighboring gradients as independent just because their coordinate labels differ. Their correlations are already controlled by Sigma. If the definition of a block reads an enlarged derivative stencil, use the corresponding enlarged tested sets; bounded overlap of these sets is sufficient.

For an actual local norm satisfying `N_b(Y)<=c_b max_(i in I_b)|Y_i|`, the event `N_b(Y)>R` implies a coordinate threshold `R/c_b`, so the theorem applies with that substitution. For a Euclidean block norm the alternative energy proof applies directly to `sum_(i in I_b)Y_i^2>R^2`, with prefactor `2^(m/2)` and no threshold conversion. For the fluctuation gY, replace R by R/g, or K by g^2K.

## 3. Exponential square estimates and entropy consequences

For nonnegative numbers t_b supported on a finite block set, put

\[
 E_b(Y)=\sum_{i\in I_b}Y_i^2,\qquad
 a_i=\sum_{b:i\in I_b}t_b,\qquad A=\operatorname{diag}(a_i).
\]

Then `||A||<=nu t_max` and `Tr A<=m sum_b t_b`. Whenever `2Knu t_max<1`, the exact Gaussian determinant and the inequality `-log(1-x)<=x/(1-x_max)` prove

\[
 \boxed{\quad
 \log\mathbb E\exp\!\left(\sum_b t_bE_b(Y)\right)
 \le\frac{Km\sum_b t_b}{1-2K\nu t_{\max}}.
 \quad}                                                       \tag{3.1}
\]

Indeed the nonzero eigenvalues are those of `Sigma^(1/2) A Sigma^(1/2)`, bounded by Knu t_max, and their sum is at most K Tr A. This also covers singular covariances.

For any probability rho absolutely continuous with respect to the Gaussian law mu, the elementary entropy variational inequality gives

\[
 \sum_b t_b\mathbb E_\rho E_b(Y)
 \le D(\rho\Vert\mu)
      +\frac{Km\sum_b t_b}{1-2K\nu t_{\max}}.     \tag{3.2}
\]

This is a genuine exponential-square/relative-entropy estimate, with all dimension dependence localized to m times the number of tested blocks.

Let p(R) be the bracket in (2.2), reduced to at most one if desired. Expanding a finite product with nonnegative z_b gives

\[
 \mathbb E\prod_b(1+z_b\mathbf1_{\mathsf B_b(R)})
       \le\prod_b(1+p(R)z_b).                    \tag{3.3}
\]

In particular the exponential moment of the bad-block count is at most `(1+p(R)(e^s-1))^N` for s>=0 and N tested blocks. This is a moment/entropy bound, not a claim that the full bad-block process is independent or stochastically dominated for every increasing event.

For a block adjacency graph of maximum degree Delta, the number of connected k-block sets containing a fixed root is at most `(4Delta)^(k-1)`. A canonical rooted traversal embeds each such set in a rooted ordered tree; the tree shapes cost at most `4^(k-1)` and edge-neighbor choices at most `Delta^(k-1)`. Therefore, if `4Delta e^a p(R)<1`,

\[
 \mathbb E\sum_{\substack{S\ni b_0\\S\ {\rm connected}}}
       e^{a|S|}\prod_{b\in S}\mathbf1_{\mathsf B_b(R)}
 \le\frac{e^a p(R)}{1-4\Delta e^a p(R)}.          \tag{3.4}
\]

This is a summable Gaussian bad-set bound. It does not by itself estimate interacting polymer activities, a determinant expansion, or strict background dependence.

## 4. Application to the microscopic derivative field

Use (1.2)–(1.3). A fixed microscopic block contains a fixed number of fine sites; after including its chosen first-difference/color coordinates, m is fixed independently of M. Disjoint tested coordinate sets have nu=1; uniformly enlarged blocks have a fixed overlap nu. Thus

\[
 \mathbb P\!\left\{\text{every }b\in S\text{ has }
       \max_{I_b}|\eta^2\nabla Z|>R\right\}
 \le\left[m\sqrt2 e^{-R^2/(4\nu K_D)}\right]^{|S|}.
                                                               \tag{4.1}
\]

The constants are uniform over homogeneous macroscopic refinements and regulator volumes. Rescaled curl coordinates are included by applying the fixed local curl combination to the derivative vector, which changes K_D and the stencil incidence by fixed constants.

A fixed unit *physical* cell contains M^4 fine sites and does not have a fixed m. Replacing microscopic blocks by such cells in (4.1) makes the entropy prefactor grow with M. The theorem is therefore a microscopic bad-block statement, not a uniform statement that a whole physical cell has bounded fine supremum with large probability.

The derivative part of the rescaled microscopic Hölder norm is also controlled: `eta^(2+alpha)[nabla Z]_alpha` is at most twice `||eta^2 nabla Z||infinity` on sampled points, with fixed collar factors. This does not add the potential component absent from (1.3).

## 5. Fixed-ratio one-step scaling includes the potential field

Now consider a single homogeneous step with fine spacing eta, coarse spacing `h=L eta`, and fixed ratio L. This is not the full macroscopic ratio M=L^j treated as one step. Let `x=h y` and define the rescaled potential

\[
 Z_s(y)=h Z_{\rm phys}(x),\qquad \eta_* =\eta/h=1/L.
                                                               \tag{5.1}
\]

In d=4, `nabla_eta Z_phys=h^(-2) nabla_(1/L) Z_s` and the Maxwell action is exactly scale invariant:

\[
 \eta^4\sum|d_\eta Z_{\rm phys}|^2
       =L^{-4}\sum|d_{1/L} Z_s|^2.
                                                               \tag{5.2}
\]

For the homogeneously rescaled fixed-ratio constraints, Z_s is the unit-coarse-scale constrained Gaussian with covariance operator C_L. Its counting covariance is `L^4 C_L`. The dimensionless potential/derivative pair is

\[
 Y_{\rm step}=(\eta Z_{\rm phys},\eta^2\nabla_\eta Z_{\rm phys})
       =(Z_s/L,\nabla_{1/L}Z_s/L^2).
\]

Its exact counting covariance is therefore

\[
 \boxed{\quad
 \operatorname{Cov}_{\rm count}(Y_{\rm step})
       =S_L\mathcal C_L S_L^T,
 \qquad S_L=\begin{pmatrix}L I\\\nabla_{1/L}\end{pmatrix}.
 \quad}                                                       \tag{5.3}
\]

Equivalently the physical covariance operator at scale h is h^2 C_L in the corresponding coordinate matrix, and the counting covariance of Z_phys is `eta^(-4) h^2 C_L`; this gives the same (5.3).

If `||C_L||<=c_0` and `||nabla C_L nabla^T||<=c_1`, positivity gives

\[
 \|S_L\mathcal C_LS_L^T\|
       \le L^2c_0+c_1=:K_L.                      \tag{5.4}
\]

The flat estimates supply c_0,c_1 uniformly in the number of coarse cells. Because L is fixed, K_L is fixed. Cross covariances require no new estimate: factor the full positive block covariance as `(S_L C_L^(1/2))(S_L C_L^(1/2))^T`.

The general theorem now gives joint microscopic tails for both rescaled potentials and derivatives at a single fixed-L step, with K=K_L. Their block norm may also include the microscopic first-difference Hölder member at fixed cost. This conclusion does not contradict (1.4): replacing fixed L by the full refinement M makes the potential contribution in (5.4) grow as M^2.

For a real changed quadratic form, a further application is conditional but elementary: if its positive precision on the same real coordinate space obeys `K_new >= (1-epsilon)K_base`, with epsilon<1, then its covariance is at most `(1-epsilon)^(-1)` times the baseline covariance. Replace K_L by that enlarged constant. Identifying an actual nonflat/source quadratic form with this hypothesis is a separate model estimate; it is not assumed merely from small potential values.

## 6. Holomorphic relative quadratic perturbations without a volume factor

Here is an abstract complex extension with a precise domain. Whiten the real baseline Gaussian on its nondegenerate slice: let zeta be standard real Gaussian in R^N, and let `Y=A zeta`, with `AA^T<=K I`. The slice can have arisen from the degenerate ambient covariance; N is its actual Gaussian dimension.

Let E be a complex symmetric N by N matrix with

\[
 \|E\|_{2\to2}\le\epsilon\le\tfrac14.
\]

Define the normalized complex Gaussian functional

\[
 d\mu_E(\zeta)=\det(I+E)^{1/2}
       e^{-\zeta^TE\zeta/2}\,d\gamma_N(\zeta),    \tag{6.1}
\]

using the analytic determinant branch equal to one at E=0. It has total mass one. In physical variables this hypothesis is exactly a relative quadratic bound `||K_X^(-1/2) V_X K_X^(-1/2)||<=epsilon`; no absolute coordinate-size bound is substituted for it. It is not a positive probability measure at complex E.

**Theorem 6.1.** For blocks satisfying (2.1), and every set S of k blocks,

\[
 \boxed{\quad
 \left|\mu_E\!\left(\bigcap_{b\in S}\mathsf B_b(R)\right)\right|
 \le\left[2^m\exp\!\left(-\frac{R^2}{6\nu K}\right)\right]^k.
 \quad}                                                       \tag{6.2}
\]

There is no ambient-N factor. The event uses the fixed real linear observable Y=A zeta and a fixed real threshold. It does not vary nonholomorphically with E.

Proof. The union of the tested coordinates in S spans an r-dimensional real row space of A, with r<=mk. Make a real orthogonal change of Gaussian coordinates so that all these tests depend only on x in R^r, and write the remaining variables as z. Integrating z exactly gives the normalized complex Gaussian marginal on x with precision

\[
 B=I+E_{11}-E_{12}(I+E_{22})^{-1}E_{21}.
                                                               \tag{6.3}
\]

Consequently

\[
 \|B-I\|\le\epsilon+\frac{\epsilon^2}{1-\epsilon}
       =\frac{\epsilon}{1-\epsilon}=:s\le\tfrac13,
 \quad \operatorname{Re}B\ge(1-s)I=:\beta I,
 \quad \beta\ge\tfrac23.                         \tag{6.4}
\]

The real-part inequality is in the ordinary real quadratic form, or equivalently its Hermitian numerical-range interpretation. Since `|det B|<=||B||^r<=(1+s)^r`, the modulus of the normalized marginal density is bounded by

\[
 \left(\frac{1+s}{\beta}\right)^{r/2}
           d\gamma_{\beta^{-1}I_r}(x)
       \le 2^{r/2}d\gamma_{\beta^{-1}I_r}(x).      \tag{6.5}
\]

Under this dominating real Gaussian, the tested vector has covariance norm at most `K/beta`. Collect all the block tests with repetitions. Its dimension is at most mk, overlap at most nu, and covariance norm at most `nu K/beta`. On the all-bad event the sum of squares is at least kR^2. The exponential-square bound at `t=beta/(4nu K)` gives probability at most

`2^(mk/2) exp[-beta k R^2/(4nu K)]`.

Multiplying by `2^(r/2)<=2^(mk/2)` and using beta>=2/3 proves (6.2).

The proof also bounds a bounded measurable factor depending only on the same tested marginal, multiplied by the all-bad indicator, by its supremum times the right side. It does not bound the integral of the modulus of the *full* N-dimensional density over that event without an N-dependent factor. Marginalizing the untested variables before taking the modulus is essential. Likewise a bounded observable involving additional untested coordinates requires enlarging the marginal and accounting for its dimension.

For fixed tested events the normalized integral is holomorphic in E on the complex operator ball: at each finite N the real-part lower bound gives Gaussian domination on compact subballs, and the determinant branch is analytic. If E depends holomorphically on source parameters with a known uniform neighborhood staying in this relative ball, multivariable Cauchy gives factorial source derivatives of the local event integral, multiplied by the same block decay evaluated on that larger neighborhood. This is conditional on the specified relative perturbation and fixed observable; it does not establish such a source neighborhood for an unverified Yang--Mills Hessian.

The event bound can again be inserted in the finite expansion of `prod_b(1+z_b 1_bad)` with nonnegative z_b, yielding an absolute bound by `prod_b(1+p_complex(R)z_b)` with `p_complex=2^m exp[-R^2/(6nu K)]`. Here p_complex need not be at most one; these are normalized complex expectations, not probabilities. The same connected-set counting applies whenever its entropy smallness inequality holds.

## 7. Provenance and unresolved quantum identifications

The deposited action and measure conventions are matched at pinned commit `e392ef45013a581664bab76b90867170b30fe10e`: Raw I:464–479 fixes the coupling-free Wilson action and the outside coupling; I:12756–12760 fixes the physical pairings; I:15643–15648 fixes the left-exponential quadratic expansion, which agrees with the ordinary flat coordinate at identity. These checks are recorded in `wilson_source_normalization_research.md`.

The flat corrected bond average and its homogeneous composition are matched to the deposited formulas at I:24349–24373 and I:47046–47048; the scalar source projection is matched at I:23937–23944. The rigorous inputs actually used here are the proved variational C and the full-G0 derivative sandwich, specifically `flat_full_inverse_research.md` §§7–8 and `flat_constrained_schauder_research.md` §§1–2. Their positivity gives (1.3). The covariance-counting normalization is audited in `flat_gaussian_roughness_audit.md`.

Thus the real derivative block theorem applies to the actual homogeneous flat constrained Gaussian already constructed. The fixed-L value-and-derivative application is its exact d4 scale transform. The complex theorem is an abstract quantitative consequence of an explicitly stated relative quadratic hypothesis. None of these assertions identifies a nonlinear Haar/Jacobian integral with this Gaussian, supplies a full retained-history source covariance, or bounds interactions on bad sets. The joint derivative tails and the fixed-step joint tails are useful Gaussian inputs to that subsequent work, not the subsequent work itself.
