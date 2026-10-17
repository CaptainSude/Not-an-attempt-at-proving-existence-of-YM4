# Independent audit: exact finite determinant gauge bridge

17 October 2026. Audited work/determinant_gauge_bridge_research.md, Sections 1–7. **Pass; no mathematical correction.** This is a finite identity and counterexample, not the missing uniform reference comparison.

## Checked identities

1. The coordinates are relative at both the fine saddle and the target. Differentiating the exact constraint chart twice gives the retained action Hessian \(K_0^T(s''-\lambda f'')K_0\), including the full multiplier curvature. No ordinary-log target derivative is substituted.
2. Based invariance makes \(CD_b=0\). Criticality of the invariant Lagrangian, rather than of the unconstrained action, makes \(\mathcal L D_b=0\). Actual contour endpoint covariance supplies \(TD_b=-I\), up to the stated harmless orientation convention.
3. The gauge replacement keeps the same complement-plus-vertical coordinate Jacobian on both sides. Equivalently, an orthonormal complement calculation includes \(\det(V^TV)\); this cancels in the ratio. There is no implicit assumption that the gauge insertion is an isometry. Positivity of the actual contour-gauge precision proves positivity of the physical quotient form and its exact vertical nullspace.
4. In ambient coordinates \((z,y)\mapsto K_0z+hy\), the determinant is \((\det C_p)^{-1}\). The other coarea calculation gives the marginal constraint covariance \(M_b=CQ_b^{-1}C^T\). Therefore \(\det Q_b\det M_b=(\det C_p)^2\det A_b\), with precisely the signs and powers used in (3.4).
5. Relative target Haar has its fixed coordinate density at zero. The formula does not acquire a factor involving the ordinary logarithm of the target field. This agrees with the separately audited actual leading-amplitude normalization.
6. The residual \(S_M(U')-S_{MK}(F_K(U'))\) is nonnegative on a common real neighborhood by the two-minimum comparison, not merely by stationarity. Its Hessian is \(H_{\rm res}=\mathcal L-C^Tq_{\rm eff}C\ge0\). Its full gauge invariance and vanishing along the actual minimum section give (4.2)–(4.3). If the canonical completion in (4.4) has a null vector, its constraint and divergence vanish; the remaining constrained null vector is based-vertical and hence zero. Thus the completion is positive even when \(I-q_{\rm eff}\) is not.
7. For \(K\ge3\), the test scalar equal to one away from centers has exactly \(2d\) differing edges per center. Its norm squared is \(K^d-1\) per center. The resulting \(O(K^{-d})\) upper Rayleigh bound genuinely contradicts a uniform \(O(K^2)\) based-ghost inverse bound in \(d=4\).
8. The full-site Schur factors satisfy \(\det G_f=\det G_b\det S_g\) and \(\det Q_f=\det Q_b\det S_v\). Substitution gives exactly \(-\log\det S_g+\tfrac12\log\det S_v-\tfrac12\log\det M_b\) in (6.3). The canonical expression (6.4), and its difference from the specified candidate mass operator (6.5), are correct.

## Scope retained

Individual logarithms need only a finite local real/complex branch; no endpoint-uniform radius is inferred. The based ghost, globally based ghost and translation-invariant massive ghost remain distinct. All coarse Schur determinants and the constraint-current curvature remain present. Existing fixed-endpoint trace/locality estimates do not provide an endpoint-uniform Maxwell comparison.

The primary-source extraction is recorded separately in work/one_loop_reference_interface_research.md. It confirms that the displayed Lüscher–Weisz massless nonzero-momentum amplitude cannot be imported into this actual finite expression without the stated comparison.

## TeX fidelity and canonical marginal refinement

The full work/determinant_gauge_bridge_fragment.tex was compared with the audited research. It preserves the relative target coordinate, multiplier term, all determinant powers, nonorthogonal orbit-density argument, canonical completion and all three general coarse correction factors. Fidelity passes.

The subsequently proposed canonical refinement also passes independently. Define \(H_b=H-D_bG_b^{-1}D_b^TH\). Then \(CH_b=I\), \(H_{\rm res}H_b=0\), and \(D_b^TH_b=0\). For the canonical \(Q_b=H_{\rm res}+D_bD_b^T+C^TC\), these imply \(Q_bH_b=C^T\), hence \(CQ_b^{-1}C^T=I\) exactly. Thus the coarse covariance determinant is one for this particular completion. The general formula remains correct; the coarse effective Hessian is now incorporated in \(H_{\rm res}=\mathcal L-C^Tq_{\rm eff}C\), rather than being discarded.

The final stronger general-completion addition was also checked in both research and TeX: \(Q_bH_b=C^T(q_{\rm eff}+B)\), while \(H_b^TQ_bH_b=q_{\rm eff}+B>0\). Hence \(M_b=(q_{\rm eff}+B)^{-1}\), and its contribution has sign \(+\tfrac12\log\det(q_{\rm eff}+B)\). The canonical identity is its exact specialization. The stated empty coarse-site determinant convention is consistent.
