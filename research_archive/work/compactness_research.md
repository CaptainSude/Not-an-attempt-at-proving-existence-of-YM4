# Fixed-cell compactness reduction for the Yang–Mills programme

Research note, 16 October 2026. This note proves finite-volume implications under explicitly stated hypotheses. It does not prove the missing Yang–Mills source estimates, nontriviality, full rotation covariance, contact-term extensions, or a mass gap. References to the public raw account describe that version only; completed companion proofs may be unposted or available on request.

## 1. Result and scope

Cutoff uniqueness and two-cutoff comparisons are unnecessary for **subsequential off-diagonal existence**. A fixed-physical-cell chessboard argument supplies the needed volume-independent bounds from a weaker, single-run package:

1. A complex-source stability bound after subtracting local source vacuum energies, with an exponent proportional to the number of **fixed-spacing coarse sites**, not bare sites.
2. An unsourced effective-density lower bound on a fixed coarse-link Haar neighbourhood.
3. Locality, holomorphy and summable long-polymer bounds for the source vacuum counterterms.
4. Reflection positivity/chessboard inequalities for the original Wilson measure.

The lower bound in item 2 gives the denominator estimate by an elementary integration, without a thermodynamic limit. Item 3 removes ultraviolet divergences from mixed derivatives at separated supports. The chessboard root converts the extensive numerator/denominator cost into a cost per occupied physical cell.

This bypasses the **named** last-scale change-of-units lemma if the above estimates are formulated and verified directly at a fixed physical stopping lattice. It does not bypass the mathematical need for a uniform per-coarse-site bound. Unbounded final-scale constants cannot be repaired by a subsequence argument alone.

## 2. Normalize the denominator correctly

Let a be the bare spacing, let Λ be a periodic physical volume, and write

\[
 Z_{a,\Lambda}(w)=\int \exp[-x_a A(U)+\mathcal O_a(w)]\,dU,
 \qquad x_a=g_a^{-2}.
\]

Introduce a source-independent real vacuum constant C_{a,Λ}, and set

\[
 \widehat Z_{a,\Lambda}(w)=e^{-C_{a,\Lambda}}Z_{a,\Lambda}(w).
 \tag{2.1}
\]

All generating-function ratios are unchanged. One must not silently identify the raw bare partition function with a renormalized coarse partition function: its entropy/free energy has bare-site, generally a^{-4}|Λ|, size. The ultraviolet vacuum constant need not converge; it cancels exactly from normalized observables.

Fix physical coarse spacing h>0, independent of a and Λ. In h-units there are V=|Λ|/h^4 coarse sites, at most 4V positively oriented links, and at most 6V plaquettes. Suppose the unsourced RG map has an exact integral identity

\[
 \widehat Z_{a,\Lambda}(0)=\int \rho_{a,\Lambda}(V_c)\,dV_c,
\]

with normalized product Haar measure and

\[
 \rho_{a,\Lambda}(V_c)\ge
 \chi(V_c)\exp[-x_* A_h(V_c)-E_-V],
 \quad 0<x_*\le X_*.
 \tag{2.2}
\]

Here X_* and E_- are independent of a,Λ. Assume that for some δ>0, likewise uniform, χ=1 whenever every coarse link lies in a fixed group ball Bδ around the identity. Put Hδ=Haar(Bδ)>0. For sufficiently small δ, normalized-trace Wilson plaquette action satisfies

\[
 A_h(V_c)\le 6 C_A\delta^2 V
 \quad\text{when every link is in }B_\delta.
\]

Consequently

\[
 \boxed{\widehat Z_{a,\Lambda}(0)\ge e^{-C_-V},\qquad
 C_-=E_-+6C_AX_*\delta^2+4\log H_\delta^{-1}.}
 \tag{2.3}
\]

**Proof.** Restrict the integral to the product of Bδ over links. Its Haar measure is at least Hδ^{4V}; use (2.2) and the plaquette bound. No comparison of two volumes, cluster expansion in the infrared, or cutoff uniqueness is used. For SU(N), Hδ≥c_N δ^{N²−1} for a fixed small coordinate ball, so C_- is explicit once δ,X_*,E_- are.

The window assumption is not automatic from the symbol χ. In Bałaban's construction χ is expressed through minimizing background configurations, not simply the coarse plaquettes. One can obtain the required window from a uniform coarse-plaquette-to-background-curvature regularity estimate, then put every link near identity. The raw account spells out this route at raw I, lines 155039–155083, label `4.31:lem-window-characteristic`, citing CMP 119 (1988), (2.16)–(2.17), and CMP 102 (1985), Theorem 1, (7)–(8). The above proof is conditional on verifying that input and the exact normalization in (2.2).

## 3. Why bare moments or centering are the wrong target

The Wilson action density observable is

\[
 \mathcal O_a(f)=\sum_p f(x_p)[1-\operatorname{Re}\operatorname{tr}U_p].
\]

At fixed physical support, the elementary compact-group bound gives |O_a(f)|≤C a^{-4}|supp f|‖f‖∞. This is volume-local but not ultraviolet-uniform. Centering removes only the first cumulant.

An exact product-Gaussian diagnostic makes the problem clear. On cells of spacing a let ξ_x be independent standard Gaussians and

\[
 X_a(f)=g_a^2\sum_x f(x)(\xi_x^2-1).
\]

Then

\[
 \operatorname{Var}X_a(f)=2g_a^4\sum_xf(x)^2,
\]

and, when |2tg_a²f(x)|<1,

\[
 \log\mathbb E e^{tX_a(f)}
 =\sum_x\{-tg_a^2f(x)-\tfrac12\log[1-2tg_a^2f(x)]\}.
 \tag{3.1}
\]

If g_a² is comparable to 1/log(1/a), the variance diverges like a^{-4}/log²(1/a) for a nonzero fixed f. This is an illustrative exact model, not a derived Yang–Mills asymptotic. It proves that asymptotically small coupling, locality, reflection positivity of a product measure, and centering do not imply uniform local exponential moments. Its cross-cumulants at disjoint supports are zero, demonstrating why the off-diagonal problem is much weaker.

Thus subtract a **nonlinear source vacuum functional**, not only a one-point expectation. The aim is bounded mixed derivatives with at least two separated supports. The renormalized generating function after nonlinear subtraction need not be a moment-generating function of a positive random variable; this does not damage reflection positivity of the original lattice observables, which is passed separately to off-diagonal limits.

## 4. A quantitative fixed-cell theorem

All lengths in this section are in fixed h-units. Let a coarse torus be tiled by M congruent cells of side ℓ, so V=Mv with v=ℓ⁴. The tiling admits the usual reflection transports. Write T_{c→d} for an isometry carrying cell c to d and ε(c→d)∈{+1,−1} for its reflection parity. Complex conjugation occurs at negative parity.

Let f₁,…,fₙ be real test functions, n≥2, with pairwise disjoint supports at distance at least d>0, all lying in the interior of one cell c at distance at least b>0 from its boundary. Set ν_i=‖f_i‖♯>0 and w_z=Σ_i z_i f_i. The weighted source ball is

\[
 D_r=\{z:\sum_i|z_i|\nu_i<r\}.
\]

Zero functions can be discarded since the desired cumulant then vanishes. Define w^{ch}_z by filling every cell with a transported copy of w_z, conjugating coefficients on cells of negative parity.

Assume:

**CB.** For F_z=e^{O_a(w_z)} supported inside cell c,

\[
 |Z(w_z)/Z(0)|\le [Z(w^{ch}_z)/Z(0)]^{1/M},
 \qquad Z(w^{ch}_z)/Z(0)\ge0.
 \tag{4.1}
\]

**S.** There is a sourced vacuum counterterm E_a(w), E_a(0)=0, such that for all required periodized weights

\[
 |e^{-E_a(w^{ch}_z)}\widehat Z(w^{ch}_z)|\le e^{C_+ V}.
 \tag{4.2}
\]

Here C_+ is independent of a,M. Along ordinary holomorphic source families E_a is holomorphic. The periodized family itself depends on z and conjugate z, so it is not asserted holomorphic in z.

**L.** The counterterm splits into cell-interior and face pieces,

\[
 E_a(w)=\sum_d E_{a,d}^{bulk}(w)+E_a^\partial(w),
\]

where the bulk part in cell d only reads the copy of the source in that cell. Its source dependence is holomorphic and zero at zero. Moreover

\[
 |E_a^\partial(w_z)|\le C_F,
 \qquad M^{-1}|E_a^\partial(w_z^{ch})|\le C_F.
 \tag{4.3}
\]

These estimates must be uniform in a,M. Define the holomorphic recentered counterterm

\[
 E_a^\#(z)=M^{-1}\sum_d
 \left[E_{a,d}^{bulk}\!\left(\sum_i z_i^{\epsilon(c\to d)}
                       f_i\circ T_{c\to d}^{-1}\right)\right]^{\epsilon(c\to d)}
 +E_a^\partial(w_z),
 \tag{4.4}
\]

where ξ^+=ξ and ξ^−=conjugate ξ. Assume its mixed derivative obeys

\[
 |\partial_1\cdots\partial_n E_a^\#(0)|
 \le B_n\prod_i\nu_i.
 \tag{4.5}
\]

The constants C_F,B_n may depend on d,b,ℓ,n,r, but not a,M. Section 5 derives (4.3)–(4.5) from explicit local-polymer estimates.

Finally assume the denominator bound (2.3), with the **same** source-independent normalization as (4.2).

**Theorem.** Set

\[
 Q=\exp[(C_++C_-)v+2C_F],\qquad
 r_0=\frac r{2Q+1}.
 \tag{4.6}
\]

Then h_a(z)=e^{-E_a^\#(z)}Z(w_z)/Z(0) is holomorphic on D_r, h_a(0)=1, and

\[
 |h_a(z)|\le Q\quad(z\in D_r),\qquad
 |h_a(z)-1|\le\tfrac12\quad(z\in D_{r_0}).
 \tag{4.7}
\]

In particular, its logarithm normalized to zero at the origin exists on D_{r₀}; one has

\[
 \boxed{\left|\operatorname{cum}\bigl(O_a(f_1),\ldots,O_a(f_n)\bigr)\right|
 \le \left[B_n+(\log2)\left(\frac{n(2Q+1)}r\right)^n\right]\prod_i\nu_i.}
 \tag{4.8}
\]

This is independent of the full volume and ultraviolet cutoff. The zero-free radius is tiny, possibly exponentially small in the **fixed cell volume**, but remains strictly positive and sufficient for compactness.

**Proof.** Each term conjugated twice in (4.4) has the form conjugate Φ(conjugate z), holomorphic because its Taylor coefficients are the conjugates of those of Φ. Locality gives

\[
 \operatorname{Re}E_a^\#(z)
 =M^{-1}\operatorname{Re}E_a^{bulk}(w_z^{ch})
   +\operatorname{Re}E_a^\partial(w_z).
\]

Combine (4.1), (4.2), (2.3), and V/M=v. The bulk terms cancel exactly in |h_a|, and the two face terms cost at most 2C_F. This proves the first bound in (4.7). It uses no invariance/covariance of the numerical bulk counterterms: their transported average defines the subtraction.

For any z, restrict h_a to the complex line through 0 and z, scaled so that its unit disc is contained in D_r. If t=(Σ|z_i|ν_i)/r<1, the one-variable Cauchy coefficient bound gives

\[
 |h_a(z)-1|\le Q\sum_{k\ge1}t^k=\frac{Qt}{1-t}.
\]

This is at most 1/2 for t≤1/(2Q+1). The power series for Log(1+(h_a−1)) has modulus at most log2 there. Use the polydisc with radii r₀/(nν_i), taking slightly smaller radii and then a limit, to bound ∂₁⋯∂ₙLog h_a by the second term in (4.8). Finally

\[
 \log Z(w_z)-\log Z(0)=E_a^\#(z)+\operatorname{Log}h_a(z)
\]

near 0. Differentiate and use (4.5). This completes the proof.

**Source-radius bookkeeping.** If the source theorem is available only for sums of real test functions with a weighted ℓ¹ source bound, group all even reflected copies of f_i into one real function f_i⁺ and all odd copies into f_i⁻. Their supports are separated by cell boundaries and they retain controlled Lipschitz norms. Then w_z^{ch}=Σ_i(z_i f_i⁺+conjugate z_i f_i⁻). This costs a factor at most two in source radius, not a factor M. Use r=r_original/2 in the theorem. Treating each copy as a separate source would wrongly lose a factor M and destroy the result.

## 5. Derive the face and mixed-derivative bounds from polymer locality

Here is one sufficient condition, stated without hiding scale summability. Let ℓ_j=L^{-j}, j=0,…,K, be the physical scales from the fixed coarse lattice toward the ultraviolet. Write E_a(w)=Σ_j Σ_X e_{a,j}(X;w). Each term is holomorphic on the admissible source ball, vanishes when w vanishes on its enlarged support X⁺, and depends only on w|_{X⁺}.

Assume the following uniform anchored estimate for every source-support ball B_R and every t>0:

\[
 \sum_{X:X^+\cap B_R\ne\varnothing,\;\operatorname{diam}X^+\ge t}
 \sup_{w\text{ admissible}}|e_{a,j}(X;w)|
 \le A(R+\ell_j)^4\ell_j^{-4}(1+j)^p e^{-c t/\ell_j}.
 \tag{5.1}
\]

A,c>0 and the fixed power p are independent of cutoff and volume. For replicated sources the bound is used per copy and summed. This is a precise, checkable polymer hypothesis; it is stronger than merely saying that individual terms are small.

Put

\[
 H_p(t)=\sum_{j=0}^{\infty}(1+j)^p L^{4j}e^{-ctL^j}<\infty.
 \tag{5.2}
\]

Splitting at L^j≈1/t, then grouping the geometrically spaced tail, proves

\[
 H_p(t)\le C_{L,c,p}(1+t^{-4})[1+\log^+(1/t)]^p.
 \tag{5.3}
\]

No cutoff-dependent sum is left. For face terms intersecting a source ball at distance b from cell faces, X⁺ must have diameter at least b. Thus (5.1) gives

\[
 C_F\le nA(R+1)^4 H_p(b).
 \tag{5.4}
\]

For a mixed derivative in all n sources, locality kills every term not meeting all n supports. A surviving term meets B_R containing the first source and has diameter at least d. Cauchy on the weighted source ball, followed by (5.1), yields

\[
 |\partial_1\cdots\partial_n E_a(w_z)|_{z=0}
 \le A(R+1)^4H_p(d)(n/r)^n\prod_i\nu_i.
 \tag{5.5}
\]

The same bound holds for any restricted subfamily, including bulk or face terms. Averaging bulk terms in (4.4) introduces no M factor; the outside conjugation preserves derivative moduli. Hence

\[
 B_n=2A(R+1)^4H_p(d)(n/r)^n
 \tag{5.6}
\]

suffices. Divergent short polymers at t=0 are allowed: they generate local source counterterms. Only polymers connecting separated supports, or travelling from a source to a cell face, need be summable.

## 6. Subsequence extraction and what it gives

Fix any sequence a_j→0 and Λ_j growing to cover R⁴, with the assumed estimates valid at the same fixed coarse spacing and endpoint-coupling window. For each n, compact region B_R, and separation d>0, (4.8) is a uniform multilinear bound in the test norm.

Choose a countable collection of rational smooth test functions dense in C¹ on each compact set, adapted so approximants preserve support inside prescribed mutually disjoint rational boxes. Diagonal extraction over n, rational boxes, and rational test functions gives a single subsequence on which every such connected correlation converges. For arbitrary separated C¹ tuples, approximate inside those boxes and telescope the multilinear difference. The uniform bound shows that the limits extend uniquely and do not depend on the approximants. The tensor kernel theorem then supplies distributions on configuration space away from diagonals. This is off-diagonal compactness, not tightness of random action-density distributions including contacts.

Original lattice reflection positivity passes through finite matrices of separated, half-space-supported monomials, because their entries are polynomials in the convergent connected correlations. Centering uses partitions into blocks of size at least two and needs no separate limit of the divergent one-point function. Translation invariance follows by approximating a physical translation with lattice translations, using C¹ convergence of translated smooth test functions and the same local bound. These deductions do not use cutoff uniqueness.

A single cell containing the entire tuple suffices for this local compactness statement. If two groups of insertions are translated arbitrarily far apart, its cell size could grow with the displacement. Therefore this one-cell version alone does **not** provide the time-uniform bound used to prove that the reconstructed time semigroup is a contraction, and does not by itself prove H≥0.

For that stronger conclusion use finitely many occupied cells of one fixed side ℓ, each source supported in a ball of radius R with a uniform face buffer. The same proof yields

\[
 Q=\exp[q(C_++C_-)\ell^4+2nC_{face}(R)],\qquad q\le n,
\]

independently of distances between cells. In (4.4), sum the transported averages over occupied cells, with only their own sources in each average. If q≥2, every bulk average depends on a proper subset of source variables and its all-source mixed derivative is zero; the face part remains. If q=1 use (5.5). This is the per-ball strengthening needed for time-translation uniformity. It requires a geometric placement lemma and compatible reflection tilings, but no two-cutoff estimate or uniqueness theorem.

None of this establishes nonzero limits. A separate lower witness is needed. Nor does this fixed-n compactness proof establish the all-n regularity, global growth control, O(4), forward-cone spectrum condition, or Yang–Mills identification needed for a full construction. **An ordinary coincident Euclidean random-field law is not necessarily a prerequisite for OS reconstruction.** One can work with Schwartz test functions flat on the diagonals, as the current manuscript's §4.3 does, provided the appropriate all-n bounds and a regularity order growing at most linearly with n are established. Contact extension must not be promoted to an obligatory prior step for that route. The present fixed-n estimates do not alone supply those quantitative all-n hypotheses.

## 6A. Factorial cumulant improvement under a coherent product-polydisc bound

The small zero-free-disc estimate in §4 is useful for fixed n but can be wasteful in n. If a many-cell chessboard bound is |h_n|≤Q^n, inserting Q^n into its zero-free radius produces roughly Q^{n²}. There is a better purely algebraic argument when source restrictions are coherent and a product polydisc of n-independent radius is available.

**Conditional factorial lemma.** For each finite source index set I, suppose h_I is holomorphic on

\[
 P_r(I)=\{(z_i)_{i\in I}: |z_i|\nu_i<r\text{ for every }i\},
\]

with h_I(0)=1, and restriction consistency

\[
 h_I(z_B,0_{I\setminus B})=h_B(z_B)\quad(B\subseteq I).
 \tag{6A.1}
\]

Assume |h_B(z_B)|≤Q^{|B|} on P_r(B), for every nonempty B, with the **same** Q,r. Then

\[
 \boxed{|\partial_I\log h_I(0)|\le |I|!\,(2Q/r)^{|I|}\prod_{i\in I}\nu_i.}
 \tag{6A.2}
\]

There is no assumed globally zero-free product polydisc. Only the local logarithm at h_I(0)=1 is used.

**Proof.** Put m_B=∂_B h_B(0). Product-polydisc Cauchy gives |m_B|≤(Q/r)^{|B|}∏_{i∈B}ν_i. The coefficient identity for the formal logarithm, valid analytically in a sufficiently small neighbourhood of 0, is

\[
 \partial_I\log h_I(0)=\sum_{\pi\in\mathcal P(I)}
 (-1)^{|\pi|-1}(|\pi|-1)!\prod_{B\in\pi}m_B.
\]

For n=|I| the sum of absolute combinatorial coefficients is c_n=Σ_{k=1}^n(k−1)!S(n,k). Count ordered set partitions by their positive block sizes: k!S(n,k)=Σ_{n₁+⋯+n_k=n, n_j≥1} n!/(n₁!⋯n_k!)≤n! binom(n−1,k−1). Consequently c_n≤n!Σ_k binom(n−1,k−1)/k≤n!2^n. Every product of m_B has the same bound (Q/r)^n∏ν_i. This proves (6A.2). An optional sharper constant comes from the exponential generating function −log(2−e^t), but is unnecessary.

**Application to the counterterm construction.** On one fixed reflection grid, define E^# as a functional of the source w, summing over all cells (empty-cell summands vanish). Setting a source coefficient to zero then automatically preserves the definition; it must not trigger a new grid, new subtraction rule, or a new choice of auxiliary data. With this coherence, h_I=e^{-E^#(w_I)}Z(w_I)/Z(0) satisfies (6A.1). If every source is contained in one cell with a uniform boundary buffer, the many-cell argument gives Q^{|I|} with

\[
 Q=\exp[(C_++C_-)\ell^4+2C_{face}(R)].
\]

At product radius r, the local-polymer proof also replaces the Cauchy factor (n/r)^n in the mixed-counterterm derivative by r^{-n}. Thus, when all its uniform geometry and source-domain assumptions hold,

\[
 |S_n^T(\vec f)|\le
 \{2A(R+1)^4H_p(d)r^{-n}+n!(2Q/r)^n\}\prod_i\nu_i.
 \tag{6A.3}
\]

This is an actual factorial improvement over a Q^{n²} logarithm estimate for that source class.

**Obtaining a product source domain.** For disjoint real supports and ν_i-normalized test functions, a pointwise source w=Σ_i z_i f_i has sup norm and Lipschitz norm bounded by a constant times max_i|z_i|ν_i, rather than their sum. For the Lipschitz bound, along a segment joining two different supports, use the portions between each endpoint and its first exit from that support; the two lengths sum to at most the total distance. A safe bound is

\[
 \|\operatorname{Re}w\|_\sharp+\|\operatorname{Im}w\|_\sharp
 \le4\max_i|z_i|\nu_i.
\]

Therefore a source theorem formulated for arbitrary finite real families with weighted coefficient budget ρ applies pointwise to the two-element family (Re w, Im w) with coefficients (1,i), for max|z_i|ν_i≤ρ/8. Holomorphy near a given z⁰ follows by adding the real family (f_i) to (Re w_{z⁰}, Im w_{z⁰}) with small increment coefficients, using the strict remaining budget; these neighbourhoods cover the product polydisc. This argument requires the same local term to be defined consistently as a functional of the weight, independent of its chosen presentation. For chessboard replicas use the same pointwise norm reasoning, with the uniform face buffer controlling the joined profile.

**Unresolved geometry, explicitly.** This does not yet prove (6A.3) for arbitrary n-tuple supports. The account's placement lemma chooses a common cell size ℓ of order n(R+1), so Q itself grows with n. Arbitrary balls cross any proposed fixed grid, and an unsupported assertion that a partition of unity fixes this is invalid: patches assigned to different shifted grids do not automatically share a chessboard inequality or a coherent holomorphic subtraction. One must prove an n-independent geometric reduction, or quantify losses in a different reduction and show they satisfy the required OS regularity. The factorial lemma removes an analytic/combinatorial inefficiency; it does not solve this geometry or verify the Yang–Mills source bounds.

## 6B. Why allowing interface counterterms is not automatically enough

A possible fixed-grid remedy is to restrict a source to each cell even when it does not vanish at the face, then reflect that restriction. For a real source the even reflection preserves continuity and a controlled Lipschitz constant. Complex chessboard reflection conjugates the source, creating an imaginary jump at the face. A piecewise-Lipschitz source theorem with interface counterterms would therefore be relevant, but there is a separate obstruction to using it in the holomorphic bound above.

Interface counterterms can mix z and conjugate z, producing |z|². Such a real expression is not the real part of a holomorphic function. Consequently one cannot assume that the bulk recentering trick automatically extends to interface energies.

An exact finite Gaussian model isolates the issue. Let (X₊,X₋) be a centered reflection-symmetric Gaussian pair with Var X₊=Var X₋=A and Cov(X₊,X₋)=B, 0≤B≤A. This pair is reflection positive: its conditional Gaussian transition operator has nonnegative Hermite eigenvalues (B/A)^k, including the degenerate endpoints by limits. Cauchy–Schwarz/RP applied to F_z=e^{zX₊} gives

\[
 |\mathbb E e^{zX_+}|
 \le(\mathbb E e^{zX_++\bar zX_-})^{1/2}
 =\exp[\tfrac12A\operatorname{Re}z^2+\tfrac12B|z|^2].
 \tag{6B.1}
\]

After the exact holomorphic source subtraction Az²/2 the true normalized generating function is identically 1, yet the chessboard upper bound is exp(B|z|²/2). If B=B_a→∞, this bound is not cutoff-uniform on any fixed complex disc. No further holomorphic subtraction J_a with J_a(0)=0 can make this upper bound uniformly bounded on an entire fixed disc: on a circle |z|=r, the mean of Re J_a is zero, whereas the mean of B_a|z|²/2 is B_a r²/2. This is a limitation of that upper-bound method, not a counterexample to boundedness of the actual renormalized generating function.

The surface scale is significant. A positive covariance behaving as |x−y|^{-8} in four dimensions produces an opposite-half-space cross integral of surface order a^{-3} when regularized at distance a, rather than a bounded face remainder. For the diagnostic kernel (|x−y|²+a²)^{-4}, integration over tangential differences gives π²[(u+v)²+a²]^{-5/2}/8 and integration over positive normal distances u,v gives π²a^{-3}/24 per unit face area, up to support cutoffs and lower-order terms. This diagnostic integral is not asserted to be the exact Wilson covariance; logarithmic running modifies it by corresponding logarithms, not by making it uniformly finite.

Thus a successful interface route needs more than spatially local face vacuum counterterms. Possible targets are a sharper normalized mixed-source inequality which cancels the single-source face contributions before taking moduli, or a different holomorphic renormalization construction with a proven uniform residual bound. Distinct-label mixed derivatives annihilate many single-source |z_i|² costs, but ordinary Cauchy estimates on a holomorphic generating function do not automatically exploit that cancellation. No such improved inequality is proved here.

## 7. Exact interface with the available Bałaban/account statements

The relevant original works are Bałaban, *Renormalization group approach… I*, CMP 109 (1987), 249–301; *II. Cluster expansions*, CMP 116 (1988), 1–22, [DOI](https://doi.org/10.1007/BF01239022); *Convergent renormalization expansions*, CMP 119 (1988), 243–285; *Large field renormalization II*, CMP 122 (1989), 355–392, [publisher record](https://link.springer.com/article/10.1007/BF01238433). The publisher record confirms the last paper's ultraviolet-stability claim. Full original PDFs were not obtained in this pass; equation-level uses below are traced through the repository and must be checked against originals before claiming discharge.

| Required interface | Relevant available statement | What it does / does not establish here |
|---|---|---|
| Unsourced density lower bound (2.2) | Raw I 2573–2582, clause (i-b), quoting CMP 122b Theorem 1 / (0.1); also raw I 154028 onward | A lower effective-density bound of the needed form is the right starting input. Verify vacuum normalization, measure, and coarse physical units. It is not a bound for the unrenormalized bare partition function. |
| Uniform χ-window | Raw I 155039–155083, `4.31:lem-window-characteristic`; CMP119 (2.16)–(2.17), CMP102b Thm 1 (7)–(8) | Supplies a possible route from a fixed coarse plaquette window to χ=1. Combined with a uniform endpoint coupling window it gives a fixed Haar ball. The product-Haar denominator proof is elementary once this is verified. |
| Complex-source upper bound (4.2) | Raw II 60731–60739, properties (S),(F); raw II 61781–61817 explains its five ingredients | **Not** an immediate consequence of unsourced stability. The account needs sourced inductive format, complex-weight modulus bounds, running-shift control, and the modulus-sum argument of CMP119 (2.49)–(2.50). These are the main remaining model-specific estimates. |
| Local analytic source counterterms | Raw II 60700–60730, (L),(A),(B) | These source-dependent assertions come from the correlation theorem, not simply from the unsourced partition-function theorem. The source support dependence must be uniform and genuinely local. |
| Anchored polymer sum (5.1) | Raw II §6.2, localised-term bound and tree-sum lemma; CMP116 (1.26) is the cited tree-graph bound | Individual exp(−κ tree length) bounds plus an anchoring/counting estimate can imply (5.1). Need check the retained rate, enlarged support diameter, scale-counting factor, and all-volume constants. The displayed theorem is conditional until that translation is done. |
| Replicated complex sources | Raw II 61755–61779, transported-weight remark | Even/odd grouping loses radius factor two, not volume factor. This is essential: no admissible source domain shrinking like 1/M. |
| Chessboard inequality | Raw II 61205 onward, `6.2:lem-chessboard-estimate`; summary PDF §3.5 | Gives (4.1) from Wilson reflection positivity. It is applied at the original measure, so the RG effective measure need not itself preserve reflection positivity. |
| Existing full reduction | Raw II 63964–64274, `6.4:thm-per-ball-bound` | The account already contains substantially this recentering/chessboard strategy. The present note isolates a smaller direct fixed-spacing interface and elementary denominator estimate; it is not claimed as a new chessboard mechanism. |

The obsolete-looking change-of-units obstacle can therefore be replaced by a concrete verification target: prove, **at a fixed coarse physical spacing and a fixed endpoint inverse-coupling interval**, the residual complex-source upper estimate (4.2) and local polymer hypothesis (5.1), with the same vacuum normalization as (2.2). The lower bound then follows from the explicit Haar-ball computation, and off-diagonal subsequential compactness follows from the displayed theorem.

## 8. What cannot be bypassed by this argument

* If the constants in (4.2) grow with the full volume, the chessboard root leaves that growth. If C_+(a) diverges, then r₀→0 and the cumulant bound diverges. Taking a subsequence does not correct either defect.
* A bound on Zhat(0) alone says nothing about source derivatives. An abstract reflection-positive constant random field X_a(x)=M_a σ, σ=±1 equally likely, has normalized partition function 1 at zero source and divergent separated two-point function M_a². This is a logical counterexample to inferring correlations from unsourced normalization, not a Wilson-model counterexample.
* A real-source pressure bound without a holomorphic counterterm and a uniform complex neighbourhood does not directly give Cauchy bounds for all mixed derivatives. Complex-source stability is an actual required input here.
* A one-source counterterm subtraction Σ_iE_a(z_if_i) is insufficient when a local polymer meets several separated supports. Their finite mixed contribution must be bounded, as in (5.5), rather than discarded.
* A continuum construction stronger than fixed-n separated scalar compactness needs additional arguments. For an OS route on test functions flat on diagonals these include quantitative all-n bounds and the relevant regularity; a positive coincident Euclidean random-field measure is not automatically required. This note removes uniqueness from the minimal route; it does not transform ultraviolet stability alone into a Clay-problem solution.

## 9. Next focused verification

1. Fix one physical coarse spacing and explicit endpoint window. Trace the source-independent vacuum normalization from the original bare measure through the exact RG integral identity. Verify the lower-density and χ-window hypotheses, then record C_- from (2.3).
2. Prove only the source class needed for chessboard replicas: bounded real profiles supported a fixed distance from cell faces, and their two even/odd complex coefficients. Do not assume a general two-cutoff or tensor-source theorem.
3. Prove (4.2) in that class by the sourced one-run induction and modulus sum, with constants expressed through the fixed endpoint window. Prove (5.1) by anchoring the local vacuum terms to a source ball and retaining a positive tree-decay rate.
4. Apply (4.8), the diagonal extraction, and separately a lower two-point witness. The last item remains independent of compactness and must not be smuggled into a normalization estimate.
