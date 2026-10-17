# Independent audit of the fixed-threshold coupling parity

17 October 2026. Auditor: rotation_audit. This audits Section5 of quantum_zero_input_force_research.md against the actual centered chart/base-factor structure and the fixed-window Gaussian construction. No outputs edited or compilation performed.

Result: pass with the stated fixed-threshold, fixed-classical-system and separate-vacuum conventions. The conclusion is an evenness and small-coupling estimate for the centered fluctuation logarithm, not an O(g²) bound for the full zero-input correction.

## 1. Exact parity of the actual factors

At fixed background w, the stationary field, retained linear coordinate map, chart and Gaussian precision are independent of g. Every unwindowed nonlinear factor is evaluated at the same product g xi. For a centered scalar action or gauge function F, the combination is

    -g^(-2)[F(g xi)-F(0)-g DF(0)xi
                         -(g²/2)D²F(0)[xi,xi]].

Its singularity at g=0 is removable because the numerator starts at degree three. Replacing g by -g is exactly the same as replacing xi by -xi: the denominator g² is unchanged, and the numerator consists of F at that product and the corresponding constant, linear and quadratic subtractions. The identity also holds on the independently centered background extension; it does not require dropping a linear term only on the stationary submanifold.

The straightening determinant and Haar factors are analytic functions of g xi with their chosen near-origin logarithms. They have the same parity relation. They need not be even in xi individually. The background pivot normalization and Gaussian determinant are independent of g.

Field-independent powers of g and the compact gauge-insertion normalization are outside this centered fluctuation factor. In particular no holomorphy of the exact compact factor c(g) at zero is being inferred or needed.

Thus the exact total base exponent obeys

    V_base(-g,xi;w)=V_base(g,-xi;w).

The actual retained window is a product of centered link/color balls and is invariant under xi -> -xi. The centered Gaussian density is an even function of xi also for complex background covariance. A real change of integration variable therefore gives

    Z(-g,T;w)=Z(g,T;w).

No background-dependent change of the window and no contour deformation is involved.

## 2. A uniform complex-g disk at fixed T

Keep T fixed during this analytic argument. The exact local chart has a common complex neighborhood in the variable g xi. On the retained window its maximum is controlled by C |g|T. The established analytic base estimates give

    v(g,T)<=C(|g|T³+|g|T+|g|²T²).

For every T>=T_0>=1, choose c>0 fixed small enough that |g|<=cT^(-3) implies all the required chart and strict base budgets. Indeed |g|T<=cT^(-2)<=c and v<=C(2c+c²). The cutoff tail requirement is met by T_0 and does not change when g is complexified.

The covariance and precision support budgets do not move with g. The same strict Gaussian theorem therefore gives nonvanishing and a normally convergent connected logarithm throughout this disk, with a uniform anchored outer-rho bound H_L*. Analyticity in g follows from the removable action/gauge remainders, analytic local measure factors and uniformly normally convergent Gaussian support/cluster sums. The sharp indicator is fixed and never differentiated.

Since the disk is connected and includes g=0, the equality of Z at g and -g gives equality of the logarithms on the branch fixed at zero. There is no possible nonzero 2pi i constant on this connected branch.

## 3. Coefficient representatives and the Cauchy estimate

Total evenness does not by itself imply that the original localized coefficients are even. Replacing a coefficient family L_H(g) by

    L_H^even(g)=[L_H(g)+L_H(-g)]/2

retains its support and does not increase its uniform anchored norm. Its total is the same even logarithm. This step is legitimate before taking an infinite local limit and on the fixed limiting system.

Subtract the g=0 coefficient family. It represents L_(g,T)-L_(0,T); the subtraction is not an assertion that the generally background-dependent cutoff logarithm is a vacuum constant. On the disk of radius r_T=cT^(-3), Banach-valued Cauchy for the even family gives

    ||[L_(g,T)-L_(0,T)]||_(Q,a,rho)
      <=H_L* sum_(n>=1)(|g|/r_T)^(2n)
      <=2H_L* (|g|T³/c)²,   |g|T³<=c/2.

One may obtain the same estimate by integrating first in g and then taking the positive anchored sums. This avoids an unjustified sum-of-root-suprema exchange. No field-coordinate dimension factor occurs.

At g=0 the centered action and gauge remainders and all g xi measure remainders vanish. Thus L_(0,T) is precisely the Gaussian cutoff logarithm. Its strictly local anchored norm is bounded by C tau(T). Consequently

    ||[G_(g,T)(0)-Delta-Qdet]||_(Q,a,rho)
                         <=C[tau(T)+g²T^6].

The bound is uniform in homogeneous depth M and volume under the established common-domain constants.

## 4. The physical diagonal and the Maxwell coefficient

After proving the fixed-T two-parameter estimate, evaluate it at the prescribed physical threshold T=T(g). This is evaluation of an inequality, not a claim that the function g -> T(g) or its sharp indicator is holomorphic. For T(g) of fixed multiple sqrt(log(1/g)) size, g²T(g)^6 tends to zero and the Gaussian tail also tends to zero.

The Maxwell functional can be applied on the same fixed outer field radius:

    |beta(G_(M,g,T(g))(0))
       -beta(Delta_M+Qdet_M)|
      <=C_beta rho^(-2) C[tau(T(g))+g²T(g)^6].

This convergence is uniform in M under the common bounds; it does not assert that beta(Delta_M+Qdet_M) itself has a limit as M grows. It also does not prove its sign or compute its value.

The determinant and pivot terms remain at order g^0. Therefore the full force is not proved O(g²), and this result supplies no asymptotic-freedom statement or infinite running-coupling trajectory.
