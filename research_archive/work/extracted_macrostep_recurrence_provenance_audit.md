# Independent audit of the extracted macrostep recurrence

17 October 2026. Auditor: provenance. Audited the current saved `extracted_macrostep_recurrence_rotation_research.md`, including the updated quantum-descent discussion and Section5.1. No output edits or compilation.

## Result

The mathematical recurrence passes. The exact reference identity, projection telescope, Duhamel estimate, common intermediate-domain control and quadratic-force envelope are correct under their stated common-system hypotheses. The distinction between prescribed weak couplings, an actual density-preserving coupling update, and uniform actual finite-regulator families is essential and is correctly retained. The quantum local-limit theorem is now an established adjacent input, not an unresolved consequence of a family norm bound.

## 1. Actual reference, not merely its quadratic normalization

The comparison is on the same fine oriented graph. Put U2=U_(MR)(W), D=M_ell^k U2, and U1=U_M(D). The inner ordinary constraints coincide, and ordinary composition makes both outer constraints W. At fixed finite R the physical field conversion A^W(x)=R A^D(Rx) has C^(1,alpha) factor at most C R^(2+alpha). The pre-gauge amplitude estimate and a smaller real input radius place both fields in both comparison neighborhoods, uniformly in preceding M and volume. The inner minimum gives one action inequality and the outer minimum the reverse. In d=4 the coupling-free Wilson plaquette sum has physical prefactor eta^(d-4)=1, so neither comparison contains an unrecorded factor of R. Both references vanish at the trivial field. Holomorphic uniqueness extends the real germ equality on the common connected product domain.

The flat midpoint q_M symbol has Maxwell coefficient one, and its identification as the Hessian of the actual homogeneous constrained action was established separately. Therefore beta(S_M)=1. Ellipticity alone would not provide this normalization, and an arbitrary other reference with beta=1 would not obey the full transport identity. The note makes both distinctions.

On the joint infinite system, compact normalized totals and summable-field substitution pass the identity. No extensive infinite action value is assumed to converge. The exact identity is T_j S_j=S_(j+1), with no vacuum ambiguity because the chosen classical actions vanish at zero.

## 2. Projection algebra

P_(j+1)T_j P_j=P_(j+1)T_j follows by subtracting beta_j(x)P_(j+1)T_j S_j, which is zero. It does not require beta_(j+1)T_j=beta_j. Applying this identity repeatedly removes all intermediate projections from the classical product; the final and initial projections stay. The actual scalar semigroup then converts the product to a direct R^q background substitution, in the quotient only. Carrier-by-carrier equality is unnecessary and is not asserted.

The norm of each full-reference projection is p=1+C_beta C_S independently of the inner radius. This uses the fixed-outer-radius O(b^2) reference representative; the b^(-2) norm of beta has not been omitted. The displayed p^2 in the block bound pays the two endpoint projections. With J fixed, q can be selected after J to beat its finite spatial-moment constant; b is selected only afterward.

## 3. Quantum comparison and Duhamel calculation

The updated Section3 correctly invokes the proved quantum local-limit/periodization theorem on one input-independent classical system. Near-minimal covariant representatives Y for y and D for x-y, followed by X=Y+D, place both complete inputs inside the family ceiling. This is the correct way to pass a family difference bound to the quotient; independently minimizing X and Y would not suffice.

For equal prescribed step couplings, the variation-of-constants identity is exact. Bounding the initial linear q-product by theta_q and all shorter products by powers of B gives

    theta_q + nu sum_(k=0)^(q-1) B^(q-1-k)(B+nu)^k
       = theta_q+(B+nu)^q-B^q.

The weaker q nu(B+nu)^(q-1) bound is valid for B,nu>=0, including nu=0 by continuity. The argument uses only a long-product improvement on the initial term and does not inadvertently assume contraction of shorter products. All intermediate differences remain controlled by (B+nu)^k.

With K=B+1, nu<=min(1,1/[4qK^(q-1)]) and theta_q<=1/4, the block Lipschitz bound is at most 1/2. For r=epsilon_bar/(8K^q) and fLq<=r/2, all intermediate states have norm at most epsilon_bar/8+r/2<epsilon_bar/4. The zero-started block output is at most fLq, so the radius-r ball is invariant. Both the original trajectory and the zero-started comparison stay inside the admissible domain. This avoids a hidden use of a Lipschitz estimate outside its domain.

## 4. Quadratic envelope and coupling magnitude

The independent zero-input result gives C_F=2H_*/rho^2, C_0=p C_F. Section5.1 correctly uses K_amp=max(1,2 C_0 Lq), r_b=K_amp b^2 and C_int=K^q K_amp+C_0 Lq. This keeps a positive radius even if the force vanishes exactly. Selecting b so C_int b^2<epsilon_bar/4 controls every intermediate stage, and C_0Lq b^2<=r_b/2 yields block invariance. The strict inherited comparison budget is the correct eta_*/(128e), not the weaker one-output eta_*/(32e).

The unprojected bound [B_T C_int+C_F+L_quant C_int]b^2 is valid: separate T_j x, G_j(0), and G_j(x)-G_j(0). Applying beta gives a uniform absolute inverse-coupling increment. No factor of b remains, but no sign appears either. The parameter order is sound: geometry and q, an outer construction, final b, then g so gT/b is sufficiently small. The force bound at the outer domain is uniform over that subsequently restricted g range.

## 5. Density sign and remaining interfaces

For exp[-gamma S+F], writing F=beta(F)S+PF forces gamma_next=gamma-beta(F). The sign in Section6 is correct. Choosing a weak sequence arbitrarily does not make it an exact physical coupling flow. Comparing two separately updated coupling sequences requires dependence estimates in g and its threshold, which the inherited-input Lipschitz theorem does not supply. An O(1) increment bound permits an O(n) accumulated change and is not an infinite weak-coupling theorem.

The finite regulator warning is also necessary. A small infinite quotient class does not automatically bound the originally chosen finite family or a finite winding remainder. Actual finite references and a normalized beta_N must be used if extraction is performed before the local limit. Canonical periodization of an independently selected infinite reference is not silently substituted. The current finite-history theorem applies only when all actual intermediate finite budgets hold. Those cautions are compatible with, rather than contradicted by, the proved infinite quotient recurrence.

No mathematical correction remains after the updated quantum-descent wording and the separately adopted 128e force budget. The optional coupling-parity refinement is not an input to this audit.

## Fragment fidelity

Read `extracted_macrostep_recurrence_fragment.tex` in full after the research pass. It faithfully preserves the exact finite reference comparison, fixed-system infinite passage, projection telescope, actual qll map and compatible representatives, Duhamel calculation, positive K_amp convention, intermediate-state induction and the 128e comparison budget. Its explicit theorem permits an infinite nonautonomous sequence of quotient classes for prescribed weak couplings; the scope correctly distinguishes that statement from a density-preserving running trajectory and from uniform actual finite-regulator histories. The unprojected amplitude and beta-increment constants match the audited derivation. The zif/qll/csgq interfaces and their theorem references have the intended meanings. No transcription or mathematical correction was found; no compilation was performed.
