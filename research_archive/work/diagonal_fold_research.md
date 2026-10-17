# Normalized Wilson diagonal slabs and two-frame folds

Research derivation, 16 October 2026. This note proves the diagonal boundary representation and the resulting finite-volume fold inequalities, using the separately established coordinate mixed-boundary representation for the second frame. It does not prove an entire Yang--Mills construction. Every statement is at a fixed positive lattice coupling.

## 1. Finite graph and normalization

Let G=SU(N), with normalized Haar measure, and let each unoriented elementary plaquette occur once in the Wilson weight

\[
 Z_\Gamma[F]=\int F(U)\prod_p
       \exp\{c_\beta\,\operatorname{ReTr}U_p\}\prod_{e}dU_e,
 \qquad c_\beta=\beta/N>0.                              \tag{1}
\]

The integrations use one chosen orientation for each link. Reversing a link changes its matrix to its inverse. Reversing a plaquette orientation does not change its real trace. A different convention that also includes exp(-beta) per plaquette is handled by assigning that constant to the same plaquette pieces below.

The lattice is Z^4 modulo an integer period lattice Gamma. Assume its shortest nonzero period in the sup norm is at least four, so the elementary cells have no short-period degeneracies. All tori used below satisfy this for sufficiently large volumes. No gauge fixing is performed in the diagonal construction.

We consider the two diagonal heights s_-=x_1-x_2 and s_+=x_1+x_2. Fix one, write s(x)=v dot x with |v|^2=2, and let Gamma_parallel be a rank-three integer period lattice inside s=0. Work on the cylinder Z^4/Gamma_parallel, whose bounded height slabs are finite. All diagonal mirrors s=c occur at integer c.

The diagonal results below apply to bounded measurable slab integrands for SU(N). For the coordinate physical-space representation used later, use SU(2), the group established in the companion transfer note, and gauge-invariant integrands. The source and operator integrands in the intended same-limit application have these properties.

## 2. Exact classification of cells at a diagonal mirror

First take s=x_1-x_2 and an integer mirror s=c.

* A link in direction 1 or 2 has endpoint heights differing by one, so the mirror never cuts its relative interior. It may end on the mirror.
* Links in directions 3 and 4 either lie entirely in the mirror or are disjoint from it.
* A (1,2)-plaquette based at height b has vertex heights b,b+1,b-1,b. It crosses the mirror through its relative interior exactly when b=c. The mirror joins its two height-c vertices, splitting the square into two paths of two links each.
* A (1,mu) or (2,mu)-plaquette, mu=3,4, has height range of length one. It can touch an integer mirror but cannot have vertices on both strict sides. Unless contained in a mirror, it belongs wholly to a single adjacent slab.
* A (3,4)-plaquette has constant height. If that height is c, it lies wholly in the mirror; otherwise it is a slab-interior plaquette.

For s=x_1+x_2 the same classification holds, except that a (1,2)-plaquette based at height b crosses the mirror at c=b+1, through its other diagonal. Its two paths again connect two fixed boundary vertices.

Choose all slab widths at least four; the application has much larger widths. For a chain of such mirrors, every link is either on one mirror or in exactly one open slab. Every plaquette is of exactly one of the following types:

1. wholly on one mirror;
2. strictly crossing one mirror, with one two-link path in each adjacent slab;
3. wholly assigned to one slab, possibly touching a boundary but neither lying in it nor crossing it.

In particular, a plaquette which only touches a mirror is not split. These rules are the graph-identification input to the kernel construction.

## 3. A concrete feature space for a split plaquette

Identify a complex N by N matrix A with its real vector u(A) of real and imaginary entries. Then

\[
 u(A)\cdot u(B)=\operatorname{ReTr}(AB^\dagger),
 \qquad |u(A)|^2=N\quad(A\in SU(N)).
\]

Let D=2N^2 and define a real feature vector in ell^2(N^D) by

\[
 \Phi_\alpha(A)
   =\left(\frac{c_\beta^{|\alpha|}}{\alpha!}\right)^{1/2}
                           u(A)^\alpha,\qquad
 \alpha\in\mathbb N^D.
\]

It obeys

\[
 \langle\Phi(B),\Phi(A)\rangle
       =e^{c_\beta\operatorname{ReTr}(AB^\dagger)},\qquad
 \|\Phi(A)\|^2=e^{c_\beta N}=e^\beta.                    \tag{2}
\]

All feature coefficients are real. Absolute convergence of every inner product follows from Cauchy--Schwarz and the constant norm.

For a split plaquette choose both paths from the same boundary vertex to the other, and let A_+,A_- be their ordered parallel transports. Its Wilson factor is exactly

\[
 e^{c_\beta\operatorname{ReTr}(A_+A_-^\dagger)}
    =\langle\Phi(A_-),\Phi(A_+)\rangle.                  \tag{3}
\]

For the minus mirror the paths may be chosen from x to x+e_1+e_2:

\[
 A_+=U_1(x)U_2(x+e_1),\qquad
 A_-=U_2(x)U_1(x+e_2).
\]

The diagonal reflection exchanges these paths and fixes their endpoints. For a plus mirror, take the endpoints x+e_1,x+e_2 and use the paths through x+e_1+e_2 and through x, respectively. The same property holds. Translation preserves these path conventions.

The complexification of the feature Hilbert space will be denoted F. Endpoint gauge transformations act orthogonally on the real matrix space and hence unitarily on its symmetric tensor feature space. This observation supplies gauge covariance if needed; no gauge quotient is needed for the identities below.

## 4. Boundary Hilbert spaces and the slab operator

At s=c let E_c be the transverse links lying wholly on the mirror, P_c^0 the plaquettes lying wholly on it, and P_c^x the split plaquettes centered on it, all taken modulo Gamma_parallel. Define

\[
 {\cal H}_c=
 L^2(G^{E_c},db)\ \widehat\otimes\
                 \bigotimes_{p\in P_c^x}{\cal F}_p.     \tag{4}
\]

There are finitely many factors. Set

\[
 W_c(b)=\prod_{p\in P_c^0}
                    e^{c_\beta\,\operatorname{ReTr}U_p(b)}.
\]

For a slab c_0<s<c_1, integrate all links assigned to that slab with normalized Haar measure. Keep the boundary links b_0,b_1 as kernel variables, and let alpha_0,alpha_1 denote the boundary feature indices. For a bounded slab function F, define S[F]:H_(c_0)->H_(c_1) by the kernel

\[
 \begin{split}
 S[F](b_1,\alpha_1;b_0,\alpha_0)
 ={}&W_{c_1}(b_1)^{1/2}W_{c_0}(b_0)^{1/2}\\
 &\times\int F(U)
       \prod_{\text{plaquettes assigned to the slab}}
                      e^{c_\beta\operatorname{ReTr}U_p}
       \prod_{p\in P_{c_1}^x}\Phi_{\alpha_{1,p}}(A_{p,\rm in})
       \prod_{p\in P_{c_0}^x}\Phi_{\alpha_{0,p}}(A_{p,\rm in})
       \prod_{e\ {\rm slab}}dU_e .
 \end{split}                                                   \tag{5}
\]

The inside path A_(p,in) is the half-plaquette path lying in this slab. The two boundary square roots assign half the weight of each sheet-contained plaquette to each adjacent slab.

The operator is Hilbert--Schmidt. To prove this directly, regard the integrand as a vector in the tensor product of all boundary feature spaces. Its feature norm is constant, by (2). All Wilson factors and boundary square roots are bounded on a finite product of compact groups, and F is bounded. Minkowski's inequality bounds the L^2 norm in b_0,b_1 and all feature indices by a finite constant times ||F||_infinity. All Haar spaces have mass one. This proof requires no positivity assumption about F.

## 5. Exact gluing, reflection, and the torus trace

### 5.1 Gluing two adjacent slabs

For bounded F_1,F_2 in adjacent slabs,

\[
 S[F_2]\,S[F_1]=S[F_1F_2]                               \tag{6}
\]

where the right side denotes the operator for their combined slab.

Indeed, kernel composition integrates the shared boundary link variables once and sums its feature indices. Each feature contraction gives exactly the missing full crossing-plaquette factor (3). The two square roots of W at that sheet multiply to W. Every other plaquette was already assigned to one of the two slabs and stays there. The link sets of the slabs, together with the shared boundary links, partition the combined slab links. Thus every link is integrated once and every plaquette has exactly one whole Wilson factor.

All changes of integration and summation are justified by the constant feature norms and bounded finite-volume weights. No gauge fixing, division by a gauge group, or extra gauge-volume factor appears.

### 5.2 Reflection is the adjoint

Let theta be reflection in the upper mirror c_1. It maps the slab [c_0,c_1] to [c_1,c_2], c_2=2c_1-c_0. On the lower mirror it agrees with translation by

\[
 q=\frac{2(c_1-c_0)}{|v|^2}v=(c_1-c_0)v\in\mathbb Z^4.
\]

Let U_q:H_(c_0)->H_(c_2) be the unitary induced by this translation, and put Theta F=overline{F composed with theta}. The exact relation is

\[
 S[\Theta F]=U_q\,S[F]^*.                              \tag{7}
\]

Reflection preserves Haar measures, exchanges the inside half paths while fixing the boundary endpoints, and reverses the order of the boundary arguments. The feature coefficients are real. The boundary halfweights are transported unchanged. These facts prove (7) directly from (5).

An odd integer slab width causes no problem. The two boundary lattices may have different tangential parity, but (5) is an operator between the two spaces; it does not identify them by a nonlattice normal half-translation. Only the paired translation q above is used, and it is integral.

### 5.3 Closing a possibly sheared torus

Suppose

\[
 \Gamma=\Gamma_\parallel\oplus\mathbb Z\gamma,
 \qquad s(\gamma)=p>0.
\]

Partition [c_0,c_0+p] into slabs with admissible mirrors and let S_j be their operators. Translation gamma gives a unitary U_gamma from H_(c_0) to H_(c_0+p). Then

\[
 Z_\Gamma[F_1\cdots F_J]
   =\operatorname{Tr}_{{\cal H}_{c_0}}
                    (U_\gamma^{-1}S_J\cdots S_1).       \tag{8}
\]

This is a cyclic version of the same graph gluing. The trace identifies the last boundary links and features with their period translates at the first boundary. It integrates each boundary link once, contracts each seam feature to one Wilson plaquette, and multiplies each pair of seam halfweights to the whole sheet weight. The sheared identification is exactly the original period gamma. Products of at least two Hilbert--Schmidt operators are trace class, and the explicit bounded-kernel/feature estimates justify the cyclic integral.

If the pure normal closing vector

\[
 \gamma_0=\frac p{|v|^2}v=\frac p2v
\]

is integral, then gamma-gamma_0 is an integer tangential translation. It is the unitary closing twist in (8) after using gamma_0 to identify the endpoint spaces. The absolute trace bound is unaffected by that unitary.

## 6. One-axis reflected folding

Assume p=Jb with J even, b an integer at least four, and let c_j=c_0+jb. The straightened period lattice is

\[
 \Gamma_0=\Gamma_\parallel\oplus\mathbb Z\gamma_0,
 \qquad \gamma_0=(p/2)v .
\]

For a function F in one slab, successively reflect it across its bounding mirrors to fill all J slabs. Denote the resulting product by Fold_s F. Then

\[
 Z_{\Gamma_0}[\operatorname{Fold}_s F]
        =\|S[F]\|_J^J\ge0.                             \tag{9}
\]

Work at the actual starting boundary; no translation to a reference boundary is needed. Put Y=S[F] and q=bv. The first reflected pair has product U_qY*Y by (7). The next pair is its translate by the integral lattice vector q. Multiplication of J/2 pairs telescopes to

\[
 U_{(J/2)q}(Y^*Y)^{J/2}.
\]

Since (J/2)q=gamma_0, the closing unitary in (8) cancels it. This gives Tr(Y*Y)^(J/2), proving (9).

For arbitrary bounded functions F_j in the J original slabs,

\[
 |Z_\Gamma[F_1\cdots F_J]|
 \le\prod_{j=1}^J
      Z_{\Gamma_0}[\operatorname{Fold}_s F_j]^{1/J}.     \tag{10}
\]

Apply Schatten Holder to (8), with exponent J for every slab, absorbing the unitary into an endpoint factor. The inequality also holds for different boundary Hilbert spaces, by placing them in an orthogonal direct sum and taking the cyclic block. Equation (9) identifies the factors.

No partition function has been normalized away in (9)--(10). They are identities and inequalities for (1).

## 7. Coordinate folds and the oblique closing identification

For coordinate directions use the independently derived physical-space representation in work/transfer_schatten_research.tex. Its positive electric convolution C, spatial multiplier V, gauge projection P and halfstep

\[
 B=V^{1/2}C^{1/2}
\]

give link-to-site and site-to-link halfsteps B and B*. Adjacent boundary factors glue to C or V, and temporal Haar integration produces P with no gauge-volume factor.

The same representation is defined for an arbitrary bounded complex gauge-invariant slab function F. One can obtain it by linearity from positive bounded slab functions: a bounded real function is a difference of two strictly positive bounded functions, each an exponential of a bounded real function; then split real and imaginary parts. The path-kernel definition is linear. Reflection takes the adjoint, and gluing inserts the product of the functions. Hilbert--Schmidt membership follows either by this decomposition or by the reflected two-slab bound.

Consequently the coordinate analogues of (8)--(10) hold for coordinate widths b in (1/2)N, with J even and Jb integral, including alternating site/link boundaries. The even-copy gluing uses a whole number of ordinary lattice time steps. It does not assume a pointwise-positive kernel for C^(1/2).

The only nonrectangular coordinate cylinder needed here is D_n, with

\[
 \Gamma_D=\langle a(1,-1),\,2a(1,1),\,n e_3,\,n e_4\rangle,
 \qquad n=2a.
\]

For the first coordinate direction, its height period is a and its spatial cross-section is

\[
 \Gamma_\parallel=\langle4a e_2,n e_3,n e_4\rangle.
\]

The closing vector is gamma=a e_1-a e_2. Its normal part is a e_1 and its tangential closing shift is -a e_2. This spatial translation induces a unitary on the full and physical boundary spaces and commutes with the gauge projection. The temporal integral is the usual product of coordinate slab kernels, followed by this spatial closing identification; hence it is the twisted trace with the inverse closing unitary, exactly as in (8). This can also be checked by taking time representatives 0,...,a-1: a top vertex (a,x_2,x_3,x_4) is identified with (0,x_2+a,x_3,x_4).

Straightening therefore gives the ordinary rectangular lattice

\[
 \Gamma_T=\langle a e_1,4a e_2,n e_3,n e_4\rangle.       \tag{11}
\]

No altered plaquette coefficient or special seam action remains. The shear merely relabels the spatial indices at the seam. The odd value of a means the two antipodal coordinate mirrors have unlike site/link types, which the halfstep representation includes.

## 8. Iteration over four cell directions

We spell out why the one-axis inequality is sufficient for the cellwise one.

Take a frame of four orthogonal mirror families with admissible wall offsets and widths b_i. Suppose the sequential height periods are p_i, the numbers J_i=p_i/b_i are even, the straight closing vectors are lattice vectors, and the cell brick with J_i indices in direction i represents the initial and successive period lattices. These facts were checked explicitly for the two frames in the companion geometry note.

Let G_kappa be bounded local functions supported strictly inside the individual cells. Group their product into the J_1 height slabs of direction one and apply (10). Each right-hand factor retains one slab and reflects its cell integrands through direction one.

Apply the direction-two version of (10) separately to every resulting partition function. Orthogonality implies that a direction-one reflection preserves every direction-two height. Thus the retained layer still separates into direction-two slabs. After this step each factor is the two-direction reflected repeat of one original row of cells.

Repeat in directions three and four. The affine reflections in different frame directions commute; the corresponding antilinear actions on scalar functions commute as well. Thus a terminal factor is precisely the full reflected cell array of one original cell function. The exponents multiply to

\[
 (J_1J_2J_3J_4)^{-1}.
\]

If N_cell=J_1J_2J_3J_4, the result is

\[
 \left|Z_\Gamma\!\left[\prod_\kappa G_\kappa\right]\right|
 \le\prod_\kappa
       Z_{\Gamma_{\rm final}}
          [\operatorname{Fold}_{\rm cells}G_\kappa]^{1/N_{\rm cell}}.
                                                               \tag{12}
\]

Each folded partition function is nonnegative by (9) in the final folding direction.

There is no unresolved corner/intersection assignment in this argument. After each one-axis gluing, all boundary variables and features for that axis have been integrated or contracted, yielding an ordinary Wilson action on the straightened torus with exactly one factor per plaquette. The next direction reclassifies that ordinary graph from scratch. A plaquette touching two orthogonal cell walls is never assigned two simultaneous halfweights from different unglued constructions.

## 9. Apply the identities to the original odd-L family

Use the geometry note's scales

\[
 n=2L^M,\quad a=n/2,\quad h\mid H\mid a,\quad
 w=qh/2,\quad q\text{ odd},\quad qh\mid H.
\]

All scales h,H,w are fixed before M tends to infinity, h,H are integers at least four, and w is a half-integer at least four.

### 9.1 Coordinate to diagonal

For the diagonal frame (s_-,s_+,x_3,x_4), the sequential height periods are

\[
 (n,2n,n,n).
\]

The first minus-diagonal straightening replaces n e_1 by a e_-. Its cross-section is generated by n e_+,n e_3,n e_4. Therefore its period lattice is already Gamma_D. The plus-diagonal straightening changes no geometric period, and neither do the two transverse straightenings. Pure Wilson fields have no fermionic closing character, so there is no separate D-prime boundary-condition sector.

The cell counts are

\[
 (n/h,2n/h,n/h,n/h),
 \qquad N=2n^4/h^4.
\]

They are even and their brick represents both period lattices. Formula (12) therefore yields the coordinate-to-diagonal cell inequality on the original n=2L^M family.

The same proof on D_n with width H gives its coarse diagonal chessboard inequality, with N'=2n^4/H^4 cells.

### 9.2 Diagonal to coordinate

For the coordinate frame on D_n, the sequential height periods are (a,4a,n,n). With w=qh/2 their slab counts are

\[
 (2A,8A,4A,4A),\qquad A=a/(qh),
 \qquad N''=n^4/w^4.
\]

All counts are even. The first straightening gives (11), and the other three leave it unchanged. The cell-index period generators are

\[
 (2A,-2A,0,0),\ (4A,4A,0,0),\ 4Ae_3,\ 4Ae_4.
\]

The brick of side counts (2A,8A,4A,4A) represents D_n by first reducing the first coordinate, then using the combination (0,8A,0,0), and finally reducing the transverse ones. It also represents T_n. Thus (12), with the coordinate mixed-type slab identity, yields the second cellwise fold. This explicitly verifies the fundamental-domain identification rather than assuming it from a diagram.

The separate placement lemma puts each amplified insertion in a distinct coordinate cell and keeps every source box away from all coordinate walls. Therefore its functions are legitimate cell integrands for (12). No source term is cut.

## 10. Correctly normalized source comparison

There is a normalization trap if one tries to raise an unnormalized single-source partition function to the number of cells. The valid comparison uses full arrays on both tori.

Let O be real, gauge invariant, and supported in one open diagonal h-cell. Form V_C and V_D by summing its wall-reflected copies in all N cells of C_n and D_n respectively. The arrays are periodic because the period lattices lie in the translation subgroup of the diagonal wall group.

For odd h, do not replace these copies by normal half-height translations: those need not be lattice translations. Instead use the actual wall reflections. Every such reflection is an integer affine signed permutation preserving the coordinate torus and its Wilson law. Hence

\[
 \mu_C(V_C)=N\mu_C(O).
\]

Every cell integrand exp(t O^[kappa]) has exactly the same full diagonal fold exp(t V_D), by consistency of the reflected copies. Equation (12) gives

\[
 Z_C[e^{tV_C}]\le Z_D[e^{tV_D}].                        \tag{13}
\]

All quantities in (13) are positive. Jensen's inequality and convexity of

\[
 F_D(t)=\log\bigl(Z_D[e^{tV_D}]/Z_D[1]\bigr)
\]

give, for t>0,

\[
 \begin{split}
 tN\mu_C(O)
 &\le \log\frac{Z_C[e^{tV_C}]}{Z_C[1]}\\
 &\le F_D(t)+\log Z_D[1]-\log Z_C[1]\\
 &\le tN\mu_{D,t}(O)+\log Z_D[1]-\log Z_C[1].
 \end{split}
\]

The last equality uses invariance of the tilted D array under its wall group, so every reflected copy has the same tilted expectation. Consequently

\[
 \mu_C(O)\le\mu_{D,t}(O)
       +\frac{\log Z_D[1]-\log Z_C[1]}{tN}.             \tag{14}
\]

With constant integrands, (12) gives Z_C[1]<=Z_D[1]<=Z_T[1]. The elementary common-pressure argument at fixed beta makes the numerator in (14) o(n^4), while N=2n^4/h^4. Thus the error vanishes with volume for each fixed positive t. This does not identify the two unperturbed local states without the separate tilt-removal/translation argument.

## 11. What is proved and what still lies outside this note

The diagonal feature construction supplies an exact Hilbert--Schmidt kernel, adjoint reflection, gluing, sheared-torus trace, even-Schatten fold, and iterated cellwise inequality. Its normalization is checked directly by a partition of links and plaquettes, with normalized Haar integration. The first-fold action on the straightened graph is precisely ordinary Wilson.

The second-frame inequality uses the coordinate physical-space slab construction, including its mixed site/link normalization. The only extension used here is to bounded complex gauge-invariant integrands and a unitary tangential closing shift, justified in Section 7. Its period lattice and cell counts are explicit.

The two-frame placement, the bounded local operator estimate, and the local outer-layer reduction are separate lemmas. Their assembly, the ordered limits in volume and tilt, and convex separation must still be checked to conclude same-limit diagonal RP. No uniqueness of a Gibbs state is assumed in the finite identities here.

## References and provenance

* QED3 manuscript, pinned repository commit e392ef45013a581664bab76b90867170b30fe10e, Section 3.2--3.3, printed pp. 20--25, especially (3.17)--(3.27), supplies the comparison architecture and the Schatten formulation. The Wilson boundary feature proof above is given explicitly instead of importing its fermionic slab theorem. https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/e392ef45013a581664bab76b90867170b30fe10e/QED3_slop/qed3.pdf
* Local companion proofs: work/transfer_schatten_research.tex and work/two_frame_geometry_research.md.
