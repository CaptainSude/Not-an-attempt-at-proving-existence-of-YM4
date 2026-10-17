# Independent audit of composite-macrostep symmetry

17 October 2026. Audit of `composite_macrostep_symmetry_research.md`, without changing its text or the outputs. This is an internal mathematical check, not independent certification of the construction.

## Result

The stated local-sector symmetry and subsequential Hessian classification pass. No mathematical correction was found. Their finite-volume and total-functional qualifications are essential.

## Checks

1. The source permutation property of the selected mean, together with the already established endpoint covariance, makes transformed coordinate-order contour families give the transformed internal contour. The centered odd hierarchy is preserved by final-lattice translations and signed permutations on cubic regulators. This does not imply current-unit translation invariance of a fixed macroblock sector. The pure-gauge root/nonroot example correctly disproves the latter.

2. The ordinary reversed-bond identity is exact: if `X=U T^{-1}`, then `U^{-1}T=T^{-1}X^{-1}T`, so the logarithm is `-Ad_{T^{-1}} log X` and the averaged bond reverses by inversion. For relative fields the transformation is `B -> -Ad_{V^{-1}} B`, not merely `-B`. At a real background it preserves each retained color Euclidean ball and has absolute Jacobian one. The selected pivot set is preserved. Uniqueness of the nonlinear pivot solution then proves the full chart identity, and the pivot/coarse orientation determinant signs cancel. The argument accounts for the complete nonlinear straightening density as well as the Gaussian Hessian.

3. The physical branch transforms by constrained-minimum/uniqueness comparison. No covariance of an arbitrarily chosen auxiliary representative is needed. The proof correctly treats the actual total integral, requires the inherited total to have the spatial symmetries, and uses nonvanishing plus a compatible logarithm branch. Auxiliary grouping and asymmetric deterministic carrier hulls need not preserve coefficientwise symmetry.

4. The measurable large-field completion can depend on an ordered reference contour. Its global spatial covariance has not been established by the local argument; the note explicitly preserves this distinction. The SU(2) charge-conjugation assertion follows from its inner implementation. Outer-automorphism covariance for an unspecified mean is correctly conditional.

5. The Hessian estimate (6.4) follows from scalar Cauchy, at most `D |H|` possible second coordinates, and the connected-carrier distance bound. Its constants retain the fixed grouping size J. No volume or earlier-refinement factor is hidden. The exponential estimate supplies fixed spatial moments and a diagonal subsequence on exhausting cubic tori.

6. Finite-torus Ward identities alone do not force the zero-momentum Hessian to vanish. In the infinite subsequential kernel, the position-space Ward relation passes locally and exponential summability makes its Fourier transform analytic. Taking momentum `p=t e_mu` in the continuous Ward relation proves `K(0)e_mu=0`, hence `K(0)=0`. This avoids a finite-period interpolation error.

7. With midpoint phases, signed permutations act as ordinary vector transformations. Full inversion makes the Hessian symbol even. Reflection parity and permutations reduce its degree-two tensor to the three constants A,B,C shown in (8.1); transversality forces A=0 and C=-B. Global adjoint invariance leaves one coefficient per simple ideal, rather than one coefficient for an arbitrary semisimple product.

8. The remainder constants are safe. The scalar cosine remainder and the absolute row moment give `M_4 ||p||_infinity^4/24`. The sine-versus-momentum replacement has row error at most `(d-1)|beta| ||p||_infinity^4/6`, so the stated `d/6` constant is conservative. Symmetry permits the row bound to control the real operator norm.

## Clarification sent to the author

The uniform flat normalization `q_M,mid(p)=|p|^2 I-p p^T+O(|p|^4)` is already supplied by `flat_covariance_decay_research.md` Section 10 and its Notebook07 transcription. It is useful to cite that proof in the final scope discussion. The note is still correct that ellipticity alone would not supply it.

## Scope retained

This is a subsequential total-kernel result, not convergence or uniqueness of the activities, a measure limit, an asymptotic-freedom coefficient, or a nonlinear subtraction theorem. In particular its constants can depend on J; a later scale-gain argument cannot silently choose R first and then treat J-dependent moment constants as fixed before R.

## Fragment fidelity

The full no-preamble `macrostep_symmetry_fragment.tex` was subsequently read. It faithfully carries the audited proof, its constants and finite-period qualifications. It now explicitly assumes reality on real fields for a real beta and cites the already available uniform q_M normalization. No mathematical correction was found. No compilation was run by this auditor.
