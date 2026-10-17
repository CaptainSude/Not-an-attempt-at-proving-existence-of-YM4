# Pointwise current neighborhoods in the homogeneous flat weak norms

16 October 2026. Proof candidate. This note combines the proved pointwise flat inverse with scalar source-gauge smoothing and the fixed-step quadratic constraint-current estimate. It proves the source-shaped maps N to N_beta for both current perturbations, and a uniform pointwise inverse neighborhood for arbitrary bounded fine currents. It does not differentiate the current or assume that the source projection Pi is bounded on arbitrary bounded fine fields. The precise right-divergence/Hölder-data estimates remain a separate extension.

## 1. Setting, weak norms, and weighted formulation

Retain the homogeneous flat operators Q=Q_M^st, scalar Q_0, scalar gradient D, componentwise positive Laplacian L=D^*D, source projection R, G'=(L+Q_0^*a'Q_0)^(-1), and

    Z=G'RG',        Lambda=Z L D^*=G'R D^*,
    Pi=I-D Lambda,
    A_0=d^*d+D R D^*+Q^*aQ,       G_0=A_0^(-1).

The scalar and one-form penalties are distinct. The matched normalized one-form penalty is a=1; a fixed positive interval is harmless. For the actual corrected nonlinear-constraint term assume M=L_step^j with fixed odd L_step, exactly as in `flat_full_constraint_current_research.md`.

At homogeneous ell=1 and U=1 the deposited definitions Raw I:12740--12752 become, up to fixed equivalent norm conventions,

    N(A)=max(||A||_infinity, ||D A||_infinity),
    N_beta(A)=max(N(A), [D A]_beta),
                  0<=beta<=beta_0<1.                 (1.1)

D A denotes all specified first fine differences of the vector field. The Holder member is localized as in the source; the estimates below give it on every fixed coarse-cell collar, and also imply the global discrete version. No Laplacian is part of N_beta. This was checked directly in the deposited lines above. Raw I:13759--13765 explicitly excludes a Laplacian assertion for the auxiliary current inverse.

For locality, let w(n)>0 be any coarse-cell weight with

    w(n)/w(m)<=exp(kappa dist(n,m)),                  (1.2)

where dist is ordinary or periodic cell distance. Define ||f||_(infinity,w)=sup_n w(n)||f||_(infinity,cell n), and N_w,N_(beta,w) by the corresponding weighted supremum of the field, its first differences, and local Holder seminorms on fixed cell collars. Enlarged collars only change constants because neighboring weights have bounded ratios. In particular w(n)=exp(kappa dist(n,m_0)) is admissible.

We work with complete global fields in these norms. We do not cut a differentiable field sharply into cells before applying D: such a cut would introduce a false eta^(-1) boundary derivative. Every bound involving D^*A uses the actual derivative of the complete field and fixed output collars.

## 2. Scalar pointwise smoothing supplied by Z

The following four estimates are sufficient. For a common sufficiently small kappa>0, uniformly in refinement and compatible volume,

    ||Z L f||_(infinity,w) <=c_0 ||f||_(infinity,w),
    ||D Z L f||_(infinity,w) <=c_1 ||f||_(infinity,w),
    N_(beta,w)(D Z f) <=z_1 ||f||_(infinity,w),
    N_(beta,w)(D Z D^* f) <=z_2 ||f||_(infinity,w),
                      0<=beta<=beta_0<1.             (2.1)

The stars are the physical adjoints on real fields and their fixed analytic bilinear continuations. These are actual maps on bounded data, including the right derivative in DZD^*: its kernel is differentiated before acting on f.

Here is a proof, reducing them to the already proved heat estimates. The canceled alias matrix for Z is a scalar high diagonal P_r^(-2), plus a fixed number of rank terms with high vectors a_r^-/P_r^2 and their transpose partners; its central entries have no massless denominator. The high diagonal is

    integral_0^infinity t
       [H_z(t)-exp(-tP_0)Pi_0(z)]dt.                 (2.2)

The weighted derivative estimates for the scalar heat kernel extend to every fixed integer order k by semigroup convolution: split p_t into k equal-time factors, put one fine difference on each factor, and use the weighted L1 convolution inequality. Thus for 0<t<=1,

    ||D_eta^k H_z(t)||_(infinity->infinity)
                                      <=C_k t^(-k/2).

A Holder difference of order beta costs at most another t^(-beta/2), by the same interpolation of the k and k+1 derivative bounds used in the pointwise G_0 proof. Fine input differences are handled by the same kernel differences or discrete summation by parts, not by estimating derivatives of the input. Hence the small-time integral for total fine derivative order m and an additional beta-Holder output difference is bounded by

    C integral_0^1 t^(1-(m+beta)/2)dt,

which converges whenever m+beta<4. Large times use the high-alias gap. In (2.1), ZL has m=2, DZL has m=3, DZ with a first derivative and beta-Holder member has m=2+beta<4, and DZD^* with that member has m=3+beta<4.

For the finite-rank terms, the input rank rows with up to three prescribed differences have uniformly bounded alias l2 norm. On the output side use

    |a_r|<=C product_nu(1+|r_nu|)^(-1)=C w_alias(r),
    |P_r|>=c(1+|r|)^2,
    sum_(dyadic shell j) w_alias(r)<=C(j+1)^(d-1).

Any output derivative/Holder order strictly below four is absolutely summable for the high vector a_r/P_r^2. Central factors are bounded. Physical-cell L2 input rows act on bounded fine data with no dimension factor. This proves common-chart pointwise bounds; full-symbol periodic gluing and contour shifting give exponential cell kernels. Their weighted row sums prove (2.1). The same argument applies to finite periodic sampling and its exact periodizations.

In particular, for an arbitrary field with N_w(A)<infinity,

    ||Lambda A||_(infinity,w)
        =||Z L D^* A||_(infinity,w)<=l_0 N_w(A),
    ||D Lambda A||_(infinity,w)
        =||D Z L D^* A||_(infinity,w)<=l_1 N_w(A).
                                                            (2.3)

The finite number of components in D^* is absorbed into l_0,l_1. It follows that

    ||Pi A||_(infinity,w)<=(1+l_1)N_w(A).             (2.4)

No l-infinity-to-l-infinity claim is made for D Lambda or Pi on unrestricted bounded input. Their use in (2.3)--(2.4) has exactly one bounded derivative available on A.

## 3. Auxiliary perturbation: a direct N to N_beta estimate

Use the already source-matched local factorization

    Theta'_J=j_J^* Lambda+Lambda^* j_J
              +Lambda^* V_J D Lambda
              +(D Lambda)^* V_J^* Lambda.            (3.1)

The coefficient maps j_J,V_J and their analytic transposes have fixed fine incidence, and their pointwise weighted norms are at most c_j||J||_infinity and c_v||J||_infinity. They contain no derivative of J. The scalar identities give exactly

    G_0 Lambda^*=D Z,
    G_0(D Lambda)^*=D Z D^*.

Consequently

    G_0 Theta'_J
       =G_0 j_J^* Lambda +D Z j_J
          +D Z V_J D Lambda +D Z D^* V_J^* Lambda.
                                                            (3.2)

Let g_beta bound G_0 from weighted bounded forcing to N_(beta,w), as proved in the pointwise inverse theorem. Combining that bound, (2.1), and (2.3) proves

    N_(beta,w)(G_0 Theta'_J A)
                <=C_aux ||J||_infinity N_w(A),       (3.3)

where, for example,

    C_aux=g_beta c_j l_0+z_1 c_j
                            +z_1 c_v l_1+z_2 c_v l_0.

Choose constants at the fixed ceiling beta_0. Smaller Holder exponents follow on bounded collars with fixed factors, so a common constant works for every 0<=beta<=beta_0. This is the homogeneous normalized form of source (J1), including a weighted version. The input needs N only; no Holder regularity of A or J is assumed.

## 4. Pointwise bound for the actual constraint-current operator

We also need the finite-range operator T_w defined by the exact corrected quadratic composition:

    <A,T_w B>_eta=2<C_j^(2)(A,B),w>_1.

Its uniform pointwise bound follows from the same fixed-step proof as its audited Hilbert estimate. At one step of physical fine spacing h,

    B_h(A,B)=(h/L_step)C_(L_step)(A,B).

This is a fixed finite bilinear tensor per output bond. In its physical adjoint pairing, the coarse/fine measure ratio is L_step^d. Summing its finitely many coefficients in any fine output row therefore gives

    ||T_(h,w)||_(infinity->infinity)
                                 <=c_step h||w||_infinity.

The row coefficient sum includes all fixed geometry and color constants; it is finite because L_step is fixed. This is a direct coefficient-row estimate, not a conversion from a growing-dimensional final-cell Hilbert norm.

The exact quadratic chain rule gives

    T_w=sum_(t=0)^(j-1)
       Q_(0:t)^* T_(h_t,w_t) Q_(0:t),
    h_t=L_step^(t-j),
    w_t=Q_(t+1:j)^*w.

Both flat Q and its physical adjoint Q^* are l-infinity contractions: their nonnegative row coefficients sum to one, with covering-space multiplicities on short tori. Thus

    ||T_w||_(infinity->infinity)
       <=c_step ||w||_infinity sum_t h_t
       <=c_step/(L_step-1)||w||_infinity.             (4.1)

Its unit-cell range is bounded by a fixed R_*; the physical reading radii are summed over the same geometric series. Therefore a weighted version follows:

    ||T_w f||_(infinity,wgt)
       <=tau_infinity ||w||_infinity
                              ||f||_(infinity,wgt),  (4.2)

for any weight wgt obeying (1.2). The fixed factor exp(kappa R_*) is included in tau_infinity. The notation wgt distinguishes a spatial weight from the coarse current weight w.

For the actual source term, w=w_J=E_J^T J, with E_J the auxiliary extension. Its proved physical-cell Schur bound gives

    ||w_J||_infinity<=C_w||J||_infinity

throughout the auxiliary current ball, analytically in J. No global fine L2 assumption is used. Hence the actual Theta_J=T_(w_J) satisfies (4.2) with tau_infinity C_w||J||_infinity.

## 5. Full constraint perturbation and the constrained baseline

The exact algebra gives

    G_0 Pi^*=G_0-D Z D^*.

Apply this identity only after the coefficient operator:

    G_0 Pi^*Theta_J Pi A
        =(G_0-D Z D^*)T_(w_J)(A-D Lambda A).

The outside factor maps bounded data to N_beta; the inside field is bounded by (2.4). Therefore

    N_(beta,wgt)(G_0 Pi^*Theta_J Pi A)
           <=C_con ||J||_infinity N_wgt(A),          (5.1)
    C_con=(g_beta+z_2)tau_infinity C_w(1+l_1).

This is the source-shaped full constraint-current estimate. It avoids both an unjustified pointwise bound for Pi on arbitrary bounded input and any derivative of J.

For completeness the constrained baseline

    Gamma=G_0-H_src q_aux^(-1)H_src^*,
    q_aux=q_Maxwell+aI,

also maps weighted bounded fine forcing to N_beta uniformly. The H_src output has the proved pointwise bound; its transpose takes bounded fine input to bounded coarse output by the physical-cell Schur estimate, and q_aux^(-1)=QG_0Q^* is local and bounded on coarse fields. Thus

    N_(beta,wgt)(Gamma Theta_J A)
                  <=C ||J||_infinity ||A||_(infinity,wgt).
                                                            (5.2)

This last bound is a separate useful source-shaped constrained-covariance member. It does not require Pi or a derivative of A.

## 6. A uniform actual pointwise current neighborhood

Define the analytic perturbation

    Psi_J=Theta'_J+Pi^*Theta_J Pi,
    K_J=G_0 Psi_J.

On the already established auxiliary current ball,

    N_(beta,w)(K_J A)
          <=C_* ||J||_infinity N_w(A),
    C_*=C_aux+C_con.                                 (6.1)

The norm N_(beta,w) dominates N_w up to a fixed convention factor; include it in C_*. Let epsilon_H be the independently proved full-current Hilbert/Schur radius. Choose

    epsilon_pt=min(epsilon_H, 1/(2C_*)).              (6.2)

For ||J||_infinity<epsilon_pt, the series

    G_1^J f=(I-K_J)^(-1)G_0 f
              =sum_(n>=0) K_J^n G_0 f               (6.3)

converges in the weighted N space. It also converges as a map from bounded forcing to weighted N_beta: for n>=1, apply the N-to-N_beta estimate to the last outside K_J and the contracting N bound to the remaining factors. For example, if g_N is the baseline bounded-forcing-to-N norm,

    N_w(G_1^Jf)<=2g_N||f||_(infinity,w),
    N_(beta,w)(G_1^Jf)
       <=[g_beta+2C_*epsilon_pt g_N]
                                  ||f||_(infinity,w). (6.4)

The operator-valued series is holomorphic in the complex l-infinity current ball. The perturbation Theta_J is nonlinear in J, through E_J^T J, but analytic with the uniform bound already proved; no linear-current derivative formula is presumed for the full family.

For forcing supported in one cell m, use w(n)=exp(kappa dist(n,m)). Equations (6.3)--(6.4) give exponential coarse-cell locality of the full current inverse in the pointwise N_beta norm, even though a general current is not translation invariant. On the infinite lattice this weighted solution lies in physical L2, and hence agrees with the independently constructed Hilbert inverse. For arbitrary bounded forcing the equality extends by the absolutely summable cell blocks; at each fixed M the original operator products are also absolutely summable. Finite tori use exactly the same estimates in periodic distance. No volume-dependent bound enters.

The auxiliary inverse is the special case retaining Theta'_J only, with the same proof and the smaller constant C_aux. The normalized extensions are also pointwise bounded: E_1^J=G_1^J Q^*q_1^J and E_J=G_pi^J Q^*q_J, while Q^* maps bounded coarse fields to bounded fine fields and the already proved coarse Schur bounds make q_1^J,q_J bounded on coarse l-infinity. This gives their uniform N_beta bounds on a possibly smaller common current ball.

## 7. Exact scope and unfinished source members

Within the deposited homogeneous flat coordinate identification, (3.3) and (5.1) prove the N-to-N_beta current estimates with bounded arbitrary complex currents. Equation (6.4) proves the corresponding actual pointwise inverse neighborhood for bounded fine forcing. The normalized norms agree with the explicit N,N_beta definition at ell=1 and U=1, subject to the fixed equivalent convention for the source's localized Holder seminorm. The output exponent can be any beta<=beta_0<1.

No pointwise Laplacian estimate is claimed for the current inverses. The source expressly does not require that member here. Indeed the potentially rough term DZD^* times bounded current coefficients has an order-zero Laplacian; treating it as bounded on arbitrary l-infinity data would be unjustified.

The right-divergence members with Holder input, mentioned in source (J2), have not been proved by this note. Such data cannot be sharply cut into cells before taking its Holder norm. A later argument must use a smooth physical partition with controlled collars or work directly in weighted global Holder spaces. A bound with output Holder exponent beta naturally requires an input exponent strictly above beta in the heat-integral argument.

General nonflat backgrounds, mixed retained histories, varying constraints beyond their exact flat quadratic coefficient, and the interacting ultraviolet construction remain outside the result. The corrected nonlinear one-step source coordinate and fixed-step composition are exactly those audited in the separate full constraint-current note, not a replacement average of ratio M.
