# Gaussian cutoff defects: a connected expansion and its locality limit

Research note, 16 October 2026. Independent derivation by the provenance agent, cross-checked against the root agent's simultaneous derivation. This proves an abstract Gaussian statement under the assumptions below. It does not verify those assumptions for the deposited Yang--Mills fluctuation measure, and it does not establish the interacting cutoff-transfer theorem.

## 1. Precise conclusion

Uniform complex accretivity, bounded covariance, fixed block dimension, and exponential decay of covariance blocks suffice for an exact hard-core polymer expansion of a sharp Gaussian cutoff partition function. Its logarithm has activities exponentially localized in the positions of the marked blocks, of norm O(exp(-c R^2)). No derivative of an indicator is taken.

They do **not** suffice for strict locality in the background on which the covariance depends. This distinction is substantive: even a diagonal covariance can have arbitrary remote background dependence. Sections 9--11 separate what is proved from possible additional locality inputs.

## 2. Assumptions and notation

Let the block set be a finite subset Lambda of Z^d, with a fixed lattice metric. Every block variable x_b is in R^D, with D fixed. Let A range over an open complex background domain U. The covariance C_Lambda(A) is complex symmetric, holomorphic, and obeys, uniformly in A and Lambda,

\[
 \operatorname{Herm} C_\Lambda(A)\ge\lambda I,
 \qquad \|C_\Lambda(A)\|\le\Lambda_0,
 \qquad 0<\lambda\le\Lambda_0<\infty.                 \tag{2.1}
\]

For distinct blocks assume the fixed majorant

\[
 \|C_{bc}(A)\|\le J_{bc}=J_{cb},\qquad
 A_\kappa:=\sup_b\sum_{c\ne b}e^{\kappa d(b,c)}J_{bc}<\infty
                                                        \tag{2.2}
\]

for some kappa>0. Exponential covariance decay of rate mu implies this for any kappa<mu. Set J_bb=0. Constants may depend on D, lambda, Lambda_0, kappa and A_kappa, but not on volume, A, or the cutoff radius R.

Principal submatrices are denoted C_S. All Gaussian expectations in the finite volume use those actual marginals. A consistency assumption between different volumes is unnecessary for the finite-volume bounds, although it is needed for a particular infinite-volume interpretation.

For a complex accretive symmetric matrix M, define

\[
 p_M(x)=(2\pi)^{-N/2}(\det M)^{-1/2}
             \exp[-\tfrac12x^T M^{-1}x].               \tag{2.3}
\]

The determinant branch is the analytic branch on the convex accretive cone agreeing with the positive square root for real positive matrices. This density integrates to one. Its real-domain integral is absolutely convergent since

\[
 \operatorname{Herm} M^{-1}
    =M^{-*}(\operatorname{Herm}M)M^{-1}>0.
\]

Take the fixed, background-independent sharp defects

\[
 q_b(x_b)=-\mathbf1_{\{\|x_b\|_2>R\}},\qquad
 Z_\Lambda(A)=\int p_{C_\Lambda(A)}(x)
                         \prod_{b\in\Lambda}(1+q_b(x_b))\,dx.
                                                        \tag{2.4}
\]

The real integration region and threshold do not move with complex A. A background-dependent norm or cutoff domain requires a separate analyticity argument and is not covered merely by writing (2.4).

## 3. BKAR interpolation stays in the accretive domain

For pairs e={b,c} in S, let s_e multiply the off-diagonal blocks C_bc and C_cb, leaving the diagonal blocks fixed. Write the resulting matrix as C_S(s). For a partition pi of S, the zero-one partition mask v_pi sets cross-component blocks to zero, so C_S(v_pi) is a direct sum of principal submatrices. Consequently it obeys (2.1).

Every s in the convex hull K_S of partition masks therefore obeys (2.1) too. For a forest F and edge parameters t_e in [0,1], the BKAR mask is

\[
 s^F_{bc}(t)=
 \begin{cases}
 \min_{e\in\text{path}_F(b,c)}t_e,&b,c\text{ in one component},\\
 0,&b,c\text{ in different components}.
 \end{cases}                                             \tag{3.1}
\]

This belongs to K_S: at each level u in [0,1], retain the edges with t_e>=u and take the partition into their components; integrating the corresponding partition masks over u gives s^F.

Define

\[
 f_S(s;A)=\int p_{C_S(s;A)}(x)\prod_{b\in S}q_b(x_b)\,dx.
                                                        \tag{3.2}
\]

It is analytic in a neighborhood of K_S and holomorphic in A. This follows directly from (2.1), dominated Gaussian integration, and compactness for the finite number of interpolation variables. The BKAR formula is valid directly for a sufficiently smooth function on K_S; there is no need to assume that every arbitrary mask in the full coordinate cube preserves positive definiteness. Abdesselam's primary notes state precisely this convex-hull version (Theorem 1, pp.1--2).

## 4. A uniform complex Gaussian all-marked tail

Choose

\[
 \delta=\lambda/2,\qquad V=8\Lambda_0^2/\lambda,\qquad
 \tau_R=\left(\frac{4V}{\lambda}\right)^{D/2}
                              e^{-R^2/(4V)}.             \tag{4.1}
\]

Suppose M is a complex symmetric perturbation, of operator norm at most delta, of an interpolated covariance C_S(s), s in K_S. Then

\[
 \operatorname{Herm}M\ge\lambda I/2,\quad
 \|M\|\le2\Lambda_0,\quad
 \operatorname{Herm}M^{-1}\ge V^{-1}I,\quad
 |\det M|\ge(\lambda/2)^{D|S|}.                          \tag{4.2}
\]

Thus the modulus of its density is at most (2V/lambda)^(D|S|/2) times the density of independent centered real Gaussian coordinates of variance V. For a D-dimensional block G of that real Gaussian,

\[
 \mathbb P(\|G\|>R)
 \le e^{-R^2/(4V)}\mathbb E e^{\|G\|^2/(4V)}
 =2^{D/2}e^{-R^2/(4V)}.
\]

It follows that

\[
 \left|\int p_M(x)\prod_{b\in S}q_b(x_b)\,dx\right|
                              \le\tau_R^{|S|}.           \tag{4.3}
\]

The prefactor in tau_R is deliberately conservative. The important features are its fixed constants, uniformity in the complex background, and one Gaussian-tail factor for every marked block.

## 5. Degree-adapted Cauchy radii: the tree derivative estimate

Let T be a tree on n=|S|>=2 vertices and let d_b be its vertex degrees. At a BKAR point s^T(t), allow independent complex changes z_e in its tree-edge coordinates, of radii

\[
 r_{\{b,c\}}=\frac{\delta}{\max(d_b,d_c)J_{bc}}.          \tag{5.1}
\]

An edge with J_bc=0 contributes a zero derivative and can be omitted. For the resulting matrix perturbation E,

\[
 \sum_c\|E_{bc}\|
 \le\delta\sum_{c:\{b,c\}\in T}\frac1{\max(d_b,d_c)}
 \le\delta.
\]

Because C is complex symmetric, the norm of a transposed block equals the norm of that block; the same bound holds for column sums. The block Schur bound gives ||E||<=delta. We can apply (4.3) throughout the product polydisc. Multivariate Cauchy, with each coordinate differentiated exactly once, gives

\[
 |\partial_T f_S(s^T(t);A)|
 \le \tau_R^n\delta^{-(n-1)}
       \prod_{\{b,c\}\in T}\max(d_b,d_c)J_{bc}.          \tag{5.2}
\]

Open radii suffice; take increasing radii to obtain the displayed closed bound. There is no n! from Cauchy because the multi-index has every entry equal to one.

For integer degrees d>=1, d^d<=e^d d!. Since max(d_b,d_c)<=d_b d_c and sum_b d_b=2n-2,

\[
 \prod_{\{b,c\}\in T}\max(d_b,d_c)
 \le\prod_b d_b^{d_b}
 \le e^{2n-2}\prod_b d_b!.
\]

Hence

\[
 |\partial_T f_S(s^T(t);A)|
 \le \tau_R^n(e^2/\delta)^{n-1}
                 \prod_b d_b!\prod_{\{b,c\}\in T}J_{bc}.
                                                        \tag{5.3}
\]

Every differentiation in this proof concerns the analytic covariance parameters in the Gaussian density. The sharp indicators remain fixed bounded measurable multipliers.

The root agent's alternative radii eta/[(d_b+d_c)J_bc] also work and give the weaker but valid constant (2e^2/eta)^(n-1). The combinatorial conclusion is identical.

## 6. Exact cumulant polymers and factorial combinatorics

Let m(S)=f_S(1). BKAR and factorization across forest components give exactly

\[
 m(S)=\sum_{\pi\text{ partition of }S}\prod_{B\in\pi}\zeta(B),
                                                        \tag{6.1}
\]

where zeta({b})=m({b}) and, for |B|>=2,

\[
 \zeta(B)=\sum_{T\text{ tree on }B}\int_{[0,1]^T}
                    \partial_T f_B(s^T(t))\,dt.          \tag{6.2}
\]

Thus zeta(B) is the joint cumulant of the distinct defect variables indexed by B. Expanding the product in (2.4) and using (6.1),

\[
 Z_\Lambda=\sum_{\{B_1,\ldots,B_k\}\text{ pairwise disjoint}}
                             \prod_i\zeta(B_i),          \tag{6.3}
\]

including the empty family with weight one. These are hard-core polymers; B need not be nearest-neighbor connected.

Let ell(B) be the minimum length of a metric spanning tree on B, with ell({b})=0. For each fixed tree, exp(kappa ell(B)) can be bounded by the product of exp(kappa d(b,c)) over its edges. To sum all B of size n containing a fixed root b, label the other n-1 distinct vertices and divide by (n-1)!. Dropping the distinctness restriction only increases the bound. Successive leaf sums yield A_kappa^(n-1).

The needed degree sum is exactly

\[
 \sum_{T\text{ on }[n]}\prod_{i=1}^n d_i!
       =(n-2)!\binom{3n-3}{n-2}.                        \tag{6.4}
\]

Indeed, put d_i=k_i+1. The Pruefer count at fixed degree sequence is (n-2)!/prod k_i!, so the remaining sum is the coefficient of z^(n-2) in (1-z)^(-2n), times (n-2)!. In particular,

\[
 \frac1{(n-1)!}\sum_T\prod_i d_i!
 =\frac1{n-1}\binom{3n-3}{n-2}\le8^{n-1}.             \tag{6.5}
\]

With B_0=8e^2 A_kappa/delta, equations (5.3)--(6.5) give

\[
 \sup_b\sum_{B\ni b,\ |B|=n}|\zeta(B)|e^{\kappa\ell(B)}
                          \le\tau_R^n B_0^{n-1}.        \tag{6.6}
\]

For every alpha>=0 with B_0 tau_R exp(alpha)<1,

\[
 \sup_b\sum_{B\ni b}|\zeta(B)|
                      e^{\kappa\ell(B)+\alpha|B|}
 \le\frac{\tau_R e^\alpha}{1-B_0\tau_R e^\alpha}.
                                                        \tag{6.7}
\]

If A_kappa=0, all nonsingleton cumulants vanish and the same formula is interpreted with B_0=0.

## 7. An exponentially localized logarithm

Suppose

\[
 \tau_R\le\frac1{2e^2\max(1,B_0)}.                     \tag{7.1}
\]

Apply the hard-core polymer criterion to the weighted absolute activities

\[
 \widetilde z(B)=|\zeta(B)|e^{\kappa\ell(B)+|B|},
 \qquad a(B)=|B|.
\]

Equation (6.7) with alpha=2 gives

\[
 \sum_{B':\ B'\cap B\ne\varnothing}
                   \widetilde z(B')e^{a(B')}
 \le |B|\,2e^2\tau_R\le a(B).                          \tag{7.2}
\]

Consequently the usual Mayer logarithm converges absolutely:

\[
 \log Z_\Lambda=
 \sum_{m\ge1}\frac1{m!}\sum_{B_1,\ldots,B_m}
       \varphi^T(B_1,\ldots,B_m)\prod_i\zeta(B_i),       \tag{7.3}
\]

where phi^T is the sum over connected graphs on [m] of the product of -1_{B_i intersects B_j} over their edges. Repeated polymers in (7.3) are allowed and are incompatible with themselves. The branch is the one obtained by turning on an auxiliary defect strength from zero; the convergent expansion proves zero-freeness along that polydisc.

Group (7.3) by X=union_i B_i to define U_Lambda(X). When the overlap graph is connected, spanning trees inside the B_i connect their union without extra length, so

\[
 \ell(X)\le\sum_i\ell(B_i),\qquad |X|\le\sum_i|B_i|.
\]

The rooted cluster estimate, followed by summing the distinguished polymer containing a fixed b, yields

\[
 \boxed{\quad
 \sup_b\sum_{X\ni b}|U_\Lambda(X;A)|
                   e^{\kappa\ell(X)+|X|}
 \le \frac{\tau_R e^2}{1-B_0\tau_R e^2}
 \le2e^2\tau_R.\quad}                                 \tag{7.4}
\]

To check the rooting: a cluster whose union contains b has at least one polymer containing b. Choosing one such polymer overcounts; its 1/(m-1)! rooted Mayer sum is bounded by exp(a(B)). Summing its weighted activity gives exactly the right-hand side of (7.4), by (6.7). Thus there is no extra uncontrolled factor proportional to the number of polymers or marks.

Each activity is holomorphic in A. The locally uniform summability makes the logarithm holomorphic too. Equations (6.6)--(7.4) are uniform finite-volume results. They do not require independence, small nearest-neighbor covariance, or positivity of the complex density. Increasing R compensates for any finite A_kappa.

## 8. Running cutoff and epsilon-independent constants

If R(g)=c_0(log g^{-2})^p with c_0>0 and p>1/2, then

\[
 \tau_{R(g)}=K_0\exp[-a_0(\log g^{-2})^{2p}],
 \quad K_0=(4V/\lambda)^{D/2},\quad a_0=c_0^2/(4V).
\]

For every fixed q in R and C_1>0, tau_R(g)<=C_1 g(log g^{-2})^q for sufficiently small g. Indeed with L=log g^{-2}, the logarithm of the ratio is log(K_0/C_1)-a_0 L^(2p)+L/2-q log L, which tends to minus infinity because 2p>1.

The small-g threshold is independent of a target remainder epsilon if all constants in (2.1), (2.2), D, c_0, p, q and C_1 were fixed independently of epsilon. Thus the cutoff-only Gaussian logarithm has a fixed-constant smallness estimate. This does not itself establish stability after multiplication by an interacting density or identify its RG polymer support.

## 9. Why mark localization does not prove background locality

Equations (6.2) and (7.3) depend only on the covariance marginal C_X(A) for their marks X. That covariance marginal may depend on A arbitrarily far from X.

For an explicit counterexample, fix a remote background coordinate A_xstar, with |A_xstar|<1, and take

\[
 C_{bc}(A)=(1+\varepsilon A_{x_*})I_D\,\delta_{bc},
 \qquad 0<\varepsilon<1/2.                              \tag{9.1}
\]

The covariance is holomorphic, uniformly accretive, uniformly bounded, and has identically zero off-diagonal blocks. Yet every singleton defect expectation, and hence every singleton log activity, depends nontrivially on A_xstar. The background dependence remains nonzero however far xstar is from that singleton. One could replace A_xstar by any uniformly bounded holomorphic functional of the full background. Therefore the hypotheses of this note cannot imply even a decaying background-response bound.

The geometric statement in (7.4) is precise: X is the set of marks occurring in a connected cutoff cluster. It is not automatically the set of background coordinates read by that cluster.

## 10. Additional assumptions that can repair the locality interface

**A genuinely sufficient special case.** Suppose in addition that C_bc(A) depends only on background coordinates within a fixed radius rho of {b,c}, uniformly for every b,c (diagonal blocks included). Then every zeta(B), and every U(X), depends only on the rho-neighborhood of B or X, respectively. This follows directly from the finite-dimensional integral and is an exact support statement. This endpoint-local covariance hypothesis is much stronger than decay and is not asserted for an inverse lattice Hessian.

To express the result using connected lattice supports, keep the tree labels in (6.2), and in each logarithmic cluster keep its overlap graph. Add fixed shortest lattice paths along the edges of the trees, then thicken by rho. The resulting connected support contains all background coordinates read by the term. Its cardinality is bounded by a fixed rho-dependent multiple of the total number of marked vertices plus total tree length. By reserving a strict fraction of the decay exponent in (2.2) and allowing a larger fixed alpha in (6.7), the same small-tau argument controls the extra support-size weight. Rooting at an added path vertex costs a finite lattice sum: if a support contains b, choose a marked a whose distance to b is no greater than its total path length plus rho and use a reserved factor exp(-eta d(a,b)). This is a conditional route to strict connected polymer norms, not a property obtained from (2.1)--(2.2) alone.

**Quasilocal response bounds.** A realistic inverse of a local precision operator can instead have a bound of the form

\[
 \|D_{A_x}C_{bc}(A)\|
       \le K\exp[-m(d(b,x)+d(c,x))],                    \tag{10.1}
\]

with analogous tree-local bounds for higher variations. Such a hypothesis connects source positions to the marked covariance graph. For example, if C=Q^{-1} and D_x Q has uniformly bounded finite support near x, then

\[
 D_x C=-C(D_xQ)C                                      \tag{10.2}
\]

and exponential decay of C gives (10.1), up to a fixed support-radius constant. Likewise

\[
 D_yD_x C=C(D_yQ)C(D_xQ)C+C(D_xQ)C(D_yQ)C-C(D_yD_xQ)C.
                                                        \tag{10.3}
\]

These identities give genuine source response information under explicit locality assumptions on Q. They are independent of the cutoff expansion. Differentiating the convergent Gaussian integrals is legitimate; one still needs to organize and bound the extra source edges through the tree and polymer expansions before claiming a localized Hessian estimate for log Z. That extension is not proved here.

**Strict local path expansion.** A uniformly convergent local path expansion of C(A), together with an analytic expansion that localizes *all* covariance dependence of the Gaussian density, could produce exact local supports. Expanding only the visible covariance edge factors in (5.3) is insufficient: the remaining Gaussian determinant and inverse still read the whole marginal. A finite-range precision plus a sufficiently strong weighted Neumann-series contraction is one possible stronger starting hypothesis; this note does not prove the required combined expansion from it.

**Why a naive ball telescope is not enough.** Exponential sensitivity to changes outside a ball can give an exact expansion into local ball-dependent terms. A shell at radius r has an error of order exp(-m r), whereas its ball support contains order r^d sites. Thus this alone does not imply a norm weighted by exp(kappa times support cardinality) in d>1. The distinction cannot be removed by relabeling a ball as a short polymer.

## 11. Remaining interfaces for the Yang--Mills cutoff step

The abstract Gaussian mark expansion is established under (2.1)--(2.2). To use it in the actual cutoff transfer requires separate verification of:

1. Fixed block dimension and uniform complex accretivity/norm bounds on the required background neighborhood, including all admissible scales and histories.
2. Uniform weighted covariance decay, with constants fixed before the small remainder parameter.
3. A fixed real cutoff domain during complex background continuation, or a justified substitute if the original domain moves.
4. The background-local support or source-response estimates actually needed by the downstream extraction theorem. Section 9 shows these do not follow from covariance decay alone.
5. Stability with the actual small interaction insertions and normalization. The Gaussian defect gas is not the full interacting RG gas.

The first nontrivial missing issue after this note is therefore model-specific background locality and interaction compatibility, rather than merely converting Gaussian marked-set tails into a connected mark expansion.

## 12. Primary references used for the two expansion identities

- A. Abdesselam and V. Rivasseau, *Trees, forests and jungles: a botanical garden for cluster expansions*, [arXiv:hep-th/9409094](https://arxiv.org/abs/hep-th/9409094). Original forest formula.
- A. Abdesselam, *Notes on the Brydges--Kennedy--Abdesselam--Rivasseau forest interpolation formula*, [author PDF](https://mabdesselam.github.io/BKAR.pdf), Theorem 1 and the partition-polytope construction, pp.1--3. Used here for the exact forest identity on the accretive interpolation domain.
- R. Kotecky and D. Preiss, *Cluster expansion for abstract polymer models*, Commun. Math. Phys. **103** (1986), 491--498, [DOI](https://doi.org/10.1007/BF01211762), [original article PDF](https://www.math.ucla.edu/~biskup/290k.1.24w/PDFs/Kotecky-Preiss.pdf). Used for convergence and the rooted cluster bound under (7.2).

The degree-adapted covariance polydiscs, the explicit all-marked complex Gaussian estimate, and their combination with the factorial tree sum are derived in this note. They are not attributed to these references as a previously located cutoff-transfer theorem.
