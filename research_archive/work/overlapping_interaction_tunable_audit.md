# Independent audit: tunable real-baseline cutoff expansion

17 October 2026. This audits Sections 13–14 of
`overlapping_interaction_cutoff_research.md`, including the optional
Chernoff parameter in (13.3a). It supplements
`overlapping_interaction_cutoff_audit.md`. The conclusions below concern
the abstract theorem under its displayed assumptions; they do not verify
the deposited Yang–Mills neighborhoods or dimension/cutoff choices.

## Result

The tunable marked theorem and tunable strict-support theorem pass this
independent audit. One necessary statement clarification was identified:
the correlated tail lemma must specify a **centered** real Gaussian.
Covariance bounds alone do not control an arbitrary mean. Every dominating
Gaussian used in the proof is centered, so this clarification changes no
application or constant. They replace the
fixed \(\exp(cD)\) density factor paid by interaction cells with a tunable
\(\exp(O(\theta D))\) factor. They retain an explicit tradeoff in the
Cauchy radii, permitted precision perturbation, and bad-cell tail.

## 1. Relative-density comparison

For \(\|F\|\le\theta<1\), the identity

\[
 (1+\theta)\operatorname{Herm}(I+F)-(I+F)^*(I+F)
 =\theta I-(1-\theta)\operatorname{Herm}F-F^*F
\]

has a nonnegative right side, since
\(\operatorname{Herm}F\le\theta I\) and \(F^*F\le\theta^2I\).
Congruence by \((I+F)^{-1}\) therefore gives

\[
 \operatorname{Herm}(I+F)^{-1}\ge(1+\theta)^{-1}I.
\]

Combining this with the singular-value bound
\(|\det(I+F)|\ge(1-\theta)^N\) proves exactly (13.1), including its
normalization. The real baseline is essential to the stated dominating
real Gaussian.

## 2. Correlated bad-cell estimates

For a centered real Gaussian, the all-bad event for \(k\) disjoint
\(D\)-dimensional cells implies
\(\sum_i\|G_i\|^2>kR^2\). Its marginal covariance is bounded by \(LI\),
so the determinant formula and exponential Markov inequality prove
(13.2) without independence. Expanding the nonnegative product in (13.3)
then proves the singleton mixture bound term by term.

For the optional parameter, taking

\[
 t=\frac{\sigma}{2(1+\sigma)L}
\]

gives \(1-2tL=(1+\sigma)^{-1}\). Thus the exact sufficient tail factor is

\[
 p_{\sigma,R}(L)
 =(1+\sigma)^{D/2}
   \exp\!\left[-\frac{\sigma R^2}{2(1+\sigma)L}\right],
\]

as written in (13.3a). This factor need not be below one before the theorem's
smallness conditions are imposed. Choosing \(\sigma\) of order \(1/D\)
removes its exponential dimension prefactor but weakens the exponent to
order \(R^2/D\); it does not remove the dimension cost of making a large
cell unlikely to be bad.

## 3. Small complex covariance family

Partition pinching is an operator-norm contraction, including on general
complex matrices. The molecule forest mask is a convex combination of
such pinchings. Consequently the background covariance difference at
every forest point is at most \(\theta\lambda/2\). The selected-edge
Cauchy polydisc contributes another \(\theta\lambda/2\), using the
majorant for the actual covariance entries. Relative to the real masked
baseline, whose smallest eigenvalue is at least \(\lambda\), the total
relative perturbation is at most \(\theta\).

The density cost is therefore
\(K_\theta^{|M|}\), where
\(K_\theta=[(1+\theta)/(1-\theta)]^{D/2}\), and the real dominating
covariance is bounded by \((1+\theta)\Lambda_0 I\).
Expanding the bad singleton choices, then applying the correlated tail
bound, gives the product molecule majorant used by the original endpoint
tree argument. There is no hidden product-measure assumption.

For the exactly real constant covariance, assigning the entire budget
\(\delta_\theta=\theta\lambda\) to the Cauchy perturbation is valid.
Operator closeness alone remains insufficient for strict variable
background support, as the statement correctly says.

## 4. Strict-support density factor

With \(\delta=\theta\lambda\), the deformed baseline retains the earlier
spectral and weighted Schur estimates. The estimates for its inverse and
the support-algebra covariance perturbation therefore remain valid with
the updated \(L,v_1,u,w\).

The complex baseline density costs
\(K_\theta^{|M|}\). The support-dependent determinant costs at most
\((1-u)^{-D|M|/2}\). For the inverse correction,

\[
 \|x\|^2\le\Lambda_0 x^TC_{r,M}^{-1}x,
 \qquad
 \frac1{1+\theta}-w\Lambda_0
 \ge\frac{1-\theta}{1+\theta}.
\]

Thus the final dominating covariance is
\(\rho_\theta C_{r,M}\), with
\(\rho_\theta=(1+\theta)/(1-\theta)\). Its normalization relative to
\((1+\theta)C_{r,M}\) contributes another
\((1-\theta)^{-D|M|/2}\). Together with \(u\le\theta\), the complete
prefactor is exactly

\[
 \mathcal K_\theta^{|M|},\qquad
 \mathcal K_\theta
 =\left[\frac{1+\theta}{(1-\theta)^3}\right]^{D/2}.
\]

The bound \(v_1\le\lambda/4\) follows from the displayed assumptions:
\(v_1\le\theta/L\), \(L\ge4/\lambda\), and \(\theta\le1/4\) actually
give the stronger \(v_1\le\lambda/16\). The updated density is therefore
well defined throughout the relevant complex polydiscs.

The support-algebra formal factorization, molecule endpoint recursion,
Mayer expansion, and hull map use precisely this density majorant. Their
previous proofs carry over, including the strict-support interaction
comparison. The replacement does not introduce a dependence on the full
volume into the local density constant.

## 5. Dimension tradeoff and scope

For \(0<\theta\le1/4\),

\[
 \log K_\theta\le\frac{16}{15}D\theta,
 \qquad
 \log\mathcal K_\theta\le\frac52D\theta.
\]

Hence \(\theta=1/(4D)\) gives the claimed constants
\(e^{4/15}\) and \(e^{5/8}\). The covariance-edge factor then grows like
\(D\), and the precision neighborhood shrinks according to (14.1).
Describing this as a polynomial loss is justified only with the other
baseline constants fixed, as stipulated in the note.

The result removes a particular density prefactor from the interaction
support norm. It does not establish the actual source covariance's
closeness to a real reference, the small local precision decomposition on
the required product background domain, the dimension/cutoff tail
budget, or uniformity over renormalization histories. Those source
interfaces remain separate.

## Fragment fidelity

The no-preamble `tunable_gaussian_overlap_fragment.tex` was also checked.
Its formulas, the use of the free \(\sigma\) parameter in both the marked
and strict versions, and the stated dimension tradeoffs match the audited
research argument. The centered-Gaussian clarification above has been
made and checked in both versions.
