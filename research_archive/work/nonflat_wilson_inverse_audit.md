# Independent audit of the Wilson energy-inverse candidate

16 October 2026. Full audit of `nonflat_wilson_inverse_research.md`, with priority on Sections 4--6. No substantive mathematical correction found. The conclusions remain conditional on the exact source-action identification stated there, and concern the augmented first-derivative energy block only.

## Wilson normalization and local form

The normalized analytic density `1-tau(P+P^{-1})/2`, multiplied by `eta^{d-4}`, has Hessian exactly `d^T d` at the identity with the physical pairing `eta^d sum tau(BC)`. There is no missing factor two. The reverse-edge increment `-Ad(U_f^{-1})B_f` and the ordered transport of all four exponential insertions are exact, also with repeated periodic incidences. Expanding the product gives the commutator correction in (3.1) with the displayed factor one half.

The reverse-loop principal term becomes the forward transported curl by cyclicity of trace, yielding exactly the symmetric plaquette multiplier (3.5). The remaining trace commutators can be multiplied by P-I because their trace at the identity vanishes. The curvature estimate pays for the two inverse mesh factors in both the remainder and `C_U^T(M_U-I)C_U`. Thus W_U is genuinely bounded of order `epsilon_1+epsilon_0^2`, rather than an unbounded lower-order differential term. The expansion (3.8) then gives the claimed first-derivative small-form representation.

## Scalar compression and zero modes

The scalar Woodbury coefficient is `P0/D_s1`, with `D_s1=A+P0(R_s1+1/a')`; the canceled central entry and both central/high entries in (4.5) follow exactly. A fine derivative on each side leaves bounded high diagonal multipliers and square-summable rank factors. The previously proved common analytic tube and physical-cell reconstruction therefore provide (4.6) without a fine-dimensional loss.

Directly, `G'_0 Q0^T=L^{-1}Q0^T/(1+a'W1)` on nonzero fibers, so `C0=W2/(1+a'W1)^2=D_s2/N^2`. Hence its inverse really is `N^2/D_s2`. The enlarged-cube positivity and common complex shrinking control all these scalar denominators uniformly. The zero coarse fiber gives `C0=(a')^{-2}`; M=1 gives `(P0+a')^{-2}`. No massless zero-mode inverse is used. Periodic gluing and contour shifting are justified by equality with the real-fiber compressed operators, as in the existing flat proofs.

## Perturbation algebra and gauge closure

The form-resolvent ordering `G-GS^T V(I+KV)^{-1}SG` is correct; multiplying by A+S^TVS verifies it at each fixed mesh. The same Neumann series gives the sharp geometric estimates stated for the augmented block. Including I in S ensures all smaller rectangular blocks needed later are available.

The scalar precision difference has the required S_s-form, after which G'_U and C_U are O(epsilon) perturbations in the same weighted algebra. Crucially, the separate C0 inverse bound makes the Gram inverse stable. The expression for R_U is algebraically idempotent; on real symmetric data its middle matrix is the Gram matrix of `G'_U Q_s(U)^T`, so it is the asserted orthogonal projection.

The gauge difference (6.10) does not ask for a uniform norm of a bare derivative. The divergence D^T is a fixed backward-shifted component combination of the ordinary gradients already in S_v. Those shifts have uniformly bounded physical-cell weighted norms. All four gauge-difference terms therefore have bounded small coefficients between the first-derivative energy legs. The final one-form inverse is a second application of the same form-resolvent argument, with no extra derivative or mesh loss.

The weighted algebra is submultiplicative, transpose preserving and dimension independent under the physical-cell normalization. Fixed positive penalties and sufficiently small coefficients give the real relative-form coercivity in every application. The result does not imply one-sided second-difference or nonflat pointwise bounds, and the note appropriately excludes them.

## Minor presentation clarifications sent to the author

1. The real relative-coercivity sentence in the abstract Lemma 5.1 should say that the baseline A is positive; it is positive in every actual use in the note, but mere real symmetry is not sufficient in the abstract formulation.
2. The constants in Section 6 use the uniform weighted norms of the flat Q and Q0. These are already known from their flat contractions and finite physical range; one sentence stating that fact makes the hypothesis bookkeeping explicit.
3. Equation (3.2) has the LaTeX typo `\tau\!left(`, requiring `\tau\!\left(`.

These do not change the theorem in its stated actual flat-baseline setting. The source-action normalization and chart match remain separate interfaces, as required by the candidate's scope.
