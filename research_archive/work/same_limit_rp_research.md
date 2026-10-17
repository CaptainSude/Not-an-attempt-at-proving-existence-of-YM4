# Same-limit diagonal RP for pure Wilson SU(2): modular proof attempt

16 October 2026. This is a research reduction, **not an established same-limit theorem**. It identifies a plausible replacement for the QED3 fermion/contour argument and records the exact interfaces still requiring independent audit. No change to the repository is made.

## 0. Status and exact next targets

The finite adapted-torus diagonal RP lemma is proved separately in `work/diagonal_rp_research.md`. It does not settle the law obtained from coordinate tori.

The following work yields:

1. A rigorous compact-group convolution lemma for the SU(2) Wilson kernel, with an explicit finite-order Sobolev bound. This replaces the formal inverse-transfer operation by a well-defined operator on smooth functions.
2. A precise outer-layer elimination formula in a product-convolution coordinate representation. Its error under the sparse bounded local tilt is O(t) in supremum norm. The descent through local temporal gauge is explained, but should be checked at the oriented-link level before treating the gauge-theory version as a theorem.
3. An operator amplification strategy that needs reflection invariance only at two adjacent **clean link planes** in each direction. Those planes avoid all copies of the tilted source. This bypasses the non-Abelian analogue of QED3's electric-character norm estimate.
4. A specific remaining geometric issue: QED3's convenient cell construction uses `4h | n` with h even. The YM4 regulator has n=2L^(m+K), L odd, so that construction does not apply verbatim. Alternating site/link coordinate cell walls may repair it, but no complete proof is supplied here.

**Exact next targets:** prove the clean-plane amplification lemma in §6, with a complete transfer-kernel normalization and cell count, then prove a two-frame placement lemma for the actual n=2L^M sequence. The SU(2) convolution lemma in §3 is suitable for independent verification now.

## 1. What QED3 actually does

The supplied [QED3 manuscript](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/e392ef45013a581664bab76b90867170b30fe10e/QED3_slop/qed3.pdf), §§3–4, has four logically different steps:

* A slab trace and Schatten inequality fold a coordinate-torus source into a diagonal-torus source.
* Equality of pressures removes an error after first taking volume to infinity at fixed positive tilt t.
* An operator amplification bound, followed by two-layer reduction and outer-layer elimination, proves extra translation invariance of the comparison states when t tends to zero.
* Convex separation transfers diagonal RP to the original coordinate-torus law.

The third step is essential. Pressure equality alone produces a wall-periodic, diagonally RP comparison Gibbs state; it does not make that state translation invariant. The free-cube averaging counterexample in the previous note also rules out simply averaging its translates.

For pure gauge fields, compactness removes the need for Gaussian tails, fermion insertions, unbounded-curvature integrability, and imaginary integration contours. It does not by itself supply the missing translation invariance.

## 2. The portion that immediately simplifies

Fix lattice spacing, a finite β>0, and gauge group SU(2). Write the Wilson weight as

    exp[(β/2) Σ_p Re Tr U_p].

For any finite link set, all local smooth functions are bounded. The infinite configuration space SU(2)^E is compact in the product topology, so every family of probability laws is tight.

### 2.1 Pressure control

Cutting or regluing a finite-range bounded interaction along a surface changes log Z by at most a constant times the number of affected plaquettes. For fixed β, this gives a common thermodynamic pressure for coordinate rectangular tori and diagonal adapted tori whose shortest periods tend to infinity with bounded aspect ratios. For a qualitative cube-tiling argument, tile by boxes of side b, bound all removed interactions by their supremum norm, first let the overall size tend to infinity and then b tend to infinity. The interface contribution per unit volume is at most Cβ/b, and the uncovered boundary contribution tends to zero at fixed b. This supplies an o(volume) difference between log Z and volume times the common pressure. No O(1/n) finite-size rate is asserted from this two-stage argument; such a rate would require a separate finite-size boundary comparison. The qualitative error suffices for the proposed amplification limit.

This is a statement about log Z divided by volume. It gives no convergence of local states by itself.

### 2.2 Fold comparison

The positive crossing kernel from the previous note permits a Hilbert-space cut at a diagonal mirror. A boundary Hilbert space contains the boundary-link Haar variables and a feature space for each plaquette cut along a diagonal. The feature expansion of the crossing kernel has finite squared norm. Thus a bounded slab insertion defines a Hilbert–Schmidt operator; reflection gives its adjoint, gluing contracts its boundary variables/features, and a tangential closing shift is unitary. This is the pure-gauge version of the slab construction used in QED3 §3.

After a complete normalization/geometry check, the resulting Schatten folding inequalities should have the same form as QED3 (3.21), (3.25), (3.26). The four-dimensional version uses the frames

    (t,x,y,z),    (t−x,t+x,y,z).

The geometry changes only in the first two coordinates.

Let O be a real, gauge-invariant local polynomial contained in one open diagonal cell Q. Let V_n be the sum of its reflected copies on the adapted torus D_n, and let μ_(D_n,t) be the law tilted by exp(tV_n). The folded source preserves RP at the cell walls. Jensen, the fold inequality, and convexity of log μ_D(exp(tV_n)) give

    μ_C_n(O) ≤ μ_(D_n,t)(O) + |Q| δ_n/t,

where δ_n→0 is a pressure error. Compactness permits the ordered limits n→∞, then t↓0. Every resulting comparison law λ is gauge invariant, RP and invariant at the chosen diagonal cell walls, and satisfies

    ν(O) ≤ λ(O)

for the original coordinate-torus limit ν. Standard finite-volume conditional-density identities also pass to the unperturbed Wilson DLR equations when t↓0, since only finitely many source copies meet a fixed local region.

None of these observations yet gives translation invariance of λ.

## 3. Proved SU(2) convolution lemma

Put G=SU(2), with normalized Haar measure, and

    kβ(g)=exp[(β/2)Tr g],
    (Cβψ)(v)=∫_G kβ(vw^−1)ψ(w)dw.

Cβ is a positive, injective, smoothing, self-adjoint convolution operator on L²(G). Its scalar eigenvalue on the spin-j Peter–Weyl sector is

    c_j = 2 I_(2j+1)(β)/β > 0.

Indeed, the Haar class measure is (2/π)sin²θ dθ and χ_j(θ)=sin((2j+1)θ)/sinθ. Integration gives

    ∫ kβ χ_j dHaar = I_(2j)(β)−I_(2j+2)(β)
                     = 2(2j+1) I_(2j+1)(β)/β,

and division by the representation dimension gives c_j.

Let f be a finite Peter–Weyl polynomial, with largest spin r. Define on finite Peter–Weyl sums

    T_f = Cβ^−1 M_f Cβ.

Then T_f extends continuously from C∞(G) to itself. More precisely, for every Sobolev index s,

    ||T_f ψ||_(H^s) ≤ C_(β,f,s) ||ψ||_(H^(s+2r)).

The same assertion holds for its Hilbert-space formal adjoint and for the reverse conjugate Cβ M_f Cβ^−1.

**Proof.** Multiplication by a spin-r matrix coefficient maps the spin-j sector into spins k with |k−j|≤r. On the corresponding block, T_f contributes a ratio c_j/c_k. For an integer q≥0,

    I_n(β) = (β/2)^n / n! · S_n,
    1 ≤ S_n = Σ_(l≥0) (β²/4)^l n!/[l!(n+l)!] ≤ exp(β²/4).

Consequently, for a fixed integer shift q≥0, I_(n+q)/I_n≤C(1+n)^(-q) and I_n/I_(n+q)≤C(1+n)^q. Thus c_j/c_k≤C(1+j)^(2r) on the finite band. The number of neighboring spin sectors is bounded in terms of r, and each multiplication block has norm at most ||f||∞. Weighted ℓ² summation proves the Sobolev estimate. Summing finitely many representation components proves it for f. Sobolev embedding, with arbitrarily large s, yields continuity on C∞. □

For a finite set S of spatial links, the tensor-product version holds with C_S=⊗_(e∈S) Cβ. If f is a finite Peter–Weyl polynomial on G^S, T_f=C_S^−1 M_f C_S is a continuous operator C∞(G^S)→C∞(G^S), with a finite derivative loss depending on the representation degrees of f. These constants do not depend on the ambient torus.

### 3.1 Exact local identity

For smooth B on G^S,

    C_S T_f B = f · C_S B.

Equivalently, writing K_S(v,u)=Π_(e∈S) kβ(v_e u_e^−1),

    ∫ K_S(v,u) f(u) B(v) dv
      = ∫ K_S(v,u) (T_f B)(v) dv.                 (3.1)

This equality remains valid when B depends smoothly on additional compact parameters, including u viewed as an external parameter: apply the identity for each fixed value of those parameters before evaluating at u.

This is the usable substitute for a contour shift. T_f acts nonlocally in the group coordinate of each selected link, but it reads no new lattice sites. Its finite derivative loss makes its action on smooth local weights controlled.

The lemma is specific here to SU(2). General SU(N) diagonal RP does not by itself prove the analogous polynomial ratio bound for its Wilson convolution eigenvalues.

## 4. Outer-plane elimination: exact analytic formula, gauge interface to audit

Suppose a gauge-invariant local observable P reads no links below coordinate plane j. In a local temporal gauge on its finitely many outgoing temporal bonds, the electric crossing weights for selected spatial links S have exactly the product form K_S(v,u), where u belongs to plane j and v to plane j+1. All other action factors that depend on v involve only planes j+1 and j+2 and spatial neighbors. Denote their product by W(v;η). For fixed S, W is smooth, strictly positive, and bounded above and below uniformly in the exterior compact variables η.

For one Peter–Weyl term of P, write P=f(u)P_+(v,η). Applying (3.1) transfers it to

    Q(v,η) = W(v;η)^−1 T_f[W(·;η)P_+(·,η)](v). (4.1)

Q reads no links in plane j. It is a bounded smooth local function. The new support reaches at most plane j+2 and a fixed spatial enlargement.

Now include a bounded smooth source array exp(tV_n). For the selected v variables, only finitely many source copies contribute; write their sum as R(v;η,u). The terms of V_n independent of v factor out. Formula (3.1) gives the exact tilted replacement

    Q_t = W^−1 e^(−tR) T_f[e^(tR) W P_+].       (4.2)

By the Sobolev estimate and compactness of all local group variables,

    ||Q_t−Q||∞ ≤ C t,    0≤t≤1,                (4.3)

uniformly in n once the fixed support embeds. The constant depends on finitely many derivative norms of R, W, and P_+, hence on the local source and the selected finite link set, not the total number of source copies. R may read u; its contribution to (4.2) is absorbed into the O(t) error. The untitled Q in (4.1) is independent of u.

Thus the corresponding expectations differ by at most Ct, using only that the tilted law is a probability measure. No operator amplification is needed for this error estimate.

After one elimination Q need not be a finite Peter–Weyl polynomial. Approximate it uniformly by one and continue. There are only finitely many layers to remove. Choosing a sufficiently accurate approximation at each step produces a two-layer observable Y_ε, independent of n and t, with

    |μ_(D_n,t)(P)−μ_(D_n,t)(Y_ε)| ≤ ε+C_ε t.   (4.4)

Eliminate lowest planes first until the target lower plane is reached; eliminate highest planes second. An upper-plane elimination can reach down only two planes, so this order retains the required lower bound, exactly as in QED3's layer bookkeeping. The construction transports under a fixed lattice reflection; the reflected observable has the same estimate with the reflected Y_ε, without assuming the tilted torus is invariant under that reflection.

### Gauge descent requiring a careful check

The intended implementation fixes the finitely many temporal links whose endpoints cover S and the original temporal support. Haar invariance makes this a legitimate local change of variables. The product electric kernel is then explicit. Residual gauge transformations satisfy g_j=g_(j+1) on the fixed bonds. Since C_S commutes with the left/right gauge actions, the sum of the transformed terms in (4.1) should retain residual gauge invariance. Because it no longer reads the lower plane, that invariance should become ordinary gauge invariance on its new support, allowing the expression to descend to unfixed link variables without reintroducing the eliminated temporal bonds. Peter–Weyl cutoffs commute with those gauge actions, so the approximations can preserve gauge invariance.

This is a concrete finite-link covariance check, not an infinite-volume uniqueness claim. It has not been expanded here into complete oriented-link formulas. It is the first gauge-specific interface to verify before invoking (4.4) for Wilson observables.

## 5. Two-layer insertions are easy to approximate on compact groups

At a coordinate link plane c=j+1/2, let H_S=L²(G^S). For a bounded local operator X commuting with the spatial gauge action, form the kernel of

    C_S^(1/2) X C_S^(1/2).

For X equal to the identity or a finite Peter–Weyl kernel operator (and their finite local algebraic combinations), this kernel is continuous. Divide it by the strictly positive crossing kernel K_S, using the temporal parallel transports to identify the two spatial slices. Call the resulting bounded gauge-invariant crossing insertion G_X. Then

    G_I=1,    Θ_c G_X=G_(X*).

Enlarging S by tensoring X with the identity does not change G_X. Spatial lattice symmetries conjugate X unitarily or antiunitarily and preserve its norm.

For a smooth gauge-invariant two-layer observable Y, its crossing kernel is K_Y=K_S Y in temporal gauge. Let P_M be a finite Peter–Weyl spectral cutoff on H_S. The kernels of P_M K_Y P_M converge uniformly to K_Y. Define

    X_M=C_S^(−1/2) P_M K_Y P_M C_S^(−1/2).

Each X_M is bounded and finite rank because every eigenvalue c_j is strictly positive. Gauge covariance is preserved. Therefore

    ||G_(X_M)−Y||∞ → 0.

The norms ||X_M|| may diverge. The correct order is volume limit, tilt removal, then M→∞. Uniform boundedness in M is neither claimed nor needed.

If one can establish

    limsup_(n→∞) |μ_(D_n,t)(G_X)| ≤ exp(A_S t)||X||, (5.1)

then the comparison law λ defines a unital norm-one functional X↦λ(G_X). Such a functional is Hermitian. The kernel adjoint identity and the above approximation show that λ is reflection invariant for all two-layer observables at c. Combining this with (4.4) shows reflection invariance for all local observables at that plane.

## 6. Proposed clean-plane amplification lemma

### Why only clean planes are needed

Let the source O be supported in a coordinate box of radius r_O inside its diagonal cell of height width h. In each of the first two coordinate directions, all reflected source boxes have at most four center residues modulo h; in the transverse directions there are at most two. Choosing h sufficiently larger than r_O leaves two adjacent half-integer coordinate planes c and c+1 meeting no source box. Call these planes clean. Taking their two reflections gives translation by 2e_μ. Doing this in every coordinate direction gives 2Z^d invariance, which is all that the convex-separation placement requires.

At a clean plane no source copy reads links on both sides of the cut. This distinction is used in the operator trace bound below. No claim of reflection invariance at every plane is initially needed.

### Precise target lemma

Fix β>0, one sparse reflected source array V_n, a clean coordinate link plane c, and a finite support S at that crossing. Prove (5.1), with A_S independent of X and n. The coefficient may depend on the support size, O, h, and β.

### Proposed proof

1. Place G_X in a much larger diagonal cell and use diagonal chessboard amplification. The coarse diagonal wall group preserves V_n. If N'_n is the number of coarse cells,

       |μ_(D_n,t)(G_X)|^(N'_n)
       ≤ Z_D_n[exp(tV_n) Π_g (G_X)^g] / Z_D_n[exp(tV_n)].

2. Choose a coordinate grid that contains each reflected G_X box in a distinct coordinate cell and cuts none of the reflected source boxes. Apply the second, diagonal-to-coordinate, fold inequality. Each resulting coordinate fold contains copies of one insertion with a single fixed time direction, together with copies of the source pieces in that cell.

3. Because the original crossing plane was clean and diagonal reflections preserve V_n, source factors do not cross any of the insertion planes in this coordinate fold. The folded source is therefore divided into bounded perturbations of slabs between the operator insertions.

4. In a coordinate transfer representation, combine insertions at the same time cut into tensor products X_j. Their norms are bounded by the product of the individual ||X||. A perturbed slab between successive cuts is an operator S_j^t. For an even integer J, its Schatten power

       ||S_j^t||_J^J = Tr[(S_j^t)*S_j^t]^(J/2)

   is the partition integral of J reflected slab copies. It contains positive Wilson factors and source weights. Bounding the latter by their suprema gives

       ||S_j^t||_J ≤ exp(t M_j) Z_rect(J l_j, cross-section)^(1/J),

   where l_j is that slab's length and M_j bounds its total source. Square-root electric kernels at the operator cuts glue in pairs to the original positive electric kernel; one must not assume the square-root kernel itself is pointwise positive.

5. Choose J equal to the even number of slabs/cuts. Schatten Hölder yields a bound for the cyclic product, with a factor Π_j||X_j||. The lengths l_j can alternate, so the comparison rectangular tori may have different time lengths J l_j. Their aspect ratios stay bounded and all sides diverge. Their log partition functions therefore have the same bulk pressure. The resulting normalized bound costs exp(o(volume)), not a uniform constant.

6. The total source cost is at most exp(t N_n||O||∞). The denominator is at least exp(−t N_n||O||∞)Z_D_n. The original and comparison torus pressures agree. Taking the N'_n-th root, where N'_n is proportional to volume with a fixed cell size, kills the o(volume) errors and gives (5.1).

This would replace QED3's character expansion and electric-shift operator norm estimate by positive folded path integrals. It requires a full check of the physical gauge projector, normalization of the local insertion, the even number of cuts, and the stated placement. Those checks have **not** been completed in this note, so (5.1) remains the central unproved target.

## 7. Geometry and the regulator's factor-of-two issue

For conveniently divisible sides, QED3 §4.4 supplies a purely geometric two-frame placement. Its extension to d=4 retains its first two-coordinate formulas and adds another independent transverse reflection bit. One chooses h''≫r+h and kh≫h'', both appropriately divisible. Coarse diagonal images of the insertion center take the form

    y+h'' κ(g)+s(a),    |s(a)|∞<2h,

where the 2^d parity classes have distinct bounded index vectors. Large kh/h'' separates them. Coordinate walls can be chosen in intervals of length greater than 2h while avoiding the finitely many forbidden source residues. This puts all insertion boxes in distinct coordinate cells and all source boxes inside cells.

However, QED3 requires n divisible by 4h and chooses h even. Its volume family n=8L^M is designed for this. The YM4 fine-lattice coordinate side is n=2L^(m+K), with L odd. There is no subsequence with 4|n. Thus the above convenient geometry is **not yet a theorem for the YM4 volume sequence**.

A possible repair is to take odd diagonal cell width h dividing n/2 and, after straightening to a coordinate torus whose short side is n/2, use coordinate cell widths h'' equal to a half-integer. Their walls alternate between coordinate site and link mirrors, both available for pure Wilson theory. Choosing 2h'' an odd multiple of h gives an even number of cells on the short side. One would then avoid two forbidden wall residue classes rather than one. This looks arithmetically feasible but requires a separate complete placement and gluing proof. It is not included as an established lemma.

Changing to highly divisible volumes is another possibility only if the needed RG bounds are also proved for that changed regulator family; it cannot silently be substituted into the existing construction.

## 8. Conditional conclusion once the interfaces close

Assume the gauge descent in §4, amplification lemma (5.1), and the regulator-compatible geometry in §7 are proved.

For any prescribed coordinate-torus subsequential limit ν and any real gauge-invariant local polynomial O, construct the ordered-limit comparison law λ. Sections 4–6 give invariance under all even translations. It retains diagonal wall RP.

Fix the target diagonal mirror. Translate O by an even vector so its support lies in one open diagonal cell bounded by that mirror and a distant parallel mirror. Original ν is translation invariant because its finite coordinate-torus laws are. The comparison λ is invariant under the selected even translation. The fold comparison therefore gives ν(O)≤λ(O) in the original position.

Let R be the set of gauge-invariant laws that are invariant and RP at the target diagonal mirror. It is convex and weakly compact: the configuration space is compact, and the defining equalities and inequalities are closed on continuous local tests. Gauge-invariant local Peter–Weyl polynomials separate gauge-invariant laws (average an arbitrary local polynomial over the finite endpoint gauge group). Thus the preceding one-observable domination, for every O with a comparison λ∈R allowed to depend on O, implies ν∈R by convex separation.

This yields diagonal RP for the **original** coordinate-torus law without uniqueness. Signed coordinate permutations and translations transport it to the other diagonal mirrors. Coordinate RP was already present in the same law. No claim about full continuum rotations follows from this statement alone.

## 9. Literature checks and limits of the conclusion

The original Osterwalder–Seiler paper, [*Gauge field theories on a lattice*](https://doi.org/10.1016/0003-4916(78)90039-8), establishes lattice physical positivity and strong-coupling results. [Kazakov–Zheng, p. 3/Fig. 5](https://arxiv.org/pdf/2203.11360) explicitly uses site, link, and diagonal Wilson RP. Neither retrieved text supplied the same-limit comparison required here.

[Shen–Zhu–Zhu](https://arxiv.org/pdf/2204.12737), Theorem 1.2 and Remark 1.3, proves uniqueness and independence from boundary conditions at sufficiently small inverse coupling. Its SU(N) condition is |β|<1/[16(d−1)] with action exponent NβΣReTr U_p. That theorem supplies the comparison in its strong-coupling range, but does not cover the asymptotically free regime sought here.

A primary general construction statement in Brydges–Fröhlich–Seiler, [*On the construction of quantized gauge fields, I*](https://omeka.ihes.fr/document/P_78_237.pdf), says periodic hypercubes provide a translation-invariant reflection-positive infinite-volume state. That statement alone does not resolve diagonal RP: its hypercube construction gives the standard coordinate reflections, and I did not verify a theorem there with both mirror families for the same state.

**Current conclusion:** compact pure Wilson variables substantially simplify the QED3 comparison problem. The convolution lemma and local O(t) formula provide a concrete possible replacement for the QED3 contour/fermion step. The clean-plane amplification and actual-volume geometry remain explicit proof obligations. Same-limit diagonal RP has not been promoted to a theorem in this audit.
