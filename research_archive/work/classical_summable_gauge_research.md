# Summable connecting gauges for the classical invariant quotient

17 October 2026. Research proof for independent audit. This addresses the additional invariance interface in activity_quotient_research.md Section 6. It uses the actual small gauges supplied by the ordinary-minimum proof, but does not require a new weighted estimate for the nonlinear gauge-fixing inverse. No output edit or compilation.

## 1. The precise infinite-system input

Fix a homogeneous preceding refinement \(M\), a finite allowed endpoint ratio \(L\), and a common classical radius. Suppose the infinite pre-gauge map \(a_L(w)\) has been obtained on a single joint subsequence of compatible cubic regulators from the actual finite-regulator maps
\[
 e^{ia_{L,N}(w)}=P_{M,L,N}(e^{iw}).
 \tag{1.1}
\]
For every compactly supported final field, the convergence is local at every current link, locally uniform in its finitely many field variables. The coherent support theorem supplies
\[
 \|a_L(w)|_i\|_\infty
 \le \rho\,e^{-\kappa\,\operatorname{dist}(i,K)},\qquad
 \rho=C_A b/L,
 \tag{1.2}
\]
when \(\|w\|_\infty<b\) has final-cell support \(K\). The same assertion holds for any other compact datum in that ball. Uniform finite-regulator support bounds and analytic compactness are one established way to supply this input. A family chosen by unrelated pointwise subsequences is not substituted for it.

Current links have spacing \(1/L\) in final physical units. All statements about summability below are on this fixed current lattice. Gauge matrices are estimated in a unitarily invariant matrix norm. The scalar-coordinate field norm of the activity polydisc is equivalent to the invariant color norm with fixed group-dependent constants; all conversions, including constant conjugation, are included in the constants below. Constants may depend on \(L\), the finite compact support and fixed group norms, but not on preceding refinement or the approximating volumes. The lattice dimension is at least two; the application is \(d=4\).

Let the input quotient consist of anchored analytic interactions whose normalized totals are invariant under compact **local gauge paths** staying inside the analytic field ball, and under constant global adjoint transformations. This is the local gauge identity used in the invariant quotient. If a definition instead imposes additional disconnected endpoint-gauge identities, those are extra conditions; they are not inferred from an infinitesimal Ward identity.

The activity norm gives the already proved summable-field estimate, for \(0<\rho_1<b\),
\[
 |\Phi_E(A)-\Phi_E(B)|
 \le \frac{\|[E]\|_Q}{b-\rho_1}\|A-B\|_{\ell^1_{\rm cell}},
 \quad \|A\|_\infty,\|B\|_\infty\le\rho_1.
 \tag{1.3}
\]
It also gives absolute convergence of the normalized total for those summable fields.

The goal is to prove, for every such invariant class and compact coarse gauge \(v\) in the allowed local component,
\[
 \Phi_E(a_L(w^v))=\Phi_E(a_L(w)).
 \tag{1.4}
\]
Here both coarse fields belong to the domain. The connecting gauges constructed below are independent of \(E\), so the conclusion is universal over the invariant quotient for the fixed joint background system.

## 2. What the actual finite equality proof gives

The equality clause of the ordinary-minimum theorem is stronger than equality of action values. We record its quantitative consequence.

For an ordinary-feasible fine field \(U=e^{i\eta A}\), the proof first applies the ordinary-to-corrected gauge \(g_1=e^{iH_b\theta}\). The induced-gauge implicit equation gives
\[
 \|\theta\|_\infty\le2\|\omega\|_\infty,\qquad
 \omega=\log b_j(U)/i,\qquad
 \|\omega\|_\infty\le C\|A\|_{C^{1,\alpha}}.
 \tag{2.1}
\]
The proved bound \(H_b:\ell^\infty\to C^{2,\alpha}\) therefore controls \(g_1-I\) uniformly. Next the constraint-preserving flat-slice flow uses the scalar velocity
\[
 \lambda(t)={\cal L}_{A(t)}A(t),\qquad
 \|\lambda(t)\|_{C^{2,\alpha}}
 \le C e^{-t}\|R_0D^TA(0)\|_{C^\alpha}
 \le C e^{-t}\|A(0)\|_{C^{1,\alpha}}.
 \tag{2.2}
\]
Integrating the actual unitary gauge ODE gives a limiting gauge \(g_2\) with
\[
 \|g_2-I\|_\infty
 \le C\int_0^\infty\|\lambda(t)\|_\infty\,dt
 \le C\|A(0)\|_{C^{1,\alpha}}.
 \tag{2.3}
\]
Finally the selected ordinary representative is obtained from the strict corrected minimum by \(h_*=e^{iE_{\rm pt}\omega_*}\), with \(\|\omega_*\|_\infty\le C\|B\|_\infty\). If equality of the two minimum values holds, strict slice convexity identifies the intervening field with that corrected minimum. The product of these actual gauges maps \(U\) to the selected ordinary minimizer and satisfies
\[
 \|g_{\rm eq}-I\|_\infty
 \le C\bigl(\|A\|_{C^{1,\alpha}}+\|B\|_\infty\bigr).
 \tag{2.4}
\]
The constants are uniform in refinement and volume on the established smaller balls. This follows from the explicit transfer, integrable flow and inverse transfer; no inverse massless gauge Laplacian or unproved spatial locality of \({\cal L}_A\) is assumed.

Apply this to gauge covariance of the ordinary minimizer. For a compact coarse gauge \(v=e^{i\theta}\), use the fixed smooth point-value extension \(\widehat v=e^{iE_{\rm pt}\theta}\) to the original fine lattice. It is compact in physical space and has \(C^{2,\alpha}\) bound \(C\|\theta\|_\infty\), uniformly in the mesh. The fields \(U_{\rm ord}(w)^{\widehat v}\) and \(U_{\rm ord}(w^v)\) satisfy the same ordinary constraint. The two minimum comparisons, using also the inverse gauge, give equality. Equation (2.4) then yields an actual fine gauge \(g_N\) such that
\[
 U_{\rm ord,N}(w^v)=U_{\rm ord,N}(w)^{g_N},\qquad
 \|g_N-I\|_\infty\le C(b+\|\theta\|_\infty).
 \tag{2.5}
\]
Choose the data and local gauge neighborhoods so the right side is a fixed small number \(\delta\). Ordinary covariance of the prefix gives
\[
 e^{ia_{L,N}(w^v)}
       =\bigl(e^{ia_{L,N}(w)}\bigr)^{g_N|_{\rm current}}.
 \tag{2.6}
\]
All competitors remain in the actual comparison class: their complete fine-potential norms are at most \(C(b+\|\theta\|_\infty)\). This establishes the needed orbit relation and the small-gauge bound from the proved construction, not merely from equal action.

## 3. Passing a connecting gauge to infinity

Fix real compact \(w,\theta\) in these neighborhoods, with \(w^v\) also in the coarse ball. Their current configurations converge along the joint subsequence in Section 1. Compactness of the group and a diagonal subsequence over current sites give a limiting gauge \(g\). For this fixed pair it is legitimate to take a further subsequence of gauges: the background maps already have their specified limits. There is no need to choose the gauge simultaneously or holomorphically for every pair.

Local passage in (2.6) gives, with \(U=e^{ia_L(w)}\) and \(V=e^{ia_L(w^v)}\),
\[
 V_{xy}=g(x)U_{xy}g(y)^{-1},\qquad
 \sup_x\|g(x)-I\|\le\delta.
 \tag{3.1}
\]
Both endpoint link fields have exponential spatial decay by (1.2), since \(w^v\) is compact when \(w,\theta\) are compact.

This argument establishes an actual infinite gauge relation for each required pair. Equal limiting action values would not establish (3.1).

## 4. Endpoint decay forces a single constant gauge at infinity

The following elementary lemma supplies the missing summability.

**Lemma.** Let \(U,V\) be compact-group link fields on \(\mathbb Z^d\), \(d\ge2\), and let \(V=U^g\). Suppose for positive bonds at \(x\),
\[
 \|U_b-I\|+\|V_b-I\|\le C_K e^{-\mu|x|_\infty}
 \tag{4.1}
\]
for some positive \(\mu\). Then a single \(c\in G\) exists with
\[
 \|g(x)-c\|\le C'_K(1+|x|_\infty)e^{-\mu|x|_\infty}.
 \tag{4.2}
\]
In particular \(c^{-1}g-I\) is summable. Its supremum is at most \(2\delta\) when \(\|g-I\|_\infty\le\delta\).

**Proof.** Rearrange the edge equation as
\[
 g(y)=V_{xy}^{-1}g(x)U_{xy}.
\]
Unitary invariance of the matrix norm gives
\[
 \|g(y)-g(x)\|
       \le\|U_{xy}-I\|+\|V_{xy}-I\|.
 \tag{4.3}
\]
The sequence \(g(ne_1)\) is Cauchy by summing (4.1) on its ray; its limit \(c\) belongs to the compact group, and its tail is \(O(e^{-\mu n})\). For \(n=|x|_\infty\), the lattice boundary of the cube \([-n,n]^d\) connects \(x\) to \(ne_1\) by a path of length at most \(C_dn\). One can keep one coordinate at \(\pm n\) while adjusting the others, use a second boundary coordinate to change its sign, and then reach the chosen ray. This uses \(d\ge2\). Every edge lies on that boundary and its positive lower endpoint has norm at least \(n-1\). Equations (4.1),(4.3) bound the oscillation by \(C_dnC_K e^{-\mu(n-1)}\). Combine with the ray tail. Summability follows because shell cardinalities grow only polynomially. The small-supremum assertion follows by taking the limit of \(g\) and using \(\|c^{-1}g-I\|=\|g-c\|\). \(\square\)

For the actual fields, (1.2) implies (4.1) with \(\mu\) a fixed positive multiple of \(\kappa/L\), after enclosing the finite final support in a cube. Constants may depend on that support and on fixed \(L\), which is harmless for equality of evaluations. This proves exponential decay of the connecting gauge modulo a constant without asserting weighted decay of every operator in the finite gauge flow.

The dimension restriction is real: in one dimension the two ends can carry different limiting constants. It does not affect the four-dimensional application.

## 5. Compact gauges, strict margins and summable inputs

Put \(h=c^{-1}g\), so \(h-I\in\ell^1\) and
\[
 U^h=c^{-1}Vc.
 \tag{5.1}
\]
For sufficiently small \(\delta\), choose the common Hermitian logarithm \(h(x)=e^{i\lambda(x)}\), with \(\lambda\in\ell^1\) and uniform small supremum. Let \(\lambda_R\) agree with \(\lambda\) in a current cube and be zero outside, and set \(h_R=e^{i\lambda_R}\). These are compact gauges. The exponential tail gives
\[
 \|h_R-h\|_{\ell^1}\longrightarrow0.
 \tag{5.2}
\]
No smooth physical cutoff is needed at this fixed current lattice; the jump tends exponentially to zero. At each current bond,
\[
 \|U^{h_R}_b-U^h_b\|
 \le\|h_R(x)-h(x)\|+\|h_R(y)-h(y)\|.
 \tag{5.3}
\]
Thus the transformed link fields converge in \(\ell^1\). On a common strict logarithm chart, their potentials converge in the cell \(\ell^1\) norm as well.

For clarity, the compact-gauge path can be kept inside the analytic field ball, rather than appealing to endpoint invariance alone. The edge equation and the uniform Lipschitz bound for the small logarithm give
\[
 \|\lambda(y)-\lambda(x)\|
 \le C\bigl(\|a_L(w)_b\|+\|a_L(w^v)_b\|\bigr)
 \le C\rho.
 \tag{5.4}
\]
Constant conjugation in (5.1) is an isometry in the invariant color norm; its fixed comparison with the scalar-coordinate polydisc norm is included in \(C_g\) below. For sufficiently large truncation \(R\), the exterior jump of \(\lambda_R\) is also at most \(\rho\). For \(0\le t\le1\), Duhamel's formula for real Hermitian matrices bounds
\[
 \|e^{it\lambda_R(y)}-e^{it\lambda_R(x)}\|
       \le \|\lambda_R(y)-\lambda_R(x)\|.
\]
It follows, using the small link logarithm, that
\[
 \sup_{t\in[0,1]}
 \left\|\log\!\left(U^{e^{it\lambda_R}}\right)/i\right\|_\infty
 \le C_g\rho.
 \tag{5.5}
\]
Here \(C_g\) depends only on fixed group/chart conventions, not on support, \(R\), refinement or volume. Choose the endpoint ratio with
\[
 C_g C_A/L<1/2.
 \tag{5.6}
\]
Then every sufficiently large compact gauge path in (5.5) has a common strict field-domain margin below \(b\). For a smaller fixed endpoint ratio the same argument proves a local germ on a correspondingly smaller data ball; it does not silently grant a whole-ball path margin.

The input field in (5.5) is summable, not compact. To invoke the defining quotient invariance correctly, first truncate its potential to a much larger cube containing the support of \(\lambda_R\) and every adjacent bond. On the gauge support the compact input agrees with the original one; outside, the gauge is identity and the compact input is either the original field or zero. Hence the same strict bound holds throughout the compact path. Local gauge invariance on compact fields gives equality of their normalized totals. Sending this input truncation to infinity and using (1.3) proves
\[
 \Phi_E(\log U^{h_R}/i)=\Phi_E(\log U/i).
 \tag{5.7}
\]
Now send \(R\) to infinity using (5.2),(5.3),(1.3). Constant global adjoint invariance, extended to summable fields by the same compact-truncation argument, gives
\[
 \Phi_E(a_L(w))
   =\Phi_E(\operatorname{Ad}_{c^{-1}}a_L(w^v))
   =\Phi_E(a_L(w^v)).
 \tag{5.8}
\]
All these equalities hold for every invariant input class; the estimates do not use an interaction-dependent gauge or an interaction-dependent domain choice.

## 6. Local analytic invariance and the quotient conclusion

The preceding construction proves (5.8) for real compact coarse data and sufficiently small compact gauge parameters, with both coarse fields in their classical domain. Finite-coordinate holomorphy extends the local identity. More explicitly, differentiate at the zero compact gauge parameter. The resulting infinitesimal identity is holomorphic in the finitely many coarse field variables on their connected product ball and vanishes on a real open set, so it vanishes throughout that complex ball. Integrating along any allowed compact local gauge path staying in the ball gives the exact local gauge invariance used to define the invariant quotient. This does not promote a local Ward identity to an arbitrary disconnected endpoint identity.

Consequently, on a fixed joint infinite background system satisfying Section 1, the scalar substitution
\[
 [E]\longmapsto\bigl(w\longmapsto\Phi_E(a_L(w))\bigr)
 \tag{6.1}
\]
preserves local gauge invariance for **every** invariant input class, provided the common margin (5.6) or the corresponding smaller germ is used. Algebraic descent and its norm estimate still use the separately proved summable-field continuity and connected representation theorem. When those hypotheses hold, this closes their previously explicit extra gauge-identity condition; it is not merely invariance of one interaction chosen together with the subsequence.

Spatial symmetry can be treated by the same endpoint method if required for the whole invariant quotient. On finite regulators the transformed ordinary minimizer and the selected minimizer at transformed data are small feasible fields with equal minimum values, hence are related by the same controlled gauges. Their prefixes satisfy the orbit identity. For compact data both infinite endpoints decay. Sections 3–5 then apply, and the input total's spatial symmetry supplies the remaining change of variables. Constant adjoint covariance is either exact by the equivariant construction or follows from the corresponding small-gauge comparisons and connectedness of the compact group. Coefficientwise symmetry is never required.

This result does not assert uniqueness of the joint infinite background system. A universal map here means an action on every admissible interaction class **for that fixed map**, not independence of all possible regulator subsequences. Classical semigroup assertions likewise require the maps and their compositions to belong to the joint system; the finite-regulator semigroup alone is not a consistency theorem for unrelated limits.

## 7. Established result and retained boundaries

The actual finite transfer and flat-slice flow give uniform small connecting gauges. The endpoint relation plus exponential decay of the two pre-gauge fields forces exponential decay of that gauge modulo one constant. Compact gauge truncation, compact approximation of its summable input, and the strict-margin path bound then prove the required identity for every invariant interaction class.

No weighted nonlinear gauge-flow theorem was presumed. No inference was made from equality of action alone. The necessary actual orbit relation came from the proved equality clause and a joint background limit. The proof is for homogeneous local fields and compact local gauge paths in \(d\ge2\); arbitrary orbit domains, mixed histories and topological sectors are outside it.

The connected representation and boundedness of the classical quotient map remain separate analytic inputs, already isolated in the quotient note. This argument does not define or prove descent of a quantum integral on that quotient, prove a quantum induction, or construct a continuum measure.
