# Local measure factors in the exact current-step pivot chart

17 October 2026. This note uses the exact homogeneous current-step chart proved and independently audited in physical_current_pivot_precision_research.md. The current spacing is one, the next block side is a fixed odd L, and the preceding classical depth M and compatible periodic volume are arbitrary. This is an internal proof candidate. It does not localize the full classical action remainder or a previously integrated interaction.

## 1. Setup and the norm being proved

Write the relative ordinary constraint as

\[
 F_V(B)=A_VB+C_V(B),\qquad C_V(0)=DC_V(0)=0.
\]

Each coarse equation c reads exactly one pivot p(c). The pivot block

\[
 A_{c,p}=D_{B(p(c))}F_V(0;c)=L^{1-d}\pi_c(V)
\]

is invertible on a fixed small product domain of current link backgrounds V=exp(ia). Its inverse is the pivot insertion h_V(c). The retained-coordinate insertion K_V has A_VK_V=0 and is the identity on retained bonds. The full straightening and constrained chart are

\[
 \psi_V(B)=B-h_V\widetilde D_V(B),\qquad
 \widetilde D_V(B)=C_V(\psi_V(B)),\qquad
 \Phi_V(z)=\psi_V(K_Vz).
 \tag{1.1}
\]

Thus F_V(psi_V(B))=A_VB and every retained component of psi_V(B) equals that of B. The local implicit equation for output c contains no other unknown output. In particular the chart, its background dependence, and every derivative below have a fixed finite dependency neighborhood; an implicit iteration does not enlarge it indefinitely.

All Lie algebra coordinates are real coordinates orthonormal for normalized trace, then complexified. Let q be their fixed number per bond. Let D_b be a sufficiently small product domain in the independent current background coordinates a(b). Fix a slightly larger product domain on which all local maps in (1.1) exist. There are constants r_L,C_L,N_L,I_L,ell_L, independent of M and volume, with these properties:

* ||K_V||_{infinity to infinity} is at most C_L, and ||Phi_V(z)||_infinity is at most C_L||z||_infinity for ||z||_infinity<r_L.
* Each primitive term used below reads a fixed set Y_r of at most N_L current cells, with tree length at most ell_L; Y_r includes all current background and retained fluctuation coordinates it reads.
* At most I_L such primitive supports contain any one cell, with periodic multiplicities counted.

One can take fixed enlargements of the two-block neighborhoods for the chart and a block neighborhood for each contour. Color dimensions and the finite number of local geometric types are absorbed into these constants. We stay within the same compatible torus geometry as the pivot theorem.

For fixed nonnegative a_0,kappa define the local coefficient norm

\[
 \|l\|_{a_0,\kappa,R}
 =\sup_x\sum_{r:x\in Y_r}
 e^{a_0|Y_r|+\kappa\ell(Y_r)}
 \sup_{V\in D_b,\ \|z|_{Y_r}\|_\infty\le R}|l_r(V,z)|.
 \tag{1.2}
\]

The supremum may be over the complex fluctuation polydisc; hence the result also applies to the fixed real retained cutoff. The supports are labels fixed before choosing the fields. If desired, primitive terms with the same support are added; the norm only decreases by the triangle inequality. The elementary bound

\[
 \|l\|_{a_0,\kappa,R}
 \le I_L e^{a_0N_L+\kappa\ell_L}\sup_r\|l_r\|_\infty
 \tag{1.3}
\]

turns all subsequent local estimates into a genuine anchored interaction norm, with no volume factor.

## 2. The ambient straightening Jacobian

**Lemma 2.1.** For B in a fixed small complex polydisc,

\[
 \det D\psi_V(B)
 =\prod_c
 \frac{\det A_{c,p}}
 {\det D_{p(c)}F_V(\psi_V(B);c)}.
 \tag{2.1}
\]

Every ratio is analytic, equals one at B=0, and depends on a fixed local neighborhood. This is the determinant of the square ambient change of variables, not a determinant of the rectangular constrained-chart derivative D Phi.

**Proof.** Order the ambient variables as retained variables followed by pivots. The retained rows of D psi are [I,0]. Because the equation defining output c reads only the corresponding input pivot, the pivot-to-pivot block is block diagonal. Differentiate F_V(psi_V(B))=A_VB with respect to B(p(c)). The only output pivot entering F_c is p(c), giving

\[
 D_{p(c)}F_V(\psi_V(B);c)
 D_{B(p(c))}\psi_V(B)(p(c))=A_{c,p}.
 \tag{2.2}
\]

The determinant of a block triangular matrix is the product of its diagonal determinants; (2.1) follows. At zero, DF=A and D psi=I. All local matrices remain invertible after reducing the fixed domain. No commutativity of the color matrices is used. QED.

Define the normalized logarithm by its branch vanishing at B=0:

\[
 j^{\rm str}_c(V;B)
 =-\operatorname{Tr}_{\mathfrak g}\log\left[
 I+A_{c,p}^{-1}
 \{D_{p(c)}F_V(\psi_V(B);c)-A_{c,p}\}\right].
 \tag{2.3}
\]

The trace is the finite-dimensional matrix trace in color space, not the normalized trace of the gauge group representation. Formula (2.3) has exponential equal to the c factor in (2.1). Although the actual diagonal Jacobian block is (DF_p)^{-1}A_p, the determinant in (2.3) is equal to its determinant; matrix order has not been identified incorrectly.

For |g|R below a fixed L-dependent radius, put B=K_Vgz. Local analyticity and DF_p(0)=A_p give

\[
 \sup_c|j^{\rm str}_c(V;K_Vgz)|\le C_L|g|R,
 \qquad
 \|j^{\rm str}(V;K_Vgz)\|_{a_0,\kappa,R}
 \le C_{L,a_0,\kappa}|g|R.
 \tag{2.4}
\]

To see the first estimate directly, the matrix inside the logarithm differs from I by at most C_L|g|R. Choose the chart radius so this is at most 1/2 and sum the logarithm series. The local supports include the local insertion K_V; their size is still bounded at fixed L.

### 2.1 The background determinant is not discarded

For real backgrounds and a sufficiently small chart, all pivot determinants have the positive orientation of the flat block L^{1-d}I. In the Lie algebra delta convention, the exact constrained integral is locally

\[
 \int dX\,\delta(F_V(X))\,f(X)
 =\mathcal D(V)\int dz\,
 \exp\!\left(\sum_cj^{\rm str}_c(V;K_Vz)\right)
 f(\Phi_V(z)),\qquad
 \mathcal D(V)=\prod_c(\det A_{c,p})^{-1}.
 \tag{2.5}
\]

Here f is supported within the chart. First change X=psi_V(B), then solve A_VB=0 for pivots, leaving B=K_Vz. This proves (2.5), and also shows why the ambient Jacobian is the relevant one. Equivalently, the reduced density before this splitting is the product of inverse pivot derivatives DF_p at Phi_V(z).

A group delta at the identity differs from this convention only by its fixed exponential-coordinate normalization, since its argument is F=0; any source measure normalization must be carried consistently. After z is rescaled to gz for positive real g, the factor g^{number of retained real coordinates} is field independent. Neither of these constants changes (2.4).

The factor D(V) is independent of fluctuations but is not generally independent of the current background or the prescribed next-scale field. It must stay in the external normalization/background contribution. Its normalized logarithm

\[
 \log\frac{\mathcal D(V)}{\mathcal D(1)}
 =-\sum_c\operatorname{Tr}_{\mathfrak g}
     \log(A_{c,p}A_{1,c,p}^{-1})
 \tag{2.6}
\]

is itself a sum of local O(||a||_infinity) terms, but it has no small factor g. All identities for complex backgrounds mean their holomorphic continuations; a distributional complex delta is not being introduced.

## 3. Haar density in the relative exponential coordinates

Let j(X) be the pullback density of Haar measure under X maps to exp(iX), divided by its value at zero. In a neighborhood of zero it is a nonvanishing real analytic function with j(0)=1. Its analytic continuation has a unique logarithm vanishing at zero. Haar invariance under inversion gives j(-X)=j(X) on the real form, and then holomorphically. Consequently

\[
 \log j(0)=D\log j(0)=0,\qquad
 |\log j(X)|\le C|X|^2.
 \tag{3.1}
\]

This argument uses the positive density on the real form; the absolute orientation change under X maps to -X cancels the orientation of group inversion. It does not identify a nonanalytic absolute determinant with a complex analytic function. Equivalently, the ordinary analytic dexp determinant gives the same local branch.

Left or right translation by V preserves Haar measure for real V. Thus the relative link parametrization exp(iX)V has density j(X), with no further background factor. For complex V this is the continuation of that identity. The local Haar logarithms are therefore exactly

\[
 j^{\rm H}_b(V;gz)=\log j(\Phi_V(gz)(b)).
 \tag{3.2}
\]

For every retained bond the argument is exactly gz(b); for a pivot it is the local implicit function from (1.1). Equations (3.1) and the local chart bound imply

\[
 \|j^{\rm H}(V;gz)\|_{a_0,\kappa,R}
 \le C_{L,a_0,\kappa}|g|^2R^2.
 \tag{3.3}
\]

The constant normalization j(0) for each original bond, if not normalized away, is independent of V and of the fluctuation and stays outside the interaction. The quadratic Haar term is generally present and is suppressed by g^2 after scaling; it is not claimed to vanish.

## 4. The exponential-gauge remainder is exactly retained-local

Index the source contour penalty by r=(y,x), x not equal to y, and write

\[
 f_r(V;z)=1-\tfrac12\tau\left[
 P_{e^{i\Phi_V(z)}V}(y,x)
 +P_{e^{i\Phi_V(z)}V}(y,x)^{-1}\right].
 \tag{4.1}
\]

Every root-to-site contour lies within its block and reads no pivot. Since the chart fixes retained coordinates,

\[
 f_r(V;z)=1-\tfrac12\tau\left[
 P_{e^{iE_fz}V}(y,x)+P_{e^{iE_fz}V}(y,x)^{-1}\right],
 \tag{4.2}
\]

where E_f inserts zero on pivots. Thus this identity holds exactly, not just to a finite order. The gauge remainder has no hidden dependence on eliminated fluctuation coordinates.

On the full small background product domain define

\[
 v^{\rm G}_r(V;g,z)=-g^{-2}\left[
 f_r(V;gz)-f_r(V;0)-gD_zf_r(V;0)z
 -\tfrac12g^2D_z^2f_r(V;0)[z,z]\right].
 \tag{4.3}
\]

The singularity at g=0 is removable; its value there is zero. Uniform local Taylor estimates give

\[
 \|v^{\rm G}(V;g,z)\|_{a_0,\kappa,R}
 \le C_{L,a_0,\kappa}|g|R^3
 \quad\hbox{when }|g|R<r_L.
 \tag{4.4}
\]

At a physical background P_V(y,x)=1, f_r(V;0)=D_zf_r(V;0)=0. Therefore (4.3) is precisely the logarithmic interaction left from exp(-g^{-2}G) after extracting its quadratic precision. At other backgrounds it is the exact third-and-higher remainder after also separating the constant and linear terms. Keeping this full-domain definition supplies local background holomorphy without pretending the condition P_V=1 defines a product domain.

## 5. Coefficients, multipliers, and application to a marked theorem

All three logarithmic interactions have convergent expansions in g on |g|R<r_L:

\[
 \begin{split}
 j^{\rm str}_c(V;K_Vgz)&=\sum_{n\ge1}g^n s_{c,n}(V;z),\\
 j^{\rm H}_b(V;gz)&=\sum_{n\ge2}g^n h_{b,n}(V;z),\\
 v^{\rm G}_r(V;g,z)&=\sum_{n\ge3}g^{n-2}v_{r,n}(V;z).
 \end{split}\tag{5.1}
\]

The displayed coefficients are homogeneous of degree n in the retained variable z, and depend holomorphically only on the background coordinates in their fixed supports. Cauchy in a local fluctuation disc of fixed radius gives constants C_0,C_1, depending on L and the interaction weights but not M or volume, such that their norm as in (1.2) is at most C_0(C_1R)^n. A smaller fixed background domain gives the corresponding background Cauchy estimates, still with the same support. This proves local coefficient bounds, not only an extensive bound for their sum.

Regroup primitive terms by their finite supports Y and put

\[
 v_Y=j_Y^{\rm str}+j_Y^{\rm H}+v_Y^{\rm G}.
\]

For small |g|R,

\[
 \sup_x\sum_{Y\ni x}e^{a_0|Y|+\kappa\ell(Y)}
 \sup|v_Y|
 \le C_{L,a_0,\kappa}
   (|g|R+|g|^2R^2+|g|R^3).
 \tag{5.2}
\]

If the right side is at most one, |e^{v_Y}-1| is at most e|v_Y|. Hence the same weighted estimate, with an extra factor e, holds for the multiplier smallness used in the overlapping-interaction theorem. For R at least one and |g|R at most one, it is bounded by C|g|R^3. At fixed L the support-cardinality factor K^{|Y|} of that theorem is absorbed by increasing a_0 by log K, since |Y| is uniformly bounded. This observation does not assert that the constants remain favorable if L or the cell dimension is simultaneously taken large.

The theorem's cutoff is the fixed retained window ||z(b)||<R. It is unchanged because Phi_V(gz)(b)=gz(b) on every retained bond. Any additional pivot, contour, or reconstructed-field indicator remains at its exact pullback and is not covered by (5.2). In particular, analyticity of the chart alone would not justify deleting such an indicator.

## 6. Exact scope and source references

This proves the local Haar, normalized straightening-Jacobian, and exponential-gauge higher-order interactions for the actual one-step chart, uniformly in preceding homogeneous classical depth. The factors are local as functions of independent current link backgrounds V. Substituting the minimizing background V_*(W) does not make them strictly finite-support functions of W. No support-valued decomposition of the full precision in W is implied.

The full classical action remainder and the previously integrated interaction need their own localization and smallness arguments; they have not been replaced by these measure terms. The background-only factor (2.5), any source delta normalization, and any extra sharp cutoff factors are retained explicitly.

Primary locations: CMP109, Part I, DOI 10.1007/BF01215223, journal pp.266–268, (2.5), (2.9)–(2.13), introduces the gauge Taylor expansion and pivot straightening; the local determinant identity above is derived directly from that chart. CMP116, Part II, DOI 10.1007/BF01239022, p.12 immediately before (2.3), explicitly defines the retained-bond cutoff set. Its (2.14), p.15, keeps that real cutoff fixed while deforming the Gaussian. The precise product subscript in the accessible CMP109 (2.9) OCR is not readable and has not been claimed as a visual verification; see pivot_cutoff_source_research.md for that limited source issue.
