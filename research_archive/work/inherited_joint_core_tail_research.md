# Inherited interactions on a common background domain: a joint-support lemma

17 October 2026. This note proves an abstract interaction estimate. Its application requires the composite macrostep and the rooted fluctuation family specified below; it does not assert those inputs or a quantum induction without their separate proofs.

## 1. Graphs, variables, and the core hypotheses

Work on a compatible finite periodic regulator. The input activity graph is Lambda_Q; the Gaussian integration graph and output background carrier graph are the same graph Lambda_G. Let pi:Lambda_Q -> Lambda_G have connected images of connected sets, fibers bounded by F, and compression

    |pi H| <= c0_old + c1_old |H|.

An old cell has at most D scalar input coordinates. The connected activities satisfy

    sup_i sum_(H contains i) exp(a0 |H|) ||E_H||_b <= epsilon,

where b is the old scalar-coordinate polydisc radius. Let xi be the real retained integration variables, restricted to their actual product of invariant link/color balls. No analytic continuation of this indicator is used. The bounds below are uniform over its restricted real values. The next background w ranges over a fixed complex product polydisc, which may have the same radius b.

For complex lambda with |lambda|<Lstar, let f_lambda(w,xi) be the actual old field inserted into E. For every H assume

    f_lambda|H = c_(H,lambda)(w,xi) + v_(H,lambda)(w,xi).

The core reads both w and xi only in a connected carrier K0(H) containing pi H. Require

    |K0(H)| <= c0+c1 |H|,
    K0(H) subset N_(h0)(pi H),
    ||c_(H,lambda)||_infinity <= b-m,    0<m<b.

For each old scalar input coordinate (i,alpha), assume a normally convergent strict family

    v_(H,lambda;i,alpha) = sum_X v_(H,lambda;i,alpha;X)(w_X,xi|K0(H)).

The family is holomorphic in lambda and w, measurable in xi, with the uniform bound

    sup_(H,i in H,alpha) sum_X
      exp[kappa tau({pi i} union X)] ||v_(H,lambda;i,alpha;X)|| <= s.

The coefficient may read xi only in K0(H); its only w-dependence is X. There is no requirement that it vanish at w=0. Finite local or constant terms can instead be put in the core. An empty X is permitted with the obvious zero joining cost. A larger vector-fiber norm with the maximum inside the support sum is a sufficient input. These are strict joint-support requirements, not pointwise locality bounds.

Use a deterministic support assignment independent of lambda. It is enough that all these bounds hold for every smaller closed lambda disk with constants no larger than those displayed.

## 2. Joint-support composition

Let B>=0 be a target exponent and delta>0. Set t=s/m. Suppose

    t<1,    B+delta <= kappa,
    c1 B + D log[1/(1-t)] <= a0.

Then the canonical core/tail expansion gives strict joint (w,xi) coefficients U_(K,lambda), with connected K in Lambda_G and

    sum_H E_H(f_lambda|H) = sum_K U_(K,lambda),
    ||U_lambda||_B :=
      sup_z sum_(K contains z) exp(B |K|) ||U_(K,lambda)||
      <= C_T epsilon,
    C_T = exp(B c0+delta h0) F S_delta,
    S_delta = sup_z sum_y exp[-delta d(z,y)].

The identity is a finite-regulator scalar identity. All constants are uniform over compatible volumes when the hypotheses are.

Proof: expand only in the tail around the bounded core. Multivariable Cauchy gives coefficient norm e_H m^(-|nu|). The Taylor coefficient reads (w,xi) only in K0(H). Each occurrence of a tail coefficient reads w on X and xi in that same K0(H). Attach each X by a deterministic minimizing Steiner graph to pi i in K0(H). Their union K with K0(H) is a strict joint carrier. If T is the sum of joining lengths, then

    |K| <= c0+c1|H|+T,
    z in K implies d(z,pi H) <= h0+T.

The anchored weight is therefore bounded by

    exp(B c0+delta h0) exp[-delta d(z,pi H)]
      exp(B c1 |H|) product_occurrences exp[(B+delta) tau].

The sum of the scalar multiindices costs exactly (1-t)^(-D|H|). Finally sum input roots using the fiber bound F and the old activity norm. The proof is identical as a positive majorant for measurable xi in the cutoff window. Uniform convergence on smaller closed w and lambda polydiscs gives holomorphy in those parameters. No Gaussian estimate has yet been used.

## 3. The fluctuation difference keeps its small factor

Assume Lstar>=2 and that f_0(w,xi)=f_0(w) is independent of xi. Use the same canonical expansion and carriers at every lambda, and define

    Q_K(w,xi)=U_(K,1)(w,xi)-U_(K,0)(w,xi).

Then

    sum_K Q_K =
      sum_H [E_H(f_1|H)-E_H(f_0|H)],
    ||Q||_B <= C_T epsilon/(Lstar-1).

Proof: U_lambda is holomorphic as a vector in the anchored activity Banach space. For 1<rho<Lstar, take its Cauchy integral on |lambda|=rho in that Banach space. The triangle inequality gives the n-th coefficient norm at most C_T epsilon rho^(-n). Equivalently, retain the Cauchy integral before the positive anchored sum and bound each integrand's whole anchored norm; do not sum separate carrier suprema over lambda and infer a bound from the supremum of an anchored sum. Let rho increase to Lstar and sum n>=1 at lambda=1. The lambda=0 family need not itself consist of individually xi-independent terms if a redundant decomposition was used, but its total is the fluctuation-independent background functional by the exact identity. It is cleaner, and possible in the intended construction, to choose the lambda=0 split independent of xi. Do not discard any lambda=0 term as a vacuum merely because it is independent of w.

Let q=C_T epsilon/(Lstar-1). Each grouped exponent obeys ||Q_K||<=q. Therefore the exact multipliers satisfy

    sup_z sum_(K contains z) exp(B |K|)
      || exp(Q_K)-1 || <= exp(q) q.

The actual multiplier used in the Gaussian theorem is

    chi_K(xi) [exp(Q_K)-1],

extended by zero outside the retained window on K. On the global retained window this replacement is exact. All additional source cutoff conditions must still be retained.

For the strict Gaussian theorem, choose

    B >= 4 + log Kcal_theta + kappa_G,

because a connected K has ell(K)=|K|-1. This pays its full overlap, density, and edge weight. If the baseline budget and exp(q)q are each at most one quarter of the Gaussian threshold, multiplier interpolation gives a connected-log difference bounded by

    4 C_out exp(q) q

in the Gaussian output norm. Both the precision and every other multiplier must already have strict w-support on this same graph. A separate theorem is needed to establish those hypotheses after stationary substitution.

## 4. How a fixed background domain could supply the inputs

Fix a primitive ordinary base ell and a macro ratio R=ell^s. Suppose the actual composite chart, its stationary branch, and its gauge transfer have been established. Write

    Vstar(w)=Vp(w)^u(w),
    f_lambda(w,xi)=
      (1/i) log[ exp(i Ad_(u(w)^-1) Phi_Vstar(w)(lambda g xi)) Vp(w) ].

The coupling is inside Phi. On a common small overlap, total gauge invariance of the inherited functional identifies this with its actual rooted insertion. At lambda=0, f_0=ap=(1/i)log Vp. This equality concerns the total functional, not individual E_H.

The desired stronger input is a joint rooted family on final unit cells with output maximum inside its support sum:

    ||ap||_(kappa,A;b) <= C_A b/R,
    ||f_lambda-ap||_(kappa,A;b,cutoff) <= C_R |lambda| g T,

where T denotes the retained link cutoff threshold, to distinguish it from the macro ratio R. In the second family the xi-dependence of each output root must be restricted to a fixed collar of that source R-block. The constant C_R is allowed to depend on the now fixed R, but neither bound may depend on the old refinement M or volume.

Choose R>=8 C_A. Then choose

    Lstar = b/(8 C_R g T) >= 2.

The absolute whole-family amplitude of f_lambda is at most b/4 on this disk. Every local truncation core has at most that amplitude, by an absolute family bound; pointwise cancellation of the full map is not enough. Hence one can take m=b/2 with room to spare.

Split the w-support family at distance ell_tail around each source root. The tail has norm at a weaker unit exponent bounded by

    (C_A b/R + C_R Lstar g T)
      exp[-c kappa ell_tail] <= (b/4) exp[-c kappa ell_tail].

Group source roots and target background cells by an independent odd J. A safe bound multiplies the tail family norm by J^d, with a fixed classical cardinal reserve paying the projection's O(|X|) term. The xi collar must be included in K0(H), as well as the projected w-core neighborhood. If ell_tail plus that fixed collar is less than J, this costs a fixed macro halo q_halo and h0. For instance a conservative coordinatewise two-neighbor halo has q_halo=5^d and h0=2d. The exact minimal halo is immaterial, but it must be established from the actual chart.

Using connected input-carrier compression by R,

    c0 <= q_halo 2^d,
    c1 <= q_halo 2^d/k_R,
    F=R^d.

The physical R may be chosen large enough that c1 B<a0/2, provided the pre-gauge constants were fixed at the primitive base before R. After R is fixed, choose J large and ell_tail proportional to log J to make

    D(J) log[1/(1-s/m)] <= a0/2,

with the actual input coordinate count D(J)=d dim(g) J^d. Even the larger safe count O(J^d R^d) is compatible with the exponential tail versus logarithmic ell_tail choice. This is finite-parameter consistency conditional on the displayed joint family, not its proof.

The resulting q has the useful size O_(R,J)(g T epsilon/b), on the same incoming and outgoing background ball b. New purely classical precision and multiplier families may use an independent fixed classical radius, chosen before b, and arbitrary finite classical support reserves. Thus an inherited radius need not be repeatedly substituted as the outer radius of every newly generated classical coefficient.

## 5. What remains before using this as a quantum step

The actual composite macrostep, the joint rooted family for f_lambda, strict stationary-substituted precision and base interactions, and the compatible gauge equality of the total inherited functional all require verification. In particular, pointwise bounds on f_lambda do not imply its required joint carrier decomposition. Nonvanishing follows only after all the Gaussian theorem's hypotheses and budgets have been met; finite-volume analyticity of the integral alone is insufficient.

Even with a common field domain, the resulting coefficient norm has a finite prefactor rather than a contraction. Vacuum and marginal extraction, coupling flow, large-field complements, mixed histories, and observables remain separate parts of the existence proof.
