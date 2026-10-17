# Independent audit of nonlinear gauge-slice coverage

Audited root's `nonlinear_gauge_slice_research.tex` completely. Verdict: passes; no substantive correction found. The argument proves uniform local coverage for the homogeneous globally defined small-field class on finite compatible periodic regulators. It does not presume that strict minimality on the fixed slice alone implies unrestricted minimality.

## 1. Induced gauge and physical units

Direct substitution in C(U)=a_-(U)^(-1)M(U)a_+(U) gives k_y=a_y(U^g)^(-1)g(y)a_y(U), with exactly the stated endpoint order. At g=1 its derivative is Ad(a_y^(-1))[lambda(y)-eta_a], where eta_a is the left derivative of a(U^g). The contour left derivative is lambda(y)-Ad(P_x)lambda(x). Applying the logarithm inverse Jacobian J_(Y_x)^(-1), averaging, then applying the exponential Jacobian J_(Ybar) gives the displayed T_U. At U=1 this is the scalar block average, not the value at the block center.

The gauge parameter is an angle. Fine gauge velocity is -D_U lambda in left physical coordinates and -J_(eta A)^(-1)D_U lambda in ordinary potential coordinates. At final spacing one the coarse physical velocity is -J_B^(-1)D_V G_A lambda. Differentiating the exact multilevel law therefore gives the displayed Q_A X_A intertwining, without a missing eta or L. The composite induced-gauge coefficients are evaluated at corrected iterates C_t; these are correctly distinguished from the ordinary references used by source Q(U).

Each one-step perturbation has coefficient size O(h||A||), finite row incidence and physical transpose factor L^d. Products have flat scalar factors of norm one, and the geometric sum of h_t yields uniform O(||A||) perturbation. This applies to bounded fields and physical adjoints; physical-cell weighted norms follow from finite final reading radius. The operator-valued holomorphy and smaller-ball Cauchy estimates follow from these uniform bounds.

## 2. Scalar smoothing and the biharmonic lift

Multiplying the previously audited Z alias matrix on the right by L gives every displayed T=ZL entry, including mixed central/high factors P_0 and P_s. After subtracting the massive inverse, the high diagonal has heat factor 1-exp(-t). Its two-output-difference Hölder norm is integrable at small time. All noncentral rank output vectors are a_r^-/P_r^2, hence absolutely summable with 2+alpha physical differences, while the input rank rows are uniformly in alias L2. The massive C^alpha->C^(2,alpha) estimate is the independently proved equal-exponent split at squared output separation; no older positive-loss result is used in its place.

The projection I-R_0 has vector chi_0=a_0^- and chi_r=P_0 a_r^-/P_r. Its output alias sums allow 1+beta differences for beta<1, so it sends bounded forcing to C^(1,beta). This supplies R_0:C^alpha->C^alpha. Complete-operator periodic reconstruction and contour shifts give the weighted locality estimates. No differentiated sharp cell cutoff is used.

The smooth lift H_b is exactly the canceled version, on nonzero real fibers, of

    L^(-2)Q_0^T [Q_0 L^(-2)Q_0^T]^(-1).

Since the scalar denominator is W_2=D_s,2/P_0^2, its central and high entries are precisely those in the note. Multiplication by the Q_0 row gives one. At zero momentum the continuation sends the constant coarse mode to the constant fine mode; at M=1 it is the identity. Its high outputs a_r/P_r^2 allow 3+beta differences for beta<1, and in particular all of Z_alpha. The abstract nonzero-fiber formula, with the canceled continuation, also makes full-symbol periodic gluing explicit. This lift is indeed different from G'^2Q_0^T(Q_0G'^2Q_0^T)^(-1) when a'>0; one must not transfer their regularity by name alone.

## 3. Gauge-fixing inverse

F_A=G_A-Q_0 maps Z_alpha to coarse bounded fields with norm O(||A||_infinity). Thus I+H_bF_A is invertible on Z_alpha and its inverse differs from the identity by the same order. Applying Q_0 to its defining equation shows exactly that T_A^s maps ker Q_0 into ker G_A.

The coefficient eta^(-1)(Ad(exp(i eta A))-I) is jointly removable at eta=0 and has C^(1,alpha) size O(||A||_X). The exponential inverse Jacobian differs from identity by a coefficient of C^(1,alpha) size O(eta||A||_X). To justify the discrete chain estimate explicitly, write a first difference of any smooth coefficient function f(A) as the integral of Df along the segment between adjacent A-values, multiplied by nabla A. Its Hölder difference is then bounded by Df times the Hölder difference of nabla A plus D^2f times A's Hölder difference and the bounded gradient. These are all controlled by X_alpha, with no inverse eta. Multiplying such coefficients by Dlambda or shifted lambda proves X_A-D:Z_alpha->X_alpha of size O(||A||_X).

Consequently M_A-I on range R_0 splits into the terms containing X_A-D and T_A^s-I. The exterior R_0D^T is bounded X_alpha->Y_alpha, T maps Y_alpha->Z_alpha, and D maps Z_alpha->X_alpha. Both perturbations are small, while M_0=R_0LT=I on range R_0. The Neumann inverse and all exact identities for L_A therefore follow. No bare fine derivative has been treated as a bounded map on an insufficient space.

For a fixed-gauge constrained tangent v, the chart tangent identification is also exact: z=(I+H DR(A))v satisfies Qz=(Q+DR(A))v=0 and R_0D^Tz=0, so z belongs to X and v=T_Az. Hence the tangent decomposition in the note really reduces full constrained stationarity to stationarity in the previously constructed slice chart.

## 4. Flow and local minimum modulo gauge

The vector field -X_A L_A A is locally Lipschitz in X_alpha on a fixed ball because all its factor maps are bounded and holomorphic in the indicated spaces. The identity R_0D^TX_A L_A A=R_0D^TA gives exact exponential decay of the gauge defect. The intertwining identity and G_A L_A=0 give constancy of the nonlinear corrected constraint. The velocity is an actual gauge velocity in the ordinary logarithm chart, so exact Wilson gauge invariance gives constancy of the action.

For real fields lambda(t)=L_(A(t))A(t) is Hermitian traceless. The ODE g'=i lambda g, g(0)=1, integrates the link equation and keeps g unitary. The stronger correction bound gives an integrable Z_alpha norm for lambda(t); thus g(t) converges uniformly, and the limiting field is in the original gauge orbit. It is not merely a field with the same action value.

The speed bound Ce^(-t)||R_0D^TA_in|| and boundedness of R_0D^T give a uniform small initial ball whose full displacement stays inside the operator domain. Standard continuation then applies for all t. Completeness gives a limit in X_alpha, with zero fixed-gauge defect and unchanged constraint. All limiting identities are continuous in the stated norms at fixed regulator.

Near a fixed slice field A_*, the initial defect is bounded by C||A_in-A_*||, and the total displacement has the same bound. Therefore a sufficiently small neighborhood flows into the strict slice-minimality neighborhood. Strict slice minimality gives the unrestricted local inequality on the same nonlinear constraint. Equality forces the slice limit to be A_*, and convergence of the gauges proves gauge equivalence to A_*. The constructed gauge path preserves the constraint at every time. The conclusion is local minimality modulo this gauge orbit, not global uniqueness or coverage of arbitrary plaquette-small/topologically nontrivial configurations.

The finite-regulator action statement and the exclusion of arbitrary bounded infinite-field total actions are appropriate. Constants are uniform in compatible volume and refinement throughout the supplied estimates.
