# Independent audit: stationary support, activity transport, and local symmetry

17 October 2026. Independently audited the authoritative Notebook21 inputs and the following research candidates:

* coarse_stationary_support_research.md;
* quantum_activity_transport_research.md;
* connected_carrier_coarsening_research.md;
* small_field_gauge_covariance_research.md.

Also checked classical_support_localization_fragment.tex for fidelity with its already audited research proof. No output file was edited. This is an internal mathematical audit, not external certification or a quantum RG induction theorem.

## Result and corrections adopted

Pass after the corrections described below. The current stationary map has an actual convergent strict-support expansion, and the activity substitution is a bounded finite-step map with an explicit support and analytic-domain budget. The geometric projection lemma and the local gauge-covariance/Ward argument also pass within their stated scopes.

The substantive correction was a supremum/order-sum issue in the first stationary-gradient majorant. The original all-order estimate bounded the supremum over output roots of a positive series, whereas the cited support theorem used the sum over orders of the supremum of each coefficient norm. These cannot be interchanged. The author adopted the safe coefficientwise repair:

\[
 v_n\le M_g t_0^{-n},\qquad
 \Phi(t)\le M_g\frac{(t/t_0)^2}{1-t/t_0},\qquad
 \Phi'(t)\le 8M_g t/t_0^2\quad(t\le t_0/2).
\]

The contraction radius was correspondingly reduced to t_0^2/(16 c_0 M_g). The saved proof explicitly records the noninterchange of supremum and summation. I checked this revised argument.

A second convention was clarified: the maximum of the separate w- and z-family norms is used through scalar-coordinate/type-colored slots, whose sums are already included in the positive Cauchy majorant. It is not identified with the generally larger sum over supports of the norm of the joint vector family. This removes a possible hidden factor in the radius calculation. The earlier Notebook21 support fixed point uses a different, consistent convention: its joint maximum over field types is inside each coefficient norm, before the support sum, and its multilinear vertex operators act on that same joint cell space. The linear source norm may be bounded by the sum of the component source-block norms. These two conventions should not be conflated.

The transport note also now makes the actual carrier staging explicit: present Notebook21 Gaussian output carriers are already L-block cells, the graph of next-coarse w. Their present substitution uses pi=identity, F=1 and the full current-background dimension D_bg=d L^d dim(g), not the retained Gaussian dimension. A later L-block projection of the transported next-current activities is a distinct operation for the following integration. No coarsening gain is counted twice.

## 1. Affine pivot chart and exact quadratic stationarity

At the identity current background, the ordinary logarithmic constraint has F_1(a)=A_1 a+C_1(a), with A_1=LQ_L^flat. Its pivot coefficient is L^(1-d)I. Therefore h_1=L^(d-1)I on the corresponding pivot is exactly the required right inverse, while K_L retains nonpivots and lies in ker A_1.

The equation

\[
 a=K_Lz+h_1w-h_1C_1(a)
\]

has the exact source incidence: each nonlinear equation reads its own pivot and no other pivot. Its local implicit solution consequently stays finite range and satisfies F_1(a)=w and a_nonpivot=z. It is the identity-background ambient straightening of K_Lz+h_1w. There is no propagation of dependency through other pivot unknowns.

The variables w are next-coarse group angles, W=exp(iw), not the physical potential w/L. All factors of L in the right inverse and affine constraint are consistent with that convention. Pairings in this finite coordinate stationarity calculation are counting pairings; no physical L^4 adjoint factor should be inserted.

The action plus actual absolute gauge function has quadratic form

\[
 \tfrac12\langle K_Lz+h_1w,(q_M+T_L^TT_L)(K_Lz+h_1w)\rangle.
\]

Since the scalar is stationary at zero, chart curvature does not contribute to this quadratic term. The retained block is the previously bounded A_M,0, and the cross block is K_L^Tq_Mh_1 because T_Lh_1=0. Its exponential block bound follows from finite range of K_L,h_1 and the known q_M decay. The construction therefore uses an already established mass gap and inverse, rather than assuming a new one.

## 2. Unbounded scalar supports and the correct gradient majorant

The earlier finite-range vertex lemma cannot be applied directly to unbounded scalar supports X. In particular, a polarization bound followed by |X|^n cell-slot counting would generally leave a factorial after spending a fixed cardinality reserve. The new note avoids that failure using coordinatewise Cauchy in the actual fixed-dimensional current cells.

For an activity bounded by M_X on a polydisc with D|X| scalar coordinates, differentiation in one retained coordinate gives the exact absolute coefficient majorant

\[
 \frac{M_X}{\rho}(1-t/\rho)^{-D|X|-1}.
\]

The extra power corresponds to the differentiated coordinate. Summing output components costs at most D_z. Scalar monomial coefficients distribute over ordered symmetric multilinear slots with multinomial weights summing to one, so their absolute coefficient sum bounds the ordered cell-slot sum. The scalar/type convention described above makes this valid for the maximum of the separate field-family norms.

All slot roots and the gradient output lie in X; their rooted Steiner length is at most tau(X). A fixed cardinal reserve A absorbs the factor (1-t_0/rho)^(-D|X|), at a sufficiently small t_0. This yields a uniform all-order row bound at t_0. The corrected coefficientwise step then supplies an analytic quadratic mixed majorant, with the geometric denominator recorded at the start of this audit.

The support contraction now uses only legitimate ingredients: the corrected majorant, the established weighted inverse A_M,0^-1, singleton w sources and rooted Steiner gluing. Arbitrary fixed output cardinal reserve is paid by the source radius. Evaluation stays inside the prior uniqueness ball by an explicit additional shrink. Applying the genuinely finite-range affine chart to the supported solution gives a_*(w)=H_cur,M w+O(r^2), with the stated strict-support norm and H_cur,M=h_1-K_L C_M,0 B_M. This is distinct from the earlier original-fine extension H.

## 3. Identification with the physical branch

The argument correctly identifies the new solution with a pre-existing physical branch; it does not infer contour gauge zero from the gradient equation alone.

Notebook19's branch is a constrained local classical minimum, is small, and has P_V=1. The actual real exponential gauge penalty is nonnegative and vanishes there. Hence that branch is also stationary for the action-plus-gauge functional in the affine retained chart. The local scalar support expansion, differentiated with fixed margins and a cardinal reserve for the column count, gives a uniform O(||w||+||z||) perturbation of A_M,0 in absolute row and column norms. On a fixed convex retained ball, the real Hessian is therefore positive with a common lower bound.

Both the newly constructed stationary solution and the old physical branch lie in that ball on a sufficiently small common data domain. Uniqueness identifies them. Holomorphic uniqueness extends the resulting constraint and gauge identities to the common complex domain, but does not extend minimum inequalities to complex fields. This supplies the actual stationary background required for transport.

## 4. Activity substitution from a single finite cardinal reserve

The transport theorem's assumptions are exactly strong enough: connected input carriers H, a scalar polydisc of radius b in D|H| actual background coordinates, an anchored exp(a0|H|) activity norm, and a genuine rooted support family for the actual background. One-weight response bounds alone would not supply the last hypothesis; the stationary theorem above does.

Coordinatewise Taylor expansion produces the exact factor

\[
 \sum_\nu(s/b)^{|\nu|}=(1-s/b)^{-D|H|}.
\]

No dimension-free estimate or missing factorial is used. The cost alpha(t)=D log(1/(1-t)), t=s/b, is explicitly paid out of the one fixed input reserve. The scalar coordinate count is the number of background coordinates, including pivots, rather than the number of retained Gaussian coordinates.

Every decorated monomial keeps the projected carrier pi(H) and adds a chosen rooted Steiner tree for each occurrence of a background support. The resulting carrier K is connected and contains all variables on which the term depends. Repetitions, overlapping trees and periodic identifications only reduce the size estimate

\[
 |K|\le|\pi(H)|+T_{\rm tot}.
\]

For z in K, the attachment length is at least d'(z,pi(H)). Moreover, since K itself includes the connecting vertices, its metric MST length is exactly |K|-1. Thus there is no hidden factor-two Steiner/MST loss at this final connected-carrier step.

With beta=a_out+mu, the conditions beta+delta<=kappa and beta+alpha(t)<=a0 give the displayed anchored bound

\[
 \|E'\|_{a_{\rm out},\mu;r}\le F S_\delta\,\epsilon.
\]

The re-rooting proof is valid: exp(-delta d'(z,pi(H))) is at most the sum over i in H of exp(-delta d'(z,pi(i))), and each coarse fiber contains at most F old cells. This handles arbitrary support size without an extra volume factor. The same positive majorant justifies all substitutions, regrouping by connected carriers and holomorphy.

The vacuum is correctly separated as sum_H E_H(0). Since each substituted support summand vanishes at w=0, every nonconstant output coefficient does too. If only the summed background vanished at zero, subtracting the constants in each support slot preserves the background by absolute convergence and costs at most two in the rooted norm, as stated.

The sharper nonconstant bound also checks. Under rho=a0-beta-alpha(t)>0, use exp(alpha k)-1<=alpha k exp(alpha k) and sup_k k exp(-rho k)<=1/(e rho). It gives F S_delta epsilon alpha(t)C_rho. This small factor comes from a smaller analytic domain; it is not a same-radius scale contraction.

Connectedness is essential when the input has only cardinality decay. Two arbitrarily separated terminals with fixed carrier size and fixed coefficient would otherwise require an arbitrarily long connected output hull with no input penalty to pay for it. The note explicitly excludes that counterexample by its hypothesis.

## 5. Coarsening geometry and actual scale bookkeeping

The connected-carrier packing lemma passes. A maximal r-separated set in connected H covers H by sup-metric boxes of side less than L, each meeting at most 2^d L-blocks. If there is more than one center, the disjoint graph balls of radius s around them each contain at least s+1 vertices of H, by following a simple path in H toward another center. Thus J(s+1)<=|H|. The one-center case is separately bounded. The proof remains valid with periodic distances; identifications do not increase its counts.

The resulting |pi(H)|<=c0+c1|H| bound changes the transport budget to c1 beta+alpha(t)<=a0 and multiplies its norm constant by exp(beta c0). The attachment-tree budget beta+delta<=kappa remains necessary; improving carrier compression alone does not supply a missing stationary-background exponent.

The auxiliary spatial projection estimate also checks: along a terminal metric spanning tree, each projected edge has length at most its fine length/J+d. Using ell<=2 tau gives tau_block(pi_JY)<=2 tau_unit(Y)/J+d(|Y|-1). The cardinal reserve required to pay the last term is explicit. This is available for the classical families with arbitrary reserve, but not automatically for a quantum family with only small fixed reserve.

For the actual Notebook21 output, the Gaussian cells already are L-blocks of the current lattice and are exactly the graph of the next-coarse w labels. Present substitution therefore uses pi=identity and F=1. After that substitution the same carriers are unit cells of the next current lattice; projecting them into the following integration's L-block cells is a separate future step. The note now states this correctly. Any later use must also pay the following pivot/chart support enlargement and analytic-domain requirements. There is no second coarsening gain inside the present substitution.

## 6. Bounded versus contractive, and the domain obstruction

The proved general operator bound is F S_delta, or exp(beta c0)F S_delta with the optional geometric improvement. These constants need not be less than one. A singleton vacuum coefficient c at each old unit cell becomes F c in a full new block. Even after vacuum subtraction, an identity background map and linear singleton activity show that generic substitution has no strict contraction at a common radius. Gauge-invariant marginal sectors require their own analysis; a Ward identity is not an estimate of their RG eigenvalues.

The explicit sufficient radius is

\[
 r\le\frac{b}{C_a}\min\{1/2,a_0/(8D)\},
\]

in addition to the stationary-map radius. The output support exponent also spends part of a0. These are real losses in the proved finite-step estimate. For example, if a0<=1/2 and C_a>=1, this sufficient choice has r/b<=1/(16D). This is a conservative sufficient bound, not a proof that the true analytic continuation stops there. It nevertheless cannot be iterated while simply assuming the original common domain remains available.

There is an exact warning against replacing C_a by an assumed L^-1 factor. For a small coarse pure gauge W(y,y')=g_y g_y'^{-1}, choose the current site gauge to be g_y throughout each L-block. The current links are identity internally and equal W across block boundaries. The field has ordinary average W, internal contour mean one and zero classical action, so uniqueness identifies it with the physical branch. Its boundary angles have the same order as w, not w/L. The distinction between angle w and physical next-coarse potential w/L does not imply a contracting angle supremum domain.

Consequently finite-step bounded transport is established. A stable sequence of analytic/orbit domains, extracted relevant and marginal sectors, coupling-flow estimates, and control of inherited interactions under the following integration are still needed for quantum induction.

## 7. Audit of exact local gauge covariance and the Ward consequence

The block-lift gauge proof passes on its common small domains. An internal contour stays in one block, so its group mean transforms by conjugation and P=1 is preserved. The ordinary coarse average has the correct endpoint gauge covariance. Local gauge invariance of the classical action is applicable with the previously constructed smooth original-fine extension; the current unit-scale jump has no M-dependent derivative. More precisely, the earlier two-direction ordinary-minimum comparison applies to arbitrary small current-site gauge values, using the smooth point-value extension to the original fine lattice. It controls both the transformed original-fine minimizer and the inversely transformed minimizer at the new current datum inside the same uniform comparison ball. The discontinuous blockwise function itself need not be extended as a discontinuous original-fine gauge. Thus this application uses the established homogeneous S_M branch, not an unproved global extension of S_M or an assumed invariance of a fixed-slice representative. The transformed physical branch is a critical point in the same common chart, and the established local uniqueness identifies it with the branch at transformed coarse data.

For relative fluctuations, the exact nonlinear constraint transforms by conjugation at the initial coarse endpoint. Since the chart retains its nonpivot variables exactly, uniqueness of the local pivot solution gives Phi_{V'}(D_u z)=R_u Phi_V(z). This is a full nonlinear identity. For real compact gauges the retained adjoint matrices are orthogonal and have determinant one, so the specified retained bond-color balls are preserved exactly.

Every normalization factor transforms correctly. Haar exponential-coordinate density is Ad-invariant. Each pivot derivative is multiplied on its two sides by adjoint matrices of determinant one, so both the pivot delta determinant and normalized straightening ratio are unchanged. The Hessian transforms by orthogonal congruence, preserving its determinant and carrying the normalized Gaussian to the transformed one. Action constants, linear Taylor terms and quadratic terms transform separately under the fixed linear retained map, so the centered remainder also transforms. This remains true away from physical stationary backgrounds: use the full absolute contour gauge function, its actual Hessian, and subtract its actual constant, linear and quadratic Taylor terms. In particular, a nonzero off-stationary linear coefficient is transformed and subtracted covariantly, not set to zero. The centered extension equals the physical saddle-point integral only on the separately identified physical branch; symmetry of the extension does not claim otherwise. No complex change of a sharp indicator is needed: the integral identity is first real, and then extended holomorphically in the common domains.

The baseline matrix A_M,0 need not itself be invariant under a local gauge for its scalar determinant to be a valid fixed denominator. The stated total correction, including the separate delta and Gaussian determinant terms, is therefore gauge invariant after composition with the physical stationary branch. Arbitrary individual support coefficients need not be invariant.

There is an additional branch qualification for the inherited-interaction extension. Multiplying by exp(E) preserves equality of the integrals if E is gauge invariant on the common current-field domain and its composition and integration exist there; holomorphic extension of that equality requires the resulting integral to be holomorphic, as follows from locally uniform integration on the finite retained domain or the established convergent cluster estimates. Equality of logarithms additionally requires that integral to be nonzero and the logarithms to be compatible on the common connected holomorphic domain. A convergent cluster logarithm supplies both requirements; alternatively one may normalize a holomorphic branch and continue along the same small real gauge paths. Convergence or gauge invariance of exp(E) alone does not rule out cancellation zeros for a complex inherited correction. The uninherited integral already has the required nonvanishing and compatible branch from the proved cluster construction and its positive real normalization. This refinement changes no integral identity or Ward calculation once the logarithmic functional is defined.

For a compact connected semisimple group, global constant gauge invariance forces each linear color covector at zero to vanish. Differentiating the local gauge identity once in the gauge parameter and once in a field direction then gives the quadratic Ward identity; the term from differentiating the nonlinear gauge generator vanishes because the first derivative is zero. This holds on each admissible finite periodic regulator.

The zero-momentum conclusion is correctly conditional. If a translation-invariant kernel limit exists with uniform exponential summability, its continuous Fourier multiplier satisfies K(p)d(p)=0. Evaluating along p=t e_mu and taking t to zero proves K(0)e_mu=0 for each direction/color. Finite discrete momenta alone would not imply this conclusion, and the candidate explicitly does not use that shortcut. The result excludes a momentum-independent quadratic mass term in that stated limit, but neither identifies the marginal coefficient nor computes its flow.

## 8. Fragment fidelity and promotion status

The complete saved coarse_stationary_support_fragment.tex and quantum_activity_transport_fragment.tex were checked against their corrected research proofs. The stationary fragment retains the repaired coefficientwise majorant, geometric denominator, factor-eight derivative bound, smaller contraction radius, colored-slot convention, physical-branch identification and pure-gauge counterexample. The transport fragment retains the actual pi=identity staging, full background coordinate count, support-hull and re-rooting proof, fixed-cardinality budget, separate vacuum, optional future projection and explicit domain losses. No additional transcription correction was found. The current classical_support_localization_fragment.tex norm convention also agrees with the clarification at the start of this audit.

These two fragments are ready for internal promotion within their stated finite-step scope. The local gauge candidate is likewise ready after making the inherited-integral logarithm qualification explicit. This audit did not edit any output notebook.

## Final scope

The audited work supplies an actual stationary-background support family, a quantitative bounded transport of connected holomorphic activities with only one fixed positive cardinal reserve, valid coarsening geometry, and exact local symmetry constraints on the total correction. The adopted repairs and scale distinctions remove the identified gaps. No remaining mathematical correction was found within those statements. Their finite-step domain and norm bounds do not yet constitute a uniform quantum RG induction.
