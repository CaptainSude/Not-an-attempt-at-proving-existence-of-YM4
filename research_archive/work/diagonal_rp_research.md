# Diagonal reflection positivity for pure Wilson SU(2)

Research note, 16 October 2026. The finite-volume lemma below is proved directly. It does not establish diagonal reflection positivity of the particular infinite-volume limit selected by the repository's coordinate tori.

## 1. Answer and literature check

**Yes:** pure Wilson SU(2), at nonnegative inverse coupling, is reflection positive across `t+x=0` on a torus genuinely adapted to that mirror. The reason is positivity of the kernel belonging to a plaquette cut along its diagonal. The proof below works for every bounded function of the positive-half link variables, hence also for gauge-invariant observables.

As primary corroboration, Kazakov and Zheng, *Bootstrap for Lattice Yang-Mills theory*, [arXiv:2203.11360](https://arxiv.org/pdf/2203.11360), p. 3 and Fig. 5, explicitly impose site, link, and diagonal reflection positivity for the Wilson lattice gauge theory in dimensions 2, 3, and 4. Their references [34] and [35] are Osterwalder–Seiler and Montvay–Münster. Their numerical problem is at large N; the direct proof below has no large-N requirement.

Osterwalder and Seiler, *Gauge field theories on a lattice*, Annals of Physics 110 (1978), 440–471, [DOI](https://doi.org/10.1016/0003-4916(78)90039-8), is the cited original source. Its abstract confirms lattice physical positivity and a positive self-adjoint transfer matrix. I did not retrieve and verify its full treatment of the diagonal geometry, so I do not attribute a specific diagonal-torus theorem to that paper.

## 2. A precise adapted torus

Work at unit spacing in dimension d≥2. Write z=(t,x,y), s(z)=t+x, and

    r(t,x,y)=(-x,-t,y).

For integers n,m≥4 and transverse periods L_j≥4, take the quotient of the cubic lattice by

    Γ = n Z(e_0+e_1) + m Z(e_0-e_1)
        + Σ_{j=2}^{d-1} L_j Z e_j.

The normal coordinate s is well defined modulo 2n. The two fixed boundary sheets are s=0 and s=n. Indeed, r z−z=−s(z)(e_0+e_1), which is a period on either sheet. Reflection exchanges the interiors 0<s<n and n<s<2n and fixes every boundary vertex and every boundary link pointwise. The boundary links have directions e_j, j≥2. Orientations of reflected links are handled by the usual convention U_(b,a)=U_(a,b)^−1.

The Wilson probability measure is

    dμ(U)=Z^−1 exp[(β/2) Σ_p Re tr U_p] Π_e dHaar(U_e),   β≥0,

with each unoriented plaquette counted once. A harmless global constant in the usual action has been omitted.

## 3. Geometry of the plaquettes

A nearest-neighbor bond changes s by 0 or ±1, so no bond joins the strict positive half directly to the strict negative half. Every plaquette either lies in a closed half, lies in a boundary sheet, or is a (t,x)-plaquette cut along a diagonal by one boundary sheet. In the latter case its four normal coordinates are −1,0,0,1 relative to that sheet. Its opposite vertices a,b lie on the boundary; its other two vertices are exchanged by r.

Let A_p be parallel transport along the two-edge positive-half path from a to b and B_p the transport along the two-edge negative-half path from a to b. Then the crossing plaquette transport is A_p B_p^−1, up to inversion/conjugation which leaves its real trace unchanged. Reflection sends A_p to B_p, with the same fixed endpoints.

The action therefore consists of a positive-half contribution W_+, its reflected W_−, a boundary contribution W_0, and crossing factors

    K_p(A_p,B_p)=exp[(β/2) Re tr(A_p B_p^−1)].

Here W_± denote the exponential weights of the corresponding half actions, not additive actions.

## 4. Positive crossing kernel and full RP proof

Write A=a_0 I+i Σ_{j=1}^3 a_j σ_j and similarly B=b_0 I+i Σ b_j σ_j, with a,b∈S^3. Then

    (1/2) Re tr(AB^−1)=a·b,

and hence

    K(A,B)=exp(β a·b)
          = Σ_{α∈N^4} [β^|α|/α!] a^α b^α.

All coefficients are nonnegative. This series is uniformly absolutely convergent on S^3×S^3. Products of the finitely many crossing factors therefore have an expansion

    Π_p K_p = Σ_λ c_λ h_λ(U_+) h_λ(rU_-),   c_λ≥0,

with real h_λ. Boundary variables can be included as parameters throughout. Haar measure factors into independent positive-half, negative-half, and boundary-link measures; reflection identifies the first two. For any bounded positive-half observable F, define ΘF(U)=overline{F(rU)}. F may depend on boundary links too. Integrating the above expansion yields

    Z ∫ F ΘF dμ
      = ∫ dU_0 W_0(U_0) Σ_λ c_λ
          |∫ dU_+ W_+(U_+,U_0) F(U_+,U_0) h_λ(U_+)|²
      ≥ 0.

Termwise integration is justified by the uniform absolute convergence and compactness of the finite configuration space. This proves diagonal RP.

The same proof applies to reflection-invariant finite cubic boxes with free boundary conditions: retain only the plaquettes and links contained in the box. A centered hypercubic box has both coordinate and diagonal RP through its center. This is a possible regularization choice, but the RG estimates and the translation-invariance argument for its limit would have to be established separately.

For SU(N), replace the quaternion coordinates by the real and imaginary matrix entries: Re tr(AB*) is their real Euclidean inner product. The exponential of that inner product has the same positive-kernel expansion. Thus the elementary pure-gauge proof is not specific to SU(2).

## 5. Why this does not settle the original limit

The repository's YM4 zeroth draft uses coordinate cubic tori

    R^4 / (2L^m Z^4)

and only claims RP at coordinate hyperplanes in its unconditional continuum theorem. See its introduction, §1 conventions, and clause (ii) of its main theorem. Its asserted full rotational invariance uses a separate infrared-flux hypothesis.

On a coordinate torus of side N, r(t,x)=(-x,-t) is a symmetry, but its fixed set is only s=0 mod N. The apparent opposite cut s=N/2 (if N is even) is not fixed pointwise: r changes points there by (−N/2,−N/2), which is not a period. Thus the Haar-factorization argument with a pointwise-fixed common boundary does not apply to that torus. Symmetry alone is not reflection positivity.

This is a geometry obstruction to this proof, not a counterexample asserting that all possible diagonal inequalities on a coordinate torus fail. I have not proved such a counterexample.

Finite adapted-torus RP passes to any local weak limit obtained from those adapted tori at fixed lattice spacing. A further continuum limit inherits RP when the chosen scalar lattice observables transform correctly under reflection and their relevant moments converge (or one works with bounded cylindrical observables and has a genuine limiting law). But this does **not** show that a limit selected by coordinate cubic tori agrees with an adapted-torus limit. At weak coupling, no appropriate uniqueness or boundary-insensitivity theorem has been supplied here. Nor do separate subsequences establish both RP directions for the same state.

The QED3 manuscript recognizes exactly this issue in §1.1: its chamber system is RP on adapted tori, whereas the coordinate tori used for the construction are not adapted to diagonal mirrors. It devotes §§3–4 to a pressure/folding and convex-separation comparison that transfers diagonal RP to the original limit. Its fermionic elimination arguments are model-specific; the conclusion cannot simply be imported into pure Yang–Mills. Pure gauge bounded compact variables may simplify a comparison, but a complete proof is still needed.

## 6. Scalar action density caveat

At finite spacing, a sum of plaquette energies weighted at plaquette centers can be made exactly covariant under r. A point-based discretization or an averaged block insertion must instead have its reflection error controlled. For tests supported a fixed positive distance from the mirror, sufficiently fine plaquettes remain in the positive half; then the above finite-volume positivity applies to their polynomial observables. Passing to a limit requires the corresponding moment convergence and consistent centering. If general test functions reach the mirror or coincidence diagonals, density/continuity arguments are additional requirements.

Finally, the repository's simplified rotation theorem concerns Gaussian-dominated **closed two-forms**. A scalar action density is neither that field nor known to satisfy that theorem's L² Gaussian domination and closedness hypotheses. Even after same-limit diagonal RP is proved, a scalar rotation argument needs its own verified regularity/analyticity theorem.

**Research status:** the finite adapted-torus pure-Wilson diagonal RP input is proved above. Same-limit geometry transfer for the YM4 construction remains open in this audit.

## 7. Free cubes: the translation-invariance obligation is real

A centered free-boundary cube has the coordinate and diagonal RP properties simultaneously. Any subsequential local weak limit of such cubes therefore retains these properties through the origin. It is also invariant under signed coordinate permutations. This observation alone does not prove translation invariance.

Nor is averaging all translates a valid automatic repair. Here is an explicit abstract counterexample. On real lattice scalar fields in dimension d≥2, set

    φ_0(z)=Σ_{j=0}^{d-1} cos(2π z_j/3),   μ=δ_{φ_0}.

The deterministic configuration is invariant under every signed coordinate permutation, hence under the coordinate and diagonal reflections through the origin. Consequently μ is RP for every such reflection: μ(F ΘF)=|F(φ_0)|²≥0 for any half-space function F.

Average μ over its finite translation orbit:

    μ_bar = 3^−d Σ_{a∈{0,1,2}^d} δ_{τ_a φ_0}.

This measure is invariant under every lattice translation and the hypercubic group. But it is not RP at t=0. Let F(φ)=φ(e_0)−φ(2e_0), which is supported in the strictly positive half-space. Every orbit configuration is 3-periodic in time, so

    ΘF(φ)=φ(−e_0)−φ(−2e_0)
          =φ(2e_0)−φ(e_0)=−F(φ).

The three time phases give F=0,−3/2,3/2, up to the convention for translation. Thus μ_bar(F²)=3/2 and

    μ_bar(F ΘF)=−3/2<0.

This is not a Wilson Gibbs counterexample. It rigorously rules out the purely abstract inference that translation averaging preserves the origin reflection positivity furnished by centered cubes, even if the original state has all hypercubic symmetries and both kinds of mirror positivity.

A genuine way to finish the free-cube route would be to prove, for every bounded local observable A in the target algebra and every lattice shift a,

    μ_C_R(A)−μ_C_R(τ_a A) → 0.

Uniqueness of the relevant infinite-volume Gibbs state is sufficient but stronger than necessary. One possible quantitative approach is interpolation between the plaquette couplings of C_R and C_R+a on their common union graph. The derivative of a local expectation is a sum of covariances with the O(|a| R^(d−1)) changed boundary plaquettes. A uniform decay estimate for these covariances throughout the inhomogeneous interpolation would prove the displayed convergence. Clustering in a single already-constructed homogeneous state does not by itself supply that estimate.

There is a primary theorem in a different coupling regime: Shen, Zhu and Zhu, *A stochastic analysis approach to lattice Yang–Mills at strong coupling*, [arXiv:2204.12737](https://arxiv.org/pdf/2204.12737), Theorem 1.2 and Remark 1.3, proves uniqueness and independence from boundary conditions for sufficiently small inverse coupling. In its normalization the action exponent is Nβ Σ Re Tr U_p, and the SU(N) condition is |β|<1/[16(d−1)]. Translation covariance of the dynamics then makes its unique invariant state translation invariant. This does not cover the large inverse couplings needed for the proposed asymptotically free continuum construction. No all-coupling SU(2) free-boundary translation-invariance theorem was verified in this audit.

## 8. SU(N) kernel audit

For completeness, let ξ(A) be the vector of real and imaginary entries of A∈SU(N), so ξ(A)∈R^(2N²), |ξ(A)|²=N, and

    Re Tr(AB*)=ξ(A)·ξ(B).

With standard Wilson normalization c=β/N≥0,

    exp[c Re Tr(AB*)]
      = Σ_{α∈N^(2N²)} [c^|α|/α!] ξ(A)^α ξ(B)^α.

The absolute sum is at most exp(cN), by Cauchy–Schwarz applied to Σ_k |ξ_k(A) ξ_k(B)|. All coefficients are nonnegative. The proof of §4 therefore extends exactly to any fixed SU(N), with no character-expansion assumptions, no large-N limit, and no gauge fixing. Reflection must preserve the directed endpoints of the two half-paths as specified in §3; otherwise one must first correct their orientations. Haar invariance under permutation and inversion handles the orientation conventions on individual reflected edges.
