# Classical background composition modulo gauge

17 October 2026. Proof candidate for independent audit. Scalar holomorphic germs on finite compatible periodic regulators; no assertion about equality of sequential and one-shot fluctuation integrals or canonical activity families.

## 1. Maps and the exact lattice identification

Fix the primitive odd ratio ell. Let M=ell^k, R1=ell^s1 and R2=ell^s2. Write U_n(D) for the selected ordinary homogeneous Wilson minimizer at total refinement n, supplied by Notebook15. Its potential, in physical units with final spacing one, obeys a uniform C^(1,alpha) bound C||log D/i||. It is a minimum among all ordinary-feasible fields in a fixed small global-potential ball, and equality in that ball implies fine gauge equivalence. These are the actual comparison and equality conclusions of `ordinary_constraint_transfer_fragment.tex`, Theorem `ot-minimum`.

Define the pre-root-gauge current configuration

    P_(M,R)(D)=M_ell^k(U_(MR)(D)),                       (1.1)

with logarithm a_(M,R)=log P_(M,R)/i. Thus M_ell^s P_(M,R)(D)=D. The field D lives on the next-coarse lattice, while P_(M,R)(D) lives on its R-times finer current lattice. All operators below include the natural relabeling of these nested lattices.

For a gauge-invariant scalar total E on the current lattice, define

    (T_(M,R)E)(D)=E(P_(M,R)(D)).                         (1.2)

The ordinary prefix estimate gives a common classical radius b_cl and constant C0, independent of M,R and volume, with

    ||a_(M,R)(exp(iw))||_infinity <= (C0/R)||w||_infinity. (1.3)

The notation T here is a background-substitution operator, not a quantum RG transformation.

For the two-step comparison take a final datum Z on the coarsest lattice and put

    U2=U_(MR1R2)(Z),
    D1=M_ell^(k+s1)(U2)=P_(MR1,R2)(Z),
    U1=U_(MR1)(D1).                                     (1.4)

Both U1 and U2 are configurations on exactly the same original fine graph. To see the physical factors, use final-Z units: the fine spacing is eta2=(MR1R2)^-1, the D1 spacing is R2^-1, and the original current spacing is (R1R2)^-1. The definition of U_(MR1)(D1) uses D1-unit coordinates, where its fine spacing is eta1=(MR1)^-1. Thus eta1=R2 eta2, and its graph and oriented links agree with those of U2 after rescaling coordinates by R2.

In d=4 the coupling-free Wilson action is the same sum of plaquette terms under this relabeling. No coupling or fluctuation cutoff is being rescaled in this comparison.

## 2. The two genuine minimum comparisons

Exact ordinary composition gives

    M_ell^(k+s1)(U1)=D1=M_ell^(k+s1)(U2),
    M_ell^(k+s1+s2)(U1)=Z=M_ell^(k+s1+s2)(U2).           (2.1)

The comparison radii can be made common for any fixed finite R1,R2, uniformly in M and volume. Here is the explicit scale issue. If A1 is a fine potential in D1-unit coordinates, then the same field in final-Z units has

    A1^Z(x)=R2 A1(R2 x).

Consequently

    ||A1^Z||_(C^(1,alpha))
       <= C R2^(2+alpha) ||A1||_(C^(1,alpha)).           (2.2)

In the reverse direction the norm can only decrease, up to a fixed convention constant, and its supremum acquires R2^-1. By (1.3), ||log D1/i||<=C0||log Z/i||/R2, so U1 in final-Z units is bounded by C R2^(1+alpha)||log Z/i||. U2 in D1 units is bounded by C||log Z/i||/R2. Shrink the real Z-ball so both competitors lie within the corresponding fixed comparison radii. This uses only finitely many constants for fixed R1,R2; none depends on M or volume.

The ordinary minimum at D1, using U2 as a feasible competitor, gives

    S(U1)<=S(U2).                                      (2.3)

The ordinary minimum at Z, using U1 as a feasible competitor, gives

    S(U2)<=S(U1).                                      (2.4)

Thus equality holds. The equality clause of the ordinary-minimum theorem supplies a fine gauge g with

    U1=U2^g.                                           (2.5)

The proof of that theorem supplies this gauge by the small ordinary-to-corrected transfer, the constraint-preserving gauge flow into the flat slice, and the inverse transfer from the same strict slice minimizer. Each transformation is small and smoothly controlled in the local class. In particular it can be joined to the identity by a path whose potentials remain in a sufficiently small neighborhood, after a further fixed-radius reduction. It is not merely an assertion that equal action values always imply gauge equivalence.

Ordinary gauge covariance now gives

    M_ell^k(U1)=(M_ell^k(U2))^(g|current).               (2.6)

Therefore

    P_(M,R1)(P_(MR1,R2)(Z))
       is gauge equivalent to P_(M,R1R2)(Z).            (2.7)

The gauge need not be uniquely chosen or identity at all intermediate current sites. Its restriction to the D1 sites stabilizes D1 because both fine fields have the same D1 constraint. No equality of the two chosen representatives is claimed.

## 3. Scalar germ identity and continuation

Let E be holomorphic on a current-angle product ball and locally gauge invariant there. On the sufficiently small real Z-ball used above, the small gauge path in (2.6) lies inside that ball. Hence

    T_(MR1,R2)(T_(M,R1)E)
             =T_(M,R1R2)E                             (3.1)

as scalar functions. The maps on both sides are holomorphic in Z on their common domains. Uniqueness of holomorphic continuation from the real slice proves (3.1) as a germ at zero, and then on every connected common product domain reached by these specified branches.

This argument uses invariance of the total E. It never applies a gauge transformation separately to a generally non-invariant coefficient E_H.

There is a useful same-ball case. If R1,R2>=C0 and 0<b<=b_cl, the angle bounds (1.3) ensure that both successive substitutions and the direct substitution map the radius-b ball into the original radius-b domain of E (strict inequalities follow by taking R_i>C0). Thus both sides are analytic on the same connected radius-b product ball. Their equality there follows from the small-germ comparison even if the real minimum-comparison proof used a smaller radius depending on R2. No minimum statement for complex configurations, or for real configurations outside the comparison class, is being used in that continuation.

The output T_(M,R)E is also locally gauge invariant. For a sufficiently small final coarse gauge v, smoothly extend its point values to the fine lattice. The gauge transform of U_(MR)(D) is a feasible competitor for D^v. Comparing its action with U_(MR)(D^v), and applying the inverse-gauge comparison, gives equality; the ordinary-minimum equality clause then identifies the two fine configurations modulo gauge. Their partial averages are gauge equivalent. Applying E proves local invariance, first on the real overlap and then holomorphically. This is the same two-comparison argument used for the classical coarse action, now applied to the chosen orbit before evaluating E.

Consequently (3.1) may be iterated. For any finite q and fixed R=ell^s,

    T_(MR^(q-1),R) ... T_(MR,R) T_(M,R) E
                   =T_(M,R^q)E                        (3.2)

as gauge-invariant scalar germs. When R>C0 and b is in the common classical and E domains, the successive substitutions and the direct one are all analytic on the same b-ball, so (3.2) holds there by continuation. For a direct real variational proof one may instead shrink the comparison ball after fixing q; the two conclusions are compatible.

All statements are uniform in preceding M and compatible volume for fixed finite q. No infinite-q convergence or regulator consistency is claimed.

## 4. What this does and does not buy for fixed R,J

The direct representative on the right of (3.2) has the already proved bounds

    ||a_(M,R^q)||<=C b R^-q,
    ||Delta a_(M,R^q)||<=C b R^(-2q),
    ||Delta² a_(M,R^q)||<=C b R^(-(2+alpha)q),            (4.1)

with primitive constants independent of q. Its complete supported output families follow from the same pgh theorem, with endpoint ratio R^q and the same fixed primitive ell.

This permits a future purely classical spatial-remainder estimate to keep the elementary macrostep R and auxiliary grouping J fixed, and only then select a finite q large enough to beat a previously established finite constant C(J). For example a genuinely proved estimate `C(J) R^(-q alpha)` would then have a noncircular parameter order. This note does not establish that estimate in the desired activity norm: it establishes the scalar background composition identity needed to attempt it.

The canonical strict families produced by q successive core/tail transports need not equal the direct family obtained from P_(M,R^q). The proof licenses equality of their scalar sums and hence use of a **new justified localization** of that scalar function. It does not imply an automatic bound for the already chosen sequential family, nor that the direct relocalization is a bounded operator on a required quotient norm. That norm interface remains separate.

Most importantly, a product of q quantum integrations includes their separate gauge factors, normalizations, intermediate Gaussian interactions and retained windows. It is not identified here with one integral using a direct R^q contour gauge or one R^q window. The new quantum terms generated at intervening steps do not disappear from a q-step amplitude recursion. This is a classical background semigroup modulo gauge only.
