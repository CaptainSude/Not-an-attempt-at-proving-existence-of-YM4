# An exponentially local flat minimizing extension

16 October 2026. This note derives an explicit minimizing right inverse for the full-block flat Maxwell problem. It uses the common complex momentum strip and notation established in `flat_covariance_decay_research.md`. Repository and output files were not edited. The selected gauge is characterized below; it is not silently identified with a source axial or multilevel Landau gauge.

## 1. Result, norms and scope

Let `M` be odd, `eta=M^(-1)`, and let `Q_M^st` be the physical straight-string average from the fine lattice to the unit lattice. There is a translation-covariant linear extension `H_M` such that

    Q_M^st H_M=I,
    ||d_eta H_M B||_eta^2=q_M(B)
       =inf_(Q_M^st A=B)||d_eta A||_eta^2.             (1.1)

The extension is selected by minimizing fine L2 norm among all energy minimizers. This is a gauge choice, not an additional energy penalty in (1.1).

Its alias symbols, and those of its fine curl, extend holomorphically to a momentum strip of width independent of `M`, with uniform operator norms

    C^d -> ell^2(I_M^d;C^d),
    C^d -> ell^2(I_M^d;C^(d choose 2)),                (1.2)

respectively. Alias norms have counting measure. After reconstruction into fine coordinates within a coarse cell, (1.2) becomes the physical cell norm

    ||v||_(cell,2)^2=M^(-d) sum_(s in I_M^d)|v(s/M)|^2.

In fact, for every fixed `0<alpha<1`, both reconstructed symbols have uniform norms from `C^d` to the physical cell Hölder space

    ||v||_(cell,C^alpha)
       =sup_s |v(s/M)|
          +sup_(s!=t) |v(s/M)-v(t/M)|/|(s-t)/M|^alpha. (1.3)

The same estimates hold on a fixed-width physical collar of a cell. Their coarse-cell Fourier coefficients consequently obey

    ||H_M(n)||_(C^d -> cell,C^alpha)
       +||(d_eta H_M)(n)||_(C^d -> cell,C^alpha)
       <=C_alpha exp(-rho_alpha |n|_1),               (1.4)

with positive constants independent of `M`. The analogous estimate holds in the physical cell L2 norms. The fine curl in these formulas includes the factor `eta^(-1)=M`.

Finite compatible periodic operators are obtained by exact periodization. These statements concern the explicit homogeneous flat extension. They prove neither a nonflat source-response theorem nor the equality of this selected extension with a differently gauge-fixed source minimizer.

## 2. Symbols recalled from the decay proof

Use `r in I_M^d`, `I_M={-(M-1)/2,...,(M-1)/2}`, and `p_r=z+2pi r`. Write

    a_r=a_M(p_r),
    omega_(r,mu)=a_M(p_r) ell_(M,mu)(p_r),
    u_(r,mu)^+=M(exp(i p_(r,mu)/M)-1),
    u_(r,mu)^-=M(exp(-i p_(r,mu)/M)-1),
    P_r=sum_mu u_(r,mu)^+u_(r,mu)^-,
    d_mu^+=exp(i z_mu)-1,
    d_mu^-=exp(-i z_mu)-1.

Superscript minus on `a_r` or `omega_r` means evaluation at `-p_r`; it is the conjugate only on real momenta. The exact gradient identity is

    omega_(r,mu)u_(r,mu)^+=a_r d_mu^+.                (2.1)

Set

    A=a_0 a_0^-,
    g_mu=omega_(0,mu)omega_(0,mu)^-,
    R_mu=sum_(r!=0) omega_(r,mu)omega_(r,mu)^-/P_r,
    D_mu=g_mu+P_0 R_mu,
    h_mu=D_mu^(-1),       h=diag(h_mu),
    E=A^(-1)-sum_mu d_mu^+d_mu^- R_mu/(g_mu D_mu).

Then

    d^- h d^+=P_0 E,
    q_M=P_0 h-h d^+d^- h/E.                          (2.2)

On a fixed strip, with a positive real margin around the Brillouin cube, the functions in (2.2) are holomorphic and uniformly bounded and `A,g_mu,D_mu,E` are uniformly separated from zero. The high denominators `P_r`, `r!=0`, obey the uniform quadratic lower bounds of the decay/limit notes. The central denominator `P_0` can vanish on a complex cone, and must be canceled rather than bounded away from zero.

## 3. A scalar energy-minimizing right inverse

Define the additional scalar remainder and denominator

    R_s=sum_(r!=0) a_r a_r^-/P_r,
    D_s=A+P_0 R_s.                                   (3.1)

High-alias Parseval gives exactly the same holomorphy and uniform boundedness for `R_s` as for the vector remainders. On the central real cube,

    0<=R_s<=1/4,
    (2/pi)^(2d)<=D_s<=1+d*pi^2/4.

On a slightly enlarged real cube the corresponding weaker positive bounds also hold. The same Cauchy-and-shrinking argument therefore supplies a fixed smaller strip on which `D_s` and its inverse are uniformly bounded. We work on the intersection of this strip with the previously established one. The factors `a_0,a_0^-` are also uniformly bounded away from zero there, since their product `A` is and each factor is bounded.

The scalar minimizing right inverse has aliases

    t_0=a_0^-/D_s,
    t_r=P_0 a_r^-/(P_r D_s),    r!=0.                (3.2)

They satisfy

    sum_r a_r t_r=1                                 (3.3)

as an analytic identity. For real `z!=0`, the scalar covariance is

    W_s=sum_r a_r a_r^-/P_r=D_s/P_0,

and (3.2) is `t_r=P_r^(-1)a_r^-/W_s`. Thus `t theta` minimizes `sum_r P_r|lambda_r|^2` subject to `sum_r a_r lambda_r=theta`. The formula at zero is `t_0=1`, `t_r=0` for `r!=0`, consistent with the constant scalar lift. No zero scalar gradient is inverted there.

## 4. Minimizing extension and exact pole cancellation

For real nonzero `z` and input `B`, put

    S=d^- h B,
    theta=S/(P_0 E),
    F_r=P_r^(-1) diag(omega_r^-) q_M B,
    H_r B=F_r+u_r^+ t_r theta.                       (4.1)

The vector `theta` is a scalar for each color component. These uncanceled formulas explain the construction but are not used to define it on the complex null cone.

The central alias cancels to

    (H_0 B)_mu=omega_(0,mu)^- h_mu B_mu
        +(u_(0,mu)^+/a_0)(R_mu h_mu-R_s/D_s) S/E.     (4.2)

To verify this, use

    diag(omega_0^-)h d^+
        =diag(u_0^+/a_0)[1-P_0(R_mu h_mu)_mu],
    A/D_s=1-P_0 R_s/D_s.

Substituting into the two central terms of (4.1) cancels their entire `P_0^(-1)` part. The sign of the `R_s/D_s` term is negative.

For each high alias the canceled formula is

    H_r B=P_r^(-1) {
          P_0 diag(omega_r^-)h B
        +[u_r^+ a_r^-/D_s-diag(omega_r^-)h d^+] S/E
                         },       r!=0.              (4.3)

Equations (4.2)--(4.3) define the holomorphic extension. None contains a central massless denominator. At zero, `H_0 B=B` and every high alias is zero. In particular the construction gives the constant fine field for a constant coarse bond field.

## 5. Right inverse, energy and the selected gauge

For real nonzero momentum, `q_M B=W^(-1)(B-d^+theta)`, with `W` the blocked Feynman covariance. Hence

    sum_r diag(omega_r)F_r=B-d^+theta.

The gradient term averages, by (2.1) and (3.3), to `d^+theta`. This proves `QH=I`. All these identities extend analytically after the cancellations; at the zero mode the statement follows directly from the constant lift.

Moreover `d^-q_M=0` and therefore

    (u_r^+)^*F_r=(a_r^-/P_r)d^-q_M B=0              (real z).

Thus `F_r` is fine transverse. Its fine Maxwell energy equals its Feynman energy, which is the minimized coarse quotient `B^*q_M B`. The added term is a fine gradient, so its curl vanishes exactly. This proves the minimizing identity (1.1).

The choice is more specific than an arbitrary energy minimizer. For `z!=0`, the transverse part of an energy minimizer is unique because its fine transverse quadratic form is strictly positive. Every other minimizing field has that same `F_r` plus fine gradients `u_r^+lambda_r` with `sum a_r lambda_r=theta`. Orthogonality of transverse and gradient parts gives

    sum_r |F_r+u_r^+lambda_r|^2
      =sum_r |F_r|^2+sum_r P_r|lambda_r|^2.

The scalar minimization in Section 3 therefore makes `H` the unique least-fine-L2-norm energy minimizer. At zero, the fixed constant component and zero high gradients give the same unique minimum-norm choice. This also characterizes the finite-volume linear extension without a momentum-dependent gauge ambiguity.

There is a useful exact divergence identity. Let `D_f^*` denote the adjoint fine forward gradient, whose alias multiplier is `u_r^-`. Then

    (D_f^*H B)_r=a_r^- S/(D_s E).                   (5.1)

Indeed the transverse term vanishes, while
`P_r t_r theta=P_0 a_r^-theta/D_s`. The right side of (5.1) is already canceled and holomorphic, including at zero.

Let `Q_0` be the scalar block average in the physical volume norms. Its adjoint extends a coarse scalar as a blockwise constant fine scalar, and

    Q_0 Q_0^*=I,
    R_0:=I-Q_0^*Q_0,
    R_0 D_f^* H=0.                                  (5.2)

Thus the divergence lies in the range of the scalar block-average adjoint. Equivalently, `H` is orthogonal to fine gauge variations whose scalar block mean is zero, exactly the gauge variations preserving the straight one-form constraint. The identity (5.2) is intrinsic to this explicitly chosen flat gauge. Whether a symbol named `R` in a source theorem equals this `R_0`, and whether its source chart selects this same minimizer, requires a separate definition check.

## 6. Uniform alias Hilbert bounds, including the curl

For `r!=0`, the common strip gives

    |P_r|>=c|r|_2^2,
    |u_r^+|<=C(1+|r|_2).

The latter follows directly from `|M(e^(ip/M)-1)|<=|p|exp(|Im p|/M)`. Scalar and vector alias Parseval give

    sum_r |a_r^-|^2<=C,
    sum_r sum_mu |omega_(r,mu)^-|^2<=C_d.            (6.1)

In (4.3), the central factors `P_0,h,d,S/B,D_s^(-1),E^(-1)` are uniformly bounded. The coefficients of high `a_r^-` are bounded by `C|u_r|/|P_r|`, and those of high `omega_r^-` by `C/|P_r|`. These ratios are uniformly bounded for nonzero aliases. Equation (6.1) proves

    sum_r |H_r(z)B|^2<=C|B|^2.                     (6.2)

The central term is bounded separately by (4.2). No alias-count factor enters.

For curl, the gradient term in (4.1) vanishes identically, so for high aliases

    (d_eta H)_r B
       =P_r^(-1) u_r^+ wedge[diag(omega_r^-)q_M B].   (6.3)

Using `|u wedge v|<=|u||v|` and (6.1) again gives a uniform alias Hilbert bound. At the central alias one simply uses `u_0^+ wedge H_0` in the canceled formula. This proves both operator estimates (1.2) on the same fixed strip. Fine colors merely give independent copies.

## 7. Stronger absolute summation and physical Hölder estimates

The componentwise sine estimates in the refinement-limit note give, uniformly on a fixed smaller enlarged tube,

    w(r)=prod_nu(1+|r_nu|)^(-1),
    |a_r^-|<=C w(r),
    |omega_(r,mu)^-|<=C w(r)/(1+|r_mu|).

Consequently (4.3) and (6.3) imply, for high aliases,

    ||H_r||+||(d_eta H)_r||
       <=C w(r)/(1+|r|_infinity).                   (7.1)

This bound covers the fine-zone edge aliases as well as fixed aliases.

On the dyadic shell `2^j<=|r|_infinity<2^(j+1)`, at least one coordinate has size in that range. Its harmonic sum is bounded by an absolute constant, while each of the other coordinate harmonic sums is bounded by `C(1+j)`. Taking a union over the `d` possible largest coordinates gives

    sum_shell w(r)<=C_d(1+j)^(d-1).

For every `alpha<1`, summing the resulting geometric series proves

    sum_r (1+|r|_infinity)^alpha
               [||H_r||+||(d_eta H)_r||]<=C_(d,alpha). (7.2)

The central term has been included using its previously proved bound. At `alpha=0`, this is a uniform absolute alias sum; at positive `alpha<1`, it controls physical fine-coordinate Hölder regularity.

For clarity, (7.2) does not give a uniform absolute sum for a full additional fine derivative at exponent one. One can infer a uniform full-gradient alias L2 bound from `|u H_r|<=C w(r)` and square summability of `w`, but a pointwise full-gradient bound is not proved by this argument. The curl is better controlled because it annihilates the added gauge gradient exactly.

## 8. Reconstruction, periodic gluing and locality in coarse cells

For a within-cell fine site `s in I_M^d`, define the reconstruction matrix

    F_M(z)_(s,r)=exp(i(z+2pi r) dot s/M),
    H_cell(z;s)=sum_r exp(i p_r dot s/M)H_r(z).        (8.1)

The same formula reconstructs the curl aliases at fine plaquette base points. For real `z`, `F_M(z)` is unitary from counting-measure alias ell2 into the cell norm `M^(-d)sum_s|v_s|^2`. This is finite Fourier orthogonality with the physical volume weight. For complex `z=x+iy`,

    F_M(x+iy)=diag_s(exp(-y dot s/M)) F_M(x),

so both its operator norm and inverse norm are bounded by `exp(sum|y_nu|/2)`, independently of `M`. Combining with Section 6 proves the cell-L2 bounds in Section 1.

To obtain the Hölder bounds, let `xi=s/M` and `xi'=t/M` lie in a fixed physical cell or any fixed bounded physical collar. On the common strip,

    |exp(i p_r dot xi)-exp(i p_r dot xi')|
       <=C_alpha (1+|r|)^alpha |xi-xi'|^alpha,

where the constant depends on the collar size and strip but not on `M`. It follows by combining the derivative bound and the bounded-exponential bound, and using `min(1,t)<=t^alpha`. Apply (7.2) to (8.1). This gives the uniform physical Hölder operator norms (1.3) for the field and curl, including fixed collars. A collar formulation also controls pairs crossing a coarse-cell boundary; it is not restricted to pairs inside a disconnected collection of cell interiors.

The alias vector itself is not a fixed-index `2pi`-periodic function of `z`. On real momenta, a `2pi` shift permutes the aliases modulo `M`. This follows from the uncanceled minimization formulas: the full scalar and vector Feynman covariances, the coarse derivative and the quotient are periodic, while fine factors are `2pi M` periodic. Formula (8.1) compensates this alias permutation. A wrapped fine alias changes its exponential by `exp(i2pi s_nu)=1`, because `s_nu` is an integer. Therefore `H_cell`, and similarly its curl, are genuinely `2pi`-periodic in the coarse momentum.

The canceled formulas are holomorphic on overlapping enlarged Brillouin charts and agree there on real points. They glue by the identity theorem exactly as in the precision proof. The reconstructed symbols are thus bounded holomorphic periodic operator-valued functions into each physical cell norm above, on a strip independent of `M`. Every target space is finite dimensional for fixed `M`; the norm bounds are independent of that dimension.

Fourier contour shifting now gives the coarse-cell coefficient estimate (1.4). In explicit kernel form, if `x=n+s/M`,

    (H_M B)(n+s/M)=sum_m H_M(n-m;s)B(m).

The bound is on `s -> H_M(n-m;s)` in the physical cell norm, with the analogous statement on collars. It provides genuine spatial locality of the map to fine coordinates, not merely boundedness in alias space. Taking the reduced exponent also gives uniform exponentially weighted coarse-cell row sums. The L2 version defines a bounded map from coarse ell2 to fine physical-volume ell2.

For a compatible finite torus, evaluate the same periodic symbols on its coarse momentum grid. Its extension kernel is the exact absolutely convergent periodization of the infinite kernel. Weighted row-sum bounds use the periodic distance and are uniform in the periods, including short periods with the usual oriented-cell multiplicities. The right-inverse and minimizing identities follow either fiberwise or by periodization.

## 9. What this gives for later source matching

The construction supplies an explicit flat minimizing map with uniform locality and regularity. It is a stronger input than a bound on the minimized quadratic form alone. Its pure gauge action is also explicit:

    H_M d^+ phi=(u_r^+ t_r phi)_r.

The gauge selected by this formula has blockwise-constant fine divergence, equivalently (5.2), and is the least-fine-L2-norm representative of the energy-minimizing affine space.

The actual Yang--Mills minimizer may be presented in an axial gauge or a different Landau chart, and the deposited multilevel projector called `R` may encode further constraints. The present proof does not identify those maps or their derivatives with `H_M` just from equality of their minimized energies. In particular, a change to a source gauge can alter potential norms, cutoff coordinates and locality unless its gauge transformation is independently controlled. The current construction does not establish such a transformation, a nonflat extension, or independent-current analytic response estimates.

Within the explicit flat full-block problem, however, the proposed formulas are valid: the central pole cancels, both field and curl have uniform holomorphic alias-Hilbert bounds, and their fine-cell kernels have exponential coarse-cell locality with physical Hölder regularity of every fixed order below one.

## 10. A stronger extension in the transcribed source scalar gauge

The source-gauge check in `flat_minimizer_source_gauge_research.md` identifies a different scalar projection. On a real homogeneous regulator, put `Delta=D_f^*D_f` and let

    G'=(Delta+Q_0^*a'Q_0)^(-1),
    P=G'Q_0^*(Q_0G'^2Q_0^*)^(-1)Q_0G',
    R=I-P.

The deposited source formulas are Raw I 23909--23918 and 23937--23944. The original CMP99b PDF was not independently recovered in this check. Algebraically, `P` is the orthogonal projection onto `ran(G'Q_0^*)`, and

    ran R=Delta ker Q_0.

In a nonzero Bloch fiber, `ker R=ran(Delta^(-1)Q_0^*)`. The zero fiber must be treated through the mass-penalized definition of `G'`, not by assigning an inverse to the constant scalar Laplacian.

Replace the scalar weight in Section 3 by

    R_(s,2)=sum_(r!=0) a_r a_r^-/P_r^2,
    D_(s,2)=A+P_0^2 R_(s,2),
    t_(2,0)=a_0^-/D_(s,2),
    t_(2,r)=P_0^2 a_r^-/(P_r^2 D_(s,2)),  r!=0.

Again `sum a_r t_(2,r)=1`. Its scalar variational characterization is minimization of `sum P_r^2 |lambda_r|^2` under the same scalar average. The new extension is

    Hsrc_r B=F_r+u_r^+ t_(2,r) theta,

with the same transverse field `F`, `theta`, and `S` as in Section 4. It has the same constraint and the same minimum Maxwell energy. It selects the least-divergence-norm representative among the energy minimizers, instead of the least-potential-norm representative selected earlier.

The exact central cancellation is

    (Hsrc_0 B)_mu=omega_(0,mu)^- h_mu B_mu
       +(u_(0,mu)^+/a_0)
          (R_mu h_mu-P_0 R_(s,2)/D_(s,2)) S/E.        (10.1)

For a high alias,

    Hsrc_r B=P_r^(-1)diag(omega_r^-)q_M B
       +u_r^+ P_0 a_r^- S/(P_r^2 D_(s,2)E).          (10.2)

All central poles have canceled. The real scalar remainder is nonnegative, at most `1/16` on the central cube, and `D_(s,2)>=A`. Alias Parseval and the high denominator gap prove uniform holomorphy and boundedness of the remainder, and a further fixed shrinking keeps `D_(s,2)` away from zero. Thus (10.1)--(10.2) are uniformly holomorphic on a common strip.

The divergence is, for nonzero real fibers,

    (D_f^*Hsrc B)_r
       =P_r^(-1)a_r^- [P_0 S/(D_(s,2)E)].            (10.3)

It belongs to `ran(Delta^(-1)Q_0^*)`, and hence `R D_f^*Hsrc=0`. At zero, the extension is constant and its divergence vanishes. Formula (10.3) is interpreted centrally through the canceled value `a_0^-S/(D_(s,2)E)`.

The high-alias bound improves to

    ||Hsrc_r||<=C w(r)/(1+|r|)^2,
    ||u_(r,nu)^+ Hsrc_r||+||u_r^+ wedge Hsrc_r||
                         <=C w(r)/(1+|r|).          (10.4)

The first term in (10.2) has two high-denominator powers of frequency, and the added gradient is smaller still, of order `w(r)/(1+|r|)^3`. The dyadic summation already proved therefore gives uniform physical **discrete C^(1,alpha)** cell norms for `Hsrc`, and C^alpha norms for its curl, for every `alpha<1`. The discrete derivative is the full fine forward derivative `M[A(x+e_nu/M)-A(x)]`. Reconstruction, integer-coordinate periodic gluing and contour shifting are unchanged. Thus this source-gauge variant has exponential coarse-cell locality in those stronger norms. No uniform pointwise second-derivative or Laplacian norm is inferred from this summation argument.

### 10.1 Homogeneous flat source matching by uniqueness

The bond operator also has an explicit deposited match. Raw I 24349--24373 transcribes the corrected one-step average. At the trivial background its transports are identities and all four correction brackets vanish, leaving exactly `Q_L^st`. Raw I 47046--47048 states that the multilevel `Q_j` are compositions. The straight-average semigroup therefore identifies the homogeneous flat composite with `Q_(L^j)^st`. This is different from the rooted next-step `Qflat` used for pivot elimination; they must not be conflated.

For this matched constraint, the Maxwell-minimizing field satisfying the transcribed `R D_f^*H=0` gauge is unique. In a nonzero Bloch sector, the difference of two minimizers is `u_r^+lambda_r`. The zero coarse average implies `sum a_r lambda_r=0`, so `Delta lambda` lies in `ran R`. The gauge difference gives `R Delta lambda=0`, hence `Delta lambda=0`, and the difference field vanishes. In the zero fiber, the coarse constraint fixes the fine constant harmonic one-form, all remaining zero-energy differences are high-alias gradients, and the same argument kills them.

Consequently the normalized homogeneous flat source minimizing right inverse, when it satisfies the stated source variational and gauge identities, is `Hsrc`. If the source notation writes `QH_0=ell^(-1)`, the normalized map to compare is `H_0 ell`, not `H_0` without that factor (Raw I 13638--13655). This is an identification with the explicit deposited homogeneous flat definitions and their stated minimizing property; it does not independently reverify the unavailable primary proof, nor extend the conclusion to nonflat backgrounds, independent currents, holes or mixed histories.

The first extension of Sections 3--9 remains a valid alternate gauge. It should not be labeled source-compatible merely because its minimized energy agrees. The variant (10.1)--(10.2), with the explicit projector and corrected bond-constraint match just stated, is the one selected by the transcribed source gauge.
