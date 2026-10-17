# Independent audit of finite-regulator classical relocalization

17 October 2026. Auditor: rotation_audit. Full read of finite_classical_contraction_research.md, with the requested detailed audit of Sections4--8. The finite Ward defect algebra in Section3 is used as the separately audited input; this audit independently checks its graded use and the subsequent repair/localization. No outputs edited or compilation performed.

Result: the mathematical carrier/norm argument passes. One scope clarification, already requested by root, is necessary in Section2: finite output invariance uses the actual small connecting gauge and a path remaining inside the activity ball, not merely gauge equivalence of its endpoints. The elementary estimate described below supplies that clarification. No correction to the contraction constants or parameter order is requested.

## 1. Finite-range jet repair

For each tail-coordinate symbol, the polynomial Taylor subtraction in z-1 has fixed relative range and coefficients O(delta_n). These are complex analytic z-derivatives at z=1, not an identification of midpoint and tail-coordinate moments. The preceding finite Ward input explicitly pays the analytic midpoint phases.

Slot permutation and reanchoring act by analytic monomial changes of the independent Laurent variables, fixing z=1, and possibly an analytic phase factor. Since the original kernel is slot symmetric, the permuted residual is the corresponding analytic pullback of F-J_mF. It still vanishes to order m+1. Thus averaging the repair over slots preserves the exact vanishing jets rather than restoring small jets accidentally. Range and norm remain bounded by fixed n,d constants. Separate point symmetry of the corrected kernel is unnecessary for the spatial argument.

The identity K_P=Per_P Khat+Per_P R+Ktail is exact. Neither the finite-range correction nor the wrapping tail is discarded or claimed separately gauge invariant. Their norms retain the correct degree-dependent factor b^(-n).

## 2. Exact periodic spatial algebra

The ordered Laurent divided-difference formula acts on one monomial with at most |r_j| output monomials and no increase of its total exponent length. Summing over directions inside the row norm loses at most |r|; the two exponent losses give the displayed 16 exp(sigma/2)/(e²sigma²) bound. The multiplication by -z_rho is the correctly signed conversion from two forward symbols to d_rho^- H d_tau^+.

Because the corrected quadratic symbol vanishes through order three, the twice-divided symbol has zero value at the identity. Periodic summation by parts therefore gives the gradient--gradient-difference identity exactly. Unlike the invalid naive symmetric-difference formula, this handles the odd/skew matrix part of a kernel. No infinite-volume summability of the periodic background is used.

The cubic expansion has precisely six remaining types after its zeroth and first moments are removed: two a,a,Rem terms, one a,ell,ell term, two a,ell,Rem terms, and one a,Rem,Rem term. Its algebra is valid for periodic fields and arbitrary integer lifted displacements; it does not require a single-valued affine function on the torus. The quartic telescoping uses only its zero moment. Repeated torus slots keep the usual multilinear multiplicities.

## 3. Complete-field near and far estimates

For m<=L all required field values and first differences lie in one fixed enlarged final-unit collar. The global coherent coefficient assignment means that restrictions to overlapping collars refer to the same coefficients. Thus physical C1alpha control applies before the support sum.

With h=1/L, the bounds a=O(bh), Da=O(bh²), translated Da difference=O(bh^(2+alpha)|r|^alpha), and Rem=O(bh^(2+alpha)|r|^(1+alpha)) give:

* quadratic O(b²h^(4+alpha)|r|^alpha);
* cubic O(b³h^(4+alpha)(1+m)^6), including the a,ell,ell term since h^5<=h^(4+alpha);
* quartic O(b^4h^5(1+m)).

The negative-edge convention is correct: its positive difference is read at the lower endpoint, and the same discrete Taylor remainder follows.

For m>L, keep the field factors at separate endpoint roots. The first-difference norms give quadratic O(b²h^4). Bounding a shifted field by O(bh), ell by O(bh²m), and Rem by O(bh(1+m)) gives the stated cubic O(b³h³(1+m)²). The quartic difference is bounded by two field norms and is O(b^4h^4). Fixed moments absorb the polynomial factors. With the later L^4 anchor count, these far terms cost at most a constant times (L+2)exp(-sigma L/8), which is bounded by a fixed multiple of L^(-alpha).

## 4. Carrier geometry on the periodic quotient

The construction correctly projects only the endpoint roots and each terminal set {root} union X, then selects the short macro graphs guaranteed by the projection lemma. It does not require retaining the full projection of a poorly chosen fine tree. Their connected union contains the anchor macrocell and every read variable.

Shortest torus trees and their projections satisfy the same estimate

    T_H <=(2/J)[tau(roots)+sum tau({root} union X)]
                         +4[n0+sum|X|]

in d=4. Repetitions or wrapping can only reduce the number of vertices once duplicates and redundant edges are removed. The inequality |H|<=1+T_H and dist(z,j(x))<=T_H give the rerooting inequality in (5.6) directly. The budget A>=4(a0+1), 2(a0+1)/J<=kappa pays the support factors at the target exponent a0.

There are exactly (JL)^4 input anchor sites per final J-cell when J divides N. The sum of the torus weights exp(-dist) is at most the infinite S1 by an injective choice of shortest representatives. Thus the sole extensive anchor count is (JL)^4. Direction/color counts and the fixed number of field factors contribute only fixed constants. No extra number of output coordinates or support roots has been introduced.

For a far tuple, a tree connecting its final-unit endpoint roots has length O(m/L+1); after projection the carrier factor is at most a constant times exp(C'm/(JL)). Taking L large enough after J absorbs it into the kernel exponent. All periodic estimates are independent of the volume above the stated collar threshold.

The notation dist_N in the rerooting display should be read as distance on the final J-cell quotient, while tau_N before projection is on final unit cells. This distinction is already clear from the construction; making it explicit would be an optional notational improvement.

## 5. Wrapping tails and finite jet corrections

For a torus kernel with exp(mu D_P) row bound, the first-slot-to-endpoint shortest paths give a root tree of length at most C_n(D_P/L+1). Fixed midpoint offsets change only the additive constant. After projection its root cost is at most exp(C_n'(a0+1)D_P/(JL)); choose L so its exponent is at most mu/4.

The endpoint product contributes (Cb/L)^n and the anchor sum (JL)^4, yielding C(J,n) A_n b^n L^(4-n). If D_P>T0, the unspent exponent gives exp(-mu T0/2). Applied to Ktail, A_n=O(epsilon b^(-n)), so the field factor cancels the full b loss. Applied to the fixed-range repair, its already small coefficient bound gives the same cancellation and exp(-cP) error. Summing degrees2--4 gives (L²+L+1)epsilon exp(-cLN).

This argument works at the output carrier scale and keeps the full a0 exponent. It does not invoke the old-scale tail representation that loses cardinal exponent. The remaining polynomial L factor is explicit and harmless for fixed L or for the final large-L choice.

## 6. High jets and quotient norm

The degree>=5 coefficientwise projection costs at most six and its supported transport contributes 6C_high epsilon/L. Increasing the endpoint L after fixing a sufficiently large base R,J decreases the compression coefficient; the same fixed tail budget remains valid. The field-scaling disk requires a final b reduction after L, as explicitly stated. It does not force a new J depending on L.

The total linear sector vanishes by adjoint invariance and the constant sector is removed by normalization. Coefficientwise vanishing is unnecessary. The repaired low kernels plus their retained errors, together with the high-jet family, represent the complete finite normalized total on the original b polydisc.

Taking a representative arbitrarily close to the input quotient infimum, constructing this output family and applying the output projection gives exactly the two C_ext factors in (8.1). They are b independent because the actual reference has an O(b²) representative. The norm estimate does not require a canonical or norm-minimizing representative.

The order fixed J, then L=R^q, then a compatible lower period threshold and finally b is noncircular. The constants in the leading two terms are fixed before L; the error uses the actual input period LN. No actual finite reference is replaced by a canonical infinite-volume periodization.

## 7. Finite gauge-path and induction scope

For output local invariance, the actual ordinary-minimum equality construction supplies a gauge close to identity. The finite link orbit equation and a common small logarithm give |D log g|<=C(|a|+|a'|)<=Cb/L. Its paths g^t therefore keep transformed link potentials at most Cb/L, after fixed matrix/coordinate norm comparisons. Taking L sufficiently large gives a strict b margin. The argument applies to the relevant spatially transformed endpoints as well. Thus the finite invariant quotient assertion is justified without invoking an infinite constant-at-infinity argument; endpoint orbit equivalence alone would not suffice.

The result gives a small exactly equivalent finite representative of the extracted classical output. It does not make the original carrier array small. A sequence of cutoff quantum steps keeps all intermediate Gaussian factors and windows. Actual finite quantum descent, strict budgets at every intermediate step, running-coupling control and vacuum normalization still need their own statements. The note retains those limitations correctly.
