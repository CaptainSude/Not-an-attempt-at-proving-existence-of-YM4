# Global four-layer source route: defining equations and a two-input reduction

Research checkpoint, 2026-10-16. Repository pinned at `e392ef45013a581664bab76b90867170b30fe10e`, checked with `git rev-parse HEAD`. All numbered raw references below are one-based lines in `work/Yang--Mills-LLM-experiment/theorem_0_complete_account_raw_I.tex`, unless Raw II is specified. This note does not edit or certify the deposited account. Its proved reductions are conditional on the explicitly listed operator bounds; identification with the selected global layer remains open where stated.

## 1. The selected route and its actual interface

The selected construction uses four global layers on determining sets, not the three localized maps of CMP122-II(1.61)–(1.63). Raw I73545–73576 specifies the global layers and expressly excludes the localized scaffolding; 73124–73140 describes the stage induction. At stage s it assumes the carrier pair `(W_s,J_s)` is in the admissible class and the two-input argument is smaller than `εsharp`; it then invokes the layer theorem and corollary, applies localization, checks the presentation entries, and obtains the next carrier's membership.

The notation is explicit at94308–94311:

\[
 \mathbb H[\mathfrak B;(W,J);\sigma;(\mathfrak j,b)],
 \qquad \mathfrak s^\sharp_\sigma[\mathbb H].
\]

Here `(W,J)` is the background pair, `𝔧` is a field/current datum, and `b` is block data. These three roles must not be conflated. Raw II5716–5718 gives the third layer both a first datum `f_1` and block data supported in the shell. Raw I73108–73112 describes that first datum as `𝔧_3=G̃_0(σ)𝒥_3`.

Raw I110264–110276 defines the carrier

\[
\mathfrak K_{109}(\mathfrak B;\gamma_0)=
\{(W,J):W=e^{i\eta a}U,\quad U\text{ satisfies CMP99b(3.35)},
\quad a\text{ satisfies CMP99b(3.37)},\quad
\sup\ell^3|J|\le\gamma_0\}.
\tag{1}
\]

The current is an independent complex one-form. Membership does not say that it is the physical current of W. Raw I94244–94248 reports the smallness conditions `Knatural(γ_0+ε_3)≤1` and `εsharp=ε_3/(4Ksharp)`. Checking these numerical inequalities is not a construction of the operator they license.

The earlier explicit chart is defined on `𝔖`, Raw I12946–12970, with the same kinds of background hypotheses and possibly smaller radii. Comparing these domains requires comparing the constants and determining-set geometry; notation alone does not prove they agree.

## 2. What is actually located for the six clauses

The layer theorem is invoked with clauses `(a)–(f)` at72392–72399 and elsewhere. The following is a reconstruction **from use sites**, not a recovered full theorem statement.

| Clause | Substance licensed by the located use | Exact use sites |
|---|---|---|
| (a) | Joint analyticity, the unique small solution, zero solution at zero datum | 72512–72516; 72846–72849; 94489–94515 |
| (b) | Weighted Lipschitz bounds for the layer and associated objects | 72521–72536; 94525–94542; 112589–112604 |
| (c) | Gauge covariance | 95762–95767 |
| (d) | Identification with the real, undecoupled Bałaban construction | 72410–72411; 95762–95767; 131690–131692 |
| (e) | Not recovered in this audit | No assertion about its content or absence |
| (f) | Separation over decoupled components, including auxiliary fields | 72500–72516; 72831–72849 |

There is also a source-containment theorem at site `(L)` referred to as having six clauses, e.g.89965–89979. It must not silently be identified with this layer theorem. The wrapped-holomorphy lemma72988–73001 explicitly takes the `(T)`, `(P)`, and `(L)` containment statements, inheritance, and arrested-term bookkeeping as hypotheses. Its extension to other exempt sets does not prove those input statements.

The crucial strength of clause (b) is visible at112589–112604: it controls differences in

\[
 \|\delta A'\|^\Delta_p,\quad
 \|\delta\mathbb H\|^\Delta_p,\quad
 \|\delta X\|_p,\quad
 \|P_1(\sigma)\delta A'\|_p,\quad
 \|\mathfrak m_H(\sigma)\delta X\|_p.
\tag{2}
\]

The first graph norm includes `ℓ³|Δ_WδA′|` (111408–111435). The field datum is also required in a graph norm:72532–72535 invokes a separate field-datum lemma giving

\[
 \|\mathfrak j\|^\Delta_p
 \le K_\sharp\|\mathsf J\|_p,
 \qquad \mathfrak j=\widetilde G_0(\sigma)\mathsf J.
\tag{3}
\]

Thus an arbitrary field datum small only in a first-derivative norm is not the stated global hypothesis. This observation narrows the matching problem; it does not prove (3).

## 3. An explicit chart that is available

Raw I13585–13676 defines, at an admissible background,

\[
 \Delta_a=\Delta+D_WR D_W^*+Q^*aQ,\quad
 G_0=\Delta_a^{-1},\quad q_0=(QG_0Q^*)^{-1},
\]
\[
 H_0=G_0Q^*q_0\ell^{-1},\quad
 P_0=I-G_0Q^*q_0Q,\quad \bar G=P_0G_0=G_0P_0^T.
\tag{4}
\]

In particular `QḠ=0`, `Δ_aḠ=P_0^T`, and `Δ_aH_0b=Q^*q_0ℓ^{-1}b`. Raw I13723–13739 defines the free-current operators `H^J`, `Θ_J`, and

\[
 G=\widetilde G^J=(I-\bar G\Theta_J)^{-1}\bar G.
\tag{5}
\]

The nonlinear block correction is `X=D^J(P)`, and the layer variable in this chart is `H=P-H^J D^J(P)` (13980ff;14396–14401). Its block-only fixed point is

\[
 A_0=G[\Theta_JH_0b-V'(A_0+H_0b)].
\tag{6}
\]

Crucially,14425–14429 says the inhomogeneous current term in CMP102b(143) was removed. Thus (6) is not by itself the defining two-input global equation.

At complex decoupling parameters, K10 defines the corresponding chart using decoupled primitive walk expansions and the displayed form (6),15306–15314. It explicitly reserves the exact representation identities for `σ=1`,15338–15339. We may use its analytic norm bounds for complex σ, but not insert undecoupled inverse identities without a proof.

The primitive Green-function bounds are cited from CMP99b. The inverse block covariance and its walk expansion are explicitly cited without a reproduced proof,13624–13627 and13674–13676. The analytic averaging input is also cited at13175–13195. The next result therefore does not remove those dependencies.

## 4. Proved conditional two-input extension and response formulas

Fix one admissible `(W,J,σ)` and the actual coefficients of K10. Write E for its field space with norm N, F for the forcing space with norm `|·|_{(-3)}`, and B for block data. Assume the bounds claimed for those coefficients:

\[
 \|G\|_{F\to E}\le g,\quad \|H_0\|_{B\to E}\le h,
 \quad\|\Theta_J\|_{E\to F}\le\theta,
 \quad |V'(P)|_F\le cN(P)^2\quad(N(P)<\varepsilon_3).
\tag{7}
\]

These are the J5/J6, quadratic-gradient, and K10 bounds at13775–13782,14266–14287,15322–15331. Define a two-input extension of this explicit chart by

\[
 A_0=-j+G[\Theta_JH_0b-V'(A_0+H_0b)],
 \quad P=A_0+H_0b.
\tag{8}
\]

Set `L=(I+GΘ_J)H_0`, `l=h(1+gθ)` and `d=N(j)+l|b|`. Choose `2r<ε_3`, `8gcr≤1`, and `d≤r/2`. Then (8) has a unique solution with `N(P)≤r`, jointly holomorphic on the strict input domain, and

\[
 N(P)\le2d,\qquad N(H)\le4d.
\tag{9}
\]

**Proof.** Equation (8) is `P=-j+Lb-GV'(P)`. Cauchy's estimate applied to the quadratic bound on the ball of radius `2r` gives `\|V''(P)\|≤4cr` for `N(P)≤r`. Therefore its right side is a contraction with constant at most `1/2` and maps the radius-r ball into the radius-`5r/8` ball. Picard iteration proves existence, uniqueness, and joint holomorphy on each strict parameter domain. Since `V'(0)=0`, the contraction estimate gives `N(P)≤d+(1/2)N(P)`. The nonlinear-correction estimate `N(P-H^JD^J(P))≤2N(P)` gives the second bound. This estimate is part of the earlier correction lemma and must be included among the coefficient assumptions. ∎

For an admissible weight ρ, assume the **whole-ball** K8 estimate

\[
 \sup_{N(P)\le r}\|GV''(P)\|_{E_\rho\to E_\rho}\le\tfrac12,
 \qquad \|L\|_{B_\rho\to E_\rho}\le l_\rho.
\tag{10}
\]

This is the type of estimate proved at14841–14866 and14952–14969, not an estimate only on existing block-only solutions. Subtracting (8) at two data and integrating the Hessian on the segment gives

\[
 N_\rho(P_1-P_2)
 \le2\{N_\rho(j_1-j_2)+l_\rho|b_1-b_2|_\rho\}.
\tag{11}
\]

With

\[
 R_P=(I+GV''(P))^{-1},\qquad
 T_P=I-H^JD^{J\prime}(P),
\]

the exact derivatives are

\[
 D_jP=-R_P,\quad D_bP=R_PL,\qquad
 D_jH=-T_PR_P,\quad D_bH=T_PR_PL.
\tag{12}
\]

If the first datum is specifically `j=Gf`, then `D_fH=-T_PR_PG`. This is a current-response kernel, with the same exponential weights as the supplied primitive and Hessian bounds. It is not merely a block derivative renamed as a current derivative. It establishes the required analytic two-input mechanism in the earlier chart's norms. Matching its first-input convention to the global `G̃_0(σ)𝒥` still requires the latter's actual definition; the similar tildes are insufficient.

Component locality follows for this extension if its coefficients separate over the decoupled components and the first datum does also. Indeed every Picard iterate then separates, and its uniform limit does. Arbitrary nonlocal j would not have this property.

## 5. A genuine elliptic improvement at σ=1

Here keep the undeformed definitions (4)–(5), and take `j=Gf`. The resolvent identity gives `G=Ḡ+ḠΘ_JG`, hence

\[
 \Delta_aG=P_0^T(I+\Theta_JG),
 \qquad
 \Delta_aL=Q^*q_0\ell^{-1}+P_0^T\Theta_JL.
\tag{13}
\]

Equivalently, (8) becomes `P=H_0b+Ḡ[-f+Θ_JP-V'(P)]`. Applying `Δ_a` yields the exact, forced representation

\[
 \boxed{\Delta_aP=P_0^T[-f+\Theta_JP-V'(P)]+Q^*q_0\ell^{-1}b.}
\tag{14}
\]

This proves an augmented elliptic bound without differentiating f. For two solutions in the radius-r ball, put `p_ρ=\|P_0^T\|_{F_ρ\to F_ρ}`, `q_ρ=\|Q^*q_0ℓ^{-1}\|_{B_ρ\to F_ρ}`, `θ_ρ=\|Θ_J\|_{E_ρ\to F_ρ}`, and `v_ρ=sup\|V''(P)\|_{E_ρ\to F_ρ}`. Then

\[
 |\Delta_a\delta P|_{F_\rho}
 \le p_\rho|\delta f|_{F_\rho}
 +p_\rho(\theta_\rho+v_\rho)N_\rho(\delta P)
 +q_\rho|\delta b|_{B_\rho}.
\tag{15}
\]

Together with (11), this closes the `Δ_aP` response estimate conditional on the listed kernel norms. No regularity of `D_W^*f` is required. The result is more than a generic missing-lemma criterion: it is an identity for the specific chart operators in the deposit.

There are two limits to this improvement. First, `Δ_a` includes the gauge-fixing and block terms in (4); it is not simply the covariant Laplacian `Δ_W` in (2). The relation `Δ_a=ℒ-D_WPD_W^*`, with `ℒ=Δ(W)+D_WD_W^*+Q^*aQ`, is displayed at25328–25336. Obtaining the desired covariant Laplacian from (15) requires the bounds for this operator difference, not an assumption that the symbols mean the same thing. Second, the layer is `H=P-H^JX`. Control of `Δ_aP` alone gives no bound for the second-order image of `H^JX`. The raw account expressly withholds those general-free-current Laplacian estimates at13763–13774 and15119–15141.

At complex σ, (13) is not supplied by K10. One must either estimate the decoupled differentiated walk kernels directly, or prove the necessary exact/residual identities and bound their residuals. The fact that every original kernel is an inverse before walk decoupling is not a proof that its decoupled sum remains that inverse.

## 6. Keep the partner-current identity separate

For the explicit forced chart at σ=1 define `Ξ_f=Θ_JP-V'(P)-f` and, using the same operators as14402–14408,

\[
 \Lambda_f=P_0^T\Xi_f+Q^*(q_0-a)\ell^{-1}b
       -Q^*\mathsf k X-\Lambda^T\mathfrak j_J(H^JX),
\]
\[
 \mathcal J_f=\Lambda_f-\Delta'H+F(W,H),
 \qquad \Delta'=\Delta-D_W^*D_W.
\tag{16}
\]

Its norm can be bounded using first-order chart estimates, the supplied lower-order/block operators, and the direct forcing term. It vanishes at `(f,b)=(0,0)`. Using (14) and `QP=ℓ^{-1}b`, the exact algebraic representation is

\[
 \mathcal J_f=(\Delta_a-Q^*aQ-\Delta')P
 -\{Q^*\mathsf kX+\Lambda^T\mathfrak j_J(H^JX)-\Delta'H^JX\}+F(W,H).
\tag{17}
\]

These are the forced versions of14405–14408 and14444–14447. They do not assert that `J+𝒥_f` is the actual physical current for arbitrary independent `(W,J,f)`.

The selected global layer has a different displayed representation at111397–111401:

\[
 \mathfrak s^\sharp_\sigma[\mathbb H]
 = (\Delta_W-P_1(\sigma)+\mathsf K)A'
   -\mathfrak m_H(\sigma)X+F(W,\mathbb H).
\tag{18}
\]

Solving (18) for `Δ_WA′` would give the desired estimate if the partner current and remaining terms had independent bounds. But the proof at111420–111443 bounds the partner current **using** the Laplacian and other entries in (2). Likewise94993–94995 uses the layer bound to estimate the current rider. Reversing those particular arguments is circular. A valid completion must identify (16) with the global partner, or provide an independently controlled global current representation.

For the selected data, cancellation is justified at true, undecoupled constrained minimizers:15767–15774 proves `J∈range Q^*`, hence `P_0^TJ=0`. It is not justified at arbitrary members of (1). The actual current-localization lemma92401ff preserves the correction

\[
 [G''(\sigma)-G''(1)]Q''^*(\lambda_2|_{D_2^\circ})
\tag{19}
\]

when it localizes the third layer's first datum. Dropping (19) would incorrectly carry undecoupled current annihilation to general complex σ. This lemma localizes the first slot; it does not by itself establish the stronger operator identities needed in (2).

## 7. Primary-source check and next exact obligation

An ordinary public link supplied the original CMP109 article, DOI10.1007/BF01215223: [original PDF hosted by SciSpace](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf). At pp.272–273, equations(3.11)–(3.16), Bałaban explains the problematic second-order current term, the Landau-gauge cancellation at the original minimizer, replacement by a covariant Laplacian plus projection and lower-order terms, and the second-order norms needed for analytic substitution. The OCR is imperfect; no claim here depends on recovering a disputed symbol from it. This is corroboration of the operator distinction, not proof of the deposited independent-current extension.

The next concrete obligation is consequently smaller and sharper than rebuilding the entire source induction: give the defining two-input equations for the selected global layer, match their first-slot convention and partner current to (8)/(16) or a verified alternative, and show how the graph bounds (2) follow on (1), including complex σ. The earlier chart already supplies a conditional two-input contraction, weighted resolvent response, and the exact undeformed elliptic identity (14). The uncompleted interface is the full covariant-Laplacian/partner-current control of the actual global objects. Neither a named invocation nor the older chart's shorter list of norms discharges that interface.

A potentially narrower repair is to change the consumer interface. If every use of (2) requires only the complete current combination (18), an independently bounded substituted expression of the form (16) can control that sum without estimating all its second-order pieces separately. One must check all consumers, especially cut-layer commutators, and preserve component locality and the actual carrier membership. The earlier chart demonstrates why this may work, but does not yet prove that the global proof can be rewritten that way. Independent-current data cannot be assigned the true-pair Landau identity merely to simplify this step.

This audit has not found a standalone full statement and proof of all six global-layer clauses. That is an unresolved source identification, not proof that no such statement occurs elsewhere or that an unpublished companion argument cannot supply it.

## 8. Exact simplification of the actual cut-current consumer

The proposed weaker interface survives the algebra of the cut-layer definition, not merely the uncut current. Set `L_σ=Δ_W-P_1(σ)+𝕂`, `Y=H(σ)X`, and let `s=L_σA′-𝔪_H(σ)X+F(W,H)` be the current in (18). The actual cut current,111542–111543, is

\[
 J^\sharp[\chi]=L_\sigma(\chi A')-\chi\mathfrak m_H(\sigma)X
 -[D_W^*D_W,\chi]Y+F(W,\chi H).
\]

Subtracting `χs` gives the exact identity

\[
 \boxed{J^\sharp[\chi]=\chi s+[L_\sigma,\chi]A'
 -[D_W^*D_W,\chi]Y+F(W,\chi H)-\chi F(W,H).}
\tag{20}
\]

The `𝔪_H X` term cancels. Thus this particular consumer can be estimated from an independent bound on the **combined** current s, first-order bounds on `A′,H,Y`, and commutator bounds, without separate second-order norms on `A′` and Y. This is an exact reduction of a stated map obligation, not yet a proof that all other consumers admit the same reduction.

The projection commutator has an especially simple bound. If the actual `P_1(σ)` belongs to `𝒦_{-2}` with constant C and rate δ in13405–13409, and `χ=t+s_0χ̂` with `|χ̂|≤1`, then `[P_1(σ),χ]` belongs to that same kernel class with constant at most `2|s_0|C`. Indeed the constant t commutes, and for input supported in a block both `P_1(χ̂f)` and `χ̂P_1f` satisfy the same block estimate. The kernel-algebra bound13433–13437, with `α=-1`, gives

\[
 |[P_1(\sigma),\chi]A'|_{(-3),\rho}
 \le2|s_0|CL^{d+4}c_1|A'|_{(-1),\rho}.
\tag{21}
\]

This incurs no fine-lattice derivative of `A′` or of the independent current. At σ=1, `P_1=D_WPD_W^*∈𝒦_{-2}` is explicitly quoted at13569–13580. At general complex σ, the corresponding actual differentiated/decoupled kernel estimate still must be identified or established; it is not obtained by merely differentiating the norm of `P(σ)`.

For the local pieces, `[Δ_W,χ]A′` and `[D_W^*D_W,χ]Y` require first-order product-rule bounds with the cutoff's first and second differences, plus any curvature terms in the chosen covariant convention. Raw I111597–111612 supplies exact product rules;111615 marks its particular coefficient-count proof incomplete. Equation (20) does not certify those advertised numerical constants. It does show that fixing that local estimate need not reintroduce a full `Δ_WY` estimate. The independent substituted bound for s, and matching it to the global layer, remain the decisive prerequisites.
