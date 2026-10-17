# Homogeneous flat matching to the source weak norms

16 October 2026. This note reads the deposited Raw I source requirements and separates them from the pointwise and physical-cell theorems already obtained. It is a homogeneous final-scale-one comparison only. It does not claim matching to mixed retained scales or nonflat backgrounds.

## 1. Source definitions and simplification at scale one

Raw I:12740–12752 defines

    N(A)=max{|A|_(-1), |nabla_U A|_(-2)},
    N_beta(A)=max{|A|_(-1), |nabla_U A|_(-2),
                         [nabla_U A]_(-2-beta)}.

The bracket is the local Hölder seminorm specified through CMP99b (3.40), with the scale factor ell_j^(2+beta). The source fixes beta<=beta_0<1. At the homogeneous identity background and retained physical scale ell=1 these reduce to the fine pointwise sup norm, sup norm of all first differences, and the local beta-Hölder seminorm of the first differences. Forward/backward conventions and fixed component/orientation multiplicities change only constants.

The definition of ell is at I:12664–12669: ell_j=L^j eta, acting on the retained layer and corresponding fine region. It is not the fine lattice spacing. Thus a fine pointwise estimate in physical derivatives, not unscaled bond differences, is required.

The weighted version at I:12762–12770 uses a coarse-geometry exponential rho(y)=exp(kappa d(y,S)) multiplying the local sup and derivative norms. In the homogeneous setting an exponential block bound with a spare decay exponent supplies these weights after summation. Fixed output collars provide comparisons across adjacent cells. Local Hölder bounds on those collars and a gradient sup bound imply the global fine-grid Hölder bound: near pairs share a bounded collar, and far pairs use the sup estimate.

The admissible current condition is only

    |J|_(-3)<a_gamma,

at I:12951–12966. At ell=1 this is a sup bound. There is no current derivative or current Hölder condition. The weak complex background perturbation, by contrast, satisfies an N bound, but that background remains zero in the present results.

## 2. Exactly which propagator norms are called for

The relevant source locations are I:13569–13615 and the current assertions J1–J8 at I:13749–13804.

| Source member | Homogeneous requirement | Relation to the new flat results |
|---|---|---|
| Sup forcing for G0, I:13593–13601 | G0 maps bounded fine forcing to bounded field and first differences; local first-difference C^beta for beta<=beta_0<1 | The pointwise inverse theorem proves this with exponential block locality |
| Baseline Laplacian member | Componentwise scalar fine Laplacian of G0 on bounded forcing; corresponding baseline extension estimate | The new pointwise inverse theorem proves the componentwise Laplacian; it does not imply bounds for each individual second difference |
| Right-divergence input, I:13601–13615 | G0 nabla* lambda and nabla G0 nabla* lambda; the latter needs positive Hölder regularity of lambda | Additional singular-integral/cancellation estimate; not a consequence of the bounded-forcing C^(1,beta) theorem alone |
| Localized double-gradient Hölder member, I:13601–13612 | phi nabla G0 nabla* psi in C^beta from localized psi in C^(beta+epsilon), with cutoff factors and exponential block separation | Needs the corresponding Hölder-input bound and controlled localization; the source prints the scalar G' version and states the analogous G0 version |
| Scalar G', P=I-R and scalar-gauge operators, I:13569–13580,13629–13636 | Separate scalar/projection kernel and weak norms, including Lambda:sup->sup and D Lambda:N->sup | Z's cell-L2 bounds alone do not prove these pointwise norms; the new scalar pointwise route must provide them or bypass unneeded ones explicitly |
| Baseline minimizing extension and constrained covariance, I:13638–13676 | N_beta(H0 B)<=C||B||_infinity and N_beta(tilde G0 f)<=C||f||_infinity, with identities | Follow from pointwise G0, bounded local Q*, bounded coarse q0, and the local source extension; see below |
| Current J1 | G0 Theta'_J:N->N_beta with O(||J||_infinity), including weights | The factorizations in Section 3 below give a sufficient route without differentiating J |
| Current J2 and J7 | Sup-forcing and right-divergence members for G_pi^J and G1^J; the source explicitly excludes the Laplacian member | Pointwise weak contraction plus appropriate baseline data bounds is sufficient; do not transfer a Laplacian assertion into the current family |
| Current J3–J6 | Coarse q_J locality, extension N_beta bound, bounded finite-range Theta_J, and N_beta(tilde G^J f) | Cell algebra plus stronger sup-row Theta bound and pointwise smoothing address these at flatness; every identification must retain its source normalization |
| Current J8 | Analyticity in background and current and genuinely localized generalized-walk expansions | Homogeneous analytic dependence on current does not establish background dependence or strict support of the original walk coefficients |

The source fixes epsilon=(1-beta_0)/2 at I:13741–13743. Thus beta+epsilon remains strictly below one for all beta<=beta_0, which is compatible with a non-endpoint Hölder analysis. The source's J2 text at I:13759–13765 expressly excludes the Laplacian member for G_pi^J; J7 imports those same members for G1^J. It is therefore incorrect to infer that bounded J must permit a componentwise-Laplacian current bound just because the baseline does.

The pointwise inverse proof's explicit counterexample also shows that a uniform C^(1,1) or individual-second-difference estimate for arbitrary bounded forcing is false. This endpoint is neither required nor supplied here.

## 3. A sufficient weak contraction with no derivative of J

Keep the exact flat identities

    G0 Lambda*=DZ,
    G0 Pi*=G0-DZD*,  Pi=I-DLambda.

Write the current coefficient factorization from the audited Notebook09 as

    Theta'_J=j_J* Lambda+Lambda* j_J
             +Lambda* V_J D Lambda+(D Lambda)* V_J* Lambda.

Then, with all products in their displayed order,

    G0 Theta'_J
      =G0 j_J* Lambda+DZ j_J
         +DZ V_J D Lambda+DZD* V_J* Lambda.       (3.1)

The local finite-incidence maps j_J,V_J are bounded on fine sup spaces by C||J||_infinity. Hence a sufficient pointwise input set is

    Lambda:N->sup,  D Lambda:N->sup,
    G0,DZ,DZD*:sup->N_beta,

with exponential localized/weighted versions and constants uniform in refinement. These estimates yield the source J1 contraction, with a possibly smaller uniform current radius than the earlier Hilbert-algebra radius. The weaker Lambda:sup->sup bound, if available, is sufficient for its occurrence in (3.1).

For the full term,

    G0 Pi* Theta_J Pi
      =(G0-DZD*) Theta_J (I-DLambda).             (3.2)

The separately audited fixed-step composition proof gives `Theta_J:sup->sup` with norm O(||J||_infinity). Thus (3.2) maps N to N_beta once the same outer smoothing and D Lambda:N->sup bounds hold. There is no need to assert Pi:sup->sup. Indeed Pi has an order-zero singular-integral part, so such an assertion would require a separate argument and is not justified by cell-L2 boundedness.

These identities keep every derivative on a fixed propagator or on the input potential. In particular one must not expand `D* V_J*` by a product rule and estimate a derivative of J; that derivative is not part of the source's assumptions. Equation (3.1) already has the exact integration-by-parts placement needed to avoid it.

If `G0 Psi_J` is small as an N->N operator, its Neumann inverse on N gives both current families on bounded forcing. Their N_beta improvement follows by writing the first term as G0 f and the remainder as `G0 Psi_J A`, which uses the smoothing side of (3.1) or (3.2). This is a weak-space proof, not an inference from a growing-dimensional Hilbert estimate.

## 4. Right-divergence data are a distinct baseline obligation

The source additionally admits forcing `nabla* lambda`. Such forcing has sup norm of order eta^-1 for a generic bounded lambda. Feeding that bound into `G0:sup->C^(1,beta)` loses uniformity. The correct target is instead a direct estimate for

    G0 nabla*:C^epsilon->N,

and the localized version of `nabla G0 nabla*` with the desired output Hölder regularity and an input exponent beta+epsilon. The order-zero principal part of the latter needs cancellation. A bound on the componentwise Laplacian G0 does not establish bounds on every mixed derivative or derivative orientation separately.

A useful direct route is the scalar heat-kernel cancellation in the full-rank piece, with the finite-rank alias corrections treated separately. Hölder increments replace the constant input in a mean-zero derivative kernel and supply a positive power of the heat scale. This is an additional proof to carry out or import explicitly; this note does not mark it as already obtained merely because the bounded-forcing theorem is available.

Localization requires care. Sharp restriction of a Hölder datum to a cell creates jumps of size O(1) across distance eta and hence an artificial eta^-epsilon seminorm. A valid local proof uses uniformly smooth physical cutoffs and fixed collars with bounded overlap, or works directly in a weighted global Hölder space. This is consistent with the explicit source cutoff factor at I:13601–13612. A naive cellwise decomposition that was valid for bounded forcing is not valid for these Hölder data.

Once the baseline right-divergence input reaches N uniformly, the same weak current contraction applies; no derivative of J is needed in the subsequent perturbation series. The current family need not retain the baseline Laplacian estimate, and the source does not require it.

## 5. Extensions, constrained inverses, and what is still separate

At ell=1, H0=E0=G0 Q* q0. The physical Q* has fine sup row sum one, and q0 acts on fixed-dimensional coarse fibers with exponential kernel decay. Thus bounded coarse input produces bounded fine forcing for G0, yielding its N_beta extension estimate. Applying the baseline componentwise Laplacian to this formula gives the corresponding H0 baseline member. The auxiliary/current extension similarly uses the pointwise current inverse once that has been proved.

The constrained baseline covariance is `tilde G0=G0-E0 q0^-1 E0*`. For bounded fine forcing the second term is controlled by the rectangular transpose cell-Schur bound and the pointwise extension: each physical unit cell of forcing has bounded L2 norm, so no global L2 assumption is needed. The same observation controls the current weight E_J^T J. This does not prove a full pointwise transpose-kernel theorem for every source operator, but it is sufficient for these displayed composites.

Generalized random-walk terms whose coefficients read only prescribed domains, nonlinear background responses, source Ward identities at nonflat backgrounds, mixed-scale weights, and retained-boundary comparisons remain separate obligations. Exponential locality of a homogeneous Fourier kernel, or holomorphy in a bounded current, is not by itself the source's strict support-dependent walk statement.

## 6. Present checkpoint

The newly audited pointwise G0 theorem supplies the bounded-forcing N_beta members and baseline componentwise Laplacian. The scalar factorizations identify exactly how to perturb these norms without adding regularity of J. The stronger fixed-step Theta_J sup-row theorem supplies the full constraint insertion needed for (3.2). The remaining homogeneous norm checks to record explicitly are the pointwise scalar legs Lambda,D Lambda,DZ,DZD*, the direct Hölder right-divergence input estimates with proper cutoffs, and their weighted versions. No endpoint beta=1, current Laplacian, or derivative of J should be silently added.
