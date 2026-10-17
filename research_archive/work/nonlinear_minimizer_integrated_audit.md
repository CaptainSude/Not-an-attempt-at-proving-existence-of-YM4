# Integrated audit of Notebook 15

Audited `outputs/ym4-nonlinear-minimizer-notebook.tex` after assembly of the cg-, wf-, nm-, ng- and ot- modules. Mathematical verdict: pass. The ordinary-constraint transfer has separate independent mathematical passes in `ordinary_constraint_transfer_audit.md` and `ordinary_constraint_transfer_second_audit.md`; this audit checks its interface and final scope against the preceding modules. No output file was edited.

## 1. Scope and normalization

The overview and final theorem consistently concern homogeneous finite compatible periodic regulators, fixed odd L, a fixed physical C^{1,alpha} global-potential ball, and sufficiently small arbitrary coarse potentials in the supremum norm. The ordinary constraint is the explicitly defined homogeneous iteration, not every geometry denoted by the deposited M_B. Equality means gauge equivalence, with no uniqueness assertion for the gauge parameter. The final small-class minimum is stronger than a pointwise local comparison, but the proof justifies it: every sufficiently small competitor enters one common strict-convexity ball after the two gauge operations, with uniform norm enlargement factors and smaller common radii.

The action counts each unoriented square once, has normalized color trace and no coupling in the bare four-dimensional density. Physical fine pairings are eta^d sums; analytic transposes are bilinear. The force module differentiates the ordinary potential action, while the deposited nonflat Delta uses a separately based simultaneous left exponential. The notebook explicitly distinguishes those Hessians and does not discard a background-current coordinate correction. The original-paper provenance qualification remains present. There is no identification of this homogeneous bare Hessian with a mixed-history effective Hessian or any quantum measure.

## 2. Interfaces

The constrained inverse is C=Gamma-DZD^T, has the exact two constraints, and is the inverse of the Maxwell form on X=ker Q intersect ker RD^T. Its same-exponent derivative-data Schauder estimate is precisely what the Wilson jet coefficient needs; no loss-of-exponent estimate is substituted. The jet density cancellation removes mesh powers before differentiating. Nonlinear coefficients remain before the exterior jet transpose, so the contraction does not differentiate a rough coefficient.

The nonlinear constraint estimates use the physical adjoint incidence factor and the genuine two-Hilbert-direction Hessian estimate. The exact stationarity equation includes its multiplier term. The real reduced Hessian retains the full constraint curvature, and flat energy coercivity controls both values and first differences without a fine Hilbert-to-pointwise estimate. The use of q versus q_aux=q+a_pen is consistent.

The gauge module uses the ordinary differential of the corrected fixed-reference map, not the separately based source Q(U). Its smooth scalar extension is the canceled biharmonic right inverse, with the constant-mode continuation and periodic gluing explicitly stated. The flow preserves the same corrected constraint, has integrable speed and converges within the actual gauge orbit. The tangent-space identification is now explicit. The ordinary transfer separately prescribes an induced coarse gauge with H_b and point values with E_pt; these two extensions are not confused. Gauge composition order and both comparison radii agree with the final theorem.

## 3. Notation bridges recommended to the assembler

These are editorial, not proof defects. The nm- module calls the ordinary-potential action mathcal S(A), whereas wf- calls it mathcal W_eta(A)=mathcal S_eta(exp(i eta A)); a single explicit alias would avoid ambiguity. The ng- module calls the fixed scalar projection R_0 rather than R, and its X_alpha norm is the same complete norm earlier denoted N_alpha or mathcal N_alpha. An explicit bridge for those names would improve readability. The broad S_jet=(I,nabla) estimate includes the selected four-slot plaquette jet, as already allowed by the cg- statement; the nm- use is that selection.

## 4. Mechanical validation

The assembled source has 136 unique labels and 93 references, with no duplicate labels or missing reference targets. Root reported successful compilation; this audit did not repeat it. The source citations in the normalization paragraph match the saved independent source-normalization check, including Raw I:12756–12760 and I:15643–15648.

## 5. Immediate envelope consequence

At a finite regulator put V(B)=S_eta(exp(i eta A_*(B))). Differentiate the exact chart A=xi+H(B-R(A)): DA[dot B]=H_A dot B+T_A Dxi[dot B]. Since Dxi lies in X and the corrected solution is stationary in the slice, the second term contributes zero to the action derivative. The already exact identity H_A^T E=m therefore gives DV[dot B]=<m,dot B>. This requires neither full constrained stationarity nor gauge coverage. The latter modules identify the same value with the ordinary representative's action.

The multiplier formula, A_*=HB+O(b^2), and the force/constraint estimates yield m(B)=qB+O(b^2) uniformly in coarse supremum norm. Thus D^2V(0)=q. Uniform holomorphy yields ||Dm(B)-q||_{infinity->infinity}=O(b) on a smaller ball. Spatially weighted Hessian locality is a further consequence only after the separately proposed weighted response estimate is checked. The scalar total action scales with volume: radial integration gives |V(B)-<B,qB>/2|<=C times (number of positive coarse bonds) times b^3, not a volume-independent total-action remainder.
