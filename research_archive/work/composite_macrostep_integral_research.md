# Exact finite-regulator integral for a composite ordinary macrostep

17 October 2026. Research proof for the proposed macrostep. Physical primitive ratio is a fixed odd integer ell, macro ratio R=ell^s is fixed after s is chosen, and preceding refinement is M=ell^k. Every statement below is on a finite compatible periodic regulator. Constants may depend on ell,R but not on M or volume. This is a one-shot pushforward by the actual composite ordinary map; it is not asserted to equal s separately gauge-fixed or truncated integrations. No output artifact or compiler is used.

## 1. Inputs and the exact map

Let G be the compact matrix gauge group, with normalized Haar measure dg and normalized representation trace tau. A current link configuration is V. Gauge convention is

    V^u(b)=u(b_-) V(b) u(b_+)^-1.

Let F_R=M_ell^s be the actual composition of the primitive ordinary group averages. In particular, no equality F_R=M_R^direct is assumed. On its local analytic domain,

    F_R(V^u)=F_R(V)^(u restricted to final R-block centers).       (1.1)

For each R-block centered at y, choose the direct-R internal averaged-contour variable P_R(V;y,x), x in that block, independently of F_R. It has endpoint covariance

    P_R(V^u;y,x)=u(y) P_R(V;y,x) u(x)^-1.                       (1.2)

All its constituent paths stay inside the R-block. Define

    q(h)=1-Re tau(h),
    G_R(V)=sum_(y,x!=y) q(P_R(V;y,x)).                          (1.3)

For analytic continuations, replace q(h) by 1-tau(h+h^-1)/2. This is the absolute gauge penalty, not a background-relative penalty.

The geometry colleague's proof supplies the following local facts. For every final bond c, there is one selected current macroface centerline pivot p(c); its exact nonlinear equation reads no other selected pivot. For

    F_V(B;c)=log[F_R(exp(iB)V)(c) F_R(V)(c)^-1]/i,
    A_V=D_B F_V(0),

the pivot coefficient is

    A_(c,p(c))=R^(1-d) pi_c(V),  pi_c(1)=I,
    h_V(c)=R^(d-1) pi_c(V)^-1,  A_V h_V=I.                     (1.4)

The analytic retained chart Phi_V(z) is the unique small solution of F_V(Phi_V(z))=0 with every retained coordinate equal to z. Its derivative at zero is K_V. It is finite range at fixed R, and

    P_R(exp(i Phi_V(z))V)=P_R(exp(i E_free z)V),
    T_V h_V=0,  T_V K_V=T_V E_free.                           (1.5)

Here E_free inserts zero on pivots and T_V differentiates the relative contour map. These statements refer to the composite constraint and independent direct-R contour gauge. They do not identify their two nonlinear averaging maps.

## 2. A global measurable completion and exact gauge insertion

The local logarithmic formula alone does not justify integration over every compact gauge transformation. There are two honest versions of the identity: work on a gauge-invariant domain on which the contour mean is defined on complete orbits, or choose a measurable equivariant completion of the local maps. Such a completion can be constructed without altering their small-field values.

For completeness, take the finitely many path transporters U_j from y to x and select one reference T=U_1. For a fixed small conjugation-invariant neighborhood of the identity, if every U_j T^-1 lies in that neighborhood, define their mean as

    P(U_1,...,U_n)=Phi(U_1 T^-1,...,U_n T^-1) T,

where Phi is the **actual specified local source contour mean evaluated on the reference-normalized tuple**, with the same ordering, contour multiplicities and distinguished reference as that definition. Only its established local endpoint covariance and holomorphy are used; no Karcher-mean equation or alternative mean is substituted. Right covariance gives the displayed representation on the original small domain, and simultaneous conjugation covariance of Phi follows from endpoint covariance. On the complementary set put P=T. The good set is invariant under multiplication of all paths at their endpoints; its indicator is measurable. Thus the completion is G-valued, measurable, endpoint-equivariant everywhere, and equals the analytic source mean near the identity. It uses only the original block-internal paths.

Similarly complete each primitive ordinary average: compute its extended internal P variables and its reference coarse string T_c. On the conjugation-invariant set where all relative transported strings U_x T_c^-1 lie in the small logarithm domain, use its original logarithmic formula; otherwise use T_c. The resulting map is measurable and exactly gauge covariant. Composing it s times gives a global measurable F_R agreeing with the intended analytic composite near the identity. This choice on the complement is part of the definition of this proposed full pushforward; no equality with a different large-field completion is claimed. All ensuing local formulas are independent of that choice where the analytic maps agree.

Let H_R be the group of current-site gauges equal to the identity at every final R-block center; give its other site variables independent normalized Haar laws. Let n_s be their number. For any real g>0 put

    c(g)=integral_G exp[-q(h)/g^2] dh > 0.

Endpoint covariance and Haar invariance give the exact identity

    integral_(H_R) exp[-G_R(V^u)/g^2] du = c(g)^n_s.          (2.1)

Indeed every factor is exp[-q(P_R(V;y,x)u(x)^-1)/g^2], and its integral is c(g), independently of V. No Faddeev-Popov determinant is being silently discarded: the identity uses integration over the full compact site groups, with their Haar measures, and the explicit constant c(g)^n_s.

For any integrable gauge-invariant current density rho(V), and bounded test function f of the final configuration,

    integral dV rho(V) f(F_R(V))
      =c(g)^(-n_s) integral dV rho(V) f(F_R(V))
                                      exp[-G_R(V)/g^2].   (2.2)

Proof: insert (2.1), use Fubini, and for each u change V to V^u. Product link Haar, rho and F_R are invariant under this root-fixed gauge group. Equation (2.2) is an equality of finite pushforward measures; it does not require a globally regular delta-function density. It also holds after multiplying rho by a gauge-invariant orbit-domain indicator on which the local contour formula is defined on complete orbits.

A noninvariant small-field window must be introduced **after** this insertion. If 0<=chi_sf(V,W)<=1 is any measurable sector on F_R(V)=W, the gauged pushforward splits exactly into its chi_sf and 1-chi_sf pieces. There is no assertion that either piece separately satisfies (2.2) without the gauge factor. Positive original rho gives two positive pieces on real fields. Estimating the complement is a further large-field problem.

## 3. The physical stationary branch for this constraint

Let U_f(W) be the proved ordinary full minimizer with total refinement MR, with final spacing R in current physical units, and set

    V_p(W)=M_ell^k U_f(W),  F_R(V_p)=W.                    (3.1)

Let U_c(V) denote the ordinary minimizer at preceding depth M to current datum V, and S_M(V)=S(U_c(V)). For real data choose a common current comparison ball of radius delta_R, and a final datum ball b_R, so that:

* U_f(W) is in the current-scale minimum class;
* U_c(V), for ||log V/i||<delta_R, is in the full final-spacing-R minimum class;
* V_p(W) and the gauges below remain in that comparison ball;
* all analytic charts and the previously proved local coarse gauge invariance hold.

These are finitely many strict bounds with constants depending on R but independent of M and volume. They can be met by shrinking delta_R and then b_R. In d=4 the coupling-free Wilson action has no extra factor under the physical rescaling; potential and Holder norms have only fixed powers of R.

The two actual minimum comparisons are

    S_M(V_p)<=S(U_f),
    S(U_f)<=S(U_c(V_p))=S_M(V_p).

The second holds because exact composition makes U_c(V_p) a full feasible competitor. Hence

    S_M(V_p)=S(U_f),
    S_M(V)>=S_M(V_p) when F_R(V)=W and V is in the common ball. (3.2)

This uses neither a dynamic-programming assertion outside the common minimum classes nor a direct-R/composite average identity.

Now set u(y)=1 at final centers and u(x)=P_R(V_p;y,x) at the other current sites. Then

    V_*(W)=V_p(W)^u,  F_R(V_*)=W,  P_R(V_*;y,x)=1.         (3.3)

At fixed R this is a local analytic current gauge with ||log u/i||<=C_R||log V_p/i||. The proved coarse-action gauge invariance, using its smooth fine point-value extension, gives S_M(V_*)=S_M(V_p) after the above radius shrink. Since G_R>=0 and G_R(V_*)=0 on real fields, V_* is a local constrained minimum of S_M+G_R.

The reduced covariance colleague proves the uniform-in-M positive Hessian on this retained chart. Combined with local analytic chart bounds and D^2 S_M=q_M+O(||log V||), the pulled-back Hessian is A_M,0+O_R(||w||+||z||) throughout one fixed convex z-ball. Thus the real centered critical point is unique in a common smaller neighborhood. Gauge zero alone would not have proved that uniqueness. Constraint, gauge-zero and first-derivative identities then continue holomorphically to complex W. Complex fields are not asserted to minimize a real action.

The pre-gauge estimate is stronger than the fixed-R existence bound:

    ||a_p(W)||<=C_a||w||/R,  a_p=log V_p/i,                (3.4)

with the supported-family constant C_a fixed at primitive ell and independent of s,k. In contrast no 1/R contraction is asserted for a_*=log V_*/i.

## 4. Exact local constrained density and every normalization

Use real Hermitian Lie coordinates orthonormal for tau, with q=dim g. Let n_e be the number of positively oriented current bonds, n_c the number of final macro bonds and n_z=q(n_e-n_c). Write normalized Haar in exponential coordinates as

    d(exp(iX))=h_0 j(X) dX,  j(0)=1, h_0>0.               (4.1)

The group delta at the identity is delta_G(exp(iF))=h_0^-1 delta_(R^q)(F). This identity is meant with the exponential-coordinate volume measure: the factor j(F) takes its value one at F=0.

For a fixed real W in the small datum ball, use V=V_*(W), and choose the sector to be exactly the component of the analytic relative chart with retained coordinates z in a prescribed product window. Any additional indicator is retained explicitly. The ambient straightening psi_V has retained rows equal to the identity and diagonal pivot blocks, so

    det D psi_V(B)=product_c det A_(c,p) /
                                    det D_p F_V(psi_V(B);c).

Let j_c^str(V;B) be the analytic logarithm of this c-th ratio, zero at B=0. Let

    D_R(V)=product_c (det A_(c,p))^-1.                    (4.2)

All determinants have positive orientation in the real small chart. Solving the group constraint gives the exact local density

    c(g)^(-n_s) h_0^(n_e-n_c) D_R(V)
      integral dz [product_b j(Phi_V(z)(b))]
        exp[sum_c j_c^str(V;K_V z)]
        rho(exp(i Phi_V(z))V) exp[-G_R(exp(i Phi_V(z))V)/g^2]. (4.3)

The domain in (4.3) is the prescribed retained window, with every additional pulled-back indicator still present. This follows by first using the square ambient change X=psi_V(B), then solving A_V B=0 for the pivots. It is not a rectangular Jacobian det D Phi. Equivalently the unrearranged pivot factor is the product of inverse D_p F_V(Phi_V(z);c).

Suppose the local density has the representation

    rho(U)=exp[-S_M(U)/g^2+E(U)]

on the common chart, with any field-independent normalization tracked separately. Put z=g xi for positive real g, let A=A_M(V) be the exact Hessian of S_M+G_R pulled back through Phi_V, and set

    R_3(V,z)=S_M(exp(iPhi_V(z))V)+G_R(exp(iPhi_V(z))V)
               -S_M(V)-one_half <z,A z>.

There is no linear term because V is the physical centered branch. Define

    I(V,g,xi)= -g^-2 R_3(V,gxi)
               +sum_c j_c^str(V;K_V gxi)
               +sum_b log j(Phi_V(gxi)(b))
               +E(exp(iPhi_V(gxi))V)-E(V).                (4.4)

Then (4.3) is exactly

    c(g)^(-n_s) h_0^(n_e-n_c) D_R(V) g^n_z
       (2 pi)^(n_z/2) det(A)^(-1/2)
       exp[-S_M(V)/g^2+E(V)]
       E_(A^-1)[ chi_window(xi) exp I(V,g,xi) ].          (4.5)

This fixes the Gaussian convention: its density is det(A)^(1/2)(2pi)^(-n_z/2) exp[-<xi,Axi>/2] in retained Euclidean coordinates. Formula (4.5) uses no inferred quantum Hessian: it is the exact classical action-plus-gauge Hessian chosen for this integral, with Haar and the other logarithms left in (4.4).

The prefactors c(g)^(-n_s), h_0^(n_e-n_c) and g^n_z are field-independent vacuum normalizations. D_R(V) and det(A) are generally background-dependent and are not vacuum constants. Their existing local determinant analyses apply at this fixed R once the composite geometry and Gaussian estimates are supplied.

## 5. The exact cutoff and local measure interactions

Take a retained link/color-ball window chi_window(xi)=product_(b retained) 1{|xi(b)|<=r_cut}. Because Phi_V(gxi)(b)=gxi(b) at every retained bond, this is exactly the window in the original relative link coordinates of the chosen sector. It is not replaced by a cutoff on K_V xi or by a Euclidean ball on the whole macro fiber.

If the original sector additionally restricts pivot links, contours, plaquettes or a reconstructed fine field, those indicators are evaluated at their exact Phi_V(gxi) pullbacks. They are not removed by analytic chart equivalence. The one-shot macro sector is newly specified here; it has not been identified with the intersection of all the primitive source windows in s separate integrations.

At fixed R, every pivot Jacobian primitive has finite local support and is O_R(|g|r_cut). Haar inversion invariance gives log j(X)=O(|X|^2), hence the Haar logarithms are O_R(g^2 r_cut^2). The gauge third-and-higher remainder is O_R(|g| r_cut^3). By (1.5) its exact full gauge factor already reads only unchanged retained coordinates. On a full independent background product ball, its constant and linear terms must also be separated away from the physical gauge-zero branch. None of these finite-dimensional estimates incurs a sum over old refinement M.

They yield fixed support coefficient bounds after multiplying by the finite number of primitives per anchor, just as in the one-step measure module. The classical action remainder and inherited quantum terms require their own mixed-support estimates; finite range of the measure terms does not prove those estimates.

## 6. Exact pre-gauge fluctuation identity and common-ball extension

For the background relation V_*=V_p^u, define at each oriented link

    B_p(w,xi)=Ad_(u(b_-)^-1) Phi_(V_*(w))(gxi)(b).

Then the exact group identity is

    (exp(iPhi_(V_*)(gxi)) V_*)^(u^-1)
          =exp(iB_p(w,xi)) V_p(w).                        (6.1)

In particular g belongs inside the nonlinear chart; Phi_V(gxi) is not replaced by g Phi_V(xi). The gauge u depends on w, not on xi. For real u its adjoint is a color-norm isometry; on the common complex gauge ball its norm is bounded by a fixed R-dependent constant.

Let E be a holomorphic total inherited functional on the current potential product ball of radius b, gauge invariant on the original common invariance domain. It need not have gauge-invariant individual activity coefficients. On a sufficiently small overlap in w and gxi, both configurations in (6.1), and a small path of connecting gauges, lie in that domain, so their E values agree. The same equality for complex arguments follows by holomorphic uniqueness. If only exp(E) is originally specified, equality of logarithms requires the supplied compatible holomorphic logarithm branch; one must not create it from a possibly vanishing integral.

For a fixed final target radius b lying below all classical domains, (3.4) gives ||a_p||<=C_a b/R. Choose R>=4 C_a. Local chart and logarithm estimates give

    ||log[exp(iB_p(w,xi)) V_p(w)]/i||
       <= C_a b/R + C_R |g|r_cut.                         (6.2)

Thus C_R |g|r_cut<=b/4 puts this argument inside the old b-ball uniformly in M and volume. The inherited insertion on the right side of (6.1) is then an actual holomorphic function on the whole target b-ball even when the rooted argument on the left lies outside the old E domain. It is the analytic continuation of the common-domain germ; it is not a claim that E was initially defined on that rooted argument.

More generally replace gxi by lambda gxi. The same conclusion holds on a fixed lambda-disc with radius at least c b/(C_R |g|r_cut), with c chosen below the strict margins and all chart domains. This is the pointwise starting point for a lambda-Cauchy increment estimate.

There is **no change of integration variable xi** in this operation. The entire inherited contribution is continued: replace the outside factor E(V) in (4.5), where V=V_*, by E(V_p), and replace its increment in (4.4) by E(exp(iB_p)V_p)-E(V_p). Their product is the continued full inherited insertion. Leaving E(V_*) outside would be undefined on part of the enlarged domain. The Gaussian, its determinant, the pivot/Haar factors, absolute gauge penalty and retained cutoff stay exactly those of (4.5). No adjoint-change Jacobian or transformed cutoff is inserted.

## 7. Holomorphy, nonvanishing, and the mixed-support boundary

At fixed finite regulator and fixed real retained window, the continued integrand is holomorphic in w on the common smaller domain. The positive real baseline and its proved uniform complex precision neighborhood provide a consistent analytic determinant square root. On each compact subdomain the finite-dimensional cutoff integral has an integrable uniform majorant, so the integral itself is holomorphic by differentiation under the integral. It agrees with the original small-field integral on the nonempty overlap, hence is an analytic continuation of that germ.

For real small w and real physical input density, the integrand in the exact representation is positive, and the retained window has positive measure, so the integral is strictly positive. This does not prove nonvanishing on a volume-independent complex ball. A complex integral of pointwise nonzero analytic factors can vanish. A finite-volume germ of its logarithm follows near a positive base point, but its uniform radius is an additional conclusion of a suitable cluster expansion, not of domination.

Likewise a pointwise lambda-Cauchy estimate of the total E composition only gives an extensive bound in general. The required next lemma is an absolute strict support-family bound for

    a_lambda(w,xi)=log[exp(i Ad_(u^-1)Phi_(V_*)(lambda gxi)) V_p(w)]/i,

with w-support tails and an explicit local xi carrier collar. Only such a bound permits the core/tail activity theorem and lambda-Cauchy to produce an anchored O(epsilon |g|r_cut/b) interaction norm. This note does not infer that mixed norm from (6.2).

Purely classical and local measure coefficients have independent fixed classical domains; one may choose the quantum b once far below those domains. They need not undergo the same recurring b-to-b/C restriction as an arbitrary inherited E. Establishing their stationary-substituted strict supports, and the inherited mixed supports above, would allow the Gaussian theorem to be applied directly in w. The old input-domain problem is concentrated in the inherited insertion, not silently solved by changing the Gaussian representation.

## 8. Status and dependencies

**Proved directly here:** an equivariant measurable completion agreeing with the analytic local maps; the exact compact-orbit gauge insertion and c(g) normalization; the finite-regulator sector split; the fixed-R two-minimum comparison and gauge-zero representative; exact Haar/delta/ambient-pivot factors and retained-window identity; the pre-gauge full-fluctuation group identity; pointwise common-ball holomorphic extension; and the distinction from uniform nonvanishing or mixed-support bounds.

**Inputs from separate modules:** the composite one-pivot incidence and coefficient R^(1-d), local chart uniqueness and contour-pivot independence; the fixed-R retained Gaussian gap/locality uniformly in M; the existing homogeneous classical minimum, gauge invariance and pre-gauge supported amplitude theorem. The positive reduced Hessian gives common-neighborhood uniqueness once those inputs are combined. No claim is made for arbitrary source orbit domains, mixed histories, or a prescribed different global large-field completion.

**Still open:** the actual uniform joint (w,xi) supported family needed for inherited insertions; uniform complex nonvanishing via its cluster norm; the large-field complement; stable activity amplitudes, relevant/marginal extraction and coupling flow. Equality with s sequential quantum integrations or a direct-R ordinary average is neither used nor established.
