# Finite ultraviolet tuning from a leading averaged drift

17 October 2026. A conditional reduction for the actual finite local extraction maps. The activity induction, finite leakage control, parity remainder, and real-coupling continuity are already available. The remaining hypothesis below is a uniformly positive averaged drift for the actual finite leading determinant coefficients. This note does not assert that hypothesis.

## 1. Fixed induction data and the actual decrement

Use the finite local induction constants at fixed elementary ratio R, grouping J, radius b, and carrier exponent a0. Let q_a be its contraction block length, r_b=K_amp b^2 its endpoint radius, and C_int b^2 its intermediate bound. All references and beta_j are the actual finite reference-normalized ones. At stage j,

    d_j(g,x)=beta_(j+1)(F_(j,g)(x)),
    gamma_(j+1)=gamma_j-d_j(g_j,x_j),
    x_(j+1)=P_(j+1)F_(j,g_j)(x_j),  g_j=gamma_j^(-1/2).

Every x_j is extracted and belongs to the real subspace: its normalized total is real on real fields. Real positive couplings and the consistent real logarithm branches preserve this subspace, so every d_j is real. The finite induction works for any realized weak coupling sequence, as long as each period stays above its fixed threshold. Its initial class can be zero, as for the reference bare local action.

Write

    b0_j=beta_(j+1)(D_(M_j,R;N_(j+1))),

for the finite leading pivot/Gaussian correction. This number is independent of g and the inherited interaction; it depends on the actual classical data and finite regulator. Do not replace it by an independently chosen infinite coefficient.

The new finite leakage theorem, homogeneous in the input, gives

    |beta_(j+1)(T_j x_j)| <= C_int omega(N_min)

on the extracted envelope, where omega(K) tends to zero along the stated cofinal nested period family. The finite parity bound and the quantum input comparison give, uniformly on this envelope,

    |d_j(g,x_j)-b0_j|
      <= C_int omega(N_min)
         +C_par,beta [tau(T(g))+g^2 T(g)^6]
         +C_in,beta gT(g)/b.                           (1.1)

Here C_par,beta includes the outer-radius factor, and C_in,beta includes C_int and the finite beta bound. The inner b^2 remainder cancels beta's b^-2 norm. Formula (1.1) follows by splitting F=T+G, then G(x)=G(0)+[G(x)-G(0)]. No finite identity beta_out T=beta_in is asserted.

Thus any prescribed tolerance epsilon>0 can be achieved by choosing one period threshold and then a sufficiently weak coupling ceiling. The chosen constants are independent of the number of permitted steps. The finite-induction magnitude bound also supplies

    |d_j(g,x_j)| <= D_abs                              (1.2)

throughout that envelope, with D_abs independent of the history length and permitted regulators.

## 2. The sole additional drift hypothesis

Assume there are c>0 and C_fin>=0 such that, for every admissible stage interval in the contemplated finite regulator family,

    sum_(j=k)^(k+n-1) b0_j >= c n-C_fin.                (2.1)

It is enough to assume (2.1) for the block length chosen below and its block starting stages. No individual coefficient need be positive. The constants in this hypothesis must be independent of the old depth and of the permitted finite periods.

Choose a multiple q of q_a so that C_fin<=c q/4. Strengthen the period and coupling thresholds so that epsilon<=c/4 in (1.1). Then every q-step sequence of projected maps started in its endpoint ball, with any prescribed couplings in the weak range, obeys

    B_- <= sum_(j=k)^(k+q-1) d_j(g_j,x_j) <= B_+,
    B_-=c q/2>0,        B_+=q D_abs.                   (2.2)

The lower bound is c q-C_fin-q epsilon >= c q/2; the upper bound uses (1.2). Each consecutive q_a subblock preserves the endpoint ball, so the same C_int envelope applies inside the larger q block. A new high-degree endpoint estimate or a new field radius depending on q is unnecessary here: this is repetition of the already established quantum q_a blocks.

## 3. A continuous clipped recursion

Let Gamma_w=g_weak^(-2)>0 be the chosen weak threshold. For the purpose of a finite shooting argument only, extend the extraction recursion to every real scalar gamma by evaluating the map at

    g_eval(gamma)=max(gamma,Gamma_w)^(-1/2),

while keeping the un-clipped scalar update

    gamma_next=gamma-d_j(g_eval(gamma),x).

The activity update is the actual projected map at g_eval. This defines an auxiliary recursion, not a physical density when gamma<Gamma_w. Its input couplings always lie in the proved weak range. For an initial activity in the endpoint ball, every q_a block and every intermediate activity remains admissible by the finite induction, independently of the scalar gamma.

The joint real-coupling/quotient continuity theorem and continuity of max imply that every finite clipped recursion is continuous in its initial gamma. On a compact shooting interval, (1.2) bounds all intermediate scalars, so the evaluated positive couplings stay in a compact positive interval. No continuity theorem at g=0, no continuous representative selection, and no volume-uniform continuity modulus is needed.

Because (1.1) and (2.1) apply to every admissible realized weak sequence, the clipped recursion also satisfies the block decrement bounds (2.2).

## 4. Endpoint tuning theorem

Fix a positive integer m and a finite history of m q steps whose final period is above the chosen threshold, with all the cofinal-family compatibility conditions. Fix a terminal inverse coupling

    Gamma_* >= Gamma_w+q D_abs.                        (4.1)

Then some initial inverse coupling in

    [Gamma_*+m B_-, Gamma_*+m B_+]                     (4.2)

generates m q genuine, un-clipped local extraction steps and ends exactly at Gamma_*.

Proof. Start the clipped recursion with x_0=0, or any fixed real extracted class in the endpoint ball. Its final scalar is continuous in gamma_0. Summing (2.2) shows that at the left endpoint of (4.2) the final scalar is at most Gamma_*, and at the right endpoint it is at least Gamma_*. The intermediate value theorem gives a clipped trajectory ending at Gamma_*.

At every earlier q-block endpoint, summing its positive future block decrements gives

    Gamma_*+(m-k) B_-
       <= gamma_(kq)
       <= Gamma_*+(m-k) B_+ ,       0<=k<=m.            (4.3)

Inside a block, (1.2) implies

    gamma_(kq+r)>=gamma_(kq)-r D_abs
                 >=Gamma_*-q D_abs>=Gamma_w,
                 0<=r<=q.                             (4.4)

Consequently no clipping occurred on the selected trajectory. Its scalar and activity updates are the actual local extraction updates, its coupling stays weak, and it reaches the prescribed terminal value. Exact finite representative/vacuum compensation implements the same normalized local density at each step. This proves the claim.

The lower and upper bare-coupling bounds follow immediately:

    (Gamma_*+m B_+)^(-1/2)
       <=g_0<=(Gamma_*+m B_-)^(-1/2).

Thus this conditional construction tunes arbitrarily long finite ultraviolet histories to one fixed interacting weak endpoint, with bare coupling of order m^(-1/2). It does not establish uniqueness of the tuned initial value, consistency between different m, or convergence of the resulting measures.

## 5. Exact remaining mathematical input

The additional hypothesis is (2.1), for the actual finite determinant coefficients with their actual cutoff extraction. The established local activity estimates, parity, continuity and qualitative finite leakage do not prove it. A determinant cocycle can telescope its infinite counterpart, but a quantitative one-loop comparison and the finite-regulator error still need to supply (2.1).

The chosen horizons are multiples of q. This already supplies an unbounded ultraviolet subsequence if the drift hypothesis is established; no claim about every integer horizon is needed here. All conclusions concern the homogeneous local extraction trajectory and its stated density domains. Mixed and large-field histories, source estimates, a nontrivial continuum limit and reconstruction remain separate requirements for Yang--Mills existence.
