# Independent audit of the flat axial-to-exponential gauge bridge

16 October 2026. Audited `exponential_gauge_bridge_research.md`, Sections 2--6, against direct finite-dimensional derivations and the indicated portions of the deposited manuscript. No repository or output files were edited.

## 1. Verdict and necessary scope clarification

The flat algebra, the signs in the two averaging constraints, both slice maps, the lower-coercivity constant, the pivot coefficient, the displayed coordinate norm estimates, and the Ward/BCH identity all check out. I found no substantive formula error in Sections 2--6 under the stated complete-block geometry.

For a boundary application, the bond convention needs to be explicit. The argument works for `Lambda` a union of complete centered `L`-blocks, with all bonds having **at least one endpoint** in `Lambda` retained as variables, other bond fluctuations set to zero, and gauge parameters set to zero outside `Lambda`. Include all coarse constraints on coarse bonds having at least one center in `Lambda'`. This convention makes the block projections and the boundary pivots available. It is the convention in raw II around line 9033, together with the complete-block hypothesis in `5.2:prop-form-positivity`, clause `(tilde H1)` around line 9743.

The same proof does not automatically apply to a different convention that freezes every crossing bond, or to a region cutting through the blocks. In such a convention the proposed gradients or block-mean subtraction may leave the allowed field/gauge space. This is a scope clarification, not a counterexample to the bridge with the deposited convention.

The mathematical conclusion is still conditional on an axial lower and upper bound for the actual flat Hessian in the stated coordinate convention. The audit does not supply the primary scale-uniform axial theorem, nor identify an arbitrary complex independent-current family with the physical Hessian. The scratch note correctly retains these distinctions.

## 2. Averaged contours and the penalty

For an oriented path from the center `y` to a site `x`, the sum of a discrete gradient is `lambda(x)-lambda(y)`, independently of path. Thus both the averaged-contour map `T` and a rooted-tree map `T0` obey

\[
 TD\lambda=T_0D\lambda=d\lambda,
 \qquad (d\lambda)(y,x)=\lambda(x)-\lambda(y).
\]

On rooted site fields this is exactly `TD=I`. The relevant site norm is the sum over all noncenter sites; extending such a field by zero at the centers preserves that norm.

At the identity, the first differential of the group average is the arithmetic average of the first differentials. Writing the averaged group contour as `exp(i[t TB+O(t^2)])`, the trace expansion gives

\[
 1-\operatorname{Re}\operatorname{tr}\Omega(t)
 ={t^2\over2}\operatorname{tr}(TB)^2+O(t^3).
\]

The order-two logarithmic term is a traceless Hermitian matrix for real variations and contributes no real linear trace. Therefore the quadratic penalty is precisely `||TB||^2/2` in the fixed trace normalization.

This matches the primary definition's derivative, rather than a chosen-tree penalty: CMP109, (0.8) specifies the first derivative of the group average; (0.11) defines the averaged contour; (0.12) uses it in the coarse average; (0.14)--(0.16) use the exponential penalty. [Primary article](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf), pp.253--255. This audit uses only these derivative-level statements, not an unverified nonlinear identity.

The distinction between the tree and averaged slices is real. In a centered two-dimensional block with `L>=3`, use the coordinate-ordered tree whose root paths first change the first coordinate. Set only the off-tree horizontal edge `(0,1)->(1,1)` to a nonzero value. Every tree path integral vanishes; the average of the two prescribed coordinate-order paths to `(1,1)` is nonzero. Thus `ker T0` does not imply `ker T`.

For `h=d(L-1)` and `n=L^d`, each row of either contour matrix has absolute sum at most `h`, and a column has absolute sum at most `n-1`. Every individual simple path uses a bond at most once; averaging cannot increase that count. Hence

\[
 \|T\|,\|T_0\|\le t_0=\sqrt{h(n-1)}.
\]

Counting each positive oriented nearest-neighbor bond once gives

\[
 \|D\lambda\|^2
 \le\sum_{(v,w)}2(|\lambda(v)|^2+|\lambda(w)|^2)
 \le4d\|\lambda\|^2,
\]

so `d0=2 sqrt(d)` is correct. The estimates are conservative; centered shortest paths actually have length at most `d(L-1)/2`, but using the larger `h` is harmless.

## 3. The two flat constraints, with a direct sign check

For a coarse positively oriented bond `c=(y,y+L e_mu)`, set `y'=y+L e_mu`, `x'=x+L e_mu`. The first derivative of its contour expression is

\[
 {1\over L^{d+1}}\sum_{x\in B(y)}
 \left[T_{y,x}B+\int_{[x,x']}B-T_{y',x'}B\right].
\]

The reference-center straight string cancels when the final reference transporter is multiplied back. The endpoint contour term has a minus sign because it is traversed from `x'` to `y'`. Thus

\[
 Q^{\flat}=Q_{\rm st}-D_1aT,
 \qquad Q_1=Q^{\flat}+D_1aT=Q_{\rm st}.
\]

There is a useful independent gradient check. If `m lambda` denotes the block mean and `r lambda` the values at centers, then

\[
 Q_{\rm st}D\lambda=D_1m\lambda,
 \qquad aTD\lambda=m\lambda-r\lambda.
\]

Consequently

\[
 Q^{\flat}D\lambda=D_1r\lambda,
 \qquad Q_1D\lambda=D_1m\lambda.
\]

These confirm both the sign and the `1/L` normalization. Rooted gradients preserve `ker Qflat`; mean-zero gradients preserve `ker Q1`. Confusing the two would invalidate the transfer, but the scratch proof does not make that substitution.

### 3.1 Bijection from the actual constraint to the averaged-contour slice

For `B in ker Qflat`, set `xi=TB`, extended by zero at centers, and `BT=B-Dxi`. Then `TBT=0`, `Qflat BT=0`, and, because the contour term is zero, `Q1 BT=0`. Conversely, any `BT in ker Q1 intersect ker T` and any rooted `xi` produce `B=BT+Dxi in ker Qflat` with `TB=xi`. This proves a bijection with its actual inverse; no rank count is being substituted for existence or uniqueness.

### 3.2 Bijection between the averaged and chosen-tree slices

Let `N` be the block-mean-zero site fields. For a noncenter-pair field `f`, extend it by zero at the centers and define

\[
 d^{-1}f=f-mf.
\]

It belongs to `N`, has `d(d^-1 f)=f`, and

\[
 \|d^{-1}f\|^2=\|f\|^2-\sum_y L^d|m_yf|^2\le\|f\|^2.
\]

Hence, on `ker Q1 intersect ker T`,

\[
 B_0=B_T-Dd^{-1}T_0B_T
\]

belongs to `ker Q1 intersect ker T0`. Its inverse is

\[
 B_T=B_0-Dd^{-1}TB_0.
\]

Indeed `TB0=-T0BT`; applying `d^-1` and substituting gives back `BT`. Both directions have norm at most `a0=1+d0 t0`. These identities and their signs pass.

## 4. Coercivity and full coordinate bounds

Assume the real symmetric action form is invariant under the relevant gradients, and on the tree/mean-constraint slice

\[
 \gamma_{\rm ax}\|B_0\|^2\le q(B_0)\le M_q\|B_0\|^2.
\]

The slice maps above give

\[
 q(B_T)=q(B_0)\ge {\gamma_{\rm ax}\over a_0^2}\|B_T\|^2
 =\gamma_T\|B_T\|^2.
\]

For `B=BT+Dxi`,

\[
 q(B)+\|TB\|^2\ge\gamma_T\|B_T\|^2+\|\xi\|^2,
\]
\[
 \|B\|^2\le
   (\gamma_T^{-1}+d_0^2)
                  (\gamma_T\|B_T\|^2+\|\xi\|^2).
\]

Thus the stated constant is correct:

\[
 \gamma_{\exp}=(\gamma_T^{-1}+d_0^2)^{-1}.
\]

A gauge penalty `a||TB||^2` replaces `d0^2` in the denominator by `d0^2/a`. The factor `1/2` in the Gaussian exponent must be kept separate from this form inequality; the scratch note uses that convention consistently.

For the upper bound, `||BT||<=a0||B||` and `||B0||<=a0||BT||`, so

\[
 q(B)+\|TB\|^2
 \le [M_qa_0^4+t_0^2]\|B\|^2.                       \tag{4.1}
\]

This proves the displayed scratch upper bound. It uses an axial **upper** bound as well as the lower bound; a lower bound alone would not imply a lower covariance bound.

Let `Kflat` be the pivot extension and `Kax` the tree-and-pivot extension. Since the independent vector is a coordinate restriction of the full field,

\[
 \|z\|\le\|Kz\|\le\|K\|\|z\|.                  \tag{4.2}
\]

If the available axial theorem is `q(Kax z)>=gamma_free||z||^2`, then it implies

\[
 \gamma_{\rm ax}\ge {\gamma_{\rm free}\over1+2L^{2d}}
\]

with the extension bound audited below. If its upper estimate is `q(Kax z)<=M_free||z||^2`, one may use `Mq=M_free` in (4.1).

Writing

\[
 r=1+2h/L,\quad
 M_K^2=1+L^{2d}(2d+2)r^2,
\]

the reduced exponential precision obeys

\[
 m_0 I\le A_{\exp}\le M_0 I,
\]
\[
 m_0=\left({(1+2L^{2d})a_0^2\over\gamma_{\rm free}}+d_0^2\right)^{-1},
 \qquad
 M_0=[M_{\rm free}a_0^4+t_0^2]M_K^2.                 \tag{4.3}
\]

These are explicit volume-independent flat constants, conditional on `gamma_free` and `M_free`. For its real flat covariance,

\[
 M_0^{-1}I\le C_{\exp}\le m_0^{-1}I.
\]

For later complex perturbations it is useful to record the separate elementary implication. If the complex symmetric precision is `Aexp+E` with `||E||<=m0/2`, then

\[
 \|C\|\le2/m_0,\qquad
 \operatorname{Herm}C\ge
 {m_0/2\over(M_0+m_0/2)^2}I.                         \tag{4.4}
\]

This follows from `Herm C=C^* Herm(Aexp+E) C`. It is not a proof that the actual independent-current precision has this small perturbation property or an exponential kernel bound.

## 5. Centered odd-L pivots and their uniqueness

Write `L=2m+1`, and use the lift of a block centered at `y` as

\[
 B(y)=y+\{-m,\ldots,m\}^d.
\]

For `c=(y,y+Le_mu)`, the claimed pivot is

\[
 b_0(c)=(y+me_\mu,\ y+(m+1)e_\mu).
\]

In a straight string from `x` to `x+Le_mu`, this bond occurs exactly when all transverse coordinates of `x` equal those of `y`. For each of the `L` possible longitudinal coordinates `x_mu=y_mu+k`, `-m<=k<=m`, the string includes its lower endpoint at `y_mu+m`. Thus precisely `L` strings contribute, each with coefficient `L^(-d-1)`, and the pivot coefficient is `L^-d`.

No other coarse equation contains it. Equations in another direction have no fine `mu`-bond in their straight strings. A translated block in a transverse direction has incompatible transverse coordinates. For the previous longitudinal block, every contributing string ends at or before the lower pivot site and so does not use the pivot bond; for the next block it starts strictly after the lower pivot site. More distant blocks are excluded. Contour terms stay inside individual blocks and never contain this interblock bond.

Therefore the pivot matrix in both `Qst` and `Qflat` is exactly `L^-d I`, not merely diagonally dominant. The extension is unique:

\[
 B_p=-L^dQ_fz,
 \qquad
 \|K_{\flat}\|^2\le1+L^{2d}\|Q^{\flat}\|^2.          \tag{5.1}
\]

The coefficient calculation uses the complete centered block, which is why arbitrary cropped blocks would require rechecking.

For `Qst`, its row sum is one, and a fine bond can occur in the strings for at most two coarse equations. Bounding each such entry by one gives column sum at most two and `||Qst||<=sqrt(2)`. For `Qflat`, the two averaged endpoint-contour terms contribute at most `2h/L` to each row, so its row sum is at most `r`. An internal fine bond can enter contour terms for at most `2d` coarse bonds incident on its block; straight strings add at most two coarse equations. A column sum is therefore at most `(2d+2)r`, and

\[
 \|Q^{\flat}\|\le r\sqrt{2d+2}.
\]

All pivots lie outside the block trees. On the tree slice the tree bonds vanish: tree path integrals zero imply each tree bond is zero by subtracting parent and child integrals. Restricting `Qst` to the remaining nonpivot, nontree coordinates cannot increase its norm. Hence

\[
 \|K_{\rm ax}\|^2\le1+2L^{2d}.
\]

This proves all constants used in (4.3). Lie-algebra multiplicity changes none of these scalar matrix-norm estimates because the flat coefficients act as the identity on the Lie-algebra factor.

### 5.1 Periodic geometry

The argument works on the ordinary periodic block tiling by using coordinate lifts for each block and each positive coarse string. Distinct geometric interfaces must be retained as distinct coarse bonds. In particular, if a periodic direction has only two coarse sites, the two interfaces have the same unordered endpoint pair but are distinct periodic lattice cells; one must not collapse them to a single edge of a simple graph. With this convention the local count and diagonal pivot matrix persist across the seam.

The scratch note assumes distinct block interfaces; that excludes a one-block torus in a direction unless a separate wrapped-cell convention is supplied. No such degenerate case is needed for large-volume applications. It is preferable to impose at least two blocks in each periodic direction, or at least three if one wants to avoid discussing the coarse multigraph convention entirely.

### 5.2 Dirichlet geometry with incident bonds

Let `Lambda` be a union of full blocks. Extend site gauges by zero outside `Lambda`; extend bond fields by zero on bonds with neither endpoint in `Lambda`. A block entirely outside `Lambda` then has no nonzero internal bonds, so its `TB`, `T0B` and blockwise means vanish. Both rooted and mean-zero inverse constructions produce site gauges supported inside `Lambda`, and their gradients lie on the retained incident bonds. Every projection in Sections 3--4 preserves the field space.

For a coarse boundary bond with one center in `Lambda'`, the center-line interface pivot has one endpoint in `Lambda`, so it is retained. The same `L` strings determine its coefficient, even though portions outside the region have zero fluctuation. Coarse equations with both centers outside have zero image because their strings meet only the two exterior blocks. Thus imposing the constraints on incident coarse bonds is equivalent to imposing the full constraint after zero extension.

This proves the boundary version under the exact incident-bond convention. If crossing bonds were instead held fixed, a site gauge nonzero at a boundary site would create a nonzero variation on a forbidden crossing bond, and the argument would fail at that first support-preservation step. The complete-block hypothesis also prevents the mean-subtraction inverse from assigning nonzero values to exterior sites in a partially occupied block.

## 6. Flat stationarity and the Ward identity

At the trivial configuration, a smooth effective action obtained by constrained minimization of the nonnegative Wilson action takes its minimum value zero. Its gradient vanishes, provided the stated minimizing map and local chart exist. Gauge invariance then implies that the Hessian annihilates infinitesimal gauge directions. A nonlinear chart contributes a gradient times its second differential to the transformed Hessian; that term is zero at this stationary reference. Thus the flat action form used in Section 4 is exactly invariant under the required gradients. The source's current-dependent constraint correction vanishes at `(U,J)=(1,0)`.

Away from stationarity the current term must be retained. I checked the BCH signs directly with the scratch convention `U^g(v,w)=g(v)^(-1)U(v,w)g(w)`. Put `a=lambda(v)`, `b'=Ad_U lambda(w)`, `DU lambda=(b'-a)/eta`. The mixed `st` part of

\[
 \log[e^{-ita}e^{i\eta sB}e^{itb'}]
\]

is `-eta st[B,a+b']/2`. Dividing by `i eta` therefore gives the coordinate term `+i st[B,a+b']/2`, exactly as in the note. Gauge invariance implies

\[
 H_U(B,D_U\lambda)=-{i\over2}\langle J_U,[B,a+b']\rangle.
\]

The pure-gauge logarithm has second coordinate derivative `-i[a,b']/eta`. Substituting `B=DU lambda` in the mixed identity gives

\[
 H_U(D_U\lambda,D_U\lambda)
 ={i\over\eta}\langle J_U,[a,b']\rangle,
\]

so the independent pure-gauge calculation agrees. There is no missing factor two or `eta` in these formulas.

For unitary backgrounds the bondwise adjoint action preserves the norm. If `|[X,Y]|<=c_br|X||Y|`, then

\[
 |H_U(B,D_U\lambda)|
 \le {c_{\rm br}\over2}j_*\|B\|
       \left[\sum_{(v,w)}(|\lambda(v)|+|\lambda(w)|)^2\right]^{1/2}
 \le c_{\rm br}\sqrt d\,j_*\|B\|\|\lambda\|.
\]

At unit spacing, `||DU||<=2sqrt(d)`, so the pure term is at most `2 c_br d j_*||lambda||^2`; the cross term carries the additional factor two from expanding the quadratic form. This verifies (6.2)--(6.3) of the audited note. For general spacing the pure estimate has the corresponding `1/eta` factor. The note explicitly restricts that bound to unit spacing.

The deposited manuscript uses the opposite gauge convention; replacing `lambda` by `-lambda` matches it. The current in this identity must be the actual first derivative of the action. A free symbol `J` in a complex analytic carrier need not be that derivative, so the physical Ward identity cannot be used to infer exact invariance of an arbitrary independent-current precision.

## 7. Source matching that is still not supplied by this audit

The primary CMP109 derivative definitions support the contour penalty and the centered constraint calculation. The raw manuscript's five covariance identities and second-order gauge expansion agree with the independent algebra above. Its later positivity proposition explicitly assumes a quantitative exponential-gauge covariance input; quoting that proposition does not independently establish the input.

The following source matches remain distinct obligations:

1. The old CMP99b axial lower and upper bound must apply to the actual flat Hessian with the specified old `Q1`, tree slice and coordinate norm. This audit derives `Qst` from the new contour formula and checks the deposited identification; it has not independently reconstructed the old paper's full operator definition and primary estimate from its original pages.
2. If the primary coordinates differ from the tree-and-interface pivots used here, their extension map must be compared. The explicit constants above only cover the chosen convention.
3. The actual complex free-current precision near `(1,0)` needs a uniform small perturbation or directional-response estimate, in the fixed independent coordinates. Equation (4.4) explains what a sufficiently small operator perturbation would yield; it does not establish that perturbation.
4. Exponential kernel decay, local precision expansions, and scale-uniform constants do not follow merely from finite-dimensional coercivity.
5. These changes of coordinates prove form inequalities. They do not preserve a sharp product cutoff automatically. Any use inside an integral with a fixed cutoff must retain the actual cutoff coordinates or track the transformed region.

Subject to these source interfaces and the boundary conventions above, the audited flat gauge bridge is a correct finite-dimensional coercivity transfer.
