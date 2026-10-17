# Uniform spatial decay of the flat variational Gaussian

Research derivation, 16 October 2026. Repository and output files were not modified. The Fourier calculation and analytic estimates below concern the explicitly defined full-block flat quadratic model. Their application to the deposited physical Gaussian retains the constrained-minimizer and pivot-coordinate identification from Notebook 06. They do not establish a complex-background perturbation theorem.

## 1. Result and setting

Fix dimension `d` and an odd one-step blocking factor `L>=3`. Let `M=L^k` be the total averaging factor from spacing `eta=M^(-1)` to spacing one. The same argument works for any odd positive `M`.

For straight-string averaging define

    q_M(B)=inf_(Q_M^st A=B) ||d_eta A||_eta^2.

There are constants `rho_d>0` and `C_d'<infinity`, independent of `M`, such that the translation-invariant precision kernel of this quadratic form satisfies

    ||q_M(x)|| <= C_d' exp(-rho_d |x|_1).

Here and below a smaller positive exponent may be substituted without changing the statement. After the fixed one-step rooted constraint, averaged-path gauge penalty and pivot insertion, put

    A_(M,0)=K_flat^* [q_M+T^*T] K_flat.

The explicit lower gap from Notebook 06 and the preceding kernel bound imply constants `c_(d,L)>0`, `C_(d,L)<infinity`, independent of `M` and volume, such that its inverse in the retained coordinates obeys

    ||C_(M,0)(n,alpha;m,beta)||
       <= C_(d,L) exp(-c_(d,L)|n-m|_1).

The indices `n,m` are L-block coordinates and `alpha,beta` are retained bond labels within a block. Finite periodic covariances are periodizations of the infinite kernel and have the corresponding uniform bound in periodic block distance. This conclusion uses analyticity proved below, not the spectral gap alone.

The case `M=1` is included by the evident single-alias formulas. Color components are independent copies at flatness.

## 2. Exact alias symbols and normalization

Take a coarse Fourier momentum `z` and aliases

    p_r=z+2*pi*r,    r in I_M^d,
    I_M={-(M-1)/2,...,(M-1)/2}.

For complex `z`, all formulas are analytic continuations of real Fourier symbols; a superscript minus below means substitution of `-z`, not complex conjugation. Define

    a_M(p)=prod_nu [(1/M) sum_(s=-(M-1)/2)^((M-1)/2)
                                      exp(i p_nu s/M)],
    ell_(M,mu)(p)=(1/M) sum_(s=0)^(M-1) exp(i p_mu s/M),
    omega_mu(p)=a_M(p) ell_(M,mu)(p).

Then `omega_mu(p)` is exactly the multiplier of `Q_M^st` on the `mu` component. It is diagonal in the vector component, and all of these finite sums are `2*pi*M` periodic in every fine physical momentum coordinate.

Write

    u_(r,mu)^+(z)=M(exp(i p_(r,mu)/M)-1),
    u_(r,mu)^-(z)=M(exp(-i p_(r,mu)/M)-1),
    P_r(z)=sum_mu u_(r,mu)^+(z) u_(r,mu)^-(z)
          =4 M^2 sum_mu sin^2(p_(r,mu)/(2M)),
    d_mu^+(z)=exp(i z_mu)-1,
    d_mu^-(z)=exp(-i z_mu)-1,
    b_mu(z)=d_mu^+(z)d_mu^-(z)=4 sin^2(z_mu/2).

Telescoping of the longitudinal string gives the exact identity

    omega_mu(p_r) u_(r,mu)^+(z)=a_M(p_r) d_mu^+(z).       (2.1)

The analogous minus identity also holds. This is the Fourier form of the scalar-gradient intertwining, with the physical derivative and averaging factors included.

With physical volume Parseval, a coarse mode is

    B_mu(z)=sum_r omega_mu(p_r) A_(r,mu),

and the fine norm/energy for that mode sums over aliases with coefficient one. There is no additional `M^d` in the covariance alias sum below. One check is that a single embedded fine plane wave of fixed amplitude has the same volume norm as its coarse plane wave.

## 3. Maxwell minimization is a gauge quotient of the blocked Feynman covariance

For real `z!=0` in the central Brillouin zone, every `P_r` is positive. The fine Maxwell form in alias `r` is

    P_r |A_r|^2 - |(u_r^+)^* A_r|^2
      = min_lambda P_r |A_r+u_r^+ lambda|^2.

By (2.1), adding fine gradients changes the averaged field by a coarse gradient `d^+` times an arbitrary scalar: the central scalar multiplier `a_M(z)` is nonzero on the central real zone. It follows that the original constrained Maxwell infimum equals the Feynman infimum with its coarse constraint allowed to vary over `B+span(d^+)`.

The blocked Feynman covariance is diagonal:

    W(z)=diag(c_mu(z)),
    c_mu(z)=sum_(r in I_M^d)
              omega_mu(p_r) omega_mu(-p_r)/P_r(z).       (3.1)

Indeed minimizing `sum_r P_r |A_r|^2` under the prescribed average `B'` gives `B'^* W^(-1) B'`. A subsequent scalar minimization over `B'=B+d^+ lambda` gives

    q_M(z)=W^(-1)
       - W^(-1)d^+ [d^- W^(-1)d^+]^(-1)d^- W^(-1).     (3.2)

For real `z`, `d^-` is the conjugate row of `d^+`. Thus (3.2) is an ordinary positive quadratic quotient, not an identification of Maxwell precision with the inverse Feynman covariance alone.

The zero coarse mode is separate. At `z=0`, `a_M(2*pi*r)=0` for every nonzero alias. The zero alias reads the constant fine field with multiplier one. Any constant coarse bond field is realized by a constant fine bond field of zero Maxwell energy. Consequently

    q_M(0)=0.                                         (3.3)

No mass is inserted into the harmonic sector and no division by a zero gauge eigenvalue is used there.

## 4. Exact cancellation of the apparent complex massless poles

Single out the central alias and write

    A(z)=a_M(z)a_M(-z),
    g_mu(z)=omega_mu(z)omega_mu(-z),
    R_mu(z)=sum_(r!=0) omega_mu(p_r)omega_mu(-p_r)/P_r(z),
    D_mu(z)=g_mu(z)+P_0(z)R_mu(z),
    h_mu(z)=D_mu(z)^(-1).

Formally `c_mu=D_mu/P_0`. However we will not use this quotient on the zero set of `P_0`. Multiplying the two versions of (2.1) for the central alias gives

    sum_mu b_mu(z)/g_mu(z)=P_0(z)/A(z).                 (4.1)

The identity is initially checked where the factors are nonzero and then extended analytically wherever the displayed `g_mu,A` are nonzero. Set

    E(z)=A(z)^(-1)
       - sum_mu b_mu(z)R_mu(z)/(g_mu(z)D_mu(z)).         (4.2)

Subtracting the two reciprocals `1/D_mu-1/g_mu` yields the exact factorization

    sum_mu b_mu(z)h_mu(z)=P_0(z)E(z).                  (4.3)

Substitute `W^(-1)=P_0 diag(h_mu)` into (3.2) and cancel `P_0` using (4.3). The result is

    q_(M,mu nu)(z)=P_0(z)h_mu(z) delta_(mu nu)
        - h_mu(z)d_mu^+(z)d_nu^-(z)h_nu(z)/E(z).       (4.4)

This expression has no inverse power of `P_0`. In particular the complex null cone of the fine massless denominator is removed exactly, not estimated away. Formula (4.4) will be shown holomorphic on a uniform strip, and at `z=0` it equals zero as required by (3.3).

For `M=1`, `A=g_mu=D_mu=E=1`, `R_mu=0`, and (4.4) is the usual finite-range lattice Maxwell precision.

## 5. Uniform control of the high aliases

### 5.1 A Parseval bound, without counting aliases crudely

For one coordinate, discrete orthogonality gives the exact identity

    sum_(r in I_M) |(1/M) sum_(s in I_M)
           exp(i(x+2*pi*r+i*y)s/M)|^2
       =(1/M) sum_(s in I_M) exp(-2ys/M)
       <=exp(|y|).

Taking products in the coordinates and using

    |ell_(M,mu)(x+2*pi*r+i*y)|<=exp(|y_mu|)

gives

    sum_r |omega_mu(x+2*pi*r+i*y)|^2
       <= exp(sum_nu |y_nu|+2|y_mu|).                  (5.1)

The same bound applies after replacing the entire argument by its negative. Cauchy--Schwarz therefore bounds the sum of absolute products `|omega_mu(p_r)omega_mu(-p_r)|` by the right-hand side of (5.1). This estimate is independent of `M`; replacing it by the number `M^d` of aliases would lose the result.

### 5.2 An open tube with high-alias denominators bounded away from zero

It is useful to include a real margin at the Brillouin-zone boundary before invoking Cauchy estimates. Choose an absolute `epsilon_0<=1/4` and consider

    |Re z_mu|<pi+epsilon_0,
    |Im z_mu|<delta_0,       delta_0<=1/(4 sqrt(d)).

For `M>=3`, any nonzero alias has at least one fine momentum coordinate whose distance, modulo `2*pi*M`, from zero is at least `pi-epsilon_0`. Using the representative in `[-pi*M,pi*M]` and `|sin t|>=2|t|/pi` for `|t|<=pi/2` gives, on the extended real box,

    P_r(x)>=4(pi-epsilon_0)^2/pi^2>3,       r!=0.

For the complex perturbation,

    Re P_r(x+i*y)
      =P_r(x)-2M^2 sum_mu cos((x_mu+2*pi*r_mu)/M)
                                      [cosh(y_mu/M)-1]
      >=P_r(x)-d delta_0^2 cosh(delta_0).

Thus `Re P_r>=1` throughout this open tube, with considerable room in these conservative constants. For `M=1` there are no high aliases. It follows from (5.1) that every `R_mu` is holomorphic and uniformly bounded there. The finite alias sum causes no hidden limit interchange.

The other quantities `a_M`, `omega_mu`, `A`, `g_mu` and `P_0` are uniformly bounded on this tube as well. The averaging factors are finite sums with physical supports of bounded diameter. For example `|M(exp(iz/M)-1)|<=|z|exp(|Im z|/M)`, which bounds `P_0` on the enlarged real box independently of `M`.

### 5.3 Real lower bounds and a uniform smaller strip

On the central real box, write

    r_M(t)=sin(t/2)/(M sin(t/(2M))),   r_M(0)=1.

Then `a_M(z)=prod_nu r_M(z_nu)` and

    g_mu(z)=a_M(z)^2 r_M(z_mu)^2.

Since `2/pi<=r_M(t)<=1` for real `|t|<=pi`,

    g_mu >= g_min:=(2/pi)^(2d+2),
    A >= (2/pi)^(2d).

Also `P_r>=4` for every nonzero alias on this central box. The real case of (5.1) gives

    0<=R_mu<=1/4,
    g_min<=D_mu<=D_max:=1+d*pi^2/4.                    (5.2)

For nonzero real `z`, equation (4.3) gives

    E(z)=[sum_mu b_mu(z)/D_mu(z)]/P_0(z)
       >=4/[pi^2 D_max].                              (5.3)

Here `sum b_mu>=4|z|^2/pi^2` and `P_0<=|z|^2`. At zero, the analytic formula (4.2) gives `E(0)=1`.

The Cauchy argument can be made entirely inside open domains. On the slightly enlarged real box, the same real gaps hold with weaker constants: if

    c_0=2 cos(epsilon_0/2)/(pi+epsilon_0)>0,

then `r_M(t)>=c_0` for `|t|<=pi+epsilon_0`. The real alias bound is still at most one and the high-alias denominators are bounded below by one. Thus on this larger box one may use

    A>=c_0^(2d),
    g_mu,D_mu>=c_0^(2d+2),
    D_mu<=1+d(pi+epsilon_0)^2,
    E>=c_0^2/[1+d(pi+epsilon_0)^2],

with the value at zero supplied by (4.2).

First apply Cauchy estimates to the uniformly bounded holomorphic `A,g_mu,D_mu` on the original open tube, using a smaller real margin and imaginary width. Their real lower bounds then keep these three functions nonzero on a uniform smaller tube: integrate their uniformly bounded derivatives along `x+i t y`. Formula (4.2) is holomorphic and uniformly bounded on that smaller tube. Apply the same argument to `E`, using its real lower bound and again retaining a smaller real margin. This gives some `rho>0`, depending only on `d`, such that `A,g_mu,D_mu,E` are nonzero and their required inverses uniformly bounded for

    |Re z_mu|<pi+epsilon_1,
    |Im z_mu|<rho,

where `epsilon_1>0` is fixed. No Cauchy disk leaves the domain on which its bound has been proved. The displayed constants are not optimized; their positivity and independence of `M` are what is used.

Formula (4.4) is therefore holomorphic and uniformly bounded on this tube.

## 6. Periodic gluing and exponential precision coefficients

The singled-out-alias quantities `g_mu,R_mu` need not individually be `2*pi` periodic. The resulting precision is periodic. On real momenta away from zero, shifting any coordinate by `2*pi` permutes the alias set modulo `M`; the fine symbols are `2*pi*M` periodic. It leaves `W`, the coarse derivative, and therefore the quotient (3.2) unchanged. The zero mode is defined consistently by (3.3).

The uniform analytic extensions (4.4) consequently agree on real overlaps of neighboring Brillouin charts, and hence agree holomorphically there. The identity theorem can be applied successively to the complex coordinates. The positive real margin from Section 5 supplies genuine open overlaps. This glues them to a bounded holomorphic `2*pi`-periodic matrix symbol on a fixed strip around the entire real torus.

Define its infinite-lattice coefficient by

    q_M(x)=(2*pi)^(-d) integral_[-pi,pi]^d
                                      exp(i z dot x) q_M(z) dz.

Shift each contour by a fixed imaginary amount with sign chosen to decay at `x_mu`. For any `0<rho'<rho`, the bounded analytic symbol gives

    ||q_M(x)||<=C exp(-rho' |x|_1),                    (6.1)

uniformly in `M`. In particular, after reducing the exponent once more,

    sum_x exp(rho''|x|_1)||q_M(x)||<=C_(rho'',d),
         0<rho''<rho'.                                (6.2)

For a finite coarse torus the same alias minimization is evaluated at its allowed momenta. Its real-space precision is exactly the periodization of (6.1). All image sums converge absolutely. The periodized kernel has a uniform exponential bound in torus distance, after reducing the exponent if desired, even for small periods.

### 6.1 An L2 minimizing field in infinite volume

There is also a direct variational identification on the infinite lattice. For a real nonzero momentum set `h=diag(h_mu)` and

    theta=(d^- h B)/(d^- h d^+),
    B'=B-d^+ theta.

The real bounds in (5.2) imply

    |d^+ theta| <= (D_max/g_min)|B|,
    |B'| <= (1+D_max/g_min)|B|.

The Feynman minimizing field for `B'` is

    A_r^F=P_r^(-1) Q_r^* W^(-1) B'
         =diag(omega_mu(-p_r)) (P_0/P_r) h B'.

The central ratio is one, while every high ratio is at most `d*pi^2/4`. Alias Parseval then bounds `sum_r |A_r^F|^2` uniformly by a constant times `|B|^2`. Moreover `d^- h B'=0`, and (2.1) shows `(u_r^+)^* A_r^F=0` for each alias. Thus this field is fine transverse, and its Maxwell and Feynman energies are equal.

Its average is `B'`, so restore `B` by adding only the central fine gradient

    A_0=A_0^F+u_0^+ theta/a_M(z),
    A_r=A_r^F for r!=0.

This leaves Maxwell energy unchanged and gives `QA=B`. It is uniformly L2 bounded because

    |u_0^+|/|d^+|<=pi/2,
    |a_M(z)|>=(2/pi)^d.

In particular the scalar `theta` may have a `1/|z|` singularity, but the actual added bond field does not. These measurable minimizing fibers define a fine L2 field for every coarse L2 field; the single zero momentum has measure zero. For a finite torus its zero fiber is the constant zero-energy lift already specified. This proves that the bounded symbol is exactly the infinite-volume variational form, with no reliance on an unproved interchange of infima and a volume limit.

## 7. Fixed-L pivot and gauge reduction

The one-step objects here are the flat objects already checked in Notebook 05/06, with `L` fixed as `M` varies:

* `T` uses averaged paths inside each L-block, so is block diagonal and finite range.
* `Q^flat=Q_L^st-D_L aT` has support in the two endpoint blocks.
* For each positively oriented coarse bond, choose its center-line interface pivot. Its coefficient is `L^(-d)` and no other coarse equation contains that pivot. Therefore the insertion `K_flat` is finite range in block coordinates, with coefficients depending only on `d,L`.

Label the retained fields by `(n,alpha)`, where `n in Z^d` is an L-block and `alpha` ranges over the nonpivot positively oriented unit bonds whose base points belong to the block. There are `d(L^d-1)` scalar retained labels per block in this convention. The exact number is not essential; its independence of `M` is.

The full precision is

    A_(M,0)=K_flat^*[q_M+T^*T]K_flat.                  (7.1)

Grouping the unit-lattice kernel (6.1) into fixed L-blocks preserves exponential decay: the distance between sites in blocks `n,m` is at least `L|n-m|_1-d(L-1)`. Multiplication by the finite-range fixed maps `K_flat,T` only changes constants and a finite number of shifts. Thus there are `eta>0,C_A<infinity`, depending only on `d,L`, such that its block matrix kernel satisfies

    sum_n exp(eta |n|_1)||A_(M,0)(n)||<=C_A             (7.2)

uniformly in `M`. This is a spatial operator estimate; it is the extra information absent from spectral bounds alone.

The established flat gap gives

    A_(M,0)(kappa)>=gamma_* I                         (7.3)

for every real block Bloch momentum. The same conclusion follows directly from the infinite-volume lower form bound and continuity of the finite-dimensional block symbol. The global gauge directions have been removed by the compatible constraint and penalty; no inverse of the unreduced Maxwell symbol is asserted.

## 8. Holomorphic inversion and covariance decay

By (7.2), the block Bloch symbol

    A_M(kappa)=sum_n A_(M,0)(n) exp(-i kappa dot n)

is holomorphic in `|Im kappa|_infinity<eta`, with uniform bounds. For `|y|_infinity<=eta/2`,

    ||A_M(x+i y)-A_M(x)||
      <= |y|_infinity sum_n |n|_1 ||A_(M,0)(n)||
                                            exp((eta/2)|n|_1)
      <= C_1 |y|_infinity,                            (8.1)

where `C_1` is independent of `M`. Equation (7.3) implies `||A_M(x)^(-1)||<=gamma_*^(-1)`. Choose a fixed positive

    eta_C < min(eta/2, gamma_*/(2 C_1)),

omitting the second restriction if `C_1=0`. The Neumann inverse around each real `x` is then valid, so

    A_M(kappa)^(-1) is holomorphic,
    ||A_M(kappa)^(-1)||<=2/gamma_*

throughout `|Im kappa|_infinity<eta_C`. Fourier contour shifting proves

    ||C_(M,0)(n)|| <= (2/gamma_*) exp(-eta_C' |n|_1),
                   0<eta_C'<eta_C,                    (8.2)

up to the harmless matrix-entry versus block-operator convention. All block dimensions are fixed, so this convention never introduces an `M` factor.

Finite tori sample the same block symbol. Their inverse covariance is therefore the exact periodization of the inverse-symbol Fourier coefficients, not the inverse of a truncated infinite covariance. Absolute convergence proves a uniform exponential estimate in the shortest periodic block distance. The argument works with any positive number of blocks in each periodic direction, using the oriented periodic-cell convention of the lower-gap audit. It also proves convergence of finite-volume kernels to the infinite kernel on each fixed region as every period tends to infinity, for fixed `M`; the exponential image error is uniform in `M` when that comparison is made at the same `M`.

## 9. What has and has not been supplied for Yang--Mills

For the explicitly normalized flat quadratic model, the argument supplies uniform exponential precision and covariance kernels. The central work is the gauge-quotient cancellation (4.4), the uniform alias Parseval estimate (5.1), and the fixed-block inversion using the independently proved gap. None of these steps imports a preexisting non-Abelian covariance decay theorem.

The rooted and straight flat constraints have equal curl-energy infima by the previously proved gradient adjustment. Consequently the result applies to the actual flat full-block physical Gaussian if its action part is the differentiated constrained Wilson minimum and its independent coordinates use the stated flat pivot insertion. Notebook 06 records the finite-regulator Hessian/implicit-function comparison and its gauge caveat. The primary physical definitions are in [Bałaban CMP109](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf), (0.21)--(0.22), (2.6)--(2.11); this note does not replace the underlying nonlinear minimizer theorem.

The following are not conclusions of this flat calculation:

1. Weighted smallness of the actual complex free-current precision perturbation, or of its first and second source responses.
2. Control of arbitrary nontrivial real backgrounds, retained domains with holes, frozen boundary bonds or mixed large-field histories.
3. Identification of a shifted sharp-cutoff domain, or a claim that cutoff coordinates may be changed without tracking that domain.
4. Nonlinear RG control, coupling trajectories, or a continuum Yang--Mills construction.

The concrete advance is that a uniform exponentially local **flat reference covariance** can be derived directly in the full-block setting. The next interface is to show that the actual complex carrier perturbs this reference in a uniform weighted local norm.

## 10. Free low-momentum normalization in the bond-midpoint basis

This is an additional consistency check for the flat model only. Let

    U_mu(z)=exp(i z_mu/2)

and conjugate the real symbol into the bond-midpoint convention, analytically continued as `q_mid(z)=U(-z)q_M(z)U(z)`. Formula (4.4) becomes

    (q_mid)_(mu nu)(z)=P_0(z)h_mu(z) delta_(mu nu)
        -4 h_mu(z)sin(z_mu/2)sin(z_nu/2)h_nu(z)/E(z).

The functions `g_mu` and `R_mu` are even in each momentum coordinate. For `R_mu`, reflect the corresponding alias component; the finite alias set is invariant and the phase in `omega_mu(p)omega_mu(-p)` has canceled. Consequently `D_mu,h_mu,E` are also even in each coordinate. Their values at zero are

    g_mu(0)=D_mu(0)=h_mu(0)=E(0)=1,
    R_mu(0)=0.

The uniform analytic neighborhood gives uniform second-derivative bounds by Cauchy. Hence

    h_mu(z)=1+O(|z|^2),
    E(z)=1+O(|z|^2),
    P_0(z)=sum_mu z_mu^2+O(|z|^4),

where the constants are independent of `M`; in the last identity, the direct sine expansion has coefficients bounded uniformly for `M>=1`. Substitution yields

    q_mid(p)=|p|^2 I-p p^T+O(|p|^4)                   (10.1)

for real small `p`, uniformly in `M`. The corresponding complex Taylor statement uses `sum p_mu^2` in place of the real Euclidean norm squared. Thus the flat quadratic model has the expected Maxwell normalization at low momentum. This is not an interacting continuum-limit result, a claim about a renormalized coupling, or an extension of a physical carrier beyond flatness.
