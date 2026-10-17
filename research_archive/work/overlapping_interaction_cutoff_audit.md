# Independent audit: overlapping interactions and strict background support

17 October 2026. This is an internal mathematical audit of
`overlapping_interaction_cutoff_research.md`, Sections 1–12, against
`gaussian_cutoff_locality_research.md`. It is not external certification or a
verification of the Yang–Mills source hypotheses. No output file was edited.

## Result

The two abstract arguments pass this audit under their displayed assumptions.
Sections 1–8 give a convergent Gaussian cutoff logarithm with overlapping
bounded interaction multipliers. Sections 9–12 additionally give strict
background support from the fixed background-independent baseline and the
small local precision decomposition. The resulting constants are independent
of volume when the displayed spectral, weighted matrix, interaction, and
fixed cell-dimension constants are uniform.

One harmless intermediate exponent was corrected during review. In Section 10,
after (10.3), the selected-edge estimate is

\[
 e^{m d(b,c)}|z_{bc}|\|(C_0)_{bc}\|
 \le \frac{\delta}{\max(d_b,d_c)}e^{-\kappa d(b,c)}
 \le \frac{\delta}{\max(d_b,d_c)}.
\]

The previous expression had an additional factor \(e^{-m d(b,c)}\), which
does not follow from the stated radius. The last inequality, the weighted
Schur bound \(K+\delta\), and every subsequent constant were already correct.
The author has corrected the research note and its fragment.

## 1. Exact grouping and its combinatorial cost

The identity in Section 3 is exact: expanding the cutoff defects and the
labelled multipliers, deleting the zero products \(q_iw_Y\) with \(i\in Y\),
and grouping the selected interactions by overlap connectivity gives
pairwise disjoint primitive molecules. Distinct labels with the same support
cause no problem; they remain distinct selected factors before grouping.

The rooted overlap-animal majorant is valid with the stated exponential
support reserve. Its exponential generating function counts each labelled
rooted tree with its correct multiplicity. Repeated labels and additional
spanning trees only enlarge the positive majorant. The estimate

\[
 \sup_i\sum_{S\ni i}b(S)e^{\kappa\ell(S)+3|S|}\le\eta
\]

therefore follows from the stated interaction norm, rather than from an
unstated bound on molecule cardinality.

## 2. Molecule forest formula and cellwise Cauchy radii

Every partition mask on the disjoint molecules is a partition mask on their
individual cells. Its covariance is a direct sum of principal compressions.
Convex combinations preserve the lower Hermitian bound and the upper operator
bound. This is precisely the partition-mask domain required by the BKAR
forest formula; see Theorem 1 of the primary
[BKAR exposition](https://mabdesselam.github.io/BKAR.pdf).

For a molecule tree, resolving each edge derivative into its cell endpoints
produces distinct cell-pair variables. The radii

\[
 r_{ij}=\frac{\delta}{\max(d_i,d_j)J_{ij}}
\]

give both row and column perturbation sums at most \(\delta\). A variable
changes both transposed covariance blocks, but the matrix perturbation
estimate already includes that fact; no extra factor two is missing.

The complex Gaussian density estimate on the entire polydisc correctly uses
the matrix dimension \(D|M|\), the bound on the Hermitian part of the inverse,
and the determinant lower bound. It yields the product molecule majorant
without differentiating the sharp indicators or the real-field dependence
of the interactions.

Finally,

\[
 \prod_{\{i,j\}}\max(d_i,d_j)
 \le\prod_i d_i^{d_i}
 \le e^{2(n-1)}\prod_i d_i!
\]

gives the stated \(c_G=e^2/\delta\). Zero covariance edges have zero
derivative and can simply be omitted.

## 3. Endpoint factorials and the planted recursion

The planted-tree recursion in Section 5 has the correct factorials. For a
root molecule \(S\) with incoming endpoint \(i\), distributing its outgoing
children over the cells cancels the child exponential-generating factorials
against the individual cell degree factorials. The incoming cell retains
the factor \(n_i+1\). Consequently the local generating factor is exactly

\[
 (1-t_i)^{-1}\prod_{k\in S}(1-t_k)^{-1},
\]

not a single uncontrolled molecule-degree factorial. The monotone iteration
with \(F\le2\eta\) gives \(t_k\le1/2\), and the reserved \(e^{|S|}\)
absorbs \(2^{|S|}\). The unplanted anchored sum is bounded by \(\eta\).

The spatial tree-length and cardinality weights are submultiplicative under
this assembly. The subsequent Kotecký–Preiss estimate is valid with the
size function \(|X|\). Pinning a polymer occurrence that contains the
specified root cell overcounts the absolute logarithmic series, as required.
The comparison using \(w_Y\mapsto t w_Y\) gives the stated \(8\epsilon\)
bound. This interpolation concerns bounded multipliers, not an unjustified
complex continuation of a moving cutoff.

## 4. Strict-support covariance and density algebra

The root algebra in (10.1) is submultiplicative, and enlarging its marked
root set is contractive. The product-domain assumption is substantive: it
makes the local coefficient suprema compatible with union convolution.

In a precision Neumann path, every background label attaches to its two
marked endpoints. Combining the internal support trees with the covariance
links proves (10.2), including both the \(\ell_M(X)\) weight and the separate
endpoint-distance weight. The bound is a full marginal bound, not merely
an estimate on the visible forest edges.

The chosen endpoint graph need not span or connect all cells of a molecule.
Neither the baseline inverse estimate nor the perturbation support-algebra
estimate needs this property. Both use only the number of selected incident
edges at each cell. With the corrected intermediate exponent above, the
baseline weighted Schur norm is at most \(K+\delta\). Weighted conjugation
then gives the stated inverse Schur constant \(L\).

The complete density expansion includes both determinant and inverse. Its
support-algebra bounds are

\[
 \|M^{-1}-M_0^{-1}\|\le w,
 \qquad
 \|\operatorname{Tr}\log(I+M_0^{-1}E)\|
 \le D|M|[-\log(1-u)].
\]

The determinant factor costs at most \(2^{D|M|/2}\), and the quadratic
correction uses at most half the baseline Gaussian decay. Combined with
the original density comparison and the change from covariance \(V_*I\)
to \(2V_*I\), these give exactly
\(\widehat K_G=(8V_*/\lambda)^{D/2}\).
Interaction factors on \(Y\subset M\) have \(\ell_M(Y)=0\), so (10.8)
follows with the stated molecule and bad-singleton constants.

The strict-support proof does not need to identify the full perturbed
covariance with the baseline edge envelope \(J_{bc}\). Its Cauchy domains
are justified instead by the separate baseline and support-algebra
perturbation estimates. This distinction prevents an unnecessary extra
hypothesis on \(C(A)\).

## 5. Formal factorization and hull conversion

Retaining precision-label tags makes the forest factorization exact before
evaluating the background. At a forest mask the full marginal covariance
is block diagonal over the molecule components, so its normalized density
factorizes as a formal power series. Overlap between the background labels
of different components does not invalidate that matrix identity. Grouping
coefficients by their support unions respects multiplication. Injecting the
component root algebras into the full root algebra is contractive.

The gas remains hard core in its marked supports, not its larger background
supports. This is essential and is handled correctly. For a connected
logarithmic cluster, the mark-union tree length and attached-background
forest length are bounded by their sums over the cluster. The pinned
estimate therefore proves (11.2).

For the fixed connected hull \(H(M,X)\), writing
\(L_* = \ell(M)+\ell_M(X)\), the estimates

\[
 |H|\le |M|+L_*,\qquad d(a,b)\le L_*,
 \quad a\in M,\ b\in H,
\]

give (11.3). Summing over possible marked anchors costs precisely the
lattice convolution \(S_{\kappa/2}\). This correctly controls roots located
in a background support or in an added connecting path, not only roots
already in the marked set. The same bounded hull map applies to the
interaction comparison, giving \(8S_{\kappa/2}\widehat\epsilon\).

## Scope retained

The conclusions are finite-volume holomorphic expansions with uniform
norm bounds. They do not prove consistency between volumes, individual
activity gauge invariance, all lattice symmetries of a deterministic hull
choice, an admissible Yang–Mills product background chart, or an actual
small precision decomposition uniform over renormalization histories.
The assumptions that each cell has fixed dimension and each multiplier is
uniformly bounded on its fixed real cutoff remain essential. A tunable
real-baseline refinement is being developed separately and is not part of
this audit.
