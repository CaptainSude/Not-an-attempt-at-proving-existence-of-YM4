# Audit of assembled Notebook 11 and its factorial corollary

16 October 2026. Independently read `ym4-full-flat-current-candidate.tex`, comparing its mathematics with the passed full constraint-current research proof and the stronger sup-row estimate in `flat_full_constraint_current_audit.md`. **Pass. No mathematical, label, or reference correction is required.** No output or candidate was edited.

## 1. Assembly and source scope

The assembly retains the exact corrected-coordinate bridge, the endpoint/BCH terms, the distinction from the later rooted quadratic vertex, the physical h/L coefficient, and the fixed-L composition. The refinement sequence is explicitly `M=L^j` with fixed odd L>=3. The source scale ell is one, not eta; physical and scalar penalties remain distinct.

The geometric sum and physical pairings are unchanged from the passed proof. The stronger fine sup lemma carries the exact row constant

    2 L^(d-1) h N_L m_L K_L^coef,

including the coarse/fine volume ratio, the quadratic h/L factor, and the factor two in the defining form. Its multilevel operator identity uses the physical adjoint Q*. Both that adjoint and Q have normalized nonnegative rows, so the contraction argument and summation of h_t are correct. The weighted extension pays a fixed final-range cost, not a fine dimension factor.

The coefficient weight E_J^T J is estimated using physical cell volume and rectangular Schur rows, so bounded currents in infinite volume are allowed without a global L2 assumption. The full inverse uses the Hilbert norm of Pi and does not infer Pi:sup->sup. The separate pointwise limitation is retained.

The two Neumann inverses, the displayed full radius, and the outside-factor fine-derivative identity agree with the audited proof. The full first-response formula has the correct sign and is described as not forced to vanish by the auxiliary cancellation. No unsupported nonvanishing example is asserted. The source identification remains explicitly a check of deposited transcriptions, not an independent full-text verification of CMP98.

## 2. The added Cauchy corollary

Let r=epsilon_1-||J||_infinity>0 and initially assume every direction K_i is nonzero. For every 0<r'<r, the polydisc

    |z_i|<=r'/(n||K_i||_infinity)

lies in the open current ball, by the triangle inequality. The Banach-valued holomorphic function T(J+sum_i z_i K_i) has uniform norm at most M_T there. Its coefficient of z_1...z_n is precisely the mixed Frechet derivative D^n T(J)[K_1,...,K_n]. There is no extra n! here: the Taylor factor 1/n! is canceled by the n! orders of the distinct directions.

Multivariable Cauchy therefore gives

    ||D^n T(J)[K_1,...,K_n]||_kappa
      <=M_T n^n (r')^-n product_i ||K_i||_infinity.

Let r' increase to r and use n^n<=exp(n)n!. This proves exactly the displayed factorial estimate. Zero directions follow by multilinearity. The notation e_num=exp(1) correctly avoids collision with the extension constant e=g b q. The result holds for the full nonlinear-current family because only holomorphy and the uniform bound are used; it does not reuse the auxiliary ordered derivative chains. The radius is the distance to the current-ball boundary, so no uniform derivative bound on the entire open ball is incorrectly implied.

## 3. Mechanical checks

The assembled source has 34 labels, all distinct. All 15 explicit internal references resolve. The built-in LaTeX compiler reported success for the complete candidate. Named prior notebooks are declared inputs, and no theorem in this document purports to prove their prior Fourier or scalar-gauge results again.

## 4. Result

The integration and added corollary are ready within the stated homogeneous flat, fixed-L, weighted physical-cell scope. No nonflat, mixed-history, pointwise-projection, or interacting-limit conclusion has been introduced by the assembly.
