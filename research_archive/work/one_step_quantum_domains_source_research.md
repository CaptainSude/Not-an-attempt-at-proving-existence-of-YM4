# Current-scale Gaussian domains: source map and next exact interface

17 October 2026. This is a source and proof-interface note, not an interacting construction. The repository remains pinned at `e392ef45013a581664bab76b90867170b30fe10e` and was not modified. The new mathematical observations below use the proved flat and classical modules already in this workspace.

## 1. Main conclusion

The all-scale roughness obstruction does not prevent a fixed-ratio fluctuation integration. Two different assertions must remain separate:

* A Gaussian potential containing every fine mode between spacing eta and a fixed macroscopic scale cannot typically lie in a fixed small physical C1-alpha ball.
* A fluctuation at the current renormalization scale has a fixed number of real coordinates per fixed current-scale cell. Uniform reduced-precision bounds give joint bad-cell estimates at that scale.

The source uses the second arrangement. At later steps its Gaussian is not simply the bare one-step Maxwell Gaussian. Its precision contains the Hessian of the previously minimized classical action. Our homogeneous flat reduced matrix already has exactly this form. The next useful theorem is a direct local-coordinate identification and perturbation bound for that matrix at small *physical stationary backgrounds*, including the nonlinear constraint and exponential gauge terms. Extending this to independent free currents and retained histories is a further interface.

## 2. Primary texts actually accessible

These links return copies of the original articles; no generated summaries are used. Page numbers below are journal pages. Formula OCR is incomplete in places, so numerical constants omitted by extraction are not reconstructed by guesswork.

### CMP109: coordinates and the Gaussian

[Bałaban, CMP109 (1987), 249–301](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf), DOI 10.1007/BF01215223. Pages 265–268, (2.3)–(2.13), choose the current-scale critical configuration, write a left relative field, straighten the averaging constraint, rescale by the coupling, and remove one pivot bond per next-level bond. The remaining variables have covariance `(C_ext^T Delta^(k) C_ext)^(-1)`. The map `C_ext` inserts the pivot variables; it is not a covariance. The exponential gauge quadratic replaces the earlier delta gauge. Haar and change-of-variable factors remain in the interaction. The fine minimizing extension is used inside the effective action; it is not a fresh Gaussian on all fine bonds. Pages 269–270, (3.1)–(3.2), distinguish physical background currents from their analytic independent-current extension. This provides the exact coordinate target, without justifying a change of cutoff coordinates.

### CMP116: conditioning, whitening and connected expansion

[Bałaban, CMP116 (1988), 1–22](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-4penm4k7hc.pdf), DOI 10.1007/BF01239022. Pages 12–13, (2.1)–(2.7), expand the interactions and cutoff defects, condition on the complement of an interior domain, whiten an exterior Gaussian by the covariance square root, and localize the resulting operators. The square root is represented by an integral of resolvents and expanded by walks. This is not an assertion of an exact finite-range covariance decomposition. Pages 15–17, (2.16)–(2.25), compare complex operators to real ones, control determinants and absorb quadratic errors; (2.24) requires a small covariance-times-error norm. Pages 18–21, (2.31), (2.38), (2.41), are the bad-bond resummation and final activity targets. The cutoff-only sector is included. Uniform Gaussian tails alone are therefore only one ingredient, not the entire localized logarithm.

### CMP119: separating good and bad regions

[Bałaban, CMP119 (1988), 243–285](https://scispace.com/pdf/convergent-renormalization-expansions-for-lattice-gauge-29jyexd38e.pdf), DOI 10.1007/BF01217741. Pages 265–267, (3.2)–(3.12), introduce exact partitions by coarse plaquette and approximate-fluctuation conditions, enlarge regions by collars, and identify the new critical background in the good region. Pages 272–273, (3.28)–(3.32), separate the Gaussian cutoff logarithm from interactions. The larger auxiliary domain in (3.43), p.276, concerns terms meeting a small-field boundary; it must not be silently substituted for every whole-lattice interior domain. The scale of the allowed physical fluctuation is small coupling times a logarithmic radius, rather than a small bound on the unscaled Gaussian coordinates.

### CMP122: normalization of large-field components

[Bałaban, CMP122-II (1989), 355–392](https://scispace.com/pdf/large-field-renormalization-ii-localization-exponentiation-h8b7ih93xo.pdf), DOI 10.1007/BF01238433, is now accessible. Theorem 1, p.355, assumes that every effective coupling stays below a sufficiently small fixed ceiling. Pages 357–359, (1.7)–(1.13), control a local quadratic form using an axial Poincare inequality and estimate the normalization denominator. The subsequent numerator estimate cancels the large Wilson contribution while retaining suppression from bad regions. Pages 384–387, (1.80)–(1.89), perform the history/combinatorial bookkeeping. Thus normalized large-field replacement requires more than a small Gaussian exceptional probability. The conditional stability theorem is not by itself a continuum reconstruction theorem.

The official link for CMP122-I, *The basic step of the R operation*, 175–202, DOI 10.1007/BF01257412, is [Project Euclid PDF](https://projecteuclid.org/download/pdf_1/euclid.cmp/1104178393). It returned a security-check page in this pass. Its formulas are not independently certified here. The deposited account cites (1.100)–(1.102) for normalized replacements, and (0.4) for integral preservation. That is a transcription-level reference pending direct inspection of Part I, not a claim that those statements are unavailable in the literature.

## 3. Exact deposited locations to use next

All line numbers refer to the pinned files. They are locating references, not substitutes for a mathematical audit.

| Location | Content relevant to the next proof |
|---|---|
| Raw I:880–935 | Exact pushforward, partitions, and the normalized large-field R operation |
| Raw I:4334–4342 | Current unit lattice, next spacing L, and independent bonds with the pivot bonds deleted |
| Raw I:4808–4848 | Reduced precision, its compression to a region, covariance and resolvent square root |
| Raw II:73865–73950, `8.2:eq-small-field-step-2` through `-4` | The actual relative-field change, constraint straightening, coupling scaling, pivot removal and full fluctuation exponent |
| Raw I:46960–47000 | Kernel-to-matrix normalization for the actual pivot insertion |
| Raw I:5500–5517; 5910–6077 | Independent-current hypotheses and conditional complex coercivity construction |
| Raw II:11178–11195 | Larger-cutoff estimates distinguish cubic action terms from merely vanishing terms |

In particular, `C^(k)(Y')=(chi_Y' A chi_Y')^(-1)` is the inverse of a precision compression, not the principal block of the full covariance. Those are different matrices. The distinction matters when reading the conditioning calculation.

The deposited scalar radius conventions also require care: Raw I:4171–4174 writes `(A1/A0) p0(g)`, while Raw II:2249–2255 packages the numerical threshold as `A1 (log g^-2)^p0` using its degree-function convention. The safe invariant notation until that convention is unpacked is `R_k=delta_k/g_k`; the needed asymptotic fact is `R_k=c (log g_k^-2)^p0` with fixed c>0.

## 4. Independently derived scaling and joint tails

Let a bare homogeneous step have fine spacing eta, coarse spacing h=L eta, and fixed odd L. Work in four dimensions with the physical pairing `eta^4 sum`. If `Z_phys` is the selected constrained Maxwell Gaussian and `x=h y`, set `Z_s(y)=h Z_phys(x)`. Then

    eta^4 sum |d_eta Z_phys|^2 = L^-4 sum |d_(1/L) Z_s|^2.

The appropriately rescaled constraints are the same fixed-L constraints, so `Z_s` has the unit-coarse-scale physical covariance operator C_L. Its counting-coordinate covariance is `L^4 C_L`. Consequently

    Y_step=(eta Z_phys, eta^2 nabla_eta Z_phys),
    Cov_count(Y_step)=S_L C_L S_L^T,
    S_L=(L I, nabla_(1/L))^T.

Equivalently, the coordinate matrix of the physical covariance operator at scale h is `h^2 C_L`; value-coordinate covariance is `eta^-4 h^2 C_L`. The factors agree. From positivity,

    ||Cov_count(Y_step)|| <= L^2 ||C_L||
                              + ||nabla C_L nabla^T||.

This is volume independent at fixed L by the established flat bounds. It must not be used with L replaced by the total refinement while claiming the same constant.

For later RG stages use the exact current-coordinate flat precision already identified in Notebook07:

    A_(M,0)=K_L^T [q_M+T_L^TT_L] K_L,
    C_ret,M=A_(M,0)^(-1),                 M=L^k.

Here q_M is the classical Maxwell effective precision after minimizing the original fine field, T_L is the next-step exponential gauge map, and K_L is the next-step pivot insertion. These last two maps have fixed local geometry. The uniform gap, upper bound and exponential covariance decay already proved for A_(M,0) imply a counting covariance bound for its current-unit retained variables, uniformly in k and volume. Applying the fixed-range K_L, or a unit-lattice first difference after K_L, preserves a uniform counting bound. This is a second useful Gaussian law, distinct from the gauge-selected bare C_L above.

For completeness, suppose a real centered tested field Y has `Cov(Y)<=K I`, each marked cell tests at most m scalar coordinates, and each coordinate occurs in at most nu tested cells. A marked set S of k cells then satisfies

    P(every b in S has max_(i in I_b)|Y_i|>R)
       <= [m sqrt(2) exp(-R^2/(4 nu K))]^k.

Indeed select one offending coordinate per cell. The selected vector, including repetitions, has covariance at most nu K. At parameter `(4 nu K)^(-1)` its exponential square moment is at most `2^(k/2)`; Markov's inequality and at most m^k choices prove the bound. The alternative prefactor `2^(m/2)` follows by collecting all tested coordinates. No independence is assumed.

For `R(g)=c(log g^-2)^p`, p>1/2, the bracket is at most `C g(log g^-2)^q` below a fixed coupling ceiling for any fixed q: writing t=log g^-2, the negative `-c' t^(2p)` dominates `-t/2+q log t`. Constants are independent of volume and level when the covariance and cell bounds are. Global absence of bad cells still incurs a volume factor; this is a joint marked-set statement.

The independently audited `gaussian_joint_block_tail_research.md` additionally proves a normalized complex version under a relative precision perturbation of norm at most 1/4. Marginalizing all untested directions first removes any ambient-dimensional determinant cost. This is well suited to a direct physical-background perturbation theorem, once its hypotheses are verified.

## 5. Exact Gaussian conditioning: what needs localization

Let a real positive reduced precision A act on coordinates I and E, with blocks A_II,A_IE,A_EI,A_EE. Completing the square gives the conditional law

    B_I | B_E=y  ~  N(-A_II^-1 A_IE y, A_II^-1),

and exterior marginal precision

    S_E=A_EE-A_EI A_II^-1 A_IE.

Thus the determinant identity is `det A=det A_II det S_E`. These are exact finite-dimensional statements. If `a I<=A<=B I`, then `a I<=A_II<=B I`; the conditional covariance is uniformly controlled. A conditional mean is not small merely because the conditional covariance is bounded. Either the exterior field is controlled or the mean must be retained and absorbed in the coupled Gaussian calculation.

For a uniformly accretive complex A the same block algebra is valid, with the determinant branch connected to the positive real reference. Bounding the modulus before marginalization can create a spurious full-volume factor. This explains why an exterior-whitening calculation or a tested-marginal proof is useful. Localization of A^-1/2 and of the conditional mean is still an operator task. A decay estimate is not the same as an exact finite-range decomposition.

## 6. Concrete next proof: physical-background reduced precision

The following is a sufficient *local-coordinate lemma*, not yet the full source theorem. It is compatible with the classical results already proved and gives a sharply delimited target.

Let S_M(a) be the classical coarse action in ordinary current-lattice exponential coordinates. Assume its gradient m_M(a) is O(b) and its Hessian is `q_M+O(b)` in the admissible weighted operator norms when `||a||<=b`. Let the actual next-step constrained relative-field chart be `a=Phi_U(z)`, with z the retained independent coordinates, `Phi_U(0)=a_*`, and

    D Phi_U(0)=K_U,        ||K_U-K_L||_weighted <= C_L b.

Require fixed-range, bounded-coefficient first and second chart derivatives; in particular the contraction of `D^2 Phi_U(0)` with any bounded current m must have weighted matrix norm at most `C_L ||m||_infinity`. Let G_U be the actual exponential gauge function and assume its pulled-back Hessian is `K_L^TT_L^TT_LK_L+O(b)` in the same norm. All constants must be uniform in M and volume.

Then the exact pulled-back physical stationary precision is

    A_M(U)=K_U^T D^2S_M(a_*) K_U
          + <m_M(a_*),D^2 Phi_U(0)>
          + D^2(G_U o Phi_U)(0).

The chain rule gives `||A_M(U)-A_(M,0)||_weighted <= C_L b`. The second term is essential: stationarity is constrained, so the unrestricted current need not vanish. A left-relative chart and ordinary-coordinate Hessian therefore cannot be identified without this correction. The nonlinear constraint contributes through the same term. Holomorphy follows if these charts and action derivatives are holomorphic on a common smaller domain.

If the flat gap is gamma_L and `C_L b<=gamma_L/4`, the real precision is positive and the complex relative perturbation satisfies

    ||A_(M,0)^(-1/2)[A_M(U)-A_(M,0)]A_(M,0)^(-1/2)|| <= 1/4.

Consequently the joint-tail theorem applies on the retained coordinates. Weighted inverse bounds follow by a Neumann expansion after reducing the weighted radius if necessary. The classical coarse Hessian and multiplier estimates are already available from Notebook16. The remaining concrete work is to construct and verify the *actual source* chart Phi_U, G_U and stationary background at the current step with the exact left-relative and pivot conventions. A general abstract change of gauge does not prove this identification or preserve a sharp cutoff automatically.

## 7. Interaction and large-field interfaces that remain separate

Once the physical source Gaussian has been matched, the finite-dimensional Haar logarithm is analytic near the identity, with zero constant and linear terms. On a physical cutoff `|gB|<=gR`, it has size O(g^2 R^2) per bond. The constraint Jacobian can begin linearly, hence O(gR), while a cubic action remainder with prefactor g^-2 has size O(gR^3). The fixed-cell version of the combined Gaussian-plus-interaction estimate is already proved in `interaction_cutoff_research.md`.

For the source, however, a minimizing extension can make interaction labels meet several overlapping cells. Its coefficient norms must be localized and summable before these estimates can be clustered. A fixed-cell theorem cannot be promoted by merely grouping arbitrary overlapping labels into larger cells: degree and support-size costs must be controlled. The sharp cutoff must also be expressed exactly on the coordinates being integrated. The fact that the pivot correction has only pivot rows is helpful, but the precise source cutoff index set and any pivot conditions still need to be recorded at the matching step.

A viable sequence is therefore: (i) prove the homogeneous physical-background reduced-precision lemma in the actual pivot chart; (ii) identify the local Jacobian/Haar factors and interaction coefficients on the logarithmic cutoff; (iii) establish the overlap-compatible cluster bound and its source dependence; (iv) extend the exact identity and estimates to collared retained-history regions and normalized bad components. A convergent coupling trajectory, observable estimates and continuum axioms remain beyond those steps. None follows from the Gaussian tail alone.
