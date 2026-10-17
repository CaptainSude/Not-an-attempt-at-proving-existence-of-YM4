# Right-divergence estimates with Holder input

16 October 2026. Proof candidate for the remaining homogeneous flat right-divergence member. It extends the audited bounded-forcing pointwise current theorem. The route separates a global massive lattice Green function from a remainder that already smooths arbitrary bounded data. All cancellation occurs in a translation-invariant full-lattice heat kernel; no Holder field is sharply cut into cells.

## 1. Statement and notation

Let G_0 be the matched homogeneous flat full inverse, and let G_pi^J and G_1^J be the auxiliary and actual full homogeneous flat current inverses on the common small current ball proved in `flat_pointwise_current_research.md`. Retain fine spacing eta=1/M, physical fine measure eta^d, fixed unit coarse cells, and fixed odd L with M=L^j for the full constraint term.

For a fine field lambda and an admissible cell weight varpi satisfying

    varpi(n)/varpi(m)<=exp(kappa dist(n,m)),

define ||lambda||_(gamma,varpi) by the weighted supremum of its pointwise norm and gamma-Holder seminorm on fixed coarse-cell collars. These are complete fields. For 0<=beta<gamma<1 we prove, for a sufficiently small fixed kappa,

    N_(beta,varpi)(G_0 D^* lambda)
                        <=C_(beta,gamma)||lambda||_(gamma,varpi),
    N_(beta,varpi)(G_pi^J D^* lambda)
                        <=C_(beta,gamma)||lambda||_(gamma,varpi),
    N_(beta,varpi)(G_1^J D^* lambda)
                        <=C_(beta,gamma)||lambda||_(gamma,varpi).
                                                            (1.1)

D^* can be any specified physical fine divergence on the forcing tensor, with the fixed finite orientation contractions included. Constants are independent of refinement and compatible volume; the current estimates use the already established common pointwise/Hilbert current radius, possibly decreased by a fixed amount if kappa is decreased. The estimate is for the physical adjoint acting on lambda as a complete field. It is not obtained by estimating ||D^*lambda||_infinity.

Choosing gamma=beta+epsilon, with beta<=beta_0<1 and a fixed positive epsilon such that beta_0+epsilon<1, gives the source-shaped loss. Constants can then be uniform in beta on that interval. The argument makes no claim at gamma=beta. For beta=0 it requires positive input Holder regularity.

The source definitions are explicit: Raw I:13601--13615 describes localized right-divergence members with higher Holder regularity on the input; I:13759--13765 lists them for the auxiliary current inverse and excludes its Laplacian member. The present theorem remains homogeneous flat and does not prove general-background or retained-history variants.

## 2. Isolate the translation-invariant singular part

Let

    G_m=(L+1)^(-1)I,      L=D^*D,
    R_m=G_0-G_m.                                        (2.1)

The massive inverse is an auxiliary comparison operator, not a change in the source definition. Its Fourier alias diagonal is (P_r+1)^(-1) in each vector component. Shrink the already common complex chart if necessary so that P_0+1 stays uniformly away from zero. On the real chart P_0>=0, so bounded holomorphic derivatives give a refinement-independent shrinking. The high denominators have the same property by their existing gap.

The high diagonal of R_m is

    P_r^(-1)-(P_r+1)^(-1)
       =integral_0^infinity (1-exp(-t))exp(-tP_r)dt,
                           r!=0.                       (2.2)

The rest consists of exactly the finite-rank terms already estimated for G_0, together with the bounded central subtraction -(P_0+1)^(-1)Pi_0. Thus we can prove the stronger remainder estimate

    N_(beta,varpi)(R_m D^* f)
                            <=C_beta||f||_(infinity,varpi),
                            0<=beta<1,                 (2.3)

with arbitrary bounded fine f and exponentially local pointwise cell blocks.

For the high diagonal, put one difference on the input, and at most one output difference with a beta-Holder increment. The small-time kernel norm has the factor

    (1-exp(-t)) t^(-(2+beta)/2)<=t^(-beta/2),
                           0<t<=1,

which is integrable. The lower output members are easier. Large times use the uniform high gap. The higher heat derivative bounds used for the Holder interpolation follow by semigroup convolution exactly as in the pointwise-current scalar proof.

For finite-rank terms, the right difference multiplies the input rows by one fine multiplier u_s. For the high row omega_s/P_s this gives O(|omega_s|/(1+|s|)); for the beta row the existing estimate becomes O(|a_s|/(1+|s|)^2+|omega_s|/(1+|s|)). Both have uniformly bounded alias l2 norm. Central rows are bounded. Output C^(1,beta) vectors are unchanged and satisfy the audited absolute alias sums for beta<1. Input physical-cell L2 is bounded by input l-infinity without a dimension factor.

All terms are uniformly holomorphic in the corresponding pointwise operator norms. The full reconstructed remainder is periodic even though its separated high and central pieces need not be. The same gluing and contour shift therefore prove exponentially local cell blocks for R_m D^*, and their weighted row sums give (2.3). Exact finite periodic sampling gives the same result on compatible tori. Hard cell support of f is harmless in this remainder estimate because f requires no Holder norm and D^* has already been put on the operator kernel.

## 3. Uniform heat-kernel moments, including sub-mesh times

Write p_t^eta(v) for the full-lattice probability heat kernel of L, where v is a fine displacement in eta Z^d. The kernel is the product of nearest-neighbor random-walk probabilities at clock time t/eta^2. For any specified composition of k differences and any fixed small kappa, we need

    sum_v exp(kappa|v|_1)|v|_1^gamma
                  |D_eta^k p_t^eta(v)|
          <=C t^((gamma-k)/2),
                 0<t<=1,      k=2,3,      0<gamma<1.     (3.1)

The probability-kernel convention is used; converting to densities against physical volume cancels the volume factors in this operator row sum.

For t>=eta^2, use the weighted variation estimate from the pointwise inverse proof with exponential scale delta=kappa+t^(-1/2). In lattice units its parameter is eta delta<=kappa+1. The constants in that elementary estimate are uniform on this fixed interval. Its exponent is bounded by C delta^2 t, which is bounded for eta^2<=t<=1. Splitting the heat semigroup into k equal-time factors gives

    sum_v exp(delta|v|_1)|D_eta^k p_t^eta(v)|
                                            <=C_k t^(-k/2).

Since |v|^gamma<=C_gamma t^(gamma/2)exp(|v|/sqrt(t)), this proves (3.1) in the stated range.

For 0<t<eta^2, expand the k-th fine difference into its fixed finite list of shifts:

    D_eta^k p_t^eta(v)
       =eta^(-k) sum_j c_j p_t^eta(v+eta a_j),
          |a_j|_1<=k,      sum_j|c_j|<=C_k.

The dimensionless walk has time t/eta^2<1. Its exponential moments and every fixed positive moment are uniformly bounded at that time, including the bounded lattice exponential parameter kappa eta. Consequently

    sum_v exp(kappa|v|_1)|v|^gamma
                          |D_eta^k p_t^eta(v)|
                                     <=C eta^(gamma-k).

Because k>gamma and t<eta^2, eta^(gamma-k)<=t^((gamma-k)/2). This proves (3.1) also at the sub-mesh times where a continuum heat estimate cannot simply be assumed.

For t>=1, use any fixed small delta_1>0 and absorb |v|^gamma into exp(delta_1|v|). The same weighted variation/convolution estimates give a bound C exp(c(kappa+delta_1)^2t) for the required moments (with harmless fixed factors). Choose kappa,delta_1 so small that this is at most C exp(t/2). The massive factor exp(-t) then leaves an integrable tail. The same reasoning gives the needed zeroth/first-difference weighted bounds without a gamma moment.

## 4. Cancellation on the complete lattice

For every nonzero difference order k,

    sum_v D_eta^k p_t^eta(v)=0.                       (4.1)

This is exact translation-invariant cancellation. It holds on the full lattice and for the periodized finite-torus heat kernel. No cell boundary is introduced.

The weighted local Holder norm implies the global increment inequality

    varpi(cell x)|lambda(y)-lambda(x)|
       <=C||lambda||_(gamma,varpi)
              exp(kappa|x-y|_1)|x-y|_1^gamma.         (4.2)

For distance at most a fixed cell diameter, use the Holder seminorm on a common fixed collar and bounded neighboring weight ratios. For larger distances use the two supremum bounds; |x-y|^gamma is then bounded below and the cell-weight ratio is controlled by the physical distance up to a fixed offset. Thus (4.2) does not differentiate the weight and does not presume a globally bounded unweighted Holder seminorm.

Subtract lambda(x) using (4.1). Equations (3.1)--(4.2) prove, for 0<t<=1,

    ||D_eta^2 exp(-tL)lambda||_(infinity,varpi)
                     <=C t^(-1+gamma/2)||lambda||_(gamma,varpi),
    ||D_eta^3 exp(-tL)lambda||_(infinity,varpi)
                     <=C t^(-3/2+gamma/2)||lambda||_(gamma,varpi).
                                                            (4.3)

For x,y in a fixed output collar, the difference of the second-derivative output is bounded both by twice the first line and by |x-y| times the second line, by telescoping. Neighboring weight ratios change only constants. Interpolating these two bounds yields

    [D_eta^2 exp(-tL)lambda]_(beta,varpi)
       <=C t^(-1+(gamma-beta)/2)||lambda||_(gamma,varpi).
                                                            (4.4)

The expression on the left denotes the local beta-Holder seminorm of the indicated derivative, not a new derivative of lambda. Formula (4.4) remains valid for beta=0 with the usual supremum interpretation or a fixed equivalent zero-Holder convention.

Because gamma>beta, its small-time integral is finite:

    integral_0^1 t^(-1+(gamma-beta)/2)dt
                                      =2/(gamma-beta). (4.5)

The field supremum in G_mD^*lambda needs only the first heat derivative and bounded input, whose t^(-1/2) bound is integrable. The first-gradient and its beta-Holder member use (4.3)--(4.5). The large-time estimates of Section 3, multiplied by exp(-t), are integrable. Therefore

    N_(beta,varpi)(G_m D^*lambda)
                            <=C_(beta,gamma)||lambda||_(gamma,varpi).
                                                            (4.6)

This is the only singular-integral cancellation needed in the proof. It is a global translation-invariant calculation, so no compatibility issue for arbitrary cellwise Holder data or complex Bloch twists is hidden in it.

On finite tori one can either periodize the heat kernel and use (4.1) directly, or extend lambda and the weight periodically to the cover. Their periodic physical distance is no greater than the cover distance, so (4.2) and the moment estimates remain valid. All periodization multiplicities are retained, with the same constants.

## 5. Baseline and current right-divergence estimates

Combine G_0D^*=G_mD^*+R_mD^*, (2.3), and (4.6). This proves the first estimate in (1.1). The constant contains an explicit possible loss proportional to 1/(gamma-beta); no bound uniform as gamma decreases to beta is asserted.

For either current family, let K_J be its already proved weak-space perturbation: G_0Theta'_J for the auxiliary inverse, and G_0(Theta'_J+Pi^*Theta_JPi) for the full inverse. On the common pointwise/Hilbert current ball,

    N_(beta,varpi)(K_JA)<=C_*||J||_infinity N_varpi(A),
    C_*||J||_infinity<1/2.

Apply the identical convergent series to the baseline right-divergence datum:

    G^J D^*lambda=(I-K_J)^(-1)G_0D^*lambda.

The baseline N estimate uses positive input Holder regularity, and the stronger baseline N_beta estimate uses gamma>beta. All later terms are controlled by the N-to-N_beta perturbation bound, exactly as for bounded forcing. This proves the remaining estimates in (1.1). Analyticity in the complex bounded-current ball follows from the same operator-valued Neumann argument. No new current regularity is needed, and the original current radius can be retained after fixing a common smaller spatial exponent.

## 6. Legitimate localization and source status

The natural statement is the direct weighted global Holder estimate (1.1). To obtain localized versions, multiply lambda by a smooth physical cutoff phi supported in a fixed cell collar, with uniformly bounded supremum and first physical derivative. Its sampled fine values obey

    ||phi lambda||_(gamma,varpi)
       <=C_phi||lambda||_(gamma,varpi;support collar),

by the product difference identity. The cutoff has a fixed physical scale, so no inverse power of eta appears. Choosing the source-centered weight exp(kappa dist(n,m)) then gives exponential decay away from that collar. A smooth fixed-scale partition of unity with bounded overlap can be used if an explicit decomposition is wanted, but is not needed for the global proof.

Replacing phi by a sharp cell indicator would generally introduce eta^(-gamma) Holder jumps and is not legitimate. Likewise the theorem is not a fine-point kernel bound on arbitrary Holder data with discontinuous zero extension.

For source input exponent gamma=beta+epsilon<1, (1.1) supplies the homogeneous flat right-divergence weak members omitted from the bounded-forcing current note. It includes arbitrary bounded currents in the previously proved ball and the actual full corrected flat constraint term. It does not add a current Laplacian member, assert the gamma=beta endpoint, or prove nonflat, retained-history, or interacting continuum results. Exact source-coordinate identifications remain those audited in the earlier flat notes and are based on the deposited transcriptions.
