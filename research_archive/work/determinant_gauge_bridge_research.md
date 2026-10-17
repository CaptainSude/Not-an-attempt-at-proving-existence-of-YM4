# Exact finite gauge and coarea bridge for the actual determinant

17 October 2026. Research proof for independent audit. This gives a finite-dimensional identity for the actual leading pivot/Gaussian correction, a concrete counterexample to a tempting uniform ghost estimate, and an exact list of the remaining comparison terms. It does not prove that the Maxwell coefficient differs by a bounded finite part from a massive background-Feynman reference.

## 1. Coordinates at the actual constrained saddle

Fix a finite compatible regulator and a composite endpoint K=ell^k. The preceding action may be S_M; the prospective reference comparison uses M=1. Let U=V_*^(M,K)(W) be the actual physical saddle, with F_K(U)=W and P_K(U)=I. All finite matrices below use the actual current-link angle and scalar-site counting coordinates, in a real trace-orthonormal color basis.

In left-relative coordinates x, define

    s(x)=S_M(e^(ix)U),
    f(x)=log[F_K(e^(ix)U)W^(-1)]/i,
    C=f'(0).

The target coordinate is a left-relative group increment at W. It is not the ordinary logarithm of W. At the saddle there is a unique target multiplier lambda with

    s'(0)=C^T lambda.

Set

    L=s''(0)-sum_c lambda_c f_c''(0).                 (1.1)

This is the Hessian of the critical Lagrangian s-lambda.f. The second term is the full constraint-current curvature. It cannot be dropped merely because the field is a constrained minimizer.

Let p be the actual pivot coordinate set, C_p its invertible block diagonal pivot matrix, and E the retained-coordinate insertion. The source chart derivative is

    h=I_p C_p^(-1),   K0=E-h C E,
    C h=I,           C K0=0.                        (1.2)

Use K0 for the insertion to distinguish it from the endpoint ratio K. The exact nonlinear chart x=Phi(z) has

    Phi'(0)=K0,
    Phi''(0)[u,v]=-h f''(0)[K0u,K0v].

The chain rule and s'=C^T lambda give the actual action Hessian K0^T L K0. The absolute contour gauge is zero at this saddle. In the normalization of the established gauge penalty, its Hessian is T^T T, where T is the derivative of the contour logarithms. Therefore the actual retained precision is

    A_T=K0^T (L+T^T T) K0.                          (1.3)

Its positivity was proved in the physical saddle module. The leading amplitude, apart from background-independent constants, is

    d_K(U) det(A_T)^(-1/2),   d_K(U)=|det C_p|^(-1). (1.4)

At real small backgrounds the determinant signs are fixed by continuation from the positive flat convention. Final formulas below use normalized logarithms log det X(W)-log det X(1), then holomorphic continuation of those branches.

## 2. Exact based gauge nullspace and gauge replacement

Let D_b map scalar site parameters vanishing at all K-centers to their left-relative infinitesimal gauge variations at U. Its domain has one color copy per noncenter site. The ordinary composite constraint is exactly invariant under this based gauge group, so

    C D_b=0.                                       (2.1)

The scalar s-lambda.f is also based-gauge invariant and is critical at zero. Differentiate its gauge identity at this critical point. The gradient term drops, leaving

    L D_b=0.                                       (2.2)

This is an identity for L, not in general for s'' alone. The actual contour endpoint covariance gives

    T D_b=-I                                       (2.3)

with the standard orientation; changing the sign convention changes only this sign. If the gauge penalty uses a fixed scalar color normalization, it can be absorbed into T and a background-independent determinant, which cancels from the normalized amplitude.

The based action is free, hence D_b is injective. Put

    G_b=D_b^T D_b>0.

We prove a general finite gauge-change fact. Let B_0 be any symmetric form on a finite space Z, with nullspace exactly im V, positive on its quotient, and let F_1,F_2:Z->R^s have F_j V invertible. Then

    |det(F_1 V)| det(B_0+F_1^T F_1)^(-1/2)
      =|det(F_2 V)| det(B_0+F_2^T F_2)^(-1/2).       (2.4)

Choose any complement E_0 to im V and write z=E_0u+V alpha. Its fixed change-of-variable Jacobian is the same for both integrals. The B_0 term depends only on u. Integration in alpha gives (2pi)^(s/2)/|det(F_j V)| independently of u, by translation of alpha. Integrating u proves (2.4). This argument retains the orbit-coordinate density; it cancels only because the same decomposition is used in both integrals.

Apply this on Z=ker C, parametrized by K0. The vertical retained insertion V is the retained restriction of D_b, so K0 V=D_b. The form K0^T L K0 is nonnegative, its nullspace is exactly im V, and it is positive on the quotient. Indeed T can remove any contour component along D_b; on the contour-zero complement the already positive A_T equals this form.

For F_1=T K0 and F_2=D_b^T K0, equations (2.1)-(2.3) give F_1 V=-I and F_2 V=G_b. Thus

    det(A_T)^(-1/2)
       =det(G_b) det(A_b)^(-1/2),
    A_b=K0^T (L+D_b D_b^T) K0.                     (2.5)

This is exact at every real small physical saddle. It is a replacement of the actual based contour gauge by based covariant divergence. It is not yet a replacement by a full-site massive Feynman gauge.

## 3. Coarea removes the pivot exactly

Let B be any symmetric coarse matrix for which

    Q_b=L+D_b D_b^T+C^T B C                         (3.1)

is positive definite. Such a completion exists at every fixed finite saddle: L+D_bD_b^T is positive on ker C, so a sufficiently large scalar B makes its complementary Schur block positive. B>0 alone need not suffice at an arbitrary nonflat saddle. The identity below only requires Q_b>0; B itself may be indefinite.

Define

    M_b=C Q_b^(-1) C^T>0.

The constrained Gaussian integral has two exact evaluations:

    integral dx delta(Cx) exp[-x^T Q_b x/2]
      =(2pi)^((n-m)/2) |det C_p|^(-1) det(A_b)^(-1/2)
      =(2pi)^((n-m)/2) [det Q_b det M_b]^(-1/2).
                                                               (3.2)

For the first, write x=K0 z+h y. In retained/pivot order the determinant of this transformation is det(C_p)^(-1), Cx=y, and the restriction of Q_b is A_b. For the second, the centered full Gaussian with covariance Q_b^(-1) sends Cx to a Gaussian with covariance M_b; its density at zero gives the stated factor.

Equivalently, the purely algebraic identity is

    det Q_b det(C Q_b^(-1) C^T)
                 =(det C_p)^2 det A_b.              (3.3)

The delta is normalized in the target's relative Lie coordinate. The actual output density is relative to target group Haar; its chart density at the origin is the fixed h0, not j(log W). No field-dependent target Haar factor has been omitted. If one instead uses induced Euclidean measure on ker C, its coarea factor is precisely accounted for by (3.2).

Combining (1.4), (2.5) and (3.2) gives the actual normalized correction:

    D_(M,K)(W)
       =N_0[ log det G_b
             -(1/2) log det Q_b
             -(1/2) log det M_b ],                 (3.4)

where N_0 F=F(W)-F(1). Thus the inverse pivot is eliminated, but a coarse constraint determinant remains. This determinant is essential. Every admissible completion B gives the same combined expression by (3.3); individual terms need not be independent of B or gauge invariant.

At a fixed finite regulator the matrices are invertible on a small real germ, with fixed branches. The determinant identities are algebraic and extend holomorphically wherever the stated inverses and chosen branches exist; equality of the combined expression can also be continued through the already defined actual D. No common complex radius uniform in K or volume is inferred for the three individual logarithms.

## 4. A canonical positive completion from the exact minimum value

This further identity uses the actual minimum action, not a guessed background Hessian. In the same relative target coordinate put

    s_eff(y)=S_(MK)(e^(iy)W),
    lambda=s_eff'(0),     q_eff=s_eff''(0).

The envelope identity gives the same lambda as in Section1. The scalar

    R(x)=s(x)-s_eff(f(x))

is critical at x=0, is invariant under the full local fine gauge group, and is nonnegative near zero by the actual local minimum comparison. Its Hessian is

    H_res=L-C^T q_eff C >=0.                         (4.1)

The inequality is an ordinary finite real quadratic-form statement. It uses the strengthened local minimum comparison among all nearby fields, not only stationarity. Full local gauge invariance of S_M and S_(MK), together with equivariance of F_K, gives

    H_res D_f=0                                     (4.2)

for every fine infinitesimal gauge direction D_f (with any convenient fixed global base convention).

If H is the actual derivative of the minimum section in these relative coordinates, then C H=I and R vanishes identically along that section. Since H_res is positive semidefinite,

    H_res H=0,       L H=C^T q_eff.                 (4.3)

No source flat-gauge lift is substituted for the actual H.

There is now a canonical positive ambient completion,

    Q_b=H_res+D_bD_b^T+C^T C.                       (4.4)

If x lies in its nullspace, then Cx=0, D_b^Tx=0 and x^T L x=0. Positivity of the constrained quotient says x=D_b alpha; then G_b alpha=0, hence x=0. Thus (4.4) is positive definite. It is the completion (3.1) with B=I-q_eff, which need not itself be positive.

There is a stronger exact identification of the general coarse compression. Define the divergence-gauge-adjusted minimum lift

    H_b=H-D_b G_b^(-1)D_b^T H.

Then C H_b=I, D_b^T H_b=0, H_res H_b=0 and L H_b=C^T q_eff. For the general completion (3.1),

    Q_b H_b=C^T(q_eff+B),
    q_eff+B=H_b^T Q_b H_b>0.

Consequently

    Q_b^(-1)C^T=H_b(q_eff+B)^(-1),
    M_b=(q_eff+B)^(-1).                             (4.5)

The exact determinant bridge can therefore also be written

    D_(M,K)=N_0[ logdet G_b-(1/2)logdet Q_b
                              +(1/2)logdet(q_eff+B)]. (4.6)

Thus the coarse covariance is the inverse of the ACTUAL relative-coordinate effective Hessian plus the chosen completion. It is not an unspecified orbit density. For the canonical choice B=I-q_eff, M_b=I identically, and (4.6) reduces to N_0[logdet G_b-(1/2)logdet Q_b]. The coarse action has not disappeared: it is inside H_res=L-C^Tq_eff C and hence inside Q_b.

All identities in Sections1-4 are exact finite ones. The positive gap of (4.4) has not been bounded uniformly as K grows.

## 5. The based ghost does not have a uniform physical mass gap

At the flat background, D_b is the ordinary nearest-neighbor gauge gradient restricted to scalar functions zero at all K-block centers. On a compatible unit-current lattice torus with K>=3, take one real color and

    phi(x)=0 at every K-center, and phi(x)=1 elsewhere.

There are n_c centers and n_f=K^d n_c fine/current sites. Each center contributes exactly 2d incident edges with squared difference one. Therefore

    ||phi||_2^2=(K^d-1)n_c,
    ||D_b phi||_2^2=2d n_c,
    lambda_min(G_b)<=2d/(K^d-1).                    (5.1)

This is an upper Rayleigh bound, not a claim of a matching spectral asymptotic. In d=4 it already implies

    ||G_b^(-1)||>= (K^4-1)/8.

A reference mass at the final physical scale is K^(-2) in these unit-current coordinates. Hence a claim ||G_b^(-1)||<=C K^2 is false uniformly in K. After rescaling final spacing to one, the physical operator K^2 G_b still has a Rayleigh eigenvalue tending to zero like at most K^(-2).

The example does not disprove a bounded Maxwell-coefficient difference for the COMPLETE expression (3.4). It proves that treating this ghost alone as a uniformly massive physical operator is invalid. The vector and coarse determinant can cancel precisely the soft point-pinning contribution.

## 6. An exact full-site/coarse Schur decomposition

One can make the coupled nature more explicit without yet estimating it. Fix a single final center as a global base. Let D_f be the fine gauge generator for all scalar sites except this base. Split its domain into non-K-centers and the other K-centers:

    D_f=[D_b,D_e].

This is a decomposition of site-coordinate columns. It is not an orthogonal decomposition of their images. The globally based action is free, so

    G_f=D_f^T D_f>0,
    S_g=D_e^T(I-D_b G_b^(-1)D_b^T)D_e>0,
    det G_f=det G_b det S_g.                         (6.1)

Let Q_b be any positive completion in Section3, and put

    Q_f=Q_b+D_eD_e^T,
    S_v=I+D_e^T Q_b^(-1)D_e.

The matrix determinant lemma gives

    det Q_f=det Q_b det S_v.                         (6.2)

Consequently (3.4) is exactly

    D_(M,K)=N_0[
       log det G_f -(1/2)log det Q_f
       -log det S_g +(1/2)log det S_v
       -(1/2)log det M_b ].                          (6.3)

Here S_g and S_v are coarse SITE matrices, and M_b is a coarse BOND matrix. The first two factors resemble vector and ghost determinants, but (6.3) retains the complete coarse correction package. G_f is still globally based, not the translation-invariant all-site massive ghost in the reference calculation.

If there is no nonbase coarse site, the site matrices in (6.1)-(6.3) are zero-dimensional and their determinants are one. The canonical completion has M_b=I by (4.5); for a general completion its contribution is +(1/2)logdet(q_eff+B). These are specializations of the same exact formula.

For the canonical completion (4.4),

    Q_f=s''+D_fD_f^T
          -lambda.f''+C^T(I-q_eff)C.                (6.4)

Against a specified massive reference vector operator

    P_eta=s''+D_fD_f^T+eta^2 I,     eta=K^(-1),

the exact difference is

    Q_f-P_eta=-lambda.f''
                   +C^T(I-q_eff)C-eta^2 I.          (6.5)

The first term is the actual constraint-current curvature. It vanishes at the flat background, but its first and second background derivatives generally survive in the determinant Hessian. The second is a coarse completion, and the last changes the infrared regulator. Neither the rank of the coarse terms nor their being absent at zero automatically bounds their Maxwell contribution.

Equation (6.5) is a proposed comparison interface, not an identification of P_eta with a particular author's operator D_W^2. The actual lattice Hessian, gauge normalization, mass, global-base removal and background parametrization must match first. Any logarithmic comparison using P_eta also requires its invertibility on the selected finite germ; no uniform neighborhood is inferred here.

## 7. A bounded coarse effective-Hessian contribution

One comparison term can now be controlled uniformly in the classical depth. Fix a sufficiently small positive coarse spatial exponent mu and a fixed analytic radius rho. The established strict scalar family for the entire action S_(MK), including its pair-supported quadratic baseline, is uniform in MK and volume and has an arbitrary prescribed fixed cardinality reserve. These are the actual inputs cl-action-theorem, cl-action-norm and cl-hessian-support and the full-baseline paragraph of classical_support_localization_fragment.tex.

For W=e^(iw), use the per-bond relative BCH coordinate

    Xi_w(y)=log(e^(iy)e^(iw))/i.

It has uniformly bounded local derivatives on a fixed small joint ball, with no spatial support enlargement. The relative Hessian is exactly

    q_eff(w)[u,v]
       =D^2S_(MK)(w)[E_w u,E_w v]
          +DS_(MK)(w)[U_w(u,v)],
    E_w=D_y Xi_w(0),   U_w=D_y^2 Xi_w(0).            (7.1)

The second term is retained. Compose each scalar support coefficient with Xi_w(y), differentiate twice in y, and up to twice in w using smaller fixed Cauchy radii. Rows, columns and all variable supports remain in the same carrier. A fixed cardinality reserve pays each finite row/source-slot count. Thus q_eff has a uniform exponentially weighted Schur bound

    sup_(||w||<rho) ||q_eff(w)||_mu <=R_mu,           (7.2)

independent of MK and compatible volume. Its first and second source derivatives have uniform strict incidence bounds. In particular, after reducing mu to m>0, for scalar coarse-coordinate sources x,y,

    sum_ij e^(m[d(i,x)+d(j,x)]) |(partial_x q_eff)_ij| <=C_1,
    sum_ij |(partial_x partial_y q_eff)_ij|
                                      <=C_2 e^(-m d(x,y)).
                                                               (7.3)

These estimates follow directly by splitting the support-tree exponential between source separation and the row-to-source distance, then summing the latter. The coarse coordinate fiber has fixed dimension; there is no K^4 microscopic-coordinate factor.

Choose one fixed a>2R_mu and use the completion B=aI. Then

    P_c(w)=q_eff(w)+aI,
    ||P_c(w)^(-1)||_mu<=2/a,                         (7.4)

by the convergent weighted Neumann series. The corresponding fine Q_b is also positive on the real germ: decompose x=xi+H_b y with Cxi=0; its quadratic form is the sum of the positive constrained-divergence form in xi and y^T(q_eff+aI)y. This proves positivity but not a uniform fine gap.

At fixed finite volume,

    logdet P_c(w)=dim(P_c) log a
                 +sum_(n>=1) (-1)^(n+1)Tr[(q_eff(w)/a)^n]/n

with absolute convergence. Let K_c be the Hessian of N_0 logdet P_c, so the desired half-logarithm has Hessian K_c/2. Explicitly,

    K_c(x,y)=Tr[P_c^(-1) q_eff,xy
                   -P_c^(-1) q_eff,x P_c^(-1) q_eff,y].

Equations (7.3)-(7.4), with a spare exponential portion along one inverse edge between the source-rooted vertices, give

    |K_c(x,y)|<=C_a e^(-m' d(x,y)),                 (7.5)

uniformly in MK and volume. The first trace uses the second line of (7.3); the second uses its two first-derivative bounds and the inverse's weighted Schur bound. Periodic sums are bounded by the infinite lattice sums.

The second displacement moment is therefore uniformly bounded. The actual finite beta ratios (above their reference threshold), and the true infinite beta in any joint limit, obey

    |beta( (1/2) N_0 logdet(q_eff+aI) )|<=C_coarse.   (7.6)

This is an actual O(1) coarse-factor bound independent of the endpoint and old depth, not a claimed estimate for the fine determinants. In (4.6), with B=aI, it isolates the remaining task to the fine based vector/ghost combination

    logdet G_b -(1/2)logdet[
                s''-lambda.f''+D_bD_b^T+a C^TC].

The action's local gauge identities also make the relative-coordinate Hessian transform by the corresponding orthogonal bond-frame conjugation under real local gauges, so the massive coarse determinant has the appropriate total local gauge identity on its common germ. The trace bound itself only requires its actual local analytic coefficient bounds; no coefficientwise Ward identity is used.

For any completion the full-site vector difference from the proposed reference is Q_f-P_eta=-lambda.f''+C^T B C-eta^2I. For this fixed-a choice it is -lambda.f''+a C^TC-eta^2I. Equation (6.5) describes the different canonical completion B=I-q_eff. The general decomposition is valid for either, but its individual comparison terms must be taken consistently from the same completion.

## 8. What a uniform reference comparison must still prove

The deposited Raw I outline around lines3901-4014 asserts a comparison of the composite one-loop coefficient with a vector/ghost expression of the form

    -(1/2)logdet(D_W^2+eta^2)+logdet(Delta_0+eta^2),
    eta=ell^(-k),

with a bounded error in the extracted Maxwell coefficient as k grows. The outline does not by itself identify those operators with (6.3). The primary background-field papers use a formal background effective action and particular gauge/ghost conventions; their explicit massless nonzero-external-momentum amplitudes do not supply this finite-part comparison automatically.

For a specified matched reference, the exact finite bridge reduces the remaining proof to these concrete estimates:

* after the proved bounded coarse effective-Hessian factor in Section7 is removed, a uniform Maxwell-moment bound for the remaining coarse-site package -logdet S_g+(1/2)logdet S_v, combined with the chosen global-base/mass ghost correction if the full-site formulation is used;
* a uniform Maxwell-moment bound for logdet Q_f-logdet P_eta, with the full multiplier, coarse-completion and mass terms for the selected completion, not an operator-norm assertion that point-pinned inverses are uniformly massive;
* the relation between the reference's background field and the actual smooth pre-gauge minimum. The based-gauge covariance of (3.4) permits computation at that pre-gauge representative, but does not identify it with an arbitrary continuum interpolation or prescribed external background;
* volume and zero-mode control allowing the resulting bound to hold for the actual finite reference-normalized extraction, uniformly in the old depth/allowed regulator family required by the finite shooting hypothesis.

The determinant Hessian of a positive matrix family P is explicitly

    d^2 logdet P[u,v]
       =Tr(P^(-1)P_uv-P^(-1)P_u P^(-1)P_v).

Thus each requested estimate can be formulated as an absolutely convergent second-background-derivative trace with a second displacement moment, using the already derived actual vertices. Existing fixed-K exponential estimates make these traces meaningful but allow constants depending on K. They do not establish the required O(1) bound as K->infinity.

The based ghost counterexample shows exactly why a separate uniform inverse bound cannot fill this gap. A coupled cancellation or a scale-resolved comparison is required. No universal coefficient, sign, averaged drift, or stable ultraviolet coupling trajectory follows from the identities alone.
