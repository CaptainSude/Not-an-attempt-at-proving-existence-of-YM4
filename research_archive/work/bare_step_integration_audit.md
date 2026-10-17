# Independent audit: bare first-step small-field integration

17 October 2026. Read work/bare_step_integration_fragment.tex and checked its use of the audited current-step chart, local measure module, and Notebook18 tunable strict-support theorem. The candidate was not edited by this auditor. One domain clarification was requested and adopted by the parent during this audit.

## Result

Pass after the adopted gauge-insertion domain correction. The argument proves a convergent representation of the explicitly defined bare M=1 constrained, gauge-weighted, retained-window integral on its small physical stationary branch, uniformly in compatible periodic volume. Its holomorphic product-background extension is a centered extension. This is not a proof for arbitrary nonstationary backgrounds of the unmodified action, and it neither includes the chart complement nor performs a later quantum step.

## 1. Actual local precision and action remainder

At M=1 the homogeneous minimized action is the original Wilson action: the original and current lattices coincide, and the identity-scale constraint fixes the original configuration. Thus no unproved localization of an earlier minimized action is used.

Every plaquette reads four links. Each pivot field in Phi_V reads a fixed neighborhood and depends on only its own nonlinear pivot equation. Composing a plaquette with Phi_V therefore produces a finite-support analytic primitive f_r. The same is true of every internal contour penalty. Background, fluctuation, and constraint-curvature dependencies are included in Y_r. The number of these primitive supports meeting a cell and their size are uniformly bounded at fixed L.

Differentiating these full local primitives gives exactly

\[
 A(V)-A_0=\sum_r\{D_x^2f_r(V,0)-D_x^2f_r(1,0)\}.
\]

Each term reads only V|Y_r and has both matrix indices in Y_r. Local background Cauchy estimates give the stated weighted label norm O(b). This is precisely the support-valued precision hypothesis needed by Notebook18, rather than merely locality of the summed matrix. The full absolute gauge Hessian and both action chart-curvature terms are retained by this differentiation.

The subtraction defining v_r^act is exact on the entire product background ball. Taylor in the scalar parameter t in f_r(V,tz), using the fixed-dimensional local fluctuation polydisc, gives O(gR^3) without a volume factor. There is no dependence on the preceding fine-scale dimension because M=1. The source gauge remainder is already included in f_r and is not added twice. The straightening and Haar estimates from the measure module add O(gR) and O(g^2R^2).

On the physical stationary family the sum of the linear terms is zero, while the constant sum is the original classical action because the gauge penalty is zero. This proves the exact physical identity. Away from that family, the separately defined centered extension is correctly distinguished from the original integral.

## 2. Retained rectangles and closing the cluster hypotheses

There are dL^d positive current bonds and d removed pivots per assigned L-cell, so the retained cell dimension is d(L^d-1)dim(g) in the stated compatible pivot geometry. Periodic occurrences must retain their multiplicities, as the candidate specifies.

The actual cutoff is a product of retained bond-color balls. Its cell bad event implies the Euclidean cell norm is at least R. The joint Gaussian tail lemma therefore dominates it with the same R; independence is not needed. The molecule identities only use fixed cell indicators, their product structure, and that joint tail domination. They do not require the indicator to be exactly a Euclidean cell ball. Interaction bounds are taken on the actual rectangle, where local bond suprema are at most R. No erroneous replacement of a pivot indicator is made.

The flat real covariance has a volume-uniform spectral interval and exponential weighted row norm. Choosing kappa<m with kappa+2m below that exponent leaves the required positive exponent margins. All other strict-support constants are then finite at fixed L. Since the support-valued precision norm is O(b), a volume-independent b can satisfy every precision smallness inequality before g is selected.

Taking a_0=4+log Kcal_theta incorporates exactly the support cost in the tunable overlapping theorem. The interaction budget is O(gR^3), and the bad-cell budget has a fixed positive Gaussian rate in R^2. Both budgets and the local chart condition hold for sufficiently small g with logarithmic R(g). The quarter budgets yield the stated O(gR^3) comparison with the cutoff-only expansion. Thus the conclusion follows from the fully matched strict-support theorem and its periodic extension.

## 3. Gaussian determinant: exact closed-chain norm

The determinant expansion has the correct sign and order:

\[
 -\tfrac12\log\det(A(V)A_0^{-1})
 =\tfrac12\sum_{n\ge1}\frac{(-1)^n}{n}
       \operatorname{Tr}[(C_0B(V))^n].
\]

An expanded trace term is a closed chain of alternating covariance links and precision-label matrices. A label's input and output cells belong to its support. Chosen shortest paths for the covariance links and spanning trees for the labels therefore form one connected hull containing the trace root and every background coordinate read by the term. If ell is the sum of the chosen path and tree lengths, the graph bounds |H|<=1+ell and d(i,j)<=ell for j in H are valid even with repeated labels and periodic wrapping.

For a fixed initial trace cell i, the color trace contributes at most D times the product of the block norms. Successive weighted covariance row sums and precision-label row sums bound the total order-n absolute weight by D(K_t nu_t)^n. The final return to i only restricts a sum already bounded without that restriction. No extra factor of the number of labels, volume, or n is missing.

For a_d+beta<=t, rerooting to j in H costs at most e^(a_d)e^(-beta d(i,j)) times the rooted t-weighted bound. The periodic sum over possible roots is bounded by the corresponding lattice sum. Summing the remaining 1/n series yields precisely the displayed -log(1-K_t nu_t), hence an anchored O(b) norm. Each trace term reads only the backgrounds on its labels, all contained in H. Absolute convergence justifies the grouping into holomorphic H-activities. The path choice need not preserve discrete rotations; no such symmetry of individual activities is claimed.

## 4. Exact Haar and delta constants

For normalized Haar measure d_H(exp(iX))=c_H j(X)dX with j(0)=1, the normalized group delta pulls back to c_H^-1 delta(X). Therefore the original positive-bond Haar factors and one group constraint per positive coarse bond produce c_H^(N_b-N_c).

The exact ambient straightening followed by linear pivot elimination gives D(V)=product_c det(A_p)^-1 and the normalized local Jacobian. Scaling the retained variables contributes g^n with n=q(N_b-N_c). The remaining ordinary Gaussian integral contributes (2pi)^(n/2)det(A(V))^-1/2. Splitting this into the baseline determinant and Q(V) gives exactly the candidate's formula, with no missing g, L, color-dimension, or group-volume factor. The L normalization is already in A_p=L^(1-d)pi_c. The local Haar logarithms account for the full products j(Phi_V(gz)(b)).

The background-dependent D(V)/D(1) is retained outside the small fluctuation correction; it is not silently dropped. Its local logarithm is -sum Tr log pi_c, with O(b) size but no coupling suppression.

## 5. Gauge insertion: required domain correction

The scalar gauge-average calculation is correct. For rooted site gauges, P_{U^u}(y,x)=P_U(y,x)u(x)^-1, so integrating each independent noncenter u(x) against normalized Haar gives z_G(g), independently of U. A gauge-invariant constrained measure on an invariant domain then satisfies the insertion identity with factor z_G(g)^(-N_s).

The first draft described this as an unrestricted full constrained integral identity. The source contour mean and ordinary logarithmic average are established on an admissible orbit domain, not automatically on every configuration. I requested that the identity explicitly assume a rooted-gauge-invariant domain on which both maps are defined and equivariant. The parent adopted that condition and explicitly disclaimed a globally defined averaging map. The local chart integral is unaffected by this correction.

The candidate also correctly says the identity is applied before restricting to a nongauge-invariant sharp chart piece. It does not identify the chart piece of the uninserted integral with the same sharp piece after insertion. The resulting gauge-weighted chart piece can subsequently be multiplied by the known external scalar in an admissible-domain decomposition.

## 6. Scope retained

The strict supports refer to independent current link backgrounds V. Substituting the physical minimizer V_*(W) need not preserve those supports. A theorem in W, a later-step theorem for prior quantum interactions, and control of the complement remain distinct. The chosen integral includes exactly the retained cutoff and chart restriction, with no undeclared extra source indicators. Within those stated limits, no remaining mathematical correction was found.
