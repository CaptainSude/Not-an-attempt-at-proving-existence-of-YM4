# Independent audit: flat Maxwell locality and constrained covariance decay

16 October 2026. Independent derivation and complete audit of `flat_covariance_decay_research.md`, Sections 1--9. The algebraic pole cancellation, scale-uniform analytic strip, periodic gluing and reduced covariance inversion are valid. No substantive mathematical correction was found. An explicit square-integrable minimizing lift, recorded below, strengthens the infinite-volume variational identification. All identifications with the actual effective action or retained-history domains remain explicit inputs.

## 1. Fourier conventions and alias weights

Let M be an odd positive integer, fine spacing eta=1/M and coarse spacing one. For coarse momentum z and alias r in {-(M-1)/2,...,(M-1)/2}^d, set

    D_r,mu(z)=M(exp(i(z_mu+2pi r_mu)/M)-1),
    D_r,mu^-(z)=M(exp(-i(z_mu+2pi r_mu)/M)-1),
    P_r(z)=sum_mu D_r,mu(z) D_r,mu^-(z).

The superscript minus is an analytic substitution, not complex conjugation at nonreal z. On real momenta it is complex conjugation. Write

    d_mu(z)=exp(i z_mu)-1,   b_mu(z)=d_mu(z)d_mu^-(z).

The centered block multiplier a_r is the average of exp(i(z+2pi r).x/M) over integer block sites x. The longitudinal string multiplier is

    ell_r,mu(z)=M^(-1) sum_(t=0)^(M-1) exp(i(z_mu+2pi r_mu)t/M),
    q_r,mu(z)=a_r(z) ell_r,mu(z).

Consequently q_r,mu D_r,mu=a_r d_mu, an entire identity, including points at which either derivative multiplier vanishes. With physical-volume Parseval normalization there is no additional M-dependent coefficient in the alias covariance sum.

For real x and arbitrary y, discrete Fourier orthogonality in r gives

    sum_r |a_r(x+i y)|^2
       =M^(-d) sum_(block x') exp(-2y.x'/M)
       <=exp(sum_nu |y_nu|).

Also |ell_r,mu(x+i y)|<=exp(|y_mu|). Therefore

    sum_r |q_r,mu(x+i y)|^2
       <=exp(sum_nu |y_nu|+2|y_mu|).

The estimate holds for every real x, not only the fundamental momentum cube. In particular the real alias squared sum is at most one. These estimates are independent of M and prevent the growing number M^d of aliases from entering the constants.

## 2. Maxwell quotient versus Feynman covariance

For real nonzero coarse momentum p, all P_r(p)>0. The fine Maxwell form on an alias is

    A_r^* [P_r I-D_r D_r^*] A_r.

Equivalently it is inf_(lambda_r) P_r |A_r-D_r lambda_r|^2. The coarse gradient produced by a fine gradient is d sum_r a_r lambda_r. Since a_0(p) is nonzero on the coarse fundamental cube, this scalar average is surjective. Thus minimizing the Maxwell action subject to Q A=B is exactly

    inf_theta (B-d theta)^* C_F(p)^(-1)(B-d theta),

where

    C_F=diag(c_mu),
    c_mu=sum_r q_r,mu(p)q_-r,mu(-p)/P_r(p).

The diagonal form follows from the identity Feynman covariance P_r^(-1)I, not from a choice of transverse basis. Eliminating theta gives

    q_eff=C_F^(-1)
       -(C_F^(-1)d)(d^* C_F^(-1))/(d^* C_F^(-1)d).

This establishes the gauge quotient before any analytic continuation. Inverting C_F alone would give the wrong Maxwell action.

At p=0, every nonzero alias has a_r(0)=0. The coarse average therefore reads only fine constant fields. These constants realize any B and have zero Maxwell energy. Hence q_eff(0)=0. This is the required coarse zero-mode statement and does not require assigning a finite Feynman covariance to its fine zero mode.

## 3. Exact cancellation of the complex null cone

Separate the r=0 term:

    c_mu=g_mu/P_0+R_mu,
    g_mu=q_0,mu(z)q_0,mu(-z),
    A=a_0(z)a_0(-z),
    D_mu=g_mu+P_0 R_mu.

Here q_-r,mu(-z) is equivalently the same multiplier evaluated at -z-2pi r. The high-alias function R_mu is the sum over r!=0.

The gradient identity gives g_mu=A b_mu/[D_0,mu D_0,mu^-] with its removable one-variable factors understood analytically. Therefore

    sum_mu b_mu/g_mu=P_0/A.

Set

    E=A^(-1)-sum_mu b_mu R_mu/(g_mu D_mu).

The elementary identity 1/D_mu=1/g_mu-P_0 R_mu/(g_mu D_mu) yields

    sum_mu b_mu/D_mu=P_0 E.

Substitute C_F^(-1)=P_0 diag(D_mu^(-1)) into the real-momentum quotient and cancel the common P_0^2. The result is

    q_eff(z)=P_0 diag(D_mu^(-1))
       -[diag(D_mu^(-1))d]
        [d^- diag(D_mu^(-1))]/E.

No P_0 denominator remains. In particular the complex hypersurface P_0(z)=0, not merely the real point z=0, has been removed from the formula. The remaining task is to prove that g_mu, D_mu and E remain nonzero in a common complex neighborhood. Real positivity alone would not supply that conclusion without the uniform analytic estimates below.

## 4. Uniform real gaps on an enlarged momentum cube

Choose pi<K<2pi, independent of M, and let |p_mu|<=K. For any nonzero alias and M>=3, the distance of at least one p_mu+2pi r_mu from 2pi M Z is at least 2pi-K. Applying sin t>=2t/pi on [0,pi/2] to the principal distance gives

    P_r(p)>=H_K:=4(2pi-K)^2/pi^2,   r!=0.

There are no high aliases for M=1. Let

    c_K=sin(K/2)/(K/2)>0.

The central normalized string factors have modulus at least c_K. Hence

    g_mu(p)>=g_*:=c_K^(2d+2),
    0<=R_mu(p)<=1/H_K,
    g_*<=D_mu(p)<=D_*:=1+dK^2/H_K.

The upper bound uses real alias Parseval and P_0(p)<=dK^2. For p!=0,

    E(p)=[sum_mu b_mu(p)/D_mu(p)]/P_0(p).

Since |d_mu(p)|>=c_K|p_mu| and |D_0,mu(p)|<=|p_mu|,

    E(p)>=c_K^2/D_*.

At p=0 the analytic defining expression gives E(0)=1, so the same lower bound holds there. These constants remain uniform in M. The enlarged real cube is useful: it supplies genuine open overlap across the periodic boundaries, rather than relying on derivative estimates at the edge of a closed cube.

## 5. Uniform complex strip

For z=p+i y, direct expansion gives

    Re P_r(z)
       =P_r(p)-2M^2 sum_mu cos((p_mu+2pi r_mu)/M)
                           [cosh(y_mu/M)-1]
       >=P_r(p)-exp(rho) sum_mu y_mu^2

when |y_mu|<=rho<=1. Choose rho so d exp(rho) rho^2<=H_K/2. Then every high-alias denominator has real part at least H_K/2. Applying Cauchy--Schwarz to the two alias factors and using Section 1 gives a uniform bound on R_mu throughout this open complex box. P_0 and the central multipliers are likewise uniformly bounded there, because their normalized frequencies are bounded independently of M.

Use nested real cubes strictly between pi and K, and shrink the imaginary width if necessary. Cauchy estimates on the larger box give uniform derivatives for g_mu and D_mu on the first smaller box. Their real lower bounds then give |g_mu|>=g_*/2 and |D_mu|>=g_*/2 for sufficiently small imaginary width, independent of M. In particular E is now holomorphic and uniformly bounded on that box. A second Cauchy shrinking, using the real lower bound c_K^2/D_*, gives

    |E(z)|>=c_K^2/(2D_*)

on a still smaller complex box whose real part contains [-pi,pi]^d in its interior. The canceled formula is consequently holomorphic and uniformly bounded there. This two-stage argument avoids assuming the desired nonvanishing of E while obtaining the estimates used to prove it.

## 6. Periodic gluing and kernel locality

On real momenta the original full alias sums are 2pi-periodic by permutation of alias labels modulo M. Their Maxwell quotient is therefore periodic away from the zero mode, and the continuous zero-mode value agrees. Analytic extensions on adjacent translated enlarged boxes agree on their open real overlaps. The identity theorem, applied successively in each complex variable, makes them agree throughout the complex overlaps. They glue to a bounded holomorphic 2pi-periodic symbol on a uniform tube about the real momentum torus.

Shifting each Fourier contour in the sign of its lattice displacement proves

    |q_eff(x)|<=C exp(-kappa |x|_1)

with C,kappa independent of M. For any finite periodic coarse lattice, evaluating the same symbol on its momentum grid gives the periodization of this kernel. Absolute convergence justifies the identity. Counting images, including coincident incidences on a short torus, gives uniform weighted Schur bounds in the periodic distance. No volume-dependent analyticity or large-torus assumption is needed.

## 7. From action locality to constrained covariance decay

Let the actual flat constrained precision be

    H_M=K_flat^* (q_eff,M+T^*T) K_flat,

where T is the fixed one-step contour map and K_flat the fixed one-step pivot solution. Their ranges and norms depend on the fixed blocking integer L and dimension, not on the earlier blocking factor M. Once this operator identity and a uniform lower bound H_M>=gamma I have been established, the kernel estimate above gives a uniform exponentially weighted Schur bound for H_M.

For a graph-distance weight f with |f(x)-f(y)|<=dist(x,y), conjugation by exp(t f) changes H_M by a matrix whose absolute row and column sums are bounded by

    sup_x sum_y |H_M(x,y)|[exp(t dist(x,y))-1].

This tends to zero uniformly as t decreases to zero, using a fraction of the exponential Schur bound. Choose t>0 so the bound is below gamma/2. The conjugated inverse has operator norm at most 2/gamma. Taking f centered at the target yields

    |H_M^(-1)(x,y)|<=(2/gamma) exp(-t dist(x,y)).

The same proof works on finite periodic graphs with their periodic distance. This is the required Combes--Thomas step. It uses both locality and the previously proved coercive lower bound; an energy upper bound alone would not suffice.

The Fourier argument proves the homogeneous full-block Maxwell action kernel. It does not by itself prove that an arbitrary retained-history boundary effective operator is a compression of that kernel. The original nonlinear minimizer and rooted/straight constraint match, together with any boundary operator identification, remain necessary before applying this conclusion to a particular source covariance.

## 8. Written-note comparison

The saved full derivation was read in its entirety. Its alias normalization, Hodge quotient, zero-mode calculation, exact cancellation, Parseval estimate, enlarged real domain, two-stage Cauchy argument, periodic gluing, block insertion and holomorphic Bloch inverse agree with the independent proof above. Its concrete high-alias bound is conservative and valid: for epsilon_0<=1/4, 4(pi-epsilon_0)^2/pi^2>3; the permitted imaginary perturbation changes the real part by less than one. The fixed one-step block dimension d(L^d-1), pivot range and kernel-to-Bloch estimate are also correct. Small periodic volumes are covered when the torus admits the stated fixed L-block tiling.

The precision kernel is exponentially local although it has a real massless zero mode. The covariance being inverted is the constrained and gauge-penalized operator with a separately established positive gap. The note keeps this distinction and the actual physical source interfaces explicit. Its exclusion of arbitrary retained histories and complex-background perturbation claims is appropriate.

### 8.1 Explicit infinite-volume minimizing lift

The note's infinite-lattice variational interpretation can be justified directly without relying only on finite-volume sampling. On real nonzero p, write h=diag(D_mu^(-1)) and

    theta=(d^*hB)/(d^*hd),   B'=B-d theta.

The central-box real bounds give

    |d theta|<=D_max/g_min |B|,
    |B'|<=(1+D_max/g_min)|B|.

The Feynman minimizer for B' is, componentwise,

    A_r,mu=conjugate(omega_mu(p_r)) (P_0/P_r) h_mu B'_mu.

For the central alias the ratio P_0/P_r is exactly one. For all other aliases it is at most d pi^2/4. Alias Parseval therefore bounds the sum of the squared norms of these fine fibers uniformly in M by a constant times |B|^2. This field averages to B', not B.

Correct that by adding only the central fine gradient

    A_0 -> A_0+u_0 theta/a_0.

Its average is d theta, so the constraint becomes exactly QA=B. Its Maxwell energy is zero and its cross terms with the other field vanish, by the gradient nullspace of the fine Maxwell matrix. Moreover

    |u_0|/|d|<=pi/2,   |a_0|>=(2/pi)^d,

so this correction also has squared norm bounded by a constant independent of M times |B|^2. Define it arbitrarily at the single zero momentum in the infinite-volume Fourier representation; on a finite torus use the separate constant-field construction there. The measurable uniformly bounded fibers define a square-integrable feasible lift attaining the pointwise minimum almost everywhere. Conversely every feasible field obeys the pointwise variational lower bound. This proves equality of the infinite-volume infimum and the quadratic form of the analytic symbol on square-integrable coarse fields.

The author agreed to include this complete construction. It closes a presentation gap in the passage from finite fibers to the infinite-volume variational statement; it does not alter any decay estimate or require a stronger physical hypothesis.
