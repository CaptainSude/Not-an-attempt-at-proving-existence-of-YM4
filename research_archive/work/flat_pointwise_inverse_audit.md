# Independent audit of the full flat pointwise inverse

16 October 2026. Root independently checked the complete saved argument in
flat_pointwise_inverse_research.md against the passed full inverse formulas.
The pointwise theorem and the endpoint counterexample pass. One explanatory
wording correction is recorded below; it does not alter the estimates.

The cooperative difference system for q_n=p_s(n)-p_s(n+1) has the correct
boundary equation q_0'=q_1-3q_0. Its nonnegative bounded generator after a
scalar shift proves unimodality. The weighted variation identity (3.3) is
exact: negative n=-m-1 contributes exp(r(m+1)) q_m, and summation by parts
on m>=0 gives the stated p_s(0) and (1-exp(-r)) remainder. Scaling time
by M^2 and the weight by 1/M gives the required physical first-derivative
bound, including times below M^-2. Semigroup convolution supplies the
second derivative with the same submultiplicative exponential weight.

The complex image sum uses exp(-iz.k), consistent with quasiperiodic
boundary condition f(s+M)=exp(iz)f(s). Summing absolute rows is controlled
by the infinite weighted heat kernel, with no fine-dimensional factor.
The gradient difference estimate is the minimum of Ct^-1/2 and
C|x-y|t^-1. Its interpolation integrates exactly for alpha<1. The central
mode subtraction is bounded at small times; the high-alias real-part gap
controls the long-time integral uniformly in M. The enlarged charts and
fixed output collars justify the same argument for Bloch symbols.

The rank corrections have output alias weights omega/P and beta, and
their (1+|r|)^(1+alpha)-weighted absolute sums converge by the dyadic
product-weight shell bound. Their input rows use physical cell L2<=L∞,
not an unnormalized counting norm. The componentwise Laplacian requires
the physical Q* profile, whose two positive weights sum to one; summing
absolute aliases instead would introduce a false logarithmic loss.
The remaining Laplacian beta term has summable w(r)/|r| weight.

Only the full reconstructed symbol is used for periodic gluing; its
separated central/high pieces need not be periodic. Operator-valued
contour estimates hold in the discrete Hölder output norm on fixed
collars, uniformly in its growing finite dimension. Exact periodization
then gives compatible torus bounds.

Wording repair in Section 7: the fine precision includes nonlocal R, so
the extension of the inverse identity to bounded forcing should cite
absolute convergence of exponentially summable operator products at each
fixed M, rather than call every operation local. The scalar identity
R=L Z L and the already proved four-derivative cell bounds for Z give
weighted cell locality of R. At each fixed M, cell norm equivalence is
finite; it suffices for the inverse identity, while the pointwise G0
bound itself remains uniform by the direct proof above.

The endpoint example is valid in every d>=2. On a single coarse cell
torus the actual fine source inverse is the scalar Laplacian inverse on
every nonconstant alias. The compactly supported function
u_epsilon=chi*x1*x2*log(|x|^2+epsilon^2)/2 has uniformly bounded
continuum Laplacian, whereas its mixed second derivative at zero is
log(epsilon). For each fixed epsilon, fine odd-grid sampling and then
M sufficiently large preserve the Laplacian bound and mixed-difference
limit. Removing the exact discrete mean makes the inverse identity
exact. Choosing epsilon first and M second proves failure of a uniform
endpoint estimate. It does not contradict the bounded Laplacian sum.

The theorem is confined to the homogeneous matched flat operator, fixed
positive penalty interval, and compatible periodic/infinite geometries.
It does not prove arbitrary nonflat or retained-history source estimates.
