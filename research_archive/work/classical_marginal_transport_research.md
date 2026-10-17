# Exact preservation of the infinite Maxwell coefficient by classical transport

17 October 2026. Research proof for independent audit. This concerns the invariant INFINITE interaction quotient on one fixed joint classical background system. It does not assert exact preservation of the finite symmetric-cutoff coefficient beta_(M,N). The finite contraction and finite quantum recurrence do not require such a finite identity.

## 1. Statement and precise existing inputs

Fix the primitive ratio ell, the auxiliary grouping J and its activity exponent a0. Let Q_(M;b)^inv be the invariant analytic interaction quotient at current scale, with the same scalar-coordinate radius b and carrier exponent at every preceding homogeneous depth M. Its beta_M is the true infinite total-kernel Maxwell coefficient, with the fixed midpoint/color normalization. The actual homogeneous reference satisfies

    beta_M(S_M)=1,      ||S_M||_b<=C_S b^2,
    P_M=I-S_M beta_M,  ||P_M||<=C_ext(J).                (1.1)

Let T_(M,L) be the actual pre-gauge ordinary classical substitution. It is a bounded map of the invariant quotient on the stipulated common b domain for each admissible finite endpoint L. It obeys

    T_(M,L) S_M=S_(ML),                                (1.2)
    T_(MR,L) T_(M,R)=T_(M,RL).                         (1.3)

These are identities of normalized scalar interactions/classes, not of their chosen support assignments. They come from the actual minimum comparisons and the controlled gauge comparison. Their finite identities and their extension to every invariant infinite class are the previously audited classical semigroup and summable-gauge results.

The actual pre-gauge families satisfy the complete C^(1,alpha) estimates on one positive outer radius r_A independent of L, M and volume. In particular, after fixing any prescribed finite classical support reserve,

    sup_i sum_X exp[kappa tau({i} union X)+A|X|]
            ||a_(M,L;i,X)||_(complete C^(1,alpha);b)
       <=C_* b/L,             0<b<=r_A.                (1.4)

The maximum and gradient Hölder quotients of the whole output fiber are taken before the support sum. The families are coherent on overlapping collars. Fix J so 2(a0+1)/J<=kappa and A>=4(a0+1). The constants of (1.4), and of these budgets, are fixed before increasing L.

The claim is:

    beta_(MR)(T_(M,R)x)=beta_M(x)                     (1.5)

for every invariant quotient class x and every fixed admissible ratio R on the common domain. The equality is algebraic over complex scalars; reality is unnecessary.

We retain the fixed-joint-system qualification. To use arbitrarily large endpoints in the proof, enlarge a chosen finite or countable joint classical system by a further diagonal extraction for the countably many endpoint powers used below. Previously fixed limits are unchanged. The uniform radius r_A and the complete-field bounds permit this extension at one fixed b; no sequence b_L tending to zero is introduced. The identities (1.2)-(1.3) are then the corresponding identities on that joint system. This is not a claim of independence from every possible unrelated classical subsequence.

## 2. A quadratic-only spatial estimate at fixed b

Let y=P_M x. Its total first derivative is zero by global semisimple color invariance. The exact infinite Ward and hypercubic classification give for its Hessian kernel K2(y)

    Gamma_2^y(p)=O(|p|^4).                              (2.1)

Thus, after the fixed midpoint-to-tail phases, all anchored tail-coordinate momentum jets through degree three vanish. Fixed-order kernel estimates give

    ||K2(y)||_(exponential row,sigma(J))
                         <=C(J)b^(-2)||y||_b.          (2.2)

Here and below the bound can be obtained by an arbitrary almost-minimal representative of y and then taking the quotient infimum.

Define the scalar quadratic polynomial, initially on summable small fields,

    Q_y(A)=1/2 K2(y)[A,A].

For a compact coarse field w, its actual pre-gauge image a_(M,L)(w) decays exponentially and is summable by (1.4). Hence Q_y(a_(M,L)(w)) is well defined. The quadratic part of the repaired low-kernel spatial proof constructs a connected output family Q_(y,L) representing this entire substituted quadratic polynomial, with

    ||Q_(y,L)||_(a0,b)
          <=C_2(J) L^(-alpha)||y||_b,
                    L>=L0(J), 0<b<=r_A.               (2.3)

For clarity, this estimate has no high-degree field-scaling disk. Its proof uses only:

* the two-divided-difference factorization K2=d^- Htilde d^+ with sum Htilde=0;
* the exact identity

      Q_y(a)=1/2 sum_(x,r,rho,tau)
          [D_rho a(x)]^T Htilde_(rho,tau)(r)
                     [D_tau a(x+r)-D_tau a(x)];

* the coherent family bounds |Da|<=C b L^-2 and
  |Da(x+r)-Da(x)|<=C b L^(-2-alpha)|r|^alpha near the anchor;
* exponential far-displacement summation and the (JL)^4 anchor count.

They give (2.3) with constants fixed after J and before L. The map a_(M,L) is evaluated only at w in the original b ball. There is no substitution a_(M,L)(lambda w) with |lambda| proportional to L. Therefore neither b L<=constant nor a radius shrinking with L is required for (2.3).

The output family Q_(y,L) need not be invariant as a full nonlinear functional. This causes no difficulty. The selected Hessian moment defining beta extends as a bounded linear functional to every interaction quotient, invariant or not:

    |b_mom(Z)|<=C_beta(J)b^(-2)||Z||_b.                (2.4)

On invariant classes it is beta. Formula (2.4) is just a fixed second derivative and second spatial moment bound. Classification is needed to identify its physical meaning, not to prove that bound.

## 3. The quadratic substituted polynomial contains the whole output Hessian

Write a_L=a_(M,L). Since a_L(0)=0 and D Phi_y(0)=0, the chain rule gives

    D^2(Phi_y o a_L)(0)[u,v]
       =D^2 Phi_y(0)[Da_L(0)u,Da_L(0)v].               (3.1)

The possible term D Phi_y(0)[D^2a_L(0)(u,v)] is exactly zero. Field degrees at least three cannot contribute to degree two under a map vanishing at zero. The right side of (3.1) is also D^2(Q_y o a_L)(0). Consequently

    beta_(ML)(T_(M,L)y)=b_mom(Q_(y,L)).                (3.2)

The equality can first be checked on finitely supported variation directions by differentiating locally normally convergent series. The existing anchored kernel bounds justify the subsequent infinite spatial moment. No cancellation among high field degrees is assumed.

Equations (2.3)-(2.4) prove

    |beta_(ML)(T_(M,L)P_M x)|
       <=C(J)b^(-2)L^(-alpha)||P_M x||_b
       <=C(J)C_ext(J)b^(-2)L^(-alpha)||x||_b.          (3.3)

At FIXED b>0 the right side tends to zero as L tends through admissible endpoint powers to infinity. By exact reference transport (1.2),

    |beta_(ML)(T_(M,L)x)-beta_M(x)|
       <=C_m(J)b^(-2)L^(-alpha)||x||_b.               (3.4)

All preceding depths have the same bound. This is an asymptotic statement at this point; the next section turns it into an exact identity.

## 4. Semigroup comparison forces exact preservation

Fix an admissible finite R and x, and put z=T_(M,R)x. The same-radius bounded classical transport gives a finite constant B_R(J) with

    ||z||_b<=B_R(J)||x||_b.                            (4.1)

Apply (3.4) to z at preceding depth MR with endpoint L:

    |beta_(MRL)(T_(MR,L)z)-beta_(MR)(z)|
       <=C_m(J)b^(-2)L^(-alpha)||z||_b.                (4.2)

Apply (3.4) directly to x with endpoint RL:

    |beta_(MRL)(T_(M,RL)x)-beta_M(x)|
       <=C_m(J)b^(-2)(RL)^(-alpha)||x||_b.             (4.3)

The leading quantities on the left are equal by (1.3). Therefore

    |beta_(MR)(T_(M,R)x)-beta_M(x)|
       <=C_m(J)b^(-2)
             [B_R(J)L^(-alpha)+(RL)^(-alpha)]||x||_b.  (4.4)

The left side does not depend on L. Let L tend to infinity in the fixed joint system. This proves (1.5).

The proof needs no convergence of T_(M,L)x as L grows, no bound on the norm of the whole transported high-degree interaction uniform in L, and no assertion that its carrier assignment forms a semigroup. It needs only the bounded fixed-R map, exact scalar semigroup, and the quadratic-only estimate uniform in L.

## 5. Why the common domain does not secretly shrink in this argument

There are three different radius issues.

1. The pre-gauge map and complete C^(1,alpha) support theorem have a fixed primitive-scale outer radius independent of endpoint L. This follows from the full ML-refined ordinary minimizer and the prefix theorem; its output angle bound is C_A b/L.

2. The real two-minimum comparison at a particular large endpoint may initially require a smaller comparison germ because physical C^(1,alpha) norms change under scale relabeling. This does not shrink the analytic domain of the two sides of (1.2) or (1.3). On every finite-coordinate compact-field polydisc both scalar sides are holomorphic on the already specified common b ball. An equality on the nonempty smaller real germ extends to that connected domain. Infinite sums are normally convergent there by the anchored and summable-field estimates.

3. The high-jet norm contraction uses a disk |lambda|<L/(8C_A) and therefore imposes b L<=constant. That disk is not used anywhere in Sections2-4. Applying its radius restriction to this proof would be an unnecessary and invalid loss of the fixed-b limit.

For the countably many endpoints, choose b once below the outer radius and the fixed admissible R-domain. The long endpoints only improve the amplitude inclusion C_A b/L<b. Finite comparisons establish each required germ identity; the fixed-b continuation then establishes it where (4.2)-(4.3) are evaluated. A further diagonal extraction can include all those maps without changing the already chosen fixed-R system.

## 6. Consequences and explicit limitations

On this infinite invariant quotient,

    beta_(MR) T_(M,R)=beta_M,
    T_(M,R) P_M=P_(MR) T_(M,R).                       (6.1)

The second identity uses the exact reference transport as well. Thus an already extracted classical input remains extracted. In a notation where ell_M denotes the classical leakage beta_(MR)T_(M,R)|ker beta_M, that leakage is exactly zero. Any adapted-coordinate correction constructed solely to remove this leakage can be chosen zero for this actual infinite classical system. The more general adapted-coordinate theorem remains valid for other operator families.

For a fixed-coupling quantum map F=T+G,

    beta_(MR)(F(x))=beta_M(x)+beta_(MR)(G(x)).

In particular the inverse-coupling increment on an extracted input comes entirely from the quantum remainder.

Here the previously proved centered Gaussian parity estimate gives a concrete reduction. Keep the same fixed outer field radius rho and define D_M=Delta_M+Qdet_M. Its zero-input estimate, after removing total constant/linear sectors and restricting to b<=rho/2, is

    ||[G_(M,g,T)(0)-D_M]||_b
       <=(2 C_par/rho^2)b^2 [tau(T)+g^2 T^6].          (6.2)

For an extracted input ||x||_b<=C_int b^2, the input Lipschitz estimate gives

    ||G_(M,g,T)(x)-G_(M,g,T)(0)||_b
                   <=C_quant(gT/b) C_int b^2.         (6.3)

Apply ||beta_(MR)||<=C_beta(J)b^-2 to (6.2)-(6.3), and use (1.5). The result is

    |beta_(MR)(F_(M,g,T)(x))-beta_(MR)(D_M)|
       <=(2 C_beta C_par/rho^2)[tau(T)+g^2 T^6]
          +C_beta C_quant C_int(gT/b).                (6.4)

The original Maxwell coordinate is used, with no adapted correction. For an actual density trajectory gamma_next=gamma-beta(F), its leading inverse-coupling decrement is therefore beta_(MR)(D_M), with the stated vanishing error at fixed b and T=T(g). This identifies the remaining determinant/pivot coefficient; it supplies neither its sign, its value, its convergence with M, nor control of an infinite running trajectory.

The finite functional beta_(M,N) is a cutoff-jet ratio and is not the beta in (1.5). Its small Ward/moment errors and folded tails are nonzero at finite period. This proof does NOT show beta_(MR,N)T_(M,R,N)=beta_(M,RN), and it does not set finite classical leakage to zero. The finite reference telescope and finite contraction already work without such an equality. Exponentially small finite leakage, if desired, needs its own finite flat-kernel comparison.

The identity is for the selected jointly compatible infinite classical system. It does not prove independence of all background subsequences, global measure matching, observable convergence, or continuum existence.
