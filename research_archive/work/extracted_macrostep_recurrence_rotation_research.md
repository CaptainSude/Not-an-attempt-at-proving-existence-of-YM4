# Exact reference transport and a conditional extracted macrostep recurrence

17 October 2026. Independent research derivation for audit. This separates an exact classical identity, a finite-block perturbation theorem, and the remaining coupling and finite-regulator interfaces. The later update incorporates the independently audited quantum_local_limit_research.md theorem: quantum quotient descent is an established input for the selected homogeneous local system, not an unresolved hypothesis of the present application. No output edit or compilation.

## 1. Actual reference family and normalization

Fix the primitive odd ratio ell, an allowed elementary macro ratio R=ell^s, and preceding depths M_j=M_0 R^j. Let S_M be the actual coupling-free homogeneous ordinary classical action: on a finite compatible regulator,

    S_M(D)=S_bare(U_M(D)),    S_M(1)=0,                  (1.1)

where U_M(D) is the selected ordinary constrained minimum from Notebook15. All references use the same trace normalization and count each unoriented plaquette once. In four dimensions the bare action is the plaquette sum without a physical scale prefactor. The coupling is outside S_M.

Let

    P_(M,R)(W)=M_ell^k U_(MR)(W),  M=ell^k,
    (T_(M,R) E)(W)=E(P_(M,R)(W)).                       (1.2)

This is the pre-root-gauge classical substitution. It does not include the fluctuation integration.

The exact identity already recorded in common_domain_macrostep_fragment.tex, equation cdm-background, is

    S_M(Vstar(W))=S_M(P_(M,R)(W))=S_(MR)(W).            (1.3)

Thus the reference family required below is supplied by the actual construction, rather than chosen only by its quadratic normalization.

Here is the independent comparison proof, including its domain qualification. Put U2=U_(MR)(W), D=M_ell^k U2, and U1=U_M(D). Both fields live on the same original fine oriented graph. In D-unit coordinates its spacing is 1/M; in W-unit coordinates it is 1/(MR). The physical potential of U1 changes by

    A1^W(x)=R A1(Rx),  ||A1^W||_(C1alpha)
                              <=C R^(2+alpha)||A1||_(C1alpha).

The prefix estimate gives ||log D/i||<=C_A||log W/i||/R. For fixed R, both U1 and U2 lie in the required comparison balls on a sufficiently small real W ball, uniformly in M and volume. Exact ordinary composition gives

    M_ell^k U1=D=M_ell^k U2,
    M_ell^(k+s) U1=W=M_ell^(k+s) U2.

The minimum at D gives S_bare(U1)<=S_bare(U2), and the minimum at W gives the reverse inequality. The two action sums are identical under the d=4 coordinate relabeling. This proves (1.3) on that real germ. Both sides are holomorphic on their specified connected common product domain. Their germ equality therefore continues to that domain. For R>C_A, the prefix angle bound maps the common b ball into itself, so this continuation does not require a new radius loss at each substitution. No assertion of a complex minimum is used.

The exact flat symbol of this reference is, in the positive-bond midpoint convention,

    q_M(p)=|p|^2 I-p p^T+O(|p|^4),                     (1.4)

with the uniform normalization proved in flat_covariance_decay_research.md Section10. Matching the classical Hessian to the actual constrained minimum gives beta(S_M)=1. This is more than ellipticity. The quotient reference bound is

    ||[S_M]||_(Q,b)<=C_S b^2,                          (1.5)

uniform in M on the stipulated small radii; activity_quotient_research.md Section5 obtains it from the fixed-outer-radius classical support estimate and the zero total linear jet.

For an infinite statement, fix a joint background/reference system supplied by the interaction compactness theorem and its common subsequence. Local convergence alone is not sufficient to pass extensive action values. The anchored connected bounds and summable-field continuity permit passing their vacuum-normalized values on compact W, and thus (1.3) in the quotient. All maps, references and compositions used in a finite block must belong to that joint system.

This proof does not apply to an arbitrary invariant reference with beta=1. In particular, using a new local Wilson plaquette reference at every scale is not justified by normalization alone: its substituted full nonlinear functional need not be the chosen next reference. Nor does this proof identify sequential quantum integrals with a one-shot integral.

## 2. Intermediate extractions cancel exactly in a classical block

Write Q_j for the invariant interaction quotient at stage j, with the fixed cell grouping J, radius b and carrier weight a. Different stages are identified only by their prescribed lattice rescalings. Let

    S_j=[S_(M_j)],  beta_j(S_j)=1,
    P_j=I-S_j beta_j,  T_j=T_(M_j,R).                   (2.1)

The operator P_j is a bounded projection onto ker beta_j. The quotient estimates give a uniform bound

    ||P_j||<=p:=1+C_beta C_S,                           (2.2)

independent of the final inner radius b, although p may depend on the fixed grouping, weights and color conventions. The factor b^(-2) in beta is cancelled by (1.5), not omitted.

By (1.3),

    T_j S_j=S_(j+1).

Consequently, for every x in Q_j,

    P_(j+1) T_j P_j x
      =P_(j+1) T_j x-beta_j(x) P_(j+1)S_(j+1)
      =P_(j+1) T_j x.                                 (2.3)

No identity beta_(j+1) T_j=beta_j is needed. Equation (2.3) is precisely the intertwining relation sufficient for the recurrence.

Define A_j=P_(j+1)T_j. Repeated use of (2.3) gives

    A_(j+q-1)...A_j
       =P_(j+q) T_(j+q-1)...T_j.                       (2.4)

On an extracted input one may append P_j to the right. The classical semigroup, valid on the fixed joint invariant system by the actual comparison theorem and summable-gauge identity, yields

    A_(j+q-1)...A_j P_j
       =P_(j+q) T_(M_j,R^q) P_j.                       (2.5)

The right side may use a newly justified connected representation. It need not equal the family generated by sequential support assignments coefficient by coefficient. Quotient equality is what licenses the estimate.

Under the explicit supported low-kernel and high-jet hypotheses in activity_quotient_research.md Section7,

    ||A_(j+q-1)...A_j|_(ker beta_j)||
       <=theta_q
       :=p^2 [C_low(J) R^(-q alpha)+6 C_high R^(-q)] .  (2.6)

The constants are uniform in preceding M_j; J and the elementary R are fixed before q. Choose a finite q making theta_q<=1/4. Then choose the common positive b to meet the direct R^q high-jet disk and all classical margins. The constants in (2.6) do not deteriorate merely because b is reduced. A one-step bound

    ||A_j||<=B,  B>=1,                                 (2.7)

follows from bounded classical transport and (2.2), uniformly in j. It may be large; no one-step contraction is asserted.

More generally, if T_j S_j differs from S_(j+1) by D_j, then the error in (2.3) is -P_(j+1)D_j beta_j. Its norm can contain b^(-2)||D_j|| and recur at every step. This identifies the actual obstruction for an incorrectly chosen reference. For the ordinary minimized reference, D_j=0 exactly.

## 3. The established local quantum map and its remainder

Use the quantum local-limit theorem on the same jointly chosen input-independent classical system, with its strict transport, precision, cutoff and interaction margins. That theorem constructs the limiting small-field map on the invariant quotient by canonical periodization and proves representative independence. It applies to the actual homogeneous local germ and its stated continuation, not to the full Wilson measure. Write its fixed-coupling form as

    F_j(x)=T_j x+G_j(x),                               (3.1)

where the fixed pivot and Gaussian determinant terms and the zero-input Gaussian logarithm are included in G_j. The coupling, threshold and classical saddle at stage j are held fixed when taking input differences. Assume on a common admissible quotient neighborhood

    ||P_(j+1)(G_j(x)-G_j(y))||<=nu ||x-y||,
    ||P_(j+1)G_j(0)||<=f,                              (3.2)

with nu,f uniform over the stages being considered.

The family-level estimate for the first line does not require equal low jets of x-y. Sections4--5 of high_jet_quantum_difference_research.md give, for the canonical Gaussian logarithm,

    ||G_j(E1)-G_j(E2)|| <= C_quant (g_j T_j/b)||E1-E2||. (3.3)

Here T_j in the scalar factor denotes the retained cutoff threshold, not the background substitution operator; below we write it as T_cut,j to avoid that collision. The determinants and base exponent are fixed and cancel in (3.3). The large interpolation disk is applied to the Gaussian exponent, not to an assumed large admissible input ball. Thus a possible projected constant is

    nu=p C_quant sup_j(g_j T_cut,j/b).                 (3.4)

The quotient proof uses compatible representatives without assuming a minimizing representative. On the quotient ball of radius epsilon_bar/4, choose covariant near-minimal representatives of y and x-y; the bounded periodization theorem permits covariance without norm loss. Their sum represents x and has norm at most 3epsilon_bar/4 plus an arbitrarily small slack. Both lie in the radius-epsilon_bar family domain. The quantum local-limit theorem passes the compatible family difference bound to the quotient by Fatou and the infimum. Its representative-independence proof uses exact equality of canonically periodized normalized totals, the actual finite integrals with their common branch, and local continuity of the strict Gaussian construction. It does not infer descent merely from compact-field equality.

From the actual common-domain bound at E=0 one has the candidate uniform forcing estimate

    f <= p [(C_Delta+C_det)b
            +2 S1(e^3 tau(T_cut,j)+exp(v_j) v_j)],
    v_j<=C_base(g_j T_cut,j^3+g_j T_cut,j+g_j^2 T_cut,j^2). (3.5)

For fixed geometric parameters and b>0, a fixed sufficiently large multiple of sqrt(log(1/g_j)) as threshold makes the bracket's Gaussian terms and nu tend to zero as g_j tends to zero. Shrinking b first reduces the determinant part. This crude estimate is sufficient for the fixed admissible-radius argument below; an O(b^2) zero-input estimate would be a useful stronger input, but is not assumed in this section.

Equality of infinite normalized totals on compact fields would not, on its own, identify finite-regulator exponentials on fluctuating configurations. The canonical periodization and Gaussian local-continuity theorems are the additional proved ingredients that discharge this issue for the selected local quotient map. Their full strict-domain and joint-system assumptions remain in force. Vacuum normalization is still tracked separately.

## 4. Finite-block perturbation theorem

Let

    Psi_j(x)=P_(j+1)F_j(x)=A_j x+H_j(x),
    H_j=P_(j+1)G_j.                                    (4.1)

The output lies in ker beta_(j+1). Assume the q-step linear products satisfy (2.6), the one-step bound (2.7), and (3.2). Every statement in this section concerns trajectories for which the maps are defined on the stipulated common neighborhood.

For two trajectories with the same prescribed couplings and other fixed step data, put delta_k=x_(j+k)-y_(j+k), with delta_0 in ker beta_j. Variation of constants gives exactly

    delta_q=A_(j+q-1)...A_j delta_0
        +sum_(k=0)^(q-1) A_(j+q-1)...A_(j+k+1)
             [H_(j+k)(x_(j+k))-H_(j+k)(y_(j+k))].       (4.2)

An empty product is the identity. The elementary estimate

    ||delta_k||<=(B+nu)^k||delta_0||

and the long-product improvement only for the first term give

    ||delta_q|| <=
       [theta_q+nu sum_(k=0)^(q-1) B^(q-1-k)(B+nu)^k]
                   ||delta_0||
     =[theta_q+(B+nu)^q-B^q]||delta_0||.                (4.3)

At nu=0 the sum formula is understood by continuity. A convenient weaker bound is

    Lip(Psi_(j+q-1)...Psi_j)
       <=theta_q+q nu (B+nu)^(q-1).                    (4.4)

There is no exponentially growing projection factor in the leading classical term. Such factors occur only in the finite perturbative sum, whose length q is fixed before the coupling is made small.

For a single trajectory, the elementary one-step inequality is

    ||Psi_j(x)|| <=(B+nu)||x||+f.                       (4.5)

Starting at zero, the q-step forcing is at most

    f sum_(l=0)^(q-1)(B+nu)^l.                         (4.6)

These inequalities are uniform in the initial stage if their hypotheses are uniform in preceding depth.

## 5. Explicit common-domain envelope

Here is a complete finite-block bookkeeping choice, including all intermediate steps. Let theta_q<=1/4, set K=B+1>=2, and choose

    0<=nu<=min(1, 1/[4q K^(q-1)]),
    Lq=sum_(l=0)^(q-1)K^l,
    r=epsilon_bar/(8K^q),
    f<=r/(2Lq).                                       (5.1)

Assume the quotient maps and their bounds are available on the ball of radius epsilon_bar/4; as noted in Section3 this leaves enough room to lift pairs into the family ball of radius epsilon_bar.

For ||x||<=r, induction using (4.5) gives, for 0<=k<=q,

    ||x_(j+k)|| <=K^k r+f sum_(l=0)^(k-1)K^l
                <=epsilon_bar/8+r/2
                <epsilon_bar/4.                      (5.2)

Thus every intermediate map stays within its admissible quotient neighborhood. The same applies to a trajectory starting at zero. Equations (4.4) and (5.1) give block Lipschitz constant at most 1/2. Comparing the block output with its zero-input output,

    ||Psi_(j+q-1)...Psi_j(x)||
        <=(1/2)||x||+f Lq<=r.                          (5.3)

Hence every q-step block preserves the radius-r extracted ball; all intervening stages remain in the larger admissible ball. Two such trajectories with identical prescribed couplings contract by at least 2^(-n) after n blocks.

Parameter order is finite and noncircular: fix the primitive geometry, R and J, then q from (2.6), then the common b including the R^q domain restrictions and the determinant forcing requirement in (3.5), and finally sufficiently weak couplings and their thresholds. The constants p,B,theta_q are independent of shrinking b. The radius r in (5.1) is chosen from a fixed epsilon_bar, not required to scale as b^2. The Gaussian thresholds can be chosen so that all the required bounds hold uniformly for 0<g_j<=g_0. For a chosen countable sequence of such parameters use the common local-limit system supplied by joint extraction. No O(b^2) force estimate is needed for this local quotient envelope.

One can state the more general radius criterion directly: if a q-step block has Lipschitz constant kappa<1, then a radius r is invariant provided

    f sum_(l<q)(B+nu)^l <=(1-kappa)r,                  (5.4)

and (4.5) places every intermediate state inside the common admissible domain.

### 5.1 The stronger quadratic envelope from one fixed outer radius

The independently audited quantum_zero_input_force_research.md supplies a stronger force input. Construct the zero-input map at a fixed outer radius rho after R,J, with the same actual thresholds T_cut(g), local charts, classical data and logarithm branch as its later restriction. Uniformly in M and weak g its connected family has outer norm at most H_*. For a semisimple group, global adjoint invariance makes the total linear jet zero. Removing the constant and linear jets coefficientwise changes no normalized class. Phase projection and restriction to b<=rho/2 give

    ||G_j(0)||_Q <= C_F b²,  C_F=2H_*/rho²,
    ||P_(j+1)G_j(0)||_Q <= C_0 b²,  C_0=p C_F.        (5.5)

The outer construction, rather than an unrelated redefinition at each radius, is essential. This result does not assert that the whole force is O(g²); the pivot and determinant corrections can persist as g tends to zero.

Keep theta_q<=1/4, K=B+1, Lq=sum_(l<q)K^l and the same bound on nu as in (5.1). Define

    K_amp=max(1,2 C_0 Lq),  r_b=K_amp b²,
    C_int=K^q K_amp+C_0 Lq.                            (5.6)

Choose b<=rho/2, meeting all direct R^q domain requirements, and so small that C_int b²<epsilon_bar/4. Finally choose the weak-coupling ceiling so that nu has the required bound and the strict two-input comparison budgets hold, in particular a_Q epsilon_bar<=eta_*/(128e).

Every intermediate stage starting in the radius-r_b extracted ball has norm at most C_int b². The q-step output at zero has norm at most C_0 Lq b²<=r_b/2. The block Lipschitz constant is at most 1/2, so the radius-r_b ball is invariant. These conclusions are uniform over the chosen weak sequence and preceding depths on the common system. Thus the envelope is O(b²), including its intermediate stages, not merely O(1) in the small inner radius.

For later bookkeeping let B_T bound the unprojected classical T_j and let L_quant bound the unprojected quantum Lipschitz constant, with p L_quant<=nu. Along this envelope,

    ||F_j(x_j)||_Q
        <=[B_T C_int+C_F+L_quant C_int]b².             (5.7)

Therefore the norm of beta gives a uniform O(1) bound on a single inverse-coupling increment. It supplies neither its sign nor a bound on the accumulated infinite drift.

## 6. Exact density extraction and the coupling boundary

The algebra above is not, by itself, a completed coupling flow. At stage j the actual density has the form

    exp[-gamma_j S_(j+1)+F_j(x)],  gamma_j=g_j^(-2).

The exact full-reference split is

    F_j(x)=beta_(j+1)(F_j(x)) S_(j+1)+Psi_j(x),

so preservation of that density requires

    gamma_(j+1)=gamma_j-beta_(j+1)(F_j(x)).             (6.1)

The sign follows from the displayed negative classical exponent. A freely prescribed coupling sequence need not satisfy (6.1). The projected amplitude estimates are valid uniformly for any weak sequence as operator estimates, and apply along an actual running trajectory if it is defined and stays in that weak regime. They do not make an arbitrary frozen sequence an exact representation of the same original measure.

For two trajectories whose couplings are separately updated by (6.1), the quantum maps differ also through their coupling and threshold parameters. The input Lipschitz estimate (3.2) holds at fixed coupling and does not bound those new differences. Consequently (4.3) is not a coupled-state contraction theorem. No sign or asymptotic-freedom conclusion follows from it.

On the admissible amplitude ball, the already known beta bound controls a single coupling increment,

    |gamma_(j+1)-gamma_j|
       <=C_beta b^(-2)||F_j(x)||_Q.                   (6.2)

For any fixed finite number of steps one can make the initial gamma large enough to retain positivity using a uniform right-hand bound. This elementary finite-time observation does not bound an infinite accumulated drift or prove that the physical trajectory remains weak.

The quotient discards field-independent totals. Any physical vacuum density needed for a measure construction must be tracked separately. Nothing in the projected recurrence supplies large-field terms, mixed histories, observable convergence or continuum measure consistency.

There is a further regulator distinction even if quantum descent has been established on a joint infinite system. A quotient infimum and a newly localized infinite representative do not automatically provide uniformly bounded actual finite-regulator intermediate families. A finite-history compatibility theorem with an explicit bound on those actual families cannot be iterated indefinitely merely by invoking (5.3). For a fixed finite q, crude canonical bounds and a further radius reduction may provide the needed finite history, but that is a separate construction. An infinite quotient envelope is not a regulator-uniform finite RG induction.

Finite extraction must use the actual finite reference S_(M,N), together with a specified finite coefficient functional beta_N converging to the infinite beta; the audited finite-volume Ward construction supplies one candidate cutoff-jet functional. One must not replace the actual finite reference by the exact periodization of an independently chosen infinite S_M. The exact finite classical action identity holds for the actual finite references, while passage of projected histories requires the separate beta_N and family compatibility statements.

## 7. Conclusion and exact remaining interfaces

The ordinary classical reference obeys the exact required identity T_j S_j=S_(j+1), already present in the actual common-domain factorization. Its normalization agrees with beta=1. Therefore intermediate full-reference extractions telescope; they do not destroy the classical finite-q contraction.

With the quantum local-limit theorem as an established input, Sections4--5 prove a contractive finite-block recurrence and common intermediate-domain amplitude envelope on the selected invariant infinite quotient. The actual Gaussian estimates provide its fixed-coupling Lipschitz and forcing bounds, and the zero-input force can be made small with the existing parameter order.

The unresolved issues are a controlled physical running-coupling trajectory, a regulator-uniform construction of actual finite intermediate families, and the remaining measure interfaces. The projection algebra and local quantum quotient descent are no longer among those missing steps. The conclusion is restricted to the homogeneous local germ and the selected joint classical system; it does not identify all regulator subsequences or complete a Yang--Mills measure construction.
