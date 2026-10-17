# Direct Hessian bound for the Gaussian cutoff logarithm

Research note, 16 October 2026. The theorem below is conditional on quantitative covariance and source-response hypotheses, and is proved using the finite-volume Gaussian cluster theorem of Notebook 03. It does not assume a strictly local decomposition in background variables. The repository and output notebooks were not modified.

## 1. Main conclusion

For an exponentially decaying, uniformly accretive complex Gaussian, a sharp-cutoff logarithm has a two-source Hessian bounded by
\[
 |D_xD_yF_{\rm cut}|\le C_{\rm H}\tau_R e^{-\lambda d(x,y)}.
 \tag{1.1}
\]
Here \(\tau_R=O(e^{-c_RR^2})\), the constants are volume independent, and the sources may be finite-support affine variations of the precision. More generally it suffices to control the first and second covariance responses as in §4. A nonzero second variation of the precision must be included.

This can bypass strict background-support activities for the scalar quadratic coefficient alone, once the total Hessian is identified with the deposited pointed sum and the infinite-volume limit is justified. It does not supply local effective actions for the full RG induction.

## 2. Geometry and a common cluster majorant

Let \(\Lambda\) be a finite subset, or a finite periodic version, of a countable metric lattice. Assume uniform bounded geometry:
\[
 S_\gamma:=\sup_x\sum_{i\in\Lambda}e^{-\gamma d(x,i)}<\infty
 \quad(\gamma>0),
 \tag{2.1}
\]
with bounds independent of volume. There are \(D\) real components per site, where \(D\) is fixed. Let
\[
 C=C^T,\qquad \operatorname{Re}C\ge cI,\qquad
 \|C\|\le K,\qquad \|C_{ij}\|\le K_0e^{-\mu d(i,j)}.
 \tag{2.2}
\]
The real Gaussian variables have this complex symmetric covariance; determinant branches are continued from positive real covariances. Fix measurable \(q_i\), independent of the background, with
\[
 |q_i(x_i)|\le{\bf1}_{|x_i|>R}.
\]
The pure sharp cutoff corresponds to \(q_i=-{\bf1}_{|x_i|>R}\). Define
\[
 F_\Lambda(C)=\log\mathbb E_C\prod_{i\in\Lambda}(1+q_i).
 \tag{2.3}
\]

Fix
\[
 \nu=\mu/2,\quad 0<\kappa<\nu,\quad
 \rho={c\over8S_\nu}.
 \tag{2.4}
\]
If symmetric matrices \(E,F\), possibly supported on a subset of coordinates, satisfy
\[
 \|E_{ij}\|,\ \|F_{ij}\|\le e^{-\nu d(i,j)},
 \tag{2.5}
\]
then for \(|z|,|w|\le\rho\), Schur's bound gives
\(\|zE+wF\|\le2\rho S_\nu=c/4\). Thus all perturbed covariances satisfy the safe bounds
\[
 \operatorname{Re}(C+zE+wF)\ge c_0I,\quad
 \|C+zE+wF\|\le K_0^{\rm op},\quad
 \|(C+zE+wF)_{ij}\|\le L_0e^{-\nu d(i,j)},
 \tag{2.6}
\]
where
\[
 c_0=c/2,\quad K_0^{\rm op}=K+c/2,\quad L_0=K_0+2\rho.
\]
The superscript on \(K_0^{\rm op}\) distinguishes this norm constant from the original kernel constant \(K_0\).

Use the Gaussian polymer theorem with these safe constants. Its internal derivative margin gives
\[
 c_1=c/4,\qquad K_1=K+3c/4,\qquad
 K_{\rm tr}={8e^2\over c_0}={16e^2\over c},
\]
\[
 \tau_R=2^{D/2}(K_1/c_1)^D
          \exp[-c_1R^2/(4K_1^2)],
 \qquad
 A_\kappa^*=L_0\sup_i\sum_{j\ne i}e^{-(\nu-\kappa)d(i,j)}.
 \tag{2.7}
\]
Choose any fixed \(\alpha>0\), and require
\[
 r_*={27\over4}e^\alpha\tau_RK_{\rm tr}A_\kappa^*
       \le\tfrac12,\qquad
 2e^\alpha\tau_R\le\alpha.
 \tag{2.8}
\]
These hold for all sufficiently large \(R\).

The important addition to the usual theorem is a single, background-independent positive majorant. Put
\[
 u(S)=
 \begin{cases}
 \tau_R,& |S|=1,\\
 \tau_R^{|S|}K_{\rm tr}^{|S|-1}
 \displaystyle\sum_{T\ {\rm tree\ on}\ S}
   \prod_{i\in S}d_i(T)!
   \prod_{\{i,j\}\in T}L_0e^{-\nu d(i,j)},& |S|\ge2.
 \end{cases}
 \tag{2.9}
\]
For every covariance in (2.6), the tree proof bounds its activity on \(S\) by this same \(u(S)\), term by term. Define
\[
 M(X)=\sum_{n\ge1}{1\over n!}
 \sum_{\substack{S_1,\ldots,S_n\ne\varnothing\\
                   \cup_jS_j=X}}
 |\phi^T(S_1,\ldots,S_n)|\prod_{j=1}^nu(S_j),
 \tag{2.10}
\]
where \(\phi^T\) is the usual hard-core Ursell coefficient and repeated polymers are allowed. The anchored tree sum and pinned polymer bound give
\[
 \sup_z\sum_{X\ni z}e^{\kappa\ell(X)}M(X)
 \le M_0,\qquad M_0=2e^\alpha\tau_R.
 \tag{2.11}
\]
Here \(\ell(X)\) is the minimum spanning-tree length. This is exactly the positive majorant argument in the proof of the logarithm theorem, now with fixed edge weights \(L_0e^{-\nu d}\).

Write \(F_\Lambda(C)=\sum_Xe_X(C)\), collecting clusters by their union of marked sites. Each \(e_X\) depends on \(C\) only through \(C_{XX}\), although \(C_{XX}\) can depend on remote background data. For every allowed perturbation in (2.6),
\[
 |e_X(C+zE+wF)|\le M(X).
 \tag{2.12}
\]
The same majorant works for every \(X\); it is not a separate bound whose sum of suprema is uncontrolled.

## 3. Proved: directional Cauchy estimates retaining the common majorant

For symmetric directions \(E,F\) on \(X\), let
\[
 \|E_{ij}\|\le b_Ee^{-\nu d(i,j)},\qquad
 \|F_{ij}\|\le b_Fe^{-\nu d(i,j)}.
 \tag{3.1}
\]
Extend them by zero off \(X\times X\). Cauchy's formula on the two-variable polydisc of radii \(\rho/b_E,\rho/b_F\), using (2.12), yields
\[
 |De_X(C)[E]|\le{\!M(X)\over\rho}b_E,\qquad
 |D^2e_X(C)[E,F]|\le{\!M(X)\over\rho^2}b_Eb_F.
 \tag{3.2}
\]
If a direction vanishes, the corresponding conclusion is immediate. The mixed coefficient is \(D^2e_X[E,F]\), so there is no additional factor two. Radii can approach the displayed values from below if analyticity is only asserted on open sets.

This argument differentiates the Gaussian density in covariance variables. It never differentiates a sharp cutoff, and it uses no local-background support claim.

## 4. Proved: abstract two-source response theorem

Let \(C(s,t)\) be a holomorphic symmetric covariance near \((0,0)\), with \(C(0,0)=C\). Denote its responses by
\[
 E_x=\partial_sC(0),\qquad E_y=\partial_tC(0),\qquad
 E_{xy}=\partial_s\partial_tC(0).
\]
Suppose, for every nonempty \(X\), their restrictions satisfy
\[
 \|(E_x)_{ij}\|\le B_1e^{-\mu\delta_x(X)}e^{-\nu d(i,j)},
 \qquad \delta_x(X)=\operatorname{dist}(x,X),
 \tag{4.1}
\]
and likewise for \(y\), together with
\[
 \|(E_{xy})_{ij}\|\le
 B_2e^{-\nu[d(x,y)+\delta_x(X)+\delta_y(X)]}
          e^{-\nu d(i,j)}.
 \tag{4.2}
\]
Then
\[
 |\partial_s\partial_tF_\Lambda(C(s,t))|_{s=t=0}
 \le M_0\left[
 {B_1^2\over\rho^2}S_{\mu-\kappa}
 +{B_2\over\rho}S_\nu
 \right]e^{-\kappa d(x,y)}.
 \tag{4.3}
\]

Proof. Chain rule and (3.2) give, for each \(X\),
\[
 |\partial_s\partial_te_X|
 \le M(X)\left[
 {B_1^2\over\rho^2}e^{-\mu(\delta_x+\delta_y)}
 +{B_2\over\rho}
 e^{-\nu[d(x,y)+\delta_x+\delta_y]}
 \right].
 \tag{4.4}
\]
Choose nearest vertices of \(X\) to \(x,y\). Connecting them inside a spanning tree proves
\[
 d(x,y)\le\delta_x(X)+\ell(X)+\delta_y(X).
 \tag{4.5}
\]
Hence
\[
 e^{-\mu(\delta_x+\delta_y)}
 \le e^{-\kappa d(x,y)}e^{\kappa\ell(X)}
        e^{-(\mu-\kappa)\delta_x(X)}.
 \tag{4.6}
\]
For \(q>0\), \(e^{-q\delta_x(X)}\le\sum_{z\in X}e^{-qd(x,z)}\). Using (2.11) therefore gives
\[
 \sum_Xe^{\kappa\ell(X)}M(X)e^{-q\delta_x(X)}
 \le M_0S_q.
 \tag{4.7}
\]
This handles the first term. For the second, \(\nu>\kappa\), so drop the \(y\)-distance factor and use (4.7) with \(q=\nu\). The sum of \(e_X\) is finite over subsets of a finite \(\Lambda\); each coefficient has its normally convergent cluster representation. Thus chain rule and summation are justified. This proves (4.3).

On \(\mathbb Z^4\), the resulting second moment is bounded uniformly:
\[
 \sum_y d(x,y)^2
 |\partial_x\partial_yF_\Lambda|
 \le C_{\rm H}\tau_R
       \sup_x\sum_y d(x,y)^2e^{-\kappa d(x,y)}<\infty.
 \tag{4.8}
\]

## 5. Proved: finite-support affine precision sources meet the responses

Let \(A=C^{-1}\), and perturb it by
\[
 A(s,t)=A+sH_x+tH_y,
 \qquad H_x=H_x^T,\quad H_y=H_y^T.
 \tag{5.1}
\]
Assume \(H_x\) is supported on \(B_{r_s}(x)\times B_{r_s}(x)\), with at most \(n_s\) sites in that ball and \(\|H_x\|\le H\), uniformly in \(x\); similarly for \(H_y\). For small complex \(s,t\) the inverse is analytic, and
\[
 E_x=-CH_xC,\qquad
 E_{xy}=CH_xCH_yC+CH_yCH_xC.
 \tag{5.2}
\]
The symmetry requirements are preserved.

Expanding matrix products in site blocks, each block of \(H_x\) has norm at most \(H\), and
\[
 \|(E_x)_{ij}\|
 \le b_1e^{-\mu[d(i,x)+d(j,x)]},
 \quad b_1=n_s^2HK_0^2e^{2\mu r_s}.
 \tag{5.3}
\]
Since the distance sum is at least \(d(i,j)\) and at least \(2\delta_x(X)\), averaging these two lower bounds proves (4.1) with \(B_1=b_1\).

For the first mixed product,
\[
 \|(CH_xCH_yC)_{ij}\|
 \le b_2e^{-\mu[d(i,x)+d(x,y)+d(y,j)]},
 \quad b_2=n_s^4H^2K_0^3e^{4\mu r_s}.
 \tag{5.4}
\]
The exponent is at least \(d(i,j)\), and also at least
\(d(x,y)+\delta_x(X)+\delta_y(X)\). Averaging gives (4.2); the reversed product gives the same estimate. Thus \(B_2=2b_2\) works.

This proves (1.1) for finite-support affine precision sources, with the explicit constant in (4.3). The result remains uniform when \(x=y\) or the source supports overlap.

## 6. Nonlinear precision and smeared physical responses

Local first variations alone are insufficient. For a nonlinear precision,
\[
 E_{xy}=CH_xCH_yC+CH_yCH_xC-C H_{xy}C,
 \qquad H_{xy}=\partial_x\partial_yA.
 \tag{6.1}
\]
The final term must be bounded. A simple sufficient local hypothesis is
\[
 H_{xy}=0\ \text{if }d(x,y)>r_2,\qquad
 \operatorname{supp}H_{xy}\subset
 B_{r_3}(x)\times B_{r_3}(x),\qquad \|H_{xy}\|\le H_2.
 \tag{6.2}
\]
The first-variation calculation then bounds
\(\|(CH_{xy}C)_{ij}\|\le b_3e^{-\mu\delta_x(X)}e^{-\nu d(i,j)}\).
Equations (3.2), (4.7) add at most
\[
 {M_0b_3\over\rho}S_\mu\,
 {\bf1}_{d(x,y)\le r_2}
 \le {M_0b_3\over\rho}S_\mu e^{\kappa r_2}
       e^{-\kappa d(x,y)}
 \tag{6.3}
\]
to the Hessian. Here \(b_3\) is given by the analogue of (5.3), with \(H_2,r_3\) and the corresponding ball size.

If a local-source Hessian kernel \(K(z,w)\) has the bound \(C\tau_Re^{-\kappa d(z,w)}\), and the normalized physical linear responses obey
\[
 |h_x(z)|\le H_h e^{-m d(x,z)},
 \tag{6.4}
\]
then its contraction with \(h_x,h_y\) has exponential decay as well. Put
\(\lambda=\tfrac12\min(\kappa,m)\). The triangle inequality gives
\[
 m d(x,z)+\kappa d(z,w)+m d(w,y)
 \ge\lambda d(x,y)
 +(m-\lambda)d(x,z)+(\kappa-\lambda)d(z,w).
 \]
Summing first \(w\), then \(z\), proves
\[
 |\langle K;h_x,h_y\rangle|
 \le C\tau_RH_h^2S_{m-\lambda}S_{\kappa-\lambda}
       e^{-\lambda d(x,y)}.
 \tag{6.5}
\]
If a nonlinear physical chart is differentiated instead, its second derivative gives an additional first-variation term. It must either vanish by an independently established symmetry or be estimated. The displayed covariance second response is never discarded solely because the first variation of the full gauge-invariant functional vanishes.

## 7. Exact relationship to the deposited coefficient

Raw I 3780–3837 defines the regular step action as the sum of a Gaussian normalization term and the logarithm of the fluctuation integral. Its formulas 4.2:eq-increment-1 and -2 first differentiate the pointed family \(E^{(j)}(X;\xi,z)\) along the free normalized responses \(h_x,h_y\), then sum \(X,z\). Formula 4.2:eq-increment-3 forms
\[
 \beta_j=\sum_u u_\mu u_\nu\,\Pi_{\mu\nu}^{(j)}(u).
 \tag{7.1}
\]
The coefficient \(\beta_j^0\) uses only the Gaussian normalization. The normalized cutoff expectation in (2.3) is a different contribution.

The exact splitting of the fluctuation remainder is
\[
 \log\mathbb E_C[\chi_R e^V]
 =\log\mathbb E_C[\chi_R]
  +\log{\mathbb E_C[\chi_Re^V]\over\mathbb E_C[\chi_R]}.
 \tag{7.2}
\]
Thus this note bounds only the pure Gaussian cutoff summand. It does not bound the interaction summand or the Gaussian normalization. CMP119 pp.272–273, (3.28)–(3.32), makes the corresponding Gaussian-cutoff separation.

If at finite volume an analytic pointing satisfies
\[
 F_{{\rm cut},\Lambda}(\xi)-F_{{\rm cut},\Lambda}(0)
  =\sum_{X,z}E_{{\rm cut},\Lambda}(X;\xi,z),
 \tag{7.3}
\]
and the sum can be differentiated twice, then its total Hessian is exactly the sum of pointed Hessians. This is linearity; support locality is not required for the equality. Therefore a direct bound on the total Hessian suffices for this coefficient if the following separate interfaces are established:

1. The actual Gaussian and cutoff use the fixed independent coordinates of (2.3), and meet the covariance bounds uniformly in the RG step and history.
2. The actual background/current precision responses, including their second variations, meet §4 or a sufficient form such as §§5–6.
3. The response used is the deposited normalized free response \(h_\infty\); all coordinate and scale factors are included.
4. The finite-volume total Hessians converge, bondwise, to the summed pointed kernel used in the definition of \(\beta\). Translation covariance gives dependence on \(x-y\).

Under these conditions (4.8), or (6.5), gives
\[
 |\beta_{{\rm cut},j}|\le C_\beta^{\rm cut}\tau_{R(g_{j-1})},
 \tag{7.4}
\]
uniformly in \(j\) and the history. The exponential bound provides uniform domination for the final weighted sum over \(u\).

One can instead define an unpointed candidate coefficient from the thermodynamic-limit criterion proved in §8. Its identification with the deposit's coefficient still requires item 4. Uniform bounds alone do not prove the local convergence assumed there, or the identification. This is a narrower possible repair of the scalar coupling estimate, not a replacement for the strict local effective-action induction.

## 8. Proved: thermodynamic limit from local covariance-response convergence

Consider growing finite regions or tori. Assume every fixed finite lattice ball embeds with its metric unchanged for all sufficiently large volumes, and the constants in §§2–4 are uniform. Assume that, for fixed sites and fixed sources \(x,y\), the entries of
\[
 C_\Lambda,\quad E_{x,\Lambda},\quad
 E_{y,\Lambda},\quad E_{xy,\Lambda}
 \tag{8.1}
\]
converge, and that the fixed functions \(q_i\) agree under these embeddings. Then the total Hessian has a limit. Its kernel satisfies (4.3), and all polynomially weighted spatial sums converge under the natural embeddings.

First, a finite-set identity makes continuity transparent. Let \(Z_Y(C)\) denote the cutoff partition function using only marked sites in \(Y\), with covariance \(C_{YY}\). All logarithm branches are the ones continued from zero defects. Since
\(\log Z_Y=\sum_{\varnothing\ne X\subset Y}e_X\), finite Möbius inversion gives
\[
 e_X(C)=\sum_{Y\subset X}(-1)^{|X\setminus Y|}\log Z_Y(C),
 \qquad \log Z_\varnothing=0.
 \tag{8.2}
\]
Thus a fixed-\(X\) coefficient and its covariance derivatives are continuous analytic functions of the finite matrix \(C_{XX}\). Equations (8.1) and chain rule imply convergence of each fixed-\(X\) source Hessian. Uniform accretivity and norm bounds pass to every limiting finite marginal.

Second, the sum over \(X\) is uniformly tight near the source. Fix \(0<\beta<\min(\kappa,\nu)\). If \(X\not\subset B_L(x)\), connect a nearest point of \(X\) to a point outside that ball inside a spanning tree to get
\[
 \delta_x(X)+\ell(X)>L.
\]
For every \(q>\beta\),
\[
 M(X)e^{-q\delta_x(X)}
 \le e^{-\beta L}M(X)e^{\beta\ell(X)}
                         e^{-(q-\beta)\delta_x(X)}.
\]
Apply the anchored bound as in (4.7), dropping unnecessary factors in (4.4), to obtain
\[
 \sum_{X\not\subset B_L(x)}
 |\partial_x\partial_ye_X|
 \le M_0\left[
 {B_1^2\over\rho^2}S_{\mu-\beta}
 +{B_2\over\rho}S_{\nu-\beta}
 \right]e^{-\beta L}.
 \tag{8.3}
\]
This holds uniformly in volume, including periodic metrics. For fixed \(L\), only finitely many subsets of \(B_L(x)\) occur and each converges. Let \(L\) tend to infinity in (8.3), proving convergence of the total Hessian. The additional nonlinear term (6.3) has the same tightness argument.

If the limiting covariance and its source responses are translation covariant, the limit is a function of \(x-y\). The uniform exponential bound (4.3) permits dominated convergence of the second spatial moment, or any fixed polynomial moment. For tori, choose nearest lattice representatives in a fundamental domain; their distances agree locally and the exponential tail is uniform. The same reasoning applies after the response contraction of (6.5).

No strictly local background activity was used in this limit argument. What was used, and must be supplied for the actual RG construction, is local convergence of the covariance and its two source responses in the same fixed cutoff coordinates.

## 9. Scope

The derivation proves a direct two-source estimate under explicit uniform inputs. It avoids background-support polymer weights entirely and needs only the marked-site tree length. This removes one unnecessary requirement for estimating the scalar coefficient, but the actual RG precision is not assumed local here. The direct response bounds (4.1)–(4.2), or their suitable variants, are the concrete remaining source target.

References for the Gaussian cluster module: A. Abdesselam, [BKAR notes](https://mabdesselam.github.io/BKAR.pdf), Theorem 1; R. Fernández and A. Procacci, [Cluster expansion for abstract polymer models](https://webspace.science.uu.nl/~ferna107/papers/ferpro07.pdf), equations (2.7), (2.12), (2.14), (2.15). The module was independently checked in outputs/ym4-current-cutoff-notebook.tex, §§3–5. Source conventions and primary covariance scope are recorded in work/cutoff_source_match_research.md.
