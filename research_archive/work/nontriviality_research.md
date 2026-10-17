# Nontriviality, generalized-free countermodels, and phase selection

Research note, 16 October 2026. Repository examined at `e392ef45013a581664bab76b90867170b30fe10e`.

**Status.** The explicit countermodel, spectral inequalities, and measure-level decomposition lemmas below have proofs in this note. Their application to the deposited Yang–Mills draft remains conditional on the draft's estimates and on additional reconstruction inputs. This is not a construction of YM4. No repository file was modified.

## 1. What the action-density sector can establish

The zeroth draft, pp. 3–5 and 16–18, concerns centered, gauge-invariant action-density correlations on pairwise disjoint supports. It claims a positive two-point witness comparable to

\[
g(d)^4\iint f(x)h(y)|x-y|^{-8}\,dx\,dy,
\qquad g(d)^{-2}\asymp\log(1/d).
\]

It expressly does not establish the number-of-points growth condition, Wightman fields, coincident-point extensions, unique vacuum, clustering, or a mass gap. Full rotations have an additional infrared-flux assumption. Consequently the claimed reconstructed Hilbert space and positive Hamiltonian are a strictly weaker endpoint than a Yang–Mills QFT.

A successful construction from this starting point needs at least:

1. Actual cutoff-independent limits with a consistent family of gauge-invariant local observables, positivity, full Euclidean covariance, appropriate distributional/number-of-points bounds, and a valid OS-to-Wightman reconstruction.
2. A nontrivial vacuum sector with the required uniqueness/clustering, rather than only a nonzero vector in a possibly reducible zero-energy sector.
3. An identification of the resulting theory as Yang–Mills. One scalar named “action density” does not by itself construct the gauge-invariant local observable content of YM. One needs the relevant renormalized curvature polynomials, their tensor structures/mixed correlations and short-distance relations, or another rigorous identification theorem.
4. For the full Clay problem, a positive mass gap, in addition to the existence statement, for every compact simple gauge group.

The official [Jaffe–Witten problem statement, pp. 5–6](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf) asks for local quantum fields corresponding to gauge-invariant curvature polynomials and their derivatives, appropriate short-distance behavior, and axioms at least as strong as the cited Wightman/OS axioms. The actual prize statement includes a mass gap. The scalar-sector endpoint should therefore be named accurately even if proved.

## 2. Explicit generalized-free countermodel to the logarithmic witness

### Proposition 2.1

There is a local, positive-energy, Poincare-covariant scalar generalized free Wightman field in four dimensions with unique vacuum, clustering, and separated Euclidean two-point function

\[
C(r)\sim\frac{48a}{\pi^2}\,
\frac{r^{-8}}{\log^2(1/(\Lambda r))}\quad(r\downarrow0),
\qquad a,\Lambda>0.
\]

All its truncated functions of order greater than two vanish. Therefore logarithmic running of this two-point observable does not exclude generalized free fields.

**Construction and proof.** Put

\[
\rho(s)=\frac{a s^2}{\log^2(e+s/\Lambda^2)},\quad s\geq0,
\qquad W_2=\int_0^\infty\rho(s)\Delta_+(\cdot;s)\,ds.
\]

Here \(\Delta_+(x;s)\) is the four-dimensional scalar free two-point function of mass \(\sqrt{s}\), with normalization

\[
\Delta_+(f,f;s)=\int\frac{d^4p}{(2\pi)^3}
\theta(p^0)\delta(p^2-s)|\widehat f(p)|^2.
\]

Equivalently, use symmetric Fock space over

\[
\mathcal K=L^2\left(V_+,\frac{\rho(p^2)d^4p}{(2\pi)^3}\right)
\]

and the usual creation/annihilation field. The measure has polynomial growth, so Schwartz smearings give continuous one-particle vectors and the field is a tempered operator-valued distribution on the finite-particle domain. Its commutator is the integral of free Pauli–Jordan commutators, each supported in the closed light cone; hence it is local. The representation has positive energy. Every nonvacuum Fock sector has strictly positive energy almost everywhere, so the vacuum is the only invariant vector. Smearing makes each two-point spectral integrand integrable; the Riemann–Lebesgue lemma gives decay under spacelike translations, and Wick expansion gives clustering of all smeared correlations.

For Euclidean distance \(r>0\), the analytically continued two-point function is

\[
C(r)=\int_0^\infty \rho(s)
\frac{\sqrt{s}}{4\pi^2r}K_1(r\sqrt{s})\,ds
=\frac{a}{2\pi^2r^8}
\int_0^\infty\frac{u^6K_1(u)}{\log^2(e+u^2/(\Lambda r)^2)}\,du.
\]

Writing \(L=\log(1/(\Lambda r))\), the denominator is asymptotic to \(4L^2\) for each fixed \(u>0\). For a rigorous limit, split the integral at \(u=(\Lambda r)^{1/2}\). In the lower part, use \(K_1(u)=O(u^{-1})\): multiplying by \(L^2\) leaves \(O(L^2(\Lambda r)^3)\). In the upper part the ratio of \(L^2\) to the denominator is bounded uniformly for small \(r\), and \(u^6K_1(u)\) is integrable. Dominated convergence applies. Finally

\[
\int_0^\infty u^6K_1(u)\,du
=2^5\Gamma(4)\Gamma(3)=384,
\]

which gives the displayed coefficient.

For nonnegative, fixed separated bump shapes \(f,h\), set \(f_d(x)=f(x/d)\), \(h_d(x)=h(x/d)\). If their separation is bounded away from zero at unit scale, the same asymptotic is uniform on their compact product support, so

\[
C(f_d,h_d)\sim\frac{48a}{\pi^2\log^2(1/(\Lambda d))}
\iint f(x)h(y)|x-y|^{-8}\,dx\,dy.
\]

Thus this model matches the *smeared* scale dependence used in the draft, not merely a pointwise analogy. The coefficient \(a\) can match any prescribed positive normalization. Replacing the denominator by a positive expression involving \(g^{-2}+b\log(1+s/\Lambda^2)\) lets one engineer a chosen leading logarithmic slope as well.

The general positive-polynomially-bounded spectral-weight construction and Wick characterization are standard; see [Dutsch–Rehren, §§1–2](https://arxiv.org/pdf/math-ph/0209035). The spectral density and asymptotic calculation above are the explicit counterexample used here.

### Reflection positivity and contact terms

For \(f\) compactly supported in \(t>0\), a positive distance from the reflection plane,

\[
C(\theta f,f)=\int_0^\infty\rho(s)ds
\int\frac{d^3p}{(2\pi)^3\,2\omega_s(p)}
\left|\int_0^\infty e^{-\omega_s(p)t}\widetilde f(t,p)\,dt\right|^2\geq0,
\quad\omega_s(p)=\sqrt{|p|^2+s}.
\]

Exponential decay from the support's distance to the plane controls the large-mass integral. Wick products give the corresponding reflection-positive separated Schwinger system.

**Do not replace this statement by an unsupported Euclidean probability measure claim.** The singularity \(r^{-8}\log^{-2}(1/r)\) is not locally integrable in four dimensions. The unsubtracted momentum integral \(\int\rho(s)/(p_E^2+s)ds\) diverges. Contact extensions/renormalized Schwinger distributions require care. The countermodel is rigorously defined as a Wightman field and on separated Euclidean configurations, which is precisely enough to show that the draft's separated two-point witness cannot identify YM. It is not being presented as a Gaussian probability measure on all Euclidean scalar distributions with that naive covariance.

Multiplying \(\rho\) by \(1_{[m_0^2,\infty)}\), \(m_0>0\), preserves the ultraviolet asymptotic and gives a generalized-free model with a mass gap. The same witness is therefore compatible with both gapped and gapless models.

### A stronger countermodel: logarithmic witness AND nonzero fourth cumulant

Let \(\chi\) instead be a generalized free scalar with spectral density

\[
\rho_0(s)=\frac{a}{\log(e+s/\Lambda^2)}.
\]

The same Bessel change of variables, now using \(\int_0^\infty u^2K_1(u)du=2\), gives

\[
C_\chi(r)\sim\frac{a}{2\pi^2}\frac{r^{-4}}{\log(1/(\Lambda r))}.
\]

The local Wick square \(O=:\!\chi^2\!:\) is a Wightman field on the same free Fock space. To see the relevant existence bound directly, its vacuum norm after smearing involves a positive convolution of two polynomially bounded forward-cone spectral measures and \(|\widehat f(p+q)|^2\). Since \(p,q\in\overline V_+\), their energies cannot cancel; each is bounded by the energy of \(p+q\). Schwartz decay in the total momentum controls the integral. The analogous finite-particle estimates define the Wick square on its usual common domain; the local commutator follows from Wick products of local fields.

At separated Euclidean points,

\[
C_O(r)=2C_\chi(r)^2
\sim\frac{a^2}{2\pi^4}\frac{r^{-8}}{\log^2(1/(\Lambda r))}.
\]

For four distinct points its connected function is

\[
S^T_{O,4}=16\bigl(C_{12}C_{23}C_{34}C_{41}
+C_{12}C_{24}C_{43}C_{31}
+C_{13}C_{32}C_{24}C_{41}\bigr),
\quad C_{ij}=C_\chi(x_i-x_j).
\]

It is strictly positive for distinct Euclidean points. Thus even a logarithmic two-point witness **together with** a nonzero connected four-point function is compatible with a quadratic observable of an underlying generalized free field. This field still has positive-energy reconstruction, unique vacuum and clustering. It is not claimed to be a finite collection of ordinary free Maxwell fields; the point is that these observable tests alone do not characterize non-Abelian YM dynamics. The same Euclidean contact-term caveat applies.

## 3. Independent zero modes also survive the ultraviolet witness

Let \(G\) be the field just constructed and let \(Z\) be an independent, centered real Gaussian variable of variance \(\sigma^2>0\). On the tensor product with \(L^2(\operatorname{law}(Z))\), define

\[
O(f)=G(f)\otimes1+1\otimes Z\int f.
\]

Translations and Lorentz transformations act trivially on the second factor. Positivity, locality and covariance persist, but the invariant-vector space now contains \(\Omega_G\otimes L^2(\operatorname{law}(Z))\). There are many zero-energy vectors and no clustering for \(O\). Its connected separated two-point function is

\[
C_O(x-y)=C_G(x-y)+\sigma^2.
\]

The added term is negligible in the short-distance asymptotic; for sup-normalized scaled bumps it contributes \(\sigma^2d^8(\int f)(\int h)\), whereas the logarithmic witness is of order \(\log^{-2}(1/d)\).

Thus the logarithmic witness rules out a *pure* random constant field but does not rule out an independent zero mode appended to a dynamical theory. A positive centered reflected norm by itself can even be supplied entirely by a zero mode: for the field \(O(x)=Z\), the reflected norm is \(\sigma^2|\int f|^2\), while \(H=0\) on the whole reconstructed space.

## 4. A stronger spectral witness that kills all zero-energy contamination

### Lemma 4.1: one semigroup ratio

Let \(H\geq0\) be self-adjoint, \(v\ne0\), \(t>0\), and

\[
C(t)=\langle v,e^{-tH}v\rangle\leq q\|v\|^2,\qquad0\leq q<1.
\]

Let \(\nu_v(B)=\|1_B(H)v\|^2\). For \(0<\alpha<\log(1/q)\),

\[
\nu_v([0,\alpha/t])\leq qe^\alpha\|v\|^2,
\qquad
\nu_v((\alpha/t,\infty))\geq(1-qe^\alpha)\|v\|^2>0.
\]

**Proof.** On \([0,\alpha/t]\), \(e^{-tE}\geq e^{-\alpha}\); integrate against \(\nu_v\).

Furthermore

\[
\|(1-e^{-tH})v\|^2
=\int(1-e^{-tE})^2d\nu_v(E)>0,
\quad
\|(1-e^{-tH})v\|\geq(1-q)\|v\|.
\]

The last inequality follows by Cauchy–Schwarz applied to \(\langle v,(1-e^{-tH})v\rangle\). The vector \((1-e^{-tH})v\) has zero projection onto \(\ker H\), including every degenerate-vacuum component.

This proves a positive-energy excitation of this state. It proves **no mass gap**: arbitrarily low positive energies may still occur in this or other vectors.

### A concrete probe pair admitted by the actual draft test class

Definition 5.1, p. 77, and the raw account's `8.1:not-test-pairs-kernel` require nonnegative Lipschitz bumps, each in a ball of radius \(d\), mass at least \(\vartheta\|f\|_\infty d^4\), Lipschitz constant at most \(\|f\|_\infty/(\vartheta d)\), and support separation in \([d,6d]\).

Let \(e_0\) be the time direction and use

\[
f_d(x)=\left(1-\frac{|x-(3d/4)e_0|^2}{(d/4)^2}\right)_+^2.
\]

This is \(C^1_c\), nonnegative, has supremum one, support radius \(d/4\), mass \(\pi^2d^4/3072\), and Lipschitz constant \(32/(3\sqrt3\,d)<7/d\). Therefore \(\vartheta=10^{-3}\) works for every \(d\).

Both pairs

\[
(\theta f_d,f_d),\qquad(\theta f_d,\tau_{4de_0}f_d)
\]

belong to the *same* class \(\mathfrak T(d;10^{-3})\): their support separations are respectively \(d\) and \(5d\). Every near-pair point distance is at most \(2d\); every far-pair point distance is at least \(5d\). For the exact continuum kernel \(K(f,h)=\iint f(x)h(y)|x-y|^{-8}dxdy\),

\[
\frac{K(\theta f_d,\tau_{4de_0}f_d)}{K(\theta f_d,f_d)}
\leq(2/5)^8.
\]

The draft's two-sided witness coefficients in (1.17) have ratio \((8/3)/(2/9)=12\). If those estimates and the continuum kernel comparison hold, the same-scale coupling and its running cancel:

\[
\limsup_{d\downarrow0}\frac{C_d(4d)}{C_d(0)}
\leq12(2/5)^8=0.00786432<1.
\]

Consequently one may take \(q=0.02\) for sufficiently small \(d\). With \(t=4d\) and \(\alpha=1\), Lemma 4.1 places at least \(1-0.02e>0.945\) of this vector's norm-squared above energy \(1/(4d)\).

**Precise dependency:** the block-conditioned kernel in the theorem is not literally the unconditioned continuum kernel at a fixed \(d\). Remark 5.7, p. 78, claims its convergence along sup-normalized dilates as \(d\downarrow0\) and \(K-s(d)\to\infty\), referring to a companion free-kernel note and Bałaban's propagator decay. Proposition 5.4's coarse constants alone do not give the displayed ratio. The usable new target is to prove the kernel ratio for these two explicit shapes, or prove the cited asymptotic. No change of the coupling scale is needed, since both pairs use the same \(d\), same \(\vartheta\), and same witness depth. The draft's witness/RG inputs remain unverified.

## 5. Rigorous reflection-positive ergodic decomposition at the measure level

Here assume a genuine probability measure \(\mu\) on a standard Borel field-configuration space, with local sigma-algebras, bounded local functions dense in \(L^2(\mu)\), and strongly continuous translations. Reflection \(\theta\) preserves \(\mu\), normalizes translations, and exchanges time half-spaces. Assume RP for every bounded function measurable in the positive half-space, extending by \(L^2\) continuity. Let \(\mathcal I\) be the completed sigma-algebra of events invariant under all translations.

### Lemma 5.1: invariant events are measurable from either half-space

For bounded local \(g\), average its translations over

\[
D_T=[T,2T]\times[-T,T]^{d-1}.
\]

For large \(T\), every translated copy of \(g\) in this average is supported in the positive half-space. The joint spectral theorem for translations shows that these averages converge in \(L^2\) to \(E[g\mid\mathcal I]\): the normalized Fourier multipliers converge to zero at every nonzero momentum and to one at zero. Bounded local functions are dense, and conditional expectation is a contraction. Hence \(L^2(\mathcal I)\) is contained in the completed positive-half-space \(L^2\) space. Negative-time averages give the other half-space.

### Lemma 5.2: reflection fixes every invariant event

The pullback \(U_\theta\) is a unitary self-adjoint involution preserving \(L^2(\mathcal I)\). By Lemma 5.1, RP applies to every \(h\) in this subspace:

\[
\langle U_\theta h,h\rangle_{L^2(\mu)}\geq0.
\]

A self-adjoint involution with nonnegative quadratic form has no minus-one eigenspace. Thus \(U_\theta=1\) on \(L^2(\mathcal I)\).

### Lemma 5.3: conditional RP

For bounded \(A\) in the positive half-space and bounded \(h\geq0\) measurable in \(\mathcal I\), Lemmas 5.1–5.2 allow RP to be applied to \(\sqrt h A\):

\[
\int h\,\overline{A\circ\theta}\,A\,d\mu\geq0.
\]

Therefore \(E[\overline{A\circ\theta}A\mid\mathcal I]\geq0\) almost surely. Disintegrating \(\mu=\int\mu_\xi\,d\nu(\xi)\) over its translation-ergodic components gives RP for \(\mu_\xi\), first for a countable determining local algebra and then by density. The same conditional-expectation argument shows reflection invariance of the components.

If the parent is fully Euclidean invariant and RP at one plane, covariance supplies RP at all planes. Apply the argument to a countable dense set of reflections and use continuity to obtain a common full-measure set of components invariant under all Euclidean motions and RP at every plane. If the parent has only coordinate/hypercubic RP and symmetry, this proves only those symmetries componentwise; it does not manufacture rotation invariance.

### Clustering after full Euclidean covariance

For \(d\geq2\), a separable strongly continuous unitary representation of \(E(d)=\mathbb R^d\rtimes O(d)\), restricted to the orthogonal complement of its translation-invariant vectors, has matrix coefficients vanishing as \(|a|\to\infty\) along translations.

One proof uses the joint spectral measure of translations. Choose a faithful finite scalar control measure by taking a weighted sum of the spectral measures of a dense sequence of unit vectors. Its measure class is invariant under rotations. Averaging it over \(O(d)\) gives an equivalent finite radial measure. Away from zero this disintegrates into uniform sphere measure times a radial measure. Every vector spectral measure has an integrable density relative to that measure. Fourier transforms of integrable densities on each positive-radius sphere vanish at infinity when \(d\geq2\); smooth approximation gives uniformity in direction, and dominated convergence integrates over radii. The atom at zero is exactly the translation-invariant projection. Polarization yields the assertion for all matrix coefficients.

Equivalently this is the relative Howe–Moore property of \((E(d),\mathbb R^d)\). A primary source is [Cluckers–Cornulier–Louvet–Tessera–Valette, Theorem 5.2 and Proposition 2.2](https://rcluckers.perso.math.cnrs.fr/prints/CCLTV.pdf): the connected rotations act nontrivially and irreducibly on \(\mathbb R^d\).

Applying this to the Koopman representation of a fully Euclidean-invariant translation-ergodic component gives

\[
\int A\,\tau_a B\,d\mu_\xi\longrightarrow
\left(\int A\,d\mu_\xi\right)\left(\int B\,d\mu_\xi\right)
\quad(|a|\to\infty)
\]

for \(A,B\in L^2(\mu_\xi)\). Thus, under the preceding measure hypotheses, these components do cluster. Arbitrary translation ergodicity without continuous rotations does not imply this conclusion.

### Which regularity properties pass?

Almost-sure support conditions, such as being a tempered distribution or satisfying a distributional constraint, pass to almost every component. Finite integrability of a countable set of observables also passes. Numerical moment bounds and OS growth estimates with the same constants do **not** follow merely by disintegration: an averaged inequality need not hold in each component.

A useful sufficient replacement is a single weighted-norm exponential estimate. If a random field is realized in a separable distribution Hilbert space with norm \(X\) and \(E_\mu e^{\delta X^2}<\infty\), then \(M_\xi=E_{\mu_\xi}e^{\delta X^2}<\infty\) almost surely, and

\[
E_{\mu_\xi}X^n\leq M_\xi\left(\frac{n}{2e\delta}\right)^{n/2}.
\]

This follows by maximizing \(x^ne^{-\delta x^2}\). Combined with a deterministic test-function bound \(|F(f)|\leq Xp(f)\), it supplies controlled componentwise moment growth. This is a sufficient condition, not an estimate established for YM4 action density here.

**Major applicability limitation:** the deposited action-density correlations only on disjoint supports are not yet the moments of a supplied Euclidean probability measure, and their local products are not automatically a bounded-observable algebra. Lemmas 5.1–5.3 therefore cannot simply be applied to the current draft. One must construct an appropriate configuration law/local bounded algebra, or prove an analogous disintegration theorem in the reconstructed operator-algebraic setting, with explicit regularity and identification hypotheses.

## 6. A positive witness survives some clustering component only after centering correctly

Suppose the measure-level setting of Section 5 holds, and \(A\) is square-integrable and supported at positive time. Let \(m_\xi=E_{\mu_\xi}A\). Reflection invariance of components gives the exact total-covariance identity

\[
q_\mu(A-E_\mu A)
=\int q_{\mu_\xi}(A-m_\xi)d\nu(\xi)
+\operatorname{Var}_\nu(m_\xi),
\quad
q_\mu(B)=E_\mu[\overline{B\circ\theta}B].
\]

The second term may account for the entire positive norm: the random-constant example has only point-mass ergodic components and zero centered fluctuation in each one.

Instead choose a time translation preserving positive support and put

\[
B=A-\tau_a A.
\]

Every translation-invariant component has \(E_{\mu_\xi}B=0\), and

\[
q_\mu(B)=\int q_{\mu_\xi}(B)d\nu(\xi).
\]

Conditional RP makes every integrand nonnegative. Therefore \(q_\mu(B)>0\) implies a positive-measure set of components with positive centered reflected norm. In the setting of Section 5 those components also cluster. Under an OS semigroup, \([B]=(1-e^{-aH})[A]\); Lemma 4.1 supplies exactly such a witness.

This proves existence of at least one nontrivial clustering component **conditionally on** the measure-level construction, regularity sufficient for its observables, full rotations, and the strict semigroup ratio. It proves neither that every component is nontrivial nor a mass gap nor the Yang–Mills identification.

## 7. Higher cumulants: what they do and do not establish

For an elementary Gaussian generalized free field, a nonzero connected \(n\)-point function for some \(n>2\) excludes that Gaussian field model. It does not show that the underlying physical theory is interacting when the observable is composite.

For a centered finite Gaussian vector \(X\) with covariance \(C\) and quadratic observable \(Q=X^TAX-\operatorname{tr}(CA)\), direct Gaussian integration gives

\[
\log E e^{tQ}
=-t\operatorname{tr}(CA)-\tfrac12\operatorname{tr}\log(1-2tCA),
\qquad
\kappa_n(Q)=2^{n-1}(n-1)!\operatorname{tr}((CA)^n),\quad n\geq2.
\]

The formula follows by expanding the logarithm; for several quadratic insertions, mixed derivatives sum the corresponding cyclic traces. It remains the free-field Wick-cycle formula at distinct points for Wick-square composite fields. In particular \(\kappa_4\) need not vanish in a free underlying theory. Special tensor or symmetry structures can kill particular odd cycles; no general assertion about odd Maxwell action-density cumulants is needed here.

Viable strengthening has three distinct levels:

* **Nonzero dynamics:** prove the explicit semigroup-ratio witness and select a nontrivial clustering sector as above.
* **Exclude specified free composite models:** calculate the connected four-point function for a declared free-Maxwell quadratic observable, with the full tensor/color covariance and normalization fixed; prove a limit differs from its Wick-cycle formula by a controlled, nonzero amount. Nonzero fourth cumulant alone is insufficient. Excluding this comparison class still does not identify YM.
* **Identify YM:** construct a sufficiently rich gauge-invariant local algebra with renormalized mixed correlations, the correct tensor structures and short-distance relations, and a consistent stress tensor/translation Ward identities. A nonzero non-Abelian correction with a rigorously controlled remainder is a meaningful target. A single scalar two-point function, however accurately its logarithm is matched, cannot provide this identification.

The most immediately reviewable new lemma is Section 4's two-shape spectral witness. Its geometric admissibility is checked here. The unresolved mathematical input is the actual uniform two-point theorem plus a sharp enough block-kernel comparison, followed by the missing continuum/reconstruction and phase-selection framework.
