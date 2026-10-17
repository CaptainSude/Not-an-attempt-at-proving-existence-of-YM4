# Actual determinant versus Lüscher–Weisz: verified interface

17 October 2026. Primary-source extraction and an independently checked finite algebraic bridge. No numerical running-coupling coefficient is imported into the actual constrained model here. The detailed gauge-change proof is being recorded separately by the theorem agent.

## 1. Exact repository claim

In the pinned raw I:

* Lines 3896–3898 set \(c_0=11C_{\mathfrak g}\log L/(24\pi^2)\).
* Lines 3901–3929 state a lemma with references to CMP109 (1.22), Theorem 3, and CMP116 (2.41). Part (b) claims
  \[
  \left|\sum_{\ell=1}^k\beta_\ell^0-kc_0\right|\le c_2.
  \]
* Lines 3943–3965 label the subsequent argument an outline, asserting composition of the Gaussian normalizers and preservation of the order-two momentum coefficient under minimizer substitution.
* Lines 3967–3985 introduce, on the same fine lattice and with \(\eta=L^{-k}\),
  \[
  \mathscr R_\eta=
  -\tfrac12\log\det(D_{\rm W}^2+\eta^2)+\log\det(\Delta_0+\eta^2),
  \]
  minus its trivial-background value. The descriptions are Wilson Hessian in background Feynman gauge and Faddeev–Popov operator. The asserted estimates are
  \[
  |B_k-B_k^{\rm ref}|\le\tfrac12 C_{\rm cmp}(L,N),\qquad
  |B_k^{\rm ref}-11C_{\mathfrak g}\log(1/\eta)/(24\pi^2)|
  \le C_{\rm det}(N).
  \]

These are extracted-coefficient estimates, not estimates on entire extensive determinants. This passage does not specify the reference background lift, scalar domain, zero-mode treatment before adding the mass, or exact vector operator at a constrained nonstationary background. The two displayed estimates are distinct obligations.

The earlier source audit in work/renormalized_induction_primary_sources.md distinguishes verified activity-induction conclusions from this additional finite-part assertion. It does not infer that no later proof exists merely because this passage gives an outline.

## 2. Verified primary formulas

[Background field technique and renormalization in lattice gauge theory](https://arxiv.org/pdf/hep-lat/9504006), Nucl. Phys. B452 (1995), 213–233, DOI [10.1016/0550-3213(95)00346-T](https://doi.org/10.1016/0550-3213(95)00346-T):

* Section 2.2 defines the formal vertex functional by a Legendre transform; the shift identity gives \(W[B,0,0,0]=0\).
* Section 5.1, printed pp.12–14, uses anti-Hermitian fields and \(U=e^{g_0aq}e^{aB}\). Equations (5.5)–(5.8) specify background backward-divergence gauge fixing and the ghost action. At \(q=0\), the positive scalar operator is \(-\sum_\mu D_\mu^*D_\mu\); their star denotes backward difference.
* Equation (5.10) gives relative exponential Haar density \(\det J(g_0aq)\).

[Computation of the relation between the bare lattice coupling and the MS coupling in SU(N) gauge theories to two loops](https://arxiv.org/pdf/hep-lat/9505011), Nucl. Phys. B452 (1995), 234–260, DOI [10.1016/0550-3213(95)00338-S](https://doi.org/10.1016/0550-3213(95)00338-S):

* Equations (2.9), (2.15) define the lattice background amplitude \(\nu(p)\). Section 4 sets \(a=1\) and uses massless propagators.
* Printed p.11, equation (5.7), at \(\lambda_0=1\), gives
  \[
  \nu^{(1)}(p)=\frac{N}{16\pi^2}
  \{-\tfrac{11}{3}\log(p^2)+\tfrac{64}{9}\}
  -\frac1{8N}
  +N\{\tfrac5{36}P_1+\tfrac{11}{3}P_2+\tfrac1{16}\}+O(p^2).
  \]
* Appendix B (B2) uses a mass to define the scalar integral constant \(P_2\); it does not state the repository's massive vector/ghost comparison.

The first paper's (5.5)–(5.8) and the second's (5.7) were checked visually in the primary PDFs.

## 3. What is not identified

The massless background one-particle-irreducible amplitude is a reference calculation, not the source-free connected normalizer. A determinant representation of that vertex functional requires the appropriate Legendre/source cancellation of its linear fluctuation term.

The quoted formula does not by itself justify:

1. Replacing nonzero external momentum \(p\) by an infrared mass \(\eta\).
2. Interchanging the zero-momentum second spatial moment at fixed mass with the massless limit.
3. Replacing a based-site ghost by a full-site covariant ghost plus \(\eta^2\).
4. Replacing the constrained Lagrangian Hessian by the ordinary Wilson Hessian.
5. Dropping the coarse-constraint covariance determinant.
6. Converting the conventional \(SU(N)\) amplitude to the repository's normalized trace without tracking field, action, color and extraction normalizations.

The \(-5/3\) logarithm in the ordinary quantum-field self-energy (5.8) is a different amplitude, not automatically the separate vector-determinant contribution claimed by the repository.

## 4. Independently checked finite algebraic bridge

This is our algebra, not a claim attributed to those papers. Transposes use the actual coordinate pairings; physical orthonormal coordinates give ordinary matrices.

At a real constrained stationary background, let \(F(x)=0\) be the relative constraint, \(C=F'(0)\), and \(S'(0)=C^T\lambda\). The relevant Hessian is
  \[
  \mathcal L=S''(0)-\lambda\cdot F''(0).
  \]
Let \(K\) be the retained chart derivative and \(D_b\) the based gauge generator. Based invariance and criticality imply \(CD_b=\mathcal L D_b=0\); the actual contour derivative satisfies \(TD_b=\pm I\).

For a retained linear gauge \(L\), set \(W=R_{\rm free}D_b\). Block Gaussian elimination gives
  \[
  \det(K^T\mathcal L K+L^TL)
  =\det((K^T\mathcal L K)|_{W^\perp})
     \frac{\det(LW)^2}{\det(W^TW)}.
  \]
Thus \(|\det(LW)|/\sqrt{\det(K^T\mathcal L K+L^TL)}\) is gauge independent. The nonorthonormal vertical Jacobian is retained.

Take \(L=D_b^TK\), so \(LW=G_b=D_b^TD_b\). If
  \[
  \widehat Q=\mathcal L+D_bD_b^T+C^TaC
  \]
is positive for a positive coarse penalty \(a\), ambient coarea yields
  \[
  D_{\rm actual}=
  \left[\log\det G_b-\tfrac12\log\det\widehat Q
  -\tfrac12\log\det(C\widehat Q^{-1}C^T)\right]_{\rm background-flat}.
  \]
The pivot determinant is included by coarea, not replaced by a determinant of a rectangular chart derivative. Positive branches extend locally holomorphically. Positivity here is explicit; no uniform large-endpoint neighborhood is inferred.

This is an exact coupled vector, based-ghost and coarse-constraint reduction. It retains the multiplier curvature and does not identify the massive reference. The theorem agent's detailed note handles the actual source chart and measure matching.

## 5. Exact next analytic obligation

After fully defining the reference, a sufficient target is
  \[
  |\beta(D_{{\rm actual},K}-\mathscr R_{K^{-1}})|\le C,
  \tag{5.1}
  \]
uniformly in the composite endpoint, old depth and required structural limits. Both terms must be evaluated on the same coarse background with the same Maxwell normalization.

One stronger sufficient criterion is a uniform weighted second-moment bound on their total background-Hessian difference:
  \[
  \sup_x\sum_y(1+d(x,y)^2)
  \|\mathcal H_K^{\rm diff}(x,y)\|\le C.
  \tag{5.2}
  \]
The fixed Maxwell moment formula then gives (5.1). This requires cancellation in the sum of vector, ghost, coarse-constraint and multiplier-curvature terms; separate absolute estimates can be too large.

A simple obstruction rules out a naive ghost comparison. On a \(K^d\)-site periodic lattice with one pinned site, a function equal to one off that site has Rayleigh quotient
  \[
  \lambda_{\min}(D_b^TD_b)\le\frac{2d}{K^d-1}.
  \]
For \(d=4\), this is \(O(K^{-4})\), while the proposed mass is \(K^{-2}\). It does not disprove the coupled estimate (5.1), but does disprove the simplest separate spectral-equivalence shortcut.

The remaining tasks are therefore a coupled determinant comparison and a mass-versus-external-momentum comparison. No actual running-coupling sign follows yet.
