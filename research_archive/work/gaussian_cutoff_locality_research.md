# Strict background locality from a small local precision perturbation

Research proof candidate, 16 October 2026. This extends `gaussian_cutoff_cluster_research.md`. The argument below is intended for independent audit before promotion to an established notebook theorem. It supplies a sufficient abstract hypothesis, not a verification of the deposited Yang--Mills precision matrix or its interaction terms.

## 1. Proposed theorem and the cancellation it uses

Let a centered Gaussian precision matrix be

\[
 Q(A)=Q_0+V(A),\qquad V(A)=\sum_Y V_Y(A|_Y),             \tag{1.1}
\]

where the background-independent inverse C_0=Q_0^{-1} is uniformly gapped and exponentially decaying. Each symmetric matrix V_Y has rows and columns supported on Y and depends holomorphically only on the background in Y. If a weighted local matrix norm of the V_Y is sufficiently small, then the logarithm of the sharp cutoff probability has an exact expansion

\[
 \log\mathbb E_{Q(A)^{-1}}\prod_{b\in\Lambda}
         \mathbf1_{\{\|x_b\|\le R\}}
   =\sum_{H\subset\Lambda\text{ or its lattice hull}}E_H(A|_H),
                                                        \tag{1.2}
\]

where H is connected, E_H is holomorphic and strictly local in A, and for some fixed a_*>0,

\[
 \sup_b\sum_{H\ni b}e^{a_*|H|}\|E_H\|_\infty
                            \le C\,e^{-cR^2}.           \tag{1.3}
\]

All constants are volume-independent. A precise version with explicit sufficient smallness conditions is developed below.

The activities are finite-volume objects: more precisely they are E_{Lambda,H}, and may depend on the entire background-independent baseline C_{0,Lambda}. Strict locality means that their **variable background dependence** reads only A|_H. It does not assert that E_{Lambda,H}=E_{Lambda',H}, or that these activities have a thermodynamic limit, without an additional consistency or comparison argument for the baselines. Volume-independent bounds and volume consistency are different claims.

The crucial normalization is to expand the Gaussian *marginal density on a nonempty marked set S*. Neumann paths contributing to that marginal begin and end at S. Thus every background perturbation in every coefficient is connected to S. There is no bulk determinant with disconnected source-only loops left to cancel later. The moment expansion has no empty marked polymer, and its logarithm therefore has no contribution containing background sources alone.

## 2. Fixed baseline and local precision norm

Work on a finite subset Lambda of Z^d, with lattice graph distance and D real coordinates per block. Constants below are uniform in Lambda. The baseline C_0 is real symmetric positive, or more generally complex symmetric with

\[
 \operatorname{Herm}C_0\ge\lambda I,
 \qquad \|C_0\|\le\Lambda_0.                            \tag{2.1}
\]

Fix 0<kappa<m such that

\[
 K:=\sup_b\sum_c e^{(\kappa+2m)d(b,c)}\|(C_0)_{bc}\|
                                                    <\infty.\tag{2.2}
\]

Symmetry gives the same column bound. The choice is possible whenever C_0 has exponential decay at a larger rate. Let ell(Y) be the minimum metric spanning-tree length of Y, with ell(singleton)=0. The background domain is a product of complex domains; every V_Y is holomorphic on its corresponding finite-coordinate domain. Define

\[
 \nu:=\sup_b\sum_{Y\ni b}\sum_{c\in Y}
          e^{(\kappa+2m)\ell(Y)}\|(V_Y)_{bc}\|_\infty.  \tag{2.3}
\]

Every V_Y is individually symmetric, so (2.3) also controls columns. In particular ||V|| in the ordinary Schur matrix norm is at most nu. We assume K nu<1 and further smallness conditions in Section 5. These conditions are fixed before the cutoff radius is increased.

The covariance is the convergent Neumann series

\[
 C(A)=\sum_{j\ge0}(-1)^j C_0(VC_0)^j.                 \tag{2.4}
\]

Expanding V into its V_Y terms assigns every coefficient an explicit finite background support, the union of its Y labels. The precision perturbations need not have mutually disjoint supports.

## 3. The support algebra rooted at the marked set

Fix a nonempty marked set S. For a finite background support X, define ell_S(X) as the minimum total metric edge length of a forest on S union X such that every component meets S. The roots S may remain in different components. Let ell_S(empty)=0. Two properties are immediate:

\[
 \ell_S(X\cup X')\le\ell_S(X)+\ell_S(X'),\qquad
 S\subset S'\Longrightarrow\ell_{S'}(X)\le\ell_S(X).   \tag{3.1}
\]

Consider formal families F=(F_X)_X, where F_X is a bounded holomorphic function of A|_X, with norm

\[
 \|F\|_{\mathcal B_S}
       =\sum_X e^{\kappa\ell_S(X)}\|F_X\|_\infty.       \tag{3.2}
\]

The product is union convolution: (FG)_Z=sum_{X union X'=Z}F_X G_X'. Equation (3.1) makes this a commutative unital Banach algebra after completion. Evaluation F -> sum_X F_X(A|_X) is a bounded algebra homomorphism. Nonuniqueness of representations is harmless: use the explicit power series in the V_Y, grouped by the union of their supports. Formal auxiliary variables multiplying the V_Y can be retained until absolute convergence is proved.

For block matrices with entries in this algebra, use the maximum of row and column Schur norms, with the block operator norm inside the support sum. This matrix norm is submultiplicative.

Let Delta C=C-C_0. Its actual marginal on S has the following uniform bound:

\[
 \max\left\{
 \sup_{b\in S}\sum_{c\in S}e^{2m d(b,c)}
                    \|(\Delta C_S)_{bc}\|_{\mathcal B_S},
 \sup_{c\in S}\sum_{b\in S}e^{2m d(b,c)}
                    \|(\Delta C_S)_{bc}\|_{\mathcal B_S}
 \right\}
 \le v:=\frac{K^2\nu}{1-K\nu}.                         \tag{3.3}
\]

**Proof.** In a term C_0 V_{Y_1} C_0 ... V_{Y_j} C_0 with endpoints b,c in S, choose a spanning tree for each Y_i and the covariance links between consecutive perturbations. Their union connects every background support to b and c. If L is the sum of those covariance-link distances plus sum_i ell(Y_i), then ell_S(union_i Y_i)<=L and d(b,c)<=L. Therefore

\[
 e^{\kappa\ell_S(\cup_iY_i)+2m d(b,c)}
                                        \le e^{(\kappa+2m)L}.
\]

Successive weighted matrix row sums bound the order-j contribution by K^(j+1) nu^j. Summing j>=1 proves (3.3). In particular each entry is at most v exp(-2m d(b,c)) in the support norm. This estimate localizes the *full covariance marginal*, not only visible tree-edge factors.

## 4. A uniform inverse Schur bound for tree-deformed baselines

Set

\[
 \delta=\lambda/4,\qquad J_{bc}=K e^{-m d(b,c)}\quad(b\ne c).
                                                        \tag{4.1}
\]

For a tree T on S with degrees d_b, let s^T be a BKAR point and let z_e vary over the product discs

\[
 |z_{\{b,c\}}|<\frac{\delta}{\max(d_b,d_c)J_{bc}}.
                                                        \tag{4.2}
\]

Let M_0 be C_{0,S} with off-diagonal entries multiplied by s^T+z on tree edges, by s^T on other edges, and diagonal entries unchanged. The row and column norms of its perturbation from C_{0,S}(s^T) are at most delta, because ||C_0,bc||<=J_bc and sum_{c neighbor b}1/max(d_b,d_c)<=1. Thus

\[
 \operatorname{Herm}M_0\ge\lambda I/2,\qquad
 \|M_0\|\le2\Lambda_0.                                 \tag{4.3}
\]

More strongly, the Schur norm with entry weight exp(m d(b,c)) is at most K+delta. Indeed ||C_0,bc||<=K exp[-(kappa+2m)d(b,c)], so the tree perturbation has weighted row sums at most delta.

Here is an elementary uniform inverse estimate. If a matrix M has Herm M>=aI and weighted Schur norm at rate m at most Kbar, set

\[
 s=\min\{m/2,\ a e m/(4\overline K)\}.
\]

For a fixed c, conjugate by the diagonal weight D_bb=exp(s d(b,c)). The row and column norm of DMD^{-1}-M is bounded by

\[
 \overline K\sup_{r\ge0}(e^{sr}-1)e^{-mr}
 \le\frac{2s\overline K}{em}\le a/2.
\]

Since ||M^{-1}||<=1/a, a Neumann inverse gives ||(DMD^{-1})^{-1}||<=2/a. Consequently

\[
 \|(M^{-1})_{bc}\|\le(2/a)e^{-s d(b,c)}.               \tag{4.4}
\]

Applying this to M_0 with a=lambda/2 and Kbar=K+delta yields a finite uniform ordinary inverse Schur bound

\[
 L:=\frac4\lambda\sum_{z\in\mathbb Z^d}e^{-s|z|},
 \qquad \|M_0^{-1}\|_{\mathrm{Schur}}\le L.             \tag{4.5}
\]

This estimate works for arbitrary S, every tree, every BKAR parameter, and every complex point in (4.2). There is no assumption of translation invariance of the covariance itself; the lattice sum is only a uniform counting bound.

## 5. Expand the entire marginal density in the support algebra

Apply the same mask s^T+z to C_S(A)=C_{0,S}+Delta C_S. The resulting matrix is M=M_0+E. By (3.3), its background-dependent part obeys

\[
 \|E\|_{\mathrm{Schur}(\mathcal B_S)}
 \le v_1:=v(1+\delta/K).                               \tag{5.1}
\]

The contribution of s^T has norm at most v. The additional tree edges have row sums bounded by delta v/K, using their exp(-2m d) coefficient bound and (4.2).

Impose the following explicit sufficient conditions:

\[
 v_1\le\lambda/4,\qquad u:=Lv_1\le1/2,\qquad
 w:=\frac{L^2v_1}{1-u}\le\frac1{2V},\qquad
 V:=8\Lambda_0^2/\lambda.                              \tag{5.2}
\]

All are satisfied for sufficiently small nu with the baseline constants fixed. In the matrix support algebra, put F=M_0^{-1}E. Then

\[
 M^{-1}-M_0^{-1}=\sum_{j\ge1}(-F)^jM_0^{-1},
 \qquad \|M^{-1}-M_0^{-1}\|_{\mathrm{Schur}(\mathcal B_S)}\le w,
                                                        \tag{5.3}
\]

and

\[
 \|\operatorname{Tr}\log(I+F)\|_{\mathcal B_S}
                       \le D|S|[-\log(1-u)].             \tag{5.4}
\]

The Gaussian density has the exact algebra identity

\[
 p_M(x)=p_{M_0}(x)
  \exp\left[-\tfrac12\operatorname{Tr}\log(I+F)
            -\tfrac12x^T(M^{-1}-M_0^{-1})x\right].       \tag{5.5}
\]

This identity expands both the determinant and the inverse. Its norm is bounded by

\[
 \|p_M(x)\|_{\mathcal B_S}
 \le |p_{M_0}(x)|
      \exp\left[\tfrac{D|S|}2[-\log(1-u)]
                              +\tfrac w2\|x\|^2\right].\tag{5.6}
\]

To justify the quadratic estimate, take block Euclidean norms of x and use the row-and-column Schur bound w. Equation (4.3) gives Herm M_0^{-1}>=V^{-1}I and |det M_0|>=(lambda/2)^(D|S|). With (5.2), (5.6) is bounded by (8V/lambda)^(D|S|/2) times the independent real Gaussian density of covariance 2V I.

Integrating against the fixed sharp defect product therefore yields the Banach-valued all-marked bound

\[
 \left\|\int p_M(x)\prod_{b\in S}q_b(x_b)\,dx\right\|_{\mathcal B_S}
 \le\widehat\tau_R^{|S|},\qquad
 \widehat\tau_R=\left(\frac{16V}{\lambda}\right)^{D/2}
                                      e^{-R^2/(8V)}.    \tag{5.7}
\]

The Gaussian tail is weakened only by fixed constants. Coefficient sums, integrals, Neumann series, logarithm series, and exponential series can be interchanged by the displayed absolute majorants. The sharp indicators are not differentiated. All coefficient functions remain holomorphic in their finite background supports.

## 6. Banach-valued tree bounds and the marked polymer gas

Use the exact moment/forest definitions from Sections 3--6 of `gaussian_cutoff_cluster_research.md`, now with their explicit support series. Banach-valued Cauchy applied to (5.7) yields

\[
 \|\partial_T f_S(s^T)\|_{\mathcal B_S}
 \le\widehat\tau_R^n(e^2/\delta)^{n-1}
                  \prod_{b\in S}d_b!\prod_{e\in T}J_e,
 \qquad n=|S|.                                        \tag{6.1}
\]

The same factorial tree identity applies. Let

\[
 A_\kappa=K\sum_{z\ne0}e^{-(m-\kappa)|z|},\qquad
 B_0=8e^2 A_\kappa/\delta.
\]

Write the canonical local representation as zeta(S)=sum_X zeta(S;X)(A|_X). Then

\[
 \sup_b\sum_{S\ni b}\sum_X
 e^{\kappa\ell(S)+\kappa\ell_S(X)+\alpha|S|}
                           \|\zeta(S;X)\|_\infty
 \le\frac{\widehat\tau_R e^\alpha}
              {1-B_0\widehat\tau_R e^\alpha}.           \tag{6.2}
\]

Forest factorization is an identity of the formal source series: setting cross-component covariance entries to zero makes the *marginal Gaussian matrix* block diagonal, even though its blocks depend on overlapping background supports. Thus the exact hard-core gas remains indexed by pairwise disjoint **marked** sets S. It would be incorrect to replace this compatibility by disjointness of their enlarged background supports.

This causes no problem for the logarithm. Apply the scalar majorant criterion to

\[
 \widetilde z(S)=e^{\kappa\ell(S)+|S|}
                  \sum_Xe^{\kappa\ell_S(X)}\|\zeta(S;X)\|_\infty.
\]

If widehat tau_R<=[2e^2 max(1,B_0)]^{-1}, the rooted logarithmic cluster bound follows exactly as in Section 7 of the preceding note.

## 7. From a marked cluster to a strictly local connected support

Group each logarithmic cluster first by its union M of marked blocks and its union X of background supports, obtaining U(M;X)(A|_X). M is always nonempty. Connectedness of the overlap graph of marked polymers gives

\[
 \ell(M)\le\sum_i\ell(S_i),\qquad
 \ell_M(\cup_iX_i)\le\sum_i\ell_{S_i}(X_i),\qquad
 |M|\le\sum_i|S_i|.
\]

The scalar majorant therefore proves

\[
 \sup_b\sum_{M\ni b,X}
      e^{\kappa[\ell(M)+\ell_M(X)]+|M|}
                              \|U(M;X)\|_\infty
                              \le2e^2\widehat\tau_R.    \tag{7.1}
\]

Choose, once and for all, a deterministic minimizing metric tree for M and a minimizing forest attaching X to M. Realize their edges by deterministic shortest lattice paths. Their union H(M,X) is connected, contains M union X, and obeys

\[
 |H(M,X)|\le |M|+L(M,X),\qquad
 L(M,X):=\ell(M)+\ell_M(X).                             \tag{7.2}
\]

For any a in M and b in H(M,X), d(a,b)<=L(M,X). If the original finite region is not geodesically convex, the support can be taken in its lattice hull; the coefficient still reads only background coordinates in X, which were inside the original region.

Group by H to define E_H. It is holomorphic and reads only A|_H. Set a_*=min(1/2,kappa/4). For b in H and a in M,

\[
 e^{a_*|H|}
 \le e^{|M|+\kappa L(M,X)}e^{-(\kappa/2)d(a,b)}.        \tag{7.3}
\]

Choose one marked a, or simply overcount by all a in M, and use (7.1). This gives the explicit connected-support norm

\[
 \boxed{\quad
 \sup_b\sum_{H\ni b}e^{a_*|H|}\|E_H\|_\infty
 \le2e^2\left(\sum_{a\in\mathbb Z^d}e^{-(\kappa/2)|a|}\right)
                                      \widehat\tau_R.\quad} \tag{7.4}
\]

The loss in decay exponent pays for roots that belong to a background support or an added connecting path rather than to a marked defect. This is the step that a mark-rooted estimate alone would miss.

## 8. Scope and interfaces still requiring model verification

Under the stated small local precision norm, the above proof candidate supplies strict local Gaussian cutoff activities and retains the Gaussian tail factor. It avoids a separate cancellation of unmarked components by expanding normalized marginals on nonempty mark sets from the outset.

The following are not consequences of this theorem:

1. A general uniformly gapped, background-dependent precision admits a uniformly small decomposition (2.3) on the exact complex neighborhood required by the RG argument.
2. Gauge constraints or background-dependent coordinates can be put in the fixed-block, fixed-real-domain form assumed here without changing the cutoff analyticity problem.
3. The small local precision expansion remains uniform over the deposited histories and scales, with constants chosen before epsilon.
4. The full interacting measure obeys the same estimate. Nonquadratic interaction polymers require a joint expansion and stability argument.
5. The obtained positive connected-support exponent a_* meets any particular numerical polymer norm in the deposited theorem. A stronger target exponent requires enough baseline and local-perturbation decay at the start.
6. The finite-volume activities agree when the volume changes. Their background-independent baseline covariance may change with the volume, even for an activity whose variable background support is fixed.
7. The admissible gauge-potential/current domain is a product domain of the kind assumed in Section 2. A general weak gauge-potential ball or a constrained gauge domain is not silently identified with that product. One must supply an appropriate product chart/polydomain or separately verify that the same support algebra and its uniform local-function bounds are valid on the actual domain.

The abstract Gaussian locality mechanism is nevertheless more than a covariance-path heuristic: it expands and bounds the full marginal determinant and inverse, preserves fixed-domain analyticity, distinguishes mark compatibility from background-support overlap, and explicitly pays for roots introduced by the localization paths.
