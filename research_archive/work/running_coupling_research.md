# Running coupling: isolate cutoff transfer from coefficient extraction

Research note, 16 October 2026. This note proves elementary reductions, not the deposited Wilson RG induction. The repository was not modified.

## 1. Finding and exact dependency

The strongest defensible conclusion is a logical relocation. The fourth hypothesis of the deposited lemma 4.2:lem-unmarked already assumes the small remainder estimate that the incomplete paragraph then tries to transfer. Once that estimate holds on a fixed normalized complex-background neighborhood, with the uniform free-response bound, coefficient extraction is a bounded linear operation. That implication is proved in §3. The unresolved model-specific work belongs in the modified-cutoff part of 4.3:thm-small-field-step, or a separate theorem supplying that part.

References to raw I mean work/Yang--Mills-LLM-experiment/theorem_0_complete_account_raw_I.tex, at current checkout line numbers.

| Deposit location | What it supplies |
|---|---|
| 3780–3837, 4.2:def-increment | The increment is the weighted second variation of the whole-lattice complete regular action. The split into Gaussian normalizer, unmarked remainder and marked remainder is linear. |
| 3901–4014, 4.2:lem-one-loop | The Gaussian finite-part assertion and an outline using determinant comparison. Proving the cutoff lemma does not prove those comparisons. |
| 4031–4068, 4.2:lem-unmarked | Assumes the actual unmarked remainder obeys CMP116 (2.41), including its small factor, then concludes a uniform small correction to the Gaussian increment. |
| 4072–4136 | Marks (*) incomplete, invokes CMP116 Lemma 3 with the CMP119 cutoff, then normalized Cauchy extraction. These are distinct operations. |
| 4166–4209, 4.3:thm-small-field-step | States the altered-cutoff remainder bound, with numerical fluctuation-box and cutoff-radius conditions, and refers to the published argument. It is not a second detailed transfer proof. |
| 53410–53549, §4.17 transfer theorem | Transfers CMP116 Lemmas 1–2 on potential localization, under additional geometry and printed-input hypotheses. It does not state/prove the final unmarked remainder bound with the required fixed-radius, epsilon-independent constant. |
| 58765–58995, 4.38:prf-polarisation-limit | Detailed Cauchy/localization proof at fixed scale. Its raw response constant may depend on scale; it does not independently establish the uniform normalized ratio. |
| 56419–56468, 4.19:prop-clause-zero | Assumes the increment estimates, then proves the first-passage trajectory. Its telescoping is not the unfinished cutoff step. |
| Raw I 166617; raw III 111368 | Final inventories still call the unmarked lemma incomplete. Searches found no independently completed replacement in the deposited tex files. This does not assert nonexistence elsewhere. |

The target is
\[
 \sup_{l\ge1}\sup_{\text{admitted histories through }l-1}
 |\beta_l^{\mathfrak A}-\beta_l^0|
 \le C_{\rm ext} A_{\rm rem}\varepsilon_1^{\rm I},
 \tag{1.1}
\]
with both constants fixed before \(\varepsilon_1^{\rm I}\). A bound at each fixed scale or coupling is insufficient.

## 2. Source check and the three radii

Original articles accessed through ordinary public PDF links:

* [CMP109](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf), T. Bałaban, *Renormalization group approach to lattice gauge field theories I*, Commun. Math. Phys. **109** (1987), 249–301, DOI 10.1007/BF01215223.
* [CMP116](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-4penm4k7hc.pdf), Part II, Commun. Math. Phys. **116** (1988), 1–22, DOI 10.1007/BF01239022.
* [CMP119](https://scispace.com/pdf/convergent-renormalization-expansions-for-lattice-gauge-29jyexd38e.pdf), *Convergent renormalization expansions for lattice gauge theories*, Commun. Math. Phys. **119** (1988), 243–285, DOI 10.1007/BF01217741.

CMP116 pp.20–21 proves the activity estimate (2.38), resums it to the remainder bound (2.41), then adds the Gaussian normalizer. Its p.15 argument supplies background analyticity. Small interaction insertions and cutoff-only contributions are separately controlled in (2.26)–(2.34), pp.17–19; the empty interaction family is not automatically zero.

CMP119 (3.43), journal p.276, replaces the domain for localization terms crossing the small-field boundary. The preceding paragraph retains the earlier hypotheses for interior terms. The whole-lattice unmarked run has no boundary-crossing terms. Its logarithm and cutoff contribution occur in (3.28)–(3.32), pp.272–273; the final expansion is discussed on pp.277–278. Thus this target is the changed real cutoff with suitable fixed complex-background control, not the entire layered-boundary transfer.

The web extraction loses equation right-hand sides. No missing numerical constant has been reconstructed from OCR guesses.

Distinguish:

1. The real fluctuation cutoff
   \[
   R(g)=\delta(g)/g=(A_1/A_0)p_0(g)
       =A_1(\log g^{-2})^{p_0}.
   \tag{2.1}
   \]
2. The auxiliary complex fluctuation box of radius \(P(g)=C_1^{\rm fl}p_1(g)\). The deposit requires \(gP(g)\le\varepsilon_1^{\rm I}\).
3. The fixed background/current radii \(\alpha_0,\alpha_1\) of CMP109/116, in appropriately scaled norms, chosen before \(\varepsilon_1^{\rm I}\).

The running CMP119 radii, such as \(C_0g(\log g^{-2})^q\), cannot silently replace item 3 in Cauchy extraction.

There is a further containment check in the deposited notation. Raw I 1355–1363 chooses \(p_1<p_0\), while 4166–4178 identifies the two fluctuation radii above with those exponents. Thus \(R(g)/P(g)=(A_1/C_1^{\rm fl})(\log g^{-2})^{p_0-p_1}\) is unbounded. The boundary-only box must not be silently treated as a complex neighborhood of the entire real cutoff support. If a whole-lattice estimate needs \(gR(g)\le\varepsilon_1^{\rm I}\), that is an additional explicit ceiling: choosing \(\varepsilon_1^{\rm I}=gP(g)\) as \(g\downarrow0\) shows it does not follow from the printed \(gP(g)\) condition alone. Such an extra ceiling is feasible, because \(gR(g)\to0\); this is a bookkeeping/interface correction, not a demonstrated failure of the published construction.

CMP109 p.259, Theorem 2 and the following paragraph, announces a perturbative running-coupling proof to be supplied separately. CMP122-II pp.355–356 calls it unpublished at that time. These historical statements do not settle the status of every later result. The deposit expressly selects another route, whose own estimates must be checked.

## 3. Proved: uniform coefficient extraction

Fix dimension \(d\), block size \(M\), and localization families \(\mathcal D_l\), using one fixed lattice norm. Suppose uniformly in \(l\),
\[
 \operatorname{diam}X\le Md_l(X)+2c_dM,\qquad
 \sup_z\sum_{X\ni z}e^{-\kappa_0d_l(X)}\le K_0.
 \tag{3.1}
\]
The constant \(c_d\) accounts for the unit-cube diameter. Let \(\kappa>\kappa_0\).

For \(X,z\in X\), let \(R_{l,X,z}\) be holomorphic on the complex norm ball \(\|\xi\|_{l,X}<r\), centered at the trivial background/current, and suppose
\[
 \sup_{\|\xi\|_{l,X}<r}|R_{l,X,z}(\xi)|
       \le A\varepsilon e^{-\kappa d_l(X)}.
 \tag{3.2}
\]
For a unit block-bond insertion \(x\), suppose its free response obeys
\[
 \|h_{l,x}|_X\|_{l,X}\le H e^{-m\operatorname{dist}(x,X)}.
 \tag{3.3}
\]
Every constant is independent of \(l,\varepsilon\) and the admitted history. The norm includes every background/current component read by \(R\); it may contain scale factors.

Define
\[
 \Pi_l(x,y,z)=\sum_{X\ni z}D^2R_{l,X,z}(0)[h_{l,x},h_{l,y}].
 \tag{3.4}
\]
Set
\[
 a=\min\{m/2,(\kappa-\kappa_0)/(4M)\},\quad
 C_{\rm pt}=4AH^2r^{-2}K_0e^{4c_dMa}.
 \tag{3.5}
\]
Then
\[
 |\Pi_l(x,y,z)|\le C_{\rm pt}\varepsilon
 e^{-a(|x-z|+|y-z|)}.
 \tag{3.6}
\]
With \(\Pi_l(x,y)=\sum_z\Pi_l(x,y,z)\),
\[
 \sum_u|u|^2|\Pi_l(0,u)|
 \le4C_{\rm pt}S_0(a)S_2(a)\varepsilon,\qquad
 S_j(a)=\sum_{v\in\mathbb Z^d}|v|^je^{-a|v|}.
 \tag{3.7}
\]
For \(S_0\), take \(|v|^0=1\). Fixed orientation/color multiplicities can be absorbed into the constants.

**Proof.** Two-variable Cauchy, with radii approaching \(r/(2\|h_x\|)\) and \(r/(2\|h_y\|)\), gives
\[
 |D^2R(0)[h_x,h_y]|
 \le4AH^2r^{-2}\varepsilon
 e^{-\kappa d_l(X)-m(d_x+d_y)}.
 \tag{3.8}
\]
Zero directions are immediate. For \(z\in X\),
\[
 a(|x-z|+|y-z|)
 \le a(d_x+d_y)+2Ma\,d_l(X)+4c_dMa.
\]
The choice of \(a\) leaves at least \(\kappa_0d_l(X)\) in the polymer exponent. Sum (3.8) using (3.1) to get (3.6). Put \(v=u-z\), use \(|u|^2\le2|z|^2+2|v|^2\), and apply Tonelli to get \(4S_0S_2\). All these series converge. \(\square\)

This bounds \(\sum_u u_\mu u_\nu\Pi_l(0,u)\). Linearity identifies it with the remainder correction once the actual family is identified with \(R\).

If only the unpointed family \(R_{l,X}\) has (3.2), distribute it over finitely many anchors in \(X\) using field-independent nonnegative weights of sum one. The same proof applies. To transfer this to the deposited coefficient, identify the unpointed total with its native pointed total, initially in finite volume. Do not assume a native pinned bound merely from an unpointed source bound.

At the identity, a gauge-invariant analytic function for a semisimple group has zero first derivative in its adjoint-valued slots: the derivative would be an invariant linear functional on the Lie algebra. Therefore the Hessian of its composition with the minimal configuration only uses the first response, as in raw I 58839ff. The source-specific chart and covariance hypotheses must still hold.

**Logical consequence.** Given the fourth hypothesis of 4.2:lem-unmarked on the correct fixed domain and its normalized free-response bound, coefficient extraction is a complete conditional corollary. Cutoff comparison does not belong inside that corollary.

**Necessary distinction.** The functions \(R_l(z)=\varepsilon(z/r_l)^2\) satisfy \(|R_l|\le\varepsilon\) on \(|z|<r_l\), but \(R_l''(0)=2\varepsilon/r_l^2\). Thus merely positive scale-dependent radii cannot imply uniform coefficient control. This is a counterexample to an abstract inference, not to the actual activities.

## 4. Proved: Gaussian cutoff tails without independence

Let \((X_b)_{b\in B}\) be centered real Gaussian, with \(D\) real components per block and covariance operator norm at most \(\sigma^2\). It need not be independent or nondegenerate. For finite \(S\subset B\),
\[
 \mathbb P\{|X_b|\ge R\ \forall b\in S\}
 \le\left(2^{D/2}e^{-R^2/(4\sigma^2)}\right)^{|S|}.
 \tag{4.1}
\]

**Proof.** The event implies \(|X_S|^2\ge R^2|S|\). The marginal covariance satisfies \(C_S\le\sigma^2I\). For \(t=1/(4\sigma^2)\),
\[
 \mathbb E e^{t|X_S|^2}
 =\det(1-2tC_S)^{-1/2}\le2^{D|S|/2}.
\]
Exponential Markov proves (4.1). Singular covariances follow by diagonalization. \(\square\)

A complex version is also available. Suppose a complex symmetric covariance on independent integration variables satisfies
\[
 \operatorname{Re}C\ge cI,\qquad \|C\|\le C_*.
 \tag{4.2}
\]
Each marginal inherits these inequalities. Then
\[
 \operatorname{Re}(C_S^{-1})\ge cC_*^{-2}I,\qquad
 |\det C_S|\ge c^{D|S|}.
\]
Indeed \(\operatorname{Re}C_S^{-1}=C_S^{-*}(\operatorname{Re}C_S)C_S^{-1}\), and every singular value is at least \(c\).
The normalized complex Gaussian marginal is dominated by \((C_*/c)^{D|S|}\) times a real isotropic Gaussian of variance \(C_*^2/c\). Thus
\[
 \left|\int\prod_{b\in S}q_b(X_b)\,d\mu_C(X)\right|
 \le\left[(C_*/c)^D2^{D/2}
 e^{-cR^2/(4C_*^2)}\right]^{|S|}
 \tag{4.3}
\]
if \(|q_b|\le1_{\{|X_b|\ge R\}}\).
The Gaussian marginal formula follows by direct Gaussian integration (equivalently holomorphic continuation from real positive covariances). The Gaussian domination just given justifies the integrations. For a constrained Gaussian, first pass to independent coordinates and establish (4.2) there; this is not automatic on redundant coordinates.

These estimates are independent of the total number of variables. A global union bound instead introduces a volume factor and does not by itself control a localized effective action.

## 5. Proved: logarithmic radii respect the parameter order

Let \(p_0>1/2\), \(p_1\ge0\), \(A_1,C_1,c,D_0>0\) be fixed independently of \(\varepsilon\). Put \(t=\log g^{-2}\). There is \(T\), depending only on these fixed quantities, for which
\[
 D_0e^{-cA_1^2t^{2p_0}}\le C_1e^{-t/2}t^{p_1}
 \quad(t\ge T).
 \tag{5.1}
\]
Choose \(T\ge1\) so that
\[
 cA_1^2t^{2p_0}\ge t,\qquad
 cA_1^2t^{2p_0}\ge2[\log(D_0/C_1)]_+.
\]
This is possible because \(2p_0>1\). Averaging gives the needed \(t/2+\log(D_0/C_1)\) bound; \(t^{p_1}\ge1\) completes the proof.

Therefore, after a fixed additional ceiling \(g\le e^{-T/2}\), the condition \(gP(g)\le\varepsilon_1^{\rm I}\) also pays a tail \(D_0e^{-cR(g)^2}\). The deposit's exponents exceed \(1/2\); see raw I 29119–29128. Another fixed ceiling enforces \(R(g)\ge R_{\min}(M,\kappa)\).

There is no numerical conflict between the cutoff requirements and an epsilon-independent multiplicative constant. The coupling ceiling can be chosen after epsilon. This does not prove the actual localized activities have the assumed Gaussian tail majorant.

## 6. Proved: analytic activity comparison

Let \(\mathcal A,\mathcal E\) be complex Banach spaces of local activities and effective actions. Suppose a cluster map \(\mathcal T\) is holomorphic and bounded by \(M_{\mathcal T}\) on the open \(\eta\)-neighborhood of the real segment from \(a_0\) to \(a_1\). Then
\[
 \|\mathcal T(a_1)-\mathcal T(a_0)\|_{\mathcal E}
 \le M_{\mathcal T}\eta^{-1}\|a_1-a_0\|_{\mathcal A}.
 \tag{6.1}
\]
For a unit direction, Banach-valued Cauchy bounds the derivative by \(M_{\mathcal T}/\eta\). Integrate along the segment. Scalar duality proves the Banach-valued Cauchy estimate.

If two cutoffs give activities on the same fixed background domain with
\[
 \|a_{R_1}-a_{R_0}\|_{\mathcal A}
 \le A_{\rm tail}e^{-c\min(R_0,R_1)^2},
 \tag{6.2}
\]
then (6.1) and §3 control the corresponding coefficient difference by this tail, uniformly. This interpolates already-defined activities; it does not differentiate a sharp indicator or assume a full finite-volume partition function has a volume-independent lower bound.

This is a precise repair option, conditional on (6.2), common domains and a uniform cluster-map margin. A direct rerun of CMP116 may be shorter: retain its potential estimates on a complex fluctuation domain containing the actual real integration support, prove cutoff-only activity estimates using §4, then repeat its resummation. The containment must be checked as explained in §2; the boundary-only \(P(g)\) box is not automatically sufficient. Either route must retain locality and the complex decoupling polydiscs.

## 7. Precise model-specific interface still open

Let \(R^{119}_{l,X}\) be the actual unmarked, non-Gaussian whole-lattice remainder at cutoff \(R(g_{l-1})\). A sufficient theorem is:

There are \(A_{\rm rem},r,m,H,\kappa,\kappa_0,K_0,M\), fixed before \(\varepsilon_1^{\rm I}\), such that for every sufficiently small \(\varepsilon_1^{\rm I}\) there is \(\gamma>0\) for which, for every scale and every admitted history with \(0<g_i\le\gamma\):

* the output exists and agrees with the localized action defining the actual increment;
* on a fixed normalized background/current ball of radius \(r\), its remainder satisfies (3.2), or an equivalent unpointed weighted-polymer estimate;
* the free response obeys (3.3) in the same norm, including current components;
* the restrictions, covariance and finite-volume compatibility identify the result with the declared whole-lattice coefficient.

For a comparison proof, the missing quantitative sublemma is (6.2) for the actual localized activities, uniformly on that domain and its decoupling polydiscs. For a direct proof, it is the corresponding locality-sensitive activity bound before final resummation. Sections 4–5 pay the numerical tail, not these source identifications.

The §4.17 theorem and subsequent path-length bounds are relevant upstream ingredients, but neither a response estimate by itself nor a running shrinking domain supplies the required fixed-background remainder bound. Conversely, the entire global layered-source problem is not a necessary antecedent of this particular whole-lattice calculation.

## 8. Consequence if that interface is proved

Accept separately
\[
 \sum_{l=i+1}^j\beta_l^0\ge c_0(j-i)-2c_2,\qquad
 |\beta_l^{\mathfrak R}|\le\bar\varsigma.
\]
Choose epsilon after the extraction constant so that
\(C_{\rm ext}A_{\rm rem}\varepsilon_1^{\rm I}\le c_0/2\), and take
\(\bar\varsigma\le c_0/4\). Then the actual recursion satisfies
\[
 (c_0/2-\bar\varsigma)(j-i)-2c_2
 \le x_i-x_j\le(C_\beta+\bar\varsigma)(j-i),\qquad x_l=g_l^{-2}.
\]
This is the averaged positive drift used in the deposited first-passage construction; individual increments need not be positive. The present note settles conditional extraction, Gaussian tail bounds, numerical parameter compatibility, and an abstract comparison reduction. Actual modified-cutoff RG source matching and the separate Gaussian finite-part input remain unverified here.
