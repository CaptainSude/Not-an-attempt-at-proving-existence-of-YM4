# Published renormalized induction, running couplings, and the remaining transfer

17 October 2026. Primary-paper research for the common-domain composite macrostep. No repository or user-facing output was edited. Journal pages, not PDF viewer page numbers, are used below. This note distinguishes a printed theorem, a proof actually located, and a transfer to our different renormalization map.

## 1. Result of the search

The published chain contains a proved small-field induction theorem and a proved large-field completion **conditional on all effective couplings remaining small**. The separate SU(2) trajectory theorem is announced in CMP109. CMP122-II explicitly reports that its proof was still unpublished in 1989. Searches of the later primary records and papers listed below did not locate that precise proof. This is a bounded search result, not a claim that no later proof or manuscript exists.

Our next reusable source input is consequently the conditional renormalized induction theorem, with its actual hypotheses retained. It cannot yet be applied to the new one-shot composite macrostep by replacing the letter L with R.

## 2. Primary proof map

### CMP109: extraction and the distinct trajectory statement

[Bałaban, CMP109 (1987), 249–301, original article](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf), [DOI](https://doi.org/10.1007/BF01215223).

Theorem 3, p.264, chooses constants kappa_0, M(kappa), gamma, epsilon_0, epsilon_1, alpha_0, alpha_1. For kappa>=kappa_0, M>=M(kappa), and 0<g_k<=gamma at every step, the actions defined by (0.17)–(0.20) satisfy (1.1)–(1.22). M here is the paper's localization parameter, not our preceding refinement M. Equation (1.18), p.263, bounds localized analytic activities on the paper's complex (U,J) domains.

Section 4 supplies the Ward cancellations. Section 5, pp.292–298, extracts the transverse second-order term: (5.37)–(5.42), p.297, identify its coefficient; (5.43)–(5.44) and p.298 perform the cancellations and distinguish localization work deferred to Part II. The beta functions also depend on preceding couplings.

Theorem 2, p.259, instead asserts, for d=4 and SU(2), a bare coupling tuned to a prescribed sufficiently small terminal g, containment in (0,gamma], and the bounds (0.31). Its proof is explicitly deferred. The scanned equation (0.31) was not reliably recovered here, so its exact constants are not retranscribed.

### CMP116: the small-field induction proof is completed

[Bałaban, CMP116 (1988), 1–22, original article](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-4penm4k7hc.pdf), [DOI](https://doi.org/10.1007/BF01239022).

The introduction, p.1, identifies the result as completion of CMP109 Theorem 3. Section 1 localizes the already renormalized fluctuation exponent; Section 2 constructs its connected logarithm. At pp.21–22, (2.41) recovers the inductive activity bound after choosing the geometric and smallness parameters. The Gaussian normalization contribution is localized separately and added back. The final paragraph explicitly closes the inductive proof. This proves preservation of the specified source class, not merely convergence of one unrenormalized fluctuation integral. It does not prove CMP109 Theorem 2.

This is the strongest immediately relevant published result for the amplitude problem: the original constant in the induction is recovered after the source's subtractions, rather than allowed to multiply at every step.

### CMP119: the full-density format and why another operation is needed

[Bałaban, CMP119 (1988), 243–285, original article](https://scispace.com/pdf/convergent-renormalization-expansions-for-lattice-gauge-29jyexd38e.pdf), [DOI](https://doi.org/10.1007/BF01217741).

The theorem on p.245 says that a density satisfying Section 2's assumptions retains the corresponding form under the renormalization transformation. Section 2 starts at p.254; (2.18) is the history-dependent density representation. The setup includes characteristic functions, restricted/background domains and large-field operations, not just homogeneous analytic activities. Pages 243–244 distinguish the exact averaging transformation T from the additional large-field operation R. The latter is needed because the suppression available in d=4 does not control all later steps in a fixed bad region; its required properties are assumed here and proved in the following papers. Equations (2.30)–(2.33), p.260, describe the localized large-field remainder and its covariance properties.

The abstract's completed superrenormalizable conclusion must not be silently substituted for a complete unconditional four-dimensional trajectory theorem.

### CMP122: what the later large-field work actually completes

Part I is [CMP122 (1989), 175–202](https://doi.org/10.1007/BF01257412), official [Euclid PDF endpoint](https://projecteuclid.org/download/pdf_1/euclid.cmp/1104178393). The endpoint returned a security/interstitial response in this pass; no new detailed Part I formula claim is based on it.

Part II is [CMP122 (1989), 355–392, original article](https://scispace.com/pdf/large-field-renormalization-ii-localization-exponentiation-h8b7ih93xo.pdf), [DOI](https://doi.org/10.1007/BF01238433).

Theorem 1, p.355: if the effective couplings lie in (0,gamma] for sufficiently small gamma, the effective densities have the form and all conditions/bounds of CMP119 Section 2. The following paragraph says the separate perturbative trajectory proof “has not been published yet”; the assumption is therefore retained. Equation (0.1), pp.355–356, gives ultraviolet-stability density bounds with constants independent of the level, lattice, and background. The paper closes normalized large-field replacements, their localization and exponentiation. The decisive concluding estimates are (1.97)–(1.102), pp.389–391; the proof explicitly closes on p.391. The alternative representation (1.104) closes on p.392.

The author separates subsequent observable analysis from this result on p.356. Thus the 1989 completion really removes the earlier large-field-operation gap; it does not remove the stated coupling hypothesis or itself construct all continuum Schwinger functions.

## 3. Later-paper search and evidentiary limit

The bibliographic search used the author-name and author-identifier queries in [INSPIRE](https://inspirehep.net/literature?q=author%3AT.Balaban.1), journal/DOI records, and the original articles' references. The name-query inventory is saved separately in `work/balaban_inspire_inventory.json`; it is a discovery aid, not proof of completeness.

A plausible later title is [Bałaban, *A low temperature expansion for classical N-vector models. II. Renormalization group equations*, CMP182 (1996), 675–721](https://link.springer.com/article/10.1007/BF02506422). Its own abstract identifies the model as classical N-vector and describes construction of its RG solutions. It is not a publication of the four-dimensional Yang–Mills theorem merely because the words “renormalization group equations” match.

[Magnen–Rivasseau–Sénéor, *Construction of YM4 with an infrared cutoff*, CMP155 (1993), 325–383](https://doi.org/10.1007/BF02097397), has an [author-uploaded primary text](https://www.researchgate.net/publication/251358884_Construction_of_YM_4_with_an_infrared_cutoff). Its stated setting is pure SU(2), trivial topological sector, fixed infrared cutoff, regularized axial gauge and specifically chosen momentum cutoffs, with gauge-restoring counterterms. It is a distinct construction, not an identified proof of Bałaban's exact lattice trajectory or a theorem about our retained-variable macrostep. Its full proof was not audited in this pass.

No later primary proof of the exact CMP109 Theorem 2 was located. The reliable historical assertion is the author's explicit 1989 statement; an assertion about all subsequent literature would require a more exhaustive bibliography/manuscript search. Recent generated proof pages and secondary summaries were not used to certify any theorem.

## 4. Precise reusable theorem and our transfer obligations

**Reusable source theorem, with references rather than altered hypotheses.** Use CMP109 Theorem 3, proved through CMP116, for its defined action sequence and its entire (1.1)–(1.22) induction class, under the coupling-containment condition. For complete densities use CMP122-II Theorem 1 with the CMP119 Section 2 class and the same containment assumption. This is a legitimate conditional input. It is not a theorem for every small gauge-invariant analytic function in an arbitrary polymer norm.

Our current theorem controls a homogeneous one-shot integral with constraint M_ell^s, a separate direct-R contour gauge, and a retained-coordinate window, R=ell^s. Its input and output share a product ball and a connected-carrier norm. The bound still contains C_T epsilon. The following are therefore transfer obligations, not consequences of the citations:

1. **Extraction space.** Define a bounded, symmetry-compatible extraction on the actual total correction, including its vacuum part and its local marginal sector. A scalar coefficient extracted from a quadratic Hessian is not by itself a proof that the associated cubic/quartic terms combine into the same gauge-invariant action. Our total Ward identity is available, but the full translation/point-symmetry hypotheses and any partition dependence must be checked for this specific map.
2. **Remainder estimate.** Prove a stable norm estimate after extraction. The presently proved same-ball transport and Gaussian logarithm estimates give boundedness, not that estimate. High-jet suppression of the pure stationary-background composition is only one term in the full quantum update.
3. **Actual coefficient and sign.** Compute or transfer the leading inverse-coupling shift for this precise integral, with its gauge normalization, Haar/pivot terms, determinant and cutoff. Bound the error uniformly in the preceding refinement and allowed inherited remainder. Perturbative universality is not a replacement for this comparison.
4. **Macrostep identity.** A one-shot retained window is not the intersection of primitive windows. Although the ordinary averaging constraint composes, the cutoff and inserted gauge weights in the selected sector do not thereby become the sequential source scheme. Neither s times a primitive beta coefficient nor the full source induction follows from the constraint identity alone.
5. **Large fields and histories.** Extend the measure identity and renormalized estimates to the actual complements and mixed histories before applying the complete-density theorem. Our homogeneous small-ball model does not supply those hypotheses.

A clean next target is a renormalized macrostep proposition with a fixed remainder ball, a positive bounded inverse-coupling decrement, and continuous dependence on the input state. Once those three inputs are proved, tuning a finite trajectory is elementary, as follows.

## 5. An elementary endpoint-tuning lemma

This lemma is derived here and is not attributed to Bałaban. It isolates the scalar shooting problem from the hard field-theoretic estimates.

Let B be a closed remainder-state ball; the state may include retained finite history. At every depth k suppose a continuous map, defined for x>=x_min and e in B, has the form

    x' = x - b_k(x,e),       e' = F_k(x,e),
    0 < b_- <= b_k(x,e) <= b_+,
    F_k(x,e) belongs to B.

Assume the initial state e_0(x) is continuous into B. Fix a finite N and terminal X>=x_min. Then some initial value

    x_0 in [X+N b_-, X+N b_+]

generates N genuine steps with x_N=X, and

    X+(N-k)b_- <= x_k <= X+(N-k)b_+       (0<=k<=N).

**Proof.** Temporarily extend the iteration to every real x by evaluating both b_k and F_k at max(x,x_min), while still setting the new real coordinate to x minus that evaluated decrement. The state remains in B and the resulting x_N(x_0) is continuous. At the left endpoint it is at most X; at the right endpoint it is at least X. The intermediate value theorem supplies x_N=X. Every decrement is positive, so this selected run has x_k>=X at all earlier steps. No clipping occurred. Summing the decrement bounds backwards proves the displayed inequalities.

With x=g^-2 this gives positive small couplings, a bare coupling tending to zero at order N^-1/2, and the prescribed terminal g=X^-1/2. It does not give uniqueness, differentiability of the tuned trajectory, consistency as N changes, a continuum limit, or the field-theoretic assumptions themselves.

For example, a proved bound

    ||F_k(x,e)|| <= alpha ||e|| + f(x),
    alpha<1,   sup_(x>=X) f(x) <= (1-alpha) radius(B)

would supply the invariant-state hypothesis. Our current unextracted C_T epsilon estimate does not. Uniform positivity and boundedness of b_k are equally substantive missing inputs. Allowing a state to carry history avoids silently assuming the coefficient is a function of only the current coupling.

## 6. What ultraviolet stability would and would not buy

Even a completed application of the conditional density theorem and the tuning lemma would first control a finite-volume ultraviolet sequence. It would not automatically provide a common measure across cutoffs, tightness in a suitable distribution/gauge-orbit topology, convergent observable families, non-Gaussianity, reflection positivity of the same limiting law, clustering, or a mass gap. Those are separate obligations in our construction. Conversely, these separate obligations do not negate the published density-stability and large-field results: the appropriate conclusion is that they are substantial conditional inputs whose exact interface still has to be proved.

## 7. Focused extraction map: primary locations and the genuine hypothesis mismatch

The following is a formula-location map for the original articles linked in Section2, rather than a replacement statement of their full induction class.

| Required feature | Exact primary location |
|---|---|
| Complex local orbit domains, including the independent current variable and descendant regularity | CMP109 pp262–263, (1.10)–(1.17) |
| Uniform localized analytic bound | CMP109 p263, (1.18) |
| Gauge invariance of **each** localized coefficient | CMP109 p263, (1.19) |
| Gauge Ward identity and its first three differentiated versions | CMP109 pp283–284, (4.9)–(4.15) |
| Only first-gradient Hölder regularity is used for the second spatial difference | CMP109 p285, (4.17)–(4.18) |
| Spatial Taylor expansion, conversion of cubic/quartic expressions to quadratic-kernel moments | CMP109 pp286–290, (4.21)–(4.34) |
| Removal of boundary dependence and resummation to the polarization tensor | CMP109 pp290–291, (4.35)–(4.37) |
| Expansion of the **full Wilson-action subtraction** | CMP109 pp291–292, (4.38)–(4.45) |
| Translation, bond-orientation, point-group, transpose and transverse identities | CMP109 pp292–294, (5.2)–(5.15) |
| Periodic analytic factorization and extraction of the Maxwell coefficient | CMP109 pp294–297, (5.17)–(5.42) |
| Spatially differentiated remainder and cancellation | CMP109 pp297–298, (5.43)–(5.44) and the following paragraph |
| Localization after subtraction; activity and logarithm bounds recovering the induction constant | CMP116 §1; pp20–22, Lemma3/(2.38) through (2.41), and the separate Gaussian-normalization paragraph |

CMP116 has Sections1–2, not Sections3–5; the latter numbering refers to PartI, CMP109.

**Transfer warning.** Our canonical activity coefficients are holomorphic on product balls and have a gauge-invariant **total**. That does not establish the coefficientwise orbit-domain hypothesis (1.19). Applying Ward identities first to the total kernel and localizing the canceled result afterward is a possible alternative proof, but it is an additional argument. The full Wilson counterterm, rather than only its quadratic Taylor term, is essential for preserving the nonlinear identity. The source's infinite-volume, translation-invariant kernel construction likewise cannot be inferred solely from a volume-uniform bound on our finite-regulator coefficients.

Section5 above is only an optional elementary shooting lemma. It is not the deposited trajectory argument and is not needed for the next extraction step: `running_coupling_research.md` already records the source's averaged-drift/first-passage formulation and its exact remaining estimate.

## 8. Independent derivation of the low-degree Ward constraints

This section fixes our own conventions and supplies a directly checkable algebraic input. It is not a transcription of OCR-damaged coefficients in (4.15) or (4.34).

Use Hermitian Lie-algebra coordinates, `U_b=exp(i A_b)`, positively oriented bonds `b=(b_-,b_+)`, and

    (d lambda)_b=lambda_(b_+)-lambda_(b_-),
    U_b(t)=exp(i t lambda_(b_-)) U_b exp(-i t lambda_(b_+)).

On the local logarithm chart, differentiation at t=0 gives

    delta_lambda A = -d lambda + L_lambda(A)+Q_lambda(A,A)+O(A^4 lambda),
    L_lambda(A)_b=(i/2)[lambda_(b_-)+lambda_(b_+), A_b],
    Q_lambda(A,B)_b=(1/24)([A_b,[B_b,d lambda_b]]
                             +[B_b,[A_b,d lambda_b]]).           (8.1)

Indeed the exact expression is

    i[lambda_-,A] - f(i ad_A)d lambda,
    f(z)=z/(1-exp(-z))=1+z/2+z^2/12+O(z^4).

The absence of the cubic Bernoulli term is not needed below, but makes the displayed remainder valid. Let `E(A)` be any analytic gauge-invariant total functional on a finite regulator and put `K_n=D^n E(0)`. Global constant gauge transformations imply `K_1=0` for a semisimple Lie algebra: its value at each bond annihilates every commutator, and commutators span the algebra. Comparing degrees in `DE(A)[delta_lambda A]=0` gives

    K_2(A,d lambda)=0,
    K_3(A,A,d lambda)=2 K_2(A,L_lambda(A)),
    K_4(A,A,A,d lambda)
       =3 K_3(A,A,L_lambda(A))+6 K_2(A,Q_lambda(A,A)).     (8.2)

Polarization yields all mixed identities. In particular

    K_3(A,B,d lambda)
      =K_2(A,L_lambda(B))+K_2(B,L_lambda(A)),

    K_4(A,B,C,d lambda)
      =K_3(A,B,L_lambda(C))+K_3(A,C,L_lambda(B))
         +K_3(B,C,L_lambda(A))
         +2K_2(A,Q_lambda(B,C))+2K_2(B,Q_lambda(A,C))
         +2K_2(C,Q_lambda(A,B)).                          (8.3)

These formulas show precisely why one cannot subtract a quadratic jet and then declare the remainder gauge invariant. They do not alone classify the transverse parts of `K_3,K_4`; spatial Taylor expansion and the local symmetry classification are also needed.

If a translation-invariant scalar/color-diagonal Hessian has, in our Fourier convention, the already established decomposition

    K_hat_(mu nu)(p)
       = beta [delta_(mu nu) sum_rho d_rho(-p)d_rho(p)
                         -d_mu(-p)d_nu(p)] + O(p^3),
    d_mu(p)=exp(i p_mu)-1,
    K_hat(p)=sum_x exp(-i p.x) K(x),                      (8.4)

then its coefficient is fixed without ambiguity by

    beta = -partial_mu partial_nu K_hat_(mu nu)(0)
         = sum_x x_mu x_nu K_(mu nu)(x),       mu!=nu,
    beta = (1/2) partial_nu^2 K_hat_(mu mu)(0)
         = -(1/2) sum_x x_nu^2 K_(mu mu)(x),   mu!=nu.    (8.5)

These are derived from (8.4), not claimed as an exact transcription of the paper's trace and orientation conventions. Color generators must be normalized once, and any overall action factor must be retained when matching the paper's beta. Full point-group symmetry makes the choices of distinct indices agree; that is an assumption of (8.4), not a consequence of analyticity alone. For SU(2) there is one invariant symmetric color form; for a general semisimple group there can be distinct coefficients on distinct simple factors.

## 9. Two concrete norm inputs available for adapting the algorithm

### 9.1 Fixed-order mixed kernel bounds from the present activity norm

Suppose the current graph is partitioned into fixed-size cells with `D` scalar coordinates per cell. Let connected `H` carry an analytic coefficient `E_H` on the scalar product radius b, with

    sup_i sum_(H contains i) exp(a0 |H|) ||E_H||_b <= epsilon,
    a0>0.                                               (9.1)

For each fixed n and each `0<sigma<a0`, the total tensor `K_n=D^n sum_H E_H(0)` has an absolutely summable anchored mixed-coordinate kernel with a positive exponential tree weight, uniformly in volume. This conclusion does not require arbitrary cardinality reserve.

To check the dimension count, one H has `m=D|H|` scalar variables. Coordinate Cauchy gives

    sum_(|alpha|=n) |c_(H,alpha)|
       <= binom(m+n-1,n) b^(-n)||E_H||_b,
    sum_(j1,...,jn) |D^n E_H(0)_(j1,...,jn)|
       <= (D|H|+n)^n b^(-n)||E_H||_b.                   (9.2)

The second bound follows by multiplying the first by n!. Fixing one tensor coordinate can only reduce the sum. Its cell belongs to H whenever the derivative is nonzero. Because H is connected, the graph Steiner length of its derivative slots is at most `|H|-1`. Consequently

    sup_i sum_(j2,...,jn)
       exp[sigma tau({i,j2,...,jn})] |K_n(i,j2,...,jn)|
       <= b^(-n) C(n,D,a0-sigma) epsilon,               (9.3)

where one may take

    C(n,D,c)=sup_(m>=1) (Dm+n)^n exp(-cm) < infinity.

Here scalar/color indices within a cell are included in the sums. Any additional fixed polynomial moment of the diameter is handled by the same unused `a0-sigma` reserve. On cells of side J in current lattice units, passing to the current-site metric costs fixed J-dependent constants and replaces sigma by a smaller positive constant of order sigma/J. J is fixed before refinement; no factor counting all original fine bonds occurs.

Thus the quadratic, cubic and quartic **total** kernels, and every fixed spatial moment needed by a low-order Taylor subtraction, already have a suitable boundedness input. What remains is their Ward-compatible extraction/localization, not an unproved dimension-free absolute Taylor norm at every order. Equations (9.2)–(9.3) are fixed-order statements and deliberately retain the scalar-coordinate count.

### 9.2 Uniform first-gradient Hölder control of an ordinary prefix

Here is a useful elementary refinement of the existing ordinary-trajectory estimate. Let the original fine spacing be eta and a prefix output spacing be h. Write

    P_h(A)=(i h)^(-1) log M_ell^k(exp(i eta A)).          (9.4)

The proved trajectory result supplies a common supremum ball on which `P_h` is uniformly bounded and holomorphic into bounded physical potentials, independently of k,h and compatible volume. On a smaller ball, Banach Cauchy therefore bounds `DP_h` and `D^2P_h` as supremum-norm operators. The nested centered hierarchy makes `P_h` commute with translations by every vector in `h Z^d`. This assertion does not require commutation with a nonaligned fine translation.

Let `A` have physical `C^(1,alpha)` norm at most b, `0<alpha<1`. For a coordinate translation `T_h`,

    nabla_h P_h(A)
      = integral_0^1 DP_h(A+t(T_h A-A)) nabla_h A dt.    (9.5)

The fine `nabla_h A` is the average of the fine nearest-neighbor gradient along a segment, so it has supremum and Hölder seminorm at most those of the original gradient. Translate (9.5) by another aligned vector z and subtract. The change in its direction is at most `C b |z|^alpha`; the change in its derivative operator is at most `C ||T_z A-A||_infinity`, by the `D^2P_h` bound. After multiplication by `||nabla_h A||`, this is at most `C b^2 |z|`, hence at most `C b^2 |z|^alpha` for `|z|<=1`. For larger z the supremum bound suffices. The same argument works with lifted distances on a periodic regulator. Therefore

    ||P_h(A)||_(C^(1,alpha)) <= C (b+b^2),               (9.6)

uniformly in prefix length. All interpolation arguments stay in the common convex supremum ball. The equality (9.5) also proves holomorphy into the complete output `C^(1,alpha)` space on a smaller input `C^(1,alpha)` ball.

Apply this to the already proved ordinary representative `A_o,MR(w)` and set `h=1/R`. In current-unit coordinates the pre-gauge angle is `B_h=h P_h(A_o,MR(w))`. Its nearest-neighbor differences satisfy

    ||B_h||_infinity <= C b h,
    ||Delta B_h||_infinity <= C b h^2,
    ||Delta Delta B_h||_infinity <= C b h^(2+alpha).       (9.7)

The last estimate is the first-gradient Hölder difference, not a claim of a mesh-uniform second classical derivative. This matches the scaling pattern used at CMP109 (4.17)–(4.18). Banach-valued Cauchy in a coarse direction yields the corresponding linearized bounds, after a fixed radius loss. A further strict-support version can be obtained by applying the existing Banach-output local vertex lemma to (9.4) with the `C^(1,alpha)` output norm; it is not needed merely for (9.7).

### 9.3 An exact discrete Taylor identity with explicit orientation

This identity is derived here so that no unreadable sign or endpoint in the scan's (4.30) is guessed. On the current unit lattice set `D_nu f(v)=f(v+e_nu)-f(v)`. Choose any fixed shortest coordinate path Gamma from x to y. For each traversed edge e, let `nu(e)` be its positive coordinate direction, `v(e)` its lower endpoint in that direction, and `s(e)=+1` or `-1` its traversal orientation. Then

    f(y)-f(x)
      = sum_nu (y_nu-x_nu) D_nu f(x) + Rem_xy(f),
    Rem_xy(f)
      = sum_(e in Gamma) s(e)
                 [D_(nu(e))f(v(e))-D_(nu(e))f(x)].       (9.8)

This follows by telescoping the first sum over edges and using `sum_(e:nu(e)=nu) s(e)=y_nu-x_nu`. In particular a negative traversal uses the positive difference at its **lower** endpoint; replacing that endpoint by the traversal's initial vertex changes the formula.

Let n be the path length. Comparing each positive difference along another shortest path gives

    |Rem_xy(f)| <= n^2 max_(nu,rho,v) |D_rho D_nu f(v)|. (9.9)

If `f=B_h` from (9.7), the stronger gradient Hölder estimate gives

    |Rem_xy(B_h)| <= C b h^(2+alpha) n^(1+alpha).       (9.10)

The corresponding first-order freezing bound is `|B_h(y)-B_h(x)|<=C b h^2 n`. All polynomial path moments are summable against (9.3).

The power counting needed after Ward conversion is now explicit: a fourth-field-degree freezing error has four amplitude factors with one `h` replaced by `h^2`, hence `h^5`; a third-field-degree Taylor remainder has two `h` factors and one `h^(2+alpha)`, hence `h^(4+alpha)`; a quadratic remainder with three spatial differences can be placed in a one-plus-two split, giving `h^2 h^(2+alpha)=h^(4+alpha)`. A four-dimensional volume sum contributes `h^-4`, leaving a positive `h^alpha` gain. These are bounds for the indicated algebraically produced terms; the assertion that **all** low-degree terms have been converted to that list still requires the Ward/extraction proof in Section10.

## 10. Exact next mathematical target, with what is still open

The primary algorithm suggests the following new proposition, rather than an unconditional citation import:

*Start with a gauge-invariant total analytic correction whose fixed-order kernels obey (9.3), whose actual finite-regulator symmetries give the Maxwell classification, and whose evaluation is on the pre-gauge fields satisfying (9.7). Construct a scalar beta by (8.5), subtract the full appropriately normalized Wilson action, and localize the remaining scalar functional with a controlled connected-carrier norm. Prove a scale gain `R^(-alpha)` (or another positive power) for its low-field-degree, higher-spatial-order sector, together with the already proved high-field-degree contraction.*

Three interfaces remain substantive:

1. **Localization after total Ward cancellation.** The total identities (8.2) do not assert them for every canonical H. A bounded local construction must preserve the cancellations without demanding the false implication that a total invariant sum has invariant summands. Group averaging on the full compact gauge group is not automatically legal on our original small product ball.
2. **Periodic/infinite-volume extraction.** The source removes remote boundaries before taking the momentum representation. Our finite-regulator coefficient functions may depend on the fixed regulator. One must construct an appropriate infinite-lattice kernel, or prove a finite periodic extraction with controlled wrapping errors and uniform constants. Bounds alone do not prove convergence or volume consistency.
3. **The relevant/marginal recursion.** Even a bounded Wilson-compatible extraction does not determine the sign of its actual one-loop coefficient, the uniformly small accumulated remainder, or the source's averaged positive drift for the composite one-shot cutoff. These are the remaining amplitude/trajectory estimates. The one-shot integral is not identified with repeated primitive integrals by composition of its constraint alone.

These targets use the published proof's structure and the existing homogeneous analytic estimates without asserting that the entire CMP109/CMP116 induction theorem has already transferred to our map.
