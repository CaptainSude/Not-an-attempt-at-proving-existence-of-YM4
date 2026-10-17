# Independent audit: total-kernel Ward extraction

17 October 2026. Read `total_kernel_ward_extraction_research.md` §§1–9 against the original CMP109 proof map saved in `renormalized_induction_primary_sources.md` §§7–10. No compilation or output edits.

**Result: mathematical pass, with one explicit midpoint-notation clarification requested for the quantitative moments.**

## Exact algebra

For Hermitian coordinates, positive bond b and dλ=λ_+−λ_-, direct differentiation of exp(itλ_-) exp(iA) exp(−itλ_+) gives the displayed generator `i[λ_-,A]−f(i ad_A)dλ`, with f(z)=z/(1−exp(−z)). Its first and second field orders are precisely the L and Q in (3.2). In particular Q(A,A)=1/12[A,[A,dλ]], with the positive sign. The diagonal and polarized Ward coefficients in (3.3)–(3.5) have the correct factorials.

Midpoint phases turn dλ into `2i sin(k_mu/2)λ`, the endpoint average in L into `i cos(k_mu/2)[λ,a]`, and Q into the stated `(i/12) sin(k_mu/2)` times the two commutators. There is no hidden singular momentum factor. Full spatial inversion contributes one minus sign per bond leg, giving the parity used in the proof.

The quadratic classification is sound under the actual continuous limiting-kernel hypotheses. For the residual after subtracting the full invariant reference, the cubic Ward right side is order four in simultaneous momentum. Thus the linear cubic tensor is transverse in every leg. With independent p,q and k=−p−q, p-transversality kills all q coefficients and q-transversality then kills all p coefficients. This argument is valid for each color tensor and leaves no antisymmetric exception. The quartic right side is order three or higher; its degree-one Ward left side forces the constant quartic tensor to vanish. Parity supplies the stated improvements to orders three and two.

The reference action must be subtracted as a full invariant functional; a subtraction of only its Hessian would invalidate these nonlinear Ward deductions. The sign and factors in the Wilson completion follow from the plaquette expansion `P=I+i t²(f+i[A_mu,A_nu])+O(t³)` and the normalized density `1−tau(P+P^-1)/2`. The rebasing identity (8.2) is algebraically correct and makes no unsupported beta-sign assertion.

## Kernel bounds and limits

The coordinate Cauchy count and anchored reserve loss in (2.2)–(2.3) are valid fixed-order bounds. They retain D and J dependence. On exhausting cubic tori the diagonal subsequence, Fatou bound and exponential tail control supply limiting kernels and their finite moments. Exact total Ward identities pass by testing finite-support directions/gauges; no separate invariance of individual activity coefficients is needed. The note correctly avoids claiming a unique limiting kernel, exact finite-torus continuous-momentum identities, or convergence of extensive vacuum sums.

For (9.1), define each `xi_j` explicitly as the bond midpoint `x_j+e_(mu_j)/2`. Then the phase in (4.1) is exactly bounded by the displayed moment, and Taylor's real-ray integral remainder gives the /4!, /3!, /2! constants in (9.2). If tail coordinates are used instead, an additive orientation-distance correction is required. This is a notation clarification, not a change to the classification.

## Comparison with the primary proof and remaining scope

CMP109 pp283–284, (4.9)–(4.15), derives the same infinitesimal hierarchy in uncentered coordinates. Its pp286–292 spatial Taylor/Ward procedure and full-action subtraction ultimately reduce the marginal sector to the same quadratic coefficient; pp294–298 classify the polarization tensor and cancel the associated terms. The present note supplies a different, independently checkable midpoint polynomial proof at the level of limiting total kernels. It does not assert that the source's coefficientwise gauge/orbit-domain hypothesis (1.19) follows from total invariance.

The stated remaining obligations are real: localizing the canceled scalar functional with a bounded norm, controlling periodic wrapping/volume choices, and establishing a noncircular scale gain with the J-dependent kernel constants. The classification alone does not close the amplitude recursion or determine the running coupling.

## Fragment fidelity

Read `total_kernel_ward_extraction_fragment.tex` in full after the midpoint clarification. It preserves the audited hypotheses, phase conventions, exact algebra, reference normalization and scope. The added conversion to ordinary tail-anchored momentum coordinates is sound: multiplication by an analytic nonzero phase cannot lower the residual vanishing order. No mathematical transcription correction found; no compilation was run.
