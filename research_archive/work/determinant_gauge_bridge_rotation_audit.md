# Independent audit: actual determinant gauge/coarea bridge

17 October 2026. Read determinant_gauge_bridge_research.md in full, checking its finite-dimensional identities against the actual retained-coordinate precision, minimum-value, Haar and gauge-insertion inputs. No output files were edited.

**Result: substantive pass.** The bridge is an exact finite identity on the stated real small physical germ and its legitimate holomorphic continuation. It does not establish a uniform large-endpoint comparison with a massive Feynman reference, a beta-function sign, or a running-coupling trajectory.

## 1. The Lagrangian Hessian and gauge replacement

The use of relative coordinates is consistent throughout:
\[
s(x)=S_M(e^{ix}U),\qquad
f(x)=\log(F_K(e^{ix}U)W^{-1})/i.
\]
Surjectivity of \(C=f'(0)\), supplied by the actual invertible pivot blocks, makes the target multiplier unique. The critical Lagrangian Hessian is
\[
L=s''(0)-\lambda\mathbin{\cdot}f''(0).
\]
The exact pivot-chart second derivative is \(-h f''[K_0\,\cdot,K_0\,\cdot]\), so its contribution is precisely the minus multiplier-curvature term. It would be incorrect to replace \(L\) by \(s''\).

The based constraint is invariant, and the critical Lagrangian is based-gauge invariant. Differentiating its gauge identity at its critical point removes the derivative-of-gauge-vector-field term and gives \(LD_b=0\). This statement would not follow for the unconstrained action Hessian at a noncritical ambient background.

The asserted constrained nullspace follows from the established positive \(A_T\), without a hidden positivity hypothesis on the whole ambient \(L\). For \(x\in\ker C\), set
\[
x_0=x+D_bTx.
\]
Since \(TD_b=-I\), one has \(Tx_0=0\), while \(x_0^TLx_0=x^TLx\). Thus the constrained form is nonnegative; a zero requires \(x_0=0\) by positivity of \(A_T\). Its kernel is exactly \(\operatorname{im}D_b\).

The finite gauge-change identity has the correct determinant power. In fixed coordinates \(z=E_0u+V\alpha\), integrating the gauge coordinate produces \(|\det(FV)|^{-1}\). Consequently
\[
|\det(FV)|\det(B_0+F^TF)^{-1/2}
\]
is independent of \(F\). Applying this with \(F_1=TK_0\), \(F_2=D_b^TK_0\) gives
\[
\det A_T^{-1/2}=\det G_b\,\det A_b^{-1/2}.
\]
There is no missing square root or orbit-volume factor. The background-dependent coordinate Jacobian of the common complement is the same on both sides of this pointwise identity.

## 2. Coarea and the actual Haar density

In retained/pivot order, \(x=K_0z+hy\) is triangular with determinant \(\det C_p^{-1}\), and \(Cx=y\). This verifies the first constrained-Gaussian evaluation directly. The density at zero of \(Cx\) under the ambient Gaussian verifies the second. Hence
\[
\det Q_b\,\det(CQ_b^{-1}C^T)=(\det C_p)^2\det A_b.
\]
The combined normalized correction is therefore exactly
\[
{\cal N}_0\!\left[\log\det G_b-\tfrac12\log\det Q_b
                         -\tfrac12\log\det M_b\right].
\]
In particular the coarse constraint determinant cannot be discarded.

The measure convention agrees with the actual saddle amplitude. Input coordinates are left-relative group coordinates, so their Haar density at \(x=0\) is the fixed identity density. The group delta is expressed in the target's relative coordinate at \(W\); right/left Haar invariance makes its density at zero the same fixed identity density. It does not produce \(j(\log W)\). The retained-coordinate Jacobian is the actual inverse pivot. Remaining fixed Haar and gauge-insertion normalizations cancel only in the explicitly normalized amplitude, as asserted.

## 3. Canonical completion and zero modes

The value function uses the same target coordinate:
\[
s_{\rm eff}(y)=S_{MK}(e^{iy}W).
\]
The previously proved local comparison among **all sufficiently nearby fields**, applied to the datum \(F_K(e^{ix}U)\), gives \(s(x)-s_{\rm eff}(f(x))\ge0\). It is stronger than stationarity and is essential. Its zero gradient and Hessian give
\[
H_{\rm res}=L-C^Tq_{\rm eff}C\ge0.
\]
Along the actual minimizing section the residual vanishes. Positive semidefiniteness then gives \(H_{\rm res}H=0\); no flat lift is silently substituted. Full local gauge invariance gives \(H_{\rm res}D_f=0\) by the same critical Ward argument.

For
\[
Q_b=H_{\rm res}+D_bD_b^T+C^TC,
\]
a null vector lies in \(\ker C\cap\ker D_b^T\) and has zero constrained \(L\)-energy. It is therefore \(D_b\alpha\), and \(G_b\alpha=0\) forces zero. This proves finite positive definiteness. It does not require \(q_{\rm eff}\ge0\) or \(I-q_{\rm eff}\ge0\), and gives no uniform large-\(K\) gap.

Basing at every final center makes \(D_b\) injective on a connected graph. Basing the full generator at one final center makes \(D_f\) injective as well. No inverse of an unbased all-site massless ghost is used. If the set of remaining coarse sites is empty, the Schur factors are empty matrices with determinant one; this harmless convention can be made explicit in the fragment.

## 4. Full-site Schur factors and infrared obstruction

The domain-column split \(D_f=[D_b,D_e]\) need not have orthogonal images. The Gram Schur complement correctly uses
\[
S_g=D_e^T(I-D_bG_b^{-1}D_b^T)D_e,
\qquad \det G_f=\det G_b\det S_g.
\]
The determinant lemma gives \(\det Q_f=\det Q_b\det S_v\). Substitution therefore yields the signs
\[
\log\det G_f-\tfrac12\log\det Q_f
-\log\det S_g+\tfrac12\log\det S_v-\tfrac12\log\det M_b.
\]
The canonical comparison identity retains all three differences:
\[
Q_f-P_\eta=-\lambda\mathbin{\cdot}f''
                         +C^T(I-q_{\rm eff})C-\eta^2I.
\]
The first term can have nonzero first and second background derivatives despite vanishing at the identity. Neither coarse rank nor pointwise vanishing bounds its Maxwell moment.

The ghost counterexample is correct. On the flat compatible torus, the scalar equal to one away from the \(K\)-centers and zero on them has norm squared \((K^d-1)n_c\) and gradient energy \(2dn_c\). Thus in \(d=4\), \(\|G_b^{-1}\|\ge(K^4-1)/8\), contradicting a uniform \(O(K^2)\) bound. It does not contradict cancellation in the complete determinant expression.

The proposed \(P_\eta\) comparison must use a specified matched operator and an invertible finite real/complex germ before its individual log determinant is taken. The note already treats it only as an interface and disclaims a common uniform complex radius. Likewise the globally based \(G_f\) is not an all-site translation-invariant massive ghost.

## 5. Scope retained

All logarithmic identities are real positive identities first, normalized at the identity, followed by continuation on compatible branches. The actual combined correction may continue farther than the individual factors. The proof supplies neither uniform control of those individual branches nor a bound on the large-\(K\) Maxwell contribution of the coarse package. The stated remaining comparison problem and its zero-mode qualifications are accurate.

## 6. Additional canonical simplification

The author's subsequently proposed simplification also passes independently. Define
\[
H_b=(I-D_bG_b^{-1}D_b^T)H.
\]
Then \(CH_b=I\), \(D_b^TH_b=0\), and \(H_{\rm res}H_b=0\): the last equality uses both \(H_{\rm res}H=0\) and \(H_{\rm res}D_b=0\). Therefore the **canonical** completion satisfies
\[
Q_bH_b=C^T,\qquad Q_b^{-1}C^T=H_b,\qquad M_b=I.
\]
Its leading correction reduces exactly to \({\cal N}_0[\log\det G_b-\tfrac12\log\det Q_b]\). This does not permit removing \(M_b\) for arbitrary completions; the effective coarse Hessian has instead been incorporated into \(Q_b\). It gives no uniform lower gap or reference-comparison estimate.

The full dgb fragment was read against the research proof: every determinant factor, sign, criticality qualification, measure convention and scope limitation matched.

**Final update fidelity pass.** The saved research and fragment now also identify the compression for a general admissible completion. Indeed \(LH_b=C^Tq_{\rm eff}\), so
\[
Q_bH_b=C^T(q_{\rm eff}+B),\qquad
q_{\rm eff}+B=H_b^TQ_bH_b>0.
\]
Since \(CH_b=I\), this proves \(M_b=(q_{\rm eff}+B)^{-1}\) and the plus sign in the equivalent term \(+\tfrac12\log\det(q_{\rm eff}+B)\). The canonical identity is its \(B=I-q_{\rm eff}\) specialization. This stronger general formula passes as well. The final fragment also explicitly records the empty-determinant convention and invertibility requirement for the proposed reference operator. No correction remains.

## 7. Final added uniform coarse-factor proposition

**The added research §7 and fragment proposition pass substantively and in fidelity.** This is a new uniform estimate for one coarse factor, not a uniform estimate for the entire fine determinant.

I checked the input against the actual strict scalar action theorem: its common-radius anchored bounds are uniform in the entire depth \(MK\). The quadratic baseline has pair carriers and a uniform exponential matrix row bound; a prescribed cardinality reserve on those pairs costs only a fixed factor. For the nonlinear remainder, the stated arbitrary fixed cardinality reserve is already supplied by that theorem on a smaller common radius.

The relative target conversion is local on each coarse bond and has uniformly bounded derivatives on a fixed joint ball. The displayed identity
\[
q_{\rm eff}(w)[u,v]
=D^2S_{MK}(w)[E_wu,E_wv]+DS_{MK}(w)[U_w(u,v)]
\]
correctly keeps the background-current term. Differentiating a scalar carrier twice in the relative increment and up to twice in the background leaves every row, column and source in that carrier. The finite source/row multiplicities are absorbed by the fixed cardinality reserve. Thus the source incidence bounds are consequences of strict support, not an inference from an unrooted operator norm.

More explicitly, with a reduced exponent \(m\), a carrier tree containing \(i,j,x\) satisfies \(d(i,x)+d(j,x)\le2\tau(Y)\). For the mixed source derivative its tree contains \(x,y\), giving \(d(x,y)\le\tau(Y)\). Allocating the available spatial exponent and the cardinality reserve proves the two displayed absolute-entry source bounds uniformly in \(MK\) and volume. The coordinate fiber here is that of a coarse bond, not all microscopic bonds in a \(K\)-block.

For one fixed \(a>2R_\mu\), the weighted Neumann series gives \(\|(q_{\rm eff}+aI)^{-1}\|_\mu\le2/a\). On the real germ \(q_{\rm eff}+aI>0\). The decomposition \(x=\xi+H_by\), \(C\xi=0\), makes the cross term in the corresponding fine completion vanish, because \(Q_bH_b=C^T(q_{\rm eff}+aI)\). Therefore that fine completion is positive; no uniform fine spectral gap follows.

The trace estimate is absolutely summable with the advertised spatial decay. For example, expand the second term as
\[
\sum_{i,j,k,l}(P_c^{-1})_{ij}
       (q_x)_{jk}(P_c^{-1})_{kl}(q_y)_{li}.
\]
The inequality
\[
d(x,y)\le d(x,j)+d(j,i)+d(i,y)
\]
lets the two source-rooted vertex bounds and one inverse-edge weight pay a positive exponential in \(d(x,y)\). The remaining inverse edge is bounded by its Schur norm, and the two complete vertex entry sums are bounded. The first trace uses the mixed source bound directly. Hence the full-logarithm Hessian has uniform exponential decay and a uniformly bounded second displacement moment. The actual finite reference denominators are already bounded below above their established threshold, so the finite normalized Maxwell bound follows too.

The final formulas correctly use \(\dim P_c\), including color dimension, in the vacuum term. They explicitly define \(K_c\) as the **full** normalized log-determinant Hessian and use \(K_c/2\) for the proposition's half-logarithm. The newly used completion is consistently \(B=aI\): its full-site difference is \(-\lambda\cdot f''+aC^TC-\eta^2I\). The earlier \(I-q_{\rm eff}\) formula remains explicitly labeled as the different canonical choice. No completion factors are mixed.

The conclusion is a proved uniform \(O(1)\) bound for \(\beta(\tfrac12{\cal N}_0\log\det(q_{\rm eff}+aI))\), for a fixed sufficiently large \(a\). The fine based vector/ghost combination, or its equivalent full-site/coarse-site package, still requires the separate large-endpoint comparison. No sign conclusion was added.
