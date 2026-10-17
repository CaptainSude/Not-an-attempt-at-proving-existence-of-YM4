# Cutoff Gaussian: source matching and a local bound

Research note, 16 October 2026. Repository and output notebooks were not modified. Statements labelled “proved” below are finite-dimensional lemmas proved here. The complete Wilson source match remains conditional.

## 1. Result of this pass

The fluctuation variables have fixed dimension per independent bond. After passing to those variables, neither an increasing color dimension nor gauge zero modes inherently prevent a uniform Gaussian tail estimate. The useful sufficient input is a uniformly bounded, uniformly accretive precision on the actual independent coordinates, on a fixed normalized complex-background/current domain.

I prove below:

1. A volume-independent bad-bond estimate, strengthened when bounds on the precision are available.
2. Exact regrouping into fixed-size cell factors with an exponentially small cell parameter.
3. Stability of the covariance hypotheses under the positive Schur multipliers used in a forest interpolation.
4. A cutoff-moment sensitivity bound and a conditional, explicitly localized collar decomposition.

These statements do not prove that the modified Wilson covariance, on the required independent-current domain, satisfies the inputs. The primary articles distinguish physical currents tied to a background from independent currents in the later analytic construction. The deposited manuscript makes substantial additional constructions for the latter; its named hypotheses cannot be replaced by the former theorem without checking the match.

## 2. Primary source map

The following are copies of the original articles:

* [CMP99b](https://scispace.com/pdf/propagators-for-lattice-gauge-theories-in-a-background-field-5dxtm5egtz.pdf), T. Bałaban, *Propagators for lattice gauge theories in a background field*, Commun. Math. Phys. **99** (1985), 389–434, DOI 10.1007/BF01240355.
* [CMP109](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf), *Renormalization group approach to lattice gauge field theories I*, **109** (1987), 249–301, DOI 10.1007/BF01215223.
* [CMP116](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-4penm4k7hc.pdf), Part II, **116** (1988), 1–22, DOI 10.1007/BF01239022.
* [CMP119](https://scispace.com/pdf/convergent-renormalization-expansions-for-lattice-gauge-29jyexd38e.pdf), *Convergent renormalization expansions for lattice gauge theories*, **119** (1988), 243–285, DOI 10.1007/BF01217741.

Page numbers below are journal pages. Parentheses give one-based PDF pages where useful.

### 2.1 Coordinates and constraints

CMP109 pp.266–268, (2.9)–(2.13) (PDF 18–20), introduces a characteristic function, linearizes the nonlinear averaging constraint, rescales the fluctuation by the effective coupling, and eliminates one pivot bond \(b_0(c)\) per next-level bond. Its remaining vector \(B\) is unconstrained; the constrained field is \(CB\). The covariance is \((C^*\Delta^{(k)}C)^{-1}\). Here \(C\) is an extension map, not the covariance. The gauge fixing is exponential; p.267 explicitly changes the delta gauge of the older propagator construction.

For the module below use one positively oriented independent bond once, with \(D=\dim_{\mathbb R}\mathfrak g\) real coordinates. Coordinates on eliminated bonds are not additional Gaussian variables. All distances are in the current unit lattice. Fixed \(L,M,G\) give a fixed upper bound on coordinates per \(LM\)-cell, even though the number of cells changes with volume and scale. A safe bond bound is \(n_0=2d(LM)^d\), with a fixed convention assigning boundary bonds to one cell.

### 2.2 What is actually asserted about covariance

CMP99b §E, pp.427–428, (3.155)–(3.158) (PDF 39–40), constructs the delta-axial-gauge reduced covariance. The paragraph following (3.158) states a positive lower bound \(\gamma_0\) for its precision, independent of \(k,U\), under (3.35)–(3.36) and small \(M\alpha_0\), and uniform exponential precision decay. Theorem 3.15, p.432, (3.187) (PDF 44), gives covariance decay with \(B_0,\delta_0\) depending only on \(d,L\), and a convergent walk expansion.

The physical current in that paper is \(J(U)\), defined by (3.11), p.392. Theorem 3.12, p.423, assumes the regularity of \(U\), including (3.36). It is not by its statement a theorem for arbitrary independent \(J\).

CMP116 pp.15–17 compares complex decoupled operators with a real reference: (2.16) controls kernel errors, (2.17) determinant costs, and (2.23)–(2.25) quadratic absorption, requiring \(\alpha_5\|C^{(k)}(Z_0,0)\|<1/2\). It does not explicitly state global bounds \(\operatorname{Re}C(s)\ge cI,\ \|C(s)\|\le C_*\) for every complex walk parameter.

Consequently, one must not infer that pair merely from exponential covariance decay. The primary proof supplies a more structured two-integral domination, conditional covariance plus exterior whitened field. A direct covariance-forest proof may instead use the simpler hypotheses of §7, after they have been checked for the actual full Gaussian.

### 2.3 Where the cutoff-only activities occur

The cutoff-only sector is \(D_{\rm int}=Y_0=\varnothing,\ P\ne\varnothing\) in CMP116 (2.1)–(2.4), p.12; \(P\) lies inside \(Z_0\). Conditioning, exterior whitening and walk localization are (2.5)–(2.10), pp.12–14. The empty-interaction contribution survives in (2.33), p.19. Bounds (2.38), (2.41), pp.20–21, are the targets.

CMP119 pp.272–273, (3.28)–(3.32), separates the Gaussian cutoff logarithm from interaction terms. The whole-lattice setting is specified near (3.39), p.274; (3.41)–(3.42), p.275, point the terms. This pass concerns that whole-lattice cutoff contribution. It does not extend the argument across large-field boundaries.

The retrieved PDF OCR loses some equation right-hand sides. No missing numerical coefficient is being inferred from OCR.

## 3. Proved: uniform complex Gaussian bad-bond bounds

All matrices in this section are finite dimensional. Transpose symmetry \(C=C^T\) is the symmetry needed for the bilinear Gaussian density. Hermitian part means \(\operatorname{Re}C=(C+C^*)/2\); the two operations must not be confused.

### Lemma 3.1: covariance form

Suppose \(C=C^T\), \(\operatorname{Re}C\ge cI\), and \(\|C\|\le K\), where \(c,K>0\). Normalize the complex Gaussian density by the analytic determinant branch on the accretive cone. For distinct bonds \(P\), each with \(D\) real components, and measurable \(q_b\) satisfying
\[
 |q_b(x)|\le {\bf1}_{|x|\ge R},
\]
one has
\[
 \left|\int\prod_{b\in P}q_b(B_b)\,d\mu_C(B)\right|
 \le \theta(c,K,R)^{|P|},\qquad
 \theta(c,K,R)=2^{D/2}(K/c)^D
           \exp[-cR^2/(4K^2)].
 \tag{3.1}
\]

Proof. The integral is exactly the marginal Gaussian on the coordinates \(P\); its covariance \(C_P\) is the corresponding principal block. It inherits the two bounds. The identity
\[
 \operatorname{Re}C_P^{-1}
   =C_P^{-*}(\operatorname{Re}C_P)C_P^{-1}
   \ge(c/K^2)I
\]
and \(|\det C_P|\ge c^{D|P|}\) dominate the absolute density by \((K/c)^{D|P|}\) times an isotropic real Gaussian of variance \(K^2/c\). For that Gaussian, the event in question implies \(|B_P|^2\ge |P|R^2\). Markov's inequality at parameter \(c/(4K^2)\) bounds the event by \(2^{D|P|/2}e^{-c|P|R^2/(4K^2)}\). This proves (3.1). Marginalization and normalization follow first for positive real matrices, then by analytic continuation, or directly by block Gaussian integration. All integrals are absolutely convergent.

### Lemma 3.2: stronger precision form

Suppose the full precision \(A=A^T\) satisfies
\[
 \operatorname{Re}A\ge aI,\qquad \|A\|\le B.
 \tag{3.2}
\]
Then (3.1) improves to
\[
 \left|\int\prod_{b\in P}q_b\,d\mu_{A^{-1}}\right|
 \le \theta_A(R)^{|P|},\qquad
 \theta_A(R)=2^{D/2}(B/a)^D e^{-aR^2/4}.
 \tag{3.3}
\]

Proof. Let \(S=( (A^{-1})_{PP})^{-1}\) be the marginal precision. Splitting coordinates into \(P,Q\), it is the Schur complement \(A_{PP}-A_{PQ}A_{QQ}^{-1}A_{QP}\). For \(v=(x,-A_{QQ}^{-1}A_{QP}x)\), \(Av=(Sx,0)\), hence
\[
 \operatorname{Re}\langle x,Sx\rangle
 =\operatorname{Re}\langle v,Av\rangle\ge a\|x\|^2.
\]
Also \(\operatorname{Re}A^{-1}\ge aB^{-2}I\), so
\(\|S\|\le B^2/a\). In \(m=D|P|\) coordinates, the absolute marginal density is at most
\((B/a)^m\) times a real Gaussian of variance \(1/a\). The same Markov argument proves (3.3). The case \(Q=\varnothing\) needs no Schur complement.

The Gaussian constrained to redundant original bond coordinates can have zero covariance eigenvalues. Lemma 3.2 is applied after the pivot elimination. Small eigenvalues of a covariance are not an obstruction if the actual reduced precision also has a uniform upper bound. A covariance upper bound alone is insufficient for the complex absolute-density estimate.

## 4. Proved: exact cell regrouping

Let \(\mathcal B_i\) be disjoint sets of independent bonds, each of size at most \(n_0\). Put
\[
 f_i(B)=\prod_{b\in\mathcal B_i}
       {\bf1}_{|B_b|<R}-1.
\]
For a nonempty finite set of cells \(S\), define the exact cutoff moment
\[
 m_S(C)=\int\prod_{i\in S}f_i(B)\,d\mu_C(B).
\]
Under either tail lemma, with its corresponding \(\theta\),
\[
 |m_S(C)|\le \eta(R)^{|S|},\qquad
 \eta(R)=(1+\theta)^{n_0}-1
       \le n_0\theta e^{n_0\theta}.
 \tag{4.1}
\]

Proof. On one cell expand
\[
 f_i=\sum_{\varnothing\ne P_i\subset\mathcal B_i}
             (-1)^{|P_i|}\prod_{b\in P_i}{\bf1}_{|B_b|\ge R}.
\]
The bond sets for different cells are disjoint, so the tail lemma bounds each term by \(\theta^{\sum_i|P_i|}\). The finite sums factor into \(\prod_i[(1+\theta)^{|\mathcal B_i|}-1]\), yielding (4.1). This proof is valid for complex Gaussian measures; a probabilistic union bound applied to complex integrals would not be a valid replacement.

This is a small raw moment, not yet a connected polymer activity or a localized function of the background. Summing all subsets directly would reintroduce a volume cost. Connectedness and spatial summability require the cluster step.

For the numerical cutoff of the deposit,
\[
 R(g)=A_1(\log g^{-2})^{p_0},\qquad p_0>1/2,
\]
(4.1) gives \(\eta(g)\le C_0\exp[-c_0A_1^2(\log g^{-2})^{2p_0}]\) once \(\theta\le1\). Constants depend on \(d,L,M,G,a,B\), or \(c,K\), but not on scale, volume, coupling history, or the number of cells. Thus the cutoff contribution can be made smaller than \(C_1g(\log g^{-2})^{p_1}\) below a fixed coupling ceiling. This numerical comparison does not control interaction insertions on the larger real fluctuation support; the distinction \(P(g)\ne R(g)\) in running_coupling_research.md remains.

## 5. Proved: forest covariance stability

Partition all coordinates into cells. Let \(w=(w_{ij})\) be a real positive semidefinite matrix with \(w_{ii}=1\), and define
\[
 C(w)_{ij}=w_{ij}C_{ij}.
\]
If \(C=C^T,\ \operatorname{Re}C\ge cI,\ \|C\|\le K\), then
\[
 C(w)=C(w)^T,\qquad \operatorname{Re}C(w)\ge cI,\qquad
 \|C(w)\|\le K.
 \tag{5.1}
\]

Proof. Choose unit vectors \(u_i\) with \(w_{ij}=\langle u_i,u_j\rangle\), and let \(V(x_i)_i=(x_i\otimes u_i)_i\). Then \(V\) is an isometry and \(C(w)=V^*(C\otimes I)V\). This proves both operator inequalities. Real \(w\) preserves transpose symmetry. Entrywise exponential off-diagonal bounds also persist since \(|w_{ij}|\le1\).

For a forest with edge parameters in \([0,1]\), the interpolation matrix with entries equal to the minimum along the path, and zero between components, is positive semidefinite. Indeed it is the integral, over \(t\in[0,1]\), of the block matrix whose entries are one when the two vertices lie in the same component of the subforest retaining edges with parameter at least \(t\). Each such block matrix is positive semidefinite. Thus (3.1) and (4.1) hold uniformly throughout this interpolation.

This says nothing by itself about complex polydiscs of independently assigned walk parameters. Those are a different interpolation.

## 6. Proved: covariance sensitivity and conditional background localization

For a fixed set \(S\) of cells, \(m_S(C)\) depends only on the covariance restricted to their bond coordinates \(J_S\), and is holomorphic on the accretive covariance cone. Sharp real cutoffs do not obstruct this holomorphy: the integration domain is fixed and the Gaussian density is holomorphic with locally uniform integrable domination.

Let \(C_0,C_1\) be symmetric matrices on \(J_S\), both satisfying \(\operatorname{Re}C_j\ge cI,\ \|C_j\|\le K\). Set
\[
 \eta_+(R)=
   [1+\theta(c/2,K+c/2,R)]^{n_0}-1.
\]
Then
\[
 |m_S(C_1)-m_S(C_0)|
 \le {4\over c}\|C_1-C_0\|\,\eta_+(R)^{|S|}.
 \tag{6.1}
\]

Proof. Along the straight segment \(C_t\), perturb in a symmetric direction \(E\) of norm one. On \(|z|\le c/4\), \(C_t+zE\) remains in the bounds \(c/2,K+c/2\). Cauchy's derivative estimate, using (4.1), gives \(|Dm_S(C_t)[E]|\le4\eta_+^{|S|}/c\). Integrate the derivative along the segment. Zero difference is immediate.

Here is an explicit useful locality consequence. Suppose the source model supplies covariance approximants \(C^{[r]}\) on \(J_S\), depending only on the background/current within distance \(r\) of \(J_S\), with the same uniform \(c,K\), and
\[
 \|(C-C^{[r]})_{J_S}\|\le K_{\rm loc}e^{-\mu r}.
 \tag{6.2}
\]
Take integer radii \(r\ge r_0\), define
\[
 L_{r_0}=m_S(C^{[r_0]}),\qquad
 L_r=m_S(C^{[r]})-m_S(C^{[r-1]})\quad(r>r_0).
\]
Then \(m_S(C)=\sum_{r\ge r_0}L_r\), absolutely, and
\[
 |L_r|\le{4K_{\rm loc}(1+e^\mu)\over c}
           e^{-\mu r}\eta_+(R)^{|S|}\quad(r>r_0),
 \tag{6.3}
\]
while \(|L_{r_0}|\le\eta(R)^{|S|}\). Each term is genuinely a function of data in the indicated collar.

This is a concrete conditional localized bound, proved without differentiating the cutoff. Its localization assumption (6.2) is essential. Restricting a globally defined precision to a coordinate region does not automatically make its background dependence local. CMP99b Theorem 3.14, pp.426–427, supplies a physical-background comparison by cancellation of common walk terms; CMP116 uses exact walk localization. Matching (6.2), or an equivalent footprint expansion, on the independent-current domain remains part of the source interface.

A sufficient kernel form for (6.2), with uniform constants, is
\[
 |(C-C^{[r]})(b,b')|
 \le K_1e^{-\mu r}e^{-\nu d(b,b')}.
\]
Schur summation yields \(K_{\rm loc}=K_1\sup_b\sum_{b'}e^{-\nu d(b,b')}\). Color dimension can be included in the block-matrix norm. Thus no factor proportional to \(|S|\) is required.

## 7. Minimal remaining operator statement for the Gaussian module

For every level \(k\), whole-lattice finite torus, and admissible history, construct the exact independent-coordinate precision \(A_k(\xi)\) of the exponential-gauge Gaussian, where \(\xi\) is the normalized complex background/current and \(\|\xi\|<r_*\). Require constants independent of \(k\), torus, history and the desired remainder tolerance:

**G1 — identification and fixed domain.** \(A_k(\xi)=A_k(\xi)^T\) is holomorphic on the fixed ball and equals the actual Gaussian precision at physical data. The cutoff is the fixed product of bond conditions on these coordinates. The extension from physical \(J(U)\) to independent \(J\) must be specified.

**G2 — uniform ellipticity and upper bound.**
\[
 \operatorname{Re}A_k(\xi)\ge aI,\qquad \|A_k(\xi)\|\le B.
\]
It suffices to prove a real-base lower bound \(A_k(0)\ge2aI\), a fixed-domain upper bound, and \(\|A_k(\xi)-A_k(0)\|\le a\). Small-current/background perturbation in a weighted Schur algebra is one possible proof. This is a proposed sufficient criterion, not a source identification already completed.

**G3 — summable spatial covariance.** For \(C_k=A_k^{-1}\), require
\[
 \sup_b\sum_{b'}e^{\mu d(b,b')}\|C_k(\xi;b,b')\|\le K_\mu.
\]
This is the direct input for connecting separated cells in a covariance forest expansion. G2 yields the needed accretivity \(c=a/B^2\) and norm \(K=1/a\), but does not alone prove G3.

**G4 — background locality.** Require local approximants as in (6.2), or an absolutely summable footprint expansion with equivalent bounds. This is needed for coefficient extraction from local activities, not for the finite Gaussian integral alone.

**G5 — symmetry and compatibility.** The chosen extension and localizations preserve the exact physical Gaussian at \(\xi\) corresponding to physical fields, and preserve the gauge/lattice symmetries required of the final coefficients. Agreement of an arbitrary analytic extension only at the trivial field is insufficient.

These conditions are intentionally narrower than all bounds on nonlinear minimizers or all large-field operator families. They suffice as operator inputs for the cutoff-only Gaussian cluster module, together with the separate connected-cluster theorem. For that module one can use the stable real forest interpolation of §5 instead of assuming accretivity throughout the primary complex walk polydisc.

## 8. Deposit status and specific unchecked bridges

All following line numbers refer to the current raw I file.

* 4333–4344 defines pivot-removed bonds; 4812–4843 defines the compressed precision and its inverse.
* 5500–5517 explicitly distinguishes the primary tied-current operator theorem from bounds at free current, and identifies the walk/one-family hypotheses.
* 5910–6077 gives a conditional proof of accretivity of the precision on a complex polydisc. Its conclusions are useful: \(\operatorname{Re}A\ge\gamma_*\), with an upper walk norm \(\mathsf B\), both scale independent. Its form-walk and positivity assumptions remain premises.
* 7171–7298 proves, under the stated localized walk/coercivity assumptions, \(C^{(k)}(Z_0)^{W'}=T_{W'}^{-1}\), \(\|C^{(k)}(Z_0)^{W'}\|\le8/(5\gamma_*)\), and \(\operatorname{Re}C^{(k)}(Z_0)^{W'}\ge5\gamma_*/(8\mathsf B^2)\). These precisely fit Lemma 3.1 when the localized covariance is transpose symmetric. A generic truncated operator series need not retain that symmetry; the subsequent symmetric-base discussion is relevant.
* 13680 onward constructs free-current operators by Neumann series and local current insertions. It expressly assumes the uniform inverse-covariance walk statement and analytic derivative bounds for averaging maps, cited there as printed without proof. This is additional deposited work, not absent work; it has not been completely independently verified in this pass.
* CMP99b's axial reduced space removes axial-tree bonds as well as pivots. CMP109's exponential gauge retains gauge variables with a Gaussian penalty. Thus the two covariance matrices cannot be identified just by renaming their symbols. A correct comparison would parameterize the block gauge variables and physical axial variables together, with uniformly controlled forward/inverse linear maps (depending on fixed \(L\)), and prove the corresponding quadratic form identity, including off-diagonal free-current terms. No such complete quantitative identification is claimed here.

The remaining obstruction is therefore a precise operator/domain identification and uniform estimate, not a demonstrated failure of the modified cutoff or a defect in the elementary Gaussian tail argument.

## 9. Proved: conditional axial-to-exponential coordinate bridge

This lemma isolates the finite-dimensional geometry from the unverified quadratic form identity.

Partition the unit lattice into \(L\)-blocks, each with a rooted spanning tree of at most \(n_L\) vertices and maximum root-path length \(\ell_L\). Let \(U\) be a real compact-group background. Parallel transports in the adjoint representation are orthogonal in an invariant Lie algebra norm. For a bond field \(B\), solve on each tree
\[
 B-D_U\lambda=0,\qquad \lambda(\text{root})=0.
\]
There is a unique solution: integrate successively along the tree. Set \(B_{\rm ax}=B-D_U\lambda\). Along a tree path, Cauchy–Schwarz gives
\[
 |\lambda(x)|^2\le\ell_L\sum_{e\text{ on path to }x}|B(e)|^2,
 \qquad
 \|\lambda\|\le H_L\|B\|,\quad H_L=\sqrt{n_L\ell_L}.
 \tag{9.1}
\]
Summing the edge bound
\(|D_U\lambda(e)|^2\le2|\lambda(e_-)|^2+2|\lambda(e_+)|^2\)
gives \(\|D_U\lambda\|\le2\sqrt d\|\lambda\|\). Hence the map
\(T:B\mapsto(B_{\rm ax},\lambda)\) and its inverse \(S:(A,\lambda)\mapsto A+D_U\lambda\) satisfy
\[
 \|T\|\le t_L:=\sqrt{(1+2\sqrt d H_L)^2+H_L^2},
 \qquad
 \|S\|\le s_d:=\sqrt{1+4d}.
 \tag{9.2}
\]
Both are independent of volume and RG level.

If the averaging constraint obeys \(QD_U\lambda=0\) for root-zero \(\lambda\), the map restricts to an isomorphism
\[
 \ker Q\longleftrightarrow
 \{A:\ QA=0,\ A|_{\rm tree}=0\}\oplus
 \{\lambda:\lambda|_{\rm roots}=0\}.
 \tag{9.3}
\]
The necessity of this Ward identity is explicit; it is not deduced from (9.1).

Suppose, on these variables, the actual exponential-gauge quadratic form is
\[
 q_{\exp}(B)=q_{\rm ax}(B_{\rm ax})+\tau\|\lambda\|^2+E(B),
 \quad
 \gamma\|A\|^2\le q_{\rm ax}(A)\le B_{\rm ax}\|A\|^2,
 \quad |E(B)|\le\varepsilon\|B\|^2,
 \tag{9.4}
\]
where \(\tau,\gamma>0\). Then
\[
 q_{\exp}(B)\ge
 \left({\min(\gamma,\tau)\over1+4d}-\varepsilon\right)\|B\|^2,
 \qquad
 |q_{\exp}(B)|\le
 [\max(B_{\rm ax},\tau)t_L^2+\varepsilon]\|B\|^2.
 \tag{9.5}
\]
Indeed (9.2) gives \(\|TB\|\ge\|B\|/s_d\); apply (9.4) and its upper bound. If pivot elimination is \(B=\mathcal C b\), \(\mathcal C\) contains the identity rows on retained bonds and \(\|\mathcal C\|\le K_L\), then the reduced precision inherits the same positive lower bound and the upper bound multiplied by \(K_L^2\). The lower bound follows from \(\|\mathcal C b\|\ge\|b\|\).

At small complex perturbations one may use a real reference and bound the precision difference in operator norm; positivity is not asserted for complex transport coefficients by themselves. Fixed tree path lengths make the coordinate-map perturbation constants uniform in scale.

For the actual source match, prove (9.3), identify the gauge quadratic penalty in (9.4), control the physical-current and free-current correction \(E\), and bound the pivot extension \(K_L\). The lemma shows exactly what such a proof would deliver. No complete verification of those identities for the deposited off-diagonal current construction is claimed here.
