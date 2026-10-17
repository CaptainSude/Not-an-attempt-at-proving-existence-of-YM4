# Exact finite local quantum induction with equivalent small representatives

17 October 2026. Research proof for independent audit. This combines the actual common-domain finite macro integral, finite-total quotient descent, the uniform zero-input force, and the finite classical contraction. The result concerns the selected homogeneous LOCAL macrostep and its specified analytic continuation. It is not an identification of the full Wilson pushforward, its other field sectors, or arbitrary mixed histories.

## 1. Fixed finite geometry and the induction problem

Fix the primitive ratio ell, one elementary composite ratio R=ell^s, auxiliary grouping J, and carrier exponent a0=1/16 satisfying the strict common-domain budgets. Each stage has current spacing one after relabeling. Let

    M_j=M_0 R^j,       Q_j=Q_0/R^j.                    (1.1)

M_j is the preceding homogeneous classical depth, and Q_j is the current-unit cubic torus period. Work only with compatible integer periods, with J dividing every Q_j used. The next step has output period Q_(j+1). All constants below are uniform in M_j and in these periods above a fixed lower threshold.

For period Q, let A_(Q;a0,b) be the finite connected J-cell activity space with

    ||E||_(Q;a0,b)=sup_i sum_(H contains i)
                           exp(a0|H|)||E_H||_b.         (1.2)

The functions are bounded holomorphic on the scalar-coordinate product ball b. The raw total and its normalized version are

    E_raw(A)=sum_H E_H(A|H),
    Phi_E(A)=E_raw(A)-E_raw(0).                         (1.3)

There are finitely many coordinates and carriers at every regulator. Quotient by equality of Phi_E on the full b polydisc and denote the finite norm by ||[E]||_(Q). The kernel is closed, since all finite normalized evaluations are continuous. The quotient is Banach. Its invariant subspace means total local gauge, translation, hypercubic and global color invariance; individual carrier coefficients need not be invariant. Use a simple Lie algebra for the scalar beta notation, or a finite componentwise version for a semisimple product.

The ordinary reference S_(M,Q) is the ACTUAL finite homogeneous minimum action, normalized by S_(M,Q)(0)=0. It is not replaced by the periodization of an independently chosen infinite reference. The common-domain theorem constructs, for admissible input E,

    F_j(E)=T_j E+G_j(E),
    G_j(E)=Delta_j+Qdet_j+L_j(Q_E),                    (1.4)

as a normalized class and as an actual raw finite coefficient family with separately tracked vacuum convention. T_j is the pre-gauge background substitution, Q_E is the exact inherited fluctuation difference, and L_j is the strict Gaussian logarithm with the actual fixed base exponent, precision and retained window. The coupling g_j and threshold T_cut,j are held fixed when comparing inputs to this one map.

At real data in the original common overlap, (1.4) is the exact chosen local macro integral. On the common b ball it is its proved holomorphic continuation, evaluated through the pre-gauge fields inside the old activity domain. Pointwise identification with a globally defined gauge-orbit density requires the additional orbit-representation hypothesis of the common-domain theorem. That hypothesis is not inferred from a finite quotient identity.

## 2. Exact descent of the finite quantum map

**Lemma 2.1.** The actual finite map F_j descends to the invariant finite quotient on its admissible ball. The same is true of T_j and G_j. No infinite periodization, limiting kernel, translation averaging, or choice of an infinite representative is needed.

**Proof.** If [E]=[E'], then on the whole input product ball

    E_raw(A)-E'_raw(A)=c,
    c=E_raw(0)-E'_raw(0).                              (2.1)

The actual pre-gauge field a_p(w) and all the inherited fluctuation fields f_lambda(w,xi) used by the strict construction lie inside that ball, uniformly on the fixed real retained window and on the proved interpolation domains. Consequently

    E_raw(f_1)-E_raw(f_0)
       =E'_raw(f_1)-E'_raw(f_0),                       (2.2)

while the exterior background terms differ by c. Thus the inherited scalar Gaussian insertion is identical, and the finite integrals differ only by the scalar e^c. The fixed base action, covariance, chart, window and all measure factors are unchanged. Their normalized holomorphic logarithms agree; compatibility also follows by continuation from the same nonvanishing near-origin branch. Any raw logarithm constant is part of the vacuum normalization and disappears from the class. Carrier arrays may differ.

Classical substitution has the same descent immediately because (2.1) is valid at a_p(w). Subtracting the two descended maps gives G_j. The exact real-sector symmetry argument and holomorphic Ward continuation preserve the stipulated total symmetries. This uses the actual finite construction, not a claim that each support coefficient is invariant. QED.

The constant in (2.1) is harmless for normalized classes but cannot be discarded from a raw density. Section7 gives its exact compensation. Real classes admit real representatives without increasing the norm: average E_H(w) with its conjugate-reflected coefficient overline(E_H(bar w)). This permits real positive density bookkeeping when the input is real.

## 3. Uniform finite quantum difference and forcing bounds

Let epsilon_bar be a family ceiling with the strict two-input Gaussian budgets. On the quotient ball of radius epsilon_bar/4, take near-minimal representatives Y of y and D of x-y and put X=Y+D. For arbitrarily small delta>0,

    ||Y||<=epsilon_bar/4+delta,
    ||D||<=||x-y||+delta<=epsilon_bar/2+delta,
    ||X||<=3epsilon_bar/4+2delta<epsilon_bar.           (3.1)

Both complete inputs are therefore admissible. Their totals have the required invariances because they represent invariant classes. No covariance of their coefficient arrays is required.

The finite Gaussian interpolation retains the full base exponent and the actual precision. Its strict budget is, in particular,

    v<=eta_*/(64e),
    a_Q epsilon_bar<=eta_*/(128e),
    a_Q=16 C_T C_R g_j T_cut,j/b.                       (3.2)

The inherited difference is linear in D. The finite Banach-valued logarithm Cauchy argument consequently gives

    ||G_j(x)-G_j(y)||_(Q_(j+1))
       <=C_quant(g_j T_cut,j/b)||x-y||_(Q_j),
    C_quant=1024e S1 C_T C_R.                          (3.3)

To justify the quotient inequality, apply the family bound to X,Y with their compatible linear inherited assignment, use Lemma2.1 to identify the resulting classes, and send delta to zero. No local-limit or Fatou argument is needed at a fixed regulator. The determinants cancel in the difference. No equal-low-jet hypothesis is used.

For the zero input, fix one classical outer radius rho after R,J with all strict Gaussian and support margins. Use the SAME threshold, charts, covariance and logarithm branch for the subsequent restriction to b. The actual finite zero-input family has norm at most H_* on rho, uniformly in M, period and weak g. Semisimple adjoint invariance makes its total first derivative zero. Removing coefficientwise homogeneous degrees zero and one and restricting to b<=rho/2 gives

    ||G_j(0)||_(Q_(j+1))<=C_F b^2,
    C_F=2H_*/rho^2.                                   (3.4)

This is the finite form of quantum_zero_input_force_research.md. It is an exact representative of the normalized total, not merely a low-jet approximation. The vacuum constant is kept separately. The full force need not be O(g^2); its pivot and Gaussian determinant pieces can persist at g=0.

## 4. Actual finite reference extraction and its classical block

At stage j define the finite Maxwell functional by the symmetric short-lift transverse Hessian coefficient divided by the corresponding coefficient of the ACTUAL S_(M_j,Q_j). The flat q_M periodization implies a uniformly nonzero denominator for Q_j>=Q_ref(J). The finite Ward theorem and the fixed-outer-radius reference representation give

    beta_j(S_j)=1,    ||beta_j||<=C_beta b^(-2),
    P_j=I-S_j beta_j, ||P_j||<=p=1+C_beta C_S,
    S_j=[S_(M_j,Q_j)], ||S_j||<=C_S b^2.               (4.1)

All constants are uniform in the indicated periods and M_j. The b^(-2) factor is retained, and it cancels only in the combined projection bound.

The exact two-minimum comparison gives, in dimension four,

    T_j S_j=S_(j+1),
    P_(j+1) T_j P_j=P_(j+1)T_j.                       (4.2)

It uses the identical fine plaquette action under physical relabeling, with eta^(d-4)=1, and the exact ordinary constraint composition. It does not follow merely from normalization of the Hessian. The actual finite background semigroup, modulo the controlled gauge comparison for invariant totals, gives for A_j=P_(j+1)T_j,

    A_(j+q-1)...A_j P_j
       =P_(j+q) T_(M_j,R^q,Q_(j+q)) P_j.              (4.3)

Here the direct map in the right side is a CLASSICAL substitution. No sequence of quantum windows is replaced by a one-shot window.

Put L=R^q. The finite classical contraction theorem, with its retained graded Ward defects and wrapping tails, bounds the right side by

    theta(q,N)
      =p^2[C_low(J)L^(-alpha)+6C_high/L
              +C_err(J)(L^2+L+1)e^(-c(J)LN)],
    N=Q_(j+q).                                        (4.4)

Every term has the same input/output field radius b and carrier weight a0. Fix J first, choose a finite q and then a compatible N0>=Q_ref so that

    theta(q,N)<=1/4 for all N>=N0.                     (4.5)

Increase N0 also for the fixed collar and period restrictions. Choose the final b only afterward, within all direct L and outer-domain requirements, including b<=min(1,rho/2). One-step transport has uniform bounds

    ||T_j||<=B_T,    ||A_j||<=B,
    B>=max(1,pB_T).                                    (4.6)

The exact finite projection telescope remains valid although both period and beta functional change with j. It requires no identity beta_(j+1) T_j=beta_j.

## 5. Finite block envelope, with all intermediate maps admissible

Define

    Psi_j(x)=P_(j+1)F_j(x)=A_j x+H_j(x),
    H_j=P_(j+1)G_j.                                   (5.1)

Let nu bound p C_quant g_j T_cut,j/b uniformly over the step data. From (3.3)-(3.4),

    Lip H_j<=nu,           ||H_j(0)||<=C_0 b^2,
    C_0=p C_F.                                         (5.2)

Choose

    K=B+1,
    L_q=sum_(l=0)^(q-1)K^l,
    K_amp=max(1,2 C_0 L_q),
    C_int=K^q K_amp+C_0 L_q.                           (5.3)

Decrease b so C_int b^2<epsilon_bar/4. Finally restrict the weak-coupling range so that all common-domain budgets, including (3.2), hold and

    nu<=min(1,1/[4q K^(q-1)]).                         (5.4)

This is possible with T_cut(g) a sufficiently large fixed multiple of sqrt(log(1/g)), with a fixed lower threshold. The outer force is already uniform on this subsequently smaller range.

For any block whose final period is at least N0, start with beta_j(x_j)=0 and

    ||x_j||<=r_b,       r_b=K_amp b^2.                 (5.5)

The elementary step bound gives, for 0<=k<=q,

    ||x_(j+k)||
       <=K^k K_amp b^2+C_0 b^2 sum_(l<k)K^l
       <=C_int b^2<epsilon_bar/4.                      (5.6)

This is an induction: it verifies the next map's domain before invoking that map. The same bound holds for a zero-started trajectory and for any second trajectory started in (5.5).

For two such trajectories using identical prescribed couplings and step data, variation of constants gives

    ||delta_q||
       <=[theta(q,Q_(j+q))+(B+nu)^q-B^q]||delta_0||
       <=[1/4+q nu K^(q-1)]||delta_0||
       <=(1/2)||delta_0||.                             (5.7)

Only the initial full classical product uses (4.4); all shorter products in the Duhamel sum use powers of B. The zero-started block output has norm at most C_0 L_q b^2<=r_b/2. Thus the q-step map preserves the radius-r_b extracted ball, and every intervening stage satisfies (5.6).

All constants are independent of the number of permitted blocks. For any finite history of n steps with compatible Q_0=R^n Q_n and Q_n>=N0, the argument can be repeated for every full q-block; a final partial block has the same intermediate bound. The initial class is assumed extracted and in (5.5). There are only finitely many available steps on any fixed starting torus. Uniformity as that starting torus grows does not assert an infinite trajectory on a fixed finite regulator.

## 6. Exact small representative selection closes the finite family budget

The preceding estimates are quotient estimates. At each finite stage they give an actual usable family, not merely an infinite class with a possibly uncontrolled finite winding remainder.

Indeed choose a representative E_j of x_j with norm within C_int b^2 of its finite quotient infimum. Then

    ||E_j||_(Q_j;a0,b)<=2 C_int b^2<epsilon_bar/2.      (6.1)

Such a representative exists by the definition of the finite quotient norm; an infimum need not be attained. It is holomorphic on the same full b ball, uses connected finite torus carriers with the same a0, and has exactly the same normalized total. For real classes one can make it real by the norm-nonincreasing conjugate average described in Section2. Its total gauge and spatial identities are unchanged.

Use this family as the next finite input. It lies strictly inside the actual family budget, so the common-domain integral, all inherited core/tail estimates and every Gaussian bound apply. Its raw total differs from that of any previously produced representative by a finite constant only. Lemma2.1 and Section7 show that replacing it changes no normalized local density and no next quotient output. Thus the choice causes NO accumulating approximation error. A fixed positive near-minimal tolerance at each stage is sufficient; a summable sequence of tolerances is unnecessary because the represented class is exact.

After the next finite integral, subtract beta_(j+1) times the ACTUAL finite reference, and again choose a small exactly equivalent representative. At q-block endpoints the sharper radius bound is available; at intermediate stages (6.1) suffices. Every generated quantum correction remains in the total. No unproved claim is made that the unmodified canonical cluster array itself has the small norm after indefinitely many steps.

This is stronger than taking a small representative only after an infinite-volume limit. There is no limiting argument in (6.1), and any winding contribution is already part of the finite normalized total whose norm was estimated by the finite classical and quantum arguments. The explicit finite classical relocalization is what permits (4.4), so an unproved disappearance of winding errors is not used.

The selection is existential in a finite Banach quotient. It is not a claimed computational algorithm for finding a minimizing family, nor a uniform bound for an unaltered original carrier assignment. Its exact equality and uniform norm are the properties needed for the present mathematical induction.

## 7. Raw normalization and the exact coupling update

Write a finite input density in the common local chart as

    Z_j exp[-gamma_j S_j+E_j,raw],    gamma_j=g_j^(-2).

Here Z_j includes every previously generated field-independent normalization. The exact chosen local macrostep has its known scalar normalization N_j and produces

    Z_j N_j exp[-gamma_j S_(j+1)+F_j,raw].             (7.1)

Let

    beta_out=beta_(j+1)([F_j,raw]),
    x_(j+1)=[F_j,raw]-beta_out[S_(j+1)],

and choose any allowed small representative E_(j+1) of this class. Because the reference vanishes at zero,

    F_j,raw(w)=beta_out S_(j+1)(w)
                       +E_(j+1),raw(w)+c_j,
    c_j=F_j,raw(0)-E_(j+1),raw(0).                     (7.2)

This equality holds on the entire common product domain. Therefore the EXACT scalar bookkeeping is

    gamma_(j+1)=gamma_j-beta_out,
    Z_(j+1)=Z_j N_j exp(c_j).                          (7.3)

If an input representative is replaced before integration, with E'_raw=E_raw+c, replace Z_j by Z_j exp(-c). These formulas keep the finite raw density unchanged. On real fields use the consistent real logarithm branches; constant multiples of 2pi i in another compatible convention would not change the exponentials. No bound or convergence of an extensive vacuum free energy is asserted.

If instead a coupling sequence is freely prescribed without satisfying (7.3), Sections3-6 still define and bound the corresponding projected local maps, but they do not describe repeated factorization of one unchanged physical density. Along the actual update (7.3), the amplitude estimates apply for as long as every resulting coupling stays in the proved weak range. They provide no drift sign or infinite-range containment.

Along (5.6), the unprojected map has norm at most

    [B_T C_int+C_F+L_quant C_int]b^2,
    L_quant=C_quant sup_j(g_j T_cut,j/b).

Consequently

    |gamma_(j+1)-gamma_j|
      <=C_beta[B_T C_int+C_F+L_quant C_int],            (7.4)

uniformly in the finite regulator. This is only a magnitude bound. For a prescribed finite number n of steps one can make the initial inverse coupling large enough to stay weak for those n steps by allowing the worst-case n times this bound. That does not impose a desired final coupling, prove averaged positive drift, or control an infinite physical trajectory. Comparing two trajectories whose couplings differ would also require a coupling-parameter comparison theorem, not supplied by the fixed-coupling input Lipschitz bound.

## 8. Precise conclusion and remaining boundary

For fixed geometry and a finite q, with b and the weak-coupling ceiling chosen in the stated order, the selected homogeneous finite local macrostep admits a uniform exact representative induction through every permitted finite sequence of q-blocks whose output periods remain above N0. At each stage the chosen connected family has norm O(b^2), at the SAME a0 and b; every intermediate actual Gaussian/input budget holds; all finite normalized total identities are exact; vacuum constants are compensated by (7.2)-(7.3). The q-block amplitude contraction is at most one half for equal prescribed coupling data.

This closes the previous finite REPRESENTATIVE-budget interface for this local scheme. It does not prove smallness of an untouched canonical array, identify the one-shot composite sector with sequential primitive sectors, supply large-field or mixed-history terms, or establish that these local germs represent every global Wilson history. Those interpretations require their own exact orbit-domain and measure identities. The local continuation and every original retained window remain precisely the ones used by the common-domain theorem.

A physical density trajectory must obey (7.3) and remain weak. Its ultraviolet tuning and beta drift, the other field sectors, vacuum limits, observables, nontriviality and continuum measure construction remain separate. No such conclusion follows solely from the finite representative induction proved here.
