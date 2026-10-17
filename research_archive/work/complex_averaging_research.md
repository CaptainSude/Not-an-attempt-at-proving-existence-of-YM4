# Complex multilevel averaging: normalization, incidence, and a restricted repair

Research checkpoint, 16 October 2026. Repository pinned at `e392ef45013a581664bab76b90867170b30fe10e`. The repository and output files were not modified. References `I:...` and `III:...` refer to the corresponding deposited raw TeX accounts.

## 1. Result and scope

The geometric part of the proposed averaging estimate is now exact. On the centered odd-L hierarchy, a normalized multilevel coefficient bound

\[
 (Q_n A)(c)=\sum_b M^{-d}K_n(c,b)A(b),\qquad
 M=L^n,\qquad \|K_n(c,b)\|\le K_*,
 \tag{1}
\]

together with the actual two-block support, implies absolute row and volume-transpose column bounds at most `2d K_*`, independently of n. In particular the deposited value K_*=4, **if it is a bound in convention (1) on the selected carrier**, gives both bounds at most 8d. No multiplication of the constant 4 over the n averaging steps is involved.

There is also a concrete alternative that avoids reading the missing multilevel kernel convention: the corrected one-step average has absolute row/volume-column norm 1 at the flat background. Finite-dimensional analyticity makes its norm at a small complex link background at most `1+C_L ||log V||_infty`. On a top-scale patch for which the intermediate background logarithms satisfy

\[
 \|\log M^p(U)\|_\infty\le C_{\rm av}bL^{p-n},\quad 0\le p<n,
 \tag{2}
\]

the n-step average therefore has both absolute norms at most

\[
 C_*:=\exp\!\left(\frac{C_L C_{\rm av}b}{L-1}\right).
 \tag{3}
\]

This is a proved quantitative implication for the actual one-step corrected operator, conditional on its local analytic domain and (2). The deposit uses precisely the amplitude-times-block-length form of CMP98 Proposition 6 at base 1 in I:17806–17810. The original full statement and proof have not been obtained in this session; the local domain and the selected retained patch must still be matched. Thus (3) is not advertised as a theorem for every weak complex background in the global four-layer carrier.

## 2. Which operator and which coefficient

Three conventions must remain distinct.

* The local bond operator Q_square is constructed from the order-n linear averages of CMP99b(3.16), I:23922–23930. The deposit says these are compositions of the one-step operators of CMP98(124), I:47046–47061 and47233–47242.
* The full one-step corrected operator Q(V) is transcribed at I:24355–24365. Its main term is I:24369. At V=1 all correction brackets vanish, so its flat operator is the straight-string average.
* Q^flat, the derivative of the centered group block average used for the exponential-gauge coordinates, is a different operator. Its discrete kernel is explicitly defined by `(Q^flat B)(c)=sum_b L^(-d)Q^flat(V;c,b)B(b)` at I:46981–46984. At flatness it is the straight-string average minus a coarse gradient of the averaged contour variable; adding that correction gives Q_1. This distinction is also derived at III:96589–96611 and in `work/exponential_gauge_bridge_research.md §3`.

It would be a mistake to use the flat row norm 1 for Q^flat. The contraction used below belongs to the **corrected** operator of CMP98(124), the one selected for Q_square.

Write q_n(c,b) for the ordinary discrete matrix coefficient, with no measure in the sum. The normalized coefficient in (1) is K_n=M^d q_n. If the fine lattice spacing is eta and the output spacing is ell_n=M eta, this is equivalently the kernel written with the fine counting weight `(eta/ell_n)^d`. A kernel written relative to the physical fine measure eta^d instead has density `ell_n^(-d) K_n`. These three quantities must not be given the same numeric bound.

The multilevel display I:47050 states `|Q_j(U;c,b)|≤2(1+theta_k)≤4`, with `theta_k=6 C'_1 alpha_0+kappa alpha_1`; it does not restate a multilevel measure convention there. The explicit one-step convention is useful evidence, but is not itself a proof of the multilevel dictionary. The proof I:47233–47249 invokes a separate complex averaging proposition and its input/analyticity theorem. In the passages located here this is a named invocation, not a reproduced coefficient proof.

## 3. Exact support and incidence

The blocks are centered odd-L blocks with M^d fine sites, and they partition the fine lattice; see I:794–805 and847–855 for one step. Iteration gives the corresponding M-block partition. The actual order-n support is

\[
 q_n(c,b)=0\quad\hbox{unless both endpoints of b lie in }
 B^n(c_-)\cup B^n(c_+),
 \tag{4}
\]

as recorded at I:23927–23930 and24332–24336, citing CMP98 p.31. Bond fields are represented with one positive orientation per unoriented bond. Reversed orientations are absorbed into the coefficient with their prescribed sign/transport; there is no separate free coordinate for each orientation.

For a fixed coarse bond c, the union in (4) has 2M^d sites. There are at most d outgoing positive fine bonds from each site. Hence its row has at most `2d M^d` potentially nonzero fine-bond coefficients.

For a fixed fine bond b, its endpoints belong to unique M-blocks. If they belong to the same block B(y), any coarse bond c whose double block can contain b must be incident to y; there are at most 2d such positive coarse bonds. If the endpoints belong to different blocks, the two blocks are adjacent, and c must be their joining coarse bond. Consequently

\[
 \#\{c:q_n(c,b)\ne0\}\le 2d.
 \tag{5}
\]

This argument remains valid for ordinary periodic centered tilings, with the natural identification of repeated indices, and for subsets of allowed coarse rows. It does not apply without checking to a changed hierarchy using overlapping site blocks or additional interface bonds not represented by the standard coarse nearest-neighbor bonds. The source's multiscale hierarchy can contain interface bonds; the present count is for **each fixed-level Q_n**, which is the primitive entering the local averaging operator.

Combining (1), (4), and (5) gives

\[
 \sup_c\sum_b\|q_n(c,b)\|\le 2dK_*,\qquad
 \sup_b\sum_c M^d\|q_n(c,b)\|\le 2dK_*.
 \tag{6}
\]

These are exactly the desired absolute row and volume-transpose column estimates. They hold for complex fiber matrices: the bilinear matrix transpose has the same Euclidean operator norm as the original matrix. No positivity or cancellation of q_n is used. At a fixed retained local head only levels j and j+1 enter the averaging supports (I:25742–25747,25479–25483); summing those two level estimates costs at most a factor two, not the total number of RG levels. Converting to the global hierarchy still requires the retained local/global scale comparison.

## 4. Transposes and the local constraint coefficient

Let F=eta^d I on fine bonds and M_c=diag(ell_c^d) on coarse bonds. The transpose for fine measure F and coarse counting measure is `Q^T_count=F^(-1)Q^mathsf{t}`, whereas the transpose for coarse volume measure is

\[
 Q^T_{\rm vol}=F^{-1}Q^{\mathsf t}M_c=Q^T_{\rm count}M_c.
 \tag{7}
\]

Thus

\[
 Q^T_{\rm count}\operatorname{diag}(a_n\ell_n^{d-2})Q
 =Q^T_{\rm vol}\operatorname{diag}(a_n\ell_n^{-2})Q.
 \tag{8}
\]

This is independent of any one-form scaling already built into Q. Section 4.5 explicitly fixes fine measure eta^d and coarse measure ell_j^d at I:12756–12760; the local §4.6 definitions print a_n ell_n^(d−2) at I:23961–23968 without explicitly fixing their measures. Equation (8) is the required conversion, not a claim that the original article used inconsistent conventions. If both fine and coarse spaces are instead given counting measure, the fine-measure conversion also has to be made.

With `sup_n |a_n|≤a_*`, at most N_lev contributing levels, and input/output scales within a factor R of each contributing ell_c, the proof in `current_interface_research.md §10` now gives

\[
 |h B_\square A|_{(-3)}
 \le \|h\|_\infty N_{\rm lev}a_*R^4
       (2dK_*)^2 |A|_{(-1)}.
 \tag{9}
\]

For K_*=4, N_lev=2 and R=L, the explicit conservative constant is `128 d^2 a_* L^4`. An exponential weight costs only its maximal ratio across the finite averaging support. The uniform a_n bound and the normalization identifying this B_square with the selected inverse remain inputs; I:23879–23881 refers the a_n recursion to CMP99b(3.23)–(3.24).

## 5. A direct complex repair using the actual one-step operator

### 5.1 A measure-aware absolute norm

For a discrete matrix P mapping the lattice of spacing s to the lattice of spacing t, define

\[
 \|P\|_{\rm av}:=\max\left\{
   \sup_c\sum_b\|P_{cb}\|,
   \sup_b\sum_c(t/s)^d\|P_{cb}\|\right\}.
 \tag{10}
\]

The second member is the absolute sup norm of its volume transpose. For consecutive scales,

\[
 \|AB\|_{\rm av}\le\|A\|_{\rm av}\|B\|_{\rm av},
 \tag{11}
\]

because the measure ratios multiply: `(u/s)^d=(u/t)^d(t/s)^d`. This proof uses the triangle inequality and sums of nonnegative coefficient norms, so it is valid for non-unitary complex backgrounds. Restricting rows or columns has norm at most one.

At V=1, the actual corrected one-step average is the straight-string average, I:24369. Its row sum is 1; its volume-transpose column sum is also 1. The latter follows by counting each fine bond L times among the `L^d` translated strings of length L; the deposit independently makes this count at III:96599–96607. Therefore

\[
 \|Q(1)\|_{\rm av}=1.
 \tag{12}
\]

### 5.2 Finite-dimensional analyticity supplies a one-step perturbation bound

Let V=e^{iB} on one-step double blocks. Assume the actual Q(V) of CMP98(124) is holomorphic for `||B||_infty<r_L` and extends to a neighborhood of the closed ball on which its coefficient norms are bounded by m_L. These are finite-dimensional local assertions: each row reads at most two L-blocks and all rows use the same formula. The constants depend on d,L and the fixed gauge group, not on the number of levels or the torus volume. One may always replace r_L by a smaller positive radius inside the analytic neighborhood.

The source inputs for this local analyticity are the group mean and contour formulas of CMP109(0.5)–(0.12), and CMP98 Proposition 3; the deposit uses them in III:96679–96695 and in I:46965–47007. The four correction brackets in I:24358–24365 are analytic near the identity and vanish there. The complete auxiliary definitions of g,Y,Y_x are referred to the original article at I:24399–24409, so this note does not pretend to reproduce their definition.

The support count of §3, at n=1, gives a uniform absolute norm bound `M_L:=2d L^d m_L` on that ball. Banach-valued Cauchy estimates on a line through B then give, for `||B||_infty≤r_L/2`,

\[
 \|Q(e^{iB})-Q(1)\|_{\rm av}
 \le C_L\|B\|_\infty,\qquad C_L:=2M_L/r_L.
 \tag{13}
\]

For clarity, the Cauchy bound is applied to the holomorphic matrix-valued map in its norm (10); it does not differentiate an absolute value. Integrating the directional derivative along the segment from 0 to B gives (13). Equations (12)–(13) imply

\[
 \|Q(e^{iB})\|_{\rm av}\le 1+C_L\|B\|_\infty.
 \tag{14}
\]

### 5.3 The actual composition and its uniform constant

For the selected corrected average, write

`Q_n(U)=Q(M^(n−1)U) ... Q(MU) Q(U)`

with the standard identification of scales; the composition is stated at I:47046–47061,47237–47242 and25147–25155. Suppose on every local block read by these factors one has (2), and `C_av b/L≤r_L/2`. Then (11),(14) give

\[
 \begin{split}
 \|Q_n(U)\|_{\rm av}
 &\le\prod_{p=0}^{n-1}\left(1+C_LC_{\rm av}b L^{p-n}\right)\\
 &\le \exp\left(C_LC_{\rm av}b\sum_{p=0}^{n-1}L^{p-n}\right)
 \le C_* .
 \end{split}
 \tag{15}
\]

This proves the desired row and volume-column bounds directly, with C_* in place of 2dK_*. It also proves an individually normalized coefficient bound, since every summand in the volume-column sum is nonnegative:

\[
 \|q_n(c,b)\|\le C_* L^{-nd}.
 \tag{16}
\]

Thus (15) can establish the multilevel normalization **from the one-step operator**, instead of inferring it from notation in I:47050. Shrinking b so that `C_L C_av b/(L−1)≤log 4` even gives a bound by 4, although that does not identify our constant with the separately printed theta_k formula.

No analyticity or norm estimate for the full n-step derivative is used in this proof. The all-n uniformity is supplied by the explicit summable sequence in (2). A uniform estimate `||log M^p(U)||≤C b` without the factor L^(p−n) would only yield an n-dependent exponential and is not sufficient.

### 5.4 Where the weak complex background enters

The earlier carrier has a real regular representative and a weak complex twist:

`U=e^{i eta a} U_r`, `U_r^u=e^{i eta A_r}`,
`ell_n |A_r|<a_0`, `ell_n² |nabla A_r|<a_0`, and `N(a)<a_1`,

at I:12946–12966. The gauge u is unitary, so conjugating the fine and coarse fiber coordinates by it preserves all coefficient norms. No independent-current condition is involved in Q.

Suppose a single regularity patch contains the full averaging supports under consideration and all its fine bonds have hierarchy scales at least ell_n/R. Then the amplitude part of N(a) gives `|a|≤R a_1/ell_n` on that patch. Combining the two exponentials by the local matrix logarithm gives

\[
 U^u=e^{i\eta A_c},\qquad
 \|A_c\|_\infty\le b/\ell_n,
 \qquad b=2C_{\rm norm}(a_0+R a_1),
 \tag{17}
\]

after the fixed smallness ceiling needed for the logarithm. Here C_norm converts the chosen Lie-algebra norm to matrix operator norm; for the normalized Hilbert–Schmidt norm one may use sqrt(N). The elementary bound is `||e^Xe^Y−I||≤e^(||X||+||Y||)−1`, followed by the convergent logarithm series. It does not need a second derivative of A_c.

The deposited base-one application of CMP98 Proposition 6, (159),(161),(163), I:17806–17810, bounds a depth-p averaged bond logarithm by its fine-field amplitude times its physical block length. Applied to (17), in the top-scale units ell_n, this has exactly the form (2), with a fixed C_av (any harmless fixed L factor can be absorbed there). The top-scale amplitude b must lie below that proposition's fixed radius. The separate statement I:47201–47209 invokes Proposition 6(164) to control complex averaged configurations relative to real ones.

**What is checked and what is not:** (13)–(16) are proved. The implication from the explicit patch hypotheses in this paragraph to (17) is proved. The implication `(17) -> (2)` is supplied by the precise base-one amplitude form of the cited Proposition 6 as used in the deposit, but its full primary hypotheses have not been inspected here. Matching the actual local head to one such regularity patch and the lower scale bound is a separate geometry check. For the local two-level head geometry the natural value is R=L, but no conclusion is made for an outer-seam global/local comparison without verifying it.

One should not extend the local field by zero and invoke a derivative-based global regularity theorem without checking the cutoff cost: a sharp extension can create an eta^-1 gradient. This proof needs either the actual local form of Proposition 6 on the read block or a regular extension with its norm controlled.

## 6. A further source result with narrower background scope

Raw III:96659–96760 proves a positive-majorant statement for corrected averages in a homogeneous Abelian-flux background. It uses local analyticity in the dimensionless flux `ell_j² f` and cites CMP98(139),(143). The one-step correction has a majorant of order `ell_j² |f|`, and the proof sums `sum_j ell_j²` and `sum_j ell_j ell_(j+1)`. It obtains a positive kernel majorant with uniform Hilbert-space norm.

This is useful structural support for the summable-step argument, but its scope is different. It neither asserts the absolute sup-norm row/column estimate (6) for the full weak complex carrier nor identifies every local retained geometry. A positive Hilbert-space kernel bound alone also does not immediately imply a volume-uniform absolute sup norm. The proof (13)–(16) supplies that latter norm directly, under its explicitly stronger local amplitude hypothesis.

## 7. Primary-source access record and exact remaining check

The original sources requested are:

* T. Bałaban, *Averaging operations for lattice gauge theories*, CMP98 (1985),17–51, [publisher record](https://link.springer.com/article/10.1007/BF01211042), DOI10.1007/BF01211042; normal Euclid record `https://projecteuclid.org/euclid.cmp/1103942283`; preprint HUTMP B147, as listed in the CMP99b references.
* T. Bałaban, *Propagators for lattice gauge theories in a background field*, CMP99 (1985),389–434, [publisher record](https://link.springer.com/article/10.1007/BF01240355), DOI10.1007/BF01240355; normal Euclid record `https://projecteuclid.org/euclid.cmp/1103942769`; preprint HUTMP-84/B153, as listed by INSPIRE.

On 16 October 2026 the publisher records were accessible as subscription previews, and the normal Euclid records were unavailable through the browser tool. The Rutgers records link only to the DOI. INSPIRE metadata provided no document URL, and the OpenAlex records provided no public PDF location. No restriction was bypassed. These access results do not establish that no public copy exists. The formulas examined above are the explicit transcriptions in the deposited raw account, not a newly verified reading of the original printed equations.

The next exact primary check is now narrow: CMP98 Proposition 6 and equations (159),(161),(163),(164), including locality, the amplitude norm at base 1, and the rescaling under which (2) holds; plus the definition and fixed-radius analyticity of the one-step corrected Q in CMP98(124). If these give the local amplitude version used at I:17806–17810, (15) proves the desired uniform complex averaging primitive on a common regular patch. Alternatively, verifying CMP99b(3.15)–(3.16)'s normalized measure and the full complex form of CMP98(139),(143) gives the direct constant 8d through §3.

Neither route by itself supplies the other four head terms, their sum over retained cubes, or the global four-layer current identity. It does replace an unspecified averaging “order” with an exact local operator obligation and a uniform composition proof.
