# Independent audit: an exponentially local flat Maxwell minimizing lift

16 October 2026. Independent derivation and audit of `flat_minimizer_locality_research.md`, initially Sections 1--9. The original alias formula and central cancellation are correct. The estimates below prove volume-normalized operator locality and uniform pointwise/Hölder locality for the field and its fine curl. Sections 8--11 additionally audit the source-compatible gauge repair: it has stronger full first-derivative bounds and matches the deposited homogeneous flat scalar projection and bond average. This does not extend the result to nonflat backgrounds or arbitrary retained histories.

## 1. Notation and the added scalar denominator

Use the alias notation of `flat_covariance_decay_audit.md`: p_r=z+2pi r, u_r^+=M(exp(i p_r/M)-1), P_r=sum u_r^+u_r^-, a_r=a_M(p_r), omega_r,mu=a_r ell_r,mu, and analytic minus evaluation a_r^-=a_M(-p_r). Let q(z) be the already audited Maxwell precision and h=diag(D_mu^(-1)). In particular

    q=P_0 h-(h d^+)(d^- h)/E,
    d^- h d^+=P_0 E,
    Q_r u_r^+=a_r d^+.

Introduce the scalar blocked Feynman covariance and its canceled denominator:

    W_s=sum_r a_r a_r^-/P_r=A/P_0+R_s,
    A=a_0 a_0^-,
    R_s=sum_(r!=0) a_r a_r^-/P_r,
    D_s=A+P_0 R_s.

The scalar high-alias sum is holomorphic and uniformly bounded on the same initial tube as the vector high-alias sums: scalar alias Parseval is even stronger. On the real enlarged cube, R_s>=0 and D_s>=A>=c_0^(2d)>0. The existing Cauchy shrinking argument, applied once more if needed, makes D_s and its inverse holomorphic and uniformly bounded in a common smaller tube. A already has a uniform positive modulus there, and a_0 is uniformly bounded, so a_0^(-1) is uniformly bounded too. No new scale-dependent domain is needed.

## 2. Feasibility and exact minimal energy

For real nonzero coarse momentum define

    v=(d^-h)/(P_0 E),
    t_r=P_0 a_r^-/(P_r D_s),
    H_r=P_r^(-1) diag(omega_r,mu^-) q + u_r^+ t_r v.

The first term is the minimizing Feynman field for the projected datum. Its coarse average is

    W q=I-d^+ v.

The scalar weights satisfy sum_r a_r t_r=1. The coarse average of the gradient term is therefore d^+v, giving the exact constraint

    sum_r Q_r H_r=I.

The first term is fine-transverse because

    u_r^- P_r^(-1) diag(omega_r,mu^-)q
       =(a_r^-/P_r)d^-q=0.

Its energy is the Maxwell minimum q, and the added gradient changes neither curl nor energy. Thus the field H B is an exact Maxwell minimizer with the prescribed coarse datum, not merely a bounded competitor.

There is also a useful real-momentum characterization. The transverse part of any minimizing field is uniquely determined. The remaining fine scalar gauges must have weighted block average vB. Minimizing their fine field norm is minimizing sum_r P_r|lambda_r|^2 with that constraint; its solution is lambda_r=t_r vB. Orthogonality of fine transverse and gradient fields then shows that H is the least fine-L2-norm field among the Maxwell minimizers. This characterization is not needed for the analytic estimates.

At coarse momentum zero, define H_0(0)=I and H_r(0)=0 for r!=0. The fine field is constant and realizes any constant coarse field with zero curl energy. The analytic formulas below have exactly these values.

## 3. Central pole cancellation

For the central alias, the identity omega_0,mu u_0,mu^+=a_0 d_mu^+ gives

    omega_0,mu^- h_mu d_mu^+
       =(u_0,mu^+/a_0) g_mu h_mu
       =(u_0,mu^+/a_0)(1-P_0 R_mu h_mu).

Also A/D_s=1-P_0 R_s/D_s. Substitution into H_0 cancels every P_0 denominator and gives, componentwise,

    (H_0)_(mu nu)
       =omega_0,mu^- h_mu delta_(mu nu)
        +(u_0,mu^+/a_0)
          [R_mu h_mu-R_s/D_s]
          (d_nu^- h_nu)/E.

This is the proposed formula. It is uniformly bounded and holomorphic on the common tube, including the entire complex null set P_0=0. It gives I at zero because the correction carries u_0 and d^- and the first term equals I there.

For a high alias the original expression can be written without P_0 in any denominator as

    H_r=P_r^(-1) diag(omega_r^-)q
         +[u_r^+ a_r^-/(P_r D_s)] (d^-h)/E.

Its denominators are all uniformly nonzero. The only apparently growing numerator, u_r^+, is controlled relative to the high-alias denominator as described next.

## 4. Uniform alias estimates, including fine curl

Fix a complex strip whose real cube satisfies |Re z_mu|<=K<2pi, with K>pi. For r!=0 in the centered alias window, real principal fine momenta satisfy

    P_r(Re z)>=c_K |r|^2.

Indeed, in a nonzero coordinate the distance of Re z_mu+2pi r_mu from 2pi M Z is at least (2pi-K)|r_mu|. The sine lower bound gives the assertion after summing coordinates. A fixed sufficiently small imaginary strip changes Re P_r by only a uniform constant, so

    |P_r(z)|>=c(1+|r|)^2,
    |u_r^+(z)|<=C(1+|r|),       r!=0.

For r_mu!=0 the sine formula for the centered block factor has bounded numerator and denominator bounded below by a constant times |r_mu|. Its r_mu=0 factor is bounded by the already controlled central multiplier. Consequently, with

    w(r)=prod_mu (1+|r_mu|)^(-1),

one has

    |a_r(z)|<=C w(r),
    |omega_r,mu(z)|<=C w(r)/(1+|r_mu|).

The longitudinal phase has bounded modulus on the fixed strip and causes no scale loss. Constants may depend on dimension and strip but not on M.

Applying these bounds to the high-alias formula gives

    ||H_r(z)||<=C w(r)/(1+|r|),       r!=0.

For the fine curl, the scalar gradient term drops out algebraically:

    G_r:=u_r^+ wedge H_r
       =P_r^(-1) u_r^+ wedge[diag(omega_r^-)q].

The same bounds give

    ||G_r(z)||<=C w(r)/(1+|r|),       r!=0.

For the central alias, use its canceled formula and the uniform bound on u_0 to bound H_0 and G_0. This proves uniform square sums and, more strongly, the summability below. The corresponding estimate for a full fine gradient of H would lose the extra inverse power of 1+|r| in its gauge component; the present argument does not claim uniform absolute summability at that endpoint.

For the max-norm shell 2^j<=|r|_infinity<2^(j+1), at least one coordinate has size comparable to 2^j. Summing its factor (1+|r_mu|)^(-1) over that interval is bounded independently of j. Summing the other factors over |r_nu|<=2^(j+1) gives at most C(j+1) per coordinate. Taking the union over choices of the large coordinate proves

    sum_(shell j) w(r)<=C_d (j+1)^(d-1).

It follows that for every 0<=alpha<1,

    sum_r (1+|r|)^alpha [||H_r(z)||+||G_r(z)||]
       <=C_(d,alpha),

uniformly in M and on a common smaller strip. This result is stronger than an estimate obtained by merely counting aliases.

## 5. Fine-cell reconstruction and periodic gluing

Write a fine site as x=n+s/M, where n is a coarse block label and s belongs to the centered integer block. The fine-cell symbol of the lift is

    F_s(z)=sum_r exp(i(z+2pi r).s/M) H_r(z).

Define the fine-curl cell symbol by replacing H_r with G_r. The absolute alias sums above bound both symbols uniformly pointwise in s, M and z. Alternatively, discrete Fourier Parseval in s gives directly the correctly normalized operator identity/bound

    M^(-d) sum_s ||F_s(z) B||^2
       <=exp(sum_mu |Im z_mu|) sum_r ||H_r(z)B||^2.

Thus the growing fine-cell dimension introduces no M^(d/2) factor in the physical volume norm. The same estimate holds for the fine-curl symbol.

The individual alias matrices are not themselves coarse-periodic. Before cancellation, however, the full Feynman covariance, scalar covariance, coarse derivative and quotient are periodic under z->z+2pi e_mu, with the aliases permuted modulo M. Thus H_r transforms by that permutation. In the reconstruction, a wrapped alias changes the phase by exp(2pi i M ell.s/M)=1 because s is an integer vector. The fine-cell symbols consequently agree on real overlaps of adjacent momentum charts. Their holomorphic extensions agree there by the several-variable identity theorem and glue to periodic bounded holomorphic symbols on the common tube.

This integer-coordinate phase is essential. Claiming periodicity separately for the central alias or omitting the internal fine-site phase would be incorrect. Fine curl has the same phase rule. Its finite differences that cross a coarse-cell boundary acquire the corresponding coarse Bloch factor, exactly as encoded by u_r^+.

Fourier contour shifts now give exponentially decaying kernels in the coarse output-input block displacement, both in pointwise fine-site norm and as operators into the physically weighted fine-cell Hilbert space. No growing output dimension appears in the constants. Periodic finite-volume kernels are obtained by periodization, with absolutely convergent image sums and uniform bounds even for short periods.

## 6. Physical Hölder regularity and operator/energy bounds

The weighted alias sums give the same localization after a physical output-site difference. For two fine sites x,y with |x-y|<=1, rewrite their Fourier phases using the same initial coarse cell. Any crossing of a coarse-cell wall contributes an integer coarse Bloch factor, which cancels the alias factor exp(-2pi i r.ell). Therefore the phase difference is exactly multiplication by

    exp(i(z+2pi r).(y-x))-1.

On the fixed strip its modulus is at most

    C_alpha (1+|r|)^alpha |x-y|^alpha,

for every alpha<1. Combining with Section 4 and shifting the common Fourier contour yields, for the lift kernel K_M and its fine curl J_M,

    |K_M(x,j)|+|J_M(x,j)|<=C exp(-c dist(x,j)),
    |K_M(y,j)-K_M(x,j)|+|J_M(y,j)-J_M(x,j)|
       <=C_alpha |x-y|^alpha exp(-c dist(x,j)),

after harmless changes of c,C to compare physical point-to-block distance with integer block distance. These statements are on the discrete fine lattice. The local difference estimate is uniform across cell boundaries. For finite tori use close periodic lifts of x,y and periodize the kernel estimates.

The pointwise exponential kernel has uniformly bounded row sums over coarse sources and uniformly bounded column sums with physical fine measure M^(-d). For the latter, the number M^d of fine sites in each coarse cell cancels its measure M^(-d). Weighted Schur therefore gives uniform coarse-L2 to fine-L2 bounds for H and its fine curl, as well as uniform coarse-l_infinity to fine-l_infinity/Hölder bounds. Fractional exponential weights can be included by spending part of the kernel exponent.

For real data the exact energy identity is

    ||d_eta H B||_eta^2=<B,q_M B>.

The previously proved compact Maxwell lift consequently gives the explicit bound

    ||d_eta H B||_eta^2<=2^(d+6)(d-1)||B||_1^2,

with its separately handled M=1 case. This uses exact minimization and is stronger evidence than merely bounding the analytic formula by an unspecified constant. The pointwise or Hölder estimates do not amount to a uniform full-gradient estimate, and they do not identify this gauge-selected minimizer with a different gauge convention without an additional comparison.

## 7. Written-note comparison and scope

The author's saved original note, Sections 1--9, was read in full. Its scalar right inverse, central and high-alias formulas, exact least-norm characterization, divergence identity, Hilbert and absolute alias sums, physical cell norms, collar Hölder bounds, fine-cell periodic gluing and Fourier localization agree with the independent derivation above. No substantive correction was found. Its additional full-gradient alias L2 observation is also valid: the bound |u_r H_r|<=C w(r) has a uniformly square-summable right side. That assertion is carefully distinguished from a full-gradient pointwise estimate.

The precise model conclusion is an exponentially local, uniformly volume-bounded minimizing right inverse for the homogeneous full-block straight-average Maxwell problem, together with matching locality for its fine curl. The construction gives a particular gauge selection, in fact the real least-norm one. It does not prove that an arbitrary retained-history or nonlinear gauge-fixed source branch differentiates to this selection, nor does it supply the complex-background perturbation theorem required later in the Yang--Mills argument.

## 8. The source scalar projection is a different gauge

The definitions independently checked in the deposit are recorded in `flat_minimizer_source_gauge_research.md`. In raw I, lines 23909--23918 give the transported scalar block average, which becomes Q_0 at flatness. Lines 23937--23944 give

    G'=(Delta+Q_0^* a' Q_0)^(-1),
    P=G'Q_0^*(Q_0 G'^2 Q_0^*)^(-1)Q_0G',
    R=I-P.

On the real finite regulator, P is the orthogonal projection onto ran(G'Q_0^*). Since G' is positive and invertible,

    ran R=ker(Q_0G')=Delta ker Q_0.

On a nonzero homogeneous Bloch fiber, Delta is invertible, and the resolvent identity shows

    ran(G'Q_0^*)=ran(Delta^(-1)Q_0^*).

The two gauges must therefore be distinguished:

* Original least-field-norm lift: D_f^*H lies in ran Q_0^*.
* Source gauge: D_f^*H_src lies in ran(Delta^(-1)Q_0^*) on nonzero fibers, or intrinsically R D_f^*H_src=0.

They differ generically. For a pure coarse gradient at a nonzero momentum with two nonzero scalar aliases of unequal P_r, the original scalar weights are proportional to a_r^-/P_r, whereas the source-compatible weights below are proportional to a_r^-/P_r^2. The former divergence has aliases proportional to a_r^- and cannot belong to the line with components a_r^-/P_r when those P_r differ. For example M=3 and a coarse momentum (pi/2,0,...,0) have such aliases. Thus equality of the two lifts is not presumed.

## 9. Exact source-compatible repair and central cancellation

Define

    W_2=sum_r a_r a_r^-/P_r^2=A/P_0^2+R_s2,
    R_s2=sum_(r!=0) a_r a_r^-/P_r^2,
    D_s2=A+P_0^2 R_s2,
    t_2,r=P_0^2 a_r^-/(P_r^2 D_s2).

For r=0 the last expression means t_2,0=a_0^-/D_s2. The high-alias denominator is uniformly bounded away from zero, and scalar Parseval bounds R_s2 uniformly. On the real enlarged cube D_s2>=A>0. Another uniform Cauchy shrinking therefore gives a bounded holomorphic inverse of D_s2. As before,

    sum_r a_r t_2,r=1.

Keep the same transverse Feynman minimizer F_r=P_r^(-1)diag(omega_r^-)q and the same row theta=(d^-h)/(P_0 E). Define

    H_src,r=F_r+u_r^+ t_2,r theta.

It is feasible and has the same minimal curl energy as the original lift. Its central alias cancels exactly to

    (H_src,0)_(mu nu)
       =omega_0,mu^- h_mu delta_(mu nu)
        +(u_0,mu^+/a_0)
           [R_mu h_mu-P_0 R_s2/D_s2]
           (d_nu^-h_nu)/E.

The cancellation uses A/D_s2=1-P_0^2 R_s2/D_s2. Every sign and power of P_0 in this formula is necessary. For r!=0 the safe high-alias formula is

    H_src,r=P_r^(-1)diag(omega_r^-)q
          +[u_r^+ P_0 a_r^-/(P_r^2 D_s2)](d^-h)/E.

Both expressions are holomorphic on the common strip and have the same zero-mode values I and 0 as before.

The divergence is

    (D_f^*H_src)_r
       =(a_r^-/P_r)[P_0(d^-h)/(D_s2 E)].

On nonzero real fibers this is exactly in ran(Delta^(-1)Q_0^*), so it satisfies the source gauge. Its central apparent quotient cancels to a_0^-(d^-h)/(D_s2 E); at zero all divergence components vanish. Thus the scalar zero mode is handled without using an undefined inverse of Delta there. The original penalized G' definition remains the appropriate intrinsic definition of R at zero.

The real t_2 weights minimize sum_r P_r^2|lambda_r|^2 with prescribed scalar block average. Thus H_src minimizes the L2 norm of its divergence among Maxwell-energy minimizers. This is distinct from minimizing the fine potential L2 norm, which selected the original t_r weights.

## 10. Stronger regularity of the source lift

Apply Section 4's alias estimates to the high source formula. Its first term is at most C w(r)/(1+|r|)^2. Its gradient term is at most C w(r)/(1+|r|)^3. Therefore

    ||H_src,r||<=C w(r)/(1+|r|)^2,
    ||u_r,nu^+ H_src,r||<=C w(r)/(1+|r|),
    ||u_r^+ wedge H_src,r||<=C w(r)/(1+|r|).

The bounds hold on the fixed complex strip. The central terms and their derivatives are separately uniformly bounded. Shell summation gives, for every alpha<1,

    sum_r (1+|r|)^alpha
       [||H_src,r||+sum_nu||u_r,nu^+H_src,r||
                         +||u_r^+ wedge H_src,r||]<=C_alpha.

Equivalently one can put the stronger weight (1+|r|)^(1+alpha) on H_src itself. Fine-cell reconstruction, periodic gluing, collar estimates and Fourier contour shifts proceed exactly as in Sections 5--6. They give uniform exponentially localized discrete C^(1,alpha) potential kernels and C^alpha curl kernels, where discrete C^(1,alpha) includes the physical forward differences M[f(x+e_nu/M)-f(x)]. These derivative bounds include every fine first derivative, unlike the original least-field-norm lift's pointwise conclusion.

Volume-normalized L2 bounds follow either from alias Parseval or from weighted Schur. The exact curl-energy identity is unchanged and retains the explicit compact-lift upper constant. Compatible finite-volume kernels are exact periodizations with uniform bounds in periodic physical distance.

## 11. Uniqueness and the homogeneous source identification

On a compatible finite torus, suppose two exact Maxwell minimizers have the same coarse field and both satisfy the source gauge. Their difference has zero curl. The finite lattice Hodge decomposition writes that difference as a fine gradient plus a constant harmonic one-form. Averaging its zero coarse constraint around each coarse cycle forces the harmonic one-form to vanish. For the remaining D_f phi, the constraint says d_c Q_0 phi=0. The coarse torus is connected, so Q_0 phi is constant; subtract a fine scalar constant to arrange Q_0 phi=0 without changing D_f phi.

Now Delta phi belongs to Delta ker Q_0=ran R, while the difference of the two source-gauge conditions says R Delta phi=0. Orthogonal projection onto ran R acts as the identity on Delta phi, so Delta phi=0. Positivity of the scalar Laplacian gives D_f phi=0. This proves uniqueness, including short periodic directions with their incidence multiplicities. The scalar zero mode causes no ambiguity in the bond field. An infinite-volume L2 uniqueness statement follows fiberwise almost everywhere.

The bond operator was also checked in the deposit: raw I 24349--24373 reproduces the corrected double-bar average linearization attributed to CMP98 (122)--(125). At the flat background its bracket corrections vanish and the surviving term is the normalized straight-string average Q_st,L. Raw I 47046--47048 states that the higher Q_j are compositions of these one-step operators. The full-block flat semigroup therefore gives Q_j=Q_st,L^j. This is the source bond Q used with the scalar Q_0; it must not be confused with the later contour-rooted Q^flat used for pivot elimination.

Consequently the constructed H_src has the same homogeneous flat bond constraint and scalar gauge as the normalized source map H_0 ell. With the source map's recorded minimizing and gauge properties, uniqueness identifies the two. The exact source formulas here are verified deposited transcriptions; this note does not claim an independent recovery of every original CMP99b/CMP98 proof. This identification remains restricted to the homogeneous flat full-block geometry and the stated physical normalization. It does not supply nonflat independent-current response estimates or a mixed-history boundary theorem.

## 12. Additional componentwise Laplacian bound

The source repair also has a uniform pointwise bound for its componentwise fine scalar Laplacian, although the crude absolute alias estimate for two individual derivatives does not prove one. Multiply the source formula by P_r:

    P_r H_src,r=diag(omega_r^-)q+Z_r,
    Z_r=[u_r^+ P_0 a_r^-/(P_r D_s2)](d^-h)/E.

The first term reconstructs exactly as Q_M^* q_M, with the physical-volume adjoint. The central part of the second term cancels to

    Z_0=[u_0^+ a_0^-/D_s2](d^-h)/E.

Its high aliases obey ||Z_r||<=C w(r)/(1+|r|). The already proved shell sum, fine reconstruction and contour shift therefore give uniform C^alpha exponential locality of Z for every alpha<1.

The adjoint Q_M^* is better handled by its real-space coefficients. In a fixed component and fine row, the transverse coordinates fix one coarse transverse block. The longitudinal weights are

    k_M(s-Mj)/M,   k_M(t)=(M-|t-h|)_+.

They are nonnegative and sum to one, because

    sum_j k_M(s-Mj)=M.

To prove the count directly, for each longitudinal string index t in {0,...,M-1}, exactly one translate of the centered M-site block contains the remaining coordinate s-t. Summing these M contributions gives the identity. Only two adjacent coarse bond rows can contribute. The same identity survives periodic identifications with multiplicity.

Consequently Q_M^* is a contraction from coarse l_infinity to fine l_infinity, with fixed physical range independent of M. Applying it to the exponentially local q_M kernel gives a uniform pointwise exponential bound on Q_M^* q_M. Its fine-volume column sums and physical L2 norm are uniformly bounded as well. Therefore

    Delta_f H_src=Q_M^* q_M+Z

has a uniform fine-l_infinity exponentially local kernel, together with a uniform physical L2 operator bound.

This decomposition does not make the entire Laplacian C^alpha uniformly: Q_M^* is blockwise constant in transverse directions and can produce jumps across block boundaries. It also does not prove pointwise bounds on each individual second fine derivative. The new conclusion is specifically the componentwise Laplacian supremum/locality bound, obtained by retaining the exact adjoint structure of its otherwise poorly summable alias term.

## 13. Candidate transcription audit

Read the complete initial `work/ym4-flat-minimizer-candidate.tex`. Its proof structure and mathematical scope agree with this audit, including source gauge uniqueness, physical fine norms, periodic gluing and the homogeneous source normalization. Two display transcription issues were reported to the author and root: the central correction must be a column times the scalar S/E, not a diagonal matrix times that scalar; and the divergence display required a missing backslash in its spacing command. The conditional first-variation identity also required an explicit real self-adjoint quadratic-family assumption, or both left and right stationarity.

The final corrected candidate was then checked. Its central expression is now correctly componentwise; the divergence spacing command is corrected; the first-variation hypothesis is explicitly real and self-adjoint. The added componentwise Laplacian subsection and theorem term agree with Section 12 above. In its explicit physical adjoint formula, for s_mu in [-h,h],

    beta_s=(s_mu+h+1)/M,
    (Q_M^*B)_mu(n+s/M)
       =beta_s B_mu(n)+(1-beta_s)B_mu(n-e_mu).

This orientation and coefficient are correct: the current row has string multiplicity h+1+s_mu, while the preceding row has multiplicity h-s_mu. They add to M. The corresponding Bloch multiplier beta_s+(1-beta_s)exp(-i z_mu) is correct and uniformly bounded. The final source-gauge, regularity, Laplacian and first-variation statements are mathematically ready for promotion within their explicitly stated homogeneous flat scope. No remaining mathematical or transcription correction was identified in this audit.
