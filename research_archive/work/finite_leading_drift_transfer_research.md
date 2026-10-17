# Qualitative transfer of a positive leading block drift to finite regulators

17 October 2026. A conditional compactness lemma for the actual homogeneous local macrostep. The compactness and moment-passage inputs are established in the preceding modules. The new positivity hypothesis below remains unproved. No finite-volume convergence rate is required.

## 1. Fixed data and the actual block coefficients

Fix the primitive ratio, elementary composite ratio \(R\), grouping \(J\), common analytic domains, and extraction convention. Fix a finite integer \(q\ge1\), preferably a multiple of the already proved activity-envelope block length \(q_a\). These data are chosen before taking a regulator limit.

Use the compatible nested cubic period family \(\mathcal P\) from the finite classical leakage theorem. In particular every fixed power of \(R\) divides all sufficiently late periods in this family. For a block of \(q\) steps with final period \(N\in\mathcal P\), set
\[
 M_j=MR^j,\qquad Q_j=R^{q-j}N,\qquad 0\le j\le q.
 \tag{1.1}
\]
The preceding depth \(M\) is any permitted homogeneous depth. Let \(D_{M_j,R;Q_{j+1}}\) be the actual finite leading correction \(\Delta+\mathcal Q_{\det}\) for step \(j\), as a function on the output torus of period \(Q_{j+1}\). Define
\[
 b_{0,j}^{M,N}
   =\beta_{M_jR,Q_{j+1}}(D_{M_j,R;Q_{j+1}}),\qquad
 B_q(M,N)=\sum_{j=0}^{q-1}b_{0,j}^{M,N}.
 \tag{1.2}
\]
Each beta is the actual finite short-lift ratio, normalized by its own actual finite classical reference. It is not replaced by a true infinite moment at finite \(N\). The coefficients in (1.2) are real with the real determinant branches and real source data.

Uniform leading-family and finite-moment bounds imply
\[
                     |b_{0,j}^{M,N}|\le B_0
 \tag{1.3}
\]
above a fixed reference threshold, uniformly in \(M,N,j\). The constant can depend on the fixed geometry and analytic radii. For example, use the leading correction's uniform outer-radius family bound and the finite Hessian-moment estimate; the reference denominators are bounded below by \(1/2\).

## 2. Exactly which infinite limits are relevant

Consider any sequence \(M_n\) of permitted old depths and \(N_n\in\mathcal P\) tending to infinity. The \(M_n\) need not stay bounded or converge. Extract jointly:

* the classical reference actions, background maps and their required fixed-order vertices at the shifted depths \(M_nR^j\);
* the actual retained flat precisions and covariances for each fixed step geometry;
* the leading corrections \(D_{M_nR^j,R;R^{q-j-1}N_n}\), for \(0\le j<q\);
* if the structural system used in a reference comparison requires it, every further fixed depth shift and fixed endpoint power.

The fixed-radius strict support bounds, the DMT exponential source-Hessian bounds, and the complete-output background bounds are uniform in old depth. Analytic-interaction compactness therefore supplies such a joint subsequence. The cofinal period condition permits every fixed extra endpoint comparison eventually, exactly as in the varying-depth finite leakage argument.

Denote the limiting leading corrections by \(D_j^*\), the true infinite Maxwell functional at their output scale \(j+1\) by \(\beta_{j+1}^*\), and put
\[
                         B_q^*=\sum_{j=0}^{q-1}\beta_{j+1}^*(D_j^*).
 \tag{2.1}
\]
The indices label the successive output scales in this structural limit; they do not assert that the system equals one at a fixed finite depth \(M_*\).

These limits can be taken as actual structural limits of the determinant formula, not merely arbitrary scalar kernels. The retained fiber per current block has fixed finite dimension for fixed \(R\); the dimension of the whole retained operator still grows with volume. Uniform local convergence and exponential matrix envelopes pass products and the inverse identity \(A_0C_0=I\) by truncating the intermediate sums. The actual local chart and pivot maps are fixed, and classical scalar vertices through fourth order converge by common-domain Cauchy estimates. DMT's absolutely convergent trace formulas therefore pass to the same limit. Equivalently one may extract the strict leading scalar families jointly and identify their Hessians by that formula. No microscopic old-depth coordinate count is involved.

## 3. The moment-passage lemma

For every such jointly extracted subsequence,
\[
                   b_{0,j}^{M_n,N_n}\longrightarrow
                       \beta_{j+1}^*(D_j^*)\qquad(0\le j<q),
 \tag{3.1}
\]
and consequently
\[
                             B_q(M_n,N_n)\longrightarrow B_q^*.
 \tag{3.2}
\]

Proof. For a fixed \(j\), the source Hessian kernel of the finite leading correction converges locally and has a common exponential row bound, by DMT and the strict leading-family bounds. The short-lift second moment is handled in two parts. At any fixed displacement radius, all entries and their moments converge. Beyond that radius the exponential bound gives a common summable second-moment tail. The finite short-lift cutoff tends to infinity because \(Q_{j+1}=R^{q-j-1}N_n\) does.

The actual finite reference denominator tends uniformly to one by the normalized flat classical \(q_{M_jR}\) periodization estimate, even when \(M_j\) varies. Division therefore gives (3.1). There are only \(q\) terms, so (3.2) follows. No convergence of an extensive total, replacement of the full nonlinear finite reference, or quantitative regulator rate has been used.

## 4. Conditional uniform positive transfer

**Unproved structural-limit positivity hypothesis.** There exists \(\delta>0\) such that every joint structural infinite limit obtainable as in Section 2 satisfies
\[
                                      B_q^*\ge\delta.
 \tag{4.1}
\]
The same \(\delta\) must work for all sequences of old depths and allowed periods. Positivity for one chosen fixed-depth limit does not suffice.

**Proposition.** Under (4.1), for every \(0<\varepsilon<\delta\) there is a period threshold \(N_*(\varepsilon)\), independent of \(M\), such that
\[
       B_q(M,N)\ge\delta-\varepsilon
       \quad\text{for every permitted }M,\ N\in\mathcal P,\
                         N\ge N_*(\varepsilon).
 \tag{4.2}
\]
In particular, \(B_q(M,N)\ge\delta/2\) above one uniform threshold.

Proof. If (4.2) failed, choose a sequence \(N_n\in\mathcal P\), \(N_n\to\infty\), and arbitrary old depths \(M_n\), for which \(B_q(M_n,N_n)<\delta-\varepsilon\). Extract the joint structural subsequence from Section 2. Equation (3.2) gives
\[
                         B_q^*\le\delta-\varepsilon,
\]
contrary to (4.1). This contradiction supplies the uniform threshold. It supplies no explicit value or rate for that threshold.

Uniformity in a block's starting stage is automatic: its preceding depth is just a new permitted \(M\), and its \(q\)-step final period is the \(N\) used in (1.1). Hence the same threshold applies to every such block in a permitted finite history whose block-output period is above it.

## 5. Consequence for finite tuning, without a convergence rate

Suppose \(q\) is a multiple of \(q_a\). On the actual finite activity envelope the already proved decrement comparison is
\[
 |d_j(g,x_j)-b_{0,j}|
 \le C_{\rm int}\omega(N_{\min})
     +C_{\rm par,\beta}\{\tau(T(g))+g^2T(g)^6\}
     +C_{\rm in,\beta}gT(g)/b.
 \tag{5.1}
\]
The first term tends to zero qualitatively with the period threshold; the remaining terms tend to zero in the weak-coupling limit at fixed \(b\) and the chosen real \(T(g)\).

Use (4.2) with \(\varepsilon=\delta/2\). Then raise the period threshold and lower the weak-coupling ceiling until the right side of (5.1) is at most \(\delta/(4q)\). Every admissible \(q\)-step block has
\[
             \frac{\delta}{4}\le
                 \sum_{j=k}^{k+q-1}d_j(g_j,x_j)
                 \le qD_{\rm abs}.
 \tag{5.2}
\]
Here the upper bound is the existing absolute-increment bound. The activity envelope is preserved by repeating its \(q_a\)-blocks, so no direct large-endpoint field-dilation estimate or new radius is invoked.

These are exactly the positive block bounds required by the conditional clipped-recursion shooting argument. That argument then tunes finite histories of \(mq\) steps to a fixed terminal inverse coupling at least \(\Gamma_{\rm w}+qD_{\rm abs}\), with
\[
 \Gamma_*+m\delta/4\le\gamma_{\rm initial}
                           \le\Gamma_*+mqD_{\rm abs}.
 \tag{5.3}
\]
All of this remains conditional on (4.1). It does not require a quantitative finite-volume convergence estimate.

If one wants the averaged-drift formulation for arbitrary finite interval lengths, (1.3) and the finite \(q\)-block lower bound also supply it. Write \(n=mq+r\), \(0\le r<q\), and partition the interval into complete blocks and a final fringe. If all its periods are above the common threshold,
\[
 \sum_{j=k}^{k+n-1} b_{0,j}
     \ge m\delta/2-rB_0
     \ge c n-C_{\rm fin},
 \quad
 c=\frac{\delta}{2q},\quad
 C_{\rm fin}=(q-1)(B_0+c).
 \tag{5.4}
\]
The shooting proof needs only the fixed-block version, so the fringe estimate is optional.

## 6. Scope of the remaining hypothesis

The hypothesis concerns every actual varying-depth structural limit. An infinite determinant cocycle or reference comparison can help prove (4.1), but its positivity and uniform positive margin are not established by compactness, the trace formula, or the cocycle alone.

More concretely, include the one fixed long-ratio \(R^q\) determinant in the joint extraction. The proved leading cocycle and true infinite classical Maxwell preservation identify
\[
                       B_q^*=\beta_q^*(D_{0,R^q}^*).
\]
Thus a uniformly positive reference comparison for that long-ratio coefficient in every structural limit would verify (4.1). This is an equivalent conditional target, not a new sign proof.

Once that structural positivity is proved, qualitative compactness is enough to transfer the needed fixed-block finite lower bound. A separate exponential finite-volume rate is unnecessary for this purpose. There is no claim of exact finite marginal additivity, summability of errors along an infinite history, old-depth convergence to one unique system, a drift sign without (4.1), or convergence of tuned local densities to a continuum measure.
