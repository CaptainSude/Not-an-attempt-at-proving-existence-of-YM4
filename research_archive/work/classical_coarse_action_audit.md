# Independent audit of the classical coarse action module

16 October 2026. Audited `work/classical_coarse_action_research.md` and the complete `work/classical_coarse_action_fragment.tex`. Result: pass. The fragment retains the finite homogeneous regulator, uniformly small global background, and classical-action scope. No mathematical correction remains requested.

## 1. Exact envelope and normalization

The chart derivative is `D_B A[c]=H_A c+T_A D_B xi[c]`. Since `D_B xi[c]` lies in the fixed linear slice space, its image under T_A is a genuine tangent to the nonlinear constraint within the fixed gauge slice. Slice stationarity therefore kills that term when paired with the ordinary-potential Euler derivative. This proves `DV[c]=<m,c>` without assuming a separate full-constraint Lagrange multiplier theorem.

The transpose push-through formula is ordered correctly:

`H_A^T=(I+H^T DmathcalR(A)^T)^(-1) H^T`.

Using `H^T K xi=0` and `H^T K H=q` then gives the exact multiplier already present in the minimizer proof. The physical Maxwell q, rather than q plus the auxiliary penalty, occurs in that formula. The term H^T N is evaluated by transposing the differentiated extension and therefore does not introduce a derivative of a rough force coefficient.

The holomorphic identity between the corrected and ordinary representatives' action values is valid: the analytic Wilson density uses the trace of P and P inverse and is invariant under complex gauge conjugation. Real minimization is not extended to complex fields.

The estimate `m-qB=O(b^2)` follows with uniform vector norms. The directional Cauchy circle of radius b around a background of norm b lies in a ball of radius 2b, so it correctly yields `Dm-q=O(b)` after restricting to a fixed smaller domain. At b zero the Taylor coefficient gives the same conclusion. Radial integration correctly gives the factor one half in the quadratic action, and its cubic remainder is proportional to the number of positive coarse bonds. No total-action estimate independent of volume is claimed.

## 2. Coarse gauge invariance and analytic continuation

The two minimum comparisons use genuine but distinct competitors. The first is U_ord(B) transformed by a smooth fine lift h of the coarse gauge g; it is feasible at B^g. The second is the separately constructed U_ord(B^g) transformed by h inverse; it is feasible at B. Ordinary covariance and the gauge composition convention give `(D^g)^(g inverse)=D` with the correct order.

The explicit margins `C_c delta<b0/2` and `C_G(C_A C_c+C_E)delta<r0/2`, together with the stated reduction for all analytic domains, control both data and both competitor norms. Because C_c is at least one, these margins also cover the first, simpler comparison. Arbitrary bounded coarse gauge parameters are allowed; their physical scale is one and E_pt supplies the smooth fine lift uniformly. No derivative of a rough fine gauge is assumed bounded without this lift.

The equality on a real open set extends to the smaller connected complex product ball by the finite-dimensional holomorphic identity theorem. This is legitimate on each finite regulator and does not require a radius depending on its dimension; all analytic domain bounds are uniform beforehand.

## 3. Ward sign and coordinate Jacobian

For `D^g=g_- D g_+ inverse`, the left link velocity is `i(omega_- - Ad_D omega_+)`, which is minus i times the displayed D_D omega. Therefore the ordinary coarse-potential velocity is exactly `-J_B inverse D_D omega`. There is no extra scale because the final coarse spacing is one.

Applying the envelope identity and the physical bilinear transpose yields `D_D^T J_B^(-T) m=0`. The order of the transpose and Jacobian is correct. The current in the left exponential coordinate is `J_B^(-T)m`; the module correctly distinguishes it from m. This is a classical Ward identity, not a statement about a quantum measure or determinant.

## 4. Weighted Hessian extraction

The previously audited weighted multiplier derivative gives an operator estimate for every admissible weight. The centered decaying weight `w_n(m)=exp(-kappa d(n,m))` is admissible. For one scalar output row, input entries of magnitude `exp(kappa d(n,m))` with phases matching the complex row entries have weighted bounded norm one. The weighted estimate therefore controls the exponentially weighted absolute row sum.

Color and orientation have fixed finite dimension, so passage from scalar entries to matrix blocks costs only a fixed component factor. Physical coarse transpose symmetry of the Hessian gives the same bound for columns. The resulting Schur norm bound is therefore valid at complex backgrounds as well. On finite regulators these row-testing directions are bounded, even though their unweighted norms can grow with the diameter; the already uniform weighted linear estimate is what is used. The infinite-lattice unbounded-direction subtlety is not silently imported into this finite theorem.

## 5. Positive auxiliary precision and inverse

For a fixed compact positive interval of penalties a, the established flat baseline gives a common spatial exponent and a uniform weighted Schur bound on `(q+aI) inverse`. The perturbation estimate `||Q_cl-q||_kappa<=C b` controls its ordinary Hilbert operator norm by Schur's inequality. Hence the Hermitian part of `Q_cl+aI` is at least a_- minus that perturbation, even at complex backgrounds. The fragment explicitly distinguishes this Hermitian numerical-range pairing from the bilinear analytic transpose used elsewhere.

The Neumann series in the weighted Schur algebra has the correct radius and constants: inverse norm at most `2 r_kappa`, and difference from the flat inverse at most `2 r_kappa^2 C b`. Holomorphy follows from the uniformly convergent series. This is an auxiliary positive classical operator; it does not supply a physical mass gap or an integrated quantum precision.

## 6. Conclusion and scope

All requested interfaces pass: exact envelope, common gauge-comparison domains, Ward sign/Jacobian, weighted Hessian, and auxiliary inverse. The proof is uniform in refinement and finite periodic volume, but only for the stated small global potential/coarse-data regime and the homogeneous averaging construction. The final paragraph correctly leaves fluctuation determinants, Jacobians, quantum interactions, mixed histories, and continuum measures outside this theorem.

The integrated Notebook 16 additionally spells out that Q_cl differentiates in the ordinary coarse potential B, whereas a based left-exponential Hessian requires Jacobians and a background-current coordinate-curvature term. This is correct and prevents an unwarranted identification with a source fluctuation precision. Its R_0=R notation bridge and the overview/final scope statements are consistent with this audit.
