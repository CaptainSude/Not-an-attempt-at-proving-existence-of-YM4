# The full flat constraint-current term: a fixed-step quadratic composition bound

16 October 2026. Research result, independently checked by a separate internal source and mathematical audit; no external certification is claimed. The target is the separate `Theta_J` in deposited Raw I:13733–13739. The background is fixed at the identity, the final physical block scale is one, and the refinement is `M=L^j` with **fixed odd L**. The corrected nonlinear averages are the iterates recorded at I:24320–24325, not a newly chosen single averaging operation of block size M. The argument below proves a refinement-uniform physical-cell Hilbert form bound from the finite one-step quadratic jet, its explicit flat linearization, and the recorded composition. No nonflat averaging theorem or path trace estimate is assumed.

The operator identification is at the level of the deposited transcriptions. The original CMP98 full text has not been recovered in this check: the workspace contains no CMP98 PDF; the Rutgers record links to the publisher DOI, and the publisher preview is the known access boundary. That does not imply the original definition or estimate is absent. The note separates the precise source identifications from the new elementary uniform bound.

## 1. Exact source path and the first-order form

The relevant defining formulas are:

* Raw I:13725–13731 defines the already controlled auxiliary `G_pi^J,q_J,H^J` using `Theta'_J`.
* I:13733 defines `Theta_J` by ` <A,Theta_J A>=2<H^J C^(2)(ell A),J> `. I:13737 adds `Pi^T Theta_J Pi` to the full fine precision, with `Pi=I-DLambda` and fixed `Lambda=G'RD^*` at the background.
* I:13924–13931 moves `H^J` onto the current and invokes CMP98 (149). It does not display a proof of a physical L2 bound there.
* I:24320–24325 explicitly defines order `j+1` of the corrected double-bar operation by composition of its one-step version with order j; the intermediate background is the corresponding averaged reference background.
* I:24339–24369 identifies the logarithmic one-step map, its linear term `L Q(V_0)A`, and its quadratic-and-higher remainder. At `V_0=1`, transports and `g(0)` are identities and `Y=Y_x=0`; every displayed correction to the main straight-string average vanishes. Thus its flat linear term is `L Q_L^st` at every intermediate step.
* I:26985–26988 identifies the tower `C_j^(2)` with the second-order term in the nonlinear average `Q_j(eta A)`, and with the corrected remainder in CMP98 (122)–(123). I:27522–27526 repeats the identification.
* I:47076–47087 explicitly incorporates CMP98 (120) and expresses this corrected logarithmic coordinate in terms of the maps `Phi^flat,Phi^g` defined at I:46965–46973. This additional identity fixes the input coordinate without guessing the omitted definition of V_1; it is written out in Section 2 below.
* The source scale `ell` is the physical length of the retained coarse layer (I:13583–13585 and I:14141); it equals one in the present homogeneous final-scale coordinates. It is not the fine spacing `eta=M^-1`.

In particular, write `C_j^(2)(A,B)` for the symmetric bilinear quadratic coefficient at final scale one, and normalize `E_J=H^J ell=H^J` in these units. Put

\[
 w_J=E_J^T J.
\]

Then the exact full constraint-current form is

\[
 \langle A,\Theta_J B\rangle_\eta
       =2\langle C_j^{(2)}(A,B),w_J\rangle_1.
                                                        \tag{1.1}
\]

At zero current, `Theta_0=0`. Its derivative in a direction `K` is

\[
 \langle A,\Theta^{[1]}_K B\rangle_\eta
       =2\langle C_j^{(2)}(A,B),E_0^T K\rangle_1.
                                                        \tag{1.2}
\]

The derivative of `E_J` contributes nothing here because it is multiplied by the zero base current. Therefore the first derivative of the full coarse precision, with the same fixed Q, is

\[
 D[(QG_1^JQ^*)^{-1}]_0[K]
       =-E_0^T\Theta^{[1]}_K E_0,
                                                        \tag{1.3}
\]

because `Pi E_0=E_0` and the auxiliary `Theta'_K` contribution cancels. Equivalently its coarse quadratic form is

\[
 -2\langle C_j^{(2)}(E_0 B,E_0 C),E_0^T K\rangle_1.
                                                        \tag{1.4}
\]

This first-order contribution is not forced to vanish by the auxiliary cancellation. Its control is the purpose of the following argument.

## 2. The fixed one-step jet and the physical factor h

Let `F_L` be the logarithmic **corrected** one-step group average at identity background, expressed in dimensionless fine bond angles X. Its Taylor jet is

\[
 F_L(X)=LQ_L^{\rm st}X+C_L(X,X)+O(X^3).
                                                        \tag{2.1}
\]

There is an explicit deposited formula for this coordinate. Define

\[
 \phi(X;c)=\Phi^{\flat}(1,X;c),\qquad
 \alpha_y(X)=L^{-d}\sum_{x\in B(y)}\Phi^{\mathfrak g}(1,X;y,x).
\]

The `Phi` maps use `e^{iX}V` as their input (I:46965–46973). At `V=1`, I:47082–47086 reads

\[
 e^{i\phi(X;c)}=e^{i\alpha_{c_-}(X)}e^{iF_L(X;c)}
                                  e^{-i\alpha_{c_+}(X)}.
\]

Consequently, on the identity logarithm branch,

\[
 F_L(X;c)=\frac1i\log\left[
 e^{-i\alpha_{c_-}(X)}e^{i\phi(X;c)}e^{i\alpha_{c_+}(X)}\right].
                                                        \tag{2.1a}
\]

For homogeneous Taylor coefficients use subscripts 1 and 2, and abbreviate `alpha_{c_±}` by `alpha_±`. BCH now gives the exact diagonal quadratic coefficient

\[
 \begin{aligned}
 C_L(X,X)(c)={}&\phi_2-\alpha_{-,2}+\alpha_{+,2}\\
 &+\frac i2\bigl(-[\alpha_{-,1},\phi_1]
                 -[\alpha_{-,1},\alpha_{+,1}]
                 +[\phi_1,\alpha_{+,1}]\bigr).
 \end{aligned}                                         \tag{2.1b}
\]

Polarization gives `C_L(A,B)`. Its linear coefficient is `-alpha_{-,1}+phi_1+alpha_{+,1}=LQ_L^st`, in agreement with the independent displayed linearization at I:24357–24369. In particular the later unit-lattice vertex named `C^(2)=Phi^flat_2` at I:46978 is **not** substituted for (2.1b): the endpoint contour terms and BCH commutators are essential. Formula (2.1a) is the deposited coordinate bridge that resolves the earlier omission of V_1 from CMP98 (120).

Here `C_L` is the symmetric bilinear coefficient, not the full second derivative (which is `2 C_L`). For each output bond c it reads a finite set `D_L(c)` of fine bonds inside its double block, or a fixed finite collar. Its coefficients are finite constants depending only on the fixed L, dimension, color space and specified averaging prescription. In particular there exists finite `K_L` such that

\[
 |C_L(A,B)(c)|\le K_L
       \max_{b\in D_L(c)}|A(b)|
       \max_{b\in D_L(c)}|B(b)|.
                                                        \tag{2.2}
\]

No estimate uniform as `L->infinity` is required. A finite one-step jet suffices. Such a jet follows from the finite analytic group products, logarithms and group means near the identity. Alternatively, the transcribed one-step remainder bound I:24349–24353 gives a finite quadratic constant directly by taking the Taylor coefficient and polarizing. This avoids importing the unproved multilevel complex-background assertions mentioned in I:13982–13983.

At physical fine spacing h, an input potential A has angle `hA`, and the output spacing is `Lh`. Thus the physical one-step potential map is exactly

\[
 \mathcal F_h(A)=(Lh)^{-1}F_L(hA)
     =Q_h A+\mathcal B_h(A,A)+O(A^3),
\]
\[
 Q_h=Q_L^{\rm st}\ \text{at spacing }h,
 \qquad \mathcal B_h(A,B)=\frac hL C_L(A,B).
                                                        \tag{2.3}
\]

The factor h is essential. Keeping only a dimensionless finite-step constant would produce a spurious factor j after iteration.

## 3. A uniform one-step paired Hilbert form estimate

Let

\[
 N_L=\sup_b\#\{c:b\in D_L(c)\}.
\]

This is finite and depends only on fixed one-step geometry. For literal double blocks, each fine bond occurs in only a bounded number of incident coarse-bond double blocks; allowing a fixed collar changes this by another finite geometric factor. On short tori use the same covering-space multiplicities. No dependence on the total refinement or on volume enters `N_L`.

For a bounded coarse one-form weight w, the physical pairing and (2.2) give

\[
 \begin{aligned}
 |\langle w,\mathcal B_h(A,B)\rangle_{Lh}|
 &\le K_L L^{d-1}h^{d+1}\|w\|_\infty
       \sum_c
        \Big(\sum_{b\in D_L(c)}|A(b)|^2\Big)^{1/2}
        \Big(\sum_{b\in D_L(c)}|B(b)|^2\Big)^{1/2}\\
 &\le K_L N_L L^{d-1}h\|w\|_\infty
               \|A\|_{2,h}\|B\|_{2,h}.
 \end{aligned}
                                                        \tag{3.1}
\]

The last step is Cauchy–Schwarz over output bonds and the incidence bound, followed by the fine volume factor `h^d` in both input norms. Denote the fixed constant `K_L N_L L^{d-1}` by `k_L`. This proves a bilinear form bound; it does not take a pointwise-to-Hilbert norm comparison over an M-sized final block.

## 4. The flat linear average has both needed contractions

For a positively oriented coarse bond in direction mu,

\[
 (Q_h A)_\mu(y)
 =L^{-d-1}\sum_{x\in B(y)}\sum_{r=0}^{L-1}
       A_\mu(x+rh e_\mu).
                                                        \tag{4.1}
\]

Its row coefficients are nonnegative and sum to one. In the physical adjoint each coefficient is multiplied by the coarse/fine volume ratio `L^d`. For each fine mu-bond, there are exactly L choices of the string offset r, each fixing one x and its unique block center y. Hence the column coefficient sum before that volume ratio is `L*L^{-d-1}=L^{-d}`. Therefore the physical adjoint also has nonnegative row coefficients summing to one:

\[
 Q_h1=1,\qquad Q_h^*1=1.
                                                        \tag{4.2}
\]

All choices are counted with multiplicity if a periodic image coincides. Jensen's inequality and (4.2) give

\[
 \|Q_hA\|_{2,Lh}\le\|A\|_{2,h},\qquad
 \|Q_h^*w\|_\infty\le\|w\|_\infty.
                                                        \tag{4.3}
\]

The same holds for every composition of the flat one-step averages. This is the precise measure-normalized contraction; a raw coefficient bound alone would not establish it.

## 5. Sum the quadratic jets of the actual iterated corrected map

Set `h_t=L^{t-j}` for `t=0,...,j`, so `h_0=M^-1` and `h_j=1`. Let `Q_t` act from spacing `h_t` to `h_{t+1}`, and write

\[
 Q_{r:s}=Q_{s-1}\cdots Q_r\quad(r<s),\qquad Q_{r:r}=I.
\]

Because the reference background is identity at every intermediate step, the actual corrected nonlinear composition has the same jet (2.3) at each scale. The quadratic chain rule gives exactly

\[
 C_j^{(2)}(A,B)
 =\sum_{t=0}^{j-1} Q_{t+1:j}
       \mathcal B_{h_t}(Q_{0:t}A,Q_{0:t}B).
                                                        \tag{5.1}
\]

This follows by induction: if a partial composition has linear part P and quadratic part C, composing with `Q_t + B_{h_t}` replaces C by `Q_t C+B_{h_t}(P,P)`. There is no extra factor two because every C and B is the homogeneous quadratic coefficient. Also, no uniform nonlinear neighborhood for the entire j-step map is needed to compute this finite Taylor jet at zero.

Pair (5.1) with w and apply (3.1) and both contractions in (4.3):

\[
 \begin{aligned}
 |\langle w,C_j^{(2)}(A,B)\rangle_1|
 &\le k_L\|w\|_\infty\|A\|_{2,\eta}\|B\|_{2,\eta}
                \sum_{t=0}^{j-1}h_t\\
 &=k_L\frac{1-L^{-j}}{L-1}
       \|w\|_\infty\|A\|_{2,\eta}\|B\|_{2,\eta}.
 \end{aligned}
                                                        \tag{5.2}
\]

Thus with `k_* = k_L/(L-1)`,

\[
 \boxed{\quad
 |\langle w,C_j^{(2)}(A,B)\rangle_1|
 \le k_*\|w\|_\infty\|A\|_{2,\eta}\|B\|_{2,\eta}.
 \quad}                                                  \tag{5.3}
\]

The constant is independent of j, M and compatible volume. For `j=0` the coefficient is zero. This proves the needed uniform paired estimate for the deposited corrected composition, subject only to the source-coordinate identification stated in Section 1. Its mathematical proof does not require the explicit list of second-order commutator coefficients or CMP98 (149).

## 6. From the form estimate to weighted physical-cell locality

Define a symmetric fine operator `T_w` by

\[
 \langle A,T_wB\rangle_\eta
       =2\langle C_j^{(2)}(A,B),w\rangle_1.
                                                        \tag{6.1}
\]

Equation (5.3) gives

\[
 \|T_w\|_{2\to2}\le2k_*\|w\|_\infty.
                                                        \tag{6.2}
\]

The final corrected operation reads only the two final blocks adjacent to its output bond, according to I:24332–24336 and I:25192–25197. In particular its quadratic coefficient has a bounded range in unit-cell coordinates. Even without the exact two-block statement, the finite one-step reading radius gives a uniform bound by summing physical radii across scales: if a step reads radius at most `rho_L h`, then the j-step composition reads radius at most `rho_L sum_t h_t <= rho_L/(L-1)`. Thus the bound requires only a fixed range, not a special sharp two-block assertion.

It follows that `T_w(x,y)=0` whenever the cell distance exceeds a fixed `R_*`, independent of j. Each block norm is at most its global Hilbert operator norm. Put `v(R_*)=# {z in Z^d:|z|_1<=R_*}`. Then

\[
 \|T_w\|_\kappa
 \le 2k_* v(R_*)e^{\kappa R_*}\|w\|_\infty
 =:\tau_\kappa\|w\|_\infty.
                                                        \tag{6.3}
\]

This is a physical-cell weighted Schur bound. It loses a fixed number of cells, never the number of fine sites in one cell. The same proof works on short compatible tori, using periodic range and counting the appropriate covering-space multiplicities in the one-step calculation.

### 6.1. A stronger pointwise bound for this vertex alone

The same fixed-step proof also gives a uniform fine `ell^infinity` bound. Write the bilinear coefficient on one step as

\[
 C_L(A,B)(c)=\sum_{b,b'\in D_L(c)}c_{c;b,b'}(A(b),B(b')),
\]

and let `K_L^coef` bound the finitely many bilinear coefficient norms and `m_L=max_c |D_L(c)|`. The physical one-step operator `T_w^h` defined by ` <A,T_w^h B>_h=2<w,B_h(A,B)>_{Lh} ` has absolute fine row sum at most

\[
 2L^{d-1}h N_Lm_LK_L^{\rm coef}\|w\|_\infty.
                                                        \tag{6.4}
\]

Indeed the matrix coefficient has the physical volume ratio `L^d`, the quadratic scaling `h/L`, and the factor 2 in the form. A fixed row meets at most N_L output coarse bonds and at most m_L second input bonds per such output. Symmetry gives the corresponding absolute column bound with the same fixed fine measure.

The exact iterated operator identity is

\[
 T_w=\sum_{t=0}^{j-1}Q_{0:t}^*\,
     T^{h_t}_{Q_{t+1:j}^*w}\,Q_{0:t}.
                                                        \tag{6.5}
\]

Both Q_{0:t} and its physical adjoint are `ell^infinity` contractions by (4.2), and the backward weight contracts as well. Therefore

\[
 \|T_w\|_{\infty\to\infty}
 \le\frac{2L^{d-1}N_Lm_LK_L^{\rm coef}}{L-1}
            \|w\|_\infty.
                                                        \tag{6.6}
\]

The final fixed coarse range also gives weighted cell-block bounds with `ell^infinity` fibers at a fixed additional range cost. This stronger assertion concerns the constraint vertex T_w itself. It does not say that `Pi=I-DLambda` is uniformly bounded on fine `ell^infinity`, and it does not by itself establish a pointwise norm for the full sandwiched perturbation `Pi^T Theta_J Pi`. A separate internal audit has checked (6.4)–(6.6).

## 7. The actual weight w_J is already controlled by the auxiliary theorem

The proved auxiliary-current neighborhood gives `||E_J||_kappa<=4e` on its fixed ball. For bounded fine J, the Hilbert norm on one unit cell obeys

\[
 \|J\|_{2,\text{one cell}}\le\sqrt d\|J\|_\infty,
\]

with a harmless fixed modification for an alternative orientation convention. The transpose rectangular Schur bound therefore yields

\[
 \|w_J\|_\infty=\|E_J^T J\|_\infty
       \le4\sqrt d\,e\|J\|_\infty.
                                                        \tag{7.1}
\]

No global L2 assumption on J is used: sum the cell blocks in each transpose row. On infinite volume this defines the bounded coarse weight by an absolutely convergent cell sum. The map `J -> w_J` is analytic from fine `ell^infinity` to coarse `ell^infinity`, since the bilinear evaluation `(E,J)->E^TJ` is bounded in these norms.

The actual full constraint term is exactly `Theta_J=T_{w_J}`. Hence

\[
 \boxed{\quad
 \|\Theta_J\|_\kappa
       \le4\sqrt d\,e\tau_\kappa\|J\|_\infty.
 \quad}                                                  \tag{7.2}
\]

It is analytic on the auxiliary ball and is finite range as an operator in A, although its coefficients depend nonlocally on J through the exponentially local extension E_J.

At zero current (1.2) and (6.3) give the same linear bound for the exact first-order form. The role of the earlier local minimizing extension is through E_0 and the auxiliary E_J; no trace of an arbitrary fine L2 field along a macroscopic axial path is taken in (7.1).

## 8. Quantitative consequence for the full homogeneous flat G_1 family

Let `p=||Pi||_kappa`, finite by the proved bound on `DLambda`. Write

\[
 \Psi_J=\Theta'_J+\Pi^T\Theta_J\Pi,\qquad
 \xi=\theta+4p^2\sqrt d\,e\tau_\kappa.
\]

Throughout the auxiliary ball, `||Psi_J||_kappa<=xi||J||_infinity`. Keep the auxiliary constants `g,b,q,c=gb^2q` and choose

\[
 \varepsilon_1=
 \min\left\{\varepsilon_{\rm aux},
              [4g\xi(1+c)]^{-1}\right\}.
                                                        \tag{8.1}
\]

For `||J||_infinity<epsilon_1`, the two Neumann arguments from the auxiliary theorem apply to the analytic (now nonlinear) perturbation Psi_J. They give the actual full flat family

\[
 G_1^J=(\Delta_0-\Psi_J)^{-1},\quad
 q_1^J=(QG_1^JQ^*)^{-1},\quad
 E_1^J=G_1^JQ^*q_1^J,
                                                        \tag{8.2}
\]

analytic in the same physical-cell algebra with bounds `2g,2q,4e`, respectively. This is the form of the actual source family I:13737–13739 in homogeneous final-scale-one coordinates. There is no auxiliary first-order cancellation for q_1: its first derivative is (1.3).

Fine derivative sandwiches of G_1 of total order at most two also follow by placing the derivatives on the outside G_0 factors in the resolvent identity, exactly as for the auxiliary family. No derivative of J is introduced. The auxiliary exact current-chain formulas cannot simply be copied to full G_1, since Psi_J is nonlinear in J; ordinary analytic differentiation or Cauchy estimates would account for its higher derivatives separately.

Source-local decay also has a different geometry. Already at first order, `w_K=E_0^TK` can carry a current from cell x to a coefficient cell y, where the two potential legs branch towards cells b,c. Its natural bound sums a Y-shaped tree over y. The auxiliary ordered path `b -> x -> c` at the same exponential rate does not follow automatically. The present result asserts uniform analytic weighted operator bounds, not that stronger path formula.

## 9. Why a path-concentration objection does not invalidate this proof

A single physical line integral of a general fine field need not have a refinement-uniform L2 bound. For a path of fixed physical length made of `O(eta^-1)` fine bonds, the functional `eta sum_path A` has norm of order `eta^{(1-d)/2}` in the fine physical Hilbert space. A field concentrated on that path demonstrates the growth. Brackets of two such unsmeared path functionals can have an even larger paired norm.

This observation means that a generic macroscopic rooted-path formula cannot be bounded using its path length and physical L2 norm alone. It does **not** establish a counterexample to the actual corrected C_j^(2). In particular a newly defined single step with block ratio M is not identified with the nonlinear iterate of the fixed L-step map merely because their flat linear terms both equal Q_M^st. Their quadratic jets can differ.

The proof above avoids that inference. Every potentially concentrated path is confined to a fixed finite L-step geometry; its entire cost is included in K_L and N_L. It is then accompanied by the physical factor h_t, while the fields arriving at that step and the backward weights are contractions. Their sum is (5.2). This is the viable norm repair: use the physically scaled quadratic jet of the actual fixed-step composition and pair it before estimating it.

## 10. Status, source limitations, and what has not been proved

The new mathematical implication is explicit: a local fixed finite one-step jet, flat differential Q_L^st, the physical normalization (2.3), and composition imply the uniform quadratic form bound (5.3). Together with the already proved flat inverse and auxiliary-current results, it implies (7.2) and the full flat current neighborhood (8.2). The required source composition, linearization, and quadratic-vertex identification are recorded at the exact deposited lines listed in Section 1; an independent internal audit of those identifications and this proof has now passed.

The deposited record itself notes at I:24399–24409 that several original CMP98 definitions are not reproduced there, including V_1 from (120), the auxiliary Y,Y_x,g, and some one-step averaging notation. The later explicit bridge I:47076–47087 fixes the flat potential coordinate needed here, as shown in (2.1a); thus the present proof no longer leaves that coordinate to guesswork. This is still not a fresh primary-paper verification of every original definition. The source C_j^(2) is the jet of the corrected iterate, not the later rooted pivot-average jet: the match uses I:26985–26988, the logarithmic/linear split I:24344–24349, the nonlinear composition I:24320–24325, and the explicit bridge (2.1a). The proof is not based on a failed search for the original paper.

The original article is T. Balaban, *Averaging operations for lattice gauge theories*, Communications in Mathematical Physics 98 (1985), 17–51, DOI [10.1007/BF01211042](https://doi.org/10.1007/BF01211042). The [Rutgers institutional record](https://scholarship.libraries.rutgers.edu/esploro/outputs/journalArticle/Averaging-operations-for-lattice-gauge-theories/991031666237604646) supplies this bibliographic match but only links to the publisher. A legitimately public copy of CMP109 was read for its separate symmetrized-average definitions (0.10)–(0.12), pp.253–254; those later definitions were not substituted for the selected corrected CMP98 map in this proof.

Even after the stated source match is audited, this result is homogeneous, flat, and in weighted physical-cell L2 norms. It does not establish nonflat source stability, a mixed-history or retained-domain theorem, pointwise/Hölder analytic-carrier bounds, the nonlinear minimizing map beyond its quadratic coefficient, or an interacting Yang–Mills continuum limit.
