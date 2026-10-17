# Restricted complex sources: response estimates and dependency audit

Research note, 16 October 2026. This is a read-only audit of the deposited raw account at commit `e392ef45013a581664bab76b90867170b30fe10e`, together with new elementary conditional reductions. It does **not** prove the Wilson-model source bound. Unposted companion proofs have not been assessed. All raw line references below are to `theorem_0_complete_account_raw_II.tex` unless stated otherwise.

**Route correction from the follow-up audit:** Sections 3–7 originally promoted the localized three-link reading of Raw II §5.6 to the next obstruction of the main source induction. That inference is withdrawn. Raw I `4.21:rem-global-chain` explicitly excludes that reading in favor of four global carriers. The actual induction consumes the global layers and their containment. Section 9 gives the corrected dependency path, the remaining reconciliation issue between the two descriptions, and the recovered current-forcing identity. The quantitative estimates in §§4 and 8 remain conditional results; they are not a verification of the global layer theorem.

## 1. What actually supplies the source bound

The objects called (L), (A), (B), (S), (F) around lines 60725–60855 are consumers of the correlation theorem, not a separate source-stability proof. Their producer is Theorem `5.1:thm-correlation-theorem`, lines 2791–2979, particularly clause (iii): the entire sourced RG density has the induction format, local analytic terms, and the enlarged activity bounds. The last-lattice argument at lines 59645–59855 then converts that format into

\[
 |e^{-\mathcal E(w)} Z(w)|\le e^{E_+^\sharp V},
 \qquad Z(0)\ge e^{-C_{\rm low}V},
 \qquad \mathcal E(0)=0,
\]

where \(V\) is the number of **last-lattice** sites. The counterterm is formed at lines 59694–59725 from the values of the local E- and R-terms at the trivial field, one-bond Haar-normalizer terms included, subtracting their zero-source values.

The bare density here is already vacuum normalized: lines 737–745 define

\[
 \rho_0^w=\exp[-A(x_0-w,U)-E],
\]

with a source-independent additive constant \(E\). Thus the simultaneous statements \(\mathcal E(0)=0\) and \(Z(0)\ge e^{-C V}\) are not a contradiction involving the unnormalized bare Haar integral. Any new proof must preserve this normalization. The precise uniform choice of \(E\) remains part of the RG input.

This theorem is different from the later **source lemma** `8.21:lem-source`, lines 145173–145219. That lemma decomposes the conditional expectation/annealed shadow of a smeared observable into small-field, live, and far pieces for the *lower two-point witness*. Its outstanding proof does not identify the first obstruction to the main correlation upper bound. Conversely, proving the main upper bound would not prove that witness decomposition or its lower estimate.

## 2. The reflected source class really is smaller, but the geometry stays

Use a fixed physical coarse spacing \(h\), and measure lengths in its units. Let a real Lipschitz \(f\) be supported in one reflection cell, with a fixed positive face buffer. Write

\[
 \nu=\|f\|_\sharp:=\max\{\|f\|_\infty,40M\operatorname{Lip}f\}.
\]

Here \(M\) is the fixed RG block parameter, not the number of reflection cells. In the unit-torus coordinates of the raw account the same norm is \(\max(\|f\|_\infty,\operatorname{Lip}f/(\lambda_*N))\), with \(\lambda_*=(40M)^{-1}\): lines 737–756.

Let \(F_e\) be the copy of \(f\) in every reflection cell, without coefficient conjugation, and let \(F_o\) have the sign of the cell-reflection parity. Then

\[
 \|F_e\|_\sharp,\|F_o\|_\sharp\le\nu,
 \qquad
 (zf)^{\rm ch}=(\Re z)F_e+i(\Im z)F_o.
 \tag{2.1}
\]

**Proof of the norm assertion.** Reflections preserve the Lipschitz seminorm. The original function vanishes in a face neighbourhood. Along a straight segment crossing cells, sum its variation on the portions within individual cells; values are zero at the intervening faces. Each portion costs at most \(\operatorname{Lip}(f)\) times its length. This applies equally to alternating signs. The torus version follows by taking a shortest geodesic. The sup norm is unchanged. No number of cells enters.

Consequently the restricted two-profile family

\[
 W_{u,v}=uF_e+vF_o,
 \qquad (|u|+|v|)\nu<r,
 \tag{2.2}
\]

lies in the admitted weight class at the fixed stopping scale. In particular the chessboard source is admissible whenever \(|z|\nu<r/\sqrt2\). The nested classes of lines 2722–2787 then put it in every earlier class. This establishes domain membership without using the correlation theorem. It does **not** establish the uniform source bound on that domain.

There are two different sets of complex variables:

1. The one or two physical source coefficients in (2.1)–(2.2).
2. The many auxiliary decoupling parameters \(s(\Delta)\), introduced to localize every RG term.

Reducing the first set does not reduce the second. The source-free scaffold, configurations, Gaussian measures, and decoupling variables are explicitly independent of the source in the proposed induction: lines 2128–2133 and 15357–15395. A reflected source also does not forbid a large-field component from intersecting its support. Hence it does not remove the large-field localization operation from that induction.

## 3. The first concrete analytic input that is not discharged

The generic proposition `5.6:prop-polydisc-holomorphy`, lines 46131–46218, asks for

\[
 F_t(\sigma;d)=t\bigl(\mathsf R(\sigma;d)\bigr)
 \quad\hbox{holomorphic and}\quad
 |F_t|\le\mathfrak b_t
 \quad\text{for every }|\sigma_v|<e^{\kappa_1}.
 \tag{3.1}
\]

Its proof is explicitly outstanding. The essential task is quantitative containment of the substituted fields in the term's actual analytic domain; finite-lattice entire dependence on the physical source does not supply it.

The raw account does distinguish a case already covered by an elementary composition argument. Theorem `5.6:thm-full-polydisc`, lines 47179–47300, and Corollary `5.6:cor-weight-hypothesis`, lines 47603–47718, treat the ordinary fluctuation/cluster step, site (T). They assume the localized-field estimate from CMP 116, the term's analytic domain, and the response membership radius. Their conclusion is a correct consumer of those hypotheses. It is not the general proposition (3.1).

The scope remark at lines 47719–47746 explicitly says that site (L), inside the large-field operation \(\mathbf R_k\), is different. It composes **three** localization maps. Definition `5.6:def-link-readings`, lines 48143–48320, assumes for each \(i=4,3,2\):

\[
 (\sigma^{(i)},\xi,\psi)\longmapsto
 H^{(i)}(\sigma^{(i)};\xi,\psi)
 \quad\hbox{jointly holomorphic},
\]
\[
 \|H^{(i)}(\sigma^{(i)};\xi,\psi)\|
 \le C e^{16\kappa_1}\|\xi\|,
 \qquad |\sigma^{(i)}_v|\le e^{\kappa_1},
 \tag{3.2}
\]

uniformly in the admissible background \(\psi\), **and** that every output belongs to the next map's argument domain. The functions are the localized versions of CMP 122-II (1.63)–(1.64), (1.62)/(1.57), and (1.61)/(1.51),(1.54). These three readings are expressly hypotheses. Theorem `5.6:thm-link-holomorphy` at line 49117 proves their compositional consequence.

This is a precise missing local estimate for the reading in §5.6. Its necessity for the active global-carrier source proof was not established: see the correction in §9. Its source-free nature means that restricting to (2.2) does not prove it. Conversely, once maps and their domains are controlled, appending two passive complex source coordinates to already jointly holomorphic potentials creates no new analytic difficulty: composition, differentiation, and finite contour integration preserve joint holomorphy under uniform majorants.

There is also an independently stated antecedent to the main correlation theorem: the preparatory-window data needed for the relative estimate on newly born boundary terms. It is explicitly outstanding at lines 2376–2385 and 2809–2812. Its output is a relative norm bound of the form

\[
 \mathfrak N^{A,\mathbb C}(\mathbf B'(A))
 \le e^{\lambda_\theta}c_1^\flat
 e^{-(1+\beta_s/4)\kappa d_k(A)}.
 \tag{3.3}
\]

The present note does not claim that proving (3.2) alone settles this window antecedent. They meet in the large-field analytic-domain machinery but should not be silently identified.

No actual circularity was established in this audit. In particular, the dependence of the weight lemma at the preparatory site on previously created terms is expressly ordered by the joint induction (lines 60329–60343). It is a missing hypothesis, not a demonstrated cycle, that obstructs the above implication.

## 4. A quantitative sufficient lemma for the three maps

The following replaces the phrase “make the coupling small enough” by two testable inequalities. It is a proved abstract lemma; verifying its hypotheses for the actual three maps is the model task.

For a finite family of field slots indexed by their creation levels \(j\), put

\[
 \delta_j=A_1g_j(\log g_j^{-2})^{p_0},
 \quad \alpha_j=C_*g_j(\log g_j^{-2})^q,
 \quad q>p_0,
 \qquad
 \|u\|_\delta=\max_j\frac{\|u_j\|_j}{\delta_j}.
 \tag{4.1}
\]

The norms \(\|\cdot\|_j\) must include **all** field, derivative, current and Hölder seminorms defining the actual analytic chart. Bounds on just the field sup norm are insufficient. Let \(\epsilon=\max_j\delta_j\). Suppose that, in fixed charts about admissible backgrounds, the three response maps are solutions of

\[
 H_i=G_i(\sigma_i)\xi_i+
 G_i(\sigma_i)\mathcal N_i(H_i;\sigma_i,\psi_i),
 \qquad i=4,3,2,
 \tag{4.2}
\]

where the output of each map is the input to the next. Assume jointly holomorphic coefficients on the open decoupling polydisc and all allowed background charts, and uniform estimates

\[
 \|G_i\|_{\delta\to\delta}\le D,\qquad D\ge1,
\]
\[
 \mathcal N_i(0)=0,\qquad
 \|\mathcal N_i(u)-\mathcal N_i(v)\|_\delta
 \le A\epsilon(\|u\|_\delta+\|v\|_\delta)\|u-v\|_\delta.
 \tag{4.3}
\]

Assume (4.3) on the balls needed below, and that the background occupies at most half of each final analytic radius. If

\[
 32 A D^4\epsilon\le1,
 \qquad 16D^3\delta_j\le\alpha_j\quad\text{for every slot }j,
 \tag{4.4}
\]

then an input with \(\|\xi_4\|_\delta\le1\) gives jointly holomorphic solutions with

\[
 \|H_4\|_\delta\le2D,
 \quad\|H_3\|_\delta\le(2D)^2,
 \quad\|H_2\|_\delta\le(2D)^3.
 \tag{4.5}
\]

The output fits in the remaining half of every analytic radius. Thus any term bounded by \(\mathfrak b_t\) on those charts obeys (3.1) after substitution. The statement is uniform in the number of decoupling variables and field slots.

**Proof.** For an input of norm at most \(s\), use the ball of radius \(R=2Ds\). On that ball (4.3) gives \(\|\mathcal N(H)\|_\delta\le A\epsilon R^2\). The fixed-point map has Lipschitz constant at most \(2DA\epsilon R=4AD^2\epsilon s\). For the largest required input \(s=(2D)^2\), the first inequality of (4.4) makes this at most \(1/2\). Its nonlinear contribution is at most \(DA\epsilon R^2\le R/4\), while the linear contribution is at most \(R/2\). It therefore maps the ball strictly into itself and contracts. Picard iteration converges uniformly with ratio at most \(1/2\); its terms are jointly holomorphic, so the limit is jointly holomorphic. Repeat three times. The second inequality of (4.4) gives \((2D)^3\delta_j\le\alpha_j/2\). Composition with the analytic term proves the last assertion. For open parameter domains one may run this argument on arbitrary compact subpolydiscs; the uniform bounds are unchanged. No assertion about analytic boundary values is needed for interior Cauchy estimates.

For the expected \(D=C e^{16\kappa_1}\), all constants in (4.4) can be fixed before the coupling ceiling. At the **same scale**, the second condition is simply

\[
 (\log \gamma^{-2})^{q-p_0}
 \ge \frac{16D^3A_1}{C_*}.
 \tag{4.6}
\]

On \(\log\gamma^{-2}>2p_0\), the function \(g(\log g^{-2})^{p_0}\) increases with \(g\), so \(\epsilon\le A_1\gamma(\log\gamma^{-2})^{p_0}\). Both conditions of (4.4) follow from an explicit sufficiently small \(\gamma\), with no upper bound on the number of UV steps. The radii and the strict inequality \(q>p_0\) occur in the raw account at lines 1754–1812. This calculation closes the **same-scale radius arithmetic**, conditionally on the operator and nonlinear estimates in the correct norms.

### Why an unweighted estimate is not enough

The operator estimate in (4.3) is scale weighted. An unweighted bound \(\|G\|\le D\), even with spatial exponential decay, does not imply it for arbitrarily old slots. As an exact two-slot diagnostic, take

\[
 T(u_j,u_k)=(u_k,0),\qquad \|T\|_{\infty\to\infty}=1.
\]

For \(j\) an arbitrarily fine old level and \(k\) a fixed physical stopping level, \(\alpha_j\to0\) as \(g_j\to0\), while \(\delta_k\) stays fixed. The input \((0,\delta_k)\) is small in the current-level norm but its image eventually lies outside the old radius \(\alpha_j\). If the slots occupy the same spatial location, a bound based only on spatial distance does not detect this failure.

This is not a counterexample to Bałaban's actual maps. It shows exactly why the generic route at lines 46179–46218—multiply argument size by \(e^{16\kappa_1}\), then shrink \(\gamma\)—needs a slot-by-slot estimate. The source-free inheritance/arrest construction may supply it, but the two-profile restriction does not.

One sufficient way to verify the missing weighted estimate is a kernel estimate

\[
 \sup_j\sum_\ell
 \|G_{j\ell}(\sigma)\|\frac{\delta_\ell}{\delta_j}\le D.
 \tag{4.7}
\]

For example, if \(\delta_\ell/\delta_j\le C(1+|\ell-j|)^b\) and the relevant transfer kernels have \(\|G_{j\ell}\|\le D_0e^{-c|\ell-j|}\), (4.7) follows with \(D=C D_0\sum_{m\in\mathbb Z}(1+|m|)^be^{-c|m|}\). This is merely a sufficient check: exponential decay in *scale separation* is not asserted by a spatial random-walk bound alone.

## 5. Why real domination does not prove the restricted complex bound

For every finite lattice, positivity of the unsourced measure gives

\[
 |Z(u+iv)|\le Z(u).
\]

After a holomorphic source subtraction it only gives

\[
 |e^{-\mathcal E(u+iv)}Z(u+iv)|
 \le e^{\mathcal E(u)-\Re\mathcal E(u+iv)}
 \bigl[e^{-\mathcal E(u)}Z(u)\bigr],
 \tag{5.1}
\]

when the real counterterm is real. The prefactor can carry the whole UV divergence even for one profile. Take an exactly Gaussian source variable \(X_a\) with variance \(\sigma_a^2\to\infty\):

\[
 Z_a(z)=e^{\sigma_a^2z^2/2},\qquad
 \mathcal E_a(z)=\sigma_a^2z^2/2.
\]

The actual normalized function is identically one, but (5.1) costs \(e^{\sigma_a^2(\Im z)^2/2}\). Thus the failure is in the proposed estimate, not in source stability itself. Positivity or a uniform bound on real sources cannot simply replace the complex analytic estimate.

Reflection symmetry does make \(Z((\Re z)F_e+i(\Im z)F_o)\) nonnegative, but does not fix this loss after subtraction. The face Gaussian diagnostic in `compactness_research.md` explains a separate interface loss. A buffered source avoids imaginary jumps at the faces; it does not remove the bulk cancellation needed in (5.1).

Nor may one define \(\mathcal E=\log Z\) and declare the remainder one. Such a counterterm must be local, consistently normalized, and have controlled mixed derivatives at separated supports. A global logarithm can fail to exist uniformly and would assume precisely the correlation information being sought.

## 6. What a fixed stopping scale genuinely removes

The last-scale argument reads the stopping coupling through

\[
 x_{K'}\le g^{-2}+b_++3\lambda m+2c_2
\]

and the top-zone exponent contains \(\log x_{K'}\): lines 59755–59785. Taking a fixed physical stopping scale, with a uniformly bounded stopping coupling, removes the dependence associated with allowing this scale to drift with the outer torus. The chessboard root then turns the extensive bound into a fixed-cell cost.

It does not bound the number \(K'\) of earlier UV steps or the age of a term in a surviving large-field history. Thus it does not remove the need for uniformity in (4.7), the preparatory-window estimate (3.3), or control of all large-field histories. Restricting to a finite number of UV steps would avoid that issue but would not construct a continuum limit.

The sourced large-field proposition at lines 15206–15331 is a conditional assembly of exactly these ingredients. Its modulus proof, lines 14396–14600, uses the small complex shift to retain a positive fraction of the Wilson action. That elementary inequality is valid, but its potential bound already assumes the needed analytic tube estimates. Reusing that modulus lemma to supply those tube estimates would be circular; the posted proof instead lists them as antecedents.

## 7. Original local target, superseded as a dependency claim by §9

The original audit proposed the following local target. Its designation as the next target for the main induction is withdrawn; the claim that the main induction actually visits these localized charts must first be justified:

> For the three localized response maps of CMP 122-II (1.61)–(1.64), on every inherited or arrested analytic chart that the single-cutoff source induction actually visits, prove the scale-weighted operator bound (4.7), a quadratic remainder bound (4.3), and the chart margin needed in (4.4), uniformly for the full decoupling polydisc. Keep the external source confined to the two buffered reflected profiles (2.2).

The contraction lemma then supplies joint holomorphy and composition without any two-cutoff comparison. This is a narrower check than proving the entire correlation theorem at once. It still leaves the relative boundary/window estimate (3.3) and the activity summations to be verified; this note does not label them solved.

Primary references checked online on 16 October 2026:

- [Bałaban, CMP 116 (1988), 1–22, DOI 10.1007/BF01239022](https://link.springer.com/article/10.1007/BF01239022): publisher abstract explicitly states the small-field scope of the cluster construction.
- [Bałaban, CMP 122 (1989), 355–392, DOI 10.1007/BF01238433](https://link.springer.com/article/10.1007/BF01238433): publisher abstract states completion of the ultraviolet-stability proof.

At this initial stage the publisher PDF endpoints returned subscription landing pages, and the attempted Project Euclid record did not expose the text. Equation-level attribution was therefore traced through the deposited account. The later ordinary public-copy access described in §9 improves this evidence, but its OCR still does not recover all of the requested right-hand sides. No access restriction was bypassed.

## 8. Follow-up: the old-slot weights can be paid for an identified response chart

### 8.1 Original-copy search and what was actually obtained

The public OpenAIRE metadata API for DOI `10.1007/BF01238433`, saved as `work/openaire_cmp122b.json`, identifies the original Project Euclid record as `oai:CULeuclid:euclid.cmp/1104178467` and lists that instance as open access. Its canonical link is [Project Euclid CMP122-II](https://projecteuclid.org/euclid.cmp/1104178467). A second metadata response for DOI `10.1007/BF01239022`, saved as `work/openaire_cmp116.json`, independently confirms the open-access [Project Euclid CMP116-II record](https://projecteuclid.org/euclid.cmp/1104161193). Ordinary requests to the CMP122-II page and the public download paths returned an Incapsula access challenge or a tool access error. No challenge was circumvented. Searches of primary institutional sources did not locate an alternative original copy. The Rutgers institutional record supplies a DOI link, not an accessible deposited manuscript.

At that stage the original printed formulas (1.61)–(1.64) remained unobtained. The later source access in §9 verifies their page locations, but the extracted text loses their right-hand sides; those formulas still have not been faithfully transcribed. The equations below are transcriptions/identifications in the deposited raw account unless explicitly stated otherwise.

There is nevertheless additional model-specific content in raw I. In particular, the earlier statement that an unweighted decay bound does not by itself pay the old-slot weights needs to be sharpened: the actual multiscale metric and the coupling-flow estimate in raw I do pay those weights, **provided the relevant response really has the stated kernel bound in that metric**. A generic two-slot counterexample does not respect that metric and therefore does not obstruct this route.

### 8.2 One actual map and its exact linearization

Raw I, lines 13583–13644, defines

\[
 G_0=(\Delta+D_URD_U^*+Q^*\ell^{-2}Q)^{-1},\qquad
 q_0=(QG_0Q^*)^{-1},\qquad
 H_0=G_0Q^*q_0\ell^{-1}.
 \tag{8.1}
\]

Here \(\ell\) is multiplication by the local layer scale. Thus \(\ell QH_0=I\); dropping the last \(\ell^{-1}\) would change the datum normalization. Raw I, lines 14376–14437, then gives the actual free-current response chart

\[
 A_0=T[\Theta_J H_0B-V'^J(A_0+H_0B)],\quad
 A=A_0+H_0B,\quad
 \mathcal H^J(B)=A-H^JD^J(A),\qquad T=\widetilde G^J,
 \tag{8.2}
\]

with the nonlinear averaging correction

\[
 D^J(A)=C\bigl(\ell A-\ell H^JD^J(A)\bigr).
 \tag{8.3}
\]

This is not a guessed model: (8.2) is the displayed response equation in that definition, identified there with the current-dependent version of CMP102 (180), and CMP116 (1.4) with a different quadratic splitting. The deposited definition identifies \(\mathcal H^J\) with the field used in CMP116 (1.2). It does **not** identify it with all three CMP122-II link functions.

At a fixed admissible background \((U,J)\), assume the displayed fixed points exist and the following inverses are bounded. Put

\[
 L_A=I-H^JD'(A),\qquad
 D'(A)=(I+C'(\ell\mathcal H^J)\ell H^J)^{-1}
 C'(\ell\mathcal H^J)\ell.
 \tag{8.4}
\]

Direct differentiation, without any additional field-theoretic input, gives

\[
 D_B\mathcal H^J
 =L_A\,(I+TV''^J(A))^{-1}(I+T\Theta_J)H_0.
 \tag{8.5}
\]

Indeed \((I+TV'')dA_0=T(\Theta_J-V'')H_0dB\), and adding \((I+TV'')H_0dB\) gives the middle two factors in (8.5). Formula (8.4) follows by differentiating (8.3). This verifies the factorization implicit in raw I, lines 13996–14026 and 14814–14825. Since \(D'(0)=V''^J(0)=0\) for the stated quadratic remainders, the linearization at zero is \((I+T\Theta_J)H_0\); at zero free current, it is exactly \(H_0\). Nonzero free current must not be silently dropped.

The asserted decay estimate for this derivative is raw I, lines 14842–14866:

\[
 |D_{B(c)}\mathcal H^J(x)|
 \le C_H\ell_j^{-1}\ell_{j'}^{-4}e^{-\mu d(y,y')},
 \qquad x\in\Delta(y),\ c\text{ at }y'\in\Lambda_{j'},
 \tag{8.6}
\]

with the analogous powers \(\ell_j^{-2}\), \(\ell_j^{-2-\beta}\), \(\ell_j^{-3}\) for the gradient, local Hölder, and current-response members. The input sum carries the measure \(\ell_{j'}^4\), which cancels the input factor in (8.6). Raw I's K10 proposition, lines 15265–15467, asserts these bounds also for the walk-localized chart on \(|s(\Delta)|\le e^{\kappa_1}\), with a fixed multiplier \(e^{c_{\mathbb K}\kappa_1}\) and smaller datum radius. Its stated antecedents include the constrained covariance inverse walk expansion and the analytic nonlinear-averaging estimates. The algebra below is proved; this note has not independently certified all antecedents of K8/K10.

### 8.3 Explicit weighted row summation

Write \(a_j=A_1g_j(\log g_j^{-2})^{p_0}\), so \(a_j\) is the small datum scale called \(\delta_j\) in §4. Use the coupling-flow hypothesis actually displayed in raw I, lines 10234–10245:

\[
 x_j\ge X:=\gamma^{-2},\qquad
 -c_5\le x_j-x_k\le B^\sharp(k-j)\quad(j\le k).
 \tag{8.7}
\]

Assume \(B^\sharp\gamma^2\le1\) and \(\log X\ge\max(1,2p_0)\). Then for every pair of layers,

\[
 \frac{a_k}{a_j}\le C_w\sqrt{1+|k-j|},\qquad
 C_w=\max\left\{
 e^{p_0c_5\gamma^2/\log X},\sqrt{1+c_5\gamma^2}\right\}.
 \tag{8.8}
\]

For \(k\ge j\), (8.7) gives \(g_k/g_j\le\sqrt{1+k-j}\), while
\((\log x_k/\log x_j)^{p_0}\le e^{p_0c_5\gamma^2/\log X}\).
For \(k<j\), it gives \(g_k/g_j\le\sqrt{1+c_5\gamma^2}\) and

\[
 \left(\frac{\log x_k}{\log x_j}\right)^{p_0}
 \le\left(1+\frac{\log(1+B^\sharp\gamma^2(j-k))}{\log X}\right)^{p_0}
 \le(1+j-k)^{p_0/\log X}\le\sqrt{1+j-k}.
\]

This proves (8.8) in both directions, including the potentially dangerous propagation from the coarser datum into an older fine layer.

The deposited multiscale geometry gives, at raw I lines 13471–13483,

\[
 d(y,y')\ge W(|j-j'|-1)_+,\qquad W=R_1\mathfrak M.
 \tag{8.9}
\]

Consequently \(1+|j-j'|\le2+d/W\le2e^{d/(2W)}\). If \(\mu W\ge1/2\), (8.8) implies

\[
 e^{-\mu d(y,y')}\frac{a_{j'}}{a_j}
 \le\sqrt2 C_w e^{-\mu d(y,y')/2}.
 \tag{8.10}
\]

Use the block sum estimate from raw I, lines 13424–13429, at the required decay fraction, and let \(C_{\rm sum}\) include the bounded number of block-bond orientations/interface bonds. Applying (8.6) to each input block now proves

\[
 \sup_y\frac{\ell_j|D_B\mathcal H^J[v](x)|}{a_j}
 \le\sqrt2 C_w C_H C_{\rm sum}
 \sup_c\frac{|v(c)|}{a_{j(c)}}.
 \tag{8.11}
\]

The same calculation applies separately to the gradient, local Hölder and current members with their displayed canonical output powers. For the localized chart, replace \(C_H\) by the K10 constant \(C_He^{c_{\mathbb K}\kappa_1}\). The bound is independent of the number of layers and of the UV cutoff. Integrating (8.11) along \(tB\), with the fixed point vanishing at \(B=0\), gives the corresponding nonlinear response bound as long as the segment stays inside the chart domain.

This explicitly supplies the weighted row estimate sought in §4 for this response, **conditional on the actual decay estimate (8.6)**. No new all-layer weighted operator theorem is needed once that estimate and the metric separation are established.

### 8.4 What still cannot be inferred for the localized three-link branch

Raw II, lines 48058–48125, defines the three links by reference to CMP122-II (1.61), (1.62), (1.63), with the last response supplied by (1.64). It does not reproduce those right-hand sides. Raw II lines 48405–48407 explicitly distinguish the \(H_k\) of CMP122-II (1.64) from the \(H_k\) of CMP116 (1.17): different step, different argument. Thus the identification needed to apply (8.5)–(8.11) to the three links is absent, rather than disproved.

If the localized three-link branch is pursued, its source/formula requirements are:

1. Obtain the right-hand sides of CMP122-II (1.61)–(1.64), plus their input identities (1.51), (1.54), (1.57), (1.58). Determine whether each response has the form (8.2)–(8.3), with which determining set, background and block datum normalization.
2. Check that each input datum is bounded by the layer scale \(a_j\) after the preceding link, and that the changed determining sets still obey (8.9). This is a statement about actual geometry, not merely an operator name.
3. Check that the background/current outputs remain in the antecedent domains of K8/K10, including the kept gauge transform \(u_k\) in the first link. Bounds on derivatives in \(B\) do not automatically bound dependence on arbitrary background and current slots.

If those checks hold, (8.11) pays the UV-age ratios and the earlier contraction argument can be applied with explicit constants. Without them, asserting stability of these links would still conflate the small-field response chart with the large-field links. They are not established as mandatory antecedents of the active global-carrier route, whose separate obligations are traced next.

## 9. Follow-up: the active global-carrier route and its actual current input

### 9.1 Original copies accessed, with an equation-recovery limit

Ordinary web access returned the original articles, hosted at these public PDF URLs:

- [CMP122-II original article](https://scispace.com/pdf/large-field-renormalization-ii-localization-exponentiation-h8b7ih93xo.pdf), journal pp.355–392, 38 PDF pages.
- [CMP116-II original article](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-4penm4k7hc.pdf), journal pp.1–22, 22 PDF pages.

These are copies of the original research papers, not third-party summaries. The extraction gives the following locations: CMP122-II (1.51),(1.54), p.370; (1.55)–(1.58), p.371; (1.61),(1.62), p.373; (1.63),(1.64), p.374; (1.65), p.375. The OCR loses most requested equation right-hand sides. The two-input dependence in (1.54) and localization through (1.55) are readable in the surrounding prose. No faithful transcription of (1.61)–(1.64) has been obtained. The screenshot API is unavailable. An ordinary direct PDF request met an access challenge; no further download route was attempted.

CMP116-II p.2, (1.2)–(1.5), supplies the small-response fixed-point equations used in §8; p.3 explains that the bounds and regularity of the operators are what their nonlinear construction uses. This supports the identity of the **small response** under study; it does not identify it with every large-field carrier.

### 9.2 Correct dependency path from the source correlation theorem

The main theorem is `5.1:thm-correlation-theorem` (Raw II 2791ff), under `5.1:def-admitted-inputs` (2083ff). Its proof's explicit dependency order is `5.2:prf-induction-order` (25480ff), not the Chapter 6 consumer discussion at60700ff:

\[
 (g)_{k-1}\longrightarrow(T)\longrightarrow I_k^{\mathbb C}
 \longrightarrow(P)\longrightarrow(c)\longrightarrow(L)
 \longrightarrow(g)_k.
 \tag{9.1}
\]

The large-field induction step is `5.2:prf-large-field-step`, Raw II25412–25478. It invokes the complex-source R-operation proposition, its companion lemma, the relative bound on R-born boundary terms, and the bracket/orbit-data statements. The explicit complex-source R proposition is `5.2:prop-sourced-large-field-step`,15206–15331. Its hypotheses include inherited chain terms on their stored domains, their complex-source extension, the stage-norm bound at cores, the sourced modulus lemma, the strip theorem and its volume/combinatorial companions, and the cascade charge bound. Thus the modulus estimate is a consumer of the domain machinery, not an independent proof of it.

At site L, the induction's closing lemma consumes the reference-coupling clause, the sourced chain induction hypothesis, containment, a relative-bound constant, nesting geometry, and the source statements (25556–25569). The exterior/recursion argument then explicitly consumes the layer objects

\[
 \mathbb H_s,\qquad \mathcal J_s^\sharp[\chi]
\]

with their input bounds and localization under sources (25597–25604). The text says these lie upstream of the correlation theorem. It also explicitly avoids using the later two-point base theorem here because that would be circular (25606–25609). No such circle has been demonstrated by this audit.

The link to the active global reading is explicit:

1. Raw II2088–2118 identifies the data passed to site L as the presented carrier pair
   \(((\hat{\mathcal U}^{\mathfrak b})^h,\operatorname{Ad}_h\hat{\mathcal J}^{\mathfrak b})\), holomorphic in the configuration/current variables. Raw II5636–5653 evaluates the units at this pair, with their live slots rotated by the site map.
2. Raw I `4.21:lem-wrapped-holomorphy`,72988–73006, assumes the key containment theorem at L, plus inheritance and arrested-term containment. Lines73107–73121 identify stage4 with original(1.51), stage3 with original(1.54), and expressly state that the expansion used at L is the global presented chain restricted to each term's true domain X.
3. Raw I73123–73140 describes the required stage induction: the stage pair is in \(\mathfrak K(\mathfrak B_s;\gamma_0)\), its argument has norm at most \(\varepsilon_\sharp\); the layer theorem and its corollary give localization, the next entries, and the next-stage membership. This must hold for the full product of complex source, decoupling and interpolation polydiscs, not merely at real points.
4. Raw I `4.21:rem-global-chain`,73545–73634, says that the four functions \(\mathbb H_4,\ldots,\mathbb H_1\) use the global determining sets \(\mathbf B''_k,\mathbf B''_k,\mathbf B_1,\mathbf B_k\), with separate decoupling families. Lines73570–73576 explicitly exclude replacing them by the localized original(1.61)–(1.63) maps on scaffold domains. The global containment is the base of wrapped holomorphy (73598–73606).

Accordingly, the prior inference “three per-link readings unproved in §5.6, therefore the main source proof first stops there” is not supported. There is a genuine exposition issue: Raw II `5.6:rem-large-field-terms`,47718–47746, also calls its localized three-link reading site L. It is followed by an expressly conditional nested-composition theorem. It must be reconciled with Raw I's explicit exclusion of that reading. Neither the positional order of the files nor the phrase “not used” proves by itself that every downstream use has been replaced. The safe research conclusion is to audit the **global layer/containment path** rather than silently identify the two paths.

### 9.3 The two-input layer is not the zero-datum response of §8

Raw I94308–94310 gives the notation

\[
 \mathbb H[\mathfrak B;(W,J);\sigma;\mathsf d]
\]

for a localized small solution. Uses with block-only datum \(\mathsf d=(0,b)\) occur at94330,94348 and131634. The third carrier has a nonzero **field/current datum** as well as block data: Raw II5716–5718 says its first argument is the localized field \(f_1\), and its second argument is supported in the shell \(\mathsf S\). Raw I73108–73112 names the first datum \(\mathfrak j_3=\widetilde G_0(\sigma)\mathsf J_3\). This is the source/current slot appearing in original(1.54).

The domain is concrete. Raw I110264–110276 defines

\[
 \mathfrak K_{109}(\mathfrak B;\gamma_0)
 =\{(W,J):W=e^{i\eta A'}U,\quad U\text{ satisfies CMP99b(3.35)},
 \ A'\text{ satisfies CMP99b(3.37)},\quad
 \sup\ell^3|J|\le\gamma_0\}.
 \tag{9.2}
\]

It keeps a regular real factor U, a small complex potential A', and an independent complex current J. Raw I94244–94248 reports the layer theorem's parameter condition

\[
 K_\natural(\gamma_0+\varepsilon_3)\le1,
 \qquad \varepsilon_\sharp=\varepsilon_3/(4K_\sharp).
 \tag{9.3}
\]

The six-clause layer theorem is invoked by name in Raw I72392–72399 and73132–73140, with holomorphy, weighted bounds, identification and locality cited at later use sites. Searches of all deposited tex files located these uses and the domain descriptions above, but did **not** identify a standalone numbered statement plus defining two-input equation under that name. This is an unresolved identification in this audit, not a proof of nonexistence. In particular, the fully displayed chart of §8 deliberately removes the inhomogeneous current forcing. Its derivative formula cannot simply be renamed as the derivative of this two-input layer.

The arbitrary-exempt-set lemma, Raw I72373–72538, also assumes the layer theorem and its corollary. It extends their valid bounds to arbitrary decoupling subfamilies by walk counting and locality; it does not independently construct the two-input layer. Consequently it does not discharge the preceding identification.

### 9.4 A model-specific advance: the current can be localized, with the decoupling error retained

The original identity (1.55) is transcribed in Raw I92374–92395 as

\[
 G''_kJ_{1,2}
 =G''_k(1-\theta)Q^*\theta_1H^*J_1
   +G''_k\theta J_{1,2}.
 \tag{9.4}
\]

This uses the projection identity \(G''_kQ''^*=0\) and constrained criticality. More importantly, Raw I `4.22:lem-current-localisation`,92401–92620, does not incorrectly apply this annihilation at general complex decoupling parameters. Its exact decomposition is

\[
\begin{aligned}
 \mathbf G''(\sigma)\hat{\mathcal J}^{\mathfrak b_2}
 &=\mathbf G''(\sigma)
   [1_{(D_2^\circ)^c}\hat{\mathcal J}^{\mathfrak b_2}+r]\\
 &\quad+[\mathbf G''(\sigma)-\mathbf G''(1)]
       Q''^*(\lambda_2|_{D_2^\circ}),
\end{aligned}
 \tag{9.5}
\]

with r supported beside the boundary of \(D_2^\circ\) and bounded by \(C_Q\sup|J_2|\). For verification, write the deep part of the current as the projected multiplier plus the boundary correction, multiply by \(\mathbf G''(\sigma)\), then add and subtract \(\mathbf G''(1)Q''^*\lambda_2=0\). This gives exactly (9.5). The second line is indispensable.

The hypotheses at92439–92464 are constrained Euler–Lagrange criticality; the identity of the presented current with the actual current on the deep stencils; a real order-h base U2 independent of the complex configuration there; the layer response bound and its argument budget; and the undecoupled annihilation, decay and walk expansion. The proof at92562–92571 observes that every walk in the difference \(\mathbf G''(\sigma)-\mathbf G''(1)\) meets a decoupled cube outside \(\Lambda\). A walk from a deep point must therefore exit \(\Lambda\). This supplies the second localized contribution, yielding

\[
 K_u\Theta_0^{\rm loc}(\mathbb H_s)(\tilde z)
 \le C_L\varepsilon_{\mathfrak Q}(k)
 e^{-\delta_L(d_{\rm sc}(z,\mathsf S)-1)},
 \quad s=3,4,\qquad
 \delta_L=\tfrac12\min(\delta_1,\delta_G).
 \tag{9.6}
\]

Raw II5719–5733 then displays the convolution that passes the localized first datum through the layer response:

\[
 \sum_y e^{-\delta_1 d_{\rm sc}(s,y)-\delta_Gd_{\rm sc}(y,\mathsf S)}
 \le C_\rho(\delta_L)e^{-\delta_Ld_{\rm sc}(s,\mathsf S)}.
 \tag{9.7}
\]

Thus “the current source is omitted” is not a valid diagnosis. What remains to verify is the stated two-input layer bound and all its actual membership assumptions. Together with §8, this isolates the next concrete task: recover the defining equation of that global two-input layer and prove it retains the needed current and block-data kernel estimates on (9.2), for the determining sets actually traversed. Once those estimates hold in the inherited metric, the age weights are already paid by (8.8)–(8.11).

### 9.5 Independent upstream stopping-coupling condition

The original CMP122-II introduction, p.355, states its small-effective-coupling hypothesis and discusses an unpublished perturbative proof at the time. This historical sentence does not establish the status of any later result.

For the deposited account the relevant test is internal. Raw I `4.19:prop-clause-zero`,56419–56458, proves the first-passage trajectory only assuming the increment estimates and the already-reached effective-density induction. The numerical reduction is sound: with

\[
 x_l=x_{l-1}-\beta_l,quad
 \sum_{l=i+1}^j\beta_l^0\ge c_0(j-i)-2c_2,
 \quad |\beta_l^{\mathfrak A}-\beta_l^0|\le c_0/2,
 \quad |\beta_l^{\mathfrak R}|\le\bar\varsigma\le c_0/4,
\]

telescoping yields

\[
 (c_0/2-\bar\varsigma)(j-i)-2c_2
 \le x_i-x_j\le(C_\beta+\bar\varsigma)(j-i).
 \tag{9.8}
\]

Then Raw I56530–56565 checks that the first-passage trajectory obeys the small-coupling hypothesis of the stability theorem. The specific unclosed input is not this arithmetic: `4.2:lem-unmarked` explicitly marks (*) at4072–4088 when transferring the CMP116 remainder estimate to the CMP119 cutoff and the chosen fluctuation radius. At56428–56430 the clause-zero proposition describes both one-loop and unmarked lemmas as incomplete, whereas the actual one-loop lemma3901–3945 is cited by statement with an outline. The unmarked correction is the clearest explicit outstanding estimate and should be cited, without exaggerating the status of the one-loop coefficient itself.

Fixing a physical stopping scale does not remove the need for a controlled actual running trajectory. An arbitrary sequence of small couplings is not yet the sequence generated by the Wilson RG. This is an upstream obligation distinct from the global carrier's analytic bounds and from two-cutoff uniqueness.
