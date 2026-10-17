# Exponential response locality of the small corrected-constraint minimizer

16 October 2026. Proof candidate passed a separate internal mathematical audit, with the infinite-lattice domain clarification below. This note derives a consequence of the proved fixed-slice minimizer construction, rather than assuming a nonflat inverse theorem. The background coarse field may be nonconstant, but its global bounded norm must lie in a fixed small ball. The fine minimizer remains in the fixed flat gauge and uses the corrected fixed-reference constraint. No statement about the separately moving source gauge or the ordinary-constraint transferred representative is included.

The constants are uniform in fixed-ratio refinements `M=L^j` and compatible finite periodic regulators. Infinite-lattice conclusions use the already constructed exponentially summable operators on complete fields, with the same caveat that a bounded field need not have finite total action.

## 1. Spaces and proved inputs

Use the notation of `nonlinear_fixed_gauge_minimizer_research.md`, but write the nonlinear remainder as `mathcal R` to distinguish it from the fixed scalar gauge projection R:

\[
 \mathcal F(A)=QA+\mathcal R(A),\qquad
 D_A=D\mathcal R(A),\qquad
 \mathcal X=\ker Q\cap\ker(RD^T).
\]

The fixed flat extension H and constrained inverse C satisfy all exact constraints recorded there. Let `N_alpha` be the complete physical field norm containing the field supremum, all first-difference suprema, and the local alpha-Hölder seminorms of those first differences.

Choose a fixed sufficiently small positive spatial exponent kappa supplied by the flat extension and constrained Schauder theorems. A positive unit-cell weight is admissible if

\[
 w(n)/w(m)\le e^{\kappa d(n,m)}.                 \tag{1.1}
\]

Weighted complete-field norms are formed by taking the supremum of `w(n)` times the local norm on a fixed cell collar. No sharp cutoff is inserted into a derivative. Coarse weighted bounded norms are defined in the same way. Constants accommodate a fixed collar enlargement.

On the infinite lattice an admissible decaying weight can allow an unbounded weighted direction. Literal Fréchet responses of the original bounded-field map are first taken on globally bounded directions with finite weighted norm. The displayed linearized formulas then define bounded extensions to the full weighted space. Higher-response symmetry is initially an assertion for bounded directions. All exponential support corollaries use growing weights `w_S>=1`, so this clarification does not weaken them.

The already established estimates, uniformly for every such w, are

\[
 H:\ell^\infty_{c,w}\to\mathcal N_{\alpha,w},\quad
 \mathcal C:\ell^\infty_{f,w}\to\mathcal N_{\alpha,w},\quad
 \mathcal C S_{\rm jet}^T:C^\alpha_{f,w}\to\mathcal N_{\alpha,w},
                                                               \tag{1.2}
\]
\[
 H^T:\ell^\infty_{f,w}\to\ell^\infty_{c,w},\quad
 (S_{\rm jet}H)^T:\ell^\infty_{f,w}\to\ell^\infty_{c,w},\quad
 q:\ell^\infty_{c,w}\to\ell^\infty_{c,w}.         \tag{1.3}
\]

References: the constrained result is `flat_constrained_schauder_research.md`, §§1,3–6; the extension and transpose kernels are the flat minimizing-extension results used there. In particular (1.2) has the same alpha in the input and output. The force has the form

\[
 N(A)=S_{\rm jet}^T f_\eta(S_{\rm jet}A).
\]

The weighted product argument in `wilson_nonlinear_force_research.md`, §5, gives, for globally small A,

\[
 \|D[f_\eta(S_{\rm jet}A)]V\|_{C^\alpha_w}
       \le C\|A\|_{\mathcal N_\alpha}\|V\|_{\mathcal N_{\alpha,w}}.
                                                               \tag{1.4}
\]

Therefore `C N'(A)` and `H^T N'(A)` have weighted norms bounded by `C_kappa ||A||N`. The second assertion uses `(Sjet H)^T`; it never differentiates the nonlinear coefficient.

## 2. The additional local transpose derivative estimate

The full corrected average has a physical dependency radius `R_*`, independent of the number of levels. This follows either from the deposited two-block property, or from the sum of one-step radii `r_L sum h_t <= r_L/(L-1)` proved in `flat_nonlinear_average_research.md`, §5. Enlarge `R_*` once to include cell collars.

The physical absolute row bounds of the differential and its transpose are

\[
 \|D_A\|_{\infty\to\infty}\le c\|A\|_\infty,\qquad
 \|D_A^T\|_{\infty\to\infty}\le c_*\|A\|_\infty.
                                                               \tag{2.1}
\]

The second bound is the new physical-column estimate of the minimizer note: at one step the physical transpose contributes `L^d`, and its remainder norm is at most `N_L K_0 L^(d-1) h ||A||`. Summing the spacings gives the uniform composite bound. No fine dimension enters it.

Finite dependency and (1.1) immediately give

\[
 \|D_AV\|_{\infty,w}\le c e^{\kappa R_*}\|A\|_\infty\|V\|_{\infty,w},
\quad
 \|D_A^Tm\|_{\infty,w}\le c_*e^{\kappa R_*}\|A\|_\infty\|m\|_{\infty,w}.
                                                               \tag{2.2}
\]

The less immediate estimate needed below differentiates the coefficients of the transpose while keeping its coarse input unweighted:

\[
 \boxed{\quad
 \|(D_A^T)'[V]m\|_{\infty,w}
       \le C_*e^{2\kappa R_*}\|V\|_{\infty,w}\|m\|_\infty.
 \quad}                                                       \tag{2.3}
\]

Here and below all background fields are in a fixed smaller complex ball; `C_*` is independent of refinement and volume.

Proof of (2.3). Fix an output fine bond b. Its row in `D_A^T` reads coarse bonds c within `R_*`; the coefficient associated with each c depends only on A in the dependency set of c, hence within `2R_*` of b. The map from the global bounded A-ball to the physical absolute row space is analytic with a uniform bound from (2.1), so Cauchy on a fixed larger ball bounds its derivative in the unweighted operator norm by `C_* ||V||infinity`. For this particular row replace V by its restriction to the union of those dependency sets; that restriction has supremum at most `e^(2kappa R_*) w(b)^(-1)||V||infinity,w`. No field derivative is taken in this operation: the corrected map and this coefficient derivative consume only bounded values. Multiply by w(b), sum the physical row against bounded m, and take the supremum over b. This proves (2.3). The same argument allows a weight on m with V unweighted. The construction is valid with lifted multiplicities on small periodic tori.

This is not a claim that `D_A^T` is local in the background with radius zero. The doubled dependency radius is essential. Cauchy is applied in the uniform physical-row operator norm, not to each fine coefficient followed by an uncontrolled count.

Higher coefficient derivatives similarly admit one weighted background direction, all other directions unweighted, with factorial constants from the fixed analytic margin. For the first response below only (2.3) is required. The two-Hilbert-direction Hessian incidence estimate used to prove strict minimality is consistent with these bounds but is not being substituted for (2.3).

## 3. Weighted linearization of the chart and multiplier

Write the exact chart and multiplier as

\[
 A=\xi+H[B-\mathcal R(A)],\qquad
 m=(I+H^TD_A^T)^{-1}\{q[B-\mathcal R(A)]+H^TN(A)\}.
                                                               \tag{3.1}
\]

All backgrounds under consideration obey `||A||N<=r`, `||B||infinity<=b`, and the already proved unweighted estimate

\[
 \|m\|_\infty\le C(b+r^2).                       \tag{3.2}
\]

The backgrounds themselves need not have finite growing-weight norm. Only their variations will be placed in weighted spaces.

Using (1.2) and (2.2), choose the common background radius small enough that

\[
 \|HD_A\|_{\mathcal N_{\alpha,w}\to\mathcal N_{\alpha,w}}<\tfrac12,
 \qquad
 \|H^TD_A^T\|_{\infty,w\to\infty,w}<\tfrac12
                                                               \tag{3.3}
\]

for every admissible weight. This is a fixed further shrinkage depending on kappa; it does not depend on the source location, M, or volume. Let `z=delta xi`, `b_1=delta B`, and `v=delta A`. Differentiating the chart gives exactly

\[
 v=P_A(z+Hb_1),\qquad P_A=(I+HD_A)^{-1},
\quad
 \|v\|_{\mathcal N_{\alpha,w}}
       \le 2(\|z\|_{\mathcal N_{\alpha,w}}+h_\kappa\|b_1\|_{\infty,w}).
                                                               \tag{3.4}
\]

Differentiating the defining equation for m, rather than differentiating a noncommuting inverse informally, gives

\[
 \delta m=(I+H^TD_A^T)^{-1}
 \left\{q(b_1-D_Av)+H^TN'(A)v-H^T(D_A^T)'[v]m\right\}.
                                                               \tag{3.5}
\]

Equations (1.3), (1.4), (2.2), (2.3), (3.2), and (3.3) prove

\[
 \|\delta m\|_{\infty,w}
 \le C_\kappa\left(\|b_1\|_{\infty,w}
                    +(r+b+r^2)\|v\|_{\mathcal N_{\alpha,w}}\right).
                                                               \tag{3.6}
\]

The term containing `(D_A^T)'` is the possible hidden obstruction in a naive weighted argument. It is precisely covered by (2.3). No weighted norm of the globally nonconstant m or B is assumed.

## 4. The response inverse at a small nonconstant background

The exact fixed-point equation is

\[
 \xi=\Phi_B(\xi)=-\mathcal C N(A)+\mathcal C D_A^Tm.
                                                               \tag{4.1}
\]

Its differential is

\[
 \delta\Phi=-\mathcal C N'(A)v
   +\mathcal C\{(D_A^T)'[v]m+D_A^T\delta m\}.    \tag{4.2}
\]

The preceding estimates imply, after restricting r below one,

\[
 \|\delta\Phi\|_{\mathcal N_{\alpha,w}}
 \le C_\kappa\left((r+b)\|v\|_{\mathcal N_{\alpha,w}}
                         +r\|b_1\|_{\infty,w}\right).
                                                               \tag{4.3}
\]

For `b_1=0`, combine (3.4) and (4.3). Choosing the fixed chart and coarse background radii so that `2C_kappa(r+b)<1/2` makes

\[
 \|D_\xi\Phi_B\|_{\mathcal N_{\alpha,w}\cap\mathcal X
                   \to\mathcal N_{\alpha,w}\cap\mathcal X}<\tfrac12.
                                                               \tag{4.4}
\]

The range is in X because every term contains C. At finite volume the space is closed; on the infinite lattice use the fixed-spacing interpretation of the exact constraints from the constrained-Green note. The uniform analytic norm estimates do not require a uniform bounded-field norm for the separate gauge projection.

Thus the derivative of the selected minimizer is obtained by the genuine weighted Neumann inverse

\[
 z=(I-D_\xi\Phi_B)^{-1}D_B\Phi_B[b_1],\qquad
 D_BA(B)[b_1]=P_A(z+Hb_1).                       \tag{4.5}
\]

Since the background solution has `||A(B)||N<=C||B||infinity`, equations (3.4)–(4.5) give the refinement- and volume-uniform conclusions

\[
 \boxed{\quad
 \|D_BA(B)[b_1]\|_{\mathcal N_{\alpha,w}}
        \le C_\kappa\|b_1\|_{\infty,w},\qquad
 \|(D_BA(B)-H)[b_1]\|_{\mathcal N_{\alpha,w}}
        \le C_\kappa\|B\|_\infty\|b_1\|_{\infty,w}.
 \quad}                                                       \tag{4.6}
\]

For the second bound, (4.3) with z=0 shows `D_BPhi=O(||B||)`, so `z=O(||B||)||b_1||w`; also `P_A-I=-P_AHD_A` has weighted norm `O(||B||)`.

This proof uses only the fixed-flat Green operators with nonlinear coefficients. It proves a response theorem at small nonconstant backgrounds without assuming a nonflat source Schauder theorem.

## 5. Exponential localization and finite nonlinear changes

For a source supported in a set S of coarse cells choose

\[
 w_S(n)=e^{\kappa d(n,S)}.
\]

This is admissible, including with periodic distance. The input norm of a bounded source supported in S equals its ordinary bounded norm, up to the fixed orientation collar convention. Equation (4.6) therefore gives

\[
 \|D_BA(B)[b_1]\|_{\mathcal N_\alpha(C_n^+)}
   \le C_\kappa e^{-\kappa d(n,S)}\|b_1\|_\infty.
                                                               \tag{5.1}
\]

The same estimate holds for the difference of two small-background minimizers whose coarse fields differ only in S. Indeed the straight coarse segment stays in the common complex ball, and integration of (4.6) along that segment gives

\[
 \|A(B')-A(B)\|_{\mathcal N_{\alpha,w}}
       \le C_\kappa\|B'-B\|_{\infty,w}.          \tag{5.2}
\]

The individual global fields need not decay. On the infinite lattice one can use truncated admissible weights, prove (5.2) with constants independent of the truncation, and then pass to the full weight; this avoids assuming weighted convergence of the initial global solutions.

## 6. Higher responses: a precise one-weight theorem

On a smaller common complex background ball, `B -> D_BA(B)` is analytic as a map to the bounded operators from `ellinfinity_w` into `N_alpha,w`. On finite regulators this is finite-dimensional holomorphy, with the uniform bound (4.6). On complete infinite fields it also follows directly from (3.4)–(4.5), the operator-valued local analyticity in §2, the weighted force product estimates, and the uniformly convergent weighted Neumann series. Varying the background in an unweighted bounded direction is sufficient; no weighted background assumption is introduced.

Let delta be the distance of the smaller background ball to the boundary of a ball on which the uniform complex estimate (4.6) holds. Multivariable Cauchy applied to this operator-valued function gives, for n>=1,

\[
 \boxed{\quad
 \|D_B^n A(B)[b_1,\ldots,b_n]\|_{\mathcal N_{\alpha,w}}
  \le C_\kappa (n-1)!\left(\frac e\delta\right)^{n-1}
          \|b_1\|_{\infty,w}\prod_{i=2}^n\|b_i\|_\infty.
 \quad}                                                       \tag{6.1}
\]

For n=1 this is (4.6). For n>1 use polyradii approaching `delta/(n-1)` and `(n-1)^(n-1)<=(n-1)! e^(n-1)`. Symmetry allows any one of the n directions to carry the weight. Consequently higher responses decay exponentially away from the support of any chosen localized insertion, while the other perturbations are arbitrary bounded directions.

If all directions are localized in sets S_i, applying (6.1) separately to each choice of the weighted direction gives an output bound with `exp[-kappa max_i d(n,S_i)]`. This is a precise consequence; it is not a fixed-exponent tree-length or ordered-path estimate among all insertions. Such stronger multivertex decay would require a separate branched response expansion or a justified multiweight argument. No such stronger claim is made here.

## 7. Scope and remaining independent audit

The result is a uniform exponential locality theorem for the derivatives and finite localized changes of the small corrected-constraint minimizer on its fixed flat gauge slice, including arbitrary small nonconstant global coarse backgrounds. The weighted exponent is chosen once from the proved flat kernel estimates and retained after a fixed shrinkage of the allowed background ball. It is not claimed that the original largest unweighted radius automatically suffices.

The proof does not identify these responses with the moving-gauge source minimizer, does not produce an interacting Gaussian inverse on a mixed history, and does not establish a uniform tree bound for all higher insertion sites. The ordinary-constraint transfer can change the chosen representative by a gauge depending on the field; locality of that transferred choice must be checked from its own formula rather than inherited merely from gauge equivalence.

Independent review should focus on §2's physical-row Cauchy estimate and doubled dependency radius, the noncommuting multiplier derivative (3.5), and the operator-valued holomorphy used in §6. All constants there arise from already proved fixed-L composition and flat weighted-operator estimates.

## 8. The coarse multiplier and its Hessian consequence

The same proof controls the selected multiplier `m(B)=m(A(B),B)`. In (3.5) substitute `v=D_B A(B)[b_1]` and use (4.6). The uniformly bounded weighted inverse gives

\[
 \|D_Bm(B)[b_1]\|_{\infty,w}\le C_\kappa\|b_1\|_{\infty,w}.
                                                               \tag{8.1}
\]

More precisely, let `M_A=I+H^TD_A^T`. Subtract `q b_1` from (3.5) to get the exact identity

\[
 (D_Bm-q)b_1=(M_A^{-1}-I)qb_1
   +M_A^{-1}\{-qD_Av+H^TN'(A)v-H^T(D_A^T)'[v]m\}.
                                                               \tag{8.2}
\]

At the solution `||A||N=O(b)` and `||m||infinity=O(b)`, where `b=||B||infinity`. The inverse difference, D_A, and N'(A) are each O(b) in their indicated weighted spaces. The last term is O(b) by (2.3), even though `(D_A^T)'` itself does not vanish at zero. Consequently

\[
 \boxed{\quad
 \|(D_Bm(B)-q)b_1\|_{\infty,w}
       \le C_\kappa\|B\|_\infty\|b_1\|_{\infty,w}.
 \quad}                                                       \tag{8.3}
\]

The multiplier is holomorphic as a global bounded-field map. Its derivative is holomorphic in the weighted operator space by the same local coefficient and weighted inverse argument used in §6. Thus on a smaller complex ball,

\[
 \|D_B^n m(B)[b_1,\ldots,b_n]\|_{\infty,w}
 \le C_\kappa(n-1)!(e/\delta)^{n-1}
                \|b_1\|_{\infty,w}\prod_{i=2}^n\|b_i\|_\infty.
                                                               \tag{8.4}
\]

The same localization and one-weight limitations as (6.1) apply.

For completeness, on a finite regulator define the classical coarse action `V(B)=S_eta(A(B))`. Differentiating the chart gives

`D_B A[b_1]=H_A b_1+T_A D_B xi[b_1]`, with `D_B xi[b_1] in X`.

Stationarity kills the second summand when paired with E(A). Since `H_A^T E(A)=m(A,B)`, the exact envelope identity is

\[
 DV(B)[b_1]=\langle m(B),b_1\rangle_1,
 \qquad D^2V(B)=D_Bm(B).                         \tag{8.5}
\]

Thus (8.3) gives a refinement-uniform exponentially local coarse classical Hessian equal to q at zero and an O(b) perturbation of q nearby. The Hessian is symmetric in the physical coarse bilinear pairing because it is a second derivative; no symmetry was assumed in deriving (8.2). This is a classical finite-regulator statement, not a quantum effective action or a positive physical mass-gap estimate. The total action can grow with volume; only the gradient and response norms claimed above are volume-uniform.
