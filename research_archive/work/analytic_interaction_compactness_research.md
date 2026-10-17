# Compactness of analytic interactions and coherent background families

17 October 2026. Proof candidate. This concerns analytic local interactions and classical maps, not probability measures or a continuum quantum field theory. It supplies a possible infinite-volume interface for the total-kernel and spatial-transport theorems.

## 1. Connected analytic interactions

Fix the current cell size J, analytic radius b>0, connected-carrier exponent a>0 and finite number of scalar coordinates per cell. Let cubic periodic lattices exhaust Z^4 through compatible side lengths. Suppose E_N has connected analytic coefficient families E_(N,H) with

    sup_I sum_(H contains I) exp(a|H|) ||E_(N,H)||_b
       <= epsilon.                                    (1.1)

No consistency between different volumes, and no symmetry of individual coefficients, is assumed. All equalities of total functionals below are vacuum-normalized. For a compactly supported field A define

    Phi_N(A)=sum_H [E_(N,H)(A|H)-E_(N,H)(0)].           (1.2)

A coefficient disjoint from the field support contributes zero. Consequently |Phi_N(A)|<=2 epsilon times the number of cells meeting the support, uniformly for ||A||<b.

For every fixed finite connected H in the infinite cell graph, its embedding in a sufficiently large central portion of the torus is unambiguous. Its coefficient is holomorphic on a fixed finite-dimensional polydisc and bounded by epsilon exp(-a|H|). Montel's theorem, or diagonal extraction of its bounded Taylor coefficients followed by Cauchy estimates on smaller polydiscs, gives a subsequential locally uniform limit E_H. There are countably many finite H and scalar Taylor indices. A diagonal subsequence therefore works for all translated carriers simultaneously. Fatou, first over a finite selection of H and then over all H, gives

    sup_I sum_(H contains I) exp(a|H|)||E_H||_b
       <= epsilon.                                    (1.3)

The b norm here is the supremum over the open b polydisc. One first passes at radius r<b, then increases r to b. No reduced radius occurs in (1.3).

Define Phi(A)=sum_H[E_H(A|H)-E_H(0)] for compact A. To justify convergence Phi_N -> Phi, fix a finite set K of cells containing the field support and truncate carriers to |H|<=Q. Only finitely many such connected H meet K, so their locally uniform coefficient convergence applies. The omitted terms obey

    sum_(H meets K, |H|>Q)
      |E_(N,H)(A|H)-E_(N,H)(0)|
       <=2 |K| epsilon exp(-a Q).                      (1.4)

This also controls winding carriers once the torus side is much larger than JQ: any carrier of size <=Q meeting the central K then has a unique central lift. Thus Phi_N converges to Phi uniformly on every fixed finite-coordinate polydisc of radius r<b.

In particular fixed derivatives of Phi_N converge to those of Phi by finite-dimensional Cauchy. The infinite kernels used in the Ward theorem can therefore be chosen as derivatives of one analytic interaction, not merely as unrelated kernel subsequences.

## 2. Total symmetries pass

Suppose Phi_N is translation invariant, hypercubic invariant and real on real fields. Its limit has the same properties, by applying the preceding convergence to A and its fixed finite-support transform. Coefficient partitions may break these symmetries; the argument concerns total Phi.

For local gauge invariance choose a compactly supported site gauge v sufficiently close to the identity and a compact field A such that A and the logarithmic transformed field A^v remain in a fixed smaller polydisc. A^v is supported in the union of the original support and the finite edge neighborhood of the gauge support. Finite-volume invariance gives Phi_N(A^v)=Phi_N(A). Passing to the limit gives Phi(A^v)=Phi(A). Differentiation yields the exact infinite total Ward identities. Constant gauge transformations preserve compact support, so global adjoint invariance passes in the same way.

No assertion of uniqueness of the subsequence is made.

## 3. Coherent complete-field support families

Fix an endpoint ratio L and preceding homogeneous depth M. The current output of the classical map has spacing h=1/L in final units. Each bounded final-unit collar therefore has finitely many current coordinates, independently of volume (but depending on fixed L). Suppose finite-regulator maps a_N have the coherent families of the pgh theorem:

    a_N|i=sum_(X nonempty) a_(N;i,X)(w_X),
    a_(N;i,X)(0)=0,
    sup_i sum_X exp(kappa tau({i} union X)+A|X|)
              ||a_(N;i,X)||_(complete C^(1,alpha),b)
       <= C b/L.                                      (3.1)

Here kappa,A>0 and the complete norm, including all collar maxima and Hölder quotients, is inside the support sum. Coefficients with the same X agree on overlaps because they arise from one global Taylor assignment.

Apply finite-dimensional Montel and a countable diagonal extraction to every fixed collar root i, finite support X, output coordinate and Taylor coefficient. The limiting coefficients agree on overlaps. Their complete norm is lower semicontinuous: on a fixed collar it is a maximum of finitely many component and difference quotients, and locally uniform convergence gives convergence of each of them. Fatou yields the full bound (3.1) for the limiting family.

Tails cause no loss of identification. If either tau({i} union X)>Q or |X|>Q, its unweighted sum is at most C(b/L)[exp(-kappa Q)+exp(-A Q)]. For the remaining X there are only finitely many possibilities. This proves locally uniform convergence of the complete field at each finite set of roots and defines an analytic map a by the absolutely normally convergent support series. The argument simultaneously applies to any countable collection of fixed M,L after taking another diagonal subsequence; compatibility can be maintained by choosing a cofinal sequence of torus sizes divisible by the first finitely many required powers at each stage.

For compact w supported in final cells K, any nonzero coefficient must have X intersecting K, because a_(i,X)(0)=0. Its rooted tree then spans from i to K. Thus

    ||a(w)||_(complete collar i)
        <= C(b/L) exp(-kappa dist(i,K)),                (3.2)

up to the fixed finite number of cells of K if a sum over them is used. The same estimate is uniform on centered finite tori with periodic distance. It gives the summable spatial decay needed to insert a(w) into low-degree infinite kernels.

This construction supplies an infinite coherent family satisfying the explicit hypothesis of the low-kernel spatial-transport theorem. It does not choose a unique background across all possible subsequences.

## 4. Continuity of background substitution on decaying fields

The interaction Phi extends continuously to summable coordinate fields A with ||A||_infinity<=rho<b. Coordinate Cauchy and integration on the segment tA give

    |E_H(A|H)-E_H(0)|
       <= C/(b-rho) ||E_H||_b sum_(i in H)|A_i|.

Summing H first at each coordinate gives

    |Phi(A)|<=C epsilon/(b-rho) ||A||_ell1,             (4.1)

and the corresponding local Lipschitz estimate for two such fields. The finite coordinate count is already in the ell1 sum, not a volume factor.

Choose L large enough that the classical amplitude bound gives ||a_N(w)||<=rho<b on the final b ball. For compact w, (3.2) controls the ell1 tails of a_N(w) uniformly in N, after embedding the centered periodic graph in the infinite lattice. At fixed L there are only O(L^4) current coordinates per final unit cell. Truncate the output to a large fixed region, use convergence of both coefficients and a_N in that region, and then use (4.1) for the tail. It follows that

    Phi_N(a_N(w)) -> Phi(a(w))                         (4.2)

locally uniformly on compact final field supports and smaller radii. This proves an actual scalar composition limit, not just convergence of a formal Taylor expansion.

For precision about a noncompact intermediate input, coordinate Cauchy applied to (3.1) gives, on a radius-rho interior ball,

    ||partial_(w_j) a_i|| <= C/(b-rho) exp(-kappa dist(i,j)).

Only supports containing j contribute, and their rooted tree spans i and j. The fixed input/output fiber counts, including the finite L^4 current coordinates in a final cell, are absorbed in C. Summing the exponential over output roots gives an ell1-to-ell1 derivative bound, uniformly in volume at fixed L. Integrating along a segment gives a corresponding ell1 Lipschitz estimate. Since a(0)=0, summable inputs have summable outputs.

The same truncation argument therefore applies to finite compositions of these maps, provided all intermediate fields remain in a strict common interior of their analytic domains. Finite-regulator scalar identities may then be passed to a joint subsequence. In particular, a classical semigroup identity can pass in this way if the full finite list of input/output maps and interactions is extracted jointly on compatible nested volumes. This last statement requires that joint setup; separate arbitrary subsequences need not compose.

## 5. Limits of the result

The conclusion is a subsequential analytic interaction and coherent classical background maps. It makes the infinite-kernel and spatial-remainder hypotheses simultaneously attainable at fixed parameters. It is not convergence of Gibbs measures, uniqueness, consistency of a renormalization map for all input families, or a continuum existence theorem. To use these objects in an infinite quantum induction one must still prove that the actual quantum update descends to the chosen interaction space and is continuous in the topology used here, with its normalizations and cutoffs retained.
