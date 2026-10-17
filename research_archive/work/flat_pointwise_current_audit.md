# Independent audit of the pointwise flat current neighborhood

16 October 2026. Reviewed all seven sections of `flat_pointwise_current_research.md`, using the independently passed pointwise baseline inverse, scalar Z formulas, full-current Hilbert neighborhood, fixed-step constraint-current proof, and the source obligations recorded in `source_flat_weak_norm_match.md`. **Pass within the stated bounded-forcing homogeneous scope. No mathematical correction found.** The right-divergence Hölder-input members remain explicitly outside this result.

## 1. Scalar heat and finite-rank estimates

The high diagonal of Z is the t-weighted high-heat integral. Splitting the scalar heat semigroup into a fixed number of equal factors proves the weighted kernel derivative bound of any fixed integer order from the already established first-difference bound. Input derivatives can be put on the kernel by summation by parts. Interpolating output differences of adjacent orders gives the fractional Hölder cost. The resulting small-time integral is

    integral_0^1 t^(1-(m+beta)/2) dt,

which converges precisely in the range m+beta<4 used here. The specific requirements are valid: ZL has total order two; DZL has order three; the C^(1,beta) output of DZ requires total order two plus beta; and the C^(1,beta) output of DZD* requires total order three plus beta. The last is why a fixed beta_0<1 is important. Large times have the established high-alias gap.

For the finite-rank part of Z, the high vector is a_r/P_r^2. Each input rank row used here has at most three derivative powers and remains uniformly in alias l2. The output vector with derivative/Hölder order s<4 has absolute alias majorant w_alias(r)|r|^(s-4); the dyadic shell bound C(j+1)^(d-1) makes its sum finite uniformly. Central blocks are bounded by the canceled formulas. This proof uses physical L2 input rows acting on one bounded unit cell and therefore has no growing-dimensional norm loss.

Reconstruction, enlarged-chart gluing, and contour shifting apply to the full operators and to the prescribed output-collar Banach norms, as in the passed baseline argument. The pieces need not individually be periodic. This establishes the weighted and periodic versions of all four scalar estimates in (2.1).

## 2. The weighted N argument is legitimate

The note uses complete global fields; it does not sharply cut a differentiable field before taking D*. If N_w(A) is finite, the actual backward differences entering D*A are bounded on the stated output collars. Adjacent-cell weight ratios are bounded independently of eta, so D*A has the needed weighted sup norm without a false eta^-1 boundary term.

Consequently Lambda A=ZL D*A and D Lambda A=DZL D*A are bounded by N_w(A), as in (2.3). This proves Pi:N_w->weighted sup, not Pi:sup->sup. Every later occurrence of Pi uses exactly the former statement. The coarse weights have a fixed multiplicative Lipschitz ratio, so cellwise localization of an already formed forcing is harmless; no derivative is then taken of those sharp cell pieces.

## 3. Auxiliary factorization and derivative placement

From the fixed scalar identities,

    G0 Lambda*=DZ,
    G0(D Lambda)*=DZD*,

the four terms of G0 Theta'_J are exactly

    G0 j_J* Lambda + DZ j_J
       + DZ V_J D Lambda + DZD* V_J* Lambda.

The finite-incidence coefficient maps and their transposes act on weighted sup fields with norm O(||J||_infinity); their physical site and bond measures agree. The three outside propagators map bounded data to N_beta, and the two inside scalar-gauge legs are bounded on N. This proves (3.3) with the displayed constant. It never differentiates J. Choosing the smoothing constants at beta_0 and comparing lower Hölder exponents on fixed collars gives a common constant for the stated range.

## 4. Constraint vertex and full factorization

The direct one-step coefficient-row estimate includes the physical volume ratio L_step^d and the h/L_step quadratic coefficient, hence is O(h)||w||_infinity with a fixed finite constant. The multilevel identity

    T_w=sum_t Q_(0:t)^* T_(h_t,w_t) Q_(0:t)

and the physical Q/Q* sup contractions give the geometric bound. Fixed final range supplies the weighted sup norm. This is the stronger result independently checked in `flat_full_constraint_current_audit.md` Section 7; it is not inferred from the final-cell Hilbert bound.

The actual weight E_J^T J is bounded and analytic into coarse sup by the previously proved rectangular Schur estimate. Thus the proof controls the actual Theta_J, whose potential arguments have finite range although its coefficient depends nonlocally on J.

The exact full factorization

    G0 Pi* Theta_J Pi A
       =(G0-DZD*) T_(w_J)(A-DLambda A)

then uses only justified pointwise estimates. The order of the factors is preserved; no commutation or unrestricted sup bound for Pi is used. The constrained baseline Gamma estimate in Section 5 is also valid: its fine transpose leg maps weighted bounded forcing to coarse bounded data by the physical-cell Schur estimate, and the output extension has the established pointwise bound.

## 5. Actual inverse, analyticity, and locality

The constant C_* controls K_J=G0 Psi_J as N_w->N_(beta,w), hence also as an N_w endomorphism after the stated fixed convention adjustment. The radius min(epsilon_H,1/(2C_*)) gives a norm-convergent N series. Applying the smoothing estimate only to the outside factor proves convergence into N_beta as claimed. Holomorphy follows from the bounded analytic map J->w_J, linearity of T_w in its coefficient, and the inverse series in these Banach spaces. Nonlinearity of Psi_J is properly retained.

For a forcing supported in cell m, the increasing weight exp(kappa dist(n,m)) gives exponential output decay in N_beta. Its solution is in physical L2 in infinite volume, uniformly with respect to the cell normalization, and it therefore agrees with the separately proved Hilbert inverse on that forcing. Absolute cell-kernel summation extends the identification to arbitrary bounded forcing. At each fixed M the required original products are well-defined; uniformity of the final bounds does not require pointwise bounds on every original factor separately. The same reasoning works with periodic distance on compatible tori.

The coarse inverses have fixed-dimensional cell fibers, so their Hilbert Schur bounds give coarse sup bounds. Composing them with the positive normalized physical Q* and the pointwise current inverse proves the stated extension bounds. No additional derivative of the current appears.

## 6. Source matching and limits

At ell=1, the source N,N_beta norms agree with the pointwise norms in the note up to fixed component/collar conventions. J requires only a sup bound. The result proves the bounded-forcing inverse and the N->N_beta current insertion members, including exponential weights. It correctly does not claim current Laplacian estimates: the source excludes those, and a Laplacian on DZD* would expose an order-zero issue on rough data.

The source's right-divergence members are separate. They need Hölder input and proper physical cutoffs; sharp cell decomposition of those input data would create refinement-dependent Hölder jumps. The note records this explicitly and does not count it as discharged. General nonflat coefficients, retained histories, strict support-dependent walk expansions, and the interacting ultraviolet limit likewise remain outside the proof.

The candidate can be promoted as the stated bounded-forcing pointwise theorem after this independent audit; it should retain the explicit unfinished right-divergence clause.
