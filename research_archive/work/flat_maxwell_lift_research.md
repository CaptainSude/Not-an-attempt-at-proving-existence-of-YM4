# A compact, uniformly bounded-energy right inverse of the flat bond average

16 October 2026. This proves a finite-dimensional and lattice-linear statement, not the nonlinear Yang--Mills minimizer theorem. The compact construction was found independently in two equivalent moment-cancellation forms by the root and provenance agents; this note uses the root's smaller-norm version. An independent Fourier construction cross-checks the normalization and scale-uniform upper bound. The repository and output notebooks were not edited.

## 1. Statement and exact normalization

Set the coarse spacing to one and the fine spacing to `eta=1/M`, where `M` is a positive odd integer. Coarse sites are `j in Z^d`, fine sites are `x in eta Z^d`. Periodic versions use the same coordinate formulas with the periodic lattice-cell multiplicities retained. Write `M=2h+1` when `M>=3`.

For physical fine one-form coordinates, define

\[
 (d_\eta A)_{\mu\nu}(x)
 ={A_\nu(x+\eta e_\mu)-A_\nu(x)
    -A_\mu(x+\eta e_\nu)+A_\mu(x)\over\eta},\quad\mu<\nu,
\]
\[
 \|A\|_\eta^2=\eta^d\sum_x\sum_\mu|A_\mu(x)|^2,
 \qquad \|F\|_\eta^2=\eta^d\sum_x\sum_{\mu<\nu}|F_{\mu\nu}(x)|^2.
                                                               \tag{1.1}
\]

The coarse norm is the unweighted counting norm. The exact straight-string average, matching `current_interface_research.md` Section 10.2, is

\[
 (Q_M A)_\mu(j)
 =M^{-d-1}\sum_{r\in\{-h,\ldots,h\}^d}
                    \sum_{t=0}^{M-1}
              A_\mu\bigl(j+\eta r+\eta t e_\mu\bigr). \tag{1.2}
\]

For `M=1`, interpret this as the identity. Formula (1.2) is a physical potential average, not an unscaled line integral. Its normalized powers of `M` and the volume factor in (1.1) are essential.

**Theorem.** For `d>=2`, there is an explicit real linear right inverse `E_M` such that

\[
 Q_ME_MB=B,
 \qquad \|E_MB\|_\eta^2\le2^{d+1}\|B\|_1^2,
\]
\[
 \boxed{\quad
 \|d_\eta E_MB\|_\eta^2
 \le C_d\|B\|_1^2,
 \qquad C_d=2^{d+6}(d-1).
 \quad}                                               \tag{1.3}
\]

The constants are independent of `M`, volume and the number of independent Lie-algebra components. Each basis field associated with one coarse bond is supported in the two blocks at that bond's endpoints. Consequently

\[
 q_M(B):=\inf_{Q_MA=B}\|d_\eta A\|_\eta^2
                         \le C_d\|B\|_1^2.            \tag{1.4}
\]

The infimum is over the unrestricted infinite or periodic fine field space, or a supported field space containing the stated compact lift. Section 6 states the boundary limitation explicitly. For `d=1`, the curl energy is identically zero and there is no Maxwell coercivity claim.

## 2. One-dimensional transverse profile

Define a real sequence on integer fine coordinates by

\[
 \phi_M(r)=
 \begin{cases}
 \dfrac{M}{h+1}\left(1-\dfrac{|r|}{h+1}\right),&|r|\le h,\\
 0,&|r|>h.
 \end{cases}                                         \tag{2.1}
\]

Its translates by multiples of `M` have disjoint site supports. Direct summation gives

\[
 {1\over M}\sum_r\phi_M(r)=1,
 \qquad 0\le\phi_M(r)\le2,
 \qquad {1\over M}\sum_r\phi_M(r)^2\le2.              \tag{2.2}
\]

Indeed the unnormalized tent sums to `h+1`, and the last inequality follows from its maximum and its average.

Let `D_eta phi(r)=M[phi(r+1)-phi(r)]`. All nonzero differences have magnitude `M^2/(h+1)^2`, and there are `2(h+1)` of them, including the two boundary differences to zero. Therefore

\[
 {1\over M}\sum_r|D_\eta\phi_M(r)|^2
 ={2M^3\over(h+1)^3}
 ={16M^3\over(M+1)^3}\le16.                         \tag{2.3}
\]

The difference supports of adjacent translates overlap only at their common boundary edge. Thus their pointwise overlap multiplicity is at most two. This will pay for arbitrary changes of the coarse coefficient across a block face.

## 3. One-dimensional longitudinal profile and exact biorthogonality

The longitudinal profile does not need a uniformly bounded derivative: the curl of an `mu`-component differentiates it only in directions different from `mu`. It needs a bounded norm and exact cancellation of the neighboring averaging moments.

For `s=0,...,M-1`, put `u_s=(s-h)/M` and let `E` mean the uniform average over these `M` sites. Define

\[
 m_1=\mathbb E|u|={M^2-1\over4M^2},
 \qquad m_2=\mathbb E u^2={M^2-1\over12M^2},
\]
\[
 v=m_2-m_1^2={1+2/M^2-3/M^4\over48}\ge{1\over48},
\]
\[
 \alpha={m_2\over v},\qquad \beta=-{m_1\over v},
 \qquad
 \psi_M(s)=\alpha+\beta|u_s|\quad(0\le s<M),          \tag{3.1}
\]

and set `psi_M(s)=0` otherwise. These formulas are used for `M>=3`. Since `m2<=1/12` and `v>=1/48`, `alpha<=4`. The defining linear equations give

\[
 \mathbb E\psi_M=1,
 \qquad \mathbb E|u|\psi_M=0,
 \qquad \mathbb E\psi_M^2=\alpha\le4.               \tag{3.2}
\]

The norm identity follows by expanding the square and using
`alpha+beta m1=1`, `alpha m1+beta m2=0`. The profile is even about `s=h`, so its positive and negative first moments vanish separately:

\[
 \sum_{s>h}(s-h)\psi_M(s)
 =\sum_{s<h}(h-s)\psi_M(s)=0.                       \tag{3.3}
\]

It is allowed to change sign. Positivity is unnecessary for a right inverse and would prevent these moment cancellations except for a thin single-site profile.

### 3.1 The three possible coarse rows

The one-dimensional part of (1.2) averages a field `a` by

\[
 (K_Ma)(z)={1\over M^2}\sum_{r=-h}^h\sum_{t=0}^{M-1}
                                                   a(Mz+r+t).
\]

Its counting kernel is triangular:

\[
 k_M(s)=\#\{(r,t):r+t=s\}
       =(M-|s-h|)_+,
\]

where it is understood as zero outside `-h<=s<=3h`. At the endpoint beyond that range the displayed positive-part formula is also zero.

For `a(s)=psi_M(s)` supported on `0<=s<M`, only rows `z=-1,0,1` can be nonzero. Write `w=s-h`. Their kernel weights on this support are respectively `(-w)_+`, `M-|w|`, and `(w)_+`. Hence

\[
 (K_M\psi_M)(0)
 ={1\over M^2}\sum_s(M-|s-h|)\psi_M(s)=1,
\]
\[
 (K_M\psi_M)(-1)=(K_M\psi_M)(1)=0,                  \tag{3.4}
\]

by (3.2)--(3.3), and all other rows are zero. Thus the translates of `psi_M` are exactly biorthogonal to all the coarse longitudinal averaging rows.

For the smallest nontrivial case `M=3`, the profile is `(0,3,0)` on `s=0,1,2`; the three triangle rows give `0,1,0` exactly. The transverse profile is `(3/4,3/2,3/4)` on `r=-1,0,1`. This checks the endpoints and the center of the construction directly.

For comparison, another exact longitudinal choice is

\[
 \psi'_M(s)=3-{6(s-h)^2\over h(h+1)},\quad0\le s<M.
\]

It has the same zeroth and separate first moments, as follows from the sums of squares and cubes. Its crude norm bound is larger, so it is not used in (1.3). This independent formula confirms that the cancellation is a moment identity, not a limiting approximation.

## 4. Tensor lift: exact right inverse and support

For the unit coarse `mu`-bond coefficient at `j`, define its scalar basis on fine sites by

\[
 \Psi_{\mu,j}(x)
 =\psi_M(Mx_\mu-Mj_\mu)
       \prod_{\nu\ne\mu}\phi_M(Mx_\nu-Mj_\nu).
                                                               \tag{4.1}
\]

Then set

\[
 (E_MB)_\mu(x)=\sum_jB_\mu(j)\Psi_{\mu,j}(x).         \tag{4.2}
\]

There are no cross-component terms. The longitudinal fine bond bases run from the first coarse center up to the last fine bond before the next center, `Mx_mu-Mj_mu=0,...,M-1`. The transverse coordinates run through the centered block `-h,...,h`. Therefore the bond and both its endpoints are contained in the union of the two endpoint blocks. The central interface bond has lower longitudinal coordinate `h`; it is included with the correct positive orientation.

For fixed `mu`, the supports for distinct `j` are disjoint at fine bond bases: longitudinal intervals of length `M` tile, and the transverse centered blocks tile. This is true also after periodic identification, provided lattice cells are counted with their proper periodic multiplicities.

The average (1.2) factorizes by coordinates. Each transverse factor is a block average of `phi_M`, which equals one in its own block and zero in every other block. The longitudinal factor is (3.4). Consequently

\[
 Q_M\Psi_{\mu,j}=\text{the unit coarse }\mu\text{-bond at }j,
 \qquad Q_ME_MB=B.                                  \tag{4.3}
\]

This proves surjectivity and an exact right inverse for every `M`, not just asymptotic approximation as the fine mesh shrinks.

## 5. Norm and curl-energy estimates

The one-dimensional norm products in (2.2) and (3.2) yield

\[
 \|\Psi_{\mu,j}\|_\eta^2\le4\,2^{d-1}=2^{d+1}.
\]

Disjoint supports for each component then give the first bound in (1.3).

For a transverse derivative `nu!=mu`, the derivative acts only on the corresponding `phi_M`. Its basis norm is bounded by

\[
 \|D_{\eta,\nu}\Psi_{\mu,j}\|_\eta^2
 \le4\cdot16\cdot2^{d-2}=2^{d+4}.                  \tag{5.1}
\]

The derivative basis supports have overlap multiplicity at most two. Thus, using `|a+b|^2<=2(|a|^2+|b|^2)` at the overlapping sites,

\[
 \|D_{\eta,\nu}(E_MB)_\mu\|_\eta^2
 \le2^{d+5}\sum_j|B_\mu(j)|^2.                     \tag{5.2}
\]

No derivative in the `mu` direction of the `mu` component occurs in the curl. Summing over `mu<nu`,

\[
 \|d_\eta E_MB\|_\eta^2
 \le2\sum_\mu\sum_{\nu\ne\mu}
                         \|D_{\eta,\nu}(E_MB)_\mu\|_\eta^2
 \le2^{d+6}(d-1)\|B\|_1^2.                         \tag{5.3}
\]

This proves (1.3). In dimension four the displayed conservative constant is `3072`. It is independent of refinement because the transverse taper changes over a physical distance of order one, and the longitudinal variation is absent from the curl estimate.

For `M=1`, take `E_1=I`. Each lattice difference has norm at most two, and the same pairwise estimate gives `||d_1 B||^2<=8(d-1)||B||^2`, which is smaller than the constant in (1.3). The right-inverse identity is immediate.

The minimization upper bound (1.4) now follows simply by inserting this feasible trial field. No minimizer existence or uniqueness is needed for the finite-dimensional infimum inequality itself.

## 6. Periodic, infinite-volume and boundary scope

The construction is real and compact, so it works on square-summable infinite-lattice fields by bounded extension from finitely supported fields. It works on a periodic lattice by periodicizing the basis fields. If a very short periodic direction identifies neighboring row labels, the cancellations in (3.4) are counted with multiplicity and still give the exact identity on that periodic row. There is no Fourier Nyquist issue in the compact proof.

The support is strictly inside the union of the two blocks at each source bond's endpoints. Therefore it gives a supported right inverse whenever the permitted fine region contains both endpoint blocks of every nonzero coarse source bond, including the fine bonds joining them. A one-block collar around the supported coarse source region is sufficient.

For an arbitrary Dirichlet problem that allows coarse data on incident boundary bonds but forbids all fluctuations in the exterior endpoint block, the displayed lift can leave the allowed region. Its periodic or whole-lattice energy bound does not by itself prove the same variational upper bound for that more restricted infimum. One must either provide the fixed collar, use a boundary-adapted right inverse, or otherwise prove the comparison. This note retains this boundary caveat rather than silently altering the integration domain.

The fine energy in this proof is the full sum of curls of the zero-extended field. Restricting the plaquette sum decreases it, but that observation cannot restore a violated constraint or a forbidden field support.

## 7. Independent Fourier check on periodic tori

Let the coarse torus have integer side lengths `N_1,...,N_d`, and let the fine torus have `MN_nu` sites in direction `nu`. Choose one representative of each coarse frequency

\[
 k_\nu=2\pi n_\nu/N_\nu\in[-\pi,\pi].
\]

Use this same physical frequency on the fine torus. Distinct chosen coarse frequencies are distinct fine Fourier modes. With the coarse counting and fine `eta^d` measures, the normalized mode `|Lambda_coarse|^-1/2 exp(ik dot x)` has norm one on both tori. This is the needed Parseval normalization; there is no leftover factor `M^d`.

For centered odd `M`, set

\[
 r_M(k)={\sin(k/2)\over M\sin(k/(2M))},\qquad r_M(0)=1.
\]

The centered block average has symbol `r_M(k)`, while the one-direction string average has symbol `exp(i(M-1)k/(2M))r_M(k)`. Hence the `mu`-component symbol of (1.2) is exactly

\[
 q_\mu(k)
 =e^{i(M-1)k_\mu/(2M)}r_M(k_\mu)\prod_\nu r_M(k_\nu).
                                                               \tag{7.1}
\]

For `|k|<=pi`, `|sin(k/2)|>=|k|/pi` and `M|sin(k/(2M))|<=|k|/2`, so

\[
 2/\pi\le r_M(k)\le1,
 \qquad |q_\mu(k)|\ge(2/\pi)^{d+1}.                \tag{7.2}
\]

Divide each embedded component Fourier coefficient by `q_mu(k)`. The resulting complex lift obeys `QA=B` and

\[
 \|A\|_\eta^2\le(\pi/2)^{2d+2}\|B\|_1^2.
\]

Its fine derivative multipliers are `delta_nu=M(e^{ik_nu/M}-1)`, so `|delta_nu|<=|k_nu|<=pi`. The exterior-product identity gives

\[
 \sum_{\mu<\nu}|\delta_\mu A_\nu-\delta_\nu A_\mu|^2
 \le\left(\sum_\nu|\delta_\nu|^2\right)\sum_\mu|A_\mu|^2.
\]

Thus this independent construction proves

\[
 q_M(B)\le d\pi^2(\pi/2)^{2d+2}\|B\|_1^2.          \tag{7.3}
\]

When `B` is real, take the real part of the complex lift. Since `Q` has real coefficients and `QA=B`, its real part is still feasible, and both its norm and energy can only decrease. This resolves any ambiguity from choosing only one representative of a coarse Nyquist mode. The Fourier proof is global and makes no support or arbitrary-Dirichlet claim.

## 8. Transfer to the flat effective Wilson Hessian: exact finite-level argument

The variational statement above is an Abelian quadratic theorem, applicable separately to every color at the trivial background. To identify it with the actual effective action one must retain the nonlinear source interface.

At a fixed finite level and volume, write the normalized fine field as `U_b=exp(i eta a_b)`, and assume the nonlinear coarse constraint is a smooth map `F(a)` with `F(0)=0` and `DF(0)=Q_M`. Let the coarse datum be parametrized by its physical Lie-algebra potential. Because `Q_M E_M=I`, the finite-dimensional map

\[
 z\longmapsto F(E_Mz)
\]

has derivative the identity at zero. The inverse function theorem provides a feasible curve

\[
 a(t)=E_Mz(t),\qquad F(a(t))=tB,
 \qquad z(t)=tB+O(t^2),
\]

and hence `a'(0)=E_MB`. The radius of this local inversion may depend on level and volume; no uniform radius is needed to compare the Hessian at zero.

For the physical Wilson normalization

\[
 S_\eta(U)=\eta^{d-4}\sum_p[1-\operatorname{Re}\operatorname{tr}U(\partial p)],
\]

the expansion at the trivial field is

\[
 S_\eta(e^{i\eta a(t)})
 ={t^2\over2}\|d_\eta E_MB\|_\eta^2+O(t^3).
\]

Suppose the stated branch of constrained minimizers exists, is twice continuously differentiable on a neighborhood of the trivial datum, takes value the trivial field there, and minimizes among these locally feasible competitors. The effective action is then at most this trial action. Its zero first derivative and the comparison after division by `t^2/2` imply

\[
 q_{\mathrm{eff},M}(B)\le\|d_\eta E_MB\|_\eta^2
                              \le C_d\|B\|_1^2.      \tag{8.1}
\]

This is a finite-level argument with a scale-independent final Hessian constant. It does not infer a uniform nonlinear analytic radius from the compact linear lift.

### 8.1 Rooted and corrected averaging conventions

The corrected multilevel average in `current_interface_research.md` Section 10.2 has flat derivative (1.2). The original contour-rooted composed average need not have the same potential-level derivative. As proved in `flat_maxwell_gap_research.md` Section 4.2, the full-block flat operators differ by a coarse gradient,

\[
 Q_k^{\rm rooted}A=Q_{L^k}^{\rm st}A+D_1\Psi_k(A).
\]

A scalar fine gradient whose values at the final coarse centers are `-Psi_k(A)` corrects a straight-feasible field to a rooted-feasible one without changing its fine curl. The scalar extension exists in finite dimension. Thus the compact lift yields a finite linear right inverse for the rooted constraint after this gradient adjustment, with the **same energy bound**, although no scale-uniform bound on the adjusted potential is asserted.

Apply the inverse function theorem to that corrected right inverse if the actual nonlinear minimizer uses the rooted constraint. Again, its finite-level radius may deteriorate; the second-order energy comparison does not. Conversely, a scalar block-mean right inverse corrects the other direction, establishing equality of the two quadratic energy infima under the full-block operator identity.

The original nonlinear average, its corrected version and the actual minimizer constraint must be identified from their definitions. Gauge covariance alone does not prove that identification. The source statement of minimizer existence/differentiability is also still an input. Arbitrary independent-current analytic carriers are not identified with a physical effective Hessian by this argument.

## 9. Consequence when combined with the audited lower bound

The lower estimate in `flat_maxwell_gap_research.md` gives `q_eff,M(B)>=||d_1B||^2`, and its finite-block axial Poincare argument gives `q_eff,M(B)>=gamma_loc||B||^2` on the one-step tree/mean-zero constraint slice, with fixed `gamma_loc(d,L)>0`. I independently checked its cochain factors, weighted contraction, finite-cube kernel proof and periodic overlap counting.

The present note supplies the missing uniform upper `q_eff,M(B)<=C_d||B||^2` on the full coarse field space, under the same finite-level minimizer identification. The explicit averaged-contour gauge bridge and pivot-extension constants then give both positive lower and finite upper bounds for the real flat reduced exponential-gauge precision, independent of the number of renormalization levels.

This closes that **flat precision bound** under the stated source match. It does not yet prove exponential covariance decay, uniform complex free-current perturbation bounds, local precision expansions, preservation of sharp cutoff coordinates under a gauge adjustment, or the interacting renormalization step. Those remain distinct obligations.
