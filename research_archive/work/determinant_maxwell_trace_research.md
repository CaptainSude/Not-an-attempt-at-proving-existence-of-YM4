# The actual pivot/Gaussian drift: an explicit Hessian trace formula

17 October 2026. Research derivation for independent audit. The objects are those of the selected homogeneous composite macrostep, with primitive ratio fixed, composite ratio \(R\) fixed, arbitrary preceding classical depth \(M\), and the actual retained-coordinate chart and direct-\(R\) internal contour gauge. The finite-regulator formulas below are exact. Infinite-volume statements concern a chosen joint local-limit system with the already proved uniform exponential bounds. No sign, numerical value, old-depth limit, or universal beta coefficient is asserted.

## 1. Exact objects and normalizations

Use normalized trace-orthonormal real Lie coordinates, complexified bilinearly. Current link angles are \(a\), final coarse link angles are \(w\), and final spacing is reset to one only for the output momentum convention. All retained-coordinate matrix traces use the Euclidean counting coordinates of the actual Gaussian integral. They do not use an extra old fine-volume factor.

The following definitions are fixed by the exact integral:

* composite_macrostep_integral_research.md, Sections 1 and 4: the relative constraint \(F_a(B)=\log[F_R(e^{iB}e^{ia})F_R(e^{ia})^{-1}]/i\), its derivative \(C_a=D_BF_a(0)\), and its unique own-pivot block
  \[
  (C_a)_{c,p(c)}=R^{1-d}\pi_c(a),\qquad \pi_c(0)=I;
  \]
* the corresponding pivot insertion \(h_a\), retained kernel insertion \(K_a=E_{\rm free}-h_aC_aE_{\rm free}\), and exact retained chart \(\Phi_a(z)\), with
  \[
  C_ah_a=I,\quad D_z\Phi_a(0)=K_a,\quad
  D_z^2\Phi_a(0)[u,v]=-h_aD_B^2F_a(0)[K_au,K_av];
  \]
* the actual absolute contour gauge function \(G_R\), not a relative gauge penalty;
* the physical centered branch \(a_*(w)\), with \(a_*(0)=0\), composite constraint \(F_R(e^{ia_*(w)})=e^{iw}\), and contour variables \(P_R(e^{ia_*};y,x)=I\).

To avoid confusing the ordinary scalar action with the relative constraint, write
\[
 \mathcal W_M(a)=S_M(e^{ia})+G_R(e^{ia}),\qquad
 f(a,z)=\frac1i\log[e^{i\Phi_a(z)}e^{ia}].
 \tag{1.1}
\]
Then \(f(a,0)=a\), and the independent-background retained precision is
\[
 \mathscr A_M(a)=D_z^2[\mathcal W_M(f(a,z))]_{z=0}.
 \tag{1.2}
\]
This is the full analytic precision on the independent background ball. At nonphysical backgrounds it need not center the Gaussian. Its restriction
\[
 A(w)=\mathscr A_M(a_*(w)),\qquad A_0=\mathscr A_M(0),\qquad C_0=A_0^{-1}
 \tag{1.3}
\]
is the centered precision in the actual macro integral.

The exact external logarithms, as in common_domain_macrostep_fragment.tex, equation cdm-external-logs, are
\[
 \Delta(w)=-\sum_c\log\det\pi_c(a_*(w)),\qquad
 \mathcal Q_{\det}(w)=-\frac12\log\det[A(w)A_0^{-1}].
 \tag{1.4}
\]
The factor \(R^{1-d}\) cancels between each pivot determinant and its value at zero. The determinant branches in (1.4) vanish at zero. Define \(D_M=\Delta+\mathcal Q_{\det}\).

The signs in (1.4) follow from the inverse pivot Jacobian and the Gaussian factor \(\det A^{-1/2}\), respectively. No background Haar factor \(j(a_*)\) should be added: the exact link Haar coordinates are left-relative, with \(j(\Phi_a(g\xi))\), whose logarithm vanishes at \(g=0\). The fluctuation straightening ratio likewise equals one at \(\xi=0\). The gauge-insertion constant \(c(g)^{-n_s}\), powers of \(g\), and flat Gaussian constants are field-independent and are outside \(D_M\).

All statements here retain the actually chosen mean, composite constraint, pivots and contour gauge. Replacing the composite map by a direct-\(R\) average or replacing the retained precision by an axial covariance would change the formula.

## 2. Complete finite-regulator chain rule

For final coarse directions \(u,v\), put
\[
 H_u=Da_*(0)u,\qquad B_{uv}=D^2a_*(0)[u,v].
 \tag{2.1}
\]
Define independent-background derivatives
\[
 \begin{split}
 \mathscr A_1[p]&=D\mathscr A_M(0)[p],&
 \mathscr A_2[p,q]&=D^2\mathscr A_M(0)[p,q],\\
 \pi_{c,1}[p]&=D\pi_c(0)[p],&
 \pi_{c,2}[p,q]&=D^2\pi_c(0)[p,q].
 \end{split}
 \tag{2.2}
\]
The derivatives along the physical branch are exactly
\[
 \begin{split}
 A_u&=\mathscr A_1[H_u],\\
 A_{uv}&=\mathscr A_2[H_u,H_v]+\mathscr A_1[B_{uv}],\\
 \pi_{c,u}&=\pi_{c,1}[H_u],\\
 \pi_{c,uv}&=\pi_{c,2}[H_u,H_v]+\pi_{c,1}[B_{uv}].
 \end{split}
 \tag{2.3}
\]
Jacobi's logarithmic derivative and \(D(A^{-1})[B]=-A^{-1}BA^{-1}\) give
\[
 \boxed{\begin{split}
 D^2D_M(0)[u,v]
 ={}&-\sum_c\operatorname{tr}
       \{\pi_{c,uv}-\pi_{c,u}\pi_{c,v}\}\\
 &-\frac12\operatorname{Tr}
       \{C_0A_{uv}-C_0A_uC_0A_v\}.
 \end{split}}
 \tag{2.4}
\]
Lowercase trace acts on one pivot color block; uppercase trace acts on all retained coordinates. Products need not commute. Cyclicity of the trace makes (2.4) symmetric in \(u,v\).

This is already an exact finite-regulator answer, including every implicit background derivative. In particular, constrained stationarity does not say that the left current of \(S_M\) is zero. It cannot justify dropping the constraint-curvature terms inside \(\mathscr A_1\) or \(\mathscr A_2\).

## 3. Global color symmetry removes only the second stationary response

Introduce the independent-background scalar
\[
 d_M(a)=-\sum_c\log\det\pi_c(a)
         -\frac12\log\det[\mathscr A_M(a)A_0^{-1}].
 \tag{3.1}
\]
It is not asserted to be invariant under arbitrary local background gauges. It is invariant under constant simultaneous color conjugation.

Indeed let \(O=\operatorname{Ad}_k\) in the fixed real orthonormal Lie basis. Endpoint covariance of the actual averages gives
\[
 \pi_c(Oa)=O\pi_c(a)O^{-1}.
 \tag{3.2}
\]
The unique small pivot chart is equivariant because both its constraint and retained-coordinate prescription are equivariant. The absolute contour gauge is a sum of class functions, and the actual scalar action is invariant under global conjugation. Therefore
\[
 \mathscr A_M(Oa)=O_{\rm ret}\mathscr A_M(a)O_{\rm ret}^{\,T},
 \qquad O_{\rm ret}^{\,T}O_{\rm ret}=I.
 \tag{3.3}
\]
The flat precision commutes with \(O_{\rm ret}\). Equations (3.2)–(3.3) prove (3.1)'s invariance first on the real domain and then on its complex continuation, with the zero-at-origin logarithmic branches.

For a semisimple Lie algebra, there is no invariant linear functional on any one adjoint color slot. Applying global conjugation to a variation supported on one current bond thus gives
\[
 Dd_M(0)[p]=0
 \quad\text{for every current variation }p.
 \tag{3.4}
\]
This applies separately to the pivot sum and the Gaussian trace logarithm. On a finite regulator it is elementary finite-dimensional invariant theory; the summable extension is justified below.

Substitute (2.3) into (2.4). The coefficient of \(B_{uv}\) is exactly \(Dd_M(0)[B_{uv}]\), so it vanishes. Hence the useful reduced formula is
\[
 \boxed{\begin{split}
 D^2D_M(0)[u,v]
 ={}&-\sum_c\operatorname{tr}
 \{\pi_{c,2}[H_u,H_v]
       -\pi_{c,1}[H_u]\pi_{c,1}[H_v]\}\\
 &-\frac12\operatorname{Tr}
 \{C_0\mathscr A_2[H_u,H_v]
       -C_0\mathscr A_1[H_u]C_0\mathscr A_1[H_v]\}.
 \end{split}}
 \tag{3.5}
\]
The cancellation uses the scalar trace and global symmetry. It does **not** say \(\mathscr A_1=0\), \(\pi_{c,1}=0\), or that the current-curvature operator terms vanish. For a group with an abelian factor, retain the full formula (2.4) unless its linear functional has been separately shown to vanish.

## 4. The actual flat stationary lift and its second response

The first response in (3.5) is explicit in the proved flat operators. Let
\[
 C_R=D_a\{\log F_R(e^{ia})/i\}_{a=0},\qquad
 h=h_0,\qquad K=K_0,\qquad
 P_M=q_M+T_R^TT_R.
 \tag{4.1}
\]
Here \(q_M\) is the ordinary homogeneous classical Hessian, and \(T_R\) is the linearized direct-\(R\) internal contour map. The constraint is still the composite map \(F_R\). With the exact angle/counting normalization,
\[
 A_0=K^TP_MK,\qquad
 B_M=K^TP_Mh=K^Tq_Mh,\qquad
 H=h-KC_0B_M.
 \tag{4.2}
\]
The simplification uses \(T_Rh=0\), because every contour is internal and uses no pivot.

To prove (4.2), use the local affine identity-background chart
\[
 \mathfrak a(w,z)=Kz+hw-h\,\mathcal C_R(\mathfrak a(w,z)),
 \quad
 \log F_R(e^{ia})/i=C_Ra+\mathcal C_R(a),
 \quad \mathcal C_R(0)=D\mathcal C_R(0)=0.
 \tag{4.3}
\]
Put \(\mathcal T_M(w,z)=\mathcal W_M(\mathfrak a(w,z))\). Its retained stationarity equation has linearization
\[
 D_z\mathcal T_M(w,z)=A_0z+B_Mw+O((|w|+|z|)^2).
 \tag{4.4}
\]
The positive flat retained Hessian and the proved local uniqueness identify its analytic critical point with the physical branch. Therefore \(z_u=-C_0B_Mu\) and \(Da_*(0)u=hu+Kz_u\), proving (4.2). There is no \(M^d\) or \(R^d\) transpose factor in these angle-coordinate matrices.

For completeness the second response omitted from (3.5) is also determined, rather than assumed zero. Let \(t_u=(u,z_u)\), and define \(z_{uv}\) by
\[
 A_0z_{uv}
 =-\bigl[\zeta\mapsto
    D^3\mathcal T_M(0)[(0,\zeta),t_u,t_v]\bigr].
 \tag{4.5}
\]
The bracket denotes its retained-coordinate vector under the counting pairing. Then
\[
 B_{uv}=-h\,D^2\mathcal C_R(0)[H_u,H_v]+Kz_{uv}.
 \tag{4.6}
\]
Equations (4.5)–(4.6) follow by twice differentiating the retained stationarity equation and (4.3). They also apply if the symmetry cancellation is unavailable.

## 5. Explicit precision vertices, including both chart curvatures

Define
\[
 E_a=D_zf(a,0),\qquad T_a=D_z^2f(a,0).
 \tag{5.1}
\]
With \(J_aX=\int_0^1\operatorname{Ad}(e^{ita})X\,dt\) on each current bond and \(\Xi_a(B)=\log(e^{iB}e^{ia})/i\), these are
\[
 \begin{split}
 E_a&=J_a^{-1}K_a,\\
 T_a[u,v]&=-J_a^{-1}h_aD_B^2F_a(0)[K_au,K_av]
             +D_B^2\Xi_a(0)[K_au,K_av].
 \end{split}
 \tag{5.2}
\]
Thus (1.2), at arbitrary independent background, is precisely
\[
 \mathscr A_M(a)[u,v]
   =D^2\mathcal W_M(a)[E_au,E_av]
          +D\mathcal W_M(a)[T_a(u,v)].
 \tag{5.3}
\]
The first term in \(T_a\) is nonlinear constraint curvature; the second is conversion from the left-relative exponential coordinate to the ordinary link logarithm. The absolute gauge function is inside \(\mathcal W_M\), so its nonphysical background curvature is also present. At the physical branch its gauge gradient vanishes, but differentiating an arbitrary-background analytic family must not replace it by a background-relative quadratic form.

Write \(W_n=D^n\mathcal W_M(0)\), so \(W_1=0\), \(W_2=P_M\), \(E_0=K\). Let \(E_1[p]=D_aE_0[p]\), \(E_2[p,q]=D_a^2E_0[p,q]\), \(T_0=T_{a=0}\), and \(T_1[p]=D_aT_0[p]\). For retained directions \(r,s\), differentiation of (5.3) gives
\[
 \begin{split}
 \mathscr A_1[p][r,s]
 ={}&W_3[p,Kr,Ks]
 +W_2[E_1[p]r,Ks]+W_2[Kr,E_1[p]s]\\
 &+W_2[p,T_0(r,s)].
 \end{split}
 \tag{5.4}
\]
The last term is already a first-background-order current/constraint contribution. Its presence is compatible with \(W_1=0\).

The second precision vertex is
\[
 \begin{split}
 \mathscr A_2[p,q][r,s]
 ={}&W_4[p,q,Kr,Ks]\\
 &+W_3[p,E_1[q]r,Ks]+W_3[p,Kr,E_1[q]s]\\
 &+W_3[q,E_1[p]r,Ks]+W_3[q,Kr,E_1[p]s]\\
 &+W_2[E_2[p,q]r,Ks]+W_2[Kr,E_2[p,q]s]\\
 &+W_2[E_1[p]r,E_1[q]s]
       +W_2[E_1[q]r,E_1[p]s]\\
 &+W_3[p,q,T_0(r,s)]\\
 &+W_2[p,T_1[q](r,s)]
       +W_2[q,T_1[p](r,s)].
 \end{split}
 \tag{5.5}
\]
No \(W_1D_a^2T\) term survives at zero. The formulas require only the actual classical action through degree four and the local constraint/exponential chart through the displayed derivatives. All operations in (5.2) use the given finite-dimensional group logarithm and the given averaging mean; they are finite-range at fixed \(R\). The pivot derivatives in (3.5) follow by differentiating
\[
 \pi_c(a)=R^{d-1}(D_BF_a(0))_{c,p(c)}
 \tag{5.6}
\]
twice. Equations (5.2)–(5.6) fix the vertices without a coordinate or gauge replacement.

### 5.1 Obtaining the classical cubic and quartic vertices without a hidden nonlinear solve

The uniform old-\(M\) action vertices in (5.4)–(5.5) can be evaluated from the already proved corrected fixed-slice simultaneous equations. This avoids applying the ordinary rooted average's potentially large physical adjoint.

Use the established fine extension \(\mathcal H_M\), constrained Green operator \(\mathcal C_M\), flat coarse Hessian \(q_M\), corrected constraint remainder \(\mathcal R_M\), Wilson jet \(f_\eta\), and its finite jet map \(\mathcal S\). With physical fine transposes and measures, the exact pair \(Y=(A,m)\) obeys
\[
 \begin{split}
 A={}&\mathcal H_M a-\mathcal H_M\mathcal R_M(A)
       -\mathcal C_M\mathcal S^T f_\eta(\mathcal SA)
       +\mathcal C_M D\mathcal R_M(A)^Tm,\\
 m={}&q_Ma-q_M\mathcal R_M(A)
       +(\mathcal S\mathcal H_M)^Tf_\eta(\mathcal SA)
       -\mathcal H_M^TD\mathcal R_M(A)^Tm.
 \end{split}
 \tag{5.7}
\]
Write this \(Y=\mathcal L_Ma+\mathcal V_M(Y)\), where
\(\mathcal L_M=(\mathcal H_M,q_M)\) and
\(\mathcal V_M(0)=D\mathcal V_M(0)=0\).
Let \(\mathcal V_n=D^n\mathcal V_M(0)\). Its first three responses are therefore exactly
\[
 \begin{split}
 Y_1[u]&=\mathcal L_Mu,\\
 Y_2[u,v]&=\mathcal V_2[\mathcal L_Mu,\mathcal L_Mv],\\
 Y_3[u,v,t]&=\mathcal V_3[\mathcal L_Mu,\mathcal L_Mv,\mathcal L_Mt]\\
 &\quad+\mathcal V_2[Y_2[u,v],\mathcal L_Mt]
       +\mathcal V_2[Y_2[u,t],\mathcal L_Mv]
       +\mathcal V_2[Y_2[v,t],\mathcal L_Mu].
 \end{split}
 \tag{5.8}
\]
There is no factorial missing: these are derivatives, not Taylor coefficients. The scalar envelope identity \(DS_M(a)=m(a)\), and equality of the corrected and ordinary action values, give
\[
 D^3S_M(0)[u,v,t]=\langle (Y_2[u,v])_m,t\rangle,\qquad
 D^4S_M(0)[u,v,t,r]=\langle (Y_3[u,v,t])_m,r\rangle.
 \tag{5.9}
\]
Add the explicit local derivatives of \(G_R\) to obtain \(W_3,W_4\).

These are finite compositions of the previously bounded propagators and finite-range analytic vertices. The derivative summations are in complete physical cell spaces with smooth supported reconstruction; their bounds do not sum unweighted \(M^4\) microscopic coordinate entries. The fine \(\eta^4\) measure remains in the physical transposes in (5.7). It must not be inserted a second time into the retained-coordinate traces of (3.5).

## 6. Absolute convergence and local infinite kernels

The existing strict precision theorem supplies symmetric pieces with matrix support inside their carrier and an analytic row bound of the form
\[
 \sup_i\sum_{Y\ni i}\sum_{j\in Y}
 e^{\sigma\tau(Y)+a|Y|}
 \|(\mathscr A_M-A_0)_{Y,ij}\|_\rho\le N,
 \tag{6.1}
\]
at fixed positive \(\sigma,a,\rho\), uniformly in old depth and permitted volume. The precision composition theorem gives the same kind of bound after substitution of \(a_*(w)\). The matrix rows stay rooted in the original carrier. The flat covariance has a uniform exponential Schur bound. The local pivot scalar and stationary field have their proved strict and rooted bounds.

Here is why these inputs suffice for the traces, rather than merely for a formal determinant series. For a background coordinate \(x\), Cauchy bounds a first source derivative by a fixed constant times \(\rho^{-1}\) on precisely those carriers that contain \(x\). A second derivative has the same assertion with \(\rho^{-2}\) and carriers containing both source slots. Reduce the spatial exponent. For each matrix row \(i\), the unused exponent pays \(e^{-\delta d(i,x)}\), because \(\tau(Y)\ge d(i,x)\) when \(i,x\in Y\). Summing \(i\) is bounded by the lattice sum \(S_\delta\), uniformly also on a periodic graph. To retain exponential decay in a second source separation, spend another exponent portion using \(\tau(Y)\ge d(x,y)\).

Consequently, for basis source directions \(e_x,e_y\), the composed matrices \(A_x,A_{xy}\) have finite absolute-entry trace norms, with an exponential source-root bound. In particular, with a possibly smaller \(m>0\),
\[
 \begin{split}
 \sum_{ij}e^{m[d(i,x)+d(j,x)]}\|(A_x)_{ij}\|&\le C_1,\\
 \sum_{ij}\|(A_{xy})_{ij}\|&\le C_2e^{-m d(x,y)}.
 \end{split}
 \tag{6.2}
\]
For the first line, use
\(d(i,x)+d(j,x)\le2\tau(Y)\), retaining a further exponent spare for the row sum. Formula (6.2) includes the finite color/fiber multiplicities. Applying the same argument to independent-background derivatives and the exponentially decaying external lift \(H\) proves corresponding bounds for the terms in (3.5). Thus these statements do not depend on cancellation of non-absolutely convergent quantities.

The first trace in (2.4) is absolutely bounded using the entry bound for \(A_{xy}\) and the uniform entry envelope for \(C_0\). For the second, expand
\[
 \operatorname{Tr}(C_0A_xC_0A_y)
   =\sum_{i,j,k,l}\operatorname{tr}
        (C_{0,ij}(A_x)_{jk}C_{0,kl}(A_y)_{li}).
 \tag{6.3}
\]
The two source-root bounds and the covariance envelope make this sum absolutely convergent. For example, spend the \(x\)-root weight at \(j\), the covariance weight along \(j\) to \(i\), and the \(y\)-root weight at \(i\); their distances bound \(d(x,y)\). The remaining factors are absolutely summable. This gives
\[
 |\operatorname{Tr}(C_0A_xC_0A_y)|\le C_3e^{-m' d(x,y)}
 \tag{6.4}
\]
after another fixed exponent reduction. The pivot traces have the same conclusion, either by their local precomposition dependence and the rooted stationary family or directly by their composed scalar strict expansion.

Therefore the Hessian kernel \(\mathcal K_{xy}=D^2D_M(0)[e_x,e_y]\) obeys
\[
 \sup_x\sum_y e^{m''d(x,y)}|\mathcal K_{xy}|\le C_D.
 \tag{6.5}
\]
All constants may depend on the fixed \(R,J\), analytic radii and color, but are uniform in old depth and volume under the earlier input bounds. Grouping retained coordinates into auxiliary \(J\)-cells only regroups the same trace; it introduces no extra multiplicative \(J^d\) into the exact formula.

On the infinite lattice, the total log determinant at a noncompact background need not exist as an extensive number. Equations (2.4) and (3.5) concern derivatives on compact or summable variation directions and their local kernels. They are defined by the absolutely convergent trace sums just proved, or by any chosen joint local limit of the actual finite matrices and vertices. The dominated bounds permit passage to that limit. No equality between an arbitrary finite activity and the periodization of a selected infinite one is assumed.

## 7. A convergent Maxwell moment of the explicit traces

Assume the chosen infinite total has the already proved translation, hypercubic and local gauge identities, and take one simple color factor. The midpoint Hessian symbol has
\[
 \widehat{\mathcal K}_{\mu\nu}^{ab}(p)
  =\delta^{ab}\beta(D_M)
      (|p|^2\delta_{\mu\nu}-p_\mu p_\nu)+O(|p|^4).
 \tag{7.1}
\]
For \(\mu\ne\nu\), choose any one normalized color basis vector \(t^a\), and let \(e_{x,\mu,a}\) be the corresponding final unit-spacing link direction. For diagonal orientation \(\mu,\mu\), the two midpoint offsets cancel. Hence
\[
 \boxed{\quad
 \beta(D_M)=-\frac12\sum_{r\in\mathbb Z^4}r_\nu^2\,
    D^2D_M(0)[e_{0,\mu,a},e_{r,\mu,a}].
 \quad}
 \tag{7.2}
\]
There is no color sum in this convention. Hypercubic and color symmetry make the allowed choices equivalent. The sign follows from differentiating \(e^{ip\cdot r}\) twice, and the factor \(1/2\) extracts the coefficient of \(p_\nu^2\). The actual classical reference has coefficient one in this same normalization.

Substituting (3.5) gives the requested explicit operator expression:
\[
 \begin{split}
 \beta(D_M)
 ={}&\frac12\sum_r r_\nu^2\sum_c\operatorname{tr}
 \{\pi_{c,2}[H_0,H_r]-\pi_{c,1}[H_0]\pi_{c,1}[H_r]\}\\
 &+\frac14\sum_r r_\nu^2\operatorname{Tr}
 \{C_0\mathscr A_2[H_0,H_r]
       -C_0\mathscr A_1[H_0]C_0\mathscr A_1[H_r]\},
 \end{split}
 \tag{7.3}
\]
where \(H_r=H e_{r,\mu,a}\). Every sum in (7.3) is absolutely convergent by Section 6. Truncating the external displacement at distance \(L\) has error at most \(C_{m_1}e^{-m_1L}\) for any \(0<m_1<m''\). Internal trace tails similarly admit exponential estimates after anchoring the sources and spending a spare exponent.

For an actual finite regulator, (2.4) and (3.5) remain exact. Apply the already defined symmetric short-lift Hessian moment and divide by the moment of the actual finite reference to obtain \(\beta_{M,N}(D_M)\). Its reference denominator is \(1+O(e^{-cN})\), not automatically exactly one. A finite Ward identity at discrete momenta is not being analytically interpolated to obtain (7.1). The infinite formula requires the stated infinite kernel and symmetries, or the separately justified local-limit passage.

## 8. What this reduction supplies

The leading zero-input drift is now specified by a convergent combination of:

1. actual local pivot vertices through second background order;
2. the actual flat stationary lift (4.2);
3. the flat retained covariance;
4. the full precision vertices (5.4)–(5.5), with the classical cubic/quartic vertices computable by (5.7)–(5.9).

The signs and all coordinate normalizations are fixed. The second physical stationary response is included in the full chain rule and removed only by a proved semisimple global-color identity. The result does not replace the physical current by an independently adjustable source, omit either chart-curvature term, or assume a sign for the competing trace terms.

Further work is needed to evaluate (7.3), compare its values as \(M\) grows, determine any sign or universal coefficient, and control the physical coupling trajectory. These questions are not answered by the trace identity or by its absolute convergence.
