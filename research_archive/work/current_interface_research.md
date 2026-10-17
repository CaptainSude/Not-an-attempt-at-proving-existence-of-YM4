# Current interface: a completed local estimate and the remaining global match

Research note, 2026-10-16. The deposited repository is pinned at `e392ef45013a581664bab76b90867170b30fe10e`. References `I:L` denote one-based lines of `theorem_0_complete_account_raw_I.tex`. The preceding note is `work/global_layer_research.md`. No repository or output files were edited. Statements proved below concern the displayed operators and explicitly stated hypotheses; they do not certify the global source induction.

## 1. The local coefficient count can be completed

We use exactly the covariant difference convention displayed at I:111491–111501. Write

\[
 (T_\mu B)(x)=R_{x,\mu}B(x+\eta e_\mu),\qquad
 (T_\mu^{-1}B)(x)=R_{x-\eta e_\mu,\mu}^{-1}B(x-\eta e_\mu),
\]
\[
 \nabla_\mu=(T_\mu-I)/\eta,\qquad
 \nabla_\mu^*=(T_\mu^{-1}-I)/\eta.
\tag{1}
\]

The second equality is the bilinear transpose, not a Hermitian adjoint after complexification. For an adjoint-group transport, invariance of the bilinear trace form gives `R^T=R^{-1}`, including at complex W. Suppose on the relevant stencil

\[
 \max(\|R_{x,\mu}\|,\|R_{x,\mu}^{-1}\|)\le\tau.
\tag{2}
\]

For a scalar χ set `a_ν=∂_νχ`, where `∂_νχ(x)=[χ(x+ηe_ν)-χ(x)]/η`, and let `∂^-_μ` be the backward difference. Multiplication by a scalar function is written without an operator symbol. The exact product rules are

\[
 [\nabla_\nu,\chi]=a_\nu T_\nu,\qquad
 [\nabla_\mu^*,\chi]=-(\partial^-_\mu\chi)T_\mu^{-1},
\tag{3}
\]
\[
 \nabla_\mu^*(a_\nu T_\nu B)
 =a_\nu\nabla_\mu^*T_\nu B
  -(\partial^-_\mu a_\nu)T_\mu^{-1}T_\nu B.
\tag{4}
\]

The useful identity, valid without commuting any covariant shifts, is

\[
 \boxed{\nabla_\mu^*T_\nu B
 =T_\mu^{-1}\nabla_\nu B
  -T_\mu^{-1}\nabla_\mu B-\nabla_\nu B.}
\tag{5}
\]

To check it, multiply by η and use `η∇_ν=T_ν-I` and `T_μ^{-1}T_μ=I`. The right side becomes `T_μ^{-1}T_νB-T_νB`, exactly the left side. This avoids a curvature commutator altogether. In the diagonal case there is the sharper identity `∇_μ^*T_μB=-∇_μB`.

Fix x. Let `g` be the supremum of all `|∇_αB_β|` on the one-step base-point stencil about x, and let `b` be the supremum of `|B_β|` there. Let `s_1` bound the first forward and backward differences of χ at the points appearing in (3)–(4), and `s_2` bound `|∂^-_μ∂_νχ|` there. The field arguments in the formulas are x, `x-ηe_μ`, `x+ηe_ν`, and `x-ηe_μ+ηe_ν`; they all lie in the ℓ∞ stencil of radius η. All transport bounds in (2) are read on the links used by these formulas.

For a mixed pair of indices, (3)–(5) give

\[
\begin{aligned}
 [\nabla_\mu^*\nabla_\nu,\chi]B
 ={}&a_\nu\{T_\mu^{-1}\nabla_\nu B
             -T_\mu^{-1}\nabla_\mu B-\nabla_\nu B\}\\
 &-(\partial^-_\mu a_\nu)T_\mu^{-1}T_\nu B
   -(\partial^-_\mu\chi)T_\mu^{-1}\nabla_\nu B.
\end{aligned}
\tag{6}
\]

Consequently

\[
 |[\nabla_\mu^*\nabla_\nu,\chi]B|
 \le(1+3\tau)s_1g+\tau^2s_2b.
\tag{7}
\]

For the diagonal pair the exact formula simplifies to

\[
 [\nabla_\mu^*\nabla_\mu,\chi]B
 =-a_\mu\nabla_\mu B
  -(\partial^-_\mu a_\mu)B
  -(\partial^-_\mu\chi)T_\mu^{-1}\nabla_\mu B,
\]
\[
 |[\nabla_\mu^*\nabla_\mu,\chi]B|
 \le(1+\tau)s_1g+s_2b.
\tag{8}
\]

Under the antisymmetric two-form pairing used by the displayed D and D*,

\[
 (D_W^*D_WB)_\nu
 =\sum_{\mu\ne\nu}
   (\nabla_\mu^*\nabla_\mu B_\nu
    -\nabla_\mu^*\nabla_\nu B_\mu).
\]

Adding (7) and (8) for each μ proves

\[
 \boxed{|([D_W^*D_W,\chi]B)_\nu(x)|
 \le(d-1)\{(2+4\tau)s_1g+(1+\tau^2)s_2b\}.}
\tag{9}
\]

For `1≤τ≤5/4`, `1+τ²≤2+4τ`, so the raw account's advertised constant is valid:

\[
 |[D_W^*D_W,\chi]B|
 \le c_d(s_1g+s_2b),\qquad
 c_d=(2+4\tau)(d-1).
\tag{10}
\]

In particular `c_d=18` in d=4 at unitary W, and `c_d≤21` when `τ≤5/4`. Equations (4)–(8) fill the coefficient-count step explicitly marked incomplete at I:111615–111628. They use no bound on `D_W^*J`, no second derivative of B, and no derivative of the curvature. They establish the local estimate for the precise displayed transport convention; a different convention must first be related to this one.

For the standard covariant Laplacian `Δ_cov=Σ_μ∇_μ^*∇_μ`, (8) also gives

\[
 |[\Delta_{\rm cov},\chi]B|
 \le d\{(1+\tau)s_1g+s_2b\}.
\tag{11}
\]

This applies to the `Δ_W` part of the global current when that symbol has this covariant-Laplacian convention. If a different convention includes an additional local lower-order operator, its commutator must be added; it should not be silently omitted.

### 1.1 Complex backgrounds

Use the matrix operator norm for the exponent, and the induced norm on the Lie algebra for Ad (the latter may be induced by Hilbert–Schmidt norm). If `W(b)=exp(iηa(b))U(b)` with U unitary, then

\[
 \|\operatorname{Ad}_{W(b)}\|,
 \|\operatorname{Ad}_{W(b)}^{-1}\|
 \le e^{2\eta\|a(b)\|}.
\tag{12}
\]

Here the norm on the right side of (12) is explicitly the matrix operator norm. This follows from `||e^M||≤e^{||M||}` and the two matrix factors in conjugation. Thus `ηsup||a||op≤1/10` implies `τ≤e^{1/5}<5/4`. If instead `|a|` denotes the normalized Hilbert–Schmidt norm explicitly fixed at I:10306, use `||a||op≤√N|a|`: the safe condition is `η√N sup|a|≤1/10`. A fixed-group smallness ceiling can absorb this factor, but it cannot be dropped from a claimed numerical bound. Smallness of the complex twist is sufficient even if the real unitary factor is not close to the identity in the displayed gauge. No positivity or unitarity of the full complex background is needed in (9).

### 1.2 The actual cutoff and scale-uniform constants

The cutoff at I:111522–111529 is

\[
 \chi=t+s\widehat\chi_\square,\qquad
 \widehat\chi_\square(x)=\prod_\mu
 \zeta\bigl((x_\mu-y_{\square,\mu})/(M\ell_\square)\bigr),
\]

where `0≤ζ≤1`, `|ζ′|,|ζ″|≤5`. Integral representations of finite differences yield

\[
 s_1\le\frac{5|s|}{M\ell_\square},\qquad
 s_2\le\frac{25|s|}{M^2\ell_\square^2}.
\tag{13}
\]

The second bound includes mixed differences. Define

\[
 N_y(B)=\max\{\ell_y\sup_{\widetilde\Delta(y)}|B|,
                 \ell_y^2\sup_{\widetilde\Delta(y)}|\nabla_WB|\}.
\]

For a bond based in Δ(y), whose required stencil is contained in `Δ̃(y)`, (9) gives the more informative scale-dependent inequality

\[
\begin{aligned}
 \ell_y^3|[D_W^*D_W,\chi]B|
 \le{}& |s|(d-1)
 \left[(2+4\tau)\frac{5\ell_y}{M\ell_\square}
       +(1+\tau^2)\frac{25\ell_y^2}{M^2\ell_\square^2}\right]N_y(B).
\end{aligned}
\tag{14}
\]

For the actual cover use the geometric implication `Δ̃(y)∩□≠∅ ⇒ ℓ_y≤Lℓ_□` proved from the collar separation at I:111655–111683, with `M≥2L²`, `L≥3`. Then

\[
 \frac{5\ell_y}{M\ell_\square}
 +\frac{25\ell_y^2}{M^2\ell_\square^2}
 \le\frac56+\frac{25}{36}=\frac{55}{36}<2.
\]

The differences vanish when the doubled stencil misses □, by the cutoff support and `Mℓ_□≥18η` as checked at I:111630–111643. Consequently

\[
 \boxed{\ell_y^3|[D_W^*D_W,\chi]B|
 \le2c_d|s|N_y(B)\,
 \mathbf1[\widetilde\Delta(y)\cap\square\ne\varnothing].}
\tag{15}
\]

The corresponding conservative constant in (11) is

\[
 \ell_y^3|[\Delta_{\rm cov},\chi]B|
 \le3d|s|N_y(B)\,
 \mathbf1[\widetilde\Delta(y)\cap\square\ne\varnothing]
\tag{16}
\]

for `τ≤5/4`: `d[(1+τ)5/6+25/36]<3d`. These constants do not depend on η, volume, or the number of RG scales. The cover comparison is an explicit geometric hypothesis of the application, not a consequence of smallness of the field alone. Any block weight can multiply (15)–(16) without changing the local constant.

## 2. What this proves for the actual cut current

Write `L_σ=Δ_W-P_1(σ)+𝕂`, `Y=H(σ)X`, and

\[
 s_\sigma=L_\sigma A'-\mathfrak m_H(\sigma)X+F(W,\mathbb H).
\]

The cut-current definition I:111542–111543 gives the exact identity

\[
\boxed{J^\sharp[\chi]=\chi s_\sigma
  +[\Delta_W,\chi]A'-[P_1(\sigma),\chi]A'+[\mathsf K,\chi]A'
  -[D_W^*D_W,\chi]Y
  +F(W,\chi\mathbb H)-\chi F(W,\mathbb H).}
\tag{17}
\]

The `𝔪_HX` term cancels. Equations (15)–(16) now give the local second-order commutator bounds in (17) from first-order norms. The auxiliary field causes no additional weak-norm demand, because `Y=A′-ℍ` (I:111727–111730), so `N_y(Y)≤N_y(A′)+N_y(ℍ)`.

The remaining projection term is genuinely nonlocal. If the actual `P_1(σ)` has the `𝒦_{-2}` block estimate of I:13405–13409, then `[P_1(σ),χ]` has the same estimate with constant at most `2|s|C`: apply the block bound separately to `P_1(χ̂f)` and `χ̂P_1f`. With the inherited weighted kernel algebra, I:13433–13437, this gives

\[
 |[P_1(\sigma),\chi]A'|_{(-3),\rho}
 \le2|s|CL^{d+4}c_1|A'|_{(-1),\rho}.
\tag{18}
\]

At σ=1, `P_1=D_WPD_W^*∈𝒦_{-2}` is explicitly quoted at I:13569–13580. A general complex-σ bound requires the corresponding differentiated walk estimate; a norm bound on P(σ) alone is insufficient. Preserving the sharper spatial source/cutoff profile uses its kernel with factor `χ(y)-χ(x)`, rather than replacing that factor by its global supremum. Outside the cutoff support this is exactly the kernel tail `P_1(χ̂A′)` already identified at I:112621–112624.

The local lower-order term 𝕂 and the nonlinear F remain the operators appearing in the original current. Their stated bounds, e.g. I:111436–111438,111575 and14126–14130, are in weak field norms. For example, if `|𝕂B|_{(-3)}≤C_KN(B)`, then

\[
 |[\mathsf K,\chi]A'|_{(-3)}
 \le |s|C_K\{N(\widehat\chi A')+N(A')\}.
\]

The product rule gives `N_y(χ̂A′)≤[1+5τℓ_y/(Mℓ_□)]N_y(A′)` on the local stencil. Thus this bound also stays uniform under the same cover comparison. This is conditional on the stated bound for 𝕂; it is not a new proof of that operator's definition or estimate.

Accordingly the cut-current estimate can be proved from an independently bounded **combined** current `s_σ`, weak norms of `A′,ℍ`, the projection-kernel tail, and the existing local 𝕂/F bounds. Separate bounds for `Δ_WA′`, `Δ_Wℍ`, and `𝔪_HX` are not forced by this particular consumer. The local coefficient-count gap has been filled, but the independent combined-current bound remains to be supplied.

## 3. Carrier audit: weak basic domain, additional composite clauses

### 3.1 The actual transcription of CMP99b(3.37)

The deposit defines

\[
 N(A)=\max\{|A|_{(-1)},|\nabla_UA|_{(-2)}\}
\tag{19}
\]

at I:12743–12746. CMP99b(3.37) is transcribed as `N_{U_r}(a)<a_1` at I:12957–12966, and expanded into those same two terms at I:13080–13082. No Laplacian occurs in this condition. The carrier `𝔎_109` at I:110264–110276 adds a regular real unitary factor and the independent current bound `supℓ³|J|≤γ_0`. It does not impose a relation between J and W. The analogous explicit earlier class says so at I:12969–12970.

Thus, for the **basic** carrier, a sufficiently small first-order potential increment and sufficiently small combined current increment are the right quantities. The complex-background perturbation argument at I:15191–15212 uses precisely these: it keeps the real factor fixed, uses a first-order BCH estimate for the twist, and uses the triangle inequality for J. It does not appeal to a second-order current identity.

### 3.2 Located consumers at T, P, and L

| Consumer | What its stated proof currently assumes | What the actual target reads |
|---|---|---|
| T, wrapped holomorphy, I:73014–73047 | The named homogeneous-containment lemma, citing CMP109(3.14),(3.9), and their localized analogues | Membership of the presented pair and a homogeneous analytic response bound; the argument as written uses strong layer estimates, so it must be rewritten before they can be removed |
| T and L, later increment lemma, I:112076–112104,112589–112624 | Four/five separate layer entries, including Laplacian, projection, and auxiliary-current terms | The final increment hypothesis is only `N_y(A″)≤C_inc θ(y)` and `ℓ_y³|J″|≤C_inc θ(y)`, I:111779–111783 |
| T and L, proof of that increment bound, I:112378–112408 | Weak composition for the gauge slot; separate-term current estimates for the current slot | It explicitly concludes only weak potential plus combined current. Equations (15)–(18) show how its local cut step can be replaced once the independent combined-current bound is available |
| P, wrapped holomorphy, I:73049–73066 | The localized stage-space corollary and weighted containment are taken as statements | Simultaneous stage-parameter membership and holomorphy; this passage supplies no independent proof of either stronger or weaker layer bounds |
| P/stage radii, I:116656–116675 | Strong layer norms, plus a separately named local current estimate and bump bounds | The local current slot is already bounded as a whole: `ℓ³|Jsharp[1]|≤2Kχ p`; the provenance of that estimate must be checked if strong norms are removed |
| L, global four-stage induction, I:73068–73140 | Layer theorem, corollary, localization, and current rider at each stage | Carrier/domain membership and one-sixteenth room for the entries. It is not enough to replace the layer theorem's statement without checking the entries of every stored term |
| Later current-closure displacement, I:141777–141813 | Strong response bounds are listed, followed by a combined bound `ℓ³|Jsharp[χ]|≤Kχ(ap+q)` | The displayed displacement estimate for the potential uses only `N_y(χℍ)`; the combined current estimate is the relevant other quantity, but its named recursive input still needs a proof |

There is an important limitation to the weak-domain observation. The full stored domains are richer than `𝔎_109`. The clause vector at I:116925–116934 is

\[
\begin{gathered}
 Q_1=|\partial\mathbb U-1|,\quad
 Q_2=|\partial U_{p,X}(M\!\bullet\mathbb U)-1|,\quad
 Q_3=|\mathbb J|,\quad Q_4=|J_{p,X}(M\!\bullet\mathbb U)|,\\
 Q_5=|\partial U-1|,\quad Q_6=|A'|,\quad Q_7=|\nabla A'|,
\end{gathered}
\tag{20}
\]

with Q8 a cube clause. The composite Q2 and Q4 clauses are imposed at **every retained triple** in the designated family; see I:119480–119484,119695–119702,125591–125608. In particular Q4 is a current of a derived configuration, not simply the independent input J. I:120558 explicitly distinguishes these current slots.

None of these listed domain entries is a separate Laplacian norm. Nevertheless, proving weak basic-carrier membership does not prove all composite-current clauses. A weaker replacement theorem must control the **combined current of each derived map**, with the required level units, weights, and thresholds. The existing strong bounds are one proposed way to do that. This audit has not established that every occurrence of them throughout the source induction is redundant.

## 4. An exact residual identity for the decoupled earlier chart

The remaining mismatch can be given a precise algebraic form. This calculation uses the earlier chart's actual K10 operators. It does not identify them with the later named global layer by notation.

Freeze a background `(W,J)`. Put `D_0=Δ_a-Q^*aQ` and use σ-subscripts on the decoupled operators. Here a is the fixed scale multiplier `ℓ^{-2}`, Q is the background block operator, and `\widetilde b=ℓ^{-1}b`. Consider the forced two-input extension proved in the preceding note, with the specific first datum `j=G_σ f`:

\[
 P=H_{0,\sigma}b+G_\sigma Y,\qquad
 Y=\Theta_\sigma H_{0,\sigma}b-f-V'_\sigma(P).
\tag{21}
\]

Set `Z=Θ_σP-f-V′_σ(P)`. Then exactly

\[
 Z=(I+\Theta_\sigma G_\sigma)Y.
\tag{22}
\]

Define two **explicit operator defects**:

\[
 E_{H,\sigma}=D_0H_{0,\sigma}
              -Q^*(q_{0,\sigma}-a)\ell^{-1},
\]
\[
 E_{G,\sigma}=D_0G_\sigma
              -P_{0,\sigma}^T(I+\Theta_\sigma G_\sigma).
\tag{23}
\]

Applying D0 to (21), and then using (22), proves the exact residual equation

\[
 \boxed{D_0P=P_{0,\sigma}^TZ
       +Q^*(q_{0,\sigma}-a)\widetilde b
       +E_{H,\sigma}b+E_{G,\sigma}Y.}
\tag{24}
\]

At σ=1, both defects vanish by the undeformed identities `QG=0`, `Δ_aG=P_0^T(I+Θ_JG)`, `QH_0=ℓ^{-1}`, and `Δ_aH_0=Q^*q_0ℓ^{-1}`. These are identities for arbitrary admissible independent background current J in the earlier chart; no true-pair cancellation was used in deriving (24).

At complex σ, K10 does **not** assert these inverse/projection identities. It decorates primitive walk expansions and does not resum them, I:15277–15314; exactness is reserved for σ=1 at15338–15339. Hence (23) is the correct discrepancy to retain.

For additional bookkeeping, define

\[
 R_H=\Delta_aH_{0,\sigma}-Q^*q_{0,\sigma}\ell^{-1},\quad
 R_G=\Delta_aG_\sigma-P_{0,\sigma}^T(I+\Theta_\sigma G_\sigma),
\]
\[
 C_H=QH_{0,\sigma}-\ell^{-1},\qquad C_G=QG_\sigma.
\]

Then `E_H=R_H-Q^*aC_H` and `E_G=R_G-Q^*aC_G`. This separates failure of the elliptic identity from failure of the exact block constraint. Either defect can occur after the specified walk decoupling.

### 4.1 The discrepancy between substituted and differential current formulas

Let `X=D^J_σ(P)`, `H=P-H^J_σX`, and put

\[
 B_\sigma X=Q^*\mathsf k_\sigma X
       +\Lambda_\sigma^T\mathfrak j_J(H^J_\sigma X).
\]

The directly substituted earlier-chart current is

\[
 J_{\rm sub}=P_{0,\sigma}^TZ
       +Q^*(q_{0,\sigma}-a)\widetilde b
       -B_\sigma X-\Delta'H+F(W,H).
\tag{25}
\]

This formula is bounded using weak chart quantities, provided its listed operators have their asserted bounds. The differential representation built from those same earlier-chart operators is

\[
 J_{\rm diff}=(D_0-\Delta')P
       -(B_\sigma-\Delta'H^J_\sigma)X+F(W,H).
\tag{26}
\]

Subtracting, and using (24), gives

\[
 \boxed{J_{\rm diff}-J_{\rm sub}
       =E_{H,\sigma}b+E_{G,\sigma}Y.}
\tag{27}
\]

This is the exact impediment to using the undeformed representation identity at complex σ **within the earlier chart**. It is not just the observation that an inverse identity might fail.

There is a second identification problem when comparing to the selected global formula. Even if its fields were identified with `(P,X,H)`, its operators would have to match

\[
 L_{\rm global,\sigma}=\Delta_W-P_1(\sigma)+\mathsf K,
 \qquad m_{\rm global,\sigma}=\mathfrak m_H(\sigma).
\]

Writing

\[
 A_\sigma=L_{\rm global,\sigma}-(D_0-\Delta'),\qquad
 M_\sigma=m_{\rm global,\sigma}-(B_\sigma-\Delta'H^J_\sigma),
\]

the comparison would be

\[
 s_{\rm global,\sigma}-J_{\rm sub}
 =E_{H,\sigma}b+E_{G,\sigma}Y+A_\sigma P-M_\sigma X.
\tag{28}
\]

Equation (28) is conditional on the field identification; it states explicitly the further operator identities one would have to prove. The present audit has not recovered a complete defining equation for the named global two-input layer that establishes these matches.

### 4.2 What walk localization does, and does not, immediately give

At fixed lattice spacing and volume, expand the coefficients in either defect (23) using the actual decorated primitive and concatenated walks. The expansion has the form `E_σ=Σ_α m_α(σ)K_α`, where `m_α` is the exact monomial dictated by the chosen products of decorated primitives. Multiplicities in products must be retained. At σ=1, `Σ_αK_α=0`; therefore

\[
 E_\sigma=\sum_\alpha[m_\alpha(\sigma)-1]K_\alpha.
\tag{29}
\]

For fixed finite cutoff this rearrangement is legitimate under the asserted absolute walk convergence, since D0 is then a bounded finite-dimensional operator. It is not a scale-uniform estimate: its naive bound can contain the fine derivative cost in D0.

If all decoupling parameters on an interior region equal one, every nonzero coefficient in (29) has a labelled localization domain meeting a cube outside that region. This explains the possible boundary-distance gain. To obtain it with a cutoff-independent prefactor, however, the coefficients after applying D0 need a differentiated walk bound, or a local parametrix identity that reduces D0 acting on the first walk piece to controlled local terms and the commutators proved above. The ordinary weak kernel bound alone does not establish this. It also does not permit dropping the residual because its value at σ=1 is zero.

The actual current localization retains precisely this kind of issue: I:92401ff includes `[G''(σ)-G''(1)]Q''*λ` instead of extending the annihilation identity to general σ. The residual must remain in the current match unless it is proved to cancel or is estimated. No true-pair Landau identity has been assigned here to arbitrary independent-current data.

## 5. What has advanced

1. The marked local coefficient-count step has an explicit proof with the advertised constants, including complex nonunitary backgrounds and the cutoff's scale normalization.
2. The basic carrier and the concrete later increment target need only weak potential and combined current. The stronger norms are used as a proof interface. The complete stored domains still require derived-current control at all retained triples; this obligation survives the proposed weakening.
3. Equations (23)–(28) isolate the exact complex-decoupling mismatch of the earlier substituted current and then the additional global-operator match. They provide a definite next estimate, rather than assuming the undecoupled identities persist.

The local commutator repair is complete for the stated convention. The global current substitution, differentiated walk control, and composite-domain propagation are not proved by this note.

## 6. Composite Q4: a current reconstruction using only one differentiated kernel

This section concerns the **derived physical current** of an actual constrained critical configuration. It does not concern the independent J slot of the global pair chart. That distinction is essential.

### 6.1 Exact finite-dimensional identity

Fix a retained composite/localized constraint structure s, and a configuration U at which its linearized constraint is Q_s. Include the fixed exterior in the tangent-space convention. Let E_s be any right inverse on the actual constraint space:

\[
 Q_sE_s=I.
\tag{30}
\]

Suppose criticality says that `⟨v,J(U)⟩=0` for every allowed variation v with `Q_sv=0`. The pairings are the same bilinear pairings used to define the transposes, including their fine- and block-lattice measures. Surjectivity in (30) implies

\[
 J(U)=Q_s^T\lambda,\qquad
 \lambda=E_s^TJ(U).
\]

The actual Wilson current is

\[
 J(U)=D_U^TF_U,\qquad
 F_U=\eta^{-2}\pi\operatorname{Im}\partial U.
\tag{31}
\]

This is explicitly transcribed at I:10308–10310 and14086. The D in (31) is the plaquette covariant derivative, not the derivative of the nonlinear block constraint. Multiplying (31) by E_s^T gives the exact identity

\[
 \boxed{J(U)=\mathcal R_s(U)F_U,\qquad
 \mathcal R_s(U):=Q_s^T(D_UE_s)^T.}
\tag{32}
\]

The proof uses `(D_UE_s)^T=E_s^TD_U^T` and no field equation beyond constrained criticality. In particular it does not apply D* to an arbitrary free current or a second derivative to a response field. It is valid after complexification if the stated criticality, surjectivity and transpose identities hold there. Real criticality can identify a holomorphic continuation, but does not by itself give a uniform bound on that continuation.

There is a concrete candidate right inverse in the earlier chart. I:13640 and13650 give `QH_0=ell^{-1}`, so

\[
 E_s=H_{0,s}\ell_s
\tag{33}
\]

has the correct **unscaled** normalization `Q_sE_s=I`, provided Q_s is exactly the Q of that chart for the selected structure. Omitting the multiplication by ell_s would give the wrong identity. The transposes in (32) automatically retain this multiplication on the correct side.

Equivalently, if the linearized constraint is normalized as `ell_s Q_s`, its right inverse is H_0 itself. The composite operator (32) is unchanged. More generally, replacing `(Q,E)` by `(SQ,ES^{-1})` for an invertible coarse normalization S leaves `Q^T(DE)^T` unchanged. This prevents a convention on the coarse datum from changing the physical current formula.

### 6.2 A quantitative consequence and the exact remaining operator test

Let h_y be the block side of the selected structure and d_s its block metric. Suppose its composite operator in (32) has the block kernel bound

\[
 \sup_{\Delta_s(y)}|\mathcal R_sf|
 \le C_Rh_y^{-1}e^{-\delta d_s(y,z)}\sup|f|
 \quad\text{when }\operatorname{supp}f\subset\Delta_s(z).
\tag{34}
\]

This is the actual `K_{-1}` bound required here. For any positive curvature profile a_z with `sup_{Δ_s(z)}|F_U|≤a_z`, decomposition into input blocks gives directly

\[
 \boxed{\sup_{\Delta_s(y)}|J(U)|
 \le C_Rh_y^{-1}\sum_z e^{-\delta d_s(y,z)}a_z.}
\tag{35}
\]

If, for some `0≤κ<δ`, the profile satisfies

\[
 a_z\le C_a a_y e^{\kappa d_s(y,z)},\qquad
 \sup_y\sum_z e^{-(\delta-\kappa)d_s(y,z)}\le C_{\rm sum},
\tag{36}
\]

then

\[
 |J(U)|_{\Delta_s(y)}
 \le C_RC_aC_{\rm sum}\,a_yh_y^{-1}.
\tag{37}
\]

This includes the fixed-scale, constant-curvature-profile case with C_a=1. For the actual Q4 unit, the desired choices are

\[
 h_y=\ell_{p\wedge\lambda(y)},\qquad
 a_y=C_F\,\omega(y)\varepsilon_{m(y)}\ell_{m(y)}^{-2}.
\tag{38}
\]

Here C_F converts the plaquette bound into the normalized curvature bound. At unitary U one may take the projection norm times the direct plaquette constant because `|Im P|≤|P−I|`. At complex U this comparison also needs a bound on P^{-1}; it is not a unitary inequality. With (38), (37) has exactly the two-scale normalization of I:128811. Crucially, (36) is a statement in the **retained structure's metric**, while m and omega are the frozen-data profile. Spatial decay in one hierarchy does not alone compare that profile in a different hierarchy.

The curvature profile in (35) must hold on every plaquette block reached by DE_s, including the boundary collar when the variation space has fixed exterior. A Q2 bound only at the observation point, or only on the twice-shrunk output region, is insufficient. One may split the sum into controlled interior and a boundary tail, but then the tail needs its own curvature bound and distance gain. The actual localized problem's collars must be checked in this application.

The ordinary earlier-chart kernel inputs suggest (34): H_0 is of order −1, its first derivative is of order −2, E=H_0 ell is of order 0, and DE is of order −1. Pointwise transpose bounds and bounded block-local Q^T then give `Q^T(DE)^T` of order −1. The precise needed inputs are the pointwise first-derivative kernel for E, its transpose with the actual lattice measures, and Q^T's block bound; a bare global estimate `N(H_0b)≤B|b|` is not enough to infer all those pointwise transpose bounds. Relevant quoted sources are I:13569–13627,13638–13676 and the pointwise transpose clause I:13443–13449. The q_0 bound used in constructing H_0 is itself explicitly quoted without proof at I:13624–13627.

This does **not** establish that the Q of this chart equals every localized composite Q_s, that its first-derivative constants are uniform over the complete retained family, or that (36) holds with uniform constants for (38). These are the concrete tests remaining. Unlike separate Laplacian response estimates, they directly target the current entry.

### 6.3 Recursive use and its first obstruction

At the real frozen background, the deposit identifies the derived configurations as constrained critical configurations at I:128787–128795, using its nested-criticality assumptions and the proof at I:128715–128765. Once that identification holds, (32) can be applied afresh at each retained triple. One need not multiply right inverses over all earlier RG stages: construct the right inverse for the selected structure at that triple. Under uniform (34)–(36), every Q4 follows from that triple's Q2/curvature bound.

The deposit's own baseline lemma does not presently derive this uniform step. It assumes exactly the multilevel bound needed at I:128807–128817, and explicitly says at I:128923–128930 that it is a hypothesis, not a consequence derived there from the one-level CMP109(1.16) statement. This is the first concrete extra operator/profile obligation in this route. Box and junction triples meet at most two adjacent levels, I:128935–128950, which narrows the geometry but is not an automatic proof of a uniform constant for arbitrary retained structures.

For complex input data, a derived minimizer may satisfy the same criticality by its defining analytic continuation, provided that continuation has already been constructed on the required weak regularity domain. For a source-decorated chart whose output has not been shown to be such a minimizer, retain a criticality defect. More precisely, if

\[
 J(U)=Q_s^T\lambda+r,
\]

the exact replacement for (32) is

\[
 \boxed{J(U)=\mathcal R_sF_U+
               (I-Q_s^TE_s^T)r.}
\tag{39}
\]

Thus noncriticality cannot be removed merely by reusing the real minimizer identity. The source-decorated residuals in §4 are a different manifestation of this issue, but have not been identified with r for the global layer.

Even when r=0, uniform **increments** of Q4 need a kernel increment as well as a curvature increment. On one fixed structure,

\[
 J(U_1)-J(U_0)
 =\mathcal R_s(U_1)(F_{U_1}-F_{U_0})
   +[\mathcal R_s(U_1)-\mathcal R_s(U_0)]F_{U_0}.
\tag{40}
\]

If the operator family in (34) is holomorphic and uniformly bounded on a larger weak-potential ball, a Cauchy estimate supplies the second term on a smaller ball. This only uses a first-derivative kernel, but its holomorphic domain and uniform radius must be proved for the actual selected structure. Changing the constraint structure adds a separate difference of Q_s and E_s; (40) must not be applied as though the structure were fixed when it is not.

## 7. Pinning the global Laplacian: current status

The exact local D*D commutator in §1 is pinned by the displayed definition I:111491–111501. The global symbol Delta_W is less completely pinned. I:111391–111409 identifies its partner-current representation with CMP109(3.11)–(3.14), but defines the corresponding norm by the role it plays in that representation rather than by a component formula.

The accessible original [CMP109, p.272](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf) uses the covariant Laplacian after rewriting `D*D+DRD*` as `D*D+DD*−DPD*`; a local lower-order remainder is retained. This supports treating its Laplacian separately from D*D. It does not, in the text recovered for this audit, give the component definition needed to identify it rigorously with the sum in (11).

There is a further notational distinction in the deposit: I:13587 defines `Delta_a=Delta+DRD*+Q*aQ`, I:13617 defines `Delta'=Delta−D*D`, and I:25328–25361 writes the same Hessian-type Delta(U) as `D*D+Delta'`. These are not a definition of the global covariant Delta_W. Therefore (16) remains a bound for `Delta_cov=Σ nabla* nabla`; inserting it for Delta_W requires confirming that convention, or adding and bounding the difference's commutator. The D*D estimate (15), the algebraic identity (17), and the reconstruction identity (32) do not depend on this unresolved notational match.

## 8. Direct increment interface still to prove

For each actual T/P/L layer, an adequate replacement for the stronger five-entry interface would prove, on the needed weighted domains and with the stated source-distance profile:

1. A bound for the weak increments of A' and H, from the actual two-input equation.
2. A bound for the combined current s_sigma and its increments, retaining the residual in (28) until matched or estimated.
3. The differentiated projection-kernel/tail bound for P_1(sigma), plus the stated local K and F bounds.
4. For every retained composite clause, the actual derived-current estimate. Equations (32)–(40) reduce this to specific right-inverse kernel, profile and holomorphic-domain estimates when constrained criticality is available; otherwise the criticality defect must also be bounded.

With those statements in hand, (17) and the completed local commutators yield the cut-current increments without separately estimating Delta_W H or m_H X. They are not supplied by the commutator argument alone. This identifies the stronger Laplacian interface as a replaceable proof route for the located consumers, while preserving the genuinely necessary combined and composite current obligations.

## 9. Differentiating the actual first walk piece

This is a more specific way to attack E_H and E_G in (23). It is about D_0 of the earlier chart, whose definition is known, rather than the still-unmatched global Delta_W.

### 9.1 The missing companion commutator

For the covariant scalar derivative, the deposit gives
`η(Dλ)(b)=Ad_U(b)λ(b_+)−λ(b_−)` at I:46713–46716. Thus under the same convention as §1,

\[
 (DD^*B)_\nu=\sum_\mu\nabla_\nu\nabla_\mu^*B_\mu.
\]

The exact identities

\[
 \nabla_\nu T_\mu^{-1}
 =T_\nu\nabla_\mu^*+\nabla_\nu-\nabla_\mu^*,
 \qquad\nabla_\mu^*=-T_\mu^{-1}\nabla_\mu
\]

and the product rules in (3) give, for a mixed pair,

\[
 |[\nabla_\nu\nabla_\mu^*,\chi]B|
 \le(1+\tau+2\tau^2)s_1g+\tau^2s_2b.
\tag{41}
\]

Indeed, with `b_mu=∂^-_mu χ`, the commutator is
`−b_mu ∇_nu T_mu^{-1}B −(∂_nu b_mu)T_nuT_mu^{-1}B +(∂_nu χ)T_nu∇_mu^*B`.
For μ=ν the two second-order products commute and (8) applies. Therefore

\[
\begin{split}
 |[DD^*,\chi]B|\le{}&
 \{1+\tau+(d-1)(1+\tau+2\tau^2)\}s_1g\\
 &+\{1+(d-1)\tau^2\}s_2b.
\end{split}
\tag{42}
\]

No curvature derivative was used. In particular, adding (9) and (42), a convenient conservative bound for `1≤τ≤5/4` is

\[
 |[D^*D+DD^*,\chi]B|\le13d(s_1g+s_2b).
\tag{43}
\]

The exact coefficients in (9),(42) are better. The local zero-order Delta' term is separate: its weak bound at I:13617–13620 gives a commutator bound by estimating `Delta'(χB)` and `χDelta'B`. If a derivative-of-cutoff gain is needed, the actual finite-range kernel of Delta' must also be used. The uniform bound without that gain is enough for the first-piece graph estimate below.

### 9.2 Actual head and exact local-inverse calculation

The background inverse called G_0 in §4.5 is written as G in the walk construction of §4.6. To avoid this notational collision, call it G_bg here. Its parametrix is

\[
 S=\sum_\square S_\square,\qquad
 S_\square=h_\square G_\square h_\square,
 \qquad G_{\rm bg}=S\sum_{n\ge0}\mathscr R^n.
\tag{44}
\]

This is explicitly the deposited reading of CMP99b(3.106) at I:25577–25610 and25722–25730. The residual mathscr R should not be confused with the gauge projection R=I−P. Every fully expanded word of (44) begins, on its output side, with exactly the piece S_square. The projection terms occur in mathscr R and in local generator definitions; they do not remove this initial factor.

Use the operators actually defined at I:13587,13617 and25328–25336:

\[
 \mathcal A=\Delta+DD^*=D^*D+DD^*+\Delta',\quad
 P_1=DPD^*,\quad D_0=\Delta_a-Q^*aQ=\mathcal A-P_1.
\tag{45}
\]

For the local cube define

\[
 P_{1,\square}=DP_\square D^*,\qquad
 B_\square=Q_\square^*a_\square Q_\square,\qquad
 \Delta_{a,\square}=\mathcal A-P_{1,\square}+B_\square.
\]

All local operators are understood with their local boundary restriction. The support/margin argument at I:25475–25503 gives `h_square Delta_{a,square}G_square h_square=h_square²`. Write h=h_square and G=G_square for this calculation only. Then

\[
\begin{aligned}
 D_0hGh
 &=(\mathcal A-P_1)hGh\\
 &=h\mathcal A Gh+[\mathcal A,h]Gh-P_1hGh\\
 &=h^2+[\mathcal A,h]Gh-P_1hGh
       +hP_{1,\square}Gh-hB_\square Gh.
\end{aligned}
\]

Hence the exact first-piece formula is

\[
 \boxed{D_0S_\square=h_\square^2
   +[\mathcal A,h_\square]G_\square h_\square
   -P_1S_\square
   +h_\square P_{1,\square}G_\square h_\square
   -h_\square B_\square G_\square h_\square.}
\tag{46}
\]

The global block constraint Q*aQ is absent. In particular, the mismatch
`h_square(Q*aQ−Q_square*a_squareQ_square)G_square h_square`
at an outer seam, explicitly recorded at I:25890–25910 for the Delta_a parametrix, cancels from (46) because D_0 subtracts the global constraint operator. Thus **level agreement is not needed for this algebraic cancellation**. This does not repair every seam issue in the construction: the local inverses, their weighted bounds and the convergence of the chosen remainder expansion must still exist. The source itself makes additional level-agreement/partition assumptions for convergence at I:28129–28146.

All five terms in (46) are candidates for order-zero kernels on the forcing space:

- h_square² has bounded local overlap.
- The D*D and DD* parts of `[mathcal A,h]Gh` are bounded by (9),(42), using only the local first-order G bound and derivatives of h. Delta' contributes its local weak bound.
- P_1 is quoted in K_{−2} at I:13569–13580, while S_square has order 2.
- The corresponding local P_{1,square}G_square product has total order zero.
- B_square is a block-local operator of order −2, so B_square G_square also has total order zero.

The orders alone are not a proof of uniform constants. Each local estimate has to be read with the actual block measures and converted to the global forcing norm, and the absolute block-row sum over heads must be bounded. Formula (46) shows exactly which estimates are needed; it eliminates a naive fine-lattice factor η^{-2} and introduces no differentiation of free-current forcing.

### 9.3 A first-piece summability lemma

Here is a precise sufficient statement suitable for the actual walk expansion. Let Z be the forcing space with norm `|f|_{(-3),rho}`, and X the weak potential space. Work with positive block-kernel majorants; their weighted row norm is submultiplicative under kernel composition. After paying the scalar decoration factors using the spare exponential of K10, suppose:

1. The sum of majorants of the **differentiated initial pieces** D_0S_square from (46), including their absolute decoration cost, has row norm at most C_head on Z.
2. The positive majorant of the expanded remainder has row norm r<1 on Z, after the same exponential payment. Additional bounded, finitely many vertex operators may be included in that majorant with their stated constants.

Then the decorated inverse built from those words obeys

\[
 \|D_0G_\sigma\|_{Z\to Z}
 \le\frac{C_{\rm head}}{1-r}.
\tag{47}
\]

Proof: D_0 acts only on the first factor of each word. A decoration m_omega(sigma) is a scalar independent of the lattice argument, so
`D_0[m_omega S_square T_omega]=m_omega(D_0S_square)T_omega`.
The n-remainder words have positive majorant bounded by the head majorant times the nth power of the remainder majorant. Their row norms sum to at most `C_head Σ_n r^n`. Uniform absolute convergence permits termwise action into Z. No identity at sigma=1 is used, and there is no derivative of sigma.

This is stronger than merely knowing that the original, undifferentiated full operator maps Z to X. The needed hypothesis is absolute summability after **replacing the first piece by (46)**. The source's two-spare-exponential argument is at I:15359–15420; it identifies how decoration can be paid, but its list of output norms does not state (47). The remaining model estimate is the corresponding head majorant, rather than a second derivative of an arbitrary free-current response.

### 9.4 Which K10 operators this can repair

The actual choices are favorable for E_H and E_G:

- H_{0,sigma} is built from `G_bg,sigma Q* q_{0,sigma} ell^{-1}` by I:13640 and15306. D_0 acts on the G_bg head. The q_0 walk remains on the input side.
- The primitive tilde G^J is the series `Σ_n(bar G_0 Theta_J)^n bar G_0`, I:13933–13942. On expanding `bar G_0=G_bg−G_bg Q*q_0QG_bg`, every term again starts with G_bg. Its insertion Theta_J maps X to Z by I:13775–13781. Thus the tail summability needed in (47) is compatible with the same weak spaces as that series.

Consequently, if (46)'s uniform head-majorant bound and the associated remainder summability are established for the actual words, (47) gives `D_0H_{0,sigma}:B→Z` and `D_0 tilde G^J_sigma:Z→Z`. The other terms defining E_H and E_G in (23) already use the stated bounded operators q_0, P_0^T, Theta_J and tilde G^J. The triangle inequality then bounds both residuals uniformly without relying on their cancellation at sigma=1. Their action on the small data b and Y would be small for exactly that reason. Spatial localization of the residual still requires following the retained exponential factors and the possible projection tails in (46).

This argument must **not** be extended automatically to G_pi^J or H^J. Their series has the insertion Theta'_J, I:13725–13731. The proof at I:13823–13845 gives only

\[
 \Theta'_JA=\psi+D\varphi,
 \qquad |\psi|_{(-3)}+|\varphi|_{(-2)}
 \le C|J|_{(-3)}N(A),
\]

with sub-Lipschitz Holder control on phi. Applying D_0 to the first inverse can expose D phi, which need not be bounded in Z uniformly at fine cutoff. This is consistent with the explicit exclusion of a Laplacian bound for G_pi^J at I:13759–13765. The benefit of targeting E_H and E_G is that their head chains use H_0 and tilde G^J with the better Theta_J insertion, not the problematic Theta'_J chain on the output side.

**Status:** (41)–(46) are exact algebra/commutator results for the pinned conventions, and (47) is proved under its explicit positive-majorant hypotheses. The actual output-head identification for H_0 and tilde G^J is verified from the deposited formulas. Uniform local-to-global head bounds, remainder summability for the selected geometries, and the identification with the global four-layer current are still required before this becomes a theorem about that source route.

## 10. A concrete head primitive: the local averaging term and its measures

This checkpoint isolates the last term of (46), `h B_square G_square h`, rather than assuming that the phrase “block-local of order −2” supplies its constant. It also completes the easy Delta-prime subclaim. All line numbers refer to the pinned Raw I.

### 10.1 The transpose conversion is exact; its application needs a dictionary

The §4.5 convention at I:12756–12760 uses fine measure eta^d and coarse measure ell_c^d. In contrast, the local definitions at I:23932–23938 and23961–23968 print the diagonal coefficient `a_n ell_n^(d−2)`, with Q* acting between spaces denoted ell². The §4.6 local definitions do not explicitly specify their Hilbert measures. Therefore the two displayed coefficients should not be compared while silently holding Q* fixed.

Let Q have its actual discrete matrix coefficients, let F=eta^d I be the fine measure matrix, and let M=diag(ell_c^d). Define

\[
 Q^{T}_{\rm count}=F^{-1}Q^{\mathsf t},\qquad
 Q^{T}_{\rm vol}=F^{-1}Q^{\mathsf t}M
                 =Q^{T}_{\rm count}M.
\tag{48}
\]

Here the superscript mathsf t transposes the matrix and its Lie-algebra fiber for the bilinear pairing; it does not complex-conjugate an analytic background. Consequently

\[
 Q^{T}_{\rm count}\operatorname{diag}(a_n\ell_n^{d-2})Q
 =Q^{T}_{\rm vol}\operatorname{diag}(a_n\ell_n^{-2})Q.
\tag{49}
\]

Any one-form scaling already present in Q occurs on both sides and does not alter (48). Equation (49) identifies exactly the convention in which the §4.6 coefficient has order −2. If §4.6 instead uses counting measure on the fine lattice too, an additional fine-measure conversion is needed; (49) deliberately keeps that measure fixed.

There is a direct test using the actually printed scalar average I:23913–23915. Set the background equal to 1 and use a single block containing N=(ell/eta)^d sites. Then Q'=N^{-1}sum, `Q'^T_count b=ell^(-d)b` on the block, and `Q'^T_vol b=b`. Hence both sides of (49) equal `a ell^(-2)` times the block-average projection. Using Q'^T_vol together with the coefficient `a ell^(d−2)` instead gives `a ell^(d−2)` times that projection, differing by ell^d. This is a normalization diagnostic, not evidence that the original paper used the inconsistent combination.

There is also a dimensionless normalization issue: the §4.5 display uses a=ell^-2 (I:13583–13593), while §4.6 retains the sequence a_n (I:23879–23881), whose recursion is referred to CMP99b(3.23)–(3.24). A bound `sup_n |a_n|≤a_*` suffices below, but its value and the identification with the selected global inverse must not be silently discarded.

### 10.2 The flat bond average gives an exact scale-uniform bound

The full one-step bond formula is transcribed at I:24355–24365. Its main term is I:24369; at the flat background the four correction brackets vanish. The resulting operator, in dimensionless fine coordinates, is

\[
 (Q_M A)_\mu(c)=M^{-(d+1)}
       \sum_{x\in B_M(c)}\sum_{t=0}^{M-1} A_\mu(x+t e_\mu),
 \qquad M=L^n.
\tag{50}
\]

The statement for n=1 is the printed main term. Its iterates have exactly the form (50): the successive block coordinates give the base-L digits of x, and the successive line coordinates give independently the base-L digits of t. Centered odd-L blocks give the centered M-block. This also verifies the powers of L without importing a kernel convention.

Write q_M(c,b) for its discrete scalar coefficient. The coefficients are nonnegative, each row sums to 1, and q_M(c,b)≤M^-d. More strongly, its volume transpose has column sum 1:

\[
 \sum_c M^d q_M(c,b)=1
 \quad\text{for each fine bond b of the given direction.}
\tag{51}
\]

To see the last assertion, the transverse coordinates select one coarse block. In the longitudinal direction the coefficient is M^(-(d+1)) times the number k_M(s) of pairs `(x_mu,t)` with x_mu in the M-block and 0≤t<M whose sum is s. For each residue modulo M there are exactly M such pairs, so `sum_z k_M(s−Mz)=M`. This gives (51). Restricting coarse rows or imposing a Dirichlet restriction can only decrease these positive sums. Thus the actual flat averaging primitive satisfies

\[
 \|Q_M^{T}_{\rm vol}\,a\ell^{-2} Q_M\|_{\infty\to\infty}
 \le |a|\ell^{-2},
\tag{52}
\]

with equality for the unrestricted constant mode when a≥0. There is no eta-dependent counting factor.

A local mixed-scale version is also immediate. Suppose only N_lev different coarse levels can contribute to an output of h B_square, that all input and output scales on their averaging supports differ from ell_c by at most a fixed factor R, and |a_n|≤a_*. With the local weighted norms of §4.5,

\[
 |h B_\square A|_{(-3)}
 \le \|h\|_\infty\,N_{\rm lev}a_*R^4 |A|_{(-1)}.
\tag{53}
\]

Indeed, the row sum gives |QA(c)|≤R ell_c^-1 |A|_(-1). Multiplication by ell_b³ ell_c^-2 costs at most R³ ell_c, and summing the volume-transpose coefficients costs at most one per contributing level by (51). This proves (53). Near the retained local head support the source identifies only levels j and j+1 (I:25742–25747), and the averaging supports stay within square^(2) when M≥L (I:25479–25483). On that local geometry one may therefore take N_lev=2 and R=L. If G_square has its asserted local forcing-to-potential bound C_G, the flat contribution to (46) is at most `2 a_* L^4 C_G ||h||_infty^2`. Conversion to the global hierarchy still requires comparable local/global weights on the relevant supports; this conclusion does not remove that requirement at an outer seam.

For an exponential weight rho, multiply the right side of (53) by `sup rho(b)/rho(b')` over the two averaging supports. When their diameter in the retained hierarchy metric is bounded by D_Q this costs at most exp(kappa D_Q). This finite-range cost is independent of the fine lattice spacing.

### 10.3 What remains for the complex bond primitive

The preceding result does not prove the non-Abelian complex averaging bound by perturbation alone. Formula I:24355–24365 includes contour terms and operator brackets involving Y,Y_x,g. Their definitions are explicitly not reproduced at I:24399–24409. Bounding each one-step factor by a fixed constant and multiplying n times would be inadequate.

There is concrete supporting normalization evidence: the unit-lattice kernel is explicitly defined by

`(Q^flat B)(c)=sum_b L^(-d) Q^flat(V;c,b) B(b)`

at I:46981–46984. The multi-level bound `|Q_j(U;c,b)|≤4` is stated at I:47046–47061 and justified by the separate complex averaging proposition at I:47233–47249. This shows why a printed kernel bound of size 4 should not be treated as an unweighted discrete matrix coefficient. It does **not**, in the lines just cited, state the multi-level measure convention or the complete proof of that proposition.

One sufficient precise completion is to identify, on every selected local complex background, positive coefficient bounds with constants C_row,C_col independent of n:

\[
 \sum_b\|q_n(c,b)\|\le C_{\rm row},\qquad
 \sup_b\sum_{c\text{ at level }n}
       (\ell_n/\eta)^d\|q_n(c,b)\|\le C_{\rm col}.
\tag{54}
\]

The proof of (53) then applies verbatim with the additional factor C_row C_col; the transpose of a complex matrix has the same fiber operator norm in the fixed Euclidean/trace norm. In particular, an actual normalized pointwise coefficient statement `||q_n(c,b)||≤C_q(eta/ell_n)^d`, together with the printed two-block support and bounded incidence per level, implies (54). The needed next source formula is the multi-level normalization and bound behind CMP98(139)/CMP99b(3.15)–(3.16), including its admissible complex background class. No claim of absence is made: the deposited account invokes that result, and the original full proof has not been obtained here.

### 10.4 The Delta-prime head term needs no second derivative of the output

For the earlier Hessian convention, Delta'=Delta−D*D is local and obeys the explicit estimate I:13617–13620. Write its constant C_Delta, so

`|Delta' A|_(-3)≤C_Delta(a_0+a_1)|A|_(-1)`.

Multiplication by a bounded scalar does not increase either weighted sup norm by more than its supremum. Therefore

\[
 |[\Delta',h]A|_{(-3)}
 \le 2\|h\|_\infty C_\Delta(a_0+a_1)|A|_{(-1)}.
\tag{55}
\]

Composing with a local bound `|G_square f|_(-1)≤C_G |f|_(-3)` gives a contribution `2 ||h||_infty^2 C_Delta(a_0+a_1) C_G` to the head norm. This requires no cutoff derivative and yields no inverse-M improvement; a bounded head constant is all that (47) asks for.

For an **absolute** kernel majorant, one must not silently identify an operator norm with the sum of its coefficient norms. Here locality repairs that step: if each output of Delta' reads at most m_d fine bonds (the one-step locality is recorded at I:25479), testing the norm estimate on one supported input gives a weighted bound for each matrix coefficient, and summing costs at most m_d. Thus the coefficientwise version of (55) holds with the conservative extra factor m_d. A safe choice for a one-step stencil, counting all directions in a surrounding cube of radius two, is `m_d=d 5^d`. Exponential weights cost the maximal rho-ratio on that stencil. This supplies the Delta-prime part of the first-head majorant subject only to the actual local G bound and the retained weight comparison, not an additional Laplacian estimate on G's output.

**Checkpoint:** the flat bond primitive (50)–(53), the transpose conversion (48)–(49), and the Delta-prime reduction (55) are proved here from explicit finite-dimensional algebra and the indicated source inputs. The complex normalized multi-level estimate (54), the local G/P1 constants on the selected retained geometries, and the final summed head majorant remain to be matched before (47) can be applied to the global source layer.
