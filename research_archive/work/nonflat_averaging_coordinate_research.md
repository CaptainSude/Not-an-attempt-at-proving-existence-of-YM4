# Exact derivative conversion: fixed-reference corrected average versus moving-reference Q

16 October 2026. Research calculation, passed by a separate internal audit recorded in `nonflat_averaging_coordinate_audit.md`; no external certification is claimed. This note derives the additional endpoint term in the change of reference. It is not legitimate to rename the derivative in `flat_nonlinear_average_research.md` as the source Q(V). All identities below are local one-step identities, on the common identity logarithm branch. The geometric ratio L is fixed. Source identifications are at the pinned deposited-transcription level, not a new verification of the full original CMP98 article.

## 1. The deposited identities and the two references

Raw I:46952--46970 defines the ordinary group average M and the two left-increment maps

\[
 \Phi^g(V,B;y,x)=\frac1i\log[(e^{iB}V)\langle y,x\rangle
                                         V\langle y,x\rangle^{-1}],
\]
\[
 \Phi^\flat(V,B;c)=\frac1i\log[M(e^{iB}V)(c)M(V)(c)^{-1}].
 \tag{1.1}
\]

At I:47076--47087, explicitly incorporating CMP98 (120), the middle corrected logarithm Q obeys

\[
 e^{i\Phi^\flat(V,B;c)}=g_{c_-}^{V}(e^{iB}V)
       e^{i\mathcal Q(V,B;c)}
       [\operatorname{Ad}_{M(V)(c)}g_{c_+}^{V}(e^{iB}V)]^{-1},
 \tag{1.2}
\]

where, for any U near V,

\[
 g_y^V(U)=\exp\left(i\sum_{x\in B(y)}L^{-d}
       \frac1i\log[U\langle y,x\rangle V\langle y,x\rangle^{-1}]
                      \right).
 \tag{1.3}
\]

The logarithmic/linear split I:24344--24349 is

\[
 \mathcal Q(V,B)=LQ(V)B+O(B^2).
 \tag{1.4}
\]

Here the identification of the middle coordinate in (1.2) with (1.4) is exactly the deposited bridge's assertion that the displays incorporate (120); the earlier local transcription explicitly does not reproduce (120) at I:24346--24347. We use this stated bridge, not an invented expression for its omitted V1. Formula (1.2) itself defines an unambiguous corrected left-increment map from the explicitly defined Phi maps.

To keep its reference visible, define the group-valued corrected increment

\[
 C_V(U)(c):=g_{c_-}^V(U)^{-1}M(U)(c)g_{c_+}^V(U)M(V)(c)^{-1}.
 \tag{1.5}
\]

Then `C_V(V)=1` and `C_V(e^{iB}V)=exp(i mathcal Q(V,B))`. In contrast the fixed identity-reference map used by the nonlinear chart is

\[
 C_1(U)(c)=a_{c_-}(U)^{-1}M(U)(c)a_{c_+}(U),
 \qquad a_y(U):=g_y^1(U),
 \tag{1.6}
\]

using `M(1)=1`. In general C_1(V) is not the identity. The full corrected identity-reference iterate composes (1.6), whereas the source linear products use the moving-reference differentials (1.4) at ordinary averaged reference backgrounds; see I:24320--24325 and I:47046--47048. These are distinct statements.

## 2. Exact group identity for the change of reference

For fixed V and U near V put

\[
 k_y(U;V)=g_y^V(U)^{-1}a_y(U)a_y(V)^{-1}.
 \tag{2.1}
\]

It equals the identity at U=V. Direct multiplication in (1.5)--(1.6) gives

\[
 \begin{aligned}
 C_1(U)(c)C_1(V)(c)^{-1}
 =\operatorname{Ad}_{a_{c_-}(V)^{-1}}
 \left[k_{c_-}(U;V)^{-1}\,C_V(U)(c)\,
       \operatorname{Ad}_{M(V)(c)}k_{c_+}(U;V)\right].
 \end{aligned}                                                    \tag{2.2}
\]

For example solve (1.5) for M(U), substitute into (1.6), and cancel adjacent factors. This verifies the noncommutative order; no cocycle property of a or g is assumed.

Let `U(s)=exp(i sB)V`. Define the two endpoint left derivatives and their difference by

\[
 \eta_y^1(V;B)=\frac1i\left.\frac d{ds}\right|_0
                               a_y(U(s))a_y(V)^{-1},
 \qquad
 \eta_y^V(B)=\frac1i\left.\frac d{ds}\right|_0g_y^V(U(s)),
\]
\[
 Z_VB(y)=\eta_y^1(V;B)-\eta_y^V(B).
 \tag{2.3}
\]

Differentiating (2.2), all middle factors being the identity at s=0, yields the exact formula

\[
 \frac1i\left.\frac d{ds}\right|_0
 C_1(e^{isB}V)(c)C_1(V)(c)^{-1}
 =\operatorname{Ad}_{a_{c_-}(V)^{-1}}
       \left[LQ(V)B(c)-d_{M(V)}(Z_VB)(c)\right],
 \tag{2.4}
\]

where the unscaled endpoint difference is explicitly

\[
 d_W z(c):=z(c_-)-\operatorname{Ad}_{W(c)}z(c_+).
 \tag{2.5}
\]

This definition fixes its sign; it is not silently identified with a source convention for the covariant derivative D. The extra term in (2.4) disappears at V=1 but need not disappear away from the identity.

There is a useful independent consistency check involving the later rooted linear operator. Raw I:46977 defines `L Q^flat(V)B=Phi_1^flat(V;B)`. Differentiating (1.2) directly at B=0, without changing the reference, gives

\[
 LQ(V)B=LQ^\flat(V)B-d_{M(V)}\overline r(V;B),
 \qquad \overline r(V;B)(y)=\sum_xL^{-d}r_x(V;B).
 \tag{2.6}
\]

Thus the rooted one-step Q^flat and corrected one-step Q are not interchangeable either. Substituting (2.6) and `Z_V=eta^1-overline r` into (2.4) reduces it to the direct derivative of (1.6), confirming both signs independently.

## 3. The endpoint term in logarithm Jacobians

For a small complex Lie-algebra element X let

\[
 \mathcal J_X K=\int_0^1\operatorname{Ad}_{e^{itX}}K\,dt.
 \tag{3.1}
\]

It satisfies

\[
 \frac1i\left.\frac d{ds}\right|_0e^{i(X+sK)}e^{-iX}
          =\mathcal J_XK.
 \tag{3.2}
\]

On a fixed sufficiently small complex ball, J_X is analytic and invertible, `||J_X-I||+||J_X^{-1}-I||<=C||X||`. These statements follow directly from the integral power series and a Neumann series. No unitarity is used.

Write

\[
 P_x=V\langle y,x\rangle=e^{iY_x},\qquad
 \overline Y_y=\sum_xL^{-d}Y_x,
 \qquad
 r_x(V;B)=\Phi_1^g(V;B;y,x).
\]

The explicitly defined contour variation r_x includes every transport, orientation sign and repeated occurrence in the contour. Applying (3.2) first to each logarithm and then to their exponential mean proves

\[
 \boxed{\quad
 Z_VB(y)=\mathcal J_{\overline Y_y}
           \sum_xL^{-d}\mathcal J_{Y_x}^{-1}r_x(V;B)
             -\sum_xL^{-d}r_x(V;B).\quad}
 \tag{3.3}
\]

This is an explicit operator formula, not an unnamed error term. At V=1 all Y's vanish, so Z_1=0.

It also exposes why a multiplicative endpoint cocycle cannot simply be assumed. To first order in the background contour logarithms,

\[
 Z_VB=\frac i2\left(
       [\overline Y,\overline r]-\sum_xL^{-d}[Y_x,r_x]\right)
       +O\left((\max_x|Y_x|)^2\max_x|r_x|\right).
 \tag{3.4}
\]

An abstract two-contour mean with equal weights, Y_1=Y, Y_2=-Y and r_1=B, r_2=-B has first-order term `-(i/2)[Y,B]`. This is a diagnostic for the failure of the proposed mean cocycle, not a claim that these independently assigned contour data automatically come from a particular lattice configuration. The exact formula (3.3), which uses the actual contour variations, is the applicable statement.

## 4. Physical potential coordinates: the exact derivative conversion

At fine spacing h, let `V=exp(i hA)` and define the fixed-reference physical average by

\[
 C_1(e^{ihA})(c)=e^{iLh\mathcal F_h(A)(c)}.
\]

The logarithm branches and h-scaling are those already established in the nonlinear-average note. For an ordinary potential variation K, the fine left increment is `h J_{hA}K`, while the coarse left increment is `Lh J_{Lh mathcal F_h(A)}D mathcal F_h(A)K`. Substitute these in (2.4). With the endpoint adjoint acting bondwise at c_-, the result is

\[
 \boxed{\quad
 Q_h(V)=\operatorname{Ad}_{a_-(V)}
    \mathcal J_{Lh\mathcal F_h(A)}
    D\mathcal F_h(A)\mathcal J_{hA}^{-1}
       +\frac1L d_{M(V)}Z_V.
       \quad}                                             \tag{4.1}
\]

Here Q_h(V) is the same normalized one-step coefficient Q(V), placed between the physical spaces of spacings h and Lh. Z_V is the linear coefficient map (3.3) and can act on a physical field because it is linear. In the substitution its argument is h times that physical field; this cancels h in the coarse factor Lh and leaves exactly 1/L. The last term in (4.1) has no extra power h and no inverse power h. Its smallness comes instead from Z_V=O(h||A||), established below.

For clarity one may verify (4.1) before rearranging:

\[
 \mathcal J_{Lh\mathcal F_h(A)}D\mathcal F_h(A)K
 =\operatorname{Ad}_{a_-(V)^{-1}}
   \left[Q_h(V)\mathcal J_{hA}K
     -L^{-1}d_{M(V)}Z_V(\mathcal J_{hA}K)\right].
 \tag{4.2}
\]

This fixes both the endpoint sign and the multiplication order. In particular an exponential-coordinate Jacobian alone does not perform the change of reference.

## 5. A rigorous one-step perturbation bound in the actual source norm

For fixed L, all paths in (1.3) have bounded finite length. If `||A||_infinity<=a` and h a is sufficiently small (depending on L), then

\[
 \max_x|Y_x|+|\overline Y_y|\le C_L h a,
 \qquad \|r_x(V;\cdot)\|_{\infty\to\mathrm{color}}\le C_L.
 \tag{5.1}
\]

Products of nonunitary complex transports are bounded by exponentials of a fixed contour length times h a. Their derivatives remain bounded finite sums of such products. Equations (3.3) and (3.1) therefore imply

\[
 \|Z_V\|_{\infty\to\infty}\le C_L h a.
 \tag{5.2}
\]

The same conclusion holds from fine physical L2 to coarse-site physical L2. To see it without a path-trace assumption at a macroscopic scale, expand Z_V into its finitely many one-step bond coefficients. Each coefficient vanishes at V=1 and is bounded by `C_L h a`; each row and column has a bounded fixed-L incidence. Multiply its column sum by the physical volume ratio L^d and apply the weighted Schur bound. Thus

\[
 \|Z_V\|_{2,h\to2,Lh}\le C_L' h a.            \tag{5.3}
\]

The constants absorb finite one-step paths only and are independent of h, refinement and compatible volume. Multiplicity counting handles short tori. The endpoint map d_{M(V)} is uniformly bounded on the coarse site/bond L2 and bounded-field spaces since it has two entries per row, fixed incidence, and bounded complex adjoints. Also

\[
 \|\operatorname{Ad}_{a_-(V)}-I\|
 +\|\mathcal J_{Lh\mathcal F_h(A)}-I\|
 +\|\mathcal J_{hA}^{-1}-I\|\le C_L h a.
\]

Combine these facts with the one-step bound
`||D mathcal F_h(A)-Q_h(1)||_{p->p}<=D_p h a` and the flat contractions. Formula (4.1) proves the actual one-step source comparison

\[
 \boxed{\quad
 \|Q_h(e^{ihA})-Q_h(1)\|_{p,h\to p,Lh}
        \le C_{L,p}h\|A\|_\infty,
        \qquad p=2,\infty.
 \quad}                                               \tag{5.4}
\]

This is a conclusion of the coordinate calculation, rather than an equality assumption. It also follows from finite local analyticity of the corrected family in (1.2); (4.1) records explicitly which coordinate factors that shorter argument would hide. A smaller common complex ball makes all constants uniform. Higher bounded background derivatives follow by ordinary local Cauchy estimates in hA, with the corresponding powers h^n.

## 6. What is still needed for a multilevel source comparison

The source products at I:47046--47048 evaluate their one-step coefficients at the ordinary averaged reference backgrounds, not at the fields produced by the fixed-reference corrected iteration. Therefore (5.4) may only be multiplied across levels once those actual backgrounds have the form

\[
 V_t=M^t(U)=e^{ih_t A_t^{\mathrm{ord}}},\qquad
 \sup_t\|A_t^{\mathrm{ord}}\|_\infty\le C a,
 \qquad h_t=L^{t-j}.
 \tag{6.1}
\]

Under (6.1) the ordered product comparison is immediate and quantitative:

\[
 \|Q_j(U)-Q_M^{\mathrm{st}}\|_{p\to p}
   \le\prod_{t<j}(1+C_{L,p}C a h_t)-1
   \le e^{C_{L,p}C a/(L-1)}-1.
 \tag{6.2}
\]

Finite physical reading range turns this into a weighted physical-cell Hilbert bound. Equation (6.1) is a separate ordinary-reference trajectory statement, not a consequence of replacing the two kinds of average by one another. It has now been supplied in `nonflat_reference_averages_research.md` and passed the independent audit `nonflat_reference_averages_audit.md`: ordinary gauge covariance and `V_t=g_t C_t g_t^{-1}` give exactly `g_{t+1}=g_t|_{coarse} a(C_t)`. Each a(C_t)-1 is O(h_t a), and the geometric partial sum is O(h_t), so the accumulated gauge and the ordinary bond logarithm are O(h_t a). Thus the input (6.1), and consequently (6.2), are now established within the stated homogeneous globally bounded-potential setting and deposited source conventions. The companion note proves the stronger absolute row/physical-adjoint-row version as well.

The result proved here is the exact change-of-reference identity, its explicit endpoint operator, and the uniform one-step bound (5.4). It neither identifies the nonlinear constraint chart with a true nonflat action minimizer nor supplies nonflat inverse stability. Those require additional equations beyond this averaging-coordinate calculation.
