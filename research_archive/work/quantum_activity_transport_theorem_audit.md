# Independent audit of strict activity transport

17 October 2026. Read `quantum_activity_transport_research.md` in full against the actual stationary-background norm in `coarse_stationary_support_research.md`. Internal mathematical review, not external certification. No output files were changed.

**Verdict:** the bounded one-step transport proof passes. It does not prove an invariant quantum domain or an RG contraction, and its stated limits correctly retain those obligations.

1. **Coordinate count.** The activity is expanded in its actual D|H| scalar background coordinates. Cauchy gives e_H b^-|nu|, and summing multiindices gives exactly (1-s/b)^(-D|H|). There is no omitted factorial or unbounded fine dimension. D is the original activity's cell coordinate count, not automatically the retained Gaussian dimension or the full stationary block dimension. The norm conversion to a scalar polydisc is explicit.

2. **Original carrier and connected support.** Retaining pi(H) as an internal carrier and attaching a rooted tree for every scalar occurrence gives a connected output K containing all true variables. The estimates |K|<=|pi(H)|+T_tot and d(z,pi(H))<=T_tot for z in K are valid even with repeated supports, shared trees and periodic wrapping. A connected lattice carrier K has metric MST length |K|-1. The proof therefore avoids deleting auxiliary roots from a metric tree.

3. **Anchored norm.** The factor e^(-delta d(z,pi(H))) is obtained by spending delta on the attached-tree sum. Rerooting it through sum_(i in H)e^(-delta d(z,pi(i))) gives exactly the fiber multiplicity F and the lattice sum S_delta. The conditions beta+delta<=kappa and beta+D log[1/(1-s/b)]<=a0 are sufficient. The order sum is performed for each fixed H before the root sum, so there is no supremum/order-sum interchange of the kind corrected in the stationary-gradient lemma.

4. **Vacuum and improved small-radius factor.** Subtracting the nu=0 terms leaves an explicit vacuum sum, with local density sum_(H contains i)E_H(0)/|H|. The refinement using exp(alpha k)-1<=alpha k exp(alpha k) and a strict reserve rho gives alpha sup_(k>=1)k exp(-rho k); the stated upper bound 1/(e rho) is valid. It is an explicit radius-loss gain, not scale contraction at a common radius.

5. **Projection and current-block fibers.** The actual stationary theorem groups current angles in an L-block output fiber and uses next-coarse w-cell labels on that same block graph. It implies the component bound rooted at pi(i) for original unit-current cells, with F=L^d, and implies the identity-projection version for activities already on those block cells. If a later step instead groups next-coarse variables into another Gaussian L-block, that is another projection/norm conversion, not an implicit identification. The transport theorem states its required projection properties and fiber factor, so either application must instantiate them explicitly.

6. **Optional connected compression.** The packing estimate in Section6 checks: maximal sup-separated centers with separation r_L have covering balls of radius r_L-1, each meeting at most 2^d blocks; graph balls of radius floor((r_L-1)/2) are disjoint. When there is another center, a path inside connected H supplies at least k_L vertices in each ball. This gives |pi(H)|<=2^d max(1,|H|/k_L), including compatible periodic geometry. The independent exponent requirement beta+delta<=kappa remains essential and is not removed by this packing gain.

7. **Compatibility with the physical branch.** The stationary theorem supplies strict scalar components u_(i,alpha;X) with each coefficient vanishing at zero and s(r)<=C r on its uniform one-step ball. Its physical branch identification is separate and uses the known gauge-zero minimum plus uniqueness. No alternative background or interacting saddle is silently inserted by the transport theorem.

The proof is ready to be combined with the corrected stationary theorem on the common smaller domain. The exact remaining issue is iteration of those domains and budgets, including required output support exponents, rather than a missing combinatorial step in this bounded substitution theorem.
