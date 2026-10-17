# Second independent audit: the classical coarse action

16 October 2026. Read `work/classical_coarse_action_research.md` in full and checked its dependence on the ordinary-constraint minimum and weighted response proofs. Status: pass; no correction needed.

## 1. Envelope and volume normalization

Differentiating the exact constraint chart yields `DA_*[c]=H_A c+T_A Dxi[c]`. The second term is an actual constrained fixed-gauge tangent, because `Dxi[c]` lies in the fixed linear slice. Slice stationarity alone therefore removes it from the action derivative. This proves `DV[c]=<H_A^T E,c>` without presuming a full-constraint multiplier theorem.

The transpose push-through identity gives the displayed ordered formula for m. The flat identity `H^T K A=q Q A=q[B-R(A)]` is correct, with the semidefinite Maxwell coarse form q rather than the positive auxiliary q+a. The force transpose is evaluated as `(S_jet H)^T f`, so no coefficient derivative is estimated pointwise.

All nonlinear corrections to m are quadratic in `b=||B||_infinity`, including the correction from the multiplier inverse. Cauchy on a circle of radius b bounds `Dm(B)-q` by `O(b)` on a sufficiently small ball; the radius stays inside the larger analytic ball since `||B+z c||<=2b` for a unit direction. The zero-background case follows from the quadratic Taylor remainder.

Integration of the envelope identity gives the stated cubic action remainder. Its factor N_b is necessary and correct: the final coarse measure is counting measure, and the normalized color trace contributes only a fixed component constant. The claim is uniform per coarse volume, not a volume-independent bound on total action.

## 2. Both gauge comparisons fit the common radii

The bound `||B^g||<=C_c(b+w)` with `C_c>=1` is uniform because the final spacing is one and a coarse bond has two endpoints. It does not require fine-type regularity of the coarse gauge parameter.

With `b+w<delta`, the first competitor has potential norm at most `C_G(C_A b+C_E w)`. The second uses the independent minimizer at the transformed target and has norm at most `C_G(C_A C_c(b+w)+C_E w)`. Both are bounded by the common expression `C_G(C_A C_c+C_E)delta`, which is strictly less than r_0/2 under the stated choice. The targets B and B^g both remain inside b_0. The additional requirement that all gauge-action and logarithm arguments lie in their analytic domains can be met by one further fixed reduction of delta.

Ordinary covariance gives the two target constraints in the correct order, including `(D^g)^(g^-1)=D`. Minimality therefore gives inequalities in both directions and hence equality. The proof does not assume that the gauge image of one selected minimizer is the selected minimizer at the other target.

The real equality holds on an open subset of the full real form of the finite-dimensional (B,omega) space. The holomorphic identity theorem then applies coordinatewise on a connected common complex product ball. This extends the equality, not the real minimum interpretation.

## 3. Classical Ward identity

For the left exponential differential `J_B`, ordinary potential variation and left group variation are related by `delta D D^-1=i J_B delta B`. The coarse gauge velocity is `i omega_-D-D i omega_+=-i(D_D omega)D`. Thus the displayed velocity `-J_B^-1 D_D omega` has the correct sign and no missing scale factor.

Using `DV=m` and the physical coarse bilinear transpose gives exactly `D_D^T J_B^-T m=0`. The left-coordinate current is therefore `j_cl=J_B^-T m`, not m itself away from zero. The statement extends holomorphically for the same reason as the gauge identity. No determinant or quantum Ward identity is being introduced.

## 4. Weighted Hessian and the auxiliary inverse

The required weighted estimate for `Dm(B)-q` is a consequence of the audited multiplier variation formula together with the weighted response bound for `DA_*`: the terms beyond `q c` are all `O(||B||_infinity)||c||_w`. It is also correctly isolated as an explicit hypothesis in the note.

At finite volume, a centered decaying weight permits a test input whose component magnitudes are `exp(kappa d(i,j))` and whose phases align the chosen output row. Such a direction is large but finite; the derivative is linear, and its weighted norm is one. The estimate therefore controls the weighted absolute row sum. A fixed color/orientation factor converts scalar entries to block norms. Symmetry of the Hessian under the physical bilinear transpose gives the column bound, including for complex backgrounds. On an infinite lattice the row argument can instead use finite-support test inputs and pass monotonically to the sum, avoiding any ambiguity about unbounded tangent directions.

The Schur norm bounds the physical Hilbert operator norm. Thus the positive real baseline `q+aI>=a_-I` and a perturbation of norm at most `a_-/2` give the asserted Hermitian-part lower bound on the complex domain. The weighted Neumann condition is independently `r_kappa C'_kappa b<=1/2`; both restrictions can be imposed by one common smaller radius. The inverse bound and the difference bound `2 r_kappa^2 C'_kappa b` follow from the exact resolvent identity.

The resulting precision is an auxiliary classical coarse object. The note accurately retains the distinction from an integrated quantum effective action, a physical mass gap, and strict background-support locality.
