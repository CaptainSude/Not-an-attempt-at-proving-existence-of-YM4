# A finite stationary-Gaussian cocycle for the actual determinant correction

17 October 2026. Research proof for independent audit. This is an exact identity of the LEADING normalized stationary amplitudes on a finite regulator. It does not equate direct and sequential sharp-window quantum sectors. The proof uses a common local orbit-tube integral solely to identify their leading coefficients.

## 1. Actual maps, measures and the proposed identity

Fix a finite compatible periodic regulator, a preceding homogeneous depth M, and two fixed allowed ratios R=ell^r and L=ell^s. Let X, Y, Z be the current, R-coarse and RL-coarse link configuration spaces, each with product normalized Haar measure. The maps are the ACTUAL iterated ordinary maps

    f=F_R:X->Y,       h=F_L:Y->Z,
    h o f=F_(RL).                                      (1.1)

No equality with a direct-R or direct-RL ordinary average is used.

The coupling-free current action S_M is the actual homogeneous ordinary minimum action, normalized at the identity. It is analytic and locally gauge invariant on its established small-link domain. For a step of ratio K, let V_*^(M,K)(W) be the physical gauge-zero stationary representative for the independently chosen direct-K contour gauge P_K. Let A_(M,K)(W) be the exact retained Hessian of S_M+G_K at this point, in the actual constraint chart, and let d_K(V_*) be its inverse pivot-Jacobian product. Use a lower-case d_K here to avoid confusion with the correction D.

The background correction already identified in the actual macro integral is

    D_(M,K)(W)
      =log[d_K(V_*^(M,K)(W))/d_K(1)]
        -(1/2) log det[A_(M,K)(W) A_(M,K)(0)^(-1)].
                                                               (1.2)

Thus D_(M,K)(1)=0. It is Delta+Qdet with the stated positive real determinant branches, analytically continued near the identity. Determinants act on the actual retained coordinates; constraint curvature and the absolute contour-gauge Hessian are included.

Write V_p^(MR,L)(W) for the pre-root-gauge intermediate stationary representative and T_(MR,L) for substitution into it. The claim is

    D_(M,RL)(W)
       =D_(M,R)(V_p^(MR,L)(W))+D_(MR,L)(W).             (1.3)

The equality is first a real small-field germ on this finite regulator and then extends to every connected common analytic product domain of the two sides. Constants such as Haar normalizations, powers of g, compact gauge integrals and flat determinants disappear because all three D's are normalized at the identity.

## 2. The based gauge groups and normalized Haar

Let H_R be the group of current site gauges equal to I at every R-center, and H_(RL) the group equal to I at every final RL-center. Restriction to the intermediate R-centers gives the exact sequence

    1 -> H_R -> H_(RL) -> H_L -> 1.                    (2.1)

Here H_L is the intermediate site-gauge group based at final centers. In fact the site sets split: H_R uses all non-intermediate current sites, while an embedded H_L is identity away from intermediate centers. These are disjoint coordinate groups, so their product is the full H_(RL). Normalized Haar disintegrates exactly as product Haar; no background-dependent orbit-volume factor is introduced.

The actions are free. A gauge preserving all links and equal to I at one specified site on a connected graph is I everywhere, by propagating the bond equation along paths. There are final centers, so this applies to H_R and H_(RL), and similarly to H_L on the intermediate graph.

Ordinary averaging is gauge equivariant:

    f(U^u)=f(U)^(u restricted to intermediate centers),
    h(V^v)=h(V)^(v restricted to final centers).         (2.2)

Hence f is H_R-invariant, h is H_L-invariant, and h o f is H_(RL)-invariant. Product link Haar is invariant under all these site actions.

The source contour variables obey endpoint covariance. For a based gauge u in H_K,

    P_K(U^u;y,x)=P_K(U;y,x)u(x)^(-1),

and the actual absolute penalty G_K=sum_(x not a center)q(P_K), q(g)=1-Re tau(g), gives the exact identity

    integral_(H_K) exp[-G_K(U^u)/g^2] du=c(g)^(n_s,K),
    c(g)=integral_G exp[-q(v)/g^2] dv.                  (2.3)

It follows that an H_K-invariant local orbit-tube integral can be gauged by G_K, with the exact factor c(g)^(-n_s,K). This factor is independent of the background. The eventual proof does not need its asymptotic constant or its power of g.

## 3. A consistent local orbit-tube action

We need a common integral on which Fubini is legitimate, without pretending that S_M was originally defined on every gauge orbit.

Here is an explicit consistency argument at fixed RL. Suppose U and V are both in a small current-link ball and V=U^u for u in H_(RL). In a unitary-invariant matrix norm the bond equation implies

    ||u(x)-u(x+e_mu)||
         <=C(||U(x,mu)-I||+||V(x,mu)-I||).             (3.1)

Every current site lies within at most C_d RL edges of a final center, where u=I. Thus

    ||u-I||_infty<=C_d RL
                         (||U-I||_infty+||V-I||_infty). (3.2)

For a sufficiently small ball, depending on the fixed ratios, u has its near-identity logarithm lambda. The logarithm is Lipschitz on that chart, so (3.1) also bounds its edge differences. Along u_t=exp(t lambda), the transformed links U^(u_t) have size at most a fixed multiple of the endpoint smallness, with fixed color-coordinate norm conversions. Choose the comparison ball small enough that this entire path remains in the established upstream action domain. Local Ward invariance then gives

    S_M(U)=S_M(V).                                     (3.3)

The same reasoning works for the intermediate action and H_L. No radius uniform in RL is required here.

Consequently, on the H_(RL)-saturation of a sufficiently small representative neighborhood, define

    S_ext(U^u)=S_M(U).                                 (3.4)

This is independent of the representative by (3.3). The action of the compact based group is free. The actual contour gauge supplies a local slice: P_(RL)=I, because the unique based gauge taking U to this slice is u(x)=P_(RL)(U;y,x). Thus (3.4) is a smooth, indeed real analytic, function in local quotient/slice coordinates and is gauge invariant on the saturated neighborhood.

The local ordinary maps and contour variables have compatible smooth equivariant extensions to this orbit tube. One can either use their actual endpoint-covariant formulas on the saturated relative-log domain, or define the extensions by equivariance from the slice. Consistency on overlaps follows from (2.2) and the actual local formulas. The measurable completions outside this tube play no role.

The known physical branch is a strict local constrained minimum modulo the based gauge orbit. Adding G_K produces the already proved strictly positive retained Hessian. On the slice P_K=I, the penalty is identically zero; the positivity therefore also gives positivity of the action Hessian on the quotient constrained tangent. The fixed finite-dimensional analytic implicit-function argument makes the quotient critical orbit unique in a smaller neighborhood.

Choose a real target germ W near I with compact closure inside that neighborhood. The stationary orbits for W in this closure form a compact set. Shrink neighborhoods and choose a smooth H_(RL)-invariant cutoff chi equal to one near these orbits and supported in a tube in which the quotient saddle is unique and its transverse Hessian is positive. The same can be arranged simultaneously for the inner conditional minima and outer minima below. One way is to choose neighborhoods successively using continuity of the conditional minimum maps, then average a smooth cutoff over the compact H_(RL) action. The averaging leaves it one on the invariant smaller neighborhood.

This cutoff is an auxiliary tool for identifying a leading coefficient. It is not asserted to be the actual sharp retained window or to define the whole Wilson pushforward.

## 4. Exact local pushforward composition

On this common tube, define the finite positive density

    chi(U) exp[-S_ext(U)/g^2] dmu_X(U),       g>0.

The maps f, h and h o f are submersions near the relevant orbits. At a small representative this follows from the actual invertible pivot blocks; equivariance transports the rank to the entire orbit, and a smaller tube retains it. Their pushforwards therefore have smooth local densities relative to the corresponding PRODUCT HAAR measures.

Let J_g(V) be the density obtained by pushing this measure through f, and let I_g(W) be its pushforward through h o f. Exact pushforward composition gives

    I_g(W)=integral_(h(V)=W) J_g(V) dmu_h(V).           (4.1)

Here dmu_h is the conditional coarea density relative to product Haar. Equivalently the identity is obtained by testing against a smooth function of W and applying Fubini, so no informal multiplication of delta distributions is required.

Because chi and S_ext are H_(RL)-invariant, J_g is H_L-invariant: lift an intermediate based gauge by the embedded group in (2.1), use (2.2), and change the current Haar variables. This is exact. Normalized Haar disintegration introduces no extra background function.

In a neighborhood of the outer stationary orbit, the inner fiber has the actual local minimum action S_(MR)(V). Its conditional minimizing configuration depends smoothly on V modulo H_R. The finite two-minimum comparison gives the outer phase

    min_(h(V)=W) S_(MR)(V)=S_(MRL)(W).                 (4.2)

The same comparison identifies the direct phase on h o f. The auxiliary cutoff can be chosen one near every conditional minimum in a smaller compact outer neighborhood. It changes neither leading stationary amplitude. Points outside that neighborhood have a fixed positive quotient-action gap after shrinking the total support, so their contributions are exponentially smaller. All statements in this paragraph are at the fixed finite regulator and fixed ratios.

## 5. The elementary parameter-dependent Laplace fact

We record the only asymptotic result needed. In a finite real chart, suppose

    F(z,w)=s(w)+(1/2)z^T A(w)z+O(|z|^3),

with a unique local minimum at z=0, A(w)>0, and a smooth compactly supported density m(z,w) whose cutoff equals one near zero. On a sufficiently small compact parameter set, assume a common positive lower bound for A and no other critical point on the support. Then

    integral exp[-F(z,w)/g^2]m(z,w) dz
      =exp[-s(w)/g^2]g^n(2pi)^(n/2)
                      m(0,w)det A(w)^(-1/2)[1+o(1)],   (5.1)

uniformly in that parameter set.

Proof: shrink the chart until F-s>=c|z|^2. On z=g xi the integrand divided by its displayed prefactor converges on every bounded xi set to the corresponding Gaussian density, uniformly in w. A fixed Gaussian majorant controls the rest inside the chart. The compact part outside a smaller chart has a positive phase gap and is exponentially negligible. First truncate xi, take the uniform limit there, and then remove the truncation. This proves (5.1) without any uniformity in ultraviolet depth, volume or the ratios.

The same proof allows a smooth positive amplitude a(z,w), multiplying the leading expression by a(0,w). It also permits an amplitude a_g converging to a uniformly near the saddle: its bounded relative error is carried through the Gaussian domination.

For a constrained orbit integral, insert the exact gauge identity (2.3) and use the actual retained chart. The gauge-zero representative is the unique isolated saddle of S+G_K in that chart. The flat-independent factor c(g)^(-n_s,K) is retained. Equation (5.1) then applies directly to the gauge-fixed finite coordinates. This is an elementary way to obtain the quotient stationary amplitude without choosing an unspecified quotient volume form.

## 6. Identification of that amplitude with the actual D

For ratio K, the exact local constrained density from the composite integral module has, at its saddle, the measure factor

    h_0^(n_e-n_c) d_K(V_*),

and the phase Hessian A_(M,K)(W). Indeed normalized Haar in relative link coordinates is h_0 j(B)dB with j(0)=1; the straightening Jacobian is one at the linear origin; solving the constraint contributes the inverse pivot product d_K(V_*). The density is relative to target GROUP HAAR, so no extra background factor j(log W) is inserted.

The normalized stationary amplitude of the orbit-tube pushforward is therefore

    exp D_(M,K)(W)
       =lim_(g->0)
          exp[(S_(MK)(W)-S_(MK)(1))/g^2]
                         I_(M,K;g)(W)/I_(M,K;g)(1).    (6.1)

The gauge normalization c(g), the powers of g, Haar constants, flat determinants and all auxiliary-cutoff constants cancel in this ratio. Formula (1.2) is exactly the remaining saddle measure/determinant ratio. A cutoff equal to one near the orbit does not change it.

The same D is the leading coefficient of the ACTUAL sharp-window small-field integral. That integral uses the identical saddle, pivot factor and A, but its retained variable is z=g xi and its product window is |xi_b|<=T(g). Take T(g)->infinity with g T(g)^3->0, as in the established centered-parity bounds. Its normalized Gaussian expectation tends to one; equivalently its logarithm is O(tau(T)+g^2 T^6). Thus it has the same normalized leading amplitude (6.1). This is a leading-coefficient identification, not equality of the orbit-tube and sharp-window integrals.

The intrinsic invariance supplied by this auxiliary integral is exactly the intermediate based H_L invariance: its input cutoff and extended phase were made H_(RL)-invariant, so Section4 proves H_L invariance of J_g and its effective phase. The normalized leading amplitude and its positive real logarithm D_(M,R) therefore have this identity on the needed intermediate orbit, with the extension defined by the same saturation argument. This is sufficient to replace the outer rooted saddle by its pre-gauge representative. The auxiliary cutoff has not been made invariant under all output site gauges with nontrivial final-center values; the full local output gauge identity for the actual D is instead the one previously proved from the zero-input quantum leading limit. No stronger invariance of this auxiliary tube is required.

## 7. Sequential Laplace and the cocycle

Apply (5.1) first on the f fibers, uniformly for V in a small compact neighborhood of the outer stationary orbit. With an unimportant scalar prefactor c_1(g),

    J_g(V)=c_1(g) exp[-S_(MR)(V)/g^2]
                      exp[D_(M,R)(V)] [1+o(1)].        (7.1)

The error is uniform there. For a neighborhood of the full compact H_L orbit, use its exact invariance to reduce to one small slice. The inner cutoff is one at the conditional minima.

Insert (7.1) into the exact identity (4.1). The outer Laplace formula with smooth amplitude exp[D_(M,R)(V)] evaluates that amplitude at the outer minimum, and gives another scalar c_2(g):

    I_g(W)=c_1(g)c_2(g) exp[-S_(MRL)(W)/g^2]
       exp[D_(M,R)(V_p^(MR,L)(W))+D_(MR,L)(W)]
                                                  [1+o(1)].    (7.2)

The outer gauge-zero representative could be used instead of V_p; invariance of D makes their values equal. The amplitude does not shift the leading phase saddle: its gradient has no g^-2 factor, and the Laplace theorem evaluates it at the existing classical saddle.

Applying (6.1) directly to h o f instead gives

    I_g(W)=c_12(g) exp[-S_(MRL)(W)/g^2]
                         exp[D_(M,RL)(W)] [1+o(1)].    (7.3)

Normalize (7.2) and (7.3) by their values at W=I after removing the phase. At the identity V_p=I and every displayed D is zero, so all scalar prefactors cancel without computing any relation between them. Taking g to zero yields

    exp[D_(M,RL)(W)]
       =exp[D_(M,R)(V_p^(MR,L)(W))+D_(MR,L)(W)].

The logs are real and zero at the identity on the positive real germ. Thus there is no logarithmic branch ambiguity, and

    D_(M,RL)=T_(MR,L)D_(M,R)+D_(MR,L).                 (7.4)

Each side is an actual holomorphic determinant/pivot functional on its given common local product domain. Equality on the real germ extends to the connected common domain by the identity theorem. The finite Laplace proof may use a smaller germ depending on the regulator and ratios; this does not shrink the already established analytic domain of either side.

## 8. Infinite-system and Maxwell consequences

For fixed R,L, the determinant/pivot modules provide uniform anchored analytic families for all three D's. On a jointly extracted system, the finite identity (7.4) therefore passes on compact fields by normal convergence and anchored tail control, as do the classical substitutions. The result is a scalar quotient cocycle; no coefficientwise identity of carrier decompositions is asserted.

Applying the independently proved true infinite marginal preservation gives

    beta_(MRL)(D_(M,RL))
       =beta_(MR)(D_(M,R))+beta_(MRL)(D_(MR,L)).         (8.1)

Consequently a long fixed-ratio determinant coefficient is the sum of its consecutive single-step coefficients in this system. This exact additivity does not compute those coefficients, prove positivity, or imply their convergence with preceding depth.

For finite cutoff beta_(M,N), one cannot simply drop the T from (7.4): only the finite reference telescope and the separately established asymptotically small finite classical leakage are available. No exact finite scalar beta additivity is claimed here.

## 9. Scope and audit boundary

The substantive bridge is the consistent local orbit-tube extension in Section3, based on actual local gauge invariance and the O(RL) path from every site to a based center. The remaining composition is exact finite Haar pushforward/Fubini followed by ordinary finite-dimensional saddle asymptotics. The actual pivot, contour penalty and retained Hessian are used in the leading amplitude identification.

The result does not assert equality of any direct and sequential noninvariant cutoff sectors at positive g. It does not import a global measurable action outside the constructed tube, identify the local step with every Wilson history, or assume a ultraviolet-uniform stationary-phase error. The auxiliary cutoff is used only to compare leading coefficients and disappears from them.

The full ghost/background-field determinant comparison, its bounded error in depth, the numerical logarithmic coefficient, its sign, physical coupling tuning, all other field sectors and continuum construction remain separate. None of these asserted source-outline steps is imported into the present cocycle proof.
